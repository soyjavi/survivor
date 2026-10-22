import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build

ROOT = build.ROOT
GOOD = "---\nid: WTR-01\ntype: guide\ntitle: T\ndescription: d\nsection: WTR\ntags: [a]\ntimestamp: 2026-10-20\norigin: generated\nreview: pending\n---\n\n# T\n\nbody\n"


def check(text, section="WTR"):
    return build.check_document(os.path.join(ROOT, "documents", section, "x.md"), text)


class BuildTests(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        build.build()

    def test_service_worker_version_ignores_build_time(self):
        build.build()
        first = open(os.path.join(build.OUT, "sw.js")).read().splitlines()[0]
        time.sleep(1.1)
        build.write_version(1)
        build.write_service_worker()
        second = open(os.path.join(build.OUT, "sw.js")).read().splitlines()[0]
        self.assertEqual(first, second)

    def test_valid_document_passes(self):
        self.assertEqual(check(GOOD), [])

    def test_empty_link_target_is_rejected(self):
        self.assertTrue(any("empty link" in e for e in check(GOOD + "\nSee [Other](#).\n")))

    def test_missing_image_is_rejected(self):
        self.assertTrue(any("missing image" in e for e in check(GOOD + "\n![a](assets/nope-1.svg)\n")))

    def test_section_mismatch_is_rejected(self):
        self.assertTrue(any("section" in e for e in check(GOOD, "FIR")))

    def test_key_order_is_enforced(self):
        swapped = GOOD.replace("type: guide\ntitle: T\n", "title: T\ntype: guide\n")
        self.assertTrue(any("frontmatter keys" in e for e in check(swapped)))

    def test_pinned_commit_is_used(self):
        env = dict(os.environ, SURVIVOR_COMMIT="abc1234")
        code = "import sys, json; sys.path.insert(0, %r); import build; build.write_version(1); print(open(build.OUT + '/version.json').read())" % HERE
        out = subprocess.run([sys.executable, "-c", code], env=env, capture_output=True, text=True).stdout
        self.assertEqual(json.loads(out)["commit"], "abc1234")

    def test_all_documents_are_valid(self):
        errors = []
        for md in glob.glob(os.path.join(ROOT, "documents", "*", "*.md")):
            errors += build.check_document(md, open(md, encoding="utf-8").read())
        self.assertEqual(errors, [])

    def test_every_section_closes_with_warning(self):
        bad = []
        for md in glob.glob(os.path.join(ROOT, "documents", "*", "*.md")):
            last = open(md, encoding="utf-8").read().rstrip().splitlines()[-1]
            if not last.startswith("**Warning:**"):
                bad.append(os.path.relpath(md, ROOT))
        self.assertEqual(bad, [])

    def test_reader_only_fetches_okf_documents(self):
        html = open(os.path.join(ROOT, "web", "reader.html"), encoding="utf-8").read()
        self.assertIn("okf\\/[A-Z]{3}\\/[a-z0-9-]+\\.md", html)


if __name__ == "__main__":
    unittest.main()
