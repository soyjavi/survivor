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


def grid_steps(d, labels, cols, y0=60, cw=170, ch=70, gapx=40, gapy=60, numbered=True):
    n = len(labels)
    rows = (n + cols - 1) // cols
    total = cols * cw + (cols - 1) * gapx
    x0 = (640 - total) / 2
    pos = []
    for i, s in enumerate(labels):
        r, c = divmod(i, cols)
        cx = x0 + c * (cw + gapx) + cw / 2
        cy = y0 + r * (ch + gapy) + ch / 2
        pos.append((cx, cy))
        chip(d, cx, cy, cw, ch, s)
        if numbered:
            d.badge(i + 1, cx - cw / 2 + 6, cy - ch / 2 + 6, r=16)
    for i in range(n - 1):
        (ax, ay), (bx, by) = pos[i], pos[i + 1]
        if ay == by:
            d.arrow(ax + cw / 2 + 3, ay, bx - cw / 2 - 3, by)
        else:
            mid = ay + ch / 2 + gapy / 2
            d.line(ax, ay + ch / 2 + 3, ax, mid)
            d.line(ax, mid, bx, mid)
            d.arrow(bx, mid, bx, by - ch / 2 - 3)
    return pos


def loop(d, labels, cx=320, cy=170, rx=200, ry=100, cw=150, ch=56):
    import math
    n = len(labels)
    pts = []
    for i in range(n):
        a = -math.pi / 2 + i * 2 * math.pi / n
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    for i, s in enumerate(labels):
        chip(d, pts[i][0], pts[i][1], cw, ch, s)
    for i in range(n):
        ax, ay = pts[i]
        bx, by = pts[(i + 1) % n]
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        def edge(px, py, sgn):
            t = min((cw / 2 + 6) / abs(ux) if ux else 1e9, (ch / 2 + 6) / abs(uy) if uy else 1e9)
            return px + sgn * ux * t, py + sgn * uy * t
        sx, sy = edge(ax, ay, 1)
        ex, ey = edge(bx, by, -1)
        d.arrow(sx, sy, ex, ey)
    return pts


def timeline(d, labels, y=180, x0=70, x1=570, sub=None):
    d.arrow(x0 - 30, y, x1 + 40, y, width=4)
    n = len(labels)
    for i, s in enumerate(labels):
        x = x0 + (x1 - x0) * (i + 0.5) / n
        d.circle(x, y, 10, fill=YELLOW)
        d.text(s, x, y + 44, size=16, weight=600)
    return [x0 + (x1 - x0) * (i + 0.5) / n for i in range(n)]


@design("HYG/caring-for-pets-in-a-crisis-1")
def _(d):
    zones = [("bag", "Food store"), ("bucket", "Water station"), ("bucket", "Waste bucket"), ("note", "ID and records")]
    w = 120
    gap = (640 - 4 * w) / 5
    d.rect(16, 50, 608, 200, fill=PAPER, rx=12)
    for i, (p, s) in enumerate(zones):
        x = gap + i * (w + gap)
        if i:
            d.line(x - gap / 2, 50, x - gap / 2, 250, width=3)
        d.piece(p, x, 90, w)
        d.text(s, x + w / 2, 225, size=16, weight=600)
    caption(d, "Each zone is set up before a crisis.", 300)


@design("HYG/caring-for-pets-in-a-crisis-2")
def _(d):
    d.piece("bowl", 40, 90, 190)
    d.piece("bowl", 410, 90, 190)
    d.piece("do-not", 275, 120, 90)
    d.text("Animals", 135, 270, size=17, weight=600)
    d.text("People", 505, 270, size=17, weight=600)
    caption(d, "Never share a bowl or container.", 330)


@design("HYG/caring-for-pets-in-a-crisis-3")
def _(d):
    pts = loop(d, ["Hunger", "Scavenging", "Illness and bites"], cx=320, cy=170, rx=210, ry=95, cw=170)
    d.piece("tip", 440, 24, 60)
    d.text("Feed regularly", 502, 58, size=15, weight=600, anchor="start")
    caption(d, "Regular feeding breaks the loop.", 340)


@design("HYG/cleaning-the-house-after-a-flood-1")
def _(d):
    grid_steps(d, ["Safety check", "Remove water\nand mud", "Remove ruined\nitems", "Scrub", "Disinfect,\nthen rinse", "Dry"], 3, y0=50, ch=76, gapy=50)
    caption(d, "Disinfect only a clean room; drying is last.")


@design("HYG/cleaning-the-house-after-a-flood-2")
def _(d):
    d.piece("door", 20, 70, 170)
    d.piece("window", 450, 70, 170)
    d.arrow(200, 140, 440, 140, width=5, color=BLUE)
    d.text("Airflow", 320, 120, size=17, weight=600, fill=BLUE)
    d.text("Open door", 105, 250, size=17, weight=600)
    d.text("Open window", 535, 250, size=17, weight=600)
    caption(d, "Cross-airflow dries the walls and keeps mould away.", 320)


@design("HYG/cleaning-the-house-after-a-flood-3")
def _(d):
    d.piece("wall-cavity", 200, 115, 240)
    d.line(16, 276, 624, 276, width=4)
    d.line(150, 250, 490, 250, dash="9 7", color=BLUE)
    for x in (262, 300, 338):
        d.arrow(x, 78, x, 124, color=BLUE, width=3)
    d.text("Waterline", 140, 256, size=16, weight=600, anchor="end")
    d.leader(130, 190, 246, 180)
    d.text("Damp plaster", 120, 196, size=16, weight=600, anchor="end")
    d.leader(500, 200, 340, 200)
    d.text("Hidden cavity", 510, 206, size=16, weight=600, anchor="start")
    caption(d, "Drying must reach inside.", 336)


@design("HYG/cleaning-the-house-after-a-flood-4")
def _(d):
    grid_steps(d, ["Safety", "Remove water", "Throw away\nruined items", "Scrub", "Disinfect", "Dry"], 3, y0=50, ch=76, gapy=50)
    caption(d, "Each stage finishes before the next begins.")


@design("HYG/cleaning-without-soap-1")
def _(d):
    d.line(16, 246, 624, 246, width=4)
    d.piece("pot-with-lid", 50, 110, 170)
    d.curve_arrow("M 90 118 C 120 60 190 60 220 118", (220, 118), 1.0)
    d.text("Scrub", 155, 54, size=16, weight=600)
    d.piece("bowl", 440, 150, 140)
    d.text("Ash paste", 510, 276, size=16, weight=600)
    d.piece("water-drop", 270, 80, 60)
    d.arrow(300, 150, 252, 190, color=BLUE)
    d.text("Rinse", 340, 120, size=16, weight=600, anchor="start")
    caption(d, "The rinse removes the paste.", 336)


@design("HYG/cleaning-without-soap-2")
def _(d):
    d.piece("pan", 16, 85, 150)
    chip(d, 262, 148, 130, 56, "Wipe grease\ndry")
    d.badge(1, 262, 100, r=16)
    d.arrow(170, 148, 190, 148)
    d.arrow(330, 148, 390, 148)
    d.badge(2, 420, 100, r=16)
    d.piece("flame", 400, 110, 80)
    d.piece("water-drop", 500, 115, 70)
    d.text("Hot rinse", 480, 230, size=16, weight=600)
    caption(d, "Wiping first does most of the work.", 320)


@design("HYG/daily-hygiene-routine-1")
def _(d):
    xs = timeline(d, ["Morning wash", "Midday check", "Evening: body\nand feet"], y=150)
    chip(d, 320, 270, 300, 50, "Weekly band at the end")
    caption(d, "Each task is tied to a fixed moment.", 336)


@design("HYG/daily-hygiene-routine-2")
def _(d):
    loop(d, ["Cue: leave\nthe latrine", "Action: wash\nhands with soap", "Reward: clean\nhands before food"], cx=320, cy=180, rx=200, ry=90, cw=170, ch=62)
    d.piece("soap", 485, 262, 70)
    caption(d, "The cue already happens, so no reminder is needed.", 340)


@design("HYG/daily-hygiene-routine-3")
def _(d):
    cols = ["Ana", "Ben", "Chi"]
    tasks = ["Water", "Rubbish", "Latrine"]
    x0, cw = 190, 140
    for i, c in enumerate(cols):
        cx = x0 + i * cw + cw / 2
        d.piece("person-standing", cx - 38, 26, 76)
        d.text(c, cx, 102, size=16, weight=600)
    for r, t in enumerate(tasks):
        y = 120 + r * 62
        d.rect(40, y, 150, 62, fill=CREAM, rx=0)
        d.text(t, 115, y + 38, size=16, weight=600)
        for i in range(3):
            d.rect(x0 + i * cw, y, cw, 62, fill=PAPER, rx=0)
    d.tick(x0 + cw / 2, 151, 15)
    d.tick(x0 + 1.5 * cw, 213, 15)
    d.tick(x0 + 2.5 * cw, 275, 15)
    d.tick(x0 + 2.5 * cw, 151, 15)
    caption(d, "The board shows who did what.", 336)


@design("HYG/daily-hygiene-routine-4")
def _(d):
    x0, cw, lw = 170, 110, 130
    d.rect(40, 40, lw, 40, fill=PAPER, rx=0)
    for i in range(4):
        d.rect(x0 + i * cw, 40, cw, 40, fill=CREAM, rx=0)
        d.text(f"Round {i + 1}", x0 + i * cw + cw / 2, 66, size=16, weight=600)
    jobs = ["Bucket fill", "Rubbish", "Latrine lid"]
    names = "ABCD"
    for r, j in enumerate(jobs):
        y = 80 + r * 60
        d.rect(40, y, lw, 60, fill=CREAM, rx=0)
        d.text(j, 40 + lw / 2, y + 36, size=15, weight=600)
        for c in range(4):
            d.rect(x0 + c * cw, y, cw, 60, fill=PAPER, rx=0)
            d.text(names[(r + c) % 4], x0 + c * cw + cw / 2, y + 38, size=20, weight=600)
    caption(d, "Each round the jobs move one person along.", 290)
    caption(d, "Nobody keeps the worst job.", 316)


@design("HYG/dental-care-without-a-dentist-1")
def _(d):
    d.piece("tooth", 16, 20, 100)
    grid_steps(d, ["Angle at\ngum line", "Small circles", "Chewing\nsurfaces", "Inner\nsurfaces"], 2, y0=100, cw=200, ch=64, gapx=60, gapy=40)
    d.text("Inner surfaces are easily missed.", 330, 52, size=16, weight=600, anchor="start")


@design("HYG/dental-care-without-a-dentist-2")
def _(d):
    d.piece("cup", 30, 90, 150)
    chip(d, 320, 150, 150, 60, "Pinch of salt,\nstirred")
    d.piece("cup", 460, 90, 150)
    d.arrow(190, 150, 238, 150)
    d.arrow(402, 150, 450, 150)
    d.text("Warm water", 105, 235, size=16, weight=600)
    d.text("Clear solution", 535, 235, size=16, weight=600)
    caption(d, "The salt must dissolve fully before rinsing.", 320)


@design("HYG/dental-care-without-a-dentist-3")
def _(d):
    xs = timeline(d, ["Morning\nbrushing", "Evening\nbrushing"], y=90, x0=110, x1=530)
    d.piece("bacterial-film", 250, 200, 140)
    d.arrow(xs[0] + 20, 175, 280, 235, width=3)
    d.arrow(xs[1] - 20, 175, 360, 235, width=3)
    d.text("Bacterial film builds up daily", 320, 328, size=16, weight=600)


@design("HYG/dental-care-without-a-dentist-4")
def _(d):
    d.piece("gum", 190, 50, 260)
    d.leader(120, 80, 300, 100)
    d.text("Enamel", 110, 86, size=16, weight=600, anchor="end")
    d.leader(120, 200, 246, 150)
    d.text("Gum line", 110, 206, size=16, weight=600, anchor="end")
    d.leader(520, 140, 372, 134)
    d.text("Plaque line", 530, 146, size=16, weight=600, anchor="start")
    caption(d, "Plaque sits where brushing must reach.", 336)


@design("HYG/disinfecting-surfaces-1")
def _(d):
    d.rect(30, 50, 580, 40, fill=CREAM, rx=0)
    d.text("Use", 235, 77, size=16, weight=600)
    d.text("Mix", 475, 77, size=16, weight=600)
    for r, (p, a, b) in enumerate([("bottle", "General\nsurfaces", "1 bleach : 50 water"), ("bucket", "Contaminated\nareas", "1 bleach : 10 water")]):
        y = 90 + r * 100
        d.rect(30, y, 580, 100, fill=PAPER, rx=0)
        d.line(350, y, 350, y + 100)
        d.piece(p, 40, y + 8, 110)
        d.text(a, 160, y + 50, size=16, weight=600, anchor="start")
        d.text(b, 480, y + 56, size=17, weight=600)
    caption(d, "Contaminated areas need the stronger mix.", 316)
    caption(d, "Mix fresh daily.", 340)


@design("HYG/disinfecting-surfaces-2")
def _(d):
    xs = timeline(d, ["Wipe on", "Stay wet", "Rinse"], y=170, x0=80, x1=560)
    d.line(xs[1] - 80, 130, xs[1] + 80, 130, width=3)
    d.text("at least 10 minutes", xs[1], 112, size=16, weight=600)
    caption(d, "Re-wet a drying patch.", 330)


@design("HYG/disinfecting-surfaces-3")
def _(d):
    d.rect(40, 40, 560, 250, fill=PAPER, rx=0)
    d.line(320, 40, 320, 290)
    d.line(40, 165, 600, 165)
    d.piece("door-handle", 70, 70, 80)
    d.text("Door handles", 110, 150, size=15, weight=600)
    d.piece("tap", 400, 70, 80)
    d.text("Taps", 440, 150, size=15, weight=600)
    d.piece("toilet-seat", 70, 190, 80)
    d.text("Toilet seat", 110, 275, size=15, weight=600)
    d.piece("light-switch", 400, 190, 80)
    d.text("Light switches", 440, 275, size=15, weight=600)
    caption(d, "Effort goes to touch points.", 330)


@design("HYG/disinfecting-surfaces-4")
def _(d):
    grid_steps(d, ["Detergent\nclean", "Rinse\nand dry", "Disinfect,\nkeep wet", "Rinse food\nsurfaces"], 2, y0=50, cw=200, ch=70, gapx=60, gapy=50)
    caption(d, "Skipping the first two makes disinfecting fail.", 320)


@design("HYG/hand-hygiene-for-children-1")
def _(d):
    d.piece("open-hand", 170, 40, 300)
    left = [("Under nails", 100, 270, 92), ("Thumbs", 180, 252, 190), ("Palms", 260, 300, 215)]
    right = [("Fingertips", 100, 388, 88), ("Between fingers", 180, 352, 130), ("Backs", 260, 345, 230)]
    for s, ly, ex, ey in left:
        d.text(s, 30, ly + 6, size=16, weight=600, anchor="start")
        d.leader(30 + len(s) * 8.6 + 8, ly, ex, ey)
    for s, ly, ex, ey in right:
        d.text(s, 610, ly + 6, size=16, weight=600, anchor="end")
        d.leader(610 - len(s) * 8.6 - 8, ly, ex, ey)
    caption(d, "Thumbs and nails are the areas most often skipped.", 336)


@design("HYG/hand-hygiene-for-children-2")
def _(d):
    flow(d, [("water-drop", "Wet hands"), ("soap", "Rub with soap,\ncount to 20"), ("open-hand", "Rinse and dry")], 80, w=130)
    caption(d, "Counting makes it a timed routine.", 320)


@design("HYG/latrines-and-waste-1")
def _(d):
    d.piece("latrine", 40, 70, 200)
    d.piece("pool", 440, 105, 150)
    d.text("Latrine", 140, 280, size=16, weight=600)
    d.text("Pool", 515, 280, size=16, weight=600)
    d.arrow(250, 190, 440, 190, width=3)
    d.arrow(440, 190, 250, 190, width=3)
    d.text("Distance to water source", 345, 172, size=16, weight=600)
    caption(d, "Siting distance is measured, not guessed.", 330)


@design("HYG/latrines-and-waste-2")
def _(d):
    d.piece("slope", 120, 40, 400)
    d.piece("pool", 400, 40, 100)
    d.piece("hut", 130, 190, 100)
    d.text("Well", 450, 62, size=16, weight=600)
    d.text("Latrine", 180, 322, size=16, weight=600)
    d.arrow(420, 175, 280, 240, color=BLUE, width=4)
    d.text("Runoff", 350, 236, size=16, weight=600, anchor="start")


@design("HYG/latrines-and-waste-3")
def _(d):
    n = ["Waste in\nlatrine", "Flies", "Food", "Hands"]
    pts = [(160, 100), (480, 100), (480, 230), (160, 230)]
    for (x, y), s in zip(pts, n):
        chip(d, x, y, 150, 62, s)
    d.arrow(240, 100, 400, 100)
    d.arrow(480, 134, 480, 196)
    d.arrow(400, 230, 240, 230)
    d.arrow(160, 196, 160, 134)
    d.text("Cover the lid", 320, 144, size=16, weight=600)
    d.text("or wash hands:", 320, 164, size=16, weight=600)
    d.text("each breaks a link", 320, 184, size=16, weight=600)


@design("HYG/laundry-without-power-1")
def _(d):
    d.piece("bucket", 20, 90, 130)
    d.piece("bucket", 255, 90, 130)
    d.piece("rope-coil", 490, 90, 130)
    d.arrow(155, 150, 250, 150)
    d.arrow(390, 150, 485, 150)
    d.text("Wash", 85, 220, size=17, weight=600)
    d.text("Wring", 320, 220, size=17, weight=600)
    d.text("Dry on line", 555, 220, size=17, weight=600)
    caption(d, "One-way flow keeps dirty and clean apart.", 320)


@design("HYG/laundry-without-power-2")
def _(d):
    d.piece("bucket", 60, 80, 190)
    d.piece("bucket", 390, 80, 190)
    d.arrow(260, 160, 380, 160, width=5)
    d.text("Washing with soap", 155, 270, size=17, weight=600)
    d.text("Clean rinse water", 485, 270, size=17, weight=600)
    caption(d, "Items move one way only.", 330)


@design("HYG/laundry-without-power-3")
def _(d):
    loop(d, ["Sweat and oil in\nsoiled fabric", "Bacteria", "Skin irritation"], cx=320, cy=175, rx=200, ry=95, cw=180, ch=62)
    caption(d, "The loop runs until the fabric is washed.", 340)


@design("HYG/laundry-without-power-4")
def _(d):
    d.piece("sun", 500, 10, 110)
    d.text("Full sun", 490, 62, size=16, weight=600, anchor="end")
    d.line(30, 130, 610, 130, width=4)
    for x in (50, 265, 480):
        d.piece("cloth", x, 130, 110)
    d.arrow(170, 215, 270, 215, color=BLUE, width=4)
    d.arrow(385, 215, 485, 215, color=BLUE, width=4)
    d.text("Airflow between spaced clothes", 320, 270, size=16, weight=600)
    caption(d, "Spacing dries heavy items through.", 330)


@design("HYG/lice-and-scabies-control-1")
def _(d):
    xs = timeline(d, ["Comb", "Check bedding", "Repeat"], y=150, x0=90, x1=550)
    d.piece("comb", xs[0] - 45, 205, 90)
    d.piece("bedding", xs[1] - 45, 205, 90)
    d.text("again, on schedule", xs[2], 215, size=15, weight=600)
    caption(d, "Combing and checks repeat on a schedule.", 336)


@design("HYG/lice-and-scabies-control-2")
def _(d):
    x0, cw = 40, 190
    heads = ["People to check", "Bedding to wash", "Items to isolate"]
    for i, h in enumerate(heads):
        d.rect(x0 + i * cw, 40, cw, 44, fill=CREAM, rx=0)
        d.text(h, x0 + i * cw + cw / 2, 68, size=16, weight=600)
        d.rect(x0 + i * cw, 84, cw, 180, fill=PAPER, rx=0)
    for k in range(3):
        d.piece("person-standing", x0 + 12 + k * 56, 115, 80)
    d.piece("bedding", x0 + cw + 40, 130, 110)
    d.piece("hat", x0 + 2 * cw + 40, 130, 110)
    caption(d, "The whole household is checked together.", 300)
    caption(d, "One untreated person reinfects the rest.", 326)


@design("HYG/lice-and-scabies-control-3")
def _(d):
    d.piece("person-standing", 270, 100, 100)
    d.piece("survivor-mark", 300, 50, 40)
    for (p, x, y, lab) in [("comb", 40, 70, "Shared combs"), ("hat", 450, 70, "Hats")]:
        d.piece(p, x, y, 120)
        d.text(lab, x + 60, y + 108, size=16, weight=600)
    d.piece("bedding", 270, 200, 100)
    d.text("Bedding", 320, 298, size=16, weight=600)
    d.arrow(180, 125, 268, 140, width=3)
    d.arrow(268, 140, 180, 125, width=3)
    d.arrow(462, 125, 374, 140, width=3)
    d.arrow(374, 140, 462, 125, width=3)
    d.arrow(320, 172, 320, 206, width=3)
    d.arrow(320, 206, 320, 172, width=3)
    caption(d, "Shared items link everyone.", 340)


@design("HYG/lice-and-scabies-control-4")
def _(d):
    grid_steps(d, ["Section 1", "Section 2", "Section 3"], 3, y0=80, cw=150, ch=64, gapx=45)
    d.piece("comb", 275, 190, 90)
    d.text("Comb each section, scalp to tip", 320, 290, size=16, weight=600)
    caption(d, "Cover the whole head in sections.", 336)


@design("HYG/menstrual-hygiene-1")
def _(d):
    grid_steps(d, ["Move behind\nthe screen", "Change", "Wash hands", "Rinse the\ncloth", "Dry out\nof sight"], 3, y0=50, cw=170, ch=72, gapy=60)
    caption(d, "The private screened area comes first.", 330)


@design("HYG/menstrual-hygiene-2")
def _(d):
    d.rect(30, 50, 580, 220, fill=PAPER, rx=14, dash="10 8")
    d.text("One kit", 320, 84, size=17, weight=600)
    items = [("absorbent-pad", "Pads"), ("soap", "Soap"), ("towel", "Towel"), ("bag", "Sealed\nwaste bag")]
    for i, (p, s) in enumerate(items):
        x = 50 + i * 140
        d.piece(p, x, 110, 120)
        d.text(s, x + 60, 232, size=16, weight=600)
    caption(d, "One kit set, so nothing is missing.", 316)


@design("HYG/menstrual-hygiene-3")
def _(d):
    labels = ["Lack of\nsupplies", "Unchanged\npads", "Infection", "Missed school\nor work", "Loss of\nincome"]
    pos = [(110, 120), (320, 120), (530, 120), (215, 255), (425, 255)]
    for (x, y), s in zip(pos, labels):
        chip(d, x, y, 160, 70, s)
    d.arrow(192, 120, 238, 120)
    d.arrow(402, 120, 448, 120)
    d.line(530, 156, 530, 187)
    d.line(530, 187, 215, 187)
    d.arrow(215, 187, 215, 217)
    d.arrow(298, 255, 342, 255)
    d.piece("warning", 30, 24, 55)
    d.text("First link", 92, 64, size=15, weight=600, anchor="start")
    caption(d, "One missing item can start the whole chain.", 338)


@design("HYG/menstrual-hygiene-4")
def _(d):
    d.piece("sun", 480, 20, 120)
    d.line(30, 140, 450, 140, width=4)
    for x in (60, 250):
        d.piece("cloth", x, 140, 110)
    d.arrow(175, 230, 255, 230, color=BLUE, width=4)
    d.text("Airflow", 215, 262, size=16, weight=600)
    d.text("Cloths in direct sunlight", 240, 110, size=16, weight=600)
    d.text("Sun", 540, 156, size=16, weight=600)
    caption(d, "Dry in full sun, in a private spot.", 330)


@design("HYG/mould-removal-1")
def _(d):
    pos = grid_steps(d, ["Ventilate", "Scrub", "Disinfect", "Dry"], 4, y0=70, cw=125, ch=64, gapx=35, gapy=60)
    x0, x3 = pos[0][0], pos[3][0]
    chip(d, 320, 235, 220, 56, "Fix source of damp", fill=YELLOW)
    d.line(x3, 137, x3, 180)
    d.line(x3, 180, 320, 180)
    d.arrow(320, 180, 320, 203)
    d.line(210, 235, x0, 235)
    d.arrow(x0, 235, x0, 142)
    caption(d, "Fix the damp source or mould returns.", 330)


@design("HYG/mould-removal-2")
def _(d):
    d.piece("wall", 220, 139, 200)
    d.line(16, 270, 624, 270, width=4)
    for x in (270, 320, 370):
        d.arrow(x, 264, x, 212, color=BLUE, width=3)
    d.text("Rising damp", 130, 240, size=16, weight=600, anchor="end")
    d.leader(145, 236, 266, 236)
    d.leader(480, 150, 402, 190)
    d.text("Cold inner face", 490, 156, size=16, weight=600, anchor="start")
    d.leader(480, 225, 396, 225)
    d.text("Condensation", 490, 231, size=16, weight=600, anchor="start")
    caption(d, "Mould starts on cold walls too.", 330)


@design("HYG/mould-removal-3")
def _(d):
    labels = ["Spores settle\non damp plaster", "Patch grows", "Visible\ncolonies", "Spores spread"]
    grid_steps(d, labels, 2, y0=50, cw=200, ch=70, gapx=60, gapy=50)
    d.piece("tip", 150, 270, 50)
    d.text("Remove it while the patch is small", 210, 304, size=16, weight=600, anchor="start")


@design("HYG/mould-removal-4")
def _(d):
    d.piece("window", 16, 80, 150)
    d.piece("window", 474, 80, 150)
    d.arrow(175, 140, 465, 140, color=BLUE, width=5)
    d.text("Airflow", 320, 120, size=17, weight=600, fill=BLUE)
    d.text("Open window", 91, 230, size=16, weight=600)
    d.text("Open window", 549, 230, size=16, weight=600)
    d.piece("furniture", 250, 160, 140)
    d.text("Keep air moving behind furniture", 320, 310, size=16, weight=600)
