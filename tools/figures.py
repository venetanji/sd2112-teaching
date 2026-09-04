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


# ═════════════════════════ week 2 · rules that make things ═════════════════════════
# Every figure here is a rule executed by this script. The p5.js code on the slides is
# the same rule for a different executor; the pictures differ only by the random numbers.

def _arrow(c, x1, y1, x2, y2, color=INK, width=4, head=14):
    c.line(x1, y1, x2, y2, color, width, cap='butt')
    ang = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(ang - 0.5), y2 - head * math.sin(ang - 0.5))
    p2 = (x2 - head * math.cos(ang + 0.5), y2 - head * math.sin(ang + 0.5))
    c.poly([(x2, y2), p1, p2], fill=color)


# ───────────────────────── machine A: if this, then that ─────────────────────────
def decision_tree(name='if-then', w=1680, h=520):
    """Is it a chair? Three rules in a row: exact, explainable, and wrong about the Tulip chair."""
    c = Canvas(w, h)
    y, bh, bw, step = 130, 120, 340, 460
    steps = [('has a seat?', 'not a seat'), ('has a back?', 'a stool'), ('three legs or more?', 'not a chair')]
    for i, (q, no) in enumerate(steps):
        x = 60 + i * step
        c.rect(x, y, bw, bh, fill='#F4F4F2', stroke=INK, width=3)
        c.text(x + bw / 2, y + bh / 2 + 8, q.upper(), size=22, anchor='middle', color=INK)
        nx = x + step if i < 2 else 1420
        _arrow(c, x + bw, y + bh / 2, nx - 4, y + bh / 2, INK, 4)
        c.text(x + bw + (nx - x - bw) / 2, y + bh / 2 - 16, 'yes', size=18, anchor='middle', color=ORANGE)
        _arrow(c, x + bw / 2, y + bh, x + bw / 2, y + bh + 110, INK, 4)
        c.text(x + bw / 2 + 24, y + bh + 66, 'no', size=18, anchor='start', color=ORANGE)
        c.text(x + bw / 2, y + bh + 156, no, size=22, anchor='middle', color=INK)
    c.rect(1420, y, 220, bh, fill=ORANGE)
    c.text(1530, y + bh / 2 + 9, 'CHAIR', size=26, anchor='middle', color=INK)
    c.text(60, 60, 'IF THIS, THEN THAT', size=18, anchor='start', color=ORANGE)
    c.text(w - 40, 60, 'Saarinen’s Tulip chair has one leg. The rule has no idea.', size=18, anchor='end', color=MUTED)
    c.text(1530, y + bh + 156, 'by definition', size=18, anchor='middle', color=MUTED)
    return c.finish(name)


# ───────────────────────── LeWitt: points at random, all connected ─────────────────────────
def _lewitt_pts(n, x0, y0, w, h, even, rnd, margin=24):
    """n points in a box. even=True: one point per cell of a grid, at random inside it (what LeWitt meant).
    even=False: plain uniform random (what the words say)."""
    pts = []
    if even:
        cols = max(1, round(math.sqrt(n * w / h)))
        rows = math.ceil(n / cols)
        cells = [(r, k) for r in range(rows) for k in range(cols)]
        rnd.shuffle(cells)
        cw, ch = (w - 2 * margin) / cols, (h - 2 * margin) / rows
        for r, k in sorted(cells[:n]):
            pts.append((x0 + margin + (k + rnd.uniform(0.12, 0.88)) * cw, y0 + margin + (r + rnd.uniform(0.12, 0.88)) * ch))
    else:
        for _ in range(n):
            pts.append((x0 + margin + rnd.random() * (w - 2 * margin), y0 + margin + rnd.random() * (h - 2 * margin)))
    return pts


def _lewitt_draw(c, pts, color=INK, width=1, dots=True, wobble=0.0, rnd=None):
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            (x1, y1), (x2, y2) = pts[i], pts[j]
            if wobble and rnd:
                mx, my = (x1 + x2) / 2 + rnd.uniform(-wobble, wobble), (y1 + y2) / 2 + rnd.uniform(-wobble, wobble)
                c.line(x1, y1, mx, my, color, width, cap='butt'); c.line(mx, my, x2, y2, color, width, cap='butt')
            else:
                c.line(x1, y1, x2, y2, color, width, cap='butt')
    if dots:
        for x, y in pts:
            c.circle(x, y, 4, fill=INK)


def lewitt_118(name='lewitt-118', w=1680, h=560, seed=118):
    """Wall Drawing 118, executed on a wall-shaped canvas: fifty points, 1,225 lines."""
    c = Canvas(w, h)
    c.rect(1, 1, w - 2, h - 2, fill='#FFFFFF', stroke=LINE, width=2)
    _lewitt_draw(c, _lewitt_pts(50, 0, 0, w, h, True, random.Random(seed), margin=40), color='#3B4451', width=1)
    return c.finish(name)


def lewitt_wall(name='lewitt-118-wall', w=800, h=500, seed=118):
    """The same rule on the 800 x 500 canvas of the p5.js code on the slide."""
    c = Canvas(w, h)
    c.rect(1, 1, w - 2, h - 2, fill='#FFFFFF', stroke=LINE, width=2)
    _lewitt_draw(c, _lewitt_pts(50, 0, 0, w, h, True, random.Random(seed), margin=24), color='#3B4451', width=1)
    return c.finish(name)


def lewitt_ten(seed=7, name=None, w=600, h=600):
    """Ten points at random, all connected — the fifteen-line p5.js sketch."""
    c = Canvas(w, h)
    c.rect(1, 1, w - 2, h - 2, fill='#FFFFFF', stroke=LINE, width=2)
    _lewitt_draw(c, _lewitt_pts(10, 0, 0, w, h, False, random.Random(seed), margin=30), width=2)
    return c.finish(name or f'lewitt-ten-{seed}')


def lewitt_seeds(name='lewitt-seeds', w=1680, h=560):
    c = Canvas(w, h)
    pw = 500
    for i, seed in enumerate((1, 2, 3)):
        x = 40 + i * 550
        c.rect(x, 0, pw, pw, fill='#FFFFFF', stroke=LINE, width=2)
        _lewitt_draw(c, _lewitt_pts(10, x, 0, pw, pw, False, random.Random(seed), margin=24), width=2)
        c.text(x + pw / 2, 546, f'randomSeed({seed})', size=20, anchor='middle', color=INK)
    return c.finish(name)


def lewitt_random_vs_even(name='lewitt-said-meant', w=1680, h=560):
    c = Canvas(w, h)
    panels = ((False, '"at random": fifty calls to random()'), (True, '"evenly distributed": one point per cell of a grid, at random inside it'))
    for i, (even, label) in enumerate(panels):
        x = i * 880
        c.rect(x + 1, 1, 798, 498, fill='#FFFFFF', stroke=LINE, width=2)
        _lewitt_draw(c, _lewitt_pts(50, x, 0, 800, 500, even, random.Random(118 + i), margin=30), color='#3B4451', width=1)
        c.text(x + 400, 546, label, size=19, anchor='middle', color=INK)
    return c.finish(name)


# ───────────────────────── Nees: Schotter ─────────────────────────
def _schotter_draw(c, x0, y0, cols, rows, s, disorder, rnd, width=2):
    for r in range(rows):
        k = r / (rows - 1)
        d, a = k * s / 2 * disorder, k * math.pi / 4 * disorder
        for col in range(cols):
            cx = x0 + s * (col + 0.5) + rnd.uniform(-d, d)
            cy = y0 + s * (r + 0.5) + rnd.uniform(-d, d)
            ang = rnd.uniform(-a, a)
            pts = []
            for dx, dy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
                px, py = dx * s / 2, dy * s / 2
                pts.append((cx + px * math.cos(ang) - py * math.sin(ang), cy + px * math.sin(ang) + py * math.cos(ang)))
            c.poly(pts, stroke=INK, width=width)


def schotter(name='schotter', cols=12, rows=22, s=30, disorder=1.0, seed=1968, margin=20):
    """After Georg Nees, c. 1968: 12 x 22 squares; shift and turn grow with the row. Same canvas as the p5.js code."""
    w, h = cols * s + 2 * margin, rows * s + 2 * margin
    c = Canvas(w, h)
    c.rect(1, 1, w - 2, h - 2, fill='#FFFFFF', stroke=LINE, width=2)
    _schotter_draw(c, margin, margin, cols, rows, s, disorder, random.Random(seed))
    return c.finish(name)


def schotter_variations(name='schotter-variations', w=1680, h=640):
    """The same rule three times: Nees's numbers, the disorder tripled, eight rows."""
    c = Canvas(w, h)
    s = 24
    specs = [(22, 1.0, 'rows = 22 · disorder = 1 · Nees'), (22, 3.0, 'disorder = 3'), (8, 1.0, 'rows = 8')]
    pw, tall = 12 * s, 22 * s
    for (rows, dis, label), x in zip(specs, (200, 696, 1192)):
        y0 = 12 + (tall - rows * s) / 2
        _schotter_draw(c, x, y0, 12, rows, s, dis, random.Random(1968), width=2)
        c.text(x + pw / 2, 600, label, size=20, anchor='middle', color=INK)
    return c.finish(name)


# ───────────────────────── Nake: Walk-Through-Raster ─────────────────────────
# Nake, 1966: a repertoire of signs; a chain of signs, each chosen from the previous one by a
# probability table (a Markov chain); the chain mapped into the raster cell by cell from the top left.
# Our repertoire (five signs) and our table are ours; the procedure is his.
WALK_DRIFT = [1, 3, 3, 4, 2]            # each sign's neighbour in the repertoire


def _walk_next(last, rnd):
    p = rnd.random()
    if p < 0.6:
        return last                     # stay
    if p < 0.85:
        return WALK_DRIFT[last]         # drift
    return rnd.randrange(5)             # jump


def _walk_sign(c, k, x, y, s=28, color=INK, width=2):
    if k in (1, 3):
        c.line(x + s * 0.15, y + s / 2, x + s * 0.85, y + s / 2, color, width, cap='butt')
    if k in (2, 3):
        c.line(x + s / 2, y + s * 0.15, x + s / 2, y + s * 0.85, color, width, cap='butt')
    if k == 4:
        c.rect(x + s * 0.28, y + s * 0.28, s * 0.44, s * 0.44, stroke=color, width=width)


def _walk_chain(length, seed):
    rnd, last, out = random.Random(seed), 0, []
    for _ in range(length):
        last = _walk_next(last, rnd)
        out.append(last)
    return out


def walk_through_raster(name='walk-through-raster', n=20, s=28, seed=1966, margin=20):
    w = n * s + 2 * margin
    c = Canvas(w, w)
    c.rect(1, 1, w - 2, w - 2, fill='#FFFFFF', stroke=LINE, width=2)
    for i, k in enumerate(_walk_chain(n * n, seed)):
        r, col = divmod(i, n)
        _walk_sign(c, k, margin + col * s, margin + r * s, s)
    return c.finish(name)


def walk_breakdown(name='walk-breakdown', w=1680, h=560):
    """Four steps: the raster, the repertoire, the chain, the mapping."""
    c = Canvas(w, h)
    xs = (0, 440, 880, 1320)
    g, s, y0 = 12, 28, 76
    for x, t in zip(xs, ('1 · THE RASTER', '2 · THE REPERTOIRE', '3 · THE CHAIN', '4 · THE MAPPING')):
        c.text(x, 34, t, size=18, anchor='start', color=ORANGE)

    def grid(x0):
        for i in range(g + 1):
            c.line(x0, y0 + i * s, x0 + g * s, y0 + i * s, LINE, 2, cap='butt')
            c.line(x0 + i * s, y0, x0 + i * s, y0 + g * s, LINE, 2, cap='butt')

    # 1 · the raster
    grid(xs[0] + 12)
    c.text(xs[0], 470, 'a grid of empty cells', size=18, anchor='start', color=INK)
    c.text(xs[0], 500, 'Nake’s: about 20 × 20', size=18, anchor='start', color=MUTED)
    # 2 · the repertoire
    for k in range(5):
        bx, by = xs[1] + 12 + k * 68, 104
        c.rect(bx, by, 56, 56, stroke=LINE, width=2)
        _walk_sign(c, k, bx, by, 56, width=3)
        c.text(bx + 28, 192, str(k), size=18, anchor='middle', color=MUTED)
    c.text(xs[1], 250, 'and a table of probabilities:', size=18, anchor='start', color=INK)
    c.text(xs[1], 284, 'stay 60% · drift 25% · jump 15%', size=18, anchor='start', color=INK)
    c.text(xs[1], 470, 'five signs, numbered 0 to 4', size=18, anchor='start', color=INK)
    c.text(xs[1], 500, 'ours; Nake’s were his own', size=18, anchor='start', color=MUTED)
    # 3 · the chain
    chain = _walk_chain(g * g, 1966)
    for i, k in enumerate(chain[:16]):
        r, col = divmod(i, 8)
        bx, by = xs[2] + 12 + col * 42, 104 + r * 58
        c.rect(bx, by, 36, 36, stroke=LINE, width=1)
        _walk_sign(c, k, bx, by, 36, width=2)
        if col < 7:
            c.text(bx + 39, by + 24, '›', size=16, anchor='middle', color=MUTED)
    c.text(xs[2], 250, 'sign i+1 = f(sign i, a random number)', size=18, anchor='start', color=INK)
    c.text(xs[2], 284, 'a Markov chain: stay, drift or jump', size=18, anchor='start', color=INK)
    c.text(xs[2], 470, 'a long chain: one sign per cell', size=18, anchor='start', color=INK)
    c.text(xs[2], 500, 'new dice, same table: new chain', size=18, anchor='start', color=MUTED)
    # 4 · the mapping
    x0 = xs[3] + 12
    grid(x0)
    for i, k in enumerate(chain[:30]):
        r, col = divmod(i, g)
        _walk_sign(c, k, x0 + col * s, y0 + r * s, s, width=2)
    _arrow(c, x0 + 6, y0 + g * s + 22, x0 + g * s - 6, y0 + g * s + 22, ORANGE, 3, 10)
    c.text(xs[3], 470, 'poured in cell by cell, top left first', size=18, anchor='start', color=INK)
    c.text(xs[3], 500, 'runs of a sign become fields', size=18, anchor='start', color=MUTED)
    return c.finish(name)


# ───────────────────────── 10 PRINT ─────────────────────────
def ten_print(name='ten-print', cols=40, rows=16, s=40, seed=1982):
    w, h = cols * s, rows * s
    c = Canvas(w, h)
    rnd = random.Random(seed)
    for r in range(rows):
        for col in range(cols):
            x, y = col * s, r * s
            if rnd.random() < 0.5:
                c.line(x, y, x + s, y + s, INK, 4, cap='butt')
            else:
                c.line(x + s, y, x, y + s, INK, 4, cap='butt')
    return c.finish(name)


# ───────────────────────── Lindenmayer: a rule applied to its own output ─────────────────────────
def lsystem_growth(name='lsystem', w=1680, h=560):
    c = Canvas(w, h)
    rule = {'F': 'F[+F]F[-F]F'}
    ang = math.radians(25.7)
    for n in range(1, 5):
        s = 'F'
        for _ in range(n):
            s = ''.join(rule.get(ch, ch) for ch in s)
        seg = 430 / (3 ** n)
        cx = 210 + (n - 1) * 420
        x, y, a = cx, 496, -math.pi / 2
        stack = []
        for ch in s:
            if ch == 'F':
                nx, ny = x + seg * math.cos(a), y + seg * math.sin(a)
                c.line(x, y, nx, ny, INK, max(1.2, 4.5 - n), cap='round')
                x, y = nx, ny
            elif ch == '+':
                a += ang
            elif ch == '-':
                a -= ang
            elif ch == '[':
                stack.append((x, y, a))
            elif ch == ']':
                x, y, a = stack.pop()
        c.text(cx, 546, f'n = {n} · {s.count("F")} lines', size=18, anchor='middle', color=INK)
    c.text(0, 30, 'F → F[+F]F[-F]F', size=22, anchor='start', color=ORANGE)
    c.text(w, 30, 'start with one F · turn 25.7° · rewrite n times', size=18, anchor='end', color=MUTED)
    return c.finish(name)


# ───────────────────────── a variable font: one letter, one number ─────────────────────────
def weight_ramp(name='weight-ramp', w=1680, h=300):
    from PIL import ImageFont
    c = Canvas(w, h)
    path = str(ROOT / 'tools' / 'fonts' / 'Inter-Variable.ttf')
    size = 150
    for i, wt in enumerate(range(100, 1000, 100)):
        x, y = 30 + i * 182 + 91, 196
        c.svg.append(f'<text x="{x}" y="{y}" font-family="\'Inter\',Helvetica,Arial,sans-serif" font-size="{size}" font-weight="{wt}" fill="{INK}" text-anchor="middle" letter-spacing="-0.04em">Aa</text>')
        f = ImageFont.truetype(path, round(c.s(size)))
        vals = []
        for ax in f.get_variation_axes():
            nm = ax['name'].decode() if isinstance(ax['name'], bytes) else str(ax['name'])
            vals.append(wt if 'eight' in nm or 'wght' in nm else ax['default'])
        f.set_variation_by_axes(vals)
        tw = f.getlength('Aa')
        asc, _d = f.getmetrics()
        c.d.text((c.s(x) - tw / 2, c.s(y) - asc), 'Aa', font=f, fill=INK)
        c.text(x, 262, f'wght {wt}', size=16, anchor='middle', color=MUTED)
    return c.finish(name)


# ───────────────────────── one spec, three executors ─────────────────────────
def spec_pipeline(name='spec-pipeline', w=1680, h=440):
    c = Canvas(w, h)
    c.rect(0, 30, 470, 380, fill='#F4F4F2')
    c.text(28, 74, 'THE SPEC', size=18, color=ORANGE)
    lines = ['On a sheet of paper, using a', 'pencil, place ten points at', 'random. The points should be', 'evenly distributed over the', 'area of the sheet. All of the', 'points should be connected', 'by straight lines.']
    for i, t in enumerate(lines):
        c.text(28, 122 + i * 36, t, size=23, color=INK, mono=False)
    rows = [('A DRAFTER', 'LeWitt’s crew, 1971 · pencil on a wall', 'never the same twice'),
            ('YOU', 'p5.js, fifteen lines, 2026', 'the same every run, with a seed'),
            ('A LANGUAGE MODEL', 'genai.polyu.edu.hk → code → p5.js', 'what you said, not what you meant')]
    for i, (who, how, verdict) in enumerate(rows):
        y = 40 + i * 130
        _arrow(c, 480, 220, 596, y + 42, INK, 3, 10)
        c.rect(600, y, 470, 84, stroke=INK, width=3)
        c.text(628, y + 36, who, size=20, color=INK)
        c.text(628, y + 66, how, size=16, color=MUTED)
        _arrow(c, 1080, y + 42, 1146, y + 42, INK, 3, 10)
        rnd = random.Random(21 + i)
        pts = _lewitt_pts(10, 1160, y - 8, 100, 100, i != 0, rnd, margin=8)
        c.rect(1160, y - 8, 100, 100, stroke=LINE, width=1)
        _lewitt_draw(c, pts, color='#5C6470' if i == 0 else INK, width=1, dots=False, wobble=2.5 if i == 0 else 0, rnd=rnd)
        c.text(1284, y + 48, verdict, size=18, color=INK)
    return c.finish(name)


# ───────────────────────── Molnár: (dés)ordres ─────────────────────────
def molnar_desordres(name='molnar', n=6, s=100, margin=20, seed=1976, p=0.06):
    """After Vera Molnár: nested squares in a grid; each corner nudged with a small probability."""
    w = n * s + 2 * margin
    c = Canvas(w, w)
    c.rect(1, 1, w - 2, w - 2, fill='#FFFFFF', stroke=LINE, width=2)
    rnd = random.Random(seed)
    for r in range(n):
        for col in range(n):
            cx, cy = margin + col * s + s / 2, margin + r * s + s / 2
            for k in range(1, 8):
                half = k * s / 16
                pts = [(cx - half, cy - half), (cx + half, cy - half), (cx + half, cy + half), (cx - half, cy + half)]
                pts = [(x + (rnd.uniform(-7, 7) if rnd.random() < p else 0), y + (rnd.uniform(-7, 7) if rnd.random() < p else 0)) for x, y in pts]
                c.poly(pts, stroke=INK, width=2)
    return c.finish(name)
