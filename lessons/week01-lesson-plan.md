# SD2112 · Week 1 lesson plan

**Two ways to teach a machine** · lecture-workshop, about 100 minutes · deck: `export/week01-classpoint.pptx` (59 slides) · web: `docs/week01/`

## Purpose of this session

For us:

1. Give a preview of the whole journey, so every later week lands in a place students already know.
2. Collect the level and the expectations of the room (studio, AI use, coding, hopes and worries) and keep the data.
3. Land one concept that carries the semester: **rules vs examples**, on a chair.
4. Establish the team, the rules and the tools.

For students, by the end of the class they can:

- state the working definition of AI and say what "intelligent-like" and "computation" are doing in it;
- explain the two ways to teach a machine and give one design example of each (Auto Levels vs Generative Fill);
- say why a definition of "chair" leaks and why a model returns the prototype;
- tell using AI (process) from incorporating AI (product);
- know what is due, when, and who to ask.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Open ClassPoint on the classroom PC; open `week01-classpoint.pptx`; put the join code on screen from slide 1. Import `classpoint/roster-2026-classpoint.csv` as the saved class (names are the last four digits + letter of the student ID). Fire the slide-3 word cloud once as a test and reset it. |
| Amber | Paper and pens for 114 people (one sheet each for the chair drawing and the activity). Seating that allows pairs and fours. Blackboard: post the deck link, the playlist and the homework. |
| Gio | Fonts on the classroom PC: install `tools/fonts/Inter-Variable.ttf` and `JetBrainsMono-Variable.ttf`, restart PowerPoint, check slide 1 shows Inter Black without a substitution warning. Fallback: Arial. Backup: the HTML deck on a laptop (`docs/week01/index.html`, press `S` for speaker notes). |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops, where the interactive moments are. | | Join code stays visible until stop 2. |
| 0:03 | 3 | Word cloud: *AI in design, one word* | One minute on screen; read the three biggest words aloud and keep them. | Word cloud (1 submission) | Screenshot the cloud. |
| 0:05 | 4–5 | Why are we here | Tools, products, job: the three things that changed. | | |
| 0:09 | 6–8 | Who is teaching you · the team | Gio's background; the three AI avatars (one photo, three models). Team card: TAs 30 min before and after; Zhibin for absences. | | Say the absence rule out loud. |
| 0:14 | 9–11 | Who are you | Three multiple-choice questions: studio, AI use, code. | 3 × multiple choice | This is the level check. Note the splits; they steer weeks 2, 4 and 5. |
| 0:20 | 12–15 | The journey | The semester map (you are here); Lovelace's objection; the course question. | | |
| 0:26 | 16–18 | What is AI | Short answer in their own words (90 s); read four that disagree; the working definition. | Short answer | |
| 0:31 | 19–20 | Intelligent or creative · Babbage | Wiggins' definition judges output; Turing 1936/1950; the engine as brass and steel. | | |
| 0:34 | 21–24 | Two machines | Write the rule or show the examples; twelve parametric chairs (machine A); four generated chairs (machine B). | | Slides 23 and 24 are the core of the class. |
| 0:40 | 25 | **Draw a chair** | 15 seconds, pen and paper, hold it up, look around: nearly everyone drew the prototype. | | Slide has a 15 s timer label. |
| 0:42 | 26–28 | Typicality · the edge · quick check | Rosch's middle and edge; "ask for the edge, get the middle"; *which of these is a chair?* | Multiple choice | The split is the point; there is no correct answer. |
| 0:47 | 29 | Same app, two machines | Auto Levels · Content-Aware Fill · Generative Fill. Ask which one they would trust for a client shot. | | |
| 0:50 | 30–34 | How we got here | Timeline; Nake 1965; how a network learns; Move 37 (play the chapter if time); Belamy. | | Cut 31–32 if behind. |
| 0:56 | | Break, 5 min | | | Optional. |
| 1:01 | 35–37 | AI in design, now | Using vs incorporating; three cases: Coca-Cola, Netflix, Humane. Ask for one more case from the last month. | | |
| 1:06 | 38 | Short answer: *where did AI touch your design work this week?* | Two minutes; sort a few live into using and incorporating. | Short answer | Replaces the old scavenger hunt. Keep the list for week 3. |
| 1:09 | 39 | The playlist | Fifteen videos; what to watch before week 3. | | |
| 1:11 | 40–43 | The designer's turn | Verbeek's line; the thing in between; designers as curators, guardrail setters, storytellers. | | Keep it to five minutes. |
| 1:16 | 44–47 | **Activity: teach the machine what a chair is** | 1 min alone: write the rule. 2 min pairs: break it. 4 min fours: teach with five examples and one hard no. | | TAs keep time and walk the room. Slides carry the timers. |
| 1:24 | 48 | Capture | Scribes only, one line per four. Read three aloud. | Short answer | About 28 lines. Export them. |
| 1:27 | 49 | What just happened | You built both machines; the machine cannot decide which examples. | | Say the last line slowly. |
| 1:29 | 50–56 | How this course works | Five components; reflection; group project; weekly challenges; three rules; before next week. | | Point at Blackboard for the rubrics. |
| 1:38 | 57–58 | What's your X · one hope and one worry | Closing word cloud, then an anonymous short answer. | Word cloud · short answer (names hidden) | Compare the two clouds. Read the worries, map each to a week. |
| 1:41 | 59 | End | Next week: rules that make things. Bring a laptop. Watch AlphaGo. | | TAs stay 30 minutes. |

Timing is tight at 100 minutes. If the slot is 90 minutes, drop slides 31–32 (learning from examples, Nake) and shorten the cases at 35–37 to one minute each. If the slot is two hours, take the break and extend the Move 37 discussion.

## The activity, in detail: Teach the machine what a chair is

Replaces the scavenger hunt. Eight minutes, no software, three rounds, one capture. It makes students *do* both machines before they have the names for them, and it produces material we reuse in weeks 3, 9 and 11.

1. **Alone, 1 minute — write the rule.** "Define chair so that a machine could apply it with no judgement of its own. One sentence: *X is a chair if ___.* Be strict." Silent, pen and paper. (This is the classical theory of concepts: necessary and sufficient conditions.)
2. **Pairs, 2 minutes — break the rule.** Swap sentences. Find one thing that passes the partner's rule and is not a chair, and one chair that fails it. Write both under the rule. Typical breakers: a rock, a bean bag, a swing, a wheelchair, a throne, half a sofa. (Every rule leaks at the edge: Plato's problem, fuzziness, counter-examples.)
3. **Fours, 4 minutes — teach with examples instead.** Join the pair behind. Pick the five photographs you would show a machine to teach it "chair", then one hard no: something that looks like a chair and is not. Decide together: what does the machine learn if all five are office chairs? Whose chairs are missing? One person writes. (This is dataset curation; the hard negative is a guardrail.)
4. **Capture, 2 minutes — ClassPoint short answer, scribes only.** Format: `RULE broke on: ___ · FIVE EXAMPLES: ___ · HARD NO: ___`. One line per group of four, about 28 lines. Read three aloud.
5. **Debrief, 2 minutes — slide 49.** The rule-writers hit every problem of the classical theory (week 3). The example-pickers hit dataset bias and curation (weeks 9 and 11). A machine can apply the rule and learn from the examples; it cannot decide which examples. That was you.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber walks the room and nudges quiet fours; both collect stray drawings at the end (they make a nice week-2 recap slide).

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 3 | Word cloud | AI in design, one word | Opening temperature; compared with slide 57 at the end; both go into the week-2 recap. |
| 9 | Multiple choice | Which studio are you closest to? | Steers the examples used in weeks 2–6 (type and campaigns vs product form vs feeds). |
| 10 | Multiple choice | How much have you used AI in your design work? | Level check. Mostly A/B: slow down the tool weeks. Many D: pair them with beginners in the challenges. |
| 11 | Multiple choice | Have you written code? | Sizes the week-2 p5.js exercise; if more than a third answer C, add the harder second half. |
| 17 | Short answer | What is AI? One sentence | Read the disagreeing ones; keep for the week-3 recap. |
| 28 | Multiple choice | Which of these is a chair? | Demonstrates fuzziness; no correct answer. |
| 38 | Short answer | Where did AI touch your design work this week? | The new "AI in the wild": the list seeds the week-3 categorising exercise. |
| 48 | Short answer | Activity capture (scribes only) | Rules become week-3 classical-theory examples; example lists become the week-9 bias exercise. |
| 57 | Word cloud | What's your X? One word | Expectations; compare with slide 3. |
| 58 | Short answer, names hidden | One hope and one worry | Expectations and anxieties; map each worry to the week that addresses it and tell them in week 2. |

After class, export the ClassPoint results and keep them in a private folder (they are student data): the three multiple-choice splits, the two clouds, the worries. Bring the numbers to the week-2 planning.

## Contingencies

- **ClassPoint fails.** Word clouds become hands up; short answers become paper, collected by the TAs; the capture is read aloud by three scribes.
- **Projector or PC fails.** The HTML deck runs from any laptop or phone browser; speaker notes with `S`, overview with `O`.
- **Fonts missing.** PowerPoint substitutes Arial automatically; the deck still reads. Install the two variable fonts from `tools/fonts/` for the next class.
- **Running late.** Cut in this order: 31–32, then 33–34, then the break.
- **Running early.** Play the Move 37 chapter; ask the room for a fourth "case from the last month"; let two groups read their whole capture line.

## After class

- TAs stay 30 minutes: accounts, laptops, the four setup items (ClassPoint name, Blackboard, p5.js editor, an image tool).
- Post on Blackboard: the deck link, the playlist, the homework (AlphaGo and the four short art films before week 3; bring a laptop).
- File the ClassPoint exports and the two word-cloud screenshots for the week-2 recap.
- Note the three level-check splits and adjust the week-2 exercise.

## Materials

- `export/week01-classpoint.pptx` (ClassPoint-ready, animations, ait4x master) and `export/week01.pptx` (plain, editable).
- `docs/week01/index.html` (HTML deck, GitHub Pages) — same content, speaker notes included.
- `classpoint/roster-2026-classpoint.csv` — saved-class roster (114 names).
- Paper and pens for 114; the two variable fonts; a laptop with the HTML deck as backup.
