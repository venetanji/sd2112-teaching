# SD2112 · Week 3 lesson plan

**Learning from examples** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week03-classpoint.pptx` (57 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week03/` (html deck with the three p5.js sketches running live; `SD2112-week03.pdf` next to it)

## Purpose of this session

For us:

1. Close **module one** with **machine B**: a rule nobody wrote, found by nudging numbers until the examples are classified — and the deal it makes (fluent, fuzzy, opaque), as the mirror of week 2's exact, explainable, brittle.
2. Give the theory its proper names: classical theory versus prototype theory (Wittgenstein, Rosch, Labov), GOFAI versus connectionism (Haugeland), and show that the two theories of concepts are the two machines.
3. Let every student *see* learning happen: the perceptron finding its line, Labov's cups at the edge of a concept, a curve that memorises instead of learning. The sketches are the argument; the slides are the captions.
4. Put the vocabulary of the reflection on the tools they use (Photoshop, Figma, the keyboard): rule-based or adaptive, and four tests to tell.
5. Open the course question for real with Move 37 (Boden, Wiggins): was it creative? — the first time the room takes a position.
6. Start Challenge 2 in class: a prompt tells, a reference shows; nobody goes home without having done both.

For students, by the end of the class they can:

- explain the difference between a definition (necessary and sufficient conditions) and a prototype (family resemblance, typicality), with a cup or a chair as the example;
- say what "learning from examples" means: numbers adjusted when a guess is wrong, until the examples are classified — and why the rule that results cannot be read;
- name one thing a hidden layer fixed (XOR) and one thing more layers and more examples fixed (learned features, AlexNet);
- tell generalising from memorising, and say why a model is judged on data it never saw;
- sort a design tool into rule-based or adaptive with the four tests, and give one pair from the same application;
- argue a position on Move 37 using exploratory / transformational creativity and the conceptual space;
- use a text prompt and a reference image on PolyU GenAI and say what each one did: the prompt selected, the reference pulled.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week03-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 word cloud once as a test and reset it. Check the two Image Upload buttons (slides 50 and 53, both *caption required*). Open `genai.polyu.edu.hk` in a browser tab with the image model that accepts an image input, and put `deck/assets/ai-chair-edge.jpg` and two of `ai-chair-1..4.jpg` on the desktop for the live demo on slide 47. Keep the html deck open on the laptop: slides 14, 21 and 26 run the sketches live and the PowerPoint only shows their stills. |
| Amber | Blackboard: post the deck link, the PDF, the Challenge 2 brief (slide 55) and the three activity prompts (slides 49, 51, 52). Download the Challenge 1 submissions; with WU Zhao and MA Jie shortlist four entries for the vote and write their specs (no names, no pictures) into the four choices on slide 6; have the four sketches ready to show on slide 7, in the same order; note which model each used. |
| WU Zhao, MA Jie | At the door: who has a working PolyU GenAI login on a phone (one test generation). Pair phone-only students with laptop owners. Confirm which Flux / Qwen model on GenAI takes a reference image next to the prompt, and tell Gio and Nicolò the exact model name for slide 45. During the activity, walk. |
| Gio | Fonts on the classroom PC (`tools/fonts/`). Screenshots from weeks 1 and 2: the cup wall (slide 15), the chair wall (slide 43), the two week-2 walls (slide 5), and the week-1 answers to "where did AI touch your design work" (for the sorting on slide 32). Find the move-37 timestamp in the film for slide 36. Backup: the html deck on a laptop — press `S` for notes. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Phones or laptops out; GenAI login checked. | | |
| 0:03 | 3–8 | Last week, in your words | *AlphaGo, one word*; what the week-2 walls said; the Challenge 1 vote on four specs, then the winners from Blackboard; the semester map. | Word cloud; multiple choice | Keep a screenshot of the cloud: it comes back on slides 39–40. Read each spec before its picture appears. |
| 0:18 | 9–17 | What is a concept? | *Define "cup" for a machine* (90 s, read four); the classical theory; Wittgenstein's games as a table; Rosch 1975; **the cups sketch** (slide 14, live); Labov's context; two theories = two machines; quick check. | Short answer; multiple choice | Slide 14 is the core of the first hour: cross from the cups to the bowls once and watch the vote go from 5–0 to 3–2. Cut 11 to a sentence if behind. |
| 0:40 | 18–28 | Machine B | GOFAI vs connectionism; one neuron; **the perceptron sketch** (21, live); the learning rule as code (22); 1958 · 1969 · 1986; XOR and the hidden layer; AlexNet and ImageNet; **the fit sketch** (26, live); fluent, fuzzy, opaque; quick check. | Multiple choice | Reload slide 21 once so the room sees the line swing and settle; then add an A among the Bs. Slide 26: sweep the mouse left to right. Cut 23 (say the dates aloud) and the detail of 25 if behind. |
| 1:12 | 29–33 | Rule-based, or adaptive? | Three pairs (Photoshop, Figma, the keyboard); four tests; *which of the four is rule-based?*; the sentence to carry across the break. | Multiple choice | If there is time, read four of the week-1 examples and have the room sort them by show of hands. Cut 31 to the four questions read aloud if behind. |
| 1:22 | 34 | **Break, 15 min** | Everyone logged into GenAI before leaving the room. | | |
| 1:37 | 35–41 | Move 37 | The film and the facts; how AlphaGo learned; Boden's conceptual space and Wiggins's R, T, E; two readings; *was Move 37 creative?*; Lee Sedol's retirement. | Short answer | Two minutes to write, five to argue: read a yes and a no, let two more respond. Cut 41 if behind. |
| 1:57 | 42–47 | Telling, and showing | The week-1 chairs again; a reference is an example, not a rule; the four moves on GenAI; what a reference can and cannot do; **live demo**: tell, show, show twice (slide 47). | | Gio live on GenAI with the edge chair; have the three results as screenshots in case it is slow. |
| 2:13 | 48–54 | **Activity: show it, don't tell it** | Section (1 min); round 1 alone, tell it (5); capture 1, everyone (3); round 2 in pairs, show it (8); round 4 in fours, off the prototype (10); capture 2 and the two walls side by side (4); what just happened (2). | 2 × image upload | Nicolò keeps time with the slide timers; the other three TAs walk. Details below. |
| 2:46 | 55–57 | Challenge 2, homework | The brief; the 3Blue1Brown video before week 4; bring the week-2 specs and a laptop. | | TAs stay 30 minutes. |
| 2:50 | | Buffer | | | |

If GenAI is slow, give round 2 ten minutes, let capture 1 be a phone photo of the screen, and cut slides 23, 31 and 41. If the room is fast, let two fours put their told chair and their shown chair side by side on screen and have the room say which inputs made each.

## The activity, in detail: Show it, don't tell it

The same chair three ways: told in words alone; shown with two pictures and three words in pairs; pushed off the prototype with references only, in fours. **Each round ends in an image; what goes into ClassPoint is an image, and the caption says which inputs made it.** A phone or a laptop on `genai.polyu.edu.hk` per pair at least, with an image model that accepts an image input (Flux or Qwen; the TAs confirm which before class).

1. **Alone, 5 minutes — tell it (slide 49).** Write a rule for a chair in at most twenty words: what makes yours a chair, and one thing it must never have. The prompt is the rule, word for word, no image attached, one run. Keep the image and the rule; look at what the model obeyed and what it ignored. Expect most "never" clauses to be ignored: rules select among the examples, they do not command.
2. **Capture 1, 3 minutes — everyone uploads, caption required (slide 50).** The wall: a hundred told chairs, most of them the prototype with an adjective. Read two captions with a "never" in them and check the picture against the rule. This is week 1's cup wall with the vocabulary of today: a prompt is a rule applied to the middle of the examples.
3. **Pairs, 8 minutes — show it (slide 51).** Swap phones; attach both round-1 images as references; prompt exactly "a chair like these", nothing else. Put the three images side by side and say out loud what the model took from each and what neither of you asked for. One more run with only the better reference; keep the image you would show a client. The sentence "this came from that picture" is the reflection's argument in miniature.
4. **Fours, 10 minutes — off the prototype (slide 52).** Join the pair behind you: four images on the table. Choose the two furthest from the middle that all four still call a chair; feed only those two; iterate by swapping a reference, never by adding words; three runs at most. Stop when the four agree that no dataset has this chair and that it is still a chair. Four people choosing which pictures to show the model is curating a dataset — week 11 in miniature. This round is the start of Challenge 2.
5. **Capture 2, 4 minutes — scribes only, caption required (slide 53).** One image per four; caption: the prompt and the references — how many, whose, from which round. Put the two walls side by side: told chairs on one side, shown chairs on the other, and ask which wall has more chairs that are not the prototype. Download the submissions: the chairs come back in week 5.
6. **Debrief, 2 minutes (slide 54).** The prompt was you telling: a rule applied to the middle; "never" did not survive. The reference was you showing: an example that moved the middle; it could pull and mix, it could not forbid. And the other way round: the reference could not ask for exactly four legs or a 40 cm seat. *The machine made every image. You chose the examples. That was the design.*

Round 4 is the start of Challenge 2 (slide 55): a picture from text and references — the image, the prompt, one to three reference images of their own, and one sentence on where the rule failed and the example worked (or the reverse), on Blackboard before week 4; the model must be named; the room votes in week 4.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room, help with the image input when a model refuses it, and note the best shown chairs for the week-4 awards.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Word cloud | AlphaGo. One word. | Warm-up on the homework film; screenshot it — it comes back on slides 39–40 as the room's first verdict. |
| 6 | Multiple choice | Challenge 1: which rule made the best picture? | The vote, on the spec alone; then the four sketches from Blackboard. Winners get a star. |
| 10 | Short answer | Define "cup" for a machine. | Read four: every definition admits the wrong thing or excludes the right one. The classical theory failing live; keep the answers for the mid-term question bank. |
| 17 | Multiple choice | Which sentence is prototype theory? | Quick check: B. |
| 28 | Multiple choice | 100% on training examples, 55% on new ones: what happened? | Quick check: B (memorising / overfitting). |
| 32 | Multiple choice | Which of the four tools is rule-based, machine A? | Quick check: B (Figma auto layout). Then sort four week-1 examples by show of hands. |
| 40 | Short answer | Was Move 37 creative? Yes or no, and one reason. | The debate; no correct answer. Keep with the word cloud: by week 12 the vocabulary has changed. |
| 50 | Image upload, everyone, caption required | Your told chair; caption: the rule | The wall of told chairs: the prototype with adjectives. |
| 53 | Image upload, one per four, caption required | The chair, and what made it | The shown chairs next to the told ones; downloaded for week 5 and the week-4 awards. |

All nine buttons are generated by the build (caption required on 50 and 53).

## What to keep after class

- The slide-4 word cloud and the slide-40 answers: the room's first position on machine creativity; they come back in week 11 (authorship) and week 12 (the recap), and the reflection asks for the same argument.
- The two walls (50 and 53) as screenshots and as downloads: week 5 opens with them when we push a model off the prototype properly (references, ControlNet, fine-tuning).
- The sorted list from slide 32 (the week-1 examples as rule-based / adaptive): it seeds week 8, using versus incorporating.
- Which Flux / Qwen model on GenAI accepted a reference image reliably, and how long a generation took: it goes in the week-5 plan.
