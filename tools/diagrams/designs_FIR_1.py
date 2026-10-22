import math

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


def ring(d, cx, cy, r, dash="10 8", color=INK, width=3):
    d.path(f"M{cx - r} {cy}A{r} {r} 0 1 0 {cx + r} {cy}A{r} {r} 0 1 0 {cx - r} {cy}", stroke=color, width=width, dash=dash)


@design("FIR/campfire-cooking-safety-1")
def _(d):
    ring(d, 300, 190, 140)
    d.piece("coals", 210, 125, 150)
    for x, y in [(250, 105), (250, 232), (180, 167), (320, 167)]:
        d.piece("rock", x, y, 70)
    d.piece("tripod-pot", 345, 150, 120)
    d.piece("bucket", 170, 225, 90)
    d.leader(120, 70, 255, 110)
    d.text("Cleared circle", 120, 64, size=16, weight=600, anchor="end")
    d.leader(110, 150, 200, 190)
    d.text("Stone ring", 100, 156, size=16, weight=600, anchor="end")
    d.leader(560, 100, 436, 120)
    d.text("2 m boundary", 500, 92, size=16, weight=600, anchor="start")
    d.leader(110, 290, 190, 262)
    d.text("Water", 100, 296, size=16, weight=600, anchor="end")


@design("FIR/carbon-monoxide-never-burn-indoors-1")
def _(d):
    d.piece("room", 30, 40, 280)
    d.piece("room", 330, 40, 280)
    d.piece("stove", 62, 128, 100)
    d.piece("warning", 140, 100, 48)
    d.arrow(175, 170, 250, 140, width=3)
    d.arrow(175, 180, 270, 180, width=3)
    d.arrow(175, 190, 250, 225, width=3)
    d.arrow(320, 170, 420, 170, width=3)
    d.arrow(320, 190, 430, 230, width=3)
    d.arrow(320, 150, 410, 120, width=3)
    d.text("Charcoal stove", 90, 288, size=16, weight=600)
    d.text("Gas in every room", 320, 320, size=16, weight=600)
    d.leader(560, 300, 505, 80)
    d.text("Window ajar", 580, 316, size=16, weight=600)
    caption(d, "Gas fills the whole house.", 346)


@design("FIR/carbon-monoxide-never-burn-indoors-2")
def _(d):
    d.line(320, 40, 320, 300, dash="6 8")
    d.piece("room", 30, 60, 270)
    d.arrow(100, 170, 100, 110, width=3)
    d.arrow(160, 170, 160, 110, width=3)
    d.piece("warning", 210, 120, 48)
    d.text("Sealed room", 165, 290, size=17, weight=600)
    d.text("Gas at ceiling", 165, 52, size=16, weight=600)
    d.piece("door", 360, 70, 190)
    d.curve_arrow("M510 200C535 120 585 120 610 175", (610, 175), 1.0, width=4)
    d.text("Open door", 465, 290, size=17, weight=600)
    caption(d, "An ajar window does not make a sealed room safe.", 336)


@design("FIR/carbon-monoxide-never-burn-indoors-3")
def _(d):
    d.piece("hut", 20, 70, 230)
    d.piece("generator", 400, 118, 120)
    d.line(16, 222, 624, 222, width=3)
    d.arrow(236, 258, 410, 258, width=3)
    d.arrow(410, 258, 236, 258, width=3)
    d.text("Distance", 323, 290, size=16, weight=600)
    d.arrow(505, 180, 600, 180, width=4)
    d.text("Exhaust", 552, 166, size=16, weight=600)
    d.arrow(330, 60, 480, 60, width=3, color=BLUE)
    d.text("Wind", 405, 48, size=16, weight=600, fill=BLUE)
    d.piece("do-not", 275, 130, 56)
    caption(d, "Distance and wind direction matter, not just being outdoors.", 340)


@design("FIR/carbon-monoxide-never-burn-indoors-4")
def _(d):
    names = ["Headache", "Dizziness", "Nausea", "Drowsiness"]
    for i, n in enumerate(names):
        x = 16 + i * 154
        chip(d, x + 65, 90, 130, 64, n, size=17)
        d.line(x + 65, 122, 320 + (i - 1.5) * 50, 212)
    chip(d, 300, 240, 300, 56, "Several people unwell together", size=17)
    d.piece("warning", 470, 212, 64)
    caption(d, "Shared symptoms are the clue: get to fresh air.", 330)


@design("FIR/carbon-monoxide-never-burn-indoors-5")
def _(d):
    d.piece("person-sitting", 20, 90, 150)
    d.text("Bedrooms", 95, 232, size=16, weight=600)
    d.piece("warning", 232, 110, 76)
    d.text("Alarm", 270, 232, size=16, weight=600)
    d.arrow(150, 270, 430, 270, width=4)
    d.piece("door", 420, 70, 140)
    d.text("Exit", 490, 232, size=16, weight=600)
    d.piece("waypoint-pin", 545, 95, 90)
    d.text("Fresh air", 590, 232, size=16, weight=600)
    caption(d, "The alarm sits between sleepers and the way out.", 330)


@design("FIR/chimney-and-flue-safety-1")
def _(d):
    d.piece("flue-liner", 180, 40, 280)
    d.leader(120, 130, 312, 140)
    d.text("Flue liner", 110, 136, size=16, weight=600, anchor="end")
    d.leader(510, 190, 346, 180)
    d.text("Creosote layer", 520, 196, size=16, weight=600, anchor="start")
    d.leader(510, 60, 324, 60)
    d.text("Cap", 520, 66, size=16, weight=600, anchor="start")
    caption(d, "Deposits build out of sight while the outside looks fine.", 330)


@design("FIR/chimney-and-flue-safety-2")
def _(d):
    d.piece("chimney", 210, 120, 220)
    chip(d, 338, 160, 90, 30, "Cap", size=16)
    d.cross(145, 88, 12)
    d.text("Rain", 118, 94, size=16, weight=600, anchor="end")
    d.arrow(172, 90, 300, 148, width=3)
    d.cross(525, 88, 12)
    d.text("Birds", 545, 94, size=16, weight=600, anchor="start")
    d.arrow(500, 90, 374, 148, width=3)
    d.arrow(337, 140, 337, 72, width=3)
    d.tick(337, 50, 12)
    d.text("Smoke out", 358, 56, size=16, weight=600, anchor="start")
    caption(d, "Check the cap for blockage each season.", 336)


@design("FIR/chimney-and-flue-safety-3")
def _(d):
    d.piece("step-1", 110, 215, 90)
    d.piece("step-2", 110, 45, 90)
    d.arrow(155, 210, 155, 130, width=4)
    d.text("Start at base", 220, 260, size=17, weight=600, anchor="start")
    d.text("Cover opening", 220, 90, size=17, weight=600, anchor="start")
    d.piece("cloth", 420, 40, 130)
    caption(d, "Base first, and the opening covered.", 336)


@design("FIR/chimney-and-flue-safety-4")
def _(d):
    d.piece("flue-liner", 200, 40, 240)
    d.arrow(60, 190, 232, 190, width=4, color=BLUE)
    d.text("Cold air in", 60, 172, size=16, weight=600, anchor="start", fill=BLUE)
    d.arrow(430, 200, 430, 60, width=4, color=RED)
    d.text("Warm air rises", 445, 120, size=16, weight=600, anchor="start", fill=RED)
    d.piece("thermometer", 520, 170, 100)
    caption(d, "A cold flue draws poorly.", 336)


@design("FIR/chimney-fires-1")
def _(d):
    d.piece("stove", 190, 90, 260)
    d.piece("flame", 307, 45, 80)
    d.leader(500, 70, 372, 76)
    d.text("Flames", 510, 76, size=16, weight=600, anchor="start")
    d.leader(500, 140, 340, 135)
    d.text("Creosote", 510, 146, size=16, weight=600, anchor="start")
    d.arrow(60, 205, 238, 205, width=4)
    d.text("Air in", 60, 189, size=16, weight=600, anchor="start")
    d.cross(120, 245, 14)
    caption(d, "Closing the air supply starves the fire.", 336)


@design("FIR/evacuating-from-a-wildfire-1")
def _(d):
    labels = ["Warning\nreceived", "Go bag and\nmedicines", "Windows and\ndoors closed,\nunlocked", "Gas off", "Leave by\nofficial route"]
    for i, s in enumerate(labels):
        x = 16 + i * 127
        chip(d, x + 50, 170, 100, 100, s, size=15)
        d.badge(i + 1, x + 50, 100, 16)
        if i < 4:
            d.arrow(x + 104, 170, x + 123, 170, width=3)
    caption(d, "Leaving follows the warning at once.", 330)


@design("FIR/evacuating-from-a-wildfire-2")
def _(d):
    d.rect(24, 24, 592, 292, fill=CREAM, rx=14)
    d.piece("flame", 125, 100, 90)
    ring(d, 170, 150, 62, width=3)
    d.text("Fire zone", 170, 240, size=16, weight=600)
    d.arrow(250, 110, 440, 125, width=4)
    d.text("Primary route", 345, 98, size=16, weight=600)
    d.curve_arrow("M225 205C300 290 430 290 485 215", (485, 215), -0.94, width=4)
    d.text("Alternate route", 350, 300, size=16, weight=600)
    d.piece("waypoint-pin", 465, 100, 100)
    d.text("Meeting point", 568, 240, size=16, weight=600)
    d.piece("compass-rose", 520, 30, 90)
    caption(d, "Plan two routes and a destination off the fire's path.", 340)


@design("FIR/evacuating-from-a-wildfire-3")
def _(d):
    d.piece("car", 30, 130, 240)
    d.piece("flame", 285, 130, 90)
    d.text("Smoke ahead", 330, 265, size=16, weight=600)
    d.piece("fan", 440, 130, 150)
    d.curve_arrow("M455 125C470 70 570 70 585 125", (585, 125), 1.3, width=4)
    d.text("Recirculate", 515, 265, size=16, weight=600)
    caption(d, "Keep smoke out of the cabin while driving slowly.", 335)


@design("FIR/evacuating-from-a-wildfire-4")
def _(d):
    d.piece("room", 150, 30, 340)
    d.piece("wet-towel", 232, 222, 90)
    d.piece("bucket", 370, 100, 100)
    d.piece("do-not", 170, 90, 44)
    d.piece("do-not", 400, 45, 44)
    d.leader(110, 300, 262, 262)
    d.text("Wet towels", 110, 322, size=16, weight=600, anchor="end")
    d.leader(540, 170, 452, 170)
    d.text("Water", 550, 176, size=16, weight=600, anchor="start")
    d.leader(100, 104, 170, 112)
    d.text("No-go walls", 100, 98, size=16, weight=600, anchor="end")


@design("FIR/fire-in-a-storm-or-wind-1")
def _(d):
    ring(d, 330, 185, 140)
    d.piece("coals", 230, 130, 140)
    d.piece("rock", 120, 95, 90)
    d.piece("rock", 120, 160, 90)
    d.piece("log-stack", 375, 135, 100)
    d.piece("survivor-mark", 275, 245, 70)
    d.arrow(20, 185, 115, 185, width=4, color=BLUE)
    d.text("Wind", 68, 168, size=16, weight=600, fill=BLUE)
    d.leader(70, 280, 165, 215)
    d.text("Windbreak", 70, 302, size=16, weight=600)
    d.leader(490, 80, 436, 105)
    d.text("Clear circle", 500, 76, size=16, weight=600, anchor="start")
    d.leader(520, 262, 430, 215)
    d.text("Spare wood", 520, 284, size=16, weight=600, anchor="start")


@design("FIR/fire-layouts-1")
def _(d):
    d.piece("tinder-pile", 240, 190, 170)
    d.piece("flame", 290, 125, 80)
    chip(d, 360, 80, 130, 40, "Kindling", size=16)
    d.line(250, 110, 250, 260, dash="8 7", width=3)
    d.arrow(40, 215, 235, 215, width=4, color=BLUE)
    d.text("Wind", 100, 197, size=16, weight=600, fill=BLUE)
    d.leader(110, 285, 250, 250)
    d.text("Open side", 110, 307, size=16, weight=600)
    d.leader(560, 285, 390, 255)
    d.text("Tinder", 560, 307, size=16, weight=600, anchor="start")
    caption(d, "The open side faces the wind so air reaches the flame.", 338)


@design("FIR/fire-layouts-2")
def _(d):
    d.piece("log-stack", 50, 30, 160)
    d.text("Layer 1", 130, 170, size=16, weight=600)
    d.piece("arrow-curved", 250, 40, 100)
    d.text("turn 90°", 300, 150, size=16, weight=600)
    d.piece("log-stack", 390, 30, 160)
    d.text("Layer 2", 470, 170, size=16, weight=600)
    d.piece("tinder-pile", 235, 185, 170)
    d.arrow(60, 270, 215, 270, width=3)
    d.arrow(580, 270, 425, 270, width=3)
    d.text("Air gaps", 320, 325, size=16, weight=600)


@design("FIR/fire-layouts-3")
def _(d):
    d.piece("coals", 245, 130, 150)
    d.piece("log-stack", 60, 120, 110)
    d.piece("log-stack", 470, 120, 110)
    d.piece("log-stack", 265, 10, 110)
    d.piece("log-stack", 265, 262, 110)
    d.arrow(170, 190, 245, 190, width=4)
    d.arrow(470, 190, 395, 190, width=4)
    d.arrow(320, 108, 320, 138, width=4)
    d.arrow(320, 284, 320, 238, width=4)
    d.leader(555, 290, 376, 224)
    d.text("Coal bed", 560, 300, size=16, weight=600, anchor="start")
    d.leader(100, 85, 112, 150)
    d.text("Logs", 100, 70, size=16, weight=600)
    d.text("Push inward", 210, 226, size=16, weight=600)


@design("FIR/fire-layouts-4")
def _(d):
    d.piece("stream-bed", 10, 91, 330)
    d.piece("tripod-pot", 360, 100, 150)
    d.piece("coals", 395, 145, 80)
    d.arrow(30, 140, 330, 140, width=4, color=BLUE)
    d.text("Wind", 180, 122, size=16, weight=600, fill=BLUE)
    d.leader(60, 310, 90, 255)
    d.text("Trench", 60, 332, size=16, weight=600)
    d.leader(560, 290, 448, 205)
    d.text("Downwind end", 560, 312, size=16, weight=600)




@design("FIR/fire-safety-at-home-1")
def _(d):
    d.piece("room", 170, 50, 300)
    d.arrow(280, 215, 280, 300, width=4)
    d.text("Exit 1", 280, 326, size=16, weight=600)
    d.arrow(323, 120, 323, 40, width=4)
    d.text("Exit 2", 345, 54, size=16, weight=600, anchor="start")
    d.piece("warning", 385, 100, 56)
    d.piece("blanket", 232, 108, 80)
    d.leader(540, 120, 440, 130)
    d.text("Alarm", 550, 126, size=16, weight=600, anchor="start")
    d.leader(110, 150, 248, 143)
    d.text("Blanket", 110, 172, size=16, weight=600, anchor="middle")


@design("FIR/fire-safety-at-home-2")
def _(d):
    d.piece("blanket", 20, 100, 120)
    d.text("Blanket", 80, 215, size=16, weight=600)
    d.piece("hob", 165, 100, 140)
    d.text("Hob", 235, 215, size=16, weight=600)
    d.piece("bucket", 335, 100, 100)
    d.text("Sand", 385, 215, size=16, weight=600)
    d.piece("door", 490, 90, 130)
    d.text("Exit", 555, 215, size=16, weight=600)
    d.arrow(60, 270, 550, 270, width=4)
    d.text("Clear path", 305, 258, size=16, weight=600)
    caption(d, "Keep the exit free while fighting a small fire.", 335)


@design("FIR/fire-safety-at-home-3")
def _(d):
    ring(d, 200, 170, 105)
    d.piece("warning", 172, 90, 60)
    d.text("Alarm", 202, 168, size=16, weight=600)
    d.arrow(60, 240, 440, 240, width=4)
    d.text("Escape route", 360, 224, size=16, weight=600)
    d.piece("door", 460, 120, 130)
    d.text("Door", 525, 275, size=16, weight=600)
    caption(d, "The alarm should cover the route out, not just the kitchen.", 335)


@design("FIR/fire-safety-at-home-4")
def _(d):
    d.piece("room", 10, 70, 250)
    d.piece("tree", 280, 10, 130)
    d.piece("shrub", 300, 215, 90)
    d.arrow(235, 155, 465, 155, width=4)
    d.arrow(235, 215, 465, 215, width=4)
    d.text("Exit 1", 300, 145, size=16, weight=600)
    d.text("Exit 2", 300, 205, size=16, weight=600)
    d.piece("waypoint-pin", 480, 120, 100)
    d.text("Meeting point", 545, 260, size=16, weight=600)


@design("FIR/fire-starters-for-damp-wood-1")
def _(d):
    d.piece("log-stack", 30, 60, 230)
    d.leader(200, 290, 144, 192)
    d.text("Dry core", 200, 312, size=16, weight=600, anchor="start")
    d.leader(70, 288, 88, 192)
    d.text("Wet outer wood", 40, 312, size=16, weight=600, anchor="start")
    d.arrow(250, 170, 385, 170, width=4)
    d.piece("tinder-pile", 390, 100, 170)
    d.text("Shavings", 480, 250, size=16, weight=600)


@design("FIR/fire-starters-for-damp-wood-3")
def _(d):
    flow(d, [("tin", "Cotton wool tin"), ("jar", "Jelly"), ("ferro-rod", "Ferro rod")], 90, w=150, arrow=False)
    caption(d, "Sealed starters stay usable in rain.", 320)


@design("FIR/fire-starters-for-damp-wood-4")
def _(d):
    d.piece("tarp-a-frame", 150, 30, 300)
    d.piece("rock", 245, 190, 110)
    d.piece("coals", 262, 165, 76)
    d.piece("rock", 460, 190, 90)
    d.text("Flat rock", 300, 320, size=16, weight=600)
    d.text("Windbreak", 505, 320, size=16, weight=600)
    d.arrow(30, 230, 150, 230, width=4, color=BLUE)
    d.text("Wind", 90, 212, size=16, weight=600, fill=BLUE)


@design("FIR/fire-watch-and-night-safety-1")
def _(d):
    for i in range(4):
        x = 16 + i * 155
        d.piece("timeline-axis", x, 150, 140)
        d.text(f"Shift {i + 1}", x + 70, 262, size=16, weight=600)
        d.piece("timeline-marker", x + 38 - 31, 163, 100)
    d.text("Round", 63, 160, size=15, weight=600)
    for i in range(3):
        bx = 16 + (i + 1) * 155 - 8
        chip(d, bx, 100, 100, 30, "Handover", size=15)
        d.line(bx, 116, bx, 209, dash="6 6", width=2)
    caption(d, "Regular rounds, with a handover at each shift change.", 335)




def table(d, x, y, widths, rowh, header, rows, size=15):
    total = sum(widths)
    d.rect(x, y, total, rowh * (len(rows) + 1), fill=CREAM, rx=8)
    d.rect(x, y, total, rowh, fill=SAND, rx=8)
    cx = x
    for i, w in enumerate(widths):
        if i:
            d.line(cx, y, cx, y + rowh * (len(rows) + 1), width=2)
        d.text(header[i], cx + w / 2, y + rowh / 2 + 5, size=size, weight=700)
        for r, row in enumerate(rows):
            d.text(row[i], cx + w / 2, y + rowh * (r + 1) + rowh / 2 + 5, size=size, weight=600 if i else 700)
        cx += w
    for r in range(len(rows)):
        d.line(x, y + rowh * (r + 1), x + total, y + rowh * (r + 1), width=2)


@design("FIR/firewood-for-weeks-1")
def _(d):
    d.piece("pallet", 215, 134, 210)
    d.piece("log-stack", 235, 80, 170)
    chip(d, 320, 80, 170, 30, "Cover top only", size=15)
    d.arrow(40, 160, 250, 160, width=3)
    d.arrow(600, 160, 390, 160, width=3)
    d.text("Air gaps", 130, 142, size=16, weight=600)
    d.text("Pallet", 320, 285, size=16, weight=600)
    caption(d, "The stack must breathe, so the sides stay open.", 335)


@design("FIR/firewood-for-weeks-2")
def _(d):
    table(d, 30, 40, [120, 105, 105, 100, 100], 48, ["Month", "Stove use", "Cooking use", "Margin", "Total m3"], [["Month 1", "", "", "", ""], ["Month 2", "", "", "", ""], ["Month 3", "", "", "", ""]])
    d.arrow(590, 100, 590, 250, width=4)
    caption(d, "Add the margin before checking the stock each month.", 320)


@design("FIR/firewood-for-weeks-3")
def _(d):
    d.piece("log-stack", 190, 40, 260)
    d.leader(90, 285, 272, 190)
    d.text("Radial checks", 90, 310, size=16, weight=600)
    d.leader(555, 255, 390, 195)
    d.text("Loosening bark", 560, 280, size=16, weight=600)
    d.leader(560, 106, 324, 110)
    d.text("End grain", 570, 100, size=16, weight=600)


@design("FIR/firewood-for-weeks-4")
def _(d):
    d.line(320, 30, 320, 300, dash="6 8")
    d.piece("log-stack", 80, 80, 170)
    d.piece("log-stack", 390, 80, 170)
    d.text("Dry", 165, 66, size=18, weight=700)
    d.text("Wet", 475, 66, size=18, weight=700)
    chip(d, 165, 240, 150, 40, "Hollow ring", size=17)
    chip(d, 475, 240, 150, 40, "Dull thud", size=17)
    d.tick(250, 140, 20)
    d.cross(560, 140, 20)
    caption(d, "Sound tells seasoning before any weighing.", 330)


@design("FIR/heat-sources-compared-1")
def _(d):
    table(d, 16, 40, [112, 100, 100, 100, 100, 96], 48, ["", "Wood", "Charcoal", "Gas", "Paraffin", "Tablets"], [["Efficiency", "Medium", "High", "High", "Good", "Low"], ["Smoke", "High", "Low", "None", "Medium", "Low"], ["Indoor risk", "Poor", "Worst", "Vent it", "Rated only", "Never"]])
    d.rect(228, 184, 100, 48, fill="none", stroke=RED, width=4, rx=6)
    d.piece("warning", 229, 193, 30)
    caption(d, "Charcoal is hot and low in smoke, yet worst indoors.", 330)


@design("FIR/indoor-warmth-from-fire-safely-1")
def _(d):
    d.piece("stove", 250, 80, 200)
    d.piece("wall", 30, 95, 170)
    d.arrow(172, 150, 286, 150, width=3)
    d.arrow(286, 150, 172, 150, width=3)
    d.text("Clearance", 230, 135, size=16, weight=600)
    d.arrow(170, 275, 300, 218, width=4, color=BLUE)
    d.text("Air in", 120, 290, size=16, weight=600, fill=BLUE, anchor="start")
    d.leader(540, 90, 395, 110)
    d.text("Flue", 550, 96, size=16, weight=600, anchor="start")
    caption(d, "The flue carries smoke out; the stove sits clear of the wall.", 335)


@design("FIR/indoor-warmth-from-fire-safely-2")
def _(d):
    d.piece("flame", 30, 90, 130)
    d.piece("barbecue", 190, 90, 130)
    d.piece("generator", 350, 90, 130)
    d.piece("door", 505, 70, 120)
    d.text("Open fire", 95, 235, size=16, weight=600)
    d.text("Barbecue", 255, 235, size=16, weight=600)
    d.text("Generator", 415, 235, size=16, weight=600)
    d.text("No flue", 565, 235, size=16, weight=600)
    for cx in (140, 300, 460):
        d.cross(cx, 100, 16)
    caption(d, "Never burn indoors.", 320)


@design("FIR/indoor-warmth-from-fire-safely-3")
def _(d):
    ring(d, 250, 175, 110)
    d.piece("stove", 180, 100, 140)
    chip(d, 250, 235, 90, 30, "Guard", size=15)
    d.piece("bed", 430, 100, 170)
    d.text("Bedding", 515, 235, size=16, weight=600)
    d.arrow(290, 170, 358, 170, width=3)
    d.arrow(358, 170, 290, 170, width=3)
    d.leader(250, 308, 250, 287)
    d.text("1 m boundary", 250, 328, size=16, weight=600)
    caption(d, "Measured from the stove, not from the wall.", 352)


@design("FIR/indoor-warmth-from-fire-safely-4")
def _(d):
    d.piece("stove", 130, 170, 170)
    d.piece("flue", 150, 20, 170)
    d.arrow(235, 168, 235, 138, width=4)
    d.piece("caution", 250, 132, 40)
    d.curve_arrow("M268 160C310 160 330 200 290 225", (290, 225), 2.4, width=4)
    d.leader(110, 270, 190, 250)
    d.text("Stove", 100, 292, size=16, weight=600)
    d.leader(150, 106, 226, 100)
    d.text("Flue", 130, 112, size=16, weight=600, anchor="end")
    d.leader(330, 36, 242, 36)
    d.text("Cap", 340, 42, size=16, weight=600, anchor="start")
    d.leader(430, 160, 295, 148)
    d.text("Leak at joint", 440, 166, size=16, weight=600, anchor="start")


@design("FIR/lighting-a-fire-without-matches-1")
def _(d):
    d.line(213, 30, 213, 330, dash="6 8")
    d.line(427, 30, 427, 330, dash="6 8")
    d.piece("ferro-rod", 40, 40, 130)
    d.piece("sun", 270, 20, 80)
    d.arrow(310, 100, 310, 135, width=3)
    chip(d, 310, 160, 80, 30, "Lens", size=15)
    d.piece("battery", 465, 40, 130)
    d.text("Ferro rod", 105, 190, size=16, weight=600)
    d.text("Lens and sun", 320, 200, size=16, weight=600)
    d.text("Battery,\nsteel wool", 530, 180, size=16, weight=600)
    d.piece("tinder-pile", 50, 220, 110)
    d.piece("tinder-pile", 265, 220, 110)
    d.piece("tinder-pile", 475, 220, 110)
    caption(d, "Each method needs a different condition.", 345)


@design("FIR/lighting-a-fire-without-matches-2")
def _(d):
    d.piece("ferro-rod", 70, 50, 190)
    d.piece("knife", 190, 40, 120)
    d.curve_arrow("M260 160C300 170 340 190 360 230", (360, 230), 1.1, width=4)
    d.piece("tinder-pile", 330, 190, 170)
    d.line(300, 300, 560, 300, width=3)
    d.leader(335, 60, 290, 82)
    d.text("Knife back", 345, 66, size=16, weight=600, anchor="start")
    d.text("Sparks", 340, 150, size=16, weight=600)
    d.text("Tinder nest", 440, 330, size=16, weight=600)


@design("FIR/lighting-a-fire-without-matches-3")
def _(d):
    d.piece("ferro-rod", 70, 70, 190)
    d.arrow(240, 160, 340, 215, width=4)
    d.piece("tinder-pile", 330, 180, 180)
    d.leader(140, 236, 140, 176)
    d.text("Low angle", 140, 258, size=16, weight=600)
    d.text("Sparks", 330, 150, size=16, weight=600)
    d.text("Tinder", 420, 330, size=16, weight=600)


@design("FIR/lighting-a-fire-without-matches-4")
def _(d):
    d.piece("battery", 200, 30, 240)
    chip(d, 320, 190, 190, 30, "Steel wool", size=15)
    d.arrow(320, 210, 320, 240, width=3)
    d.text("Glow", 345, 240, size=16, weight=600, anchor="start")
    d.piece("tinder-pile", 250, 232, 140)
    d.leader(450, 300, 372, 290)
    d.text("Dry tinder", 460, 306, size=16, weight=600, anchor="start")
    d.leader(110, 150, 250, 170)
    d.text("Terminals", 110, 144, size=16, weight=600)


@design("FIR/lighting-a-fire-without-matches-5")
def _(d):
    chip(d, 320, 50, 240, 34, "Bow", size=16)
    d.arrow(180, 90, 460, 90, width=3)
    d.arrow(460, 90, 180, 90, width=3)
    chip(d, 320, 150, 110, 34, "Spindle", size=16)
    chip(d, 320, 240, 280, 36, "Fireboard", size=16)
    d.line(320, 67, 320, 133, width=3)
    d.line(320, 167, 320, 222, width=3)
    d.piece("coals", 350, 255, 110)
    d.text("Ember", 520, 300, size=16, weight=600, anchor="start")
    d.leader(515, 295, 440, 290)
    caption(d, "The ember forms slowly, so keep the dust collecting.", 345)
