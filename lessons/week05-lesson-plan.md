# SD2112 · Week 5 lesson plan

**Images, intentions, iterations** · Friday 2 October 2026 (date confirmed by Gio; confirm room and teaching-team arrangements in Canvas) · three-hour lecture-workshop · deck: `week05-classpoint.pptx` from the *Build PowerPoints* artifact; web/PDF paths follow the repository's Week 5 naming convention after the deck is registered.

## Purpose

Students bring their own image ideas and visual intent. A language agent helps them clarify and sharpen a prompt without taking over authorship. Students make a first image with the approved image-generation API or course platform, critique the result against their intention, then make deliberate iterations and document their decisions.

By the end of class, students can:

- describe an image they want to make and identify the visual choices that matter to them;
- use an agent to clarify an image brief, notice assumptions and approve or reject a rewritten prompt;
- submit a prompt to the authorized image-generation service and record the model/tool details available;
- critique an output against intent, naming a visible choice they did not specify;
- make at least one deliberate iteration, compare versions and explain what they kept, changed or rejected;
- document a process that supports Challenge 4 and the Week 7 reflection.

This session intentionally prioritizes the student-led making process over a survey of architectures. Keep the diffusion/CLIP explanation brief and only add it if time permits; do not let technical exposition crowd out generation, critique and iteration. The Week 5 syllabus topic remains “Image machines and mediation”; close by asking how the tool's interface shaped what the student could specify and see. The core Verbeek reading remains assigned in the syllabus.

The 2025 Week 5 deck provides a useful bridge, not a script to repeat: it moves from the prior language-model work through technological mediation, then introduces data-driven image generation and its tool interfaces. Preserve that connection in the closing discussion: the prompt interface and the model mediate how the student's intent becomes an image, and what can be inspected or changed depends on the service. Do not assign one fixed Ihde relation to “image generation” in general; ask what relation this particular workflow created for the student.

## Important pre-class check: API and platform access

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
| 0:10–0:22 | Intent, prompt, judgement | Establish the designer's role: intent first, agent-assisted clarification second, student approval and judgement throughout. | Keep the agenda short. Do not lead with a tool demo. |
| 0:22–0:34 | Pair exercise: prompt clarification | One student describes their idea; partner/agent asks questions, flags assumptions and proposes a prompt. Student approves, edits or rejects it. | If the LLM is unavailable, pairs use the same questions. |
| 0:34–0:44 | A working specification | Discuss subject, intended use, composition, viewpoint, material/light, constraints and deliberately open choices. | Emphasize that more prompt text is not necessarily better. |
| 0:44–0:56 | Approved image service/API | Demonstrate one low-risk generation, naming only controls and models verified before class. | If endpoint/API authorization is unconfirmed, use the course UI accurately or the fallback; no keys in chat. |
| 0:56–1:01 | First critique | Students name one visible decision the model made that was not specified. | Short answer; distinguish observation from evaluation. |
| 1:01–1:11 | Critique framework | Compare output with intent; identify a success, a miss/reinterpretation and one decision to test. | Model one example from a student-volunteered idea. |
| 1:11–1:21 | Break | Ten minutes. | TAs confirm tool access and help resolve ordinary login issues. |
| 1:21–1:31 | Set up iteration | Write one testable change and predict its effect. Keep other prompt dimensions stable where possible. | Use seed/reference controls only if the verified service supports them. |
| 1:31–2:06 | Activity: deliberate iteration | Generate, compare, and iterate once or twice; keep prompts and versions in order. Pair critique supports, but does not override, the image author's judgement. | 35-minute activity. If generation is slow, one version plus a written next-iteration prompt still counts as evidence. |
| 2:06–2:21 | Compare and discuss | Compare versions against original intent; share what changed, what stayed, and whether the result should be kept, revised or rejected. | Short answer and two contrasting examples. |
| 2:21–2:36 | Challenge 4 and process record | Explain the Week 6 deliverable, model/tool disclosure, prompt/version record and critique. Confirm Canvas logistics only after verified. | No new deadline is inferred here. |
| 2:36–2:50 | Mediation and close | Ask how the interface and model shaped what was easy to specify, see or revise. Connect the work to the Week 7 reflection. | Keep a bridge to Week 6 sound and the course mediation vocabulary. |

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
| 12 | Short answer | What did the model decide that you did not specify? | Ask for an observable output choice. |
| 15 | Short answer | What did you keep, change or reject—and what evidence led you there? | Make the student's design decision visible. |

## Sources and teaching material

- Current syllabus, Week 5: image machines and mediation; Challenge 4; PolyU GenAI and named Flux/Qwen models; Verbeek (2015) core reading.
- Week 4 lesson and deck: preserve the course's distinction between learned model behaviour and designed constraints/harness; refer back to Challenge 3's prompt/draft/edit evidence.
- PR #3 draft `week05` deck and lesson: reviewed for the image-making context and workshop lineage; its very long technical tour and multi-stage ClassPoint wall exercise are not carried over wholesale. This plan narrows the class around Gio's confirmed focus: student intent, agent clarification, image generation, critique and deliberate iteration.
- 2025 SD2112 references reviewed: `SD2112 - AI in Design - Week 5.pdf` (61 pages) and `SD2112 - AI in Design - Master.pdf` (50 pages), from `/home/venetanji/.openclaw/workspace-sd2112/references/2025/`. Week 5 places “Mediation Theory” before “Data-driven image generation” in its agenda (pp. 2, 34–44), names Ihde/Verbeek/Rosenberger and the four relations (pp. 35–43), then surveys GANs, CLIP, U-Net, VAE, latent diffusion, and UI/API tools (pp. 44–55). The Master deck condenses the image-model sequence (pp. 18–19), mediation relations (pp. 21–24), and design implications (pp. 25, 47–49). These are evidence of the 2025 teaching sequence and framing, not current platform/API documentation or authority for 2026 tool availability. The 2026 lesson retains the useful mediation bridge while shifting classroom time to student-owned intent, agent-assisted clarification, generation, critique and iteration as directed by Gio.
