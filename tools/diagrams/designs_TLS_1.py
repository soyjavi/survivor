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


def steps(d, items, y=50, w=150, arrows=True, label_dy=24):
    n = len(items)
    gap = (640 - n * w) / (n + 1)
    py = y + 34
    for i, (pieces, label) in enumerate(items):
        x = gap + i * (w + gap)
        cx = x + w / 2
        d.badge(i + 1, cx, y)
        if isinstance(pieces, str):
            chip(d, cx, py + w * 0.375, w - 10, 64, pieces)
        else:
            m = len(pieces)
            for j, e in enumerate(pieces):
                name, pw = e[0], e[1]
                if len(e) == 4:
                    d.piece(name, cx - pw / 2 + e[2], py + w * 0.375 - pw * 0.375 + e[3], pw)
                    continue
                px = x + (w - pw * m) / 2 + j * pw if m > 1 else cx - pw / 2
                d.piece(name, px, py + w * 0.375 - pw * 0.375, pw)
        d.text(label, cx, py + w * 0.75 + label_dy, size=16, weight=600)
        if arrows and i < n - 1:
            d.arrow(x + w + 4, py + w * 0.375, x + w + gap - 4, py + w * 0.375)


@design("TLS/basic-carpentry-1")
def _(d):
    steps(d, [([("board", 140)], "Measure\nand mark"), ("30 · 40 · 50 cm", "Check the corner"), ([("saw", 140)], "Cut joints")])
    caption(d, "Check the corner before the first cut.")


@design("TLS/basic-carpentry-2")
def _(d):
    d.piece("board", 150, 90, 340)
    d.line(340, 120, 340, 290, dash="9 7", width=3, color=RED)
    d.piece("saw", 350, 20, 130)
    d.arrow(440, 106, 440, 160, width=3)
    d.text("Waste", 440, 310, size=16, weight=600)
    d.text("Cut line", 330, 116, size=16, weight=600, anchor="end")
    d.text("Keep", 240, 310, size=16, weight=600)
    d.leader(190, 160, 330, 184)
    d.text("Kerf", 180, 164, size=16, weight=600, anchor="end")
    caption(d, "Blade stays on the waste side.")


@design("TLS/basic-carpentry-3")
def _(d):
    steps(d, [([("board", 140)], "Upper half\nremoved"), ([("board", 140)], "Lower half\nremoved"), ([("board", 140, 0, 8), ("board", 140, 0, -8)], "Overlap flush")])
    caption(d, "The two cuts must match.")


@design("TLS/basic-carpentry-4")
def _(d):
    d.piece("board", 190, 106, 260)
    d.piece("board", 190, 20, 260)
    d.line(200, 192, 480, 122, dash="9 7", width=3, color=RED)
    for x in (250, 320, 390):
        d.arrow(x, 24, x, 78, width=3)
        d.arrow(x, 330, x, 262, width=3)
    d.text("Glue line", 490, 122, size=16, weight=600, anchor="start")
    d.text("Boards", 170, 124, size=16, weight=600, anchor="end")
    d.text("Boards", 170, 200, size=16, weight=600, anchor="end")


@design("TLS/basic-lashing-and-frames-1")
def _(d):
    steps(d, [([("rope-coil", 130)], "Hitch anchor on\ntwo crossed poles"), ([("rope-coil", 130)], "Wraps"), ([("rope-coil", 100, -34, 0), ("arrow-curved", 80, 50, 0)], "Frapping")])
    caption(d, "Frapping pulls the poles together.")


@design("TLS/basic-lashing-and-frames-2")
def _(d):
    d.piece("post", 200, 118, 240)
    d.piece("beam", 200, 40, 240)
    d.piece("rope-coil", 290, 126, 60)
    d.arrow(320, 20, 320, 84, width=4)
    d.text("Load", 340, 48, size=16, weight=600, anchor="start")
    d.text("Beam", 190, 130, size=16, weight=600, anchor="end")
    d.leader(250, 222, 308, 214)
    d.text("Post", 240, 226, size=16, weight=600, anchor="end")
    d.leader(480, 170, 340, 156)
    d.text("Lashing", 490, 174, size=16, weight=600, anchor="start")
    caption(d, "The lashing only stops sliding.")


@design("TLS/basic-sewing-repairs-for-clothing-1")
def _(d):
    names = ["Running", "Backstitch", "Whipstitch"]
    for i, n in enumerate(names):
        x = 16 + i * 206
        d.rect(x, 24, 196, 270)
        d.text(n, x + 98, 58, size=17, weight=700)
        d.piece("stitch-line", x + 18, 90, 160)
    d.arrow(56, 240, 172, 240, width=3)
    d.arrow(270, 230, 370, 230, width=3)
    d.arrow(340, 262, 290, 262, width=3)
    d.arrow(470, 240, 580, 240, width=3)
    caption(d, "Arrows show needle direction; backstitch doubles back.", 322)


@design("TLS/basic-sewing-repairs-for-clothing-2")
def _(d):
    d.piece("patch", 190, 50, 260)
    d.leader(120, 130, 276, 152)
    d.text("Stitches", 110, 134, size=16, weight=600, anchor="end")
    d.leader(540, 120, 380, 120)
    d.text("Patch", 550, 124, size=16, weight=600, anchor="start")
    d.arrow(160, 290, 480, 290, width=3)
    d.arrow(480, 290, 160, 290, width=3)
    d.text("Strain", 320, 274, size=16, weight=600)
    caption(d, "The patch edges carry the load.", 330)


@design("TLS/basic-tool-list-1")
def _(d):
    groups = [("Cutting", [("knife", 100), ("saw", 100)]), ("Fastening", [("hammer", 100)]), ("Measuring", []), ("Light", [("flashlight", 100)]), ("Cooking", [("pot-with-lid", 100)])]
    for i, (g, ps) in enumerate(groups):
        x = 18 + i * 122
        d.rect(x, 24, 112, 284)
        d.text(g, x + 56, 56, size=16, weight=700)
        for j, (n, w) in enumerate(ps):
            d.piece(n, x + 6, 80 + j * 100, w)
        if not ps:
            d.text("tape\nmeasure", x + 56, 150, size=15, fill="#4a4238")
    caption(d, "A missing job shows a missing tool.", 336)


@design("TLS/basic-tool-list-2")
def _(d):
    d.piece("adjustable-spanner", 20, 80, 240)
    d.piece("bolt", 400, 100, 200)
    d.arrow(250, 170, 420, 170, width=4)
    d.text("Jaws close onto the flats", 330, 140, size=16, weight=600)
    d.leader(100, 70, 163, 152)
    d.text("Jaw screw", 90, 66, size=16, weight=600, anchor="end")
    d.leader(529, 256, 529, 190)
    d.text("Hex nut", 529, 276, size=16, weight=600, anchor="middle")
    caption(d, "Flats, not corners, so the nut does not round.")


@design("TLS/basic-tool-list-3")
def _(d):
    for i, s in enumerate(["10", "13", "17"]):
        y = 50 + i * 90
        chip(d, 130, y + 30, 150, 52, f"Size {s}")
        d.arrow(210, y + 30, 360, y + 30, width=4)
        d.piece("bolt", 380, y - 12, 150)
    caption(d, "One size fits one bolt head.", 336)


@design("TLS/bicycle-repair-1")
def _(d):
    steps(d, [([("tyre", 130)], "Find the\npuncture"), ([("patch", 130)], "Patch it"), ("Brake pads", "Pads to rim")])
    caption(d, "The puncture is found before gluing.")


@design("TLS/bicycle-repair-2")
def _(d):
    d.piece("bowl", 40, 100, 280)
    chip(d, 180, 62, 110, 44, "Tube")
    d.arrow(180, 88, 180, 150, width=3)
    d.piece("waves", 400, 130, 130)
    d.piece("water-drop", 435, 70, 60)
    d.leader(590, 110, 515, 170)
    d.text("Hole", 596, 100, size=16, weight=600, anchor="end")
    caption(d, "Patch only on the marked spot.")


@design("TLS/essential-knots-1")
def _(d):
    steps(d, [([("rope-coil", 130)], "Small loop"), ([("rope-coil", 130)], "Working end\nup through"), ([("rope-coil", 100, -34, 0), ("arrow-curved", 80, 50, 0)], "Around and\nback down")])
    caption(d, "Loop, working end, standing part: pull the standing part.")


@design("TLS/essential-knots-2")
def _(d):
    d.piece("pole", 40, 80, 190)
    d.piece("rope-coil", 270, 90, 170)
    d.leader(500, 100, 395, 150)
    d.text("Wraps", 510, 104, size=16, weight=600, anchor="start")
    d.leader(500, 200, 400, 185)
    d.text("Tucked end", 510, 204, size=16, weight=600, anchor="start")
    d.arrow(200, 290, 440, 290, width=3)
    d.arrow(440, 290, 200, 290, width=3)
    d.text("Load direction", 320, 274, size=16, weight=600)
    caption(d, "It slips one way.", 330)


@design("TLS/essential-knots-3")
def _(d):
    d.piece("rope-coil", 160, 80, 240)
    d.leader(100, 110, 230, 160)
    d.text("Bight", 90, 106, size=16, weight=600, anchor="end")
    d.leader(100, 220, 250, 190)
    d.text("Loop", 90, 226, size=16, weight=600, anchor="end")
    d.leader(560, 220, 380, 210)
    d.text("Tail", 570, 226, size=16, weight=600, anchor="start")
    d.piece("arrow-curved", 440, 90, 120)
    d.text("Tail back through", 500, 90, size=16, weight=600)
    caption(d, "The bulky knot stops at the hole.")


@design("TLS/essential-knots-4")
def _(d):
    d.piece("rope-coil", 240, 90, 170)
    d.piece("strap", 20, 190, 190)
    d.text("Strap", 115, 304, size=16, weight=600)
    d.arrow(430, 160, 600, 160, width=4)
    d.text("Pull", 515, 140, size=16, weight=600)
    d.piece("arrow-curved", 250, 200, 110)
    d.text("Lever", 305, 300, size=16, weight=600)
    d.leader(120, 70, 305, 128)
    d.text("Loop", 110, 66, size=16, weight=600, anchor="end")
    caption(d, "The loop gives mechanical advantage.", 340)


@design("TLS/improvised-tools-1")
def _(d):
    items = [("Stick", None, "Dig"), ("Rock", "rock", "Cut"), ("Cord", "rope-coil", "Bind"), ("Bottle", "bottle", "Scoop")]
    for i, (name, piece, use) in enumerate(items):
        x = 16 + i * 154
        d.rect(x, 40, 146, 250)
        if piece:
            d.piece(piece, x + 13, 70, 120)
        else:
            chip(d, x + 73, 120, 100, 44, name)
        d.leader(x + 73, 205, x + 73, 150)
        chip(d, x + 73, 245, 100, 40, use)
    caption(d, "Each tool matches one task.", 326)


@design("TLS/improvised-tools-2")
def _(d):
    steps(d, [("Stick", "Forearm length"), ("One end\nflat", "Scrape flat"), ([("coals", 90, -30, 0), ("arrow-curved", 70, 50, 0)], "Over the coals")], y=50)
    caption(d, "Set the point before heating.")


@design("TLS/improvised-tools-3")
def _(d):
    d.piece("coals", 200, 170, 200)
    d.piece("flame", 245, 100, 110)
    chip(d, 300, 52, 130, 44, "Stick point")
    d.piece("arrow-curved", 400, 20, 80)
    d.line(220, 100, 380, 100, dash="9 7", width=3, color=RED)
    d.text("Stop here", 400, 106, size=16, weight=600, anchor="start")
    d.leader(500, 240, 380, 250)
    d.text("Coals", 510, 246, size=16, weight=600, anchor="start")
    caption(d, "The point stays above the flame.")


@design("TLS/knife-safety-1")
def _(d):
    for i in range(3):
        d.rect(16 + i * 208, 30, 192, 260)
    d.piece("knife", 24, 100, 100)
    d.piece("sheath", 120, 100, 80)
    d.text("Sheath", 112, 270, size=16, weight=600)
    d.piece("person-standing", 250, 50, 160)
    d.piece("knife", 325, 98, 80)
    d.text("Grip", 320, 270, size=16, weight=600)
    d.piece("knife", 450, 110, 130)
    d.arrow(450, 200, 590, 200, width=4)
    d.text("Away", 520, 270, size=16, weight=600)
    caption(d, "The blade points away from the body and other hand.", 326)


@design("TLS/knife-safety-2")
def _(d):
    d.piece("person-kneeling", 16, 50, 190)
    d.piece("hand", 240, 90, 120)
    d.piece("knife", 370, 100, 180)
    d.arrow(360, 250, 580, 250, width=4)
    d.text("Away from the fingers", 470, 280, size=16, weight=600)
    d.leader(300, 60, 292, 128)
    d.text("Knuckles", 300, 56, size=16, weight=600, anchor="middle")
    d.leader(440, 60, 428, 166)
    d.text("Edge", 440, 56, size=16, weight=600)
    caption(d, "Hand position, not speed, prevents cuts.")


@design("TLS/knife-safety-3")
def _(d):
    d.piece("board", 110, 80, 320)
    d.piece("rope-coil", 220, 158, 100)
    d.piece("hand", 20, 135, 110)
    d.piece("knife", 460, 90, 140)
    d.arrow(600, 190, 450, 190, width=3, dash="8 6")
    d.text("Blade path", 525, 222, size=16, weight=600)
    d.leader(80, 108, 76, 176)
    d.text("Holding hand", 80, 100, size=16, weight=600)
    caption(d, "The blade passes clear of the holding hand.")


@design("TLS/knife-safety-4")
def _(d):
    for x in (130, 190, 250):
        d.arrow(x, 20, x, 62, width=3)
    d.text("Pressure", 280, 46, size=16, weight=600, anchor="start")
    ys = [("bandage-roll", "Bandage"), ("cloth", "Cloth"), ("bleeding", "Bleeding")]
    for i, (n, lab) in enumerate(ys):
        y = 70 + i * 76
        d.piece(n, 130, y, 140)
        d.text(lab, 300, y + 56, size=16, weight=600, anchor="start")
    caption(d, "Pressure stays until bleeding stops.", 340)


@design("TLS/ladder-safety-1")
def _(d):
    d.piece("wall", 30, 80, 200)
    d.piece("ladder", 290, 80, 200)
    for x in (2, 174, 346):
        d.piece("ground-line", x, 143, 200)
    d.line(212, 236, 212, 276, width=2)
    d.line(354, 236, 354, 276, width=2)
    d.arrow(222, 262, 344, 262, width=3)
    d.arrow(344, 262, 222, 262, width=3)
    chip(d, 283, 304, 250, 38, "Base: one quarter of height", size=16)
    caption(d, "The base distance sets the angle.", 40)


@design("TLS/ladder-safety-2")
def _(d):
    items = [("ladder", "Stepladder"), ("spreader-bar", "Spreader bars"), ("latch", "Latches")]
    for i, (n, lab) in enumerate(items):
        x = 16 + i * 180
        d.piece(n, x, 70, 160)
        d.text(lab, x + 80, 230, size=16, weight=600)
    d.piece("caution", 560, 90, 64)
    d.text("Unlocked", 592, 190, size=16, weight=600)
    caption(d, "Lock them before the first step.")


@design("TLS/ladder-safety-3")
def _(d):
    d.piece("ladder", 170, 30, 300)
    d.piece("person-standing", 250, 70, 140)
    d.line(320, 36, 320, 270, dash="9 7", width=3, color=RED)
    d.leader(500, 160, 326, 160)
    d.text("Belt buckle", 510, 166, size=16, weight=600, anchor="start")
    d.arrow(260, 296, 380, 296, width=3)
    d.arrow(380, 296, 260, 296, width=3)
    d.text("Stay between the stiles", 320, 326, size=16, weight=600)


@design("TLS/making-simple-containers-1")
def _(d):
    d.piece("bucket", 150, 20, 340)
    d.line(240, 134, 400, 134, dash="9 7", width=3, color=RED)
    d.text("Fill line", 420, 140, size=16, weight=600, anchor="start")
    d.leader(210, 56, 318, 56)
    d.text("Bail", 200, 62, size=16, weight=600, anchor="end")
    d.leader(210, 108, 246, 108)
    d.text("Rim", 200, 114, size=16, weight=600, anchor="end")
    caption(d, "Fill only to the line so it carries without spilling.")


@design("TLS/making-simple-containers-2")
def _(d):
    d.piece("bag", 170, 30, 300)
    d.line(320, 100, 320, 240, dash="2 8", width=4, color=BLUE)
    d.text("Seam", 520, 150, size=16, weight=600, anchor="start")
    d.leader(512, 146, 326, 170)
    d.arrow(560, 190, 560, 260, width=4)
    d.text("Weight", 560, 286, size=16, weight=600)
    caption(d, "Load runs through the seam, not the fabric.")


@design("TLS/repairing-footwear-1")
def _(d):
    steps(d, [([("sole", 80), ("adhesive", 80)], "Glue both faces"), ([("timeline-marker", 110)], "Wait until tacky"), ([("rope-coil", 110)], "Clamp with cord")])
    d.arrow(517, 78, 517, 112, width=3)
    d.arrow(517, 198, 517, 170, width=3)
    caption(d, "The clamp holds the sole while the glue cures.")


@design("TLS/repairing-footwear-2")
def _(d):
    d.piece("sole", 40, 20, 280)
    d.piece("rope-coil", 107, 80, 120)
    d.leader(480, 94, 200, 86)
    d.text("Flex zone", 490, 100, size=16, weight=600, anchor="start")
    d.leader(480, 154, 214, 120)
    d.text("Cord", 490, 160, size=16, weight=600, anchor="start")
    d.leader(480, 214, 172, 152)
    d.text("Tightest turns here", 490, 220, size=16, weight=600, anchor="start")
    caption(d, "The flex zone lifts first.")


@design("TLS/repairing-footwear-3")
def _(d):
    d.piece("leather-split", 170, 40, 300)
    d.line(285, 70, 285, 250, dash="6 6", width=2)
    d.line(355, 70, 355, 250, dash="6 6", width=2)
    chip(d, 320, 290, 90, 36, "3 mm", size=15)
    d.leader(285, 272, 285, 252)
    d.leader(355, 272, 355, 252)
    d.arrow(520, 90, 520, 220, width=4)
    d.text("Cord direction", 520, 250, size=16, weight=600)


@design("TLS/repairing-footwear-4")
def _(d):
    d.piece("leather-split", 30, 60, 280)
    d.piece("patch", 380, 80, 220)
    d.leader(120, 70, 160, 150)
    d.text("Stitches", 110, 64, size=16, weight=600, anchor="end")
    d.leader(480, 70, 490, 135)
    d.text("Patch", 480, 62, size=16, weight=600, anchor="end")
    d.arrow(375, 175, 300, 175, width=4)
    caption(d, "The patch takes the load, not the torn edge.")


@design("TLS/rope-and-cordage-1")
def _(d):
    for i, n in enumerate(["Paracord", "Nylon", "Polyester", "Plant cord"]):
        x = 24 + i * 152
        d.piece("rope-coil", x, 60, 130)
        d.text(n, x + 65, 190, size=16, weight=600)
    d.arrow(80, 270, 560, 270, width=3)
    d.arrow(560, 270, 80, 270, width=3)
    d.text("Strength", 80, 250, size=16, weight=600, anchor="start")
    d.text("Stretch", 560, 250, size=16, weight=600, anchor="end")
    caption(d, "The load decides the rope.", 320)


@design("TLS/rope-and-cordage-2")
def _(d):
    d.piece("rope-coil", 90, 50, 260)
    d.leader(470, 90, 290, 118)
    d.text("Sheath", 480, 94, size=16, weight=600, anchor="start")
    d.leader(470, 170, 230, 160)
    d.text("Core", 480, 174, size=16, weight=600, anchor="start")
    d.piece("caution", 440, 210, 64)
    d.text("Soft, flat spot", 520, 262, size=16, weight=600, anchor="start")
    d.arrow(440, 250, 318, 226, width=3)
    caption(d, "A soft, flat spot signals hidden core damage.")


@design("TLS/rope-and-cordage-3")
def _(d):
    steps(d, [([("rope-coil", 80, -45, 0), ("rope-coil", 80, 45, 0)], "Roll two strands"), ([("rope-coil", 100, -22, 0), ("rope-coil", 100, 22, 0)], "Join with overlap"), ([("rope-coil", 100, -34, 0), ("arrow-curved", 80, 50, 0)], "Twist opposite")])
    caption(d, "Spread the join along the length.")


@design("TLS/sewing-and-mending-1")
def _(d):
    notes = ["Forward each stitch", "Forward, then back", "Over the edge"]
    for i, n in enumerate(["Running", "Backstitch", "Whipstitch"]):
        y = 20 + i * 104
        d.rect(16, y, 608, 96)
        d.text(n, 36, y + 55, size=17, weight=700, anchor="start")
        d.piece("stitch-line", 190, y - 8, 130)
        d.text(notes[i], 480, y + 86, size=15, fill="#4a4238")
        if i == 0:
            d.arrow(360, y + 40, 600, y + 40, width=3)
        elif i == 1:
            d.arrow(360, y + 28, 520, y + 28, width=3)
            d.arrow(520, y + 54, 440, y + 54, width=3)
        else:
            d.piece("arrow-curved", 400, y - 6, 90)
            d.arrow(520, y + 40, 600, y + 40, width=3)
    caption(d, "Each stitch path is matched to its use.", 346)


@design("TLS/sewing-and-mending-2")
def _(d):
    steps(d, [([("thread", 130)], "Cut the thread"), ([("overhand-knot", 130)], "Knot the end"), ([("needle", 130)], "Eye and tail")])
    caption(d, "The knot sits at the thread end.")


@design("TLS/sewing-and-mending-3")
def _(d):
    d.piece("stitch-line", 40, 90, 300)
    d.piece("needle", 400, 70, 180)
    d.curve_arrow("M431 160 C 420 70, 330 80, 300 218", (300, 218), 1.78)
    d.leader(120, 70, 200, 226)
    d.text("Overlap", 110, 64, size=16, weight=600, anchor="end")
    caption(d, "Each stitch returns into the last one.")


@design("TLS/basic-carpentry-5")
def _(d):
    d.piece("board", 170, 20, 300)
    d.leader(530, 130, 440, 125)
    d.text("Edge gap", 540, 136, size=16, weight=600, anchor="start")
    d.arrow(150, 250, 490, 250, width=4)
    d.arrow(490, 250, 150, 250, width=4)
    d.text("Across grain: moves most", 320, 238, size=16, weight=600)
    d.arrow(250, 305, 390, 305, width=3)
    d.arrow(390, 305, 250, 305, width=3)
    d.text("Along grain: moves little", 320, 330, size=16, weight=600)
