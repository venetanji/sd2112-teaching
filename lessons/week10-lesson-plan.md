# SD2112 · Week 10 lesson plan

**Recommendation systems** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week10-classpoint.pptx` (62 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week10/` (html deck with the four p5.js sketches running live; `SD2112-week10.pdf` next to it)

## Purpose of this session

For us:

1. Close module 3 with the product most people meet most often: the feed. Land it as week 8's five parts run in a loop — a pool, a few hundred candidates, a score, a screen, and what the person does becoming the data of the next screen — so that "the algorithm" stops being one thing and becomes five parts, four of which are rules somebody writes.
2. Teach the two ways to say "this is like that" with the course spine: **content-based filtering** (an item is a point; the axes are written by hand or learned — machine A or B) and **collaborative filtering** (the crowd is the description; no features at all — machine B from behaviour alone), with the user–item matrix, the Netflix Prize, two towers in a sentence, and the cold start as a design problem.
3. Make the **objective** the centre of the second half: the model maximises a proxy, not a value (Strathern 1997); YouTube's own arc from clicks to watch time to satisfaction; the echo-chamber sketch with an exploration dial; and the honest state of the evidence on filter bubbles.
4. Give every team three handles on a feed — the objective, the explanation ("why am I seeing this"), the exploration dial — with Ihde's relations (a feed is mostly hermeneutic and mostly background) and the DSA as the floor.
5. Have every team build a similarity search with their own hands (a language model writes the axes, a twenty-line script finds the neighbours), then write the objective, the drift, the explanation and the dial of its own product — the raw material of the mediation brief.

For students, by the end of the class they can:

- name the five parts of a feed and say which one a model makes and which four are rules somebody sets;
- explain content-based and collaborative filtering, say what each needs and what each cannot do (the mirror; the cold start), and read the user–item matrix;
- say what an embedding is (a list of numbers; near means similar by whatever the numbers measure), and why the metric and its weights are a design decision;
- state Goodhart's law in Strathern's words and apply it to a product: the number the model makes bigger, and the cheap route it will find;
- name the three handles — objective, explanation, dial — with one shipped example of each (YouTube's satisfaction surveys; TikTok's "Why this video"; Spotify's mix of what you like and what you might like), and place a feed among Ihde's four relations.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week10-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-5 short answer once as a test and reset it. Check the Image Upload button on slide 56 (*caption required*). Open the html deck in a second browser tab: the four sketches (slides 16–17, 22, 35, 47) run only there; check that T switches the metric on 16 (click inside the sketch first), that clicking the YOU row on 22 changes the predictions, that mouse y moves the exploration rate on 35 and a card click re-samples the screen, and that a click cycles the product on 47. Keep the slide timers ready for the stand-up (4), the hands-on (48) and rounds 1–4 (51, 53, 55, 57). |
| Amber | Blackboard: post the deck link, the PDF, the prompt template (slide 46, also on the site), the script (slide 47; the sketch page `week10/sketches/w10-vectors.html` has it — view source), the four activity panels (slides 51, 53, 55, 57) as text, and the prototype-v1 brief with its deadline (slide 60; confirm the wording with Gio). Read the week-9 registers as they arrived and pick two good guardrail lines to read aloud on slide 5 (team numbers only). After class, export the slide-52 and slide-54 answers and download the slide-56 screens; they are read against the prototypes. |
| WU Zhao, MA Jie | At the door with the team list: seat every student with their team from the start; anyone without a team goes to Amber during slide 4. One laptop per team, logged into `editor.p5js.org` and `genai.polyu.edu.hk` before the break. One A4 sheet per team (landscape) and pens on every table before slide 50; one phone per team for the upload. During the hands-on (48) walk for the usual errors (a missing comma in the table, a row with four numbers, `names` and `v` of different lengths). During rounds 1 and 3 walk with one question each: *what would you log?* (for objectives that are values, not numbers) and *in her words?* (for reasons written in the product's words). |
| Gio | Fonts on the classroom PC (`tools/fonts/`). Screenshots from week 9 (the register wall) for the recap. Backup: the html deck on a laptop — press `S` for notes; the sketches on 16, 17, 22, 35 and 47 run live there. Decide the prototype-v1 deadline wording for slide 60 and Blackboard. While the wall fills on slide 56, pick two screens for the room: one with an honest data line, one with the data line missing. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Everyone sits with their team; laptops out. | | |
| 0:03 | 3–7 | Last week, in your words | The stand-up at the team table (4, 12 min, standing: three questions, then show what exists of prototype v1); *team number and the guardrail your register names* (5, read six); week 9 in three lines (Coded Bias, the four doors, the register); the semester map (module 3 closes). | Short answer | The stand-up is the review of the sprint: show the thing, not the plan. A team with nothing to show gets a slot with Amber after class, not a lecture now. |
| 0:20 | 8–12 | The feed is the product | *What does your feed think you are?* (9, word cloud); the anatomy (10, figure: five parts in a loop); three feeds in their own words (11: YouTube, TikTok, Spotify); *nobody drew your home screen*. | Word cloud | Slide 10 is the vocabulary of the day: walk it left to right and name which parts are rules. Keep the word-cloud screenshot for the debrief. |
| 0:32 | 13–19 | An item is a point | Embeddings (14, figure); three ways to get the axes (15: by hand A, learned B, from behaviour); **live: similarity search** (16; press T); the metric as code (17); content-based filtering (18: rule, strength, limit); *two songs are close in an embedding: what does it mean?* (19). | Multiple choice | 16 and 17 are the mechanism of the week: move the query, then press T without moving it. Cut 17 to one sentence if behind. |
| 0:54 | 20–29 | People like you | The matrix (21, figure); **live: collaborative filtering** (22; click your row); three dates (23: 1992, 1994, 2003); the Netflix Prize (24); three families (25); two towers in a sentence (26, figure); the cold start (27); *a new user opens the app: which system has the least to say?* (28); *a recommendation is a neighbour* (29). | Multiple choice | On 22 click H after A and D and watch the similarities fall. Cut 26 to its caption and 25 to one sentence if behind; never cut 24 (the privacy lesson) or 27. |
| 1:18 | 30 | **Break, 15 min** | Laptops logged into the p5 editor and GenAI before leaving the room. | | |
| 1:33 | 31–38 | The objective | *The model optimises what you click, not what you value* (32); four steps down (33, figure: value, proxy, target, trap); YouTube's three objectives 2012 / 2016 / 2019 (34); **live: the echo chamber** (35; mouse y = exploration, click = engage); Strathern (36); bubbles: Sunstein, Pariser, the evidence (37); *trained to maximise minutes: what will it learn?* (38). | Multiple choice | Slide 33 is the core of the second half; say Strathern's sentence twice. On 35 start at the still, go to zero exploration and click the commonest card, then go to fifty percent. Cut 36 if behind (it is on 33's caption). |
| 1:51 | 39–44 | The feed as a mediation | Ihde's four relations with a feed in each (40, figure); designing the objective: time, satisfaction, return (41); "why am I seeing this": Facebook 2019, TikTok 2022, Spotify 2018, the DSA (42); the exploration dial: exploit, explore, reset, the shared row (43); *you design the objective, the explanation and the dial* (44). | | 42 and 43 are the brief for rounds 3 and 4; read them as instructions. |
| 2:04 | 45–49 | **Workshop: similarity search, by hand** | The prompt (46); the script, live (47); **hands on** (48, 10 min: ten descriptions into GenAI, the table into the script, then price times three); what to look for (49: the axes, the disagreement, the weight). | | The TAs walk. Teams that finish early add a sixth axis the model did not think of. |
| 2:18 | 50–59 | **Activity: your feed's objective** | Section (1 min); round 1, the objective (3); capture 1 (2); round 2, the drift (3); capture 2 (2); round 3, the "why am I seeing this" screen on paper (8); capture 3, one photo per team (3); round 4, the dial (2); the vote (2); what just happened (2). | 2 × short answer; image upload; multiple choice | Nicolò keeps time; the other three TAs walk. Details below. |
| 2:46 | 60–62 | Homework | Prototype v1 on Blackboard; a draft poster and a draft mediation brief for the poster lab; the Belamy video (61). | | TAs stay 30 minutes: the prototype review. |
| 2:50 | | Buffer | | | |

If GenAI is slow, do the hands-on with the ten fictional products already in the script (skip the prompt) and cut 49 to one sentence. If the room is fast, give round 3 ten minutes and let two teams read their three reasons aloud before the wall.

## The activity, in detail: Your feed's objective

Team-based, at the team table; four rounds, each ending in ClassPoint. **What goes into ClassPoint is two lines of text per team (the objective, then the drift), a photo of the "why am I seeing this" screen (caption = team number and the first reason), and one vote.** One A4 sheet per team, pens, one phone.

1. **Teams, 3 minutes — the objective (slide 51).** One number: the one a developer would put in the code as the thing to maximise, for each person, per unit of time. Written as the sentence on the panel: *for each person, maximise ______ per ______.* A team that cannot name a number writes "none yet" and says why — it has found that its product is a rule, not a model, which is a good line for the brief. TAs: *what would you log?*
2. **Capture 1, 2 minutes (slide 52).** Short answer, scribe only: team number, then the objective. Read five aloud, fast, without comment; sort them in your head into time, satisfaction and return (slide 41).
3. **Teams, 3 minutes — the drift (slide 53).** Strathern's sentence on the panel. The cheapest route the model will find to make the number bigger, and what the person gets: *it will learn to ______, and the person will ______.* TAs help teams that say "nothing": what would a lazy intern paid per unit of that number do?
4. **Capture 2, 2 minutes (slide 54).** Short answer, scribe only: team number, then the drift. Now read pairs — the objective from 52, the drift from 54, same team number — five of them. The two lines together are the objective row of the mediation brief.
5. **Teams, 8 minutes — the "why am I seeing this" screen (slide 55).** One A4, landscape, big letters: the recommended item, drawn; three reasons in the person's words ("because you ___", "because people who ___", "because it is popular in ___"); the data each reason used, including one signal she did not know the product had; the controls (less like this, not this reason, the dial, start fresh). Page one of prototype v1. TAs: *in her words?* and *which data?*
6. **Capture 3, 3 minutes (slide 56).** Image upload, one per team, caption required: team number, then the first reason word for word. Put the wall on screen; read three captions without the picture and ask which kind of neighbour it is (the item's own numbers, or people like you). Show two screens: an honest data line, and a missing one.
7. **Teams, 2 minutes — the dial (slide 57).** How much of the feed is not the best guess: 0, 10, 30, 50 %. The cost of a wrong recommendation decides the number. The team writes it on its screen.
8. **The vote, 2 minutes (slide 58).** Everyone votes. No correct answer; show the split and ask one team at each end why. Teams whose wrong recommendation is cheap choose high; teams whose wrong recommendation hurts choose low.
9. **Debrief, 2 minutes (slide 59).** Every feed is an objective, an explanation and a dial; the model finds the neighbours. Verbeek: a feed designs what a person takes to be the world, in the background; the "why" screen is where it faces her. *The model finds the neighbours. You decided the objective, the explanation and the dial. That was the design.*

The four captures are the raw material of the mediation brief (slide 60): the objective and its drift, the explanation, the dial — next to the relation, the data, the bias and the guardrails from weeks 5, 8 and 9.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room with the two questions (what would you log; in her words), and note the two screens for the wall.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 5 | Short answer, one per team | Team number, and the guardrail your bias register names. | Recap of week 9; two columns get added to the register today (objective, explanation). |
| 9 | Word cloud | What does your feed think you are? | Warm-up: the room describes the model of itself. Screenshot for the debrief. |
| 19 | Multiple choice | Two songs are close in an embedding: what does that mean? | Quick check: B — their numbers are similar, by whatever the numbers measure. |
| 28 | Multiple choice | A brand-new user opens the app: which system has the least to say? | Quick check: B — collaborative filtering; her row is empty. |
| 38 | Multiple choice | Trained to maximise minutes spent: what will it learn to do? | Quick check: B — what keeps you watching, glad or not. |
| 52 | Short answer, one per team | Team number, and the objective your model optimises. | Capture 1: the number. Read against 54. |
| 54 | Short answer, one per team | Team number, and the wrong objective it could drift to. | Capture 2: Goodhart's law, twenty-five times, in their own products. |
| 56 | Image upload, one per team, caption required | The "why am I seeing this" screen | The wall; two screens discussed; page one of prototype v1. |
| 58 | Multiple choice | How much exploration should your feed have? | The vote: no correct answer; the split by the cost of a wrong recommendation. |

All nine buttons are generated by the build (caption required on 56).

## What to keep after class

- The slide-52 and slide-54 pairs (export): the objective row of each team's mediation brief, and the list of teams that wrote "none yet" — their product is a rule, and the brief should say so.
- The slide-56 screens (download): page one of prototype v1; Amber reads them against the uploads.
- The slide-9 word cloud and the slide-58 split, for the debrief in week 11 and the participation stars.
- The five axes each team got from the model in the workshop: the "missing axis" is a line for the bias register.
- Which teams had nothing to show at the stand-up: they get the first review slot after class.
