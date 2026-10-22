import glob
import importlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from dg import D
from elements import ROOT

PREVIEW_SIZE = 700


def load_designs():
    designs = {}
    for path in sorted(glob.glob(os.path.join(HERE, "designs_*.py"))):
        module = importlib.import_module(os.path.basename(path)[:-3])
        for key, fn in module.DESIGNS.items():
            if key in designs:
                raise ValueError(f"duplicate design {key} in {os.path.basename(path)}")
            designs[key] = fn
    return designs


def render(key, fn):
    d = D(key)
    fn(d)
    return d.svg()


def target_path(key):
    section = key.split("/")[0]
    name = key.split("/")[1]
    return os.path.join(ROOT, "assets", section, f"{name}.svg")


def build(prefix=None, preview=None):
    designs = load_designs()
    written = []
    for key, fn in sorted(designs.items()):
        if prefix and not key.startswith(prefix):
            continue
        path = target_path(key)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(key, fn))
        written.append(path)
        if preview:
            os.makedirs(preview, exist_ok=True)
            subprocess.run(["qlmanage", "-t", "-s", str(PREVIEW_SIZE), "-o", preview, path], capture_output=True)
    return written


def parse_args(argv):
    prefix = None
    preview = None
    args = list(argv)
    while args:
        arg = args.pop(0)
        if arg == "--preview":
            preview = args.pop(0)
        else:
            prefix = arg
    return prefix, preview


if __name__ == "__main__":
    prefix, preview = parse_args(sys.argv[1:])
    written = build(prefix, preview)
    print(f"built {len(written)} diagrams")
