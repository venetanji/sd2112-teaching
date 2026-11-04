# Double Diamond / UX Design for Analytical Laboratory Software

Separate contributor entry: `deck/week10_nicolo.py`, branch `contrib/week10-nicolo-20261103`. The variant was based on the verified PR #23 snapshot `2330036350ed76a8433e8a6ac9b9fcb267412ccf`; it does not modify that PR, main, staging or the original Week 10 deck and companions. This is a draft preview, not a course release.

## Current structure

Nicolo's 4 Nov revisions retain four current-product phase slides and add three proposed AI concept slides. There are **17 slides total: one opening cover, seven introduction slides, one case cover, four current-product slides, three AI concept slides and one closing slide**. Previous versions remain recoverable in Git history.

| Slides | Section and sources | Current content |
|---|---|---|
| 01-07 | Double Diamond introduction | Verbatim opening definition; official diagram; principle / industry example / potential AI use for each phase; iteration; stakeholder management |
| 08 | UX Design for Analytical Laboratory Software | Case cover, included in Discover's speaking allocation |
| 09 | Discover: 3.pdf and 5.pdf, PDF page 1 each | Inexperienced Lab Analyst; cumbersome workflows and transcription errors; five-step paper-based workflow with return loop; genuine laboratory photograph |
| 10 | Define: 7.pdf, PDF page 1 | Three leading principles, original questions, and their exact Task Completion Rate / Ease of use / Time on Task associations |
| 11 | Develop: 8.pdf and 9.pdf, PDF page 1 each | Barcode scanner as primary input; automatic next-field focus; genuine historical predefined-list first draft; sequential constraints and missing source-container validation |
| 12 | Deliver: 16.pdf and 17.pdf, PDF page 1 each | Aligned quantitative/qualitative/wishes columns; italic participant quotes; original screenshot and complete looping video |
| 13-15 | Contributor-supplied ASL-1 / ASL-2 / ASL-3 concept images | Mirror-like UI; sample selection by barcode/container type; transfer registration and editable VLM comments with voice control |

The case has proposed speaking allocations of 1.25 / 1 / 1.25 / 2 / 0.5 / 0.75 / 1.25 minutes, plus two minutes of Q&A: ten minutes total, including the cover and one full 49.365-second video pass. Pause the loop after one pass to preserve that budget. The introduction remains separate and its duration is open. There are no ClassPoint collections, new submissions or assessment changes.

## Writing and visual contract

- Retain the source PDFs' language and project distinctions. Full participant quotations and supporting source sentences remain in notes; on-screen wishes shorten only the introductory wording. First-person participant quotations are attributed evidence, not a return to first-person speaker narration.
- Only the four introductory phase slides retain subtitles, lowercase before and after the tiny teal diamond. The case-phase slides retain only their phase title and highlighted DD map, with content raised to use the reclaimed space. Discover and Develop use `divergent thinking (creative thinking)`; Define and Deliver use `convergent thinking (logical thinking)`. Keep the one-third-size glyph, x-height alignment, equal explicit 12 px advances and renderer-normalized SVG font instance.
- The opening official diagram is 972 px wide, 90% of the preceding 1080 px version, centered on the slide. Its Problem Space and Solution Space labels stay centered above the appropriate diamonds. The full opening definition remains verbatim from the replacement DOCX; there is no three-layer explanation on the opener.
- Navigation maps use the same geometry and active-phase teal in the introduction and case. The iteration slide's map remains black and white, without any highlighted half. Its paragraph states that the phases do not all take the same amount of time; equal diagram halves do not represent equal phase durations.
- Retain the current typography, palette and section-cover treatment. Footer text is `Double Diamond` for slides 01-07 and `UX Design for Analytical Laboratory Software` for the cover and case. The case cover uses that same full title. The retained product image caption is `Workbench Tablet Device` and travels with the image to Deliver, rather than remaining attached to the old slide number.
- Retain Engineer in the industry examples. Slide 07's existing professional-role wording stays intact; only its footer and obsolete transition note are updated for the current case.
- Native notes and the Markdown notes companion must match. Keep native slide numbering continuous across both sections.

## Assets and source fidelity

Original input PDFs remain outside the repository. `deck/assets/week10/nicolo-portfolio-sources.json` records their hashes, PDF-page positions, phase mapping and extraction methods. The lab-context photograph is the original embedded JPEG from 5.pdf. The first-draft mockup is an authentic rendered crop from 9.pdf, including its magenta sequential-focus annotations and source placeholder identifiers; it is not a reconstructed final screen or an AI redesign.

The previously supplied product screenshot, full MP4 and genuine poster remain byte-identical to the preceding reviewed version `2fdb10f`. The screenshot preserves its 2420:1525 aspect ratio with `contain`, without cropping. The 1920x1080 video remains 49.365 seconds and untrimmed, with muted autoplay and continuous looping until paused; Space toggles play/pause in the parent slide, iframe body and focused native video. Repeated keydown events do not repeatedly toggle. The generic LIVE overlay and video caption are removed from the projected slide. Its digitally silent stream is described as no audio. The course-owned player uses the existing live-frame API, has a real poster for native output, and must stop when leaving the slide or opening reading view. Both media now belong to the single Deliver slide, superseding the earlier dedicated-video-slide arrangement to meet the four-slide case request.

## Evidence boundaries

| Evidence | Source/status | Boundary |
|---|---|---|
| DD phases and official opening diagram | Design Council, The Double Diamond, CC BY 4.0 | Retain source and licence links; small maps are simplified redraws without an endorsement claim |
| General principles, industry examples and potential GenAI uses | Contributor replacement DOCX | Keep personal project account, proposed AI ideas and independently established effects distinct |
| Target user, paper-based workflow and UX principles | 3.pdf, 5.pdf, 7.pdf | Project framing and evaluation dimensions, not a measured error-reduction claim |
| Scanner input and predefined-list draft | 8.pdf, 9.pdf | Preserve the failed sequential constraint and missing source-container validation; do not call the draft the final product |
| Three positive comments and two improvement wishes | 16.pdf | Wishes are requested capabilities, not evidence that those capabilities exist; priorities are not supplied |
| 30% faster than manual workflows / Time on Task | 17.pdf, reported comparative portfolio outcome | Do not convert to 30% less time; participant/task counts, raw timings, calculation, study date and uncertainty are not supplied |
| 1 Click to prepare and submit a sample list | 17.pdf, reported current-product outcome | Limited to that action; not the entire transfer workflow or an AI benefit |
| Testing methods | 16.pdf | Task-based usability testing with follow-up semi-structured interview; comparative manual/digital workflow testing; do not invent statistics |
| Original screenshot/video | Contributor supplied and already reviewed | Illustrates the current product, not independent efficiency evidence or proposed AI capability |
| Proposed AI redesign | Three genuine contributor-supplied ASL mockups and explanation | Proposed, not implemented or validated; no claimed AI efficiency benefit. Detecting an action does not verify volume, identity or successful transfer. VLM observations are editable drafts, not scientific conclusions. |
| Site-specific constraints | Speaker notes | Camera/privacy permission, lighting, occlusion, compute and system integration need actual site assessment; no laboratory-readiness audit claimed |

## Review permission and preservation

Nicolo authorized extracting relevant text and resources from the supplied PDFs to rewrite this separate presentation, following the already authorized GitHub/Cloudflare draft-preview path. This authorizes that draft use, not production release or independent verification of company rights. No confidential watermark, named research participant or real laboratory record was observed in the supplied PDF pages. Do not include the unused persona portrait or invent identifying information. Future supplied company assets need their own scoped assessment.

Keep the first reviewed commit `8cb0febbc29db33750d91c4514e9d4d3ee6f3505` and the successive reviewed versions in history; do not amend or force-push. The immediately preceding reviewed preview is `d02563425339f714b97fa41d1b86d50309aab0ef`. PR #23 was independently at `e9ad463c37db10e05c75449e3668d762d582972b` when this revision began; this variant must not change it. Verify the exact new Cloudflare check and route before delivering the next link. Do not merge or publish production.

## Latest layout revision

Slide 09 uses a smaller photograph, close-set problem labels and a vertically centred five-step workflow with return arrow. Slide 11 places the orange draft caption and constraints in the compact left column, with the ideal-UX statement under and aligned to the right-hand image. Slide 12 removes the ease-of-use block, reduces the screenshot, and uses the full bottom band for the three aligned findings columns. The three ASL images now use the replacement full-resolution 2420x1525 PNGs, retaining their supplied bytes and uncropped proportions; semantic order is list overlay, source tube, target vial, rather than Telegram upload order. Their hashes are recorded in the provenance manifest. The ASL-3 mockup includes an unvalidated processing recommendation; notes explicitly warn not to treat it as a laboratory instruction.

## Noon refinement

Deliver keeps only the caption `Workbench Tablet Device`, removes the projected Time on Task label while retaining the source measurement context in notes, and reduces the accent metrics to 44 / 36 px in a shorter block. The italic quotation block keeps its original 138 px height, using 25 px type, 1.08 line height and 10 px paragraph gaps. The original complete silent video now starts muted automatically and loops; Space remains play/pause and playback stops off-slide or in reading mode. The newly supplied PNG ASL assets are 2420x1525 (rather than the earlier compressed 1200x757 JPEGs) and remain uncropped.

## Opening and closing

The introduction now begins with the requested `Double Diamond \U0001f48e\U0001f48e` cover. The full definition/official-diagram slide remains immediately afterwards. The final slide contains only a centred, 48 px `thanks!`, without footer, logo or extra prompts. Inserting the cover shifts the former slide 12 Deliver layout to slide 13, and the ASL concept slides to 14-16; the closing is slide 17. The separate Q&A PowerPoint remains exactly four slides, one per TA.
