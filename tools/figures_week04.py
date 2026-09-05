"""
Drawn figures for week 4 · Language machines. Every function name and every c.finish name starts
with w04_ / w04- (the generated files share one folder). Each figure explains a mechanism:
tokens, the embedding map, the lineage of the chain, temperature, the training pipeline, the
context window, the agent loop, the spec that becomes a brief, and what three briefs get back.
Token counts in w04_tokens_split were measured with tiktoken (cl100k_base, GPT-4's tokenizer).
"""
from __future__ import annotations

import math
import random

from figures import Canvas, _arrow, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#F4F4F2'
PALETTE = ['#D3E7E8', '#E5DAEB', '#F9E5D6', '#F7E3E8', '#F8DEB1']   # teal, violet, orange, pink, yellow tints


# ───────────────────────── text → tokens ─────────────────────────
# measured with tiktoken cl100k_base on 2026-09-05; the boxes are the real pieces
TOK_EN = ['Design', ' a', ' poster', ' for', ' the', ' week', '-', '13', ' poster', ' fair', '.']
TOK_ZH = ['�', '�', '�', '第', '十', '三', '�', '�', '的', '海', '報', '展', '�', '�', '計', '一', '�', '�', '海', '報', '。']
TOK_WORDS = [('tokenization', ['token', 'ization']), ('unbelievable', ['un', 'belie', 'vable']), ('hallucination', ['hall', 'uc', 'ination']), ('p5.js', ['p', '5', '.js'])]


CJK_FONTS = ['/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
             '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc', '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
             '/System/Library/Fonts/PingFang.ttc', 'C:/Windows/Fonts/msjh.ttc']


def _cjk_font(px):
    """A font with Chinese glyphs for the PIL backend, or None (the SVG side always has the browser's fallback)."""
    import os
    from PIL import ImageFont
    for path in CJK_FONTS:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, px)
            except Exception:
                continue
    return None


def _is_cjk(t):
    return any('\u3000' <= ch <= '\u9fff' or '\uff00' <= ch <= '\uffef' for ch in t)


def _cjk_text(c, x, y, t, size=22, color=INK):
    """Chinese text: SVG with a CJK fallback stack; PIL with a CJK font when the machine has one, else a block per character."""
    fam = "'Noto Sans CJK TC','PingFang TC','Microsoft JhengHei','Inter',sans-serif"
    c.svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" font-weight="500" fill="{color}">{t}</text>')
    f = _cjk_font(round(c.s(size)))
    if f is None:
        for i, _ch in enumerate(t):     # no CJK font here: one block per character, so the count still reads
            c.d.rectangle([c.s(x + i * size * 1.05), c.s(y - size * 0.85), c.s(x + i * size * 1.05 + size * 0.9), c.s(y)], fill='#B3B7BE')
        return size * 1.05 * len(t)
    asc, _d = f.getmetrics()
    c.d.text((c.s(x), c.s(y) - asc), t, font=f, fill=color)
    return f.getlength(t) / c.scale


def _token_row(c, x, y, toks, size=22, h=44, gap=6, pad=12, mono=True):
    """Draw tokens as tinted boxes in a row; returns the x after the last box.
    A leading space is drawn as a small hollow square; a byte piece (part of one character) as a small grey block."""
    from deckgen import pil_font
    f = pil_font('monomed' if mono else 'semibold', round(c.s(size)))
    for i, t in enumerate(toks):
        fill = PALETTE[i % len(PALETTE)]
        if t == '\ufffd':
            w = size + 2 * pad
            c.rect(x, y, w, h, fill=fill)
            c.rect(x + pad + size * 0.2, y + h / 2 - size * 0.3, size * 0.6, size * 0.6, fill='#B3B7BE')
        elif _is_cjk(t):
            w = size * 1.1 + 2 * pad
            c.rect(x, y, w, h, fill=fill)
            _cjk_text(c, x + pad, y + h / 2 + size * 0.36, t, size=size)
        else:
            sp = t.startswith(' ')
            label = t.strip() if sp else t
            tw = f.getlength(label) / c.scale + (size * 0.8 if sp else 0)
            w = tw + 2 * pad
            c.rect(x, y, w, h, fill=fill)
            if sp:
                c.rect(x + pad, y + h / 2 - size * 0.22, size * 0.44, size * 0.44, stroke=MUTED, width=1.5)
            c.text(x + pad + (size * 0.8 if sp else 0), y + h / 2 + size * 0.36, label, size=size, color=INK, mono=mono)
        x += w + gap
    return x


def w04_tokens_split(name='w04-tokens-split', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'THE SAME BRIEF, TWO LANGUAGES, ONE TOKENIZER (GPT-4, cl100k_base)', size=18, color=ORANGE)
    # English
    c.text(0, 90, 'Design a poster for the week-13 poster fair.', size=26, color=INK, mono=False)
    _token_row(c, 0, 112, TOK_EN, size=22)
    c.text(0, 196, f'{len(TOK_EN)} tokens · 44 characters · 8 words', size=20, color=INK)
    c.text(0, 226, 'the small square is a leading space: " poster" and "poster" are different tokens', size=16, color=MUTED)
    c.text(w, 196, 'rule of thumb: one token ≈ 4 characters ≈ ¾ of an English word', size=18, anchor='end', color=MUTED)
    # Chinese
    _cjk_text(c, 0, 262, '為第十三週的海報展設計一張海報。', size=26)
    _token_row(c, 0, 284, TOK_ZH, size=22)
    c.text(0, 368, f'{len(TOK_ZH)} tokens · 16 characters · almost twice the cost of the English', size=20, color=INK)
    c.text(0, 398, 'a grey block is a piece of one character: one byte of it', size=16, color=MUTED)
    c.text(w, 368, 'vocabulary: about 100,000 pieces, learned from data (byte-pair encoding)', size=18, anchor='end', color=MUTED)
    # words that split
    c.text(0, 440, 'WORDS ARE NOT THE UNIT', size=18, color=ORANGE)
    x = 0
    for word, parts in TOK_WORDS:
        c.text(x, 484, word, size=20, color=MUTED)
        x2 = _token_row(c, x, 496, parts, size=20, h=40, pad=10)
        x = max(x2, x + 240) + 40
    c.text(w, 516, 'the model never sees letters: it sees these pieces, as numbers', size=18, anchor='end', color=MUTED)
    return c.finish(name)


# ───────────────────────── tokens → embeddings ─────────────────────────
# the same 40 hand-placed words as the live sketch w04-embeddings (canvas 1400 x 520)
WORDS = [
    ('chair', 300, 150), ('stool', 250, 190), ('sofa', 340, 200), ('bench', 240, 130), ('table', 400, 160), ('desk', 410, 210), ('shelf', 340, 240),
    ('red', 1150, 120), ('blue', 1200, 160), ('green', 1120, 180), ('yellow', 1240, 110), ('black', 1180, 220),
    ('draw', 700, 400), ('paint', 760, 430), ('sketch', 650, 440), ('render', 780, 380), ('print', 720, 470), ('model', 640, 380),
    ('wood', 230, 410), ('steel', 170, 440), ('glass', 290, 460), ('fabric', 210, 480), ('concrete', 130, 390),
    ('font', 1050, 380), ('serif', 1100, 420), ('kerning', 1010, 440), ('grid', 1150, 380), ('layout', 1090, 340),
    ('designer', 620, 130), ('client', 700, 100), ('user', 660, 180), ('curator', 740, 150), ('brief', 590, 200),
    ('prompt', 900, 250), ('token', 950, 300), ('data', 860, 300), ('rule', 920, 200),
    ('king', 590, 305), ('queen', 520, 345), ('man', 470, 305), ('woman', 400, 345),
]


def w04_embedding_map(name='w04-embedding-map', w=1680, h=560):
    c = Canvas(w, h)
    sx, sy = (w - 80) / 1400, (h - 60) / 520
    ox, oy = 40, 20
    pt = {wd: (ox + x * sx, oy + y * sy) for wd, x, y in WORDS}
    # faint axes through the middle: no names
    c.line(ox, oy + 260 * sy, ox + 1400 * sx, oy + 260 * sy, LINE, 2, cap='butt')
    c.line(ox + 700 * sx, oy, ox + 700 * sx, oy + 520 * sy, LINE, 2, cap='butt')
    c.text(ox + 1400 * sx, oy + 260 * sy - 12, 'axis 1 · no name', size=16, anchor='end')
    c.text(ox + 700 * sx + 10, oy + 18, 'axis 2 · no name', size=16)
    # the analogy: two parallel arrows
    for a, b in (('man', 'woman'), ('king', 'queen')):
        (x1, y1), (x2, y2) = pt[a], pt[b]
        _arrow(c, x1, y1, x2, y2, ORANGE, 3, 10)
    c.text((pt['man'][0] + pt['king'][0]) / 2, pt['man'][1] - 30, 'king − man + woman ≈ queen', size=18, anchor='middle', color=ORANGE)
    # clusters
    groups = {'furniture': ('chair', 'stool', 'sofa', 'bench', 'table', 'desk', 'shelf'), 'colours': ('red', 'blue', 'green', 'yellow', 'black'),
              'making': ('draw', 'paint', 'sketch', 'render', 'print', 'model'), 'materials': ('wood', 'steel', 'glass', 'fabric', 'concrete'),
              'type': ('font', 'serif', 'kerning', 'grid', 'layout'), 'people': ('designer', 'client', 'user', 'curator', 'brief')}
    for g, members in groups.items():
        xs = [pt[m][0] for m in members]; ys = [pt[m][1] for m in members]
        cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
        r = max(math.hypot(x - cx, y - cy) for x, y in zip(xs, ys)) + 26
        c.circle(cx, cy, r, fill=None, stroke=TEAL, width=2)
        c.text(cx, cy - r - 8, g, size=16, anchor='middle', color=TEAL)
    for wd, (x, y) in pt.items():
        c.circle(x, y, 5, fill=INK)
        c.text(x + 10, y + 6, wd, size=18, color=INK)
    c.text(ox, h - 8, 'nearby means used alike: positions learned from which words keep company (Firth 1957 · word2vec 2013). Real embeddings: thousands of axes, none with a name.', size=16, color=MUTED)
    return c.finish(name)


# ───────────────────────── the lineage of the chain ─────────────────────────
def w04_chain_lineage(name='w04-chain-lineage', w=1680, h=560):
    c = Canvas(w, h)
    cols = [
        ('1913 · MARKOV', 'Pushkin, 20,000 letters', 'vowel or consonant?', 'memory: 1 letter', 'The next letter depends on the last one. The first Markov chain, counted by hand.'),
        ('1948 · SHANNON', 'a table of word pairs', 'THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER THAT THE CHARACTER OF THIS POINT IS…', 'memory: 1 word', 'Choose each word by the frequency with which it follows the last. Almost English.'),
        ('1957 · 1966 · HILLER · NAKE', 'notes · signs', 'stay 60% · drift 25% · jump 15%', 'memory: 1 sign', 'The Illiac Suite and Walk-Through-Raster: the same chain, in sound and on a plotter (week 2).'),
        ('2018 → · GPT', 'the whole internet', 'p(next token | everything so far)', 'memory: thousands of tokens', 'The table is too big to write down, so it is learned: a network that gives the next-token odds.'),
    ]
    cw, gap = 390, 40
    for i, (head, data, sample, mem, body) in enumerate(cols):
        x = i * (cw + gap)
        c.rect(x, 0, cw, 500, fill=PAPER)
        c.text(x + 24, 44, head, size=18, color=ORANGE)
        c.text(x + 24, 90, data, size=20, color=INK)
        # the chain: dots and arrows
        n = 5 + i * 2
        for k in range(n):
            px = x + 34 + k * (cw - 68) / (n - 1)
            c.circle(px, 150, 8, fill=INK if k < n - 1 else ORANGE)
            if k < n - 1:
                c.line(px + 10, 150, px + (cw - 68) / (n - 1) - 10, 150, MUTED, 2, cap='butt')
        c.text(x + 24, 200, mem, size=18, color=VIOLET)
        # sample text, wrapped by hand
        words = sample.split(' ')
        line, y = '', 250
        for wd in words + ['']:
            if wd and len(line + ' ' + wd) < 30:
                line = (line + ' ' + wd).strip()
            else:
                c.text(x + 24, y, line, size=17, color=INK)
                y += 26
                line = wd
        # body, wrapped
        words = body.split(' ')
        line, y = '', 390
        for wd in words + ['']:
            if wd and len(line + ' ' + wd) < 34:
                line = (line + ' ' + wd).strip()
            else:
                c.text(x + 24, y, line, size=17, color=MUTED, mono=False)
                y += 26
                line = wd
        if i < 3:
            _arrow(c, x + cw + 6, 150, x + cw + gap - 6, 150, INK, 3, 10)
    c.text(0, 545, 'One idea, a century long: the next thing depends on what came before. What grew is the memory, and the size of the table.', size=18, color=MUTED)
    return c.finish(name)


# ───────────────────────── temperature ─────────────────────────
NEXT_WORDS = [('draft', 0.34), ('brief', 0.22), ('picture', 0.14), ('rule', 0.10), ('poster', 0.08), ('chair', 0.06), ('sentence', 0.04), ('mistake', 0.02)]


def _temper(ps, t):
    if t <= 0.001:
        return [1.0 if i == 0 else 0.0 for i in range(len(ps))]
    z = [p ** (1 / t) for p in ps]
    s = sum(z)
    return [v / s for v in z]


def w04_temperature(name='w04-temperature', w=1680, h=560):
    c = Canvas(w, h)
    c.text(0, 30, 'THE MACHINE WRITES: "a model writes a …"  ·  the next-token odds, reshaped by temperature', size=18, color=ORANGE)
    panels = [(0.2, 'T = 0.2 · cold · the same word every time'), (1.0, 'T = 1 · the odds as learned'), (1.5, 'T = 1.5 · hot · the long tail wakes up')]
    pw = 520
    for i, (t, label) in enumerate(panels):
        x = i * (pw + 60)
        ps = _temper([p for _, p in NEXT_WORDS], t)
        c.rect(x, 70, pw, 400, fill=PAPER)
        for k, ((wd, _p0), p) in enumerate(zip(NEXT_WORDS, ps)):
            y = 92 + k * 46
            c.text(x + 20, y + 26, wd, size=18, color=INK)
            bw = max(2, p * 320)
            c.rect(x + 140, y + 6, bw, 30, fill=ORANGE if k == 0 else TEAL)
            c.text(x + 148 + bw, y + 27, f'{p * 100:.0f}%', size=16, color=MUTED)
        c.text(x + pw / 2, 505, label, size=18, anchor='middle', color=INK)
    c.text(0, 548, 'p ~ odds^(1/T), normalised. Temperature 0 = always the top word (deterministic). The die is thrown on these bars; the bars come from the examples.', size=17, color=MUTED)
    return c.finish(name)


# ───────────────────────── pre-training → fine-tuning → RLHF ─────────────────────────
def w04_pipeline(name='w04-pipeline', w=1680, h=560):
    c = Canvas(w, h)
    stages = [
        ('1 · PRE-TRAINING', 'the base model', 'Trillions of tokens of text. One task: guess the next token; nudge every weight when wrong. Months, thousands of GPUs.',
         'GPT-3, 2020: 175 billion weights', 'It completes. Ask it a question and it may answer with more questions.'),
        ('2 · INSTRUCTION TUNING', 'show it examples', 'Thousands of hand-written pairs: an instruction and a good answer. The base model learns the shape of a reply.',
         'InstructGPT, 2022', 'Machine B, shown examples of being helpful.'),
        ('3 · RLHF', 'people rank answers', 'Two answers to one prompt; a person picks the better one, many thousand times. A reward model learns the taste; the model is trained to please it.',
         'ChatGPT, 30 Nov 2022', 'Where sycophancy comes from: the taste of the raters.'),
    ]
    sw, gap = 500, 90
    for i, (head, sub, body, stamp, verdict) in enumerate(stages):
        x = i * (sw + gap)
        c.rect(x, 20, sw, 470, fill=PAPER)
        c.text(x + 24, 64, head, size=18, color=ORANGE)
        c.text(x + 24, 106, sub, size=26, color=INK, mono=False, weight=700)
        words, line, y = body.split(' '), '', 156
        for wd in words + ['']:
            if wd and len(line + ' ' + wd) < 40:
                line = (line + ' ' + wd).strip()
            else:
                c.text(x + 24, y, line, size=18, color=INK, mono=False)
                y += 28
                line = wd
        c.text(x + 24, 360, stamp, size=18, color=VIOLET)
        words, line, y = verdict.split(' '), '', 410
        for wd in words + ['']:
            if wd and len(line + ' ' + wd) < 40:
                line = (line + ' ' + wd).strip()
            else:
                c.text(x + 24, y, line, size=17, color=MUTED, mono=False)
                y += 26
                line = wd
        if i < 2:
            _arrow(c, x + sw + 10, 250, x + sw + gap - 10, 250, INK, 4, 12)
    c.text(0, 540, 'Machine B three times over: examples of language, then examples of instructions, then examples of what people prefer. Nobody wrote a rule.', size=18, color=MUTED)
    return c.finish(name)


# ───────────────────────── the context window ─────────────────────────
def w04_context_window(name='w04-context-window', w=1680, h=400):
    c = Canvas(w, h)
    segs = [('SYSTEM PROMPT', 'the product designer’s brief: who the model is, what it may not do', 300, '#E5DAEB'),
            ('YOUR BRIEF', 'goal · audience · constraints · what to leave out', 300, '#F9E5D6'),
            ('EXAMPLES', 'two briefs you like', 220, '#F8DEB1'),
            ('THE CONVERSATION SO FAR', 'every turn, yours and its, in order', 520, '#D3E7E8'),
            ('THE ANSWER', 'written one token at a time', 260, '#F7E3E8')]
    x, y0, hh = 40, 120, 120
    for head, sub, sw, col in segs:
        c.rect(x, y0, sw, hh, fill=col)
        c.text(x + 16, y0 + 40, head, size=16, color=INK)
        words, line, yy = sub.split(' '), '', y0 + 72
        for wd in words + ['']:
            if wd and len(line + ' ' + wd) * 10 < sw - 24:
                line = (line + ' ' + wd).strip()
            else:
                c.text(x + 16, yy, line, size=15, color=MUTED, mono=False)
                yy += 22
                line = wd
        x += sw + 6
    # the window bracket
    c.line(40, 90, x - 6, 90, INK, 3, cap='butt'); c.line(40, 90, 40, 110, INK, 3, cap='butt'); c.line(x - 6, 90, x - 6, 110, INK, 3, cap='butt')
    c.text(40, 70, 'THE CONTEXT WINDOW · everything the model can see right now · measured in tokens', size=18, color=ORANGE)
    # the answer arrow: reading direction
    _arrow(c, 40, 280, x - 6, 280, MUTED, 3, 10)
    c.text(40, 316, 'read left to right, every token attending to every token before it', size=16, color=MUTED)
    c.text(x - 6, 316, 'the next token is predicted from all of this', size=16, anchor='end', color=MUTED)
    c.text(40, 362, 'What is not in the window does not exist for the model: not last week’s chat, not your files, not the web — unless a tool puts it here.', size=16, color=MUTED)
    c.text(40, 388, 'Sizes: a few thousand tokens in 2022; hundreds of thousands, and for some models a million or more, now.', size=16, color=MUTED)
    return c.finish(name)


# ───────────────────────── the agent loop ─────────────────────────
def w04_agent_loop(name='w04-agent-loop', w=1680, h=560):
    c = Canvas(w, h)
    cx, cy, r = 470, 250, 160
    nodes = [('PLAN', ('the model writes', 'what to do next'), -90), ('ACT', ('it calls a tool: search,', 'calculator, code, files'), 30), ('OBSERVE', ('the result goes back', 'into the window'), 150)]
    pts = []
    for head, sub, ang in nodes:
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        pts.append((x, y))
    for i in range(3):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 3]
        dx, dy = x2 - x1, y2 - y1
        d = math.hypot(dx, dy)
        _arrow(c, x1 + dx / d * 70, y1 + dy / d * 70, x2 - dx / d * 74, y2 - dy / d * 74, INK, 4, 12)
    for (head, sub, ang), (x, y) in zip(nodes, pts):
        c.circle(x, y, 64, fill=ORANGE if head == 'ACT' else PAPER, stroke=INK, width=3)
        c.text(x, y + 8, head, size=20, anchor='middle', color=INK)
    for (head, sub, ang), (x, y) in zip(nodes, pts):
        for k, ln in enumerate(sub):
            if head == 'PLAN':
                c.text(x + 80, y - 4 + k * 22, ln, size=16, color=MUTED)
            else:
                c.text(x, y + 90 + k * 22, ln, size=16, anchor='middle', color=MUTED)
    c.text(cx, cy + 20, 'until done,', size=15, anchor='middle', color=MUTED)
    c.text(cx, cy + 40, 'or a person says stop', size=15, anchor='middle', color=MUTED)
    # the tools on the right
    tx = 1000
    c.text(tx, 60, 'THE TOOLS ARE MACHINE A', size=18, color=ORANGE)
    tools = [('search', 'a query in, ten links out — the model reads them into its window'), ('calculator · code runner', 'the model writes the sum or the program; a computer executes it exactly'),
             ('your files, a calendar, an API', 'anything with an interface can be a tool; week 12 designs that interface'), ('another model', 'a planner briefs a writer briefs a checker: agents all the way down')]
    for i, (t, sub) in enumerate(tools):
        y = 110 + i * 100
        c.rect(tx, y, 640, 78, fill=PAPER)
        c.text(tx + 20, y + 32, t, size=19, color=INK)
        c.text(tx + 20, y + 60, sub, size=15, color=MUTED, mono=False)
    c.text(0, 545, 'ReAct, 2022: reasoning and acting interleaved. The model is fluent and fuzzy; the tools are exact. Together: a machine that can check itself, when the loop is designed to.', size=16, color=MUTED)
    return c.finish(name)


# ───────────────────────── the week-2 spec becomes a brief ─────────────────────────
def w04_spec_to_brief(name='w04-spec-to-brief', w=1680, h=560):
    c = Canvas(w, h)
    left = [('RULE', 'what is drawn, how many, how they relate'), ('CHANCE', 'what is random, and how much'), ('NUMBERS', 'canvas, counts, sizes, colours'), ('CONSTRAINTS', 'no libraries · draw once · a seed'), ('OUTPUT', 'the whole sketch, nothing else')]
    right = [('GOAL', 'what the thing must do, in one sentence'), ('AUDIENCE', 'who it is for, and what they already know'), ('CONSTRAINTS', 'format, length, tone, brand, budget, deadline'), ('EXAMPLES', 'two you like, one you do not — and why'), ('OUTPUT FORMAT', 'headings, length, a table, a list, a file'), ('LEAVE OUT', 'what the model would add if you let it')]
    c.text(0, 30, 'WEEK 2 · A SPEC FOR A MACHINE THAT DRAWS', size=18, color=ORANGE)
    c.text(940, 30, 'WEEK 4 · A BRIEF FOR A MACHINE THAT WRITES', size=18, color=ORANGE)
    for i, (h1, s1) in enumerate(left):
        y = 70 + i * 92
        c.rect(0, y, 640, 76, fill=PAPER)
        c.text(20, y + 32, h1, size=19, color=INK)
        c.text(20, y + 60, s1, size=15, color=MUTED, mono=False)
    for i, (h2, s2) in enumerate(right):
        y = 70 + i * 78
        c.rect(940, y, 740, 64, fill='#E5DAEB' if i == 5 else PAPER)
        c.text(960, y + 28, h2, size=19, color=INK)
        c.text(960, y + 52, s2, size=15, color=MUTED, mono=False)
    links = [(0, 0), (1, 5), (2, 2), (3, 2), (4, 4), (0, 1), (2, 3)]
    for a, b in links:
        y1 = 70 + a * 92 + 38
        y2 = 70 + b * 78 + 32
        c.line(640, y1, 940, y2, ORANGE if (a, b) in ((1, 5), (2, 3)) else LINE, 3 if (a, b) in ((1, 5), (2, 3)) else 2, cap='butt')
    c.text(0, 548, 'Same habits, one new heading: leave out. Where the spec said "chance", the brief says what the model may not decide for you.', size=17, color=MUTED)
    return c.finish(name)


# ───────────────────────── one job, three briefs: what comes back ─────────────────────────
def w04_three_briefs(name='w04-three-briefs', w=1680, h=560):
    c = Canvas(w, h)
    rows = [('ONE LINE', '"Write a brief for a poster for a student design fair."', 1.0, 'the middle: the typical brief, for the typical fair'),
            ('A PARAGRAPH', 'the fair, the room, the date, who walks past, three constraints', 0.45, 'closer: still the model’s structure, your facts'),
            ('A STRUCTURED BRIEF', 'goal · audience · constraints · two examples · format · leave out', 0.14, 'yours: the model fills in a shape you drew')]
    rnd = random.Random(4)
    x0, x1 = 700, 1420
    c.text(x0, 30, 'WHAT COMES BACK · a hundred runs of the same brief', size=18, color=ORANGE)
    c.text(x1 + 30, 30, 'the brief you meant', size=16, color=VIOLET)
    c.line(x1, 50, x1, 500, VIOLET, 2, cap='butt')
    for i, (head, brief, spread, verdict) in enumerate(rows):
        y = 90 + i * 150
        c.rect(0, y - 20, 640, 120, fill=PAPER)
        c.text(20, y + 14, head, size=19, color=INK)
        words, line, yy = brief.split(' '), '', y + 46
        for wd in words + ['']:
            if wd and len(line + ' ' + wd) < 56:
                line = (line + ' ' + wd).strip()
            else:
                c.text(20, yy, line, size=16, color=MUTED, mono=False)
                yy += 24
                line = wd
        # the spread of outputs: dots along a line, centred on the model's middle (left) drifting to the target (right)
        centre = x0 + 120 + (1 - spread) * (x1 - x0 - 120)
        for _ in range(60):
            dx = rnd.gauss(0, spread * 240 + 12)
            dy = rnd.gauss(0, 18)
            c.circle(min(max(centre + dx, x0), x1 + 60), y + 40 + dy, 4, fill=ORANGE if abs(dx) < 40 and spread < 0.2 else TEAL)
        c.text(x0, y + 100, verdict, size=16, color=INK, mono=False)
    c.text(x0, 60, 'the model’s middle', size=16, color=MUTED)
    c.text(0, 548, 'The model does what you said. The less you say, the more it fills in from its middle — and its middle is the average brief on the internet.', size=17, color=MUTED)
    return c.finish(name)


if __name__ == '__main__':
    for fn in (w04_tokens_split, w04_embedding_map, w04_chain_lineage, w04_temperature, w04_pipeline, w04_context_window, w04_agent_loop, w04_spec_to_brief, w04_three_briefs):
        svg, png = fn()
        print(png, len(svg))


# ───────────────────────── side figures (800 wide) for the content slides ─────────────────────────
def w04_guess_or_blank(name='w04-guess-or-blank', w=800, h=700):
    """The exam that rewards guessing: ten questions, two policies, two ways of scoring (after Kalai et al., 2025)."""
    c = Canvas(w, h)
    c.text(0, 30, 'TEN QUESTIONS · THE MODEL IS SURE OF SIX', size=18, color=ORANGE)
    # question outcomes: (right, wrong, blank) per cell
    sure_only = ['R'] * 6 + ['B'] * 4
    always_guess = ['R'] * 6 + ['R', 'W', 'W', 'W']
    cols = {'R': TEAL, 'W': ORANGE, 'B': '#E1E1DE'}
    rows = [('SAY "I DON\'T KNOW" WHEN UNSURE', sure_only), ('ALWAYS GUESS', always_guess)]
    for i, (label, cells) in enumerate(rows):
        y = 90 + i * 150
        c.text(0, y, label, size=18, color=INK)
        for k, v in enumerate(cells):
            c.rect(k * 62, y + 20, 52, 52, fill=cols[v])
            c.text(k * 62 + 26, y + 54, {'R': '✓', 'W': '✗', 'B': '—'}[v], size=22, anchor='middle', color=INK if v != 'W' else '#FFFFFF')
        r, wr = cells.count('R'), cells.count('W')
        c.text(0, y + 106, f'right {r} · wrong {wr} · blank {cells.count("B")}', size=16, color=MUTED)
    # scoring
    c.text(0, 410, 'SCORED THE USUAL WAY · right = 1, wrong = 0, blank = 0', size=16, color=ORANGE)
    c.text(0, 445, '"I don\'t know": 6        always guess: 7   ← guessing wins', size=18, color=INK)
    c.text(0, 510, 'SCORED WITH A PENALTY · right = 1, wrong = −1, blank = 0', size=16, color=ORANGE)
    c.text(0, 545, '"I don\'t know": 6        always guess: 4   ← honesty wins', size=18, color=INK)
    c.text(0, 620, 'Most benchmarks score the usual way. A model trained to score', size=16, color=MUTED)
    c.text(0, 646, 'well learns to guess: fluent, plausible, and sometimes wrong.', size=16, color=MUTED)
    c.text(0, 672, 'Change the exam and the guessing stops paying. — Kalai et al., 2025', size=16, color=MUTED)
    return c.finish(name)


def w04_thumbs(name='w04-thumbs', w=800, h=700):
    """RLHF in one incident: two answers, a thumb, a reward model that learns what the thumb likes."""
    c = Canvas(w, h)
    c.text(0, 30, 'ONE PROMPT · TWO ANSWERS · ONE THUMB', size=18, color=ORANGE)
    c.rect(0, 60, 800, 60, fill=PAPER)
    c.text(20, 98, '"Here is my poster idea. What do you think?"', size=20, color=INK, mono=False)
    boxes = [('ANSWER 1', '"Brilliant idea — bold, fresh, sure to stand out!"', '#F7E3E8', '+1  chosen'),
             ('ANSWER 2', '"Three problems: the title is unreadable from 3 m, …"', '#D3E7E8', ' 0  rejected')]
    for i, (head, body, col, verdict) in enumerate(boxes):
        y = 150 + i * 130
        c.rect(0, y, 560, 100, fill=col)
        c.text(20, y + 34, head, size=16, color=INK)
        c.text(20, y + 70, body, size=17, color=INK, mono=False)
        c.text(600, y + 60, verdict, size=20, color=ORANGE if i == 0 else MUTED)
    _arrow(c, 400, 420, 400, 470, INK, 4, 12)
    c.rect(100, 480, 600, 70, fill=INK)
    c.text(400, 523, 'REWARD MODEL LEARNS: PRAISE WINS', size=18, anchor='middle', color='#FFFFFF')
    _arrow(c, 400, 560, 400, 610, INK, 4, 12)
    c.text(400, 645, 'the next model praises more, and is trained to', size=17, anchor='middle', color=INK, mono=False)
    c.text(400, 672, 'thousands of clicks, and nobody wrote "flatter the user"', size=16, anchor='middle', color=MUTED, mono=False)
    return c.finish(name)


def w04_window_stack(name='w04-window-stack', w=800, h=700):
    """The context window as a stack: the system prompt first, then the turns, then the answer being written."""
    c = Canvas(w, h)
    c.text(0, 30, 'THE WINDOW, TOP TO BOTTOM', size=18, color=ORANGE)
    segs = [('SYSTEM PROMPT', 'who the model is · what it may not do · how to talk · what to leave out', 110, '#E5DAEB', True),
            ('YOU', 'the brief: goal, audience, constraints, examples, output, leave out', 74, '#F9E5D6', False),
            ('MODEL', 'the first draft', 44, '#D3E7E8', False),
            ('YOU', '"shorter; no tagline; write to confirm where you do not know"', 60, '#F9E5D6', False),
            ('MODEL', 'the second draft', 44, '#D3E7E8', False),
            ('YOU', '…', 36, '#F9E5D6', False),
            ('MODEL', 'the answer being written, one token at a time', 60, '#F7E3E8', False)]
    y = 60
    for head, sub, hh, col, strong in segs:
        c.rect(0, y, 800, hh, fill=col, stroke=INK if strong else None, width=3)
        c.text(20, y + 30, head, size=16, color=INK)
        c.text(20, y + 54 if hh > 44 else y + 30, sub, size=15 if hh > 44 else 15, color=MUTED if not strong else INK, mono=False) if hh > 44 else c.text(140, y + 30, sub, size=15, color=MUTED, mono=False)
        y += hh + 8
    _arrow(c, 770, 60, 770, y - 8, MUTED, 3, 10)
    c.text(0, y + 30, 'The model reads all of it, every time it writes a token.', size=16, color=INK, mono=False)
    c.text(0, y + 56, 'The system prompt is a brief the product designer wrote before you arrived;', size=15, color=MUTED, mono=False)
    c.text(0, y + 80, 'the model weighs it more than your message. Too long a chat, and the top falls off.', size=15, color=MUTED, mono=False)
    return c.finish(name)
