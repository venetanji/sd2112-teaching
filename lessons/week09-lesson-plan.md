# SD2112 · Week 9 lesson plan

**Recommendations, bias and reflective use** · implemented local slide draft · October 29, 2026

## Status and source reconciliation

This draft follows the latest intended sequence: Week 8 humanizing AI, Week 9 recommendations/bias, Week 10 Double Diamond reframing/testing. It now has a 51-slide native Deckgen implementation for review, not a timetable announcement or a syllabus amendment. The class is Friday 30 October 2026, confirmed by Giovanni on 28 October 2026.

The earlier draft recorded published main at 54f38c7 with approved Weeks 1-8. This polish checkout starts from 6fe8c92; parent owns combined integration and PR updates. This is not a fresh check of published main. Old [PR #3](https://github.com/venetanji/sd2112-teaching/pull/3) contains an unmerged Week 9 bias/privacy deck and Week 10 recommendation deck. Reuse ideas selectively, not those weeks' obsolete tooling, assumed submissions, Blackboard deadlines or slide numbers.

The original 50-page 2025 Week 9 PDF has now been recovered and visually inspected. Historical slide pointers: Week 9 pages 23–37 cover recommendations, embeddings, filtering and echo chambers; pages 38–45 cover bias, labour and consequences; pages 47–49 propose platform redesign. Pages 40–41 are image-heavy facial-analysis/AJL material and belong in the bias discussion; the cited Gender Shades study audits binary gender classification, not face identification. Page 49 proposes a diversity slider and explore-new-spaces button. Update these historical examples with the research below rather than treating the old deck as immutable.

## Purpose

The feed looks personal, but each stage expresses choices about what to collect, retrieve, rank and show. A model is not a passive, neutral mirror of humanity: it transforms selected traces through representations and objectives, and its use can change what people notice and do. Students explain a mechanism, identify two examples of AI bias, closely examine one with a comparison, and redesign how a person can notice and respond.

Research → AI-product context → existing team project remains the teaching pattern. Week 8's papers and project-specific research remain part of an accumulating evidence base; today adds the recommendation/data layer rather than replacing it.

By the end, students can:

- Describe candidate selection, ranking, presentation and feedback as distinct stages.
- Compare content-based and collaborative filtering and identify a cold-start limitation.
- Explain an embedding as a representation whose similarity depends on its construction and metric, not an objective description of a person.
- Locate bias in collection, labels, objectives and feedback, including human labour and missing perspectives.
- Distinguish inductive assumptions, learned regularities and harmful social bias; a repeated pattern is not automatically an error or injustice.
- Relate Heidegger, Ihde and Verbeek to Van Den Eede's questions about transparency in use and the visibility of mediation's social context.
- Document two examples, closely examine one and support a reflective interaction revision with evidence, a limitation and a testable outcome.

## Preparation and roles to allocate

The instructor should allocate these tasks; names in earlier plans do not establish current commitments.

- Technical support: preflight any toy similarity/ranking demo, provide static screenshots and a paper fallback, check ClassPoint settings if used.
- Research support: prepare accessible copies/links for selected readings, with page pointers for claims. Use manual library access where appropriate; no automated gated access.
- Facilitation: bring a blank evidence/decision sheet, help teams formulate project-specific questions, and check that cited work actually supports claims.
- Instructor: retain the R1–R5 research walkthroughs and prepare the bounded mediation bridge; confirm current Canvas instructions, and select anonymized examples only if permission allows their classroom use.

Do not assume every team already has a prototype or has submitted a formal proposal. A sketch and a defined product decision are enough to enter the activity.

## Implemented three-hour run of show

Relative timings are a planning allocation. Optional 28 October news uses at most five minutes **inside** the opener, replacing elaboration. It does not consume the protected activity time. Six clear topic dividers take approximately ten seconds within their blocks, not extra minutes.

| Minutes | Segment | Actual slides |
|---|---|---|
| 0–10 | Orient: user goal, selected outputs and the next choice | 1–3 |
| 10–25 | Mechanisms: R1 walkthrough/architecture, filtering, representations | 4–12 |
| 25–45 | Bias: three meanings, proxies, R4 audit, R5 documentation | 13–23 |
| 45–60 | Mediation: selected traces, Heidegger/Ihde/Verbeek, Van Den Eede, reflective use | 24–28 |
| 60–75 | Feedback studies: R2 field experiment and R3 controlled task | 29–35 |
| 75–90 | Protected break | 36 |
| 90–105 | Same controlled ranking demo | 37–38 |
| 105–135 | Identify two examples of AI bias; compare and examine one closely | 39–41 |
| 135–165 | Reflective redesign + test planning: 20 + 10 minutes | 42–45 |
| 165–180 | Compare examples, changed interaction and remaining uncertainty | 46–47 |

## Actual slide map

### Visual teaching pass / 29 October

The projected deck now uses diagrams, historical study images and short visual
instructions rather than prose-heavy cards. Detailed explanations remain in
speaker notes; the sequence, timing and assessment contract are unchanged.
Following the Week 8 teaching pattern, each of the five paper walkthroughs
keeps a **concrete example in simple English on screen**, before the authentic
source figure or excerpt. Explain what changes, what is compared, and what the
result does and does not establish; do not assume pre-reading.

- R1: an invented workshop app first chooses 100 candidates, then shows 10;
  ranking cannot rescue a workshop excluded earlier.
- R2: two illustrative people start with newest-first feeds; one switches and
  one stays. Compare later following. The diagram shows assignment within
  each initial feed group, not random past exposure.
- R3: a 53% guess and 73% advice combine to 65% with 40/60 weighting. The weight
  is chosen before advice. Ask whether the next unaided estimate changes.
- R4: an invented five wrong labels among 100 portraits means 5% error. Compare
  within-group percentages; then inspect the actual historical audit table.
- R5: a workshop is tagged "relevant". Who chose the label, who paid them, and
  what remains unknown? This is documentation, not an effectiveness experiment.

Keep invented examples visibly distinct from reported findings. Original
schematics do not replace the authentic research figures or their limitations.

**47-slide main route + 4 non-assigned reference slides.** No pre-reading assumed: all five research papers retain their standalone task/argument, comparison, labelled worked example and measurement/evidence walkthrough before the authentic source figure/excerpt. Engineering and documentation are not participant experiments. Philosophy is an analytical framework, not a sixth effectiveness experiment. Extra slides separate ideas; they do not add teaching minutes.

1. **Inside the feed.**
2. **What shapes the next choice?**
3. **Selected for you. By whose objective?**
4. **How a feed selects.**
5. **How does YouTube narrow the choice?**
6. **First retrieve. Then rank.**
7. **The feed is several decisions.**
8. **Similar to what you liked.**
9. **Near depends on the representation.**
10. **Learn from a pattern of choices.**
11. **What can the system honestly infer?**
12. **A reason is not the whole mechanism.**
13. **Whose errors count?**
14. **Learning is selective. Is it unfair?**
15. **A click is not the user goal.**
16. **The next screen changes the next data.**
17. **Diversity is a decision to specify.**
18. **Where can a pattern become a problem?**
19. **Who disappears inside an average?**
20. **Read the error row, not just the average.**
21. **What should travel with a dataset?**
22. **Ask who did the work.**
23. **Useful does not mean necessary.**
24. **Not just a mirror.**
25. **Whose humanity does AI reflect?**
26. **Using a tool also shapes our experience.**
27. **Transparent in which sense?**
28. **Pause. Compare. Choose differently.**
29. **A feed can change us.**
30. **Can changing a feed change people?**
31. **Following is not just a feed setting.**
32. **Can advice change your next judgement?**
33. **Estimate first. See the advice later.**
34. **Learning can go in either direction.**
35. **Different studies answer different questions.**
36. **Break. 15 minutes.**
37. **Same four items. Two scoring rules.**
38. **The objective changes the shortlist.**
39. **Find and question bias.**
40. **Find two examples of AI bias.**
41. **What makes this an example of bias?**
42. **Change the interaction.**
43. **Change how the person can respond.**
44. **Who might this revision miss?**
45. **What changes in the interaction?**
46. **From spotting bias to changing the relation.**
47. **Keep the example and the open question.**
48. **Candidate generation is not ranking.** Non-assigned reference shelf only.
49. **Read the design, not just the headline.** Non-assigned reference shelf only.
50. **An average can hide a relevant difference.** Non-assigned reference shelf only.
51. **Read the distinctions in context.** Non-assigned reference shelf only.

### Pacing inside the retained budget

- 0–10: orient and recall one concrete decision; discuss the user's goal versus the system's proxy. The optional news bridge replaces up to five minutes here only.
- 10–25: R1 walkthrough 2 minutes, architecture figure 1, pipeline 2, content-based filtering 1, vectors 2, collaborative example 2, cold start 1, spoken explanation check 3, divider/transitions 1. Use the examples to contrast mechanisms, not narrate every bullet or teach vector arithmetic from scratch.
- 25–45: divider + bias distinctions 2 minutes; goal/proxy/feedback/diversity 5; bias entry points 2; R4 walkthrough/table 4; R5 walkthrough/excerpt 3; privacy 2; questions/transition 2. A learned regularity, statistical error and harmful unequal consequence are different claims. Read the IBM row within its subgroup denominators; do not infer undisclosed training-data causes.
- 45–60: divider + selected traces 2 minutes; Heidegger/Ihde/Verbeek recall 3; Van Den Eede use/context questions 4; reflective-use comparison 5; transition 1. Ask what becomes noticeable and what action becomes possible, not whether more explanation automatically makes a system fair.
- 60–75: divider + R2 walkthrough/figure 5 minutes; R3 walkthrough/procedure/results 5; distinguish task, measures, transfer and transition 5. Read highlighted rows/axes, not every coefficient. Different n=50 follow-ups and different outcomes are not directly comparable bar heights.
- 90–105: inspect the same four invented inputs 4 minutes; compare the two scoring rules/results 6; discuss whose objective changed and what the demo cannot establish 5. All arithmetic and fallback are visible natively.
- 105–135: transition + identify two examples 10 minutes; compare them and closely document one 15; state uncertainty and a next check 5. This replaces the previous broad paper-search task, not an extra activity.
- 135–165: transition + redesign 20 minutes, then test planning 10; keep the evidence and benefits/burdens prompts visible rather than introducing additional timers.
- 165–180: two-team spoken comparison 10 minutes, carry-forward/open question 5. No fairness winner or new pitch deliverable.
- Protect the full break and later blocks. If behind, trim lecture elaboration/reference discussion, not activity time. No new ClassPoint question: count stays zero.

## Activity: identify bias, then change the interaction

### 1. Identify two examples and closely examine one, 30 minutes

Use existing Week 8 research, a documented case, a permitted public output, or an optional safe test with invented inputs. Identify **two examples of AI bias**, compare the kind of claim each makes, then select **one for close examination**. Do not force a feed into a project that has none. A sketch or a documented example is enough; no mandatory prototype, paid account, live generation or new paper quota.

For the selected example, keep these items in existing private team notes:

- System and task; source link/version and relevant passage/page, or model/version/date when available, exact invented prompt/input, settings and output for a safe test.
- Observation and comparison: what happened, compared with what? Distinguish a documented finding from our observation and our hypothesis. A matched comparison is useful; one pair remains exploratory, not a population-level audit.
- Interpretation: identify an inductive assumption, learned regularity, error or harmful consequence without collapsing them. Do not infer the training corpus or designer intention from an output alone.
- Consequence: who is favoured, excluded or misrepresented, for this task and context? Not every repeated pattern establishes unfairness.
- Uncertainty: what else could explain it, what does the evidence not establish, and what would you check next?

Do not collect classmates' accounts, faces, histories or sensitive attributes, run harmful prompts, or upload private assets. If access fails, use the prepared Gender Shades table and existing permitted course examples, explicitly labelled as historical evidence or instructor illustration rather than new discoveries. A suspected risk can remain a hypothesis; do not manufacture an observed disparity to fill the activity.

### 2. Reflective redesign, 20 minutes

Use the selected example to sketch the current interaction and a revised one. Transfer the insight to the existing project only where relevant. Annotate what the person notices, accepts and does before and after:

- Make one relevant hidden assumption or selection visible at the point of use, not a wall of technical detail.
- Offer a meaningful response: compare, question, correct, override, browse an alternative or refuse.
- Identify who still cannot use the control, what burden it adds and who remains responsible for correction.
- Retain the evidence, transfer limitation, required data and one avoidable inference; connect to the existing bias register without inventing a new required template.

Heidegger's absorbed use helps ask what recedes; Ihde and Verbeek help analyse changed perception/action; Van Den Eede keeps fluent use and reflection on social context in view. These are related, not identical theories. Reflection can change attention, interpretation and action without retraining. A warning without usable recourse is not meaningful agency, and responsibility does not move from the designer to the user merely because a warning exists.

### 3. Test planning, 10 minutes; then spoken comparison, 15 minutes

Compare the original and revised interaction on a safe task. Name an observable outcome, a comparator and a failure condition that would change or remove the revision. Separate awareness, ability to act, task success and unequal burdens; improvement in one does not prove the others. Plan the comparison rather than recruit participants or claim a full audit in class.

For example, can a person detect and correct an unsuitable workshop suggestion using an explanation and editable access constraints, compared with the original ranked list? Access labels and control effectiveness remain unverified. The toy scoring demo illustrates a mechanism; it does not establish that either ranking or the reflective redesign is fair, safe or effective. Awareness alone is not mitigation.

During the debrief, two teams show their example/comparison, consequence/uncertainty and changed interaction without personal data. Keep the source, comparison, limitation, sketch and proposed test for the next session in existing team notes. No new submission channel, mark, upload, deadline or ClassPoint collection is created.

## Reading and reuse register

Core selection for the instructor, not an instruction that all readings must be assigned:

- Covington, Adams & Sargin (2016), **Deep Neural Networks for YouTube Recommendations**: https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/ . Useful for distinguishing candidate generation and ranking; a historical system paper, not a verified map of today's live product.
- Koren, Bell & Volinsky (2009), **Matrix Factorization Techniques for Recommender Systems**: https://doi.org/10.1109/MC.2009.263 . Mechanism background, not a universal product recipe.
- Buolamwini & Gebru (2018), **Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification**: https://proceedings.mlr.press/v81/buolamwini18a.html . A specific audit of classification systems, not a recommendation-system experiment or a claim about current versions.
- Gebru et al., **Datasheets for Datasets** (2018 preprint; 2021 CACM): https://arxiv.org/abs/1803.09010 . Documentation questions for the team's data assumptions; documentation alone does not establish fairness.
- Narayanan & Shmatikov (2008), **Robust De-anonymization of Large Sparse Datasets**: https://www.cs.cornell.edu/~shmat/shmat_oak08netflix.pdf . Optional bridge between recommendation data and privacy; inspect the attack assumptions before numerical claims.
- Zuiderveen Borgesius et al. (2016), **Should we worry about filter bubbles?**: https://policyreview.info/articles/analysis/should-we-worry-about-filter-bubbles . Historical research review; do not present its 2016 conclusion as a fresh 2026 consensus.
- Verbeek (2015), **Beyond Interaction**: https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf . Connect the feed to mediation and human agency.

Source reuse: [old Week 9 source](https://github.com/venetanji/sd2112-teaching/blob/83733ca09969da3439c251260a45549a16f12e71/deck/week09.py), [old Week 10 source](https://github.com/venetanji/sd2112-teaching/blob/83733ca09969da3439c251260a45549a16f12e71/deck/week10.py). Do not copy their unsupported promises, platform logistics or obsolete build commands.

## Implementation and review gates before teaching

- Reconcile additional instructor-supplied slides and the final Week 8 work.
- Verify any contemporary product claim or legal statement from a current primary source. No current legal advice is supplied by this plan.
- Confirm actual project stage, current Canvas milestones and demo accessibility.
- Current source: `deck/week09.py`; deterministic demo: `deck/week09_demo.py`. Native notes companion: [week09-speaker-notes.md](week09-speaker-notes.md); primary-claim/access/version ledger and offline cards: [week09-evidence-ledger.md](week09-evidence-ledger.md); truthful build/QA record: [week09-verification.md](week09-verification.md). Target-week builds do not establish a full-course site build or deployment.
- No ClassPoint collection is added. The explanation check and closing comparisons are spoken reflections; activities remain existing private team notes. The report-attachment hook is retained and safely no-ops until a legitimate mapping exists; a stale nonempty mapping is rejected.
- Ranking demo is complete and native/static: all four invented items, two formulas and both result lists are visible. Optional local Python runs identical arithmetic; no browser sketch, service, new account or model is required.
- All substantive claim boundaries are visible near their findings, with methods/transfer/access detail in native notes and the evidence ledger. Instructor must still check classroom readability, links/network and any actual ClassPoint add-in use separately.
- Preserve the published assessment requirements unless explicitly revised; do not publish student work or private records.

## Existing syllabus milestone to reconcile

The current syllabus lists a Week 9 concept board and bias register. This revised sequence does not cancel or reschedule those existing milestones; reconcile their scope and actual Canvas instructions before teaching.

## Selected research refresh: recommendations and feedback loops

Both contemporary studies receive a short standalone summary and actual figure explanation in class. Neither is compulsory pre-reading. Other bibliography-only entries remain non-assigned background.

- Gauthier, Hodler, Widmer & Zhuravskaya (2026), **The political effects of X’s feed algorithm**, Nature: https://doi.org/10.1038/s41586-026-10098-2 . A randomized seven-week US X experiment conducted in 2023 found that activating the algorithmic feed shifted some policy attitudes and follow choices; switching it off was not symmetric. It found no significant effect on self-reported partisanship or affective polarization. The platform/time-specific setting and largely self-reported compliance limit transfer. Do not summarize this as “all algorithms radicalize.” Discussion: if recommendations change whom I follow, what should “reset recommendations” reset? Proposed design exercise: distinguish feed mode, history and following controls, then choose an outcome beyond engagement.
- Glickman & Sharot (online 2024; 2025 issue), **How human–AI feedback loops alter human perceptual, emotional and social judgements**, Nature Human Behaviour: https://doi.org/10.1038/s41562-024-02077-2 . Controlled experiments show that biased AI can amplify subsequent human bias, while accurate AI can improve judgement. This supports a feedback-loop mechanism, not a real-world recommender effect size. Discussion: when does a recommendation stop reflecting preference and start teaching it? Map choice → data → recommendation → changed judgement and identify a test point.

Teach these through **Can changing a feed change people?** to **Learning can go in either direction.** within 60–75, then carry their limitations into the bias-example and reflective-redesign activities. Proposed controls are design hypotheses, not proven remedies. The historical audit/documentation papers retain walkthroughs and source images within 25–45, not an extra lecture block.

The mediation bridge adds Mitchell (1980), **The Need for Biases in Learning Generalizations**, and Van Den Eede (2011; online 2010), **In Between Us: On the Transparency and Opacity of Technological Mediation**, alongside Verbeek (2015). See the evidence ledger for precise source/read scope and the non-assigned **Read the distinctions in context.** shelf. Heidegger and Ihde originals were not newly read; their recall is checked through the mediation articles. No new compulsory reading is created.
