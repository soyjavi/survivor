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


def snake(d, labels, numbered=0, y1=90, y2=210):
    w, h = 150, 56
    xs = [100, 320, 540]
    pos = [(xs[i], y1) for i in range(3)] + [(xs[i], y2) for i in range(3)]
    pos = pos[: len(labels)]
    for i, ((cx, cy), s) in enumerate(zip(pos, labels)):
        chip(d, cx, cy, w, h, s)
        if i < numbered:
            d.badge(i + 1, cx - w / 2, cy - h / 2, r=15)
    for i in range(len(pos) - 1):
        (ax, ay), (bx, by) = pos[i], pos[i + 1]
        if ay == by:
            d.arrow(ax + w / 2 + 4, ay, bx - w / 2 - 4, by)
        else:
            my = (ay + by) / 2
            d.path(f"M{ax} {ay + h / 2 + 4}V{my}H{bx}V{by - h / 2 - 16}", stroke=INK, width=4)
            d.curve_arrow(f"M{bx} {by - h / 2 - 16}L{bx} {by - h / 2 - 4}", (bx, by - h / 2 - 4), math.pi / 2)


def rowtable(d, x, y, w, rh, labels, hw, fill_head=SAND, size=16, lines=True):
    for i, s in enumerate(labels):
        yy = y + i * rh
        d.rect(x, yy, hw, rh, fill=fill_head, rx=0)
        n = s.count("\n")
        d.text(s, x + hw / 2, yy + rh / 2 + size * 0.35 - n * size * 0.6, size=size, weight=600)
        d.rect(x + hw, yy, w - hw, rh, fill=CREAM, rx=0)
        if lines:
            d.line(x + hw + 14, yy + rh / 2 + 6, x + w - 14, yy + rh / 2 + 6, width=1.5, color=SAND)


def coltable(d, x, y, cw, rh, cols, rows, hw=0, size=16):
    for j, s in enumerate(cols):
        d.rect(x + hw + j * cw, y, cw, rh, fill=SAND, rx=0)
        d.text(s, x + hw + j * cw + cw / 2, y + rh / 2 + size * 0.35, size=size, weight=600)
    for i, r in enumerate(rows):
        yy = y + (i + 1) * rh
        if hw:
            d.rect(x, yy, hw, rh, fill=SAND, rx=0)
            d.text(r, x + hw / 2, yy + rh / 2 + size * 0.35, size=size, weight=600)
        for j in range(len(cols)):
            d.rect(x + hw + j * cw, yy, cw, rh, fill=CREAM, rx=0)


@design("COM/battery-radio-and-information-1")
def _(d):
    d.piece("radio", 20, 20, 360)
    for ty, tx, ty2, s in [(137, 205, 100, "AM/FM dial"), (175, 262, 180, "Torch"), (238, 225, 260, "Phone port")]:
        d.leader(420, ty2 - 6, tx, ty)
        d.text(s, 430, ty2, size=17, weight=600, anchor="start")
    caption(d, "Each control has one use: the set runs without a grid.")


@design("COM/battery-radio-and-information-3")
def _(d):
    chip(d, 90, 150, 120, 56, "Crank")
    d.arrow(154, 150, 240, 150)
    d.piece("battery", 235, 90, 200)
    d.text("Internal cell", 335, 250, size=16, weight=600)
    d.curve_arrow("M390 118C400 30 270 30 280 112", (280, 112), math.pi / 2, width=4)
    d.arrow(430, 150, 480, 150)
    chip(d, 550, 150, 120, 56, "Indicator")
    caption(d, "Cranking charges the cell; the indicator shows enough is stored.")


@design("COM/battery-radio-and-information-4")
def _(d):
    d.piece("tin", 5, 50, 190)
    d.text("Dry box", 100, 212, size=16, weight=600)
    d.piece("bag", 195, 50, 190)
    d.text("Spare cells", 290, 212, size=16, weight=600)
    d.line(410, 50, 410, 270, dash="9 7", width=3)
    d.piece("radio", 430, 40, 200)
    d.text("Radio", 530, 212, size=16, weight=600)
    chip(d, 290, 260, 130, 40, "Test date")
    caption(d, "Batteries sit apart from the radio so a leak cannot reach it.")


@design("COM/charging-batteries-without-a-grid-1")
def _(d):
    for i, (p, s) in enumerate([('solar-panel', 'Solar panel'), ('charge-controller', 'Controller'), ('battery', 'Battery')]):
        cx = 80 + i * 155
        d.piece(p, cx - 75, 90, 150)
        d.text(s, cx, 235, size=16, weight=600)
        d.arrow(cx + 60, 150, cx + 100 if i < 2 else 515, 150)
    chip(d, 575, 150, 100, 56, 'Device')
    caption(d, 'The controller regulates before storage.')


@design("COM/charging-batteries-without-a-grid-2")
def _(d):
    for i, (p, s) in enumerate([('crank-handle', 'Crank handle'), ('gear-train', 'Gear train'), ('generator-core', 'Generator core')]):
        cx = 80 + i * 155
        d.piece(p, cx - 75, 90, 150)
        d.text(s, cx, 235, size=16, weight=600)
        d.arrow(cx + 60, 150, cx + 100 if i < 2 else 515, 150)
    chip(d, 575, 150, 100, 56, 'USB output')
    caption(d, 'Slow cranking still gives a short charge.')


@design("COM/charging-batteries-without-a-grid-3")
def _(d):
    d.piece("sun", 20, 0, 100)
    d.piece("solar-panel", 10, 80, 200)
    d.text("Panel", 112, 250, size=16, weight=600)
    d.piece("charge-controller", 270, 10, 150)
    d.text("Controller", 460, 70, size=16, weight=600, anchor="start")
    d.piece("battery", 270, 160, 160)
    d.text("Battery", 460, 225, size=16, weight=600, anchor="start")
    d.line(185, 140, 290, 70, width=3)
    d.line(350, 106, 350, 192, width=3)
    d.text("Cable", 150, 70, size=16, weight=600)
    d.leader(175, 78, 235, 105)
    d.text("Cable", 400, 150, size=16, weight=600, anchor="start")
    d.leader(396, 144, 354, 150)
    caption(d, "The controller sits apart from the battery: short, dry cables.", 345)


@design("COM/charging-batteries-without-a-grid-4")
def _(d):
    for i, (p, s) in enumerate([('solar-panel', 'Solar input'), ('charge-controller', 'Controller'), ('battery', 'Battery terminals')]):
        cx = 80 + i * 155
        d.piece(p, cx - 75, 90, 150)
        d.text(s, cx, 235, size=16, weight=600)
        d.arrow(cx + 60, 150, cx + 100 if i < 2 else 515, 150)
    chip(d, 575, 150, 100, 56, 'Load\noutputs')
    caption(d, 'Power flows in order from source to device.')


@design("COM/community-notice-boards-1")
def _(d):
    labs = ["Official news", "Requests", "Offers", "Lost and found", "Meetings"]
    for i, s in enumerate(labs):
        y = 30 + i * 56
        d.rect(150, y, 340, 56, fill=SAND if i == 0 else CREAM, rx=0)
        d.text(s, 320, y + 35, size=18, weight=600)
    d.badge(1, 120, 58)
    d.arrow(560, 300, 560, 40, width=3)
    d.text("Read first", 560, 330, size=15)
    caption(d, "Official news sits highest so it is read first.", 346)


@design("COM/community-notice-boards-2")
def _(d):
    rowtable(d, 120, 40, 400, 52, ["Date", "Source", "Text", "Contact", "Removal date"], 150, size=17)
    caption(d, "Every notice carries source and expiry.")


@design("COM/community-notice-boards-3")
def _(d):
    snake(d, ["Write", "Source", "Contact", "Date", "Read aloud", "Pin"], numbered=3)
    caption(d, "The spoken test comes before pinning.")


@design("COM/community-notice-boards-4")
def _(d):
    d.text("Before", 150, 40, size=18, weight=700)
    for i in range(4):
        d.rect(40, 60 + i * 52, 220, 44, fill=GREY, rx=0, dash="6 5")
    d.cross(150, 290, 16)
    d.arrow(285, 170, 345, 170)
    d.text("After", 490, 40, size=18, weight=700)
    for i in range(4):
        d.rect(380, 60 + i * 52, 220, 44, fill=CREAM, rx=0)
        d.text("Date", 400, 88 + i * 52, size=15, anchor="start")
    d.piece("do", 460, 258, 60)
    caption(d, "Refreshing is a daily removal step.", 340)


@design("COM/digital-safety-in-a-crisis-1")
def _(d):
    rows = [(None, "Strong password", True), ("two-factor-code", "Two-factor code", True), (None, "Suspicious link", False), ("phone-call", "Verified number", True)]
    for i, (p, s, ok) in enumerate(rows):
        y = 24 + i * 74
        d.rect(150, y, 360, 60, rx=10)
        d.text(s, 170, y + 38, size=18, weight=600, anchor="start")
        if p:
            d.piece(p, 40, y - 14, 90, 90)
        (d.tick if ok else d.cross)(570, y + 30, 20)
    caption(d, "Keep the ticked items and refuse the crossed one.")


@design("COM/digital-safety-in-a-crisis-2")
def _(d):
    d.piece("info", 5, 80, 150)
    d.text("Suspicious\nmessage", 80, 215, size=16, weight=600)
    d.arrow(125, 150, 190, 150)
    d.piece("do-not", 175, 90, 120)
    d.text("Stop", 235, 215, size=16, weight=600)
    d.arrow(285, 150, 330, 150)
    d.piece("phone-call", 305, 70, 160)
    d.text("Verify call", 385, 215, size=16, weight=600)
    d.arrow(440, 150, 495, 150)
    chip(d, 565, 150, 110, 64, "Authority's\nlist")
    caption(d, "Call the authority's own number, not the one in the message.")


@design("COM/digital-safety-in-a-crisis-3")
def _(d):
    d.rect(170, 30, 300, 270, rx=24)
    d.text("Phone", 320, 66, size=20, weight=700)
    chip(d, 320, 130, 220, 56, "Device lock")
    d.line(190, 180, 450, 180, dash="9 7", width=3)
    chip(d, 320, 230, 220, 56, "Account protection")
    caption(d, "Two independent layers.")


@design("COM/digital-safety-in-a-crisis-4")
def _(d):
    d.text("Owner", 160, 40, size=20, weight=700)
    d.piece("person-standing", 60, 40, 200, 150)
    chip(d, 160, 245, 200, 50, "Private accounts")
    d.line(320, 20, 320, 310, dash="9 7", width=3)
    d.text("Guest", 480, 40, size=20, weight=700)
    chip(d, 480, 130, 200, 50, "Logins")
    d.piece("do-not", 420, 150, 120)
    d.text("No saved logins", 480, 290, size=17, weight=600)
    caption(d, "Guests cannot reach owner data.")


@design("COM/emergency-broadcasts-1")
def _(d):
    d.piece("ladder", 30, 20, 260, 300)
    for ty, s in [(112, "Evacuation order"), (165, "Warning"), (214, "Watch")]:
        d.text(s, 360, ty + 6, size=19, weight=600, anchor="start")
        d.leader(350, ty, 200, ty)
    d.arrow(600, 290, 600, 60, width=3)
    d.text("Urgency", 600, 40, size=14)
    caption(d, "Prepare, then act now, then leave.")


@design("COM/emergency-broadcasts-2")
def _(d):
    d.piece("radio", 20, 90, 200)
    d.arrow(215, 170, 270, 170, width=3)
    for i in range(3):
        d.rect(280, 70 + i * 70, 130, 60, rx=0)
        d.text(["Who", "Where", "What"][i], 345, 107 + i * 70, size=16)
    for i, s in enumerate(["Issuing authority", "Named area", "Required action"]):
        y = 107 + i * 70
        d.leader(432, y - 6, 412, y - 6)
        d.text(s, 440, y, size=16, weight=600, anchor="start")
    caption(d, "Match the area to your address before acting.")


@design("COM/emergency-broadcasts-3")
def _(d):
    snake(d, ["Opening tone", "Issuing authority", "Named area", "Instruction", "Repeat aloud", "Written record"], numbered=3)
    caption(d, "The listener repeats and writes the alert first.")


@design("COM/emergency-broadcasts-4")
def _(d):
    labs = ["Note the time", "Note the area", "Act", "Tell neighbours", "Keep listening"]
    for i, s in enumerate(labs):
        y = 40 + i * 52
        chip(d, 300, y, 220, 40, s)
        d.tick(150, y, 14)
    d.path("M412 248H470V140H412", stroke=INK, width=4)
    d.curve_arrow("M412 140L420 140", (410, 140), math.pi)
    d.text("Updates\narrive", 480, 190, size=15, anchor="start")


@design("COM/family-communication-plan-1")
def _(d):
    rowtable(d, 100, 36, 440, 66, ["Contact list", "Out-of-area\ncontact", "Three meeting\npoints", "Medical notes"], 170, size=17)
    caption(d, "Everything needed to reconnect fits on one page.")


@design("COM/family-communication-plan-2")
def _(d):
    d.rect(100, 40, 440, 250, rx=20)
    for i, s in enumerate(["Name", "Meeting point", "Out-of-area number"]):
        y = 110 + i * 70
        d.text(s, 130, y, size=26, weight=700, anchor="start")
        d.line(130, y + 14, 510, y + 14, width=2, color=SAND)
    caption(d, "Only the three items needed for collection.")


@design("COM/family-communication-plan-3")
def _(d):
    for i, s in enumerate(["Contacts", "Meeting\npoints", "Medical\nnotes"]):
        x = 20 + i * 205
        d.rect(x, 50, 190, 240, rx=12)
        d.rect(x, 50, 190, 64, fill=SAND, rx=12)
        d.text(s, x + 95, 78 if "\n" in s else 88, size=18, weight=700)
        for k in range(3):
            d.line(x + 18, 160 + k * 40, x + 172, 160 + k * 40, width=1.5, color=SAND)
    caption(d, "Each box is a separate section.")


@design("COM/family-communication-plan-4")
def _(d):
    d.arrow(30, 150, 614, 150, width=4)
    labs = ["Separation", "Nearest\nmeeting point", "Waiting\nperiod", "Out-of-area\ncall", "Reunion"]
    for i, s in enumerate(labs):
        x = 70 + i * 125
        d.piece("timeline-marker", x - 36, 75, 120)
        d.text(s, x, 215, size=16, weight=600)
    caption(d, "The report-in call comes after reaching the meeting point.")


@design("COM/keeping-a-crisis-log-1")
def _(d):
    coltable(d, 40, 60, 93, 50, ["Date", "Water", "Food", "Fuel", "Medicines", "Events"], ["", "", "", ""], size=15)
    caption(d, "One row per day; read down a column to see supply fall.")


@design("COM/keeping-a-crisis-log-2")
def _(d):
    rowtable(d, 70, 30, 500, 52, ["Date and weather", "Stock counts", "Medicine dose\nand recipient", "Events", "Initials"], 210, size=16)
    d.tick(530, 30 + 4 * 52 + 26, 16)
    caption(d, "Complete only once initialled.", 340)


@design("COM/keeping-a-crisis-log-3")
def _(d):
    d.text("Entry", 240, 50, size=17, weight=700)
    d.text("Unconfirmed", 505, 50, size=17, weight=700)
    for i in range(3):
        y = 66 + i * 70
        d.rect(60, y, 360, 62, rx=0)
        d.rect(420, y, 150, 62, rx=0)
        d.line(80, y + 36, 400, y + 36, width=1.5, color=SAND)
    d.rect(56, 62 + 70, 518, 70, fill="none", stroke=YELLOW, width=4, rx=0, dash="9 7")
    d.piece("caution", 470, 144, 70)
    caption(d, "Unverified items stay visible and flagged, not deleted.")


@design("COM/keeping-a-crisis-log-4")
def _(d):
    coltable(d, 70, 50, 120, 52, ["Day 1", "Day 2", "Day 3"], ["Water", "Food", "Fuel", "Medicine"], hw=140, size=17)
    caption(d, "The rate of use shows a stock running low.")


@design("COM/meeting-points-1")
def _(d):
    d.piece("person-standing", 235, 120, 110, 120)
    d.text("Home", 290, 262, size=17, weight=600)
    d.piece("waypoint-pin", 40, 30, 80)
    d.arrow(250, 150, 125, 100, width=3)
    d.text("Near home", 80, 120, size=16, weight=600)
    d.piece("waypoint-pin", 280, 0, 80)
    d.arrow(295, 140, 318, 70, width=3)
    d.text("Outside neighbourhood", 360, 40, size=16, weight=600, anchor="start")
    d.piece("waypoint-pin", 500, 140, 80)
    d.arrow(340, 180, 510, 178, width=3)
    d.text("Further away", 540, 235, size=16, weight=600)
    caption(d, "One blocked route still leaves another.")


@design("COM/meeting-points-2")
def _(d):
    d.arrow(30, 190, 614, 190, width=4)
    xs = [70, 230, 390, 550]
    labs = ["Home", "Stop 1", "Stop 2", "Stop 3"]
    for x, s in zip(xs, labs):
        d.piece("timeline-marker", x - 36, 115, 120)
        d.text(s, x, 250, size=16, weight=600)
    for a, b in zip(xs, xs[1:]):
        m = (a + b) / 2
        d.piece("footprints", m - 45, 50, 90)
        d.text("__ min", m + 28, 150, size=15)
    d.text("Landmark per stop", 320, 290, size=16, weight=600)
    caption(d, "Times add up: total travel time is known before a real trip.")


@design("COM/meeting-points-3")
def _(d):
    for i in range(3):
        x = 20 + i * 205
        d.rect(x, 60, 190, 220, rx=12)
        for k, s in enumerate(["Name", "Time", "Next destination"]):
            y = 60 + k * 73
            d.rect(x, y, 190, 34, fill=SAND, rx=0)
            d.text(s, x + 95, y + 23, size=15, weight=700)
            d.line(x + 14, y + 58, x + 176, y + 58, width=1.5, color=SAND)
    caption(d, "Each card shows where a person went next.")


@design("COM/meeting-points-4")
def _(d):
    d.piece("waypoint-pin", 0, 90, 100)
    d.text("Home", 50, 92, size=16, weight=600)
    d.piece("waypoint-pin", 270, 40, 100)
    d.text("Meeting points", 320, 40, size=16, weight=600)
    d.piece("waypoint-pin", 540, 90, 100)
    d.line(85, 140, 295, 110, width=4)
    d.line(345, 110, 565, 140, width=4)
    d.text("Main route", 190, 98, size=16, weight=600)
    d.path("M60 200C200 320 450 320 590 200", stroke=INK, width=3, dash="9 7")
    d.text("Alternative", 320, 312, size=16, weight=600)
    caption(d, "The dashed route is the fallback when the main is blocked.")


@design("COM/message-relays-and-runners-1")
def _(d):
    rowtable(d, 120, 22, 400, 46, ["Number", "Sender", "Recipient", "Time", "Place", "Text"], 150, size=17)
    caption(d, "The recipient's name is outside the message text.")


@design("COM/message-relays-and-runners-2")
def _(d):
    for i in range(3):
        y = 20 + i * 90
        d.piece("person-standing", 20, y, 90, 76)
        d.text(f"Runner {i + 1}", 65, y + 84, size=14, weight=600)
        d.arrow(115, y + 40, 235, y + 40, width=3)
        d.piece("waypoint-pin", 240, y + 6, 66, 60)
    d.text("Rest points", 273, 322, size=15, weight=600)
    d.text("Timetable", 530, 40, size=17, weight=700)
    for i in range(3):
        d.rect(430, 56 + i * 80, 190, 64, rx=0)
        d.text(f"Runner {i + 1}", 445, 94 + i * 80, size=16, anchor="start")
    caption(d, "Each runner has one route.", 346)


@design("COM/offline-maps-and-information-1")
def _(d):
    d.piece("waypoint-pin", 20, 100, 100)
    d.text("Home", 70, 190, size=16, weight=600)
    d.piece("waypoint-pin", 500, 30, 100)
    d.text("Meeting points", 550, 125, size=16, weight=600)
    d.piece("water-drop", 230, 190, 100)
    d.text("Water", 280, 285, size=16, weight=600)
    d.piece("tent", 480, 170, 130)
    d.text("Shelter", 545, 280, size=16, weight=600)
    d.arrow(105, 125, 500, 90, width=4)
    d.text("Planned route", 300, 90, size=16, weight=600)
    d.path("M112 182C140 245 200 245 235 240", stroke=INK, width=3, dash="9 7")
    d.arrow(330, 238, 480, 238, width=3, dash="9 7")
    d.text("Alternative", 400, 270, size=16, weight=600)
    caption(d, "One route is planned, the other the alternative.")


@design("COM/offline-maps-and-information-2")
def _(d):
    d.rect(60, 30, 520, 270, rx=18, fill=CREAM)
    items = [("water-drop", "Water"), ("tent", "Shelter"), ("waypoint-pin", "Meeting point"), ("first-aid-kit", "First aid")]
    for i, (p, s) in enumerate(items):
        x = 90 + (i % 2) * 250
        y = 50 + (i // 2) * 125
        d.piece(p, x, y, 100)
        d.text(s, x + 115, y + 52, size=18, weight=600, anchor="start")
    caption(d, "One symbol set everywhere: any pencil mark reads the same.")


@design("COM/offline-maps-and-information-3")
def _(d):
    chip(d, 320, 60, 160, 50, "Guides", fill=SAND)
    d.line(320, 85, 320, 130, width=3)
    d.line(76, 130, 564, 130, width=3)
    for i, s in enumerate(["Water", "First aid", "Fire", "Shelter", "Maps"]):
        cx = 76 + i * 122
        d.line(cx, 130, cx, 175, width=3)
        chip(d, cx, 200, 108, 50, s)
    caption(d, "The key guides sit at top level.")


@design("COM/offline-maps-and-information-4")
def _(d):
    ox, oy = 150, 280
    d.arrow(ox, oy, ox, 60, width=4)
    d.text("North", ox, 42, size=17, weight=600)
    d.arrow(ox, oy, ox + 270 * math.sin(math.radians(40)), oy - 270 * math.cos(math.radians(40)), width=4)
    d.text("Route", ox + 285 * math.sin(math.radians(40)), oy - 285 * math.cos(math.radians(40)), size=17, weight=600, anchor="start")
    r = 110
    ex, ey = ox + r * math.sin(math.radians(40)), oy - r * math.cos(math.radians(40))
    d.path(f"M{ox} {oy - r}A{r} {r} 0 0 1 {ex:.1f} {ey:.1f}", stroke=BLUE, width=3)
    d.text("Bearing", ox + 30, oy - 135, size=16, weight=600, fill=BLUE, anchor="start")
    d.piece("compass", 420, 140, 200)
    caption(d, "The bearing is measured from north.")


@design("COM/passwords-and-accounts-1")
def _(d):
    rowtable(d, 30, 40, 400, 52, ["Account name", "Username", "Recovery contact", "Codes location", "Sealed envelope"], 170, size=16)
    d.piece("envelope", 450, 190, 150)
    d.leader(432, 266, 470, 266)
    caption(d, "Routes back in, never passwords.")


@design("COM/passwords-and-accounts-2")
def _(d):
    snake(d, ["Log in", "Confirm recovery", "Generate codes", "Date sheet", "Seal envelope"], numbered=3)
    caption(d, "Dating and sealing come last.")


@design("COM/passwords-and-accounts-3")
def _(d):
    d.rect(30, 50, 580, 220, rx=16, fill=PAPER)
    d.text("Account", 320, 84, size=19, weight=700)
    for i, s in enumerate(["Password", "Phone code", "Paper backup\ncode"]):
        chip(d, 125 + i * 195, 170, 160, 70, s)
    d.piece("do-not", 325, 95, 90)
    d.text("Phone lost", 320, 240, size=16, weight=600, fill=RED)
    caption(d, "The paper code still works.")


@design("COM/phone-use-with-a-limited-battery-1")
def _(d):
    for i, s in enumerate(["Airplane mode", "Lowered brightness", "Background data off"]):
        y = 70 + i * 80
        chip(d, 300, y, 300, 58, s, size=18)
        d.tick(500, y, 18)
    caption(d, "Three switches cut the largest drains; each takes seconds.")


@design("COM/phone-use-with-a-limited-battery-2")
def _(d):
    labs = [("Morning check", CREAM, 56), ("Short messages", CREAM, 56), ("One reserve call", YELLOW, 70), ("The rest saved", CREAM, 100)]
    y = 30
    for s, f, h in labs:
        d.rect(200, y, 160, h, fill=f, rx=0)
        d.text(s, 380, y + h / 2 + 6, size=17, weight=600, anchor="start")
        y += h
    caption(d, "The reserve is a fixed slice, not what is left over.")


@design("COM/phone-use-with-a-limited-battery-3")
def _(d):
    d.piece("airplane-mode", 40, 80, 170)
    d.text("Airplane mode", 125, 230, size=17, weight=600)
    d.arrow(225, 140, 330, 140)
    d.piece("battery", 345, 80, 170)
    d.text("Battery level", 430, 230, size=17, weight=600)
    caption(d, "Stay in airplane mode between uses; the level says when to stop.")
