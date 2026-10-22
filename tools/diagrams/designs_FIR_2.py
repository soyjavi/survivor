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


def label(d, s, x, y, anchor="middle", size=16):
    d.text(s, x, y, size=size, weight=600, anchor=anchor)


def ring(d, cx, cy, r, color=INK):
    d.path(f"M{cx - r} {cy}a{r} {r} 0 1 0 {2 * r} 0a{r} {r} 0 1 0 {-2 * r} 0", stroke=color, width=3, dash="9 7")


@design("FIR/putting-out-fires-1")
def _(d):
    d.piece("flame", 270, 20, 100)
    label(d, "Fuel", 320, 120)
    items = [("bucket", "Water"), ("bag", "Sand"), ("blanket", "Blanket"), ("pot-with-lid", "Lid")]
    for i, (p, s) in enumerate(items):
        x = 24 + i * 152
        d.piece(p, x, 170, 130)
        label(d, s, x + 65, 300)
    d.piece("water-drop", 62, 150, 50)
    caption(d, "The material must match the fuel.")


@design("FIR/putting-out-fires-2")
def _(d):
    xs = [100, 245, 390, 535]
    heads = ["Wood", "Oil", "Electrical", "Petrol"]
    d.rect(16, 24, 608, 50, fill=SAND, rx=8)
    d.rect(16, 74, 608, 200, fill=CREAM, rx=8)
    for x, h in zip(xs, heads):
        label(d, h, x + 20, 57, size=17)
    for x in xs[:3]:
        d.piece("water-drop", x - 25, 105, 90)
        label(d, "Water", x + 20, 250)
    d.piece("bag", xs[3] - 50, 105, 100)
    label(d, "Sand", xs[3] + 20, 250)
    d.tick(xs[0] + 50, 120, 16)
    d.cross(xs[1] + 50, 120, 16)
    d.cross(xs[2] + 50, 120, 16)
    d.tick(xs[3] + 50, 120, 16)
    caption(d, "Some fires must never be doused with water.", 316)


@design("FIR/putting-out-fires-3")
def _(d):
    items = [("bucket", "Pour"), ("coals", "Stir"), ("open-hand", "Hand test")]
    for i, (p, s) in enumerate(items):
        x = 30 + i * 200
        d.badge(i + 1, x + 20, 70, 18)
        d.piece(p, x + 10, 110, 150)
        label(d, s, x + 85, 270, size=17)
        if i < 2:
            d.arrow(x + 168, 170, x + 208, 170, width=4)
    caption(d, "Hissing stops before the ash is cold.", 330)


@design("FIR/putting-out-fires-4")
def _(d):
    items = [("person-standing", "Stop"), ("person-sitting", "Drop"), ("person-kneeling", "Roll")]
    for i, (p, s) in enumerate(items):
        x = 30 + i * 200
        d.rect(x, 40, 180, 250, fill=CREAM, rx=10)
        d.badge(i + 1, x + 24, 64, 16)
        d.piece(p, x + 20, 90, 140)
        label(d, s, x + 90, 270, size=18)
    caption(d, "Running feeds flames, rolling smothers them.", 328)


@design("FIR/putting-out-fires-5")
def _(d):
    d.piece("stove", 24, 100, 150)
    label(d, "Stove", 99, 250)
    d.piece("door", 450, 100, 140)
    label(d, "Exit", 520, 250)
    d.piece("waypoint-pin", 480, 30, 60)
    d.arrow(184, 170, 440, 170, width=5)
    chip(d, 312, 110, 100, 36, "Clutter")
    d.cross(312, 72, 16)
    label(d, "Clear path", 312, 212, size=17)
    caption(d, "Plan the route before the fire starts.", 328)


@design("FIR/starting-a-fire-with-matches-and-tinder-1")
def _(d):
    d.piece("tinder-pile", 290, 90, 260)
    label(d, "Tinder", 420, 300, size=17)
    d.piece("flame", 190, 150, 120)
    d.leader(110, 110, 232, 175)
    label(d, "Light here", 16, 104, anchor="start")
    d.arrow(30, 235, 180, 235, width=5)
    label(d, "Wind", 105, 275, size=17)
    caption(d, "First flame goes on the side facing the wind.", 340)


@design("FIR/starting-a-fire-with-matches-and-tinder-2")
def _(d):
    d.piece("log-stack", 120, 20, 130)
    label(d, "Fuel logs", 280, 80, anchor="start", size=17)
    chip(d, 185, 175, 130, 44, "Kindling")
    d.piece("tinder-pile", 120, 230, 130)
    label(d, "Tinder nest", 280, 290, anchor="start", size=17)
    label(d, "Catch first", 280, 322, anchor="start", size=15)
    d.arrow(185, 228, 185, 202, width=4)
    d.arrow(185, 150, 185, 122, width=4)
    for n, y in ((1, 280), (2, 175), (3, 70)):
        d.badge(n, 80, y, 16)


@design("FIR/starting-a-fire-with-matches-and-tinder-4")
def _(d):
    d.piece("match", 90, 30, 150)
    d.piece("hand", 280, 30, 150)
    label(d, "Match", 165, 150)
    label(d, "Sheltered flame", 355, 150)
    d.arrow(320, 170, 320, 220, width=4)
    d.piece("tinder-pile", 245, 215, 150)
    label(d, "Tinder", 320, 340, size=17)
    d.text("Light it before\nit burns down", 440, 270, size=16, weight=600, anchor="start")


@design("FIR/storing-fuel-1")
def _(d):
    d.piece("log-stack", 150, 20, 110)
    label(d, "Wood", 16, 70, anchor="start", size=17)
    chip(d, 205, 182, 110, 50, "Cylinder")
    label(d, "Gas", 16, 188, anchor="start", size=17)
    d.piece("jerrycan", 150, 250, 110)
    label(d, "Liquid fuel", 16, 315, anchor="start", size=17)
    d.piece("house", 440, 110, 180)
    label(d, "House", 530, 275, size=17)
    d.arrow(270, 70, 440, 150, width=3)
    d.arrow(440, 150, 270, 70, width=3)
    d.arrow(270, 182, 440, 182, width=3)
    d.arrow(440, 182, 270, 182, width=3)
    d.arrow(270, 290, 440, 215, width=3)
    d.arrow(440, 215, 270, 290, width=3)


@design("FIR/storing-fuel-2")
def _(d):
    for i in range(5):
        d.piece("waves", 16 + i * 122, 262, 120)
    d.line(16, 250, 624, 250, dash="10 8", width=4, color=BLUE)
    label(d, "Flood line", 624, 238, anchor="end")
    d.piece("table", 210, 50, 220)
    d.piece("bag", 235, 66, 90)
    d.piece("jerrycan", 335, 66, 90)
    label(d, "Charcoal", 120, 70, anchor="end")
    d.leader(124, 62, 250, 100)
    label(d, "Fuel cans", 520, 70, anchor="start")
    d.leader(516, 62, 410, 100)
    label(d, "Upper shelf", 110, 160, anchor="end")
    d.leader(114, 154, 230, 148)


@design("FIR/storing-fuel-3")
def _(d):
    d.piece("hut", 190, 60, 260)
    d.piece("vent", 205, 190, 56)
    d.piece("vent", 380, 125, 56)
    d.arrow(40, 230, 200, 230, width=4)
    d.arrow(440, 150, 560, 100, width=4)
    label(d, "Low vent", 120, 275)
    label(d, "High vent", 560, 140)
    caption(d, "Air in low and out high keeps moisture moving.", 340)


@design("FIR/storing-fuel-5")
def _(d):
    d.piece("hut", 30, 90, 240)
    d.piece("vent", 88, 200, 46)
    d.leader(70, 120, 100, 205)
    label(d, "Vent", 40, 112)
    d.piece("table", 360, 120, 200)
    d.piece("jerrycan", 410, 125, 100)
    d.leader(580, 90, 480, 150)
    label(d, "Fuel", 580, 82, anchor="start")
    chip(d, 150, 300, 110, 40, "Locked")
    d.piece("caution", 220, 270, 50)
    d.line(150, 280, 150, 258, width=3)
    caption(d, "Labels, vents and restricted access.", 346)


@design("FIR/wildfire-home-defence-1")
def _(d):
    cx, cy = 230, 185
    ring(d, cx, cy, 45)
    ring(d, cx, cy, 85)
    ring(d, cx, cy, 125)
    d.piece("hut", cx - 40, cy - 30, 80)
    d.piece("tree", cx - 24, cy - 82, 48)
    d.piece("shrub", cx + 42, cy + 8, 44)
    d.piece("flame", 20, 140, 70)
    d.arrow(90, 170, 190, 182, width=4)
    label(d, "Embers", 60, 235, size=15)
    label(d, "Zone 1 clear and watered", 380, 90, anchor="start")
    d.leader(376, 84, cx + 32, cy - 22)
    label(d, "Zone 2 thinned", 380, 175, anchor="start")
    d.leader(376, 169, cx + 90, cy + 5)
    label(d, "Beyond short grass", 380, 260, anchor="start")
    d.leader(376, 254, cx + 135, cy + 36)


@design("FIR/wildfire-home-defence-2")
def _(d):
    cx, cy = 220, 185
    ring(d, cx, cy, 60)
    ring(d, cx, cy, 140)
    d.piece("hut", cx - 38, cy - 28, 76)
    d.arrow(cx + 40, cy, cx + 58, cy, width=3)
    d.arrow(cx, cy - 30, cx, cy - 138, width=3)
    d.arrow(cx, cy - 138, cx, cy - 30, width=3)
    chip(d, 500, 120, 200, 56, "5 metres\nZone 1")
    d.leader(400, 120, cx + 58, cy - 6)
    chip(d, 500, 240, 200, 56, "30 metres\nZone 2 and beyond")
    d.leader(400, 240, cx + 138, cy + 30)


@design("FIR/wildfire-home-defence-3")
def _(d):
    d.piece("vent", 40, 150, 150)
    d.piece("gutter", 430, 130, 190)
    label(d, "Fine mesh", 115, 300)
    label(d, "Clean gutter", 525, 300)
    label(d, "Embers", 320, 50)
    d.curve_arrow("M290 70C230 80 140 90 120 140", (120, 140), 1.9)
    d.curve_arrow("M350 70C410 80 500 90 520 140", (520, 140), 1.2)
    caption(d, "Mesh and clean gutters stop embers entering.", 340)


@design("FIR/wildfire-home-defence-4")
def _(d):
    d.piece("hut", 230, 60, 180)
    d.piece("hose", 20, 90, 130)
    label(d, "Hose", 85, 210)
    d.piece("ladder", 480, 80, 130)
    label(d, "Ladder", 545, 220)
    d.piece("bucket", 250, 230, 120)
    label(d, "Bucket", 310, 345)
    d.arrow(160, 140, 235, 130, width=3)
    d.arrow(235, 130, 160, 140, width=3)
    d.arrow(470, 140, 405, 130, width=3)
    d.arrow(405, 130, 470, 140, width=3)
    d.arrow(310, 228, 310, 190, width=3)
    d.arrow(310, 190, 310, 228, width=3)


@design("FIR/winter-driving-emergency-kit-1")
def _(d):
    d.piece("car", 16, 100, 220)
    label(d, "Rear seat", 126, 280)
    d.arrow(250, 170, 380, 170, width=5)
    kit = [("bag", "Sand", 400, 30), ("bottle", "Water", 510, 30), ("flashlight", "Light", 400, 190), ("first-aid-kit", "First aid", 510, 190)]
    for p, s, x, y in kit:
        d.piece(p, x, y, 100)
        label(d, s, x + 50, y + 100)
    caption(d, "Kit within reach of the rear seat.", 346)
