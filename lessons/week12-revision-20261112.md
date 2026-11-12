# Week 12 instructor revision / staff handoff / 12 November 2026

## Ownership and state

Isolated clean-at-start detached worktree: `/home/venetanji/.openclaw/workspace-sd2112/tmp/weeks11-12-theory-20261112/week12`, canonical PR25 base `b97d4c05f4173458f6d0feb9535250f266748f70` (`docs/week12-planning`). Week 12 files only; no commit, push, PR, staging or release change by this worker. Week 11 is another worker's responsibility. Local generated `_site/` and `export/` are ignored review artifacts, not publication.

## Teaching edit

36 slides: timed slides 1-34 and two optional reference slides. Week 11's mediation/curation/authorship/Suno vocabulary now leads to the Week 12 question of **justified reliance**: what evidence warrants a suggestion, which actions require specific permission, how a person can refuse/contest/repair, and who can investigate failure. The 2025 Week 12 PDF (70 pages, positions 54-69 reviewed; page 59 visually checked) supplies historical curation/language questions, not its obsolete poster-board URL, date, authorship-law insinuations or "ultimate interface" prediction. The first 75 minutes follow delegation -> 2018 Autopilot investigation -> bounded incorrect-advice experiment -> fictional project revision; they are not disconnected four-paper summaries. The existing walkthrough, mock review and revision remain at full length. Week 13 is quiz and posters with no new theory or invented quiz format.

| Minutes | Segment | Slides |
|---|---|---|
| 0-10 | Reconnect | 1-3 |
| 10-40 | Delegation and Autopilot case | 4-15 |
| 40-65 | Evidence for reliance / Cecil study | 16-20 |
| 65-75 | Evidence to project revision | 21-23 |
| 75-90 | Break | 24 |
| 90-120 | Interface walkthrough | 25-27 |
| 120-155 | Mock review | 28-31 |
| 155-175 | Revision | 32-33 |
| 175-180 | Close | 34 |

Two optional ClassPoint short answers remain at slides 3/34, with oral/private-team-note alternatives. No new assessed collections, deadlines, grading weights, mandatory readings, prototype requirement, print requirement or live-data exercise. Paper/static screens and non-chatbot projects remain complete routes. Existing poster/video/brief and rubric untouched.

## Case and status

The vehicle was a **2017 Model X P100D using Autopilot: Traffic-Aware Cruise Control + Autosteer (SAE Level 2 supervised driver assistance)** on 23 March 2018. It was not Full Self-Driving (Supervised), and it was not autonomous driving. NTSB HAR-20/01 (2020), https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR2001.pdf , downloaded/read 12 November 2026: log reports Autosteer left input ~5.9 seconds before impact, cruise-control acceleration after the lead car was lost ~3.9 seconds before impact, no forward collision warning/automatic braking and impact at ~71 mph. Probable cause includes system limitations and driver nonresponse associated with likely distraction and overreliance; ineffective driver engagement monitoring contributed. Damaged road hardware contributed to severity. No final-minute engagement warning despite intervals without detected wheel torque; absence of torque does not identify exact hand position. The NTSB report distinguishes manufacturer design, driver role, road maintenance and regulator oversight; none alone explains or absolves all others.

Guardian/Reuters reported the family civil suit settled just before trial on **8 April 2024**, with undisclosed terms: https://www.theguardian.com/technology/2024/apr/08/tesla-crash-lawsuit-apple-engineer . That is a contemporary secondary report of court documents, **not** an independently obtained filing or verified docket status through 2026. No jury liability determination in that case is claimed. Company statements and lawsuit allegations are not NTSB findings. Later procedural developments remain uncertain; confirm the actual court docket if a current legal-status announcement is necessary. No graphic/archival crash image or imagined Tesla UI is shown.

Original, editable, labelled conceptual loop, simplified not-to-scale incident layout (left SR-85 exit shown above continuing US-101, orange = nontravel gore, black = damaged attenuator), vehicle-log timeline and responsibility map carry the explanation; case references are visible clickable links on relevant slides. Alternative activation checks/monitoring/fallback are explicitly design hypotheses, not proof of a prevented crash.

## Selected research and images

Cecil et al., *Scientific Reports* (2024), https://doi.org/10.1038/s41598-024-60220-5 : 1,403 participants across five online fictional-CV studies, 16 CV decisions per person; about 75%-correct manipulated advice and no-advice/explanation comparisons; immediate decision accuracy distinct from confidence and perceived advice quality. Wrong-advice trial performance fell; tested explanations did not clearly mitigate wrong-advice reliance. Figure 6a is experiment 2a only: two pooled contrasts (not four arms), 70.61% no-advice baseline and standard-error bars. No real hiring, universal explanation verdict or measured project safety. The publisher PDF Figure 6a passage and p. 15 CC BY 4.0 notice were freshly rechecked; the retained figure crop is publisher CC BY 4.0; exact page/crop/hash/credit and reuse basis are in `deck/assets/week12/provenance.md`. Only this third-party crop is currently embedded. NTSB report is linked rather than redistributed; all case images are original native shapes and include text equivalents. Other old Week 12 paper crops remain archived and are not used in the revised timed slides.

## Local QA

Own `.venv` installed from unchanged pinned `requirements.txt`; Playwright 1.56.1 in `.venv/node_modules`; `/ms-playwright` Chromium selected through `CHROMIUM`. `deckgen build --no-pdf week12` succeeded with zero text overflow and fresh 36-slide HTML/plain/ClassPoint PPTX and PNG previews. This is a target HTML/native build, **not** full-site PDF QA. After fresh exports, full repository `unittest discover -s tests -q`: 135 tests pass. Focused Week 12: 8 pass, including schedule/order, source facts/limits, editable diagrams, notes/plan sync, clickable hrefs, native element bounds and ClassPoint report drift/withholding.

Browser desktop: all 36 slides traversed; no JavaScript errors or failed asset requests; only seven known tight-line-height display/chapter/activity headings trip a generic scrollHeight heuristic, visually not clipped. All other body boxes fit. Three unique primary URLs present; a real click on the visible case diagram source opens the expected NTSB URL. Fresh mobile 390x844 context auto-enters reading view, with 36 handout sections, eight NTSB links, no horizontal overflow, no script/network errors and Deck view restored correctly. Full-size screenshots of changed slides 1-23 on both, plus contact sheets, in `/tmp/week12-case-research/qa/`; copy of sheets in ignored `export/preview/week12/`. All three native generator sheets visually inspected; no crash photo. Both PPTX files: 36/36 paragraph-aware exact native speaker-note matches against source/companion; case and study source hyperlinks in slide relationships; plain has zero ClassPoint activity tags and ClassPoint export has two. A live classroom ClassPoint run and Microsoft PowerPoint render are not established.

Evidence paths: `lessons/week12-evidence-ledger.md`, `lessons/week12-lesson-plan.md`, `lessons/week12-speaker-notes.md`, `deck/assets/week12/provenance.md`, browser reports `/tmp/week12-case-research/qa/{desktop,mobile}-report.json`, previews `export/preview/week12/`. PDF not generated because no print-layout check was needed for the requested HTML/native QA. Remaining limits: no court-docket validation after April 2024; no participant study or physical projector/screen-reader test; no safety guarantee from one case or one experiment. Parent owns integration with Week 11 and any later preview or release decision.

## 12 November continuity correction

Updated speaker notes now refer to the mock-review and revision activities by title instead of stale slide positions; optional earlier-week research is not presented as part of the taught Week 12 study. Closing notes affirm the instructor-confirmed Week 13 quiz and poster session without guessing quiz format or duration. Native notes, companion and activity schedule rechecked after the source correction.
