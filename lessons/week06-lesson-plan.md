# SD2112 - Week 6 lesson plan

**Sound machines** - Semester 1, 2026/27; confirm the class date, room and arrangements in Canvas - three-hour lecture-workshop - deck: `week06-classpoint.pptx` (46 slides); web/PDF follow the repository's Week 6 naming convention.

## Purpose

Close the creative-process module with sound. One product moment connects three routes: **Machine A** executes musical rules; **Machine B** generates audio from learned patterns; **A+B** combines saved material under explicit arrangement and editing decisions. Easel supplies the project, agent and tools, but the student sets the purpose and decides what belongs in the result. **Machine B writes the code; Machine A executes it.** This distinction concerns how the sound is produced, not whether the helper agent is learned.

Teach the complete theory lecture first. A ten-minute break precedes a ten-minute instructor Easel demonstration, then fifteen minutes for setup and one shared sonic brief. Protect **10 + 10 + 15 + 5 = 40** minutes for A, B, A+B and listening/saving. Collect **one final playable result**, not intermediate uploads or a screenshot in place of sound. The remaining booked time is flexible feedback, help, mock-quiz practice and close, not an extension of making.

By the end, students can:

- distinguish waveform, sampled signal, frequency spectrum, spectrogram and MIDI;
- explain what an explicit synthesis/sequencing rule controls, including controlled randomness;
- describe historical spectrogram diffusion and learned codec-token generation without treating either as every current product's architecture;
- keep a sonic brief stable while comparing A, B and A+B;
- identify an unrequested model choice and one arrangement decision that they made themselves;
- assemble and listen to a short playable result, retaining sources and honest tool attribution;
- use their own experiments as evidence for the existing Week 7 reflection.

## Lecture: listening, rules, learned sound and agents

Slides 1-29 occupy the hour before the break. Keep concepts tied to listening and design purpose; do not open with Easel or use a live generation wait as teaching time. Suggested allocations within the hour: introduction/listening and representations 18 minutes, Machine A/history 16 minutes, Machine B/choices 18 minutes, agents and boundary recap 8 minutes. The two short answers are included in these allocations, not extra activities.

### Listening and representations (slides 3-10)

Listening is a relation between a person, technology and a situation. A completion sound can reassure one listener and interrupt another. Ask what a sound helps someone notice or do, not merely whether it sounds impressive. Do not assign one universal Ihde relation to all listening or sound generation.

- **Waveform:** amplitude over time. Amplitude is a physical/signal quantity, not perceived loudness; hearing also depends on frequency, duration, context and the listener.
- **Sampling:** measurements at discrete times. Sample rate is not pitch; distinguish sample rate, bit depth and file compression. A sampled representation has limits and needs appropriate filtering.
- **Spectrum/FFT:** a frequency analysis of a chosen interval, not a score or the whole evolving sound. Explain the time/frequency trade-off without a derivation.
- **Spectrogram:** successive short-time spectra, with time and frequency axes and colour encoding magnitude/energy (often logarithmic). It is not a direct picture of subjective loudness. A magnitude image alone omits phase: reconstruction needs phase information or an estimate and an inversion procedure; resizing a picture does not automatically produce valid audio.
- **Perception/music:** pitch, timbre, rhythm, melody and harmony are useful distinctions, not exhaustive definitions of musical meaning. A rule-based composition can be expressive and meaningful; Machine A is not confined to meaningless beeps.
- **MIDI:** symbolic performance messages, including notes, velocity and timing/control events, not recorded audio. A synthesizer or instrument renders those instructions into sound.

### Machine A (slides 11-18)

Use the Illiac Suite (1957) as a historical example of programmed composition, including generate-and-test and probabilistic procedures. Not every movement uses the same procedure, and modern learned music is not merely a larger Markov table. Explain synthesis, a sequencer grid and Strudel as explicit musical instructions; explain where a seed or probability enters without equating randomness with learning. An agent may propose the code, but the executed pattern and exposed parameters are still inspectable rules.

Slide 18 is the first deep short answer. Invite an argument about a meaningful musical choice, supported by an audible or procedural example. It should help students distinguish intention, chance and execution rather than rehearse an A-good/B-bad slogan.

### Machine B (slides 19-26)

Use two **documented** roads: the historical Riffusion spectrogram-diffusion demonstration and MusicGen's learned discrete audio-codec tokens. Riffusion is a situated historical implementation, not a claim about the current Riffusion product. A codec compresses/represents audio; a learned generation model predicts sequences in that representation; decoding turns tokens into waveform audio. Learned music models are not explained adequately as Markov chains alone.

Suno is the practical classroom route in the upcoming Easel release, but its proprietary architecture is not publicly established. Do not claim Suno secretly uses MusicGen, Riffusion or one specified diffusion/transformer design. Compare tools by the verified interface, permitted access, queue, editable decisions, output and licence, not a guessed architecture or marketing ranking.

Authorship and consent belong to the design decision: use authorized inputs, avoid impersonation or unauthorized voice cloning, and record tools and any supplied material. Product terms and legal cases are time- and jurisdiction-sensitive. Before teaching, verify any concise dated claim against a primary source; otherwise state the uncertainty or omit the claim. Do not copy the original PR's September lawsuit chronology as current fact, or treat access to a generated file as blanket ownership of all uses.

Slide 26 is the second deep short answer. Ask students to argue which choices they would retain, reject or insist on controlling, with evidence and a reason connected to the brief. Both ClassPoint answers may seed arguments for the **existing reflection**; neither creates a new assessed submission, compulsory essay section or new rubric.

### Agents and boundaries (slides 27-29)

An agent can interpret a brief, select a permitted tool, propose Strudel code, request learned audio, inspect returned assets and help arrange them. Explicit software controls playback, files, timing, permissions and the timeline. Keep these levels separate: learned proposal, tool execution, student approval. Agents do not guarantee duration, licensing, aesthetic success or faithful compliance with a prompt. A+B is a division of responsibilities, not automatically the best route.

## Installation and access checks

Use the **upcoming Thursday Easel release with proper Strudel and Suno support**, as specified by Gio. Its release is the preparation target, not a claim that an unreleased build is already available. Link the [Easel Client / Easel Studio releases](https://github.com/venetanji/easel-client/releases) in the class materials; the instructor verifies the actual release and merged support before class. Do not direct students to an old release as though it is the workshop target, or burden the student setup slide with an obsolete-version warning.

### Instructor pre-class check

Test the complete path on a classroom-equivalent device after the target release is available:

1. Confirm release/package, OS/architecture and the supported classroom configuration; open a project. Use approved installers without bypassing security controls.
2. Confirm the authorized agent, Strudel and Suno tools, selected model, account/tool quota and queue behaviour. A working installer does not establish generation access. Put credentials only in protected configuration, never slides, chat or student submissions.
3. Play and Stop a short Strudel pattern, inspect its tempo/timbre controls, check headphones and safe output level, and save A in a format the timeline can actually import. Verify the supported capture/save route; do not assume Strudel can import arbitrary samples or export a particular file type.
4. Submit one non-sensitive Suno request and save an actual returned B asset. Test the supported import route. Do not promise exact generated duration, stems, extensions or reference-audio support. Students may trim a longer result; the brief is not proof that a model obeyed it.
5. Import saved A and B into Easel's timeline; trim, position, fade and adjust gain; play the result, save the project, export and reopen the file/share link on a second playback device. Test Play/Stop there too. Verify both audible sound and the final duration.
6. Verify the actual export container and codec. If the current timeline exports **WebM with Opus sound**, a verified playable WebM is acceptable, even if it has a visual track. Do not promise audio-only MP3 export. A silent canvas recording or still waveform is not the sonic result.
7. Prepare saved A and a **pre-generated, licensed B fallback**, with source/permission and an explicit supplied label. Also prepare a working shared device and a short completed instructor example. Do not generate new media merely for deck preparation. Rehearse this demo and export path rather than improvise integrations during class.

Publish the release link, course deck, brief and confirmed Canvas collection route in the class materials. Installation, access and playback checks happen before the making timer. Pair or use the shared device when needed while preserving each student's brief and decisions. Any alternative permitted harness must satisfy the same save/import/playable-result contract, not add a separate exercise. If B queues or fails, use the licensed supplied B excerpt, label it as supplied and critique the resulting division of control; do not claim it as the student's own generation.

## Before class (from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Verify the target release, authorized tools/model/quota, Strudel Play/Stop and save route, Suno saved asset, timeline import/export and reopened sound. Prepare the shared device and labelled licensed fallback. Test ClassPoint short answers on slides 18 and 26, then reset; keep the web/PDF backup ready. |
| Amber | Post release and class-material links through Canvas. Confirm the final file/share-link destination and access settings; post Challenge 5 and the unchanged reflection brief/rubric. Prepare optional reflection-draft support, not a new submission. |
| WU Zhao, MA Jie | Help with packages, project setup, headphones and safe volume; organize paired access. Keep credentials and personal material out of shared/public records. |
| Gio | Rehearse the ten-minute Easel demonstration using saved, authorized material. Verify dated product/legal claims or remove them. Confirm one brief and the export fallback. Use only actual instructor evidence or explicitly labelled illustrations, never invented student work. |

## Run of show

**Start the 40-minute clock only after** setup, Play/Stop, access and the shared brief are ready. Listening/saving is inside the 40 minutes; submission must not become a fifth making round.

| Time | Slides | Segment | What happens | Notes |
|---|---|---|---|---|
| 0:00-1:00 | 1-29 | Theory lecture | Listening/representations, A/history/rules, B/documented models/choices, agents and boundaries. | Deep short answers at 18 and 26; no Easel opening demo. |
| 1:00-1:10 | 30 | Break | Ten minutes. | Keep demo project and release links ready. |
| 1:10-1:20 | 31-32 | Instructor Easel demo | Show the same brief as a Strudel rule, a saved learned example, then a timeline arrangement. Play/Stop, save/import and reopen the actual supported export. | Ten minutes total; avoid a live generation queue. Do not invent an example success or student response. |
| 1:20-1:35 | 33-36 | Setup and sonic brief | Release/access/playback checks; one product moment; sound spec and controls; explain the 40-minute overview. | Setup and writing the initial brief are outside making time. |
| 1:35-2:15 | 37-41 | A / B / A+B / listen and save | 10 minutes rules, 10 minutes learned audio, 15 minutes timeline combination, 5 minutes listening/saving and one final collection. | Protect all 40 minutes. No intermediate uploads or extra comparison block. |
| 2:15-3:00 | 42-46 | Feedback, help, practice and close | Listen to willing students' actual results, discuss choices, practise three mock-quiz prompts, revisit Challenge 5 and the existing reflection. | Flexible within the booked time, not more making or a graded quiz. TAs support drafts and accounts. |

## Activity: one sonic brief, three routes

**Shared brief, before the timer:** choose one product and one moment in its use: unlocking, confirmation, arrival, transition or another specific event. State the listener and purpose; a target duration **up to 30 seconds**; a tempo/structure if useful; timbre/mood; and one must-not. Do not require a 30-second notification for an event that calls for a shorter sound. Choose two controls that can be tested, such as tempo and note density. Keep the same intent across A, B and A+B. Avoid artist imitation requests, personal voice uploads and unnecessary sensitive inputs.

The sound spec separates executable controls (pattern, tempo, duration after editing, gain) from interpreted requests (calm, playful, reassuring). A mood is not a guaranteed output parameter. Retain this spec privately with the source, prompts and decisions; it is not a compulsory intermediate upload.

| Activity minute | Route | Make and inspect | Evidence |
|---|---|---|---|
| 0-10 | A - rules (slide 37) | Ask the Easel agent for a modest Strudel pattern using the brief. Play/Stop it, expose two controls and change one. Save A through the verified route. | Keep the code, chosen values and audible saved result. Machine B wrote the code; Machine A executes it. |
| 10-20 | B - learned sound (slide 38) | Ask the agent to use the supported Suno tool for the same intent. Save the returned material; listen and identify one unrequested choice. Select an excerpt if longer than needed. | Keep prompt, tool/model details available, returned asset and the decision to keep/reject it. One accepted request is enough; do not require repeated generations. |
| 20-35 | A+B - arrangement (slide 39) | Reuse **saved A intro + B excerpt + A outro** in Easel's timeline. Trim, position, fade and adjust gain to make a short coherent result. Check the transition against the product moment. | Keep the project and sources. This baseline needs no new generation, arbitrary sample import or automatic beat matching. The student controls order and edit boundaries. |
| 35-40 | Listen, save and collect (slides 40-41) | Listen to the complete result safely, inspect duration/transitions, save and export through the verified path, then reopen it. Submit **one final playable result** as a Canvas file or accessible share link. | No required caption, essay, comparison collage, A-only/B-only upload or native ClassPoint audio activity. A verified WebM with sound is valid if that is the supported timeline export. |

If a generation is pending, do not resubmit it. Use time for A/source preparation or use the labelled licensed B fallback; keep the same brief and finish within the timer. If export fails, use the prechecked working route/shared device rather than promising an unverified converter or submitting silent video. Record an actual technical blocker honestly. A+B is an experiment, not evidence by itself that the hybrid improved the design.

## ClassPoint questions and final collection

Keep exactly **two deep short answers**. Neither requires a caption or image. Discuss evidence, responsibility and what the student would change; the answers seed arguments for the existing Week 7 reflection, not new assessment. During making, retain observations privately rather than interrupting all three routes with submission walls.

| Slide | Type | Question focus | Use |
|---|---|---|---|
| 18 | Short answer | Which musical choice would you fix—and which would you leave open? | Ground an argument in an audible/rule-based example; connect control, chance and intention. |
| 26 | Short answer | Which choice in generated music would you accept—and which would you challenge? | Explain a boundary with evidence and a reason tied to the brief, consent or responsibility. |
| 41 | Canvas file/share link | One final playable A+B result. | Collection after all three routes; not a generated native ClassPoint audio-upload button. |

### Mock quiz practice (slide 43)

Use three ungraded prompts to practise for the existing Week 7 quiz on weeks 1-6 and the playlist. Students answer aloud, privately or by a show of hands; no additional ClassPoint activities. Discuss the answers from speaker notes. Cover MIDI versus recorded audio, why a handwritten probability table remains Machine A despite chance, and why codec tokens are not necessarily musical notes. Do not reinstate the original draft's eight quiz slides or graded captures. The instructor can adapt the explanation to actual misunderstandings without fabricating a response distribution.

## Challenge 5 - sound for a product

The existing weekly challenge remains **up to 30 seconds of sound**, collected through Canvas using the confirmed destination/timing. The workshop result is a starting point, not a new assessment component. Revise one sonic decision deliberately; retain the brief, sources, code/prompt where applicable, available tool/model details and what was kept, rejected or supplied. Keep a screenshot/image of the code, timeline, waveform or spectrogram as process evidence **alongside** the playable sound, not as its substitute. Verify permission before sharing generated or supplied material. Do not invent a submission deadline or add compulsory intermediate captures.

## Reminder of the individual reflection brief (slide 45)

The approved syllabus remains unchanged: about **1000 words** on AI's role in the student's creative process, particularly **Machine A versus Machine B**, using **at least three of their own experiments from the weekly challenges (weeks 2-6), with images**, ending with a short note on **how AI was used to write it**. Submit on **Canvas in Week 7**. Preserve the current weighting, rubric and process-note rule. Sound can contribute one of those experiments with an appropriate process image; it does not replace all three or remove the image requirement.

Offer TA draft support, not a required new draft submission. Encourage claim -> evidence -> interpretation: which choice was expressed, which was delegated, what the result showed, and why the next intervention belonged in code, prompt, selection or editing. The two ClassPoint answers are possible arguments to develop, not mandated essay sections. Do not treat tool praise or an attractive output as sufficient evidence.

## Sources and teaching material

- Current `syllabus/SD2112-syllabus-2026.md`: Week 6 sound, Challenge 5, Week 7 quiz/reflection and unchanged assessment; Week 5 lesson plan supplies the established theory/break/demo/setup/40-minute structure.
- [Original course-refresh PR #3](https://github.com/venetanji/sd2112-teaching/pull/3), Week 6 lesson plan: useful representation/history/model themes, **not** the current slide count, timing, platform, quiz count or three-round capture contract. Its waveform/loudness, spectrogram inversion, Markov-only music, product/legal and guaranteed-compliance shortcuts are corrected here.
- Gio's approved 46-slide order: title/agenda 1-2; listening and representations 3-10; A 11-18; B 19-26; agents/boundaries 27-29; break 30; workshop title/demo 31-32; setup/brief/spec/overview 33-36; A/B/A+B/listen-save 37-40; one final collection 41; debrief 42; three mock prompts 43; Challenge 5 44; unchanged reflection 45; end 46.
- [Riffusion's original spectrogram-diffusion repository](https://github.com/riffusion/riffusion), for the historical example and reconstruction caveat; [MusicGen / AudioCraft](https://github.com/facebookresearch/audiocraft), for documented codec-token generation. These are not evidence of Suno's proprietary internal architecture.
- [Strudel documentation](https://strudel.cc/learn/) and [Easel releases](https://github.com/venetanji/easel-client/releases): verify the actual upcoming classroom release, permitted tools and complete save/import/export route before class. PR #13 integration is expected soon, not proof that a given release already includes it.
- Current Suno documentation/terms and primary legal sources: verify and date any specific product-plan, licence, consent or case-status claim immediately before teaching. This plan makes no unverified legal chronology or blanket ownership claim.

## What to keep after class

Retain the final playable result and students' own process records through approved course storage, not the public source repository. Note actual playback/export problems and tool queues for the next class. Preserve useful reflection themes without inventing quotes or exporting identities into public materials. Keep TA support records private. No student sound generation is needed to prepare this deck, and no new assessment is introduced.
