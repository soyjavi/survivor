import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ELEMENTS_DIR = os.path.join(ROOT, "assets", "elements")


def index_elements():
    return {os.path.basename(path)[:-4]: path for path in glob.glob(f"{ELEMENTS_DIR}/*/*.svg")}


def element_body(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    inner = re.sub(r"^.*?<svg[^>]*>", "", text, count=1, flags=re.S)
    return re.sub(r"</svg>\s*$", "", inner)


def scope_ids(body, prefix):
    body = re.sub(r'id="([^"]+)"', lambda m: f'id="{prefix}{m.group(1)}"', body)
    return re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{prefix}{m.group(1)})", body)
