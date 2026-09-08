"""
SD2112 · Artificial Intelligence in Design · Week 07 — the slide spec.

    python deck/week07.py            # builds _site/week07/ (html deck + pdf), export/week07*.pptx, export/preview/
    python deck/week07.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Mid-term: the Challenge 5 vote, the reflection (due today), the quiz on weeks 1–6 and the playlist
(run in ClassPoint quiz mode, Blackboard as the fallback; the twenty questions sit at the end of a
local classroom copy of the PowerPoint, never in this repository), the group project brief (40 %),
sixty-second pitches, and teams of four or five. Two live sketches: the course so far on one line
(rules ↔ examples), and a pitch timer; the same timer, set to twenty-five minutes, sits on the quiz
placeholder slide.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week07 as F                            # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full, timeline,   # noqa: E402
                     journey, activity, assessment, two_col, figure_slide, sketch_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(7)

# ───────────────────────── live sketches (html deck) ─────────────────────────
TWO_MACHINES_JS = """// The course so far, on one line: write the rule (left) or show the examples (right).
// The mouse is a product. Where it sits on the line decides what it is like, and which tool it is.
const items = [
  [0.04, 'a grid system', 'snap to 8 px: a rule you set once, and every screen obeys it', 'week 2'],
  [0.20, 'a parametric chair', 'chair(seat, width, back, angle, legs, splay): six numbers, a million chairs, never a beanbag', 'week 1'],
  [0.40, 'spell-check', 'a word list and four edits; the commonest candidate wins. Rules, plus a count', 'weeks 2 · 3'],
  [0.60, 'autocomplete', 'the next word, learned from what people typed: a small network on your phone', 'week 4'],
  [0.80, 'generative fill', 'a diffusion model trained on Adobe Stock invents what belongs in the hole', 'weeks 1 · 5'],
  [0.96, 'a diffusion model', 'noise, denoised step by step, steered by words. It cannot say why', 'weeks 5 · 6'],
];
const pairs = [['exact', 'fluent'], ['explainable', 'opaque'], ['brittle', 'typical'], ['hand-written', 'learned']];
const X0 = 90, X1 = 1310, Y = 330;                   // the line
const A = '#ED6D24', B = '#64C2C3', INK = '#000B1C', MUTED = '#5C6470';

function setup() { createCanvas(1400, 500); textFont('JetBrains Mono'); }

function draw() {
  background(255);
  let t = constrain((mouseX - X0) / (X1 - X0), 0, 1);     // 0 = all rule, 1 = all examples
  let tone = lerpColor(color(A), color(B), t);
  // the line, and the six products on it
  stroke('#E1E1DE'); strokeWeight(6); line(X0, Y, X1, Y);
  let near = 0;
  for (let i = 0; i < items.length; i++) {
    let x = X0 + items[i][0] * (X1 - X0);
    if (abs(items[i][0] - t) < abs(items[near][0] - t)) near = i;
    noStroke(); fill(lerpColor(color(A), color(B), items[i][0])); circle(x, Y, 16);
    fill(INK); textSize(16); textAlign(CENTER, BASELINE); text(items[i][1], x, Y - 40);
  }
  noStroke(); textAlign(LEFT, BASELINE); textSize(18); fill(A); text('RULES · MACHINE A', X0, Y + 46);
  textAlign(RIGHT); fill(B); text('EXAMPLES · MACHINE B', X1, Y + 46);
  textSize(14); fill(MUTED); textAlign(LEFT); text('write the rule · weeks 1, 2', X0, Y + 68);
  textAlign(RIGHT); text('show the examples · weeks 3 to 6', X1, Y + 68);
  // the marker: where the mouse says the product is
  let mx = X0 + t * (X1 - X0);
  stroke(INK); strokeWeight(3); line(mx, Y - 26, mx, Y + 30);
  noStroke(); fill(INK); circle(mx, Y, 26);
  // what it is like there: four pairs of words, the dot between them
  for (let k = 0; k < pairs.length; k++) {
    let col = k % 2, row = floor(k / 2);
    let bx = 330 + col * 680, by = 150 + row * 48, bw = 250;
    stroke('#E1E1DE'); strokeWeight(4); line(bx, by, bx + bw, by);
    noStroke(); fill(INK); circle(bx + t * bw, by, 14);
    textSize(16); textAlign(RIGHT, CENTER); fill(lerpColor(color(INK), color('#C9CBC7'), t)); text(pairs[k][0], bx - 14, by);
    textAlign(LEFT, CENTER); fill(lerpColor(color('#C9CBC7'), color(INK), t)); text(pairs[k][1], bx + bw + 14, by);
  }
  // the product nearest the marker
  fill(INK); textAlign(LEFT, BASELINE); textSize(34); text(items[near][1], X0, 62);
  fill(MUTED); textSize(16); text(items[near][2], X0, 92);
  fill(tone); textSize(14); text(items[near][3].toUpperCase() + '  ·  ' + round(t * 100) + ' % EXAMPLES', X0, 116);
  fill(MUTED); textSize(14); textAlign(RIGHT); text('most products are a mix. the designer decides where on the line it sits.', X1, 436);
  textAlign(LEFT); text('move the mouse along the line', X0, 436);
}"""

TIMER_JS = """// A pitch timer. Click to start; click again to reset. + and - change the length.
const START = 60, WARN = 15;             // seconds: orange when WARN are left, red at zero
const PITCH = true;                      // the four beats of a pitch, and a count of pitches done
const BEATS = [['the person', 10], ['the decision', 20], ['for whom', 10], ['with what data', 20]];
let total = START, t0 = -1, left = START, done = 0;

function setup() { createCanvas(1400, 500); textFont('JetBrains Mono'); }

function draw() {
  background(255);
  if (t0 >= 0) left = max(0, total - (millis() - t0) / 1000);
  let col = left <= 0 ? '#D22B2B' : left <= WARN ? '#ED6D24' : '#64C2C3';
  // the ring drains
  noFill(); strokeCap(SQUARE); strokeWeight(28);
  stroke('#E1E1DE'); circle(250, 250, 400);
  if (left > 0) { stroke(col); arc(250, 250, 400, 400, -HALF_PI, -HALF_PI + TWO_PI * left / total); }
  // the number
  noStroke(); fill(left <= 0 ? '#D22B2B' : '#000B1C'); textAlign(CENTER, CENTER);
  textSize(ceil(left) >= 100 ? 110 : 170); text(clock(left), 250, 242);
  // the words
  textAlign(LEFT, BASELINE); fill('#000B1C'); textSize(40);
  text(t0 < 0 ? 'click to start' : left <= 0 ? 'time. click to reset' : PITCH ? 'pitch ' + (done + 1) : 'running', 540, 140);
  fill('#5C6470'); textSize(20);
  text('length ' + clock(total) + '   ·   + and - change it' + (PITCH ? '   ·   pitches done: ' + done : ''), 540, 186);
  if (!PITCH) {                                          // the quiz clock: the rules, not the beats
    fill('#000B1C'); textSize(20);
    text('twenty questions · one at a time · answer once', 540, 300);
    text('a closed question stays closed · laptops closed · no talking', 540, 336);
    text('finished: phone face down · late: join at the question on screen', 540, 372);
    fill('#5C6470'); textSize(17); text('blackboard only when gio says so. nobody switches alone.', 540, 412);
    return;
  }
  // the four beats, and where the pitch is now
  let x0 = 540, w = 800, y = 290, e = total - left, acc = 0;
  for (let [name, secs] of BEATS) {
    let bx = x0 + acc / 60 * w, bw = secs / 60 * w;
    let on = t0 >= 0 && left > 0 && e >= acc / 60 * total && e < (acc + secs) / 60 * total;
    fill(on ? col : '#F4F4F2'); rect(bx, y, bw - 4, 60);
    fill(on ? '#FFFFFF' : '#000B1C'); textSize(15); textAlign(LEFT, CENTER); text(name, bx + 12, y + 30);
    fill(on ? '#FFFFFF' : '#5C6470'); textSize(14); text(round(secs / 60 * total) + ' s', bx + 12, y + 50);
    acc += secs;
  }
  stroke('#000B1C'); strokeWeight(3); let mx = x0 + constrain(e / total, 0, 1) * w; line(mx, y - 12, mx, y + 72);
  noStroke(); fill('#5C6470'); textSize(14); textAlign(LEFT, BASELINE);
  text('no slides, no demo, the product\\'s name last. the room writes three words per idea.', x0, 420);
}

function clock(s) { s = ceil(s); return s >= 100 ? floor(s / 60) + ':' + nf(s % 60, 2) : '' + s; }

function mousePressed() {
  if (t0 < 0) t0 = millis();                              // start
  else { if (total - left >= 5) done++; t0 = -1; left = total; }   // reset; a run of 5 s or more counts as a pitch
}

function keyPressed() {
  if (key === '+' || key === '=') total += 15;
  else if (key === '-' || key === '_') total = max(15, total - 15);
  else return;                                           // every other key goes to the deck
  if (t0 < 0) left = total;
  return false;                                          // keep + and - from the deck
}"""

QUIZ_TIMER_JS = TIMER_JS.replace('const START = 60, WARN = 15;', 'const START = 1500, WARN = 60;').replace('const PITCH = true;', 'const PITCH = false;')

TEAM_CHECKLIST = [
    'THE TEAM CHECKLIST', ' ',
    '[ ] four or five people',
    '[ ] at least three of the five kinds of work',
    '[ ] one scribe: the log, the board, the brief',
    '[ ] a team name, not a person\'s name',
    '[ ] the idea in one line: the person, the',
    '    decision, for whom, with what data', ' ',
    'THEN', ' ',
    '[ ] scribe: register on ClassPoint (next slide)',
    '[ ] scribe: sign the team up on Blackboard',
    '    (Groups) before you leave the room',
    '[ ] everyone: the team\'s chat, today',
    '[ ] the proposal, one page, for week 8',
]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 07 · MID-TERM',
               'Mid-term.',
               'Week 7 — the quiz, your pitches, and teams. The reflection is due today.',
               notes='Join code on screen from 30 minutes before; the TAs are checking that everyone can join, because the quiz runs on ClassPoint. Three parts today: the quiz on weeks 1 to 6, then, after the break, the group project — your pitches and your teams. Phones charged, laptops closed for the first half.'))

S.append(agenda('SD2112 · WEEK 07', [
    'Last week, in your words', 'The reflection: due today', 'The quiz: how it works', 'The quiz',
    'The group project: 40%', 'Pitches: sixty seconds each', 'Teams of four or five', 'Guest slot · week 8',
], notes='Eight stops, three parts. Before the break: the Challenge 5 vote, the reflection, then the quiz — ten percent, twenty questions, twenty-five minutes. After the break: the group project brief, sixty seconds for everyone who wants to pitch, and teams of four or five formed in the room. If a guest is confirmed, they take thirty minutes after the break and the pitches are capped.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'challenge 5 · the reflection · the map', bg=INK,
                 notes='Twelve minutes: what you want back before the quiz, the last challenge vote, the reflection, and where we are.'))

S.append(question('word_cloud', 'The one idea you want back before the quiz.',
                  hint='One word or two: "tokens", "CLIP", "Move 37", "Markov", "mediation". The three biggest words get two minutes each, right before the quiz.',
                  eyebrow_text='01 · WARM-UP · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each, ninety seconds. This is the revision agenda: read the three biggest words and promise them two minutes each on the recap slide. Expect tokens, diffusion, CLIP, mediation, Markov. Keep the screenshot: the least-sure answers after the quiz will match it, and that is what week 8 opens with.'))

S.append(cards('01 · CHALLENGE 5 · FOUR ENTRIES · BY SPEC', 'Thirty seconds of sound.', [
    ('ENTRY A', 'The spec', '"a bike-share app · the lock clicks open · 3 s · marimba, no voice · the model added a reverb tail; kept"'),
    ('ENTRY B', 'The spec', '"a meditation timer · the last ten seconds · 10 s · a bowl, then silence · generated twice, the second one edited"'),
    ('ENTRY C', 'The spec', '"a night bus app · your stop is next · 2 s · two notes, up · sequenced by hand; the rule is the sound"'),
    ('ENTRY D', 'The spec', '"a plant-care app · the pot is dry · 4 s · water, a wooden knock · the model gave a ukulele; undone"'),
], text_size=22, notes='Replace these four with the real ones: the four best Challenge 5 entries from Blackboard, anonymised, the spec on the card and the sound played from the Blackboard page. Read each spec before playing its sound and ask the room to guess what the model decided that the spec did not say. Four sounds, four specs, five minutes.'))

S.append(question('multiple_choice', 'Challenge 5: which sound gets the star?', [
    'Entry A', 'Entry B', 'Entry C', 'Entry D',
], eyebrow_text='01 · CHALLENGE 5 · AWARDS · MULTIPLE CHOICE',
    notes='ClassPoint vote, one minute. No correct answer: the room decides, the winner gets a participation star and thirty seconds on what the model decided that they kept or undid. The TAs add one more star for the best-written spec. This was the last challenge: from today the making moves into the group project, and all five challenges are the evidence in the reflection.'))

S.append(content('01 · THE REFLECTION · 20% · DUE TODAY', 'The reflection is due today.',
                 ['**On Blackboard, today; the time is on the assignment page.** About 1000 words: the role of AI in your creative process, with particular attention to the difference between rule-based and adaptive systems.',
                  '- Evidence: at least three of your own experiments from the challenges of weeks 2 to 6, with images. The walls from class are on Blackboard.',
                  '- **The process note, at the end:** which tools you used to write it, and how. Allowed, expected, disclosed. A missing note costs one grade band on clarity and style.',
                  '- Invented citations fail the assignment. Check every reference before you press submit.',
                  'Not submitted yet? Talk to Amber at the break. The TAs\' desk is for uploads, not for edits.'],
                 body_size=30,
                 notes='Say the time out loud — Amber confirms it before class. If the assignment closes during the class, say so now and once more at the break; if it closes later today, say the time and nothing more. The process note is the thing people forget: one paragraph, which model, for what, and what you changed. Programme policy on late work applies; ask before the deadline, not after. Anyone in trouble goes to Amber at the break, not now.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(2, 0),
                 notes='The middle of the semester. Six weeks of what AI is and how to use it in your own process are behind you; the quiz closes them. Six weeks of AI inside a product are ahead, and they are the group project: module three is what the product needs, module four is what is left for the designer, week 13 is the fair and the final quiz. Today is the hinge.'))

# ───────────────────────── 02 · the quiz ─────────────────────────
S.append(section('02', 'The mid-term quiz', '10% · weeks 1 to 6 · the playlist · multiple choice', bg=INK,
                 notes='Chapter two: the recap in one picture, how the quiz works on ClassPoint and on Blackboard, the rules of the room, then the quiz itself. Forty-five minutes including the quiz.'))

S.append(sketch_slide('02 · LIVE · SIX WEEKS ON ONE LINE', 'Six weeks in one picture.',
                      live('w07-two-machines', TWO_MACHINES_JS, 1400, 500, hint='move the mouse along the line: the product changes, and so do its properties'),
                      body=['One line, two ends. Write the rule: exact, explainable, brittle, hand-written. Show the examples: fluent, opaque, typical, learned. Every tool from the six weeks sits somewhere on it, and most products are a mix. The quiz asks, twenty times, where.'],
                      caption='Grid system, parametric chair, spell-check, autocomplete, generative fill, a diffusion model: six products, one line. Spell-check is a word list and four edits plus a count of what people write; autocomplete is a small network trained on what people typed. The mix is the point.',
                      notes='Walk the line slowly, left to right, and say the week for each stop: the grid and the chair are week 2 and week 1, spell-check is rules with a count, autocomplete is week 4 in your pocket, generative fill and the diffusion model are weeks 1 and 5. Then the words: at every stop ask which four words apply. Give the three biggest words from the warm-up cloud two minutes each here — tokens, CLIP, Markov, whatever they were — with the deck of that week open on the second screen. This is the last thing before the quiz; do not add new material.'))

S.append(figure_slide('02 · HOW IT WORKS', 'Twenty questions. Twenty-five minutes. One attempt.', F.w07_quiz_flow(),
                      body=['One idea, four choices, one right answer, weeks 1 to 6 and the playlist, in course order. On ClassPoint, one question at a time on the big screen and on your phone, about a minute each; a closed question stays closed. If ClassPoint fails the room we switch to a Blackboard test with the same questions and a 25-minute timer — only when Gio says so.'],
                      caption='Ten percent. The marks come from the ClassPoint summary, or from the Blackboard test, onto Blackboard within the week. The mock questions in week 6 were the model.',
                      notes='Two lanes, one quiz. The plan is ClassPoint quiz mode: Nicolò jumps to the quiz slides at the end of the classroom copy, each question is a multiple-choice activity in quiz mode, one right answer, auto-marked. Say the pace: about a minute per question, you answer once, then it closes and the next opens; there is no going back, so answer every question. The fallback is a Blackboard test with a timer, the same twenty questions in random order, one attempt, submitting itself at 25 minutes. Nobody switches lanes alone: if the room switches, everyone switches, and I say so.'))

S.append(cards('02 · TWO WAYS TO RUN IT · AND THE ROOM', 'The plan, the fallback, the rules.', [
    ('THE PLAN · CLASSPOINT', 'Quiz mode, on your phone.',
     ['Join with the class code and your ID. Each question opens on the big screen and on your phone, stays open about a minute, then closes and the next one opens.',
      'Answer once. It is marked automatically. Twenty questions.']),
    ('THE FALLBACK · BLACKBOARD', 'A test with a timer.',
     ['Only if Gio says so. Blackboard → SD2112 → Mid-term quiz: the same twenty questions in random order, 25 minutes on the clock, one attempt.',
      'It submits itself when the time is up. Laptop or phone.']),
    ('THE ROOM', 'Quiet, closed, face down.',
     ['Laptops closed unless we switch to Blackboard. No talking, no second screen, no notes, no chatbot.',
      'Late: you join at the question on screen; the closed ones stay closed. Finished: phone face down until the last question closes.']),
], text_size=22, notes='Read the third card aloud, all of it. During the quiz Nicolò drives the deck, Amber sits at the desk with the Blackboard fallback hidden and ready, WU Zhao and MA Jie walk the aisles from the back and the side. Someone arriving late joins at the question on screen and that is that — say it now so nobody argues later. Anyone whose phone dies borrows the TAs\' spare, or joins from classpoint.app in a laptop browser at the front on a TA\'s say. Nobody goes to Blackboard alone.'))

S.append(sketch_slide('02 · THE QUIZ · 25 MINUTES', 'Quiz: open the ClassPoint quiz mode.',
                      live('w07-timer-quiz', QUIZ_TIMER_JS, 1400, 500, hint='click to start the clock · click again to reset · + and - change the length'),
                      body=['The questions are not in this deck: in the classroom copy they sit after slide 34, and Nicolò jumps there from here and back after question twenty. This clock stays on the second screen. Blackboard fallback: the test opens at Gio\'s word and closes itself 25 minutes later.'],
                      caption='A placeholder. The twenty questions are never in the published deck; they live at the end of the classroom copy on the PC and in the Blackboard test, and change every year.',
                      notes='Placeholder: this slide is what the room sees for a moment while Nicolò types 35 and Enter to jump to the first quiz slide — the same slideshow, so nobody rejoins ClassPoint. Start the clock with a click when question one opens; it turns orange at the last minute and red at zero. The quiz slides: twenty multiple-choice slides in quiz mode, one right answer each, about a minute per question — Nicolò closes each question when the room has answered and opens the next. After the last question: phones face down, then 14 and Enter brings the deck back to the next slide. If we are on Blackboard instead, this clock is the only thing on screen for 25 minutes.'))

S.append(question('short_answer', 'The question you were least sure about.',
                  hint='One line: the topic, or the number of the question. Names are hidden. It decides what week 8 opens with, and what the final quiz revisits.',
                  eyebrow_text='02 · AFTER THE QUIZ · SHORT ANSWER · ANONYMOUS',
                  cp={'type': 'short_answer', 'hide_names': True, 'multiple': False},
                  notes='Anonymous short answer, two minutes, straight after the quiz while it is fresh. Read six aloud, sorted by topic; do not give the answers yet — the marks are not out. Match the list against the warm-up cloud: the overlap is what week 8 opens with, and it is the revision list for the final quiz. Then the break.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · THE GROUP PROJECT · PITCHES · TEAMS', size=120, bg=PAPER,
                   notes='1:00. Anyone who has not submitted the reflection: Amber, now. Everyone who wants to pitch: your name on the list at the door before you come back — the TAs keep it, first come, first on. Bring one sentence.'))

# ───────────────────────── 03 · the group project ─────────────────────────
S.append(section('03', 'The group project', '40% · four or five people · a poster, a video, one page · week 13', bg=ORANGES[0],
                 notes='Chapter three, after the break: the brief. One sentence, three deliverables, the rubric, and the milestones week by week. Twenty-five minutes.'))

S.append(figure_slide('03 · THE BRIEF · ONE SENTENCE', 'A model decides something for each person.', F.w07_decision_loop(),
                      body=['**And you account for what that does to them.** Not a tool: a thing you ship, with a model inside that decides — show, rank, suggest, refuse — for the person in front of it, from what it knows about them. The loop is the design.'],
                      caption='Using AI is weeks 1 to 6. Incorporating it is weeks 8 to 12: the model is inside the product, and its decision is your design decision.',
                      notes='Read the sentence twice. "Decides something for each person" is the test of every idea you will hear today: if the product shows everyone the same thing, there is no model deciding, and it is not this brief. Walk the loop: the person gives off data, the model turns it into a decision, the decision changes what the person sees and does, and that changes the data. The four orange questions are the four sections of the one-page brief; every one of them has a week that answers it. Ask the room for a product they used this morning that sits on this loop. There will be five.'))

S.append(question('multiple_choice', 'Which of these is "a model deciding something for each person"?', [
    'A poster with a QR code to the same page for everyone', 'The artwork Netflix picks for your account', 'A grid system that snaps every box to 8 px', 'A variable font at weight 600',
], eyebrow_text='03 · QUICK CHECK · MULTIPLE CHOICE',
    notes='B. Netflix shows the same film with a different picture per account, chosen by a model from what you watched; the viewer never sees the choice. A shows everyone the same thing; C and D are rules, machine A with no one in particular in mind. The test for every pitch this afternoon is the one in the question.'))

S.append(cards('03 · THREE DELIVERABLES · WEEK 13', 'A poster, a video, one page.', [
    ('A0 POSTER', 'The research and the concept.',
     ['Who the person is, what the model decides, what that does to them: the argument on a wall, readable from two metres, with the sources on it.',
      'Rubric: research and contextual analysis 30; communication and poster design 20.']),
    ('VIDEO · 3 TO 5 MINUTES', 'How it works, for a stranger.',
     ['One person, one session, the decision being made and felt. Not a feature list; a story with a model in it. Shown at the fair on a loop.',
      'Rubric: video presentation 10.']),
    ('MEDIATION BRIEF · ONE PAGE', 'The relation, the data, the bias, the guardrails.',
     ['Four answers on one page, in the vocabulary of weeks 5, 9, 11 and 12. The part of the project that the ethics mark reads first.',
      'Rubric: ethical and sociological impact 30.']),
], text_size=22, sub='Behind them, a process log: the evidence for the team-and-process ten percent.', notes='Three things on the wall in week 13, and a process log behind them. The poster carries the research: sources on the poster, not in a folder. The video is for someone who has never seen the product — one person, one session. The brief is one page and it is where the theory shows up: the relation, the data, the bias, the guardrails. Next slide, its anatomy.'))

S.append(figure_slide('03 · THE MEDIATION BRIEF', 'One page. Four questions. Every answer has a week.', F.w07_brief_anatomy(),
                      body=['Which relation, and how hard does it push? What must the model know, and where from? Where is it wrong, and for whom? What may it not decide, and who answers when it does? One page, in the words of the course.'],
                      caption='Ihde 1990 and Verbeek 2015 for the relation (week 5). Data, bias and the bias register: weeks 8 to 10. Guardrails, output curation and explainability: weeks 11 and 12. Due in week 11.',
                      notes='Go section by section. The relation: one of Ihde\'s four or Verbeek\'s three, and its force — hidden or apparent, weak or strong; you did this for a layout tool in week 5, now do it for your product. The data: what it needs, given, taken or inferred, and consent; week 8 and week 9 give you the words. The bias: the four kinds and the bias register, week 9. The guardrails: what it may not decide, when a human is in the loop, how it fails in front of a person — weeks 11 and 12. The brief is due in week 11; start it in week 8 with the proposal, because the proposal is its first two sections.'))

S.append(assessment('03 · THE RUBRIC · 40%', 'Five criteria.', [
    ('30%', 'Research and contextual analysis', 'Thorough, well-structured research from multiple credible sources; the product situated in the AI-and-design discourse.', False),
    ('30%', 'Ethical and sociological impact', 'The mediation brief names the relation, the data, the bias and the guardrails convincingly; risks and opportunities, not generalities.', True),
    ('20%', 'Communication and poster design', 'Visually clear, engaging, professional; well organised; a balance of visuals and text.', False),
    ('10%', 'Video presentation', 'Clear, well paced; explains the product and its implications; polished.', False),
    ('10%', 'Team and process', 'Team collaboration and process documentation: strong shared effort; a transparent, documented process; roles clear. The scribe\'s log is the evidence.', False),
], notes='Sixty percent of the mark is research and ethics, forty is craft. Say that slowly: this is not a prototype competition, and a beautiful poster for a shallow idea sits at C. The last ten percent is the one teams lose: a process log, who did what, when. That is the scribe\'s job, and today every team appoints one. The full rubric with the A, B and C bands, under these five names, is in the syllabus on the course site and on Blackboard.'))

S.append(timeline('03 · WEEK BY WEEK', 'Six weeks, six milestones.', [
    ('WEEK 8', 'Proposal', 'One page: the decision the product makes, for whom, with what data. Drafted before the class, finished in it, on Blackboard after it.'),
    ('WEEK 9', 'Concept board + bias register', 'The concept on a board. Where the data and the model are wrong, and for whom: a register, kept from now on.'),
    ('WEEK 10', 'Prototype v1', 'The interaction: paper, Figma or code. The decision, made and shown to one person.'),
    ('WEEK 11', 'Draft poster + mediation brief', 'The A0 in draft; the one page in full. Feedback from the TAs in the poster lab.'),
    ('WEEK 12', 'Final poster and video', 'Ready. The mock poster session: two rounds, half the teams present, half review with the rubric card; one fix each.'),
    ('WEEK 13', 'The fair', 'A0 posters, 3 to 5 minute videos, peer and instructor feedback. Then the final quiz, same class.'),
], notes='One milestone a week, each one checked in class by the TAs; none of them is graded on its own, all of them feed the forty percent. The proposal is next week: one page, the three things in the pitch format. Week 13 is the fair and the final quiz in the same three hours, so the poster and the video are ready in week 12, not in week 13. Amber is the TA for the group project: feedback on work in progress, before and after every class.'))

# ───────────────────────── 04 · pitches ─────────────────────────
S.append(section('04', 'Pitches', 'sixty seconds · the person · the decision · for whom · the data', bg=INK,
                 notes='Chapter four: everyone who wants to pitch gets sixty seconds, the format is four beats, and the room writes three words per idea. Forty-five minutes at most; the sign-up list from the door decides the order.'))

S.append(figure_slide('04 · THE FORMAT', 'Sixty seconds, four beats.', F.w07_pitch_anatomy(),
                      body=['Ten seconds for the person in front of the product. Twenty for the one thing the model decides for them. Ten for who else, and who is left out. Twenty for the data, and where it comes from. No slides, no demo.'],
                      caption='The four beats are the four lines of the week-8 proposal and the first two sections of the mediation brief. A pitch that has them is a proposal already.',
                      notes='Read the bar left to right with the example, then say the rule: if you cannot say the decision in one sentence, it is not a pitch yet. The room is listening for one thing — a decision a model makes for a person — and for one more: whether they would join. Nobody needs to pitch; everybody needs to listen and write three words for the ideas they would join. The timer is on the next slide; sixty seconds, and it does not care.'))

S.append(sketch_slide('04 · LIVE · YOUR SIXTY SECONDS', 'Your sixty seconds.',
                      live('w07-timer', TIMER_JS, 1400, 500, hint='click to start · click again to reset · + and - change the length'),
                      body=['One click when you start. The ring drains; the bar underneath shows which beat you should be in. Orange at fifteen seconds, red at zero — and at zero you stop, mid-sentence if you must. The next person is already walking up.'],
                      caption='The timer counts the pitches done. Nicolò runs it from the html deck; + and − change the length in fifteen-second steps if the room is short of time.',
                      notes='Nicolò clicks; the pitcher speaks; the room writes. Keep the rhythm brutal and kind: thank, next. Between pitches say the number and the pitcher\'s first name only, no more. Every five pitches, glance at the join answers coming in on the ClassPoint screen — if an idea is getting nothing, it may be the pitch, not the idea; say so gently at the end. At thirty pitches, or at 2:21, stop, whatever the list says; the leftovers pitch at their tables in the forming round.'))

S.append(question('short_answer', 'The idea you would join, in three words.',
                  hint='Submit as many times as you like, one line per idea, while the pitches run: "night bus · alarms · ward". The wall is the market for the next twenty minutes.',
                  eyebrow_text='04 · WHILE THE PITCHES RUN · SHORT ANSWER · ANONYMOUS · MULTIPLE SUBMISSIONS',
                  cp={'type': 'short_answer', 'hide_names': True, 'multiple': True},
                  notes='Open this activity before the first pitch and leave it open on the second screen through all of them; multiple submissions are on, so one person can name five ideas. After the last pitch put the wall up: the ideas with the most lines are the tables that will fill first, and the ones with none need a merger. Read the three most-named aloud. Names are hidden: the wall counts demand, and the walk to the numbered sheets does the matching.'))

S.append(question('word_cloud', 'The domain of the idea you want to build. One word.',
                  hint='health · transport · food · music · learning · money · home · care · games · the city. The cloud shows where the room is going, and where nobody is.',
                  eyebrow_text='04 · AFTER THE PITCHES · WORD CLOUD',
                  notes='One word each, one minute. The cloud is the map of the room: three big words and a lot of small ones. Point at the big ones: five teams in health means five teams competing for the same references; point at the empty ones: nobody in money, nobody in the city — a team that goes there has the fair to itself. Then the teams.'))

# ───────────────────────── 05 · teams ─────────────────────────
S.append(section('05', 'Teams', 'four or five · mixed skills · one scribe · registered today', bg=YELLOWS[0],
                 notes='Chapter five: what a team needs, twelve minutes to form, and the registration — on ClassPoint now, on Blackboard before you leave. Nicolò keeps time; Amber, WU Zhao and MA Jie place the leftovers.'))

S.append(figure_slide('05 · WHAT A TEAM NEEDS', 'Four or five people. Five kinds of work.', F.w07_team_skills(),
                      body=['Research, concept and prototype, visual, video and story, a scribe. Five kinds of work, not five roles; everyone does two. Mixed skills: every deliverable has a line into it. The scribe keeps the log, the ten percent most teams lose.'],
                      caption='Teams of four or five; ~114 people is about twenty-five teams. A team of three is not a team yet; a team of six is two teams of three. The TAs move people until the numbers work.',
                      notes='The figure is the argument for mixing: five illustrators make a poster and no brief; five coders make a demo and no poster. When you walk to a table, look at who is already there and at the lines on this slide. The scribe is not the leader; the scribe is the one who writes down who did what, and that log is a tenth of the mark. Then: twelve minutes.'))

S.append(activity('FORM', 12, 'Find your four.',
                  ['The pitchers stand at a numbered spot along the walls, the idea on a sheet: **three words**. Ideas nobody named: merge, or come to the desk.',
                   'Everyone else walks to an idea. A spot is full at **five**; the sixth person moves on. Four is a team; three is not yet.',
                   'Mix the kinds of work. Choose a **scribe**. Name the team.',
                   'Nobody at the twelfth minute: the TAs\' desk. You will be placed, today.'],
                  panel=TEAM_CHECKLIST, panel_size=23, bg=YELLOWS[0],
                  notes='Twelve minutes on the clock; Nicolò calls six, nine and twelve. The pitchers go first: one per spot, the sheet with three words held up. Watch the tables that fill past five and split them — two teams of three cannot stay two teams of three, so a full table of six sends two people to the nearest table of three. At nine minutes the TAs start placing whoever is still walking; at twelve nobody is without a team. If two tables have the same idea, they are two teams with the same idea, and that is fine; the fair will show two answers.'))

S.append(question('short_answer', 'Scribes: the team name, and the idea in one line.',
                  hint='"Night Shift · a ward app decides which alarms a nurse hears first, from the ward\'s logs". One per team, no people\'s names. Then the Blackboard sign-up.',
                  eyebrow_text='05 · REGISTER · SHORT ANSWER · ONE PER TEAM',
                  notes='Scribes only, one line per team, about twenty-five lines, three minutes. Put the wall up and read five: every line should have a person, a decision and a source of data in it; where one is missing, say so — that is the proposal\'s first correction. Amber opens the Blackboard group sign-up now; the scribe adds the members before the room empties, and the TAs check the numbers against this wall. Download the list: it is the team register for the semester.'))

# ───────────────────────── 06 · guest · week 8 ─────────────────────────
S.append(content('06 · GUEST LECTURE · IF CONFIRMED', 'A guest, when the slot is confirmed.',
                 ['This slide is a placeholder. When a guest is confirmed, the talk takes thirty minutes after the break, before the pitches; the pitches are capped at twenty, from the sign-up list at the door.',
                  '- The slide that replaces this one carries the guest\'s name, affiliation and the title of the talk, written the way they want it written.',
                  '- The brief for the guest: a product with a model inside that decides something for each person, and what that did to the people who used it. Twenty minutes of talk, ten of questions.',
                  '- No guest: this slide is skipped and the time goes to the pitches.'],
                 body_size=30,
                 notes='Placeholder, hidden or replaced on the day. If a guest is confirmed: swap this slide for their title slide, move it to right after the break, and tell Nicolò the pitch cap is twenty. The question to ask the guest in front of the room is the one on the loop: what did the model decide, and what did that do to people? That is the brief the teams just received, seen from the inside.'))

S.append(content('06 · BEFORE WEEK 8', 'Bring the idea and the team.',
                 ['**The team**, on Blackboard (Groups) before you leave the room: four or five people, a name, a scribe. Not there by tomorrow: Amber registers you from your scribe\'s line.',
                  '**The proposal**, one page, drafted before the class and finished in it: the decision the product makes, for whom, with what data — the four beats of the pitch, written down. On Blackboard after week 8.',
                  '**One product** that decided something for you today — a feed, a route, a price, an autocomplete — and one line on what it decided. Week 8 opens with those.',
                  '**The quiz marks** on Blackboard within the week; the least-sure list opens week 8.',
                  f'[{SITE}]({"https://" + SITE}) · [{PLAYLIST.replace("https://", "")}]({PLAYLIST})'],
                 body_size=30,
                 notes='Four things, one of them new: the product that decided for you. Everyone has one on their phone; the line they write is the first sentence of week 8, which is AI as design material — using versus incorporating, a product that decides something for each person, the double diamond with a model inside. Teams sit together from week 8. The TAs stay for thirty minutes: team registration, and the reflection for anyone still stuck.'))

S.append(end('See you next week. AI as design material.',
             'Bring the idea and the team. Sit together.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: AI as design material — using versus incorporating, the model inside the product, the proposal in class. Homework in one line: the team on Blackboard, one page of proposal, one product that decided for you. The TAs stay for 30 minutes.'))

DECK = dict(title='SD2112 · AI in Design · Week 07', slides=finalize(S, FOOTER), pdf='SD2112-week07.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week07', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 5–6 September 2026)
# Course facts (weights, deliverables, rubric, milestones, team size, the reflection and its process note, the playlist):
#   syllabus/SD2112-syllabus-2026.md (this repository) and deck/week06.py (the mock quiz and the week-7 order announced there)
# ClassPoint:
#   https://www.classpoint.io/features/quiz-mode  (Quiz Mode converts multiple-choice slides; auto-marking; stars by difficulty;
#       the Quiz Summary with correct count and answer speed; export to Excel)
#   https://www.classpoint.io/features/multiple-choice  (multiple choice is the only activity that runs in Quiz Mode)
#   https://www.classpoint.io/features/timer-stopwatch  (the add-in's own countdown timer and stopwatch, docked or full screen)
#   https://www.classpoint.io/blog/student-guide-to-classpoint  (students join at classpoint.app "on any browser with any device"
#       with the class code and a name: the laptop-browser route for a dead phone)
# Blackboard tests (the fallback lane):
#   https://help.anthology.com/blackboard/instructor/en/assessments/tests.html  (Ultra: the Tests landing page; the settings
#       are on its sub-pages, below)
#   https://help.anthology.com/blackboard/instructor/en/assessments/assessment-settings/time-limit.html  (whole minutes, 1 to 1440;
#       "work is automatically saved and submitted when time expires", or extra time after the limit)
#   https://help.anthology.com/blackboard/instructor/en/assessments/assessment-settings/presentation-options.html  (randomise
#       questions; randomise answers for Multiple Choice and Multiple Answer questions)
#   https://help.anthology.com/blackboard/instructor/en/assessments/assessment-settings/grading---submissions.html  (the number
#       of attempts allowed)
#   https://sites.reading.ac.uk/TEL-Support-Staff/blackboard-ultra-tests-settings/  (attempts allowed 1–10 or unlimited;
#       randomise questions and answers; "work is automatically saved and submitted when the time expires")
# The jump to the quiz slides (one slideshow, so the room never rejoins ClassPoint):
#   https://support.microsoft.com/en-us/office/use-keyboard-shortcuts-to-deliver-powerpoint-presentations-1524ffce-bd2a-45f4-9a7f-f18b992b93a0
#       ("Go to a specific slide: type the slide number, then press Enter")
# The mediation brief's vocabulary:
#   https://dl.acm.org/doi/10.1145/2751314  Verbeek, P.-P. (2015). Beyond interaction: a short introduction to mediation theory.
#       Interactions 22(3), 26–31 (Ihde's four relations as schemas; cyborg, immersion, augmentation; visibility and force)
#   https://research.utwente.nl/en/publications/cover-story-beyond-interaction-a-short-introduction-to-mediation-/
#   Ihde, D. (1990). Technology and the Lifeworld: From Garden to Earth. Indiana University Press
#       (embodiment, hermeneutic, alterity, background) — https://www.goodreads.com/book/show/556451.Technology_and_the_Lifeworld
# The six products on the line (the w07-two-machines sketch):
#   https://norvig.com/spell-correct.html  Norvig, How to Write a Spelling Corrector (a word count and four edits:
#       deletes, transposes, replaces, inserts; the commonest candidate wins)
#   https://arxiv.org/abs/1811.03604  Hard et al. (2018). Federated Learning for Mobile Keyboard Prediction
#       (Gboard next-word prediction: a recurrent network trained on phones from what people type)
#   https://research.google/blog/federated-learning-collaborative-machine-learning-without-centralized-training-data/
#       (McMahan & Ramage, 6 April 2017)
#   https://techcrunch.com/2023/05/23/adobe-brings-fireflys-generative-ai-to-photoshop/  (Generative Fill in the Photoshop beta,
#       23 May 2023; Firefly trained on Adobe Stock photos and other commercially safe images)
#   https://news.adobe.com/news/news-details/2023/adobe-unveils-future-of-creative-cloud-with-generative-ai-as-a-creative-co-pilot-in-photoshop
#       (Adobe, 23 May 2023: Firefly "trained on Adobe Stock images, openly licensed content and other public domain content
#       without copyright restrictions")
#   The grid system, the parametric chair and the diffusion model: deck/week01.py, deck/week02.py, deck/week05.py
