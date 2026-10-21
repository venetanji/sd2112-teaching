# SD2112 · Week 9 lesson plan

**Recommendations, bias and the decisions inside a feed** · planning draft · October 21, 2026

## Status and source reconciliation

This draft follows the latest intended sequence: Week 8 humanizing AI, Week 9 recommendations/bias, Week 10 Double Diamond reframing/testing. It is a plan for review, not a built deck, a timetable announcement or a syllabus amendment. October 30 is an inferred date, not independently confirmed.

Current main contains Weeks 1–7. Week 8 is being developed separately in [PR #21](https://github.com/venetanji/sd2112-teaching/pull/21); do not edit that branch to implement this plan. Old [PR #3](https://github.com/venetanji/sd2112-teaching/pull/3) contains an unmerged Week 9 bias/privacy deck and Week 10 recommendation deck. Reuse ideas selectively, not those weeks' obsolete tooling, assumed submissions, Blackboard deadlines or slide numbers.

The original 50-page 2025 Week 9 PDF has now been recovered and visually inspected. Historical slide pointers: Week 9 pages 23–37 cover recommendations, embeddings, filtering and echo chambers; pages 38–45 cover bias, labour and consequences; pages 47–49 propose platform redesign. Pages 40–41 are image-heavy face-recognition/AJL material and belong in the bias discussion. Page 49 proposes a diversity slider and explore-new-spaces button. Update these historical examples with the research below rather than treating the old deck as immutable.

## Purpose

The feed looks personal, but each stage expresses choices about what to collect, retrieve, rank and show. Students should explain a recommendation mechanism, question its objective and evidence, and revise the decisions inside their own product.

Research → AI-product context → existing team project remains the teaching pattern. Week 8's papers and project-specific research remain part of an accumulating evidence base; today adds the recommendation/data layer rather than replacing it.

By the end, students can:

- Describe candidate selection, ranking, presentation and feedback as distinct stages.
- Compare content-based and collaborative filtering and identify a cold-start limitation.
- Explain an embedding as a representation whose similarity depends on its construction and metric, not an objective description of a person.
- Locate bias in collection, labels, objectives and feedback, including human labour and missing perspectives.
- Support one product revision with a relevant paper, a limitation and a testable outcome.

## Preparation and roles to allocate

The instructor should allocate these tasks; names in earlier plans do not establish current commitments.

- Technical support: preflight any toy similarity/ranking demo, provide static screenshots and a paper fallback, check ClassPoint settings if used.
- Research support: prepare accessible copies/links for selected readings, with page pointers for claims. Use manual library access where appropriate; no automated gated access.
- Facilitation: bring a blank evidence/decision sheet, help teams formulate project-specific questions, and check that cited work actually supports claims.
- Instructor: choose the core studies, confirm the class date and current Canvas instructions, and select anonymized examples only if permission allows their classroom use.

Do not assume every team already has a prototype or has submitted a formal proposal. A sketch and a defined product decision are enough to enter the activity.

## Proposed three-hour run of show

Relative timings are a planning allocation. Optional news is coordinated separately and must not consume the protected project work without an explicit adjustment.

| Minutes | Segment | Proposed slides |
|---|---|---|
| 0–10 | Reconnect to evidence and the current product decision | 1–3 |
| 10–35 | How recommendations work | 4–9 |
| 35–60 | Objectives, feedback, bias and hidden labour | 10–15 |
| 60–75 | Research comparison and product implications | 16–18 |
| 75–90 | Break | 19 |
| 90–105 | Small controlled recommendation demo | 20–21 |
| 105–135 | Team research and evidence audit | 22–23 |
| 135–165 | Redesign one recommendation/decision and specify a test | 24–26 |
| 165–180 | Compare revisions, record limits and next steps | 27–28 |

## Slide construction plan

These are proposed slots, not existing slide numbers.

1. The recommendation is part of the product.
2. Week 8 connection: what relationship and expectation did the team identify?
3. Today's question: what is selected for this person, and by whose objective?
4. Feed anatomy: pool → candidates → ranking → presentation → feedback.
5. Content-based filtering: item features and similarity.
6. Embeddings: what is near depends on the representation.
7. Collaborative filtering: the user–item pattern, with a small readable matrix.
8. Cold start and sparse evidence: what can the system honestly infer?
9. Check understanding: distinguish a recommendation from an explanation of it.
10. Value versus proxy: what is easy to measure, and what does the user actually want?
11. Feedback loops: the screen changes the data used to make the next screen.
12. Exploration and exposure: why diversity is a design choice, not a magic guarantee.
13. Four entry points for bias: collection, labels, objectives and interaction.
14. Human labour: who labels, moderates, maintains and absorbs errors?
15. Privacy and control: which data is necessary, retained or inferred?
16. Gauthier et al.: randomized feed intervention, changed follow choices, and limits on generalization.
17. Glickman/Sharot: controlled human–AI feedback-loop experiments; distinguish a mechanism from a live recommender effect size.
18. Evidence limits: filter-bubble claims depend on platform, population, measure and time.
19. Break.
20. Demo: rank a small synthetic set under two explicit objectives or feature weightings.
21. Compare what changed, what stayed hidden and what the demo cannot establish.
22. Search the team's own question; include alternative explanations and contrary evidence.
23. Read and log the study population, system, comparator, finding and limitation.
24. Redesign one decision: objective, data boundary, explanation or user control.
25. Map who benefits and who may be poorly served; name the missing evidence.
26. Specify a test that could change the design decision.
27. Compare two teams' choices and trade-offs without declaring one universal fairness metric.
28. Save the evidence and carry the open question into the reframing/prototyping session.

## Activity: from evidence to a different decision

### 1. Investigate, 30 minutes

Begin with the team's existing research. Prioritize one well-supported claim from a closely read paper; compare 2–3 sources already accumulated where feasible. This is not a new paper quota for marks. A team whose product has no feed should investigate its selection/ranking/personalization decision; do not force a recommendation feature into every concept.

For each usable paper, record the citation, the relevant passage/page, study context, what it supports and what it does not establish. Distinguish papers from vendor descriptions and news reports. If no sufficiently relevant evidence is found, keep that as an explicit gap and narrow the product claim.

### 2. Redesign, 20 minutes

Draw the existing decision and one revised version. Annotate:

- The user's goal and the system's measurable proxy.
- Required data and one field or inference the product can avoid.
- Who is missing or misrepresented, and the consequence of being wrong.
- A control, explanation or fallback that a person could actually use.
- The research that motivated the revision and the transfer limitation.

### 3. Test planning and comparison, 10 minutes plus debrief

Choose one observable outcome, a comparison and a failure condition. A toy simulation illustrates a mechanism; it does not prove that the product is fair, safe or effective. Keep the team's notes for the next session. No new submission channel, mark or deadline is created here.

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

## Review gates before teaching

- Reconcile additional instructor-supplied slides and the final Week 8 work.
- Verify any contemporary product claim or legal statement from a current primary source. No current legal advice is supplied by this plan.
- Confirm date, actual project stage, current Canvas milestones and demo accessibility.
- Build in the current course style; inspect every slide/export, bibliography and ClassPoint mapping. No render or full-course build has been performed for this docs-only plan.
- Preserve the published assessment requirements unless explicitly revised; do not publish student work or private records.

## Existing syllabus milestone to reconcile

The current syllabus lists a Week 9 concept board and bias register. This revised sequence does not cancel or reschedule those existing milestones; reconcile their scope and actual Canvas instructions before teaching.

## Selected research refresh: recommendations and feedback loops

Use one short methods/results excerpt in class and the second paper as background or a comparison, not two compulsory full-paper homework readings.

- Gauthier, Hodler, Widmer & Zhuravskaya (2026), **The political effects of X’s feed algorithm**, Nature: https://doi.org/10.1038/s41586-026-10098-2 . A randomized seven-week US X experiment conducted in 2023 found that activating the algorithmic feed shifted some policy attitudes and follow choices; switching it off was not symmetric. It found no significant effect on self-reported partisanship or affective polarization. The platform/time-specific setting and largely self-reported compliance limit transfer. Do not summarize this as “all algorithms radicalize.” Discussion: if recommendations change whom I follow, what should “reset recommendations” reset? Proposed design exercise: distinguish feed mode, history and following controls, then choose an outcome beyond engagement.
- Glickman & Sharot (online 2024; 2025 issue), **How human–AI feedback loops alter human perceptual, emotional and social judgements**, Nature Human Behaviour: https://doi.org/10.1038/s41562-024-02077-2 . Controlled experiments show that biased AI can amplify subsequent human bias, while accurate AI can improve judgement. This supports a feedback-loop mechanism, not a real-world recommender effect size. Discussion: when does a recommendation stop reflecting preference and start teaching it? Map choice → data → recommendation → changed judgement and identify a test point.

Use these at slide slots 16–17, then carry their limitations into the platform-redesign exercise. Proposed controls are design hypotheses, not proven remedies. Retain the historical audit/documentation readings as supporting material rather than adding another lecture block.
