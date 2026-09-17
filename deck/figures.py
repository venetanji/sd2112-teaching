"""
Drawn figures for the SD2112 decks: the chairs, the typicality scale, the perceptron,
the two machines, the mediation diagram (week 1); the two machines with cups, if-then, LeWitt's
points, Schotter, Walk-Through-Raster, 10 PRINT, the Koch curve, the L-system, the spec pipeline,
the weight ramp (week 2); Wittgenstein's games, Rosch's fruit, one neuron, the XOR limit,
backpropagation, AlexNet's layers, the two theories and the two machines, conceptual blending,
serial and parallel (week 3).
Each returns (svg_markup, png_path). A figure that stands in for a live p5.js sketch draws
the same rule the sketch runs, so the PDF and the PowerPoint show the same picture.

The dual SVG/PIL Canvas they are built on is generic and ships with deckgen; these
drawings are not, so they live with the deck that uses them.

    uv run deck/figures.py       # redraw them all into deck/assets/generated/
"""
from __future__ import annotations

import math
import random

from deckgen.figures import Canvas, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

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


# ───────────────────────── a cup from rules, and cups from examples ─────────────────────────
def draw_cup(c, ox, oy, size, body_h=0.72, body_w=0.58, taper=0.12, handle=0.26, lip=True, stroke=INK, width=4):
    """Side-elevation cup from parameters, all ratios of `size`; origin = bottom-left of the drawing box.
    A body that narrows towards the foot, a lip line, a handle on the right."""
    h = body_h * size
    wt = body_w * size                       # width at the rim
    wb = wt * (1 - 2 * taper)                # width at the foot
    cx = ox + size * 0.4                     # the body sits left of centre to leave room for the handle
    top, bottom = oy + size - h, oy + size
    c.poly([(cx - wt / 2, top), (cx + wt / 2, top), (cx + wb / 2, bottom), (cx - wb / 2, bottom)], stroke=stroke, width=width)
    if lip:
        k = 0.12
        c.line(cx - wt / 2 + (wt - wb) / 2 * k, top + h * k, cx + wt / 2 - (wt - wb) / 2 * k, top + h * k, stroke, max(1.5, width - 2))
    # the handle: half an ellipse, hung between a third and two thirds of the way down
    y1, y2 = top + h * 0.3, top + h * 0.72
    hx = cx + wt / 2 - (wt - wb) / 2 * 0.3
    rx, ry = handle * size, (y2 - y1) / 2
    pts = [(hx + rx * math.sin(i / 12 * math.pi), (y1 + y2) / 2 - ry * math.cos(i / 12 * math.pi)) for i in range(13)]
    for (x1, y1_), (x2, y2_) in zip(pts, pts[1:]):
        c.line(x1, y1_, x2, y2_, stroke, width)


def two_machines_cups(name='two-machines-cups', w=1680, h=520):
    """Week 2's recap of the week-1 cups: the same two panels as two_machines, with cups."""
    c = Canvas(w, h)
    c.rect(0, 0, 800, 520, fill='#F4F4F2')
    c.text(40, 60, 'MACHINE A · RULES', size=20, color=ORANGE)
    c.text(40, 130, 'if hollow and a handle and holds a drink:', size=26, color=INK)
    c.text(40, 172, '    return "cup"', size=26, color=INK)
    c.text(40, 240, 'definition → verdict', size=20, color=MUTED)
    draw_cup(c, 520, 220, 220, body_h=0.7, body_w=0.58, taper=0.1, handle=0.26)
    c.text(40, 470, 'exact · explainable · brittle', size=20, color=MUTED)
    c.rect(880, 0, 800, 520, fill='#000B1C')
    c.text(920, 60, 'MACHINE B · EXAMPLES', size=20, color=TEAL)
    rnd = random.Random(2112)
    for i in range(12):
        col, row = i % 6, i // 6
        s = 84
        ox = 920 + col * 124
        oy = 110 + row * 130
        draw_cup(c, ox, oy, s, body_h=rnd.uniform(0.5, 0.85), body_w=rnd.uniform(0.45, 0.7), taper=rnd.uniform(0, 0.2),
                 handle=rnd.uniform(0.16, 0.3), lip=rnd.random() < 0.7, stroke='#D3E7E8', width=2)
    c.text(920, 420, '12 000 photos labelled "cup" → a feel for cup-ness', size=20, color='#D3E7E8')
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
def _lewitt_pts(n, x0, y0, w, h, even, rnd, margin=24, cols=None):
    """n points in a box. even=True: one point per cell of a grid, at random inside it (what LeWitt meant).
    even=False: plain uniform random (what the words say).
    cols: the grid's width in cells; the p5.js code on the slides uses 10 x 5 for its fifty points, so the
    stills that stand in for it pass 10 and every cell gets its point. Left out, a grid near the box's
    proportions is picked, and the cells over n are skipped at random."""
    pts = []
    if even:
        cols = cols or max(1, round(math.sqrt(n * w / h)))
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
    """Wall Drawing 118, executed on a wall-shaped canvas: fifty points, one per cell of a 10 x 5 grid, 1,225 lines."""
    c = Canvas(w, h)
    c.rect(1, 1, w - 2, h - 2, fill='#FFFFFF', stroke=LINE, width=2)
    _lewitt_draw(c, _lewitt_pts(50, 0, 0, w, h, True, random.Random(seed), margin=40, cols=10), color='#3B4451', width=1)
    return c.finish(name)


def lewitt_wall(name='lewitt-118-wall', w=800, h=500, seed=118):
    """The same rule on the 800 x 500 canvas of the p5.js code on the slide: its 10 x 5 grid, one point per cell."""
    c = Canvas(w, h)
    c.rect(1, 1, w - 2, h - 2, fill='#FFFFFF', stroke=LINE, width=2)
    _lewitt_draw(c, _lewitt_pts(50, 0, 0, w, h, True, random.Random(seed), margin=24, cols=10), color='#3B4451', width=1)
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
        _lewitt_draw(c, _lewitt_pts(50, x, 0, 800, 500, even, random.Random(118 + i), margin=30, cols=10), color='#3B4451', width=1)
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
def _walk_cells(n, cap_chance, seed):
    """The rule of Walk-Through-Raster as we execute it (after Nake, and after the 2025 pfad script):
    column by column, top to bottom. A cell is one of four things: empty, a bar |, a cap ¯, or both.
    A bar is likelier the nearer the cell is to the diagonal; a cap is drawn only under an empty cell,
    so never in the top row, which has nothing above it. Returns {(w, h): (bar, cap)}."""
    rnd = random.Random(seed)
    cells = {}
    for w in range(n):
        above = False
        for h in range(n):
            bar = rnd.uniform(0, n - 1) >= abs(w - h)
            cap = above and rnd.random() < cap_chance
            cells[(w, h)] = (bar, cap)
            above = not bar and not cap
    return cells


def _walk_draw(c, cells, n, x0, y0, g, width=1.6, tint=None):
    """Paint the cells of _walk_cells at (x0, y0), g px each; tint: a fill for the empty cells."""
    for (w, h), (bar, cap) in cells.items():
        x, y = x0 + w * g, y0 + h * g
        if tint and not bar and not cap:
            c.rect(x, y, g, g, fill=tint)
        if bar:
            c.line(x, y, x, y + g, INK, width, cap='butt')
        if cap:
            c.line(x, y, x + g, y, INK, width, cap='butt')


def walk_through_raster(name='walk-through-raster', n=30, size=600, cap_chance=0.8, seed=1966):
    c = Canvas(size, size)
    c.rect(1, 1, size - 2, size - 2, fill='#FFFFFF', stroke=LINE, width=2)
    g = size / (n + 2)
    _walk_draw(c, _walk_cells(n, cap_chance, seed), n, g, g, g)
    return c.finish(name)


def walk_breakdown(name='walk-breakdown', w=1680, h=560):
    """Four panels: the raster and the order of the walk, the four states of a cell, the rule (the cell
    above decides), and the flow of the empty space that the rule guarantees."""
    c = Canvas(w, h)
    xs = (0, 440, 880, 1320)
    g, s, y0 = 12, 28, 76
    for x, t in zip(xs, ('1 · THE RASTER', '2 · FOUR STATES', '3 · THE RULE', '4 · THE FLOW')):
        c.text(x, 34, t, size=18, anchor='start', color=ORANGE)

    def grid(x0, cells=g, size=s, y=y0):
        for i in range(cells + 1):
            c.line(x0, y + i * size, x0 + cells * size, y + i * size, LINE, 2, cap='butt')
            c.line(x0 + i * size, y, x0 + i * size, y + cells * size, LINE, 2, cap='butt')

    # 1 · the raster, and the order of the walk: down the first column, then the next
    x0 = xs[0] + 12
    grid(x0)
    _arrow(c, x0 + s / 2, y0 + 8, x0 + s / 2, y0 + g * s - 8, ORANGE, 3, 10)
    _arrow(c, x0 + s * 1.5, y0 + 8, x0 + s * 1.5, y0 + g * s - 8, ORANGE, 2, 8)
    _arrow(c, x0 + 6, y0 + g * s + 22, x0 + g * s - 6, y0 + g * s + 22, ORANGE, 3, 10)
    c.text(xs[0], 470, 'a grid of cells, 30 × 30', size=18, anchor='start', color=INK)
    c.text(xs[0], 500, 'drawn column by column, top to bottom', size=18, anchor='start', color=MUTED)
    # 2 · the four states of a cell
    for k, (bar, cap, label) in enumerate([(False, False, 'empty'), (True, False, 'a bar'), (False, True, 'a cap'), (True, True, 'both')]):
        bx, by, sz = xs[1] + 12 + k * 104, 104, 72
        c.rect(bx, by, sz, sz, fill='#E3F1F4' if not (bar or cap) else None, stroke=LINE, width=2)
        if bar:
            c.line(bx, by, bx, by + sz, INK, 5, cap='butt')
        if cap:
            c.line(bx, by, bx + sz, by, INK, 5, cap='butt')
        c.text(bx + sz / 2, 206, label, size=18, anchor='middle', color=INK)
    c.text(xs[1], 250, 'every cell is one of these four', size=18, anchor='start', color=INK)
    c.text(xs[1], 284, 'a bar | on its left, a cap ¯ on its top', size=18, anchor='start', color=INK)
    c.text(xs[1], 470, 'two yes/no decisions per cell', size=18, anchor='start', color=INK)
    c.text(xs[1], 500, 'Nake\'s were his own; these are ours', size=18, anchor='start', color=MUTED)
    # 3 · the rule: the cell above decides; a bar is likelier near the diagonal
    x3 = xs[2] + 12
    c.rect(x3, 104, 72, 72, fill='#E3F1F4', stroke=LINE, width=2)
    c.text(x3 + 84, 132, 'the cell above: empty', size=18, anchor='start', color=INK)
    c.rect(x3, 176, 72, 72, stroke=LINE, width=2)
    c.line(x3, 176, x3 + 72, 176, INK, 5, cap='butt')
    c.text(x3 + 84, 204, 'so this one may get a cap', size=18, anchor='start', color=INK)
    c.text(x3 + 84, 232, 'under a bar or a cap: never', size=18, anchor='start', color=MUTED)
    mini, ms = 7, 24
    my = 290
    grid(x3, mini, ms, my)
    for ww in range(mini):
        for hh in range(mini):
            if abs(ww - hh) <= 1 or (abs(ww - hh) == 2 and (ww + hh) % 2 == 0):
                c.line(x3 + ww * ms, my + hh * ms, x3 + ww * ms, my + (hh + 1) * ms, INK, 3, cap='butt')
    c.text(x3 + mini * ms + 16, my + 60, 'a bar: likelier', size=18, anchor='start', color=INK)
    c.text(x3 + mini * ms + 16, my + 88, 'near the diagonal', size=18, anchor='start', color=INK)
    c.text(xs[2], 500, 'one fact carried from cell to cell', size=18, anchor='start', color=MUTED)
    # 4 · the flow: a small raster executed by the rule, the empty cells tinted
    x4 = xs[3] + 12
    grid(x4)
    _walk_draw(c, _walk_cells(g, 0.8, 1966), g, x4, y0, s, width=3, tint='#E3F1F4')
    _arrow(c, x4 + 10, y0 + g * s - 10, x4 + g * s - 10, y0 + 10, ORANGE, 4, 14)
    c.text(xs[3], 470, 'empty space flows up and right', size=18, anchor='start', color=INK)
    c.text(xs[3], 500, 'so fields of caps have gaps', size=18, anchor='start', color=MUTED)
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


# ───────────────────────── ELIZA's 1966 transcript: the still of the live chat ─────────────────────────
def eliza_transcript(lines, name='eliza', w=600, h=600):
    """The conversation from Weizenbaum's paper, drawn like the chat in the html deck: ELIZA's lines
    (tagged {violet:...} in the deck) in violet capitals, the patient's after a prompt."""
    import re, textwrap
    c = Canvas(w, h, bg='#F4F4F2')
    y = 40
    for line in lines:
        m = re.fullmatch(r'\{violet:(.*)\}', line)
        eliza = bool(m)
        text = m.group(1) if m else '> ' + line
        for part in textwrap.wrap(text, 46, subsequent_indent='  ' if not eliza else ''):
            c.text(24, y, part, size=17, anchor='start', color=VIOLET if eliza else INK)
            y += 26
        y += 8
    return c.finish(name)


# ───────────────────────── the exercise's own canvas: what the pptx and the PDF show ─────────────────────────
def sketch_placeholder(name='your-sketch', w=600, h=600):
    """The still for the 'your sketch' slide: an empty canvas that says where the sketch runs."""
    c = Canvas(w, h)
    c.rect(1, 1, w - 2, h - 2, fill='#FFFFFF', stroke=LINE, width=2)
    c.line(0, 0, w, h, LINE, 2)
    c.text(w / 2, h / 2 - 12, 'your sketch runs here', size=22, anchor='middle', color=MUTED)
    c.text(w / 2, h / 2 + 24, 'in the html deck: paste, then Run', size=18, anchor='middle', color=MUTED)
    return c.finish(name)


# ───────────────────────── Koch, 1904: replace every line with four, again ─────────────────────────
def _koch(p, q, n):
    """The Koch rule applied n times to the segment p → q: the points of the curve."""
    if n == 0:
        return [p, q]
    (x1, y1), (x2, y2) = p, q
    dx, dy = (x2 - x1) / 3, (y2 - y1) / 3
    a, b = (x1 + dx, y1 + dy), (x1 + 2 * dx, y1 + 2 * dy)
    peak = (a[0] + dx * 0.5 + dy * 0.866, a[1] + dy * 0.5 - dx * 0.866)   # the middle third, turned 60° (up, on screen)
    pts = []
    for s, e in ((p, a), (a, peak), (peak, b), (b, q)):
        pts.extend(_koch(s, e, n - 1)[:-1])
    pts.append(q)
    return pts


def koch_generations(name='koch', w=1680, h=300):
    """Five generations of the Koch curve, side by side: the same rule, applied to its own output."""
    c = Canvas(w, h)
    gens = 5
    cw = w / gens
    for n in range(gens):
        x0, x1, y = n * cw + 24, (n + 1) * cw - 24, 190
        pts = _koch((x0, y), (x1, y), n)
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            c.line(ax, ay, bx, by, INK, max(1.2, 4 - n * 0.6), cap='round')
        c.text((x0 + x1) / 2, 240, f'n = {n} · {4 ** n} lines', size=18, anchor='middle', color=INK)
        c.text((x0 + x1) / 2, 270, f'length × {(4 / 3) ** n:.2f}', size=18, anchor='middle', color=MUTED)
    c.text(w, 30, 'Helge von Koch, 1904 · the same rule, applied to its own output', size=18, anchor='end', color=MUTED)
    return c.finish(name)


def koch_curve(name='koch-4', n=4, w=900, h=300):
    """One Koch curve, at generation n: the twin of the live sketch on the code slide."""
    c = Canvas(w, h)
    pts = _koch((40, 240), (w - 40, 240), n)
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        c.line(ax, ay, bx, by, INK, 1.6, cap='round')
    c.text(w - 40, 280, f'n = {n} · {4 ** n} lines · length × {(4 / 3) ** n:.2f}', size=16, anchor='end', color=MUTED)
    return c.finish(name)


# ───────────────────────── Turing's imitation game, 1950 ─────────────────────────
def imitation_game(name='imitation-game', w=800, h=520):
    """An interrogator, a wall, a machine and a person; only typed text crosses the wall."""
    c = Canvas(w, h)
    c.text(400, 26, 'WHICH ONE IS THE MACHINE?', size=16, anchor='middle', color=INK, weight=700)
    c.rect(40, 170, 250, 180, fill=None, stroke=INK, width=4)
    c.text(165, 252, 'C', size=64, color=INK, anchor='middle', weight=800, mono=False)
    c.text(165, 300, 'THE INTERROGATOR', size=15, anchor='middle', color=MUTED)
    c.line(400, 50, 400, 480, INK, 10)
    c.text(400, 506, 'A WALL · ONLY TYPED TEXT CROSSES IT', size=14, anchor='middle', color=MUTED)
    c.rect(510, 60, 250, 170, fill=None, stroke=ORANGE, width=4)
    c.text(635, 137, 'A', size=64, color=ORANGE, anchor='middle', weight=800, mono=False)
    c.text(635, 185, 'A MACHINE', size=15, anchor='middle', color=MUTED)
    c.rect(510, 290, 250, 170, fill=None, stroke=TEAL, width=4)
    c.text(635, 367, 'B', size=64, color=TEAL, anchor='middle', weight=800, mono=False)
    c.text(635, 415, 'A PERSON', size=15, anchor='middle', color=MUTED)
    _arrow(c, 300, 230, 500, 135, INK, 3)      # questions, typed
    _arrow(c, 300, 290, 500, 385, INK, 3)
    _arrow(c, 500, 165, 300, 250, MUTED, 3)    # answers, typed
    _arrow(c, 500, 355, 300, 270, MUTED, 3)
    return c.finish(name)


# ───────────────────────── a variable font: one letter, one number ─────────────────────────
def weight_ramp(name='weight-ramp', w=1680, h=300):
    from PIL import ImageFont
    c = Canvas(w, h)
    from deckgen.core import FONT_DIR
    path = str(FONT_DIR / 'Inter-Variable.ttf')     # Inter ships inside the deckgen package
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


# ═════════════════════════ week 3 · learning from examples ═════════════════════════
# Concepts as definitions and as prototypes; one neuron, the perceptron's limit, backpropagation,
# the layers of AlexNet; serial versus parallel; and concept blending, for the activity.

PAPER = '#F4F4F2'
TEAL_TINT = '#D3E7E8'
ORANGE_TINT = '#FBE2D3'
VIOLET_TINT = '#E9D9EA'


def _dashed(c, x1, y1, x2, y2, color=MUTED, width=2, dash=10, gap=8):
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    t = 0.0
    while t < length:
        e = min(t + dash, length)
        c.line(x1 + ux * t, y1 + uy * t, x1 + ux * e, y1 + uy * e, color, width, cap='butt')
        t = e + gap


def _triangle(c, x, y, r, fill=None, stroke=None, width=2):
    c.poly([(x, y - r), (x + r * 0.9, y + r * 0.7), (x - r * 0.9, y + r * 0.7)], fill=fill, stroke=stroke, width=width)


def _lines(c, x, y, lines, size=17, gap=25, color=INK, mono=True, anchor='start'):
    for k, t in enumerate(lines):
        c.text(x, y + k * gap, t, size=size, color=color, mono=mono, anchor=anchor)


# ───────────────────────── Wittgenstein: no feature runs through all the games ─────────────────────────
GAMES = [
    ('chess', ('board', 'winning', 'skill', 'players')),
    ('football', ('ball', 'winning', 'skill', 'players')),
    ('poker', ('cards', 'winning', 'luck', 'skill', 'players')),
    ('patience', ('cards', 'winning', 'luck', 'skill')),
    ('tennis', ('ball', 'winning', 'skill', 'players')),
    ('ring-a-ring-a-roses', ('players',)),
]
FEATURES = ['board', 'ball', 'cards', 'winning', 'luck', 'skill', 'players']


def family_resemblance(name='family-resemblance', w=1680, h=560):
    """Wittgenstein's games as a tick matrix in which no column is full. A definition needs a full column."""
    c = Canvas(w, h)
    x0, col_w, y0, row_h = 330, 144, 128, 62
    c.text(0, 40, 'WITTGENSTEIN, 1953, §66 · "CONSIDER FOR EXAMPLE THE PROCEEDINGS THAT WE CALL GAMES"', size=18, color=ORANGE)
    for j, f in enumerate(FEATURES):
        c.text(x0 + j * col_w + col_w / 2, 100, f, size=19, anchor='middle', color=INK)
    for i, (game, feats) in enumerate(GAMES):
        y = y0 + i * row_h
        c.line(0, y + row_h - 8, x0 + len(FEATURES) * col_w, y + row_h - 8, LINE, 2, cap='butt')
        c.text(0, y + 36, game, size=21, color=INK)
        for j, f in enumerate(FEATURES):
            cx = x0 + j * col_w + col_w / 2
            if f in feats:
                c.circle(cx, y + 28, 13, fill=ORANGE)
            else:
                c.circle(cx, y + 28, 5, fill=LINE)
    y = y0 + len(GAMES) * row_h + 14
    c.text(0, y + 28, 'in all of them?', size=19, color=MUTED)
    for j in range(len(FEATURES)):
        c.text(x0 + j * col_w + col_w / 2, y + 28, 'no', size=19, anchor='middle', color=MUTED)
    c.rect(1400, 128, 280, 300, fill=PAPER)
    _lines(c, 1424, 168, ['No column is full:', 'no feature runs', 'through every game.', ' ', 'A definition needs', 'a full column.', ' ', 'The resemblances', 'overlap and', 'criss-cross instead.'], size=18, gap=27, mono=False)
    return c.finish(name)


# ───────────────────────── Rosch, 1975: fruit, from the best example to the worst ─────────────────────────
# Rank order of Rosch's goodness-of-example ratings for fruit (1 = a very good example, 7 = a very poor one),
# a subset of her 51 items; the positions along the scale are approximate, the order is hers.
FRUIT = [('orange', 1.07), ('apple', 1.08), ('banana', 1.15), ('pear', 1.18), ('plum', 1.37), ('strawberry', 1.61),
         ('pineapple', 1.94), ('lemon', 2.16), ('honeydew', 2.74), ('date', 2.87), ('coconut', 3.19), ('tomato', 5.58), ('olive', 6.21)]


def fruit_typicality(name='fruit-typicality', w=800, h=720):
    c = Canvas(w, h)
    x0, x1 = 230, 760
    c.text(0, 30, 'ROSCH, 1975 · "HOW GOOD AN EXAMPLE OF A FRUIT IS THIS?"', size=15, color=ORANGE)
    c.text(x0, 66, '1 · a very good example', size=14, color=INK)
    c.text(x1, 66, '7 · a very poor one', size=14, color=MUTED, anchor='end')
    for k in range(1, 8):
        x = x0 + (k - 1) / 6 * (x1 - x0)
        c.line(x, 78, x, 690, LINE, 1, cap='butt')
        c.text(x, 706, str(k), size=13, anchor='middle', color=MUTED)
    row = 46
    for i, (fruit, r) in enumerate(FRUIT):
        y = 106 + i * row
        x = x0 + (r - 1) / 6 * (x1 - x0)
        col = ORANGE if r < 1.5 else TEAL if r < 3.5 else MUTED
        c.text(30, y + 6, f'{i + 1:2d}', size=15, color=MUTED)
        c.text(70, y + 6, fruit, size=19, color=INK, mono=False)
        c.line(x0, y, x, y, col, 6, cap='butt')
        c.circle(x, y, 9, fill=col)
    return c.finish(name)


# ───────────────────────── one neuron: a weighted vote ─────────────────────────
def neuron(name='neuron', w=1680, h=520):
    c = Canvas(w, h)
    x1, x2 = 1.1, 0.4
    w1, w2, b = 1.6, -0.8, -1.2
    s = x1 * w1 + x2 * w2 + b
    ins = [(230, 150, 'height ÷ width', x1), (230, 370, 'size', x2)]
    sx, sy = 820, 260
    ox, oy = 1300, 260
    c.text(0, 40, 'ONE NEURON · ROSENBLATT, 1958', size=18, color=ORANGE)
    for (px, py, label, val), wt in zip(ins, (w1, w2)):
        c.line(px + 40, py, sx - 62, sy, INK, 4)
        mx, my = (px + 40 + sx - 62) / 2, (py + sy) / 2
        c.rect(mx - 58, my - 24, 116, 48, fill=ORANGE)
        c.text(mx, my + 8, f'× {wt:+.1f}', size=20, anchor='middle', color=INK)
        c.circle(px, py, 40, fill=TEAL)
        c.text(px, py + 8, f'{val:.1f}', size=22, anchor='middle', color=INK)
        c.text(px - 60, py + 8, label, size=18, anchor='end', color=INK)
    c.text(230, 76, 'INPUTS · THE OBJECT', size=16, anchor='middle')
    c.circle(sx, sy, 62, fill=VIOLET)
    c.text(sx, sy + 9, 'Σ + b', size=24, anchor='middle', color='#FFFFFF')
    c.text(sx, sy + 110, f'b = {b:+.1f}', size=20, anchor='middle', color=INK)
    c.text(sx, sy + 140, f'{x1:.1f}×{w1:+.1f} + {x2:.1f}×{w2:+.1f} {b:+.1f} = {s:+.2f}', size=18, anchor='middle', color=MUTED)
    c.text(sx, 76, 'WEIGHTS · THE KNOWLEDGE', size=16, anchor='middle')
    _arrow(c, sx + 64, sy, ox - 66, oy, INK, 4)
    c.text((sx + ox) / 2, sy - 22, 'above 0?', size=18, anchor='middle', color=INK)
    c.circle(ox, oy, 62, fill=ORANGE)
    c.text(ox, oy + 9, '1', size=30, anchor='middle', color=INK)
    c.text(ox, 76, 'GUESS', size=16, anchor='middle')
    c.text(ox + 90, oy - 6, f'{s:+.2f} > 0', size=20, color=INK)
    c.text(ox + 90, oy + 26, 'so: "cup"', size=20, color=INK)
    c.text(0, 496, 'three numbers decide. learning = changing them when the guess is wrong', size=20, color=INK)
    return c.finish(name)


# ───────────────────────── one line cannot; two layers can ─────────────────────────
def _xor_points(seed=11, n=9):
    rnd = random.Random(seed)
    out = []
    for cx, cy, t in ((0.25, 0.25, 'A'), (0.75, 0.75, 'A'), (0.25, 0.75, 'B'), (0.75, 0.25, 'B')):
        for _ in range(n):
            out.append((cx + rnd.gauss(0, 0.07), cy + rnd.gauss(0, 0.07), t))
    return out


def _xor_panel(c, x0, y0, size, pts, lines=False):
    c.rect(x0, y0, size, size, fill='#FFFFFF', stroke=LINE, width=2)

    def sx(v):
        return x0 + v * size

    def sy(v):
        return y0 + (1 - v) * size

    if lines:
        band = [(0, 0.35), (0.65, 1), (1, 1), (1, 0.65), (0.35, 0), (0, 0)]
        c.poly([(sx(x), sy(y)) for x, y in band], fill=ORANGE_TINT)
        c.line(sx(0), sy(0.35), sx(0.65), sy(1), INK, 3)
        c.line(sx(0.35), sy(0), sx(1), sy(0.65), INK, 3)
    for x, y, t in pts:
        x, y = min(max(x, 0.03), 0.97), min(max(y, 0.03), 0.97)
        if t == 'A':
            c.circle(sx(x), sy(y), 7, fill=ORANGE)
        else:
            _triangle(c, sx(x), sy(y), 9, fill=TEAL)


def xor_limit(name='xor-limit', w=1680, h=560):
    c = Canvas(w, h)
    pts = _xor_points()
    size = 400
    _xor_panel(c, 0, 70, size, pts)
    _dashed(c, 0, 70 + size / 2, size, 70 + size / 2, MUTED, 3)
    _dashed(c, size / 2, 70, size / 2, 70 + size, MUTED, 3)
    _dashed(c, 0, 70 + size, size, 70, MUTED, 3)
    c.text(0, 40, '1969 · MINSKY & PAPERT · ONE LINE CANNOT', size=18, color=ORANGE)
    c.text(0, 520, 'A on one diagonal, B on the other: no line gets all of them right', size=17, color=INK)
    mx = 640
    c.text(mx, 40, '1986 · A HIDDEN LAYER, TRAINED BY BACKPROPAGATION', size=18, color=ORANGE)
    ins = [(mx + 40, 190), (mx + 40, 350)]
    hid = [(mx + 200, 190), (mx + 200, 350)]
    out = (mx + 360, 270)
    for a in ins:
        for bnode in hid:
            c.line(a[0], a[1], bnode[0], bnode[1], LINE, 4)
    for bnode in hid:
        c.line(bnode[0], bnode[1], out[0], out[1], LINE, 4)
    for x, y in ins:
        c.circle(x, y, 26, fill=TEAL)
    for x, y in hid:
        c.circle(x, y, 26, fill=VIOLET)
    c.circle(out[0], out[1], 30, fill=ORANGE)
    c.text(ins[0][0], 130, 'x, y', size=16, anchor='middle')
    c.text(hid[0][0], 130, 'two lines', size=16, anchor='middle')
    c.text(out[0], 130, 'A or B', size=16, anchor='middle')
    _lines(c, mx, 412, ['each hidden unit is one neuron, one line each;', 'the output unit votes on their two verdicts.', 'wrong guess: the error travels backwards', 'and every weight moves a little.'], size=17, gap=24)
    c.text(mx, 412 + 4 * 24, '(9 weights here; 60 million in AlexNet)', size=17, color=MUTED)
    _xor_panel(c, 1280, 70, size, pts, lines=True)
    c.text(1280, 40, 'TWO LINES · A IN THE BAND, B OUTSIDE', size=18, color=ORANGE)
    c.text(1280, 520, 'a rule nobody wrote: "A is in the band"', size=17, color=INK)
    return c.finish(name)


# ───────────────────────── backpropagation: the guess goes forward, the error comes back ─────────────────────────
def backprop(name='backprop', w=1680, h=560):
    c = Canvas(w, h)
    layers = [[(200, 150 + i * 110) for i in range(4)], [(560, 120 + i * 88) for i in range(5)], [(920, 205 + i * 110) for i in range(3)], [(1220, 260 + i * 110) for i in range(2)]]
    names = ['PIXELS IN', 'HIDDEN', 'HIDDEN', 'GUESS OUT']
    for a, b_ in zip(layers, layers[1:]):
        for x1, y1 in a:
            for x2, y2 in b_:
                c.line(x1, y1, x2, y2, LINE, 2)
    fills = [TEAL, VIOLET, VIOLET, ORANGE]
    for layer, fill, label in zip(layers, fills, names):
        for x, y in layer:
            c.circle(x, y, 22, fill=fill)
        c.text(layer[0][0], 82, label, size=15, anchor='middle')
    c.text(1300, 266, 'chair  0.35', size=20, color=INK)
    c.text(1300, 376, 'cup    0.65', size=20, color=INK)
    c.rect(1420, 230, 260, 190, fill=PAPER)
    _lines(c, 1440, 266, ['THE TRUTH: a chair', ' ', 'chair should be 1.00', 'it said 0.35', ' ', 'error: 0.65'], size=16, gap=26)
    _arrow(c, 160, 520, 1250, 520, INK, 4)
    c.text(700, 552, 'FORWARD · every unit sums its inputs and passes a number on · the guess comes out at the end', size=16, anchor='middle', color=INK)
    _arrow(c, 1250, 40, 160, 40, ORANGE, 4)
    c.text(700, 26, 'BACKWARD · the error is shared out along the same connections · every weight moves a little, in proportion to its share', size=16, anchor='middle', color=ORANGE)
    return c.finish(name)


# ───────────────────────── deep: the features are learned too, layer by layer ─────────────────────────
def alexnet_layers(name='alexnet-layers', w=1680, h=560):
    c = Canvas(w, h)
    rnd = random.Random(2012)
    stages = ['PIXELS', 'EDGES', 'PARTS', 'OBJECTS', 'A LABEL']
    xs = [0, 340, 680, 1020, 1360]
    bw, by, bh = 300, 90, 300
    for x, t in zip(xs, stages):
        c.text(x, 50, t, size=18, color=ORANGE)
        c.rect(x, by, bw, bh, fill='#FFFFFF', stroke=LINE, width=2)
    for i in range(len(xs) - 1):
        _arrow(c, xs[i] + bw + 6, by + bh / 2, xs[i + 1] - 8, by + bh / 2, INK, 3, 10)
    n, cell = 10, 26
    gx, gy = xs[0] + (bw - n * cell) / 2, by + (bh - n * cell) / 2
    for r in range(n):
        for k in range(n):
            g = rnd.randint(150, 235)
            c.rect(gx + k * cell, gy + r * cell, cell - 2, cell - 2, fill=f'#{g:02x}{g:02x}{g:02x}')
    for r in range(3):
        for k in range(4):
            cx, cy = xs[1] + 45 + k * 70, by + 55 + r * 95
            a = rnd.choice((0, math.pi / 4, math.pi / 2, 3 * math.pi / 4))
            dx, dy = 22 * math.cos(a), 22 * math.sin(a)
            c.line(cx - dx, cy - dy, cx + dx, cy + dy, INK, 5)
    px = xs[2]
    c.line(px + 50, by + 60, px + 50, by + 240, INK, 6)
    c.line(px + 40, by + 250, px + 60, by + 250, INK, 5)
    c.rect(px + 100, by + 130, 120, 14, fill=INK)
    c.line(px + 250, by + 240, px + 268, by + 60, INK, 7)
    c.line(px + 238, by + 68, px + 268, by + 60, INK, 5)
    c.text(px + 50, by + 280, 'leg', size=15, anchor='middle')
    c.text(px + 160, by + 280, 'seat', size=15, anchor='middle')
    c.text(px + 258, by + 280, 'back', size=15, anchor='middle')
    draw_chair(c, xs[3] + 50, by + 40, 200, seat_h=0.45, back_h=0.6, back_angle=8, seat_w=0.62, legs=4, width=5)
    lx = xs[4]
    for k, (lab, p) in enumerate((('chair', 0.93), ('stool', 0.05), ('table', 0.02))):
        y = by + 70 + k * 80
        c.text(lx + 24, y + 6, lab, size=20, color=INK)
        c.rect(lx + 110, y - 14, 120, 28, fill=PAPER)
        c.rect(lx + 110, y - 14, 120 * p, 28, fill=ORANGE if k == 0 else TEAL)
        c.text(lx + 280, y + 6, f'{p:.2f}', size=16, anchor='end', color=MUTED)
    c.text(xs[0], 440, 'input: the pixels', size=16, color=MUTED)
    c.text(xs[1], 440, 'layer 1 (convolutional)', size=16, color=MUTED)
    c.text(xs[2], 440, 'layers 2 – 5 (convolutional)', size=16, color=MUTED)
    c.text(xs[3], 440, 'layers 6 – 8 (fully connected)', size=16, color=MUTED)
    c.text(xs[4], 440, 'output: 1,000 scores', size=16, color=MUTED)
    c.text(0, 500, 'AlexNet, 2012: 8 layers, 60 million weights, all found from 1.2 million labelled photos.', size=20, color=INK)
    c.text(0, 532, 'nobody wrote a rule for "edge" or "leg"; the layers became those detectors because it lowered the error', size=18, color=MUTED)
    return c.finish(name)


# ───────────────────────── two theories of concepts, two kinds of machine ─────────────────────────
def theories_machines(name='theories-machines', w=1680, h=520):
    c = Canvas(w, h)
    x0, cw, gap = 300, 660, 24
    y0, rh = 104, 170
    c.text(x0 + cw / 2, 66, 'HUMANS + CONCEPTS', size=20, anchor='middle', color=INK, weight=700)
    c.text(x0 + cw + gap + cw / 2, 66, 'MACHINES + CONCEPTS', size=20, anchor='middle', color=INK, weight=700)
    rows = [
        ('RULE-BASED', PAPER, ORANGE,
         ['CLASSICAL THEORY', 'a concept is a definition:', 'necessary and sufficient conditions', 'Aristotle · Kant · the dictionary'],
         ['GOFAI · SYMBOLIC AI', 'knowledge written down as rules,', 'applied by a program', 'Dartmouth 1956 · ELIZA · expert systems']),
        ('ADAPTIVE', TEAL_TINT, TEAL,
         ['PROTOTYPE THEORY', 'a concept is its best examples,', 'membership a matter of degree', 'Wittgenstein 1953 · Rosch 1975'],
         ['CONNECTIONISM · MACHINE LEARNING', 'the knowledge is in the weights,', 'found from examples', 'Rosenblatt 1958 · Hinton 1986 · 2012 · today']),
    ]
    for i, (label, fill, col, left, right) in enumerate(rows):
        y = y0 + i * (rh + gap)
        c.text(0, y + rh / 2 + 8, label, size=22, color=col, weight=700)
        for j, lines in enumerate((left, right)):
            x = x0 + j * (cw + gap)
            c.rect(x, y, cw, rh, fill=fill)
            c.text(x + 30, y + 46, lines[0], size=18, color=col, weight=700)
            _lines(c, x + 30, y + 84, lines[1:3], size=20, gap=30, mono=False)
            c.text(x + 30, y + 152, lines[3], size=15, color=MUTED)
    c.text(0, 500, 'the same two ideas, in a mind and in a machine: a rule you can read, or examples you cannot', size=18, color=INK)
    return c.finish(name)


# ───────────────────────── Fauconnier & Turner: two inputs, one blended space ─────────────────────────
def blend_spaces(name='blend-spaces', w=800, h=640):
    c = Canvas(w, h)
    g, a, b_, bl = (400, 110), (170, 300), (630, 300), (400, 500)
    for p, q in ((g, a), (g, b_), (a, bl), (b_, bl), (a, b_)):
        _dashed(c, p[0], p[1], q[0], q[1], MUTED, 2)
    c.circle(*g, 72, fill=PAPER, stroke=MUTED, width=2)
    c.circle(*a, 92, fill=TEAL_TINT, stroke=TEAL, width=3)
    c.circle(*b_, 92, fill=ORANGE_TINT, stroke=ORANGE, width=3)
    c.circle(*bl, 100, fill=VIOLET_TINT, stroke=VIOLET, width=3)
    c.text(g[0], g[1] - 8, 'GENERIC', size=14, anchor='middle', color=MUTED)
    c.text(g[0], g[1] + 14, 'what both share', size=13, anchor='middle', color=MUTED, mono=False)
    c.text(a[0], a[1] - 22, 'INPUT 1', size=14, anchor='middle', color=TEAL)
    c.text(a[0], a[1] + 6, 'house', size=24, anchor='middle', color=INK, mono=False, weight=700)
    c.text(a[0], a[1] + 32, 'lived in · stays put', size=13, anchor='middle', color=INK, mono=False)
    c.text(b_[0], b_[1] - 22, 'INPUT 2', size=14, anchor='middle', color=ORANGE)
    c.text(b_[0], b_[1] + 6, 'boat', size=24, anchor='middle', color=INK, mono=False, weight=700)
    c.text(b_[0], b_[1] + 32, 'floats · moves · a crew', size=13, anchor='middle', color=INK, mono=False)
    c.text(bl[0], bl[1] - 30, 'THE BLEND', size=14, anchor='middle', color=VIOLET)
    c.text(bl[0], bl[1] + 2, 'houseboat', size=26, anchor='middle', color=INK, mono=False, weight=700)
    c.text(bl[0], bl[1] + 30, 'lived in, and it floats', size=13, anchor='middle', color=INK, mono=False)
    c.text(bl[0], bl[1] + 52, 'new: a mooring, a licence, a view that changes', size=12, anchor='middle', color=MUTED, mono=False)
    c.text(400, 628, 'after Fauconnier & Turner, The Way We Think, 2002', size=13, anchor='middle', color=MUTED)
    return c.finish(name)


# ───────────────────────── what an image model does with two concepts ─────────────────────────
def blend_outcomes(name='blend-outcomes', w=1680, h=520):
    c = Canvas(w, h)
    panels = [(0, 'A COLLAGE', 'cup and chair, side by side', 'a rule can do this: both conditions, nothing new'),
              (580, 'A BLEND', 'one thing with properties of both', 'no definition can do this; a prototype machine can'),
              (1160, 'ONE WINS', 'the stronger prototype eats the other', 'watch for it: the middle pulls, always')]
    for x, head, sub, foot in panels:
        c.rect(x, 70, 520, 330, fill='#FFFFFF', stroke=LINE, width=2)
        c.text(x, 40, head, size=18, color=ORANGE)
        c.text(x, 440, sub, size=20, color=INK, mono=False)
        c.text(x, 474, foot, size=16, color=MUTED)
    # left: a cup on a chair
    draw_chair(c, 110, 130, 240, seat_h=0.5, back_h=0.6, back_angle=8, seat_w=0.62, legs=4, width=5)
    draw_cup(c, 300, 110, 130, body_h=0.7, body_w=0.58, taper=0.1, handle=0.26, width=4)
    # middle: a cup with legs and a back: one object
    ox, oy, size = 700, 110, 240
    draw_cup(c, ox, oy, size, body_h=0.62, body_w=0.62, taper=0.1, handle=0.24, width=5)
    foot = oy + size
    cx = ox + size * 0.4
    wb = size * 0.62 * 0.8
    for lx in (cx - wb / 2 + 8, cx - wb / 6, cx + wb / 6, cx + wb / 2 - 8):
        c.line(lx, foot, lx, foot + 70, INK, 5)
    top = oy + size - 0.62 * size
    c.line(cx + size * 0.31, top, cx + size * 0.31 + 10, top - 110, INK, 6)
    c.line(cx + size * 0.31 + 10, top - 110, cx + size * 0.31 - 40, top - 118, INK, 5)
    # right: a chair, the cup a faint outline behind it
    draw_cup(c, 1300, 130, 200, body_h=0.7, body_w=0.58, taper=0.1, handle=0.26, stroke=LINE, width=3)
    draw_chair(c, 1290, 130, 240, seat_h=0.5, back_h=0.6, back_angle=8, seat_w=0.62, legs=4, width=5)
    return c.finish(name)


# ───────────────────────── one step at a time, or every unit at once ─────────────────────────
def serial_parallel(name='serial-parallel', w=1680, h=520):
    c = Canvas(w, h)
    c.text(0, 40, 'A TURING MACHINE · ONE STEP AT A TIME', size=18, color=ORANGE)
    for i in range(10):
        x = i * 78
        c.rect(x, 90, 56, 56, fill=PAPER, stroke=INK, width=2)
        c.text(x + 28, 126, str(i + 1), size=18, anchor='middle', color=INK)
        if i < 9:
            _arrow(c, x + 58, 118, x + 76, 118, INK, 3, 9)
    c.rect(0, 190, 760, 70, fill='#FFFFFF', stroke=INK, width=2)
    for i in range(1, 14):
        c.line(i * 54, 190, i * 54, 260, LINE, 2)
    for i, ch in enumerate('1 0 1 1 0 0 1 0 1 1 0 1 0 0'.split()):
        c.text(27 + i * 54, 234, ch, size=22, anchor='middle', color=INK)
    c.text(0, 300, 'one head, one tape: the whole state is in one place, and you can read it', size=17, color=INK)
    c.text(0, 330, 'the next step waits for this one · rules, applied in order', size=17, color=MUTED)
    c.text(0, 400, 'exact · explainable · one thing at a time', size=18, color=INK)
    x0 = 900
    c.text(x0, 40, 'A NETWORK · EVERY UNIT AT ONCE', size=18, color=ORANGE)
    rnd = random.Random(1958)
    for r in range(4):
        for k in range(8):
            cx, cy = x0 + 40 + k * 100, 110 + r * 76
            for dx in (-16, 0, 16):
                c.line(cx + dx, cy - 44, cx + dx * 0.4, cy - 22, LINE, 2)
            c.circle(cx, cy, 20, fill=(VIOLET, TEAL, ORANGE)[rnd.randint(0, 2)])
            c.text(cx, cy + 6, 'Σ', size=15, anchor='middle', color='#FFFFFF')
    c.text(x0, 420, 'thirty-two sums at the same time, none of them waiting: the same tick for all', size=17, color=INK)
    c.text(x0, 450, 'no state in one place, nothing to read · examples, not rules', size=17, color=MUTED)
    c.text(x0, 500, 'fast, if you have thousands of small processors · opaque, whatever you have', size=18, color=INK)
    c.text(0, 440, 'AlexNet\'s forward pass is about 700 million multiply-adds; a GPU does them a few thousand at a time', size=15, color=MUTED)
    return c.finish(name)


if __name__ == '__main__':
    from deckgen import configure
    configure()
    for fn in (parametric_chairs, typicality_scale, perceptron, two_machines, mediation,
               decision_tree, lewitt_118, lewitt_random_vs_even, lewitt_seeds, lewitt_ten, lewitt_wall, lsystem_growth,
               molnar_desordres, schotter, schotter_variations, spec_pipeline, ten_print, walk_breakdown, walk_through_raster, weight_ramp,
               family_resemblance, fruit_typicality, neuron, xor_limit, backprop, alexnet_layers, theories_machines, blend_spaces, blend_outcomes, serial_parallel):
        svg, png = fn()
        print(png, len(svg))
