"""
SD2112 · Artificial Intelligence in Design · Week 08 — the slide spec.

    python deck/week08.py            # builds _site/week08/ (html deck + pdf), export/week08*.pptx, export/preview/
    python deck/week08.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

AI as design material: module 3 opens. Using versus incorporating, now on the product side; a product
that decides something for each person (the decision, the data, the score, the threshold, the fallback);
five products read as designers (Spotify DJ, Netflix, Duolingo, the Humane AI Pin, the Rabbit R1); the
double diamond with a model inside; a model as a material (grain, edges, appetite, drift); Scrum and
versioning for a design team; the brainstorm ladder; and the activity "Ten ideas. One decision.", which
starts the group proposal. Three live p5.js sketches; drawn figures in tools/figures_week08.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week08 as F8                             # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, sketch_slide, code_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(8)
CHAIRS = [f'ai-chair-{i}.jpg' for i in range(1, 5)]   # week 1: one prompt, four seeds

# ───────────────────────── the live sketches (html deck; the pptx and the PDF show a snapshot) ─────────────────────────
DECIDE_CODE = """// A product that decides something for each person.
// 120 people, two hidden traits each: how much they like new
// things, how much time they have. The rule: score = w * novelty
// + (1 - w) * time; show the new thing if score > t.
// mouse x = the threshold t · mouse y = the weight w · click = new people
const N = 120, ORANGE = '#ED6D24';
let people = [];

function setup() {
  createCanvas(1400, 560); textFont('JetBrains Mono');
  randomSeed(2112); make();
}

function make() {                       // the people, and the truth nobody sees
  people = [];
  for (let i = 0; i < N; i++) {
    let nov = random(), tim = random();
    let wants = 0.55 * nov + 0.45 * tim + random(-0.22, 0.22) > 0.62;
    people.push({ nov, tim, wants });
  }
}

function draw() {
  background(255);
  let t = constrain(mouseX / width, 0, 1);            // the threshold
  let w = constrain(1 - mouseY / height, 0, 1);       // the weight on novelty
  let px = 70, py = 50, pw = 640, ph = 440;           // the plane
  noFill(); stroke(215); strokeWeight(1); rect(px, py, pw, ph);
  let shown = 0, wanted = 0, hit = 0;
  for (let p of people) {
    let show = w * p.nov + (1 - w) * p.tim > t;       // the rule
    shown += show; wanted += p.wants; hit += show && p.wants;
    mark(px + p.nov * pw, py + ph - p.tim * ph, show, p.wants);
  }
  boundary(px, py, pw, ph, t, w);
  noStroke(); fill(90); textSize(14);
  text('likes new things →', px, py + ph + 24);
  push(); translate(px - 14, py + ph); rotate(-HALF_PI); text('has time →', 0, 0); pop();
  // the rule and the counts
  let rx = 770;
  fill(0); textSize(20);
  text('show it if  ' + nf(w, 1, 2) + ' × novelty + ' + nf(1 - w, 1, 2) + ' × time  >  ' + nf(t, 1, 2), rx, 90);
  textSize(15); fill(90);
  text('mouse x = threshold t · mouse y = weight w · click = new people', rx, 118);
  bar(rx, 160, shown / N, 'shown to ' + round(100 * shown / N) + ' % of people', ORANGE);
  bar(rx, 240, shown ? hit / shown : 0, 'of whom ' + (shown ? round(100 * hit / shown) : 0) + ' % would have wanted it', ORANGE);
  bar(rx, 320, wanted ? (wanted - hit) / wanted : 0, 'missed: ' + (wanted ? round(100 * (wanted - hit) / wanted) : 0) + ' % of those who wanted it never saw it', '#5C6470');
  legend(rx, 420, true, true, 'shown, wanted');
  legend(rx + 200, 420, true, false, 'shown, not wanted (annoyed)');
  legend(rx, 446, false, true, 'wanted, not shown (missed)');
  legend(rx + 300, 446, false, false, 'neither');
  noStroke(); fill(0); textSize(14);
  text('the truth is hidden: nobody knows who wants it until it is shown', rx, 490);
}

function mark(x, y, show, wants) {      // one mark per outcome; the legend is drawn by the same function
  strokeWeight(2);
  if (show && wants) { stroke(ORANGE); fill(ORANGE); circle(x, y, 15); }   // the hit
  else if (show) { stroke(ORANGE); fill(255); circle(x, y, 15); }          // the annoyance
  else if (wants) { noStroke(); fill(ORANGE); circle(x, y, 9); }           // the miss
  else { stroke(200); fill(225); circle(x, y, 9); }                        // the default
}

function legend(x, y, show, wants, label) {
  mark(x + 8, y - 5, show, wants);
  noStroke(); fill(0); textSize(14); text(label, x + 26, y);
}

function bar(x, y, k, label, col) {
  noStroke(); fill(235); rect(x, y, 560, 22);
  fill(col); rect(x, y, 560 * k, 22);
  fill(0); textSize(16); text(label, x, y + 44);
}

function boundary(px, py, pw, ph, t, w) {    // the line where score = t
  stroke(0); strokeWeight(2); noFill();
  if (w > 0.999) { line(px + t * pw, py, px + t * pw, py + ph); return; }   // all the weight on novelty: vertical
  let pts = [];
  for (let i = 0; i <= 64; i++) {
    let nov = i / 64, tim = (t - w * nov) / (1 - w);
    if (tim >= 0 && tim <= 1) pts.push([px + nov * pw, py + ph - tim * ph]);
  }
  for (let i = 1; i < pts.length; i++) line(pts[i - 1][0], pts[i - 1][1], pts[i][0], pts[i][1]);
}

function mousePressed() { make(); }"""

PERSONALISE_CODE = """// A home screen: twelve cards on a 3 x 4 grid, and a dial.
// At 0 % everyone sees the same screen. At 100 % nobody does.
// Every card has a shared rank (popularity) and a personal rank
// (this person's taste); the dial blends the two, then the grid is
// rebuilt from the blended rank — one weighted sum, like a real feed.
// mouse x = how personalised · keys 1 to 4 = which person you are
const CATS = ['music', 'news', 'sport', 'food', 'film', 'travel'];
const COLS = ['#64C2C3', '#943890', '#ED6D24', '#F6AD00', '#E94D7F', '#5C6470'];
let items = [], profiles = [], pos = [], who = 0;

function setup() {
  createCanvas(1400, 560); textFont('JetBrains Mono'); randomSeed(8);
  for (let i = 0; i < 12; i++) items.push({ cat: i % 6 });   // shared order: by popularity, 1 first
  for (let p = 0; p < 4; p++) {                              // four people, a taste per category
    let taste = [];
    for (let c = 0; c < 6; c++) taste.push(random());
    profiles.push(taste); pos.push([]);
  }
}

function slots(p, k) {                  // the blended order: (1 - k) * shared rank + k * personal rank
  let idx = items.map((it, i) => i);
  let personal = idx.slice().sort((a, b) => profiles[p][items[b].cat] - profiles[p][items[a].cat] || a - b);
  let prank = []; personal.forEach((it, r) => prank[it] = r);
  let score = idx.map(i => (1 - k) * i + k * prank[i]);
  let order = idx.sort((a, b) => score[a] - score[b] || a - b);
  let slot = []; order.forEach((it, s) => slot[it] = s);
  return slot;
}

function screen(x, y, w, h, p, k, big) {  // the grid, rebuilt from the blended order; cards ease into place
  let gap = big ? 10 : 5, cw = (w - gap * 4) / 3, ch = (h - gap * 5) / 4, moved = 0;
  let slot = slots(p, k);
  for (let i = 0; i < 12; i++) {
    let tx = x + gap + (slot[i] % 3) * (cw + gap), ty = y + gap + floor(slot[i] / 3) * (ch + gap);
    let key = big ? 'b' + i : 's' + i;
    if (!pos[p][key]) pos[p][key] = { x: tx, y: ty };
    let c = pos[p][key]; c.x = lerp(c.x, tx, 0.25); c.y = lerp(c.y, ty, 0.25);
    if (slot[i] != i) moved++;
    noStroke(); fill(lerpColor(color(COLS[items[i].cat]), color(255), (1 - profiles[p][items[i].cat]) * 0.75 * k));
    rect(c.x, c.y, cw, ch, 4);
    if (big) { fill(0); textSize(14); text(CATS[items[i].cat] + ' ' + (i + 1), c.x + 8, c.y + 20); }
  }
  return moved;
}

function draw() {
  background(255);
  let k = constrain(mouseX / width, 0, 1);
  // the dial
  noStroke(); fill(235); rect(60, 30, 1280, 10);
  fill('#ED6D24'); rect(60, 30, 1280 * k, 10); circle(60 + 1280 * k, 35, 22);
  fill(0); textSize(16);
  text('0 %  the same screen for everyone', 60, 66);
  textAlign(RIGHT); text('100 %  one screen per person', 1340, 66); textAlign(LEFT);
  text(round(100 * k) + ' % personalised', 640, 66);
  // the big screen: the person you are
  stroke(0); strokeWeight(2); noFill(); rect(60, 90, 360, 400, 8);
  let moved = screen(60, 90, 360, 400, who, k, true);
  noStroke(); fill(0); textSize(16);
  text('person ' + (who + 1) + '  (keys 1 – 4)', 460, 118);
  text(moved + ' of 12 cards are not where everyone else sees them', 460, 144);
  // the four people, side by side
  for (let p = 0; p < 4; p++) {
    let x = 460 + p * 220;
    stroke(p == who ? '#ED6D24' : 0); strokeWeight(p == who ? 3 : 1); noFill(); rect(x, 170, 190, 270, 6);
    screen(x, 170, 190, 270, p, k, false);
    noStroke(); fill(p == who ? '#ED6D24' : 0); textSize(14); text('person ' + (p + 1), x, 464);
  }
  fill(90); textSize(14);
  text(k < 0.02 ? 'four people, one product' : k > 0.98 ? 'four people, four products: nobody can show a friend "the app"' : 'the further right, the less any two of them share', 460, 492);
}

function keyPressed() {
  if (key >= '1' && key <= '4') { who = int(key) - 1; return false; }
}"""

DIAMOND_CODE = """// The double diamond (Design Council, 2004) with a model inside.
// mouse x = where you are in the process; the text under the diamond
// says what the model does — or is — in that phase.
const PHASES = [
  ['DISCOVER', 'what data exists?', 'There is no model yet. Who is the person, what is the moment, what do you already know about them — and what would you have to take from them to decide anything.'],
  ['DEFINE', 'the decision, in one sentence', 'The model is a sentence: "for this person, at this moment, it decides X." Then the score it needs, the threshold you will set, and the fallback when the score is below it.'],
  ['DEVELOP', 'rule or model? the wizard first', 'Write the rule (machine A) if you can say it; show examples (machine B) if you cannot. Before either exists, a teammate behind a curtain plays the model and you test the decision.'],
  ['DELIVER', 'guardrails and monitoring', 'What it may never decide; when a human steps in; what you watch after launch — the two kinds of error, the people at the edge of the grain, and the drift after every retraining.'],
];
let cur = 2, slide = 0;

function setup() { createCanvas(1400, 500); textFont('JetBrains Mono'); }

function draw() {
  background(255);
  let ph = constrain(floor(4 * mouseX / width), 0, 3);
  if (ph != cur) { cur = ph; slide = 1; }
  slide = max(0, slide - 0.08);                       // the text slides in
  let x0 = 90, x1 = 1310, y = 170, h = 110, mid = (x0 + x1) / 2, q = (mid - 12 - x0) / 2;
  let tris = [                                        // the four phases as four halves
    [[x0, y], [x0 + q, y - h], [x0 + q, y + h]], [[x0 + q, y - h], [mid - 12, y], [x0 + q, y + h]],
    [[mid + 12, y], [mid + 12 + q, y - h], [mid + 12 + q, y + h]], [[mid + 12 + q, y - h], [x1, y], [mid + 12 + q, y + h]],
  ];
  for (let i = 0; i < 4; i++) {
    let t = tris[i];
    stroke(0); strokeWeight(2); fill(i == cur ? '#F9E5D6' : 255);
    triangle(t[0][0], t[0][1], t[1][0], t[1][1], t[2][0], t[2][1]);
    noStroke(); fill(i == cur ? '#ED6D24' : 120); textSize(16); textAlign(CENTER);
    text(PHASES[i][0], (t[0][0] + t[1][0] + t[2][0]) / 3, y + h + 30);
  }
  textSize(14); fill(90);
  text('THE PROBLEM · diverge, then converge', x0 + q, y - h - 16);
  text('THE SOLUTION · diverge, then converge', mid + 12 + q, y - h - 16);
  marker(cur, x0, x1, y, mid, q);
  // what the model does in this phase
  let dx = 24 * slide;
  textAlign(LEFT); fill(0); textSize(24); text(PHASES[cur][0] + '  ·  ' + PHASES[cur][1], x0 + dx, 340);
  fill(60); textSize(16); text(PHASES[cur][2], x0 + dx, 360, 1200, 120);
  fill(150); textSize(14); text('move the mouse across the four phases', x0, 466);
}

function marker(ph, x0, x1, y, mid, q) {              // the model inside: where it is in each phase
  textAlign(CENTER); textSize(14);
  if (ph == 0) { noFill(); stroke(150); strokeWeight(1); rect(x0 + q - 22, y - 22, 44, 44); tag(x0 + q, y + 4, 'no model yet: what data is there?', 120); }
  if (ph == 1) { noStroke(); fill('#943890'); rect(mid - 34, y - 22, 44, 44, 4); tag(mid - 12, y + 42, 'one sentence', 0); }
  if (ph == 2) { noStroke(); fill('#943890'); rect(mid + 12 + q - 44, y - 36, 88, 72, 6); fill(255); text('THE MODEL', mid + 12 + q, y + 5); tag(mid + 12 + q, y + 60, 'rule? examples? a wizard?', 0); }
  if (ph == 3) { noStroke(); fill('#943890'); rect(x1 - 96, y - 22, 44, 44, 4); stroke('#ED6D24'); strokeWeight(3); noFill(); rect(x1 - 108, y - 34, 68, 68, 8); tag(x1 - 74, y + 58, 'inside a guardrail, watched', 0); }
}

function tag(x, y, t, col) {                          // a label on a white backing, so the diamond's lines do not cross it
  noStroke(); fill(255); rectMode(CENTER); rect(x, y - 5, textWidth(t) + 12, 20); rectMode(CORNER);
  fill(col); text(t, x, y);
}"""

# ───────────────────────── the panels of the activity ─────────────────────────
LADDER_PANEL = [
    'THE LADDER · ONE LINE PER RUNG', ' ',
    '1  THE PERSON    who, exactly? one person, not "users"',
    '2  THE MOMENT    when and where does it meet them?',
    '3  THE DECISION  what does it decide for them?',
    '4  THE DATA      what must it know? does that exist?',
    '5  THE FAILURE   the day it is wrong: what do they see?', ' ',
    'ONE IDEA = ONE LINE, e.g.', ' ',
    'a night-shift nurse · on the minibus home, 7:40 · it decides',
    'what she eats tonight · her roster, what she bought · it',
    'suggests the dish she just had at work', ' ',
    'ten of these. quantity first. no judging until round 2.',
]

PICK_PANEL = [
    'THREE TESTS · PICK THE IDEA THAT PASSES ALL THREE', ' ',
    'A  DOES THE DATA EXIST?', '   somewhere, today, about this person — or could', '   you ask for it and get a yes?', ' ',
    'B  IS THE FAILURE SURVIVABLE?', '   the day it is wrong, is she annoyed — or hurt,', '   excluded, exposed?', ' ',
    'C  CAN YOU WIZARD IT BY WEEK 10?', '   could one of you play the model behind a', '   curtain and test the decision on a stranger?', ' ',
    'tie? take the one with the clearest sentence at rung 3.',
]

CARD_PANEL = [
    'THE DECISION CARD · ON PAPER · A4, LANDSCAPE', ' ',
    'TEAM        ___', ' ',
    'THE DECISION   for this person, at this moment,', '               it decides ____________________', ' ',
    'FOR WHOM       one person, named like a character', ' ',
    'THE DATA       what it must know · have / do not have', ' ',
    'IF IT IS WRONG what she sees · what she can do', '               · the fallback', ' ',
    'big letters. a phone photo has to read it from the wall.',
]

GALLERY_PANEL = [
    'THE GALLERY · FOUR CARDS · TEAM NUMBERS, NO NAMES', ' ',
    'CARD A   team ___', 'CARD B   team ___', 'CARD C   team ___', 'CARD D   team ___', ' ',
    'THREE QUESTIONS FOR EACH CARD', ' ',
    '1  is the decision one sentence?', '2  does the data exist — today, about this person?', '3  the wrong day: what does she see, what can she do?', ' ',
    'THEN THE VOTE: the product you would let decide for you.',
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 08 · LECTURE + WORKSHOP',
               'AI as design material.',
               'Week 8 — a product that decides something for each person.',
               notes='Join code on screen from 30 minutes before. Today sit with your team from the start: the second half is the first sprint of the group project. The TAs have the team list from week 7 and are seating people who were absent.'))

S.append(agenda('SD2112 · WEEK 08', [
    'Last week, in your words', 'Using, or incorporating', 'Five products, read as designers', 'The double diamond, with a model inside',
    'A model as a material', 'Working as a team', 'Workshop: the brainstorm ladder', 'Activity: ten ideas, one decision',
], notes='Eight stops. The first five are the lecture: the distinction from week 1 turned towards the product, five products taken apart with one card, the design process with a model in it, and the model as a material with a grain. Break. Then how a team of four or five works for six weeks, the brainstorm ladder, and the activity, which ends with your decision card on the wall and starts the group proposal.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the quiz · the pitches · the teams', bg=INK,
                 notes='Eight minutes of recap from what you gave us last week: the quiz, the pitch sentences, and the teams. Module 3 opens today.'))

S.append(question('short_answer', 'Your team number, and what your product decides for each person.',
                  hint='One line. "Team 12: it decides what a night-shift nurse eats tonight." No sentence yet? Write the team number and "not yet".',
                  eyebrow_text='01 · WARM-UP · SHORT ANSWER',
                  notes='ClassPoint short answer, two minutes, one per person so that every team hears itself disagree. Read six aloud. Most sentences name a product, not a decision: "an app for students" is not a decision; "it decides which of your notes to show you at 8 a.m." is. Do not correct them yet: by the end of the class every team rewrites this line on a card. Keep the screenshot: the activity compares the two.'))

S.append(cards('01 · WEEK 7 · IN THREE LINES', 'The quiz, the pitches, the teams.', [
    ('THE QUIZ', 'Three questions the room got wrong.',
     'The question, the answer, and the week that taught it — three of them, from the quiz export, read aloud. They come back in the final quiz in week 13, reworded.'),
    ('THE PITCHES', 'About twenty-five sentences.',
     'Most pitched a product. A few pitched a decision. Today turns every product into a decision: for this person, at this moment, it decides X.'),
    ('THE TEAMS', 'Four or five people. Sit with them.',
     'Teams are on Blackboard. If you were absent, the TAs are placing you now. From next week: a fifteen-minute stand-up at your table before every class.'),
], text_size=24, notes='Before class, paste the three most-missed questions from Amber\'s quiz export into the first card, or read them from the export: read each, give the answer, point at the week that taught it. The pitches: name two good sentences from the wall without names. Teams: anyone not on a team goes to Amber now, not at the break.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(3, 0),
                 notes='Module 3, first week of three. Weeks 8 to 10 are the product side: the model inside the thing you design; next week is data, bias and privacy, then recommendation systems. Module 4 is what is left for the designer. The group proposal is the first deliverable and it is due before next week.'))

# ───────────────────────── 02 · using, or incorporating ─────────────────────────
S.append(section('02', 'Using, or incorporating', "week 1's distinction · now on the product side", bg=ORANGES[0],
                 notes='Chapter two: the distinction that organises the course, turned around. Six weeks of AI in your process; now AI in your product. And the sentence that runs through every week from here: a product that decides something for each person.'))

S.append(cards('02 · THE DISTINCTION, TURNED AROUND', 'The model was in your process. Now it is in your product.', [
    ('WEEKS 1 – 6 · USING', 'A model in how you design.',
     ['A brief drafted with a chatbot, a moodboard from a diffusion model, a layout you could not design, thirty seconds of sound. The model made things; you chose what shipped.',
      'The mediation was between you and your own work.']),
    ('WEEKS 8 – 12 · INCORPORATING', 'A model in what you design.',
     ['A feed, a recommendation, an assistant, a poster picked per person. The model decides something for each person who uses the product, on its own, at scale, while you are asleep.',
      'The mediation is between your product and a stranger. You design that.']),
], notes='Week 1, slide by slide, said this: using is about your practice, incorporating is about the outcome. The new word is "decides". In the first half of the course the model produced and you decided. From now on the model decides, and you design the deciding: what it may decide, from what, how sure it must be, and what happens when it is wrong. Every week until the fair is one of those four.'))

S.append(figure_slide('02 · A PRODUCT THAT DECIDES', 'Five parts. You design all five.', F8.w08_decision_anatomy(),
                      body=['A person, their data, a score, a threshold, and two branches: the decision and the fallback. The score is the only part a model makes. Everything else — what to take, how sure is sure enough, what the wrong branch looks like — is a design decision that somebody makes by hand, or by not making it.'],
                      caption='The vocabulary for the next six weeks. The mediation brief asks for the data, the bias, the guardrails and the relation; all four sit on this drawing.',
                      notes='Walk left to right. The data: given, taken or inferred; you choose which. The score: one number, how likely this person wants the thing; a rule can write it (machine A) or a model can learn it (machine B). The threshold: a number somebody sets, and it decides how often the product is wrong in each direction. The two branches: the decision, and the fallback — what the person gets when the score is below the line, which is usually the old product. Ask: in Netflix, what is the fallback? The default poster. In a chatbot? A human, or nothing. The next slide lets you move the threshold.'))

S.append(sketch_slide('02 · LIVE · THE THRESHOLD', 'A threshold is a design decision.',
                      live('w08-decide', DECIDE_CODE, 1400, 560, hint='mouse x = the threshold · mouse y = the weight · click = new people'),
                      body=['A hundred and twenty people, each with two traits the product cannot see. One rule scores them; the threshold decides who gets the new thing. Every position of the line trades one mistake for the other.'],
                      caption='The model gives you the score. Where you cut it is yours — and the counters are the two numbers a team should be able to say about its product before it ships.',
                      notes='Move the mouse to the right: fewer people are shown the thing, and a larger share of them wanted it — but the missed number grows. To the left: everyone gets it, most of them did not want it. Up and down changes what the rule weighs. There is no position where both errors are zero, because the truth is hidden. Ask the room where they would put the line for a birthday-discount message, and where for a "we think you are at risk" message. Different lines, same rule. Click reshuffles the people: the shape stays, the numbers move — the grain, in chapter five.'))

S.append(cards('02 · TWO MISTAKES', 'Every threshold makes two mistakes.', [
    ('SHOWN · WANTED', 'The hit.', 'The product decided, and the person is glad. This is the only outcome anyone demos. It is also the only one you cannot design; the other three you can.'),
    ('SHOWN · NOT WANTED', 'The annoyance.', 'The poster that means nothing to you, the DJ that talks over the song, the discount for a thing you already bought. Cheap for the product, paid by the person, a hundred times a day.'),
    ('NOT SHOWN · WANTED', 'The miss.', 'The person who needed it never saw it. Invisible: nobody complains about what they did not see. It shows up only if you go looking, and only for the people whose data you have.'),
    ('NOT SHOWN · NOT WANTED', 'The default.', 'Most people, most of the time, get the fallback. If the fallback is bad, the product is bad for most people, however good the model. Design the fallback first.'),
], text_size=22, notes='The two mistakes have names in statistics — false positive, false negative — and feelings in design: the annoyance and the miss. Moving the threshold trades one for the other; it never removes both. The design question is which mistake your person can afford: a wrong song is nothing, a wrong medical nudge is not. Then the fourth card, which nobody thinks about: the fallback is what most people get.'))

S.append(sketch_slide('02 · LIVE · PERSONALISATION', 'At 100 %, no two people see the same product.',
                      live('w08-personalise', PERSONALISE_CODE, 1400, 560, hint='mouse x = how personalised · keys 1 – 4 = which person you are'),
                      body=['Twelve cards, one home screen. The dial blends the same-for-everyone order into a per-person order driven by a hidden profile. Turn it up and watch the four people drift apart.'],
                      caption='This is the week-1 Netflix poster, generalised: you no longer draw the screen. You draw the cards, the rule that orders them, and the dial — and you decide where the dial sits.',
                      notes='At zero, four people, one product: you can screenshot it, print it, put it on a poster. At a hundred, nobody can show a friend "the app", and nobody — including you — has seen the whole product. Press 1 to 4 to become each person. Somewhere in between is a design decision most teams never make on purpose: how much of the screen is shared. Shared parts can be talked about; personal parts cannot. Ask: what on your phone is the same for everyone in this room? Not much, and that is recent.'))

S.append(statement('You no longer design the screen. You design the space of screens, and who gets which.', eyebrow_text='02 · WHERE THIS LEAVES YOU', size=96,
                   notes='The sentence of the chapter. The artefact you used to make becomes a space of possible artefacts and a rule for choosing among them. Week 1 said it about the Netflix poster; today it is every product with a model inside. One quick check, then the next chapter reads five of them with one card.'))

S.append(question('multiple_choice', 'A product shows a new feature only to people whose score is above 0.7. Who decided 0.7?', [
    'The model learned it from the data', 'Someone chose it — and can change it', 'The users, by clicking', 'Nobody; it is the natural cut',
], eyebrow_text='02 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. A model gives every person a score; where to cut it is a number a person typed, in a meeting, or in a default nobody read. It moves with the business, with the season and with every retraining. If the room says A, go back to the threshold sketch on slide 10: it has no model in it, only a rule and a slider, and the errors are already there. Whoever owns that number owns the two mistakes.'))

# ───────────────────────── 03 · five products, read as designers ─────────────────────────
S.append(section('03', 'Five products, read as designers', 'Spotify · Netflix · Duolingo · Humane · Rabbit · 2015 – 2025', bg=INK,
                 notes='Chapter three: one card, five products. Three that ship and two that did not survive. Read each as a designer: what does it decide, for whom, from what, and what happens when it is wrong. The cautionary cases are the ones that teach the most.'))

S.append(content('03 · HOW TO READ A PRODUCT', 'Five questions. One card.',
                 ['One card, five rows, in this order:',
                  '- **The decision:** what it decides for each person, in one sentence.',
                  '- **For whom:** one person, at one moment.',
                  '- **The data:** what it must know, and where it comes from.',
                  '- **The score, the threshold:** who makes the number, who cuts it.',
                  '- **If it is wrong:** what the person sees, and what they can do.'],
                 figure=F8.w08_card_blank(), caption='The decision card. Blank now; on the wall, in your handwriting, by 2:40.',
                 body_size=28,
                 notes='Every product with a model inside can be read with these five rows, and the reading is faster than any teardown. The fifth row is the one that separates products that last from products that do not. Practise on the next five together; the room fills the rows aloud before I show the card.'))

S.append(content('03 · SPOTIFY DJ · 22 FEBRUARY 2023', 'A model chooses the song. A model says why.',
                 ['Beta for Premium listeners in the US and Canada; 50 markets by August 2023.',
                  '- Two decisions in one product: **what plays next**, from the personalisation model; and **what to say about it**, written with generative AI and read by a voice model of Xavier "X" Jernigan, made with Sonantic, a voice company Spotify had bought.',
                  '- The words are not free-running: a "Writers\' Room" of music and culture experts, data curators and scriptwriters shapes the commentary.',
                  '- The fallback is a button. "If you\'re not feeling the vibe, just tap the DJ button and it will switch it up."'],
                 figure=F8.w08_card_spotify(), caption='The card, filled. Spotify Newsroom, 22 February and 8 March 2023; the expansion to 50 markets, 8 August 2023.',
                 body_size=26,
                 notes='Ask the room for the five rows before showing the card. The interesting design decision is the second one: the DJ talks, and talking is a decision too — which fact about the artist, in which tone. Spotify put humans in that loop, the Writers\' Room, which is machine A guarding machine B. And the fallback is one big button: cheap to press, obvious, always there. Compare that with the Pin in three slides.'))

S.append(content('03 · NETFLIX · ARTWORK 2017 · ROWS 2015', 'The same film wears a different face for each of you.',
                 ['- **Artwork:** several images per title; a contextual bandit picks the one each member is most likely to click, and learns from the click. Netflix Tech Blog, December 2017.',
                  '- **Rows:** the home page is assembled per member from candidate rows — found, filtered, ranked, then ordered — with no fixed template. Tech Blog, April 2015.',
                  '- The fallback is the scroll. The miss becomes data: a poster you passed is a vote against it.',
                  'The poster designer makes a **space** of posters. The page designer makes a **space** of pages.'],
                 figure=F8.w08_card_netflix(), caption='The card, filled. Note the fifth row: the person has nothing to do when it is wrong — and that is by design.',
                 body_size=26,
                 notes='Two decisions stacked: which image of a film, and which rows in which order. Both learn from every visit. For the communication designers: the poster brief changed — you now design several images that each tell the truth about the film to a different person, and a model chooses. For the interaction designers: there is no home page; there is a procedure that makes one. The fifth row is telling: nothing to do when it is wrong, because being wrong is cheap here and every scroll teaches the model.'))

S.append(content('03 · DUOLINGO · 2023 – 2025', 'The lesson decides. Then the company decided.',
                 ['**Duolingo Max, 14 March 2023:** a GPT-4 tutor — Explain My Answer, and Roleplay conversations — as a subscription tier.',
                  '- **28 April 2025:** Luis von Ahn\'s "AI-first" memo to staff: the company would "gradually stop using contractors to do work that AI can handle". Two days later: 148 new courses, made with generative AI in about a year; the first 100 had taken about twelve.',
                  '- The backlash was public; von Ahn later clarified on LinkedIn that Duolingo was still hiring.',
                  'Read it on the card: the decision is the next exercise and the explanation. The fifth row is the one the memo changed.'],
                 figure=F8.w08_card_duolingo(), caption='The card, filled. Sources: Duolingo press releases, 14 March 2023 and 30 April 2025; TechCrunch, 30 April 2025.',
                 body_size=26,
                 notes='Duolingo is the honest case: a product that decides well — what to practise next, why you were wrong — and a company that decided to make the lessons themselves with models. The design question is the fifth row: a generated explanation that is wrong reads exactly like one that is right, and the person cannot tell. Who checks? The memo answered: fewer contractors. Do not moralise; ask the room who in their product plays that role, and whether the proposal names them.'))

S.append(content('03 · HUMANE AI PIN · 2023 – 2025', 'A model was the whole product. Then the servers went.',
                 ['Announced 9 November 2023 at US$699 plus US$24 a month; shipped April 2024. Founded by two former Apple employees: an interface designer and a software-engineering director. No screen: a laser projector on your palm, and a voice.',
                  '- The reviews, April 2024. The Verge: "not even close". Marques Brownlee: "The Worst Product I\'ve Ever Reviewed… For Now".',
                  '- February 2025: HP bought most of Humane\'s assets for US$116 million. On 28 February 2025 the Pins stopped connecting to the servers, and stopped working.',
                  'On the card: it decided everything for you, and when it was wrong you could only ask again.'],
                 figure=F8.w08_card_humane(), caption='The card, filled. Sources: TechCrunch, 18 February 2025; Tom\'s Guide and Android Authority review round-ups, April 2024.',
                 body_size=26,
                 notes='The most designed object in this chapter, and the least designed decision. Every request went to a model in the cloud: what you asked, what it saw, where you were. The fallback row is empty: no screen to check, no app to fall back to, and when the company sold its assets the object on your jacket became a badge. The lesson is not "AI wearables fail"; it is that the fifth row was never designed. Ask: what is the fallback of your product on the day the model is down?'))

S.append(content('03 · RABBIT R1 · 2024', 'It promised to act for you inside apps. It could not, reliably.',
                 ['Announced at CES on 9 January 2024, US$199, designed with Teenage Engineering; a first batch of 10,000 offered on the day.',
                  '- The promise was a "Large Action Model": you speak, it operates apps on your behalf — a ride, a song, a meal.',
                  '- Shipped in the spring; reviews called it unfinished. Brownlee: "barely reviewable". Android Authority ran its software on a phone: the R1 was, in practice, an Android app.',
                  'On the card: the decision was **how** to act for you inside someone else\'s product. Nobody had designed what happens when the action fails halfway.'],
                 figure=F8.w08_card_rabbit(), caption='The card, filled. Sources: TechRadar and Tom\'s Guide, January 2024; Gizmodo review, May 2024; Wikipedia, "Rabbit r1", for the later updates.',
                 body_size=26,
                 notes='Rabbit is the cousin: a beautiful orange object, and a decision the model could not actually make — operating apps built by other companies, who had not agreed. Two lessons for the proposal: an "agent" that acts for a person needs a fallback at every step, not one at the end; and if your product decides inside somebody else\'s product, your data row depends on their permission. Note the vocabulary: "Large Action Model" is a name, not a mechanism. Ask the room what it would have to be, in week-4 terms.'))

S.append(cards('03 · THE CAUTIONARY CASES', 'What Humane and Rabbit teach a design team.', [
    ('A MODEL, NOT A PRODUCT', 'The score is one part in five.',
     'Both objects had a state-of-the-art model in the cloud and nothing designed around it: no data of their own, no threshold anyone could set, no fallback. Week 1 said it; the market agreed.'),
    ('THE FALLBACK', 'Design row five first.',
     'Most of the time the model is slow, unsure or wrong. What the person sees then is the product they remember. A button (Spotify), a scroll (Netflix), or nothing (the Pin).'),
    ('LATENCY', 'Seconds are a broken promise.',
     'Reviewers of both objects waited, holding a device, for a cloud to answer. A decision that arrives after the moment has passed is a wrong decision, however good the score.'),
    ('THE SERVER', 'When it goes, the product goes.',
     'The Pin worked until 28 February 2025 and then did not. A product with a model inside is a service with a body. The body outlives the service; design for that day too.'),
], text_size=24, notes='Four lessons, all of them rows of the card. The ones your proposal is most likely to skip are the second and the fourth. Ask each team, later, for the day their server is off: what does the person hold? If the answer is "nothing", the concept needs a fallback before it needs a model.'))

S.append(question('multiple_choice', 'When the model is wrong, which product leaves the person with the least to do about it?', [
    'Spotify DJ: skip, or tap the button', 'Netflix: scroll past the poster', 'Duolingo: report the sentence, move on', 'Humane AI Pin: ask again, or nothing',
], eyebrow_text='03 · QUICK CHECK · MULTIPLE CHOICE',
    notes='D. The Pin had no screen, no app and no way to see what it had understood; the only move was to ask again, slower. A, B and C are all fallbacks somebody designed. Some will argue for C, because a wrong explanation is invisible: accept that as the better argument, and say the difference — Duolingo\'s person does not know it was wrong; the Pin\'s person knows and cannot act. Both are row-five failures of a different kind.'))

# ───────────────────────── 04 · the double diamond, with a model inside ─────────────────────────
S.append(section('04', 'The double diamond, with a model inside', 'discover · define · develop · deliver · Design Council, 2004', bg=ORANGES[0],
                 notes='Chapter four: the process you already know, with one thing added. The Design Council drew the double diamond in 2004 from how design teams actually worked. We put a model inside it and ask what the model does, or is, in each of the four phases.'))

S.append(sketch_slide('04 · LIVE · THE PROCESS', 'The model enters at define, and never leaves.',
                      live('w08-diamond', DIAMOND_CODE, 1400, 500, hint='move the mouse across the four phases'),
                      body=['Two diamonds: the problem, then the solution; diverge, then converge, twice. With a model inside, each phase has one extra question — and the model changes shape as it passes through.'],
                      caption='Design Council, 2004: discover, define, develop, deliver. The model is a question in the first diamond, a sentence at the pinch, a prototype in the third phase and a guarded, watched thing in the fourth.',
                      notes='Move across. Discover: no model; the question is what data exists about this person, and what you would have to take. Define: the model is a sentence, and the sentence is the decision — for this person, at this moment, it decides X — with the score, the threshold and the fallback named. Develop: rule or model, and before either exists, a wizard. Deliver: guardrails and monitoring, because the model keeps changing after launch. The proposal due this week is the define pinch: one page, one sentence, the data.'))

S.append(cards('04 · WHAT THE MODEL DOES IN EACH PHASE', 'Four phases, four jobs.', [
    ('DISCOVER', 'What data exists?',
     'Before an idea: what is already known about this person, by whom, with what permission. A product can only decide from data it has. Most concepts die here, quietly, in week 9.'),
    ('DEFINE', 'The decision, in one sentence.',
     '"For this person, at this moment, it decides X." Then the score, the threshold and the fallback, named. This is the group proposal: one page, due before week 9.'),
    ('DEVELOP', 'Rule or model. Wizard first.',
     'Write the rule if you can say it; show examples if you cannot. Before either exists, one of you plays the model behind a curtain and you test the decision on a stranger. Prototype v1, week 10.'),
    ('DELIVER', 'Guardrails and monitoring.',
     'What it may never decide; when a human steps in; what you watch after launch: the two errors, the edges, the drift. The mediation brief, week 11; the poster, week 13.'),
], text_size=22, notes='The four cards are the four deliverables of the project, in order. Say that plainly: proposal, concept board and bias register, prototype, brief and poster. The rubric rewards the second and fourth phases most — research and the ethical account — and teams tend to spend their time in the third. The wizard is how you spend little time there and learn a lot.'))

S.append(figure_slide('04 · DEVELOP · THE WIZARD', 'Test the decision before the model exists.', F8.w08_wizard(),
                      body=['A person uses what looks like the product. Behind a curtain, a teammate plays the model: reads the rule off a card, looks up the person\'s row in a spreadsheet, types the decision. In an afternoon you learn whether the decision is wanted, how fast it must arrive, and what the person does when it is wrong.'],
                      caption='Gould, Conti & Hovanyecz, 1983: IBM\'s "listening typewriter" took dictation; the speech recogniser was a typist in the next room. Kelley, 1984, gave the method its name.',
                      notes='The oldest trick in interaction design and the best one for this project. IBM wanted to know whether people would dictate letters to a machine before such a machine existed; a typist behind a wall was the machine. The question was whether an imperfect listening typewriter would still be worth using; the paper found that some versions were, even at first use. For your teams: one person is the wizard, one the interface, one observes, one is the stranger. The rule on the card is machine A played by a human; a spreadsheet is the data. What you cannot fill in the spreadsheet is the data you do not have — the last question of the activity.'))

S.append(cards('04 · DEVELOP · RULE OR MODEL', 'Write the rule if you can. Show examples if you must.', [
    ('WRITE THE RULE', 'Machine A, if you can say it.',
     '"Show the reminder if they opened the app twice this week." Exact, explainable, cheap, and the wizard can play it from a card. If the decision fits in a sentence with numbers, it is a rule. Most decisions in most products are.'),
    ('SHOW THE EXAMPLES', 'Machine B, if you cannot.',
     '"Show the poster this person is most likely to click." Nobody can write that rule; a model learns it from clicks. Fluent, fuzzy, needs data you may not have, and cannot say why. Only here does the grain matter.'),
    ('RULES AROUND A MODEL', 'Machine A guarding machine B.',
     'The Writers\' Room around the DJ. A threshold, a list of what it may never say, a human for the risky cases. Week 1\'s designer as guardrail-setter: this is the deliver phase, and the mediation brief.'),
], text_size=22, notes='The spine of the course, applied. Ask each decision in the room: can you say it as a sentence with numbers? Then it is a rule, and you do not need a model; say so in the proposal, it is a strength. If not, it is a model, and the proposal must say where the examples come from. Almost every shipped product is the third card: a model with rules around it.'))

S.append(question('multiple_choice', '"What data already exists about this person?" belongs to which phase?', [
    'Discover', 'Define', 'Develop', 'Deliver',
], eyebrow_text='04 · QUICK CHECK · MULTIPLE CHOICE',
    notes='A. It is the first question, before any idea, because a product can only decide from data it has. Teams that ask it in develop find out in week 10 that the data does not exist. If the room splits between A and B, that is fine: the sentence in define depends on the answer in discover — which is why the ladder later puts the person and the moment before the decision, and the data right after it.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · A MODEL AS A MATERIAL · THEN YOUR TEAM, FOR SIX WEEKS', size=120, bg=PAPER,
                   notes='1:14. Back at 1:29. Sit with your team when you come back: the second half is the team\'s. Paper and pens are on the tables; the TAs are handing out one A4 sheet per team for the card.'))

# ───────────────────────── 05 · a model as a material ─────────────────────────
S.append(section('05', 'A model as a material', 'grain · edges · appetite · drift', bg=INK,
                 notes='Chapter five, short: the metaphor that names the course. Wood has a grain, and so does a model. Four properties every team should be able to say about the model in its product.'))

S.append(statement('A material with a grain.', eyebrow_text='05 · HOLMQUIST · INTERACTIONS · 2017 · "INTELLIGENCE ON TAP"', size=140,
                   notes='Lars Erik Holmquist, Interactions, 2017: AI as a design material, available on tap like electricity, with its own properties and limits. The same year Dove, Halskov, Forlizzi and Zimmerman asked designers why they found machine learning so hard to design with; Yang and colleagues in 2020 gave the two reasons: you do not know what it can do, and its output is not one thing. We say it with a woodworker\'s word: grain. Cut with it and it is easy; cut across it and it splits.'))

S.append(figure_slide('05 · THE GRAIN', 'Fluent in the middle. Wrong at the edges. And it moves.', F8.w08_grain(),
                      body=['Week 1\'s typicality, drawn as a material. A model is fluent where its examples were dense and wrong where they ran out — and it sounds exactly as sure in both places. Retrain it and the grain moves; the threshold you set in October does not.'],
                      caption='Left: the examples it learned from. Right: the same product after retraining — the shape moved, the line did not, and the people it now decides for are not the people you tested it on.',
                      notes='Two panels. Left: the middle is the chair with four legs, the edge is the swing; the model is confident everywhere, right only in the middle. Right: the same model in December, retrained on new data — more of one kind of person, fewer of another. The grain moved. Your threshold, the number from the sketch, stayed. So the two errors changed without anyone touching the product. Ask: which of the five products this morning retrains? All three that survive. Week 9 asks who is missing from the examples; this slide says the examples are also moving.'))

S.append(cards('05 · FOUR PROPERTIES', 'Grain, edges, appetite, drift.', [
    ('GRAIN', 'It is best in the middle of its examples.',
     'Typicality, from week 1: fluent and right where the examples were dense. Work with the grain: put the decision where the data is thick, and say so in the proposal.'),
    ('EDGES', 'It fails where the examples ran out — confidently.',
     'The swing, the stump, the person unlike the training set. A model does not know it is at an edge. Guardrails are the designer\'s way of knowing for it: what it may never decide, and for whom a human decides instead.'),
    ('APPETITE', 'It needs data, and keeps needing it.',
     'Yours, theirs, given, taken, inferred. A product that decides from examples is a product that collects. What it collects, and whether it asked, is next week — and one line of your proposal.'),
    ('DRIFT', 'It changes with retraining.',
     'The product you tested in October is not the product that ships in December. Dove et al. 2017, Yang et al. 2020: probabilistic, and it keeps changing. Monitoring is a design deliverable, not an engineering one.'),
], text_size=22, notes='Four words to carry into the project. Grain and edges are the week-1 scale, now about a product. Appetite is next week. Drift is the one nobody plans for: the model your poster describes in week 13 will not be the model in the product in March. Ask each team later which of the four their concept is most exposed to; the bias register in week 9 starts there.'))

S.append(content('05 · THE GRAIN, SEEN IN WEEK 1', 'Four chairs, one grain.',
                 ['One prompt, four seeds: four legs, a back, wood, a bit of mid-century, every time. The grain of the examples, made visible.',
                  '- A product on this model decides "chair" well for dining rooms and badly for beanbags, hammocks and the floor.',
                  '- Ask for the edge and you get the middle. The model cannot tell you it is at an edge; it sounds the same.',
                  'Whose chairs? Whose cups, from week 1? Next week.'],
                 images=CHAIRS, caption='Week 1: "a chair, studio product photograph, plain white background" — one model, four seeds, September 2026.',
                 body_size=28,
                 notes='The chairs from week 1 are worth a second look now that the word is material. Nobody wrote "four legs"; the examples did. The design point for the proposal: the examples your product decides from have a middle that is somebody\'s — the dataset\'s, not Hong Kong\'s — and the proposal should say whose. Next week does this properly with Coded Bias.'))

S.append(question('multiple_choice', 'Your team ships the model in October. It is retrained in December. What must you check again?', [
    'Nothing: a retrained model is a better model', 'The threshold, and the two errors, on the people it now decides for', 'The logo and the colours', 'Only the loading time',
], eyebrow_text='05 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. The grain moved; the line did not; the two errors changed for people who never saw the October version. "Better on average" can be worse at an edge. This is what monitoring means in the deliver phase, and it is one line in the mediation brief: what we watch, how often, and what we do when it moves.'))

# ───────────────────────── 06 · working as a team ─────────────────────────
S.append(section('06', 'Working as a team', 'a sprint · a backlog · a stand-up · a branch · five jobs', bg=ORANGES[0],
                 notes='Chapter six: six weeks, four or five people, one product. Two ways software teams stopped losing work and losing each other — Scrum and versioning — translated for a design team. Ten percent of the project mark is the process; this chapter is how to earn it as a side effect.'))

S.append(cards('06 · SCRUM', 'A sprint, a backlog, a stand-up.', [
    ('THE SPRINT', 'A fixed box of time with one goal.',
     'The Scrum Guide (Schwaber & Sutherland, 2020): one month or less. Ours is a week: class to class. One goal per sprint, one thing that exists at the end that did not at the start. The word comes from rugby, via a 1986 Harvard Business Review article on product teams that move as one.'),
    ('THE BACKLOG', 'One ordered list. The only source of work.',
     'Everything the product needs, in order, in one place; the top item is this week\'s. Nothing is work unless it is on the list. A shared document is enough. The product owner keeps it — one person, rotating or not.'),
    ('THE STAND-UP', 'Fifteen minutes. Standing. Three questions.',
     'At your table before every class, from week 9, with the TAs in the room: what did I do since last class, what will I do before the next, what is in my way. The Guide says every working day; we say every class and one message in between. Standing keeps it short.'),
], text_size=22, notes='Three words, no ceremony. Scrum has more parts — a review, a retrospective, a Scrum Master — and you do not need them; you need a box of time, a list, and a fifteen-minute meeting nobody can skip. The TAs run the review: thirty minutes after every class, show what exists, not what you plan — the first one is today. The stand-up is the team\'s own, in the half hour before class, when the TAs are already in the room. Say the rule about the backlog twice: nothing is work unless it is on the list. It saves teams from the member who "was working on the logo".'))

S.append(figure_slide('06 · THE SEMESTER AS SPRINTS', 'One sprint per week. One deliverable per sprint.', F8.w08_sprints(),
                      body=['Six sprints from today to the fair; the backlog on the left is the syllabus in order. From week 9 every sprint opens with the stand-up, at your table before class; every review is with the TAs, thirty minutes after class, showing the thing that exists now. The first review is today.'],
                      caption='Week 8 the proposal · 9 the concept board and the bias register · 10 prototype v1 · 11 the draft poster and the mediation brief · 12 the final poster and the video · 13 the fair, then the final quiz.',
                      notes='The syllabus, redrawn as a backlog. The point of drawing it: every week has one deliverable and it is small; a team that does one thing a week finishes with a poster that has six layers of evidence. A team that starts the poster in week 12 finishes with a poster. The stand-up boxes are literal: fifteen minutes at your table in the half hour before every class from week 9, standing, with the TAs in the room; week 10 opens with one in class so that every team has seen the format once. The review box on week 8 is today: thirty minutes after class, with the TAs.'))

S.append(figure_slide('06 · VERSIONS', 'A repository is a history you can branch.', F8.w08_git(),
                      body=['Git, 2005: a folder that remembers every saved state, with a message; a branch to try an idea without breaking the main line; a merge to bring it back. Figma, 2021: the same four words for design files. A commit is a decision with a date and a name on it — the process documentation the rubric asks for, made as a side effect.'],
                      caption='Git: Linus Torvalds, April 2005. Figma branching: announced at Config, April 2021, in beta on the Organization plan. No branching where you are? Name the versions: v1, v2, v3, one line each.',
                      notes='You do not need Git; you need the idea. Main is the version you would show; every idea is a branch; a branch you abandon is kept, because the rubric grades process and an abandoned branch with a reason is evidence. The four words are in Figma for teams with the Organization plan, and in every tool as "save as v3" with a line about what changed. The one rule: nobody works on main. Ask: who in the room has lost a file to a teammate\'s save? Everyone. That is what this fixes.'))

S.append(content('06 · THE PROCESS IS GRADED', 'Ten percent is the process. Keep the evidence.',
                 ['The rubric: "team collaboration and process documentation, 10 %: strong shared effort; transparent, well-documented process; roles clear." Evidence, not adjectives:',
                  '- **The backlog**, with dates: what was on top each week.',
                  '- **The versions**: v1, v2, v3 of the card, the board, the poster — with one line each on what changed and why.',
                  '- **The wizard logs**: who you tested, what they did when it was wrong.',
                  '- **The stand-up notes**: three questions, five names, six weeks.',
                  'Each member\'s contribution must show. A vanished member shows too; tell the team early, tell Amber before it costs you.'],
                 body_size=30,
                 notes='The 10 % is the easiest in the course to get and the easiest to lose. The scribe keeps four things and they cost nothing if you keep them as you go; they cost a weekend if you reconstruct them in week 12. The last line is the one to say slowly: PolyU rules require each member\'s contribution to show; a team with a missing member should talk to Amber in week 9, not at the fair.'))

S.append(cards('06 · ROLES', 'Five jobs in a team of four or five.', [
    ('THE OWNER', 'Keeps the decision and the backlog.',
     'Owns the sentence: for this person, at this moment, it decides X. Says no to features. Rotate it if you like; never leave it empty.'),
    ('THE RESEARCHER', 'Owns the data, the bias, the sources.',
     'Discover and the bias register. Finds what data exists and who is missing from it. Feeds the 30 % of the mark that is research.'),
    ('THE WIZARD', 'Owns the prototype and the test.',
     'Plays the model behind the curtain; runs the test on strangers; writes down what the person did when it was wrong.'),
    ('THE MAKER', 'Owns the poster and the video.',
     'The A0 and the three to five minutes. Starts in week 9 with the concept board, not in week 12 with a blank page.'),
    ('THE SCRIBE', 'Owns the record.',
     'The stand-up notes, the versions, the wizard logs, who did what. The 10 % for process — and the answer when a member vanishes.'),
], text_size=20, head_size=26, sub='Sixty seconds, now, at your table: say who is who. The scribe writes it down; the proposal names them.', notes='Five jobs, four or five people: with four, the scribe is a hat someone else wears. These are not the poster credits; they are who is accountable for which row of the card and which deliverable. Teams that skip the owner drift; teams that skip the scribe cannot prove who worked. Sixty seconds at the table now: say who is who, the scribe writes it down, and the proposal names them. The chapter ends when every team has five names on paper.'))

# ───────────────────────── 07 · the workshop: the brainstorm ladder ─────────────────────────
S.append(section('07', 'The brainstorm ladder', 'the person · the moment · the decision · the data · the failure', bg=PAPER,
                 notes='Chapter seven, short: the tool for the next forty minutes. A ladder with five rungs, climbed in order, and the group brief it leads to.'))

S.append(figure_slide('07 · THE LADDER', 'Five rungs, in this order.', F8.w08_ladder(),
                      body=['An idea is one line that climbs all five: a person, a moment, a decision, the data, the failure. Start with the person, never with the technology; an idea that skips a rung is a feature, not a product. The example is made up; yours will be too, until rung four makes you check.'],
                      caption='One line per idea. The rung most teams skip is the fourth — does the data exist? — and it is the whole of the proposal.',
                      notes='Climb it once aloud with the example: a night-shift nurse; the minibus home at 7:40; it decides what she eats tonight; her roster, what she bought, what she cooked before; the day it is wrong it suggests the dish she just had at work and she orders out. Ninety seconds, five rungs, one line. Ask the room to climb it with a different person — a taxi driver, a first-year — and notice that the decision changes as soon as the moment does. Ten of these in five minutes is the first round.'))

S.append(content('07 · THE GROUP PROPOSAL', 'One page, before week 9.',
                 ['One page, one per team, on Blackboard:',
                  '- **The decision**, for whom, at what moment — one sentence.',
                  '- **The data**: have / do not have / would have to ask for.',
                  '- **Rule or model**, and why. A rule is a fine answer.',
                  '- **If it is wrong:** what the person sees; the fallback.',
                  '- The team and the five roles.',
                  'Amber reads every one before week 9; week 9 opens with them.'],
                 figure=F8.w08_card_blank(), caption='The decision card is the proposal, in your handwriting. Type it up, add the two lines about rule-or-model and the team, upload.',
                 body_size=28,
                 notes='Say the deadline twice and check Blackboard has it. The proposal is deliberately small: a page, five rows, and it is the define pinch of the diamond. The bit teams under-write is the data row: "user data" is not an answer; "her shift roster, which the hospital app has and we do not" is. The card today is the draft; the upload adds two lines and the names.'))

S.append(cards('07 · HOW TO BRAINSTORM', 'Four rules for the next five minutes.', [
    ('QUANTITY', 'Ten, not one.',
     'The first three ideas are everybody\'s. The good one is usually seventh. Write fast, write badly, keep the pen moving; the choosing is round two.'),
    ('NO JUDGEMENT YET', 'Do not say "but".',
     'Not "that exists", not "the data is impossible". Rung four is where that is checked, in the next round, with a test, not a reflex.'),
    ('ONE LINE PER IDEA', 'Climb all five rungs.',
     'Person, moment, decision, data, failure. If a line stops at the decision it is a feature; add the person and it becomes a product.'),
    ('BUILD ON THE LAST', 'Change one rung.',
     'Same person, new moment. Same moment, new decision. The chairs from week 1: one rule, one number changed. Ideas are parametric too.'),
], text_size=22, notes='Standard brainstorm hygiene, with the ladder as the format. The fourth card is the one that produces ten quickly: change one rung and you have a new line. Nicolò keeps time from the next slide; the other three walk and stop anyone who is debating instead of writing.'))

# ───────────────────────── 08 · activity: ten ideas, one decision ─────────────────────────
S.append(section('08', 'Ten ideas. One decision.', '35 minutes · your team · paper · one phone per team', bg=YELLOWS[0],
                 notes='The activity. Four rounds at the team table, all on paper: ten ideas, one pick, one decision card, then a gallery vote and one last question. What goes into ClassPoint is a pulse, a photo of the card, a vote and one short answer. Nicolò keeps time with the slide timers; Amber, WU Zhao and MA Jie walk. One phone per team for the upload.'))

S.append(activity('1 — TEAMS · TEN IDEAS', 5, 'Ten ideas in five minutes.',
                  ['One sheet, one pen each, the ladder on the right. **Ten lines**, each climbing all five rungs.',
                   'No debating. If someone says "but", the next line is theirs.',
                   'Change one rung of the last line to make the next.'],
                  panel=LADDER_PANEL, panel_size=20, bg=YELLOWS[0],
                  notes='Five minutes, loud. Watch for teams writing technologies ("an AI that…") and send them back to rung one: who. Watch for one person writing and four watching: pens for everyone, lines in turn. A team with three lines at two minutes gets a TA who reads the example aloud and changes a rung.'))

S.append(question('multiple_choice', 'How many ideas did your team write?', [
    'Fewer than five', 'Five to nine', 'Ten', 'More than ten',
], eyebrow_text='08 · PULSE · MULTIPLE CHOICE',
    notes='Pulse, one minute, one answer per person is fine. No correct answer; show the split. Teams at A get thirty extra seconds and a TA. Then the pick.'))

S.append(activity('2 — TEAMS · PICK ONE', 3, 'Pick the one you can build.',
                  ['Read the ten aloud. Apply the three tests on the right to each; a line that fails one is out.',
                   'If two survive, take the one with the clearest **sentence at rung three**.',
                   'Circle it. That is your product for the next six weeks — until the wizard test says otherwise.'],
                  panel=PICK_PANEL, panel_size=20, bg=YELLOWS[1],
                  notes='Three minutes and a hard stop. The tests are discover, deliver and develop in disguise: does the data exist, is the failure survivable, can you wizard it. Teams that cannot choose get the tie-break; teams that choose in ten seconds get asked test A out loud. This is a pick, not a marriage: week 10 can change it.'))

S.append(activity('3 — TEAMS · THE CARD', 10, 'Fill the decision card.',
                  ['One A4, landscape, big letters. The five rows on the right, in order; **the decision is one sentence**.',
                   'The data row has two columns: **have** and **do not have**. Be honest in the second.',
                   'Row five: the day it is wrong, what does she see, what can she do? If the answer is "nothing", write "nothing".'],
                  panel=CARD_PANEL, panel_size=20, bg=YELLOWS[2],
                  notes='Ten minutes. This is the proposal in draft. The TAs read over shoulders for two things: a decision that is really a feature ("it has an AI chat") and a data row that says "user data". Both get one question: which person, which moment, which data, from where. Big letters: the photo goes on the wall next.'))

S.append(question('image_upload', 'One per team: the decision card.',
                  hint='One photo, one per team. Caption: the team number, then the decision sentence, word for word.',
                  eyebrow_text='08 · CAPTURE · IMAGE UPLOAD · ONE PER TEAM',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='ClassPoint image upload, one phone per team, about twenty-five images, caption required: team number and the sentence. Put the wall on screen. While it fills, read three captions aloud without the card and ask the room what the product is; where the room cannot say, the sentence is not finished. Download the submissions after class: Amber reads them against the proposals.'))

S.append(activity('4 — THE GALLERY', 5, 'Read four cards. Argue.',
                  ['Four cards from the wall go on screen, one at a time, labelled **A to D** — team numbers, no names.',
                   'For each, the three questions on the right, asked of the room.',
                   'Then the vote: **which product would you sign up for?** Not the best drawing — the one you would let decide for you.'],
                  panel=GALLERY_PANEL, panel_size=20, bg=YELLOWS[0],
                  notes='Five minutes, Gio at the wall. Pick four cards that differ: one with a crisp sentence, one with a data row that says "do not have" honestly, one that is a feature dressed as a product, one with an empty row five. Do not say which is which; ask the room the three questions for each. The vote follows. Keep it kind: every card is a draft, and the team whose card is a feature gets the most useful five minutes of the day.'))

S.append(question('multiple_choice', 'Gallery vote: which product would you let decide for you?', [
    'Card A', 'Card B', 'Card C', 'Card D',
], eyebrow_text='08 · GALLERY VOTE · MULTIPLE CHOICE · BY CARD',
    notes='Two minutes, everyone votes, teams may vote for themselves. No correct answer: the room decides, and the winning team gets a participation star and thirty seconds to say what its person does on the wrong day. Note the split for the awards list. Say the team numbers of all four aloud; no names on screen.'))

S.append(question('short_answer', 'The data your product needs and does not have.',
                  hint='One line per team, from the scribe: the team number, then the data. "Team 12: her shift roster — the hospital app has it; we do not."',
                  eyebrow_text='08 · LAST QUESTION · SHORT ANSWER · ONE PER TEAM',
                  notes='Three minutes, scribes only. This is the discover question, answered honestly, and it is the seed of next week: every line here is either data you must ask a person for — consent — or data somebody else holds — a platform, a hospital, a school. Read five aloud and sort them into "ask" and "take". Keep the export: week 9 opens with it, and the bias register starts from it.'))

S.append(content('08 · WHAT JUST HAPPENED', 'Every product here is a mediation.',
                 ['Twenty-five cards, twenty-five decisions, each made for a stranger at a moment you chose. The loop from week 7: a person, their data, a model, a decision, and what it does to them.',
                  'Verbeek, week 1: designing things is designing human existence. Today you designed what a person sees at 7:40 on a minibus, and what they do not see. The threshold you will set decides how often you are wrong, and in which direction.',
                  'The card is the proposal. The data you do not have is next week. The wrong day is the week after. The whole of module 3 is the fifth row.',
                  '**The model will make the score. You decided what it decides, for whom, from what, and what happens when it is wrong. That was the design.**'],
                 body_size=30,
                 notes='Mirror of the whole class. Say the loop slowly: person, data, model, decision, and back to the person. Then the last line, which is the week-1 and week-2 last lines with the verb changed: the machine decides, you designed the deciding. Point at the three homework items and let them go; the TAs stay thirty minutes — the first review — and the first stand-up is at your table before next week\'s class.'))

S.append(cards('08 · BEFORE WEEK 9', 'The proposal, the film, the stand-up.', [
    ('THE PROPOSAL', 'One page, on Blackboard, one per team.',
     'The card typed up: the decision, for whom, the data (have / do not have), rule or model and why, the wrong day, the team and the five roles. Before the week-9 class. Amber reads every one; week 9 opens with them.'),
    ('CODED BIAS', 'Watch it before week 9.',
     'Shalini Kantayya, 2020; premiered at Sundance. Joy Buolamwini finds that face recognition fails on faces unlike its examples — the edge of the grain, with people at it. Ninety minutes. Next week starts from it.'),
    ('THE STAND-UP', 'Fifteen minutes, at your table, before class.',
     'From week 9, in the half hour before every class: three questions, standing, the TAs in the room. Bring the backlog with one item on top. The review with the TAs is thirty minutes after class: show the thing, not the plan.'),
], notes='Three things, one deadline. The proposal is the first sprint\'s increment; small on purpose. Coded Bias is the reading for next week and the quiz draws on it. The stand-up is before next week\'s class, not in it: the TAs are in the room from half an hour before, and a team that arrives at 0:00 has missed its own meeting.'))

S.append(end('See you next week. Data, bias and privacy.',
             'Upload the proposal. Watch Coded Bias. Bring your backlog.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: how data powers adaptive systems, four kinds of bias, and privacy — consent, minimisation, anonymisation — with your own decision cards as the cases. Homework in one line: the proposal on Blackboard, Coded Bias, and the backlog with one item on top. The TAs stay for 30 minutes: the first review.'))

DECK = dict(title='SD2112 · AI in Design · Week 08', slides=finalize(S, FOOTER), pdf='SD2112-week08.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week08', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 5 September 2026)
# Spotify DJ launch: https://newsroom.spotify.com/2023-02-22/spotify-debuts-a-new-ai-dj-right-in-your-pocket/
# Spotify DJ, how it works (Sonantic, Xavier Jernigan, the Writers' Room): https://newsroom.spotify.com/2023-03-08/spotify-new-personalized-ai-dj-how-it-works/
# Spotify DJ, 50 markets: https://newsroom.spotify.com/2023-08-08/ai-dj-expanded-new-markets-how-to-use-feature/
# Netflix artwork personalization (December 2017; contextual bandits): https://netflixtechblog.com/artwork-personalization-c589f074ad76
#   (the post itself was not reachable from the build environment; the mechanism and date were confirmed via
#   https://www.geteppo.com/blog/netflix-lyft-yahoo-contextual-bandits and
#   https://www.reforge.com/blog/brief-netflix-artwork-personalization-through-multi-armed-bandit-testing)
# Netflix, Learning a Personalized Homepage (April 2015): http://techblog.netflix.com/2015/04/learning-personalized-homepage.html
# Duolingo Max (14 March 2023, GPT-4, Explain My Answer, Roleplay): https://investors.duolingo.com/news-releases/news-release-details/duolingo-max-shows-future-ai-education
#   and https://techcrunch.com/2023/03/14/duolingo-launches-new-subscription-tier-with-access-to-ai-tutor-powered-by-gpt-4
# Duolingo "AI-first" memo (28 April 2025) and the 148 courses (30 April 2025): https://techcrunch.com/2025/04/30/duolingo-launches-148-courses-created-with-ai-after-sharing-plans-to-replace-contractors-with-ai
# Duolingo's clarification: https://www.entrepreneur.com/business-news/duolingo-ceo-clarifies-ai-stance-after-backlash-read-memo/492141
# Humane AI Pin, HP asset purchase (US$116M) and shutdown (28 February 2025): https://techcrunch.com/2025/02/18/humanes-ai-pin-is-dead-as-hp-buys-startups-assets-for-116m
# Humane timeline (announced 9 November 2023, US$699 + US$24/month, shipped April 2024): https://en.wikipedia.org/wiki/Humane_Inc.
# Humane reviews (The Verge "not even close"; Brownlee "The Worst Product I've Ever Reviewed… For Now"): https://www.tomsguide.com/ai/humane-ai-pin-review-roundup-this-is-a-disaster
#   and https://www.androidauthority.com/humane-ai-pin-reviews-3433607/
# Rabbit R1 (CES 9 January 2024, US$199, Teenage Engineering, Large Action Model, "barely reviewable", the Android app finding): https://en.wikipedia.org/wiki/Rabbit_r1
#   https://www.techradar.com/computing/artificial-intelligence/what-is-the-rabbit-r1 · https://www.tomsguide.com/features/rabbits-r1-ai-device-took-ces-2024-by-storm-what-is-it-and-why-might-you-want-one
#   https://gizmodo.com/rabbit-r1-review-ai-companion-performance-1851452097
# Design Council, history of the Double Diamond (2003–2004; shared from 2004): https://www.designcouncil.org.uk/resources/the-double-diamond/history-of-the-double-diamond/
# Wizard of Oz: Gould, Conti & Hovanyecz 1983 (the listening typewriter); Kelley 1984 named the method:
#   https://www.usabilitybok.org/wizard-of-oz/ · https://ieeexplore.ieee.org/document/6276976
# Holmquist, L. E. (2017). Intelligence on tap: artificial intelligence as a new design material. Interactions 24(4): https://dl.acm.org/doi/10.1145/3085571
# Dove, Halskov, Forlizzi & Zimmerman (2017). UX design innovation: challenges for working with machine learning as a design material. CHI 2017: https://dblp.org/rec/conf/chi/DoveHFZ17.html
# Yang, Steinfeld, Rosé & Zimmerman (2020). Re-examining whether, why, and how human-AI interaction is uniquely difficult to design. CHI 2020: https://dl.acm.org/doi/10.1145/3313831.3376301
# The Scrum Guide (Schwaber & Sutherland, 2020): https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf
# Takeuchi & Nonaka (1986), The New New Product Development Game, HBR (paywalled; the rugby-versus-relay framing via https://www.scrummanager.com/bok/index.php/New_New_Product_Development_Game)
# Git's first commit, 7 April 2005: https://github.blog/open-source/git/git-turns-20-a-qa-with-linus-torvalds/
# Figma branching (Config, April 2021, beta, Organization plan): https://www.figma.com/blog/introducing-branching-space-to-iterate-and-explore-freely/
# Coded Bias (Shalini Kantayya, 2020, Sundance): https://en.wikipedia.org/wiki/Coded_Bias · https://www.pbs.org/independentlens/documentaries/coded-bias/
# Consulted 6 September 2026, after the review:
# Humane's founders (Chaudhri: Apple's interface designer; Bongiorno: Apple director of software engineering):
#   https://www.fastcompany.com/90555755/humane-imran-chaudhri-bethany-bongiorno-funding
#   https://www.inverse.com/tech/humane-projection-device-ex-apple-employees-artificial-intelligence
#   https://techcrunch.com/2021/09/01/humane-a-stealthy-hardware-and-software-startup-co-founded-by-an-ex-apple-designer-and-engineer-raises-100m/
# Gould, Conti & Hovanyecz (1983), CACM 26(4): the aim was to find out whether an imperfect listening typewriter would be useful:
#   https://dl.acm.org/doi/abs/10.1145/2163.358100 · https://research.ibm.com/publications/composing-letters-with-a-simulated-listening-typewriter--1
