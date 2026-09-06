"""
Drawn figures for week 7 · Mid-term: quiz, pitches, teams. Every function name and every
c.finish name starts with w07_ / w07- (the generated files share one folder). Each figure
explains a mechanism of the class rather than decorating it: how the quiz runs on ClassPoint
and on Blackboard, the loop the group project asks for (a person, their data, a model, a
decision, and what it does to them), the anatomy of the one-page mediation brief, the four
beats of a sixty-second pitch, and how five kinds of work map onto the deliverables.
No text smaller than 18 px (9 pt in PowerPoint): the figures are read from the back of a
114-seat room, so the lines are short and the boxes are sized for them.
"""
from __future__ import annotations

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
TINT_TEAL, TINT_VIOLET, TINT_ORANGE, TINT_YELLOW, TINT_GRAY = '#D3E7E8', '#E5DAEB', '#F9E5D6', '#F8DEB1', '#E9E9E6'
RED = '#D22B2B'


def _lines(c, x, y, lines, size=18, color=INK, lh=None, anchor='start'):
    """A few short mono lines, top-left at (x, y)."""
    lh = lh or round(size * 1.4)
    for i, t in enumerate(lines):
        c.text(x, y + i * lh, t, size=size, color=color, anchor=anchor)


def _box(c, x, y, w, h, title, lines, fill=PAPER, stroke=None, title_color=INK, size=18):
    """A titled box with up to three short lines (22 characters at 18 px fit a 296-px box)."""
    c.rect(x, y, w, h, fill=fill, stroke=stroke, width=2)
    c.text(x + 20, y + 36, title, size=19, color=title_color)
    _lines(c, x + 20, y + 68, lines, size=size, color=MUTED, lh=26)


# ───────────────────────── the quiz: two lanes ─────────────────────────
def w07_quiz_flow(name='w07-quiz-flow', w=1680, h=520):
    """How the mid-term runs: the ClassPoint lane (the plan) and the Blackboard lane (the fallback)."""
    c = Canvas(w, h)
    bw, bh, step = 296, 140, 338
    # lane 1: ClassPoint quiz mode
    c.text(20, 34, 'THE PLAN · CLASSPOINT · QUIZ MODE · ONE QUESTION AT A TIME, ON SCREEN', size=18, color=ORANGE)
    lane1 = [('JOIN', ['the class code,', 'your ID (e.g. 3456A),', 'phone · laptops closed']),
             ('A QUESTION', ['one idea, four choices', 'on the big screen', 'and on your phone']),
             ('ANSWER', ['about a minute', 'then it closes', 'no going back']),
             ('TWENTY TIMES', ['weeks 1 to 6', 'and the playlist', 'in course order']),
             ('AUTO-MARKED', ['one right answer each', 'summary after class', 'marks on Blackboard'])]
    y = 56
    for i, (t, lines) in enumerate(lane1):
        x = 20 + i * step
        _box(c, x, y, bw, bh, t, lines, fill=TINT_ORANGE if i == 2 else PAPER)
        if i < len(lane1) - 1:
            _arrow(c, x + bw + 4, y + bh / 2, x + step - 6, y + bh / 2, INK, 3, 10)
    # the switch
    c.text(20, 240, 'IF CLASSPOINT FAILS THE ROOM: GIO SAYS "BLACKBOARD" AND EVERYONE SWITCHES LANES TOGETHER. NOBODY SWITCHES ON THEIR OWN.', size=18, color=MUTED)
    # lane 2: Blackboard
    c.text(20, 290, 'THE FALLBACK · BLACKBOARD · A TEST WITH A TIMER · YOUR OWN PACE', size=18, color=TEAL)
    lane2 = [('OPEN THE TEST', ['Blackboard → SD2112', '→ Mid-term quiz', 'laptop or phone']),
             ('25 MINUTES', ['the timer runs', 'one attempt', 'questions shuffled']),
             ('SUBMIT', ['or it submits itself', 'when the time is up', 'then phone face down']),
             ('MARKED', ['same twenty questions', 'same one right answer', 'marks on Blackboard'])]
    y = 312
    for i, (t, lines) in enumerate(lane2):
        x = 20 + i * step
        _box(c, x, y, bw, bh, t, lines, fill=TINT_TEAL if i == 1 else PAPER)
        if i < len(lane2) - 1:
            _arrow(c, x + bw + 4, y + bh / 2, x + step - 6, y + bh / 2, INK, 3, 10)
    _lines(c, 20 + 4 * step, 348, ['either lane:', 'the same questions,', 'one attempt,', 'ten percent.'], size=18, color=INK, lh=26)
    return c.finish(name)


# ───────────────────────── the group project: the loop ─────────────────────────
def w07_decision_loop(name='w07-decision-loop', w=1680, h=560):
    """A model decides something for each person: the loop, and the four questions of the mediation brief on it."""
    c = Canvas(w, h)
    y = 210
    bw, bh = 260, 130
    # the person
    c.circle(170, y, 66, fill=TEAL)
    c.text(170, y + 8, 'A PERSON', size=20, color=INK, anchor='middle')
    # data, model, decision
    boxes = [(410, 'THEIR DATA', ['what they do and say,', 'what they gave, what', 'was taken'], PAPER),
             (780, 'THE MODEL', ['rules, or examples,', 'or both: the middle', 'of what it saw'], TINT_VIOLET),
             (1150, 'A DECISION', ['for this person, now:', 'what to show, rank,', 'suggest, refuse'], TINT_ORANGE)]
    for x, t, lines, fill in boxes:
        c.rect(x, y - bh / 2, bw, bh, fill=fill)
        c.text(x + 18, y - 26, t, size=20, color=INK)
        _lines(c, x + 18, y + 2, lines, size=18, color=MUTED, lh=24)
    _arrow(c, 240, y, 404, y, INK, 4, 12)
    _arrow(c, 670, y, 774, y, INK, 4, 12)
    _arrow(c, 1040, y, 1144, y, INK, 4, 12)
    # the return: what it does to them
    c.line(1280, y + bh / 2, 1280, 436, INK, 4, cap='butt')
    c.line(1280, 436, 170, 436, INK, 4, cap='butt')
    _arrow(c, 170, 436, 170, y + 70, INK, 4, 12)
    c.text(722, 468, 'WHAT IT DOES TO THEM', size=20, color=INK, anchor='middle')
    c.text(722, 496, 'what they see · what they do · what they stop doing · who they become', size=18, color=MUTED, anchor='middle')
    # the four questions of the brief, as tags on the loop
    c.text(322, 60, 'WHAT DATA?', size=18, color=ORANGE, anchor='middle')
    _lines(c, 322, 84, ['taken, given, inferred', 'consent · minimisation'], size=18, color=MUTED, lh=22, anchor='middle')
    c.line(322, 116, 322, y - 14, ORANGE, 2, cap='butt')
    c.text(905, 60, 'WHERE IS IT BIASED?', size=18, color=ORANGE, anchor='middle')
    _lines(c, 905, 84, ['data · label · algorithm · interaction', 'who is missing from the examples'], size=18, color=MUTED, lh=22, anchor='middle')
    c.line(905, 116, 905, y - bh / 2 - 6, ORANGE, 2, cap='butt')
    c.text(1087, 322, 'THE GUARDRAILS', size=18, color=ORANGE, anchor='middle')
    _lines(c, 1087, 346, ['what it may not decide', 'when a human is in the loop'], size=18, color=MUTED, lh=22, anchor='middle')
    c.line(1087, y + 14, 1087, 300, ORANGE, 2, cap='butt')
    c.text(1312, 416, 'WHICH RELATION?', size=18, color=ORANGE)
    _lines(c, 1312, 440, ['through it · off it · facing it', 'around them · how hard it pushes'], size=18, color=MUTED, lh=22)
    c.line(1286, 436, 1304, 436, ORANGE, 2, cap='butt')
    c.text(20, 34, 'THE PRODUCT YOU DESIGN: A LOOP, NOT A PICTURE', size=18, color=ORANGE)
    c.text(w - 20, 34, 'the four questions on the loop are the four sections of the mediation brief', size=18, color=MUTED, anchor='end')
    return c.finish(name)


# ───────────────────────── the mediation brief: one page, four questions ─────────────────────────
def w07_brief_anatomy(name='w07-brief-anatomy', w=1680, h=560):
    """The one-page mediation brief as a wireframe, with the vocabulary and the week that answers each section."""
    c = Canvas(w, h)
    px, py, pw, ph = 40, 14, 380, 532
    c.rect(px, py, pw, ph, fill='#FFFFFF', stroke=INK, width=3)
    c.text(px + 24, py + 40, 'MEDIATION BRIEF', size=18, color=INK)
    c.text(px + 24, py + 66, '[team] · [product] · one page', size=18, color=MUTED)
    c.line(px + 24, py + 80, px + pw - 24, py + 80, LINE, 2, cap='butt')
    sections = [('1 · THE RELATION', 'WHICH RELATION ARE YOU BUILDING?',
                 ['embodiment · hermeneutic · alterity · background — Ihde, 1990',
                  'cyborg · immersion · augmentation — Verbeek, 2015',
                  'and its force: hidden or apparent, weak or strong'], 'WEEK 5', TINT_VIOLET),
                ('2 · THE DATA', 'WHAT DOES THE MODEL NEED TO KNOW ABOUT EACH PERSON?',
                 ['what it needs · where it comes from · what it keeps',
                  'given, taken or inferred · consent · minimisation · anonymisation'], 'WEEKS 8 – 10', TINT_ORANGE),
                ('3 · THE BIAS', 'WHERE IS IT WRONG, AND FOR WHOM?',
                 ['data bias · label bias · algorithmic bias · interaction bias',
                  'the bias register: who is missing from the examples, who pays'], 'WEEK 9', TINT_ORANGE),
                ('4 · THE GUARDRAILS', 'WHAT MAY IT NOT DECIDE?',
                 ['when a human is in the loop · how it fails in front of a person',
                  'what the person can see, refuse, correct · who is accountable'], 'WEEKS 11 – 12', '#F7E3E8')]
    sy = py + 96
    sh = 108
    for i, (head, q, lines, wk, tint) in enumerate(sections):
        y = sy + i * sh
        c.rect(px + 24, y, pw - 48, sh - 14, fill=tint)
        c.text(px + 38, y + 30, head, size=18, color=INK)
        for k in range(3):                                   # the text of the section, as a wireframe
            lw = (pw - 76) * (0.92 if k < 2 else 0.55)
            c.rect(px + 38, y + 46 + k * 14, lw, 6, fill='#C9CBC7')
        # the annotation on the right
        ax = 500
        c.line(px + pw, y + 30, ax - 16, y + 30, ORANGE, 2, cap='butt')
        c.circle(ax - 16, y + 30, 5, fill=ORANGE)
        c.text(ax, y + 24, q, size=20, color=INK)
        _lines(c, ax, y + 54, lines, size=18, color=MUTED, lh=24)
        c.text(w - 20, y + 24, wk, size=18, color=ORANGE, anchor='end')
    c.text(w - 20, 40, 'one page · four answers · every answer has a week', size=18, color=MUTED, anchor='end')
    return c.finish(name)


# ───────────────────────── the pitch: sixty seconds, four beats ─────────────────────────
def w07_pitch_anatomy(name='w07-pitch-anatomy', w=1680, h=560):
    """A sixty-second bar cut into four beats, the question each answers, and one made-up pitch along it."""
    c = Canvas(w, h)
    x0, x1, y, bh = 60, 1620, 250, 64
    pps = (x1 - x0) / 60                          # pixels per second
    beats = [(0, 10, 'THE PERSON', TINT_TEAL, 'who is in front of it?', ['On the 6:40 bus, half', 'asleep, one hand free.']),
             (10, 30, 'THE DECISION', TINT_ORANGE, 'what it decides for them: one thing', ['The app picks which of her three routes to', 'show, before she asks. It does not show', 'the other two.']),
             (30, 40, 'FOR WHOM', TINT_VIOLET, 'who else, and who not', ['Commuters whose route', 'changes with the', 'weather. Not tourists.']),
             (40, 60, 'WITH WHAT DATA', TINT_GRAY, 'what it must know, and where from', ['Her past taps, the transport feed, the', 'forecast. Nothing from her calendar.', 'Nothing kept past a month.'])]
    for s0, s1, t, tint, q, ex in beats:
        bx0, bx1 = x0 + s0 * pps, x0 + s1 * pps
        c.rect(bx0, y, bx1 - bx0, bh, fill=tint)
        c.text(bx0 + 4, y - 66, t, size=20, color=ORANGE)
        c.text(bx0 + 4, y - 36, q, size=18, color=INK)
        c.text(bx0 + (bx1 - bx0) / 2, y + bh / 2 + 7, f'{s1 - s0} s', size=20, color=INK, anchor='middle')
        _lines(c, bx0 + 4, y + bh + 40, ex, size=18, color=MUTED, lh=24)
    for s in range(0, 61, 10):
        x = x0 + s * pps
        c.line(x, y + bh, x, y + bh + 12, INK, 2, cap='butt')
    c.text(x0, 70, 'SIXTY SECONDS · NO SLIDES · NO DEMO · SAY THE PRODUCT\'S NAME LAST', size=18, color=ORANGE)
    c.text(x1, 70, 'the example is made up; the beats are not', size=18, color=MUTED, anchor='end')
    c.text(x0, y + bh + 140, '0 s', size=18, color=MUTED)
    c.text(x1, y + bh + 140, '60 s · the timer does not care. stop.', size=18, color=MUTED, anchor='end')
    c.text(x0 + 30 * pps, y + bh + 140, '30 s', size=18, color=MUTED, anchor='middle')
    c.text(x0, y + bh + 190, 'The room listens for one thing: a decision a model makes for a person, said in a sentence. If it needs a demo, it is not a pitch yet.', size=18, color=INK)
    return c.finish(name)


# ───────────────────────── teams: five kinds of work, three deliverables and the log ─────────────────────────
def w07_team_skills(name='w07-team-skills', w=1680, h=560):
    """Five kinds of work in a team of four or five, and which deliverable each one feeds (the log is the evidence, not a deliverable)."""
    c = Canvas(w, h)
    work = [('RESEARCH', ['reads, interviews, sources', 'the 30 % most teams skip'], TEAL),
            ('CONCEPT & PROTOTYPE', ['the decision, the flow', 'paper, Figma or code'], VIOLET),
            ('VISUAL', ['the A0, the system', 'the 20 %'], ORANGE),
            ('VIDEO & STORY', ['three to five minutes', 'for a stranger'], '#E94D7F'),
            ('THE SCRIBE', ['the log, the board, the brief', 'the 10 % most teams lose'], INK)]
    deliv = [('THE POSTER · A0', 'research and concept'), ('THE VIDEO · 3 – 5 MIN', 'how it works'),
             ('THE MEDIATION BRIEF', 'relation, data, bias, guardrails'), ('THE PROCESS LOG', 'the 10 %: who did what, when')]
    feeds = {0: [0, 2], 1: [0, 1, 2], 2: [0, 1], 3: [1], 4: [2, 3]}
    wx = [190 + i * 325 for i in range(5)]
    wy = 130
    dx = [225 + j * 410 for j in range(4)]
    dy = 440
    for i, js in feeds.items():
        for j in js:
            c.line(wx[i], wy + 156, dx[j], dy - 40, LINE, 3, cap='butt')
    for i, (t, lines, col) in enumerate(work):
        c.circle(wx[i], wy, 44, fill=col)
        c.circle(wx[i], wy - 14, 12, fill='#FFFFFF')
        c.poly([(wx[i] - 22, wy + 30), (wx[i] + 22, wy + 30), (wx[i] + 16, wy + 6), (wx[i] - 16, wy + 6)], fill='#FFFFFF')
        c.text(wx[i], wy + 92, t, size=18, color=INK, anchor='middle')
        _lines(c, wx[i], wy + 116, lines, size=18, color=MUTED, lh=24, anchor='middle')
    for j, (t, sub) in enumerate(deliv):
        c.rect(dx[j] - 190, dy - 40, 380, 80, fill=PAPER, stroke=INK if j < 3 else MUTED, width=2)
        c.text(dx[j], dy - 6, t, size=18, color=INK if j < 3 else MUTED, anchor='middle')
        c.text(dx[j], dy + 20, sub, size=18, color=MUTED, anchor='middle')
    c.text(20, 34, 'FIVE KINDS OF WORK · EVERYONE DOES TWO', size=18, color=ORANGE)
    c.text(w - 20, 34, 'five illustrators: a poster and no brief · five coders: a demo and no poster', size=18, color=MUTED, anchor='end')
    c.text(w / 2, 536, 'The lines are who feeds what. Three deliverables and the log behind them: every one needs at least one line into it.', size=18, color=INK, anchor='middle')
    return c.finish(name)


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    for fn in (w07_quiz_flow, w07_decision_loop, w07_brief_anatomy, w07_pitch_anatomy, w07_team_skills):
        svg, png = fn()
        print(png, len(svg))
