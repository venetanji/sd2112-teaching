"""Navigation figures for the separate contributor deck."""
from html import escape
from math import ceil

from deckgen.core import pil_font
from deckgen.figures import Canvas

PHASE_NAMES = ('discover', 'define', 'develop', 'deliver')
THINKING_MODES = {
    'discover': 'Divergent Thinking (Creative Thinking)',
    'define': 'Convergent Thinking (Logical Thinking)',
    'develop': 'Divergent Thinking (Creative Thinking)',
    'deliver': 'Convergent Thinking (Logical Thinking)',
}


def phase_subtitle(space, phase):
    """Use browser-shaped text and equal explicit gaps around the small separator."""
    scale, size, baseline = 6, 34, 34
    font = pil_font('body', size*scale)
    small = pil_font('body', size*scale//3)
    left, right, glyph, gap = space, THINKING_MODES[phase], '\u25c6', 12
    glyph_x = font.getlength(left)/scale+gap
    right_x = glyph_x+small.getlength(glyph)/scale+gap
    width = ceil(right_x+font.getlength(right)/scale)+2
    xb, gb = font.getbbox('x', anchor='ls'), small.getbbox(glyph, anchor='ls')
    x_center = baseline+(xb[1]+xb[3])/(2*scale)
    glyph_baseline = x_center-(gb[1]+gb[3])/(2*scale)
    c = Canvas(width, 48, scale=scale)
    label = escape(space+' '+glyph+' '+right)
    c.svg[0] = c.svg[0][:-1]+f' role="img" aria-label="{label}">'
    c.svg.append(f'<title>{label}</title>')
    spans = []
    for cls, x, y, text, font_size, color, face in [
            ('subtitle-space', 0, baseline, left, size, '#5A626B', font),
            ('subtitle-separator', glyph_x, glyph_baseline, glyph, size/3, '#246E70', small),
            ('subtitle-mode', right_x, baseline, right, size, '#5A626B', font)]:
        # Browser glyph advances must not be inferred from the separate raster renderer.
        horizontal = 'x="0"' if cls == 'subtitle-space' else f'dx="{gap}"'
        spans.append(f'<tspan class="{cls}" {horizontal} y="{y}" '
                     f'font-size="{font_size}" fill="{color}">{escape(text)}</tspan>')
        c.d.text((x*scale, y*scale), text, font=face, fill=color, anchor='ls')
    c.svg.append('<text font-family="Inter,sans-serif" font-weight="400" '
                 'style="font-optical-sizing:none;font-feature-settings:normal;'
                 'text-rendering:geometricPrecision">'
                 +''.join(spans)+'</text>')
    svg, png = c.finish('week10-nicolo-subtitle-'+phase)
    return width, svg, png


def phase_map(phase=None):
    """Simplified Double Diamond after Design Council; color only the active half."""
    if phase is not None and phase not in PHASE_NAMES:
        raise ValueError(f'Unknown Double Diamond phase: {phase}')
    c = Canvas(360, 176)
    description = phase.title()+' highlighted' if phase else 'all phases, no highlight'
    c.svg.append(f'<title>Double Diamond navigation: {description}</title>')
    halves = [
        [(12, 88), (96, 4), (96, 172)],
        [(96, 4), (180, 88), (96, 172)],
        [(180, 88), (264, 4), (264, 172)],
        [(264, 4), (348, 88), (264, 172)],
    ]
    for name, points in zip(PHASE_NAMES, halves):
        c.poly(points, '#246E70' if name == phase else '#FFFFFF', '#222222', 2)
    return c.finish('week10-nicolo-map-'+(phase or 'all'))
