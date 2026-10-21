# Week 8 implementation and verification

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
