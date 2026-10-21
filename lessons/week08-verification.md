# Week 8 implementation and verification

Prepared 21 October 2026 for draft PR #21. Local source implementation, not a merge, release, deployment or confirmation of a dated class timetable.

## Produced

- `deck/week08.py`: 32 main slides plus ten untimed appendix slides, using the existing native Deckgen layouts, course typography, palette, footers and activity treatment.
- `deck/week08_figures.py`: original conceptual diagrams; the Week 5 mediation diagram is reused unchanged. No fabricated empirical chart or publisher figure.
- Native speaker notes on all 42 slides, with a synchronized Markdown companion in `week08-speaker-notes.md`.
- Complete 13-paper register, two primary-source evidence ledgers, and a fifteen-minute manual search demonstration with network/login/offline contingencies.
- Week 8 added to the configured build list only. Earlier decks, syllabus, landing page/navigation, workflows, assessment weights and submission requirements are unchanged. Generated exports are ignored, as required by this source-only repository.

## Evidence review

All R1-R13 primary article texts were reviewed in the explicitly identified versions, not merely abstracts. This is a focused claim check, not replication or systematic review. Full citation, access route, supporting page/section and limitation are in `week08-evidence-benefits.md` and `week08-evidence-risks.md`.

- R1 funding/competing-interest correction disclosed in main speaker notes and appendix.
- R2 authenticity result bounded by its six-month nonconcurrent reassessment; conflicting Discussion wording not repeated.
- R4 final Science paper and N=2,405 used; intentions/return preference not treated as long-term addiction or relationship breakdown.
- R5 January PsyArXiv v1 clearly marked working paper, not peer reviewed. No claim that the later SSRN/supplied version is byte-identical; no long-term deskilling claim.
- R6 final five-study publication used, not earlier six-study working paper; temporary relief distinguished from persistence.
- R7 self-reported initiation and factual-chat control distinguished from conversation quality or comparison to human rehearsal.
- R8 source choice distinguished from response ratings, repeated relationships and clinical outcomes.
- R9 symptom outcomes tied to the particular supervised intervention, waitlist and eligibility conditions. Published primary R4/R9 texts accessed via public mirrors after publisher blocks; supplements remain unreviewed. No full paper redistributed.
- Optional R10-R13 remain in the appendix, with qualitative/exploratory/task-specific limits. Vendor account explicitly identified; unverified Friend/BBC cases omitted.

## Local verification completed

- Pinned `requirements.txt` unchanged: Deckgen v0.11.2; per-worktree Python environment and Playwright 1.56.1; existing node Chromium used.
- Unfiltered `.venv/bin/deckgen build` passed for all eight configured weeks, including HTML, standard PDF printing, plain and ClassPoint-compatible PowerPoints, documents, preview images, text-overflow and report-map checks. All eight PDFs built; Week 8 has 42 pages.
- `.venv/bin/python -m unittest discover -s tests -v`: **107 tests passed**. Eight Week 8 regression tests cover timing/order, source boundaries, access fallback, scope/data output, references, notes synchronization, geometry and integration. Non-failing ResourceWarnings originate in Deckgen's image-preview file handles; no source/build failure occurred.
- Browser capture/review: all 42 projected HTML slides at 1920x1080 and all 42 mobile handout sections at 390x844; no body-text overflow, horizontal overflow, missing local resources or JavaScript errors. Mobile Deck view toggle checked. All 42 dual-renderer native preview slides inspected; revised slides confirmed after corrections.
- Final standard PDF page count and font embedding checked. Both PPTX files contain 42 slides, with every native speaker note matching the source and declared Inter/JetBrains Mono font families matching earlier classes. Native previews do not establish actual PowerPoint font resolution on the classroom PC; retain the repository classroom checklist.
- Thirty visible resource anchors across the deck, nineteen unique destinations. A visible R8 link was clicked and navigation to its intended DOI verified with an intercepted target (not a claim that every publisher endpoint is currently reachable). Primary-access success/blocks are recorded separately in the evidence ledgers.
- `git diff --check` passed. No student data, credentials, full-paper PDFs, generated decks or QA screenshots staged.

## Exact local preview

From this branch's checkout on the prepared course node:

```bash
export NODE_PATH="$PWD/.venv/node_modules"
export CHROMIUM="$(printf '%s\n' /ms-playwright/chromium-*/chrome-linux*/chrome | head -n 1)"
test -x "$CHROMIUM"
node /home/venetanji/.openclaw/workspace-sd2112/.openclaw/output-budget/run.mjs -- .venv/bin/deckgen build week08
.venv/bin/python -m http.server 8088 --bind 127.0.0.1 --directory _site
```

Open `http://127.0.0.1:8088/week08/` on that machine. Press `S` for notes; mobile reading mode and Deck view are available. A targeted site build recreates `_site/` with that week; use the unfiltered build when checking a complete course site. This local server does not deploy or publish the course.

## Remaining instructor decisions

- Confirm the actual dated timetable/return clock time. Relative 15-minute break, 15-minute demo, 40-minute research, 25-minute revision and ten-minute comparison are preserved.
- Confirm formal one-page proposal instructions/deadline in Canvas. No new upload or grading requirement is created here; revised scope explicitly includes necessary data and collection limits.
- Decide whether to use the optional brief R9 contrast and whether to preflight a live agent comparison. Manual verification remains the default; Scopus metadata is not assumed to grant abstract/full-text access.
- Confirm the proposed Week 9 recommendations/bias direction, later Double Diamond session, November 6 coverage and ESFQ arrangements against the current official schedule. The syllabus is intentionally not silently rewritten.
- Verify classroom PowerPoint fonts and the instructor's legitimate library access before teaching. No deployment was performed to provide a remote preview.
