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


def lab(d, s, x, y, anchor="middle", size=16, fill=INK):
    d.text(s, x, y, size=size, weight=600, anchor=anchor, fill=fill)


@design("WTR/chemical-water-purification-1")
def _(d):
    d.piece("bottle", 16, 70, 120)
    lab(d, "Dose", 76, 190)
    d.arrow(140, 125, 180, 125)
    chip(d, 240, 125, 100, 44, "Shake")
    d.arrow(296, 125, 336, 125)
    d.piece("timeline-axis", 330, 70, 210)
    d.piece("bracket", 345, 150, 130)
    lab(d, "30 min or more", 435, 305)
    d.piece("do", 544, 90, 80)
    lab(d, "Drink", 584, 190)
    caption(d, "Cold water stretches the wait; drink only after the full time.")


@design("WTR/chemical-water-purification-2")
def _(d):
    d.piece("bottle", 16, 80, 120)
    lab(d, "Litres measured", 76, 220)
    d.arrow(146, 135, 214, 135)
    d.piece("pills", 220, 80, 120)
    lab(d, "Dose per litre", 280, 220)
    d.arrow(350, 135, 424, 135)
    d.piece("table-grid", 430, 70, 180)
    lab(d, "Tablets needed", 520, 220)
    caption(d, "Tablet count follows the measured volume, not a guess.")


@design("WTR/chemical-water-purification-3")
def _(d):
    d.piece("pills", 230, 100, 180)
    d.leader(190, 70, 290, 150)
    lab(d, "Dose per litre", 180, 62, "end")
    d.leader(450, 70, 350, 150)
    lab(d, "Cold-water dose", 460, 62, "start")
    d.leader(190, 260, 290, 205)
    lab(d, "Contact time", 180, 270, "end")
    d.leader(450, 260, 350, 205)
    lab(d, "Expiry date", 460, 270, "start")
    d.piece("do-not", 566, 240, 50)
    caption(d, "An expired packet no longer counts.")


@design("WTR/chemical-water-purification-4")
def _(d):
    d.piece("compass", 20, 60, 190)
    d.piece("thermometer", 230, 60, 120)
    zones = [("Cold", "longest wait"), ("Cool", "medium wait"), ("Warm", "shortest wait")]
    for i, (a, b) in enumerate(zones):
        y = 70 + i * 80
        d.piece("bracket", 380, y - 10, 70, 60)
        chip(d, 535, y + 22, 150, 56, a + "\n" + b, size=16)
    caption(d, "Colder water waits longer: read the dial before the tablet goes in.")


@design("WTR/daily-water-needs-1")
def _(d):
    x, w = 200, 200
    d.rect(x, 50, w, 36, fill=CREAM, dash="8 6")
    lab(d, "+20%", x + w / 2, 75)
    d.rect(x, 86, w, 56, fill=SAND)
    lab(d, "Hygiene", x + w / 2, 120)
    d.rect(x, 142, w, 56, fill=SAND)
    lab(d, "Cooking", x + w / 2, 176)
    d.rect(x, 198, w, 86, fill=BLUE)
    lab(d, "Drinking", x + w / 2, 247)
    d.piece("bracket", 410, 120, 120)
    lab(d, "3 litres", 520, 190, "start")
    d.piece("water-drop", 262, 6, 60)
    caption(d, "Drinking is fixed, so washing is cut first.", 322)


@design("WTR/daily-water-needs-2")
def _(d):
    rows = [("Drinking", 100), ("Cooking", 130), ("Hygiene", 280), ("Washing", 330), ("Laundry", 400)]
    d.line(150, 40, 150, 290, width=4)
    for i, (s, w) in enumerate(rows):
        y = 48 + i * 48
        lab(d, s, 140, y + 24, "end")
        d.rect(150, y, w, 36, fill=SAND if w < 200 else BLUE, rx=6)
    d.arrow(480, 318, 570, 318)
    lab(d, "Cuts start here", 470, 324, "end")
    caption(d, "Cut from the long end first.", 346)


def table(d, x, y, widths, rh, header, rows, hsize=15):
    total = sum(widths)
    d.rect(x, y, total, rh, fill=SAND, rx=6)
    cx = x
    for w, h in zip(widths, header):
        d.text(h, cx + w / 2, y + rh / 2 + 5 - (h.count("\n")) * 9, size=hsize, weight=700)
        cx += w
    for r in range(len(rows) + 1):
        pass
    d.rect(x, y + rh, total, rh * len(rows), fill=CREAM, rx=6)
    for r in range(1, len(rows)):
        d.line(x, y + rh * (r + 1), x + total, y + rh * (r + 1), width=2)
    cx = x
    for w in widths[:-1]:
        cx += w
        d.line(cx, y, cx, y + rh * (len(rows) + 1), width=2)
    for r, row in enumerate(rows):
        cx = x
        for w, c in zip(widths, row):
            if c:
                d.text(c, cx + w / 2, y + rh * (r + 1) + rh / 2 + 5, size=15, weight=600)
            cx += w


@design("WTR/daily-water-needs-3")
def _(d):
    widths = [100, 120, 120, 130, 110]
    table(d, 20, 30, widths, 32, ["Date", "Litres used", "Litres left", "Running total", "Days left"], [[""] * 5 for _ in range(7)])
    d.rect(20 + 470, 30 + 32 * 7, 110, 32, fill=YELLOW, rx=6)
    d.piece("info", 540, 262, 44)
    d.text("left / daily", 545, 308, size=15, weight=600)
    caption(d, "Litres left divided by the daily total gives days of supply.", 346)


@design("WTR/disinfecting-water-with-bleach-1")
def _(d):
    widths = [200, 220]
    table(d, 80, 40, widths, 62, ["Water", "Drops per litre"], [["Clear", "Standard"], ["Cloudy", "Double"], ["Very cloudy", "Filter first"]], hsize=16)
    for i in range(3):
        d.piece("water-drop", 84, 100 + i * 62 + 4, 44)
    d.piece("do-not", 520, 170, 54)
    caption(d, "Very cloudy water must be filtered before any dose.", 320)


@design("WTR/disinfecting-water-with-bleach-2")
def _(d):
    d.piece("bottle", 30, 70, 130)
    lab(d, "Bleach", 95, 215)
    d.arrow(170, 125, 240, 125)
    d.piece("jerrycan", 250, 50, 150)
    lab(d, "10 litres", 325, 215)
    d.piece("spoon", 460, 80, 150)
    lab(d, "1/4 teaspoon", 535, 215)
    d.arrow(470, 150, 410, 120, width=3)
    caption(d, "Large volumes use a spoon, not drops.")


@design("WTR/disinfecting-water-with-bleach-3")
def _(d):
    d.piece("jerrycan", 20, 100, 170)
    levels = [("None", 70), ("Faint chlorine", 150), ("Strong chlorine", 230)]
    for s, y in levels:
        chip(d, 330, y, 190, 52, s)
    d.arrow(200, 165, 222, 165, width=3)
    d.tick(450, 150, 18)
    lab(d, "Target", 480, 156, "start")
    d.piece("caution", 440, 205, 50)
    d.arrow(500, 230, 520, 230, width=3)
    chip(d, 570, 230, 100, 44, "Let it\nstand", size=15)
    caption(d, "Faint is the target; strong means stand uncovered.", 334)


@design("WTR/distillation-at-home-1")
def _(d):
    d.piece("weight", 285, 6, 70)
    d.piece("pot-with-lid", 250, 52, 140)
    lab(d, "Cold lid with weight", 400, 40, "start")
    d.arrow(320, 168, 320, 196, width=3)
    d.piece("bowl", 270, 198, 100)
    lab(d, "Bowl", 380, 240, "start")
    d.piece("grate", 270, 266, 100)
    lab(d, "Rack", 380, 308, "start")
    d.piece("pool", 30, 190, 150)
    lab(d, "Water", 105, 316)
    d.arrow(150, 200, 244, 120, width=3)
    lab(d, "Vapour", 140, 140, "end")


@design("WTR/distillation-at-home-2")
def _(d):
    items = [("pool", "Rising"), ("water-drop", "Beading"), ("weight", "Centre"), ("bowl", "Drip")]
    w = 120
    gap = (640 - 4 * w) / 5
    for i, (p, s) in enumerate(items):
        x = gap + i * (w + gap)
        d.piece(p, x, 100, w)
        lab(d, s, x + w / 2, 230)
        if i < 3:
            d.arrow(x + w + 4, 145, x + w + gap - 4, 145)
    caption(d, "The weight centres the drip.", 300)


@design("WTR/distillation-at-home-3")
def _(d):
    rows = [("Wipe lid underside", "pot-with-lid"), ("Wipe bowl", "bowl"), ("Wash output container", "jerrycan")]
    for i, (s, p) in enumerate(rows):
        y = 30 + i * 100
        d.piece("do", 24, y + 10, 70)
        chip(d, 310, y + 45, 280, 56, s, size=17)
        d.piece(p, 480, y - 2, 120)
    caption(d, "Clean the still itself before each run, not only the output container.", 344)


@design("WTR/filtering-water-at-home-1")
def _(d):
    d.piece("bucket", 20, 90, 200)
    d.piece("water-drop", 366, 6, 44)
    d.arrow(388, 56, 388, 74, width=3)
    layers = [("Gravel", SAND), ("Coarse sand", SAND), ("Fine sand", YELLOW), ("Cloth", CREAM)]
    for i, (s, f) in enumerate(layers):
        d.rect(290, 80 + i * 56, 200, 56, fill=f, rx=4)
        lab(d, s, 390, 114 + i * 56)
    d.arrow(215, 160, 280, 160, width=3)
    lab(d, "Bucket", 120, 270)
    d.leader(540, 220, 484, 220)
    lab(d, "Last\ncleaning", 548, 216, "start", 15)
    caption(d, "Fine sand sits just above the cloth, so it does the last cleaning.", 346)


@design("WTR/filtering-water-at-home-2")
def _(d):
    d.piece("bucket", 255, 0, 130)
    lab(d, "Pour", 395, 60, "start")
    d.arrow(320, 98, 320, 114, width=3)
    layers = ["Gravel", "Coarse sand", "Fine sand", "Cloth"]
    for i, s in enumerate(layers):
        d.rect(220, 116 + i * 38, 200, 38, fill=SAND if i < 3 else CREAM, rx=4)
        lab(d, s, 320, 141 + i * 38)
    d.arrow(320, 274, 320, 292, width=3)
    d.piece("jar", 270, 290, 80)
    d.piece("water-drop", 366, 298, 34)
    lab(d, "Clean jug", 410, 332, "start")


@design("WTR/filtering-water-at-home-3")
def _(d):
    d.arrow(100, 290, 100, 40, width=4)
    d.arrow(100, 290, 590, 290, width=4)
    lab(d, "Clear", 90, 62, "end")
    lab(d, "Cloudy", 90, 285, "end")
    for i, x in enumerate([200, 340, 480]):
        d.line(x, 284, x, 296, width=3)
        lab(d, f"Pass {i + 1}", x, 318)
    d.path("M140 270C220 130 280 100 590 90", stroke=BLUE, width=5)
    d.piece("water-drop", 112, 250, 32)
    d.line(340, 60, 340, 284, dash="8 6", width=3)
    d.piece("threshold", 300, 14, 80)


@design("WTR/finding-water-in-an-emergency-1")
def _(d):
    chip(d, 170, 40, 220, 40, "Indoor: check first", size=16, fill=YELLOW)
    d.piece("jerrycan", 40, 80, 120)
    lab(d, "Heater tank", 100, 205)
    d.piece("toilet-cistern", 190, 80, 120)
    lab(d, "Toilet cistern", 250, 205)
    chip(d, 490, 40, 220, 40, "Outdoor: treat", size=16, fill=YELLOW)
    d.piece("rain", 400, 80, 110)
    lab(d, "Rain", 455, 205)
    d.piece("river", 530, 80, 100)
    lab(d, "River", 580, 205)
    d.line(340, 30, 340, 250, dash="8 6", width=3)
    caption(d, "Indoor stores come first; outdoor sources need treatment.", 300)


@design("WTR/finding-water-in-an-emergency-2")
def _(d):
    d.piece("shrub", 20, 80, 130)
    d.piece("water-drop", 70, 40, 34)
    lab(d, "Dew", 85, 215)
    d.curve_arrow("M160 130 C 180 100 200 100 220 125", (220, 125), 0.9, width=4)
    d.piece("cloth", 215, 80, 130)
    lab(d, "Drag cloth", 280, 215)
    d.arrow(350, 130, 400, 130)
    chip(d, 450, 130, 90, 44, "Wring")
    d.arrow(500, 130, 520, 130)
    d.piece("cup", 515, 85, 100)
    lab(d, "Cup", 565, 215)
    caption(d, "Dew comes in small amounts: wring often to fill a cup.", 300)


@design("WTR/finding-water-in-an-emergency-3")
def _(d):
    d.piece("jerrycan", 250, 6, 130)
    lab(d, "Tank", 390, 60, "start")
    d.arrow(315, 104, 315, 150)
    d.piece("water-drop", 340, 112, 30)
    d.piece("bucket", 250, 150, 130)
    lab(d, "Bucket", 315, 270)
    chip(d, 110, 70, 150, 44, "Power on")
    d.piece("do-not", 190, 45, 50)
    lab(d, "Power off first", 110, 120)
    chip(d, 520, 200, 200, 56, "Check first flow:\ncool, clear", size=15)
    d.arrow(420, 200, 392, 200, width=3)


@design("WTR/finding-water-in-an-emergency-4")
def _(d):
    d.piece("slope", 20, 60, 190)
    lab(d, "Slope", 115, 215)
    d.leader(160, 44, 192, 80)
    lab(d, "Ridge", 150, 44, "end")
    d.arrow(225, 130, 275, 150)
    d.piece("pool", 270, 80, 150)
    lab(d, "Hollow", 345, 215)
    d.arrow(425, 150, 465, 150)
    d.piece("stream-bed", 470, 70, 150)
    lab(d, "Stream", 545, 215)
    d.line(16, 245, 624, 245, width=4)
    caption(d, "Low ground and streambeds hold water: search the valley.", 300)


@design("WTR/rain-water-catchment-1")
def _(d):
    xs = [16, 138, 260, 382, 504]
    d.piece("rain", 20, 20, 100)
    d.piece("roof", 16, 90, 110)
    lab(d, "Roof", 71, 205)
    d.piece("gutter", 138, 90, 110)
    lab(d, "Gutter mesh", 193, 205)
    d.piece("downpipe", 260, 90, 110)
    lab(d, "Downpipe", 315, 205)
    chip(d, 437, 140, 100, 44, "First\nflush", size=15)
    d.piece("barrel", 504, 80, 120)
    lab(d, "Tank", 564, 205)
    for a, b in [(122, 134), (250, 258), (372, 382), (488, 502)]:
        d.arrow(a, 135, b, 135, width=3)
    caption(d, "Clean water reaches the tank only after the diverter.", 300)


@design("WTR/rain-water-catchment-2")
def _(d):
    chip(d, 170, 40, 150, 40, "First flush", size=16)
    d.arrow(170, 62, 170, 92)
    d.piece("standpipe", 100, 90, 140)
    lab(d, "Standpipe", 170, 225)
    lab(d, "Slow drain", 170, 247, size=15)
    d.piece("water-drop", 250, 120, 34)
    d.arrow(250, 170, 380, 170)
    lab(d, "Outlet", 315, 155)
    d.piece("barrel", 400, 100, 150)
    lab(d, "Tank", 475, 235)
    caption(d, "Dirty water stays in the pipe; clean water passes on.", 330)


@design("WTR/rain-water-catchment-3")
def _(d):
    d.piece("barrel", 170, 60, 300)
    d.line(170, 240, 470, 240, width=4)
    d.leader(210, 66, 296, 76)
    lab(d, "Lid", 200, 62, "end")
    d.leader(440, 100, 378, 112)
    lab(d, "Fill date", 450, 106, "start")
    d.leader(210, 166, 262, 170)
    lab(d, "Tap", 200, 172, "end")
    d.leader(440, 212, 366, 216)
    lab(d, "Sediment", 450, 218, "start")
    caption(d, "The raised tap keeps sediment from being drawn off.", 330)


@design("WTR/rain-water-catchment-4")
def _(d):
    d.piece("rain", 20, 60, 120)
    lab(d, "Rainfall mm", 80, 170)
    lab(d, "x", 165, 120, size=24)
    d.piece("roof", 190, 60, 120)
    lab(d, "Roof area m2", 250, 170)
    d.arrow(320, 105, 360, 105, width=3)
    d.piece("gutter", 365, 60, 110)
    lab(d, "Gutter run", 420, 170)
    d.arrow(480, 105, 505, 105, width=3)
    d.piece("barrel", 500, 50, 120)
    lab(d, "Tank: litres", 560, 160)
    caption(d, "Area times rainfall gives litres: a small roof collects little.", 300)


@design("WTR/rationing-water-for-hygiene-1")
def _(d):
    tiers = [("Drinking", 200), ("Cooking", 270), ("Hand washing and wounds", 340), ("Body washing", 410), ("Laundry", 480)]
    for i, (s, w) in enumerate(tiers):
        chip(d, 300, 76 + i * 56, w, 48, s, size=16, fill=BLUE if i == 0 else CREAM)
    d.piece("water-drop", 278, 0, 44)
    d.arrow(590, 60, 590, 290, width=4)
    lab(d, "Cut first", 590, 318, size=15)
    lab(d, "Last", 590, 50, size=15)


@design("WTR/rationing-water-for-hygiene-2")
def _(d):
    d.piece("bowl", 60, 100, 190)
    lab(d, "Soapy wash", 155, 250)
    d.arrow(270, 170, 350, 170)
    d.piece("bowl", 370, 100, 190)
    lab(d, "Rinse with boiled water", 465, 250)
    d.piece("water-drop", 445, 36, 44)
    lab(d, "Dishes", 320, 60)
    caption(d, "Two bowls and a small rinse keep water use low.", 320)


@design("WTR/rationing-water-for-hygiene-3")
def _(d):
    d.piece("cloth", 16, 40, 130)
    lab(d, "Clean cloth", 81, 160)
    d.piece("soap", 160, 40, 130)
    lab(d, "Soap", 225, 160)
    d.piece("bowl", 305, 40, 130)
    d.piece("water-drop", 350, 18, 36)
    lab(d, "Clean water", 370, 160)
    d.arrow(445, 100, 490, 100, width=3)
    d.piece("jar", 500, 50, 120)
    lab(d, "Wounds only", 560, 160)
    d.piece("bucket", 160, 200, 110)
    d.piece("do-not", 275, 230, 46)
    lab(d, "Drinking bucket", 215, 320)


@design("WTR/rationing-water-for-hygiene-4")
def _(d):
    widths = [130, 110, 110, 150]
    table(d, 20, 40, widths, 56, ["Allowance\nper person", "Litres used", "Litres left", "Where we\nstruggled"], [[""] * 4, [""] * 4])
    d.piece("note", 546, 100, 80)
    caption(d, "Shows where the allowance runs out first, so plan changes before a shortage.", 300)


@design("WTR/recognising-contaminated-water-1")
def _(d):
    for i, s in enumerate(["Smell", "Colour", "Surface", "Life", "Location"]):
        y = 44 + i * 56
        chip(d, 320, y, 240, 46, s, size=17)
        d.piece("do", 130, y - 22, 44)
        d.piece("do-not", 466, y - 22, 44)
    caption(d, "One failed sign rules the source out, even when the water looks clear.", 346)


@design("WTR/recognising-contaminated-water-2")
def _(d):
    d.piece("glass", 235, 70, 170)
    d.piece("do", 70, 80, 60)
    lab(d, "Clear", 100, 165)
    d.arrow(140, 110, 230, 130, width=3)
    d.piece("do-not", 510, 80, 60)
    lab(d, "Cloudy or film", 540, 165)
    d.arrow(500, 110, 410, 130, width=3)
    chip(d, 320, 270, 300, 46, "Smell after settling", size=17)
    caption(d, "Judge in a clear glass, not a bottle.", 340)


@design("WTR/recognising-contaminated-water-3")
def _(d):
    d.piece("bottle", 30, 90, 140)
    lab(d, "Sample", 100, 230)
    d.arrow(180, 130, 270, 90)
    chip(d, 340, 80, 130, 44, "Visual check", size=16)
    d.piece("do-not", 430, 58, 44)
    d.arrow(180, 160, 270, 210)
    chip(d, 355, 215, 160, 60, "Lab test\nLead, Nitrates", size=16)
    d.piece("do", 460, 192, 44)
    caption(d, "Visual checks miss dissolved chemicals.", 320)


@design("WTR/recognising-contaminated-water-4")
def _(d):
    d.piece("glass", 120, 60, 210)
    lab(d, "Surface film", 355, 80, "start")
    d.leader(345, 76, 257, 74)
    d.piece("caution", 470, 54, 54)
    lab(d, "Clear band", 355, 150, "start")
    d.leader(345, 146, 257, 140)
    d.piece("water-drop", 475, 112, 40)
    lab(d, "Silt", 355, 222, "start")
    d.leader(345, 218, 255, 170)
    d.piece("caution", 470, 190, 54)


@design("WTR/solar-disinfection-sodis-1")
def _(d):
    d.piece("bottle", 20, 140, 110)
    d.arrow(130, 230, 610, 230, width=4)
    d.piece("timeline-marker", 230, 150, 80)
    lab(d, "Strong sun\n6 hours", 270, 280)
    d.piece("timeline-marker", 470, 150, 80)
    lab(d, "Overcast\n2 days", 510, 280)
    caption(d, "Sky cover, not the clock, sets the wait.", 346)


@design("WTR/solar-disinfection-sodis-2")
def _(d):
    d.piece("sun", 20, 20, 120)
    lab(d, "Sun angle", 80, 150)
    d.arrow(150, 70, 280, 110, width=4)
    d.piece("bottle", 280, 70, 110)
    lab(d, "Bottle", 335, 182)
    d.piece("slope", 400, 130, 180)
    d.piece("tip", 550, 100, 60)
    lab(d, "Dark surface", 490, 290)
    caption(d, "Steep full sun and a dark base add winter heat.", 340)


@design("WTR/solar-disinfection-sodis-3")
def _(d):
    d.piece("bottle", 260, 60, 150)
    rays = [("UV", 60, 75), ("Heat", 100, 95), ("Clear wall", 140, 115)]
    for s, y, e in rays:
        d.arrow(150, y, 300, e, width=3)
        lab(d, s, 140, y + 6, "end")
    chip(d, 540, 130, 150, 56, "Cloudy bottle", size=16)
    d.piece("do-not", 515, 170, 50)
    lab(d, "Blocks light", 540, 240, size=15)
    caption(d, "Light passes clear walls; cloudy water blocks it.", 330)


@design("WTR/solar-disinfection-sodis-4")
def _(d):
    d.curve_arrow("M70 260 C 150 40 490 40 570 255", (570, 255), 1.9, width=5)
    lab(d, "East", 60, 295)
    lab(d, "West", 590, 295)
    d.piece("bottle", 275, 100, 90)
    lab(d, "Midday", 320, 195)
    d.piece("threshold", 285, 14, 70)
    d.piece("compass", 20, 20, 100)
    d.piece("shadow-stick", 420, 190, 100)
    lab(d, "Shade", 470, 300)


@design("WTR/storing-water-for-two-weeks-1")
def _(d):
    chip(d, 170, 36, 220, 40, "Cool dark corner", size=16, fill=YELLOW)
    d.piece("jerrycan", 110, 70, 120)
    lab(d, "Water", 170, 190)
    d.piece("tray", 110, 200, 120)
    lab(d, "Tray", 170, 310)
    d.line(340, 20, 340, 320, dash="8 6", width=4)
    d.piece("do-not", 315, 150, 50)
    d.piece("shelf", 410, 100, 180)
    lab(d, "Fuel", 500, 230)
    caption(d, "Water and fuel never share a shelf.", 346)


@design("WTR/storing-water-for-two-weeks-2")
def _(d):
    widths = [180, 180, 180]
    table(d, 50, 40, widths, 70, ["Fill date", "Check date", "Replace date\n6 months on"], [[""] * 3 for _ in range(3)])
    for r in range(3):
        for c in range(3):
            d.piece("timeline-marker", 50 + c * 180 + 50, 114 + r * 70, 70)
    caption(d, "Every container runs the same cycle, so the oldest is always visible.", 346)


@design("WTR/storing-water-for-two-weeks-3")
def _(d):
    rows = [("Oldest front", 20), ("Newer", 115), ("Add at back", 210)]
    for s, y in rows:
        d.piece("jerrycan", 200, y, 100)
        d.line(170, y + 82, 480, y + 82, width=4)
        lab(d, s, 330, y + 50, "start")
    d.piece("step-1", 150, 22, 70)
    d.arrow(570, 300, 570, 40, width=4)
    lab(d, "Use order", 570, 328, size=15)


@design("WTR/water-after-a-flood-1")
def _(d):
    d.piece("decision", 270, 0, 100)
    lab(d, "Water source?", 320, 108, size=15)
    cols = [(90, "Floodwater", "Discard", "do-not"), (230, "Tap", "Boil", None), (370, "Well", "Disinfect", None), (530, "Sealed bottles", "Drink", "do")]
    for cx, src, out, mark in cols:
        d.line(320, 120, cx, 150, width=3)
        chip(d, cx, 175, 130, 44, src, size=15)
        d.arrow(cx, 199, cx, 238, width=3)
        chip(d, cx, 262, 120, 44, out, size=16, fill=SAND if mark is None else CREAM)
        if mark:
            d.piece(mark, cx - 20, 286, 40)


@design("WTR/water-after-a-flood-2")
def _(d):
    xs = [15, 140, 265, 390, 515]
    d.piece("step-1", xs[0], 70, 100)
    lab(d, "Dose", xs[0] + 50, 190)
    d.piece("step-2", xs[1], 70, 100)
    lab(d, "Wait", xs[1] + 50, 190)
    d.piece("step-3", xs[2], 70, 100)
    lab(d, "Pump until\nsmell fades", xs[2] + 50, 190, size=15)
    d.piece("decision", xs[3], 70, 100)
    lab(d, "Test", xs[3] + 50, 190)
    d.piece("do", xs[4], 70, 100)
    lab(d, "Drink", xs[4] + 50, 190)
    for i in range(4):
        d.arrow(xs[i] + 98, 115, xs[i + 1] + 2, 115, width=3)
    d.curve_arrow("M440 235 C 440 300 315 300 315 240", (315, 240), -1.57, width=4)
    caption(d, "The test is the last gate before drinking, not the pump.", 340)


@design("WTR/water-after-a-flood-3")
def _(d):
    d.piece("bucket", 16, 90, 120)
    d.piece("warning", 56, 30, 50)
    lab(d, "Flood contact", 76, 215, size=15)
    names = ["Scrub", "Rinse", "Disinfect", "Dry"]
    for i, s in enumerate(names):
        cx = 210 + i * 115
        chip(d, cx, 140, 90, 48, s, size=16)
        d.arrow(cx - 70 if i else 140, 140, cx - 47, 140, width=3)
    caption(d, "A flood-contact container is cleaned in full before reuse.", 300)


@design("WTR/water-after-a-flood-4")
def _(d):
    d.arrow(30, 240, 610, 240, width=4)
    xs = [70, 190, 320, 440, 560]
    names = ["Rises", "Recedes", "Cleaning", "Testing", "Drinking\nallowed"]
    for x, s in zip(xs, names):
        d.circle(x, 240, 9, fill=INK)
        lab(d, s, x, 285, size=15)
    d.piece("river", 20, 130, 110)
    d.piece("waves", 140, 130, 110)
    d.piece("do", 520, 130, 80)
    caption(d, "Safe drinking water comes last, not when the water recedes.", 346)
