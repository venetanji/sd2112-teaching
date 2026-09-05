"""
Drawn figures for week 6 · Sound machines. Every function name and every c.finish name starts
with w06_ / w06- (the generated files share one folder). Each figure explains a mechanism:
a waveform and its samples, how a spectrogram is made, MIDI as a score of numbers, a step grid as
time, the Illiac Suite's generate-and-test loop and its Markov table, the two roads of machine B
for audio (a picture of sound, a language of sound), and the anatomy of a sound spec.
The tones drawn here are computed, not recorded: the pictures are the rules that make them.
"""
from __future__ import annotations

import math
import random

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
TINT_TEAL, TINT_VIOLET, TINT_ORANGE, TINT_YELLOW = '#D3E7E8', '#E5DAEB', '#F9E5D6', '#F8DEB1'


def _tone(t, f=220.0, harmonics=(1.0, 0.5, 0.3, 0.2)):
    """A steady tone: a fundamental and a few harmonics, amplitude in -1..1."""
    s = sum(a * math.sin(2 * math.pi * f * (k + 1) * t) for k, a in enumerate(harmonics))
    return s / sum(harmonics)


def _gray(v):
    """0..1 loudness -> a grey between paper and ink (dark = loud)."""
    v = max(0.0, min(1.0, v))
    r = round(244 - v * (244 - 0))
    g = round(244 - v * (244 - 11))
    b = round(242 - v * (242 - 28))
    return f'#{r:02X}{g:02X}{b:02X}'


# ───────────────────────── sound is pressure over time ─────────────────────────
def w06_waveform(name='w06-waveform', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'SOUND IS PRESSURE OVER TIME · A WAVEFORM IS THE DRAWING', size=18, color=ORANGE)
    # left: 40 ms of a tone
    x0, y0, pw, ph = 0, 70, 1040, 380
    c.rect(x0, y0, pw, ph, fill='#FFFFFF', stroke=LINE, width=2)
    mid = y0 + ph / 2
    c.line(x0, mid, x0 + pw, mid, LINE, 2, cap='butt')
    ms = 40.0
    pts = []
    for i in range(0, pw + 1, 2):
        t = i / pw * ms / 1000
        pts.append((x0 + i, mid - _tone(t) * ph * 0.42))
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        c.line(xa, ya, xb, yb, INK, 2.5, cap='round')
    for k in range(5):
        x = x0 + k * pw / 4
        c.line(x, y0 + ph, x, y0 + ph + 10, MUTED, 2, cap='butt')
        c.text(x, y0 + ph + 34, f'{k * 10} ms', size=16, anchor='middle' if 0 < k < 4 else ('start' if k == 0 else 'end'))
    c.text(x0 + 16, y0 + 30, 'louder ↑', size=16, color=MUTED)
    c.text(x0 + 16, y0 + ph - 14, 'quieter ↓', size=16, color=MUTED)
    c.text(x0 + pw - 16, y0 + 30, 'a 220 Hz tone with four harmonics · 40 ms · about nine cycles', size=16, anchor='end', color=MUTED)
    c.text(x0, 512, 'one cycle every 4.5 ms = 220 cycles a second = 220 Hz: the pitch is how often the wave repeats', size=18, color=INK)
    c.text(x0, 542, 'you hear from about 20 Hz to 20,000 Hz · A above middle C = 440 Hz (ISO 16, 1975)', size=18, color=MUTED)
    # right: 3 ms, sampled
    rx, rw = 1120, 560
    c.rect(rx, y0, rw, ph, fill='#FFFFFF', stroke=LINE, width=2)
    c.line(rx, mid, rx + rw, mid, LINE, 2, cap='butt')
    span = 0.003
    n = int(44100 * span)                       # 132 samples
    for i in range(n + 1):
        t = i / 44100
        x = rx + 20 + (rw - 40) * (t / span)
        y = mid - _tone(t) * ph * 0.42
        c.line(x, mid, x, y, TEAL, 1.5, cap='butt')
        c.circle(x, y, 2.6, fill=INK)
    _arrow(c, 1040 + 8, y0 + 40, rx - 8, y0 + 40, ORANGE, 3, 10)
    c.text(rx + 16, y0 + 30, 'zoom: 3 ms', size=16, color=ORANGE)
    c.text(rx + rw - 16, y0 + ph - 14, f'{n} dots', size=16, anchor='end', color=MUTED)
    c.text(rx, 512, 'a computer keeps only dots: 44,100 a second (CD)', size=18, color=INK)
    c.text(rx, 542, 'one number per dot: a second is 44,100 numbers', size=18, color=MUTED)
    return c.finish(name)


# ───────────────────────── how a spectrogram is made ─────────────────────────
def _spec_amp(col, row, cols, rows):
    """A synthetic spectrogram: a tone that rises then falls, with three harmonics; row 0 = lowest frequency.
    Frequencies on a log scale from 50 Hz to 8 kHz."""
    lo, hi = 50.0, 8000.0
    f_row = lo * (hi / lo) ** (row / (rows - 1))
    u = col / (cols - 1)
    f0 = 180 * 2 ** (1.6 * math.sin(math.pi * u) ** 1.2)           # rises to about 550 Hz and comes back
    amp = 0.0
    for k, a in ((1, 1.0), (2, 0.55), (3, 0.35), (4, 0.2)):
        fk = f0 * k
        d = abs(math.log(f_row / fk)) / 0.06
        amp += a * math.exp(-d * d)
    return min(1.0, amp + 0.06)


def w06_spectrogram_how(name='w06-spectrogram-how', w=1680, h=560):
    c = Canvas(w, h)
    for x, t in ((0, '1 · A SLICE OF THE WAVE'), (520, '2 · FOURIER: WHICH FREQUENCIES, HOW LOUD'), (1080, '3 · MANY SLICES SIDE BY SIDE: THE PICTURE')):
        c.text(x, 30, t, size=18, color=ORANGE)
    # 1 · a slice (20 ms), the window boxed
    x0, y0, pw, ph = 0, 60, 460, 300
    c.rect(x0, y0, pw, ph, fill='#FFFFFF', stroke=LINE, width=2)
    mid = y0 + ph / 2
    for i in range(0, pw + 1, 2):
        t = i / pw * 0.02
        y = mid - _tone(t, 220, (1.0, 0.55, 0.35, 0.2)) * ph * 0.4
        if i:
            c.line(x0 + i - 2, py, x0 + i, y, INK, 2.2, cap='round')
        py = y
    c.rect(x0 + 150, y0 + 8, 160, ph - 16, stroke=ORANGE, width=3)
    c.text(x0 + 230, y0 + ph + 30, 'a window of about 20 ms', size=16, anchor='middle', color=INK)
    c.text(x0, 410, 'take a short window of the sound —', size=18, color=INK)
    c.text(x0, 440, 'too short to hear a note, long enough', size=18, color=MUTED)
    c.text(x0, 470, 'to count how fast it wiggles', size=18, color=MUTED)
    _arrow(c, 470, 210, 512, 210, INK, 3, 10)
    # 2 · the spectrum of that window
    x1, bw = 520, 480
    c.rect(x1, y0, bw, ph, fill='#FFFFFF', stroke=LINE, width=2)
    base = y0 + ph - 30
    c.line(x1 + 20, base, x1 + bw - 20, base, MUTED, 2, cap='butt')
    lo, hi = 150.0, 2000.0
    for k, a in ((1, 1.0), (2, 0.55), (3, 0.35), (4, 0.2)):
        f = 220 * k
        px = x1 + 20 + (bw - 40) * math.log(f / lo) / math.log(hi / lo)
        c.rect(px - 9, base - a * 220, 18, a * 220, fill=INK if k == 1 else '#3B4451')
        c.text(px, base - a * 220 - 10, f'{f}', size=14, anchor='middle', color=MUTED)
    for f, lab in ((150, '150'), (500, '500'), (1000, '1k'), (2000, '2k Hz')):
        px = x1 + 20 + (bw - 40) * math.log(f / lo) / math.log(hi / lo)
        c.text(px, base + 22, lab, size=14, anchor='middle' if f < 2000 else 'end', color=MUTED)
    lo, hi = 50.0, 8000.0
    c.text(x1 + 20, y0 + 26, 'louder ↑', size=14, color=MUTED)
    c.text(x1, 410, 'Fourier, 1822: any wave is a sum of sines.', size=18, color=INK)
    c.text(x1, 440, 'the bars say which sines, and how loud:', size=18, color=MUTED)
    c.text(x1, 470, 'the pitch is the first bar, the timbre is the rest', size=18, color=MUTED)
    _arrow(c, 1010, 210, 1070, 210, INK, 3, 10)
    # 3 · the spectrogram: one column per slice
    x2, y2, sw, sh = 1080, 60, 500, 300
    cols, rows = 70, 44
    cw, rh = sw / cols, sh / rows
    for col in range(cols):
        for row in range(rows):
            a = _spec_amp(col, row, cols, rows)
            c.rect(x2 + col * cw, y2 + sh - (row + 1) * rh, cw + 0.6, rh + 0.6, fill=_gray(a))
    c.rect(x2, y2, sw, sh, stroke=LINE, width=2)
    hl = 24                                           # the column that panel 2 becomes
    c.rect(x2 + hl * cw - 1, y2 - 6, cw + 2, sh + 12, stroke=ORANGE, width=3)
    for f, lab in ((100, '100 Hz'), (1000, '1 kHz'), (8000, '8 kHz')):
        r = math.log(f / lo) / math.log(hi / lo)
        yy = y2 + sh - r * sh
        c.line(x2 + sw, yy, x2 + sw + 8, yy, MUTED, 2, cap='butt')
        c.text(x2 + sw + 14, yy + 5, lab, size=13, color=MUTED)
    c.text(x2, y2 + sh + 30, 'time →', size=16, color=INK)
    c.text(x2 + hl * cw + cw / 2 + 40, y2 + sh + 30, 'one slice = one column', size=14, anchor='middle', color=ORANGE)
    c.text(x2 + sw, y2 + sh + 30, 'dark = loud', size=16, anchor='end', color=MUTED)
    c.text(x2, 410, 'time across, frequency up, loudness as darkness.', size=18, color=INK)
    c.text(x2, 440, 'this one is a tone rising and falling, its harmonics', size=18, color=MUTED)
    c.text(x2, 470, 'above it: an image a model can learn from', size=18, color=MUTED)
    c.text(0, 530, 'waveform: time × loudness (two things) · spectrogram: time × frequency × loudness (three things) — the picture of sound machine B looks at', size=18, color=INK)
    return c.finish(name)


# ───────────────────────── MIDI: a score as numbers ─────────────────────────
MIDI_NOTES = [  # (pitch number, beat on, length in beats, velocity)
    (60, 0, 1, 96), (62, 1, 1, 80), (64, 2, 2, 110), (67, 4, 1, 70), (65, 5, 1, 60),
    (64, 6, 2, 100), (62, 8, 1, 84), (60, 9, 3, 120), (67, 12, 1, 50), (69, 13, 1, 64), (72, 14, 2, 116),
]
NOTE_NAMES = {60: 'C4 · 60', 62: 'D4 · 62', 64: 'E4 · 64', 65: 'F4 · 65', 67: 'G4 · 67', 69: 'A4 · 69', 71: 'B4 · 71', 72: 'C5 · 72'}


def w06_midi(name='w06-midi', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'MIDI, 1983 · A NOTE IS FOUR NUMBERS: PITCH, ONSET, DURATION, VELOCITY', size=18, color=ORANGE)
    x0, y0, pw = 120, 70, 940
    rows = [72, 71, 69, 67, 65, 64, 62, 60]
    rh, beats = 40, 16
    bw = pw / beats
    ph = rh * len(rows)
    for i, p in enumerate(rows):
        y = y0 + i * rh
        c.rect(x0, y, pw, rh, fill=PAPER if i % 2 else '#FFFFFF')
        c.text(x0 - 12, y + rh / 2 + 6, NOTE_NAMES[p], size=15, anchor='end', color=INK if p in (60, 72) else MUTED)
    for b in range(beats + 1):
        x = x0 + b * bw
        c.line(x, y0, x, y0 + ph, LINE if b % 4 else MUTED, 1.5 if b % 4 else 2, cap='butt')
        if b % 4 == 0 and b < beats:
            c.text(x + 4, y0 + ph + 22, f'bar {b // 4 + 1}', size=14, color=MUTED)
    for p, on, ln, vel in MIDI_NOTES:
        i = rows.index(p)
        x, y = x0 + on * bw, y0 + i * rh + 6
        c.rect(x + 2, y, ln * bw - 4, rh - 12, fill=_gray(0.25 + 0.75 * vel / 127))
    # annotations on one note (E4 at beat 2, two beats, velocity 110)
    i = rows.index(64)
    nx, ny = x0 + 2 * bw, y0 + i * rh
    _arrow(c, nx, ny - 40, nx, ny - 4, ORANGE, 3, 10)
    c.text(nx, ny - 48, 'ONSET: beat 2', size=14, color=ORANGE)
    c.line(nx + 2, ny + rh + 8, nx + 2 * bw - 2, ny + rh + 8, ORANGE, 3, cap='butt')
    c.text(nx + 2 * bw + 8, ny + rh + 26, 'DURATION: 2 beats', size=14, color=ORANGE)
    c.text(x0 + pw + 12, ny + rh / 2 + 5, '← VELOCITY 110', size=14, color=ORANGE)
    c.text(x0, 470, 'the piano roll: pitch up (0–127, middle C = 60), time across, darkness = how hard the key was hit', size=18, color=INK)
    c.text(x0, 500, 'nothing here is sound: it is a score, and a synthesiser plays it — change the instrument and every number stays', size=18, color=MUTED)
    c.text(x0, 530, 'a language model can write this; a sequencer can obey it exactly. The rule side of music, since 1983.', size=18, color=MUTED)
    # right: the messages
    mx, my = 1240, 70
    c.rect(mx, my, 440, 360, fill=PAPER)
    c.text(mx + 24, my + 36, 'THE WIRE, MESSAGE BY MESSAGE', size=15, color=ORANGE)
    msgs = ['note on   ch 1   60   96', 'note off  ch 1   60', 'note on   ch 1   62   80', 'note off  ch 1   62',
            'note on   ch 1   64  110', '        …', 'note off  ch 1   64', 'note on   ch 1   67   70']
    for k, m in enumerate(msgs):
        c.text(mx + 24, my + 80 + k * 32, m, size=18, color=INK if 'on' in m and '…' not in m else MUTED)
    c.text(mx + 24, my + 346, 'kind · channel · pitch · velocity', size=14, color=MUTED)
    return c.finish(name)


# ───────────────────────── a step grid is time ─────────────────────────
GRID_ROWS = ['kick', 'snare', 'hat', 'bass C2', 'C4', 'E4']
GRID_SEED = {0: [0, 4, 8, 12], 1: [4, 12], 2: [0, 2, 4, 6, 8, 10, 12, 14], 3: [0, 7, 10], 4: [0, 3, 6, 11], 5: [2, 9, 14]}


def w06_grid_score(name='w06-grid-score', w=800, h=684):
    c = Canvas(w, h)
    c.text(0, 28, 'THE GRID IS THE SCORE', size=18, color=ORANGE)
    x0, y0, cs = 110, 60, 40
    for r, lab in enumerate(GRID_ROWS):
        c.text(x0 - 12, y0 + r * cs + cs / 2 + 6, lab, size=15, anchor='end', color=INK)
        for s in range(16):
            on = s in GRID_SEED[r]
            c.rect(x0 + s * cs + 2, y0 + r * cs + 2, cs - 4, cs - 4, fill=(ORANGE if r < 3 else TEAL) if on else '#FFFFFF', stroke=LINE if not on else None, width=1.5)
    gh = 6 * cs
    c.rect(x0 + 5 * cs, y0 - 6, cs, gh + 12, stroke=INK, width=3)
    c.text(x0 + 5 * cs + cs / 2, y0 - 14, 'playhead', size=14, anchor='middle', color=INK)
    for b in range(4):
        x = x0 + b * 4 * cs
        c.line(x, y0 + gh + 6, x, y0 + gh + 18, MUTED, 2, cap='butt')
        c.text(x + 4, y0 + gh + 36, f'beat {b + 1}', size=14, color=MUTED)
    c.text(x0 + 16 * cs, y0 + gh + 36, 'step 16', size=14, anchor='end', color=MUTED)
    _arrow(c, x0, y0 + gh + 60, x0 + 16 * cs, y0 + gh + 60, INK, 3, 10)
    c.text(x0 + 8 * cs, y0 + gh + 88, 'one bar = 16 steps, read left to right, then again', size=16, anchor='middle', color=INK)
    y = 450
    c.rect(0, y, w, 220, fill=PAPER)
    lines = [('AT 120 BPM', ORANGE), ('a beat  = 60 ÷ 120 = 0.5 s', INK), ('a step  = a beat ÷ 4 = 0.125 s', INK),
             ('a bar   = 16 steps = 2 s', INK), ('the mouse changes one number: the BPM', MUTED), ('every cell is a rule: on this step, this sound', MUTED)]
    for k, (t, col) in enumerate(lines):
        c.text(24, y + 40 + k * 30, t, size=18 if k else 15, color=col)
    return c.finish(name)


# ───────────────────────── the Illiac Suite: generate and test, then a table ─────────────────────────
def w06_generate_test(name='w06-generate-test', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'EXPERIMENTS 1 – 2 · GENERATE A NOTE, TEST IT AGAINST THE RULES', size=18, color=ORANGE)
    c.text(1000, 30, 'EXPERIMENT 4 · A TABLE INSTEAD OF RULES', size=18, color=ORANGE)
    # the loop
    bx, by, bw, bh = 0, 70, 300, 80
    c.rect(bx, by, bw, bh, fill=PAPER, stroke=INK, width=3)
    c.text(bx + bw / 2, by + 34, 'PROPOSE A PITCH', size=18, anchor='middle', color=INK)
    c.text(bx + bw / 2, by + 62, 'a random number', size=15, anchor='middle', color=MUTED)
    _arrow(c, bx + bw, by + bh / 2, bx + bw + 56, by + bh / 2, INK, 3, 10)
    rx = bx + bw + 60
    c.rect(rx, by - 10, 380, 200, fill='#FFFFFF', stroke=INK, width=3)
    c.text(rx + 20, by + 24, 'TEST: THE RULES', size=18, color=INK)
    rules = ['stays inside the range?', 'no leap of a tritone?', 'no parallel fifths or octaves?', 'no more than one repeat?', 'ends on the tonic?']
    for k, r in enumerate(rules):
        c.text(rx + 20, by + 56 + k * 27, '- ' + r, size=16, color=MUTED)
    _arrow(c, rx + 380, by + 40, rx + 440, by + 40, INK, 3, 10)
    c.text(rx + 410, by + 24, 'all yes', size=14, anchor='middle', color=ORANGE)
    c.rect(rx + 444, by, 220, 80, fill=ORANGE)
    c.text(rx + 554, by + 34, 'KEEP IT', size=18, anchor='middle', color=INK)
    c.text(rx + 554, by + 62, 'next note', size=15, anchor='middle', color=INK)
    _arrow(c, rx + 190, by + 190, rx + 190, by + 228, INK, 3, 10)
    c.text(rx + 204, by + 214, 'any no', size=14, color=ORANGE)
    c.rect(rx + 60, by + 232, 260, 52, fill=PAPER, stroke=MUTED, width=2)
    c.text(rx + 190, by + 264, 'THROW IT AWAY', size=16, anchor='middle', color=MUTED)
    # back arrow from throw-away to propose
    c.line(rx + 60, by + 258, bx + bw / 2, by + 258, MUTED, 3, cap='butt')
    _arrow(c, bx + bw / 2, by + 258, bx + bw / 2, by + bh + 6, MUTED, 3, 10)
    c.text(bx + bw / 2 + 12, by + 210, 'again', size=14, color=MUTED)
    # a cantus with rejected candidates
    sx, sy = 0, 392
    c.text(sx, sy - 20, 'a melody grows one accepted note at a time · × = a proposal the rules rejected', size=16, color=INK)
    rnd = random.Random(1957)
    pitches = [0, 2, 4, 5, 4, 2, 3, 1, 0]
    for k, p in enumerate(pitches):
        x = sx + 30 + k * 100
        for j in range(rnd.choice([0, 1, 1, 2, 3])):
            c.text(x, sy + 104 - rnd.choice([1, 3, 6, 7]) * 14 + 5, '×', size=18, anchor='middle', color=MUTED)
        c.circle(x, sy + 104 - p * 14, 8, fill=INK)
        if k:
            c.line(x - 100, sy + 104 - pitches[k - 1] * 14, x, sy + 104 - p * 14, INK, 2, cap='round')
    c.text(sx, 542, 'generate and test: the rules are the design; chance only proposes.', size=18, color=MUTED)
    # experiment 4: the table
    tx, ty, cell = 1000, 70, 48
    labels = ['same', '2nd', '3rd', '4th', '5th', 'bigger']
    table = [[0.30, 0.34, 0.16, 0.10, 0.06, 0.04], [0.28, 0.36, 0.18, 0.10, 0.05, 0.03], [0.24, 0.32, 0.22, 0.12, 0.06, 0.04],
             [0.22, 0.30, 0.20, 0.14, 0.09, 0.05], [0.20, 0.28, 0.20, 0.14, 0.11, 0.07], [0.18, 0.26, 0.20, 0.14, 0.12, 0.10]]
    c.text(tx + 120 + 3 * cell, ty - 6, 'NEXT INTERVAL', size=14, anchor='middle', color=MUTED)
    for j, lab in enumerate(labels):
        c.text(tx + 120 + j * cell + cell / 2, ty + 18, lab, size=13, anchor='middle', color=MUTED)
    for i, row in enumerate(table):
        c.text(tx + 108, ty + 30 + i * cell + cell / 2 + 5, labels[i], size=13, anchor='end', color=MUTED)
        for j, p in enumerate(row):
            x, y = tx + 120 + j * cell, ty + 30 + i * cell
            c.rect(x, y, cell, cell, fill=_gray(p * 2.2), stroke='#FFFFFF', width=1)
            c.text(x + cell / 2, y + cell / 2 + 5, f'{round(p * 100)}', size=13, anchor='middle', color='#FFFFFF' if p > 0.22 else INK)
    c.text(tx, ty + 30 + 3 * cell, 'LAST', size=13, color=MUTED)
    c.text(tx, ty + 30 + 3 * cell + 18, 'INTERVAL', size=13, color=MUTED)
    c.rect(tx + 120 + 1 * cell, ty + 30 + 0 * cell, cell, cell, stroke=ORANGE, width=3)
    c.text(tx, 434, 'the next interval depends on the last one: a Markov chain', size=18, color=INK)
    c.text(tx, 462, 'simpler intervals more likely than bigger ones (Hiller & Isaacson)', size=16, color=MUTED)
    c.text(tx, 488, 'our numbers, their idea · Nake 1966 with signs · GPT with tokens', size=16, color=MUTED)
    c.text(tx, 542, 'no rule says what is wrong; the table says what is likely.', size=18, color=MUTED)
    return c.finish(name)


# ───────────────────────── machine B for audio: two roads ─────────────────────────
def _mini_wave(c, x, y, w, h, seed=3, color=INK):
    rnd = random.Random(seed)
    mid = y + h / 2
    px, py = x, mid
    for i in range(1, 41):
        nx = x + i * w / 40
        ny = mid + (rnd.random() - 0.5) * h * 0.9 * (0.4 + 0.6 * abs(math.sin(i / 5)))
        c.line(px, py, nx, ny, color, 2, cap='round')
        px, py = nx, ny


def _mini_spec(c, x, y, w, h, seed=5, noise=0.0):
    rnd = random.Random(seed)
    cols, rows = 24, 14
    cw, rh = w / cols, h / rows
    for col in range(cols):
        for row in range(rows):
            a = _spec_amp(col, row, cols, rows) * (1 - noise) + rnd.random() * noise
            c.rect(x + col * cw, y + h - (row + 1) * rh, cw + 0.5, rh + 0.5, fill=_gray(a))
    c.rect(x, y, w, h, stroke=LINE, width=1.5)


def _tokens(c, x, y, n=8, s=22, seed=9):
    rnd = random.Random(seed)
    tints = [TINT_TEAL, TINT_VIOLET, TINT_ORANGE, TINT_YELLOW]
    for i in range(n):
        c.rect(x + i * (s + 4), y, s, s, fill=rnd.choice(tints))
        c.text(x + i * (s + 4) + s / 2, y + s / 2 + 5, str(rnd.randrange(10, 99)), size=11, anchor='middle', color=INK)


def w06_two_roads(name='w06-two-roads', w=1680, h=560):
    c = Canvas(w, h)
    for y, head in ((30, 'ROAD 1 · A PICTURE OF SOUND · SPECTROGRAM DIFFUSION'), (312, 'ROAD 2 · A LANGUAGE OF SOUND · TOKENS FROM A CODEC')):
        c.text(0, y, head, size=18, color=ORANGE)
    # road 1
    y = 70
    boxes = [(0, 'SOUND', 'wave'), (280, 'SPECTROGRAM', 'spec'), (560, 'DIFFUSION', 'noise'), (880, 'SPECTROGRAM', 'spec2'), (1160, 'INVERSE FOURIER', 'txt'), (1440, 'SOUND', 'wave2')]
    for x, lab, kind in boxes:
        bw = 240
        c.rect(x, y, bw, 150, fill='#FFFFFF' if kind != 'noise' else TINT_VIOLET, stroke=INK, width=2.5)
        c.text(x + 16, y + 28, lab, size=15, color=INK)
        if kind == 'wave':
            _mini_wave(c, x + 20, y + 50, bw - 40, 80, seed=3)
        elif kind == 'wave2':
            _mini_wave(c, x + 20, y + 50, bw - 40, 80, seed=11)
        elif kind == 'spec':
            _mini_spec(c, x + 20, y + 44, bw - 40, 90, seed=5)
        elif kind == 'spec2':
            _mini_spec(c, x + 20, y + 44, bw - 40, 90, seed=6)
        elif kind == 'noise':
            _mini_spec(c, x + 20, y + 44, 90, 90, seed=7, noise=1.0)
            _arrow(c, x + 116, y + 89, x + 128, y + 89, INK, 2, 8)
            _mini_spec(c, x + 132, y + 44, 90, 90, seed=6, noise=0.15)
        else:
            c.text(x + 16, y + 74, 'the picture, played', size=15, color=MUTED)
            c.text(x + 16, y + 100, 'back as a wave', size=15, color=MUTED)
        if x < 1440:
            _arrow(c, x + bw + 4, y + 75, x + 276, y + 75, INK, 3, 10)
    c.text(560 + 120, y + 178, '"blues guitar" steers the denoising', size=14, anchor='middle', color=MUTED)
    c.text(0, 280, 'Riffusion, 15 December 2022: Stable Diffusion fine-tuned on spectrograms tagged with genres. Week 5\'s machine, pointed at a picture of sound.', size=17, color=INK)
    # road 2
    y = 340
    boxes = [(0, 'SOUND', 'wave'), (280, 'CODEC → TOKENS', 'tok'), (560, 'NEXT-TOKEN MODEL', 'lm'), (880, 'TOKENS', 'tok2'), (1160, 'CODEC → SOUND', 'txt'), (1440, 'SOUND', 'wave2')]
    for x, lab, kind in boxes:
        bw = 240
        c.rect(x, y, bw, 150, fill='#FFFFFF' if kind != 'lm' else TINT_TEAL, stroke=INK, width=2.5)
        c.text(x + 16, y + 28, lab, size=15, color=INK)
        if kind == 'wave':
            _mini_wave(c, x + 20, y + 50, bw - 40, 80, seed=3)
        elif kind == 'wave2':
            _mini_wave(c, x + 20, y + 50, bw - 40, 80, seed=13)
        elif kind == 'tok':
            _tokens(c, x + 16, y + 56, seed=9); _tokens(c, x + 16, y + 90, seed=10)
            c.text(x + 16, y + 136, 'a few pieces per frame', size=13, color=MUTED)
        elif kind == 'tok2':
            _tokens(c, x + 16, y + 56, seed=21); _tokens(c, x + 16, y + 90, seed=22)
            c.text(x + 16, y + 136, 'new pieces, same vocabulary', size=13, color=MUTED)
        elif kind == 'lm':
            c.text(x + 16, y + 68, 'week 4\'s machine:', size=15, color=INK)
            c.text(x + 16, y + 94, 'a table, a die,', size=15, color=INK)
            c.text(x + 16, y + 120, 'a temperature', size=15, color=INK)
        else:
            c.text(x + 16, y + 74, 'the decoder plays', size=15, color=MUTED)
            c.text(x + 16, y + 100, 'the pieces back', size=15, color=MUTED)
        if x < 1440:
            _arrow(c, x + bw + 4, y + 75, x + 276, y + 75, INK, 3, 10)
    c.text(0, 532, 'Jukebox (OpenAI, April 2020) · MusicLM (Google, January 2023, SoundStream tokens) · MusicGen (Meta, June 2023, EnCodec tokens) · the products of 2024–26', size=17, color=INK)
    return c.finish(name)


# ───────────────────────── the anatomy of a sound spec ─────────────────────────
SPEC_A = [('LENGTH', '3 seconds, then silence'), ('TEMPO', '120 BPM · in time with the bell'), ('STRUCTURE', 'two rising notes, then one chord, then stop'),
          ('MUST NOT', 'no voice, no words, no reverb tail'), ('DELIVERABLE', 'one WAV, 44.1 kHz, plus the spec')]
SPEC_B = [('MOOD', 'light, outdoors, a morning, a small win'), ('TIMBRE', 'a marimba and a soft bell, nothing electric'),
          ('LIKE', 'a bicycle bell, not a car horn'), ('NOT LIKE', 'a slot machine, a notification ping'), ('THE MOMENT', 'the lock clicks open: 08:10, a busy street')]


def w06_sound_spec(name='w06-sound-spec', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'A SOUND SPEC · FOR A SHARED-BIKE APP · THE MOMENT THE LOCK OPENS', size=18, color=ORANGE)
    c.text(w, 30, 'the product is made up; the headings are the point', size=16, anchor='end', color=MUTED)
    for x, head, items, tint, note in ((0, 'MACHINE A LINES · RULES A SEQUENCER OBEYS EXACTLY', SPEC_A, PAPER, 'numbers and structure: same result every time, and you can point at the line that decided'),
                                       (860, 'MACHINE B LINES · EXAMPLES A MODEL INTERPRETS', SPEC_B, TINT_VIOLET, 'words and references: the model answers from its middle; say what it must not be, too')):
        c.rect(x, 60, 820, 400, fill=tint)
        c.text(x + 28, 96, head, size=15, color=INK)
        for k, (lab, txt) in enumerate(items):
            y = 140 + k * 60
            c.text(x + 28, y, lab, size=15, color=ORANGE)
            c.text(x + 200, y, txt, size=21, color=INK, mono=False)
            c.line(x + 28, y + 20, x + 792, y + 20, LINE if tint == PAPER else '#D7C3DC', 1.5, cap='butt')
        c.text(x + 28, 440, note, size=15, color=MUTED)
    c.text(0, 500, 'PURPOSE first, always: what the sound is for, and for whom — "so the rider knows the bike is theirs, without looking down"', size=18, color=INK)
    c.text(0, 532, 'a spec is complete when a stranger, a sequencer, or a model could execute it. Week 2\'s spec, week 4\'s brief, now audible.', size=18, color=MUTED)
    return c.finish(name)


if __name__ == '__main__':
    for fn in (w06_waveform, w06_spectrogram_how, w06_midi, w06_grid_score, w06_generate_test, w06_two_roads, w06_sound_spec):
        svg, png = fn()
        print(png, len(svg))
