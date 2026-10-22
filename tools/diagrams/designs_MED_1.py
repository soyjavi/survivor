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


def steps(d, labels, pieces, y=60, pw=100, ch=70, size=16, caption_text=None):
    n = len(labels)
    col = 608 / n
    cw = col - (44 if n < 5 else 30)
    cy = y + pw * 0.75 + 10 + ch / 2
    for i, (label, piece) in enumerate(zip(labels, pieces)):
        cx = 16 + col * (i + 0.5)
        d.piece(piece, cx - pw / 2, y, pw)
        chip(d, cx, cy, cw, ch, label, size=size)
        if i < n - 1:
            d.arrow(cx + cw / 2 + 4, cy, cx + col - cw / 2 - 4, cy, width=3)
    if caption_text:
        caption(d, caption_text)


def loop_under(d, x_from, x_to, y_top, y_bot):
    d.curve_arrow(f"M{x_from} {y_top}V{y_bot}H{x_to}V{y_top + 8}", (x_to, y_top), -math.pi / 2, width=3)


@design("MED/altitude-sickness-1")
def _(d):
    d.arrow(70, 300, 610, 300, width=3)
    d.arrow(70, 300, 70, 40, width=3)
    d.text("days", 610, 325, size=16, weight=600, anchor="end")
    d.text("height", 82, 50, size=16, weight=600, anchor="start")
    d.path("M70 295L230 245L330 245L560 155", stroke=GREEN, width=5)
    d.path("M70 295L560 70", stroke=RED, width=5, dash="10 8")
    d.line(280, 250, 280, 300, dash="5 6", width=3)
    chip(d, 280, 322, 100, 28, "rest day", size=15)
    d.text("safe acclimatisation", 600, 212, size=16, weight=600, anchor="end", fill=GREEN)
    d.text("risky ascent", 200, 130, size=16, weight=600, anchor="start", fill=RED)


@design("MED/altitude-sickness-2")
def _(d):
    d.piece("start-or-end", 10, 120, 120)
    d.text("symptoms", 70, 240, size=16, weight=600)
    d.piece("decision", 150, 100, 160)
    d.arrow(300, 150, 440, 90, width=3)
    d.arrow(300, 200, 440, 260, width=3)
    d.text("mild", 360, 108, size=16, weight=600, anchor="start")
    d.text("worsening\nor confusion", 330, 262, size=16, weight=600, anchor="start")
    d.piece("do", 450, 40, 80)
    chip(d, 560, 126, 120, 56, "rest and\nreassess", size=15)
    d.piece("warning", 450, 220, 80)
    chip(d, 560, 306, 120, 40, "descend now", size=15)
    caption(d, "Confusion alone means descend, no waiting.", 346)


@design("MED/asthma-attacks-1")
def _(d):
    steps(d, ["Shake\ninhaler", "Fit to\nspacer", "One puff", "Slow\nbreath in"], ["step-1", "step-2", "step-3", "step-box"], y=60, pw=110)
    caption(d, "One puff at a time, spacer between inhaler and mouth.")


@design("MED/asthma-attacks-2")
def _(d):
    x0, y0 = 16, 90
    lw, cw, rh = 140, 150, 44
    rows = ["speech", "breathing rate", "lip colour", "action"]
    heads = ["mild", "moderate", "severe"]
    d.rect(x0, y0, lw + 3 * cw, rh, fill=INK, rx=8)
    for i, h in enumerate(heads):
        d.text(h, x0 + lw + cw * (i + 0.5), y0 + 29, size=17, weight=700, fill="#ffffff")
    for r, label in enumerate(rows):
        y = y0 + rh * (r + 1)
        d.rect(x0, y, lw + 3 * cw, rh, fill=CREAM if r % 2 == 0 else PAPER, rx=0)
        d.text(label, x0 + 12, y + 29, size=16, weight=600, anchor="start")
    for i in range(1, 4):
        x = x0 + lw + cw * (i - 1)
        d.line(x, y0, x, y0 + rh * 5, width=2)
    d.text("1-2 words", x0 + lw + cw * 2.5, y0 + rh + 29, size=16, weight=700, fill=RED)
    d.piece("caution", x0 + lw + cw * 2 + 40, 8, 80)
    caption(d, "One or two words at a time: call for help now.", 346)


@design("MED/asthma-attacks-3")
def _(d):
    d.rect(200, 120, 240, 90, fill=CREAM, rx=14)
    d.text("spacer chamber", 320, 172, size=18, weight=700)
    chip(d, 100, 60, 150, 34, "inhaler slot", size=15)
    d.leader(100, 78, 204, 134)
    chip(d, 540, 60, 150, 34, "mask seal", size=15)
    d.leader(540, 78, 436, 134)
    d.arrow(230, 260, 410, 260, width=4)
    d.text("dose", 320, 290, size=16, weight=600)
    caption(d, "The dose stays in the chamber when the seal is tight.", 340)


@design("MED/asthma-attacks-4")
def _(d):
    labels = ["Breathe\nout", "Puff", "Slow breath\nin", "Wait one\nminute"]
    col = 608 / 4
    cw = col - 40
    for i, s in enumerate(labels):
        cx = 16 + col * (i + 0.5)
        d.badge(i + 1, cx, 70, 18)
        chip(d, cx, 140, cw, 66, s)
        if i < 3:
            d.arrow(cx + cw / 2 + 4, 140, cx + col - cw / 2 - 4, 140, width=3)
    x1 = 16 + col * 3.5
    x0 = 16 + col * 0.5
    loop_under(d, x1, x0, 176, 250)
    d.text("repeat", 320, 280, size=16, weight=600)
    caption(d, "The wait between puffs is about a minute.")


@design("MED/austere-medicine-priorities-1")
def _(d):
    labels = ["danger", "response", "airway", "breathing", "bleeding", "disability", "exposure"]
    for i, s in enumerate(labels):
        y = 36 + i * 46
        chip(d, 300, y, 220, 28, s, size=16)
        d.badge(i + 1, 150, y, 13)
        if i < 6:
            d.arrow(300, y + 15, 300, y + 31, width=2.5)
    d.curve_arrow("M412 312H500V36H416", (412, 36), math.pi, width=3)
    d.text("re-check", 560, 160, size=16, weight=600)


@design("MED/austere-medicine-priorities-2")
def _(d):
    d.piece("person-lying", 110, 20, 420)
    chip(d, 160, 110, 120, 34, "airway", size=15)
    d.leader(160, 127, 185, 232)
    chip(d, 320, 90, 120, 34, "chest", size=15)
    d.leader(320, 107, 300, 250)
    chip(d, 500, 110, 150, 34, "limb pressure", size=15)
    d.leader(500, 127, 490, 252)
    caption(d, "Check the most dangerous problem first.", 340)


@design("MED/basic-childbirth-care-1")
def _(d):
    chip(d, 90, 160, 110, 44, "baby", size=17)
    d.line(145, 160, 610, 160, width=6, color=SAND)
    d.piece("overhand-knot", 270, 125, 100)
    d.piece("overhand-knot", 400, 125, 100)
    d.text("tie one", 320, 230, size=16, weight=600)
    d.text("tie two", 450, 230, size=16, weight=600)
    d.arrow(150, 270, 260, 270, width=3)
    d.arrow(260, 270, 150, 270, width=3)
    d.text("away from the baby", 205, 300, size=15, weight=600)
    caption(d, "The cord is tied in two places.", 346)


@design("MED/basic-childbirth-care-2")
def _(d):
    steps(d, ["support\nmother", "support\nhead, no\npulling", "check\ncord", "support\nshoulders\nand body", "dry and\nwarm baby"], ["step-1", "step-2", "step-3", "step-box", "step-box"], y=50, pw=90, ch=80, size=15, caption_text="The order is fixed.")


@design("MED/basic-childbirth-care-3")
def _(d):
    d.line(40, 200, 600, 200, width=5, color=SAND)
    d.piece("overhand-knot", 200, 163, 100)
    d.piece("overhand-knot", 340, 163, 100)
    d.text("tie", 250, 170, size=17, weight=600)
    d.text("tie", 390, 170, size=17, weight=600)
    d.piece("knife", 275, 20, 130)
    d.arrow(320, 120, 320, 180, width=3)
    d.text("cut", 345, 150, size=17, weight=600, anchor="start")
    d.path("M255 235V245H385V235", width=3)
    d.text("a finger's width", 320, 300, size=15, weight=600)
    caption(d, "The cut always falls between the two ties.", 346)


@design("MED/basic-cpr-1")
def _(d):
    d.piece("person-lying", 110, 20, 420)
    chip(d, 290, 110, 150, 34, "hand position", size=15)
    d.leader(290, 127, 290, 252)
    d.arrow(560, 218, 560, 268, width=3)
    d.arrow(560, 268, 560, 218, width=3)
    d.text("about 5 cm", 560, 205, size=16, weight=600)
    caption(d, "Let the chest rise fully.", 340)


@design("MED/basic-cpr-2")
def _(d):
    chip(d, 170, 130, 200, 64, "30\ncompressions", size=17)
    chip(d, 470, 130, 200, 64, "2 breaths", size=17)
    d.arrow(276, 130, 364, 130, width=4)
    loop_under(d, 470, 170, 166, 240)
    d.text("repeat", 320, 270, size=16, weight=600)
    caption(d, "Repeat until help takes over.", 340)


@design("MED/basic-cpr-3")
def _(d):
    d.piece("person-lying", 110, 20, 420)
    chip(d, 200, 100, 190, 34, "below right collarbone", size=15)
    d.leader(200, 117, 250, 248)
    chip(d, 460, 100, 170, 34, "left below armpit", size=15)
    d.leader(460, 117, 330, 252)
    caption(d, "Pads go on bare skin.", 340)


@design("MED/basic-cpr-4")
def _(d):
    d.piece("person-lying", 90, 30, 400)
    d.piece("person-kneeling", 150, 60, 200)
    d.arrow(205, 105, 205, 200, width=4)
    d.text("body\nweight", 190, 150, size=16, weight=600, anchor="end")
    chip(d, 500, 90, 150, 34, "straight arms", size=15)
    d.leader(430, 98, 290, 130)
    caption(d, "Body weight does the work, not bent arms.", 340)


@design("MED/basic-first-aid-kit-1")
def _(d):
    d.piece("first-aid-kit", 20, 90, 190)
    d.arrow(215, 160, 255, 160, width=3)
    cells = ["dressings", "bandages", "gloves", "rehydration\nsalts", "medicines", "medical\nnote"]
    for i, s in enumerate(cells):
        x = 270 + (i % 3) * 120
        y = 90 + (i // 3) * 90
        chip(d, x + 56, y + 40, 112, 80, s, size=15)
    caption(d, "Grouped items let a helper find things quickly.", 320)


@design("MED/basic-first-aid-kit-2")
def _(d):
    cols = ["item", "quantity", "expiry date", "last checked"]
    cw, x0, y0, rh = 140, 40, 40, 50
    d.rect(x0, y0, cw * 4, rh, fill=INK, rx=8)
    for i, c in enumerate(cols):
        d.text(c, x0 + cw * (i + 0.5), y0 + 32, size=17, weight=700, fill="#ffffff")
    for r in range(1, 5):
        d.rect(x0, y0 + rh * r, cw * 4, rh, fill=CREAM if r % 2 else PAPER, rx=0)
    for i in range(1, 4):
        d.line(x0 + cw * i, y0, x0 + cw * i, y0 + rh * 5, width=2)
    caption(d, "Expiry tracked per item; replace used or expired stock.", 340)


@design("MED/basic-first-aid-kit-3")
def _(d):
    labels = ["inspect", "replace", "record"]
    ps = ["step-1", "step-2", "step-3"]
    xs = [120, 320, 520]
    for x, s, p in zip(xs, labels, ps):
        d.piece(p, x - 50, 40, 100)
        chip(d, x, 160, 130, 44, s, size=17)
    d.arrow(190, 160, 250, 160, width=3)
    d.arrow(390, 160, 450, 160, width=3)
    loop_under(d, 520, 120, 186, 250)
    chip(d, 320, 250, 190, 34, "every six months", size=15)
    caption(d, "Replace after every use, not only at the check.", 340)


@design("MED/basic-first-aid-kit-4")
def _(d):
    labels = ["hook by door", "kitchen shelf", "go-bag by exit"]
    xs = [120, 320, 520]
    for x, s in zip(xs, labels):
        d.piece("waypoint-pin", x - 60, 60, 120)
        chip(d, x, 200, 170, 40, s, size=16)
    caption(d, "One main kit place plus a grab-ready kit.", 300)


@design("MED/basic-first-aid-kit-5")
def _(d):
    items = [("gauze-pad", "gauze pad"), ("triangular-bandage", "triangular\nbandage"), ("bandage-roll", "roller bandage")]
    xs = [120, 320, 520]
    for x, (p, s) in zip(xs, items):
        d.piece(p, x - 85, 50, 170)
        chip(d, x, 220, 160, 56, s, size=16)
    caption(d, "Compare sizes to choose a dressing without reading packets.", 320)


@design("MED/burns-1")
def _(d):
    steps(d, ["Cool with\nrunning water", "Keep cooling\nfull period", "Cover\nloosely", "Record\ntime"], ["step-1", "step-2", "step-3", "step-box"], y=60, pw=110, ch=66)
    caption(d, "Keep cooling even after the pain eases.")


@design("MED/burns-2")
def _(d):
    ls = ["superficial", "partial thickness", "full thickness"]
    for i, s in enumerate(ls):
        y = 60 + i * 70
        d.rect(40, y, 260, 70, fill=CREAM, rx=0)
        d.text(s, 170, y + 42, size=17, weight=700)
    d.text("blisters mark\ndeeper burns", 345, 205, size=16, weight=600, anchor="start")
    d.leader(340, 197, 302, 165)
    d.text("white or charred\nskin: full depth", 345, 275, size=16, weight=600, anchor="start")
    d.leader(340, 267, 302, 235)


@design("MED/burns-3")
def _(d):
    d.piece("burn", 20, 20, 260)
    d.arrow(150, 190, 150, 245, width=4)
    d.piece("water-drop", 175, 190, 44)
    d.piece("bucket", 85, 235, 130)
    chip(d, 450, 190, 170, 34, "running water", size=16)
    d.leader(365, 190, 160, 205)
    chip(d, 450, 280, 170, 34, "catch basin", size=16)
    d.leader(365, 280, 200, 280)
    caption(d, "Cooling needs continuous flow, not one splash.", 346)


@design("MED/burns-4")
def _(d):
    steps(d, ["Lubricate\nwith soap", "Slide ring\noff gently", "Act while\nswelling\nis small"], ["step-1", "step-2", "step-3"], y=60, pw=120, ch=84)
    caption(d, "Remove the ring before it tightens.")


@design("MED/chest-pain-and-heart-attack-1")
def _(d):
    d.piece("heart", 30, 50, 250)
    d.text("heart muscle", 150, 275, size=16, weight=600)
    d.arrow(290, 140, 385, 140, width=4)
    d.text("blood flow", 335, 118, size=16, weight=600)
    chip(d, 440, 140, 90, 44, "clot", size=17)
    d.line(488, 140, 600, 140, dash="8 8", width=3)
    d.cross(545, 140, 16)
    caption(d, "A clot stops blood flow beyond it.", 340)


@design("MED/chest-pain-and-heart-attack-2")
def _(d):
    items = [("warning", "Chest pressure,\nbreathless or sweating"), ("phone-call", "Call emergency\nnow"), ("person-sitting", "Keep still\nand calm")]
    cx = [110, 320, 530]
    for x, (p, s) in zip(cx, items):
        d.piece(p, x - 70, 40, 140)
        d.text(s, x, 220, size=15, weight=600)
    d.arrow(190, 100, 250, 100, width=3)
    d.arrow(395, 100, 455, 100, width=3)
    caption(d, "The call comes before any other step.", 320)


@design("MED/choking-and-airway-obstruction-1")
def _(d):
    d.line(320, 30, 320, 320, dash="10 8", width=3)
    d.piece("person-standing", 80, 40, 180)
    d.text("adult", 170, 240, size=17, weight=700)
    d.text("abdominal thrusts", 170, 270, size=16, weight=600)
    d.piece("person-kneeling", 370, 40, 220)
    d.text("infant", 480, 240, size=17, weight=700)
    d.text("back blows", 480, 270, size=16, weight=600)


@design("MED/choking-and-airway-obstruction-2")
def _(d):
    d.piece("decision", 20, 100, 200)
    d.arrow(210, 170, 330, 90, width=3)
    d.arrow(210, 200, 330, 270, width=3)
    d.text("coughing and\nspeaking", 270, 70, size=15, weight=600, anchor="end")
    d.text("silent, unable\nto breathe", 270, 285, size=15, weight=600, anchor="end")
    d.piece("do", 340, 30, 80)
    chip(d, 520, 90, 170, 56, "encourage cough", size=16)
    d.piece("warning", 340, 215, 80)
    chip(d, 520, 270, 170, 56, "act now", size=16)
    caption(d, "A strong cough is always the first option.", 346)


@design("MED/choking-and-airway-obstruction-3")
def _(d):
    d.piece("person-standing", 150, 0, 340)
    d.tick(475, 100, 14)
    chip(d, 560, 100, 120, 34, "above navel", size=15)
    d.leader(540, 117, 330, 126)
    chip(d, 90, 80, 90, 34, "ribs", size=15)
    d.cross(160, 80, 14)
    d.leader(90, 97, 306, 100)
    caption(d, "The thrust point is above the navel.", 340)


@design("MED/choking-and-airway-obstruction-4")
def _(d):
    d.piece("person-standing", 250, 10, 240)
    d.piece("person-standing", 200, 10, 240)
    chip(d, 540, 70, 170, 34, "arms around waist", size=15)
    d.leader(540, 87, 380, 100)
    d.curve_arrow("M170 175Q250 185 282 105", (282, 105), -1.1, width=4)
    d.text("inward, then upward", 130, 215, size=16, weight=600, anchor="start")
    caption(d, "Inward and upward, never sideways.", 340)


@design("MED/choking-and-airway-obstruction-5")
def _(d):
    d.piece("infant", 150, 40, 340)
    chip(d, 320, 60, 180, 34, "two fingers", size=16)
    d.leader(320, 77, 330, 160)
    chip(d, 320, 300, 200, 34, "below nipple line", size=16)
    d.leader(320, 283, 320, 236)


@design("MED/chronic-medicines-without-a-pharmacy-1")
def _(d):
    d.piece("pills", 250, 5, 140)
    cols = ["name", "strength", "dose", "frequency", "prescriber"]
    cw, x0, y0, rh = 120, 20, 120, 50
    d.rect(x0, y0, cw * 5, rh, fill=INK, rx=8)
    for i, c in enumerate(cols):
        d.text(c, x0 + cw * (i + 0.5), y0 + 32, size=16, weight=700, fill="#ffffff")
    for r in range(1, 4):
        d.rect(x0, y0 + rh * r, cw * 5, rh, fill=CREAM if r % 2 else PAPER, rx=0)
    for i in range(1, 5):
        d.line(x0 + cw * i, y0, x0 + cw * i, y0 + rh * 4, width=2)
    caption(d, "Record each medicine once.", 340)


@design("MED/chronic-medicines-without-a-pharmacy-2")
def _(d):
    x0, y0, cw, rh = 90, 70, 56, 52
    for r in range(2):
        d.text(f"week {r + 1}", x0 - 12, y0 + rh * r + 33, size=16, weight=600, anchor="end")
        for c in range(7):
            d.rect(x0 + cw * c, y0 + rh * r, cw, rh, fill=CREAM, rx=0, width=2)
    d.path(f"M{x0 + cw * 7 + 12} {y0}Q{x0 + cw * 7 + 24} {y0} {x0 + cw * 7 + 24} {y0 + 12}V{y0 + 92}Q{x0 + cw * 7 + 24} {y0 + 104} {x0 + cw * 7 + 12} {y0 + 104}", width=3)
    d.text("two weeks\nspare stock", x0 + cw * 7 + 34, y0 + 48, size=15, weight=600, anchor="start")
    d.line(x0, 210, x0 + cw * 7, 210, dash="10 8", width=3, color=RED)
    chip(d, 320, 255, 200, 40, "request refill here", size=16)
    d.leader(320, 235, 320, 212)
    caption(d, "Refill when stock drops below two weeks.", 340)


@design("MED/chronic-medicines-without-a-pharmacy-3")
def _(d):
    d.rect(30, 50, 400, 250, fill=CREAM, rx=16)
    fields = ["name", "strength", "dose", "time of day", "prescriber", "nearest clinic"]
    for i, s in enumerate(fields):
        y = 70 + i * 38
        d.text(s, 56, y + 24, size=16, weight=600, anchor="start")
        d.line(190, y + 28, 410, y + 28, width=2, color=SAND)
    d.piece("pills", 450, 100, 170)
    caption(d, "One card per medicine, kept beside the supply.", 340)


@design("MED/chronic-medicines-without-a-pharmacy-4")
def _(d):
    d.arrow(60, 250, 600, 250, width=3)
    d.text("days", 600, 275, size=16, weight=600, anchor="end")
    d.line(60, 190, 400, 190, width=14, color=BLUE)
    d.text("days left", 150, 168, size=16, weight=600)
    d.line(250, 130, 250, 250, dash="8 8", width=3, color=RED)
    chip(d, 250, 100, 140, 34, "two-week line", size=15)
    chip(d, 500, 130, 130, 34, "request refill", size=15)
    d.leader(470, 147, 256, 184)
    d.piece("pills", 480, 175, 90)


@design("MED/chronic-medicines-without-a-pharmacy-5")
def _(d):
    items = ["ice-cube", "bottle", "thermometer"]
    labels = ["ice packs", "medicine", "thermometer"]
    xs = [140, 260, 380]
    for x, p, s in zip(xs, items, labels):
        d.piece(p, x - 50, 30, 100)
        d.text(s, x, 125, size=15, weight=600)
        d.arrow(x, 135, x, 160, width=3)
    d.piece("cool-box", 70, 150, 220)
    chip(d, 480, 250, 170, 34, "insulated walls", size=15)
    d.leader(395, 250, 268, 275)
    caption(d, "Refrigerated medicines stay cool when power fails.", 340)


@design("MED/cleaning-and-dressing-wounds-1")
def _(d):
    steps(d, ["Rinse", "Remove\ndebris", "Stroke\noutward", "Dress"], ["step-1", "step-2", "step-3", "step-box"], y=60, pw=110, ch=60)
    caption(d, "Clean first, before any dressing goes on.")


@design("MED/cleaning-and-dressing-wounds-2")
def _(d):
    d.piece("bleeding", 150, 90, 300)
    d.piece("water-drop", 280, 10, 50)
    d.arrow(305, 68, 305, 118, width=3)
    d.arrow(298, 140, 210, 140, width=3)
    d.arrow(312, 140, 400, 140, width=3)
    chip(d, 500, 40, 150, 34, "clean water", size=15)
    d.leader(425, 42, 325, 42)
    d.piece("bowl", 460, 190, 130)
    chip(d, 525, 305, 120, 30, "catch dish", size=15)
    d.arrow(440, 215, 470, 240, width=3)
    caption(d, "The flow carries dirt away, not deeper.", 346)


@design("MED/cleaning-and-dressing-wounds-3")
def _(d):
    d.piece("bleeding", 170, 55, 300)
    for y in (45, 85):
        d.arrow(300, y, 190, y, width=3)
        d.arrow(340, y, 450, y, width=3)
    chip(d, 320, 290, 240, 34, "fresh stroke each pass", size=15)
    caption(d, "Never drag dirt back toward the cut.", 346)


@design("MED/cleaning-and-dressing-wounds-4")
def _(d):
    ls = ["tape", "rolled bandage", "gauze", "non-stick pad"]
    for i, s in enumerate(ls):
        chip(d, 300, 50 + i * 60, 220, 46, s, size=16)
    d.path("M170 28Q150 28 150 48V220Q150 240 170 240", width=3)
    d.text("outer layers\nonly hold it", 40, 100, size=15, weight=600, anchor="start")
    d.text("touches\nthe wound", 480, 230, size=15, weight=600, anchor="start")
    d.leader(475, 224, 412, 230)


@design("MED/cleaning-and-dressing-wounds-5")
def _(d):
    d.arrow(60, 210, 610, 210, width=3)
    for i, x in enumerate([150, 320, 490]):
        d.line(x, 200, x, 220, width=3)
        d.text(f"day {i + 1}", x, 240, size=16, weight=600)
    d.line(150, 150, 600, 150, width=10, color=GREEN)
    d.text("normal healing", 380, 130, size=16, weight=600, fill=GREEN)
    d.line(150, 290, 600, 290, width=8, color=RED, dash="12 8")
    d.piece("warning", 60, 250, 70)
    d.text("redness, swelling, pus, red streaks", 150, 322, size=15, weight=600, anchor="start", fill=RED)
