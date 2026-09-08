"""
Drawn figures for week 8 · AI as design material. Every function name and every c.finish name
starts with w08_ / w08- (the generated files share one folder). Each figure explains a mechanism
rather than decorating a slide: the five parts of a product that decides something for each person
(data, score, threshold, decision, fallback); the decision card, filled for four products and blank
for the activity; a wizard-of-Oz prototype (a teammate behind a curtain plays the model); the grain
of a model (typicality, and how the grain moves when it is retrained); the semester as five sprints
with a backlog; a repository with commits, branches and a merge (Git, and Figma's branches); and the
brainstorm ladder of the workshop, with one fictional example filled in.
"""
from __future__ import annotations

import math
import random

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
TINT_TEAL, TINT_VIOLET, TINT_ORANGE, TINT_YELLOW, TINT_GRAY = '#D3E7E8', '#E5DAEB', '#F9E5D6', '#F8DEB1', '#E9E9E6'
RED = '#D22B2B'


def _lines(c, x, y, lines, size=18, color=INK, lh=None, anchor='start'):
    """A few short mono lines, top-left at (x, y)."""
    lh = lh or round(size * 1.45)
    for i, t in enumerate(lines):
        c.text(x, y + i * lh, t, size=size, color=color, anchor=anchor)


def _dashed(c, x1, y1, x2, y2, color=MUTED, width=2, dash=10, gap=8):
    """A dashed line, drawn as short segments so that both backends agree."""
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    t = 0.0
    while t < length:
        e = min(length, t + dash)
        c.line(x1 + ux * t, y1 + uy * t, x1 + ux * e, y1 + uy * e, color, width, cap='butt')
        t += dash + gap


# ───────────────────────── five parts of a product that decides ─────────────────────────
def w08_decision_anatomy(name='w08-decision-anatomy', w=1680, h=560):
    """A person → their data → a score → a threshold → the decision, or the fallback. Who sets each part."""
    c = Canvas(w, h)
    c.text(0, 34, 'A PRODUCT THAT DECIDES SOMETHING FOR EACH PERSON: FIVE PARTS', size=18, color=ORANGE)
    c.text(w, 34, 'every arrow is a place where the product can be wrong', size=17, color=MUTED, anchor='end')
    y = 200
    bw, bh = 240, 104
    # the person
    c.circle(100, y, 60, fill=TEAL)
    c.text(100, y + 8, 'A PERSON', size=18, color=INK, anchor='middle')
    # data · score
    bw = 290
    boxes = [(250, 'THEIR DATA', ['what they did, said, are;', 'given, taken, inferred'], PAPER),
             (600, 'A SCORE', ['one number: how likely they', 'want it · rule or model'], TINT_VIOLET)]
    for x, t, lines, fill in boxes:
        c.rect(x, y - bh / 2, bw, bh, fill=fill)
        c.text(x + 18, y - 14, t, size=19, color=INK)
        _lines(c, x + 18, y + 14, lines, size=15, color=MUTED, lh=20)
    _arrow(c, 166, y, 244, y, INK, 4, 12)
    _arrow(c, 540, y, 594, y, INK, 4, 12)
    # the threshold: a gate
    gx = 950
    c.poly([(gx + 70, y - 70), (gx + 140, y), (gx + 70, y + 70), (gx, y)], fill=TINT_ORANGE, stroke=INK, width=3)
    c.text(gx + 70, y - 4, 'score', size=15, color=INK, anchor='middle')
    c.text(gx + 70, y + 18, '> t ?', size=17, color=INK, anchor='middle')
    c.text(gx + 70, y - 96, 'THE THRESHOLD', size=19, color=INK, anchor='middle')
    _arrow(c, 890, y, gx - 6, y, INK, 4, 12)
    # yes → the decision · no → the fallback
    dx = 1300
    bw = 240
    c.rect(dx, 60, bw + 80, bh, fill=ORANGE)
    c.text(dx + 18, 100, 'THE DECISION', size=19, color=INK)
    _lines(c, dx + 18, 128, ['show it, rank it first, say it,', 'suggest it — for this person, now'], size=15, color=INK, lh=20)
    c.rect(dx, 300, bw + 80, bh, fill=TINT_GRAY)
    c.text(dx + 18, 340, 'THE FALLBACK', size=19, color=INK)
    _lines(c, dx + 18, 368, ['what everyone gets: the default,', 'the same-for-all screen, a human'], size=15, color=MUTED, lh=20)
    c.line(gx + 140, y, gx + 200, y, INK, 4, cap='butt')
    c.line(gx + 200, y, gx + 200, 112, INK, 4, cap='butt')
    _arrow(c, gx + 200, 112, dx - 6, 112, INK, 4, 12)
    c.line(gx + 200, y, gx + 200, 352, INK, 4, cap='butt')
    _arrow(c, gx + 200, 352, dx - 6, 352, INK, 4, 12)
    c.text(gx + 214, 100, 'yes', size=17, color=ORANGE)
    c.text(gx + 214, 340, 'no', size=17, color=MUTED)
    # who sets each part
    c.line(0, 430, w, 430, LINE, 2, cap='butt')
    c.text(0, 464, 'WHO SETS IT', size=16, color=ORANGE)
    cols = [(250, 'the data', 'you choose what to take, and ask'),
            (600, 'the score', 'written (machine A) or learned (B)'),
            (950, 'the threshold', 'a number you set; it moves'),
            (1300, 'both branches', 'designed — the wrong one most')]
    for x, t, s in cols:
        c.text(x, 464, t, size=17, color=INK)
        c.text(x, 492, s, size=15, color=MUTED)
    c.text(0, 540, 'the fallback is what the person sees on the day the model is wrong · the threshold decides how often that day comes', size=17, color=INK)
    return c.finish(name)


# ───────────────────────── the decision card: four products, and the blank ─────────────────────────
CARD_ROWS = ['THE DECISION', 'FOR WHOM', 'THE DATA', 'THE SCORE · THE THRESHOLD', 'IF IT IS WRONG']


def w08_decision_card(name, product, sub, rows, w=800, h=700, accent=ORANGE):
    """The decision card: five rows for one product. rows: five lists of short lines (or None: a blank card)."""
    c = Canvas(w, h)
    c.rect(0, 0, w, h, fill=PAPER)
    c.rect(0, 0, w, 8, fill=accent)
    c.text(28, 52, 'DECISION CARD', size=15, color=accent)
    c.text(28, 88, product, size=26, color=INK, mono=False, weight=700)
    c.text(28, 116, sub, size=15, color=MUTED)
    c.line(28, 136, w - 28, 136, LINE, 2, cap='butt')
    y = 160
    step = (h - y - 10) / 5
    for i, label in enumerate(CARD_ROWS):
        ry = y + i * step
        c.text(28, ry + 20, label, size=15, color=accent)
        lines = rows[i] if rows else None
        if lines:
            _lines(c, 28, ry + 48, lines, size=17, color=INK, lh=23)
        else:
            for k in range(2):
                _dashed(c, 28, ry + 56 + k * 28, w - 28, ry + 56 + k * 28, LINE, 2, 6, 6)
        if i < 4:
            c.line(28, ry + step - 8, w - 28, ry + step - 8, LINE, 1, cap='butt')
    return c.finish(name)


def w08_card_blank():
    return w08_decision_card('w08-card-blank', 'Your product', 'team __ · one product · one decision per person', None)


def w08_card_spotify():
    return w08_decision_card('w08-card-spotify', 'Spotify DJ', 'beta 22 February 2023 · Premium · US and Canada, then 50 markets', [
        ['what plays next for you — and what', 'to say about it, in a voice'],
        ['each Premium listener, one lineup', 'each; nobody hears the same DJ'],
        ['your listening history, your skips; for the', 'words, a Writers\' Room of music and culture', 'experts, data curators and scriptwriters'],
        ['the personalisation model ranks tracks;', 'generated commentary read by a voice model', 'of Xavier "X" Jernigan (Sonantic)'],
        ['skip; hit the DJ button and it switches', 'direction; or leave DJ for your playlist'],
    ], accent=TEAL)


def w08_card_netflix():
    return w08_decision_card('w08-card-netflix', 'Netflix', 'artwork per member (Tech Blog, December 2017) · rows per member (2015)', [
        ['which poster of a title you see, which', 'rows you get, and in what order'],
        ['every member, every visit — the same', 'film wears a different face for each'],
        ['what you watched, when, on what, what', 'you clicked and what you scrolled past'],
        ['a contextual bandit picks the artwork;', 'candidate rows are ranked and the page', 'is assembled, no fixed template'],
        ['you scroll past a poster that was aimed', 'at you; the miss becomes data'],
    ], accent=RED)


def w08_card_duolingo():
    return w08_decision_card('w08-card-duolingo', 'Duolingo', 'Max, 14 March 2023 · "AI-first" memo, 28 April 2025 · 148 courses, 30 April 2025', [
        ['the next exercise for you, and why', 'your answer was wrong (Explain My Answer)'],
        ['every learner; Max subscribers get the', 'GPT-4 tutor and Roleplay conversations'],
        ['every tap: what you got wrong, how fast,', 'when you come back, what you skip'],
        ['a model estimates what you know; the', 'courses are generated with models:', '148 in about a year, the first 100 in 12'],
        ['a wrong explanation reads like a right', 'one; who checks it now? the memo\'s', 'answer: fewer contractors'],
    ], accent=VIOLET)


def w08_card_humane():
    return w08_decision_card('w08-card-humane', 'Humane AI Pin', 'announced 9 November 2023 · shipped April 2024 · off on 28 February 2025', [
        ['the answer to whatever you asked —', 'spoken, or lasered onto your palm'],
        ['anyone who paid US$699 and US$24 a', 'month; no screen, no apps, no phone'],
        ['your voice, the camera, your location,', 'everything routed through the cloud'],
        ['a language model in the cloud decides', 'everything; the Pin is a microphone,', 'a camera and a projector'],
        ['ask again, slower; when HP bought the', 'assets and the servers went, so did it'],
    ], accent=INK)


def w08_card_rabbit():
    return w08_decision_card('w08-card-rabbit', 'Rabbit R1', 'CES, 9 January 2024 · US$199 · designed with Teenage Engineering', [
        ['which app to operate on your behalf,', 'and how: a ride, a song, a meal'],
        ['anyone who wanted a phone that is', 'not a phone; a first batch of 10,000'],
        ['your voice, and the accounts you log', 'it into (Spotify, Uber and a few more)'],
        ['a "Large Action Model" that clicks', 'through apps for you — in practice an', 'Android app that reviewers found buggy'],
        ['you take out your phone and do it', 'yourself; reviewers: "barely reviewable"'],
    ], accent=ORANGE)


# ───────────────────────── a wizard behind a curtain ─────────────────────────
def w08_wizard(name='w08-wizard', w=1680, h=560):
    """A wizard-of-Oz prototype: the person talks to an interface; a teammate behind a curtain plays the model."""
    c = Canvas(w, h)
    c.text(0, 34, 'A WIZARD-OF-OZ PROTOTYPE: TEST THE DECISION BEFORE THE MODEL EXISTS', size=18, color=ORANGE)
    c.text(w, 34, 'Gould, Conti & Hovanyecz 1983 · named by Kelley 1984', size=17, color=MUTED, anchor='end')
    y = 230
    # the person
    c.circle(140, y, 60, fill=TEAL)
    c.text(140, y + 8, 'A PERSON', size=18, color=INK, anchor='middle')
    _lines(c, 140, y + 96, ['thinks it is the product', 'asks, taps, waits'], size=15, color=MUTED, lh=20, anchor='middle')
    # the interface
    c.rect(360, y - 90, 300, 180, fill=PAPER, stroke=INK, width=3)
    c.text(510, y - 46, 'THE INTERFACE', size=18, color=INK, anchor='middle')
    _lines(c, 510, y - 14, ['a paper screen, a chat window,', 'a voice from a laptop:', 'the shape of the decision'], size=15, color=MUTED, lh=20, anchor='middle')
    _arrow(c, 206, y - 16, 354, y - 16, INK, 4, 12)
    _arrow(c, 354, y + 16, 206, y + 16, INK, 4, 12)
    c.text(280, y - 30, 'a request', size=15, color=MUTED, anchor='middle')
    c.text(280, y + 44, 'a decision', size=15, color=MUTED, anchor='middle')
    # the curtain
    cx = 800
    for k in range(0, 400, 26):
        c.line(cx, 70 + k, cx, 70 + k + 14, VIOLET, 5, cap='butt')
    c.text(cx, 500, 'THE CURTAIN', size=16, color=VIOLET, anchor='middle')
    c.text(cx, 524, 'the person must not see behind it', size=15, color=MUTED, anchor='middle')
    # the wizard
    c.circle(1000, y, 60, fill=VIOLET)
    c.text(1000, y + 8, 'THE WIZARD', size=17, color='#FFFFFF', anchor='middle')
    _lines(c, 1000, y + 96, ['a teammate playing the model', 'types the answer in ten seconds'], size=15, color=MUTED, lh=20, anchor='middle')
    _arrow(c, 666, y - 16, cx - 8, y - 16, VIOLET, 3, 10)
    _arrow(c, cx + 8, y - 16, 934, y - 16, VIOLET, 3, 10)
    _arrow(c, 934, y + 16, cx + 8, y + 16, VIOLET, 3, 10)
    _arrow(c, cx - 8, y + 16, 666, y + 16, VIOLET, 3, 10)
    # what the wizard holds
    c.rect(1180, 100, 480, 120, fill=TINT_ORANGE)
    c.text(1200, 138, 'THE RULE ON A CARD', size=17, color=INK)
    _lines(c, 1200, 166, ['"show the new thing if they opened it twice', 'this week" — machine A, played by a human'], size=15, color=MUTED, lh=20)
    c.rect(1180, 250, 480, 120, fill=TINT_VIOLET)
    c.text(1200, 288, 'THE DATA ON A SHEET', size=17, color=INK)
    _lines(c, 1200, 316, ['a spreadsheet with a row per person: what', 'you already know, and what you had to invent'], size=15, color=MUTED, lh=20)
    c.line(1060, y, 1172, 160, MUTED, 2, cap='butt')
    c.line(1060, y, 1172, 310, MUTED, 2, cap='butt')
    # what you learn
    c.line(0, 420, 760, 420, LINE, 2, cap='butt')
    c.text(0, 454, 'WHAT YOU LEARN IN AN AFTERNOON', size=16, color=ORANGE)
    _lines(c, 0, 484, ['is the decision wanted at all · how fast it has to be', 'what the person does when it is wrong · which data you do not have'], size=15, color=INK, lh=22)
    c.text(1180, 454, 'IBM, 1983: a "listening typewriter" that took dictation.', size=15, color=INK)
    c.text(1180, 480, 'The speech recogniser was a typist in the next room.', size=15, color=MUTED)
    c.text(1180, 506, 'Would an imperfect one still be useful? Some were.', size=15, color=MUTED)
    return c.finish(name)


# ───────────────────────── the grain of a model ─────────────────────────
def _bell(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2)


def w08_grain(name='w08-grain', w=1680, h=560):
    """Left: the examples a model saw, as a distribution over typicality: fluent in the middle, wrong at the edges.
    Right: the same model retrained — the grain moved, and the threshold set on the old grain is now wrong."""
    c = Canvas(w, h)
    c.text(0, 34, 'THE GRAIN OF A MODEL IS THE SHAPE OF ITS EXAMPLES', size=18, color=ORANGE)
    c.text(w, 34, 'Rosch 1975: a middle and an edge · Dove et al. 2017, Yang et al. 2020: probabilistic, and it changes', size=16, color=MUTED, anchor='end')

    def panel(x0, mu, sigma, label, ghost=None, threshold=None):
        pw, base, top = 720, 400, 110
        c.line(x0, base, x0 + pw, base, INK, 2, cap='butt')
        n = 36
        bw = pw / n
        for i in range(n):
            u = i / (n - 1)
            v = _bell(u, mu, sigma)
            bh = v * (base - top)
            near = abs(u - mu) < sigma * 1.1
            c.rect(x0 + i * bw + 2, base - bh, bw - 4, bh, fill=ORANGE if near else TINT_GRAY)
        if ghost:
            pts = [(x0 + (i / 120) * pw, base - _bell(i / 120, ghost[0], ghost[1]) * (base - top)) for i in range(121)]
            for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
                c.line(xa, ya, xb, yb, MUTED, 2, cap='butt')
        if threshold is not None:
            tx = x0 + threshold * pw
            _dashed(c, tx, top - 10, tx, base + 8, INK, 3, 10, 7)
            c.text(tx + 12, 190, 'the threshold', size=15, color=INK)
            c.text(tx + 12, 211, 'you set', size=15, color=INK)
        c.text(x0, base + 30, 'edge', size=15, color=MUTED)
        c.text(x0 + pw / 2, base + 30, 'typical', size=15, color=INK, anchor='middle')
        c.text(x0 + pw, base + 30, 'edge', size=15, color=MUTED, anchor='end')
        c.text(x0, 84, label, size=17, color=INK)

    panel(0, 0.5, 0.16, 'THE EXAMPLES IT LEARNED FROM · OCTOBER', threshold=0.72)
    panel(960, 0.6, 0.12, 'RETRAINED ON NEW EXAMPLES · DECEMBER', ghost=(0.5, 0.16), threshold=0.72)
    _lines(c, 0, 470, ['the middle: fluent, confident, usually right — the chair with four legs',
                       'the edges: still confident, often wrong — the swing, the tree stump',
                       'and confident looks the same in both places'],
           size=15, color=INK, lh=22)
    _lines(c, 960, 470, ['same product, new grain: what was typical moved; the threshold did not',
                         'the people it now shows the new thing to are not the people you tested it on'],
           size=15, color=INK, lh=22)
    c.text(w / 2, 540, 'a material with a grain: work with it in the middle, guard it at the edges, and check it again after every retraining', size=16, color=MUTED, anchor='middle')
    return c.finish(name)


# ───────────────────────── the semester as five sprints ─────────────────────────
def w08_sprints(name='w08-sprints', w=1680, h=560):
    """Weeks 8 to 13 as sprints: a backlog on the left, one deliverable per sprint, a stand-up at the team table before
    every class from week 9, and the review with the TAs after class (the first one is today)."""
    c = Canvas(w, h)
    c.text(0, 34, 'THE GROUP PROJECT AS SCRUM · WEEKS 8 – 13', size=18, color=ORANGE)
    c.text(w, 34, 'Scrum Guide 2020: a sprint is one month or less; ours is a week', size=16, color=MUTED, anchor='end')
    # the backlog
    c.rect(0, 70, 340, 300, fill=PAPER)
    c.text(20, 104, 'THE BACKLOG', size=18, color=INK)
    c.text(20, 128, 'in order · the only source of work', size=14, color=MUTED)
    items = ['1  the decision, in one sentence', '2  the data we have · do not have', '3  the bias register', '4  a wizard-of-Oz test', '5  the prototype of the moment', '6  poster · video · brief']
    for i, t in enumerate(items):
        c.text(28, 166 + i * 30, t, size=15, color=INK if i < 2 else MUTED)
    c.rect(20, 152, 300, 34, stroke=ORANGE, width=2)
    c.text(320, 146, 'this sprint', size=14, color=ORANGE, anchor='end')
    _arrow(c, 340, 200, 394, 200, INK, 4, 12)
    # the sprints
    x0, sw, gap = 400, 200, 16
    weeks = [('WEEK 8', 'the proposal', 'one page: decision,', 'for whom, what data'),
             ('WEEK 9', 'concept board', 'plus the register,', 'after Coded Bias'),
             ('WEEK 10', 'prototype v1', 'paper, Figma, code:', 'the moment, decided'),
             ('WEEK 11', 'draft poster', 'and the one-page', 'mediation brief'),
             ('WEEK 12', 'final poster', 'and the 3–5 minute', 'video, ready'),
             ('WEEK 13', 'the fair', 'A0 on the wall,', 'then the final quiz')]
    for i, (wk, head, l1, l2) in enumerate(weeks):
        x = x0 + i * (sw + gap)
        fill = TINT_ORANGE if i == 0 else (INK if i == 5 else PAPER)
        c.rect(x, 90, sw, 250, fill=fill)
        tc = '#FFFFFF' if i == 5 else INK
        mc = '#B3B7BE' if i == 5 else MUTED
        c.text(x + 16, 124, wk, size=15, color=ORANGE if i < 5 else '#F0BD60')
        c.text(x + 16, 160, head, size=19, color=tc, mono=False, weight=700)
        c.text(x + 16, 192, l1, size=14, color=mc)
        c.text(x + 16, 213, l2, size=14, color=mc)
        # today the first review; from week 9 a stand-up before every class
        c.rect(x + 16, 264, sw - 32, 52, fill=TEAL if i < 5 else '#2A3644')
        band = ('REVIEW · THE TAs', 'after class today') if i == 0 else ('STAND-UP · 15 MIN', 'before class')
        c.text(x + sw / 2, 286, band[0], size=14, color=INK if i < 5 else '#FFFFFF', anchor='middle')
        c.text(x + sw / 2, 306, band[1], size=14, color=INK if i < 5 else '#B3B7BE', anchor='middle')
        if i < 5:
            _arrow(c, x + sw, 215, x + sw + gap - 2, 215, INK, 3, 9)
    # the stand-up's three questions, and the review
    c.line(0, 400, w, 400, LINE, 2, cap='butt')
    c.text(0, 434, 'THE STAND-UP: THREE QUESTIONS, FIFTEEN MINUTES, STANDING, BEFORE CLASS', size=16, color=ORANGE)
    _lines(c, 0, 464, ['what did I do since last class · what will I do before the next · what is in my way',
                       'at your table in the half hour before class, the TAs in the room; the scribe writes it down'], size=15, color=INK, lh=22)
    c.text(900, 434, 'THE REVIEW: THE TAs, THIRTY MINUTES AFTER CLASS', size=16, color=ORANGE)
    _lines(c, 900, 464, ['show the increment — the thing that exists now — not the plan;', 'then move one item from the backlog into the next sprint'], size=15, color=INK, lh=22)
    c.text(0, 540, 'Takeuchi & Nonaka, HBR, January 1986: teams that move like a rugby side, not a relay · Schwaber & Sutherland, Scrum, 1995 · the Scrum Guide, 2020', size=14, color=MUTED)
    return c.finish(name)


# ───────────────────────── a repository: commits, branches, a merge ─────────────────────────
def w08_git(name='w08-git', w=1680, h=560):
    """A commit graph: the main line, a branch that is merged back, a branch that is kept but not merged.
    The same words in Git (2005) and in Figma (branching, 2021)."""
    c = Canvas(w, h)
    c.text(0, 34, 'A REPOSITORY IS A HISTORY YOU CAN BRANCH', size=18, color=ORANGE)
    c.text(w, 34, 'Git: Torvalds, April 2005 · Figma branching: Config, April 2021, beta on the Organization plan', size=16, color=MUTED, anchor='end')
    ym, yb1, yb2 = 250, 150, 350
    xs = [120, 340, 560, 780, 1000, 1220]
    # main line
    c.line(xs[0], ym, xs[-1], ym, INK, 5, cap='butt')
    c.text(xs[-1] + 24, ym + 6, 'MAIN', size=16, color=INK)
    # branch 1: off commit 2, merged at commit 5
    c.line(xs[1], ym, xs[2], yb1, VIOLET, 4, cap='butt')
    c.line(xs[2], yb1, xs[3], yb1, VIOLET, 4, cap='butt')
    c.line(xs[3], yb1, xs[4], ym, VIOLET, 4, cap='butt')
    # branch 2: off commit 3, kept
    c.line(xs[2], ym, xs[3], yb2, TEAL, 4, cap='butt')
    c.line(xs[3], yb2, xs[4] + 60, yb2, TEAL, 4, cap='butt')
    labels = ['v1 · the pitch sentence', 'v2 · the decision card', 'v3 · the data we have', 'v4 · voice merged in', 'v5 · wizard test, fixed', 'v6 · concept board']
    for i, x in enumerate(xs):
        c.circle(x, ym, 16, fill=ORANGE if i in (1, 4) else INK)
        c.text(x, ym + 52, labels[i], size=15, color=INK, anchor='middle')
    for x, t in ((xs[2], 'try: a voice, no screen'), (xs[3], 'the voice, tested')):
        c.circle(x, yb1, 14, fill=VIOLET)
        c.text(x, yb1 - 30, t, size=15, color=VIOLET, anchor='middle')
    for x, t in ((xs[3], 'try: decide for a family'), (xs[4] + 60, 'kept, not merged')):
        c.circle(x, yb2, 14, fill=TEAL)
        c.text(x, yb2 + 40, t, size=15, color=INK, anchor='middle')
    c.text(xs[1], ym - 34, 'branch', size=15, color=VIOLET, anchor='middle')
    c.text(xs[4], ym - 34, 'merge', size=15, color=VIOLET, anchor='middle')
    # the vocabulary, in both tools
    x0 = 1300
    c.rect(x0, 90, 380, 340, fill=PAPER)
    c.text(x0 + 20, 124, 'THE SAME FOUR WORDS', size=16, color=ORANGE)
    rows = [('REPOSITORY', 'Git: the folder + its history', 'Figma: the file'),
            ('COMMIT', 'Git: a saved state, with a message', 'Figma: a named version'),
            ('BRANCH', 'Git: a copy to try things in', 'Figma: a branch of the file'),
            ('MERGE', 'Git: bring the branch back', 'Figma: review, then merge')]
    for i, (t, g, f) in enumerate(rows):
        y = 160 + i * 66
        c.text(x0 + 20, y, t, size=15, color=INK)
        c.text(x0 + 20, y + 22, g, size=14, color=MUTED)
        c.text(x0 + 20, y + 44, f, size=14, color=MUTED)
    c.line(0, 440, 1240, 440, LINE, 2, cap='butt')
    _lines(c, 0, 474, ['a commit is a decision with a date and a name on it: the process documentation the rubric asks for, made as a side effect',
                       'the rule of the team: nobody works on main; every idea is a branch; a branch that is not merged is still kept — it is evidence for the poster'],
           size=15, color=INK, lh=22)
    c.text(0, 540, 'no Organization plan? name the versions by hand: v1, v2, v3 in the file name and in the version history, with one line each', size=15, color=MUTED)
    return c.finish(name)


# ───────────────────────── the brainstorm ladder ─────────────────────────
def w08_ladder(name='w08-ladder', w=1680, h=560):
    """Five rungs, in order: the person, the moment, the decision, the data, the failure — with one fictional example."""
    c = Canvas(w, h)
    c.text(0, 34, 'THE BRAINSTORM LADDER · ONE LINE PER IDEA', size=18, color=ORANGE)
    c.text(w, 34, 'an idea that skips a rung is a feature, not a product', size=17, color=MUTED, anchor='end')
    rungs = [('1 · THE PERSON', 'who, exactly — one person,', 'not "users"', 'a night-shift nurse in Kwun Tong', TEAL),
             ('2 · THE MOMENT', 'when and where the product', 'meets them', 'on the minibus home, 7:40 a.m., tired', TINT_TEAL),
             ('3 · THE DECISION', 'what it decides for them,', 'in one sentence', 'what she will eat tonight — chosen for her', ORANGE),
             ('4 · THE DATA', 'what it needs to know, and', 'whether that exists', 'her roster, what she bought, what she cooked before', TINT_ORANGE),
             ('5 · THE FAILURE', 'the day it is wrong: what', 'she sees, what she does', 'it suggests the dish she just had at work; she orders out', TINT_GRAY)]
    n = len(rungs)
    step_w, step_h = 300, 60
    for i, (t, l1, l2, ex, fill) in enumerate(rungs):
        x = 40 + i * (step_w + 30)
        y = 330 - i * step_h
        c.rect(x, y, step_w, 100, fill=fill)
        c.text(x + 16, y + 34, t, size=17, color=INK)
        c.text(x + 16, y + 60, l1, size=15, color=INK if fill in (TEAL, ORANGE) else MUTED)
        c.text(x + 16, y + 81, l2, size=15, color=INK if fill in (TEAL, ORANGE) else MUTED)
        # the riser
        if i < n - 1:
            c.line(x + step_w, y + 100, x + step_w, y - step_h + 100, LINE, 3, cap='butt')
        # the example, hung under the rung
        c.line(x + 16, y + 118, x + 16, 470, LINE, 2, cap='butt')
        _lines(c, x + 28, 466, _wrap(ex, 32), size=15, color=INK, lh=20)
    c.text(0, 540, 'the example is made up · yours will be too, until rung 4 makes you check whether the data exists — that check is the proposal', size=15, color=MUTED)
    return c.finish(name)


def _wrap(text, width):
    """Greedy word wrap into short lines."""
    out, cur = [], ''
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > width:
            out.append(cur)
            cur = word
        else:
            cur = f'{cur} {word}' if cur else word
    if cur:
        out.append(cur)
    return out


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    for fn in (w08_decision_anatomy, w08_card_blank, w08_card_spotify, w08_card_netflix, w08_card_duolingo, w08_card_humane,
               w08_card_rabbit, w08_wizard, w08_grain, w08_sprints, w08_git, w08_ladder):
        svg, png = fn()
        print(png, len(svg))
