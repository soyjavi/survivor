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


def P(d, name, cx, cy, w):
    d.piece(name, cx - w / 2, cy - w * 0.375, w)


def L(d, s, x, y, size=16, anchor="middle"):
    d.text(s, x, y, size=size, weight=600, anchor=anchor)


def flow(d, items, y, w=130, arrow=True, label_dy=26):
    n = len(items)
    gap = (640 - n * w) / (n + 1)
    for i, (piece, label) in enumerate(items):
        x = gap + i * (w + gap)
        d.piece(piece, x, y, w)
        d.text(label, x + w / 2, y + w * 0.75 + label_dy, size=16, weight=600)
        if arrow and i < n - 1:
            d.arrow(x + w + 4, y + w * 0.375, x + w + gap - 4, y + w * 0.375)


@design("SEC/de-escalation-1")
def _(d):
    P(d, "person-standing", 160, 180, 170)
    P(d, "person-standing", 480, 180, 170)
    d.arrow(240, 150, 400, 150, width=3)
    d.arrow(400, 150, 240, 150, width=3)
    d.line(320, 100, 320, 220, dash="9 7", width=3)
    L(d, "arm's length", 320, 90)
    caption(d, "Angled and spaced, not square face-on.")


@design("SEC/de-escalation-2")
def _(d):
    d.line(320, 40, 320, 300, dash="9 7", width=3)
    P(d, "person-standing", 90, 160, 150)
    d.arrow(150, 150, 210, 150, width=3)
    chip(d, 255, 150, 80, 36, "Threat")
    L(d, "Narrow focus", 160, 270)
    P(d, "person-standing", 400, 160, 150)
    P(d, "arrow-branch", 495, 150, 80)
    P(d, "start-or-end", 580, 120, 60)
    P(d, "start-or-end", 580, 185, 60)
    L(d, "Wide view", 470, 270)
    caption(d, "Fear shrinks what a person sees and hears.")


@design("SEC/de-escalation-3")
def _(d):
    P(d, "person-sitting", 110, 190, 160)
    P(d, "person-sitting", 530, 190, 160)
    P(d, "table-grid", 320, 210, 150)
    d.leader(120, 90, 110, 140)
    L(d, "Eye level", 120, 80)
    d.leader(520, 90, 530, 140)
    L(d, "Hands visible", 520, 80)
    caption(d, "Sit level, not standing over the other person.")


@design("SEC/de-escalation-4")
def _(d):
    ys = [290, 232, 174, 116, 58]
    labels = ["Calm talk", "Clenched fists", "Raised voice", "Shrinking space", "Walking away"]
    for y, s in zip(ys, labels):
        chip(d, 380, y, 190, 34, s)
    for i, (a, b) in enumerate(zip(ys[:-1], ys[1:])):
        if i != 2:
            d.arrow(380, a - 19, 380, b + 19, width=3)
    d.line(270, 145, 490, 145, dash="9 7", width=3, color=RED)
    L(d, "Warning signs", 500, 151, anchor="start")
    d.curve_arrow("M 285 116 C 200 116 200 232 285 232", (285, 232), 0, color=BLUE, width=4)
    L(d, "Step back", 185, 180, anchor="end")
    caption(d, "Step back at the warning signs, before the top.", 342)


@design("SEC/de-escalation-5")
def _(d):
    P(d, "person-standing", 160, 180, 170)
    P(d, "person-standing", 480, 180, 170)
    P(d, "open-hand", 320, 105, 100)
    L(d, "Slow offer", 320, 160)
    d.line(240, 215, 400, 215, dash="9 7", width=3)
    L(d, "arm's length", 320, 245)
    caption(d, "The offered hand moves slowly and visibly.")


@design("SEC/de-escalation-6")
def _(d):
    P(d, "crowd", 140, 170, 190)
    L(d, "Crowd", 140, 255)
    P(d, "person-standing", 470, 150, 110)
    P(d, "person-standing", 570, 150, 110)
    d.curve_arrow("M 230 120 C 280 50 380 50 410 100", (410, 100), 0.9, color=BLUE, width=4)
    d.line(330, 160, 330, 300, dash="9 7", width=3)
    L(d, "Quieter corner", 520, 240)
    caption(d, "Stepping away lowers the temperature.")


@design("SEC/dealing-with-strangers-1")
def _(d):
    P(d, "person-standing", 100, 180, 150)
    P(d, "door", 320, 150, 170)
    P(d, "chain", 320, 150, 50)
    P(d, "person-standing", 540, 180, 150)
    d.arrow(210, 255, 430, 255, width=3)
    d.arrow(430, 255, 210, 255, width=3)
    L(d, "Questions pass", 320, 285)
    L(d, "Inside", 100, 255)
    L(d, "Visitor", 540, 255)
    caption(d, "Questions pass through the gap; the door stays locked.")


@design("SEC/dealing-with-strangers-2")
def _(d):
    P(d, "door", 180, 170, 190)
    P(d, "chain", 290, 150, 70)
    L(d, "Chain", 290, 200)
    P(d, "person-standing", 520, 170, 160)
    L(d, "Visitor", 520, 250)
    d.arrow(350, 150, 440, 150, width=3)
    caption(d, "The door opens only as far as the chain allows.")


@design("SEC/dealing-with-strangers-3")
def _(d):
    P(d, "person-standing", 100, 200, 150)
    P(d, "person-standing", 540, 200, 150)
    P(d, "table-grid", 320, 220, 190)
    P(d, "jerrycan", 320, 140, 90)
    P(d, "person-standing", 520, 60, 110)
    L(d, "Water", 200, 120, anchor="end")
    d.leader(208, 114, 292, 140)
    L(d, "Second household member", 480, 100, size=15, anchor="end")
    L(d, "Table", 320, 300)
    caption(d, "The exchange happens in view of others.")




@design("SEC/dealing-with-strangers-4")
def _(d):
    P(d, "door", 70, 170, 110)
    P(d, "person-standing", 175, 170, 140)
    P(d, "person-sitting", 345, 170, 140)
    P(d, "phone-call", 530, 170, 130)
    d.curve_arrow("M 175 95 C 260 30 440 30 520 95", (520, 95), 1.0, width=4)
    L(d, "Speaks", 175, 250)
    L(d, "Hidden child", 345, 250)
    L(d, "Calls", 530, 250)
    caption(d, "Each role has a fixed position.")


@design("SEC/earthquake-safety-1")
def _(d):
    d.line(320, 40, 320, 300, dash="9 7", width=3)
    P(d, "table-grid", 150, 100, 150)
    P(d, "person-kneeling", 150, 205, 130)
    d.tick(250, 90, 20)
    L(d, "Under sturdy table", 160, 285)
    P(d, "window", 410, 110, 130)
    P(d, "shelf", 550, 110, 130)
    d.cross(410, 190, 18)
    d.cross(550, 190, 18)
    L(d, "Windows", 410, 225)
    L(d, "Shelves", 550, 225)
    caption(d, "Drop and hold in safe spots, away from unsafe ones.")


@design("SEC/earthquake-safety-2")
def _(d):
    P(d, "wall", 80, 190, 130)
    P(d, "bed", 230, 220, 170)
    P(d, "person-kneeling", 230, 105, 120)
    P(d, "shelf", 540, 190, 150)
    P(d, "warning", 540, 90, 60)
    d.line(300, 140, 480, 170, dash="3 9", width=4)
    d.arrow(190, 105, 120, 130, width=3)
    L(d, "Toward wall", 150, 70)
    L(d, "Shelf", 540, 280)
    caption(d, "Staying put beats reaching for furniture.")


@design("SEC/earthquake-safety-3")
def _(d):
    flow(d, [("step-1", "Injury"), ("step-2", "Gas"), ("step-3", "Damage"), ("step-box", "Aftershock")], 90, w=110)
    caption(d, "The order of checks.", 300)


@design("SEC/earthquake-safety-4")
def _(d):
    P(d, "wall", 130, 170, 200)
    P(d, "shelf", 340, 140, 170)
    P(d, "tin", 340, 235, 70)
    d.leader(130, 280, 135, 215)
    L(d, "Fixed to wall", 130, 300)
    d.leader(520, 192, 378, 240)
    L(d, "Heavy tin low", 530, 190, anchor="start")
    caption(d, "The fixings go in the wall.")


@design("SEC/earthquake-safety-5")
def _(d):
    P(d, "person-kneeling", 110, 130, 140)
    P(d, "table-grid", 270, 130, 140)
    P(d, "timeline-marker", 480, 120, 140)
    L(d, "Timer", 480, 190)
    for i, s in enumerate(["Drop", "Cover", "Hold"]):
        chip(d, 140 + i * 180, 265, 120, 40, s)
        if i < 2:
            d.arrow(206 + i * 180, 265, 254 + i * 180, 265, width=3)
    caption(d, "The position used in the drill.")


@design("SEC/evacuating-a-building-quickly-1")
def _(d):
    P(d, "room", 160, 180, 190)
    P(d, "start-or-end", 490, 90, 90)
    P(d, "start-or-end", 490, 250, 90)
    d.arrow(260, 150, 440, 95, width=4)
    d.arrow(260, 210, 440, 250, width=4, dash="10 8")
    L(d, "Exit 1", 580, 95)
    L(d, "Exit 2", 580, 255)
    L(d, "Primary", 330, 105)
    L(d, "Second", 330, 280)
    caption(d, "Every room has two ways out.")


@design("SEC/evacuating-a-building-quickly-2")
def _(d):
    P(d, "bicycle", 120, 190, 150)
    P(d, "do-not", 120, 105, 60)
    L(d, "Bicycle", 120, 270)
    d.arrow(210, 190, 410, 190, width=4)
    P(d, "tip", 310, 110, 60)
    L(d, "Clear landing", 310, 245)
    P(d, "door", 520, 180, 150)
    L(d, "Exit door", 520, 260)
    caption(d, "Clear obstacles before drills.")


@design("SEC/evacuating-a-building-quickly-3")
def _(d):
    flow(d, [("person-kneeling", "Crouch low"), ("hand", "Hand on wall"), ("door", "Feel the door")], 100, w=140)
    for i in range(3):
        d.badge(i + 1, 70 + i * 205, 85)
    caption(d, "Air is cleaner near the floor.", 300)


@design("SEC/evacuating-a-building-quickly-4")
def _(d):
    flow(d, [("door", "Touch door"), ("warning", "Hot door"), ("arrow-branch", "Another exit")], 100, w=140)
    for i in range(3):
        d.badge(i + 1, 70 + i * 205, 85)
    caption(d, "Check before opening.", 300)


@design("SEC/evacuating-a-building-quickly-5")
def _(d):
    P(d, "waypoint-pin", 80, 170, 110)
    L(d, "Meeting point", 80, 250, size=15)
    for x in (200, 280, 360):
        P(d, "person-standing", x, 175, 90)
    P(d, "person-standing", 450, 175, 90)
    P(d, "table-grid", 560, 175, 90)
    L(d, "Checklist", 560, 235)
    P(d, "tip", 330, 70, 60)
    L(d, "Answer aloud", 375, 78, anchor="start")
    caption(d, "The head count comes before anyone goes back.")


@design("SEC/local-hazard-map-4")
def _(d):
    d.rect(70, 20, 500, 305, rx=14)
    L(d, "Symbol", 130, 52)
    L(d, "Hazard", 250, 52, anchor="start")
    L(d, "Note", 500, 52)
    d.line(70, 68, 570, 68, width=2, color=SAND)
    rows = [("river", "Flood"), ("slope", "Slope"), ("tree", "Woodland"), ("caution", "Industrial site"), ("waypoint-pin", "Safe place")]
    for i, (p, s) in enumerate(rows):
        y = 100 + i * 50
        P(d, p, 130, y, 64)
        L(d, s, 250, y + 6, anchor="start")
        P(d, "note", 500, y, 46)
        if i:
            d.line(84, y - 25, 556, y - 25, width=2, color=SAND)


@design("SEC/local-hazard-map-5")
def _(d):
    flow(d, [("footprints", "Route"), ("caution", "Narrow point"), ("waypoint-pin", "Flooded dip"), ("arrow-branch", "Second route")], 100, w=110)
    caption(d, "Which stretches need a note, and where the second route begins.", 300)


@design("SEC/neighbourhood-watch-1")
def _(d):
    P(d, "map", 320, 190, 330)
    for x, y in [(215, 165), (430, 165), (225, 245), (425, 250)]:
        P(d, "waypoint-pin", x, y, 52)
    P(d, "waypoint-pin", 320, 210, 66)
    L(d, "Meeting point", 320, 40)
    d.leader(320, 48, 320, 208)
    L(d, "Households", 90, 100)
    d.leader(110, 108, 210, 182)
    caption(d, "Every block has a named contact.")


@design("SEC/neighbourhood-watch-2")
def _(d):
    P(d, "table-grid", 320, 170, 130)
    L(d, "Shared list", 320, 245)
    spots = [(135, 70, "Check on elders"), (505, 70, "Medical needs"), (135, 280, "Supplies record"), (505, 280, "Contact list")]
    for x, y, s in spots:
        chip(d, x, y, 190, 44, s)
    d.arrow(215, 98, 270, 135, width=3)
    d.arrow(425, 98, 370, 135, width=3)
    d.arrow(215, 252, 270, 215, width=3)
    d.arrow(425, 252, 370, 215, width=3)
    caption(d, "Every role feeds one shared list.", 342)


@design("SEC/neighbourhood-watch-3")
def _(d):
    for y, n in [(90, "Pair 1"), (225, "Pair 2")]:
        P(d, "person-standing", 80, y, 90)
        P(d, "person-standing", 160, y, 90)
        d.arrow(220, y, 380, y, width=3)
        L(d, n, 120, y + 55)
    P(d, "timeline-axis", 520, 160, 190)
    P(d, "timeline-marker", 520, 118, 70)
    L(d, "Patrol times", 520, 225)
    caption(d, "Visible, predictable, no one alone.")


@design("SEC/neighbourhood-watch-4")
def _(d):
    P(d, "table-grid", 190, 85, 120)
    L(d, "Contact list", 190, 150)
    P(d, "timeline-marker", 450, 85, 110)
    L(d, "Timer", 450, 150)
    for x in (70, 150, 230):
        P(d, "person-standing", x, 245, 80)
    d.arrow(290, 245, 450, 245, width=3)
    P(d, "waypoint-pin", 540, 245, 90)
    L(d, "Meeting point", 540, 315)
    caption(d, "The drill times how long it takes to reach everyone.", 342)


@design("SEC/non-violent-defensive-posture-1")
def _(d):
    d.rect(30, 16, 580, 316, fill=CREAM)
    L(d, "Distance", 320, 44)
    d.rect(90, 58, 460, 252, fill=PAPER)
    L(d, "Routine", 320, 86)
    d.rect(150, 100, 340, 190, fill=CREAM)
    L(d, "Awareness", 320, 128)
    P(d, "survivor-mark", 320, 200, 150)


@design("SEC/non-violent-defensive-posture-2")
def _(d):
    P(d, "person-standing", 80, 160, 140)
    for i, (n, s) in enumerate([("step-1", "Exits"), ("step-2", "People"), ("step-3", "Objects")]):
        x = 250 + i * 150
        P(d, n, x, 150, 100)
        L(d, s, x, 215)
        if i < 2:
            d.arrow(x + 50, 150, x + 100, 150, width=3)
    d.line(40, 280, 600, 280, dash="9 7", width=3)
    L(d, "Safe distance", 320, 310)


@design("SEC/non-violent-defensive-posture-3")
def _(d):
    chip(d, 90, 175, 110, 44, "Start")
    d.line(150, 175, 255, 175, width=4)
    P(d, "arrow-branch", 320, 175, 130)
    d.line(385, 150, 480, 92, width=4)
    d.line(385, 200, 480, 258, width=4, dash="2 10")
    chip(d, 550, 90, 130, 44, "Route A: lit")
    chip(d, 550, 260, 130, 44, "Route B: dark")
    P(d, "caution", 420, 250, 46)
    caption(d, "Vary the route; avoid empty stretches.")


@design("SEC/non-violent-defensive-posture-4")
def _(d):
    P(d, "person-standing", 140, 180, 150)
    P(d, "person-standing", 500, 180, 150)
    d.curve_arrow("M 100 105 C 130 45 220 45 250 105", (250, 105), 1.1, color=BLUE, width=4)
    L(d, "Step back", 175, 40)
    d.arrow(230, 235, 410, 235, width=3)
    d.arrow(410, 235, 230, 235, width=3)
    d.line(320, 215, 320, 255, dash="9 7", width=3)
    L(d, "Distance, no contact", 320, 280)


@design("SEC/keeping-a-low-profile-1")
def _(d):
    P(d, "footprints", 75, 175, 110)
    L(d, "Path", 75, 225)
    P(d, "bucket", 320, 90, 100)
    L(d, "Water container", 320, 145, size=15)
    P(d, "flashlight", 320, 255, 100)
    L(d, "Lamp", 320, 300)
    d.line(140, 160, 265, 100, dash="9 7", width=3, color=BLUE)
    d.line(140, 190, 265, 250, dash="9 7", width=3, color=BLUE)
    P(d, "tent", 490, 190, 150)
    P(d, "tree", 585, 80, 90)
    L(d, "Shaded corner", 565, 140, size=15)


@design("SEC/local-hazard-map-1")
def _(d):
    d.rect(110, 20, 420, 300, rx=14)
    rows = [("river", "Flood low ground"), ("slope", "Slopes"), ("shrub", "Dry woodland"), ("caution", "Industrial sites"), ("waypoint-pin", "Safe places")]
    for i, (p, s) in enumerate(rows):
        y = 52 + i * 58
        P(d, p, 190, y, 80)
        L(d, s, 260, y + 6, size=17, anchor="start")
        if i:
            d.line(124, y - 29, 516, y - 29, width=2, color=SAND)


@design("SEC/local-hazard-map-2")
def _(d):
    P(d, "river", 85, 160, 130)
    P(d, "waypoint-pin", 230, 160, 90)
    P(d, "slope", 380, 160, 130)
    P(d, "tree", 540, 160, 130)
    L(d, "River", 85, 240)
    L(d, "Home", 230, 240)
    L(d, "Slope", 380, 240)
    L(d, "Woodland", 540, 240)
    caption(d, "Zones are judged one by one, not as general danger.")


@design("SEC/local-hazard-map-3")
def _(d):
    P(d, "river", 110, 85, 140)
    L(d, "Low ground", 110, 150)
    P(d, "slope", 530, 85, 140)
    L(d, "Slope", 530, 150)
    P(d, "tree", 320, 55, 100)
    L(d, "Woodland", 385, 70, anchor="start")
    P(d, "waypoint-pin", 320, 175, 90)
    d.arrow(285, 200, 170, 285, width=4)
    d.arrow(355, 200, 470, 285, width=4)
    L(d, "Route 1", 120, 315)
    L(d, "Route 2", 520, 315)


@design("SEC/personal-documents-and-identity-1")
def _(d):
    cols = [("Identity", 215), ("Property", 320), ("Medical", 425), ("Finance", 530)]
    d.rect(160, 60, 450, 220, rx=12)
    d.line(160, 170, 610, 170, width=2, color=SAND)
    for s, x in cols:
        chip(d, x, 36, 96, 32, s, size=16)
        d.line(x, 60, x, 280, width=2, color=SAND)
        d.line(x - 30, 115, x + 30, 115, width=4)
        d.line(x - 30, 225, x + 30, 225, width=4, dash="8 6")
    L(d, "Original", 150, 121, anchor="end")
    L(d, "Photocopy", 150, 231, anchor="end")
    caption(d, "Copies stay beside originals, so one folder is grabbed.", 320)


@design("SEC/personal-safety-at-night-1")
def _(d):
    flow(d, [("door", "Lock doors\nand windows"), ("flashlight", "Torch by bed"), ("whistle", "Household\nsignal")], 100, w=140)
    for i in range(3):
        d.badge(i + 1, 70 + i * 205, 85)
    caption(d, "The bedtime order.", 300)


@design("SEC/personal-safety-at-night-2")
def _(d):
    P(d, "bed", 100, 175, 150)
    P(d, "flashlight", 235, 100, 80)
    L(d, "Torch", 235, 145)
    P(d, "phone-call", 235, 235, 70)
    L(d, "Phone", 235, 285)
    d.arrow(300, 175, 440, 175, width=3, dash="10 8")
    P(d, "door", 535, 175, 140)
    L(d, "Way out", 535, 245)
    caption(d, "The path from bed to door can be walked in the dark.")


@design("SEC/personal-safety-at-night-3")
def _(d):
    P(d, "person-standing", 80, 170, 120)
    d.line(150, 215, 290, 215, width=4)
    d.line(290, 215, 430, 215, width=4, dash="2 10")
    L(d, "Lit", 220, 195)
    L(d, "Dark", 360, 195)
    P(d, "flashlight", 540, 90, 90)
    P(d, "footprints", 540, 190, 100)
    L(d, "Next step", 540, 250)
    caption(d, "Light only to see the next step.")


@design("SEC/personal-safety-at-night-4")
def _(d):
    d.line(60, 115, 580, 115, width=5)
    L(d, "Hand on wall", 320, 100)
    P(d, "child-standing", 130, 195, 130)
    P(d, "person-standing", 510, 195, 140)
    d.arrow(210, 215, 420, 215, width=3)
    L(d, "Child at back", 130, 275)
    L(d, "Adult at front", 510, 275)
    caption(d, "Wall contact keeps the line together.")


@design("SEC/protecting-food-and-water-from-theft-1")
def _(d):
    P(d, "latch", 70, 160, 90)
    L(d, "Latched inside", 70, 215, size=15)
    P(d, "jerrycan", 200, 160, 110)
    L(d, "Heavy low", 200, 225)
    P(d, "barrel", 350, 160, 120)
    L(d, "Lidded drum", 350, 225)
    P(d, "tin", 500, 160, 100)
    L(d, "Tins at back", 500, 225)
    d.arrow(150, 285, 580, 285, width=3)
    L(d, "Toward back wall", 365, 315)


@design("SEC/protecting-property-and-avoiding-looting-1")
def _(d):
    P(d, "house", 320, 105, 190)
    P(d, "flashlight", 130, 130, 90)
    L(d, "Entrance light", 130, 185, size=15)
    P(d, "footprints", 320, 245, 110)
    L(d, "Tidy path", 320, 305)
    P(d, "jerrycan", 530, 220, 90)
    P(d, "lock", 575, 185, 40)
    L(d, "Locked", 530, 280)
    caption(d, "These signs make the house look occupied.", 342)


@design("SEC/protecting-property-and-avoiding-looting-2")
def _(d):
    d.line(320, 30, 320, 290, dash="9 7", width=3)
    P(d, "flashlight", 90, 150, 100)
    P(d, "footprints", 215, 160, 100)
    P(d, "do", 150, 65, 55)
    L(d, "Tidy", 150, 240)
    P(d, "bag", 420, 160, 100)
    P(d, "crate", 540, 160, 100)
    P(d, "do-not", 420, 65, 55)
    P(d, "caution", 540, 65, 55)
    L(d, "Cluttered", 480, 240)
    caption(d, "Clutter signals an empty house.")


@design("SEC/protecting-property-and-avoiding-looting-3")
def _(d):
    P(d, "bag", 120, 175, 120)
    P(d, "caution", 120, 90, 50)
    L(d, "Abandoned goods", 120, 245, size=15)
    P(d, "hand", 300, 175, 90)
    d.curve_arrow("M 215 110 C 250 60 330 60 365 110", (365, 110), 1.0, width=4)
    L(d, "Leave them", 300, 245)
    d.arrow(360, 190, 450, 190, width=3)
    P(d, "phone-call", 540, 175, 110)
    L(d, "Report", 540, 245)


@design("SEC/protecting-property-and-avoiding-looting-4")
def _(d):
    P(d, "house", 110, 170, 150)
    P(d, "house", 530, 170, 150)
    d.line(320, 100, 320, 240, width=5)
    d.arrow(190, 135, 450, 135, width=3)
    d.arrow(450, 135, 190, 135, width=3)
    L(d, "Agreed signal", 320, 80)
    P(d, "flashlight", 215, 225, 70)
    L(d, "Porch light", 215, 275, size=15)
    caption(d, "Simple, visible, agreed in advance.")
