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


def lab(d, s, x, y, size=16, anchor="middle", fill=INK):
    d.text(s, x, y, size=size, weight=600, anchor=anchor, fill=fill)


def flow(d, items, y, w=130, arrow=True, label_dy=26):
    n = len(items)
    gap = (640 - n * w) / (n + 1)
    for i, (piece, label) in enumerate(items):
        x = gap + i * (w + gap)
        d.piece(piece, x, y, w)
        d.text(label, x + w / 2, y + w * 0.75 + label_dy, size=16, weight=600)
        if arrow and i < n - 1:
            d.arrow(x + w + 4, y + w * 0.375, x + w + gap - 4, y + w * 0.375)


@design("NAV/evacuation-routes-1")
def _(d):
    d.piece("waypoint-pin", 24, 120, 100)
    lab(d, "Home", 74, 236)
    d.arrow(128, 190, 200, 190)
    d.piece("river", 205, 135, 150)
    d.piece("warning", 262, 100, 44)
    lab(d, "Hazard", 280, 266)
    d.arrow(360, 180, 470, 100)
    chip(d, 545, 90, 130, 44, "Primary")
    d.arrow(360, 200, 470, 280)
    chip(d, 545, 280, 130, 44, "Secondary")
    caption(d, "Same first road means not two routes.")


@design("NAV/evacuation-routes-2")
def _(d):
    d.piece("car", 210, 0, 220)
    d.piece("bottle", 40, 210, 90)
    lab(d, "Water", 85, 316)
    d.piece("flashlight", 150, 210, 90)
    lab(d, "Torch", 195, 316)
    d.piece("first-aid-kit", 260, 210, 90)
    lab(d, "Kit", 305, 316)
    d.piece("map", 370, 210, 90)
    lab(d, "Map", 415, 316)
    chip(d, 540, 235, 130, 40, "Documents")
    chip(d, 540, 290, 130, 40, "Fuel")
    d.line(305, 222, 305, 210, width=3, dash="9 7", color=BLUE)
    d.line(305, 210, 620, 210, width=3, dash="9 7", color=BLUE)
    d.line(620, 210, 620, 290, width=3, dash="9 7", color=BLUE)
    d.arrow(620, 290, 607, 290, width=3, color=BLUE)
    lab(d, "Checked together", 460, 200, size=15, fill=BLUE)


@design("NAV/evacuation-routes-3")
def _(d):
    d.piece("trail-marker", 220, 50, 200)
    d.arrow(420, 100, 500, 100)
    chip(d, 560, 100, 110, 40, "Primary", size=15)
    d.piece("do-not", 436, 78, 44)
    lab(d, "Closed", 458, 68, size=15)
    d.arrow(290, 200, 170, 262)
    chip(d, 110, 280, 120, 40, "Secondary", size=15)
    caption(d, "The fallback leaves from a different junction.")


@design("NAV/finding-north-without-a-compass-1")
def _(d):
    chip(d, 200, 240, 130, 60, "Watch")
    d.piece("sun", 440, 60, 130)
    d.arrow(265, 215, 440, 140)
    lab(d, "Hour hand to sun", 400, 215, size=15)
    d.line(200, 208, 200, 120, dash="9 7", width=3, color=BLUE)
    d.piece("north-arrow", 150, 30, 100)
    lab(d, "Midpoint to 12", 188, 170, size=15, anchor="end", fill=BLUE)
    lab(d, "South", 200, 310)
    caption(d, "The midpoint line gives direction.", 346)


@design("NAV/finding-north-without-a-compass-2")
def _(d):
    d.line(16, 290, 624, 290, width=4)
    d.piece("shadow-stick", 70, 160, 170)
    d.piece("waypoint-pin", 176, 226, 60)
    d.piece("waypoint-pin", 380, 226, 60)
    lab(d, "First tip", 205, 322, size=15)
    lab(d, "Second tip\n15-20 min", 410, 322, size=15)
    d.arrow(225, 272, 395, 272, width=4)
    lab(d, "West", 40, 250)
    lab(d, "East", 596, 250)
    d.arrow(100, 235, 60, 235, width=3)
    d.arrow(480, 235, 570, 235, width=3)
    d.text("Level ground needed", 320, 110, size=16, weight=600)


@design("NAV/finding-north-without-a-compass-3")
def _(d):
    d.piece("north-star", 400, 20, 110)
    lab(d, "North Star", 455, 150, size=15)
    d.piece("big-dipper", 120, 90, 200)
    lab(d, "Big Dipper", 220, 230, size=15)
    d.line(16, 290, 624, 290, width=4)
    d.arrow(292, 168, 468, 50, dash="9 7", width=3, color=BLUE)
    d.arrow(455, 172, 455, 280, width=4)
    lab(d, "North", 455, 316)
    caption(d, "The pointer line gives a fixed bearing.", 330)


@design("NAV/finding-north-without-a-compass-4")
def _(d):
    d.piece("southern-cross", 180, 20, 220)
    lab(d, "Southern Cross", 316, 215, size=15, anchor="start")
    d.line(298, 152, 298, 290, width=3, dash="9 7", color=BLUE)
    d.line(16, 290, 624, 290, width=4)
    d.arrow(290, 312, 480, 312, width=4)
    lab(d, "South", 540, 318, anchor="start")
    caption(d, "South only in the southern hemisphere.", 346)


@design("NAV/grid-references-on-paper-1")
def _(d):
    d.piece("map", 190, 40, 260)
    d.piece("table-grid", 270, 95, 100)
    d.badge(1, 100, 262, 16)
    lab(d, "Easting", 100, 302, size=15)
    d.leader(118, 262, 308, 200)
    d.badge(2, 100, 110, 16)
    lab(d, "Northing", 100, 150, size=15)
    d.leader(118, 112, 275, 140)
    d.piece("bracket", 450, 85, 90)
    lab(d, "Tenths", 545, 140, anchor="start")
    caption(d, "Easting first, then northing, each with tenths.")


@design("NAV/grid-references-on-paper-2")
def _(d):
    d.piece("map", 190, 40, 260)
    d.piece("table-grid", 270, 95, 100)
    d.leader(110, 300, 300, 190)
    chip(d, 80, 310, 120, 36, "Easting", size=15)
    d.leader(110, 110, 275, 140)
    chip(d, 80, 90, 120, 36, "Northing", size=15)
    d.rect(470, 90, 150, 120, fill=CREAM)
    d.badge(1, 495, 120, 14)
    lab(d, "Easting pair", 515, 126, size=15, anchor="start")
    d.badge(2, 495, 170, 14)
    lab(d, "Northing pair", 515, 176, size=15, anchor="start")
    caption(d, "Six-figure reference in pairs.")


@design("NAV/grid-references-on-paper-3")
def _(d):
    rows = [("4 figures", 110, "1 km"), ("6 figures", 75, "100 m"), ("8 figures", 45, "10 m")]
    for i, (t, w, u) in enumerate(rows):
        y = 70 + i * 90
        chip(d, 110, y, 130, 40, t)
        d.arrow(185, y, 300, y, width=3)
        d.piece("table-grid", 320, y - w * 0.375, w)
        lab(d, u, 480, y + 6, anchor="start")
    d.arrow(580, 50, 580, 280, width=3)
    lab(d, "Tenfold", 580, 308, size=15)
    caption(d, "Each extra pair shrinks the square tenfold.")


@design("NAV/grid-references-on-paper-4")
def _(d):
    d.piece("person-standing", 20, 90, 150)
    d.piece("phone-call", 100, 60, 80)
    d.piece("map", 200, 110, 150)
    d.piece("table-grid", 245, 140, 60)
    d.leader(300, 60, 275, 150)
    lab(d, "Easting", 300, 52, size=15, anchor="start")
    d.leader(420, 190, 300, 165)
    chip(d, 470, 200, 100, 36, "Northing", size=15)
    d.rect(480, 80, 140, 60, fill=CREAM)
    lab(d, "Pairs:", 550, 105, size=15)
    lab(d, "east, then north", 550, 127, size=14)
    caption(d, "Say the reference in pairs.")


@design("NAV/if-you-are-lost-1")
def _(d):
    flow(d, [("start-or-end", "Lost"), ("step-1", "Stop"), ("step-2", "Check"), ("signal-fires-3", "Signal")], 100, w=125)
    caption(d, "Signal before walking.", 300)


@design("NAV/if-you-are-lost-2")
def _(d):
    d.line(30, 230, 610, 230, width=4)
    xs = [50, 170, 300, 440, 590]
    for x, t in zip(xs, ["0", "5", "15", "30", "60 min"]):
        d.line(x, 218, x, 242, width=3)
        lab(d, t, x, 268, size=15)
    for i, t in enumerate(["Stop", "Check", "Shelter", "Signal"]):
        cx = (xs[i] + xs[i + 1]) / 2
        chip(d, cx, 160, 100, 40, t, size=15)
    caption(d, "Shelter is finished before the signal goes up.")


@design("NAV/if-you-are-lost-3")
def _(d):
    d.piece("signal-fires-3", 150, 70, 260)
    lab(d, "Three fires", 280, 60)
    d.arrow(215, 275, 345, 275, width=3)
    d.arrow(345, 275, 215, 275, width=3)
    lab(d, "Equal spacing", 280, 310, size=15)
    d.piece("cloth", 470, 130, 110)
    lab(d, "Cloth", 525, 250)
    caption(d, "Three of anything reads as human-made.", 346)


@design("NAV/if-you-are-lost-4")
def _(d):
    d.piece("arrow-loop", 40, 70, 160)
    d.piece("footprints", 85, 105, 70)
    d.cross(120, 40, 18)
    lab(d, "Circling", 120, 250)
    d.piece("waypoint-pin", 330, 110, 90)
    lab(d, "Last known point", 375, 250, size=15)
    d.arrow(430, 160, 600, 160, width=4)
    d.tick(515, 125, 18)
    lab(d, "Straight", 515, 200)
    caption(d, "Loops waste energy while the search area grows.")


@design("NAV/leaving-a-flood-area-1")
def _(d):
    d.arrow(120, 300, 120, 140, width=3)
    d.arrow(120, 140, 120, 300, width=3)
    for y, t in [(264, "6 in"), (228, "12 in"), (157, "2 ft")]:
        d.line(112, y, 128, y, width=3)
        lab(d, t, 100, y + 5, anchor="end")
        d.line(140, y, 210, y, dash="9 7", width=3, color=BLUE)
    d.piece("waves", 190, 52, 380)
    d.piece("car", 290, 40, 160)
    d.line(16, 300, 624, 300, width=4)
    caption(d, "Deeper water takes your footing, then a car.", 340)


@design("NAV/leaving-a-flood-area-2")
def _(d):
    d.piece("river", 30, 90, 170)
    lab(d, "River", 115, 215)
    chip(d, 115, 270, 100, 38, "Low", size=15)
    d.arrow(210, 150, 400, 150, width=4)
    lab(d, "Route", 305, 135)
    d.piece("slope", 410, 80, 200)
    lab(d, "High ground", 510, 270)
    caption(d, "Away from the water means uphill.")


@design("NAV/leaving-a-flood-area-3")
def _(d):
    d.line(16, 280, 624, 280, width=4)
    d.piece("person-standing", 40, 196, 130)
    lab(d, "High edge", 100, 312, size=15)
    d.piece("shadow-stick", 170, 191, 130)
    d.piece("waves", 300, 202, 120)
    lab(d, "Shallow", 360, 312, size=15)
    d.piece("river", 450, 186, 150)
    d.piece("do-not", 500, 168, 50)
    lab(d, "Moving channel", 525, 312, size=15)
    caption(d, "Stay on the higher edge.", 346)


@design("NAV/map-and-compass-basics-1")
def _(d):
    flow(d, [("step-1", "Orient map"), ("step-2", "Align edge"), ("step-3", "Turn bezel"), ("compass", "Read index")], 90, w=125)
    caption(d, "Set the bearing on the map before you turn.", 300)


@design("NAV/map-and-compass-basics-2")
def _(d):
    d.piece("compass", 190, 60, 260)
    chip(d, 90, 90, 140, 36, "Bezel", size=15)
    d.leader(160, 96, 250, 140)
    chip(d, 90, 220, 140, 36, "Needle", size=15)
    d.leader(160, 216, 309, 190)
    chip(d, 550, 80, 150, 36, "Graduated edge", size=15)
    d.leader(475, 92, 393, 152)
    d.piece("direction-of-travel", 450, 140, 80)
    lab(d, "Travel\narrow", 490, 250, size=15)
    d.piece("north-arrow", 540, 140, 80)
    lab(d, "Orienting\narrow", 580, 250, size=15)
    caption(d, "Needle sits inside the orienting arrow.", 340)


@design("NAV/map-and-compass-basics-3")
def _(d):
    d.piece("map", 20, 100, 270)
    d.piece("north-arrow", 130, 10, 70)
    lab(d, "Grid north", 185, 52, anchor="start", size=15)
    d.piece("compass", 360, 80, 250)
    d.arrow(300, 210, 350, 210, width=3)
    chip(d, 440, 40, 120, 36, "Bezel", size=15)
    d.leader(440, 58, 470, 150)
    chip(d, 450, 300, 120, 36, "Needle", size=15)
    d.leader(450, 282, 480, 220)
    caption(d, "The map grid is the reference.", 346)


@design("NAV/map-and-compass-basics-4")
def _(d):
    pts = [(80, 70), (300, 45), (520, 70)]
    d.piece("survivor-mark", 280, 222, 80)
    for x, y in pts:
        d.piece("waypoint-pin", x - 30, y, 60)
        d.line(x, y + 50, 320, 236, width=3, dash="9 7", color=BLUE)
    lab(d, "Bearing 1", 150, 190, size=15)
    lab(d, "Bearing 2", 365, 170, size=15, anchor="start")
    lab(d, "Bearing 3", 500, 190, size=15)
    lab(d, "You are here", 320, 335)


@design("NAV/marking-a-route-1")
def _(d):
    flow(d, [("cloth", "Strip"), ("cairn", "Cairn"), ("arrow-straight", "Turn"), ("do-not", "Dead end")], 90, w=125, arrow=False)
    caption(d, "One symbol per meaning, kept constant.", 300)


@design("NAV/marking-a-route-2")
def _(d):
    d.piece("trail-marker", 60, 60, 200)
    d.arrow(270, 105, 350, 105)
    d.arrow(115, 105, 70, 105)
    d.piece("do-not", 15, 90, 40)
    d.rect(400, 70, 220, 150, fill=CREAM)
    lab(d, "Key", 510, 98)
    d.piece("legend-solid", 415, 105, 70)
    lab(d, "Direction", 490, 137, anchor="start")
    d.piece("legend-dot", 415, 160, 70)
    lab(d, "Dead end", 490, 192, anchor="start")
    caption(d, "The key decides how the route is read.", 300)


@design("NAV/marking-a-route-3")
def _(d):
    d.line(16, 220, 624, 220, dash="2 12", width=5)
    for x in [60, 140, 220]:
        d.piece("trail-marker", x - 50, 150, 100)
    for x in [380, 540]:
        d.piece("trail-marker", x - 50, 150, 100)
    d.arrow(60, 280, 140, 280, width=3)
    d.arrow(140, 280, 60, 280, width=3)
    lab(d, "Fog spacing", 100, 315, size=15)
    d.arrow(380, 280, 540, 280, width=3)
    d.arrow(540, 280, 380, 280, width=3)
    lab(d, "Clear spacing", 460, 315, size=15)
    caption(d, "Marks sit closer in fog.", 346)


@design("NAV/marking-a-route-4")
def _(d):
    d.piece("cairn", 40, 70, 130)
    lab(d, "Stack", 105, 220)
    d.arrow(185, 130, 245, 130)
    d.piece("cairn", 255, 70, 130)
    d.arrow(320, 200, 320, 250, width=3)
    lab(d, "Dismantle", 320, 275)
    d.arrow(400, 130, 460, 130)
    for x in [480, 530, 580]:
        d.piece("rock", x - 25, 150, 50)
    lab(d, "Flat", 545, 225)
    caption(d, "Remove the whole cairn: no false trail.", 330)


@design("NAV/natural-direction-signs-1")
def _(d):
    d.curve_arrow("M110 200Q320 -40 530 200", (530, 200), 0.85)
    lab(d, "East", 90, 225)
    lab(d, "West", 550, 225)
    lab(d, "Sun path", 320, 55)
    d.piece("shadow-stick", 250, 170, 140)
    d.arrow(110, 320, 530, 320, width=3)
    d.arrow(530, 320, 110, 320, width=3)
    lab(d, "Shadow line", 320, 345, size=15)


@design("NAV/natural-direction-signs-2")
def _(d):
    d.curve_arrow("M110 210Q320 -50 530 210", (530, 210), 0.85)
    d.circle(320, 79, 7)
    lab(d, "Midday", 320, 55)
    d.piece("shadow-stick", 190, 180, 140)
    lab(d, "Shortest shadow", 260, 345, size=15)
    d.arrow(480, 250, 480, 320, width=4)
    lab(d, "South", 480, 345)


@design("NAV/natural-direction-signs-3")
def _(d):
    d.arrow(20, 120, 90, 120)
    lab(d, "Wind", 55, 100)
    d.piece("slope", 80, 120, 260)
    lab(d, "Windward", 190, 318, size=15)
    d.piece("snowdrift", 340, 180, 190)
    lab(d, "Lee: snowdrift", 470, 318, size=15)
    caption(d, "Drift follows recent wind.", 346)


@design("NAV/natural-direction-signs-4")
def _(d):
    d.piece("river", 30, 90, 160)
    lab(d, "River", 110, 230)
    d.arrow(200, 150, 340, 150, width=4)
    lab(d, "Downhill", 270, 130)
    d.piece("river", 350, 80, 270)
    lab(d, "Larger river", 485, 290)
    d.piece("footprints", 215, 215, 120)
    lab(d, "Path", 275, 330)


@design("NAV/navigating-a-city-without-gps-1")
def _(d):
    d.piece("tower", 20, 60, 110)
    lab(d, "Tower", 75, 220)
    d.arrow(140, 130, 235, 130, width=3)
    d.piece("table-grid", 245, 70, 150)
    d.arrow(405, 130, 500, 130, width=3)
    d.piece("station", 505, 60, 110)
    lab(d, "Station", 560, 220)
    d.piece("bracket", 270, 200, 100)
    lab(d, "Count blocks", 320, 300)
    caption(d, "Landmarks anchor the count.", 346)


@design("NAV/navigating-a-city-without-gps-2")
def _(d):
    d.piece("sun", 30, 30, 110)
    d.arrow(150, 90, 330, 150, width=4)
    lab(d, "Sun", 85, 150)
    d.piece("river", 30, 190, 120)
    d.arrow(160, 260, 330, 190, width=4)
    lab(d, "River", 95, 310)
    d.piece("decision", 340, 80, 150)
    lab(d, "Heading", 530, 170, anchor="start")
    d.tick(570, 220, 20)
    caption(d, "Two cues agree: choose the turn.", 346)


@design("NAV/navigating-a-city-without-gps-3")
def _(d):
    d.piece("person-standing", 30, 110, 130)
    lab(d, "Staff", 95, 290)
    d.piece("info", 255, 20, 70)
    lab(d, "Help", 340, 65, anchor="start")
    d.piece("door", 215, 100, 150)
    d.piece("bulletin", 410, 100, 150)
    lab(d, "Map board", 485, 290)
    caption(d, "Ask here; read the board first.", 346)


@design("NAV/navigating-at-night-1")
def _(d):
    d.piece("flashlight", 20, 90, 110)
    lab(d, "Light", 75, 210)
    d.piece("footprints", 175, 90, 100)
    lab(d, "Count", 225, 210)
    d.piece("compass", 330, 85, 100)
    lab(d, "Bearing", 380, 210)
    d.piece("waypoint-pin", 500, 90, 90)
    lab(d, "Stop", 545, 210)
    d.arrow(135, 130, 170, 130, width=3)
    d.arrow(280, 130, 325, 130, width=3)
    d.arrow(435, 130, 495, 130, width=3)
    d.piece("arrow-loop", 250, 235, 100)
    lab(d, "Repeat every 50 m", 340, 290, anchor="start", size=15)
    caption(d, "Three checks, not only at the start.", 346)


@design("NAV/navigating-at-night-2")
def _(d):
    d.piece("flashlight", 30, 40, 150)
    chip(d, 105, 190, 120, 36, "Red light", size=15, color=RED)
    d.leader(105, 172, 105, 130)
    d.piece("map", 230, 110, 230)
    d.piece("compass", 490, 130, 120)
    lab(d, "Map", 345, 300)
    lab(d, "Compass", 550, 280)
    d.arrow(150, 100, 250, 150, width=3)
    caption(d, "Light close to the map protects night vision.", 346)


@design("NAV/navigating-at-night-3")
def _(d):
    d.piece("table-grid", 20, 70, 180)
    lab(d, "Tally: one mark per 50 m", 110, 250, size=15)
    d.line(260, 200, 600, 200, width=4)
    for x in [260, 380, 490, 600]:
        d.line(x, 188, x, 212, width=3)
    for x in [320, 435, 545]:
        lab(d, "50 m", x, 235, size=15)
    d.piece("waypoint-pin", 440, 150, 70)
    lab(d, "Reset", 475, 140)
    caption(d, "A landmark resets the count.", 340)


@design("NAV/navigating-at-night-4")
def _(d):
    d.piece("tent", 30, 80, 170)
    lab(d, "Shelter", 115, 255)
    d.line(220, 220, 620, 220, dash="2 12", width=5)
    d.piece("waypoint-pin", 270, 159, 90)
    lab(d, "Stop point", 315, 255)
    d.piece("tree", 480, 127, 140)
    lab(d, "Landmark", 550, 255)
    caption(d, "Choose the stop before dark.", 340)


@design("NAV/planning-routes-1")
def _(d):
    d.piece("waypoint-pin", 40, 130, 80)
    d.piece("waypoint-pin", 520, 130, 80)
    d.path("M110 190C220 60 420 60 540 190", stroke=INK, width=4)
    d.path("M110 195C220 330 420 330 540 195", stroke=INK, width=4, dash="10 8")
    d.piece("waypoint-pin", 293, 75, 44)
    d.piece("waypoint-pin", 293, 232, 44)
    lab(d, "Main", 320, 52)
    lab(d, "Alternative", 320, 345)
    lab(d, "Checkpoints", 320, 180, size=15)
    d.leader(320, 162, 315, 112)
    d.leader(320, 192, 315, 240)


@design("NAV/planning-routes-2")
def _(d):
    d.piece("contour-lines", 160, 30, 320)
    chip(d, 70, 110, 100, 36, "Steep", size=15)
    d.leader(122, 112, 270, 150)
    chip(d, 560, 90, 100, 36, "Ridge", size=15)
    d.leader(510, 94, 318, 146)
    chip(d, 560, 270, 100, 36, "Saddle", size=15)
    d.piece("waypoint-pin", 300, 190, 60)
    d.leader(510, 270, 330, 214)
    caption(d, "The saddle is the lowest crossing.", 346)


@design("NAV/planning-routes-3")
def _(d):
    parts = [(30, 110, "Flat"), (140, 300, "Climb"), (440, 70, "Rest"), (510, 110, "Climb")]
    for x, w, t in parts:
        d.rect(x, 110, w, 70, fill=CREAM, rx=8)
        lab(d, t, x + w / 2, 152)
    d.arrow(30, 230, 620, 230, width=3)
    lab(d, "Time", 320, 262, size=15)
    caption(d, "Climbs and rests take more of the day than distance suggests.", 330)


@design("NAV/planning-routes-4")
def _(d):
    d.piece("table-grid", 30, 80, 250)
    lab(d, "Name", 92, 82, size=15)
    lab(d, "Time", 155, 82, size=15)
    lab(d, "Contact", 218, 82, size=15)
    d.arrow(290, 150, 380, 150)
    d.piece("person-standing", 390, 90, 130)
    d.piece("phone-call", 510, 90, 90)
    lab(d, "Contact", 500, 225)
    caption(d, "A late checkpoint triggers action.", 346)


@design("NAV/signalling-with-a-mirror-and-light-1")
def _(d):
    d.piece("person-standing", 20, 150, 130)
    d.piece("signal-mirror", 150, 120, 90)
    d.piece("sun", 220, 0, 100)
    d.line(260, 80, 205, 150, dash="3 8", width=4, color=BLUE)
    lab(d, "Sunlight", 330, 65, anchor="start")
    d.line(230, 165, 510, 165, dash="3 8", width=4, color=BLUE)
    d.piece("waypoint-pin", 500, 110, 90)
    lab(d, "Target", 545, 215)
    chip(d, 190, 290, 130, 36, "Sight hole", size=15)
    d.leader(190, 272, 190, 190)
    caption(d, "The spot stays on target while the mirror moves.", 346)


@design("NAV/signalling-with-a-mirror-and-light-2")
def _(d):
    d.piece("flashlight", 20, 90, 140)
    for x in [220, 270, 320]:
        d.circle(x, 155, 12)
    for x in [450, 500, 550]:
        d.circle(x, 155, 12)
    d.line(345, 155, 425, 155, dash="3 8", width=4, color=BLUE)
    lab(d, "Three flashes", 270, 205, size=15)
    lab(d, "Pause", 385, 130, size=15)
    lab(d, "Three flashes", 500, 205, size=15)
    caption(d, "Repeat the three, pause so the receiver can reply.", 300)


@design("NAV/walking-distances-and-pace-1")
def _(d):
    d.piece("person-standing", 20, 40, 110)
    d.piece("footprints", 170, 40, 100)
    chip(d, 360, 90, 100, 44, "Timer")
    d.piece("table-grid", 470, 50, 130)
    lab(d, "Average", 535, 175, size=15)
    d.arrow(135, 85, 170, 85, width=3)
    d.arrow(275, 85, 305, 85, width=3)
    d.arrow(415, 90, 465, 90, width=3)
    d.line(40, 280, 600, 280, width=4)
    d.line(40, 268, 40, 292, width=3)
    d.line(600, 268, 600, 292, width=3)
    d.arrow(60, 240, 580, 240, width=3)
    d.arrow(580, 240, 60, 240, width=3)
    lab(d, "100 m", 320, 228)
    caption(d, "Three repeats are averaged.", 330)


@design("NAV/walking-distances-and-pace-2")
def _(d):
    d.path("M20 260L300 260L610 110", stroke=INK, width=4)
    d.piece("person-standing", 100, 195, 100)
    lab(d, "Flat: steady pace", 150, 305, size=15)
    d.piece("person-standing", 380, 125, 100)
    lab(d, "Uphill: slower", 480, 200, anchor="start", size=15)
    caption(d, "Uphill takes longer than the same distance on the flat.", 346)


@design("NAV/walking-distances-and-pace-3")
def _(d):
    d.piece("waypoint-pin", 40, 140, 70)
    d.piece("waypoint-pin", 530, 140, 70)
    d.line(100, 188, 550, 188, width=4)
    lab(d, "Straight line", 325, 170, size=15)
    d.path("M100 205C170 330 250 150 330 270S470 330 550 205", stroke=INK, width=4, dash="2 12")
    lab(d, "Real path", 330, 335, size=15)
