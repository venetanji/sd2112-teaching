"""Course adaptation of Design Council's Double Diamond, CC BY 4.0."""
from deckgen.figures import Canvas
from deckgen.core import pil_font


def diamond():
    c = Canvas(1680, 540, bg='#F4F4F2')
    def label(x, cy, text, size=32, color='#000B1C'):
        f = pil_font('semibold', round(c.s(size)))
        top, bottom = f.getbbox(text)[1::2]
        baseline = cy + (f.getmetrics()[0] - (top + bottom) / 2) / c.s(1)
        c.text(x, baseline, text, size=size, color=color, weight=600, anchor='middle')
    for x in (80, 850):
        for a, b in [((x, 255), (x+350, 80)), ((x+350, 80), (x+700, 255)),
                     ((x+700, 255), (x+350, 430)), ((x+350, 430), (x, 255))]:
            c.line(*a, *b, '#246E70', 7)
        c.line(x+350, 93, x+350, 417, '#BBBCB9', 2)
    for x, phase, detail in [(255, 'DISCOVER', 'Explore evidence'), (605, 'DEFINE', 'Focus the question'),
                              (1025, 'DEVELOP', 'Explore responses'), (1375, 'DELIVER', 'Test and improve')]:
        label(x, 230, phase, 30)
        label(x, 277, detail, 20)
    label(430, 35, 'PROBLEM SPACE', 26)
    label(1200, 35, 'SOLUTION SPACE', 26)
    label(840, 495, 'Open up possibilities. Focus a decision. Return when evidence changes.', 29)
    return c.finish('week10-double-diamond')
