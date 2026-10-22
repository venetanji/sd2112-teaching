# SD2112 Week 9 speaker notes

Generated from current native `deck/week09.py` notes, 22 October 2026. Main route 1-40; 41-43 non-assigned reference shelf. No pre-reading, extra assessment or collection. Historical consultation statements describe 21 October; targeted source rechecks are labelled separately.

## 01 / Inside the feed.

Three-hour draft; standalone paper summaries assume no pre-reading. Four topic dividers are transitions within existing budgets, not extra segments. Three-hour draft class: research -> AI-product analysis -> existing team project. Main route ends before the three-slide non-assigned reference shelf; see the updated lesson map. Relative minutes: 0-10 opening; 10-35 mechanism; 35-60 objectives/bias; 60-75 research; 75-90 break; 90-105 controlled ranking demo; 105-135 research/evidence audit; 135-165 redesign and test; 165-180 comparison. Preserve all protected blocks. No date, submission, mark or deadline is announced. The syllabus still lists Week 9 concept board/bias register and Week 10 recommendation systems: this draft follows the intended revised sequence but does not amend the syllabus. Instructor must reconcile Canvas and timetable before teaching.

## 02 / What did your product promise?

About four minutes within the opening. Recall Week 8 humanizing AI and mediation: an apparently friendly adviser or invisible background system shapes what a person can notice and choose. Reuse the existing evidence, not a new team pitch or mandatory prototype. Ask for one concrete moment of use. Products can rank design alternatives, route requests or suggest actions without a scrolling feed. Teams open their own work privately; no projection of personal records and no new upload.

## 03 / Selected for you. By whose objective?

Remaining opening minutes: pairs name a user goal, the system action and a possible proxy. Example: find a suitable workshop versus maximize click probability. These are instructor-authored examples, not claims about a named service. Return to this distinction after mechanisms. A recommendation is part of the product, not just an algorithm hidden behind a neutral screen.

## 04 / How a feed selects.

Ten-second transition within the existing twenty-five-minute mechanism block. The opening asks whose objective; now distinguish selecting candidates, ordering and showing them. The next paper is explained in class: no pre-reading is assumed. Allocate about two minutes to its summary, two to its figure, then abbreviate the original mechanism examples; preserve the spoken reflection.

## 05 / How does YouTube narrow the choice?

Full eight-page RecSys 2016 primary PDF read, including sections 1-5, figures and evaluation tables. Section 2 and Figure 2 on PDF p.2 distinguish candidate generation and ranking; sections 3.5 and 4.3 report offline improvements. Live A/B evaluation is discussed but this is not an independent social-outcome trial. Figure 2 is an architecture, not an empirical effect-size chart. Paper question: scale personalized recommendations to a vast changing video corpus. Transfer: inspect which pool an item can enter before debating its final rank. About two minutes within 10-35. Targeted primary recheck 22 Oct 2026: RecSys 2016 primary eight-page PDF: p.2 section2/Figure2; pp.4-7 sections3.5/4.3 and evaluation figures/table. Historical engineering account, not a current product map or participant welfare trial. No unverified benchmark effect size is quoted. This explanation replaces the old abstract within its existing allocation; no extra minutes.

## 06 / First retrieve. Then rank.

Authentic Figure 2 crop from https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf , PDF position 2 of 8, original 2016 paper. Cropped only surrounding prose/caption; arrows and every diagram label remain intact. Retains the tiny original output thumbnails; these are historical illustrations, not a current app screenshot. Architecture alone establishes neither fairness nor wellbeing. Source classroom-use permission on p.1 retained in asset provenance register. About two minutes, then original teaching schema shows interface/presentation and feedback beyond the two-network architecture.

## 07 / The feed is several decisions.

About three minutes within 10-35 after the R1 summary and figure. Walk a fictional creative-event feed from the available pool to what is actually seen. Candidate selection retrieves a subset; ranking orders it against an objective; presentation determines visibility; interaction becomes possible feedback. A highly relevant item cannot rank if it was excluded upstream. R1 section 2 and Figure 2 support candidate-generation versus ranking as a historical architecture. The five-stage drawing is an instructor synthesis, not a diagram of current YouTube, TikTok or Spotify. Different systems may combine stages, insert business rules or use no learned model. Ask which stage belongs to Machine A, B or A+B; explicit eligibility rules can surround a learned ranker.

## 08 / Similar to what you liked.

About three minutes within 10-35. Teach the principle, not a claim that every recommender uses hand-labelled genres. Features can be explicit metadata or learned vectors; hybrid systems combine signals. Distinguish the item-feature relation from collaborative filtering on slide 10. Do not infer a permanent identity from one click. The example is synthetic and simplified. Historical PDF/PPTX slide 31 makes this distinction; retain it with clearer limits.

## 09 / Near depends on the representation.

About three minutes within 10-35. Recall CLIP/latent representations in Week 5. In the tiny hand-set example all vectors have length one, so their dot product equals cosine similarity; higher cosine means more similar, not smaller distance in every metric. Do not call these two hand-set coordinates an actual trained embedding or a map of personality. R1 section 3.1 defines learned user/video vectors, supporting the representation concept but not this synthetic arithmetic. Historical slide 27 visually relates query/document vectors to a similarity metric; this revision makes the metric and toy status explicit.

## 10 / Learn from a pattern of choices.

About three minutes within 10-35. A nearest-neighbour intuition: another person with overlapping preferences liked C, so C is a candidate for you. This table is not enough to guarantee preference or to fit a production model. Question marks mean unobserved, not negative. Collaborative filtering can instead learn latent factors; it need not explicitly find a human look-alike. R1 section 2 describes collaborative candidate generation using coarse behaviour/history; this is an original pedagogical simplification, not its algorithm or real user data.

## 11 / What can the system honestly infer?

About three minutes within 10-35. Cold start is limited evidence about a new person/item; sparse data also affects established users. The interventions are candidate design choices, not universally effective remedies. R1 introduction and section 3 discuss freshness, sparse implicit feedback and modelling uncertainty around satisfaction. Separate absence of interaction from dislike and from absence of demand. Ask which fields the proposed product truly needs to collect rather than demanding more data by default.

## 12 / A reason is not the whole mechanism.

Final four minutes of the mechanism block. Brief pair exchange; take two spoken answers. This is not an attention-check quiz or ClassPoint submission. A plausible natural-language explanation need not be faithful to the actual ranker. Candidate generation, ranking rules and display can all contribute. Request a product decision, evidence and interpretation rather than a vocabulary definition. Transition: even a faithful explanation does not tell us whether the objective is worthwhile.

## 13 / Whose errors count?

Ten-second transition within 35-60. Keep the goal/proxy distinction; compress the illustrative discussion to make room for a historical audit and a documentation proposal. These are different kinds of paper, neither a live recommendation experiment. All source context is supplied in class. Preserve the fifteen-minute break and downstream team blocks.

## 14 / A click is not the user goal.

About two minutes within 35-60. Fictional event product, not a measured outcome. R1 introduction calls implicit feedback noisy and section 4 contrasts click/watch-time objectives; do not present its 2016 watch-time objective as current YouTube policy. A proxy is not necessarily useless or malicious. It is incomplete relative to the human goal and may create incentives. Teams should state one goal and one candidate measure without assuming the measure proves welfare.

## 15 / The next screen changes the next data.

About two minutes within 35-60. Draw the return arrow verbally: suggestions shape available actions, not just mirror an independent preference. The loop is conceptual, not a claim that every iteration increases bias or polarization. R2 tests a field intervention; R3 tests controlled judgement learning. Their different evidence will prevent treating this diagram as an empirical effect size. Even unchanged preferences can produce different clicks if visibility changes; a behavioural change does not by itself prove changed beliefs.

## 16 / Diversity is a decision to specify.

About two minutes within 35-60. Retain the historical 2025 slide 49 slider/explore-button idea as a design hypothesis, not a proven remedy. Diversity is not one scalar moral property: a topic-diverse list can still omit a community, show unsafe content or overwhelm a person. R1 introduction discusses exploration/exploitation for freshness, not a fairness guarantee. Ask whether exploration should be optional, explained or constrained; do not prescribe a universal setting.

## 17 / Where can a pattern become a problem?

About two minutes within 35-60. Four entry points grouped into three visual cards: collection, labels, objectives and interaction. These are useful analysis handles, not an exhaustive or mutually exclusive taxonomy. Historical slide 43 gives four bias types; avoid implying only malicious design produces unequal effects. Gender Shades (R4, Table 4) found intersectional error disparities in three historical commercial binary gender classifiers: it is not a face-identification/recommender experiment, a definition of anyone's gender or a current vendor audit. Its transferable lesson is to inspect relevant groups and errors rather than an overall average alone. R5 sections 3.2-3.5 offer documentation questions; documentation does not establish fairness. Link and fuller audit context are in the reference shelf.

## 18 / Who disappears inside an average?

Full fifteen-page PMLR PDF read, main text including audit methods, Tables 4-5, discussion and references; supplement not separately reviewed. April-May 2017 system versions; PPB 1,270 individuals from six parliaments. Labels are the study constrained binary categories; paper section 3.4 explicitly criticizes the reductionist view. Section 4.4 and Table 4 p.9 support the disparity. The classifier training data were not disclosed, so the audit does not isolate the cause. About two minutes within 35-60. Targeted primary recheck 22 Oct 2026: PMLR81 primary PDF pp.5-8 benchmark/labels/methods; p.9 Table4. Binary perceived labels and constrained portraits limit transfer. The audit does not isolate error causes or describe current vendors. This explanation replaces the old abstract within its existing allocation; no extra minutes.

## 19 / Read the error row, not just the average.

Authentic full Table 4 crop from https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf , PDF p.9 of 15. All table rows/headers retained; no invented chart or selective reshaping. Explain only error rate (1-TPR); PPV/TPR/FPR remain visible but are not a new statistics lesson. Table describes 2017 versions, not current vendor comparisons. PPB n=1,270; table subgroup denominators differ. Binary perceived labels and relatively fixed-pose parliamentary portraits limit transfer; gender identity cannot be inferred from appearance. About two minutes.

## 20 / What should travel with a dataset?

Full arXiv:1803.09010v8 manuscript read, dated 1 Dec 2021, 18 PDF pages, including example appendix. Sections 1-2 explain the motivation and iterative development with product-team/colleague/legal feedback, not a randomized effectiveness trial. Sections 3.2-3.7 provide questions; section 4 p.11 says datasheets are not a complete solution and notes dynamic-data and overhead challenges. Do not conflate version/typesetting with CACM publication. About two minutes, followed by the collection excerpt. Targeted primary recheck 22 Oct 2026: arXiv1803.09010v8,1Dec2021 PDF pp.2-4 objectives/development; p.7 section3.3; p.11 implementation limits. Actual source excerpt follows. Documentation supports scrutiny, not proof of fairness, fair pay or legal compliance. Questions are not a new required assignment. This explanation replaces the old abstract within its existing allocation; no extra minutes.

## 21 / Ask who did the work.

Authentic document excerpt, NOT a figure or empirical result: one complete collection/compensation question from section 3.3, PDF p.7 of 18, arXiv:1803.09010v8, 1 Dec 2021. https://arxiv.org/pdf/1803.09010v8 . Other surrounding questions cover validation, sampling and consent. Main paper has no empirical labour-effect chart to reproduce. About one minute; connect to data boundaries, keeping all questions contextual and optional rather than a newly required submission template.

## 22 / Useful does not mean necessary.

About three minutes, with remaining 35-60 time for questions. R5 composition/collection/maintenance questions cover identifiability, consent and retention. This is design analysis, not jurisdiction-specific legal advice, a promise that deletion is technically immediate or an empirical re-identification rate. Optional Netflix de-anonymization paper remains background only; no attack procedure or number is asserted without reading its assumptions. Ask about downstream copies/inferences as well as source records. Teams must use synthetic examples, not collect classmates' histories or put user records in tools/prompts.

## 23 / A feed can change us.

Ten-second transition inside the original fifteen-minute evidence block. Move from auditing a system output to studying changes in people. Explain one field experiment and one controlled task, each with a standalone summary before reading its authentic figures. Budget five minutes R2, five R3, remaining time comparison/transition. No additional homework reading or lecture time.

## 24 / Can changing a feed change people?

About two minutes for this summary, then three for the actual figure, within 60-75. Published open-access Nature article retrieved 21 Oct 2026: online 18 Feb 2026, volume 652 pp. 416-423. Read Design, Impact, Discussion and Methods including figure captions. 6,043 completed baseline, 4,965 completed post-survey (main sample), 2,387 shared follow data. July-September 2023, average 7 weeks + 1 day. Random assignment within initial feed groups permits intention-to-treat comparisons, not a randomized lifetime exposure history. Activation versus staying chronological shifted conservative policy-priority/current-event indices and conservative activist following; removal in initially algorithmic users did not produce comparable reversals. Authors support a following/exposure mechanism but acknowledge unobserved differences between initial-feed groups may contribute to asymmetry. Do not say the whole mechanism was independently randomized or that all algorithms radicalize. Most compliance self-report, 599 post-survey extension users, no transfer to current X or Hong Kong users established. Supplementary PDF/replication not independently reviewed or reproduced. Reset design is our hypothesis, not a validated remedy. Targeted primary recheck 22 Oct 2026: Published Nature HTML Design, Impact, Figure4 caption and Methods/ITT; retained21Oct2026, targeted recheck22Oct. No clear partisanship/affective-polarization effect does not establish zero effect. Largely self-reported compliance. Following is not an independently randomized sole mediator; reset remains a hypothesis. This explanation replaces the old abstract within its existing allocation; no extra minutes.

## 25 / Following is not just a feed setting.

Figure 4, publisher full-size image, https://www.nature.com/articles/s41586-026-10098-2/figures/4. Two assembled condition excerpts: authentic top political-leaning/activist rows and their corresponding original x-axes; unchanged full shared legend proportionally resized below each. Right excerpt repeats original shared row labels. White gutters identify assembly; no data redrawn. Earlier three faithful crops retained in assets as historical provenance. Omitted news/entertainment/official rows are not implied absent; full figure linked. n=2,387 consenting follow-data participants, not all 4,965 survey completers. Units are standardized intention-to-treat effects; blue unconditional and orange covariate-adjusted estimates; bars 90%/95% confidence intervals. Follow the conservative activist row, not every coefficient. Random assignment is within initial feed settings; prior lifetime exposure was not randomized. No significant partisanship/affective-polarization effect in Figure 2. Product reset remains a hypothesis, not a tested remedy. Use about three minutes after the two-minute summary, within 60-75.

## 26 / Can advice change your next judgement?

About two minutes for this summary, then one procedure and two results minutes, within 60-75. Published online 18 Dec 2024, NHB 9, 345-359 (2025). Publisher full HTML retrieved; Results, Discussion and Methods reviewed. Overall n=1,401 includes supplementary experiments, not a single feed sample. Focus on experiment 2: 120 Prolific participants estimated moving-dot direction, first alone then with accurate, rightward-biased or noisy hard-coded algorithms in counterbalanced order. Algorithm output was revealed after participants' own estimate/weighting. Later independent estimates shifted in the biased condition; accurate advice improved accuracy. Follow-up n=50 per biased/accurate condition examined repeated interaction. This is not merely copying the current displayed answer. It is also not a news-ranking experiment or proof of lasting everyday preference change. Experiment 1 uses a CNN/emotion task; experiment 3 uses Stable Diffusion 2.1 image exposure (not a current model benchmark). The narrative has a reversed-label sentence in Results under input/perception; Fig. 1 caption and Methods distinguish the conditions correctly. No numerical label-effect claim used here. Supplement PDF/computational fits not independently checked or reproduced. Targeted primary recheck 22 Oct 2026: Published NHB HTML Methods/RDK main experiment and effects across time; Results/Figure2a-c,e,g. Retained21Oct, targeted recheck22Oct. Hard-coded algorithms, not trained recommendation models. Later independent estimates distinguish learning from current-answer copying; persistence beyond the task remains unknown. This explanation replaces the old abstract within its existing allocation; no extra minutes.

## 27 / Estimate first. See the advice later.

Authentic contiguous crop of Figure 2 panels a-c, not a recreated experiment. https://www.nature.com/articles/s41562-024-02077-2/figures/2 . Published main HTML consulted in full including Methods. Main experiment n=120 Prolific participants; 30 baseline trials then counterbalanced accurate, rightward-biased and noisy hard-coded algorithms, 30 trials each. The distributions in b are the paper schematic algorithm response patterns, not a new empirical plot. Use one minute to explain the procedure; no in-class experiment is being run.

## 28 / Learning can go in either direction.

Figure 2e,g, authentic separate crops from the published HTML full-size Figure 2; each preserves axes, values, error bars and panel letter. Left n=50 biased-algorithm follow-up; right a DIFFERENT n=50 accurate-algorithm follow-up. The vertical axes measure different outcomes: induced signed bias versus accuracy improvement (baseline error minus current error); do not compare their heights as one common scale. Horizontal axis is five interaction blocks within a task, not days or years. Error bars are standard errors of the mean, not individual ranges. Charts concern independent estimates before the current advice; no field-feed, lasting effect or mitigation established. Use about two minutes within 60-75, then compare study contexts. Primary URL https://www.nature.com/articles/s41562-024-02077-2/figures/2 .

## 29 / Different studies answer different questions.

Remaining evidence-block minutes before break. Ask teams to name population, system, comparator, outcome and time before asserting a filter bubble or an echo chamber. These terms overlap in ordinary use but do not name one measured outcome. R2 found no significant affective-polarization/partisanship effect despite other changes; R3 establishes controlled learning mechanisms, not field effect sizes. A null is not proof of universal absence, and a positive result is not universal presence. R2's main article discusses contrasting prior Meta results; that citation is background, not independently re-reviewed here. Do not claim a fresh systematic review or consensus. Use one methods/results excerpt in discussion, not two new compulsory full papers.

## 30 / Break. 15 minutes.

Preserve the full fifteen-minute break. Announce the actual return clock time in class once the timetable is confirmed. Next is one fifteen-minute controlled demo, then thirty minutes research and thirty minutes redesign/test. Open slides 31-32; the full fallback is native and needs no login, network or learned model.

## 31 / Same four items. Two scoring rules.

First seven minutes of one fifteen-minute demo. Scores 0-10 are invented by the instructor for a fictional creative-workshop feed: relevance means fit to a prior interest; novelty means difference from that prior interest. Neither is estimated from people. Same four candidates, no filtering, personalization training, click simulation, accounts or network. Ask for a prediction: which two items enter the top two under each rule? Rule A = 0.8 relevance + 0.2 novelty; rule B = 0.3 relevance + 0.7 novelty. Compute A by hand: 0.8*9+0.2*1=7.4 under rule A; 0.3*9+0.7*1=3.4 under rule B. Optional local terminal: .venv/bin/python deck/week09_demo.py. All values, formulas and results are already native on these slides; if terminal/code fails, continue on paper without changing the activity budget. Do not present this weighted rule as a learned recommender or as study data.

## 32 / The objective changes the shortlist.

Remaining eight minutes of the same fifteen-minute block. Both lists are generated from week09_demo.py at import, not transcribed separately. Decimal arithmetic, deterministic ID tie-break and input validation make the local script reliable. Rule A scores A7.4 B7.0 C5.6 D5.0; rule B scores D7.5 C7.1 B4.5 A3.4. Hold candidates and scores fixed: only weights change. This isolates a scoring choice in the toy setup, not real user utility. Ask what did NOT change: candidate pool, feature definitions, who chose the scores and missing needs/accessibility. No evidence that B is fairer, safer, more satisfying or less polarizing. A native/PDF/handout reader has the whole calculation and outcome. Teams can reproduce one row on paper and choose an outcome to test in the real project.

## 33 / Change one decision.

Ten-second orientation within 105-135, not extra time. The toy ranking changed only a weight. Now use an actual relevant source to justify or challenge a decision in the existing team project. Preserve thirty minutes research and thirty minutes redesign/test (twenty plus ten). No ClassPoint, mark, upload or deadline is added; current Canvas concept-board/bias-register scope remains to be confirmed.

## 34 / Investigate your existing decision.

105-135, one thirty-minute block over slides 34-35. Suggested internal checkpoints: five minutes question/keywords, fifteen close reading/access, ten evidence card and comparison. A team with no feed examines its own selection/ranking/adaptation decision rather than inventing a feature. Manual route: open PolyU Library or a primary DOI, verify title/authors/version, find Methods and Results, follow references. No automated gated access, new service account or private project/user data in search prompts. Agents may suggest citations only if humans open and verify them. If network/library fails, use R2 Design/Discussion or R3 experiment 2 from the prepared evidence ledger, explicitly as a prepared example, not live discovery. Keep all work in existing team notes; no upload.

## 35 / What does the paper actually support?

Leave visible during reading. Use actual passage locations, not agent-invented page numbers. An HTML subheading can replace a PDF page. A vendor description, a systematic review and a primary experiment serve different evidential purposes. One strong relevant paper is better than three irrelevant abstracts. Abstract-only access should stay labelled; do not infer unobserved procedures. Prepared offline card in lessons/week09-evidence-ledger.md includes primary passage, method and limit for R2/R3. That ledger is instructor-authored extraction, not a substitute for the full paper or a new assignment.

## 36 / Change one decision inside your product.

135-165, one thirty-minute block over slides 36-38: twenty minutes redesign then ten test planning, as in the approved activity foundation. Redesign one objective, data boundary, explanation or usable control; not a whole new product. Retaining a choice with stronger evidence can be a valid revision. The group proposal/concept board/bias register already in the syllabus are not cancelled or rescheduled here. Confirm actual Canvas instructions separately. If the class runs late, trim lecture/debrief detail rather than the fifteen-minute break, thirty-minute research or thirty-minute redesign/test.

## 37 / Who might this revision miss?

This is part of the twenty-minute redesign portion, not a third timer. Ask who contributes data/labour, who gets visibility and who bears errors. Relevant groups need not map to the demographic categories in Gender Shades. Do not collect sensitive attributes merely to fill a template; identify an evidence gap and plan an ethical check. A proposed control is not automatically mitigation: can a person find it, understand it and see whether it changed anything? Paper sketches are sufficient. No private participant research is required today. Worked row / instructor illustration, not a new submission: decision=rank workshops; data=tagged catalogue and prior clicks; missing perspective=people with access needs absent from our evidence; false positive=an inaccessible option ranked suitable; false negative=a suitable option hidden. Proposed recourse=editable access constraints plus browse-all and correction. Test whether a person can recover a suitable option; neither access labels nor control effectiveness are established. This adapts the archived bias-register scaffold to the current fictional example within the same redesign time.

## 38 / What result would change your mind?

Final ten minutes of the thirty-minute redesign/test block. Example design hypothesis: an optional unfamiliar-event control helps people discover suitable events without losing task success. Candidate outcomes: chosen event fits stated constraints, unwanted exposure, ability to understand and undo a selection; compare baseline/revised under similar conditions. Do not imply a classroom sketch can establish causal effectiveness in every population. Plan only; no demand to recruit participants, expose people to harmful content or collect new sensitive data. An explicit failure condition and transfer boundary matter more than statistical jargon.

## 39 / Compare decisions, not ethical slogans.

About ten minutes. Invite two teams, with permission, to describe reasoning without disclosing personal/user data. One minute explanation each, then compare differences and discuss. Do not add a required pitch deck, ClassPoint upload, grade or public answer link. Listen for context and method rather than polished production. If no teams volunteer, use the fictional workshop toy and compare a relevance objective with a novelty objective; explicitly label it an instructor example.

## 40 / Keep the evidence and the open question.

Final five minutes. Ask one spoken closing question: what did evidence make you less certain about, and what can you now test? The intended revised sequence moves into Double Diamond reframing/testing; no date or syllabus amendment is made by this deck. The published syllabus currently lists recommendations in Week 10 and concept board/bias register in Week 9. Instructor must reconcile these with Canvas and the separately drafted Week 10 material. Preserve the existing group assessment and deliverables. Team work stays private unless existing approved channels require otherwise.

## 41 / Candidate generation is not ranking.

NON-ASSIGNED BACKGROUND / untimed reference shelf. Primary full eight-page PDF retrieved from Google research archive and consulted for sections 1-4 and Figure 2. DOI 10.1145/2959100.2959190. R1 is mechanism background, not current product documentation, independent audit or proof of social effects. The simplified collaborative matrix and hand-set vector arithmetic in this deck are instructor-authored, not reproduced training examples. No production benchmark is asserted.

## 42 / Read the design, not just the headline.

NON-ASSIGNED BACKGROUND / untimed reference shelf. Both publisher HTML full texts accessed 21 Oct 2026. Gauthier, Hodler, Widmer and Zhuravskaya; Glickman and Sharot. Evidence ledger records passage locations, comparator/outcome/time and transfer limits. Supplementary PDFs and data/code replication were not independently reviewed. A full-text consultation is not replication or a systematic review. Prepare one short excerpt from either paper for the timed comparison rather than assigning both as compulsory new homework.

## 43 / An average can hide a relevant difference.

NON-ASSIGNED BACKGROUND / untimed reference shelf. Gender Shades, PMLR 81, 1-15 (2018), Table 4 and dataset/limitations sections. Historical commercial versions, parliamentary-portrait benchmark and binary gender labels: do not generalize to current vendors or define gender identity from an image. R5 arXiv 1803.09010v8, 1 Dec 2021, manuscript consulted, distinct from asserting identical typesetting to the CACM version. Read sections 3.2-3.7. Source scope for privacy/labour is documentation questions, not legal advice or universal labour statistics. Historical Week 9 PDF/PPTX pp./slides 40-41 visually feature Joy Buolamwini/AJL; this deck replaces uncaptioned historical imagery with a primary audit and correct task boundaries.
