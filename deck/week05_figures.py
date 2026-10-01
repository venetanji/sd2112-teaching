"""Week 5 diagrams: model roles, latent generation and a human-directed tool loop."""
from __future__ import annotations

import base64
import math
import random
from pathlib import Path

from PIL import Image, ImageOps
from deckgen.figures import Canvas, INK, TEAL, ORANGE, VIOLET, MUTED, LINE
from figures import draw_chair

PAPER = '#F4F4F2'
PALE_TEAL = '#E9F3F4'
PALE_VIOLET = '#F2ECF5'
PALE_ORANGE = '#FCF2EA'
WHITE = '#FFFFFF'
DARK_TEAL = '#246E70'


def _arrow(c, x1, y1, x2, y2, color=INK, width=5, head=17):
    c.line(x1, y1, x2, y2, color, width)
    angle = math.atan2(y2 - y1, x2 - x1)
    for offset in (-0.48, 0.48):
        a = angle + math.pi + offset
        c.line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), color, width)


def _label(c, x, y, text, size=30, color=INK, mono=False):
    c.text(x, y, text, size=size, color=color, anchor='middle', mono=mono, weight=700)


def _node(c, x, y, w, h, title, detail='', fill=PAPER, accent=LINE):
    c.rect(x, y, w, h, fill=fill, stroke=accent, width=3)
    color = WHITE if fill == INK else INK
    _label(c, x + w / 2, y + h / 2 - (8 if detail else -10), title, 32, color)
    if detail:
        c.text(x + w / 2, y + h / 2 + 35, detail, size=27,
               color='#D3E7E8' if fill == INK else color, mono=False, anchor='middle')


def _latent_tile(c, x, y, noisy, w=230, h=150):
    """Symbolic data, not miniature pictures or actual intermediate model states."""
    c.rect(x, y, w, h, fill='#1D303B', stroke=TEAL, width=3)
    rng = random.Random(31)
    clean = ('#27505E', '#4B8991', TEAL, '#78CFCC')
    noise = ('#34404D', '#607180', '#8B879E', VIOLET, ORANGE)
    dx, dy = (w - 32) / 7, (h - 30) / 5
    for row in range(5):
        for col in range(7):
            color = rng.choice(noise) if noisy else clean[(col // 2 + row) % len(clean)]
            c.rect(x + 16 + col * dx, y + 15 + row * dy, dx - 4, dy - 4, fill=color)


def _lantern_photo(c, x, y, w, h):
    """Use the real course example in both raster and vector diagram outputs."""
    path = Path(__file__).resolve().parent / 'assets/week05-lantern-easel.jpg'
    with Image.open(path) as source:
        tile = ImageOps.fit(source.convert('RGBA'), (round(c.s(w)), round(c.s(h))))
        c.im.paste(tile, (round(c.s(x)), round(c.s(y))))
    encoded = base64.b64encode(path.read_bytes()).decode('ascii')
    c.svg.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" '
                 f'href="data:image/jpeg;base64,{encoded}" preserveAspectRatio="xMidYMid slice"/>')


def gan_adversaries(name='w05-gan-adversaries', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    _node(c, 25, 215, 255, 145, 'RANDOM INPUT', 'sample noise')
    _node(c, 360, 215, 285, 145, 'GENERATOR', 'makes an image', PALE_ORANGE, ORANGE)
    _node(c, 725, 215, 260, 145, 'CANDIDATE', 'generated image', PALE_ORANGE, ORANGE)
    _node(c, 1065, 215, 320, 145, 'DISCRIMINATOR', 'real or generated?', INK, INK)
    _node(c, 1065, 15, 320, 115, 'REAL EXAMPLES', 'training images', PALE_TEAL, TEAL)
    _label(c, 1540, 270, 'TRAINING', 28, DARK_TEAL)
    _label(c, 1540, 315, 'SIGNAL', 32)
    for start, stop in ((280, 360), (645, 725), (985, 1065), (1385, 1440)):
        _arrow(c, start, 285, stop, 285, ORANGE)
    _arrow(c, 1225, 130, 1225, 215, DARK_TEAL)
    c.line(1510, 350, 1510, 440, DARK_TEAL, 5)
    c.line(1510, 440, 1225, 440, DARK_TEAL, 5)
    _arrow(c, 1225, 440, 1225, 360, DARK_TEAL)
    c.line(1225, 440, 502, 440, ORANGE, 5)
    _arrow(c, 502, 440, 502, 360, ORANGE)
    _label(c, 855, 506, 'Both learn: distinguish examples; make harder-to-distinguish images.', 32)
    return c.finish(name)


def clip_shared_space(name='w05-clip-shared-space', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    _node(c, 25, 45, 345, 145, 'CAPTION', 'a chair with curved back', PALE_VIOLET, VIOLET)
    c.rect(25, 275, 345, 200, fill=PAPER)
    draw_chair(c, 125, 290, 160, seat_h=0.42, back_h=0.6,
               back_angle=12, seat_w=0.7, legs=4, stroke=INK, width=6)
    _node(c, 450, 45, 300, 145, 'TEXT ENCODER', 'caption to vector', PALE_VIOLET, VIOLET)
    _node(c, 450, 305, 300, 145, 'IMAGE ENCODER', 'picture to vector', PALE_TEAL, TEAL)
    _arrow(c, 370, 118, 450, 118, VIOLET)
    _arrow(c, 370, 378, 450, 378, DARK_TEAL)
    c.rect(860, 15, 790, 470, fill=PAPER)
    _label(c, 1255, 65, 'SHARED EMBEDDING SPACE', 34)
    _arrow(c, 750, 118, 930, 230, VIOLET)
    _arrow(c, 750, 378, 970, 290, DARK_TEAL)
    c.circle(1030, 230, 17, fill=VIOLET)
    c.rect(1070, 255, 34, 34, fill=DARK_TEAL)
    c.line(1047, 245, 1070, 255, MUTED, 3)
    _label(c, 1060, 192, 'matching pair', 28)
    c.circle(1360, 350, 17, fill=VIOLET)
    c.rect(1400, 310, 34, 34, fill=DARK_TEAL)
    c.line(1377, 345, 1400, 327, MUTED, 3)
    c.circle(1470, 175, 17, fill=VIOLET)
    _label(c, 1470, 225, 'different caption', 26)
    _label(c, 1255, 436, 'mismatched pairs move apart', 30)
    _label(c, 840, 540, 'Similarity is not synthesis. A matching vector is not a picture.', 34)
    return c.finish(name)


def text_conditioning(name='w05-text-conditioning', w=1680, h=560):
    """Two inputs meet at iterative updates; the decoder follows the final latent."""
    c = Canvas(w, h, bg=WHITE)
    _node(c, 25, 25, 350, 130, 'PROMPT', 'paper lantern in a garden', PALE_VIOLET, VIOLET)
    _node(c, 455, 25, 320, 130, 'TEXT ENCODER', 'words to features', PALE_VIOLET, VIOLET)
    _arrow(c, 375, 90, 455, 90, VIOLET)
    c.line(775, 90, 865, 90, VIOLET, 5)
    _arrow(c, 865, 90, 865, 220, VIOLET)
    _label(c, 1010, 145, 'TEXT FEATURES', 28, VIOLET)
    _latent_tile(c, 25, 235, True, 250, 170)
    _label(c, 150, 450, 'INITIAL LATENT', 28)
    _node(c, 385, 220, 490, 200, 'DENOISING MODEL', 'text-conditioned latent updates', INK, INK)
    _arrow(c, 275, 320, 385, 320, DARK_TEAL)
    _arrow(c, 875, 320, 1020, 320, DARK_TEAL)
    _label(c, 950, 274, 'final z', 28, DARK_TEAL)
    c.poly([(1020, 260), (1300, 220), (1300, 420), (1020, 380)],
           fill=PALE_TEAL, stroke=TEAL, width=4)
    _label(c, 1160, 311, 'VAE', 34)
    _label(c, 1160, 352, 'DECODER', 32)
    _arrow(c, 1300, 320, 1380, 320, DARK_TEAL)
    _lantern_photo(c, 1380, 215, 270, 220)
    _label(c, 1515, 477, 'OUTPUT IMAGE', 28)
    c.line(750, 420, 750, 505, DARK_TEAL, 5)
    c.line(750, 505, 455, 505, DARK_TEAL, 5)
    _arrow(c, 455, 505, 455, 420, DARK_TEAL)
    _label(c, 601, 549, 'REPEAT', 28, DARK_TEAL)
    return c.finish(name)


def vae_latent(name='w05-vae-latent', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    c.rect(25, 140, 235, 260, fill=PAPER)
    _label(c, 142, 118, 'INPUT IMAGE x', 28)
    draw_chair(c, 75, 180, 145, seat_h=0.42, back_h=0.6,
               back_angle=10, seat_w=0.68, legs=4, stroke=INK, width=6)
    c.poly([(320, 110), (590, 205), (590, 335), (320, 430)],
           fill=PALE_ORANGE, stroke=ORANGE, width=4)
    _label(c, 438, 263, 'ENCODER', 34)
    _label(c, 438, 308, 'q(z|x)', 28, mono=True)
    _label(c, 790, 90, 'DISTRIBUTION', 28, VIOLET)
    _label(c, 790, 137, 'mean + log variance', 28)
    c.line(665, 157, 910, 157, VIOLET, 3)
    _label(c, 790, 217, 'SAMPLE', 28, VIOLET)
    c.circle(790, 290, 60, fill=VIOLET)
    _label(c, 790, 306, 'z', 44, WHITE)
    c.poly([(990, 205), (1260, 110), (1260, 430), (990, 335)],
           fill=PALE_TEAL, stroke=TEAL, width=4)
    _label(c, 1142, 263, 'DECODER', 34)
    _label(c, 1142, 308, 'p(x|z)', 28, mono=True)
    c.rect(1370, 140, 285, 260, fill=PAPER)
    _label(c, 1512, 118, 'RECONSTRUCTION', 28)
    draw_chair(c, 1435, 180, 145, seat_h=0.42, back_h=0.6,
               back_angle=13, seat_w=0.65, legs=4, stroke=INK, width=6)
    _label(c, 1512, 440, 'x-hat', 28, mono=True)
    for x1, x2 in ((260, 320), (590, 730), (850, 990), (1260, 1370)):
        _arrow(c, x1, 290, x2, 290, DARK_TEAL)
    _label(c, 840, 532, 'Reconstruction is approximate. Compact data is not a smaller photograph.', 32)
    return c.finish(name)


def diffusion_training(name='w05-diffusion-training', w=1680, h=560):
    """Classic noise-prediction training: make a target, compare, update weights."""
    c = Canvas(w, h, bg=WHITE)
    _label(c, 840, 36, 'PREPARE A TRAINING PAIR', 30, DARK_TEAL)
    c.rect(25, 65, 215, 135, fill=PAPER)
    draw_chair(c, 78, 73, 110, seat_h=0.42, back_h=0.6,
               back_angle=10, seat_w=0.68, legs=4, stroke=INK, width=5)
    _label(c, 132, 241, 'EXAMPLE IMAGE', 26)
    c.poly([(325, 65), (555, 95), (555, 170), (325, 200)],
           fill=PALE_ORANGE, stroke=ORANGE, width=4)
    _label(c, 440, 135, 'VAE ENCODER', 28)
    _latent_tile(c, 635, 65, False, 230, 135)
    _label(c, 750, 241, 'CLEAN LATENT  z0', 26)
    _node(c, 950, 65, 255, 135, 'ADD NOISE', 'save the target', PALE_ORANGE, ORANGE)
    _latent_tile(c, 1310, 65, True, 290, 135)
    _label(c, 1455, 241, 'NOISY LATENT  zt', 26)
    for a, b in ((240, 325), (555, 635), (865, 950), (1205, 1310)):
        _arrow(c, a, 132, b, 132, DARK_TEAL)
    c.line(1455, 260, 1455, 300, DARK_TEAL, 5)
    c.line(1455, 300, 185, 300, DARK_TEAL, 5)
    _arrow(c, 185, 300, 185, 355, DARK_TEAL)
    _node(c, 25, 355, 320, 125, 'DENOISER', 'latent + noise level', INK, INK)
    _node(c, 450, 355, 310, 125, 'PREDICT NOISE', 'model output', PALE_TEAL, TEAL)
    _node(c, 885, 355, 295, 125, 'COMPARE', 'prediction vs target', PALE_ORANGE, ORANGE)
    _node(c, 1305, 355, 350, 125, 'UPDATE WEIGHTS', 'reduce prediction error', PALE_ORANGE, ORANGE)
    for a, b in ((345, 450), (760, 885), (1180, 1305)):
        _arrow(c, a, 418, b, 418, ORANGE)
    _label(c, 1032, 333, 'KNOWN NOISE', 24, INK)
    _arrow(c, 1032, 338, 1032, 355, ORANGE, head=10)
    _label(c, 840, 546, 'Repeat across many images and noise levels. Text conditioning omitted here.', 30)
    return c.finish(name)


def diffusion_generation(name='w05-diffusion-generation', w=1680, h=560):
    c = Canvas(w, h, bg=WHITE)
    _node(c, 375, 5, 330, 100, 'TEXT FEATURES', '', PALE_VIOLET, VIOLET)
    _arrow(c, 540, 105, 540, 180, VIOLET)
    _latent_tile(c, 25, 180, True, 250, 180)
    _label(c, 150, 405, 'NEW NOISY LATENT', 26)
    _node(c, 375, 180, 330, 180, 'DENOISER', 'learned prediction', INK, INK)
    _latent_tile(c, 810, 180, False, 250, 180)
    _label(c, 935, 405, 'FINAL LATENT', 28)
    c.poly([(1150, 220), (1375, 180), (1375, 360), (1150, 320)],
           fill=PALE_TEAL, stroke=TEAL, width=4)
    _label(c, 1262, 267, 'VAE DECODER', 28)
    _lantern_photo(c, 1455, 155, 200, 225)
    _label(c, 1555, 425, 'OUTPUT IMAGE', 26)
    for a, b in ((275, 375), (705, 810), (1060, 1150), (1375, 1455)):
        _arrow(c, a, 270, b, 270, DARK_TEAL)
    c.line(758, 270, 758, 465, DARK_TEAL, 5)
    c.line(758, 465, 335, 465, DARK_TEAL, 5)
    c.line(335, 465, 335, 320, DARK_TEAL, 5)
    _arrow(c, 335, 320, 375, 320, DARK_TEAL)
    _label(c, 545, 507, 'REPEAT LATENT UPDATE', 28, DARK_TEAL)
    _label(c, 1260, 527, 'Decode after the last update.', 30)
    return c.finish(name)


def agent_image_tools(name='w05-agent-image-tools', w=1680, h=560):
    """Explicit observation return, without an invented vision-to-image tool edge."""
    c = Canvas(w, h, bg=WHITE)
    _node(c, 25, 180, 320, 165, 'YOUR INTENT', 'approve the next step')
    _node(c, 450, 180, 340, 165, 'AGENT', 'plan / call / observe', INK, INK)
    _node(c, 905, 50, 335, 150, 'VISION TOOL', 'inspect an output', PALE_TEAL, TEAL)
    _node(c, 905, 330, 335, 150, 'MEDIA TOOL', 'generate / edit', PALE_ORANGE, ORANGE)
    _lantern_photo(c, 1380, 165, 270, 225)
    _label(c, 1515, 434, 'CANDIDATE', 28)
    _arrow(c, 345, 263, 450, 263, VIOLET)
    _arrow(c, 790, 310, 905, 405, ORANGE)
    _arrow(c, 1240, 405, 1380, 315, ORANGE)
    _arrow(c, 1380, 215, 1240, 125, DARK_TEAL)
    _arrow(c, 905, 125, 790, 215, DARK_TEAL)
    _label(c, 620, 100, 'OBSERVATION', 28, DARK_TEAL)
    c.line(620, 345, 620, 485, VIOLET, 5)
    c.line(620, 485, 185, 485, VIOLET, 5)
    _arrow(c, 185, 485, 185, 345, VIOLET)
    _label(c, 410, 545, 'YOU KEEP / REVISE / REJECT', 28, VIOLET)
    return c.finish(name)
