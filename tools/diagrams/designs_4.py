from dg import *

DESIGNS = {}


def design(key):
    def wrap(fn):
        DESIGNS[key] = fn
        return fn
    return wrap


def caption(d, s, y=340):
    d.text(s, 320, y, size=15, fill="#4a4238")


def chip(d, cx, cy, w, h, s, size=16, fill=CREAM, weight=600, color=INK):
    d.rect(cx - w / 2, cy - h / 2, w, h, fill=fill, rx=12)
    lines = s.split("\n")
    y0 = cy + size * 0.35 - (len(lines) - 1) * size * 0.6
    d.text(s, cx, y0, size=size, weight=weight, fill=color)


@design("HYG/body-washing-with-little-water-1")
def _(d):
    d.piece("person-standing", 30, 30, 190)
    d.piece("cloth", 40, 230, 120)
    d.text("Clean cloth", 100, 330, size=16, weight=600)
    steps = ["Face, neck and arms", "Chest and back", "Legs and feet", "Genitals last"]
    for i, s in enumerate(steps):
        y = 70 + i * 66
        d.badge(i + 1, 300, y, 20)
        d.text(s, 336, y + 6, size=18, weight=600, anchor="start")
    d.arrow(590, 60, 590, 290, width=4)
    d.text("Clean to\ndirty", 590, 316, size=14, weight=600)


@design("HYG/body-washing-with-little-water-2")
def _(d):
    d.piece("person-standing", 155, 10, 330)
    pts = [("Armpits", 150, 92, 288, 84, "end"), ("Under the breasts", 150, 150, 306, 98, "end"), ("Groin", 500, 150, 336, 131, "start"), ("Between the toes", 500, 220, 330, 219, "start")]
    for label, lx, ly, px, py, anchor in pts:
        d.leader(lx + (10 if anchor == "end" else -10), ly - 6, px, py)
        d.text(label, lx, ly, size=17, weight=600, anchor=anchor)
    caption(d, "Folds, not open skin, are where rashes start: dry them fully.", 334)


@design("HYG/body-washing-with-little-water-3")
def _(d):
    chip(d, 150, 60, 230, 70, "Sweat and dirt stay", size=17)
    chip(d, 490, 60, 230, 70, "Folds stay damp", size=17)
    chip(d, 490, 230, 230, 70, "Rash forms", size=17)
    chip(d, 150, 230, 230, 70, "Scratching opens skin\nto bacteria", size=17)
    d.arrow(270, 60, 366, 60)
    d.arrow(490, 98, 490, 192)
    d.arrow(366, 230, 270, 230)
    d.arrow(150, 192, 150, 98)
    d.piece("do", 300, 6, 40)
    d.text("Dry the folds: breaks the loop", 320, 128, size=15, weight=700, fill=GREEN)
    caption(d, "Drying is the cheapest point to break the loop.", 330)


@design("HYG/body-washing-with-little-water-4")
def _(d):
    cards = [("jerrycan", "Two litres in\na marked jug"), ("cloth", "Two cloths\nper person"), ("towel", "One towel for\ndrying only"), ("fabric", "Clean clothes\nfolded ready")]
    for i, (piece, label) in enumerate(cards):
        cx = 170 + (i % 2) * 300
        cy = 90 + (i // 2) * 160
        d.rect(cx - 140, cy - 62, 280, 128, fill=CREAM, rx=12, width=2)
        d.piece(piece, cx - 130, cy - 48, 100)
        d.text(label, cx - 10, cy - 8, size=16, weight=600, anchor="start")
        d.tick(cx + 118, cy + 42, 12)
    caption(d, "Everything is set aside before washing starts.", 340)


@design("PSY/asking-for-help-1")
def _(d):
    d.rect(100, 14, 440, 330, fill=CREAM, rx=14)
    d.rect(100, 14, 440, 52, fill=INK, rx=14)
    d.text("Request", 130, 48, size=20, weight=700, fill="#ffffff", anchor="start")
    rows = ["Problem", "Help needed and urgency", "What I can offer", "Name"]
    for i, s in enumerate(rows):
        y = 84 + i * 62
        d.text(s, 130, y + 24, size=18, weight=600, anchor="start")
        d.line(130, y + 40, 510, y + 40, color=SAND, width=4)


@design("PSY/asking-for-help-2")
def _(d):
    labels = [["Pause", "Choose person", "Say request"], ["Repeat back", "Record", "Follow up"]]
    for r, row in enumerate(labels):
        y = 70 + r * 130
        for i, s in enumerate(row):
            cx = 110 + i * 210
            chip(d, cx, y, 150, 64, s, size=17, fill=CREAM if (r, i) != (1, 2) else YELLOW)
            d.badge(r * 3 + i + 1, cx - 66, y - 26, 13)
            if i < 2:
                d.arrow(cx + 80, y, cx + 130, y)
    d.path("M530 102V135H110V150", width=4)
    d.arrow(110, 140, 110, 164)
    d.path("M530 232V290H30V70H34", stroke=SAND, width=4, dash="10 8")
    d.arrow(30, 70, 34, 70, color=SAND)
    d.text("If nothing arrives, ask again", 320, 316, size=15, weight=600)


@design("PSY/asking-for-help-3")
def _(d):
    d.piece("ladder", 20, 30, 180, 240)
    rows = ["Family and neighbours", "Clinic or health post", "Police", "Local authority"]
    for i, s in enumerate(rows):
        y = 22 + i * 76
        chip(d, 410, y + 30, 300, 60, s, size=18)
        d.badge(i + 1, 245, y + 30, 14)
    d.arrow(590, 40, 590, 280, width=4)
    caption(d, "Move down only when the level above fails.", 346)


@design("PSY/asking-for-help-4")
def _(d):
    d.piece("person-standing", 20, 60, 130)
    d.piece("person-standing", 490, 60, 130)
    d.piece("bucket", 255, 20, 130)
    d.arrow(170, 150, 470, 150, width=4)
    d.text("Water", 320, 176, size=17, weight=600)
    d.piece("hammer", 255, 190, 130)
    d.arrow(470, 280, 170, 280, width=4)
    d.text("Tools", 320, 312, size=17, weight=600)
    d.text("Thanks", 80, 300, size=17, weight=700)
    caption(d, "Help is a loop that returns.", 346)


@design("PSY/asking-for-help-5")
def _(d):
    d.rect(100, 14, 440, 330, fill=CREAM, rx=14)
    d.rect(100, 14, 440, 52, fill=INK, rx=14)
    d.text("Before you finish", 130, 48, size=20, weight=700, fill="#ffffff", anchor="start")
    rows = ["Problem", "Urgency", "Source contacted", "Thanks given", "Request note"]
    for i, s in enumerate(rows):
        y = 84 + i * 50
        d.tick(135, y + 22, 14)
        d.text(s, 165, y + 28, size=18, weight=600, anchor="start")
        d.line(340, y + 34, 510, y + 34, color=SAND, width=4)
