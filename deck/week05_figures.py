"""Week 5 diagrams: image-model lineage and a human-directed agent tool loop."""
from __future__ import annotations

import math
import random

from deckgen.figures import Canvas, INK, TEAL, ORANGE, VIOLET, MUTED, LINE
from figures import draw_chair

PAPER = '#F4F4F2'
PALE_TEAL = '#E9F3F4'
PALE_VIOLET = '#F2ECF5'
PALE_ORANGE = '#FCF2EA'
WHITE = '#FFFFFF'


def _arrow(c, x1, y1, x2, y2, color=INK, width=5, head=17):
    c.line(x1, y1, x2, y2, color, width)
    angle = math.atan2(y2 - y1, x2 - x1)
    for offset in (-0.48, 0.48):
        a = angle + math.pi + offset
        c.line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), color, width)


def _box(c, x, y, w, h, title, detail, fill, accent, title_color=INK):
    c.rect(x, y, w, h, fill=fill, stroke=accent, width=4)
    c.text(x + w / 2, y + 43, title, size=25, color=title_color,
           mono=True, anchor='middle', weight=700)
    c.text(x + w / 2, y + 82, detail, size=23, color=title_color,
           mono=False, anchor='middle')


def gan_adversaries(name='w05-gan-adversaries', w=1680, h=620):
    """The generator/discriminator competition, explicitly without caption input."""
    c = Canvas(w, h, bg=WHITE)
    c.text(840, 45, 'LEARN FROM EXAMPLES · NOT A TEXT PROMPT', size=23,
           color=VIOLET, anchor='middle', weight=700)

    c.rect(1090, 80, 255, 145, fill=PAPER, stroke=LINE, width=3)
    c.text(1217, 116, 'TRAINING IMAGES', size=20, color=INK, anchor='middle', weight=700)
    tile = 68
    colors = [TEAL, '#9FCED0', '#6685BF', '#B68EBB', '#E38E5D', '#F0BD60']
    for i, color in enumerate(colors):
        x, y = 1100 + (i % 3) * 76, 135 + (i // 3) * 42
        c.rect(x, y, 64, 34, fill=WHITE, stroke=LINE, width=2)
        c.rect(x + 7, y + 5, 50, 18, fill=color)
        c.line(x + 8, y + 28, x + 56, y + 28, MUTED, 2)

    c.rect(115, 262, 220, 95, fill=INK)
    rng = random.Random(8)
    for row in range(4):
        for col in range(10):
            shade = rng.choice(['#35404C', '#57616D', '#79828B', '#28313A'])
            c.rect(128 + col * 19, 274 + row * 17, 15, 13, fill=shade)
    c.text(225, 384, 'RANDOM LATENT', size=20, color=MUTED, anchor='middle')

    _box(c, 440, 300, 230, 130, 'GENERATOR', 'makes a candidate',
         PALE_VIOLET, VIOLET)
    c.rect(735, 285, 245, 165, fill=PALE_ORANGE, stroke=ORANGE, width=4)
    c.text(857, 325, 'SYNTHETIC', size=21, color=ORANGE, anchor='middle', weight=700)
    for i, color in enumerate(('#B68EBB', '#6685BF', '#E38E5D')):
        x = 755 + i * 67
        c.rect(x, 355, 52, 60, fill=WHITE, stroke=LINE, width=2)
        c.circle(x + 26, 377, 11, fill=color)
        c.rect(x + 15, 392, 22, 14, fill=color)

    _box(c, 1090, 300, 245, 130, 'DISCRIMINATOR', 'real or generated?',
         PALE_TEAL, TEAL)
    c.circle(1500, 365, 75, fill=INK)
    c.text(1500, 359, 'REAL?', size=25, color=WHITE, anchor='middle', weight=700)
    c.text(1500, 391, 'OR FAKE?', size=19, color='#D3E7E8', anchor='middle')

    _arrow(c, 335, 310, 440, 350, color=ORANGE)
    _arrow(c, 670, 365, 735, 365, color=VIOLET)
    _arrow(c, 980, 365, 1090, 365, color=ORANGE)
    _arrow(c, 1212, 225, 1212, 300, color=LINE, width=4)
    _arrow(c, 1335, 365, 1425, 365, color=TEAL)
    c.line(1500, 440, 1500, 485, ORANGE, 4)
    c.line(1500, 485, 555, 485, ORANGE, 4)
    _arrow(c, 555, 485, 555, 430, color=ORANGE)
    c.text(1030, 535, 'The discriminator learns to catch fakes. The generator learns to fool it.',
           size=25, color=INK, mono=False, anchor='middle', weight=600)
    return c.finish(name)


def clip_shared_space(name='w05-clip-shared-space', w=1680, h=620):
    """Show text and image encoders aligning paired examples in one vector space."""
    c = Canvas(w, h, bg=WHITE)
    c.rect(45, 85, 330, 155, fill=PALE_VIOLET, stroke=VIOLET, width=3)
    c.text(75, 125, 'CAPTION', size=21, color=VIOLET, weight=700)
    c.text(75, 165, 'a chair with a', size=22, color=INK, mono=False)
    c.text(75, 193, 'curved back', size=22, color=INK, mono=False)

    c.rect(45, 285, 330, 225, fill=PAPER, stroke=LINE, width=3)
    c.text(75, 325, 'IMAGE', size=21, color=TEAL, weight=700)
    draw_chair(c, 125, 337, 155, seat_h=0.42, back_h=0.6,
               back_angle=12, seat_w=0.7, legs=4, stroke=INK, width=5)

    _box(c, 455, 115, 250, 105, 'TEXT ENCODER', 'caption → vector',
         PALE_VIOLET, VIOLET)
    _box(c, 455, 335, 250, 105, 'IMAGE ENCODER', 'picture → vector',
         PALE_TEAL, TEAL)
    _arrow(c, 375, 160, 455, 160, color=VIOLET)
    _arrow(c, 375, 397, 455, 397, color=TEAL)

    c.rect(800, 85, 825, 430, fill='#FBFBFA', stroke=LINE, width=3)
    c.text(1212, 125, 'SHARED EMBEDDING SPACE', size=24, color=INK,
           anchor='middle', weight=700)
    c.line(880, 445, 1550, 445, MUTED, 2)
    c.line(880, 170, 880, 445, MUTED, 2)
    for i in range(1, 5):
        c.line(880 + i * 134, 170, 880 + i * 134, 445, '#E1E1DE', 1)
    for i in range(1, 3):
        c.line(880, 170 + i * 91, 1550, 170 + i * 91, '#E1E1DE', 1)

    pairs = [((1030, 260), (1084, 282)), ((1335, 340), (1390, 322))]
    for (tx, ty), (ix, iy) in pairs:
        c.line(tx, ty, ix, iy, MUTED, 3)
        c.circle(tx, ty, 14, fill=VIOLET)
        c.circle(ix, iy, 14, fill=TEAL)
    c.circle(1190, 210, 14, fill=VIOLET)
    c.circle(1500, 255, 14, fill=TEAL)
    c.text(1060, 235, 'caption', size=18, color=VIOLET, anchor='middle')
    c.text(1115, 315, 'matching image', size=18, color=TEAL, anchor='middle')
    c.text(1265, 405, 'different meaning → farther apart', size=19,
           color=MUTED, anchor='middle')
    c.text(840, 570, 'CLIP aligns meaning across modalities; it does not generate the picture.',
           size=25, color=INK, mono=False, anchor='middle', weight=600)
    return c.finish(name)


def diffusion_denoising(name='w05-diffusion-denoising', w=1680, h=620):
    """Conceptual latent-noise-to-image sequence, not a recorded model trajectory."""
    c = Canvas(w, h, bg=WHITE)
    stages = [35, 445, 855, 1265]
    labels = ['1 · NOISE', '2 · DENOISE', '3 · STRUCTURE', '4 · DECODE']
    for x, label in zip(stages, labels):
        c.text(x + 170, 76, label, size=21, color=INK, anchor='middle', weight=700)
        c.rect(x, 100, 340, 390, fill=PAPER, stroke=LINE, width=2)
    rng = random.Random(5)
    palette = ['#4F5559', '#6685BF', '#943890', '#64C2C3', '#ED6D24', '#BBBCB9']
    for row in range(8):
        for col in range(8):
            c.rect(55 + col * 36, 140 + row * 36, 28, 28,
                   fill=rng.choice(palette))

    draw_chair(c, 520, 190, 180, seat_h=0.42, back_h=0.6,
               back_angle=10, seat_w=0.66, legs=4, stroke='#BBBCB9', width=8)
    for _ in range(25):
        x, y = rng.randrange(460, 765), rng.randrange(145, 450)
        c.rect(x, y, 14, 14, fill=rng.choice(palette))

    draw_chair(c, 930, 190, 180, seat_h=0.42, back_h=0.6,
               back_angle=10, seat_w=0.66, legs=4, stroke='#56616D', width=7)
    for _ in range(8):
        x, y = rng.randrange(895, 1160), rng.randrange(145, 455)
        c.rect(x, y, 10, 10, fill=rng.choice(palette))

    draw_chair(c, 1345, 190, 180, seat_h=0.42, back_h=0.6,
               back_angle=10, seat_w=0.66, legs=4, stroke=INK, width=7)
    c.rect(1295, 392, 280, 48, fill=PALE_TEAL)
    c.text(1435, 423, '“a chair with a curved back”', size=17, color=INK,
           mono=False, anchor='middle')

    for x in (385, 795, 1205):
        _arrow(c, x, 290, x + 48, 290, color=ORANGE, width=5, head=15)
    c.text(840, 555, 'Text conditions the denoising; latent diffusion decodes the final image back to pixels.',
           size=23, color=INK, mono=False, anchor='middle', weight=600)
    return c.finish(name)


def agent_image_tools(name='w05-agent-image-tools', w=1680, h=620):
    """Human-directed agent loop using vision and image-generation tools."""
    c = Canvas(w, h, bg=WHITE)
    _box(c, 45, 205, 260, 150, 'YOUR INTENT', 'what should it do?',
         PAPER, LINE)
    _box(c, 425, 205, 270, 150, 'AGENT', 'plan · call · compare',
         INK, INK, title_color=WHITE)
    _box(c, 825, 95, 300, 145, 'VISION TOOL', 'describe / inspect',
         PALE_TEAL, TEAL)
    _box(c, 825, 355, 300, 145, 'IMAGE TOOL', 'generate / edit',
         PALE_ORANGE, ORANGE)
    c.rect(1260, 195, 350, 270, fill=PAPER, stroke=LINE, width=3)
    c.text(1435, 235, 'CANDIDATE IMAGE', size=21, color=INK,
           anchor='middle', weight=700)
    c.rect(1340, 265, 190, 135, fill=PALE_VIOLET, stroke=VIOLET, width=2)
    c.circle(1435, 300, 24, fill=ORANGE)
    c.rect(1400, 327, 70, 45, fill=TEAL)

    _arrow(c, 305, 280, 425, 280, color=VIOLET)
    _arrow(c, 695, 245, 825, 175, color=TEAL)
    _arrow(c, 695, 315, 825, 425, color=ORANGE)
    _arrow(c, 1125, 425, 1260, 340, color=ORANGE)
    _arrow(c, 1260, 240, 1125, 175, color=TEAL)
    c.line(975, 240, 975, 355, TEAL, 4)
    _arrow(c, 825, 175, 695, 245, color=TEAL)
    c.text(840, 555, 'The agent can inspect and generate. The designer still chooses what counts as success.',
           size=23, color=INK, mono=False, anchor='middle', weight=600)
    return c.finish(name)
