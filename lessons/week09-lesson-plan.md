# SD2112 · Week 9 lesson plan

**Data, bias and privacy** · three-hour lecture-workshop (about 165 minutes of content plus a 15-minute break, with a buffer) · deck: `week09-classpoint.pptx` (55 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week09/` (html deck with the three p5.js sketches running live; `SD2112-week09.pdf` next to it)

## Purpose of this session

For us:

1. Land the sentence of the day — **the model's world is the dataset's world** — mechanically: a dataset is examples, labels, a window and a purpose, and a model trained inside a window is confident and wrong outside it (the live sampling window, slides 12–13).
2. Replace "AI is biased" with **four doors**, each a decision somebody made: who was collected (data), who named them (labels), what the model was told to want and where the line was drawn (algorithmic), and what the product learns from its own use (interaction) — with a designer-facing case at every door.
3. Make the **threshold** felt as a design decision: two ways to be wrong, the same line costing two groups differently, the COMPAS contradiction and the theorem behind it, and the four things a team can actually do about it.
4. Teach **privacy** as three design moves — collect less, link less, keep less — with re-identification by linkage, k-anonymity live, and synthetic data as the escape route that is not one; and name the two regimes (GDPR, Hong Kong PDPO) as principles, not law.
5. Run the **neutrality debate** as two votes on the same question, before and after the teams have mapped their own product, so that the movement in the room comes from their own work.
6. Get every team to leave with a **bias register** for its concept — three decisions, five columns each, red-penned by another team — which goes on Blackboard tonight with the concept board and becomes the data, bias and guardrail paragraphs of the mediation brief.

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
| Nicolò | Classroom PC: ClassPoint open with the saved class, `week09-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 word cloud once as a test and reset it. Check the anonymous short answer on slide 33 (names hidden) and the Image Upload button on slide 49 (*caption required*). Html deck open on the laptop: the sketches on slides 13, 25 and 37 run there (the PowerPoint shows stills); rehearse each for one minute — the window, the threshold with a click, k from 1 to 6. Slide timers for the pair debate (42) and the three rounds (47, 48, 50). |
| Amber | Blackboard: the two submission points due tonight — **concept board** and **bias register**, one per team — with the time confirmed by Gio before slide 54; the register template (slide 48) posted as a document; the deck link and the PDF; the Coded Bias links (Netflix title page, PBS Independent Lens page) in an announcement for anyone who has not watched it. From the week-8 proposals: three anonymised "with what data" phrases for slide 7, and a list of the teams that already named a dataset (they get a mention). |
| WU Zhao, MA Jie | At the door: teams sit together from the start (the week-7 teams; anyone without a team joins the nearest one for today); a ClassPoint join check. Thirty A3 sheets with the five-column register grid pre-drawn, one per team, and thirty red pens for round 3. During the activity walk with the five tests from slide 45 and read one aloud at any table that has written "users", "everyone" or "we will monitor it". |
| Gio | Fonts on the classroom PC (`tools/fonts/`). Take a screenshot of the vote-1 split (slide 6) before the break; it goes next to vote 2 (slide 53). Decide the Blackboard time for tonight and tell Amber. Backup: the html deck on a laptop — press `S` for notes; slides 13, 25 and 37 run live there. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops, teams together from the start. | | |
| 0:03 | 3–8 | Last week, in your words | *Coded Bias, one word* (2 min); the film — the mask, Gender Shades, where to watch (3); **vote 1: can a model be neutral?** (1); the proposals, three parts, today is the third (3); the map (1). | Word cloud; multiple choice | Screenshot the vote-1 split. Replace the quotes on slide 7 with Amber's three phrases. |
| 0:15 | 9–15 | A dataset is a set of examples | The sentence of the day (1); anatomy of a dataset — examples, labels, window, purpose, datasheets (3); three windows, three rules (3); **live: the window** (5); the week-1 chairs and LAION (4); quick check (2). | Multiple choice | Slide 13 is the sketch: park the window in the corner, slide it to the far edge, find a one-colour window, lock it. Cut 11 if behind. |
| 0:35 | 16–22 | Four doors | The loop and the four doors (3); data bias — Gender Shades, Amazon, your beta testers (5); label bias — ImageNet, Google Photos, who says what "tired" is (5); the objective — Twitter's crop (4); interaction — Tay, PredPol, Sweeney's ads, your feed (5); quick check (2). | Multiple choice | Ask two teams who their beta testers are at slide 18. Cut the Tay card's discussion if behind, not the slide. |
| 1:00 | 23–29 | The threshold | Anatomy: two ways to be wrong (4); **live: the threshold**, then click for a threshold per group (5); COMPAS: both sides right, the theorem (4); equal thresholds or equal error rates: four things a team can do (3); stance poll (2); *a threshold is a design decision* (1). | Multiple choice | Slide 25: narrate the bars while sliding; the click is the Hardt move. One person per letter defends the poll on 28. |
| 1:19 | 30 | **Break, 15 min** | Teams sit together after the break. Anyone who has not seen the film: the first twenty minutes now. | | |
| 1:34 | 31–38 | Privacy | Four principles, two laws (4); *one thing your product could stop collecting* (3); re-identification by linkage — Sweeney, Weld (3); 87 % (1); Netflix Prize, Strava, the rule (3); **live: k-anonymity** (5); synthetic data and model collapse (3). | Short answer, names hidden | Slide 37: slide k from 1 to 6 and read the neighbour line each time; at k = 5 the table is empty — say why. Cut 36 or 38 if behind. |
| 1:56 | 39–42 | Can a model be neutral? | Three positions (4); the sentence to argue with (1); **pairs: argue the side you did not vote for** (5, timed). | | TAs note the two best examples per side for slide 53. Do not give your own answer. |
| 2:06 | 43–45 | The bias register | The filled example, row by row (3); how to fill it — the five tests (3). | | Ask the room what is missing from the second row of the example. |
| 2:12 | 46–53 | **Activity: map the ethics of your concept** | Section (1); round 1, the decisions (6); round 2, the register (10); capture, one image per team (4); round 3, the red pen (6); *which of your biases is the worst?* (2); what just happened (2); **vote 2** (3). | Image upload; 2 × multiple choice | Nicolò keeps time; the other three TAs walk with the five tests. Details below. |
| 2:46 | 54–55 | Homework | Concept board and register on Blackboard tonight; prototype v1 for week 10; two screenshots of recommendations. | | TAs stay 30 minutes. |
| 2:49 | | Buffer | | | |

If the room is slow, cut slides 11, 36 and 38 and give round 3 four minutes instead of six. If the room is fast, let two teams read a full row of their register aloud after the capture and have the room say which of the five tests it fails, if any.

## The activity, in detail: Map the ethics of your concept

Each team takes its own product from the week-8 proposal and writes a **bias register**: one row per decision the model makes, five columns — the decision, the data it learns from, who is thin in that data, the harm when it is wrong (both ways), the guardrail. Paper (the A3 grid the TAs hand out) or a shared document; the template is on slide 48 and the filled example (Nightlight, a fictional bedside lamp) on slide 44. **What goes into ClassPoint is one image per team, with a caption naming the product and the row the team thinks is the worst**; then two votes.

1. **Round 1, teams, 6 minutes — the decisions (slide 47).** Open the proposal; write down every decision the model makes for a person, a verb and a person each. Most products have five to ten once they look: the ranking, the default, the notification, the moment it stays silent. Circle the three with the biggest harm when wrong.
2. **Round 2, teams, 10 minutes — the register (slide 48).** Three rows, five columns. Every cell names something concrete: "users" is not a data source, "everyone" is not a thin group, "we will monitor it" is not a guardrail. The TAs walk with the five tests from slide 45; an empty cell after two minutes is a finding, not a failure — usually the team has not decided what the data is, so send them back a column. Nicolò calls two minutes before the end so that every cell has at least a question mark.
3. **Capture, 4 minutes — one image per team, caption required (slide 49).** A photo or screenshot of the three rows; caption: the product name and the worst row. Put the wall on screen and read one row from two registers — one with a real person in the thin column, one with "everyone" — naming rows, not teams.
4. **Round 3, swap, 6 minutes — the red pen (slide 50).** Swap registers with the neighbouring team. In red, add one person who is thin in their data and one harm they did not write. Give it back; read the additions; no arguing. This is the Gender Shades audit done by amateurs in a hurry, and it works because a window is easiest to see from outside the team.
5. **Which of your team's biases is the worst? (slide 51).** One vote per person, so teams can disagree with themselves. Ask a D (interaction) to explain — those products learn after they ship, which is week 10 — and ask a C (algorithmic) which threshold they meant.
6. **What just happened (slide 52).** The decisions were more than they thought; the third column was the hard one and the red pen found more; the guardrail is machine A guarding machine B. *The model learned the window. You decided who else needs to be in it. That was the design.*
7. **Vote 2 (slide 53).** The same four answers as slide 6, side by side with the morning's screenshot. Movement in either direction is the point: whoever moved, moved because of their own product. The TAs read the two best examples from the pair debate (slide 42).

The register goes on Blackboard tonight with the concept board (slide 54), red-pen additions marked as additions; it becomes the bias and guardrail paragraphs of the mediation brief.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk with the five tests, help teams that stall on the third column, and note the two or three best rows for the week-11 datasets session.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Word cloud | Coded Bias: one word that stayed with you. | Warm-up and a check that the film was watched; screenshot for slide 40. |
| 6 | Multiple choice | Can a model be neutral? (vote 1 of 2) | No correct answer; screenshot the split for slide 53. |
| 15 | Multiple choice | Why did the model give four almost identical chairs? | Quick check: C — the most typical chair in its dataset. |
| 22 | Multiple choice | A photo app learns from what you favourite and stops showing your grandmother. Which door? | Quick check: D — interaction bias (C, the objective, is half right; reward the reasoning). |
| 28 | Multiple choice | Your model is less sure about one group. What ships? | Stance; no correct answer. One person per letter defends it. |
| 33 | Short answer, names hidden | Name one thing your product could stop collecting tomorrow. | Data minimisation as an exercise; the list feeds the register's data column. Keep it. |
| 49 | Image upload, one per team, caption required | Your register: three rows; caption = product and worst row. | The wall; the captions say which row each team fears. Download for week 11 and the brief review. |
| 51 | Multiple choice | Which of your team's biases is the worst? | Self-diagnosis; no correct answer. Ask a D and a C to explain. |
| 53 | Multiple choice | Now that you have mapped your own product: can a model be neutral? (vote 2 of 2) | Show next to the slide-6 split; the movement is the debrief. |

All nine buttons are generated by the build (names hidden on 33; caption required on 49).

## What to keep after class

- The two vote screenshots (slides 6 and 53): they open the week-12 chapter on transparency and accountability.
- The slide-33 list of things products could stop collecting: it comes back in week 10 with the feed, and in week 11 with the datasets.
- The slide-49 registers, downloaded: Amber checks them against tonight's Blackboard uploads and flags any team whose data column still says "users"; the three best rows are shown (anonymised) in week 11 next to the LoRA datasets.
- The best red-pen additions and the two best debate examples the TAs noted: the week-12 recap.
