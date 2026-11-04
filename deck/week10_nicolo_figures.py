"""Navigation figures for the separate contributor deck."""
from html import escape
from math import ceil

from deckgen.core import pil_font
from deckgen.figures import Canvas

PHASE_NAMES = ('discover', 'define', 'develop', 'deliver')


def phase_subtitle(space, phase):
    """Align the small separator to the text's measured x-height in both outputs."""
    scale, size, baseline = 6, 34, 34
    font = pil_font('body', size*scale)
    small = pil_font('body', size*scale//3)
    left, right, glyph = space+' ', ' '+phase, '\u25c6'
    glyph_x = font.getlength(left)/scale
    right_x = glyph_x+small.getlength(glyph)/scale
    width = ceil(right_x+font.getlength(right)/scale)+2
    xb, gb = font.getbbox('x', anchor='ls'), small.getbbox(glyph, anchor='ls')
    x_center = baseline+(xb[1]+xb[3])/(2*scale)
    glyph_baseline = x_center-(gb[1]+gb[3])/(2*scale)
    c = Canvas(width, 48, scale=scale)
    label = escape(space+' '+glyph+' '+phase)
    c.svg[0] = c.svg[0][:-1]+f' role="img" aria-label="{label}">'
    c.svg.append(f'<title>{label}</title>')
    for cls, x, y, text, font_size, color, face in [
            ('subtitle-space', 0, baseline, left, size, '#5A626B', font),
            ('subtitle-separator', glyph_x, glyph_baseline, glyph, size/3, '#246E70', small),
            ('subtitle-phase', right_x, baseline, right, size, '#5A626B', font)]:
        c.svg.append(f'<text class="{cls}" x="{x}" y="{y}" '
                     f'font-family="Inter,sans-serif" font-size="{font_size}" '
                     f'font-weight="400" fill="{color}" xml:space="preserve">{escape(text)}</text>')
        c.d.text((x*scale, y*scale), text, font=face, fill=color, anchor='ls')
    svg, png = c.finish('week10-nicolo-subtitle-'+phase)
    return width, svg, png


def phase_map(phase):
    """Simplified Double Diamond after Design Council; color only the active half."""
    if phase not in PHASE_NAMES:
        raise ValueError(f'Unknown Double Diamond phase: {phase}')
    c = Canvas(360, 176)
    c.svg.append(f'<title>Double Diamond navigation: {phase.title()} highlighted</title>')
    halves = [
        [(12, 88), (96, 4), (96, 172)],
        [(96, 4), (180, 88), (96, 172)],
        [(180, 88), (264, 4), (264, 172)],
        [(264, 4), (348, 88), (264, 172)],
    ]
    for name, points in zip(PHASE_NAMES, halves):
        c.poly(points, '#246E70' if name == phase else '#FFFFFF', '#222222', 2)
    return c.finish('week10-nicolo-map-'+phase)
