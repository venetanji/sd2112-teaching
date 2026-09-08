# SD2112 · Artificial Intelligence in Design — teaching repo

Class planning and slides for PolyU School of Design, Semester 1 2026/27.
Lecturer Giovanni Lion (giovanni.lion@polyu.edu.hk) · teaching assistants Nicolò Azzolin, Amber, WU Zhao and MA Jie (in the room 30 min before and after class) · class coordinator Zhibin Zhou.

The repository holds **sources only**. The slide toolchain is not in here either — it is
[`ait4x/deckgen`](https://github.com/ait4x/deckgen), pinned by tag in `requirements.txt` and
shared with [`sd5913/teaching`](https://github.com/sd5913/teaching), so a fix to the PowerPoint
or ClassPoint plumbing lands in both courses at once.

Two GitHub Actions workflows run on every push to `main` (and on demand):

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
| `deckgen.toml` | The course as the generator sees it: code, name, year, footer, which decks, what gets published. |
| `deck/figures.py` | The drawn illustrations — chairs, typicality, perceptron, two machines, mediation. Built on `deckgen.figures.Canvas`. |
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

## After the class: publish the answers

ClassPoint keeps every activity on a **public** page at
`app.classpoint.io/activity/<activityId>` — no login, all the responses on it. Once a week
those links go into the deck, so a student can find their own work again in week 12.

1. Open [the ClassPoint activities dashboard](https://app.classpoint.io/cp/reports/activities).
   It is behind the login and has no API, so save the page: devtools → copy the cards
   element → paste into a file.
2. Run the routine from [`classpoint.py`](https://github.com/venetanji/classpoint.py):

   ```bash
   python3 weekly.py --repo ~/dev/sd2112-teaching --week weekNN \
           --on YYYY-MM-DD --from-html ~/Downloads/activities.html
   ```

   `--on` is the date the class ran, and it matters: it is what separates this course's
   activities from the other one's. The runner fetches each activity, reads
   `deck/weekNN.py` with `ast` to get the question text, and writes
   `deck/weekNN-reports.json` and [`ANSWERS.md`](ANSWERS.md). Both are rewritten in place.
3. `deckgen build` — the eyebrow of every question slide gains a **YOUR ANSWERS** link, and
   the build fails if the deck and the mapping have drifted apart.
4. Commit both files and open a PR.

Each `deck/weekNN.py` calls `attach_reports(S, …)` just before `DECK = …`. It is a no-op
until the mapping file exists, so a week authored today picks its links up the week it is
taught, with no edit.

**Activities run with names hidden are not linked.** ClassPoint's page honours
`isNamesHidden`, but the payload behind it still carries `participantName` for every
response — so linking one would hand out a way to undo the anonymity the room was
promised. `weekly.py` records those with a null id and no link, and `ANSWERS.md` says so.
Week 1's *One hope and one worry* is the current example.

## Keeping the repository public

Nothing in the sources identifies a student. Keep it that way:

- Student IDs, rosters and ClassPoint exports stay local (`ids.csv`, `classpoint/*.csv` are git-ignored); the roster is a one-off local build, not a workflow step, so no secret is needed.
- Grades, gradebooks and submissions never enter the repository, not even in a branch: the history is public too.
- Workflow artifacts on a public repository are downloadable by anyone with a GitHub account: the PowerPoint artifact is fine, a roster would not be.
- Examples of IDs in docs and slides are made up (`3456A`).
- ClassPoint report links are public by design and go in `ANSWERS.md` — but never link an
  activity that was run with names hidden. See **After the class** above.

## Design system

Slides and site follow the ait4x design system (PolyU Design brand): Pantone Black 6 ink `#000B1C`, white, cool gray, teal `#64C2C3`, the 70-tile secondary matrix for bands, orange `#ED6D24` for the X and for numbers; Inter (display 800–900, tight tracking) and JetBrains Mono (eyebrows, caps, tracked). Tokens: `site/vendor/ait4x-colors_and_type.css`. PowerPoint font names follow [`PPTX-EXPORT.md`](https://github.com/ait4x/deckgen/blob/main/PPTX-EXPORT.md) in the generator: *Inter Black* / *Inter ExtraBold* / *Inter* + bold / *JetBrains Mono*.

Scale: the canvas is 1920 × 1080 px on a 13.333 × 7.5 in slide, so **one design pixel is 0.5 pt** in PowerPoint (72 px title = 36 pt, 36 px body = 18 pt, 24 px eyebrow = 12 pt). `deckgen.PT` holds that factor; the kit's master and layouts use the same scale.

## Adding a week

Copy `deck/week01.py` to `deck/week02.py`, change `FOOTER` and `pdf`, write slides with the layout functions in `deckgen.layouts` (`title`, `agenda`, `section`, `statement`, `quote`, `content`, `cards`, `question`, `image_full`, `timeline`, `journey`, `activity`, `video`, `assessment`, `team`, `two_col`, `figure_slide`), add `"week02"` to `decks` in `deckgen.toml`, and add a card in `site/index.html`. ClassPoint activities come from `question(...)` (word cloud, multiple choice, short answer, image upload) or an explicit `cp={...}`.
