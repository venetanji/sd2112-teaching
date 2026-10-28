# SD2112 · Week 9 lesson plan

**Recommendations, bias and the decisions inside a feed** · implemented local slide draft · October 22, 2026

## Status and source reconciliation

This draft follows the latest intended sequence: Week 8 humanizing AI, Week 9 recommendations/bias, Week 10 Double Diamond reframing/testing. It now has a 43-slide native Deckgen implementation for review, not a timetable announcement or a syllabus amendment. The class is Friday 30 October 2026, confirmed by Giovanni on 28 October 2026.

Published main at 54f38c7 includes approved Weeks 1-8. This isolated Week 9 checkout preserves that baseline; parent owns combined integration and PR updates. Old [PR #3](https://github.com/venetanji/sd2112-teaching/pull/3) contains an unmerged Week 9 bias/privacy deck and Week 10 recommendation deck. Reuse ideas selectively, not those weeks' obsolete tooling, assumed submissions, Blackboard deadlines or slide numbers.

The original 50-page 2025 Week 9 PDF has now been recovered and visually inspected. Historical slide pointers: Week 9 pages 23–37 cover recommendations, embeddings, filtering and echo chambers; pages 38–45 cover bias, labour and consequences; pages 47–49 propose platform redesign. Pages 40–41 are image-heavy facial-analysis/AJL material and belong in the bias discussion; the cited Gender Shades study audits binary gender classification, not face identification. Page 49 proposes a diversity slider and explore-new-spaces button. Update these historical examples with the research below rather than treating the old deck as immutable.

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
- Instructor: the taught selection is R1–R5; confirm current Canvas instructions, and select anonymized examples only if permission allows their classroom use.

Do not assume every team already has a prototype or has submitted a formal proposal. A sketch and a defined product decision are enough to enter the activity.

## Implemented three-hour run of show

Relative timings are a planning allocation. Optional news is coordinated separately and must not consume the protected project work without an explicit adjustment.

| Minutes | Segment | Actual slides |
|---|---|---|
| 0–10 | Reconnect to existing product decision | 1–3 |
| 10–35 | How a feed selects: R1 walkthrough, actual architecture, mechanisms | 4–12 |
| 35–60 | Whose errors count: proxy/data choices, R4 audit, R5 documentation | 13–22 |
| 60–75 | A feed can change us: R2 field study and R3 controlled task | 23–29 |
| 75–90 | Protected break | 30 |
| 90–105 | Same controlled ranking demo | 31–32 |
| 105–135 | Team research/evidence audit, including brief transition | 33–35 |
| 135–165 | Redesign + test: 20 + 10 minutes | 36–38 |
| 165–180 | Compare and carry forward | 39–40 |

## Actual slide map

**40-slide main route + 3 non-assigned reference slides.** No pre-reading assumed: all five papers used in teaching have a standalone plain-English walkthrough before their image/excerpt. More slides split explanation from evidence; they do not add teaching minutes. Section dividers take approximately ten seconds within their block. Every paper starts with task/argument, comparison, a labelled worked example and measurement/evidence before the source figure/result. Engineering and documentation are explicitly not participant experiments. Repeated titles/labels use the Week 8 grid; technical details remain in notes.

1. **Inside the feed.**
2. **What did your product promise?**
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
14. **A click is not the user goal.**
15. **The next screen changes the next data.**
16. **Diversity is a decision to specify.**
17. **Where can a pattern become a problem?**
18. **Who disappears inside an average?**
19. **Read the error row, not just the average.**
20. **What should travel with a dataset?**
21. **Ask who did the work.**
22. **Useful does not mean necessary.**
23. **A feed can change us.**
24. **Can changing a feed change people?**
25. **Following is not just a feed setting.**
26. **Can advice change your next judgement?**
27. **Estimate first. See the advice later.**
28. **Learning can go in either direction.**
29. **Different studies answer different questions.**
30. **Break. 15 minutes.**
31. **Same four items. Two scoring rules.**
32. **The objective changes the shortlist.**
33. **Change one decision.**
34. **Investigate your existing decision.**
35. **What does the paper actually support?**
36. **Change one decision inside your product.**
37. **Who might this revision miss?**
38. **What result would change your mind?**
39. **Compare decisions, not ethical slogans.**
40. **Keep the evidence and the open question.**
41. **Candidate generation is not ranking.** Non-assigned reference shelf only.
42. **Read the design, not just the headline.** Non-assigned reference shelf only.
43. **An average can hide a relevant difference.** Non-assigned reference shelf only.

### Pacing inside the retained budget

- 10–35: transition + R1 walkthrough/figure about 4 minutes; remaining 21 minutes for the mechanism schema, filtering, vectors, cold start and spoken reflection. Do not narrate every bullet.
- 35–60: about 4 minutes goal/proxy + feedback, 3 minutes diversity and bias entry points, 4 minutes R4 walkthrough/table, 3 minutes R5 walkthrough/excerpt, 3 minutes privacy; use the remaining time for questions/transitions, not an added quiz. Labour is taught through the paper question instead of the old duplicate slide.
- 60–75: R2 walkthrough/figure about 5 minutes; R3 walkthrough/procedure/results about 5; compare contexts and transition in the remaining time. Read only the highlighted rows/axes, not every coefficient or statistic.
- Protect all later blocks. If behind, trim lecture elaboration/reference discussion, not break or project time. No new ClassPoint question: count stays zero.

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

## Implementation and review gates before teaching

- Reconcile additional instructor-supplied slides and the final Week 8 work.
- Verify any contemporary product claim or legal statement from a current primary source. No current legal advice is supplied by this plan.
- Confirm actual project stage, current Canvas milestones and demo accessibility.
- Current source: `deck/week09.py`; deterministic demo: `deck/week09_demo.py`. Native notes companion: [week09-speaker-notes.md](week09-speaker-notes.md); primary-claim/access/version ledger and offline cards: [week09-evidence-ledger.md](week09-evidence-ledger.md); truthful build/QA record: [week09-verification.md](week09-verification.md). Target-week builds do not establish a full-course site build or deployment.
- No ClassPoint collection is added. Slide 12 and closing comparisons are spoken reflections; activities remain existing private team notes. The report-attachment hook is retained and safely no-ops until a legitimate mapping exists; a stale nonempty mapping is rejected.
- Ranking demo is complete and native/static: all four invented items, two formulas and both result lists are visible. Optional local Python runs identical arithmetic; no browser sketch, service, new account or model is required.
- All substantive claim boundaries are visible near their findings, with methods/transfer/access detail in native notes and the evidence ledger. Instructor must still check classroom readability, links/network and any actual ClassPoint add-in use separately.
- Preserve the published assessment requirements unless explicitly revised; do not publish student work or private records.

## Existing syllabus milestone to reconcile

The current syllabus lists a Week 9 concept board and bias register. This revised sequence does not cancel or reschedule those existing milestones; reconcile their scope and actual Canvas instructions before teaching.

## Selected research refresh: recommendations and feedback loops

Both contemporary studies receive a short standalone summary and actual figure explanation in class. Neither is compulsory pre-reading. Other bibliography-only entries remain non-assigned background.

- Gauthier, Hodler, Widmer & Zhuravskaya (2026), **The political effects of X’s feed algorithm**, Nature: https://doi.org/10.1038/s41586-026-10098-2 . A randomized seven-week US X experiment conducted in 2023 found that activating the algorithmic feed shifted some policy attitudes and follow choices; switching it off was not symmetric. It found no significant effect on self-reported partisanship or affective polarization. The platform/time-specific setting and largely self-reported compliance limit transfer. Do not summarize this as “all algorithms radicalize.” Discussion: if recommendations change whom I follow, what should “reset recommendations” reset? Proposed design exercise: distinguish feed mode, history and following controls, then choose an outcome beyond engagement.
- Glickman & Sharot (online 2024; 2025 issue), **How human–AI feedback loops alter human perceptual, emotional and social judgements**, Nature Human Behaviour: https://doi.org/10.1038/s41562-024-02077-2 . Controlled experiments show that biased AI can amplify subsequent human bias, while accurate AI can improve judgement. This supports a feedback-loop mechanism, not a real-world recommender effect size. Discussion: when does a recommendation stop reflecting preference and start teaching it? Map choice → data → recommendation → changed judgement and identify a test point.

Use these at slides 24–28, then carry their limitations into the platform-redesign exercise. Proposed controls are design hypotheses, not proven remedies. The historical audit/documentation papers now have short summaries and source images within 35–60, not an extra lecture block.
