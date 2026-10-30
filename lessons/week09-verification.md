# Week 9 current verification / 30 October 2026

## PR reconciliation and final polish

Giovanni authorized pushing the local revision to existing PR #22 on 30 October.
Combined in a separate worktree based on current PR head
`37c5210fcec3dbafcfbe66a292cde719c3609b3d`; the original local draft is preserved.
The remote CC BY links and spaced worked arithmetic are retained. The merged
link regression now checks **27 native link instances**, including all seven
licence links and the three added philosophy sources.

The second polish review restores the specific **conservative activist**
finding on the X results slide and explains uncertainty bars and crossing zero
in ordinary English. It does not turn a null polarization result into proof of
no effect. The source figures, slide count, timing and activities are unchanged.

Fresh combined-source checks before push:

- `deckgen build --no-pdf week09`: **51 slides**, both native PowerPoints,
  no text overflow. This does not certify a fresh PDF.
- Full test suite: **147 tests pass, zero skips**, after fresh exports exist.
  Native notes and regenerated Markdown companion agree; source hashes pass.
- Browser: **51 desktop + 51 mobile** sections, no page errors or measured
  horizontal overflow, both view controls work. All **27 links** activate in
  each view (destinations intercepted, not external-page availability tests).
- Fresh desktop/mobile and native inspection of the changed chart copy,
  licence attribution and retained clean transparency layout passes.
- `git diff --check` passes. Original saved draft hashes are retained outside
  the repository. No merge or production-site update is authorized.

Receipts in workspace `.openclaw/output-budget/logs/`:
`run-1793325831473-d26b950d-5811-4276-bb83-699fa9e889c0` (build),
`run-1793325986461-ab1b7091-d841-42cb-ab40-de4044f823c4` (tests),
`run-1793325937179-73bd194a-44a9-46eb-820a-179c1cdb022f` (browser).
PR head, CI and hosted-preview verification are reported separately after push;
the historical no-push/private-preview statements below describe 29 October.

## Latest: visual + plain-English example revision

Supersedes the initial polish's rendering/test receipts below. Instructor
requests: less projected text, more diagrams/images, and paper explanations
through concrete simple-English examples like Week 8.

- **16 slides** now use new diagram/image-led explanations: five mechanism
  slides, six bias/mediation slides and five paper walkthroughs. Five source
  figure annotations and five activity/comparison slides are also shortened.
  Full explanations remain in native and Markdown speaker notes.
- The paper walkthroughs retain visible, explicitly labelled examples: a
  100-to-10 workshop shortlist; two people with switch/stay feeds; the 53/73/65
  advice calculation; an invented 5/100 error rate; and a workshop relevance
  label whose provenance/pay is questioned. Authentic research figures are
  unchanged. The five examples are not represented as new study observations.
- Original course-owned illustrations supplement the existing storefront photo
  and two historical FastGAN outputs. Source attribution and the distinction
  between learned regularity and discrimination remain. No new external media
  or dependency changes. Diagram generators live in the Week 9 visual modules.
- Still **51 slides, 47 main + 4 references**, six dividers, same three-hour
  schedule, 15-minute break, two 30-minute activities and zero collections.
- Fresh `deckgen build --no-pdf week09` passes with **no text overflow**.
  Both native PowerPoint variants are fresh. Full suite: **147 tests pass,
  zero skips**. Notes tests compare complete non-empty paragraphs; source
  image hashes, native links, arithmetic, geometry and report drift remain
  checked. Existing shared-renderer ResourceWarnings persist without failures.
- Actual private HTTP preview: **51 desktop + 51 mobile reading sections**,
  no JavaScript errors or measured horizontal overflow; both mode controls
  work. All **20 source-link instances** activate correctly in both views,
  with external destinations intercepted for navigation verification.
- All desktop/mobile/native contact sheets inspected, with selected new
  visuals at full resolution. A stale two-column text panel on the transparency
  slide and a paper-diagram/caption clearance issue were corrected and checked
  again in desktop/mobile/native output. This is not a classroom projector or
  Microsoft PowerPoint application test.
- `git diff --check` passes. No commit, push or public deployment. Private
  preview remains `http://100.64.0.12:8769/week09/`; instructor-device access
  remains unverified and requires the private network.

Latest receipts under the workspace `.openclaw/output-budget/logs/`:

- Build: `run-1793280680084-12729dce-7c97-4cbf-a832-4b797eeeb186`.
- Full tests: `run-1793280690760-92761c55-31a4-42f5-9809-64d84615c82e`.
- Browser: `run-1793280719641-c025a71d-a7f5-4a06-8be2-c6a71414b0ab`.

Latest browser captures/report and pre-visual text/source snapshots:
`tmp/week09-polish-20261029/visual-pass/`. Image labels are not included in
native-text word counts, so those counts are not claimed as a complete visual
word-count reduction.

## Initial polish / retained context

Local polish checkout: `/home/venetanji/.openclaw/workspace-sd2112/tmp/week09-polish-20261029/worktree`, detached at the current draft PR #22 head `6fe8c92bbf2cb775c691de2ad318c2d6313ea487` when recovered. Its confirmed 30 October class date and 28 October news handoff are preserved. Older dirty worktrees, main, staging and remote PR contents are untouched. No commit, push or public deployment is part of this revision.

## Revised teaching contract

- 51 slides: 47 main-route plus 4 explicitly non-assigned references. Six section dividers distinguish mechanisms, bias, mediation, feedback evidence, finding bias examples and reflective use. The original three-hour envelope, 15-minute break, two 30-minute activity blocks and zero ClassPoint collections remain.
- The first activity now identifies two examples of AI bias and closely examines one: observation/comparison, interpretation, consequence and uncertainty. A safe test is optional; documented examples are sufficient. No mandatory paper quota, paid service, personal data, new upload or assessment.
- Inductive assumptions, learned regularities and harmful social bias are distinguished. AI reflects selected traces and transforms them; it is not a complete passive mirror of humanity. Necessary selectivity does not excuse preventable discrimination.
- Heidegger/Ihde/Verbeek lead into Van Den Eede's use/context questions and double vision. Reflective use can change attention, interpretation and action without retraining; neither awareness nor an explanation establishes fairness. Source locations/access limits are in the evidence ledger, including the fact that the Heidegger/Ihde books were not newly read.
- All five inherited research walkthroughs and all authentic source assets/provenance are retained. This revision does not claim a fresh replication or full reread of those five studies. New philosophy/inductive-bias sources received the bounded primary-text checks documented in the research report and ledger.

## Fresh verification

Pinned own environment: Deckgen `v0.11.2`, Playwright `1.56.1`, existing Chromium `/ms-playwright/chromium-1246/chrome-linux64/chrome`. All builds run on the bound course node, without changing shared tools or dependency pins.

- `deckgen build --no-pdf week09`: passes, no text overflow. Fresh 51-slide HTML and both native PowerPoints; zero-entry ClassPoint manifest. No PDF finalization or full-course export build claimed.
- Full suite: **145 tests pass, zero skips**, including 18 Week 9 checks for sequence, activity/privacy/assessment contract, philosophy distinctions, all five paper walkthroughs, asset hashes, report drift, toy arithmetic, companion notes, native links/notes and slide geometry. The run emits ResourceWarnings but exits successfully; retained stderr is available for inspection.
- Browser checks against the actual private HTTP route: **51 desktop slides at 1920x1080; 51 mobile reading sections at 390x844**. No JavaScript errors or measured horizontal overflow. Both reading/deck controls work. All **20 source-link instances** activate to the expected URLs in both modes; publisher requests are intercepted, so this verifies navigation rather than classroom external-network availability.
- All desktop/mobile/native slides inspected in contact sheets; new philosophy/activity slides checked at full resolution. One awkward divider wrap and long activity kickers were corrected, rebuilt and reconfirmed. Native previews/XML are not a Microsoft PowerPoint or classroom-projector test.
- `git diff --check` passes. Changes remain confined to Week 9 source, its philosophical helper, companion documents and regression tests; earlier weeks, assets, syllabus, registrations and shared tools are unchanged.

Private-network review: `http://100.64.0.12:8769/week09/`, served only from the generated `_site` directory on the course node's private address. HTTP 200 and desktop/mobile browser rendering verified from that node; access from the instructor's device is not verified and requires private-network reachability. This is not the public Cloudflare PR preview or production site.

Evidence root: `tmp/week09-polish-20261029/` in the workspace; `research.md`, retained primary extracts under `sources/`, final `qa/browser-qa.json`, desktop/mobile captures, `qa/qa.cjs` and native previews under the worktree. Final output-budget receipts:

- Build: `run-1793276502746-d45c8858-d2ed-4329-abb6-08c7e705de42`.
- Tests: `run-1793276513992-66589e8b-de12-4f6f-8ed1-f48ad45d4e77`.
- Served browser QA: `run-1793276543132-655770b1-ff83-48ee-bfa9-f314299170c3`.

## Historical verification / 22 October 2026

The retained records below describe earlier revisions and their rights decisions, not fresh checks of the 29 October polish. Current counts, timings, activity and verification above supersede their corresponding claims.

Isolated prepared checkout: `/home/venetanji/.openclaw/workspace-sd2112/tmp/weeks09-13-standard-20261022/week09/worktree`, detached prepared head429ebcc. Uncommitted changes only. The original `week09-worktree` and every recorded source/asset hash were preserved. Prepared Week09 sources matched original baseaf4f0cd exactly before reconciliation; no newer remote Week09 choices were overwritten. Published main54f38c7/Weeks1-8 and registration remain untouched.

## Current teaching and evidence

43 slides =40 main +3 non-assigned reference;180minutes;0ClassPoint collections. All protected blocks and existing concept-board/bias-register/Canvas uncertainty preserved. Five walkthroughs replace compressed abstracts, not additional slides: engineering task/evaluation(R1), historical classifier audit/error denominator(R4), documentation argument/development(R5), randomized feed assignment/following(R2), controlled0-100% dot estimates/baseline errors(R3). Examples distinguish instructor illustrations from the source-adapted53/73/40 calculation. Result slides explain charts, limits and proposed design questions. Common paper titles x120/y184/w1680/h140,size72; label/body gap52; citationy956 with6pxfooter clearance.

This author performed targeted retained-primary methods/results rechecks, not a fresh full-paper read. Details/version/access in evidence ledger and `deck/week09_studies.py`. Source pages/figures visually inspected; full papers remain outside Git. Current11asset provenance records preserve9inherited crops plus2authentic condition assemblies. Eight displayed image elements on6explanation slides. R2assemblies improve phone scale without redrawing data; old crops remain historical.

## Fresh local checks

Pinned own `.venv`: Deckgen requirements v0.11.2, Playwright1.56.1 in `.venv/node_modules`, existing executable Chromium override. Target `deckgen build --no-pdf week09` succeeds without overflow; fresh43-slide HTML, plain+ClassPoint PowerPoints, native previews and zero-entry activity manifest. No PDF or deployment is claimed. Full suite and focused test receipts, exact counts and current artifact hashes are in task-local `author-report.json`; source/companion/native notes, links, geometry, causal limits, arithmetic and report drift are checked.

Fresh browser at desktop1920x1080 and a new mobile390x844context captures all43sections in each mode. Handout is visible, both toggles work, no JS errors or measured horizontal overflow. All17primary-link instances activate to their expected destinations in both views; destination requests are stubbed, so this is navigation QA rather than publisher/classroom network reachability. Every desktop/mobile/native slide was reviewed in sheets, with final full-resolution confirmation of modified results and phone Figure4after the one corrective split. Native previews/XML are not a test in Microsoft PowerPoint or on a classroom projector.

Current private evidence root: `/home/venetanji/.openclaw/workspace-sd2112/tmp/weeks09-13-standard-20261022/week09/qa/`: browser-qa.json,qa.cjs,desktop/,mobile/,contact sheets. Build/test receipts are linked in author-report.md/json. `git diff --check`passes. Parent owns combined13-week PDF/export QA and all GitHub integration.

## Current public-review rights decision

The earlier author report gated R1/R2/R5 because a distribution-specific public-use basis was undocumented; it remains historical evidence, not the current complete decision. Follow-up 22 October read raw official IPD FAQ16-18 bodies and assessed exact purpose, necessary amount, attribution, potential market and unrestricted public GitHub/Cloudflare/HTML/PDF/PPTX workflow distribution. A narrow Hong Kong section39 criticism/review/quotation basis is supported; not education alone, classroom-only permission, restricted recipients, attribution alone or an open licence. Gauthier remains **CC BY-NC-ND 4.0**, with no ND-licence permission asserted for crop/assembly. Exact rationale/credits/boundaries are in `deck/assets/week09/README.md` and provenance.

Parent correction verified 22 October: native reference slide42 names Gauthier, Hodler, Widmer and Zhuravskaya and The political effects of X's feed algorithm; slide43 names Gebru et al. and Datasheets for Datasets. Both rebuilt PowerPoint variants contain these title and author credits as actual native slide text. HTML/PDF derive from the same source. The precise missing-title condition is resolved for the assessed public-review use. This does not grant ND-licence permission or blanket legal clearance; the scoped exception and jurisdiction-sensitive boundaries remain. Historical absent-credit conditions are preserved in the original rights-only report and provenance history. Parent also replaced the Figure4 left/right locator with Switch ON/OFF wording and added an explicitly invented completed bias-register row to the existing redesign notes, without a new slide, collection or minute. Companion notes regenerated. Final combined/hosted checks remain separate; earlier author receipts do not certify these later corrections.

---

# Historical record / 21 October 2026 / not current QA

The following retained VersionBverification describes the original checkout and earlier assets/claims. Current checks and corrected rights scope above supersede it; its receipts are not counted as fresh.

# Week 9 paper-visual revision verification

21 October 2026. Worktree `week09-worktree`, branch `docs/week09-planning`, starting clean at `af4f0cd`. This revision is **uncommitted**. No push, PR mutation, deployment, shared generator, registration, earlier-week, syllabus or requirement-pin edit.

## Revised teaching contract

- 43 slides: 40 main-route + 3 visibly **NON-ASSIGNED / REFERENCE SHELF** slides. Five standalone paper summaries, each before its authentic source image; body lengths R1 47, R2 42, R3 43, R4 48, R5 47 words, excluding title/labels/source.
- Four purposeful teal section transitions: mechanism; objectives/data; feedback evidence; evidence-to-design. Shorter visible exposition on mechanism/privacy slides; fuller method in native notes and regenerated companion. Labour is taught through an actual documentation question instead of a duplicate prose slide.
- Nine faithful image crops on six explanation slides: Covington Figure 2; Gender Shades Table 4; Datasheets section 3.3 document excerpt; Gauthier Figure 4 top rows plus separately preserved original axes/legend; Glickman Figure 2a-c and separate panels e/g. No invented empirical chart. Full source/version/page/crop/hash information in `deck/assets/week09/provenance.json`, asset README, native notes and evidence ledger.
- Original 180-minute budget retained. Break 75–90 (slide 30), demo 90–105 (31–32), research 105–135 (33–35), redesign/test 135–165 (36–38; 20+10), debrief 165–180 (39–40). Added summary/image slides split explanations, not add time. Zero ClassPoint activities as before. Concept-board/bias-register Canvas scope/date remain uncertain; no new submission, grade, deadline, account or student-data collection.

## Fresh verification

Unchanged worktree-local `.venv`; Deckgen requirements pin `v0.11.2`, Playwright 1.56.1 in `.venv/node_modules`, installed Chromium override. All commands on bound course node through output-budget wrapper. No global install or toolchain patch.

- `.venv/bin/deckgen build --no-pdf week09`: exit 0, no text-overflow/error, fresh 43-slide HTML, plain PPTX, ClassPoint PPTX, 43 native previews and zero-entry manifest. **No fresh PDF requested/generated**; any prior PDF is stale and is not a deliverable/evidence for this revision.
- `.venv/bin/python -m unittest discover -s tests -v`: **112 tests pass**, including **13 Week09 tests**. Tests cover summary count/length, actual image files and crop hashes, mobile image-before-explanation order, visible bounded claims, native links, timing/assessment, report mapping no-op/drift rejection, deterministic toy arithmetic, geometry/footer, plan titles and companion/native notes in both fresh PowerPoints.
- Browser: all **43 desktop slides at 1920×1080**, all **43 mobile handout sections at 390×844**, no JS errors or measured horizontal overflow. All **17 visible source-link instances** clicked in both views with observed intended navigation URLs. Destination requests intercepted as QA stubs; this verifies activation/destination, not publisher or classroom network availability. Deck/Reading view controls pass.
- All desktop/mobile/native previews inspected in batched contact sheets. Initial full X figure was too small: corrected once to its actual political rows, with separately preserved original x-axis and legend strips, visibly labelled as crops. Final mobile confirmation keeps figure, axes and legend together before explanation and citation. Divider kickers moved above footer locally, not by shared-layout edits. No aesthetic cycling after final confirmation.
- `git diff --check` passes. Only Week09 sources/assets/docs/tests changed. Native preview/XML checks are not Microsoft PowerPoint-on-classroom-device rendering or instructor approval.

## Retained evidence

Task QA root: `/home/venetanji/.openclaw/workspace-sd2112/tmp/paper-visual-revision-20261021/week09/`.

- `qa.cjs`, `browser-qa.json`, `desktop/`, `mobile/`, desktop/mobile/native contact sheets and `research/` original downloaded figures/source page renders.
- Recovered full primary texts: sibling `tmp/weekly-draft-audit-20261021/week09/research/`. Main primary versions reread; supplements and replication code/data not newly reviewed/reproduced. HTML Nature figures have exact figure anchors, not invented PDF page numbers.
- Final content build log: `.openclaw/output-budget/logs/run-1792578325052-1cecf002-068e-43f6-bd10-f62ca72c76de` under workspace.
- Final full tests: `.openclaw/output-budget/logs/run-1792578333962-a362f72a-93d6-468d-85d3-16c49bc35d22`.
- Final browser: `.openclaw/output-budget/logs/run-1792578357404-10ca4bfd-5518-4dfe-8599-731aea86c2e6`.
- Handoff report: `tmp/paper-visual-revision-20261021/week09-report.md` under workspace. Parent owns combined QA and any requested review URL. No public preview claimed here.

## Remaining boundaries

This is a target-week HTML/PPTX review, not an unfiltered combined-course build, PDF finalization, replication or legal opinion. Full papers remain private reference aids; only attributed useful excerpts/images enter teaching assets. Classroom projection/PowerPoint font resolution, actual network access and human acceptance remain checks for the instructor. Source reuse notices/limits are recorded; no unsupported open licence is asserted for Covington or the short Datasheets quotation. All product controls remain hypotheses, not proven remedies.
