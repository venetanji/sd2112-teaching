# SD2112 · Week 5 lesson plan

**Images, intentions, iterations** · Friday 2 October 2026 (date confirmed by Gio; confirm room and teaching-team arrangements in Canvas) · three-hour lecture-workshop · deck: `week05-classpoint.pptx` from the *Build PowerPoints* artifact; web/PDF paths follow the repository's Week 5 naming convention after the deck is registered.

## Purpose

Students bring their own image ideas and visual intent. A visual lecture distinguishes GAN synthesis, CLIP alignment, VAE representation and text-conditioned latent generation. Classic noise-prediction training is a teaching example, not a universal description of modern flow-matching models. Gio demos Easel Client for agent-directed images, video and HTML, and shows the actual chat and iterations from the course-logo video experiment. HTML is agent-authored code rendered by a browser, not a diffusion-generated image. In the workshop, a language agent helps clarify student prompts without taking over authorship; students generate, critique and iterate using the approved service, then document their decisions.

By the end of class, students can:

- describe an image they want to make and identify the visual choices that matter to them;
- explain the distinct roles of GANs, CLIP and diffusion in the move from image-only generation to text-conditioned image generation;
- describe how an agent can call image-understanding and image-generation tools, and identify where the student still directs the process;
- use an agent to clarify an image brief, notice assumptions and approve or reject a rewritten prompt;
- submit a prompt to the authorized image-generation service and record the model/tool details available;
- critique an output against intent, naming a visible choice they did not specify;
- make at least one deliberate iteration, compare versions and explain what they kept, changed or rejected;
- document a process that supports Challenge 4 and the Week 7 reflection.

The model sequence is core lecture content, not optional material: use the visuals to make each model's role distinct, then move quickly into the agent/tool relationship and student-led making. Do not turn it into a full architecture survey. The Week 5 syllabus topic remains “Image machines and mediation”; close by asking how the model and interface shaped what the student could specify and see. The core Verbeek reading remains assigned in the syllabus.

The 2025 Week 5 deck provides the visual source, not a script to repeat. Adapt its progression from GAN output samples and the generator/discriminator competition, to CLIP's paired caption/image representations, to the noisy-image/denoising sequence and latent-diffusion pipeline. The old slide's image/text similarity matrix is a useful reference, but explain it as alignment in a shared embedding space—not as CLIP generating images. Preserve the mediation connection in the closing discussion: the prompt interface and model shape how student intent becomes an image, and what can be inspected or changed depends on the tools. Do not assign one fixed Ihde relation to “image generation” in general; ask what relation this particular workflow created for the student.

## Lecturer demo and student access

The confirmed lecturer demo is [Easel Client / Easel Studio](https://github.com/venetanji/easel-client), selected by Gio on 1 October. Its documented tools generate/edit images, submit video jobs, author HTML project files and inspect canvas captures. Actual model support depends on configured endpoints and the installed build. This is not a new student installation or API-access requirement.

Demo sequence: make one image; critique a visible choice; request one short video via a verified model route; use the wait to build an HTML comparison using saved assets. Show model/tool identity and one revision, not a long feature tour. Do not resubmit an accepted pending generation. Play the resulting video rather than inferring continuity from sampled frames, and click the HTML controls rather than trusting a screenshot.

For the video discussion, Gio opens the real chat and selected iterations from the course-logo experiment. Compare the intended nature/leaves → origami → circuits/fibres → upper-right-dot reveal with visible motion, shape and continuity. Ask whether the next intervention belongs in the prompt, reference inputs or workflow. Do not claim a successful final cut, fixed duration or controlled A/B comparison unless the selected evidence establishes it. No new video render is part of slide preparation.

### Student platform check

The syllabus currently identifies PolyU GenAI (`genai.polyu.edu.hk`) and names Flux and Qwen image models. It does **not** establish that students have direct API access, a supported endpoint, API quotas, or permission to use a specific client library. Before the class, Gio/Nicolò must confirm, with the course/platform owner:

1. the approved image-generation API or platform workflow available to students on 2 October;
2. whether the workflow is a direct API call or a browser UI, and the accurate wording to use in class;
3. authentication, account/credit limits, image-input support, model names, size/aspect-ratio controls, and expected latency;
4. whether students can safely generate multiple versions during the activity;
5. a fallback if API access, rate limits, network or model availability fails.

Do not invent an endpoint, distribute credentials, ask students to paste keys into an LLM, or put secrets in slides, prompts, screenshots or submissions. If only the approved browser interface is available, use that and tell students what they are actually using; direct API use is an unresolved course/platform assumption, not something this plan presumes. A no-login fallback is partner-led prompt clarification and critique against teaching-team sample outputs.

## Before class (from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Confirm the approved image-generation route and test it with a non-sensitive sample; note model, available controls, latency and limits. Test ClassPoint short-answer questions, then reset. Open the web deck as backup. If there is no confirmed direct API, do not label the UI as one. |
| Amber | Post the deck and Challenge 4 brief on the course platform named in Canvas. Confirm the submission location and deadline with Gio; the syllabus only says the challenge is brought to Week 6. |
| WU Zhao, MA Jie | Help students without working access pair up; circulate during prompt clarification and critique. Remind students not to upload images they do not have permission to use or any sensitive personal content. |
| Gio | Confirm room, date in Canvas, API/platform access, fallback, and whether references/seeds/settings are available. Keep the demo to a volunteered or fictional image idea. Confirm Challenge 4 submission logistics without inventing policy. |

## Run of show

The three-hour block is planned as 170 minutes of class plus one 10-minute break. Slide timings are approximate; protect at least 45 minutes for making and critique.

| Time | Segment | What happens | ClassPoint / notes |
|---|---|---|---|
| 0:00–0:10 | Open: image idea | Students write an image they have wanted to make and one visual quality they care about. | Short answer. Use volunteered examples; no sensitive personal details. |
| 0:10–0:18 | Intent, prompt, judgement | Establish the designer's role: intent first, agent-assisted clarification second, student approval and judgement throughout. | Keep this bridge concise; the model sequence follows. |
| 0:18–0:43 | Image-model roles | Compare GAN synthesis and CLIP alignment; use the lantern candidate, VAE hourglass, classic training comparison and generation loop. Briefly distinguish noise prediction from flow matching, then ask the CLIP question. | The training error updates weights; sampling updates the latent with trained weights fixed. The symbolic tiles are not actual intermediate images. Allow three minutes for the question. |
| 0:43–1:03 | Easel Client and our iterations | Show the agent/tool loop and source-mark comparison. Demo image, short video job and HTML authoring; use the real chat and selected logo-video versions for the discussion. | Keep model generation, agent code and human decisions distinct. Ask what survived, what failed, and whether to change prompt, references or workflow. A selected exploration is not a finalized logo. |
| 1:03–1:15 | Pair exercise: prompt clarification | One student describes their idea; partner/agent asks questions, flags assumptions and proposes a prompt. Student approves, edits or rejects it. | Preserve the 12-minute exercise. If the LLM is unavailable, pairs interview each other. |
| 1:15–1:18 | Working specification and student route | Recap the choices that matter and show the confirmed student-facing service or fallback. | The lecturer demo does not establish student Easel/API access. No keys in chat. |
| 1:18–1:23 | First critique | Students name one visible decision the model made that was not specified. | Short answer; distinguish observation from evaluation. |
| 1:23–1:33 | Break | Ten minutes. | TAs confirm tool access and help resolve ordinary login issues. |
| 1:33–1:43 | Critique framework | Compare output with intent; identify a success, a miss/reinterpretation and one decision to test. | Model one example from a student-volunteered idea. |
| 1:43–1:48 | Set up iteration | Write one testable change and predict its effect. Keep other prompt dimensions stable where possible. | Use seed/reference controls only if the verified service supports them. |
| 1:48–2:23 | Activity: deliberate iteration | Generate, compare, and iterate once or twice; keep prompts and versions in order. Pair critique supports, but does not override, the image author's judgement. | 35-minute activity. If generation is slow, one version plus a written next-iteration prompt still counts as evidence. |
| 2:23–2:35 | Compare and discuss | Compare versions against original intent; share what changed, what stayed, and whether the result should be kept, revised or rejected. | Short answer and two contrasting examples. |
| 2:35–2:50 | Challenge 4 and process record | Explain the Week 6 deliverable, model/tool disclosure, prompt/version record and critique. Confirm Canvas logistics only after verified. | No new deadline is inferred here. |
| 2:50–2:58 | Mediation and close | Ask how the interface and model shaped what was easy to specify, see or revise. Connect the work to the Week 7 reflection. | Keep a bridge to Week 6 sound and the course mediation vocabulary. |
| 2:58–3:00 | Transition buffer | Leave two minutes for questions or room handoff. | The three-hour block remains 170 minutes of class plus a 10-minute break. |

## Activity: your idea, your prompt, your iterations

Students work from their own image ideas. One device per student is ideal; sharing a device is fine if each person retains ownership of their own idea and process. Use the course-approved API/platform only after the pre-class check above.

1. **State the intent.** Write a private one-sentence idea and circle the most important visual quality. Students may choose an imagined concept rather than upload a personal photograph.
2. **Clarify.** Ask an agent to ask questions before rewriting. Students can accept, edit or reject every suggestion. Keep the original idea and approved prompt.
3. **Generate.** Submit the approved prompt; record service/model/settings as available and save the first image. Do not include tokens or keys in records.
4. **Critique.** Compare the image to the intention. Name one visible success, one gap/reinterpretation and one unrequested model decision.
5. **Iterate.** Choose one point to change; write the intended change; generate again. If available controls allow it, keep other variables stable. Repeat if time allows.
6. **Decide and explain.** Compare versions side by side. Keep, revise or reject the result and explain why in terms of the original intent, not generic image quality.
7. **Record.** Save the idea, prompt versions, outputs, model/tool information and a short rationale. Students submit through the confirmed course platform.

## Challenge 4 · bring to Week 6

The syllabus names this “a layout you could not design, generated, iterated and critiqued.” Keep that scope and ask students to bring:

- their image/layout intention and approved starting prompt;
- two or more outputs or versions where access permits (if service failure prevents this, include the attempted prompt and planned next iteration);
- the model/service name and available settings, with no credentials;
- one critique naming a visible decision the model made;
- a short account of a deliberate change and the evidence used to keep, revise or reject it.

Confirm the submission destination and deadline in Canvas before teaching; neither is specified in the current syllabus beyond “bring it to the next class.”

## ClassPoint questions

| Slide | Type | Question | Use |
|---:|---|---|---|
| 3 | Short answer | What image have you wanted to make but not yet managed to make? | Start with student interests and visual intent. |
| 15 | Short answer | If CLIP can match the words 'a chair' to a picture, why can't CLIP draw that chair? | Separate matching/conditioning from generating the latent and decoding the image. Ask what the tool exposes versus what needs evidence. |
| 27 | Short answer | What did the model decide that you did not specify? | Ask for an observable output choice. |
| 31 | Short answer | What did you keep, change or reject—and what evidence led you there? | Make the student's design decision visible. |

## Sources and teaching material

- Current syllabus, Week 5: image machines and mediation; Challenge 4; PolyU GenAI and named Flux/Qwen models; Verbeek (2015) core reading.
- Week 4 lesson and deck: preserve the course's distinction between learned model behaviour and designed constraints/harness; refer back to Challenge 3's prompt/draft/edit evidence.
- PR #3 draft `week05` deck and lesson: reviewed for the image-making context and workshop lineage; its very long technical tour and multi-stage ClassPoint wall exercise are not carried over wholesale. This plan narrows the class around Gio's confirmed focus: student intent, agent clarification, image generation, critique and deliberate iteration.
- Original 2025 slide sources reviewed visually: `SD2112 - AI in Design - Week 5.pptx` and `SD2112 - AI in Design - Master.pptx` under `/home/venetanji/.openclaw/workspace-sd2112/references/onedrive-pptx/`; matching PDFs are in `references/2025/`. The Week 5 sequence uses GAN output grids and a generator/discriminator schematic (slides 45–46), Edmond de Belamy (47), a prompt/image example and CLIP encoder/similarity visuals (48–50), forward/reverse noise and U-Net/VAE diagrams (51–54), then UI/API examples (55). The 2026 deck adapts those visual ideas with the existing Edmond portrait asset, newly drawn diagrams in the course palette, and the agent-tool loop requested by Gio. The sources establish the prior teaching sequence and visuals, not current platform/API documentation or 2026 tool availability.
- SD2112 group logo exploration (September 2026): the clean `a` mark was provided as the base; a selected forest/wall variant was edited for its brighter landscape. The lecture compares these two course-created images as an exploratory prompt/edit example, not as a finalized course logo or a single-step generation.
- Lantern example is a course-generated still from Easel Flux2-9B (image server), 28 September 2026. The on-slide intent summarizes the teaching example, not a verbatim prompt. A second ComfyUI attempt produced unwanted lettering and is not used or presented as a valid comparison.
- Easel Client repository README checked 1 October 2026: media generation and editing, queued video jobs, HTML project authoring, live inspection/capture and local export. These are documented capabilities, not a guarantee that every classroom endpoint supports every input.
- Modern model caveat: Black Forest Labs Flux documentation; Qwen Image model documentation and Diffusers Qwen Image pipeline (`FlowMatchEulerDiscreteScheduler`). Keep the classic noise-prediction diagram explicitly labeled rather than presenting it as every current model's objective.
