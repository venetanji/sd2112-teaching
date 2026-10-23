# Week 11 revision verification / 22 October 2026

Current source set is the isolated prepared worktree at `tmp/weeks09-13-standard-20261022/week11/worktree`, baseline d7c43ba (published main54f38c7 plus canonical Week11 remote). No commits, pushes, PR edits, deployments, registration changes, shared-generator edits or original-worktree edits.

## Reconciliation and teaching contract

- Checked every preserved VersionB file against baseline-state SHA256 before copying and again after authoring. Original unchanged. All six tracked week-specific files were identical between original base dff469e and current remote; applied the actual local delta without overwriting any remote-only choice. Reconciliation decisions are in task-local `reconciliation.json`.
- 36 main-route slides plus one bibliography appendix (37 total), exactly180 minutes. Opening0-15; evidence15-45; curation/authorship45-75; break75-90; communication90-110; audit110-140; peer140-165; debrief165-180. Zero ClassPoint activities. No added pre-reading, submission, deadline, marks or class minutes.
- Six taught sources: Naqvi interviews; Doshi randomized starting ideas; Gebru documentation proposal; Joshi interface experiments; U.S. official legal analysis; Verbeek philosophy. Each has task/question, comparison/analysis, concrete labelled example and measurement/evidence basis before findings/application. Legal/philosophical/documentation work is not presented as an experiment.
- Week-owned repeated paper title x120/y184/w1680/h140, size72; label/body gap52; citations y956. Existing course Inter/mono typography retained. Shortened overflowing copy rather than shrinking type. Paper citations end994, above actual footer y1000; tests now use the actual footer rather than an incompatible old990 heuristic.
- Agency, material contribution, permission, contestability, accountable actor and the fictional guide's unresolved trade-off remain visible. Project40%, A0 poster,3-5min video,one-page brief and within-project30/30/20/10/10 rubric unchanged. Canvas milestones/mock review/current local legal advice remain confirmations.

## Current source and rights checks

Targeted recheck of retained primary methods/results/legal/conceptual passages, not a fresh full-paper read or current-law survey. Exact versions/pages/access in evidence ledger. Source-page and figure visual inspections retained privately. Public-review distribution is explicitly public GitHub PR source plus Cloudflare HTML, not local-only.

Four source assets remain: two Doshi crops/assembly and Joshi Fig1 under verified CC BY4.0 notices; official Part2 text excerpt under documented U.S. federal-text17USC105 basis. Exact attribution/changes/hash/licence recorded. Naqvi participant artwork and Gebru/Verbeek facsimile crops are omitted because a supported public-republication basis was not established; original VersionB copies remain untouched. Attributed text adaptations and instructor illustrations preserve their teaching purpose. Full papers remain private; no blanket legal clearance claimed.

## Historical pre-P2 test/build receipts

A checkout-local .venv was created using requirements.txt Deckgen v0.11.2 (resolved commit9990546), uv link-mode=copy; Playwright1.56.1 installed only under .venv. Existing preinstalled Chromium1246 used via CHROMIUM; no browser download or package patch.

- Focused: `.venv/bin/python -W ignore::ResourceWarning -m unittest discover -s tests -p 'test_week11*.py'`:10 tests pass.
- Full: `.venv/bin/python -W ignore::ResourceWarning -m unittest discover -s tests`:137 tests pass,28.466s. Private logs: task-local focused-tests.log/full-tests.log. No unrelated test edits.
- Build: standard output-budget wrapper around `.venv/bin/deckgen build --no-pdf week11`: exit0,37 slides,0 activities,no overflow/stderr. Current content receipt `run-1792655001940-9b9ab331-9f65-43b9-a5ca-3ab74189889b`; task-local build-receipt.json. Initial overflows were corrected in source and successful build repeated. Parent owns combined/full-PDF verification.
- `git diff --check`: pass. Only authorized Week11 files changed.

## Historical pre-P2 visual, browser and native QA

The following preserves the original author QA claim for audit history, not current P2 acceptance. Independent review W11-01 found the full three-panel Joshi image unreadable on mobile; native summaries did not satisfy actual-source legibility. Superseding P2 evidence is below. Original task-local evidence is under `tmp/weeks09-13-standard-20261022/week11/`, not the older21October directory.

- All37 desktop1600x900 active Reveal slides captured; all37 fresh390x844 mobile visible handout sections captured; all37 native generator previews inspected in contact sheets. Full-size figure/axis, interview-result and legal-position confirmation checked separately. No observed title/label/citation collision, clipped body, missing image or horizontal mobile overflow. Authentic small UI/report text is supplemental; essential task, measure and finding are readable native text, and images/primary citations are clickable.
- `browser-qa.json`:37 desktop +37 mobile sections; zero page errors; no horizontal handout bounds failures. All18 visible text/image primary-resource links activated on each mode:36/36 intended requests. External requests are intercepted in QA after navigation activation, so this verifies destination/clickability, not external-host uptime or access. Deck control changes visible mobile handout to deck; captured body state `reveal-viewport` confirms toggle.
- `native-integrity.json`: plain/ClassPoint PPTX each37 slides and37 exact source-note matches;14 external hyperlink relationships;four named paper images plus course logos;zero activity models. All37 companion entries match final source/native notes. Native previews/XML do not substitute for physical Microsoft PowerPoint/font/projector verification.
- Local HTML `_site/week11/index.html` is built, not hosted. Parent owns combined integration and authorized remote/hosted delivery.

## Historical evidence and remaining caveats

Earlier28-slide and VersionB32+1 records stay under `tmp/weekly-draft-audit-20261021/` and `tmp/paper-visual-revision-20261021/`; they are not current QA. Instructor still confirms relative-to-clock timetable, current team state, Canvas milestones/mock review, physical fonts/projector and jurisdiction-specific advice. No main release or worldwide legal clearance is implied.

## P2 / W11-01 mobile correction / current acceptance

Only the Joshi interface illustration on existing result slide 20 changed: `joshi-fig1a-motor.png` is authentic Fig. 1(a), not a redrawn chart. Exact author-v3 PDF1, its figure caption and CC BY 4.0 notice were re-read; a 240-dpi source render was visually inspected. Crop `(172,664,706,1202)` from 2040x2640 retains the full motor-cost panel (534x538), including instruction, prompt, gauge and pictured 113 reps. No controls/text/colours were redrawn. Caption, native notes, companion and provenance disclose that (b)/(c) are omitted; linked image/citation open the full primary source. Task slide 19 retains all comparisons; results, 37-slide count, 180-minute timing, activities, assessment and typography unchanged. The old three-panel asset/provenance and original author-report/browser QA stay historical rather than retroactively becoming valid legibility proof.

- Checkout `.venv`, pinned requirements and existing Chromium: targeted `build --no-pdf week11` exits 0, no overflow or stderr. Parent retains full-course/PDF/hosted integration responsibility.
- Current focused suite: 11 pass; full suite: 138 pass (27.970s). `git diff --check` passes; Impeccable mechanical detector returns `[]`, exit 0.
- Inspected full-size native 960x540 preview, desktop Reveal 1600x900 viewport and full-height fresh 390x844 mobile section. Mobile crop renders 350x352.609px, rather than reducing all three panels into a 350px landscape strip. Its heading, story prompt, progress-bar instruction, pumping explanation and 113-reps example are readable in the retained capture; no title/caption/native-body clipping or collisions observed. This does not claim large-print accessibility or real-device/physical-projector verification.
- Browser: no page errors, no mobile text/image horizontal overflow; both visible primary links target exact arXiv v3, with a real primary-link activation per mode verified by intercepted navigation request (not external-host uptime).
- Plain and ClassPoint PPTX: each 37 slides, 37/37 exact normalized source-note matches, zero activity models. Slide 20 embedded pixels exactly match the new 534x538 source crop in each package; all companion notes match source.
- New receipts/captures: task-local `mobile-fix-qa/{build-receipt,browser-report,native-report}.json`, `focused-tests.log`, `full-tests.log`, `desktop-20.png`, `mobile-20.png`; current native preview at `worktree/export/preview/week11/slide-20.png`. Handoff `mobile-fix.md/json` lives adjacent to the unchanged historical author report. No commit/push/API mutation or other-week source edit.
