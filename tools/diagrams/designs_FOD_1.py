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


def p(d, name, cx, cy, w, h=None):
    h = h if h else w * 0.75
    d.piece(name, cx - w / 2, cy - h / 2, w, h)


def lab(d, s, x, y, anchor="middle", size=17):
    d.text(s, x, y, size=size, weight=600, anchor=anchor)


def brace(d, x, y1, y2, side=1):
    d.path(f"M{x} {y1}C{x + 14 * side} {y1} {x + 14 * side} {(y1 + y2) / 2 - 4} {x + 24 * side} {(y1 + y2) / 2}C{x + 14 * side} {(y1 + y2) / 2 + 4} {x + 14 * side} {y2} {x} {y2}")



@design("FOD/cooking-over-a-wood-fire-1")
def _(d):
    for i, (label, piece) in enumerate([("Hot", "pot-with-lid"), ("Medium", "pan"), ("Cool", "bowl")]):
        cx = 120 + i * 200
        d.text(label, cx, 44, size=18, weight=700)
        d.piece(piece, cx - 60, 70, 120)
        d.piece("coals", cx - 75, 160, 150)
    d.line(220, 56, 220, 290, dash="9 7")
    d.line(420, 56, 420, 290, dash="9 7")
    d.arrow(90, 310, 550, 310, width=3)
    d.arrow(550, 310, 90, 310, width=3)
    caption(d, "Move the food between zones, not the wood.", 345)


@design("FOD/cooking-over-a-wood-fire-2")
def _(d):
    p(d, "pot-with-lid", 320, 64, 130)
    p(d, "rock", 175, 165, 140)
    p(d, "rock", 465, 165, 140)
    p(d, "grate", 320, 135, 300, 110)
    p(d, "coals", 320, 245, 150)
    d.arrow(320, 335, 320, 290, width=4)
    lab(d, "Heat", 336, 322, "start")
    d.leader(120, 70, 220, 132)
    lab(d, "Grate", 112, 76, "end")
    d.leader(500, 300, 385, 250)
    lab(d, "Coals", 510, 306, "start")
    d.text("Food above the coals, never in the flames", 320, 24, size=15, fill="#4a4238")


@design("FOD/cooking-over-a-wood-fire-3")
def _(d):
    d.line(60, 290, 580, 290, width=4)
    p(d, "coals", 320, 170, 200)
    d.arrow(60, 252, 290, 252, width=4)
    lab(d, "Air gap", 60, 318, "start")
    lab(d, "Ash", 540, 90, "start")
    d.leader(536, 86, 340, 160)
    lab(d, "Coals", 540, 190, "start")
    d.leader(536, 186, 395, 200)
    caption(d, "Air must reach the coals from below.", 346)


@design("FOD/cooking-without-gas-1")
def _(d):
    p(d, "pot-with-lid", 150, 150, 170)
    p(d, "flame", 150, 245, 100)
    lab(d, "Boil", 150, 318)
    d.arrow(250, 160, 390, 160)
    p(d, "pot-with-lid", 500, 120, 130)
    p(d, "blanket", 500, 166, 190)
    lab(d, "Wrap", 500, 318)
    d.text("Food keeps cooking after the flame is off", 320, 34, size=15, fill="#4a4238")


@design("FOD/cooking-without-gas-2")
def _(d):
    d.line(320, 40, 320, 310, dash="9 7")
    p(d, "pot-with-lid", 150, 110, 190)
    p(d, "flame", 150, 205, 70)
    p(d, "pot-with-lid", 490, 110, 190)
    p(d, "flame", 490, 210, 190)
    d.text("Simmer", 150, 318, size=18, weight=600)
    d.text("Roaring", 490, 318, size=18, weight=600)
    d.piece("do", 120, 24, 44)
    d.piece("do-not", 470, 24, 44)


@design("FOD/cooking-without-gas-3")
def _(d):
    d.rect(80, 40, 320, 250, fill=PAPER)
    p(d, "pot-with-lid", 240, 105, 130)
    p(d, "blanket", 240, 165, 250)
    d.leader(500, 80, 300, 100)
    lab(d, "Pot", 510, 86, "start")
    d.leader(500, 180, 340, 190)
    lab(d, "Blanket", 510, 186, "start")
    d.leader(500, 270, 400, 270)
    lab(d, "Box", 510, 276, "start")
    caption(d, "Insulation layers hold heat through a slow cook.", 336)


@design("FOD/cooking-without-gas-4")
def _(d):
    d.rect(60, 24, 520, 280, fill=CREAM)
    d.line(60, 74, 580, 74)
    d.line(200, 24, 200, 304)
    d.line(390, 24, 390, 304)
    for x, s in [(130, "Fuel"), (295, "Quantity"), (485, "Days of use")]:
        lab(d, s, x, 57)
    for i, n in enumerate(["log-stack", "coals", "tinder-pile"]):
        y = 74 + i * 76
        if i:
            d.line(60, y, 580, y)
        p(d, n, 130, y + 38, 100)
    caption(d, "Count fuel, not recipes, to start the plan.", 336)


@design("FOD/drying-fruit-at-home-1")
def _(d):
    p(d, "sun", 90, 80, 120)
    p(d, "tray", 280, 220, 220)
    p(d, "fruit-slice", 240, 192, 60)
    p(d, "fruit-slice", 280, 192, 60)
    p(d, "fruit-slice", 320, 192, 60)
    p(d, "cloth", 280, 150, 200)
    d.line(130, 275, 440, 275, width=4)
    lab(d, "Tray in full sun", 285, 306)
    d.leader(500, 70, 340, 130)
    lab(d, "Cover", 510, 76, "start")
    d.arrow(450, 215, 490, 215, width=4)
    chip(d, 565, 215, 100, 60, "Indoors\nat night", size=15)
    caption(d, "The cover keeps insects off.", 346)


@design("FOD/drying-fruit-at-home-2")
def _(d):
    d.line(320, 40, 320, 310, dash="9 7")
    p(d, "tray", 160, 220, 220)
    for x in (110, 160, 210):
        p(d, "fruit-slice", x, 198, 60)
    p(d, "tray", 480, 220, 220)
    p(d, "fruit-slice", 420, 208, 40)
    p(d, "fruit-slice", 470, 188, 80)
    p(d, "fruit-slice", 530, 208, 40)
    p(d, "caution", 540, 175, 56)
    lab(d, "Even batch", 160, 318, size=18)
    lab(d, "Mixed batch", 480, 318, size=18)


@design("FOD/drying-fruit-at-home-3")
def _(d):
    p(d, "tray", 320, 215, 240)
    for x in (270, 320, 370):
        p(d, "fruit-slice", x, 200, 60)
    d.arrow(50, 228, 215, 228, width=4)
    lab(d, "Air in", 125, 275)
    d.arrow(210, 145, 440, 145, width=4)
    d.arrow(450, 145, 570, 70, width=4)
    lab(d, "Air out", 570, 52, "end")
    d.leader(110, 130, 280, 192)
    lab(d, "Slices", 100, 126, "end")


@design("FOD/drying-fruit-at-home-4")
def _(d):
    for i, (w, s) in enumerate([(150, "Fresh"), (120, "Leathery"), (90, "Dry")]):
        cx = 110 + i * 210
        p(d, "fruit-slice", cx, 170, w)
        lab(d, s, cx, 270, size=18)
        d.badge(i + 1, cx, 80, 18)
        if i < 2:
            d.arrow(cx + 85, 170, cx + 125, 170)
    caption(d, "Judge dryness by texture, not by days.", 340)


@design("FOD/drying-herbs-at-home-1")
def _(d):
    d.line(180, 40, 460, 40, width=5)
    d.line(320, 40, 320, 75, width=3)
    p(d, "rope-coil", 320, 108, 90)
    d.line(320, 138, 320, 185, width=3)
    chip(d, 320, 215, 130, 54, "Herbs")
    lab(d, "String", 355, 90, "start")
    d.arrow(120, 215, 244, 215, width=4)
    d.arrow(520, 215, 396, 215, width=4)
    d.arrow(320, 320, 320, 252, width=4)
    lab(d, "Airflow", 120, 250, "start")
    caption(d, "Airflow and warm dry air decide the speed.", 346)


@design("FOD/edible-wild-plants-1")
def _(d):
    d.rect(120, 20, 400, 296, fill=CREAM)
    d.line(120, 64, 520, 64)
    d.line(380, 20, 380, 316)
    lab(d, "Feature", 250, 50)
    lab(d, "Matches", 450, 50)
    for i, s in enumerate(["Leaves", "Stems", "Flowers", "Smell", "Habitat"]):
        y = 64 + i * 50.4
        if i:
            d.line(120, y, 520, y)
        lab(d, s, 190, y + 32, "start")
        d.tick(450, y + 25, 15)
    p(d, "leaf", 155, 64 + 25, 44)
    caption(d, "One feature never confirms a plant.", 340)


@design("FOD/edible-wild-plants-2")
def _(d):
    d.line(30, 262, 610, 262, width=4)
    for cx, item, s in [(130, "leaf", "Species 1"), (320, "shrub", "Species 2"), (510, "berry-cluster", "Species 3")]:
        p(d, "bag", cx, 205, 140)
        p(d, item, cx, 82, 90)
        lab(d, s, cx, 300)
    caption(d, "Keep species apart.", 346)


@design("FOD/edible-wild-plants-3")
def _(d):
    d.line(320, 40, 320, 300, dash="9 7")
    p(d, "leaf", 160, 150, 170)
    p(d, "leaf", 480, 150, 170)
    d.piece("do", 130, 22, 44)
    d.piece("do-not", 450, 22, 44)
    lab(d, "Edible herb", 188, 50, "start", 18)
    lab(d, "Look-alike", 508, 50, "start", 18)
    chip(d, 320, 318, 170, 36, "Check the veins", size=16)
    d.leader(235, 318, 180, 170)
    d.leader(405, 318, 460, 170)


@design("FOD/edible-wild-plants-4")
def _(d):
    flow(d, [("leaf", "Observe"), ("document", "Compare"), ("person-standing", "Confirm")], 90, w=140)
    for i in range(3):
        d.badge(i + 1, 95 + i * 225, 60, 18)
    caption(d, "A person confirms it, never a guess.", 330)


@design("FOD/eggs-and-dairy-without-a-fridge-1")
def _(d):
    p(d, "bowl", 320, 220, 300)
    p(d, "waves", 320, 195, 200)
    p(d, "egg", 270, 120, 90)
    p(d, "egg", 380, 120, 90)
    lab(d, "Fresh", 150, 112, "end")
    d.leader(160, 108, 235, 135)
    lab(d, "Old", 500, 112, "start")
    d.leader(490, 108, 415, 135)
    caption(d, "The air cell grows with age.", 340)


@design("FOD/eggs-and-dairy-without-a-fridge-2")
def _(d):
    p(d, "pot-with-lid", 170, 150, 170)
    p(d, "flame", 170, 245, 90)
    d.arrow(260, 150, 370, 150)
    p(d, "jar", 460, 150, 140)
    lab(d, "Foam", 170, 50)
    d.leader(170, 58, 170, 105)
    lab(d, "Solids", 60, 270, "start")
    d.leader(100, 258, 135, 170)
    lab(d, "Clear fat", 460, 260)
    d.leader(460, 245, 460, 195)
    caption(d, "Milk solids stay behind in the pot.", 340)


@design("FOD/eggs-and-dairy-without-a-fridge-3")
def _(d):
    p(d, "pot-with-lid", 210, 130, 200)
    p(d, "coals", 210, 245, 170)
    p(d, "spoon", 400, 130, 110)
    p(d, "arrow-loop", 520, 130, 100)
    lab(d, "Stir", 520, 214)
    lab(d, "Coals", 330, 266, "start")
    d.leader(326, 262, 275, 255)
    caption(d, "Stirring stops scorching.", 340)


@design("FOD/eggs-and-dairy-without-a-fridge-4")
def _(d):
    d.rect(30, 30, 580, 250, fill=PAPER, dash="10 8")
    d.line(80, 230, 560, 230, width=6)
    p(d, "tray", 230, 205, 170)
    for x in (195, 230, 265):
        p(d, "egg", x, 190, 44)
    p(d, "cheese", 420, 185, 120)
    p(d, "cloth", 420, 165, 90)
    lab(d, "Eggs point down", 230, 318)
    lab(d, "Cheese in cloth", 420, 318)
    lab(d, "Cool and dark", 320, 64)


@design("FOD/feeding-children-and-older-people-1")
def _(d):
    d.rect(40, 16, 560, 290, fill=CREAM)
    d.line(40, 60, 600, 60)
    d.line(150, 16, 150, 306)
    for i, s in enumerate(["Children", "Adults", "Older people"]):
        x = 150 + i * 150
        if i:
            d.line(x, 16, x, 306)
        lab(d, s, x + 75, 45, size=16)
    for r, s in enumerate(["Breakfast", "Midday", "Evening"]):
        y = 60 + r * 82
        if r:
            d.line(40, y, 600, y)
        lab(d, s, 95, y + 46, size=16)
        for c in range(3):
            p(d, "bowl", 225 + c * 150, y + 42, 70)
    caption(d, "Protein spreads across every group.", 336)


@design("FOD/feeding-children-and-older-people-2")
def _(d):
    p(d, "person-sitting", 120, 190, 150)
    p(d, "person-sitting", 520, 180, 190)
    p(d, "bowl", 320, 215, 130)
    lab(d, "Porridge", 320, 285)
    lab(d, "Child", 120, 290)
    lab(d, "Adult", 520, 290)
    d.arrow(190, 100, 450, 100, width=3)
    d.arrow(450, 100, 190, 100, width=3)
    caption(d, "Shared and slow, paced to the child.", 340)


@design("FOD/feeding-children-and-older-people-3")
def _(d):
    d.line(30, 240, 610, 240, width=4)
    for i in range(4):
        p(d, "bowl", 90 + i * 100, 212, 80)
    p(d, "person-sitting", 520, 170, 150)
    lab(d, "Small portions", 190, 285)
    d.leader(190, 268, 190, 232)
    lab(d, "Child height", 520, 285)
    caption(d, "Portions sized for small hands and mouths.", 340)


@design("FOD/feeding-children-and-older-people-4")
def _(d):
    p(d, "spouted-cup", 130, 150, 150)
    p(d, "bowl", 340, 160, 140)
    p(d, "spoon", 500, 150, 110)
    for x in (130, 340, 500):
        d.tick(x, 60, 16)
    lab(d, "Spouted cup", 130, 250)
    lab(d, "Soft food", 340, 250)
    lab(d, "Spoon", 500, 250)
    caption(d, "For anyone who cannot manage a full cup.", 336)


@design("FOD/feeding-children-and-older-people-5")
def _(d):
    for i in range(3):
        g = 120 + i * 200
        p(d, "water-drop", g - 50, 70, 44)
        p(d, "cup", g - 50, 130, 80)
        p(d, "bowl", g + 40, 140, 90)
    d.arrow(30, 255, 610, 255, width=3)
    for x in (220, 420):
        d.circle(x, 255, 7, fill=INK)
        d.line(x, 255, x, 215, dash="5 5", width=2)
    lab(d, "Between meals", 320, 300)
    d.leader(246, 296, 224, 264)
    lab(d, "Water", 70, 38)
    lab(d, "Meal", 160, 38)


@design("FOD/fermenting-vegetables-1")
def _(d):
    p(d, "jar", 250, 195, 380, 380)
    p(d, "weight", 250, 168, 100)
    d.arrow(250, 90, 250, 36, width=4)
    lab(d, "Gas out", 270, 60, "start")
    d.line(165, 200, 335, 200, dash="7 6", width=2)
    lab(d, "Brine", 520, 246, "start")
    d.leader(515, 242, 330, 214)
    lab(d, "Weight", 520, 176, "start")
    d.leader(515, 172, 292, 168)
    lab(d, "Loose lid", 520, 116, "start")
    d.leader(515, 112, 335, 112)


@design("FOD/fermenting-vegetables-2")
def _(d):
    p(d, "jar", 250, 195, 380, 380)
    d.arrow(250, 40, 250, 92, width=4)
    d.line(160, 180, 340, 180, dash="9 7", width=3)
    p(d, "leaf", 250, 215, 80)
    p(d, "leaf", 250, 240, 80)
    lab(d, "Mould zone", 520, 150, "start")
    d.leader(515, 146, 335, 150)
    lab(d, "Brine line", 520, 216, "start")
    d.leader(515, 212, 345, 180)
    lab(d, "Pressed layers", 520, 286, "start")
    d.leader(515, 282, 295, 245)


@design("FOD/fermenting-vegetables-3")
def _(d):
    d.arrow(40, 240, 600, 240, width=4)
    for x, s in [(60, "Day one"), (580, "Week four")]:
        d.line(x, 228, x, 252, width=3)
        lab(d, s, x, 282)
    for x, s in [(200, "Bubbling"), (340, "Taste")]:
        d.circle(x, 240, 8, fill=INK)
        d.line(x, 232, x, 160, dash="5 5", width=2)
        lab(d, s, x, 146)
    d.line(440, 100, 440, 252, dash="9 7", width=3, color=RED)
    lab(d, "Sour = ready", 440, 86)
    caption(d, "Ready when it tastes sour, not when bubbling stops.", 330)


@design("FOD/fermenting-vegetables-4")
def _(d):
    p(d, "jar", 250, 195, 380, 380)
    p(d, "weight", 250, 235, 100)
    d.arrow(250, 36, 250, 92, width=4)
    d.line(160, 190, 340, 190, dash="9 7", width=3)
    p(d, "caution", 250, 158, 44)
    lab(d, "Brine line", 520, 156, "start")
    d.leader(515, 152, 345, 190)
    lab(d, "Weight", 520, 226, "start")
    d.leader(515, 222, 292, 235)
    lab(d, "Press under", 520, 286, "start")
    d.leader(515, 282, 300, 260)


@design("FOD/food-after-a-flood-1")
def _(d):
    p(d, "decision", 150, 150, 200)
    lab(d, "Water got in?", 150, 56, size=18)
    d.arrow(240, 120, 380, 70, width=4)
    d.arrow(240, 180, 380, 250, width=4)
    lab(d, "Yes", 300, 80, "end", 16)
    lab(d, "No", 300, 240, "end", 16)
    p(d, "do-not", 450, 70, 80)
    lab(d, "Discard", 540, 76, "start")
    p(d, "do", 450, 250, 80)
    lab(d, "Keep after\ncleaning", 540, 246, "start")
    caption(d, "Water entry, not appearance, decides.", 346)


@design("FOD/food-after-a-flood-2")
def _(d):
    items = [("bucket", "Rinse"), ("bucket", "Scrub\nwith bleach"), ("bucket", "Rinse"), ("sun", "Dry"), ("note", "Label")]
    w = 90
    gap = (640 - 5 * w) / 6
    for i, (pc, s) in enumerate(items):
        x = gap + i * (w + gap)
        d.piece(pc, x, 110, w)
        d.text(s, x + w / 2, 218, size=16, weight=600)
        d.badge(i + 1, x + w / 2, 80, 16)
        if i < 4:
            d.arrow(x + w + 2, 150, x + w + gap - 2, 150, width=3)
    caption(d, "Tins are dry before any label is written.", 330)


@design("FOD/food-after-a-flood-3")
def _(d):
    d.line(320, 40, 320, 310, dash="9 7")
    p(d, "tin", 160, 165, 150)
    d.arrow(30, 165, 80, 165, width=4)
    d.cross(98, 165, 14)
    lab(d, "Sealed tin seam", 160, 290, size=17)
    p(d, "box", 480, 175, 170)
    p(d, "water-drop", 420, 80, 44)
    p(d, "water-drop", 480, 70, 44)
    p(d, "water-drop", 540, 80, 44)
    d.arrow(420, 105, 435, 135, width=3)
    d.arrow(480, 98, 480, 130, width=3)
    d.arrow(540, 105, 525, 135, width=3)
    lab(d, "Plain box soaks", 480, 290, size=17)


@design("FOD/food-safety-with-limited-water-1")
def _(d):
    p(d, "bowl", 190, 215, 220)
    p(d, "waves", 190, 190, 150)
    p(d, "leaf", 190, 205, 60)
    p(d, "arrow-loop", 190, 90, 100)
    lab(d, "Swirl", 250, 70, "start")
    p(d, "bucket", 470, 195, 160)
    d.line(415, 210, 525, 210, dash="7 6", width=3)
    lab(d, "Fill line", 540, 206, "start", 16)
    caption(d, "Swirl, then change the water instead of running it.", 340)


@design("FOD/food-safety-with-limited-water-2")
def _(d):
    flow(d, [("bowl", "Dirty"), ("bucket", "Rinse"), ("bowl", "Clean")], 90, w=140, label_dy=30)
    for i in range(3):
        d.badge(i + 1, 95 + i * 225, 70, 18)
    d.line(288, 150, 352, 150, dash="6 5", width=2)
    lab(d, "Fill line", 420, 90, "start", 16)
    d.leader(416, 94, 354, 148)
    d.text("Produce moves one way only", 320, 330, size=15, fill="#4a4238")


@design("FOD/food-spoilage-and-safety-1")
def _(d):
    d.rect(250, 118, 260, 112, fill="#f9e3b4", stroke="#f9e3b4", width=1, rx=0)
    d.line(250, 60, 250, 310, width=4)
    p(d, "thermometer", 130, 185, 150, 190)
    d.line(250, 118, 510, 118, dash="9 7", width=3, color=RED)
    d.line(250, 230, 510, 230, dash="9 7", width=3, color=BLUE)
    lab(d, "60 °C", 240, 123, "end", 16)
    lab(d, "5 °C", 240, 235, "end", 16)
    lab(d, "Cooked above", 530, 80, "start", 16)
    lab(d, "Danger zone", 530, 180, "start", 16)
    lab(d, "Below", 530, 280, "start", 16)
    d.arrow(300, 100, 300, 50, width=3)
    d.arrow(300, 250, 300, 300, width=3)


@design("FOD/food-spoilage-and-safety-2")
def _(d):
    p(d, "hands", 90, 190, 130)
    p(d, "water-drop", 90, 80, 40)
    steps = ["Wet", "Soap", "Palms", "Backs", "Fingers", "Rinse"]
    for i, s in enumerate(steps):
        cx = 260 + (i % 3) * 150
        cy = 100 + (i // 3) * 130
        chip(d, cx, cy, 116, 54, s)
        d.badge(i + 1, cx - 58, cy - 27, 14)
        if i % 3 < 2:
            d.arrow(cx + 62, cy, cx + 86, cy, width=3)
    caption(d, "Each step covers a different part, so order matters.", 340)


@design("FOD/food-spoilage-and-safety-3")
def _(d):
    for y, s, x2, sp in [(90, "Hot weather", 200, "1 hour"), (220, "Normal", 440, "Longer")]:
        d.arrow(40, y + 50, 600, y + 50, width=3)
        d.circle(60, y + 50, 8, fill=INK)
        d.circle(x2, y + 50, 8, fill=INK)
        d.line(60, y + 12, x2, y + 12, width=3)
        d.line(60, y + 4, 60, y + 20, width=3)
        d.line(x2, y + 4, x2, y + 20, width=3)
        lab(d, sp, (60 + x2) / 2, y - 2, size=16)
        lab(d, s, 600, y + 30, "end")
    caption(d, "Heat shortens the safe window sharply.", 340)


@design("FOD/food-spoilage-and-safety-4")
def _(d):
    d.arrow(40, 280, 600, 280, width=4)
    d.circle(100, 280, 9, fill=INK)
    d.line(100, 270, 100, 190, dash="5 5", width=2)
    chip(d, 100, 150, 150, 52, "Cooking ends")
    d.arrow(190, 150, 285, 150, width=3)
    p(d, "caution", 320, 150, 60)
    d.arrow(355, 150, 450, 150, width=3)
    chip(d, 540, 150, 140, 52, "Cold place")
    lab(d, "Late move", 320, 215, size=16)
    caption(d, "The clock starts when cooking ends.", 340)


@design("FOD/home-canning-basics-1")
def _(d):
    d.line(320, 40, 320, 310, dash="9 7")
    p(d, "pot-with-lid", 170, 150, 200)
    lab(d, "Water-bath canner", 170, 270)
    p(d, "pot-with-lid", 440, 150, 200)
    lab(d, "Pressure canner", 440, 270)
    p(d, "jar", 580, 150, 130)
    caption(d, "Two equipment types.", 336)


@design("FOD/home-canning-basics-2")
def _(d):
    p(d, "jar", 250, 195, 380, 380)
    d.line(160, 185, 340, 185, dash="9 7", width=3)
    d.line(135, 150, 135, 185, width=3)
    d.line(127, 150, 143, 150, width=3)
    d.line(127, 185, 143, 185, width=3)
    lab(d, "Headspace", 120, 173, "end")
    lab(d, "Food level", 520, 216, "start")
    d.leader(515, 212, 342, 185)
    lab(d, "Sealed lid", 520, 90, "start")
    d.leader(515, 86, 335, 100)


@design("FOD/home-canning-basics-3")
def _(d):
    p(d, "bubble-remover", 230, 180, 340)
    lab(d, "Bubble remover", 440, 70, "start")
    d.leader(435, 66, 330, 100)
    lab(d, "Recheck headspace", 440, 230, "start")
    d.leader(435, 226, 330, 200)


@design("FOD/home-canning-basics-4")
def _(d):
    d.line(320, 40, 320, 310, dash="9 7")
    p(d, "jar", 160, 190, 300, 300)
    p(d, "jar", 480, 190, 300, 300)
    d.tick(110, 50, 16)
    d.cross(390, 50, 16)
    p(d, "open-hand", 480, 88, 90)
    lab(d, "Sealed", 160, 318, size=18)
    lab(d, "Unsealed", 480, 318, size=18)
