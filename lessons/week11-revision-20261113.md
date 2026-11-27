# Week 11 clarity revision / 13 November 2026

Instructor request: simplify the guide example and project activity; give each of four topics a section slide; highlight paper findings; restore opening news and a deep question; add a group-project AMA directly after the break. Activity clarification: apply ONE of the four topics to the group's own project.

## Changes

- Fictional AI museum guide: an old fishing boat, museum facts, and the fishing family's experience. If the family has not been interviewed, say so rather than inventing its story.
- Four explicit sections: mediation; curation and power; agency and authorship; responsibility. Papers are grouped under the relevant topic, not a detached paper list.
- Five result/argument panels have bold text, pale-teal backing and an orange edge. Empirical findings, interview reports, a documentation proposal and an Office position retain distinct labels, visible limitations and source figures.
- News slides 2-3 cite the 12 November market close and NVIDIA's 12 November CEO-transition release. Resignation is confirmed, retirement is not established. Opening discussion immediately follows: 'If AI makes the work, what makes it yours?'
- Break remains 75-90. AMA is the immediately following slide, 90-105.
- One project activity: choose a topic and one part of the project, identify one problem, sketch/rewrite one change, explain it in 60 seconds and improve it after one peer question. No separate audit, extra worksheet, upload or grading requirement.
- 36 timed slides + 2 optional reference slides = 38. Exactly 180 minutes. Existing project brief and Week 13 quiz+posters unchanged. Week 12 / PR25 untouched.

## Initial clarity QA / before ClassPoint requests

- Full unfiltered `deckgen build --no-pdf` passed for all 10 registered decks; this local run does not claim PDF verification.
- Post-build full regression suite: **180 tests passed, no skips**. Existing nonblocking image ResourceWarnings from the pinned generator remain previously reported; no package patch or upgrade.
- Native speaker notes: **38/38 exactly match final source in both plain and ClassPoint PPTX**. Companion regenerated from the same source. Zero ClassPoint collections.
- Desktop 1600x900 and fresh mobile 390x844: 38/38 sections; zero page errors, missing images or mobile horizontal overflow. Reading/deck toggle works. Final screenshots and browser report retained under ignored `export/qa-week11/`.
- All changed desktop/native layouts inspected; representative mobile news, finding and activity captures inspected. Seven tight display-heading line-box warnings were visually checked: no glyph clipping or adjacent-content collision. No body-text overflow was reported.
- Existing empirical claims and source-image provenance are retained, with simplified instructor examples and current timing. News primary/reporting sources directly read; no financial advice, motive speculation or unverified retirement claim.

## Delivery boundary

Prepared from verified PR24 head `0cf5bfa23c1951c20f01a47c9edf39daa53493bc` in a separate worktree. Only Week11 source, tests and companions change. The existing draft PR may receive this review update; main, staging and PR25 must not change. Exact-head CI and hosted preview identity are verified separately in the PR handoff. Do not send interim PDF/PPTX or QA attachments.

## Instructor-authorized release update

The instructor subsequently requested publication and merging, plus ClassPoint submissions for the AMA and final exercise. This supersedes the earlier draft-only delivery boundary and zero-collection state.

- Slide 29 immediately follows the full break and collects AMA questions, up to three per person. Slide 35 collects one revised project summary per group. Both use the existing in-slide short-answer button and the presenter's scrollable answer overlay.
- Activity instructions, native speaker notes and the companion describe the same classroom collection. The deck remains 38 slides and exactly 180 minutes, with no new assessment or Canvas deadline.
- Week 11 appears in the homepage, PDF downloads and shared navigation. Export assertions skip an unselected Week 11 build while requiring the complete artifact set when present.
- Fresh Week 11 HTML and both PowerPoint exports build with two short-answer activities (slides 29 and 35). Full local regression: 183 tests pass with five existing skips for unbuilt exports outside this selected-week run. PDF and hosted release checks run separately in CI.
