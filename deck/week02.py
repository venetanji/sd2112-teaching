"""
SD2112 · Artificial Intelligence in Design · Week 02 — the slide spec.

    deckgen build                    # everything, as the GitHub Actions workflows run it (the generator is ait4x/deckgen)
    deckgen build --pptx             # export/ only, no node needed
    python deck/week02.py --html     # only the html deck of this week

Rules that make things: machine A (symbolic AI), instructions as art, Stuttgart 1965,
rules that grow (Koch, Lindenmayer, parameters), p5.js, prompts for coding (spec → model →
code → picture), and the one exercise: a spec, a model, a twist, and iterations. Every p5.js
sketch on a slide has a Python twin in deck/figures.py that draws the same rule (what the
pptx and the PDF show); the html deck runs the sketches live, and the code slides are
editable there: change a number, press Run, see the picture change.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import figures as F                                   # noqa: E402
from deckgen import attach_reports, activity_url, build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from deckgen.layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full,   # noqa: E402
                             journey, activity, video, two_col, figure_slide, code_slide, sketch_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, JOURNEY  # noqa: E402

FOOTER = 'SD2112 · AI IN DESIGN · WEEK 02'
HERE = Path(__file__).resolve().parent


def _week1_answers(question):
    """The public page of a week-1 activity, from deck/week01-reports.json (written after the class by
    classpoint.py's weekly runner), or None: the file is not there yet, or the activity was withheld — an
    activity the room was told was anonymous gets no public link, because the page's payload carries
    the names (deckgen.reports). Give the entry its id and the slide links on the next build."""
    p = HERE / 'week01-reports.json'
    if not p.exists():
        return None
    for e in json.loads(p.read_text(encoding='utf-8')):
        if e.get('question') == question and e.get('activity'):
            return activity_url(e['activity'])
    return None


WORRIES_URL = _week1_answers('One hope and one worry.')
CUPS_URL = _week1_answers('Everyone: upload your first cup.')

# ───────────────────────── the code on the slides (p5.js) ─────────────────────────
# Editable in the html deck (deckgen: a code_slide with a sketch): what the students see is
# what runs. `extra` is appended only in the sketch page, for interaction the panel does not
# show. createSlider's fifth argument is a label the sketch page shows; the p5 editor ignores it.

TEN_CODE = """let pts = [];                        // the points
function setup() {
  createCanvas(600, 600);
  noLoop();                          // draw once
  roll();
}
function roll() {                    // the rule: ten points
  pts = [];
  for (let i = 0; i < 10; i++) {
    pts.push([random(600), random(600)]);    // chance
  }
}
function draw() {
  background(255); stroke(0);
  for (let a of pts) {               // every pair
    for (let b of pts) {
      line(a[0], a[1], b[0], b[1]);
    }
  }
  fill(0); for (let p of pts) circle(p[0], p[1], 6);
}"""

TEN_EXTRA = """function mousePressed() { roll(); redraw(); }   // new dice, the same rule (as edited)"""

SCHOTTER_CODE = """const cols = 12, rows = 22, s = 30;  // Nees's numbers
let disorder, seed = 1968;           // the one number: a slider
function setup() {
  createCanvas(400, 700); noLoop();
  disorder = createSlider(0, 2, 1, 0.05, 'disorder');
}
function draw() {
  background(255); noFill(); stroke(0);
  randomSeed(seed);                  // the same dice every time
  for (let r = 0; r < rows; r++) {   // rows
    let k = r / (rows - 1) * disorder.value();
    let d = k * s / 2, a = k * PI / 4;  // shift, turn
    for (let c = 0; c < cols; c++) { // columns
      push();
      translate(20 + s * (c + .5), 20 + s * (r + .5));
      translate(random(-d, d), random(-d, d)); // chance
      rotate(random(-a, a));                   // chance
      square(-s / 2, -s / 2, s);
      pop();
    }
  }
}"""

SCHOTTER_EXTRA = """function mousePressed() { seed = floor(random(1e6)); redraw(); }"""

# Schotter, drawn row by row, for the slide that explains it: the sliders are the rule's two numbers.
SCHOTTER_ROWS = """const cols = 12, s = 30;
let rows, disorder, r = 0, seed = 1968;
function setup() {
  createCanvas(400, 700); frameRate(8);
  disorder = createSlider(0, 2, 1, 0.05, 'disorder');
  rows = createSlider(2, 22, 22, 1, 'rows');
  disorder.input(restart); rows.input(restart);
  restart();
}
function draw() {
  let n = rows.value();
  if (r >= n) { if (frameCount % 48 == 0) restart(); return; }
  let k = r / (n - 1) * disorder.value();
  let d = k * s / 2, a = k * PI / 4;
  stroke(0); noFill();
  for (let c = 0; c < cols; c++) {
    push(); translate(20 + s * (c + .5), 20 + s * (r + .5));
    translate(random(-d, d), random(-d, d)); rotate(random(-a, a));
    square(-s / 2, -s / 2, s); pop();
  }
  noStroke(); fill(0); textSize(12); textFont('JetBrains Mono');
  fill(255); rect(0, 682, 400, 18); fill(0);
  text('row ' + (r + 1) + ' of ' + n + ' · shift up to ' + nf(d, 1, 1) + ' px · turn up to ' + round(degrees(a)) + '°', 20, 694);
  r++;
}
function restart() { randomSeed(seed); background(255); r = 0; }
function mousePressed() { seed = floor(random(1e6)); restart(); }"""

WALK_CODE = """const n = 30;                        // the raster: 30 x 30
let capChance;                       // a slider
function setup() {
  createCanvas(600, 600); noLoop();
  capChance = createSlider(0, 1, 0.8, 0.05, 'cap chance');
}
function draw() {
  background(255); stroke(0); strokeWeight(1.6);
  let g = width / (n + 2);
  for (let w = 0; w < n; w++) {      // column by column
    let above = false;               // was the cell above empty?
    for (let h = 0; h < n; h++) {    // top to bottom
      let x = (w + 1) * g, y = (h + 1) * g;
      let bar = random(n - 1) >= abs(w - h);  // the diagonal
      let cap = h > 0 && above && random() < capChance.value();
      if (bar) line(x, y, x, y + g);            // a bar: |
      if (cap) line(x, y, x + g, y);            // a cap: ¯
      above = !bar && !cap;          // what the cell below sees
    }
  }
}"""

WALK_EXTRA = """function mousePressed() { randomSeed(floor(random(1e6))); redraw(); }"""

# The walk, watched: the raster filling column by column, the four states and their counts, the rule
# in words. The empty cells are tinted, so the flow of the empty space shows. Not editable; the code
# slide after it is.
WALK_WATCH = """const n = 30, x0 = 40, y0 = 60, g = 16;    // the raster: 30 x 30 cells
let capChance, speed, i = 0, cells = [], counts = [0, 0, 0, 0], above = true, seed = 1966;

function setup() {
  createCanvas(1200, 600); frameRate(30);
  capChance = createSlider(0, 1, 0.8, 0.05, 'cap chance');
  speed = createSlider(1, 40, 6, 1, 'cells per frame');
  capChance.input(restart);                // a new chance: the same dice, from the top
  restart();
}

function state(j) {                        // the rule, for cell j: column by column, top to bottom
  let w = floor(j / n), h = j % n;
  if (h == 0) above = false;               // the top row: nothing above, so no cap
  let bar = random(n - 1) >= abs(w - h);   // likelier near the diagonal
  let cap = h > 0 && above && random() < capChance.value();   // only under an empty cell
  above = !bar && !cap;
  return (bar ? 1 : 0) + (cap ? 2 : 0);    // 0 empty · 1 bar · 2 cap · 3 both
}

function cell(j, k, hi) {                  // paint cell j in state k
  let w = floor(j / n), h = j % n, x = x0 + w * g, y = y0 + h * g;
  noStroke(); fill(hi ? '#FDE3D3' : k == 0 ? '#E3F1F4' : 255); rect(x, y, g, g);
  stroke(225); strokeWeight(1); noFill(); rect(x, y, g, g);
  stroke(0); strokeWeight(1.6);
  if (k & 1) line(x, y, x, y + g);
  if (k & 2) line(x, y, x + g, y);
}

function draw() {
  for (let t = 0; t < speed.value() && i < n * n; t++) {
    if (i > 0) cell(i - 1, cells[i - 1], false);
    cells[i] = state(i); counts[cells[i]]++;
    cell(i, cells[i], true); i++;
  }
  panel();
  if (i >= n * n && frameCount % 150 == 0) { seed = floor(random(1e6)); restart(); }
}

function panel() {                         // the right side: the four states, the rule, the walk
  noStroke(); fill(255); rect(600, 0, 600, 600);
  textFont('JetBrains Mono'); textSize(14); textAlign(LEFT, BASELINE);
  fill(0); text('2 · FOUR STATES · what a cell can be', 640, 60);
  let names = ['empty', 'a bar', 'a cap', 'both'];
  for (let k = 0; k < 4; k++) {
    let x = 640 + k * 110, y = 78, cur = i > 0 && cells[i - 1] == k;
    noStroke(); fill(cur ? '#FDE3D3' : k == 0 ? '#E3F1F4' : 245); rect(x, y, 64, 64);
    stroke(cur ? '#ED6D24' : 0); strokeWeight(3);
    if (k & 1) line(x, y, x, y + 64);
    if (k & 2) line(x, y, x + 64, y);
    noStroke(); fill(0); text(names[k], x, y + 86); fill(110); text('so far: ' + counts[k], x, y + 106);
  }
  fill(0); text('3 · THE RULE · the cell above decides', 640, 230);
  fill(110);
  text('a cap ¯ is drawn only under an empty cell', 640, 256);
  text('a bar | is more likely near the diagonal', 640, 278);
  text('never in the top row: there is nothing above it', 640, 300);
  fill(0); text('4 · THE WALK · column by column, top to bottom', 640, 350);
  fill(110);
  text('cell ' + i + ' of ' + (n * n) + (i >= n * n ? ' · done, new dice soon' : ''), 640, 376);
  text('empty cells are tinted: watch the empty space flow', 640, 398);
  text('from the bottom left to the top right', 640, 420);
  text('the orange cell is the one just drawn · click = new dice', 640, 442);
  text('cap chance 0: bars only · 1: a cap under every empty cell', 640, 464);
}

function mousePressed() { seed = floor(random(1e6)); restart(); }

function restart() {
  randomSeed(seed); i = 0; cells = []; counts = [0, 0, 0, 0]; above = false;
  background(255);
  stroke(225); strokeWeight(1); noFill();
  for (let j = 0; j <= n; j++) {
    line(x0 + j * g, y0, x0 + j * g, y0 + n * g);
    line(x0, y0 + j * g, x0 + n * g, y0 + j * g);
  }
  noStroke(); fill(0); textFont('JetBrains Mono'); textSize(14);
  text('1 · THE RASTER · 30 x 30', x0, y0 - 14);
}"""

TEN_PRINT = """const s = 40;                    // the cell: 40 px
let heads;                       // the coin: a slider
function setup() {
  createCanvas(800, 480); noLoop();
  heads = createSlider(0, 1, 0.5, 0.05, 'heads');
}
function draw() {
  background(255); stroke(0); strokeWeight(3);
  for (let y = 0; y < height; y += s)   // row by row
    for (let x = 0; x < width; x += s) { // cell by cell
      if (random() < heads.value())   // the coin toss
        line(x, y, x + s, y + s);     // heads: ╲
      else
        line(x + s, y, x, y + s);     // tails: ╱
    }
}"""

TEN_PRINT_EXTRA = """function mousePressed() { randomSeed(floor(random(1e6))); redraw(); }"""

YOUR_SKETCH = """// Paste the model's code over this, then press Run.
// It needs setup() and draw(); keep the seed, so the
// picture comes back the same.
function setup() {
  createCanvas(600, 600);
  background(255);
  noLoop();
}
function draw() {
  stroke(0);
  line(0, 0, width, height);   // until you paste
}"""

ELIZA_RULES = r"""// ELIZA, 1966. A rule: what to look for, what to say back.
const rules = [
  ["i am (.*)",          "How long have you been $1?"],
  ["i feel (.*)",        "Tell me more about feeling $1."],
  ["i (want|need) (.*)", "Why do you $1 $2?"],
  ["my (mother|father|family|boyfriend|girlfriend)",
                         "Tell me more about your $1."],
  ["because (.*)",       "Is that the real reason?"],
  ["(always|never|everyone|nobody)",
                         "Can you think of a specific example?"],
  ["you (.*)",           "We were discussing you, not me."],
  ["(computer|machine)", "Do computers worry you?"],
  ["(yes|no)",           "I see. Why do you say $1?"],
  ["(.*)",               "Please go on.",
                         "What does that suggest to you?"],
];
function reply(text) {           // the whole program
  let t = text.toLowerCase().replace(/[.,!?]/g, "");
  for (let [pattern, ...says] of rules) {
    let m = t.match(new RegExp(pattern));
    if (m) return pick(says)
      .replace(/\$(\d)/g, (_, i) => reflect(m[i]));
  }
}
function setup() { noCanvas(); chat(reply); }   // the screen"""

# The screen, and the two helpers the rules lean on: pick cycles through a rule's replies, reflect turns
# "my" into "your" and "i" into "you" in what is echoed back. Only in the sketch page.
ELIZA_SCREEN = r"""const SWAP = {i: "you", me: "you", my: "your", am: "are", you: "I", your: "my", are: "am", mine: "yours"};
function reflect(s) { return (s || "").split(" ").map(w => SWAP[w] || w).join(" "); }
const turn = {};
function pick(says) { let k = says[0]; turn[k] = ((turn[k] || 0) + 1) % says.length; return says[turn[k]]; }
function chat(reply) {
  let old = document.getElementById("eliza"); if (old) old.remove();
  const css = document.createElement("style");
  css.textContent = "#eliza{position:absolute;inset:0;display:flex;flex-direction:column;background:#F4F4F2;font:15px/1.55 'JetBrains Mono',Menlo,Consolas,monospace;color:#000B1C}#log{flex:1;overflow:auto;padding:18px 22px}#log p{margin:0 0 10px;white-space:pre-wrap}#log p.eliza{color:#943890}#log p.you:before{content:'> ';color:#5C6470}#ask{padding:12px 22px;border-top:1px solid #E1E1DE;background:#fff}#in{width:100%;border:0;outline:0;font:inherit;background:transparent;color:#000B1C}";
  document.head.appendChild(css);
  const box = document.createElement("div"); box.id = "eliza";
  box.innerHTML = '<div id="log"></div><form id="ask"><input id="in" autocomplete="off" placeholder="Say something, then press enter"></form>';
  document.body.appendChild(box);
  const log = box.querySelector("#log"), inp = box.querySelector("#in");
  const say = (who, s) => { const p = document.createElement("p"); p.className = who; p.textContent = s; log.appendChild(p); log.scrollTop = log.scrollHeight; };
  say("eliza", "HOW DO YOU DO. PLEASE TELL ME YOUR PROBLEM.");
  box.querySelector("#ask").addEventListener("submit", e => {
    e.preventDefault();
    const s = inp.value.trim(); if (!s) return;
    say("you", s); say("eliza", (reply(s) || "Please go on.").toUpperCase()); inp.value = "";
  });
  if (self !== top) inp.focus();
}"""

KOCH_CODE = """let times;                          // how many times
function setup() {
  createCanvas(900, 300); noLoop();
  times = createSlider(0, 6, 4, 1, 'times');
}
function koch(x1, y1, x2, y2, n) {      // the rule
  if (n == 0) { line(x1, y1, x2, y2); return; }
  let dx = (x2 - x1) / 3, dy = (y2 - y1) / 3;
  let ax = x1 + dx, ay = y1 + dy;       // one third
  let bx = x1 + 2 * dx, by = y1 + 2 * dy;  // two thirds
  let px = ax + dx / 2 + dy * .866;     // the peak: the
  let py = ay + dy / 2 - dx * .866;     // middle, turned 60°
  koch(x1, y1, ax, ay, n - 1);          // again, on each
  koch(ax, ay, px, py, n - 1);          // of the four
  koch(px, py, bx, by, n - 1);
  koch(bx, by, x2, y2, n - 1);
}
function draw() {
  background(255); stroke(0);
  koch(40, 240, 860, 240, times.value());  // n times
}"""

# Plays like the gif: one more time every second, until someone touches the slider.
KOCH_EXTRA = """let touched = false;
document.addEventListener('pointerdown', function (e) { if (e.target && e.target.type === 'range') touched = true; });
if (window._kochTimer) clearInterval(window._kochTimer);
window._kochTimer = setInterval(function () {
  if (touched || !times) return;
  times.value((times.value() + 1) % 7);
  times.elt.dispatchEvent(new Event('input'));   // the bar's label, and a redraw
}, 1100);"""

LEWITT_CODE = """const n = 50;                          // fifty points
let pts = [];
function setup() {
  createCanvas(800, 500);              // a wall
  stroke(0); noLoop();
  randomSeed(118);
  roll();
}
function roll() {                      // evenly distributed:
  pts = [];                            // one point per cell of
  let cols = 10, rows = 5;             // a 10 x 5 grid, at
  let w = width / cols, h = height / rows;   // random inside it
  for (let i = 0; i < n; i++) {
    let c = i % cols, r = floor(i / cols);
    pts.push([c * w + random(w), r * h + random(h)]);
  }
}
function draw() {
  background(255);
  for (let a of pts)                   // all connected
    for (let b of pts)
      line(a[0], a[1], b[0], b[1]);
}"""

LEWITT_EXTRA = """function mousePressed() { roll(); redraw(); }   // the same words, new dice"""

TEMPLATE = [
    'Write a p5.js sketch.',
    ' ',
    'RULE: [one sentence: what is drawn, how many, how they relate to each other]',
    ' ',
    'CHANCE: [what is random, and how much: a range]',
    ' ',
    'NUMBERS: canvas 600 x 600, white background, black stroke 1 px. [sizes, counts, colours]',
    ' ',
    'CONSTRAINTS: plain p5.js, no libraries. Draw once (noLoop). randomSeed(1). Nothing I did not ask for.',
    ' ',
    'OUTPUT: the whole sketch.js and nothing else. Then, in one sentence, the rule the code follows.',
]

SPEC_TWIST = [
    'Write a p5.js sketch.', ' ',
    'RULE: place ten points at random; the points', 'should be evenly distributed over the canvas;', 'all of the points should be connected by', 'straight lines — and one twist of your own:', ' ',
    '· the points sit on a circle', '· each line is as thick as it is long', '· lines are curves, bent by chance', '· thirty points; each joins its three', '  nearest neighbours only', '· the lines are coloured by their angle', ' ',
    'CHANCE, NUMBERS, CONSTRAINTS, OUTPUT:', 'as in the template (slide 51).',
]

ELIZA = [
    'Men are all alike.',
    '{violet:IN WHAT WAY}',
    "They're always bugging us about something or other.",
    '{violet:CAN YOU THINK OF A SPECIFIC EXAMPLE}',
    'Well, my boyfriend made me come here.',
    '{violet:YOUR BOYFRIEND MADE YOU COME HERE}',
    "He says I'm depressed much of the time.",
    '{violet:I AM SORRY TO HEAR YOU ARE DEPRESSED}',
    "It's true. I am unhappy.",
    '{violet:DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE UNHAPPY}',
]


def _live():
    """A link to the slide being appended, in the html deck: the pptx and the PDF show the code and a
    still, the html deck has the editor. len(S) is the new slide's index, and reveal counts from 0."""
    return f' · [edit it live](https://{SITE}/week02/#/{len(S)})'


def _linked(eyebrow_text, label, url):
    """An eyebrow with a link at the end, when there is somewhere to link to."""
    return f'{eyebrow_text} · [{label}]({url})' if url else eyebrow_text


S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 02 · LECTURE + WORKSHOP',
               'Rules that make things.',
               'Week 2 — machine A, p5.js, and a machine that writes rules.',
               notes='Join code on screen from 30 minutes before. Laptops out from the start: the code slides in the second half are editable in the html deck, and the exercise at the end needs one laptop per pair. The TAs have been pairing people without a laptop with people who have one.'))

S.append(agenda('SD2112 · WEEK 02', [
    'Last week, in your words', 'Machine A: rules', 'Instructions as art', 'Rules make pictures',
    'Rules that grow', 'p5.js: a sketchbook that runs', 'Specs, and prompts for coding', 'Exercise: one spec, one twist',
], notes='Eight stops. The first five are the lecture: what a rule is, and sixty years of people making art and design from rules, before and after computers. Break. Then the workshop: p5.js, in the slides themselves; a language model that writes p5.js from your words; and the one exercise, where a spec of forty words gets executed by a model, then twisted by you.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the cloud · the worries · the cups', notes='Five minutes of recap, from the data you gave us.'))

S.append(question('multiple_choice', 'Before we start: what do you have with you?', [
    'A laptop', 'A tablet', 'Only a phone', 'Nothing today',
], eyebrow_text='01 · LOGISTICS · MULTIPLE CHOICE',
    notes='ClassPoint. The sketches and the exercise run inside the html deck, in the browser: nothing to install, no account. The exercise needs one laptop per pair, so Cs and Ds move next to As now, not at the break; the TAs walk the room while the next two slides run.'))

S.append(cards(_linked('01 · YOUR WORRIES · AND THE WEEK THAT ANSWERS THEM', 'THE ANSWERS', WORRIES_URL), 'You worried about five things.', [
    ('CHEATING', 'Allowed, disclosed, yours.', 'The rule from week 1 stands: use any model, say which one, and answer for what it made. Week 11 is about authorship: who made Belamy?'),
    ('LOSING SKILLS', 'Five small makes.', 'Weeks 2 to 6: one thing a week where your hand stays on the rule. Today is the first.'),
    ('COPYRIGHT', 'Week 11.', 'Datasets, LoRAs, the Thaler cases, and what a court calls transformative.'),
    ('JOBS', 'Weeks 8 and 12.', "The designer's turn: what is left for you when the model makes the artefact. Curator, briefer, guardrail-setter."),
    ('BEING LIED TO', 'Weeks 4 and 9.', 'Hallucination and sycophancy in week 4. Bias, data and privacy in week 9.'),
], text_size=22, notes='Open the week-1 answers (the link in the eyebrow, once deck/week01-reports.json carries the id of "One hope and one worry" — it is withheld while the public page still carries names) and read three worries aloud, then point each at its week. The point is that every worry in the room is on the syllabus. Then the hopes, briefly: most of them are week 4 and 5.'))

S.append(figure_slide(_linked('01 · THE CUPS', 'THE WALL', CUPS_URL), 'Your prompts were rules. The model had the examples.', F.two_machines_cups(),
                      body=['A hundred first cups: white, ceramic, a handle. Nobody typed "handle". Your prompt was a rule, and the model pulled every cup back to its average. Today we look at the rules side on its own.'],
                      caption='Machine A: write the rule. Machine B: show the examples. This week is the left half; next week the right.',
                      notes='Open the cup wall from the link in the eyebrow (the week-1 image upload). The average cup was the dataset\'s, not Hong Kong\'s. Then: today we stay on the left. No model learns anything today, except in the last hour, where a language model writes machine A for you.'))

S.append(image_full('cups-wall.jpg', '01 · THE WALL · 87 FIRST CUPS, THEN THE 60 THAT SHIPPED',
                    'Every cup the room uploaded last week. The top rows are the average: white, ceramic, a handle, a wooden table, and nobody asked for any of it. The bottom rows are what a prompt with a rule in it does.',
                    fit='contain', bg=WHITE,
                    notes='Both uploads from week 1, in order: the 87 first cups, then the 60 that shipped. Let the room look for ten seconds. Ask: who typed "wooden table"? Nobody. That is the model\'s middle. Then the bottom rows: once the prompt carried a rule (a material, a use, a mood), the pictures spread out. The picture is made by tools/classpoint/collage.py from the public activity pages, images only.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(0, 1),
                 notes='Week 2 of module one. Next week, examples; then the three tool weeks. Challenge 1 starts today; awards next week.'))

# ───────────────────────── 02 · machine A ─────────────────────────
S.append(section('02', 'Machine A', 'symbolic AI · 1956 – today · if this, then that', bg=INK,
                 notes='Chapter two: what a rule is, sixty years of rule-based AI in one chapter, and why every designer already writes rules.'))

S.append(figure_slide('02 · A RULE', 'If this, then that. Nothing else.', F.decision_tree(),
                      body=['A rule is a condition and a consequence. A computer is a machine that follows rules exactly, forever, without judgement (Turing, 1936). Newell and Simon, 1976: intelligence is symbols plus search, which means rules applied to rules.'],
                      caption='Symbolic AI: knowledge written down as rules, applied by a program. Exact, explainable, and it has never heard of the Tulip chair.',
                      notes='Three questions in a row decide "chair". Walk the room through it. Then the pedestal chair: one leg, and the rule says no. You can add a rule for it, and then a beanbag arrives. Every fix is another rule written by hand. Hold that thought until the expert systems.'))

S.append(cards('02 · SIXTY YEARS OF MACHINE A', 'Rules were the first AI.', [
    ('1956 · DARTMOUTH', 'AI gets its name.',
     'McCarthy, Minsky, Shannon and Rochester spend a summer on "making machines use language, form abstractions and concepts". Newell and Simon bring the Logic Theorist: a program that proves theorems.'),
    ('1966 · ELIZA', 'Two hundred rules pass for a therapist.',
     'Weizenbaum\'s script finds a keyword and turns the sentence around. "I am sad" becomes "How long have you been sad?" His secretary asked him to leave the room so she could talk to it in private.'),
    ('1972 – 1986 · EXPERT SYSTEMS', 'Rules run a business. Then the winter.',
     'MYCIN: about 600 rules diagnose blood infections as well as Stanford\'s specialists. XCON: 10,000 rules configure every computer DEC sells. Then it ends: someone has to write, and maintain, every single rule.'),
], text_size=22, notes='Three moments. Dartmouth: the name and the bet: everything about intelligence can be described precisely enough for a machine. ELIZA: the first chatbot, and the first proof that people will talk to rules. Expert systems: rules made money, then hit the knowledge bottleneck: every rule hand-written by an engineer interviewing an expert. Machine B, learning the rules from examples, is the answer to that bottleneck. Week 3.'))

S.append(code_slide('02 · ELIZA · 1966', 'A rule that feels like a person.', ELIZA_RULES, F.eliza_transcript(ELIZA),
                    caption='Weizenbaum\'s script: find a keyword, apply its rule, send the rest back. No memory, no meaning. Talk to it; then add a rule of your own and press Run' + _live() + '.',
                    code_size=18, hint='add a rule, then Run', sketch=live('eliza', ELIZA_RULES, 600, 600, hint='type, then enter', extra=ELIZA_SCREEN),
                    notes='In the html deck the right side is a chat: type "I am sad" and read the rule that answers. The still is the 1966 transcript from Weizenbaum\'s paper, ELIZA in capitals. Every reply is a rule you can read: "you X" becomes "we were discussing you". Ask: does it understand? No. Does it behave intelligently, by our week-1 definition? Enough to fool people. Let someone add a rule: ["i hate (.*)", "Why do you hate $1?"], Run, try it. Intelligent-like behaviour through computation, and here you can read every line of the computation. Built to show how shallow this is; people confided in it anyway. Week 12: rule-based versus generative chatbots.'))

S.append(cards('02 · THE DEAL', 'Exact. Explainable. Brittle.', [
    ('EXACT', 'Same input, same output.',
     'A rule does the same thing every time. Even chance can be made repeatable: give the die a seed and the same picture comes back, on any machine, forever.'),
    ('EXPLAINABLE', 'You can point at the line that decided.',
     'Every output has a reason you can read. When a rule-based product does something strange, you can find out why. Machine B cannot say why. Next week.'),
    ('BRITTLE', 'Nothing outside the rule can happen.',
     'The definition does not know beanbags exist. Every new case needs a new rule, written by hand. That bottleneck ended the expert-systems boom.'),
], notes='The deal you make with machine A. All three come from the same fact: the rule is all there is. For the reflection, this is the vocabulary: rule-based versus adaptive. Ask the room for a rule-based feature they love and one they hate; auto-correct usually comes up on both sides.'))

S.append(cards('02 · YOU ALREADY WRITE RULES', 'Every designer already writes machine A.', [
    ('THE GRID', 'Snap to 8 px.', 'Columns, gutters, a spacing scale: a rule you set once, and every screen obeys it.'),
    ('THE BREAKPOINT', 'Narrower than 600 px? One column.', 'An if-then you have written, in words, for a developer to execute.'),
    ('THE SYSTEM', 'One button, every state.', 'Tokens, variants, auto layout: a rule-based machine that makes every button in the product.'),
    ('THE SPEC', 'Redlines, briefs, handoffs.', 'A rule written in words for a human to execute. Today you write one for a machine, and then for a machine that writes machines.'),
], text_size=24, notes='Designers are fluent in machine A and do not call it that. A design system is an expert system for buttons. A responsive layout is a rule. The spec is the one that matters today: a rule in words, for someone else to execute. The whole second half is about writing that well. Next slide: they write one.'))

S.append(question('short_answer', 'Write a rule for drawing a house.',
                  hint='One sentence. A stranger who has never seen a house must be able to follow it.',
                  eyebrow_text='02 · QUESTION · SHORT ANSWER',
                  notes='Ninety seconds. Read four aloud. Every rule leaves things open: size, roof angle, where the door is, whether there is a chimney. Two people following the same rule draw two houses. That gap, between what you said and what you meant, is the subject of the whole day. Keep the answers: the exercise comes back to them.'))

# ───────────────────────── 03 · instructions as art ─────────────────────────
S.append(section('03', 'Instructions as art', '1959 – 1971 · scores, events, wall drawings', bg=PINKS[0],
                 notes='Chapter three: before computers made art from rules, artists did, by writing the rule and handing the execution to someone else.'))

S.append(statement('Draw a straight line and follow it.', eyebrow_text='03 · LA MONTE YOUNG · COMPOSITION 1960 #10 · TO BOB MORRIS', size=120,
                   notes='One line. A complete artwork and a complete program. Performed hundreds of times, no two alike: the line, the surface, the walk, the speed were all left to the executor. Fluxus made a genre of these: the event score.'))

S.append(cards('03 · THE EVENT SCORE', 'The score is the work. Anyone can execute it.', [
    ('GEORGE BRECHT · 1959', 'Drip Music',
     '"A source of dripping water and an empty vessel are arranged so that the water falls into the vessel." Performed with a ladder and a jug, with a tap, with a pipette. The rule survives every execution.'),
    ('YOKO ONO · 1964', 'Grapefruit',
     'A book of instructions. "Painting to be stepped on: leave a piece of canvas or finished painting on the floor or in the street." Some cannot be executed at all. They are still pieces.'),
    ('JOHN CAGE · 1951 – 1960', 'Chance inside rules',
     'Music of Changes: every note decided by coin tosses on the I Ching. Water Walk: a score of timed actions with a bathtub, performed on live television. The rule decides where chance is allowed in.'),
], text_size=22, notes='Three scores. Brecht\'s is a rule with an open executor; Ono\'s are rules that may be impossible; Cage\'s put chance inside the rule and decide exactly how much. You watched Water Walk on the playlist: every action is timed to the second, and the sounds are whatever the objects do. Rules and chance, 1960. Schotter is the same idea with a plotter, eight years later.'))

S.append(video('03 · TINGUELY · MOMA GARDEN · 17 MARCH 1960', 'A machine whose rule was to destroy itself.', '6dgGu2w3Qvo',
               ['Homage to New York: bicycle wheels, motors, a piano, a weather balloon, built in the museum garden. Switched on, it was meant to end itself in about half an hour.',
                '- It failed properly: the fire brigade put it out. The rule ran; the execution surprised its author.',
                '- On the playlist with Cage, Kaprow and the Illiac Suite: watch the four before week 3.'],
               thumb='yt/6dgGu2w3Qvo.jpg',
               notes='Play a minute if there is time. The design point: Tinguely built the rule and then had no control over the execution, and the failure is part of the piece. Every rule you write for a machine will surprise you in execution. Cut this slide if behind.'))

S.append(video('03 · KAPROW · 1967 · PASADENA 2008 · BERLIN 2015', 'Instructions executed by strangers, decades later.', 'RZ_FAgfJsss',
               ['Fluids, 1967. The whole score: "During three days, about twenty rectangular enclosures of ice blocks (measuring about 30 feet long, 10 wide and 8 high) are built throughout the city. Their walls are unbroken. They are left to melt."',
                '- Kaprow called every re-execution a reinvention. Each one is the piece.',
                '- The spec is the artwork. The execution is delegated, and it is still the work.'],
               thumb='yt/RZ_FAgfJsss.jpg', body_size=28,
               notes='Forty-three words. Los Angeles, 1967; Pasadena, 2008; Berlin and Los Angeles, 2015, built by people Kaprow never met, after his death. Ask: who is the author of the Berlin one? Same answer as for a wall drawing, next slide, and the same answer we will give for code a model writes from your spec.'))

S.append(quote('"The idea becomes a machine that makes the art."',
               'Sol LeWitt, Paragraphs on Conceptual Art, Artforum, June 1967', size=96,
               notes='The full sentence: "When an artist uses a conceptual form of art, it means that all of the planning and decisions are made beforehand and the execution is a perfunctory affair. The idea becomes a machine that makes the art." Machine A, in a sentence, from an artist who never touched a computer.'))

S.append(statement('On a wall surface, any continuous stretch of wall, using a hard pencil, place fifty points at random. The points should be evenly distributed over the area of the wall. All of the points should be connected by straight lines.',
                   eyebrow_text='03 · SOL LEWITT · WALL DRAWING 118 · 1971 · THE WHOLE WORK', size=68, bg=PAPER,
                   notes='This is the entire artwork. First drawn in December 1971 at the Museum School in Boston by five art students, without LeWitt. Read it as a spec: an object, a tool, a count, a placement, an action. And two words that fight each other: "at random" and "evenly distributed". The exercise at the end starts from these forty-five words.'))

S.append(figure_slide('03 · WALL DRAWING 118 · EXECUTED BY A PYTHON SCRIPT, TODAY', 'Fifty points. 1,225 lines. Any wall.', F.lewitt_118(),
                      body=['Every execution is the work. The drafters decide what the words left open: the pencil, the wall, what "random" means. A museum buys the instructions and a certificate; the drawing is made again, by other hands, each time it is shown.'],
                      caption='The same forty-five words, executed by a program instead of five art students. LeWitt: "Each person draws a line differently and each person understands words differently."',
                      notes='Our execution: fifty points, one per cell of a jittered grid, so that "evenly distributed" and "at random" both hold. The drafters in Boston made the same decision with their eyes. Point at the quote: it is the spec-writer\'s problem in one sentence, and it is why a language model given the same words will give you something else. Executions of 118 exist in dozens of museums; none match.'))

S.append(content('03 · VERA MOLNÁR · 1959 – 1976', 'She executed her algorithms by hand for nine years.',
                 ['Machine imaginaire: from 1959 Molnár wrote procedures, a grid, a rule, a small dose of chance, and executed them herself, on paper, step by step, before she had access to a computer.',
                  '- 1968: her first plotter. The rule did not change. The executor did.',
                  '- (Dés)ordres, 1974: nested squares in a grid, and a small chance that any corner is nudged. Find the disorder.',
                  'A spec written for a machine that does not exist yet is still a spec.'],
                 figure=F.molnar_desordres(), caption='After Molnár: nested squares, every corner nudged with a small probability. Our execution, her rule.',
                 body_size=28,
                 notes='Molnár is the bridge between the wall drawing and the plotter: the same person, the same rules, two executors. She called her early method the imaginary machine. The lesson for the exercise: you can execute a rule by hand to understand it before you hand it to anything else.'))

# ───────────────────────── 04 · rules make pictures ─────────────────────────
S.append(section('04', 'Rules make pictures', 'Stuttgart 1965 · Bense · Nees · Nake · the plotter',
                 notes='Chapter four: the first computer art, and two rules worth knowing by heart: Schotter and Walk-Through-Raster.'))

S.append(content('04 · MAX BENSE · INFORMATION AESTHETICS', 'Beauty, measured. Art, generated.',
                 ['Birkhoff, 1933: aesthetic measure = order ÷ complexity. Bense, Stuttgart, 1950s: if beauty is information, it can be programmed.',
                  '- February 1965: Georg Nees shows plotter drawings in Bense\'s seminar gallery. Bense calls it artificial art. The first computer art exhibition, anywhere.',
                  '- A painter asks Nees whether the machine could draw the way he does. Nees: "Yes, if you tell me how you draw."',
                  'November 1965: Nake and Nees, Galerie Niedlich. This one hangs in the V&A.'],
                 image='nake-homage-to-paul-klee-1965.jpg', fit='contain',
                 caption='Frieder Nake, Hommage à Paul Klee 13/9/65 Nr.2, 1965. Zuse Graphomat Z64 plotter, programmed in ALGOL.',
                 body_size=28,
                 notes='Bense\'s claim: aesthetics is not taste, it is measurable order in a signal, and therefore generatable. The Nees anecdote is the whole lecture: the painter could not say how he drew, so the machine could not do it. Nake\'s Klee is on the wall from week 1; today we open the two rules behind pictures like it.'))

S.append(content('04 · GEORG NEES · SCHOTTER · c. 1968', 'One rule. One random number.',
                 ['Twelve columns, twenty-two rows of squares. Each square is moved and turned by a random amount, and the amount grows with the row.',
                  '- Row 0: a perfect grid. Row 21: gravel. Schotter means gravel.',
                  '- The rule decides everything except two numbers per square. Chance is kept on a leash; the picture is order turning into disorder.',
                  'The sliders are the rule\'s two numbers: how much disorder, how many rows.'],
                 figure=F.schotter(), sketch=live('schotter-rows', SCHOTTER_ROWS, 400, 700, hint='click = new dice'),
                 caption='After Nees: our execution of his rule. Siemens 4004, ALGOL, Zuse Graphomat; the original print is 28 × 22 cm.',
                 body_size=28,
                 notes='Say the rule in one breath: a grid; each square shifts and turns by a random amount that grows down the page. Watch it draw: the label under the picture says how far a square may move and turn on that row. Drag disorder to zero: the grid. To two: gravel from the third row. Ask: where is the design decision? In the rule and in the rate of decay, not in any square. After the break you get the twenty lines of code, editable.'))

S.append(code_slide('04 · 1982 · 10 PRINT CHR$(205.5+RND(1)); : GOTO 10', 'One coin toss. Two states. No memory.', TEN_PRINT, F.ten_print(cols=20, rows=12),
                    caption='One line of Commodore 64 BASIC, 1982: one of two diagonals, chosen by a coin toss, forever. Every cell is a fresh toss; none knows about the others' + _live() + '.',
                    sketch=live('ten-print', TEN_PRINT, 800, 480, hint='click = new dice', extra=TEN_PRINT_EXTRA),
                    notes='The smallest generative program there is, and the floor for the challenge: one rule, one random number, and it is already a picture. Two states per cell, heads or tails, and nothing carried from one cell to the next. Drag the coin: at 0.5 the maze; at 0.9 nearly all one diagonal, with the odd break. Everyone can hold the whole program in their head. Then Nake: two more states, and one thing remembered from the cell above. Thirty years later 10 PRINT got a book (Montfort et al., MIT Press, 2013).'))

S.append(image_full('nake-walk-through-raster-1966.jpg', '04 · FRIEDER NAKE · WALK-THROUGH-RASTER · SERIES 2, 1–4 · 1966',
                    'Look first. What repeats? What never happens? Four prints from one program: ALGOL 60 on a Zuse Graphomat Z64. Victoria and Albert Museum, E.955-2008.',
                    fit='contain', bg=WHITE,
                    notes='Ninety seconds of looking before any explanation. 10 PRINT had two states and no memory; ask what is different here. Then: what repeats? (vertical bars, horizontal caps, fields of each; a dense band along the diagonal). What never happens? (a cap directly under a drawn cell: every field of caps has gaps). Then the rule, in four steps. Nake finished a PhD in probability theory the year after he made these.'))

S.append(figure_slide('04 · WALK-THROUGH-RASTER · THE RULE IN FOUR STEPS', 'Four states. The cell above decides.', F.walk_breakdown(),
                      body=['A grid, drawn column by column, top to bottom. Every cell is one of four things: empty, a bar, a cap, or both (10 PRINT had two). Two rules decide: a bar is more likely near the diagonal, and a cap can only be drawn under an empty cell, so a cell remembers one thing about the one above it. The empty space flows up and to the right, and every field of caps has gaps.'],
                      caption='Nake, Walk-Through-Raster, series 2.1–4, 1966. Our reading of his rule: two yes/no decisions per cell, and one fact carried from the cell above.',
                      notes='Break it down slowly; this is the model for every generative piece. One: the raster is the stage, and the order of the walk matters: down each column, then the next. Two: four states, from two yes/no decisions. Three: the rule. The bar is chance, weighted by the distance to the diagonal. The cap depends on the cell above: only under an empty one. That one dependency is the whole texture. Four: because a cap needs an empty cell above it, and the walk goes down and then right, the empty space cannot be closed off: it flows from the bottom left to the top right, and the thick fields of caps along the diagonal always open up. Look back at the print with that in mind.'))

S.append(sketch_slide('04 · WALK-THROUGH-RASTER · WATCH THE WALK', 'The raster fills up, column by column.',
                      live('walk-watch', WALK_WATCH, 1200, 600, hint='click = new dice'),
                      body=['Left: the raster filling up, top to bottom, then the next column. Empty cells are tinted: watch the empty space flow up and to the right. Right: the four states and how many of each so far. Drag the cap chance: at 0 only bars; at 1, a cap under every empty cell.'],
                      notes='Let it run for one full walk (about five seconds at the default speed), then click for new dice. Point at the orange cell: the one just drawn. Its cap was allowed only because the cell above it was empty. Then slow it down with the speed slider and watch a field of caps form along the diagonal: every cap sits on an empty cell, so the field is full of gaps, and the tinted empty space climbs through it to the top right. Cap chance at 1: the maximum; still gaps. That is the rule guaranteeing something about the picture. In the pptx this is a still; the html deck runs it.'))

S.append(code_slide('04 · WALK-THROUGH-RASTER · THE RULE, IN TWENTY LINES', 'Two loops, two decisions, one fact carried down.', WALK_CODE, F.walk_through_raster(),
                    caption='Our execution, after Nake. "above" carries one fact from cell to cell: was the cell above empty? That line is the whole texture' + _live() + '.',
                    code_size=19, sketch=live('walk-through-raster', WALK_CODE, 600, 600, hint='click = new dice', extra=WALK_EXTRA),
                    notes='Read it top to bottom with the room. Two loops: columns, then rows, so the walk goes down each column. Two decisions per cell: bar, from a die weighted by the distance to the diagonal; cap, only below the top row and only if above is true. Then above is set for the next cell. Point at h > 0: the top row never gets a cap, because nothing is above it; look for that in the print. On your laptop: abs(w - h) → w - h, Run: half the picture turns solid (the fault from the sd5913 deck). Remove "above &&", Run: caps everywhere, no gaps, the flow is gone. This is the shape of every generative rule: a walk, a few decisions, and what one cell remembers about the last.'))

S.append(video('04 · HILLER & ISAACSON · UNIVERSITY OF ILLINOIS · 1957', 'A computer writes a string quartet.', 'n0njBFLQSk8',
               ['The Illiac Suite: the ILLIAC makes random notes and keeps the ones that pass the rules of counterpoint. Generate and test: the oldest move in symbolic AI.',
                '- The fourth movement chooses each note from the one before it: a chain. Nake\'s cells, nine years later, each decided by the one above.',
                '- On the playlist. Sixteen minutes, four experiments, one machine.'],
               thumb='yt/n0njBFLQSk8.jpg',
               notes='Rules make music too. The generate-and-test loop, propose at random and reject what breaks a rule, is the engine of a great deal of rule-based AI, and of most generative art. Week 6 comes back to sound with machine B. Cut if behind.'))

# ───────────────────────── 05 · rules that grow ─────────────────────────
S.append(section('05', 'Rules that grow', 'fractals · L-systems · parameters', bg=ORANGES[0],
                 notes='Chapter five, short: two more kinds of rule designers use: rules applied to their own output, and rules with the numbers left open.'))

S.append(figure_slide('05 · HELGE VON KOCH · 1904 · A FRACTAL', 'Replace every line with four. Then do it again.', F.koch_generations(),
                      body=['One rule, applied to its own output: cut a line in three, turn the middle third into a peak, and do the same to each of the four new lines. Four times: 256 lines. Forever: a curve of infinite length that fits in your hand, the same at every scale. Its dimension is log 4 ÷ log 3 = 1.26: more than a line, less than a surface.'],
                      caption='Mandelbrot, The Fractal Geometry of Nature, 1982: coastlines, clouds and ferns are rules like this one. Nobody could draw the twentieth generation before computers.',
                      notes='The fractal part, back from the 2025 deck: Koch\'s curve and its fractional dimension. The rule is one sentence; the picture is impossible by hand past four or five rounds. Self-similarity: zoom into any bump and you see the whole. Ask: is this still a line? Then the code, next slide, which is ten lines and calls itself.'))

S.append(code_slide('05 · KOCH · IN P5.JS', 'A rule that calls itself.', KOCH_CODE, F.koch_curve(),
                    caption='koch() draws a line, or replaces it with four shorter koch()s. The slider is how many times; it plays by itself until you touch it. Try turning 60° into 90°' + _live() + '.',
                    code_size=20, sketch=live('koch', KOCH_CODE, 900, 300, hint='plays on its own', extra=KOCH_EXTRA),
                    notes='Recursion in ten lines: the function calls itself with n − 1 until n is 0, when it draws a line. Let it play: 0, 1, 2 … 6 times. On your laptop: change .866 to 1 (a taller peak), or dx / 2 to dx (the peak leans). Every fractal, every procedural tree in a game, every Houdini setup is this: a rule that runs on its own result.'))

S.append(figure_slide('05 · LINDENMAYER · 1968', 'The same trick grows a plant.', F.lsystem_growth(),
                      body=['Rewrite every F with the rule, then rewrite the result, and again: four generations from one line. Lindenmayer, a biologist, wrote it for algae. The brackets are branches.'],
                      caption='F → F[+F]F[-F]F, turn 25.7°. Lindenmayer 1968; Prusinkiewicz & Lindenmayer, The Algorithmic Beauty of Plants, 1990.',
                      notes='F means draw forward; + and − turn; the brackets save and restore the position: a branch. Apply the rule four times and you have 81 segments on the trunk. Grasshopper, Houdini and every procedural-generation tool in games are this: rules that call themselves.'))

S.append(content('05 · PARAMETRIC DESIGN', 'Machine A, with sliders.',
                 ['A rule with numbers left open is a design space. Change a number, get a design; every one obeys the rule.',
                  '- Grasshopper, 2007: architecture as a graph of rules. A tower is a rule and a hundred numbers.',
                  '- The MIT Media Lab identity, 2011: one algorithm, forty thousand logos, one per person.',
                  '- Nervous System, Kinematics dress, 2014: a rule folds itself around a body.',
                  'The twelve chairs from week 1 are the same idea: chair(seat, back, angle, legs).'],
                 figure=F.parametric_chairs(), caption='Week 1: one function, twelve chairs. Parametric design is a rule you can ship.',
                 body_size=28,
                 notes='Same chairs as last week, now with the vocabulary: parameters. The sliders you have been dragging are parameters. The design work moves from the artefact to the rule and to choosing the numbers. Ask product designers in the room what they parametrise already; ask communication designers about their grids. Same thing.'))

S.append(figure_slide('05 · VARIABLE FONTS · 2016', 'One font, one number.', F.weight_ramp(),
                      body=['A letter is a rule with a parameter. Type designers have written machine A for a century: hinting, kerning, optical sizes. A variable font puts the number in your hands. This is Inter, the typeface of these slides, along its weight axis.'],
                      caption='Inter Variable, wght 100 to 900. OpenType 1.8, 2016: Adobe, Apple, Google and Microsoft, together for once.',
                      notes='For the communication designers: the closest rule-based machine to your daily work. One file, every weight, and the in-betweens that never existed as drawings.'))

S.append(statement('A rule is a design. The execution can be delegated.', eyebrow_text='05 · WHERE WE ARE', size=110,
                   notes='The sentence to carry across the break. LeWitt delegated to drafters, Nees to a plotter, Molnár to herself. After the break you delegate to p5.js, and then to a language model. The design is the rule.'))

S.append(statement('Break. Ten minutes.', eyebrow_text='AFTER THE BREAK · P5.JS · THEN A MACHINE THAT WRITES RULES', size=120, bg=PAPER,
                   notes='1:30. Laptops charged, the html deck of this week open on them: the code slides are editable there, and the exercise runs there. The TAs help anyone who cannot find it.'))

# ───────────────────────── 06 · p5.js ─────────────────────────
S.append(section('06', 'p5.js', 'a sketchbook that runs · inside these slides', bg=INK,
                 notes='Chapter six, hands-on: the tool, twenty lines, and Schotter in twenty. The code on these slides is editable in the html deck on your laptop: change a number, press Run.'))

S.append(content('06 · PROCESSING → P5.JS', 'Code as a sketchbook.',
                 ['1999: John Maeda\'s Design By Numbers at the MIT Media Lab: a language small enough for designers.',
                  '- 2001: Casey Reas and Ben Fry, Maeda\'s students, make Processing, "a software sketchbook".',
                  '- 2013: Lauren McCarthy starts p5.js: Processing for the browser. Nothing to install: today it runs inside these slides.',
                  '- Why it is here: the whole rule fits on one screen, and the picture is instant.'],
                 figure=F.lewitt_ten(seed=7), caption='Ten points at random, all connected: twenty lines of p5.js. Next slide.',
                 body_size=28,
                 notes='Processing is the tool every generative artist of the last twenty years learned on; p5.js is the same thing in a browser tab. The slides run it, and the same code runs in the p5 web editor or anywhere else later; today nothing leaves the deck. If someone knows Python or JavaScript already, fine; the vocabulary today is ten words.'))

S.append(code_slide('06 · ANATOMY', 'setup() runs once. draw() runs the rule.', TEN_CODE, F.lewitt_ten(seed=7),
                    caption='(0,0) is the top-left corner; y grows downwards; random(600) is a number between 0 and 600. Change 10 to 30, press Run. Then one 600 to 200, and see what breaks' + _live() + '.',
                    code_size=20, sketch=live('ten-points', TEN_CODE, 600, 600, hint='click = new dice', extra=TEN_EXTRA),
                    notes='Read it top to bottom. setup: make a canvas, say "once", roll the dice. roll: the rule: ten times, push a point at a random place. draw: paint it white, then for every pair a line, then a dot on every point. Ten words: createCanvas, noLoop, for, random, push, background, stroke, line, fill, circle. Then everyone on their laptop: 10 → 30, Run. One 600 → 200, Run: the points crowd the left. Six minutes, the TAs walk. A rule you can break on purpose is a rule you understand.'))

S.append(figure_slide('06 · RANDOM() · RANDOMSEED()', 'Same rule, three seeds.', F.lewitt_seeds(),
                      body=['random(600) is a number between 0 and 600, different every run. randomSeed(1) loads the die: the same picture every run, on every machine. Where you call random() is where the rule lets go; everything else is the rule.'],
                      caption='Three runs of the ten-point sketch with randomSeed(1), (2) and (3). Change the seed, keep the rule: a new picture that is still yours.',
                      notes='The seed is what makes machine A with chance still exact: Cage tossing coins, but with the coins recorded. For the challenge: a seed means you can show the exact picture you chose. For the reflection: this is the difference between a rule-based and an adaptive system in one function call.'))

S.append(code_slide('06 · SCHOTTER · IN P5.JS', 'A grid is two loops. Disorder is one number.', SCHOTTER_CODE, F.schotter(),
                    caption='Twenty lines. The outer loop walks the rows, the inner loop the columns; k grows from 0 to 1 down the picture and scales the shift and the turn. The slider is the number' + _live() + '.',
                    code_size=19, sketch=live('schotter', SCHOTTER_CODE, 400, 700, hint='click = new dice', extra=SCHOTTER_EXTRA),
                    notes='Two loops make a grid: say that sentence twice, it is the most useful thing in generative art. push/translate/rotate/pop: move the pen to the cell, nudge it, turn it, draw a square, come back. The chance is two lines. Nees wrote this in ALGOL for a plotter; you have it in a slide. On your laptop: rows 22 → 8, Run. PI / 4 → PI, Run. square → circle, Run.'))

S.append(figure_slide('06 · CHANGE ONE NUMBER', 'The same rule. Which one is yours?', F.schotter_variations(),
                      body=['This is the whole craft of the weekly challenge: write one rule, then find the one number that makes it yours.'],
                      caption='Left: Nees\'s numbers. Middle: the disorder tripled. Right: eight rows instead of twenty-two. Nothing else changed.',
                      notes='Three sketches, one rule, one number each. The design decision is the number, and taste is choosing it. Ask the room which of the three they would print.'))

# ───────────────────────── 07 · prompts for coding ─────────────────────────
S.append(section('07', 'Prompts for coding', 'machine B writes machine A · spec → code → picture',
                 notes='Chapter seven: the other executor. A language model turns your words into p5.js in seconds. That makes the words the work.'))

S.append(figure_slide('07 · THE SPEC IS THE DESIGN', 'One spec. Three executors.', F.spec_pipeline(),
                      body=['LeWitt\'s drafters; you, in the editor; a language model on genai.polyu.edu.hk. Same words, delegated execution, and never quite what you meant. Machine B writes machine A, and machine A does exactly what it is told.'],
                      caption='A language model is not a rule: the same prompt gives different code every time. The code it writes is a rule: the same seed gives the same picture every time.',
                      notes='Name the two machines in the pipeline. The model (B) is a translator from words to rules; the sketch (A) is the rule. Everything we said about machine A applies to the code: exact, readable, brittle. Everything about machine B applies to the model: fluent, typical, cannot say why. The spec is your handle on both.'))

S.append(cards('07 · ANATOMY OF A SPEC', 'Five things a rule must say.', [
    ('WHAT', 'The rule, in one sentence.', 'Like LeWitt: an object, a count, an action. "A grid of squares, each moved and turned by a random amount that grows with its row."'),
    ('CHANCE', 'Where the die is thrown.', 'Say exactly what is random and how much. "Up to half a cell and 45 degrees in the last row, nothing in the first."'),
    ('NUMBERS', 'Canvas, counts, sizes, colours.', 'Give them, or say "choose". A model that has to guess guesses the average: 400 × 400, pastel, particles.'),
    ('CONSTRAINTS', 'The rules about the rule.', 'Plain p5.js. No libraries. Draw once. A seed, so it repeats. Nothing you did not ask for.'),
    ('OUTPUT', 'What to hand back.', 'The whole sketch, nothing else. Then: "describe the rule this code follows in one sentence", a check that it understood.'),
], text_size=21, notes='Five headings. They are also the five things the room\'s house rules left out. Show how LeWitt\'s forty-five words cover the first three and leave the last two to the wall. A spec for a machine needs all five.'))

S.append(two_col('07 · THE TEMPLATE', 'A prompt that is a spec.',
                 ['Copy it, fill the brackets, paste it into a language model on **genai.polyu.edu.hk**. Paste what comes back into the editor on the **sketch slide** (59) and press Run.',
                  '- Rule first, constraints last: models obey the end of a prompt more than the middle.',
                  '- One rule per prompt. Two ideas are two sketches.',
                  'Keep the spec. When the code drifts, paste the spec again, not the code.'],
                 TEMPLATE, right_size=23, left_size=30, lang=None,  # a prompt, not code
                 notes='The template is on the course site and on Blackboard. Any of the language models on GenAI will do; pick one and stay with it for the session so the errors are consistent. The last bullet matters: the spec is the source, the code is a build.'))

S.append(code_slide('07 · WHAT GOOD LOOKS LIKE', 'Fifty points, all connected, from forty-five words.', LEWITT_CODE, F.lewitt_wall(),
                    caption='LeWitt\'s spec as twenty-two lines a model can write in seconds. Read it: where is the rule, where is the chance, where are the numbers? Then give it a twist' + _live() + '.',
                    code_size=19, sketch=live('fifty-points', LEWITT_CODE, 800, 500, hint='click = new dice', extra=LEWITT_EXTRA),
                    notes='This is what should come back from the template filled with Wall Drawing 118. Notice the decision in the middle: "evenly distributed" became a grid with one point per cell, at random inside it. A model may make that decision, or may not: next slide. Either way you can read it, because it is machine A. It is also a boring picture: every execution looks the same. The exercise fixes that with a twist.'))

S.append(figure_slide('07 · WHAT YOU SAID · WHAT YOU MEANT', '"At random", or "evenly distributed"?', F.lewitt_random_vs_even(),
                      body=['LeWitt asked for both at once. A drafter works it out by eye; a model picks one and does not tell you. Left: fifty calls to random(), clumps and gaps. Right: one point per grid cell, at random inside it. The spec decides, or the executor does.'],
                      caption='Same forty-five words, two readings. Ask for the rule back in one sentence and the difference shows up before you run anything.',
                      notes='The most important slide of the second half. Every ambiguity in a spec is a decision you handed to the executor. With drafters you get a phone call; with a model you get code. The fix is never in the code: rewrite the sentence.'))

S.append(cards('07 · WHAT GOES WRONG', 'Four ways the machine misreads you.', [
    ('IT ADDS', 'Things you did not ask for.', 'Colours, animation, noise(), a title. That is the model\'s average: the typical generative sketch. Say the constraints again; delete the rest.'),
    ('IT INVENTS', 'A function that does not exist.', 'The error under the box says "x is not defined". Paste it back to the model, word for word. Do not describe it.'),
    ('IT DROPS', 'A constraint quietly vanishes.', 'No seed, wrong canvas, draw() looping. Check the spec line by line against the code. Five lines, five ticks.'),
    ('YOU WERE VAGUE', '"Random", or "evenly"?', 'It did what you said, not what you meant. Fix the spec, not the code, and only then ask again.'),
], text_size=23, notes='All four are the average pulling: the model gives you the typical sketch, the typical function name, the typical omission. Three are fixed by restating the spec. The fourth is fixed by writing a better one. The exercise will produce all four in the room within ten minutes.'))

S.append(cards('07 · READING A RULE YOU DID NOT WRITE', 'Machine A can be read. Use it.', [
    ('THE RULE', 'Find the loop.', 'for is the rule\'s heartbeat: how many times, over what. Two loops are a grid.'),
    ('THE CHANCE', 'Find random().', 'Each call is one throw of the die. Count them: that is how much of the picture is not yours.'),
    ('THE NUMBERS', 'Find the constants.', 'Change one. Run. Change it back. This is how you learn what a number does, and how you make the sketch yours.'),
    ('THE BREAK', 'Delete a line.', 'What disappears tells you what the line did. A rule you can break on purpose is a rule you understand. Next week\'s machine cannot be read this way.'),
], notes='You do not need to write code to read it. Four moves, in this order, on any sketch a model gives you. You did all four on the slides before the break. The last one is the reflection\'s argument in miniature: rule-based systems are legible; adaptive ones are not.'))

S.append(content('07 · ITERATE LIKE A DESIGNER', 'One change per prompt. Keep the spec.',
                 ['Version the sketches: v1, v2, v3. The spec stays; the code is disposable.',
                  '- If you cannot say the change in words, the spec is not finished. Go back to the words.',
                  '- Ask for the rule back: "describe the rule this code follows in one sentence." If it does not match yours, the code does not either.',
                  '- Save the spec with the picture: as the caption today, as the process note in your reflection later.',
                  'Week 4 makes this general: prompting is briefing. Week 12: agents that execute the whole spec.'],
                 body_size=32,
                 notes='Iteration discipline, because the model makes iteration free and therefore sloppy. One change per prompt so you know what caused what. The spec in the caption is the same rule as last week\'s prompt in the caption: we keep the words with the picture, always. Then the exercise.'))

# ───────────────────────── 08 · the exercise: one spec, one twist ─────────────────────────
S.append(section('08', 'One spec. One twist.', f'30 minutes · in pairs · the sketch slide · {GENAI}', bg=YELLOWS[0],
                 notes='The one exercise of the day, in pairs, one laptop per pair. Step 1: LeWitt\'s forty-five words, cut to ten points, plus a twist of the pair\'s own, executed by a language model on the sketch slide. Step 2: a rule and a spec entirely their own, iterated until the picture is the one they meant; one upload per pair with the spec as the caption. Nicolò keeps time; the other three TAs walk.'))

S.append(activity('1 — LEWITT, WITH A TWIST', 10, 'Let the machine execute it.',
                  ['Put the spec on the right into a language model on **genai.polyu.edu.hk**, with **one twist of your own**: pick one, or invent one. Paste the code into the editor on the **next slide** and press Run.',
                   'If it fails, paste the error back, word for word. Then read the code: **what did the machine decide that the words left open?**'],
                  panel=SPEC_TWIST, panel_size=22, bg=YELLOWS[0],
                  notes='Ten minutes, like last week\'s cups: the same words for everyone, plus one sentence each, so the wall does not look alike. Expect all four failure modes: added colour, an invented function, a dropped seed, and the random-versus-evenly decision made silently. The TAs help with pasting errors back. The reading question is the point; make every pair answer it out loud to each other.'))

S.append(code_slide('08 · YOUR SKETCH', 'Paste the code here. Run it.', YOUR_SKETCH, F.sketch_placeholder(),
                    caption='The editor keeps what you paste, even after a reload. An error shows under the box: paste it back to the model, word for word. Come back here for every version' + _live() + '.',
                    hint='ctrl+enter runs it · Reset = the starter', sketch=live('your-sketch', YOUR_SKETCH, 600, 600, hint='your sketch'),
                    notes='The pair\'s workbench for the rest of the class: the model\'s code goes in the box, Run draws it, the errors show under the box. Nothing to install and nothing to log into; the code survives a reload. From the pptx or the PDF the caption links to this slide in the html deck. The TAs: a pair whose box shows red text pastes that text back to the model.'))

S.append(activity('2 — YOUR OWN RULE', 12, 'Your rule. Your spec. From scratch.',
                  ['Now a rule that is entirely yours: **one rule, one random number**, in the template on the right, in words a stranger could execute. Not Schotter, not LeWitt.',
                   'Ask the model, run it on the sketch slide, look. Fix the **spec**, not the code, until the picture is the one you meant. Keep v1, v2, v3.'],
                  panel=TEMPLATE, panel_size=21, bg=YELLOWS[1],
                  notes='Twelve minutes. The blank template: five lines to fill, and the words are the deliverable. One change per prompt; if the code drifts, paste the spec again. Push for precision on the chance: "a random amount" is not a spec; "up to 20 px" is. When a pair is happy, the whole spec becomes the caption of their upload. This is the start of Challenge 1.'))

S.append(question('image_upload', 'One per pair. Your rule: the picture, and the words that made it.',
                  hint='Caption: your spec, word for word.',
                  eyebrow_text='08 · CAPTURE · IMAGE UPLOAD · ONE PER PAIR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='One image per pair, about 55: the pair\'s own rule. Put the wall on screen: fifty-five rules, no two alike. Read two captions aloud and ask the room to guess the picture before showing it. Where the guess fails, the spec failed. Download the submissions: the specs come back in week 4 as the first briefs.'))

S.append(content('08 · WHAT JUST HAPPENED', 'You wrote the rule. The machine executed it.',
                 ['The model: it did what you said, not what you meant. Machine B translated your words into machine A, and machine A has no judgement to add.',
                  'The code: exact, repeatable with a seed, and readable. You could point at the line that decided. Next week: the machine that cannot say why.',
                  'The twist, then your own rule: one sentence changed the wall, and then the wall was yours. The design was in the words.',
                  '**The machine drew every line. You wrote the rule. That was the design.**'],
                 body_size=32,
                 notes='Mirror of the whole class. One spec, one executor that is a machine that writes machines, and the design was in the words every time. Say the last line slowly; it is last week\'s last line with one word changed.'))

S.append(cards('08 · CHALLENGE 1 · DUE BEFORE WEEK 3', 'A picture from rules.', [
    ('THE RULE', 'One rule, one random number.', 'Your own picture: not Schotter, not LeWitt. Start from the rule your pair wrote today, or from scratch.'),
    ('THE SPEC', 'Words first.', 'A stranger, or a model, could execute it. Keep it: it is the caption today and evidence in your reflection.'),
    ('THE SKETCH', 'p5.js, in the slide or anywhere.', 'Written by you, by a model, or both: say which. The code as a text file plus a screenshot, on Blackboard.'),
    ('THE VOTE', 'Bring it next week.', 'The room votes; the winners get shown and a participation star. The TAs help 30 minutes before and after class.'),
], notes='Three things on Blackboard before next class: the spec, the code as a text file, one screenshot. The model is allowed and must be named. Next week the room votes; the winners get shown and a star.'))

S.append(end('See you next week. Learning from examples.',
             'Bring your sketch. Watch AlphaGo and the four films.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: the other machine, concepts, neurons, Move 37, and the first challenge awards. Homework: the sketch on Blackboard, AlphaGo, and Cage, Tinguely, Kaprow and the Illiac Suite on the playlist. The TAs stay for 30 minutes.'))

# After the class: links each question slide to the answers the room gave (README, "After the
# class: publish the answers"). deck/week02-reports.json is written by classpoint.py's weekly.py
# once the class has run; until it exists this is a no-op.
attach_reports(S, HERE / 'week02-reports.json')

DECK = dict(title='SD2112 · AI in Design · Week 02', slides=finalize(S, FOOTER), pdf='SD2112-week02.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week02', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')
