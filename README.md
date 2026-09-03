# SD2112 · Artificial Intelligence in Design — teaching repo

Class planning, slides, and the pipeline that builds them. PolyU School of Design, Semester 1 2026/27.
Lecturer Giovanni Lion · teaching assistants Nicolò and Amber (in the room 30 min before and after class) · class coordinator ZHOU Zhibin.

## What is here

| Path | What |
|---|---|
| `syllabus/SD2112-syllabus-2026.md` (+ `.docx`) | The refreshed syllabus: team, outcomes, four modules, weekly plan with examples and readings, assessment and rubrics, policies. |
| `lessons/week01-lesson-plan.md` (+ `.docx`) | Week 1 run of show, the *Teach the machine what a chair is* activity, ClassPoint questions and what to do with the answers, contingencies. |
| `deck/week01.py` | **The Week 1 slides, as one Python spec** (text, notes, ClassPoint activities). Edit here, rebuild, both outputs update. |
| `docs/` | The course site for GitHub Pages: `index.html`, `week01/` (reveal.js deck), `syllabus.html`, `week01-lesson-plan.html`, vendored reveal.js and fonts. |
| `export/week01-classpoint.pptx` | **The classroom PowerPoint**: ait4x master and layouts, entrance animations, ClassPoint buttons and activity tags on 10 slides. |
| `export/week01.pptx` | The same deck without the post-processing (plain, editable). `export/week01-activities.json` is the ClassPoint manifest. |
| `export/preview/*.jpg` | Contact sheets of every slide (PIL render of the pptx geometry, and Chromium screenshots of the html deck). |
| `classpoint/roster-2026-classpoint.csv` | ClassPoint saved-class roster: last four digits + letter of each student ID (114 names, same convention as the 2025 gradebook). |
| `tools/deckgen.py`, `tools/layouts.py`, `tools/figures.py` | The generator: layout engine on a 1920×1080 canvas, html / pptx / png backends, ait4x layouts, drawn figures (parametric chairs, typicality, perceptron). |
| `tools/classpoint/build.py` | From the ait4x template kit: theme, master and 8 layouts, animations, ClassPoint tags. Patched to read the footer and the activity manifest from the environment and to run on Python 3.11. `tools/PPTX-EXPORT.md` explains the font rules. |
| `tools/fonts/` | Inter and JetBrains Mono variable fonts (install on the classroom PC). |
| `deck/assets/` | Images used in the decks (reused from the 2025 decks, four generated chairs, drawn figures). |

## Build

```bash
pip install python-pptx pillow markdown python-docx   # once
python deck/week01.py          # docs/week01/, export/week01.pptx, export/week01-classpoint.pptx, previews
python tools/build_docs.py     # syllabus and lesson plan -> .docx and docs/*.html
```

Optional QA (what was run before committing):

```bash
python <pptx-skill>/scripts/office/validate.py export/week01-classpoint.pptx     # schema and package checks
NODE_PATH=$(npm root -g) node tools/screenshot.js http://127.0.0.1:8765/week01/index.html export/preview/html-week01   # with `http-server docs -p 8765`
```

The html deck: arrow keys to navigate, `S` speaker notes, `O` overview, `F` full screen, `?print-pdf` in the URL for a PDF. Video slides embed YouTube; the pptx carries a thumbnail and a link instead.

## Classroom checklist (from the template kit)

1. Install `tools/fonts/Inter-Variable.ttf` and `JetBrainsMono-Variable.ttf` on the classroom PC (right-click → install for all users). Restart PowerPoint. Slide 1 should show *Inter Black* in the font box. Fallback: Arial substitutes automatically.
2. Open `export/week01-classpoint.pptx` with the ClassPoint add-in. Fire one activity (slide 3, word cloud) before class; a malformed tag fails silently.
3. Import `classpoint/roster-2026-classpoint.csv` as the saved class. Students join with the last four digits and the letter of their ID (e.g. `8695D`).
4. Keep the html deck open on a laptop as backup: `docs/week01/index.html` (or the Pages URL).

## GitHub Pages

`.github/workflows/pages.yml` publishes `docs/` on every push to `main` (and to `claude/**` branches) with the official Pages actions, and tries to enable Pages automatically. If the first run fails on enablement, turn it on once in **Settings → Pages → Source: GitHub Actions**, then re-run the workflow. Note: the repository is private; GitHub Pages on a private repository needs a plan that includes it (GitHub Pro, Team, or Enterprise; teachers get Pro through GitHub Education). Making the repository public also works and is the usual choice for course material.

Site URL once live: `https://venetanji.github.io/sd2112-teaching/` (deck at `/week01/`).

## Design system

Slides and site follow the ait4x design system (PolyU Design brand): Pantone Black 6 ink `#000B1C`, white, cool gray, teal `#64C2C3`, the 70-tile secondary matrix for bands, orange `#ED6D24` for the X and for numbers; Inter (display 800–900, tight tracking) and JetBrains Mono (eyebrows, caps, tracked). Tokens are in `docs/vendor/ait4x-colors_and_type.css`; the full system was supplied as `ait4x_Design_System.zip`. PowerPoint font names follow `tools/PPTX-EXPORT.md`: *Inter Black* / *Inter ExtraBold* / *Inter* + bold / *JetBrains Mono*.

Scale: the design canvas is 1920 × 1080 px on a 13.333 × 7.5 in slide, so **one design pixel is 0.5 pt** in PowerPoint (a 72 px title is 36 pt, 36 px body is 18 pt, 24 px eyebrows are 12 pt). `deckgen.PT` holds that factor; the kit's master and layouts use the same scale.

## Adding a week

Copy `deck/week01.py` to `deck/week02.py`, change `FOOTER`, write slides with the layout functions in `tools/layouts.py` (`title`, `agenda`, `section`, `statement`, `quote`, `content`, `cards`, `question`, `image_full`, `timeline`, `journey`, `activity`, `video`, `assessment`, `team`, `two_col`, `figure_slide`), and run it. ClassPoint activities come from `question(...)` (word cloud, multiple choice, short answer) or an explicit `cp={...}`. Add the deck to `docs/index.html`.
