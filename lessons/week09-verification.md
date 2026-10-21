# Week 9 local draft verification

Date: 21 October 2026. Branch: `docs/week09-planning`. Worktree: `/home/venetanji/.openclaw/workspace-sd2112/week09-worktree`. Initial `git status --short` was empty; existing lesson plan preserved as foundation and updated to the actual map. No commit, push, PR update, merge or deployment authorized/performed.

## Source and scope

- **31 slides**: 28 main-route slides + 3 untimed reference-shelf slides. Five linked primary references; detailed notes on all 31 slides; native editable diagram, interaction matrix and deterministic ranking table/results. No generated/photo assets or borrowed screenshots needed.
- Main source `deck/week09.py`, reproducible toy `deck/week09_demo.py`, tests `tests/test_week09_sequence.py`, actual lesson plan, evidence/access/version ledger, notes companion and this record.
- Only `week09` appended to the existing `deckgen.toml` build list. No site landing/nav, workflows, syllabus, shared generator, requirement pin or other week edited.
- Exact allocations retained: 75-90 break (15 min), 90-105 demo (15 min), 105-135 research (30 min), 135-165 redesign/test (30 min = 20+10), 165-180 debrief (15 min). No new grade, collection/submission, deadline or account; no private/student data. No ClassPoint activities are added. Report hook is retained; no synthetic live report mappings.

## Build environment and completed checks

Prepared worktree-local `.venv` from unchanged `requirements.txt` (`v0.11.2` Git pin resolves to `9990546c01865807e6aaac5aaa50977b4b6b916a`). Used `uv pip install --python .venv/bin/python --link-mode=copy -r requirements.txt` and Playwright 1.56.1 under `.venv/node_modules`. No global install, generator patch or browser download.

Full target-week build command on the bound course node:

```sh
export NODE_PATH="$PWD/.venv/node_modules"
export CHROMIUM="$(printf '%s\n' /ms-playwright/chromium-*/chrome-linux*/chrome | head -n 1)"
test -x "$CHROMIUM"
node /home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/run.mjs -- .venv/bin/deckgen build week09
```

- Standard full target build succeeds with exit 0, no stderr/text-overflow failure. Final build log: `.openclaw/output-budget/logs/run-1792564267710-be915489-ba02-4106-a75f-a892cd681da8` under the shared workspace. Fresh HTML, **31-page PDF**, plain PPTX and ClassPoint PPTX, preview images, zero-entry activity manifest and document exports generated. Actual `pdfinfo` page count agrees with source (31).
- `.venv/bin/python -m unittest discover -s tests -p 'test_week09_sequence.py' -v`: **12 tests pass**, including protected sequence/timing, visible evidence limits, primary hyperlink runs, toy arithmetic/endpoints/ties/invalid inputs, original no-collection contract, actual report-hook invocation/no-op/stale-map rejection, canvas/footer bounds, lesson-map/native-note companion consistency, and all exported notes in both PPTX variants.
- Full existing suite `.venv/bin/python -m unittest discover -s tests -v`: **111 tests pass** in 22.502 seconds; log retained as `full-tests.log` in the QA root.
- Optional toy terminal run reproduces rule A A7.4/B7.0/C5.6/D5.0 and rule B D7.5/C7.1/B4.5/A3.4. No model, network, seed or service required. All input scores, formulas and result lists remain visible if the terminal is unavailable.
- Browser QA uses installed Chromium (`chromium-1246`) and Playwright 1.56.1: all **31 desktop slides at 1920x1080** and **31 mobile handout sections at 390x844** captured. No browser page errors or horizontal overflow in the measured views. Mobile is checked through `.handout .ho-slide`, not hidden Reveal navigation.
- All source links are native `Run.url` hyperlinks; nine rendered anchor instances are visible on their active slides. All nine links were clicked in **both** views with observed request URLs matching their intended targets; mobile Deck view and Reading view controls both work. Source-link activation is intercepted only to verify the intended navigation destination without making publisher/network availability part of a click test. Successful link activation does not claim current classroom internet access.
- All 31 Deckgen native preview PNGs, all desktop captures and all mobile captures inspected in batched sheets; corrected the interaction-matrix and toy-score cells to carry their own labels when reflowed on mobile. Targeted final screenshots of slides 7 and 20 confirm that correction in desktop, mobile and native previews. Native notes extracted from **both** PPTX files match every source note and the companion; no claim of actual desktop PowerPoint font resolution is made.
- `git diff --check` passes. Focused source changes only; all build outputs remain ignored.

## QA locations

Internal QA root (outside tracked repository files):
`/home/venetanji/.openclaw/workspace-sd2112/tmp/weekly-draft-audit-20261021/week09/`

- `full-tests.log`: all 111 existing and new tests.
- `browser-qa.json`, `qa.cjs`: slide counts, errors, visible anchors, horizontal bounds and link activation.
- `desktop/01.png` through `31.png`; `mobile/01.png` through `31.png`.
- `desktop-sheet-1.jpg` through `4.jpg`, `mobile-sheet-1.jpg` through `4.jpg`, `native-sheet-1.jpg` through `4.jpg`: full visual audit.
- `research/`: internal full-text consultation extracts and historical render/selected PPTX comparison. These are evidence aids, not public redistributed teaching assets.
- Ignored native previews: `export/preview/week09/slide-01.png` through `slide-31.png`.
- Local review HTML: `_site/week09/index.html`; not a reachable deployed preview URL. Parent may serve it through its approved local-preview route. Generated PDF/PPTX are internal QA, not unsolicited Telegram attachments.

## Evidence/access boundaries and instructor decisions

- Read relevant recovered 2025 Week 9 PDF ranges 23-45, 47-49; render diagram/image-heavy pages. Compared selected content/order with the same week's 50-slide OneDrive PPTX rather than assuming identical exports. The updated deck corrects universal exposure-to-polarization wording and does not reuse an unattributable labour quotation.
- Gauthier et al. **2026 published main full text** concerns a **2023** active-US-X field experiment. Glickman/Sharot **online 2024 / issue 2025 main full text** concerns controlled judgement tasks, not a live feed effect size. Supplements and replication data/code not independently reviewed/reproduced. Other primary-paper consultation scope and exact versions recorded in `week09-evidence-ledger.md`.
- Proposed diversity/reset/override controls are hypotheses to test, not validated safeguards or legal compliance. No current platform internals or universal algorithm-radicalization claims.
- Instructor must reconcile intended Week 8/9/10 sequence with unchanged published syllabus (which places recommendation systems in Week 10), confirm actual class date and current Canvas concept-board/bias-register scope/timing, and choose one short research excerpt. No confirmed date invented.
- Native PPTX XML/Deckgen previews and browser/PDF checks do **not** reproduce Microsoft PowerPoint's on-device rendering, classroom projection readability, actual ClassPoint add-in behaviour or instructor approval. No new ClassPoint collection needs classroom setup for this draft.
- This is a full **target-week** export check, not a complete course-site rebuild. No public preview/deployment, commit, push or PR mutation. Parent independent review/build remains required by the assignment.

## Independent cross-week verification

Independent parent review on 21 October 2026, after authoring handoff:

- Re-ran the standard targeted build and repository tests on this branch: build exit 0; **111 tests passed**. All 31 PDF pages and 31 slides in each PPTX match source count; all native notes match the source and companion.
- Parent inspected all new desktop, mobile-handout and generator-native slides in independently captured contact sheets. Browser checks find no measured body/horizontal overflow, JavaScript errors or failed local resources. Native preview inspection does not establish Microsoft PowerPoint classroom rendering.
- Assembled a separate, detached, local-only integration checkout from unchanged main plus the six weekly source sets, combining only the build-list registrations. **The unfiltered 13-week HTML/PDF/PPTX build passes, and all 165 combined repository tests pass.** This is integration verification, not a merge or production deployment.
- Parent reviewed source/notes, activity pacing, assessment boundaries and archive continuity. Primary-source access/version limits in the evidence ledger remain in force; this is not replication or a claim to newly reread every reference independently.
- The registration regression now permits later weeks while requiring Week 9 exactly once and retaining the earlier seven weeks; the combined run exposed the old last-week-only assumption.
- Review evidence is retained outside tracked course sources at `tmp/weekly-draft-audit-20261021/week09/parent/`; combined build/test receipts and source hashes are in the adjacent audit root. Generated exports, QA screenshots and archived full papers are not staged.
- PR remains a draft; operational instructor decisions listed above are not invented or silently resolved. No merge, staging update or production change is authorized by these checks.
