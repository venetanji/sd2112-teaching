"""Original teaching diagrams, not empirical charts or model explanations."""
from deckgen.figures import Canvas, INK

PAPER = '#F4F4F2'
TEAL = '#246E70'
LINE = '#D5DCDA'


def label(c, x, y, text, size=32, color=INK):
    c.text(x, y, text, size=size, color=color, anchor='middle', mono=False, weight=700)


def node(c, x, y, w, heading, detail):
    c.rect(x, y, w, 136, fill='#FFFFFF', stroke=LINE, width=3)
    label(c, x + w / 2, y + 55, heading, 36)
    label(c, x + w / 2, y + 105, detail, 27, TEAL)


def arrow(c, x1, y, x2):
    c.line(x1, y, x2, y, TEAL, 4)
    c.line(x2 - 16, y - 10, x2, y, TEAL, 4)
    c.line(x2 - 16, y + 10, x2, y, TEAL, 4)


def alterity():
    c = Canvas(1680, 520, bg=PAPER)
    label(c, 840, 55, 'ALTERITY: FACING A QUASI-OTHER', 32, TEAL)
    node(c, 70, 135, 350, 'PERSON', 'addresses the system')
    arrow(c, 420, 203, 570)
    node(c, 570, 135, 510, 'TECHNOLOGY', 'appears to answer back')
    c.line(1100, 203, 1220, 203, LINE, 4)
    node(c, 1240, 135, 370, 'WORLD', 'recedes from focus')
    label(c, 840, 360, 'The relation is experienced. Consciousness is not established.', 34)
    label(c, 840, 445, 'One product can invite different relations in different moments.', 30, TEAL)
    return c.finish('w08-alterity')


def expectations():
    c = Canvas(1680, 520, bg=PAPER)
    for x, head, detail in ((40, 'CUES', 'voice / name / memory'),
                            (620, 'EXPECTATIONS', 'care / competence'),
                            (1200, 'ACTIONS', 'disclose / rely / check')):
        node(c, x, 120, 440, head, detail)
    arrow(c, 480, 188, 620)
    arrow(c, 1060, 188, 1200)
    label(c, 840, 350, 'What might a person infer? What would you need to observe?', 34)
    label(c, 840, 445, 'Design-analysis questions, not a proven universal causal chain.', 30, TEAL)
    return c.finish('w08-expectations')


def layers():
    c = Canvas(1680, 520, bg=PAPER)
    items = ((40, 'DATA', 'What is collected?', 'Who can access or delete it?'),
             (620, 'AI', 'What is selected or generated?', 'What is rewarded or missed?'),
             (1200, 'EXPERIENCE', 'What does the person infer?', 'What can they change or refuse?'))
    for x, head, question, action in items:
        node(c, x, 60, 440, head, '')
        label(c, x + 220, 268, question, 27)
        label(c, x + 220, 330, action, 25, TEAL)
    arrow(c, 480, 128, 620)
    arrow(c, 1060, 128, 1200)
    label(c, 840, 445, 'Locate a mechanism. Propose a design response. Test the effect.', 34)
    return c.finish('w08-layers')


def transfer():
    c = Canvas(1680, 520, bg=PAPER)
    node(c, 60, 80, 620, 'THE STUDY', 'people / system / task / duration')
    node(c, 1000, 80, 620, 'YOUR PRODUCT', 'people / system / task / duration')
    arrow(c, 680, 148, 1000)
    label(c, 840, 290, 'Which conditions match? Which ones change?', 38)
    label(c, 840, 370, 'A transfer gap is a research question, not a blank cheque.', 34)
    label(c, 840, 455, 'Narrow the claim or design a comparison before scaling the promise.', 30, TEAL)
    return c.finish('w08-transfer')
