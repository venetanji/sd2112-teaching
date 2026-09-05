"""
SD2112 · Artificial Intelligence in Design · Week 11 — the slide spec.

    python deck/week11.py            # builds _site/week11/ (html deck + pdf), export/week11*.pptx, export/preview/
    python deck/week11.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Curators of outputs and datasets — module 4 opens, the designer's turn. Who made Edmond de Belamy
(six hands, one signature); curating outputs (the model makes 64, you pick one: the pick is the
authorship, and gatekeeping is the second half of the job); curating datasets (a style is twenty
images; what you put in is what comes out; LAION-5B, opt-outs, consent); authorship and ownership
(Thaler, Zarya, the Copyright Office's 2025 report, Allen's 624 prompts, Hong Kong's s.11(3);
Google Books, Bartz v. Anthropic, Kadrey v. Meta, Getty v. Stability; what transformative means
for a designer); the poster lab (the A0's four zones, the video's six shots, the mediation brief);
and the activity: curate three of sixty-four, assemble a twelve-image dataset of a style you own,
critique a draft poster. Two live sketches (w11-curate, w11-dataset); drawn figures in
tools/figures_week11.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week11 as F                            # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, sketch_slide, code_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(11)
CHAIRS = [f'ai-chair-{i}.jpg' for i in range(1, 5)]   # week 1: one prompt, four seeds (deck/assets)

# ───────────────────────── live sketches (html deck) ─────────────────────────
# (a) curate: one rule, sixty-four outputs; the curator picks three and says why
CURATE_JS = """// One rule, sixty-four outputs. Every tile is a k x k grid of cells; each cell is drawn with
// probability `density`, with one motif, one rotation, one weight, one colour. The model makes
// all 64 in a blink. The curator picks three, and says why. Click = choose (up to 3) · N = 64 new.
const S = 80, G = 6, X0 = 20, Y0 = 20, RX = 730;   // the grid, and the right column
const COLORS = ['#000B1C', '#ED6D24', '#64C2C3'], MOTIF = ['lines', 'arcs', 'dots'], NAME = ['ink', 'orange', 'teal'];
let base = 11, tiles = [], chosen = [];

function setup() {
  createCanvas(1100, 760); textFont('JetBrains Mono');
  generate(); chosen = [5, 27, 50];                       // three already picked, so the still reads
}

function generate() {                                     // the rule, with seeded chance
  randomSeed(base); tiles = []; chosen = [];
  for (let i = 0; i < 64; i++) tiles.push({ k: random([2, 3, 4, 5]), density: random(0.35, 1), motif: floor(random(3)),
    rot: floor(random(4)), weight: random([1, 2, 3]), color: floor(random(3)), seed: base * 64 + i });
}

function tile(t, x, y, s, frame) {                        // one execution of the rule
  randomSeed(t.seed);
  stroke(frame); strokeWeight(frame == '#ED6D24' ? 4 : 1); fill(255); rect(x, y, s, s);
  let cell = s / t.k, w = max(1, t.weight * s / 80);
  for (let r = 0; r < t.k; r++) for (let c = 0; c < t.k; c++) {
    if (random() > t.density) continue;                    // the die: drawn, or left empty
    let cx = x + c * cell, cy = y + r * cell, d = (t.rot + r + c) % 4;
    stroke(COLORS[t.color]); strokeWeight(w); noFill();
    if (t.motif == 0) { if (d % 2 == 0) line(cx + 2, cy + 2, cx + cell - 2, cy + cell - 2); else line(cx + cell - 2, cy + 2, cx + 2, cy + cell - 2); }
    else if (t.motif == 1) { let px = [cx, cx + cell, cx + cell, cx][d], py = [cy, cy, cy + cell, cy + cell][d]; arc(px, py, 2 * cell - 4, 2 * cell - 4, d * HALF_PI, d * HALF_PI + HALF_PI); }
    else { noStroke(); fill(COLORS[t.color]); circle(cx + cell / 2, cy + cell / 2, cell * (0.24 + 0.16 * t.weight)); }
  }
}

function label(t) { return t.k + 'x' + t.k + ' · ' + MOTIF[t.motif] + ' · density ' + nf(t.density, 1, 2) + '\\nrot ' + t.rot * 90 + '° · ' + t.weight + ' px · ' + NAME[t.color]; }

function draw() {
  background(255);
  let hover = -1;
  for (let i = 0; i < 64; i++) {                           // the sixty-four
    let x = X0 + (i % 8) * (S + G), y = Y0 + floor(i / 8) * (S + G);
    if (mouseX >= x && mouseX < x + S && mouseY >= y && mouseY < y + S) hover = i;
    tile(tiles[i], x, y, S, chosen.includes(i) ? '#ED6D24' : hover == i ? '#5C6470' : '#E1E1DE');
  }
  let rx = RX;                                             // the right column: the count, the hovered, the chosen
  noStroke(); textAlign(LEFT, BASELINE);
  fill(0); textSize(18); text('CURATE', rx, 40);
  fill('#ED6D24'); textSize(22); text(chosen.length + ' of 64 chosen', rx, 74);
  fill('#5C6470'); textSize(16); text((64 - chosen.length) + ' discarded', rx, 98);
  if (hover >= 0) { tile(tiles[hover], rx, 122, 150, '#5C6470'); noStroke(); fill(0); textSize(14); text('#' + (hover + 1) + '  ' + label(tiles[hover]), rx, 298); }
  else { fill('#5C6470'); textSize(14); text('hover a tile: its numbers', rx, 150); }
  for (let j = 0; j < chosen.length; j++) {
    let t = tiles[chosen[j]], y = 350 + j * 118;
    tile(t, rx, y, 88, '#ED6D24'); noStroke();
    fill(0); textSize(14); text('#' + (chosen[j] + 1), rx + 104, y + 20);
    fill('#5C6470'); text(label(t), rx + 104, y + 46);
  }
  noStroke(); fill('#5C6470'); textSize(14); text('click = choose, up to 3 · N = 64 new', rx, 740);
}

function mousePressed() {                                  // choose, or un-choose
  for (let i = 0; i < 64; i++) {
    let x = X0 + (i % 8) * (S + G), y = Y0 + floor(i / 8) * (S + G);
    if (mouseX >= x && mouseX < x + S && mouseY >= y && mouseY < y + S) {
      if (chosen.includes(i)) chosen = chosen.filter(j => j != i); else if (chosen.length < 3) chosen.push(i);
    }
  }
}

function keyPressed() {                                    // N: the same rule, sixty-four new
  if (key == 'n' || key == 'N') { base = floor(random(1e6)); generate(); return false; }
}"""

# (b) dataset: thirty candidates, a twelve-slot dataset, and the style it teaches
DATASET_JS = """// A LoRA dataset toy. Thirty candidate images; each has five features: hue, stroke, roundness, size,
// rotation. Click one to put it in the dataset (up to twelve); click again to take it out. The style
// learned is the mean of the dataset, drawn large, plus the spread of every feature; every click draws
// a new sample from mean ± spread. What you put in is what comes out.
const N = 30, T = 84, G = 8, X0 = 20, Y0 = 44, FEAT = ['hue', 'stroke', 'round', 'size', 'rot'];
const LO = { hue: 0, stroke: 1, round: 0, size: 0.4, rot: 0 }, HI = { hue: 1, stroke: 6, round: 1, size: 0.9, rot: 45 };
let cands = [], data = [], sampleSeed = 1;

function setup() {
  createCanvas(1400, 600); textFont('JetBrains Mono'); randomSeed(11);
  for (let i = 0; i < N; i++) cands.push({ hue: random(), stroke: random(1, 6), round: random(), size: random(0.4, 0.9), rot: random(45) });
  data = cands.map((c, i) => i).sort((a, b) => score(cands[b]) - score(cands[a])).slice(0, 8);   // eight already in: one style
}
function score(c) { return c.hue + c.round - abs(c.stroke - 2) / 5; }   // round, orange, thin

function tile(c, x, y, s, frame, bg) {                     // one image: a rounded square, rotated
  stroke(frame); strokeWeight(frame == '#ED6D24' ? 3 : 1); fill(bg || 255); rect(x, y, s, s);
  push(); translate(x + s / 2, y + s / 2); rotate(radians(c.rot));
  noFill(); stroke(lerpColor(color('#64C2C3'), color('#ED6D24'), c.hue)); strokeWeight(max(1, c.stroke * s / 80));
  let side = c.size * s; rect(-side / 2, -side / 2, side, side, c.round * side / 2); pop();
}

function stats() {                                         // the style learned: mean and spread of each feature
  let mean = {}, spread = {};
  for (let f of FEAT) {
    let v = data.map(i => cands[i][f]), m = v.reduce((a, b) => a + b, 0) / max(1, v.length);
    mean[f] = m; spread[f] = sqrt(v.reduce((a, b) => a + (b - m) * (b - m), 0) / max(1, v.length));
  }
  return [mean, spread];
}

function numbers(c, nl) { return 'hue ' + nf(c.hue, 1, 2) + ' · stroke ' + nf(c.stroke, 1, 1) + (nl ? '\\n' : ' · ') + 'round ' + nf(c.round, 1, 2) + ' · size ' + nf(c.size, 1, 2) + (nl ? '\\n' : ' · ') + 'rot ' + round(c.rot) + '°'; }

function draw() {
  background(255);
  let hover = -1;
  for (let i = 0; i < N; i++) {                            // the candidates
    let x = X0 + (i % 10) * (T + G), y = Y0 + floor(i / 10) * (T + G);
    if (mouseX >= x && mouseX < x + T && mouseY >= y && mouseY < y + T) hover = i;
    tile(cands[i], x, y, T, data.includes(i) ? '#ED6D24' : hover == i ? '#5C6470' : '#E1E1DE');
  }
  noStroke(); textAlign(LEFT, BASELINE);
  fill(0); textSize(16); text('CANDIDATES · 30 · click = into the dataset', X0, 30);
  fill('#5C6470'); textSize(14); text(hover >= 0 ? '#' + (hover + 1) + '  ' + numbers(cands[hover]) : 'hover an image: its numbers', X0, Y0 + 3 * (T + G) + 14);
  let dy = 400;                                            // the dataset
  fill(0); textSize(16); text('THE DATASET · ' + data.length + ' of 12', X0, dy - 14);
  for (let j = 0; j < 12; j++) {
    let x = X0 + j * 76;
    if (j < data.length) tile(cands[data[j]], x, dy, 72, '#ED6D24');
    else { stroke('#E1E1DE'); strokeWeight(1); fill('#F4F4F2'); rect(x, dy, 72, 72); }
  }
  noStroke(); fill('#5C6470'); textSize(14); text('click a chosen image, here or above, to take it out', X0, dy + 96);
  let rx = 980;                                            // the style learned
  fill(0); textSize(16); text('STYLE LEARNED · mean ± spread', rx, 30);
  if (data.length) {
    let [mean, spread] = stats();
    tile(mean, rx, Y0, 200, '#000B1C', '#F4F4F2'); noStroke();
    for (let k = 0; k < FEAT.length; k++) {                // the bars: how much room each feature keeps
      let f = FEAT[k], rel = spread[f] / (HI[f] - LO[f]), y = Y0 + 12 + k * 38;
      noStroke(); fill('#5C6470'); textSize(14); text(f, rx + 224, y + 12);
      fill('#E9E9E6'); rect(rx + 290, y, 110, 14);
      fill(rel > 0.15 ? '#ED6D24' : '#64C2C3'); rect(rx + 290, y, max(3, 110 * min(1, rel * 3.2)), 14);
    }
    randomSeed(sampleSeed);
    let s = {};
    for (let f of FEAT) s[f] = constrain(randomGaussian(mean[f], spread[f]), LO[f], HI[f]);
    fill(0); textSize(16); text('WHAT COMES OUT · one sample, mean ± spread', rx, 300);
    tile(s, rx, 316, 160, '#E1E1DE'); noStroke();
    fill('#5C6470'); textSize(14); text(numbers(s, true), rx + 180, 340);
    text('a new one on every click', rx + 180, 420);
  }
  noStroke(); fill('#ED6D24'); textSize(18); text('what you put in is what comes out', X0, 560);
}

function mousePressed() {
  for (let i = 0; i < N; i++) {                            // a candidate: in, or out
    let x = X0 + (i % 10) * (T + G), y = Y0 + floor(i / 10) * (T + G);
    if (mouseX >= x && mouseX < x + T && mouseY >= y && mouseY < y + T) {
      if (data.includes(i)) data = data.filter(j => j != i); else if (data.length < 12) data.push(i);
    }
  }
  for (let j = 0; j < data.length; j++) {                  // a chosen image in the strip: out
    let x = X0 + j * 76;
    if (mouseX >= x && mouseX < x + 72 && mouseY >= 400 && mouseY < 472) { data.splice(j, 1); break; }
  }
  sampleSeed = floor(random(1e6));
}"""

# ───────────────────────── panels ─────────────────────────
SHEET = [
    'THE DATASET SHEET · 12 IMAGES', ' ',
    'STYLE: [one sentence: what these twelve', '  have in common]',
    'OWNER: [whose images: yours, the team’s,', '  licensed — and from where]', ' ',
    'Twelve images in a 3 x 4 grid, numbered.', 'Under each: one line — why it is in.', ' ',
    'WHAT THIS TEACHES: [three things the', '  model would learn: a line, a colour,', '  a habit]',
    'WHAT IT WOULD NOT TEACH: [one thing you', '  wanted and left out, and why]', ' ',
    'CAPTION FOR THE UPLOAD: "what this', '  teaches", in one sentence.',
]

BRIEF = [
    'MEDIATION BRIEF · ONE PAGE · [product] · [team]', ' ',
    '1  THE RELATION', '   Ihde / Verbeek: which one, and its force —', '   hidden or apparent, weak or strong.', ' ',
    '2  THE DATA', '   What it needs; given, taken or inferred;', '   consent, and how it is asked for.', ' ',
    '3  THE BIAS', '   Three rows of the register: the decision,', '   who is thin, the two harms.', ' ',
    '4  THE GUARDRAILS', '   What it may never decide; when a person', '   steps in; how it fails in front of', '   someone; what you watch after launch.', ' ',
    '5  THE PROCESS NOTE', '   What you used, what you chose, what you', '   changed. Names of tools, not adjectives.',
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 11 · LECTURE + WORKSHOP',
               'Curators of outputs and datasets.',
               'Week 11 — the designer’s turn: who made Belamy, and who makes yours.',
               notes='Join code on screen from 30 minutes before. Module 4 starts today: the designer’s turn. Teams sit together from the start; the draft poster, however rough, should be on a laptop at every table — the last round of the activity is a critique of it. The TAs have been checking who has one.'))

S.append(agenda('SD2112 · WEEK 11', [
    'Last week, in your words', 'Who made Belamy?', 'Curators of outputs', 'Curators of datasets',
    'Whose is it? Authorship and ownership', 'The poster lab', 'Activity: curate, assemble, critique', 'Homework: the final poster and video',
], notes='Eight stops. Before the break: a portrait that sold for four hundred thousand dollars and the six hands that made it; then the two things left for the designer when the machine makes the artefact — choosing the outputs and choosing the examples. After the break: the law, in eight rulings on two sides; the anatomy of your poster and your video; and the activity, three rounds, each ending in ClassPoint. Draft poster and mediation brief are due tonight.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the prototypes · the video · the map', bg=PINKS[0],
                 notes='Chapter one: what came back from week 10, the homework video, and where we are. Ten minutes.'))

S.append(question('word_cloud', 'Edmond de Belamy: who made it? One word.',
                  hint='The video was the homework: Obvious’s own account of the portrait. One word — a name, a thing, a machine.',
                  eyebrow_text='01 · QUESTION · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each; leave it on screen for a minute. Expect: Obvious, algorithm, GAN, computer, nobody, Barrat if someone read further. Read the three biggest aloud and say nothing yet; the whole of chapter two is the answer, and the same question comes back as a vote on slide 12. Screenshot it. If the cloud is thin, the room did not watch a four-minute video; say so, without blame, and play a minute on slide 10.'))

S.append(cards('01 · PROTOTYPE V1 · WHAT CAME BACK', 'Three things we saw in your prototypes.', [
    ('THE SCREEN', 'Most of you drew the moment.', 'The screen where the decision lands — the card, the suggestion, the voice — was there in nearly every prototype. Good. That is the shot the video needs.'),
    ('THE DECISION', 'Fewer of you drew the decision.', 'What the model decided, from what, was often a label: "AI recommends". Week 8’s anatomy — data, score, line, decision or fallback — belongs on the poster, drawn.'),
    ('THE NO', 'Almost nobody drew the no.', 'How the person refuses, corrects or appeals. Week 9’s guardrail column, week 10’s feed you did not want. It is a screen too, and the rubric’s ethics mark lives there.'),
], notes='Replace these three with the real ones: Amber has the prototypes; pick two anonymised screenshots for each card if there is time, no team names. The point is not to scold: the prototypes did what week 10 asked — the interaction, not the model. Today adds the two things every poster still needs: the decision, drawn, and the no, drawn. Both come back in the poster lab after the break.', text_size=23))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(4, 0),
                 notes='Week 11, module four opens: the designer’s turn. Modules one to three were about the machines and the products; this one is about you. Today curating and authorship; next week language as an interface and the mock poster session; week 13 the fair and the final quiz. Draft poster and mediation brief tonight; final poster and video for next week.'))

# ───────────────────────── 02 · who made Belamy? ─────────────────────────
S.append(section('02', 'Who made Belamy?', 'Paris · New York · 25 October 2018 · six hands, one signature', bg=INK,
                 notes='Chapter two: the portrait from week 1 comes back with its whole story. Fifteen minutes, and the room votes at the end.'))

S.append(image_full('edmond-de-belamy.jpg', '2018 · OBVIOUS · EDMOND DE BELAMY · CHRISTIE’S, NEW YORK',
                    'Sold on 25 October 2018 for US$432,500, against an estimate of $7,000 to $10,000. Week 1 asked who the author is. Today you answer.',
                    notes='Same slide as week 1, with the question turned round. Let the room look for ten seconds. A blurred face in a gilt frame, a printed canvas, a formula where the signature goes. Everything about it was a choice somebody made — the frame, the blur, the formula, the name — and none of the choices was the network’s. Hold that; the next slides name the hands.'))

S.append(cards('02 · THE SALE', 'Four facts about a portrait.', [
    ('25 OCTOBER 2018', 'Christie’s, New York.', 'The Prints & Multiples sale. Estimate $7,000 to $10,000; hammer $432,500. The first work made with a GAN sold at a major auction house, and the headline that put AI art in every newspaper.'),
    ('ONE OF ELEVEN', 'La Famille de Belamy.', 'Eleven portraits of an invented French family, from one trained network. Edmond is the one Obvious printed, framed and sent to auction. The other ten stayed in the studio.'),
    ('THE SIGNATURE', 'A loss function.', 'Bottom right, where a painter signs: the formula every GAN is trained with — Ian Goodfellow’s, 2014. Belamy is a pun on his name: bel ami, good fellow. The signature credits the inventor of the method.'),
    ('THE CODE', 'Robbie Barrat, 2017.', 'Open source, on GitHub, already trained on portraits. Barrat was a teenager. On Twitter, the week of the sale: "Am I crazy for thinking that they really just used my network and are selling the results?"'),
], text_size=21, notes='Four facts, all verifiable, and the fourth is the one the room has not heard. Obvious — Hugo Caselles-Dupré, Pierre Fautrel, Gauthier Vernier, Paris — found Barrat’s code on GitHub, ran it on fifteen thousand portraits from WikiArt, kept eleven outputs, printed one. Caselles-Dupré told The Verge that not much of the code had been modified. Nobody broke a licence; the code was open. The question is not legal yet. It is: which of these hands is the author?'))

S.append(video('02 · THE HOMEWORK · OBVIOUS · GENERATION OF EDMOND DE BELAMY', 'The makers’ own account.', 'Pu2GZ3du7PI',
               ['Obvious’s video of the portrait being generated: the dataset, the training, the outputs, the print.',
                '- Watch for what the video shows and what it does not: you see the network run; you do not see the moment somebody said "that one".',
                '- Every generative story is told this way. The choosing is edited out, because it looks like nothing.'],
               thumb='yt/Pu2GZ3du7PI.jpg',
               notes='Play one minute if the word cloud was thin; skip if it was full. The design point is the edit: the video shows the machine working and cuts the human deciding, because deciding is a person looking at a screen. That is the whole of chapter three. Cut this slide if behind.'))

S.append(figure_slide('02 · SIX HANDS', 'Six hands between the painters and the hammer.', F.w11_belamy_chain(),
                      body=['Read it left to right: made, gathered, invented, wrote, chose, sold. The network drew every stroke; every decision on this line was a person’s. The market paid the hand that chose.'],
                      caption='The painters (14th to 19th century, via WikiArt); Goodfellow’s GAN (2014); Barrat’s code (2017); Obvious’s run, pick and print (2018); Christie’s hammer, 25 October 2018.',
                      notes='Walk the boxes. The painters made the examples and never knew. WikiArt gathered them: a dataset before the word. Goodfellow invented the method: two networks, a forger and a critic, trained against each other, one loss function — the formula on the canvas. Barrat wrote and trained the code, openly. Obvious ran it, kept eleven, printed one, signed it with somebody else’s formula. Christie’s sold it. Ask: which box would you put your name in? Then the vote.'))

S.append(question('multiple_choice', 'Who is the author of Edmond de Belamy?', [
    'Obvious: they chose, printed, signed and sold it', 'Robbie Barrat: he wrote and trained the code', 'The painters of the fifteen thousand portraits', 'Nobody: a machine made it',
], eyebrow_text='02 · YOUR VERDICT · MULTIPLE CHOICE',
    notes='No correct answer, and the split is the lesson; screenshot it. Most rooms split between A and B, with a loud minority on D. Ask one of each to defend it in a sentence. Then say where the law stands, as a preview of chapter five: nobody has sued over Belamy; if the US Copyright Office were asked today, the image itself would probably not be protected at all (D), while the selection and arrangement of the eleven as a family might be Obvious’s (A). The market answered A in 2018. Barrat’s case is moral, not legal: the code was open, and he was not credited.'))

S.append(statement('The machine painted all eleven. Somebody chose Edmond.', eyebrow_text='02 · WHERE THE AUTHORSHIP WENT', size=110,
                   notes='The sentence of the chapter. Everything the network did, it did eleven times, and would have done a thousand. The one act that happened once was the choice. Chapter three makes that act a craft.'))

# ───────────────────────── 03 · curators of outputs ─────────────────────────
S.append(section('03', 'Curators of outputs', 'generate · discard · shortlist · ship', bg=PINKS[0],
                 notes='Chapter three: the first thing left for the designer. The model makes many; you pick one; the pick is the authorship, and the reasons for it are the design. A live sketch, and the chairs and layouts from earlier weeks.'))

S.append(statement('The model makes 64. You pick one.', eyebrow_text='03 · THE CURATOR', size=124,
                   notes='Say it plainly. Midjourney gives four; a batch gives sixty-four; a feed gives a thousand. Nothing that comes out is finished until someone says which. That someone is you, and this chapter is about doing it well rather than fast.'))

S.append(sketch_slide('03 · LIVE · CURATE', 'Sixty-four from one rule. Three of them are yours.',
                      live('w11-curate', CURATE_JS, 1100, 760, hint='click = choose up to three · N = sixty-four new'),
                      caption='One rule (a grid of cells, a motif, a density, a rotation, a weight, a colour), sixty-four seeds. The machine cannot tell them apart. Hover for the numbers; click three; press N for a fresh batch. The reasons you give are the design.',
                      notes='In the html deck this runs live; ask the room to call out numbers. Pick three yourself, saying why out loud — "the only one with a rhythm", "the one that would survive at stamp size", "the one that looks like a mistake and is not". Then press N and do it again: the taste survives the batch, the tiles do not. Every tile obeys the rule equally; the rule cannot rank them. Ranking is what you are for. Then hand it to the room in the activity.'))

S.append(figure_slide('03 · THE FUNNEL', 'From sixty-four to one. Where the taste is.', F.w11_funnel(),
                      body=['Generate wide: that is the model’s work, and it is cheap. Discard, shortlist, ship: that is yours, and it is the whole of the authorship. Belamy: eleven kept, one printed.'],
                      caption='The tiles follow the same rule as the sketch. 52 gone at the first pass (the wrong, the same, the unsafe); three with a written reason each; one with your name on it.',
                      notes='Four stages, and only the first belongs to the machine. Discard is fast and mostly negative: wrong, duplicate, unsafe. Shortlist is where the reasons get written, and the reasons are what you can show a client, a jury, a court. Ship is one, and you answer for it. Ask the room where they usually stop: most people stop at "that one’s nice", which is a discard without a shortlist. The written reason is the difference between taste and luck.'))

S.append(content('03 · WEEKS 1, 3 AND 5, REVISITED', 'You have been curating since week 1.',
                 ['Week 1: one prompt, four seeds, and the wall of cups. Each four chose one cup that was "still a cup". The wall was already curated: 28 picks out of a hundred and more.',
                  '- Week 3: told chairs and shown chairs. You kept the one furthest from the middle that was still a chair. The reference pulled; you chose.',
                  '- Week 5: the layout the model made from your brief. The critique asked what the model decided that you did not. Today’s question is the mirror: what did **you** decide that the model did not?',
                  'The pick, and the reason. That was you, every time.'],
                 images=CHAIRS, body_size=27,
                 caption='Week 1: "a chair, studio product photograph, plain white background" — one model, four seeds. You looked at four and shipped one. That was the authorship.',
                 notes='The four chairs from week 1 come back for the last time. Nobody in the room would ship all four; everyone would pick one, and could say why — the light, the proportion, the least mid-century. That sentence is the design. Week 3’s activity and week 5’s layouts were the same act with references and briefs added. For the reflection you wrote in week 7, this is the thread: the machine generated, you selected, and the selection was where your practice lived.'))

S.append(cards('03 · FOUR MOVES', 'Four moves of a curator.', [
    ('GENERATE WIDE', 'Sixty-four, not four.', 'Ask for more than you need, with a seed, so the batch can be shown again. Change one thing between batches: the prompt, the reference, the seed. Never all three.'),
    ('DISCARD FAST', 'Say no in seconds.', 'The wrong ones, the same ones, the ones you could not defend to the person in the picture. Most of a batch goes here. Do not explain a discard; explain a keep.'),
    ('SAY WHY', 'One line per keep.', 'A noun, not an adjective: "the only one with a rhythm", not "nice". Written reasons are what a client, a jury and a court can read. Belamy’s eleven had no written reasons.'),
    ('ANSWER FOR IT', 'Your name on the one.', 'The course rule since week 1: allowed, disclosed, yours. Ship it, and take the credit and the blame. The model has neither.'),
], text_size=22, notes='Four moves, in order, and the third is the one nobody does. Generating wide is free; discarding is instinct; shipping is a deadline. Saying why is the craft, and it is the part that the law, in chapter five, and the rubric, in chapter six, both reward. The activity makes them write three reasons for three tiles. Watch how hard that is.'))

S.append(cards('03 · GATEKEEPING', 'Not everything generated should be released.', [
    ('THE LIKENESS', 'A real face, a real voice.', 'Week 6’s cases: the voice that sounded like a named singer, the clip nobody was told about. If the batch contains a person who exists, the pick is not yours to make.'),
    ('THE STYLE', 'Somebody’s living hand.', '"In the style of" a working illustrator is a discard, whatever the law says this year. Your own style, your own dataset, is chapter four.'),
    ('THE HARM', 'The person on the other side.', 'Week 9’s two errors: the false yes and the false no. A picture that is untrue about the product, a face that is untrue about a people. The bias register applies to outputs too.'),
    ('THE WRONG ONE', 'True to the brief, wrong for the world.', 'The trailer with no product in it; the poster that promises what the model cannot do. The gatekeeper’s question: would I show this to the person it is about?'),
], text_size=22, notes='The second half of the curator’s job is saying no to things the client would have loved. Four gates, and two of them — likeness and style — have been in the news every month since 2023. Ask the room for one case from the last month; there is always one. The course line: the gate is a rule you write, machine A protecting people from machine B, week 1’s guardrail-setter. Chapter five gives the legal floor; the gate should sit above it.'))

S.append(question('multiple_choice', 'A model gives you sixty-four logos in a minute. Where is the design?', [
    'In the prompt', 'In the model', 'In the pick, and the written reasons for it', 'In the training data',
], eyebrow_text='03 · QUICK CHECK · MULTIPLE CHOICE',
    notes='C. A and D are partly true — the prompt is a spec (week 2) and the data set the middle (week 9) — but neither chooses. The model cannot rank its own outputs; that is what the loss function does not measure. Ask a B to explain: they usually mean "the model did the work", which is the Belamy video’s edit. The design is the decision, and the decision is yours.'))

# ───────────────────────── 04 · curators of datasets ─────────────────────────
S.append(section('04', 'Curators of datasets', 'twenty images · one style · whose?', bg=INK,
                 notes='Chapter four: the second thing left for the designer — choosing the examples. A LoRA in one drawing and one sketch, how to build a dataset, and who the images belong to. Twenty-seven minutes, with the break at the end.'))

S.append(figure_slide('04 · A STYLE IS TWENTY IMAGES', 'What you put in is what comes out.', F.w11_lora_mean(),
                      body=['Week 5: a LoRA freezes the model and trains a small set of extra weights on your images. The middle moves to the mean of what you gave it, and stays as loose as your examples disagree.'],
                      caption='Two twelve-image datasets, the style each teaches (the mean tile, and how much room each feature keeps), and what comes out. A drawing of the mechanism, not a training run.',
                      notes='Two rows, same mechanism. Dataset A agrees on three things — round, orange, thin — and varies the rest; the learned style is those three things, every time, with the rest still free. Dataset B is twelve things the team liked; the mean is a brownish rounded square nobody drew, and the samples are the middle of everything. Hu and colleagues, 2021, for the method; the numbers on the bars are the whole design decision: what to hold constant, what to leave open. The sketch lets you move them.'))

S.append(sketch_slide('04 · LIVE · THE DATASET', 'Put twelve in. Watch what it learns.',
                      live('w11-dataset', DATASET_JS, 1400, 600, hint='click = into the dataset, up to twelve · click again = out'),
                      caption='Thirty candidates, five features each. The dataset at the bottom; the style learned on the right: the mean, the spread of every feature, and one sample from mean ± spread on every click. Take out the odd ones and watch the bars shrink.',
                      notes='Start from the eight already in — one style, narrow bars. Add three images that do not belong and the mean drifts, the bars go orange, the sample turns to muddle. Take them out. Then build the opposite: twelve that agree on nothing. The lesson is the bars: a dataset teaches what its images agree on, and leaves free what they do not. Ask: what should your team’s dataset agree on? That is the activity’s "what this teaches".'))

S.append(cards('04 · HOW TO BUILD ONE', 'Twenty images, deliberately chosen.', [
    ('ONE THING IN COMMON', 'The style is the agreement.', 'Every image shares the thing you want learned — a line, a palette, a way of framing — and the model learns exactly that. Twelve that agree teach more than a hundred that do not.'),
    ('EVERYTHING ELSE VARIED', 'Or it learns the wrong thing.', 'Same subject every time and the model learns the subject, not the style. Vary what you do not want learned: the object, the angle, the background.'),
    ('CAPTIONED', 'Words for what to ignore.', 'Each image gets a line: what is in it, so the model can separate the content from the style. A wrong caption teaches a wrong link. Read every one.'),
    ('COUNTED', 'Twenty to fifty.', 'Enough to average over, few enough to have looked at each. A narrow style: twenty. A broad one: fifty. Near-duplicates count as one.'),
], text_size=22, notes='Practical numbers, from the community guides rather than from a paper: twenty to fifty for a style, more for a broad one. The design rule is the first card: a dataset is an agreement, and you decide what is agreed. The second card is the trap every first dataset falls into — twenty photos of the same mug teach "mug", not "your lighting". The activity builds one on paper; anyone who wants to train it for real can, with the TAs, on their own images only.'))

S.append(content('04 · LAION-5B · 2022', '5.85 billion pairs. Nobody chose them.',
                 ['The dataset behind most open image models: 5.85 billion image–text pairs, scraped from Common Crawl, kept if a model thought the alt-text matched the picture. Released March 2022; its makers called it uncurated, for research, not for products.',
                  '- December 2023: Stanford’s Internet Observatory found more than a thousand confirmed images of child sexual abuse in it. LAION took it down. August 2024: Re-LAION-5B, with 2,236 links removed.',
                  '- Nobody in it consented. Spawning’s Have I Been Trained lets people search it and register an opt-out; by 2023 about eighty million works had opted out of the next round of training.',
                  'Week 9 called it the window. This week it is the example of a dataset nobody curated — and the reason yours must be.'],
                 body_size=30,
                 notes='The counter-example to the twenty images. Nobody chose five billion; a similarity score did. Two consequences. The middle: week 9’s chairs and week 1’s cups came from this window, and the middle of five billion captions is a very particular middle. The floor: an uncurated scrape contains the worst of the web, which is why it was pulled in December 2023 and rebuilt eight months later. Opt-outs exist and are honoured by some trainers; they are not consent. Your dataset of twenty is the opposite object: every image chosen, every owner known.'))

S.append(cards('04 · WHOSE IMAGES', 'Four sources, four answers.', [
    ('YOUR OWN', 'Your sketches, your photos.', 'Nothing to ask. The model learns your edge, not the internet’s middle. This is the dataset the activity builds, and the one the course recommends.'),
    ('LICENSED', 'Bought, or granted.', 'Stock with a licence that allows training; a client’s archive with their written yes; a colleague’s work with theirs. Keep the licence with the dataset.'),
    ('OPTED IN', 'Asked, and answered.', 'Images whose makers said yes to this use — not "did not say no". Consent is a design decision, and a sentence on your poster.'),
    ('SCRAPED', 'Taken because it was there.', 'Legal in some places for some uses, and being litigated in the rest. A living artist’s Instagram is a scrape whatever the court says next year. Discard.'),
], text_size=22, notes='Four sources on a scale of consent, and the course position is the first two. Say the fourth card carefully: the training-side rulings after the break say scraping can be lawful; the gate on the previous chapter says it is still a discard when the source is a person who did not agree. Hong Kong’s proposed exception, after the break, has an opt-out — which is the third card, reversed.'))

S.append(question('multiple_choice', 'Which of these can you fine-tune on without asking anyone?', [
    'Thirty of your own sketches', 'Thirty posts from an illustrator you admire', 'Thirty frames from a film', 'Thirty stock photos whose licence you have not read',
], eyebrow_text='04 · QUICK CHECK · MULTIPLE CHOICE',
    notes='A. D is the trap: a licence is a yes only once you have read it, and most stock licences say nothing about training or forbid it. B and C are other people’s work: the law after the break is unsettled, the gate is not. Ask who in the room has thirty of their own sketches; nearly everyone does, on a phone. That is the dataset for the activity.'))

S.append(statement('Choose the examples and you have chosen the prototype. Whose examples, and did they agree?', eyebrow_text='04 · WHERE WE ARE', size=96,
                   notes='The sentence to carry across the break. Week 1 said the first half; today adds the second. Two questions for any model you use or build: whose images taught it, and what did those images agree on. After the break: what the law says about both.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · AUTHORSHIP AND OWNERSHIP · THE POSTER LAB · THE ACTIVITY', size=120, bg=PAPER,
                   notes='1:20. Teams sit together after the break with the draft poster open and thirty of their own images reachable — a phone gallery is fine. The TAs check every table has both.'))

# ───────────────────────── 05 · whose is it? ─────────────────────────
S.append(section('05', 'Whose is it?', 'authorship · ownership · what a court calls transformative', bg=PINKS[0],
                 notes='Chapter five: the law, in eight rulings on two sides — who owns what comes out, and whether what went in was allowed. One card each, one sentence each; this is not a law class, it is a designer’s map of where the lines are in 2026. Twenty-eight minutes.'))

S.append(statement('No human author, no copyright.', eyebrow_text='05 · THALER v. PERLMUTTER · D.C. CIRCUIT · 18 MARCH 2025 · CERT. DENIED 2 MARCH 2026', size=124,
                   notes='Stephen Thaler asked the US Copyright Office in 2018 to register A Recent Entrance to Paradise with his "Creativity Machine" as the sole author. Refused; refused again in court; the D.C. Circuit affirmed on 18 March 2025; the Supreme Court declined the case on 2 March 2026. The holding is narrow and firm: the Copyright Act’s author is a human. The court said nothing about works made with a machine’s help — that is the next slide, and it is where you live.'))

S.append(cards('05 · THE OUTPUT SIDE', 'Who owns what comes out. Four positions.', [
    ('THALER · 2018 – 2026', 'A machine cannot be the author.',
     'Thaler listed his machine as sole author of an image. The Copyright Office refused; the D.C. Circuit affirmed, 18 March 2025; the Supreme Court declined, 2 March 2026. The court left works made with AI help for another day.'),
    ('ZARYA · 2023', 'The arrangement is yours. The pictures are not.',
     'Kris Kashtanova’s graphic novel, images by Midjourney. The Office’s letter of 21 February 2023: the text and the selection, coordination and arrangement are protected; the individual images are not, because she lacked control over what came out.'),
    ('USCO · JANUARY 2025', 'Prompts alone are not authorship.',
     'Part 2 of the Office’s AI report: a prompt, however long, is an instruction and does not control the expression. Human authorship survives in what you select, coordinate, arrange or modify — case by case. No new law needed.'),
    ('ALLEN · 2022 – PENDING', '624 prompts, 100 hours, one refusal.',
     'Théâtre D’opéra Spatial won a Colorado State Fair prize in 2022. The Office refused registration in 2023; Allen sued in September 2024; briefing ended in early 2026 and a ruling was awaited when this deck was written. The test case for "but I worked at it".'),
], text_size=20, notes='Four positions, one direction. The machine is never the author; the person is, exactly to the extent of what they chose, arranged and changed. Zarya is the one designers should know by heart: the book is hers, the pages’ arrangement is hers, each picture is nobody’s. Allen is the honest hard case — six hundred prompts is real labour — and the Office’s answer is that labour at the prompt is not control of the picture. Check the Colorado docket (Allen v. Perlmutter, 1:24-cv-02665) before class: a ruling was expected in 2026 and the card must say what it held. The ladder on the next slide puts your own work on this scale.'))

S.append(figure_slide('05 · THE LADDER', 'Where a human author begins.', F.w11_authorship_ladder(),
                      body=['Five things you might have done, and what the 2025 US position says about each. The line the law draws is the line the rubric draws: what you chose, arranged, changed and made.'],
                      caption='A designer’s reading of the Copyright Office’s Part 2 report (January 2025), Zarya of the Dawn (February 2023) and the Allen refusal. Not legal advice; a map of where the line is this year.',
                      notes='Walk the rungs with the room’s own work. The prompt: yours, but the picture it makes is not. The pick: the image stays unprotected; picking alone is not a work. Arranging several — a layout, a sequence, a poster — is a compilation and it is yours; the tiles inside are not. Modifying: what you changed is yours, and the more you changed, the more that is. Making: your drawing, your dataset of your drawings, always yours. Point at the bar: the further right you work, the more of the poster is yours in law — and the more the rubric can give you marks for.'))

S.append(content('05 · CLOSER TO HOME · HONG KONG', 'The person who made the arrangements.',
                 ['The Copyright Ordinance has had a clause for computer-generated works since the 1990s. Section 11(3): the author is "the person by whom the arrangements necessary for the creation of the work are undertaken".',
                  '- A person, not a machine — but which person: the developer who trained it, or you, who prompted and chose? The clause was written for plotters, and nobody has tested it on a diffusion model.',
                  '- July to September 2024: a public consultation on copyright and AI. The proposal: a text-and-data-mining exception that would allow training, with an opt-out for owners who reserve their rights. Outcomes published 18 February 2025, with a text-and-data-mining exception to follow; the bill was still to come.',
                  'Two jurisdictions, two vocabularies: the US asks who controlled the expression; Hong Kong asks who arranged for it. Your process note answers both.'],
                 body_size=29,
                 notes='The local answer, and it is older than the question. Section 11(3) came from the UK’s 1988 Act, for works with no human author; it names the arranger. Ask the room who arranged Belamy: Obvious, on this reading. The 2024 consultation is the training side: an exception for text and data mining with an opt-out — the third card of chapter four, turned into law. Nothing had passed as of this deck; check the Intellectual Property Department’s page before class and update the last bullet if a bill has moved.'))

S.append(cards('05 · THE TRAINING SIDE', 'Whether what went in was allowed. Four rulings.', [
    ('GOOGLE BOOKS · 2015', 'Copying to search is transformative.',
     'Authors Guild v. Google, Second Circuit, 16 October 2015: scanning millions of books to index them and show snippets is fair use — a new purpose that does not substitute for the books. The Supreme Court declined the appeal in 2016. Every AI training defence starts here.'),
    ('ANTHROPIC · 2025 – 26', 'Training, yes. The pirated library, no.',
     'Judge Alsup, June 2025: training a language model on lawfully bought books is "exceedingly transformative" and fair use; keeping a library of pirated copies is not. Settled for $1.5 billion — about $3,000 a book — announced September 2025, approved July 2026.'),
    ('KADREY v. META · 2025', 'Fair use here — because of the arguments made.',
     'Judge Chhabria, 25 June 2025: Meta’s training on the authors’ books was fair use on this record, but the ruling "does not stand for the proposition" that such training is lawful — the plaintiffs "made the wrong arguments". Market dilution is the argument left open.'),
    ('GETTY · UK · 2025', 'A model is not a copy of its training data.',
     'High Court, 4 November 2025: Getty dropped its training claims mid-trial (no evidence the training happened in the UK); on what remained, Stable Diffusion’s weights are not an "infringing copy" of Getty’s images. Limited trade-mark findings only.'),
], text_size=19, notes='Four rulings, two countries, one shape: training on what you lawfully have is being allowed; taking what you do not have is not; and the market question — does the model’s output replace the work it learned from — is the one still open, named by Chhabria and left for the next plaintiff. The Anthropic number is worth saying slowly: a billion and a half dollars, for the library, not for the training. For a designer the practical line is the same as chapter four’s cards: what you own or licensed, yes; what you scraped, at your own risk; what you pirated, never.'))

S.append(content('05 · TRANSFORMATIVE, FOR A DESIGNER', 'New purpose, not a substitute.',
                 ['The Google Books test, in the court’s words: a transformative use "communicates something new and different from the original or expands its utility". The other half of the test: it must not stand in for the original in its market.',
                  '- A moodboard of someone’s work is a new purpose. A poster that could replace theirs is a substitute.',
                  '- A model that learned a thousand styles and makes yours is a new purpose. A LoRA of one living illustrator, sold as their look, is a substitute — and Chhabria’s open argument.',
                  '- Your pick of one output is neither: it is a choice, and the law does not protect it. Your arrangement, your changes and your own drawings are, and it does.',
                  'Two questions before anything ships: would the person whose work is in it recognise theirs? And does it do their job?'],
                 body_size=29,
                 notes='The word "transformative" comes from a 1994 Supreme Court case about a parody song and was made the centre of fair use by Google Books. Give the room the two questions and stop there; they are enough for a poster and a process note. The second question is the market one and the one the AI cases turn on. Then the process note: the practical instrument that answers all of this for your project.'))

S.append(cards('05 · YOUR PROCESS NOTE', 'What the law protects, the rubric grades.', [
    ('WHAT YOU USED', 'Name the tools.', 'Which model, which version, for which part: the images, the text, the video, the code. The course rule since week 1: allowed, disclosed. A tool left out of the note is the only way to fail this.'),
    ('WHAT YOU CHOSE', 'Keep the batch and the reasons.', 'Sixty-four and the three, with a line each. The selection is yours in law only if it can be seen; it is yours in the rubric only if it can be read. Screenshots, with dates.'),
    ('WHAT YOU CHANGED', 'Show before and after.', 'The output as it came and the poster as it is. Every change is yours; the rubric’s research and ethics marks live in the changes, not in the generation.'),
], notes='Three columns, and they are the same three the ladder rewarded. The process note was on the reflection in week 7 and is on the group project’s poster strip. Say the practical thing: keep everything — the batches, the picks, the reasons, the befores — in a shared folder from tonight, because the note is written from it in week 12, and nobody remembers a seed. Then the quick check.'))

S.append(question('multiple_choice', 'You type a 400-word prompt. The model returns one image. You ship it untouched. Under the 2025 US position, who holds the copyright?', [
    'You: the prompt was yours', 'The company that made the model', 'Nobody: the image is not protected', 'The people whose work trained the model',
], eyebrow_text='05 · QUICK CHECK · MULTIPLE CHOICE',
    notes='C. The Copyright Office’s January 2025 report: a prompt, however long, does not control the expression; Allen’s 624 prompts did not either. Not A; not B, which is a terms-of-service question, not a copyright one; not D, which is the training side. Ask what would change the answer: arrange it with others, change it, draw over it — the ladder. Then the poster lab.'))

# ───────────────────────── 06 · the poster lab ─────────────────────────
S.append(section('06', 'The poster lab', 'A0 · four zones · six shots · one page', bg=INK,
                 notes='Chapter six, short and practical: what the A0 poster is made of and where the marks sit; the video in six shots; the one-page mediation brief; and how to critique a draft. Twelve minutes, then the activity uses all of it.'))

S.append(figure_slide('06 · THE A0', 'Four zones. The marks sit on two of them.', F.w11_poster_anatomy(),
                      body=['841 by 1189 millimetres. Three metres away it is one sentence and one picture; one metre away it is the research and the mediation. Sixty percent of the mark is in the two zones most drafts leave thin.'],
                      caption='Title band · RESEARCH and CONCEPT · THE DECISION (week 8’s anatomy, drawn) · THE MEDIATION (the brief, drawn) · the process strip with the QR code to the video. Rubric weights from the syllabus.',
                      notes='Read the poster top to bottom, then the annotations. Title: the product in one sentence a stranger can read from the door. Research and concept side by side: what you found, and the person and the moment. The decision, drawn as week 8 drew it — data, score, line, decide or fall back — because a label saying "AI" is not a decision. The mediation: the four cells of the brief. The strip: roles, tools, sources, the QR code. Then point at the percentages: research thirty, ethics thirty. The two zones drafts leave thin are worth more than half the mark.'))

S.append(cards('06 · THE FOUR ZONES', 'What goes in each.', [
    ('RESEARCH', 'What you found out.', 'Sources you read, products you compared (weeks 8 and 10), people you asked. Named, dated, cited. Thin here costs more than anywhere else.'),
    ('CONCEPT', 'The person and the moment.', 'Who, where, doing what, and what the product does for them. One image of the moment; one sentence of the promise. The prototype from week 10, cleaned.'),
    ('THE DECISION', 'What the model decides, from what.', 'Week 8’s anatomy, drawn for your product: the data (given, taken, inferred), the score, the line, the decision and the fallback. Rule or examples: say which.'),
    ('THE MEDIATION', 'What it does to them.', 'The brief, drawn: the relation (week 5), the data and consent (week 9), the bias register’s worst row, the guardrails. Names, not adjectives.'),
], text_size=22, notes='One card per zone, and each card names the week it comes from — say that: the poster is the course, folded. The decision zone is the one to check first at critique: if you cannot find the line and the fallback, the poster describes an app, not a model. The mediation zone is the brief; the next slides give it a page.'))

S.append(figure_slide('06 · THE VIDEO', 'Six shots. Shoot the decision, not the logo.', F.w11_storyboard(),
                      body=['Three to five minutes, for someone who has never seen the product. Six shots in order: the person, the gap, the decision, what they see, when it is wrong, what it does to them. Phone footage is fine; a trailer with no decision in it is not.'],
                      caption='Timings for a four-minute cut. Shot five — the false yes, the false no, and how the person says no — is the one most storyboards skip and the one the ethics mark reads.',
                      notes='Storyboard it on paper tonight, six boxes, before anyone opens an editor. The rubric gives the video ten percent for one thing: how it works, explained. The decision shot is the middle of the film; if the product is a wizard behind a curtain (week 8) the shot can be the curtain. Generated footage is allowed and goes in the strip. A QR code on the poster links to it; test the code on a phone before the fair.'))

S.append(two_col('06 · THE MEDIATION BRIEF · ONE PAGE', 'Five headings. One page. Due tonight.',
                 ['The brief is the ethics mark on paper: thirty percent of the project. Five headings, one paragraph each, one page.',
                  '- **Relation and data** are weeks 5 and 9, written for your product.',
                  '- **Bias** is the register from week 9, three rows, cleaned.',
                  '- **Guardrails** are the rules you write to protect people from the model: what it may never decide, who steps in, how it fails.',
                  'The **process note** is chapter five: used, chose, changed.'],
                 BRIEF, right_size=20, left_size=29,
                 notes='The template is on Blackboard. One page means one page: the poster’s mediation zone is a drawing of this, and the fair’s jury reads the page, not the zone. The draft due tonight can have gaps marked with a question mark; a heading left out is the only draft that gets sent back. Amber reads every draft before week 12.'))

S.append(cards('06 · THE CRITIQUE PROTOCOL', 'Three moves, eight minutes, no defending.', [
    ('SAY WHAT YOU SEE', 'From three metres.', 'Stand back. Say the product in one sentence from what the poster shows, not from what the team tells you. If you cannot, that is the first finding.'),
    ('FIND THE DECISION', 'From one metre.', 'Point at the data, the line, the fallback and the no. Anything you cannot point at is missing, whatever the team says is "implied".'),
    ('ONE FIX', 'In writing.', 'The single change that would move the poster most, in one sentence, on a sticky note. Not three. The team writes it on the upload; they do not argue with it.'),
], notes='The same rule as week 9’s red pen: no defending. Critique is fast when it is structured and endless when it is not; three moves, one sticky note. The sticky note is the caption of the last upload, which is how the fix survives the afternoon. Then the activity.'))

# ───────────────────────── 07 · activity: curate, assemble, critique ─────────────────────────
S.append(section('07', 'Curate. Assemble. Critique.', '33 minutes · your team · the sketch · your images · your draft', bg=YELLOWS[0],
                 notes='The activity: three rounds, each ending in ClassPoint. Curate three of sixty-four and write why; assemble a twelve-image dataset of a style you own and say what it teaches; swap draft posters with the next team and give one fix. Nicolò keeps time; Amber, WU Zhao and MA Jie walk. One laptop per team for the sketch (the course site, week 11, the curate sketch opens on its own from the LIVE chip), phones for the images.'))

S.append(activity('1 — TEAMS · CURATE', 6, 'Pick three of sixty-four. Say why.',
                  ['Open the curate sketch on the course site, or watch the screen. Press **N** once: your own sixty-four.',
                   'As a team, choose **three**. For each, one line: a noun, not an adjective. "#27: the only one with a rhythm." "#3: survives at stamp size."',
                   'Then the hard one: **which one ships**, and why it beat the other two.'],
                  sketch=live('w11-curate', CURATE_JS, 1100, 760, hint='click = choose up to three · N = sixty-four new'), bg=YELLOWS[0],
                  notes='Six minutes. Teams that cannot agree are doing it right; make them write the disagreement down. Watch for "nice", "clean", "modern" — adjectives without a noun — and send the TA over with "which part?" The third step is the shipping decision and it should hurt a little. The sketch runs on the slide too, for anyone without a laptop: call out numbers.'))

S.append(question('short_answer', 'Your three of sixty-four, and why.',
                  hint='One scribe per team. Three tile numbers, a reason each, and the one that ships — in one line.',
                  example='#27 rhythm · #3 survives at stamp size · #50 the mistake that isn’t → ships #27',
                  eyebrow_text='07 · CAPTURE 1 · SHORT ANSWER · ONE PER TEAM',
                  notes='ClassPoint short answer, scribes only, three minutes; about 28 answers. Read four aloud and put the tiles on screen if the html deck is up: the room sees three different teams pick three different tiles from the same rule with three different reasons, and every reason is legible. That is authorship, written down. Keep the answers: the reasons come back as examples of a process note.'))

S.append(activity('2 — TEAMS · THE DATASET', 10, 'Twelve images of a style you own.',
                  ['A style **you own**: your sketches, your photos, the team’s drawings from week 8. Nothing scraped, nothing from an illustrator you admire.',
                   'Pick twelve that **agree on one thing** and vary in the rest. Lay them out with the sheet on the right: numbered, one line each.',
                   'Write **what this teaches** — three things the model would learn — and one thing you left out, and why.'],
                  panel=SHEET, panel_size=21, bg=YELLOWS[1],
                  notes='Ten minutes, the heart of the afternoon. A phone gallery and a table is enough: photograph twelve images side by side, or paste them into a slide. The stall is always the same: the team has twelve things it likes and cannot say what they agree on — send them back to the sketch’s bars. "What it would not teach" is the curator’s gate from chapter three, applied to their own work. Anyone who wants to actually train it: the TAs can point them to a LoRA trainer after class, on their own images only.'))

S.append(question('image_upload', 'Scribes only. The twelve, and what they teach.',
                  hint='One image per team: the sheet, twelve images numbered. Caption: "what this teaches", in one sentence.',
                  eyebrow_text='07 · CAPTURE 2 · IMAGE UPLOAD · ONE PER TEAM · CAPTION REQUIRED',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='One upload per team, about 28 sheets, caption required. Put the wall on screen and read three captions before showing the sheets: can the room guess what the twelve look like from "what this teaches"? Where the guess works, the dataset is an agreement; where it fails, it is a pile. Download the submissions; they come back in week 12 as examples of a process note, and the best three on the last slide of the course.'))

S.append(activity('3 — PAIRS OF TEAMS · CRITIQUE', 8, 'Swap draft posters. One fix each.',
                  ['Swap laptops with the team next to you. Their draft poster, your eyes; no explaining allowed.',
                   'Three metres: **say the product in one sentence** from the poster alone. One metre: **point at the decision** — the data, the line, the fallback, the no.',
                   'Write **one fix** on a sticky note, one sentence. Give it back. Read yours; do not argue; write it down.'],
                  bg=YELLOWS[2],
                  notes='Eight minutes, four each way. The protocol from chapter six: see, find, fix, no defending. The finding is usually the same at every table — the decision is a label, not a drawing — and hearing it from another team lands harder than hearing it from me. Teams without a draft yet critique the poster anatomy figure against their concept board and write the fix for themselves.'))

S.append(question('image_upload', 'Scribes only. The draft poster, and its one fix.',
                  hint='One image per team: your draft poster as it is today, however rough. Caption: the one fix the other team gave you, word for word.',
                  eyebrow_text='07 · CAPTURE 3 · IMAGE UPLOAD · ONE PER TEAM · CAPTION REQUIRED',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='One upload per team, caption required. Put the wall on screen for a minute and read four fixes without showing which poster: "draw the decision", "say who it is for", "where is the no", "the title is the company, not the product". The room hears that the fixes are the same four sentences, and that is the checklist for tonight. Amber downloads the drafts; they are the baseline for the mock session next week.'))

# ───────────────────────── 08 · debrief and homework ─────────────────────────
S.append(content('08 · WHAT JUST HAPPENED', 'You chose the outputs. You chose the examples. You answered for both.',
                 ['Curate: sixty-four tiles from one rule, and the three you kept had reasons a stranger could read. The rule could not rank them; you could. That is the authorship, and the law protects exactly that much of it.',
                  'Assemble: twelve of your own images, and a sentence saying what they agree on. What you put in is what comes out — and whose images, and whether they agreed, are the two questions for any model you will ever use.',
                  'Critique: someone else found your decision missing, and wrote the fix. The gate works better from outside the team; keep the swap until the fair.',
                  '**The machine made every one. You chose which, and from what. That was the design.**'],
                 body_size=30,
                 notes='Mirror of the whole day. The designer’s turn, in two verbs: choose the outputs, choose the examples — and the third that makes them yours: answer for both, in a process note. Say the last line slowly; it is the last line of weeks 1, 2 and 9 with the verbs changed. Then the homework, which is heavy this week.'))

S.append(cards('08 · DUE · BLACKBOARD', 'Two things tonight. Two for next week.', [
    ('DRAFT POSTER', 'Tonight.', 'A PDF of the A0, four zones present, however rough, with today’s fix applied or written on it. One submission per team.'),
    ('MEDIATION BRIEF', 'Tonight.', 'One page, five headings — relation, data, bias, guardrails, process note. Gaps marked with a question mark are fine; a missing heading is not.'),
    ('FINAL POSTER AND VIDEO', 'For week 12’s mock session.', 'The A0 at A3 for the mock, printed; the video, 3 to 5 minutes, six shots, on a link. Next week the class runs the fair once, without the jury.'),
    ('BEFORE WEEK 12', 'Watch, and read.', 'IBM’s Generative vs Rules-Based Chatbots on the playlist (next slide) — machine A and machine B, as two chatbots. And Van Den Eede (2011), In Between Us, on Blackboard: transparency and opacity.'),
], text_size=22, notes='Heavy week, said plainly. Tonight: draft and brief, one submission per team, so Amber can read them before the mock session. Next week: the mock fair — final poster at A3, video on a link — and it is a rehearsal with feedback, not a grade; the A0 print is for week 13. The video is eight minutes on the playlist; the reading is twenty pages and is the last one of the course. The TAs stay for 30 minutes and will read any brief brought to them.'))

S.append(video('08 · THE HOMEWORK · IBM TECHNOLOGY · ON THE PLAYLIST', 'Two chatbots. Two machines.', 'lZjUS_8btEo',
               ['IBM’s explainer of the two ways to build a chatbot: a decision tree of rules, or a language model. Machine A and machine B, as products that talk.',
                '- Watch for where each one fails: the rule that has no branch for your question; the model that answers fluently and wrongly.',
                '- Next week: language as an interface — trust, transparency, opacity, and the chatbot you design for your own product.'],
               thumb='yt/lZjUS_8btEo.jpg',
               notes='Eight minutes; the last video on the playlist. It is the week-1 distinction one more time, as two chatbots, and it is the lens for next week’s exercise: an assistant for your product, and whether it should be rules, a model, or rules around a model. Play the first minute if there is time. Cut if behind; it is homework either way.'))

S.append(end('See you next week. Language as an interface.',
             'Draft poster and brief tonight. Final poster and video next week.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: chatbots, agents, trust and opacity, the Turing test revisited, and the mock poster session — the last class before the fair. Homework in one line: draft and brief tonight, final poster and video next week, one video, one reading. The TAs stay for 30 minutes.'))

DECK = dict(title='SD2112 · AI in Design · Week 11', slides=finalize(S, FOOTER), pdf='SD2112-week11.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week11', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 5 September 2026 by web search and fetch; every date, number and quotation on the slides was checked against these)
# Belamy: https://en.wikipedia.org/wiki/Edmond_de_Belamy (sale, estimate, the eleven, WikiArt 14th–19th c., Obvious's members, Barrat at 19, the Verge line, the signature)
#   https://www.dezeen.com/2018/10/29/christies-ai-artwork-obvious-portrait-edmond-de-belamy-design/ (Prints & Multiples, 23–25 October 2018)
#   https://hyperallergic.com/christies-sells-ai-generated-art-for-432500-as-controversy-swirls-over-creators-use-of-copied-code/ (Barrat's tweet)
#   https://www.lrb.co.uk/blog/2018/november/fool-the-discriminator (Belamy / bel ami / Goodfellow)
#   video title via https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=Pu2GZ3du7PI&format=json
# Thaler v. Perlmutter: https://law.justia.com/cases/federal/appellate-courts/cadc/23-5233/23-5233-2025-03-18.html (D.C. Circuit, 18 March 2025)
#   https://www.mayerbrown.com/en/insights/publications/2026/03/supreme-court-denies-review-in-ai-authorship-case · https://www.scotusblog.com/cases/thaler-v-perlmutter/ (cert. denied 2 March 2026)
#   https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act
# Zarya of the Dawn: https://www.cooley.com/news/insight/2023/2023-02-28-us-copyright-office-grants-limited-registration-for-ai-generated-graphic-novel (letter of 21 February 2023)
#   the letter itself: https://www.copyright.gov/docs/zarya-of-the-dawn.pdf
# Copyright Office, Part 2 (29 January 2025): https://copyrightalliance.org/ai-report-part-2-copyrightability/
#   the report: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf
# Allen, Théâtre D'opéra Spatial: https://www.copyright.gov/rulings-filings/review-board/docs/Theatre-Dopera-Spatial.pdf (the 2023 refusal)
#   https://ipwatchdog.com/2025/08/28/ai-artist-challenges-copyright-office-denial-ai-assisted-work/ · https://www.thefashionlaw.com/resource-center-snapshot-jason-allen-v-perlmutter-et-al/
#   https://artificialinventor.com/copyright/ · https://www.courtlistener.com/docket/69198079/allen-v-perlmutter/ (filed 26 September 2024; briefed to early 2026; no ruling found by 5 September 2026)
# Hong Kong s.11(3) and the 2024 consultation: https://libguides.hkust.edu.hk/ai-literacy/copyright (the wording of s.11(3))
#   https://www.ipd.gov.hk/filemanager/ipd/en/share/consultation-papers/Eng-Copyright-and-AI-Consultation-Paper-20240708.pdf (8 July 2024)
#   https://www.mayerbrown.com/en/insights/publications/2024/10/a-new-chapter-hong-kong-proposes-introducing-copyright-exception-for-text-and-data-mining
#   https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3299206/hong-kong-lawmakers-raise-concerns-over-ai-safeguards-copyrighted-works (outcomes paper, 18 February 2025)
#   https://www.lexology.com/library/detail.aspx?g=a4d69199-0ade-4eb8-9c8f-c3d802b8d327 (no bill introduced by the end of 2025)
# Authors Guild v. Google: https://www.copyright.gov/fair-use/summaries/authorsguild-google-2dcir2015.pdf (2d Cir., 16 October 2015; cert. denied 2016)
# Bartz v. Anthropic: https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/district-court-rules-ai-training-can-be-fair-use-in-bartz-v-anthropic (23 June 2025, "exceedingly transformative")
#   https://authorsguild.org/advocacy/artificial-intelligence/what-authors-need-to-know-about-the-anthropic-settlement/ ($1.5 billion, about $3,000 a work)
#   https://www.jurist.org/news/2026/07/judge-approves-record-1-5-billion-settlement-involving-anthropic/ · https://www.authorsalliance.org/2026/07/21/bartz-v-anthropic-settlement-receives-final-approval/ (final approval, 20 July 2026)
# Kadrey v. Meta: https://authorsguild.org/news/meta-ai-ruling-meta-gets-technical-win-but-law-favors-authors/ (25 June 2025; the "wrong arguments" passage) · https://copyrightalliance.org/kadrey-v-meta-decision/
# Getty Images v. Stability AI (UK): https://www.lw.com/en/insights/getty-images-v-stability-ai-english-high-court-rejects-secondary-copyright-claim (4 November 2025)
#   https://www.judiciary.uk/judgments/getty-images-v-stability-ai/ · https://www.mayerbrown.com/en/insights/publications/2025/11/getty-images-v-stability-ai-what-the-high-courts-decision-means-for-rights-holders-and-ai-developers
# LAION-5B and Re-LAION-5B: https://laion.ai/blog/laion-5b/ (31 March 2022; 5.85 billion; "uncurated"; not for products) · https://laion.ai/blog/relaion-5b/ (2,236 links removed; the 1,008 of the Stanford report)
#   https://cyber.fsi.stanford.edu/news/investigation-finds-ai-image-generation-models-trained-child-abuse (December 2023)
#   https://www.techcrunch.com/2024/08/30/the-org-behind-the-data-set-used-to-train-stable-diffusion-claims-it-has-removed-csam
# Opt-outs: https://openfuture.eu/note/spawning-ai-announces-to-have-collected-opt-out-requests-for-80-million-artworks/ · https://the-decoder.com/artists-remove-80-million-images-from-stable-diffusion-3-training-data/
# LoRA: https://export.arxiv.org/api/query?id_list=2106.09685 (Hu et al., June 2021); dataset sizes from community guides: https://learn.rundiffusion.com/how-to-prepare-a-dataset-for-model-training-on-rundiffusion/
#   https://zsky.ai/blog/lora-training-guide · https://aiofm.info/en/guides/lora-complete-guide
# Van Den Eede (2011): https://api.crossref.org/works/10.1007/s10699-010-9190-y (Foundations of Science 16, 139–159)
# IBM video title via https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=lZjUS_8btEo&format=json
# Earlier weeks referred to on the slides: deck/week01.py (the chairs, the four roles), week03.py (told and shown chairs), week05.py (the three handles, LoRA),
#   week06.py (the three voice cases), week08.py (the anatomy of a decision), week09.py (the bias register, the red pen), week10.py (prototype v1, the homework)
