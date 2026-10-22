import glob
import os
import re
import sys

from elements import ELEMENTS_DIR, index_elements

CELL = re.compile(r'<div class="cell"><(svg[^>]*)>(.*?)</svg><span>', re.S)
LABEL = re.compile(r'aria-label="([^"]+)"')


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def extract(boards_dir):
    existing = set(index_elements())
    added = []
    for path in sorted(glob.glob(os.path.join(boards_dir, "*.dc.html"))):
        board = os.path.basename(path)[: -len(".dc.html")].lower()
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        for match in CELL.finditer(html):
            name = slug(LABEL.search(match.group(1)).group(1))
            if name in existing:
                continue
            target = os.path.join(ELEMENTS_DIR, board)
            os.makedirs(target, exist_ok=True)
            svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 120">{match.group(2)}</svg>'
            with open(os.path.join(target, f"{name}.svg"), "w", encoding="utf-8") as fh:
                fh.write(svg)
            existing.add(name)
            added.append(f"{board}/{name}")
    return added


if __name__ == "__main__":
    for item in extract(sys.argv[1]):
        print(item)
