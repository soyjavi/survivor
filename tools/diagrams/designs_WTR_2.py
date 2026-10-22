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


@design("WTR/water-for-animals-1")
def _(d):
    d.piece("bucket", 50, 70, 180)
    d.text("Animal water", 140, 250, size=17, weight=600)
    d.piece("jerrycan", 410, 70, 180)
    d.text("Household tap", 500, 250, size=17, weight=600)
    d.piece("do-not", 285, 120, 70)
    caption(d, "Animals never draw from the family tank.", 320)


@design("WTR/water-for-animals-2")
def _(d):
    chip(d, 320, 50, 200, 48, "Shade cloth")
    d.piece("pan", 150, 150, 160)
    d.piece("bucket", 330, 110, 160)
    d.line(60, 270, 580, 270, width=3)
    d.text("Poultry drinker", 230, 305, size=16, weight=600)
    d.text("Goat trough", 410, 305, size=16, weight=600)
    caption(d, "Trough height depends on the animal.", 340)


@design("WTR/water-for-animals-3")
def _(d):
    chip(d, 160, 90, 200, 56, "Dry hay", size=18)
    chip(d, 480, 90, 200, 56, "Fresh grass", size=18)
    for i in range(3):
        d.piece("water-drop", 70 + i * 66, 160, 64)
    d.piece("water-drop", 450, 160, 64)
    d.text("Water needed", 320, 300, size=16, weight=600)
    caption(d, "Dry feed raises the water need.", 334)


@design("WTR/water-from-ice-and-snow-1")
def _(d):
    d.piece("pot-with-lid", 50, 50, 190)
    d.piece("flame", 100, 175, 90)
    d.piece("ice-cube", 300, 40, 90)
    d.arrow(340, 125, 235, 140, width=3)
    d.text("Snow added slowly", 250, 195, size=16, weight=600, anchor="start")
    d.text("Starter water", 145, 320, size=16, weight=600)
    chip(d, 500, 90, 190, 50, "Roadside snow")
    d.piece("do-not", 465, 120, 70)


@design("WTR/water-from-ice-and-snow-2")
def _(d):
    d.piece("ice-cube", 40, 60, 110)
    d.piece("ice-cube", 40, 170, 110)
    d.text("Layer 1", 95, 150, size=16, weight=600)
    d.text("Layer 2", 95, 262, size=16, weight=600)
    d.arrow(170, 180, 250, 180)
    d.piece("pot-with-lid", 260, 100, 160)
    d.arrow(450, 180, 500, 180)
    d.piece("water-drop", 505, 140, 80)
    d.text("Meltwater", 545, 250, size=16, weight=600)
    caption(d, "Thin layers melt faster and waste less fuel.", 332)


@design("WTR/water-from-ice-and-snow-3")
def _(d):
    chip(d, 320, 50, 180, 46, "Inside the tent")
    d.piece("bottle", 70, 110, 130)
    d.text("Lidded bottle", 135, 290, size=16, weight=600)
    d.piece("person-sitting", 420, 90, 170)
    d.arrow(410, 170, 220, 170)
    d.text("Body heat", 315, 150, size=16, weight=600)
    caption(d, "Meltwater stays near the body until boiled.", 335)


@design("WTR/water-from-ice-and-snow-4")
def _(d):
    d.piece("ice-cube", 40, 50, 170)
    d.piece("knife", 240, 60, 150)
    d.text("Trim", 315, 190, size=16, weight=600)
    d.tick(60, 250, 16)
    d.text("Clear ice", 86, 256, size=16, weight=600, anchor="start")
    d.cross(60, 295, 16)
    d.text("Cloudy", 86, 301, size=16, weight=600, anchor="start")
    d.arrow(410, 110, 460, 110)
    d.piece("pot-with-lid", 465, 50, 150)
    d.text("Melt", 540, 190, size=16, weight=600)


@design("WTR/water-with-broken-pipes-1")
def _(d):
    chip(d, 110, 120, 160, 56, "Main shut-off")
    d.badge(1, 110, 60)
    d.arrow(200, 120, 320, 120)
    d.piece("tap", 330, 70, 130)
    d.badge(2, 395, 60)
    d.text("Drain tap", 460, 128, size=16, weight=600, anchor="start")
    d.piece("bucket", 345, 190, 110)
    d.text("Bucket", 400, 310, size=16, weight=600)
    d.text("Close first", 110, 190, size=16, weight=600)


@design("WTR/water-with-broken-pipes-2")
def _(d):
    d.line(40, 160, 600, 160, width=14)
    chip(d, 320, 160, 130, 44, "Rubber patch", fill=YELLOW)
    chip(d, 215, 90, 120, 40, "Hose clamp", size=15)
    chip(d, 425, 90, 120, 40, "Hose clamp", size=15)
    d.line(240, 110, 245, 148, width=2)
    d.line(400, 110, 395, 148, width=2)
    d.text("Crack", 320, 230, size=16, weight=600)
    d.leader(320, 214, 320, 184)
    chip(d, 130, 280, 160, 44, "Clean metal", size=15)
    d.tick(235, 280, 16)
    chip(d, 450, 280, 100, 44, "Grit", size=15)
    d.cross(520, 280, 16)


@design("WTR/water-with-broken-pipes-3")
def _(d):
    d.piece("barrel", 40, 40, 170)
    d.text("Tank", 125, 30, size=16, weight=600)
    d.piece("rock", 60, 200, 80)
    d.text("Sediment", 100, 300, size=16, weight=600)
    d.piece("tap", 180, 130, 120)
    d.text("Drain tap", 255, 120, size=16, weight=600)
    d.arrow(310, 200, 420, 200)
    d.piece("bucket", 440, 120, 150)
    d.text("Bucket", 515, 260, size=16, weight=600)
    d.text("First flush: most debris", 440, 320, size=16, weight=600, anchor="middle")


@design("WTR/water-with-broken-pipes-4")
def _(d):
    d.line(40, 170, 600, 170, width=8)
    for i, x in enumerate((140, 260, 380)):
        d.piece("waypoint-pin", x - 30, 100, 60)
        d.text(f"Joint {i + 1}", x, 220, size=16, weight=600)
    d.piece("caution", 470, 80, 80)
    d.text("Repair", 510, 190, size=16, weight=600)
    chip(d, 140, 50, 150, 44, "Gauge low")
    caption(d, "Low reading: check every joint.", 320)


@design("WTR/well-water-safety-1")
def _(d):
    d.piece("well", 60, 70, 170)
    d.piece("slope", 240, 110, 150)
    d.piece("waste-pit", 450, 110, 150)
    d.arrow(240, 280, 400, 280, width=3)
    d.arrow(400, 280, 240, 280, width=3)
    d.text("Distance", 320, 310, size=16, weight=600)
    d.text("Cover", 145, 60, size=16, weight=600)
    d.text("Slope away", 315, 100, size=16, weight=600)
    d.text("Waste pit", 525, 100, size=16, weight=600)


@design("WTR/well-water-safety-2")
def _(d):
    rows = ["Cover", "Distance from waste", "Apron", "Drainage slope", "Test"]
    for i, s in enumerate(rows):
        y = 24 + i * 60
        d.rect(120, y, 400, 48, fill=CREAM, rx=10)
        d.text(s, 150, y + 31, size=17, weight=600, anchor="start")
        d.tick(490, y + 24, 14)


@design("WTR/well-water-safety-3")
def _(d):
    d.arrow(70, 280, 600, 280, width=3)
    d.arrow(70, 280, 70, 40, width=3)
    d.text("Level", 76, 36, size=16, weight=600, anchor="start")
    d.text("Time", 600, 308, size=16, weight=600, anchor="end")
    d.path("M 90 70 L 260 210", stroke=INK, width=4)
    d.path("M 260 210 L 430 90", stroke=INK, width=4)
    d.line(70, 240, 590, 240, dash="9 7", width=3, color=RED)
    d.text("Low level", 590, 262, size=16, weight=600, anchor="end", fill=RED)
    d.text("Pumping", 150, 205, size=16, weight=600, anchor="start")
    d.text("Rest", 440, 140, size=16, weight=600, anchor="start")
