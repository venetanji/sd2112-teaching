# SD2112 · Week 5 lesson plan

**Images, intentions, iterations** · Friday 2 October 2026 (date confirmed by Gio; confirm room and teaching-team arrangements in Canvas) · lecture-workshop in the booked three-hour slot · deck: `week05-classpoint.pptx`; web/PDF paths follow the repository's Week 5 naming convention.

## Purpose

One personal identity connects three visual-making routes: **Machine A** executes coded shapes and parameters; **Machine B** generates an interpretation from learned patterns; **A+B** puts generated pixels inside a coded form or surface. Easel supplies the agent, project and tools, but students set the intent and judge each result. The coding agent is itself Machine B: **Machine B writes the code; Machine A executes it.** Applying generated pixels as a texture does not generate the geometry or a 3D model.

Gio teaches the full theory lecture first, with no opening Easel demo. After the break, a ten-minute logo/Easel/chat demonstration leads into installation and the shared brief, then a protected 40-minute activity: **10 + 10 + 15 + 5 = 40**. The target is three quick studies, not three finished logos. Comparison is the final five minutes within the 40-minute activity. The remaining booked time is flexible feedback, close and help—not more making.

By the end, students can:

- distinguish coded visual rules from image generation, even when the same learned agent helps with both;
- explain the distinct roles of GANs, CLIP, VAE representation and diffusion/flow generation;
- define one identity brief and two recognizable features shared across three routes;
- make a coded mark and demonstrate one controlled parameter change;
- inspect one generated interpretation and identify an unrequested model choice;
- reuse an image as a texture within a coded silhouette, then explain what each component controls;
- compare A / B / A+B against intent, without assuming the hybrid is best;
- keep evidence for Challenge 4 and the Week 7 reflection.

Keep the image-model theory visual and concise. Classic noise-prediction training is a teaching example, not every modern model's objective. The 2025 deck's useful caption/image and latent diagrams are adapted rather than treated as authoritative: CLIP aligns representations; it does not generate pictures or captions. Preserve the course's mediation question: how did the interface and model shape what was easy to specify, inspect or revise? Do not assign one fixed Ihde relation to image generation in general. The Verbeek core reading remains assigned.

## Lecture, followed by logo/Easel demonstration

Teach the theory before showing Easel. The lecture runs through slide 27: images and technology, Machine A's computer-art history, Machine B's image models, then the agent/tool bridge. Do not open with a product showcase or move the demo into the lecture.

After the break, use the ten-minute demonstration to show the course-logo still, Easel's three routes and the actual chat/video iterations from the course-logo experiment. Compare the intended nature/leaves → origami → circuits/fibres → upper-right-dot reveal with visible shape, motion and continuity. Ask whether a next intervention belongs in the prompt, reference inputs or workflow. Do not claim a successful final cut or controlled A/B comparison unless the selected evidence establishes it. No new video generation is required for preparation or the student activity. HTML is authored code rendered by the browser, not diffusion-generated media.

### Photography, apparatus and mediation inside the lecture

Reserve **8–10 minutes of the 60-minute lecture** for the five-slide block (slides 3–7 of the 47-slide sequence). Keep the lecture theory-first and the break, post-break demonstration, setup and 40-minute activity fixed. Make room by tightening narration around model diagrams; the actual chat/video evidence belongs in the post-break demonstration. Do not remove the CLIP distinction or core model concepts. This is a conceptual bridge, not a new exercise or assessment.

Use the sequence to move from Heidegger's account of equipment, through Ihde's postphenomenological mediation and Flusser's apparatus, to photographs as mediated choices, to a concrete comparison using the course's terms **Machine A, Machine B and A+B**. Keep the distinctions precise: Flusser's apparatus is not the later postphenomenological framework; Heidegger's equipment/readiness-to-hand is not interchangeable with his later account of revealing and enframing; enframing is not simply a photographic crop. Apply the same request across different machines to discuss what each makes easy to specify, notice or revise. Treat the course's A/B/A+B comparison as Gio's teaching application, not Ihde's original typology. A rule-based route can still involve learned code-writing and seeded randomness; a learned system can be repeatable. Neither label guarantees full transparency or independence from human choices.

The storefront photographs from Sham Shui Po and their repeated GAN outputs in Gio's thesis offer a grounded case: a dataset's recurring dark central corridor becomes a habit reproduced across generated results. Use it to ask how capture, selection, dataset and model shape what appears—not to claim a neutral photographic record or equate the camera crop with enframing. This adds no student task and does not change the shared identity brief.

### Machine A and the computer-art debate

A chapter divider on slide 9 leads into slides 10–14, which add roughly six minutes within the same lecture: the programmed image-making procedure; Bense's information/generative aesthetics; Nake's artist-programmer practice; exhibitions and public attention; Nake's 1971 critique of market fashion and technological mystification. Reuse the actual Nake works from Week 2. Keep Birkhoff distinct from Bense and Nees's *Schotter* distinct from Nake's work. Information aesthetics is not an entropy-equals-beauty formula. Nake's title does not mean he opposed all artistic use of computers: his essay supports investigation and socially meaningful communication. Machine A and B are different approaches, not a progress ladder.

Rebalance the hour: about five minutes opening/intent, nine minutes photography/mediation, six minutes computer-art history, thirty minutes model diagrams/examples, three minutes the first reflective answer and seven minutes agent bridge/recap. These are approximate narration allocations, not extra exercises.

The three case/reflection slides (33–35) fit inside the ten-minute post-break demo: the brief emerged through choices; a better prompt was not always the right repair; the agent coordinated learned proposals with explicit software. Select short saved excerpts, including failures and targeted revisions. V9 was delivered for review, not confirmed final creative acceptance. Technical validation is not aesthetic approval. Exact frame preservation concerns the lossless master, not the pixels of every lossy review copy. No new rendering or extra student task is required.

## Installation and access checks

Use [Easel Client / Easel Studio releases](https://github.com/venetanji/easel-client/releases). The release checked on 2 October is [v0.0.4](https://github.com/venetanji/easel-client/releases/tag/v0.0.4), with Windows x64 EXE/ZIP, macOS ARM64 DMG/ZIP and Linux x86_64 AppImage/DEB. No Intel Mac installer was listed. Recheck the available packages and match OS/architecture; the packaged installer is not the Node.js development setup. Do not bypass OS or institutional security controls.

Before class, test the installer and the complete path on a classroom-equivalent device:

1. Open Easel, create a project and run a simple HTML/SVG/Canvas mark.
2. Confirm the course-approved agent and image service, accounts, endpoint configuration, model, quotas and expected waits. A desktop install alone does not establish generation access or offline media support.
3. Generate one non-sensitive image, save it in the project, and successfully reuse that saved asset in a clipped SVG or masked Canvas composition. Use the actual project asset reference, not a guessed path.
4. For the optional 3D route, confirm the bundled Three.js kit under Settings > Kits and in project settings, and check WebGL. External URLs/CDNs are blocked by the viewer; use bundled kit/assets. **Three.js is optional**, not a prerequisite for completing the activity.
5. Prepare a working shared device, browser-based SVG/Canvas example and a supplied image for fallback. A supplied image must be labeled as supplied, not claimed as a student's generated result.

The syllabus names PolyU GenAI and Flux/Qwen models but does not establish student API credentials or Easel access. Confirm the authorized route rather than inventing an endpoint or distributing credentials. Keys belong only in the approved protected configuration, never chats, slides, screenshots or submissions. Installation and access support happen before the activity timer; students without access can pair while retaining their own brief and decisions. Students may also use an already working, permitted Open Design setup or another harness with the same brief. [PolyU GenAI](https://genai.polyu.edu.hk/) can support the image route; it is not a promised replacement for Easel's code/project workflow or API access. Record which tools supplied each part, and label any provided fallback assets.

## Before class (from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Test the chosen installer, authorized agent/image route, saved-image reuse and optional offline Three.js kit. Prepare the Canvas/SVG fallback and supplied texture. Test ClassPoint and open the web deck as backup. |
| Amber | Post the release/download link and deck through the course platform. Confirm the Challenge 4 submission destination and Week 6 logistics with Gio; do not infer a new deadline. |
| WU Zhao, MA Jie | Help with OS/package matching and project setup; organize shared devices. Preserve individual briefs and authorship. Keep personal data and credentials out of shared work. |
| Gio | Prepare the post-break logo/Easel demo and real chat/video examples. Confirm the two-feature brief, tool configuration and fallback. Do not let an asynchronous live job consume lecture or making time. |

## Run of show

Keep the three-hour booking's core sequence fixed: 60-minute theory lecture, ten-minute break, ten-minute logo/Easel/chat demo, fifteen-minute install and brief, then **40 minutes total** for making and comparison. The comparison is within those 40 minutes, not additional. From 2:15–3:00, use the remaining time flexibly for feedback, close and help; do not extend the making block. **Start the 40-minute clock only after** installation, tool checks and the shared brief are complete.

| Time | Segment | What happens | Notes |
|---|---|---|---|
| 0:00–1:00 | Theory lecture | Slides 1–27: roadmap and images/technology chapter; Heidegger → Ihde → Flusser → photography/mediation 3–7; designer intent 8; Machine A chapter/history 9–14; Machine B from 15; reflective question 25; agent diagram and A/B recap. | Keep all Easel material for after the break. Fit both conceptual/history blocks within the hour by tightening diagram narration. |
| 1:00–1:10 | Break | Ten minutes. | Keep release links and the backup device ready. |
| 1:10–1:20 | Logo/Easel/chat demo | Slides 29–35: moved title, Easel routes, logo/chat/video and three case/reflection slides. | Select short real excerpts. Added slides guide discussion within this ten-minute window; no extra demo or live generation wait. |
| 1:20–1:35 | Install and brief | Slides 36–39: installer and tool checks; identity brief; reflective boundary-setting question; 40-minute overview. | Outside the making timer. Pair or use prepared fallback rather than endless troubleshooting. |
| 1:35–2:15 | Activity: A / B / A+B / compare | Ten minutes coded mark, ten minutes generated interpretation, fifteen minutes combination, five minutes side-by-side comparison. | Protect the full 40 minutes, including comparison. One modest study per route; no extra prompt-writing or iteration block. |
| 2:15–3:00 | Flexible feedback, close and help | Support students, discuss outcomes, revisit Challenge 4 evidence and close. | Flexible use of booked time; not more making or an expanded activity. Submission details remain those confirmed in Canvas. |

## Activity: one identity, three ways of making it

**Shared brief, before the timer:** choose a name, nickname, invented character or personal symbol. Write one sentence about what it should communicate and two features that must remain recognizable. A fictional identity is welcome; a portrait, real name or personal photograph is not required. Keep this brief across all three routes; do not change the identity to rescue a weak result.

| Activity minute | Route | Make and inspect | Evidence |
|---|---|---|---|
| 0–10 | A · rules | Ask Easel's agent for a simple HTML/SVG/Canvas mark, without an image-generation call. Expose two controls and change one value. | Keep source code, one view and the parameter change. Machine B wrote the code; Machine A executed it. |
| 10–20 | B · learned image | Give the image tool the same brief and two features. Explore a material/texture/atmosphere, save one candidate and identify one unrequested choice. | Keep prompt, returned asset and model/tool details where available. Exact lettering is not a requirement. The observation question is inside these ten minutes. |
| 20–35 | A+B · combination | Reuse A's code and B's image. Clip the image or a chosen material region into the silhouette; adjust crop, scale or offset. | Keep the coded boundary, reused asset and hybrid view. Code controls geometry and placement; pixels supply the surface. Three.js is optional when the offline kit is verified. |
| 35–40 | Compare | Show A / B / A+B side by side: did combining the machines increase your control—or relocate it? | Identify one enforced decision, one delegated decision and one trade-off against the original brief. A hybrid can be worse. |

The agent is learned in every route; the labels describe how the visual artifact is made, not three different kinds of agent. Machine A can include seeded randomness. Adding a generated texture to coded geometry is not generating a 3D model. If B contains a whole mark, choose a material region rather than accidentally duplicating its shape inside A. No new generation is needed in A+B. Use project assets and offline kits rather than external URLs.

If a generation waits, submit it once and work on code while the accepted job runs. Do not resubmit it or silently extend the activity. If it fails, use a supplied image, label the substitution and critique what remains controllable. One imperfect study per route is enough; polish and iteration count are not the measure of success. Keep any reference/output uploads within the course privacy and permission rules.

## Challenge 4 · bring to Week 6

Use the personal-mark studies in a **side-by-side comparison layout**, then make and critique one deliberate revision. This connects the workshop to the existing syllabus wording: “a layout you could not design, generated, iterated and critiqued.” The page can be code-authored and use generated media; do not claim the image model generated the HTML/layout if it did not. This is not a change to assessment weights or deadlines.

Keep:

- the shared identity brief, two key features and A / B / A+B views;
- A's code and a parameter change; B's prompt, image and available model/tool details;
- the hybrid's source asset and mask/crop/texture decisions;
- one revised version and a critique tied to visible evidence;
- a short account of what was enforced, delegated, kept or rejected, including any supplied fallback assets.

Confirm submission destination and timing in Canvas; do not invent a deadline beyond bringing the work to Week 6. These records can support the Week 7 reflection on Machine A/B and the student's creative process.

## ClassPoint questions

Keep **four short answers total**. These are reflexive moments and possible seeds for the Week 7 argument, not attention checks, an extra quiz or four compulsory essay sections. Ask for a decision, evidence and a reason. The shared brief remains the reference point; an attractive output or fluent explanation is not proof of success. The last three answers happen within briefing, B and comparison respectively, without extending the timer.

| Slide | Type | Question | Use |
|---:|---|---|---|
| 25 | Short answer | When would a convincing image still fail your intention? | Within the lecture: distinguish appearance, matching words and serving a purpose; name evidence and a requirement. |
| 38 | Short answer | What should your mark never lose—even when a model reinterprets it? | Within briefing: identify an invariant and its significance; locate the boundary of delegated interpretation. |
| 42 | Short answer | What did the model's interpretation reveal about your own brief? | Within B's ten minutes: use a visible kept/rejected choice to examine ambiguity, assumptions or possibilities. |
| 44 | Short answer | Did combining the machines increase your control—or relocate it? | Within the final five minutes: compare all three against intent; explain a gain, loss and change in who decides. |

### Reminder of the individual reflection brief

Slide 46 turns the process record into an argument. The existing syllabus asks for about **1000 words** on AI's role in the student's creative process, particularly **Machine A versus Machine B**, with **at least three of their own weekly-challenge experiments from weeks 2–6, with images**, and a short note on **how AI was used in writing**. It is submitted through Canvas in Week 7. ClassPoint themes are optional ways into that argument; they do not change weighting, rubric or submission details. Encourage claim → evidence → interpretation rather than a tool list or unexamined praise.

## Sources and teaching material

- Gio's approved 1 October sequencing correction: theory lecture first (0:00–1:00), break (1:00–1:10), logo/Easel/chat demonstration (1:10–1:20), installation and brief (1:20–1:35), then making including comparison (1:35–2:15). The original standalone prompt exercise and 35-minute iteration block are replaced; 2:15–3:00 is flexible feedback, close and help, not more making.
- Approved 2 October review order (47 slides): 1 roadmap; 2 images/technology chapter; 3 Heidegger; 4 Ihde; 5 Flusser; 6 photography; 7 A/B mediation; 8 designer intent; 9 Machine A chapter; 10–14 Machine A history; 15 Machine B chapter; 16–17 GANs; 18 CLIP; 19 pipeline; 20 lantern; 21 VAE; 22 training; 23 generation; 24 modern models; 25 reflection; 26 agent diagram; 27 A/B recap; 28 break; 29 moved title; 30 Easel routes; 31 logo still; 32 chat/video; 33–35 case/reflection; 36 installation; 37 brief; 38 reflection; 39 overview; 40 A; 41 B; 42 reflection; 43 A+B; 44 comparison reflection; 45 Challenge 4; 46 reflection/process record; 47 close.
- Both five-slide lecture blocks fit within 60 minutes. The ClassPoint map is 25, 38, 42 and 44; no questions are added by either new block.
- Historical block: 2025 Week 2 PDF positions 28–30 and 36–37; Frieder Nake, [There should be no Computer Art](https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/), *Bulletin of the Computer Arts Society*, October 1971, pp. 18–19. Do not repeat the old PDF's unverified Berlin/first-exhibition claim.
- Current syllabus: image machines and mediation; Challenge 4; PolyU GenAI and named Flux/Qwen models; Verbeek (2015) core reading. The workshop supplies a comparison-layout route without silently rewriting assessment.
- Week 2 deck: “Machine B writes Machine A” and controlled parameters/seeds. Week 4 deck: tools and harnesses connect learned proposals with explicit software rules and permissions.
- Original 2025 slide sources: `SD2112 - AI in Design - Week 5.pptx` and `SD2112 - AI in Design - Master.pptx` under `references/onedrive-pptx/`; PDFs under `references/2025/`. GAN examples/competition are on Week 5 PDF pp. 45–46, Edmond portrait 47, caption/image alignment 48–50, noise/U-Net/VAE 51–54 and tools 55. PDF page positions are not printed slide numbers. The revised CLIP account corrects the old generation claim.
- Course-logo exploration: source a-plus-dot and forest/wall variant shared in September 2026. The exploratory edit is not a finalized logo or a guaranteed one-prompt result. The real chat/video iterations are discussed without inventing a successful final movie.
- Giovanni Lion, thesis chapter 5.1, [Photography](https://giovannilion.link/thesis/5-study-images.html#scope-1), and chapter 5.3, [Sham Shui Po storefront study](https://giovannilion.link/thesis/5-study-images.html#method-1): photography/dataset habits and repeated GAN outputs. [Chapter 3.1](https://giovannilion.link/thesis/3-methodology.html#sec:technological-mediation) provides the Ihde framework; the Machine A/B/A+B comparison is Gio's course application. [Chapter 6.1](https://giovannilion.link/thesis/6-study-text-to-image.html#scope-2) supplies the historical two-circle samples, not a new controlled A/B experiment. Present these as the thesis's situated case and extension, not as claims that Ihde authored the course typology.
- Lantern still: Easel Flux2-9B, 28 September 2026. On-slide intent is a teaching summary, not the verbatim prompt; it is not a controlled comparison.
- Easel [README](https://github.com/venetanji/easel-client#readme) and [v0.0.4 release](https://github.com/venetanji/easel-client/releases/tag/v0.0.4), checked 2 October: packaged installers, project image assets, HTML authoring, queued media generation and offline Three.js kit. Documented support is not proof of the installed classroom configuration.
- Modern model caveat: Black Forest Labs Flux documentation; Qwen Image documentation and Diffusers Qwen Image pipeline (`FlowMatchEulerDiscreteScheduler`). Classic noise prediction is explicitly labeled rather than presented as every current model's objective.
