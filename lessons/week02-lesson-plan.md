# SD2112 · Week 2 lesson plan

**Rules that make things** · three-hour lecture-workshop (about 170 minutes of content plus a 10-minute break) · deck: `week02-classpoint.pptx` (63 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week02/` (the html deck: the p5.js sketches run live, the code slides are editable, `SD2112-week02.pdf` next to it)

## Purpose of this session

For us:

1. Land **machine A** properly: what a rule is, what it buys you (exact, explainable) and what it costs (brittle, hand-written), with sixty years of symbolic AI in one chapter.
2. Show that art and design have been made from rules since before computers, and that in every case the design was the rule and the execution was delegated (Young, Brecht, Cage, Kaprow, LeWitt, Molnár, Nees, Nake).
3. Explain two rules step by step, with the picture drawing itself: Schotter (row by row, two sliders) and Walk-Through-Raster (four states of a cell, the cell above decides, the empty space flows), then the code of each. Bring back the fractal part of the 2025 deck: Koch's curve, a rule that calls itself.
4. Get every student to change a number in a p5.js sketch and see the picture change, without leaving the slides.
5. Teach **specs**: a rule written in words precisely enough for an executor — a drafter, a program, or a language model — and the discipline of fixing the spec, not the code.
6. Run the one exercise: a language model executes LeWitt's spec, then each pair twists it and iterates. Start Challenge 1 in class, so nobody goes home with a blank page.

For students, by the end of the class they can:

- define a rule-based system and give one design example of each of its three properties (exact, explainable, brittle);
- explain Schotter and Walk-Through-Raster as rules, and say where the random number enters each;
- read a p5.js sketch: find the loop, the random() calls and the constants; change one number; run it;
- write a five-part spec (rule, chance, numbers, constraints, output), get working p5.js code from a language model on PolyU GenAI, and iterate on the spec rather than the code;
- say what "it did what you said, not what you meant" means, with an example from their own sketch.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week02-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 poll once as a test and reset it. Check the Image Upload button on slide 60 (*caption required*). Open the html deck in a browser tab as well: slides 26, 27, 30, 31, 35, 43, 45, 51 and 58 run live there, and that is what the room sees for the sketches. |
| Amber | Blackboard: post the deck link, the PDF, the prompt template (slide 50, also on the site), the spec of the exercise (slide 57), the twists (slide 59) and the Challenge 1 brief (slide 62). Check that a language model on `genai.polyu.edu.hk` answers the filled template (slide 57) with code that runs on the sketch slide (58); note which model you used and tell Gio. |
| WU Zhao, MA Jie | At the door: who has a laptop. Nothing to install and no account: the sketches and the exercise run inside the html deck, in the browser. Seat phone-only students next to laptop owners; the exercise needs one laptop per pair, and the editable slides need one to try things on. |
| Gio | Fonts on the classroom PC (Inter and JetBrains Mono ship inside the deckgen package; README, *Classroom checklist*). The week-1 links: slide 6 links to the cup wall; slide 5 links to the hopes-and-worries answers only once `deck/week01-reports.json` carries that activity's id (it is withheld while ClassPoint's public page still carries names — decide before class). Backup: the html deck on a laptop — press `S` for notes; the sketches run there, which is the fallback if the p5 editor is slow. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Laptops out from the start. | | |
| 0:03 | 3–7 | Last week, in your words | Logistics poll; the five worries mapped to weeks (read three real ones from the link); the cups, with the wall; the semester map. | Multiple choice | The poll tells you how many pairs you can form; the TAs reseat people during slides 5–7. |
| 0:11 | 8–14 | Machine A | If-then; Dartmouth, ELIZA, expert systems; the ELIZA transcript; exact/explainable/brittle; every designer writes rules; then *write a rule for drawing a house* (90 s, read four). | Short answer | The house rules come back in the exercise: none of them was a complete spec. |
| 0:29 | 15–23 | Instructions as art | Young's one line; event scores; Tinguely (video, 1 min); Kaprow (video, 1 min); LeWitt's sentence; Wall Drawing 118, the whole work; 118 executed by a script; Molnár by hand. | | Slides 21–22 are the core of the first half: read the 45 words aloud, then show the execution. Cut 18 if behind. |
| 0:47 | 24–32 | Rules make pictures | Bense and Nees 1965; **Schotter drawing itself, row by row** (two sliders: disorder, rows); **10 PRINT** (two states, one coin toss per cell, no memory; the heads slider); Nake's print — look first; the rule in four steps (four states; a cap only under an empty cell; the flow); **watch the walk** (the raster filling column by column, the empty cells tinted, the counts; the cap-chance slider); the rule in twenty lines, editable; the Illiac Suite. | | The progression is 26 → 27 → 30: one number, then two states with no memory, then four states with one thing remembered. Let each sketch run once, then move the slider and say what changed. Slide 31 is read, not typed. Cut 32 if behind. |
| 1:09 | 33–40 | Rules that grow | Koch's curve (the fractal, five generations); Koch in p5.js (a rule that calls itself, plays on its own); L-systems; parametric design (the week-1 chairs; the sliders were parameters); variable fonts; *a rule is a design, execution can be delegated*. | | Cut 38 if behind. |
| 1:20 | 40 | **Break, 10 min** | Everyone with the html deck open on their laptop before leaving the room. | | |
| 1:30 | 41–46 | p5.js | Processing to p5.js; **anatomy** (on your laptop: 10 → 30, Run; one 600 → 200, Run: six minutes, the TAs walk); seeds; **Schotter in twenty lines** (rows 22 → 8, PI / 4 → PI, square → circle); change one number. | | The code on slides 43, 45 and 51 is editable in the html deck: Run re-runs the sketch beside it, Reset brings the slide's code back. Nobody types the sketches in, and nobody leaves the deck; they change them. |
| 1:50 | 47–55 | Specs, and prompts for coding | One spec, three executors; anatomy of a spec; the template; what good looks like (LeWitt in 22 lines — and why it is boring); what you said vs what you meant; what goes wrong; reading a rule you did not write; iterate like a designer. | | Slide 52 is the core of the second half. Cut 54 if behind. |
| 2:10 | 56–61 | **Exercise: one spec, one twist** | Section (1 min); step 1, the spec through a model, in pairs (8), the code pasted into the sketch slide (58); step 2, the twist, iterated on the same slide (12); capture, one per pair (5); what just happened (2). | Image upload, one per pair, caption required | Nicolò keeps time; the other three TAs walk. Details below. |
| 2:38 | 62–63 | Challenge 1, homework | The brief; the spec, the code and a screenshot on Blackboard before week 3; AlphaGo and the four films. | | TAs stay 30 minutes. |
| 2:42 | | Buffer | | | |

If GenAI is slow, give step 2 fifteen minutes and cut slides 32 and 54. If the room is fast, let two pairs read their spec aloud and have the room guess the picture before it is shown.

## The exercise, in detail: One spec, one twist

The same words — Sol LeWitt's Wall Drawing 118 cut from fifty points to ten — executed by a language model, then changed by one sentence of the pair's own, and iterated until the picture is the one they meant. **The exercise ends in a picture; what goes into ClassPoint is one image per pair, and its caption is the spec, twist included.** One laptop per pair, with the html deck (the code runs on the sketch slide, 58) and a language model on `genai.polyu.edu.hk`.

1. **Step 1, pairs, 8 minutes — let the machine execute it (slides 57–58).** The filled template is on the slide (rule = the spec; chance = the positions; numbers = 600 × 600, black, 1 px; constraints; output). Ask the model, paste the code into the editor on the sketch slide, press Run; if it fails, the error shows under the box: paste it back word for word. Then read the code: **what did the machine decide that the words left open?** Expect all four failure modes from slide 53, and the random-versus-evenly decision made silently.
2. **Step 2, pairs, 12 minutes — the twist (slide 59, back on 58 to run).** LeWitt executed exactly is a boring picture, and every pair has the same one. Each pair adds one twist to the rule — from the list on the slide (points on a circle; lines as thick as they are long; curves bent by chance; thirty points, nearest neighbours only; lines coloured by angle; the drawing repeated smaller in a corner) or their own — written as a sentence a stranger could execute, then asks the model again, runs, looks, and fixes the spec, not the code, until the picture is what they meant. Push for precision on the chance: "a random amount" is not a spec, "up to 20 px" is. One change per prompt; v1, v2, v3.
3. **Capture, 5 minutes — one per pair, caption = the spec (slide 60).** Caption required. Put the wall on screen: the same forty-five words plus one sentence each, and no two pictures alike. Read two captions aloud and have the room guess the picture before it is shown. Where the guess fails, the spec failed. Download the submissions: the specs come back in week 4 as the first briefs.
4. **Debrief, 2 minutes (slide 61).** The model: it did what you said, not what you meant. The code: exact, repeatable with a seed, readable. The twist: one sentence changed the whole wall. *The machine drew every line. You wrote the rule. That was the design.*

The twist is the start of Challenge 1 (slide 62): a picture from rules, one rule and one random number, the spec plus the code as a text file plus a screenshot on Blackboard before week 3; the model is allowed and must be named; the room votes in week 3.

TA roles: Nicolò keeps time with the slide timers and calls the step changes; Amber, WU Zhao and MA Jie walk the room, help paste errors back, and note the best twists for the week-3 awards.

## The editable slides

In the html deck, the code panel of slides 27, 31, 35, 43, 45, 51 and 58 is an editor: **Run** (or ctrl+enter) re-runs the sketch beside it with whatever is in the box, **Reset** brings the slide's code back, and what a student typed survives a reload. Sliders under a sketch are the rule's numbers (disorder, rows, heads, cap chance, times); a click on a sketch throws new dice. Slide 58 is the exercise's workbench: the model's code is pasted there and run there. The PowerPoint and the PDF show the code and a still, and their captions link to the slide in the html deck. Nobody is sent to the p5 web editor; the same code runs there later if a student wants it.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Multiple choice | What do you have with you? | Pairs for the exercise. |
| 14 | Short answer | Write a rule for drawing a house. | Read four: none is a complete spec. Comes back in the exercise and in week 4 (briefs). |
| 60 | Image upload, one per pair, caption required | The picture, and the spec that made it | Spec–picture pairs for week 4 (briefs) and for the Challenge 1 awards in week 3. |

All three buttons are generated by the build (caption required on 60). Slides 5 and 6 link to the week-1 answers (the hopes and worries; the cup wall) through `deck/week01-reports.json`.

## What to keep after class

- The slide-14 house rules and the slide-60 specs: week 4 opens with them as briefs.
- The wall (60) as a screenshot, for the week-3 recap and the awards.
- Which language model on GenAI produced runnable p5.js most reliably: it goes in the week-4 plan.
