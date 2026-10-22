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


def boxed(d, cx, cy, w, s, size=16):
    chip(d, cx, cy, w, 64, s, size=size)


@design("HYG/preventing-infection-1")
def _(d):
    xs = [100, 320, 540]
    for x, s in zip(xs, ["Source", "Route", "New host"]):
        boxed(d, x, 110, 150, s)
    for i, (x, s) in enumerate(zip([210, 430], ["Hand washing", "Safe water"])):
        d.arrow(x - 40, 110, x + 40, 110)
    d.badge(1, 100, 40, 16)
    d.badge(2, 320, 40, 16)
    d.badge(3, 540, 40, 16)
    for x, s in zip(xs, ["Waste\ndisposal", "Safe water", "Hand\nwashing"]):
        d.cross(x, 200, 16)
        d.text(s, x, 242, size=16, weight=600)
    caption(d, "Each link has its own break.", 330)


@design("HYG/preventing-infection-2")
def _(d):
    d.line(16, 50, 400, 50, dash="9 7")
    d.line(16, 250, 400, 250, dash="9 7")
    d.line(16, 50, 16, 250, dash="9 7")
    d.line(400, 50, 400, 250, dash="9 7")
    d.line(200, 50, 200, 250, dash="9 7")
    d.piece("person-sitting", 50, 100, 110)
    d.text("Unwell\nsleeping area", 108, 82, size=15, weight=600)
    d.piece("bed", 240, 100, 120)
    d.text("Bedding zone", 300, 82, size=15, weight=600)
    d.piece("cup", 40, 175, 60)
    d.text("Cup zone", 100, 232, size=15, weight=600, anchor="start")
    d.piece("toilet", 470, 100, 130)
    d.path("M110 250C110 310 450 310 510 210", stroke=BLUE, width=4, dash="10 8")
    d.arrow(508, 218, 512, 205, color=BLUE)
    d.text("Path to toilet", 300, 336, size=16, weight=600, fill=BLUE)


@design("HYG/preventing-infection-3")
def _(d):
    pts = [(140, 100, "One untreated\ncase"), (500, 100, "New cases\nin a week"), (500, 250, "More\ncontamination"), (140, 250, "More cases")]
    for x, y, s in pts:
        boxed(d, x, y, 160, s, size=15)
    d.arrow(230, 100, 410, 100)
    d.arrow(500, 160, 500, 190)
    d.arrow(410, 250, 230, 250)
    d.arrow(140, 190, 140, 160)
    d.piece("do", 20, 20, 50)
    d.text("Isolate early", 85, 50, size=15, weight=600, anchor="start")
    caption(d, "Isolation stops the loop at the first case.", 340)


@design("HYG/preventing-infection-4")
def _(d):
    d.piece("person-standing", 20, 40, 110)
    d.piece("cup", 140, 70, 60)
    d.piece("bowl", 140, 130, 60)
    d.text("Ana", 75, 160, size=16, weight=600)
    d.piece("person-standing", 240, 40, 110)
    d.piece("cup", 360, 70, 60)
    d.piece("bowl", 360, 130, 60)
    d.text("Ben", 295, 160, size=16, weight=600)
    d.line(450, 40, 450, 270, dash="9 7")
    d.piece("bowl", 480, 60, 100)
    d.piece("bowl", 510, 150, 100)
    d.text("Shared dishes", 540, 270, size=16, weight=600)
    d.text("Each person's cup and bowl", 190, 250, size=16, weight=600)
    caption(d, "Cups are kept by name.", 330)


@design("HYG/rubbish-and-garbage-1")
def _(d):
    d.piece("slope", 160, 70, 340)
    d.piece("pool", 490, 60, 120)
    d.text("Water source", 550, 58, size=16, weight=600)
    d.piece("bucket", 30, 100, 90)
    d.text("Lidded bin", 75, 98, size=16, weight=600)
    d.piece("pit", 10, 210, 130)
    d.text("Rubbish pit", 80, 205, size=16, weight=600)
    d.arrow(440, 150, 200, 262, color=BLUE)
    d.text("Downslope", 290, 186, size=16, weight=600, fill=BLUE)
    caption(d, "The pit goes downslope of the water.", 346)


@design("HYG/rubbish-and-garbage-2")
def _(d):
    items = [("bucket", "Food\nwaste"), ("bucket", "Dry\nrubbish"), ("bucket", "Hazardous\nwaste"), ("tin", "Ash")]
    for i, (p, s) in enumerate(items):
        x = 24 + i * 152
        d.piece(p, x, 80, 130)
        d.text(s, x + 65, 220, size=16, weight=600)
    caption(d, "Sort at source to keep hazards out of the burn pile.", 320)


@design("HYG/rubbish-and-garbage-3")
def _(d):
    pts = [(140, 100, "Food waste"), (500, 100, "Flies"), (500, 250, "Rats"), (140, 250, "Contamination")]
    for x, y, s in pts:
        boxed(d, x, y, 170, s)
    d.arrow(235, 100, 405, 100)
    d.arrow(500, 135, 500, 215)
    d.arrow(405, 250, 235, 250)
    d.arrow(140, 215, 140, 135)
    d.piece("bucket", 280, 120, 80)
    d.piece("do", 345, 120, 36)
    d.text("Lid breaks the loop", 320, 224, size=15, weight=600)


@design("HYG/rubbish-and-garbage-4")
def _(d):
    d.piece("pit", 20, 50, 340)
    d.text("Add soil as it fills", 190, 40, size=16, weight=600)
    labels = ["Soil cap", "Soil layer", "Rubbish layer", "Soil layer", "Rubbish layer"]
    for i, s in enumerate(labels):
        y = 136 + i * 40
        chip(d, 520, y, 170, 34, s, size=15)
        d.arrow(430, y, 366, y, width=3)


@design("HYG/sanitising-water-containers-1")
def _(d):
    d.piece("jerrycan", 200, 50, 240)
    d.piece("water-drop", 270, 140, 60)
    d.leader(372, 52, 374, 78)
    d.text("Cap and neck", 372, 40, size=16, weight=600)
    d.leader(150, 150, 262, 150)
    d.text("Inner walls", 140, 156, size=16, weight=600, anchor="end")
    d.leader(500, 185, 320, 170)
    d.text("Solution level", 510, 191, size=16, weight=600, anchor="start")
    caption(d, "Shake with the cap on so it touches every inner surface.", 340)


@design("HYG/sanitising-water-containers-2")
def _(d):
    d.piece("jerrycan", 200, 50, 240)
    d.piece("do", 292, 140, 56)
    d.leader(372, 52, 374, 78)
    d.text("Cap sealed", 372, 40, size=16, weight=600)
    d.text("Inside clean", 510, 191, size=16, weight=600, anchor="start")
    d.leader(505, 186, 344, 172)
    d.piece("water-drop", 500, 60, 60)
    d.arrow(500, 96, 400, 120)
    d.text("Rinse", 560, 56, size=16, weight=600)
    caption(d, "Check the seal at every refill.", 340)


@design("HYG/washing-hands-without-running-water-1")
def _(d):
    items = [("bucket", "Wet hands"), ("soap", "Apply soap"), ("open-hand", "Rub palms\nand backs"), ("bowl", "Rinse"), ("towel", "Dry")]
    flow(d, items, 100, w=100, label_dy=22)
    for i in range(5):
        d.badge(i + 1, 16 + 23 + i * 123 + 50, 80, 14)
    caption(d, "Rinse with a thin stream to use little water.", 320)


@design("HYG/washing-hands-without-running-water-2")
def _(d):
    d.piece("open-hand", 190, 40, 260)
    d.leader(150, 150, 252, 164)
    d.text("Thumbs", 140, 156, size=16, weight=600, anchor="end")
    d.leader(500, 60, 348, 58)
    d.text("Fingertips", 510, 66, size=16, weight=600, anchor="start")
    d.leader(488, 140, 364, 116)
    d.text("Between fingers", 498, 146, size=15, weight=600, anchor="start")
    d.leader(500, 240, 357, 208)
    d.text("Wrists", 510, 246, size=16, weight=600, anchor="start")


@design("HYG/washing-hands-without-running-water-3")
def _(d):
    flow(d, [("latrine", "Latrine"), ("hands", "Unwashed\nhands"), ("cup", "Shared cup"), ("mouth", "Drinker's\nmouth")], 90, w=120)
    d.piece("warning", 364, 20, 60)
    caption(d, "One shared cup carries germs to a person.", 320)


@design("HYG/waste-from-the-sick-1")
def _(d):
    d.piece("bag", 40, 80, 190)
    d.piece("overhand-knot", 100, 45, 60)
    d.leader(300, 78, 160, 84)
    d.text("Second knot", 310, 84, size=16, weight=600, anchor="start")
    d.text("Double bag", 135, 270, size=16, weight=600)
    d.arrow(240, 170, 380, 170)
    d.piece("bucket", 400, 90, 190)
    d.text("Lidded rigid bin", 495, 270, size=16, weight=600)


@design("HYG/waste-from-the-sick-2")
def _(d):
    d.piece("tin", 30, 70, 150)
    d.text("Disinfectant soak", 105, 230, size=16, weight=600)
    d.arrow(190, 130, 235, 130)
    d.piece("pot-with-lid", 245, 70, 150)
    d.piece("flame", 285, 175, 70)
    d.text("Hot wash", 320, 262, size=16, weight=600)
    d.arrow(405, 130, 450, 130)
    d.piece("rope-coil", 460, 70, 150)
    d.text("Sun-drying", 535, 230, size=16, weight=600)
    d.badge(1, 105, 56, 16)
    d.badge(2, 320, 56, 16)
    d.badge(3, 535, 56, 16)
