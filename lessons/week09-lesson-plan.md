# SD2112 · Week 9 lesson plan

**Data, bias and privacy** · three-hour lecture-workshop (about 160 minutes of content plus a 15-minute break, with a 6-minute buffer) · deck: `week09-classpoint.pptx` (57 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week09/` (html deck with the three p5.js sketches running live; `SD2112-week09.pdf` next to it)

## Purpose of this session

For us:

1. Open with the **first stand-up** of the six that week 8 promised: twelve minutes at the team table, three questions standing, the proposal as the increment, Amber's one sentence back to every team — so the day starts from each team's own data line.
2. Land the sentence of the day — **the model's world is the dataset's world** — mechanically: a dataset is examples, labels, a window and a purpose, and a model trained inside a window is confident and wrong outside it (the live sampling window, slides 13–14).
3. Replace "AI is biased" with **four doors**, each a decision somebody made: who was collected (data), who named them (labels), what the model was told to want and where the line was drawn (algorithmic), and what the product learns from its own use (interaction) — with a designer-facing case at every door.
4. Make the **threshold** felt as a design decision: two ways to be wrong, the same line costing two groups differently, the COMPAS contradiction and the theorem behind it, and the four things a team can actually do about it.
5. Teach **privacy** as three design moves — collect less, link less, keep less — with re-identification by linkage, k-anonymity live, and synthetic data as the escape route that is not one; and name the two regimes (GDPR, Hong Kong PDPO) as principles, not law.
6. Run the **neutrality debate** as two votes on the same question, before and after the teams have mapped their own product, so that the movement in the room comes from their own work.
7. Get every team to leave with a **bias register** for its concept — three decisions, five columns each, red-penned by another team — which goes on Blackboard tonight with the concept board and becomes the data, bias and guardrail paragraphs of the mediation brief.

For students, by the end of the class they can:

- say what a dataset is (examples, labels, a window, a purpose) and why a model only ever knows the window, with the week-1 chairs as the example;
- name the four doors where bias enters and give one real case and one case from their own product for each;
- explain a threshold's two kinds of error, say why one threshold gives two groups different error rates, and choose (and defend) one of the four responses;
- explain re-identification by linkage and k-anonymity in one sentence each, and name the three columns of their own product's data that would re-identify a person;
- fill a bias register row that passes the five tests (a verb and a person; a named window; a real thin group; both harms; a rule plus a person to appeal to);
- take a position on whether a model can be neutral and argue the other side for two minutes.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open with the saved class, `week09-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-5 word cloud once as a test and reset it. Check the anonymous short answer on slide 34 (names hidden), the one-per-team short answer on slide 49 and the Image Upload button on slide 51 (*caption required*). Html deck open on the laptop: the sketches on slides 14, 26 and 38 run there (the PowerPoint shows stills); rehearse each for one minute — the window (a click locks it and the panel says LOCKED), the threshold with a click (group 2 gets its own threshold and the false-YES gap appears), k from 1 to 6 (at 5 the table goes blank). Slide timers for the stand-up (4), the pair debate (43), the three rounds (48, 50, 52) and the short answer (49). |
| Amber | Read every week-8 proposal before class and prepare one sentence back per team for the stand-up (slide 4). Export the week-8 short answer *the data your product needs and does not have*, one line per team, and bring it to round 2 (slide 50): it is read back to any team whose data column is empty. From the proposals: three anonymised "with what data" phrases for slide 8, and the list of teams that already named a dataset (they get a mention). Blackboard: the two submission points due tonight — **concept board** and **bias register**, one per team — with the time confirmed by Gio before slide 56; the register template (slide 50) posted as a document; the deck link and the PDF. Coded Bias: check that the Netflix title plays from Hong Kong (or ask the library for a licence) before posting a where-to-watch line; the PBS Independent Lens page is background reading, not a place to stream. |
| WU Zhao, MA Jie | At the door: teams sit together from the start (the week-7 teams; anyone without a team joins the nearest one for today); a ClassPoint join check. During the stand-up walk with one question per team: what is the data, and do you have it? Thirty A3 sheets with the five-column register grid pre-drawn, one per team, and thirty red pens for round 3. During the activity walk with the five tests from slide 46 and read one aloud at any table that has written "users", "everyone" or "we will monitor it". |
| Gio | Fonts on the classroom PC (`tools/fonts/`). Screenshots: the word cloud (slide 5) for slide 41, and the vote-1 split (slide 7) for slide 55 — take both before the break. Decide the Blackboard time for tonight and tell Amber. Backup: the html deck on a laptop — press `S` for notes; slides 14, 26 and 38 run live there. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops, teams together from the start. | | |
| 0:03 | 3–9 | Last week, in your words | **The stand-up** at the team table (4, 12 min, standing: three questions, then the proposal read aloud, one item on top of the backlog; Amber answers every proposal); *Coded Bias, one word* (2); the film — the mask, Gender Shades, where to watch (2); **vote 1: can a model be neutral?** (1); the proposals, three parts, today is the third (2); the map (1). | Word cloud; multiple choice | The stand-up is timed on the slide; hold it at twelve. Screenshot the word cloud and the vote-1 split. Replace the quotes on slide 8 with Amber's three phrases. |
| 0:23 | 10–16 | A dataset is a set of examples | The sentence of the day (1); anatomy of a dataset — examples, labels, window, purpose, datasheets (3); three windows, three rules (3); **live: the window** (5); the week-1 chairs and LAION (4); quick check (2). | Multiple choice | Slide 14 is the sketch: park the window in the corner, slide it to the far edge, find a one-colour window, click to lock it (the panel says LOCKED). Cut 12 if behind. |
| 0:42 | 17–23 | Four doors | The loop and the four doors (3); data bias — Gender Shades, Amazon, your beta testers (4); label bias — ImageNet, Google Photos, who says what "tired" is (5); the objective — Twitter's crop and what the audit did and did not find (4); interaction — Tay, PredPol, Sweeney's ads, your feed (4); quick check (2). | Multiple choice | Ask two teams who their beta testers are at slide 19. Cut the Tay card's discussion if behind, not the slide. |
| 1:05 | 24–30 | The threshold | Anatomy: two ways to be wrong (4); **live: the threshold**, then click for a threshold per group (5); COMPAS: both sides right, the theorem (3); equal thresholds or equal error rates: four things a team can do (3); stance poll (2); *a threshold is a design decision* (1). | Multiple choice | Slide 26: narrate the bars while sliding; the click is the Hardt move — group 2's threshold drops and its false-YES bar rises. One person per letter defends the poll on 29. |
| 1:23 | 31 | **Break, 15 min** | Teams sit together after the break. Anyone who has not seen the film: the first twenty minutes now. | | |
| 1:38 | 32–39 | Privacy | Four principles, two laws (4); *one thing your product could stop collecting* (3); re-identification by linkage — Sweeney, Weld (3); 87 % (1); Netflix Prize, Strava, the rule (2); **live: k-anonymity** (5); synthetic data and model collapse (3). | Short answer, names hidden | Slide 38: slide k from 1 to 6 and read the neighbour line each time; at k = 5 the table is blank — say why. Cut 37 or 39 if behind. |
| 1:59 | 40–43 | Can a model be neutral? | Three positions, with the slide-5 word cloud next to them (4); the sentence to argue with (1); **pairs: argue the side you did not vote for** (4, timed). | | TAs note the two best examples per side for slide 55. Do not give your own answer. |
| 2:09 | 44–46 | The bias register | The filled example, row by row (3); how to fill it — the five tests (2). | | Ask the room what is missing from the second row of the example. |
| 2:15 | 47–55 | **Activity: map the ethics of your concept** | Section (1); round 1, the decisions (6); capture 1, one line per team (2); round 2, the register (10); capture 2, one image per team (4); round 3, the red pen (6); *which of your biases is the worst?* (2); what just happened (2); **vote 2** (3). | Short answer; image upload; 2 × multiple choice | Nicolò keeps time; the other three TAs walk with the five tests. Details below. |
| 2:51 | 56–57 | Homework | Concept board and register on Blackboard tonight; prototype v1 started, shown as it stands at the week-10 stand-up, on Blackboard before week 11; look at your own feed before next week. | | TAs stay 30 minutes. |
| 2:54 | | Buffer | | | |

If the room is slow, cut slides 12, 37 and 39 and give round 3 four minutes instead of six; the stand-up stays at twelve, the timer is on the slide. If the room is fast, let two teams read a full row of their register aloud after capture 2 and have the room say which of the five tests it fails, if any.

## The activity, in detail: Map the ethics of your concept

Each team takes its own product from the week-8 proposal and writes a **bias register**: one row per decision the model makes, five columns — the decision, the data it learns from, who is thin in that data, the harm when it is wrong (both ways), the guardrail. Paper (the A3 grid the TAs hand out) or a shared document; the template is on slide 50 and the filled example (Nightlight, a fictional bedside lamp) on slide 45. **Every round ends in ClassPoint: one line per team after round 1, one image per team after round 2 with a caption naming the product and the row the team thinks is the worst, and two votes after round 3.**

1. **Round 1, teams, 6 minutes — the decisions (slide 48).** Open the proposal; write down every decision the model makes for a person, a verb and a person each. Most products have five to ten once they look: the ranking, the default, the notification, the moment it stays silent. Circle the three with the biggest harm when wrong.
2. **Capture 1, 2 minutes — one line per team (slide 49).** The scribe types the team number and the decision with the biggest harm, as a verb and a person. Read four aloud and apply the first test: "personalises the experience" fails, "dims the lamp when it thinks she is tired" passes; a line that fails goes back to its team as the first row to fix. Keep the export: week 10 opens by asking each team for the guardrail of this same decision.
3. **Round 2, teams, 10 minutes — the register (slide 50).** Three rows, five columns. Every cell names something concrete: "users" is not a data source, "everyone" is not a thin group, "we will monitor it" is not a guardrail. The TAs walk with the five tests from slide 46; an empty cell after two minutes is a finding, not a failure — usually the team has not decided what the data is, so send them back a column, and Amber reads the team its own week-8 line about the data it does not have. Nicolò calls two minutes before the end so that every cell has at least a question mark.
4. **Capture 2, 4 minutes — one image per team, caption required (slide 51).** A photo or screenshot of the three rows; caption: the product name and the worst row. Put the wall on screen and read one row from two registers — one with a real person in the thin column, one with "everyone" — naming rows, not teams.
5. **Round 3, swap, 6 minutes — the red pen (slide 52).** Swap registers with the neighbouring team. In red, add one person who is thin in their data and one harm they did not write. Give it back; read the additions; no arguing. This is the Gender Shades audit done by amateurs in a hurry, and it works because a window is easiest to see from outside the team.
6. **Which of your team's biases is the worst? (slide 53).** One vote per person, so teams can disagree with themselves. Ask a D (interaction) to explain — those products learn after they ship, which is week 10 — and ask a C (algorithmic) which threshold they meant.
7. **What just happened (slide 54).** The decisions were more than they thought; the third column was the hard one and the red pen found more; the guardrail is machine A guarding machine B. *The model learned the window. You decided who else needs to be in it. That was the design.*
8. **Vote 2 (slide 55).** The same four answers as slide 7, side by side with the morning's screenshot. Movement in either direction is the point: whoever moved, moved because of their own product. The TAs read the two best examples from the pair debate (slide 43).

The register goes on Blackboard tonight with the concept board (slide 56), red-pen additions marked as additions; it becomes the bias and guardrail paragraphs of the mediation brief. Prototype v1 is next sprint's item: the teams start it now, show whatever exists at the week-10 stand-up, and upload it before week 11 (the week-10 deck says the same).

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk with the five tests, help teams that stall on the third column, and note the two or three best rows for the week-11 datasets session.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 5 | Word cloud | Coded Bias: one word that stayed with you. | Warm-up and a check that the film was watched; screenshot for slide 41. |
| 7 | Multiple choice | Can a model be neutral? (vote 1 of 2) | No correct answer; screenshot the split for slide 55. |
| 16 | Multiple choice | Why did the model give four almost identical chairs? | Quick check: C — the most typical chair in its dataset. |
| 23 | Multiple choice | A photo app learns from what you favourite and stops showing your grandmother. Which door? | Quick check: D — interaction bias (C, the objective, is half right; reward the reasoning). |
| 29 | Multiple choice | Your model is less sure about one group. What ships? | Stance; no correct answer. One person per letter defends it. |
| 34 | Short answer, names hidden | Name one thing your product could stop collecting tomorrow. | Data minimisation as an exercise; the list feeds the register's data column. Keep it. |
| 49 | Short answer, one per team | Team number, and the decision with the biggest harm. | The first test applied in public; the export seeds the week-10 warm-up (the guardrail of the same decision). |
| 51 | Image upload, one per team, caption required | Your register: three rows; caption = product and worst row. | The wall; the captions say which row each team fears. Download for week 11 and the brief review. |
| 53 | Multiple choice | Which of your team's biases is the worst? | Self-diagnosis; no correct answer. Ask a D and a C to explain. |
| 55 | Multiple choice | Now that you have mapped your own product: can a model be neutral? (vote 2 of 2) | Show next to the slide-7 split; the movement is the debrief. |

All ten buttons are generated by the build (names hidden on 34; caption required on 51).

## What to keep after class

- The two vote screenshots (slides 7 and 55): they open the week-12 chapter on transparency and accountability.
- The slide-34 list of things products could stop collecting: it comes back in week 10 with the feed, and in week 11 with the datasets.
- The slide-49 decisions, one per team: week 10's warm-up asks for the guardrail of the same decision, so keep the export next to the week-10 deck.
- The slide-51 registers, downloaded: Amber checks them against tonight's Blackboard uploads and flags any team whose data column still says "users"; the three best rows are shown (anonymised) in week 11 next to the LoRA datasets.
- Which teams had nothing to say at the stand-up, or no proposal on Blackboard: they get the first review slot with Amber after class.
- The best red-pen additions and the two best debate examples the TAs noted: the week-12 recap.
