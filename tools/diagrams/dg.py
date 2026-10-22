import math

from elements import index_elements, element_body, scope_ids

INK = "#2b2620"
SAND = "#b9ab8f"
CREAM = "#faf7f0"
PAPER = "#f5f1e8"
YELLOW = "#f6b84b"
RED = "#c4432f"
GREEN = "#5f8436"
BLUE = "#3f7fb0"
GREY = "#b3bec4"
ELEMENTS = index_elements()
FONT = "Source Sans 3, Helvetica, Arial, sans-serif"


class D:
    def __init__(self, key):
        self.key = key
        self.parts = []
        self.n = 0

    def piece(self, name, x, y, w, h=None):
        h = h if h is not None else w * 0.75
        body = scope_ids(element_body(ELEMENTS[name]), f"{self.key.replace('/', '-')}-{self.n}-")
        self.n += 1
        self.parts.append(f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="0 0 160 120">{body}</svg>')

    def text(self, s, x, y, size=16, weight=400, anchor="middle", fill=INK):
        lines = s.split("\n")
        if len(lines) == 1:
            self.parts.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}">{s}</text>'
            )
            return
        spans = "".join(
            f'<tspan x="{x:.1f}" dy="{0 if i == 0 else size * 1.2:.1f}">{ln}</tspan>' for i, ln in enumerate(lines)
        )
        self.parts.append(
            f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}">{spans}</text>'
        )

    def line(self, x1, y1, x2, y2, dash=None, width=3, color=INK):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{d}/>'
        )

    def arrow(self, x1, y1, x2, y2, color=INK, width=4, dash=None):
        ang = math.atan2(y2 - y1, x2 - x1)
        hx, hy = x2 - 12 * math.cos(ang), y2 - 12 * math.sin(ang)
        self.line(x1, y1, hx, hy, dash=dash, width=width, color=color)
        px, py = -math.sin(ang), math.cos(ang)
        pts = f"{x2:.1f},{y2:.1f} {hx + 8 * px:.1f},{hy + 8 * py:.1f} {hx - 8 * px:.1f},{hy - 8 * py:.1f}"
        self.parts.append(f'<polygon points="{pts}" fill="{color}"/>')

    def path(self, d, fill="none", stroke=INK, width=3, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{da}/>'
        )

    def curve_arrow(self, d, end, ang, color=INK, width=4):
        self.path(d, stroke=color, width=width)
        ex, ey = end
        px, py = -math.sin(ang), math.cos(ang)
        bx, by = ex - 12 * math.cos(ang), ey - 12 * math.sin(ang)
        pts = f"{ex:.1f},{ey:.1f} {bx + 8 * px:.1f},{by + 8 * py:.1f} {bx - 8 * px:.1f},{by - 8 * py:.1f}"
        self.parts.append(f'<polygon points="{pts}" fill="{color}"/>')

    def rect(self, x, y, w, h, fill=CREAM, stroke=INK, width=3, rx=10, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"{da}/>'
        )

    def circle(self, cx, cy, r, fill=CREAM, stroke=INK, width=3):
        self.parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')

    def ellipse(self, cx, cy, rx, ry, fill=CREAM, stroke=INK, width=3):
        self.parts.append(
            f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
        )

    def badge(self, n, cx, cy, r=20):
        self.circle(cx, cy, r, fill=INK, stroke=INK)
        self.text(str(n), cx, cy + r * 0.36, size=r * 1.1, weight=800, fill="#ffffff")

    def tick(self, cx, cy, r=14):
        self.circle(cx, cy, r, fill=GREEN, stroke=INK, width=2.5)
        self.path(f"M{cx - r * 0.45:.1f} {cy:.1f}L{cx - r * 0.1:.1f} {cy + r * 0.35:.1f}L{cx + r * 0.5:.1f} {cy - r * 0.4:.1f}", stroke="#ffffff", width=3.5)

    def cross(self, cx, cy, r=14):
        self.circle(cx, cy, r, fill=RED, stroke=INK, width=2.5)
        s = r * 0.4
        self.path(f"M{cx - s:.1f} {cy - s:.1f}L{cx + s:.1f} {cy + s:.1f}M{cx + s:.1f} {cy - s:.1f}L{cx - s:.1f} {cy + s:.1f}", stroke="#ffffff", width=3.5)

    def leader(self, x1, y1, x2, y2):
        self.line(x1, y1, x2, y2, width=2)
        self.circle(x2, y2, 4, fill="#ffffff", stroke=INK, width=2)

    def body(self):
        return "\n".join(self.parts)

    def svg(self):
        return (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360">'
            f'<rect width="640" height="360" fill="{PAPER}"/>\n{self.body()}\n</svg>'
        )
