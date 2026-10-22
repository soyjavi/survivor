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


def table(d, x, y, colw, rowh, header, rows):
    xs = [x]
    for w in colw:
        xs.append(xs[-1] + w)
    total = sum(colw)
    d.rect(x, y, total, rowh, fill=SAND, rx=6)
    for i, h in enumerate(header):
        d.text(h, xs[i] + colw[i] / 2, y + rowh / 2 + 6, size=16, weight=600)
    for r, label in enumerate(rows):
        ry = y + rowh * (r + 1)
        d.rect(x, ry, total, rowh, fill=CREAM, rx=6)
        d.text(label, xs[0] + 12, ry + rowh / 2 + 6, size=16, weight=600, anchor="start")
    for xv in xs[1:-1]:
        d.line(xv, y, xv, y + rowh * (len(rows) + 1), width=2)
    return xs


@design("MED/controlling-bleeding-1")
def _(d):
    d.piece("person-kneeling", 30, 50, 280)
    d.piece("bleeding", 390, 190, 190)
    d.arrow(485, 120, 485, 215)
    d.text("Body weight", 485, 100, size=17, weight=600)
    caption(d, "Pressure comes from leaning, not the arms.")


@design("MED/controlling-bleeding-2")
def _(d):
    d.piece("bleeding", 20, 60, 270)
    d.arrow(295, 175, 345, 175)
    d.piece("gauze-pad", 360, 50, 260)
    d.text("Deep cut", 155, 270, size=17, weight=600)
    d.text("Gauze-pad layers", 490, 270, size=17, weight=600)
    caption(d, "Packing fills the full depth before the outer pad.")


@design("MED/controlling-bleeding-3")
def _(d):
    d.piece("tourniquet", 20, 50, 330)
    d.piece("bleeding", 440, 120, 170)
    d.arrow(375, 180, 435, 180, width=3)
    d.arrow(435, 180, 375, 180, width=3)
    d.text("2-3 inches", 405, 150, size=15, weight=600)
    d.leader(70, 48, 120, 134)
    d.text("Band", 60, 44, size=16, weight=600, anchor="end")
    d.leader(310, 48, 262, 113)
    d.text("Windlass", 320, 44, size=16, weight=600, anchor="start")
    chip(d, 190, 290, 200, 40, "Time written", size=16)
    caption(d, "Tighten until bleeding stops.")


@design("MED/controlling-bleeding-4")
def _(d):
    d.piece("gauze-pad", 220, 215, 150)
    d.piece("gauze-pad", 220, 130, 150)
    d.piece("gauze-pad", 220, 45, 150)
    d.leader(480, 262, 360, 262)
    d.text("Soaked pad", 490, 267, size=16, weight=600, anchor="start")
    d.leader(480, 128, 360, 100)
    d.leader(480, 158, 360, 185)
    d.text("New pads", 490, 148, size=16, weight=600, anchor="start")
    d.arrow(215, 262, 120, 262, color=RED)
    d.cross(92, 262, 16)
    d.text("Never removed", 92, 305, size=16, weight=600)


@design("MED/controlling-bleeding-5")
def _(d):
    d.piece("person-lying", 20, 20, 360)
    d.piece("blanket", 400, 185, 150)
    d.arrow(385, 215, 385, 160)
    d.text("Legs raised", 385, 140, size=16, weight=600)
    d.text("Blanket", 540, 305, size=16, weight=600)
    chip(d, 320, 322, 340, 36, "Legs down if leg or hip injury", size=15)


@design("MED/diarrhoea-and-dehydration-1")
def _(d):
    flow(d, [("jar", "Litre"), ("spoon", "Spoon"), ("cup", "Cup")], 70, w=150, arrow=False)
    caption(d, "The mix is measured, not estimated.", 300)


@design("MED/diarrhoea-and-dehydration-2")
def _(d):
    xs = table(d, 16, 30, [156, 150, 150, 150], 44, ["", "Mild", "Moderate", "Severe"],
               ["Thirst", "Dizziness", "Sunken eyes", "No tears", "Sleepiness"])
    start = [0, 1, 1, 2, 2]
    for r, s in enumerate(start):
        for c in range(s, 3):
            d.tick(xs[c + 1] + 75, 30 + 44 * (r + 1) + 22, 12)
    caption(d, "Severity rises across the columns.", 342)


@design("MED/diarrhoea-and-dehydration-3")
def _(d):
    d.arrow(30, 230, 610, 230)
    for x in (80, 190, 300):
        d.piece("cup", x - 45, 100, 90)
        d.line(x, 180, x, 230, width=3)
    d.piece("cup", 390, 40, 150)
    d.line(465, 155, 465, 230, width=3)
    d.text("Small cup", 190, 268, size=16, weight=600)
    d.text("Larger cup after each loss", 465, 268, size=16, weight=600)
    caption(d, "Fluid is paced to losses, not drunk at once.")


@design("MED/diarrhoea-and-dehydration-4")
def _(d):
    flow(d, [("spoon", "Level spoon"), ("cup", "Cup"), ("jar", "Litre")], 50, w=150, arrow=False)
    chip(d, 320, 270, 560, 44, "6 level tsp sugar, half tsp salt, 1 litre", size=16)
    caption(d, "Level, not heaped.")


@design("MED/dislocations-recognition-and-care-1")
def _(d):
    d.piece("person-standing", 50, 30, 300)
    d.leader(480, 90, 230, 105)
    d.text("Shoulder", 490, 96, size=16, weight=600, anchor="start")
    d.arrow(520, 200, 440, 200)
    d.text("Direction of displacement", 480, 240, size=16, weight=600)
    caption(d, "Shows which way the joint moved, to guide support.", 345)


@design("MED/dislocations-recognition-and-care-2")
def _(d):
    flow(d, [("step-1", "Check circulation\nand sensation"), ("step-2", "Support joint\nin position"), ("step-3", "Move only\nafter checks")], 20, w=110, label_dy=24)
    d.piece("warning", 110, 200, 90)
    d.text("Loss of colour\nor feeling", 155, 315, size=16, weight=600)
    d.arrow(215, 240, 395, 240)
    d.piece("phone-call", 410, 190, 110)
    d.text("Call for help", 465, 315, size=16, weight=600)


@design("MED/drowning-and-first-aid-after-a-flood-1")
def _(d):
    d.piece("ground-line", 10, 96, 260)
    d.piece("person-standing", 50, 91, 130)
    d.piece("river", 380, 92, 240)
    d.piece("person-sitting", 480, 52, 110)
    d.piece("rock", 290, 115, 80)
    d.arrow(200, 105, 470, 105)
    d.text("Reach or throw", 335, 82, size=16, weight=600)
    d.text("Debris", 330, 215, size=16, weight=600)
    d.text("Current", 500, 285, size=16, weight=600)
    d.piece("do-not", 30, 262, 55)
    d.text("Entering the water", 95, 288, size=15, weight=600, anchor="start")
    caption(d, "The rescuer stays out of the water.")


@design("MED/drowning-and-first-aid-after-a-flood-2")
def _(d):
    d.piece("ground-line", 10, 96, 250)
    d.piece("person-standing", 30, 91, 130)
    d.piece("rope-coil", 150, 115, 100)
    d.piece("post", 250, 70, 80)
    d.text("Fixed post", 290, 190, size=16, weight=600)
    d.line(240, 150, 286, 128, width=3)
    d.piece("river", 380, 100, 240)
    d.piece("person-sitting", 480, 62, 110)
    d.curve_arrow("M175 105C260 10 400 10 470 100", (470, 100), 0.7)
    caption(d, "The rope stays anchored while the person is pulled in.")


@design("MED/drowning-and-first-aid-after-a-flood-3")
def _(d):
    d.piece("recovery-position", 140, 40, 360)
    d.leader(320, 120, 300, 232)
    d.text("On side", 320, 108, size=16, weight=600)
    d.leader(130, 240, 190, 242)
    d.text("Head tilted back", 126, 246, size=16, weight=600, anchor="end")
    d.leader(470, 150, 405, 205)
    d.text("Top leg bent", 475, 150, size=16, weight=600, anchor="start")
    caption(d, "Keeps the airway clear.")


@design("MED/drowning-and-first-aid-after-a-flood-4")
def _(d):
    flow(d, [("step-1", "Remove wet\nclothes"), ("step-2", "Dry layers"), ("step-3", "Blanket"), ("step-box", "Off cold\nground")], 90, w=110)
    caption(d, "The ground draws heat, so insulate underneath.", 300)


@design("MED/ear-pain-and-infection-1")
def _(d):
    for i, s in enumerate(["Outer ear", "Middle ear", "Inner ear"]):
        chip(d, 140 + i * 180, 140, 180, 110, s, size=17)
    d.line(230, 85, 230, 195, dash="8 6", width=4, color=RED)
    d.text("Eardrum", 230, 290, size=16, weight=600)
    d.leader(230, 270, 230, 200)
    caption(d, "Infection sits behind the eardrum.")


@design("MED/ear-pain-and-infection-2")
def _(d):
    d.piece("decision", 30, 110, 170)
    d.text("Pain type?", 115, 270, size=16, weight=600)
    d.piece("do", 390, 30, 110)
    d.piece("warning", 390, 190, 110)
    d.arrow(210, 170, 380, 100)
    d.arrow(210, 190, 380, 240)
    d.text("Comfort care\nfor mild pain", 515, 80, size=16, weight=600, anchor="start")
    d.text("Professional\nassessment", 515, 240, size=16, weight=600, anchor="start")
    d.text("Drainage, fever or facial weakness", 445, 330, size=15, weight=600)


@design("MED/eye-injuries-1")
def _(d):
    d.piece("eye", 150, 50, 340)
    d.piece("water-drop", 90, 140, 60)
    d.arrow(170, 270, 470, 270)
    d.text("Inner corner", 160, 322, size=16, weight=600, anchor="start")
    d.text("Outer corner", 480, 322, size=16, weight=600, anchor="end")
    d.text("Rinse direction", 320, 322, size=16, weight=600)


@design("MED/eye-injuries-2")
def _(d):
    d.piece("eye", 60, 110, 340)
    d.leader(180, 70, 235, 200)
    d.text("Debris", 170, 64, size=16, weight=600, anchor="end")
    d.text("Lid lifted", 330, 60, size=16, weight=600)
    d.curve_arrow("M250 130C290 80 340 80 370 120", (370, 120), 1.0)
    d.piece("do-not", 470, 130, 100)
    d.text("Rubbing", 520, 270, size=16, weight=600)


@design("MED/eye-injuries-3")
def _(d):
    d.piece("person-sitting", 40, 70, 230)
    d.piece("water-drop", 280, 40, 60)
    d.arrow(330, 95, 450, 170)
    d.text("Steady stream", 395, 215, size=16, weight=600, anchor="start")
    chip(d, 160, 290, 220, 40, "Injured side down", size=16)
    caption(d, "Water runs away from the uninjured eye.", 346)


@design("MED/eye-injuries-4")
def _(d):
    d.piece("cup", 130, 20, 130)
    d.arrow(195, 125, 195, 170)
    d.piece("eye", 60, 170, 270)
    d.text("Shield", 140, 70, size=16, weight=600, anchor="end")
    d.piece("do-not", 320, 40, 90)
    d.text("Pressing", 365, 160, size=16, weight=600)
    d.leader(450, 280, 250, 270)
    d.text("Object", 460, 286, size=16, weight=600, anchor="start")
    caption(d, "The object stays in place and is never pressed.")


@design("MED/eye-injuries-5")
def _(d):
    d.piece("eye", 40, 160, 260)
    d.piece("cup", 110, 70, 130)
    d.leader(110, 135, 100, 215)
    d.text("Bone rim", 110, 130, size=16, weight=600, anchor="end")
    d.piece("tape", 360, 150, 110)
    d.arrow(355, 210, 290, 190, width=3)
    d.text("Tape", 415, 270, size=16, weight=600)
    d.piece("caution", 510, 30, 80)
    chip(d, 560, 160, 130, 60, "No pressure\non eye", size=15)


@design("MED/fever-1")
def _(d):
    d.piece("thermometer", 40, 80, 180)
    for y, s, f in [(60, "Monitor", GREEN), (150, "Seek care soon", YELLOW), (240, "Emergency", RED)]:
        chip(d, 440, y + 25, 230, 56, s, fill=f)
        d.arrow(230, 170, 310, y + 25, width=3)
    caption(d, "Behaviour, not the reading alone, decides the zone.")


@design("MED/fever-2")
def _(d):
    d.piece("person-sitting", 70, 50, 230)
    d.piece("thermometer", 370, 60, 150)
    d.arrow(375, 150, 240, 160)
    d.leader(100, 290, 190, 185)
    d.text("Arm against chest", 30, 316, size=16, weight=600, anchor="start")
    d.text("Under arm", 440, 55, size=16, weight=600)
    caption(d, "The arm stays closed so the reading holds steady.")


@design("MED/fever-3")
def _(d):
    d.piece("pills", 291, 20, 90)
    d.piece("cup", 505, 20, 90)
    xs = table(d, 16, 120, [100, 120, 200, 188], 44, ["Time", "Reading", "Medicine given", "Fluids taken"], ["", "", ""])
    caption(d, "Each entry is written before the next dose.", 340)


@design("MED/fever-4")
def _(d):
    flow(d, [("step-box", "Monitor\nat home"), ("step-box", "Seek care\nsoon"), ("step-box", "Call emergency\nhelp")], 90, w=150)
    d.piece("warning", 485, 30, 70)
    caption(d, "Breathing trouble or chest pain raises the zone.", 330)


@design("MED/field-dressings-and-pressure-bandages-1")
def _(d):
    flow(d, [("bleeding", "Wound"), ("gauze-pad", "Thick pad"), ("bandage-roll", "Overlapping\nturns"), ("limb-outline", "Limb")], 110, w=130)
    d.arrow(551, 125, 551, 75)
    d.text("Upward", 551, 62, size=16, weight=600)


@design("MED/field-dressings-and-pressure-bandages-2")
def _(d):
    d.piece("gauze-pad", 40, 190, 150)
    d.piece("gauze-pad", 40, 90, 150)
    d.leader(300, 240, 180, 255)
    d.text("Soaked pad", 310, 246, size=16, weight=600, anchor="start")
    d.leader(300, 140, 180, 155)
    d.text("Fresh pad", 310, 146, size=16, weight=600, anchor="start")
    d.piece("bandage-roll", 450, 130, 140)
    d.text("Bandage", 520, 270, size=16, weight=600)
    d.arrow(440, 190, 250, 190, dash="8 6")
    caption(d, "The old pad stays under the new one.")


@design("MED/foot-care-and-blisters-1")
def _(d):
    d.piece("footprints", 100, 20, 330)
    d.leader(470, 60, 298, 67)
    d.text("Between toes", 480, 66, size=16, weight=600, anchor="start")
    d.leader(470, 140, 324, 112)
    d.text("Ball of foot", 480, 146, size=16, weight=600, anchor="start")
    d.leader(128, 210, 206, 208)
    d.text("Heel", 118, 216, size=16, weight=600, anchor="end")
    caption(d, "Where friction most often starts a blister.")


@design("MED/foot-care-and-blisters-2")
def _(d):
    for i, s in enumerate(["Intact roof", "Fluid pocket", "Healing skin"]):
        chip(d, 220, 70 + i * 80, 260, 64, s, size=17)
    d.piece("water-drop", 450, 125, 70)
    d.leader(450, 170, 350, 150)
    caption(d, "Keep the roof intact to protect the skin beneath.")


@design("MED/fractures-and-splinting-1")
def _(d):
    d.piece("splint", 20, 60, 200)
    chip(d, 320, 130, 120, 56, "Joint", size=17)
    d.piece("splint", 420, 60, 200)
    d.text("Support above", 120, 240, size=16, weight=600)
    d.text("Support below", 520, 240, size=16, weight=600)
    d.piece("bandage-roll", 245, 180, 150)
    d.text("Padding and bandages", 320, 320, size=16, weight=600)
    caption(d, "Two supports hold the joint still.", 348)


@design("MED/fractures-and-splinting-2")
def _(d):
    rows = ["Colour", "Warmth", "Movement", "Feeling"]
    for i, s in enumerate(rows):
        y = 40 + i * 62
        d.rect(120, y, 400, 52, fill=CREAM, rx=8)
        d.text(s, 150, y + 33, size=18, weight=600, anchor="start")
        d.tick(480, y + 26, 15)
    caption(d, "Checks are made after the splint goes on, not before.", 330)


@design("MED/fractures-and-splinting-3")
def _(d):
    d.piece("person-kneeling", 30, 70, 220)
    chip(d, 140, 300, 230, 40, "Support wrist and elbow", size=15)
    d.piece("padding", 440, 120, 150)
    d.arrow(430, 190, 300, 190)
    d.text("Slide padding\nunder forearm", 365, 120, size=16, weight=600)
    caption(d, "Slide padding in rather than lifting the limb.", 345)


@design("MED/fractures-and-splinting-4")
def _(d):
    for i, (p, s) in enumerate([("limb-outline", "Limb"), ("padding", "Padding"), ("splint", "Rigid support")]):
        d.piece(p, 60, 4 + i * 106, 160)
        d.text(s, 260, 74 + i * 106, size=17, weight=600, anchor="start")
    caption(d, "A soft gap keeps hard edges off the skin.", 346)


@design("MED/frostbite-recognition-and-care-1")
def _(d):
    flow(d, [("step-box", "Frostnip"), ("step-box", "Superficial\nfrostbite"), ("step-box", "Deep\nfrostbite")], 80, w=160)
    caption(d, "Damage moves from surface to deeper tissue.", 320)


@design("MED/frostbite-recognition-and-care-2")
def _(d):
    flow(d, [("step-1", "Rewarm in comfortably\nwarm water"), ("step-2", "Dry protection"), ("step-3", "Assessment if\nstill discoloured")], 70, w=130)
    caption(d, "Rewarming comes first.", 320)


@design("MED/head-injury-and-concussion-2")
def _(d):
    xs = table(d, 16, 20, [208, 200, 200], 48, ["Sign", "Normal", "Call for help"],
               ["Consciousness", "Confusion", "Vomiting", "Pupils", "Weakness"])
    d.tick(xs[1] + 150, 44, 12)
    d.cross(xs[2] + 170, 44, 12)
    caption(d, "Each sign is checked and recorded separately.", 346)


@design("MED/heat-illness-and-hypothermia-1")
def _(d):
    xs = table(d, 16, 30, [150, 150, 150, 150], 56, ["", "Heat exhaustion", "Heatstroke", "Hypothermia"],
               ["Signs", "First response", "Confusion"])
    for c in range(3):
        d.tick(xs[c + 1] + 75, 30 + 56 * 3 + 28, 14)
    caption(d, "Confusion is an early warning shared by all three.", 320)


@design("MED/heat-illness-and-hypothermia-2")
def _(d):
    d.piece("person-sitting", 190, 40, 250)
    d.leader(115, 86, 270, 110)
    d.text("Neck", 105, 92, size=16, weight=600, anchor="end")
    d.leader(115, 150, 272, 150)
    d.text("Armpits", 105, 156, size=16, weight=600, anchor="end")
    d.leader(115, 212, 298, 182)
    d.text("Groin", 105, 218, size=16, weight=600, anchor="end")
    d.piece("fan", 490, 90, 110)
    d.arrow(505, 150, 430, 150)
    d.text("Fan", 545, 205, size=16, weight=600)
    caption(d, "Large vessels lie close to the skin there.")


@design("MED/heat-illness-and-hypothermia-3")
def _(d):
    flow(d, [("step-1", "Dry layers"), ("step-2", "Blanket"), ("step-3", "Warm drink"), ("step-box", "Heat to chest\nand trunk")], 80, w=110)
    caption(d, "The centre warms first.", 320)


@design("MED/heat-illness-and-hypothermia-4")
def _(d):
    d.piece("tarp-a-frame", 30, 40, 250)
    d.text("Shade", 150, 235, size=16, weight=600)
    d.piece("person-sitting", 300, 100, 170)
    d.arrow(590, 205, 510, 205)
    d.text("Moving air", 550, 250, size=16, weight=600)
    caption(d, "Shade and moving air work together.")


@design("MED/heat-illness-and-hypothermia-5")
def _(d):
    d.arrow(80, 310, 80, 30)
    for i, s in enumerate(["Waterproof outer", "Insulating layer", "Thin dry base"]):
        d.piece("step-box", 150, 20 + i * 100, 120)
        d.text(s, 300, 74 + i * 100, size=17, weight=600, anchor="start")
    caption(d, "Dry layers go on from the body outward.", 346)
