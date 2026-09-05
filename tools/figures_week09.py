"""
Drawn figures for week 9 · Data, bias and privacy. Every function name and every c.finish name
starts with w09_ / w09- (the generated files share one folder). Each figure explains a mechanism
rather than decorating a slide:

  w09_windows            the same population, three sampling windows, three fitted rules — the model
                         knows the window, not the world (the Python twin of the w09-sample sketch)
  w09_doors              the data loop of a product and the four doors where bias enters
  w09_threshold_anatomy  two score distributions, one threshold, the two ways to be wrong — and why the
                         same threshold gives two groups different error rates
  w09_linkage            re-identification by linkage: quasi-identifiers join an "anonymised" table to a
                         public one (Sweeney, 1997 / 2000); all records fictional
  w09_register           the bias register, filled for a fictional product
"""
from __future__ import annotations

import math
import random

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
TEAL_TINT = '#D3E7E8'
ORANGE_TINT = '#FBE2D3'
GRAY_TINT = '#E9E9E6'
RED = '#D22B2B'


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


def _lines(c, x, y, lines, size=18, color=INK, lh=None, anchor='start'):
    lh = lh or round(size * 1.45)
    for i, t in enumerate(lines):
        c.text(x, y + i * lh, t, size=size, color=color, anchor=anchor)


# ───────────────────────── 1 · the window and the world ─────────────────────────
# The same population and the same fit as the w09-sample sketch: 300 people in two colours, a hidden
# curved rule, and a straight line fitted (least squares) to whatever fell inside a window.
PW, PH = 1000, 500


def _rule(x):
    return 250 + 110 * math.sin(x / 150 + 1.2)


def _population(seed=9, n=300):
    rnd = random.Random(seed)
    pts = []
    for _ in range(n):
        x = rnd.uniform(40, 520) if rnd.random() < 0.65 else rnd.uniform(40, PW - 40)
        y = rnd.uniform(40, 260) if rnd.random() < 0.65 else rnd.uniform(40, PH - 40)
        pts.append((x, y, 1 if y < _rule(x) else 0))       # 1 = teal, above the curve; 0 = orange, below
    return pts


def _fit(sample):
    """Least squares on labels ±1 with features (1, x, y): the line w0 + w1 x + w2 y = 0."""
    M = [[0.0] * 4 for _ in range(3)]
    for x, y, cl in sample:
        f = [1.0, x / PW, y / PH]
        t = 1.0 if cl else -1.0
        for i in range(3):
            for j in range(3):
                M[i][j] += f[i] * f[j]
            M[i][3] += f[i] * t
    for i in range(3):
        M[i][i] += 1e-6
    for col in range(3):
        piv = max(range(col, 3), key=lambda r: abs(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        if abs(M[col][col]) < 1e-12:
            return None
        for r in range(3):
            if r != col:
                k = M[r][col] / M[col][col]
                for j in range(col, 4):
                    M[r][j] -= k * M[col][j]
    return [M[i][3] / M[i][i] for i in range(3)]


def _predict(w, x, y):
    return 1 if w[0] + w[1] * x / PW + w[2] * y / PH > 0 else 0


def _line_ends(w):
    """Where w0 + w1 x/PW + w2 y/PH = 0 crosses the plot box."""
    pts = []
    if abs(w[2]) > 1e-9:
        for x in (0, PW):
            y = -(w[0] + w[1] * x / PW) * PH / w[2]
            if 0 <= y <= PH:
                pts.append((x, y))
    if abs(w[1]) > 1e-9:
        for y in (0, PH):
            x = -(w[0] + w[2] * y / PH) * PW / w[1]
            if 0 <= x <= PW:
                pts.append((x, y))
    return pts[:2] if len(pts) >= 2 else None


def w09_windows(name='w09-windows', w=1680, h=560):
    c = Canvas(w, h)
    pts = _population()
    windows = [((300, 150), (360, 200), 'TEAM A · the crowded corner'),
               ((780, 250), (360, 200), 'TEAM B · the far edge'),
               ((500, 250), (860, 400), 'TEAM C · nearly the whole world')]
    s = 0.54
    pw, ph = PW * s, PH * s
    for i, ((cx, cy), (ww, wh), label) in enumerate(windows):
        ox, oy = i * 570, 40
        c.rect(ox, oy, pw, ph, fill='#FFFFFF', stroke=LINE, width=2)
        # the true rule, which no model ever sees
        for x in range(40, PW - 40, 12):
            c.circle(ox + x * s, oy + _rule(x) * s, 1.2, fill='#C9C9C6')
        x0, y0, x1, y1 = cx - ww / 2, cy - wh / 2, cx + ww / 2, cy + wh / 2
        sample = [p for p in pts if x0 <= p[0] <= x1 and y0 <= p[1] <= y1]
        wgt = _fit(sample) if len(sample) >= 3 else None
        c.rect(ox + x0 * s, oy + y0 * s, ww * s, wh * s, fill='#FBF3EC', stroke=INK, width=2)
        wrong_world = 0
        for x, y, cl in pts:
            inside = x0 <= x <= x1 and y0 <= y <= y1
            col = TEAL if cl else ORANGE
            if wgt and _predict(wgt, x, y) != cl:
                wrong_world += 1
                c.circle(ox + x * s, oy + y * s, 4.2, stroke=RED, width=1.4)
            c.circle(ox + x * s, oy + y * s, 3.2 if inside else 2.4, fill=col, stroke=INK if inside else None, width=1)
        if wgt:
            ends = _line_ends(wgt)
            if ends:
                (ax, ay), (bx, by) = ends
                c.line(ox + ax * s, oy + ay * s, ox + bx * s, oy + by * s, INK, 3, cap='butt')
            wrong_win = sum(1 for p in sample if _predict(wgt, *p[:2]) != p[2])
            acc_win = 100 * (1 - wrong_win / len(sample))
            acc_world = 100 * (1 - wrong_world / len(pts))
        else:
            acc_win = acc_world = float('nan')
        c.text(ox, 352, label, size=18, color=ORANGE)
        c.text(ox, 384, f'trained on {len(sample)} people · right in the window: {acc_win:.0f} %', size=18, color=INK)
        c.text(ox, 412, f'right in the world: {acc_world:.0f} %  ({wrong_world} red rings)', size=18, color=INK)
    c.text(0, 470, '300 people, two colours (teal / orange), one hidden rule: the grey curve. Each team trained a straight line on what fell inside its window.',
           size=18, color=MUTED)
    c.text(0, 500, 'Ringed dots are the training set; a red ring is a person the line gets wrong. The model knows the window, not the world.', size=18, color=MUTED)
    return c.finish(name)


# ───────────────────────── 2 · the four doors ─────────────────────────
def w09_doors(name='w09-doors', w=1680, h=560):
    c = Canvas(w, h)
    boxes = [('THE WORLD', 'people, as they are', PAPER), ('THE DATA', 'the examples collected', TEAL_TINT),
             ('THE LABELS', 'the name of each example', TEAL_TINT), ('THE MODEL', 'an objective, a threshold', ORANGE_TINT),
             ('THE PRODUCT', 'a decision per person', ORANGE_TINT)]
    bw, bh, y = 260, 110, 170
    xs = [40 + i * 340 for i in range(5)]
    doors = [('1 · DATA BIAS', 'who is in the dataset,', 'and who is not'),
             ('2 · LABEL BIAS', 'who named the examples,', 'with which words'),
             ('3 · ALGORITHMIC BIAS', 'what the model is told to want;', 'where the line is drawn'),
             ('', '', '')]
    for i, (title, sub, fill) in enumerate(boxes):
        x = xs[i]
        c.rect(x, y, bw, bh, fill=fill, stroke=INK, width=3)
        c.text(x + bw / 2, y + 48, title, size=22, anchor='middle', color=INK)
        c.text(x + bw / 2, y + 82, sub, size=16, anchor='middle', color=MUTED)
        if i < 4:
            _arrow(c, x + bw, y + bh / 2, xs[i + 1] - 4, y + bh / 2, INK, 4)
            head, l1, l2 = doors[i]
            if head:
                mx = x + bw + 40
                c.text(mx, 62, head, size=18, color=ORANGE)
                c.text(mx, 92, l1, size=16, color=INK)
                c.text(mx, 116, l2, size=16, color=INK)
                _arrow(c, mx + 30, 128, mx + 30, y + bh / 2 - 14, ORANGE, 3, 10)
    # the loop back: what people do with the product becomes tomorrow's data
    px, dx = xs[4] + bw / 2, xs[1] + bw / 2
    c.line(px, y + bh, px, 420, INK, 4, cap='butt')
    c.line(px, 420, dx, 420, INK, 4, cap='butt')
    _arrow(c, dx, 420, dx, y + bh + 6, INK, 4)
    c.text((px + dx) / 2, 458, '4 · INTERACTION BIAS', size=18, anchor='middle', color=ORANGE)
    c.text((px + dx) / 2, 488, 'what we click, skip and accept becomes tomorrow’s examples: the feed learns from us, then we learn from the feed',
           size=16, anchor='middle', color=INK)
    c.text((px + dx) / 2, 400, 'clicks · skips · complaints · nothing at all', size=16, anchor='middle', color=MUTED)
    c.text(40, 540, 'Four doors. Every one of them is a decision somebody made, or did not make.', size=18, color=MUTED)
    return c.finish(name)


# ───────────────────────── 3 · the threshold: two ways to be wrong ─────────────────────────
def _phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def _bell(x, mu, sd):
    return math.exp(-0.5 * ((x - mu) / sd) ** 2)


def w09_threshold_anatomy(name='w09-threshold-anatomy', w=1680, h=560, t=60):
    c = Canvas(w, h)
    groups = [('GROUP 1 · the model is sure about them', 66, 36, 11), ('GROUP 2 · the model is less sure about them', 58, 42, 16)]
    for gi, (label, mu_yes, mu_no, sd) in enumerate(groups):
        ox = gi * 880
        ax0, ax1, base, top = ox + 40, ox + 760, 380, 120
        scale = (ax1 - ax0) / 100
        tx = ax0 + t * scale
        c.text(ox, 40, label, size=20, color=INK)
        # the two curves as filled shapes, and the two error areas
        for mu, col, tint, side in ((mu_no, MUTED, GRAY_TINT, 'right'), (mu_yes, TEAL, TEAL_TINT, 'left')):
            curve = [(ax0 + s * scale, base - 230 * _bell(s, mu, sd)) for s in range(0, 101)]
            c.poly([(ax0, base)] + curve + [(ax1, base)], fill=tint)
            err = [p for p in curve if (p[0] >= tx if side == 'right' else p[0] <= tx)]
            if len(err) > 1:
                c.poly([(err[0][0], base)] + err + [(err[-1][0], base)], fill=ORANGE if side == 'right' else '#2E8F90')
            for (x1, y1), (x2, y2) in zip(curve, curve[1:]):
                c.line(x1, y1, x2, y2, col, 2.5, cap='butt')
        c.line(ax0, base, ax1, base, INK, 2, cap='butt')
        c.line(tx, top - 20, tx, base + 8, ORANGE, 4, cap='butt')
        c.text(tx, top - 32, f'threshold {t}', size=18, anchor='middle', color=ORANGE)
        c.text(ax0, base + 30, 'score 0', size=16, color=MUTED)
        c.text(ax1, base + 30, '100', size=16, color=MUTED, anchor='end')
        c.text(tx - 12, base + 30, '← the product says NO', size=16, anchor='end', color=MUTED)
        c.text(tx + 12, base + 30, 'YES →', size=16, color=MUTED)
        fpr = 1 - _phi((t - mu_no) / sd)
        fnr = _phi((t - mu_yes) / sd)
        c.text(ax0, 130, 'grey: should get NO', size=16, color=MUTED)
        c.text(ax1, 130, 'teal: should get YES', size=16, color=TEAL, anchor='end')
        c.text(ox, 440, f'false YES (orange): {100 * fpr:.0f} % of the NO-people are let through', size=18, color=INK)
        c.text(ox, 470, f'false NO (dark teal): {100 * fnr:.0f} % of the YES-people are turned away', size=18, color=INK)
    c.text(0, 530, 'Same score, same threshold, same rule for everyone. The wider the curves, the more of both errors, and the two groups do not pay the same.',
           size=18, color=MUTED)
    return c.finish(name)


# ───────────────────────── 4 · re-identification by linkage ─────────────────────────
HOSPITAL = [('02139', '1961-03-14', 'F', 'asthma'), ('02139', '1958-11-02', 'M', 'fracture'), ('02140', '1975-06-30', 'F', 'migraine'),
            ('02138', '1945-07-31', 'M', 'heart disease'), ('02141', '1983-01-09', 'F', 'eczema'), ('02138', '1969-09-21', 'M', 'insomnia')]
VOTERS = [('L. Svensson', '14 Elm St', '02139', '1961-03-14', 'F'), ('T. Ho', '9 Oak Rd', '02139', '1958-11-02', 'M'),
          ('M. Rivera', '77 Pine Ave', '02140', '1975-06-30', 'F'), ('P. Okafor', '3 Bay Lane', '02138', '1945-07-31', 'M'),
          ('J. Ng', '120 Main St', '02141', '1983-01-09', 'F'), ('S. Bauer', '41 Hill St', '02138', '1969-09-21', 'M')]


def _table(c, x, y, cols, widths, rows, hl=None, size=17, rh=44):
    cx = x
    for (head, wd) in zip(cols, widths):
        c.text(cx, y, head, size=15, color=ORANGE)
        cx += wd
    c.line(x, y + 12, x + sum(widths), y + 12, INK, 2, cap='butt')
    for ri, row in enumerate(rows):
        ry = y + 24 + ri * rh
        if ri == hl:
            c.rect(x - 8, ry - 2, sum(widths) + 8, rh - 6, fill=ORANGE_TINT)
        cx = x
        for (val, wd) in zip(row, widths):
            c.text(cx, ry + 26, val, size=size, color=INK)
            cx += wd
        c.line(x, ry + rh - 6, x + sum(widths), ry + rh - 6, LINE, 1, cap='butt')


def w09_linkage(name='w09-linkage', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 34, 'HOSPITAL DISCHARGES · NAMES REMOVED · “ANONYMISED”', size=18, color=INK)
    c.text(920, 34, 'VOTER ROLL · PUBLIC, FOR SALE', size=18, color=INK)
    _table(c, 0, 80, ['ZIP', 'birth date', 'sex', 'diagnosis'], [140, 200, 90, 260], HOSPITAL, hl=3)
    _table(c, 920, 80, ['name', 'address', 'ZIP', 'birth date', 'sex'], [180, 200, 130, 190, 60], VOTERS, hl=3)
    # the join
    ry = 80 + 24 + 3 * 44 + 18
    _arrow(c, 700, ry, 906, ry, ORANGE, 4)
    _arrow(c, 906, ry, 700, ry, ORANGE, 4)
    c.text(803, ry - 22, 'same ZIP', size=15, anchor='middle', color=ORANGE)
    c.text(803, ry + 36, 'same birth date', size=15, anchor='middle', color=ORANGE)
    c.text(803, ry + 58, 'same sex', size=15, anchor='middle', color=ORANGE)
    c.text(0, 400, 'No name anywhere in the left table. The three shared columns are quasi-identifiers: harmless alone, a key together.',
           size=18, color=INK)
    c.text(0, 430, 'Sweeney, 1997: a hospital dataset for Massachusetts state employees, linked to the Cambridge voter roll, gave the governor’s records.',
           size=18, color=MUTED)
    c.text(0, 460, 'Sweeney, 2000: on the 1990 census, 87 % of Americans were unique on ZIP + birth date + sex. Golle, 2006: 63 % on the 2000 census.',
           size=18, color=MUTED)
    c.text(0, 520, 'All records above are fictional.', size=16, color=MUTED)
    return c.finish(name)


# ───────────────────────── 5 · the bias register ─────────────────────────
REGISTER_COLS = ['THE DECISION', 'THE DATA IT LEARNS FROM', 'WHO IS THIN IN THE DATA', 'THE HARM WHEN WRONG', 'THE GUARDRAIL']
REGISTER_ROWS = [
    [['dims the lamp when it', 'thinks you are tired'], ['phone use, time of day,', 'how still you sit; from', 'the beta testers'],
     ['shift workers, parents of', 'newborns, anyone who', 'reads in bed'], ['false YES: the light goes', 'off over your exam notes', 'false NO: it never helps'],
     ['never below 30 %; a physical', 'dial overrides for the', 'night; you can turn it off']],
    [['picks a colour temperature', 'for your mood'], ['the words you type into', 'the app, in English'], ['anyone writing in another', 'language; anyone who', 'does not type'],
     ['a wrong mood, every', 'evening, and no way to', 'say so'], ['a default that is not a', 'mood; a one-tap undo']],
    [['…'], ['…'], ['…'], ['…'], ['…']],
]


def w09_register(name='w09-register', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'BIAS REGISTER · TEAM NIGHTLIGHT · a bedside lamp that decides when you are tired (fictional)', size=18, color=INK)
    x0, y0, cw = 0, 70, 336
    for i, head in enumerate(REGISTER_COLS):
        c.text(x0 + i * cw + 12, y0 + 22, head, size=15, color=ORANGE)
    c.line(x0, y0 + 36, w, y0 + 36, INK, 2, cap='butt')
    rh = 138
    for ri, row in enumerate(REGISTER_ROWS):
        ry = y0 + 36 + ri * rh
        if ri == 0:
            c.rect(x0, ry, w, rh, fill=PAPER)
        for ci, cell in enumerate(row):
            _lines(c, x0 + ci * cw + 12, ry + 34, cell, size=16, color=INK if ri < 2 else MUTED, lh=26)
        c.line(x0, ry + rh, w, ry + rh, LINE, 1, cap='butt')
    for i in range(1, 5):
        c.line(x0 + i * cw, y0 + 36, x0 + i * cw, y0 + 36 + 3 * rh, LINE, 1, cap='butt')
    c.text(0, 545, 'One row per decision the model makes. Three rows minimum. The guardrail is a rule (machine A) that catches machine B when it is wrong — and says who can appeal.',
           size=16, color=MUTED)
    return c.finish(name)


if __name__ == '__main__':
    for fn in (w09_windows, w09_doors, w09_threshold_anatomy, w09_linkage, w09_register):
        svg, png = fn()
        print(png, len(svg))
