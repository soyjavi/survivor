import glob
import os
import re
import sys
import unittest
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build
from elements import ROOT

IMAGE = re.compile(r"^!\[[^\]]*\]\(assets/([^)/]+)-(\d+)\.svg\)$")
MARKER = "> @svg "
PENDING_FILE = os.path.join(HERE, "pending.txt")


def scan_documents():
    linked = {}
    pending = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "documents", "*", "*.md"))):
        section = path.split(os.sep)[-2]
        doc = os.path.basename(path)[:-3]
        position = 0
        with open(path, encoding="utf-8") as fh:
            for line in fh.read().split("\n"):
                image = IMAGE.match(line)
                if image and image.group(1) == doc:
                    position = int(image.group(2))
                    linked[f"{section}/{doc}-{position}"] = path
                elif line.startswith(MARKER):
                    position += 1
                    pending[f"{section}/{doc}-{position}"] = line[len(MARKER):].strip()
    return linked, pending


class DiagramTests(unittest.TestCase):
    def setUp(self):
        self.designs = build.load_designs()
        self.linked, self.pending = scan_documents()

    def test_every_design_renders_valid_svg(self):
        for key, fn in self.designs.items():
            ET.fromstring(build.render(key, fn))

    def test_every_design_is_linked_from_a_document(self):
        self.assertEqual(sorted(set(self.designs) - set(self.linked)), [])

    def test_every_linked_diagram_has_a_design(self):
        self.assertEqual(sorted(set(self.linked) - set(self.designs)), [])

    def test_built_files_match_designs(self):
        stale = []
        for key, fn in self.designs.items():
            path = build.target_path(key)
            if not os.path.exists(path):
                stale.append(key)
                continue
            with open(path, encoding="utf-8") as fh:
                if fh.read() != build.render(key, fn):
                    stale.append(key)
        self.assertEqual(stale, [])

    def test_pending_list_matches_documents(self):
        with open(PENDING_FILE, encoding="utf-8") as fh:
            listed = {line.split("\t")[0] for line in fh.read().split("\n") if line}
        self.assertEqual(listed, set(self.pending))

    def test_pending_markers_have_no_design(self):
        self.assertEqual(sorted(set(self.pending) & set(self.designs)), [])


if __name__ == "__main__":
    unittest.main()
