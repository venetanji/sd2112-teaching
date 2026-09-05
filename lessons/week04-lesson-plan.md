# SD2112 · Week 4 lesson plan

**Language machines** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week04-classpoint.pptx` (66 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week04/` (html deck with the four p5.js sketches running live; `SD2112-week04.pdf` next to it)

## Purpose of this session

For us:

1. Open module 2 with a working model of how a language model writes: text → tokens → embeddings → attention → the odds of the next token, and a die thrown on them — the same chain as Nake's Walk-Through-Raster, with a very long memory.
2. Show what training does to that machine (base, instruction-tuned, RLHF) and what it can see (the context window, the system prompt), so that the two failures — hallucination and sycophancy — are consequences, not mysteries.
3. Land **prompting as briefing**: the week-2 spec (rule, chance, numbers, constraints, output) becomes the anatomy of a brief (goal, audience, constraints, examples, output, leave out), and a vague brief gets the model's middle.
4. Get every student to brief one small real job three ways and to name the heading that moved the draft.
5. Start Challenge 3 in class (a brief drafted by a model, then edited), so nobody goes home with a blank page.

For students, by the end of the class they can:

- say what a token is, why the same brief costs more tokens in Chinese than in English, and why a model cannot count letters;
- explain "a word is a point; nearby means similar; the axes have no names", and connect it to search, CLIP and recommenders;
- describe next-token prediction as a table and a die, and say what temperature does to the bars;
- explain why models hallucinate (guessing was rewarded: Kalai et al., September 2025) and why they flatter (short-term feedback: the GPT-4o rollback, April 2025), and write two defences into a brief;
- write a six-heading brief and a system prompt, run both on PolyU GenAI, and say which heading changed the draft.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week04-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 short answer once as a test and reset it. Check the Image Upload button on slide 61 (*caption required*). Open the html deck in a browser tab as well: the four sketches (slides 11, 16, 20, 26, 28) only run there; the pptx shows stills. Open `genai.polyu.edu.hk`, log in, pick the language model that answered the week-2 template most reliably, and test the system prompt from slide 53 on one product idea: it should return a one-page brief with six headings and "to confirm" where it does not know. Tell Gio which model. |
| Amber | Blackboard: post the deck link, the PDF, the brief anatomy (slide 45 / 58), the system prompt template (slide 53), the Challenge 3 brief (slide 64), the Verbeek (2015) PDF and the three video links (slide 65). Pick the four best Challenge 2 entries, anonymise them (prompt + image, no names), and send Gio the four prompts for slide 6 and the images for the screen. |
| WU Zhao, MA Jie | At the door: who has a laptop or a phone, whose PolyU GenAI login works. Fix logins on the spot. Seat phone-only students next to laptop owners; rounds 2 and 4 need one device per pair. During the class, walk with the four compare questions from slide 54 (did it do what I said · what did it decide · what did it invent · would I send it). |
| Gio | Fonts on the classroom PC (`tools/fonts/`). Paste the four Challenge 2 prompts into slide 6 and two real week-2 briefs (one slide-9 house rule, one capture-2 spec) into slide 46 before the build, or read them aloud from the phone. Screenshot of the week-2 capture-2 wall for slide 46. Backup: the html deck on a laptop — press `S` for notes; the sketches on 11, 16, 20, 26 and 28 run live there. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Devices out from the start. | | |
| 0:03 | 3–8 | Last week, in your words | *3Blue1Brown: one thing you understood, one you did not* (2 min, read six); week 3 in three lines; the four Challenge 2 entries by prompt; the vote; the semester map (module 2 begins). | Short answer; multiple choice | The "did not understand" lines tell you which chapter to slow down on; say which. |
| 0:13 | 9–13 | Text → tokens | The tokenizer figure (English 11 tokens, Chinese 21); the live toy tokenizer (type, hover); four things tokens decide; quick check. | Multiple choice | Slide 11 is live in the html deck only: type a Cantonese word in letters, a URL, "unbelievably". |
| 0:24 | 14–18 | Tokens → embeddings | Forty words on two axes; the live nearest-five (click: cosine); what a point buys you (similar, search, arithmetic, CLIP); *the word is a point, the sentence is a path*. | | Slide 16 live. Be honest about the word2vec caveat (notes on 15). |
| 0:36 | 19–22 | The transformer | Attention, live (hover "it": chair); the whole machine in four moves; the 3Blue1Brown video, rewatch the attention minute if the short answers asked for it. | | Cut 22 if the room understood attention. |
| 0:47 | 23–29 | The next token, and temperature | *A language model is a Markov chain with a very long memory*; Markov → Shannon → Hiller/Nake → GPT; the live bigram machine (click, mouse height, C); temperature at three heats; the whole model in three functions; quick check. | Multiple choice | Slides 26–28 are the heart of the lecture; 26 and 28 live. Cut 28 if behind. |
| 1:02 | 30–34 | Base, tuned, briefed | Pre-training → instruction tuning → RLHF; same weights, different manners; the context window; the system prompt (published since August 2024). | | Cut 32 if behind. |
| 1:12 | 35–40 | Fluent, typical, cannot say why | Hallucination (Kalai et al., 4 Sept 2025: guessing was rewarded; the exam figure); sycophancy (25–29 April 2025: the thumbs); four defences; agents: plan, act, observe; quick check. | Multiple choice | Slide 38 is the bridge to the second half: two of the defences are briefing rules. |
| 1:24 | 41 | **Break, 15 min** | Everyone logged into GenAI before leaving the room; one model, kept for the session. | | |
| 1:39 | 42–50 | Prompting as briefing | *A prompt is a brief*; the week-2 spec becomes the brief; anatomy (six headings); the first briefs (yours, from week 2); one job, three briefs; what each gets back (the middle); the structured brief for the poster; edit the brief, not the draft. | | Slide 48 is the core of the second half. Cut 46 or 50 if behind. |
| 1:57 | 51–54 | The workshop | The job (fair poster or exhibit caption); the system prompt as a workflow; the four compare questions. | | Nicolò's tested model is the one everyone uses. |
| 2:06 | 55–63 | **Activity: brief it three ways** | Section (1 min); round 1 alone, one line (5); capture 1, everyone (3); round 2 in pairs, the anatomy (8); pulse (2); round 4 in fours, the workflow on a stranger's idea (10); capture 2, scribes, and the wall (5); the vote (2); what just happened (3). | Short answer; multiple choice; image upload; multiple choice | Nicolò keeps time; the other three TAs walk. Details below. |
| 2:45 | 64–66 | Challenge 3, homework | The brief: prompt, unedited draft, your edit, on Blackboard before week 5; three videos and Verbeek. | | TAs stay 30 minutes. |
| 2:50 | | Buffer | | | |

If GenAI is slow, give round 2 ten minutes and cut slides 22, 28 and 46. If the room is fast, let two fours read their system prompt aloud and have the room guess what it imposes on any idea before the two briefs are shown.

## The activity, in detail: Brief it three ways

One small real job — an A2 poster for the week-13 poster fair, or the forty-word caption of an exhibit — briefed three ways: a line alone, the six-heading brief in pairs, a system prompt in fours run on a stranger's idea. **Each round ends in ClassPoint; the last capture is an image, and its caption is the brief or the prompt.** One device per pair with a language model on `genai.polyu.edu.hk`; the same model for everyone, so the middle stays the same middle.

1. **Alone, 5 minutes — one line (slide 56).** Pick the job. Type one line and no more: *Write a brief for a poster for a student design fair* (or *a caption for an object in a design exhibition*). Read the draft; underline every sentence you did not ask for. Stop anyone who improves the line — the point is the middle.
2. **Capture 1, 3 minutes — everyone pastes the first sentence (slide 57).** A wall of a hundred first sentences, most of them the same sentence: "This brief outlines…". Read five in a row; the room laughs at the third. That is the model's middle, and nobody typed it. Screenshot it.
3. **Pairs, 8 minutes — the anatomy (slide 58).** Same job, same model, new chat. Write the six headings together (goal, audience, constraints, examples, output, leave out); paste two examples if you have them. Run it; tick the six headings in the draft, circle what it decided, box what it invented. **Where did the draft get closer to what you meant, and which heading did that?** Expect dropped headings and an invented date for the fair.
4. **Pulse (slide 59).** *Compared with round 1, the second draft is…* the same with more words / specific, and we can name the heading / worse, boxed in / not back yet. Ask two Bs for the heading; ask a C what the corner was (usually a wrong constraint: a brief problem, not a model problem). Ds get a TA.
5. **Fours, 10 minutes — the workflow (slide 60).** Join the pair behind. New chat; paste the system prompt from the slide (edit it if you dare). Each pair writes a product idea in two lines; swap; run the workflow on the other pair's idea, then on your own. What repeats across the two briefs is the prompt's middle. Fix the prompt, run once more; one scribe screenshots the best brief.
6. **Capture 2, 5 minutes — scribes only, caption = the prompt (slide 61).** One screenshot per four, caption required. Put the wall on screen; read two captions aloud and have the room guess what the brief looks like before showing it; where the guess fails, the prompt failed. Download the submissions: the seed of Challenge 3 and evidence for the reflection.
7. **The vote, 2 minutes (slide 62).** *Which draft would you send to a client?* D — none without my edit — is the honest answer; the follow-up is the debrief. Anyone who votes A reads it aloud.
8. **Debrief, 3 minutes (slide 63).** The line got the middle; the anatomy moved the draft when a door closed, and you can name the heading; the workflow's middle is the prompt's, and editing it is designing a product's manners (week 12). *The machine wrote every word. You wrote the brief. That was the design.*

Round 4 is the start of Challenge 3 (slide 64): a brief drafted by a language model from your prompt, then edited by you — prompt, unedited draft and your edit with the changes visible, on Blackboard before week 5; the model is named; the room votes in week 5.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room with the four compare questions, help with logins and new chats, and note the best system prompts for the week-5 awards.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Short answer | 3Blue1Brown: one thing you understood, one you did not | Read six; the "not yet" lines pick the chapter to slow down on. Keep for the mid-term. |
| 7 | Multiple choice | Challenge 2: which entry gets the star? | The awards; no correct answer. Note the split. |
| 13 | Multiple choice | Which costs the model more tokens? | Quick check: B (the Chinese sentence: 21 tokens against 11). |
| 29 | Multiple choice | Temperature 0 means… | Quick check: A (always the most likely token; repeatable, not true). D is the trap. |
| 40 | Multiple choice | Why do language models make things up? | Quick check: B (guessing was rewarded — Kalai et al., 2025). |
| 57 | Short answer, everyone | The first sentence of the one-line draft | The wall of identical first sentences: the middle. Screenshot it. |
| 59 | Multiple choice | Compared with round 1, the second draft is… | Pulse; Bs name the heading, Cs name the corner, Ds get a TA. |
| 61 | Image upload, one per four, caption required | The best brief, and the prompt that made it | Prompt–brief pairs for Challenge 3 and the week-5 awards. |
| 62 | Multiple choice | Which draft would you send to a client? | The vote; D is the honest answer and the debrief follows from it. |

All nine buttons are generated by the build (caption required on 61).

## What to keep after class

- The slide-4 answers: what the room did not understand about the video, for the mid-term quiz and for the week-5 recap.
- The two walls (57 and 61) as screenshots, for the week-5 recap and the Challenge 3 awards.
- The best system prompts from round 4: week 12 (language as an interface) opens with them.
- Which language model on GenAI produced usable briefs most reliably and how it handled "to confirm": it goes in the week-5 plan and in the week-8 product brief.
