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


def grid(d, x, y, widths, rowh, rows, header=None, headh=36):
    w = sum(widths)
    total = (headh if header else 0) + rowh * rows
    d.rect(x, y, w, total, rx=8)
    cx = x
    for cw in widths[:-1]:
        cx += cw
        d.line(cx, y, cx, y + total, width=2)
    top = y
    if header:
        top = y + headh
        d.line(x, top, x + w, top, width=3)
        cx = x
        for cw, s in zip(widths, header):
            d.text(s, cx + cw / 2, y + headh / 2 + 6, size=16, weight=600)
            cx += cw
    for r in range(1, rows):
        d.line(x, top + r * rowh, x + w, top + r * rowh, width=2)
    return top


def hbrace(d, x1, x2, y, up=True):
    k = 12 if up else -12
    m = (x1 + x2) / 2
    d.path(f"M{x1} {y}L{x1} {y - k}L{m} {y - k}L{m} {y - 2 * k}M{m} {y - k}L{x2} {y - k}L{x2} {y}")


@design("FOD/keeping-food-cool-without-power-1")
def _(d):
    xs = [30, 245, 460]
    for x, p, s in zip(xs, ["hut", "cool-box", "cellar"], ["Cool room", "Cool box", "Cellar or stream"]):
        d.rect(x, 60, 150, 220, rx=14)
        d.piece(p, x + 5, 100, 140)
        d.text(s, x + 75, 250, size=17, weight=600)
    d.line(184, 170, 241, 170, dash="9 7")
    d.line(399, 170, 456, 170, dash="9 7")
    caption(d, "Each option suits different foods.", 330)


@design("FOD/keeping-food-cool-without-power-2")
def _(d):
    d.piece("freezer", 50, 60, 210)
    d.text("Freezer", 155, 270, size=17, weight=600)
    d.piece("thermometer", 290, 70, 130)
    d.text("Thermometer", 355, 270, size=17, weight=600)
    d.leader(470, 120, 366, 140)
    d.text("Reading", 478, 126, size=16, weight=600, anchor="start")
    d.piece("do-not", 500, 180, 100)
    d.text("Opening the door", 550, 300, size=15, weight=600)
    caption(d, "Check a closed freezer without letting cold air out.", 340)


@design("FOD/keeping-food-cool-without-power-3")
def _(d):
    d.rect(150, 30, 260, 290, rx=14)
    d.piece("ice-cube", 220, 44, 120)
    d.text("Ice", 450, 100, size=17, weight=600, anchor="start")
    d.leader(444, 94, 330, 100)
    d.arrow(280, 150, 280, 240, width=4)
    d.text("Cold air sinks", 300, 200, size=16, weight=600, anchor="start")
    chip(d, 280, 275, 200, 44, "Food")
    caption(d, "Ice sits above the food.", 346)


@design("FOD/keeping-food-cool-without-power-4")
def _(d):
    labels = ["Cooked food", "Fridge items", "Frozen items", "Dry goods"]
    for i, s in enumerate(labels):
        cy = 50 + i * 80
        chip(d, 320, cy, 220, 46, s, size=17)
        d.badge(i + 1, 180, cy, 17)
        if i < 3:
            d.arrow(320, cy + 25, 320, cy + 54, width=3)
    d.text("Eat first", 470, 56, size=17, weight=600, anchor="start")
    d.text("Eat last", 470, 296, size=17, weight=600, anchor="start")
    caption(d, "Use these foods first when power fails.", 346)


@design("FOD/making-vinegar-and-acids-for-preservation-1")
def _(d):
    d.arrow(50, 220, 590, 220, width=4)
    for x in (130, 250, 370, 490):
        d.line(x, 210, x, 230, width=3)
    d.text("Weaker acid", 50, 258, size=15, anchor="start")
    d.text("Stronger acid", 590, 258, size=15, anchor="end")
    d.circle(190, 220, 9, fill=YELLOW)
    d.leader(190, 140, 190, 208)
    chip(d, 190, 122, 140, 40, "Lemon juice")
    d.line(380, 90, 380, 220, dash="9 7", color=RED, width=4)
    d.circle(470, 220, 9, fill=YELLOW)
    d.leader(470, 140, 470, 208)
    chip(d, 470, 122, 110, 40, "Vinegar")
    hbrace(d, 392, 590, 100, up=True)
    d.text("Safe zone", 490, 60, size=17, weight=600)
    caption(d, "Acid strength decides what keeps.", 330)


@design("FOD/making-vinegar-and-acids-for-preservation-2")
def _(d):
    d.piece("jar", 50, 50, 250)
    d.leader(430, 100, 215, 105)
    d.text("Mother", 440, 106, size=17, weight=600, anchor="start")
    d.leader(430, 170, 200, 170)
    d.text("Liquid", 440, 176, size=17, weight=600, anchor="start")
    d.leader(430, 240, 206, 200)
    d.text("Sediment", 440, 246, size=17, weight=600, anchor="start")
    caption(d, "Mother and sediment are normal, not spoilage.", 330)


@design("FOD/meal-planning-from-the-pantry-1")
def _(d):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    x0, cw = 126, 70
    top = grid(d, x0, 30, [cw] * 7, 70, 3, header=days)
    for r, s in enumerate(["Staples", "Proteins", "Vegetables"]):
        d.text(s, 114, top + r * 70 + 41, size=16, weight=600, anchor="end")
    for r in range(3):
        for c in range(7):
            cx, cy = x0 + c * cw + cw / 2, top + r * 70 + 35
            if (r, c) == (1, 4):
                d.piece("caution", cx - 22, cy - 22, 44, 44)
            else:
                d.tick(cx, cy, 14)
    caption(d, "Every day fills all three slots, so gaps show.", 330)


@design("FOD/meal-planning-from-the-pantry-2")
def _(d):
    top = grid(d, 110, 50, [210, 210], 190, 1, header=["Main dish", "Accompaniment"], headh=44)
    d.piece("bowl", 130, top + 20, 170)
    d.piece("bowl", 340, top + 20, 170)
    caption(d, "Two boxes per day keep cooking short.", 330)


@design("FOD/meal-planning-from-the-pantry-3")
def _(d):
    xs = [30, 190, 350, 510]
    labels = ["Staple", "Protein", "Vegetable", "Meal"]
    for x, s in zip(xs, labels):
        d.piece("bowl", x, 120, 100)
        d.text(s, x + 50, 245, size=17, weight=600)
    d.text("+", 150, 190, size=30, weight=600)
    d.text("+", 310, 190, size=30, weight=600)
    d.text("=", 470, 190, size=30, weight=600)
    hbrace(d, 40, 600, 112, up=True)
    d.text("Same build every meal", 320, 70, size=17, weight=600)
    caption(d, "Every meal is built the same way.", 330)


@design("FOD/meal-planning-from-the-pantry-4")
def _(d):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    x0, cw = 75, 70
    top = grid(d, x0, 40, [cw] * 7, 110, 1, header=days)
    d.piece("note", x0 + 8, top + 22, 54, 65)
    d.piece("tip", x0 + cw + 8, top + 22, 54, 65)
    hbrace(d, x0 + 6, x0 + 2 * cw - 6, 270, up=False)
    d.text("Perishable first", x0 + cw, 312, size=17, weight=600)
    hbrace(d, x0 + 2 * cw + 6, x0 + 7 * cw - 6, 270, up=False)
    d.text("Dry stock later", x0 + 4.5 * cw, 312, size=17, weight=600)


@design("FOD/ninety-day-pantry-1")
def _(d):
    d.rect(60, 30, 340, 270, rx=8)
    d.line(60, 120, 400, 120, width=2)
    d.line(60, 210, 400, 210, width=2)
    d.piece("jar", 160, 34, 120, 86)
    d.piece("tin", 160, 124, 120, 86)
    d.piece("barrel", 90, 214, 120, 86)
    d.piece("bag", 240, 214, 120, 86)
    d.text("Dry goods high", 420, 82, size=17, weight=600, anchor="start")
    d.text("Cans middle", 420, 170, size=17, weight=600, anchor="start")
    d.text("Grains low", 420, 258, size=17, weight=600, anchor="start")
    caption(d, "Heavy stock sits low so shelving stays stable.", 334)


@design("FOD/ninety-day-pantry-2")
def _(d):
    grid(d, 40, 40, [220], 44, 3, header=["Weekly list"], headh=44)
    grid(d, 380, 40, [220], 44, 5, header=["Core list"], headh=44)
    d.arrow(270, 140, 370, 140, width=5)
    caption(d, "The core list grows from what the household buys.", 340)


@design("FOD/ninety-day-pantry-3")
def _(d):
    for i in range(4):
        d.piece("tin", 36 + i * 150, 120, 120, 90)
    d.arrow(80, 90, 560, 90, width=4)
    d.text("Back", 80, 66, size=16, weight=600, anchor="start")
    d.text("Front", 560, 66, size=16, weight=600, anchor="end")
    d.text("New", 96, 250, size=17, weight=600)
    d.badge(1, 96, 280, 15)
    d.text("Oldest", 546, 250, size=17, weight=600)
    d.piece("do", 496, 258, 64, 48)
    d.text("Use first", 556, 294, size=16, weight=600, anchor="start")
    caption(d, "Rotation keeps the oldest stock used first.", 342)


@design("FOD/ninety-day-pantry-4")
def _(d):
    top = grid(d, 130, 30, [200, 180], 52, 4, header=["Check", "Done"], headh=40)
    for r, s in enumerate(["Damage", "Swelling", "Leaks", "Insects"]):
        cy = top + r * 52 + 26
        d.text(s, 230, cy + 6, size=17, weight=600)
        d.piece("do", 400, cy - 20, 40, 40)
    caption(d, "Checks are a routine list, not a one-off look.", 336)


@design("FOD/pest-control-in-the-pantry-1")
def _(d):
    d.line(560, 24, 560, 290, width=6)
    d.text("Wall", 590, 160, size=16, weight=600)
    d.piece("shelf", 70, 90, 290)
    d.line(30, 296, 540, 296, width=5)
    d.text("Ground", 60, 322, size=15, weight=600, anchor="start")
    d.text("Raised storage", 215, 60, size=17, weight=600)
    d.leader(215, 70, 215, 120)
    chip(d, 450, 262, 160, 40, "Trap along wall", size=15)
    d.arrow(536, 262, 552, 262, width=3)
    caption(d, "Raised storage and wall-side traps stop pests early.", 342)


@design("FOD/pest-control-in-the-pantry-3")
def _(d):
    xs = [40, 245, 450]
    for i, (x, s) in enumerate(zip(xs, ["Walls", "Corners", "Shelves"])):
        d.piece("waypoint-pin", x, 90, 150)
        d.badge(i + 1, x + 75, 80, 18)
        d.text(s, x + 75, 250, size=17, weight=600)
        if i < 2:
            d.arrow(x + 150, 170, x + 205 - 4, 170, width=4)
    caption(d, "The order of checks leaves no zone missed.", 330)


@design("FOD/pest-control-in-the-pantry-4")
def _(d):
    d.path("M150 40L490 40L490 290L150 290Z", width=6)
    for cx, cy in [(190, 66), (450, 66), (190, 264), (450, 264)]:
        chip(d, cx, cy, 64, 30, "Trap", size=15)
    d.piece("footprints", 230, 56, 170, 128)
    d.text("Wall", 120, 170, size=16, weight=600, anchor="end")
    d.leader(124, 164, 146, 164)
    caption(d, "Rodents travel along walls, so traps go there.", 334)


@design("FOD/portions-and-rationing-1")
def _(d):
    top = grid(d, 30, 60, [140, 110, 100], 56, 2, header=["Daily need", "People", "Days"], headh=44)
    d.arrow(400, 150, 460, 150, width=4)
    chip(d, 540, 150, 140, 56, "Daily ration", size=17)
    caption(d, "One store becomes one ration.", 330)


@design("FOD/portions-and-rationing-2")
def _(d):
    d.piece("bowl", 40, 100, 180)
    d.text("Dry rice", 130, 90, size=17, weight=600)
    chip(d, 130, 250, 170, 44, "Scale")
    d.arrow(240, 170, 390, 170, width=4)
    d.piece("bowl", 410, 100, 180)
    d.text("Portion", 500, 90, size=17, weight=600)
    caption(d, "Weight keeps portions consistent.", 320)


@design("FOD/portions-and-rationing-3")
def _(d):
    labels = ["Total store", "Divide by\npeople", "Divide by\ndays", "Daily ration"]
    for i, s in enumerate(labels):
        cx = 85 + i * 157
        chip(d, cx, 170, 120, 70, s, size=16)
        if i < 3:
            d.badge(i + 1, cx - 38, 118, 15)
            d.arrow(cx + 62, 170, cx + 92, 170, width=3)
    caption(d, "Each step shows so the arithmetic can be checked.", 300)


@design("FOD/portions-and-rationing-4")
def _(d):
    pieces = ["person-standing", "person-sitting", "person-standing", "person-sitting"]
    for i, p in enumerate(pieces):
        x = 40 + i * 150
        d.piece("bowl", x, 100, 110)
        d.piece(p, x + 15, 190, 80)
    hbrace(d, 50, 590, 100, up=True)
    d.text("Equal share", 320, 62, size=17, weight=600)
    chip(d, 450, 300, 190, 40, "Extra for need", size=16)
    d.arrow(450, 278, 450, 254, width=3)
    d.arrow(500, 278, 560, 254, width=3)
    d.arrow(400, 278, 345, 254, width=3)


@design("FOD/preserving-eggs-without-refrigeration-1")
def _(d):
    d.piece("egg", 60, 60, 240)
    d.arrow(90, 160, 165, 160, width=3)
    d.arrow(165, 160, 90, 160, width=3)
    d.text("Exchange", 100, 130, size=15, weight=600)
    labels = [("Pores", 90), ("Air cell", 150), ("Membranes", 210), ("Coating", 270)]
    for s, y in labels:
        d.leader(440, y - 6, 215, 100 + (y - 90) * 0.4)
        d.text(s, 450, y, size=17, weight=600, anchor="start")
    caption(d, "The coating slows moisture and air exchange.", 336)


@design("FOD/preserving-eggs-without-refrigeration-2")
def _(d):
    top = grid(d, 170, 30, [330], 62, 4)
    for r in range(4):
        cy = top + r * 62 + 31
        d.piece("note", 180, cy - 24, 40, 48)
        for k in range(3):
            d.piece("egg", 250 + k * 80, cy - 28, 66, 50)
    d.text("Dated row", 16, 62, size=16, weight=600, anchor="start")
    d.leader(100, 56, 188, 56)
    d.arrow(560, 40, 560, 250, width=4)
    d.text("Back", 560, 28, size=15, weight=600)
    d.text("Front", 560, 274, size=15, weight=600)
    d.text("Oldest first", 560, 304, size=17, weight=600)


@design("FOD/salting-and-drying-meat-and-fish-2")
def _(d):
    d.text("Tin", 320, 36, size=17, weight=600)
    d.rect(170, 50, 300, 250, rx=12)
    for i, (s, f) in enumerate([("Strip", CREAM), ("Salt", PAPER), ("Strip", CREAM), ("Salt", PAPER), ("Strip", CREAM)]):
        chip(d, 320, 80 + i * 48, 240, 38, s, fill=f)
    caption(d, "Every strip sits in salt, so no surface is left unsalted.", 334)


@design("FOD/salting-and-drying-meat-and-fish-3")
def _(d):
    d.piece("post", 30, 120, 130)
    d.piece("post", 480, 120, 130)
    d.line(95, 132, 545, 132, width=4)
    d.text("Cord", 320, 120, size=16, weight=600)
    for x in (200, 320, 440):
        d.line(x, 132, x, 160, width=3)
        chip(d, x, 180, 90, 36, "Strips", size=15)
    d.piece("cloth", 250, 20, 140, 90)
    d.text("Screen", 410, 70, size=16, weight=600, anchor="start")
    d.arrow(160, 262, 480, 262, width=4)
    d.text("Airflow", 320, 296, size=16, weight=600)
    caption(d, "Airflow dries the strips; the screen keeps flies off.", 342)


@design("FOD/smoking-fish-safely-1")
def _(d):
    d.rect(230, 24, 180, 300, rx=14)
    d.piece("vent", 255, 34, 130)
    d.piece("rack", 255, 120, 130)
    d.piece("flame", 255, 220, 130)
    d.text("Vent", 210, 70, size=17, weight=600, anchor="end")
    d.leader(214, 64, 270, 66)
    d.text("Racks", 210, 170, size=17, weight=600, anchor="end")
    d.leader(214, 164, 270, 164)
    d.text("Firebox", 210, 270, size=17, weight=600, anchor="end")
    d.leader(214, 264, 285, 264)
    d.piece("thermometer", 440, 90, 100)
    d.text("Probe", 490, 66, size=17, weight=600)
    d.leader(478, 152, 376, 152)
    d.arrow(590, 300, 590, 60, width=4)
    d.text("Heat and smoke rise", 570, 330, size=15, weight=600, anchor="end")


@design("FOD/solar-food-dryers-1")
def _(d):
    d.rect(210, 90, 230, 220, rx=10)
    chip(d, 325, 118, 200, 32, "Glass cover", size=15, fill="#e3eef5")
    d.piece("tray", 250, 160, 150)
    d.text("Trays", 325, 262, size=16, weight=600)
    chip(d, 325, 288, 200, 32, "Collector", size=15, fill="#e8d8b8")
    d.piece("sun", 40, 20, 130)
    d.arrow(150, 90, 232, 110, width=4)
    d.piece("vent", 395, 140, 90)
    d.text("Vent high", 490, 120, size=15, weight=600, anchor="start")
    d.leader(488, 126, 450, 164)
    d.piece("vent", 165, 222, 90)
    d.text("Vent low", 150, 300, size=15, weight=600, anchor="end")
    d.leader(154, 294, 200, 268)


@design("FOD/solar-food-dryers-2")
def _(d):
    d.rect(210, 60, 240, 240, rx=10)
    d.piece("vent", 150, 178, 100)
    d.piece("vent", 150, 243, 100)
    d.piece("vent", 400, 30, 130)
    d.arrow(30, 215, 160, 215, width=4)
    d.arrow(30, 280, 160, 280, width=4)
    d.text("Air in", 90, 255, size=16, weight=600)
    d.arrow(500, 78, 590, 78, width=4)
    d.text("Moist\nair out", 560, 112, size=16, weight=600)
    caption(d, "Cloth over each vent; lower vents bring air in.", 336)


@design("FOD/solar-food-dryers-3")
def _(d):
    d.piece("vent", 70, 150, 110)
    d.arrow(20, 200, 90, 200, width=4)
    d.text("Air in", 60, 262, size=17, weight=600)
    d.piece("tray", 260, 130, 150)
    d.text("Trays", 335, 245, size=17, weight=600)
    d.piece("vent", 480, 40, 110)
    d.curve_arrow("M172 199C260 199 250 120 340 120C400 120 430 86 484 86", (490, 84), 0, width=4)
    d.arrow(580, 82, 626, 82, width=4)
    d.text("Air out", 535, 150, size=17, weight=600)
    caption(d, "The air path, not heat, carries moisture out.", 336)


@design("FOD/solar-food-dryers-4")
def _(d):
    d.piece("tray", 140, 60, 360)
    for i in range(3):
        d.piece("fruit-slice", 170 + i * 110, 186, 90)
    d.arrow(268, 226, 292, 226, width=3)
    d.arrow(292, 226, 268, 226, width=3)
    d.text("Gap", 280, 285, size=15, weight=600)
    d.leader(280, 272, 280, 232)
    d.text("Single layer", 320, 100, size=17, weight=600)
    hbrace(d, 190, 450, 150, up=True)
    caption(d, "Gaps let air reach every surface.", 336)


@design("FOD/solar-ovens-1")
def _(d):
    d.rect(190, 130, 260, 170, rx=10)
    chip(d, 320, 146, 236, 30, "Glass lid", size=15, fill="#e3eef5")
    d.piece("pot-with-lid", 250, 170, 140)
    d.piece("insulation", 40, 150, 130)
    d.text("Insulation", 105, 262, size=16, weight=600)
    d.leader(150, 200, 198, 214)
    chip(d, 540, 190, 130, 34, "Reflector flap", size=15)
    d.arrow(475, 190, 452, 190, width=3)
    d.text("Pot", 320, 292, size=16, weight=600)
    d.piece("sun", 250, 10, 110)
    d.arrow(305, 90, 305, 128, width=4)


@design("FOD/solar-ovens-2")
def _(d):
    d.curve_arrow("M80 200Q320 -10 560 200", (562, 202), 0.9, width=4)
    d.piece("sun", 275, 20, 90)
    d.piece("compass-rose", 14, 14, 110)
    for cx, s in [(110, "Morning"), (320, "Midday"), (530, "Afternoon")]:
        chip(d, cx, 270, 140, 56, "Oven\n" + s, size=16)
    caption(d, "The oven is re-aimed through the day.", 340)


@design("FOD/solar-ovens-3")
def _(d):
    d.piece("sun", 30, 20, 130)
    chip(d, 300, 100, 120, 44, "Flap", size=17)
    d.arrow(170, 80, 236, 96, width=4)
    chip(d, 440, 270, 200, 56, "Glass lid", size=17, fill="#e3eef5")
    d.arrow(320, 125, 410, 238, width=4)
    d.text("Sunlight, not outside heat", 330, 336, size=15, weight=600, fill="#4a4238")


@design("FOD/solar-ovens-4")
def _(d):
    d.rect(100, 50, 300, 250, rx=12)
    d.piece("pot-with-lid", 140, 110, 220)
    d.piece("thermometer", 205, 168, 90)
    d.text("Pot centre", 250, 290, size=16, weight=600)
    d.leader(470, 150, 276, 184)
    d.text("Reading", 478, 156, size=16, weight=600, anchor="start")
    d.piece("do-not", 470, 190, 100)
    d.text("Air", 520, 300, size=16, weight=600)


@design("FOD/soup-from-scraps-1")
def _(d):
    d.rect(20, 60, 250, 230, rx=14)
    d.piece("pot-with-lid", 40, 110, 150)
    d.piece("leaf", 190, 130, 70)
    d.text("Trimmings", 145, 270, size=17, weight=600)
    d.arrow(285, 175, 345, 175, width=4)
    d.rect(360, 60, 260, 230, rx=14)
    d.piece("cloth", 380, 80, 110)
    d.piece("bowl", 450, 150, 150)
    d.text("Stock", 520, 270, size=17, weight=600)
    d.text("Solids stay behind", 490, 172, size=15, weight=600)
    caption(d, "Solids are removed; flavour stays in the liquid.", 330)


@design("FOD/soup-from-scraps-2")
def _(d):
    d.rect(80, 30, 240, 280, rx=14)
    d.piece("leaf", 150, 40, 100)
    d.piece("beans", 100, 120, 90)
    d.piece("grain", 210, 120, 90)
    d.piece("water-drop", 150, 210, 100)
    d.text("Herbs", 400, 76, size=17, weight=600, anchor="start")
    d.leader(394, 70, 230, 76)
    d.text("Beans and grain", 400, 166, size=17, weight=600, anchor="start")
    d.leader(394, 160, 296, 160)
    d.text("Stock", 400, 256, size=17, weight=600, anchor="start")
    d.leader(394, 250, 230, 256)
    d.badge(1, 50, 260, 15)
    d.badge(2, 50, 160, 15)
    d.badge(3, 50, 70, 15)
    caption(d, "Stock is the base; herbs go in last.", 336)


@design("FOD/soup-from-scraps-3")
def _(d):
    d.piece("pot-with-lid", 235, 20, 170)
    d.arrow(50, 250, 590, 250, width=4)
    for x in (130, 250, 370, 490):
        d.line(x, 240, x, 260, width=3)
    d.text("Start", 50, 290, size=15, anchor="start")
    d.text("End", 590, 290, size=15, anchor="end")
    d.circle(130, 250, 9, fill=YELLOW)
    d.leader(130, 200, 130, 238)
    chip(d, 130, 180, 100, 40, "Grain")
    d.circle(520, 250, 9, fill=YELLOW)
    d.leader(520, 200, 520, 238)
    chip(d, 520, 180, 100, 40, "Herbs")
    caption(d, "Time decides when each goes in.", 336)


@design("FOD/soup-from-scraps-4")
def _(d):
    d.piece("pot-with-lid", 200, 160, 200)
    d.piece("cloth", 215, 100, 170)
    chip(d, 300, 100, 120, 34, "Solids", size=15)
    d.arrow(300, 30, 300, 70, width=4)
    d.text("Stock", 340, 54, size=16, weight=600, anchor="start")
    d.text("Cloth", 470, 176, size=17, weight=600, anchor="start")
    d.leader(464, 170, 372, 160)
    d.text("Clean stock", 300, 322, size=17, weight=600)


@design("FOD/storing-grains-flour-and-legumes-1")
def _(d):
    d.piece("bucket", 60, 80, 220)
    d.text("Bucket with lid", 170, 270, size=16, weight=600)
    labels = ["Dry food", "Sealed container", "Regular checks"]
    for i, s in enumerate(labels):
        cy = 80 + i * 80
        chip(d, 500, cy, 200, 44, s, size=16)
        d.leader(398, cy, 214, 180 + (i - 1) * 24)
    caption(d, "Moisture, air and insects each need their own defence.", 336)


@design("FOD/storing-grains-flour-and-legumes-2")
def _(d):
    d.piece("grain", 20, 110, 150)
    d.text("Grain", 95, 230, size=17, weight=600)
    d.piece("bucket", 240, 80, 170)
    d.piece("cloth", 470, 110, 150)
    d.text("Cloth", 545, 230, size=17, weight=600)
    d.arrow(160, 180, 255, 180, width=4)
    d.arrow(480, 180, 385, 180, width=4)
    d.text("Less air", 325, 270, size=17, weight=600)
    caption(d, "A fuller container leaves less air.", 336)


@design("FOD/storing-grains-flour-and-legumes-3")
def _(d):
    d.rect(60, 36, 480, 180, rx=8)
    for x in (220, 380):
        d.line(x, 36, x, 216, width=2)
    for i in range(3):
        d.piece("bag", 80 + i * 160, 56, 120)
        d.piece("note", 170 + i * 160, 146, 40, 50)
    d.text("Date label", 120, 262, size=16, weight=600)
    d.leader(150, 250, 186, 182)
    chip(d, 320, 296, 180, 36, "Monthly check", size=15)
    d.tick(430, 296, 12)
    caption(d, "Dated bags make the monthly check quick.", 342)


@design("FOD/storing-grains-flour-and-legumes-4")
def _(d):
    for x, p in zip([50, 235, 420], ["bucket", "tin", "bucket"]):
        d.piece(p, x, 90, 150)
    d.line(30, 200, 610, 200, width=5)
    d.text("Dry storeroom", 320, 244, size=17, weight=600)
    for x in (217, 402):
        d.arrow(x, 190, x, 116, width=3)
        d.text("Air gap", x, 100, size=16, weight=600)
    caption(d, "Gaps let air circulate and stop damp.", 336)


@design("FOD/storing-potatoes-onions-and-root-crops-2")
def _(d):
    d.piece("cellar", 140, 60, 250)
    d.piece("vent", 420, 80, 110)
    d.piece("vent", 420, 190, 110)
    d.text("Upper vent", 470, 176, size=16, weight=600)
    d.text("Lower vent", 470, 286, size=16, weight=600)
    d.arrow(580, 250, 580, 100, width=4)
    d.text("Airflow", 585, 290, size=16, weight=600)
    d.piece("crate", 20, 150, 110)
    d.text("Crates", 75, 250, size=16, weight=600)
    caption(d, "Air moves up and carries moisture away.", 336)
