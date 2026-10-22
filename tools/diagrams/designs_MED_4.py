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


def chain(d, labels, y, w, h=48, gap=None, size=16):
    n = len(labels)
    gap = gap if gap is not None else (608 - n * w) / (n - 1)
    x0 = (640 - (n * w + (n - 1) * gap)) / 2
    for i, s in enumerate(labels):
        cx = x0 + i * (w + gap) + w / 2
        chip(d, cx, y, w, h, s, size=size)
        if i < n - 1:
            d.arrow(cx + w / 2 + 3, y, cx + w / 2 + gap - 3, y, width=3)


P = "MED/"


@design(P + "toothache-and-dental-pain-1")
def _(d):
    d.piece("bowl", 20, 100, 150)
    d.piece("water-drop", 70, 60, 50)
    d.text("Warm rinse", 95, 250, size=17, weight=600)
    d.piece("person-sitting", 225, 50, 190)
    d.piece("ice-pack", 480, 100, 140)
    d.text("Cold pack\noutside cheek", 550, 250, size=17, weight=600)
    d.leader(485, 135, 309, 88)
    caption(d, "The cold pack stays outside the mouth.")


@design(P + "toothache-and-dental-pain-2")
def _(d):
    chain(d, ["Sip", "Swish gently", "Spit"], 130, 150, h=56, gap=70)
    d.path("M480 160 C 480 250 160 250 160 162", stroke=INK, width=4)
    d.arrow(160, 190, 160, 160, width=4)
    d.text("Repeat", 320, 240, size=17, weight=600)
    chip(d, 320, 300, 300, 40, "Never swallow the salt water", size=16, color=RED)


@design(P + "toothache-and-dental-pain-3")
def _(d):
    d.piece("tooth", 60, 60, 200)
    d.piece("wax", 330, 40, 110)
    d.arrow(385, 150, 235, 130, width=3)
    d.text("Wax on chipped edge", 385, 190, size=17, weight=600)
    chip(d, 500, 255, 190, 44, "Tongue area", size=16)
    d.piece("do-not", 590, 232, 40)
    d.text("Keep the tongue away", 320, 330, size=16, weight=600)


@design(P + "toothache-and-dental-pain-4")
def _(d):
    d.piece("person-sitting", 60, 50, 200)
    d.arrow(150, 112, 440, 112, color=RED, width=5)
    d.leader(80, 76, 128, 99)
    d.text("Jaw", 62, 72, size=16, weight=600)
    d.text("Spread to neck", 300, 150, size=17, weight=600)
    d.piece("warning", 500, 190, 90)
    d.text("Spread beyond\nthe tooth: urgent care", 400, 255, size=16, weight=600)


@design(P + "treating-common-illness-without-a-clinic-1")
def _(d):
    d.piece("cup", 30, 70, 150)
    d.text("Fluids", 105, 210, size=17, weight=600)
    d.piece("thermometer", 245, 70, 150)
    d.text("Temperature", 320, 210, size=17, weight=600)
    d.piece("notebook", 460, 70, 150)
    d.text("Notebook", 535, 210, size=17, weight=600)
    caption(d, "The three things tracked during home care.")


@design(P + "treating-common-illness-without-a-clinic-2")
def _(d):
    d.piece("decision", 20, 110, 160)
    d.text("Red flag?", 100, 250, size=16, weight=700)
    d.arrow(180, 160, 330, 90, width=4)
    d.arrow(180, 175, 330, 260, width=4, color=RED)
    d.piece("do", 340, 40, 100)
    d.text("Mild and improving:\nhome care", 455, 80, size=15, weight=600, anchor="start")
    d.piece("warning", 340, 210, 100)
    d.text("Breathing trouble,\nconfusion: urgent help", 455, 250, size=15, weight=600, anchor="start")


@design(P + "urinary-problems-and-hydration-1")
def _(d):
    chain(d, ["Kidneys", "Ureters", "Bladder", "Urethra"], 150, 120, h=56, gap=44, size=17)
    d.text("The path urine takes", 320, 250, size=18, weight=600)
    caption(d, "Kidneys are the starting point.")


@design(P + "urinary-problems-and-hydration-2")
def _(d):
    d.piece("decision", 20, 110, 160)
    d.text("Which symptoms?", 100, 250, size=16, weight=700)
    d.arrow(180, 160, 330, 90, width=4)
    d.arrow(180, 175, 330, 260, width=4, color=RED)
    d.piece("do", 340, 40, 100)
    d.text("Burning urination,\nfluids tolerated:\nhome care", 460, 70, size=16, weight=600, anchor="start")
    d.piece("warning", 340, 210, 100)
    d.text("Fever, back pain,\nvomiting: urgent care", 460, 250, size=16, weight=600, anchor="start")


@design(P + "waterborne-illness-1")
def _(d):
    d.piece("pool", 20, 110, 170)
    d.text("Water", 105, 250, size=17, weight=600)
    d.arrow(195, 150, 330, 60, width=4)
    d.arrow(195, 170, 330, 170, width=4)
    d.arrow(195, 190, 330, 280, width=4)
    d.piece("hands", 340, 20, 110)
    d.text("Hands", 480, 85, size=17, weight=600, anchor="start")
    chip(d, 395, 170, 110, 50, "Food")
    d.piece("person-standing", 350, 235, 90)
    d.text("Other people", 480, 300, size=17, weight=600, anchor="start")


@design(P + "waterborne-illness-2")
def _(d):
    d.piece("pot-with-lid", 20, 70, 130)
    d.text("Boil", 85, 195, size=17, weight=600)
    chip(d, 225, 130, 76, 44, "Cool")
    d.piece("jar", 300, 70, 130)
    d.text("Store covered", 365, 195, size=16, weight=600)
    d.piece("cup", 490, 70, 120)
    d.text("Clean cup", 550, 195, size=16, weight=600)
    d.arrow(152, 130, 183, 130, width=3)
    d.arrow(267, 130, 296, 130, width=3)
    d.arrow(432, 130, 488, 130, width=3)
    caption(d, "Storage is part of the safe-water chain.")


@design(P + "waterborne-illness-3")
def _(d):
    chain(d, ["Wet", "Soap", "Scrub", "Rinse", "Dry"], 150, 98, h=56, gap=28, size=17)
    d.piece("water-drop", 52, 205, 60)
    d.piece("soap", 153, 200, 110)
    d.piece("hands", 279, 200, 110)
    d.piece("water-drop", 430, 205, 60)
    caption(d, "Fixed order, none skipped.")


@design(P + "waterborne-illness-4")
def _(d):
    d.piece("jar", 30, 90, 150)
    d.text("Covered container", 105, 230, size=16, weight=600)
    d.piece("cup", 200, 110, 100)
    d.text("Clean cup", 250, 230, size=16, weight=600)
    d.piece("toilet-seat", 500, 90, 120)
    d.text("Toilet", 560, 230, size=16, weight=600)
    d.line(305, 160, 495, 160, dash="9 7", width=4)
    d.text("Away from toilet", 400, 140, size=16, weight=600)


@design(P + "waterborne-illness-5")
def _(d):
    d.piece("pot-with-lid", 30, 80, 160)
    d.piece("waves", 70, 40, 80)
    d.text("Rolling boil", 110, 230, size=17, weight=600)
    d.arrow(200, 150, 400, 150, width=4)
    d.piece("bowl", 430, 80, 160)
    d.text("Cool, covered", 510, 230, size=17, weight=600)
    caption(d, "Boil first, covered storage after.")


@design(P + "when-to-seek-professional-care-1")
def _(d):
    d.piece("phone-call", 40, 40, 110)
    chip(d, 95, 200, 160, 70, "Call emergency\nnow", color=RED)
    d.piece("warning", 265, 40, 110)
    chip(d, 320, 200, 160, 70, "Seek care\nsoon")
    d.piece("notebook", 490, 40, 110)
    chip(d, 545, 200, 160, 70, "Monitor\nat home")
    d.arrow(95, 280, 545, 280, width=3)
    d.text("Immediate", 95, 310, size=15)
    d.text("Watchful", 545, 310, size=15)


@design(P + "when-to-seek-professional-care-2")
def _(d):
    d.text("Red flags", 320, 50, size=20, weight=700)
    d.rect(120, 70, 400, 220, fill=CREAM)
    for i in range(4):
        y = 70 + i * 55
        if i:
            d.line(120, y, 520, y, width=2)
        d.piece("warning", 140, y + 6, 56)
        d.rect(440, y + 12, 30, 30, fill=PAPER, rx=4)
        d.tick(455, y + 27, 12)
    d.line(420, 70, 420, 290, width=2)
    caption(d, "Each red flag is checked separately.")


@design(P + "when-to-seek-professional-care-3")
def _(d):
    labels = ["Breathing and\nalertness?", "Red flags\npresent?", "Worsening\nover hours?"]
    for i, s in enumerate(labels):
        x = 20 + i * 205
        d.piece("decision", x, 100, 150)
        d.text(s, x + 75, 62, size=16, weight=700)
        if i < 2:
            d.arrow(x + 150, 160, x + 200, 160, width=3)
        d.arrow(x + 75, 216, x + 75, 262, width=3, color=RED)
        chip(d, x + 75, 285, 150, 40, "Own outcome", size=15)
    caption(d, "Questions run in order.", 346)


@design(P + "when-to-seek-professional-care-4")
def _(d):
    d.piece("phone-call", 50, 70, 190)
    d.text("Emergency number", 145, 240, size=17, weight=600)
    d.piece("note", 400, 70, 190)
    d.text("Red flag list", 495, 240, size=17, weight=600)
    d.line(250, 140, 390, 140, dash="9 7", width=4)
    caption(d, "Kept together.")


@design(P + "when-to-seek-professional-care-5")
def _(d):
    cols = ["Time", "Breathing", "Alertness", "Pulse", "Colour", "Treatment"]
    w = 600 / 6
    d.rect(20, 50, 600, 230, fill=CREAM)
    d.rect(20, 50, 600, 46, fill=SAND)
    for i, s in enumerate(cols):
        d.text(s, 20 + i * w + w / 2, 80, size=15, weight=700)
        if i:
            d.line(20 + i * w, 50, 20 + i * w, 280, width=2)
    for r in range(1, 5):
        d.line(20, 50 + 46 * r + (r - 1) * 0, 620, 50 + 46 * r, width=2)
    caption(d, "Recorded so the next helper sees the trend.")


@design(P + "wilderness-medical-kit-1")
def _(d):
    d.piece("first-aid-kit", 20, 60, 180)
    items = [("gloves", "Gloves"), ("gauze-pad", "Gauze"), ("tape", "Tape"), ("tweezers", "Tweezers"), ("blanket", "Blanket"), ("thermometer", "Thermometer")]
    for i, (p, s) in enumerate(items):
        c, r = i % 3, i // 3
        x, y = 250 + c * 125, 50 + r * 150
        d.piece(p, x, y, 100)
        d.text(s, x + 50, y + 100, size=16, weight=600)
    caption(d, "Rows let items be found quickly.")


@design(P + "wilderness-medical-kit-2")
def _(d):
    d.piece("first-aid-kit", 20, 90, 170)
    items = [("adhesive-plaster", "Wounds"), ("pills", "Medicines"), ("knife", "Tools"), ("note", "Paperwork")]
    for i, (p, s) in enumerate(items):
        y = 25 + i * 78
        d.arrow(200, 180, 305, y + 33, width=3)
        d.rect(310, y, 300, 66, fill=CREAM)
        d.piece(p, 318, y + 4, 70)
        d.text(s, 410, y + 40, size=17, weight=600, anchor="start")


@design(P + "wound-closure-without-a-surgeon-1")
def _(d):
    d.piece("bleeding", 20, 80, 220)
    for x in [290, 365, 510]:
        d.piece("adhesive-plaster", x, 100, 90)
    d.text("Strips", 377, 190, size=16, weight=600)
    d.leader(487, 255, 487, 142)
    d.text("Drainage gap stays open", 487, 280, size=16, weight=600)


@design(P + "wound-closure-without-a-surgeon-2")
def _(d):
    d.piece("decision", 20, 110, 160)
    d.text("Wound condition?", 100, 250, size=16, weight=700)
    d.arrow(180, 160, 330, 90, width=4)
    d.arrow(180, 175, 330, 260, width=4, color=RED)
    d.piece("do", 340, 40, 100)
    d.text("Clean and fresh:\nclose it", 470, 80, size=16, weight=600, anchor="start")
    d.piece("do-not", 340, 210, 100)
    d.text("Dirty, old or over\na joint: leave open,\ndress it", 470, 245, size=16, weight=600, anchor="start")
