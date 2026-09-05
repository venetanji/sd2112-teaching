"""
Drawn figures for week 12 · Language as an interface. Every function name and every c.finish name
starts with w12_ / w12- (the generated files share one folder). Each figure explains a mechanism:

  w12_two_chatbots        the same message through a rules-based chatbot (machine A), an intent bot
                          (B sorts, A answers) and a generative one (machine B), and what each buys
  w12_eliza_rule          one ELIZA rule, step by step: keyword and rank, decomposition, the pronoun
                          swap, reassembly; NONE and MEMORY when nothing matches (Weizenbaum 1966)
  w12_agent_loop          the agent loop: goal → plan → tool → observe → … → done; read tools and
                          write tools, the confirmation valve, and the two ways it goes wrong
  w12_transparency_axes   Van Den Eede's two transparencies as two axes, with a hammer, glasses, a
                          thermometer, ELIZA and a chat assistant placed on them
  w12_turing_test         Turing's 1950 game and prediction next to the 2025 three-party result
  w12_levers              the four levers of the mediation brief's guardrails heading: before,
                          inside, at the screen, after
"""
from __future__ import annotations

import math

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
WHITE = '#FFFFFF'
PINK = '#E94D7F'
YELLOW = '#F6AD00'
TINT_TEAL, TINT_ORANGE, TINT_PINK, TINT_GRAY, TINT_YELLOW, TINT_VIOLET = '#D3E7E8', '#F9E5D6', '#F7E3E8', '#E9E9E6', '#F8DEB1', '#E5DAEB'


def _lines(c, x, y, lines, size=18, color=INK, lh=None, anchor='start', mono=True):
    lh = lh or round(size * 1.45)
    for i, t in enumerate(lines):
        c.text(x, y + i * lh, t, size=size, color=color, anchor=anchor, mono=mono)


def _dashed(c, x1, y1, x2, y2, color=MUTED, width=2, dash=10, gap=8):
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    t = 0.0
    while t < length:
        e = min(t + dash, length)
        c.line(x1 + ux * t, y1 + uy * t, x1 + ux * e, y1 + uy * e, color, width, cap='butt')
        t = e + gap


def _box(c, x, y, w, h, fill=WHITE, stroke=INK, width=2):
    c.rect(x, y, w, h, fill=fill, stroke=stroke, width=width)


def _card(c, x, y, w, h, label, lines, fill=WHITE, stroke=INK, size=17, label_color=ORANGE, text_color=INK, width=2):
    _box(c, x, y, w, h, fill, stroke, width)
    c.text(x + 14, y + 26, label, size=14, color=label_color)
    _lines(c, x + 14, y + 52, lines, size=size, color=text_color, lh=round(size * 1.35))


# ───────────────────────── 1 · the same message through three chatbots ─────────────────────────
def w12_two_chatbots(name='w12-two-chatbots', w=1680, h=560):
    c = Canvas(w, h)
    cols = [(0, 'RULES-BASED · MACHINE A', PAPER), (570, 'INTENTS · B SORTS, A ANSWERS', TINT_TEAL), (1140, 'GENERATIVE · MACHINE B', INK)]
    cw = 540
    for x, title, bg in cols:
        c.rect(x, 0, cw, 470, fill=bg)
        c.text(x + 24, 40, title, size=18, color=ORANGE if bg != INK else TEAL)
    msg = '"Where is my parcel?"'
    # column 1: keyword → tree → script
    x = 0
    _card(c, x + 24, 70, 492, 66, 'THE MESSAGE', [msg], size=18)
    _arrow(c, x + 270, 136, x + 270, 166, INK, 3, 10)
    _card(c, x + 24, 170, 492, 100, 'KEYWORD · BRANCH', ['parcel → tracking branch', 'tracking number given? no → ask'], fill=WHITE, size=17)
    _arrow(c, x + 270, 270, x + 270, 300, INK, 3, 10)
    _card(c, x + 24, 304, 492, 66, 'THE SCRIPT SAYS', ['"Please enter your tracking number."'], fill=TINT_ORANGE, size=17)
    _lines(c, x + 24, 412, ['exact · a script · a guarantee', 'brittle: no branch, no answer'], size=17, color=MUTED)
    # column 2: classifier → flow
    x = 570
    _card(c, x + 24, 70, 492, 66, 'THE MESSAGE', [msg], size=18)
    _arrow(c, x + 270, 136, x + 270, 166, INK, 3, 10)
    _card(c, x + 24, 170, 492, 100, 'A MODEL SORTS IT', ['intent = track_parcel  (0.92)', 'learned from examples: where is / status'], fill=WHITE, size=17)
    _arrow(c, x + 270, 270, x + 270, 300, INK, 3, 10)
    _card(c, x + 24, 304, 492, 66, 'A SCRIPT ANSWERS', ['"Please enter your tracking number."'], fill=TINT_ORANGE, size=17)
    _lines(c, x + 24, 412, ['B decides which branch; A speaks', 'fuzzy at the door, exact inside'], size=17, color=MUTED)
    # column 3: tokens → next token → fluent reply
    x = 1140
    _card(c, x + 24, 70, 492, 66, 'THE MESSAGE + A SYSTEM PROMPT', [msg], fill=WHITE, size=18)
    _arrow(c, x + 270, 136, x + 270, 166, WHITE, 3, 10)
    _card(c, x + 24, 170, 492, 100, 'NEXT TOKEN, AGAIN AND AGAIN', ['the likeliest continuation of', 'everything it read, in this tone'], fill=WHITE, size=17)
    _arrow(c, x + 270, 270, x + 270, 300, WHITE, 3, 10)
    _card(c, x + 24, 304, 492, 66, 'IT WRITES', ['"It left the depot at 9:40, due by 6."'], fill=TINT_PINK, size=17)
    c.text(x + 516, 392, 'invented: it never looked', size=14, color=PINK, anchor='end')
    _lines(c, x + 24, 412, ['fluent · no script · no guarantee', 'answers what it never looked up, too'], size=17, color='#D3E7E8')
    # the bottom band: the designer's version
    c.rect(0, 490, w, 70, fill=TINT_YELLOW)
    c.text(24, 518, "THE DESIGNER'S VERSION", size=16, color=INK)
    c.text(24, 545, 'rules around a model: a system prompt (A) · refusals (A) · a person for the risky cases · the fluent reply (B) inside them', size=17, color=INK)
    return c.finish(name)


# ───────────────────────── 2 · one ELIZA rule, step by step ─────────────────────────
def w12_eliza_rule(name='w12-eliza-rule', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'ELIZA · 1966 · "input sentences are analyzed on the basis of decomposition rules which are triggered by key words"', size=17, color=ORANGE)
    steps = [
        ('1 · THE INPUT', ['"I need a poster', 'for my exhibition."'], WHITE),
        ('2 · KEYWORD · RANK', ['need  rank 3  ←', 'my    rank 1', 'poster rank 2', 'the highest rank wins'], PAPER),
        ('3 · DECOMPOSITION', ['(I need) (a poster for', 'my exhibition)', 'part 1 · part 2'], WHITE),
        ('4 · THE PRONOUN SWAP', ['my → your · I → you', 'me → you · am → are', '"a poster for your', 'exhibition"'], PAPER),
        ('5 · REASSEMBLY', ['"What should [part 2]', 'do for the people who', 'see it?"'], TINT_ORANGE),
    ]
    bw, bh, y0 = 296, 190, 70
    for i, (label, lines, fill) in enumerate(steps):
        x = i * 346
        _card(c, x, y0, bw, bh, label, lines, fill=fill, size=17)
        if i < 4:
            _arrow(c, x + bw + 6, y0 + bh / 2, x + 342, y0 + bh / 2, INK, 3, 10)
    # the output line
    c.rect(0, 290, w, 60, fill=INK)
    c.text(24, 327, 'ELIZA:  What should a poster for your exhibition do for the people who see it?', size=22, color=WHITE)
    # when nothing matches
    _card(c, 0, 380, 520, 150, 'NONE · NO KEYWORD FOUND', ['a content-free remark from the script:', '"Please go on."  "What does that', 'suggest to you?"  "I see."'], fill=PAPER, size=17)
    _card(c, 560, 380, 560, 150, 'MEMORY · SOMETHING YOU SAID ABOUT "MY"', ['stored when "my" is the keyword, used', 'later when nothing matches:', '"Earlier you said your exhibition …"'], fill=PAPER, size=17)
    _card(c, 1160, 380, 520, 150, 'THE SCRIPT IS DATA', ['"a script is data; i.e., it is not part', 'of the program itself." Change the', 'rules, keep the machine. Machine A.'], fill=TINT_TEAL, size=17)
    return c.finish(name)


# ───────────────────────── 3 · the agent loop ─────────────────────────
def w12_agent_loop(name='w12-agent-loop', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'AN AGENT IS A MODEL IN A LOOP', size=18, color=ORANGE)
    c.text(w - 8, 30, 'ReAct, 2022: reason and act, interleaved · the tools are machine A, the plan is machine B', size=15, color=MUTED, anchor='end')
    # goal
    _card(c, 0, 70, 330, 120, 'THE GOAL · IN WORDS', ['"Book a room for four', 'on Thursday."'], fill=PAPER, size=18)
    _arrow(c, 336, 130, 420, 130, INK, 3, 10)
    # the loop: three nodes on a ring
    cx, cy, r = 720, 200, 120
    nodes = [('PLAN', (cx, cy - r), WHITE, INK), ('TOOL', (cx + r * 0.95, cy + r * 0.55), ORANGE, INK), ('OBSERVE', (cx - r * 0.95, cy + r * 0.55), TEAL, INK)]
    for i, (lab, (nx, ny), fill, col) in enumerate(nodes):
        c.circle(nx, ny, 52, fill=fill, stroke=INK, width=3)
        c.text(nx, ny + 7, lab, size=17, color=col, anchor='middle')

    def arc_arrow(a0, a1):
        pts = [(cx + (r + 8) * math.cos(math.radians(a)), cy + (r + 8) * math.sin(math.radians(a))) for a in range(int(a0), int(a1), 4)]
        for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
            c.line(xa, ya, xb, yb, INK, 3, cap='round')
        (xa, ya), (xb, yb) = pts[-2], pts[-1]
        _arrow(c, xa, ya, xb, yb, INK, 3, 12)
    arc_arrow(-62, 4)      # plan -> tool
    arc_arrow(64, 116)     # tool -> observe
    arc_arrow(184, 240)    # observe -> plan
    c.text(cx, cy + 12, 'again, until', size=15, color=MUTED, anchor='middle')
    c.text(cx, cy + 32, 'done or stopped', size=15, color=MUTED, anchor='middle')
    c.text(cx + 170, cy - 100, 'the model writes the next step', size=15, color=MUTED)
    c.text(cx + 170, cy - 80, 'from the goal and the trace so far', size=15, color=MUTED)
    # exit
    _arrow(c, cx + r + 60, cy + 66, 1030, cy + 66, INK, 3, 10)
    _card(c, 1040, cy + 10, 220, 110, 'DONE', ['"Booked V502,', 'Thursday 14:00."'], fill=INK, stroke=INK, size=17, text_color=WHITE, label_color=TEAL)
    # tools: read and write, and the valve
    _card(c, 1300, 70, 380, 140, 'READ TOOLS · SAFE TO RETRY', ['search_rooms · check_calendar', 'read a page · run a calculation', 'exact, checkable, nothing changes'], fill=PAPER, size=16)
    _card(c, 1300, 240, 380, 140, 'WRITE TOOLS · THEY ACT FOR YOU', ['book · send · pay · delete', 'the world changes, and so does', 'who answers for it'], fill=TINT_PINK, size=16)
    c.rect(1300, 380, 380, 50, fill=YELLOW)
    c.text(1490, 411, 'CONFIRM? · a person before every write', size=15, color=INK, anchor='middle')
    # the two ways it goes wrong, tied to the node they hit
    _card(c, 0, 240, 330, 130, 'IT DOES WHAT YOU SAID', ['"for four": four people, or', 'four o\'clock? The plan picks', 'one and never asks.'], fill=TINT_ORANGE, size=16)
    _card(c, 0, 390, 330, 140, 'AND WHAT THE PAGE SAID', ['a tool result is text, and text', 'can carry orders for the model:', 'indirect prompt injection, 2023'], fill=TINT_ORANGE, size=15)

    def tie(x1, y1, node, pad=62):
        nx, ny = node
        dx, dy = nx - x1, ny - y1
        d = math.hypot(dx, dy)
        _dashed(c, x1, y1, nx - dx / d * pad, ny - dy / d * pad, MUTED, 2)
    tie(330, 300, nodes[0][1])
    tie(330, 455, nodes[2][1])
    # the log
    c.rect(420, 470, 800, 60, fill=PAPER)
    c.text(440, 507, 'THE LOG: every plan, call and result, kept — the audit trail the last chapter asks for', size=16, color=INK)
    return c.finish(name)


# ───────────────────────── 4 · two transparencies, two axes ─────────────────────────
def w12_transparency_axes(name='w12-transparency-axes', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'VAN DEN EEDE · 2011 · "an essential contradiction between transparency of \'use\' and transparency of social origins and effects"', size=17, color=ORANGE)
    x0, x1, y0, y1 = 60, 1000, 90, 500
    # the dangerous corner, under everything
    c.rect(x1 - 280, y1 - 200, 280, 200, fill=TINT_PINK)
    c.text(x1 - 10, y1 - 10, 'the corner to design out of', size=14, color=PINK, anchor='end')
    # axes
    c.line(x0, y1, x1, y1, INK, 3, cap='butt'); _arrow(c, x1 - 20, y1, x1 + 10, y1, INK, 3, 12)
    c.line(x0, y1, x0, y0, INK, 3, cap='butt'); _arrow(c, x0, y0 + 20, x0, y0 - 10, INK, 3, 12)
    c.text(x0, y1 + 34, 'OPAQUE IN USE · you look at it', size=15, color=MUTED)
    c.text(x1, y1 + 34, 'TRANSPARENT IN USE · you look through it', size=15, color=MUTED, anchor='end')
    c.text(x0 + 16, y0 + 6, 'ORIGINS AND EFFECTS VISIBLE', size=14, color=MUTED)
    c.text(x0 + 16, y1 - 12, 'ORIGINS AND EFFECTS HIDDEN', size=14, color=MUTED)

    def dot(x, y, label, sub, fill=INK, col=INK):
        c.circle(x, y, 12, fill=fill)
        c.text(x + 18, y + 6, label, size=17, color=col)
        c.text(x + 18, y + 28, sub, size=14, color=MUTED)

    dot(880, 140, 'a hammer', 'Heidegger 1927: in use it withdraws', fill=INK)
    dot(960, 230, 'glasses', 'Ihde 1990: embodiment', fill=TEAL)
    dot(440, 190, 'a thermometer', 'hermeneutic: you read it off the scale', fill=TEAL)
    dot(240, 290, 'a menu bot', 'shows every branch; the script is the product', fill=ORANGE)
    dot(380, 355, 'ELIZA', 'talks like a person; the script is readable data', fill=ORANGE)
    dot(900, 425, 'a chat assistant', 'data, prompt and objective unseen', fill=PINK, col=PINK)
    # the moves out of the corner
    _arrow(c, 882, 425, 700, 425, ORANGE, 3, 12)
    c.text(640, 413, 'say "I am an AI" · hand over', size=14, color=ORANGE)
    _arrow(c, 900, 407, 900, 300, ORANGE, 3, 12)
    c.text(886, 340, '"why this answer" · the rule that fired', size=14, color=ORANGE, anchor='end')
    # legend on the right
    _card(c, 1210, 90, 470, 200, 'TRANSPARENT IS NOT EXPLAINED', ['A tool that disappears in use is', 'transparent in the first sense and', 'usually opaque in the second. A chat', 'assistant is built to disappear.'], fill=PAPER, size=16)
    _card(c, 1210, 320, 470, 180, "THE DESIGNER'S DIAL", ['Where does it show itself, and', 'when? At the first message, at a', 'refusal, before a purchase, on', 'request. Next slide: a dial to move.'], fill=TINT_TEAL, size=16)
    return c.finish(name)


# ───────────────────────── 5 · the Turing test, 1950 and 2025 ─────────────────────────
def w12_turing_test(name='w12-turing-test', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'TURING · 1950 · THE IMITATION GAME', size=18, color=ORANGE)
    c.text(900, 30, 'JONES & BERGEN · 2025 · THE SAME GAME, 5 MINUTES, 3 PARTIES', size=18, color=ORANGE)
    # left: C questions A and B through a wall
    _box(c, 40, 80, 200, 110, PAPER, INK, 2)
    c.text(140, 128, 'C', size=34, color=INK, anchor='middle')
    c.text(140, 160, 'the interrogator', size=14, color=MUTED, anchor='middle')
    c.rect(400, 60, 8, 260, fill=INK)
    c.text(404, 345, 'a wall · teleprinter only', size=14, color=MUTED, anchor='middle')
    _box(c, 560, 60, 200, 100, ORANGE, INK, 2)
    c.text(660, 104, 'A', size=34, color=INK, anchor='middle')
    c.text(660, 138, 'a machine', size=14, color=INK, anchor='middle')
    _box(c, 560, 200, 200, 100, TEAL, INK, 2)
    c.text(660, 244, 'B', size=34, color=INK, anchor='middle')
    c.text(660, 278, 'a person', size=14, color=INK, anchor='middle')
    _arrow(c, 246, 120, 552, 108, INK, 3, 10)
    _arrow(c, 246, 150, 552, 248, INK, 3, 10)
    c.text(300, 52, 'which one is the person?', size=14, color=MUTED)
    _lines(c, 40, 390, ['"an average interrogator will not have more than', '70 per cent chance of making the right identification', 'after five minutes of questioning" — his bet for the', 'year 2000. The question "Can machines think?" he called', '"too meaningless to deserve discussion."'], size=16, color=INK, lh=25)
    # right: the 2025 bars
    bx, by, bw, bh = 900, 70, 740, 300
    rows = [('GPT-4.5, told to act human', 73, PINK), ('LLaMa-3.1-405B, same prompt', 56, ORANGE), ('ELIZA, 1966 rules', 23, INK), ('GPT-4o, no persona', 21, MUTED)]
    scale = (bw - 300) / 100
    for i, (lab, pct, col) in enumerate(rows):
        y = by + i * 66
        c.text(bx, y + 28, lab, size=16, color=INK)
        c.rect(bx + 300, y + 8, pct * scale, 30, fill=col)
        c.text(bx + 306 + pct * scale, y + 30, f'{pct}%', size=16, color=INK)
    chance = bx + 300 + 50 * scale
    _dashed(c, chance, by - 10, chance, by + 4 * 66, MUTED, 2)
    c.text(chance, by - 16, 'chance: 50%', size=14, color=MUTED, anchor='middle')
    c.text(bx, 348, '"judged to be the human … % of the time": the judges chose the machine over the real person', size=14, color=MUTED)
    _lines(c, bx, 390, ['The test measures the judge, not the machine. When the', 'judge loses to a persona prompt, "passing" is a design', 'fact, not a proof of thought — and the law answers it:', 'from 2 August 2026 an EU chatbot must say what it is.'], size=16, color=INK, lh=25)
    return c.finish(name)


# ───────────────────────── 6 · four levers on the guardrails heading ─────────────────────────
def w12_levers(name='w12-levers', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, "THE GUARDRAILS HEADING OF THE MEDIATION BRIEF · FOUR PLACES TO WORK", size=18, color=ORANGE)
    c.text(w, 30, 'before · inside · at the screen · after', size=16, color=MUTED, anchor='end')
    stations = [
        ('BEFORE · PARTICIPATORY DESIGN', TINT_TEAL, ['design with the people the model', 'decides about, not for them', '· who is in the room when the', '  decision is written?', '· NJMF 1970s · UTOPIA 1981–86', '· Charlton 1998: "nothing about', '  us without us"']),
        ('INSIDE · GUARDRAILS', TINT_YELLOW, ['rules around the model', '· the system prompt: may, never,', '  when unsure', '· refusals: the rule that says no', '· a person before every write:', '  Operator 2025 asks before it', '  buys, sends or deletes']),
        ('AT THE SCREEN · EXPLAINABILITY', TINT_ORANGE, ['the moment it shows itself', '· "I am an AI": Article 50, 2026', '· "why am I seeing this":', '  Facebook 2019, TikTok 2022', '· the rule that fired, on request', '· a model\'s "because" is another', '  generation: show data, not prose']),
        ('AFTER · AUDITING', TINT_PINK, ['evidence that it does what the', 'brief says, kept and checked', '· the log of every decision', '· red-teaming: DEF CON, 2023', '· the bias register, in use', '· model cards 2019 · a bias audit', '  by law: New York, 2023']),
    ]
    bw, gap, y0, bh = 390, 40, 70, 380
    asks = [['IN THE BRIEF: who you asked,', 'and what they changed'], ['IN THE BRIEF: three mays, three', 'nevers, one handover'], ['IN THE BRIEF: the sentence the', 'person reads when it decides'], ['IN THE BRIEF: what you log, who', 'reads it, how often']]
    for i, (label, fill, lines) in enumerate(stations):
        x = i * (bw + gap)
        c.rect(x, y0, bw, bh, fill=fill)
        c.text(x + 20, y0 + 34, label, size=15, color=INK)
        _lines(c, x + 20, y0 + 72, lines, size=16, color=INK, lh=24)
        c.rect(x + 20, y0 + bh - 90, bw - 40, 2, INK)
        _lines(c, x + 20, y0 + bh - 58, asks[i], size=15, color=ORANGE, lh=22)
        if i < 3:
            _arrow(c, x + bw + 6, y0 + bh / 2, x + bw + gap - 6, y0 + bh / 2, INK, 3, 10)
    c.rect(0, 480, w, 60, fill=INK)
    c.text(24, 517, 'One paragraph each in the brief: who was in the room · what the rules say · where it shows itself · what you check after launch', size=17, color=WHITE)
    return c.finish(name)


if __name__ == '__main__':
    for fn in (w12_two_chatbots, w12_eliza_rule, w12_agent_loop, w12_transparency_axes, w12_turing_test, w12_levers):
        svg, png = fn()
        print(png, len(svg))
