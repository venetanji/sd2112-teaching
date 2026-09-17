# SD2112 · Week 3 lesson plan

**Learning from examples** · three-hour lecture-workshop (about 170 minutes of content plus a 10-minute break) · deck: `week03-classpoint.pptx` (66 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week03/` (the html deck: the two p5.js sketches run live and their code slides are editable, `SD2112-week03.pdf` next to it)

## Purpose of this session

For us:

1. Close **module one** with **machine B**: a concept a machine holds without anyone writing it down, and the deal it makes (fluent, fuzzy, opaque), as the mirror of week 2's exact, explainable, brittle.
2. Give the theory its proper names, from the 2025 deck: the classical theory of concepts (Aristotle's definitions, with Plato's *Meno* and Wittgenstein's games as the witnesses against it) against prototype theory (Rosch's fruit, typicality), and show that the two theories are the two machines: classical theory + GOFAI, prototype theory + connectionism.
3. Tell the birth of AI twice: Dartmouth 1956, intelligence as reasoning with symbols; Rosenblatt 1958, a machine modelled on the brain. Then Hinton: backpropagation in 1986, the students and the GPUs in 2012, the Nobel Prize in 2024.
4. Explain parallel calculation and why the second school needed the chips made for games: one Turing machine step at a time against thousands of units at once, felt on a sketch that paints the Mandelbrot set with one core or four thousand.
5. Put modern AI on one timeline, 2012 to today, ending with the image editors that take reference images, which the room uses an hour later.
6. Run the one activity: a concept made visible in a picture, then two concepts blended in pairs with the pictures as references, then four in fours. The room meets the problem prototype theory could not solve (which properties survive a combination?) with a machine that has no definitions. Start Challenge 2 in class.

For students, by the end of the class they can:

- explain the difference between a definition (necessary and sufficient conditions) and a prototype (a middle and an edge, typicality), with a fruit or a cup as the example, and say why the *Meno* paradox and Wittgenstein's games are arguments against definitions;
- say what "learning from examples" means: numbers adjusted when a guess is wrong, until the examples are classified, and why the rule that results cannot be read;
- name the two births of AI (Dartmouth 1956; the perceptron 1958), one thing a hidden layer fixed (XOR) and what 2012 added (examples and GPUs);
- explain why a network is parallel by nature and why that made graphics cards the engine of modern AI;
- describe conceptual blending (two inputs, a generic space, a blend with emergent structure) and tell a blend from a collage in a generated image;
- use an image editor with one to three reference images on PolyU GenAI and say what came from each.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week03-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 word cloud once as a test and reset it. Check the three Image Upload buttons (slides 58, 60 and 62, all *caption required*). Open the html deck in a browser tab as well: slides 30 and 42 run the sketches live there, and that is what the room sees for them. |
| Amber | Canvas: post the deck link, the PDF, the blend prompt template (slide 55) and the Challenge 2 brief (slide 64). Download the Challenge 1 submissions; with WU Zhao and MA Jie shortlist five entries and have them ready to show from Canvas on slide 6, in a fixed order, the spec on screen before its picture (no names until the end). Nothing to paste into the deck and nothing to rebuild: the vote is a show of hands. |
| WU Zhao, MA Jie | At the door: who has a working PolyU GenAI login on a phone or laptop (one test generation). There is no logistics poll in the deck, so this count is the one we have: pair phone-only students with laptop owners, and sit anyone without a login next to someone with one. Confirm which image editor on `genai.polyu.edu.hk` takes reference images and how many at once (Flux, or Qwen Image Edit; the activity assumes up to three), and tell Gio and Nicolò the exact model name: slides 54 and 57–61 say "the image editor that takes references", and Gio names it aloud. During the activity, walk. |
| Gio | Fonts on the classroom PC (Inter and JetBrains Mono ship inside the deckgen package; README, *Classroom checklist*). The week-2 link: slide 5 links the wall of specs once `deck/week02-reports.json` carries the id of the image upload activity. Keep a screenshot of the slide-4 word cloud (it comes back on slide 46) and of the slide-18 fruit cloud (it goes next to slide 20). Backup: the html deck on a laptop — press `S` for notes. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Phones or laptops out; GenAI login checked. | | |
| 0:03 | 3–7 | Last week, in your words | *AlphaGo, one word*; what the week-2 wall said (one rule each, fifty-five pictures, and nobody defined "a picture"); the Challenge 1 winners: the five shortlisted entries shown from Canvas, the spec read aloud before each picture, a show of hands for the star and one TA pick; the semester map. | Word cloud | Anyone without a GenAI login sorts it out with a TA now, not at the break. Read each spec before its picture appears; then hands up, one vote each. Keep the cloud screenshot for slide 46. |
| 0:18 | 8–16 | What is a concept? | The classical theory (Aristotle pointing down; Plato, pointing up, disagrees); *sounds easy, try these* (prime numbers, furniture, sunset, pizza, an A+ essay); *define "cup" for a machine* (90 s, read four); Meno's paradox and Socrates's answer (ideas are real, learning is remembering, definitions are not the essence); Wittgenstein: "don't think, but look!"; the family-resemblance table; where the classical theory leaves us. | Short answer | Slide 15 is the core of this chapter: walk one column and show there is no full one. Cut 10 to two examples if behind. |
| 0:38 | 17–23 | Prototypes: Rosch, 1975 | *Name a fruit* (30 s: the room produces a prototype); Rosch's experiment; **the fruit, in her order** (put the cloud next to it); five typicality effects; prototype theory, its gain and its two costs (the edge, and combinations); quick check. | Word cloud; multiple choice | The two costs on slide 22 are the second half of the day: say them slowly. Quick check: C. |
| 0:53 | 24–32 | The birth of AI, twice | Dartmouth 1956, the proposal and the bet; Rosenblatt 1958, the brain as the model; the Mark I and the New York Times; one neuron as a weighted vote; what the perceptron code does, in four cards (slide 29: the examples, the rule, the nudge, the clicks); **the perceptron, live** (slide 30: watch it settle from a reload, then click an A among the Bs); 1958 · 1969 · 1986; the XOR limit and the hidden layer. | | Slide 30 is the core of the hour: "wrong: 0" after a few seconds, nobody wrote the line. Read the four cards of slide 29 first so the room knows what to watch. On a laptop: lr 0.05 → 0.5, Run. Cut 27 to a sentence if behind. |
| 1:11 | 33–38 | Neurons that learn: Hinton | Hinton, 1986 to 2024; backpropagation as a picture; two theories, two machines; the deal (fluent, fuzzy, opaque); the sentence to carry across the break. | | Slide 36 is the bridge of the module and the map for the reflection: the figure fills the slide, the two sentences are in the notes. |
| 1:23 | 39 | **Break, 10 min** | Everyone logged into GenAI before leaving the room. | | |
| 1:33 | 40–48 | Parallel: GPUs and modern AI | One step at a time against every unit at once; **the same rule 240,000 times** (slide 42: the cores slider from 1 to 4,096); the chips made for games and CUDA; inside the GTX 580; AlexNet; Move 37 with today's vocabulary (put the cloud back up); the timeline 2012–2026, ending with the editors that take references; how many numbers a model holds, from three to a trillion, on a log axis (slide 48). | | Slide 42: drag the slider to 0, then 12, and say that nothing about the rule changed. Cut 44 if behind. |
| 1:50 | 49–55 | Blending concepts | Bachelor was easy, pet fish is not; Fauconnier & Turner's four spaces (the houseboat, slide 51), then what a blend does (selective projection, emergent structure, every mash-up, slide 51); what an image editor does with two pictures: a collage, a blend, or one wins; four moves on GenAI; the prompt template. | | Ask the room for one blend of their own on slide 51 before moving on. |
| 2:00 | 56–63 | **Activity: the blend** | Section (1 min); round 1 alone, a concept as a picture (8); capture 1, everyone (3); round 2 in pairs, two concepts in one picture (12); capture 2, one per pair (2); round 4 in fours, four concepts, three images (15); capture 3, scribes (4); what just happened (3). | 3 × image upload | Nicolò keeps time with the slide timers; the other three TAs walk. Details below. |
| 2:48 | 64–66 | Challenge 2, homework | The brief; the 3Blue1Brown video before week 4; bring the week-2 specs and a laptop. | | TAs stay 30 minutes. |
| 2:52 | | Buffer | | | |

If GenAI is slow, give round 2 fifteen minutes, let capture 1 be a phone photo of the screen, and cut slides 27, 44 and 47. If the room is fast, let two fours put their four originals and their blend side by side on screen and have the room say which concept got lost and why.

## The activity, in detail: The blend

One concept per person, made visible; then two concepts in one picture; then four. **Each round ends in an image; what goes into ClassPoint is an image, and the caption says which concepts are in it and what came from where.** A phone or a laptop on `genai.polyu.edu.hk` per pair at least, with an image editor that takes reference images (Flux or Qwen Image Edit; up to three images in; the TAs confirm which before class). The prompt template is on slide 54 and on Canvas.

1. **Alone, 8 minutes — a concept as a picture (slide 57).** Pick a concept: anything, as specific as "my first bicycle" or as broad as "justice", abstract or concrete. Think how a picture would say it, write the prompt, text only, generate; look, change one thing, run again; two runs at most. Push people away from the first noun that comes to mind; a few abstract concepts in the room make the best blends later.
2. **Capture 1, 3 minutes — everyone uploads, caption required (slide 58).** Caption: the concept, in 50 characters or fewer. Put the wall up and read six captions with their pictures: does the picture say the concept? Most pictures are the prototype of their concept (the typical bicycle, the scales for justice): that is Rosch on the wall, and worth saying.
3. **Pairs, 12 minutes — two concepts in one picture (slide 59).** Show each other picture and concept; talk about how the two could become one thing, not two things side by side, and what each contributes. Write the prompt together from the template; images in: the two pictures, plus one more if it helps, three at most; run on the image editor, two runs. Expect the three outcomes from slide 52: a collage (both, side by side), a blend (one thing with properties of both), or one concept eating the other. Make every pair say which one they got and what came from where; that sentence is the caption.
4. **Capture 2, 2 minutes — one upload per pair, caption required (slide 60).** Caption: concept A + concept B, and one line on what came from each. Put the blend wall next to the concept wall; read three captions and ask the room for each: collage, blend, or one wins? The fours start as soon as the upload is in.
5. **Fours, 15 minutes — four concepts, three images, one picture (slide 61).** Join the pair behind you: four concepts and two blends on the table; say all four out loud. Choose the three images that go in (three at most; which stay out, and why?). One prompt: the thing you want and what comes from each image. Run; iterate by swapping one image or changing one line, never both; three runs. Stop when all four agree it is one thing; say which concept got lost, if one did. Four people choosing which pictures to show the model is curating a dataset: week 11 in miniature. This round is the start of Challenge 2.
6. **Capture 3, 4 minutes — scribes only, caption required (slide 62).** One image per four; caption: the four concepts, and the lost one. Put the three walls side by side: concepts, pairs, fours. Ask which wall has the most pictures that are one thing rather than a collage, and which concept got lost most often, and why (usually the one with the weaker prototype, or the one that went in as image 3). Download the submissions: the blends come back in week 5.
7. **Debrief, 3 minutes (slide 63).** Alone: the concept became its prototype. In pairs: a blend, a collage, or one wins; where it blended, the machine did what no definition can do, and cannot say how. In fours: the concept with the weaker prototype got lost; the middle pulls, in a mind and in a machine. *The machine made every image. You chose the concepts. That was the design.*

Round 4 is the start of Challenge 2 (slide 64): a picture from text and references, with two or three concepts of the student's own, one to three reference images of their own, the prompt word for word, and one sentence on what came from where and what got lost; the model must be named; on Canvas before week 4; the room votes in week 4.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room, help with attaching several images and their order, and note the best blends for the week-4 awards.

## The editable slides

In the html deck, the code panel of slides 30 and 42 is an editor: **Run** (or ctrl+enter) re-runs the sketch beside it with whatever is in the box, **Reset** brings the slide's code back, and what a student typed survives a reload. On 30 the sketch is the perceptron: it settles from a reload, a click adds an example of class A, a shift-click one of class B, and C starts again; the bar under it shows the three numbers. Slide 29, just before it, says in four cards what the code is trying to do (the examples, the rule, the nudge, the clicks), so read that one before pressing anything. On 42 the slider is how many pixels are painted in each frame, 2^k from 1 to 4,096, and a click starts the painting again from the top. The PowerPoint and the PDF show the code and a still, and their captions link to the slide in the html deck.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Word cloud | AlphaGo. One word. | Warm-up on the homework film; screenshot it, it comes back on slide 46 as the room's first verdict. |
| 11 | Short answer | Define "cup" for a machine. | Read four: every definition admits the wrong thing or excludes the right one. The classical theory failing live; keep the answers for the mid-term question bank. |
| 18 | Word cloud | Name a fruit. The first one that comes to mind. | The room's prototype: three or four big words and a long tail. Put it next to Rosch's list on slide 20. |
| 23 | Multiple choice | Which sentence is prototype theory? | Quick check: C. |
| 58 | Image upload, everyone, caption required | Your concept, as a picture; caption: the concept, 50 characters or fewer | The concept wall: prototypes, mostly. |
| 60 | Image upload, one per pair, caption required | The blend; caption: A + B, and what came from each | The blend wall next to the concept wall: collages, blends, and concepts that ate the other. |
| 62 | Image upload, one per four, caption required | The four-way blend; caption: the four concepts, and the lost one | The third wall; downloaded for week 5 and the week-4 awards. |

All seven buttons are generated by the build (caption required on 58, 60 and 62). There is no logistics poll and no ClassPoint vote this week: the TAs count logins at the door, and the five Challenge 1 entries are shown from Canvas on slide 6, where a show of hands picks the star and the TAs pick one more. Slide 5 links the week-2 wall of specs through `deck/week02-reports.json` once it exists.

## What to keep after class

- The slide-4 word cloud and the slide-11 definitions: the room's first vocabulary for machine creativity and for concepts; they come back in week 11 (authorship) and week 12 (the recap), and the reflection asks for the same argument.
- The three walls (58, 60 and 62) as screenshots and as downloads: week 5 opens with them when we push a model off the prototype properly (references, ControlNet, fine-tuning).
- Which image editor on GenAI accepted several reference images reliably, how many, and how long a generation took: it goes in the week-5 plan.
