# Week 12 / local verification record

**21 October 2026 / local draft only / branch `docs/week12-planning` / PR #25 context.** No commit, push, PR update, merge, deployment or change to live teaching was performed. The parent/instructor still reviews this draft independently.

## Scope and outputs

Eight source files changed/added, all in this Week 12 worktree:

- `deck/week12.py`: 34 actual slides, including 30 timed slides and four reference slides; substantive native notes on every slide.
- `deck/week12_figures.py`: two original native editable conceptual diagrams, agent/harness loop and accessible privacy flow. No external/generated image dependency or sketch still.
- `lessons/week12-lesson-plan.md`: synchronized actual 34-slide map, exact 180-minute run of show, activity contracts, source and policy boundaries.
- `lessons/week12-speaker-notes.md`: all 34 native notes, compared exactly with source and both exported PPTX files.
- `lessons/week12-evidence-ledger.md`: primary claim/version/method/outcome/limit and archival comparison record.
- `lessons/week12-verification.md`: this record.
- `tests/test_week12_sequence.py`: 15 focused regressions.
- `deckgen.toml`: only `week12` appended to the build list. Navigation, site shell, workflows, syllabus, requirements pin, other weeks and shared generator unchanged.

Generated ignored artifacts:

- `_site/week12/index.html`: local HTML, not a published preview URL.
- `_site/week12/SD2112-week12.pdf`: standard Deckgen PDF, **34 pages**, 1440 x 810 pt.
- `export/week12.pptx` and `export/week12-classpoint.pptx`: **34 slides each**.
- `export/week12-activities.json`: short answers at **slides 3 and 30**; no workshop artifact collection.
- `export/preview/week12/slide-01.png` through `slide-34.png`: 34 native-layout previews; generator contact sheets also present.
- `export/docs/`: generated instructor documents, not public site publishing.

Targeted site builds contain only selected weeks. This local `_site/` is not evidence of a complete all-weeks course site, and no navigation/site registration for Week 12 was added under the authorized scope.

## Environment and build

All shell execution used the bound course node, from this worktree. It started clean on `docs/week12-planning`. Read workspace AGENTS, repo README, full current Week 12 plan/syllabus, Weeks 5-7 sources and the separate Week 8 draft for continuity. No unrelated worktree files changed.

Prepared this worktree's own environment:

```sh
uv venv .venv
uv pip install --python .venv/bin/python --link-mode=copy -r requirements.txt
npm install --prefix .venv --no-save --package-lock=false playwright@1.56.1
```

Retained `deckgen` Git pin `v0.11.2` (resolved commit `9990546c01865807e6aaac5aaa50977b4b6b916a`). No shared-package edits, pin upgrades or browser downloads. Used existing `/ms-playwright/chromium-1246/chrome-linux64/chrome` via `CHROMIUM` and the worktree's `.venv/node_modules` via `NODE_PATH`.

Final standard build command:

```sh
export NODE_PATH="$PWD/.venv/node_modules"
export CHROMIUM="$(printf '%s\n' /ms-playwright/chromium-*/chrome-linux*/chrome | head -n 1)"
test -x "$CHROMIUM"
node /home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/run.mjs -- .venv/bin/deckgen build week12
```

**Exit 0**, no text overflow, no missing still, PDF34/pages and both PPTX34/slides emitted. Final build log: `/home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/logs/run-1792564568082-4ef21d63-5da2-4daf-902e-924d489807e3/`. This was a standard full target build, not a `--no-pdf` substitute or manually printed PDF.

## Tests and native artifact checks

- Focused: `.venv/bin/python -m unittest discover -s tests -p test_week12_sequence.py -v` -> **15 tests pass**.
- Entire repository: `.venv/bin/python -m unittest discover -s tests -v` -> **114 tests pass**, including all 15 Week 12 tests.
- `git diff --check` passes.
- Tests cover source order, exact contiguous 180-minute timing, protected 15/30/35/20-minute break/walkthrough/mock/revision budgets, real slide map, exact notes companion, bounded visible evidence, non-chatbot/static fallback, ethical argument, assessment preservation, no final-quiz announcement, native bounds/chrome, attributed exact-version links and separate R2 link paragraphs.
- Actual deck invocation tested with synthetic report mappings: attach one answer URL, withhold a null/private entry, reject count/question drift, and allow empty/missing map. No fabricated live reports or real responses added.
- Both PPTX files contain **34/34 exact native notes matches** with the final source and companion; nine native reading hyperlinks each. Declared families: Inter, Inter Black, Inter ExtraBold, JetBrains Mono, JetBrains Mono Medium.
- Plain PPTX has no ACTIVITYMODEL tags. ClassPoint PPTX has exactly two actual ShortAnswerActivity DTOs, single response, names not hidden, quiz mode false; slide relationship inspection confirms tags on **3 and 30**. This is emitted-package verification, not a classroom ClassPoint add-in test.
- Two custom figures use editable native rectangles/text, with stage explanations interleaved for semantic reading order. Geometry tests ensure content remains above the footer and within the canvas. No shared renderer patch.

## Browser and all-slide visual review

Private QA root: `/home/venetanji/.openclaw/workspace-sd2112/tmp/weekly-draft-audit-20261021/week12/`.

Playwright 1.56.1 used the existing Chromium and a task-local HTTP server with correct CSS/JS/font MIME types. The server/browser closed at completion; no persistent preview service or automation was installed.

- **34/34 desktop captures**, 1920 x 1080, active `.slides > section.present`, after fonts and Reveal readiness.
- **34/34 mobile reading-mode captures**, 390 x 844 viewport, each actual `.handout .ho-slide` separately captured; not the hidden Reveal deck.
- **34/34 native-layout previews** visually inspected. All desktop/mobile/native slides reviewed in batches; stage order, title/body separation, attribution, figure captions, contrast and footer clearance checked.
- Final browser diagnostics: no body-box overflow, no horizontal/mobile content overflow, document scroll width **390 for viewport390**, no page-script errors and no failed local resource responses.
- **18 actual browser link activations**, nine in each view, covering the research and reference-shelf links. Visible active anchors were clicked; desktop opens a popup, mobile navigates in the same tab. The requested destination was intercepted with a local QA response to verify navigation without publisher cookie/login variability. This proves the active link target/behavior, **not successful full-text access at every external destination**. Source access is separately recorded in the ledger.
- Visible mobile **Deck view** and **Reading view** controls both exercised successfully.
- One observed issue corrected: Sharma's final-record and author-version links were in one newline-containing paragraph, which concatenated in native preview/mobile output. They are now separate native paragraphs on slides 13 and 32, with a regression test. Rebuilt and recaptured all slides; affected slides confirmed in all three views. No aesthetic cycling or shared-toolchain changes.
- Early browser QA assumed every link opened a popup and then checked a popup before its URL settled. The harness was corrected to handle mobile same-tab navigation and await the expected URL. These were QA-harness errors, not slide defects; final report passes.

QA contents:

- `desktop/01.png` ... `34.png`, `mobile/01.png` ... `34.png`.
- `desktop-sheet-01.jpg` ... `09.jpg`, `mobile-sheet-01.jpg` ... `09.jpg`, `native-sheet-01.jpg` ... `09.jpg`.
- `browser-qa.cjs`, `browser-report.json`, `native-report.json`.
- `unittest-week12.txt`, `unittest-all.txt`.
- `archive27.png`, `archive29.png`, `archive-synthesis.jpg`, archival page54-69 renders and `sources/archive54-69.txt`.

**Limits:** native previews and OOXML declarations are not the same as opening the PPTX on the classroom PowerPoint installation. No desktop PowerPoint/LibreOffice rendering, physical projector/mobile-device review, screen-reader user evaluation or classroom add-in run was available. Those remain pre-class checks; the deck does not claim validated accessibility, privacy or safety.

## Source access and teaching boundaries

Cecil et al.: published open full primary article read; supplements, data/scripts and preregistrations not independently audited. Sharma et al.: full primary **author preprint v2** read, not asserted identical to the final ACM typeset paper; interview preferences are not control efficacy. ReAct v3 and Model Cards v2 primary author texts read for mechanism/documentation. The Van Den Eede syllabus reading's full text was not newly retrieved; slide 8 labels its distinction as our working design distinction and does not attribute detailed claims to an unread theory text. An optional Anthropic mechanism page returned 403 and was not used as evidence. No ELIZA/current-incident/legal-ownership claims require verification because none were retained.

Archive PDF has70/pages: positions54-69 extracted/rendered and positions27/29 separately inspected. Editable OneDrive deck has71/slides and an extra Ask Me Anything at54; source comparison recorded in the plan/ledger. Old fair board, dates, exam, four-group feedback and PR3 tooling/logistics were not adopted.

No real participant test, third-party action/account, image upload, booking, purchase, private data collection or unlabelled model simulation. Existing A0 poster, 3-5 minute video and one-page mediation brief remain a 40% project. No new grade/deadline/submission; the existing Week12 readiness milestone is not cancelled. Final-quiz policy is neither announced nor cancelled.

## Remaining instructor decisions

1. Reconcile the current syllabus's Week13 final-quiz item with showcase-first direction before any operational announcement; no assumed question count, duration, platform or cancellation.
2. Confirm actual Canvas Week12 readiness/deadline instructions, room/displays, team count/pairing, accessibility needs, playback and facilitation roles.
3. Decide whether to use the two optional ClassPoint prompts; preflight classroom add-in/privacy/report settings. Oral/team-note alternatives are complete.
4. Independent parent/instructor content and visual review before any authorized commit/PR update or publication. No public preview URL is claimed by this local verification.

## Independent cross-week verification

Independent parent review on 21 October 2026, after authoring handoff:

- Re-ran the standard targeted build and repository tests on this branch: build exit 0; **114 tests passed**. All 34 PDF pages and 34 slides in each PPTX match source count; all native notes match the source and companion.
- Parent inspected all new desktop, mobile-handout and generator-native slides in independently captured contact sheets. Browser checks find no measured body/horizontal overflow, JavaScript errors or failed local resources. Native preview inspection does not establish Microsoft PowerPoint classroom rendering.
- Assembled a separate, detached, local-only integration checkout from unchanged main plus the six weekly source sets, combining only the build-list registrations. **The unfiltered 13-week HTML/PDF/PPTX build passes, and all 165 combined repository tests pass.** This is integration verification, not a merge or production deployment.
- Parent reviewed source/notes, activity pacing, assessment boundaries and archive continuity. Primary-source access/version limits in the evidence ledger remain in force; this is not replication or a claim to newly reread every reference independently.
- The registration regression now permits other weekly drafts while requiring Week 12 exactly once and retaining the earlier seven weeks; no navigation or other-week source was changed.
- Review evidence is retained outside tracked course sources at `tmp/weekly-draft-audit-20261021/week12/parent/`; combined build/test receipts and source hashes are in the adjacent audit root. Generated exports, QA screenshots and archived full papers are not staged.
- PR remains a draft; operational instructor decisions listed above are not invented or silently resolved. No merge, staging update or production change is authorized by these checks.
