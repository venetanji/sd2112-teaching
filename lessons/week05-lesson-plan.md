# SD2112 · Week 5 lesson plan

**Images, intentions, iterations** · Friday 2 October 2026 (date confirmed by Gio; confirm room and teaching-team arrangements in Canvas) · lecture-workshop in the booked three-hour slot · deck: `week05-classpoint.pptx`; web/PDF paths follow the repository's Week 5 naming convention.

## Purpose

One personal identity connects three visual-making routes: **Machine A** executes coded shapes and parameters; **Machine B** generates an interpretation from learned patterns; **A+B** puts generated pixels inside a coded form or surface. Easel supplies the agent, project and tools, but students set the intent and judge each result. The coding agent is itself Machine B: **Machine B writes the code; Machine A executes it.** Applying generated pixels as a texture does not generate the geometry or a 3D model.

Gio opens with a five-minute Easel showcase, then lectures for roughly 55 minutes. After the break, installation and the shared brief precede a protected 40-minute activity: **10 + 10 + 15 + 5 = 40**. The target is three quick studies, not three finished logos. There is no separate prompt-clarification exercise or extra iteration block; deliberate changes happen within the three tasks.

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

## Opening showcase and lecture examples

Show one prepared identity in three forms: coded HTML/SVG/Canvas graphics, a generated interpretation and a combination. This is a five-minute invitation to the lecture, not installation or a live generation wait. Keep saved assets ready; do not claim an illustrative route is a documented successful experiment. Easel's image, video and HTML capabilities remain part of the tool discussion; HTML is authored code rendered by the browser, not diffusion-generated media.

During the lecture, Gio opens the actual chat and selected video iterations from the course-logo experiment. Compare the intended nature/leaves → origami → circuits/fibres → upper-right-dot reveal with visible shape, motion and continuity. Ask whether a next intervention belongs in the prompt, reference inputs or workflow. Do not claim a successful final cut or controlled A/B comparison unless the selected evidence establishes it. No new video generation is required for lecture preparation or the student activity.

## Installation and access checks

Use [Easel Client / Easel Studio releases](https://github.com/venetanji/easel-client/releases). The release checked on 1 October is [v0.0.1](https://github.com/venetanji/easel-client/releases/tag/v0.0.1), with Windows x64 EXE/ZIP, macOS ARM64 DMG/ZIP and Linux x86_64 AppImage/DEB. No Intel Mac installer was listed. Recheck the available packages and match OS/architecture; the packaged installer is not the Node.js development setup. Do not bypass OS or institutional security controls.

Before class, test the installer and the complete path on a classroom-equivalent device:

1. Open Easel, create a project and run a simple HTML/SVG/Canvas mark.
2. Confirm the course-approved agent and image service, accounts, endpoint configuration, model, quotas and expected waits. A desktop install alone does not establish generation access or offline media support.
3. Generate one non-sensitive image, save it in the project, and successfully reuse that saved asset in a clipped SVG or masked Canvas composition. Use the actual project asset reference, not a guessed path.
4. For the optional 3D route, confirm the bundled Three.js kit under Settings > Kits and in project settings, and check WebGL. External URLs/CDNs are blocked by the viewer; use bundled kit/assets. **Three.js is optional**, not a prerequisite for completing the activity.
5. Prepare a working shared device, browser-based SVG/Canvas example and a supplied image for fallback. A supplied image must be labeled as supplied, not claimed as a student's generated result.

The syllabus names PolyU GenAI and Flux/Qwen models but does not establish student API credentials or Easel access. Confirm the authorized route rather than inventing an endpoint or distributing credentials. Keys belong only in the approved protected configuration, never chats, slides, screenshots or submissions. Installation and access support happen before the activity timer; students without access can pair while retaining their own brief and decisions.

## Before class (from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Test the chosen installer, authorized agent/image route, saved-image reuse and optional offline Three.js kit. Prepare the Canvas/SVG fallback and supplied texture. Test ClassPoint and open the web deck as backup. |
| Amber | Post the release/download link and deck through the course platform. Confirm the Challenge 4 submission destination and Week 6 logistics with Gio; do not infer a new deadline. |
| WU Zhao, MA Jie | Help with OS/package matching and project setup; organize shared devices. Preserve individual briefs and authorship. Keep personal data and credentials out of shared work. |
| Gio | Prepare the short opening showcase and real chat/video examples. Confirm the two-feature brief, tool configuration and fallback. Do not let an asynchronous live job consume lecture or making time. |

## Run of show

Follow Gio's actual rhythm rather than filling every minute of the three-hour booking. The approximate core is 130 minutes including a ten-minute break and a fifteen-minute setup/brief; remaining booked time is flexible installation, individual help or discussion, not an expanded making exercise. Setup may shift the later clock times. **Start the 40-minute clock only after** installation, tool checks and the shared brief are complete.

| Time | Segment | What happens | Notes |
|---|---|---|---|
| 0:00–0:05 | Opening Easel showcase | Show one mark as code, generated pixels and a combination. | Use prepared outputs. Give students something to wonder about; no installation yet. |
| 0:05–1:00 | Lecture | Opening identity question and designer's role; GANs, CLIP, text conditioning, lantern example, VAE, classic training/generation and flow-matching caveat; deep question; agent loop, course mark and actual video iterations; Machine A/B bridge. | Keep the opening plus lecture to about an hour. Allow roughly three minutes for the CLIP question; the video/chat is evidence, not a claimed perfect result. |
| 1:00–1:10 | Break | Ten minutes. | Keep release links and the backup device ready. |
| 1:10–1:25 | Install and brief | Match installer to OS; open a project; check tools. Choose an identity, one sentence of intent and two recognizable features. Explain all three tasks. | Approximate setup allocation, outside the making timer. Pair or use the prepared fallback instead of endless troubleshooting. |
| 1:25–2:05 | Activity: A / B / A+B / compare | Ten minutes coded mark, ten minutes generated interpretation, fifteen minutes combination, five minutes side-by-side comparison. | Protect the full 40 minutes after setup. One modest study per route; no extra prompt-writing or 35-minute iteration block. |
| 2:05–2:10 | Challenge 4 and close | Keep the three views, source/prompt/asset evidence and one decision. Explain the comparison layout and a deliberate revision to bring to Week 6. | Submission details remain those confirmed in Canvas. Connect to Machine A/B and mediation. |

## Activity: one identity, three ways of making it

**Shared brief, before the timer:** choose a name, nickname, invented character or personal symbol. Write one sentence about what it should communicate and two features that must remain recognizable. A fictional identity is welcome; a portrait, real name or personal photograph is not required. Keep this brief across all three routes; do not change the identity to rescue a weak result.

| Activity minute | Route | Make and inspect | Evidence |
|---|---|---|---|
| 0–10 | A · rules | Ask Easel's agent for a simple HTML/SVG/Canvas mark, without an image-generation call. Expose two controls and change one value. | Keep source code, one view and the parameter change. Machine B wrote the code; Machine A executed it. |
| 10–20 | B · learned image | Give the image tool the same brief and two features. Explore a material/texture/atmosphere, save one candidate and identify one unrequested choice. | Keep prompt, returned asset and model/tool details where available. Exact lettering is not a requirement. The observation question is inside these ten minutes. |
| 20–35 | A+B · combination | Reuse A's code and B's image. Clip the image or a chosen material region into the silhouette; adjust crop, scale or offset. | Keep the coded boundary, reused asset and hybrid view. Code controls geometry and placement; pixels supply the surface. Three.js is optional when the offline kit is verified. |
| 35–40 | Compare | Show A / B / A+B side by side and answer: what did combining the machines buy you? | Identify one enforced decision, one delegated decision and one trade-off against the original brief. A hybrid can be worse. |

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

| Slide | Type | Question | Use |
|---:|---|---|---|
| 4 | Short answer | What could stand for you without being a portrait? | Start from an identity and one quality; no personal image is required. |
| 16 | Short answer | If CLIP can match the words 'a chair' to a picture, why can't CLIP draw that chair? | Separate alignment from generation; ask what tool controls or claims require evidence. |
| 27 | Short answer | What did the model decide that you did not specify? | One brief observation within B's ten minutes, not extra activity time. |
| 29 | Short answer | What did combining the machines buy you? | Final five minutes: compare the three views, enforced/delegated decisions and trade-offs. |

## Sources and teaching material

- Gio's approved 1 October redesign: opening showcase, approximately one-hour lecture, break, then installation/brief and 40-minute personal-mark activity. The original standalone prompt exercise and 35-minute iteration block are replaced.
- Current syllabus: image machines and mediation; Challenge 4; PolyU GenAI and named Flux/Qwen models; Verbeek (2015) core reading. The workshop supplies a comparison-layout route without silently rewriting assessment.
- Week 2 deck: “Machine B writes Machine A” and controlled parameters/seeds. Week 4 deck: tools and harnesses connect learned proposals with explicit software rules and permissions.
- Original 2025 slide sources: `SD2112 - AI in Design - Week 5.pptx` and `SD2112 - AI in Design - Master.pptx` under `references/onedrive-pptx/`; PDFs under `references/2025/`. GAN examples/competition are on Week 5 PDF pp. 45–46, Edmond portrait 47, caption/image alignment 48–50, noise/U-Net/VAE 51–54 and tools 55. PDF page positions are not printed slide numbers. The revised CLIP account corrects the old generation claim.
- Course-logo exploration: source a-plus-dot and forest/wall variant shared in September 2026. The exploratory edit is not a finalized logo or a guaranteed one-prompt result. The real chat/video iterations are discussed without inventing a successful final movie.
- Lantern still: Easel Flux2-9B, 28 September 2026. On-slide intent is a teaching summary, not the verbatim prompt; it is not a controlled comparison.
- Easel [README](https://github.com/venetanji/easel-client#readme) and [v0.0.1 release](https://github.com/venetanji/easel-client/releases/tag/v0.0.1), checked 1 October: packaged installers, project image assets, HTML authoring, queued media generation and offline Three.js kit. Documented support is not proof of the installed classroom configuration.
- Modern model caveat: Black Forest Labs Flux documentation; Qwen Image documentation and Diffusers Qwen Image pipeline (`FlowMatchEulerDiscreteScheduler`). Classic noise prediction is explicitly labeled rather than presented as every current model's objective.
