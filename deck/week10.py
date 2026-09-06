"""
SD2112 · Artificial Intelligence in Design · Week 10 — the slide spec.

    python deck/week10.py            # builds _site/week10/ (html deck + pdf), export/week10*.pptx, export/preview/
    python deck/week10.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Recommendation systems: the feed as the most-used AI product; an item is a point (embeddings, similarity
search, content-based filtering); people like you (the user–item matrix, collaborative filtering, the
Netflix Prize, two towers, the cold start); the objective (engagement as the target, the attention trap,
bubbles); the feed as a mediation (Ihde's relations, designing the objective, "why am I seeing this", the
exploration dial); a similarity search by hand on PolyU GenAI and in the p5 editor; and the activity
"Your feed's objective", which writes the objective, the drift, the explanation and the dial of each
team's product. Four live p5.js sketches; drawn figures in tools/figures_week10.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week10 as F10                            # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, sketch_slide, code_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(10)

# ───────────────────────── the live sketches (html deck; the pptx and the PDF show a snapshot) ─────────────────────────
SIM_A = """// Forty items, three features each: shape (0 = triangle,
// 1 = circle), colour (0 = warm, 1 = cool), size. The mouse
// is what you looked at; the five nearest are what comes next.
const N = 40;
let items = [], byShape = true;

function setup() {
  createCanvas(1400, 560); randomSeed(10);
  for (let i = 0; i < N; i++)
    items.push({ shape: random(), hue: random(),
                 size: random() });
}

function dist3(a, b) {   // the metric: a weighted distance
  let w = byShape ? [1, .2, .2] : [.2, 1, .2]; // the weights
  return sqrt(w[0] * sq(a.shape - b.shape)
            + w[1] * sq(a.hue - b.hue)
            + w[2] * sq(a.size - b.size));
}

function keyPressed() {         // T: the other metric
  if (key == 't' || key == 'T') {
    byShape = !byShape; return false;
  }
}"""

SIM_B = """function draw() {
  background(255); textFont('JetBrains Mono');
  let px = 60, py = 50, pw = 900, ph = 460;            // the map
  let q = { shape: constrain((mouseX - px) / pw, 0, 1),
            hue: constrain((mouseY - py) / ph, 0, 1), size: 0.5 };
  let ranked = items.map((it, i) => [i, dist3(q, it)])
                    .sort((a, b) => a[1] - b[1]).slice(0, 5);
  let near = ranked.map(r => r[0]);
  let qx = px + q.shape * pw, qy = py + q.hue * ph;
  noFill(); stroke(225); strokeWeight(1); rect(px, py, pw, ph);
  noStroke(); fill(120); textSize(14); textAlign(LEFT);
  text('triangle', px, py - 10); text('warm', px + pw + 8, py + 12);
  text('cool', px + pw + 8, py + ph); textAlign(RIGHT);
  text('circle', px + pw, py - 10); textAlign(LEFT);
  for (let i = 0; i < N; i++) {
    let it = items[i], x = px + it.shape * pw, y = py + it.hue * ph;
    if (near.includes(i)) { stroke('#ED6D24'); strokeWeight(2); line(qx, qy, x, y); }
  }
  for (let i = 0; i < N; i++) {
    let it = items[i];
    glyph(px + it.shape * pw, py + it.hue * ph, it, near.includes(i));
  }
  noFill(); stroke(0); strokeWeight(3); circle(qx, qy, 26);   // the query
  noStroke(); fill(0); textSize(13); text('you looked at this', qx + 18, qy + 5);
  // the list: the five nearest, with their distances
  let lx = 1060;
  fill('#ED6D24'); textSize(15); text('THE FIVE NEAREST', lx, 70);
  fill(0); textSize(14);
  text('metric: by ' + (byShape ? 'SHAPE' : 'COLOUR') + '   (press T)', lx, 96);
  fill(120); textSize(13);
  text(byShape ? 'shape x 1 · colour x 0.2 · size x 0.2' : 'shape x 0.2 · colour x 1 · size x 0.2', lx, 118);
  for (let k = 0; k < 5; k++) {
    let it = items[ranked[k][0]], y = 160 + k * 58;
    glyph(lx + 20, y, it, true);
    noStroke(); fill(0); textSize(15);
    text((k + 1) + '  item ' + ranked[k][0] + '   d = ' + nf(ranked[k][1], 1, 2), lx + 50, y + 5);
  }
  fill(120); textSize(13);
  text('same query, other metric: other five.', lx, 470);
  text('which axis counts is the design.', lx, 490);
}

function glyph(x, y, it, hot) {
  let r = 7 + it.size * 14, n = 3 + floor(it.shape * 5.99);   // 3 to 8 sides
  colorMode(HSB, 360, 100, 100); fill(20 + it.hue * 230, 65, 92); colorMode(RGB);
  stroke(hot ? '#ED6D24' : 0); strokeWeight(hot ? 3 : 1);
  if (it.shape > 0.92) circle(x, y, 2 * r);
  else {
    beginShape();
    for (let k = 0; k < n; k++)
      vertex(x + r * cos(-HALF_PI + TWO_PI * k / n), y + r * sin(-HALF_PI + TWO_PI * k / n));
    endShape(CLOSE);
  }
}"""

SIM_CODE = SIM_A + '\n\n' + SIM_B

COLLAB_CODE = """// Twelve listeners, ten items; a like is a filled cell — the same
// table as the figure before this slide. The last row is you: click
// a cell to like or unlike an item. User–user collaborative
// filtering: cosine similarity between your row and every other
// row; the three rows most like yours vote on the items you have
// not liked. Tinted cells are predictions; the top three are your
// feed. Hover a column to see who liked it.
const U = 12, I = 10, ITEMS = 'ABCDEFGHIJ';
let likes = [];

function setup() {
  createCanvas(1400, 560); textFont('JetBrains Mono');
  likes = [   // three tastes, written by hand: A B C D · E F G · H I J, and a few likes across them
    [1,1,1,1,0,0,0,0,0,0], [0,0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,1,1,1],   // U1 U2 U3
    [1,0,1,1,0,0,0,0,0,0], [0,1,0,0,1,0,1,0,0,0], [0,0,0,1,0,0,0,1,0,1],   // U4 U5 U6
    [1,1,0,1,0,1,0,0,0,0], [0,0,0,0,0,1,1,0,0,0], [0,0,0,0,1,0,0,0,1,1],   // U7 U8 U9
    [1,1,1,0,0,0,0,0,0,0], [0,0,0,0,1,1,0,1,0,0],                          // U10 U11
    [1,0,0,1,0,0,0,0,0,0]];                                                // YOU: A and D, so far
}

function cosine(a, b) {                      // how much two rows agree: 0 to 1
  let dot = 0, na = 0, nb = 0;
  for (let j = 0; j < I; j++) { dot += a[j] * b[j]; na += a[j]; nb += b[j]; }
  return na && nb ? dot / sqrt(na * nb) : 0;
}

function predict() {                         // the three most like you vote
  let you = likes[U - 1], sims = [], score = Array(I).fill(0), total = 0;
  for (let u = 0; u < U - 1; u++) sims.push([u, cosine(you, likes[u])]);
  sims.sort((a, b) => b[1] - a[1]);
  let top = sims.slice(0, 3).filter(s => s[1] > 0);
  for (let [u, s] of top) { total += s; for (let j = 0; j < I; j++) score[j] += s * likes[u][j]; }
  for (let j = 0; j < I; j++) score[j] = you[j] || !total ? 0 : score[j] / total;
  return { top, score };
}

const X0 = 200, Y0 = 50, CS = 38;

function draw() {
  background(255);
  let { top, score } = predict();
  let ranked = score.map((s, j) => [j, s]).filter(r => r[1] > 0).sort((a, b) => b[1] - a[1]).slice(0, 3);
  let hover = floor((mouseX - X0) / CS);
  if (hover >= I || mouseY < Y0 || mouseY > Y0 + U * CS) hover = -1;
  for (let j = 0; j < I; j++) {
    noStroke(); fill(hover == j ? 245 : 255); rect(X0 + j * CS, Y0, CS, U * CS);
    fill(0); textSize(15); textAlign(CENTER); text(ITEMS[j], X0 + j * CS + CS / 2, Y0 - 10);
  }
  textAlign(RIGHT);
  for (let u = 0; u < U; u++) {
    let y = Y0 + u * CS, isTop = top.some(t => t[0] == u);
    noStroke(); fill(u == U - 1 ? '#ED6D24' : isTop ? '#0E8C8D' : 120); textSize(14);
    text(u == U - 1 ? 'YOU' : 'U' + (u + 1), X0 - 12, y + CS / 2 + 5);
    for (let j = 0; j < I; j++) {
      let x = X0 + j * CS;
      stroke(225); strokeWeight(1); noFill(); rect(x, y, CS, CS);
      if (likes[u][j]) { noStroke(); fill(u == U - 1 ? '#ED6D24' : 0); rect(x + 7, y + 7, CS - 14, CS - 14); }
      else if (u == U - 1 && score[j] > 0) {
        noStroke(); fill(237, 109, 36, 40 + 180 * score[j]); rect(x + 4, y + 4, CS - 8, CS - 8);
        let k = ranked.findIndex(r => r[0] == j);
        if (k >= 0) { fill(0); textSize(14); textAlign(CENTER); text(k + 1, x + CS / 2, y + CS / 2 + 5); textAlign(RIGHT); }
      }
    }
    if (isTop) { noFill(); stroke('#0E8C8D'); strokeWeight(3); rect(X0 - 2, y - 2, I * CS + 4, CS + 4); }
  }
  textAlign(LEFT); noStroke();
  fill('#ED6D24'); textSize(15); text('THE THREE MOST LIKE YOU', 760, 70);
  for (let k = 0; k < 3; k++) {
    let y = 100 + k * 30;
    if (k < top.length) {
      fill(0); textSize(15); text('U' + (top[k][0] + 1), 760, y + 5);
      fill('#0E8C8D'); rect(820, y - 8, 300 * top[k][1], 16);
      fill(0); text(nf(top[k][1], 1, 2), 1130, y + 5);
    } else { fill(120); textSize(14); text('— nobody agrees with you yet', 760, y + 5); }
  }
  fill('#ED6D24'); textSize(15); text('PREDICTED FOR YOU', 760, 230);
  for (let k = 0; k < 3; k++) {
    let y = 260 + k * 30;
    if (k < ranked.length) {
      fill(0); textSize(15); text((k + 1) + '  item ' + ITEMS[ranked[k][0]], 760, y + 5);
      fill(237, 109, 36); rect(900, y - 8, 220 * ranked[k][1], 16);
      fill(0); text(nf(ranked[k][1], 1, 2), 1130, y + 5);
    } else { fill(120); textSize(14); text('— nothing to say: the cold start', 760, y + 5); }
  }
  fill(120); textSize(13);
  text('score = how much of the vote of the three most like you went to this item', 760, 370);
  text('nobody knows what an item is; the crowd is the description', 760, 392);
  text('like everything and you are like nobody · like nothing and it has nothing', 760, 414);
  if (hover >= 0) {
    let n = likes.slice(0, U - 1).filter(r => r[hover]).length;
    fill(0); textSize(14); text('item ' + ITEMS[hover] + ': liked by ' + n + ' of 11 other listeners', 760, 484);
  }
  fill(0); textSize(14); text('click a cell in your row to like or unlike · R restarts', 760, 452);
}

function mousePressed() {
  let j = floor((mouseX - X0) / CS), u = floor((mouseY - Y0) / CS);
  if (u == U - 1 && j >= 0 && j < I) likes[U - 1][j] = 1 - likes[U - 1][j];
}"""

FEED_CODE = """// An echo-chamber simulator. Eight topics; a screen is twelve cards
// drawn from what the feed thinks you like. Clicking a card engages:
// the distribution moves towards that topic by the learning rate.
// Mouse y sets the exploration rate: the share of cards drawn at
// random instead. The line at the right is how many topics your last
// fifty cards really covered: 8 when they are spread evenly, 1 when
// they are all the same. Before you arrived, twelve screens went by
// with no exploration and a person who always clicked the commonest
// card — no taste at all. That is what the loop learns anyway.
const TOPICS = ['music', 'news', 'sport', 'food', 'film', 'travel', 'craft', 'science'];
const COLS = ['#64C2C3', '#943890', '#ED6D24', '#F6AD00', '#E94D7F', '#5C6470', '#B68EBB', '#000B1C'];
const LR = 0.15;                            // how much one click moves the feed
let p = [], feed = [], seen = [], hist = [], explore = 0.2, clicks = 0, moved = false;

function setup() {
  createCanvas(1400, 560); textFont('JetBrains Mono'); randomSeed(2112);
  p = Array(8).fill(1 / 8);                 // day one: every topic equally likely
  for (let k = 0; k < 12; k++) { screen(0); engage(commonest()); }   // the pre-run: no tries, no taste
  screen(explore);
}

function screen(eps) {                      // the next twelve cards
  feed = [];
  for (let i = 0; i < 12; i++) {
    let tried = random() < eps, t = 7;
    if (tried) t = floor(random(8));
    else { let r = random(), acc = 0; for (let k = 0; k < 8; k++) { acc += p[k]; if (r < acc) { t = k; break; } } }
    feed.push({ t, tried });
    seen.push(t); if (seen.length > 50) seen.shift();
  }
  hist.push(spread()); if (hist.length > 40) hist.shift();
}

function spread() {                         // how many topics the last 50 cards really cover: 1 / the sum of squared shares
  let n = Array(8).fill(0), s = 0;
  for (let t of seen) n[t]++;
  for (let k = 0; k < 8; k++) s += sq(n[k] / seen.length);
  return 1 / s;                             // 8 = spread evenly · 1 = all the same topic
}

function commonest() {                      // the topic with most cards on the screen
  let n = Array(8).fill(0); for (let c of feed) n[c.t]++;
  return n.indexOf(max(n));
}

function engage(t) {                        // the feed learns from one click
  for (let k = 0; k < 8; k++) p[k] = k == t ? p[k] + LR * (1 - p[k]) : p[k] * (1 - LR);
}

function draw() {
  background(255);
  if (moved) explore = constrain(mouseY / height, 0, 1) * 0.5;
  // what it thinks you like
  noStroke(); fill('#ED6D24'); textSize(15); text('WHAT THE FEED THINKS YOU LIKE', 40, 40);
  for (let k = 0; k < 8; k++) {
    let y = 70 + k * 50;
    fill(0); textSize(14); text(TOPICS[k], 40, y + 16);
    fill(235); rect(120, y, 280, 22); fill(COLS[k]); rect(120, y, 280 * p[k], 22);
    fill(0); text(round(100 * p[k]) + ' %', 410, y + 16);
  }
  fill(120); textSize(13); text('a click moves ' + round(100 * LR) + ' % of the weight to that topic', 40, 486);
  // the screen
  fill('#ED6D24'); textSize(15); text('THE SCREEN · twelve cards · click one to engage', 500, 40);
  for (let i = 0; i < 12; i++) {
    let c = feed[i], x = 500 + (i % 3) * 176, y = 60 + floor(i / 3) * 112;
    if (c.tried) { stroke(COLS[c.t]); strokeWeight(3); fill(255); rect(x, y, 166, 102, 6); }
    else { noStroke(); fill(COLS[c.t]); rect(x, y, 166, 102, 6); }
    noStroke(); fill(c.tried ? COLS[c.t] : c.t == 7 || c.t == 5 ? 255 : 0); textSize(14);
    text(TOPICS[c.t], x + 12, y + 26);
    if (c.tried) { textSize(12); text('explore: a try', x + 12, y + 88); }
  }
  // the history and the dial
  let hx = 1050, hy = 70, hw = 310, hh = 180;
  fill('#ED6D24'); textSize(15); text('DIVERSITY · THE LAST 50 CARDS', hx, 40);
  stroke(225); strokeWeight(1); noFill(); rect(hx, hy, hw, hh);
  noStroke(); fill(120); textSize(12); text('8', hx - 16, hy + 10); text('1', hx - 16, hy + hh);
  stroke('#ED6D24'); strokeWeight(3); noFill(); beginShape();
  for (let i = 0; i < hist.length; i++) vertex(hx + i * hw / 39, hy + hh - (hist[i] - 1) * hh / 7);
  endShape();
  noStroke(); fill(0); textSize(14);
  text('now: effectively ' + nf(hist[hist.length - 1], 1, 1) + ' of 8 topics', hx, hy + hh + 24);
  fill(120); textSize(13); text(new Set(seen).size + ' of 8 turned up · one point per screen', hx, hy + hh + 44);
  fill('#ED6D24'); textSize(15); text('THE DIAL · mouse y', hx, 350);
  fill(0); textSize(20); text('exploration ' + round(100 * explore) + ' %', hx, 380);
  fill(120); textSize(13);
  text('about ' + round(12 * explore) + ' of 12 cards are not the best guess', hx, 404);
  text('top of the canvas: 0 % — the trap', hx, 428); text('bottom: 50 % — half chance', hx, 448);
  fill(0); textSize(14); text('your clicks: ' + clicks + ' · R restarts', hx, 484);
}

function mouseMoved() { moved = true; }

function mousePressed() {
  for (let i = 0; i < 12; i++) {
    let x = 500 + (i % 3) * 176, y = 60 + floor(i / 3) * 112;
    if (mouseX > x && mouseX < x + 166 && mouseY > y && mouseY < y + 102) {
      engage(feed[i].t); clicks++; screen(explore); return;
    }
  }
}"""

# the workshop script: what students paste into the p5 editor (the panel shows it; the page adds the interaction)
VECTORS_CODE = """// ten products, five numbers each (0 to 1): the model's table
const names = ['lamp', 'kettle', 'stool', 'vase', 'clock',
               'rug', 'radio', 'planter', 'tray', 'lantern'];
const v = [[.4,.8,.2,.9,.1], [.3,.6,.3,.9,.2], [.5,.2,.7,.3,.6],
           [.2,.5,.3,.1,.8], [.6,.3,.2,.8,.3], [.7,.9,.9,.0,.5],
           [.5,.4,.4,.7,.2], [.2,.6,.4,.2,.9], [.3,.3,.3,.6,.3],
           [.3,.9,.3,.4,.7]];
let w = [1, 1, 1, 1, 1];       // the metric: a weight per axis
let q = 0;                     // the product you just looked at
function cosine(a, b) {        // 1 = same direction, 0 = none
  let d = 0, na = 0, nb = 0;
  for (let i = 0; i < 5; i++) {
    d += w[i] * a[i] * b[i];
    na += w[i] * a[i] * a[i]; nb += w[i] * b[i] * b[i];
  }
  return d / sqrt(na * nb);
}
function setup() {
  createCanvas(800, 600); background(255); fill(0); textSize(22);
  text('nearest to: ' + names[q], 30, 50);
  let r = names.map((n, i) => [n, cosine(v[q], v[i])])
    .filter(x => x[0] != names[q]).sort((a, b) => b[1] - a[1]);
  for (let k = 0; k < 3; k++)
    text((k + 1) + '. ' + r[k][0] + '  ' + nf(r[k][1], 1, 2),
         30, 100 + 36 * k);
}"""

VECTORS_EXTRA = """// the page adds the axes, the whole ranking, and the interaction: click = next product, mouse x = weight on price
const AXES = ['price', 'warmth', 'size', 'metal', 'colour'];
function draw() {
  background(255); textFont('JetBrains Mono');
  let r = names.map((n, i) => [n, cosine(v[q], v[i]), i]).sort((a, b) => b[1] - a[1]);
  noStroke(); fill('#ED6D24'); textSize(15); text('NEAREST TO: ' + names[q].toUpperCase(), 30, 40);
  fill(120); textSize(13); text('click = next product · mouse x = weight on price', 30, 62);
  fill(0); textSize(13);
  for (let a = 0; a < 5; a++) { text(AXES[a], 300 + a * 100, 96); text('x ' + nf(w[a], 1, 1), 300 + a * 100, 116); }
  let rank = 0;
  for (let k = 0; k < r.length; k++) {
    let [n, s, i] = r[k], y = 140 + k * 42, isQ = i == q;
    if (!isQ) rank++;
    noStroke(); fill(isQ ? '#ED6D24' : rank <= 3 ? 0 : 150); textSize(15);
    text(isQ ? 'YOU LOOKED AT' : rank + '.', 30, y + 16); text(n, 180, y + 16);
    for (let a = 0; a < 5; a++) {
      fill(235); rect(300 + a * 100, y, 80, 18);
      fill(isQ ? '#ED6D24' : rank <= 3 ? 0 : 170); rect(300 + a * 100, y, 80 * v[i][a], 18);
    }
    fill(isQ ? '#ED6D24' : rank <= 3 ? 0 : 150); if (!isQ) text(nf(s, 1, 2), 30, y + 34);
  }
  fill(120); textSize(13); text('the three nearest are the recommendation · the weights are the metric · ten fictional products', 30, 585);
}
function mousePressed() { q = (q + 1) % names.length; }
function mouseMoved() { w[0] = constrain(map(mouseX, 0, width, 0, 3), 0, 3); }"""

# ───────────────────────── panels ─────────────────────────
STANDUP_PANEL = [
    'THE STAND-UP · THREE QUESTIONS · STANDING', ' ',
    '1  what did I do since last class?',
    '2  what will I do before the next?',
    '3  what is in my way?', ' ',
    "THIS SPRINT'S ITEM: PROTOTYPE V1",
    '   paper, Figma or code — the moment where your',
    '   product decides, and what the person sees.',
    '   show what exists, not the plan.', ' ',
    'the scribe writes five names, three lines each.',
    'the TAs walk: one question per team.',
]

PROMPT = [
    'Here are ten short product descriptions, 1 to 10:',
    '[paste them]', ' ',
    '1. Choose FIVE features a buyer would care about.',
    '   Each is a number from 0 to 1; say what 0 and 1',
    '   mean (price: 0 = cheap, 1 = expensive).',
    '2. Give a table: one row per product, five numbers.',
    '3. For product 4, list the three nearest products',
    '   by cosine similarity, with the number, and say',
    '   in one sentence why each is near.',
    '4. Redo step 3 with the price feature counted',
    '   three times. What changed, and why?', ' ',
    'OUTPUT: the five feature names, the table, then',
    'the two lists. Nothing else.',
]

OBJECTIVE_PANEL = [
    'THE OBJECTIVE · ONE NUMBER', ' ',
    'the model in your product makes one number',
    'bigger. which?', ' ',
    '  minutes spent · items opened · things bought',
    '  days in a row · lessons finished · replies',
    '  "was this worth it?" answered yes · ...', ' ',
    'write it as a developer could code it:',
    '  "for each person, maximise ______ per ______"', ' ',
    'e.g. Team 12: maximise dinners cooked from a',
    '     suggestion, per week', ' ',
    'no number? then no model can be trained. that',
    'is a finding: write "none yet" and say why.',
]

DRIFT_PANEL = [
    'THE DRIFT · STRATHERN 1997', ' ',
    '"when a measure becomes a target, it ceases',
    ' to be a good measure"', ' ',
    'the model will find the cheapest way to make',
    'your number bigger. what is it?', ' ',
    '  minutes  → autoplay, cliffhangers, outrage',
    '  opened   → clickbait titles, red badges',
    '  streak   → guilt notifications at 23:50',
    '  bought   → the expensive thing, always', ' ',
    'e.g. Team 12: dinners cooked → the same three',
    '     easy dishes, forever', ' ',
    'write: "it will learn to ______, and the',
    '        person will ______"',
]

WHY_PANEL = [
    'WHY AM I SEEING THIS · ONE SCREEN · A4', ' ',
    'the screen a person sees when they tap "why?"',
    'on one recommendation of your product', ' ',
    '1  THE ITEM     what was recommended, drawn',
    '2  THE REASONS  three, in her words:',
    '                "because you ___", "because',
    '                people who ___", "because it',
    '                is popular in ___"',
    '3  THE DATA     which of her data each reason',
    '                used — and one she did not',
    '                know you had',
    '4  THE CONTROLS less like this · not this',
    '                reason · the dial · start fresh', ' ',
    'big letters. a phone photo has to read it.',
]

DIAL_PANEL = [
    'THE EXPLORATION DIAL', ' ',
    'how much of your feed is not the best guess?', ' ',
    '   0 %   only what the score says — the trap',
    '  10 %   one card in ten is a try',
    '  30 %   a third of the feed is new to her',
    '  50 %+  half chance: a shop that shows you',
    '         random shelves', ' ',
    'Stål (Spotify), 2021: "a mix of what you like',
    'and what you might like"', ' ',
    'decide as a team, then vote. write the number',
    'on your screen, next to the controls.',
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 10 · LECTURE + WORKSHOP',
               'Recommendation systems.',
               'Week 10 — an item is a point, people like you, and the attention trap.',
               notes='Join code on screen from 30 minutes before. Sit with your team from the start: the stand-up is the first thing that happens, and the second half is team work again. Laptops out: the workshop after the break needs one per team, logged into the p5 editor and PolyU GenAI.'))

S.append(agenda('SD2112 · WEEK 10', [
    'Last week, in your words', 'The feed is the product', 'An item is a point', 'People like you',
    'The objective', 'The feed as a mediation', 'Workshop: similarity search, by hand', "Activity: your feed's objective",
], notes='Eight stops. The stand-up first, then the lecture in five chapters: what a feed is, the two ways to say "this is like that" — by the item\'s own numbers, and by what people like you did — then the number the model is told to make bigger, and what that does to the person. Break after chapter four. Then the workshop, where you build a similarity search from ten product descriptions, and the activity, where every team writes the objective, the drift, the explanation and the dial of its own product.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the stand-up · the register · the board', bg=ORANGES[0],
                 notes='Chapter one: the stand-up at the team table, fifteen minutes, then one line per team from the bias register, then week 9 in three lines and the map. Prototype v1 is this sprint\'s item; the TAs review it after class.'))

S.append(activity('STAND-UP', 15, 'Three questions, standing.',
                  ['At your table, standing, one minute per person: **what I did, what I will do, what is in my way.**',
                   'Then the increment: show what exists of **prototype v1** — a paper screen, a Figma frame, a script. Not the plan.',
                   'The scribe writes it down. The TAs walk.'],
                  eyebrow_text='01', panel=STANDUP_PANEL, panel_size=20, bg=YELLOWS[0],
                  notes='Fifteen minutes, standing, at the team table — the in-class stand-up week 8 promised, so that every team has seen the format once; from next week it happens at your table in the half hour before class, with the TAs in the room. Nicolò keeps the time on the slide, the other three TAs walk with one question each: what exists now? The rule from week 8: show the thing, not the plan; week 9 asked you to bring what exists of prototype v1, and the upload is due before the week-11 class. A team with nothing to show gets a review slot with Amber after class, not a lecture now. Anyone whose team is not here goes to Amber.'))

S.append(question('short_answer', 'Team number, and the guardrail your bias register names.',
                  hint='One line, scribe only. "Team 12: never below 30 %; a physical dial overrides at night; you can turn it off." No register yet? Write the team number and "not yet".',
                  eyebrow_text='01 · WARM-UP · SHORT ANSWER · ONE PER TEAM',
                  notes='ClassPoint short answer, two minutes, one per team. Read six aloud. A guardrail is a rule — machine A — that catches the model when it is wrong, and it should name who can appeal. Most lines will name a setting; a few will name a person. Keep the screenshot: today adds two more rules to every register, the objective and the explanation, and next week\'s mediation brief asks for all of them.'))

S.append(cards('01 · WEEK 9 · IN THREE LINES', 'Coded Bias, four doors, a register.', [
    ('THE FILM', 'The edge of the grain, with people at it.',
     'Coded Bias: face recognition failing on faces unlike its examples. Not a broken model — a model working exactly as trained, on a dataset with a middle that was somebody\'s.'),
    ('THE FOUR DOORS', 'Data, label, algorithm, interaction.',
     'Bias enters where the examples are chosen, where they are named, where the rule is written, and where people react to the product — and the last door feeds the first. Today is the last door, at scale.'),
    ('THE REGISTER', 'One row per decision.',
     'The decision · the data it learns from · who is thin in the data · the harm when wrong · the guardrail. Three rows minimum. Today adds two columns to every row: the objective, and the explanation.'),
], text_size=22, notes='Three lines from last week. The film is the reference point for the whole module: a model that is confidently wrong at the edge of its examples. The four doors are the vocabulary; the fourth — interaction — is the one a feed opens a hundred times a day: what people click becomes the data the next screen is built from. The register is the deliverable; by the end of today each row has an objective and an explanation next to it.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(3, 2),
                 notes='Module 3, last week of three. Week 8 put the model inside the product, week 9 asked whose data it learns from; today is the product that most people meet most often — the feed — and it closes the module. Next week module 4 opens: what is left for the designer, starting with curating outputs and datasets, and who made Belamy. Prototype v1 is this sprint; the draft poster and the mediation brief are next.'))

# ───────────────────────── 02 · the feed is the product ─────────────────────────
S.append(section('02', 'The feed is the product', 'YouTube · TikTok · Spotify · a decision, a hundred times a day', bg=INK,
                 notes='Chapter two: the most-used AI product is not a chatbot. It is the thing that decides what you see next, and it has been shipping to billions of people since long before anyone typed a prompt. One word cloud, then the anatomy, then three feeds in their own words.'))

S.append(question('word_cloud', 'What does your feed think you are?',
                  hint='One word: the person your For You page, your Discover Weekly or your YouTube home is built for. Not who you are — who it thinks you are.',
                  eyebrow_text='02 · WARM-UP · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each, ninety seconds. Read the biggest three. Expect: cats, food, gym, sad, anime, shopping. Then the question that runs under the chapter: how does it know? It does not know; it has a row of numbers about you and a rule for filling in the rest — and you are about to see both. Keep the screenshot for the debrief: the room described the model of itself.'))

S.append(figure_slide('02 · ANATOMY', "A feed is week 8's five parts, run in a loop.", F10.w10_feed_anatomy(),
                      body=['A pool of millions, cut to a few hundred candidates, each given a score, ten of them put on the screen — and what you do with them goes back into the data the next screen is built from. The model makes the score. Every other part is a rule somebody wrote, or did not.'],
                      caption='Two stages, from YouTube\'s own papers: candidate generation, then a ranking model over a few hundred survivors (Covington, Adams & Sargin, RecSys 2016; Zhao et al., RecSys 2019).',
                      notes='Walk left to right and name the five parts with week 8\'s words. The pool: a policy decides what may appear at all. The candidates: a similarity search — the neighbours of what you did — which is chapter three and four. The score: the objective — chapter five. The screen: the dial and the shared row — chapter six. The person: what counts as a signal. Then the loop, which is the fourth door from last week drawn as an arrow: your click is the training data for your next screen. Ask: which of the five parts does a designer usually get to touch? All of them, and most teams touch none.'))

S.append(cards('02 · THREE FEEDS, IN THEIR OWN WORDS', 'What each platform says it does.', [
    ('YOUTUBE', 'Watch time, then satisfaction.',
     ['12 October 2012: search and suggestions tuned for time watched — "less clicking, more watching." Today the company says it weighs "viewing behavior, likes, dislikes, subscriptions, and feedback, including from satisfaction surveys."',
      'Neal Mohan, CES, January 2018: more than 70 % of watch time comes from recommendations.']),
    ('TIKTOK', 'The For You feed.',
     ['June 2020: three kinds of signal — your interactions, the video\'s captions, sounds and hashtags, and your device and account settings. Finishing a long video counts for more than sharing a country with its maker.',
      'It will not show two videos in a row from the same sound or creator; new users pick categories or get "a generalized feed of popular videos." One billion monthly users by September 2021.']),
    ('SPOTIFY', 'Discover Weekly.',
     ['July 2015: the first personalised playlist — thirty tracks every Monday; more than 100 billion streams by June 2025. Oskar Stål, 2021: two listeners share four top artists, so each gets the other\'s fifth.',
      'Half a trillion events a day — searches, listens, likes — and the aim is "a mix of what you like and what you might like."']),
], text_size=20, notes='Three feeds, all sourced from the companies themselves; the dates are on the cards. YouTube is the arc of the objective: clicks, then watch time in 2012, then surveys — chapter five tells it properly. TikTok is the clearest public description of signals and it says two design things out loud: some signals weigh more, and the feed deliberately breaks its own pattern. Spotify is collaborative filtering explained by its own vice president in one sentence — the other person\'s fifth artist — and the exploration dial in another. Ask the room which of the three they could turn off, and how.'))

S.append(statement('Nobody drew your home screen. A rule ranked it, from what you did and from what people like you did.', eyebrow_text='02 · WHERE THIS LEAVES YOU', size=92,
                   notes='The sentence of the chapter. Week 8 said you design the space of screens; a feed is that space with a rule that assembles one screen per person per visit. Two sources of the ranking, and they are the next two chapters: what you did — the item\'s own numbers, chapter three — and what people like you did — the crowd, chapter four.'))

# ───────────────────────── 03 · an item is a point ─────────────────────────
S.append(section('03', 'An item is a point', 'features · embeddings · neighbours · content-based filtering', bg=ORANGES[0],
                 notes='Chapter three: the first way to say "this is like that". Describe a thing with numbers and it becomes a point; the recommendation is the nearest points. Where the numbers come from is the two-machines question again.'))

S.append(figure_slide('03 · EMBEDDINGS', 'Describe a thing with numbers, and it becomes a point.', F10.w10_embedding(),
                      body=['Four numbers make a lamp a point in four dimensions; every other lamp is a point too; the three nearest are what you see next. Two ways to say "near" — a straight line, or an angle — and a weight on any axis moves the whole neighbourhood.'],
                      caption='Week 4 called the word version an embedding. Same idea for a song, a poster, a chair: a list of numbers, and near means similar — by whatever the numbers measure.',
                      notes='Slow down here: this is the mechanism of the whole week. Left: one item, four axes, four numbers. Middle: the same numbers as a position; twenty-eight items; the mouse in the next slide is a query. Right: two distances, and the weighted one, which is the design decision in the sketch. Ask the room what four numbers would describe a chair for a furniture shop — price, height, material, how many legs — and then whether "comfortable" is on the list. It is not, because nobody can write it. That gap is the next slide.'))

S.append(cards('03 · WHERE THE NUMBERS COME FROM', 'Three ways to get the axes.', [
    ('BY HAND', 'You write the axes. Machine A.',
     'Price, warmth, size, metal. A tag, a genre, a colour picked from a list. Exact and explainable — "because it is also warm and small" — and blind to everything nobody wrote down. Comfort. Taste. Why.'),
    ('LEARNED', 'The network chooses the axes. Machine B.',
     'word2vec, 2013: a network places words so that words used in the same places end up near. Do it with songs, pictures, products: hundreds of axes nobody can name, learned from the examples. Fluent, and it cannot say why two things are near.'),
    ('FROM BEHAVIOUR', 'The crowd is the description.',
     'No features at all: two items are near if the same people liked both. "Customers who bought this also bought." The item can be anything — a song, a stranger, a job — because nobody looks at it. That is chapter four.'),
], text_size=22, notes='The two-machines question, applied to the axes. By hand is the rule: readable, brittle, and it misses whatever the designer did not think to write. Learned is the examples: the axes are there but unnamed, so "why is this near?" has no answer a person can read — week 4\'s embeddings again. The third is the odd one: no description of the item at all, only who touched it, and it is the one that built Amazon and Netflix. The sketch next uses the first kind, so that you can see the axes and change their weight.'))

S.append(sketch_slide('03 · LIVE · SIMILARITY SEARCH', 'The five nearest are the recommendation.',
                      live('w10-similarity', SIM_CODE, 1400, 560, hint='move the mouse = the query · T = the other metric'),
                      body=['Forty items with three hand-written features: shape, colour, size. The mouse is what you just looked at; the five nearest are what you see next. Press T and "near" changes from shape to colour — the same query, another five.'],
                      caption='Content-based filtering in one picture: no crowd, no history, only the item\'s own numbers and a distance. The axes and their weights are the design.',
                      notes='Move the query around: the five neighbours follow, with their distances in the list. Then press T, and without moving the mouse the five change, because the metric now weighs colour over shape. Say it plainly: the recommendation depends on which axis counts, and somebody chose that. For a shop, price weighs more than colour; for a moodboard, colour weighs more than price; the sketch cannot know which, and neither can the model. Ask a product designer and a communication designer in the room which metric they would ship.'))

S.append(code_slide('03 · THE METRIC', 'Distance is a design decision.', SIM_A,
                    caption='The whole mechanism is one function: a weighted distance over the features. Change the weights and you change what "similar" means — and what everyone is shown next.',
                    code_size=19, figure=F10.w10_metric(),
                    notes='The figure is the rule run twice: the same forty items, the same query, and the five nearest under each weighting — two different fives. Read dist3 aloud: three differences, each multiplied by a weight, added up, square root. That is Euclidean distance with a knob on every axis. The T key flips the knobs. Everything else in the sketch is drawing. For the workshop after the break you write this function yourself, with cosine instead of Euclidean, over ten products and five axes a language model chose for you.'))

S.append(cards('03 · CONTENT-BASED FILTERING', 'This is like what you liked.', [
    ('THE RULE', 'A profile is a point too.',
     'Average the points of what you liked; recommend the nearest to that average. Netflix\'s "because you watched", a shop\'s "similar items": the same distance, with you as the query.'),
    ('THE STRENGTH', 'It works on day one, and it can say why.',
     'A new item has features before anyone has touched it, so it can be recommended at once. And the reason is readable: "because it is also warm and small." Machine A\'s deal, again.'),
    ('THE LIMIT', 'It never leaves your neighbourhood.',
     'More of the same, forever: the tenth warm small lamp. It cannot suggest the thing you did not know you wanted, because that thing is far away by every axis it has. The crowd can.'),
], notes='Content-based in three cards. The rule is the sketch with the query replaced by your average. The strength is the cold start, in advance: an item with features needs no history, and the explanation comes free. The limit is the one every designer feels: it is a mirror. Ask the room for the feed that only ever shows you more of what you already clicked — most will name one — and then the feed that surprised them. The second needs strangers; that is next.'))

S.append(question('multiple_choice', 'Two songs are close to each other in an embedding. What does that mean?', [
    'They have the same title', 'Their numbers are similar — by whatever the numbers measure', 'The same person uploaded them', 'They were released in the same year',
], eyebrow_text='03 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. Near means the numbers are near, and the numbers measure whatever the axes measure: tempo and key if written by hand, "used in the same playlists" if learned from behaviour, nobody knows what if learned by a network. If the room says D, that is one possible axis, not the meaning. The follow-up question is the important one: who chose the axes?'))

# ───────────────────────── 04 · people like you ─────────────────────────
S.append(section('04', 'People like you', 'collaborative filtering · 1992 – 2009 · the matrix · the cold start', bg=INK,
                 notes='Chapter four: the second way to say "this is like that", and the one that made recommendation an industry. No description of the item at all — only a table of who liked what, and the rows that agree with yours.'))

S.append(figure_slide('04 · THE MATRIX', 'The matrix is mostly empty. Filling a cell is the job.', F10.w10_matrix(),
                      body=['Rows are people, columns are items, a filled cell is a like. Almost every cell is empty — Netflix\'s 2006 table was about 1.2 % full — and the recommendation is a guess at one empty cell in your row. Three ways to guess: the rows that agree with yours, the columns that co-occur with what you liked, or a point for every row and every column.'],
                      caption='Twelve fictional listeners, ten items. The teal rows agree with yours; the violet column co-occurs with what you liked; the ? is the cell the next slide fills in, live, from the same table.',
                      notes='The matrix is the whole of collaborative filtering. Point at the ? and ask how you would fill it with no idea what A, C and D are. The room will say: look at U1, U4 and U7, they liked what I liked, and two of them liked C. That is user–user. Or: everyone who liked A and D also liked C. That is item–item. The third way is the Netflix Prize trick: give every person and every item a short list of numbers so that the product of the two predicts the cell — an embedding learned from the matrix alone, chapter three\'s point without a single feature. Say the 1.2 % again: it is why every guess is a guess.'))

S.append(sketch_slide('04 · LIVE · COLLABORATIVE FILTERING', 'People like you liked this.',
                      live('w10-collab', COLLAB_CODE, 1400, 560, hint='click a cell in your row to like · hover a column'),
                      body=['You are the last row. Click to like an item; the sketch finds the three rows most like yours by cosine similarity and lets them vote on everything you have not liked. The tinted cells are the prediction; the top three are your feed.'],
                      caption='Nobody in this picture knows what an item is. Like two things and you have neighbours; like everything and you are like nobody; like nothing and it has nothing to say.',
                      notes='Click B: U1 and U7 rise to the top and F appears in the predictions. Click something from another taste group — H, say — and watch the similarities fall and a stranger enter: U6, who liked D and H, is now as close to you as U4, and J, a taste you never showed, enters the predictions. Unlike everything: the cold start, nothing to say. The point to make slowly: there is no description of any item anywhere in this program. The crowd is the description, and it is machine B in its purest form — examples, no rule about what a thing is. Hover a column to see how many liked it: popular items are easy to predict; the long tail is where every system is bad.'))

S.append(cards('04 · THREE DATES', 'Collaborative filtering, in three dates.', [
    ('1992 · TAPESTRY', 'The term is coined at Xerox PARC.',
     'Goldberg, Nichols, Oki and Terry, Communications of the ACM: people annotate their incoming mail and news, and others filter by those annotations. The first system to let strangers\' reactions decide what you read.'),
    ('1994 · GROUPLENS', 'Ratings predict ratings.',
     'Resnick and colleagues at CSCW: Usenet news articles rated by readers; your predicted rating comes from readers who rated the way you did. User–user, with an open architecture so any newsreader could join.'),
    ('2003 · AMAZON', 'Item-to-item scales to millions.',
     'Linden, Smith and York, IEEE Internet Computing: compare items to items instead of customers to customers, offline, once — and "customers who bought this also bought" runs for every product page.'),
], text_size=22, notes='Three dates, one idea. Tapestry named it: filtering done collaboratively, by other people\'s reactions. GroupLens made it automatic and user–user. Amazon turned it item–item because comparing millions of customers to each other every night was impossible and comparing items was not — an engineering decision that became the sentence on every shop in the world. Ask: which of the three did your bias register\'s product most resemble? Then the prize that made it a science.'))

S.append(cards('04 · THE NETFLIX PRIZE · 2006 – 2009', 'A million dollars for ten percent.', [
    ('THE BET', '2 October 2006.',
     'US$1,000,000 to whoever beat Netflix\'s own Cinematch by 10 % — from an error of 0.9525 to 0.8572 on a hidden test set. The data: 100,480,507 ratings by 480,189 people on 17,770 films, "anonymised".'),
    ('THE WIN', '21 September 2009.',
     'BellKor\'s Pragmatic Chaos, a team of teams, at 0.8567. What worked: giving every person and every film a short list of learned numbers — matrix factorisation — which the winners called superior to nearest-neighbour methods (Koren, Bell & Volinsky, 2009).'),
    ('THE LESSON', 'The sequel was cancelled.',
     'Narayanan and Shmatikov re-identified people in the ratings by matching them with public reviews on IMDb. A lawsuit and privacy concerns at the FTC followed; Netflix dropped the second prize. Week 9\'s linkage, on the most famous dataset in the field.'),
], text_size=21, notes='The prize is worth three minutes because it contains the whole module. The bet: a public dataset and one number to beat, which is how machine B research works. The win: the method that won is chapter three\'s embedding learned from chapter four\'s matrix — a point per person, a point per film, no feature written by hand. The lesson is last week\'s: "anonymised" ratings plus a public site equals names. When a team says its data is anonymous, ask what it can be joined to.'))

S.append(cards('04 · THREE FAMILIES', 'Like what you liked. Liked by people like you. Both.', [
    ('CONTENT-BASED', 'The item\'s own numbers.',
     'Works from day one for a new item; can say why; never leaves your neighbourhood. Needs the axes: written by hand, or learned from the item itself.'),
    ('COLLABORATIVE', 'The crowd\'s behaviour.',
     'No description needed; finds the thing you did not know you wanted, because someone like you did. Nothing to say about a new person or a new item, and it cannot say why beyond "people like you".'),
    ('HYBRID', 'Both, in one model.',
     'Every real feed. The item\'s features and the crowd\'s clicks go into the same score; the two towers next slide are the shape it usually takes. The cold start of one is covered by the other.'),
], notes='Three families, and the third is the answer in practice. The exam question is the first two: what each needs, what each cannot do. The design question is the third: when your product has features and a crowd, which one wins in the score, and does the person know? Spotify\'s Stål described the collaborative side in one sentence — the other listener\'s fifth artist; what the item tower adds is the next slide.'))

S.append(figure_slide('04 · TWO TOWERS', 'Two towers, in a sentence.', F10.w10_two_tower(),
                      body=['One network turns the person into a point, another turns the item into a point, in the same space; the score is one multiplication. The item points are computed once and stored, so finding the nearest for a person is a similarity search over the whole catalogue — tens of millions of videos at YouTube.'],
                      caption='Covington, Adams & Sargin, RecSys 2016: candidate generation, then ranking. Yi et al., RecSys 2019: the two-tower retrieval model, deployed for YouTube. The sentence for your poster is on the figure.',
                      notes='One slide, one sentence, no more: two towers make two points, near means recommended. It matters for the project because it is the hybrid drawn: the item tower can eat features (content) and the person tower can eat history (the crowd), and both end in the same space. If a team says "we would use a model", this is the picture to ask them to point at: what goes into each tower, and what is the score? Do not go deeper; the ranking stage, with its many objectives, is chapter five.'))

S.append(cards('04 · THE COLD START', 'Day one, nobody knows you.', [
    ('A NEW PERSON', 'Her row is empty.',
     'Collaborative filtering has nothing to say. TikTok\'s answer, in its own words: ask new users to pick categories, or start with "a generalized feed of popular videos". Spotify builds a taste profile from the first listens. The onboarding is the cold start, designed.'),
    ('A NEW ITEM', 'Its column is empty.',
     'Nobody has clicked it, so the crowd cannot vote. Content-based filtering can place it from its features at once; a feed can also give it a slot on purpose — a try, shown to a few people, to learn. That slot is the exploration dial.'),
    ('THE FALLBACK', 'What everyone gets.',
     'Week 8\'s fourth branch: the most popular, the editors\' pick, the same screen for all. On day one every product is this. If the fallback is bad, the first day is bad, and most people leave on the first day.'),
], text_size=22, notes='The cold start is a design problem before it is a technical one. The new person: the questionnaire on the first screen is not onboarding decoration; it is the only row the model has. The new item: the same for a creator\'s first video, a new product, a new restaurant — someone decides whether it gets a chance. The fallback: what everyone sees when the model has nothing, and it is the product most new users judge. Ask each team later what their product shows on the first day; "nothing yet" is the honest answer for most.'))

S.append(question('multiple_choice', 'A brand-new user opens the app. Which system has the least to say?', [
    'Content-based filtering: it has the item features', 'Collaborative filtering: her row is empty', 'A popularity list: the same for everyone', "An editor's pick",
], eyebrow_text='04 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. With an empty row there is nobody like her, so the crowd cannot vote; the other three work without knowing her at all. Content-based needs only the items\' features and one signal from her — which is why so many first screens ask you to pick three things you like. The real design answer is "a mix, and here is what she sees on day one"; that is the fallback row of the decision card from week 8.'))

S.append(statement('A recommendation is a neighbour. Which distance, and whose neighbours, is the design.', eyebrow_text='04 · WHERE WE ARE', size=100,
                   notes='The sentence to carry across the break. Chapter three: the item\'s own numbers and a distance. Chapter four: the crowd\'s behaviour and a similarity. Either way, near means recommended, and somebody chose what near means. After the break: the number the model is told to make bigger — and what that does to the person on the other side.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · THE OBJECTIVE · THE FEED AS A MEDIATION · THEN YOUR OWN SEARCH', size=120, bg=PAPER,
                   notes='1:18. Back at 1:33. One laptop per team when you come back, logged into editor.p5js.org and genai.polyu.edu.hk; the TAs help anyone who is not. Paper and pens on the tables for the activity.'))

# ───────────────────────── 05 · the objective ─────────────────────────
S.append(section('05', 'The objective', 'engagement · the attention trap · bubbles · Pariser 2011', bg=ORANGES[0],
                 notes='Chapter five: the score. A model is trained to make one number bigger, and the number is chosen by a person. This chapter is what happens when that number is attention — and the sketch has a dial for the way out.'))

S.append(statement('The model optimises what you click, not what you value.', eyebrow_text='05 · THE ATTENTION TRAP', size=110,
                   notes='Say it once, then unpack it. A model cannot see what you value; it can see what you did. It is trained on the second and it will, tirelessly and at scale, find whatever makes the second number bigger. If the second is a good proxy for the first, fine. It stops being a good proxy the moment it becomes the target — the next figure.'))

S.append(figure_slide('05 · FOUR STEPS DOWN', 'Value, proxy, target, trap.', F10.w10_objective(),
                      body=['What a person values cannot be measured, so a proxy is measured instead; the model maximises the proxy exactly; the product becomes whatever makes the proxy biggest. The repair is to measure closer to the value and to write rules around the number.'],
                      caption='Goodhart, 1975; Strathern, 1997: "when a measure becomes a target, it ceases to be a good measure." The most important sentence in your mediation brief is the number the model makes bigger.',
                      notes='Walk down the steps. One: an evening well spent — nobody can log that. Two: minutes watched — you can log that, and on average it is not a bad proxy. Three: the model is told to maximise step two, and it does, with no idea that step one exists. Four: the product becomes whatever produces minutes — autoplay, the cliffhanger, the thing that makes you angry, because anger keeps you watching. Strathern\'s sentence is Goodhart\'s law; say it twice. The repair box is the chapter after this one. Ask: what is the proxy in your product?'))

S.append(cards('05 · YOUTUBE, THREE OBJECTIVES', 'Clicks, then watch time, then satisfaction.', [
    ('2012 · WATCH TIME', '"Less clicking, more watching."',
     'YouTube, 12 October 2012: search results re-ranked to reward videos that keep people watching, after the same change to suggested videos in March. The objective moved from the click — which clickbait wins — to the minute.'),
    ('2016 · EXPECTED WATCH TIME', 'The ranking model\'s target.',
     'Covington, Adams & Sargin, RecSys 2016: a deep network for candidate generation, and a ranking network trained to predict expected watch time. The proxy from 2012, now the loss function of a neural network.'),
    ('2019 · SATISFACTION', 'Two groups of objectives.',
     'Zhao et al., RecSys 2019: "engagement objectives, such as user clicks, and degree of engagement with recommended videos" and "satisfaction objectives, such as user liking a video on YouTube, and leaving a rating on the recommendation." Surveys enter the score.'),
], text_size=21, notes='One company, seven years, three objectives, all from its own posts and papers. 2012 is the honest moment: clicks rewarded clickbait, so they moved the target to time — and time rewarded something else. 2016 is the proxy inside the network. 2019 is the repair from the last figure: a second group of objectives, closer to the value, including what people say when asked. Note the word "satisfaction" is theirs. The design lesson is not that YouTube is good or bad; it is that the objective was chosen three times by people, and each time the product changed shape.'))

S.append(sketch_slide('05 · LIVE · THE ECHO CHAMBER', 'The attention trap has a dial.',
                      live('w10-feed', FEED_CODE, 1400, 560, hint='click a card = engage · mouse y = exploration · R restarts'),
                      body=['Eight topics; twelve cards drawn from what the feed thinks you like. Every click moves the feed towards that topic. Before you arrived, twelve screens went by with no exploration and a person who clicked whatever was commonest — no taste at all. The line is how many topics the last fifty cards really covered — eight when they are spread evenly, one when they are all the same; mouse y is the exploration rate.'],
                      caption='A feed with no exploration invents a taste for a person who had none, in a dozen clicks. Turn the dial down the canvas and the line climbs back — at the price of cards you did not ask for.',
                      notes='Start where the still is: one topic has most of the weight and the diversity line is already down to about two — and the person who produced that had no preference; they clicked the commonest card, and the loop did the rest. Move the mouse to the top — zero exploration — and click the commonest card ten times: the line drops towards one; this is the trap, and nobody designed it, the objective did. Now move to the bottom — fifty percent — and click the hollow cards, the tries: the weight spreads and the line climbs. Somewhere in between is a design decision every feed makes and few make on purpose. Ask the room where they would set it for a music app, for a news app, for a dating app. Different numbers; same model.'))

S.append(quote('"When a measure becomes a target, it ceases to be a good measure."',
               'Marilyn Strathern, "Improving ratings": audit in the British University system, European Review 5(3), 1997 — the sentence usually called Goodhart\'s law', size=88,
               notes='Strathern wrote it about university audits, citing Goodhart\'s 1975 point about monetary targets; it has become the one-line theory of every metric-driven product. For the activity: your team names the number, then names what the model will do to that number that you did not mean. That second line is this sentence, applied.'))

S.append(cards('05 · BUBBLES', 'Echo chamber, filter bubble, and what the evidence says.', [
    ('2001 · SUNSTEIN', 'The echo chamber: you filter yourself.',
     'Republic.com: with enough choice, people read only what they already agree with — Negroponte\'s "Daily Me" of 1995, read darkly — and a democracy loses the experiences it did not choose. The filter here is the person.'),
    ('2011 · PARISER', 'The filter bubble: the algorithm filters for you.',
     'The Filter Bubble: What the Internet Is Hiding from You, and the TED talk of March 2011: two friends search "Egypt" and get different results. TED\'s summary: "we get trapped in a \'filter bubble\' and don\'t get exposed to information that could challenge or broaden our worldview." Invisible, unchosen.'),
    ('2015 · THE EVIDENCE', 'Measured, the effect is smaller than the fear.',
     'Bakshy, Messing and Adamic, Science, 2015: 10.1 million Facebook users; what friends shared and what people chose to click narrowed their news more than the ranking did. Zuiderveen Borgesius et al., 2016, reviewing the studies: "little empirical evidence that warrants any worries about filter bubbles." Real in some feeds, small in others: measure yours.'),
], text_size=21, notes='Two words that get mixed up, and a caution. Sunstein\'s chamber is chosen: the person filters. Pariser\'s bubble is not: the ranking filters, and you cannot see what was removed — that is why it is a design problem and not a taste problem. Then the honest slide: when researchers measured it on Facebook in 2015, individual choice narrowed exposure more than the algorithm did, and the 2016 review by Zuiderveen Borgesius and colleagues in Internet Policy Review found little empirical evidence that warranted the worry — while warning that stronger personalisation could change that. The sketch shows the mechanism exists; the evidence says its size depends on the product. So: measure it — the diversity line is one number your product could log.'))

S.append(question('multiple_choice', 'Your feed is trained to maximise minutes spent. Which of these will it learn to do?', [
    'Show shorter videos', 'Show what keeps you watching — whether or not you are glad afterwards', 'Show what you rated highly last year', 'Show fewer videos',
], eyebrow_text='05 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. The model has minutes and nothing else; anything that produces minutes is rewarded, including the thing you regret. A is backwards — longer keeps you longer; C is a different objective, a rating; D loses minutes. The follow-up is chapter six: what number would you give it instead, and what would that cost?'))

# ───────────────────────── 06 · the feed as a mediation ─────────────────────────
S.append(section('06', 'The feed as a mediation', "Ihde's relations · the objective · why am I seeing this · the dial", bg=PAPER,
                 notes='Chapter six: the designer\'s three handles on a feed, with week 5\'s vocabulary. Which relation a feed is; which number to give the model; how the feed explains itself; and the dial.'))

S.append(figure_slide('06 · IHDE', 'A feed is mostly hermeneutic, and mostly background.', F10.w10_relations(),
                      body=['Week 5\'s four relations, with a feed in each. The scroll is embodied and the DJ talks, but a feed mostly does two things: it is a reading of the world you look through — "this is what is happening" — and it runs while you are not looking. Both are relations a person does not notice, which is the point of designing them.'],
                      caption='Ihde, Technology and the Lifeworld, 1990; Verbeek, Beyond Interaction, 2015. The mediation brief names the relation; for a feed, say which of the two — and where the person gets to see it decide.',
                      notes='Go across. Embodiment: the thumb, a little. Hermeneutic: mostly — the feed is a thermometer for the world, and a reading can be wrong; nobody checks a thermometer. Alterity: a little, when it talks. Background: mostly — it decides while you sleep and never presents the decision as one. The bars are our estimate, not a measurement; say so. The last line of the figure is the bridge to the transparency slide: "why am I seeing this" makes the feed face you for a moment. Verbeek\'s line from week 1: designing things is designing human existence; a feed designs what a person takes to be the world.'))

S.append(cards('06 · DESIGNING THE OBJECTIVE', 'Three numbers you could make bigger.', [
    ('TIME SPENT', 'Cheap, immediate, and the trap.',
     'Logged for free on every screen; a fine proxy on average. It is what the sketch optimised, and it rewards the cliffhanger and the outrage as much as the good evening. Ask what a person would say if you told them.'),
    ('SATISFACTION', 'Ask, afterwards.',
     'A survey after the fact — "was this worth your time?" — YouTube\'s second group of objectives. Slow, sparse, and honest: a few answers weigh against millions of minutes. The design question is when to ask, and whom.'),
    ('RETURN, AND REGRET', 'Did she come back? Did she say no?',
     'A return next week is a number that only a good evening produces. A "not interested", an "exclude from my taste profile" — TikTok\'s and Spotify\'s own controls — is a number that says no. Count the no.'),
], notes='Three candidates for the number, from cheap to honest. Time is the default because it is free; the second and third cost a question or a button, and each is machine A around machine B — a rule about what counts. For the brief: name the number, name what it costs to collect, name who it ignores (people who never answer surveys are thin in the data, last week\'s column). Ask the room which of the three their own favourite app seems to use; the answer is usually the first, and they can tell.'))

S.append(cards('06 · WHY AM I SEEING THIS', 'Three explanations, and a law.', [
    ('FACEBOOK · 2019', '"Why am I seeing this post?"',
     '31 March 2019: a menu on every post, from the obvious — you are friends — to the not obvious — you comment more on photos. The first time the ranking was explained inside the app; the ad version had existed since 2014.'),
    ('TIKTOK · 2022', '"Why this video."',
     '20 December 2022: share panel, question mark. Reasons: "user interactions", "accounts you follow or suggested accounts for you", "content posted recently in your region", "popular content in your region." Four kinds of neighbour, in plain words.'),
    ('SPOTIFY · 2018', 'Explanations as part of the model.',
     'McInerney et al., RecSys 2018: "recsplanations" — the model learns which explanation each listener responds to, alongside what to recommend, and balances exploring with exploiting. The reason is a design decision too.'),
    ('THE LAW · DSA', 'Plain language, and a way out.',
     'The EU Digital Services Act, in force for the largest platforms since 25 August 2023. Article 27: the main parameters of the recommender, in plain and intelligible language, with options to change them. Article 38: at least one option not based on profiling.'),
], text_size=20, notes='Transparency in four moves, three of them products and one a law. Facebook and TikTok show the shape: three or four reasons, in the person\'s words, mapped onto the kinds of neighbour from chapters three and four. Spotify shows the twist: the explanation is itself chosen by a model, which is a design decision with an objective inside it. The DSA sets the floor for anything shipped in Europe: say the parameters, offer a non-profiled option. Round three of the activity is this slide on paper: your product\'s "why", in her words, with the data each reason used.'))

S.append(cards('06 · THE EXPLORATION DIAL', 'How much of the feed is not for you yet.', [
    ('EXPLOIT', 'The best guess.',
     'Show the highest score. Safe, sharp, and a mirror: the sketch at zero. Every recommendation is a hit and nobody learns anything, including the model.'),
    ('EXPLORE', 'A try, and a lesson.',
     'A slot for the uncertain item — the new video, the fifth artist. Stål, 2021: "a mix of what you like and what you might like." TikTok says it out loud: sometimes a video "doesn\'t appear to be relevant to your expressed interests." The bandit trade-off, in the interface.'),
    ('THE RESET', 'Start fresh.',
     'TikTok, 16 March 2023: refresh your For You feed and it starts as if you had just signed up; following, profile and inbox untouched. The dial turned to the beginning — a control most feeds do not have.'),
    ('THE SHARED ROW', 'What everyone sees.',
     'Netflix Top 10, 24 February 2020: one row that is the same for everyone in your country. The part of a feed you can talk about with a friend — the piece of the common world personalisation removes.'),
], text_size=21, notes='The dial has four positions to design. Exploit and explore are the two ends; the sketch is the slider between them, and it is a number somebody sets. The reset is a control that admits the model can be wrong about you, and gives you back the cold start on purpose. The shared row is the one to say slowly: it is the answer to Sunstein — the experience you did not choose — and it is cheap. Round four asks each team for its number.'))

S.append(statement('You design the objective, the explanation and the dial. The model does the rest.', eyebrow_text='06 · WHERE THIS LEAVES YOU', size=100,
                   notes='The three handles, and the activity is all three. Not "make a better model": the model will make the score whatever you decide. You decide what number it makes bigger, how it tells the person why, and how much of the screen is a try. Those are rules — machine A — around the examples. Now the workshop: a similarity search of your own — ten minutes hands-on, about fifteen with the prompt and the debrief.'))

# ───────────────────────── 07 · workshop: similarity search by hand ─────────────────────────
S.append(section('07', 'Similarity search, by hand', f'ten products · five numbers · {GENAI} · {P5}', bg=INK,
                 notes='Chapter seven, hands-on: the mechanism of chapter three, built by each team — ten minutes hands-on, about fifteen with the prompt and the debrief. A language model writes the axes and the numbers; a twenty-six-line script finds the neighbours; you judge whether they make sense — and whose axes they were.'))

S.append(two_col('07 · THE PROMPT', 'Ask the model for the numbers, not the answer.',
                 ['Ten one-line descriptions of products your team knows — chairs, snacks, apps — or the ten on the next slide.',
                  f'- Paste them with the template into a language model on **{GENAI}**. It chooses five axes and gives every product five numbers: an embedding, by hand, by a machine.',
                  '- Step 3 is the model searching in words; step 4 changes the metric.',
                  'Keep the table: it goes into the script. Keep the axes: who chose them?'],
                 PROMPT, right_size=21, left_size=27,
                 notes='The template is on the course site and on Blackboard. The trick of the exercise: we ask the model for features and numbers — a description, machine A style — and not for a recommendation, so that the search is done by a rule you can read. Any language model on GenAI will do; stay with one. Watch step 1: the axes it chooses are its idea of what a buyer cares about, which is the dataset\'s idea, which is the week-9 question again. Step 4 is the T key from the sketch.'))

S.append(code_slide('07 · THE SCRIPT', 'Twenty-six lines find the neighbours.', VECTORS_CODE,
                    caption='Ten fictional products, five numbers each, one cosine function, a sort. Replace the names and the table with the model\'s; change w to change the metric.',
                    code_size=18, sketch=live('w10-vectors', VECTORS_CODE, 800, 600, hint='click = next product · mouse x = the weight on price', extra=VECTORS_EXTRA),
                    notes='Read it top to bottom: the names, the table, the weights, the query. cosine() is chapter three\'s angle with a weight per axis — the same knob as dist3 in the sketch. draw() sorts everything by similarity and prints the top three. In the html deck the script runs live: click cycles the product you looked at, and the mouse moves the weight on price from zero to three; watch the neighbours change. The script is on the site; students paste it into the editor and replace the table.'))

S.append(activity('LIVE', 10, 'Ten products, five numbers, three neighbours.',
                  [f'One laptop per team. Put your ten descriptions and the template into a language model on **{GENAI}**. Keep the five axis names.',
                   f'Paste the script from the site into **{P5}**; replace **names** and **v** with the model\'s table. Play.',
                   'Compare: the model\'s three nearest (step 3) and the script\'s. Then set **w** so that price counts three times. Which neighbour left?'],
                  eyebrow_text='07 · HANDS ON', bg=YELLOWS[0],
                  notes='Ten minutes; the TAs walk. Typical errors: a missing comma in the table, a row with four numbers, names and v of different lengths. The comparison is the point: the model\'s answer in words and the script\'s answer from its own numbers usually differ, because the model did not actually compute — it guessed a plausible list. The script is machine A over numbers machine B wrote. Teams that finish early: add a sixth axis the model did not think of.'))

S.append(content('07 · WHAT TO LOOK FOR', 'Did the neighbours make sense? Whose axes were they?',
                 ['- **The axes.** Five numbers a buyer cares about, chosen by a model trained on other people\'s shops. Is "comfortable" there? "Made nearby"? Whatever is missing cannot be recommended.',
                  '- **The disagreement.** The neighbour you would never have suggested. Find the axis that put it there; that is what the metric thinks matters.',
                  '- **The weight.** Price times three moved the neighbourhood. In your product, which axis should count most — and who decided?',
                  'Write the five axes into your notes. They are the first line of the "why am I seeing this" screen you draw next.'],
                 body_size=30,
                 notes='Three minutes, two or three teams speaking. The most useful thing to surface is the missing axis: the model chose what a buyer cares about, and left out what your person cares about. That is content-based filtering\'s limit and the week-9 grain in one exercise. The five axes carry straight into round three of the activity, as the reasons a person could be given.'))

# ───────────────────────── 08 · activity: your feed's objective ─────────────────────────
S.append(section('08', "Your feed's objective.", '28 minutes · your team · paper · one phone per team', bg=YELLOWS[0],
                 notes='The activity. Four rounds at the team table, each ending in ClassPoint: the number your model makes bigger, the number it will actually chase, the screen that explains a recommendation, and the dial. Nicolò keeps time; Amber, WU Zhao and MA Jie walk. One A4 per team for round three, one phone for the upload.'))

S.append(activity('1 — TEAMS · THE OBJECTIVE', 3, 'What number does your model make bigger?',
                  ['One number. The one a developer would put in the code as the thing to maximise, for each person.',
                   'Write it as the sentence on the right. If there is no number, write **"none yet"** and say why — that is a finding.',
                   'The scribe types it. Team number first.'],
                  panel=OBJECTIVE_PANEL, panel_size=20, bg=YELLOWS[0],
                  notes='Three minutes and a hard stop. Most teams will write a value — "help her eat well" — and the TAs\' one question is: what would you log? Push until it is a number per person per time. A team that honestly cannot name one has found that its product is a rule, not a model, and that is a good line for the brief.'))

S.append(question('short_answer', 'Team number, and the objective your model optimises.',
                  hint='One line, scribe only. "Team 12: maximise dinners cooked from a suggestion, per week." Or "Team 12: none yet — it is a rule, not a model."',
                  eyebrow_text='08 · CAPTURE 1 · SHORT ANSWER · ONE PER TEAM',
                  notes='ClassPoint short answer, two minutes, one per team. Read five aloud, fast, without comment. Sort them in your head into time, satisfaction and return — the three cards from chapter six. Most are time or count. Keep the screen: the next round writes the second line under each.'))

S.append(activity('2 — TEAMS · THE DRIFT', 3, 'What will it learn to do that you did not mean?',
                  ['Your number, made bigger by the cheapest route. What is the route? What does the person get?',
                   'Strathern\'s sentence is on the right. Fill the blanks: **it will learn to ___, and the person will ___.**',
                   'Be unkind to your own product. The model will be.'],
                  panel=DRIFT_PANEL, panel_size=20, bg=YELLOWS[1],
                  notes='Three minutes. This is the step-four box from the figure, applied to their own number. The TAs help teams that say "nothing": ask what a lazy intern paid per unit of that number would do. Every objective has a cheap route; the teams that find theirs fastest have the clearest number.'))

S.append(question('short_answer', 'Team number, and the wrong objective it could drift to.',
                  hint='One line, scribe only. "Team 12: it will learn to suggest the same three easy dishes forever, and she will stop opening it."',
                  eyebrow_text='08 · CAPTURE 2 · SHORT ANSWER · ONE PER TEAM',
                  notes='ClassPoint short answer, two minutes. Now read pairs: the objective from the last screen, then the drift from this one, for the same team number. Five pairs. The room hears Goodhart\'s law twenty-five times in their own products. The two lines together are the objective row of the mediation brief; say so.'))

S.append(activity('3 — TEAMS · WHY AM I SEEING THIS', 8, 'Draw the explanation.',
                  ['One A4, landscape. The screen a person sees when she taps **"why?"** on one recommendation of your product.',
                   'The four parts on the right: the item, **three reasons in her words**, the data each reason used — including one she did not know you had — and the controls.',
                   'Big letters. This is page one of prototype v1.'],
                  panel=WHY_PANEL, panel_size=20, bg=YELLOWS[2],
                  notes='Eight minutes; the longest round. The TAs read over shoulders for two things: reasons written in the product\'s words ("high affinity score") instead of hers, and a data line that hides the uncomfortable signal — the location, the time of night, the thing she looked at and did not buy. The one she did not know you had is compulsory; that is the honesty of the screen. Controls: at least "less like this" and the dial. The photo goes on the wall next.'))

S.append(question('image_upload', 'One per team: the "why am I seeing this" screen.',
                  hint='One photo, one per team. Caption: the team number, then the first reason, word for word.',
                  eyebrow_text='08 · CAPTURE 3 · IMAGE UPLOAD · ONE PER TEAM',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='ClassPoint image upload, one phone per team, about twenty-five images, caption required. Put the wall on screen. Read three captions without the picture and ask the room which kind of neighbour it is — the item\'s own numbers, or people like you. Then pick two screens: one where the data line is honest, one where it is missing, and ask what the person would think of each. Download the submissions after class: Amber reads them against the prototypes.'))

S.append(activity('4 — TEAMS · THE DIAL', 2, 'Set the exploration dial.',
                  ['How much of your feed is **not the best guess**? Zero, one in ten, a third, half.',
                   'Decide as a team in two minutes, then everyone votes on the next slide.',
                   'Write the number on your screen, next to the controls.'],
                  panel=DIAL_PANEL, panel_size=20, bg=YELLOWS[0],
                  notes='Two minutes. There is no right number and the teams should feel the trade: zero is the mirror, half is noise. The useful question from the TAs: what does a try cost your person — a wrong song, or a wrong medical nudge? The cost decides the number. Then the vote.'))

S.append(question('multiple_choice', 'How much exploration should your feed have?', [
    '0 %: only the best guess', '10 %: one card in ten is a try', '30 %: a third of the feed is new', '50 % or more: half chance',
], eyebrow_text='08 · THE DIAL · MULTIPLE CHOICE · EVERYONE',
    notes='Everyone votes, one minute. No correct answer: show the split, and ask one team at each end to say why. The pattern worth naming: teams whose wrong recommendation is cheap choose high; teams whose wrong recommendation hurts choose low — and the ones who chose zero have built the mirror from the sketch. The number goes on the screen and into the brief.'))

S.append(content('08 · WHAT JUST HAPPENED', 'Every feed is an objective, an explanation and a dial.',
                 ['Twenty-five products; each now has a number its model makes bigger, the cheap route that number invites, a screen that says why, and a share of the screen that is a try. That is the whole of chapter six, in your handwriting.',
                  'The model will make the score from neighbours — the item\'s own numbers, or people like you. You chose what "near" means, what the score is for, and how the person is told.',
                  'Verbeek, week 1: designing things is designing human existence. A feed designs what a person takes to be the world, and does it in the background. The "why" screen is where it faces her.',
                  '**The model finds the neighbours. You decided the objective, the explanation and the dial. That was the design.**'],
                 body_size=30,
                 notes='Mirror of the whole class. Say the four things each team now has, then the two sources of neighbours, then the last line slowly — it is the week-8 last line with the three handles filled in. Point at the homework and let them go; the TAs stay thirty minutes for the prototype review.'))

S.append(cards('08 · BEFORE WEEK 11', 'Prototype v1, the poster, the brief, Belamy.', [
    ('PROTOTYPE V1', 'Before the week-11 class, on Blackboard.',
     'Paper, Figma or code, one per team: the moment your product decides and what the person sees — and the "why am I seeing this" screen from today as page one. The date week 9 gave. The TAs review what exists thirty minutes after class.'),
    ('THE DRAFT POSTER', 'Start it now, not in week 12.',
     'A0, the research and the concept. Next week is the poster lab: bring a draft — even a sketch of the layout with the decision sentence at the top. The maker owns it; everyone brings a paragraph.'),
    ('THE MEDIATION BRIEF', 'One page. Four rows, plus today\'s two.',
     'The relation (hermeneutic? background?), the data, the bias, the guardrails — and now the objective with its drift, and the explanation. Draft it for next week; the register and today\'s three captures are the raw material.'),
    ('BELAMY', 'Watch it before week 11.',
     'Obvious, "Generation of Edmond de Belamy": how the portrait that sold at Christie\'s in 2018 was made. Next week asks who made it — the collective, the coder, the painters behind the fifteen thousand portraits in the dataset.'),
], text_size=21, notes='Four things. Prototype v1 is this sprint\'s increment and it is due on Blackboard before the week-11 class — the date week 9 gave; Amber posts it tonight. The poster and the brief are next sprint\'s, and next week is the lab, so a draft has to exist. Belamy is the video for next week and the quiz draws on it. Say the three deadlines once more, slowly.'))

S.append(video('08 · HOMEWORK · WATCH BEFORE WEEK 11', 'Who made this?', 'Pu2GZ3du7PI',
               ['Obvious, "Generation of Edmond de Belamy": the portrait from week 1, and how it was made — a network trained on portraits, an output chosen, a signature that is a formula.',
                '- Watch it before next week. Week 11 is curating outputs and datasets: which of the hundred generated faces ships, and whose paintings taught the model.',
                '- On the playlist. Bring one sentence: who is the author?'],
               thumb='yt/Pu2GZ3du7PI.jpg',
               notes='Play the first thirty seconds if there is time. Next week opens with it: the collective that chose the output, the coder whose model they used, the painters whose portraits are in the dataset, and what a court and the Copyright Office say about each. Ask them to arrive with an answer to "who made this?" — the room will disagree, which is the class.'))

S.append(end('See you next week. Curators of outputs and datasets.',
             'Upload prototype v1. Draft the poster and the brief. Watch Belamy.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: module 4 opens — output selection and gatekeeping, fine-tuning and LoRA datasets, authorship and ownership, the Thaler cases; and the poster lab begins. Homework in one line: prototype v1 on Blackboard, a draft poster and a draft mediation brief to bring, and the Belamy video. The TAs stay for 30 minutes: the prototype review.'))

DECK = dict(title='SD2112 · AI in Design · Week 10', slides=finalize(S, FOOTER), pdf='SD2112-week10.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week10', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 5–6 September 2026)
# Netflix Prize (2 October 2006; US$1M; Cinematch RMSE 0.9525 on the test set (0.9514 on the quiz set), target 0.8572 test (0.8563 quiz);
#   BellKor's Pragmatic Chaos 0.8567 test, 21 September 2009;
#   100,480,507 ratings, 480,189 users, 17,770 movies; the cancelled sequel, Narayanan & Shmatikov): https://en.wikipedia.org/wiki/Netflix_Prize
# Koren, Bell & Volinsky (2009). Matrix factorization techniques for recommender systems. IEEE Computer 42(8): 30–37: https://dl.acm.org/doi/10.1109/mc.2009.263
# Pariser, The Filter Bubble: What the Internet Is Hiding from You (Penguin, 2011); the "Egypt" example; the critiques: https://en.wikipedia.org/wiki/The_Filter_Bubble
# Pariser, TED, March 2011, "Beware online 'filter bubbles'" (TED's summary sentence quoted on the bubbles card): https://www.ted.com/talks/eli_pariser_beware_online_filter_bubbles
# YouTube, 12 October 2012, "YouTube search, now optimized for time watched" ("less clicking, more watching"; Suggested Videos in March):
#   https://blog.youtube/news-and-events/youtube-search-now-optimized-for-time/
# Covington, Adams & Sargin (2016). Deep neural networks for YouTube recommendations. RecSys 2016 (candidate generation, ranking, expected watch time):
#   https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/
# Zhao et al. (2019). Recommending what video to watch next: a multitask ranking system. RecSys 2019 (engagement vs satisfaction objectives, "a few hundred candidates"):
#   https://research.google/pubs/recommending-what-video-to-watch-next-a-multitask-ranking-system/ · https://dl.acm.org/doi/10.1145/3298689.3346997
# Yi et al. (2019). Sampling-bias-corrected neural modeling for large corpus item recommendations. RecSys 2019 (two towers; tens of millions of videos):
#   https://research.google/pubs/sampling-bias-corrected-neural-modeling-for-large-corpus-item-recommendations/
# YouTube, How YouTube works — recommendations (viewing behavior, likes, dislikes, subscriptions, satisfaction surveys):
#   https://www.youtube.com/howyoutubeworks/product-features/recommendations/
# Neal Mohan, CES, January 2018: more than 70 % of watch time from recommendations: https://www.tubefilter.com/2018/01/11/youtube-most-watch-time-driven-by-recommendations/
#   and https://qz.com/1178125/youtubes-recommendations-drive-70-of-what-we-watch
# TikTok, 18 June 2020, "How TikTok recommends videos #ForYou": https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you
# TikTok, 20 December 2022, "Learn why a video is recommended For You": https://newsroom.tiktok.com/en-us/learn-why-a-video-is-recommended-for-you
# TikTok, 16 March 2023, "Introducing a way to refresh your For You feed": https://newsroom.tiktok.com/en-us/introducing-a-way-to-refresh-your-for-you-feed-on-tiktok-us
#   and https://techcrunch.com/2023/03/16/tiktoks-new-feature-lets-you-refresh-your-for-you-feed-and-retrain-your-algorithm/
# TikTok, 27 September 2021, "Thanks a billion" (one billion monthly users): https://wersm.com/tiktok-celebrates-reaching-1-billion-monthly-users/
# Spotify, Discover Weekly turns 10 (June 2025; launched 2015; first personalised playlist; 100 billion+ streams):
#   https://newsroom.spotify.com/2025-06-30/discover-weekly-turns-10-celebrating-100-billion-tracks-streamed-and-a-decade-of-personalized-discovery/
# Spotify, Oskar Stål, 13 October 2021 (the fifth artist; half a trillion events a day; "a mix of what you like and what you might like"):
#   https://newsroom.spotify.com/2021-10-13/adding-that-extra-you-to-your-discovery-oskar-stal-spotify-vice-president-of-personalization-explains-how-it-works/
# Spotify, Understanding recommendations (taste profile; exclude from taste profile; not interested): https://www.spotify.com/us/safetyandprivacy/understanding-recommendations
# McInerney et al. (2018). Explore, exploit, and explain: personalizing explainable recommendations with bandits. RecSys 2018:
#   https://research.atspotify.com/publications/explore-exploit-explain-personalizing-explainable-recommendations-with-bandits · https://dl.acm.org/doi/pdf/10.1145/3240323.3240354
# Goldberg, Nichols, Oki & Terry (1992). Using collaborative filtering to weave an information tapestry. CACM 35(12): https://dl.acm.org/doi/10.1145/138859.138867
# Resnick et al. (1994). GroupLens: an open architecture for collaborative filtering of netnews. CSCW 1994: https://dblp.org/rec/conf/cscw/ResnickISBR94.html
# Linden, Smith & York (2003). Amazon.com recommendations: item-to-item collaborative filtering. IEEE Internet Computing 7(1): https://dl.acm.org/doi/10.1109/MIC.2003.1167344
# Collaborative filtering (memory-based vs model-based; the cold start): https://en.wikipedia.org/wiki/Collaborative_filtering
# Mikolov et al. (2013). Efficient estimation of word representations in vector space (word2vec): https://arxiv.org/abs/1301.3781
# Facebook, 31 March 2019, "Why am I seeing this post?" (Ramya Sethuraman; the ad version since 2014): https://about.fb.com/news/2019/03/why-am-i-seeing-this/
#   and https://www.cnbc.com/2019/04/01/facebook-new-tool-explains-why-am-i-seeing-this-post-on-news-feed.html
# EU Digital Services Act, Articles 27 and 38; obligations for VLOPs from 25 August 2023:
#   https://www.pinsentmasons.com/out-law/analysis/how-the-digital-services-act-changes-things-for-platforms · https://dsa-observatory.eu/2025/05/19/making-recommender-systems-work-for-people/
#   the date: the Commission's enforcement page (designation of 17 VLOPs and 2 VLOSEs on 25 April 2023; enforcement "under the DSA since 25 August 2023"):
#   https://digital-strategy.ec.europa.eu/en/policies/dsa-enforcement
# Strathern (1997). "Improving ratings": audit in the British University system. European Review 5(3): 305–321 (Goodhart's law): https://en.wikipedia.org/wiki/Goodhart's_law
# Simon (1971). Designing organizations for an information-rich world ("a wealth of information creates a poverty of attention"): https://conversableeconomist.com/2015/08/17/economics-of-information-overload-thoughts-from-herb-simon/
# Sunstein, Republic.com (2001), echo chambers and the Daily Me: https://hls.harvard.edu/bibliography/republic-com · https://lareviewofbooks.org/article/pointing-at-the-wrong-villain-cass-sunstein-and-echo-chambers/
# Negroponte, Being Digital (1995): the "Daily Me", the phrase Sunstein read darkly: https://en.wikipedia.org/wiki/The_Daily_Me
# Zuiderveen Borgesius, Trilling, Möller, Bodó, de Vreese & Helberger (2016). Should we worry about filter bubbles? Internet Policy Review 5(1)
#   ("at present there is little empirical evidence that warrants any worries about filter bubbles"): https://policyreview.info/articles/analysis/should-we-worry-about-filter-bubbles
# Bakshy, Messing & Adamic (2015). Exposure to ideologically diverse news and opinion on Facebook. Science 348: 1130–1132: https://pubmed.ncbi.nlm.nih.gov/25953820/
# Netflix Top 10 rows, 24 February 2020: https://about.netflix.com/en/news/see-whats-popular-on-netflix · https://variety.com/2020/digital/news/netflix-top-10-daily-rankings-popular-titles-1203513514/
# Ihde (1990), Technology and the Lifeworld — the four relations: https://books.google.com/books/about/Technology_and_the_Lifeworld.html?id=qGx-_VpaJKUC
#   the schemas as week 5 writes them, after Verbeek (2015), Beyond Interaction, Interactions 22(3): https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf
# The Belamy video (Obvious, "GENERATION OF EDMOND DE BELAMY"): https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=Pu2GZ3du7PI&format=json
# Edmond de Belamy: the GAN "was trained on a set of 15,000 portraits from the online art encyclopedia WikiArt, spanning the 14th to the 19th centuries";
#   Christie's, 25 October 2018: https://en.wikipedia.org/wiki/Edmond_de_Belamy
