# Week 8 implementation and verification

## Current combined draft (21 October 2026)

Combines the remote news/CI head `da38455` with the independently reviewed paper-summary revision. The original local revision and previous immutable preview remain preserved. This section supersedes the historical receipts below; it does not authorize a merge or production release.

- **Combination:** the optional two-minute Kling news discussion replaces the old pair prompt at slide 3. All other 47 slide titles, projected text and native notes match the reviewed paper revision; all seven paper-image hashes match. Vendor claims, upcoming features and access/cost qualifications are retained.
- **Scope and pacing:** 48 exported slides: 37 main-route slides and 11 untimed appendix slides. Eight individually summarized core papers, three topic blocks and dense-figure enlargements remain inside the existing 35-minute evidence block. Break/demo/research/revision/comparison retain 15/15/40/25/10 minutes. No additional ClassPoint collection or assessment requirement.
- **Tests and registration:** all 118 repository tests pass, including both the news-opener and expanded-paper regression contracts. Weekly registration validation and `git diff --check` pass. No earlier-week, shared toolchain or workflow edit is introduced by this combination.
- **Build:** pinned targeted standard `deckgen build week08` succeeds: HTML, 48-page PDF, both 48-slide PowerPoints, native previews and companion documents. All 48 native notes match the source in each PowerPoint and the Markdown companion. Existing shared image-handle ResourceWarnings are not patched in the course source.
- **Browser/visual checks:** all 48 desktop slides and 48 actual mobile handout sections checked; no measured overflow, missing local resources or JavaScript errors. Mobile Deck view works; the news citation activates its intended primary URL. The opener and adjacent mediation/topic/paper slides were inspected at desktop/mobile sizes; the remaining paper material is unchanged from the reviewed revision. These checks do not certify classroom PowerPoint fonts, physical access, live generation or publisher availability.
- **Publication boundary:** requested update is draft PR #21 and its automatic Cloudflare review preview only. No merge, staging/production update, later-week edit or Canvas publication. Source-image notices remain explicit; see the specific criticism/review quotation assessment in `week08-paper-figures.md`, not an assertion that all figures are openly licensed. Exact-head remote CI/deployment results must be checked separately after pushing.

Private verification receipts: workspace `tmp/week08-combination-20261021/` (browser report, artifact report, content-identity check and source-merge receipt). Local test/build receipts: `run-1792590122288-5709901d-0240-4563-9690-343e9dd7076c` and `run-1792590146231-cbf7dbdc-c9d5-4595-9c5b-cdbfaf958e07`. Local outputs do not establish a live preview.

## Prior no-pre-reading / paper-figure revision (historical, 21 October 2026)

This section supersedes historical 32-main/42-total counts and no-publisher-figure statements below. The historical checks remain as dated receipts, not checks of this new revision. Work began from clean `29b2adf` on `docs/week08-humanizing-ai-plan`; only Week 8 sources/assets/tests/docs changed. No commit, push, PR edit, deployment or live-course change was made.

- **Coverage:** eight separately taught core papers, each with question/setup, finding, limit, design question and primary citation in 35-37 words excluding labels/source: R1/R2/R8 (perception and choice), R6/R7 (benefits and time horizon), R3/R4/R5 (agreement and overreliance). R9 has a 36-word optional appendix summary. R10-R13 remain clearly optional/later references, with no new required pre-reading.
- **Actual paper artwork:** R8 published Figure 1, PDF p. 5; R6 final Figure 3 A+B, p. 13; R7 accepted-manuscript Figure 1, PDF p. 11 / printed p. 10; R3 Figure 1 quantitative panel, p. 3; R4 final Science Figure 4 A+B, PDF p. 7 / printed 6 of 9; R5 January v1 Figure 2, PDF p. 23. R1/R2 instead have explicitly original method illustrations, not invented paper figures or empirical charts. Every selected chart retains axes, legends, conditions and uncertainty; images use contain, never cover/stretch. Clickable primary attribution is visible. Exact source URLs, version/access, crop geometry, hashes and rights gates are in `week08-paper-figures.md`.
- **Interpretation:** R7's 65%/59% initiation result is prose, not the displayed pathway diagram; mediation is not proof of mechanism. R4's final N=2,405 and Figure 4 replace no final-source facts with preprint values. R5's faulty-advice adoption is conditional on consultation, not all participants/trials. R3 does not establish that RLHF alone causes sycophancy. Existing R1 correction, R2 timing/attrition/nonsignificance and R8 chosen-not-random comparison caveats remain explicit in native notes.
- **Pacing:** 37 timed main slides plus 11 untimed appendix slides = 48 total. Three signposts, the R6/R7 split and two dense-figure follow-ups stay inside the original 35-minute evidence budget; no extra lecture minutes are assumed. The 15-minute break, 15-minute demo, 40-minute project search/read, 25-minute revision and 10-minute comparison are unchanged. No assessment, deadline, student upload, syllabus or later-week logistical gate is invented or changed.
- **Source reading:** full R1/R2/R8 primary texts reviewed for this pass, with R1 correction; collaborators fully read the identified R3-R7 primary versions. R4 separate supplement and R5 separate Web Appendices remain unreviewed. R9-R13 rely on the preceding full-text audit and are not claimed as freshly reread. R4 publisher blocks were not bypassed; public mirror primary text was cross-checked with publication/author records.
- **Fresh build and tests:** pinned Deckgen v0.11.2, worktree-local environment, existing node Chromium and output-budget wrapper. Fresh HTML, both 48-slide PPTX files, native previews and companion docs build successfully; focused Week 8 regressions **12/12 pass**, full repository suite **111/111 pass**, and `git diff --check` passes. All 48 native notes in each PPTX exactly match source notes; the Markdown companion matches those final notes. Declared Inter/JetBrains Mono families are preserved. Non-failing image-handle ResourceWarnings remain a shared Deckgen issue, not patched here.
- **Visual preflight:** fresh 1920x1080 desktop captures and 390x844 mobile handout captures cover all 48 sections; no measured body/horizontal overflow, missing local resources or JavaScript errors. Mobile Deck view toggle passes. All materially changed evidence/summary/signpost/detail slides and optional R9 were visually inspected in desktop, mobile and native previews. Initial R6/R4 tiny-label findings were corrected with two figure-led detail slides, then rebuilt/rechecked once. Journal chart labels on a phone can still require pinch zoom; explanatory summaries are readable in handout flow. Native previews do not establish actual Microsoft PowerPoint rendering or classroom font availability.
- **Links:** 40 visible anchors / 19 unique destinations. A visible R2 resource link activated the exact intended DOI under browser interception; this verifies activation, not reachability of every publisher endpoint. Existing access blocks remain disclosed.
- **Release gate:** R8 is verified CC BY 4.0; public-republication permission for the other exact rasters remains unresolved (especially AAAS/OUP artwork). Access is not reuse permission. Assets are local attributed teaching quotations for requested instructor review, not cleared public-release artwork. Resolve permission or an applicable teaching/quotation exception before public-repository/site release. No full-paper PDF or student data was added to tracked sources.

Evidence: `/home/venetanji/.openclaw/workspace-sd2112/tmp/paper-visual-revision-20261021/week08-report.md`, adjacent `week08/browser/browser-report.json`, `week08/native-structure.json`, desktop/mobile/native captures and full-text collaborator reports. A targeted local site is not a complete-course build or remote staging deployment. Instructor library login/network, optional agent demo, actual classroom fonts, exact dated timetable/coverage/ESFQ/quiz policy and proposal deadline remain preflight/confirmation gates.

## Historical verification receipts (superseded counts)


### Remote news integration receipt (historical; 42-slide counts superseded)

## Prior news-opener verification: 21 October 2026

The current export has **42 slides**. Slide 3 now integrates the dated Kling 4.0 news discussion as an optional two-minute replacement within the existing ten-minute opening. No slides or minutes were added; the 15-minute break, 40-minute research and 25-minute revision remain protected. The primary release was rechecked on 21 October; vendor claims and upcoming API/extension availability stay qualified.

- New regression failed against the previous source before the fix. Full repository suite now passes: **110 tests** (`python -m unittest discover -s tests`). Existing Deckgen image ResourceWarnings remain; they are not new failures.
- `deckgen build week08 --no-pdf` passed with pinned Deckgen v0.11.2 (`9990546c01865807e6aaac5aaa50977b4b6b916a`). HTML, both PPTX variants, native previews and companion documents were generated; no text-overflow failure.
- Inspected the changed generator-native previews. This is not Microsoft PowerPoint/ClassPoint or full browser/mobile certification.
- The attempted full PDF build could not launch local Chromium: the execution sandbox rejects its socket call (`Operation not permitted`). PDF rendering is not claimed for these changed sources; the affected-week CI build must verify it. No security restriction was bypassed.
- Generated exports, screenshots and local logs remain outside version control. No merge, production deployment or assessment-platform change.

## Prior authoring evidence (historical)

The record below describes the previous source/export version and is retained for provenance. Its full PDF/browser checks do not certify the changed output above.

Prepared 21 October 2026 for draft PR #21. Local source implementation, not a merge, release, deployment or confirmation of a dated class timetable.

## Produced

- `deck/week08.py`: 32 main slides plus ten untimed appendix slides, using the existing native Deckgen layouts, course typography, palette, footers and activity treatment.
- `deck/week08_figures.py`: original conceptual diagrams; the Week 5 mediation diagram is reused unchanged. No fabricated empirical chart or publisher figure.
- Native speaker notes on all 42 slides, with a synchronized Markdown companion in `week08-speaker-notes.md`.
- Complete 13-paper register, two primary-source evidence ledgers, and a fifteen-minute manual search demonstration with network/login/offline contingencies.
- Week 8 added to the configured build list only. Earlier decks, syllabus, landing page/navigation, workflows, assessment weights and submission requirements are unchanged. Generated exports are ignored, as required by this source-only repository.

## Evidence review

All R1-R13 primary article texts were reviewed in the explicitly identified versions, not merely abstracts. This is a focused claim check, not replication or systematic review. Full citation, access route, supporting page/section and limitation are in `week08-evidence-benefits.md` and `week08-evidence-risks.md`.

- R1 funding/competing-interest correction disclosed in main speaker notes and appendix.
- R2 authenticity result bounded by its six-month nonconcurrent reassessment; conflicting Discussion wording not repeated.
- R4 final Science paper and N=2,405 used; intentions/return preference not treated as long-term addiction or relationship breakdown.
- R5 January PsyArXiv v1 clearly marked working paper, not peer reviewed. No claim that the later SSRN/supplied version is byte-identical; no long-term deskilling claim.
- R6 final five-study publication used, not earlier six-study working paper; temporary relief distinguished from persistence.
- R7 self-reported initiation and factual-chat control distinguished from conversation quality or comparison to human rehearsal.
- R8 source choice distinguished from response ratings, repeated relationships and clinical outcomes.
- R9 symptom outcomes tied to the particular supervised intervention, waitlist and eligibility conditions. Published primary R4/R9 texts accessed via public mirrors after publisher blocks; supplements remain unreviewed. No full paper redistributed.
- Optional R10-R13 remain in the appendix, with qualitative/exploratory/task-specific limits. Vendor account explicitly identified; unverified Friend/BBC cases omitted.

## Local verification completed

- Pinned `requirements.txt` unchanged: Deckgen v0.11.2; per-worktree Python environment and Playwright 1.56.1; existing node Chromium used.
- Unfiltered `.venv/bin/deckgen build` passed for all eight configured weeks, including HTML, standard PDF printing, plain and ClassPoint-compatible PowerPoints, documents, preview images, text-overflow and report-map checks. All eight PDFs built; Week 8 has 42 pages.
- `.venv/bin/python -m unittest discover -s tests -v`: **107 tests passed**. Eight Week 8 regression tests cover timing/order, source boundaries, access fallback, scope/data output, references, notes synchronization, geometry and integration. Non-failing ResourceWarnings originate in Deckgen's image-preview file handles; no source/build failure occurred.
- Browser capture/review: all 42 projected HTML slides at 1920x1080 and all 42 mobile handout sections at 390x844; no body-text overflow, horizontal overflow, missing local resources or JavaScript errors. Mobile Deck view toggle checked. All 42 dual-renderer native preview slides inspected; revised slides confirmed after corrections.
- Final standard PDF page count and font embedding checked. Both PPTX files contain 42 slides, with every native speaker note matching the source and declared Inter/JetBrains Mono font families matching earlier classes. Native previews do not establish actual PowerPoint font resolution on the classroom PC; retain the repository classroom checklist.
- Thirty visible resource anchors across the deck, nineteen unique destinations. A visible R8 link was clicked and navigation to its intended DOI verified with an intercepted target (not a claim that every publisher endpoint is currently reachable). Primary-access success/blocks are recorded separately in the evidence ledgers.
- `git diff --check` passed. No student data, credentials, full-paper PDFs, generated decks or QA screenshots staged.

## Continuity/archive audit follow-up (21 October 2026)

This follow-up starts from clean `9d13b4b`, fast-forwarded only to the existing remote news handoff `c081d20`. The live PR #21 body and handoff were read; the news file remains unchanged and no news slides were added. The earlier all-eight-week build/107-test record above is retained as historical authoring evidence, not a claim that this follow-up rebuilt all weeks.

- Fixed slide 32 and its native/Markdown notes to state the confirmed Week 9 recommendations/bias, Week 10 interactive Double Diamond during instructor absence, Weeks 11-12 ethics and Week 13 showcase/reflection arc. Exact dates, coverage person, timetable, ESFQ arrangements and quiz policy remain unconfirmed; existing assessment requirements are not canceled or rewritten.
- Aligned the recovered plan/register with the actual cautious R2 slide: six-month reassessment, attrition/familiarity, authenticity-only significant source contrast, no clean causal label effect and no equivalence inference. Preserved R8's chosen-not-random source comparison and established-relationship/repeated-dialogue limits. Removed obsolete inclusion shorthand for the unverified Friend/BBC cases; the deck still omits them.
- Directly compared `references/2025/SD2112 - AI in Design - Week 8.pdf` (44 pages) with `references/onedrive-pptx/SD2112 - AI in Design - Week 8.pptx` (44 slides), focusing on PDF positions/PPTX slides 16-29, 31-39 and 41-43. Their relevant section sequence and R2 wording agree; this is not an assertion of full visual/byte identity. PDF positions 18, 21, 27, 38 and 41 were rendered and visually inspected. The source's diagram notation is historical teaching framing, not a faithful model-internals explanation. The R2 slide omits timing/attrition and overinterprets nonsignificance; the revision does not inherit those errors. Historical Blackboard, dates, team formation and table submission were not reinstated.
- Read both complete evidence ledgers and the thirteen-paper register; spot-checked retained R2 full primary text (methods 2.1-2.5, Results/Table 1) and R8 full published text (choice/rating methods and relationship limitations). This follow-up did not freshly reread all thirteen papers. All existing per-paper version/access qualifications remain intact, including R4/R9 mirror access and unreviewed supplements, R5 January v1/non-peer-review and unverified later version identity, R7 accepted manuscript, R11 author preprint and R6 final five-study publication.
- Focused regressions: **10 passed** (two added; both failed against the pre-fix content). Full repository suite: **109 passed**. Non-failing Deckgen image-handle ResourceWarnings remain unchanged. No shared toolchain patch was made.
- Exact requested `.venv/bin/deckgen build week08` passed with pinned v0.11.2, this worktree's `NODE_PATH`, existing `/ms-playwright` Chromium and the output-budget wrapper: standard 42-page PDF, both 42-slide PPTX files, native previews, HTML and companion documents. Text-overflow/report-map checks passed. Both PPTX files have 42/42 source-matching notes; source remains 32 main + 10 appendix and zero ClassPoint collections. PDF Inter/JetBrains Mono embedding checked.
- Fresh browser checks covered all 42 desktop slides (1920x1080) and all 42 mobile handout sections (390x844): no body/horizontal overflow, JavaScript errors or failed local resources. Mobile Deck view toggle passed. Thirty resource anchors/nineteen destinations remain; visible R1 link activation reached its intended DOI under interception (not proof of publisher availability). Only slide 32 materially changed visually; it was inspected in desktop, mobile and native preview, with no clipping/readability issue. Classroom Office font resolution still needs the normal PC check.
- QA evidence is local at `/home/venetanji/.openclaw/workspace-sd2112/tmp/weekly-draft-audit-20261021/week08/`: preserved `parent-baseline*`, `archive-week08*.txt`, `archive-page-*.png`, fresh `audit-structure.json`, `audit-browser/browser-report.json`, all fresh browser captures and `changed-slide32-desktop-mobile-native.jpg`. No QA or article files are added to git.
- No other weeks, site/navigation, syllabus, workflows or toolchain sources changed. No commit, push, PR edit, merge, deployment or live-course change was performed. The only history synchronization was the authorized clean fast-forward. Local `_site/` is the targeted Week 8 build, not a complete-course build or remote delivery.

## Exact local preview

From this branch's checkout on the prepared course node:

```bash
export NODE_PATH="$PWD/.venv/node_modules"
export CHROMIUM="$(printf '%s\n' /ms-playwright/chromium-*/chrome-linux*/chrome | head -n 1)"
test -x "$CHROMIUM"
node /home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/run.mjs -- .venv/bin/deckgen build week08
.venv/bin/python -m http.server 8088 --bind 127.0.0.1 --directory _site
```

Open `http://127.0.0.1:8088/week08/` on that machine. Press `S` for notes; mobile reading mode and Deck view are available. A targeted site build recreates `_site/` with that week; use the unfiltered build when checking a complete course site. This local server does not deploy or publish the course.

## Remaining instructor decisions

- Confirm the actual dated timetable/return clock time. Relative 15-minute break, 15-minute demo, 40-minute research, 25-minute revision and ten-minute comparison are preserved.
- Confirm formal one-page proposal instructions/deadline in Canvas. No new upload or grading requirement is created here; revised scope explicitly includes necessary data and collection limits.
- Decide whether to use the optional brief R9 contrast and whether to preflight a live agent comparison. Manual verification remains the default; Scopus metadata is not assumed to grant abstract/full-text access.
- Teaching direction is confirmed: Week 9 recommendations/bias; Week 10 interactive Double Diamond while the instructor is absent; Weeks 11-12 ethics; Week 13 showcase/reflection. Confirm exact dates, coverage person, timetable, ESFQ arrangements and quiz policy against current official instructions. November 6 is older planning shorthand, not a verified timetable; no assessment is canceled and the syllabus is not silently rewritten.
- Verify classroom PowerPoint fonts and the instructor's legitimate library access before teaching. No deployment was performed to provide a remote preview.

## Independent cross-week verification

Independent parent review on 21 October 2026, after authoring handoff:

- Re-ran the standard targeted build and repository tests on this branch: build exit 0; **109 tests passed**. All 42 PDF pages and 42 slides in each PPTX match source count; all native notes match the source and companion.
- Parent independently rechecked all 42 HTML/mobile sections and export notes; visually rechecked changed slide 32 in desktop, mobile and native preview. Previous full 42-slide visual evidence remains applicable to the unchanged slides. Browser checks find no measured body/horizontal overflow, JavaScript errors or failed local resources. Native preview inspection does not establish Microsoft PowerPoint classroom rendering.
- Assembled a separate, detached, local-only integration checkout from unchanged main plus the six weekly source sets, combining only the build-list registrations. **The unfiltered 13-week HTML/PDF/PPTX build passes, and all 165 combined repository tests pass.** This is integration verification, not a merge or production deployment.
- Parent reviewed source/notes, activity pacing, assessment boundaries and archive continuity. Primary-source access/version limits in the evidence ledger remain in force; this is not replication or a claim to newly reread every reference independently.
- Review evidence is retained outside tracked course sources at `tmp/weekly-draft-audit-20261021/week08/parent/`; combined build/test receipts and source hashes are in the adjacent audit root. Generated exports, QA screenshots and archived full papers are not staged.
- PR remains a draft; operational instructor decisions listed above are not invented or silently resolved. No merge, staging update or production change is authorized by these checks.
