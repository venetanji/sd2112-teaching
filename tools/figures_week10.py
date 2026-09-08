"""
Drawn figures for week 10 · Recommendation systems. Every function name and every c.finish name
starts with w10_ / w10- (the generated files share one folder). Each figure explains a mechanism
rather than decorating a slide:

  w10_feed_anatomy   a feed as week 8's five parts run in a loop: the pool, the candidates, the score,
                     the screen, the person — and what you do becoming the data of the next screen
  w10_embedding      an item described with numbers becomes a point; the nearest points are the
                     recommendation; two distances (Euclidean, cosine); the axes are a design decision
  w10_metric         the still twin of the w10-similarity sketch for the code slide: the same forty items and
                     the same query under two weightings, and the two different fives that come out
  w10_matrix         the user–item matrix, mostly empty, and the three ways to fill a cell:
                     rows like yours, columns like this one, a point per row and per column (the same
                     table as the w10-collab sketch, so the figure's ? and the sketch's prediction agree)
  w10_two_tower      a two-tower model in a sentence: the person and the item become points in the same
                     space; the score is one multiplication, so it works for tens of millions of items
  w10_objective      four steps down from what a person values to what the product becomes when a proxy
                     is the target (Strathern 1997), and the repair
  w10_relations      Ihde's four human–technology relations with a feed in each; a feed is mostly
                     hermeneutic and mostly background
"""
from __future__ import annotations

import colorsys
import math
import random

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
TINT_TEAL, TINT_VIOLET, TINT_ORANGE, TINT_YELLOW, TINT_GRAY = '#D3E7E8', '#E5DAEB', '#F9E5D6', '#F8DEB1', '#E9E9E6'
WHITE = '#FFFFFF'


def _lines(c, x, y, lines, size=18, color=INK, lh=None, anchor='start'):
    """A few short mono lines, top-left at (x, y)."""
    lh = lh or round(size * 1.45)
    for i, t in enumerate(lines):
        c.text(x, y + i * lh, t, size=size, color=color, anchor=anchor)


def _dashed(c, x1, y1, x2, y2, color=MUTED, width=2, dash=10, gap=8):
    """A dashed line, drawn as short segments so that both backends agree."""
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    t = 0.0
    while t < length:
        e = min(length, t + dash)
        c.line(x1 + ux * t, y1 + uy * t, x1 + ux * e, y1 + uy * e, color, width, cap='butt')
        t += dash + gap


# ───────────────────────── a feed: five parts in a loop ─────────────────────────
def w10_feed_anatomy(name='w10-feed-anatomy', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 34, "A FEED IS WEEK 8'S FIVE PARTS, RUN IN A LOOP", size=18, color=ORANGE)
    c.text(w, 34, 'Covington, Adams & Sargin 2016 · Zhao et al. 2019: two stages, a few hundred candidates', size=16, color=MUTED, anchor='end')
    y, bw, bh = 180, 250, 104
    boxes = [(0, 'THE POOL', ['millions of items:', 'everything allowed in'], PAPER),
             (330, 'THE CANDIDATES', ['a few hundred: the', 'neighbours of what you did'], TINT_TEAL),
             (660, 'THE SCORE', ['one number per candidate:', 'the objective, predicted'], TINT_VIOLET),
             (990, 'THE SCREEN', ['ten, in order — plus the', 'tries and the shared row'], TINT_ORANGE)]
    for x, t, lines, fill in boxes:
        c.rect(x, y - bh / 2, bw, bh, fill=fill)
        c.text(x + 16, y - 14, t, size=18, color=INK)
        _lines(c, x + 16, y + 14, lines, size=14, color=MUTED, lh=19)
        if x < 990:
            _arrow(c, x + bw, y, x + 330 - 6, y, INK, 4, 12)
    # the person
    c.circle(1430, y, 60, fill=TEAL)
    c.text(1430, y + 8, 'A PERSON', size=17, color=INK, anchor='middle')
    _arrow(c, 1240, y, 1364, y, INK, 4, 12)
    _lines(c, 1520, y - 20, ['watches, skips,', 'likes, answers', 'a survey — or', 'closes the app'], size=14, color=MUTED, lh=19)
    # the loop back
    ly = 300
    c.line(1430, y + 60, 1430, ly, INK, 4, cap='butt')
    c.line(1430, ly, 455, ly, INK, 4, cap='butt')
    _arrow(c, 455, ly, 455, y + bh / 2 + 6, INK, 4, 12)
    c.line(785, ly, 785, y + bh / 2 + 24, INK, 4, cap='butt')
    _arrow(c, 785, y + bh / 2 + 24, 785, y + bh / 2 + 6, INK, 4, 12)
    c.text(940, ly + 30, 'THE LOOP: what you did becomes the data the next screen is built from', size=15, color=INK, anchor='middle')
    # who sets each part
    c.line(0, 380, w, 380, LINE, 2, cap='butt')
    c.text(0, 414, 'WHO SETS IT', size=16, color=ORANGE)
    cols = [(0, 'the pool', 'a policy: what may appear at all'),
            (330, 'the metric', 'which neighbours, by which distance'),
            (660, 'the objective', 'the number you asked it to make bigger'),
            (990, 'the dial', 'how many tries · what everyone sees'),
            (1320, 'the signal', 'what counts: a watch? a like? a survey?')]
    for x, t, s in cols:
        c.text(x, 448, t, size=17, color=INK)
        c.text(x, 474, s, size=14, color=MUTED)
    c.text(0, 540, 'the model makes the score; the pool, the metric, the objective, the dial and the signal are written by hand — by you, or by nobody', size=16, color=INK)
    return c.finish(name)


# ───────────────────────── an item is a point ─────────────────────────
def w10_embedding(name='w10-embedding', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 34, 'DESCRIBE A THING WITH NUMBERS AND IT BECOMES A POINT', size=18, color=ORANGE)
    c.text(w, 34, 'the nearest points are the recommendation · which axes, and which distance, is the design', size=16, color=MUTED, anchor='end')
    # the item and its four numbers
    c.rect(0, 70, 440, 300, fill=PAPER)
    c.text(20, 104, 'ONE ITEM', size=15, color=ORANGE)
    c.text(20, 134, 'a brass desk lamp, warm light,', size=17, color=INK)
    c.text(20, 158, 'small, HK$ 420 (fictional)', size=17, color=INK)
    feats = [('price', 0.35), ('warmth', 0.85), ('size', 0.20), ('metal', 0.90)]
    for i, (f, v) in enumerate(feats):
        fy = 200 + i * 38
        c.text(20, fy + 6, f, size=15, color=MUTED)
        c.rect(120, fy - 8, 240, 18, fill=TINT_GRAY)
        c.rect(120, fy - 8, 240 * v, 18, fill=ORANGE if i == 1 else INK)
        c.text(372, fy + 6, f'{v:.2f}', size=15, color=INK)
    c.text(20, 356, '[0.35, 0.85, 0.20, 0.90]  ·  a point in four dimensions', size=15, color=INK)
    _arrow(c, 450, 220, 520, 220, INK, 4, 12)
    # the map: two of the four axes
    px, py, pw, ph = 560, 70, 560, 276
    c.rect(px, py, pw, ph, stroke=LINE, width=2)
    c.text(px + pw / 2, py + ph + 22, 'warmth →', size=14, color=MUTED, anchor='middle')
    c.text(px - 8, py + 14, 'size', size=14, color=MUTED, anchor='end')
    c.text(px - 8, py + 34, '↑', size=14, color=MUTED, anchor='end')
    rnd = random.Random(10)
    pts = [(rnd.random(), rnd.random()) for _ in range(28)]
    q = (0.85, 0.20)
    ds = sorted(range(len(pts)), key=lambda i: math.hypot(pts[i][0] - q[0], pts[i][1] - q[1]))
    near = ds[:3]
    def P(p):
        return px + 20 + p[0] * (pw - 40), py + ph - 20 - p[1] * (ph - 40)
    qx, qy = P(q)
    for i, p in enumerate(pts):
        x, y = P(p)
        if i in near:
            c.line(qx, qy, x, y, ORANGE, 2, cap='butt')
    for i, p in enumerate(pts):
        x, y = P(p)
        c.circle(x, y, 9 if i in near else 6, fill=ORANGE if i in near else INK)
    c.circle(qx, qy, 14, stroke=ORANGE, width=3)
    c.text(qx - 20, qy - 20, 'the lamp', size=14, color=ORANGE, anchor='end')
    for k, i in enumerate(near):
        x, y = P(pts[i])
        d = math.hypot(pts[i][0] - q[0], pts[i][1] - q[1])
        lx, ly, an = ((x + 16, y + 6, 'start'), (x - 16, y + 24, 'end'), (x - 16, y - 12, 'end'))[k]
        c.text(lx, ly, f'{k + 1} · d = {d:.2f}', size=13, color=INK, anchor=an)
    c.text(px + pw / 2, 404, 'two of the four axes drawn · 28 items · the three nearest to the lamp are what you see next', size=14, color=MUTED, anchor='middle')
    # the two distances
    x0 = 1180
    c.text(x0, 104, 'TWO WAYS TO SAY "NEAR"', size=15, color=ORANGE)
    c.text(x0, 140, 'EUCLIDEAN', size=16, color=INK)
    c.text(x0, 166, 'd = sqrt( sum (a - b)^2 )', size=15, color=INK)
    c.text(x0, 190, 'the straight line between two points', size=13, color=MUTED)
    c.text(x0, 240, 'COSINE', size=16, color=INK)
    c.text(x0, 266, 'the angle between two arrows', size=15, color=INK)
    c.text(x0, 290, 'from the origin: 1 = same direction,', size=13, color=MUTED)
    c.text(x0, 310, '0 = nothing in common; size ignored', size=13, color=MUTED)
    ox, oy = x0 + 380, 330
    _arrow(c, ox, oy, ox + 110, oy - 40, INK, 3, 10)
    _arrow(c, ox, oy, ox + 60, oy - 100, ORANGE, 3, 10)
    c.text(ox + 62, oy - 10, 'θ', size=15, color=MUTED)
    c.text(x0, 356, 'WEIGHTED: multiply an axis before measuring —', size=14, color=INK)
    c.text(x0, 378, 'price x 3 and the neighbourhood changes', size=14, color=INK)
    # bottom
    c.line(0, 430, w, 430, LINE, 2, cap='butt')
    _lines(c, 0, 464, ['by hand: you write the axes (machine A) — price, warmth, size, metal',
                       'learned: a network places items so that things seen together end up near (machine B; word2vec, Mikolov et al. 2013)',
                       'either way the recommendation is the same rule: measure the distance, take the nearest'],
           size=15, color=INK, lh=24)
    c.text(0, 540, 'content-based filtering: "this is like what you liked" — a profile is a point too: the average of what you liked', size=15, color=MUTED)
    return c.finish(name)


# ───────────────────────── the metric, twice ─────────────────────────
def _hsb(h, s, b):
    """p5's colorMode(HSB, 360, 100, 100) as hex — the glyph colours of the w10-similarity sketch."""
    r, g, bl = colorsys.hsv_to_rgb((h % 360) / 360, s / 100, b / 100)
    return '#%02X%02X%02X' % (round(r * 255), round(g * 255), round(bl * 255))


def _glyph(c, x, y, it, hot, scale=1.0):
    """An item as the sketch draws it: 3 to 8 sides by shape (a circle at the top), hue by colour, radius by size."""
    r = (5 + it['size'] * 9) * scale
    n = 3 + int(it['shape'] * 5.99)
    fill = _hsb(20 + it['hue'] * 230, 65, 92)
    stroke, width = (ORANGE, 2.5) if hot else (INK, 1)
    if it['shape'] > 0.92:
        c.circle(x, y, r, fill=fill, stroke=stroke, width=width)
    else:
        pts = [(x + r * math.cos(-math.pi / 2 + 2 * math.pi * k / n), y + r * math.sin(-math.pi / 2 + 2 * math.pi * k / n)) for k in range(n)]
        c.poly(pts, fill=fill, stroke=stroke, width=width)


def w10_metric(name='w10-metric', w=800, h=600):
    """The same forty items and the same query under two metrics: the still twin of the w10-similarity sketch."""
    c = Canvas(w, h)
    rnd = random.Random(10)
    items = [dict(shape=rnd.random(), hue=rnd.random(), size=rnd.random()) for _ in range(40)]
    q = dict(shape=0.60, hue=0.70, size=0.5)   # a query where the two metrics disagree most
    c.text(0, 22, 'ONE QUERY, TWO METRICS, TWO FEEDS', size=16, color=ORANGE)
    panels = [(44, 'BY SHAPE', [1, .2, .2], 'shape x 1 · colour x 0.2 · size x 0.2'),
              (322, 'BY COLOUR', [.2, 1, .2], 'shape x 0.2 · colour x 1 · size x 0.2')]
    px, pw, ph = 0, 480, 210
    for py, label, wts, wtext in panels:
        def d(a, b, wts=wts):
            return math.sqrt(wts[0] * (a['shape'] - b['shape']) ** 2 + wts[1] * (a['hue'] - b['hue']) ** 2 + wts[2] * (a['size'] - b['size']) ** 2)
        ranked = sorted(range(len(items)), key=lambda i: d(q, items[i]))[:5]
        c.text(px, py + 14, label, size=15, color=INK)
        c.text(px + 110, py + 14, wtext, size=13, color=MUTED)
        my = py + 26
        c.rect(px, my, pw, ph, stroke=LINE, width=1)
        c.text(px, my + ph + 16, 'triangle', size=12, color=MUTED)
        c.text(px + pw, my + ph + 16, 'circle', size=12, color=MUTED, anchor='end')
        c.text(px + pw + 8, my + 12, 'warm', size=12, color=MUTED)
        c.text(px + pw + 8, my + ph, 'cool', size=12, color=MUTED)

        def P(it):
            return px + 14 + it['shape'] * (pw - 28), my + 14 + it['hue'] * (ph - 28)

        qx, qy = P(q)
        for i in ranked:
            x, y = P(items[i])
            c.line(qx, qy, x, y, ORANGE, 2, cap='butt')
        for i, it in enumerate(items):
            x, y = P(it)
            _glyph(c, x, y, it, i in ranked, scale=0.8)
        c.circle(qx, qy, 11, stroke=INK, width=2.5)
        lx = 570
        c.text(lx, py + 14, 'THE FIVE NEAREST', size=13, color=ORANGE)
        for k, i in enumerate(ranked):
            y = py + 46 + k * 36
            _glyph(c, lx + 10, y, items[i], True, scale=0.8)
            c.text(lx + 30, y + 5, f'{k + 1} · item {i}   d = {d(q, items[i]):.2f}', size=13, color=INK)
    c.text(0, 590, 'same forty items, same query (the ring); the weights decide which five are "near"', size=13, color=MUTED)
    return c.finish(name)


# ───────────────────────── the user–item matrix ─────────────────────────
# The eleven other listeners, written by hand — the same rows as the w10-collab sketch in deck/week10.py (COLLAB_CODE),
# so that the figure's ? and the sketch's live prediction are one table. Three tastes: A B C D · E F G · H I J,
# and a few likes across them.
LIKES = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],   # U1   A B C D
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],   # U2   E F G
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],   # U3   H I J
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],   # U4   A C D
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],   # U5   B E G
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],   # U6   D H J
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 0],   # U7   A B D F
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],   # U8   F G
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],   # U9   E I J
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],   # U10  A B C
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],   # U11  E F H
]
YOU = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0]  # you: A and D, so far


def w10_matrix(name='w10-matrix', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 34, 'THE USER–ITEM MATRIX IS MOSTLY EMPTY. FILLING A CELL IS THE JOB.', size=18, color=ORANGE)
    c.text(w, 34, 'Netflix, 2006: 100,480,507 ratings in 480,189 × 17,770 cells — about 1.2 % full', size=16, color=MUTED, anchor='end')
    rows = LIKES + [YOU]
    agree = [i for i, r in enumerate(LIKES) if r[0] and r[3]]       # the rows that liked A and D, like you
    with_c = [i for i in agree if LIKES[i][2]]                        # and, of those, the ones that liked C
    x0, y0, cs = 200, 76, 34
    items = 'ABCDEFGHIJ'
    for j, it in enumerate(items):
        c.text(x0 + j * cs + cs / 2, y0 - 10, it, size=15, color=INK, anchor='middle')
    for i, row in enumerate(rows):
        ry = y0 + i * cs
        label = 'YOU' if i == 11 else f'U{i + 1}'
        c.text(x0 - 12, ry + cs / 2 + 6, label, size=15, color=ORANGE if i == 11 else (INK if i in agree else MUTED), anchor='end')
        for j in range(10):
            cx = x0 + j * cs
            c.rect(cx, ry, cs, cs, stroke=LINE, width=1)
            if row[j]:
                c.rect(cx + 6, ry + 6, cs - 12, cs - 12, fill=ORANGE if i == 11 else INK)
    # the cell to fill
    qx, qy = x0 + 2 * cs, y0 + 11 * cs
    c.rect(qx + 2, qy + 2, cs - 4, cs - 4, stroke=ORANGE, width=3)
    c.text(qx + cs / 2, qy + cs / 2 + 7, '?', size=20, color=ORANGE, anchor='middle')
    # rows like yours: the ones that liked A and D too, read off the table
    for i in agree:
        c.rect(x0 - 2, y0 + i * cs - 2, 10 * cs + 4, cs + 4, stroke=TEAL, width=3)
    names = lambda ix: ', '.join(f'U{i + 1}' for i in ix)
    labels = ['rows that agree with yours', f'{names(agree)} liked A and D too', f'{names(with_c)} liked C as well']
    for k, i in enumerate(agree[:3]):
        c.text(x0 + 10 * cs + 16, y0 + i * cs + 24, labels[k], size=14, color=TEAL)
    # the column like the ones you liked
    c.rect(qx - 2, y0 - 2, cs + 4, 12 * cs + 4, stroke=VIOLET, width=3)
    c.text(qx + cs / 2, y0 + 12 * cs + 24, 'column C co-occurs with A and D', size=14, color=VIOLET, anchor='middle')
    # three ways to fill it
    rx = 820
    c.text(rx, 104, 'THREE WAYS TO FILL THE CELL', size=15, color=ORANGE)
    ways = [(140, 'USER–USER', TEAL, ['find the rows that agree with yours; copy what they liked and you have not.',
                                      'GroupLens, 1994: ratings on Usenet news, predicted from users who rated alike.']),
            (250, 'ITEM–ITEM', VIOLET, ['find the columns that co-occur with the ones you liked; recommend those.',
                                        'Amazon, 2003: "customers who bought this also bought" — scales to millions.']),
            (360, 'MODEL-BASED', ORANGE, ['give every row and every column a point — a few numbers each — and make the',
                                          'cell their product. Matrix factorisation: the Netflix Prize, 2006 – 2009.'])]
    for y, t, col, lines in ways:
        c.rect(rx, y - 22, 8, 68, fill=col)
        c.text(rx + 24, y, t, size=17, color=INK)
        _lines(c, rx + 24, y + 26, lines, size=14, color=MUTED, lh=20)
    c.line(rx, 452, w, 452, LINE, 2, cap='butt')
    _lines(c, rx, 486, ['no features anywhere: the crowd is the description. Machine B, from behaviour alone —',
                        'and on day one, with an empty row, it has nothing to say. That is the cold start.'],
           size=15, color=INK, lh=24)
    c.text(0, 540, 'twelve fictional listeners, ten items, a like is a filled cell; the ? is the cell the sketch on the next slide predicts, from this same table', size=15, color=MUTED)
    return c.finish(name)


# ───────────────────────── two towers ─────────────────────────
def w10_two_tower(name='w10-two-tower', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 34, 'TWO TOWERS, IN A SENTENCE: THE PERSON AND THE ITEM BECOME POINTS IN THE SAME SPACE', size=18, color=ORANGE)
    c.text(w, 34, 'Yi et al., RecSys 2019: retrieval from tens of millions of videos', size=16, color=MUTED, anchor='end')

    def tower(x, label, inputs, col):
        c.rect(x, 90, 300, 60, fill=PAPER)
        c.text(x + 150, 116, label, size=16, color=INK, anchor='middle')
        c.text(x + 150, 138, inputs, size=13, color=MUTED, anchor='middle')
        widths = [300, 220, 140, 70]
        for i, ww in enumerate(widths):
            yy = 170 + i * 52
            c.rect(x + (300 - ww) / 2, yy, ww, 36, fill=col if i == 3 else TINT_GRAY)
            if i < 3:
                _arrow(c, x + 150, yy + 36, x + 150, yy + 50, INK, 2, 8)
        c.text(x + 150, 356 + 26, 'a point: a list of numbers', size=13, color=MUTED, anchor='middle')

    tower(80, 'THE PERSON TOWER', 'watched · searched · skipped · when', TEAL)
    tower(1300, 'THE ITEM TOWER', 'title · sound · creator · who watched', VIOLET)
    # the shared space
    sx, sy, sw = 620, 90, 440
    c.rect(sx, sy, sw, 300, stroke=LINE, width=2)
    c.text(sx + sw / 2, sy - 12, 'ONE SPACE', size=15, color=ORANGE, anchor='middle')
    rnd = random.Random(19)
    for _ in range(40):
        c.circle(sx + 20 + rnd.random() * (sw - 40), sy + 20 + rnd.random() * 260, 4, fill=LINE)
    ux, uy = sx + 150, sy + 180
    ix, iy = sx + 300, sy + 110
    c.circle(ux, uy, 12, fill=TEAL)
    c.circle(ix, iy, 12, fill=VIOLET)
    c.line(ux, uy, ix, iy, ORANGE, 3, cap='butt')
    c.text(ux - 16, uy + 6, 'you', size=14, color=INK, anchor='end')
    c.text(ix + 16, iy + 6, 'the item', size=14, color=INK)
    c.text(sx + sw / 2, sy + 330, 'score = you · item  (one multiplication per item)', size=15, color=INK, anchor='middle')
    _arrow(c, 380, 340, sx - 6, 270, TEAL, 3, 10)
    _arrow(c, 1300, 340, sx + sw + 6, 270, VIOLET, 3, 10)
    c.line(0, 430, w, 430, LINE, 2, cap='butt')
    _lines(c, 0, 464, ['the item points are computed once and stored; for a person, find the nearest — a similarity search, like the sketch, over the whole catalogue',
                       'then the ranking model scores the few hundred survivors against the objective (Covington 2016; Zhao et al. 2019)',
                       'a hybrid: the towers can take features (content) and behaviour (who else watched) on the same footing'],
           size=15, color=INK, lh=24)
    c.text(0, 540, 'the sentence for the poster: "a model turns the person and the item into points; near means recommended"', size=15, color=MUTED)
    return c.finish(name)


# ───────────────────────── from what you value to what the product becomes ─────────────────────────
def w10_objective(name='w10-objective', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 34, 'FOUR STEPS DOWN: FROM WHAT A PERSON VALUES TO WHAT THE PRODUCT BECOMES', size=18, color=ORANGE)
    c.text(w, 34, 'Strathern 1997: "when a measure becomes a target, it ceases to be a good measure"', size=16, color=MUTED, anchor='end')
    steps = [('1 · WHAT THEY VALUE', 'an evening well spent;', 'a song they still play in a year', TEAL, 'cannot be measured'),
             ('2 · WHAT CAN BE MEASURED', 'minutes watched · clicks ·', 'days in a row · streams', TINT_TEAL, 'a proxy: near the value, on average'),
             ('3 · WHAT THE MODEL MAXIMISES', 'the proxy — exactly, tirelessly,', 'for a billion people at once', TINT_ORANGE, 'the target'),
             ('4 · WHAT THE PRODUCT BECOMES', 'whatever makes the proxy biggest:', 'autoplay, the cliffhanger, the outrage', ORANGE, 'the trap')]
    sw, sh = 330, 100
    for i, (t, l1, l2, fill, gap) in enumerate(steps):
        x = 0 + i * 350
        y = 80 + i * 62
        c.rect(x, y, sw, sh, fill=fill)
        c.text(x + 16, y + 32, t, size=16, color=INK)
        c.text(x + 16, y + 58, l1, size=14, color=INK if fill in (TEAL, ORANGE) else MUTED)
        c.text(x + 16, y + 78, l2, size=14, color=INK if fill in (TEAL, ORANGE) else MUTED)
        if i < 3:
            _arrow(c, x + sw, y + sh - 10, x + 350, y + 62 + sh - 10, INK, 3, 10)
        c.text(x + 16, y + sh + 24, gap, size=13, color=MUTED)
    # the repair
    rx, ry = 1420, 80
    c.rect(rx, ry, 260, 262, stroke=INK, width=3)
    c.text(rx + 16, ry + 32, 'THE REPAIR', size=16, color=INK)
    _lines(c, rx + 16, ry + 62, ['measure closer to the value:', 'a survey after, a return', 'next week, a regret button',
                                 ' ', 'and write rules around', 'the number: what it may', 'never do to make it bigger'],
           size=14, color=INK, lh=22)
    c.text(rx + 16, ry + 240, 'machine A around machine B', size=13, color=ORANGE)
    c.line(0, 400, w, 400, LINE, 2, cap='butt')
    _lines(c, 0, 434, ['YouTube, 12 October 2012: search and suggestions optimised for time watched — "less clicking, more watching"',
                       'YouTube, RecSys 2019: two groups of objectives — engagement (clicks, watch time) and satisfaction (a like, a rating on the recommendation)',
                       'the number the model makes bigger is the most important sentence in your mediation brief; the model cannot tell step 3 from step 1'],
           size=15, color=INK, lh=24)
    c.text(0, 540, 'Goodhart 1975; Strathern, European Review 5(3), 1997 · the model does not know which step it is on — only you do', size=15, color=MUTED)
    return c.finish(name)


# ───────────────────────── Ihde's four relations, with a feed in each ─────────────────────────
def w10_relations(name='w10-relations', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 34, "WHICH OF IHDE'S FOUR RELATIONS IS A FEED?", size=18, color=ORANGE)
    c.text(w, 34, 'Ihde 1990, Technology and the Lifeworld · Verbeek 2015, Beyond Interaction · week 5', size=16, color=MUTED, anchor='end')
    rels = [('EMBODIMENT', '(I – technology) → world', 'the thumb: the scroll is a gesture', 'you stop noticing, like glasses', 0.25, TINT_GRAY),
            ('HERMENEUTIC', 'I → (technology – world)', 'you read the world through the', 'ranking, as through a thermometer', 0.9, TINT_ORANGE),
            ('ALTERITY', 'I → technology (– world)', 'the DJ that talks, the "For You"', 'that addresses you by name', 0.3, TINT_GRAY),
            ('BACKGROUND', 'I (– technology / world)', 'it runs while you are not looking:', 'the badge, autoplay, Monday\'s playlist', 0.85, TINT_ORANGE)]
    cw = 390
    for i, (t, formula, l1, l2, share, fill) in enumerate(rels):
        x = i * (cw + 40)
        c.rect(x, 70, cw, 250, fill=fill)
        c.text(x + 20, 104, t, size=17, color=INK)
        c.text(x + 20, 134, formula, size=15, color=ORANGE if share > 0.5 else MUTED)
        # the little diagram: I, T, W
        yy = 190
        for k, (lab, col) in enumerate((('I', TEAL), ('T', ORANGE), ('W', VIOLET))):
            cx = x + 60 + k * 120
            c.circle(cx, yy, 22, fill=col)
            c.text(cx, yy + 7, lab, size=16, color=INK if col != VIOLET else WHITE, anchor='middle')
        if i == 0:
            c.rect(x + 30, yy - 32, 200, 64, stroke=INK, width=2)
            _arrow(c, x + 240, yy, x + 270, yy, INK, 3, 10)
        if i == 1:
            c.rect(x + 150, yy - 32, 200, 64, stroke=INK, width=2)
            _arrow(c, x + 90, yy, x + 142, yy, INK, 3, 10)
        if i == 2:
            _arrow(c, x + 90, yy, x + 150, yy, INK, 3, 10)
            _dashed(c, x + 210, yy, x + 270, yy, MUTED, 2, 8, 6)
        if i == 3:
            _dashed(c, x + 90, yy, x + 150, yy, MUTED, 2, 8, 6)
            c.rect(x + 150, yy - 32, 200, 64, stroke=INK, width=2)
        c.text(x + 20, 256, l1, size=14, color=INK)
        c.text(x + 20, 278, l2, size=14, color=INK)
        # how much of the feed lives here
        c.rect(x + 20, 296, cw - 40, 10, fill=WHITE)
        c.rect(x + 20, 296, (cw - 40) * share, 10, fill=ORANGE if share > 0.5 else MUTED)
    c.text(0, 350, 'how much of a feed lives in each relation (our estimate, not a measurement)', size=14, color=MUTED)
    c.line(0, 380, w, 380, LINE, 2, cap='butt')
    _lines(c, 0, 414, ['mostly hermeneutic: the feed is a reading of the world — "this is what is happening, this is what people like you like" — and a reading can be wrong',
                       'mostly background: it works while you do nothing, and the decision it makes on your behalf is never presented as a decision',
                       'the mediation brief names the relation you are building; for a feed, say which of the two — and where the person gets to see it decide'],
           size=15, color=INK, lh=24)
    c.text(0, 520, 'a transparency feature ("why am I seeing this") moves the feed one step towards alterity: for a moment, it faces you and answers', size=15, color=MUTED)
    return c.finish(name)


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    for fn in (w10_feed_anatomy, w10_embedding, w10_metric, w10_matrix, w10_two_tower, w10_objective, w10_relations):
        svg, png = fn()
        print(png, len(svg))
