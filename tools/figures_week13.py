"""
Drawn figures for week 13 · Poster fair and final quiz. Every function name and every
c.finish name starts with w13_ / w13- (the generated files share one folder). Each figure
explains a mechanism of the last class rather than decorating it: the room and its two
halves, the four rounds and where the feedback goes, how the forty percent is decided,
the four human–technology relations recapped, the map of the arguments on the course
question, and how the final quiz runs on ClassPoint and on Blackboard.
"""
from __future__ import annotations

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
TINT_TEAL, TINT_VIOLET, TINT_ORANGE, TINT_YELLOW, TINT_GRAY, TINT_PINK = '#D3E7E8', '#E5DAEB', '#F9E5D6', '#F8DEB1', '#E9E9E6', '#F7E3E8'
RED = '#E42519'
TEAMS = 26                      # the working number: set it from the Blackboard group list and rebuild (the deck, the
                                # figures and the fair clock's default all read it); the clock's [ and ] change it on the day
HALF = (TEAMS + 1) // 2         # teams 1–HALF are half A, the rest half B


def _lines(c, x, y, lines, size=18, color=INK, lh=None, anchor='start'):
    """A few short mono lines, top-left at (x, y)."""
    lh = lh or round(size * 1.45)
    for i, t in enumerate(lines):
        c.text(x, y + i * lh, t, size=size, color=color, anchor=anchor)


def _box(c, x, y, w, h, title, lines, fill=PAPER, stroke=None, title_color=INK, size=17, lh=None):
    c.rect(x, y, w, h, fill=fill, stroke=stroke, width=2)
    c.text(x + 20, y + 36, title, size=19, color=title_color)
    _lines(c, x + 20, y + 68, lines, size=size, color=MUTED, lh=lh)


# ───────────────────────── the room: boards on three walls, two halves, one screen ─────────────────────────
def w13_room(name='w13-room', w=1680, h=560):
    """The fair's room: TEAMS numbered boards along three walls, half A (1–HALF) and half B (the rest),
    a laptop with the video at every board, the screen with the clock, the desk with the grading sheets."""
    c = Canvas(w, h)
    rx, ry, rw, rh = 200, 80, 1280, 440
    c.rect(rx, ry, rw, rh, fill='#FFFFFF', stroke=INK, width=3)
    # the door: a gap in the front wall, top left
    c.rect(rx + 40, ry - 3, 70, 6, fill='#FFFFFF')
    c.text(rx + 75, ry + 22, 'door', size=13, color=MUTED, anchor='middle')
    # the screen, front wall centre
    c.rect(rx + rw / 2 - 130, ry - 4, 260, 14, fill=INK)
    c.text(rx + rw / 2, ry + 34, 'THE SCREEN · THE CLOCK · THE FEEDBACK WALL', size=15, color=INK, anchor='middle')
    # the desk
    c.rect(rx + 160, ry + 24, 150, 44, fill=PAPER, stroke=INK, width=2)
    c.text(rx + 235, ry + 44, 'THE DESK', size=14, color=INK, anchor='middle')
    c.text(rx + 235, ry + 62, 'sheets · chargers', size=12, color=MUTED, anchor='middle')

    def board(n, x, y, vertical):
        tint = TINT_TEAL if n <= HALF else TINT_ORANGE
        edge = TEAL if n <= HALF else ORANGE
        if vertical:
            c.rect(x, y, 22, 34, fill=tint, stroke=edge, width=2)
            c.rect(x + 4, y + 38, 14, 8, fill=INK)          # the laptop, under the board
        else:
            c.rect(x, y, 44, 22, fill=tint, stroke=edge, width=2)
            c.rect(x + 48, y + 8, 14, 8, fill=INK)          # the laptop, beside the board

    side = max(1, round(TEAMS * 8 / 26))       # boards on each side wall (8 of 26); the rest along the back wall
    back = TEAMS - 2 * side
    step_v = min(42, (rh - 100) / side)        # the spacing gives way when the count grows
    step_h = min(112, (rw - 250) / max(1, back))
    # left wall: 1 to side, top to bottom
    for i in range(side):
        y = ry + 86 + i * step_v
        board(i + 1, rx + 8, y, True)
        c.text(rx + 40, y + 24, str(i + 1), size=16, color=INK)
    # back wall: the middle of the list, left to right
    for i in range(back):
        x = rx + 120 + i * step_h
        board(side + i + 1, x, ry + rh - 30, False)
        c.text(x + 22, ry + rh - 40, str(side + i + 1), size=16, color=INK, anchor='middle')
    # right wall: the last boards, bottom to top
    for i in range(side):
        y = ry + 86 + (side - 1 - i) * step_v
        board(side + back + i + 1, rx + rw - 30, y, True)
        c.text(rx + rw - 40, y + 24, str(side + back + i + 1), size=16, color=INK, anchor='end')
    # the legend and the flow, in the middle of the room
    c.rect(rx + 300, ry + 110, 22, 22, fill=TINT_TEAL, stroke=TEAL, width=2)
    c.text(rx + 336, ry + 128, f'HALF A · TEAMS 1 – {HALF} · PRESENT IN ROUNDS 1 AND 3', size=17, color=INK)
    c.rect(rx + 300, ry + 150, 22, 22, fill=TINT_ORANGE, stroke=ORANGE, width=2)
    c.text(rx + 336, ry + 168, f'HALF B · TEAMS {HALF + 1} – {TEAMS} · PRESENT IN ROUNDS 2 AND 4', size=17, color=INK)
    c.rect(rx + 300, ry + 190, 22, 22, fill=INK)
    c.text(rx + 336, ry + 208, 'A LAPTOP AT EVERY BOARD · THE VIDEO LOOPS · A QR CODE ON THE POSTER', size=17, color=INK)
    _arrow(c, rx + 880, ry + 248, rx + 420, ry + 248, ORANGE, 4, 12)
    c.text(rx + 650, ry + 236, 'rounds 1 and 3: B walks to A', size=15, color=MUTED, anchor='middle')
    _arrow(c, rx + 420, ry + 286, rx + 880, ry + 286, TEAL, 4, 12)
    c.text(rx + 650, ry + 314, 'rounds 2 and 4: A walks to B', size=15, color=MUTED, anchor='middle')
    _lines(c, rx + 300, ry + 350, ['one presenter at the board at all times; the others visit',
                                   'two of us grade every board over the fair, a sheet each; the peer wall grows on the screen'], size=15, color=MUTED, lh=22)
    c.text(20, 34, f'THE ROOM · {TEAMS} BOARDS ON THREE WALLS · TWO HALVES', size=18, color=ORANGE)
    c.text(w - 20, 34, 'team numbers as on the Blackboard group list · 30 minutes before class: posters up, videos playing', size=15, color=MUTED, anchor='end')
    c.text(w / 2, 552, f'A plan for {TEAMS} teams, not a survey of the room: the TAs tape the real numbers to the boards before the doors open.', size=15, color=MUTED, anchor='middle')
    return c.finish(name)


# ───────────────────────── four rounds, two passes ─────────────────────────
def w13_rotation(name='w13-rotation', w=1680, h=560):
    """The fair as a timeline: four rounds of twelve minutes, who presents and who visits, the two sheets every
    team gets from two different graders, and the ClassPoint activities that stay open across the rounds."""
    c = Canvas(w, h)
    x0, span = 250, 1370                     # bars from x0; 61 minutes across
    ppm = span / 61
    blocks = [(0, 12, 'r1'), (12, 14, 'swap'), (14, 26, 'r2'), (26, 28, 'swap'), (28, 40, 'r3'), (40, 42, 'swap'), (42, 54, 'r4'), (54, 61, 'prize')]
    rows = [(f'TEAMS 1 – {HALF}', 'HALF A'), (f'TEAMS {HALF + 1} – {TEAMS}', 'HALF B'), ('FIVE GRADERS', 'TWO SHEETS PER TEAM'), ('CLASSPOINT', 'ON THE SCREEN')]
    ys = [96, 186, 276, 366]
    bh = 64
    for (label, sub), y in zip(rows, ys):
        c.text(40, y + 30, label, size=17, color=INK)
        c.text(40, y + 52, sub, size=14, color=MUTED)
    for s0, s1, kind in blocks:
        bx, bw = x0 + s0 * ppm, (s1 - s0) * ppm - 4
        r = int(kind[1]) if kind.startswith('r') else 0
        a_presents = r in (1, 3)
        if kind.startswith('r'):
            c.rect(bx, ys[0], bw, bh, fill=TINT_TEAL if a_presents else PAPER)
            c.text(bx + 12, ys[0] + 28, 'present' if a_presents else 'visit', size=17, color=INK)
            c.text(bx + 12, ys[0] + 50, 'at the board, one talks' if a_presents else 'four posters, three min each', size=13, color=MUTED)
            c.rect(bx, ys[1], bw, bh, fill=PAPER if a_presents else TINT_ORANGE)
            c.text(bx + 12, ys[1] + 28, 'visit' if a_presents else 'present', size=17, color=INK)
            c.text(bx + 12, ys[1] + 50, 'four posters, three min each' if a_presents else 'at the board, one talks', size=13, color=MUTED)
            c.rect(bx, ys[2], bw, bh, fill=TINT_VIOLET)
            c.text(bx + 12, ys[2] + 28, ('A' if a_presents else 'B') + (': first sheet' if r <= 2 else ': second sheet'), size=17, color=INK)
            c.text(bx + 12, ys[2] + 50, 'one of us a board, 4 min each' if r <= 2 else 'a different one of us', size=13, color=MUTED)
            c.text(bx + bw / 2, 82, f'ROUND {r} · 12 MIN', size=15, color=ORANGE, anchor='middle')
        elif kind == 'swap':
            for y in ys[:3]:
                c.rect(bx, y, bw, bh, fill=TINT_GRAY)
            c.text(bx + bw / 2, 82, 'swap', size=13, color=MUTED, anchor='middle')
        else:
            c.rect(bx, ys[3], bw, bh, fill=TINT_ORANGE)
            c.text(bx + 12, ys[3] + 28, 'the prize', size=17, color=INK)
            c.text(bx + 12, ys[3] + 50, 'upload · cloud · vote', size=13, color=MUTED)
            c.text(bx + bw / 2, 82, 'PRIZE · 7 MIN', size=15, color=ORANGE, anchor='middle')
    # the short answer stays open through the four rounds
    fx, fw = x0, 54 * ppm - 4
    c.rect(fx, ys[3], fw, bh, fill=TINT_ORANGE)
    c.text(fx + 12, ys[3] + 28, 'short answer, open the whole time: "team number · one strength · one question", one line per poster visited', size=15, color=INK)
    c.text(fx + 12, ys[3] + 50, 'names hidden · multiple submissions · exported after class for the grading meeting and forwarded to every team', size=13, color=MUTED)
    c.text(40, 34, 'FOUR ROUNDS · TWO PASSES · EVERYONE PRESENTS TWICE AND VISITS TWICE', size=18, color=ORANGE)
    c.text(w - 20, 34, 'twelve minutes a round; the clock on the screen says which half, and rings a drawn bell', size=15, color=MUTED, anchor='end')
    _lines(c, 40, 470, ['The second pass is not a repeat: visitors go to the posters they missed, a different presenter talks, and a different grader comes to every board.',
                        'Between rounds: two minutes. The TAs call the swap when the bell shows; nobody moves before it. Two sheets per team go to the grading meeting.'], size=16, color=INK, lh=26)
    return c.finish(name)


# ───────────────────────── how the forty percent is decided ─────────────────────────
def w13_grading(name='w13-grading', w=1680, h=560):
    """What is read (poster, video, brief, log), the five criteria and their weights, and the path from the
    graders' sheets to the marks and the notes on Blackboard."""
    c = Canvas(w, h)
    c.text(20, 34, 'FORTY PERCENT · FOUR THINGS WE READ · FIVE CRITERIA · ONE MEETING', size=18, color=ORANGE)
    c.text(w - 20, 34, 'the rubric bands (A, B, C) are in the syllabus on the site and on Blackboard', size=15, color=MUTED, anchor='end')
    # what is read
    c.text(40, 74, 'WHAT IS READ', size=16, color=MUTED)
    reads = [('THE POSTER', 'A0, at the fair', TINT_TEAL), ('THE VIDEO', '3 to 5 min, on the laptop', TINT_TEAL),
             ('THE BRIEF', 'one page, on Blackboard', TINT_ORANGE), ('THE LOG', 'who did what, on Blackboard', TINT_GRAY)]
    ry = [92, 200, 308, 416]
    for (t, sub, tint), y in zip(reads, ry):
        c.rect(40, y, 300, 84, fill=tint)
        c.text(60, y + 36, t, size=19, color=INK)
        c.text(60, y + 62, sub, size=15, color=MUTED)
    # the rubric
    c.text(560, 74, 'THE RUBRIC · 40 %', size=16, color=MUTED)
    crit = [('RESEARCH AND CONTEXT', '30', PAPER), ('ETHICAL AND SOCIAL IMPACT', '30', TINT_ORANGE),
            ('POSTER DESIGN', '20', PAPER), ('VIDEO', '10', PAPER), ('TEAM AND PROCESS', '10', PAPER)]
    cy = [88, 178, 268, 358, 448]
    for (t, pct, fill), y in zip(crit, cy):
        c.rect(560, y, 360, 70, fill=fill)
        c.text(580, y + 44, t, size=17, color=INK)
        c.text(902, y + 46, pct, size=26, color=ORANGE, anchor='end')
    # who feeds what
    for i, j in ((0, 0), (0, 2), (1, 3), (2, 1), (2, 0), (3, 4)):
        c.line(340, ry[i] + 42, 560, cy[j] + 35, LINE, 3, cap='butt')
    # the path
    c.text(1120, 74, 'HOW IT IS DECIDED', size=16, color=MUTED)
    steps = [('AT THE FAIR', ['two of us at every board, a sheet each:', 'a band and a line per criterion, a note']),
             ('THE GRADING MEETING', ['the two sheets side by side; the video', 'and the brief read again; the peer wall read']),
             ('ON BLACKBOARD', ['the mark, and a paragraph per team:', 'two strengths, one thing to fix'])]
    sy = [92, 236, 380]
    for (t, lines), y in zip(steps, sy):
        c.rect(1120, y, 520, 108, fill=PAPER, stroke=INK, width=2)
        c.text(1140, y + 36, t, size=19, color=INK)
        _lines(c, 1140, y + 66, lines, size=15, color=MUTED, lh=22)
        if y != sy[-1]:
            _arrow(c, 1380, y + 110, 1380, y + 140, INK, 3, 10)
    _arrow(c, 924, 268, 1116, 146, INK, 3, 10)
    c.text(1120, 520, 'peer feedback and the prize are read at the meeting;', size=15, color=MUTED)
    c.text(1120, 542, 'the rubric decides the mark', size=15, color=MUTED)
    return c.finish(name)


# ───────────────────────── mediation, recapped: four relations, the AI version of each ─────────────────────────
def w13_mediation(name='w13-mediation', w=1680, h=560):
    """You – technology – world, and Ihde's four relations (the examples are Ihde's classic cases and Verbeek's 2015 ones,
    as week 5 gave them) with the AI product that builds each and its risk."""
    c = Canvas(w, h)
    y = 78
    c.circle(300, y, 44, fill=TEAL); c.text(300, y + 7, 'YOU', size=18, color=INK, anchor='middle')
    c.rect(720, y - 34, 240, 68, fill=ORANGE); c.text(840, y + 7, 'TECHNOLOGY', size=18, color=INK, anchor='middle')
    c.circle(1380, y, 44, fill=VIOLET); c.text(1380, y + 7, 'WORLD', size=18, color='#FFFFFF', anchor='middle')
    c.line(350, y, 712, y, INK, 4, cap='butt'); c.line(968, y, 1330, y, INK, 4, cap='butt')
    c.text(531, y - 18, 'perceives through', size=15, color=MUTED, anchor='middle')
    c.text(1149, y - 18, 'acts on', size=15, color=MUTED, anchor='middle')
    c.text(40, 34, 'IHDE 1990 · VERBEEK 2015 · THE THING IN BETWEEN CHANGES WHAT YOU SEE AND WHAT YOU DO', size=18, color=ORANGE)
    cols = [('EMBODIMENT', 'through it', '(you – tech) → world', 'glasses; a cane',
             ['Generative Fill, autocomplete:', 'it withdraws into the tool.'], 'you forget it decides', TINT_TEAL),
            ('HERMENEUTIC', 'off it', 'you → (tech – world)', 'a thermometer; a map',
             ['a feed, a summary, a chosen poster:', 'you read the world off a screen.'], 'the picture for the world', TINT_VIOLET),
            ('ALTERITY', 'facing it', 'you → tech (world)', 'an ATM; a robot',
             ['a chatbot, an assistant: you brief', 'it, argue with it, thank it.'], 'a quasi-other for a person', TINT_ORANGE),
            ('BACKGROUND', 'around you', 'you (– tech / world)', 'the heating; a fridge hum',
             ['a filter, a ranking, a default:', 'nobody sees the choice being made.'], 'nobody is accountable', TINT_GRAY)]
    for i, (t, short, schema, ex, ai, risk, tint) in enumerate(cols):
        x = 40 + i * 410
        c.rect(x, 150, 380, 340, fill=tint)
        c.text(x + 22, 188, t, size=20, color=INK)
        c.text(x + 358, 188, short, size=17, color=ORANGE, anchor='end')
        c.text(x + 22, 222, schema, size=16, color=MUTED)
        c.text(x + 22, 262, 'EXAMPLES: ' + ex, size=15, color=INK)
        c.text(x + 22, 306, 'THE AI VERSION', size=14, color=MUTED)
        _lines(c, x + 22, 334, ai, size=16, color=INK, lh=24)
        c.text(x + 22, 410, 'THE RISK', size=14, color=MUTED)
        c.text(x + 22, 438, risk, size=16, color=INK)
        c.text(x + 22, 470, 'week 5 · the mediation brief', size=13, color=MUTED)
    c.text(w / 2, 536, 'Same model, four products, four relations. The brief asked which one you built, and how hard it pushes: hidden or apparent, weak or strong.', size=16, color=INK, anchor='middle')
    return c.finish(name)


# ───────────────────────── the course question: the arguments, three columns ─────────────────────────
def w13_question_map(name='w13-question-map', w=1680, h=560):
    """Can a machine originate a design? The arguments the course gave for no, for yes, and for 'it depends on who chose'."""
    c = Canvas(w, h)
    c.text(40, 34, 'CAN A MACHINE ORIGINATE A DESIGN? · ASKED IN WEEK 1, IN WEEK 12, AND TODAY', size=18, color=ORANGE)
    c.text(w - 20, 34, 'the arguments the course gave you, by week', size=15, color=MUTED, anchor='end')
    cols = [('NO', INK, TINT_GRAY,
             [('LOVELACE · 1843 · AS TURING QUOTED HER, 1950', ['"It can do whatever we know how', 'to order it to perform."']),
              ('WEEK 2 · THE RULE', ['the rule is all there is; nothing', 'outside it can ever appear']),
              ('WEEKS 1 · 3 · 5 · THE MIDDLE', ['ask for the edge, get the middle:', 'a model pulls towards the typical']),
              ('WEEK 9 · THE DATA', ['it learns the world it was shown,', 'and whoever labelled it'])]),
            ('YES', TEAL, TINT_TEAL,
             [('TURING · 1950', ['"Machines take me by surprise', 'with great frequency."']),
              ('WEEK 3 · MOVE 37', ['10 March 2016: a move most professionals', 'would not have considered — and it won']),
              ('WEEK 1 · WIGGINS · 2006', ['judge the output, not the process:', 'if a person did it, we would call it creative']),
              ('WEEK 2 · THE SPEC', ['it did what you said, not what you', 'meant — and sometimes that was better'])]),
            ('IT DEPENDS WHO CHOSE', ORANGE, TINT_ORANGE,
             [('LEWITT · 1967', ['the idea becomes a machine that', 'makes the art; the design is the rule']),
              ('WEEK 11 · BELAMY · 2018', ['a network painted; a person picked;', 'the pick was the authorship']),
              ('WEEKS 11 · 12 · THE TURN', ['curator, briefer, guardrail-setter:', 'the machine makes, you decide what ships']),
              ('THE PROCESS NOTE', ['say which decisions were yours;', 'that sentence is where the author is'])])]
    for i, (t, col, tint, items) in enumerate(cols):
        x = 40 + i * 550
        c.rect(x, 60, 520, 440, fill=tint)
        c.text(x + 24, 100, t, size=24, color=col)
        for k, (head, lines) in enumerate(items):
            y = 140 + k * 90
            c.text(x + 24, y, head, size=14, color=MUTED)
            _lines(c, x + 24, y + 26, lines, size=16, color=INK, lh=23)
    c.text(w / 2, 540, 'Any of the three can be defended. The reflection and the poster were marked on the defence, not on the side. The quiz does not ask this question.', size=16, color=INK, anchor='middle')
    return c.finish(name)


# ───────────────────────── the final quiz: two lanes ─────────────────────────
def w13_quiz_flow(name='w13-quiz-flow', w=1680, h=520):
    """How the final runs: the ClassPoint lane (the plan) and the Blackboard lane (the fallback), as in week 7."""
    c = Canvas(w, h)
    bw, bh, step = 290, 128, 330
    c.text(20, 34, 'THE PLAN · CLASSPOINT · QUIZ MODE · ONE QUESTION AT A TIME, ON SCREEN', size=18, color=ORANGE)
    lane1 = [('JOIN', ['the class code on screen', 'your ID, e.g. 3456A', 'phone or laptop browser']),
             ('A QUESTION', ['one idea, four choices', 'on the big screen', 'and on your phone']),
             ('ANSWER', ['about a minute', 'then it closes', 'no going back']),
             ('THIRTY TIMES', ['weeks 1 to 12', 'and the playlist', 'in course order']),
             ('AUTO-MARKED', ['one right answer each', 'the summary after class', 'marks on Blackboard'])]
    y = 56
    for i, (t, lines) in enumerate(lane1):
        x = 20 + i * step
        _box(c, x, y, bw, bh, t, lines, fill=TINT_ORANGE if i == 2 else PAPER)
        if i < len(lane1) - 1:
            _arrow(c, x + bw + 4, y + bh / 2, x + step - 6, y + bh / 2, INK, 3, 10)
    c.text(20, 262, 'IF CLASSPOINT FAILS THE ROOM: GIO SAYS "BLACKBOARD", EVERYONE SWITCHES LANES. NOBODY SWITCHES ALONE.', size=17, color=MUTED)
    c.text(20, 318, 'THE FALLBACK · BLACKBOARD · A TEST WITH A TIMER · YOUR OWN PACE', size=18, color=TEAL)
    lane2 = [('OPEN THE TEST', ['Blackboard → SD2112', '→ Final quiz', 'laptop or phone']),
             ('35 MINUTES', ['the timer runs', 'one attempt', 'questions shuffled']),
             ('SUBMIT', ['or it submits itself', 'when the time is up', 'then phone face down']),
             ('MARKED', ['same thirty questions', 'same one right answer', 'marks on Blackboard'])]
    y = 340
    for i, (t, lines) in enumerate(lane2):
        x = 20 + i * step
        _box(c, x, y, bw, bh, t, lines, fill=TINT_TEAL if i == 1 else PAPER)
        if i < len(lane2) - 1:
            _arrow(c, x + bw + 4, y + bh / 2, x + step - 6, y + bh / 2, INK, 3, 10)
    _lines(c, 20 + 4 * step, 372, ['either lane:', 'the same questions,', 'one attempt,', 'twenty percent.'], size=18, color=INK)
    return c.finish(name)


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    for fn in (w13_room, w13_rotation, w13_grading, w13_mediation, w13_question_map, w13_quiz_flow):
        svg, png = fn()
        print(png, len(svg))
