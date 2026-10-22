from dg import *

DESIGNS = {}

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


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


def grid(d, x, y, cw, ch, cols, rows, header_h=None, fills=None):
    hh = header_h or ch
    W = cw * cols
    H = hh + ch * rows
    d.rect(x, y, W, H, fill=CREAM, rx=6)
    d.rect(x, y, W, hh, fill=SAND, rx=6)
    for c in range(1, cols):
        d.line(x + c * cw, y, x + c * cw, y + H, width=2)
    for r in range(rows):
        d.line(x, y + hh + r * ch, x + W, y + hh + r * ch, width=2)


def row_chips(d, labels, widths, y, h, gap, x0=16, size=16, arrows=True):
    x = x0
    centers = []
    for lab, w in zip(labels, widths):
        chip(d, x + w / 2, y, w, h, lab, size=size)
        centers.append((x, x + w))
        x += w + gap
    if arrows:
        for i in range(len(labels) - 1):
            d.arrow(centers[i][1] + 3, y, centers[i + 1][0] - 3, y, width=3)


@design("PSY/boredom-and-idle-time-1")
def _(d):
    x, y, cw = 140, 40, 62
    grid(d, x, y, cw, 48, 7, 4, header_h=34)
    for i, s in enumerate(DAYS):
        d.text(s, x + cw * i + cw / 2, y + 23, size=15, weight=600)
    for i, s in enumerate(["Games", "Stories", "Skills", "Shared"]):
        d.text(s, x - 12, y + 34 + 48 * i + 30, size=16, weight=600, anchor="end")
    d.rect(x, y + 34 + 48 * 3, cw * 7, 48, fill=YELLOW, rx=6)
    d.text("Same group activity", x + cw * 3.5, y + 34 + 48 * 3 + 30, size=16, weight=600)
    d.curve_arrow("M 590 80 C 636 100 636 190 596 214", (596, 214), 2.6, width=3)
    d.text("Rotate weekly", 320, 296, size=16, weight=600)
    caption(d, "Non-shared rows rotate so no game goes stale.")


@design("PSY/boredom-and-idle-time-2")
def _(d):
    x, y, cw = 160, 50, 64
    grid(d, x, y, cw, 52, 7, 3, header_h=34)
    for i, s in enumerate(DAYS):
        d.text(s, x + cw * i + cw / 2, y + 23, size=15, weight=600)
    d.rect(x, y + 34, cw * 7, 52, fill=YELLOW, rx=6)
    for i in range(7):
        d.tick(x + cw * i + cw / 2, y + 60, 12)
    for r, row in enumerate(["ABCDEFG", "CDEFGAB"]):
        for i, ch in enumerate(row):
            d.text(ch, x + cw * i + cw / 2, y + 34 + 52 * (r + 1) + 32, size=17, weight=600)
    d.text("Shared\nactivity", x - 14, y + 56, size=16, weight=600, anchor="end")
    d.path(f"M {x - 8} {y + 34 + 56} L {x - 18} {y + 34 + 56} L {x - 18} {y + 34 + 52 * 3 - 4} L {x - 8} {y + 34 + 52 * 3 - 4}", width=3)
    d.text("Rotating\nrows", x - 28, y + 34 + 52 * 2 - 4, size=16, weight=600, anchor="end")
    caption(d, "The same group activity repeats daily while other rows change.")


@design("PSY/boredom-and-idle-time-3")
def _(d):
    d.piece("threshold", 10, 120, 200)
    d.text("Doorway", 110, 296, size=16, weight=600)
    d.line(220, 215, 520, 215, dash="10 8", width=4)
    d.arrow(500, 215, 610, 215, width=4)
    d.text("Foot traffic", 400, 244, size=16, weight=600)
    d.piece("waypoint-pin", 230, 20, 140)
    d.text("Quiet corner", 300, 150, size=16, weight=600)
    caption(d, "The corner sits off the route.")


@design("PSY/boredom-and-idle-time-4")
def _(d):
    d.rect(16, 60, 230, 230, fill=PAPER, rx=14, dash="10 8")
    d.piece("person-sitting", 46, 100, 170)
    d.text("Play area", 131, 272, size=16, weight=600)
    for p, lab, x, y in [("flame", "Fire", 290, 50), ("jerrycan", "Fuel", 460, 50), ("knife", "Sharp tools", 290, 190), ("hut", "Storage", 460, 190)]:
        d.piece(p, x, y, 130)
        d.text(lab, x + 65, y + 98 + 22, size=16, weight=600)
    caption(d, "Play sits at a distance, not just supervised.")


@design("PSY/caring-for-babies-without-supplies-1")
def _(d):
    d.piece("cloth", 10, 70, 250)
    for i, s in enumerate(["Fold", "Fasten", "Cover"]):
        y = 76 + i * 80
        d.badge(i + 1, 300, y, 20)
        chip(d, 440, y, 200, 52, s)
    caption(d, "The folds keep the cloth fastened and the bottom covered.")


@design("PSY/caring-for-the-carers-1")
def _(d):
    x, y = 70, 40
    cols = [160, 180, 180]
    hh, rh = 42, 62
    d.rect(x, y, sum(cols), hh + rh * 3, fill=CREAM, rx=6)
    d.rect(x, y, sum(cols), hh, fill=SAND, rx=6)
    cx = x
    for w, s in zip(cols, ["Shift", "Carer", "Back-up"]):
        d.text(s, cx + w / 2, y + 28, size=16, weight=700)
        cx += w
    d.line(x + cols[0], y, x + cols[0], y + hh + rh * 3, width=2)
    d.line(x + cols[0] + cols[1], y, x + cols[0] + cols[1], y + hh + rh * 3, width=2)
    names = [("Morning", "Amal", "Beth"), ("Afternoon", "Beth", "Chen"), ("Night", "Chen", "Amal")]
    for r, row in enumerate(names):
        yy = y + hh + rh * r
        d.line(x, yy, x + sum(cols), yy, width=2)
        d.text(row[0], x + cols[0] / 2, yy + 38, size=16, weight=600)
        d.text(row[1], x + cols[0] + cols[1] / 2, yy + 38, size=16)
        d.circle(x + cols[0] + cols[1] + 40, yy + 32, 7, fill=YELLOW)
        d.text(row[2], x + cols[0] + cols[1] + 100, yy + 38, size=16)
    caption(d, "No shift lacks a second name.")


@design("PSY/caring-for-the-carers-2")
def _(d):
    d.piece("person-standing", 30, 50, 150)
    d.piece("person-standing", 460, 50, 150)
    d.text("Carer A", 105, 190, size=16, weight=600)
    d.text("Carer B", 535, 190, size=16, weight=600)
    d.arrow(190, 130, 450, 130, width=4)
    d.text("Handover", 320, 112, size=17, weight=600)
    d.piece("timeline-marker", 240, 180, 160)
    d.text("Handover time", 320, 316, size=16, weight=600)
    caption(d, "Handover is a timed exchange.")


@design("PSY/caring-for-the-carers-3")
def _(d):
    d.piece("bowl", 150, 50, 120)
    d.piece("pills", 370, 50, 120)
    d.piece("phone-call", 370, 200, 120)
    d.piece("person-sitting", 150, 200, 120)
    d.text("Food", 210, 44, size=16, weight=600)
    d.text("Medicine", 430, 44, size=16, weight=600)
    d.text("Outside contact", 430, 310, size=16, weight=600)
    d.text("Short break", 210, 310, size=16, weight=600)
    d.arrow(282, 100, 358, 100, width=3)
    d.arrow(430, 150, 430, 192, width=3)
    d.arrow(358, 250, 282, 250, width=3)
    d.arrow(210, 192, 210, 150, width=3)
    d.text("Daily", 320, 182, size=17, weight=700)
    caption(d, "Self-care is a daily cycle, not a one-off.", 346)


@design("PSY/caring-for-the-carers-4")
def _(d):
    chip(d, 300, 46, 300, 46, "Handover card", fill=SAND, weight=700)
    for i, s in enumerate(["Patient needs", "Due times", "Recent changes"]):
        chip(d, 300, 120 + i * 70, 300, 50, s)
        if i < 2:
            d.line(300, 145 + i * 70, 300, 165 + i * 70, width=3)
    d.piece("caution", 470, 200, 110)
    caption(d, "The card lists what changed, not only the routine.")


@design("PSY/caring-for-the-carers-5")
def _(d):
    d.piece("person-sitting", 24, 100, 170)
    x, y = 250, 40
    d.rect(x, y, 360, 256, fill=CREAM, rx=6)
    for i, s in enumerate(["Food", "Medicine", "Break", "Talking"]):
        yy = y + i * 64
        if i:
            d.line(x, yy, x + 360, yy, width=2)
        d.text(s, x + 30, yy + 40, size=17, weight=600, anchor="start")
        d.tick(x + 300, yy + 32, 16)
    caption(d, "Self-care is checked like any other task.")


@design("PSY/child-fever-and-dehydration-signs-1")
def _(d):
    d.text("Dehydrated", 120, 34, size=17, weight=700, fill=RED)
    d.text("Well hydrated", 520, 34, size=17, weight=700, fill=GREEN)
    d.line(250, 50, 250, 320, dash="8 8", width=3)
    d.line(390, 50, 390, 320, dash="8 8", width=3)
    rows = [("eye", "Eyes", "Sunken", "Normal"), ("mouth", "Mouth", "Dry", "Moist"), ("water-drop", "Tears", "None", "Present")]
    for i, (p, lab, a, b) in enumerate(rows):
        y = 58 + i * 90
        d.piece(p, 24, y, 90)
        d.text(a, 126, y + 44, size=16, weight=600, anchor="start")
        d.text(lab, 320, y + 44, size=17, weight=700)
        d.text(b, 410, y + 44, size=16, weight=600, anchor="start")
        d.piece(p, 526, y, 90)
    caption(d, "Compare the three signs to catch the difference early.")


@design("PSY/children-medicine-doses-and-safety-1")
def _(d):
    d.piece("bottle", 30, 80, 170)
    d.text("Concentration", 115, 250, size=17, weight=600)
    d.arrow(215, 135, 405, 135, width=4)
    d.arrow(405, 135, 215, 135, width=4)
    chip(d, 510, 135, 200, 64, "Millilitre marks\non the syringe", size=16)
    caption(d, "The same dose is a different volume per strength.")


@design("PSY/coping-with-grief-1")
def _(d):
    row_chips(d, ["Listen", "Acknowledge", "Offer practical\nhelp"], [130, 160, 180], 160, 70, 50, x0=40)
    caption(d, "Acknowledge first, so help lands as care.")


@design("PSY/coping-with-grief-2")
def _(d):
    d.piece("start-or-end", 245, 105, 150)
    labs = [(110, 60, "Numbness"), (530, 60, "Sadness and guilt"), (110, 290, "Poor sleep\nor appetite"), (530, 290, "Waves of memory")]
    for cx, cy, s in labs:
        chip(d, cx, cy, 190, 54, s)
    d.line(215, 90, 262, 160, width=3)
    d.line(425, 90, 378, 160, width=3)
    d.line(215, 262, 270, 200, width=3)
    d.line(425, 262, 370, 200, width=3)
    caption(d, "All four are expected, not failures.", 346)


@design("PSY/coping-with-grief-3")
def _(d):
    d.line(320, 30, 320, 300, dash="8 8", width=3)
    d.piece("do-not", 110, 50, 100)
    chip(d, 160, 220, 200, 60, "At least", size=17)
    d.piece("do", 430, 50, 100)
    chip(d, 480, 220, 260, 70, "I am sorry,\nthis is very hard", size=17)
    caption(d, "The helpful phrase names the loss directly.")


@design("PSY/coping-with-grief-4")
def _(d):
    d.piece("rock", 110, 80, 190)
    d.piece("flame", 340, 80, 190)
    d.text("Memorial", 320, 270, size=18, weight=700)
    caption(d, "Two household objects can make a ceremony.")


@design("PSY/coping-with-grief-5")
def _(d):
    chip(d, 80, 190, 128, 54, "Distress\nsign", size=16)
    d.arrow(146, 190, 190, 190, width=3)
    d.piece("decision", 190, 130, 130)
    d.text("Self-harm or weeks\nnot functioning?", 255, 100, size=16, weight=600)
    d.arrow(320, 190, 372, 190, width=3)
    d.text("Yes", 346, 176, size=16, weight=700, fill=RED)
    for i, s in enumerate(["Health post", "Counsellor", "Community leader"]):
        y = 80 + i * 110
        chip(d, 500, y, 200, 52, s)
        d.line(372, 190, 398, y, width=3)
    d.line(255, 250, 255, 290, width=3)
    d.text("No", 270, 270, size=16, weight=700, anchor="start", fill=GREEN)
    chip(d, 255, 312, 170, 38, "Keep checking in", size=15)


@design("PSY/daily-structure-1")
def _(d):
    xs = [90, 240, 400, 550]
    d.line(30, 250, 610, 250, width=4)
    for x, s in zip(xs, ["Morning", "Midday", "Afternoon", "Evening"]):
        d.circle(x, 250, 9, fill=YELLOW)
        chip(d, x, 44, 120, 40, s)
        d.line(x, 64, x, 241, dash="4 7", width=2)
    d.piece("axe", 180, 90, 120)
    d.text("Heavy work", 240, 292, size=16, weight=600)
    d.piece("person-sitting", 335, 85, 130)
    d.text("Rest", 400, 292, size=16, weight=600)
    caption(d, "Heavy work sits at midday, rest in the afternoon.", 336)


@design("PSY/daily-structure-2")
def _(d):
    for i in range(3):
        chip(d, 300, 50 + i * 54, 160, 44, f"Priority {i + 1}", fill=YELLOW)
    d.path("M 400 30 L 416 30 L 416 176 L 400 176", width=3)
    d.text("Finish first", 428, 108, size=16, weight=600, anchor="start")
    chip(d, 300, 250, 460, 70, "Everything else", size=17)
    caption(d, "The base is optional when the day goes wrong.")


@design("PSY/daily-structure-3")
def _(d):
    chip(d, 110, 40, 150, 44, "Date", size=16)
    d.piece("rain", 200, 8, 100)
    d.text("Owner", 460, 100, size=16, weight=700)
    d.text("Back-up", 560, 100, size=16, weight=700)
    for i in range(3):
        y = 150 + i * 62
        chip(d, 190, y, 260, 48, f"Priority {i + 1}")
        d.piece("person-standing", 415, y - 34, 90)
        d.piece("person-sitting", 515, y - 34, 90)
    caption(d, "No priority depends on one absence.", 346)


@design("PSY/daily-structure-4")
def _(d):
    d.rect(40, 130, 380, 70, fill=SAND, rx=8)
    d.rect(420, 130, 180, 70, fill=YELLOW, rx=8)
    d.text("Work", 230, 174, size=18, weight=700)
    d.text("Rest", 510, 174, size=18, weight=700)
    d.piece("timeline-marker", 385, 36, 110)
    d.text("Fixed slice", 436, 112, size=16, weight=600, anchor="start")
    d.arrow(40, 236, 600, 236, width=3)
    d.text("Day", 320, 270, size=16, weight=600)
    caption(d, "Rest is a fixed slice, not leftover time.")


@design("PSY/daily-structure-5")
def _(d):
    cols = [(110, "No rest"), (320, "One person"), (530, "No name")]
    for cx, lab in cols:
        d.piece("warning", cx - 45, 24, 90)
        d.text(lab, cx, 300, size=17, weight=600)
    d.piece("timeline-marker", 40, 130, 140)
    d.piece("person-standing", 262, 120, 120)
    d.rect(460, 137, 140, 70, fill=PAPER, rx=12, dash="8 6")
    caption(d, "Each sign points to a rigid routine.")


@design("PSY/dealing-with-fear-1")
def _(d):
    row_chips(d, ["Sit", "In through\nnose", "Hold", "Out through\nmouth", "Repeat"], [84, 106, 76, 150, 96], 150, 80, 24, x0=16, size=15)
    d.arrow(334, 215, 498, 215, width=3)
    d.text("Longest phase", 416, 246, size=16, weight=600)
    caption(d, "The long out-breath slows the heart.")


@design("PSY/dealing-with-fear-2")
def _(d):
    d.line(40, 260, 600, 260, width=2)
    d.path("M 40 260 L 190 90 L 290 90 L 600 260", width=5, stroke=BLUE)
    for x1, x2, lab in [(40, 190, "In"), (190, 290, "Hold"), (290, 600, "Out")]:
        d.arrow(x1 + 3, 290, x2 - 3, 290, width=2)
        d.arrow(x2 - 3, 290, x1 + 3, 290, width=2)
        d.text(lab, (x1 + x2) / 2, 320, size=17, weight=700)
    caption(d, "The exhale is drawn wider than the inhale.", 60)


@design("PSY/dealing-with-fear-3")
def _(d):
    xs = [30, 240, 450]
    labs = ["Fill bottle", "Check door", "Next task"]
    for i, (x, s) in enumerate(zip(xs, labs)):
        chip(d, x + 80, 70, 150, 48, s, fill=YELLOW if i == 2 else CREAM)
        d.piece("rock", x, 130, 160)
        if i < 2:
            d.arrow(x + 150, 230, xs[i + 1] + 8, 230, width=3, dash="8 7")
    caption(d, "Only the next stone needs thought.")


@design("PSY/dealing-with-fear-4")
def _(d):
    d.line(30, 190, 610, 190, width=4)
    for x, s in [(110, "Morning"), (530, "Evening")]:
        d.circle(x, 190, 10, fill=YELLOW)
        chip(d, x, 110, 150, 44, "Check news")
        d.line(x, 132, x, 180, width=2)
        d.text(s, x, 228, size=16, weight=600)
    d.arrow(190, 160, 450, 160, width=3)
    d.arrow(450, 160, 190, 160, width=3)
    d.text("Free", 320, 150, size=18, weight=700)
    caption(d, "News at fixed points, the day otherwise free.")


@design("PSY/dealing-with-fear-5")
def _(d):
    d.piece("ladder", 10, 70, 240)
    labs = ["Professional support", "Talk to someone", "Self-care"]
    for i, s in enumerate(labs):
        y = 60 + i * 100
        chip(d, 450, y, 240, 54, s)
        if i < 2:
            d.arrow(450, y + 96 - 30, 450, y + 30 + 0, width=3)
            d.text("Not helped?", 466, y + 62, size=15, weight=600, anchor="start")
    caption(d, "Move up only when the step below has not helped.", 346)


@design("PSY/first-aid-for-trauma-1")
def _(d):
    row_chips(d, ["Safety", "Sit", "Speak", "Listen"], [110, 110, 110, 110], 130, 66, 36, x0=46, size=17)
    d.piece("do-not", 260, 190, 120)
    d.text("Never reverse the order", 320, 330, size=16, weight=600)


@design("PSY/first-aid-for-trauma-2")
def _(d):
    d.rect(16, 70, 260, 130, fill=PAPER, rx=14, dash="10 8")
    d.piece("caution", 110, 48, 70)
    for i, p in enumerate(["rock", "flame", "waves"]):
        d.piece(p, 26 + i * 84, 100, 80)
    d.text("Hazard zone", 146, 228, size=16, weight=600)
    d.arrow(290, 150, 430, 150, width=3)
    d.arrow(430, 150, 290, 150, width=3)
    d.text("Distance", 360, 130, size=16, weight=600)
    d.piece("person-sitting", 460, 80, 150)
    d.text("Gathering spot", 535, 228, size=16, weight=600)
    caption(d, "The spot sits far from danger.")


@design("PSY/first-aid-for-trauma-3")
def _(d):
    d.piece("person-standing", 30, 60, 160)
    d.piece("person-standing", 450, 60, 160)
    d.arrow(200, 150, 440, 150, width=4)
    d.arrow(440, 150, 200, 150, width=4)
    d.text("Reflective sentence", 320, 128, size=16, weight=600)
    d.text("Key word repeated", 320, 190, size=16, weight=600)
    caption(d, "Listening echoes their words, not fixes the feeling.")


@design("PSY/first-aid-for-trauma-4")
def _(d):
    for cx, s in [(110, "Blame"), (320, "Broken promise"), (530, "Looping question")]:
        d.piece("do-not", cx - 60, 60, 120)
        chip(d, cx, 220, 190, 54, s)
    caption(d, "These three habits restart fear.")


@design("PSY/first-aid-for-trauma-5")
def _(d):
    d.piece("person-sitting", 24, 70, 160)
    d.piece("cup", 70, 220, 90)
    x, y = 250, 50
    d.rect(x, y, 360, 216, fill=CREAM, rx=6)
    for i, s in enumerate(["Safe", "Warm", "Heard"]):
        yy = y + i * 72
        if i:
            d.line(x, yy, x + 360, yy, width=2)
        d.text(s, x + 30, yy + 44, size=18, weight=600, anchor="start")
        d.tick(x + 300, yy + 36, 18)
    caption(d, "The list ends with the person settled.")


@design("PSY/infant-feeding-when-formula-runs-out-1")
def _(d):
    d.piece("person-sitting", 20, 70, 220)
    d.piece("infant", 200, 120, 130)
    chip(d, 500, 90, 170, 44, "Chin touching", size=16)
    chip(d, 500, 230, 170, 44, "Nose clear", size=16)
    d.leader(415, 90, 300, 150)
    d.leader(415, 230, 300, 195)
    caption(d, "Clear nose and chin contact make latching work.")


@design("PSY/infant-feeding-when-formula-runs-out-2")
def _(d):
    d.piece("infant", 50, 80, 220)
    d.piece("infant", 370, 80, 220)
    d.line(320, 40, 320, 300, dash="8 8", width=3)
    d.tick(160, 56, 18)
    d.cross(480, 56, 18)
    d.text("Soft spot", 92, 124, size=16, weight=600)
    d.leader(94, 130, 102, 162)
    d.text("Soft spot", 414, 124, size=16, weight=600)
    d.leader(416, 130, 424, 162)
    d.text("Normal", 160, 290, size=17, weight=700)
    d.text("Sunken", 480, 290, size=17, weight=700)
    caption(d, "A sunken soft spot is a dehydration sign.")


@design("PSY/keeping-hope-1")
def _(d):
    d.line(70, 160, 480, 160, width=4)
    for i, x in enumerate([90, 210, 330]):
        d.circle(x, 160, 14, fill=YELLOW)
        d.tick(x, 110, 16)
        d.text(f"Milestone {i + 1}", x, 214, size=16, weight=600)
    d.piece("start-or-end", 440, 105, 150)
    d.text("Goal", 515, 214, size=17, weight=700)
    caption(d, "Progress is counted in small steps.")


@design("PSY/keeping-hope-2")
def _(d):
    d.piece("ladder", 10, 60, 240)
    for i, s in enumerate(["End of crisis", "Done", "Done", "Done"]):
        y = 56 + i * 76
        if i == 0:
            d.rect(340, y - 28, 240, 56, fill=PAPER, rx=12, dash="8 6")
            d.text(s, 460, y + 6, size=16, weight=600)
        else:
            chip(d, 460, y, 240, 56, s)
            d.tick(366, y, 14)
    caption(d, "Hope climbs by finished rungs, not by the top one.", 346)


@design("PSY/keeping-hope-3")
def _(d):
    d.piece("table", 20, 70, 230)
    d.piece("bowl", 290, 90, 140)
    d.piece("note", 460, 90, 140)
    d.text("Tradition", 530, 230, size=17, weight=700)
    d.text("Song at dusk", 320, 320, size=17, weight=700)


@design("PSY/keeping-hope-4")
def _(d):
    chip(d, 110, 50, 150, 44, "Known", fill=SAND, weight=700)
    chip(d, 290, 50, 150, 44, "Unknown", fill=SAND, weight=700)
    for i in range(3):
        y = 130 + i * 66
        chip(d, 110, y, 150, 48, "")
        d.tick(110, y, 14)
        chip(d, 290, y, 150, 48, "?", size=20)
        d.arrow(368, y, 440, y, width=3)
    chip(d, 530, 196, 150, 190, "Group\naction", size=17, fill=YELLOW)
    caption(d, "Every unknown is given an action.")


@design("PSY/keeping-hope-5")
def _(d):
    chip(d, 130, 160, 200, 80, "Big goal", size=18, fill=YELLOW)
    for g in range(2):
        x0 = 330 + g * 130
        for i in range(4):
            d.line(x0 + i * 22, 120, x0 + i * 22, 200, width=5)
        d.line(x0 - 8, 190, x0 + 78, 130, width=5)
    d.text("Daily wins", 430, 250, size=17, weight=700)
    caption(d, "Small daily wins sit beside the big goal.")


@design("PSY/leadership-in-a-group-1")
def _(d):
    chip(d, 320, 36, 150, 44, "Leader", fill=YELLOW, weight=700)
    d.line(320, 58, 320, 90, width=3)
    d.line(65.5, 90, 570.5, 90, width=3)
    roles = ["Water", "Food", "Fire", "Medical", "Children", "Comms"]
    for i, s in enumerate(roles):
        cx = 16 + 49.5 + i * 101
        d.line(cx, 90, cx, 120, width=3)
        chip(d, cx, 148, 99, 52, s, size=15, weight=400)
        d.line(cx, 174, cx, 210, width=3)
        chip(d, cx, 236, 80, 40, "Deputy", size=15, weight=400, fill=PAPER)
    caption(d, "No role lacks a second name.")


@design("PSY/leadership-in-a-group-2")
def _(d):
    d.piece("survivor-mark", 260, 130, 120)
    labs = [(320, 36, "Calm instructions"), (110, 120, "Explains reasons"), (530, 120, "Listens to dissent"), (130, 270, "Admits mistakes"), (510, 270, "Cares for wellbeing")]
    for cx, cy, s in labs:
        chip(d, cx, cy, 200, 46, s)
    d.line(320, 59, 320, 134, width=3)
    d.line(210, 130, 275, 165, width=3)
    d.line(430, 130, 365, 165, width=3)
    d.line(230, 255, 280, 215, width=3)
    d.line(410, 255, 360, 215, width=3)
    caption(d, "Leadership is habits, not control.", 346)


@design("PSY/leadership-in-a-group-3")
def _(d):
    row_chips(d, ["Facts", "Options", "Decide", "Review"], [120, 120, 120, 120], 110, 70, 40, x0=20, size=17)
    d.curve_arrow("M 560 148 C 560 290 80 290 80 150", (80, 150), -1.5708, width=4)
    d.text("Fresh facts", 320, 234, size=16, weight=600)
    caption(d, "Review feeds fresh facts into the next decision.")


@design("PSY/leadership-in-a-group-4")
def _(d):
    d.piece("table", 10, 80, 190)
    d.text("Meeting", 105, 250, size=17, weight=700)
    d.text("+", 225, 160, size=28, weight=700)
    d.piece("timeline-marker", 250, 90, 140)
    d.text("Time limit", 320, 250, size=17, weight=700)
    d.text("+", 415, 160, size=28, weight=700)
    d.piece("note", 450, 85, 160)
    d.text("Written record", 530, 250, size=17, weight=700)
    caption(d, "Both are built into each meeting.")


@design("PSY/leadership-in-a-group-5")
def _(d):
    x, y, cw = 140, 40, 62
    grid(d, x, y, cw, 56, 7, 2, header_h=34)
    for i, s in enumerate(DAYS):
        d.text(s, x + cw * i + cw / 2, y + 23, size=15, weight=600)
    rest = {2, 5}
    for i in range(7):
        cx = x + cw * i + cw / 2
        if i in rest:
            d.circle(cx, y + 34 + 28, 9, fill=YELLOW)
            d.text("Lead", cx, y + 34 + 56 + 33, size=15, weight=600)
        else:
            d.text("Lead", cx, y + 34 + 33, size=15, weight=600)
    d.text("Leader", x - 12, y + 34 + 33, size=16, weight=600, anchor="end")
    d.text("Deputy", x - 12, y + 34 + 56 + 33, size=16, weight=600, anchor="end")
    d.circle(250, 230, 9, fill=YELLOW)
    d.text("Rest day", 270, 236, size=16, weight=600, anchor="start")
    caption(d, "Handover is built into the rota.")
