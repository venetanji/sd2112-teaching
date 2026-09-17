"""
SD2112 · Artificial Intelligence in Design · Week 03 — the slide spec.

    deckgen build                    # everything, as the GitHub Actions workflows run it (the generator is ait4x/deckgen)
    deckgen build --pptx             # export/ only, no node needed
    python deck/week03.py --html     # only the html deck of this week

Learning from examples: what a concept is (definitions, Plato's Meno, Wittgenstein's games), Rosch's
prototypes, the birth of AI twice (Dartmouth 1956, Rosenblatt's perceptron 1958), Hinton and
backpropagation, parallel calculation and the GPUs that made 2012 possible, modern AI in one
timeline, concept blending, and the activity: a concept as a picture, then two concepts blended in
pairs, then four in fours, with the image editors on PolyU GenAI that take reference images. Two
editable p5.js sketches: a perceptron that finds its own line, and the same rule painted pixel by
pixel with one "core" or four thousand.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import figures as F                                   # noqa: E402
from deckgen import attach_reports, activity_url, build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from deckgen.layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full, timeline,   # noqa: E402
                             journey, activity, video, two_col, figure_slide, code_slide, sketch_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, JOURNEY  # noqa: E402

FOOTER = 'SD2112 · AI IN DESIGN · WEEK 03'
HERE = Path(__file__).resolve().parent


def _week2_answers(question):
    """The public page of a week-2 activity, from deck/week02-reports.json (written after the class by
    classpoint.py's weekly runner), or None until then."""
    p = HERE / 'week02-reports.json'
    if not p.exists():
        return None
    for e in json.loads(p.read_text(encoding='utf-8')):
        if e.get('question') == question and e.get('activity'):
            return activity_url(e['activity'])
    return None


SPECS_URL = _week2_answers('One per pair. Your rule: the picture, and the words that made it.')

# ───────────────────────── the code on the slides (p5.js) ─────────────────────────
# Editable in the html deck (deckgen: a code_slide with a sketch): what the students see is what runs.
# `extra` is appended only in the sketch page, for interaction the panel does not show.

# A perceptron: three numbers, nudged whenever a guess is wrong, until every example is on its side.
PERCEPTRON_CODE = """let pts = [], w1 = 0.3, w2 = -1, b = 0.1;   // three numbers
const lr = 0.05;                            // how big a nudge
const g = (m, s) => randomGaussian(m, s);   // a bell-curve die
function setup() {
  createCanvas(600, 600); randomSeed(3); frameRate(8);
  for (let i = 0; i < 12; i++) {            // twelve A, twelve B
    pts.push([g(-.45, .2), g(-.3, .2), -1]);
    pts.push([g(.45, .2), g(.35, .2), 1]);
  }
}
function guess(x, y) { return w1 * x + w2 * y + b > 0 ? 1 : -1; }
function draw() {                           // one pass per frame
  let wrong = 0;
  for (let [x, y, t] of pts)                // wrong? nudge
    if (guess(x, y) != t) { wrong++;        // a little, towards it
      w1 += lr * t * x; w2 += lr * t * y; b += lr * t; }
  background(255); stroke(0); strokeWeight(2);
  let ya = -(b - w1) / w2, yb = -(b + w1) / w2;   // where the rule
  line(0, 300 - 300 * ya, 600, 300 - 300 * yb);   // says 0
  for (let [x, y, t] of pts) {
    fill(t < 0 ? '#ED6D24' : '#64C2C3');
    circle(300 + 300 * x, 300 - 300 * y, 14);
  }
  fill(0); noStroke(); text('wrong: ' + wrong, 16, 24);
}"""

# The sketch page adds: the verdict everywhere as a tint, a readout of the three numbers, and clicks that
# add examples (an A; with shift, a B). C clears. None of it is in the panel, so the panel stays readable.
PERCEPTRON_EXTRA = r"""(function () {
  let box = document.getElementById('readout');
  if (!box) {
    box = document.createElement('div'); box.id = 'readout';
    box.style.cssText = "position:absolute;right:0;top:0;padding:6px 14px;font:13px/1.5 'JetBrains Mono',Menlo,monospace;color:#000B1C;text-align:right;background:rgba(244,244,242,.92);border-bottom:1px solid #E1E1DE;border-left:1px solid #E1E1DE;pointer-events:none;white-space:pre";
    document.body.appendChild(box);
  }
  if (window._perceptronTimer) clearInterval(window._perceptronTimer);
  window._perceptronTimer = setInterval(function () {
    try {
      box.textContent = 'w1 ' + w1.toFixed(2) + '   w2 ' + w2.toFixed(2) + '   b ' + b.toFixed(2) + '   ·   ' + pts.length + ' examples\nclick: add an A · shift-click: add a B · C: start again';
    } catch (e) { box.textContent = ''; }
  }, 150);
})();
function mousePressed() {
  if (mouseX < 0 || mouseX > 600 || mouseY < 0 || mouseY > 560) return;
  pts.push([(mouseX - 300) / 300, (300 - mouseY) / 300, keyIsDown(SHIFT) ? 1 : -1]);
}
function keyPressed() {
  if (key == 'c' || key == 'C') { pts = []; w1 = 0.3; w2 = -1; b = 0.1; }
}"""

# The Mandelbrot rule from week 2, painted in raster order, 2^k pixels per frame: one core, or four thousand.
PARALLEL_CODE = """let cores, i = 0, t0;                 // pixels per frame: a slider
const n = 60, W = 600, H = 400;       // steps per pixel; the canvas
function setup() {
  createCanvas(W, H); pixelDensity(1);
  cores = createSlider(0, 12, 8, 1, 'cores: 2^k');
  cores.input(restart); restart();
}
function restart() {                  // from the top, blank
  background(255); loadPixels(); i = 0; t0 = millis();
}
function draw() {
  let k = 1 << cores.value();         // 2^k pixels in this frame
  for (let j = 0; j < k && i < W * H; j++, i++) {   // pixel i
    let a = (i % W - 420) / 200, b = (floor(i / W) - 200) / 200;
    let x = 0, y = 0, s = 0;            // c; z starts at 0
    while (x * x + y * y < 4 && s < n) {   // z = z² + c, again
      let t = x * x - y * y + a; y = 2 * x * y + b; x = t; s++;
    }
    let v = s == n ? 0 : 255 * sqrt(s / n), q = 4 * i;
    pixels[q] = v * .3; pixels[q + 1] = v * .6; pixels[q + 2] = v;
  }
  updatePixels(); noStroke(); fill(255); rect(0, 380, 600, 20);
  let sec = nf((millis() - t0) / 1000, 1, 1);
  fill(0); text(k + '/frame · ' + i + ' px · ' + sec + ' s', 10, 394);
}"""

PARALLEL_EXTRA = """function mousePressed() { restart(); }   // from the top, same rule"""

VOTE_ENTRIES = [   # placeholders: the TAs paste the five shortlisted specs here before the deck is built (the spec only, no names)
    '(the first shortlisted rule goes here: the spec, no names)',
    '(the second shortlisted rule)',
    '(the third shortlisted rule)',
    '(the fourth shortlisted rule)',
    '(the fifth shortlisted rule)',
]

BLEND_PROMPT = [
    'Blend the two concepts into ONE thing.', ' ',
    'IMAGE 1 is [concept A]:', 'keep its [shape / colour / mood].', ' ',
    'IMAGE 2 is [concept B]:', 'keep its [material / setting / use].', ' ',
    'The result is a single object or scene,', 'not two things side by side.', 'Photographic, plain background.', 'Nothing I did not ask for.', ' ',
    'Then, in one line: what did you take', 'from each image?',
]

CONCEPT_PANEL = [
    'ROUND 1 · ALONE · 8 MIN', ' ',
    '1. Pick a concept. Anything:', '   as small as "my first bicycle",', '   as big as "justice"; concrete or', '   abstract; "Tuesday", "hospitality",', '   "a minibus at 2 am", "entropy".', ' ',
    '2. How would a picture say it?', '   Write the prompt. Text only.', ' ',
    '3. Generate. Look. Change one thing.', '   Two runs at most.', ' ',
    '4. Upload. Caption: the concept,', '   50 characters or fewer.',
]

PAIR_PANEL = [
    'ROUND 2 · IN PAIRS · 12 MIN', ' ',
    '1. Show each other the picture and', '   the concept. Two minutes.', ' ',
    '2. Talk: how could the two become', '   ONE thing? What from each?', ' ',
    '3. Write the prompt together', '   (template, previous slide).', '   Images in: your two pictures,', '   plus one more if it helps. Max 3.', ' ',
    '4. Image edit model. Two runs.', ' ',
    '5. One upload. Caption:', '   A + B, and what came from each.',
]

FOUR_PANEL = [
    'ROUND 4 · TWO PAIRS · 15 MIN', ' ',
    '1. Four concepts, two blends', '   on the table. Say all four.', ' ',
    '2. Choose the three images that', '   go in. Max 3. Which stay out?', ' ',
    '3. One prompt: the thing you want,', '   and what comes from each image.', ' ',
    '4. Run. Iterate: swap one image', '   or change one line. Three runs.', ' ',
    '5. Stop when all four agree it is', '   one thing. Say which concept', '   got lost, if one did.', ' ',
    '6. Scribe uploads. Caption: the four', '   concepts, and the lost one.',
]


def _live():
    """A link to the slide being appended, in the html deck: the pptx and the PDF show the code and a
    still, the html deck has the editor. len(S) is the new slide's index, and reveal counts from 0."""
    return f' · [edit it live](https://{SITE}/week03/#/{len(S)})'


def _linked(eyebrow_text, label, url):
    """An eyebrow with a link at the end, when there is somewhere to link to."""
    return f'{eyebrow_text} · [{label}]({url})' if url else eyebrow_text


S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 03 · LECTURE + WORKSHOP',
               'Learning from examples.',
               'Week 3 — concepts, neurons, GPUs, and a picture that blends two ideas.',
               notes='Join code on screen from 30 minutes before. Phones or laptops out from the start: the second half runs on genai.polyu.edu.hk, like week 1, with the image editors that take reference images. Challenge 1 is on Blackboard; the TAs have shortlisted five entries for the vote.'))

S.append(agenda('SD2112 · WEEK 03', [
    'Last week, in your words', 'What is a concept?', 'Prototypes: Rosch, 1975', 'The birth of AI, twice',
    'Neurons that learn: Hinton', 'Parallel: GPUs and modern AI', 'Blending concepts', 'Activity: the blend',
], notes='Eight stops. The first five are the lecture: what a concept is, and how a machine can hold one without anyone writing it down: Plato, Wittgenstein, Rosch; then AI born twice, in 1956 as rules and in 1958 as a brain; Hinton and the machine that learns; and after the break, why it needed the chips made for games, and where that got us. Then blending: two concepts in one picture, alone, in pairs, in fours. Module one closes today: after this you have both machines, and you have used both.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the film · the wall · the awards',
                 notes='Fifteen minutes of recap: logistics, the film you watched, what week 2 left on the wall, and the first challenge awards.'))

S.append(question('multiple_choice', 'Before we start: where will you run GenAI today?', [
    'A laptop, logged in', 'A phone, logged in', 'A device, but no login yet', 'Nothing with me today',
], eyebrow_text='01 · LOGISTICS · MULTIPLE CHOICE',
    notes='ClassPoint. The activity in the second half needs genai.polyu.edu.hk on at least one device per pair, with the image editor that takes reference images. Phones are fine. Cs sort out the login with a TA now, not at the break; Ds sit next to an A or a B. The TAs reseat people while the next slides run.'))

S.append(question('word_cloud', 'AlphaGo. One word.',
                  hint='You watched the film. The first word that comes to mind.',
                  eyebrow_text='01 · QUESTION · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each; leave it up for a minute. Expect: sad, Lee Sedol, move 37, creative, alien, machine, beautiful. Read the three biggest aloud and keep a screenshot: the cloud comes back after the break, when move 37 turns up in the story of modern AI. Anyone who has not watched it: it is on the playlist, ninety minutes, before the quiz in week 7.'))

S.append(cards(_linked('01 · WEEK 2 · WHAT THE WALL SAID', 'THE WALL', SPECS_URL), 'One rule each. Fifty-five pictures.', [
    ('THE SPEC', 'Words a stranger could execute.',
     'Every pair wrote a rule and one random number, and a language model turned it into p5.js. Where the words were vague, the model decided silently: "at random" or "evenly", it picked one.'),
    ('THE MODEL', 'It did what you said, not what you meant.',
     'Machine B wrote machine A. The code it gave you was exact, repeatable with a seed, and you could read the line that decided. Today we meet the machine that cannot be read.'),
    ('THE CONCEPT', 'Nobody defined "a picture".',
     'Fifty-five rules, no two alike, and every one of them was a picture. You never agreed on a definition; you did not need one. Hold that thought: it is the whole of today.'),
], text_size=22, notes='Open the wall from last week (the link in the eyebrow, once deck/week02-reports.json carries the id of the upload activity) and read two captions with the room; guess the picture before it appears. Then the sentence to carry into today: machine A is a rule you wrote. In an hour you will have the other half, and it starts with a question about concepts.'))

S.append(question('multiple_choice', 'Challenge 1. Which rule made the best picture?', VOTE_ENTRIES,
                  eyebrow_text='01 · CHALLENGE 1 · THE AWARDS · MULTIPLE CHOICE',
                  notes='Replace the five entries with the ones the TAs shortlisted (VOTE_ENTRIES in deck/week03.py, then rebuild): the spec only, no names, no pictures yet. Read each spec aloud and let the room imagine the picture before voting. Then show the five sketches from Blackboard, in the same order, and count the surprise: where the picture is better than the spec suggested, the executor did the work. Winners get a star; anyone who submitted gets the participation mark.'))

S.append(content('01 · CHALLENGE 1 · THE WINNERS', 'Shown from Blackboard. Read the spec first.',
                 ['Five rules, five random numbers, five pictures: shown live from the submissions, the spec read aloud before each picture appears.',
                  '- The vote decides the star. The TAs choose one more: the spec a stranger could execute best.',
                  '- Every submission is evidence for your reflection: keep the spec, the code and the screenshot together.',
                  'What to look for: where does chance enter, and how much is it allowed to move?'],
                 body_size=32,
                 notes='Open Blackboard on the second screen. Show the five in the vote order; for each, ask the room where the die is thrown. Add the TA pick: the best-written spec, which is not always the best picture, and say why that matters: a spec a stranger can execute is a rule you actually understand. Two minutes, then the map.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(0, 2),
                 notes='Week 3 closes module one. Week 1 gave you both machines in a chair; week 2 was the rules side; today is the examples side. Next week the tools begin: language machines, then images, then sound, each with a challenge.'))

# ───────────────────────── 02 · what is a concept? ─────────────────────────
S.append(section('02', 'What is a concept?', 'ideas · definitions · Plato · Wittgenstein', bg=INK,
                 notes='Chapter two: before the neurons, the thing they will have to hold. What is an idea? Two answers, two and a half thousand years apart, and they map onto the two machines exactly.'))

S.append(content('02 · THE CLASSICAL THEORY · ARISTOTLE TO KANT', 'A concept is a definition.',
                 ['A definition is a list of properties a thing must have to belong: necessary, and together sufficient. Bachelor = man + unmarried.',
                  '- Categorising is then trivial: check each property, apply the concept. X is a bachelor if X is a man and X is unmarried. A machine can do that.',
                  '- New ideas by assembly: put definitions together and you have a new one. Kant, last week: analytic, all in the words.',
                  'Plato pointing up: the idea is real, above the things. Aristotle pointing down: look at the things, and sort them by their properties.'],
                 image='plato-aristotle-raphael.jpg', fit='cover', body_size=27,
                 caption='Plato and Aristotle, detail of Raphael\'s The School of Athens, 1509–1511. Public domain, Wikimedia Commons.',
                 notes='The classical theory, so called because it goes back to Aristotle: a concept is a definition, a definition is a list of necessary and sufficient conditions, and membership is a verdict. Its virtue is that the check is mechanical: for every property, present or absent, then in or out. Say what it buys: exact verdicts, and new concepts by combination. Then the question for the room: can you write the list? Next slide.'))

S.append(cards('02 · SOUNDS EASY · TRY THESE', 'Write the definition.', [
    ('A PRIME NUMBER', 'Easy.', 'Divisible only by one and by itself. Every number is in or out, no argument. Mathematics is where the classical theory lives.'),
    ('FURNITURE', 'Try.', 'Movable, for a room, for living? A lamp? A rug? A built-in wardrobe? Every list you write admits something wrong or leaves out something right.'),
    ('SUNSET COLOUR', 'Try.', 'Orange? Pink? Grey over Kowloon? You know it when you see it, and you cannot say it in a way a stranger could check.'),
    ('A PIZZA', 'Try.', 'Dough, tomato, cheese, baked. Then a white pizza, a calzone, pineapple. Is a pizza defined by its base, its shape, its country, or by pizza places?'),
    ('AN A+ ESSAY', 'The rubric tries.', 'Argument, evidence, structure, style, with bands. It is the best list we can write, and two markers still disagree at the edge.'),
], text_size=21, notes='From the 2025 deck. Prime numbers: the classical theory at its best. Then it degrades: furniture, sunset, pizza, an A+. Let the room argue for a minute about the pizza. The point is not that definitions are useless; it is that most of the concepts a designer works with have none, and everyone uses them all day anyway. Now they try one themselves, on the cup from week 1.'))

S.append(question('short_answer', 'Define "cup" for a machine.',
                  hint='One sentence. The machine will apply it to every object on Earth, with no judgement of its own.',
                  eyebrow_text='02 · QUESTION · SHORT ANSWER',
                  notes='Ninety seconds; read four aloud. Every definition lets in something wrong or throws out something right: "a container for drinking" admits a glass and a bottle; "with a handle" throws out most of the cups in this room. This is the classical theory failing in real time, on the object the room generated a hundred of in week 1. Keep the answers for the mid-term question bank.'))

S.append(quote('"But in what way will you look for it, Socrates, this thing that you don\'t know at all what it is? Or even if you should meet right up against it, how will you know that this is the thing you didn\'t know?"',
               'Meno to Socrates. Plato, Meno, 80d, c. 385 BC.', size=64,
               notes='Meno, a visitor, asks Socrates how virtue is acquired. Socrates says he cannot even say what virtue is, and asks Meno to define it; every definition Meno offers fails. Then Meno turns the tables with this: if you do not know what a thing is, how will you look for it, and how will you know it when you find it? Read it twice. It is the problem of every concept you cannot define: you use it, you find instances of it, and you cannot say what you are looking for.'))

S.append(content('02 · PLATO · MENO · WHERE IDEAS COME FROM', 'Ideas are real. Definitions are not their essence.',
                 ['Socrates calls it a debater\'s trick: you cannot seek what you know, because you know it, nor what you don\'t know, because you don\'t know what to look for.',
                  '- His answer: learning is remembering. The soul has seen the ideas; the world is a copy; to learn is to recognise. He shows it with a slave boy who "finds" geometry he was never taught.',
                  '- Whatever you think of the soul, the lesson holds: we have ideas without definitions. The definition is not the essence of a concept.',
                  'Hold that. The machine after the break holds a concept of "chair" with no definition anywhere in it.'],
                 image='socrates-louvre.jpg', fit='cover', body_size=27,
                 caption='Socrates, Roman marble after a Greek original, 1st century, Louvre. Photo: Eric Gaba, CC BY-SA 2.5, Wikimedia Commons.',
                 notes='From the 2025 deck: are ideas real? Plato says yes, and that learning is remembering them. Keep the metaphysics light and the design point sharp: we recognise cups without a definition of cup, so a definition cannot be what a concept is. Then Wittgenstein, who two thousand years later says the same thing about games and gives it a name.'))

S.append(quote('"Don\'t think, but look!"',
               'Ludwig Wittgenstein, Philosophical Investigations, §66, 1953, on what all games have in common', image='wittgenstein-1930.jpg', size=96,
               notes='Wittgenstein, 1953: consider the things we call games: board games, card games, ball games, ring-a-ring-a-roses. Do not say there must be something in common or they would not all be called games; look and see whether there is. You find similarities, relationships, and a whole series of them, but nothing common to all. He called it family resemblance: the members of a family look alike in overlapping ways, and no single feature runs through the whole family. Photo: Moritz Nähr, 1930, public domain. Next slide: his paragraph as a table.'))

S.append(figure_slide('02 · WITTGENSTEIN · 1953 · FAMILY RESEMBLANCE', 'No feature runs through all of them.', F.family_resemblance(),
                      body=['Six games, seven features. A definition would need a full column; there is none. Chess and ring-a-ring-a-roses share almost nothing, yet both are games, because a chain of resemblances links them: overlapping and criss-crossing, like the resemblances in a family.'],
                      caption='After Philosophical Investigations §66–67. The features are ours; the argument is his. Rosch borrowed the term for her experiments twenty years later.',
                      notes='Walk one column: "winning": ring-a-ring-a-roses has no winner. "players": patience has one. No column is full, so no definition exists, and yet nobody in this room is confused about what a game is. Hold this table: in forty minutes the perceptron will be doing the same thing with numbers instead of dots.'))

S.append(cards('02 · THE CLASSICAL THEORY · WHERE IT LEAVES US', 'Easy to check. Impossible to write.', [
    ('THE BENEFIT', 'Categorising is trivial.',
     'Set formal requirements and the check is mechanical: every property, present or absent. That is why a rule-based machine can hold a concept at all: a definition is a rule, and week 2 was about rules.'),
    ('NEW IDEAS', 'By assembly.',
     'Put two definitions together and you have a third: unmarried + man. Later today: which properties survive when you combine "pet" and "fish"? Assembly is exactly where definitions start to fail.'),
    ('THE PROBLEM', 'Most concepts have no definition.',
     'Outside mathematics and law, almost nothing you design has one, and you use those concepts all day without it. So what is a concept, if not a definition? A psychologist in Berkeley asked people about fruit.'),
], text_size=22, notes='The classical theory is machine A applied to meaning: a definition is a rule, membership is a verdict. It works for primes and for contracts and fails for almost everything a designer makes. The bridge to the next chapter is the last card: if not a definition, then what? Rosch went and measured.'))

# ───────────────────────── 03 · prototypes: Rosch ─────────────────────────
S.append(section('03', 'Prototypes', 'Rosch · 1975 · a middle and an edge', bg=TEALS[0],
                 notes='Chapter three: the experiment that ended the classical theory for psychology, replicated in this room in thirty seconds.'))

S.append(question('word_cloud', 'Name a fruit. The first one that comes to mind.',
                  hint='One word. Do not think.',
                  eyebrow_text='03 · QUESTION · WORD CLOUD',
                  notes='ClassPoint word cloud. Thirty seconds. The cloud will have three or four big words: apple, banana, orange, maybe mango or durian in Hong Kong, and a long tail. If concepts were definitions, every fruit would be as good an answer as any other and the cloud would be flat. It is not flat. The room just produced a prototype. Keep the screenshot next to Rosch\'s list on the slide after next.'))

S.append(content('03 · ELEANOR ROSCH · BERKELEY · 1975', 'I asked people to rate fruits.',
                 ['Rosch gave about two hundred students lists of items in ten categories, fruit, birds, furniture, vehicles, and asked for each: how good an example of the category is this? From 1, a very good example, to 7, a very poor one.',
                  '- If a concept were a definition, an orange and an olive would be equally fruit, and the ratings would be noise.',
                  '- They were not. People agreed, strongly and quickly: some fruits are more fruit than others.',
                  'Two papers in 1975, with Carolyn Mervis: typicality is real, shared, and it is made of family resemblance, counted.'],
                 image='rosch-2012.jpg', fit='cover', body_size=27,
                 caption='Eleanor Rosch, 2012 (Wikimedia Commons, CC0). Rosch 1975, J. Exp. Psych.: General 104; Rosch & Mervis 1975, Cognitive Psychology 7.',
                 notes='Eleanor Rosch, Berkeley, 1975: the goodness-of-example ratings, 209 students, ten categories, and everyone agreed on which members were the good ones. The second paper with Mervis explains why: the most typical members share the most features with the rest of the category and the fewest with other categories, Wittgenstein\'s table with numbers in it. Say the design version: every category has a middle everyone can draw and an edge everyone argues about. Then the fruit.'))

S.append(content('03 · ROSCH · 1975 · THE FRUIT', 'Some fruits are more fruit than others.',
                 ['Thirteen of her fifty-one fruits, in her order. Orange, apple and banana sit at the very top, about 1 on the scale; tomato is above 5; the olive comes last.',
                  '- Nobody had trouble answering, and the ratings were the same across people: the concept has a shape, and it is shared.',
                  '- Compare the word cloud. Your first fruit was near the top of this list. A prototype is what a room produces when it does not think.',
                  'A concept with a middle and an edge cannot be a definition. Definitions have no middle.'],
                 figure=F.fruit_typicality(), body_size=27,
                 caption='Rank order of Rosch\'s 1975 goodness-of-example ratings for fruit, 1 = a very good example, 7 = a very poor one; the positions are approximate, the order is hers.',
                 notes='From the 2025 deck: the sorted fruits. Put the word cloud next to it: the room\'s big words are the top of the list. Then the argument in one line: if concepts were definitions, the ratings would be random; they are not, so concepts are not definitions. Ask who put the tomato in the vegetables: that is the edge, and a court once had to rule on it (Nix v. Hedden, 1893: a vegetable, for tariff purposes). The concept has a middle and an edge, and the edge is where you argue.'))

S.append(cards('03 · WHAT TYPICALITY DOES', 'The middle is faster, first, and easier.', [
    ('JUDGED', 'Typical items are called members more often.', 'Hampton, 1979.'),
    ('FASTER', 'Categorising a typical item takes less time.', 'Rips, Shoben & Smith, 1973.'),
    ('LEARNED FIRST', 'Children learn the typical members before the atypical ones.', 'Rosch & Mervis, 1975.'),
    ('EASIER TO TEACH', 'A category is learned faster from typical examples.', 'Mervis & Pani, 1980.'),
    ('UNDERSTOOD', 'In a sentence, a typical member is understood more easily.', 'Garrod & Sanford, 1977.'),
], text_size=22, notes='From the 2025 deck: five effects, all the same shape. Whatever concepts are, the middle is privileged: it comes first, it goes faster, it is what you teach from. For the room: this is why every model you have used gives you the middle. A machine built from examples inherits the middle; you saw it in the week-1 cups and the week-1 chairs. Now name the theory.'))

S.append(cards('03 · PROTOTYPE THEORY', 'A concept is its best examples.', [
    ('THE THEORY', 'A structured representation of what members tend to have.',
     'Not a list of conditions but a picture of the typical case, and a distance from it. Membership is a degree: a robin is a very good bird, a penguin a poor one, and neither needs a definition.'),
    ('THE GAIN', 'Only similarity is needed.',
     'No definition to write: you judge a new thing by how much it resembles what you have seen. That is learning from examples, and it is why a machine can hold "chair" with no rule for it.'),
    ('THE COST', 'Outliers, and combinations.',
     'Exceptions are hard: there are fewer examples at the edge, so the edge is unsure. And combining concepts is a puzzle: which properties of "pet" and "fish" does "pet fish" keep? After the break we make a machine do exactly that.'),
], text_size=22, notes='Prototype theory, Rosch\'s name for it. Say the two costs slowly, because they are the second half of today. Outliers: a prototype machine is unsure at the edge, and the edge is where designers work. Combinations: nobody knows the rule for combining two prototypes, and the activity at the end is that problem given to an image model. Quick check next.'))

S.append(question('multiple_choice', 'Which sentence is prototype theory?', [
    'A chair is anything with a seat, a back and at least three legs',
    'Every chair shares one feature that makes it a chair',
    'Some chairs are better examples of "chair" than others',
    'A chair is whatever the dictionary says it is',
], eyebrow_text='03 · QUICK CHECK · MULTIPLE CHOICE',
    notes='C. A, B and D are the classical theory in different clothes: a list of conditions, a single essential feature, an authority holding the list. Only C admits degrees. Ask for a chair that is a "worse example": a beanbag, a swing, a throne, and notice nobody says "not a chair".'))

# ───────────────────────── 04 · the birth of AI, twice ─────────────────────────
S.append(section('04', 'The birth of AI, twice', '1956 · Dartmouth · 1958 · the perceptron', bg=INK,
                 notes='Chapter four: AI was born twice, two years apart, with the two theories of concepts built in. One school wrote definitions; the other copied the brain.'))

S.append(content('04 · DARTMOUTH · SUMMER 1956', 'AI gets its name, and a bet.',
                 ['31 August 1955: McCarthy, Minsky, Rochester and Shannon propose a summer study "on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."',
                  '- Summer 1956, Dartmouth: the field gets its name. Turing\'s intelligence as computation becomes a programme.',
                  '- Intelligence = analytical reasoning. Symbols, rules, search: the classical theory of concepts, built.',
                  'Haugeland named it GOFAI in 1985: good old-fashioned AI, the AI of week 2.'],
                 image='dartmouth-proposal-1955.jpg', fit='contain', body_size=26,
                 caption='The first page of the proposal, 31 August 1955. Public domain, Wikimedia Commons.',
                 notes='The founding document, first page. Read the conjecture aloud: precisely described, therefore simulable. It is Kant\'s analytic judgement as a research programme: if intelligence can be written down, a machine can run it. This school gave us rules, expert systems, and the knowledge bottleneck from week 2. Two years later, a hundred miles away, a psychologist made the opposite bet.'))

S.append(content('04 · THE OTHER BIRTH · ROSENBLATT · 1958', 'A machine modelled on the brain, not on logic.',
                 ['Frank Rosenblatt, Cornell, 1957–58: the perceptron. Not a program that applies rules but a network of simple units modelled on neurons, whose connections adjust from examples.',
                  '- Top: a brain, as he drew it: retina, projection areas, association areas, responses. Bottom: the perceptron, the same shape, in wires.',
                  '- Show it a letter; it guesses; if wrong, the connections that voted wrong are weakened, the ones that voted right strengthened. Again.',
                  'No definition of "A" anywhere. The knowledge is in the weights, and the weights come from the examples.'],
                 image='rosenblatt-brain-perceptron-1958.jpg', fit='contain', body_size=26,
                 caption='Rosenblatt, "The design of an intelligent automaton", 1958, figures 1 and 2. Public domain, Wikimedia Commons.',
                 notes='The second birth. Rosenblatt was a psychologist, and his diagram says it all: top a brain, bottom the machine, the same boxes. The bet is Rosch\'s theory before Rosch: no definition, a feel for the typical "A" built up from examples. Say the learning rule in one sentence, wrong guess, nudge the connections, and note that this is exactly the sentence we will read in code in three slides.'))

S.append(image_full('mark-i-perceptron-1960.jpg', '04 · THE MARK I PERCEPTRON · 1960 · PHOTO: US NAVY, PUBLIC DOMAIN',
                    '400 photocells look at a letter; motors turn the potentiometers that hold the weights when a guess is wrong. The New York Times, July 1958: the Navy expects it "will be able to walk, talk, see, write, reproduce itself and be conscious of its existence".',
                    notes='The first hardware: the Mark I, 1960. Four hundred photocells for eyes, motors turning the potentiometers that held the weights. And the first AI hype cycle, sixty-eight years ago: the Times promised consciousness on the strength of a machine that told C from E. Hold the two ideas together: a real learning machine, and a press release that could be printed today. The perceptron itself is on the next slide, as three numbers.'))

S.append(figure_slide('04 · ONE NEURON', 'A neuron is a weighted vote.', F.neuron(),
                      body=['Two inputs, two weights, a bias, a threshold. Multiply, add, compare with zero: that is the whole unit. Three numbers hold everything it knows. Rosenblatt, 1958, called it a perceptron; the shape and the size are the week-1 cup.'],
                      caption='Rosenblatt, "The perceptron: a probabilistic model for information storage and organization in the brain", Psychological Review 65, 1958.',
                      notes='Read it left to right with the numbers: shape 1.1 times 1.6, size 0.4 times minus 0.8, minus 1.2, equals 0.24, above zero, so "cup". Now the important sentence: nobody typed 1.6. The three numbers were found. Change them and the neuron holds a different concept. Learning is changing them when the guess is wrong, and the next slide does that live.'))

S.append(code_slide('04 · THE PERCEPTRON · 1958 · IN P5.JS', 'Wrong? Nudge the three numbers. Again.', PERCEPTRON_CODE,
                    caption='Each frame is one pass: where a guess is wrong, the three numbers move a little towards the example, and the line settles. Click: add an example; shift-click: a B' + _live() + '.',
                    code_size=18, sketch=live('perceptron', PERCEPTRON_CODE, 600, 600, hint='click = add an A · shift-click = a B · C = again', extra=PERCEPTRON_EXTRA),
                    notes='The whole of machine learning in twenty-four lines. guess() is the rule applied; draw() looks at every example and, where the guess is wrong, moves each number a little towards the example. lr is how big a step. Watch it once from a reload: the line starts wrong, swings, settles; "wrong: 0". Nobody wrote that line; it came out of the examples. Then click: add an A among the Bs and it never settles: one line cannot, which is the 1969 objection on the slide after next. Press C to start again. On your laptop: lr 0.05 → 0.5, Run: it overshoots. Say what is not here: no definition of A or B, no if-then about anything. Compare with week 2\'s code: there the rule was the code; here the code is a rule for finding rules.'))

S.append(cards('04 · 1958 · 1969 · 1986', 'A machine that learns, and what it took.', [
    ('1958 · ROSENBLATT', 'The perceptron.',
     'The paper in Psychological Review, then the Mark I. A machine that learns, and the press promising consciousness within the year. Rosenblatt died in 1971, aged 43, with the idea out of fashion.'),
    ('1969 · MINSKY & PAPERT', 'One line cannot.',
     'Perceptrons, the book: a single layer can only draw one straight line, so it cannot even learn XOR. Funding for networks dries up for a decade. The rules school, Minsky\'s own, wins the seventies.'),
    ('1986 · BACKPROPAGATION', 'Rumelhart, Hinton & Williams.',
     'Four pages in Nature: put units in layers, send the error backwards, nudge every weight. Hidden units invent their own features. Connectionism has its learning rule, and the other school of AI is back.'),
], text_size=21, notes='Three dates. 1958: the machine learns, and the first hype cycle. 1969: the limit is real; a single neuron is a single line, and Minsky, one of the Dartmouth four, wrote the book that buried the other school for fifteen years. 1986: layers plus backpropagation, and the limit is gone, on paper. What was still missing was examples and speed, which is the chapter after the break. Next slide shows the limit and the fix as pictures.'))

S.append(figure_slide('04 · THE LIMIT, AND THE FIX', 'One line cannot. Two layers can.', F.xor_limit(),
                      body=['XOR: A on one diagonal, B on the other. No straight line separates them, so one neuron never settles. Add a hidden layer of two neurons and the network can draw two lines and vote on them. The band is a rule nobody wrote.'],
                      caption='Minsky & Papert, Perceptrons, 1969 · Rumelhart, Hinton & Williams, "Learning representations by back-propagating errors", Nature 323, 1986.',
                      notes='Left: try to draw a line; every one gets a cluster wrong; you can make the perceptron sketch do this by adding As among the Bs. Middle: two hidden units, each a neuron, each one line; the output unit combines their verdicts. Right: the band between the two lines is the concept the network found. Nobody said "band". That is what "learned representation" means in the 1986 title: the hidden units come to represent features nobody named. The man in the middle of that paper is the next chapter.'))

# ───────────────────────── 05 · neurons that learn: Hinton ─────────────────────────
S.append(section('05', 'Neurons that learn', 'Hinton · connectionism · 1986 · 2012 · 2024',
                 notes='Chapter five: the person who kept the second school alive for thirty years, the learning rule that made it work, and the deal it makes.'))

S.append(content('05 · GEOFFREY HINTON', 'Fifty years betting on the brain.',
                 ['A psychologist, like Rosenblatt. 1986: backpropagation, with Rumelhart and Williams, when almost nobody believed in networks.',
                  '- Connectionism: a concept is a pattern of activity over many units, never a list. Rosch\'s graded categories as an engineering brief.',
                  '- 2012: with his students Krizhevsky and Sutskever, AlexNet wins ImageNet. 2018: the Turing Award. 2023: leaves Google to speak about the risks.',
                  '2024: the Nobel Prize in Physics, with John Hopfield, "for foundational discoveries and inventions that enable machine learning with artificial neural networks".'],
                 image='hinton-nobel-lecture-2024.jpg', fit='cover', body_size=25,
                 caption='Geoffrey Hinton at the 2024 Nobel Lectures, Stockholm University. Photo: Jay Dixit, CC BY-SA 4.0, Wikimedia Commons.',
                 notes='Hinton is the through-line from 1986 to today: the learning rule, the students, the chips, the prize, and the warning. Say why a psychologist ends up with a physics prize: the idea was about how a brain might hold a concept, and it turned out to be how a machine can. The PDP point matters for us: connectionism took the prototype theory seriously; a concept as a pattern over many units is a middle with an edge, never a definition. Next: the rule itself.'))

S.append(figure_slide('05 · BACKPROPAGATION · 1986', 'Send the error backwards. Nudge every weight.', F.backprop(),
                      body=['Forward: every unit sums its inputs, weighted, and passes a number on; at the end, a guess. Backward: compare the guess with the truth, and share the error out along the same connections, so every weight moves a little in proportion to its part in the mistake. Then the next example. A million times.'],
                      caption='Rumelhart, Hinton & Williams, Nature 323, 533–536, 9 October 1986. The perceptron\'s rule, extended to units that never see the answer directly.',
                      notes='The perceptron could only nudge weights that touched the output. Backpropagation works out, for a weight three layers deep, how much of the final error was its fault, and nudges it by that much. That is the whole trick: the chain rule from calculus, applied backwards through the network. The design point: nobody tells the hidden units what to detect; they become edge detectors or leg detectors because that lowers the error. Deep learning is this with more layers, more examples, and faster chips.'))

S.append(figure_slide('05 · HUMANS + CONCEPTS · MACHINES + CONCEPTS', 'Two theories. Two machines.', F.theories_machines(),
                      body=['The classical theory of concepts and GOFAI are one idea: a concept is a definition, a definition is a rule, and a machine can apply it. Prototype theory and connectionism are the other: a concept is its examples, the knowledge is in the weights, and nobody can read it.'],
                      caption='Rule-based: classical theory + symbolic AI. Adaptive: prototype theory + connectionism. This is the distinction your reflection is about.',
                      notes='From the 2025 deck, and the bridge of the whole module. Every AI in this course holds concepts one of these two ways. Ask: which theory did your week-1 cup prompt meet? The second. Which one did your week-2 spec meet? The first: the code is a definition. For the reflection: rule-based versus adaptive, with this table as the map.'))

S.append(cards('05 · THE DEAL', 'Fluent. Fuzzy. Opaque.', [
    ('FLUENT', 'It handles the case nobody wrote.',
     'A learned concept covers the middle of its examples and interpolates between them. That is why it can write, draw and see: no list of conditions could.'),
    ('FUZZY', 'Every answer is a degree.',
     'Chair 0.93, stool 0.05. There is no line, only a slope, and it moves with the examples. The edge of the concept is exactly where it is least sure, and where you work.'),
    ('OPAQUE', 'It cannot say why.',
     'Sixty million numbers found by nudging. No line to point at, no rule to read, no fix but more examples. When it is wrong you cannot ask it; you can only retrain it.'),
], notes='The mirror of week 2\'s "exact, explainable, brittle". Machine B trades all three for the ability to handle what nobody wrote down. For the reflection this is the vocabulary: rule-based versus adaptive, and the deal each one makes. Ask the room for a feature they love that is fuzzy and one they hate that is opaque; autocomplete usually gets both answers.'))

S.append(statement('Machine A is a rule you wrote. Machine B is a rule nobody wrote.', eyebrow_text='05 · WHERE WE ARE', size=104,
                   notes='The sentence to carry across the break. A rule you wrote: exact, explainable, brittle. A rule nobody wrote, found from examples: fluent, fuzzy, opaque. Neither is better; every AI feature you meet is one, the other, or a mix, and your job is to know which one you are holding.'))

S.append(statement('Break. Ten minutes.', eyebrow_text='AFTER THE BREAK · GPUS · MODERN AI · THEN THE BLEND', size=120, bg=PAPER,
                   notes='1:25. After the break: why the second school needed the chips made for games, what happened from 2012 to now, and then phones and laptops on genai.polyu.edu.hk. Anyone without a PolyU GenAI login sorts it out with a TA now.'))

# ───────────────────────── 06 · parallel: GPUs and modern AI ─────────────────────────
S.append(section('06', 'Parallel', 'every unit at once · GPUs · 2012 · today', bg=ORANGES[0],
                 notes='Chapter six: the missing ingredient. Backpropagation was known in 1986 and nothing much happened for twenty-five years. The reason is hardware, and the hardware came from games.'))

S.append(figure_slide('06 · PARALLEL CALCULATION', 'Every unit decides on its own.', F.serial_parallel(),
                      body=['A Turing machine does one step at a time, and its whole state sits in one place, readable. A network is thousands of small sums that do not wait for each other and share nothing: harder to read, and far faster for some tasks, if you have something that can do thousands of sums at once. For decades, nobody did.'],
                      caption='The rule-based machine is serial by nature; the learned one is parallel by nature. The chip you run it on decides whether that is a strength or a wait.',
                      notes='From the 2025 deck: parallel calculation. Two consequences of "every neuron on its own". First, interpretability: there is no tape to read; the state is smeared over a million units. Second, speed: all those sums could happen at once, but a CPU does them one after another. The next slide lets you feel that with the picture from last week.'))

S.append(code_slide('06 · THE SAME RULE, 240,000 TIMES · IN P5.JS', 'One core, pixel by pixel. A GPU, all at once.', PARALLEL_CODE,
                    caption='The Mandelbrot rule from week 2, one pixel after another. The slider is how many pixels are done in each frame: 1, or 4,096. Same rule, same picture, a thousand times sooner' + _live() + '.',
                    code_size=18, sketch=live('parallel', PARALLEL_CODE, 600, 400, hint='the slider is how many at once · click = from the top', extra=PARALLEL_EXTRA),
                    notes='The rule per pixel is week 2\'s; the only new thing is the loop that does k pixels a frame and then stops until the next frame. Drag the slider to 0: one pixel per frame, an hour for the picture. To 8: fifteen seconds. To 12: about a second. Nothing about the rule changed; only how many copies of it run at the same time. That is what a GPU is: not a faster core, but thousands of slow ones, each doing the same small job on its own pixel, or its own neuron. A shader is this code; so is a layer of a network.'))

S.append(content('06 · GPUS · NOT ONLY FOR GAMING', 'The chips made for games.',
                 ['A graphics processing unit does the same small calculation on millions of pixels at once: textures, shading, vertices, physics. Games needed that, and paid for twenty years of it.',
                  '- 2007: CUDA. NVIDIA opens the chip to any calculation that has the same shape: many small identical jobs, no waiting.',
                  '- A neural network is exactly that shape: multiply, add, everywhere, at once. What a CPU did in weeks, a graphics card did in days.',
                  '2012: two of these, a GeForce GTX 580 each, trained AlexNet in about a week. The other school of AI finally had its engine.'],
                 image='gtx580-card.jpg', fit='cover', body_size=27,
                 caption='An NVIDIA GeForce GTX 580, late 2010: the card AlexNet was trained on, two of them. Photo: TheStriker, CC BY-SA 4.0, Wikimedia Commons.',
                 notes='From the 2025 deck: not only for gaming. The story in one line: the machine that learns is parallel by nature, and the only cheap parallel chips on Earth were made for games. CUDA in 2007 let researchers use them for anything; Krizhevsky wrote the network to run on two of them. Say the design consequence: the AI you use is shaped by what gaming hardware could do, and the companies that made it are now the largest on the planet.'))

S.append(image_full('gtx580-die.jpg', '06 · INSIDE THE GTX 580 · THE GF110 DIE · 512 CORES · 3 BILLION TRANSISTORS',
                    'The chip under the fan, sanded down and photographed: sixteen blocks of thirty-two small processors, each doing the same job on its own piece of the picture. This, twice, is what learned to see in 2012. Photo: Fritzchens Fritz, CC0, Wikimedia Commons.',
                    notes='Let the room look. The green blocks are the streaming multiprocessors: sixteen of them, thirty-two cores each, five hundred and twelve in all, every one of them slow on its own and fast together. Compare with the four or eight big cores of the laptop you are looking at it on. Then the point for the next slide: give this chip a million labelled photographs and a week.'))

S.append(figure_slide('06 · 2012 · ALEXNET', 'Deep: the features are learned too.', F.alexnet_layers(),
                      body=['30 September 2012: Krizhevsky, Sutskever and Hinton win the ImageNet challenge with an eight-layer network: 15.3% error against 26.2% for the runner-up, trained on 1.2 million labelled photos in about a week on two GTX 580s. The other entries ran on hand-crafted features; AlexNet grew its own from the pixels.'],
                      caption='ImageNet: Fei-Fei Li, from 2006; 14 million images labelled by 49,000 Mechanical Turk workers in 167 countries. Who chose the examples, and who labelled them, is week 9.',
                      notes='The picture is a story of layers: the first layers become edge detectors, the middle ones parts, the last ones objects, and nobody programmed any of that; the layers became those detectors because it lowered the error. AlexNet is the 1986 idea with a million examples and a graphics card. Say the two enablers plainly: the web gave the examples, gaming gave the chips. And then the design point in the caption: 49,000 people labelled the photos for pennies. The examples are the material, and someone chose them.'))

S.append(video('06 · 2016 · ALPHAGO · MOVE 37', 'A move outside the human middle.', 'WXuK6gekU1Y',
               ['Seoul, 10 March 2016, game two: AlphaGo plays a move the commentators call a mistake. Humans would have played it, DeepMind said, one time in ten thousand.',
                '- Trained first on human games: the prototype of a good move. Then on millions of games against itself: examples no human had ever produced.',
                '- Move 37 came from the second set. It sits far from the human prototype, and it was right.',
                'Your word cloud from the start of the class was the room\'s verdict. Creative, alien, or just a very large set of examples? Week 11 comes back to it.'],
               thumb='yt/WXuK6gekU1Y.jpg', body_size=26,
               notes='The film you watched, in one slide, with today\'s vocabulary. A model trained on human games plays the human middle. Self-play gave it a dataset nobody had curated, and move 37 lives there: a move humans rated one in ten thousand is, by definition, far from the prototype of good play. Put the word cloud back up. The question of whether that is creativity is the course question; we take it up properly in week 11, with authorship. Now the rest of the story, fast.'))

S.append(timeline('06 · MODERN AI · 2012 – 2026', 'The same loop, a billion times bigger.', [
    ('2012', 'AlexNet', '60 million weights, two gaming GPUs, a week. The examples school wins at seeing.'),
    ('2014', 'GANs', 'Two networks, one forging, one judging. Edmond de Belamy, 2018, was one of these.'),
    ('2017', 'The transformer', '"Attention is all you need": the architecture inside every chatbot since. Week 4.'),
    ('2020', 'GPT-3', '175 billion weights, trained on the web. Scale as the strategy.'),
    ('2022', 'Diffusion · ChatGPT', 'Stable Diffusion, then ChatGPT: machine B reaches everyone through a text box.'),
    ('2024', 'Two Nobel Prizes', 'Physics: Hopfield and Hinton, the networks. Chemistry: Hassabis and Jumper, AlphaFold.'),
    ('2025', 'Editors that take references', 'Flux Kontext, Qwen-Image-Edit, FLUX.2: show the model pictures, not only words.'),
    ('2026', 'You', 'Both machines in every tool. The designer decides which, and when, and with which examples.'),
], notes='Fourteen years in eight stops, and every stop is the same loop: examples in, a guess, an error, every weight nudged; only bigger. 2012 needed two graphics cards; 2020 needed thousands; today\'s models are trained on tens of thousands, and the chips are still the descendants of the ones made for games. The last two stops are today: the editors that take reference images are what you use in an hour, and the designer\'s job is choosing the examples. Which is the next chapter: what happens when you give one of these machines two concepts at once.'))

# ───────────────────────── 07 · blending concepts ─────────────────────────
S.append(section('07', 'Blending concepts', 'pet fish · houseboat · a picture from two ideas', bg=PINKS[0],
                 notes='Chapter seven, short: the problem prototype theory could not solve, the theory of how humans do it anyway, and what an image model does with it.'))

S.append(cards('07 · COMBINING CONCEPTS', 'Bachelor was easy. Pet fish is not.', [
    ('THE CLASSICAL WAY', 'Add the conditions.',
     'Man + unmarried. A rule combines any two definitions: everything from both, nothing new. It also gives you "fake gun" (a gun?) and "small elephant" (small?). Assembly is where lists show their seams.'),
    ('THE PROTOTYPE PROBLEM', 'Typicality does not multiply.',
     'A guppy is a poor example of a pet and a poor example of a fish, and a very good pet fish (Osherson & Smith, 1981). Which properties survive the combination? Nobody has found the rule (Hampton, 1988).'),
    ('THE BLEND', 'Two inputs, one new space.',
     'Fauconnier & Turner, 2002: we build a blended space that takes some structure from each input and grows structure of its own. A houseboat, a computer virus, a desk lamp. We do it all day; we cannot say how.'),
], text_size=22, notes='The second cost of prototype theory, from the Rosch chapter, now in full. The classical theory combines by conjunction and produces nonsense at the edges. Prototype theory cannot combine at all: the pet fish is the standard counter-example. Conceptual blending is the best account we have of what people actually do: a new space with emergent properties, made without a rule. Koestler called it bisociation in 1964; Boden calls it combinational creativity. Next slide: the diagram.'))

S.append(content('07 · FAUCONNIER & TURNER · 2002', 'Two inputs. One new space.',
                 ['Two input spaces: a house and a boat. A generic space of what they share: a structure, a place, people. And the blend: a houseboat, with what it took from each and what neither had, a mooring fee, a bathroom on deck, a view that changes.',
                  '- Selective projection: not every property comes across. The house\'s foundations stay behind; so does the boat\'s cargo.',
                  '- Emergent structure: the blend has properties no input had. That is where the new idea lives.',
                  'Every metaphor, every product mash-up, every "what if a chair were a cup" is one of these. Now let a machine do it.'],
                 figure=F.blend_spaces(), body_size=26,
                 caption='After Fauconnier & Turner, The Way We Think: Conceptual Blending and the Mind\'s Hidden Complexities, 2002.',
                 notes='The four-space diagram. Walk it with the houseboat: what each input contributes, what is left behind, what appears only in the blend. Then ask the room for one: a computer virus (biology + software), a desk lamp, a mermaid. The design point: blending is how new concepts are made, and nobody can write the rule for which properties come across. Which is exactly the situation of a machine that has no rules: the activity tests whether examples are enough.'))

S.append(figure_slide('07 · A MACHINE THAT BLENDS', 'Show it two pictures. Ask for one.', F.blend_outcomes(),
                      body=['An image editor that takes references has the examples; a reference image is one more example, placed in front. Give it two and a sentence and one of three things comes back: a collage, both things side by side, which is what a rule would do; a blend, one thing with properties of both, which no definition could do; or the stronger prototype eats the other, which is the middle pulling, as always.'],
                      caption='Cup and chair, three outcomes. In the activity, name which one you got; the caption says what came from where. Making the model blend rather than collage is a prompt-writing skill, and a design skill.',
                      notes='The three outcomes to expect in the next hour, drawn with the week-1 cup and the week-1 chair. The collage is the classical conjunction: both, side by side, nothing new. The blend is the interesting case: properties of both in one object; it can only come from a machine that has no definitions. One wins: the prototype effect from the Rosch chapter, on the picture level: the stronger concept swallows the weaker. Say the skill: getting a blend instead of a collage is in the words, "one thing, not two", and in which pictures you show it.'))

S.append(cards('07 · ON GENAI · IMAGE TO IMAGE', 'Four moves.', [
    ('1 · PICK', 'The model with an image input.',
     f'On {GENAI}, choose the image editor that takes reference images: Flux, or Qwen Image Edit. Up to three images in. Same login as week 1.'),
    ('2 · SHOW', 'Attach the references.',
     'One to three pictures: your own from round 1, your partner\'s, one more if it helps. Each one is an example the model stands near. Their order matters: image 1 pulls hardest.'),
    ('3 · TELL', 'One sentence, and what from where.',
     '"Blend image 1 and image 2 into one thing: the shape of the first, the material of the second." Say "one thing, not two". A reference cannot forbid; the sentence can ask.'),
    ('4 · ITERATE', 'One change per run.',
     'Swap a reference, or change one phrase, never both: then you know which machine answered. Keep every prompt with its picture; the caption is the prompt and the references.'),
], text_size=22, notes='Four moves, and the discipline from week 2 applies: one change per run so you know what caused what. The TAs checked which editor on GenAI accepts several reference images and how many; say the name aloud. Phone browsers work. If uploads are slow, one laptop per pair. The template is on the next slide and on Blackboard.'))

S.append(two_col('07 · A PROMPT FOR A BLEND', 'Say what comes from where.',
                 ['Fill the brackets. Attach the images in the order the prompt names them. Run once, look, change one line.',
                  '- Name the thing you want as one noun if you can: "a lamp", "a room", "a creature". A blend needs a home.',
                  '- Say what each image gives. Left open, the model averages, and the stronger prototype wins.',
                  'Ask for the line back: what it took from each. If it cannot say, look harder at the picture.'],
                 BLEND_PROMPT, right_size=23, left_size=30, lang=None,
                 notes='The template for rounds 2 and 4, on Blackboard as well. The three sentences that matter: one thing not two, what from each image, nothing I did not ask for. The last line, asking what it took from each, is the reflection\'s argument in miniature: the machine made the image; you decided the examples and what each was for. Then the activity.'))

# ───────────────────────── 08 · the activity: the blend ─────────────────────────
S.append(section('08', 'The blend.', f'50 minutes · alone, in pairs, in fours · {GENAI}', bg=YELLOWS[0],
                 notes='The activity. Three rounds. Alone: a concept, any concept, made visible in a picture; everyone uploads it with the concept as the caption. In pairs: two concepts blended into one picture, with the two pictures as references. In fours: four concepts, three images in, one picture. Nicolò keeps time; Amber, WU Zhao and MA Jie walk. One device per pair at least.'))

S.append(activity('1 — ALONE', 8, 'Pick a concept. Make it visible.',
                  ['Any concept: as specific as **your first bicycle**, as broad as **justice**; abstract or concrete. Then: how would a picture say it? Write the prompt, text only, and generate on **genai.polyu.edu.hk**.',
                   'Look. Does the picture say the concept to a stranger? Change one thing, run again. Two runs at most.',
                   'Upload it. **Caption: the concept, in 50 characters or fewer.** That caption is what your partner will work from.'],
                  panel=CONCEPT_PANEL, panel_size=21, bg=YELLOWS[0],
                  notes='Eight minutes, silent. The choice of concept is the design decision; push people away from the first noun that comes to mind and towards something they care about, and let a few pick something abstract: those make the best blends. The prompt is text only this round. The caption is a constraint on purpose: fifty characters is a concept, not a description. The TAs help with the login and the model choice.'))

S.append(question('image_upload', 'Everyone: your concept, as a picture.',
                  hint='The image from round 1. Caption: the concept, 50 characters or fewer.',
                  eyebrow_text='08 · CAPTURE 1 · IMAGE UPLOAD · EVERYONE',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='ClassPoint image upload, everyone, caption required: the concept. Three minutes. Put the wall up and read six captions with their pictures: does the picture say the concept? Notice how many pictures are the prototype of their concept: the typical bicycle, the typical justice (a scale, a blindfold). That is Rosch on the wall. The pairs start as soon as the upload is in.'))

S.append(activity('2 — IN PAIRS', 12, 'Blend two concepts into one picture.',
                  ['Show each other your picture and your concept. Talk: **how could the two become one thing**, not two things side by side? What does each contribute?',
                   'Write the prompt together, from the template. **Images in: your two pictures**, plus one more if it helps; three at most. The image editor on GenAI. Two runs.',
                   'One upload per pair. **Caption: concept A + concept B, and one line on what came from each.**'],
                  panel=PAIR_PANEL, panel_size=21, bg=YELLOWS[1],
                  notes='Twelve minutes. The conversation is the point: two people negotiating what a blend of their concepts would be is conceptual blending done aloud. Expect the three outcomes from the slide: collages, blends, and one concept eating the other. Make every pair say which one they got, and what came from where; that sentence is the caption. The TAs help with attaching several images and with the order.'))

S.append(question('image_upload', 'One per pair: the blend.',
                  hint='The image from round 2. Caption: A + B, and what came from each.',
                  eyebrow_text='08 · CAPTURE 2 · IMAGE UPLOAD · ONE PER PAIR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='Two minutes, one upload per pair, caption required. Put the blend wall next to the concept wall. Read three captions and, for each, ask the room: collage, blend, or one wins? Then ask which was harder: choosing the concept or writing the sentence that made the model blend rather than paste. The fours start as soon as the upload is in.'))

S.append(activity('4 — TWO PAIRS', 15, 'Four concepts. Three images. One picture.',
                  ['Join the pair behind you. Four concepts and two blends on the table. Say all four out loud. **Choose the three images that go in**, three at most: which stay out, and why?',
                   'One prompt: the thing you want, and what comes from each image. Run. Iterate by **swapping one image or changing one line**. Three runs.',
                   'Stop when all four agree it is **one thing**. Say which concept got lost, if one did. The scribe uploads it; **caption: the four concepts, and the lost one.**'],
                  panel=FOUR_PANEL, panel_size=21, bg=YELLOWS[2],
                  notes='Fifteen minutes in fours. The constraint is the lesson: four concepts, three inputs, so the group must decide what goes in; that is curating a dataset, week 11 in miniature. Most groups will lose a concept, and the one that survives best is the one with the strongest prototype: watch for it and name it in the debrief. This round is the start of Challenge 2: they finish it at home with concepts and references of their own.'))

S.append(question('image_upload', 'Scribes only: the four-way blend.',
                  hint='One image per four. Caption: the four concepts, and which one got lost, if one did.',
                  eyebrow_text='08 · CAPTURE 3 · IMAGE UPLOAD · ONE PER FOUR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='Scribes only, about 28 images, caption required. Put the three walls side by side: concepts, pairs, fours. Ask the room which wall has the most pictures that are one thing rather than a collage, and which concept got lost most often. Read two captions with a lost concept and ask why it lost: usually because the other concept had the stronger prototype, or because it went in as image 3. Download the submissions: the blends come back in week 5, when we push a model off the prototype properly.'))

S.append(content('08 · WHAT JUST HAPPENED', 'You blended concepts with a machine that has no definitions.',
                 ['Alone: your concept became its prototype. The picture the model found first was the middle of its examples, the typical bicycle, the typical justice. Rosch, on the wall.',
                  'In pairs: a blend, or a collage, or one concept ate the other. Where you got a collage, the machine combined like a rule: both, side by side. Where you got a blend, it did what no definition can do, and you cannot say how, and neither can it.',
                  'In fours: something got lost, and it was the concept with the weaker prototype. The middle pulls, in a mind and in a machine. You chose which examples went in, and in what order. That was the design.',
                  '**The machine made every image. You chose the concepts. That was the design.**'],
                 body_size=30,
                 notes='Mirror of the whole class. The prototype, on the concept wall; the combination problem, on the pair wall; curating the inputs, in the fours. Say the last line slowly: it is week 1\'s last line, and week 2\'s, with the noun changed. Module one is done: two ways to teach a machine, and you have used both.'))

S.append(cards('08 · CHALLENGE 2 · DUE BEFORE WEEK 4', 'A picture from text and references.', [
    ('THE CONCEPTS', 'Two or three, in a line each.',
     'Your own, not today\'s. Say each in a line: what it is, and what a picture of it must have.'),
    ('THE REFERENCES', 'One to three images, yours.',
     'Your photographs, your drawings, your round-1 picture: not other people\'s work. Say what each one is for.'),
    ('THE RESULT', 'One image, on Blackboard.',
     'The image, the prompt word for word, the references, and one sentence: what came from where, and what got lost. Name the model.'),
    ('THE VOTE', 'Bring it next week.',
     'The room votes in week 4; the winners get shown and a participation star. Evidence for your reflection: your second experiment of five.'),
], notes='Four things on Blackboard before next class: the image, the prompt, the references, one sentence. Own pictures only for the references; the model must be named. Next week the room votes. The one sentence is the reflection in miniature; tell them to write it while the difference between a blend and a collage is still fresh.'))

S.append(video('08 · HOMEWORK · WATCH BEFORE WEEK 4', 'Next week: language machines.', 'LPZh9BOjkQs',
               ['3Blue1Brown, "Large Language Models explained briefly": eight minutes on tokens, embeddings and transformers, the machine B that writes.',
                '- Watch it before class; the quiz in week 7 draws on it.',
                '- Bring the specs from week 2: next week they become briefs.',
                '- Also: a laptop, and your GenAI login.'],
               thumb='yt/LPZh9BOjkQs.jpg',
               notes='One video, short, on the playlist. Next week is the language model as a tool: tokens, embeddings, what a transformer does, hallucination and sycophancy, and prompting as briefing. The week-2 specs come back as briefs. Challenge 2 due before class; the TAs stay 30 minutes now.'))

S.append(end('See you next week. Language machines.',
             'Challenge 2 on Blackboard. Watch the 3Blue1Brown video. Bring a laptop.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Module one is done: two ways to teach a machine, and you have used both. Next week the tools begin with language. Homework in one line: the picture from text and references on Blackboard, the video, a laptop. The TAs stay for 30 minutes.'))

# After the class: links each question slide to the answers the room gave (README, "After the
# class: publish the answers"). deck/week03-reports.json is written by classpoint.py's weekly.py
# once the class has run; until it exists this is a no-op.
attach_reports(S, HERE / 'week03-reports.json')

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

# Sources (consulted 17 September 2026 while writing this deck)
# https://eric.ed.gov/?id=EJ128794 — Rosch (1975), Cognitive representations of semantic categories, J. Exp. Psych.: General 104(3): 209 raters, ten categories, a 1–7 goodness-of-example scale
# http://matt.colorado.edu/teaching/categories/rm75.pdf — Rosch & Mervis (1975), Family resemblances, Cognitive Psychology 7, 573–605
# https://en.wikipedia.org/wiki/Prototype_theory and https://en.wikipedia.org/wiki/Family_resemblance — typicality effects; Wittgenstein, Philosophical Investigations §66–67 (1953), "don't think, but look!"
# https://en.wikipedia.org/wiki/Meno — Meno's paradox (80d–e), recollection, the slave boy; the translation on the slide follows the 2025 deck (Plato, trans. 1998)
# https://en.wikipedia.org/wiki/Nix_v._Hedden — the tomato, a vegetable for tariff purposes, 1893
# https://en.wikipedia.org/wiki/Dartmouth_workshop — the proposal of 31 August 1955 (McCarthy, Minsky, Rochester, Shannon), the conjecture quoted, summer 1956
# https://en.wikipedia.org/wiki/GOFAI — Haugeland (1985), Artificial Intelligence: The Very Idea
# https://en.wikipedia.org/wiki/Perceptron and https://en.wikipedia.org/wiki/Frank_Rosenblatt — 1957–58, the Mark I (400 photocells, 20 × 20, motor-driven potentiometers), the New York Times of July 1958, Minsky & Papert 1969, Rosenblatt's death in 1971
# https://www.nature.com/articles/323533a0 — Rumelhart, Hinton & Williams (1986), Learning representations by back-propagating errors, Nature 323, 533–536
# https://www.nobelprize.org/prizes/physics/2024/summary/ — Hopfield and Hinton, Nobel Prize in Physics 2024, the citation quoted; https://en.wikipedia.org/wiki/Geoffrey_Hinton — Turing Award 2018, Google 2013–2023
# https://en.wikipedia.org/wiki/AlexNet — 30 Sept 2012, 15.3% vs 26.2%, 60 M parameters, 8 layers, two GTX 580 3 GB, 1.2 M images, about a week
# https://en.wikipedia.org/wiki/ImageNet — Fei-Fei Li, 2006 / CVPR 2009, 14 M images, 49,000 Mechanical Turk workers from 167 countries
# https://en.wikipedia.org/wiki/CUDA and https://en.wikipedia.org/wiki/GeForce_500_series — CUDA 2007; GTX 580: GF110, 512 CUDA cores, 16 streaming multiprocessors, 3.0 billion transistors
# https://deepmind.google/research/alphago/ and https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol — move 37, 10 March 2016, "1 in 10,000"; human games then self-play
# https://en.wikipedia.org/wiki/Generative_adversarial_network (2014) · https://arxiv.org/abs/1706.03762 (Attention is all you need, 2017) · https://en.wikipedia.org/wiki/GPT-3 (175 B, 2020) · https://en.wikipedia.org/wiki/Stable_Diffusion (22 Aug 2022) · https://en.wikipedia.org/wiki/ChatGPT (30 Nov 2022) · https://www.nobelprize.org/prizes/chemistry/2024/summary/ (Hassabis and Jumper)
# https://bfl.ai/models/flux-kontext (FLUX.1 Kontext, May 2025) · https://github.com/QwenLM/Qwen-Image/blob/main/Qwen-Image-Edit-2509.md (Qwen-Image-Edit-2509, Sept 2025: 1–3 input images) · https://bfl.ai/blog/flux-2 (FLUX.2, 25 Nov 2025, multi-reference)
# https://en.wikipedia.org/wiki/Conceptual_blending — Fauconnier & Turner (2002), The Way We Think: input spaces, generic space, the blend, selective projection, emergent structure
# Osherson & Smith (1981), On the adequacy of prototype theory as a theory of concepts, Cognition 9, 35–58 (the pet fish); Hampton (1988), Overextension of conjunctive concepts, J. Exp. Psych.: LMC 14, 12–32
# Typicality effects as listed in the 2025 deck: Hampton (1979); Rips, Shoben & Smith (1973); Rosch & Mervis (1975); Mervis & Pani (1980); Garrod & Sanford (1977)
# https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=WXuK6gekU1Y — "AlphaGo - The Movie" (Google DeepMind); https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=LPZh9BOjkQs — "Large Language Models explained briefly" (3Blue1Brown)
