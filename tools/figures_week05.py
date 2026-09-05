"""
Drawn figures for week 5 · Image machines and mediation. Every function name and every c.finish name
starts with w05_ / w05- (the generated files share one folder). Each figure explains a mechanism:
the forward process (an image destroyed by noise, step by step), the training step (learn to undo one
step), CLIP's shared space and its contrastive diagonal, the autoencoder and the latent, the whole
text-to-image machine as a node graph (the ComfyUI diagram), pushing a model off its prototype, and
Ihde's four human–technology relations with their AI versions, and Netflix's artwork choice as a learning loop.

W05_SHAPE is the 24 × 24 chair the noise sketch (w05-noise) also uses: the deck turns it into the JS array.
Numbers on the figures: DDPM (Ho, Jain & Abbeel, 2020) trained with T = 1000 steps and a linear noise
schedule; Stable Diffusion v1 works on a 64 × 64 × 4 latent of a 512 × 512 × 3 image (downsampling factor 8,
860M-weight UNet, CLIP ViT-L/14 text encoder, 50 sampling steps and guidance 7.5 by default in the
reference script); CLIP was trained on 400 million image–text pairs.
"""
from __future__ import annotations

import math
import random

from figures import Canvas, _arrow, draw_chair, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
TINT_T, TINT_V, TINT_O, TINT_P, TINT_Y = '#D3E7E8', '#E5DAEB', '#F9E5D6', '#F7E3E8', '#F8DEB1'

# ───────────────────────── the 24 × 24 chair (shared with the w05-noise sketch) ─────────────────────────
W05_SHAPE = [
    '........................',
    '........................',
    '.............#####......',
    '.............#####......',
    '................##......',
    '................##......',
    '................##......',
    '................##......',
    '................##......',
    '................##......',
    '................##......',
    '................##......',
    '.....#############......',
    '.....#############......',
    '......##........##......',
    '......##........##......',
    '......##........##......',
    '......##........##......',
    '......##........##......',
    '......##........##......',
    '......##........##......',
    '......##........##......',
    '........................',
    '........................',
]
N = 24


def _x0():
    """The clean image as values in [-1, 1]: ink is -0.85, paper is +0.9."""
    return [[-0.85 if ch == '#' else 0.9 for ch in row] for row in W05_SHAPE]


def _noise(seed=5):
    rnd = random.Random(seed)
    return [[rnd.gauss(0, 1) for _ in range(N)] for _ in range(N)]


def _mix(x0, eps, t):
    """x_t = sqrt(1 - t) · x0 + sqrt(t) · ε : signal fades out, noise fades in."""
    a, b = math.sqrt(max(0.0, 1 - t)), math.sqrt(max(0.0, t))
    return [[a * x0[r][c] + b * eps[r][c] for c in range(N)] for r in range(N)]


def _grey(v):
    g = int(round(max(0.0, min(1.0, (v + 1) / 2)) * 235 + 10))
    return f'#{g:02x}{g:02x}{g:02x}'


def _grid(c, x, y, size, img, frame=True):
    """Draw a 24 × 24 value grid as grey cells in a size × size box."""
    cell = size / N
    for r in range(N):
        for k in range(N):
            c.rect(x + k * cell, y + r * cell, cell + 0.4, cell + 0.4, fill=_grey(img[r][k]))
    if frame:
        c.rect(x, y, size, size, stroke=LINE, width=2)


# ───────────────────────── 1 · the forward process ─────────────────────────
def w05_forward(name='w05-forward', w=1680, h=560):
    c = Canvas(w, h)
    x0, eps = _x0(), _noise()
    ts = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    size, gap = 230, (w - 6 * 230) / 5
    y = 90
    c.text(0, 36, 'FORWARD: DESTROY THE IMAGE, A LITTLE NOISE AT A TIME', size=18, color=ORANGE)
    c.text(w, 36, 'DDPM, 2020: 1,000 steps, the noise growing by a fixed schedule', size=18, anchor='end')
    for i, t in enumerate(ts):
        x = i * (size + gap)
        _grid(c, x, y, size, _mix(x0, eps, t))
        c.text(x + size / 2, y + size + 30, f't = {t:.1f}', size=20, anchor='middle', color=INK)
        c.text(x + size / 2, y + size + 56, 'the image' if t == 0 else ('pure noise' if t == 1 else f'{round((1 - t) * 100)}% signal'), size=16, anchor='middle')
        if i < 5:
            _arrow(c, x + size + 8, y + size / 2 - 14, x + size + gap - 8, y + size / 2 - 14, MUTED, 3, 10)
            _arrow(c, x + size + gap - 8, y + size / 2 + 14, x + size + 8, y + size / 2 + 14, ORANGE, 3, 10)
    c.text(0, 430, 'x_t = √(1 − t) · x₀ + √t · ε', size=22, color=INK)
    c.text(480, 430, 'ε ~ gaussian noise, one number per pixel', size=20)   # its own text run: SVG collapses runs of spaces
    c.text(0, 470, 'grey arrows: forward, no learning — a rule. orange arrows: backward, one step at a time — a network learns each one.', size=18)
    c.text(0, 500, 'nothing is drawn: the picture is the noise, subtracted.', size=18)
    return c.finish(name)


# ───────────────────────── 2 · the training step ─────────────────────────
def w05_train_step(name='w05-train-step', w=1680, h=560):
    c = Canvas(w, h)
    x0, eps = _x0(), _noise(11)
    t = 0.55
    xt = _mix(x0, eps, t)
    # a crude 'prediction' of the noise: the true noise, slightly wrong
    rnd = random.Random(3)
    pred = [[eps[r][k] * 0.85 + rnd.gauss(0, 0.35) for k in range(N)] for r in range(N)]
    size, y = 200, 120
    c.text(0, 36, 'ONE TRAINING STEP · REPEATED MILLIONS OF TIMES', size=18, color=ORANGE)
    # x0
    _grid(c, 0, y, size, x0)
    c.text(size / 2, y + size + 30, 'x₀ · from the dataset', size=16, anchor='middle', color=INK)
    _arrow(c, size + 10, y + size / 2, 300, y + size / 2, INK, 3, 10)
    c.text(255, y + size / 2 - 14, 'pick t', size=16, anchor='middle', color=ORANGE)
    c.text(255, y + size / 2 + 26, 'add ε', size=16, anchor='middle', color=ORANGE)
    # xt
    _grid(c, 310, y, size, xt)
    c.text(310 + size / 2, y + size + 30, f'x_t · t = {t:.2f}', size=16, anchor='middle', color=INK)
    _arrow(c, 310 + size + 10, y + size / 2, 620, y + size / 2, INK, 3, 10)
    # the network
    c.rect(630, y - 10, 300, size + 20, fill=INK)
    c.text(780, y + 60, 'THE NETWORK', size=20, anchor='middle', color='#FFFFFF')
    c.text(780, y + 92, 'a UNet, 860M weights', size=16, anchor='middle', color='#B3B7BE')
    c.text(780, y + 134, '"which pixels', size=16, anchor='middle', color=TEAL)
    c.text(780, y + 156, 'are the noise?"', size=16, anchor='middle', color=TEAL)
    _arrow(c, 940, y + size / 2, 1030, y + size / 2, INK, 3, 10)
    # predicted noise vs true noise
    _grid(c, 1040, y, size, pred)
    c.text(1040 + size / 2, y + size + 30, 'ε* · the guess', size=16, anchor='middle', color=INK)
    c.text(1300, y + size / 2 + 8, 'compare', size=18, anchor='middle', color=ORANGE)
    _arrow(c, 1252, y + size / 2 - 12, 1340, y + size / 2 - 12, ORANGE, 3, 10)
    _arrow(c, 1340, y + size / 2 + 12, 1252, y + size / 2 + 12, ORANGE, 3, 10)
    _grid(c, 1360, y, size, eps)
    c.text(1360 + size / 2, y + size + 30, 'ε · the noise we added', size=16, anchor='middle', color=INK)
    # the loop back
    c.line(1460, y + size + 70, 1460, y + size + 120, ORANGE, 3, cap='butt')
    c.line(1460, y + size + 120, 780, y + size + 120, ORANGE, 3, cap='butt')
    _arrow(c, 780, y + size + 120, 780, y + size + 30, ORANGE, 3, 10)
    c.text(1120, y + size + 112, 'wrong guess → nudge every weight a little → again', size=18, anchor='middle', color=INK)
    c.text(0, 510, 'No labels, no captions needed: the noise we added is the answer key. Machine B, week 3 — the perceptron loop, on pixels.', size=18)
    c.text(0, 540, 'After training, the network can undo one step of noise on any image it never saw. Sampling runs that backwards, 1,000 times, from pure noise.', size=18)
    return c.finish(name)


# ───────────────────────── 3 · CLIP: two encoders, one space ─────────────────────────
def _icon(c, kind, cx, cy, s=22, color=INK):
    """Tiny glyphs: chair, cup, tree, car, house, cat."""
    if kind == 'chair':
        draw_chair(c, cx - s, cy - s, 2 * s, seat_h=0.45, back_h=0.6, back_angle=6, seat_w=0.62, legs=2, stroke=color, width=2)
    elif kind == 'cup':
        c.rect(cx - s * 0.6, cy - s * 0.5, s * 1.1, s * 1.0, stroke=color, width=2)
        c.circle(cx + s * 0.7, cy, s * 0.3, stroke=color, width=2)
    elif kind == 'tree':
        c.line(cx, cy + s, cx, cy - s * 0.2, color, 3)
        c.circle(cx, cy - s * 0.4, s * 0.6, stroke=color, width=2)
    elif kind == 'car':
        c.rect(cx - s, cy - s * 0.2, 2 * s, s * 0.6, stroke=color, width=2)
        c.rect(cx - s * 0.5, cy - s * 0.6, s, s * 0.4, stroke=color, width=2)
        c.circle(cx - s * 0.55, cy + s * 0.5, s * 0.22, fill=color)
        c.circle(cx + s * 0.55, cy + s * 0.5, s * 0.22, fill=color)
    elif kind == 'house':
        c.rect(cx - s * 0.7, cy - s * 0.1, s * 1.4, s * 1.0, stroke=color, width=2)
        c.poly([(cx - s * 0.85, cy - s * 0.1), (cx, cy - s * 0.9), (cx + s * 0.85, cy - s * 0.1)], stroke=color, width=2)
    elif kind == 'cat':
        c.circle(cx, cy - s * 0.3, s * 0.45, stroke=color, width=2)
        c.poly([(cx - s * 0.4, cy - s * 0.55), (cx - s * 0.3, cy - s * 0.95), (cx - s * 0.05, cy - s * 0.7)], fill=color)
        c.poly([(cx + s * 0.4, cy - s * 0.55), (cx + s * 0.3, cy - s * 0.95), (cx + s * 0.05, cy - s * 0.7)], fill=color)
        c.circle(cx + s * 0.1, cy + s * 0.45, s * 0.5, stroke=color, width=2)


CLIP_PAIRS = ['chair', 'cup', 'tree', 'car', 'house', 'cat']


def w05_clip_space(name='w05-clip-space', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 36, 'CLIP, 2021 · TWO ENCODERS, ONE SPACE', size=18, color=ORANGE)
    c.text(w, 36, 'trained on 400 million image–caption pairs from the internet', size=18, anchor='end')
    # encoders
    c.rect(0, 90, 220, 90, fill=PAPER, stroke=INK, width=2)
    c.text(110, 128, 'TEXT ENCODER', size=16, anchor='middle', color=INK)
    c.text(110, 156, '"a wooden chair"', size=15, anchor='middle')
    c.rect(0, 220, 220, 90, fill=PAPER, stroke=INK, width=2)
    c.text(110, 258, 'IMAGE ENCODER', size=16, anchor='middle', color=INK)
    _icon(c, 'chair', 110, 290, 16)
    _arrow(c, 226, 135, 300, 200, INK, 3, 10)
    _arrow(c, 226, 265, 300, 220, INK, 3, 10)
    c.text(0, 346, 'each → a list of numbers,', size=15)
    c.text(0, 368, 'a point in one space', size=15)
    # the shared space
    sx, sy, sw, sh = 310, 80, 640, 400
    c.rect(sx, sy, sw, sh, fill='#FFFFFF', stroke=LINE, width=2)
    c.text(sx + 12, sy + 24, 'ONE SPACE · nearby means "goes together"', size=15, color=INK)
    spots = {'chair': (400, 300), 'cup': (540, 150), 'tree': (780, 130), 'car': (800, 400), 'house': (660, 290), 'cat': (480, 430)}
    for k, (px, py) in spots.items():
        c.circle(px - 22, py, 6, fill=ORANGE)
        c.text(px - 12, py + 6, f'"{k}"', size=16, color=ORANGE)
        _icon(c, k, px + 78, py + 8, 14, color=INK)
    c.text(sx + sw - 12, sy + sh - 12, 'the word and its picture land together; strangers land apart', size=14, anchor='end')
    # the contrastive matrix
    mx, my, cell = 1030, 90, 56
    n = len(CLIP_PAIRS)
    c.text(mx, 60, 'THE TRAINING TABLE · match the pairs', size=16, color=INK)
    for i, k in enumerate(CLIP_PAIRS):
        _icon(c, k, mx - 34, my + i * cell + cell / 2, 12)
        c.text(mx + i * cell + cell / 2, my + n * cell + 26, f'"{k}"', size=13, anchor='middle', color=INK)
        for j in range(n):
            on = i == j
            c.rect(mx + j * cell, my + i * cell, cell - 4, cell - 4, fill=ORANGE if on else TINT_T)
            c.text(mx + j * cell + cell / 2 - 2, my + i * cell + cell / 2 + 6, '↑' if on else '↓', size=18, anchor='middle', color=INK if on else MUTED)
    c.text(mx, my + n * cell + 60, 'pull every real pair together (the diagonal),', size=15)
    c.text(mx, my + n * cell + 82, 'push every wrong pair apart. Nobody labels a "chair":', size=15)
    c.text(mx, my + n * cell + 104, 'the caption is the label. Machine B, from company.', size=15)
    c.text(0, 410, 'A prompt is a point here.', size=16, color=INK)
    c.text(0, 432, 'The image model is steered', size=16, color=INK)
    c.text(0, 454, 'towards pictures whose point', size=16, color=INK)
    c.text(0, 476, 'is near it: "a chair" pulls', size=16, color=INK)
    c.text(0, 498, 'the chairs.', size=16, color=INK)
    c.text(0, 540, 'Radford et al., 2021. Week 4\'s embeddings, with pictures in the same space.', size=15)
    return c.finish(name)


# ───────────────────────── 4 · the autoencoder and the latent ─────────────────────────
def w05_autoencoder(name='w05-autoencoder', w=1680, h=560):
    c = Canvas(w, h)
    x0 = _x0()
    c.text(0, 36, 'AN AUTOENCODER · SQUEEZE, THEN REBUILD', size=18, color=ORANGE)
    c.text(w, 36, 'Stable Diffusion v1: a 512 × 512 image becomes a 64 × 64 grid with four numbers per cell', size=18, anchor='end')
    big, y = 280, 90
    # left: the image
    _grid(c, 0, y, big, x0)
    c.text(0, y + big + 28, '512 × 512 × 3 = 786,432 numbers', size=16, color=INK)
    # encoder funnel
    c.poly([(290, y), (540, y + 100), (540, y + 180), (290, y + big)], fill=TINT_T, stroke=INK, width=2)
    c.text(415, y + 135, 'ENCODER', size=18, anchor='middle', color=INK)
    c.text(415, y + 160, 'a network', size=14, anchor='middle')
    # the latent: an 8 x 8 block picture in violet
    lx, ly, ls = 580, y + 80, 120
    cell = ls / 8
    for r in range(8):
        for k in range(8):
            vals = [x0[r * 3 + a][k * 3 + b] for a in range(3) for b in range(3)]
            v = sum(vals) / 9
            g = int(round((v + 1) / 2 * 200))
            c.rect(lx + k * cell, ly + r * cell, cell + 0.4, cell + 0.4, fill=f'#{max(0, g - 60):02x}{max(0, g - 100):02x}{g:02x}')
    c.rect(lx, ly, ls, ls, stroke=VIOLET, width=3)
    c.text(lx + ls / 2, ly - 20, 'THE LATENT', size=16, anchor='middle', color=VIOLET)
    c.text(lx + ls / 2, ly + ls + 26, '64 × 64 × 4 = 16,384 numbers', size=16, anchor='middle', color=INK)
    c.text(lx + ls / 2, ly + ls + 48, '48 × fewer', size=16, anchor='middle', color=ORANGE)
    # decoder funnel
    c.poly([(740, y + 100), (990, y), (990, y + big), (740, y + 180)], fill=TINT_T, stroke=INK, width=2)
    c.text(865, y + 135, 'DECODER', size=18, anchor='middle', color=INK)
    c.text(865, y + 160, 'a network', size=14, anchor='middle')
    # right: the rebuilt image, slightly soft
    rnd = random.Random(21)
    soft = [[x0[r][k] * 0.92 + rnd.gauss(0, 0.06) for k in range(N)] for r in range(N)]
    _grid(c, 1000, y, big, soft)
    c.text(1000 + big / 2, y + big + 28, 'rebuilt: nearly the same', size=16, anchor='middle', color=INK)
    # notes on the right
    c.text(1310, y + 20, 'TRAINED WITHOUT LABELS', size=16, color=ORANGE)
    c.text(1310, y + 50, 'The only task: rebuild the input.', size=15, color=INK)
    c.text(1310, y + 72, 'To pass through the bottleneck the', size=15)
    c.text(1310, y + 94, 'network must keep what matters', size=15)
    c.text(1310, y + 116, 'and drop what does not.', size=15)
    c.text(1310, y + 160, 'THE LATENT IS NOT A SMALL PICTURE', size=16, color=VIOLET)
    c.text(1310, y + 190, 'Four numbers per cell, and no one', size=15)
    c.text(1310, y + 212, 'named them. The violet block is only', size=15)
    c.text(1310, y + 234, 'a drawing to help.', size=15)
    c.text(1310, y + 278, 'DIFFUSION RUNS HERE', size=16, color=ORANGE)
    c.text(1310, y + 308, 'Noise and denoise 16,384 numbers,', size=15)
    c.text(1310, y + 330, 'not 786,432; decode once at the end.', size=15)
    c.text(0, 500, 'Rombach, Blattmann, Lorenz, Esser & Ommer, "High-Resolution Image Synthesis with Latent Diffusion Models", CVPR 2022 — the paper behind Stable Diffusion.', size=15)
    c.text(0, 526, 'The autoencoder here is a VAE (variational autoencoder): the same squeeze, with the bottleneck kept smooth so that nearby latents decode to nearby pictures.', size=15)
    return c.finish(name)


# ───────────────────────── 5 · the whole machine as a node graph ─────────────────────────
def _node(c, x, y, w, h, title, lines, fill='#FFFFFF', stroke=INK, title_color=INK, dashed=False):
    if dashed:
        # a dashed frame: short segments
        n = 14
        for i in range(n):
            f0, f1 = i / n, (i + 0.55) / n
            c.line(x + w * f0, y, x + w * f1, y, stroke, 2, cap='butt')
            c.line(x + w * f0, y + h, x + w * f1, y + h, stroke, 2, cap='butt')
        m = max(2, round(n * h / w))
        for i in range(m):
            f0, f1 = i / m, (i + 0.55) / m
            c.line(x, y + h * f0, x, y + h * f1, stroke, 2, cap='butt')
            c.line(x + w, y + h * f0, x + w, y + h * f1, stroke, 2, cap='butt')
        c.rect(x + 1, y + 1, w - 2, h - 2, fill=fill)
    else:
        c.rect(x, y, w, h, fill=fill, stroke=stroke, width=2)
    c.text(x + 12, y + 26, title, size=15, color=title_color)
    for i, ln in enumerate(lines):
        c.text(x + 12, y + 50 + i * 20, ln, size=14, color=INK if i == 0 else MUTED)


def w05_pipeline(name='w05-pipeline', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'THE WHOLE MACHINE · EVERY BOX IS A NODE IN COMFYUI', size=18, color=ORANGE)
    c.text(w, 30, 'solid: the model (machine B) · orange: the rules you set (machine A) · dashed: the optional handles', size=16, anchor='end')
    # row 1: prompt → CLIP → UNet
    _node(c, 0, 70, 250, 100, 'PROMPT · a rule', ['"a chair, studio photo,', 'plain white background"'], fill=TINT_O, title_color=ORANGE)
    _node(c, 300, 70, 250, 100, 'CLIP TEXT ENCODER', ['77 tokens → 77 points', 'week 4, with pictures'], fill=PAPER)
    _arrow(c, 254, 120, 296, 120, INK, 3, 10)
    # noise + seed
    _node(c, 0, 210, 250, 100, 'NOISE · seed 2112', ['a 64 × 64 × 4 grid of', 'random numbers'], fill=TINT_O, title_color=ORANGE)
    # UNet
    ux, uy, uw, uh = 620, 60, 330, 250
    c.rect(ux, uy, uw, uh, fill=INK)
    c.text(ux + 16, uy + 30, 'UNET · THE DENOISER', size=16, color='#FFFFFF')
    c.text(ux + 16, uy + 58, '860M weights, learned', size=14, color='#B3B7BE')
    c.text(ux + 16, uy + 96, 'in: the noisy latent, t,', size=14, color=TEAL)
    c.text(ux + 16, uy + 116, 'the prompt\'s points', size=14, color=TEAL)
    c.text(ux + 16, uy + 150, 'out: "this is the noise"', size=14, color=TEAL)
    c.text(ux + 16, uy + 196, '× 50 steps · guidance 7.5', size=15, color=ORANGE)
    c.text(ux + 16, uy + 220, 'two more rules you set', size=13, color='#B3B7BE')
    # loop arrow on the UNet
    c.line(ux + uw, uy + 180, ux + uw + 40, uy + 180, ORANGE, 3, cap='butt')
    c.line(ux + uw + 40, uy + 180, ux + uw + 40, uy + 100, ORANGE, 3, cap='butt')
    _arrow(c, ux + uw + 40, uy + 100, ux + uw + 4, uy + 100, ORANGE, 3, 10)
    c.text(ux + uw + 52, uy + 146, 'again', size=14, color=ORANGE)
    _arrow(c, 554, 120, ux - 4, 120, INK, 3, 10)
    _arrow(c, 254, 260, ux - 4, 260, INK, 3, 10)
    c.text(430, 250, 'the latent, x_t', size=14, anchor='middle')
    # decoder → image
    _node(c, 1070, 110, 230, 100, 'VAE DECODER', ['64 × 64 × 4 → 512 × 512', 'once, at the end'], fill=PAPER)
    _arrow(c, ux + uw + 40 + 4, 160, 1066, 160, INK, 3, 10)
    c.rect(1360, 70, 200, 180, fill='#FFFFFF', stroke=INK, width=2)
    draw_chair(c, 1400, 90, 120, seat_h=0.45, back_h=0.6, back_angle=8, seat_w=0.62, legs=4, width=3)
    c.text(1460, 236, 'THE IMAGE', size=14, anchor='middle', color=INK)
    _arrow(c, 1304, 160, 1356, 160, INK, 3, 10)
    # optional handles (dashed)
    _node(c, 0, 370, 250, 100, 'REFERENCE IMAGE', ['→ VAE encoder → noised', 'start the walk from here'], fill=TINT_V, stroke=VIOLET, title_color=VIOLET, dashed=True)
    _arrow(c, 125, 366, 125, 316, VIOLET, 3, 10)
    c.text(140, 345, 'image-to-image: replaces the pure noise', size=13, color=VIOLET)
    _node(c, 330, 370, 250, 100, 'SKETCH · POSE · EDGES', ['→ ControlNet: a copy of the', 'UNet that reads your drawing'], fill=TINT_V, stroke=VIOLET, title_color=VIOLET, dashed=True)
    _arrow(c, 590, 420, ux + 60, uy + uh + 4, VIOLET, 3, 10)
    c.text(596, 452, 'a rule laid over the model', size=13, color=VIOLET)
    _node(c, 1010, 400, 250, 100, 'LORA · a style', ['a small set of extra weights', 'learned from your 20 images'], fill=TINT_V, stroke=VIOLET, title_color=VIOLET, dashed=True)
    _arrow(c, 1010, 430, ux + uw - 40, uy + uh + 4, VIOLET, 3, 10)
    c.text(1280, 430, 'examples, added', size=13, color=VIOLET)
    c.text(1280, 450, 'to the examples', size=13, color=VIOLET)
    # legend row
    c.text(0, 520, 'Text → points (CLIP) · noise → less noise, fifty times, steered by the points (UNet, in the latent) · latent → pixels (VAE). Everything else is a knob you turn.', size=15)
    c.text(0, 546, 'Numbers are Stable Diffusion v1\'s defaults (2022). Flux and Qwen-Image, on PolyU GenAI, keep the shape and change the parts: a transformer where the UNet is, a bigger text encoder.', size=15)
    return c.finish(name)


# ───────────────────────── 6 · pushing a model off its prototype ─────────────────────────
def _bell(x, mu, sd):
    return math.exp(-0.5 * ((x - mu) / sd) ** 2)


def w05_push(name='w05-push', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'THE MODEL\'S CHAIRS · A DISTRIBUTION WITH A MIDDLE', size=18, color=ORANGE)
    x0, x1, base = 80, 1600, 360
    # axis
    c.line(x0, base, x1, base, INK, 3, cap='butt')
    c.text(x0, base + 28, 'TYPICAL · the middle of the examples', size=15, color=INK)
    c.text(x1, base + 28, 'THE EDGE · where its examples ran out', size=15, anchor='end', color=INK)
    # base curve (the model) and the LoRA curve
    mu, sd = 480, 170
    pts = [(x, base - 260 * _bell(x, mu, sd)) for x in range(x0, x1 + 1, 8)]
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        c.line(ax, ay, bx, by, INK, 4)
    mu2, sd2 = 1100, 150
    pts2 = [(x, base - 200 * _bell(x, mu2, sd2)) for x in range(x0, x1 + 1, 8)]
    for (ax, ay), (bx, by) in zip(pts2, pts2[1:]):
        c.line(ax, ay, bx, by, VIOLET, 3)
    c.text(mu2 + 20, base - 250, 'after a LoRA on your twenty chairs:', size=15, anchor='middle', color=VIOLET)
    c.text(mu2 + 20, base - 228, 'a new middle, learned from your examples', size=15, anchor='middle', color=VIOLET)
    # chairs along the axis, getting stranger
    rnd = random.Random(2112)
    for i, x in enumerate(range(200, 1560, 170)):
        k = i / 7
        draw_chair(c, x - 40, base - 120 - 0 * k, 80, seat_h=0.45 + 0.1 * k, back_h=0.6 - 0.45 * k, back_angle=6 + 40 * k,
                   seat_w=0.62 - 0.25 * k, legs=[4, 4, 4, 3, 2, 2, 2, 2][i], leg_splay=0.18 * k, stroke=INK if k < 0.5 else MUTED, width=2)
    # the prompt: a window on the base curve
    c.rect(mu - 140, base - 290, 280, 290, fill=None, stroke=ORANGE, width=3)
    c.text(mu, base - 304, 'THE PROMPT selects a region', size=15, anchor='middle', color=ORANGE)
    c.text(mu, base + 58, '"a chair" → this window;', size=13, anchor='middle', color=ORANGE)
    c.text(mu, base + 78, '"barely a chair" → a little to the right, rarely further', size=13, anchor='middle', color=ORANGE)
    # a reference: an arrow from a point
    rx = 780
    _arrow(c, rx, base - 300, rx, base - 90, TEAL, 4, 12)
    c.text(rx, base - 314, 'A REFERENCE starts the walk here', size=15, anchor='middle', color=TEAL)
    c.text(rx + 30, base + 58, 'a reference drifts back towards the middle as it denoises', size=13, color=TEAL)
    # controlnet: fixed shape
    cx = 1440
    c.text(cx, base - 314, 'CONTROLNET fixes the shape', size=15, anchor='middle', color=INK)
    c.text(cx, base - 292, 'your line, its filling', size=13, anchor='middle')
    draw_chair(c, cx - 50, base - 270, 100, seat_h=0.5, back_h=0.4, back_angle=50, seat_w=0.4, legs=2, leg_splay=0.2, stroke=INK, width=3)
    # bottom notes
    c.text(0, 480, 'Prompt: cheap, weak, pulls back to the middle (week 1\'s edge chair). Reference: starts elsewhere, still drifts. ControlNet: the geometry is yours, the surface is its middle.', size=15)
    c.text(0, 506, 'LoRA: the middle itself moves — because you gave it new examples. Four handles, from write-the-rule to show-the-examples. A drawing, not data.', size=15)
    return c.finish(name)


# ───────────────────────── 7 · Ihde's four relations, and their AI versions ─────────────────────────
def _you(c, x, y, r=22):
    c.circle(x, y, r, fill=TEAL)
    c.text(x, y + 6, 'you', size=14, anchor='middle', color=INK)


def _tech(c, x, y, s=44, color=ORANGE):
    c.rect(x - s / 2, y - s / 2, s, s, fill=color)
    c.text(x, y + 6, 'tech', size=13, anchor='middle', color=INK)


def _world(c, x, y, r=30, faint=False):
    c.circle(x, y, r, fill='#E5DAEB' if faint else VIOLET)
    c.text(x, y + 6, 'world', size=14, anchor='middle', color=MUTED if faint else '#FFFFFF')


def w05_relations(name='w05-relations', w=1680, h=560):
    c = Canvas(w, h)
    cols = [
        ('EMBODIMENT', '(you – tech) → world', 'you act and see through it; it withdraws',
         ['Ihde: glasses · a phone call · a microscope'], ['AI: Generative Fill · autocomplete', 'a spell-checker · noise cancelling']),
        ('HERMENEUTIC', 'you → (tech – world)', 'you read the world off it',
         ['Ihde: a thermometer · an MRI scan', 'a metal detector'], ['AI: the feed · an AI summary', 'the poster Netflix chose for you']),
        ('ALTERITY', 'you → tech (world)', 'you face it as a quasi-other',
         ['Ihde: an ATM · a robot', 'operating a machine'], ['AI: a chatbot · an assistant', 'Sophia']),
        ('BACKGROUND', 'you (tech / world)', 'it shapes the room; you never notice it',
         ['Ihde: the fridge hum · heating', 'notification sounds'], ['AI: a spam filter · a ranking', 'the default the model picked']),
    ]
    cw = 400
    for i, (title, schema, gloss, ihde, ai) in enumerate(cols):
        x = i * (cw + 26)
        c.rect(x, 20, cw, 520, fill=PAPER)
        c.text(x + 20, 56, title, size=18, color=ORANGE)
        c.text(x + 20, 86, schema, size=17, color=INK)
        c.text(x + 20, 112, gloss, size=14)
        cy = 210
        if i == 0:
            c.rect(x + 40, cy - 45, 190, 90, stroke=INK, width=2)
            _you(c, x + 90, cy); _tech(c, x + 180, cy)
            _arrow(c, x + 236, cy, x + 300, cy, INK, 3, 10)
            _world(c, x + 340, cy)
        elif i == 1:
            _you(c, x + 60, cy)
            _arrow(c, x + 88, cy, x + 150, cy, INK, 3, 10)
            c.rect(x + 160, cy - 45, 210, 90, stroke=INK, width=2)
            _tech(c, x + 215, cy); _world(c, x + 320, cy)
        elif i == 2:
            _you(c, x + 60, cy)
            _arrow(c, x + 88, cy, x + 170, cy, INK, 3, 10)
            _tech(c, x + 210, cy, 56)
            _world(c, x + 330, cy, faint=True)
        else:
            c.circle(x + 200, cy, 90, fill='#E5DAEB')
            _tech(c, x + 130, cy - 40, 30, color='#EBAC83')
            c.text(x + 265, cy + 50, 'world', size=13, anchor='middle', color=MUTED)
            _you(c, x + 200, cy + 6)
        for j, ln in enumerate(ihde):
            c.text(x + 20, 320 + j * 22, ln, size=14, color=INK)
        for j, ln in enumerate(ai):
            c.text(x + 20, 390 + j * 22, ln, size=14, color=VIOLET)
        c.text(x + 20, 470, ['designed as a tool: it must vanish', 'designed as a display: it must be read', 'designed as a face: it must be trusted', 'designed as a setting: it is never seen'][i], size=13)
        c.text(x + 20, 492, ['the risk: you forget it decides', 'the risk: you mistake it for the world', 'the risk: you mistake it for a person', 'the risk: nobody is accountable'][i], size=13, color=ORANGE)
    return c.finish(name)


# ───────────────────────── 8 · Netflix: one title, several artworks, one choice per viewer ─────────────────────────
def _frame(c, x, y, w, h, kind, label, color=INK):
    """A small abstract 'artwork': two heads (a couple), one head (a face) or a horizon (a scene). Drawn, not a poster."""
    c.rect(x, y, w, h, fill='#FFFFFF', stroke=color, width=2)
    if kind == 'couple':
        c.circle(x + w * 0.36, y + h * 0.42, h * 0.17, fill=color)
        c.circle(x + w * 0.64, y + h * 0.42, h * 0.17, fill=color)
        c.line(x + w * 0.2, y + h * 0.84, x + w * 0.8, y + h * 0.84, color, 4, cap='butt')
    elif kind == 'face':
        c.circle(x + w * 0.5, y + h * 0.4, h * 0.22, fill=color)
        c.line(x + w * 0.3, y + h * 0.84, x + w * 0.7, y + h * 0.84, color, 4, cap='butt')
    else:
        c.line(x + w * 0.1, y + h * 0.62, x + w * 0.9, y + h * 0.62, color, 2)
        c.circle(x + w * 0.72, y + h * 0.34, h * 0.12, stroke=color, width=2)
    if label:
        c.text(x, y + h + 20, label, size=13, color=INK)   # left-aligned: wider than the frame, must not clip at x = 0


def w05_netflix(name='w05-netflix', w=800, h=720):
    """Artwork personalization as a mechanism: a family of images → a model → one choice per viewer → the click teaches it."""
    c = Canvas(w, h)
    c.text(0, 30, 'ONE TITLE · SEVERAL ARTWORKS · ONE CHOICE PER VIEWER', size=16, color=ORANGE)
    # the family the designer made
    c.text(0, 76, 'THE FAMILY', size=15, color=INK)
    c.text(0, 98, 'the designer makes several', size=13)
    fw, fh = 120, 72
    mx, my, mw, mh = 290, 170, 230, 200
    for i, (kind, label) in enumerate([('couple', 'artwork A · the couple'), ('face', 'artwork B · the comedian'), ('scene', 'artwork C · the scene')]):
        y = 120 + i * 120
        _frame(c, 0, y, fw, fh, kind, label)
        _arrow(c, fw + 8, y + fh / 2, mx - 6, my + mh / 2, MUTED, 2, 8)
    # the model
    c.rect(mx, my, mw, mh, fill=INK)
    c.text(mx + mw / 2, my + 34, 'THE MODEL', size=16, anchor='middle', color='#FFFFFF')
    c.text(mx + mw / 2, my + 58, 'a contextual bandit', size=13, anchor='middle', color='#B3B7BE')
    c.text(mx + mw / 2, my + 96, 'in: what you watched', size=14, anchor='middle', color=TEAL)
    c.text(mx + mw / 2, my + 120, 'out: which artwork to show', size=14, anchor='middle', color=TEAL)
    c.text(mx + mw / 2, my + 164, 'learns from every click', size=14, anchor='middle', color=ORANGE)
    # two viewers, two choices
    vx = 600
    for i, (who, kind, saw) in enumerate([('watches romances', 'couple', 'sees artwork A'), ('watches comedies', 'face', 'sees artwork B')]):
        y = 150 + i * 150
        c.text(vx, y - 34, f'VIEWER {i + 1}', size=13, color=INK)
        c.text(vx, y - 14, who, size=13)
        _frame(c, vx, y, fw, fh, kind, saw)
        _arrow(c, mx + mw + 6, my + mh / 2, vx - 6, y + fh / 2, INK, 3, 10)
    # the click goes back into the model: the loop
    c.line(vx + fw / 2, 300 + fh + 34, vx + fw / 2, 450, ORANGE, 3, cap='butt')
    c.line(vx + fw / 2, 450, mx + mw / 2, 450, ORANGE, 3, cap='butt')
    _arrow(c, mx + mw / 2, 450, mx + mw / 2, my + mh + 4, ORANGE, 3, 10)
    c.text((vx + mx + mw) / 2 + 20, 474, 'the click: the reward it learns from', size=14, anchor='middle', color=ORANGE)
    # the reading
    c.text(0, 530, 'WHICH RELATION?', size=15, color=INK)
    c.text(0, 556, 'hermeneutic: you read the catalogue off the picture it chose', size=14, color=VIOLET)
    c.text(0, 578, 'seductive: hidden and weak — you never see the other artworks', size=14, color=ORANGE)
    c.text(0, 620, "THE DESIGNER'S JOB", size=15, color=INK)
    c.text(0, 646, 'not one poster: a family of images and a rule for choosing,', size=14)
    c.text(0, 668, 'and never the choice itself. Is it the same film for two people?', size=14)
    c.text(0, 706, "Netflix Tech Blog, 7 December 2017. Frames drawn here, not Netflix's artwork.", size=13)
    return c.finish(name)
