"""Week 4's full-slide diagrams: language rules, sequence models and agents."""
from __future__ import annotations

import math
import random
import re

from deckgen import WHITE, PAPER
from deckgen.core import pil_font
from deckgen.figures import Canvas, INK, TEAL, ORANGE, VIOLET, MUTED, LINE
from figures import draw_chair

DARK_TEAL = '#246E70'


def _arrow(c, x1, y1, x2, y2, color=INK, width=4, head=16):
    c.line(x1, y1, x2, y2, color, width)
    angle = math.atan2(y2 - y1, x2 - x1)
    for offset in (-0.45, 0.45):
        a = angle + math.pi + offset
        c.line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), color, width)


def _box(c, x, y, w, h, label, fill=WHITE, stroke=LINE, color=INK, size=30, mono=False):
    c.rect(x, y, w, h, fill=fill, stroke=stroke, width=3)
    c.text(x + w / 2, y + h / 2 + size * 0.34, label, size=size, color=color,
           anchor='middle', mono=mono)


def machine_ab(name='w04-machine-ab', w=1680, h=860):
    """Full-slide recap of explicit rules and examples that teach a model."""
    c = Canvas(w, h)
    c.rect(0, 0, 820, h, fill='#F4F4F2')
    c.rect(860, 0, w - 860, h, fill=INK)

    c.text(70, 88, 'MACHINE A · RULES', size=32, color=ORANGE)
    c.text(70, 156, 'Write the test.', size=48, color=INK, mono=False)
    c.text(70, 285, 'if seat and back and legs ≥ 3:', size=29, color=INK)
    c.text(70, 334, '    return "chair"', size=29, color=INK)
    draw_chair(c, 500, 270, 270, seat_h=0.45, back_h=0.6,
               back_angle=8, seat_w=0.62, legs=4, width=6)
    c.text(70, 750, 'Exact · explainable · brittle', size=28, color=MUTED, mono=False)

    c.text(930, 88, 'MACHINE B · EXAMPLES', size=32, color=TEAL)
    c.text(930, 156, 'Learn from examples.', size=48, color=WHITE, mono=False)
    rng = random.Random(7)
    for i in range(6):
        col, row = i % 3, i // 3
        draw_chair(c, 970 + col * 220, 250 + row * 230, 150,
                   seat_h=rng.uniform(0.38, 0.55),
                   back_h=rng.uniform(0.4, 0.7),
                   back_angle=rng.uniform(0, 16),
                   seat_w=rng.uniform(0.5, 0.75),
                   legs=rng.choice([2, 4, 4]), stroke='#D3E7E8', width=4)
    c.text(930, 750, 'Patterns from labeled examples', size=28,
           color='#D3E7E8', mono=False)
    return c.finish(name)


def grammar_tree(name='w04-grammar-tree', w=1680, h=860):
    """A larger toy phrase-structure tree, explicitly distinct from Universal Grammar."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(80, 88, 'MACHINE A · A TOY GENERATIVE GRAMMAR', size=30, color=ORANGE)
    c.text(80, 154, 'Rules can generate new sentences.', size=48, color=INK, mono=False)
    c.text(840, 244, 'S → NP + VP', size=42, color=VIOLET, anchor='middle', mono=False)

    _box(c, 650, 290, 380, 100, 'SENTENCE', fill='#EEE8F5', stroke=VIOLET, size=34)
    _box(c, 310, 470, 380, 100, 'NOUN PHRASE', fill='#E8F3F2', stroke=TEAL, size=30)
    _box(c, 990, 470, 380, 100, 'VERB PHRASE', fill='#EEE8F5', stroke=VIOLET, size=30)
    for start, end in (((840, 390), (500, 454)), ((840, 390), (1180, 454)),
                       ((500, 570), (355, 650)), ((500, 570), (645, 650)),
                       ((1180, 570), (1035, 650)), ((1180, 570), (1325, 650))):
        _arrow(c, *start, *end, color=LINE, width=4, head=13)
    for x, label in ((235, 'the'), (525, 'designer'), (915, 'writes'), (1205, 'a brief')):
        _box(c, x, 660, 260, 82, label, fill=WHITE, stroke=LINE, size=30)
    c.text(840, 812, 'A teaching example of phrase structure · not a diagram of Universal Grammar.',
           size=24, color=MUTED, anchor='middle', mono=False)
    return c.finish(name)


def sentence_stack(name='w04-sentence-stack', w=1680, h=640):
    """Printable still for the live rule-based noun/verb sentence generator; no raster title."""
    c = Canvas(w, h, bg=PAPER)
    samples = [
        ('designer', 'writes', 'brief'),
        ('robot', 'studies', 'map'),
        ('archivist', 'finds', 'page'),
        ('student', 'questions', 'sentence'),
        ('agent', 'drafts', 'answer'),
        ('artist', 'redraws', 'image'),
    ]
    size, start_y, row_h, gap = 36, 55, 70, 18
    font = pil_font('semibold', round(c.s(size)))
    for i, (subject, verb, obj) in enumerate(samples):
        y = start_y + i * (row_h + gap)
        c.rect(70, y, 1540, row_h, fill=WHITE, stroke=LINE, width=2)
        c.text(100, y + 46, f'{i + 1:02}', size=20, color=MUTED, mono=True)
        x = 182
        for part, color in ((f'The {subject} ', ORANGE),
                            (f'{verb} ', DARK_TEAL),
                            (f'the {obj}.', VIOLET)):
            c.text(x, y + 48, part, size=size, color=color, mono=False)
            x += font.getlength(part) / c.scale
    return c.finish(name)


def tool_call_example(name='w04-tool-call-example', w=1680, h=860):
    """A concrete, illustrative search tool call for the visitor FAQ example."""
    c = Canvas(w, h, bg=PAPER)
    c.text(70, 78, 'A TOOL CALL · ONE STEP AT A TIME', size=28,
           color=VIOLET, mono=True)
    c.text(70, 148, 'The model requests; the harness runs the tool.', size=46,
           color=INK, mono=False)

    stages = [
        ('1 · MODEL REQUEST', 'Search the official event page',
         'for visitor time and location.', '#EEE8F5', VIOLET),
        ('2 · HARNESS RUNS IT', 'Search returns a page,',
         'a matching passage, and its URL.', '#E8F3F2', TEAL),
        ('3 · MODEL USES RESULT', 'Cite what is present.',
         'Mark a missing detail as unknown.', '#FBE8DD', ORANGE),
    ]
    xs, box_w, box_y, box_h = [70, 620, 1170], 440, 300, 290
    for i, (x, (head, line1, line2, fill, accent)) in enumerate(zip(xs, stages)):
        c.rect(x, box_y, box_w, box_h, fill=fill, stroke=accent, width=4)
        c.text(x + box_w / 2, box_y + 58, head, size=23,
               color=DARK_TEAL if accent == TEAL else accent,
               mono=True, anchor='middle')
        c.text(x + box_w / 2, box_y + 145, line1, size=27,
               color=INK, mono=False, anchor='middle')
        c.text(x + box_w / 2, box_y + 198, line2, size=25,
               color=INK, mono=False, anchor='middle')
        if i < 2:
            _arrow(c, x + box_w + 15, box_y + box_h / 2,
                   xs[i + 1] - 18, box_y + box_h / 2,
                   color=VIOLET, width=5, head=16)

    c.text(840, 710,
           'Illustrative trace · the tool returns evidence, not an answer.',
           size=29, color=INK, anchor='middle', mono=False)
    c.text(840, 765,
           'The harness exposes the tool and executes the request.',
           size=27, color=MUTED, anchor='middle', mono=False)
    return c.finish(name)


def eliza_transcript(lines, name='w04-eliza-example', w=1680, h=860):
    """A readable, two-turn ELIZA example with pattern replies highlighted."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(80, 88, 'MACHINE A · ELIZA · DOCTOR SCRIPT · 1966', size=30, color=ORANGE)
    c.text(80, 154, 'A written pattern turns a statement into a question.',
           size=44, color=INK, mono=False)

    y = 224
    for line in lines:
        match = re.fullmatch(r'\{violet:(.*)\}', line)
        is_eliza = bool(match)
        message = match.group(1) if match else line.removeprefix('> ')
        fill = '#EEE8F5' if is_eliza else WHITE
        stroke = VIOLET if is_eliza else LINE
        speaker = 'ELIZA' if is_eliza else 'PERSON'
        c.rect(100, y, 1480, 112, fill=fill, stroke=stroke, width=3)
        c.text(150, y + 69, speaker, size=24,
               color=VIOLET if is_eliza else MUTED, mono=True)
        c.text(390, y + 70, message, size=31,
               color=VIOLET if is_eliza else INK, mono=False)
        y += 142
    c.text(840, 812, 'Pattern matching can sound conversational without a model of the situation.',
           size=25, color=MUTED, anchor='middle', mono=False)
    return c.finish(name)


def rnn_steps(name='w04-rnn-steps', w=1680, h=860):
    """One full-slide RNN view: the state passed from one position to the next."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(80, 88, 'MACHINE B · RNN · RECURRENT STATE', size=30, color=ORANGE)
    c.text(80, 154, 'Read one position, then the next.', size=48, color=INK, mono=False)

    words = ['the', 'designer', 'writes', 'a', 'brief']
    xs = [80, 400, 720, 1040, 1360]
    for i, (x, word) in enumerate(zip(xs, words)):
        _box(c, x, 275, 240, 82, word, fill=WHITE, stroke=LINE, size=30)
        _box(c, x + 28, 490, 184, 116, f'h{i + 1}',
             fill='#E8F3F2', stroke=TEAL, size=40, mono=True)
        _arrow(c, x + 120, 365, x + 120, 472, color=LINE, width=4, head=14)
        if i:
            _arrow(c, xs[i - 1] + 212, 548, x + 16, 548,
                   color=TEAL, width=5, head=15)
    c.text(840, 744, 'The learned hidden state carries a summary forward.',
           size=32, color=INK, anchor='middle', mono=False)
    return c.finish(name)


def transformer_mask(name='w04-transformer-mask', w=1680, h=860):
    """A large causal-attention mask, separated from the RNN diagram for legibility."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=INK)
    c.text(80, 88, 'MACHINE B · TRANSFORMER · SELF-ATTENTION', size=30, color=TEAL)
    c.text(80, 154, 'Each position uses its earlier context.', size=48,
           color=WHITE, mono=False)

    words = ['the', 'designer', 'writes', 'a', 'brief']
    gx, gy, cell = 390, 300, 110
    for col, word in enumerate(words):
        c.text(gx + col * cell + cell / 2, 270, word, size=22,
               color=WHITE, anchor='middle', mono=False)
    for row, word in enumerate(words):
        c.text(345, gy + row * cell + 65, word, size=22,
               color=WHITE, anchor='end', mono=False)
        for col in range(5):
            fill = '#64C2C3' if col <= row else '#12263B'
            c.rect(gx + col * cell, gy + row * cell, cell - 8, cell - 8,
                   fill=fill, stroke='#657180', width=2)

    c.text(1050, 360, 'TEAL', size=30, color=TEAL, mono=True)
    c.text(1050, 405, 'Current and earlier tokens', size=26,
           color=WHITE, mono=False)
    c.text(1050, 490, 'DARK', size=30, color='#AEB7C3', mono=True)
    c.text(1050, 535, 'Future tokens are masked', size=26,
           color=WHITE, mono=False)
    c.text(1050, 660, 'Training processes positions in parallel.',
           size=28, color=WHITE, mono=False)
    c.text(1050, 715, 'GPT still generates one token at a time.',
           size=28, color=WHITE, mono=False)
    return c.finish(name)


def qa_pipeline(name='w04-qa-pipeline', w=1680, h=860):
    """A fixed retrieval-and-answer path with fewer, larger stages."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(80, 88, 'QUESTION ANSWERING · A FIXED RETRIEVAL PATH',
           size=30, color=VIOLET)
    c.text(80, 154, 'Find relevant passages, then write one answer.',
           size=44, color=INK, mono=False)

    stages = [
        ('QUESTION', 'What do I need to know?'),
        ('SEARCH', 'Look in a collection'),
        ('EVIDENCE', 'Select useful passages'),
        ('ANSWER', 'Generate with sources'),
    ]
    xs = [70, 490, 910, 1330]
    for i, (x, (head, sub)) in enumerate(zip(xs, stages)):
        c.rect(x, 330, 280, 200, fill=WHITE,
               stroke=VIOLET if i == 2 else LINE, width=4)
        c.text(x + 140, 405, head, size=30,
               color=VIOLET if i == 2 else INK, anchor='middle', mono=True)
        c.text(x + 140, 465, sub, size=23, color=MUTED,
               anchor='middle', mono=False)
        if i < len(stages) - 1:
            _arrow(c, x + 295, 430, xs[i + 1] - 18, 430,
                   color=VIOLET, width=5, head=16)
    c.text(840, 694, 'One search-and-answer pass · citations depend on the system.',
           size=30, color=INK, anchor='middle', mono=False)
    return c.finish(name)


def agent_loop(name='w04-agent-loop', w=1680, h=860):
    """A concrete visitor-FAQ example of an agent's observable tool loop."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(80, 88, 'AGENTS · THE LOOP, WITH A WORKED EXAMPLE',
           size=30, color=VIOLET)
    c.text(80, 154, 'Use the result to choose what happens next.',
           size=44, color=INK, mono=False)

    stages = [
        ('GOAL + LIMITS', '3 FAQs · event page only'),
        ('MODEL', 'choose the next step'),
        ('TOOL CALL', 'search the event page'),
        ('OBSERVATION', 'page text + URL'),
    ]
    xs = [100, 500, 900, 1300]
    for i, (x, (label, sub)) in enumerate(zip(xs, stages)):
        fill = INK if label == 'MODEL' else WHITE
        color = WHITE if label == 'MODEL' else INK
        stroke = INK if label == 'MODEL' else LINE
        c.rect(x, 330, 280, 150, fill=fill, stroke=stroke, width=4)
        c.text(x + 140, 385, label, size=25, color=color,
               anchor='middle', mono=True)
        c.text(x + 140, 435, sub, size=22,
               color=WHITE if label == 'MODEL' else MUTED,
               anchor='middle', mono=False)
        if i < len(stages) - 1:
            _arrow(c, x + 294, 405, xs[i + 1] - 18, 405,
                   color=ORANGE if label == 'TOOL CALL' else VIOLET,
                   width=5, head=16)

    c.line(1440, 480, 1440, 610, TEAL, 5)
    _arrow(c, 1440, 610, 660, 610, color=TEAL, width=5, head=16)
    _arrow(c, 660, 610, 660, 496, color=TEAL, width=5, head=16)
    c.text(1050, 682, 'Missing detail? Search again or ask. Supported? Draft and stop.',
           size=25, color=TEAL, anchor='middle', mono=False)
    c.text(840, 790, 'A person checks the source and the final draft.',
           size=28, color=INK, anchor='middle', mono=False)
    return c.finish(name)


def harness_map(name='w04-harness-map', w=1680, h=860):
    """A simplified view of the model and the controls supplied by its harness."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(80, 88, 'AGENT HARNESS · THE RUNNING SYSTEM',
           size=30, color=VIOLET)
    c.text(80, 154, 'The model is one component among several.',
           size=46, color=INK, mono=False)
    c.rect(70, 220, 1540, 550, fill='#FAFAF8', stroke=VIOLET, width=5)
    c.text(120, 278, 'HARNESS', size=28, color=VIOLET, mono=True)

    stages = [
        ('GOAL + CONTEXT', WHITE, INK),
        ('MODEL', INK, WHITE),
        ('TOOL ROUTER', WHITE, INK),
        ('SEARCH / FILES', WHITE, INK),
    ]
    xs = [130, 510, 890, 1270]
    for i, (x, (label, fill, color)) in enumerate(zip(xs, stages)):
        _box(c, x, 340, 260, 130, label, fill=fill,
             stroke=INK if fill == INK else LINE, color=color, size=25, mono=True)
        if i < len(stages) - 1:
            _arrow(c, x + 272, 405, xs[i + 1] - 18, 405,
                   color=TEAL, width=5, head=16)

    supports = [
        (120, 'MEMORY'),
        (640, 'PERMISSIONS + SANDBOX'),
        (1160, 'LOGS + HUMAN REVIEW'),
    ]
    for x, label in supports:
        _box(c, x, 565, 400, 112, label, fill=WHITE,
             stroke=LINE, size=25, mono=True)
    c.text(840, 724, 'The harness shapes what the model can see, do, and hand back.',
           size=26, color=MUTED, anchor='middle', mono=False)
    return c.finish(name)


def reflection_evidence(name='w04-reflection-evidence', w=1680, h=860):
    """A large timeline that asks students to keep evidence across five weeks."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.text(80, 88, 'THE WEEK 7 REFLECTION · COLLECT EVIDENCE AS YOU GO',
           size=30, color=VIOLET)
    c.text(80, 154, 'Choose experiments that support your argument.',
           size=44, color=INK, mono=False)
    weeks = [
        ('W2', 'rules + picture', TEAL),
        ('W3', 'text + image blend', TEAL),
        ('W4', 'language + agent', VIOLET),
        ('W5', 'image + layout', ORANGE),
        ('W6', 'sound + music', ORANGE),
    ]
    centers = [180, 510, 840, 1170, 1500]
    y = 430
    for i, ((week, label, color), x) in enumerate(zip(weeks, centers)):
        c.circle(x, y, 64, fill=color)
        c.text(x, y + 12, week, size=32, color=WHITE, anchor='middle', mono=True)
        c.text(x, y + 145, label, size=23, color=INK, anchor='middle', mono=False)
        if i < len(weeks) - 1:
            _arrow(c, x + 78, y, centers[i + 1] - 78, y,
                   color=LINE, width=5, head=16)
    c.text(840, 740, 'Save the prompt, result, revision, and an image.',
           size=32, color=INK, anchor='middle', mono=False)
    return c.finish(name)
