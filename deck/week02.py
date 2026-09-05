"""
SD2112 · Artificial Intelligence in Design · Week 02 — the slide spec.

    python deck/week02.py            # builds _site/week02/ (html deck + pdf), export/week02*.pptx, export/preview/
    python deck/week02.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Rules that make things: machine A (symbolic AI), instructions as art, Stuttgart 1965,
rules that grow, p5.js, prompts for coding (spec → model → code → picture), and the
activity "One spec, three executors". Every p5.js sketch on a slide has a Python twin in
tools/figures.py that draws the same rule; the html deck runs the sketches live.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures as F                                   # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, code_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY  # noqa: E402

FOOTER = 'SD2112 · AI IN DESIGN · WEEK 02'

# ───────────────────────── the code on the slides (p5.js) ─────────────────────────
TEN_CODE = """let pts = [];                        // the points

function setup() {
  createCanvas(600, 600);
  background(255);
  noLoop();                          // draw once
  for (let i = 0; i < 10; i++) {     // the rule: ten
    pts.push([random(600), random(600)]);    // chance
  }
}

function draw() {
  stroke(0);
  for (let a of pts) {               // every pair
    for (let b of pts) {
      line(a[0], a[1], b[0], b[1]);
    }
  }
  fill(0); for (let p of pts) circle(p[0], p[1], 6);
}"""

SCHOTTER_CODE = """const cols = 12, rows = 22, s = 30;  // Nees's numbers

function setup() {
  createCanvas(400, 700);
  background(255); noFill(); stroke(0);
  randomSeed(1968); noLoop();
}

function draw() {
  for (let r = 0; r < rows; r++) {   // rows
    let k = r / (rows - 1);          // 0 top, 1 bottom
    let d = k * s / 2, a = k * PI / 4;  // shift, turn
    for (let c = 0; c < cols; c++) { // columns
      push();
      translate(20 + s * (c + 0.5), 20 + s * (r + 0.5));
      translate(random(-d, d), random(-d, d)); // chance
      rotate(random(-a, a));                   // chance
      square(-s / 2, -s / 2, s);
      pop();
    }
  }
}"""

WALK_CODE_A = """const n = 20, s = 28;             // the raster: 20 x 20
const drift = [1, 3, 3, 4, 2];    // each sign's neighbour
let last = 0;                     // the previous sign

function next() {                 // the chain: one step
  let p = random();               // one throw of the die
  if (p < 0.6) return last;       // stay: 60%
  if (p < 0.85) return drift[last];   // drift: 25%
  return floor(random(5));        // jump: 15%
}

function sign(k, x, y) {          // the repertoire
  if (k == 1 || k == 3) line(x + 4, y + 14, x + 24, y + 14);
  if (k == 2 || k == 3) line(x + 14, y + 4, x + 14, y + 24);
  if (k == 4) square(x + 8, y + 8, 12);
}"""

WALK_CODE_B = """function setup() {
  createCanvas(600, 600);
  background(255); stroke(0); noFill();
  noLoop();
}

function draw() {                      // the walk
  for (let r = 0; r < n; r++) {        // row by row
    for (let c = 0; c < n; c++) {      // cell by cell
      last = next();                   // the next sign
      sign(last, 20 + c * s, 20 + r * s);
    }
  }
}"""

WALK_CODE = WALK_CODE_A + '\n\n' + WALK_CODE_B

LEWITT_CODE = """const n = 50;                          // fifty points
let pts = [];

function setup() {
  createCanvas(800, 500);              // a wall
  background(255); stroke(0); noLoop();
  randomSeed(118);
  // evenly distributed: one point per cell
  // of a 10 x 5 grid, at random inside it
  let cols = 10, rows = 5;
  let w = width / cols, h = height / rows;
  for (let i = 0; i < n; i++) {
    let c = i % cols, r = floor(i / cols);
    pts.push([c * w + random(w), r * h + random(h)]);
  }
}

function draw() {
  for (let a of pts)                   // all connected
    for (let b of pts)
      line(a[0], a[1], b[0], b[1]);
}"""

# ───────────────────────── interaction in the html deck (not shown on the code panels) ─────────────────────────
# Appended to the sketch pages only: the code above stays what the students type; the mouse becomes the number.
TEN_EXTRA = """function mousePressed() {            // new dice, same rule
  pts.length = 0;
  for (let i = 0; i < 10; i++) pts.push([random(600), random(600)]);
  background(255); redraw();
}"""

SCHOTTER_EXTRA = """let gain = 1, moved = false;        // how much disorder: the mouse is the number
function draw() {
  background(255);
  if (moved) gain = constrain(map(mouseX, 0, width, 0, 2), 0, 2);
  for (let r = 0; r < rows; r++) {
    let k = r / (rows - 1) * gain;
    let d = k * s / 2, a = k * PI / 4;
    for (let c = 0; c < cols; c++) {
      push();
      translate(20 + s * (c + 0.5), 20 + s * (r + 0.5));
      translate(random(-d, d), random(-d, d));
      rotate(random(-a, a));
      square(-s / 2, -s / 2, s);
      pop();
    }
  }
  noStroke(); fill(0); textSize(13); textFont('JetBrains Mono');
  text('disorder x ' + nf(gain, 1, 2), 20, 690); stroke(0); noFill();
}
function mouseMoved() { moved = true; randomSeed(seed); redraw(); }
let seed = 1968;
function mousePressed() { seed = floor(random(1e6)); randomSeed(seed); redraw(); }"""

WALK_EXTRA = """let stay = 0.6, moved = false;      // the mouse sets the table: y = how sticky
function next() {
  if (moved) stay = constrain(map(mouseY, 0, height, 0.92, 0.1), 0.1, 0.92);
  let p = random();
  if (p < stay) return last;
  if (p < stay + (1 - stay) * 0.6) return drift[last];
  return floor(random(5));
}
function mouseMoved() { moved = true; background(255); last = 0; redraw(); label(); }
function mousePressed() { background(255); last = 0; redraw(); label(); }
function label() {
  noStroke(); fill(0); textSize(13); textFont('JetBrains Mono');
  text('stay ' + round(stay * 100) + '% · drift ' + round((1 - stay) * 60) + '% · jump ' + round((1 - stay) * 40) + '%', 20, 592);
  stroke(0); noFill();
}"""

LEWITT_EXTRA = """function mousePressed() {            // the same words, new dice
  pts.length = 0;
  let cols = 10, rows = 5, w = width / cols, h = height / rows;
  for (let i = 0; i < n; i++) {
    let c = i % cols, r = floor(i / cols);
    pts.push([c * w + random(w), r * h + random(h)]);
  }
  background(255); redraw();
}"""

TEMPLATE = [
    'Write a p5.js sketch for the web editor.',
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

SPEC_TEN = [
    'THE SPEC', ' ',
    'On a sheet of paper, using a pencil,', 'place ten points at random.', ' ',
    'The points should be evenly distributed', 'over the area of the sheet.', ' ',
    'All of the points should be connected', 'by straight lines.', ' ',
    '— after Sol LeWitt, Wall Drawing 118, 1971',
]

SPEC_FILLED = [
    'Write a p5.js sketch for the web editor.', ' ',
    'RULE: place ten points at random; the points', 'should be evenly distributed over the canvas;', 'all of the points should be connected by', 'straight lines.', ' ',
    'CHANCE: the position of each point.', ' ',
    'NUMBERS: canvas 600 x 600, white background,', 'black stroke 1 px.', ' ',
    'CONSTRAINTS: plain p5.js, no libraries, draw', 'once (noLoop), randomSeed(1), nothing else.', ' ',
    'OUTPUT: the whole sketch.js, nothing else.',
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

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 02 · LECTURE + WORKSHOP',
               'Rules that make things.',
               'Week 2 — machine A, p5.js, and a machine that writes rules.',
               notes='Join code on screen from 30 minutes before. Laptops out from the start: the second half is hands-on. The TAs have been pairing people without a laptop with people who have one.'))

S.append(agenda('SD2112 · WEEK 02', [
    'Last week, in your words', 'Machine A: rules', 'Instructions as art', 'Rules make pictures',
    'Rules that grow', 'p5.js: a sketchbook that executes', 'Specs, and prompts for coding', 'Activity: one spec, three executors',
], notes='Eight stops. The first five are the lecture: what a rule is, and sixty years of people making art and design from rules — before and after computers. Break. Then the workshop: p5.js, a language model that writes p5.js from your words, and the activity, where the same forty words get executed by your hand, by a model, and then your own rule.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the cloud · the worries · the cups', notes='Five minutes of recap, from the data you gave us.'))

S.append(question('multiple_choice', 'Before we start: what do you have with you?', [
    'A laptop and a p5.js account', 'A laptop, no account yet', 'Only a phone', 'Nothing today',
], eyebrow_text='01 · LOGISTICS · MULTIPLE CHOICE',
    notes='ClassPoint. The workshop needs one laptop with a p5.js account per pair. Cs and Ds move next to As now, not at the break; the TAs walk the room while the next two slides run. An account takes one minute at editor.p5js.org.'))

S.append(cards('01 · YOUR WORRIES · AND THE WEEK THAT ANSWERS THEM', 'You worried about five things.', [
    ('CHEATING', 'Allowed, disclosed, yours.', 'The rule from week 1 stands: use any model, say which, answer for it. Week 11 is authorship: who made Belamy?'),
    ('LOSING SKILLS', 'Five small makes.', 'Weeks 2 to 6: one thing a week where your hand stays on the rule. Today is the first.'),
    ('COPYRIGHT', 'Week 11.', 'Datasets, LoRAs, the Thaler cases, what a court calls transformative.'),
    ('JOBS', 'Weeks 8 and 12.', "The designer's turn: what is left when the model makes the artefact. Curator, briefer, guardrail-setter."),
    ('BEING LIED TO', 'Weeks 4 and 9.', 'Hallucination and sycophancy in week 4. Bias, data and privacy in week 9.'),
], text_size=22, notes='Replace these five with the real ones: open the slide-19 answers from last week before class and read three worries aloud, then point each at its week. The point is that every worry in the room is on the syllabus. Then the hopes, briefly: most of them are week 4 and 5.'))

S.append(figure_slide('01 · THE CUPS', 'Prompts were rules. The model had the examples.', F.two_machines(),
                      body=['A hundred first cups: white, ceramic, a handle; nobody typed "handle". Your prompts were rules, and the model pulled every cup back to its middle. Today: the rules side, on its own.'],
                      caption='Machine A: write the rule. Machine B: show the examples. This week is the left half; next week the right.',
                      notes='Show the cup wall from last week if you have the screenshot. The prototype was the dataset\'s, not Hong Kong\'s. Then: today we stay entirely on the left. No model learns anything today — except in the last hour, where a language model writes machine A for you.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(0, 1),
                 notes='Week 2 of module one. Next week, examples; then the three tool weeks. Challenge 1 is today; awards next week.'))

# ───────────────────────── 02 · machine A ─────────────────────────
S.append(section('02', 'Machine A', 'symbolic AI · 1956 – today · if this, then that', bg=INK,
                 notes='Chapter two: what a rule is, sixty years of rule-based AI in one chapter, and why every designer already writes rules.'))

S.append(question('short_answer', 'Write a rule for drawing a house.',
                  hint='One sentence. A stranger who has never seen a house must be able to follow it.',
                  eyebrow_text='02 · QUESTION · SHORT ANSWER',
                  notes='Ninety seconds. Read four aloud. Every rule leaves things open: size, roof angle, where the door is, whether there is a chimney. Two people following the same rule draw two houses. That gap, between what you said and what you meant, is the subject of the whole day. Keep the answers: the activity comes back to them.'))

S.append(figure_slide('02 · A RULE', 'If this, then that. Nothing else.', F.decision_tree(),
                      body=['A rule is a condition and a consequence. A computer is a machine that follows rules exactly, forever, without judgement: Turing, 1936. Newell and Simon, 1976: intelligence is symbols plus search — rules, applied to rules.'],
                      caption='Symbolic AI: knowledge written down as rules, applied by a program. Exact, explainable, and it has never heard of the Tulip chair.',
                      notes='Three questions in a row decide "chair". Walk the room through it. Then the pedestal chair: one leg, and the rule says no. You can add a rule for it — and then a beanbag arrives. Every fix is another rule written by hand. Hold that thought until the expert systems.'))

S.append(cards('02 · SIXTY YEARS OF MACHINE A', 'Rules were the first AI.', [
    ('1956 · DARTMOUTH', 'AI gets its name.',
     'McCarthy, Minsky, Shannon and Rochester spend a summer on "making machines use language, form abstractions and concepts". Newell and Simon bring the Logic Theorist: a program that proves theorems from Russell and Whitehead.'),
    ('1966 · ELIZA', 'Two hundred rules pass for a therapist.',
     'Weizenbaum\'s script matches a keyword and echoes the sentence back. "I am sad" becomes "How long have you been sad?" His secretary asked him to leave the room so she could talk to it in private.'),
    ('1972 – 1986 · EXPERT SYSTEMS', 'Rules run a business. Then the winter.',
     'MYCIN: about 600 rules diagnose blood infections as well as Stanford\'s specialists. XCON: 10,000 rules configure every computer DEC sells. Then the boom ends: someone has to write, and maintain, every single rule.'),
], text_size=22, notes='Three moments. Dartmouth: the name and the bet — everything about intelligence can be described precisely enough for a machine. ELIZA: the first chatbot, and the first proof that people will talk to rules. Expert systems: rules made money, then the knowledge bottleneck: every rule hand-written by an engineer interviewing an expert. Machine B — learning the rules from examples — is the answer to that bottleneck. Week 3.'))

S.append(two_col('02 · ELIZA · 1966', 'A rule that feels like a person.',
                 ['The script: find a keyword, apply its rule, echo the rest back. No memory, no meaning.',
                  '- **"I am X"** → "How long have you been X?"',
                  '- **"my mother"** → "Tell me more about your family."',
                  'Built to show how shallow this is; people confided in it anyway. Week 12: rule-based versus generative chatbots.'],
                 ELIZA, right_size=24,
                 notes='The transcript is from Weizenbaum\'s 1966 paper; ELIZA in capitals. Every reply is a rule you can read: "you X" becomes "why do you X". Ask: does it understand? No. Does it behave intelligently, by our week-1 definition? Enough to fool people. Intelligent-like behaviour through computation — and here you can read every line of the computation.'))

S.append(cards('02 · THE DEAL', 'Exact. Explainable. Brittle.', [
    ('EXACT', 'Same input, same output.',
     'A rule does the same thing every time. Even chance can be made repeatable: give the die a seed and the same picture comes back, on any machine, forever.'),
    ('EXPLAINABLE', 'You can point at the line that decided.',
     'Every output has a reason you can read. When a rule-based product does something strange, you can find out why. Machine B cannot say why — next week.'),
    ('BRITTLE', 'Nothing outside the rule can appear.',
     'The definition does not know beanbags exist. Every new case needs a new rule, written by hand: the knowledge bottleneck that ended the expert-systems boom.'),
], notes='The deal you make with machine A. All three come from the same fact: the rule is all there is. For the reflection, this is the vocabulary: rule-based versus adaptive. Ask the room for a rule-based feature they love and one they hate; auto-correct usually comes up on both sides.'))

S.append(cards('02 · YOU ALREADY WRITE RULES', 'Every designer already writes machine A.', [
    ('THE GRID', 'Snap to 8 px.', 'Columns, gutters, a spacing scale: a rule you set once and every screen obeys.'),
    ('THE BREAKPOINT', 'Narrower than 600 px? One column.', 'An if-then you have written, in words, for a developer to execute.'),
    ('THE SYSTEM', 'One button, every state.', 'Tokens, variants, auto layout: a rule-based machine that makes every button in the product.'),
    ('THE SPEC', 'Redlines, briefs, handoffs.', 'A rule written in words for a human executor. Today you write one for a machine — and then for a machine that writes machines.'),
], text_size=24, notes='Designers are fluent in machine A and do not call it that. A design system is an expert system for buttons. A responsive layout is a rule. The spec is the one that matters today: a rule in words, for someone else to execute. The whole second half is about writing that well.'))

S.append(question('multiple_choice', 'Which of these is machine A, pure rules?', [
    'Face ID unlocking your phone', 'Figma snapping a box to the grid', 'The For You feed on TikTok', 'Generative Fill in Photoshop',
], eyebrow_text='02 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. The other three learned from examples. A snap is a rule you could write on a napkin: if the edge is within 4 px of a grid line, move it there. Ask: which of the four could you explain to a client, line by line? Only B. That is the deal.'))

# ───────────────────────── 03 · instructions as art ─────────────────────────
S.append(section('03', 'Instructions as art', '1959 – 1971 · scores, events, wall drawings', bg=PINKS[0],
                 notes='Chapter three: before computers made art from rules, artists did — by writing the rule and handing the execution to someone else.'))

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
               notes='Play a minute if there is time. The design point: Tinguely built the rule and then had no control over the execution — and the failure is part of the piece. Every rule you write for a machine will surprise you in execution. Cut this slide if behind.'))

S.append(video('03 · KAPROW · 1967 · PASADENA 2008 · BERLIN 2015', 'Instructions executed by strangers, decades later.', 'RZ_FAgfJsss',
               ['Fluids, 1967. The whole score: "During three days, about twenty rectangular enclosures of ice blocks (measuring about 30 feet long, 10 wide and 8 high) are built throughout the city. Their walls are unbroken. They are left to melt."',
                '- Kaprow called every re-execution a reinvention. Each one is the piece.',
                '- The spec is the artwork. The execution is delegated — and it is still the work.'],
               thumb='yt/RZ_FAgfJsss.jpg', body_size=28,
               notes='Forty-three words. Los Angeles, 1967; Pasadena, 2008; Berlin and Los Angeles, 2015 — built by people Kaprow never met, after his death. Ask: who is the author of the Berlin one? Same answer as for a wall drawing, next slide, and the same answer we will give for code a model writes from your spec.'))

S.append(quote('"The idea becomes a machine that makes the art."',
               'Sol LeWitt, Paragraphs on Conceptual Art, Artforum, June 1967', size=96,
               notes='The full sentence: "When an artist uses a conceptual form of art, it means that all of the planning and decisions are made beforehand and the execution is a perfunctory affair. The idea becomes a machine that makes the art." Machine A, in a sentence, from an artist who never touched a computer.'))

S.append(statement('On a wall surface, any continuous stretch of wall, using a hard pencil, place fifty points at random. The points should be evenly distributed over the area of the wall. All of the points should be connected by straight lines.',
                   eyebrow_text='03 · SOL LEWITT · WALL DRAWING 118 · 1971 · THE WHOLE WORK', size=68, bg=PAPER,
                   notes='This is the entire artwork. First drawn in December 1971 at the Museum School in Boston by five art students, without LeWitt. Read it as a spec: an object, a tool, a count, a placement, an action. And two words that fight each other — "at random" and "evenly distributed". The activity at the end starts from these forty-five words.'))

S.append(figure_slide('03 · WALL DRAWING 118 · EXECUTED BY A PYTHON SCRIPT, TODAY', 'Fifty points. 1,225 lines. Any wall.', F.lewitt_118(),
                      body=['Every execution is the work. The drafters decide what the words left open: the pencil, the wall, what "random" means. A museum buys the instructions and a certificate; the drawing is redrawn, by other hands, each time it is shown.'],
                      caption='The same forty-five words, executed by a program instead of five art students. LeWitt: "Each person draws a line differently and each person understands words differently."',
                      notes='Our execution: fifty points, one per cell of a jittered grid, so that "evenly distributed" and "at random" both hold. The drafters in Boston made the same decision with their eyes. Point at the quote: it is the spec-writer\'s problem in one sentence, and it is why a language model given the same words will give you something else. Executions of 118 exist in dozens of museums; none match.'))

S.append(content('03 · VERA MOLNÁR · 1959 – 1976', 'She executed her algorithms by hand for nine years.',
                 ['Machine imaginaire: from 1959 Molnár wrote procedures — a grid, a rule, a small dose of chance — and executed them herself, on paper, step by step, before she had access to a computer.',
                  '- 1968: her first plotter. The rule did not change. The executor did.',
                  '- (Dés)ordres, 1974: nested squares in a grid, and a small probability that any corner is nudged. Find the disorder.',
                  'A spec written for a machine that does not exist yet is still a spec.'],
                 figure=F.molnar_desordres(), caption='After Molnár: nested squares, every corner nudged with a small probability. Our execution, her rule.',
                 body_size=28,
                 notes='Molnár is the bridge between the wall drawing and the plotter: the same person, the same rules, two executors. She called her early method the imaginary machine. The lesson for the activity: you can execute a rule by hand to understand it before you hand it to anything else. That is round one.'))

# ───────────────────────── 04 · rules make pictures ─────────────────────────
S.append(section('04', 'Rules make pictures', 'Stuttgart 1965 · Bense · Nees · Nake · the plotter',
                 notes='Chapter four: the first computer art, and two rules worth knowing by heart — Schotter and Walk-Through-Raster.'))

S.append(content('04 · MAX BENSE · INFORMATION AESTHETICS', 'Beauty, measured. Art, generated.',
                 ['Birkhoff, 1933: aesthetic measure = order ÷ complexity. Bense, Stuttgart, 1950s: if aesthetics is information, it can be programmed.',
                  '- February 1965: Georg Nees shows plotter drawings in Bense\'s seminar gallery. Bense calls it artificial art. The first computer art exhibition, anywhere.',
                  '- A painter asks Nees whether the machine could draw the way he does. Nees: "Yes — if you tell me how you draw."',
                  'November 1965: Nake and Nees, Galerie Niedlich. This one hangs in the V&A.'],
                 image='nake-homage-to-paul-klee-1965.jpg', fit='contain',
                 caption='Frieder Nake, Hommage à Paul Klee 13/9/65 Nr.2, 1965. Zuse Graphomat Z64 plotter, programmed in ALGOL.',
                 body_size=28,
                 notes='Bense\'s claim: aesthetics is not taste, it is measurable order in a signal — and therefore generatable. The Nees anecdote is the whole lecture: the painter could not say how he drew, so the machine could not do it. Nake\'s Klee is on the wall from week 1; today we open the two rules behind pictures like it.'))

S.append(content('04 · GEORG NEES · SCHOTTER · c. 1968', 'One rule. One random number.',
                 ['Twelve columns, twenty-two rows of squares. Each square is moved and turned by a random amount, and the amount grows with the row.',
                  '- Row 0: a perfect grid. Row 21: gravel. Schotter means gravel.',
                  '- The rule decides everything except two numbers per square. Chance is confined; the picture is order becoming disorder.',
                  'This is the shape of the weekly challenge: one rule, one place where chance enters, your picture.'],
                 figure=F.schotter(), caption='After Nees: our execution of his rule. Siemens 4004, ALGOL, Zuse Graphomat; the original print is 28 × 22 cm.',
                 body_size=28,
                 notes='Say the rule in one breath: a grid; each square shifts and turns by a random amount that grows down the page. Nees\'s picture is order decaying into disorder — Bense\'s two words, in one image. Ask: where is the design decision? In the rule and in the rate of decay, not in any square. We will write this in p5.js after the break.'))

S.append(question('multiple_choice', 'Where does chance enter in Schotter?', [
    'Which squares are drawn', 'How far each square moves and turns', 'The colour of the ink', 'The number of rows',
], eyebrow_text='04 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. Everything else is the rule. This is the question to ask of every generative piece you will meet: where, exactly, is the die thrown — and how much is it allowed to move?'))

S.append(figure_slide('04 · FRIEDER NAKE · WALK-THROUGH-RASTER · 1966', 'A raster, a repertoire, a chain, a walk.', F.walk_breakdown(),
                      body=['Four steps. A grid of cells. A small repertoire of signs. A chain of signs, each chosen from the one before it by a table of probabilities — a Markov chain. Then the chain is poured into the raster, cell by cell, from the top left.'],
                      caption='Nake, Walk-Through-Raster, series 2.1–4, 1966: ALGOL 60, Zuse Graphomat Z64. Four prints from one program. Nake finished a PhD in probability theory the year after.',
                      notes='Break it down slowly; this is the model for every generative piece. One: the raster is the stage. Two: the repertoire is the vocabulary — Nake\'s signs were his own; ours are five. Three: the chain is where the aesthetic lives: the next sign depends on the last one, so runs of the same sign appear and fields form; change the table and the whole texture changes. Four: the mapping is the walk — the chain is written into the cells in order. The random numbers only ever choose from the table. Series 2.1 to 2.4 are four runs of the same program.'))

S.append(code_slide('04 · WALK-THROUGH-RASTER · THE CHAIN AND THE REPERTOIRE', 'The next sign depends on the last one.', WALK_CODE_A, F.walk_through_raster(),
                    caption='Our execution, after Nake. The table — stay 60%, drift 25%, jump 15% — is the whole aesthetic. Change it and the fields dissolve or freeze.',
                    code_size=19, sketch=live('walk-through-raster', WALK_CODE, 600, 600, hint='mouse y = how sticky · click = new dice', extra=WALK_EXTRA),
                    notes='Two functions. next() is the Markov step: one throw of the die, three outcomes, and the outcome depends on last. sign() is the repertoire: nothing, a horizontal, a vertical, both, a small square. In the html deck this runs live: every visit to the slide is a new chain.'))

S.append(code_slide('04 · WALK-THROUGH-RASTER · THE WALK', 'The walk writes the chain into the cells.', WALK_CODE_B, F.walk_through_raster(),
                    caption='Two loops walk the raster, row by row, cell by cell. At every cell the chain advances one step and the sign is drawn. Four hundred cells, four hundred throws of the die.',
                    code_size=21, sketch=live('walk-through-raster-2', WALK_CODE, 600, 600, hint='mouse y = how sticky · click = new dice', extra=WALK_EXTRA),
                    notes='The mapping in Nake\'s words: the first sign goes into the top-left cell, the second into the next, and so on. Ask what would change if the walk went down the columns instead — the fields would run vertically. The picture is the rule plus the walk plus the dice; only the dice are not yours.'))

S.append(video('04 · HILLER & ISAACSON · UNIVERSITY OF ILLINOIS · 1957', 'A computer writes a string quartet.', 'n0njBFLQSk8',
               ['The Illiac Suite: the ILLIAC generates random notes and keeps the ones that pass the rules of counterpoint. Generate and test — the oldest move in symbolic AI.',
                '- The fourth movement chooses notes with a Markov chain: the next note depends on the last. Nake\'s signs, nine years earlier, in sound.',
                '- On the playlist. Sixteen minutes, four experiments, one machine.'],
               thumb='yt/n0njBFLQSk8.jpg',
               notes='Rules make music too. The generate-and-test loop — propose at random, reject what breaks a rule — is the engine of a great deal of rule-based AI, and of most generative art. Week 6 comes back to sound with machine B. Cut if behind.'))

S.append(figure_slide('04 · 1982 · 10 PRINT CHR$(205.5+RND(1)); : GOTO 10', 'One line of code. One coin toss. A maze.', F.ten_print(),
                      body=['The smallest generative program there is: print one of two diagonals, chosen by a coin toss, forever. Its rule fits in a message, its chance is a single random number, and it never draws the same maze twice.'],
                      caption='One line of Commodore 64 BASIC, from the machine\'s user guide. Thirty years later it got a book (Montfort et al., 10 PRINT, MIT Press, 2013).',
                      notes='If Schotter is too much, this is the floor: one rule, one random number, and it is already a picture. Everyone in the room can hold this whole program in their head. That is the size of rule to start from in the challenge.'))

# ───────────────────────── 05 · rules that grow ─────────────────────────
S.append(section('05', 'Rules that grow', 'recursion · L-systems · parameters', bg=ORANGES[0],
                 notes='Chapter five, short: two more kinds of rule designers use — rules applied to their own output, and rules with the numbers left open.'))

S.append(figure_slide('05 · LINDENMAYER · 1968', 'One rule, applied to its own output.', F.lsystem_growth(),
                      body=['Rewrite every F with the rule, then rewrite the result, and again: four generations from one line. Lindenmayer, a biologist, wrote it for algae. Fractals are the same trick: a short rule, an endless picture.'],
                      caption='F → F[+F]F[-F]F, turn 25.7°. Lindenmayer 1968; Prusinkiewicz & Lindenmayer, The Algorithmic Beauty of Plants, 1990; Mandelbrot, The Fractal Geometry of Nature, 1982.',
                      notes='F means draw forward; + and − turn; the brackets save and restore the position — a branch. Apply the rule four times and you have 81 segments on the trunk. Grasshopper, Houdini and every procedural-generation tool in games are this: rules that call themselves.'))

S.append(content('05 · PARAMETRIC DESIGN', 'Machine A, with sliders.',
                 ['A rule with numbers left open is a design space. Change a number, get a design; every one obeys the rule.',
                  '- Grasshopper, 2007: architecture as a graph of rules. A tower is a rule and a hundred numbers.',
                  '- The MIT Media Lab identity, 2011: one algorithm, forty thousand logos, one per person.',
                  '- Nervous System, Kinematics dress, 2014: a rule folds itself around a body.',
                  'The twelve chairs from week 1 are the same idea: chair(seat, back, angle, legs).'],
                 figure=F.parametric_chairs(), caption='Week 1: one function, twelve chairs. Parametric design is a rule you can ship.',
                 body_size=28,
                 notes='Same chairs as last week, now with the vocabulary: parameters. The design work moves from the artefact to the rule and to choosing the numbers. Ask product designers in the room what they parametrise already; ask communication designers about their grids. Same thing.'))

S.append(figure_slide('05 · VARIABLE FONTS · 2016', 'One font, one number.', F.weight_ramp(),
                      body=['A letter is a rule with a parameter. Type designers have written machine A for a century: hinting, kerning, optical sizes. A variable font puts the number in your hands. This is Inter, the typeface of these slides, along its weight axis.'],
                      caption='Inter Variable, wght 100 to 900. OpenType 1.8, 2016: Adobe, Apple, Google and Microsoft, together for once.',
                      notes='For the communication designers: the closest rule-based machine to your daily work. One file, every weight, and the in-betweens that never existed as drawings. In the html deck this line is live text; drag the weight in your browser\'s inspector if you want to see it move.'))

S.append(statement('A rule is a design. The execution can be delegated.', eyebrow_text='05 · WHERE WE ARE', size=110,
                   notes='The sentence to carry across the break. LeWitt delegated to drafters, Nees to a plotter, Molnár to herself. After the break you delegate to p5.js, and then to a language model. The design is the rule.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · P5.JS · THEN A MACHINE THAT WRITES RULES', size=120, bg=PAPER,
                   notes='1:30. Laptops charged, editor.p5js.org open, logged in. The TAs help anyone without an account now.'))

# ───────────────────────── 06 · p5.js ─────────────────────────
S.append(section('06', 'p5.js', 'a sketchbook that executes · editor.p5js.org · no install', bg=INK,
                 notes='Chapter six, hands-on: the tool, fifteen lines, and Schotter in twenty.'))

S.append(content('06 · PROCESSING → P5.JS', 'Code as a sketchbook.',
                 ['1999: John Maeda\'s Design By Numbers at the MIT Media Lab: a language small enough for designers.',
                  '- 2001: Casey Reas and Ben Fry, Maeda\'s students, make Processing, "a software sketchbook".',
                  '- 2013: Lauren McCarthy starts p5.js: Processing for the browser. 2018: the web editor. A free account, nothing to install.',
                  '- Why it is here: the whole rule fits on one screen, and the picture is instant.'],
                 figure=F.lewitt_ten(seed=7), caption='Ten points at random, all connected: twenty lines of p5.js. Next slide.',
                 body_size=28,
                 notes='Processing is the tool every generative artist of the last twenty years learned on; p5.js is the same thing in a browser tab. We use the web editor so that nobody installs anything. If someone knows Python or JavaScript already, fine; the vocabulary today is ten words.'))

S.append(code_slide('06 · ANATOMY', 'setup() runs once. draw() runs the rule.', TEN_CODE, F.lewitt_ten(seed=7),
                    caption='(0,0) is the top-left corner; y grows downwards; random(600) is a number between 0 and 600. noLoop() draws once instead of sixty times a second.',
                    sketch=live('ten-points', TEN_CODE, 600, 600, hint='click = new dice', extra=TEN_EXTRA),
                    notes='Read it top to bottom. setup: make a canvas, paint it white, say "once", then the rule: ten times, push a point at a random place. draw: for every pair, a line; then a dot on every point. Ten words: createCanvas, background, noLoop, for, random, push, stroke, line, fill, circle. That is the whole vocabulary for today.'))

S.append(figure_slide('06 · RANDOM() · RANDOMSEED()', 'Same rule, three seeds.', F.lewitt_seeds(),
                      body=['random(600) is a number between 0 and 600, different every run. randomSeed(1) loads the die: the same picture every run, on every machine. Where you call random() is where the rule lets go; everything else is the rule.'],
                      caption='Three runs of the ten-point sketch with randomSeed(1), (2) and (3). Change the seed, keep the rule: a new picture that is still yours.',
                      notes='The seed is what makes machine A with chance still exact — Cage tossing coins, but with the coins recorded. For the challenge: a seed means you can show the exact picture you chose. For the reflection: this is the difference between a rule-based and an adaptive system in one function call.'))

S.append(code_slide('06 · SCHOTTER · IN P5.JS', 'A grid is two loops. Disorder is one number.', SCHOTTER_CODE, F.schotter(),
                    caption='Twenty lines. The outer loop walks the rows, the inner loop the columns; k grows from 0 to 1 down the picture and scales both the shift and the turn.',
                    code_size=21, sketch=live('schotter', SCHOTTER_CODE, 400, 700, hint='mouse x = disorder · click = new dice', extra=SCHOTTER_EXTRA),
                    notes='Two loops make a grid — say that sentence twice, it is the most useful thing in generative art. push/translate/rotate/pop: move the pen to the cell, nudge it, turn it, draw a square, come back. The chance is two lines. Nees wrote this in ALGOL for a plotter; you have it in a browser tab.'))

S.append(figure_slide('06 · CHANGE ONE NUMBER', 'The same rule. Which one is yours?', F.schotter_variations(),
                      body=['This is the whole craft of the weekly challenge: write one rule, then find the one number that makes it yours.'],
                      caption='Left: Nees\'s numbers. Middle: the disorder tripled. Right: eight rows instead of twenty-two. Nothing else changed.',
                      notes='Three sketches, one rule, one number each. The design decision is the number, and taste is choosing it. Ask the room which of the three they would print. Then: type it.'))

S.append(activity('LIVE', 6, 'Type it. Run it.',
                  ['Open **editor.p5js.org** and log in. Replace everything in the editor with the twenty lines on the right.',
                   'Press play. You should see ten points and forty-five lines.',
                   'Change **10** to **30**. Play again. Then change one **600** to **200**, and see what breaks.'],
                  eyebrow_text='06 · HANDS ON', panel=TEN_CODE.splitlines(), panel_size=21,
                  notes='Six minutes; the TAs walk. Typical errors: a missing bracket, Random with a capital R, a stray semicolon. The last step is the point: a rule you can break on purpose is a rule you understand. Anyone finished early: make the lines grey, then make the points bigger than the lines.'))

S.append(question('multiple_choice', 'Did it run?', [
    'Yes, first time', 'After fixing an error', 'Not yet — help', 'I am on my phone',
], eyebrow_text='06 · PULSE · MULTIPLE CHOICE',
    notes='Pulse check. Cs get a TA now. Ds pair with an A for the rest of the class; the activity needs one laptop per pair.'))

# ───────────────────────── 07 · prompts for coding ─────────────────────────
S.append(section('07', 'Prompts for coding', 'machine B writes machine A · spec → code → picture',
                 notes='Chapter seven: the other executor. A language model turns your words into p5.js in seconds. That makes the words the work.'))

S.append(figure_slide('07 · THE SPEC IS THE DESIGN', 'One spec. Three executors.', F.spec_pipeline(),
                      body=['LeWitt\'s drafters; you, in the editor; a language model on genai.polyu.edu.hk. Same words, delegated execution, and never quite what you meant. Machine B writes machine A — and machine A does exactly what it is told.'],
                      caption='A language model is not a rule: the same prompt gives different code every time. The code it writes is a rule: the same seed gives the same picture every time.',
                      notes='Name the two machines in the pipeline. The model (B) is a translator from words to rules; the sketch (A) is the rule. Everything we said about machine A applies to the code: exact, readable, brittle. Everything about machine B applies to the model: fluent, typical, cannot say why. The spec is your handle on both.'))

S.append(cards('07 · ANATOMY OF A SPEC', 'Five things a rule must say.', [
    ('WHAT', 'The rule, in one sentence.', 'Like LeWitt: an object, a count, an action. "A grid of squares, each moved and turned by a random amount that grows with its row."'),
    ('CHANCE', 'Where the die is thrown.', 'Say exactly what is random and how much. "Up to half a cell and 45 degrees in the last row, nothing in the first."'),
    ('NUMBERS', 'Canvas, counts, sizes, colours.', 'Give them, or say "choose". A model that has to guess guesses the middle: 400 × 400, pastel, particles.'),
    ('CONSTRAINTS', 'The rules about the rule.', 'p5.js in the web editor. No libraries. Draw once. A seed, so it repeats. Nothing you did not ask for.'),
    ('OUTPUT', 'What to hand back.', 'The whole sketch, nothing else. Then: "describe the rule this code follows in one sentence" — a check that it understood.'),
], text_size=21, notes='Five headings. They are also the five things the room\'s house rules left out at the start of the class. Show how LeWitt\'s forty-five words cover the first three and leave the last two to the wall. A spec for a machine needs all five.'))

S.append(two_col('07 · THE TEMPLATE', 'A prompt that is a spec.',
                 ['Copy it, fill the brackets, paste it into a language model on **genai.polyu.edu.hk**. Paste what comes back into **editor.p5js.org**.',
                  '- Rule first, constraints last: models obey the end of a prompt more than the middle.',
                  '- One rule per prompt. Two ideas are two sketches.',
                  'Keep the spec. When the code drifts, paste the spec again — not the code.'],
                 TEMPLATE, right_size=23, left_size=30,
                 notes='The template is on the course site and on Blackboard. Any of the language models on GenAI will do; pick one and stay with it for the session so the errors are consistent. The last bullet matters: the spec is the source, the code is a build.'))

S.append(code_slide('07 · WHAT GOOD LOOKS LIKE', 'Fifty points, all connected, from forty-five words.', LEWITT_CODE, F.lewitt_wall(),
                    caption='LeWitt\'s spec as twenty-two lines a model can write in seconds. Read it: where is the rule, where is the chance, where are the numbers?',
                    code_size=21, sketch=live('fifty-points', LEWITT_CODE, 800, 500, hint='click = new dice', extra=LEWITT_EXTRA),
                    notes='This is what should come back from the template filled with Wall Drawing 118. Notice the decision in the middle: "evenly distributed" became a grid with one point per cell, at random inside it. A model may make that decision, or may not — next slide. Either way you can read it, because it is machine A.'))

S.append(figure_slide('07 · WHAT YOU SAID · WHAT YOU MEANT', '"At random", or "evenly distributed"?', F.lewitt_random_vs_even(),
                      body=['LeWitt asked for both at once. A drafter negotiates by eye; a model picks one and does not tell you. Left: fifty calls to random(), clumps and gaps. Right: one point per grid cell, at random inside it. The spec decides — or the executor does.'],
                      caption='Same forty-five words, two readings. Ask for the rule back in one sentence and the difference shows up before you run anything.',
                      notes='The most important slide of the second half. Every ambiguity in a spec is a decision you handed to the executor. With drafters you get a phone call; with a model you get code. The fix is never in the code: rewrite the sentence.'))

S.append(cards('07 · WHAT GOES WRONG', 'Four ways the machine misreads you.', [
    ('IT ADDS', 'Flourishes you did not ask for.', 'Colours, animation, noise(), a title. That is the model\'s middle: the typical generative sketch. Restate the constraints; delete the rest.'),
    ('IT INVENTS', 'A function that does not exist.', 'The console says "x is not defined". Paste the error back, word for word. Do not describe it.'),
    ('IT DROPS', 'A constraint quietly vanishes.', 'No seed, wrong canvas, draw() looping. Check the spec line by line against the code. Five lines, five ticks.'),
    ('YOU WERE VAGUE', '"Random", or "evenly"?', 'It did what you said, not what you meant. Fix the spec, not the code — and only then ask again.'),
], text_size=23, notes='All four are the middle pulling: the model gives you the typical sketch, the typical function name, the typical omission. Three are fixed by restating the spec. The fourth is fixed by writing a better one. The activity will produce all four in the room within ten minutes.'))

S.append(cards('07 · READING A RULE YOU DID NOT WRITE', 'Machine A can be read. Use it.', [
    ('THE RULE', 'Find the loop.', 'for is the rule\'s heartbeat: how many times, over what. Two loops are a grid.'),
    ('THE CHANCE', 'Find random().', 'Each call is one throw of the die. Count them: that is how much of the picture is not yours.'),
    ('THE NUMBERS', 'Find the constants.', 'Change one. Run. Change it back. This is how you learn what a number does — and how you make the sketch yours.'),
    ('THE BREAK', 'Delete a line.', 'What disappears tells you what the line did. A rule you can break on purpose is a rule you understand. Next week\'s machine cannot be read this way.'),
], notes='You do not need to write code to read it. Four moves, in this order, on any sketch a model gives you. The last one is the reflection\'s argument in miniature: rule-based systems are legible; adaptive ones are not.'))

S.append(content('07 · ITERATE LIKE A DESIGNER', 'One change per prompt. Keep the spec.',
                 ['Version the sketches: v1, v2, v3. The spec stays; the code is disposable.',
                  '- If you cannot say the change in words, the spec is not finished. Go back to the words.',
                  '- Ask for the rule back: "describe the rule this code follows in one sentence." If it does not match yours, the code does not either.',
                  '- Save the spec with the picture: as the caption today, as the process note in your reflection later.',
                  'Week 4 makes this general: prompting is briefing. Week 12: agents that execute the whole spec.'],
                 body_size=32,
                 notes='Iteration discipline, because the model makes iteration free and therefore sloppy. One change per prompt so you know what caused what. The spec in the caption is the same rule as last week\'s prompt in the caption: we keep the words with the picture, always.'))

# ───────────────────────── 08 · activity: one spec, three executors ─────────────────────────
S.append(section('08', 'One spec. Three executors.', f'35 minutes · a pencil · {P5} · {GENAI}', bg=YELLOWS[0],
                 notes='The activity. LeWitt\'s forty-five words, cut to ten points: by hand alone, by a language model in pairs, then your own rule in fours. What goes into ClassPoint is an image, and the caption is the spec. Nicolò keeps time; the other three TAs walk. One laptop per pair.'))

S.append(activity('1 — ALONE · BY HAND', 4, 'Execute it by hand.',
                  ['Pencil and paper. Execute the spec on the right, exactly as written. Do not improve it.',
                   'Photograph the result with your phone.'],
                  panel=SPEC_TEN, bg=YELLOWS[0],
                  notes='Four minutes, silent. Watch for people who arrange the points, who draw a grid first, who forget "evenly". All of them are executing correctly, because the spec allows it. Molnár\'s imaginary machine, for four minutes.'))

S.append(question('image_upload', 'Everyone: upload your drawing.',
                  hint='Ten points, forty-five lines, your hand. We put them all on the wall.',
                  eyebrow_text='08 · CAPTURE 1 · IMAGE UPLOAD · EVERYONE',
                  notes='ClassPoint image upload, everyone, three minutes. The wall: the same words, a hundred drawings, none alike — orientation, pencil pressure, what "random" meant, whether "evenly" won. LeWitt\'s point and the whole lecture in one screen. Pick two and ask which followed the spec better. The room disagrees; that is the answer.'))

S.append(activity('2 — IN PAIRS · THE MODEL', 8, 'Let the machine execute it.',
                  ['Put the same spec into the template. Ask a language model on **genai.polyu.edu.hk**; paste the code into **editor.p5js.org**; run it. If it fails, paste the error back, word for word.',
                   'Compare with your two drawings. **What did the machine decide that you decided differently?**'],
                  panel=SPEC_FILLED, panel_size=22, bg=YELLOWS[1],
                  notes='Eight minutes. Expect all four failure modes: added colour, an invented function, a dropped seed, and the random-versus-evenly decision made silently. The TAs help with pasting errors back. The comparison question is the whole point; make every pair answer it out loud to each other.'))

S.append(question('multiple_choice', "Did the model's code run?", [
    'First time', 'After pasting one error back', 'After rewriting the spec', 'Not yet',
], eyebrow_text='08 · PULSE · MULTIPLE CHOICE',
    notes='Pulse. Show the split: usually most run first time, a fifth need one error pasted back. Ask two pairs what the machine decided differently. Then the fours.'))

S.append(activity('4 — TWO PAIRS · YOUR RULE', 10, 'Write your own spec.',
                  ['Join the pair behind you. **One rule, one random number.** Write the spec in the template, in words a stranger could execute. The words are the deliverable.',
                   'Run it through the model, run the code, look. Fix the **spec**, not the code, until the picture is the one you meant.',
                   'One scribe uploads the picture, with the spec as the caption.'],
                  panel=TEMPLATE, panel_size=21, bg=YELLOWS[2],
                  notes='Ten minutes in fours. Four people negotiating one rule is a design team writing a brief. Push them to say the chance precisely: "a random amount" is not a spec; "up to 20 px" is. This is the start of Challenge 1 — they finish it at home, alone or in the same four.'))

S.append(question('image_upload', 'Scribes only. The picture, and the words that made it.',
                  hint='One image per four. Caption: the spec, word for word.',
                  eyebrow_text='08 · CAPTURE 2 · IMAGE UPLOAD · ONE PER FOUR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='Scribes only, about 28 images. Put the wall on screen; read two captions aloud and ask the room to guess the picture before showing it. Where the guess fails, the spec failed. Download the submissions: the specs come back in week 4 as the first briefs.'))

S.append(content('08 · WHAT JUST HAPPENED', 'You wrote the rule. Three machines executed it.',
                 ['The hand: forty-five words, a hundred drawings. A spec is never complete; the executor finishes it. LeWitt knew.',
                  'The model: it did what you said, not what you meant. Machine B translated your words into machine A, and machine A has no judgement to add.',
                  'The computer: exact, repeatable with a seed, and readable — you can point at the line that decided. Next week: the machine that cannot say why.',
                  '**The machine drew every line. You wrote the rule. That was the design.**'],
                 body_size=32,
                 notes='Mirror of the whole class. Three executors, one spec, and the design was in the words every time. Say the last line slowly; it is last week\'s last line with one word changed.'))

S.append(cards('08 · CHALLENGE 1 · DUE BEFORE WEEK 3', 'A picture from rules.', [
    ('THE RULE', 'One rule, one random number.', 'Your own picture: not Schotter, not LeWitt. Start from what your four wrote today, or from scratch.'),
    ('THE SPEC', 'Words first.', 'A stranger — or a model — could execute it. Keep it: it is the caption today and evidence in your reflection.'),
    ('THE SKETCH', 'p5.js, in the web editor.', 'Written by you, by a model, or both: say which. The share link plus a screenshot, on Blackboard.'),
    ('THE VOTE', 'Bring it next week.', 'The room votes; the winners get shown and a participation star. The TAs help 30 minutes before and after class.'),
], notes='Three things on Blackboard before next class: the spec, the editor share link, one screenshot. The model is allowed and must be named. Next week the room votes; the winners get shown and a star.'))

S.append(end('See you next week. Learning from examples.',
             'Bring your sketch. Watch AlphaGo and the four short films.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: the other machine — concepts, neurons, Move 37 — and the first challenge awards. Homework: the sketch on Blackboard, AlphaGo, and Cage, Tinguely, Kaprow and the Illiac Suite on the playlist. The TAs stay for 30 minutes.'))

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
