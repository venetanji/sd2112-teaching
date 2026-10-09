# SD2112 - Week 6 lesson plan

**Sound machines** - Semester 1, 2026/27; confirm the class date, room and arrangements in Canvas - three-hour lecture-workshop - deck: `week06-classpoint.pptx` (50 slides); web/PDF follow the repository's Week 6 naming convention.

## Purpose

Close the creative-process module with sound. For one identity and product moment, **Machine A** executes musical rules to make an original demo; **Machine B** uses that exported demo as an audio reference to propose a transformation; **A+B** is this connection between authored input, learned arrangement and human listening/editing decisions. It is not unrelated A/B clips joined as an intro, excerpt and outro. Students may use Strudel, GarageBand or another available tool for the demo. Easel coordinates the supported Suno reference operation, but the student sets the purpose and decides what belongs in the result. When an agent writes Strudel, **Machine B writes the code; Machine A executes it.** This distinction concerns how the sound is produced, not whether the helper agent is learned.

Teach the complete theory lecture first. A ten-minute break precedes a ten-minute instructor Easel demonstration, then fifteen minutes for setup and one shared sonic brief. Protect **15 + 15 + 5 + 5 = 40** minutes for making/exporting, reference-conditioned transformation, comparing/revising and listening/saving. Collect **one final playable result up to 30 seconds**, not intermediate uploads or a screenshot in place of sound. Keep the original demo privately as process evidence; uploading it to a provider for transformation is not a course submission. The remaining 45 minutes are flexible feedback, the two deep ClassPoint answers, help, mock-quiz practice and close, not an extension of making.

By the end, students can:

- distinguish waveform, sampled signal, frequency spectrum, spectrogram and MIDI;
- explain what an explicit synthesis/sequencing rule controls, including controlled randomness;
- describe historical spectrogram diffusion and learned codec-token generation without treating either as every current product's architecture;
- make and export actual audio, then use their own demo as a reference while keeping the sonic brief stable;
- compare a recognisable motif in the original demo and completed transformation, identify an unrequested model choice and make one deliberate revision;
- save, reopen and listen to a short playable result, retaining sources and honest tool attribution;
- use their own experiments as evidence for the existing Week 7 reflection.

## Lecture: listening, rules, learned sound and agents

Slides 1-31 occupy the hour before the break. Keep concepts tied to listening and design purpose; do not open with Easel or use a live generation wait as teaching time. Suggested allocations within the hour: introduction/listening and representations 22 minutes, Machine A/history 14 minutes, Machine B/choices/rights 16 minutes, agents and boundary recap 8 minutes. The two deep short answers are on slides 45 and 46 **after real making and listening**, not inside this theory hour. Brief oral listening questions are not additional ClassPoint activities.

### Listening and representations (slides 3-13)

Listening is a relation between a person, technology and a situation. A completion sound can reassure one listener and interrupt another. Ask what a sound helps someone notice or do, not merely whether it sounds impressive. Do not assign one universal Ihde relation to all listening or sound generation.

- **Waveform:** amplitude over time. Amplitude is a physical/signal quantity, not perceived loudness; hearing also depends on frequency, duration, context and the listener.
- **Sampling:** measurements at discrete times. Sample rate is not pitch; distinguish sample rate, bit depth and file compression. A sampled representation has limits and needs appropriate filtering.
- **Spectrum/FFT:** a frequency analysis of a chosen interval, not a score or the whole evolving sound. Explain the time/frequency trade-off without a derivation.
- **Spectrogram:** successive short-time spectra, with time and frequency axes and colour encoding magnitude/energy (often logarithmic). It is not a direct picture of subjective loudness. A magnitude image alone omits phase: reconstruction needs phase information or an estimate and an inversion procedure; resizing a picture does not automatically produce valid audio.
- **Perception/music:** pitch, timbre, rhythm, melody and harmony are useful distinctions, not exhaustive definitions of musical meaning. A rule-based composition can be expressive and meaningful; Machine A is not confined to meaningless beeps.
- **MIDI:** symbolic performance messages, including notes, velocity and timing/control events, not recorded audio. A synthesizer or instrument renders those instructions into sound.

Use the HTML lecture's controlled oscillator on slides 4 and 6: click Play, change pitch and sine/triangle/sawtooth, then compare the actual waveform, FFT spectrum and time-history waterfall. Start quiet; Stop or Escape before navigation. There is **no microphone access**, student recording or equalizer effect. Frequency relates to pitch for periodic tones; harmonic content changes with waveform. The waterfall's relative signal level is not perceived loudness. PDF/PPTX show explicitly illustrative stills, not measured captures or playable audio.

Slides 9-12 isolate **rhythm, bass, harmony and melody** in four standalone Strudel layers. The left-hand code shows one role; each clickable online-editor link combines that role with the earlier layers at 100 BPM (`setcpm(100/4)` for a four-beat cycle). Hear the additional role and stop other players before moving on. Rhythm uses short C2 sine attacks/rests; bass plays C2 C2 G2 C2 on triangle; harmony sounds C3 E3 G3 together; melody plays C4 E4 G4 B4 on sine. These native oscillators need no external sample pack. The online REPL and Easel's `app.js`/`createPattern` integration are different environments; do not paste the REPL code unchanged into a wrapper. Practical export happens after the break.

### Machine A (slides 14-20)

Use the Illiac Suite (1957) as a historical example of programmed composition, including generate-and-test and probabilistic procedures. Not every movement uses the same procedure, and modern learned music is not merely a larger Markov table. Explain synthesis, a sequencer grid and Strudel as explicit musical instructions; explain where a seed or probability enters without equating randomness with learning. An agent may propose the code, but the executed pattern and exposed parameters are still inspectable rules.

Slide 18's live grid is a course-owned written sequencer, not Easel or Strudel. Human clicks Play, changes a cell or tempo and stops it; native Web Audio plays the written rule. Slide 19 supplies the combined four-part Strudel starter and its online-editor link. Invite a short oral observation about control and chance, but defer the evidence-led ClassPoint answers until students have made and heard their own transformation.

### Machine B (slides 21-28)

Use two **documented** roads: the historical Riffusion spectrogram-diffusion demonstration and MusicGen's learned discrete audio-codec tokens. Riffusion is a situated historical implementation, not a claim about the current Riffusion product. A codec compresses/represents audio; a learned generation model predicts sequences in that representation; decoding turns tokens into waveform audio. Learned music models are not explained adequately as Markov chains alone.

Suno is the intended practical classroom route through Easel, but its proprietary architecture is not publicly established. Do not claim Suno secretly uses MusicGen, Riffusion or one specified diffusion/transformer design. Compare tools by the verified interface, permitted access, queue, editable decisions, output and licence, not a guessed architecture or marketing ranking. Describe reference-conditioned generation as a proposal: audio input does not guarantee exact motif preservation, duration, BPM or arrangement.

Authorship and consent belong to the design decision: use authorized inputs, avoid impersonation or unauthorized voice cloning, and record tools and any supplied material. Product terms and legal cases are time- and jurisdiction-sensitive. Before teaching, verify any concise dated claim against a primary source; otherwise state the uncertainty or omit the claim. Do not copy the original PR's September lawsuit chronology as current fact, or treat access to a generated file as blanket ownership of all uses.

Slides 27-28 separate input ownership, provider permission and output rights. **Suno consumer terms, as checked for this revision on 9 October 2026:** original uploads remain yours, but uploading grants a broad provider licence, including service/model improvement; ownership is not confidentiality. Use self-authored or appropriately licensed material and necessary collaborator/voice consent. Attribution alone is not permission, and owning a GarageBand project does not automatically clear every borrowed loop for provider use.

For consumer generations, **Basic is personal/non-commercial**. **Pro/Premier assigns the provider's rights subject to current terms, including an approved download for commercial use**; an unofficial capture is not a substitute. Paying later does **not automatically** license older free-plan outputs. Assignment of whatever rights the provider owns does not guarantee legal copyright, uniqueness or freedom from other rights. Specific Remix restrictions may differ; do not conflate every own-demo transformation with that product operation. Hong Kong rules differ from US rules, with originality and the necessary arranger fact-specific. This is teaching context, not legal advice.

Verify the **actual Easel/provider contract**, entitlement and permitted operations before class. Easel credits do not establish a student's consumer Pro subscription or commercial rights. Consumer terms are not proof of the integration agreement. Recheck primary terms if the teaching date changes; do not repeat stale pricing or lawsuit chronology.

### Agents and boundaries (slides 29-31)

An agent can interpret a brief, select a permitted tool, propose Strudel code, supply the student's exported audio to the supported reference operation, track a job and save returned assets. Explicit software controls playback, files, timing and editing; the student approves input and judges the sound. Keep learned proposal, tool execution and human approval separate. A textual description of a demo is not evidence that audio was attached. There is **no compulsory timeline**, fixed intro/excerpt/outro recipe or arbitrary sample-import requirement. A+B connects authored material to a learned transformation, not automatically the best result. Agents do not guarantee duration, licensing, aesthetic success or faithful compliance with a prompt.

## Installation and access checks

Use the **classroom Easel release Gio identifies**, targeting the Thursday Strudel/Suno support he specified. Link the [Easel Client / Easel Studio releases](https://github.com/venetanji/easel-client/releases) in the class materials. **Gio owns the local Strudel/Easel integration fixes and classroom smoke test.** This course-source revision is not a verified integration test and does not establish that any published release supports audio reference upload. Do not modify local integrations or the shared generator as part of course-source preparation. Exact input limits, file formats, operation names and arguments must come from the actual tested classroom configuration, not guessed consumer documentation.

### Instructor pre-class check

Gio tests the complete path on a classroom-equivalent device after the target release is available; TAs assist with the confirmed configuration:

1. Confirm release/package, OS/architecture and the supported classroom configuration; open a project. Use approved installers without bypassing security controls.
2. Confirm the authorized agent, Strudel and Suno tools, selected model, account/tool quota and queue behaviour. A working installer does not establish generation access. Put credentials only in protected configuration, never slides, chat or student submissions.
3. Play and Stop a short self-authored demo in Strudel, GarageBand or another available tool. Inspect controls, safe output level and headphones; export actual audio and replay that file. Confirm a format the reference operation accepts. Do not assume arbitrary sample import, a particular export type or an undocumented converter.
4. Give Easel that exported demo and verify the actual Suno **audio reference** attachment and operation, authorized access, bounded request, job receipt and completion. A prompt naming a file is not evidence of successful upload. Check the current Easel/provider agreement and input permission. Do not promise precise motif fidelity, exact generated duration/BPM, stems, extensions or consumer-plan entitlements.
5. Save a **completed transformation**, compare it with the original demo and make one supported edit/revision if needed. Reopen the saved final file/share link on a second playback device. Verify audible sound and a final duration up to 30 seconds. Editing may use a tested timeline, but combining unrelated A/B clips is not the required exercise.
6. Verify the actual export container and codec. A verified playable **WebM with sound** is acceptable even if it has a visual track; do not promise audio-only MP3 export. A silent canvas recording, MIDI file or still waveform is not the sonic result.
7. Prepare the original demo, its completed reference-conditioned transformation and a **pre-generated, licensed fallback**, with source/permission and an explicit supplied label. Also prepare a working shared device. Do not generate new media merely for deck preparation. Rehearse the ten-minute demo and export path rather than improvise integrations during class. Test the lecture oscillators' quiet Play/Stop and cumulative Strudel editor links separately from the Easel workflow.

Post the release link, course deck, brief and confirmed Canvas collection route in the class materials. Installation, access and playback checks happen before the making timer. Pair or use the shared device when needed while preserving each student's brief and decisions. Any alternative permitted tool must satisfy the same actual-audio reference and playable-result contract, not add a separate exercise. If B queues or fails, use the labelled licensed fallback and describe the limitation honestly; do not claim it was generated from the student's demo. If reference upload fails, do not silently substitute text-only generation and report reference conditioning as successful.

## Before class (from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Assist Gio's classroom smoke test using the confirmed release/tools/quota and export/reference/save path. Prepare the shared device and labelled licensed fallback. Test ClassPoint short answers on slides 45 and 46, then reset; keep the web/PDF backup ready. |
| Amber | Post release and class-material links through Canvas. Confirm the final file/share-link destination and access settings; post Challenge 5 and the unchanged reflection brief/rubric. Prepare optional reflection-draft support, not a new submission. |
| WU Zhao, MA Jie | Help with packages, project setup, headphones and safe volume; organize paired access. Keep credentials and personal material out of shared/public records. |
| Gio | Own local Strudel/Easel fixes and the classroom export -> reference upload -> completed transformation -> reopened final-result smoke test. Rehearse the ten-minute demonstration with saved authorized material; confirm actual tool arguments/limits and Easel/provider rights. Verify dated product/legal claims or remove them. Use actual instructor evidence or labelled illustrations, never invented student work. |

## Run of show

**Start the 40-minute clock only after** setup, Play/Stop, access and the shared brief are ready. Listening/saving is inside the 40 minutes; submission must not become a fifth making round.

| Time | Slides | Segment | What happens | Notes |
|---|---|---|---|---|
| 0:00-1:00 | 1-31 | Theory lecture | Listening/representations and four musical layers, A/history/rules, B/documented models/choices/rights, agents and boundaries. | All theory before break; no Easel opening demo or deep ClassPoint answers yet. |
| 1:00-1:10 | 32 | Break | Ten minutes. | Keep demo project and release links ready. |
| 1:10-1:20 | 33-34 | Instructor Easel demo | Make/play the demo, export and replay actual audio, show Easel's supported Suno reference workflow, then hear a saved completed transformation. | Ten minutes total; precompleted material avoids a live generation queue. No invented upload or success. |
| 1:20-1:35 | 35-38 | Setup and sonic brief | Demo tool/release/access/playback checks; one identity and moment; sound spec and controls; explain the 40-minute overview. | Setup and writing the initial brief are outside making time. |
| 1:35-2:15 | 39-43 | Demo / transformation / revise / listen and save | 15 minutes demo/export, 15 minutes audio-reference transformation, 5 minutes comparison/revision, 5 minutes listening/saving and one final collection. | Protect all 40 minutes. Slide 43 explains that same collection, not another making round. No intermediate uploads. |
| 2:15-3:00 | 44-50 | Feedback, help, practice and close | Debrief actual results; deep ClassPoint short answers 45/46; three mock prompts 47; Challenge 5 at 48; unchanged reflection 49; end 50. | 45 flexible minutes, not more making or a graded quiz. TAs support drafts and accounts. |

## Activity: your demo becomes the reference

**Shared brief, before the timer:** use the previous mark/product or invent an identity; choose one moment such as opening, unlocking, confirmation, arrival or waiting. State the listener and purpose; a final target duration **up to 30 seconds**; tempo/structure if useful; timbre/mood; a recognisable motif to listen for; and one must-not. A small self-authored motif is enough; neither lyrics nor a whole song are required. Do not require a 30-second notification for an event that calls for a shorter sound. Choose controls that can be tested, such as tempo and note density, and describe what the transformation should preserve or change. Keep the same intent across demo and transformation. Avoid artist imitation requests, personal voice uploads and unnecessary sensitive inputs.

The sound spec separates executable controls (pattern, tempo, duration after editing, gain) from interpreted requests (calm, playful, reassuring). A mood is not a guaranteed output parameter. Retain this spec privately with the source, prompts and decisions; it is not a compulsory intermediate upload.

| Activity minute | Route | Make and inspect | Evidence |
|---|---|---|---|
| 0-15 | A - make and export (slide 39) | Make an original demo in Strudel, GarageBand or another available tool. Choose notes/rhythm/timbre, change one thing and listen. **Export actual audio** through the demonstrated route and replay the file. | Keep the original demo and code/project privately. A MIDI file, screenshot or editor preview alone is not the reference. Check permission for any loops or collaborators. |
| 15-30 | B - transform from audio (slide 40) | Give Easel the exported demo as the Suno audio reference. Ask for a new arrangement for the same identity/moment and name the feature to preserve. Track the supported job; listen to and save a completed transformation. | Keep the prompt, available tool/model details, actual input/output and choice. Confirm attached audio; no unrelated text-only prompt in its place. Do not duplicate a pending job or require repeated generations. |
| 30-35 | A+B - compare and revise (slide 41) | Replay the original demo and transformation separately. Compare the recognisable motif: identify a preserved feature and a changed/missing one. Keep the result or make one supported edit/revision for the listener; trim if needed to up to 30 seconds. | Keep a reason for the decision privately. No compulsory timeline, fixed intro/excerpt/outro, comparison collage or automatic beat matching. A+B is reference conditioning plus human judgement, not proof the hybrid improved the design. |
| 35-40 | Listen, save and collect (slides 42-43) | Stop competing players, listen quietly, save/export through the tested route, then reopen and check duration and sound. Submit **one final playable result** as a Canvas file or accessible share link. | No required caption, essay, original-demo upload, separate B-only capture or native ClassPoint audio activity. A verified WebM with sound is valid if that is the supported export. |

If a generation is pending, do not resubmit it. Use time to review the original/source record or use the labelled licensed fallback; keep the same brief and finish within the timer. If no completed transformation exists, do not fabricate a comparison or say the fallback came from the student's reference. If export/upload fails, use the prechecked working route/shared device rather than promise an unverified converter or submit silent video. Record an actual technical blocker honestly. The final collection remains one result, not an intermediate submission wall.

## ClassPoint questions and final collection

Keep exactly **two deep short answers**, after the actual making, final save/collection and spoken debrief. Neither requires a caption or image. Discuss audible evidence, responsibility and what the student would change; the answers seed arguments for the existing Week 7 reflection, not new assessment. During making, retain observations privately rather than interrupting the workflow with submission walls. A missing motif, failed job or labelled fallback can support an honest argument but cannot establish unobserved model behaviour.

| Slide | Type | Question focus | Use |
|---|---|---|---|
| 43 | Canvas file/share link | One final playable result. | Same final collection as the last five making minutes; not a generated native ClassPoint audio-upload button. |
| 45 | Short answer | What made this sound yours: the demo, the prompt, or the listening decision? | Use one audible change from demo to final result; explain the student's contribution and its limits. |
| 46 | Short answer | Which choice would you reclaim from the model—and why does it matter to your listener? | Name a concrete change and the evidence heard; argue whether to act in code, reference, prompt or editing. |

### Mock quiz practice (slide 47)

Use three ungraded prompts to practise for the existing Week 7 quiz on weeks 1-6 and the playlist. Students answer aloud, privately or by a show of hands; no additional ClassPoint activities. Discuss the answers from speaker notes. Cover MIDI versus recorded audio, why a handwritten probability table remains Machine A despite chance, and why codec tokens are not necessarily musical notes. Do not reinstate the original draft's eight quiz slides or graded captures. The instructor can adapt the explanation to actual misunderstandings without fabricating a response distribution.

## Challenge 5 - sound for a product (slide 48)

The existing weekly challenge remains **up to 30 seconds of sound**, collected through Canvas using the confirmed destination/timing. The workshop result is a starting point, not a new assessment component. Revise one sonic decision deliberately; retain the brief, sources, code/prompt where applicable, available tool/model details and what was kept, rejected or supplied. Keep a screenshot/image of the code, timeline, waveform or spectrogram as process evidence **alongside** the playable sound, not as its substitute. Verify permission before sharing generated or supplied material. Do not invent a submission deadline or add compulsory intermediate captures.

## Reminder of the individual reflection brief (slide 49)

The approved syllabus remains unchanged: **20% individual reflection**, about **1000 words** on AI's role in the student's creative process, particularly **Machine A versus Machine B**, using **at least three of their own experiments from the weekly challenges (weeks 2-6), with images**, ending with a short note on **how AI was used to write it**. Submit on **Canvas in Week 7**. Preserve the current rubric: understanding 30%, argument/critical thinking 30%, evidence/examples 20%, clarity/structure/style 10%, engagement/originality 10%. A missing AI-writing process note costs one grade band on clarity/style; invented citations fail the assignment. Sound can contribute one experiment with an appropriate process image; it does not replace all three or remove the image requirement. The Week 7 quiz remains 10%; these ClassPoint answers add no new assessment weight.

Offer TA draft support, not a required new draft submission. Encourage claim -> evidence -> interpretation: which choice was expressed, which was delegated, what the result showed, and why the next intervention belonged in code, prompt, selection or editing. The two ClassPoint answers are possible arguments to develop, not mandated essay sections. Do not treat tool praise or an attractive output as sufficient evidence.

## Sources and teaching material

- Current `syllabus/SD2112-syllabus-2026.md`: Week 6 sound, Challenge 5, Week 7 quiz/reflection and unchanged assessment; Week 5 lesson plan supplies the established theory/break/demo/setup/40-minute structure.
- [Original course-refresh PR #3](https://github.com/venetanji/sd2112-teaching/pull/3), Week 6 lesson plan: useful representation/history/model themes, **not** the current slide count, timing, platform, quiz count or three-round capture contract. Its waveform/loudness, spectrogram inversion, Markov-only music, product/legal and guaranteed-compliance shortcuts are corrected here.
- Gio's approved 50-slide order: title/agenda 1-2; listening/representations and four layers 3-13; A 14-20; B 21-28; agents/boundaries 29-31; break 32; workshop title/demo 33-34; setup/brief/spec/overview 35-38; demo/reference/revise/listen-save 39-42; one final collection 43; debrief 44; two deep ClassPoint answers 45-46; three mock prompts 47; Challenge 5 48; unchanged reflection 49; end 50.
- [Riffusion's original spectrogram-diffusion repository](https://github.com/riffusion/riffusion), for the historical example and reconstruction caveat; [MusicGen / AudioCraft](https://github.com/facebookresearch/audiocraft), for documented codec-token generation. These are not evidence of Suno's proprietary internal architecture.
- [Strudel documentation](https://strudel.cc/learn/), the cumulative editor links in slides 9-12/19/35, and [Easel releases](https://github.com/venetanji/easel-client/releases): Gio verifies the actual classroom release, permitted tools and complete export/reference/completion/save route before class. Expected integration work is not proof that a release already includes it.
- [Suno consumer terms](https://suno.com/terms-of-service), revised 10 August 2026/effective 3 September 2026 and checked for the revision on 9 October 2026: input licence, output assignment and approved-download conditions. These terms are not proof of the actual Easel/provider contract. [Suno rights help](https://help.suno.com/en/articles/2425729) may simplify or lag current terms; use primary terms for dated claims.
- Hong Kong Intellectual Property Department, 8 July 2024 consultation on copyright and AI: the relevant Hong Kong framework differs from US positions; do not import a blanket US copyright conclusion or give individual legal advice. Verify current primary guidance before teaching.

## What to keep after class

Retain the final playable result and students' own process records through approved course storage, not the public source repository. Note actual playback/export problems and tool queues for the next class. Preserve useful reflection themes without inventing quotes or exporting identities into public materials. Keep TA support records private. No student sound generation is needed to prepare this deck, and no new assessment is introduced.
