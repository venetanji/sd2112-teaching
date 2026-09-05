# SD2112 · Week 12 lesson plan

**Language as an interface** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week12-classpoint.pptx` (58 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week12/` (html deck with the three p5.js sketches running live; `SD2112-week12.pdf` next to it)

## Purpose of this session

For us:

1. Close the course's spine with the product everyone talks to: a **rules-based chatbot is machine A** (ELIZA, back from week 2 as a live script of our own rules — the room sees the rule that decided) and a **generative one is machine B** (fluency, no script, no guarantee), with three cases where the company paid for what its bot said (Chevrolet, DPD, Air Canada); and the designer's version, rules around a model.
2. Land **agents** as a loop the room can step through — plan, tool, observe — and the two ways it fails: it does what you said ("for four": people, or o'clock?) and what the page said (indirect prompt injection); the confirm card before every write as the guardrail.
3. Teach the core reading, **Van Den Eede (2011)**: transparency of use (the tool withdraws; Heidegger's hammer, Ihde's glasses) against transparency of origins and effects, "an essential contradiction" — and a chat assistant as the product built for the first and against the second. The Turing test revisited: 1950's bet, 2025's result (a persona prompt beats the person), and Article 50 as the law's answer.
4. Give every team the **four levers of the mediation brief's guardrails heading** — participatory design (before), guardrails (inside), explainability (at the screen), auditing (after) — one paragraph each.
5. Run the chatbot exercise on every team's own product (five rules, then a system prompt, on the same three messages) and the **mock poster session** (A3 on the wall, two rounds, a rubric card, one fix), so that week 13's fair has no first-time surprises. Fold the course: the two machines, the designer's turn, the course question asked for the record.

For students, by the end of the class they can:

- explain how a rules-based chatbot decides (keyword, rank, template, pronoun swap; NONE and MEMORY) and what the generative version changes: fluency, no script, no guarantee;
- describe an agent as a model in a loop with tools, tell read tools from write tools, and say where a person in the loop belongs and why;
- state Van Den Eede's two transparencies, place a chat assistant on them, and name the moments where their own assistant should show itself;
- say what the Turing test measured in 1950 and what passing means in 2025, and what Article 50 requires of a chatbot from August 2026;
- write the guardrails paragraph of their mediation brief as four sentences (who was in the room; may, never, when unsure; where it shows itself; what they log) and a system prompt that enacts the inside one.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week12-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 word cloud once as a test and reset it. Check the two Image Upload buttons (slides 48 and 54, both *caption required*) and the multiple-submission short answer on 55. Open the html deck in a second browser tab: the three sketches (slides 12, 18, 25) run only there — on 12 click the box, type "I need a logo for my café" and check that rule 1 lights up; on 18 put the mouse in the lower half and click through to the CONFIRM card; on 25 move the mouse across and click once for the dosage question. Keep the slide timers ready for rounds 1 and 2 (46, 47) and rounds A and B (52, 53). |
| Amber | Blackboard: post the deck link, the PDF, the rule format (slide 44) and the system-prompt template (slide 45) as text, the rubric card (slide 51) as a printable, and the week-13 brief (slide 57) once Gio confirms the printing instructions. Read every draft poster and mediation brief from week 11 and pick three findings for slide 5 (team numbers only, no names; one anonymised example each if there is time). After class: export the slide-55 fixes and post them on Blackboard tonight by team number; download the slide-48 screenshots and the slide-54 poster photos. |
| WU Zhao, MA Jie | Number the walls before class: one spot per team, tape at each. At the door: does every team have its A3 print and the video link on a laptop? Make the visiting list for the mock session (each team visits two posters, never a neighbouring team) and pin it on the door. One laptop per team logged into `genai.polyu.edu.hk` before the break. Print two rubric cards per team per round (about 110). During the mock session each of you takes a wall and listens for "it uses AI to" — a product with no decision in it; note the team numbers for Gio. |
| Gio | Fonts on the classroom PC (`tools/fonts/`). Screenshots for the recap if wanted: the week-11 dataset wall and two draft posters. Backup: the html deck on a laptop — press `S` for notes; the sketches on 12, 18 and 25 run live there. Decide the two things Blackboard needs tonight: where and by when the A0 is printed, and the time of the TAs' revision hour before week 13. Keep the week-1 "What is AI?" screenshot: the slide-41 answers are compared with it on the last slide of week 13. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Teams sit together; A3 prints and video links checked at the door. | | |
| 0:03 | 3–6 | Last week, in your words | *The last chatbot you talked to: one word* (4); three things we saw in the drafts and briefs (5, replace with the real ones); the semester map (6). | Word cloud | Screenshot the cloud; it comes back at the vote (49). |
| 0:12 | 7–15 | Two chatbots, two machines | The IBM homework (8, play a minute if the cloud was thin); the same message through three machines (9); seventy-six years of talking machines (10); one ELIZA rule step by step (11); **live: ELIZA with fourteen rules of our own** (12); fluency, no script, no guarantee (13); Chevrolet, DPD, Air Canada (14); *what decided ELIZA's answer?* (15). | Multiple choice | Type three lines from the room on 12; the last one should break it. Cut 10 to its four bold dates if behind. |
| 0:35 | 16–21 | Agents | The loop (17, figure); **live: a room for four** (18: click through alone, then again with the mouse low); read, write, the valve, the log (19); four failure modes (20); *the agent booked six seats at two o'clock* (21). | Multiple choice | On 18 do both endings; the CONFIRM card is the slide. Tell the Replit case in full on 20. |
| 0:51 | 22–29 | Trust, transparency, opacity | Weizenbaum 1976 (23); the reading as two axes (24, figure); **live: the dial** (25: left, right, then click for the dosage question); *designed to disappear, opaque about how it decides* (26); the Turing test 1950 and 2025 (27, figure); what passing means when everyone passes (28); *transparent, in Van Den Eede's sense* (29). | Multiple choice | 24 and 25 are the core of the first half: say the contradiction, then move the dial. 29 is a final-quiz question; say so. |
| 1:10 | 30–36 | Designing the mediation | The four levers on the guardrails heading (31, figure); explainability (32); participatory design (33); auditing (34); guardrails (35); *the guardrails heading is yours to write* (36). | | Two minutes a slide. Cut 35 to its title if behind; slide 45 repeats it as a template. |
| 1:22 | 37 | **Break, 15 min** | Every team pins its A3 at its number and logs into GenAI before leaving the room. | | The TAs have tape and the visiting list. |
| 1:37 | 38–42 | The course, folded | The two machines, week 1's drawing (39); curator, briefer, guardrail-setter (40); *can a machine originate a design?* (41, everyone, read six); the final quiz (42). | Short answer | Keep the 41 answers; they close week 13. |
| 1:49 | 43–49 | **Workshop: an assistant for your product** | Section (1 min); the exercise (44, 3); the system prompt (45, 2); round 1, five rules (46, 8); round 2, the model (47, 8); capture, one screenshot per team (48, 3); the vote (49, 3). | Image upload; multiple choice | Nicolò keeps time; the other three TAs walk with one question: "which rule fires on M3?" Details below. |
| 2:17 | 50–55 | **The mock poster session** | Section (1 min); the rubric card (51, 2); round A, odd teams present (52, 10); round B, swap (53, 10); capture, the poster on the wall (54, 2); the fixes, one line per card (55, 3). | Image upload; short answer | Each TA takes a wall. Details below. |
| 2:45 | 56–58 | Debrief, homework | What just happened (56); due for the fair: the A0, the video, the brief, the quiz (57); end (58). | | TAs stay 30 minutes and read briefs. |
| 2:50 | | Buffer | | | |

If GenAI is slow, round 2 becomes a paper round: teams write the system prompt and predict the three answers, and the capture is a photo of the sheet. If the room is fast, give the mock session a third round in which every team reads its two cards aloud at its poster and says which fix it will make.

## The activities, in detail

### An assistant for your product (slides 43–49, 28 minutes)

Team-based, one laptop per team on `genai.polyu.edu.hk`, one sheet for the rules. **What goes into ClassPoint is one screenshot per team (caption: the message no rule caught, or the answer the model got wrong) and one vote.**

1. **Teams, 8 minutes — three messages, five rules (slide 46).** First the three messages the assistant must survive, for this product: M1 the normal request, M2 the edge, M3 the one it must refuse (a dose, a price, a promise, a person's data). Then five rules in the sketch's format — pattern → response — plus NONE (what it says when nothing fits) and the handover (when a person takes over, how). Test by hand: which rule fires on each message? Write "none" where none does. Expected: M1 fires, M2 fires the wrong rule, M3 fires none, and NONE says "please go on" to a question that needed a refusal. TAs: "which rule fires on M3?"
2. **Teams, 8 minutes — the same three messages through a system prompt (slide 47).** New chat; paste the template filled for the product (may, never, when unsure, say what you are, hand over); paste M1, M2, M3 one at a time; screenshot the three answers. Compare with the rules table: what did the rules refuse that the model answered? What did the model answer that no rule could? Teams whose model answered M3 rewrite one line of the never-list and try again — that is the guardrail being designed.
3. **Capture, 3 minutes (slide 48).** Image upload, scribes only, caption required. Read four captions without the pictures: the room hears "no rule fired on the refusal" and "it answered the dose" over and over — chapter two, on their own products. The captions are the guardrails paragraph in draft.
4. **The vote, 3 minutes (slide 49).** Rules only · a model, free · a model inside rules · no assistant. No correct answer; most choose the third, and some products honestly need a screen, not a conversation. Put the slide-4 word cloud next to the split.

### The mock poster session (slides 50–55, 28 minutes)

Posters are on the wall by team number from the break; the video is on a laptop at each poster. Two rubric cards per visiting team per round (printed by the TAs). **What goes into ClassPoint is one photo per team of its poster on the wall (caption: team number and the product in one sentence) and one line per rubric card from the reviewers: "Team N: one thing to fix before the fair".**

1. **The rubric card, 2 minutes (slide 51).** The project rubric folded: research 30, ethics 30, poster 20, video 10, team 10, each A, B or C from what the poster and the video show; three metres (the product in one sentence?), one metre (the decision, the data, the no?); one fix, one sentence. No defending.
2. **Round A, 10 minutes (slide 52).** Odd-numbered teams present (two people at the poster, the video ready); even-numbered teams visit the two posters on their list, four minutes each, fill a card, hand it over. Presenters photograph their poster for the upload.
3. **Round B, 10 minutes (slide 53).** Swap. Amber asks presenters what their first card said; Gio visits the teams the TAs flagged in round A.
4. **Capture, 2 minutes (slide 54).** Image upload, one per team, caption required. The wall on screen for a minute: read three captions and ask whether the poster says the same sentence.
5. **The fixes, 3 minutes (slide 55).** Short answer, multiple submissions: one line per card filled. Read six without team numbers; the room hears the same five sentences — draw the decision, say who it is for, where is the no, name the data, the title is the company not the product. Exported and posted tonight by team number.
6. **Debrief, 2 minutes (slide 56).** Rules, then rules around a model, then the fair once without the jury. *The model wrote every reply. You wrote the rules around it. That was the design.*

TA roles: Nicolò keeps time with the slide timers and calls the rounds; Amber, WU Zhao and MA Jie walk during the workshop with one question (which rule fires on M3?) and each take a wall during the mock session, listening for "it uses AI to".

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Word cloud | The last chatbot you talked to: one word for how it felt. | Warm-up; the room's words for other people's bots. Screenshot; back at the vote (49). |
| 15 | Multiple choice | ELIZA answered "What should the poster do…": what decided that? | Quick check: A — a pattern matched "I need"; rules are ranked. |
| 21 | Multiple choice | The agent booked six seats at two o'clock: what went wrong? | Quick check: B — the goal left "four" open and the loop filled it in. |
| 29 | Multiple choice | In Van Den Eede's sense, a technology is transparent when… | Quick check: B — it disappears in use. A final-quiz question. |
| 41 | Short answer, everyone | Can a machine originate a design? Yes or no, and one sentence of evidence. | The course question, for the record; read six; kept for the last slide of week 13. |
| 48 | Image upload, one per team, caption required | The three answers, and the one that broke. | The guardrails paragraph in draft; read four captions. |
| 49 | Multiple choice | Your product's assistant: which one ships? | The vote; no correct answer; the split next to the word cloud. |
| 54 | Image upload, one per team, caption required | Your poster, on the wall. | The wall as the fair will see it; the jury's baseline next week. |
| 55 | Short answer, one line per card, multiple submissions | "Team N: one thing to fix before the fair." | Exported and posted tonight by team number; the week's checklist. |

All nine buttons are generated by the build (caption required on 48 and 54; multiple submissions on 55).

## What to keep after class

- The slide-55 fixes (export): on Blackboard tonight by team number; the list of teams flagged for "it uses AI to" gets the first review slot with Amber.
- The slide-54 photos (download): the baseline the jury compares against at the fair; Amber keeps them with the week-11 drafts.
- The slide-48 screenshots and captions: the guardrails paragraph of each brief in draft; teams that had no refusal rule get a reminder with the fixes.
- The slide-41 answers (export): the course question, for the last slide of week 13, next to the week-1 definitions of AI.
- The slide-4 cloud and the slide-49 split, for the week-13 opening and the participation stars.
- The two Blackboard items Gio decides today: where and by when the A0 is printed; the time of the revision hour.
