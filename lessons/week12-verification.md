# Week 12 / local verification / 12 November 2026

Current staff report: `lessons/week12-revision-20261112.md`. Current claim ledger: `lessons/week12-evidence-ledger.md`. This supersedes the historical October checks of a different 42-slide draft.

- Detached base `b97d4c05f4173458f6d0feb9535250f266748f70`; Week 12-only edits; no commit, push or deployment.
- Fresh `.venv` from unchanged `requirements.txt` (deckgen v0.11.2), Playwright 1.56.1 in `.venv/node_modules`, preinstalled Chromium via `CHROMIUM`. `NODE_PATH` points to this checkout's `.venv/node_modules`.
- `node /home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/run.mjs -- .venv/bin/deckgen build --no-pdf week12` passes, zero text overflow; 36-slide HTML, native and ClassPoint PowerPoints, notes/docs, 36 preview PNGs.
- `node /home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/run.mjs -- .venv/bin/python -m unittest discover -s tests -q` passes, 135 tests. Focused Week 12 8 pass. No skips in reported suite output.
- Both native PPTX packages: 36 slides, 36/36 exact notes via paragraph-aware XML comparison against source and companion. Native slide relationships include NTSB and Cecil hyperlinks. ClassPoint has two tags, slide 3 and 34; plain PPTX has none. Live add-in behavior not tested.
- Browser desktop: 36 slides traversed, no JS errors/failed resources; no body-text/horizontal overflow. Seven known chapter/display/activity heading line boxes report small extra scroll height from tight typography; visually inspected, no clipped glyphs. Case link clicked from the active diagram and opened exact NTSB URL. Native preview sheets for all slides and full desktop images of materially revised 1-23 inspected.
- New 390x844 mobile context auto-enters reading view: 36 handout sections; no horizontal overflow, JS errors or failed assets; eight NTSB source links present, Deck view restores a 390px-wide page. Screen captures for materially revised 1-23 inspected. QA local reports in `/tmp/week12-case-research/qa/`; ignored preview contact sheets in `export/preview/week12/`.
- PDF deliberately omitted for target HTML/native QA. No Microsoft PowerPoint desktop app, ClassPoint live session, projector, screen-reader study, court docket after April 2024, participant study or safety trial is established.

## Continuity and diagram correction / 12 November

After parent review, replaced stale speaker-note slide numbers with semantic mock-review/revision references; closing notes now confirm Week 13 quiz and posters while leaving its format/duration unspecified. Corrected the source-labelled incident schematic: the SR-85 left exit sits above continuing US-101, with orange nontravel gore and black damaged attenuator keyed in text. Short labels read without clipping at 390px. Rebuilt HTML/plain/ClassPoint PPTX (`--no-pdf` exit 0), reran the full 135-test suite (exit 0), checked final mobile diagram screenshot/zero page errors/zero horizontal overflow, and rechecked all 36 native notes in each PPTX (zero mismatches). `git diff --check` clean.
