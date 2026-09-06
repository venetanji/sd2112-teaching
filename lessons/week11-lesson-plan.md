# SD2112 · Week 11 lesson plan

**Curators of outputs and datasets** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week11-classpoint.pptx` (56 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week11/` (html deck with the two p5.js sketches running live; `SD2112-week11.pdf` next to it)

## Purpose of this session

For us:

1. Open module 4 — the designer's turn — with the portrait from week 1: Edmond de Belamy, its six hands (the painters, WikiArt, Goodfellow, Barrat, Obvious, Christie's) and the one act that happened once: somebody chose Edmond out of eleven. The room votes on the author before and after the story.
2. Make **curating outputs** a craft, not an instinct: generate wide, discard fast, say why, answer for it — with the live curate sketch (sixty-four tiles from one rule, three chosen, a written reason each) and the funnel 64 → 12 → 3 → 1. Gatekeeping is the second half of the job: the likeness, the style, the harm, the wrong one.
3. Make **curating datasets** concrete: a LoRA learns what its images agree on and leaves free what they do not (the mean tile and the spread bars, live); twenty to fifty images, one thing in common, everything else varied, captioned; LAION-5B as the dataset nobody curated; four sources on a scale of consent.
4. Give a designer's map of **authorship and ownership in 2026**, one card and one sentence per ruling: the output side (Thaler, Zarya, the Copyright Office's Part 2 report, Allen; Hong Kong's s.11(3)) and the training side (Google Books, Bartz v. Anthropic, Kadrey v. Meta, Getty v. Stability); the ladder from prompt to make; what "transformative" means for a poster; the process note as the instrument that answers all of it.
5. Start the **poster lab**: the A0's four zones and where the marks sit, the video in six shots, the one-page mediation brief, the critique protocol — and run the activity in three rounds so that every team leaves with three written reasons, a twelve-image dataset sheet, and one fix on its draft poster. Draft poster and brief are due tonight.

For students, by the end of the class they can:

- tell the Belamy story with its six hands and say which one the market paid, which one the law would recognise, and which one they would put their own name in;
- run the four moves of a curator on a batch — generate wide, discard fast, say why (a noun, not an adjective), answer for it — and name the four gates that keep an output from shipping;
- explain what a fine-tuning dataset teaches (the agreement) and what it leaves free (the spread), build a twelve-image dataset of a style they own and write "what this teaches" in one sentence, and say which of four image sources need nobody's consent;
- place any AI-assisted piece of their own on the authorship ladder (prompt, pick, arrange, modify, make) and state the 2025 US position on each rung; say the Google Books test in one line (new purpose, not a substitute) and the two questions to ask before anything ships;
- name the four zones of the A0 and the rubric weight on each, storyboard a video in six shots with the decision in the middle, and write the five headings of the mediation brief.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week11-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 word cloud once as a test and reset it. Check the two Image Upload buttons (slides 50 and 52; both *caption required*) and the short answer on 48. Open the html deck in a second browser tab: the curate sketch (slides 16 and 47) and the dataset sketch (24) run only there; click inside the curate sketch and press N to check a fresh batch appears, click three tiles, then on 24 click two odd candidates in (the bars turn orange) and out again (teal). Post the standalone sketch page `week11/sketches/w11-curate.html` (the ↗ in the LIVE chip) on Blackboard so teams can open it on their own laptops. Keep the slide timers ready for rounds 1–3 (47, 49, 51). |
| Amber | Blackboard: post the deck link, the PDF, the dataset sheet (slide 49) and the mediation-brief template (slide 44) as text, the critique protocol (45), and the due list (54) with tonight's deadline and the mock-session deadline confirmed with Gio. From the week-10 prototypes pick two anonymised screenshots per card for slide 5 (team numbers only, no names): one where the decision is a label, one where the "no" exists. Bring the week-10 `week10/sketches` link in case a team wants its similarity search back for the poster. After class: export the slide-48 answers, download the slide-50 sheets and the slide-52 drafts; read every draft brief before week 12. |
| WU Zhao, MA Jie | At the door with the team list: seat every student with their team from the start. Every team needs one laptop with the draft poster open (or the week-9 concept board if the draft does not exist yet), one phone with thirty of their own images reachable (a camera roll is fine), sticky notes and pens on the table before slide 46. During round 1 walk with one question: *which part?* (for "nice", "clean", "modern"). During round 2: *what do the twelve agree on?* During round 3 enforce the protocol: no explaining while the other team reads the poster. |
| Gio | Fonts on the classroom PC (`tools/fonts/`). The week-10 screenshots (the slide-9 word cloud, the slide-58 exploration split) for the recap if you want them. Backup: the html deck on a laptop — press `S` for notes; the sketches on 16, 24 and 47 run live there. Before class press N on slide 16 a few times and pick three tiles you can defend out loud, so the live demo is not improvised. Check two things that may have moved since the deck was written and update the card if so: the Allen docket (slide 33: a ruling was expected in 2026) and the IPD page on the text-and-data-mining bill (slide 35). The Belamy numbers on slides 9 and 11 follow Christie's: hammered at $350,000, $432,500 with the premium; 15,000 portraits from the 14th to the 20th century; Le Comte de Belamy sold privately for €10,000 in February 2018. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Module 4 opens. Teams sit together; the draft poster on a laptop at every table. | | |
| 0:03 | 3–6 | Last week, in your words | *Edmond de Belamy: who made it? One word* (4); three things we saw in prototype v1 (5: the screen, the decision, the no — replace with the real ones); the semester map (6). | Word cloud | Screenshot the cloud: the same question comes back as a vote on 12. If the cloud is thin, nobody watched the clip: play it on 10 (34 seconds). |
| 0:13 | 7–13 | Who made Belamy? | The portrait, with the question turned round (8); four facts (9: the sale, one of eleven, the signature, the code); the makers' clip (10, 34 seconds, if needed); six hands (11, figure); *who is the author?* (12); *the machine painted all eleven; somebody chose Edmond* (13). | Multiple choice | 11 is the core of the first half: walk the boxes, then ask which one they would sign. No correct answer on 12; screenshot the split next to the cloud. Cut 10 if the cloud was full. |
| 0:28 | 14–21 | Curators of outputs | *The model makes 64. You pick one* (15); **live: curate** (16 — pick three out loud, saying why, then press N and do it again); the funnel (17, figure); weeks 1, 3 and 5 revisited (18); four moves (19); gatekeeping (20); *sixty-four logos in a minute: where is the design?* (21). | Multiple choice | On 16 the room calls out numbers; the reasons you give are the model for round 1. Cut 18 to one sentence if behind. Never cut 19 or 20. |
| 0:52 | 22–29 | Curators of datasets | A style is twenty images (23, figure: two datasets, the mean, the spread); **live: the dataset** (24 — add three odd ones, watch the bars go orange, take them out); how to build one (25); LAION-5B (26); whose images (27); *which of these can you fine-tune on without asking?* (28); *choose the examples and you have chosen the prototype* (29). | Multiple choice | 23 and 24 are the mechanism of the week: the bars are the design decision. 26 can be cut to its first bullet if behind; 27 cannot — it is the rule for round 2. |
| 1:20 | 30 | **Break, 15 min** | Teams come back with the draft poster open and thirty of their own images reachable. | | |
| 1:35 | 31–39 | Whose is it? | *No human author, no copyright* (32: Thaler, 18 March 2025; cert. denied 2 March 2026); the output side (33: Thaler, Zarya, the Office's Part 2 report, Allen); the ladder (34, figure); Hong Kong's s.11(3) and the 2024 consultation (35); the training side (36: Google Books, Anthropic, Meta, Getty); transformative, for a designer (37); the process note (38); *a 400-word prompt, one image, shipped untouched: who holds the copyright?* (39). | Multiple choice | One sentence per card; this is a map, not a law class. 34 is the core of the second half: walk the rungs with the room's own work. Cut 35 to one sentence if behind. |
| 2:03 | 40–45 | The poster lab | The A0 and where the marks sit (41, figure); the four zones (42); the video in six shots (43, figure); the mediation brief, one page, due tonight (44); the critique protocol (45). | | Read 42 and 45 as instructions: they are the brief for rounds 2 and 3. |
| 2:15 | 46–53 | **Activity: curate, assemble, critique** | Section (1 min); round 1, curate three of sixty-four (6); capture 1, short answer (3); round 2, the twelve-image dataset sheet (10); capture 2, image upload (3); round 3, swap draft posters, one fix (8); capture 3, image upload (3); what just happened (2). 36 minutes in all, as the section slide says. | Short answer; 2 × image upload | Nicolò keeps time; the other three TAs walk. Details below. |
| 2:51 | 54–56 | Homework | Due tonight and next week (54); IBM's chatbots video (55, 7:25, the last one in course order); *see you next week: language as an interface* (56). | | TAs stay 30 minutes and read any brief brought to them. |
| 2:54 | | Buffer | | | |

If the room is slow, give round 2 twelve minutes and cut 10, 18 and 35. If the room is fast, let two teams read their three reasons aloud on 48 and put their tiles on screen from the html deck, and give round 3 ten minutes.

## The activity, in detail: Curate. Assemble. Critique.

Team-based, at the team table; three rounds, each ending in ClassPoint. **What goes into ClassPoint is one line of text per team (three tile numbers with a reason each, and the one that ships), a photo of the twelve-image dataset sheet (caption = "what this teaches"), and a photo of the draft poster (caption = the one fix the other team gave).** One laptop per team with the curate sketch (the course site, week 11, the LIVE chip's ↗ opens it on its own) and the draft poster; one phone per team for the images and the uploads; sticky notes.

1. **Teams, 6 minutes — curate (slide 47).** The curate sketch runs on the slide and on the team's laptop. Press N once: your own sixty-four. As a team, choose three; for each, one line, a noun, not an adjective ("#27: the only one with a rhythm", "#3: survives at stamp size"). Then the hard one: which of the three ships, and why it beat the other two. Teams that cannot agree are doing it right; make them write the disagreement down. TAs: *which part?*
2. **Capture 1, 3 minutes (slide 48).** Short answer, scribe only: three tile numbers with a reason each, and the one that ships, in one line. Read four aloud and put the tiles on screen from the html deck if it is up: three teams, three different picks from the same rule, three legible reasons. That is authorship, written down.
3. **Teams, 10 minutes — the dataset (slide 49).** A style the team owns: their sketches, their photos, the week-8 drawings; nothing scraped, nothing from an illustrator they admire. Twelve that agree on one thing and vary in the rest, laid out with the sheet: numbered, one line under each. Then "what this teaches" — three things the model would learn — and one thing they left out, and why. The stall is always the same: twelve things they like and no sentence about what the twelve agree on; send them back to the bars on slide 24. TAs: *what do the twelve agree on?*
4. **Capture 2, 3 minutes (slide 50).** Image upload, one per team, caption required: the sheet, twelve images numbered; caption "what this teaches" in one sentence. Put the wall on screen and read three captions before showing the sheets: can the room guess what the twelve look like from the sentence? Where the guess works, the dataset is an agreement; where it fails, it is a pile.
5. **Pairs of teams, 8 minutes — critique (slide 51).** Swap laptops with the next team; their draft poster, your eyes, no explaining. Three metres: say the product in one sentence from the poster alone. One metre: point at the decision — the data, the line, the fallback, the no. Write one fix on a sticky note, one sentence; give it back. Read yours; do not argue; write it down. Teams without a draft yet critique the poster anatomy on slide 41 against their concept board and write the fix for themselves.
6. **Capture 3, 3 minutes (slide 52).** Image upload, one per team, caption required: the draft poster as it is today, caption = the fix, word for word. Put the wall on screen and read four fixes without showing which poster: they are usually the same four sentences — draw the decision, say who it is for, where is the no, the title is the company not the product. That list is tonight's checklist.
7. **Debrief, 2 minutes (slide 53).** Curate: the rule could not rank the tiles; you could, and the law protects exactly that much. Assemble: what you put in is what comes out — whose images, and did they agree. Critique: the gate works better from outside the team. *The machine made every one. You chose which, and from what. That was the design.*

The three captures are the raw material of the process note (slide 38) and the baseline for next week's mock session (slide 54): the reasons, the dataset sheet and the fixed draft go into the shared folder every team keeps from tonight.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room with the two questions (which part; what do the twelve agree on), enforce no defending in round 3, and note the two sheets and the two fixes worth showing.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Word cloud | Edmond de Belamy: who made it? One word. | Warm-up and homework check; screenshot it, the vote on 12 answers it. |
| 12 | Multiple choice | Who is the author of Edmond de Belamy? | No correct answer; the split is the lesson. Show it next to the cloud. |
| 21 | Multiple choice | Sixty-four logos in a minute: where is the design? | Quick check: C — in the pick, and the written reasons for it. |
| 28 | Multiple choice | Which of these can you fine-tune on without asking anyone? | Quick check: A — thirty of your own sketches. D is the trap (an unread licence). |
| 39 | Multiple choice | A 400-word prompt, one image, shipped untouched: who holds the copyright? | Quick check: C — nobody; a prompt alone is not authorship (Part 2, January 2025). |
| 48 | Short answer, one per team | Your three of sixty-four, and why; the one that ships. | Capture 1: authorship written down. Comes back in week 12 as examples of a process note. |
| 50 | Image upload, one per team, caption required | The twelve-image dataset sheet; caption = what this teaches. | Capture 2: the wall; guess the sheet from the caption. The best three close the course in week 13. |
| 52 | Image upload, one per team, caption required | The draft poster; caption = the one fix. | Capture 3: the four sentences of tonight's checklist; Amber's baseline for the mock session. |

All eight buttons are generated by the build (caption required on 50 and 52).

## What to keep after class

- The slide-48 reasons (export): examples of a process note for week 12, and the list of teams whose reasons were adjectives — they get the *which part?* question again at the mock session.
- The slide-50 sheets (download): each team's dataset and its sentence; the three best come back on the last slide of the course.
- The slide-52 drafts and their fixes (download): the baseline Amber reads the final posters against next week.
- The slide-4 cloud and the slide-12 split, side by side, for the week-12 recap and the participation stars.
- Two things to re-check before week 12 and before the quiz: the Allen ruling (slide 33) and Hong Kong's bill (slide 35); the quiz must not ask what the deck could not verify.
