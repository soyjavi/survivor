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


def flow(d, items, y, w=130, arrow=True, label_dy=26, size=16):
    n = len(items)
    gap = (640 - n * w) / (n + 1)
    centers = []
    for i, (piece, label) in enumerate(items):
        x = gap + i * (w + gap)
        d.piece(piece, x, y, w)
        d.text(label, x + w / 2, y + w * 0.75 + label_dy, size=size, weight=600)
        centers.append(x + w / 2)
        if arrow and i < n - 1:
            d.arrow(x + w + 4, y + w * 0.375, x + w + gap - 4, y + w * 0.375)
    return centers


def tbl(d, x, y, widths, header, rows, rowh=34, hh=36, size=15, hl=None):
    cx = []
    xx = x
    for i, (w, h) in enumerate(zip(widths, header)):
        d.rect(xx, y, w, hh, fill=INK, rx=0)
        d.text(h, xx + w / 2, y + hh / 2 + 5, size=size, weight=600, fill=CREAM)
        for r in range(rows):
            fill = YELLOW if hl == i else CREAM
            d.rect(xx, y + hh + r * rowh, w, rowh, fill=fill, rx=0, width=2)
        cx.append(xx + w / 2)
        xx += w
    return cx


def timeline(d, y, ticks):
    d.arrow(24, y, 616, y, width=4)
    for x in ticks:
        d.line(x, y - 9, x, y + 9, width=3)


def loopback(d, xl, xf, y):
    d.curve_arrow(f"M{xl} {y}C{xl} {y + 70} {xf} {y + 70} {xf} {y}", (xf, y), -math.pi / 2)


@design("PSY/looking-after-isolated-older-people-1")
def _(d):
    tbl(d, 24, 80, [110, 130], ["Name", "Address"], 4, rowh=36)
    tbl(d, 336, 80, [140, 150], ["Time seen", "Water checked"], 4, rowh=36, size=14)
    d.tick(406, 134, 12)
    d.tick(406, 170, 12)
    d.tick(551, 134, 12)
    d.tick(551, 170, 12)
    d.arrow(274, 170, 330, 170)
    d.text("Street list", 144, 280, size=16, weight=600)
    d.text("Visit sheet", 481, 280, size=16, weight=600)
    caption(d, "The list is the source, the sheet records each visit.")


@design("PSY/looking-after-isolated-older-people-2")
def _(d):
    d.piece("map", 130, 16, 380)
    xs = [215, 270, 325, 380, 435]
    d.line(200, 150, 450, 150, width=3)
    for i, x in enumerate(xs):
        if i < 3:
            d.badge(i + 1, x, 150, 16)
        else:
            d.circle(x, 150, 16, fill=CREAM)
            d.text(str(i + 1), x, 156, size=15, weight=600)
    d.piece("legend-solid", 80, 290, 130)
    d.text("Visited", 228, 343, size=17, weight=600, anchor="start")
    d.piece("legend-dashed", 340, 290, 130)
    d.text("Not yet", 488, 343, size=17, weight=600, anchor="start")


@design("PSY/looking-after-isolated-older-people-3")
def _(d):
    c = flow(d, [("step-box", "Visit"), ("step-box", "Water and food"), ("step-box", "Health"), ("step-box", "Toilet and washing")], 100, w=130, size=15)
    for i, x in enumerate(c):
        d.badge(i + 1, x, 82, 15)
    caption(d, "Stock is checked before the conversation.")


@design("PSY/looking-after-isolated-older-people-4")
def _(d):
    tbl(d, 40, 60, [110, 110, 190, 150], ["Date", "Time", "Note", "Next check"], 5, rowh=40)
    caption(d, "Each visit is recorded so another person can pick it up.")


@design("PSY/looking-after-isolated-older-people-5")
def _(d):
    for i, s in enumerate(["Confusion", "Fall", "Chest pain", "Breathing trouble"]):
        y = 14 + i * 76
        d.piece("warning", 90, y, 84)
        d.piece("step-box", 220, y, 84)
        d.text(s, 330, y + 38, size=17, weight=600, anchor="start")
    caption(d, "Emergencies: report at once, do not wait.")


@design("PSY/looking-after-isolated-older-people-6")
def _(d):
    d.piece("person-sitting", 10, 100, 200)
    d.piece("threshold", 215, 151, 170)
    d.text("Doorway", 300, 275, size=17, weight=600)
    d.piece("person-standing", 430, 100, 200)
    d.piece("cup", 385, 105, 90)
    d.arrow(440, 200, 375, 200)
    d.text("Water", 410, 262, size=17, weight=600)
    caption(d, "Brief, at the threshold, offering one thing.")


@design("PSY/making-rationing-decisions-as-a-group-1")
def _(d):
    n = 5
    w = 100
    gap = (640 - n * w) / (n + 1)
    labels = ["Facts", "Principles", "Decide", "Record", "Review"]
    cs = []
    for i, s in enumerate(labels):
        x = gap + i * (w + gap)
        d.piece("step-box", x, 80, w)
        d.text(s, x + w / 2, 190, size=16, weight=600)
        cs.append(x + w / 2)
        if i < n - 1:
            d.arrow(x + w + 3, 118, x + w + gap - 3, 118)
    loopback(d, cs[-1], cs[0], 215)
    caption(d, "Repeat whenever stock changes.")


@design("PSY/making-rationing-decisions-as-a-group-2")
def _(d):
    tbl(d, 30, 60, [90, 80, 120, 170, 110], ["Item", "Count", "Daily use", "Days remaining", "Initials"], 4, rowh=40, hl=3)
    caption(d, "Days remaining drives the decision; two initials confirm each count.")


@design("PSY/making-rationing-decisions-as-a-group-3")
def _(d):
    labels = ["Count stock", "Principles", "Decide", "Portion", "Post"]
    pieces = ["step-1", "step-2", "step-3", "step-box", "step-box"]
    w = 96
    gap = (640 - 5 * w) / 6
    for i, (p, s) in enumerate(zip(pieces, labels)):
        x = gap + i * (w + gap)
        d.piece(p, x, 50, w)
        d.text(s, x + w / 2, 160, size=15, weight=600)
        if i < 4:
            d.arrow(x + w + 3, 86, x + w + gap - 3, 86)
        if i == 3:
            d.piece("bowl", x - 12, 205, 120)
            d.arrow(x + w / 2, 172, x + w / 2, 215)
    caption(d, "The portion is set last.")


@design("PSY/making-rationing-decisions-as-a-group-4")
def _(d):
    d.piece("barrel", 245, 110, 150)
    d.piece("lock", 300, 85, 40)
    d.text("Store", 320, 280, size=16, weight=600)
    d.piece("person-standing", 20, 120, 150)
    d.piece("person-standing", 470, 120, 150)
    d.piece("do", 89, 82, 44)
    d.piece("do", 539, 82, 44)
    d.arrow(175, 190, 245, 190, dash="8 6")
    d.arrow(465, 190, 395, 190, dash="8 6")
    d.text("Counter 1", 95, 280, size=16, weight=600)
    d.text("Counter 2", 545, 280, size=16, weight=600)
    caption(d, "Two independent people check the same count.")


@design("PSY/making-rationing-decisions-as-a-group-5")
def _(d):
    c = flow(d, [("person-standing", "Concern"), ("step-box", "Private talk"), ("step-box", "Agreed change"), ("step-box", "Group decision")], 110, w=120, size=15)
    d.piece("note", 45, 140, 44)
    caption(d, "Private steps feed back into public ones.")


@design("PSY/recovering-after-a-disaster-1")
def _(d):
    timeline(d, 270, [40, 190, 340])
    d.piece("step-box", 40, 100, 120)
    d.piece("step-box", 190, 100, 120)
    d.piece("step-box", 340, 15, 270)
    d.text("Immediate needs", 100, 225, size=15, weight=600)
    d.text("Daily life", 250, 225, size=15, weight=600)
    d.text("Rebuilding", 475, 225, size=16, weight=600)
    caption(d, "Rebuilding starts once the first two are reliable.")


@design("PSY/recovering-after-a-disaster-2")
def _(d):
    d.piece("ladder", 10, 75, 290)
    for i, s in enumerate(["Roof", "Doors", "Electricity", "Drainage"]):
        y = 250 - i * 76
        d.badge(i + 1, 300, y + 31, 16)
        d.piece("step-box", 335, y, 84)
        d.text(s, 435, y + 38, size=17, weight=600, anchor="start")
    caption(d, "Safety repairs first, cosmetic work last.", 346)


@design("PSY/recovering-after-a-disaster-3")
def _(d):
    tbl(d, 130, 40, [190, 190], ["Task", "Neighbour"], 3, rowh=76)
    for r in range(3):
        y = 76 + r * 76
        d.piece("step-box", 175, y + 6, 100)
        d.piece("person-standing", 380, y + 4, 100)
    caption(d, "Every repair has a named neighbour.")


@design("PSY/recovering-after-a-disaster-4")
def _(d):
    cx = tbl(d, 90, 50, [140, 190, 190], ["Date", "Photos", "Receipts"], 3, rowh=70)
    for r in range(3):
        y = 86 + r * 70
        d.piece("timeline-marker", 112, y + 6, 70)
    for r, c in [(0, 1), (0, 2), (1, 1), (2, 2)]:
        d.piece("note", cx[c] - 28, 86 + r * 70 + 8, 56)
    caption(d, "Evidence is indexed by date.")


@design("PSY/recovering-after-a-disaster-5")
def _(d):
    d.arrow(40, 318, 40, 40, width=3)
    d.text("Progress", 54, 48, size=16, weight=600, anchor="start")
    d.arrow(40, 318, 610, 318, width=3)
    d.path("M50 270L160 200L200 225L320 130L360 160L480 85L590 55", stroke=GREEN, width=5)
    for (x, y) in [(200, 225), (360, 160)]:
        d.piece("warning", x - 24, y + 14, 48)
        d.text("Setback", x, y + 70, size=16, weight=600)


@design("PSY/recovering-after-a-disaster-6")
def _(d):
    c = flow(d, [("step-box", ""), ("step-box", ""), ("step-box", ""), ("step-box", "")], 130, w=120)
    for i, x in enumerate(c):
        d.piece("do", x - 22, 70, 44)
        d.badge(i + 1, x, 260, 16)
    caption(d, "No box is ticked before the one before it.")


@design("PSY/resolving-conflict-1")
def _(d):
    labels = ["Pause", "Meet privately", "Each speaks", "Summarise", "Shared goal", "One change"]
    w = 120
    gap = (640 - 3 * w) / 4
    for i, s in enumerate(labels):
        row, col = divmod(i, 3)
        x = gap + col * (w + gap)
        y = 30 + row * 160
        d.piece("step-box", x, y, w)
        d.badge(i + 1, x + 6, y + 6, 15)
        d.text(s, x + w / 2, y + 112, size=16, weight=600)
        if col < 2:
            d.arrow(x + w + 4, y + 45, x + w + gap - 4, y + 45)
    caption(d, "The pause comes before any meeting.")


@design("PSY/resolving-conflict-2")
def _(d):
    xs = [50, 260, 470]
    for x, s in zip(xs, ["Withdrawal", "Remarks", "Avoided jobs"]):
        d.piece("warning", x, 20, 120)
        d.text(s, x + 60, 150, size=16, weight=600)
    d.arrow(320, 170, 320, 205)
    d.piece("door", 255, 210, 130)
    d.text("Open anger", 450, 270, size=16, weight=600, anchor="start")
    caption(d, "Early signs appear before open anger.")


@design("PSY/resolving-conflict-3")
def _(d):
    d.piece("step-box", 20, 50, 340)
    d.text("One agreed change", 400, 140, size=18, weight=600, anchor="start")
    d.leader(395, 134, 300, 134)
    d.piece("timeline-marker", 420, 190, 100)
    d.text("Check-by date", 410, 292, size=16, weight=600, anchor="start")
    caption(d, "One change with a date, not a full settlement.")


@design("PSY/resolving-conflict-4")
def _(d):
    d.piece("table-grid", 210, 110, 220)
    d.piece("person-sitting", 20, 130, 150)
    d.piece("person-sitting", 470, 130, 150)
    d.piece("person-sitting", 245, 0, 150)
    d.text("Person A", 95, 262, size=16, weight=600)
    d.text("Person B", 545, 262, size=16, weight=600)
    d.text("Mediator", 410, 70, size=16, weight=600, anchor="start")
    caption(d, "Equal seating and a neutral third person.")


@design("PSY/resolving-conflict-5")
def _(d):
    d.piece("person-standing", 20, 40, 130)
    d.piece("person-standing", 490, 40, 130)
    d.arrow(165, 120, 475, 120, width=3, dash="9 7")
    d.arrow(475, 120, 165, 120, width=3, dash="9 7")
    d.text("Safe distance", 320, 105, size=17, weight=600)
    d.line(16, 190, 624, 190, dash="3 9", width=3)
    d.piece("phone-call", 255, 210, 130)
    d.text("Call for help", 410, 270, size=16, weight=600, anchor="start")
    caption(d, "Separation comes before any mediation.")


@design("PSY/reuniting-separated-children-1")
def _(d):
    for i in range(4):
        d.piece("person-standing", 6 + i * 68, 110, 110)
    d.text("Family", 150, 260, size=16, weight=600)
    d.piece("trail-marker", 300, 80, 120)
    d.piece("waypoint-pin", 500, 30, 90)
    d.piece("waypoint-pin", 500, 190, 90)
    d.arrow(405, 150, 495, 95)
    d.arrow(405, 190, 495, 250)
    d.text("Near point", 545, 150, size=16, weight=600)
    d.text("Far point", 545, 310, size=16, weight=600)
    caption(d, "Each child needs both.", 346)


@design("PSY/routines-for-children-1")
def _(d):
    c = flow(d, [("step-box", s) for s in ["Meals", "Play", "Learning", "Sleep", "Others"]], 100, w=100, size=15)
    for i, x in enumerate(c):
        d.badge(i + 1, x, 80, 14)
    caption(d, "The card's order is the schedule.")


@design("PSY/routines-for-children-2")
def _(d):
    w = 76
    gap = (640 - 6 * w) / 7
    cs = []
    for i, s in enumerate(["Wake", "Eat", "Work", "Play", "Rest", "Sleep"]):
        x = gap + i * (w + gap)
        d.piece("step-box", x, 80, w)
        d.text(s, x + w / 2, 170, size=16, weight=600)
        cs.append(x + w / 2)
        if i < 5:
            d.arrow(x + w + 2, 108, x + w + gap - 2, 108, width=3)
    loopback(d, cs[-1], cs[0], 195)
    caption(d, "Order repeats daily and matters more than clock times.")


@design("PSY/routines-for-children-3")
def _(d):
    for x in (-10, 210, 430):
        d.piece("ground-line", x, 170, 220)
    d.piece("sun", 40, 115, 100)
    d.piece("sun", 270, 10, 100)
    d.piece("sun", 500, 115, 100)
    d.piece("shadow-stick", 255, 150, 130)
    d.piece("compass-rose", 490, 0, 130)
    d.text("Morning", 90, 318, size=16, weight=600)
    d.text("Noon", 320, 318, size=16, weight=600)
    d.text("Evening", 550, 318, size=16, weight=600)


@design("PSY/routines-for-children-4")
def _(d):
    timeline(d, 292, [40, 190])
    d.piece("step-box", 40, 105, 120)
    d.piece("step-box", 190, 20, 330)
    d.text("Learning", 100, 258, size=16, weight=600)
    d.text("Play", 355, 258, size=16, weight=600)
    caption(d, "Learning stays a short slot and play follows.")


@design("PSY/routines-for-children-5")
def _(d):
    d.piece("person-sitting", 245, 6, 150)
    d.piece("person-sitting", 450, 120, 150)
    d.piece("person-sitting", 245, 240, 150)
    d.piece("person-sitting", 40, 120, 150)
    d.text("Speaker", 410, 50, size=16, weight=600, anchor="start")
    d.text("Next", 525, 110, size=16, weight=600)
    d.curve_arrow("M385 70C430 80 450 100 465 135", (465, 135), 1.1)
    d.curve_arrow("M505 245C490 280 450 300 410 305", (410, 305), 2.8)
    d.curve_arrow("M255 305C215 300 180 280 160 245", (160, 245), -2.0)
    d.curve_arrow("M135 125C150 90 190 70 235 65", (235, 65), -0.3)


@design("PSY/routines-for-children-6")
def _(d):
    d.piece("person-sitting", 20, 100, 190)
    d.piece("table-grid", 190, 150, 170)
    d.piece("document", 440, 90, 150)
    d.text("Draw the day", 275, 300, size=16, weight=600)
    d.text("Checklist", 515, 262, size=16, weight=600)
    caption(d, "Drawing ends the day and records the routine.")


@design("PSY/sleep-and-stress-1")
def _(d):
    d.piece("table-grid", 24, 60, 250)
    d.piece("table-header", 366, 60, 250)
    d.text("+", 320, 175, size=44, weight=600)
    d.text("Fixed bedtime", 150, 290, size=17, weight=600)
    d.text("Night watch", 491, 290, size=17, weight=600)


@design("PSY/sleep-and-stress-2")
def _(d):
    d.piece("bed", 190, 95, 260)
    spots = [(120, 70, "Noise"), (320, 40, "Cold"), (520, 70, "Light"), (120, 315, "Hunger"), (520, 315, "Worry")]
    d.arrow(160, 90, 245, 140)
    d.arrow(320, 55, 320, 128)
    d.arrow(480, 90, 395, 140)
    d.arrow(160, 290, 240, 255)
    d.arrow(480, 290, 400, 255)
    for x, y, s in spots:
        d.text(s, x, y, size=18, weight=600)


@design("PSY/sleep-and-stress-3")
def _(d):
    cx = tbl(d, 25, 50, [100, 120, 120, 120, 120], ["", "Block 1", "Block 2", "Block 3", "Block 4"], 2, rowh=100)
    plan = [("Pair A", [1, 0, 1, 0]), ("Pair B", [0, 1, 0, 1])]
    for r, (name, cells) in enumerate(plan):
        y = 86 + r * 100
        d.text(name, cx[0], y + 55, size=16, weight=600)
        for c, watch in enumerate(cells):
            if watch:
                d.piece("person-standing", cx[c + 1] - 56, y + 14, 70)
                d.piece("person-standing", cx[c + 1] - 14, y + 14, 70)
            else:
                d.text("Sleep", cx[c + 1], y + 55, size=16, weight=600, fill="#7a6f5c")
    caption(d, "No one stands watch two blocks in a row.")


@design("PSY/sleep-and-stress-4")
def _(d):
    d.arrow(60, 280, 60, 40, width=3)
    d.arrow(60, 280, 610, 280, width=3)
    d.text("Light", 50, 76, size=16, weight=600, anchor="end")
    d.text("Deep", 50, 230, size=16, weight=600, anchor="end")
    d.path("M70 80L110 210L160 90L210 195L260 90L310 175L360 85L410 155L460 80L510 130L560 78L600 75", stroke=BLUE, width=4)
    d.text("Bedtime", 70, 312, size=16, weight=600)
    d.text("Morning", 580, 312, size=16, weight=600)
    caption(d, "Deep sleep is early, so early rest matters most.", 346)


@design("PSY/sleep-and-stress-5")
def _(d):
    timeline(d, 250, [60, 300, 380, 470, 560])
    d.piece("step-box", 285, 135, 110)
    d.text("Nap 20 minutes", 340, 118, size=16, weight=600)
    d.piece("threshold", 455, 150, 130)
    d.text("Last daylight", 515, 290, size=16, weight=600)
    d.text("Daylight", 150, 232, size=16, weight=600)
    caption(d, "A late nap harms night sleep.")


@design("PSY/sleep-and-stress-6")
def _(d):
    for i, s in enumerate(["Bedtime", "Worries notebook", "Evening drinks"]):
        x = 40 + i * 200
        d.piece("step-box", x, 50, 140)
        d.text(s, x + 70, 195, size=16, weight=600)
    d.piece("bottle", 465, 215, 100)
    caption(d, "Each object maps to one habit.")


@design("PSY/teenagers-in-a-crisis-1")
def _(d):
    cx = tbl(d, 130, 40, [190, 190], ["Role", "Rule"], 3, rowh=76)
    for r in range(3):
        y = 76 + r * 76
        d.piece("person-standing", cx[0] - 50, y + 4, 100)
        d.piece("step-box", cx[1] - 50, y + 6, 100)
    caption(d, "Every role comes with a stated rule.")


@design("PSY/teenagers-in-a-crisis-2")
def _(d):
    cx = tbl(d, 130, 40, [190, 190], ["Rule", "Reason"], 3, rowh=76)
    for r in range(3):
        y = 76 + r * 76
        d.piece("step-box", cx[0] - 50, y + 6, 100)
        d.piece("step-box", cx[1] - 50, y + 6, 100)
        d.line(cx[0] + 40, y + 38, cx[1] - 40, y + 38, width=3)
    caption(d, "Each rule is paired with its reason.")


@design("PSY/teenagers-in-a-crisis-3")
def _(d):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    cx = tbl(d, 30, 40, [80] * 7, days, 3, rowh=50)
    for r, c in [(0, 1), (0, 4), (1, 2), (1, 5), (2, 0), (2, 3), (2, 6)]:
        d.circle(cx[c], 76 + r * 50 + 25, 11, fill="#d9622b")
    d.piece("legend-dot", 190, 250, 110)
    d.text("Friends window", 305, 308, size=17, weight=600, anchor="start")
    caption(d, "Contact in set blocks: not banned, not unlimited.")


@design("PSY/teenagers-in-a-crisis-4")
def _(d):
    d.piece("waypoint-pin", 55, 70, 120)
    d.piece("person-standing", 215, 70, 120)
    d.piece("person-standing", 290, 70, 120)
    d.piece("timeline-marker", 465, 70, 120)
    d.text("Where", 115, 240, size=17, weight=600)
    d.text("With whom", 320, 240, size=17, weight=600)
    d.text("When back", 525, 240, size=17, weight=600)
    caption(d, "Asked at every departure.")


@design("PSY/teenagers-in-a-crisis-5")
def _(d):
    d.piece("note", 50, 80, 140)
    d.piece("note", 450, 80, 140)
    d.piece("arrow-both-ways", 220, 110, 200)
    d.text("Adult to teen", 120, 250, size=17, weight=600)
    d.text("Teen to adult", 520, 250, size=17, weight=600)
    caption(d, "A shared channel, not one-way instruction.")


@design("PSY/teenagers-in-a-crisis-6")
def _(d):
    d.piece("person-standing", 30, 80, 200)
    d.piece("note", 170, 150, 60)
    for i in range(4):
        d.piece("person-sitting", 290 + i * 85, 130, 100)
    d.text("Team leader", 125, 270, size=17, weight=600)
    d.text("Children", 470, 270, size=17, weight=600)
    caption(d, "The teenager leads a team, not just watches children.")
