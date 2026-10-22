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


def axis(d, y, x1=40, x2=610, dots=()):
    d.arrow(x1, y, x2, y, width=4)
    for x in dots:
        d.circle(x, y, 9)


def table(d, x, y, w, heads, nrows, rh=46, size=16):
    cw = w / len(heads)
    d.rect(x, y, w, rh, fill=INK, rx=8)
    for i, h in enumerate(heads):
        d.text(h, x + cw * (i + 0.5), y + rh / 2 + size * 0.35, size=size, weight=600, fill=CREAM)
    for r in range(nrows):
        d.rect(x, y + rh * (r + 1), w, rh, fill=CREAM, rx=0)
    for i in range(1, len(heads)):
        d.line(x + cw * i, y + rh, x + cw * i, y + rh * (nrows + 1), width=2)


def decision_flow(d, start, top, top_do, bottom, bottom_warn):
    d.piece("decision", 30, 120, 150)
    d.text(start, 105, 262, size=17, weight=600)
    d.arrow(185, 165, 462, 95)
    d.text(top, 318, 110, size=16, weight=600)
    d.arrow(185, 200, 462, 262)
    d.text(bottom, 330, 292, size=16, weight=600)
    d.piece("do", 470, 40, 110)
    d.text(top_do, 525, 150, size=16, weight=600)
    d.piece("warning", 470, 215, 110)
    d.text(bottom_warn, 525, 322, size=16, weight=600)


def recovery(d, labels, cap):
    d.piece("recovery-position", 150, 30, 340)
    d.leader(100, 132, 202, 207)
    d.text(labels[2], 40, 124, size=17, weight=600, anchor="start")
    d.leader(500, 118, 400, 168)
    d.text(labels[1], 506, 124, size=17, weight=600, anchor="start")
    d.leader(320, 272, 320, 228)
    d.text(labels[0], 320, 296, size=17, weight=600)
    caption(d, cap)


@design("MED/hypoglycaemia-1")
def _(d):
    axis(d, 190, dots=(130, 320, 510))
    for x, s in ((130, "Fast sugar"), (320, "Wait and recheck"), (510, "Longer-acting food")):
        d.text(s, x, 150, size=17, weight=600)
    for i, x in enumerate((130, 320, 510)):
        d.badge(i + 1, x, 235, 18)
    caption(d, "The recheck is part of the sequence.")


@design("MED/hypoglycaemia-2")
def _(d):
    for x, p, s in ((25, "cup", "Half a cup\nof juice"), (225, "spoon", "A spoon\nof sugar"), (425, "pills", "Glucose\ntablets")):
        d.piece(p, x, 60, 190)
        d.text(s, x + 95, 235, size=17, weight=600)
    caption(d, "No clinic needed.")


@design("MED/hypoglycaemia-3")
def _(d):
    table(d, 40, 60, 560, ["Time", "Reading before", "Treatment given", "Reading after"], 3, rh=52, size=15)
    caption(d, "Each dose is recorded for the next helper.")


@design("MED/hypoglycaemia-4")
def _(d):
    xs = (90, 205, 320, 435, 550)
    axis(d, 200, dots=xs)
    for x, s in zip(xs, ("Meal", "Snack", "Meal", "Snack", "Meal")):
        chip(d, x, 130, 90, 44, s, fill=YELLOW if s == "Meal" else CREAM)
        d.line(x, 152, x, 190, width=2)
    d.text("Day", 600, 235, size=16, weight=600, anchor="end")
    caption(d, "Regular eating prevents low sugar.")


@design("MED/hypoglycaemia-5")
def _(d):
    recovery(d, ("On side", "Top leg bent", "Head tilted back"), "Keeps the airway open.")


@design("MED/infections-and-antibiotics-1")
def _(d):
    signs = ["Fever", "Confusion", "Fast breathing", "Spreading redness"]
    d.rect(40, 50, 340, 220, fill=CREAM, rx=8)
    for i, s in enumerate(signs):
        y = 50 + i * 55
        if i:
            d.line(40, y, 380, y, width=2)
        d.text(s, 60, y + 35, size=17, weight=600, anchor="start")
        d.tick(340, y + 28, 16)
    d.arrow(392, 160, 470, 160)
    d.piece("warning", 475, 100, 140)
    d.text("More urgent", 545, 230, size=17, weight=600)
    caption(d, "Several signs together raise urgency.")


@design("MED/infections-and-antibiotics-2")
def _(d):
    cols = (120, 320, 520)
    for i, (cx, s) in enumerate(zip(cols, ("Wound\ninfection", "Fever and\nconfusion", "Emergency\ncall"))):
        d.piece(f"step-{i + 1}", cx - 50, 30, 100)
        d.text(s, cx, 150, size=17, weight=600)
        if i < 2:
            d.arrow(cx + 56, 67, cols[i + 1] - 56, 67)
    d.piece("warning", 265, 195, 110)
    d.piece("phone-call", 455, 190, 130)
    caption(d, "The sequence that can lead to sepsis.")


@design("MED/infections-and-antibiotics-3")
def _(d):
    d.piece("pills", 20, 70, 150)
    d.text("Prescribed dose", 95, 205, size=16, weight=600)
    axis(d, 140, x1=210, dots=(260, 350, 440, 530))
    d.text("Daily schedule", 350, 108, size=17, weight=600)
    d.line(530, 150, 530, 190, width=2)
    chip(d, 530, 215, 150, 52, "Finish full\ncourse", fill=YELLOW)
    caption(d, "Complete the course even when symptoms ease.")


@design("MED/infections-and-antibiotics-4")
def _(d):
    d.piece("pills", 10, 100, 190)
    d.piece("card", 215, 70, 240)
    for y, s in ((135, "Drug name"), (165, "Dose"), (195, "Start date")):
        d.leader(480, y - 6, 400, y - 6)
        d.text(s, 490, y, size=17, weight=600, anchor="start")
    caption(d, "The card links the course to its start date.")


@design("MED/infections-and-antibiotics-5")
def _(d):
    axis(d, 130, dots=(90, 205, 320, 435, 550))
    d.text("Dose times", 320, 90, size=17, weight=600)
    d.rect(60, 180, 520, 52, fill=CREAM, rx=8)
    for x in (90, 205, 320, 435):
        d.tick(x, 206, 16)
    d.cross(550, 206, 16)
    d.text("Tick per dose", 320, 275, size=17, weight=600)
    caption(d, "A gap shows a missed dose.")


@design("MED/medicine-stock-and-expiry-1")
def _(d):
    d.piece("shelf", 20, 60, 280)
    d.piece("pills", 335, 50, 160)
    d.leader(512, 96, 458, 108)
    d.text("Expiry date\non each pack", 516, 98, size=17, weight=600, anchor="start")
    d.cross(385, 250, 18)
    chip(d, 515, 250, 190, 50, "Expired: set aside")
    caption(d, "Dates are read on every item.")


@design("MED/medicine-stock-and-expiry-2")
def _(d):
    table(d, 40, 60, 560, ["Medicine", "Quantity", "Expiry date", "Storage location"], 3, rh=52, size=15)
    caption(d, "Each item is tracked by where it is kept.")


@design("MED/medicine-stock-and-expiry-3")
def _(d):
    for x, s in ((100, "Cool dark\ncupboard"), (320, "Fridge door"), (540, "Dry shelf away\nfrom bathroom")):
        d.piece("waypoint-pin", x - 75, 45, 150)
        d.text(s, x, 215, size=17, weight=600)
    caption(d, "Each medicine type has a place.")


@design("MED/medicine-stock-and-expiry-4")
def _(d):
    d.piece("shelf", 190, 40, 260)
    d.arrow(440, 245, 200, 245)
    d.text("Back to front", 320, 232, size=16, weight=600)
    chip(d, 130, 290, 170, 46, "Oldest at front")
    chip(d, 510, 290, 170, 46, "New at back")
    caption(d, "First in, first out.")


@design("MED/medicine-stock-and-expiry-5")
def _(d):
    d.piece("cabinet", 40, 60, 240)
    d.piece("table-header", 340, 70, 260)
    d.arrow(345, 150, 236, 150)
    d.text("Taped on door", 292, 136, size=16, weight=600)
    for x, y, s in ((404, 252, "Item"), (470, 282, "Quantity"), (536, 252, "Expiry date")):
        d.leader(x, y - 18, x, 224)
        d.text(s, x, y + 6, size=16, weight=600)
    caption(d, "The list sits where a helper looks first.")


@design("MED/medicine-stock-and-expiry-6")
def _(d):
    xs = (24, 180, 336, 492)
    for x, p, s in zip(xs, ("ice-pack", "bottle", "thermometer", "cool-box"), ("Ice packs", "Medicine\nbottle", "Thermometer", "Cool box")):
        d.piece(p, x, 80, 124)
        d.text(s, x + 62, 200, size=16, weight=600)
    d.text("+", 166, 140, size=28, weight=600)
    d.text("+", 322, 140, size=28, weight=600)
    d.arrow(466, 135, 490, 135, width=3)
    caption(d, "Keeps refrigerated stock cool when power fails.")


@design("MED/pandemic-household-plan-1")
def _(d):
    d.piece("hut", 40, 40, 150)
    d.text("Sick room", 115, 175, size=17, weight=600)
    d.piece("toilet", 450, 40, 140)
    d.text("Bathroom", 520, 175, size=17, weight=600)
    d.arrow(200, 100, 440, 100, width=5)
    d.text("Sick person's route", 320, 84, size=16, weight=600)
    d.piece("tray", 45, 195, 140)
    d.text("Tray at door", 115, 310, size=17, weight=600)
    d.piece("house", 460, 200, 120)
    d.text("Rest of house", 520, 310, size=17, weight=600)
    d.arrow(450, 250, 185, 250, dash="10 8")
    d.text("Others stay apart", 318, 238, size=16, weight=600)


@design("MED/pandemic-household-plan-2")
def _(d):
    n = 4
    w = 120
    gap = (640 - n * w) / (n + 1)
    for i in range(n):
        x = gap + i * (w + gap)
        d.piece("step-box", x, 100, w)
        d.badge(i + 1, x + w / 2, 80, 16)
        d.text(f"Action {i + 1}", x + w / 2, 225, size=16, weight=600)
        if i < n - 1:
            d.arrow(x + w + 4, 145, x + w + gap - 4, 145)
    caption(d, "One action each, in a fixed sequence.")


@design("MED/removing-a-tick-1")
def _(d):
    d.line(60, 250, 600, 250, width=4)
    d.text("Skin level", 600, 280, size=16, weight=600, anchor="end")
    chip(d, 300, 226, 130, 44, "Tweezers")
    d.arrow(300, 200, 300, 80, width=5)
    d.text("Pull straight up", 318, 125, size=17, weight=600, anchor="start")
    d.leader(208, 226, 236, 226)
    d.text("Grip at skin", 202, 232, size=17, weight=600, anchor="end")
    caption(d, "Grip sits at the skin surface, not the tick's body.")


@design("MED/removing-a-tick-2")
def _(d):
    d.line(60, 270, 600, 270, width=4)
    d.arrow(320, 262, 320, 70, width=5)
    d.leader(190, 244, 312, 262)
    d.text("Close to skin", 184, 244, size=17, weight=600, anchor="end")
    d.text("Straight up", 340, 170, size=17, weight=600, anchor="start")
    d.text("Steady pressure", 340, 100, size=17, weight=600, anchor="start")
    caption(d, "Angle and steadiness matter more than force.")


@design("MED/removing-a-tick-3")
def _(d):
    d.piece("person-kneeling", 30, 60, 240)
    d.arrow(300, 225, 300, 80, width=5)
    d.text("Lift straight", 320, 140, size=17, weight=600, anchor="start")
    d.leader(320, 275, 238, 210)
    d.text("Skin held taut", 328, 281, size=17, weight=600, anchor="start")
    caption(d, "The second hand keeps the skin still.")


@design("MED/removing-a-tick-4")
def _(d):
    d.piece("jar", 100, 60, 200)
    d.piece("note", 166, 138, 70)
    d.leader(340, 96, 246, 96)
    d.text("Sealed lid", 346, 102, size=17, weight=600, anchor="start")
    d.leader(340, 176, 238, 170)
    d.text("Bite date", 346, 182, size=17, weight=600, anchor="start")
    caption(d, "The tick is stored with the date of the bite.")


def dashed_ring(d, cx, cy, r):
    d.path(f"M{cx - r} {cy}a{r} {r} 0 1 0 {2 * r} 0a{r} {r} 0 1 0 {-2 * r} 0", dash="9 8", width=3)


@design("MED/removing-a-tick-5")
def _(d):
    cx, cy = 320, 175
    d.piece("bite-or-sting", cx - 50, cy - 38, 100)
    dashed_ring(d, cx, cy, 62)
    dashed_ring(d, cx, cy, 98)
    d.arrow(cx, cy + 36, cx, cy + 82, width=4)
    d.leader(170, cy, 274, cy)
    d.text("Bite site", 164, cy + 6, size=17, weight=600, anchor="end")
    d.leader(466, 96, cx + 69, cy - 69)
    d.text("Expanding ring", 472, 102, size=17, weight=600, anchor="start")
    caption(d, "The rash grows outward from the bite site.", 346)


@design("MED/respiratory-illness-at-home-1")
def _(d):
    d.piece("window", 30, 60, 130)
    d.text("Window", 95, 185, size=16, weight=600)
    d.piece("window", 480, 60, 130)
    d.text("Window", 545, 185, size=16, weight=600)
    d.arrow(170, 108, 470, 108, width=5)
    d.text("Fresh air crosses the room", 320, 90, size=17, weight=600)
    d.piece("hut", 245, 150, 150)
    d.text("Sick room", 320, 290, size=17, weight=600)
    caption(d, "Air moves across the room, not in at one point.")


@design("MED/respiratory-illness-at-home-2")
def _(d):
    d.piece("person-sitting", 50, 80, 200)
    d.text("Upright", 150, 255, size=17, weight=600)
    d.piece("cup", 400, 110, 150)
    d.text("Fluids", 475, 255, size=17, weight=600)
    chip(d, 350, 50, 150, 56, "Breaths\nper minute")
    d.leader(275, 60, 150, 148)
    caption(d, "Breath count is tracked alongside fluids.")


@design("MED/seizures-first-aid-1")
def _(d):
    recovery(d, ("Side-lying", "Top leg bent", "Head tilted slightly back"), "Used once the seizure has ended.")


@design("MED/seizures-first-aid-2")
def _(d):
    axis(d, 230, dots=(80, 300, 515))
    d.piece("phone-call", 440, 50, 150)
    d.line(515, 168, 515, 218, width=2)
    d.text("Onset", 80, 270, size=17, weight=600)
    d.text("2-3 min\nusual end", 300, 270, size=17, weight=600)
    d.text("5 min\ncall emergency", 515, 270, size=17, weight=600)
    caption(d, "Shows when to move from watching to calling.")


@design("MED/skin-infections-and-boils-2")
def _(d):
    decision_flow(d, "Boil: how far?", "Stays local", "Warm compresses", "Spreading redness\nor fever", "Professional care")


@design("MED/snakebite-1")
def _(d):
    d.piece("heart", 20, 60, 80)
    d.line(100, 90, 420, 90, dash="10 8", width=3)
    d.text("Heart level", 420, 75, size=16, weight=600, anchor="end")
    d.arrow(250, 96, 250, 170, width=4)
    d.text("Below heart", 264, 140, size=17, weight=600, anchor="start")
    d.piece("limb-outline", 90, 140, 240)
    d.piece("do-not", 440, 110, 70)
    d.text("No cutting", 520, 142, size=17, weight=600, anchor="start")
    d.piece("do-not", 440, 200, 70)
    d.text("No tourniquet", 520, 232, size=17, weight=600, anchor="start")


@design("MED/snakebite-2")
def _(d):
    d.piece("person-carrying", 70, 80, 220)
    d.leader(330, 130, 248, 160)
    d.text("Heart level", 336, 136, size=17, weight=600, anchor="start")
    d.piece("direction-of-travel", 400, 190, 150)
    d.text("Kept still", 475, 300, size=17, weight=600)
    caption(d, "The limb is level, not raised.")


@design("MED/snakebite-3")
def _(d):
    table(d, 30, 60, 580, ["Time", "Swelling", "Pain", "Breathing", "Dizziness"], 4, rh=46, size=15)
    caption(d, "Each check is logged to track change.")


@design("MED/snakebite-4")
def _(d):
    d.piece("bite-or-sting", 40, 70, 260)
    d.leader(340, 118, 217, 160)
    d.text("Swelling edge", 346, 126, size=17, weight=600, anchor="start")
    d.piece("timeline-marker", 380, 190, 130)
    d.text("Time", 445, 304, size=17, weight=600)
    caption(d, "Spread is tracked by marking the edge at set times.", 346)


@design("MED/spinal-injury-keeping-still-1")
def _(d):
    d.piece("person-lying", 200, 60, 340)
    d.piece("person-kneeling", 60, 149, 190)
    d.arrow(270, 205, 570, 205, width=4)
    d.text("Head", 280, 182, size=17, weight=600)
    d.text("Neck", 345, 182, size=17, weight=600)
    d.text("Body in line", 470, 182, size=17, weight=600)
    caption(d, "The body is moved as one unit.")


@design("MED/spinal-injury-keeping-still-2")
def _(d):
    d.piece("arrow-curved", 230, 50, 180)
    d.text("Log-roll", 320, 50, size=17, weight=600)
    d.piece("person-lying", 170, 95, 300)
    caption(d, "The body turns together, not piece by piece.")


@design("MED/sprains-and-strains-1")
def _(d):
    xs = (95, 245, 395, 545)
    for i, (x, s) in enumerate(zip(xs, ("Rest", "Ice", "Compression", "Elevation"))):
        d.badge(i + 1, x, 110, 22)
        chip(d, x, 190, 112, 56, s)
        if i < 3:
            d.text("+", x + 75, 200, size=28, weight=600)
    caption(d, "The four steps are applied together.")


@design("MED/sprains-and-strains-2")
def _(d):
    d.piece("bandage-roll", 20, 110, 130)
    d.arrow(160, 160, 240, 160)
    d.piece("limb-outline", 290, 50, 300)
    for x in (350, 364, 378):
        d.line(x, 138, x + 14, 192, width=3)
    d.leader(365, 250, 365, 190)
    d.text("Overlap", 365, 275, size=17, weight=600)
    d.leader(500, 250, 464, 190)
    d.text("Ankle", 500, 275, size=17, weight=600)
    d.piece("arrow-curved", 330, 30, 120)
    caption(d, "Each turn overlaps the one before.")


@design("MED/sprains-and-strains-3")
def _(d):
    d.piece("ice-cube", 20, 90, 130)
    d.text("Ice pack", 85, 225, size=16, weight=600)
    d.arrow(155, 145, 195, 145)
    d.piece("cloth", 200, 90, 130)
    d.text("Cloth", 265, 225, size=16, weight=600)
    d.arrow(335, 145, 375, 145)
    chip(d, 430, 145, 90, 48, "Skin")
    d.line(485, 100, 485, 230, dash="4 8", width=2)
    d.piece("timeline-marker", 500, 90, 120)
    d.text("15 to 20\nminutes", 560, 225, size=16, weight=600)
    caption(d, "The cloth stays between ice and skin.")


@design("MED/sprains-and-strains-4")
def _(d):
    d.piece("heart", 20, 45, 80)
    d.line(100, 80, 600, 80, dash="10 8", width=3)
    d.text("Heart level", 600, 66, size=16, weight=600, anchor="end")
    d.piece("pillow", 190, 140, 220)
    d.piece("footprints", 225, 95, 140)
    d.line(40, 290, 600, 290, width=4)
    d.leader(450, 162, 346, 160)
    d.text("Heel supported", 456, 166, size=17, weight=600, anchor="start")
    d.leader(450, 232, 398, 232)
    d.text("Pillow", 456, 238, size=17, weight=600, anchor="start")
    caption(d, "Elevation is measured at the ankle.")


@design("MED/sprains-and-strains-5")
def _(d):
    d.piece("bandage-roll", 20, 120, 120)
    d.piece("limb-outline", 150, 60, 280)
    d.leader(280, 250, 270, 170)
    d.text("Ankle", 280, 275, size=17, weight=600)
    d.leader(400, 250, 400, 160)
    d.text("Foot", 400, 275, size=17, weight=600)
    d.piece("arrow-loop", 470, 100, 140)
    d.text("Crossover", 540, 250, size=17, weight=600)
    caption(d, "Each turn crosses itself at the ankle.")


@design("MED/sprains-and-strains-6")
def _(d):
    xs = (90, 240, 390, 540)
    axis(d, 170, dots=xs)
    for x, s in zip(xs, ("Rest", "Gentle\nmovement", "Gradual\nloading", "Full\nactivity")):
        d.text(s, x, 105 if "\n" in s else 125, size=17, weight=600)
    d.curve_arrow("M540 190C470 300 160 300 90 190", (90, 190), -2.0)
    d.text("If pain recurs", 315, 300, size=16, weight=600)
    caption(d, "One to two weeks.", 346)


@design("MED/stroke-recognition-1")
def _(d):
    d.piece("person-standing", 60, 60, 220)
    d.leader(330, 90, 194, 90)
    d.text("Face", 336, 96, size=17, weight=600, anchor="start")
    d.leader(330, 150, 202, 150)
    d.text("Arm", 336, 156, size=17, weight=600, anchor="start")
    d.piece("mouth", 450, 185, 100)
    d.text("Speech", 336, 236, size=17, weight=600, anchor="start")
    caption(d, "The checks look for one-sided change.")


@design("MED/stroke-recognition-2")
def _(d):
    d.rect(95, 135, 475, 135, fill=YELLOW, stroke=YELLOW, rx=10)
    axis(d, 200, x1=60, dots=(130, 220))
    d.piece("phone-call", 155, 20, 130)
    d.line(220, 118, 220, 190, width=2)
    d.text("Onset", 130, 245, size=17, weight=600)
    d.text("Call for help", 220, 245, size=17, weight=600, anchor="start")
    d.text("Treatment window", 430, 175, size=17, weight=600)
    caption(d, "The call must come early, inside the window.")


@design("MED/temporary-dental-care-1")
def _(d):
    d.piece("tooth", 70, 70, 220)
    d.leader(40, 100, 140, 125)
    d.text("Sharp edge", 40, 90, size=17, weight=600, anchor="start")
    d.piece("wax", 400, 90, 140)
    d.leader(422, 160, 232, 150)
    d.text("Wax pad", 470, 240, size=17, weight=600)
    caption(d, "The wax covers the edge that would cut the tongue.")


@design("MED/temporary-dental-care-2")
def _(d):
    decision_flow(d, "Toothache", "No swelling", "Pain relief\nand cover", "Swelling\nor fever", "Urgent care")
