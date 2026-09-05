"""
SD2112 · Artificial Intelligence in Design · Week 03 — the slide spec.

    python deck/week03.py            # builds _site/week03/ (html deck + pdf), export/week03*.pptx, export/preview/
    python deck/week03.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Learning from examples: machine B. Theories of concepts (classical vs prototype; Rosch, Labov),
GOFAI vs connectionism, the perceptron → backpropagation → deep learning, generalisation and
overfitting, rule-based vs adaptive systems in design tools, Move 37 and non-human creativity
(Boden, Wiggins), the image workshop (a prompt tells, a reference shows), and the activity
"Show it, don't tell it". Three live p5.js sketches: a perceptron that finds its own line,
Labov's cups and bowls as a 2-D space with a nearest-prototype and a 5-nearest-neighbour
verdict, and a polynomial fit that memorises or generalises. The drawn figures are in
tools/figures_week03.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week03 as W                            # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, code_slide, sketch_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(3)
CHAIRS = [f'ai-chair-{i}.jpg' for i in range(1, 5)]   # week 1: one prompt, four seeds

# ───────────────────────── the code on the slides (p5.js) ─────────────────────────
# The learning rule of the perceptron, as shown on the code slide: three numbers, nudged when a guess is wrong.
TRAIN_CODE = """let w1 = 0.3, w2 = -1.0, b = 0.1; // three numbers: the rule
const lr = 0.05;                   // how big a nudge
let wrong = 0;

function guess(x, y) {             // the rule, applied
  return w1 * x + w2 * y + b > 0 ? 1 : -1;
}

function onePass() {               // look at every example
  wrong = 0;
  for (const [x, y, t] of pts) {   // t: -1 is A, +1 is B
    if (guess(x, y) != t) {       // wrong? nudge, a little,
      w1 += lr * t * x;            // towards the example
      w2 += lr * t * y;
      b  += lr * t;
      wrong++;
    }
  }
}                                 // again, until none wrong"""

# (a) a perceptron that finds its own line · click adds A, shift-click adds B, C clears
PERCEPTRON_CODE = """// A rule nobody wrote: a perceptron finds a line from the examples.
// click: add a point of class A · shift-click: class B · B: toggle · C: clear
let pts = [];                        // [x, y, t]  t = -1 (A) or +1 (B)
let w1 = 0.3, w2 = -1.0, b = 0.1;    // three numbers: the whole rule
const lr = 0.05;
let passes = 0, wrong = 1, addB = false;
const PW = 920, PH = 480;            // the plot: x, y in [-1, 1]

function setup() {
  createCanvas(1400, 480);
  randomSeed(3);
  for (let i = 0; i < 12; i++) pts.push([randomGaussian(-0.45, 0.2), randomGaussian(-0.3, 0.2), -1]);
  for (let i = 0; i < 12; i++) pts.push([randomGaussian(0.45, 0.2), randomGaussian(0.35, 0.2), 1]);
  textFont('JetBrains Mono');
}

function guess(x, y) { return w1 * x + w2 * y + b > 0 ? 1 : -1; }

function onePass() {                 // the learning rule
  wrong = 0;
  for (const [x, y, t] of pts) {
    if (guess(x, y) != t) {          // wrong: nudge the three numbers
      w1 += lr * t * x; w2 += lr * t * y; b += lr * t; wrong++;
    }
  }
  passes++;
}

const sx = x => (x + 1) / 2 * PW, sy = y => (1 - y) / 2 * PH;

function draw() {
  if (wrong > 0 && frameCount % 2 == 0) onePass();   // one pass every other frame, until settled
  background(255);
  noStroke();                        // the verdict everywhere: A tint, B tint
  for (let gx = 0; gx < PW; gx += 20) for (let gy = 0; gy < PH; gy += 20) {
    const g = guess(gx / PW * 2 - 1 + 0.02, 1 - gy / PH * 2 - 0.02);
    fill(g < 0 ? color(251, 226, 211) : color(211, 231, 232)); rect(gx, gy, 20, 20);
  }
  stroke(0); strokeWeight(3);        // the line: w1 x + w2 y + b = 0
  if (abs(w2) > 1e-6) line(sx(-1), sy(-(w1 * -1 + b) / w2), sx(1), sy(-(w1 * 1 + b) / w2));
  else line(sx(-b / w1), 0, sx(-b / w1), PH);
  for (const [x, y, t] of pts) {
    strokeWeight(1.5); stroke(0);
    if (t < 0) { fill(237, 109, 36); circle(sx(x), sy(y), 14); }
    else { fill(100, 194, 195); triangle(sx(x), sy(y) - 9, sx(x) + 8, sy(y) + 6, sx(x) - 8, sy(y) + 6); }
  }
  const inPlot = mouseX >= 0 && mouseX < PW && mouseY >= 0 && mouseY < PH;
  if (inPlot) {                      // the mouse is a new object: what would the rule say?
    const mx = mouseX / PW * 2 - 1, my = 1 - mouseY / PH * 2;
    noFill(); stroke(0); strokeWeight(2); circle(mouseX, mouseY, 22);
    noStroke(); fill(0); textSize(16);
    const left = mouseX > PW - 240;    // keep the label inside the plot
    textAlign(left ? RIGHT : LEFT);
    text('here: ' + (guess(mx, my) < 0 ? 'A' : 'B') + '  score ' + nf(w1 * mx + w2 * my + b, 1, 2), mouseX + (left ? -16 : 16), mouseY - 12);
  }
  panel();
}

function panel() {
  noStroke(); fill(244, 244, 242); rect(PW, 0, width - PW, height);
  fill(237, 109, 36); textSize(15); textAlign(LEFT);
  text('A RULE NOBODY WROTE', PW + 30, 40);
  fill(0); textSize(19);
  text('the rule: w1·x + w2·y + b > 0 ?', PW + 30, 84);
  textSize(24);
  text('w1 = ' + nf(w1, 1, 2), PW + 30, 134);
  text('w2 = ' + nf(w2, 1, 2), PW + 30, 168);
  text('b  = ' + nf(b, 1, 2), PW + 30, 202);
  textSize(19);
  text('passes ' + passes + ' · wrong ' + wrong, PW + 30, 256);
  fill(wrong == 0 ? color(0, 120, 90) : color(200, 60, 30));
  text(wrong == 0 ? 'settled: every example on its side' : 'still moving: some examples wrong', PW + 30, 286);
  fill(92, 100, 112); textSize(16);
  text('● A: ' + pts.filter(p => p[2] < 0).length + '   ▲ B: ' + pts.filter(p => p[2] > 0).length, PW + 30, 328);
  text('click: add ' + (addB ? '▲ B' : '● A') + '  ·  shift-click: add ▲ B', PW + 30, 372);
  text('B: toggle the class  ·  C: clear', PW + 30, 398);
  text('put an A among the Bs: the line never settles', PW + 30, 436);
}

function mousePressed() {
  if (mouseX < 0 || mouseX >= PW || mouseY < 0 || mouseY >= PH) return;
  const t = (keyIsDown(SHIFT) || addB) ? 1 : -1;
  pts.push([mouseX / PW * 2 - 1, 1 - mouseY / PH * 2, t]);
  wrong = 1;
}

function keyPressed() {
  if (key == 'c' || key == 'C') { pts = []; w1 = 0.3; w2 = -1.0; b = 0.1; passes = 0; wrong = 0; return false; }
  if (key == 'b' || key == 'B') { addB = !addB; return false; }
}"""

# (b) Labov's cups and bowls: a 2-D space, a nearest prototype and a 5-nearest-neighbour vote
# (the verdicts sit on the left so that the resting mouse of the snapshot, at 60 % / 40 % of the canvas,
#  lands between the cup and the bowl prototypes: a big cup, or a tall bowl — the edge)
CUPS_CODE = """// Labov's cups and bowls: thirty example vessels in a space of shape (height ÷ width) and size.
// The mouse is a new object. Two machines judge it: the nearest prototype, and a vote of its 5 nearest examples.
const PANEL = 480, K = 5;                       // the verdicts on the left, the space on the right
const X0 = 540, X1 = 1380, Y0 = 40, Y1 = 440;   // the plot box
const R0 = 0.3, R1 = 2.3;                       // shape axis: height ÷ width, wide … tall
const CLASSES = ['cup', 'bowl', 'vase'];
const COL = {cup: [237, 109, 36], bowl: [100, 194, 195], vase: [148, 56, 144]};
let ex = [], proto = {};

function setup() {
  createCanvas(1400, 480);
  randomSeed(1973);
  for (let i = 0; i < 12; i++) ex.push({r: randomGaussian(1.05, 0.2), s: randomGaussian(0.36, 0.14), c: 'cup'});
  for (let i = 0; i < 10; i++) ex.push({r: randomGaussian(0.5, 0.14), s: randomGaussian(0.6, 0.17), c: 'bowl'});
  for (let i = 0; i < 8; i++) ex.push({r: randomGaussian(1.95, 0.2), s: randomGaussian(0.6, 0.15), c: 'vase'});
  for (const e of ex) { e.r = constrain(e.r, R0 + 0.05, R1 - 0.05); e.s = constrain(e.s, 0.08, 0.95); }
  for (const c of CLASSES) {                     // the prototype: the middle of the class
    const m = ex.filter(e => e.c == c);
    proto[c] = {r: m.reduce((a, e) => a + e.r, 0) / m.length, s: m.reduce((a, e) => a + e.s, 0) / m.length};
  }
  textFont('JetBrains Mono');
}

const px = r => map(r, R0, R1, X0, X1), py = s => map(s, 0, 1, Y1, Y0);
const dist = (a, b) => sqrt(sq((a.r - b.r) / (R1 - R0)) + sq(a.s - b.s));   // both axes count the same

function vessel(x, y, r, s, col, w = 2) {       // a little profile: width from size, height from ratio
  const wd = 12 + s * 26, ht = constrain(wd * r, 6, 70);
  stroke(col); strokeWeight(w); noFill();
  quad(x - wd / 2, y - ht / 2, x + wd / 2, y - ht / 2, x + wd * 0.38, y + ht / 2, x - wd * 0.38, y + ht / 2);
}

function draw() {
  background(255);
  noStroke(); fill(244, 244, 242); rect(0, 0, PANEL, height);
  stroke(225); strokeWeight(1);
  line(X0, Y1, X1, Y1); line(X0, Y0, X0, Y1);
  noStroke(); fill(92, 100, 112); textSize(15); textAlign(LEFT);
  text('height ÷ width: ' + R0 + ' wide → ' + R1 + ' tall', X0 + 8, 468);
  push(); translate(X0 - 36, 240); rotate(-HALF_PI); textAlign(CENTER); text('size  →', 0, 0); pop();
  for (const e of ex) vessel(px(e.r), py(e.s), e.r, e.s, COL[e.c]);
  for (const c of CLASSES) {                     // the prototypes
    const p = proto[c];
    noFill(); stroke(COL[c]); strokeWeight(3); circle(px(p.r), py(p.s), 46);
    noStroke(); fill(255, 230); rect(px(p.r) - 62, py(p.s) + 28, 124, 18);
    fill(COL[c]); textSize(14); textAlign(CENTER); text(c + ' prototype', px(p.r), py(p.s) + 42);
  }
  const m = {r: map(constrain(mouseX, X0, X1), X0, X1, R0, R1), s: map(constrain(mouseY, Y0, Y1), Y1, Y0, 0, 1)};
  // machine 1: the nearest prototype
  let best = CLASSES[0];
  for (const c of CLASSES) if (dist(m, proto[c]) < dist(m, proto[best])) best = c;
  // machine 2: a vote of the K nearest examples
  const near = ex.map(e => ({e, d: dist(m, e)})).sort((a, b) => a.d - b.d).slice(0, K);
  const votes = {}; for (const n of near) votes[n.e.c] = (votes[n.e.c] || 0) + 1;
  const win = CLASSES.reduce((a, c) => (votes[c] || 0) > (votes[a] || 0) ? c : a, CLASSES[0]);
  for (const n of near) { stroke(0, 60); strokeWeight(1); line(px(m.r), py(m.s), px(n.e.r), py(n.e.s)); }
  vessel(px(m.r), py(m.s), m.r, m.s, [0, 11, 28], 3);
  panel(m, best, win, votes, near);
}

function panel(m, best, win, votes, near) {
  const x = 30;
  noStroke(); fill(237, 109, 36); textSize(15); textAlign(LEFT);
  text('A NEW OBJECT · WHAT IS IT?', x, 40);
  const wd = 40 + m.s * 90, ht = constrain(wd * m.r, 12, 150);
  stroke(0, 11, 28); strokeWeight(3); noFill();
  quad(x + 90 - wd / 2, 150 - ht / 2, x + 90 + wd / 2, 150 - ht / 2, x + 90 + wd * 0.38, 150 + ht / 2, x + 90 - wd * 0.38, 150 + ht / 2);
  noStroke(); fill(0); textSize(17);
  text('shape ' + nf(m.r, 1, 2) + ' · size ' + nf(m.s, 1, 2), x + 200, 130);
  fill(92, 100, 112); textSize(15); text('the mouse reshapes it', x + 200, 158);
  fill(0); textSize(17);
  text('nearest prototype:', x, 270);
  fill(COL[best]); textSize(26); text(best, x + 260, 272);
  fill(0); textSize(17);
  text(K + ' nearest examples:', x, 330);
  let vx = x + 260;
  for (const n of near) { fill(COL[n.e.c]); rect(vx, 316, 22, 18); vx += 28; }
  fill(COL[win]); textSize(26); text(win + ' ' + round(100 * (votes[win] || 0) / K) + '%', x + 260, 380);
  fill(92, 100, 112); textSize(15);
  text((votes[win] || 0) == K ? 'every neighbour agrees: the middle of a concept' : 'the neighbours disagree: the edge of a concept', x, 416);
  text('Labov, 1973: the boundary is a region, not a line', x, 440);
}"""

# (c) memorising vs generalising: a polynomial of degree 1 … 11 through 12 points, tested on 6 hidden ones
FIT_CODE = """// Memorising or generalising: twelve examples, a curve of degree 1 to 11 (the mouse), six hidden test points.
const PW = 920, PH = 480, X0 = 60, X1 = 880, Y0 = 60, Y1 = 420;
let train = [], test = [], showTest = true;
const truth = x => 0.5 + 0.28 * sin(2.4 * PI * x + 0.5) + 0.08 * x;

function setup() {
  createCanvas(1400, 480);
  randomSeed(12);
  for (let i = 0; i < 12; i++) { const x = (i + 0.5) / 12 + random(-0.02, 0.02); train.push([x, truth(x) + randomGaussian(0, 0.05)]); }
  for (let i = 0; i < 6; i++) { const x = (i + 0.5) / 6 + random(-0.05, 0.05); test.push([x, truth(x) + randomGaussian(0, 0.05)]); }
  textFont('JetBrains Mono');
}

const cheb = (k, x) => cos(k * acos(constrain(2 * x - 1, -1, 1)));   // a well-behaved basis

function fit(pts, d) {                          // least squares: the numbers that make the curve pass closest
  const n = d + 1, A = [], y = [];
  for (const [x, v] of pts) { A.push(Array.from({length: n}, (_, k) => cheb(k, x))); y.push(v); }
  const M = Array.from({length: n}, () => Array(n + 1).fill(0));
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) for (let p = 0; p < A.length; p++) M[i][j] += A[p][i] * A[p][j];
  for (let i = 0; i < n; i++) for (let p = 0; p < A.length; p++) M[i][n] += A[p][i] * y[p];
  for (let i = 0; i < n; i++) M[i][i] += 1e-9;
  for (let c = 0; c < n; c++) {                 // Gaussian elimination with pivoting
    let piv = c; for (let r = c + 1; r < n; r++) if (abs(M[r][c]) > abs(M[piv][c])) piv = r;
    [M[c], M[piv]] = [M[piv], M[c]];
    for (let r = 0; r < n; r++) if (r != c) { const f = M[r][c] / M[c][c]; for (let k = c; k <= n; k++) M[r][k] -= f * M[c][k]; }
  }
  return M.map((row, i) => row[n] / row[i]);
}

const evalAt = (co, x) => co.reduce((a, c, k) => a + c * cheb(k, x), 0);
const rmse = (co, pts) => sqrt(pts.reduce((a, [x, v]) => a + sq(evalAt(co, x) - v), 0) / pts.length);
const px = x => map(x, 0, 1, X0, X1), py = v => map(v, 0, 1, Y1, Y0);

function draw() {
  background(255);
  const d = round(constrain(map(mouseX, X0, X1, 1, 11), 1, 11));
  const co = fit(train, d), eTrain = rmse(co, train), eTest = rmse(co, test);
  stroke(225); strokeWeight(1); line(X0, Y1, X1, Y1); line(X0, Y0, X0, Y1);
  stroke(0, 11, 28); strokeWeight(3); noFill();
  beginShape();
  for (let x = 0; x <= 1.0001; x += 0.004) { const v = evalAt(co, x); if (v >= -0.01 && v <= 1.01) vertex(px(x), py(v)); else { endShape(); beginShape(); } }   // clipped to the plot box
  endShape();
  strokeWeight(1.5); stroke(0); fill(237, 109, 36);
  for (const [x, v] of train) circle(px(x), py(v), 14);
  if (showTest) { noFill(); stroke(100, 194, 195); strokeWeight(3); for (const [x, v] of test) triangle(px(x), py(v) - 10, px(x) + 9, py(v) + 7, px(x) - 9, py(v) + 7); }
  noStroke(); fill(92, 100, 112); textSize(15); textAlign(LEFT);
  text('● 12 examples it learned from   ▲ 6 hidden points it never saw', X0, 40);
  text('mouse x: degree 1 (left) → 11 (right)', X0, 456);
  panel(d, eTrain, eTest);
}

function panel(d, eTrain, eTest) {
  const x = PW + 30;
  noStroke(); fill(244, 244, 242); rect(PW, 0, width - PW, height);
  fill(237, 109, 36); textSize(15); text('HOW FLEXIBLE IS THE RULE?', x, 40);
  fill(0); textSize(40); text('degree ' + d, x, 100);
  textSize(15); fill(92, 100, 112); text((d + 1) + ' numbers to find', x, 128);
  const bar = (label, e, y, col) => {
    fill(0); textSize(17); text(label, x, y);
    fill(232, 232, 228); rect(x, y + 12, 340, 22);
    fill(col); rect(x, y + 12, constrain(map(e, 0, 0.3, 0, 340), 0, 340), 22);
    fill(0); textSize(15); text(nf(e, 1, 3), x + 352, y + 30);
  };
  bar('error on the 12 examples', eTrain, 170, color(237, 109, 36));
  bar('error on the 6 hidden points', eTest, 250, color(100, 194, 195));
  fill(0); textSize(17);
  const v = d <= 2 ? ['too simple: it misses the shape', 'underfitting'] : d <= 6 ? ['about right: it learned the shape', 'generalising'] : ['hits every example, misses the new ones', 'memorising · overfitting'];
  text(v[0], x, 350);
  fill(237, 109, 36); textSize(24); text(v[1], x, 386);
  fill(92, 100, 112); textSize(15); text('click: hide or show the hidden points', x, 434);
}

function mousePressed() { showTest = !showTest; }"""

VOTE_ENTRIES = [   # placeholders: the TAs paste the four shortlisted specs here before the deck is built (spec only, no names)
    '(the first shortlisted spec goes here — TAs fill in; no names)',
    '(the second shortlisted spec goes here)',
    '(the third shortlisted spec goes here)',
    '(the fourth shortlisted spec goes here)',
]

RULE_PANEL = [
    'ROUND 1 · TELL IT', ' ',
    'Write the rule for your chair:', ' ',
    '"A chair is ________ with ________', 'and ________. It is never ________."', ' ',
    'Twenty words at most.', ' ',
    'Prompt = your rule, word for word.', 'No image attached.', ' ',
    'Keep the rule: it is the caption.',
]

SHOW_PANEL = [
    'ROUND 2 · SHOW IT', ' ',
    'Prompt, exactly:', ' ',
    '"a chair like these"', ' ',
    'Attached: your two round-1 images.', 'No other words.', ' ',
    'Then ask, out loud:', ' ',
    'What did it take from each image?', 'What did neither of us ask for?', ' ',
    'One of you uploads it. Caption:', 'the three words + whose two chairs.',
]

PUSH_PANEL = [
    'ROUND 4 · OFF THE PROTOTYPE', ' ',
    'Prompt: "a chair like these"', 'References only. No adjectives.', ' ',
    'Iterate by swapping a reference,', 'never by adding words.', ' ',
    'Stop when all four agree:', '- no dataset has this chair', '- it is still a chair', ' ',
    'Caption: which inputs made it.',
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 03 · LECTURE + WORKSHOP',
               'Learning from examples.',
               'Week 3 — machine B: concepts, neurons, Move 37, and a picture from references.',
               notes='Join code on screen from 30 minutes before. Phones or laptops out: the second half is on genai.polyu.edu.hk again, like week 1. Challenge 1 is on Blackboard; the TAs have shortlisted four entries for the vote.'))

S.append(agenda('SD2112 · WEEK 03', [
    'Last week, in your words', 'What is a concept?', 'Machine B: neurons that learn', 'Rule-based, or adaptive?',
    'Move 37', 'Telling, and showing', "Activity: show it, don't tell it", 'Challenge 2, and next week',
], notes='Eight stops. The first four are the lecture: what a concept is, and how a machine can have one without anyone writing it down. Break. Then Move 37 and the creativity debate, the image workshop, and the activity, where the same chair gets told in words and then shown in pictures. Module one closes today: after this you have both machines.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the film · the walls · the vote', bg=TEALS[0],
                 notes='Fifteen minutes: the homework film, what week 2 left on the wall, and the first challenge awards.'))

S.append(question('word_cloud', 'AlphaGo. One word.',
                  hint='You watched the film. The first word that comes to mind.',
                  eyebrow_text='01 · QUESTION · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each; leave it up for a minute. Expect: sad, Lee Sedol, move 37, creative, alien, machine, beautiful. Read the three biggest aloud and keep a screenshot: the cloud comes back in chapter five, when we ask whether the move was creative. Anyone who has not watched it: it is on the playlist, ninety minutes, before the quiz in week 7.'))

S.append(cards('01 · WEEK 2 · WHAT THE WALLS SAID', 'One spec. A hundred executions.', [
    ('THE HAND', 'Forty-five words, a hundred drawings.',
     'Nobody drew the same ten points. The spec left the pencil, the spread and the meaning of "random" to you. A rule is never complete; the executor finishes it.'),
    ('THE MODEL', 'It did what you said.',
     'A language model wrote your p5.js. Where the spec was vague it decided silently: "at random" or "evenly", it picked one. Machine B wrote machine A.'),
    ('THE CODE', 'You could read the line that decided.',
     'Exact, repeatable with a seed, legible. Today we meet the machine that cannot be read that way, and find out why we still use it.'),
], text_size=22, notes='Show the two walls from last week: the hand drawings and the four-person specs. Pick one spec and one drawing and read them together. Then the sentence to carry into today: machine A is a rule you wrote. In an hour you will have the other half.'))

S.append(question('multiple_choice', 'Challenge 1. Which rule made the best picture?', VOTE_ENTRIES,
                  eyebrow_text='01 · CHALLENGE 1 · THE VOTE · MULTIPLE CHOICE',
                  notes='Replace the four entries with the ones the TAs shortlisted: the spec only, no names, no pictures yet. Read each spec aloud and let the room imagine the picture before voting. Then show the four sketches from Blackboard, in the same order, and count the surprise: where the picture is better than the spec suggested, the executor did the work. Winners get a star; anyone who submitted gets the participation mark.'))

S.append(content('01 · CHALLENGE 1 · THE WINNERS', 'Shown from Blackboard. Read the spec first.',
                 ['Four rules, four random numbers, four pictures: shown live from the submissions, the spec read aloud before each picture appears.',
                  '- The vote decides the star. The TAs choose one more: the spec a stranger could execute best.',
                  '- Every submission is evidence for your reflection: keep the spec, the link and the screenshot together.',
                  'What to look for: where does chance enter, and how much is it allowed to move?'],
                 body_size=32,
                 notes='Open Blackboard on the second screen. Show the four in the vote order; for each, ask the room where the die is thrown. Add the TA pick: the best-written spec, which is not always the best picture, and say why that matters — a spec a stranger can execute is a rule you actually understand. Two minutes, then the map.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(0, 2),
                 notes='Week 3 closes module one. Week 1 gave you both machines in a chair; week 2 was the rules side; today is the examples side. Next week the tools begin: language machines, then images, then sound, each with a challenge.'))

# ───────────────────────── 02 · what is a concept? ─────────────────────────
S.append(section('02', 'What is a concept?', 'definitions · prototypes · cups and bowls', bg=INK,
                 notes='Chapter two: before the neurons, the idea they will have to hold. Two theories of what a concept is, and they map onto the two machines exactly.'))

S.append(question('short_answer', 'Define "cup" for a machine.',
                  hint='One sentence. The machine will apply it to every object on Earth, with no judgement of its own.',
                  eyebrow_text='02 · QUESTION · SHORT ANSWER',
                  notes='Ninety seconds; read four aloud. Every definition lets in something wrong or throws out something right: "a container for drinking" admits a glass and a bottle; "with a handle" throws out most of the cups in this room. This is the classical theory failing in real time. Keep the answers: the cups sketch in a few minutes does the same job with numbers.'))

S.append(cards('02 · THE CLASSICAL THEORY', 'A concept is a definition.', [
    ('SINCE ARISTOTLE', 'Necessary and sufficient conditions.',
     'A thing is a member if it has every required feature, and anything with them all is in. A triangle: three sides, closed. In or out; no degrees of triangle.'),
    ('THE TEST', 'Can you write the list?',
     'For a triangle, yes. For a cup, a chair, a game, a good layout: every list you write admits the wrong thing or excludes the right one. You just tried.'),
    ('WITTGENSTEIN · 1953', 'Games have no common feature.',
     'Philosophical Investigations, §66: board games, card games, ball games, ring-a-ring-a-roses. What runs through all of them? Nothing. "A complicated network of similarities overlapping and criss-crossing."'),
], text_size=22, notes='The classical theory is machine A applied to meaning: a definition is a rule, membership is a verdict. It works for mathematics and for law and fails for almost everything a designer makes. Wittgenstein\'s games are the famous counter-example: he asks you to look, not think, and you find no feature shared by all. Next slide is that paragraph as a table.'))

S.append(figure_slide('02 · WITTGENSTEIN · FAMILY RESEMBLANCE', 'No feature runs through all of them.', W.w03_family(),
                      body=['Six games, seven features. A definition would need a full column; there is none. Chess and ring-a-ring-a-roses share almost nothing, yet both are games, because a chain of resemblances links them: "family resemblances", he called it, §67.'],
                      caption='After Philosophical Investigations §66–67 (1953). The features are ours; the argument is his. Rosch borrowed the term for her 1975 experiments.',
                      notes='Walk one column: "winning" — ring-a-ring-a-roses has no winner. "players" — patience has one. No column is full, so no definition exists, and yet nobody in this room is confused about what a game is. Hold this table: in twenty minutes the perceptron will be doing the same thing with numbers instead of ticks.'))

S.append(cards('02 · ROSCH · 1975', 'Concepts have a middle and an edge.', [
    ('ROSCH · 1975', 'Goodness of example.',
     'People rated members of ten categories from 1 (a very good example) to 7. A robin is a very good bird; a penguin is a poor one. A chair is furniture at its best. Nobody had trouble answering: typicality is real and shared.'),
    ('ROSCH & MERVIS · 1975', 'Family resemblance, measured.',
     'The most typical members share the most features with the rest of the category and the fewest with other categories. Typicality is a score, not a verdict: Wittgenstein\'s table with numbers in it.'),
    ('WHAT IT MEANS', 'A prototype, not a definition.',
     'A concept is organised around its best examples. The edge is fuzzy, and it moves. This is the week-1 chair wall: everyone pictured the same chair, and nobody had written a rule.'),
], text_size=22, notes='Eleanor Rosch, Berkeley, 1975: two papers that ended the classical theory for psychology. The first measures typicality and finds everyone agrees on it; the second explains it with Wittgenstein\'s family resemblance, counted. Say the design version: every category has a middle everyone can draw and an edge everyone argues about. The prompts in week 1 pulled to the middle because the model is a prototype machine. Now the cups.'))

S.append(sketch_slide('02 · LABOV · 1973 · CUPS AND BOWLS · LIVE', 'Where does a cup stop being a bowl?',
                      live('w03-cups', CUPS_CODE, 1400, 480, hint='the mouse is a new object'),
                      caption='Thirty example vessels in a space of shape (height ÷ width) and size. The mouse is a new object. First verdict: the nearest prototype. Second verdict: a vote of its five nearest examples — where they disagree, you are at the edge. At rest it sits between the cup and the bowl.',
                      notes='Labov showed people line drawings of containers that varied in width and depth and asked them to name each one. The names shifted gradually from cup to bowl as the drawing widened, with a wide region where people disagreed. This sketch is his experiment as a machine: move the mouse from the cups to the bowls and watch the vote go from five-nil to three-two — that is the edge, and it is a region, not a line. Note that neither verdict uses a definition: one measures distance to a prototype, the other asks the neighbours. Both are machine B in miniature. Cut short if behind, but do the crossing once.'))

S.append(content('02 · LABOV · 1973 · CONTEXT', 'The edge moves with what is in it.',
                 ['Labov\'s second move: the same drawings, imagined with something in them. With coffee, more people said "cup". With mashed potatoes, more said "bowl". Flowers: "vase".',
                  '- The object did not change. The concept did. Context is part of the category.',
                  '- Your week-1 cups: a hundred white mugs with handles, the dataset\'s prototype, not Hong Kong\'s.',
                  'A definition cannot do this. A prototype with examples can: the edge is where design happens.'],
                 figure=W.w03_labov_context(), caption='After Labov 1973: one drawing, three contexts, three names.',
                 body_size=27,
                 notes='This is the slide that matters for designers: the same shape is a cup with coffee in it and a bowl with soup in it. Meaning is not in the object; it is in the object plus the situation. Put the week-1 cup wall up if you have the screenshot: whose prototype is that? The dataset\'s. Week 9 comes back to who chose the examples. Now let us name the two theories with the two machines.'))

S.append(cards('02 · TWO THEORIES · TWO MACHINES', 'A definition is a rule. A prototype is examples.', [
    ('CLASSICAL THEORY', 'Machine A.',
     'A concept is a list of conditions. Membership is a verdict: in or out. Exact, explainable, and it throws out the beanbag. Symbolic AI took this theory and built expert systems on it.'),
    ('PROTOTYPE THEORY', 'Machine B.',
     'A concept is a cloud of examples with a middle. Membership is a distance: more or less typical. Fuzzy, fluent, and it cannot say why. Machine learning is this theory, built.'),
], notes='The bridge of the day. Every AI in this course holds concepts one of these two ways. The rule-based system has a definition of "chair" and applies it; the learned system has ten thousand chairs and a feel for the middle. Ask: which theory did your week-1 cup prompt meet? The second. Which one did your week-2 spec meet? The first — the code is a definition. Quick check next.'))

S.append(question('multiple_choice', 'Which sentence is prototype theory?', [
    'A chair is anything with a seat, a back and at least three legs',
    'Every chair shares one feature that makes it a chair',
    'Some chairs are better examples of "chair" than others',
    'A chair is whatever the dictionary says it is',
], eyebrow_text='02 · QUICK CHECK · MULTIPLE CHOICE',
    notes='C. A, B and D are all the classical theory in different clothes: a list of conditions, a single essential feature, an authority holding the list. Only C admits degrees. Ask for a chair that is a "worse example": a beanbag, a swing, a throne — and notice nobody says "not a chair".'))

# ───────────────────────── 03 · machine B: neurons that learn ─────────────────────────
S.append(section('03', 'Machine B', 'GOFAI vs connectionism · 1958 · 1986 · 2012', bg=TEALS[0],
                 notes='Chapter three, the core of the lecture: how a machine gets a concept without anyone writing it. One neuron, one learning rule, sixty years.'))

S.append(cards('03 · TWO SCHOOLS', 'Write the symbols, or grow the connections.', [
    ('GOFAI', 'Good Old-Fashioned AI.',
     'Haugeland\'s name, 1985, for what we called machine A: intelligence is symbols and rules, written by people. Knowledge is a list. Dartmouth 1956, ELIZA, MYCIN, XCON.'),
    ('CONNECTIONISM', 'Knowledge in the weights.',
     'Many simple units, each a weighted vote; the knowledge is in the numbers on the connections, and the numbers are found from examples. Nothing is written down anywhere.'),
    ('THE BET', 'Which one scales?',
     'The rules school won the first thirty years: it worked, and it could be read. The examples school needed data and chips it did not have. Then it got both.'),
], text_size=22, notes='Two schools of AI, both born in the 1950s, that spent thirty years not talking to each other. GOFAI is Haugeland\'s 1985 label for the symbolic school. Connectionism is the other bet: no symbols, just connections with numbers on them, adjusted by experience. The rest of this chapter is one neuron, one learning rule, and why it took until 2012.'))

S.append(figure_slide('03 · ONE NEURON', 'A neuron is a weighted vote.', W.w03_neuron(),
                      body=['Two inputs, two weights, a bias, a threshold. Multiply, add, compare with zero: that is the whole unit. Three numbers hold everything it knows. Rosenblatt, 1958, called it a perceptron.'],
                      caption='Rosenblatt, "The perceptron: a probabilistic model for information storage and organization in the brain", Psychological Review 65, 1958. The cup here is Labov\'s: shape and size in, a verdict out.',
                      notes='Read it left to right with the numbers: shape 1.1 times 1.6, size 0.4 times minus 0.8, minus 1.2, equals 0.24, above zero, so "cup". Now the important sentence: nobody typed 1.6. The three numbers were found. Change them and the neuron holds a different concept. Learning is changing them when the guess is wrong, and the next slide does that live.'))

S.append(sketch_slide('03 · THE PERCEPTRON · 1958 · LIVE', 'A rule nobody wrote.',
                      live('w03-perceptron', PERCEPTRON_CODE, 1400, 480, hint='move the mouse: what would it say? · click adds A · shift-click adds B · C clears'),
                      caption='Twenty-four examples, two classes. The line is w1·x + w2·y + b = 0; every pass over the examples nudges the three numbers where a guess was wrong, and the line settles. Add an A among the Bs and it never settles: one line cannot.',
                      notes='Watch it once from a reload: the line starts wrong, swings, settles, and the panel reads zero wrong. Nobody wrote that line; it came out of the examples. Then interact: move the mouse — the verdict for a new point, with its score. Click to add examples: the line moves to accommodate them. Then the failure: add a few A points deep inside B and the line thrashes forever. That is Minsky and Papert\'s 1969 objection in one gesture, and the reason this took until 1986 to fix. Press C to clear and let a student build a dataset.'))

S.append(code_slide('03 · THE LEARNING RULE', 'Wrong? Nudge the three numbers. Again.', TRAIN_CODE, W.w03_perceptron_steps(),
                    caption='Our execution of Rosenblatt\'s rule: after zero, one, three and twenty-five passes over the same examples. The line moves only when a guess is wrong; when nothing is wrong it stops.',
                    code_size=20,
                    notes='The whole of machine learning in fifteen lines. guess() is the rule applied; onePass() looks at every example and, where the guess is wrong, moves each number a little towards the example. lr is how big a step. Say what is not here: no definition of A or B, no feature named, no if-then about chairs. Compare with the week-2 code: there the rule was the code; here the code is a rule for finding rules. Everything since 1958 is this loop, bigger.'))

S.append(cards('03 · 1958 · 1969 · 1986', 'A machine that learns, and what it took.', [
    ('1958 · ROSENBLATT', 'The perceptron.',
     'The paper in Psychological Review, then hardware: the Mark I, 400 photocells in a 20 × 20 grid, weights as motor-driven potentiometers. The New York Times, July 1958: a machine the Navy expects "will be able to walk, talk, see, write, reproduce itself and be conscious of its existence".'),
    ('1969 · MINSKY & PAPERT', 'One line cannot.',
     'Perceptrons, the book: a single layer can only draw one straight line, so it cannot even learn XOR. Funding for networks dries up for a decade. The rules school wins the seventies.'),
    ('1986 · BACKPROPAGATION', 'Rumelhart, Hinton and Williams.',
     'Four pages in Nature: put units in layers, send the error backwards, nudge every weight. Hidden units invent their own features. Hinton: Nobel Prize in Physics, 2024, with Hopfield.'),
], text_size=21, notes='Three dates. 1958: the machine learns, and the press promises consciousness — the first AI hype cycle, sixty-eight years ago. 1969: the limit is real; a single neuron is a single line. 1986: layers plus backpropagation, and the limit is gone, on paper. What was still missing was examples and speed. Next slide shows the limit and the fix as pictures.'))

S.append(figure_slide('03 · THE LIMIT, AND THE FIX', 'One line cannot. Two layers can.', W.w03_xor(),
                      body=['XOR: A on one diagonal, B on the other. No straight line separates them, so one neuron never settles. Add a hidden layer of two neurons and the network can draw two lines and vote on them. The band is a rule nobody wrote.'],
                      caption='Minsky & Papert, Perceptrons, 1969 · Rumelhart, Hinton & Williams, "Learning representations by back-propagating errors", Nature 323, 1986.',
                      notes='Left: try to draw a line; every one gets a cluster wrong. Middle: two hidden units, each a neuron, each one line; the output unit combines their verdicts. Right: the band between the two lines is the concept the network found. Nobody said "band". That is what "learned representation" means in the 1986 title: the hidden units come to represent features nobody named. Stack more layers and the features get richer, which is the next slide.'))

S.append(figure_slide('03 · 2012 · ALEXNET', 'Deep: the features are learned too.', W.w03_layers(),
                      body=['30 September 2012: Krizhevsky, Sutskever and Hinton win the ImageNet challenge with an eight-layer network: 15.3% error against 26.2% for the runner-up, trained on 1.2 million labelled photos in about a week on two gaming GPUs. The other entries that year ran on hand-crafted features (SIFT, Fisher vectors); AlexNet grew its own from the pixels, at a scale nobody had managed.'],
                      caption='ImageNet: Fei-Fei Li, from 2006; 14 million images labelled by 49,000 Mechanical Turk workers in 167 countries. Who chose the examples, and who labelled them, is week 9.',
                      notes='The picture is a story of layers: the first layers become edge detectors, the middle ones parts, the last ones objects — and nobody programmed any of that; the layers became those detectors because it lowered the error. AlexNet is the 1986 idea with a million examples and a graphics card. Say the two enablers plainly: the web gave the examples, gaming gave the chips. And then the design point in the caption: 49,000 people labelled the photos for pennies. The examples are the material, and someone chose them.'))

S.append(sketch_slide('03 · GENERALISATION · LIVE', 'Memorising is not learning.',
                      live('w03-fit', FIT_CODE, 1400, 480, hint='mouse x = how flexible the rule is · click hides the hidden points'),
                      caption='Twelve examples; a curve with 2 to 12 numbers to find; six hidden points it never saw. Left: the fit. Right: the error on the examples and on the hidden points. Move right and the first error falls to zero while the second explodes.',
                      notes='The mouse sets how flexible the rule is. Far left: a straight line, too simple, wrong everywhere. Middle: it learns the shape, and the hidden points agree. Far right: it passes through every example exactly and misses every new point: it has memorised the examples, not learned the concept. This is overfitting, and it is why every model is judged on data it never saw. Ask: which of the two errors does a client see? The second one, always. Then the design version: a portfolio of twelve chairs is not a concept of chair.'))

S.append(cards('03 · THE DEAL', 'Fluent. Fuzzy. Opaque.', [
    ('FLUENT', 'It handles the case nobody wrote.',
     'A learned rule covers the middle of its examples and interpolates between them. That is why it can write, draw and see: no list of conditions could.'),
    ('FUZZY', 'Every answer is a degree.',
     'Chair 0.93, stool 0.05. There is no line, only a slope, and it moves with the examples. The edge of the concept is exactly where it is least sure — and where you work.'),
    ('OPAQUE', 'It cannot say why.',
     'Sixty million numbers found by nudging. No line to point at, no rule to read, no fix but more examples. When it is wrong you cannot ask it; you can only retrain it.'),
], notes='The mirror of week 2\'s "exact, explainable, brittle". Machine B trades all three for the ability to handle what nobody wrote down. For the reflection this is the vocabulary: rule-based versus adaptive, and the deal each one makes. Ask the room for a feature they love that is fuzzy and one they hate that is opaque; autocomplete usually gets both answers.'))

S.append(question('multiple_choice', 'A model scores 100% on its training examples and 55% on new ones. What happened?', [
    'It learned the rule perfectly', 'It memorised the examples: overfitting', 'The new examples are wrong', 'It needs fewer examples',
], eyebrow_text='03 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. Perfect on the examples and bad on new ones is the signature of memorising. A is the trap: a hundred percent on training data is not evidence of anything. D is backwards: more examples, not fewer, and a less flexible rule. This is the question that separates people who have understood machine B from people who have used it.'))

# ───────────────────────── 04 · rule-based or adaptive ─────────────────────────
S.append(section('04', 'Rule-based, or adaptive?', 'the same menu · two machines · four tests', bg=ORANGES[0],
                 notes='Chapter four, short: the vocabulary of your reflection, on the tools you already use. Three pairs, four tests, one question.'))

S.append(cards('04 · THE SAME MENU', 'Three pairs you use every week.', [
    ('PHOTOSHOP', 'Auto Levels · Generative Fill',
     ['**Auto Levels** stretches the histogram so the darkest pixel is black and the lightest white. A rule, for decades. Same input, same output.',
      '**Generative Fill**, May 2023: a diffusion model trained on Adobe Stock invents what belongs in the hole. Examples.']),
    ('FIGMA', 'Auto layout · Figma Make',
     ['**Auto layout**, December 2019: padding, direction, spacing; the frame resizes by rules you set.',
      '**Figma Make**, May 2025: describe the screen, get a prototype. A language model decided the layout. Examples.']),
    ('YOUR KEYBOARD', 'Spell-check · autocomplete',
     ['**Spell-check** looks a word up in a list. Not in the list: red line. A rule.',
      '**Autocomplete** predicts your next word from everything ever typed. It is fluent, it is usually right, and it once finished your sentence with someone else\'s.']),
], text_size=21, notes='Same application, two machines, side by side. The test is always the same: is there a list someone wrote, or a pile of examples someone collected? Ask for a fourth pair from the room — Grammarly\'s two modes, Lightroom\'s presets versus its AI masks, a font\'s kerning table versus a layout suggestion. There is always one.'))

S.append(cards('04 · FOUR TESTS', 'How to tell which machine you are holding.', [
    ('SAME IN, SAME OUT?', 'Rules repeat.',
     'Run it twice with the same input. Identical: a rule. Different, or "regenerate" is a button: examples.'),
    ('CAN IT SAY WHY?', 'Rules explain.',
     'A rule-based feature can show you the line that decided. A learned one shows you a confidence, at best.'),
    ('DOES IT NEED DATA?', 'Examples eat.',
     'If it got better after "training", "learning your style" or "more usage", it is adaptive. Ask what it was fed and by whom.'),
    ('CAN IT SURPRISE YOU?', 'Examples interpolate.',
     'A rule cannot output what is outside the rule. A model can produce the case nobody wrote — and the mistake nobody expected.'),
], text_size=23, notes='Four questions to ask of any feature, in a review, in a brief, in your reflection. They are the four properties of the two deals: exact/repeatable, explainable/opaque, hand-written/fed, brittle/fluent. Practise on the next slide with the list you made in week 1.'))

S.append(question('multiple_choice', 'Which of these four is rule-based, machine A?', [
    'Figma auto layout', 'Photoshop Generative Fill', 'Spotify\'s Discover Weekly playlist', 'Google Translate',
], eyebrow_text='04 · SORT THE TOOLS · MULTIPLE CHOICE',
    notes='A. Auto layout is padding and direction, set by you, applied by rules. The other three are learned: a diffusion model, a recommender trained on listening, a neural translation model. Then, if there is time, open the week-1 answers to "where did AI touch your design work" and read four; the room sorts each one by show of hands, using the four tests. Keep the sorted list: it seeds the week-8 discussion of using versus incorporating.'))

S.append(statement('Machine A is a rule you wrote. Machine B is a rule nobody wrote.', eyebrow_text='04 · WHERE WE ARE', size=104,
                   notes='The sentence to carry across the break. A rule you wrote: exact, explainable, brittle. A rule nobody wrote, found from examples: fluent, fuzzy, opaque. Neither is better; every AI feature you meet is one, the other, or a mix, and your job is to know which one you are holding.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · MOVE 37 · THEN IMAGES FROM REFERENCES', size=120, bg=PAPER,
                   notes='1:22. After the break: the creativity debate, then phones and laptops on genai.polyu.edu.hk. Anyone without a PolyU GenAI login sorts it out with a TA now.'))

# ───────────────────────── 05 · Move 37 ─────────────────────────
S.append(section('05', 'Move 37', 'Seoul · 10 March 2016 · non-human creativity', bg=PINKS[0],
                 notes='Chapter five: the film you watched, the move everyone remembers, and the question under the whole course: was it creative?'))

S.append(video('05 · ALPHAGO · THE FILM · 2017', 'You watched it. Now the move.', 'WXuK6gekU1Y',
               ['Seoul, 9–15 March 2016: five games, AlphaGo 4, Lee Sedol 1. Lee Sedol: 9-dan, eighteen international titles.',
                '- Game 2, 10 March, move 37: a shoulder hit on the fifth line. Michael Redmond, commentating, called it "creative" and "unique": a move most professionals would not have considered.',
                '- DeepMind: the model gave a human a 1-in-10,000 chance of playing it. It played it anyway, and won.',
                '- Game 4, move 78: Lee Sedol\'s reply, "a divine move". His only win.'],
               thumb='yt/WXuK6gekU1Y.jpg', body_size=26,
               notes='Play the move-37 sequence if the room has not all watched it: the commentators\' silence, Lee Sedol leaving the room. Facts first: the dates, the score, and the number DeepMind gave — one in ten thousand. Then the setup for the debate: nobody ordered move 37. Lovelace said that was impossible. Hold the word cloud from the start of the class next to this.'))

S.append(cards('05 · HOW ALPHAGO LEARNED', 'Shown human games. Then it played itself.', [
    ('SHOWN', 'About 30 million positions.',
     'Trained first on expert human games: predict the human move. Machine B, exactly as this morning: examples in, a feel for the good move out.'),
    ('SELF-PLAY', 'Millions of games against itself.',
     'Then it played its own copies and learned from the results. The examples were now its own: a dataset nobody curated, that no human had played.'),
    ('THE MATCH', 'October 2015, then Seoul.',
     'Fan Hui, the European champion, 5–0 in October 2015; the Nature paper in January 2016; Lee Sedol in March. AlphaGo Zero, 2017: no human games at all, and stronger.'),
    ('THE MOVE', 'Outside the human middle.',
     'A move humans rated at 1 in 10,000 is, by definition, far from the prototype of good play. It came from the self-play examples, not the human ones.'),
], text_size=21, notes='Two phases. The first is this morning\'s lecture: examples from humans, a network that predicts the typical expert move. The second is where the interesting part comes from: playing itself, it generated examples no human had ever produced, and learned from those. Move 37 lives in that second dataset. So: is that creativity, or a very large search? Boden and Wiggins give us the words.'))

S.append(figure_slide('05 · BODEN · WIGGINS · THE CONCEPTUAL SPACE', 'Exploring the space, or moving it.', W.w03_conceptual_space(),
                      body=['Boden: a conceptual space is the set of things a style, a genre or a tradition allows. Exploring it finds new things inside; transforming it changes the rules of the space. Wiggins, 2006, wrote that down as three things a creative system has: what counts as a member (R), how it searches (T), how it judges (E).'],
                      caption='Boden, The Creative Mind, 1990 / 2004 · Wiggins, "A preliminary framework for description, analysis and comparison of creative systems", Knowledge-Based Systems 19, 2006.',
                      notes='The universe is every legal move; humans only ever play inside a small region of it, the moves three thousand years of play consider good — that region is R. Exploratory creativity searches inside it. Move 37 sits outside R and inside the game. After 2016 professionals started playing fifth-line shoulder hits: the region moved. In Boden\'s terms that is transformational — for us. For AlphaGo it was exploratory: it searched its own, larger space. Which one you call it depends on whose R you mean. That is the debate.'))

S.append(two_col('05 · TWO READINGS', 'Creative, or alien?',
                 ['**Creative.** Wiggins\' test judges the output: experts were astonished, and the move changed how humans play. New and valued, by the field itself. Lovelace\'s objection meets a counter-example.',
                  '**Alien.** It searched a space it does not know is Go. It has no idea what it did, no intention, no audience in mind. The move is only creative in our conceptual space; in its own it was typical.',
                  'Both readings agree on one thing: the examples decided. Choose them and you choose what the machine can surprise you with.'],
                 ['WIGGINS · 2006', 'Creativity: "the performance of tasks', 'which, if performed by a human,', 'would be deemed creative."', ' ',
                  'BODEN', 'exploratory: new places inside', 'the rules of the space', 'transformational: change the rules', ' ',
                  'LOVELACE · 1843', 'it "can do whatever we know how', 'to order it to perform"', ' ',
                  'YOUR WORD CLOUD', 'the first word you gave AlphaGo', 'was the room\'s verdict'],
                 right_size=23, left_size=28,
                 notes='Two readings, both defensible, and the point is to make the room take one. The creative reading uses Wiggins\' output test from week 1 and the fact that the field changed. The alien reading says creativity needs a subject, an intention, an audience — and AlphaGo has none. Ask: does it matter that Lee Sedol thought it was beautiful? Then the short answer.'))

S.append(question('short_answer', 'Was Move 37 creative? Yes or no, and one reason.',
                  hint='One line. Use a word from today: prototype, edge, examples, exploratory, transformational, opaque.',
                  eyebrow_text='05 · THE DEBATE · SHORT ANSWER',
                  notes='Two minutes to write; then five to argue. Read a yes and a no aloud, pick people who used different words, and let two more respond. No correct answer; this is the course question in its first concrete form, and it comes back in the reflection and in week 11. Keep the answers with the word cloud: by week 12 you can show them how their vocabulary changed.'))

S.append(quote('"…there is an entity that cannot be defeated."',
               'Lee Sedol to the Yonhap news agency, November 2019, after announcing his retirement: with AI in Go, even the number one player would face it.',
               size=88,
               notes='November 2019: Lee Sedol retires, saying that even as number one he would face an entity that cannot be defeated. Read it two ways. The human reading: a game lost its point. The design reading: the field\'s conceptual space moved, and the humans in it had to decide what they were now for. That is chapter seven of week 1 — the designer\'s turn — happening to a Go player three years early. Now the tools.'))

# ───────────────────────── 06 · telling and showing ─────────────────────────
S.append(section('06', 'Telling, and showing', f'{GENAI} · a prompt, then a reference image', bg=TEALS[0],
                 notes='Chapter six, the workshop: two ways to steer an image model, and they are the two machines again. A prompt tells; a reference shows. Phones and laptops on genai.polyu.edu.hk.'))

S.append(content('06 · WEEK 1 · THE CHAIRS COME BACK', 'Your prompt told. The model had the examples.',
                 ['One prompt, four seeds, four chairs, and they are the same chair: four legs, a back, wood, a bit of mid-century.',
                  '- The words selected a region of the examples. They did not add any. The model answered from its middle.',
                  '- "No handle", "unusual", "barely a chair": adjectives are rules, and the prototype pulled every one back.',
                  'Today: the other input. Not a rule for the model to apply, but an example for it to stand near.'],
                 images=CHAIRS,
                 caption='Week 1: "a chair, studio product photograph, plain white background". One model, four seeds.',
                 body_size=28,
                 notes='Same four chairs as week 1, now with the vocabulary: the prompt selected the middle of a prototype. Every word you add is a rule, and a rule can only select among the examples the model already has. The way to move the middle is to give it a new example: a reference image. That is showing instead of telling, and it is why this week\'s challenge has references in it.'))

S.append(figure_slide('06 · TELL, OR SHOW', 'A reference image is an example, not a rule.', W.w03_tell_show(),
                      body=['Words select among the examples the model already has, so "a chair" lands in the middle every time. A reference puts one more example on the table and the output moves toward it. It cannot say "no handle"; it can show a cup with none.'],
                      caption='On genai.polyu.edu.hk, use the Flux or Qwen model that takes an image input next to the text (the TAs confirm which). What comes back sits between the reference and the prototype: a mix, not a copy, and not a rule applied.',
                      notes='Two rows, same model. Top: telling; the output is the prototype. Bottom: showing; the output is pulled toward the references — their proportions, their splay, their back — and sits between them and the middle. Three consequences for the workshop: a reference cannot forbid anything; two references give you an in-between; and a reference is somebody\'s picture, which is week 11\'s question. Now how to do it.'))

S.append(cards('06 · ON GENAI', 'Four moves.', [
    ('1 · PICK', 'A model that takes an image.',
     f'On {GENAI}, choose the Flux or Qwen image model that has an image input next to the prompt box. Same login as week 1.'),
    ('2 · TELL', 'Text only, first.',
     'Write the rule for what you want, run it, keep the image. That is your baseline: the prototype for those words.'),
    ('3 · SHOW', 'Attach one or two references.',
     'Say almost nothing: "like this", "like these". Run it. Compare with the baseline: what moved, what the model refused to give up.'),
    ('4 · EDIT', 'One change at a time.',
     'Feed it its own output with one instruction — "the same chair, no arms" — or swap a reference, or add three words. One change per run, so you know which machine answered. Save the prompt and the references with every image.'),
], text_size=22, notes='Four moves, and the discipline from week 2 applies: one change per run so you know what caused what. The TAs checked which model on GenAI accepts an image input; say which. Phone browsers work. If uploads are slow, one laptop per pair.'))

S.append(cards('06 · WHAT A REFERENCE DOES', 'It can pull. It cannot forbid.', [
    ('IT PULLS', 'Toward the example.',
     'Proportions, palette, material, mood: whatever the model can read off the picture moves the output that way. This is how you leave the middle without a paragraph of adjectives.'),
    ('IT MIXES', 'Two references, an in-between.',
     'Two references do not add up; they average. Use that on purpose: a chair between a stool and a throne is a design you could not have typed.'),
    ('IT CANNOT FORBID', 'No rule survives.',
     '"No handle" is a rule; the model has no rule-machine to apply it. Show a cup without one and it may still add it back: the prototype pulls on the reference too.'),
    ('IT COPIES', 'Somebody made that picture.',
     'A reference that is someone\'s work pulls their work into yours. Style, likeness, a product. Week 11 is authorship; today: use your own images, or ours.'),
], text_size=22, notes='Four things to expect in the next half hour. The pull is the point. The mixing is the creative trick. The failure to forbid is the lesson: references are machine B inputs, and there is no machine A in there to enforce a rule. The last one is the ethics: only your own pictures today, or the course chairs.'))

S.append(content('06 · LIVE · THE EDGE CHAIR', 'Watch: tell it, then show it.',
                 ['**Tell.** "a chair" — the middle. Then "an object that is barely still a chair" — still the middle, slightly more designed. Week 1\'s failure, repeated on purpose.',
                  '**Show.** The same words with this image attached. Watch what moves and what does not.',
                  '**Show twice.** Two week-1 chairs as references and "a chair like these". A chair nobody typed.',
                  'Then it is your turn: alone, in pairs, in fours.'],
                 image='ai-chair-edge.jpg', fit='cover', body_size=30,
                 caption='Week 1: "an object that is barely still a chair, an unusual seat that stretches the definition of chair". Same model, one seed.',
                 notes='Live, five minutes, on the classroom PC with GenAI. First telling: get the prototype, then ask for the edge with words and get the prototype again — the room saw this in week 1. Then attach the edge chair as a reference and run the same words: the output moves. Then two references and almost no words. If there is a minute, the edit: feed the result back with "the same chair, no arms" and see which machine answers. Narrate the two machines while it generates: words are rules the model applies to its middle; pictures are examples that move the middle. If GenAI is slow, have the three results ready as screenshots.'))

# ───────────────────────── 07 · activity: show it, don't tell it ─────────────────────────
S.append(section('07', "Show it, don't tell it.", f'35 minutes · a chair · {GENAI} · phone or laptop', bg=YELLOWS[0],
                 notes='The activity. Three rounds, one chair: alone, you tell the model in words; in pairs, you show it two pictures and no words; in fours, you push it off the prototype with references only. Each round ends in an image; the caption says which inputs made it. Nicolò keeps time; Amber, WU Zhao and MA Jie walk. One device per pair at least.'))

S.append(activity('1 — ALONE · TELL IT', 5, 'Write the rule. Get the picture.',
                  [f'Open **{GENAI}** and pick an image model. Write a **rule for a chair** in at most twenty words: what makes yours a chair, and one thing it must never have.',
                   'Prompt = the rule, word for word. **No image attached.** One run.',
                   'Keep the image and the rule. Then look: what did the model obey, and what did it ignore?'],
                  panel=RULE_PANEL, panel_size=22, bg=YELLOWS[0],
                  notes='Five minutes, silent. The rule is a definition: this is machine A talking to machine B. Watch for the "never" clause: most of the room will ask for no arms or no legs and get them anyway. That is the point, and they should notice it before anyone tells them.'))

S.append(question('image_upload', 'Everyone: upload your told chair.',
                  hint='The image from round 1. Caption: your rule, word for word.',
                  eyebrow_text='07 · CAPTURE 1 · IMAGE UPLOAD · EVERYONE',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='ClassPoint image upload, everyone, caption required: the rule. Three minutes. Put the wall up: a hundred chairs told in words, and most of them are the same chair with a different adjective. Read two captions with a "never" in them and check the picture: did the model obey? Usually not. Rules select; they do not command.'))

S.append(activity('2 — IN PAIRS · SHOW IT', 8, 'Two pictures. Three words.',
                  ['Swap phones. Attach **both** of your round-1 images as references. Prompt: **"a chair like these"** — nothing else.',
                   'Run it. Put the three images side by side. **What did it take from each?** What did neither of you ask for?',
                   'Run it once more with only the better reference. Keep the image you would show a client.'],
                  panel=SHOW_PANEL, panel_size=22, bg=YELLOWS[1],
                  notes='Eight minutes. Now the same chair is shown, not told. Expect an in-between: the proportions of one, the material of the other, and something from the prototype nobody asked for. Make every pair say out loud what came from where; that sentence is the reflection\'s argument in miniature. The TAs help with the image input if a model refuses it.'))

S.append(question('image_upload', 'One per pair: the chair like these.',
                  hint='The image from round 2. Caption: "a chair like these", and whose two round-1 chairs went in as references.',
                  eyebrow_text='07 · CAPTURE 2 · IMAGE UPLOAD · ONE PER PAIR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='Two minutes, one upload per pair, caption required: the three words and the two references. This is the shown wall; put it next to the told wall and let the room see the in-betweens: the proportions of one chair, the material of the other, and something from the prototype nobody asked for. Read one caption and check what came from which picture. The fours start as soon as the upload is in.'))

S.append(activity('4 — TWO PAIRS · OFF THE PROTOTYPE', 10, 'References only. Leave the middle.',
                  ['Join the pair behind you: four images on the table. Choose the **two furthest from the middle** that all four of you still call a chair.',
                   'Feed only those two. Iterate by **swapping a reference**, never by adding words. Three runs at most.',
                   'Stop when the four of you agree: **no dataset has this chair, and it is still a chair.** One scribe uploads it; caption: which inputs made it.'],
                  panel=PUSH_PANEL, panel_size=22, bg=YELLOWS[2],
                  notes='Ten minutes in fours. The constraint is the lesson: no adjectives, only examples. Four people choosing which two pictures to show the model is curating a dataset — week 11, in miniature. Push them to keep swapping references rather than reaching for words; when they reach for words, ask which machine they are talking to. This is also the start of Challenge 2: they finish it at home with references of their own.'))

S.append(question('image_upload', 'Scribes only. The chair, and what made it.',
                  hint='One image per four. Caption: the prompt, and which references — how many, whose, from which round.',
                  eyebrow_text='07 · CAPTURE 3 · IMAGE UPLOAD · ONE PER FOUR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='Scribes only, about 28 images, caption required. Put the three walls side by side: told (capture 1), shown two pictures (capture 2), references only (capture 3). Ask the room which wall has more chairs that are not the prototype. Read two captions: the inputs, not adjectives. Download the submissions: the chairs come back in week 5, when we push a model off the prototype properly, with ControlNet and fine-tuning.'))

S.append(content('07 · WHAT JUST HAPPENED', 'The prompt was you telling. The reference was you showing.',
                 ['The model has the examples. Your prompt was a rule it applied to the middle of them: it obeyed what selected and ignored what forbade. "Never" did not survive.',
                  'The reference was an example. It moved the middle: it could pull, it could mix, it could not forbid. Where the rule failed, the example worked.',
                  'And the other way round: the example could not ask for exactly four legs or a 40 cm seat. Where you needed a rule, the picture could not say it. Every tool is one of the two, or a mix, and you have to know which one you are talking to.',
                  '**The machine made every image. You chose the examples. That was the design.**'],
                 body_size=32,
                 notes='Mirror of the whole class. Tell: a rule, applied to examples; show: one more example. Where the rule failed and the example worked — the edge chair. Where the example failed and the rule worked — a count, a dimension, a "never". Say the last line slowly: it is week 1\'s last line, and week 2\'s, with the verb changed.'))

# ───────────────────────── 08 · challenge 2, homework ─────────────────────────
S.append(cards('08 · CHALLENGE 2 · DUE BEFORE WEEK 4', 'A picture from text and references.', [
    ('THE PROMPT', 'Tell it, in your words.',
     'One text prompt, kept word for word. Say what it selects and, if you dare, what it forbids: you will see what survived.'),
    ('THE REFERENCES', 'Show it, with your own pictures.',
     'One to three reference images: your photographs, your drawings, your week-1 cups or today\'s chairs. Not other people\'s work. Say what each one was for.'),
    ('THE RESULT', 'One image, on Blackboard.',
     'The image, the prompt, the references, and one sentence: where did the rule fail and the example work, or the other way round?'),
    ('THE VOTE', 'Bring it next week.',
     'The room votes in week 4; the winners get shown and a participation star. Evidence for your reflection: this is your second experiment of five.'),
], notes='Four things on Blackboard before next class: the image, the prompt, the references, one sentence. Own pictures only for the references; the model must be named. Next week the room votes. The one sentence is the reflection in miniature; tell them to write it while the difference is still fresh.'))

S.append(video('08 · HOMEWORK · WATCH BEFORE WEEK 4', 'Next week: language machines.', 'LPZh9BOjkQs',
               ['3Blue1Brown, "Large Language Models explained briefly": eight minutes on tokens, embeddings and transformers — the machine B that writes.',
                '- Watch it before class; the quiz in week 7 draws on it.',
                '- Bring the specs from week 2: next week they become briefs.',
                '- Also: a laptop, and your GenAI login.'],
               thumb='yt/LPZh9BOjkQs.jpg',
               notes='One video, short, on the playlist. Next week is the language model as a tool: tokens, embeddings, what a transformer does, hallucination and sycophancy, and prompting as briefing. The week-2 specs come back as briefs. Challenge 2 due before class; the TAs stay 30 minutes now.'))

S.append(end('See you next week. Language machines.',
             'Challenge 2 on Blackboard. Watch the 3Blue1Brown video. Bring a laptop.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Module one is done: two ways to teach a machine, and you have used both. Next week the tools begin with language. Homework in one line: the picture from text and references on Blackboard, the video, a laptop. The TAs stay for 30 minutes.'))

DECK = dict(title='SD2112 · AI in Design · Week 03', slides=finalize(S, FOOTER), pdf='SD2112-week03.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week03', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 5 September 2026 while writing this deck; every date, number and attribution above was checked against them)
# https://eric.ed.gov/?id=EJ128794 — Rosch (1975), Cognitive representations of semantic categories, J. Exp. Psych.: General 104(3), 192–233
# http://matt.colorado.edu/teaching/categories/rm75.pdf — Rosch & Mervis (1975), Family resemblances, Cognitive Psychology 7, 573–605
# https://en.wikipedia.org/wiki/Prototype_theory — typicality (robin vs penguin; chair as furniture), classical theory, basic levels
# https://linguistically.substack.com/p/eleanor-rosch-prototype-category — Rosch 1975 goodness-of-example ratings, 1–7 scale, ten categories
# https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00072/114924/Latent-Diversity-in-Human-Concepts — Labov (1973) cups/bowls: drawings varying in width and height, disagreement at the edge
# https://uobrep.openrepository.com/bitstream/handle/10547/625850/Prototype_Theory_an_evaluation.pdf — Labov (1973): coffee → cup, mashed potatoes → bowl; ratio of width to depth
# https://improbable.com/2017/02/23/is-it-a-mug-or-cup-recent-progress-in-fuzziness-studies/ — Labov cup/bowl/vase drawings
# https://en.wikipedia.org/wiki/Family_resemblance — Wittgenstein, Philosophical Investigations §66–67 (1953), the quoted phrases
# https://en.wikipedia.org/wiki/GOFAI and http://www-formal.stanford.edu/jmc/reviews/haugeland.html — Haugeland (1985), Artificial Intelligence: The Very Idea
# https://pubmed.ncbi.nlm.nih.gov/13602029/ — Rosenblatt (1958), Psychological Review 65(6), 386–408
# https://en.wikipedia.org/wiki/Perceptron — the learning rule, the Mark I (400 photocells, 20 × 20, motor-driven potentiometers), Minsky & Papert 1969
# https://theconversation.com/weve-been-here-before-ai-promised-humanlike-machines-in-1958-222700 — the New York Times, July 1958: "walk, talk, see, write, reproduce itself and be conscious of its existence"
# https://seantrott.substack.com/p/perceptrons-xor-and-the-first-ai — Minsky & Papert (1969), XOR, the funding winter
# https://www.nature.com/articles/323533a0 — Rumelhart, Hinton & Williams (1986), Learning representations by back-propagating errors, Nature 323, 533–536
# https://en.wikipedia.org/wiki/AlexNet — 30 Sept 2012, 15.3% vs 26.2% top-5 error, 60 M parameters, 8 layers, two GTX 580, 1.2 M images, 1,000 classes
# https://image-net.org/challenges/LSVRC/2012/results.html — ILSVRC 2012: SuperVision (a CNN on raw pixels) 15.3%; ISI, OXFORD_VGG, XRCE/INRIA, LEAR-XRCE on SIFT + Fisher vectors (26.2% and up)
# https://en.wikipedia.org/wiki/ImageNet — Fei-Fei Li, 2006 / CVPR 2009, 14 M images, 49,000 Mechanical Turk workers from 167 countries
# https://www.nobelprize.org/prizes/physics/2024/summary/ — Hopfield and Hinton, Nobel Prize in Physics 2024
# https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol — 9–15 March 2016, Four Seasons Seoul, 4–1, move 37 on 10 March (Redmond: creative, unique), move 78 in game 4, 18 international titles
# https://deepmind.google/research/alphago/ — "1 in 10,000 chance" of a human playing move 37; human games then self-play
# https://en.wikipedia.org/wiki/AlphaGo — ~30 million positions from expert games, self-play, Fan Hui 5–0 (Oct 2015), Silver et al. Nature Jan 2016, AlphaGo Zero (Oct 2017), Lee Sedol's retirement (Nov 2019)
# https://www.cnn.com/2019/11/27/tech/go-master-google-intl-hnk-scli and https://www.usgo-archive.org/news/2019/11/lee-sedol-retirement-reported-worldwide/ — the retirement quote ("an entity that cannot be defeated"), Yonhap
# https://en.wikipedia.org/wiki/AlphaGo_(film) — the film: 2017, Greg Kohs, 90 min
# https://www.sciencedirect.com/science/article/abs/pii/S0950705106000645 — Wiggins (2006), Knowledge-Based Systems 19(7), 449–458
# https://www.researchgate.net/publication/318494266_The_Creative_Mind_Myths_and_Mechanisms — Boden, The Creative Mind (1990; 2nd ed. 2004): combinational, exploratory, transformational
# https://www.figma.com/blog/announcing-auto-layout/ — Figma auto layout, December 2019
# https://www.figma.com/blog/config-2025-press-release/ — Figma Make, Config, 7 May 2025
# https://blog.adobe.com/en/publish/2023/05/23/future-of-photoshop-powered-by-adobe-firefly — Generative Fill, May 2023, Firefly trained on Adobe Stock
# https://qwenlm.github.io/blog/qwen-image-edit/ and https://bfl.ai/models/flux-kontext — Qwen-Image-Edit (Aug 2025) and FLUX.1 Kontext (May 2025): image models that take a reference image next to the text
# https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=WXuK6gekU1Y — "AlphaGo - The Movie | Full award-winning documentary" (Google DeepMind)
# https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=LPZh9BOjkQs — "Large Language Models explained briefly" (3Blue1Brown)
