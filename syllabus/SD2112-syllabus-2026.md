# SD2112 · Artificial Intelligence in Design

**Syllabus · Semester 1, 2026/27 · PolyU School of Design**

> Can a machine originate a design? By week 13 you will have an answer you can defend.

## At a glance

| | |
|---|---|
| Subject code | SD2112 |
| Title | Artificial Intelligence in Design |
| Credits / level | 2 credits · level 2 · no prerequisites |
| Programme | BA (Hons) Scheme in Design |
| Semester | Semester 1, 2026/27 · 13 teaching weeks · the final quiz is in week 13 |
| Class size | ~114 students |
| Format | One three-hour lecture-workshop block a week, with a break. Lectures with ClassPoint questions, in-class activities, a weekly making challenge. |
| Help desk | Teaching assistants are in the room **30 minutes before and 30 minutes after** every class. |
| Platforms | Blackboard (submissions, rubrics, announcements) · ClassPoint (in-class questions; join with the last four digits and the letter of your student ID, e.g. `3456A`) · PolyU GenAI (`genai.polyu.edu.hk`: language and image models, including Flux and Qwen, with your PolyU login) · course site with the slides and PDFs: `venetanji.github.io/sd2112-teaching` · video playlist: `youtube.com/playlist?list=PLU58DFEI5YDQ` |
| Study effort (subject form) | Lectures 17 h · tutorials and labs 9 h · reading 30 h · assignments 22 h · exam preparation 12 h · total 90 h |

## Teaching team

| Role | Who | What to come to them for |
|---|---|---|
| Lecturer | **Giovanni Lion** (PhD, computational creativity) · giovanni.lion@polyu.edu.hk | Lectures, briefs, grading, the course question. Ask in class first, then by email. |
| Teaching assistant | **Nicolò Azzolin** | Tools, accounts, code, the weekly challenges, the video playlist (which Nicolò compiled). In the room 30 min before and after class. |
| Teaching assistant | **Amber** | Assignments, the group project, feedback on work in progress. In the room 30 min before and after class. |
| Teaching assistant | **WU Zhao** | Anything about the class. In the room 30 min before and after class. |
| Teaching assistant | **MA Jie** | Anything about the class. In the room 30 min before and after class. |
| Class coordinator | **Zhibin Zhou** · zhibin.zhou@polyu.edu.hk · office V502b | Anything about the class as a whole: admin, timetabling, the group as a group. |

**If you cannot come to a class, let the teaching team know before it starts**: an email to the lecturer or a message to a TA. That is what keeps your participation mark.

Lecturer: giovanni.lion@polyu.edu.hk. Coordinator: zhibin.zhou@polyu.edu.hk, office V502b. TA contact details are on Blackboard.

## What this course is about

AI is now in the tools designers use, in the products designers make, and in the definition of the job. This course gives you a working understanding of what these systems are, hands-on experience using them in your own process, and a vocabulary for designing products that have a model inside them.

The whole course runs on one distinction: there are **two ways to teach a machine** what something is. You can **write the rule** (symbolic AI, parametric design, expert systems: exact, explainable, brittle) or you can **show it examples** (machine learning, deep learning, diffusion models, language models: fluent, fuzzy, unable to say why). Every AI feature you will meet is one of these, or a mix. The designer's job increasingly sits between them: choosing the examples, setting the rules, and deciding what ships.

The theoretical spine comes from the lecturer's research on concept formation in computational creativity (theories of concepts, the history of GOFAI and connectionism, non-human creativity) and from the philosophy of technology (Ihde and Verbeek's technological mediation): a tool is never neutral, and designing things is designing human existence.

## Intended learning outcomes

On completing the subject you will be able to:

1. **Explain**, in non-technical terms, how rule-based and data-driven AI systems work, how they differ, and where each appears in design tools and products.
2. **Use** current AI tools (language, image, sound) within a design process, critically and with documented authorship.
3. **Analyse** a product that incorporates AI in terms of the human–technology relation it creates, the data it depends on, its biases and its accountability.
4. **Design and present** a product concept that incorporates AI, with a research-based account of its ethical and social implications.
5. **Argue** a position on machine creativity and on the designer's role in AI-mediated work, using evidence from your own practice and from the literature.

## Structure: four modules

| Module | Weeks | Question |
|---|---|---|
| 1 · What is AI? | 1–3 | Where does "intelligent-like behaviour" come from: rules, or examples? |
| 2 · AI for the creative process | 4–6 | What do language, image and sound models do to how you make things? |
| Mid-term | 7 | Quiz · project pitches · team forming · reflection due |
| 3 · Incorporating AI in products | 8–10 | What changes when the model is inside the thing you design? |
| 4 · The designer's turn | 11–12 | What is left for the designer: curating, guardrails, language as interface |
| Showcase | 13 | Poster fair · final quiz |

## Weekly plan

Dates: confirm against the PolyU academic calendar for 2026/27 and add them to Blackboard. Readings and videos are due **before** the class listed.

| Wk | Topic | Key examples and references | In class | Make / due |
|---|---|---|---|---|
| 1 | **Two ways to teach a machine.** Course intro and the journey; a working definition of AI; Lovelace's objection and Turing's question; rules vs examples, with chairs; using AI vs incorporating AI; the designer's turn. | Lovelace Note G (1843); Turing (1950); Nake, *Homage to Paul Klee* (1965); Rosch & Mervis (1975) typicality; Photoshop's Auto Levels vs Content-Aware Fill vs Generative Fill; Netflix artwork personalisation; Coca-Cola's 2024 generative holiday ad; the Humane AI Pin; Verbeek (2015). | ClassPoint: level and expectation check (studio, AI use, one hope and one worry). Activity **Push the machine to the edge**: 1-2-4 on a cup — each round ends in a prompt, tested on PolyU GenAI (Flux or Qwen), and what you submit to ClassPoint is an image. | Set up ClassPoint, Blackboard and a p5.js editor account; log into PolyU GenAI. Watch *AlphaGo* and the four short art films on the playlist before week 3. |
| 2 | **Rules that make things.** Symbolic AI (machine A): if-then, ELIZA, expert systems, the knowledge bottleneck; instructions as art: Young, Fluxus scores, Cage, Tinguely, Kaprow, Sol LeWitt's wall drawings, Molnár; Bense's information aesthetics; Nees's *Schotter* and Nake's *Walk-Through-Raster* broken down into their rules and drawn step by step; 10 PRINT; fractals (Koch's curve) and L-systems; parametric design (Grasshopper, variable fonts). p5.js as a sketchbook that executes. **Specs and prompts for coding:** a rule written in words (rule, chance, numbers, constraints, output), executed by a language model into p5.js; what you said vs what you meant. | Young, *Composition 1960 #10*; Brecht, *Drip Music* (1959); Cage, *Water Walk* (1960); Tinguely, *Homage to New York* (1960); Kaprow, *Fluids* (1967); LeWitt, *Wall Drawing 118* (1971) and "the idea becomes a machine that makes the art" (1967); Nees, *Schotter* (c. 1968); Nake, *Walk-Through-Raster* (1966); Illiac Suite (1957); *10 PRINT* (1982); Weizenbaum's ELIZA (1966); MYCIN and XCON. | p5.js in the slides: Schotter, Walk-Through-Raster, Koch's curve and LeWitt's points as editable sketches with sliders — change a number, see the picture change. Exercise **One spec, one twist**: LeWitt's Wall Drawing 118 (ten points) executed by a language model on PolyU GenAI into p5.js, then one twist of the pair's own, iterated on the spec rather than the code; one image per pair into ClassPoint, the spec as the caption. | **Challenge 1:** a picture from rules — one rule, one random number, the spec plus a p5.js share link and a screenshot on Blackboard. Awards in week 3. |
| 3 | **Learning from examples.** Theories of concepts: classical vs prototype theory; GOFAI vs connectionism; perceptron → backpropagation → deep learning; rule-based vs adaptive systems in design tools; non-human creativity and Move 37. | Rosch (1975); Labov (1973) on cups and bowls; Rosenblatt (1958); Rumelhart, Hinton & Williams (1986); AlexNet (2012); *AlphaGo* (film); Wiggins (2006); the week-1 cups revisited. | Image workshop: generate and edit with a text prompt and reference images; sort the examples the class collected in week 1 into rule-based and adaptive; Move 37 debate. | **Challenge 2:** a picture from text and references — an image generated with diffusion models from a text prompt and images as reference. |
| 4 | **Language machines.** How LLMs work (tokens, embeddings, transformers, base vs instruction-tuned); hallucination and sycophancy; agents and tools; prompting as briefing. | 3Blue1Brown, *LLMs explained briefly*; OpenAI on hallucination and sycophancy; a design brief written three ways. | Prompt-engineering workshop: write a brief, automate a workflow, compare. | **Challenge 3:** a brief drafted by a language model from your prompt, then edited by you. Show both. |
| 5 | **Image machines and mediation.** CLIP, diffusion, latent space, ControlNet and LoRA; pushing a model off the prototype; Ihde's four human–technology relations and their AI versions. | Welch Labs, *How AI images work*; AssemblyAI on diffusion; Computerphile on CLIP; ComfyUI models; **Verbeek (2015), *Beyond Interaction*** (core reading); Netflix artwork; the week-1 chairs and cups. | Layout workshop and critique: a layout generated from a brief and references; what did the model decide that you did not? | **Challenge 4:** a layout you could not design, generated, iterated and critiqued. |
| 6 | **Sound machines.** What sound and music are (spectrograms, MIDI, melody, harmony, rhythm); data-driven music and voice generation; authenticity and copyright. | AltexSoft, *How AI sound and music generation works*; Suno, AIVA; UMG v. Udio settlement (2025). Mock quiz. | Music-generation workshop: thirty seconds of sound for a product. | **Challenge 5:** thirty seconds of sound. Reflection draft check with the TAs. |
| 7 | **Mid-term.** Quiz (weeks 1–6 and the playlist); project pitches; team forming. Guest lecture slot if available. | | Mid-term quiz (10%). Pitch session: individuals present early ideas; teams of 4–5 form. | **Individual reflection due (20%).** |
| 8 | **AI as design material.** Using vs incorporating; a product that decides something for each person; the double diamond with a model inside; collaborative workflows (Scrum, Git). | Spotify AI DJ; Netflix; Duolingo's AI-first lessons; the Humane AI Pin and Rabbit R1 as cautionary cases. | Team brainstorming and concept sketching; the group brief. | **Group proposal** (one page: the decision the product makes, for whom, with what data). |
| 9 | **Data, bias and privacy.** How data powers adaptive systems; data, label, algorithmic and interaction bias; data minimisation, anonymisation, consent. | *Coded Bias* (watch before class); the week-3 datasets revisited for bias. | AI-neutrality debate: can a model be neutral? Ethics mapping on each team's concept. | **Concept board**; a bias register for your product. |
| 10 | **Recommendation systems.** Embeddings and similarity search; collaborative vs content-based filtering; echo chambers; the feed as a designed mediation. | YouTube, TikTok, Spotify; the attention-trap problem. | Hands-on: a simple similarity search over text or images; test and reflect. | **Prototype v1** of the interaction (paper, Figma or code). |
| 11 | **Curators of outputs and datasets.** Output selection and gatekeeping; fine-tuning and LoRA datasets; authorship and ownership (Thaler cases, Google Books, transformative use). | Edmond de Belamy (2018); the LoRA dataset exercise; US Copyright Office and court decisions on AI authorship. | LoRA dataset exploration and its ethics; poster lab begins. | **Draft poster**; the one-page **mediation brief**. |
| 12 | **Language as an interface.** Rules-based vs generative chatbots; agents; trust, transparency and opacity (Van Den Eede); designing the mediation: explainability, participatory design, auditing. Course recap. | IBM, *Generative vs rules-based chatbots*; Van Den Eede (2011); the Turing test revisited. | Chatbot design exercise: prototype an assistant for your product; mock poster session. | **Final poster and video** ready. |
| 13 | **Poster fair and final quiz.** Group projects on A0 posters with 3–5 minute videos; peer and instructor feedback. The final quiz takes the last part of the three-hour class. | | Graded showcase (40%). Final quiz (20%): multiple choice on the whole course. | **Group project due.** |

## Assessment

Weights follow the approved subject description form.

| Weight | Component | What it is | When |
|---|---|---|---|
| 10% | Participation | Come to class, or let the teaching team know before the class. Answer in ClassPoint: attendance plus activity stars. Weekly-challenge awards add stars. | Weekly |
| 20% | Individual reflection | *The role of AI in your creative process, with particular attention to the difference between rule-based and adaptive systems.* About 1000 words. Evidence: at least three of your own experiments from the weekly challenges (weeks 2–6), with images. Ends with a short process note on how you used AI to write it. Submitted on Blackboard. | Week 7 |
| 10% | Mid-term quiz | Multiple choice on weeks 1–6 and the playlist videos. | Week 7 |
| 40% | Group project | Teams of 4–5. **Design a product or service that incorporates AI**: a model decides something for each person, and you account for what that does to them. Deliverables: an **A0 poster** (research and concept), a **3–5 minute video** (how it works), and a **one-page mediation brief** (which human–technology relation you are building, what data it needs, where it is biased, what the guardrails are). Shown at the poster fair. | Week 13 |
| 20% | Final quiz | Multiple choice on the whole course. In class, after the poster fair. | Week 13 |

### Individual reflection rubric (20%)

| Criterion | A (excellent) | B (good) | C (satisfactory) |
|---|---|---|---|
| Understanding of concepts: rule-based vs adaptive (30%) | Explains both kinds of system accurately and in depth; shows nuanced understanding of how they differ and what that means in a creative process. | Describes both correctly; minor gaps or oversimplifications. | Basic understanding with notable gaps; may address only one kind. |
| Argument and critical thinking (30%) | A clear stance on AI's role in creativity, well structured and supported by reasoning. | Coherent, somewhat supported argument; lacks depth in places. | Mostly opinion; argument underdeveloped. |
| Evidence and examples (20%) | Several relevant, well-explained examples from your own experiments and from tools, cases or literature, integrated into the argument. | Some examples, thinly explained or loosely connected. | Minimal examples, mentioned without explanation. |
| Clarity, structure and style (10%) | Clear, organised, easy to follow, few errors. | Generally clear; minor lapses. | Understandable but uneven. |
| Engagement and originality (10%) | Original thought and curiosity; goes beyond surface commentary. | Some independent thought. | Mostly descriptive. |

The process note (how AI was used in writing) is required; a missing note costs one grade band on clarity and style. Invented citations fail the assignment.

### Group project rubric (40%)

| Criterion | A (excellent) | B (good) | C (satisfactory) |
|---|---|---|---|
| Research and contextual analysis (30%) | Thorough, well-structured research from multiple credible sources; the product is clearly situated in the AI-and-design discourse. | Solid research; good awareness of context; some areas thin. | Few sources; shallow context. |
| Ethical and sociological impact (30%) | Insightful, nuanced account of implications, risks and opportunities; the mediation brief names the relation, the data, the bias and the guardrails convincingly. | Good consideration of ethics and society; not comprehensive. | Generic or shallow mention. |
| Communication and poster design (20%) | Visually clear, engaging, professional; well organised; balance of visuals and text. | Well structured; minor layout issues. | Cluttered or unrefined. |
| Video presentation (10%) | Clear, well paced, explains the product and its implications; polished. | Clear and mostly effective; minor pacing issues. | Communicates basics; lacks polish. |
| Team collaboration and process documentation (10%) | Strong shared effort; transparent, well-documented process; roles clear. | Good teamwork; some documentation. | Uneven; little documentation. |

### Weekly challenges (weeks 2–6)

Small, low-stakes, one per week: a picture from rules · a picture from text and references · a brief, automated · a layout you could not design · thirty seconds of sound. Bring it to the next class; the room votes; winners are shown and get a participation star. All five are evidence for the reflection. The TAs help before and after class.

## Policies

- **Attendance.** Participation is attendance plus ClassPoint activity. If you cannot attend, let the teaching team know before the class starts (an email to the lecturer, or a message to a TA). Silent absence costs the mark; a message does not.
- **AI use.** Allowed in every assignment, and expected. You must disclose which tools you used and how, in a short process note. You are the author: you are responsible for accuracy, sources and taste. Fabricated references or facts are treated as academic misconduct.
- **Academic integrity.** PolyU regulations apply. Group work must show each member's contribution.
- **Late work.** Per programme policy; ask the lecturer before the deadline, not after.
- **Accessibility.** Slides are published as an HTML deck and on Blackboard before class; recordings and captions per school practice. Tell the team early about anything we can adapt.

## Readings, films and resources

Core (short, assigned):

- Verbeek, P.-P. (2015). *Beyond interaction: a short introduction to mediation theory.* Interactions 22(3), 26–31. (Week 5.)
- Van Den Eede, Y. (2011). *In between us: on the transparency and opacity of technological mediation.* Foundations of Science 16, 139–159. (Week 12.)
- Lion, G. Thesis, chapter 2, literature review: theories of concepts; philosophy of technology; GOFAI, generative art, connectionism, deep learning; non-human creativity; the computational-creativity literature. giovannilion.link/thesis/2-Litreview (Weeks 2–3 background.)

Background (dip in):

- Lovelace, A. (1843). Notes on the Analytical Engine, Note G. · Turing, A. (1950). *Computing machinery and intelligence.* · Rosch, E. & Mervis, C. (1975). *Family resemblances.* · Wiggins, G. (2006). *A preliminary framework for description, analysis and comparison of creative systems.* · Boden, M. (2003). *The Creative Mind.* · Nake, F. on the 1965 exhibitions. · Bandyopadhyay & Forster (2011), *Philosophy of Statistics* (subject form reading).

Films: *AlphaGo* (2017; before week 3) · *Coded Bias* (2020; before week 9).

Playlist (compiled by Nicolò, in course order): LLMs explained briefly (3Blue1Brown) · Diffusion models explained (AssemblyAI) · How AI images and videos work (Welch Labs) · UNet · Autoencoders (IBM) · CLIP (Computerphile) · Text-to-video (Google Research) · ComfyUI models · AI sound and music (AltexSoft) · Generative vs rules-based chatbots (IBM) · AlphaGo · Illiac Suite · Cage, *Water Walk* · Tinguely, *Homage to New York* · Kaprow, *Fluids*.

Tools you will need an account for: ClassPoint (student app), Blackboard, the p5.js web editor, PolyU GenAI (`genai.polyu.edu.hk`, your PolyU login: it covers image generation with Flux and Qwen, and language models). Adobe Firefly or Bing Image Creator work as alternatives. Everything else is provided in class.

## What changed from 2025

- Week 1 has a new spine (two ways to teach a machine, on chairs), a new activity (*Push the machine to the edge*: 1-2-4 on a cup, prompts on PolyU GenAI, images into ClassPoint; it replaces the scavenger hunt) and a built-in level and expectation check.
- The class is three hours, so the final quiz moves into week 13 after the poster fair; there is no week 14 session.
- Examples are designer-facing throughout: Photoshop's three fills, Netflix artwork, the Coca-Cola ad, the Humane Pin, parametric chairs, Belamy, LeWitt and the Fluxus scores.
- The weekly challenges (previously informal "awards") are formalised as five small makes that feed the reflection.
- The group project adds a one-page mediation brief, so the theory (Ihde, Verbeek, bias, guardrails) shows up in the deliverable.
- Four teaching assistants (Nicolò Azzolin, Amber, WU Zhao, MA Jie) hold a help desk 30 minutes before and after each class; Zhibin Zhou coordinates the class; absences go to the teaching team.
- The playlist is mapped week by week; quizzes draw on it.
- Week 2 teaches specs: LeWitt's rule executed by a language model into p5.js, then twisted and iterated by each pair; the html deck runs the p5.js sketches live, and the code on the slides is editable.
- Slides are built from one source into an HTML deck and a PDF (GitHub Pages) and a ClassPoint-ready PowerPoint.
