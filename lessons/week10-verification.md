# Week 10 / local implementation verification

## Current AI-inside revision / October 30, 2026

Instructor-approved focus: products/services with AI inside, considered through Discover, Define, Develop and Deliver, using Week 8 mediation/AI-as-material and Week 9 data/bias/privacy. This supersedes the workshop-only teaching sequence below. Zhibin and four PhD researchers are intended contributors; their acceptance, identities beyond Zhibin, topics, order, individual allocations and facilitation roles are not invented. The new contributor brief records these open fields.

Prepared a separate detached worktree at exact PR #23 head `82d796ed66a0ec942186164712b04bcad57f2eff`: `tmp/week10-ai-inside-20261030`. The older dirty `week10-worktree` is untouched. No syllabus, assessment, report, workflow, dependency, shared-renderer, main or staging change is part of this revision. The existing PR stays open/draft; branch preview is separate from production delivery.

29 native slides: 26 in the proposed relative-minute route, then an untimed reference shelf and two preserved AI-as-design-tool study slides. The study is explicitly optional background, not AI-product validation. The new phase prompts are course-authored application, not an empirical result or official Design Council AI guidance. Existing primary-source checks, licences, source pixels and access boundaries remain in the ledger; no new full-paper audit is claimed.

Proposed budget: opening/phase framing 15, collective guest cases 45, shared questions 10, break 15, four-phase map 15, develop/prototype 30, voluntary walkthrough 25, revise/share 10, provisional ESFQ reserve 15 = **180 minutes**. All workshop substeps sum to their blocks. Date, speaker allocations and the school arrangement remain provisional. Zero ClassPoint collections, new uploads or new assessment; Prototype v1 and actual Canvas instructions still apply.

Fresh local verification on the bound course node, using this checkout's own pinned environment:

- `.venv/bin/deckgen build --no-pdf week10`: exit 0, 29-slide HTML, both PPTX variants, native preview images and document exports. No build overflow, missing asset or report mismatch. Receipt `run-1793342232181-eb437de1-e136-46f2-91b6-5d6ea0a4529e`. This command deliberately does not certify a PDF or complete-course build.
- Post-build full unittest discovery: **140 passed, zero skips**; Week 10's 13 regressions cover focus/bridge, phase order, provisional guests, full timing/substeps, evidence limits, privacy, zero collections, native geometry, links, plan map and exact notes synchronization. Full-suite receipt `run-1793342260919-12afba94-1b63-4a38-b347-b884b151ba75`. Existing generator image-reader ResourceWarnings are non-failing and not patched here.
- Browser QA: all **29 desktop slides and 29 fresh 390x844 mobile reading sections** captured and visually reviewed alongside all 29 generator-native previews. No mobile horizontal overflow or browser page errors. Ten real anchor activations across desktop/mobile verify framework/licence/study/Verbeek destinations using intercepted external navigation, not external publisher availability. Visible mobile Deck view toggle passes. Receipt `run-1793342298612-8a2508f5-9d69-434b-97ec-310b41ee88c4`.
- Measured text bounds: no body overflow. Only established title/activity-heading line boxes exceed scrollHeight (slides 1, 11, 14, 20, 23); glyphs and neighbouring content were visually inspected and do not collide. This is a rendering-specific line-box observation, not a body-overflow exemption.
- Both native PPTXs contain **29 slides**; every native notes frame exactly matches the final source and regenerated Markdown companion. These are structural and generator-preview checks, not Microsoft PowerPoint classroom rendering or live add-in tests.

Private evidence: `tmp/week10-ai-inside-20261030-qa/` contains browser/native JSON, screenshots and contact sheets. It is not staged or delivered to the instructor. Exact-head CI and hosted-preview results belong in the current PR handoff, not the historical receipts below. Classroom device/font/access checks and actual facilitation remain unverified.

## Historical Week 8-standard revision / October 22, 2026

26 slides: 25 in the timed route (including provisional ESFQ and break), one untimed reference shelf. The compressed study card is replaced, not supplemented, by a task/recording slide followed by the authentic Figure 5 result map. The same four minutes and 15-minute framing allocation remain. Verbeek's conceptual checkpoint now uses a labelled argument/example/application/limit layout. The week-owned helper uses Week 8's x120/y184/w1680/h140, 72px paper title, 52px label/body gap and citation y956. No workshop exercises, ClassPoint prompts, grading or deadlines were added.

Prepared isolated checkout: `tmp/weeks09-13-standard-20261022/week10/worktree`, detached head `9336ded93f9d2a154df51b4ae096e7c9ecebd082`. Read original-base/current/local B for every recorded file: all tracked current Week 10 files equal their original base, so Version B changes were applied without overwriting a competing newer Week 10 edit; new source images were copied byte-identically. Preserved published Weeks 1-8, remote registration and original worktree untouched. Reconciliation receipt: task-local `reconciliation.json`.

Fresh pinned environment: Deckgen requirements Git commit `9990546c01865807e6aaac5aaa50977b4b6b916a` (v0.11.2 pin; metadata 0.1.0), Playwright 1.56.1 under `.venv`, preinstalled Chromium. No shared/global renderer, pin or browser changes.

Fresh passing receipts (private output-budget log IDs):
- `.venv/bin/deckgen build --no-pdf week10`: `run-1792654563165-b686dbf2-b7d1-4311-9e12-e57f5ef5f683`, exit 0; 26-slide HTML, plain/ClassPoint PPTXs and native previews; zero collections; no missing assets/overflow/JS errors. No PDF generated; parent owns complete-course PDF/export integration.
- Focused unittest discovery: 10 tests, `run-1792654700380-241926c9-75d3-4424-bc69-641a50a54823`, exit 0.
- Full repository unittest discovery: 137 tests, `run-1792654700511-41910e87-4a6e-4db9-b786-228498541f09`, exit 0. Existing image-reader ResourceWarnings are non-failing, not patched here.

Fresh browser QA: task-local `qa/browser-results.json`, 26 desktop slides, 26 genuinely fresh 390x844 mobile reading sections, horizontal bounds pass, zero page errors, real visible Deck view toggle. Ten desktop/mobile primary/licence anchor activations land on the intended intercepted destinations; this verifies interaction and URL, not publisher uptime. Full sheets for desktop/mobile/native were visually inspected, plus slide 7 full-size in all three modes. Body text, headings, labels and citations are separated. Figure is an explanatory four-phase category map, not a chart with numerical axes; small raster activity labels are supplemented by visible prose and a clickable full article/image. Only the established bottom-aligned display title/activity heading line boxes exceed scrollHeight; visually inspected glyphs and adjacent content do not collide. No body overflow exemptions.

Both exported PowerPoints: 26 slides, every native notes frame exactly matches final source; Markdown companion generated from the same notes and covered by tests. `qa/native-results.json` retains receipts. No classroom Office rendering or live facilitation test is claimed.

Sources: targeted final publisher PDF recheck pp.4-7,13-16 and licence p.1; original Figure 5 p.16 visually inspected. Design Council retained official HTML and Verbeek retained primary extraction rechecked, not a fresh full-paper audit. Public GitHub draft sources, Cloudflare preview and downloadable artifacts are the actual review distribution, not local-only. Explicit CC BY 4.0 image licences cover these two reused images; preserve attribution and crop disclosure. Full papers stay private. Details and source pixels: `week10-references.md` and asset `PROVENANCE.md`.

Open classroom decisions: date, facilitator coverage, ESFQ visit/placement and actual Canvas Prototype v1 instructions remain unconfirmed. No guest or staff acceptance inferred. No commit/push/PR/deployment/main release performed in this author pass; parent owns review/integration/GitHub and hosted verification.

## Historical 25-slide receipts (superseded for current source count)

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
