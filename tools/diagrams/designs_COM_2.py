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


@design("COM/sending-messages-without-internet-1")
def _(d):
    d.piece("ladder", 16, 50, 240)
    labels = ["Written notes", "Runners", "Amateur radio", "Short-range radio", "Mobile text"]
    for i, s in enumerate(labels):
        chip(d, 420, 52 + i * 54, 220, 42, s, fill=YELLOW if i < 2 else CREAM)
        d.badge(5 - i, 290, 52 + i * 54, 15)
    d.line(556, 30, 556, 104, width=4, color=GREEN)
    d.text("Backup", 566, 72, size=15, weight=600, anchor="start", fill=GREEN)
    caption(d, "Top two need no power or network.")


@design("COM/sending-messages-without-internet-2")
def _(d):
    xs = [90, 320, 550]
    for x, s in zip(xs, ["Sender", "Runner", "Recipient"]):
        chip(d, x, 100, 130, 60, s)
    d.arrow(159, 100, 251, 100)
    d.arrow(389, 100, 481, 100)
    d.text("writes note", 205, 78, size=15, weight=600)
    d.text("carries", 435, 78, size=15, weight=600)
    d.path("M550 132L550 230L90 230L90 140", stroke=BLUE, width=4)
    d.arrow(90, 150, 90, 134, color=BLUE)
    d.text("Reply returns", 320, 260, size=17, weight=600, fill=BLUE)
    d.text("recipient replies", 528, 175, size=15, weight=600, anchor="end")
    caption(d, "The loop closes only when the reply returns.")


@design("COM/sending-messages-without-internet-3")
def _(d):
    d.piece("radio", 16, 30, 120)
    d.piece("radio", 504, 30, 120)
    d.arrow(150, 100, 490, 100)
    d.arrow(490, 100, 150, 100, color=BLUE)
    items = ["Call", "Identify", "Message", "Key\nrelease", "Reply"]
    w, g = 112, 12
    for i, s in enumerate(items):
        cx = 16 + w / 2 + i * (w + g)
        chip(d, cx, 220, w, 64, s, fill=YELLOW if i == 3 else CREAM)
        d.badge(i + 1, cx, 170, 16)
    caption(d, "Key release is its own step so the other side can answer.")


@design("COM/sending-messages-without-internet-4")
def _(d):
    d.piece("bag", 60, 50, 280)
    d.rect(140, 160, 120, 70, fill=CREAM)
    d.line(140, 195, 260, 195, width=2)
    d.text("Date", 200, 184, size=16, weight=600)
    d.text("Recipient", 200, 220, size=16, weight=600)
    d.leader(420, 130, 262, 175)
    d.text("Routing label", 430, 136, size=17, weight=600, anchor="start")
    d.leader(420, 250, 262, 215)
    d.text("Delivered unopened", 430, 256, size=17, weight=600, anchor="start")
    caption(d, "The outside carries routing; the runner never opens it.")


@design("COM/signalling-for-help-1")
def _(d):
    d.arrow(30, 150, 610, 150)
    for x in (110, 170, 230):
        d.piece("timeline-marker", x - 45, 80, 90)
    d.text("Three blasts", 170, 60, size=17, weight=600)
    d.arrow(270, 200, 450, 200)
    d.arrow(450, 200, 270, 200)
    d.text("One-minute gap: listen", 360, 230, size=17, weight=600)
    d.path("M580 170C600 290 120 300 110 175", stroke=BLUE, width=4)
    d.arrow(110, 190, 110, 172, color=BLUE)
    d.text("Repeat", 360, 300, size=17, weight=600, fill=BLUE)


@design("COM/signalling-for-help-2")
def _(d):
    for x, p, s in ((16, "sos-ground-signal", "SOS letters"), (225, "ground-signal-v", "V sign"), (434, "signal-fires-3", "Three fires")):
        d.piece(p, x, 70, 190)
        d.text(s, x + 95, 250, size=17, weight=600)
    caption(d, "Contrast and spacing keep each shape readable from above.", 310)


@design("COM/signalling-for-help-3")
def _(d):
    d.piece("sun", 16, 40, 150)
    d.piece("signal-mirror", 245, 130, 150)
    d.piece("airplane", 470, 40, 150)
    d.line(150, 110, 285, 185, dash="9 7", width=3, color=BLUE)
    d.line(335, 188, 490, 112, dash="9 7", width=3, color=BLUE)
    d.text("Sun", 90, 215, size=17, weight=600)
    d.text("Mirror", 320, 270, size=17, weight=600)
    d.text("Aircraft", 545, 215, size=17, weight=600)
    caption(d, "Mirror sits between sun and target.")


@design("COM/signalling-for-help-4")
def _(d):
    d.rect(16, 30, 290, 270, fill=PAPER)
    d.rect(334, 30, 290, 270, fill=PAPER)
    d.arrow(161, 210, 161, 70, width=3)
    d.text("Thin plume", 161, 250, size=17, weight=600)
    d.arrow(479, 150, 479, 66, width=14)
    d.piece("flame", 429, 150, 100)
    d.piece("leaf", 520, 190, 70)
    d.text("Thick plume", 479, 275, size=17, weight=600)
    d.text("Green material", 560, 180, size=15, weight=600)
    caption(d, "Green material thickens the smoke.", 330)


@design("COM/two-way-radio-basics-1")
def _(d):
    d.piece("radio", 16, 40, 130)
    d.piece("radio", 494, 40, 130)
    d.arrow(160, 90, 480, 90)
    d.arrow(480, 120, 160, 120, color=BLUE)
    items = ["Call", "Identify", "Message", "Release", "Reply"]
    w, g = 112, 12
    for i, s in enumerate(items):
        cx = 16 + w / 2 + i * (w + g)
        chip(d, cx, 230, w, 56, s, fill=YELLOW if i == 3 else CREAM)
        d.badge(i + 1, cx, 185, 15)
    caption(d, "Release comes before the reply, leaving the channel clear.")


@design("COM/two-way-radio-basics-2")
def _(d):
    d.piece("radio", 190, 50, 260)
    d.leader(100, 62, 318, 66)
    d.text("Antenna", 90, 68, size=17, weight=600, anchor="end")
    d.leader(540, 100, 378, 88)
    d.text("Signal", 550, 106, size=17, weight=600, anchor="start")
    d.leader(100, 200, 300, 200)
    d.text("Grip point", 90, 206, size=17, weight=600, anchor="end")
    caption(d, "Hold below the antenna, clear of the face.")


@design("COM/verifying-rumours-1")
def _(d):
    qs = ["Who said it?", "How do they know?", "Confirmed elsewhere?", "Useful?"]
    w, g = 130, 29
    for i, s in enumerate(qs):
        x = 16 + i * (w + g) + 0
        d.piece("step-box", x, 50, w)
        d.text(s, x + w / 2, 180, size=15, weight=600)
        d.tick(x + w / 2, 225, 16)
        if i < 3:
            d.arrow(x + w + 2, 98, x + w + g - 2, 98)
    caption(d, "A report must pass every box before it is acted on or shared.", 300)


@design("COM/verifying-rumours-2")
def _(d):
    d.piece("person-standing", 16, 40, 110)
    d.text("Witness", 71, 150, size=16, weight=600)
    xs = (230, 380, 530)
    for i, x in enumerate(xs):
        chip(d, x, 100, 90, 50, "Link")
        d.arrow(130 if i == 0 else xs[i - 1] + 47, 100, x - 47, 100)
    d.piece("do-not", 355, 30, 50)
    d.piece("bulletin", 245, 190, 150)
    d.text("Bulletin", 410, 290, size=17, weight=600, anchor="start")
    for x in xs:
        d.leader(320, 198, x, 128)
    caption(d, "One broken link leaves the report unconfirmed.")


@design("COM/verifying-rumours-3")
def _(d):
    d.piece("step-box", 16, 120, 120)
    d.text("First message", 76, 235, size=16, weight=600)
    for y in (60, 140, 220):
        d.arrow(150, 180, 300, y + 20)
        chip(d, 370, y + 20, 120, 50, "Forward")
    d.text("Forwarded copies", 370, 40, size=16, weight=600)
    d.path("M490 120L610 120L610 250L490 250Z", stroke=INK, width=3, dash="9 7")
    d.text("Source\nmissing", 550, 180, size=17, weight=600)
    caption(d, "Copies multiply while the source is missing.")
