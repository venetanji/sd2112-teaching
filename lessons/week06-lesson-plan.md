# SD2112 · Week 6 lesson plan

**Sound machines** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week06-classpoint.pptx` (66 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week06/` (html deck with the four p5.js sound sketches running live — they make sound only there, after a click, and the deck must be opened from the site or served locally, not from a downloaded file; `SD2112-week06.pdf` next to it)

## Purpose of this session

For us:

1. Close module 2 with the third medium: what sound is to a machine — a waveform, a spectrogram (time × frequency × loudness), MIDI (a note as four numbers) — so that every tool in the second half can be read as "which representation did it learn from".
2. Run the two machines again, on sound, live: a step sequencer and a Markov melody as machine A (the Illiac Suite's generate-and-test and its table of what follows what), spectrogram diffusion and codec-token models as machine B (Riffusion; Jukebox, MusicLM, MusicGen; Suno, Udio, AIVA).
3. Give the room the state of play on voices and ownership as of 5 September 2026 — three voice cases, two years of lawsuits, and the terms of the three products — so that Challenge 5 names the tool and the plan.
4. Land the **sound spec**: the week-2 spec and the week-4 brief made audible, with the rule lines a sequencer obeys exactly and the example lines a model interprets — and get every student to write one, hear a model's answer, and rebuild it as a rule.
5. Rehearse the mid-term with eight mock questions in the real format, and send everyone home with a reflection draft plan, Challenge 5 and a pitch sentence for week 7.

For students, by the end of the class they can:

- say what a waveform and a spectrogram show (two things vs three), what a sample rate is, and why a spectrogram is the picture a model looks at;
- read a step grid and a Markov table as rules, say where chance enters in each, and explain what temperature does to the table;
- describe the two roads of machine B for audio — a picture of sound denoised, a language of sound predicted — and name one system on each;
- state where the Suno, Udio and GEMA cases stand, which plan of which product gives you what, and why "name the tool and the plan" is part of a process note;
- write a sound spec with rule lines and example lines, get a music-model prompt from a language model, and say what the model decided that the spec did not.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week06-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 short answer once as a test and reset it. Check the Image Upload button on slide 56 (*caption required*). Open the html deck in a second browser tab **from the course site** (`venetanji.github.io/sd2112-teaching/week06/`), or serve a local build with `python -m http.server` in `_site` — never by double-clicking `index.html`: from a `file://` page Chromium refuses p5.sound's audio worklet, and the spectrogram silently shows the sweep instead of the microphone. The sound sketches (slides 12, 13, 18, 22, 23, 55) run only there, start on a click, and need the room speakers — test the speakers, and on slide 12 accept the microphone permission once so the prompt does not appear in class (if the PC has no microphone the sketch falls back to a built-in sweep by itself). Test which music model answers from the classroom network with the example spec of slide 44 — Suno's free plan (personal, non-commercial), the MusicGen demo on Hugging Face, or Stable Audio's free tier — and tell Gio which one the room uses. Post on Blackboard the link to the sequencer's own page on the course site, `venetanji.github.io/sd2112-teaching/week06/sketches/w06-sequencer.html` (also listed in the Sketchbook; vendored p5.js 1.11 + p5.sound 1.0, runs on a phone), and test it on a phone: it is the fallback and round 4. Do not paste the code into a new sketch at `editor.p5js.org`: the editor's default has been p5.js 2.x since 31 July 2026, under which this p5.sound 1.x code throws an error; if the editor is wanted anyway, set the sketch to p5.js 1.11.x in its settings, check in its `index.html` that the p5.sound it loads is the 1.x one (the version selector does not reliably swap p5.sound with it: p5.js-web-editor issue #3513), and test the share link on a phone. |
| Amber | Blackboard: post the deck link, the PDF, the sound spec template (slide 45), the round-2 instruction to the language model (slide 53), the Challenge 5 brief (slide 64), the reflection rubric with "what a good draft has" (slide 63) and a sign-up sheet for the draft check. Pick the four best Challenge 4 entries, anonymise them (brief + layout, no names), and send Gio the four briefs for slide 6 and the layouts for the screen. |
| WU Zhao, MA Jie | At the door: who has a laptop, headphones, and a working `genai.polyu.edu.hk` login. Fix logins on the spot. Seat phone-only students next to laptop owners; round 2 needs one laptop and one pair of headphones per pair. During the class, walk with the four questions of slide 46 (did it do what I said · what did it decide · what did it invent · would I ship it). After class, run the draft-check table for 30 minutes with the rubric of slide 63: a draft of any length and the three experiments the student intends to use. |
| Gio | Fonts on the classroom PC (`tools/fonts/`). Paste the four Challenge 4 briefs into slide 6 before the build, or read them aloud from the phone. Screenshots of the week-5 walls for the recap. Decide with Nicolò which music model the room uses; if none answers from the network, the workshop is the spec plus the sequencer (slide 50 notes) and the debrief is unchanged. Backup: the html deck on a laptop, opened from the course site or served locally (`python -m http.server` in `_site`), not from a file — press `S` for notes; the sketches on 12, 13, 18, 22, 23 and 55 run live there. Check the dates on slides 37 and 38 against the news of the week: the lawsuits move monthly. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Headphones and laptops out from the start. | | |
| 0:03 | 3–8 | Last week, in your words | *AltexSoft: one thing you understood, one you did not* (2 min, read six); week 5 in three lines; the four Challenge 4 entries by brief; the vote; the semester map (module 2 closes). | Short answer; multiple choice | The "not yet" lines tell you whether to slow down on the spectrogram (chapter 2) or the tokens (chapter 4). |
| 0:13 | 9–16 | What a machine hears | The waveform (dots, 44,100 a second); how a spectrogram is made; **live: the microphone as a spectrogram** (whistle, "aaa", clap); live: timbre as harmonics; MIDI, four numbers; melody, harmony, rhythm, timbre; quick check by a show of hands. | | 12 and 13 are html-only and need a click for sound. Cut 13 if behind. |
| 0:35 | 17–25 | Rules that play | **Live: the step sequencer** (toggle cells, tempo, C); the clock in eleven lines; the Illiac Suite (video, 1 min); generate-and-test and the table; **live: the Markov melody** (temperature, new dice); the Markov step in code; the SLOrk video; quick check by a show of hands. | | 18 and 22 are the heart of the first half. Cut 24, then 23, if behind. |
| 1:00 | 26–32 | Models that listen | Two roads; Riffusion; Jukebox, MusicLM, MusicGen, the products; the AltexSoft video (point, do not play); Suno, AIVA, Udio and what you own; quick check by a show of hands. | | Slide 31 is read as of 5 September 2026: say the date. Cut 28 to one sentence if behind. |
| 1:18 | 33 | **Break, 15 min** | Everyone logged into GenAI and the music model before leaving the room; headphones found. | | |
| 1:33 | 34–41 | Voices, and who owns a sound | Voice cloning as a vector; three cases (Heart on My Sleeve, Sky, The Velvet Sundown); two years of lawsuits in eight steps (read three); where it stands; **mock quiz 1–3**. | 3 × multiple choice | Say what the mock quiz is: the real format, not graded, answers discussed on the spot. |
| 1:49 | 42–48 | Sound for a product | Five sounds you know (THX, Intel, Windows 95, Netflix, Mastercard); the sound spec, rule lines and example lines; the template and the two-machine pipeline; the four questions; **mock quiz 4–5**. | 2 × multiple choice | Slide 44 is the core of the second half: read one line from each column and ask which machine could execute it. |
| 2:01 | 49–57 | **Activity: thirty seconds for a product** | Section and the tools (2 min); round 1 alone, the spec (5); capture 1, everyone (2); round 2 in pairs, generate and listen (10); capture 2, one per pair (2); round 4 in fours, the same brief in the sequencer (10); capture 3, scribes, and the wall (3); what just happened (2). | Short answer; short answer; image upload | Nicolò keeps time; the other three TAs walk. Details below. |
| 2:37 | 58–65 | The quiz, the reflection, the challenge | **Mock quiz 6–8**; how the real quiz works; the reflection rubric and the draft check; Challenge 5; before week 7 (the reflection, the revision, the sound, a pitch sentence). | 3 × multiple choice | Say the order of next week: the Challenge 5 vote, the quiz, the pitches, the teams. |
| 2:50 | 66 | End | See you next week: the mid-term. TAs stay 30 minutes for the draft check. | | |
| 2:53 | | Buffer | | | |

If the music model queues or fails in class, round 2 becomes the sequencer round (the spec's tempo and structure as a grid) and round 4 compares two grids from two specs; the debrief is the same. If behind, cut 13, 24 and 28 in that order, and move mock questions 6–8 to Blackboard as a practice set. If the room is fast, play two of the capture-2 links to the room and ask which line of the spec each sound broke.

## The activity, in detail: Thirty seconds for a product

A sound for a moment in a product — a lock opening, a payment going through, an app starting, a timer ending — specified alone, generated and criticised in pairs, rebuilt as a rule in fours. **Each round ends in ClassPoint; the last capture is an image, and its caption is the spec.** One laptop and one pair of headphones per pair; a language model on `genai.polyu.edu.hk`; the one music model Nicolò tested; the sequencer on its own page on the course site, linked from Blackboard, on any device.

1. **Alone, 5 minutes — write the spec (slide 51).** The template is on the slide and on Blackboard: purpose, the moment, length, tempo, mood, timbre, structure, like / not like, must-not, deliverable. Numbers where possible (seconds, BPM), words where necessary, at least one must-not. Watch for specs with no purpose and no must-not, and for "epic" and "cinematic" — the middle of every music model. A sound without a moment is a song, not a product sound.
2. **Capture 1, 2 minutes — everyone: the product, the moment, the length (slide 52).** One line: "a bike-share app · the lock clicks open · 3 s". A wall of a hundred products and moments; the lengths cluster at three seconds and thirty, the moments are payments, unlocks and alarms. Point at one whose purpose you can hear, and one you cannot. Screenshot it.
3. **Pairs, 10 minutes — generate, listen, write what it decided (slide 53).** Pick the better spec. Paste it into the language model with the instruction on the slide (a prompt for a text-to-music model under sixty words, no lyrics, no artist names; then "the rule the sound follows" in one sentence). Paste the prompt into the music model; **generate twice**; listen with the four questions. Tick the rule lines, circle the middle, box what it invented. **Three lines: what did the model decide that the spec did not say?** Fix one line of the spec, run once more. Expect the length ignored, a fade nobody asked for, a voice appearing, the ukulele.
4. **Capture 2, 2 minutes — one per pair: the spec in one line, the link, one thing it decided (slide 54).** "3 s · 120 BPM · marimba, no voice · [link] · it added a reverb tail". Read the "it decided" halves in a row: the list is the model's middle for "product sound", and nobody typed it. Keep the links — they are the start of Challenge 5.
5. **Fours, 10 minutes — the same brief, as a rule (slide 55).** Join the pair behind. Take the better spec and build it in the sequencer: the spec's tempo, sixteen steps, three sounds at most, C first. Play the model's and the grid's back to back: **which one is the product's?** All four must agree and say why in a sentence. The grid obeys the rule lines exactly and is deaf to mood; the model had the mood and ignored the tempo. Expect the grid to win for unlocks and notifications, the model for anything longer than five seconds.
6. **Capture 3, 3 minutes — scribes only, caption = the spec (slide 56).** One image per four: a screenshot of the sequencer grid or of the model's waveform, caption required. Put the wall on screen; read two captions aloud and ask whether the picture is a grid or a waveform before showing it. Download the submissions: seeds of Challenge 5 and evidence for the reflection.
7. **Debrief, 2 minutes (slide 57).** The spec: half rules, half examples, and they could say which. The model: exact where the spec had numbers, the middle where it had words. The grid: exact, explainable, deaf to mood. *The machine played every note. You wrote the spec. That was the design.*

Round 2 is the start of Challenge 5 (slide 64): thirty seconds of sound — the spec, the sound with a screenshot of the spectrogram or the grid, and a note naming the tool, the plan and what the model decided that they kept or undid — on Blackboard before week 7; the room votes first thing next week, before the quiz.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room with the four questions, help with the music model's queue, and note the best specs for the week-7 vote.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Short answer | AltexSoft: one thing you understood, one you did not. | Which chapter to slow down on; a screenshot for the quiz revision. |
| 7 | Multiple choice | Challenge 4: which entry gets the star? | The vote; a star for the winner. |
| 39 | Multiple choice | Mock quiz 1 · Photoshop's three fills: which learned from examples? | C (Generative Fill). Week 1. |
| 40 | Multiple choice | Mock quiz 2 · randomSeed(1) means… | B (the same "random" numbers every run). Week 2. |
| 41 | Multiple choice | Mock quiz 3 · Move 37 mattered because… | B (a move no human would play, and it won). Week 3, the film. |
| 47 | Multiple choice | Mock quiz 4 · a token is… | B (a piece of text read as a number). Week 4. |
| 48 | Multiple choice | Mock quiz 5 · a diffusion model makes an image by… | B (removing noise step by step, steered by the prompt). Week 5, the playlist. |
| 52 | Short answer, everyone | The product, the moment, the length | The wall of moments. Screenshot it. |
| 54 | Short answer, one per pair | The spec in one line, the link, one thing it decided | The model's middle for "product sound"; the links seed Challenge 5. |
| 56 | Image upload, one per four, caption required | The grid or the spectrogram, and the spec | Spec–sound pairs for the week-7 vote and the reflection. |
| 59 | Multiple choice | Mock quiz 6 · the Illiac Suite's fourth experiment chose notes with… | B (a Markov chain). Week 6, the playlist. |
| 60 | Multiple choice | Mock quiz 7 · Riffusion made music by… | B (spectrogram images from a diffusion model, played back). Week 6. |
| 61 | Multiple choice | Mock quiz 8 · "Designing things is designing human existence" | C (Verbeek, 2015). Weeks 1 and 5, the core reading. |

All thirteen buttons are generated by the build (caption required on 56). The three chapter quick checks (slides 16, 25, 32: a spectrogram's three axes, A; where chance enters in the Illiac Suite, A; which is machine B, C) are a show of hands, not ClassPoint questions, to keep the button count down in a week that already carries eight mock questions. The mock-quiz answers are in the speaker notes; discuss each one on the spot — the split per question tells you which week needs a revision note before the real quiz.

## What to keep after class

- The three walls (52, 54, 56) as screenshots, and the links from 54: the seeds of Challenge 5 and evidence for the reflection.
- The per-question splits of the eight mock questions (39–41, 47–48, 59–61): whichever week scored worst gets a revision note on Blackboard before week 7.
- Which music model answered from the classroom network, and how long its queue was: it goes in the week-7 plan for the Challenge 5 playback.
- The draft-check list: who came, and which of the three experiments each student is using — Amber follows up with the ones who did not come before the week-7 deadline.
- Anything that changed in the Suno, Udio and GEMA cases since 5 September 2026: slides 37 and 38 carry dates and need a line added, not rewritten.
