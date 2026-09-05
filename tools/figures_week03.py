"""
Drawn figures for week 3 · Learning from examples. Every function returns (svg, png) through the
Canvas dual backend in figures.py, so the html deck and the PowerPoint carry the same drawing.
Names are prefixed w03- (the generated figures share one folder).

Each figure explains a mechanism: family resemblance (no feature runs through all the games), the
neuron as a weighted vote, the perceptron settling on a line it was never given, the XOR limit and
the hidden layer, learned features layer by layer, Boden's conceptual space with Move 37 outside it,
telling versus showing an image model, and Labov's cup that becomes a bowl with what is in it.
"""
from __future__ import annotations

import math
import random

from figures import Canvas, _arrow, draw_chair, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

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


def _dashed_ellipse(c, cx, cy, rx, ry, color=MUTED, width=2, n=72):
    pts = [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n + 1)]
    for i in range(0, n, 2):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        c.line(x1, y1, x2, y2, color, width, cap='butt')


def _ellipse(c, cx, cy, rx, ry, fill=None, stroke=None, width=2, n=90):
    pts = [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]
    c.poly(pts, fill=fill, stroke=stroke, width=width)


def _triangle(c, x, y, r, fill=None, stroke=None, width=2):
    c.poly([(x, y - r), (x + r * 0.9, y + r * 0.7), (x - r * 0.9, y + r * 0.7)], fill=fill, stroke=stroke, width=width)


# ───────────────────────── 1 · family resemblance: games ─────────────────────────
GAMES = [
    ('chess', ('board', 'winning', 'skill', 'players')),
    ('football', ('ball', 'winning', 'skill', 'players')),
    ('poker', ('cards', 'winning', 'luck', 'skill', 'players')),
    ('patience', ('cards', 'winning', 'luck', 'skill')),
    ('tennis', ('ball', 'winning', 'skill', 'players')),
    ('ring-a-ring-a-roses', ('players',)),
]
FEATURES = ['board', 'ball', 'cards', 'winning', 'luck', 'skill', 'players']


def w03_family(name='w03-family', w=1680, h=560):
    """Wittgenstein's games: a tick matrix in which no column is full. A definition needs a full column."""
    c = Canvas(w, h)
    x0, col_w, y0, row_h = 330, 144, 128, 62
    c.text(0, 40, 'WITTGENSTEIN, 1953, §66 · CONSIDER FOR EXAMPLE THE PROCEEDINGS THAT WE CALL "GAMES"', size=18, color=ORANGE)
    for j, f in enumerate(FEATURES):
        cx = x0 + j * col_w + col_w / 2
        c.text(cx, 100, f, size=19, anchor='middle', color=INK)
    for i, (game, feats) in enumerate(GAMES):
        y = y0 + i * row_h
        c.line(x0 - 330, y + row_h - 8, x0 + len(FEATURES) * col_w, y + row_h - 8, LINE, 2, cap='butt')
        c.text(0, y + 36, game, size=21, color=INK)
        for j, f in enumerate(FEATURES):
            cx = x0 + j * col_w + col_w / 2
            if f in feats:
                c.circle(cx, y + 28, 13, fill=ORANGE)
            else:
                c.circle(cx, y + 28, 5, fill=LINE)
    y = y0 + len(GAMES) * row_h + 14
    c.text(0, y + 28, 'in all of them?', size=19, color=MUTED)
    for j, f in enumerate(FEATURES):
        cx = x0 + j * col_w + col_w / 2
        c.text(cx, y + 28, 'no', size=19, anchor='middle', color=MUTED)
    c.rect(1400, 128, 280, 300, fill=PAPER)
    for k, t in enumerate(['No column is full:', 'no feature runs', 'through every game.', ' ', 'A definition needs', 'a full column.', ' ', 'The resemblances', 'overlap and', 'criss-cross instead.']):
        c.text(1424, 168 + k * 27, t, size=18, color=INK, mono=False)
    return c.finish(name)


# ───────────────────────── 2 · a neuron is a weighted vote ─────────────────────────
def w03_neuron(name='w03-neuron', w=1680, h=520):
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
    c.text(230, 76, 'INPUTS', size=16, anchor='middle')
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


# ───────────────────────── 3 · the perceptron settling (the same rule as the live sketch) ─────────────────────────
def _clusters(seed=3, n=12):
    rnd = random.Random(seed)
    pts = []
    for _ in range(n):
        pts.append((rnd.gauss(-0.45, 0.2), rnd.gauss(-0.3, 0.2), -1))
    for _ in range(n):
        pts.append((rnd.gauss(0.45, 0.2), rnd.gauss(0.35, 0.2), 1))
    return pts


def _train(pts, epochs, w=(0.3, -1.0, 0.1), lr=0.05):
    w1, w2, b = w
    errors = 0
    for _ in range(epochs):
        errors = 0
        for x, y, t in pts:
            guess = 1 if w1 * x + w2 * y + b > 0 else -1
            if guess != t:
                errors += 1
                w1 += lr * t * x
                w2 += lr * t * y
                b += lr * t
    if epochs == 0:
        errors = sum(1 for x, y, t in pts if (1 if w1 * x + w2 * y + b > 0 else -1) != t)
    return (w1, w2, b), errors


def _panel(c, x0, y0, pw, ph, pts, wts, label):
    c.rect(x0, y0, pw, ph, fill='#FFFFFF', stroke=LINE, width=2)

    def sx(v):
        return x0 + (v + 1) / 2 * pw

    def sy(v):
        return y0 + (1 - v) / 2 * ph

    w1, w2, b = wts
    # the decision line, clipped to the panel
    segs = []
    for xv in (-1, 1):
        if abs(w2) > 1e-6:
            yv = -(w1 * xv + b) / w2
            if -1 <= yv <= 1:
                segs.append((xv, yv))
    for yv in (-1, 1):
        if abs(w1) > 1e-6:
            xv = -(w2 * yv + b) / w1
            if -1 < xv < 1:
                segs.append((xv, yv))
    if len(segs) >= 2:
        (xa, ya), (xb, yb) = segs[0], segs[1]
        c.line(sx(xa), sy(ya), sx(xb), sy(yb), INK, 3)
    for x, y, t in pts:
        if t < 0:
            c.circle(sx(x), sy(y), 7, fill=ORANGE)
        else:
            _triangle(c, sx(x), sy(y), 9, fill=TEAL)
    c.rect(x0 + 2, y0 + 2, 300, 30, fill='#FFFFFF')
    c.text(x0 + 12, y0 + 24, label, size=16, color=INK)


def w03_perceptron_steps(name='w03-perceptron-steps', w=800, h=684):
    c = Canvas(w, h)
    pts = _clusters()
    pw, ph = 380, 300
    for k, (ep, x0, y0) in enumerate(((0, 0, 40), (1, 420, 40), (3, 0, 380), (25, 420, 380))):
        wts, errors = _train(pts, ep)
        _panel(c, x0, y0, pw, ph, pts, wts, f'after {ep} pass{"" if ep == 1 else "es"} · {errors} wrong')
    c.text(0, 24, 'THE LINE MOVES ONLY WHEN A GUESS IS WRONG', size=16, color=ORANGE)
    c.text(800, 24, '● A   ▲ B', size=16, anchor='end', color=MUTED)
    return c.finish(name)


# ───────────────────────── 4 · one line cannot; two layers can ─────────────────────────
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
        # the band |x - y| < 0.35 between two hidden-unit lines holds A
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


def w03_xor(name='w03-xor', w=1680, h=560):
    c = Canvas(w, h)
    pts = _xor_points()
    size = 400
    # left: no single line
    _xor_panel(c, 0, 70, size, pts)
    _dashed(c, 0, 70 + size / 2, size, 70 + size / 2, MUTED, 3)
    _dashed(c, size / 2, 70, size / 2, 70 + size, MUTED, 3)
    _dashed(c, 0, 70 + size, size, 70, MUTED, 3)
    c.text(0, 40, '1969 · MINSKY & PAPERT · ONE LINE CANNOT', size=18, color=ORANGE)
    c.text(0, 520, 'A on one diagonal, B on the other: no line gets all right', size=17, color=INK)
    # middle: the network
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
    for k, t in enumerate(['each hidden unit is one neuron, one line each;', 'the output unit votes on their two verdicts.', 'wrong guess: the error travels backwards', 'and every weight moves a little.', '(9 weights here; 60 million in AlexNet)']):
        c.text(mx, 412 + k * 24, t, size=17, color=INK if k < 4 else MUTED)
    # right: two lines carve a band
    _xor_panel(c, 1280, 70, size, pts, lines=True)
    c.text(1280, 40, 'TWO LINES · A IN THE BAND, B OUTSIDE', size=18, color=ORANGE)
    c.text(1280, 520, 'a rule nobody wrote: "A is in the band"', size=17, color=INK)
    return c.finish(name)


# ───────────────────────── 5 · deep: learned features, layer by layer ─────────────────────────
def w03_layers(name='w03-layers', w=1680, h=560):
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
    # pixels: a grey grid
    n, cell = 10, 26
    gx, gy = xs[0] + (bw - n * cell) / 2, by + (bh - n * cell) / 2
    for r in range(n):
        for k in range(n):
            g = rnd.randint(150, 235)
            c.rect(gx + k * cell, gy + r * cell, cell - 2, cell - 2, fill=f'#{g:02x}{g:02x}{g:02x}')
    # edges: short strokes at a few angles
    for r in range(3):
        for k in range(4):
            cx, cy = xs[1] + 45 + k * 70, by + 55 + r * 95
            a = rnd.choice((0, math.pi / 4, math.pi / 2, 3 * math.pi / 4))
            dx, dy = 22 * math.cos(a), 22 * math.sin(a)
            c.line(cx - dx, cy - dy, cx + dx, cy + dy, INK, 5)
    # parts: a leg, a seat, a back
    px = xs[2]
    c.line(px + 50, by + 60, px + 50, by + 240, INK, 6)                       # a leg
    c.line(px + 40, by + 250, px + 60, by + 250, INK, 5)
    c.rect(px + 100, by + 130, 120, 14, fill=INK)                              # a seat
    c.line(px + 250, by + 240, px + 268, by + 60, INK, 7)                      # a back
    c.line(px + 238, by + 68, px + 268, by + 60, INK, 5)
    c.text(px + 50, by + 280, 'leg', size=15, anchor='middle')
    c.text(px + 160, by + 280, 'seat', size=15, anchor='middle')
    c.text(px + 258, by + 280, 'back', size=15, anchor='middle')
    # objects: a chair
    draw_chair(c, xs[3] + 50, by + 40, 200, seat_h=0.45, back_h=0.6, back_angle=8, seat_w=0.62, legs=4, width=5)
    # label
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


# ───────────────────────── 6 · the conceptual space (Boden, Wiggins) and Move 37 ─────────────────────────
def w03_conceptual_space(name='w03-conceptual-space', w=1680, h=560):
    c = Canvas(w, h)
    rnd = random.Random(37)
    ux, uy, uw, uh = 0, 60, 1140, 470
    c.rect(ux, uy, uw, uh, fill=PAPER, stroke=INK, width=3)
    c.text(ux + 20, uy + 34, 'THE UNIVERSE · EVERY LEGAL MOVE', size=18, color=INK)
    cx, cy, rx, ry = 480, 310, 330, 160
    _dashed_ellipse(c, cx + 80, cy - 10, rx + 190, ry + 78, VIOLET, 3)
    c.text(ux + uw - 20, uy + 34, 'dashed: the space after 2016. human Go, moved', size=17, anchor='end', color=VIOLET)
    _ellipse(c, cx, cy, rx, ry, fill=TEAL_TINT, stroke=TEAL, width=3)
    c.text(cx, cy - 100, 'THE CONCEPTUAL SPACE', size=18, anchor='middle', color=INK)
    c.text(cx, cy - 74, 'the moves people think are good · the rules R', size=16, anchor='middle', color=MUTED)
    for _ in range(60):
        a, r = rnd.uniform(0, 2 * math.pi), math.sqrt(rnd.random())
        c.circle(cx + rx * 0.9 * r * math.cos(a), cy + 20 + ry * 0.75 * r * math.sin(a), 4, fill=INK)
    c.text(cx, cy + 135, 'exploratory: search inside the space (T), keep what scores well (E)', size=16, anchor='middle', color=INK)
    mx, my = 980, 160
    c.circle(mx, my, 14, fill=ORANGE)
    c.text(mx, my - 30, 'MOVE 37', size=18, anchor='middle', color=ORANGE)
    c.text(mx, my + 44, 'outside R, inside the game', size=16, anchor='middle', color=INK)
    _arrow(c, cx + rx * 0.7, cy - 40, mx - 24, my + 14, ORANGE, 3, 12)
    c.text(860, 300, 'transformational:', size=16, anchor='middle', color=ORANGE)
    c.text(860, 324, 'the space itself moves', size=16, anchor='middle', color=ORANGE)
    # right: the vocabulary
    tx = 1200
    c.text(tx, 84, 'BODEN, 1990 / 2004', size=18, color=ORANGE)
    for k, t in enumerate(['combinational: familiar ideas,', 'new combination', 'exploratory: new places in a', 'known space', 'transformational: change the', 'rules of the space']):
        c.text(tx, 118 + k * 26, t, size=17, color=INK if k % 2 == 0 else MUTED)
    c.text(tx, 320, 'WIGGINS, 2006', size=18, color=ORANGE)
    for k, t in enumerate(['R  what counts as a member', 'T  how the space is searched', 'E  how a member is judged', ' ', 'creative systems can be', 'compared on R, T and E']):
        c.text(tx, 354 + k * 26, t, size=17, color=INK if k < 3 else MUTED)
    return c.finish(name)


# ───────────────────────── 7 · telling and showing an image model ─────────────────────────
def _model_box(c, x, y, w, h, seed):
    c.rect(x, y, w, h, fill=INK)
    rnd = random.Random(seed)
    for i in range(10):
        col, row = i % 5, i // 5
        draw_chair(c, x + 14 + col * 54, y + 16 + row * 66, 44, seat_h=rnd.uniform(0.38, 0.55), back_h=rnd.uniform(0.4, 0.7),
                   back_angle=rnd.uniform(0, 16), seat_w=rnd.uniform(0.5, 0.75), legs=rnd.choice([2, 4, 4]), stroke=TEAL_TINT, width=1.5)
    c.text(x + w / 2, y + h - 12, 'the model: millions of examples', size=14, anchor='middle', color=TEAL_TINT)


def w03_tell_show(name='w03-tell-show', w=1680, h=520):
    c = Canvas(w, h)
    rows = ((40, 'TELL · a prompt is a rule', '"a chair"'), (290, 'SHOW · a reference is an example', '"a chair like these"'))
    for y, head, prompt in rows:
        c.text(0, y - 10, head, size=18, color=ORANGE)
        c.rect(0, y + 10, 330, 170, fill=PAPER)
        c.text(20, y + 60, prompt, size=24, color=INK, mono=False)
        _arrow(c, 340, y + 95, 430, y + 95, INK, 3, 10)
        _model_box(c, 440, y + 10, 300, 170, 7)
        _arrow(c, 750, y + 95, 840, y + 95, INK, 3, 10)
        c.rect(850, y + 10, 240, 170, fill='#FFFFFF', stroke=LINE, width=2)
    # row 1: the prototype
    draw_chair(c, 900, 65, 140, seat_h=0.45, back_h=0.6, back_angle=8, seat_w=0.62, legs=4, width=4)
    c.text(1120, 120, 'the middle: four legs, a back,', size=18, color=INK)
    c.text(1120, 148, 'a bit of mid-century. every time.', size=18, color=INK)
    c.text(1120, 190, 'words select; they do not add examples', size=17, color=MUTED)
    # row 2: two references, an in-between
    y = 290
    draw_chair(c, 40, y + 95, 70, seat_h=0.62, back_h=0.75, back_angle=20, seat_w=0.5, legs=3, width=3)
    draw_chair(c, 140, y + 95, 70, seat_h=0.3, back_h=0.3, back_angle=0, seat_w=0.85, legs=2, leg_splay=0.12, width=3)
    c.text(240, y + 160, '+ 2 refs', size=16, color=MUTED)
    draw_chair(c, 900, y + 25, 140, seat_h=0.46, back_h=0.52, back_angle=10, seat_w=0.68, legs=3, leg_splay=0.06, width=4)
    c.text(1120, y + 80, 'pulled toward the references:', size=18, color=INK)
    c.text(1120, y + 108, 'their height, their splay, their back.', size=18, color=INK)
    c.text(1120, y + 150, 'an example moves the middle;', size=17, color=MUTED)
    c.text(1120, y + 176, 'it cannot say "no handle"', size=17, color=MUTED)
    return c.finish(name)


# ───────────────────────── 8 · Labov: the same drawing, three contexts ─────────────────────────
def _vessel(c, cx, base_y, width, height, fill='#FFFFFF'):
    top_w = width
    bot_w = width * 0.78
    pts = [(cx - top_w / 2, base_y - height), (cx + top_w / 2, base_y - height), (cx + bot_w / 2, base_y), (cx - bot_w / 2, base_y)]
    c.poly(pts, fill=fill, stroke=INK, width=4)
    return pts


def w03_labov_context(name='w03-labov-context', w=800, h=500):
    c = Canvas(w, h)
    rnd = random.Random(1973)
    c.text(0, 36, 'LABOV, 1973 · THE SAME DRAWING, THREE CONTEXTS', size=16, color=ORANGE)
    vw, vh, base = 150, 130, 330
    for k, (cx, content, label) in enumerate(((140, 'coffee', 'cup'), (400, 'mashed potatoes', 'bowl'), (660, 'flowers', 'vase'))):
        _vessel(c, cx, base, vw, vh)
        if content == 'coffee':
            c.poly([(cx - vw / 2 + 8, base - vh + 30), (cx + vw / 2 - 8, base - vh + 30), (cx + vw * 0.39 - 6, base - 6), (cx - vw * 0.39 + 6, base - 6)], fill='#5A3A1E')
            for i in range(3):
                x = cx - 30 + i * 30
                c.line(x, base - vh - 14, x + 6, base - vh - 40, MUTED, 3)
        elif content == 'mashed potatoes':
            pts = [(cx - vw / 2 + 6, base - vh + 40)]
            for i in range(9):
                pts.append((cx - vw / 2 + 6 + (i + 1) * (vw - 12) / 10, base - vh + 40 - rnd.uniform(4, 34)))
            pts += [(cx + vw / 2 - 6, base - vh + 40), (cx + vw * 0.39 - 6, base - 6), (cx - vw * 0.39 + 6, base - 6)]
            c.poly(pts, fill='#F1E4B8')
        else:
            for i, dx in enumerate((-36, -12, 14, 38)):
                c.line(cx + dx * 0.4, base - 20, cx + dx, base - vh - 50 - i % 2 * 20, '#3E7A3A', 4)
                c.circle(cx + dx, base - vh - 56 - i % 2 * 20, 14, fill=(ORANGE, VIOLET, TEAL, ORANGE)[i])
        c.text(cx, base + 44, f'with {content}', size=18, anchor='middle', color=MUTED)
        c.text(cx, base + 86, f'"{label}"', size=26, anchor='middle', color=INK)
    c.text(400, 470, 'the edge of a concept moves with what is in it', size=18, anchor='middle', color=INK)
    return c.finish(name)


if __name__ == '__main__':
    for fn in (w03_family, w03_neuron, w03_perceptron_steps, w03_xor, w03_layers, w03_conceptual_space, w03_tell_show, w03_labov_context):
        svg, png = fn()
        print(png, len(svg))
