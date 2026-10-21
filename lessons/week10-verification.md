# Week 10 / local implementation verification

Checked October 21, 2026 in `/home/venetanji/.openclaw/workspace-sd2112/week10-worktree`, branch `docs/week10-planning`, for draft PR #23. Initial worktree status was clean. This is an **uncommitted local draft**, not a PR update, deployment, accepted staff rota or confirmed school visit.

## Implemented artifacts

- `deck/week10.py`: **25 native slides**, comprising one provisional ESFQ holding slide, 23 workshop slides and one untimed reference shelf. Native notes on every slide.
- `deck/week10_figures.py`: redrawn course Double Diamond adaptation; visible Design Council attribution and CC BY 4.0 link. Readable prose phase descriptions accompany the figure for mobile reading.
- `lessons/week10-lesson-plan.md`: preserved purpose/protocol and existing milestone caveat; actual 25-slide map replaces the construction proposal.
- `lessons/week10-speaker-notes.md`: generated directly from final native notes; checked against every exported plain/ClassPoint PPTX notes frame.
- `lessons/week10-references.md`: primary claim/access ledger, archive corrections and offline evidence card.
- `tests/test_week10_sequence.py`: eight focused regressions.
- `deckgen.toml`: adds **only week10** to the build list. No navigation, site, syllabus, workflow, other-week or shared-toolchain source changes.

## Budget and assessment contract

The synchronized relative-minute map is 0-15 provisional school reserve; 15-30 framing; 30-55 reframe; 55-75 develop; 75-90 break; 90-115 prototype; 115-145 test; 145-165 revise; 165-180 share. Total **180 minutes**. Support slides are within those activity blocks. An unused reserve becomes revision/feedback; a moved school visit moves the reserve. The full break is retained.

There are **zero ClassPoint activities**, zero new uploads, zero fabricated report IDs and no new assessment, deadline or recruitment requirement. The real `attach_reports` hook runs before finalization, with a missing report mapping a safe no-op. A nonempty mapping against this zero-collection deck raises drift rather than silently creating links. The syllabus's Week 10 Prototype v1 milestone remains; this workshop does not cancel or move it.

## Environment and build

Prepared a worktree-local `.venv` with `uv venv`, `uv pip install --python .venv/bin/python --link-mode=copy -r requirements.txt`, and `npm install --prefix .venv --no-save --package-lock=false playwright@1.56.1`. Preserved the requirements pin **Deckgen v0.11.2**, Git commit `9990546c01865807e6aaac5aaa50977b4b6b916a`; installed package metadata calls itself 0.1.0. No browser downloads or global toolchain changes.

Full target build on the bound course node:

```bash
export NODE_PATH="$PWD/.venv/node_modules"
export CHROMIUM="$(printf '%s\n' /ms-playwright/chromium-*/chrome-linux*/chrome | head -n 1)"
test -x "$CHROMIUM"
node /home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/run.mjs -- .venv/bin/deckgen build week10
```

Final full-build log: `run-1792564290110-0ff641ec-bbbc-499c-bc01-fd89a5849f3d` (exit 0). The target full build passes, with **25-page PDF**, plain PPTX, ClassPoint PPTX, HTML, native previews, manifest and document exports. No text overflow, missing still or report-map mismatch. This target build recreates `_site/` for week10 only; it is **not** a complete-course site verification.

Local outputs: `_site/week10/index.html`, `_site/week10/SD2112-week10.pdf`, `export/week10.pptx`, `export/week10-classpoint.pptx`, `export/week10-activities.json`, `export/preview/week10/` and `export/docs/`.

## Source and visual checks

- Full repository unittest discovery also passes: **107 tests** in 23.302 seconds. Full-suite output retained in wrapper log `run-1792564305519-1c315f74-740a-403b-befd-9e7d84568b08`; warnings are non-failing generator image-reader ResourceWarnings.
- Eight focused tests pass: timing/sequence, reserve/assessment uncertainty, simulation/ethics/observation boundaries, native primary-source links, actual report-hook invocation, build-only registration, canvas/footer geometry and exact plan/notes synchronization.
- Both exported PPTXs have 25 slides and notes exactly matching the source; each contains eight native hyperlink runs and no ACTIVITYMODEL tags. Activity manifest has no activity entries. This is an artifact-structure check, not a classroom add-in test.
- All **25 desktop slides** captured at 1280 x 720; all **25 mobile reading cards** individually captured at 390 x 844, rather than navigating hidden Reveal slides. All mobile cards stay within horizontal bounds. Visible Deck view control tested separately. No browser page errors.
- Design Council, CC BY 4.0, paper DOI and Verbeek links each visibly activated on their actual slide in desktop and mobile reading mode. Desktop opens a popup; mobile navigates the current page. Destination navigation was intercepted by the QA harness, so this verifies anchor activation and intended URLs, not every external site's current availability. Design Council and Cambridge primary content were independently retrieved for the evidence check.
- Every slide inspected through desktop/mobile contact sheets and Deckgen's native PNG preview sheets. Corrected a Double Diamond label that approached an edge, and added textual phase descriptions so mobile reading does not depend on tiny figure text. Native previews are Deckgen's rendering, **not** a PowerPoint application screenshot. Classroom font/device rendering remains a delivery check.
- Source notes are compared exactly with exported native notes, not a separately improvised facilitation script. No real student responses or tests were used.

## QA evidence

Private workspace evidence root:
`/home/venetanji/.openclaw/workspace-sd2112/tmp/weekly-draft-audit-20261021/week10/`

Contains `qa.cjs`, `browser-results.json`, `native-results.json`, `desktop-01.png` through `desktop-25.png`, `mobile-01.png` through `mobile-25.png`, `mobile-deck-view.png`, contact sheets, the primary Cambridge PDF/extraction and `archive/` with the rendered historical references. Native previews remain under ignored `export/preview/`. Wrapper command logs are under workspace `.openclaw/output-budget/logs/`. Internal QA is not instructor delivery media.

Early QA harness attempts incorrectly expected mobile links to open popups and then awaited a DOI without intercepting its redirect. The corrected run tests same-tab navigation with explicit destinations; no source workaround was added for those harness issues. A non-failing Deckgen ResourceWarning about its image reader appears in tests; no shared-package edit was made.

## Archive and primary access

Read the complete supplied Week 10 lesson plan and syllabus; inspected recent Weeks 5-7 native patterns and the Week 8 worktree's source. The 2025 Week 8 PDF positions 27-29 were extracted and visually inspected. All 19 pages of the 2025 Week 10 PDF were text-extracted and visually checked as a contact sheet. Historical Scrum/Git/Docker recap title, guest introduction and old deadline are not carried forward. The archive's divergence/convergence slogan is corrected rather than repeated.

Official Design Council framework meanings, iteration paragraph and CC BY 4.0 attribution checked on the official page. The **primary final Cambridge 19-page Sözen & Börekçi paper** was downloaded lawfully from its publisher record and directly checked at methods pp. 4-7, results/discussion pp. 13-16, and visually at Figure 5 p. 16. There is no central numerical performance claim. Speaker-note sample counts were checked against methods; no randomized superiority, universal transfer, time saving or 2026 tool-performance claim is made. Supplementary data were not audited. The OneDrive PPTX and obsolete PR #3 toolchain were unnecessary and not used.

## Remaining decisions and delivery checks

Confirm actual class date, facilitation coverage, equipment and the school's ESFQ visit/placement. Giovanni's absence alone is confirmed. Confirm team starting points and reconcile Prototype v1 with the actual Canvas instructions; do not change the approved brief or deadline through this draft. Check classroom PowerPoint font resolution and physical projector/mobile access before delivery. Peer testing stays voluntary, synthetic, low-risk and private; no real recordings or research data belong in this public repo.

No commit, push, PR edit, merge, deployment or external message was performed.

## Independent cross-week verification

Independent parent review on 21 October 2026, after authoring handoff:

- Re-ran the standard targeted build and repository tests on this branch: build exit 0; **107 tests passed**. All 25 PDF pages and 25 slides in each PPTX match source count; all native notes match the source and companion.
- Parent inspected all new desktop, mobile-handout and generator-native slides in independently captured contact sheets. Browser checks find no measured body/horizontal overflow, JavaScript errors or failed local resources. Native preview inspection does not establish Microsoft PowerPoint classroom rendering.
- Assembled a separate, detached, local-only integration checkout from unchanged main plus the six weekly source sets, combining only the build-list registrations. **The unfiltered 13-week HTML/PDF/PPTX build passes, and all 165 combined repository tests pass.** This is integration verification, not a merge or production deployment.
- Parent reviewed source/notes, activity pacing, assessment boundaries and archive continuity. Primary-source access/version limits in the evidence ledger remain in force; this is not replication or a claim to newly reread every reference independently.
- Review evidence is retained outside tracked course sources at `tmp/weekly-draft-audit-20261021/week10/parent/`; combined build/test receipts and source hashes are in the adjacent audit root. Generated exports, QA screenshots and archived full papers are not staged.
- PR remains a draft; operational instructor decisions listed above are not invented or silently resolved. No merge, staging update or production change is authorized by these checks.
