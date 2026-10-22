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


@design("SHL/tarp-shelters-1")
def _(d):
    d.piece("tarp-a-frame", 30, 80, 200)
    d.piece("lean-to", 300, 80, 200)
    d.arrow(520, 230, 600, 230)
    d.text("Wind", 560, 262, size=16, weight=600)
    d.text("A-frame", 130, 270, size=16, weight=600)
    d.text("Lean-to", 400, 270, size=16, weight=600)
    caption(d, "The slope sheds rain.")


@design("SHL/tarp-shelters-2")
def _(d):
    d.piece("rope-coil", 40, 100, 170)
    d.line(190, 170, 450, 170, width=5)
    d.text("Standing end", 320, 150, size=16, weight=600)
    d.leader(120, 70, 120, 120)
    d.text("Loop", 120, 62, size=16, weight=600)
    d.arrow(250, 250, 450, 250, width=3)
    d.arrow(450, 250, 250, 250, width=3)
    d.text("Tension", 350, 284, size=16, weight=600)


@design("SHL/ventilation-in-shelters-2")
def _(d):
    d.piece("room", 150, 50, 340)
    d.curve_arrow("M 285 255 C 285 190, 320 170, 320 112", (320, 112), -1.5708, color=BLUE)
    d.text("Upper opening", 470, 40, size=16, weight=600)
    d.leader(400, 46, 335, 78)
    d.text("Lower opening", 170, 335, size=16, weight=600)
    d.leader(240, 322, 285, 282)


@design("SHL/winter-insulation-1")
def _(d):
    d.piece("house", 190, 70, 260)
    d.arrow(320, 36, 320, 80, width=6)
    d.text("Roof", 345, 62, size=17, weight=600, anchor="start")
    d.arrow(120, 200, 240, 200, width=3)
    d.text("Walls", 110, 206, size=16, weight=600, anchor="end")
    d.arrow(520, 224, 396, 224, width=3)
    d.text("Doors", 530, 230, size=16, weight=600, anchor="start")
    d.arrow(520, 190, 396, 190, width=3)
    d.text("Windows", 530, 196, size=16, weight=600, anchor="start")
    caption(d, "Heat escapes fastest through the roof.")