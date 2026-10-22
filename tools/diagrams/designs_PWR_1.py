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


def pc(d, name, cx, cy, w):
    d.piece(name, cx - w / 2, cy - w * 0.375, w)


def label(d, s, x, y, size=16, anchor="middle", fill=INK):
    d.text(s, x, y, size=size, weight=600, anchor=anchor, fill=fill)


def flow(d, items, y, w=130, label_dy=26, size=16):
    n = len(items)
    gap = (640 - n * w) / (n + 1)
    for i, (piece, text) in enumerate(items):
        x = gap + i * (w + gap)
        d.piece(piece, x, y, w)
        d.text(text, x + w / 2, y + w * 0.75 + label_dy, size=size, weight=600)
        if i < n - 1:
            d.arrow(x + w + 4, y + w * 0.375, x + w + gap - 4, y + w * 0.375)


def circ_path(cx, cy, r):
    return f"M{cx - r} {cy}A{r} {r} 0 1 1 {cx + r} {cy}A{r} {r} 0 1 1 {cx - r} {cy}"


def table(d, x, y, widths, heads, rows, rh=40, size=15):
    w = sum(widths)
    d.rect(x, y, w, rh, fill=SAND, rx=6)
    d.rect(x, y + rh, w, rh * len(rows), fill=CREAM, rx=6)
    cx = x
    for i, wd in enumerate(widths):
        d.text(heads[i], cx + wd / 2, y + rh / 2 + 5, size=size, weight=700)
        if i:
            d.line(cx, y, cx, y + rh * (len(rows) + 1), width=2)
        cx += wd
    for r in range(len(rows)):
        yy = y + rh * (r + 1)
        d.line(x, yy, x + w, yy, width=2)
        cx = x
        for i, wd in enumerate(widths):
            d.text(rows[r][i], cx + wd / 2, yy + rh / 2 + 5, size=size)
            cx += wd


@design("PWR/electrical-hazards-after-a-disaster-1")
def _(d):
    d.path(circ_path(320, 175, 130), stroke=INK, width=3, dash="10 8")
    label(d, "10 m", 320, 30)
    d.leader(320, 36, 320, 45)
    pc(d, "power-line", 260, 170, 150)
    label(d, "Power line", 110, 120)
    d.leader(150, 125, 215, 150)
    pc(d, "footprints", 380, 205, 110)
    d.curve_arrow("M340 262C375 285 415 285 445 262", (445, 262), -0.7, width=4)
    label(d, "Shuffle, feet together", 400, 322)
    pc(d, "person-standing", 520, 190, 120)
    caption(d, "One foot stays on the ground at every step.", 348)


@design("PWR/electrical-hazards-after-a-disaster-2")
def _(d):
    pc(d, "table-grid", 200, 150, 380)
    pc(d, "pool", 105, 89, 90)
    pc(d, "do-not", 105, 89, 30)
    label(d, "Standing water", 105, 38)
    d.leader(105, 44, 105, 68)
    d.arrow(60, 212, 450, 212)
    label(d, "Dry path", 250, 270)
    pc(d, "main-switch", 540, 200, 130)
    label(d, "Main switch", 540, 285)
    caption(d, "The path avoids all water before the switch.", 340)


@design("PWR/electrical-hazards-after-a-disaster-3")
def _(d):
    pc(d, "waypoint-pin", 80, 150, 100)
    label(d, "Door", 80, 235)
    chip(d, 540, 150, 130, 50, "Meter box")
    d.line(120, 150, 475, 150, width=5)
    label(d, "Dry path", 300, 138)
    d.rect(205, 30, 190, 70, fill="none", rx=16, dash="9 7")
    pc(d, "pool", 300, 65, 120)
    pc(d, "do-not", 300, 65, 36)
    d.rect(205, 200, 190, 70, fill="none", rx=16, dash="9 7")
    pc(d, "pool", 300, 235, 120)
    pc(d, "do-not", 300, 235, 36)
    label(d, "Standing water", 300, 300)
    caption(d, "The route stays on dry ground throughout.", 340)


@design("PWR/fridge-and-freezer-during-a-cut-1")
def _(d):
    pc(d, "freezer", 190, 170, 270)
    for x in (120, 170, 220):
        pc(d, "bottle", x, 205, 58)
    label(d, "Full freezer", 190, 60)
    label(d, "Food", 30, 120, anchor="start")
    d.leader(70, 126, 146, 196)
    label(d, "Frozen bottles", 450, 175, anchor="start")
    d.leader(440, 170, 236, 200)
    label(d, "Door closed", 450, 245, anchor="start")
    d.arrow(440, 240, 292, 218)
    caption(d, "Cold stays in.", 335)


@design("PWR/fridge-and-freezer-during-a-cut-2")
def _(d):
    d.line(320, 40, 320, 140, width=7)
    d.line(320, 230, 320, 315, width=7)
    d.arrow(470, 205, 335, 205, color=RED)
    label(d, "Warm air in", 540, 175)
    d.arrow(305, 170, 170, 170, color=BLUE)
    label(d, "Cold air out", 170, 205)
    label(d, "Worn seal", 470, 80)
    d.leader(450, 88, 325, 143)
    caption(d, "A small gap lets warm air in all the time.", 345)


@design("PWR/fridge-and-freezer-during-a-cut-3")
def _(d):
    pc(d, "fridge", 250, 170, 300)
    pc(d, "bottle", 250, 105, 46)
    pc(d, "caution", 250, 205, 46)
    d.arrow(120, 90, 120, 260, color=BLUE)
    label(d, "Cold sinks", 120, 290)
    label(d, "Bottles top", 420, 105, anchor="start")
    d.leader(412, 100, 262, 105)
    label(d, "Fast-spoiling food", 420, 215, anchor="start")
    d.leader(412, 210, 270, 205)
    caption(d, "Fast-spoiling food goes at the bottom.", 345)


@design("PWR/fridge-and-freezer-during-a-cut-4")
def _(d):
    pc(d, "thermometer", 110, 175, 240)
    rows = [("tick", "At or below 5 C: safe", 80), ("caution", "Above 5 C, up to 2 h: still safe", 175), ("cross", "Beyond 2 h: discard perishables", 270)]
    for kind, s, y in rows:
        d.rect(220, y - 28, 390, 56, fill=CREAM, rx=12)
        if kind == "tick":
            d.tick(256, y, 16)
        elif kind == "cross":
            d.cross(256, y, 16)
        else:
            pc(d, "caution", 256, y, 52)
        d.text(s, 285, y + 6, size=16, weight=600, anchor="start")
    d.line(220, 128, 610, 128, dash="9 7", width=3, color=RED)
    d.line(220, 223, 610, 223, dash="9 7", width=3, color=RED)
    caption(d, "The two hours count from the first reading above 5 C.", 345)


@design("PWR/generator-safety-1")
def _(d):
    pc(d, "hut", 130, 190, 200)
    label(d, "House", 130, 285)
    pc(d, "generator", 510, 190, 150)
    label(d, "Generator", 510, 285)
    d.arrow(235, 215, 435, 215, width=3)
    d.arrow(435, 215, 235, 215, width=3)
    label(d, "6 m", 335, 205, size=17)
    d.arrow(50, 55, 590, 55, color=BLUE)
    label(d, "Wind", 320, 42, fill=BLUE)
    pc(d, "do-not", 130, 222, 30)
    caption(d, "Distance and downwind placement keep exhaust out.", 345)


@design("PWR/generator-safety-2")
def _(d):
    pc(d, "hut", 380, 130, 200)
    pc(d, "do-not", 380, 168, 30)
    pc(d, "do-not", 430, 150, 30)
    label(d, "Door", 335, 60)
    d.leader(345, 66, 372, 152)
    label(d, "Window", 460, 60)
    d.leader(450, 66, 434, 134)
    pc(d, "generator", 100, 224, 140)
    label(d, "Generator", 100, 185)
    for x in (5, 190, 375):
        d.piece("ground-line", x, 182, 215)
    pc(d, "appliance", 560, 205, 100)
    label(d, "Devices", 560, 160)
    d.line(165, 258, 520, 258, width=5, color=BLUE)
    label(d, "Cable", 330, 246, fill=BLUE)
    caption(d, "A cable through a gap lets exhaust in.", 345)


@design("PWR/generator-safety-3")
def _(d):
    names = ["Site\ncheck", "Fuel and oil,\nengine cold", "Alarm\ncheck", "Start and\nsettle", "Connect one\ndevice"]
    for i, s in enumerate(names):
        x = 20 + i * 124
        chip(d, x + 52, 105, 104, 76, s, size=15)
        d.badge(i + 1, x + 8, 62, 15)
        if i < 4:
            d.arrow(x + 108, 105, x + 140, 105, width=3)
    chip(d, 320, 260, 190, 46, "Recheck wattage")
    d.curve_arrow("M530 145V240H420", (420, 240), 3.14159, width=3)
    d.curve_arrow("M420 275H600V150", (600, 150), -1.5708, width=3)
    caption(d, "Recheck after every connection.", 345)


@design("PWR/lighting-without-electricity-1")
def _(d):
    items = [("flashlight", "Flashlight", "Movement"), ("head-torch", "Head torch", "Hands-free"), ("lantern", "Lantern", "A room"), ("oil-lamp", "Oil lamp", "Reading")]
    for i, (p, n, t) in enumerate(items):
        cx = 90 + i * 153
        pc(d, p, cx, 100, 130)
        label(d, n, cx, 185)
        chip(d, cx, 240, 130, 46, t, size=16)
    caption(d, "Each job needs a different light.", 335)


@design("PWR/lighting-without-electricity-2")
def _(d):
    rooms = [("Bedroom", 60, 40, "flashlight"), ("Hallway and stairs", 330, 40, None), ("Kitchen", 60, 180, "lantern"), ("Living room", 330, 180, "candle")]
    for name, x, y, p in rooms:
        d.rect(x, y, 250, 125, fill=CREAM, rx=10)
        label(d, name, x + 125, y + 26)
        if p:
            pc(d, p, x + 125, y + 80, 90)
        else:
            pc(d, "caution", x + 125, y + 70, 60)
    label(d, "No light source", 455, 155, size=14, fill=RED)
    caption(d, "A room without light is the gap to fix before the cut.", 345)


@design("PWR/lighting-without-electricity-3")
def _(d):
    nodes = [("bed", "Bedside"), ("flashlight", "Hallway"), ("flashlight", "Stairs"), ("toilet", "Toilet")]
    for i, (p, n) in enumerate(nodes):
        cx = 85 + i * 157
        pc(d, p, cx, 130, 110)
        label(d, n, cx, 215)
        if i < 3:
            d.arrow(cx + 62, 130, cx + 95, 130)
    d.arrow(85, 290, 545, 290)
    pc(d, "footprints", 320, 262, 70)
    label(d, "Bed-to-toilet route", 320, 322)
    caption(d, "Light the night route first.", 348)


@design("PWR/lighting-without-electricity-4")
def _(d):
    pc(d, "bed", 100, 140, 160)
    label(d, "Bed", 100, 215)
    pc(d, "flashlight", 245, 60, 80)
    label(d, "Torch", 300, 60, anchor="start")
    pc(d, "door", 540, 140, 120)
    label(d, "Door", 540, 215)
    d.arrow(190, 150, 470, 150, width=3)
    pc(d, "footprints", 330, 110, 70)
    d.line(30, 275, 610, 275, width=6)
    label(d, "Wall", 575, 260)
    pc(d, "hand", 330, 252, 80)
    caption(d, "A hand on the wall keeps direction.", 335)


@design("PWR/medical-devices-without-power-1")
def _(d):
    table(d, 140, 70, [140, 170, 150], ["Device", "Power source", "Hours left"],
          [["Oxygen unit", "Battery", "2"], ["Insulin fridge", "Cool box", "8"], ["Phone", "Power bank", "24"]], rh=48)
    d.arrow(60, 142, 130, 142)
    label(d, "Check first", 70, 122)
    caption(d, "Shortest backup sits at the top.", 320)


@design("PWR/medical-devices-without-power-2")
def _(d):
    table(d, 40, 60, [130, 150, 150, 130], ["Device", "Power source", "Backup time", "Supplier contact"],
          [["", "", "", ""]] * 4, rh=46, size=14)
    caption(d, "One row per device shows gaps at a glance.", 320)


@design("PWR/medical-devices-without-power-3")
def _(d):
    chip(d, 90, 170, 120, 70, "Device", size=17)
    srcs = [("battery", "Battery", 62), ("solar-panel", "Solar panel", 137), ("car", "Car charger", 212), ("oxygen-cylinder", "Oxygen cylinder", 287)]
    for p, n, y in srcs:
        d.arrow(155, 170, 270, y, width=3)
        pc(d, p, 330, y, 90)
        label(d, n, 385, y + 6, anchor="start")
        chip(d, 575, y, 90, 34, "__ h", size=15)
    label(d, "Run time", 575, 330, size=15)


@design("PWR/oil-lamps-and-candles-safely-1")
def _(d):
    for cx, p, n in ((170, "candle", "Candle"), (470, "oil-lamp", "Oil lamp")):
        d.path(circ_path(cx, 150, 100), stroke=INK, width=3, dash="10 8")
        pc(d, p, cx, 150, 120)
        label(d, n, cx, 275)
        label(d, "30 cm clear", cx, 40, size=15)
    pc(d, "do-not", 215, 318, 34)
    label(d, "Curtains", 240, 324, anchor="start")
    pc(d, "do-not", 395, 318, 34)
    label(d, "Paper", 420, 324, anchor="start")


@design("PWR/oil-lamps-and-candles-safely-2")
def _(d):
    pc(d, "oil-lamp", 320, 170, 250)
    label(d, "Flame", 110, 140, anchor="middle")
    d.leader(145, 135, 300, 150)
    label(d, "Chimney", 110, 90, anchor="middle")
    d.leader(155, 88, 300, 105)
    label(d, "Wick trimmed even", 530, 140)
    d.leader(450, 135, 326, 190)
    label(d, "Fuel tank", 530, 255)
    d.leader(470, 250, 345, 245)


@design("PWR/oil-lamps-and-candles-safely-3")
def _(d):
    names = ["Check\nholder", "Clear\n30 cm", "Light, hand\nbelow flame", "Adjust wick,\nchimney on", "Note\nthe time"]
    for i, s in enumerate(names):
        x = 20 + i * 124
        chip(d, x + 52, 80, 104, 76, s, size=15)
        d.badge(i + 1, x + 8, 37, 15)
        if i < 4:
            d.arrow(x + 108, 80, x + 140, 80, width=3)
    d.path(circ_path(320, 255, 65), stroke=INK, width=3, dash="10 8")
    pc(d, "candle", 320, 255, 100)
    label(d, "30 cm clear", 490, 262, anchor="start")
    d.leader(480, 257, 387, 257)


@design("PWR/planning-power-autonomy-1")
def _(d):
    stages = [
        (20, "Stage 3: generator, stored fuel", ["generator"]),
        (134, "Stage 2: solar power", ["solar-panel", "charge-controller", "battery"]),
        (248, "Stage 1: torches and radio", ["flashlight", "radio"]),
    ]
    for y, s, ps in stages:
        d.rect(70, y, 550, 82, fill=CREAM, rx=12)
        for i, p in enumerate(ps):
            pc(d, p, 125 + i * 85, y + 41, 80)
        d.text(s, 125 + 85 * len(ps) + 10, y + 47, size=16, weight=600, anchor="start")
    for y in (116, 230):
        d.arrow(40, y + 18, 40, y - 18, width=4)
    caption(d, "Each stage depends on the one below.", 348)


@design("PWR/planning-power-autonomy-2")
def _(d):
    flow(d, [("solar-panel", "Panel"), ("charge-controller", "Controller"), ("battery", "Battery"), ("appliance", "Load")], 90, w=130)
    caption(d, "The controller sits between panel and battery, never at the load.", 300)


@design("PWR/planning-power-autonomy-3")
def _(d):
    d.rect(250, 120, 110, 40, fill=YELLOW, rx=4)
    d.rect(250, 160, 110, 150, fill=CREAM, rx=4)
    d.text("Usable\n6,000 Wh", 305, 232, size=16, weight=600)
    d.path("M372 120H382V160H372", stroke=INK, width=3)
    label(d, "Loss 1,500 Wh", 395, 146, anchor="start")
    d.path("M236 120H226V310H236", stroke=INK, width=3)
    label(d, "Nominal\n7,500 Wh", 216, 205, anchor="end")
    d.line(110, 312, 530, 312, width=5)
    caption(d, "Losses are a fifth of nominal capacity.", 345)


@design("PWR/planning-power-autonomy-4")
def _(d):
    d.arrow(30, 190, 610, 190, width=4)
    months = "J F M A M J J A S O N D".split()
    seasons = {2: "Spring", 5: "Summer", 8: "Autumn", 11: "Winter"}
    for i, m in enumerate(months):
        x = 55 + i * 46
        if i in seasons:
            d.circle(x, 190, 11, fill=YELLOW)
            label(d, seasons[i], x, 150)
        else:
            d.circle(x, 190, 6, fill=INK)
        d.text(m, x, 222, size=15, weight=600)
    d.circle(55, 190, 11, fill=RED)
    chip(d, 130, 290, 150, 40, "Annual full test", size=15)
    d.leader(95, 270, 55, 202)
    label(d, "Checks cluster at season changes", 420, 295, size=15)


@design("PWR/medical-devices-without-power-4")
def _(d):
    d.rect(80, 50, 480, 230, fill=CREAM, rx=14)
    label(d, "Cool box", 320, 80)
    pc(d, "ice-pack", 150, 170, 120)
    pc(d, "ice-pack", 490, 170, 120)
    label(d, "Ice packs", 150, 250)
    label(d, "Ice packs", 490, 250)
    pc(d, "pills", 320, 170, 100)
    label(d, "Medicine", 320, 250)
    pc(d, "thermometer", 395, 170, 100)
    d.arrow(200, 165, 278, 165, width=3)
    d.arrow(278, 165, 200, 165, width=3)
    label(d, "Gap", 239, 150, size=15)
    label(d, "Thermometer", 400, 112, size=15)
    d.leader(400, 118, 396, 150)
    caption(d, "Cold reaches the medicine without freezing it.", 330)


@design("PWR/power-cut-checklist-1")
def _(d):
    d.arrow(30, 120, 610, 120, width=4)
    for cx, t, task in ((120, "First hour", "Medical needs"), (320, "First day", "Heat, water, food"), (520, "First week", "Budget")):
        d.circle(cx, 120, 11, fill=YELLOW)
        label(d, t, cx, 85, size=17)
        d.line(cx, 135, cx, 175, width=3)
        chip(d, cx, 205, 170, 56, task, size=16)
    caption(d, "Medical needs come before comfort tasks.", 320)


@design("PWR/power-cut-checklist-2")
def _(d):
    d.rect(30, 40, 230, 250, fill="#fbe9c4", rx=12)
    label(d, "Heating room", 145, 75)
    d.rect(370, 40, 240, 105, fill=CREAM, rx=12)
    d.rect(370, 185, 240, 105, fill=CREAM, rx=12)
    label(d, "Closed rooms", 490, 75)
    label(d, "Closed rooms", 490, 220)
    pc(d, "towel", 315, 92, 90)
    pc(d, "towel", 315, 237, 90)
    d.arrow(265, 130, 365, 130, width=3, dash="8 6")
    label(d, "Towel at door", 315, 330, size=16)
    d.leader(315, 318, 315, 262)
    caption(d, "Heat stays in one room when door gaps are sealed.", 352)


@design("PWR/power-cut-checklist-3")
def _(d):
    cols = [("Hour", ["Medical needs", "Heat one room", "Light"]), ("Day", ["Food and water", "Charge plan", "Check neighbours"]), ("Week", ["Budget", "Restock fuel", "Review plan"])]
    for i, (h, items) in enumerate(cols):
        x = 20 + i * 210
        d.rect(x, 40, 180, 40, fill=SAND, rx=8)
        label(d, h, x + 90, 67, size=17)
        for j, it in enumerate(items):
            chip(d, x + 90, 120 + j * 58, 180, 46, it, size=15, weight=500)
        if i < 2:
            d.arrow(x + 184, 160, x + 206, 160, width=4)
    caption(d, "Each tier builds on the one before.", 340)


@design("PWR/power-cut-checklist-4")
def _(d):
    for i in range(4):
        x = 20 + i * 168
        pc(d, "appliance", x + 48, 150, 84)
        chip(d, x + 48, 230, 96, 40, f"Appliance {i + 1}", size=15)
        if i < 3:
            d.arrow(x + 100, 150, x + 160, 150, width=3)
            d.circle(x + 130, 150, 9, fill=YELLOW)
            label(d, "Pause", x + 130, 120, size=15)
    caption(d, "One device at a time avoids a combined surge.", 320)


@design("PWR/powering-devices-from-a-car-1")
def _(d):
    pc(d, "car", 200, 215, 190)
    pc(d, "hut", 530, 205, 170)
    d.arrow(120, 262, 28, 262, width=3)
    label(d, "Exhaust", 75, 290, size=15)
    d.arrow(300, 285, 445, 285, width=3)
    d.arrow(445, 285, 300, 285, width=3)
    label(d, "Distance", 372, 313, size=15)
    pc(d, "charger", 150, 70, 90)
    label(d, "12 V charger", 150, 36, size=15)
    pc(d, "phone-call", 340, 70, 90)
    label(d, "Phone", 340, 118, size=15)
    d.line(190, 70, 300, 70, width=4)
    label(d, "Cable", 245, 55, size=15)
    d.line(162, 98, 200, 172, width=3, dash="6 6")
    caption(d, "Same distance rule as a generator.", 348)


@design("PWR/powering-devices-from-a-car-2")
def _(d):
    d.arrow(30, 220, 610, 220, width=4)
    for x, t in ((40, "0"), (325, "30"), (600, "60 min")):
        d.line(x, 212, x, 228, width=3)
        d.text(t, x, 250, size=15, weight=600, anchor="middle" if x < 600 else "end")
    for a, b in ((40, 190), (400, 540)):
        d.line(a, 160, b, 160, width=10, color=GREEN)
        d.circle(a, 160, 7, fill=YELLOW)
        d.circle(b, 160, 7, fill=YELLOW)
        label(d, "Engine on", (a + b) / 2, 135)
        label(d, "Charging", (a + b) / 2, 190, size=15)
    d.line(197, 160, 393, 160, width=4, dash="6 8", color=GREY)
    label(d, "Rest", 295, 135)
    caption(d, "The battery recovers between runs.", 320)


@design("PWR/powering-devices-from-a-car-3")
def _(d):
    chip(d, 100, 180, 150, 60, "Read battery\nlevel", size=16)
    d.arrow(177, 180, 235, 180)
    pc(d, "decision", 310, 180, 150)
    label(d, "Above start\nthreshold?", 310, 260, size=15)
    d.arrow(375, 150, 450, 90)
    label(d, "Yes", 425, 140, size=15)
    chip(d, 540, 85, 150, 60, "Run engine\noutdoors", size=16)
    d.arrow(375, 210, 450, 270)
    label(d, "No", 425, 235, size=15)
    chip(d, 540, 275, 150, 60, "Rest", size=16)
    caption(d, "Check before every run.", 345)


@design("PWR/powering-devices-from-a-car-4")
def _(d):
    pc(d, "car", 110, 200, 180)
    pc(d, "car", 530, 200, 180)
    leads = [("1  Red: flat +", RED), ("2  Red: donor +", RED), ("3  Black: donor -", INK), ("4  Black: bare metal", INK)]
    for i, (s, c) in enumerate(leads):
        y = 140 + i * 32
        d.arrow(205, y, 435, y, color=c, width=3)
        d.text(s, 320, y - 6, size=15, weight=600)
    caption(d, "Last clamp on bare metal, away from the flat battery.", 345)


@design("PWR/solar-power-basics-1")
def _(d):
    flow(d, [("solar-panel", "Panel"), ("charge-controller", "Charge\ncontroller"), ("battery", "Battery"), ("inverter", "Inverter"), ("appliance", "Appliances")], 100, w=100, size=15)
    caption(d, "The inverter sits after the battery, never before it.", 300)


@design("PWR/solar-power-basics-2")
def _(d):
    pc(d, "battery", 90, 140, 120)
    label(d, "Battery", 90, 205)
    pc(d, "charge-controller", 320, 140, 120)
    label(d, "Controller", 320, 205)
    pc(d, "solar-panel", 550, 140, 120)
    label(d, "Panel", 550, 205)
    d.arrow(160, 140, 250, 140, width=4)
    d.badge(1, 205, 100, 16)
    chip(d, 205, 175, 66, 30, "Fuse", size=15)
    d.arrow(390, 140, 480, 140, width=4)
    d.badge("2", 435, 100, 16)
    chip(d, 435, 175, 66, 30, "Fuse", size=15)
    label(d, "Controller to battery first", 205, 260, size=15)
    label(d, "Panel last", 435, 260, size=15)
    caption(d, "Disconnect in the reverse order.", 330)


@design("PWR/solar-power-basics-3")
def _(d):
    d.arrow(30, 280, 610, 280, width=4)
    for x, t in ((100, "Dawn"), (280, "Midday"), (460, "Dusk"), (570, "Night")):
        d.line(x, 272, x, 288, width=3)
        label(d, t, x, 310, size=15)
    d.curve_arrow("M100 280C170 280 200 100 280 100C360 100 390 280 460 280", (460, 280), 0, color=YELLOW, width=5)
    label(d, "Panel output", 280, 80)
    d.line(460, 200, 600, 200, width=5, color=BLUE)
    label(d, "Battery draw", 530, 182, size=15)
    caption(d, "After dark the battery carries the whole load.", 348)


@design("PWR/storing-batteries-1")
def _(d):
    d.rect(90, 70, 460, 220, fill=CREAM, rx=14)
    d.line(320, 70, 320, 290, width=3)
    label(d, "Type A", 205, 105, size=17)
    label(d, "Type B", 435, 105, size=17)
    pc(d, "battery", 145, 190, 100)
    pc(d, "battery", 265, 190, 100)
    pc(d, "battery", 390, 190, 100)
    pc(d, "battery", 480, 190, 100)
    chip(d, 320, 40, 140, 34, "Date: 06/2026", size=15)
    pc(d, "tape", 182, 172, 40)
    label(d, "Tape over terminals", 205, 140, size=14)
    d.leader(190, 146, 186, 165)


@design("PWR/storing-batteries-2")
def _(d):
    table(d, 60, 50, [120, 150, 150, 120], ["Type", "Date bought", "Meter reading", "Action"],
          [["AA", "03/2025", "1.5 V", "Keep"], ["AAA", "11/2023", "1.0 V", "Replace"], ["9 V", "06/2025", "9.0 V", "Keep"]], rh=52)
    pc(d, "caution", 38, 180, 40)
    caption(d, "A low reading on one row triggers action on that row.", 330)


@design("PWR/storing-batteries-3")
def _(d):
    d.line(320, 30, 320, 320, width=3, dash="9 7")
    pc(d, "battery", 160, 130, 130)
    pc(d, "tape", 200, 105, 50)
    pc(d, "do", 70, 135, 44)
    label(d, "Terminal covered", 160, 275)
    pc(d, "battery", 440, 130, 110)
    pc(d, "warning", 440, 70, 44)
    pc(d, "gloves", 540, 140, 90)
    pc(d, "cloth", 560, 225, 80)
    label(d, "Leaking cell", 440, 205)
    label(d, "Gloves", 540, 190, size=15)
    label(d, "Dry cloth", 560, 275, size=15)
    caption(d, "Cover terminals; handle leaking cells apart.", 335)
