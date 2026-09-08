"""
SD2112 · Artificial Intelligence in Design · Week 09 — the slide spec.

    python deck/week09.py            # builds _site/week09/ (html deck + pdf), export/week09*.pptx, export/preview/
    python deck/week09.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Data, bias and privacy: a dataset is a set of examples and the model's world is the dataset's
world; four doors where bias enters (data, labels, the objective and the threshold, interaction);
the threshold as a design decision and the fairness trade-off; privacy (minimisation, linkage and
re-identification, k-anonymity, consent and purpose, synthetic data); the neutrality debate voted
before and after; and the workshop: a bias register on each team's concept. Three live sketches
(the sampling window, the threshold, k-anonymity) with drawn twins in tools/figures_week09.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week09 as F                            # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, sketch_slide, code_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(9)
CHAIRS = [f'ai-chair-{i}.jpg' for i in range(1, 5)]   # week 1: one prompt, four seeds (deck/assets)

# ───────────────────────── live sketches (html deck) ─────────────────────────
# (a) the sampling window: 300 people, a hidden curved rule, a straight line fitted to what fell in the window
SAMPLE_JS = """// The model knows the window, not the world. 300 people in two colours follow a hidden curved rule;
// a rectangular window (the mouse) is the training set; a straight line is fitted to what fell inside it.
const N = 300, PW = 1000, PH = 500, WW = 360, WH = 200;
let pts = [], locked = false, wx = 600, wy = 250;
const rule = x => 250 + 110 * sin(x / 150 + 1.2);         // the true rule, which the model never sees

function setup() {
  createCanvas(1400, 500); randomSeed(9); textFont('JetBrains Mono');
  for (let i = 0; i < N; i++) {                             // unevenly spread: most people live top-left
    let x = random() < 0.65 ? random(40, 520) : random(40, PW - 40);
    let y = random() < 0.65 ? random(40, 260) : random(40, PH - 40);
    pts.push({ x, y, c: y < rule(x) ? 1 : 0 });             // 1 = teal, above the curve; 0 = orange, below
  }
}

function fit(s) {                                           // least squares on ±1 labels: one straight line
  let M = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]];
  for (let p of s) {
    let f = [1, p.x / PW, p.y / PH], t = p.c ? 1 : -1;
    for (let i = 0; i < 3; i++) { for (let j = 0; j < 3; j++) M[i][j] += f[i] * f[j]; M[i][3] += f[i] * t; }
  }
  for (let i = 0; i < 3; i++) M[i][i] += 1e-6;
  for (let c = 0; c < 3; c++) {                             // Gaussian elimination with pivoting
    let piv = c; for (let r = c + 1; r < 3; r++) if (abs(M[r][c]) > abs(M[piv][c])) piv = r;
    [M[c], M[piv]] = [M[piv], M[c]];
    if (abs(M[c][c]) < 1e-12) return null;
    for (let r = 0; r < 3; r++) if (r != c) { let k = M[r][c] / M[c][c]; for (let j = c; j < 4; j++) M[r][j] -= k * M[c][j]; }
  }
  return [M[0][3] / M[0][0], M[1][3] / M[1][1], M[2][3] / M[2][2]];
}
const guess = (w, p) => (w[0] + w[1] * p.x / PW + w[2] * p.y / PH > 0) ? 1 : 0;

function draw() {
  background(255);
  if (!locked) { wx = mouseX; wy = mouseY; }
  wx = constrain(wx, 40 + WW / 2, PW - 40 - WW / 2); wy = constrain(wy, 40 + WH / 2, PH - 40 - WH / 2);
  let x0 = wx - WW / 2, y0 = wy - WH / 2;
  noFill(); stroke(225); strokeWeight(1); rect(0.5, 0.5, PW - 1, PH - 1);
  stroke(200); strokeWeight(2); for (let x = 40; x < PW - 40; x += 12) point(x, rule(x));   // the rule, faintly
  const inWin = p => p.x >= x0 && p.x <= x0 + WW && p.y >= y0 && p.y <= y0 + WH;
  let sample = pts.filter(inWin), w = sample.length >= 3 ? fit(sample) : null;
  noStroke(); fill(251, 243, 236); rect(x0, y0, WW, WH); noFill(); stroke(0); strokeWeight(locked ? 4 : 2); rect(x0, y0, WW, WH);
  let wrongWorld = 0, wrongWin = 0;
  for (let p of pts) {
    let inside = inWin(p), wrong = w && guess(w, p) != p.c;
    if (wrong) { wrongWorld++; if (inside) wrongWin++; noFill(); stroke(210, 43, 43); strokeWeight(1.5); circle(p.x, p.y, 13); }
    noStroke(); if (inside) { stroke(0); strokeWeight(1); }
    fill(p.c ? '#64C2C3' : '#ED6D24'); circle(p.x, p.y, inside ? 9 : 6);
  }
  if (w) drawLine(w);
  panel(sample, w, wrongWin, wrongWorld);
}

function drawLine(w) {                                      // where w0 + w1 x + w2 y = 0 crosses the box
  let ends = [];
  if (abs(w[2]) > 1e-9) for (let x of [0, PW]) { let y = -(w[0] + w[1] * x / PW) * PH / w[2]; if (y >= 0 && y <= PH) ends.push([x, y]); }
  if (abs(w[1]) > 1e-9) for (let y of [0, PH]) { let x = -(w[0] + w[2] * y / PH) * PW / w[1]; if (x >= 0 && x <= PW) ends.push([x, y]); }
  if (ends.length >= 2) { stroke(0, 11, 28); strokeWeight(3); line(ends[0][0], ends[0][1], ends[1][0], ends[1][1]); }
}

function panel(s, w, wrongWin, wrongWorld) {
  noStroke(); fill(244, 244, 242); rect(PW, 0, width - PW, height);
  let x = PW + 30, teal = s.filter(p => p.c).length;
  textAlign(LEFT, BASELINE); fill('#ED6D24'); textSize(15); text('TRAINING SET · what fell in the window', x, 44);
  fill(0); textSize(30); text(s.length + ' people', x, 92);
  fill(92, 100, 112); textSize(15); text(teal + ' teal · ' + (s.length - teal) + ' orange', x, 118);
  fill('#ED6D24'); text('THE MODEL · one straight line', x, 172);
  if (!w) { fill(0); textSize(16); text('too few examples to learn from', x, 214); }
  else {
    let accWin = 100 * (1 - wrongWin / s.length), accWorld = 100 * (1 - wrongWorld / N);
    bar(x, 196, 'right in the window', accWin, color(0, 11, 28));
    bar(x, 276, 'right in the world', accWorld, color(237, 109, 36));
    fill(0); textSize(16);
    let v = teal == 0 || teal == s.length ? 'one kind of example: it says all ' + (teal ? 'teal' : 'orange')
          : accWin - accWorld > 15 ? 'it learned the window, not the world'
          : accWorld > 85 ? 'a fair sample: it learned the world' : 'a straight line; the world is curved';
    text(v, x, 384);
  }
  if (locked) { fill('#ED6D24'); textSize(15); text('LOCKED · click to release', x, 436); }
  else { fill(92, 100, 112); textSize(14); text('mouse = the window · click = lock it', x, 436); }
}
function bar(x, y, label, v, col) {
  fill(0); textSize(16); text(label, x, y + 14);
  fill(232, 232, 228); rect(x, y + 26, 300, 20); fill(col); rect(x, y + 26, 3 * v, 20);
  fill(0); textSize(17); text(round(v) + ' %', x + 312, y + 43);
}
function mousePressed() { locked = !locked; }"""

# (b) the threshold: two groups, one score, one line; the two ways to be wrong, per group
THRESHOLD_JS = """// Two groups, one score, one threshold. Above the line the product says YES.
// Mouse x moves the threshold. A click gives group 2 its own threshold, chosen so that the false-NO rates match.
const G = [{ name: 'GROUP 1 · the model is sure about them', yes: 0.55, mu: [66, 36], sd: 11 },
           { name: 'GROUP 2 · the model is less sure about them', yes: 0.45, mu: [58, 42], sd: 16 }];
const X0 = 80, X1 = 1320, ROW = [30, 222], RH = 122, BIN = 5;
let people = [[], []], separate = false;

function setup() {
  createCanvas(1400, 500); randomSeed(2018); textFont('JetBrains Mono');
  for (let g = 0; g < 2; g++) for (let i = 0; i < 200; i++) {
    let yes = random() < G[g].yes;                          // the truth: should this person get a YES?
    people[g].push({ yes, s: constrain(randomGaussian(G[g].mu[yes ? 0 : 1], G[g].sd), 0, 99.9) });
  }
}

function rates(g, t) {                                      // the two ways to be wrong, at threshold t
  let fp = 0, tn = 0, fn = 0, tp = 0;
  for (let p of people[g]) { if (p.s >= t) { p.yes ? tp++ : fp++; } else { p.yes ? fn++ : tn++; } }
  return { fpr: fp / max(1, fp + tn), fnr: fn / max(1, fn + tp) };
}
function matchedThreshold(t0) {                             // group 2's threshold with the same false-NO rate as group 1
  let want = rates(0, t0).fnr, best = t0, d = 9;
  for (let t = 0; t <= 100; t++) { let e = abs(rates(1, t).fnr - want); if (e < d) { d = e; best = t; } }
  return best;
}
const sx = s => map(s, 0, 100, X0, X1);

function draw() {
  background(255);
  let t = [round(constrain(map(mouseX, X0, X1, 0, 100), 0, 100)), 0];
  t[1] = separate ? matchedThreshold(t[0]) : t[0];
  let r = [rates(0, t[0]), rates(1, t[1])];
  for (let g = 0; g < 2; g++) {
    let y0 = ROW[g], base = y0 + RH, counts = [[], []], bw = (X1 - X0) / (100 / BIN);
    noStroke(); fill(237, 109, 36, 26); rect(sx(t[g]), y0, X1 - sx(t[g]), RH);        // the YES side
    for (let p of people[g]) { let b = floor(p.s / BIN), k = p.yes ? 1 : 0; counts[k][b] = (counts[k][b] || 0) + 1; }
    for (let b = 0; b < 100 / BIN; b++) {
      let x = sx(b * BIN), n0 = counts[0][b] || 0, n1 = counts[1][b] || 0;
      fill(150); rect(x + 4, base - 4 * n0, bw / 2 - 5, 4 * n0);
      fill('#64C2C3'); rect(x + bw / 2 + 1, base - 4 * n1, bw / 2 - 5, 4 * n1);
    }
    stroke(0); strokeWeight(1); line(X0, base, X1, base);
    stroke('#ED6D24'); strokeWeight(4); line(sx(t[g]), y0 - 8, sx(t[g]), base + 6);
    noStroke(); textAlign(LEFT, BASELINE); fill(0); textSize(15); text(G[g].name, X0, y0 - 14);
    fill('#ED6D24'); textAlign(sx(t[g]) > X1 - 160 ? RIGHT : LEFT); text('threshold ' + t[g], sx(t[g]) + (sx(t[g]) > X1 - 160 ? -8 : 8), y0 + 16);
    fill(92, 100, 112); textSize(13); textAlign(LEFT); text('score 0', X0, base + 18); textAlign(RIGHT); text('100', X1, base + 18);
    textAlign(CENTER); text('NO ←', sx(t[g]) - 30, base + 18); text('→ YES', sx(t[g]) + 34, base + 18);
  }
  fill(92, 100, 112); textSize(13); textAlign(RIGHT, BASELINE); text('grey: should get NO · teal: should get YES', X1, ROW[0] - 14);
  stats(r, t);
}

function stats(r, t) {
  let y = 388;                                              // the verdict line stays clear of the deck's LIVE chip
  for (let g = 0; g < 2; g++) {
    let x = X0 + g * 640;
    noStroke(); fill(0); textSize(15); textAlign(LEFT, BASELINE); text('GROUP ' + (g + 1) + ' · threshold ' + t[g], x, y);
    bar(x, y + 14, 'false YES', r[g].fpr, '#ED6D24'); bar(x + 300, y + 14, 'false NO', r[g].fnr, '#000B1C');
  }
  let dfp = abs(r[0].fpr - r[1].fpr) * 100, dfn = abs(r[0].fnr - r[1].fnr) * 100, gap = max(dfp, dfn);
  let msg = separate ? 'two thresholds: the false-NO rates match, and the false-YES rates now differ by ' + round(dfp) + ' points'
          : gap > 10 ? 'one threshold for everyone: the two groups’ error rates differ by ' + round(gap) + ' points'
          : 'one threshold for everyone: the two groups’ error rates are within 10 points';
  fill(gap > 10 || separate ? '#ED6D24' : '#5C6470'); textSize(16); textAlign(LEFT, BASELINE); text(msg, X0, y + 66);
  fill(92, 100, 112); textSize(13); text('mouse x = the threshold · click = one threshold per group', X0, y + 90);
}
function bar(x, y, label, v, col) {
  noStroke(); fill(92, 100, 112); textSize(13); textAlign(LEFT, BASELINE); text(label, x, y + 12);
  fill(232, 232, 228); rect(x + 92, y, 150, 14); fill(col); rect(x + 92, y, 150 * v, 14);
  fill(0); textSize(15); text(round(v * 100) + ' %', x + 252, y + 12);
}
function mousePressed() { separate = !separate; }"""

# (c) k-anonymity: twelve fictional patients, a neighbour who knows your age, district and sex, and k
ANON_JS = """// Anonymous means: at least k people look like you. Twelve fictional patients; the diagnosis is the secret.
// Mouse x sets k. Age, district and sex are generalised, one step at a time, until every row shares them with k − 1 others.
const ROWS = [[22, 'A', 'F', 'asthma'], [24, 'A', 'F', 'migraine'], [27, 'B', 'F', 'hay fever'], [29, 'B', 'F', 'eczema'],
              [41, 'E', 'M', 'back pain'], [43, 'E', 'M', 'asthma'], [46, 'F', 'M', 'insomnia'], [48, 'F', 'M', 'flu'],
              [61, 'C', 'M', 'fracture'], [63, 'C', 'M', 'migraine'], [66, 'D', 'M', 'hay fever'], [68, 'D', 'M', 'insomnia']];
const STEPS = ['age → 10-year band', 'district → region', 'sex → *', 'age → 20-year band', 'age → *', 'district → *'];
const YOU = 6;                                              // row 7: the person a neighbour is looking for

function view(r, L) {                                       // the row as released at generalisation level L
  let [age, d, s] = r, b10 = floor(age / 10) * 10, b20 = floor(age / 20) * 20;
  let a = L >= 5 ? '*' : L >= 4 ? b20 + '–' + (b20 + 19) : L >= 1 ? b10 + '–' + (b10 + 9) : '' + age;
  let dd = L >= 6 ? '*' : L >= 2 ? (d <= 'D' ? 'North' : 'South') : d;
  return [a, dd, L >= 3 ? '*' : s];
}
function sizes(L) {                                         // how many rows share each released key
  let n = {};
  for (let r of ROWS) { let k = view(r, L).join('|'); n[k] = (n[k] || 0) + 1; }
  return ROWS.map(r => n[view(r, L).join('|')]);
}

function setup() { createCanvas(1400, 500); textFont('JetBrains Mono'); }

function draw() {
  background(255);
  let k = 1 + floor(constrain(mouseX / width, 0, 0.999) * 6);
  let L = 0; while (L < 6 && min(sizes(L)) < k) L++;       // the least generalisation that reaches k
  let g = sizes(L), unique = g.filter(v => v == 1).length, me = view(ROWS[YOU], L).join('|');
  let twins = ROWS.filter(r => view(r, L).join('|') == me);
  // the table
  textAlign(LEFT, BASELINE); noStroke();
  fill('#ED6D24'); textSize(14);
  [['#', 30], ['age', 90], ['district', 250], ['sex', 450], ['diagnosis', 560]].forEach(([h, x]) => text(h, x, 60));
  stroke(0); strokeWeight(1); line(30, 70, 780, 70);
  for (let i = 0; i < 12; i++) {
    let y = 100 + i * 30, v = view(ROWS[i], L), same = view(ROWS[i], L).join('|') == me;
    noStroke();
    if (same) { fill(i == YOU ? '#FBE2D3' : '#F4F4F2'); rect(20, y - 21, 770, 30); }
    textSize(17); fill(92, 100, 112); text(i + 1, 30, y);
    fill(L >= 1 ? '#ED6D24' : 0); text(v[0], 90, y);
    fill(L >= 2 ? '#ED6D24' : 0); text(v[1], 250, y);
    fill(L >= 3 ? '#ED6D24' : 0); text(v[2], 450, y);
    fill(0); text(ROWS[i][3], 560, y);
    if (i == YOU) { fill('#ED6D24'); textSize(13); text('← you', 700, y); }
  }
  // the panel
  fill(244, 244, 242); rect(820, 0, 580, 500);
  let x = 850;
  fill('#ED6D24'); textSize(15); text('K-ANONYMITY', x, 44);
  fill(0); textSize(44); text('k = ' + k, x, 96);
  textSize(15); fill(92, 100, 112);
  text(k == 1 ? 'no protection: rows are released as they are' : 'every row shares its age · district · sex', x, 126);
  if (k > 1) text('with at least ' + (k - 1) + ' other row' + (k > 2 ? 's' : ''), x, 148);
  fill('#ED6D24'); text('GENERALISED', x, 196);
  fill(0); textSize(16);
  let done = STEPS.slice(0, L), lines = L == 0 ? ['nothing'] : [done.slice(0, 3).join(' · '), done.slice(3).join(' · ')].filter(s => s);
  lines.forEach((s, i) => text(s, x, 222 + i * 22));                            // three steps per line
  fill('#ED6D24'); textSize(15); text('UNIQUE ROWS', x, 278);
  fill(0); textSize(28); text(unique + ' of 12', x, 313);
  fill('#ED6D24'); textSize(15); text('A NEIGHBOUR WHO KNOWS YOU ARE 46, DISTRICT F, M', x, 356);
  fill(0); textSize(16);
  text(twins.length == 1 ? 'finds one row: ' + ROWS[YOU][3] + '. That is your diagnosis.' : 'narrows it to ' + twins.length + ' rows:', x, 382);
  if (twins.length > 1) { fill(92, 100, 112); text(twins.length == 12 ? 'all 12 rows: every diagnosis in the table' : twins.map(r => r[3]).filter((d, i, a) => a.indexOf(d) == i).join(', '), x, 406); }
  fill(twins.length == 12 ? '#ED6D24' : 92); textSize(14);
  text(L == 6 ? 'anonymous — and the table says nothing any more' : L == 0 ? 'a name is not the only name' : 'the price: ' + L + ' column step' + (L > 1 ? 's' : '') + ' lost', x, 446);
  fill(92, 100, 112); text('mouse x = k, from 1 (left) to 6 (right)', x, 480);
}"""

REGISTER = [
    'BIAS REGISTER · team · product', ' ',
    'one row per decision:', ' ',
    '1  THE DECISION', '   a verb and a person', ' ',
    '2  THE DATA', '   what it learns from; where it came', '   from; who collected it', ' ',
    '3  WHO IS THIN IN THE DATA', '   a real group of people', ' ',
    '4  THE HARM WHEN WRONG', '   false yes → ?    false no → ?', ' ',
    '5  THE GUARDRAIL', '   the rule that catches it;', '   who a person can appeal to',
]

STANDUP_PANEL = [
    'THE STAND-UP · THREE QUESTIONS · STANDING', ' ',
    '1  what did I do since last class?',
    '2  what will I do before the next?',
    '3  what is in my way?', ' ',
    "THIS SPRINT'S ITEM: THE PROPOSAL",
    '   one page, on Blackboard: the decision, for whom,',
    '   the data you have and do not have, the wrong day.',
    '   open it: it is the case for the whole day.', ' ',
    'the backlog: one item on top for this week —',
    '   the concept board and the bias register.', ' ',
    'the scribe writes five names, three lines each.',
    'the TAs walk: Amber answers every proposal.',
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 09 · LECTURE + WORKSHOP',
               'Data, bias and privacy.',
               'Week 9 — the model’s world is the dataset’s world.',
               notes='Join code on screen from 30 minutes before. Sit with your team from the start: the stand-up is the first thing that happens, the last hour is the register, done as a team, and the first ClassPoint question is about the film. Anyone who has not watched Coded Bias watches the first twenty minutes at the break on a phone; it is not optional for the group project.'))

S.append(agenda('SD2112 · WEEK 09', [
    'Last week, in your words', 'A dataset is a set of examples', 'Four doors for bias', 'The threshold',
    'Privacy: collect, link, keep', 'Can a model be neutral?', 'The bias register', 'Activity: map the ethics of your concept',
], notes='Eight stops. The stand-up first, at your table, twelve minutes, then the film. Stops two to four are the lecture: what a dataset is and why the model only ever knows the window; the four doors where bias comes in; and the threshold, one number that decides who pays for the model’s mistakes. Break. Then privacy, the debate, and the workshop: your own product, one row per decision, five columns, and a red pen from the team next to you. Two votes on the same question, one now and one at the end.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the stand-up · Coded Bias · your proposals · the map', bg=ORANGES[0],
                 notes='Chapter one: the stand-up at the team table — twelve minutes, the first of six — then the film you watched, the proposals you wrote, and where we are.'))

S.append(activity('STAND-UP', 12, 'Three questions, standing.',
                  ['At your table, standing, one minute per person: **what I did, what I will do, what is in my way.**',
                   'Then the increment: open **the proposal** you uploaded and read the data line aloud — what you have, what you do not. It is the case for the whole day.',
                   'Put one item on top of the backlog for this week. The scribe writes it down. The TAs walk; Amber answers every proposal.'],
                  eyebrow_text='01', panel=STANDUP_PANEL, panel_size=20, bg=YELLOWS[0],
                  notes='Twelve minutes, standing, at the team table: the first stand-up of six, as promised last week. Nicolò keeps the time on the slide; the other three TAs walk with one question each — what is the data, and do you have it? Amber has read every proposal and gives each team one sentence back. The rule from week 8: show the thing, not the plan; today the thing is one page. Teams that are late miss their own meeting; anyone whose team is not here goes to Amber. The "data you need and do not have" line from last week comes back in the register, so keep the proposal open.'))

S.append(question('word_cloud', 'Coded Bias: one word that stayed with you.',
                  hint='The film was the homework. One word: a scene, a person, a feeling, a question.',
                  eyebrow_text='01 · QUESTION · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each; leave it on screen for a minute. Expect: mask, face, camera, police, Brooklyn, scary, data, China. Read the three biggest aloud and ask one person for the scene behind their word. Screenshot it: it comes back on the three-positions slide after the break, next to the engineer, the philosopher and the designer. If the cloud is thin, the room did not watch it — say the twenty-minute rule now, without blame.'))

S.append(content('01 · CODED BIAS · SHALINI KANTAYYA · 2020', 'A face the camera could not see.',
                 ['Joy Buolamwini, MIT Media Lab: the face-tracking software in her project found her face only when she put on a white mask. She went looking for the reason and found the dataset.',
                  '- **Gender Shades, 2018**, with Timnit Gebru: three commercial gender classifiers tested on 1,270 parliamentarians. Error rates up to 34.7 % for darker-skinned women; at most 0.8 % for lighter-skinned men.',
                  '- The film follows the finding out of the lab: a police van in London, tenants in Brooklyn fighting a face-recognition lock on their building, a hearing in Washington.',
                  'Not seen it yet? Ninety minutes, Sundance 2020. On Netflix since April 2021; PBS Independent Lens premiere March 2021. Watch it before the project goes further.'],
                 body_size=28,
                 notes='Three things to say. The mask: the software was not broken, it had learned faces from a dataset that looked like its makers. The numbers: Gender Shades is an audit — a balanced test set, three products, one table — and within seven months all three companies shipped better versions; measuring is a design act. The film: Buolamwini takes the finding to the people it lands on. Where to watch: Netflix lists it — check that it plays from Hong Kong before class, or ask the library for a licence; the PBS page is the US broadcast, background only. No clips today: the film is the homework, not the lecture.'))

S.append(question('multiple_choice', 'Can a model be neutral?', [
    'Yes: the maths is neutral, the data is the problem', 'No: every dataset and every threshold is a choice', 'Only if a person checks every decision', 'Wrong question: neutral for whom?',
], eyebrow_text='01 · STANCE · VOTE 1 OF 2 · MULTIPLE CHOICE',
    notes='ClassPoint, thirty seconds, no discussion yet. There is no correct answer; screenshot the split. This is vote one of two: the same question comes back at the very end, after they have mapped their own product, and the movement between the two is the point of the day. Most rooms start with a majority on A. Say nothing about it.'))

S.append(cards('01 · YOUR PROPOSALS · ONE PAGE, LAST WEEK', 'Every proposal has three parts. Today is the third.', [
    ('THE DECISION', 'What the model decides.', 'Which lamp, which song, which route, which price, whose face gets in. Most of you wrote this part well: a verb and a person.'),
    ('FOR WHOM', 'Who gets the decision.', 'Each person, on their own. That is what makes it incorporating rather than using: the product behaves differently for you than for me. Weeks 8 and 10.'),
    ('WITH WHAT DATA', 'What it learns from.', 'The column most proposals left thin: "user data", "the internet", "our app". Today we open that column and look for the people who are not in it.'),
], notes='Replace the quotes in the third card with three real phrases from the proposals, no team names. The point is not to scold: nobody knows what the data is yet, because nobody has asked who is in it. By the end of the day every team has a register that says. Amber has the proposals and answered each one at the stand-up; the ones that already named a dataset get a mention.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(3, 1),
                 notes='Week 9, the middle of module three. Last week the model became a material; this week the material turns out to be people. Next week the feed: recommendation systems, and the interaction loop we meet today at door four. Concept board and bias register are due after this class; prototype v1 starts now and is shown, as it stands, at the week-10 stand-up.'))

# ───────────────────────── 02 · a dataset is a set of examples ─────────────────────────
S.append(section('02', 'A dataset is a set of examples', 'the window · the world · whose chair', bg=INK,
                 notes='Chapter two: what a dataset is, mechanically, and the sentence of the day.'))

S.append(statement('The model’s world is the dataset’s world.', eyebrow_text='02 · THE SENTENCE OF THE DAY', size=116,
                   notes='Machine B, from week 3: show the examples and it develops a feel. Everything it will ever know about chairs, faces, tiredness or taste is in the examples, and the examples were collected by someone, somewhere, for some reason. Nothing outside the dataset exists for the model. Say it twice; it comes back at every door.'))

S.append(cards('02 · ANATOMY OF A DATASET', 'Examples, labels, a window, a purpose.', [
    ('THE EXAMPLES', 'Rows.', 'Photos, sentences, clicks, sensor readings. Each one is a person or a thing, caught once, from one angle. A dataset is never the world; it is what was collectable.'),
    ('THE LABELS', 'What each row is called.', '"chair", "spam", "tired", "high risk". Somebody wrote the list of allowed words and somebody applied them, fast, thousands of times. The label is the concept.'),
    ('THE WINDOW', 'Where the collector looked.', 'A city, a language, a decade, a beta group, the most-photographed side of the web. The model learns the window and calls it the world.'),
    ('THE PURPOSE', 'Why it was collected.', 'Gebru et al., 2018: datasets should ship with a datasheet — motivation, composition, collection, labelling, intended uses. Reuse for a new purpose is where privacy law starts, after the break.'),
], text_size=21, notes='Four parts of any dataset, and the vocabulary for the whole day. Examples and labels are the two machines of week 3 in another form: the labels are a rule written by a person, the examples are what the model generalises from. The window is the new word: every dataset has one, and the register asks you to name yours. Datasheets for Datasets: an electronics idea — every component ships with its specs — applied to data. Ask: does the dataset behind your proposal have one? Almost never.'))

S.append(figure_slide('02 · THREE TEAMS, ONE WORLD', 'Three windows. Three rules. One world.', F.w09_windows(),
                      body=['Same 300 people, same hidden rule. Each team collected examples where it happened to look and trained the same kind of model on them. A model is only ever as wide as its window.'],
                      caption='The drawn twin of the live sketch on the next slide: a straight line fitted by least squares to whatever fell inside the window. A red ring is a person the line gets wrong.',
                      notes='Walk through the three. Team A looked at the crowded corner: high accuracy inside, decent outside, because the corner happens to look like most of the world. Team B looked at the far edge: twelve people, a line that is right for them and wrong for two thirds of everyone else. Team C looked at nearly everyone and still gets a tenth wrong, because the world is curved and the rule is a line — a different limit, not a data one. Ask: which team would notice the problem from inside its own window? None. That is why you test outside it.'))

S.append(sketch_slide('02 · LIVE · THE WINDOW', 'The model knows the window, not the world.',
                      live('w09-sample', SAMPLE_JS, 1400, 500, hint='move the mouse = move the window · click = lock it'),
                      caption='300 people, two colours, a hidden curved rule. Whatever falls in the window is the training set; the line is the model; the panel counts how often it is right inside the window and out in the world.',
                      notes='Drive it slowly. Park the window in the crowded corner: the line is confident and mostly right. Slide it to the far right: the same fit, the same confidence, and the world accuracy collapses. Find a spot where the window holds only one colour: the model says everyone is teal and is very sure. Then lock it and ask the room where they would put the window if they could only afford one. The honest answer is: two windows, and a test outside both. In the PowerPoint this slide is a still; the html deck runs it.'))

S.append(content('02 · WEEK 1, REVISITED', 'Whose chair was it?',
                 ['"A chair", four times, one model: four legs, a back, black steel tube, a grey seat, catalogue lighting. Nobody typed "black" or "steel".',
                  '- It learned "chair" from web pictures with the word nearby. The web’s most photographed chair became its middle.',
                  '- **LAION-5B, 2022:** 5.85 billion image–text pairs, filtered by another model, behind Stable Diffusion. Nobody chose the chairs.',
                  '- Bloomberg, 2023: 5,000+ Stable Diffusion images of jobs. Lighter skin for every high-paying job; darker skin for "fast-food worker".',
                  'Your prompt was the rule. The dataset was the window.'],
                 images=CHAIRS, caption='Week 1: "a chair, studio product photograph, plain white background" — one model, four seeds.',
                 body_size=25,
                 notes='The chairs from week 1, now with the vocabulary. The prototype was not Hong Kong’s chair and not yours: it was the dataset’s, and the dataset was the web as scraped in 2022, filtered by a model that kept what looked like a good caption. LAION-5B is the window behind most open image models; nobody curated it, which is the point — the middle of five billion captions is a very particular middle. The Bloomberg study is what that middle does to people: they asked for jobs and got a hierarchy. Same mechanism as the chairs, higher stakes. Week 11 comes back to datasets as something you curate.'))

S.append(question('multiple_choice', 'Why did the model give four almost identical chairs?', [
    'It has taste', 'The prompt asked for that chair', 'That is the most typical chair in its dataset', 'The seed was the same',
], eyebrow_text='02 · QUICK CHECK · MULTIPLE CHOICE',
    notes='C. The seeds were different (D is wrong: four seeds, four images), the prompt said nothing about wood or legs (B), and taste is what we call it when the middle agrees with us (A). The model’s middle is the dataset’s middle. Anyone who answers A gets the follow-up: whose taste?'))

# ───────────────────────── 03 · four doors ─────────────────────────
S.append(section('03', 'Four doors', 'data · labels · the objective · interaction', bg=ORANGES[0],
                 notes='Chapter three: bias is not one thing. Four doors, four different mistakes, four different fixes.'))

S.append(figure_slide('03 · WHERE BIAS ENTERS', 'Bias enters through four doors.', F.w09_doors(),
                      caption='The data loop of a product that decides something for each person. A different mistake at each door, and a different fix — which is why the register has a column for the data and a column for the guardrail.',
                      notes='Read the loop left to right, then the return arrow. Door one: who got collected. Door two: what they were called. Door three: what the model was told to want, and where the yes/no line was drawn. Door four: the product ships, people react, the reactions become tomorrow’s data — the loop closes and the product starts teaching itself from its own behaviour. One slide per door now; the threshold half of door three gets its own chapter.'))

S.append(cards('03 · DOOR 1 · DATA BIAS', 'Who is in the dataset. Who is not.', [
    ('GENDER SHADES · 2018', 'The benchmark was the bias.', 'Buolamwini and Gebru built a balanced test set: 1,270 parliamentarians from three African and three European countries. Three commercial gender classifiers: up to 34.7 % error for darker-skinned women, at most 0.8 % for lighter-skinned men. Within seven months all three companies shipped better versions.'),
    ('AMAZON · 2014 – 2017', 'Ten years of CVs, mostly men.', 'A recruiting model trained on a decade of applications learned the pattern of the past and marked down CVs containing the word "women’s" and graduates of two women’s colleges. Reuters, 2018: the tool was scrapped.'),
    ('YOUR PRODUCT', 'The beta testers.', 'A model trained on the twenty people who tried the prototype learns those twenty: their language, their hours, their city. Who was not in the room? That is the third column of the register.'),
], text_size=21, notes='Door one is the window. Gender Shades: the products worked on the faces they had been shown, and the faces they had been shown were mostly lighter-skinned men; the fix was not a better algorithm, it was a better test set and a public table. Amazon: the data was the company’s own history, and history is not a neutral source of examples — a model trained to find "people like our best hires" finds people like the past. Your product: the twenty beta testers are a window. Ask two teams who their testers are; the answer is almost always "us".'))

S.append(cards('03 · DOOR 2 · LABEL BIAS', 'Who named the examples, with which words.', [
    ('IMAGENET · 2009 – 2019', 'A "person" branch with 2,832 categories.', 'Fourteen million web images, labelled by crowd workers on Mechanical Turk for a few cents each. Crawford and Paglen, Excavating AI, 2019: the person categories included insults applied to photos of strangers. ImageNet removed more than 600,000 images that year.'),
    ('GOOGLE PHOTOS · 2015', 'The fix was to delete the label.', 'The app tagged two Black users as "gorillas". The repair, still in place years later: the word was removed from the tagger. A guardrail, not a cure — the model did not change.'),
    ('YOUR PRODUCT', 'Who says what "tired" looks like?', 'Every label is a decision by a person with a deadline and a list of allowed words. Whoever writes the list writes the concept. Weeks 1 and 3: the prototype, and the edge nobody labelled.'),
], text_size=21, notes='Door two is the rule inside machine B: the label is a word chosen by a person, applied at speed. ImageNet is the dataset that started deep learning in 2012, and its person branch was a taxonomy of slurs and judgements nobody had looked at until two artists did. Google Photos: the label was wrong and racist; the fix was to forbid the word, which is a rule protecting people from a model — a guardrail, our word for the last column. Your product: whoever decides what counts as tired, good, relevant, risky has written the concept. Ask the teams: who labelled your examples? Usually nobody has yet, which means the team will, which means the team’s idea of tired is the model’s.'))

S.append(content('03 · DOOR 3 · ALGORITHMIC BIAS', 'The objective is what the model is told to want.',
                 ['A model does not want fairness. It wants the number it was given: clicks, watch time, "the point the eye goes to".',
                  '- **Twitter, 2018 – 2021:** a saliency model, trained on eye-tracking data, cropped every photo to its most looked-at point. Twitter’s own audit in 2021: the crops favoured women over men by 8 points and white faces over Black faces by 4; the "male gaze" users had reported did not show up in the test — the disparity was there without it.',
                  '- Twitter removed the automatic crop and let people choose. Rumman Chowdhury: "how to crop an image is a decision best made by people."',
                  '- The objective was innocent: where do eyes go. The product was not. And after the objective comes the second half of door three: where the yes/no line is drawn. Next chapter.'],
                 body_size=30,
                 notes='Door three, first half: the objective. Nobody at Twitter wrote a rule about skin; they wrote a rule about attention, trained it on where eyes had gone, and shipped the crop. Attention is not neutral, so the crop was not. The numbers, if asked: demographic parity, 8 points in favour of women over men and 4 in favour of white over Black individuals; and the crop landed away from a head in no more than 3 images per 100, on things like a jersey number, the same for both genders — no evidence of the "male gaze" people had reported, which is the honest half of the finding. The fix is a design decision, not a model one: give the crop back to the person. Note the shape of that fix — it is the same shape as the guardrail column: the model proposes, the person decides. The other half of door three is the threshold, and it needs its own chapter because it is the one you will sign.'))

S.append(cards('03 · DOOR 4 · INTERACTION BIAS', 'The product learns from what we do with it.', [
    ('TAY · MARCH 2016', 'Sixteen hours.', 'Microsoft’s chatbot learned from the people who talked to it. A group of users fed it abuse on purpose; within sixteen hours it was repeating it, and Microsoft switched it off.'),
    ('PREDPOL · OAKLAND · 2016', 'Predicting policing, not crime.', 'Lum and Isaac fed a predictive-policing model the city’s drug-arrest records. It sent patrols back to the neighbourhoods already patrolled; the new arrests confirmed the prediction. A loop.'),
    ('YOUR FEED · EVERY DAY', 'It shows what you click. You click what it shows.', 'Sweeney, 2013: searching a first name more common among Black Americans was 25 % more likely to bring up an ad suggesting an arrest record. Nobody wrote that rule; clicks trained it. Week 10 is this loop in full.'),
], text_size=21, notes='Door four is the return arrow: the product’s own behaviour becomes its training data. Tay is the fast version — a model that learns live from whoever shows up. PredPol is the slow version: the model does not predict crime, it predicts where the police recorded crime, sends them there, and the records grow where it pointed. Sweeney’s ads: the ad system learned which copy got clicked next to which names; the people clicking taught it a prejudice nobody typed. Ask: what does your product learn from after it ships? If the answer is "nothing", it is frozen and will drift out of date; if the answer is "usage", door four is open.'))

S.append(question('multiple_choice', 'A photo app learns from what you favourite, and slowly stops showing you photos of your grandmother. Which door?', [
    'Data bias', 'Label bias', 'Algorithmic bias', 'Interaction bias',
], eyebrow_text='03 · QUICK CHECK · MULTIPLE CHOICE',
    notes='D. The app was fine on day one; it learned from your taps, you tap what it shows, and the loop narrowed. Someone will argue C, the objective — "maximise favourites" — and they are half right: door four only closes because door three told the model to want taps. Good answer; give the star to both if the reasoning is out loud.'))

# ───────────────────────── 04 · the threshold ─────────────────────────
S.append(section('04', 'The threshold', 'one number · two ways to be wrong · the trade-off', bg=INK,
                 notes='Chapter four: the number that turns a score into a decision, and the one you will be asked to sign.'))

S.append(figure_slide('04 · ANATOMY', 'Above the line, yes. Below it, no. Two ways to be wrong.', F.w09_threshold_anatomy(),
                      body=['The model gives everyone a score. A threshold turns the score into a decision. Every threshold makes two kinds of mistake, and moving it trades one for the other. If the model is less sure about one group, that group makes more of both.'],
                      caption='Two groups, same rule, same threshold at 60. Group 2’s curves are wider — the model is less sure about them, which is Gender Shades in a picture — so more of them land on the wrong side of the line.',
                      notes='Vocabulary first. Score: the model’s number for a person. Threshold: the line. False yes: the product lets through someone it should not — a spam email in your inbox, a loan that defaults, a stranger through the door. False no: it turns away someone it should not — your own email in the spam folder, a loan refused to someone who would have paid, you locked out of your own building. Move the line right and false yeses fall while false noes rise. Now the two panels: same line, and group two pays more of both, because the model is less sure about them. Nobody chose that; the dataset did.'))

S.append(sketch_slide('04 · LIVE · THE THRESHOLD', 'Move the line. Watch who pays.',
                      live('w09-threshold', THRESHOLD_JS, 1400, 500, hint='mouse x = the threshold · click = one threshold per group'),
                      caption='Two groups of 200, scored by the same model. Grey: people who should get NO; teal: people who should get YES. The bars are the error rates; the message appears when the groups differ by more than ten points.',
                      notes='Slide the line from left to right and narrate the bars: on the left everyone gets YES, no false noes, many false yeses; on the right the reverse. Somewhere in the middle both are small for group one and neither is small for group two. Then click: group two gets its own threshold, chosen so that the false-NO rates match — equal opportunity, Hardt 2016 — and watch its false-YES rate rise instead. There is no position where both bars match for both groups. That is not a bug in the sketch; it is a theorem, next slide.'))

S.append(cards('04 · COMPAS · 2016', 'Both sides were right. That is the problem.', [
    ('PROPUBLICA', 'The errors fall unequally.', 'Machine Bias, May 2016: 7,214 defendants in Broward County, Florida, followed for two years. Of those who did not reoffend, 45 % of Black defendants had been scored higher risk against 23 % of white defendants. White reoffenders were labelled low risk almost twice as often.'),
    ('NORTHPOINTE', 'The scores mean the same thing.', 'The company’s reply: at each score, Black and white defendants went on to reoffend at about the same rate. Calibrated, by their measure. Both measures are called fairness.'),
    ('THE THEOREM', 'You cannot have both.', 'Kleinberg, Mullainathan and Raghavan (2016) and Chouldechova (2017): when two groups have different base rates, no score can be calibrated and have equal error rates at the same time. Choose. Say which.'),
], text_size=21, notes='The case every fairness paper cites. COMPAS scored defendants for the risk of reoffending; judges saw the score. ProPublica measured error rates by group and found them unequal. Northpointe measured calibration — does a 7 mean the same thing for everyone — and found it equal. Then four researchers — Kleinberg, Mullainathan and Raghavan, and Chouldechova on her own — showed that with different base rates you cannot have both; the two fairnesses contradict each other. The design lesson is not "the maths is broken". It is that "fair" was never one number, and somebody has to pick which one and write it down. That is a design decision, and in your register it is the guardrail column.'))

S.append(content('04 · EQUAL THRESHOLDS, OR EQUAL ERROR RATES', 'Choose which "equal" you mean. Then say so.',
                 ['- **Same threshold for everyone.** Equal treatment on paper; the group the model is less sure about pays in both errors.',
                  '- **Same error rates for everyone.** Hardt, Price and Srebro, 2016: move each group’s threshold until the false-no rates match. The cost moves from the group to the company, which now has a reason to build a better model.',
                  '- **A better model.** The Gender Shades answer: fix the data, retest, publish. Slow, and the only one that closes the gap instead of moving it.',
                  '- **A person in the loop.** Send the uncertain band to a human. Which human, how fast, and can they overrule the score?',
                  'Google’s 2016 explorable by Wattenberg, Viégas and Hardt let you drag the thresholds; our sketch is the small version.'],
                 body_size=28,
                 notes='Four things a team can actually do, none of them free. One threshold is what you get by default, and the default is a decision too. Equal error rates is the sketch two slides back, click mode: it is a rule you add on top of machine B — machine A guarding machine B — and it shifts the cost onto the company, which is the incentive Hardt wants. A better model is the only real fix and takes months. A person in the loop is the one most products ship, and the register asks the two questions that make it real: who, and can they say no. Then the poll.'))

S.append(question('multiple_choice', 'Your model is less sure about one group of users. What ships?', [
    'One threshold for everyone', 'A threshold per group, so the error rates match', 'Nothing, until the model is equally good', 'The uncertain cases go to a person',
], eyebrow_text='04 · STANCE · MULTIPLE CHOICE',
    notes='No single right answer; show the split and ask one person per letter to defend it in a sentence. B is the equal-opportunity move and someone will object that it treats groups differently on purpose — yes, that is what it does, on purpose, and it is legal in some places and not others. C is Gender Shades and it costs a launch. D is what most products do and the follow-up is: who is the person, and what happens to the queue at 3 a.m.? A is the default, and the point of the chapter is that a default is a decision.'))

S.append(statement('A threshold is a design decision. Someone signs it.', eyebrow_text='04 · WHERE WE ARE', size=110,
                   notes='The sentence to carry across the break. The model gives a number; a person decides what the number means, where the line goes, and who pays for the mistakes on each side. In your mediation brief, that person is you. After the break: what the dataset knows about people that it should not, and the debate.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · PRIVACY · THE DEBATE · THE REGISTER', size=120, bg=PAPER,
                   notes='1:23. Teams sit together after the break; the last hour is the register. Anyone who has not seen Coded Bias: the first twenty minutes now, on a phone, with headphones.'))

# ───────────────────────── 05 · privacy ─────────────────────────
S.append(section('05', 'Privacy', 'collect less · link less · keep less · ask', bg=ORANGES[0],
                 notes='Chapter five: the data is people. Four principles, two laws, one attack, one defence, and the synthetic escape route that is not one.'))

S.append(cards('05 · FOUR PRINCIPLES, TWO LAWS', 'Collect less. Say why. Keep less. Ask.', [
    ('DATA MINIMISATION', 'Only what the decision needs.', 'GDPR art. 5(1)(c): "adequate, relevant and limited to what is necessary". Hong Kong PDPO, DPP1: "adequate but not excessive". A sign-up form is a data policy; every field is a claim about the decision.'),
    ('PURPOSE LIMITATION', 'Collected for one thing, used for that thing.', 'GDPR 5(1)(b): "specified, explicit and legitimate purposes". PDPO DPP3: no new purpose without the person’s express and voluntary consent. Training a model on old support tickets is a new purpose.'),
    ('STORAGE LIMITATION', 'Not a day longer than needed.', 'GDPR 5(1)(e); PDPO DPP2: not kept "longer than is necessary". Every month of logs is a month more to leak and a month more to subpoena. Deletion is a feature you design.'),
    ('CONSENT AND OVERSIGHT', 'Informed, specific, revocable.', 'PDPO in force since 1996, GDPR since 2018. The PCPD’s 2024 AI framework asks the same of models: a governance structure, a risk assessment, human oversight, and stakeholders who are told.'),
], text_size=20, notes='Principles, not law school. Two regimes say the same four things: collect only what you need, for a purpose you stated, keep it only as long as that purpose lasts, and ask. Hong Kong’s ordinance is older than most of the room; the six data protection principles are on the PCPD site and the 2024 framework is the local guidance for anyone shipping a model. The designer-facing version: the sign-up form is where minimisation is decided, the privacy policy is where purpose is stated, the settings page is where consent is revoked — all three are screens you draw. Then the anonymous question.'))

S.append(question('short_answer', 'Name one thing your product could stop collecting tomorrow.',
                  hint='One field, one sensor, one log. Would the decision still work without it? Names are hidden.',
                  eyebrow_text='05 · QUESTION · SHORT ANSWER · ANONYMOUS',
                  cp={'type': 'short_answer', 'hide_names': True, 'multiple': False},
                  notes='Ninety seconds, anonymous. Read six. Typical answers: location, contacts, exact birth date, the camera, "everything we log just in case". For each one ask the room: would the decision still work? Usually yes. That is data minimisation as a design exercise: start from the decision and work backwards to the fields. Keep the list; it goes into the register’s data column.'))

S.append(figure_slide('05 · RE-IDENTIFICATION', 'No names, and still you.', F.w09_linkage(),
                      caption='Latanya Sweeney, then a graduate student, linked "anonymised" hospital records to the public voter roll of Cambridge, Massachusetts, and found the governor’s records. The records above are fictional.',
                      notes='Removing the name column is what most people mean by anonymising, and it does not work. The left table has no names. The right table is public. Three columns appear in both, and together they pick out one person — ZIP code, birth date, sex — which is how Sweeney, in the nineties, found Governor Weld’s hospital records in a dataset the state had released as anonymous. The lesson for your product: any column that is rare in your data and public somewhere else is a name. Say the word: quasi-identifier.'))

S.append(statement('87 % of Americans could be picked out by ZIP code, birth date and sex.', eyebrow_text='05 · LATANYA SWEENEY · 2000 · ON THE 1990 CENSUS', size=100,
                   notes='Sweeney, 2000: on the 1990 census, 87 % of the US population — 216 of 248 million — was unique on those three fields. Golle redid it on the 2000 census in 2006 and got 63 %. Either number is the end of "we removed the names". In Hong Kong the district is too coarse — eighteen of them for about seven and a half million people — but an estate or a building name plus birth date plus sex would do the same work: a building holds a few hundred people, and there are tens of thousands of birth dates. Ask: which three columns in your product’s data would do it?'))

S.append(cards('05 · ANONYMISED IS NOT ANONYMOUS', 'Three ways the names came back.', [
    ('NETFLIX PRIZE · 2006 – 2009', 'Ratings plus IMDb.', 'Netflix published the film ratings of about half a million subscribers, names removed, as a competition dataset. Narayanan and Shmatikov, 2008: a handful of public IMDb ratings was enough to find a person’s Netflix record — and everything else they had rated.'),
    ('STRAVA · 2018', 'A heatmap of a billion activities.', 'Aggregated, anonymised, published as a global map in late 2017. In the desert the only people running laps were soldiers: the map drew the perimeter of bases nobody had announced, and the routes between them.'),
    ('THE RULE', 'Linkage.', 'Anything that is rare in your data and public somewhere else is a name: a birth date, a ZIP code, ten films, a running route. Design the dataset for the linker, not for the honest reader.'),
], text_size=21, notes='Two more, because the room will think Sweeney is a special case. Netflix: high-dimensional data — a few hundred ratings per person — is a fingerprint; two researchers matched it to the public ratings people had posted under their own names on IMDb. Strava: not even individual data, an aggregate map, and still it leaked, because in some places the aggregate is one person. The rule is the register’s data column with a privacy lens: for every field, ask what it can be joined to. Then the defence.'))

S.append(sketch_slide('05 · LIVE · K-ANONYMITY', 'Anonymous means: at least k people look like you.',
                      live('w09-anonymise', ANON_JS, 1400, 500, hint='mouse x = k, from 1 to 6'),
                      caption='Sweeney, 2002. Twelve fictional patients; the diagnosis is the secret. Age, district and sex are generalised, one step at a time, until every row shares them with at least k − 1 others. The price is printed on the right.',
                      notes='k-anonymity, Sweeney 2002: a release is k-anonymous when every combination of quasi-identifiers appears at least k times. Slide from the left. k = 1: the table as collected, every row unique, the neighbour who knows your age, district and sex reads your diagnosis. k = 2: ages become bands, the neighbour gets two rows. k = 3 or 4: districts become regions, four rows. k = 5: with only twelve people there is nothing left to generalise except everything; the table is anonymous and useless. Two lessons: anonymity is a number you choose, and it costs information — and it still leaks if all four rows share a diagnosis, which is why later work added l-diversity. Differential privacy, which the 2020 US census used, is the stronger cousin; mention it, do not teach it.'))

S.append(content('05 · SYNTHETIC DATA', 'Examples made by a model. Cheap, private, and a copy of the middle.',
                 ['Generate the training set instead of collecting it: no real person in it, rare cases on demand, no consent to ask for.',
                  '- It is the model’s world again, one step removed: the synthetic patients carry the generating model’s biases, plus its blind spots.',
                  '- **Shumailov et al., Nature, 2024:** train a model on the output of a model, and again, and the tails of the distribution disappear first. Model collapse. The edge goes before the middle.',
                  '- Useful for testing, for padding a thin group, for a prototype. Not a substitute for the people who were not in the room.',
                  'Week 1: the designer starts where the model’s confidence ends. Synthetic data has no edge to start from.'],
                 body_size=29,
                 notes='The escape route every team will propose at some point: no people, no privacy problem. Half true. The synthetic examples come out of a model, and the model has a middle and an edge like every other; the rare cases you wanted are exactly what it does worst. The Nature paper is the extreme case — a model trained on its own output loses the tails in a few generations — and it is the week-1 argument in reverse: the edge is where the designer works, and synthetic data is all middle. Fine for a prototype, and say so in the register.'))

# ───────────────────────── 06 · can a model be neutral ─────────────────────────
S.append(section('06', 'Can a model be neutral?', 'three positions · argue the other side', bg=INK,
                 notes='Chapter six, short: the question from vote one, taken seriously, in three positions. Then two minutes each in pairs.'))

S.append(cards('06 · THREE POSITIONS', 'Yes. No. Wrong question.', [
    ('YES · THE ENGINEER', 'The maths is neutral. Fix the data.', 'A model is a function; bias is what went in. Collect better examples, test every group, publish the numbers. Gender Shades is the proof: named, measured, and improved within months. Neutrality is a target you can move towards.'),
    ('NO · THE PHILOSOPHER', 'Every window is a choice.', 'Verbeek, week 1: designing things is designing human existence. The dataset, the labels, the objective, the threshold: four decisions, four sets of values. There is no view from nowhere, and a model is a view.'),
    ('WRONG QUESTION · THE DESIGNER', 'Neutral for whom? Accountable to whom?', 'Nobody asks whether a chair is neutral; they ask who it was made for and who cannot sit in it. Ask that of the model. Then write down who answers when it is wrong — which is the last column of the register.'),
], text_size=21, notes='Give each position its best day. The engineer is right that bias can be measured and reduced, and that "it is all political" is a way of not doing the work. The philosopher is right that there is no neutral window: every dataset was collected by someone for something, and the threshold is a value with a number on it. The designer moves the question: neutrality is not a property a thing has, accountability is a relationship a thing is in. Notice that the register is the third position turned into a form. Put the word cloud from the start of class up next to the three positions and ask which position each of the three biggest words argues for. Do not say which one you hold; the second vote is at the end.'))

S.append(statement('There is no view from nowhere. Someone chose the window.', eyebrow_text='06 · THE SENTENCE TO ARGUE WITH', size=104,
                   notes='One sentence, deliberately on the philosopher’s side, so that the engineers in the room have something to push against. In pairs now.'))

S.append(activity('PAIRS', 4, 'Argue the side you did not vote for.',
                  ['Turn to your neighbour. Two minutes each. Take a position you did **not** choose in the first vote and make its best case, with one example from today.',
                   'Then swap. No winner. The second vote comes after the activity, once you have mapped your own product.'],
                  eyebrow_text='06 · DEBATE', bg=YELLOWS[0],
                  notes='Four minutes, two each, timed on the slide. Walk the room; the TAs listen for the best example on each side and note two to read out after the vote at the end. The rule "the side you did not vote for" is the whole exercise: it is the red pen of the activity, applied to yourself. Then the register.'))

# ───────────────────────── 07 · the bias register ─────────────────────────
S.append(section('07', 'The bias register', 'one row per decision · five columns · the guardrail', bg=PAPER,
                 notes='Chapter seven, the workshop: the form the activity fills in, and what a good row looks like.'))

S.append(figure_slide('07 · THE REGISTER', 'One row per decision. Five columns.', F.w09_register(),
                      caption='A fictional example: Nightlight, a bedside lamp that decides when you are tired. The register goes on Blackboard with the concept board; its rows become the data, bias and guardrail paragraphs of your mediation brief.',
                      notes='Read the first row aloud, column by column. The decision is a verb and a person. The data names the window: phone use, the time, how still you sit, and from whom — the beta testers. The thin column names real people the window missed. The harm is written twice, once per kind of mistake — the threshold chapter, applied. The guardrail is a rule you can read, machine A protecting people from machine B, plus the person who can be appealed to. The second row is a weaker one on purpose: ask the room what is missing (the harm has no false-no line; the guardrail has no person).'))

S.append(cards('07 · HOW TO FILL IT', 'Concrete, or it is not a row.', [
    ('THE DECISION', 'A verb and a person.', '"Dims the lamp when it thinks you are tired." Not "personalises the experience". If you cannot say what it decides, it is not a decision yet.'),
    ('THE DATA', 'Where it comes from, who is in it.', 'Sensors, logs, a public dataset, your beta testers. Name the window: the twenty people, the one language, the one city, the one year.'),
    ('WHO IS THIN', 'Someone real.', 'Shift workers. People who read in bed. Anyone who does not type. The edge of your concept from week 1: say who lives there.'),
    ('THE HARM', 'False yes and false no.', 'Two lines of harm for every decision: what happens when it says yes and should not, and when it says no and should. And to whom.'),
    ('THE GUARDRAIL', 'A rule, and a way to appeal.', 'Machine A protecting people from machine B: a floor, a default, an off switch, a person. And who the person is, and how fast.'),
], text_size=19, notes='Five columns, five tests. The most common failures, from experience: a decision that is a feature name, a data column that says "users", a thin column that says "everyone", a harm with only one kind of mistake, a guardrail that says "we will monitor it". The TAs walk with these five sentences and read them out at any table that has written one of them. Then the activity.'))

# ───────────────────────── 08 · activity: map the ethics of your concept ─────────────────────────
S.append(section('08', 'Map the ethics of your concept.', '30 minutes · your team · paper or a shared doc · ClassPoint', bg=YELLOWS[0],
                 notes='The activity: your own product, one register, three rows, then a red pen from the team next to you. What goes into ClassPoint is one image per team with a caption, then a vote on your own worst bias, then the second vote on neutrality. Nicolò keeps time; Amber, WU Zhao and MA Jie walk with the five tests. Teams from week 7; anyone without a team joins the nearest one for today.'))

S.append(activity('1 — TEAMS · THE DECISIONS', 6, 'List every decision the model makes.',
                  ['Sit with your team. Open last week’s proposal.',
                   'Write down **every decision the model makes for a person**: a verb and a person, one per line. Most products have five to ten once you look.',
                   'Circle the three that matter most: the ones with the biggest harm when they are wrong.'],
                  bg=YELLOWS[0],
                  notes='Six minutes. Teams usually find more decisions than their proposal admits: the ranking, the default, the notification, the moment it stays silent. Silence is a decision too — a false no. Push for verbs; "recommends" is fine, "engages" is not. The three they circle are the three rows.'))

S.append(question('short_answer', 'Team number, and the decision with the biggest harm.',
                  hint='One line, scribe only: the team number, then the decision as a verb and a person. "Team 12: dims the lamp when it thinks she is tired."',
                  eyebrow_text='08 · CAPTURE 1 · SHORT ANSWER · ONE PER TEAM',
                  notes='Two minutes, scribes only, about 25 lines. Read four aloud and apply the first test to each: is it a verb and a person? "Personalises the experience" fails; "dims the lamp when it thinks she is tired" passes. A line that fails goes back to its team as the first row to fix. Keep the export: week 10 opens by asking every team for the guardrail of this same decision.'))

S.append(activity('2 — TEAMS · THE REGISTER', 10, 'Fill the register for the three.',
                  ['Three rows, five columns, on paper or in a shared doc. The template is on the right; the filled example is in chapter 07.',
                   'Rule: every cell names something concrete. "Users" is not a data source; "the 20 beta testers, all students" is. "Everyone" is not a thin group.',
                   'The TAs walk. Call one over if a cell has stayed empty for two minutes: the empty cell is usually the finding.'],
                  panel=REGISTER, panel_size=21, bg=YELLOWS[1],
                  notes='Ten minutes, the heart of the class. The third column is where teams stall, and the stall is the lesson: they do not know who is thin in their data because they have not decided what the data is. Send them back a column — and to last week’s line: Amber has every team’s "data we need and do not have" answer from the week-8 short answer, one line per team, and reads it back to any team whose data column is empty. The harm column wants both kinds of mistake; the guardrail wants a person’s job title. Nicolò calls two minutes before the end so that every register has something in every cell, even a question mark.'))

S.append(question('image_upload', 'One per team: your register.',
                  hint='A photo or a screenshot of the three rows. Caption: the product name, and the row you think is the worst.',
                  eyebrow_text='08 · CAPTURE 2 · IMAGE UPLOAD · ONE PER TEAM',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='One upload per team, about 28 images, caption required. Put the wall on screen and pick two registers to read a row from: one with a real person in the thin column, one with "everyone". Do not name the teams; name the rows. The captions tell you which row each team fears, and that is the row to ask about at the poster review. Download the submissions; they come back in week 11 next to the datasets.'))

S.append(activity('3 — SWAP · THE RED PEN', 6, 'Read another team’s register. Add what they missed.',
                  ['Swap registers with the team next to you.',
                   'In red: add **one person who is thin in their data** and **one harm** they did not write. Be specific; be kind; be quick.',
                   'Give it back. Read what they added to yours. Do not argue with it; write it down.'],
                  bg=YELLOWS[2],
                  notes='Six minutes. This is the audit step from Gender Shades, done by amateurs in a hurry, and it still works: a product’s window is easiest to see from outside the team. Watch for the teams that defend instead of writing; the rule is no arguing. The additions go into the Blackboard version tonight, marked as additions.'))

S.append(question('multiple_choice', 'Which of your team’s biases is the worst?', [
    'Data: who is not in our examples', 'Label: who decided what "good" looks like', 'Algorithmic: our objective, our threshold', 'Interaction: the loop with our users',
], eyebrow_text='08 · YOUR PRODUCT · MULTIPLE CHOICE',
    notes='No correct answer; one vote per person, so a team can disagree with itself, which is useful. Most rooms land on A, because it is the one they can see now. Ask a D to explain: those are the products that learn after they ship, and they are the ones week 10 is about. Ask a C which threshold they meant; if they cannot say, it is an A.'))

S.append(content('08 · WHAT JUST HAPPENED', 'You found the people who are not in the room.',
                 ['The decisions: most of you had more than you thought. Every one has a window, and every window has an edge.',
                  'The register: the third column was the hard one, and the red pen found more. Your product’s bias is easiest to see from outside the team. Keep the swap; do it again before the poster.',
                  'The guardrail: a rule you can read, protecting people from a model that cannot say why. Machine A guarding machine B. That is the designer’s turn, in one column.',
                  '**The model learned the window. You decided who else needs to be in it. That was the design.**'],
                 body_size=32,
                 notes='Mirror of the whole day. The dataset is the window, the model knows only the window, and the four doors are four places somebody decided — or did not — who is in it. The register is the deciding, written down. Say the last line slowly; it is the last line of weeks 1 and 2 with the nouns changed. Then the second vote.'))

S.append(question('multiple_choice', 'Now that you have mapped your own product: can a model be neutral?', [
    'Yes: the maths is neutral, the data is the problem', 'No: every dataset and every threshold is a choice', 'Only if a person checks every decision', 'Wrong question: neutral for whom?',
], eyebrow_text='08 · STANCE · VOTE 2 OF 2 · MULTIPLE CHOICE',
    notes='Same four answers as slide 7. Show the two splits side by side — the screenshot from the morning and this one. Movement is the point, in either direction; there is no correct answer, but there is a correct thing to notice: whoever moved, moved because of their own product, not because of an argument. The TAs read out the two best examples from the pair debate. Then the homework.'))

S.append(cards('08 · DUE · BLACKBOARD', 'Two uploads tonight. A prototype to start.', [
    ('CONCEPT BOARD', 'Due after this class.', 'One board: the product, the person, the decision, the data, the relation you are building. The proposal, grown up, with pictures.'),
    ('BIAS REGISTER', 'With the concept board.', 'The three rows from today, cleaned up, plus the red-pen additions marked as additions. It becomes the bias and guardrail paragraphs of your mediation brief.'),
    ('PROTOTYPE V1', 'Start it now.', 'The interaction, not the model: paper, Figma or code — the moment the product decides something for a person, what that person sees, and how they say no. Bring what exists to the week-10 stand-up; on Blackboard before week 11.'),
    ('BEFORE WEEK 10', 'Nothing to watch.', 'Recommendation systems: the feed as a designed mediation. Open your own For You page, Discover Weekly or YouTube home once before class and ask what it thinks you are. Week 10 opens with that.'),
], text_size=22, notes='Three things, two deadlines. Concept board and register tonight on Blackboard, one submission per team. Prototype v1 is next sprint’s item: start it now, show whatever exists at the week-10 stand-up, upload it before week 11 — and the word is interaction, the screen where the decision lands, not the model behind it. Next week needs no video; it needs a look at your own feed. The TAs stay for 30 minutes and will read any register that is brought to them.'))

S.append(end('See you next week. Recommendation systems.',
             'Board and register on Blackboard tonight. Prototype v1: bring what exists.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: the feed — embeddings, similarity, collaborative filtering, echo chambers, and door four in full. Homework in one line: board and register tonight, start the prototype and bring what exists to the stand-up, look at your own feed. The TAs stay for 30 minutes.'))

DECK = dict(title='SD2112 · AI in Design · Week 09', slides=finalize(S, FOOTER), pdf='SD2112-week09.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week09', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 2026-09-05, revised 2026-09-06; every date, number and attribution above was checked against these)
# Coded Bias: https://www.pbs.org/independentlens/documentaries/coded-bias/ (Independent Lens premiere 22 March 2021)
#   https://en.wikipedia.org/wiki/Coded_Bias (Sundance 2020, 90 min, Netflix from 5 April 2021, who appears, the white mask)
#   https://www.netflix.com/title/81328723 (listed on Netflix, September 2026)
# Gender Shades: https://proceedings.mlr.press/v81/buolamwini18a.html (FAT* 2018; 34.7 % / 0.8 %)
#   https://gs.ajl.org/ and https://www.media.mit.edu/publications/actionable-auditing-investigating-the-impact-of-publicly-naming-biased-performance-results-of-commercial-ai-products/
#   (IBM, Microsoft, Face++; Pilot Parliaments Benchmark, 1,270 faces; new API versions within seven months)
# Sweeney: https://dataprivacylab.org/projects/identifiability/paper1.pdf via https://www.johndcook.com/blog/2018/12/07/simulating-zipcode-sex-birthdate/
#   (2000: 87 %, 216 of 248 million, 1990 census); https://crypto.stanford.edu/~pgolle/papers/census.pdf (Golle 2006: 63 %)
#   https://epic.org/wp-content/uploads/privacy/reidentification/Sweeney_Article.pdf (k-anonymity, 2002); the Weld linkage as told in
#   https://www.johndcook.com/blog/2018/12/07/no-funding-for-unwanted-news/
# Sweeney 2013, ad delivery: https://dl.acm.org/doi/10.1145/2447976.2447990 (25 % more likely, black-identifying first names)
# GDPR art. 5: https://gdpr-info.eu/art-5-gdpr/ · PDPO: https://www.pcpd.org.hk/english/data_privacy_law/ordinance_at_a_Glance/ordinance.html
#   and https://www.pcpd.org.hk/english/data_privacy_law/6_data_protection_principles/principles.html (1995 / December 1996; DPP1–6)
#   PCPD AI framework: https://www.pcpd.org.hk/english/news_events/media_statements/press_20240611.html (11 June 2024; four areas)
# Netflix Prize: https://www.cs.cornell.edu/~shmat/shmat_oak08netflix.pdf (Narayanan & Shmatikov, IEEE S&P 2008; ~500,000 subscribers; IMDb)
# Strava: https://www.nbcnews.com/tech/security/strava-fitness-tracking-map-reveals-military-bases-movements-war-zones-n841871 (January 2018; map posted November 2017)
# Amazon recruiting: https://www.irishtimes.com/business/technology/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-1.3658651 (Reuters / Dastin, 10 October 2018)
# ImageNet: https://www.theartnewspaper.com/2019/09/23/leading-online-database-to-remove-600000-images-after-art-project-reveals-its-racist-bias
#   https://excavating.ai/ (Crawford & Paglen 2019); https://qz.com/1034972/the-data-that-changed-the-direction-of-ai-research-and-possibly-the-world (Mechanical Turk, 14 million images)
#   https://www.deeplearning.ai/the-batch/imagenet-gets-a-makeover (2,832 person categories)
# Google Photos 2015: https://www.cbc.ca/news/trending/google-photos-black-people-gorillas-1.3135754 · https://incidentdatabase.ai/cite/16/
# Twitter cropping: https://blog.x.com/engineering/en_us/topics/insights/2021/sharing-learnings-about-our-image-cropping-algorithm (May 2021; 403 on 2026-09-06)
#   https://www.cnn.com/2021/05/19/tech/twitter-image-cropping-algorithm-bias (Chowdhury quote); https://arxiv.org/pdf/2105.08667 (Yee, Tantipongpipat & Mishra:
#   'no more than 3 out of 100 images per gender have the crop not on the head', 'a number on the jersey', 'consistent across genders')
#   https://www.africanews.com/2021/05/20/twitter-scraps-algorithm-after-finding-it-excludes-black-people-and-women/ (AFP: 8 % in favour of women,
#   4 % in favour of white individuals; 'We did not find any evidence of an objectification bias', Chowdhury)
# Tay: https://en.wikipedia.org/wiki/Tay_(chatbot) (23 March 2016; 16 hours)
# PredPol: https://rss.onlinelibrary.wiley.com/doi/full/10.1111/j.1740-9713.2016.00960.x (Lum & Isaac, Significance, 2016)
# COMPAS: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing and
#   https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm (7,214 defendants; 45 % vs 23 %; 48 % vs 28 %)
# The theorem: https://www.cs.cornell.edu/home/kleinber/aer18-fairness.pdf (Kleinberg, Mullainathan & Raghavan 2016; Chouldechova 2017)
# Equal opportunity: https://papers.nips.cc/paper/6374-equality-of-opportunity-in-supervised-learning (Hardt, Price & Srebro, NeurIPS 2016)
#   https://research.google.com/bigpicture/attacking-discrimination-in-ml/ (Wattenberg, Viégas & Hardt, 2016 explorable; the URL now 301s to pair.withgoogle.com —
#   archived copy: http://web.archive.org/web/20230607114941/http://research.google.com/bigpicture/attacking-discrimination-in-ml/ ;
#   introduced in https://research.google/blog/equality-of-opportunity-in-machine-learning/ , Hardt, 7 October 2016)
# LAION-5B: https://papers.nips.cc/paper_files/paper/2022/hash/a1859debfb3b59d094f3504d5ebb6c25-Abstract-Datasets_and_Benchmarks.html (5.85 billion pairs)
# Bloomberg 2023: https://www.bloomberg.com/graphics/2023-generative-ai-bias/ via https://racismandtechnology.center/2023/07/07/racist-technology-in-action-stable-diffusion-exacerbates-and-amplifies-racial-and-gender-disparities/
# Datasheets: https://arxiv.org/pdf/1803.09010 (Gebru et al. 2018) · Model collapse: https://www.nature.com/articles/s41586-024-07566-y (Shumailov et al., Nature 631, 2024)
# Differential privacy and the 2020 census: https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/process/disclosure-avoidance/2020-das-updates/2020-das-faqs.html
