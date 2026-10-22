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


def flow(d, items, y, w=130, arrow=True, label_dy=26):
    n = len(items)
    gap = (640 - n * w) / (n + 1)
    for i, (piece, label) in enumerate(items):
        x = gap + i * (w + gap)
        d.piece(piece, x, y, w)
        d.text(label, x + w / 2, y + w * 0.75 + label_dy, size=16, weight=600)
        if arrow and i < n - 1:
            d.arrow(x + w + 4, y + w * 0.375, x + w + gap - 4, y + w * 0.375)


@design("NAV/estimating-height-and-distance-1")
def _(d):
    flow(d, [("footprints", "Count 100 paces"), ("overhand-knot", "Tie a knot"), ("notebook", "Tally in blocks"), ("note", "Total")], 60, w=120)
    caption(d, "Counts kept in blocks, so one missed step does not spoil the total.", 300)


@design("NAV/estimating-height-and-distance-2")
def _(d):
    d.piece("person-standing", 30, 110, 160)
    d.piece("tree", 390, 40, 240)
    d.line(130, 132, 520, 74, dash="9 7", width=3, color=BLUE)
    d.text("Fist fixes the angle", 235, 98, size=16, weight=600, fill=BLUE)
    d.arrow(130, 262, 520, 262, width=3)
    d.arrow(520, 262, 130, 262, width=3)
    d.text("Paced distance", 325, 292, size=17, weight=600)
    d.leader(70, 70, 112, 128)
    d.text("Eye", 46, 66, size=16, weight=600)
    d.arrow(380, 210, 380, 76, width=3)
    d.arrow(380, 76, 380, 210, width=3)
    d.text("Height?", 366, 150, size=16, weight=600, anchor="end")


@design("SEC/child-safety-in-a-crisis-1")
def _(d):
    d.piece("card", 30, 30, 290)
    d.leader(430, 92, 250, 98)
    d.text("Child's name", 440, 98, size=17, weight=600, anchor="start")
    d.leader(430, 140, 240, 130)
    d.text("Home address", 440, 146, size=17, weight=600, anchor="start")
    d.leader(430, 188, 240, 150)
    d.text("Contact number", 440, 194, size=17, weight=600, anchor="start")
    d.piece("child-standing", 60, 200, 130)
    d.text("Sealed card on the child's body,\nnot in a bag", 230, 270, size=17, weight=600, anchor="start")


@design("SEC/child-safety-in-a-crisis-2")
def _(d):
    d.piece("child-standing", 10, 90, 140)
    d.line(10, 120, 630, 120, dash="3 9", width=5)
    d.text("Child's reach", 330, 106, size=16, weight=600)
    d.piece("cabinet", 170, 140, 130)
    d.piece("lock", 215, 108, 60)
    d.text("Low cabinet:\nlock it", 235, 288, size=16, weight=600)
    d.piece("cord", 340, 170, 120)
    d.piece("caution", 380, 118, 50)
    d.text("Trailing cord:\ntie it up", 400, 288, size=16, weight=600)
    d.piece("shelf", 490, 130, 140)
    d.piece("candle", 530, 100, 60)
    d.text("Candle on a low shelf:\nmove it high", 560, 288, size=16, weight=600)


@design("SEC/child-safety-in-a-crisis-3")
def _(d):
    steps = [(40, 220, "Toddler\narm's length", "child-standing"), (230, 170, "School age\nin sight, named adult", "child-standing"), (420, 120, "Teenager\nagreed check-ins", "person-standing")]
    for x, y, label, piece in steps:
        d.rect(x, y + 20, 180, 316 - (y + 20), fill=CREAM, rx=10)
        d.piece(piece, x + 40, y - 70, 100)
        d.text(label, x + 90, y + 54, size=15, weight=600)
    caption(d, "Supervision loosens as age rises.", 348)


@design("SEC/child-safety-in-a-crisis-4")
def _(d):
    flow(d, [("child-standing", "Stay where\nyou are"), ("person-standing", "Find an adult in uniform\nor a police officer"), ("phone-call", "Ask for help")], 50, w=140)
    for i in range(3):
        d.badge(i + 1, 60 + i * 200, 40, 16)
    caption(d, "Staying still comes first, not searching.", 330)


@design("SEC/child-safety-in-a-crisis-5")
def _(d):
    d.piece("waypoint-pin", 40, 90, 90)
    d.text("Home", 85, 224, size=17, weight=600)
    d.piece("waypoint-pin", 510, 90, 90)
    d.text("Meeting point", 555, 224, size=17, weight=600)
    d.arrow(140, 140, 240, 140, width=4)
    d.piece("gate", 250, 70, 130)
    d.piece("caution", 300, 40, 44)
    d.text("Locked gate", 315, 190, size=16, weight=600)
    d.arrow(390, 140, 500, 140, width=4, dash="10 8")
    d.path("M150 190C190 280 450 280 500 190", stroke=BLUE, width=4, dash="10 8")
    d.text("Detour", 320, 276, size=17, weight=600, fill=BLUE)
    d.text("Route", 190, 124, size=16, weight=600)
    d.piece("timeline-marker", 20, 250, 100)
    d.text("Timed walk", 70, 340, size=15, weight=600)


@design("SEC/child-safety-in-a-crisis-6")
def _(d):
    d.piece("wall", 10, 40, 220)
    d.piece("child-standing", 180, 120, 150)
    d.text("Hand on the wall", 120, 258, size=17, weight=600)
    d.piece("person-standing", 350, 70, 150)
    d.text("Adult in view", 425, 258, size=17, weight=600)
    d.piece("flashlight", 480, 190, 150)
    d.arrow(580, 262, 580, 300, width=4)
    d.text("Torch pointing down", 560, 328, size=16, weight=600)


@design("TLS/basic-mechanics-1")
def _(d):
    items = [("jerrycan", "Fuel level"), ("tyre", "Tyre pressure"), ("battery", "Battery terminals"), ("bolt", "Fasteners tight")]
    flow(d, items, 40, w=120, arrow=False)
    for i in range(4):
        gap = (640 - 4 * 120) / 5
        x = gap + i * (120 + gap) + 60
        d.tick(x, 220, 14)
    d.piece("timeline-marker", 20, 250, 90)
    d.text("Before every start", 330, 300, size=18, weight=700)
    caption(d, "The check repeats at every start, not once a season.", 336)


@design("TLS/basic-mechanics-2")
def _(d):
    d.piece("tin", 215, 90, 210)
    d.piece("filter", 40, 20, 120)
    d.leader(170, 80, 262, 150)
    d.text("Filter", 100, 150, size=16, weight=600)
    d.piece("fuse", 480, 20, 120)
    d.leader(470, 80, 380, 150)
    d.text("Fuse", 540, 150, size=16, weight=600)
    chip(d, 100, 250, 150, 44, "Spark plug", size=16)
    d.leader(176, 240, 262, 200)
    chip(d, 540, 250, 150, 44, "Inner tube", size=16)
    d.leader(464, 240, 380, 200)
    caption(d, "Seal and date the case so spares stay findable.", 336)


@design("TLS/basic-mechanics-3")
def _(d):
    d.piece("jar", 200, 50, 240)
    d.line(200, 118, 440, 118, dash="9 7", color=RED, width=4)
    d.text("Upper mark", 470, 124, size=16, weight=600, anchor="start", fill=RED)
    d.line(200, 178, 440, 178, dash="9 7", color=RED, width=4)
    d.text("Lower mark", 470, 184, size=16, weight=600, anchor="start", fill=RED)
    d.arrow(320, 36, 320, 110, width=4)
    d.text("Insert the stick", 320, 28, size=16, weight=600)
    caption(d, "Read the level from the wiped tip.", 330)


@design("TLS/basic-mechanics-4")
def _(d):
    d.rect(40, 24, 560, 44, fill=INK, rx=8)
    for x, s in [(60, "Date"), (190, "Hours"), (320, "Task"), (470, "Notes")]:
        d.text(s, x, 53, size=17, weight=700, fill="#ffffff", anchor="start")
    for i in range(2):
        y = 68 + i * 56
        d.rect(40, y, 560, 56, fill=CREAM if i == 0 else PAPER, rx=0, width=2)
        for x in (60, 190, 320, 470):
            d.line(x, y + 34, x + 90, y + 34, color=SAND, width=4)
    d.arrow(60, 214, 580, 214, width=4)
    d.text("Read across a row to spot wear patterns", 320, 250, size=16, weight=600)
    caption(d, "Hours and task sit side by side.", 330)
