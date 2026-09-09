# SD2112 · Artificial Intelligence in Design — teaching repo

Class planning and slides for PolyU School of Design, Semester 1 2026/27.
Lecturer Giovanni Lion (giovanni.lion@polyu.edu.hk) · teaching assistants Nicolò Azzolin, Amber, WU Zhao and MA Jie (in the room 30 min before and after class) · class coordinator Zhibin Zhou.

The repository holds **sources only**. The slide toolchain is not in here either — it is
[`ait4x/deckgen`](https://github.com/ait4x/deckgen), pinned by tag in `requirements.txt` and
shared with [`sd5913/teaching`](https://github.com/sd5913/teaching), so a fix to the PowerPoint
or ClassPoint plumbing lands in both courses at once.

Two GitHub Actions workflows run on every push to `main` (and on demand), and a third on every push to `staging`:

| Workflow | What it makes | Where it goes |
|---|---|---|
| **Publish site** (`.github/workflows/site.yml`) | The html decks, a PDF of each deck without the ClassPoint buttons, the syllabus page, the landing page. | GitHub Pages: `https://venetanji.github.io/sd2112-teaching/` (Week 1: `/week01/`, PDF: `/week01/SD2112-week01.pdf`). |
| **Build PowerPoints** (`.github/workflows/pptx.yml`) | `week01.pptx` (plain), `week01-classpoint.pptx` (ait4x master, animations, ClassPoint buttons), the activity manifest, `.docx` of the syllabus and lesson plans, preview sheets. | The `sd2112-powerpoints` artifact of the run (Actions → the run → Artifacts), kept 90 days. Not published. |
| **Build staging** (`.github/workflows/staging.yml`) | Everything above, from the `staging` branch: html decks, PDFs, PowerPoints, documents, previews. | The `staging-site` and `staging-powerpoints` artifacts of the run, kept 30 days; and *Publish site* re-runs and shows the html under `https://venetanji.github.io/sd2112-teaching/staging/`. |

## Staging: check a week before it reaches main

Push (or merge) to the `staging` branch. **Build staging** builds everything and fails the way `main` would (a text overflow, a sketch with no still); its summary links the two artifacts. When it ends, **Publish site** re-runs from `main` and republishes the Pages site with the staging build under `/staging/`, built with the staging branch's own `requirements.txt`, so a toolchain change can be checked there too. The published decks are untouched. A broken staging build never blocks `main`: the step is allowed to fail, and `/staging/` is then restored from the last successful *Build staging* run's `staging-site` artifact (kept 30 days), so the preview does not disappear. When it looks right, merge to `main` (the feature branch, or `staging` itself).

## Layout

| Path | What |
|---|---|
| `deck/week01.py`, `deck/week02.py` | **The slides of each week as one Python spec**: text, speaker notes, ClassPoint activities, live p5.js sketches, in the order the class runs. Edit here; every output updates. |
| `deck/course.py` | Shared course facts: links, the semester map, the week titles and module colours. |
| `deck/assets/` | Images the decks use. Drawn figures are generated at build time; `deck/assets/sketches/` holds the stills of live sketches that have no drawn twin (`deckgen snap`, committed). |
| `syllabus/SD2112-syllabus-2026.md` | The syllabus: team, outcomes, four modules, 13-week plan with examples and readings, assessment and rubrics, policies. Published on the site; a `.docx` is built too. |
| `lessons/week01-lesson-plan.md`, `week02-lesson-plan.md` | Each week's run of show (three hours), the activity in detail (*Push the machine to the edge*; *One spec, three executors*), the ClassPoint question map, contingencies. For the teaching team: `.docx` and `.html` in the artifact, **not published**. |
| `site/` | The site shell: landing page, vendored reveal.js and the ait4x design tokens. |
| `deckgen.toml` | The course as the generator sees it: code, name, year, footer, which decks, what gets published. |
| `deck/figures.py` | The drawn illustrations — chairs, typicality, perceptron, two machines, mediation; for week 2 Schotter, Walk-Through-Raster, LeWitt's points, 10 PRINT, the L-system, the spec pipeline. Built on `deckgen.figures.Canvas`. Every p5.js sketch on a slide has its Python twin here, drawing the same rule for the PDF and the PowerPoint. |
| `tools/roster.py` | ClassPoint saved class from a local ID list. |

Generated and git-ignored: `_site/` (the site), `export/` (pptx, manifest, docx, previews), `deck/assets/generated/`, `node_modules/`, `classpoint/*.csv`, `ids.csv`.

## Build locally

```bash
uv venv && uv pip install -r requirements.txt
deckgen build --pptx          # export/: PowerPoints, manifest, docx, previews (no node needed)
deckgen build --site          # _site/: html decks, PDFs, syllabus — needs node + playwright (below)
deckgen build                 # both
deckgen build --no-pdf        # skip the PDF step
python tools/roster.py ids.csv classpoint/roster-2026-classpoint.csv   # ClassPoint saved class (local only)
```

`deckgen build` **exits non-zero if any text overflows its box**, so a broken slide fails the
workflow rather than reaching the projector.

The PDF step needs node 18+ and Playwright's Chromium: `npm install --no-save playwright@1.56.1 && npx playwright install chromium` in the repo folder (the workflow does the same). The html deck: arrow keys, `S` speaker notes, `O` overview, `F` full screen. Video slides embed YouTube; the pptx and the PDF carry a thumbnail and a link instead. Previews and a text-overflow check land in `export/preview/`.

## Classroom checklist

1. Download the PowerPoint from the latest *Build PowerPoints* run (Actions → Artifacts → `sd2112-powerpoints`).
2. Install Inter and JetBrains Mono on the classroom PC — they ship inside the `deckgen` package (`python -c "import deckgen, pathlib; print(pathlib.Path(deckgen.__file__).parent / 'fonts')"`), right-click → install for all users. Restart PowerPoint. Slide 1 should show *Inter Black* in the font box; Arial substitutes automatically if not.
3. Open the deck with the ClassPoint add-in and fire one activity (slide 4, word cloud) before class; a malformed tag fails silently.
4. Import the roster as the saved class. Students join with the last four digits and the letter of their ID (e.g. `3456A`).
5. Keep the html deck or the PDF open on a laptop as backup.

## Keeping the repository public

Nothing in the sources identifies a student. Keep it that way:

- Student IDs, rosters and ClassPoint exports stay local (`ids.csv`, `classpoint/*.csv` are git-ignored); the roster is a one-off local build, not a workflow step, so no secret is needed.
- Grades, gradebooks and submissions never enter the repository, not even in a branch: the history is public too.
- Workflow artifacts on a public repository are downloadable by anyone with a GitHub account: the PowerPoint artifact is fine, a roster would not be.
- Examples of IDs in docs and slides are made up (`3456A`).

## Design system

Slides and site follow the ait4x design system (PolyU Design brand): Pantone Black 6 ink `#000B1C`, white, cool gray, teal `#64C2C3`, the 70-tile secondary matrix for bands, orange `#ED6D24` for the X and for numbers; Inter (display 800–900, tight tracking) and JetBrains Mono (eyebrows, caps, tracked). Tokens: `site/vendor/ait4x-colors_and_type.css`. PowerPoint font names follow [`PPTX-EXPORT.md`](https://github.com/ait4x/deckgen/blob/main/PPTX-EXPORT.md) in the generator: *Inter Black* / *Inter ExtraBold* / *Inter* + bold / *JetBrains Mono*.

Scale: the canvas is 1920 × 1080 px on a 13.333 × 7.5 in slide, so **one design pixel is 0.5 pt** in PowerPoint (72 px title = 36 pt, 36 px body = 18 pt, 24 px eyebrow = 12 pt). `deckgen.PT` holds that factor; the kit's master and layouts use the same scale.

## Adding a week

Copy `deck/week02.py` to `deck/week03.py`, change `FOOTER` and `pdf`, write slides with the layout functions in `deckgen.layouts` (`title`, `agenda`, `section`, `statement`, `quote`, `content`, `cards`, `question`, `image_full`, `timeline`, `journey`, `activity`, `video`, `assessment`, `team`, `two_col`, `figure_slide`, `code_slide`, `sketch_slide`), add `"week03"` to `decks` in `deckgen.toml`, and add a card in `site/index.html`. ClassPoint activities come from `question(...)` (word cloud, multiple choice, short answer, image upload) or an explicit `cp={...}`.

A slide can run a p5.js sketch live in the html deck: `live(name, code, w, h, hint=...)` placed with `sketch_slide(...)` or as the `sketch=` of `content`, `figure_slide`, `code_slide` and `activity`. The PowerPoint and the PDF show a still instead: the `figure=` you pass (draw the same rule in `deck/figures.py`, as week 2 does), or a snapshot made by `deckgen snap` into `deck/assets/sketches/` (committed: the PowerPoint workflow has no browser).
