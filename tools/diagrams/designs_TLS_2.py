from dg import *

DESIGNS = {}


def design(key):
    def wrap(fn):
        DESIGNS[key] = fn
        return fn
    return wrap


def caption(d, s, y=340):
    d.text(s, 320, y, size=15, fill="#4a4238")


def chip(d, cx, cy, w, h, s, size=16, fill=CREAM, weight=600, color=INK, dash=None):
    d.rect(cx - w / 2, cy - h / 2, w, h, fill=fill, rx=12, dash=dash)
    lines = s.split("\n")
    y0 = cy + size * 0.35 - (len(lines) - 1) * size * 0.6
    d.text(s, cx, y0, size=size, weight=weight, fill=color)


GX = [195, 321, 445]
GY = [99, 176, 255]


def grid(d):
    d.piece("table-grid", 70, -10, 500, 375)


def put(d, name, col, row, w=80):
    d.piece(name, GX[col] - w / 2, GY[row] - w * 0.375, w)


@design("TLS/sharpening-a-knife-1")
def _(d):
    d.arrow(60, 100, 270, 100, width=4)
    d.text("Heel to tip", 165, 85, size=16, weight=600)
    d.piece("knife", 50, 70, 230)
    chip(d, 165, 225, 260, 50, "Stone")
    d.piece("bracket", 330, 110, 110)
    d.text("15 to 20 degrees", 450, 165, size=17, weight=600, anchor="start")
    caption(d, "Hold the angle through each stroke.")


@design("TLS/sharpening-a-knife-2")
def _(d):
    d.piece("knife", 40, 50, 220)
    d.piece("coin", 105, 148, 70)
    chip(d, 160, 270, 270, 46, "Stone")
    d.leader(190, 70, 130, 126)
    d.text("Spine", 200, 66, size=17, weight=600, anchor="start")
    d.leader(430, 170, 178, 192)
    d.text("Coin", 440, 176, size=17, weight=600, anchor="start")
    d.arrow(430, 250, 320, 250, width=4)
    d.text("Angle", 440, 256, size=17, weight=600, anchor="start")
    caption(d, "The same coin repeats the same angle.")


@design("TLS/sharpening-a-knife-3")
def _(d):
    xs = [70, 250, 430]
    labels = ["Heel", "Middle", "Tip"]
    for i, x in enumerate(xs):
        d.badge(i + 1, x + 70, 50)
        d.piece("knife", x, 70, 140)
        d.arrow(x + 5, 190, x + 135, 190, width=4)
        d.text(labels[i], x + 70, 225, size=16, weight=600)
    chip(d, 320, 275, 540, 46, "Stone")
    d.leader(560, 318, 540, 296)
    d.text("Burr on far edge", 540, 336, size=16, weight=600, anchor="end")


@design("TLS/sharpening-a-knife-4")
def _(d):
    d.piece("knife", 40, 40, 190)
    chip(d, 320, 190, 60, 190, "Steel", size=16)
    d.arrow(250, 100, 250, 270, width=3)
    d.arrow(390, 270, 390, 100, width=3)
    d.text("Left", 250, 300, size=16, weight=600)
    d.text("Right", 390, 300, size=16, weight=600)
    d.piece("bracket", 470, 130, 100)
    d.text("Fixed angle", 520, 260, size=16, weight=600)
    caption(d, "Alternate sides, steel upright.")


@design("TLS/sharpening-an-axe-or-hatchet-1")
def _(d):
    d.line(190, 90, 360, 180, width=5)
    d.line(190, 270, 360, 180, width=5)
    d.piece("bracket", 40, 135, 110)
    d.text("Angle", 90, 112, size=17, weight=600)
    d.leader(480, 90, 290, 135)
    d.text("Bevel", 490, 96, size=17, weight=600, anchor="start")
    d.leader(480, 180, 366, 180)
    d.text("Edge", 490, 186, size=17, weight=600, anchor="start")
    d.piece("file", 150, 262, 90)
    d.arrow(270, 300, 360, 258, width=4)
    d.text("File stroke", 480, 296, size=16, weight=600, anchor="start")
    caption(d, "Match the bevel to the angle.")


@design("TLS/sharpening-an-axe-or-hatchet-2")
def _(d):
    d.piece("shelf", 400, 70, 170)
    d.piece("axe", 250, 20, 190)
    d.piece("hand", 250, 160, 80)
    d.arrow(150, 260, 390, 260, width=4)
    d.text("Push", 275, 290, size=16, weight=600)
    d.leader(140, 80, 370, 90)
    d.text("Head", 130, 86, size=17, weight=600, anchor="end")
    d.leader(140, 150, 290, 150)
    d.text("Handle", 130, 156, size=17, weight=600, anchor="end")
    caption(d, "Push firmly, do not swing.")


@design("TLS/tool-storage-1")
def _(d):
    grid(d)
    put(d, "knife", 0, 0)
    put(d, "saw", 1, 0)
    put(d, "hammer", 0, 1)
    put(d, "axe", 1, 1)
    chip(d, GX[2], GY[1], 84, 60, "Empty", size=15, dash="6 5")
    put(d, "caution", 2, 0, 56)
    d.text("Missing\ntool", 530, 175, size=16, weight=600, anchor="start")
    caption(d, "One place per tool.")


@design("TLS/tool-storage-2")
def _(d):
    grid(d)
    for i, t in enumerate(["Cutting", "Fastening", "Measuring"]):
        d.text(t, GX[i], 44, size=16, weight=600)
    put(d, "knife", 0, 0)
    put(d, "saw", 0, 1)
    put(d, "hammer", 1, 0)
    caption(d, "One tray per job.")


@design("TLS/tool-storage-3")
def _(d):
    grid(d)
    put(d, "knife", 0, 0)
    put(d, "saw", 1, 0)
    put(d, "axe", 0, 2)
    put(d, "hammer", 1, 2)
    d.arrow(540, 70, 540, 270, width=4)
    d.text("Heavy", 540, 300, size=16, weight=600)
    caption(d, "Weight sets height.")


@design("TLS/tool-storage-4")
def _(d):
    chip(d, 320, 32, 150, 34, "Month", size=16)
    grid(d)
    for i, t in enumerate(["Handles", "Blades", "Fasteners"]):
        d.text(t, 118, GY[i] + 6, size=16, weight=600, anchor="end")
        d.piece("do", GX[2] - 25, GY[i] - 25, 50)
    d.piece("timeline-axis", 100, 285, 440, 100)


@design("TLS/using-a-multitool-1")
def _(d):
    d.piece("multitool", 260, 90, 220)
    d.leader(130, 80, 296, 150)
    d.text("Blade", 120, 76, size=17, weight=600, anchor="end")
    d.leader(130, 170, 300, 190)
    d.text("Pliers", 120, 176, size=17, weight=600, anchor="end")
    d.leader(130, 280, 310, 230)
    d.text("Screwdriver", 120, 286, size=16, weight=600, anchor="end")
    d.arrow(560, 90, 440, 140, width=4)
    d.text("Lock", 565, 86, size=17, weight=600, anchor="start")
    caption(d, "One lock check covers all.")


@design("TLS/using-a-multitool-2")
def _(d):
    d.piece("multitool", 60, 90, 200)
    d.piece("sheath", 360, 90, 200)
    d.arrow(270, 170, 350, 170, width=4)
    d.leader(90, 70, 130, 130)
    d.text("Locking blade", 50, 62, size=16, weight=600, anchor="start")
    d.leader(300, 290, 200, 220)
    d.text("Pliers", 310, 296, size=17, weight=600, anchor="start")
    d.piece("caution", 400, 40, 60)
    d.text("Lock first", 470, 66, size=16, weight=600, anchor="start")
    caption(d, "Lock engages before it goes in.")


@design("TLS/using-a-multitool-3")
def _(d):
    d.piece("pliers", 200, 80, 200)
    d.line(100, 125, 540, 125, width=4)
    d.text("Wire", 550, 131, size=16, weight=600, anchor="start")
    d.leader(195, 56, 280, 104)
    d.text("Jaw tip", 185, 52, size=16, weight=600, anchor="end")
    d.leader(435, 56, 322, 112)
    d.text("Cutting edge", 445, 52, size=16, weight=600, anchor="start")
    d.arrow(150, 235, 222, 235, width=3)
    d.arrow(450, 235, 378, 235, width=3)
    d.leader(300, 280, 300, 160)
    d.text("Hinge", 300, 304, size=16, weight=600)
    caption(d, "Cut at the tip.")


@design("TLS/using-a-multitool-4")
def _(d):
    d.piece("pliers", 30, 90, 190)
    d.piece("line-solid", 215, 135, 80)
    d.arrow(300, 160, 580, 160, width=4)
    d.text("Flight path", 440, 120, size=16, weight=600)
    d.piece("do-not", 420, 125, 70)
    d.piece("hand", 250, 220, 80)
    d.tick(350, 262, 18)
    d.text("Hand clear", 380, 268, size=16, weight=600, anchor="start")
    caption(d, "The cut end flies off.")