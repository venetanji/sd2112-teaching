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


def text_conditioning(name='w05-text-conditioning', w=1680, h=620):
    """Show text conditioning and latent noise meeting in an image-generation path."""
    c = Canvas(w, h, bg=WHITE)
    c.rect(35, 195, 270, 165, fill=PALE_ORANGE, stroke=ORANGE, width=3)
    c.text(70, 232, 'PROMPT', size=20, color=ORANGE, weight=700)
    c.text(58, 278, 'paper lantern', size=22, color=INK)
    c.text(58, 316, 'in a night garden', size=22, color=INK)

    c.rect(370, 210, 255, 135, fill=PALE_VIOLET, stroke=VIOLET, width=3)
    c.text(497, 258, 'TEXT ENCODER', size=22, color=INK, anchor='middle', weight=700)
    c.text(497, 294, 'words → features', size=19, color=MUTED, anchor='middle')

    c.text(707, 194, 'TEXT FEATURES', size=18, color=VIOLET, anchor='middle', weight=700)
    for i, height in enumerate((54, 82, 62, 91, 68, 79)):
        x = 675 + i * 12
        c.rect(x, 230 + 90 - height, 8, height, fill=VIOLET if i % 2 else TEAL)

    c.rect(825, 175, 325, 240, fill=INK, stroke=INK, width=3)
    c.text(987, 215, 'DENOISING MODEL', size=22, color=WHITE,
           anchor='middle', weight=700)
    c.text(987, 249, 'uses text features', size=18, color='#DCE8E9', anchor='middle')
    c.circle(987, 326, 48, fill='#182B3A', stroke=TEAL, width=4)
    c.text(987, 322, 'UPDATE', size=15, color=WHITE, anchor='middle', weight=700)
    c.text(987, 343, 'repeat', size=14, color='#DCE8E9', anchor='middle')

    palette = ('#33434F', '#77828A', '#64C2C3', '#943890', '#ED6D24')
    rng = random.Random(41)
    for row in range(4):
        for col in range(6):
            c.rect(958 + col * 15, 480 + row * 14, 11, 10,
                   fill=rng.choice(palette))
    c.text(1000, 562, 'INITIAL LATENT', size=17, color=TEAL,
           anchor='middle', weight=700)

    c.poly([(1200, 238), (1325, 238), (1325, 372), (1200, 338)],
           fill=PALE_TEAL, stroke=TEAL, width=4)
    c.text(1260, 287, 'VAE', size=19, color=INK, anchor='middle', weight=700)
    c.text(1260, 317, 'DECODER', size=18, color=INK, anchor='middle', weight=700)

    c.rect(1450, 190, 190, 205, fill='#172B37', stroke=LINE, width=2)
    c.text(1545, 220, 'OUTPUT IMAGE', size=16, color=WHITE,
           anchor='middle', weight=700)
    c.circle(1545, 305, 57, fill='#24434A')
    c.line(1545, 246, 1545, 260, ORANGE, 4)
    c.line(1527, 260, 1563, 260, ORANGE, 3)
    c.poly([(1526, 263), (1564, 263), (1571, 322), (1519, 322)],
           fill=ORANGE, stroke=ORANGE, width=2)
    c.line(1530, 278, 1560, 278, '#F9C68E', 3)
    c.line(1530, 298, 1560, 298, '#F9C68E', 3)
    c.line(1530, 315, 1560, 315, '#F9C68E', 3)

    _arrow(c, 305, 277, 370, 277, color=ORANGE, width=4, head=14)
    _arrow(c, 625, 277, 660, 277, color=VIOLET, width=4, head=14)
    _arrow(c, 742, 277, 825, 277, color=VIOLET, width=4, head=14)
    _arrow(c, 1000, 480, 1000, 420, color=TEAL, width=4, head=13)
    _arrow(c, 1150, 290, 1200, 290, color=ORANGE, width=4, head=14)
    _arrow(c, 1325, 290, 1450, 290, color=ORANGE, width=4, head=14)
    c.text(1384, 270, 'final z', size=15, color=ORANGE, anchor='middle')
    return c.finish(name)


def vae_latent(name='w05-vae-latent', w=1680, h=620):
    """Show the VAE's tapered encoder, sampled latent bottleneck and decoder."""
    c = Canvas(w, h, bg=WHITE)
    c.rect(35, 205, 210, 205, fill=PALE_TEAL, stroke=TEAL, width=3)
    c.text(140, 238, 'INPUT IMAGE x', size=19, color=INK, anchor='middle', weight=700)
    draw_chair(c, 83, 260, 112, seat_h=0.42, back_h=0.6,
               back_angle=10, seat_w=0.68, legs=4, stroke=INK, width=5)

    c.poly([(300, 165), (540, 225), (540, 370), (300, 430)],
           fill=PALE_ORANGE, stroke=ORANGE, width=4)
    c.text(403, 275, 'ENCODER', size=23, color=INK, anchor='middle', weight=700)
    c.text(403, 309, 'q(z|x)', size=20, color=MUTED, anchor='middle')

    c.rect(600, 218, 190, 158, fill=PALE_VIOLET, stroke=VIOLET, width=3)
    c.text(695, 250, 'DISTRIBUTION', size=18, color=VIOLET,
           anchor='middle', weight=700)
    c.text(695, 290, 'mean', size=18, color=INK, anchor='middle')
    c.rect(638, 300, 115, 8, fill=VIOLET)
    c.text(695, 336, 'log variance', size=16, color=INK, anchor='middle')
    c.rect(638, 346, 84, 8, fill=TEAL)

    c.text(860, 248, 'SAMPLE', size=17, color=VIOLET, anchor='middle', weight=700)
    c.circle(860, 310, 48, fill=VIOLET)
    c.text(860, 319, 'z', size=29, color=WHITE, anchor='middle', weight=700)

    c.poly([(970, 245), (1240, 175), (1240, 420), (970, 350)],
           fill=PALE_TEAL, stroke=TEAL, width=4)
    c.text(1100, 285, 'DECODER', size=23, color=INK, anchor='middle', weight=700)
    c.text(1100, 319, 'p(x-hat|z)', size=18, color=MUTED, anchor='middle')

    c.rect(1410, 205, 235, 205, fill=PAPER, stroke=LINE, width=3)
    c.text(1527, 238, 'RECONSTRUCTION', size=18, color=INK,
           anchor='middle', weight=700)
    draw_chair(c, 1467, 260, 112, seat_h=0.42, back_h=0.6,
               back_angle=10, seat_w=0.68, legs=4, stroke=INK, width=5)
    c.text(1527, 388, 'x-hat', size=18, color=MUTED, anchor='middle')

    _arrow(c, 245, 307, 300, 307, color=TEAL, width=4, head=14)
    _arrow(c, 540, 295, 600, 295, color=ORANGE, width=4, head=14)
    _arrow(c, 790, 295, 812, 295, color=VIOLET, width=4, head=14)
    _arrow(c, 908, 310, 970, 310, color=VIOLET, width=4, head=14)
    _arrow(c, 1240, 307, 1410, 307, color=TEAL, width=4, head=14)
    return c.finish(name)


def _diffusion_snapshot(c, x, y, level, seed):
    """Draw one illustrative image/noise state; levels are qualitative, not measured."""
    c.rect(x, y, 300, 112, fill='#E8E8E4', stroke=LINE, width=2)
    if level < 3:
        draw_chair(c, x + 105, y + 19, 92, seat_h=0.42, back_h=0.6,
                   back_angle=10, seat_w=0.68, legs=4,
                   stroke=('#B8BEC0' if level == 2 else INK), width=4)
    rng = random.Random(seed)
    count = (0, 9, 25, 42)[level]
    palette = ('#535A60', '#74818C', '#9A8CB0', '#64C2C3', '#ED6D24')
    for _ in range(count):
        nx = x + rng.randrange(12, 278)
        ny = y + rng.randrange(9, 100)
        c.rect(nx, ny, 11, 9, fill=rng.choice(palette))


def diffusion_denoising(name='w05-diffusion-denoising', w=1680, h=620):
    """Contrast training's forward noising with generation's iterative reverse process."""
    c = Canvas(w, h, bg=WHITE)
    xs = (35, 455, 875, 1295)
    c.text(840, 46, 'TRAINING · FORWARD PROCESS · ADD NOISE TO EXAMPLES', size=21,
           color=ORANGE, anchor='middle', weight=700)
    top_labels = ('clean image  x0', 'add some noise', 'add more noise', 'mostly noise  xT')
    for i, (x, label) in enumerate(zip(xs, top_labels)):
        c.text(x + 150, 90, label, size=17, color=INK, anchor='middle', weight=700)
        _diffusion_snapshot(c, x, 105, i, 20 + i)
    for x in (345, 765, 1185):
        _arrow(c, x, 160, x + 95, 160, color=ORANGE, width=4, head=13)

    c.text(840, 275, 'GENERATION · REVERSE PROCESS · START FROM LATENT NOISE', size=21,
           color=VIOLET, anchor='middle', weight=700)
    bottom_labels = ('latent noise  zT', 'denoise', 'denoise again', 'clean latent  z0')
    for i, (x, label) in enumerate(zip(xs, bottom_labels)):
        c.text(x + 150, 319, label, size=17, color=INK, anchor='middle', weight=700)
        _diffusion_snapshot(c, x, 334, 3 - i, 40 + i)
    for x in (345, 765, 1185):
        _arrow(c, x, 389, x + 95, 389, color=VIOLET, width=4, head=13)

    c.rect(275, 480, 1130, 58, fill=PALE_TEAL, stroke=TEAL, width=2)
    c.text(840, 516, 'At each reverse step, the text condition can guide the latent update.',
           size=21, color=INK, anchor='middle', weight=600)
    c.text(840, 574, 'Only a few snapshots are shown; real sampling uses many smaller updates.',
           size=18, color=MUTED, anchor='middle')
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
