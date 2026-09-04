# SD2112 · Week 1 lesson plan

**Two ways to teach a machine** · three-hour lecture-workshop (about 170 minutes of content plus a 15-minute break) · deck: `week01-classpoint.pptx` (55 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week01/` (html deck; `SD2112-week01.pdf` next to it)

## Purpose of this session

For us:

1. Give a preview of the whole journey, so every later week lands in a place students already know.
2. Collect the level and the expectations of the room (studio, AI use, hopes and worries) and keep the data.
3. Land one concept that carries the semester: **rules vs examples**, on a chair — and let them feel it on a cup.
4. Establish the team, the rules and the tools, early, while everyone is fresh.

For students, by the end of the class they can:

- state the working definition of AI and say what "intelligent-like" and "computation" are doing in it;
- explain the two ways to teach a machine and give one design example of each (Auto Levels vs Generative Fill);
- say why a definition of "chair" leaks and why a model returns the prototype — and show a cup they pushed to the edge;
- tell using AI (process) from incorporating AI (product);
- know what is due, when, and who to ask.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Open ClassPoint on the classroom PC; open `week01-classpoint.pptx`; join code on screen from slide 1. Import the roster as the saved class (build it locally with `tools/roster.py` from the ID list; names are the last four digits + letter of the student ID; the file never goes on GitHub). Fire the slide-4 word cloud once as a test and reset it. **Add the two Image Upload buttons by hand** (ClassPoint tab → Image Upload) on slides 51 and 54 if they are not there yet; on 54 set *caption required*. |
| Amber | Check `genai.polyu.edu.hk` on a phone with a student login: pick an image model (Flux or Qwen), run "a cup", time it. Seating that allows pairs and fours. Blackboard: post the deck link, the PDF, the playlist and the homework. |
| Gio | Fonts on the classroom PC: install `tools/fonts/Inter-Variable.ttf` and `JetBrainsMono-Variable.ttf`, restart PowerPoint, check slide 1 shows Inter Black without a substitution warning. Fallback: Arial. Backup: the html deck on a laptop (press `S` for speaker notes) or the PDF. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---|---|---|---|---|
| 0:00 | 1–2 | Welcome | Course code, the eight stops, where the interactive moments are. | | Join code stays visible until stop 2. |
| 0:04 | 3–5 | Why are we here | Section, then the word cloud *why is AI relevant for design?*, then tools, products, job. | Word cloud (1 submission) | Screenshot the cloud for the week-2 recap. |
| 0:12 | 6–10 | Who are we | Gio's background; the three AI avatars; the team card (email, TAs 30 min before and after, Zhibin for the class as a whole). Two multiple-choice questions: closest field, AI use. | 2 × multiple choice | This is the level check. Note the splits; they steer weeks 2, 4 and 5. Say the absence rule out loud: let us know before, not after. |
| 0:22 | 11–12 | The journey | The semester map, you are here; week 13 is poster fair plus final quiz. | | |
| 0:28 | 13–19 | How this course works | Five components; reflection; group project; weekly challenges; three rules; then the anonymous hope and worry. | Short answer (names hidden) | Point at Blackboard for the rubrics. Read two worries aloud, keep the rest for week 2. |
| 0:42 | 20–25 | What is AI | Short answer in their own words (90 s); read four that disagree; the working definition; Babbage's engine; Lovelace's objection; intelligent vs creative (Wiggins, Turing). | Short answer | The course question lives in the Lovelace slide now: can a machine originate a design? |
| 0:56 | 26–32 | Two machines | Write the rule or show the examples; twelve parametric chairs (A); four generated chairs (B); Rosch's middle and edge; "ask for the edge, get the middle"; *which of these is a chair?* | Multiple choice | Slides 28–31 are the core of the class. The MC split is the point; there is no correct answer. |
| 1:12 | 33–38 | How we got here | Photoshop's three fills; the timeline; Nake 1965; how a network learns; Move 37 (play the chapter, 5 min); Belamy. | | Cut 35–36 if behind. |
| 1:30 | | **Break, 15 min** | | | |
| 1:45 | 39–43 | AI in design, now | Using vs incorporating; three cases: Coca-Cola, Netflix, Humane; *where did AI touch your design work this week?*; the playlist. | Short answer | Sort a few answers live into using and incorporating. Keep the list for week 3. |
| 2:02 | 44–47 | The designer's turn | Verbeek's line; the thing in between; designers as curators, guardrail setters, storytellers. | | Keep it to ten minutes; the activity needs the time. |
| 2:12 | 48 | Homework in one line | Laptop, AlphaGo, a p5.js account. The site and the playlist address. | | Not goodbye yet: the activity follows. |
| 2:14 | 49–55 | **Activity: push the machine to the edge** | Section (2 min); round 1 alone (4); capture 1, everyone (3); round 2 in pairs (5); round 4 in fours (6); capture 2 and the wall (6); what just happened (4). | 2 × image upload | Nicolò keeps time with the slide timers; Amber walks the room. Details below. |
| 2:44 | | Questions, buffer | | | TAs stay 30 minutes. |

If GenAI is slow, give round 1 six minutes and drop the Move 37 chapter. If the room is fast, let three groups read their prompts aloud before the debrief.

## The activity, in detail: Push the machine to the edge

Replaces the scavenger hunt and the pen-and-paper chair exercise. What Gio did with the chair on slides 29–31, the students do with a cup, on PolyU GenAI. Three rounds; **each round ends in a prompt, and what goes into ClassPoint is an image**. One device per pair is enough; `genai.polyu.edu.hk` works in a phone browser with a PolyU login; the image models are Flux and Qwen.

1. **Alone, 4 minutes — ask for a cup, then ask for the edge (slide 50).** Prompt 1: "a cup". Look: that is the middle. Prompt 2, in their own words: a cup that is still a cup but that nobody has seen. Keep both images.
2. **Capture 1, 3 minutes — everyone uploads the first cup (slide 51).** ClassPoint image upload. The wall shows a hundred near-identical cups: white, ceramic, a handle, three-quarter view. Nobody typed "white" or "handle". That is the prototype, and it is the dataset's prototype, not Hong Kong's: most cups in the room have no handle. Rosch in one screen.
3. **Pairs, 5 minutes — swap, judge, push further (slide 52).** Show the neighbour the edge cup. Is it still a cup? What did the model refuse to give up: the handle, the ceramic, the size, the shape? Write one prompt together that goes further without falling off the edge; run it; keep the better image. (Prompts are rules; the model is examples; the pull towards the middle is machine B ignoring the rule.)
4. **Fours, 6 minutes — choose what ships (slide 53).** Join the pair behind. Four images on the table; pick the one furthest from the middle that all four still call a cup. One last prompt if it improves. One person uploads. (Four people negotiating the edge of a concept is what a design team does with a brief.)
5. **Capture 2, 6 minutes — scribes only (slide 54).** ClassPoint image upload, one per four, **caption = the prompt, word for word** (set caption required). Put the wall on screen; point at three: still a cup? Show of hands on the most extreme one. Read the two best prompts. Download the submissions afterwards; week 5 revisits them.
6. **Debrief, 4 minutes (slide 55).** Prompts were rules, the model had the examples, and it pulled every cup towards its middle (week 3). Whose middle: the dataset's (weeks 9 and 11). Labov 1973: the same object is a cup with coffee in it and a bowl with soup in it; the edge moves with the context. The machine made every image; they decided which one was still a cup. Say the last line slowly.

TA roles: Nicolò keeps time with the slide timers and calls the round changes; Amber walks the room, helps with logins and nudges quiet fours; both note the best prompts for the week-2 recap.

## ClassPoint questions and what we do with the answers

| Slide | Type | Question | Use |
|---|---|---|---|
| 4 | Word cloud | Why is AI relevant for design? | Opening temperature; week-2 recap. |
| 9 | Multiple choice | Which are you closest to? | Steers the examples in weeks 2–6 (type and campaigns vs product form vs feeds). |
| 10 | Multiple choice | How much have you used AI in your design work? | Level check. Mostly A/B: slow down the tool weeks. Many D: pair them with beginners in the challenges. |
| 19 | Short answer, names hidden | One hope and one worry | Expectations and anxieties; map each worry to the week that addresses it and tell them in week 2. |
| 21 | Short answer | What is AI? One sentence | Read the disagreeing ones; keep for the week-3 recap. |
| 32 | Multiple choice | Which of these is a chair? | Demonstrates fuzziness; no correct answer. |
| 42 | Short answer | Where did AI touch your design work this week? | The new "AI in the wild": the list seeds the week-3 categorising exercise. |
| 51 | Image upload, everyone | Your first cup ("a cup") | The prototype wall. Screenshot it. |
| 54 | Image upload, one per four, caption required | The cup that ships, with its prompt | Prompt–image pairs for week 5 (pushing a model off the prototype) and week 9 (whose middle). |

The two image-upload buttons are not generated by the build (the ClassPoint model for that activity type is not in the kit yet): add them in PowerPoint through the ClassPoint tab once and save; the build prints a reminder. Every other button is generated.

After class, export the ClassPoint results and keep them in a private folder (they are student data): the two multiple-choice splits, the cloud, the worries, the two image sets. Bring the numbers to the week-2 planning.

## Contingencies

- **GenAI down or slow.** Any image tool students already have (Bing Image Creator, Firefly, Midjourney); or run prompts from the lecturer's machine on the projector, taking prompts from the room, and skip capture 1.
- **ClassPoint image upload fails.** Students AirDrop or email the image to a TA, or post it in a Blackboard discussion thread; the wall becomes a quick scroll on the projector.
- **ClassPoint fails altogether.** Word cloud becomes hands up; short answers become paper, collected by the TAs.
- **Projector or PC fails.** The html deck runs from any laptop or phone browser; speaker notes with `S`, overview with `O`. The PDF works anywhere.
- **Fonts missing.** PowerPoint substitutes Arial automatically; the deck still reads. Install the two variable fonts from `tools/fonts/` for the next class.
- **Running late.** Cut in this order: 35–36 (Nake, how it learns), the Move 37 chapter, then shorten the three cases to one minute each. Do not cut the activity.
- **Running early.** Let more groups read their prompts; ask the room for a fourth "case from the last month".

## After class

- TAs stay 30 minutes: accounts, laptops, the setup items (ClassPoint name, Blackboard, the p5.js editor, GenAI login).
- Post on Blackboard: the deck link and PDF, the playlist, the homework (AlphaGo and the four short art films before week 3; bring a laptop).
- Download both image-upload sets and the ClassPoint exports; file them privately for weeks 2, 3, 5 and 9.
- Note the two level-check splits and adjust the week-2 exercise.

## Materials

- `week01-classpoint.pptx` (ClassPoint-ready: animations, ait4x master, buttons) and `week01.pptx` (plain, editable): from the *Build PowerPoints* workflow artifact, or `python tools/build_all.py --pptx`.
- `venetanji.github.io/sd2112-teaching/week01/` — the html deck with speaker notes, and `SD2112-week01.pdf` without the ClassPoint buttons.
- The saved-class roster (built locally, never committed); the two variable fonts; a laptop with the html deck as backup.
