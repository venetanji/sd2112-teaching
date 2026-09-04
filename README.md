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
| `deck/week01.py` | **The Week 1 slides as one Python spec**: text, speaker notes, ClassPoint activities, in the order the class runs. Edit here; every output updates. |
| `deck/assets/` | Images the decks use. Drawn figures are generated at build time. |
| `syllabus/SD2112-syllabus-2026.md` | The syllabus: team, outcomes, four modules, 13-week plan with examples and readings, assessment and rubrics, policies. Published on the site; a `.docx` is built too. |
| `lessons/week01-lesson-plan.md` | Week 1 run of show (three hours), the *Push the machine to the edge* activity, the ClassPoint question map, contingencies. For the teaching team: `.docx` and `.html` in the artifact, **not published**. |
| `site/` | The site shell: landing page, vendored reveal.js and the ait4x design tokens. |
| `tools/deckgen.py`, `layouts.py`, `figures.py` | The generator: a 1920×1080 layout engine with html, pptx and png backends, the ait4x layouts, drawn figures. |
| `tools/pdf.js` | Prints a built html deck to PDF with Chromium (reveal.js print mode; chips hidden, video thumbnails shown). |
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
python deck/week01.py                     # only the Week 1 deck
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

## Adding a week

Copy `deck/week01.py` to `deck/week02.py`, change `FOOTER` and `pdf`, write slides with the layout functions in `tools/layouts.py` (`title`, `agenda`, `section`, `statement`, `quote`, `content`, `cards`, `question`, `image_full`, `timeline`, `journey`, `activity`, `video`, `assessment`, `team`, `two_col`, `figure_slide`), add `'week02'` to `DECKS` in `tools/build_all.py`, and add a card in `site/index.html`. ClassPoint activities come from `question(...)` (word cloud, multiple choice, short answer, image upload) or an explicit `cp={...}`.
