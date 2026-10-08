"""Course-owned sound diagrams, adapted from the PR 3 Week 6 illustrations.

All waves, spectra, scores and transition values are computed teaching examples,
not recordings, model outputs or a transcription of the Illiac Suite.
Provenance: deck/assets/week06-sources.md. Titles belong to the parent slide.
"""
from __future__ import annotations

import math
import random

from deckgen.core import pil_font
from deckgen.figures import Canvas, INK, ORANGE, MUTED, LINE, TEAL

__all__ = ['w06_waveform', 'w06_spectrogram_how', 'w06_midi',
           'w06_grid_score', 'w06_generate_test', 'w06_two_roads', 'w06_sound_spec',
           'w06_written_score', 'w06_strudel_pattern']

WHITE = '#FFFFFF'
PAPER = '#F4F4F2'
PALE_TEAL = '#E9F3F4'
PALE_ORANGE = '#FCF2EA'
DARK_TEAL = '#246E70'


def _label(c, x, cy, text, size=28, color=INK, anchor='start', mono=False):
    # Canvas uses a baseline: center the visible glyphs with the actual PIL font.
    font = pil_font('monomed' if mono else 'semibold', round(c.s(size)))
    top, bottom = font.getbbox(text)[1::2]
    baseline = cy + (font.getmetrics()[0] - (top + bottom) / 2) / c.s(1)
    c.text(x, baseline, text, size=size, color=color, anchor=anchor,
           mono=mono, weight=600)
    c.svg[-1] = c.svg[-1].replace('<text ', f'<text data-cy="{cy}" ', 1)


def _arrow(c, x1, y1, x2, y2, color=INK, width=4, head=14):
    c.line(x1, y1, x2, y2, color, width)
    angle = math.atan2(y2 - y1, x2 - x1)
    for offset in (-0.48, 0.48):
        a = angle + math.pi + offset
        c.line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), color, width)


def _node(c, x, y, w, h, lines, fill=PAPER, title_size=28):
    """Tagged bounds make the course's padding checks independent of slide layout."""
    c.svg.append(f'<g data-node="true" data-x="{x}" data-y="{y}" '
                 f'data-w="{w}" data-h="{h}">')
    c.rect(x, y, w, h, fill=fill, stroke=LINE, width=2)
    for i, line in enumerate(lines):
        _label(c, x + w / 2, y + h / 2 + (i - (len(lines) - 1) / 2) * 39,
               line, size=title_size if i == 0 else 26, anchor='middle')
    c.svg.append('</g>')


def _tone(t, f=220.0, harmonics=(1.0, 0.5, 0.3, 0.2)):
    return sum(a * math.sin(2 * math.pi * f * (k + 1) * t)
               for k, a in enumerate(harmonics)) / sum(harmonics)


def _gray(value):
    """Relative magnitude, not perceptual loudness; dark means larger magnitude."""
    value = max(0.0, min(1.0, value))
    return '#%02X%02X%02X' % tuple(round(a + (b - a) * value)
                                    for a, b in zip((244, 244, 242), (0, 11, 28)))


def _wave(c, x, y, w, h, span=0.04):
    mid = y + h / 2
    c.line(x, mid, x + w, mid, LINE, 2)
    points = [(x + i * w / 520, mid - _tone(i / 520 * span) * h * 0.42)
              for i in range(521)]
    for a, b in zip(points, points[1:]):
        c.line(*a, *b, INK, 2.5)


def w06_waveform(name='w06-waveform', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    _label(c, 40, 35, 'Continuous waveform: 40 ms', 30)
    _label(c, 1110, 35, 'Sampled waveform: 3 ms', 30)
    c.rect(40, 85, 950, 290, fill=PAPER, stroke=LINE, width=2)
    _wave(c, 55, 105, 920, 250)
    _label(c, 65, 108, 'positive amplitude', 22, MUTED)
    _label(c, 65, 350, 'negative amplitude', 22, MUTED)
    for k in range(5):
        _label(c, 55 + k * 230, 404, f'{k * 10} ms', 24,
               anchor='start' if k == 0 else 'end' if k == 4 else 'middle')
    _arrow(c, 1008, 230, 1090, 230, ORANGE)
    c.rect(1110, 85, 530, 290, fill=PAPER, stroke=LINE, width=2)
    mid, span, rate = 230, 0.003, 44100
    c.line(1130, mid, 1620, mid, LINE, 2)
    # The sample interval is half-open: 133 actual dots in this 3 ms segment.
    count = len(range(math.ceil(rate * span)))
    for i in range(count):
        x = 1130 + 490 * (i / rate) / span
        y = mid - _tone(i / rate) * 105
        c.line(x, mid, x, y, TEAL, 1.5)
        c.circle(x, y, 2.5, fill=INK)
    _label(c, 1375, 404, f'{count} samples at 44,100 samples/s', 26, anchor='middle')
    _label(c, 40, 454, '220 Hz fundamental + harmonics: about nine cycles in 40 ms.', 28)
    _label(c, 40, 507, 'Vertical axis = signal amplitude, not perceptual loudness.', 30)
    return c.finish(name)


def _spec_amp(col, row, cols, rows):
    """Synthetic magnitude on a log-frequency axis: a rising/falling harmonic tone."""
    f_row = 50 * (8000 / 50) ** (row / (rows - 1))
    u = col / (cols - 1)
    f0 = 180 * 2 ** (1.6 * math.sin(math.pi * u) ** 1.2)
    magnitude = sum(a * math.exp(-(abs(math.log(f_row / (f0 * k))) / 0.06) ** 2)
                    for k, a in ((1, 1.0), (2, 0.55), (3, 0.35), (4, 0.2)))
    return min(1.0, magnitude + 0.06)


def _mini_spec(c, x, y, w, h):
    cols, rows = 64, 40
    for col in range(cols):
        for row in range(rows):
            c.rect(x + col * w / cols, y + h - (row + 1) * h / rows,
                   w / cols, h / rows, fill=_gray(_spec_amp(col, row, cols, rows)))
    c.rect(x, y, w, h, stroke=LINE, width=2)


def w06_spectrogram_how(name='w06-spectrogram-how', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    for x, text in ((40, '1. Window the wave'), (610, '2. Fourier transform'),
                    (1180, '3. Stack magnitudes')):
        _label(c, x, 35, text, 30)
    c.rect(40, 85, 460, 275, fill=PAPER, stroke=LINE, width=2)
    _wave(c, 55, 100, 430, 240, span=0.02)
    c.rect(200, 98, 140, 249, stroke=ORANGE, width=3)
    _arrow(c, 520, 220, 590, 220)
    c.rect(610, 85, 460, 275, fill=PAPER, stroke=LINE, width=2)
    base = 324
    c.line(630, base, 1050, base, MUTED, 2)
    for i, magnitude in enumerate((1.0, 0.5, 0.3, 0.2)):
        x = 670 + i * 110
        c.rect(x - 12, base - magnitude * 180, 24, magnitude * 180, fill=INK)
        _label(c, x, base - magnitude * 180 - 21, str(220 * (i + 1)), 22,
               anchor='middle')
    _arrow(c, 1090, 220, 1160, 220)
    _mini_spec(c, 1180, 85, 460, 275)
    _label(c, 40, 405, 'Short, overlapping windows', 28)
    _label(c, 610, 405, 'Frequency (Hz) across', 28)
    _label(c, 1180, 405, 'Time across; frequency up', 28)
    _label(c, 40, 453, 'Each window has its own spectrum.', 26)
    _label(c, 610, 453, 'Bar height = magnitude', 26)
    _label(c, 1180, 453, 'Dark = larger magnitude', 26)
    _label(c, 40, 516, 'Separate illustrative examples. Magnitude omits phase; it is not perceptual loudness.', 28)
    return c.finish(name)


MIDI_NOTES = [(60, 0, 1, 96), (62, 1, 1, 80), (64, 2, 2, 110),
              (67, 4, 1, 70), (65, 5, 1, 60), (64, 6, 2, 100),
              (62, 8, 1, 84), (60, 9, 3, 120), (67, 12, 1, 50),
              (69, 13, 1, 64), (72, 14, 2, 116)]


def w06_midi(name='w06-midi', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    rows = [72, 71, 69, 67, 65, 64, 62, 60]
    names = ['C5 / 72', 'B4 / 71', 'A4 / 69', 'G4 / 67',
             'F4 / 65', 'E4 / 64', 'D4 / 62', 'C4 / 60']
    x0, y0, pw, rh = 155, 55, 885, 42
    for i, label in enumerate(names):
        y = y0 + i * rh
        c.rect(x0, y, pw, rh, fill=PAPER if i % 2 else WHITE)
        _label(c, x0 - 18, y + rh / 2, label, 24, anchor='end')
    for beat in range(17):
        x = x0 + beat * pw / 16
        c.line(x, y0, x, y0 + rh * 8, MUTED if beat % 4 == 0 else LINE, 2)
        if beat % 4 == 0 and beat < 16:
            _label(c, x + 8, 419, f'bar {beat // 4 + 1}', 24)
    for pitch, onset, length, velocity in MIDI_NOTES:
        c.rect(x0 + onset * pw / 16 + 2, y0 + rows.index(pitch) * rh + 7,
               length * pw / 16 - 4, rh - 14, fill=_gray(0.25 + 0.75 * velocity / 127))
    _node(c, 1130, 55, 510, 336,
          ['ONE NOTE EVENT', 'Pitch: 64 (E4)', 'Note on: beat 2, velocity 110',
           'Note off: beat 4', 'Duration follows from timing'], PALE_TEAL)
    _label(c, 40, 472, 'MIDI carries events, not sound. A synthesiser turns the events into audio.', 30)
    _label(c, 40, 522, 'Velocity is a performance parameter; its effect depends on the instrument.', 28)
    return c.finish(name)


GRID_ROWS = ['kick', 'snare', 'hat', 'bass C2', 'C4', 'E4']
GRID_SEED = {0: [0, 4, 8, 12], 1: [4, 12], 2: list(range(0, 16, 2)),
             3: [0, 7, 10], 4: [0, 3, 6, 11], 5: [2, 9, 14]}


def w06_grid_score(name='w06-grid-score', w=800, h=684):
    c = Canvas(w, h, bg=WHITE)
    x0, y0, cell = 140, 85, 39
    _label(c, x0 + 5.5 * cell, 42, 'playhead', 24, anchor='middle')
    for row, label in enumerate(GRID_ROWS):
        _label(c, x0 - 16, y0 + (row + 0.5) * cell, label, 24, anchor='end')
        for step in range(16):
            c.rect(x0 + step * cell + 2, y0 + row * cell + 2, cell - 4, cell - 4,
                   fill=(ORANGE if row < 3 else TEAL) if step in GRID_SEED[row] else PAPER,
                   stroke=LINE, width=1)
    c.rect(x0 + 5 * cell, y0 - 8, cell, 6 * cell + 16, stroke=INK, width=3)
    for beat in range(4):
        _label(c, x0 + beat * 4 * cell, 356, f'beat {beat + 1}', 24)
    _arrow(c, x0, 395, x0 + 16 * cell, 395)
    _label(c, 400, 436, 'One bar = 16 steps; read, then repeat.', 28, anchor='middle')
    _node(c, 35, 484, 730, 162,
          ['120 BPM: one beat = 0.5 s', 'Four steps per beat: one step = 0.125 s',
           '16 steps = 2 s (one bar in 4/4)'], PALE_ORANGE)
    return c.finish(name)


TRANSITIONS = ((0.5, 0.3, 0.2), (0.3, 0.4, 0.3), (0.2, 0.3, 0.5))

WRITTEN_SEED = [[1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 0, 1]]


def w06_written_score(name='w06-written-score', w=1000, h=600):
    """The same initial notes and subdivisions as the live lecture sequencer."""
    c = Canvas(w, h, bg=WHITE)
    _label(c, 40, 38, 'A written score: four sine voices, eight steps', 30)
    for step in range(8):
        _label(c, 145 + step * 100, 105, str(step + 1), 26, anchor='middle')
    for row, pitch in enumerate(('C4', 'E4', 'G4', 'B4')):
        _label(c, 77, 161 + row * 75, pitch, 28, anchor='end')
        for step, active in enumerate(WRITTEN_SEED[row]):
            c.rect(100 + step * 100, 130 + row * 75, 90, 62,
                   fill=DARK_TEAL if active else PALE_TEAL)
            c.svg[-1] = c.svg[-1].replace('<polygon ',
                f'<polygon data-row="{row}" data-step="{step}" data-active="{active}" ', 1)
    _node(c, 40, 450, 920, 120,
          ['100 BPM: two steps per beat; one step = 0.3 s',
           'Eight steps = 2.4 s (four beats); read, then repeat.'], PALE_ORANGE)
    return c.finish(name)


def w06_strudel_pattern(name='w06-strudel-pattern', w=1000, h=600):
    c = Canvas(w, h, bg=WHITE)
    _label(c, 40, 40, 'One cycle: four evenly spaced note events', 30)
    for i, note in enumerate(('C4', 'E4', 'G4', 'B4')):
        _node(c, 40 + i * 240, 145, 200, 155, [note, 'sine'], PALE_TEAL, 36)
    _arrow(c, 40, 355, 960, 355)
    _label(c, 500, 403, 'Time moves left to right; the cycle repeats.', 30, anchor='middle')
    _node(c, 40, 470, 920, 100,
          ['The Easel template controls tempo and Play / Stop.'], PALE_ORANGE)
    return c.finish(name)


def w06_generate_test(name='w06-generate-test', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    _label(c, 40, 35, 'MACHINE A: random proposals + explicit rules', 30)
    _label(c, 1180, 35, 'A handwritten table', 30)
    _node(c, 40, 100, 280, 130, ['PROPOSE', 'random pitch'], PALE_ORANGE)
    _node(c, 410, 100, 310, 130, ['TEST RULES', 'range / allowed leap'])
    _node(c, 810, 100, 280, 130, ['KEEP', 'append next note'], PALE_TEAL)
    _arrow(c, 330, 165, 400, 165)
    _arrow(c, 730, 165, 800, 165)
    _label(c, 765, 80, 'pass', 24, anchor='middle')
    c.line(565, 240, 565, 302, ORANGE, 4)
    c.line(565, 302, 180, 302, ORANGE, 4)
    _arrow(c, 180, 302, 180, 240, ORANGE)
    _label(c, 375, 338, 'fail: discard and propose again', 26, anchor='middle')
    rng = random.Random(1957)
    pitches = [0, 2, 4, 5, 4, 2, 3, 1, 0]
    for i, pitch in enumerate(pitches):
        x, y = 70 + i * 115, 455 - pitch * 12
        if i:
            c.line(x - 115, 455 - pitches[i - 1] * 12, x, y, INK, 2)
        c.circle(x, y, 7, fill=INK)
        if rng.random() < 0.6:
            _label(c, x, 385, 'x', 24, MUTED, anchor='middle')
    _label(c, 40, 492, 'Illustrative melody; x = rejected proposal', 26)
    labels = ['C', 'D', 'E']
    tx, ty, cell = 1290, 155, 100
    _label(c, 1440, 86, 'next pitch', 26, anchor='middle')
    for i, label in enumerate(labels):
        _label(c, tx + (i + 0.5) * cell, 122, label, 26, anchor='middle')
        _label(c, tx - 34, ty + (i + 0.5) * cell, label, 26, anchor='middle')
        for j, probability in enumerate(TRANSITIONS[i]):
            c.rect(tx + j * cell, ty + i * cell, cell, cell,
                   fill=PALE_TEAL, stroke=WHITE, width=3)
            _label(c, tx + (j + 0.5) * cell, ty + (i + 0.5) * cell,
                   f'{int(probability * 100)}%', 28, anchor='middle')
    _label(c, 1190, 492, 'Current pitch selects a row.', 26)
    _label(c, 40, 535, 'Illustrative Markov probabilities are designed, not learned: chance still follows a rule.', 28)
    return c.finish(name)


def w06_two_roads(name='w06-two-roads', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    _label(c, 40, 33, 'Historic Riffusion v1 (2022): a documented magnitude-spectrogram route', 30)
    boxes = [(40, 330, ['DIFFUSION', 'text + noise']),
             (450, 340, ['MAGNITUDE PICTURE', 'generated spectrogram']),
             (870, 380, ['PHASE RECONSTRUCTION', 'Griffin-Lim + inversion']),
             (1330, 300, ['AUDIO', 'waveform'])]
    for x, width, lines in boxes:
        _node(c, x, 78, width, 128, lines, PALE_ORANGE,
              title_size=26 if x == 870 else 28)
    for start, end in ((380, 440), (800, 860), (1260, 1320)):
        _arrow(c, start, 142, end, 142)
    _label(c, 40, 248, 'Magnitude alone is not enough: phase must be estimated before reconstructing audio.', 28)
    _label(c, 40, 306, 'MusicGen (2023): a documented audio-codec-token route', 30)
    boxes = [(40, 330, ['CODEC TOKENS', 'EnCodec audio codes']),
             (450, 340, ['PREDICT TOKENS', 'learned token predictor']),
             (870, 380, ['CODEC DECODE', 'tokens to waveform']),
             (1330, 300, ['AUDIO', 'waveform'])]
    for x, width, lines in boxes:
        _node(c, x, 352, width, 128, lines, PALE_TEAL)
    for start, end in ((380, 440), (800, 860), (1260, 1320)):
        _arrow(c, start, 416, end, 416)
    _label(c, 40, 528, 'Training audio is codec-encoded; generation predicts tokens. No claim about Suno internals.', 28)
    return c.finish(name)


def w06_sound_spec(name='w06-sound-spec', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    _label(c, 40, 35, 'Illustrative brief: a shared-bike lock opens', 30)
    _node(c, 40, 95, 780, 305,
          ['EXPLICIT CONSTRAINTS', '3 seconds; 120 BPM',
           'Two rising notes, then one chord', 'No voice; stop cleanly at the end',
           'Deliverable: one 44.1 kHz WAV'], PALE_ORANGE)
    _node(c, 860, 95, 780, 305,
          ['INTERPRETED QUALITIES', 'Light, outdoors, a small win',
           'Marimba + soft bell', 'Like a bicycle bell, not a car horn',
           'Not a slot machine or notification ping'], PALE_TEAL)
    _label(c, 40, 451, 'Purpose: let the rider recognise the unlock without looking at the screen.', 30)
    _label(c, 40, 507, 'A sequencer can enforce timing. A model interprets qualities. Check the actual audio.', 28)
    return c.finish(name)
