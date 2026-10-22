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


def row(d, items, y, w=130, arrows=False, label_dy=26, size=16):
    n = len(items)
    gap = (640 - n * w) / (n + 1)
    for i, (piece, label) in enumerate(items):
        x = gap + i * (w + gap)
        d.piece(piece, x, y, w)
        d.text(label, x + w / 2, y + w * 0.75 + label_dy, size=size, weight=600)
        if arrows and i < n - 1:
            d.arrow(x + w + 4, y + w * 0.375, x + w + gap - 4, y + w * 0.375)


@design("SEC/safe-room-1")
def _(d):
    row(d, [("room", "Room"), ("shelf", "Supplies"), ("phone-call", "Phone"), ("arrow-both-ways", "Ventilation gap")], 70, w=145)
    caption(d, "Room sits away from outside walls and windows.", 320)


@design("SEC/safe-room-2")
def _(d):
    row(d, [("bottle", "Water"), ("tin", "Food"), ("flashlight", "Torch")], 28, w=130, label_dy=24)
    row(d, [("radio", "Radio"), ("first-aid-kit", "First aid"), ("note", "Phone list")], 178, w=130, label_dy=24)
    caption(d, "Grouped by function, so anyone finds them in the dark.", 342)


@design("SEC/safe-room-3")
def _(d):
    d.piece("door", 40, 40, 190)
    d.arrow(60, 222, 250, 222, width=3)
    d.arrow(250, 256, 60, 256, width=3)
    d.text("Air in under door", 262, 228, size=16, weight=600, anchor="start")
    d.text("Air out under door", 262, 262, size=16, weight=600, anchor="start")
    d.piece("flame", 420, 60, 150)
    d.piece("do-not", 480, 40, 70)
    d.text("No fuel or fire", 495, 200, size=16, weight=600)
    caption(d, "A sealed room still needs air.", 340)


@design("SEC/safe-room-4")
def _(d):
    d.piece("door", 16, 50, 150)
    d.text("Bolted door", 91, 190, size=16, weight=600)
    for x in (220, 340, 460):
        d.piece("person-sitting", x, 40, 110)
    d.text("Household", 385, 150, size=16, weight=600)
    d.piece("bottle", 220, 190, 90)
    d.piece("tin", 340, 190, 90)
    d.piece("flashlight", 460, 190, 90)
    d.text("Supplies within reach", 385, 292, size=16, weight=600)
    caption(d, "People and supplies stay together near the door.", 340)


@design("SEC/safe-room-5")
def _(d):
    row(d, [("door", "Lockable door"), ("tap", "Tap, water close"), ("arrow-both-ways", "Ventilation"), ("window", "Few windows")], 70, w=145)
    caption(d, "A bathroom suits a safe room.", 320)


@design("SEC/search-and-rescue-for-households-1")
def _(d):
    row(d, [("wall", "Wall"), ("ground-signal-x", "X mark + date"), ("beam", "Unsafe beam")], 40, w=150)
    d.piece("warning", 450, 40, 56)
    d.arrow(30, 280, 610, 280, width=4)
    d.text("Route", 320, 270, size=16, weight=600)
    caption(d, "The route keeps clear of the weakest parts.", 340)


@design("SEC/securing-the-home-1")
def _(d):
    row(d, [("bracket", "Door bar"), ("caution", "Window locks"), ("flashlight", "Entrance light"), ("key", "Spare key")], 70, w=145)
    caption(d, "Lock, frame and bar work together.", 320)


@design("SEC/securing-the-home-2")
def _(d):
    d.piece("door", 20, 90, 200)
    d.text("Door frame", 120, 270, size=16, weight=600)
    d.piece("screw", 270, 30, 120)
    d.tick(430, 90, 24)
    d.text("Into framing", 470, 96, size=17, weight=600, anchor="start")
    d.piece("screw", 270, 190, 120)
    d.cross(430, 250, 24)
    d.text("Into trim only", 470, 256, size=17, weight=600, anchor="start")


@design("SEC/securing-the-home-3")
def _(d):
    row(d, [("flashlight", "Motion light"), ("warning", "Power cut"), ("flashlight", "Torch"), ("key", "Keys")], 90, w=110)
    d.arrow(154, 131, 186, 131, width=3)
    d.arrow(304, 131, 336, 131, width=3)
    caption(d, "The torch stays beside the keys.", 330)


@design("SEC/securing-the-home-4")
def _(d):
    d.piece("map", 30, 50, 280)
    d.text("House plan", 170, 290, size=16, weight=600)
    d.piece("footprints", 400, 40, 150)
    d.text("Walk the perimeter", 475, 180, size=16, weight=600)
    for i, x in enumerate((370, 440, 510, 580)):
        d.badge(i + 1, x, 250, 20)
    d.text("Each door and window", 475, 296, size=16, weight=600)


@design("SEC/staying-safe-in-crowds-1")
def _(d):
    d.piece("start-or-end", 20, 20, 110)
    d.piece("start-or-end", 510, 20, 110)
    d.text("Exit", 140, 70, size=16, weight=600, anchor="start")
    d.text("Exit", 500, 70, size=16, weight=600, anchor="end")
    d.line(70, 150, 70, 320, width=4)
    d.line(570, 150, 570, 320, width=4)
    d.arrow(70, 300, 70, 170, width=3, color=GREEN)
    d.arrow(70, 160, 120, 100, width=3, color=GREEN)
    d.arrow(570, 300, 570, 170, width=3, color=GREEN)
    d.arrow(570, 160, 520, 100, width=3, color=GREEN)
    d.text("Edge lane", 86, 312, size=16, weight=600, anchor="start")
    chip(d, 320, 230, 200, 70, "Dense centre")
    d.piece("caution", 270, 100, 100)
    caption(d, "Move along the edge, never against the flow.", 345)


@design("SEC/staying-safe-in-crowds-2")
def _(d):
    d.piece("person-standing", 60, 30, 230)
    d.line(125, 226, 245, 226, dash="9 7", width=4, color=BLUE)
    d.text("Feet under body", 330, 232, size=17, weight=600, anchor="start")
    d.leader(325, 226, 250, 226)
    d.piece("bracket", 220, 95, 70)
    d.text("Arms make space", 400, 134, size=17, weight=600, anchor="start")
    d.leader(395, 128, 292, 128)
    caption(d, "Arms keep space against being squeezed.", 335)


@design("SEC/staying-safe-in-crowds-3")
def _(d):
    d.piece("start-or-end", 30, 30, 120)
    d.piece("waypoint-pin", 260, 30, 120)
    d.piece("start-or-end", 490, 30, 120)
    d.text("Exit A", 90, 150, size=16, weight=600)
    d.text("Open space", 320, 150, size=16, weight=600)
    d.text("Exit B", 550, 150, size=16, weight=600)
    d.line(160, 85, 255, 85, dash="2 9", width=5)
    d.line(385, 85, 480, 85, dash="2 9", width=5)
    d.piece("arrow-curved", 120, 190, 120)
    d.text("Gate swing", 180, 310, size=16, weight=600)
    d.piece("timeline-marker", 400, 190, 120)
    d.text("Seconds per exit", 460, 310, size=16, weight=600)


@design("SEC/staying-safe-in-crowds-4")
def _(d):
    d.piece("person-standing", 30, 40, 180)
    d.piece("child-standing", 230, 80, 130)
    d.piece("person-standing", 430, 40, 180)
    d.path("M236 70H356V215H236Z", stroke=BLUE, width=3, dash="9 7")
    d.text("Adult", 120, 215, size=16, weight=600)
    d.text("Child", 296, 240, size=16, weight=600)
    d.text("Adult", 520, 215, size=16, weight=600)
    d.line(16, 262, 624, 262, width=5)
    d.arrow(60, 296, 580, 296, width=3)
    d.text("Edge route", 320, 324, size=16, weight=600)


@design("SEC/storm-safety-1")
def _(d):
    row(d, [("room", "Interior room"), ("wall", "External wall"), ("window", "Window")], 70, w=150)
    d.piece("do", 140, 60, 56)
    d.piece("warning", 330, 60, 56)
    d.piece("warning", 510, 60, 56)
    caption(d, "Pick a room away from windows.", 320)


@design("SEC/storm-safety-2")
def _(d):
    d.piece("bucket", 16, 20, 120)
    d.text("Bin", 76, 130, size=16, weight=600)
    d.piece("shrub", 170, 20, 120)
    d.text("Pot", 230, 130, size=16, weight=600)
    d.piece("chair", 16, 180, 120)
    d.text("Chair", 76, 290, size=16, weight=600)
    d.piece("bicycle", 170, 180, 120)
    d.text("Bicycle", 230, 290, size=16, weight=600)
    d.arrow(310, 190, 430, 190, width=4)
    d.text("Bring in", 370, 170, size=16, weight=600)
    d.piece("house", 440, 110, 180)
    d.piece("caution", 325, 60, 90)
    caption(d, "Loose objects cause storm damage.", 342)


@design("SEC/storm-safety-3")
def _(d):
    row(d, [("wall", "Inside wall"), ("mattress", "Mattress"), ("window", "Window")], 70, w=150)
    d.piece("do", 330, 60, 56)
    d.piece("warning", 510, 60, 56)
    caption(d, "Shelter away from flying glass.", 320)


@design("SEC/storm-safety-4")
def _(d):
    row(d, [("chair", "Chairs"), ("bucket", "Bins"), ("shrub", "Plant pots"), ("main-switch", "Main switch")], 100, w=120)
    for i, x in enumerate((30, 190, 350, 510)):
        d.badge(i + 1, x + 20, 90, 18)
    caption(d, "Secure before the storm.", 320)


@design("SEC/the-go-bag-1")
def _(d):
    d.piece("bag", 30, 90, 190)
    d.arrow(230, 180, 290, 180, width=4)
    d.rect(300, 30, 320, 270)
    for i, s in enumerate(["Documents", "Light", "Tools", "Money", "Power bank"]):
        y = 30 + i * 54
        if i:
            d.line(300, y, 620, y, width=2)
        d.text(s, 320, y + 34, size=17, weight=600, anchor="start")
        d.tick(590, y + 27, 14)
    caption(d, "Check one group at a time.", 335)


@design("SEC/the-go-bag-2")
def _(d):
    d.piece("bag", 215, 70, 210)
    d.text("ID copies", 16, 90, size=17, weight=600, anchor="start")
    d.leader(110, 85, 265, 135)
    d.text("Insurance", 16, 250, size=17, weight=600, anchor="start")
    d.leader(110, 245, 270, 190)
    d.text("Contact copies", 624, 90, size=17, weight=600, anchor="end")
    d.leader(515, 85, 380, 135)
    d.text("Meeting point card", 624, 250, size=17, weight=600, anchor="end")
    d.leader(488, 245, 375, 190)
    caption(d, "Paper copies back up failed phones.", 335)


@design("SEC/the-go-bag-3")
def _(d):
    d.piece("bag", 200, 40, 230)
    d.line(245, 50, 245, 260, dash="9 7", width=4, color=BLUE)
    d.text("Back", 230, 160, size=16, weight=600, anchor="end")
    d.text("Light above", 490, 100, size=17, weight=600, anchor="start")
    d.leader(485, 95, 350, 100)
    d.text("Heavy low", 490, 220, size=17, weight=600, anchor="start")
    d.leader(485, 215, 350, 185)
    caption(d, "Packing order decides how the load sits.", 335)


@design("SEC/the-go-bag-4")
def _(d):
    d.piece("person-standing", 16, 60, 150)
    d.piece("child-standing", 170, 90, 110)
    d.text("Adult", 91, 200, size=16, weight=600)
    d.text("Child", 225, 210, size=16, weight=600)
    d.arrow(290, 150, 380, 150, width=4)
    d.piece("door", 390, 70, 130)
    d.text("Door", 455, 190, size=16, weight=600)
    d.piece("timeline-marker", 530, 80, 90)
    d.text("Timer", 575, 190, size=16, weight=600)
    caption(d, "Time the walk with the bag on your back.", 320)


@design("SEC/travelling-safely-in-unrest-1")
def _(d):
    d.piece("waypoint-pin", 16, 110, 100)
    d.piece("waypoint-pin", 524, 110, 100)
    d.text("Home", 66, 210, size=16, weight=600)
    d.text("Destination", 574, 210, size=16, weight=600)
    d.path("M115 150C200 40 440 40 525 150", stroke=INK, width=4)
    d.path("M115 170C200 280 440 280 525 170", stroke=INK, width=4, dash="9 7")
    d.piece("caution", 290, 40, 60)
    d.text("Route A: checkpoint", 320, 30, size=16, weight=600)
    d.piece("decision", 280, 220, 80)
    d.text("Route B: turn back", 320, 320, size=16, weight=600)


@design("SEC/travelling-safely-in-unrest-2")
def _(d):
    row(d, [("map", "Paper map"), ("note", "Written ahead"), ("decision", "Turn back"), ("hut", "Shelter")], 90, w=130, arrows=True)
    caption(d, "The decision is already made at the junction.", 320)


@design("SEC/travelling-safely-in-unrest-3")
def _(d):
    row(d, [("step-1", "Stop calmly"), ("step-2", "Hands visible"), ("step-3", "Show ID")], 80, w=150, arrows=True)
    caption(d, "Hands are seen first, before any movement.", 320)


@design("SEC/travelling-safely-in-unrest-4")
def _(d):
    d.piece("person-sitting", 30, 60, 220)
    d.text("Driver", 140, 260, size=16, weight=600)
    d.piece("table-grid", 300, 130, 160)
    d.text("Dashboard", 380, 280, size=16, weight=600)
    chip(d, 380, 60, 80, 40, "ID")
    d.arrow(380, 84, 380, 130, width=3)
    d.piece("tip", 500, 120, 110)
    d.text("Ready before\nthe officer", 555, 240, size=16, weight=600)
