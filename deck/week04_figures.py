"""Week 4 diagrams: language structure, sequence models, retrieval, agents and harnesses."""
from __future__ import annotations

import math

from deckgen.figures import Canvas, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, MUTED, LINE


def _arrow(c, x1, y1, x2, y2, color=INK, width=3, head=12):
    c.line(x1, y1, x2, y2, color, width)
    angle = math.atan2(y2 - y1, x2 - x1)
    for offset in (-0.45, 0.45):
        a = angle + math.pi + offset
        c.line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), color, width)


def _box(c, x, y, w, h, label, fill=WHITE, stroke=LINE, color=INK, size=20):
    c.rect(x, y, w, h, fill=fill, stroke=stroke, width=2)
    c.text(x + w / 2, y + h / 2 + size * 0.34, label, size=size, color=color, anchor='middle')


def grammar_tree(name='w04-grammar-tree', w=1680, h=560):
    """A toy phrase-structure tree; not a diagram of Universal Grammar itself."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(80, 70, 'A TOY GENERATIVE GRAMMAR', size=20, color=ORANGE)
    c.text(80, 112, 'One rule can generate many sentences.', size=36, color=INK)
    c.text(840, 180, 'S → NP + VP', size=26, color=VIOLET, anchor='middle')

    root = (840, 226)
    np = (490, 340)
    vp = (1190, 340)
    det = (260, 448)
    noun = (680, 448)
    verb = (1040, 448)
    obj = (1410, 448)
    for a, b in ((root, np), (root, vp), (np, det), (np, noun), (vp, verb), (vp, obj)):
        _arrow(c, a[0], a[1], b[0], b[1], color=LINE, width=3, head=10)

    _box(c, 370, 292, 240, 64, 'NP · noun phrase', fill='#E8F3F2', stroke=TEAL, size=19)
    _box(c, 1070, 292, 240, 64, 'VP · verb phrase', fill='#EEE8F5', stroke=VIOLET, size=19)
    for x, label in ((140, 'the'), (560, 'designer'), (940, 'writes'), (1300, 'a brief')):
        _box(c, x, 418, 240, 64, label, fill=WHITE, stroke=LINE, size=23)
    c.text(840, 530, 'The example is deliberately small. Human language is not this four-box rule.', size=18,
           color=MUTED, anchor='middle')
    return c.finish(name)


def sequence_models(name='w04-sequence-models', w=1680, h=620):
    """Compare recurrent state with transformer self-attention schematically."""
    c = Canvas(w, h)
    c.rect(0, 0, 810, h, fill='#F4F4F2')
    c.rect(870, 0, w - 870, h, fill=INK)

    c.text(50, 64, 'RNN · RECURRENT STATE', size=22, color=ORANGE)
    c.text(50, 104, 'Read one position, then the next.', size=32, color=INK)
    c.text(920, 64, 'TRANSFORMER · SELF-ATTENTION', size=22, color=TEAL)
    c.text(920, 104, 'Each position uses its context.', size=32, color=WHITE)

    words = ['the', 'designer', 'writes', 'a', 'brief']
    xs = [82, 222, 362, 502, 642]
    for i, (x, word) in enumerate(zip(xs, words)):
        _box(c, x, 158, 104, 50, word, fill=WHITE, stroke=LINE, size=17)
        _box(c, x + 7, 336, 90, 68, f'h{i + 1}', fill='#E4F1F0', stroke=TEAL, size=22)
        _arrow(c, x + 52, 210, x + 52, 322, color=LINE, width=2, head=8)
        if i:
            _arrow(c, xs[i - 1] + 100, 370, x + 2, 370, color=TEAL, width=3, head=9)

    c.text(410, 458, 'the hidden state carries a summary forward', size=19, color=MUTED, anchor='middle')
    c.text(410, 534, 'one recurrent step follows another', size=17, color=MUTED, anchor='middle')

    tx = [922, 1062, 1202, 1342, 1482]
    for x, word in zip(tx, words):
        _box(c, x, 158, 112, 50, word, fill='#172C43', stroke='#657180', color=WHITE, size=17)
    c.text(920, 258, 'CAUSAL ATTENTION · FUTURE TOKENS MASKED', size=17, color='#B7D5D8')
    gx, gy, cell = 1060, 298, 58
    for row in range(5):
        for col in range(5):
            fill = '#64C2C3' if col == row else ('#2C5669' if col < row else '#12263B')
            c.rect(gx + col * cell, gy + row * cell, cell - 5, cell - 5,
                   fill=fill, stroke='#657180', width=1)
    c.text(920, 592, 'Schematic attention mask · not learned weights', size=16, color='#B7D5D8')
    c.text(1480, 592, 'Training can process positions in parallel.', size=16, color='#B7D5D8', anchor='end')
    return c.finish(name)


def qa_to_agent(name='w04-qa-to-agent', w=1680, h=620):
    """Separate one-pass retrieve-and-answer from an agent that iterates with tools."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)

    c.text(55, 62, 'QUESTION ANSWERING · RETRIEVE, THEN ANSWER', size=22, color=VIOLET)
    c.text(55, 100, 'One pass can add evidence to a reply.', size=30, color=INK)
    top = 180
    boxes = [
        (60, 'QUESTION', 190), (330, 'SEARCH / INDEX', 210), (630, 'PASSAGES', 220),
        (940, 'LANGUAGE MODEL', 250), (1290, 'ANSWER (+ SOURCES)', 300),
    ]
    for x, label, bw in boxes:
        _box(c, x, top, bw, 80, label, fill=WHITE, stroke=LINE, size=18)
    for (x, _, bw), (nx, _, _) in zip(boxes, boxes[1:]):
        _arrow(c, x + bw + 8, top + 40, nx - 12, top + 40, color=VIOLET, width=3, head=11)

    c.rect(0, 330, w, 290, fill='#071629')
    c.text(55, 384, 'AGENT · SELECT A TOOL, READ WHAT HAPPENED, CONTINUE OR STOP', size=22, color=TEAL)
    c.text(55, 422, 'The route can change while the task is running.', size=30, color=WHITE)
    lower = [
        (60, 'GOAL', 190), (330, 'MODEL CHOICE', 220), (650, 'TOOL · SEARCH / FILES', 250),
        (1010, 'OBSERVATION', 240), (1350, 'DONE? · HUMAN CHECK', 270),
    ]
    y = 484
    for x, label, bw in lower:
        _box(c, x, y, bw, 78, label, fill='#142A40', stroke='#647285', color=WHITE, size=17)
    for (x, _, bw), (nx, _, _) in zip(lower, lower[1:]):
        _arrow(c, x + bw + 8, y + 39, nx - 12, y + 39, color=TEAL, width=3, head=11)
    _arrow(c, 1120, 573, 450, 573, color=ORANGE, width=3, head=13)
    c.text(790, 606, 'A result returns to the model for another decision.', size=16, color='#E8C3AA', anchor='middle')
    return c.finish(name)


def agent_loop(name='w04-agent-loop', w=1680, h=520):
    """Show the visible action / observation loop, including a human stop point."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(70, 62, 'AN AGENT REPEATS A SMALL LOOP', size=21, color=VIOLET)
    c.text(70, 105, 'The model proposes; the harness routes and records.', size=32, color=INK)
    boxes = [
        (70, 'GOAL + LIMITS', 235), (400, 'MODEL', 205), (700, 'TOOL CALL', 210),
        (1010, 'OBSERVATION', 245), (1360, 'CONTINUE / STOP', 260),
    ]
    y = 205
    for x, label, bw in boxes:
        fill = '#172A40' if label == 'MODEL' else WHITE
        color = WHITE if label == 'MODEL' else INK
        stroke = INK if label == 'MODEL' else LINE
        _box(c, x, y, bw, 88, label, fill=fill, stroke=stroke, color=color, size=18)
    for (x, _, bw), (nx, _, _) in zip(boxes, boxes[1:]):
        _arrow(c, x + bw + 10, y + 44, nx - 12, y + 44,
               color=ORANGE if x == 1010 else VIOLET, width=3, head=12)
    _arrow(c, 1120, 312, 500, 312, color=TEAL, width=3, head=12)
    c.text(810, 354, 'tool result returns as new context', size=18, color=MUTED, anchor='middle')
    c.text(1490, 420, 'Person can approve, redirect or stop.', size=18, color=INK, anchor='middle')
    c.text(840, 486, 'A tool call is an action. A reply alone is not.', size=19, color=VIOLET, anchor='middle')
    return c.finish(name)


def harness_layers(name='w04-harness-layers', w=1680, h=620):
    """A compact view of the software around an agent model."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(840, 50, 'THE HARNESS IS THE RUNNING SYSTEM AROUND THE MODEL', size=22,
           color=VIOLET, anchor='middle')
    c.rect(70, 88, 1540, 470, fill='#FAFAF8', stroke=VIOLET, width=4)
    c.text(840, 122, 'HARNESS · loop, state, tool routing, boundaries, record', size=20,
           color=VIOLET, anchor='middle')

    flow = [
        (110, 'GOAL + INPUT', 260),
        (440, 'MODEL', 260),
        (770, 'TOOL ROUTER', 260),
        (1100, 'TOOL', 260),
    ]
    for x, label, bw in flow:
        is_model = label == 'MODEL'
        _box(c, x, 185, bw, 78, label,
             fill=INK if is_model else WHITE,
             stroke=INK if is_model else LINE,
             color=WHITE if is_model else INK,
             size=19)
    for (x, _, bw), (nx, _, _) in zip(flow, flow[1:]):
        _arrow(c, x + bw + 9, 224, nx - 12, 224, color=TEAL, width=3, head=10)

    # A single return path keeps the tool-result loop readable at a glance.
    _arrow(c, 1230, 276, 570, 328, color=ORANGE, width=3, head=11)
    c.text(900, 348, 'tool result → next model turn', size=17, color=MUTED, anchor='middle')

    supports = [
        (170, 'CONTEXT + MEMORY', 350),
        (665, 'PERMISSIONS + SANDBOX', 350),
        (1160, 'LOGS + HUMAN CHECK', 350),
    ]
    for x, label, bw in supports:
        _box(c, x, 410, bw, 68, label, fill=WHITE, stroke=LINE, size=17)

    c.text(840, 526, 'These controls shape what the model can see, do, and hand back.',
           size=18, color=MUTED, anchor='middle')
    return c.finish(name)


def reflection_evidence(name='w04-reflection-evidence', w=1680, h=420):
    """Map weekly challenges to the Week 7 reflection without implying all five are required."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(70, 58, 'YOUR PROCESS, ACROSS FIVE WEEKS', size=20, color=VIOLET)
    weeks = [
        ('W2', 'rule-based picture', TEAL),
        ('W3', 'concept blend', TEAL),
        ('W4', 'language agent', VIOLET),
        ('W5', 'image / layout', ORANGE),
        ('W6', 'sound / music', ORANGE),
    ]
    x0, gap = 150, 300
    for i, (week, label, color) in enumerate(weeks):
        x = x0 + i * gap
        c.circle(x, 194, 45, fill=color)
        c.text(x, 202, week, size=20, color=WHITE, anchor='middle')
        c.text(x, 282, label, size=20, color=INK, anchor='middle')
        if i < len(weeks) - 1:
            _arrow(c, x + 54, 194, x + gap - 54, 194, color=LINE, width=3, head=11)
    c.text(840, 370, 'Bring evidence from at least three of your own experiments into the Week 7 reflection.',
           size=19, color=MUTED, anchor='middle')
    return c.finish(name)
