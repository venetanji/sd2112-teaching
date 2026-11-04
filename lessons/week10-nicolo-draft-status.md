# Nicolo's separate Week 10 variant

Contributor branch: `contrib/week10-nicolo-20261103`, based on verified PR #23 head `2330036350ed76a8433e8a6ac9b9fcb267412ccf`. Nicolo approved public HTML review, and Gio authorized a separate GitHub branch push and Cloudflare preview. PR #23, main, staging and the original Week 10 deck and companions remain unchanged. This preview is not a course release.

Entry point: `deck/week10_nicolo.py`. Seven introduction slides, a case-study cover and eight case-content slides (including a dedicated video slide): 16 slides total. The introduction duration remains open. The case has a proposed eight-minute presentation plus two minutes Q&A, within ten minutes total; the cover is included in the first half-minute.

## Writing and navigation revision

- Preserve the first reviewed commit `8cb0febbc29db33750d91c4514e9d4d3ee6f3505` in history and on local backup branch `backup/week10-nicolo-first-review-8cb0feb`; do not amend or force-push it. Its immutable Cloudflare preview remains the first-review snapshot.
- Use the replacement document's direct wording and phase names, with an impersonal professional account as requested in the latest correction. Retain the three layers on the phase slides, labelled General Principles / Industry Example / Potential AI Use, and the approved privacy/data and wishes/priorities additions, without replacing the explanation with slogans. Keep pending case content explicit and use short, literal placeholder labels.
- Put a `space [diamond] thinking mode` subtitle under each of the four phase titles, rendered with an accent-teal diamond (U+25C6) at one third of the 34 px text size, with its visual center aligned to the measured x-height center: Discover and Develop use `Divergent Thinking (Creative Thinking)`; Define and Deliver use `Convergent Thinking (Logical Thinking)`. Use equal explicit spacing around the diamond, without repeating the phase title.
- `deck/week10_nicolo_figures.py` draws four small text-free navigation maps after the Design Council Double Diamond (CC BY 4.0, source and licence linked on the opening slide). The opening slide begins with the full definition verbatim from the replacement document (including its explanation of what the model is used for). No three-layer introduction appears on the opener; the larger official diagram takes the central stage. The official opening image remains unchanged; native Problem Space and Solution Space labels are centered above the corresponding diamonds. The navigation maps are simplified redraws: text and arrows omitted, all inactive halves black and white, only the active half teal. SVG and native PNG share the same geometry. The maps do not show an official recolored image or imply Design Council endorsement.

## Current instructions

- Introduction: retain the document's principle / professional account / potential GenAI use at each DD phase. Use official Design Council diagram with CC BY 4.0 attribution.
- Discover: emphasize users' AI needs, privacy attitudes, willingness to share and permissible AI data; willingness is not permission.
- Deliver: include what worked, user wishes and the priority of those wishes, alongside meaningful outcomes, failures and evidence limits.
- B1: the original 2420 x 1525 tablet screenshot and a 1920 x 1080 promotional video have been received and integrated locally. After the local-only notice, Nicolo requested the link to this revised deck on 4 Nov; that request authorizes the separate draft-branch/public-preview path including these supplied assets, not production release or independent verification of company rights. No reconstructed product images. The full 49.365-second video has a dedicated slide; it has a silent audio stream. The current screen, before/after areas and three proposed-screen placeholders all preserve the 2420:1525 aspect ratio without cropping. Replace Developer with Engineer outside slide 07, which remains unchanged.
- B2: qualitative positives and improvement wishes first; quantitative statements on a separate slide.
- B3: one before/after slide, then a three-screen annotated proposed-flow slide. No invented AI feature, actual screen or implementation claim.
- B4: investigate environmental/camera, site digital/cloud/integration, device compute and adaptation constraints. These are potential site-specific questions, not an audit of current lab infrastructure.

## Evidence and permissions ledger

| Claim or asset | Source and status | Remaining input or check |
|---|---|---|
| DD phases, iteration and official image | Official Design Council page, consulted 3 Nov 2026; existing unmodified course PNG; CC BY 4.0 | Retain source and licence links |
| Laboratory UX experience, learning the domain, workflow goals, co-design and usability testing | Nicolo's replacement DOCX attachment ending `3d5a17e8-e965-41f1-9206-db71041951e4.docx`; attributed personal account, not independent effect evidence | Contributor correction and public-sharing clearance |
| AI assistance in discovery, definition, prototyping and analysis | Prospective ideas in Nicolo's DOCX; not historical claims of tools used or benefits measured | Keep proposed label and evidence/permission limits |
| Week 8/9 links | Current course Python sources at the base: mediation/control, value versus proxy, privacy/data boundaries, representation and outcome testing | No new empirical findings inferred from transfer |
| Two positive qualitative findings and improvement wishes | Requested by Nicolo, not supplied | Actual observations, context, priority and permission; no fake quotes |
| 30% faster than manual workflows | Speaker-supplied current-product statement in 3 Nov feedback; context pending; not independently verified | Define faster vs less time, task, manual comparator, method, source, uncertainty and permission |
| One click to prepare and submit a sample list | Speaker-supplied current-product statement; context pending, not an AI redesign result | Action boundaries, setup excluded/included, actual screen and permission |
| Original tablet screenshot and promotional video | Received from Nicolo on 4 Nov 2026; original files inspected; contributor requested sharing this revised deck after the local-only notice | Contributor-authorized draft GitHub/HTML preview only; no production-release or independent company-rights claim |
| Portfolio slides, additional intended-use material and product context | Not yet supplied | Receive actual files and confirm sharing rights separately |
| Before/after and three-screen proposed AI flow | Requested structure only | Actual proposal, UX goals, screens, AI/human responsibilities and annotations |
| Low light, cameras, digital/cloud readiness, compute and device adaptation | Contributor's potential constraint categories | Site-specific user, IT, lab and engineering evidence; no universal industry-readiness claim |

## Review boundary

This is not a completed case study or classroom-tested presentation. Native notes retain explanations and evidence boundaries. No ClassPoint collections, new submissions or assessment changes. No paid image/video generation or additional cloud-agent execution is needed. Public HTML review of this draft is approved. Additional portfolio material remains pending; Nicolo requested the link to this revised deck on 4 Nov after the public-sharing boundary was explained. That authorizes the supplied screenshot, video and extracted poster in this draft preview only. It does not authorize exposing future company assets merely because they are supplied for drafting.

## 4 Nov local revision

The 49.365-second original video is not trimmed or looped and is not represented as AI functionality. Proposed case allocations are 0.5 / 1 / 1 / 1 / 1.5 / 1.5 / 1 / 0.5 minutes, plus 2 minutes Q&A: 10 minutes including full video playback. No extra case time is added. The course-owned video player uses the pinned generator's existing live-frame API with a genuine poster for native exports; no shared package changes. Playback is user-initiated and pauses when leaving the slide or switching to reading view. The local-only QA was followed by Nicolo's explicit request to share this revised deck. Publish on the separate contributor branch and verify its exact-revision preview; do not merge or alter PR #23.

Local QA completed 4 Nov: 27 Week 10 tests pass; both native exports retain all 16 source notes and the exact opening definition. Browser and raster checks confirm a 34/3 px separator with its center within 0.2 px of the browser-measured x-height center. All 16 desktop/mobile sections and source links pass; original-video playback, seeking, stopping on slide leave, stopping in reading mode and mobile-link playback pass without page errors. Supplied screenshot and MP4 copies are byte-identical to the attachments. Public branch remains at `847e96556f3974574764a983595b0b9a3332244d`; no commit or push was made for this local revision.

## 4 Nov requested preview publication

At 05:09 UTC, Nicolo requested the link to this revision after the prior reply explained that public GitHub/preview sharing included the supplied assets. Proceed with the authorized separate contributor-branch preview, preserving all existing commits and the original deck. PR #23 has independently advanced to `e9ad463c37db10e05c75449e3668d762d582972b`; do not change it. The earlier 03:30 local-only QA receipt remains historical. This preview authorization is not a production release or a claim of independently verified rights.

## 4 Nov thinking-mode and iteration revision

Requested at 08:20 UTC: scale the opening official diagram to 90% of the preceding reviewed width (1080 to 972 design pixels), retaining its center and aligning the Problem Space / Solution Space labels above their diamonds. The four phase subtitles now show the appropriate Divergent Thinking (Creative Thinking) / Convergent Thinking (Logical Thinking) wording. The tiny teal separator retains its one-third size and x-height alignment. Equal explicit 12 px advance gaps replace renderer-dependent spaces; one SVG text run shapes the three spans naturally. Normalize local SVG optical sizing and stylistic features to match the raster font instance, rather than guessing fixed browser positions from mismatched PIL metrics.

Slide 06 has the same upper-right navigation geometry as the phase slides, with all four halves white and black outlines, no accent highlight. Its time-prioritisation paragraph adds: The phases do not all take the same amount of time. Notes distinguish equal-sized map halves from actual phase durations. The case, its supplied media, 10-minute inclusive timing, slide 07 wording, original deck and protected PR remain unchanged.
