"""
SD2112 · Artificial Intelligence in Design · Week 05 — the slide spec.

    python deck/week05.py            # builds _site/week05/ (html deck + pdf), export/week05*.pptx, export/preview/
    python deck/week05.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Image machines and mediation: noise → picture (diffusion), words → pictures (CLIP), the latent
(autoencoders, the whole machine as ComfyUI's diagram), pushing a model off its prototype (references,
ControlNet, LoRA), then Ihde's four human–technology relations, Verbeek's three more and their AI
versions; the layout workshop and the activity "The silent decisions". Four live p5.js sketches (noise
and a toy denoiser, a CLIP-like shared space, a latent space of chairs, a ControlNet-like fill) run in
the html deck; the pptx and the PDF show their snapshots.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week05 as F                              # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, timeline,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, sketch_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(5)
CHAIRS = [f'ai-chair-{i}.jpg' for i in range(1, 5)]   # week 1: one prompt, four seeds

# ───────────────────────── the live sketches (p5.js) ─────────────────────────
# (a) diffusion in one picture: the mouse destroys the image with noise; a click runs a toy denoiser
SHAPE_JS = ',\n  '.join(f"'{row}'" for row in F.W05_SHAPE)
NOISE_CODE = f"""// diffusion in one picture: destroy an image with noise, then undo it one step at a time
const W = 1400, H = 500, N = 24;
const SHAPE = [
  {SHAPE_JS}
];
let x0 = [], eps = [], k = 8, run = 0;   // the image, the noise, denoising steps done, when the click was

function gauss() {{                 // one gaussian number (Box-Muller)
  let u = random(1e-6, 1), v = random();
  return sqrt(-2 * log(u)) * cos(TWO_PI * v);
}}

function setup() {{
  createCanvas(W, H); randomSeed(5); textFont('sans-serif');
  for (let r = 0; r < N; r++) {{
    x0[r] = []; eps[r] = [];
    for (let c = 0; c < N; c++) {{
      x0[r][c] = SHAPE[r][c] == '#' ? -0.85 : 0.9;   // ink is -1, paper is +1
      eps[r][c] = gauss();                           // one noise number per pixel, fixed
    }}
  }}
}}

function noised(t) {{               // forward: x_t = sqrt(1 - t) * x0 + sqrt(t) * eps
  let a = sqrt(1 - t), b = sqrt(t);
  return x0.map((row, r) => row.map((v, c) => a * v + b * eps[r][c]));
}}

function denoise(g, steps) {{       // a toy denoiser: average the neighbours, lean on what it learned
  for (let s = 0; s < steps; s++) {{
    let out = [];
    for (let r = 0; r < N; r++) {{
      out[r] = [];
      for (let c = 0; c < N; c++) {{
        let sum = 0, n = 0;
        for (let dr = -1; dr <= 1; dr++) for (let dc = -1; dc <= 1; dc++) {{
          let rr = r + dr, cc = c + dc;
          if (rr >= 0 && rr < N && cc >= 0 && cc < N) {{ sum += g[rr][cc]; n++; }}
        }}
        let avg = sum / n;
        out[r][c] = avg + 0.35 * (x0[r][c] - avg);   // what it learned: this one chair
      }}
    }}
    g = out;
  }}
  return g;
}}

function grid(g, x, y, size) {{     // draw a 24 x 24 grid of greys
  let cell = size / N; noStroke();
  for (let r = 0; r < N; r++) for (let c = 0; c < N; c++) {{
    fill(constrain(map(g[r][c], -1, 1, 10, 245), 10, 245));
    rect(x + c * cell, y + r * cell, cell + 0.5, cell + 0.5);
  }}
  noFill(); stroke(225); strokeWeight(1); rect(x, y, size, size);
}}

function draw() {{
  background(255);
  let t = constrain(mouseX / W, 0, 1), xt = noised(t);
  if (run > 0) k = min(8, floor((frameCount - run) / 12));   // the click: one step every 12 frames
  let size = 320, y = 70, x1 = 70, x2 = 540, x3 = 1010;
  grid(x0, x1, y, size); grid(xt, x2, y, size); grid(denoise(xt, k), x3, y, size);
  noStroke(); fill(0); textSize(18); textAlign(CENTER, BASELINE);
  text('x\\u2080 \\u00b7 the image', x1 + size / 2, y + size + 30);
  text('x\\u209c \\u00b7 t = ' + t.toFixed(2) + ' \\u00b7 ' + round((1 - t) * 100) + '% signal', x2 + size / 2, y + size + 30);
  text('denoised \\u00b7 ' + k + ' of 8 steps', x3 + size / 2, y + size + 30);
  fill(120); textSize(15);
  text('+ noise, a rule \\u2192', (x1 + size + x2) / 2, y + size / 2 - 6);
  fill(237, 109, 36); text('\\u2190 the network,', (x2 + size + x3) / 2, y + size / 2 - 16); text('one step at a time', (x2 + size + x3) / 2, y + size / 2 + 6);
  fill(120); textAlign(LEFT); textSize(15);
  text('DIFFUSION \\u00b7 mouse x = how much noise (t) \\u00b7 click = run the denoiser', 40, 36);
  stroke(225); strokeWeight(3); line(70, 460, W - 70, 460);     // the schedule
  noStroke(); fill(237, 109, 36); circle(70 + t * (W - 140), 460, 12);
  fill(120); textAlign(LEFT); text('t = 0 \\u00b7 the image', 70, 490); textAlign(RIGHT); text('t = 1 \\u00b7 pure noise', W - 70, 490);
  textAlign(CENTER); text('a toy: it learned one picture, so it always finds it \\u00b7 a real model learned billions, and finds the middle of them', W / 2, 490);
}}

function mousePressed() {{ run = frameCount; k = 0; }}"""

# (b) a CLIP-like shared space: eight words, eight small pictures, one similarity table by hand
CLIP_CODE = """// one space for words and pictures: hover a word (or a picture) and read the similarity
const W = 800, H = 600;
const NAMES = ['chair', 'cup', 'tree', 'car', 'house', 'cat', 'boat', 'lamp'];
// hand-made vectors: [furniture, vessel, living, vehicle, building, light, animal]
const WORD = [[1, 0, 0, 0, .1, 0, 0], [.1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, .1, 0, 0], [0, .1, 0, 1, 0, .2, 0],
  [.2, .1, 0, 0, 1, .2, 0], [.1, 0, .6, 0, 0, 0, 1], [0, .3, 0, 1, 0, 0, 0], [.5, 0, 0, 0, .2, 1, 0]];
const PIC = [[.9, .1, 0, 0, .2, 0, 0], [.2, .9, 0, 0, 0, 0, 0], [0, 0, .9, 0, .2, 0, .1], [.1, .2, 0, .9, 0, .1, 0],
  [.3, .1, 0, 0, .9, .1, 0], [.1, 0, .5, 0, 0, 0, .9], [0, .4, 0, .8, 0, 0, 0], [.4, 0, 0, 0, .3, .9, 0]];

function cosine(a, b) {            // how alike two lists of numbers point
  let d = 0, na = 0, nb = 0;
  for (let i = 0; i < a.length; i++) { d += a[i] * b[i]; na += a[i] * a[i]; nb += b[i] * b[i]; }
  return d / sqrt(na * nb);
}

function icon(k, x, y, s, col) {   // eight small drawings
  stroke(col); strokeWeight(2); noFill();
  if (k == 0) { line(x - s, y + s, x - s, y); line(x - s, y, x + s * .6, y); line(x + s * .6, y + s, x + s * .6, y - s); }
  if (k == 1) { rect(x - s * .7, y - s * .5, s * 1.2, s); circle(x + s * .8, y, s * .6); }
  if (k == 2) { line(x, y + s, x, y - s * .2); circle(x, y - s * .4, s * 1.2); }
  if (k == 3) { rect(x - s, y - s * .2, 2 * s, s * .6); rect(x - s * .5, y - s * .6, s, s * .4); circle(x - s * .55, y + s * .5, s * .4); circle(x + s * .55, y + s * .5, s * .4); }
  if (k == 4) { rect(x - s * .7, y - s * .1, s * 1.4, s); triangle(x - s * .9, y - s * .1, x, y - s * .9, x + s * .9, y - s * .1); }
  if (k == 5) { circle(x, y - s * .3, s * .9); triangle(x - s * .4, y - s * .6, x - s * .3, y - s, x - s * .05, y - s * .7); triangle(x + s * .4, y - s * .6, x + s * .3, y - s, x + s * .05, y - s * .7); circle(x + s * .1, y + s * .5, s); }
  if (k == 6) { quad(x - s, y + s * .2, x + s, y + s * .2, x + s * .6, y + s * .7, x - s * .6, y + s * .7); line(x, y + s * .2, x, y - s); triangle(x, y - s, x + s * .8, y + s * .1, x, y + s * .1); }
  if (k == 7) { line(x, y + s, x, y - s * .2); line(x - s * .6, y + s, x + s * .6, y + s); quad(x - s * .4, y - s * .2, x + s * .4, y - s * .2, x + s * .7, y - s, x - s * .7, y - s); }
}

function setup() { createCanvas(W, H); textFont('sans-serif'); }

function draw() {
  background(255);
  let row = constrain(floor((mouseY - 60) / 62), 0, 7);      // the hovered row
  let side = mouseX < W / 2 ? 0 : 1;                        // 0: a word, 1: a picture
  let q = side == 0 ? WORD[row] : PIC[row], others = side == 0 ? PIC : WORD;
  noStroke(); fill(120); textSize(14); textAlign(LEFT, BASELINE);
  text('ONE SPACE \\u00b7 hover a word or a picture \\u00b7 the bars are how close they are', 30, 36);
  for (let i = 0; i < 8; i++) {
    let y = 90 + i * 62, sim = cosine(q, others[i]);
    noStroke(); fill(side == 0 && i == row ? color(237, 109, 36) : 0); textSize(22); textAlign(LEFT, CENTER);
    text('"' + NAMES[i] + '"', 60, y);
    icon(i, 720, y, 16, side == 1 && i == row ? color(237, 109, 36) : color(0));
    noStroke(); fill(sim > 0.8 ? color(237, 109, 36) : color(100, 194, 195));
    if (side == 0) rect(230, y - 12, sim * 340, 24); else rect(610 - sim * 340, y - 12, sim * 340, 24);
    fill(120); textSize(14); textAlign(side == 0 ? LEFT : RIGHT, CENTER);
    text(sim.toFixed(2), side == 0 ? 236 + sim * 340 : 604 - sim * 340, y);
  }
  noStroke(); fill(120); textSize(14); textAlign(LEFT, BASELINE);
  text('cosine similarity of hand-made 7-number vectors \\u00b7 CLIP\\'s are hundreds long, learned from 400 million pairs', 30, H - 22);
}"""

# (c) a latent space of chairs: two numbers in, a whole chair out — week 1's rule with learned parameters
LATENT_CODE = """// a latent space of chairs: two numbers in, a whole chair out. the mouse is the point.
const W = 1400, H = 500;
let pinned = null;                 // a click pins the point; moving the mouse frees it

function decode(z1, z2) {          // the 'decoder': two numbers -> six chair parameters, with a few bends
  let s = x => 1 / (1 + exp(-x));  // an S-curve: the nonlinearity a network is made of
  return {
    seat: 0.3 + 0.32 * s(4 * (z2 - 0.5)),
    back: 0.22 + 0.5 * (1 - z2) * (0.6 + 0.4 * sin(3 * z1)),
    angle: -4 + 34 * z1 * z1,
    width: 0.42 + 0.36 * s(5 * (0.5 - abs(z1 - z2))),
    legs: z1 + z2 < 0.55 ? 4 : (z1 > 0.75 && z2 < 0.4 ? 2 : 3),
    splay: 0.14 * z1 * (1 - z2)
  };
}

function chair(ox, oy, size, p) {  // week 1's rule, unchanged: side elevation from six numbers
  let sh = p.seat * size, sw = p.width * size, th = 0.05 * size;
  let x0 = ox + (size - sw) / 2, ys = oy + size - sh;
  stroke(0); strokeWeight(max(1.5, size / 60)); fill(0); rect(x0, ys, sw, th);
  let xs = p.legs == 2 ? [x0 + th / 2, x0 + sw - th / 2] : Array.from({ length: p.legs }, (_, i) => x0 + th / 2 + i * (sw - th) / (p.legs - 1));
  for (let lx of xs) { let sp = p.splay * size * (lx < x0 + sw / 2 ? -1 : 1); line(lx, ys + th, lx + sp, oy + size); }
  let bh = p.back * size, a = radians(p.angle), bx = x0 + sw - th / 2;
  let tx = bx + sin(a) * bh, ty = ys - cos(a) * bh;
  line(bx, ys, tx, ty); line(tx - 0.22 * sw * cos(a), ty - 0.22 * sw * sin(a), tx, ty);
}

function setup() { createCanvas(W, H); textFont('sans-serif'); }

function draw() {
  background(255);
  let z1 = constrain(mouseX / W, 0, 1), z2 = constrain(mouseY / H, 0, 1);
  if (pinned) [z1, z2] = pinned;
  let mx = 880, my = 60, ms = 380;                // the map of the space, on the right
  noFill(); stroke(225); strokeWeight(1); rect(mx, my, ms, ms);
  for (let i = 0; i < 5; i++) for (let j = 0; j < 5; j++)   // every chair in between: a 5 x 5 walk
    chair(mx + 6 + i * (ms - 12) / 5, my + 6 + j * (ms - 12) / 5, (ms - 12) / 5 - 10, decode(i / 4, j / 4));
  noStroke(); fill(237, 109, 36); circle(mx + z1 * ms, my + z2 * ms, 14);
  let p = decode(z1, z2);
  chair(100, 60, 380, p);                         // the chair at the point, large
  noStroke(); fill(0); textSize(22); textAlign(LEFT, BASELINE);
  text('z = (' + z1.toFixed(2) + ', ' + z2.toFixed(2) + ')', 560, 200);
  fill(120); textSize(15);
  text('seat ' + p.seat.toFixed(2) + ' \\u00b7 back ' + p.back.toFixed(2) + ' \\u00b7 ' + round(p.angle) + '\\u00b0', 560, 232);
  text('width ' + p.width.toFixed(2) + ' \\u00b7 ' + p.legs + ' legs \\u00b7 splay ' + p.splay.toFixed(2), 560, 254);
  text('two numbers in,', 560, 300); text('six parameters out,', 560, 322); text('one chair.', 560, 344);
  textSize(14); text('LATENT SPACE \\u00b7 move the mouse: two numbers, every chair in between \\u00b7 click: pin', 40, 36);
  text('z\\u2081 \\u2192', mx + ms - 30, my + ms + 20); text('z\\u2082 \\u2193', mx + ms + 8, my + 16);
  text('a parametric design (week 1) whose parameters were learned. nobody writes decode(): here we did, to show its shape.', 40, H - 20);
}

function mousePressed() { pinned = pinned ? null : [constrain(mouseX / W, 0, 1), constrain(mouseY / H, 0, 1)]; }
function mouseMoved() { pinned = null; }"""

# (d) ControlNet as a rule laid over a generator: your scribble decides the shape, a texture fills in
CONTROL_CODE = """// ControlNet as a rule laid over a generator: your line decides the shape, the texture obeys it
const W = 1400, H = 500, HALF = 700;
let strokes = [], cur = null, pts = [], dirty = true, pg;

function hash(x, y) {              // a deterministic 'random' number for a place: the same every frame
  let v = sin(x * 12.9898 + y * 78.233) * 43758.5453;
  return v - floor(v);
}

function setup() {
  createCanvas(W, H); textFont('sans-serif'); pg = createGraphics(HALF, H);
  // a seeded scribble to start with: a chair in profile, in two strokes
  for (let s of [[[430, 96], [426, 180], [420, 266], [196, 272], [204, 428]], [[416, 270], [426, 428]]]) {
    let st = [];
    for (let i = 0; i < s.length - 1; i++) {
      let [ax, ay] = s[i], [bx, by] = s[i + 1], n = ceil(dist(ax, ay, bx, by) / 6);
      for (let k = 0; k < n; k++) { let f = k / n; st.push([lerp(ax, bx, f) + 2 * hash(k, i) - 1, lerp(ay, by, f) + 2 * hash(i, k) - 1]); }
    }
    strokes.push(st);
  }
}

function render() {                // the 'generator': hatching that turns to follow the nearest line
  pts = [];
  for (let s of strokes) for (let i = 1; i < s.length; i++)
    pts.push([s[i][0], s[i][1], s[i][0] - s[i - 1][0], s[i][1] - s[i - 1][1]]);   // a point and its direction
  pg.background(255); pg.strokeWeight(1.5);
  for (let y = 60; y < H - 34; y += 16) for (let x = 12; x < HALF; x += 16) {
    let best = 1e9, dir = 0;
    for (let p of pts) { let d = (p[0] - x) ** 2 + (p[1] - y) ** 2; if (d < best) { best = d; dir = atan2(p[3], p[2]); } }
    let d = sqrt(best), near = constrain(1 - d / 140, 0, 1);
    let a = (near > 0 ? dir + HALF_PI : 0.4) + 0.3 * (hash(x, y) - 0.5);   // perpendicular to the line; far away: a house style
    let len = 4 + 20 * near, jx = 3 * (hash(y, x) - 0.5), jy = 3 * (hash(x + 1, y) - 0.5);
    pg.stroke(lerp(200, 20, near));
    pg.line(x + jx - cos(a) * len, y + jy - sin(a) * len, x + jx + cos(a) * len, y + jy + sin(a) * len);
  }
  dirty = false;
}

function draw() {
  if (dirty) render();
  background(255);
  image(pg, HALF, 0);
  stroke(225); strokeWeight(2); line(HALF, 0, HALF, H);
  stroke(0); strokeWeight(3); noFill();
  for (let s of strokes) { beginShape(); for (let p of s) vertex(p[0], p[1]); endShape(); }
  noStroke(); fill(120); textSize(14); textAlign(LEFT, BASELINE);
  text('CONTROL \\u00b7 your scribble, a rule \\u00b7 drag to draw \\u00b7 C clears', 30, 36);
  text('GENERATED \\u00b7 a texture that obeys the line: perpendicular near it, its own way far from it', HALF + 30, 36);
  text('ControlNet, 2023: a sketch, a pose or an edge map is read by a trained copy of the denoiser and steers every step', 30, H - 20);
}

function mousePressed() { if (mouseX < HALF) { cur = []; strokes.push(cur); } }
function mouseDragged() { if (cur && mouseX < HALF) { cur.push([mouseX, mouseY]); dirty = true; } }
function mouseReleased() { cur = null; }
function keyPressed() { if (key == 'c' || key == 'C') { strokes = []; dirty = true; return false; } }"""

# ───────────────────────── the panels on the slides ─────────────────────────
BRIEF = [
    'THE BRIEF · AN A2 POSTER', '(or one screen of a landing page)', ' ',
    'TITLE: SD2112 Poster Fair', 'SUB: every project of the class, one afternoon', 'WHEN / WHERE: week 13 · PolyU School of Design', '(day, time and room: to confirm)', ' ',
    'MUST SHOW: title, sub, when / where,', 'a square placeholder for a QR code', 'MUST NOT: stock photos, a robot, more than', 'two typefaces', ' ',
    'TONE: a design school, not a tech conference', 'SIZE: A2 portrait, readable from 3 m',
]

REFERENCES = [
    'ROUND 2 · TWO REFERENCES', ' ',
    '1 · A GRID YOU DREW', 'Pen and paper: the columns, the title band,', 'where the QR goes. Photograph it.', ' ',
    '2 · A COLOUR SET', 'Three colours, as swatches or hex codes.', 'e.g. #000B1C · #ED6D24 · #F4F4F2', ' ',
    'If the model takes an image input, upload both.', 'If not, describe them in words, exactly:', '"three columns; title in the top band;', 'QR bottom right; only these three colours".',
]

ITERATE = [
    'ROUND 4 · THREE ITERATIONS, ONE SPEC', ' ',
    'v1 → v2: change ONE thing. Write it down.', 'v2 → v3: change ONE thing. Write it down.', 'v3 → v4: change ONE thing. Write it down.', ' ',
    'THE SPEC (the caption of your upload):', 'what changed at each step, and', 'THE SILENT DECISION: one thing the model', 'decided that nobody asked for —', 'and whether you kept it.', ' ',
    'One prompt per change. New chat if it drifts.',
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 05 · LECTURE + WORKSHOP',
               'Image machines and mediation.',
               'Week 5 — how a picture comes out of noise, and what a tool does to you.',
               notes='Join code on screen from 30 minutes before. Laptops or phones out from the start: the second half is on genai.polyu.edu.hk with the image models. Today has two halves that look unrelated and are not: how an image model works, and what any tool does to the person using it. The activity puts them together on a poster.'))

S.append(agenda('SD2112 · WEEK 05', [
    'Last week, in your words', 'Noise → picture: diffusion', 'Words → pictures: CLIP', 'The latent: a space of pictures',
    'Off the prototype: three handles', 'Mediation: Ihde and Verbeek', 'The layout workshop', 'Activity: the silent decisions',
], notes='Eight stops. Four chapters of mechanism before the break — noise, words, the latent, and the handles that push a model off its middle — then Verbeek after the break, then the workshop and the activity: a layout generated from a brief, and the question that runs through the whole afternoon: what did the model decide that you did not?'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the videos · the awards · the map',
                 notes='Fifteen minutes of recap from what you gave us: the homework videos, week 4 in three lines, the Challenge 3 vote, and where we are.'))

S.append(question('short_answer', 'Welch Labs, AssemblyAI: one thing you understood, one you did not.',
                  hint='Two short lines. "Understood: … Not yet: …". No wrong answers; the second line writes the first half of today.',
                  eyebrow_text='01 · HOMEWORK · SHORT ANSWER',
                  notes='ClassPoint short answer, two minutes. Read six aloud, sorted. What people understood is usually "it removes noise"; what they did not is usually why removing noise makes a picture, or how the words get in. Say which chapter answers each: chapter two is the noise, chapter three is the words, chapter four is where it all happens. Keep the screenshot: the mid-term draws on these videos.'))

S.append(cards('01 · WEEK 4 · IN THREE LINES', 'The machine that writes by dice and a table.', [
    ('TOKENS → POINTS', 'A word is a point. Nearby means used alike.', 'Embeddings: a space with thousands of unnamed axes, learned from company. Today the same space gets pictures in it.'),
    ('THE NEXT TOKEN', 'A table, a die, a temperature.', 'The model writes one token at a time from odds it learned. Today the same move, on pixels: one step of noise at a time.'),
    ('A PROMPT IS A BRIEF', 'Fluent, typical, cannot say why.', 'The less you say, the more it fills in from the middle. Today the middle is a picture, and the brief is a layout.'),
], notes='Three lines from last week, because today stands on them. Embeddings become CLIP. The die on a table becomes the denoiser. And the brief becomes the layout brief in the activity: same discipline, now with a picture coming back instead of a draft.'))

S.append(video('01 · WELCH LABS · 25 JULY 2025 · THE HOMEWORK', 'Diffusion, CLIP, and the maths of turning text into images.', 'iv-5mZ_9CPY',
               ['You watched it: a guest video by Stephen Welch on the 3Blue1Brown channel. The two claims to hold on to:',
                '- A model learns to remove a little noise from an image; run that backwards from pure noise and a picture appears.',
                '- The words reach the picture through a shared space of words and images: CLIP.',
                'Chapters two to four are these two claims, slowly, with sketches you can touch.'],
               thumb='yt/iv-5mZ_9CPY.jpg', body_size=28,
               notes='If the short answers said "why does removing noise make a picture" was the thing not understood, play the noise minute now and go straight to the sketch on slide 12. Otherwise cut this slide. AssemblyAI\'s video comes back in chapter two as the four-level version.'))

S.append(cards('01 · CHALLENGE 3 · FOUR ENTRIES · THE EDIT', 'A brief, automated — then edited by you.', [
    ('ENTRY A', 'What the model decided', '"It invented a launch date and a tagline. I cut both and added the constraint it had ignored: two colours."'),
    ('ENTRY B', 'What the model decided', '"The system prompt made every brief start with the goal. Mine start with the audience now; I changed the prompt, not the draft."'),
    ('ENTRY C', 'What the model decided', '"It wrote for a general reader. The audience heading fixed it: tutors who have seen 27 other posters."'),
    ('ENTRY D', 'What the model decided', '"It praised the idea in the first line. I added: do not praise. The second draft was a critic."'),
], text_size=22, notes='Replace these four with the real ones: the four best entries from Blackboard, anonymised, the prompt and the edit on screen from the Blackboard page and the one-line "what the model decided" on the card. Read each card before showing the edit; ask the room to guess what was cut. The gap between the guess and the edit is the subject of the whole day.'))

S.append(question('multiple_choice', 'Challenge 3: which entry gets the star?', [
    'Entry A', 'Entry B', 'Entry C', 'Entry D',
], eyebrow_text='01 · CHALLENGE 3 · AWARDS · MULTIPLE CHOICE',
    notes='ClassPoint vote, one minute. No correct answer: the room decides, the winner gets a participation star and thirty seconds to say what the edit undid. Note the split for the awards list.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(1, 1),
                 notes='Week 5 of module 2: language last week, images today, sound next week. Challenge 4 is briefed at the end of today; the reflection is due in week 7, and next week the TAs check drafts. Two more weeks of tool weeks, then the quiz and the pitches.'))

# ───────────────────────── 02 · noise → picture ─────────────────────────
S.append(section('02', 'Noise → picture', 'destroy · learn one step · run it backwards', bg=INK,
                 notes='Chapter two: the mechanism of every image model you will use this year, in one picture and one sketch. Six slides.'))

S.append(figure_slide('02 · THE FORWARD PROCESS', 'An image is destroyed by noise, step by step.', F.w05_forward(),
                      body=['Take any picture. Add a little gaussian noise. Add a little more. After a thousand steps nothing of the picture is left: every pixel is a random number. This half needs no learning at all — it is a rule, and it can be run on every photo on the internet.'],
                      caption='Sohl-Dickstein and colleagues, 2015: destroy structure slowly, then learn to reverse it. Ho, Jain and Abbeel, "Denoising Diffusion Probabilistic Models", 2020: T = 1,000 steps, the noise growing on a fixed linear schedule.',
                      notes='Read the row left to right: the chair, then less chair, then none. Say the two facts on the figure. The forward half is machine A: a rule, a schedule, no learning. And "pure noise" is not nothing: it is a specific grid of random numbers, and that grid is where every generated image begins. The orange arrows are the whole trick, and they are the next three slides.'))

S.append(sketch_slide('02 · LIVE · NOISE, AND A TOY DENOISER', 'Move the mouse: destroy it. Click: undo it.',
                      live('w05-noise', NOISE_CODE, 1400, 500, hint='mouse x = how much noise · click = run the denoiser'),
                      caption='Left: the image. Middle: the same image with the mouse\'s share of noise mixed in. Right: eight steps of a toy denoiser that averages neighbours and leans on the one picture it learned. Pure noise still comes back as the chair: that is the point.',
                      notes='Move to the right until the middle panel is pure noise, then click: the right panel finds the chair anyway, because our toy denoiser only ever learned one picture. Say the honest version: a real model learned billions, so from pure noise it finds the middle of them — the week-1 chair, the week-1 cup. Then move to t = 0.3 and click: it finds the chair faster and cleaner; that is image-to-image, chapter five. Everything in the right panel is subtraction. Nothing is drawn.'))

S.append(figure_slide('02 · ONE TRAINING STEP', 'A network learns to undo one step.', F.w05_train_step(),
                      body=['Pick a photo, pick a step t, add that much noise, and ask the network: which part of this is the noise? Compare its guess with the noise you added; nudge every weight a little; again. The answer key is free, because you made the noise yourself.'],
                      caption='The network is a UNet (Ronneberger, Fischer and Brox, 2015 — built for medical image segmentation): a funnel down and a funnel up, with shortcuts across. Stable Diffusion v1\'s has 860 million weights.',
                      notes='This is the perceptron loop from week 3, on pixels: guess, compare, nudge, a million times. The design point is the answer key: nobody labels anything, the noise is the label, so the whole internet of images is training data. Then say what the network is not learning: it does not learn a chair. It learns "what noise looks like on top of a chair", which is a subtler thing, and it is why the middle comes back so strongly.'))

S.append(cards('02 · THE THREE MOVES', 'Destroy. Learn one step. Run it backwards.', [
    ('FORWARD', 'A rule.', 'Add noise to every image, a thousand times. No learning; a fixed schedule. Machine A prepares the examples.'),
    ('ONE STEP', 'Learned.', 'A network learns to undo one step of noise on any image. Machine B, with the noise as the label.'),
    ('SAMPLING', 'The backward walk.', 'Start from a grid of random numbers. Undo one step, fifty or a thousand times. A picture appears that was never anywhere — and is the middle of everything it saw.'),
], notes='Three moves; say them as a sentence, twice. Then the design consequence: the seed. Same seed, same noise grid, same walk, same picture — randomSeed() from week 2. Change the seed and you get a cousin. That is why the week-1 chairs were four cousins from one prompt.'))

S.append(video('02 · ASSEMBLYAI · THE HOMEWORK', 'Diffusion, explained at four levels of difficulty.', 'yTAMrHVG1ew',
               ['You watched it. Level one is the last three slides. Levels three and four are the mathematics of the noise schedule and the loss; you do not need them to design with the tool.',
                '- What to keep: the forward process is fixed; the backward process is learned; sampling is the backward process run from noise.',
                '- The mid-term draws on the first two levels.'],
               thumb='yt/yTAMrHVG1ew.jpg', body_size=28,
               notes='Cut this slide if the room is fine; keep it if the short answers were confused about forward versus backward. Play level one, two minutes, if you keep it.'))

S.append(question('multiple_choice', 'What does the network learn to predict?', [
    'The noise that was added to the image at that step', 'The finished image, in one go', 'The caption of the image', 'The seed',
], eyebrow_text='02 · QUICK CHECK · MULTIPLE CHOICE',
    notes='A. The network never outputs a finished picture; it outputs a guess about the noise, and the picture is what is left when you subtract the guess, step after step. B is what most people assume and is the reason "it removes noise" sounds like magic. C is CLIP\'s job, next chapter. D is your job.'))

# ───────────────────────── 03 · words → pictures ─────────────────────────
S.append(section('03', 'Words → pictures', 'CLIP · one space · the prompt steers the walk',
                 notes='Chapter three: how "a chair" gets into a machine that only knows about noise. Five slides.'))

S.append(figure_slide('03 · CLIP · 2021', 'Words and pictures in the same space.', F.w05_clip_space(),
                      body=['Two encoders — one for text, one for images — trained together on 400 million captioned pictures from the internet. The task: for a batch of pairs, pull each caption towards its own picture and away from all the others. Nobody labels a chair. The caption is the label.'],
                      caption='Radford and colleagues, "Learning Transferable Visual Models From Natural Language Supervision", 2021. Week 4\'s embeddings, with pictures in the same space: "a chair" and a photo of a chair are neighbours.',
                      notes='Point at the diagonal: that is the whole training signal. Pull the real pairs together, push the wrong pairs apart, on the internet\'s captions. What you get is a space where the word and the picture land together — and where "a wooden chair" lands nearer to a wooden chair than to a plastic one. Whose captions? The internet\'s: alt text, product pages, Flickr. The middle of that space is the middle we keep meeting. Week 9.'))

S.append(content('03 · LIVE · ONE SPACE', 'A word and its picture are neighbours.',
                 ['Eight words, eight small pictures, one table of similarities. Hover a word: the bars are how close each picture is to it. Hover a picture: the same, the other way round.',
                  '- "chair" is closest to the chair, and not far from the lamp: our hand-made vectors share a "furniture" number.',
                  '- Real CLIP vectors are hundreds of numbers long, and nobody named them. The closeness was learned.',
                  'A prompt is a point in this space. The denoiser is steered towards pictures whose point is near it.'],
                 sketch=live('w05-clip', CLIP_CODE, 800, 600, hint='hover a word on the left, or a picture on the right'),
                 body_size=27,
                 caption='Similarity is the cosine between two lists of seven numbers we wrote by hand. CLIP\'s were learned from 400 million pairs.',
                 notes='Hover "boat": the boat first, then the car, then the cup — a vehicle and a vessel. Hover the cat picture: cat, then tree, because we gave both a "living" number. Our numbers are made up; the mechanism is the real one, and so is the lesson: similarity is geometry, and geometry was learned from company. Ask what "a chair, Hong Kong, 1970s" would be near, and whose photos decided that.'))

S.append(cards('03 · HOW THE WORDS REACH THE PICTURE', 'Three ways the prompt steers the walk.', [
    ('THE EMBEDDING', 'The prompt becomes points.', 'The text encoder turns your words into a list of points — one per token, up to 77 in Stable Diffusion v1. Every one of them is a handle the denoiser can hold.'),
    ('CROSS-ATTENTION', 'Every step looks at the words.', 'At each denoising step the network attends from the image to the prompt\'s points: week 4\'s attention, from pixels to tokens. "Wooden" pulls the texture; "chair" pulls the shape.'),
    ('GUIDANCE', 'How hard to push.', 'Classifier-free guidance (Ho and Salimans, 2022): denoise once with the prompt and once without, and exaggerate the difference. Stable Diffusion\'s default is 7.5. Low: loose and varied. High: literal, then burnt.'),
], text_size=22, notes='Three mechanisms, three knobs you can find in ComfyUI. The embedding is why word order and word choice matter. Cross-attention is why a prompt with two objects sometimes swaps their colours — the attention got the wrong token. Guidance is the one to try tonight: the same seed at 3, 7.5 and 20 is a lesson in the difference between a suggestion and an order.'))

S.append(video('03 · COMPUTERPHILE · THE HOMEWORK', 'How AI "understands" images: CLIP.', 'KcSXcpluDe4',
               ['You watched it. What to keep: an image and a caption are encoded separately, and training makes the matching pairs land together.',
                '- The same trick lets you search a photo library with a sentence, and lets a prompt steer a denoiser.',
                '- On the playlist; the mid-term draws on it.'],
               thumb='yt/KcSXcpluDe4.jpg', body_size=28,
               notes='Cut if behind. If you keep it, play the minute where the two encoders are drawn side by side, then go back one slide and hover again.'))

# ───────────────────────── 04 · the latent ─────────────────────────
S.append(section('04', 'The latent', 'an autoencoder · a space of pictures · the whole machine', bg=INK,
                 notes='Chapter four: where the diffusion actually runs, why that makes it fast, and the whole machine on one slide. Seven slides.'))

S.append(figure_slide('04 · AUTOENCODERS', 'Squeeze the picture, then rebuild it.', F.w05_autoencoder(),
                      body=['An autoencoder is two networks and a bottleneck: the encoder squeezes an image into a few numbers, the decoder rebuilds it. Trained on one task — rebuild the input — it has to keep what matters and drop what does not. The numbers in the middle are the latent.'],
                      caption='Stable Diffusion v1: a 512 × 512 × 3 image becomes a 64 × 64 × 4 latent — 48 times fewer numbers. Diffusion runs on the latent; the decoder turns the result into pixels once, at the end. Rombach and colleagues, CVPR 2022.',
                      notes='The IBM video on the playlist is this slide. Two things to land. One: no labels again — the picture is its own answer key. Two: the latent is not a small picture; it is a list of numbers nobody named, and the violet block is only a drawing. The reason this matters for you: the noise, the denoising, the ControlNet, the LoRA all happen on the 16,384 numbers, not the 786,432 pixels, which is why a laptop can do it.'))

S.append(sketch_slide('04 · LIVE · A LATENT SPACE OF CHAIRS', 'Two numbers, every chair in between.',
                      live('w05-latent', LATENT_CODE, 1400, 500, hint='move the mouse: the point in the space · click to pin it'),
                      caption='Week 1\'s chair rule, six parameters, driven by two numbers through a few bends. The map on the right is the space: a 5 × 5 walk through it. A real latent has thousands of numbers and nobody wrote decode() — it was learned.',
                      notes='Move slowly along one edge of the map: the seat rises, the back leans, the legs change count at a line you cannot see. That is a latent space: every point is a design, nearby points are similar designs, and the axes have no names. Say the link to week 1 out loud: this is a parametric design whose parameters were learned — machine A with its numbers chosen by machine B. Click to pin a chair and ask the room to guess where in the map it is.'))

S.append(figure_slide('04 · THE WHOLE MACHINE', 'Text → points. Noise → less noise. Latent → pixels.', F.w05_pipeline(),
                      body=['Every box is a node in ComfyUI. Solid boxes are the model: learned, machine B. Orange is what you set: the prompt, the seed, the steps, the guidance — rules, machine A. Dashed are the handles of chapter five: a reference, a sketch, a style.'],
                      caption='Stable Diffusion v1\'s defaults (2022): 50 steps, guidance 7.5, a 64 × 64 × 4 latent, CLIP ViT-L/14. Flux (Black Forest Labs, 2024) and Qwen-Image (Alibaba, 2025), the models on PolyU GenAI, keep the shape and swap the parts.',
                      notes='This is the slide to photograph. Walk it left to right: the prompt becomes points; a seed makes a grid of noise; the UNet takes the noisy latent, the step number and the points and says "this is the noise"; fifty times; then the decoder makes pixels once. Then the dashed boxes: they are the second half of the lecture. When you open ComfyUI, or the advanced tab of any image tool, you are looking at this drawing with sliders on it.'))

S.append(cards('04 · FOUR PARTS, FOUR NAMES', 'What the menus call them.', [
    ('CHECKPOINT', 'The whole model, saved.', 'The UNet, the text encoder and the VAE, trained together and written to one file. Stable Diffusion 1.5, SDXL, Flux: each is a checkpoint with its own middle.'),
    ('TEXT ENCODER', 'CLIP, or bigger.', 'Words to points. Swap it and the same prompt lands somewhere else. Newer models use larger language models here, which is why long prompts started working.'),
    ('UNET · DIT', 'The denoiser.', 'The part that learned. A UNet in 2022; a transformer (a diffusion transformer, DiT) in Flux and Qwen-Image. Same job: "this is the noise".'),
    ('VAE · SAMPLER', 'The bottleneck and the walk.', 'The VAE squeezes and rebuilds. The sampler is the rule for how the fifty steps are taken — a schedule, machine A, and the reason step counts differ between tools.'),
], text_size=22, notes='The vocabulary of the ComfyUI video on the playlist and of every "advanced" panel. The two to remember: a checkpoint has a middle — change the checkpoint and you change the prototype more than any prompt will — and the sampler is a rule, so the same seed with a different sampler is a different picture. Everything else on the menu is one of these four.'))

S.append(content('04 · ON THE PLAYLIST', 'Two short ones: the squeeze, and the funnel.',
                 ['**IBM Technology, What are Autoencoders?** The encoder, the bottleneck, the decoder — and why a network forced through a bottleneck learns what matters.',
                  '- **UNet for Image Segmentation (Johannes Frey).** The denoiser\'s architecture: a funnel down, a funnel up, and shortcuts across so that fine detail survives. Built in 2015 to outline cells in microscope images.',
                  'Neither was written for image generation. Both are inside every image model you will use today.'],
                 images=['yt/qiUEgSCyY5o.jpg', 'yt/-dfSZ_uLfo8.jpg'],
                 caption='On the course playlist, in this week\'s block. The mid-term draws on the autoencoder video.',
                 body_size=27,
                 notes='Two minutes. The point of showing them together: the two networks in the machine were borrowed. The autoencoder is an old idea for compression; the UNet was a medical-imaging tool. Diffusion put them in a loop. Cut if behind; both are homework.'))

S.append(timeline('04 · HOW WE GOT HERE', 'Ten years, from a physics idea to a poster tool.', [
    ('2015', 'Diffusion', 'Sohl-Dickstein and colleagues: destroy structure slowly, learn to reverse it.'),
    ('2020', 'DDPM', 'Ho, Jain and Abbeel: a thousand steps, a UNet, photographs that fool people.'),
    ('2021', 'CLIP · LoRA', 'Words and pictures in one space (Radford et al.). LoRA: a small fine-tune (Hu et al.).'),
    ('2022', 'Stable Diffusion', 'Latent diffusion (Rombach et al.); released 22 August 2022, open weights, on a laptop.'),
    ('2023', 'ControlNet · ComfyUI', 'A rule laid over the model (Zhang, Rao, Agrawala). ComfyUI: the machine as a diagram.'),
    ('2023', 'Generative Fill', 'Adobe puts a diffusion model in Photoshop, 23 May 2023, in beta. Machine B in the toolbar.'),
    ('2024', 'FLUX.1', 'Black Forest Labs, 1 August 2024: a transformer where the UNet was. On PolyU GenAI.'),
    ('2025', 'Qwen-Image', 'Alibaba, 4 August 2025: 20 billion weights, built for text rendering. On PolyU GenAI.'),
], notes='One decade. The first two are the mechanism; 2021 is the words; 2022 is the year it reached everyone — DALL·E 2 and Midjourney the same year, Stable Diffusion with open weights so that everything after it could be built. 2023 is the year of handles, and of the toolbar. The last two are the models in your browser today. The mid-term asks for the order, not the dates.'))

S.append(question('multiple_choice', 'Where does Stable Diffusion\'s denoising run?', [
    'On the pixels of the 512 × 512 image', 'On a 64 × 64 × 4 latent made by an autoencoder', 'Inside the CLIP text encoder', 'In the seed',
], eyebrow_text='04 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. That is the word "latent" in latent diffusion, and the reason it runs on a laptop. A was the 2020 way and needed a data centre. C turns words into points and never sees the picture. D is a number that makes the first grid of noise.'))

# ───────────────────────── 05 · off the prototype ─────────────────────────
S.append(section('05', 'Off the prototype', 'a reference · a rule · a style · the chairs and the cups return', bg=INK,
                 notes='Chapter five: week 1\'s edge chair, with the machinery to do it properly. Nine slides, then the break.'))

S.append(content('05 · WEEK 1 · THE MIDDLE', 'Ask for a chair. Get the middle, four times.',
                 ['The week-1 chairs: one prompt, four seeds. Now you know what the seeds are — four grids of noise — and why the chairs are cousins: the same walk, steered by the same points, from four different starting grids.',
                  '- The prompt is a rule. The seed is a rule. Everything in between is the middle of 400 million captions and a few billion pictures.',
                  '- Your cups in week 1: white, ceramic, a handle. Nobody typed "handle". The examples did.',
                  'Prompting harder is negotiating with the middle. This chapter is about the other handles.'],
                 images=CHAIRS,
                 caption='Prompt: "a chair, studio product photograph, plain white background" — one fast text-to-image model, four seeds, September 2026.',
                 body_size=27,
                 notes='Same four chairs as week 1, now with the vocabulary to read them. Ask the room to name the two rules in the picture: the prompt and the seed. Then the honest limit: a prompt selects a region of the model\'s distribution; it cannot make the distribution contain something it never saw. That was the edge chair. Next slide.'))

S.append(content('05 · WEEK 1 · THE EDGE', 'Ask for the edge. Get the middle, slightly more designed.',
                 ['"An object that is barely still a chair." A chair. The prompt moved the walk a little right of the middle; the denoiser walked it back.',
                  '- A prompt is cheap and weak: it steers every step, and every step also pulls towards the typical.',
                  'Three handles that are not words:',
                  '- **A reference:** start from a noised picture of yours, not pure noise.',
                  '- **A rule:** ControlNet reads a sketch, a pose, an edge map; every step obeys it.',
                  '- **A style:** LoRA, a small fine-tune on twenty of your images. The middle moves.'],
                 image='ai-chair-edge.jpg', fit='cover', body_size=25,
                 caption='Prompt: "an object that is barely still a chair, an unusual seat that stretches the definition of chair, studio product photograph". Same model, one seed.',
                 notes='The most honest slide of week 1 comes back with its answer. Three handles, in increasing cost and increasing reach: a reference is one image and one slider; ControlNet is a drawing and a second model; a LoRA is twenty images and an hour of training. Say the spine: the first two are rules laid over the model — machine A inside machine B — and the third is more examples. Write the rule, or show the examples, again.'))

S.append(figure_slide('05 · FOUR HANDLES', 'How far each handle pushes, and what it costs.', F.w05_push(),
                      body=['The model\'s chairs form a distribution with a middle. A prompt selects a window in it. A reference starts the walk elsewhere and still drifts back. ControlNet fixes the geometry and lets the model fill the surface from its middle. A LoRA moves the middle, because you gave it new examples.'],
                      caption='A drawing, not data. Challenge 2\'s references were the second handle: the reference pulled, the prompt selected. Today\'s activity uses the first two on a layout; ControlNet and LoRA come back in week 11 with their datasets.',
                      notes='Read the four annotations left to right. The distribution is the same curve as the typicality scale in week 1. The design question for each handle: what stays yours? With a prompt, the words. With a reference, the composition. With ControlNet, the geometry. With a LoRA, the examples — and whoever chose them chose the prototype, which is week 11\'s ethics and week 9\'s bias.'))

S.append(sketch_slide('05 · LIVE · A RULE LAID OVER A GENERATOR', 'Your line decides the shape. The texture obeys it.',
                      live('w05-control', CONTROL_CODE, 1400, 500, hint='drag on the left to draw · C clears · the right half obeys'),
                      caption='Left: your scribble, the condition. Right: a generator that knows only one thing — hatch perpendicular to the nearest line, and in its own way far from any line. ControlNet, 2023: the drawing is read by a trained copy of the denoiser and steers every step.',
                      notes='Draw a second chair, or a word. The fill has no idea what a chair is; it obeys the line. That is the whole idea of ControlNet: the geometry comes from a rule you drew, the surface from the model\'s middle. Zhang, Rao and Agrawala, February 2023; they tested edges, depth, segmentation and human pose as conditions, and it trains on as few as fifty thousand pairs. For product designers: a hand sketch becomes a render that keeps your proportions. For communication designers: a grid becomes a layout that keeps your columns — which is round two of the activity, in words if GenAI has no sketch input.'))

S.append(cards('05 · THREE HANDLES', 'A reference, a rule, a style.', [
    ('IMAGE-TO-IMAGE', 'Start from your picture.', 'Encode a reference into the latent, add noise up to a strength you choose, denoise from there. Low strength: your composition, its surface. High: its middle. The Challenge 2 references did this.'),
    ('CONTROLNET', 'Machine A inside machine B.', 'A sketch, a pose, a depth or edge map, read by a trained copy of the denoiser and added to every step. Your geometry survives; the model fills the rest. Zhang, Rao and Agrawala, 2023.'),
    ('LORA', 'Twenty images, one style.', 'Freeze the model; train a small set of extra weights on your images (Hu and colleagues, 2021, written for language models; now the way to teach an image model a style or a product). The middle moves. Week 11 asks whose images.'),
], text_size=22, notes='Three handles, three costs. Image-to-image is one slider and any picture. ControlNet needs a second model and a condition you can draw. A LoRA needs a dataset and training, and is the first place in the course where you choose the examples — the week-11 exercise. The spine: two rules and one set of examples, and a designer decides which handle keeps what they care about.'))

S.append(video('05 · COMFYUI · ON THE PLAYLIST', 'The machine as a diagram: checkpoints, LoRAs, VAEs.', 'bXAl9XAsF44',
               ['ComfyUI, January 2023: every part of the pipeline is a node, every node has its wires showing. The slide-25 drawing, as a tool.',
                '- Watch for the four names: checkpoint, text encoder, the denoiser, the VAE — and where a LoRA and a ControlNet plug in.',
                '- You do not need ComfyUI for the activity. You need to know that the friendly text box on GenAI is this graph with the wires hidden.'],
               thumb='yt/bXAl9XAsF44.jpg', body_size=27,
               notes='Play a minute where a LoRA node is wired into the model if there is time. The design point: a tool that shows its wires is a hermeneutic relation — you read the machine — and a tool that hides them is an embodiment relation; after the break we get the words for that. Cut if behind.'))

S.append(video('05 · GOOGLE RESEARCH · ON THE PLAYLIST', 'Text to video: the same walk, with time as one more axis.', 'dECiAdfn2d4',
               ['A video is a stack of frames. Diffuse the stack — noise in space and in time — and the denoiser learns that the frame after this one must agree with it.',
                '- The words reach the video the same way: a text encoder, attention at every step.',
                '- The hard part is not the picture; it is consistency: the same chair from every side, for five seconds.',
                'On the playlist; the mid-term draws on it.'],
               thumb='yt/dECiAdfn2d4.jpg', body_size=27,
               notes='Keep it to two sentences: same mechanism, one more axis, and the whole difficulty is agreement between frames. Ask the room what a video model\'s middle looks like — slow pans, soft light, nothing changes — because that is what most video looks like. Cut if behind.'))

S.append(statement('Write the rule, or show the examples — now both, inside one machine.', eyebrow_text='05 · WHERE WE ARE', size=104,
                   notes='The sentence to carry across the break. The denoiser learned from examples. The prompt, the seed, the schedule, the ControlNet are rules laid over it. A LoRA is more examples. Every handle you touch this afternoon is one or the other, and the design decision is which one keeps what you care about.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · WHAT A TOOL DOES TO YOU · THEN THE LAYOUT WORKSHOP', size=120, bg=PAPER,
                   notes='1:22. Everyone logged into genai.polyu.edu.hk before leaving the room, with an image model open — Flux or Qwen. The TAs help anyone whose login fails. Pen and paper for round two: the grid is drawn by hand.'))

# ───────────────────────── 06 · mediation ─────────────────────────
S.append(section('06', 'Mediation', 'Ihde · Verbeek · four relations, three more, and their AI versions', bg=VIOLETS[0],
                 notes='Chapter six, after the break: the reading. Verbeek\'s six pages, in nine slides, with an AI example for every relation. This is the vocabulary of the mediation brief in the group project.'))

S.append(quote('"Designing technology is designing human beings: robots, vacuum cleaners, smart watches — any technology creates specific relations between its users and their world, resulting in specific experiences and practices."',
               'Peter-Paul Verbeek, Beyond Interaction: A Short Introduction to Mediation Theory, Interactions 22(3), May–June 2015 — the core reading', size=60,
               notes='Verbeek, written for interaction designers, six pages. The claim in one sentence: a technology is not a thing between a finished person and a finished world; it shapes both. His examples in the paper: the printer default that decides how many double-sided pages a company makes; the ultrasound that turns a pregnancy into a decision. Ours: the default artwork, the autocomplete, the fill. Week 1 had the shorter line — "designing things is designing human existence" — from the same paper.'))

S.append(figure_slide('06 · IHDE · FOUR HUMAN–TECHNOLOGY RELATIONS', 'Through it, off it, facing it, around you.', F.w05_relations(),
                      body=['Don Ihde, Technology and the Lifeworld, 1990: four ways a technology can sit between you and the world. Verbeek writes them as schemas. Under each: Ihde\'s examples, then the AI version — and the risk that comes with designing for that relation.'],
                      caption='Verbeek 2015 gives the schemas and the examples: the phone and the microscope; the MRI scan and the metal detector; the ATM and the robot; the fridge hum and the heating. Glasses and the thermometer are Ihde\'s classic cases.',
                      notes='Take them one at a time, with the room naming an AI tool for each before you show the violet line. Embodiment: you act through it and it withdraws — Generative Fill, autocomplete; the risk is forgetting it decides. Hermeneutic: you read the world off it — a feed, a summary, the poster Netflix chose; the risk is mistaking the representation for the world. Alterity: you face it — a chatbot, Sophia; the risk is mistaking it for a person. Background: it shapes the room — a spam filter, a ranking, a default; the risk is that nobody is accountable. Same model, four relations: the next slides.'))

S.append(cards('06 · VERBEEK · THREE MORE', 'Recent technologies do not fit the four.', [
    ('CYBORG', 'human / technology → world', 'More intimate than embodiment: a brain implant for deep brain stimulation "merges with the human body into a new, hybrid being." AI version: a hearing aid that decides what you hear; a prosthesis that learns your gait.'),
    ('IMMERSION', 'human ⟷ technology / world', 'More than a background: smart environments that "detect if people are present or not, recognize faces, give feedback on behavior." AI version: the feed that learns from your scrolling; a shop that watches where you look.'),
    ('AUGMENTATION', '(human – tech) → world + human → (tech – world)', 'Smart glasses: embodied and read at once, "a bifurcation of the human–world relation." AI version: glasses that caption the street; a heads-up display that names what you see.'),
], text_size=22, notes='Verbeek\'s three additions, quoted from the paper. Cyborg: the technology and the body become one being. Immersion: the environment interacts back — this is the one most AI products are, and the one the brief in week 8 will name. Augmentation: two relations at once, the glasses case. The word "composite" belongs to his earlier work on cyborg intentionality; in this paper the terms are these three.'))

S.append(cards('06 · ONE MODEL, FOUR PRODUCTS', 'The same diffusion model, shipped four ways.', [
    ('AS A FILL', 'Embodiment.', 'Generative Fill in Photoshop: select, type, done. The model withdraws into the toolbar. You forget it chose the middle for you.'),
    ('AS A FEED', 'Hermeneutic.', 'A style feed, a mood board that generates: you read taste off it. It looks like the world of design; it is the middle of a dataset.'),
    ('AS AN ASSISTANT', 'Alterity.', 'A chat that makes images and talks back: you brief it, argue with it, thank it. A quasi-other, trained to please.'),
    ('AS A DEFAULT', 'Background or immersion.', 'The artwork picked for each viewer, the thumbnail auto-generated, the layout chosen: nobody sees the choice being made. If it learns from you, it is immersion.'),
], text_size=22, notes='The product designer\'s slide: the relation is not in the model, it is in the product, and you choose it. The same weights can be a tool, a display, a face or a setting. Each choice has its risk from the figure. For the group project, the mediation brief asks exactly this: which relation are you building, and what does it do to the person? Netflix next: a real one, chosen and measured.'))

S.append(content('06 · NETFLIX · 7 DECEMBER 2017', 'The poster you saw was chosen for you.',
                 ['"Artwork Personalization at Netflix", Netflix Tech Blog: Chandrashekar, Amat, Basilico and Jebara. The same title, several images; a model picks the one each member is most likely to click, and learns from the click (a contextual bandit).',
                  '- Good Will Hunting: someone who watches romances sees Matt Damon and Minnie Driver; someone who watches comedies sees Robin Williams.',
                  '- Pulp Fiction: a fan of Uma Thurman sees Uma; a fan of John Travolta sees John.',
                  'Which relation? You read the catalogue off it: hermeneutic. Hidden, and mild: seductive, in Verbeek\'s terms. The poster designer now designs a space of images and the rule for choosing — and never sees the choice.'],
                 body_size=27,
                 notes='Verified: the post is from 7 December 2017 and both examples are in it. Two design readings. As mediation: hermeneutic — the picture is how you read the catalogue — and the influence is hidden and weak, which Verbeek calls seductive. As a job: the designer no longer makes one poster; they make a family and hand the choice to a model, and the choice is invisible to the viewer and to them. Ask: is this the same film? Is it the same catalogue for two people? The mediation brief in week 8 asks your product these questions.'))

S.append(cards('06 · THE FORCE OF A MEDIATION', 'Hidden or apparent. Weak or strong.', [
    ('COERCIVE', 'Strong, apparent.', 'Verbeek: a turnstile; a car that will not start without the seat belt. AI: a model that refuses to generate; a filter that blocks the upload.'),
    ('PERSUASIVE', 'Weak, apparent.', 'Verbeek: a smart energy meter; an e-coaching app. AI: "Are you still watching?"; a screen-time nudge; a draft with a suggestion you can decline.'),
    ('SEDUCTIVE', 'Weak, hidden.', 'Verbeek: a coffee machine in the hall; material that ages beautifully. AI: the artwork chosen for you; autoplay; the first draft that sounds fine.'),
    ('DECISIVE', 'Strong, hidden.', 'Verbeek: an apartment building without a lift. AI: the ranking that decides what you never see; the default the model picked and nobody reviewed.'),
], text_size=22, notes='Verbeek borrows the two axes from Tromp and colleagues: visibility and force. The four names and the non-AI examples are his; the AI examples are ours. The uncomfortable one is decisive: strong and hidden, and most recommendation and ranking systems live there. Responsible design, in his words, "does not shy away from influencing human behavior, but rather aims to give such influences a desirable direction." Your mediation brief has to say which quadrant your product is in, and why.'))

S.append(question('multiple_choice', 'Photoshop\'s Generative Fill is closest to which relation?', [
    'Embodiment: you act on the image through it', 'Hermeneutic: you read the world off it', 'Alterity: you face it as an other', 'Background: it shapes the room, unnoticed',
], eyebrow_text='06 · QUICK CHECK · MULTIPLE CHOICE',
    notes='A, with a caveat worth saying: the moment you type into the prompt box is a flicker of alterity, and the choice of what fills the hole is a hidden decision — seductive. Verbeek\'s point is that a product mixes relations, and the designer decides which one dominates. Anyone who answers D has a good argument if they mean the default fill nobody reviews.'))

S.append(statement('A tool is never neutral. A model is a tool that also has a middle.', eyebrow_text='06 · WHERE WE ARE', size=104,
                   notes='Two sentences to carry into the workshop. The first is Verbeek. The second is this course: a model mediates like any tool, and it also pulls what it makes towards the typical, silently. The workshop is about seeing that pull on a page you know how to read — a layout.'))

# ───────────────────────── 07 · the layout workshop ─────────────────────────
S.append(section('07', 'The layout workshop', f'a brief · two references · {GENAI} · Flux or Qwen', bg=INK,
                 notes='Chapter seven: the tools for the activity. The brief, what a layout model decides, and the four questions to ask a generated page. Four slides, then the rounds.'))

S.append(two_col('07 · THE BRIEF', 'One small real job. A poster you could design.',
                 ['The week-13 poster fair needs a poster. You briefed it in words last week; today an image model gives you a picture back — and you know what a layout should look like, so you can see what it decided.',
                  '- Image models on **genai.polyu.edu.hk**: **Flux** or **Qwen-Image**. Qwen-Image was built to render text; try it first.',
                  '- Ask for the layout, not a photo: "an A2 poster layout, flat, no photograph".',
                  'A landing page instead: allowed, same brief, one screen.'],
                 BRIEF, right_size=21, left_size=28,
                 notes='The brief is on the course site and on Blackboard. It is deliberately under-specified where a brief usually is: no typeface, no colours, no grid. Those are the decisions the model will make silently, and finding them is the exercise. Say the two practical things: ask for a layout, flat, no photograph — otherwise you get a stock image with type on it — and try Qwen-Image for anything with words, because its team built it for text rendering.'))

S.append(cards('07 · WHAT A LAYOUT MODEL DECIDES', 'Everything you did not say.', [
    ('HIERARCHY', 'What is biggest.', 'The title, usually, centred, usually. Ask why: because most posters in the dataset are. The middle of posters.'),
    ('THE GRID', 'Where things sit.', 'Columns, margins, alignment. A model has no grid; it has the average of a million grids, which looks like one until you measure it.'),
    ('TYPE AND COLOUR', 'What it looks like.', 'A geometric sans, a gradient, one accent. The prototype of "design poster" in the training data — often 2015 tech-conference.'),
    ('THE ADDITIONS', 'What nobody asked for.', 'A robot, a brain, a glowing circuit, a date it invented, a tagline. Week 4\'s "it adds", as pictures. Circle them.'),
], text_size=22, notes='Four places to look. Every one is a decision a designer would make on purpose and the model makes from its middle. The additions are the easiest to spot and the most useful to keep in the caption: a robot on a design-school poster is the dataset talking. The grid is the hardest to spot and the most important — round two is about it.'))

S.append(cards('07 · READ IT LIKE A DESIGNER', 'Four questions for a generated layout.', [
    ('DID IT DO WHAT I SAID?', 'Tick the brief.', 'Title, sub, when and where, the QR square. A missing one is a dropped constraint: restate it, one change per prompt.'),
    ('WHAT DID IT DECIDE?', 'Find the middle.', 'Centred title, geometric sans, a gradient, a robot. Name each one. That list is the caption of your upload.'),
    ('WHAT DID IT INVENT?', 'Find the guess.', 'A date, a room, a sponsor, words that are almost words. Where you wrote "to confirm", did it?'),
    ('WHICH RELATION?', 'Name the mediation.', 'Did you act through it, read off it, face it, or let it decide in the background? Which relation did the tool make with you today? Round four ends with this.'),
], text_size=22, notes='Week 4\'s four questions with the last one replaced: the mediation question. The TAs walk with these. The second question is the whole activity; the fourth is the bridge to the group project. Say that "which relation" has no wrong answer today, only a reason.'))

# ───────────────────────── 08 · activity: the silent decisions ─────────────────────────
S.append(section('08', 'The silent decisions.', f'35 minutes · one brief · {GENAI} · a layout, three ways', bg=YELLOWS[0],
                 notes='The activity. One brief, three rounds: alone from the brief only; in pairs with two references; in fours iterating three times with a spec of what changed. Each round ends in ClassPoint; the last capture is an image whose caption is the decision the model made silently. Nicolò keeps time; Amber, WU Zhao and MA Jie walk with the four questions. One device per pair at least; pen and paper for round two.'))

S.append(activity('1 — ALONE · THE BRIEF ONLY', 5, 'Generate it from the brief.',
                  [f'Open **{GENAI}**, pick **Flux** or **Qwen-Image**. Paste the brief on the right, as it is, with "an A2 poster layout, flat, no photograph" in front.',
                   'One image. Do not improve the prompt yet.',
                   'Circle, in your head, everything on it that you did not ask for. That is the middle.'],
                  panel=BRIEF, panel_size=21, bg=YELLOWS[0],
                  notes='Five minutes, silent. The brief is deliberately bare, like "a cup" in week 1 and the one-line brief in week 4: everyone gets the prototype. Watch for people who add adjectives; stop them — the point is to see the middle first. The TAs help with the model choice and with "no photograph".'))

S.append(question('image_upload', 'Everyone: upload your first layout.',
                  hint='The image from round 1, as it came, before you changed anything. We put them all on the wall.',
                  eyebrow_text='08 · CAPTURE 1 · IMAGE UPLOAD · EVERYONE',
                  notes='ClassPoint image upload, everyone, three minutes. The wall: a hundred posters from one brief, and most of them are the same poster — a centred title, a geometric sans, a gradient, and at least a dozen robots. The cup wall, the first-sentence wall, now in layout. Point at three: which decisions repeat? Those are the dataset\'s, not yours. Screenshot the wall.'))

S.append(activity('2 — IN PAIRS · TWO REFERENCES', 8, 'Give it a grid and a colour set.',
                  ['Same brief, same model, **new chat**. Draw a grid on paper — columns, the title band, where the QR goes — and photograph it. Pick three colours.',
                   'If the model takes an image input, upload both with the brief. If not, describe them in words, exactly.',
                   'Run it. **Which reference changed what?** The grid should move the geometry; the colours should move the surface.'],
                  panel=REFERENCES, panel_size=21, bg=YELLOWS[1],
                  notes='Eight minutes, one laptop per pair, pen and paper for the grid. The two references are the two handles from chapter five in miniature: the grid is a rule about geometry — ControlNet in words if there is no image input — and the colours are a constraint on the surface. Push them to say which reference did what. Expect the model to keep the centred title anyway: that is the middle winning over the reference, and it is worth saying aloud.'))

S.append(question('multiple_choice', 'Compared with round 1, the references…', [
    'Changed the layout, and we can say which reference did what', 'Changed the surface, not the geometry', 'Were mostly ignored: it did its own thing', 'Not back yet — help',
], eyebrow_text='08 · PULSE · MULTIPLE CHOICE',
    notes='Pulse, one minute; no correct answer, but A is the hoped-for one. B is the common honest answer: the colours landed, the grid did not — the middle keeps its grid. C means the reference was described too vaguely or the model has no image input; ask what words they used. Ds get a TA now.'))

S.append(activity('4 — TWO PAIRS · ITERATE, AND KEEP THE SPEC', 10, 'Three changes. Write each one down.',
                  ['Join the pair behind you. Pick the better round-2 layout. **Three iterations, one change each**, in three prompts. After each: what changed, in one line.',
                   'Find **the silent decision**: one thing the model decided that nobody asked for — and decide, as four, whether to keep it.',
                   'One scribe uploads the last layout. Caption: the three changes, and the silent decision.'],
                  panel=ITERATE, panel_size=21, bg=YELLOWS[2],
                  notes='Ten minutes in fours. One change per prompt so you know what caused what — week 2\'s iteration discipline, week 4\'s edit-the-brief. The silent decision is the deliverable: four people agreeing on what the model chose for them is a design team doing a critique. This is the start of Challenge 4; they finish it at home, alone or in the same four.'))

S.append(question('image_upload', 'Scribes only. The layout, and what it decided.',
                  hint='One image per four. Caption: the three changes, then "silent decision: …" — kept, or undone.',
                  eyebrow_text='08 · CAPTURE 2 · IMAGE UPLOAD · ONE PER FOUR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='Scribes only, about 28 images, caption required. Put the wall on screen next to capture 1. Read two captions aloud and ask the room to find the silent decision on the picture before you say it. Where the room finds a different one, both are right: the picture is full of them. Download the submissions: they are the seed of Challenge 4 and evidence for the reflection.'))

S.append(question('short_answer', 'Which relation did your layout tool create?',
                  hint='Embodiment, hermeneutic, alterity, background — or cyborg, immersion, augmentation. One word, then one line: why.',
                  eyebrow_text='08 · THE MEDIATION · SHORT ANSWER',
                  notes='Short answer, two minutes. Read six, sorted by relation. Most say alterity — they briefed it and argued with it — and some say hermeneutic — they read what a poster should be off it. Both are right, and the point is the reason. Then ask: which relation would the same model create if it were the "auto layout" button in Figma? Embodiment, or background. Same weights, a different product, a different relation. That is the mediation brief.'))

S.append(content('08 · WHAT JUST HAPPENED', 'It laid out every page. You found the decisions.',
                 ['The brief alone: a hundred posters, one poster. The middle of a million layouts, with a robot on it.',
                  'The references: a rule about geometry and a constraint on the surface moved the picture — and the middle kept what you did not pin down. You could say which reference did what. That is authorship.',
                  'The iterations: one change per prompt, and a caption that names what the model chose. A critique is a list of silent decisions made loud.',
                  '**The machine laid out every page. You decided what it had decided. That was the design.**'],
                 body_size=31,
                 notes='Mirror of the whole class, and of weeks 1, 2 and 4: the cup, the spec, the brief, the layout. Say the last line slowly. Then the sentence for the reflection: an image model is machine B with a middle; every handle you used today was a rule laid over it or an example given to it; and the relation it made with you was chosen by whoever put it in a text box.'))

# ───────────────────────── 09 · challenge 4 · homework ─────────────────────────
S.append(cards('09 · CHALLENGE 4 · DUE BEFORE WEEK 6', 'A layout you could not design — generated, iterated, critiqued.', [
    ('THE LAYOUT', 'A poster or a page.', 'A real job of yours, or today\'s brief pushed somewhere you could not have taken it by hand. The brief and the references, kept.'),
    ('THE SPEC', 'What changed, each step.', 'v1 to v4 at least: one change per step, one line each. The model named. The seed, if the tool shows it.'),
    ('THE CRITIQUE', 'What it decided.', 'Three lines: the silent decisions you found, which you kept and why, and the relation the tool created with you — one of the seven.'),
    ('THE VOTE', 'All of it on Blackboard.', 'Layout, spec, critique, together. The room votes in week 6; winners get a star. TAs help 30 minutes before and after class.'),
], notes='Four things on Blackboard before week 6: the final layout with the brief and references, the spec of changes, the three-line critique, and the model named. The critique is the assignment; the layout is the evidence. Next week the room votes.'))

S.append(video('09 · BEFORE WEEK 6 · SOUND MACHINES', 'One video, and a draft of your reflection.', 'bp7Qb8QY1Pw',
               ['**Watch, on the playlist:** AltexSoft, How AI Sound and Music Generation Works. Spectrograms, MIDI, and the same walk from noise — in sound.',
                '- **Bring a draft of your reflection.** Next week the TAs check drafts: the rule-based versus adaptive argument, and three experiments from the challenges. Due in week 7.',
                '- Next week also has the mock quiz: weeks 1 to 6 and the playlist.',
                'Bring headphones.'],
               thumb='yt/bp7Qb8QY1Pw.jpg', body_size=27,
               notes='Next week is sound: what a spectrogram is, how a music model is a diffusion model or a language model on sound, and the authenticity and copyright argument. One video, headphones, and a draft of the reflection — the TAs will read drafts before and after class. The mock quiz is next week too; it draws on the playlist.'))

S.append(end('See you next week. Sound machines.',
             'Bring your layout. Watch AltexSoft. Headphones, and a reflection draft.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: sound machines — spectrograms, MIDI, generated music and voice, the UMG v. Udio settlement — and the Challenge 4 vote. Homework in one line: the layout on Blackboard, one video, headphones, a draft. The TAs stay for 30 minutes.'))

DECK = dict(title='SD2112 · AI in Design · Week 05', slides=finalize(S, FOOTER), pdf='SD2112-week05.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week05', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 2026-09-05)
# Verbeek, P.-P. (2015). Beyond interaction: a short introduction to mediation theory. Interactions 22(3), 26–31.
#   https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf (full text: Ihde's four relations with the phone / microscope,
#   MRI scan / metal detector, ATM / robot, fridge / heating examples; cyborg, immersion, augmentation; Tromp's coercive /
#   persuasive / seductive / decisive; Dorrestijn's contact points; "Designing technology is designing human beings…")
#   https://research.utwente.nl/en/publications/cover-story-beyond-interaction-a-short-introduction-to-mediation-/
#   https://interactions.acm.org/archive/view/may-june-2015/beyond-interaction
# Ihde, D. (1990). Technology and the Lifeworld: From Garden to Earth. Indiana University Press.
#   https://iupress.org/9780253205605/technology-and-the-lifeworld/ · https://www.futurelearn.com/info/courses/philosophy-of-technology/0/steps/26324
# Netflix Tech Blog (7 December 2017). Artwork Personalization at Netflix. Chandrashekar, Amat, Basilico, Jebara.
#   https://netflixtechblog.com/artwork-personalization-c589f074ad76 (Good Will Hunting, Pulp Fiction examples; contextual bandits)
#   https://www.dezeen.com/2017/12/20/netflix-targets-film-artwork-depending-users-viewing-habits-design-technology/
# Sohl-Dickstein, Weiss, Maheswaranathan & Ganguli (2015). Deep Unsupervised Learning using Nonequilibrium Thermodynamics. https://arxiv.org/abs/1503.03585
# Ho, Jain & Abbeel (2020). Denoising Diffusion Probabilistic Models. https://arxiv.org/abs/2006.11239 (T = 1000; β from 1e-4 to 0.02, linear)
# Ronneberger, Fischer & Brox (2015). U-Net: Convolutional Networks for Biomedical Image Segmentation. https://arxiv.org/abs/1505.04597
# Radford et al. (2021). Learning Transferable Visual Models From Natural Language Supervision (CLIP). https://arxiv.org/abs/2103.00020 (400M pairs)
# Ho & Salimans (2022). Classifier-Free Diffusion Guidance. https://arxiv.org/abs/2207.12598
# Rombach, Blattmann, Lorenz, Esser & Ommer (2022). High-Resolution Image Synthesis with Latent Diffusion Models, CVPR 2022. https://arxiv.org/abs/2112.10752
# Stable Diffusion: https://github.com/CompVis/stable-diffusion (factor-8 autoencoder, 860M UNet, CLIP ViT-L/14, 50 PLMS steps, scale 7.5)
#   https://huggingface.co/CompVis/stable-diffusion-v1-4 (H × W × 3 → H/8 × W/8 × 4) · https://en.wikipedia.org/wiki/Stable_Diffusion (22 August 2022)
#   https://stability.ai/news-updates/stable-diffusion-public-release
# Hu et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. https://arxiv.org/abs/2106.09685
# Ruiz et al. (2022). DreamBooth. https://arxiv.org/abs/2208.12242
# Zhang, Rao & Agrawala (2023). Adding Conditional Control to Text-to-Image Diffusion Models (ControlNet), ICCV 2023. https://arxiv.org/abs/2302.05543
#   https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html
# ComfyUI: https://en.wikipedia.org/wiki/ComfyUI (first release 16 January 2023)
# Adobe Generative Fill, 23 May 2023: https://news.adobe.com/news/news-details/2023/adobe-unveils-future-of-creative-cloud-with-generative-ai-as-a-creative-co-pilot-in-photoshop
#   https://techcrunch.com/2023/05/23/adobe-brings-fireflys-generative-ai-to-photoshop/
# FLUX.1, Black Forest Labs, 1 August 2024: https://venturebeat.com/ai/stable-diffusion-creators-launch-black-forest-labs-secure-31m-for-flux-1-ai-image-generator
#   https://en.wikipedia.org/wiki/Flux_(text-to-image_model)
# Qwen-Image, 4 August 2025: https://qwenlm.github.io/blog/qwen-image/ · https://www.alibabacloud.com/blog/introducing-qwen-image-novel-model-in-image-generation-and-editing_602447
# Midjourney open beta 12 July 2022: https://en.wikipedia.org/wiki/Midjourney
# Welch Labs / 3Blue1Brown, 25 July 2025: https://www.3blue1brown.com/lessons/diffusion-models/
# Video titles verified with YouTube oEmbed: iv-5mZ_9CPY, yTAMrHVG1ew, KcSXcpluDe4, qiUEgSCyY5o, -dfSZ_uLfo8, dECiAdfn2d4, bXAl9XAsF44, bp7Qb8QY1Pw
