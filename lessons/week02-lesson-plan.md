# SD2112 · Week 2 lesson plan

**Rules that make things** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week02-classpoint.pptx` (66 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week02/` (html deck with the p5.js sketches running live; `SD2112-week02.pdf` next to it)

## Purpose of this session

For us:

1. Land **machine A** properly: what a rule is, what it buys you (exact, explainable) and what it costs (brittle, hand-written), with sixty years of symbolic AI in one chapter.
2. Show that art and design have been made from rules since before computers, and that in every case the design was the rule and the execution was delegated (Young, Brecht, Cage, Kaprow, LeWitt, Molnár, Nees, Nake).
3. Get every student to run a p5.js sketch, read it, and break it on purpose.
4. Teach **specs**: a rule written in words precisely enough for an executor — a drafter, a program, or a language model — and the discipline of fixing the spec, not the code.
5. Start Challenge 1 in class, so nobody goes home with a blank page.

For students, by the end of the class they can:

- define a rule-based system and give one design example of each of its three properties (exact, explainable, brittle);
- explain Schotter and Walk-Through-Raster as rules, and say where the random number enters each;
- read a p5.js sketch: find the loop, the random() calls and the constants; change one number; run it;
- write a five-part spec (rule, chance, numbers, constraints, output) and get working p5.js code from a language model on PolyU GenAI;
- say what "it did what you said, not what you meant" means, with an example from their own drawing.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week02-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 poll once as a test and reset it. Check the two Image Upload buttons (slides 59 and 63; 63 has *caption required*). Open `editor.p5js.org` in a browser tab and paste the twenty-line sketch from slide 42, ready for the live demo. |
| Amber | Blackboard: post the deck link, the PDF, the prompt template (slide 51, also on the site), the spec of the activity (slide 58) and the Challenge 1 brief (slide 65). Check that a language model on `genai.polyu.edu.hk` answers the filled template (slide 60) with runnable code; note which model you used and tell Gio. |
| WU Zhao, MA Jie | At the door: who has a laptop, who has a p5.js account. Make accounts on the spot (one minute at `editor.p5js.org`, any email). Seat phone-only students next to laptop owners; the workshop needs one laptop per pair. |
| Gio | Fonts on the classroom PC (`tools/fonts/`). The week-1 data: a screenshot of the slide-19 hopes and worries (for slide 5) and the cup wall (for slide 6). Backup: the html deck on a laptop — press `S` for notes; the sketches on slides 30, 31, 42, 44 and 52 run live there, which is the fallback if the p5 editor is slow. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Laptops out from the start. | | |
| 0:03 | 3–7 | Last week, in your words | Logistics poll; the five worries mapped to weeks (replace with the real ones); the cups; the semester map. | Multiple choice | The poll tells you how many pairs you can form; the TAs reseat people during slides 5–7. |
| 0:11 | 8–15 | Machine A | *Write a rule for drawing a house* (90 s, read four); if-then; Dartmouth, ELIZA, expert systems; the ELIZA transcript; exact/explainable/brittle; every designer writes rules; quick check. | Short answer; multiple choice | The house rules come back at the end: none of them was a complete spec. |
| 0:29 | 16–24 | Instructions as art | Young's one line; event scores; Tinguely (video, 1 min); Kaprow's Fluids (video, 1 min); LeWitt's sentence; Wall Drawing 118, the whole work; 118 executed by a script; Molnár by hand. | | Slides 22–23 are the core of the first half: read the 45 words aloud, then show the execution. Cut 19 if behind. |
| 0:47 | 25–33 | Rules make pictures | Bense and Nees 1965; Schotter as a rule; *where does chance enter?*; Walk-Through-Raster in four steps; the chain and the repertoire; the walk; the Illiac Suite; 10 PRINT. | Multiple choice | Slide 29 is the breakdown; 30–31 are the same rule as code — read them, do not type them yet. Cut 32 and 33 if behind. |
| 1:09 | 34–38 | Rules that grow | L-systems; parametric design (the week-1 chairs); variable fonts; *a rule is a design, execution can be delegated*. | | Cut 37 if behind. |
| 1:20 | 39 | **Break, 15 min** | Everyone logged into the p5 editor before leaving the room. | | |
| 1:35 | 40–47 | p5.js | Processing to p5.js; anatomy of a sketch; seeds; Schotter in twenty lines; change one number; **type it, run it** (6 min); *did it run?* | Multiple choice | Gio live in the editor for 42–45, then the room types. TAs walk during 46. Cs get a TA now; Ds pair. |
| 1:59 | 48–56 | Specs, and prompts for coding | One spec, three executors; anatomy of a spec; the template; what good looks like; what you said vs what you meant; what goes wrong; reading a rule you did not write; iterate like a designer. | | Slide 53 is the core of the second half. Cut 55 if behind. |
| 2:15 | 57–64 | **Activity: one spec, three executors** | Section (1 min); round 1 by hand (4); capture 1, everyone (3); round 2 in pairs (8); *did the code run?* (2); round 4 in fours (10); capture 2 and the wall (5); what just happened (2). | 2 × image upload; multiple choice | Nicolò keeps time; the other three TAs walk. Details below. |
| 2:50 | 65–66 | Challenge 1, homework | The brief; the sketch, the spec and a screenshot on Blackboard before week 3; AlphaGo and the four films. | | TAs stay 30 minutes. |
| 2:53 | | Buffer | | | |

If the p5 editor or GenAI is slow, give round 2 ten minutes and cut slides 32, 33 and 55. If the room is fast, let two fours read their spec aloud and have the room guess the picture before it is shown.

## The activity, in detail: One spec, three executors

The same words — Sol LeWitt's Wall Drawing 118 cut from fifty points to ten — executed three ways; then a rule of their own. **Each round ends in a picture; what goes into ClassPoint is an image, and the caption of the last one is the spec.** Pencil and paper for round 1; one laptop per pair with `editor.p5js.org` and a language model on `genai.polyu.edu.hk` for rounds 2 and 4.

1. **Alone, 4 minutes — execute it by hand (slide 58).** The spec is on the slide: *on a sheet of paper, using a pencil, place ten points at random; the points should be evenly distributed over the area of the sheet; all of the points should be connected by straight lines.* Execute it exactly, do not improve it, photograph it.
2. **Capture 1, 3 minutes — everyone uploads (slide 59).** The wall: the same words, a hundred drawings, none alike — orientation, pressure, what "random" meant, whether "evenly" won. Pick two and ask which followed the spec better; the room disagrees, which is the answer. This is LeWitt's point and the whole lecture in one screen.
3. **Pairs, 8 minutes — let the machine execute it (slide 60).** The filled template is on the slide (rule = the spec; chance = the positions; numbers = 600 × 600, black, 1 px; constraints; output). Ask a language model, paste the code into the editor, run it; if it fails, paste the error back word for word. Then compare with the two hand drawings: **what did the machine decide that you decided differently?** Expect all four failure modes from slide 54, and the random-versus-evenly decision made silently.
4. **Pulse (slide 61).** *Did the model's code run?* First time / after one error pasted back / after rewriting the spec / not yet. Ask two pairs what the machine decided differently.
5. **Fours, 10 minutes — write your own spec (slide 62).** One rule, one random number, in the template, in words a stranger could execute; the words are the deliverable. Run it through the model, run the code, look; fix the spec, not the code, until the picture is the one they meant. Push for precision on the chance: "a random amount" is not a spec, "up to 20 px" is.
6. **Capture 2, 5 minutes — scribes only, caption = the spec (slide 63).** One image per four, caption required. Put the wall on screen; read two captions aloud and have the room guess the picture before it is shown. Where the guess fails, the spec failed. Download the submissions: the specs come back in week 4 as the first briefs.
7. **Debrief, 2 minutes (slide 64).** The hand: a spec is never complete, the executor finishes it. The model: it did what you said, not what you meant. The computer: exact, repeatable with a seed, readable. *The machine drew every line. You wrote the rule. That was the design.*

Round 4 is the start of Challenge 1 (slide 65): a picture from rules, one rule and one random number, the spec plus the editor share link plus a screenshot on Blackboard before week 3; the model is allowed and must be named; the room votes in week 3.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room, help paste errors back, and note the best specs for the week-3 awards.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Multiple choice | What do you have with you? | Pairs for the workshop; who needs an account now. |
| 9 | Short answer | Write a rule for drawing a house. | Read four: none is a complete spec. Comes back in the debrief and in week 4 (briefs). |
| 15 | Multiple choice | Which of these is machine A? | Quick check: B. |
| 28 | Multiple choice | Where does chance enter in Schotter? | Quick check: B. The question to ask of every generative piece. |
| 47 | Multiple choice | Did it run? | Pulse after the live typing; Cs get a TA, Ds pair. |
| 59 | Image upload, everyone | Your hand-drawn execution of the spec | The wall: one spec, a hundred drawings. Screenshot it. |
| 61 | Multiple choice | Did the model's code run? | Pulse on execution; usually most run first time. |
| 63 | Image upload, one per four, caption required | The picture, and the spec that made it | Spec–picture pairs for week 4 (briefs) and for the Challenge 1 awards in week 3. |

All eight buttons are generated by the build (caption required on 63).

## What to keep after class

- The slide-9 house rules and the slide-63 specs: week 4 opens with them as briefs.
- The two walls (59 and 63) as screenshots, for the week-3 recap and the awards.
- Which language model on GenAI produced runnable p5.js most reliably: it goes in the week-4 plan.
