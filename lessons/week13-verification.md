# SD2112 Week 13 - current reconciliation verification

Fresh checks: 22 October 2026, prepared detached worktree at `0fd7d93`. Current review student export: **33 slides**, with **four staff-only source objects excluded** (37 authored objects total). Earlier records below are historical and do not certify this revision.

- Own `.venv`: requirements Git pin `v0.11.2`, resolved Deckgen commit `9990546c01865807e6aaac5aaa50977b4b6b916a`; Playwright 1.56.1 installed only under `.venv`. Existing `/ms-playwright/chromium-1246/chrome-linux64/chrome` used; no package patch or browser download.
- Fresh `deckgen build --no-pdf week13` through the workspace output-budget wrapper: exit 0, 33 student HTML sections, 33 slides in both PPTX variants, no text overflow, no missing asset/still, zero ClassPoint activities. Full build receipt in task `week13/qa/build-receipt.txt`. Parent owns full-course PDF build; **no current PDF is generated or certified here**. PDF exclusion follows the same 33-slide `DECK`, but page count remains the parent's check.
- Focused Week 13 suite: **18 tests passed**. Complete repository suite: **145 tests passed**. `git diff --check` passed. Geometry contracts cover header x120/y184/w1680/h140/72, label/body gap52, citations y956; no shrinking body copy to force fit.
- Independent package audit: both native PPTX variants have **33 slides and 33 matching source notes**; companion has exact native transcripts. Four complete staff sections/notes retained only in `STAFF_SLIDES` and the companion; none in student slide XML or native note XML. Zero ClassPoint tag parts. Staff text absent from student HTML sections. Reports: `week13/qa/artifact-report.json`, `student-boundary-report.json`.
- Browser checks: all **33 desktop slides at 1920x1080** and all **33 visible mobile handout sections in a fresh 390x844 mobile context** captured; zero browser exceptions, missing local assets, body-text overflows or horizontal/mobile bounds failures. All eight resource anchors activated on desktop and mobile with destination interception; this proves actual activation/target, not publisher availability. Same-tab mobile links were returned with Back before checking the visible Deck view control; **Deck view passed**. Report: `week13/qa/browser-report.json`.
- Visually inspected all desktop, mobile and generator-native contact sheets, plus full-size conceptual recap/application captures. Titles, labels, body, citations and footer are separated; mobile question/example precedes argument/limit, and person/technology/world labels stay with their explanations. No new/source photo; the original diagram remains editable. Captures: `week13/qa/{desktop,mobile}/slide-*.png`, `{desktop,mobile,native}-sheet-*.jpg`; native originals remain `worktree/export/preview/week13/`.
- Source check: retained six-page Verbeek institutional copy rechecked in full, fresh visual renders of PDF positions 4 and 6. The printer example is attributed conceptual analysis, not a participant trial. Editorial photograph remains unported because no supported public-repository/Cloudflare reuse basis is established. Prior local asset and source remain unchanged.

## Unresolved Delivery Gates

No classroom room/media/access/PowerPoint/add-in test, live quiz preflight, staffing/rotation confirmation or hosted deployment is claimed. Published project 40% / A0 / 3-5 minute video / one-page mediation brief and final quiz20% / whole-course MC / last portion remain intact. Exact timetable remains conditional `180 - Q - A - 15`; no new activities, assessment rules, deadlines or class minutes. User-facing preview publication, full 13-week integration/PDF verification, commits/pushes and PR handling remain with the parent.

## Historical Evidence / Retained Without Re-certification

# SD2112 Week 13 - verification record

## Historical review-fix verification: 21 October 2026

That reviewed export had **28 slides**. The four staff-only readiness/provenance sections are retained in `week13-notes.md` and separate source objects, never included in the exported deck. The old 32-slide output below is historical, not the current student artifact. Student-facing production disclaimers were replaced with useful actions.

- New regression failed against the previous source before the fix. Full repository suite now passes: **114 tests** (`python -m unittest discover -s tests`). Existing Deckgen image ResourceWarnings remain; they are not new failures.
- `deckgen build week13 --no-pdf` passed with pinned Deckgen v0.11.2 (`9990546c01865807e6aaac5aaa50977b4b6b916a`). HTML, both PPTX variants, native previews and companion documents were generated; no text-overflow failure.
- Inspected the changed generator-native previews. This is not Microsoft PowerPoint/ClassPoint or full browser/mobile certification.
- A local PDF preflight using the Week 8 build could not launch Chromium: the execution sandbox rejects its socket call (`Operation not permitted`). PDF rendering is not claimed for these changed sources; the affected-week CI build must verify it. No security restriction was bypassed.
- Generated exports, screenshots and local logs remain outside version control. No merge, production deployment or assessment-platform change.
- Independently inspected both PPTX packages: 28 slides and 28 exact source-note matches in each; no staff gate text. Generated HTML has exactly 28 sections and no staff gates. The staff companion preservation test covers every retained staff paragraph and note.

## Prior authoring evidence (historical)

The record below describes the previous source/export version and is retained for provenance. Its full PDF/browser checks do not certify the changed output above.

Local review draft, 21 October 2026, branch `docs/week13-planning`, isolated `week13-worktree`. Initial tracked worktree status was clean. No commit, push, PR update, merge or deployment was performed. This is actual built teaching material, not a plan-only result; operational readiness is separate.

## Scope and outputs

- 32 slides: 28 main-route teaching/showcase slides, four explicitly marked instructor-review readiness/provenance appendix slides. All 32 have substantive source/native speaker notes; companion notes cover every slide and distinguish spoken prompts from submissions.
- New course sources: `deck/week13.py`, `lessons/week13-notes.md`, `lessons/week13-sources.md`, this record and `tests/test_week13_sequence.py`.
- Updated `lessons/week13-lesson-plan.md` with the actual slide map and explicit readiness gates. `deckgen.toml` adds only `week13` to the existing build list; no navigation, site, syllabus, workflow, shared generator or other-week source changes.
- Original editable native person/technology/world figure on slide 18. No new image assets or browser-dependent sketches are needed.
- Local HTML: `_site/week13/index.html`; PDF: `_site/week13/SD2112-week13.pdf` (32 pages). Plain native `export/week13.pptx` and ClassPoint-ready `export/week13-classpoint.pptx` (32 slides each); generated lesson-plan DOCX/HTML and preview images remain ignored build outputs.

## Environment and build

Prepared this checkout's own `.venv` with `uv venv .venv`, `uv pip install --python .venv/bin/python --link-mode=copy -r requirements.txt` and `npm install --prefix .venv --no-save --package-lock=false playwright@1.56.1`. Requirements retain the repository's Deckgen `v0.11.2` Git pin, resolving to `9990546c01865807e6aaac5aaa50977b4b6b916a`. Installed Python package metadata reports `0.1.0`; that does not imply a pin change. No global install, package patch or browser download.

All shell work ran on the bound course node. Standard full target build:

```sh
export NODE_PATH="$PWD/.venv/node_modules"
export CHROMIUM="$(printf '%s\n' /ms-playwright/chromium-*/chrome-linux*/chrome | head -n 1)"
test -x "$CHROMIUM"
node /home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/run.mjs -- .venv/bin/deckgen build week13
```

Build passed, exit 0, PDF 32 pages, zero ClassPoint activities, no generator text overflow or missing still errors. Build log evidence is retained under the workspace `.openclaw/output-budget/logs/`; initial successful full build: `run-1792563745442-94e33ccc-3d0f-48aa-a8cc-81071c8b85ab`. Final rebuild after documentation synchronization also passed; see the QA summary JSON for its final checks.

Targeted build recreates `_site/` with Week 13 only; this is not a complete-course-site validation or a deployment.

## Tests

- Focused `test_week13_sequence.py`: 12/12 passed. Covers substantive route/order and main/appendix boundary; unchanged deliverables/rubric; no new collection/peer marks; static manual holds; published quiz and conditional reserve; conceptual synthesis scope; fictional example/native figure reading order; native footer bounds and useful notes; descriptive native links; registration and document synchronization.
- Deck-level report integration is tested by executing the actual module with a patched recording wrapper. Missing/empty mapping is a safe no-op; synthetic nonempty mapping raises zero-activity count drift rather than silently inventing links. There are no questions to match, withhold or publish in this zero-collection deck.
- Entire existing repository suite plus Week 13: **111 tests passed**, exit 0. Retained log: `.openclaw/output-budget/logs/run-1792564154053-443f07e3-27e8-4ea3-8ddd-feabc33712b1`. No unrelated tests or course sources were changed.

## Visual and artifact QA

Evidence root, outside tracked sources:
`/home/venetanji/.openclaw/workspace-sd2112/tmp/weekly-draft-audit-20261021/week13/`.

- Captured and visually inspected all 32 active projected HTML slides at a 1440 x 810 browser viewport (`desktop/`), with fonts loaded and Reveal ready. Four `desktop-sheet-*.jpg` review sheets cover every slide.
- Captured and visually inspected all 32 actual visible mobile `.handout .ho-slide` sections at 390 x 844 (`mobile/`), not the hidden Reveal deck. Four `mobile-sheet-*.jpg` sheets cover every slide; reading order of the native diagram is person, technology, world, then the question. No horizontal body/handout overflow was detected; no observed clipping or footer collisions in visual review. Mobile Deck control switches correctly.
- Visually inspected all 32 generator PNG previews used for native geometry (`native-sheet-*.jpg`; originals in `export/preview/week13/`). This is generator-native preview inspection, **not rendering in Microsoft PowerPoint**. No missing text/figure element or observed clipping. Actual Office font substitution/animations remain a classroom-device check.
- `native-artifact-report.json`: both PPTX packages have 32 slides, 32 notes, 274 editable text shapes, six real hyperlink relationships and zero `ACTIVITYMODEL` tags. Fonts declare Inter, Inter Black, Inter ExtraBold and JetBrains Mono Medium. Activity manifest has no activity entries, matching zero collections.
- `browser-report.json`: 32 desktop, 32 mobile sections, no browser page errors, zero measured horizontal overflow cases. All five resource-shelf links activated successfully from the active desktop slide and visible mobile handout, yielding 10 intended navigation destinations. Destinations were intercepted with task-local test pages to verify actual click routing without relying on external network; this establishes activation, not live publisher availability or authenticated access. The separate rubric link uses the same native URL mechanism and is also present in both PPTXs.
- Direct fetch of the Verbeek DOI returned 406; DOI/title matched ACM and institutional search records. Thesis resource separately returned HTTP 200, redirected to its canonical extensionless literature-review route. No newly reviewed full article or live classroom access is claimed.
- `qa-browser.cjs`, `qa-visual.py`, the contact sheets and evidence JSON are retained for reproduction. An initial contact-sheet helper expected static fonts; it failed before creating sheets, was corrected to the installed Inter variable font, then completed. No course/source rendering fix was required.

## Historical archive and reference access

All five archived Week 13 slide XML parts, the sole notes part and embedded core/app/custom metadata were read. Core created/modified timestamps and explicit dates support a 2025 saved artifact; filename alone is not the dating evidence. The archive includes a fair, feedback and an old Week 14 exam announcement; only the broad fair/feedback intent informs this new draft. The sole notes part is only a slide number. No historical date, room, visit quota, board URL, platform or exam setting is imported.

There is no Week 13 PDF in the 2025 directory. The editable archive exists. Since Office/LibreOffice is not installed, archived slides 4-5 were reconstructed using original text/shape geometry/pictures with an explicit non-Office label, then visually inspected. These are **not pixel-faithful original slide renders**. The old shared board was not opened. The leaderboard picture was not used or published.

Full Master PDF text and Week 12 PDF positions 54-69 were read; Master p. 21 and Week 12 p. 60 were rendered and inspected. Supporting files and archive hash/metadata are in the QA root and `lessons/week13-sources.md`. Historical overbroad legal, deterministic recommender and chronology claims are not repeated as current facts.

## Remaining instructor decisions and limits

The draft is reviewable, not operationally finalized. Confirm the authorized resolution of the published 20% Week 13 quiz; if retained here, count/time/platform/resources/attempts/access/instructions/recovery/results and private whole-course blueprint remain undecided. No default Q is supplied. The equation `180 - Q - A - 15` is conditional on retention and a provisional break, not a universal session schedule.

Date/room, actual teams, equitable presenting/visiting protocol, grader coverage/moderation, transitions, printing/display/media, actual existing Canvas submission route/deadlines, contingencies and feedback handling still require confirmation. Classroom display/font/audio/caption/offline playback/access and any retained assessment platform require actual authorized tests. Feedback is formative; no new deliverable, marks, peer quota or anonymity promise. No assessment bank, answers or student data appear in the new sources or outputs.

## Independent cross-week verification

Independent parent review on 21 October 2026, after authoring handoff:

- Re-ran the standard targeted build and repository tests on this branch: build exit 0; **112 tests passed**. All 32 PDF pages and 32 slides in each PPTX match source count; all native notes match the source and companion.
- Parent inspected all new desktop, mobile-handout and generator-native slides in independently captured contact sheets. Browser checks find no measured body/horizontal overflow, JavaScript errors or failed local resources. Native preview inspection does not establish Microsoft PowerPoint classroom rendering.
- Assembled a separate, detached, local-only integration checkout from unchanged main plus the six weekly source sets, combining only the build-list registrations. **The unfiltered 13-week HTML/PDF/PPTX build passes, and all 165 combined repository tests pass.** This is integration verification, not a merge or production deployment.
- Parent reviewed source/notes, activity pacing, assessment boundaries and archive continuity. Primary-source access/version limits in the evidence ledger remain in force; this is not replication or a claim to newly reread every reference independently.
- The facilitation tables are preserved. An exact 32-slide native-notes transcript was appended to the companion and covered by a thirteenth focused regression; final branch suite is 112 tests, superseding the authoring-pass count of 111.
- Review evidence is retained outside tracked course sources at `tmp/weekly-draft-audit-20261021/week13/parent/`; combined build/test receipts and source hashes are in the adjacent audit root. Generated exports, QA screenshots and archived full papers are not staged.
- PR remains a draft; operational instructor decisions listed above are not invented or silently resolved. No merge, staging update or production change is authorized by these checks.
