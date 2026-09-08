"""
SD2112 · Artificial Intelligence in Design · Week 13 — the slide spec.

    python deck/week13.py            # builds _site/week13/ (html deck + pdf), export/week13*.pptx, export/preview/
    python deck/week13.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

The last class: the poster fair (40 %, four rounds of twelve minutes, half the teams present while
the other half visits, peer feedback and a peer prize on ClassPoint, the graders' sheets), the break,
the course recapped in five slides and the course question answered by the room one last time, the
final quiz (20 %, ClassPoint quiz mode with Blackboard as the fallback; the questions live in the
quiz deck on the classroom PC, never in this repository), and goodbye. Two live sketches: the fair
clock (rounds, halves, a drawn bell; hover it for the keys, 0 resets it; its team count defaults to TEAMS in
tools/figures_week13.py, which the room and rotation figures read too) and the thirteen weeks on the
rules ↔ examples line; the fair clock, set to thirty-five minutes, also sits on the quiz placeholder slide.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week13 as F                            # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full, timeline,   # noqa: E402
                     journey, activity, assessment, team_band, two_col, figure_slide, sketch_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, P5, JOURNEY, footer  # noqa: E402

FOOTER = footer(13)
TEAMS, HALF = F.TEAMS, F.HALF     # the working team count (set in tools/figures_week13.py from the group list; the clock's [ and ] on the day)

# ───────────────────────── live sketches (html deck) ─────────────────────────
ROUNDS_JS = """// The fair clock. Four rounds: half the teams present while the other half visits, then they swap.
// Click: start, pause; when the bell shows, click again for the next round.
// Keys: + and - change the length of a round, [ and ] the number of teams, 0 resets the clock (0 again at rest:
// back to round 1). Every other key goes to the deck. Hover the clock to give it the keyboard.
const MODE = 'fair';                       // 'fair': rounds and halves · 'quiz': one clock and the rules
const ROUNDS = 4;                          // two passes: everyone presents twice and visits twice
let minutes = 12, teams = 26;              // set on the day
let round = 1, running = false, t0 = 0, spent = 0;   // spent: ms of this round used before the current run
const A = '#ED6D24', B = '#64C2C3', INK = '#000B1C', MUTED = '#5C6470', RED = '#E42519';

function setup() { createCanvas(1400, 500); textFont('JetBrains Mono'); }

function used() { return spent + (running ? millis() - t0 : 0); }

function draw() {
  background(255);
  let total = minutes * 60000, e = min(used(), total), left = total - e, over = e >= total;
  let col = over ? RED : left < 60000 ? A : B;
  // the ring drains; orange in the last minute, red at zero
  noFill(); strokeCap(SQUARE); strokeWeight(26); stroke('#E1E1DE'); circle(230, 250, 340);
  if (!over) { stroke(col); arc(230, 250, 340, 340, -HALF_PI, -HALF_PI + TWO_PI * left / total); }
  noStroke(); fill(over ? RED : INK); textAlign(CENTER, CENTER); textSize(92); text(clock(left), 230, 244);
  textAlign(LEFT, BASELINE); fill(col); textSize(22);
  let status = over ? (round < ROUNDS && MODE == 'fair' ? 'TIME · SWAP · CLICK FOR ROUND ' + (round + 1) : 'TIME · CLICK TO RESET')
             : running ? 'RUNNING · CLICK TO PAUSE' : e > 0 ? 'PAUSED · CLICK TO RESUME' : 'READY · CLICK TO START';
  text(status, 470, 262);
  fill(MUTED); textSize(15);
  text(MODE == 'fair' ? '+ / -: minutes    [ / ]: teams    0: reset    click: start · pause · next round' : '+ / -: minutes    0: reset    click: start · pause', 470, 452);
  if (over) bell(1260, 110, frameCount % 40 < 20);
  if (MODE == 'quiz') return quiz();
  // which half presents, which half visits
  let half = ceil(teams / 2), aFirst = round % 2 == 1;
  let present = aFirst ? '1 – ' + half : (half + 1) + ' – ' + teams;
  let visit = aFirst ? (half + 1) + ' – ' + teams : '1 – ' + half;
  fill(MUTED); textSize(18); text('ROUND ' + round + ' OF ' + ROUNDS + '  ·  ' + minutes + ' MIN  ·  ' + teams + ' TEAMS', 470, 78);
  fill(INK); textSize(50); text('Teams ' + present + ' present.', 470, 148);
  fill(MUTED); textSize(26); text('Teams ' + visit + ' visit: one line per poster.', 470, 200);
  // the four rounds as a bar
  for (let r = 1; r <= ROUNDS; r++) {
    let x = 470 + (r - 1) * 222, done = r < round, now = r == round;
    fill(done ? INK : now ? col : '#F4F4F2'); rect(x, 306, 206, 56);
    fill(done || now ? '#FFFFFF' : MUTED); textSize(15);
    text('round ' + r + ' · ' + (r % 2 ? '1–' + half : (half + 1) + '–' + teams), x + 14, 340);
  }
  fill(MUTED); textSize(15); text('two passes: everyone presents twice and visits twice · feedback open on ClassPoint throughout', 470, 410);
}

function quiz() {                          // the same clock on the quiz slide: the rules instead of the halves
  fill(MUTED); textSize(18); text('THE FINAL QUIZ  ·  ' + minutes + ' MIN  ·  20 %', 470, 78);
  fill(INK); textSize(50); text('Thirty questions. One attempt.', 470, 148);
  textSize(20);
  text('one question at a time · answer once · a closed question stays closed', 470, 320);
  text('laptops closed · no talking · no second screen · finished: phone face down', 470, 352);
  text('late: join at the question on screen · Blackboard only when Gio says so', 470, 384);
}

function bell(x, y, swing) {               // drawn, not rung: the TAs call the swap
  push(); translate(x, y); rotate(swing ? -0.12 : 0.12);
  noStroke(); fill(A); arc(0, 0, 120, 140, PI, TWO_PI); rect(-60, 0, 120, 20); rect(-8, -80, 16, 14);
  fill(INK); circle(0, 32, 18);
  pop();
  stroke(A); strokeWeight(4); noFill();
  for (let d of [190, 230]) { arc(x, y, d, d, -0.7, -0.2); arc(x, y, d, d, PI + 0.2, PI + 0.7); }
  noStroke(); fill(RED); textAlign(CENTER, BASELINE); textSize(22); text('TIME', x, y + 96); textAlign(LEFT);
}

function clock(ms) { let s = ceil(ms / 1000); return floor(s / 60) + ':' + nf(s % 60, 2); }

function mousePressed() {
  if (used() >= minutes * 60000) { if (round < ROUNDS && MODE == 'fair') round++; spent = 0; running = false; }
  else if (running) { spent += millis() - t0; running = false; }
  else { t0 = millis(); running = true; }
}

function keyPressed() {
  if (key === '+' || key === '=') minutes = min(60, minutes + 1);
  else if (key === '-' || key === '_') minutes = max(1, minutes - 1);
  else if (key === ']') teams = min(40, teams + 1);
  else if (key === '[') teams = max(2, teams - 1);
  else if (key === '0') { if (used() == 0) round = 1; spent = 0; running = false; }   // reset; at rest: back to round 1
  else return;                             // every other key goes to the deck
  return false;
}"""

ROUNDS_JS = ROUNDS_JS.replace('teams = 26;', f'teams = {TEAMS};')       # one working count, kept in tools/figures_week13.py
QUIZ_CLOCK_JS = ROUNDS_JS.replace("const MODE = 'fair';", "const MODE = 'quiz';").replace('let minutes = 12,', 'let minutes = 35,')
CLOCK_EXTRA = """// the clock takes the keyboard when the mouse is over it, so [ ] + - 0 work without a click (a click would start it)
addEventListener('pointermove', function () { if (!document.hasFocus()) window.focus(); });"""

COURSE_JS = """// Thirteen weeks in one picture. Hover a week: its idea in one line, what you made or handed in,
// and where it sat between the two machines: write the rule (left) or show the examples (right).
// [title, the idea, made or due, position from rules 0 to examples 1, module]
const weeks = [
  ['Two ways to teach a machine', 'write the rule, or show the examples: a chair both ways, a cup pushed to the edge', 'a cup at the edge · accounts set up', 0.50, 1],
  ['Rules that make things', 'machine A: LeWitt, Nees, Nake; a spec a stranger can execute; a model writes machine A', 'challenge 1: a picture from rules', 0.04, 1],
  ['Learning from examples', 'machine B: concepts have a middle and an edge; a perceptron finds its line; Move 37', 'challenge 2: a picture from text and references', 0.98, 1],
  ['Language machines', 'tokens, embeddings, attention, the next word; hallucination; prompting is briefing', 'challenge 3: a brief, automated', 0.94, 2],
  ['Image machines and mediation', 'CLIP, diffusion, the latent, ControlNet and LoRA; Ihde\\'s four relations', 'challenge 4: a layout you could not design', 0.90, 2],
  ['Sound machines', 'spectrograms and MIDI; music and voice generated; who owns a voice', 'challenge 5: thirty seconds of sound', 0.76, 2],
  ['Mid-term', 'the quiz on weeks 1 to 6; sixty-second pitches; teams of four or five', 'the reflection · the mid-term quiz', 0.44, 0],
  ['AI as design material', 'using vs incorporating: a model decides something for each person; the diamond with a model inside', 'the group proposal', 0.60, 3],
  ['Data, bias and privacy', 'the model learns the world it was shown; four kinds of bias; minimisation and consent', 'concept board · bias register', 0.86, 3],
  ['Recommendation systems', 'an item is a point; people like you; the objective; the feed as a designed mediation', 'prototype v1', 0.82, 3],
  ['Curators of outputs and datasets', 'the pick is the authorship; what a dataset teaches; who owns what', 'draft poster · mediation brief', 0.68, 4],
  ['Language as an interface', 'rules-based vs generative chatbots; agents; transparency and opacity; guardrails', 'final poster and video', 0.36, 4],
  ['Poster fair and final quiz', 'the fair, the quiz, and the question one last time', 'the group project', 0.50, 0],
];
const MOD = ['#000B1C', '#64C2C3', '#943890', '#ED6D24', '#E94D7F'];   // module 0 to 4
const X0 = 90, X1 = 1310, Y = 350;                                     // the axis (its captions stay clear of the chip at the bottom)
let tw;

function setup() { createCanvas(1400, 500); textFont('JetBrains Mono'); tw = (X1 - X0 - 12 * 8) / 13; }

function draw() {
  background(255);
  let hov = constrain(floor((mouseX - X0) / (tw + 8)), 0, 12), w = weeks[hov];
  // the tiles: one per week, coloured by module
  for (let i = 0; i < 13; i++) {
    let x = X0 + i * (tw + 8), on = i == hov;
    noStroke(); fill(MOD[weeks[i][4]]); rect(x, 40, tw, on ? 100 : 84);
    fill(255); textAlign(LEFT, BASELINE); textSize(14); text('WEEK', x + 10, 62); textSize(30); text(i + 1, x + 10, 98);
    if (on) { stroke('#000B1C'); strokeWeight(4); noFill(); rect(x - 2, 38, tw + 4, 104); }
  }
  // the hovered week: title, idea, what was made
  noStroke(); fill('#000B1C'); textAlign(LEFT, BASELINE); textSize(34); text(w[0], X0, 200);
  fill('#5C6470'); textSize(17); text(w[1], X0, 232);
  fill(MOD[w[4]]); textSize(15); text(('made or due: ' + w[2]).toUpperCase(), X0, 262);
  // the axis: rules on the left, examples on the right, and where every week sat (ties stack)
  stroke('#E1E1DE'); strokeWeight(6); line(X0, Y, X1, Y);
  for (let i = 0; i < 13; i++) {
    let x = X0 + weeks[i][3] * (X1 - X0), lane = 0;
    for (let j = 0; j < i; j++) if (abs(weeks[j][3] - weeks[i][3]) < 0.03) lane++;
    let y = Y + lane * 30, on = i == hov;
    noStroke(); fill(MOD[weeks[i][4]]); circle(x, y, on ? 36 : 26);
    fill(255); textAlign(CENTER, CENTER); textSize(on ? 16 : 14); text(i + 1, x, y);
  }
  textAlign(LEFT, BASELINE); fill('#ED6D24'); textSize(17); text('RULES · MACHINE A', X0, Y + 58);
  fill('#5C6470'); textSize(14); text('write the rule: exact, explainable, brittle', X0, Y + 82);
  textAlign(RIGHT); fill('#64C2C3'); textSize(17); text('EXAMPLES · MACHINE B', X1, Y + 58);
  fill('#5C6470'); textSize(14); text('show the examples: fluent, opaque, typical', X1, Y + 82);
  textAlign(CENTER); text('where each week sat on the line, roughly · hover a week', (X0 + X1) / 2, Y - 34);
}"""

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 13 · POSTER FAIR · FINAL QUIZ',
               'Poster fair and final quiz.',
               'Week 13 — the fair, the quiz, and goodbye.',
               notes='Join code on screen from 30 minutes before, and it matters more than ever: the peer feedback and the quiz both run on ClassPoint. The posters have been going up since the TAs opened the room; the videos loop on the teams\' laptops. Three parts today: the fair, then the break, then the course in five slides and the final quiz, then goodbye. Phones charged.'))

S.append(agenda('SD2112 · WEEK 13', [
    'Welcome: the room and the rules', 'The fair: how it runs', 'Rounds 1 to 4: present, visit, swap', 'Peer feedback and the prize',
    'Break', 'The course in five slides', 'The final quiz: 20%', 'Goodbye',
], notes='Eight stops. Before the break, the fair: how it runs, four rounds of twelve minutes with the clock on the screen, one line of feedback per poster you visit, then the prize. After the break, the whole course in five slides and the course question one last time, the final quiz — twenty percent, thirty questions — and goodbye. Nothing new is taught today; everything on the walls and in the quiz is yours already.'))

# ───────────────────────── 01 · the last class ─────────────────────────
S.append(section('01', 'The last class.', 'the fair · the quiz · goodbye', bg=INK,
                 notes='Chapter one, eight minutes: one word from everyone, the three parts of today, the room, and a check that every board is ready.'))

S.append(question('word_cloud', 'Thirteen weeks in one word.',
                  hint='The one word you would use for this course now. Week 1 asked why AI is relevant for design; this is the other end of the semester.',
                  eyebrow_text='01 · WARM-UP · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each, ninety seconds. Put the real week-1 cloud next to it — Amber has the screenshot; week 1 asked why AI is relevant for design, so expect words like tools, speed, jobs, cheating there. Read the three biggest words now and say what changed. Keep the screenshot: it goes in the last slide of the course next year. Then the three parts.'))

S.append(cards('01 · THREE PARTS', 'Three parts. Then it is done.', [
    ('THE FAIR · 40 %', 'Your project, on the wall.',
     ['Four rounds of twelve minutes. Half the teams present while the other half visits; then they swap, twice. One line of feedback per poster you visit, on ClassPoint. Two of us grade every board, a sheet each.',
      'Ends with the peer prize: the poster you would give it to, its number in a cloud, and a vote.']),
    ('THE QUIZ · 20 %', 'Thirty questions on thirteen weeks.',
     ['After the break: the course in five slides, the course question one last time, then the quiz on ClassPoint — multiple choice, one attempt, thirty-five minutes. Blackboard is the fallback, only when I say so.',
      'The questions are not on the site. The ideas are.']),
    ('GOODBYE', 'What to take, where it stays, thanks.',
     ['Four sentences to keep. Where the slides, the sketches, the syllabus and the playlist stay. How this course was made. Thanks to the team.',
      'Marks and a paragraph per team on Blackboard after the grading meeting.']),
], text_size=22, notes='Three parts, said once, so nobody asks at 2:30 when the quiz is. The fair is nearly everything before the break and forty percent of the mark; the quiz is twenty. Say the rule of the day: you present twice and you visit twice, and every visit ends in one line on ClassPoint. Then the room.'))

S.append(figure_slide('01 · THE ROOM', 'Boards on the walls. Two halves. One clock.', F.w13_room(),
                      body=[f'Boards on three walls, one per team, numbered as on the Blackboard group list: half A is the first half of the list, teams 1 to {HALF}; half B the second, {HALF + 1} to {TEAMS}. A laptop with the video at every board, the clock on the screen, the desk by the door.'],
                      caption='Posters were due up thirty minutes before class, video looping, a QR code to the video on the poster. One presenter at the board at all times; the rest of the team visits.',
                      notes=f'Walk the plan with a finger. The teal boards are half A, the first half of the group list, presenting in rounds 1 and 3; the orange ones are half B, rounds 2 and 4. The screen shows the clock and, behind it, the feedback wall growing. The desk is where the graders\' sheets live and where a dead phone gets a charger. The plan assumes {TEAMS} teams; the real count is on the boards and in the clock. Ask each team to look at its number now and to decide who stands at the board in round 1 — and who in round 3, because it should be a different person.'))

S.append(question('multiple_choice', 'Is your poster up and your video playing?', [
    'Up, and the video plays on our laptop', 'Up, but the video is not playing yet', 'Not up yet — we need a hand', 'A team member is missing',
], eyebrow_text='01 · LOGISTICS · MULTIPLE CHOICE',
    notes='One answer per person, but it is the team that matters. Bs and Cs get a TA now: Nicolò for the video, WU Zhao and MA Jie for tape and boards. Ds come to Amber at the break, not now — a missing member is a process-log question, not a fair question. Show the split; if more than two boards are not up, give the fair five more minutes and take them from the buffer, not from the rounds.'))

# ───────────────────────── 02 · the poster fair ─────────────────────────
S.append(section('02', 'The poster fair', '40 % · four rounds of twelve minutes · present, visit, swap', bg=YELLOWS[0],
                 notes='Chapter two: how the fair runs, what visitors ask, how the forty percent is decided, and then the four rounds with the clock on the screen. Nicolò runs the clock from the html deck; Amber, WU Zhao and MA Jie grade with me.'))

S.append(figure_slide('02 · FOUR ROUNDS', 'Half present. Half visit. Then swap.', F.w13_rotation(),
                      body=[f'Twelve minutes a round: a visitor sees four posters, three minutes each, and writes one line per poster — eight of the other half\'s {HALF} over the two visiting rounds. The second pass is not a repeat: you go to the posters you missed, a different person talks at the board, and a different grader comes to every board.'],
                      caption='Between rounds, two minutes. The clock on the screen says which half presents and shows a bell at zero; the TAs call the swap. The short answer stays open through all four rounds.',
                      notes='Read the rows top to bottom. Half A presents in rounds 1 and 3, half B in 2 and 4, so everyone presents twice and visits twice. The graders\' row: five of us, three boards each a round, about four minutes a board, a band and a line per criterion; the second pass sends a different one of us to every board, so every team ends the fair with two sheets from two people. The ClassPoint row: one activity, open the whole time, one line per poster visited. Say the visitor\'s pace out loud — three minutes a poster, then move, four posters a round — and that the presenter\'s job is to answer the five questions on the next slide, not to give a speech.'))

S.append(cards('02 · WHAT VISITORS ASK', 'Five questions at every poster.', [
    ('THE DECISION', 'What does the model decide, from what?', 'Point at it on the poster: the data in, the score, the line, the decision, the fallback. If you cannot find the line, say so in your feedback.'),
    ('THE DATA', 'What must it know, and where from?', 'Given, taken or inferred. Asked for, or assumed. What it keeps, and for how long. Week 9\'s minimisation question, asked of a stranger\'s product.'),
    ('THE BIAS', 'Where is it wrong, and for whom?', 'The bias register\'s worst row. Who is missing from the examples; who pays when the model is wrong. A good poster names a person, not a category.'),
    ('THE GUARDRAIL', 'What may it never decide?', 'When a human steps in; how it fails in front of a person; what the person can see, refuse and correct. Machine A around machine B.'),
    ('THE RELATION', 'Through it, off it, facing it, around you?', 'Which of Ihde\'s four the product builds, and how hard it pushes: hidden or apparent, weak or strong. The brief\'s first question, asked back.'),
], text_size=20, notes='The five questions are the mediation brief plus the decision, which is the poster\'s third zone. Visitors ask them; presenters answer them; graders listen for them. The strength you write in your feedback should be one of these five done well, and the question should be one of them left open. Tell the presenters: if a visitor asks the guardrail question and the answer is "we would add that later", that is the note the graders write too.'))

S.append(figure_slide('02 · THE FORTY PERCENT', 'How the forty percent is decided.', F.w13_grading(),
                      body=['Four things are read: the poster at the fair, the video on the laptop, the brief and the log on Blackboard. Five criteria from the syllabus. Two of us at every board today, a sheet each; a grading meeting after; the mark and a paragraph per team on Blackboard.'],
                      caption='Peer feedback and the prize are read at the meeting and forwarded to every team; the rubric decides the mark. The A, B and C bands are in the syllabus on the site.',
                      notes='The instructor feedback, explained once. Today each of us grades three boards a round, about four minutes each: a band and a line per criterion, a note in the margin. The second pass sends a different one of us to every board, so every team gets two independent sheets — the arithmetic of forty-eight minutes does not allow five, and two unhurried sheets beat five rushed ones. The meeting puts the two sheets side by side, reads the video and the brief again, and reads the peer wall. What comes back on Blackboard is the mark and a short paragraph: two strengths, one thing to fix. Sixty percent of the mark is research and ethics — the two zones most drafts left thin in week 11 — so a beautiful poster for a shallow idea still sits at C. Say when the marks come: after the meeting, within the programme\'s timeline, and I will announce the date on Blackboard.'))

S.append(question('short_answer', 'Visitors: team number · one strength · one question.',
                  hint='One line per poster you visit, as many posters as you visit. Team numbers only — never a person\'s name. Open now; it stays open through all four rounds.',
                  example='12 · the decision is drawn, with the fallback · what happens when the data is missing?',
                  eyebrow_text='02 · PEER FEEDBACK · SHORT ANSWER · MULTIPLE SUBMISSIONS · NAMES HIDDEN',
                  cp={'type': 'short_answer', 'hide_names': True, 'multiple': True},
                  notes='Open the activity now and leave it open on the classroom PC until the prize; multiple submissions are on and names are hidden, so the wall is a list of lines that start with a team number. Read the example aloud: a number, a strength that is one of the five questions done well, a question that is one of the five left open. Nobody writes a person\'s name; a line with a name in it is deleted before the export. The export goes to the grading meeting and every team gets its own lines afterwards. Then Nicolò puts the clock on the screen.'))

S.append(sketch_slide('02 · LIVE · THE FAIR CLOCK', 'Round 1. Half A presents, half B visits.',
                      live('w13-rounds', ROUNDS_JS, 1400, 500, hint='click = start · pause · next round  ·  + and − the length  ·  [ and ] the teams  ·  0 = reset', extra=CLOCK_EXTRA),
                      body=['Twelve minutes a round, four rounds. The clock says which teams present and which visit; at zero the ring turns red and a bell appears — it is drawn, not rung: the TAs call the swap. Two minutes to swap, then the next round.'],
                      caption='Nicolò runs it from the html deck on the second screen; the PowerPoint keeps the feedback activity open. Hover the clock to give it the keyboard: [ and ] set the number of teams, + and − the length of a round, 0 resets the clock (0 again at rest: back to round 1).',
                      notes='Before the first presenters are at their boards: Nicolò hovers the clock, sets the team count with ] and [ so the halves match the group list, and presses 0 if a click has started it. Then the click. Round 1: half A at the boards, half B walking with phones. At the bell: two minutes, everyone swaps, click, round 2. Rounds 3 and 4 are the second pass — say it again when round 3 starts: go to the posters you missed, and a different person talks. If the room is behind, press minus twice for rounds 3 and 4 (ten minutes); if it is ahead, do not add time — start the prize early. The graders keep moving; if a board has no visitor for a minute, a TA sends one.'))

S.append(question('image_upload', 'Everyone: the poster you would give the prize to.',
                  hint='One image: the poster, photographed during the last round. Caption: the team number, nothing else. Not your own team.',
                  eyebrow_text='02 · THE PEER PRIZE · IMAGE UPLOAD · CAPTION REQUIRED · NAMES HIDDEN',
                  cp={'type': 'image_upload', 'hide_names': True, 'caption_required': True},
                  notes='Three minutes, everyone, one image each, caption required and the caption is a team number. Names hidden, so the wall is posters and numbers. Nobody counts the captions: the next slide does the tally. Download the responses after class: the photographs are the only pictures of the fair we keep, and none of them shows a face if the teams photographed the board.'))

S.append(question('word_cloud', 'The prize: type that team number.',
                  hint='The number from your caption, once. The four biggest numbers on the screen are the finalists — the cloud counts, nobody does.',
                  eyebrow_text='02 · THE PEER PRIZE · WORD CLOUD · ONE NUMBER EACH',
                  notes='One minute, one number each, the same number as the caption. A word cloud sizes a word by how often it was typed, so the four biggest numbers on the screen are the four most-nominated teams and nobody has to count photographs. Amber writes the four numbers on the whiteboard as A, B, C and D, in the order they stand on the wall; if the fourth place is a tie, I break it with a coin, out loud — the cloud is the shortlist, the vote is the prize. Nothing on the classroom PC is edited during the session. Then the vote.'))

S.append(question('multiple_choice', 'The peer prize: which of the four?', [
    'Finalist A · the first number on the whiteboard', 'Finalist B · the second number', 'Finalist C · the third number', 'Finalist D · the fourth number',
], eyebrow_text='02 · THE PEER PRIZE · MULTIPLE CHOICE · ONE VOTE EACH',
    notes='Amber reads the four team numbers from the whiteboard and points at the boards; the room votes once, not for its own team. No correct answer: the room decides, the winning team gets a participation star each, the same as a challenge award, and thirty seconds at the goodbye to say what their model decides. Show the split and thank all four; then the break. The prize is peer recognition, not a grade — say so, because the rubric decides the forty percent.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · THE COURSE IN FIVE SLIDES · THE FINAL QUIZ · GOODBYE', size=120, bg=PAPER,
                   notes='1:21. Posters stay up until the end of class; laptops off the boards and closed, because the quiz needs a room with no second screen. Phones charged at the desk if needed. Amber takes anyone with a missing team member now. The TAs collect the sheets from the graders and put them in the folder.'))

# ───────────────────────── 03 · the course in five slides ─────────────────────────
S.append(section('03', 'The course in five slides', 'two machines · use vs incorporate · mediation · bias · the turn', bg=INK,
                 notes='Chapter three, twenty minutes: the whole course in five slides, then the course question one last time. Nothing new; this is the revision the quiz draws on.'))

S.append(sketch_slide('03 · LIVE · THIRTEEN WEEKS IN ONE PICTURE', 'Two ways to teach a machine.',
                      live('w13-course', COURSE_JS, 1400, 500, hint='hover a week: its idea, what you made, where it sat between the two machines'),
                      body=['Write the rule, or show the examples. Every week sat somewhere on that line: week 2 at the rules end, week 3 at the examples end, the product weeks in between, and the last two back towards rules — guardrails are machine A around machine B.'],
                      caption='The positions are rough and mine; argue with them. Hover a tile: the idea in one line, and the challenge or the deliverable of the week.',
                      notes='Recap one: the spine. Walk the tiles left to right in three minutes, one sentence each — the sentence under the tile. Then the line: ask the room where week 12 sat and why it moved back towards rules; the answer is guardrails, and the rules-based chatbot. Ask where their own product sits; most are a mix, which is the point. Give the two biggest words from the warm-up cloud one minute each here, with the deck of that week open on the second screen. No new material after this slide.'))

S.append(cards('03 · RECAP 2 · USING AND INCORPORATING', 'Using AI, or incorporating AI.', [
    ('WEEKS 1 – 6 · THE PROCESS', 'Using AI',
     ['AI as a tool in **how** you design: a brief drafted with a language model, a picture from text and references, a layout you could not design, thirty seconds of sound. The model produced; you decided.',
      'You stayed the author: curator, briefer, editor. The reflection was this, argued.']),
    ('WEEKS 8 – 12 · THE PRODUCT', 'Incorporating AI',
     ['AI as a material in **what** you design: a model decides something for each person, on its own — show, rank, suggest, refuse — from what it knows about them.',
      'You designed the deciding: what it may decide, from what data, how sure it must be, what happens when it is wrong. The poster on the wall is this.']),
], notes='Recap two: the distinction that organised the semester, week 1\'s cards with the verbs from week 8. Using: the model produces and you decide. Incorporating: the model decides and you design the deciding. Ask for one example of each from the fair — a poster made with Generative Fill is using; the product on it is incorporating. The quiz asks this in four or five different ways.'))

S.append(figure_slide('03 · RECAP 3 · MEDIATION', 'The thing in between is never neutral.', F.w13_mediation(),
                      body=['Ihde\'s four relations, Verbeek\'s reading of them for designers, and the AI product that builds each. The same model can be a fill, a feed, an assistant or a default; the relation is in the product, and you chose it. That was the first question of the mediation brief.'],
                      caption='Ihde 1990; Verbeek 2015, the core reading. Verbeek adds cyborg, immersion and augmentation for the technologies that do not fit the four; the feed that learns from you is immersion.',
                      notes='Recap three: mediation. Say the schema once — you, the technology, the world; you perceive through it and act on it — then the four columns with the AI version and the risk, which the quiz asks about: forgetting it decides, mistaking the picture for the world, mistaking it for a person, nobody accountable. Verbeek\'s point for designers, in my words: a technology creates relations between people and their world, and designing one is designing those relations. Every poster on the wall named one; ask two teams which.'))

S.append(cards('03 · RECAP 4 · BIAS AND DATA', 'The model learns the world it was shown.', [
    ('DATA', 'Who is missing from the examples.',
     'The model learns the middle of what it saw: the cup wall in week 1, the datasets in week 3, Coded Bias in week 9. Choose the examples and you choose the prototype.'),
    ('LABEL', 'Who named the examples.',
     'A label is a decision a person made once, then applied at scale: "chair", "spam", "risky". The bias register\'s first column asks who wrote it.'),
    ('ALGORITHM · INTERACTION', 'The objective, and the loop.',
     'A model wants the number it was given — clicks, watch time — not fairness (week 10). What people do with the output feeds the next version: the loop from week 8, with drift.'),
    ('PRIVACY', 'Collect only what the decision needs.',
     'Minimisation, a stated purpose, a retention limit, consent (week 9). Removing the name column is not anonymising; any rare column that is public elsewhere is a name.'),
], text_size=22, notes='Recap four: the four kinds of bias from week 9, with the objective from week 10 and the loop from week 8, and the privacy principles. The one sentence to remember for the quiz: the model learns the world it was shown, and whoever labelled it. Ask the room for the bias register\'s worst row from one poster; it should name a person and a cost.'))

S.append(cards('03 · RECAP 5 · THE DESIGNER\'S TURN', 'Designers as…', [
    ('OUTPUTS', 'Curators of what ships',
     'A model makes a hundred; you choose one and answer for it. Sixty-four tiles, three picks, a reason each (week 11). Not everything generated should be released.'),
    ('DATASETS', 'Curators of what it learns',
     'Twelve images of a style you own, and a sentence saying what they agree on (week 11). Choose the examples and you choose the prototype — and whose consent you needed.'),
    ('RULES', 'Setters of guardrails',
     'What the machine may never decide, when a human is in the loop, how it fails in front of a person (week 12). Machine A protecting people from machine B.'),
    ('STORY', 'Tellers of the process',
     'The process note: which tools, for what, what you changed. On the reflection, on the poster strip, in every brief you will write. The author is in that sentence.'),
], text_size=22, notes='Recap five: week 1\'s four roles, now with the week that practised each. This is the answer to the fear the room brought in week 1 — "will AI replace designers" — and the answer is: which of the four do you want to be good at? Then the question, one last time.'))

S.append(question('short_answer', 'Can a machine originate a design? Yes or no — and why.',
                  hint='One line. Week 1 asked it with Lovelace; week 12 asked it again. This is the last time. Names are hidden; the answer is not graded.',
                  eyebrow_text='03 · THE COURSE QUESTION · SHORT ANSWER · NAMES HIDDEN',
                  cp={'type': 'short_answer', 'hide_names': True, 'multiple': False},
                  notes='Three minutes, anonymous. Read six lines, two from each side, and count the room roughly by hand: yes, no, it depends. Week 12 promised that its answers would come back today next to the week-1 definitions of AI, so put both screenshots beside this wall — Amber has them: in week 1 nobody had the vocabulary; now the "why" clause has the words in it — the middle, the pick, the guardrail. Do not give your own answer yet; the next slide has the arguments, and my answer is the last sentence of the notes there.'))

S.append(figure_slide('03 · THE ARGUMENTS', 'The same question, three times.', F.w13_question_map(),
                      body=['No: Lovelace, the rule, the middle, the data. Yes: Turing, Move 37, Wiggins, the spec that came back better than you meant. Who chose: LeWitt, Belamy, the curator, the process note. Marked on the defence, not the side.'],
                      caption='Lovelace 1843, as Turing quoted her in 1950; Turing 1950; AlphaGo v. Lee Sedol, game 2, 10 March 2016; Wiggins 2006; LeWitt 1967; Christie\'s, 25 October 2018.',
                      notes='Read one item from each column against what the room just wrote. The no column is the machine as we opened it: the rule is all there is, the model gives the middle. The yes column is the surprise: Turing\'s sentence, the move most professionals would not have considered, and the code that did what you said and was better than what you meant. The third column is the designer\'s turn: the machine makes, a person picks, and the pick is where the author is. Your own answer goes here, in one sentence and in your own words — the course leans towards the third column, but the room should hear yours. Then the quiz.'))

# ───────────────────────── 04 · the final quiz ─────────────────────────
S.append(section('04', 'The final quiz', '20 % · the whole course · multiple choice · one attempt', bg=INK,
                 notes='Chapter four, three quarters of an hour with the quiz: how it runs, the rules of the room, then the quiz itself on ClassPoint, with Blackboard as the fallback. Same lanes as the mid-term in week 7.'))

S.append(figure_slide('04 · HOW IT WORKS', 'Thirty questions. Thirty-five minutes. One attempt.', F.w13_quiz_flow(),
                      body=['One idea, four choices, one right answer, weeks 1 to 12 and the playlist, in course order: the shape of the mid-term, revisiting week 7\'s least-sure list. One question at a time on ClassPoint; a closed question stays closed.'],
                      caption='Laptops closed, no talking, no second screen, no notes, no chatbot. Late: join at the question on screen. Finished: phone face down. Twenty percent; the marks on Blackboard with the summary.',
                      notes='Two lanes, one quiz, exactly as in week 7 — say that, because the room has done this before. The plan is ClassPoint quiz mode: Nicolò opens the quiz deck with the add-in; each question is a multiple-choice activity in quiz mode with one right answer, auto-marked; about a minute a question, you answer once, then it closes and the next opens. The fallback is a Blackboard test with the same thirty questions in random order, one attempt, submitting itself at thirty-five minutes. Nobody switches lanes alone. Read the caption aloud, all of it, and add: anyone with a second screen open is noted by a TA and dealt with under the integrity policy after class, not in front of the room.'))

S.append(sketch_slide('04 · THE QUIZ · 35 MINUTES', 'Quiz: open the ClassPoint quiz mode.',
                      live('w13-quiz-clock', QUIZ_CLOCK_JS, 1400, 500, hint='click = start · pause  ·  + and − change the length  ·  0 = reset', extra=CLOCK_EXTRA),
                      body=['The questions are in the quiz deck, not in this one. Nicolò opens it with the ClassPoint add-in; this clock stays on the second screen — hover it for the keys, 0 resets it. Blackboard fallback: the test opens at my word and closes itself thirty-five minutes later.'],
                      caption='A placeholder. The thirty questions are never in the published deck; they live in the quiz deck on the classroom PC and in the Blackboard test, and change every year.',
                      notes='Placeholder: the room sees this for a moment while Nicolò switches to the quiz deck. Start the clock with a click when question one opens; it turns orange in the last minute and red at zero, with the bell. In the quiz deck: thirty multiple-choice slides in quiz mode, one right answer each, about a minute per question — Nicolò closes each when the room has answered and opens the next. After the last question: phones face down, and back to this deck for goodbye. If we switch to Blackboard part-way, Nicolò presses 0 and clicks: the clock restarts at 35:00 and is the only thing on screen. If we are on Blackboard from the start, it is the only thing on screen for thirty-five minutes. Nicolò exports the quiz summary before leaving the room.'))

# ───────────────────────── 05 · goodbye ─────────────────────────
S.append(section('05', 'Goodbye', 'what to take · where it stays · thank you', bg=PAPER,
                 notes='Chapter five, ten minutes: four sentences to keep, where everything stays, how the course was made, thanks, one line for next year, and the end.'))

S.append(cards('05 · WHAT TO TAKE AWAY', 'Four sentences to keep.', [
    ('ONE', 'Write the rule, or show the examples.',
     'Every AI feature you will meet is one of these, or a mix: exact, explainable and brittle, or fluent, typical and unable to say why. Ask which before you trust it.'),
    ('TWO', 'The machine makes. You decide what ships.',
     'Prompts are rules and models are examples, and neither decides what is still a cup. The pick is the authorship, and you answer for it.'),
    ('THREE', 'The thing in between is never neutral.',
     'A fill, a feed, an assistant, a default: each builds a relation and changes what a person sees and does. Name the relation; write the guardrail.'),
    ('FOUR', 'Say how it was made.',
     'Which tools, for what, what you changed, whose data. The process note is the habit this course leaves you with; clients and juries will ask.'),
], text_size=22, notes='Four sentences, one per module, and the room has heard every one of them before. Say them slowly and do not explain them; the cards do. If the peer-prize team is in the room, this is their thirty seconds: what does your model decide, and what did you decide it may never do.'))

S.append(content('05 · WHERE IT STAYS · AND HOW IT WAS MADE', 'The materials stay. So does the method.',
                 [f'[{SITE}]({"https://" + SITE}): every deck as an html deck with the sketches running, and as a PDF. The **Sketchbook** page: every live sketch on its own page — the perceptron, the cups, the tokens, the feed, ELIZA, the fair clock. The syllabus. The playlist: [{PLAYLIST.replace("https://", "")}]({PLAYLIST}).',
                  '- Blackboard: your submissions, the marks, and a paragraph per team after the grading meeting. Your peer-feedback lines come back to you there too.',
                  '- The course practised what it taught. Every deck is one spec, built into three outputs — a rule, executed by a script. The drawn figures are rules; the week-1 chairs were examples. Every deck ends with the sources it used, and the repository that builds the site is public.',
                  '- The rule you were graded on applies to us: which tools were used to make this course, for what, and what was changed. The process note, said out loud, here — and which decisions were mine.'],
                 body_size=28,
                 notes='Where it stays: the site, which does not go away when Blackboard closes; the Sketchbook, which is the part of the course people come back to; the playlist. Then the process, in the terms we asked of them: one spec, three outputs, a rule executed by a script; the sources at the end of every deck; the repository public. Say your own process note here, out loud, in the same form as theirs — which tools, for what, what you changed, which decisions were yours. That is the last lesson and it should not be a slide; it should be you.'))

S.append(team_band('05 · THANK YOU', 'Thank you.', [
    ('Zhibin Zhou', 'Class coordinator', ['Timetables, rooms, the class as a class: everything that let the fair happen in this room today.', 'zhibin.zhou@polyu.edu.hk · office V502b'], VIOLET, 'ZZ', True),
], 'The teaching assistants · in the room 30 minutes before and after every class, all semester', [
    ('Nicolò Azzolin', 'Tools, accounts, code, the challenges, the playlist, and every clock in this deck.', TEAL, 'NA', False),
    ('Amber', 'Assignments, the group project, every draft poster and brief, Blackboard today.', ORANGE, 'A', False),
    ('WU Zhao', 'The door, the room, the numbered boards, the proctoring, anything about the class.', PINK, 'WZ', False),
    ('MA Jie', 'The door, the room, the numbered boards, the proctoring, anything about the class.', YELLOW, 'MJ', False),
], notes='Names first, applause second. Four teaching assistants who were in this room half an hour before and after every class for thirteen weeks; the coordinator who made the room and the timetable work. Then the room: thank them for the fair, which was the best thing on the walls of this building this semester, whatever the sheets say. Then one last line.'))

S.append(question('short_answer', 'One line for next year\'s students.',
                  hint='What you wish you had known in week 1. One line; names are hidden. It goes into the syllabus for 2027, in your words.',
                  eyebrow_text='05 · ONE LAST LINE · SHORT ANSWER · NAMES HIDDEN',
                  cp={'type': 'short_answer', 'hide_names': True, 'multiple': False},
                  notes='Two minutes, anonymous, the last ClassPoint activity of the course. Read four aloud. Typical lines: start the challenges early, keep the seed, the spec is the work, ask the guardrail question first. Export it: the best lines go into next year\'s syllabus and the week-1 deck, in their words and without names. Cut this slide if the quiz ran long; the export can be done from Blackboard as an announcement instead.'))

S.append(end('That was SD2112.',
             'Thank you. Marks on Blackboard after the grading meeting; the site stays.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='The end. Posters come down now — take yours home, or leave it with the TAs for the school\'s wall if they ask. Marks and a paragraph per team on Blackboard after the grading meeting; the date on Blackboard. The TAs stay for thirty minutes, as always, and so do I.'))

DECK = dict(title='SD2112 · AI in Design · Week 13', slides=finalize(S, FOOTER), pdf='SD2112-week13.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week13', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 5, 6 and 8 September 2026 by web search and fetch; every date, number and quotation on the slides was checked against these)
# Course facts (weights, deliverables, the rubric and its bands, the poster's four zones, the team, the TAs' hours, the playlist, the platforms):
#   syllabus/SD2112-syllabus-2026.md, tools/course.py, README.md (this repository); deck/week01.py (the four roles, the Lovelace quote slide),
#   deck/week07.py and lessons/week07-lesson-plan.md (the mid-term's two lanes, the quiz clock, the team register), deck/week08.py (the least-sure
#   questions "come back in the final quiz in week 13"), deck/week11.py (the poster's four zones, the critique protocol, the mock session in week 12)
# Lovelace and Turing:
#   https://www.abelard.org/turpap/turpap.php  Turing, A. M. (1950). Computing Machinery and Intelligence. Mind LIX(236), October 1950 —
#       section (6) "Lady Lovelace's Objection": "The Analytical Engine has no pretensions to originate anything. It can do whatever we know how to
#       order it to perform"; "Machines take me by surprise with great frequency."
#   https://www.fourmilab.ch/babbage/sketch.html  Menabrea's Sketch of the Analytical Engine with Lovelace's notes (A.A.L.), 1843 (the translation of
#       the 1842 Bibliothèque Universelle de Genève article; Note G itself is beyond the excerpt fetched, so the quote is given as Turing quoted it)
# Move 37: https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol  (Seoul, 9–15 March 2016; game 2 on 10 March 2016; AlphaGo 4–1; Redmond on move 37:
#       "a move that most professional players would not have considered" — the figure says that, not "no human would play")
# Belamy: https://en.wikipedia.org/wiki/Edmond_de_Belamy  (US$432,500, Christie's New York, 25 October 2018; Obvious; a GAN trained on 15,000 WikiArt
#       portraits; signed with the loss function)
# LeWitt: https://monoskop.org/images/3/3d/LeWitt_Sol_1967_1999_Paragraphs_on_Conceptual_Art.pdf
#       Paragraphs on Conceptual Art, Artforum, June 1967 ("The idea becomes a machine that makes the art"; given as a paraphrase on the figure)
# Wiggins: https://research.gold.ac.uk/1000/  Wiggins, G. A. (2006). A preliminary framework for description, analysis and comparison of creative systems.
#       Knowledge-Based Systems 19(7), 449–458 (full text not fetched: the definition is paraphrased, not quoted)
# Ihde and Verbeek:
#   Ihde, D. (1990). Technology and the Lifeworld: From Garden to Earth. Indiana University Press, Bloomington — the four relations: embodiment,
#       hermeneutic, alterity, background (catalogue record: https://archive.org/details/technologylifewo00ihde); the example line on the mediation
#       figure is labelled EXAMPLES, not IHDE, because it mixes Ihde's classic cases (glasses, the thermometer) with Verbeek's 2015 ones (the ATM
#       and the robot, the fridge hum and the heating), as deck/week05.py gives them
#   https://link.springer.com/article/10.1007/s13347-014-0149-8  Nørskov, M. (2015). Revisiting Ihde's Fourfold "Technological Relationships":
#       Application and Modification. Philosophy & Technology 28, 189–207 (a secondary source on the four relations; the page needs a browser)
#   https://research.utwente.nl/en/publications/cover-story-beyond-interaction-a-short-introduction-to-mediation-/  Verbeek, P.-P. (2015). Beyond
#       interaction: a short introduction to mediation theory. Interactions 22(3), 26–31 (the PDF was too large to fetch, so Verbeek is paraphrased,
#       never quoted, on these slides; cyborg, immersion, augmentation as in deck/week05.py, which quotes the paper)
# The poster: https://en.wikipedia.org/wiki/International_standard_paper_sizes  (ISO 216: A0 is 841 × 1189 mm)
# ClassPoint:
#   https://www.classpoint.io/features/word-cloud  (the prize's shortlist: "the number of submissions allowed for the word cloud" is a setting; the page
#       shows the cloud as a picture of "favored opinions" and "outliers" without spelling out that the biggest word is the most-typed one, which is
#       what a word cloud is — so the plan has Nicolò test it with numbers before class and keeps a counted fallback)
#   https://www.classpoint.io/features/short-answer  ("Allow multiple submissions"; "Hide participant names"; stars for the best responses)
#   https://www.classpoint.io/features/image-upload  (names hidden; "download the responses as images"; the caption-required flag is the add-in's
#       own model, read back in tools/classpoint/build.py)
#   https://www.classpoint.io/features/multiple-choice  ("Up to 8 choices"; the correct answer for quiz questions)
#   https://www.classpoint.io/features/quiz-mode  (auto-marking; the quiz summary; "export a report in Excel format"; difficulty levels and stars)
