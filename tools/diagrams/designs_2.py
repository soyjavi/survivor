from dg import *

DESIGNS = {}


def design(key):
    def wrap(fn):
        DESIGNS[key] = fn
        return fn
    return wrap


def caption(d, s, y=340):
    d.text(s, 320, y, size=15, fill="#4a4238")


def chip(d, cx, cy, w, h, s, size=16, fill=CREAM, weight=600):
    d.rect(cx - w / 2, cy - h / 2, w, h, fill=fill, rx=12)
    lines = s.split("\n")
    y0 = cy + size * 0.35 - (len(lines) - 1) * size * 0.6
    d.text(s, cx, y0, size=size, weight=weight)


@design("FOD/bread-without-an-oven-1")
def _(d):
    d.piece("coals", 250, 0, 140)
    d.arrow(320, 100, 320, 128, color=RED, width=5)
    d.piece("pot-with-lid", 235, 100, 170)
    d.arrow(250, 262, 250, 236, color=RED, width=5)
    d.piece("coals", 250, 196, 140)
    d.leader(450, 52, 380, 52)
    d.text("Coals on the lid", 460, 58, size=17, weight=600, anchor="start")
    d.leader(450, 170, 372, 170)
    d.text("Dough inside", 460, 176, size=17, weight=600, anchor="start")
    d.leader(450, 270, 385, 270)
    d.text("Coals below", 460, 276, size=17, weight=600, anchor="start")
    caption(d, "Heat arrives from both sides, so the pot acts as an oven.", 346)


@design("FOD/bread-without-an-oven-2")
def _(d):
    d.piece("pot-with-lid", 170, 36, 300)
    d.text("Crust sets first\n(top and base)", 160, 100, size=17, weight=600, anchor="end")
    d.leader(170, 98, 260, 140)
    d.text("Centre sets last", 490, 200, size=17, weight=600, anchor="start")
    d.leader(484, 196, 362, 196)
    caption(d, "Colour alone does not show doneness.", 330)


@design("FOD/bread-without-an-oven-3")
def _(d):
    items = [("pot-with-lid", "Loaf placed"), ("coals", "Coals set"), ("hand", "Tap the base")]
    for i, (piece, label) in enumerate(items):
        x = 45 + i * 200
        d.piece(piece, x, 40, 150, 112)
        d.badge(i + 1, x + 12, 56, 15)
        d.text(label, x + 75, 190, size=17, weight=600)
        if i < 2:
            d.arrow(x + 156, 96, x + 196, 96)
    d.rect(60, 236, 520, 62, fill=CREAM)
    d.text("A hollow sound at the base, not colour,\nmarks a finished loaf.", 320, 262, size=16)


@design("FOD/bread-without-an-oven-4")
def _(d):
    chip(d, 100, 110, 150, 70, "Fresh\nloaf", size=18)
    d.arrow(184, 110, 240, 110)
    d.piece("grate", 250, 50, 140)
    d.text("Toasted dry", 320, 180, size=17, weight=600)
    d.arrow(400, 110, 456, 110)
    d.piece("cloth", 465, 50, 150)
    d.text("Cloth bag", 540, 180, size=17, weight=600)
    caption(d, "Drying the slices is what slows mould.", 280)


@design("MED/allergies-and-anaphylaxis-1")
def _(d):
    d.piece("person-standing", 30, 40, 180)
    d.leader(236, 126, 144, 126)
    d.text("Outer thigh", 246, 132, size=17, weight=600, anchor="start")
    d.text("Auto-injector", 470, 56, size=20, weight=700)
    for i, s in enumerate(["Cap off", "Press on the outer thigh", "Hold in place for\nthe printed time"]):
        y = 110 + i * 68
        d.badge(i + 1, 400, y, 18)
        d.text(s, 430, y + 6, size=17, weight=600, anchor="start")
    caption(d, "Press and hold; a quick tap is not enough.", 330)


@design("MED/allergies-and-anaphylaxis-2")
def _(d):
    d.rect(40, 24, 560, 40, fill=INK, rx=8)
    d.text("System", 130, 50, size=17, weight=700, fill="#ffffff")
    d.text("Example sign", 400, 50, size=17, weight=700, fill="#ffffff")
    rows = [("Skin", "Hives, itching, swelling"), ("Airway", "Swollen tongue or throat"), ("Breathing", "Wheeze, short of breath"), ("Circulation", "Faint, pale, fast pulse"), ("Digestion", "Vomiting, cramps")]
    for i, (a, b) in enumerate(rows):
        y = 64 + i * 46
        d.rect(40, y, 560, 46, fill=CREAM if i % 2 == 0 else PAPER, rx=0, width=2)
        d.text(a, 60, y + 29, size=17, weight=600, anchor="start")
        d.text(b, 240, y + 29, size=17, anchor="start")
        d.tick(570, y + 23, 11)
    caption(d, "Signs in several systems together mean anaphylaxis.", 330)


@design("MED/allergies-and-anaphylaxis-3")
def _(d):
    labels = ["Recognise\nsigns", "Use the\nauto-injector", "Call emergency\nhelp"]
    for i, label in enumerate(labels):
        cx = 110 + i * 210
        d.badge(i + 1, cx, 50, 26)
        d.text(label, cx, 108, size=16, weight=600)
        if i < 2:
            d.arrow(cx + 34, 50, cx + 176, 50)
    d.piece("person-sitting", 60, 160, 150)
    d.text("Lay flat or sit up", 135, 300, size=16, weight=600)
    d.arrow(230, 230, 330, 230)
    d.piece("timeline-marker", 345, 170, 130)
    d.text("Repeat after\n5 to 15 minutes", 410, 300, size=16, weight=600)
    caption(d, "The device comes first.", 346)


@design("COM/amateur-radio-basics-1")
def _(d):
    d.piece("radio", 250, 90, 140)
    for cx, cy, n, label, ly in [(110, 90, 1, "Listen", 40), (530, 90, 2, "Transmit", 40), (320, 270, 3, "Listen again", 326)]:
        d.badge(n, cx, cy, 26)
        d.text(label, cx, ly, size=17, weight=600)
    d.arrow(146, 90, 492, 90)
    d.arrow(512, 116, 350, 248)
    d.arrow(290, 250, 130, 120)


@design("COM/amateur-radio-basics-2")
def _(d):
    d.piece("tower", 250, 14, 140)
    d.piece("do-not", 285, 30, 70)
    d.text("Broken tower: no direct path", 320, 138, size=16, weight=600)
    items = [("person-standing", "Home station"), ("radio", "Local relay"), ("radio", "Distant station")]
    for i, (piece, label) in enumerate(items):
        x = 45 + i * 200
        d.piece(piece, x, 180, 150, 112)
        d.text(label, x + 75, 320, size=17, weight=600)
        if i < 2:
            d.arrow(x + 156, 236, x + 196, 236)
    caption(d, "The message arrives only through the relay.", 350)


@design("COM/amateur-radio-basics-3")
def _(d):
    d.rect(20, 20, 290, 300, fill=PAPER, rx=14, width=2)
    d.rect(330, 20, 290, 300, fill=PAPER, rx=14, width=2)
    d.piece("person-standing", 30, 100, 130)
    d.piece("radio", 120, 190, 80)
    d.piece("rock", 205, 160, 90)
    d.arrow(190, 222, 236, 222, color=BLUE)
    d.piece("do-not", 213, 150, 44)
    d.text("Hill", 250, 270, size=15, weight=600)
    d.text("Low antenna", 165, 296, size=17, weight=600)
    d.piece("person-standing", 340, 100, 130)
    d.piece("antenna", 440, 80, 120)
    d.piece("rock", 520, 160, 90)
    d.curve_arrow("M505 120C540 60 590 60 604 130", (604, 130), 1.2, color=BLUE)
    d.text("Hill", 565, 270, size=15, weight=600)
    d.text("High antenna", 475, 296, size=17, weight=600)
    caption(d, "Height extends range; a hill can block it.", 346)


@design("COM/amateur-radio-basics-4")
def _(d):
    def box(cx, cy, w, h, s):
        d.rect(cx - w / 2, cy - h / 2, w, h, fill=CREAM, rx=h / 2 if s == "Listen" else 12)
        d.text(s, cx, cy + 6, size=17, weight=600)
    box(95, 100, 110, 56, "Listen")
    d.path("M270 52L340 100L270 148L200 100Z", fill=CREAM)
    d.text("Gap found?", 270, 106, size=16, weight=600)
    box(435, 100, 110, 56, "Transmit")
    box(570, 100, 100, 56, "Confirm")
    d.arrow(150, 100, 198, 100)
    d.arrow(342, 100, 378, 100)
    d.text("Yes", 360, 88, size=14, weight=600)
    d.arrow(490, 100, 518, 100)
    d.path("M270 148V230H95", stroke=INK, width=4)
    d.arrow(95, 230, 95, 130)
    d.text("No: keep listening", 180, 252, size=15, weight=600)
    d.path("M570 128V300H30V100", stroke=INK, width=4)
    d.arrow(30, 100, 38, 100)
    d.text("Repeat for the next call", 300, 322, size=15, weight=600)


@design("COM/amateur-radio-basics-5")
def _(d):
    d.rect(80, 20, 480, 300, fill=CREAM, rx=14)
    d.rect(80, 20, 480, 54, fill=INK, rx=14)
    d.text("Call sign", 110, 54, size=19, weight=700, fill="#ffffff", anchor="start")
    d.line(240, 58, 530, 58, color="#ffffff", width=2)
    for i, label in enumerate(["Time", "Message", "Confirmation"]):
        y = 90 + i * 70
        d.text(label, 110, y + 36, size=19, weight=600, anchor="start")
        d.line(240, y + 42, 530, y + 42, color=SAND, width=3)
    d.tick(500, 270, 20)
    caption(d, "The message is complete only when the confirmation row is filled.", 346)


@design("PWR/energy-budgeting-1")
def _(d):
    cols = [(60, "Device"), (220, "Watts"), (340, "Hours"), (470, "Watt-hours")]
    d.rect(40, 16, 560, 40, fill=INK, rx=8)
    for x, s in cols:
        d.text(s, x, 42, size=17, weight=700, fill="#ffffff", anchor="start")
    rows = [("Radio", "5 W", "4 h", "20 Wh"), ("Light", "3 W", "5 h", "15 Wh"), ("Charger", "10 W", "2 h", "20 Wh")]
    for i, row in enumerate(rows):
        y = 56 + i * 48
        d.rect(40, y, 560, 48, fill=CREAM if i % 2 == 0 else PAPER, rx=0, width=2)
        for (x, _), s in zip(cols, row):
            d.text(s, x, y + 31, size=17, anchor="start")
    d.arrow(520, 204, 520, 252, width=4)
    d.rect(40, 256, 560, 52, fill=YELLOW, rx=10)
    d.text("Daily total", 60, 289, size=19, weight=700, anchor="start")
    d.text("55 Wh", 470, 289, size=19, weight=700, anchor="start")
    caption(d, "Each row is one multiplication; the total is their sum.", 340)


@design("PWR/energy-budgeting-2")
def _(d):
    d.piece("battery", 10, 100, 130)
    d.arrow(140, 150, 180, 150)
    stages = [(250, "5 days", "theoretical"), (400, "4 days", "after losses"), (550, "3.3 days", "with margin\non the need")]
    for i, (cx, big, small) in enumerate(stages):
        chip(d, cx, 150, 120, 80, big, size=24, fill=CREAM if i < 2 else YELLOW, weight=700)
        d.text(small, cx, 222, size=16, weight=600)
        if i < 2:
            d.arrow(cx + 64, 150, cx + 86, 150)
    caption(d, "A margin on the need cuts the result further.", 330)


@design("PWR/energy-budgeting-3")
def _(d):
    d.piece("ladder", 20, 40, 190, 240)
    rows = [("Medical devices", GREEN), ("Communication", BLUE), ("Lighting for safety", YELLOW), ("Anything else", RED)]
    for i, (label, color) in enumerate(rows):
        y = 24 + i * 74
        d.rect(240, y, 300, 58, fill=color, rx=12)
        d.text(label, 390, y + 37, size=19, weight=700, fill="#ffffff" if color != YELLOW else INK)
    d.arrow(580, 36, 580, 280, width=5)
    d.text("Cut from\nthe bottom", 580, 306, size=14, weight=600)
    caption(d, "The bottom rung is cut first.", 346)

