# SD2112 · Artificial Intelligence in Design — teaching repo

Class planning and slides for PolyU School of Design, Semester 1 2026/27.
Lecturer Giovanni Lion (giovanni.lion@polyu.edu.hk) · teaching assistants Nicolò Azzolin, Amber, WU Zhao and MA Jie (in the room 30 min before and after class) · class coordinator Zhibin Zhou.

The repository holds **sources only**. Two GitHub Actions workflows run on every push to `main` (and on demand):

| Workflow | What it makes | Where it goes |
|---|---|---|
| **Publish site** (`.github/workflows/site.yml`) | The html decks, a PDF of each deck without the ClassPoint buttons, the syllabus page, the landing page. | GitHub Pages: `https://venetanji.github.io/sd2112-teaching/` (Week 1: `/week01/`, PDF: `/week01/SD2112-week01.pdf`). |
| **Build PowerPoints** (`.github/workflows/pptx.yml`) | `week01.pptx` (plain), `week01-classpoint.pptx` (ait4x master, animations, ClassPoint buttons), the activity manifest, `.docx` of the syllabus and lesson plans, preview sheets. | The `sd2112-powerpoints` artifact of the run (Actions → the run → Artifacts), kept 90 days. Not published. |

## Layout

| Path | What |
|---|---|
| `deck/week01.py`, `deck/week02.py` | **The slides, one Python spec per week**: text, speaker notes, ClassPoint activities, in the order the class runs. Edit here; every output updates. Week 2 carries its p5.js sketches as strings: the html deck runs them live, the pptx and PDF show a Python-drawn twin of the same rule. |
| `deck/assets/` | Images the decks use. Drawn figures are generated at build time; `assets/sketches/` holds the committed stills of the live sketches. |
| `syllabus/SD2112-syllabus-2026.md` | The syllabus: team, outcomes, four modules, 13-week plan with examples and readings, assessment and rubrics, policies. Published on the site; a `.docx` is built too. |
| `lessons/week01-lesson-plan.md`, `lessons/week02-lesson-plan.md` | Run of show for each three-hour class, the activity in detail (*Push the machine to the edge*; *One spec, three executors*), the ClassPoint question map, contingencies. For the teaching team: `.docx` and `.html` in the artifact, **not published**. |
| `site/` | The site shell: landing page, vendored reveal.js and the ait4x design tokens. |
| `tools/deckgen.py`, `layouts.py`, `figures.py`, `course.py` | The generator: a 1920×1080 layout engine with html, pptx and png backends, the ait4x layouts (plus a code-and-figure slide and an activity panel), drawn figures (Schotter, Walk-Through-Raster, LeWitt, 10 PRINT, L-systems…), and the shared semester map. |
| `tools/pdf.js` | Prints a built html deck to PDF with Chromium (reveal.js print mode; chips hidden, video thumbnails shown). |
| `tools/snap.js`, `snap.py`, `shot.js` | Snapshots of the live sketches into `deck/assets/sketches/` (the still the pptx and the PDF show; committed), and screenshots of chosen slides with the sketches running, for checking them by eye. |
| `tools/classpoint/build.py` | From the ait4x template kit: theme, master and 8 layouts, entrance animations, ClassPoint buttons and activity tags (word cloud, multiple choice, short answer, image upload; the image-upload model was read back from a deck where the add-in inserted the button). |
| `tools/build_all.py`, `build_docs.py`, `roster.py` | Build everything; markdown → docx/html; ClassPoint roster from a local ID list. |
| `tools/fonts/` | Inter and JetBrains Mono variable fonts: used by the build, and to install on the classroom PC. |

Generated and git-ignored: `_site/` (the site), `export/` (pptx, manifest, docx, previews), `deck/assets/generated/`, `node_modules/`, `classpoint/*.csv`, `ids.csv`.

## Build locally

```bash
pip install -r tools/requirements.txt
python tools/build_all.py --pptx          # export/: PowerPoints, manifest, docx, previews (no node needed)
python tools/build_all.py --site          # _site/: html decks, PDFs, syllabus — needs node + playwright (below)
python tools/build_all.py                 # both
python tools/build_all.py --no-pdf        # skip the PDF step
python deck/week01.py                     # only the Week 1 deck (same for week02.py)
python tools/roster.py ids.csv classpoint/roster-2026-classpoint.csv   # ClassPoint saved class (local only)
```

The PDF step needs node 18+ and Playwright's Chromium: `npm install --no-save playwright@1.56.1 && npx playwright install chromium` in the repo folder (the workflow does the same). The html deck: arrow keys, `S` speaker notes, `O` overview, `F` full screen. Video slides embed YouTube; the pptx and the PDF carry a thumbnail and a link instead. Previews and a text-overflow check land in `export/preview/`.

## Classroom checklist

1. Download the PowerPoint from the latest *Build PowerPoints* run (Actions → Artifacts → `sd2112-powerpoints`).
2. Install `tools/fonts/Inter-Variable.ttf` and `JetBrainsMono-Variable.ttf` on the classroom PC (right-click → install for all users), restart PowerPoint. Slide 1 should show *Inter Black* in the font box; Arial substitutes automatically if not.
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

Slides and site follow the ait4x design system (PolyU Design brand): Pantone Black 6 ink `#000B1C`, white, cool gray, teal `#64C2C3`, the 70-tile secondary matrix for bands, orange `#ED6D24` for the X and for numbers; Inter (display 800–900, tight tracking) and JetBrains Mono (eyebrows, caps, tracked). Tokens: `site/vendor/ait4x-colors_and_type.css`. PowerPoint font names follow `tools/PPTX-EXPORT.md`: *Inter Black* / *Inter ExtraBold* / *Inter* + bold / *JetBrains Mono*.

Scale: the canvas is 1920 × 1080 px on a 13.333 × 7.5 in slide, so **one design pixel is 0.5 pt** in PowerPoint (72 px title = 36 pt, 36 px body = 18 pt, 24 px eyebrow = 12 pt). `deckgen.PT` holds that factor; the kit's master and layouts use the same scale.

## Live, interactive sketches

Any slide can carry a p5.js sketch that runs live in the html deck: `live(name, code, w, h, hint=..., extra=..., sound=False)` from `tools/layouts.py`, placed with `sketch_slide(...)` (full width), or as the media of `content(..., sketch=)`, `figure_slide(..., sketch=)`, `code_slide(..., sketch=)` and `activity(..., sketch=)`. The page (`_site/<deck>/sketches/<name>.html`) scales the canvas to its frame while keeping `mouseX`/`mouseY` right, so mouse, touch and keyboard interaction just work; the deck's navigation keys (arrows, space, Esc, S, O, F) still reach reveal.js when the sketch has the focus, `R` restarts the sketch, and a **LIVE** chip with the `hint` tells the room what to do. A sketch that uses a key itself returns `false` from `keyPressed()`. `sound=True` also loads p5.sound (oscillators, the microphone). Opened on its own (the ↗ in the chip, or from the landing page) the page gets a title bar. p5.js and p5.sound are vendored in `site/vendor/p5`, so all of it works offline in the classroom.

The PowerPoint and the PDF cannot run code, so every sketch has a still twin: either a figure you pass (`figure=` — the Python drawing of the same rule, as week 2 does) or, by default, a snapshot in `deck/assets/sketches/<name>.png` made by `python tools/snap.py <deck>` (1.5 s after load, mouse resting at 60 % / 40 % of the canvas, no click: design the sketch so that state looks right). Snapshots are committed, because the PowerPoint workflow has no browser; a missing one shows as a labelled grey box and a build warning. `code` is what students see (keep it short and readable); `extra` is JavaScript appended only in the page, for the interaction the code panel does not show.

## Adding a week

Copy `deck/week02.py` to `deck/week03.py`, change `FOOTER` and `pdf`, write slides with the layout functions in `tools/layouts.py` (`title`, `agenda`, `section`, `statement`, `quote`, `content`, `cards`, `question`, `image_full`, `timeline`, `journey`, `activity` (with an optional mono `panel` or a live `sketch`), `video`, `assessment`, `team`, `team_band`, `two_col`, `figure_slide`, `code_slide`, `sketch_slide`); every `deck/weekNN.py` is built. Week-specific drawn figures go in `tools/figures_weekNN.py` (names prefixed `wNN-`), shared ones in `tools/figures.py`. Add a card in `site/index.html`. ClassPoint activities come from `question(...)` (word cloud, multiple choice, short answer, image upload) or an explicit `cp={...}`. A `code_slide(..., sketch=(name, js, w, h))` runs the p5.js code live in the html deck (p5.js is vendored in `site/vendor/p5`, so the deck works offline); the figure you pass is what the pptx and the PDF show, so draw the same rule in `tools/figures.py`.
