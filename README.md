# SD2112 · Artificial Intelligence in Design — teaching repo

Class planning and slides for PolyU School of Design, Semester 1 2026/27.
Lecturer Giovanni Lion · teaching assistants Nicolò and Amber (in the room 30 min before and after class) · class coordinator ZHOU Zhibin.

The repository holds **sources only**. Every push to `main` builds the html decks, the ClassPoint PowerPoints, the documents and the site with GitHub Actions, publishes the site to GitHub Pages, and keeps the PowerPoints as a downloadable artifact.

Site: `https://venetanji.github.io/sd2112-teaching/` · Week 1 deck: `/week01/` · PowerPoint: `/week01/SD2112-week01-classpoint.pptx`

## Layout

| Path | What |
|---|---|
| `deck/week01.py` | **The Week 1 slides as one Python spec**: text, speaker notes, ClassPoint activities. Edit here; both outputs update. |
| `deck/assets/` | Images the decks use (reused from the 2025 decks, four generated chairs, two video thumbnails). Drawn figures are generated at build time. |
| `syllabus/SD2112-syllabus-2026.md` | The syllabus: team, outcomes, four modules, weekly plan with examples and readings, assessment and rubrics, policies. Published on the site; a `.docx` is built too. |
| `lessons/week01-lesson-plan.md` | Week 1 run of show, the *Teach the machine what a chair is* activity, ClassPoint question map, contingencies. For the teaching team: built as `.docx` and `.html` in the artifact, **not published**. |
| `site/` | The site shell: landing page, vendored reveal.js and the ait4x design tokens. |
| `tools/deckgen.py`, `layouts.py`, `figures.py` | The generator: a 1920×1080 layout engine with html, pptx and png backends, the ait4x layouts, drawn figures (parametric chairs, typicality, perceptron, mediation). |
| `tools/classpoint/build.py` | From the ait4x template kit: theme, master and 8 layouts, entrance animations, ClassPoint buttons and activity tags. Patched to run on Python 3.11+, to read the footer and the activity manifest from the environment, and to use the 0.5 pt/px scale. `tools/PPTX-EXPORT.md` explains the font rules. |
| `tools/build_all.py`, `build_docs.py`, `roster.py` | Build everything; markdown → docx/html; ClassPoint roster from a local ID list. |
| `tools/fonts/` | Inter and JetBrains Mono variable fonts: used by the build, and to install on the classroom PC. |
| `.github/workflows/build.yml` | Build + Pages deploy on push to `main` (and on demand). |

Generated and git-ignored: `_site/` (the site), `export/` (pptx, manifest, docx, previews), `deck/assets/generated/`, `classpoint/*.csv`.

## Build locally

```bash
pip install -r tools/requirements.txt
python tools/build_all.py        # _site/ and export/, exactly as the workflow does
python deck/week01.py            # only the Week 1 deck (html + pptx + previews)
python tools/roster.py ids.csv classpoint/roster-2026-classpoint.csv   # ClassPoint saved class (local only)
```

The html deck: arrow keys, `S` speaker notes, `O` overview, `F` full screen, add `?print-pdf` to the URL for a PDF. Video slides embed YouTube; the pptx carries a thumbnail and a link instead. Previews and a text-overflow check land in `export/preview/`.

## Classroom checklist

1. Download the PowerPoint from the site (or the `sd2112-decks` artifact of the latest workflow run).
2. Install `tools/fonts/Inter-Variable.ttf` and `JetBrainsMono-Variable.ttf` on the classroom PC (right-click → install for all users), restart PowerPoint. Slide 1 should show *Inter Black* in the font box; Arial substitutes automatically if not.
3. Open the deck with the ClassPoint add-in and fire one activity (slide 3, word cloud) before class; a malformed tag fails silently.
4. Import the roster as the saved class. Students join with the last four digits and the letter of their ID (e.g. `8695D`).
5. Keep the html deck open on a laptop as backup.

## Design system

Slides and site follow the ait4x design system (PolyU Design brand): Pantone Black 6 ink `#000B1C`, white, cool gray, teal `#64C2C3`, the 70-tile secondary matrix for bands, orange `#ED6D24` for the X and for numbers; Inter (display 800–900, tight tracking) and JetBrains Mono (eyebrows, caps, tracked). Tokens: `site/vendor/ait4x-colors_and_type.css`. PowerPoint font names follow `tools/PPTX-EXPORT.md`: *Inter Black* / *Inter ExtraBold* / *Inter* + bold / *JetBrains Mono*.

Scale: the canvas is 1920 × 1080 px on a 13.333 × 7.5 in slide, so **one design pixel is 0.5 pt** in PowerPoint (72 px title = 36 pt, 36 px body = 18 pt, 24 px eyebrow = 12 pt). `deckgen.PT` holds that factor; the kit's master and layouts use the same scale.

## Adding a week

Copy `deck/week01.py` to `deck/week02.py`, change `FOOTER` and `download`, write slides with the layout functions in `tools/layouts.py` (`title`, `agenda`, `section`, `statement`, `quote`, `content`, `cards`, `question`, `image_full`, `timeline`, `journey`, `activity`, `video`, `assessment`, `team`, `two_col`, `figure_slide`), add `'week02'` to `DECKS` in `tools/build_all.py`, and add a card in `site/index.html`. ClassPoint activities come from `question(...)` (word cloud, multiple choice, short answer) or an explicit `cp={...}`.
