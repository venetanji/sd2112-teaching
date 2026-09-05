# SD2112 · Week 8 lesson plan

**AI as design material** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week08-classpoint.pptx` (58 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week08/` (html deck with the three p5.js sketches running live; `SD2112-week08.pdf` next to it)

## Purpose of this session

For us:

1. Open module 3 by turning week 1's distinction around: the model was in the process (weeks 1–6), now it is in the product — and the product **decides something for each person**. Land the five parts of such a product (the data, the score, the threshold, the decision, the fallback) as the vocabulary of the next six weeks, with the two mistakes every threshold makes.
2. Read five products with one tool, the **decision card** (Spotify DJ, Netflix, Duolingo, the Humane AI Pin, the Rabbit R1), so that the cautionary cases teach the fifth row — what the person sees when the model is wrong — rather than "AI hardware fails".
3. Put a model inside the double diamond (discover: what data exists; define: the decision in one sentence; develop: rule or model, wizard first; deliver: guardrails and monitoring) and map the four phases onto the four project deliverables.
4. Name the model as a material with four properties — grain, edges, appetite, drift — so that the bias register (week 9) and the mediation brief (week 11) have somewhere to start.
5. Set up six weeks of teamwork: a sprint per week, a backlog, a fifteen-minute stand-up at the start of every class, versions and branches for design files, five roles — and start the group proposal in class so that no team goes home with a blank page.

For students, by the end of the class they can:

- say what "using AI" and "incorporating AI" mean on the product side, and name the five parts of a product that decides something for each person;
- explain what a threshold does, name the two mistakes it trades, and say which one their own product can afford;
- fill a decision card for any product with a model inside (the decision, for whom, the data, the score and threshold, if it is wrong), and read Spotify DJ, Netflix, Duolingo, Humane and Rabbit with it;
- place "what data exists", "the decision in one sentence", "rule or model, wizard first" and "guardrails and monitoring" in the four phases of the double diamond, and describe a wizard-of-Oz test of their own decision;
- run a sprint: keep a backlog, hold a stand-up, name the five roles, and version design files as a history with branches.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week08-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 short answer once as a test and reset it. Check the Image Upload button on slide 52 (*caption required*). Open the html deck in a second browser tab: the three sketches (slides 10, 13, 25) run only there; check that the mouse moves the threshold on slide 10, that keys 1–4 switch the person on slide 13 (click inside the sketch first), and that the phase text changes on slide 25. Keep the slide timers ready for rounds 1–4 (slides 48, 50, 51, 53). |
| Amber | Blackboard: post the deck link, the PDF, the group-proposal brief (slide 45: one page, due before the week-9 class), the decision-card template (the blank card of slide 16 as an image, and the panel of slide 51 as text), and the team list from week 7. Export the week-7 quiz results and send Gio the three most-missed questions with their answers for slide 5; anonymise two good pitch sentences from the week-7 wall for the same slide. After class, download the slide-52 cards and read them against the proposals as they arrive. |
| WU Zhao, MA Jie | At the door with the team list: seat every student with their team from the start; anyone not on a team goes to Amber before slide 7, not at the break. One A4 sheet per team (landscape) and pens on every table before slide 47; one phone per team for the upload. During rounds 1–3 walk with two questions: *which person, which moment?* (for lines that start with a technology) and *which data, from where?* (for cards that say "user data"). |
| Gio | Fonts on the classroom PC (`tools/fonts/`). Paste the three most-missed quiz questions into slide 5 before the build, or read them from the export. Screenshot of the week-7 pitch wall for the recap. Backup: the html deck on a laptop — press `S` for notes; the sketches on 10, 13 and 25 run live there. Decide the four cards for the gallery (slide 53) while the wall fills on slide 52: one crisp sentence, one honest "do not have" data row, one feature dressed as a product, one empty fifth row. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Everyone sits with their team from the start. | | |
| 0:03 | 3–6 | Last week, in your words | *Your team number, and what your product decides* (2 min, read six); week 7 in three lines (the three most-missed quiz questions, the pitches, the teams); the semester map (module 3 opens). | Short answer | Most answers name a product, not a decision; do not correct yet — the card at the end does. Anyone without a team goes to Amber now. |
| 0:11 | 7–14 | Using, or incorporating | The distinction turned around; the five parts (figure); **live: the threshold** (two mistakes, the counters); every threshold makes two mistakes; *who decided 0.7?*; **live: personalisation** (the dial, keys 1–4); *you design the space of screens*. | Multiple choice | Slides 9 and 10 are the core of the first half: walk the figure left to right, then move the line. Cut 13 to one sentence if behind. |
| 0:33 | 15–23 | Five products, read as designers | The blank card; Spotify DJ; Netflix; Duolingo; the Humane AI Pin; the Rabbit R1; what the cautionary cases teach; *which leaves the person with the least to do?* | Multiple choice | Ask the room for the five rows before showing each card. Cut 21 (Rabbit) to one sentence if behind; never cut 20 (Humane). |
| 0:57 | 24–29 | The double diamond, with a model inside | **Live: the process** (the model in each phase); four phases, four jobs; the wizard (figure); rule or model; *which phase?* | Multiple choice | 26 maps the phases onto the four deliverables: say the dates. 27 is the method every team uses in week 10. |
| 1:14 | 30 | **Break, 15 min** | Sheets and pens on the tables during the break. | | |
| 1:29 | 31–36 | A model as a material | Holmquist's "intelligence on tap"; the grain (figure: October and December); grain, edges, appetite, drift; the week-1 chairs as the grain; *retrained in December: what do you check?* | Multiple choice | Cut 35 if behind. |
| 1:41 | 37–42 | Working as a team | Scrum in three words; the semester as sprints (figure); versions and branches (figure); five roles; the process is graded. | | Say "nothing is work unless it is on the list" twice. Cut 40 to its caption if behind. |
| 1:55 | 43–46 | The brainstorm ladder | The ladder (figure, climbed aloud once); the group proposal; four rules for brainstorming. | | Slide 45: say the deadline twice. |
| 2:04 | 47–55 | **Activity: ten ideas, one decision** | Section (1 min); round 1, ten ideas (5); *how many?* (2); round 2, pick one (3); round 3, the card (8); upload, one per team (4); the gallery, four cards (5); the vote (2); *the data you do not have* (3). | Multiple choice; image upload; multiple choice; short answer | Nicolò keeps time; the other three TAs walk. Details below. |
| 2:42 | 56 | Debrief | Every product here is a mediation: the loop, Verbeek, the fifth row. | | |
| 2:46 | 57–58 | Homework | The proposal on Blackboard before week 9; Coded Bias; the stand-up at 0:00 next week. | | TAs stay 30 minutes: the first review. |
| 2:50 | | Buffer | | | |

If the room is slow to form teams, take the time from chapter 3 (one sentence each for Rabbit and the cautionary cards) rather than from the activity. If the room is fast, give round 3 ten minutes and let two teams read their card aloud before the gallery.

## The activity, in detail: Ten ideas. One decision.

Team-based, on paper, at the team table; four rounds, each ending in something the room sees. **What goes into ClassPoint is a photo of the decision card (one per team, caption = team number and the decision sentence), a vote, and one short answer.** One A4 sheet per team, pens for everyone, one phone per team.

1. **Teams, 5 minutes — ten ideas (slide 48).** One sheet, one pen each, the ladder on the panel: ten lines, each climbing all five rungs (the person, the moment, the decision, the data, the failure). No debating; if someone says "but", the next line is theirs. Change one rung of the last line to make the next. TAs send lines that start with a technology back to rung one.
2. **Pulse (slide 49).** *How many ideas did your team write?* Fewer than five / five to nine / ten / more than ten. Teams at A get thirty seconds and a TA.
3. **Teams, 3 minutes — pick one (slide 50).** Read the ten aloud; apply the three tests on the panel (does the data exist? is the failure survivable? can you wizard it by week 10?); a line that fails one is out. Tie-break: the clearest sentence at rung three. Circle it. A pick, not a marriage: week 10 can change it.
4. **Teams, 8 minutes — the decision card (slide 51).** One A4, landscape, big letters: team number; the decision in one sentence; for whom (one person, named like a character); the data in two columns, *have* and *do not have*; if it is wrong — what she sees, what she can do, the fallback. If the honest answer to row five is "nothing", write "nothing". This is the proposal in draft.
5. **Capture, 4 minutes — one photo per team (slide 52).** Caption required: the team number, then the decision sentence word for word. Put the wall on screen; while it fills, read three captions without the card and ask the room what the product is — where the room cannot say, the sentence is not finished.
6. **The gallery, 5 minutes (slide 53).** Four cards from the wall on screen one at a time, labelled A to D, team numbers only, no names: one crisp sentence, one honest data row, one feature dressed as a product, one empty fifth row. For each, three questions to the room: is the decision one sentence? does the data exist? what happens on the wrong day?
7. **The vote, 2 minutes (slide 54).** *Which product would you let decide for you?* Card A–D. No correct answer; the winning team gets a participation star and thirty seconds on what its person does on the wrong day.
8. **Last question, 3 minutes (slide 55).** Scribes only: *the data your product needs and does not have* — team number, then the data, and who holds it. Read five and sort them into "ask" (consent) and "take" (someone else's). This is the seed of week 9.
9. **Debrief, 4 minutes (slide 56).** The loop from week 7; Verbeek; the card is the proposal, the missing data is next week, the wrong day is the week after. *The model will make the score. You decided what it decides, for whom, from what, and what happens when it is wrong. That was the design.*

The card is the draft of the group proposal (slide 45): typed up, with two extra lines (rule or model, and why; the team and the five roles), one page on Blackboard before the week-9 class. Amber answers every proposal in the week-9 stand-up.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room with the two questions (which person, which moment; which data, from where), and note the four cards for the gallery.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Short answer | Your team number, and what your product decides for each person. | Warm-up and baseline: most name a product, not a decision. Compare with the slide-52 captions. |
| 12 | Multiple choice | A product shows a feature only above a score of 0.7. Who decided 0.7? | Quick check: B — someone chose it, and can change it. |
| 23 | Multiple choice | When the model is wrong, which product leaves the person with the least to do? | Quick check: D — the Pin. Accept C as the better argument (a wrong explanation is invisible). |
| 29 | Multiple choice | "What data already exists about this person?" belongs to which phase? | Quick check: A — discover. |
| 36 | Multiple choice | Shipped in October, retrained in December: what must you check again? | Quick check: B — the threshold and the two errors, on the people it now decides for. |
| 49 | Multiple choice | How many ideas did your team write? | Pulse after round 1; teams under five get a TA. |
| 52 | Image upload, one per team, caption required | The decision card | The wall; the gallery; downloaded for Amber to read against the proposals. |
| 54 | Multiple choice | Gallery vote: which product would you let decide for you? (Cards A–D) | The room decides; a star for the winning team. Team numbers only. |
| 55 | Short answer, one per team | The data your product needs and does not have. | Sorted into "ask" and "take"; week 9 opens with it; the bias register starts here. |

All nine buttons are generated by the build (caption required on 52).

## What to keep after class

- The slide-4 sentences and the slide-52 captions side by side: the before-and-after of the day, and the first entry in each team's process record.
- The slide-52 cards (download) and the slide-55 answers (export): Amber reads the cards against the proposals; week 9 opens with the missing-data lines.
- The gallery winner and the split on slide 54, for the participation stars.
- Which teams have no card, or a card that is a feature: they get the first review slot with the TAs after class.
