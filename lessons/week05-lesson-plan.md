# SD2112 · Week 5 lesson plan

**Image machines and mediation** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week05-classpoint.pptx` (64 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week05/` (html deck with the four p5.js sketches running live; `SD2112-week05.pdf` next to it)

## Purpose of this session

For us:

1. Land **how an image model works** without maths: an image is destroyed by noise step by step (a rule), a network learns to undo one step (examples), sampling runs it backwards from pure noise — and the picture that comes out is the middle of everything it saw.
2. Show how the words get in (CLIP: words and pictures in one space, week 4's embeddings with pictures), where it all runs (the latent of an autoencoder) and the whole machine as a diagram (the ComfyUI vocabulary: checkpoint, text encoder, denoiser, VAE, sampler).
3. Close week 1's edge chair with the handles that push a model off its prototype — a reference, ControlNet, a LoRA — and name each as a rule laid over machine B or as more examples.
4. Give the reading its proper names: Ihde's four relations (embodiment, hermeneutic, alterity, background), Verbeek's three more (cyborg, immersion, augmentation), the force of a mediation (coercive, persuasive, seductive, decisive), and an AI version of each — the vocabulary of the group project's mediation brief.
5. Run the layout workshop: a layout generated from a brief and two references, and the question that runs through the afternoon — *what did the model decide that you did not?* — so that Challenge 4 starts in class.

For students, by the end of the class they can:

- explain diffusion in three moves (destroy, learn one step, run it backwards) and say what the network predicts (the noise, not the picture) and what the seed is;
- say what CLIP does (a word and its picture are neighbours in one space) and name the three ways a prompt reaches the picture (embedding, cross-attention, guidance);
- say where the denoising runs in Stable Diffusion (a 64 × 64 × 4 latent) and what the four parts of the machine are called in a tool's menu;
- choose between a prompt, a reference, ControlNet and a LoRA for a given job, and say what each keeps under their control;
- name Ihde's four relations with an AI example each, and Verbeek's three additions; place a product on the visibility / force grid;
- generate a layout from a brief and two references on PolyU GenAI, iterate with one change per prompt, keep the spec, and name the decision the model made silently.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: ClassPoint open, `week05-classpoint.pptx` loaded, join code on screen from slide 1. Fire the slide-4 short answer once as a test and reset it. Check the three Image Upload buttons (slides 55, 57 and 59; 57 and 59 have *caption required*). Open `genai.polyu.edu.hk` in a browser tab with **Flux** and **Qwen-Image**; run the slide-50 brief with "an A2 poster layout, flat, no photograph" in front of it on both, and note which one renders the title legibly — tell Gio. Keep the html deck open on the laptop: slides 12, 19, 24 and 34 run the sketches live and the PowerPoint only shows their stills. |
| Amber | Blackboard: post the deck link, the PDF, the brief (slide 50, also on the site), the reference instructions (slide 56), the iteration spec (slide 58) and the Challenge 4 brief (slide 62). Pull the four best Challenge 3 entries from Blackboard for slide 7 and paste their one-line "what the model decided" into `CHALLENGE3_ENTRIES` in `deck/week05.py` (anonymised: no names, no IDs; one line each), then rebuild the deck or hand the four lines to Gio — the slide shows placeholders until then. The prompt, the draft and the edit go on screen from the Blackboard page, not on the slide. Check whether the GenAI image models accept an image input this week and tell Gio: it decides how round 2 is worded (upload the references, or describe them). |
| WU Zhao, MA Jie | At the door: who has a laptop, who is logged into GenAI. Seat phone-only students next to laptop owners; the workshop needs one device per pair. Bring a stack of A4 and pens for round 2 (the grid is drawn by hand). During the activity, walk with the four questions of slide 52. |
| Gio | Fonts on the classroom PC (`tools/fonts/`). The week-4 data: the capture-2 wall and the Challenge 3 entries for slides 7–8 — check that slide 7 shows the four real one-liners, not the placeholders. Decide before class which of the cut-if-behind slides to keep (6, 15, 21, 27, 36, 37, 46). Backup: the html deck on a laptop — press `S` for notes; the sketches on slides 12, 19, 24 and 34 run live there. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops. Laptops or phones out from the start. | | |
| 0:03 | 3–9 | Last week, in your words | *Welch Labs, AssemblyAI: understood / not yet* (2 min, read six); week 4 in three lines; the Welch Labs video (cut if the answers are fine); the four Challenge 3 entries (replace with the real ones); the vote; the semester map. | Short answer; multiple choice | The "not yet" lines tell you which of chapters 2–4 to slow down on. |
| 0:17 | 10–16 | Noise → picture | The forward process (the figure); **live: noise and a toy denoiser** (slide 12); one training step; the three moves; AssemblyAI (cut if behind); quick check *what does the network predict?* | Multiple choice | Slide 12 is the core of the first half: move to pure noise, click, the chair comes back — say why (it learned one picture; a real model finds the middle of billions). |
| 0:35 | 17–21 | Words → pictures | CLIP's shared space and the diagonal; **live: one space** (slide 19, hover a word); three ways the prompt steers; Computerphile (cut if behind). | | Hover "boat", then the cat picture. Similarity is geometry, learned from company. |
| 0:47 | 22–29 | The latent | Autoencoders (786,432 → 16,384 numbers); **live: a latent space of chairs** (slide 24); the whole machine (slide 25 — the one to photograph); four parts, four names; the IBM autoencoder video (the UNet one is linked on the slide); the timeline; quick check *where does the denoising run?* | Multiple choice | Slide 25 is the ComfyUI diagram; everything after the break points back to it. Cut 27 if behind. |
| 1:03 | 30–38 | Off the prototype | The week-1 chairs (the middle); the edge chair and the three handles; four handles on a distribution; **live: a rule laid over a generator** (slide 34, draw); a reference, a rule, a style; ComfyUI (video); text to video (video); *write the rule, or show the examples — now both*. | | Cut 36 and 37 if behind. The four-handles figure is the bridge to the activity (round 2 = the first two handles). |
| 1:22 | 39 | **Break, 15 min** | Everyone logged into GenAI with an image model open before leaving the room. Pen and paper ready. | | |
| 1:37 | 40–48 | Mediation | Verbeek's sentence; Ihde's four relations (the figure, with the AI versions); Verbeek's three more; one model, four products; Netflix artwork (7 December 2017); the force of a mediation; quick check *Generative Fill is closest to…*; *a tool is never neutral; a model also has a middle*. | Multiple choice | Slide 42 is the core of the second half: have the room name an AI tool per relation before showing the violet line. Cut 46 if behind (keep the four words). |
| 1:57 | 49–52 | The layout workshop | The brief (poster or landing page; Flux or Qwen-Image; "a layout, flat, no photograph"); what a layout model decides; four questions for a generated layout. | | The fourth question — *which relation?* — is the bridge to the group project. |
| 2:07 | 53–61 | **Activity: the silent decisions** | Section (1 min); round 1 alone, brief only (5); capture 1, everyone (3); round 2 in pairs, two references (8); capture 2, one per pair, and the pulse by hands (3); round 4 in fours, three iterations and the spec (10); capture 3 and the wall (5); *which relation did your layout tool create?* (3); what just happened (2). | 3 × image upload; short answer | 40 minutes, as the section slide says. Nicolò keeps time; the other three TAs walk with the four questions. Details below. |
| 2:47 | 62–64 | Challenge 4, homework | The brief: the layout, the spec, the critique, on Blackboard before week 6; AltexSoft; a reflection draft; headphones. | | TAs stay 30 minutes. |
| 2:51 | | Buffer | | | |

If GenAI is slow, give round 2 ten minutes and cut slides 15, 21, 36 and 37. If the room is fast, let two fours read their caption aloud and have the room find the silent decision on the picture before it is named. If the image models take no image input this week, round 2 is done entirely in words (the panel on slide 56 has the sentence to use) — say so at the start of the round, not during it.

## The activity, in detail: The silent decisions

One brief — the week-13 poster fair, as an A2 poster or one screen of a landing page — laid out three ways by an image model on `genai.polyu.edu.hk` (Flux or Qwen-Image): from the brief alone, with two references, and iterated three times with a spec of what changed. **Each round ends in a picture; what goes into ClassPoint is an image, and the caption of the last one is the spec plus the decision the model made silently.** One device per pair at least; pen and paper for round 2.

1. **Alone, 5 minutes — the brief only (slide 54).** Paste the brief from the slide as it is, with "an A2 poster layout, flat, no photograph" in front. One image. Do not improve the prompt. Circle, in your head, everything on it that nobody asked for: that is the middle.
2. **Capture 1, 3 minutes — everyone uploads (slide 55).** The wall: a hundred posters from one brief, and most of them the same poster — a centred title, a geometric sans, a gradient, robots. The cup wall and the first-sentence wall, in layout. Point at three: which decisions repeat? Screenshot the wall.
3. **Pairs, 8 minutes — two references (slide 56).** Same brief, same model, new chat. Draw a grid on paper (columns, the title band, where the QR goes) and photograph it; pick three colours. If the model takes an image input, upload both with the brief; if not, describe them in words, exactly (the sentence is on the panel). Run it. **Which reference changed what?** The grid should move the geometry; the colours should move the surface. Expect the centred title to survive: the middle keeping what was not pinned down.
4. **Capture 2, 3 minutes — one per pair, caption required (slide 57).** The round-2 layout as it came, caption "grid: … · colours: …" — what each reference moved. Put this wall next to capture 1: the same brief without and with references. Then the pulse, by hands: *compared with round 1, the references…* changed the layout and we can say which did what (hoped for) / changed the surface, not the geometry (the common honest one: the colours landed, the grid did not) / were mostly ignored (ask what words they used). Anyone still waiting for an image gets a TA.
5. **Fours, 10 minutes — iterate, and keep the spec (slide 58).** Join the pair behind you; pick the better round-2 layout. Three iterations, one change each, in three prompts; after each, one line on what changed. Then find **the silent decision** — one thing the model decided that nobody asked for — and decide, as four, whether to keep it. New chat if the layout drifts.
6. **Capture 3, 5 minutes — scribes only, caption required (slide 59).** One image per four. Caption: the three changes, then "silent decision: …" — kept, or undone. Put the wall on screen next to captures 1 and 2; read two captions and have the room find the decision on the picture before it is named. Download the submissions: they seed Challenge 4 and are evidence for the reflection.
7. **Short answer, 3 minutes — which relation did your layout tool create? (slide 60).** One word (one of the seven), then one line why. Read six, sorted by relation. Most say alterity (they briefed it and argued with it); some say hermeneutic (they read what a poster should be off it). Both are right; the reason is the point. Then ask what relation the same model would create as an "auto layout" button — embodiment, or background. That is the mediation brief of week 8.
8. **Debrief, 2 minutes (slide 61).** The brief alone: one poster, a hundred times, with a robot on it. The references: a rule about geometry and a constraint on the surface moved the picture, and you can say which did what — that is authorship. The iterations: a critique is a list of silent decisions made loud. *The machine laid out every page. You decided what it had decided. That was the design.*

Round 4 is the start of Challenge 4 (slide 62): a layout you could not design — generated, iterated, critiqued — on Blackboard before week 6: the layout with its brief and references, the spec of changes (v1 to v4 at least, the model named), and a three-line critique (the silent decisions found, which were kept and why, the relation the tool created). The room votes in week 6.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber, WU Zhao and MA Jie walk the room with the four questions of slide 52, help with "no photograph" and with describing the references in words, and note the best captions for the week-6 awards.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Short answer | Welch Labs, AssemblyAI: one thing you understood, one you did not. | Which chapter to slow down on; keep the screenshot for the mid-term. |
| 8 | Multiple choice | Challenge 3: which entry gets the star? | The award; no correct answer. Note the split. |
| 16 | Multiple choice | What does the network learn to predict? | Quick check: A, the noise added at that step. |
| 29 | Multiple choice | Where does Stable Diffusion's denoising run? | Quick check: B, a 64 × 64 × 4 latent made by an autoencoder. |
| 47 | Multiple choice | Photoshop's Generative Fill is closest to which relation? | Quick check: A, embodiment — with the caveat in the notes (the prompt box is a flicker of alterity; the hidden fill is seductive). |
| 55 | Image upload, everyone | Your first layout, from the brief alone | The wall: one brief, a hundred posters, one poster. Screenshot it. |
| 57 | Image upload, one per pair, caption required | The round-2 layout, with what the grid and the colours moved | The reference wall next to the capture-1 wall: the same brief without and with references. The pulse is asked by hands. |
| 59 | Image upload, one per four, caption required | The layout, the three changes, and the silent decision | Layout–spec–critique triples: the seed of Challenge 4 and evidence for the reflection. |
| 60 | Short answer | Which relation did your layout tool create? | The first draft of every team's mediation brief (week 8); read six, sorted by relation. |

All nine buttons are generated by the build (caption required on 57 and 59).

## What to keep after class

- The capture-1 wall (slide 55) as a screenshot: the middle of a million layouts, for the week-6 recap and for week 11 (whose layouts were in the dataset).
- The capture-2 wall (slide 57) as a screenshot next to the capture-1 wall: the same brief without and with references, for the week-6 recap.
- The capture-3 submissions (slide 59) with their captions: the Challenge 4 seeds, the week-6 awards shortlist, and reflection evidence.
- The slide-60 relations: week 8 opens the mediation brief with them.
- The slide-4 answers: the mid-term draws on these videos.
- Which GenAI image model rendered the title legibly, and whether image input worked: it goes in the week-6 plan and decides how the week-11 LoRA exercise is set up.
