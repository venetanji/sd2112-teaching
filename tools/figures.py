"""
Drawn figures for the decks. Each function returns (svg_markup, png_path).
The same geometry is drawn twice — as SVG (html deck) and with PIL (pptx / preview) —
so both outputs carry the identical illustration.
"""
from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'deck' / 'assets' / 'generated'
INK, ORANGE, MUTED, LINE, TEAL, VIOLET = '#000B1C', '#ED6D24', '#5C6470', '#E1E1DE', '#64C2C3', '#943890'


class Canvas:
    """Tiny dual backend: collects SVG and draws PIL at the same time."""

    def __init__(self, w, h, bg=None, scale=2):
        self.w, self.h, self.scale = w, h, scale
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">']
        self.im = Image.new('RGBA', (w * scale, h * scale), (0, 0, 0, 0) if bg is None else bg)
        self.d = ImageDraw.Draw(self.im)
        if bg:
            self.svg.append(f'<rect width="{w}" height="{h}" fill="{bg}"/>')

    def s(self, v):
        return v * self.scale

    def line(self, x1, y1, x2, y2, color=INK, width=3, cap='round'):
        self.svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}" stroke-linecap="{cap}"/>')
        self.d.line([self.s(x1), self.s(y1), self.s(x2), self.s(y2)], fill=color, width=max(1, round(self.s(width))))
        if cap == 'round':
            r = self.s(width) / 2
            for (x, y) in ((x1, y1), (x2, y2)):
                self.d.ellipse([self.s(x) - r, self.s(y) - r, self.s(x) + r, self.s(y) + r], fill=color)

    def poly(self, pts, fill=None, stroke=None, width=3):
        p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        self.svg.append(f'<polygon points="{p}" fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{width}" stroke-linejoin="round"/>')
        spts = [(self.s(x), self.s(y)) for x, y in pts]
        self.d.polygon(spts, fill=fill, outline=stroke, width=max(1, round(self.s(width))) if stroke else 0)

    def rect(self, x, y, w, h, fill=None, stroke=None, width=3):
        self.poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], fill, stroke, width)

    def circle(self, cx, cy, r, fill=None, stroke=None, width=3):
        self.svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{width}"/>')
        self.d.ellipse([self.s(cx - r), self.s(cy - r), self.s(cx + r), self.s(cy + r)], fill=fill, outline=stroke, width=max(1, round(self.s(width))) if stroke else 0)

    def text(self, x, y, t, size=20, color=MUTED, mono=True, anchor='start', weight=500):
        fam = "'JetBrains Mono',Menlo,Consolas,monospace" if mono else "'Inter',Helvetica,Arial,sans-serif"
        ta = {'start': 'start', 'middle': 'middle', 'end': 'end'}[anchor]
        self.svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{ta}">{t}</text>')
        from deckgen import pil_font
        f = pil_font('monomed' if mono else 'semibold', round(self.s(size)))
        tw = f.getlength(t)
        ax = {'start': 0, 'middle': tw / 2, 'end': tw}[anchor]
        asc, desc = f.getmetrics()
        self.d.text((self.s(x) - ax, self.s(y) - asc), t, font=f, fill=color)

    def finish(self, name):
        self.svg.append('</svg>')
        OUT.mkdir(parents=True, exist_ok=True)
        p = OUT / f'{name}.png'
        self.im.save(p)
        return '\n'.join(self.svg), str(p)


# ───────────────────────── a chair from rules ─────────────────────────
def draw_chair(c, ox, oy, size, seat_h=0.5, back_h=0.5, back_angle=8, seat_w=0.6, legs=4, leg_splay=0.0, stroke=INK, width=4):
    """Side-elevation chair from parameters. All ratios of `size`. Origin = bottom-left of the drawing box."""
    sh = seat_h * size
    sw = seat_w * size
    thick = 0.05 * size
    x0 = ox + (size - sw) / 2          # seat left
    y_seat = oy + size - sh            # seat top
    # seat
    c.rect(x0, y_seat, sw, thick, fill=stroke)
    # legs
    n = max(2, legs)
    xs = [x0 + thick / 2, x0 + sw - thick / 2] if n == 2 else [x0 + thick / 2 + i * (sw - thick) / (n - 1) for i in range(n)]
    for i, lx in enumerate(xs):
        splay = leg_splay * size * (-1 if lx < x0 + sw / 2 else 1)
        c.line(lx, y_seat + thick, lx + splay, oy + size, stroke, width)
    # back, hinged at the rear edge of the seat
    bh = back_h * size
    ang = math.radians(back_angle)
    bx0 = x0 + sw - thick / 2
    tip = (bx0 + math.sin(ang) * bh, y_seat - math.cos(ang) * bh)
    c.line(bx0, y_seat, tip[0], tip[1], stroke, width + 1)
    # top rail
    c.line(tip[0] - 0.22 * sw * math.cos(ang) , tip[1] - 0.22 * sw * math.sin(ang), tip[0], tip[1], stroke, width)


def parametric_chairs(name='chairs-rules', cols=4, rows=3, w=800, h=720, seed=2112):
    """A grid of chairs, every one produced by the same rule with different numbers."""
    rnd = random.Random(seed)
    c = Canvas(w, h)
    cw, ch = w / cols, h / rows
    size = min(cw, ch) * 0.62
    for r in range(rows):
        for k in range(cols):
            params = dict(seat_h=rnd.uniform(0.32, 0.6), back_h=rnd.uniform(0.3, 0.75), back_angle=rnd.uniform(-2, 22),
                          seat_w=rnd.uniform(0.45, 0.8), legs=rnd.choice([2, 3, 4, 4, 4]), leg_splay=rnd.uniform(0, 0.12))
            ox = k * cw + (cw - size) / 2
            oy = r * ch + (ch - size) / 2 - 6
            draw_chair(c, ox, oy, size, **params)
            label = f'{params["seat_h"]:.2f} · {max(0, params["back_angle"]):.0f}° · {params["legs"]}'
            c.text(ox + size / 2, r * ch + ch - 10, label, size=14, anchor='middle')
    return c.finish(name)


def one_chair(name='chair-one', w=400, h=400, **params):
    c = Canvas(w, h)
    draw_chair(c, 40, 30, w - 80, **params)
    return c.finish(name)


# ───────────────────────── a chair from examples: the prototype ─────────────────────────
def typicality_scale(name='typicality', w=1680, h=300):
    """A horizontal scale from the typical chair to the edge of the concept."""
    c = Canvas(w, h)
    items = [('dining chair', 1.0), ('armchair', 0.9), ('stool', 0.7), ('bean bag', 0.5), ('swing', 0.35), ('tree stump', 0.2), ('rock', 0.08)]
    n = len(items)
    c.line(80, 200, w - 80, 200, LINE, 4)
    for i, (label, typ) in enumerate(items):
        x = 80 + i * (w - 160) / (n - 1)
        r = 10 + 26 * typ
        c.circle(x, 200, r, fill=ORANGE if typ > 0.6 else (TEAL if typ > 0.3 else MUTED))
        c.text(x, 265, label, size=20, anchor='middle', color=INK)
        c.text(x, 150, f'{typ:.2f}', size=16, anchor='middle')
    c.text(80, 60, 'TYPICAL', size=18, anchor='start', color=ORANGE)
    c.text(w - 80, 60, 'IS IT STILL A CHAIR?', size=18, anchor='end', color=MUTED)
    return c.finish(name)


# ───────────────────────── perceptron ─────────────────────────
def perceptron(name='perceptron', w=800, h=560):
    c = Canvas(w, h)
    ins = [(140, 120 + i * 106) for i in range(4)]
    hid = [(400, 173 + i * 106) for i in range(3)]
    out = (660, 280)
    for x1, y1 in ins:
        for x2, y2 in hid:
            c.line(x1, y1, x2, y2, LINE, 3)
    for x2, y2 in hid:
        c.line(x2, y2, out[0], out[1], LINE, 3)
    for x, y in ins:
        c.circle(x, y, 28, fill=TEAL)
    for x, y in hid:
        c.circle(x, y, 28, fill=VIOLET)
    c.circle(out[0], out[1], 34, fill=ORANGE)
    c.text(140, 60, 'EXAMPLES IN', size=16, anchor='middle')
    c.text(400, 60, 'WEIGHTS', size=16, anchor='middle')
    c.text(660, 60, 'GUESS OUT', size=16, anchor='middle')
    c.text(400, 530, 'wrong guess → nudge every weight a little → again, a million times', size=16, anchor='middle', color=INK)
    return c.finish(name)


# ───────────────────────── two machines ─────────────────────────
def two_machines(name='two-machines', w=1680, h=520):
    c = Canvas(w, h)
    # left: rules
    c.rect(0, 0, 800, 520, fill='#F4F4F2')
    c.text(40, 60, 'MACHINE A · RULES', size=20, color=ORANGE)
    c.text(40, 130, 'if seat and back and legs >= 3:', size=26, color=INK)
    c.text(40, 172, '    return "chair"', size=26, color=INK)
    c.text(40, 240, 'definition → verdict', size=20, color=MUTED)
    draw_chair(c, 520, 220, 220, seat_h=0.45, back_h=0.6, back_angle=8, seat_w=0.62, legs=4)
    c.text(40, 470, 'exact · explainable · brittle', size=20, color=MUTED)
    # right: examples
    c.rect(880, 0, 800, 520, fill='#000B1C')
    c.text(920, 60, 'MACHINE B · EXAMPLES', size=20, color=TEAL)
    rnd = random.Random(7)
    for i in range(12):
        col, row = i % 6, i // 6
        s = 84
        ox = 920 + col * 124
        oy = 110 + row * 130
        draw_chair(c, ox, oy, s, seat_h=rnd.uniform(0.38, 0.55), back_h=rnd.uniform(0.4, 0.7), back_angle=rnd.uniform(0, 16), seat_w=rnd.uniform(0.5, 0.75), legs=rnd.choice([2, 4, 4]), stroke='#D3E7E8', width=2)
    c.text(920, 420, '12 000 photos labelled "chair" → a feel for chair-ness', size=20, color='#D3E7E8')
    c.text(920, 470, 'fuzzy · fluent · cannot say why', size=20, color='#B3B7BE')
    return c.finish(name)


# ───────────────────────── mediation: I – technology – world ─────────────────────────
def mediation(name='mediation', w=1680, h=260):
    c = Canvas(w, h)
    y = 130
    c.circle(240, y, 70, fill=TEAL); c.text(240, y + 9, 'YOU', size=22, anchor='middle', color=INK)
    c.rect(720, y - 70, 240, 140, fill=ORANGE); c.text(840, y + 9, 'TECHNOLOGY', size=22, anchor='middle', color=INK)
    c.circle(1440, y, 70, fill=VIOLET); c.text(1440, y + 9, 'WORLD', size=22, anchor='middle', color='#FFFFFF')
    c.line(320, y, 700, y, INK, 5); c.line(980, y, 1360, y, INK, 5)
    c.text(510, y - 30, 'perceives through', size=18, anchor='middle')
    c.text(1170, y - 30, 'acts on', size=18, anchor='middle')
    c.text(840, 240, 'the thing in between changes what you see and what you do', size=20, anchor='middle', color=INK)
    return c.finish(name)


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(ROOT / 'tools'))
    for fn in (parametric_chairs, typicality_scale, perceptron, two_machines, mediation):
        svg, png = fn()
        print(png, len(svg))
