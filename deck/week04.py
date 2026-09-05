"""
SD2112 · Artificial Intelligence in Design · Week 04 — the slide spec.

    python deck/week04.py            # builds _site/week04/ (html deck + pdf), export/week04*.pptx, export/preview/
    python deck/week04.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Language machines: module 2 opens. Text → tokens → embeddings → attention → the next token, and
temperature; base and instruction-tuned models, the context window; hallucination, sycophancy,
agents; prompting as briefing, and the activity "Brief it three ways". Four live p5.js sketches
(a toy tokenizer, an embedding map, an attention row, a bigram machine that writes by dice and a
table) run in the html deck; the pptx and the PDF show their snapshots.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week04 as F                              # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, code_slide, sketch_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(4)

# ───────────────────────── the live sketches (p5.js) ─────────────────────────
# (a) a toy tokenizer: type a sentence, see the pieces and the count
TOKENS_CODE = """// a toy tokenizer: real ones learn the pieces from data
const W = 1400, H = 520;
const SAMPLES = ['Design a poster for the week-13 poster fair.',
  'The unbelievable tokenization of hallucination.',
  'Write a one-page brief for a foldable stool, in Cantonese.'];
const SUFFIX = ['ization', 'ation', 'tion', 'ing', 'ness',
  'ment', 'able', 'ly', 'ed', 'er', 'es'];
const TINT = ['#D3E7E8', '#E5DAEB', '#F9E5D6', '#F7E3E8', '#F8DEB1'];
let txt = SAMPLES[0], which = 0;

function pieces(w) {              // a long word breaks into pieces
  let sp = w.startsWith(' ') ? ' ' : '', core = w.trim();
  if (core.length <= 6) return [w];
  for (let s of SUFFIX)           // a common ending is its own piece
    if (core.endsWith(s) && core.length - s.length >= 3)
      return pieces(sp + core.slice(0, -s.length)).concat([s]);
  let out = [];                   // the rest: four letters at a time
  for (let i = 0; i < core.length; i += 4)
    out.push((i ? '' : sp) + core.slice(i, i + 4));
  return out;
}

function tokenize(s) {            // split on spaces and punctuation
  let m = s.match(/ ?[A-Za-z]+| ?\\d+| ?[^\\sA-Za-z\\d]/g) || [];
  return m.flatMap(pieces);
}

function id(t) {                  // a token is a number in a vocabulary
  let h = 7;
  for (let ch of t) h = (h * 31 + ch.charCodeAt(0)) % 100000;
  return h;
}

function setup() { createCanvas(W, H); textFont('sans-serif'); }

function draw() {
  background(255);
  let toks = tokenize(txt), words = txt.trim() ? txt.trim().split(/\\s+/).length : 0;
  fill(120); noStroke(); textSize(15); textAlign(LEFT, BASELINE);
  text('TYPE A SENTENCE  ·  Delete clears  ·  hover a token  ·  click this line for another example', 40, 44);
  textAlign(RIGHT); text('a toy tokenizer: real ones learn the pieces from data', W - 40, 44); textAlign(LEFT);
  textSize(28); fill(0);
  text(txt + (frameCount % 60 < 30 ? '|' : ' '), 40, 100);
  let x = 40, y = 172, hov = -1;   // the token boxes, in rows
  textSize(22);
  for (let i = 0; i < toks.length; i++) {
    let label = toks[i].replace(' ', '\\u2423'), w = textWidth(label) + 26;
    if (x + w > W - 40) { x = 40; y += 56; }
    if (mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + 44) hov = i;
    fill(TINT[i % 5]); noStroke();
    if (hov === i) { stroke(0); strokeWeight(2); }
    rect(x, y, w, 44, 4);
    fill(0); noStroke(); text(label, x + 13, y + 30);
    if (hov === i) { fill(237, 109, 36); textSize(15); text('token #' + id(toks[i]), x, y - 8); textSize(22); }
    x += w + 8;
  }
  let count = toks.length + ' tokens';   // one bottom line: the last 60 px stay free for the LIVE chip
  fill(0); textSize(44); text(count, 40, H - 60);
  let sx = 70 + textWidth(count);
  fill(120); textSize(18);
  text(txt.length + ' characters  ·  ' + words + ' words  ·  about ' + (txt.length / max(toks.length, 1)).toFixed(1) + ' characters per token', sx, H - 60);
}

function keyPressed() {           // typing edits the sentence
  if (keyCode === BACKSPACE) { txt = txt.slice(0, -1); return false; }
  if (keyCode === DELETE) { txt = ''; return false; }
  if (key.length === 1) { txt += key; return false; }
}

function mousePressed() {         // a click on the top line: another example
  if (mouseY < 60) { which = (which + 1) % SAMPLES.length; txt = SAMPLES[which]; }
}"""

# Appended to the sketch page only. The page forwards the deck's keys (space, S, O, F; R reloads) to reveal.js unless
# the sketch has claimed them; p5 claims them too late (keyPressed runs after the forwarder), so typed keys are claimed
# here in the capture phase: 'a poster' stays in the sketch, and the arrows and Escape still reach the deck.
TOKENS_EXTRA = """window.addEventListener('keydown', e => {
  if (!e.metaKey && !e.ctrlKey && !e.altKey && (e.key.length === 1 || e.key === 'Backspace' || e.key === 'Delete')) e.preventDefault();
}, true);"""

# (b) a bigram machine: the next word depends on the last one — a Markov chain, like Nake's, with a temperature dial
NEXT_TEXT = ('a designer writes a brief . a model writes a draft . the brief is a rule and the draft is a guess . '
             'a rule is exact and a guess is typical . the model learned from examples and the designer learned from clients . '
             'a client wants a poster . a designer wants a chair that nobody has seen . the model wants the middle . '
             'the middle is the typical poster and the typical chair . a good brief moves the model off the middle . '
             'a bad brief gets the middle back . the machine draws every line and the designer writes the rule . '
             'the machine writes every word and the designer writes the brief . the model is fluent and the model is fuzzy '
             'and the model cannot say why . a rule can say why . the designer decides what ships . the designer decides what '
             'the model may not decide . a prompt is a rule for a machine made of examples . show the examples or write the rule . '
             'the brief is the design . a brief is a design . the draft is a guess about the brief . the designer edits the guess .')

NEXT_MODEL = """let table = {}, sent = ['the'], T = 1;  // table, text, heat

function train() {                // count every word pair
  let w = TEXT.split(/\\s+/);
  for (let i = 0; i < w.length - 1; i++) {
    let a = w[i], b = w[i + 1];
    table[a] = table[a] || {};
    table[a][b] = (table[a][b] || 0) + 1;
  }
}
function odds(last) {             // top 8 next words, by heat
  let row = table[last] || {};
  let list = Object.keys(row).map(k => [k, row[k]]);
  list.sort((p, q) => q[1] - p[1]);
  list = list.slice(0, 8);
  let z = list.map(p => pow(p[1], 1 / T));  // temperature
  let s = z.reduce((a, b) => a + b, 0);
  return list.map((p, i) => [p[0], z[i] / s]);
}
function pick(list) {             // one throw of the die
  let r = random(), acc = 0;
  for (let [w, p] of list) if ((acc += p) > r) return w;
  return list[list.length - 1][0];
}"""

NEXT_DRAW = """function setup() {
  createCanvas(W, H); randomSeed(4); train(); textFont('sans-serif');
  T = 0.7;                         // a few words to start with
  for (let i = 0; i < 9; i++) sent.push(pick(odds(sent[sent.length - 1])));
}

function draw() {
  background(255);
  T = constrain(map(mouseY, 40, H - 40, 0.2, 1.5), 0.2, 1.5);
  let PW = min(420, W * 0.45), px = W - PW - 30;
  // the sentence so far, wrapped; the oldest lines scroll off the top
  noStroke(); fill(120); textSize(15); textAlign(LEFT, BASELINE);
  text(W > 1000 ? 'THE MACHINE WRITES  ·  click: next word  ·  mouse up/down: temperature  ·  C: start again' : 'click: next word · mouse: heat · C: reset', 30, 40);
  textSize(24); fill(0);
  let x = 30, rows = [], row = '';
  for (let w of sent) {
    let piece = (w === '.' ? '.' : (row ? ' ' : '') + w);
    if (textWidth(row + piece) > px - 60) { rows.push(row); row = w; }
    else row += piece;
  }
  rows.push(row);
  let y = 90, first = max(0, rows.length - floor((H - 190) / 34));
  for (let i = first; i < rows.length; i++, y += 34) text(rows[i], x, y);
  fill(237, 109, 36); text('_', x + textWidth(row) + 4, y - 34);
  // the odds of the next word
  let last = sent[sent.length - 1], list = odds(last);
  fill(120); textSize(15);
  text('after "' + last + '"  ·  the next word, top 8', px, 40);
  textSize(18);
  for (let i = 0; i < list.length; i++) {
    let by = 62 + i * 40;
    fill(0); text(list[i][0], px, by + 22);
    fill(i === 0 ? color(237, 109, 36) : color(100, 194, 195));
    rect(px + 110, by + 2, list[i][1] * (PW - 180), 28);
    fill(120); text(round(list[i][1] * 100) + '%', px + 118 + list[i][1] * (PW - 180), by + 23);
  }
  // the temperature dial (the bottom 60 px of the canvas stay free for the LIVE chip)
  let dy = 62 + 8 * 40 + 12;
  fill(0); textSize(18); text('temperature  T = ' + T.toFixed(2), px, dy + 18);
  fill(120); textSize(14); text('0.2 cold', px, dy + 42); textAlign(RIGHT); text('hot 1.5', px + PW - 30, dy + 42);
  stroke(200); strokeWeight(3); line(px, dy + 58, px + PW - 30, dy + 58);
  noStroke(); fill(237, 109, 36); circle(px + map(T, 0.2, 1.5, 0, PW - 30), dy + 58, 14);
  textAlign(LEFT); fill(120); textSize(14);
  text('a Markov chain: the next word depends only on the last one', 30, W > 1000 ? H - 20 : H - 64);
}

function mousePressed() { sent.push(pick(odds(sent[sent.length - 1]))); }

function keyPressed() {
  if (key === 'c' || key === 'C') { sent = ['the']; return false; }
}"""


def next_code(w, h):
    return f'const W = {w}, H = {h};\nconst TEXT = `{NEXT_TEXT}`;   // the examples: 200 words about design\n\n' + NEXT_MODEL + '\n\n' + NEXT_DRAW


# (c) an embedding map: 40 words placed by hand; the mouse is a query; the five nearest light up
EMB_WORDS_JS = ',\n  '.join(f"['{w}', {x}, {y}]" for w, x, y in F.WORDS)
EMBED_CODE = f"""// a word is a point. nearby means used alike. the axes have no names.
const W = 1400, H = 520;
const WORDS = [
  {EMB_WORDS_JS}
];
let cosine = false;                // click: cosine or euclidean

function dist2(a, b) {{             // two ways to measure 'near'
  if (!cosine) return dist(a[0], a[1], b[0], b[1]);
  let ax = a[0] - W / 2, ay = a[1] - H / 2;      // from the origin
  let bx = b[0] - W / 2, by = b[1] - H / 2;
  let cos = (ax * bx + ay * by) / (mag(ax, ay) * mag(bx, by) + 1e-9);
  return 1 - cos;                  // 0 = same direction
}}

function setup() {{ createCanvas(W, H); textFont('sans-serif'); }}

function draw() {{
  background(255);
  let q = [mouseX, mouseY];
  let ranked = WORDS.map(w => [w, dist2(q, [w[1], w[2]])]);
  ranked.sort((a, b) => a[1] - b[1]);
  let near = ranked.slice(0, 5);
  stroke(225); strokeWeight(1);    // two axes, no names
  line(0, H / 2, W, H / 2); line(W / 2, 0, W / 2, H);
  noStroke(); fill(160); textSize(14); textAlign(LEFT, BASELINE);
  text('axis 1 · no name', W - 140, H / 2 - 8); text('axis 2 · no name', W / 2 + 8, 20);
  if (cosine) {{ stroke(237, 109, 36, 90); strokeWeight(1); line(W / 2, H / 2, W / 2 + (mouseX - W / 2) * 4, H / 2 + (mouseY - H / 2) * 4); }}
  for (let [w, x, y] of WORDS) {{  // every word, as a labelled point
    let k = near.findIndex(n => n[0][0] === w);
    if (k >= 0) {{ stroke(237, 109, 36, 120); strokeWeight(2); line(mouseX, mouseY, x, y); }}
    noStroke(); fill(k >= 0 ? color(237, 109, 36) : 0);
    circle(x, y, k >= 0 ? 10 : 6);
    textSize(k >= 0 ? 20 : 17); text(w, x + 9, y + 6);
  }}
  noStroke(); fill(237, 109, 36); circle(mouseX, mouseY, 12);
  fill(0); textSize(16);            // the five nearest and their distances
  text((cosine ? 'COSINE' : 'EUCLIDEAN') + ' · the 5 nearest', 24, 30);
  fill(90); textSize(15);
  for (let i = 0; i < near.length; i++)
    text((i + 1) + '. ' + near[i][0][0] + '  ' + (cosine ? near[i][1].toFixed(3) : round(near[i][1])), 24, 52 + i * 19);
  fill(160); textSize(14); textAlign(RIGHT);   // top right: the bottom stays free for the LIVE chip
  text('nearby means similar  ·  real embeddings have thousands of axes', W - 30, 30);
  text('click: switch the distance', W - 30, 50);
  textAlign(LEFT);
}}

function mousePressed() {{ cosine = !cosine; }}"""

# (d) attention, by hand: hover a word and see how much it looks at the words before it
ATTN_CODE = """// attention, by hand: each token looks back at the ones before it
const W = 800, H = 600;
const S = ['The', 'client', 'loves', 'the', 'chair', 'because', 'it', 'is', 'red', '.'];
const LINKS = {                   // the strong looks; everything else is faint
  1: {0: 0.5}, 2: {1: 0.6}, 3: {2: 0.3}, 4: {3: 0.4, 2: 0.2},
  5: {2: 0.3, 4: 0.3}, 6: {4: 0.65, 1: 0.1}, 7: {6: 0.5, 4: 0.2},
  8: {4: 0.55, 7: 0.15, 6: 0.1}, 9: {8: 0.3, 4: 0.3, 1: 0.1},
};
function weights(i) {             // one row of the attention table, adding up to 1
  let w = [], s = 0;
  for (let j = 0; j < S.length; j++) {
    w[j] = j > i ? 0 : 0.03 + ((LINKS[i] || {})[j] || 0);   // nothing after i
    s += w[j];
  }
  return w.map(v => v / s);
}
function setup() { createCanvas(W, H); textFont('sans-serif'); }
function draw() {
  background(255);
  let n = S.length, sp = 80, x0 = 36, yq = 150, yk = 420;
  let i = constrain(round((mouseX - x0) / sp), 0, n - 1);   // the hovered token
  let w = weights(i);
  noStroke(); fill(120); textSize(14); textAlign(LEFT, BASELINE);
  text('HOVER A WORD  ·  this token looks at …', 30, 40);
  text('… every token before it, this much  (a row of the attention table, sum = 1)', 30, yk + 86);
  for (let j = 0; j < n; j++) {   // the lines: thickness is the weight
    if (w[j] < 0.001) continue;
    stroke(237, 109, 36, 40 + 200 * w[j]); strokeWeight(1 + 16 * w[j]);
    line(x0 + i * sp, yq + 16, x0 + j * sp, yk - 24);
  }
  textAlign(CENTER, CENTER);
  for (let j = 0; j < n; j++) {   // the words, twice: as the looker and as the looked-at
    noStroke(); fill(j === i ? color(237, 109, 36) : 0); textSize(j === i ? 22 : 18);
    text(S[j], x0 + j * sp, yq);
    fill(w[j] > 0.001 ? 0 : 200); textSize(18); text(S[j], x0 + j * sp, yk);
    if (w[j] > 0.001) { fill(120); textSize(13); text(round(w[j] * 100) + '%', x0 + j * sp, yk + 26); }
  }
  noStroke(); fill(120); textSize(14); textAlign(LEFT, BASELINE);
  text('"' + S[i] + '" mostly looks at "' + S[w.indexOf(max(w))] + '"  ·  a real model has many such tables, learned, in every layer', 30, H - 56);
}"""

# ───────────────────────── the briefs on the slides ─────────────────────────
BRIEF_ANATOMY = [
    'GOAL: [what the thing must do, in one sentence]', ' ',
    'AUDIENCE: [who reads or sees it, and what they', 'already know]', ' ',
    'CONSTRAINTS: [format, size, length, tone, brand,', 'deadline, budget]', ' ',
    'EXAMPLES: [two you like, one you do not — and why]', ' ',
    'OUTPUT: [headings, length, a table, a list, a file]', ' ',
    'LEAVE OUT: [what it would add if you let it: stock', 'phrases, a tagline, emoji, "innovative"]',
]

BRIEF_STRUCTURED = [
    'GOAL: an A0 poster that makes a tutor stop for', 'ten seconds and remember one product name.', ' ',
    'AUDIENCE: 114 design students and their tutors,', 'walking past at the week-13 fair. They know', 'what AI is; they have seen 27 other posters.', ' ',
    'CONSTRAINTS: A0 portrait; readable from 3 m; the', 'product name first, the team name second; no', 'stock imagery; our two brand colours.', ' ',
    'EXAMPLES: [two posters we like, one we do not,', 'pasted or linked, with one line on why each]', ' ',
    'OUTPUT: six headings: goal, audience, message,', 'must show, must not show, open questions. 200 words.', ' ',
    'LEAVE OUT: taglines, adjectives, "innovative", anything', 'the brief does not say — write "to confirm".',
]

SYSTEM_PROMPT = [
    "You are a design studio's brief writer.", ' ',
    'The user gives you a product idea in one or two', 'lines. Reply with a one-page brief and nothing', 'else, under these headings:', ' ',
    'Goal · Audience · Constraints · Success looks like', '· Out of scope · Open questions.', ' ',
    'Under 250 words. Plain sentences. No adjective', 'that does no work. Where the idea does not say,', 'do not invent: write "to confirm" and put the', 'question under Open questions.', ' ',
    'Do not praise the idea. Do not add features.',
]

FIRST_BRIEFS = [
    'AN EXAMPLE HOUSE RULE · AS ON WEEK 2, SLIDE 9', ' ',
    'Draw a square. Put a triangle on top.', 'Add a door and two windows.', ' ',
    '{muted:· no size, no roof angle, no where the door goes}', ' ',
    'AN EXAMPLE SPEC · AS IN WEEK 2, CAPTURE 2', ' ',
    'RULE: 30 circles on a 6 x 5 grid, each circle', 'as big as its cell.', 'CHANCE: each circle shifts up to 20 px.', 'NUMBERS: 600 x 600, white, black stroke 1 px.', 'CONSTRAINTS: noLoop, randomSeed(1), nothing else.', 'OUTPUT: the whole sketch.js.',
]

THREE_WAYS = [
    ('ONE LINE', 'The middle.',
     ['"Write a brief for a poster for a student design fair."',
      'Fluent, complete, plausible, and for nobody: the typical brief for the typical fair. Every word the model added, it took from its middle. Fifty runs give fifty cousins.']),
    ('A PARAGRAPH', 'Your facts, its shape.',
     ['The fair, the room, the date, who walks past, three constraints, in prose.',
      'The facts land; the structure is still the model\'s, and so are the priorities. Where you were silent it still decided — and did not tell you.']),
    ('A STRUCTURED BRIEF', 'Your shape, its filling.',
     ['Goal, audience, constraints, two examples, the output format, what to leave out.',
      'The model fills in a shape you drew. What comes back is close to what you meant, and where it is wrong you can point at the heading that let it in.']),
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 04 · LECTURE + WORKSHOP',
               'Language machines.',
               'Week 4 — module 2 opens: how a model writes, and how to brief one.',
               notes='Join code on screen from 30 minutes before. Laptops or phones out from the start: the second half is on genai.polyu.edu.hk. Today is the first of the three tool weeks — language, then images, then sound — and the first week where the machine talks back.'))

S.append(agenda('SD2112 · WEEK 04', [
    'Last week, in your words', 'Text → tokens', 'Tokens → embeddings', 'The transformer',
    'The next token, and temperature', 'Base, tuned, briefed', 'Fluent, typical, cannot say why', 'Prompting as briefing · the activity',
], notes='Eight stops. The first seven are the lecture: how a language model works, in the order the text travels — pieces, points, attention, the next word — and then what training does to it and what goes wrong. Break. Then the workshop: a prompt is a brief, and the activity, where the same small job gets briefed three ways.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the video · the awards · the map',
                 notes='Ten minutes of recap from what you gave us: the homework video, the Challenge 2 vote, and where we are.'))

S.append(question('short_answer', '3Blue1Brown: one thing you understood, one you did not.',
                  hint='Two short lines. "Understood: … Not yet: …". No wrong answers; the second line writes today\'s lecture.',
                  eyebrow_text='01 · HOMEWORK · SHORT ANSWER',
                  notes='ClassPoint short answer, two minutes. The video was Large Language Models explained briefly, eight minutes, 20 November 2024. Read six aloud, sorted: what people understood is usually "it predicts the next word"; what they did not is usually attention, or why it works at all. Say which chapter answers each one. Keep the screenshot: the mid-term draws on this video.'))

S.append(cards('01 · WEEK 3 · IN THREE LINES', 'The machine that cannot say why.', [
    ('CONCEPTS', 'A middle and an edge.', 'Rosch: a concept is a prototype and a fringe, not a definition. Machine B lives in the middle. Today: the middle of language.'),
    ('NEURONS', 'A guess, a correction, a million times.', 'Perceptron, backprop, deep learning. Nobody writes the rule; the weights settle. Today the weights write.'),
    ('MOVE 37', 'Fluent, fuzzy, alien.', 'AlphaGo played what no human would. Today\'s machine plays the next word — and sometimes plays one that is not true.'),
], notes='Three lines from last week, because module 2 stands on them. Prototype theory is the tool for reading every model output this week: what comes back is the middle of the examples. And "cannot say why" is the deal we made with machine B; today we see the price of it in text.'))

S.append(cards('01 · CHALLENGE 2 · FOUR ENTRIES · BY PROMPT', 'A picture from text and references.', [
    ('EXAMPLE A', 'The prompt', '"a cup that is a landscape, ceramic, studio light, after the reference sketch, no handle"'),
    ('EXAMPLE B', 'The prompt', '"a chair for a corridor, plywood, one bend, seen from above, the reference is the floor plan"'),
    ('EXAMPLE C', 'The prompt', '"a poster with no words, only a shadow that reads as a letter, risograph, two colours"'),
    ('EXAMPLE D', 'The prompt', '"a lamp that is mostly cable, brass, the reference photo for the light, not the shape"'),
], text_size=22, notes='These four are invented examples in the right shape. Replace them with the real ones: the four best entries from Blackboard, anonymised, the image on screen from the Blackboard page and the prompt on the card. Read each prompt before showing its picture; ask the room to guess the picture from the words. The gap between the guess and the image is the subject of the second half.'))

S.append(question('multiple_choice', 'Challenge 2: which entry gets the star?', [
    'Entry A', 'Entry B', 'Entry C', 'Entry D',
], eyebrow_text='01 · CHALLENGE 2 · AWARDS · MULTIPLE CHOICE',
    notes='ClassPoint vote, one minute. No correct answer: the room decides, the winner gets a participation star and thirty seconds to say what the reference image did that the prompt could not. Note the split for the awards list.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(1, 0),
                 notes='Module 2: the three tool weeks. Language today, images next week, sound the week after. Each ends in a small make; all three are evidence for the reflection due in week 7. Challenge 3 is briefed at the end of today.'))

# ───────────────────────── 02 · text → tokens ─────────────────────────
S.append(section('02', 'Text → tokens', 'the pieces · the count · the price', bg=INK,
                 notes='Chapter two: the model never sees words. It sees pieces, and the pieces are numbers. Five slides.'))

S.append(figure_slide('02 · A TOKENIZER · GPT-4\'S, ON TWO SENTENCES', 'The model never sees words. It sees pieces.', F.w04_tokens_split(),
                      body=['A tokenizer cuts text into pieces from a fixed vocabulary of about a hundred thousand, learned by counting which letter groups appear together most (byte-pair encoding). Each piece is a number. The English brief is 11 tokens; the same brief in Chinese is 21.'],
                      caption='Counted with tiktoken, cl100k_base (GPT-4), September 2026. OpenAI\'s rule of thumb: a token is about four characters, about three quarters of an English word.',
                      notes='Walk the top row: "poster" with its leading space is one token; "week-13" is three. Then the Chinese: the same meaning costs almost twice as many tokens, and several characters are split into bytes the model has to reassemble. For a Hong Kong designer that is money and context: the price list is per token, and the window is measured in tokens. Then the four words at the bottom: "hallucination" is three pieces, and none of them is a syllable.'))

S.append(sketch_slide('02 · LIVE · A TOY TOKENIZER', 'Type a sentence. Count the pieces.',
                      live('w04-tokens', TOKENS_CODE, 1400, 520, hint='click, then type · Delete clears · click the top line for another example', extra=TOKENS_EXTRA),
                      caption='A toy: split on spaces and punctuation, then cut long words at common endings and every four letters. Real tokenizers learn the pieces from data; the counting is the same.',
                      notes='Click into the sketch, press Delete to clear the example, type a sentence — your name, a Cantonese word in letters, a URL — and watch the count. Hover a token: it is a number, and that number is all the model gets. Ask someone to type "unbelievable" and then "unbelievably": the pieces change. A click on the top line brings back an example sentence. The point to land: the unit of cost, of memory, of everything, is the token, and it is not the word.'))

S.append(cards('02 · WHY A DESIGNER SHOULD CARE', 'Four things tokens decide.', [
    ('THE PRICE', 'You pay per token.', 'Every model on a price list charges per token, in and out. A brief in Chinese costs more than the same brief in English, on most tokenizers.'),
    ('THE WINDOW', 'Memory is counted in tokens.', 'The context window — chapter six — is so many tokens. A long chat plus a long document plus your examples: it adds up, and the oldest part falls off.'),
    ('THE LETTERS', 'It cannot see them.', 'Counting letters, rhyming, spelling backwards, exact character limits: the model guesses these, because it never sees a letter, only pieces.'),
    ('THE LANGUAGES', 'The vocabulary has a middle too.', 'Pieces were learned from a corpus that is mostly English. Rarer languages get cut finer: more tokens, less room, and a model that has seen less of them.'),
], text_size=23, notes='Four consequences, all designer-facing. The price and the window are budget questions you will meet in week 8 when the model is inside your product. The letters one explains a whole genre of embarrassing screenshots. The languages one is week 9 in miniature: the corpus has a middle, and it is English.'))

S.append(question('multiple_choice', 'Which costs the model more tokens?', [
    '"Design a poster for the week-13 poster fair."', 'The same sentence in Chinese', 'They cost the same: same meaning', 'It depends only on the number of words',
], eyebrow_text='02 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. Eleven tokens against twenty-one on GPT-4\'s tokenizer; we counted. The ratio differs from tokenizer to tokenizer, but the direction is the same for almost every non-English language. C is what people assume, and D confuses words with tokens — the two things this chapter separates.'))

# ───────────────────────── 03 · tokens → embeddings ─────────────────────────
S.append(section('03', 'Tokens → embeddings', 'a word is a point · nearby means similar · the axes have no names',
                 notes='Chapter three: each token becomes a list of numbers, a point in a space with thousands of axes. Words used alike end up close. Five slides.'))

S.append(figure_slide('03 · AN EMBEDDING · FORTY WORDS, TWO AXES', 'A word is a point. Nearby means used alike.', F.w04_embedding_map(),
                      body=['An embedding gives every token a position: a list of numbers, thousands long. It is learned from company — which words appear near which — so words used alike land near each other. Nobody names the axes; the model finds them. Ours is drawn by hand, in two dimensions, to show the idea.'],
                      caption='Firth, 1957: "You shall know a word by the company it keeps." Mikolov and colleagues, 2013 (word2vec): king − man + woman lands nearest to queen. Positions here are ours, not a model\'s.',
                      notes='Say the three things in the title. A point: the token is now a list of numbers. Nearby: the distance between two points is how alike the words are used, and that was learned from co-occurrence, not from a dictionary. No names: the axes are not "furniture-ness" and "colour-ness"; they are whatever fell out of training. Then the arrow: in 2013 word2vec showed that directions mean something — the man-to-woman arrow and the king-to-queen arrow are almost parallel. Be honest about the caveat: in the original paper the input words are excluded from the answer, otherwise the nearest point to king − man + woman is king itself.'))

S.append(sketch_slide('03 · LIVE · THE NEAREST FIVE', 'The mouse is a query. Distance is a choice.',
                      live('w04-embeddings', EMBED_CODE, 1400, 520, hint='move the mouse · click to switch euclidean / cosine'),
                      caption='Forty words placed by hand. The five nearest to the mouse light up with their distance. Click: cosine distance measures the angle from the origin instead — a different five.',
                      notes='Move around: near the furniture, the furniture lights up; between clusters, you get a mix — that is what the model sees when your word is unusual. Then click: cosine instead of euclidean, and the five change. Two lessons. Nearby means similar, and similar is whatever the training made it. And "near" is itself a design decision: week 10 builds a recommender on exactly this, and the choice of distance is the product.'))

S.append(cards('03 · WHAT A POINT BUYS YOU', 'Everything this course does with meaning is geometry.', [
    ('SIMILAR', 'Distance.', 'Two words, two sentences, two images as points: how far apart they are is how alike they are. No definitions, no rules. Machine B\'s version of a concept.'),
    ('SEARCH', 'The nearest neighbours.', 'Embed a question, find the closest documents, hand them to the model. Every "chat with your PDF" and every recommender: week 10.'),
    ('ARITHMETIC', 'Directions mean things.', 'king − man + woman ≈ queen; the same trick finds capitals from countries. A direction in the space can mean "gender" or "capital of", unnamed but usable — and biased, week 9.'),
    ('IMAGES', 'One space for words and pictures.', 'CLIP, next week: text and images embedded into the same space, so "a chair" the words and a chair the picture are neighbours. That is how a prompt reaches a diffusion model.'),
], text_size=22, notes='The reason to teach embeddings in a design course: the next five weeks stand on them. Similarity is a distance; search is nearest neighbours; CLIP is one space for two media; a recommender is "people near you liked". Ask which axis "gender" is on. Nobody knows, and the arrow still works — that is both the power and the week-9 problem.'))

S.append(statement('The word is a point. The sentence is a path. The model learned the map from company.', eyebrow_text='03 · WHERE WE ARE', size=96,
                   notes='Three sentences to carry into the next chapter. The remaining question is how the points talk to each other — what "chair" means changes when "high" or "committee" is next to it. That is attention.'))

# ───────────────────────── 04 · the transformer ─────────────────────────
S.append(section('04', 'The transformer', '2017 · attention: every token looks at every other', bg=INK,
                 notes='Chapter four, short: the architecture inside every chatbot, in one mechanism. You watched the video; this is the slide to argue with.'))

S.append(content('04 · ATTENTION · LIVE', 'Every token looks back at every token before it.',
                 ['"It" means the chair. "Red" belongs to the chair, not the client. A token\'s meaning is fixed by the tokens around it, and attention is the operation that lets it look.',
                  '- For each token: a set of weights over the tokens before it, adding up to one. Big weight, big influence on the token\'s new position in the space.',
                  '- Learned, not written: the model has many such tables, in every layer, and nobody typed a rule about pronouns.',
                  'Hover a word. Ours are made by hand; a model\'s come from the examples.'],
                 sketch=live('w04-attention', ATTN_CODE, 800, 600, hint='hover a word in the top row'),
                 body_size=27,
                 caption='A hand-made attention row: the hovered token and how much it looks at each earlier token. In a GPT a token looks only backwards.',
                 notes='Hover "it": most of its weight is on "chair". Hover "red": chair again. Hover "loves": client. Say the mechanism plainly: attention is a weighted average — each token pulls its meaning from the tokens it attends to, and the weights come from how well the two tokens match, in a learned sense. Then repeat: nobody wrote the pronoun rule; it fell out of predicting the next token on trillions of examples. The strongest example of machine B learning a rule that machine A would have to be written by hand.'))

S.append(cards('04 · 2017 · ATTENTION IS ALL YOU NEED', 'The whole machine, in four moves.', [
    ('1 · TOKENS', 'Cut the text into pieces.', 'A hundred thousand possible pieces; a number each. Chapter two.'),
    ('2 · EMBED', 'A point for each piece.', 'Plus a point for its position, so the order is not lost. Chapter three.'),
    ('3 · ATTEND, MANY TIMES', 'Every token looks at the others.', 'Attention, then a small network on each token, then again: dozens of layers. Each pass moves the points; "bank" drifts towards river or money.'),
    ('4 · PREDICT', 'The odds of every next token.', 'The last point is turned into a probability for each of the hundred thousand pieces. Pick one. Append. Repeat. Chapter five.'),
], text_size=22, notes='Vaswani and seven colleagues, June 2017, a translation paper; the T in GPT. Four moves, and the third is the only new one: attention replaces reading left to right with everything looking at everything, which is why it scales on GPUs and why the whole thing exploded after 2017. The sizes are the only other thing that changed since: more layers, more data, more weights.'))

S.append(video('04 · 3BLUE1BROWN · 20 NOVEMBER 2024 · THE HOMEWORK', 'Eight minutes. Rewatch the attention minute.', 'LPZh9BOjkQs',
               ['You watched it. The two claims to hold on to:',
                '- A language model is a function that predicts the next word for any piece of text, and its parameters were tuned by that one task.',
                '- Attention lets the lists of numbers "communicate with one another and refine the meanings they encode based on the context around."',
                'The mid-term quiz draws on this video and on the playlist.'],
               thumb='yt/LPZh9BOjkQs.jpg', body_size=28,
               notes='If the short answers at the start said "attention" was the thing not understood, play the attention minute now, then go back one slide and hover again. Otherwise cut this slide. The video also names the two training phases, which is chapter six.'))

# ───────────────────────── 05 · the next token, and temperature ─────────────────────────
S.append(section('05', 'The next token', 'a table, a die, a temperature · Markov 1913 → Nake 1966 → GPT',
                 notes='Chapter five, the heart of the lecture: the model writes by throwing a die on a table of odds, one token at a time. Nake did this in 1966 with signs. Six slides.'))

S.append(statement('A language model is a Markov chain with a very long memory.', eyebrow_text='05 · THE CLAIM', size=110,
                   notes='Say it, then defend it for five slides. Nake\'s chain, week 2: the next sign depends on the last one, chosen by a table of probabilities and a throw of the die. A language model: the next token depends on everything in the window, chosen from a table too big to write down — so it is learned — and a throw of the die. Same shape. What changed is the memory and the size of the table.'))

S.append(figure_slide('05 · ONE IDEA, A CENTURY LONG', 'The next thing depends on what came before.', F.w04_chain_lineage(),
                      body=['Markov, 1913: 20,000 letters of Pushkin\'s Eugene Onegin, and the next letter depends on the last. Shannon, 1948: choose each word by how often it follows the previous one, and the text is almost English. Hiller in 1957 and Nake in 1966 did it with notes and with signs. A GPT does it with tokens, remembering thousands of them.'],
                      caption='Shannon\'s sentence is verbatim from A Mathematical Theory of Communication, Bell System Technical Journal, 1948, "second-order word approximation". The Illiac Suite\'s fourth movement and Walk-Through-Raster are on the week-2 slides.',
                      notes='Read Shannon\'s sentence aloud; it is 1948, and it is a bigram model. The resemblance to English grows with the memory: one letter, one word, and — Shannon noticed — the text stays plausible for about twice the range the table knows. Then the jump: a transformer remembers the whole window, and the table is a network with billions of weights. The mechanism is the same one you coded in week 2 as next(): a throw of the die on a table.'))

S.append(sketch_slide('05 · LIVE · A MACHINE THAT WRITES BY DICE AND A TABLE', 'Click: the next word. Move the mouse: the temperature.',
                      live('w04-next-token', next_code(1400, 520), 1400, 520, hint='click: next word · mouse up and down: temperature · C: start again'),
                      caption='A bigram model trained, at load, on 200 words about design and AI. The bars are the odds of the next word after the last one; the mouse height reshapes them; a click throws the die. Nake\'s raster, in words.',
                      notes='Click ten times with the mouse high — cold — and it repeats the most likely path: "the model wants the middle". Press C, put the mouse low — hot — and click ten times: rarer words wake up and the sentence goes strange. This is the entire mechanism of a chatbot, with a table of 200 words instead of the internet and a memory of one word instead of a hundred thousand. Everything in the bars came from the examples. The die is the only thing that is not the examples.'))

S.append(figure_slide('05 · TEMPERATURE', 'The same odds, three heats.', F.w04_temperature(),
                      body=['Temperature reshapes the bars before the die is thrown. Cold: the top word almost always, the same answer every time. Hot: the long tail wakes up — surprise, and nonsense. The API exposes it as a number, usually 0 to 2; the chat window hides it.'],
                      caption='p ~ odds^(1/T), normalised. OpenAI\'s API takes 0 to 2 with a default of 1. Temperature 0 makes the model repeatable: the same prompt, the same text — like randomSeed() in week 2.',
                      notes='This is the seed slide of week 2 again. At temperature 0 the model is deterministic; the same brief gives the same draft. At 1 it samples from the odds it learned. Above 1 it flattens them: more variety, more mistakes. Ask: which would you use to draft a contract, and which for twenty names for a chair? The answer is the design decision the chat box makes for you without asking.'))

S.append(code_slide('05 · THE TABLE AND THE DIE · THE WHOLE MODEL', 'Count the pairs. Reshape by heat. Throw the die.', NEXT_MODEL,
                    sketch=live('w04-next-token-tall', next_code(800, 600), 800, 600, hint='click: next word · mouse: temperature · C: reset'),
                    code_size=20, caption='train() counts which word follows which. odds() takes the eight most likely and reshapes them by temperature. pick() throws one die on the bars. Compare next() in Walk-Through-Raster, week 2.',
                    notes='Three functions. train is the whole of "learning from examples" for this model: count. odds is the table, with the temperature applied — a power of 1/T then normalised. pick is next() from week 2 with more than three outcomes. Everything a hundred-billion-weight model does differently is inside odds: it does not look up a row, it computes one from the whole window. The shape of the loop is the same.'))

S.append(question('multiple_choice', 'Temperature 0 means…', [
    'Always the most likely token: the same answer every time', 'The model is more accurate', 'The model gives shorter answers', 'The model stops making things up',
], eyebrow_text='05 · QUICK CHECK · MULTIPLE CHOICE',
    notes='A. Temperature 0 is repeatability, not truth: a confident wrong guess is still the most likely token and comes back every time. D is the trap and the bridge to chapter seven. B and C confuse heat with quality and length.'))

# ───────────────────────── 06 · base, tuned, briefed ─────────────────────────
S.append(section('06', 'Base, tuned, briefed', 'pre-training · tuning · RLHF · the window · the system prompt', bg=INK,
                 notes='Chapter six: what turns a next-token machine into an assistant, and what the assistant can see. Five slides.'))

S.append(figure_slide('06 · THREE ROUNDS OF EXAMPLES', 'A base model completes. An assistant answers.', F.w04_pipeline(),
                      body=['Pre-training gives you a base model: it continues any text, brilliantly, and does not know it is being asked anything. Instruction tuning shows it thousands of question-and-answer pairs. RLHF shows it which of two answers people preferred, and trains it to please them. Machine B, three times.'],
                      caption='GPT-3, May 2020: 175 billion weights, a base model. InstructGPT, 2022: a 1.3-billion-weight model tuned on human feedback was preferred to the 175-billion base. ChatGPT: 30 November 2022.',
                      notes='The base model is the honest one: ask it "what is a good chair" and it may continue with three more questions, because the internet does. Instruction tuning is a few thousand examples of how a reply looks. RLHF is the interesting one for designers: people rank answers, a reward model learns their taste, the model is pushed towards it. That taste is where "helpful" comes from — and, in chapter seven, where flattery comes from. The InstructGPT number is the one to remember: the small tuned model beat the huge raw one on what people wanted.'))

S.append(cards('06 · WHAT THE TUNING CHANGES', 'Same weights, different manners.', [
    ('BASE', 'Completes.', 'Give it "Dear client," and it writes the letter — or ten letters, or a forum thread about letters. No idea it is talking to you. Rarely shipped; always underneath.'),
    ('INSTRUCTION-TUNED', 'Answers.', 'Knows the shape of a reply: a question gets an answer, a brief gets a draft. The shape was shown to it, not written as a rule.'),
    ('RLHF', 'Pleases.', 'Trained on what raters preferred: polite, structured, confident, eager. The manners you meet in a chat window are a taste that was learned from thousands of people\'s clicks.'),
], text_size=24, notes='Three manners, one machine. For the reflection this is the vocabulary: a model\'s behaviour is examples all the way down — of language, of replies, of preferences. Ask: whose preferences? The raters\'. Week 9 asks who they were.'))

S.append(figure_slide('06 · THE CONTEXT WINDOW', 'The model sees the window, and nothing else.', F.w04_context_window(),
                      body=['Everything the model can use right now is in one strip of tokens: a system prompt, your brief, your examples, the conversation so far, and the answer it is writing. Nothing outside the strip exists for it — not last week\'s chat, not your files, not the web — unless something puts it in.'],
                      caption='Liu and colleagues, 2023, Lost in the Middle: models use the start and the end of a long window best and lose what sits in the middle. Put what matters first or last.',
                      notes='Two design consequences, and a third from the paper in the caption — Liu and colleagues measured it in 2023: what sits in the middle of a long window is used worst, so the brief goes first and the question last. One: a model has no memory between conversations, and inside a conversation its memory is this strip; a long chat pushes your brief out of the window, and the draft drifts. Start a new chat for a new job. Two: everything the model "knows" about you it knows from the strip, so what you paste is the whole world it works in. The agents chapter is about tools that put things in the strip.'))

S.append(content('06 · THE SYSTEM PROMPT', 'The product designer\'s brief comes first.',
                 ['Before your first message, the product has already put a prompt in the window: who the model is, what it may not do, how to talk. A brief, written by a designer — and the model is trained to rank it above your message (OpenAI\'s instruction hierarchy, 2024): trained, not guaranteed.',
                  '- Since August 2024 Anthropic publishes the system prompts of its Claude apps. Read one: tone, refusals, formatting, what to leave out. A design document.',
                  '- Week 2 returns: a system prompt is machine A wrapped around machine B. Words, not code — but readable, and the first place to look when a product misbehaves.'],
                 figure=F.w04_window_stack(), caption='The window as a stack: the system prompt first, and ranked highest — Wallace and colleagues, OpenAI, April 2024. The workshop template comes in chapter nine.',
                 body_size=27,
                 notes='The system prompt is the designer\'s handle on a chatbot and the subject of week 12. The rank is trained, not built in: Wallace and colleagues at OpenAI (April 2024) call it the instruction hierarchy — system above user above tool output — and prompt injection is the attack on it; a chat product also keeps the system prompt when a long conversation pushes the oldest turns out of the window. Show a published one if there is time — it reads like a style guide with refusals. Land the connection to week 2: it is a rule in words, and everything we said about specs applies, including "it does what you said, not what you meant".'))

# ───────────────────────── 07 · fluent, typical, cannot say why ─────────────────────────
S.append(section('07', 'Fluent, typical, cannot say why', 'hallucination · sycophancy · agents and tools', bg=INK,
                 notes='Chapter seven: what goes wrong, and the machinery being built around the model to catch it. Seven slides; the last is the break.'))

S.append(content('07 · HALLUCINATION · OPENAI, SEPTEMBER 2025', 'It guesses because guessing was rewarded.',
                 ['A model that has to answer will answer. Kalai, Nachum, Vempala and Zhang, Why Language Models Hallucinate (4 September 2025): "language models hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty."',
                  '- "Like students facing hard exam questions, large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty."',
                  '- The fix they propose is not a better model but a different exam: score "I don\'t know" above a confident wrong answer.',
                  'Fluent is not the same as true.'],
                 figure=F.w04_guess_or_blank(), caption='The paper\'s argument as an exam: score blanks and wrong answers the same, and guessing wins. Score wrong answers below blanks, and it stops.',
                 body_size=26,
                 notes='The paper is the reading for this slide: OpenAI\'s researchers, with Georgia Tech\'s Santosh Vempala, saying that hallucination is not a bug in transformers but a consequence of how models are trained and graded — a guess scores better than a blank on almost every benchmark, so models learned to guess. For a designer: never ask a model for a fact you cannot check, and design the prompt so that "I don\'t know" is a permitted answer. The mid-term will ask why models make things up: because guessing was rewarded, not because they are broken.'))

S.append(content('07 · SYCOPHANCY · APRIL 2025', 'It agrees because agreeing was rewarded.',
                 ['On 25 April 2025 OpenAI updated GPT-4o; within days it was praising every idea, validating every doubt, agreeing with everything. The update was rolled back by 29 April.',
                  '- OpenAI\'s post-mortem: "we focused too much on short-term feedback, and did not fully account for how users\' interactions with ChatGPT evolve over time" — the thumbs-up, in their own words.',
                  '- RLHF in one incident: train on what people click, and you get what people click. People click on praise.',
                  'For a designer the failure is precise: a model that likes your idea is not a critic. Do not ask it whether the work is good.'],
                 figure=F.w04_thumbs(), caption='Stage three of the pipeline is where it happened: a reward signal from the thumbs, and a model trained to earn it.',
                 body_size=26,
                 notes='Dates verified: the update went out on 25 April 2025, complaints filled the weekend, the rollback was announced on 29 April, and OpenAI published two post-mortems; the quotation on the slide is OpenAI\'s own sentence from the first of them, not the press paraphrase. The design lesson is the one to spend time on: the thing you are talking to was trained to be liked. So brief it to disagree — "give me three reasons this poster fails" gets critique; "is this good?" gets applause. That is a briefing rule, and it comes back after the break.'))

S.append(cards('07 · A DESIGNER\'S FOUR DEFENCES', 'Fluent, typical, cannot say why — so:', [
    ('CHECK', 'Every fact, every name, every date.', 'A citation from a model is a plausible citation. Open it. Invented references fail the assignment; the rule is in the syllabus because this is why.'),
    ('ALLOW "I DON\'T KNOW"', 'Write it into the brief.', '"If the brief does not say, write to confirm." A permitted blank beats a confident guess — the September paper in one line.'),
    ('THE CASE AGAINST', 'Never "is this good?"', '"Three reasons a tutor would reject this." The model is trained to please; make pleasing you mean disagreeing.'),
    ('KEEP THE MIDDLE IN VIEW', 'Typical is not yours.', 'What comes back is the average of the examples. Your job starts where the average ends: the edge, week 1, again.'),
], text_size=22, notes='Four habits; make them the house rules for the second half. The second and third are prompt-level: you can write them into a brief today. The first is discipline. The fourth is the course: the middle is theirs, the edge is yours.'))

S.append(figure_slide('07 · AGENTS · PLAN, ACT, OBSERVE', 'A model that can call a tool is a model that can check.', F.w04_agent_loop(),
                      body=['An agent is a language model in a loop: it writes a plan, calls a tool — a search, a calculator, a code runner, your files — reads the result back into its window, and goes again until the job is done or a person stops it. The tools are machine A: exact, checkable. The loop is what lets machine B correct itself.'],
                      caption='Yao and colleagues, ReAct, 2022: reasoning and acting interleaved. Week 12 designs the interface the tool needs; week 8 puts the loop inside a product.',
                      notes='The mechanism is small: the model writes a line that says "search: poster fair PolyU 2026", the product runs the search, the result is pasted into the window, and the model continues. Everything an "agent" does is this loop. Two design points: a tool is exact, so a model with a calculator does not guess sums; and a loop that runs unwatched is a machine that acts on its own guesses — the stop button is a design decision. The week-13 fair posters will be researched this way; check what comes back.'))

S.append(question('multiple_choice', 'Why do language models make things up?', [
    'They are broken; the next version will fix it', 'Training and tests rewarded a guess over "I don\'t know"', 'They lie on purpose to please users', 'They were trained on too little data',
], eyebrow_text='07 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B, the September 2025 paper. C is half of the sycophancy story but not hallucination, and "on purpose" is the wrong word for a die on a table. A and D are the two folk theories; neither explains why the same model guesses confidently on things it was never trained on.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · A PROMPT IS A BRIEF · THEN YOU WRITE THREE', size=120, bg=PAPER,
                   notes='1:24. Everyone logged into genai.polyu.edu.hk before leaving the room; the TAs help anyone whose login fails. Pick one language model there and stay with it for the session.'))

# ───────────────────────── 08 · prompting as briefing ─────────────────────────
S.append(section('08', 'Prompting as briefing', 'the spec becomes a brief · one job, three ways · the middle', bg=YELLOWS[0],
                 notes='Chapter eight, after the break: the practical half. A prompt is a brief; you have written briefs for years; the week-2 spec was one. Nine slides.'))

S.append(statement('A prompt is a brief.', eyebrow_text='08 · THE CLAIM', size=150,
                   notes='The sentence of the second half. Everything you know about briefing a junior, a printer, a photographer applies to a model, with one difference: the model does not phone you back when the brief is unclear. It fills the gap from its middle, silently. So the brief has to be better than the one you would give a person.'))

S.append(figure_slide('08 · WEEK 2 → WEEK 4', 'The week-2 spec is the week-4 brief.', F.w04_spec_to_brief(),
                      body=['Rule, chance, numbers, constraints, output: the five habits of the week-2 spec. Goal, audience, constraints, examples, output format, what to leave out: the six headings of a brief. The one new heading is the last: where a spec said where chance may enter, a brief says what the model may not decide for you.'],
                      caption='Your specs from week 2 come back on slide 46 as the first briefs.',
                      notes='Map them out loud. Rule became goal and audience. Numbers became constraints and examples. Output stayed output. Chance — the place the spec let the die in — became "leave out": the place the brief closes the door on the middle. Then say why examples matter more here than in week 2: a language model was trained to continue text, so two examples of what you want are worth a paragraph describing it.'))

S.append(cards('08 · ANATOMY OF A BRIEF', 'Six headings a model cannot guess.', [
    ('GOAL', 'One sentence.', 'What the thing must do, for whom, and how you will know. "A poster that makes a tutor stop for ten seconds."'),
    ('AUDIENCE', 'Who, and what they know.', 'The model writes for the average reader unless told. Tell it: tutors who have seen 27 other posters.'),
    ('CONSTRAINTS', 'Format, length, tone, brand.', 'Numbers, like week 2: A0, 200 words, two colours, readable from three metres. What you do not fix, it guesses.'),
    ('EXAMPLES', 'Two you like, one you do not.', 'Paste them. A model was trained to continue text; examples move it further than adjectives ever will. Say why for each.'),
    ('OUTPUT · LEAVE OUT', 'The shape, and the door.', 'Headings, a table, a length. Then the list of things it would add if you let it: taglines, "innovative", praise, anything not in the brief — "write to confirm".'),
], text_size=21, notes='Five cards, six headings. Put the anatomy next to the week-2 template in your head: the same discipline, for words. The two that students skip are examples and leave out — and those are the two that move the model off its middle. "Leave out" is the sycophancy defence and the hallucination defence written into the brief.'))

S.append(two_col('08 · THE FIRST BRIEFS · YOURS, FROM WEEK 2', 'You have already written two.',
                 ['The week-2 house rules were briefs: a stranger executes them and fills every gap. The capture-2 specs were better briefs: numbers, constraints, an output.',
                  '- Read the house rule. What would a model add? A roof colour, a chimney, a garden.',
                  '- Read the spec. Where can the model still decide? The stroke colour, what "up to" means at the edge.',
                  'Same author, same week, two gaps of different sizes. The brief decides the size of the gap.'],
                 FIRST_BRIEFS, right_size=22, left_size=30,
                 notes='The two on the slide are examples in the right shape. Pull two real ones from the week-2 wall before class if you can — one house rule from the slide-9 short answers and one spec from the capture-2 captions, anonymised — and paste them over these. Read them as briefs. The house rule leaves the executor almost everything; the spec leaves it almost nothing. Ask the room which they would send to a model and which to a friend. Cut if behind.'))

S.append(cards('08 · ONE JOB, THREE BRIEFS', 'A design brief, written three ways.', THREE_WAYS, text_size=23,
               notes='The same job three times. The one-liner is what most people type, and what most people get is the average brief on the internet — fluent and for nobody. The paragraph gets your facts in but leaves the structure and the priorities to the model. The structured brief hands the model a shape and a door: it fills the shape, and "leave out" keeps the middle from walking in. The next slide is what each gets back.'))

S.append(figure_slide('08 · WHAT EACH GETS BACK', 'The less you say, the more it fills in from the middle.', F.w04_three_briefs(),
                      body=['Run the same brief a hundred times and plot the drafts. The one-liner scatters across the model\'s middle: the typical brief for the typical fair. The paragraph narrows. The structured brief lands near what you meant — and where it misses, you can point at the heading that let it in.'],
                      caption='A drawing, not data: the mechanism is the bars of chapter five. Every unspecified decision is a die thrown on the odds the model learned.',
                      notes='This is the week-1 cup wall, in text: ask for a cup, get the middle. The die is thrown on every decision you did not make, and the odds are the internet\'s. Say the two consequences: a vague brief does not get a bad draft, it gets an average one, which is worse because it looks fine; and the brief is the place to fix a draft, never the draft — exactly as in week 2, fix the spec, not the code.'))

S.append(two_col('08 · WHAT GOOD LOOKS LIKE', 'The structured brief, for the poster.',
                 ['This is the brief for the round-2 draft. Read it as the six headings.',
                  '- Goal: one sentence, with a test in it.',
                  '- Audience: who, where, what they have seen.',
                  '- Constraints: numbers. Examples: pasted, with a why.',
                  '- Output: the headings and the length. Leave out: the door.',
                  'Two hundred words of brief for two hundred words of draft. The ratio is normal.'],
                 BRIEF_STRUCTURED, right_size=20, left_size=30,
                 notes='Read the "leave out" line aloud twice. "Write to confirm" is the September paper as a design rule: give the model permission to leave a blank, and it will, instead of inventing a date for the fair. The ratio matters too: a good brief is as long as the draft, and that is not a failure of the tool.'))

S.append(content('08 · ITERATE LIKE A DESIGNER', 'Edit the brief, not the draft.',
                 ['The draft drifts; the brief is the source. When the draft is wrong, find the heading that let it in, fix the heading, run again. One change per run, so you know what caused what.',
                  '- New job, new chat: the window forgets, and an old brief pushed off the strip drifts the draft.',
                  '- Ask for the brief back: "in one line, what did I ask for?" If it does not match, the draft will not either.',
                  '- Temperature low for the contract, high for the twenty names. Say which you want; the chat box picks for you.',
                  'Keep the brief with the draft: the caption today, the process note in your reflection.'],
                 body_size=30,
                 notes='The week-2 iteration discipline, for words. Fix the spec, not the code, became fix the brief, not the draft. The "ask for the brief back" move is the cheapest check there is. And the process note: the reflection asks how you used AI; the honest answer is the brief you wrote and what you changed in it.'))

# ───────────────────────── 09 · workshop: briefing as a workflow ─────────────────────────
S.append(section('09', 'The workshop', f'a real small job · {GENAI} · a brief, then a workflow', bg=INK,
                 notes='Chapter nine: the tools for the activity. The job, the system prompt that turns briefing into a workflow, and the checklist for comparing drafts. Four slides, then the rounds.'))

S.append(content('09 · THE JOB', 'One small real job. Pick one.',
                 ['**A poster for the week-13 poster fair.** A0, on a wall, 114 students and their tutors walking past, your group project on it. You do not have the project yet; brief the poster anyway — the brief is the exercise.',
                  '**Or: the caption of an exhibit.** One object from your studio, on a plinth, forty words on the wall: name, maker, year, what to notice.',
                  '- Both are jobs a language model will draft in five seconds and you will edit for an hour. That ratio is the lesson.',
                  f'Tool: any language model on **{GENAI}**. One model for the whole session, so the middle stays the same middle.'],
                 body_size=30,
                 notes='Two jobs, both real: the poster fair is in week 13 and captions are the smallest brief a designer writes. Tell people to pick one and keep it for all three rounds, so the comparison is fair. Pick a model on GenAI and stay with it; the TAs know which one answered the week-2 template most reliably.'))

S.append(two_col('09 · THE WORKFLOW · A SYSTEM PROMPT', 'Automate the briefing. Then brief the automation.',
                 ['A system prompt is a brief for every future brief: paste it as the first message, or in the system field if there is one. From then on: any product idea in, a one-page brief out.',
                  '- Machine A around machine B: rules in words, obeyed every time.',
                  '- Run it on two ideas. What repeats is the prompt\'s middle; what differs is the idea\'s.',
                  'Round 4 runs it on a stranger\'s idea. Then you edit the prompt, not the output.'],
                 SYSTEM_PROMPT, right_size=22, left_size=29,
                 notes='The template is on the course site and on Blackboard. Read the last two lines aloud: "do not praise, do not add" is the sycophancy defence and the middle defence as rules. On GenAI, if there is no system field, paste it as the first message and then paste the idea as the second; the effect is nearly the same. The exercise after the run is to compare two outputs and find what the prompt imposed on both.'))

S.append(cards('09 · COMPARE', 'Four questions for every draft.', [
    ('DID IT DO WHAT I SAID?', 'Tick the headings.', 'Six headings in the brief, six ticks. A missing one is a dropped constraint: restate it.'),
    ('WHAT DID IT DECIDE?', 'Find the middle.', 'Every sentence you did not brief: where did it come from? The typical fair, the typical poster. Circle them.'),
    ('WHAT DID IT INVENT?', 'Find the guess.', 'A date, a name, a size you never gave. If "to confirm" was allowed, did it use it?'),
    ('WOULD I SEND IT?', 'The client test.', 'To a client, under your name, today. If not: which heading fixes it? Fix the brief, run again.'),
], text_size=22, notes='The checklist for the rounds and for Challenge 3. The second and third questions are the two failure modes from the lecture — the middle and the guess — and the fourth is the final vote of the activity. Print it in your head; the TAs will ask it as they walk.'))

# ───────────────────────── 10 · activity: brief it three ways ─────────────────────────
S.append(section('10', 'Brief it three ways.', f'40 minutes · one job · {GENAI} · three briefs', bg=YELLOWS[0],
                 notes='The activity. One small job, briefed three ways: a line alone, a structured brief in pairs, a system prompt in fours on a stranger\'s idea. Each round ends in ClassPoint; the last capture is an image with the brief as the caption. Nicolò keeps time; Amber, WU Zhao and MA Jie walk with the four compare questions. One device per pair at least.'))

S.append(activity('1 — ALONE · ONE LINE', 5, 'Brief it in one line.',
                  [f'Open **{GENAI}**, pick a language model. Pick your job: the fair poster, or a caption.',
                   'Type **one line**. No more: "Write a brief for a poster for a student design fair." Read what comes back.',
                   'Underline every sentence you did not ask for. That is the middle.'],
                  panel=['THE ONE-LINE PROMPT', ' ', 'Write a brief for a poster', 'for a student design fair.', ' ', '— or —', ' ', 'Write a caption for an object', 'in a design exhibition.', ' ', ' ', 'Then: underline what you', 'did not ask for.'],
                  panel_size=24, bg=YELLOWS[0],
                  notes='Five minutes, silent. The one-liner is deliberately dumb, like "a cup" in week 1: everyone gets the prototype. Watch for people who improve the line — stop them; the point is the middle. The underlining is the work: most of the draft was not asked for.'))

S.append(question('short_answer', 'Everyone: paste the first sentence of the draft.',
                  hint='Copy the first sentence the model wrote, word for word. We put all of them on the wall.',
                  eyebrow_text='10 · CAPTURE 1 · SHORT ANSWER · EVERYONE',
                  notes='ClassPoint short answer, everyone, two minutes. The wall: a hundred first sentences from a hundred one-liners, and most of them are the same sentence — "This brief outlines…", "The goal of this poster is…". The cup wall in text. Read five aloud in a row; the room laughs at the third. That is the model\'s middle, and nobody typed it.'))

S.append(activity('2 — IN PAIRS · THE STRUCTURED BRIEF', 8, 'Brief it with the anatomy.',
                  ['Same job, same model, **new chat**. Write the six headings together; paste two examples if you have them (a poster you like, a caption you like).',
                   'Run it. Tick the six headings in the draft. Circle what it decided; box what it invented.',
                   '**Where did the draft get closer to what you meant — and which heading did that?**'],
                  panel=BRIEF_ANATOMY, panel_size=21, bg=YELLOWS[1],
                  notes='Eight minutes, one laptop per pair. New chat, so the one-liner is not in the window. Push for numbers in constraints and a real "leave out" line. The comparison question at the end is the whole point: pairs should be able to name the heading that moved the draft. Expect dropped headings and an invented date for the fair; both are the lecture happening in front of them.'))

S.append(question('multiple_choice', 'Compared with round 1, the second draft is…', [
    'The same brief with more words', 'Specific to our job: we can say which heading did it', 'Worse: the brief constrained it into a corner', 'Not back yet — help',
], eyebrow_text='10 · PULSE · MULTIPLE CHOICE',
    notes='Pulse, one minute; no correct answer, but B is the hoped-for one and usually wins. Ask two pairs who chose B for the heading. Ask one pair who chose C what the corner was — often it is a constraint that was wrong, which is a brief problem, not a model problem. Ds get a TA now.'))

S.append(activity('4 — TWO PAIRS · THE WORKFLOW', 10, 'Automate it. Run it on a stranger\'s idea.',
                  ['Join the pair behind you. **New chat.** Paste the system prompt on the right — edit it if you dare.',
                   'Each pair writes a product idea in two lines. **Swap.** Run the workflow on the other pair\'s idea. Then run it on your own.',
                   'Compare the two briefs. What repeats is the prompt\'s middle. Fix the **prompt**, run once more. One scribe screenshots the best brief.'],
                  panel=SYSTEM_PROMPT, panel_size=20, bg=YELLOWS[2],
                  notes='Ten minutes in fours. The swap is the point: a brief written by a workflow on an idea you did not have is the test of the workflow, not the idea. The comparison of the two outputs shows what the system prompt imposed. When they edit the prompt, they are doing the week-12 job — designing the manners of a product — three weeks early. This is the start of Challenge 3.'))

S.append(question('image_upload', 'Scribes only. The best brief, and the words that made it.',
                  hint='One screenshot per four. Caption: the system prompt, or the brief, word for word.',
                  eyebrow_text='10 · CAPTURE 2 · IMAGE UPLOAD · ONE PER FOUR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='Scribes only, about 28 screenshots, caption required. Put the wall on screen. Read two captions aloud and ask the room what the brief would look like before showing it; where the guess fails, the prompt failed. Download the submissions: they are the seed of Challenge 3 and evidence for the reflection.'))

S.append(question('multiple_choice', 'Which draft would you send to a client?', [
    'The one-line draft, as it came', 'The structured-brief draft, as it came', 'The workflow\'s draft, as it came', 'None of them without my edit',
], eyebrow_text='10 · THE VOTE · MULTIPLE CHOICE',
    notes='The last vote. D is the honest answer and the room usually knows it — and the follow-up is the debrief: if none goes out without your edit, then the edit is the design, and the brief is what made the edit small. Anyone who votes B or C: ask what they would have to check first. Anyone who votes A is asked to read it aloud.'))

S.append(content('10 · WHAT JUST HAPPENED', 'It did what you said. The brief was the design.',
                 ['The line: a hundred first sentences, one sentence. A vague brief does not get a bad draft; it gets the middle, and the middle is for nobody.',
                  'The anatomy: the draft moved when you closed a door — a number, an example, a "leave out". You can name the heading that moved it. That is authorship.',
                  'The workflow: a system prompt is a brief for every future brief, and what it imposes on two ideas is its middle. Editing it is designing a product\'s manners. Week 12.',
                  '**The machine wrote every word. You wrote the brief. That was the design.**'],
                 body_size=32,
                 notes='Mirror of the whole class, and of weeks 1 and 2: the cup, the spec, the brief. Say the last line slowly; it is the week-2 line with one word changed. Then the sentence for the reflection: a language model is machine B that writes, and a brief is the rule you hand it — the designer stands between the two.'))

# ───────────────────────── 11 · challenge 3 · homework ─────────────────────────
S.append(cards('11 · CHALLENGE 3 · DUE BEFORE WEEK 5', 'A brief, automated — then edited by you.', [
    ('THE PROMPT', 'Your words first.', 'A structured brief or a system prompt, for a real job of yours: a poster, a caption, a product page, a portfolio blurb. Keep it.'),
    ('THE DRAFT', 'What the model wrote.', 'Unedited, saved as it came, with the model named. This is the machine\'s half.'),
    ('THE EDIT', 'What you changed, and why.', 'Your version next to it, changes visible, three lines on what the model decided that you undid. This is your half.'),
    ('THE VOTE', 'Both on Blackboard.', 'Prompt, draft, edit, together. The room votes in week 5; winners get a star. TAs help 30 minutes before and after class.'),
], notes='Three things on Blackboard before week 5: the prompt, the unedited draft, your edit with the changes visible. Show both halves — the assignment is the difference between them. The model is named. Next week the room votes.'))

S.append(content('11 · BEFORE WEEK 5 · IMAGE MACHINES', 'Three videos and one reading.',
                 ['**Watch, on the playlist, in this order:**',
                  '- Welch Labs: But how do AI images and videos actually work? (a guest video on 3Blue1Brown).',
                  '- AssemblyAI: Diffusion models explained in 4-difficulty levels.',
                  '- Computerphile: How AI "understands" images (CLIP). The embedding space of chapter three, with pictures in it.',
                  '**Read:** Verbeek, P.-P. (2015). Beyond interaction: a short introduction to mediation theory. Interactions 22(3). The core reading of the course; six pages.'],
                 images=['yt/iv-5mZ_9CPY.jpg', 'yt/yTAMrHVG1ew.jpg', 'yt/KcSXcpluDe4.jpg'],
                 caption='Welch Labs · AssemblyAI · Computerphile, on the course playlist. Verbeek is on Blackboard.',
                 body_size=27,
                 notes='Next week is images: CLIP is today\'s embeddings with pictures in the same space, diffusion is today\'s die on a table applied to noise, and Verbeek is the philosophy that makes the whole course a design course. Six pages; read it twice. The quiz in week 7 draws on all three videos.'))

S.append(end('See you next week. Image machines and mediation.',
             'Bring your brief, drafted and edited. Watch the three videos. Read Verbeek.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: CLIP, diffusion, latent space, ControlNet, and Ihde\'s four relations — and the Challenge 3 vote. Homework in one line: the brief on Blackboard, three videos, Verbeek. The TAs stay for 30 minutes.'))

DECK = dict(title='SD2112 · AI in Design · Week 04', slides=finalize(S, FOOTER), pdf='SD2112-week04.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week04', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 2026-09-05)
# https://arxiv.org/abs/2509.04664 — Kalai, Nachum, Vempala, Zhang, "Why Language Models Hallucinate", submitted 4 Sep 2025 (abstract quoted verbatim)
# https://openai.com/index/why-language-models-hallucinate/ — OpenAI's post on the paper (blocked to fetch; date and claim confirmed via arXiv and coverage)
# https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic/ — the GPT-4o rollback date (TechCrunch's wording paraphrases OpenAI; not quoted)
# https://simonwillison.net/2025/Apr/30/sycophancy-in-gpt-4o/ — OpenAI's post-mortem reproduced verbatim (openai.com returns 403 from here): "we focused too much on short-term feedback, and did not fully account for how users' interactions with ChatGPT evolve over time" (slide 37)
# https://www.deeplearning.ai/the-batch/openai-pulls-gpt-4o-update-after-users-report-sycophantic-behavior — the thumbs-up/down cause
# https://openai.com/index/sycophancy-in-gpt-4o/ and https://openai.com/index/expanding-on-sycophancy/ — OpenAI's two post-mortems (25 April update; rollback)
# https://www.law.georgetown.edu/tech-institute/research-insights/insights/tech-brief-ai-sycophancy-openai-2/ — 25 April 2025 release date
# https://arxiv.org/abs/1706.03762 — Vaswani et al., "Attention Is All You Need", submitted 12 June 2017, eight authors
# https://arxiv.org/abs/2005.14165 — Brown et al., "Language Models are Few-Shot Learners", 28 May 2020, 175 billion parameters
# https://arxiv.org/abs/2203.02155 — Ouyang et al., InstructGPT, 2022: the 1.3B tuned model preferred to the 175B GPT-3
# https://openai.com/index/chatgpt/ and https://techcrunch.com/2025/11/30/chatgpt-launched-three-years-ago-today/ — ChatGPT, 30 November 2022
# https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them — one token ≈ 4 characters ≈ ¾ word; 100 tokens ≈ 75 words
# https://github.com/openai/tiktoken — cl100k_base; the token counts on the slides were measured locally with tiktoken 2026-09-05
# https://www.research.ed.ac.uk/en/publications/neural-machine-translation-of-rare-words-with-subword-units — Sennrich, Haddow, Birch, 2016: byte-pair encoding for NMT
# https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf — Shannon 1948, section 3, the approximations to English (sentence quoted verbatim)
# https://en.wikipedia.org/wiki/Andrey_Markov and https://alexander-teplyaev.media.uconn.edu/wp-content/uploads/sites/1703/2024/01/Markov.pdf — Markov, 1913, 20,000 letters of Eugene Onegin
# https://quoteinvestigator.com/2022/09/18/word-company/ — Firth, 1957, "A synopsis of linguistic theory": "You shall know a word by the company it keeps"
# https://medium.com/plotly/understanding-word-embedding-arithmetic-why-theres-no-single-answer-to-king-man-woman-cd2760e2cb7f — word2vec 2013 and the excluded-input caveat
# https://arxiv.org/abs/2210.03629 — Yao et al., ReAct, 2022 (ICLR 2023)
# https://arxiv.org/abs/2404.13208 — Wallace, Xiao, Leike, Weng, Heidecke, Beutel (OpenAI), "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions", 19 April 2024 (slide 34: the system prompt ranked above the user's message)
# https://arxiv.org/abs/2307.03172 — Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang, "Lost in the Middle: How Language Models Use Long Contexts", 6 July 2023 (slide 33)
# https://arxiv.org/pdf/2509.04664 — first page of Kalai et al.: Kalai, Nachum and Zhang at OpenAI, Vempala at Georgia Tech (slide 36 notes)
# https://dl.acm.org/doi/10.1145/3442188.3445922 — Bender, Gebru, McMillan-Major, Shmitchell, "On the Dangers of Stochastic Parrots", FAccT 2021
# https://techcrunch.com/2024/08/26/anthropic-publishes-the-system-prompt-that-makes-claude-tick/ and https://simonwillison.net/2024/Aug/26/anthropic-system-prompts/ — system prompts published since August 2024
# https://community.openai.com/t/cheat-sheet-mastering-temperature-and-top-p-in-chatgpt-api/172683 and https://www.coursera.org/articles/openai-temperature — API temperature 0–2, default 1
# https://www.3blue1brown.com/lessons/mini-llm/ — "Large Language Models explained briefly", 20 November 2024
# https://aeon.co/videos/why-large-language-models-are-mysterious-even-to-their-creators — the same video listed at 8 minutes (YouTube is blocked from here; "Eight minutes" on slide 22)
# https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=LPZh9BOjkQs — and iv-5mZ_9CPY, yTAMrHVG1ew, KcSXcpluDe4: video titles verified
# https://codingscape.com/blog/llms-with-largest-context-windows — context-window sizes (kept vague on the slides)
