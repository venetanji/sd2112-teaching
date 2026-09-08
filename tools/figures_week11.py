"""
Drawn figures for week 11 · Curators of outputs and datasets. Every function name and every c.finish
name starts with w11_ / w11- (the generated files share one folder). Each figure explains a mechanism
rather than decorating a slide:

  w11_belamy_chain      six hands between the 14th-century painters and the Christie's hammer, and what
                        each one did: made, gathered, invented, wrote, chose, sold
  w11_funnel            64 → 12 → 3 → 1: the model generates, the designer discards, shortlists and ships;
                        the tiles follow the same rule as the w11-curate sketch
  w11_lora_mean         two twelve-image datasets, the style each one teaches (the mean tile and the
                        spread of every feature) and what comes out; the twin of the w11-dataset sketch
  w11_authorship_ladder prompt · pick · arrange · modify · make: what the designer did at each step and
                        where, in the 2025 US position, a human author begins
  w11_poster_anatomy    the A0 poster's four zones and the process strip, with the rubric weights drawn
                        onto the zones they reward
  w11_storyboard        the 3–5 minute video in six shots, timed
"""
from __future__ import annotations

import math
import random

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
WHITE = '#FFFFFF'
TINT_TEAL, TINT_ORANGE, TINT_PINK, TINT_GRAY, TINT_YELLOW = '#D3E7E8', '#F9E5D6', '#F7E3E8', '#E9E9E6', '#F8DEB1'
PINK = '#E94D7F'


def _lines(c, x, y, lines, size=18, color=INK, lh=None, anchor='start'):
    lh = lh or round(size * 1.45)
    for i, t in enumerate(lines):
        c.text(x, y + i * lh, t, size=size, color=color, anchor=anchor)


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


def _arc(c, cx, cy, r, a0, a1, color=INK, width=2, n=10):
    """A circular arc as short segments (the Canvas has no arc)."""
    pts = [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        c.line(xa, ya, xb, yb, color, width, cap='round')


def _hex_lerp(a, b, t):
    ra, ga, ba = int(a[1:3], 16), int(a[3:5], 16), int(a[5:7], 16)
    rb, gb, bb = int(b[1:3], 16), int(b[3:5], 16), int(b[5:7], 16)
    return '#%02X%02X%02X' % (round(ra + (rb - ra) * t), round(ga + (gb - ga) * t), round(ba + (bb - ba) * t))


# ───────────────────────── the curate rule (the same rule as the w11-curate sketch) ─────────────────────────
def _curate_params(rnd):
    """One tile of the rule: a k × k grid of cells; each cell drawn with probability `density`, with one motif."""
    return dict(k=rnd.choice([2, 3, 4, 5]), density=rnd.uniform(0.35, 1.0), motif=rnd.choice([0, 1, 2]),
                rot=rnd.choice([0, 1, 2, 3]), weight=rnd.choice([1, 2, 3]), color=rnd.choice([INK, ORANGE, TEAL]))


def _curate_tile(c, x, y, s, p, seed, frame=LINE, frame_w=1):
    rnd = random.Random(seed)
    c.rect(x, y, s, s, fill=WHITE, stroke=frame, width=frame_w)
    k, cell = p['k'], s / p['k']
    w = max(1, round(p['weight'] * s / 80))
    for r in range(k):
        for col in range(k):
            if rnd.random() > p['density']:
                continue
            cx, cy = x + col * cell, y + r * cell
            d = (p['rot'] + r + col) % 4
            if p['motif'] == 0:                                   # a diagonal, direction from the rotation and the cell
                if d % 2 == 0:
                    c.line(cx + 2, cy + 2, cx + cell - 2, cy + cell - 2, p['color'], w)
                else:
                    c.line(cx + cell - 2, cy + 2, cx + 2, cy + cell - 2, p['color'], w)
            elif p['motif'] == 1:                                 # a quarter circle, hinged on one corner
                corner = [(cx, cy), (cx + cell, cy), (cx + cell, cy + cell), (cx, cy + cell)][d]
                a0 = [0, math.pi / 2, math.pi, 3 * math.pi / 2][d]
                _arc(c, corner[0], corner[1], cell - 2, a0, a0 + math.pi / 2, p['color'], w)
            else:                                                 # a dot, sized by the weight
                c.circle(cx + cell / 2, cy + cell / 2, max(1.5, cell * (0.12 + 0.08 * p['weight'])), fill=p['color'])


def _curate_set(seed=11, n=64):
    rnd = random.Random(seed)
    return [_curate_params(rnd) for _ in range(n)]


# ───────────────────────── the dataset rule (the same rule as the w11-dataset sketch) ─────────────────────────
def _style_params(rnd, hue=None, stroke=None, rnd_=None, size=None, rot=None):
    return dict(hue=rnd.uniform(0, 1) if hue is None else hue, stroke=rnd.uniform(1, 6) if stroke is None else stroke,
                round=rnd.uniform(0, 1) if rnd_ is None else rnd_, size=rnd.uniform(0.4, 0.9) if size is None else size,
                rot=rnd.uniform(0, 45) if rot is None else rot)


def _style_tile(c, x, y, s, p, frame=LINE, frame_w=1, bg=WHITE):
    """A rounded square, rotated: colour from the hue, corner radius from roundness, stroke, size, rotation."""
    c.rect(x, y, s, s, fill=bg, stroke=frame, width=frame_w)
    color = _hex_lerp(TEAL, ORANGE, p['hue'])
    half = p['size'] * s / 2
    r = p['round'] * half
    a = math.radians(p['rot'])
    cx, cy = x + s / 2, y + s / 2
    pts = []
    for (qx, qy, a0) in ((half - r, -(half - r), -math.pi / 2), (half - r, half - r, 0), (-(half - r), half - r, math.pi / 2), (-(half - r), -(half - r), math.pi)):
        for i in range(7):
            ang = a0 + (math.pi / 2) * i / 6
            px, py = qx + r * math.cos(ang), qy + r * math.sin(ang)
            pts.append((cx + px * math.cos(a) - py * math.sin(a), cy + px * math.sin(a) + py * math.cos(a)))
    c.poly(pts, stroke=color, width=max(1, p['stroke'] * s / 80))


FEATS = ['hue', 'stroke', 'round', 'size', 'rot']
RANGES = dict(hue=(0, 1), stroke=(1, 6), round=(0, 1), size=(0.4, 0.9), rot=(0, 45))


def _mean_spread(ps):
    mean, spread = {}, {}
    for f in FEATS:
        vals = [p[f] for p in ps]
        m = sum(vals) / len(vals)
        mean[f] = m
        spread[f] = math.sqrt(sum((v - m) ** 2 for v in vals) / len(vals))
    return mean, spread


def _sample(mean, spread, rnd):
    out = {}
    for f in FEATS:
        lo, hi = RANGES[f]
        out[f] = min(hi, max(lo, rnd.gauss(mean[f], spread[f])))
    return out


# ───────────────────────── 1 · six hands between the painters and the hammer ─────────────────────────
def w11_belamy_chain(name='w11-belamy-chain', w=1680, h=560):
    c = Canvas(w, h)
    c.text(20, 44, 'WHO MADE EDMOND DE BELAMY? SIX HANDS, ONE SIGNATURE.', size=18, color=ORANGE)
    hands = [
        ('MADE', 'The painters', ['14th – 20th century.', 'Fifteen thousand', 'portraits, one at a', 'time, by hand.'], TINT_GRAY),
        ('GATHERED', 'WikiArt', ['Scanned, tagged and', 'put online: the', 'dataset, before anyone', 'called it that.'], TINT_GRAY),
        ('INVENTED', 'Goodfellow · 2014', ['The GAN: a forger and', 'a critic, trained', 'against each other.', 'One loss function.'], TINT_TEAL),
        ('WROTE', 'Robbie Barrat · 2017', ['The code, on GitHub,', 'open source, trained', 'on portraits. He was', 'a teenager.'], TINT_TEAL),
        ('CHOSE', 'Obvious · 2018', ['Ran the code. Kept', 'eleven. Sent one to', 'auction, signed with', 'the loss function.'], TINT_ORANGE),
        ('SOLD', 'Christie’s · 2018', ['25 October, New York.', 'Estimate $7,000 to', '$10,000. Sold for', '$432,500 with premium.'], TINT_PINK),
    ]
    bw, gap, y0, bh = 240, 40, 100, 280
    for i, (tag, who, lines, tint) in enumerate(hands):
        x = 20 + i * (bw + gap)
        c.rect(x, y0, bw, bh, fill=tint)
        c.text(x + 20, y0 + 40, tag, size=18, color=ORANGE if tag != 'CHOSE' else INK)
        c.text(x + 20, y0 + 80, who, size=19, color=INK)
        _lines(c, x + 20, y0 + 122, lines, size=16, color=INK if tag == 'CHOSE' else MUTED, lh=26)
        if i < len(hands) - 1:
            _arrow(c, x + bw + 6, y0 + bh / 2, x + bw + gap - 6, y0 + bh / 2, INK, 3, 10)
    # the signature and the two questions under it
    c.rect(20, 410, 1640, 2, LINE)
    c.text(20, 452, 'signed, bottom right:  min G max D  Ex[log D(x)] + Ez[log(1 − D(G(z)))]', size=20, color=INK)
    c.text(20, 490, 'the formula every GAN is trained with — not Obvious’s, not Barrat’s: Goodfellow’s, 2014', size=16, color=MUTED)
    c.text(w - 20, 452, 'the market paid the hand that chose', size=20, color=ORANGE, anchor='end')
    c.text(w - 20, 490, 'the paintings, the code and the formula were somebody else’s', size=16, color=MUTED, anchor='end')
    return c.finish(name)


# ───────────────────────── 2 · the funnel: 64 → 12 → 3 → 1 ─────────────────────────
def w11_funnel(name='w11-funnel', w=1680, h=560):
    c = Canvas(w, h)
    ps = _curate_set(11)
    rnd = random.Random(64)
    keep12 = sorted(rnd.sample(range(64), 12))
    keep3 = sorted(rnd.sample(keep12, 3))
    ship = keep3[1]
    # stage 1: the 64
    x1, y1, s1, g1 = 60, 130, 26, 4
    for i, p in enumerate(ps):
        col, row = i % 8, i // 8
        _curate_tile(c, x1 + col * (s1 + g1), y1 + row * (s1 + g1), s1, p, 1000 + i)
    # stage 2: the 12
    x2, y2, s2, g2 = 430, 150, 44, 6
    for j, i in enumerate(keep12):
        col, row = j % 4, j // 4
        _curate_tile(c, x2 + col * (s2 + g2), y2 + row * (s2 + g2), s2, ps[i], 1000 + i)
    # stage 3: the 3
    x3, y3, s3, g3 = 740, 170, 96, 12
    for j, i in enumerate(keep3):
        _curate_tile(c, x3 + j * (s3 + g3), y3, s3, ps[i], 1000 + i, frame=ORANGE, frame_w=3)
    # stage 4: the one
    x4, y4, s4 = 1160, 100, 240
    _curate_tile(c, x4, y4, s4, ps[ship], 1000 + ship, frame=ORANGE, frame_w=5)
    # arrows and labels
    for (xa, xb) in ((300, 420), (632, 728), (1058, 1148)):
        _arrow(c, xa, 235, xb, 235, INK, 3, 10)
    labels = [
        (x1, 'GENERATE', 'the model · 64 in a minute', 'every one obeys the rule'),
        (x2, 'DISCARD', 'you · 52 gone', 'the wrong, the same, the unsafe'),
        (x3, 'SHORTLIST', 'you · three, with a reason each', 'the reasons are the design'),
        (x4, 'SHIP', 'you · one, your name on it', 'and you answer for it'),
    ]
    for x, head, sub, sub2 in labels:
        c.text(x, 100 if x != x4 else 80, head, size=18, color=ORANGE if x != x1 else MUTED)
        c.text(x, 396, sub, size=17, color=INK)
        c.text(x, 424, sub2, size=15, color=MUTED)
    # the two brackets
    c.line(60, 470, 300, 470, MUTED, 3, cap='butt'); c.text(180, 500, 'THE MODEL’S WORK', size=16, color=MUTED, anchor='middle')
    c.line(430, 470, 1400, 470, ORANGE, 3, cap='butt'); c.text(915, 500, 'YOUR WORK: THE PICK IS THE AUTHORSHIP', size=16, color=ORANGE, anchor='middle')
    c.text(w - 20, 540, 'Belamy: eleven kept, one sent to auction. Netflix: several posters, one shown. Midjourney: four, and you press one.', size=15, color=MUTED, anchor='end')
    return c.finish(name)


# ───────────────────────── 3 · what you put in is what comes out ─────────────────────────
def _dataset(seed, tight):
    rnd = random.Random(seed)
    out = []
    for _ in range(12):
        if tight:
            out.append(_style_params(rnd, hue=rnd.uniform(0.8, 1.0), stroke=rnd.uniform(1.2, 2.2), rnd_=rnd.uniform(0.75, 1.0), size=rnd.uniform(0.6, 0.8), rot=rnd.uniform(0, 12)))
        else:
            out.append(_style_params(rnd))
    return out


def _row(c, y, ps, label, sub, seed, verdict):
    # the twelve
    s, g = 56, 6
    for i, p in enumerate(ps):
        col, row = i % 6, i // 6
        _style_tile(c, 40 + col * (s + g), y + row * (s + g), s, p)
    c.text(40, y - 16, label, size=18, color=ORANGE)
    c.text(40, y + 2 * (s + g) + 22, sub, size=15, color=MUTED)
    _arrow(c, 430, y + 60, 490, y + 60, INK, 3, 10)
    # the style learned: mean tile and spread bars
    mean, spread = _mean_spread(ps)
    _style_tile(c, 510, y - 4, 124, mean, frame=INK, frame_w=2, bg=PAPER)
    c.text(510, y - 16, 'STYLE LEARNED', size=18, color=ORANGE)
    bx = 660
    for i, f in enumerate(FEATS):
        lo, hi = RANGES[f]
        rel = spread[f] / (hi - lo)
        yy = y + 4 + i * 26
        c.text(bx, yy + 10, f, size=14, color=MUTED)
        c.rect(bx + 70, yy - 2, 200, 14, fill=TINT_GRAY)
        c.rect(bx + 70, yy - 2, max(4, 200 * min(1, rel * 3.2)), 14, fill=ORANGE if rel > 0.15 else TEAL)
    c.text(bx, y + 150, 'the mean is the middle · the bars are how much room is left', size=14, color=MUTED)
    _arrow(c, 960, y + 60, 1020, y + 60, INK, 3, 10)
    # what comes out
    rnd = random.Random(seed)
    for i in range(4):
        _style_tile(c, 1040 + i * 92, y + 12, 84, _sample(mean, spread, rnd))
    c.text(1040, y - 16, 'WHAT COMES OUT', size=18, color=ORANGE)
    c.text(1040, y + 122, verdict, size=15, color=INK)


def w11_lora_mean(name='w11-lora-mean', w=1680, h=560):
    c = Canvas(w, h)
    _row(c, 60, _dataset(1, True), 'DATASET A · 12 OF YOUR ROUND SKETCHES', 'consistent in one thing, varied in the rest', 5,
         'round, orange, thin — every time. A style.')
    _row(c, 330, _dataset(2, False), 'DATASET B · 12 OF EVERYTHING YOU LIKED', 'no two alike; nothing in common', 6,
         'the middle of everything. A muddle.')
    c.rect(40, 292, 1600, 2, LINE)
    c.text(w - 20, 540, 'a fine-tune moves the middle to the mean of what you gave it, and leaves as much room as your examples disagree', size=15, color=MUTED, anchor='end')
    return c.finish(name)


# ───────────────────────── 4 · the authorship ladder ─────────────────────────
def w11_authorship_ladder(name='w11-authorship-ladder', w=1680, h=560):
    c = Canvas(w, h)
    steps = [
        ('PROMPT', ['You typed. Even', '624 times, about', '80 hours (Allen).'], ['not an author: a prompt', 'is an instruction; the', 'model decides the picture'], TINT_GRAY),
        ('PICK', ['You chose one of', '64 and shipped it', 'as it came.'], ['the picked image is not', 'yours in law; a pick alone', 'is not a work'], TINT_GRAY),
        ('ARRANGE', ['You chose several', 'and composed them:', 'pages, a layout.'], ['the selection and the', 'arrangement are yours', '(Zarya, 2023); the images', 'inside are not'], TINT_YELLOW),
        ('MODIFY', ['You repainted,', 'cut, redrew what', 'came back.'], ['what you changed is', 'yours; the rest is not;', 'how much, case by case'], TINT_ORANGE),
        ('MAKE', ['You drew it. You', 'fed a model your', 'own sketches.'], ['yours. It always was.', 'And the model learned', 'your edge, not the middle'], TINT_TEAL),
    ]
    bw, gap, x0 = 300, 30, 30
    y_head, y_box, bh = 60, 90, 120
    for i, (head, did, verdict, tint) in enumerate(steps):
        x = x0 + i * (bw + gap)
        c.text(x, y_head, f'{i + 1} · {head}', size=18, color=ORANGE)
        c.rect(x, y_box, bw, bh, fill=tint)
        _lines(c, x + 16, y_box + 34, did, size=16, color=INK, lh=26)
        # a small drawing of the step
        ix, iy = x + 208, y_box + 20
        if i == 0:
            for k in range(4):
                c.line(ix, iy + 12 + k * 18, ix + 70 - (k % 2) * 24, iy + 12 + k * 18, MUTED, 3)
        elif i == 1:
            for k in range(9):
                cc, rr = k % 3, k // 3
                c.rect(ix + cc * 26, iy + rr * 26, 22, 22, fill=WHITE, stroke=ORANGE if k == 4 else LINE, width=3 if k == 4 else 1)
        elif i == 2:
            for k, (cc, rr, ww, hh) in enumerate(((0, 0, 46, 30), (50, 0, 24, 30), (0, 34, 24, 40), (28, 34, 46, 40))):
                c.rect(ix + cc, iy + rr, ww, hh, fill=WHITE, stroke=ORANGE, width=2)
        elif i == 3:
            c.rect(ix, iy, 74, 74, fill=WHITE, stroke=LINE, width=1)
            c.line(ix + 10, iy + 60, ix + 64, iy + 12, ORANGE, 5)
            c.line(ix + 12, iy + 20, ix + 40, iy + 66, ORANGE, 5)
        else:
            _arc(c, ix + 37, iy + 40, 30, 0.3, 5.6, ORANGE, 4, n=16)
            c.line(ix + 10, iy + 70, ix + 66, iy + 66, ORANGE, 4)
        c.text(x, y_box + bh + 40, 'US COPYRIGHT OFFICE · 2025', size=14, color=MUTED)
        _lines(c, x, y_box + bh + 70, verdict, size=16, color=INK, lh=25)
    # the bar under it all: where an author begins
    yb = 470
    for i in range(5):
        x = x0 + i * (bw + gap)
        c.rect(x, yb, bw, 14, fill=[TINT_GRAY, TINT_GRAY, TINT_YELLOW, TINT_ORANGE, ORANGE][i])
    c.text(x0, yb + 44, 'none of it is yours', size=16, color=MUTED)
    c.text(x0 + 4 * (bw + gap) + bw, yb + 44, 'all of it is yours', size=16, color=ORANGE, anchor='end')
    c.text(w / 2, yb + 44, 'the law and the rubric draw the same line: what you chose, arranged, changed and made', size=16, color=INK, anchor='middle')
    return c.finish(name)


# ───────────────────────── 5 · the A0 poster, and where the marks are ─────────────────────────
def w11_poster_anatomy(name='w11-poster-anatomy', w=1680, h=560):
    """The A0's four zones and the process strip, the rubric weight written on the zone it rewards, and the five
    rubric rows beside it. Drawn at 1680 × 560 for a slide with no body, so nothing is scaled down."""
    c = Canvas(w, h)
    px, py, pw, ph = 40, 16, 364, 515            # 841 × 1189 mm, portrait, at scale
    c.rect(px, py, pw, ph, fill=WHITE, stroke=INK, width=3)
    ix, iw = px + 10, pw - 20                     # the inner column
    half = (iw - 10) / 2
    # the title band, and the whole-poster mark on it
    c.rect(ix, py + 10, iw, 50, fill=INK)
    c.text(ix + 12, py + 41, 'TITLE · ONE SENTENCE · TEAM', size=15, color=WHITE)
    c.text(ix + iw - 12, py + 41, '20%', size=20, color=ORANGE, anchor='end')
    # the zones, each with its weight
    zones = [
        (ix, py + 70, half, 150, TINT_TEAL, 'RESEARCH', '30%'),
        (ix + half + 10, py + 70, half, 150, TINT_YELLOW, 'CONCEPT', ''),
        (ix, py + 230, iw, 104, TINT_ORANGE, 'THE DECISION', ''),
        (ix, py + 344, iw, 110, TINT_PINK, 'THE MEDIATION', '30%'),
        (ix, py + 464, iw, 41, TINT_GRAY, 'PROCESS · TOOLS · QR', '10% + 10%'),
    ]
    for x, y, zw, zh, tint, label, pct in zones:
        c.rect(x, y, zw, zh, fill=tint)
        c.text(x + 10, y + 26, label, size=16 if zh > 60 else 14, color=INK)
        if pct:
            c.text(x + zw - 10, y + 26, pct, size=20 if zh > 60 else 18, color=ORANGE, anchor='end')
    # research: four sources; concept: the person and the moment
    for k in range(4):
        c.rect(ix + 12, py + 108 + k * 26, 118 - k * 14, 12, fill=WHITE)
    cx = ix + half + 10 + half / 2
    c.circle(cx, py + 134, 22, fill=WHITE, stroke=INK, width=2)
    c.rect(cx - 18, py + 164, 36, 46, fill=WHITE, stroke=INK, width=2)
    # the decision: data → score → line → decides, or falls back (week 8's anatomy)
    dx, dy = ix + 12, py + 274
    for k, lab in enumerate(['data', 'score', 'line']):
        c.rect(dx + k * 70, dy, 56, 36, fill=WHITE, stroke=INK, width=2)
        c.text(dx + k * 70 + 28, dy + 23, lab, size=14, color=INK, anchor='middle')
        if k < 2:
            _arrow(c, dx + k * 70 + 58, dy + 18, dx + (k + 1) * 70 - 2, dy + 18, INK, 2, 7)
    _arrow(c, dx + 198, dy + 18, dx + 228, dy + 6, INK, 2, 7)
    _arrow(c, dx + 198, dy + 18, dx + 228, dy + 32, INK, 2, 7)
    c.text(dx + 234, dy + 11, 'decides', size=14, color=INK)
    c.text(dx + 234, dy + 37, 'fallback', size=14, color=MUTED)
    # the mediation: the four cells of the brief
    cw_ = (iw - 24 - 8) / 2
    for k, lab in enumerate(['relation', 'data', 'bias', 'guardrails']):
        col, row = k % 2, k // 2
        x, y = ix + 12 + col * (cw_ + 8), py + 378 + row * 38
        c.rect(x, y, cw_, 32, fill=WHITE)
        c.text(x + cw_ / 2, y + 21, lab, size=14, color=INK, anchor='middle')
    # the QR code in the strip
    qx, qy = ix + 190, py + 470                 # between the label and the weight
    c.rect(qx, qy, 29, 29, fill=INK)
    for (ox, oy) in ((4, 4), (18, 4), (4, 18)):
        c.rect(qx + ox, qy + oy, 7, 7, fill=WHITE)
    c.text(px, py + ph + 22, '841 × 1189 mm, portrait', size=15, color=MUTED)
    # the rubric, row by row, with the zone each row reads
    rows = [
        ('30%', 'Research and context', ['Sources you read, products you compared, people you asked. Zone: RESEARCH.', 'Thin here is the most common way to lose marks.']),
        ('30%', 'Ethical and social impact', ['The mediation brief, drawn: the relation, the data, the bias register, the guardrails.', 'Zone: THE MEDIATION. Names, not adjectives.']),
        ('20%', 'Communication and poster', ['One sentence a stranger can read from three metres; one image of the moment.', 'The whole poster: hierarchy, not decoration.']),
        ('10%', 'Video', ['3 to 5 minutes: how it works, for someone who has never seen it. A QR code in the strip.', 'Storyboard on the next slide.']),
        ('10%', 'Team and process', ['Who did what; which tools; what the model made and what you chose.', 'The process strip, and the process note.']),
    ]
    for i, (pct, head, lines) in enumerate(rows):
        y = 34 + i * 100
        c.text(500, y + 32, pct, size=34, color=ORANGE)
        c.text(600, y + 14, head.upper(), size=18, color=INK)
        _lines(c, 600, y + 44, lines, size=16, color=MUTED, lh=25)
        if i < len(rows) - 1:
            c.rect(500, y + 84, 1160, 1, LINE)
    c.text(w - 20, 548, 'A0 is 841 × 1189 mm: three metres away it is one sentence and one picture; one metre away it is the research and the mediation', size=16, color=MUTED, anchor='end')
    return c.finish(name)


# ───────────────────────── 6 · the video, in six shots ─────────────────────────
def w11_storyboard(name='w11-storyboard', w=1680, h=560):
    c = Canvas(w, h)
    c.text(20, 44, 'THE VIDEO · 3 TO 5 MINUTES · SIX SHOTS', size=18, color=ORANGE)
    shots = [
        ('0:00', 'The person, the moment', ['Who, where, doing what,', 'before your product exists.']),
        ('0:30', 'What goes wrong now', ['The gap the product fills.', 'Show it; do not say it.']),
        ('1:00', 'The decision', ['What the model decides for', 'this person, from what data.']),
        ('2:00', 'What they see', ['The screen, the voice, the', 'object. The prototype, live.']),
        ('2:45', 'When it is wrong', ['The false yes, the false no;', 'how the person says no.']),
        ('3:30', 'What it does to them', ['The relation. The guardrail.', 'The team, the tools, the end.']),
    ]
    pw_, ph_, gap, x0, y0 = 250, 150, 28, 15, 90
    for i, (t, head, lines) in enumerate(shots):
        x = x0 + i * (pw_ + gap)
        c.rect(x, y0, pw_, ph_, fill=PAPER, stroke=INK, width=2)
        cx, cy = x + pw_ / 2, y0 + ph_ / 2
        if i == 0:
            c.circle(cx, cy - 22, 22, fill=WHITE, stroke=INK, width=3); c.rect(cx - 26, cy + 4, 52, 50, fill=WHITE, stroke=INK, width=3)
        elif i == 1:
            c.circle(cx - 40, cy, 22, fill=WHITE, stroke=INK, width=3)
            c.line(cx + 10, cy - 30, cx + 60, cy + 30, ORANGE, 5); c.line(cx + 60, cy - 30, cx + 10, cy + 30, ORANGE, 5)
        elif i == 2:
            c.rect(cx - 90, cy - 16, 50, 32, fill=WHITE, stroke=INK, width=2); c.text(cx - 65, cy + 6, 'data', size=14, color=INK, anchor='middle')
            _arrow(c, cx - 36, cy, cx - 4, cy, INK, 2, 8)
            c.poly([(cx + 30, cy - 34), (cx + 64, cy), (cx + 30, cy + 34), (cx - 4, cy)], fill=TINT_ORANGE, stroke=INK, width=2)
            c.text(cx + 30, cy + 5, '?', size=16, color=INK, anchor='middle')
        elif i == 3:
            c.rect(cx - 30, cy - 56, 60, 112, fill=WHITE, stroke=INK, width=3)
            for k in range(3):
                c.rect(cx - 20, cy - 40 + k * 28, 40, 18, fill=TINT_TEAL)
        elif i == 4:
            c.rect(cx - 30, cy - 56, 60, 112, fill=WHITE, stroke=INK, width=3)
            c.rect(cx - 20, cy - 40, 40, 18, fill=TINT_ORANGE)
            c.text(cx, cy + 30, 'NO', size=18, color=ORANGE, anchor='middle')
        else:
            c.circle(cx - 70, cy, 18, fill=TEAL); c.rect(cx - 22, cy - 16, 44, 32, fill=ORANGE); c.circle(cx + 70, cy, 18, fill=VIOLET)
            c.line(cx - 52, cy, cx - 24, cy, INK, 3); c.line(cx + 22, cy, cx + 52, cy, INK, 3)
        c.text(x, y0 + ph_ + 32, t, size=17, color=ORANGE)
        c.text(x, y0 + ph_ + 62, head, size=18, color=INK)
        _lines(c, x, y0 + ph_ + 92, lines, size=15, color=MUTED, lh=24)
    c.rect(20, 410, 1640, 2, LINE)
    c.text(20, 450, 'Shoot the decision, not the logo. Ten percent of the project mark is the video, and the rubric asks for one thing: how it works, and what it does to a person.', size=16, color=INK)
    c.text(20, 484, 'Phone footage is fine. A voice-over is fine. A model-made video is fine and must be disclosed in the strip. What is not fine: a trailer with no decision in it.', size=16, color=MUTED)
    return c.finish(name)


if __name__ == '__main__':
    for fn in (w11_belamy_chain, w11_funnel, w11_lora_mean, w11_authorship_ladder, w11_poster_anatomy, w11_storyboard):
        svg, png = fn()
        print(png, len(svg))
