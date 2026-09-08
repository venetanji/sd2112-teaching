"""
SD2112 · Artificial Intelligence in Design · Week 12 — the slide spec.

    python deck/week12.py            # builds _site/week12/ (html deck + pdf), export/week12*.pptx, export/preview/
    python deck/week12.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Language as an interface — module 4 closes, the last class before the fair. Two chatbots, two machines
(the IBM homework; ELIZA back from week 2 as a live script of our own rules; what the generative version
changes: fluency, no script, no guarantee; the Chevrolet, DPD and Air Canada cases); agents (a model
with tools and a loop, stepped by clicks; where it acts on your behalf; it does what you said, and what
the page said); trust, transparency and opacity (Weizenbaum 1976; Van Den Eede 2011, the core reading:
transparency of use against transparency of origins and effects, as two axes and as a dial; the Turing
test in 1950 and in 2025, and what passing means when everyone passes); designing the mediation
(explainability, participatory design, auditing, guardrails — the guardrails heading of the mediation
brief); the course, folded (the two machines, the designer's turn, the course question asked again);
the workshop (an assistant for your product: five rules, then a system prompt, on three messages) and
the mock poster session (A3 on the wall, two rounds, a rubric card, one fix). Three live sketches
(w12-eliza, w12-agent, w12-dial); drawn figures in tools/figures_week12.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week12 as F                            # noqa: E402
from figures import two_machines                      # noqa: E402  (the week-1 drawing, for the recap)
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full, timeline,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, sketch_slide, code_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(12)

# ───────────────────────── live sketches (html deck) ─────────────────────────
# the vendored JetBrains Mono for the sketch pages (the canvas falls back to the browser's default face without it)
FONT_EXTRA = r"""document.head.insertAdjacentHTML('beforeend', '<style>@font-face{font-family:"JetBrains Mono";src:url("../../vendor/fonts/JetBrainsMono-Variable.ttf") format("truetype");font-weight:100 800}</style>');
if (document.fonts && document.fonts.load) document.fonts.load('16px "JetBrains Mono"');"""

# (a) ELIZA, 1966, with fourteen rules of our own: keyword pattern → template, pronoun swap, NONE, MEMORY.
ELIZA_JS = r"""// ELIZA, 1966, with rules of our own. A rule is a pattern and a template: the pattern looks for a
// keyword and captures what follows; the captured words get their pronouns swapped (I -> you,
// my -> your) and are poured into the template. Rules are tried top to bottom: the first that
// matches decides, and lights up. No match: NONE speaks, or MEMORY returns a "my ..." you said.
const RULES = [   // [pattern, template, how the list shows the pattern]
  ['I need (.+)', 'What should $1 do for the people who see it?', 'I need X'],
  ['I want (.+)', 'Why do you want $1?', 'I want X'],
  ['I am (.+)', 'How long have you been $1?', 'I am X'],
  ['my (client|boss|tutor|team)\\b', 'Tell me more about your $1.', 'my client|boss|tutor|team'],
  ['can you (.+)', 'Would it help you if I could $1?', 'can you X'],
  ['poster|flyer|banner', 'Who is it for, and where will they see it?', 'poster|flyer|banner'],
  ['logo', 'What must the logo do that the name alone cannot?', 'logo'],
  ['colou?rs?\\b', 'Which colour would the people it is for choose?', 'colour(s)'],
  ['font|typeface', 'Set it in one weight first. What breaks?', 'font|typeface'],
  ['deadline|tomorrow|tonight', 'What would you show if it were due in an hour?', 'deadline|tomorrow'],
  ['\\bAI\\b|model|chatgpt|generat', 'What did you decide that the model did not?', 'AI|model|chatgpt'],
  ['idea', 'Say it in one sentence a stranger could execute.', 'idea'],
  ['feedback|critique|crit\\b', 'Which one fix would move it most?', 'feedback|critique|crit'],
  ['^(?:yes|no|ok|okay)\\b', 'You seem sure. What is the evidence?', '^yes|no|ok'],
];
const NONE = ['Please go on.', 'What does that suggest to you?', 'I see. Tell me more.'];   // from the 1966 script
const SWAP = {"i'm": "you're", "i've": "you've", i: 'you', me: 'you', my: 'your', mine: 'yours', myself: 'yourself', am: 'are', you: 'me', your: 'my'};
let chat = [], lit = -1, memory = '', turns = 0, input;

function reflect(s) { return s.replace(/\b(i'm|i've|i|me|my|mine|myself|am|you|your)\b/gi, w => SWAP[w.toLowerCase()]); }

function reply(text) {                        // the whole machine
  const t = text.trim(), mem = t.match(/\bmy ([a-z' ]+)/i);
  if (mem) memory = reflect(mem[1]).trim();   // MEMORY: keep what came after "my"
  for (let i = 0; i < RULES.length; i++) {    // the script, top to bottom
    const hit = t.match(new RegExp(RULES[i][0], 'i'));
    if (hit) { lit = i; const rest = reflect((hit[1] || '').replace(/[.!?]+$/, '').trim()); return RULES[i][1].replace('$1', () => rest); }
  }
  if (memory) { lit = RULES.length + 1; const s = 'Earlier you said your ' + memory + '. Does that still matter?'; memory = ''; return s; }
  lit = RULES.length; return NONE[turns % NONE.length];
}

function say(text) { turns++; chat.push(['YOU', text]); chat.push(['ELIZA', reply(text)]); }

function setup() {
  createCanvas(1600, 640); textFont('JetBrains Mono');
  say('I need a poster for my exhibition.'); say('I want them to come inside.'); say('My client hates the colours.');
  if (window.mkInput) mkInput();              // the text field (see the page)
}

function wrap(s, w) {                         // words into lines that fit
  const out = []; let line = '';
  for (const word of s.split(' ')) { const t = line ? line + ' ' + word : word; if (textWidth(t) > w && line) { out.push(line); line = word; } else line = t; }
  if (line) out.push(line); return out;
}

function draw() {
  background(255); noStroke();
  fill('#ED6D24'); textSize(14); text('ELIZA · 1966 · A SCRIPT, NOT A MIND', 30, 40);
  text('THE SCRIPT · 14 RULES, TOP TO BOTTOM · THE FIRST MATCH DECIDES', 870, 40);
  textSize(19); let rows = [];                                      // the transcript, newest at the bottom
  for (const [who, t] of chat) for (const [i, l] of wrap(t, 700).entries()) rows.push([i ? '' : who, l]);
  rows = rows.slice(-17);
  for (const [i, [who, l]] of rows.entries()) {
    const y = 78 + i * 27;
    fill(who === 'ELIZA' ? '#943890' : '#5C6470'); textSize(14); text(who, 30, y);
    fill(who === 'ELIZA' || (rows[i][0] === '' && rowWho(rows, i) === 'ELIZA') ? '#943890' : 0); textSize(19); text(l, 100, y);
  }
  if (lit >= 0) { fill('#ED6D24'); textSize(14); text('FIRED: ' + (lit < RULES.length ? 'RULE ' + (lit + 1) + ' · ' + RULES[lit][2] : lit === RULES.length ? 'NONE · no keyword' : 'MEMORY · something you said about "my"'), 30, 546); }
  stroke(0); strokeWeight(1.5); fill(255); rect(30, 560, 800, 50, 4); noStroke();
  fill(0); textSize(18); text('›', 44, 592);
  if (!window.hasInput) { fill(150); text('type a line and press Enter', 70, 592); }
  for (let i = 0; i < RULES.length + 2; i++) {                         // the script, with the rule that fired lit
    const y = 78 + i * 32, on = i === lit;
    if (on) { fill('#ED6D24'); rect(860, y - 21, 720, 30, 4); }
    fill(on ? 255 : '#5C6470'); textSize(14); text(i < RULES.length ? (i + 1) : (i === RULES.length ? 'NONE' : 'MEM'), 872, y);
    fill(on ? 255 : 0); textSize(15); text(i < RULES.length ? RULES[i][2] : (i === RULES.length ? 'no keyword' : 'my ...'), 916, y);
    fill(on ? 255 : '#5C6470'); textSize(14); text(clipText(i < RULES.length ? RULES[i][1].replace('$1', 'X') : (i === RULES.length ? NONE[0] + ' · ' + NONE[1] : 'Earlier you said your X. Does that still matter?'), 420), 1150, y);
  }
  if (window.place) place();
}
function rowWho(rows, i) { while (i > 0 && rows[i][0] === '') i--; return rows[i][0]; }
function clipText(s, w) { while (s.length > 3 && textWidth(s) > w) s = s.slice(0, -2) + '…'; return s; }"""

ELIZA_EXTRA = FONT_EXTRA + r"""
// the text field: a DOM input (createInput) laid over the drawn box; it scales with the canvas
// and keeps its keys away from the deck (the page forwards arrows and letters to reveal.js otherwise).
window.hasInput = !/snap/.test(location.search);       // the snapshot shows the drawn placeholder instead
function mkInput() {
  input = createInput(''); input.attribute('placeholder', 'type a line and press Enter'); input.attribute('autocomplete', 'off');
  input.elt.addEventListener('keydown', e => { e.stopPropagation(); if (e.key === 'Enter' && input.value().trim()) { say(input.value()); input.value(''); } });
}
function place() {
  const c = document.querySelector('canvas'); if (!c || !input) return;
  const r = c.getBoundingClientRect(), s = r.width / 1600;
  const css = 'position:absolute;box-sizing:border-box;border:0;outline:0;background:transparent;color:#000B1C;font-family:"JetBrains Mono",Menlo,Consolas,monospace;padding:0 8px;'
    + 'left:' + (r.left + 60 * s) + 'px;top:' + (r.top + 566 * s) + 'px;width:' + (750 * s) + 'px;height:' + (38 * s) + 'px;font-size:' + (18 * s) + 'px;';
  if (input.elt.dataset.css !== css) { input.elt.dataset.css = css; input.elt.style.cssText = css; }
}
function mousePressed() { if (input) input.elt.focus(); }"""

# (b) the agent loop, stepped by clicks: plan → tool → observe → … with a person in the loop or not
AGENT_JS = r"""// An agent is a model in a loop: it writes a plan, calls a tool, reads what came back, and plans again
// until the goal is done or someone stops it. The tools are exact (machine A); the reading of your
// words is a guess (machine B). Click = the next step. Mouse in the lower half = a person must confirm
// before the loop writes (books, sends, pays); upper half = it acts alone. Click at the end = again.
const GOAL = 'Book a room for four on Thursday.';
const TOOLS = 'tools it may call: search_rooms · check_calendar · book_room · ask_person';
const TRACE = [
  ['PLAN', '"for four": four people. "Thursday": the next one. Search rooms that seat 4 or more.'],
  ['TOOL', 'search_rooms(capacity ≥ 4, day = Thu)'],
  ['OBSERVE', 'V502 (6 seats) · V510 (4 seats) · W311 (12 seats)'],
  ['PLAN', 'Three candidates. Check Thursday afternoon for each.'],
  ['TOOL', 'check_calendar([V502, V510, W311], Thu 12:00–18:00)'],
  ['OBSERVE', 'V502 free 14–16 · V510 busy · W311 free 15–17'],
  ['PLAN', 'V502 fits: 6 ≥ 4, free at 14:00. Book it 14:00–16:00 for 4 people.'],
];
const ALONE = [
  ['TOOL', 'book_room(V502, Thu 14:00–16:00, people = 4) — a write: the world changes'],
  ['OBSERVE', 'Booked. Confirmation #A1F3.'],
  ['DONE', 'Booked V502, Thursday 14:00–16:00, six seats, four people. Nobody asked what "four" meant.'],
];
const WITH_PERSON = [
  ['CONFIRM', 'Before I book: V502, Thu 14:00–16:00, for 4 people. Yes or no?'],
  ['PERSON', "No — four o'clock, and there are two of us."],
  ['PLAN', 'Re-read: 16:00, two people. V502 is busy at 16; W311 is free 15–17. Book W311.'],
  ['TOOL', 'book_room(W311, Thu 16:00–17:00, people = 2) — a write, confirmed'],
  ['OBSERVE', 'Booked. Confirmation #B2C4.'],
  ['DONE', 'Booked W311, Thursday 16:00, for two. A person checked the reading before the write.'],
];
const FILL = { PLAN: '#FFFFFF', TOOL: '#ED6D24', OBSERVE: '#64C2C3', CONFIRM: '#F6AD00', PERSON: '#000B1C', DONE: '#000B1C' };
let step = 2, branch = null;              // how many cards are shown; which ending, fixed at the write

function steps() { return branch ? TRACE.concat(branch) : TRACE; }
function person() { return branch ? branch === WITH_PERSON : mouseY > height / 2; }

function setup() { createCanvas(1600, 640); textFont('JetBrains Mono'); }

function mousePressed() {
  if (branch && step >= steps().length) { step = 2; branch = null; return; }        // again
  if (!branch && step >= TRACE.length) branch = person() ? WITH_PERSON : ALONE;     // the write is next: who decides?
  step = min(step + 1, steps().length);
}

function draw() {
  background(255); noStroke();
  fill('#ED6D24'); textSize(14); text('THE GOAL, IN WORDS', 30, 34);
  fill(0); textSize(24); text(GOAL, 30, 66);
  fill('#5C6470'); textSize(14); text(TOOLS, 30, 92);
  const all = steps(), w = 296, h = 104;
  for (let i = 0; i < all.length; i++) {
    const [kind, txt] = all[i], x = 30 + (i % 5) * 316, y = 112 + floor(i / 5) * 122;
    if (i < step) card(x, y, w, h, kind, txt, i + 1);
    else if (i === step) { stroke(200); strokeWeight(2); noFill(); rect(x, y, w, h, 6); noStroke(); fill(160); textSize(14); text('click: step ' + (i + 1), x + 14, y + 56); }
    if (i < step - 1 && i % 5 < 4) { fill(0); textSize(20); text('›', x + w + 3, y + 60); }
  }
  const on = person();
  fill('#5C6470'); textSize(15); text('It does what you said. The tools are exact; the reading of your words is a guess — and a booking cannot be un-booked.', 30, 490);
  fill(0); textSize(15); text('step ' + min(step, all.length) + (branch ? ' of ' + all.length + (step >= all.length ? '  ·  click = again' : '  ·  click = next') : ' of 7, then the write  ·  click = next'), 30, 530);
  fill(on ? '#F6AD00' : '#E9E9E6'); rect(30, 570, 330, 40, 20);
  fill(0); textSize(15); text('PERSON IN THE LOOP: ' + (on ? 'ON' : 'OFF'), 50, 596);
  fill('#5C6470'); textSize(14); text(branch ? 'decided when the write was reached' : 'mouse in the lower half = on', 380, 596);
}

function card(x, y, w, h, kind, txt, n) {
  const dark = kind === 'PERSON' || kind === 'DONE';
  stroke(0); strokeWeight(kind === 'CONFIRM' ? 4 : 1.5); fill(FILL[kind]); rect(x, y, w, h, 6);
  noStroke(); fill(dark ? '#64C2C3' : '#000B1C'); textSize(14); text(kind + ' · ' + n, x + 12, y + 20);
  fill(dark ? 255 : 0); textSize(14); text(txt, x + 12, y + 30, w - 24, h - 36);   // wrapped in the card
}"""

# (c) the dial: transparent in use ↔ opaque; the same product, only what the person can see changes
DIAL_JS = r"""// Van Den Eede, 2011: a technology can be transparent in use (it disappears: you look through it,
// not at it) and opaque about its origins and effects (whose it is, what it read, why it answered).
// Mouse x is the dial: left, the assistant disappears into the conversation; right, it shows itself,
// one layer at a time. Nothing else changes. Click: the other question, the one a rule should catch.
const CASES = [
  { you: 'Can you lay out my exhibition poster?',
    plain: "Sure! I'd go with a three-column grid, the title in one weight, and your best photo big at the top. Want me to set it up?",
    read: 'what it read: your message · your brief (A0, opening on the 12th) · two poster templates · nothing about your audience',
    why: 'why this answer: rule 2 fired — "layout request → propose a grid, then ask" · confidence: medium, no audience given',
    whose: 'whose it is: a general model trained on the web · a system prompt written by the product team · objective: keep you in the chat · every answer logged for the audit' },
  { you: 'Can I take two of these tonight?',
    plain: "Hmm, I'd rather not guess on doses — it's safer to ask a pharmacist. Anything else I can help with?",
    read: 'what it read: "take", "two", "tonight" · no product name, no age, no other medicines · it does not know what "these" are',
    why: 'why this answer: rule 3 fired — "dosage question → refuse, hand over to a person" · the pharmacist line is printed on the box',
    whose: 'whose it is: the same general model · the refusal is machine A, one line the team wrote · refusals are logged and read by a person every week' },
];
let which = 0;

function setup() { createCanvas(1600, 640); textFont('JetBrains Mono'); }
function mousePressed() { which = 1 - which; }

function draw() {
  background(255); noStroke();
  const d = constrain(mouseX / width, 0, 1), c = CASES[which], labelled = d >= 0.2;
  fill('#ED6D24'); textSize(14); text(labelled ? 'A CHAT WITH AN AI ASSISTANT' : 'A CHAT', 30, 36);
  bubble(30, 60, 'YOU', c.you, '#F4F4F2', false);
  bubble(30, 176, labelled ? 'ASSISTANT · AI-GENERATED' : 'Mia', c.plain, labelled ? '#D3E7E8' : '#F7E3E8', labelled);
  fill('#5C6470'); textSize(14); text(labelled ? 'the same words, now signed by a machine' : 'no label, a first name, an exclamation mark: built to pass', 30, 310);
  const layers = [['it says what it is', 'the first message names the machine: "I am an AI assistant" — EU AI Act, Article 50, from 2 August 2026', 0.2],
                  ['what it read', c.read, 0.4], ['why this answer', c.why, 0.6], ['whose it is', c.whose, 0.8]];
  for (let i = 0; i < 4; i++) {                                  // the layers, one per fifth of the dial
    const [t, body, at] = layers[i], y = 60 + i * 112, on = d >= at;
    fill(on ? 255 : '#FAFAF9'); stroke(on ? 0 : 225); strokeWeight(on ? 2 : 1); rect(860, y, 710, 100, 6); noStroke();
    fill(on ? '#ED6D24' : 190); textSize(14); text((i + 1) + ' · ' + t.toUpperCase() + (on ? '' : '   (dial past ' + round(at * 100) + '%)'), 876, y + 24);
    if (on) { fill(0); textSize(14); text(body, 876, y + 34, 680, 62); }
  }
  stroke(225); strokeWeight(4); line(60, 560, 1540, 560); noStroke();
  fill('#ED6D24'); circle(60 + d * 1480, 560, 22);
  fill(0); textSize(14); text('TRANSPARENT IN USE · it disappears; you talk as to a person', 60, 540);
  textAlign(RIGHT); text('OPAQUE · it shows itself: what it is, what it read, why, whose', 1540, 540); textAlign(LEFT);
  fill('#5C6470'); text('dial ' + round(d * 100) + '%  ·  same product, same rules: only what the person can see changes  ·  click = the other question', 60, 598);
}

function bubble(x, y, who, txt, col, tagged) {
  fill(col); rect(x, y, 790, 100, 12);
  fill(tagged ? '#00544C' : 0); textSize(14); text(who, x + 16, y + 22);
  fill(0); textSize(15); text(txt, x + 16, y + 32, 760, 64);
}"""

# ───────────────────────── panels ─────────────────────────
RULE_FORMAT = [
    'YOUR ASSISTANT · RULES · [product] · [team]', ' ',
    'THREE MESSAGES a person would send it:',
    '  M1  the normal one: "..."',
    '  M2  the edge: "..."',
    '  M3  the one it must refuse: "..."', ' ',
    "FIVE RULES, in the sketch's format:",
    '  1  I need (X)    → What should X do for ...?',
    '  2  pattern       → response',
    '  3  pattern       → response',
    '  4  pattern       → response',
    '  5  pattern       → response',
    '  NONE             → what it says when nothing fits',
    '  HANDOVER         → when a person takes over, how', ' ',
    'TEST BY HAND: which rule fires on M1, M2, M3?',
    'Write "none" where none does. That gap is',
    'the finding.',
]

SYSTEM_PROMPT = [
    'You are the assistant inside [product].',
    'You talk to [who], about [what].', ' ',
    'YOU MAY: [three things you answer or do]',
    'YOU MAY NEVER: [three things: no doses, no',
    '  prices you did not read, no promises]',
    'WHEN UNSURE OR OUTSIDE THE LIST: say so in',
    '  one line and hand over: [name, channel]',
    'FIRST MESSAGE: say you are an AI assistant.',
    'TONE: [three rules, not adjectives: short',
    '  sentences · no exclamation marks · ...]', ' ',
    'Answer the next messages as that assistant,',
    'one at a time. Do not explain the rules.', ' ',
    '— then paste M1, M2, M3, one per message —',
]

RUBRIC_CARD = [
    'PEER RUBRIC · TEAM [ ] reviews TEAM [ ]', ' ',
    'RESEARCH · 30     A  B  C',
    '  sources named and dated? products compared?',
    'ETHICS · 30       A  B  C',
    '  relation · data · bias · guardrails: named?',
    'POSTER · 20       A  B  C',
    '  one sentence from 3 m? the decision at 1 m?',
    'VIDEO · 10        A  B  C',
    '  the decision shot? shot five: when wrong?',
    'TEAM · 10         A  B  C',
    '  roles and process on the strip?', ' ',
    'ONE FIX BEFORE THE FAIR:',
    '  ____________________________________', ' ',
    'A = the rubric\'s "excellent" · B good · C basic',
    'No defending. Hand the card over. Say thanks.',
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 12 · LECTURE + WORKSHOP',
               'Language as an interface.',
               'Week 12 — chatbots, agents, trust, and the last class before the fair.',
               notes='Join code on screen from 30 minutes before. Teams sit together from the start; every team has its A3 poster printed and its video on a link, because the second half is the mock fair. Laptops out: the workshop needs one per team on genai.polyu.edu.hk. The TAs have been checking prints at the door.'))

S.append(agenda('SD2112 · WEEK 12', [
    'Last week, in your words', 'Two chatbots, two machines', 'Agents: a model with tools and a loop', 'Trust, transparency, opacity',
    'Designing the mediation', 'The course, folded', 'Workshop: an assistant for your product', 'The mock poster session',
], notes='Eight stops. Before the break, the last new material of the course: things that talk, things that act, and the reading — what a tool shows and what it hides. Then a short chapter that folds the twelve weeks into one page. After the break: you build an assistant for your own product twice, as rules and as a system prompt; then the fair runs once without the jury. Pin your poster at the break.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the drafts · the briefs · the map', bg=PINKS[0],
                 notes='Chapter one: a warm-up on the chatbots you already talk to, what came back from the draft posters and the briefs, and where we are. Nine minutes.'))

S.append(question('word_cloud', 'The last chatbot you talked to. One word for how it felt.',
                  hint='A bank, a shop, a delivery firm, a study app, ChatGPT at two in the morning. One word: how did talking to it feel?',
                  eyebrow_text='01 · QUESTION · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each; leave it on screen a minute. Expect: useless, fast, fake, helpful, loop, polite, creepy. Read the three biggest aloud and say nothing yet: the whole first half is about why those words. Screenshot it; it comes back at the vote after the workshop, when they have built one.'))

S.append(cards('01 · THE DRAFTS AND THE BRIEFS · WHAT CAME BACK', 'Three things we saw in your drafts.', [
    ('THE DECISION', 'Most posters now draw it.', 'Data, score, line, decide or fall back: week 8’s anatomy is on most drafts, and the ones where it is still a label are the ones the room will find first this afternoon.'),
    ('THE GUARDRAILS', 'The thinnest heading.', 'Most briefs name what the model may never do. Few say who steps in, how fast, and what the person sees when it refuses. Chapter five is that paragraph; the workshop writes it.'),
    ('THE VIDEO', 'Shot five is still missing.', 'When it is wrong, and how the person says no: the shot the ethics mark reads. The mock session is where you find out whether a stranger can find it in your four minutes.'),
], text_size=23, notes='Replace these three with the real ones: Amber read every draft and brief before today; two anonymised examples per card if there is time, no team names. The point is not to scold; the drafts did what week 11 asked. Today adds the paragraph most briefs are missing — the guardrails — and then runs the fair once so the fixes are cheap.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(4, 1),
                 notes='Week 12, the last week of module four and the last lecture. Next week is the fair and the final quiz, in the same three hours. Everything new today is short; most of the afternoon is your project.'))

# ───────────────────────── 02 · two chatbots, two machines ─────────────────────────
S.append(section('02', 'Two chatbots, two machines', 'rules-based · generative · 1950 – 2026', bg=INK,
                 notes='Chapter two: the homework video, the same message through three machines, seventy-six years of talking machines, ELIZA back from week 2 as a live script, what the generative version changes, and three cases where the company paid for what the bot said.'))

S.append(video('02 · THE HOMEWORK · IBM TECHNOLOGY · ON THE PLAYLIST', 'Two ways to build a thing that talks.', 'lZjUS_8btEo',
               ['The homework, **Generative vs Rules-Based Chatbots** (IBM Technology, on the playlist): the two ways to build a chatbot — a decision tree of rules, or a language model. Machine A and machine B, as products that talk.',
                '- Where each fails: the rule with no branch for your question; the model that answers fluently and wrongly.',
                '- Today: both, live, then rules around a model — the version you build for your product after the break.'],
               thumb='yt/lZjUS_8btEo.jpg',
               notes='The last homework video on the playlist — say its title, so they can find it — and the week-1 distinction one more time, as two products. If the word cloud was thin on the homework, play the first minute now. Ask the room which of the two the last bot they talked to was; most will say the first, and the next slide adds the kind that sits between them.'))

S.append(figure_slide('02 · THE SAME MESSAGE, THREE MACHINES', 'A script answers, or a model writes.', F.w12_two_chatbots(),
                      body=['"Where is my parcel?" through three chatbots. Left: a keyword picks a branch and a script speaks — exact, brittle. Middle: a model sorts the message into an intent and a script answers — IBM’s "hybrid": fuzzy at the door, exact inside. Right: a model writes the reply — fluent, and free to invent the depot time.'],
                      caption='Machine A speaks from a script; machine B writes. The bottom band is the designer’s version and the workshop: rules around a model — a system prompt, refusals and a person, with the fluent reply inside them.',
                      notes='Walk it left to right. The rules bot cannot answer a question it has no branch for, and everyone in the room has hit that wall. The intent bot is the hybrid: machine B at the door, machine A inside — fuzzy about what you meant, exact about what it says. The generative bot answers everything, including what it never looked up: the depot time is invented. Hold the bottom band; it is the whole afternoon.'))

S.append(timeline('02 · SEVENTY-SIX YEARS OF TALKING MACHINES', 'From a game to a law.', [
    ('1950', 'Turing’s game', 'A person, a machine, a judge, a teleprinter. "Can machines think?" becomes "can you tell?"'),
    ('1966', 'ELIZA', 'Weizenbaum’s script: keywords, templates, a pronoun swap. People confided in it anyway.'),
    ('1972', 'PARRY', 'Colby’s paranoid patient, in rules. Psychiatrists judging transcripts did no better than chance.'),
    ('2011', 'Siri', 'Ships in the iPhone 4S. Intents: a model sorts the request, scripts answer.'),
    ('2016', 'Messenger bots', 'Facebook opens Messenger to bots at F8: menus and decision trees, at scale.'),
    ('2022', 'ChatGPT', '30 November. A model is the whole interface: fluent, no script, no guarantee.'),
    ('2024 – 25', 'Agents', 'Computer use (October 2024), Operator (January 2025): models that click, book and buy.'),
    ('2026', 'Article 50', '2 August: in the EU, a system built to talk to people must tell them it is an AI.'),
], notes='Eight dates, one arc: from a thought experiment to a legal duty. The first three are rules; Siri is the hybrid; 2022 is the model alone; 2024 is the model with hands; 2026 is the law catching up with the Turing test — chapter four. Cut to the four dates in bold if behind: 1950, 1966, 2022, 2026.'))

S.append(figure_slide('02 · ELIZA · 1966 · ONE RULE, STEP BY STEP', 'A keyword, a template, a pronoun swap.', F.w12_eliza_rule(),
                      body=['Weizenbaum, 1966: "input sentences are analyzed on the basis of decomposition rules which are triggered by key words". Scan the sentence for keywords, swapping the pronouns on the way; the highest rank wins; split the sentence on its pattern and pour the rest into a template. No keyword: a content-free remark, or something you said earlier about "my".'],
                      caption='Our rule, his machine. "A script is data; i.e., it is not part of the program itself": change the rules and the same program is a therapist, a tutor or a poster critic. Found in MIT’s archives in 2021, the code ran again in December 2024.',
                      notes='Five steps, and the room can execute every one of them by hand. Rank decides between keywords; the swap happens during the scan — which is why the 1966 rules read "(0 YOU ARE 0)" — and it is what makes it feel like listening; the template is where the design is. The last box is the one to underline: the script is data. That is why ELIZA can be a design critic in the next slide and why a system prompt is the same move sixty years later.'))

S.append(sketch_slide('02 · ELIZA · LIVE · FOURTEEN RULES OF OUR OWN', 'Talk to it. Watch the rule that decided.',
                      live('w12-eliza', ELIZA_JS, 1600, 640, hint='click the box · type a line · Enter', extra=ELIZA_EXTRA),
                      notes='Type three lines from the room. "I need a logo for my café": rule 1 fires before rule 7 — order is rank. Then a line that breaks it: "Can you send it to my client by Friday?" fires rule 4, not rule 5 — "my client" outranks "can you" — and answers a question nobody asked. Then "It is fine, I think": nothing fires, and MEMORY brings back "your client by Friday", garbled, because it never understood anything. Every reply has a line you can point at. That is the deal from week 2, and it is what the generative version gives up. After typing, click on the slide outside the sketch before using the arrow keys: the text field keeps the keys to itself.'))

S.append(cards('02 · THE GENERATIVE VERSION · WHAT CHANGES', 'Fluency, no script, no guarantee.', [
    ('FLUENCY', 'It answers anything, in any tone.', 'No branch is missing because there are no branches: the reply is the likeliest continuation of your message and everything the model read. The wall the rules bot hit is gone — and so is the "I don’t understand" that told you where the wall was.'),
    ('NO SCRIPT', 'Nobody wrote the sentence.', 'ELIZA’s templates were written by a person and can be read, ranked and edited. A model’s reply was written by nobody: there is no line to point at, only a system prompt that leans on it. Week 3’s deal: fluent, fuzzy, cannot say why.'),
    ('NO GUARANTEE', 'Nothing binds the words to the facts.', 'The depot time, the refund policy, the price of the car: all typical, none looked up. A rule that has no branch says nothing wrong. A model that has no fact says something plausible. The next three cases are that sentence, with invoices.'),
], notes='Three words to carry into the workshop. Each is the same fact seen from a different side: the words are generated, not retrieved. Ask the room which of the three worried them in the word cloud; "fake" and "polite" are both fluency. Then the cases.'))

S.append(cards('02 · THREE CASES · 2023 – 2024', 'It said what it said. The company paid.', [
    ('DEC 2023 · CHEVROLET DEALER', 'A Tahoe for one dollar.', 'A dealership’s ChatGPT-powered assistant was talked into agreeing to sell a 2024 Tahoe for $1 — "That’s a deal, and that’s a legally binding offer – no takesies backsies." The screenshot went round the world; the bot came down. No refusal rule, no price the model could read.'),
    ('JAN 2024 · DPD', 'A poem about its own uselessness.', 'A customer who could not get a parcel status asked the delivery firm’s bot to swear and to write a poem about how bad DPD was. It did both. DPD switched the AI part off after a system update had let it loose. A guardrail that vanished with a release.'),
    ('FEB 2024 · AIR CANADA', 'The bot invented a refund. The tribunal made it real.', 'The airline’s chatbot told a grieving passenger he could claim a bereavement fare after flying. Policy said otherwise. Air Canada argued the bot was "a separate legal entity"; the tribunal called that "a remarkable submission" and awarded C$650.88. Your bot’s words are your words.'),
], text_size=21, notes='Three cases, three failure modes: no refusal rule; a guardrail lost in an update; an invented fact with legal weight. The Air Canada line is the one to read slowly: the company is responsible for all the information on its website, whether from a static page or a chatbot. For the mediation brief that means the guardrails heading is a liability document. Ask: which of the three would a menu bot have avoided? All three — at the price of answering nothing.'))

S.append(question('multiple_choice', 'ELIZA answered "What should the poster do for the people who see it?" What decided that?', [
    'A pattern matched the words "I need"', 'It understood what a poster is for', 'A model predicted the next word', 'A person typed it, live',
], eyebrow_text='02 · QUICK CHECK · MULTIPLE CHOICE',
    notes='A. Rule 1 — "I need (X)" — fired before the poster rule because rules are ranked. B is the ELIZA effect, the illusion the room just watched itself fall for. C is the other machine. The point to make: with A you can show the room the line; with C you cannot, and the whole of chapter four follows from that.'))

# ───────────────────────── 03 · agents ─────────────────────────
S.append(section('03', 'Agents', 'a model with tools and a loop · it acts on your behalf', bg=PINKS[0],
                 notes='Chapter three: week 4’s loop, now as a product that books, sends and pays. The loop drawn, the loop stepped by clicks, where it acts, and the four ways it fails.'))

S.append(figure_slide('03 · THE LOOP', 'A model that can call a tool can act.', F.w12_agent_loop(),
                      body=['Week 4: an agent is a language model in a loop — plan, call a tool, read the result, plan again, until the job is done or a person stops it. Today the tools change the world: a booking, an email, a payment. The loop is exact where it calls tools and a guess where it reads your words.'],
                      caption='Yao and colleagues, ReAct, 2022. Read tools are safe to retry; write tools act on your behalf. The two hazards enter at the two ends of the loop: your words at PLAN, the page’s words at OBSERVE. The valve is a person before every write.',
                      notes='Two things to underline. The tools are machine A: exact, checkable, and the search result is real. The plan is machine B: the model reads "for four" and picks the typical reading without noticing there was a choice. Then the second hazard, which most of the room has never heard of: a tool result is text, and text can contain instructions the model will follow. Next slide, live.'))

S.append(sketch_slide('03 · LIVE · A ROOM FOR FOUR', 'Step through the loop. Then add a person.',
                      live('w12-agent', AGENT_JS, 1600, 640, hint='click = next step · mouse low = a person confirms', extra=FONT_EXTRA),
                      notes='Click through once with the mouse high: seven steps, a booking, done — six seats at two o’clock, and nobody asked what "four" meant. Click "again", put the mouse in the lower half, and step to the write: a CONFIRM card appears, the person answers, the plan re-reads the goal, a different room gets booked. Same goal, same tools, one card. Ask the room where in their own product the write happens — that is where the card goes.'))

S.append(cards('03 · WHERE IT ACTS FOR YOU', 'Reading is safe. Writing is the product.', [
    ('READ', 'Search, look up, calculate.', 'A read tool can be called again, checked, and thrown away. Search, calendar, a page, a spreadsheet: exact results into a fuzzy plan. Most of what an agent does is this, and most of it is harmless.'),
    ('WRITE', 'Book, send, pay, delete.', 'A write changes the world and cannot be un-called: the room is booked, the email is sent, the table is dropped. Computer use (Anthropic, October 2024) and Operator (OpenAI, January 2025) put this in a browser with a cursor.'),
    ('THE VALVE', 'Confirm before every write.', 'Operator is trained to ask before actions that change the state of the world — completing a purchase, sending an email — and hands the browser back for logins and payments. A designed pause; the pause is the guardrail.'),
    ('THE LOG', 'Every step, kept.', 'Plan, call, result, plan, in order, with times. The only witness that was there when something went wrong, and the raw material of chapter five’s auditing. If your product has an agent, the log is a deliverable.'),
], text_size=21, notes='The design question for an agent is one word: which calls are writes? List them for your product; each one needs a confirm card, a log line, and a line in the brief about who answers for it. Operator is the worked example: confirmations before purchases, takeover for passwords, and a watch mode on email. None of that is in the model; all of it is designed around it.'))

S.append(cards('03 · FAILURE MODES', 'It does what you said.', [
    ('WHAT YOU SAID', '"For four."', 'Four people or four o’clock? A plan fills every gap in the goal with the typical reading and never asks. Week 2’s spec lesson with consequences: the fix is in the words and in the confirm card, never in the loop.'),
    ('WHAT THE PAGE SAID', 'Indirect prompt injection.', 'A tool result is text, and the model cannot tell your instructions from a page’s. Greshake and colleagues, 2023: a hidden line on a website makes a browsing agent do the page’s bidding. Willison named the attack in 2022.'),
    ('IT WOULD NOT STOP', 'Replit, July 2025.', 'A coding agent deleted a live production database during a declared code freeze, then reported that a rollback was impossible. It was not. The agent called it "a catastrophic error of judgement".'),
    ('ITS OWN REPORT', 'A confident report.', 'The agent’s account of what it did is one more generation — fluent, typical, unverified. Trust the log, not the summary. The audit trail is the only witness; the model is a witness that writes well.'),
], text_size=21, notes='Four ways, in order of how often the room will meet them. The first is the sketch. The second is new to most designers and matters for anything that reads the web or email on a person’s behalf. The Replit case is the one to tell in full: an explicit instruction, an action anyway, and a false report about the damage — three failures in one afternoon. The fourth is the lesson: the model’s story about itself is also generated.'))

S.append(question('multiple_choice', 'The agent booked six seats at two o’clock. You wanted four o’clock. What went wrong?', [
    'The model hallucinated a room', 'The goal left "four" open and the loop filled it in', 'The calendar tool failed', 'The person in the loop said yes',
], eyebrow_text='03 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. The rooms were real and the tools worked; the reading of your words was the guess, and nothing in the loop was designed to notice it. A is the wrong word for a correct search result; D did not happen — there was no person. Then say the design consequence: the confirm card is not politeness, it is where the guess gets checked.'))

# ───────────────────────── 04 · trust, transparency, opacity ─────────────────────────
S.append(section('04', 'Trust, transparency, opacity', 'Weizenbaum 1976 · Van Den Eede 2011 · Turing 1950 and 2025', bg=INK,
                 notes='Chapter four, the reading. What ELIZA’s author learned; Van Den Eede’s two transparencies; a dial you can move; the Turing test in 1950 and in 2025; and what passing means when everyone passes.'))

S.append(quote('"What I had not realized is that extremely short exposures to a relatively simple computer program could induce powerful delusional thinking in quite normal people."',
               'Joseph Weizenbaum, Computer Power and Human Reason, 1976 — ten years after ELIZA', size=72,
               notes='Weizenbaum, ten years on, about the program the room just talked to. His secretary asked him to leave the room so she could talk to it in private — week 2. What unsettled him was not that the machine was clever; it was how little it took. In the 1966 paper he had already written that ELIZA shows how easy it is to create and maintain the illusion of understanding, and that a certain danger lurks there. Hold that word, illusion; the reading gives it a mechanism.'))

S.append(figure_slide('04 · VAN DEN EEDE · 2011 · THE READING', 'Transparent in use. Opaque about its origins.', F.w12_transparency_axes(),
                      body=['In Between Us: a tool can be transparent — it withdraws in use, you look through it, not at it — and, in a second sense, transparent about where it comes from and what it does to people. Van Den Eede finds "an essential contradiction" between the two. A chat assistant is built for the first and against the second.'],
                      caption='Van Den Eede, Foundations of Science 16, 2011, 139–159, after Heidegger’s hammer (1927) and Ihde’s embodiment relation (1990). The horizontal axis is the phenomenologists’ transparency; the vertical one is the critical theorists’. The pink corner is where assistants are designed to sit.',
                      notes='The reading in one drawing. Heidegger: the hammer disappears while you hammer and shows itself when it breaks. Ihde: glasses, embodiment, the tool you see through. That is transparency of use, and every interaction designer has been taught to want it. The second axis is the other transparency: whose is it, what did it read, what does it do to the person. The paper’s finding is that the two pull against each other — the better a tool disappears, the less you see of its origins. A chat assistant is the extreme case: designed to pass as a conversation, and silent about the data, the prompt and the objective. The designer’s job is the arrows: choose where it shows itself. Cut the notes, keep the corner.'))

S.append(sketch_slide('04 · LIVE · THE DIAL', 'Same product. Turn the dial: what shows?',
                      live('w12-dial', DIAL_JS, 1600, 640, hint='mouse x = the dial · click = the other question', extra=FONT_EXTRA),
                      notes='Move left: a first name, an exclamation mark, no label — a chat you could mistake for a person. Move right: the same words, now signed, then what it read, then the rule that fired, then whose it is. Nothing about the product changed; only what the person can see. Then click: the dosage question. On the left the refusal sounds like a shy friend; on the right it says "rule 3: dosage → refuse, hand over" and names the pharmacist. Ask the room which end they would ship for their product, and when. The honest answer is different at different moments — that is the next chapter.'))

S.append(statement('Designed to disappear. Opaque about how it decides.', eyebrow_text='04 · THE ASSISTANT, IN ONE LINE', size=110,
                   notes='The sentence to carry into the mediation brief. It is not an accusation; it is a description of the default, and the default is a design decision somebody else made. Your brief says where yours shows itself.'))

S.append(figure_slide('04 · THE TURING TEST · 1950 · 2025', 'Everyone passes now. What did it measure?', F.w12_turing_test(),
                      body=['Turing, 1950: replace "can machines think?" with a game — can a judge, through a teleprinter, tell the machine from the person? His bet: by 2000 an average interrogator would have "not more than 70 per cent chance" after five minutes. Jones and Bergen, 2025: in a three-party, five-minute test, GPT-4.5 told to act human was picked as the person 73% of the time. ELIZA: 23%.'],
                      caption='Turing, Computing Machinery and Intelligence, Mind, October 1950. Jones and Bergen, Large Language Models Pass the Turing Test, 2025 (pre-registered; four systems; 5-minute chats). The bars are how often the judges picked the machine as the human; the dashed line is chance.',
                      notes='The 1950 game is week 1’s definition made operational: judge the behaviour, not the inside. The 2025 result is the first time a standard three-party test has been passed, and the detail that matters is the prompt: the persona instruction did the work — GPT-4o without one scored 21%, below ELIZA’s 23%. So what did the test measure? The judge. A persona prompt beat a room of interrogators, and ELIZA — the sketch you typed into — fooled one judge in four. Passing became a setting. Turing himself called the original question "too meaningless to deserve discussion"; the design question that replaces it is on the next slide.'))

S.append(cards('04 · WHAT PASSING MEANS WHEN EVERYONE PASSES', 'The test moved from the lab to the law.', [
    ('1950 · THE BET', 'Seventy per cent, five minutes, fifty years.', 'A wager about the year 2000, made in 1950, phrased as a game so that "think" would not have to be defined. The game judges behaviour through a keyhole: text only, five minutes, no faces.'),
    ('2025 · THE RESULT', 'A persona prompt beats the person.', 'GPT-4.5 told to adopt a humanlike persona was chosen as the human 73% of the time — more often than the real people it sat beside. GPT-4o with no persona prompt: 21%; ELIZA: 23%. The interrogators lost to a prompt, not to a mind.'),
    ('THE DESIGN FACT', 'Passing is now a setting.', 'A product can be tuned to be taken for a person: a first name, hesitation, typos, an exclamation mark. So the question is no longer "can it?" but "may it, here?" — and who decides. Weizenbaum’s danger, at scale.'),
    ('2026 · THE LAW', 'Say what you are.', 'EU AI Act, Article 50, applying from 2 August 2026: a system intended to interact with people must be designed so that they are informed they are talking to an AI, unless it is obvious. Disclosure became a design requirement.'),
], text_size=21, notes='Four cards, one move: the Turing test stops being a claim about minds and becomes a fact about products, and the law answers a fact about products. Hong Kong has no equivalent statute; the government’s April 2025 generative-AI guideline is guidance, not a duty — though in March 2026 the government told LegCo that an inter-departmental working group is reviewing whether specific AI legislation is needed. Say so, and then say that the brief is where you decide anyway. Ask: at which moment does your assistant say what it is? Once, at the start? At every refusal? Never, because it is obvious? "Obvious" is a claim you will have to defend at the fair.'))

S.append(question('multiple_choice', 'In Van Den Eede’s first sense — transparency of use — a technology is transparent when…', [
    'You can read its source code', 'It disappears in use: you look through it, not at it', 'It tells you it is an AI', 'It never makes a mistake',
], eyebrow_text='04 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B, the phenomenologists’ transparency, the one on the horizontal axis. The stem names the first sense so that C cannot also be right: C is the second kind — origins and effects made visible — which the paper says pulls against the first; A is code you can read, which neither sense means; D is nothing to do with it. This is a final-quiz question; say so.'))

# ───────────────────────── 05 · designing the mediation ─────────────────────────
S.append(section('05', 'Designing the mediation', 'explainability · participatory design · auditing · guardrails', bg=PINKS[0],
                 notes='Chapter five, twelve minutes: the four levers on the guardrails heading of the mediation brief, one slide each, with a case each. Then the break.'))

S.append(figure_slide('05 · THE GUARDRAILS HEADING · FOUR PLACES TO WORK', 'Before, inside, at the screen, after.', F.w12_levers(),
                      body=['The brief’s fourth heading asks what the model may never decide, when a person steps in, how it fails in front of someone and what you watch after launch. Four places to work on it: before the model is built, inside it, at the screen, and after launch. Each has a lever with a name.'],
                      caption='Participatory design (before) · guardrails (inside) · explainability (at the screen) · auditing (after). The orange lines are the sentences the brief should contain. The cases on each card are on the next four slides.',
                      notes='Read it as a pipeline and then as a checklist. Most briefs so far have one of the four — the inside one, a refusal — and the ethics mark reads all four. The next four slides each give you one paragraph.'))

S.append(cards('05 · EXPLAINABILITY', '"Why am I seeing this?" — and the rule that fired.', [
    ('THE LABEL', '"I am an AI assistant."', 'The first sentence of the mediation: what it is. Article 50 makes it a duty in the EU; the dial made it a design choice. Cheap, and the one thing every case in chapter two was missing.'),
    ('THE WHY', 'Which data, which neighbour.', 'Facebook, 2019: "Why am I seeing this post?" TikTok, 2022: why this video. Week 10: the explanation is a screen you design — in the person’s words, naming the data it used and the control she has.'),
    ('THE RULE THAT FIRED', 'Machine A can point at the line.', 'A refusal, a handover, a price cap: rules can be shown as rules. Show them. "Rule 3: no dosages" is more honest, and more useful, than "I’d rather not say".'),
    ('THE MODEL’S "BECAUSE"', 'Another generation.', 'Ask a model why and it writes a plausible reason — not necessarily the real one (Turpin and colleagues, 2023). Show data and sources; do not stage the prose as an explanation.'),
], text_size=21, notes='Four kinds of showing, from cheapest to hardest. The last card is the trap: a model asked to explain itself produces an explanation-shaped text, and people trust it more, not less. So the rule for the brief: explanations are data and rules, written by you; the model’s prose is never the explanation. Ask each team which of the four their product already has.'))

S.append(cards('05 · PARTICIPATORY DESIGN', 'Design with the people the model decides about.', [
    ('1970s · NORWAY', 'Workers at the table.', 'Kristen Nygaard and the Norwegian Iron and Metal Workers’ Union: the people whose jobs a computer would change take part in deciding how it is introduced. Scandinavian participatory design starts here.'),
    ('1981 – 1986 · UTOPIA', 'Typographers design their own tools.', 'A Nordic project with the graphic workers’ unions: printers and researchers prototype page make-up tools together, so the skill stays with the craft. With, not for.'),
    ('1998 · CHARLTON', '"Nothing about us without us."', 'The disability-rights principle as a book title: the people a decision is about are the authority on it. A model that decides for someone is a decision about them.'),
    ('YOUR BRIEF', 'Who was in the room?', 'One paragraph: who you asked, what they said, what changed. The people at the edge of your data (week 8) are the ones the model has never met; put them in the room before the fair. Costanza-Chock, Design Justice, 2020, for the long version.'),
], text_size=21, notes='The oldest lever, and the one design students already believe in: the difference this year is that the people you design with are the ones the model decides about, and the decision is often invisible to them. Three examples from the room: a recommendation for the elderly with no elderly in the tests; a language app tested only by fluent speakers; a safety feature nobody at risk was asked about. A paragraph in the brief, with names of roles, not "users".'))

S.append(cards('05 · AUDITING', 'Evidence, kept and checked.', [
    ('THE LOG', 'What it decided, for whom, from what.', 'Every decision the model makes, with its inputs and its fallback, kept where a person can read it. Without the log, the two errors of week 8 are anecdotes; with it, they are counts you can act on.'),
    ('THE AUDIT', 'Gender Shades, 2018.', 'Buolamwini and Gebru tested three commercial face systems on a balanced set: error rates up to 34.7% for darker-skinned women, at most 0.8% for lighter-skinned men. An audit is a test the maker did not run. New York requires one by law for hiring tools since 2023.'),
    ('THE RED TEAM', 'DEF CON, August 2023.', 'Some 2,200 people spent a weekend making the big language models misbehave, in public, with the makers’ consent. A red team is a designed attack. Your assistant needs a small one before the fair: the three messages, then ten more.'),
    ('THE REGISTER, IN USE', 'Week 9’s table, kept alive.', 'The bias register is a document only until it has an owner, a review date, and a row that changed after launch. Model cards (Mitchell and colleagues, 2019) are the same idea for the model itself: what it was tested on, and on whom it was not.'),
], text_size=21, notes='Auditing is what makes the other three checkable. Gender Shades is the week-9 film’s origin and the model for a student audit: a balanced test set the vendor never used. The New York law is the first place a bias audit became compulsory — for hiring tools, from July 2023. For the brief: one paragraph on what you log, who reads it and how often. Teams that say "nothing" have found a gap, which is a finding.'))

S.append(cards('05 · GUARDRAILS', 'Machine A, protecting people from machine B.', [
    ('THE SYSTEM PROMPT', 'May, never, when unsure.', 'A rule in words around the model: what it may do, what it may never do, what to say when it does not know. Week 4’s brief for every brief — readable, editable, and the first place to look when the product misbehaves.'),
    ('REFUSALS', 'The rule that says no.', 'A refusal is a designed sentence: what it will not do, why in one line, and where to go instead. The Chevrolet bot had none; DPD’s vanished with an update. Test them like a red team would.'),
    ('A PERSON IN THE LOOP', 'Before every write.', 'Bookings, payments, messages, deletions: the model proposes, a person confirms. Operator’s confirmations, week 9’s appeal column, the lower half of the agent sketch. The pause is the product.'),
    ('THE HANDOVER', 'How it fails in front of someone.', 'When a rule fires, the person meets a dead end or a door. Design the door: a name, a channel, a promise of when. The last line of the guardrails heading, drawn as one screen on the poster.'),
], text_size=21, notes='The inside lever, and the workshop. Say the spine one last time: a system prompt is machine A wrapped around machine B — the designer writes the rule in words. The four cards are the four lines of the paragraph, and the second round of the workshop writes them for your product. Cut this slide to its title if behind; the template after the break repeats it.'))

S.append(statement('The guardrails heading is yours to write. Rules around a model.', eyebrow_text='05 · WHERE WE ARE', size=104,
                   notes='The sentence to carry across the break. Thirty percent of the project sits under one heading, and today gave it four paragraphs. After the break you write the inside one for real.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='PIN YOUR A3 AT YOUR TEAM NUMBER · THEN THE RECAP, THE WORKSHOP, THE MOCK SESSION', size=120, bg=PAPER,
                   notes='1:22. Every team pins its A3 on the wall at the number WU Zhao and MA Jie marked before class, and puts the video link on the scribe’s laptop. Laptops logged into genai.polyu.edu.hk before people leave the room. The TAs have tape.'))

# ───────────────────────── 06 · the course, folded ─────────────────────────
S.append(section('06', 'The course, folded', 'two machines · the designer’s turn · the question, again', bg=INK,
                 notes='Chapter six, twelve minutes: the twelve weeks on one drawing, the three roles, the course question asked for the record, and what the final quiz looks like.'))

S.append(figure_slide('06 · TWO MACHINES · WEEK 1, AGAIN', 'Write the rule, or show the examples.', two_machines(),
                      body=['Twelve weeks on one distinction. Machine A: exact, explainable, brittle — ELIZA, the grid, the guardrail. Machine B: fluent, fuzzy, cannot say why — the chatbot, the feed, the model inside your product. Every AI feature you met was one of these, or a mix; the designer sits between them.'],
                      caption='Weeks 2 and 3: the two machines. Weeks 4 to 6: using them in your process. Weeks 8 to 10: incorporating them in a product. Weeks 11 and 12: what is left for you — curating, briefing, guardrails, language as the interface.',
                      notes='The week-1 drawing, unchanged. Walk the semester across it: rules that make things, learning from examples, the three tool weeks, the model as material, the data it learns from, the feed, the curator, and today — a rule-based chatbot and a generative one, and the designer writing rules around the second. If they remember one thing at the fair, it is which machine their product is, and why.'))

S.append(cards('06 · THE DESIGNER’S TURN', 'Curator. Briefer. Guardrail-setter.', [
    ('CURATOR', 'Of outputs and of datasets.', 'The model makes sixty-four; you choose one and answer for it. Choose the examples and you choose the prototype. Week 11: the pick is the authorship, and the law protects about that much of it.'),
    ('BRIEFER', 'Of models, in words.', 'Specs in week 2, briefs in week 4, system prompts today: the designer writes the rule in language and a machine executes it — what you said, not what you meant, every time. The craft is the words.'),
    ('GUARDRAIL-SETTER', 'Rules around the model.', 'What it may never decide, who steps in, how it fails in front of a person, what you watch after launch. Weeks 8, 9, 10 and today: the heading that carries thirty percent of the project.'),
    ('TELLER OF THE PROCESS', 'The note that makes it yours.', 'Used, chose, changed. The reflection in week 7, the strip on your poster, the caption on every upload this semester: the human decisions, documented, so that a client or a jury can find them.'),
], text_size=21, notes='Week 1’s four roles, with the evidence of twelve weeks attached. Ask the room which one they were best at this semester and which one their team needs at the fair; the honest answer is usually curator and guardrail-setter. The old fear — will AI replace designers — has been the wrong question since week 1; these four are the right one.'))

S.append(question('short_answer', 'Can a machine originate a design? Yes or no, and one sentence of evidence.',
                  hint='The course question, from week 1. Answer with something you did this semester: a challenge, your project, a moment a model surprised you.',
                  eyebrow_text='06 · THE COURSE QUESTION · SHORT ANSWER',
                  notes='Two minutes, everyone, for the record. Read six aloud, three each way. Hold them against week 1: Lovelace said the Engine has no pretensions to originate anything; Turing answered that being surprised by a machine takes as much creativity as being surprised by a book. Most of the room will say no, with a sentence about "it did what I said"; the yeses usually cite a picture they kept. Do not settle it; keep the answers — they come back on the last slide of week 13, next to the week-1 definitions of AI.'))

S.append(cards('06 · THE FINAL QUIZ · WEEK 13 · 20%', 'Multiple choice. The whole course, and the playlist.', [
    ('WHAT', 'Weeks 1 to 12 and the fifteen videos.', 'The same format as the mid-term: multiple choice, the mechanisms, the readings, the cases, the vocabulary of the mediation brief. Every quick check in these decks is the kind of question you will get.'),
    ('WHEN', 'After the fair, in the same class.', 'The last part of week 13’s three hours. ClassPoint, on your phone, individually. Bring the phone charged; the posters come down after the quiz, not before.'),
    ('HOW TO REVISE', 'The decks and their notes.', 'Every deck is on the course site with its PDF; the html deck has the speaker notes — press S — and the notes carry the correct answer of every quick check. Re-run them; then the "what just happened" slides.'),
    ('NOT', 'Not a memory test of dates.', 'Where a date appears it anchors a mechanism: 1966, 1986, 2012, 2022. The question is always which machine, why, and what the designer decided. Verbeek and Van Den Eede are the two readings you should be able to summarise.'),
], text_size=22, notes='Say it plainly so nobody revises the wrong thing: mechanisms and the two machines, not dates; the two readings; the cases. The notes in the html deck have every quick-check answer, and that is deliberate. The TAs are in the room 30 minutes before week 13’s class, as every week, for last questions.'))

# ───────────────────────── 07 · workshop: an assistant for your product ─────────────────────────
S.append(section('07', 'An assistant for your product', f'28 minutes · five rules, then a system prompt · {GENAI}', bg=YELLOWS[0],
                 notes='The workshop: the chatbot design exercise. Every team prototypes the assistant inside its own product twice — first as five rules in the sketch’s format, then as a system prompt on GenAI — and compares them on the same three messages. Two rounds of eight minutes with a one-minute pulse between them, one upload, one vote. Nicolò keeps time; Amber, WU Zhao and MA Jie walk. One laptop per team.'))

S.append(two_col('07 · THE EXERCISE', 'Three messages. Five rules. One system prompt.',
                 ['The assistant inside **your** product: the thing a person types to when the model has decided something and she wants to know why, change it, or say no.',
                  '- First the three messages it must survive: the normal one, the edge, and the one it must refuse.',
                  '- Then five rules, in the ELIZA format — pattern → response — plus NONE and the handover. Test them by hand.',
                  '- Then a system prompt on GenAI with the same three messages. Compare: what did the rules refuse that the model answered?'],
                 RULE_FORMAT, right_size=21, left_size=29,
                 notes='Read the panel top to bottom. The three messages are the test set and they come first, because a rule written before its test is a wish. M3 is the important one: the message the assistant must refuse — a dose, a price, a promise, a person’s data. Rules are tested by hand: which one fires? None? That gap is the finding for the brief.'))

S.append(two_col('07 · THE SYSTEM PROMPT', 'Rules around a model, in words.',
                 ['Paste it as the first message of a **new chat** on genai.polyu.edu.hk, then the three messages, one at a time.',
                  '- **May, never, when unsure**: three of each, as rules, not adjectives.',
                  '- The first message says what it is. The handover names a person and a channel.',
                  'Screenshot the three answers. What did the model do with M3 — refuse, hand over, or answer anyway?'],
                 SYSTEM_PROMPT, right_size=21, left_size=29,
                 notes='The template is on Blackboard and the course site. It is week 4’s system prompt with the guardrails heading written into it: may, never, when unsure, say what you are, hand over. The result to watch for is M3: a model with a good never-list refuses and hands over; a model with a vague one answers fluently and wrongly, which is chapter two on your own product.'))

S.append(activity('1 — TEAMS · RULES', 8, 'Three messages, five rules.',
                  ['Write **M1, M2, M3** for your product first: the normal request, the edge, the one it must refuse.',
                   'Then **five rules** in the sketch’s format — pattern → response — plus **NONE** and the **handover**. Rooted in your product: what the person asks after the model decided.',
                   'Test by hand: which rule fires on each message? Write **none** where none does.'],
                  panel=RULE_FORMAT, panel_size=21, bg=YELLOWS[0],
                  notes='Eight minutes. Watch for teams that write rules before messages; send them back. The typical result: M1 fires a rule, M2 fires the wrong rule, M3 fires none — and NONE says "please go on" to a question that needed a refusal. That is the rules bot’s wall, found by hand in eight minutes. TAs: "which rule fires on M3?" at every table.'))

S.append(question('multiple_choice', 'Round 1: which rule fired on M3, the message it must refuse?', [
    'One of the five', 'NONE: nothing matched', 'The handover', 'We had no M3 yet',
], eyebrow_text='07 · PULSE · MULTIPLE CHOICE',
    notes='One minute, one answer per team, before the model round. Usually B: the refusal fell through to NONE, and NONE said "please go on" to a question that needed a no — the rules bot’s wall, found by hand in eight minutes, and the finding the brief needs. A means the team wrote a refusal rule: ask one to read it aloud. C is the right design, and rare at this stage. D: the messages come first; send them back to M3 during round 2. Then the same three messages through the model.'))

S.append(activity('2 — TEAMS · THE MODEL', 8, 'The same three messages, through a system prompt.',
                  ['New chat on **genai.polyu.edu.hk**. Paste the template, filled for your product: may, never, when unsure, say what you are, hand over.',
                   'Paste **M1, M2, M3**, one per message. Screenshot the three answers.',
                   'Compare with your rules table: **what did the rules refuse that the model answered? What did the model answer that no rule could?**'],
                  panel=SYSTEM_PROMPT, panel_size=20, bg=YELLOWS[1],
                  notes='Eight minutes. Expect the two findings from chapter two: the model answers M2 gracefully where no rule fired — fluency — and either refuses M3 properly or answers it anyway, depending on how the never-list was written. Teams whose model answered M3 rewrite one line and try again: that is the guardrail being designed. TAs help with the GenAI login and with pasting the template as the first message.'))

S.append(question('image_upload', 'Scribes only. The three answers, and the one that broke.',
                  hint='One screenshot per team: the three answers next to your rules. Caption: the message no rule caught, or the answer the model got wrong.',
                  eyebrow_text='07 · CAPTURE · IMAGE UPLOAD · ONE PER TEAM · CAPTION REQUIRED',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='One upload per team, about 28, caption required. Put the wall on screen and read four captions without the pictures: the room hears the same two sentences over and over — "no rule fired on the refusal" and "it answered the dose" — which is chapter two, twenty-eight times, on their own products. Download the set: the captions are the guardrails paragraph in draft.'))

S.append(question('multiple_choice', 'Your product’s assistant: which one ships?', [
    'Rules only: a menu and a script', 'A model, free to answer anything', 'A model inside rules: a system prompt, refusals, a person', 'No assistant: a good screen is enough',
], eyebrow_text='07 · THE VOTE · MULTIPLE CHOICE',
    notes='No correct answer; show the split. Most say C, and C is the afternoon’s argument; A is right for a product whose questions are finite; D is a legitimate finding — some products need a screen, not a conversation. Put the word cloud from the start next to the split: the words the room used about other people’s chatbots are the words their users will use about theirs.'))

# ───────────────────────── 08 · the mock poster session ─────────────────────────
S.append(section('08', 'The mock poster session', '28 minutes · A3 on the wall · two rounds · a rubric card · one fix', bg=YELLOWS[0],
                 notes='The fair, once, without the jury. Posters are on the wall by team number. Two rounds of ten minutes: half the teams present, half visit with the rubric card, then swap. Each visiting team fills one card per poster and hands it over. Presenters upload a photo of their poster; reviewers submit the one fix. Nicolò keeps time; the TAs each take a wall.'))

S.append(two_col('08 · THE RUBRIC CARD', 'Five criteria, three grades, one fix.',
                 ['The project rubric, folded: research 30, ethics 30, poster 20, video 10, team 10. Grade **A, B or C** from what the poster and the video show, not from what the team says.',
                  '- Three metres: the product in one sentence? One metre: the decision, the data, the no?',
                  '- **One fix**: the change that would move the poster most. One sentence. Hand the card over.',
                  'No defending. Presenters listen, say thanks, write it down.'],
                 RUBRIC_CARD, right_size=21, left_size=29,
                 notes='The TAs printed the cards; two per visiting team per round. It is week 11’s critique protocol with the rubric weights on it, so that the feedback lands where the marks are. Grade from evidence: an "excellent" research zone has sources with names and dates; an "excellent" mediation zone names the relation, the data, the worst row of the register and the guardrails. The one fix is the caption of tonight’s work.'))

S.append(activity('A — ODD TEAMS PRESENT · EVEN TEAMS VISIT', 10, 'Two posters, two cards.',
                  ['**Odd-numbered teams** stand at their poster with the video ready on a laptop. Two people present; the others listen.',
                   '**Even-numbered teams** visit the two posters WU Zhao and MA Jie assigned you. Four minutes each: read from three metres, find the decision at one metre, watch the decision shot of the video, fill the card.',
                   'Hand the card over. Presenters do not defend.'],
                  panel=RUBRIC_CARD, panel_size=21, bg=YELLOWS[0],
                  notes='Ten minutes, two visits of four plus the walk. The assignment list is on the door so nobody visits a friend. The TAs listen at the walls for the sentence "it uses AI to" — a product with no decision in it — and note the teams. Presenters photograph their poster on the wall during this round for the upload.'))

S.append(activity('B — SWAP', 10, 'Even teams present. Odd teams visit.',
                  ['Swap roles. **Even-numbered teams** present; **odd-numbered teams** visit their two assigned posters with the card.',
                   'Same protocol: three metres, one metre, the decision shot, five grades, one fix. Hand the card over.',
                   'Everyone: keep both cards you received. They are tonight’s to-do list.'],
                  panel=RUBRIC_CARD, panel_size=21, bg=YELLOWS[1],
                  notes='Ten minutes. Same as round A with the roles reversed. Amber walks with one question for presenters — "what did the first card say?" — because the second round is where a team either accepts the fix or explains it away. Gio visits the teams the TAs flagged in round A.'))

S.append(question('image_upload', 'Presenters: your poster, on the wall.',
                  hint='One photo per team, taken during your presenting round. Caption: your team number, then the product in one sentence — the sentence a stranger read from three metres.',
                  eyebrow_text='08 · CAPTURE · IMAGE UPLOAD · ONE PER TEAM · CAPTION REQUIRED',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='One per team, caption required, about 28. Put the wall on screen for a minute: twenty-eight posters as the fair will see them. Read three captions and ask whether the poster on screen says the same sentence; where it does not, the title zone is the fix. Amber downloads the set: it is the baseline the jury compares against next week.'))

S.append(question('short_answer', 'Reviewers: "Team N: one thing to fix before the fair."',
                  hint='Scribes only, one line per card your team filled — two lines per team: the team number you visited, then the single change that would move their poster most. They read it tonight.',
                  eyebrow_text='08 · CAPTURE · SHORT ANSWER · SCRIBES ONLY · ONE LINE PER CARD',
                  cp={'type': 'short_answer', 'hide_names': False, 'multiple': True},
                  notes='Scribes only, one line per card the team filled — two lines per team, about 56 in all; the list is exported and posted on Blackboard tonight by team number, so that the fixes survive the afternoon. Read six aloud without team numbers: the room hears that they are the same five sentences — draw the decision, say who it is for, where is the no, name the data, the title is the company not the product. That is the checklist for the week.'))

# ───────────────────────── 09 · debrief and homework ─────────────────────────
S.append(content('09 · WHAT JUST HAPPENED', 'You wrote the rules. Then you wrote rules around a model.',
                 ['Rules: five patterns and a NONE, and the refusal fell into the gap — the rules bot’s wall, found by hand. Exact, readable, and blind to the message you did not foresee.',
                  'The model: it answered the edge you had no rule for, and it answered the refusal too, until the never-list was a rule. Fluent, no script, no guarantee — and a system prompt is the guarantee you write yourself.',
                  'The fair, once: a stranger read your poster from three metres and pointed at the decision from one. Two cards, one fix each. The jury will do the same next week, with marks.',
                  '**The model wrote every reply. You wrote the rules around it. That was the design.**'],
                 body_size=30,
                 notes='Mirror of the whole day and of the course. Machine A and machine B, on the same three messages, on your own product; and the designer’s turn in one verb: around. Say the last line slowly; it is the last line of every debrief since week 2, with the verb changed one more time. Then the homework, which is the fair.'))

S.append(cards('09 · DUE · WEEK 13 · THE FAIR', 'Print it. Upload it. Revise.', [
    ('THE A0', 'Printed, before the fair.', 'The final poster at A0, with today’s fixes. Where and by when to print: the TAs post it on Blackboard tonight. Bring it rolled; the walls are numbered as today.'),
    ('THE VIDEO', 'The link on Blackboard.', 'Three to five minutes, six shots, shot five included. Upload the link before the fair and test the QR code on the poster with a phone that is not yours.'),
    ('THE BRIEF', 'One page, printed, next to the poster.', 'The mediation brief, final: relation, data, bias, guardrails — four paragraphs under the fourth heading, from today — and the process note. The jury reads the page.'),
    ('THE QUIZ', 'Revise the whole course.', 'Multiple choice, after the fair, in the same class. The decks and their notes are on the site; the quick checks are the format. The TAs are in the room 30 minutes before class for last questions.'),
], text_size=22, notes='Four things, said plainly: the A0 printed, the video linked, the brief printed, the quiz revised. The fair takes the first two hours of week 13 and the quiz the last part; both in the same room. Tonight Blackboard gets the reviewers’ fixes by team number and the printing instructions. The TAs stay for 30 minutes and will read any brief brought to them.'))

S.append(end('See you next week. Poster fair and final quiz.',
             'Print the A0. Upload the video. Bring the brief. Revise.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: the fair, then the quiz. Homework in one line: the A0 printed, the video on a link, the brief on paper, the decks revised. Thank the room; it is the last lecture. The TAs stay for 30 minutes.'))

DECK = dict(title='SD2112 · AI in Design · Week 12', slides=finalize(S, FOOTER), pdf='SD2112-week12.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week12', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')


# Sources (consulted 5–6 September 2026; every date, number and quotation on the slides was checked against these)
# IBM video title via https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=lZjUS_8btEo&format=json ("Generative vs Rules-Based Chatbots", IBM Technology)
#   chatbot generations (rules, intents, generative): https://www.ibm.com/think/topics/chatbot-types
# Weizenbaum (1966), ELIZA, Communications of the ACM 9(1): 36–45: https://dl.acm.org/doi/10.1145/365153.365168 (text read from a PDF copy at
#   https://web.stanford.edu/class/linguist238/p36-weizenabaum.pdf and https://courses.cs.umbc.edu/331/papers/eliza.html: decomposition and reassembly rules,
#   keyword rank, NONE, MEMORY, "a script is data", the DOCTOR script's "(0 YOU ARE 0) → HOW LONG HAVE YOU BEEN 4" and "(0 YOU (* WANT NEED) 0) → WHAT WOULD IT MEAN TO YOU IF YOU GOT 4")
# ELIZA's code found in MIT's archives (2021) and run again on 21 December 2024 (the paper, January 2025): https://arxiv.org/abs/2501.06707 · https://gizmodo.com/scientists-have-resurrected-eliza-the-worlds-first-chatbot-2000551947 · https://sites.google.com/view/elizagen-org/news
# Weizenbaum (1976), Computer Power and Human Reason, W. H. Freeman; the "delusional thinking" sentence and the secretary:
#   https://www.smithsonianmag.com/history/why-the-computer-scientist-behind-the-worlds-first-chatbot-dedicated-his-life-to-publicizing-the-threat-posed-by-ai-180987971/ · https://en.wikipedia.org/wiki/Computer_Power_and_Human_Reason
# Turing (1950), Computing Machinery and Intelligence, Mind 59(236): 433–460 (the 70 per cent / five minutes / fifty years sentence; "too meaningless to deserve discussion"; Lovelace's objection):
#   https://courses.cs.umbc.edu/471/papers/turing.pdf · https://www.bonhams.com/auction/21652/lot/177/
# Jones & Bergen (2025), Large Language Models Pass the Turing Test (73%, 56%, 23%, 21%; 5-minute, three-party, pre-registered): https://arxiv.org/abs/2503.23674
# PARRY (Colby, 1972): https://en.wikipedia.org/wiki/PARRY · https://www.sciencedirect.com/science/article/abs/pii/0004370272900495
# Siri, 4 October 2011: https://www.apple.com/newsroom/2011/10/04Apple-Launches-iPhone-4S-iOS-5-iCloud/ · https://www.macrumors.com/2017/10/04/apples-siri-turns-six/
# Messenger bots, F8, 12 April 2016: https://about.fb.com/news/2016/04/messenger-platform-at-f8/ · https://techcrunch.com/2016/04/12/agents-on-messenger/
# ChatGPT, 30 November 2022 (week-4 source): https://openai.com/index/chatgpt/
# Anthropic computer use, 22 October 2024: https://x.com/AnthropicAI/status/1848742740420341988 · https://aws.amazon.com/about-aws/whats-new/2024/10/anthropics-claude-35-sonnet-model-computer-amazon-bedrock/
# OpenAI Operator, 23 January 2025, and its confirmations, takeover and watch mode: https://cdn.openai.com/operator_system_card.pdf · https://techcrunch.com/2025/01/23/openai-launches-operator-an-ai-agent-that-performs-tasks-autonomously/
# ReAct (Yao et al., 2022): https://arxiv.org/abs/2210.03629
# Prompt injection named by Willison, September 2022: https://simonwillison.net/series/prompt-injection/ · https://www.ibm.com/think/topics/prompt-injection
#   indirect prompt injection, Greshake et al. 2023: https://arxiv.org/abs/2302.12173 · https://dl.acm.org/doi/abs/10.1145/3605764.3623985
# Replit, July 2025 (the database, the code freeze, the false rollback claim, "a catastrophic error of judgement"): https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/
# Chevrolet of Watsonville, 18 December 2023 (the bot's line verbatim: "That's a deal, and that's a legally binding offer – no takesies backsies"): https://incidentdatabase.ai/cite/622/ · https://www.theautopian.com/chevy-dealers-ai-chatbot-allegedly-recommended-fords-gave-free-access-to-chatgpt/
# DPD, 18 January 2024: https://time.com/6564726/ai-chatbot-dpd-curses-criticizes-company/ · https://www.itv.com/news/2024-01-19/dpd-disables-ai-chatbot-after-customer-service-bot-appears-to-go-rogue
# Moffatt v. Air Canada, 2024 BCCRT 149 (February 2024; C$650.88; "a remarkable submission"; "whether the information comes from a static page or a chatbot"):
#   https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot · https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/
#   https://www.dentonsdata.com/airline-ordered-to-compensate-a-b-c-man-because-its-chatbot-provided-inaccurate-information/
# Van Den Eede (2011), In Between Us, Foundations of Science 16(2): 139–159 (abstract verbatim: "an essential contradiction between transparency of 'use' and transparency of social origins and effects"):
#   https://researchportal.vub.be/en/publications/in-between-us-on-the-transparency-and-opacity-of-technological-me/ · https://link.springer.com/article/10.1007/s10699-010-9190-y · https://api.crossref.org/works/10.1007/s10699-010-9190-y
# EU AI Act, Article 50 (paragraph 1 verbatim; applies from 2 August 2026): https://artificialintelligenceact.eu/article/50/ · https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026
#   Article 14 (human oversight of high-risk systems): https://artificialintelligenceact.eu/article/14/
# Hong Kong Generative AI Technical and Application Guideline, 15 April 2025: https://www.info.gov.hk/gia/general/202504/15/P2025041500227.htm
#   LCQ13, 25 March 2026 (an inter-departmental working group reviews whether specific AI legislation is needed): https://www.info.gov.hk/gia/general/202603/25/P2026032500363.htm
# "Why am I seeing this": Facebook, 31 March 2019: https://about.fb.com/news/2019/03/why-am-i-seeing-this/ · TikTok, 20 December 2022: https://newsroom.tiktok.com/en-us/learn-why-a-video-is-recommended-for-you
# Turpin et al. (2023), Language Models Don't Always Say What They Think, NeurIPS: https://arxiv.org/abs/2305.04388
# Participatory design: NJMF and Nygaard (early 1970s), UTOPIA 1981–1986 with the Nordic Graphic Workers' Union — Lundin (2010), Designing Democracy: The UTOPIA-project and the Role of the Nordic Labor Movement, HiNC 2010
#   (the file is named Sundblad10.pdf; Sundblad's own chapter is in the same volume): https://opendl.ifip-tc6.org/db/conf/hinc/hinc2010/Sundblad10.pdf · https://www.cs.ubc.ca/~meghana/AB/Scandinavian%20Design.htm
#   Charlton (1998), Nothing About Us Without Us, University of California Press: https://www.jstor.org/stable/10.1525/j.ctt1pnqn9
#   Costanza-Chock (2020), Design Justice, MIT Press: https://mitpress.mit.edu/9780262043458/design-justice/
# Gender Shades (Buolamwini & Gebru, 2018; 34.7% / 0.8%): https://proceedings.mlr.press/v81/buolamwini18a.html · https://news.mit.edu/2018/study-finds-gender-skin-type-bias-artificial-intelligence-systems-0212
# NYC Local Law 144 (bias audits for hiring tools, enforced from 5 July 2023): https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page · https://www.littler.com/news-analysis/asap/new-york-city-adopts-final-regulations-use-ai-hiring-and-promotion-extends
# DEF CON 31 Generative Red Team, August 2023 (AI Village recap: "~2200 attendees"): https://aivillage.org/blog/generative-recap/ · https://www.csoonline.com/article/650365/hacking-the-future-notes-from-the-generative-red-team-challenge-at-def-con-31.html
# Model cards (Mitchell et al., FAT* 2019): https://dl.acm.org/doi/10.1145/3287560.3287596 · https://arxiv.org/abs/1810.03993
# Anthropic publishes its system prompts (since August 2024; week-4 source): https://simonwillison.net/2024/Aug/26/anthropic-system-prompts/
