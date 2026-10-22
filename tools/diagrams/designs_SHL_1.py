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


def lab(d, s, x, y, anchor="middle", size=16):
    d.text(s, x, y, size=size, weight=600, anchor=anchor)


def flow4(d, labels, pieces):
    w, gap = 120, 36
    x0 = (640 - 4 * w - 3 * gap) / 2
    for i, (p, s) in enumerate(zip(pieces, labels)):
        x = x0 + i * (w + gap)
        d.piece(p, x, 100, w)
        lab(d, s, x + w / 2, 224)
        if i < 3:
            d.arrow(x + w + 4, 145, x + w + gap - 4, 145)


@design("SHL/building-a-snow-trench-1")
def _(d):
    d.piece("snow-cave", 190, 70, 230)
    d.arrow(30, 215, 205, 215)
    d.piece("arrow-curved", 400, 80, 100)
    d.piece("vent-hole", 490, 130, 110)
    lab(d, "Entrance tunnel", 115, 250)
    lab(d, "Vent hole", 545, 250)
    caption(d, "Cold air enters low, warm air leaves high.")


@design("SHL/cold-weather-shelter-1")
def _(d):
    d.piece("snow-cave", 180, 40, 280)
    d.piece("person-sitting", 235, 130, 110)
    d.arrow(60, 90, 60, 220)
    lab(d, "Cold air sinks", 60, 250, size=15)
    d.piece("arrow-curved", 450, 30, 90)
    d.piece("vent-hole", 530, 20, 90)
    lab(d, "Vent hole", 575, 120)
    d.leader(190, 300, 280, 212)
    lab(d, "Sleeping platform", 180, 322, anchor="end")


@design("SHL/cold-weather-shelter-2")
def _(d):
    flow4(d, ["Mark outline", "Dig", "Roof with\nthick snow", "Vent last"], ["step-1", "step-2", "step-3", "step-box"])
    caption(d, "The vent comes after the roof is complete.", 300)


@design("SHL/debris-hut-1")
def _(d):
    d.piece("hut", 150, 40, 290)
    d.piece("person-sitting", 225, 140, 100)
    d.arrow(300, 320, 300, 252, color=BLUE)
    lab(d, "Wind", 320, 300, anchor="start")
    d.leader(120, 288, 283, 234)
    lab(d, "Entrance", 120, 312, anchor="end")
    lab(d, "Leaf insulation", 560, 90, anchor="end")
    d.leader(470, 100, 375, 135)
    lab(d, "Under sleeper", 610, 300, anchor="end")
    d.leader(500, 290, 380, 246)


@design("SHL/drying-clothes-and-gear-in-shelter-1")
def _(d):
    d.piece("tent", 20, 80, 230)
    d.line(300, 100, 300, 250, width=5)
    lab(d, "Clothing line", 300, 80)
    d.rect(440, 120, 170, 150, fill="none", stroke=RED, rx=14)
    d.piece("flame", 480, 150, 90)
    lab(d, "Heat zone", 525, 108)
    d.arrow(235, 175, 420, 175, color=BLUE)
    lab(d, "Airflow", 360, 160)
    d.arrow(300, 295, 440, 295, width=3)
    d.arrow(440, 295, 300, 295, width=3)
    lab(d, "Gap", 370, 322)


@design("SHL/emergency-bed-1")
def _(d):
    d.piece("log-stack", 155, 150, 120)
    d.piece("log-stack", 380, 150, 120)
    d.piece("ground-line", 60, 205, 520, 50)
    d.piece("leaf", 185, 112, 100)
    d.piece("leaf", 275, 112, 100)
    d.piece("leaf", 365, 112, 100)
    d.piece("bracket", 290, 173, 60, 62)
    lab(d, "Air gap", 352, 212, anchor="start", size=15)
    lab(d, "Logs", 140, 212, anchor="end")
    d.leader(148, 206, 190, 206)
    lab(d, "Boughs", 320, 95)
    caption(d, "The frame lifts the sleeper above the cold ground.")


@design("SHL/emergency-bed-2")
def _(d):
    xs = [60, 260, 460]
    for x, p, s, n in zip(xs, ["bedding", "sleeping-mat", "fabric"], ["Bedding", "Base", "Waterproof sheet"], [1, 2, 3]):
        d.piece(p, x, 90, 130)
        lab(d, s, x + 65, 220)
        d.badge(n, x + 20, 90)
    d.arrow(200, 150, 255, 150)
    d.arrow(400, 150, 455, 150)
    caption(d, "Stored together and dry, the bed can be rebuilt quickly.", 290)


@design("SHL/emergency-shelter-in-a-vehicle-1")
def _(d):
    d.piece("car", 180, 100, 280)
    d.piece("do-not", 140, 195, 70)
    lab(d, "Exhaust clear", 140, 310, anchor="middle")
    d.arrow(360, 50, 360, 182, color=GREEN)
    lab(d, "Fresh air", 360, 40)
    d.arrow(60, 80, 190, 140, color=BLUE)
    lab(d, "Wind", 50, 70, anchor="start")


@design("SHL/heating-without-power-1")
def _(d):
    x0, y0, w, h = 40, 60, 186, 150
    for c in range(3):
        d.rect(x0 + c * w, y0, w, h, fill="#fbe3b8" if c == 1 else CREAM, rx=4)
    d.piece("flame", x0 + w + 48, y0 + 30, 90)
    d.piece("caution", x0 + 60, y0 + 40, 65)
    d.piece("caution", x0 + 2 * w + 60, y0 + 40, 65)
    lab(d, "Cold room", x0 + 0.5 * w, y0 + h + 28)
    lab(d, "Warm room", x0 + 1.5 * w, y0 + h + 28)
    lab(d, "Cold room", x0 + 2.5 * w, y0 + h + 28)
    for c in (1, 2):
        d.line(x0 + c * w, y0 + 30, x0 + c * w, y0 + 120, width=8, color=BLUE)
    d.leader(300, 300, x0 + w, y0 + 110)
    lab(d, "Draught stopper", 310, 320, anchor="start")


@design("SHL/heating-without-power-2")
def _(d):
    d.piece("stove", 30, 100, 170)
    d.piece("wall", 260, 30, 120, 150)
    d.line(168, 111, 400, 111, width=8)
    d.piece("arrow-curved", 400, 56, 90)
    d.piece("log-stack", 60, 210, 110)
    lab(d, "Stove", 115, 100)
    lab(d, "Flue", 222, 98)
    lab(d, "Fuel store", 115, 310, size=15)
    caption(d, "Smoke leaves through the flue; fuel stays dry.")


@design("SHL/hot-weather-shelter-1")
def _(d):
    d.piece("cloth", 170, 0, 300)
    d.piece("tarp-a-frame", 200, 175, 240)
    d.piece("bracket", 140, 150, 60, 80)
    lab(d, "Canopy", 560, 86, anchor="start")
    d.leader(552, 80, 440, 90)
    lab(d, "Air gap", 150, 195, anchor="end")
    lab(d, "Tarp", 560, 295, anchor="start")
    d.leader(552, 289, 420, 285)
    d.piece("arrow-curved", 470, 120, 90)

@design("SHL/hot-weather-shelter-2")
def _(d):
    d.piece("tent", 20, 80, 220)
    d.piece("sleeping-mat", 300, 135, 130)
    d.piece("person-sitting", 310, 100, 110)
    d.arrow(250, 150, 480, 150, color=BLUE)
    d.piece("cloth", 490, 100, 110)
    lab(d, "Open sides", 130, 70)
    lab(d, "Thin mat", 365, 240)
    lab(d, "Wet cloth", 545, 230)


@design("SHL/hot-weather-shelter-3")
def _(d):
    d.piece("sun", 30, 20, 110)
    d.piece("jar", 290, 113, 130)
    d.piece("rock", 280, 160, 150)
    d.arrow(140, 70, 260, 130, color=YELLOW)
    d.piece("do-not", 165, 95, 55)
    d.piece("cloth", 480, 140, 110)
    lab(d, "Shade", 355, 300)
    lab(d, "Lid", 470, 100, anchor="start")
    d.leader(465, 94, 378, 129)
    lab(d, "Wet cloth", 535, 280)


@design("SHL/keeping-warm-while-sleeping-1")
def _(d):
    rows = [("blanket", "Top cover", 3, 10), ("bedding", "Bedding", 2, 90), ("sleeping-mat", "Ground insulation", 1, 170)]
    for p, s, n, y in rows:
        d.piece(p, 230, y, 130)
        d.badge(n, 215, y + 55)
        lab(d, s, 380, y + 60, anchor="start")
    d.piece("ground-line", 190, 240, 300, 60)
    d.arrow(100, 60, 100, 270)
    lab(d, "Heat leaves down", 100, 305, size=15)


@design("SHL/keeping-warm-while-sleeping-2")
def _(d):
    d.piece("person-sitting", 245, 40, 150)
    d.piece("ground-line", 190, 190, 260, 50)
    d.arrow(320, 160, 320, 290)
    lab(d, "Ground", 345, 300, anchor="start")
    d.arrow(300, 60, 300, 20)
    lab(d, "Head", 330, 30, anchor="start")
    d.arrow(250, 120, 120, 120)
    d.arrow(390, 120, 520, 120)
    lab(d, "Sides", 120, 150)
    lab(d, "Sides", 520, 150)


@design("SHL/keeping-warm-while-sleeping-3")
def _(d):
    d.piece("person-standing", 100, 30, 320)
    for y, s in [(98, "Neck"), (172, "Hands"), (229, "Feet")]:
        x = 260 if y == 98 else (300 if y == 172 else 278)
        d.piece("survivor-mark", x - 28, y - 21, 56)
        d.arrow(x + 32, y, 440, y, width=3)
        lab(d, s, 455, y + 6, anchor="start")

@design("SHL/living-in-an-evacuation-centre-1")
def _(d):
    for y in (110, 182, 254):
        d.rect(30, y, 130, 64, rx=6)
        d.rect(480, y, 130, 64, rx=6)
    chip(d, 250, 50, 120, 44, "Toilets")
    chip(d, 390, 50, 140, 44, "Wash stations")
    d.arrow(320, 310, 320, 120)
    lab(d, "Corridor", 340, 220, anchor="start")
    lab(d, "Family bays", 95, 98)
    lab(d, "Family bays", 545, 98)


@design("SHL/living-in-an-evacuation-centre-2")
def _(d):
    d.rect(150, 30, 340, 270, fill="none", rx=22)
    items = [("document", "Documents", 160, 40), ("pills", "Medicines", 320, 40), ("bottle", "Water", 160, 170), ("gloves", "Warm clothes", 320, 170)]
    for p, s, x, y in items:
        d.rect(x, y, 160, 125, rx=4)
        d.piece(p, x + 35, y + 8, 90)
        lab(d, s, x + 80, y + 108, size=15)
    caption(d, "Packed by category so items are found quickly.")


@design("SHL/living-in-an-evacuation-centre-3")
def _(d):
    for y in (40, 120):
        d.rect(30, y, 130, 66, rx=6)
        d.rect(480, y, 130, 66, rx=6)
    lab(d, "Bays", 95, 30)
    lab(d, "Bays", 545, 30)
    d.rect(190, 205, 260, 105, fill="none", stroke=BLUE, dash="9 7", rx=12)
    d.piece("flashlight", 230, 215, 110)
    lab(d, "Dimmed zone", 320, 330, size=15)
    d.arrow(320, 100, 320, 195, width=3)
    lab(d, "Light and noise away", 335, 150, anchor="start", size=15)
    d.piece("do-not", 490, 215, 60)
    d.piece("phone-call", 545, 215, 70)
    lab(d, "Phones silent", 545, 300, size=15)


@design("SHL/repairing-a-tent-1")
def _(d):
    d.piece("tent", 60, 40, 330)
    d.piece("patch", 190, 150, 110)
    d.rect(205, 165, 80, 70, fill="none", dash="6 5", rx=6)
    lab(d, "Patch", 500, 130, anchor="start")
    d.leader(495, 124, 290, 180)
    lab(d, "Stitching", 500, 210, anchor="start")
    d.leader(495, 204, 287, 225)
    caption(d, "The patch overlaps the tear on every side.")


@design("SHL/repairing-a-tent-2")
def _(d):
    d.rect(60, 50, 340, 230, rx=8)
    d.line(78, 68, 382, 68, width=4)
    d.line(78, 68, 78, 262, width=4)
    d.line(382, 68, 382, 262, width=4)
    d.line(78, 262, 382, 262, width=4)
    d.piece("patch", 52, 42, 120)
    d.piece("seam-sealer", 470, 90, 130)
    lab(d, "Seam sealer", 535, 200)
    lab(d, "First wear points", 230, 326)
    d.arrow(160, 305, 90, 284, width=3)
    d.arrow(300, 305, 372, 284, width=3)
    lab(d, "Patch", 250, 40, anchor="start")
    d.leader(245, 34, 160, 80)


@design("SHL/repairing-a-tent-3")
def _(d):
    d.piece("bag", 80, 20, 160)
    d.piece("bag", 400, 20, 160)
    lab(d, "Tent bag", 160, 160)
    lab(d, "Pole bag", 480, 160)
    d.piece("fabric", 150, 200, 130)
    d.piece("do-not", 290, 220, 65)
    d.piece("pole", 360, 195, 120)
    lab(d, "Pole ends away from fabric", 320, 330)

@design("SHL/sanitation-in-a-shelter-1")
def _(d):
    d.piece("pool", 30, 20, 130)
    d.piece("water-drop", 160, 35, 70)
    lab(d, "Drinking water", 125, 140)
    d.line(30, 165, 560, 165, dash="9 7", width=3)
    chip(d, 300, 200, 120, 36, "Wash")
    d.line(30, 235, 560, 235, dash="9 7", width=3)
    d.piece("latrine", 400, 235, 110)
    lab(d, "Latrine", 455, 335)
    d.arrow(300, 60, 500, 60, color=BLUE, width=3)
    lab(d, "Wind", 400, 45)
    d.arrow(595, 30, 595, 290)
    lab(d, "Downhill", 590, 322)


@design("SHL/sanitation-in-a-shelter-2")
def _(d):
    d.piece("latrine", 30, 100, 150)
    d.piece("bucket", 270, 80, 150)
    d.piece("tap", 400, 140, 70)
    d.arrow(165, 150, 325, 185)
    lab(d, "Latrine", 105, 250)
    lab(d, "Tap", 440, 130)
    d.piece("soap", 480, 80, 70)
    d.piece("towel", 520, 160, 90)
    lab(d, "Soap", 515, 80)
    lab(d, "Towel", 565, 270)


@design("SHL/sanitation-in-a-shelter-3")
def _(d):
    d.piece("ground-line", 60, 250, 440, 50)
    d.piece("stand", 200, 170, 160)
    d.piece("jerrycan", 218, 114, 120)
    d.piece("tap", 300, 150, 70)
    d.arrow(385, 195, 385, 270)
    d.arrow(385, 270, 385, 195)
    lab(d, "Lid", 240, 112, anchor="end")
    d.leader(244, 108, 270, 128)
    lab(d, "Tap", 335, 150, anchor="start")
    lab(d, "Stand", 190, 250, anchor="end")

@design("SHL/sealing-a-room-against-the-cold-1")
def _(d):
    d.rect(150, 30, 400, 270, fill="none", rx=10)
    d.piece("door", 170, 190, 110)
    d.piece("window", 340, 40, 110)
    d.piece("caution", 262, 200, 45)
    d.piece("caution", 440, 62, 45)
    d.piece("caution", 385, 247, 45)
    chip(d, 490, 270, 90, 32, "Socket", size=15)
    d.arrow(30, 270, 195, 270)
    d.arrow(30, 95, 335, 95)
    lab(d, "Door gap", 235, 290)
    lab(d, "Window frame", 400, 160)

@design("SHL/sealing-a-room-against-the-cold-2")
def _(d):
    d.piece("cloth", 150, 20, 300)
    d.piece("arrow-curved", 230, 190, 100)
    lab(d, "Warm air trapped", 345, 240, anchor="start")
    d.arrow(415, 70, 480, 70, width=3)
    lab(d, "Top gap", 490, 76, anchor="start")
    d.arrow(190, 215, 130, 215, width=3)
    lab(d, "Side gap", 160, 245)
    caption(d, "Do not seal every gap.")


@design("SHL/shelter-after-a-flood-1")
def _(d):
    flow4(d, ["Entry check", "Power off", "Gas check", "Move higher"], ["step-1", "step-2", "step-3", "step-box"])
    caption(d, "Each step must clear before the next.", 300)


@design("SHL/shelter-after-a-flood-2")
def _(d):
    d.piece("wall", 190, 40, 260, 195)
    d.line(190, 215, 450, 215, dash="9 7", width=3, color=BLUE)
    lab(d, "Damp line", 320, 260)
    d.piece("fan", 20, 110, 120)
    lab(d, "Fan", 80, 240)
    d.arrow(120, 180, 190, 215, color=BLUE)
    d.arrow(450, 215, 520, 215, color=BLUE)
    d.piece("window", 500, 90, 120)
    lab(d, "Open window", 560, 260)


@design("SHL/shelter-after-a-flood-3")
def _(d):
    d.piece("fan", 20, 110, 130)
    d.arrow(160, 180, 430, 120, color=BLUE)
    d.arrow(160, 180, 430, 240, color=BLUE)
    d.piece("window", 450, 40, 120)
    d.piece("window", 450, 170, 120)
    lab(d, "Fan", 85, 250)
    lab(d, "Windows", 510, 160)
    caption(d, "The air path matters more than the fan's size.")


@design("SHL/shelter-after-a-storm-1")
def _(d):
    d.piece("roof", 120, 130, 300)
    d.piece("tarp-a-frame", 150, 20, 240)
    for x in (230, 270, 310):
        d.line(x, 60, x, 200, width=4)
    d.piece("rock", 110, 240, 70)
    d.piece("rock", 340, 240, 70)
    d.arrow(520, 250, 440, 160, color=BLUE)
    lab(d, "Wind", 520, 275)
    lab(d, "Weights", 30, 330, anchor="start", size=15)
    d.leader(95, 322, 128, 292)


@design("SHL/shelter-after-a-storm-2")
def _(d):
    d.piece("person-carrying", 190, 30, 260)
    lab(d, "Bent knees", 90, 270)
    d.leader(90, 256, 300, 205)
    lab(d, "Straight back", 100, 120)
    d.leader(150, 114, 284, 135)
    lab(d, "Load close", 540, 120)
    d.leader(500, 114, 385, 120)
    d.arrow(320, 245, 320, 300)


@design("SHL/shelter-after-a-storm-3")
def _(d):
    d.piece("window", 120, 40, 260)
    d.piece("board", 170, 90, 160)
    d.arrow(520, 150, 336, 150)
    lab(d, "Fixing", 430, 138)
    lab(d, "Board", 480, 260)
    d.leader(480, 246, 275, 165)
    lab(d, "Frame", 565, 80)
    d.leader(540, 74, 332, 88)
    caption(d, "Fix to the frame, not the glass.")


@design("SHL/shelter-for-people-with-disabilities-1")
def _(d):
    d.rect(40, 30, 560, 260, fill="none", rx=6)
    d.piece("door", 50, 180, 110)
    d.piece("bed", 440, 150, 150)
    d.arrow(160, 255, 440, 255)
    lab(d, "Step-free route", 300, 240, size=15)
    d.piece("bottle", 360, 50, 70)
    d.piece("flashlight", 440, 40, 80)
    lab(d, "Bedside items", 440, 120, size=15)
    lab(d, "Bed", 515, 320)


@design("SHL/shelter-for-people-with-disabilities-2")
def _(d):
    d.piece("door", 40, 170, 110)
    d.piece("bed", 470, 130, 140)
    d.piece("arrow-loop", 240, 40, 160)
    d.arrow(150, 250, 460, 250)
    lab(d, "Route", 305, 280)
    lab(d, "Turning circle", 320, 210, size=15)
    lab(d, "Bed", 540, 290)


@design("SHL/shelter-for-people-with-disabilities-3")
def _(d):
    d.piece("bed", 20, 160, 210)
    d.piece("table", 250, 180, 130)
    d.piece("flashlight", 230, 60, 70)
    d.piece("bottle", 310, 55, 60)
    d.piece("phone-call", 380, 55, 70)
    lab(d, "Lamp", 265, 50, size=15)
    lab(d, "Water", 340, 50, size=15)
    lab(d, "Call bell", 415, 50, size=15)
    d.arrow(55, 140, 420, 140, width=3)
    d.arrow(420, 140, 55, 140, width=3)
    lab(d, "Reach distance", 240, 130, size=15)

@design("SHL/shelter-in-a-public-building-1")
def _(d):
    d.rect(30, 30, 580, 270, fill="none", rx=6)
    d.rect(170, 55, 300, 150, fill="none", dash="9 7", rx=10)
    d.piece("survivor-mark", 270, 80, 100)
    lab(d, "Shelter zone", 320, 195)
    d.piece("waypoint-pin", 40, 150, 80)
    d.piece("waypoint-pin", 520, 150, 80)
    lab(d, "Exits", 80, 250)
    lab(d, "Exits", 560, 250)
    d.piece("toilet", 60, 40, 80)
    lab(d, "Toilets", 100, 118)
    d.piece("first-aid-kit", 500, 40, 80)
    lab(d, "First aid", 540, 118)
    d.arrow(120, 288, 520, 288)
    lab(d, "Route", 320, 276, size=15)

@design("SHL/shelter-in-an-apartment-1")
def _(d):
    d.rect(30, 30, 250, 200, rx=6)
    d.rect(360, 30, 250, 200, rx=6)
    d.line(320, 20, 320, 240, width=8)
    d.piece("bed", 85, 70, 140)
    d.piece("stove", 415, 75, 140)
    lab(d, "Sleeping", 155, 56, size=15)
    lab(d, "Cooking", 485, 56, size=15)
    d.piece("door", 100, 235, 90)
    d.piece("door", 430, 235, 90)
    d.arrow(155, 205, 155, 236, width=3)
    d.arrow(485, 205, 485, 236, width=3)
    lab(d, "Exit", 145, 345 - 20)
    lab(d, "Exit", 475, 345 - 20)


@design("SHL/shelter-in-an-apartment-2")
def _(d):
    d.piece("window", 30, 80, 130)
    d.piece("arrow-curved", 160, 60, 110)
    d.piece("door", 480, 150, 130)
    d.arrow(60, 280, 470, 280)
    lab(d, "Window", 95, 70)
    lab(d, "Exit path", 265, 268)
    d.piece("jerrycan", 300, 90, 100)
    d.piece("do-not", 380, 100, 60)
    lab(d, "Stored fuel", 360, 200, size=15)


@design("SHL/shelter-priorities-1")
def _(d):
    labels = ["Shade", "Trap warm air", "Insulated", "Dry", "Out of wind"]
    for i, s in enumerate(labels):
        y = 20 + i * 58
        d.piece("step-box", 150, y, 90)
        lab(d, s, 260, y + 40, anchor="start")
    d.arrow(80, 280, 80, 40)
    caption(d, "Base is most urgent.", 335)


@design("SHL/shelter-in-an-apartment-3")
def _(d):
    d.rect(180, 25, 430, 120, rx=6)
    d.rect(180, 155, 430, 120, rx=6)
    d.piece("tin", 220, 35, 100)
    d.piece("tin", 330, 35, 100)
    d.piece("jerrycan", 220, 165, 110)
    d.piece("bucket", 350, 165, 110)
    lab(d, "Tins above", 100, 95)
    lab(d, "Water low", 100, 225)
    d.arrow(60, 310, 580, 310)
    lab(d, "Clear floor", 320, 300, size=15)


@design("SHL/shelter-priorities-2")
def _(d):
    d.piece("slope", 30, 60, 250)
    d.arrow(90, 100, 140, 205, color=BLUE)
    lab(d, "Cold air", 80, 90)
    lab(d, "Hollow", 120, 270)
    d.leader(120, 256, 125, 232)
    d.piece("slope", 360, 60, 250)
    d.arrow(350, 110, 570, 110, color=BLUE)
    lab(d, "Wind", 440, 98)
    lab(d, "Ridge", 565, 80)
    d.leader(570, 88, 590, 108)


@design("SHL/shelter-priorities-3")
def _(d):
    d.piece("wall", 20, 80, 170)
    d.piece("bedding", 250, 70, 150)
    d.piece("sleeping-mat", 250, 130, 150)
    d.piece("ground-line", 220, 200, 210, 50)
    d.piece("bracket", 440, 60, 60, 60)
    lab(d, "Windbreak", 105, 260)
    lab(d, "Bedding", 440, 160, anchor="start")
    lab(d, "Ground mat", 440, 210, anchor="start")
    lab(d, "Ventilation gap", 510, 95, anchor="start", size=15)

@design("SHL/sleeping-outdoors-in-rain-1")
def _(d):
    d.piece("tarp-a-frame", 190, -5, 250)
    d.piece("rain", 450, 20, 110)
    d.piece("person-sitting", 255, 130, 100)
    d.piece("bed", 240, 155, 130)
    d.piece("ground-line", 170, 230, 330, 50)
    d.piece("stream-bed", 20, 200, 140)
    d.arrow(200, 150, 110, 215, color=BLUE)
    lab(d, "Tarp", 540, 200)
    d.leader(525, 194, 428, 160)
    lab(d, "Bed", 305, 335 - 15)
    lab(d, "Channel", 90, 320)
