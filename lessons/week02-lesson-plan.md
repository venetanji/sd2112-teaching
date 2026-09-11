# SD2112 · Week 2 lesson plan

**Rules that make things** · three-hour lecture-workshop (about 170 minutes of content plus a 10-minute break) · deck: `week02-classpoint.pptx` (70 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week02/` (the html deck: the p5.js sketches run live, the code slides are editable, `SD2112-week02.pdf` next to it)

## Purpose of this session

For us:

1. Land **machine A** properly: what a rule is, what it buys you (exact, explainable) and what it costs (brittle, hand-written), with sixty years of symbolic AI in one chapter.
2. Show that art and design have been made from rules since before computers, and that in every case the design was the rule and the execution was delegated (Young, Brecht, Cage, Kaprow, LeWitt, Molnár, Nees, Nake).
3. Explain two rules step by step, with the picture drawing itself: Schotter (row by row, two sliders) and Walk-Through-Raster (four states of a cell, the cell above decides, the empty space flows), then the code of each. Bring back the fractal part of the 2025 deck: Koch's curve, a rule that calls itself, and the Mandelbrot zoom, the same rule at every scale, with a sketch that zooms in on a click.
4. Get every student to change a number in a p5.js sketch and see the picture change, without leaving the slides.
5. Teach **specs**: a rule written in words precisely enough for an executor — a drafter, a program, or a language model — and the discipline of fixing the spec, not the code.
6. Run the one exercise: a language model executes LeWitt's spec with a twist of the pair's own, then each pair writes a rule and a spec entirely their own and iterates. Start Challenge 1 in class, so nobody goes home with a blank page.

For students, by the end of the class they can:

- define a rule-based system and give one design example of each of its three properties (exact, explainable, brittle);
- explain Schotter and Walk-Through-Raster as rules, and say where the random number enters each;
- read a p5.js sketch: find the loop, the random() calls and the constants; change one number; run it;
- write a five-part spec (rule, chance, numbers, constraints, output), get working p5.js code from a language model on PolyU GenAI, and iterate on the spec rather than the code;
- say what "it did what you said, not what you meant" means, with an example from their own sketch.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week02-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 poll once as a test and reset it. Check the Image Upload button on slide 67 (*caption required*). Open the html deck in a browser tab as well: slides 14, 31, 32, 35, 36, 40, 42, 50, 52, 58 and 65 run live there, and that is what the room sees for the sketches. |
| Amber | Blackboard: post the deck link, the PDF, the prompt template (slide 57, also on the site), the spec of the exercise (slide 64), the twists (slide 66) and the Challenge 1 brief (slide 69). Check that a language model on `genai.polyu.edu.hk` answers the filled template (slide 64) with code that runs on the sketch slide (65); note which model you used and tell Gio. |
| WU Zhao, MA Jie | At the door: who has a laptop. Nothing to install and no account: the sketches and the exercise run inside the html deck, in the browser. Seat phone-only students next to laptop owners; the exercise needs one laptop per pair, and the editable slides need one to try things on. |
| Gio | Fonts on the classroom PC (Inter and JetBrains Mono ship inside the deckgen package; README, *Classroom checklist*). The week-1 links: slide 6 links to the cup wall and slide 7 shows it; slide 5 links to the hopes-and-worries answers only once `deck/week01-reports.json` carries that activity's id (it is withheld while ClassPoint's public page still carries names — decide before class). Backup: the html deck on a laptop — press `S` for notes; the sketches run there, which is the fallback if the p5 editor is slow. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Laptops out from the start. | | |
| 0:03 | 3–8 | Last week, in your words | Logistics poll; the five worries mapped to weeks (read three real ones from the link); the cups; the wall of all 147 uploads; the semester map. | Multiple choice | The poll tells you how many pairs you can form; the TAs reseat people during slides 5–8. |
| 0:12 | 9–17 | Machine A | If-then; Kant's analytic and synthetic (run the five sentences with the room; 2 + 2 = 4 is the trap); Turing's imitation game; Dartmouth, ELIZA, expert systems; ELIZA live (Weizenbaum's whole 1966 script; three of its rules on the left, a chat on the right; add a rule); exact/explainable/brittle; every designer writes rules; then *write a rule for drawing a house* (90 s, read four). | Short answer | The house rules come back in the exercise: none of them was a complete spec. |
| 0:32 | 18–28 | Instructions as art | Young's one line; event scores; Tinguely (video, 1 min); Kaprow (video, 1 min); LeWitt's sentence; two of his walls, drawn by others from the rule (Barcelona 2001, Metz 2012); Wall Drawing 118, the whole work; 118 executed by a script; Molnár by hand. | | Slides 26–27 are the core of the first half: read the 45 words aloud, then show the execution. Cut 21 if behind. |
| 0:52 | 29–37 | Rules make pictures | Bense and Nees 1965; **Schotter drawing itself, row by row** (two sliders: disorder, rows); **10 PRINT** (two states, one coin toss per cell, no memory; the heads slider); Nake's print — look first; the rule in four steps (four states; a cap only under an empty cell, never in the top row; the flow); **watch the walk** (the raster filling column by column, the empty cells tinted, the counts; the cap-chance slider); the rule in twenty lines, editable; the Illiac Suite. | | The progression is 31 → 32 → 35: one number, then two states with no memory, then four states with one thing remembered. Let each sketch run once, then move the slider and say what changed. Slide 36 is read, not typed. Cut 37 if behind. |
| 1:14 | 38–47 | Rules that grow | Koch's curve (the fractal, five generations); Koch in p5.js (a rule that calls itself, plays on its own); **the Mandelbrot zoom** (the 2025 gif, back: let it run); **Mandelbrot in p5.js** (one rule per pixel; click to zoom in; the steps slider); L-systems; parametric design (the week-1 chairs; the sliders were parameters); variable fonts; *a rule is a design, execution can be delegated*. | | Cut 45 if behind. |
| 1:26 | 47 | **Break, 10 min** | Everyone with the html deck open on their laptop before leaving the room. | | |
| 1:36 | 48–53 | p5.js | Processing to p5.js; **anatomy** (on your laptop: 10 → 30, Run; one 600 → 200, Run: six minutes, the TAs walk); seeds; **Schotter in twenty lines** (rows 22 → 8, PI / 4 → PI, square → circle); change one number. | | The code on slides 50, 52 and 58 is editable in the html deck: Run re-runs the sketch beside it, Reset brings the slide's code back. Nobody types the sketches in, and nobody leaves the deck; they change them. |
| 1:56 | 54–62 | Specs, and prompts for coding | One spec, three executors; anatomy of a spec; the template; what good looks like (LeWitt in 22 lines — and why it needs a twist); what you said vs what you meant; what goes wrong; reading a rule you did not write; iterate like a designer. | | Slide 59 is the core of the second half. Cut 61 if behind. |
| 2:16 | 63–68 | **Exercise: one spec, one twist** | Section (1 min); step 1, LeWitt plus a twist of the pair's own through a model (10), the code pasted into the sketch slide (65); step 2, a rule and a spec entirely their own, iterated on the same slide (12); capture, one per pair (5); what just happened (2). | Image upload, one per pair, caption required | Nicolò keeps time; the other three TAs walk. Details below. |
| 2:44 | 69–70 | Challenge 1, homework | The brief; the spec, the code and a screenshot on Blackboard before week 3; AlphaGo and the four films. | | TAs stay 30 minutes. |
| 2:42 | | Buffer | | | |

If GenAI is slow, give step 2 fifteen minutes and cut slides 37 and 61. If the room is fast, let two pairs read their spec aloud and have the room guess the picture before it is shown.

## The exercise, in detail: One spec, one twist

First the same words for everyone — Sol LeWitt's Wall Drawing 118 cut from fifty points to ten — plus one twist of the pair's own, executed by a language model, as with last week's cups. Then a rule and a spec entirely the pair's own, iterated until the picture is the one they meant. **The exercise ends in a picture; what goes into ClassPoint is one image per pair, the pair's own rule, and its caption is the spec.** One laptop per pair, with the html deck (the code runs on the sketch slide, 59) and a language model on `genai.polyu.edu.hk`.

1. **Step 1, pairs, 10 minutes — LeWitt, with a twist (slides 64–65).** The spec is on the slide with a list of twists (points on a circle; lines as thick as they are long; curves bent by chance; thirty points, nearest neighbours only; lines coloured by angle); each pair adds one, its own or from the list, and asks the model. Paste the code into the editor on the sketch slide, press Run; if it fails, the error shows under the box: paste it back word for word. Then read the code: **what did the machine decide that the words left open?** Expect all four failure modes from slide 60, and the random-versus-evenly decision made silently.
2. **Step 2, pairs, 12 minutes — your own rule (slide 66, back on 65 to run).** The blank template: one rule and one random number of the pair's own, not Schotter and not LeWitt, in words a stranger could execute. Ask the model, run, look, and fix the spec, not the code, until the picture is what they meant. Push for precision on the chance: "a random amount" is not a spec, "up to 20 px" is. One change per prompt; v1, v2, v3.
3. **Capture, 5 minutes — one per pair, caption = the spec (slide 67).** The pair's own rule, caption required. Put the wall on screen: fifty-five rules, no two pictures alike. Read two captions aloud and have the room guess the picture before it is shown. Where the guess fails, the spec failed. Download the submissions: the specs come back in week 4 as the first briefs.
4. **Debrief, 2 minutes (slide 68).** The model: it did what you said, not what you meant. The code: exact, repeatable with a seed, readable. The twist, then the own rule: one sentence changed the wall, and then the wall was theirs. *The machine drew every line. You wrote the rule. That was the design.*

The own rule is the start of Challenge 1 (slide 69): a picture from rules, one rule and one random number, the spec plus the code as a text file plus a screenshot on Blackboard before week 3; the model is allowed and must be named; the room votes in week 3.

TA roles: Nicolò keeps time with the slide timers and calls the step changes; Amber, WU Zhao and MA Jie walk the room, help paste errors back, and note the best rules for the week-3 awards.

## The editable slides

In the html deck, the code panel of slides 14, 32, 36, 40, 42, 50, 52, 58 and 65 is an editor (on 14 the sketch is ELIZA's chat): **Run** (or ctrl+enter) re-runs the sketch beside it with whatever is in the box, **Reset** brings the slide's code back, and what a student typed survives a reload. Sliders under a sketch are the rule's numbers (disorder, rows, heads, cap chance, times, steps); a click on a sketch throws new dice, or zooms in on the Mandelbrot set. Slide 65 is the exercise's workbench: the model's code is pasted there and run there. The PowerPoint and the PDF show the code and a still, and their captions link to the slide in the html deck. Nobody is sent to the p5 web editor; the same code runs there later if a student wants it.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Multiple choice | What do you have with you? | Pairs for the exercise. |
| 17 | Short answer | Write a rule for drawing a house. | Read four: none is a complete spec. Comes back in the exercise and in week 4 (briefs). |
| 67 | Image upload, one per pair, caption required | The picture, and the spec that made it | Spec–picture pairs for week 4 (briefs) and for the Challenge 1 awards in week 3. |

All three buttons are generated by the build (caption required on 67). Slides 5 and 6 link to the week-1 answers (the hopes and worries; the cup wall) through `deck/week01-reports.json`; slide 7 is the wall itself, made by `tools/classpoint/collage.py` from the two upload activities (images only, no names).

## What to keep after class

- The slide-17 house rules and the slide-67 specs: week 4 opens with them as briefs.
- The wall (61) as a screenshot, for the week-3 recap and the awards.
- Which language model on GenAI produced runnable p5.js most reliably: it goes in the week-4 plan.
