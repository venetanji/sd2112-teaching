"""Week 5 philosophy diagrams, using the course's visual language."""
from deckgen.figures import Canvas, INK, TEAL

PAPER = '#F4F4F2'
DARK_TEAL = '#246E70'
LINE = '#D5DCDA'


def _label(c, x, y, text, size=32, color=INK):
    c.text(x, y, text, size=size, color=color, anchor='middle', weight=700, mono=False)


def _box(c, x, y, w, title, detail):
    c.rect(x, y, w, 140, fill='#FFFFFF', stroke=LINE, width=3)
    _label(c, x + w / 2, y + 58, title, 36)
    c.text(x + w / 2, y + 105, detail, size=28, color=INK, anchor='middle', mono=False)


def _arrow(c, x1, y, x2):
    c.line(x1, y, x2, y, DARK_TEAL, 5)
    c.line(x2 - 17, y - 11, x2, y, DARK_TEAL, 5)
    c.line(x2 - 17, y + 11, x2, y, DARK_TEAL, 5)


def tool_encounter(name='w05-tool-encounter', w=1680, h=520):
    c = Canvas(w, h, bg=PAPER)
    _label(c, 405, 48, 'IN USE', 30, DARK_TEAL)
    _label(c, 1275, 48, 'IN INSPECTION', 30, DARK_TEAL)
    _box(c, 35, 90, 390, 'YOU + TOOL', 'work through it')
    _arrow(c, 425, 160, 480)
    _box(c, 480, 90, 300, 'PROJECT', 'attention on the task')
    _box(c, 920, 90, 250, 'YOU', 'examine it')
    _arrow(c, 1170, 160, 1225)
    _box(c, 1225, 90, 410, 'TOOL', 'attention on the object')
    _label(c, 405, 307, 'Ready-to-hand', 40)
    _label(c, 1275, 307, 'Present-at-hand', 40)
    c.line(35, 365, 1635, 365, LINE, 3)
    _label(c, 840, 425, 'LATER: ENFRAMING', 30, DARK_TEAL)
    c.text(840, 487, 'Modern technology reveals the world as resources to order and use.',
           size=32, color=INK, anchor='middle', mono=False)
    return c.finish(name)


def mediation_relations(name='w05-mediation-relations', w=1680, h=520):
    c = Canvas(w, h, bg=PAPER)
    for x, width, label in ((55, 380, 'HUMAN'), (645, 390, 'TECHNOLOGY'),
                            (1245, 380, 'WORLD')):
        c.rect(x, 20, width, 100, fill='#FFFFFF', stroke=TEAL, width=3)
        _label(c, x + width / 2, 83, label, 36)
    # Connections name a relation, not a one-way information pipeline.
    c.line(435, 70, 645, 70, DARK_TEAL, 4)
    c.line(1035, 70, 1245, 70, DARK_TEAL, 4)
    for x, label, form, example in (
        (425, 'EMBODIMENT', '(I \u2014 TECHNOLOGY) \u2192 WORLD',
         'Look through the viewfinder at a scene.'),
        (1255, 'HERMENEUTIC', 'I \u2192 (TECHNOLOGY \u2014 WORLD)',
         'Read a photograph as a representation.'),
    ):
        _label(c, x, 210, label, 32, DARK_TEAL)
        _label(c, x, 279, form, 34)
        c.text(x, 345, example, size=31, color=INK, anchor='middle', mono=False)
    c.line(55, 408, 1625, 408, LINE, 3)
    _label(c, 840, 479, 'OTHER RELATIONS: ALTERITY / BACKGROUND', 32)
    return c.finish(name)


def two_circle_rules(name='w05-two-circle-rules', w=600, h=450):
    c = Canvas(w, h, bg='#FFFFFF')
    c.circle(200, 300, 75, stroke=INK, width=4)
    c.circle(400, 200, 125, stroke=INK, width=4)
    return c.finish(name)
