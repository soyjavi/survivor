from dg import *

DESIGNS = {}


def design(key):
    def wrap(fn):
        DESIGNS[key] = fn
        return fn
    return wrap


def caption(d, s, y=340):
    d.text(s, 320, y, size=15, fill="#4a4238")


@design("WTR/boiling-water-1")
def _(d):
    for i, (extra, label) in enumerate([("flame", "Heat"), ("waves", "Small bubbles"), ("water-drop", "Rolling boil")]):
        x = 45 + i * 200
        d.piece("pot-with-lid", x, 24, 150, 112)
        d.badge(i + 1, x + 12, 40, 15)
        d.piece(extra, x + 33, 142, 84, 63)
        d.text(label, x + 75, 232, size=17, weight=600)
        if i < 2:
            d.arrow(x + 156, 82, x + 196, 82)
    d.rect(60, 262, 520, 62, fill=CREAM)
    d.text("The 1-minute timer starts at the full rolling boil,\nnot at first heat.", 320, 288, size=16)


@design("WTR/boiling-water-2")
def _(d):
    d.line(40, 140, 200, 140, dash="10 8", color=GREY, width=4)
    d.arrow(200, 140, 604, 140, width=5)
    d.text("Warming\nclock not running", 92, 100, size=16, fill="#4a4238")
    d.circle(200, 140, 13, fill=YELLOW)
    d.text("Rolling boil", 200, 98, size=17, weight=600)
    d.path("M200 178V192H320V178", width=3)
    d.text("1 min", 260, 220, size=17, weight=600)
    d.path("M200 238V252H462V238", stroke=RED, width=3)
    d.text("3 min above 2,000 m", 331, 280, size=17, weight=600, fill=RED)
    caption(d, "The clock never runs while the water is still warming.", 334)


@design("WTR/boiling-water-3")
def _(d):
    d.arrow(30, 190, 612, 190, width=5)
    stages = [("Cold", 0), ("First bubbles", 2), ("Rising bubbles", 4), ("Rolling boil", 7)]
    for i, (label, bubbles) in enumerate(stages):
        cx = 100 + i * 150
        d.piece("pot-with-lid", cx - 65, 24, 130, 97)
        d.line(cx, 124, cx, 178, dash="5 6", width=2)
        d.circle(cx, 190, 12, fill=YELLOW)
        d.text(label, cx, 228, size=16, weight=600)
    caption(d, "Small bubbles are not a boil. Large volumes take longest to reach the rolling stage.", 328)


@design("WTR/boiling-water-4")
def _(d):
    rows = [
        [("pot-with-lid", "Fill"), ("flame", "Heat, lid on"), ("step-box", "Time the boil")],
        [("cup", "Cool, lid on"), ("jerrycan", "Store"), ("document", "Note fuel used")],
    ]
    n = 0
    for r, row in enumerate(rows):
        y = 18 + r * 170
        for i, (piece, label) in enumerate(row):
            x = 45 + i * 200
            d.piece(piece, x, y, 150, 112)
            n += 1
            d.badge(n, x + 12, y + 14, 15)
            d.text(label, x + 75, y + 140, size=17, weight=600)
            if i < 2:
                d.arrow(x + 156, y + 56, x + 196, y + 56)


@design("FIR/ash-and-fire-cleanup-1")
def _(d):
    d.piece("water-drop", 265, 4, 110)
    d.leader(190, 50, 270, 56)
    d.text("Water", 180, 56, size=17, weight=600, anchor="end")
    d.arrow(320, 96, 320, 150, color=BLUE, width=5)
    d.piece("coals", 200, 130, 240)
    d.leader(190, 190, 280, 232)
    d.text("Grey crust\nover the embers", 180, 186, size=17, weight=600, anchor="end")
    d.piece("bracket", 450, 196, 110)
    d.text("Cooled layer", 580, 266, size=17, weight=600)
    caption(d, "A grey surface does not mean cold underneath.", 330)


@design("FIR/ash-and-fire-cleanup-2")
def _(d):
    for cx, piece, label in [(120, "bucket", "Water"), (320, "tin", "Scoop"), (520, "pot-with-lid", "Lidded metal bin")]:
        d.piece(piece, cx - 75, 30, 150, 112)
        d.text(label, cx, 176, size=17, weight=600)
    d.rect(60, 206, 520, 76, fill=CREAM)
    d.tick(96, 236, 13)
    d.text("Warm ash goes into metal", 122, 242, size=16, weight=600, anchor="start")
    d.cross(96, 266, 13)
    d.text("Never into plastic or paper", 122, 272, size=16, weight=600, anchor="start")
    caption(d, "Also bring a long shovel and heat gloves.", 322)


@design("FIR/ash-and-fire-cleanup-3")
def _(d):
    d.piece("hand", 255, 10, 130)
    d.piece("coals", 200, 105, 240)
    d.leader(470, 60, 392, 70)
    d.text("Hand just above", 480, 66, size=17, weight=600, anchor="start")
    d.leader(470, 150, 346, 156)
    d.text("Heat rising", 480, 156, size=17, weight=600, anchor="start")
    caption(d, "Feel the heat from close above. Do not touch the ash.", 340)


@design("FIR/ash-and-fire-cleanup-4")
def _(d):
    d.piece("house", 8, 90, 180)
    d.text("House wall", 98, 270, size=16, weight=600)
    d.piece("pot-with-lid", 250, 130, 140)
    d.text("Lidded metal bin", 320, 270, size=16, weight=600)
    d.piece("shrub", 470, 96, 160)
    d.text("Dry grass", 550, 270, size=16, weight=600)
    for x1, x2 in [(192, 248), (392, 468)]:
        c = (x1 + x2) / 2
        d.arrow(c, 190, x2, 190, color=RED)
        d.arrow(c, 190, x1, 190, color=RED)
    d.text("Keep well away", 320, 56, size=18, weight=600, fill=RED)
    caption(d, "Warm ash must sit away from anything that can burn.", 330)


@design("FIR/ash-and-fire-cleanup-5")
def _(d):
    d.arrow(30, 190, 612, 190, width=5)
    stages = [("coals", "Hissing\nstops"), ("water-drop", "Ash stirred\nand wet"), ("hand", "Cold to the back\nof the hand"), ("sun", "Rechecked\nafter hours")]
    for i, (piece, label) in enumerate(stages):
        cx = 100 + i * 150
        d.piece(piece, cx - 52, 40, 104, 78)
        d.line(cx, 122, cx, 164, dash="5 6", width=2)
        d.badge(i + 1, cx, 190, 20)
        d.text(label, cx, 238, size=16, weight=600)
    caption(d, "Cold comes last, not first.", 334)


@design("SHL/building-a-lean-to-1")
def _(d):
    d.piece("lean-to", 170, 80, 290)
    for x in (260, 300, 340, 380, 415):
        end = 149 + 80 - 70 + (x - 229) * 0.51 - 12
        d.arrow(x, end - 64, x, end, color=BLUE, width=3)
    d.text("Rain", 215, 74, size=17, weight=600, fill=BLUE)
    d.leader(100, 150, 232, 168)
    d.text("Ridge pole", 90, 150, size=17, weight=600, anchor="end")
    d.leader(520, 112, 330, 215)
    d.text("Roof layers", 530, 112, size=17, weight=600, anchor="start")
    d.piece("flame", 480, 190, 90)
    d.text("Open front", 525, 290, size=17, weight=600)
    caption(d, "Water sheds top to bottom and never pools on the cover.", 340)


@design("SHL/building-a-lean-to-2")
def _(d):
    labels = ["Ridge pole\non supports", "Uprights", "Roof layers\nbottom up", "Waterproof\ncover"]
    for i, label in enumerate(labels):
        cx = 100 + i * 147
        d.badge(i + 1, cx, 60, 28)
        d.text(label, cx, 118, size=16, weight=600)
        if i < 3:
            d.arrow(cx + 36, 60, cx + 111, 60)
    d.piece("lean-to", 205, 160, 230)
    caption(d, "Each layer overlaps the one below.", 344)


@design("SHL/building-a-lean-to-3")
def _(d):
    d.piece("lean-to", 170, 60, 300)
    d.piece("person-sitting", 218, 175, 110)
    d.curve_arrow("M255 150C225 130 225 100 250 70", (250, 70), -1.0, color=RED)
    d.text("Gap at the top\nof the back wall", 140, 90, size=16, weight=600)
    d.leader(200, 110, 240, 120)
    caption(d, "The vent sits high so warm moist air escapes above the sleeper.", 342)
