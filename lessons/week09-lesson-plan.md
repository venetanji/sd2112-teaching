# SD2112 · Week 9 lesson plan

**Recommendations, bias and reflective use** · implemented local slide draft · October 30, 2026

## Status and source reconciliation

This draft follows the latest intended sequence: Week 8 humanizing AI, Week 9 recommendations/bias, Week 10 Double Diamond reframing/testing. It now has a 51-slide native Deckgen implementation for review, not a timetable announcement or a syllabus amendment. The class is Friday 30 October 2026, confirmed by Giovanni on 28 October 2026.

The earlier draft recorded published main at 54f38c7 with approved Weeks 1-8. This polish checkout starts from 6fe8c92; parent owns combined integration and PR updates. This is not a fresh check of published main. Old [PR #3](https://github.com/venetanji/sd2112-teaching/pull/3) contains an unmerged Week 9 bias/privacy deck and Week 10 recommendation deck. Reuse ideas selectively, not those weeks' obsolete tooling, assumed submissions, Blackboard deadlines or slide numbers.

The original 50-page 2025 Week 9 PDF has now been recovered and visually inspected. Historical slide pointers: Week 9 pages 23–37 cover recommendations, embeddings, filtering and echo chambers; pages 38–45 cover bias, labour and consequences; pages 47–49 propose platform redesign. Pages 40–41 are image-heavy facial-analysis/AJL material and belong in the bias discussion; the cited Gender Shades study audits binary gender classification, not face identification. Page 49 proposes a diversity slider and explore-new-spaces button. Update these historical examples with the research below rather than treating the old deck as immutable.

## Purpose

The feed looks personal, but each stage expresses choices about what to collect, retrieve, rank and show. A model is not a passive, neutral mirror of humanity: it transforms selected traces through representations and objectives, and its use can change what people notice and do. Students explain a mechanism, discuss harmful AI bias encountered through experience or a public documented case, examine one example and research ways to reduce or remove its harm. They submit two private, ungraded team text responses: first the example and possible project connection, then a researched mitigation proposal with evidence and a limitation. Personal disclosure is optional; reflective interface redesign is one possible response, not the required remedy.

Research → AI-product context → existing team project remains the teaching pattern. Week 8's papers and project-specific research remain part of an accumulating evidence base; today adds the recommendation/data layer rather than replacing it.

By the end, students can:

- Describe candidate selection, ranking, presentation and feedback as distinct stages.
- Compare content-based and collaborative filtering and identify a cold-start limitation.
- Explain an embedding as a representation whose similarity depends on its construction and metric, not an objective description of a person.
- Locate bias in collection, labels, objectives and feedback, including human labour and missing perspectives.
- Distinguish inductive assumptions, learned regularities and harmful social bias; a repeated pattern is not automatically an error or injustice.
- Relate Heidegger, Ihde and Verbeek to Van Den Eede's questions about transparency in use and the visibility of mediation's social context.
- Explain one harmful-bias example, distinguish evidence from hypothesis and connect it to the existing project if possible.
- Support a proposed mitigation with a credible source/link, relevant evidence, a transfer limitation and a check that could show it fails.

## Preparation and roles to allocate

The instructor should allocate these tasks; names in earlier plans do not establish current commitments.

- Technical support: preflight both ClassPoint short-answer activities and private-result handling; confirm hidden display names and single submission per team per stage. Keep private team notes as the fallback if the add-in is unavailable; do not invent another upload channel.
- Research support: prepare accessible copies/links for selected readings, with page pointers for claims. Use manual library access where appropriate; no automated gated access.
- Facilitation: help teams describe a harmful-bias example without identifying details, formulate a research question and check that the cited source actually supports the proposal. A public documented case is an equally valid alternative to personal experience.
- Instructor: retain the R1–R5 research walkthroughs and prepare the bounded mediation bridge; confirm current Canvas instructions, and prepare public or non-identifying examples for voluntary discussion; do not project collected individual responses.

Do not assume every team already has a prototype or has submitted a formal proposal. A sketch and a defined product decision are enough to enter the activity.

## Implemented pacing / finish by 13:20

Class ends at **13:20**, as confirmed by Giovanni on 30 October. Relative timings below total **160 minutes** and are planning allocations, not an inferred class start time. Work backwards from the hard finish: start activity 1 **no later than 12:25**, activity 2 **no later than 12:45**, complete the second submission by **13:05**, then close discussion/carry-forward by **13:20**. If ahead, retain the margin; do not stretch either twenty-minute activity. If behind, trim earlier lecture elaboration rather than run past 13:20. Optional 28 October news uses at most five minutes **inside** the opener, replacing elaboration. It does not consume the protected activity time. Six clear topic dividers take approximately ten seconds within their blocks, not extra minutes.

| Minutes | Segment | Actual slides |
|---|---|---|
| 0–10 | Orient: user goal, selected outputs and the next choice | 1–3 |
| 10–25 | Mechanisms: R1 walkthrough/architecture, filtering, representations | 4–12 |
| 25–45 | Bias: three meanings, proxies, R4 audit, R5 documentation | 13–23 |
| 45–60 | Mediation: selected traces, Heidegger/Ihde/Verbeek, Van Den Eede, reflective use | 24–28 |
| 60–75 | Feedback studies: R2 field experiment and R3 controlled task | 29–35 |
| 75–90 | Protected break | 36 |
| 90–105 | Invented caption example + research-to-proposal preparation | 37–38 |
| 105–125 | Harmful-bias example: 5 recall + 10 examine + 5 compose/submit | 39–41 |
| 125–145 | Mitigation proposal: 15 research + 5 synthesize/submit | 42–45 |
| 145–160 | Compare public/non-identifying examples, research and uncertainty | 46–47 |

## Actual slide map

### Visual teaching pass / 29 October, activity alignment / 30 October

The projected deck now uses diagrams, historical study images and short visual
instructions rather than prose-heavy cards. Detailed explanations remain in
speaker notes. The 30 October revision replaces slides 37–38 and adds the two
authorized in-class responses without changing the 51-slide count or protected break; the later timing correction sets two twenty-minute
blocks and a hard 13:20 finish, without changing assessment requirements.
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
37. **From an experience to a harmful-bias claim.**
38. **From a source to a mitigation proposal.**
39. **Find and question harmful bias.**
40. **Where have you encountered harmful AI bias?**
41. **What makes this an example of bias?**
42. **Research ways to reduce the harm.**
43. **How could this harmful bias be reduced or removed?**
44. **Who might this revision miss?**
45. **How would you check whether it helps?**
46. **From harmful bias to a researched response.**
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
- 90–105: invented automatic-caption example 7 minutes; research-to-proposal preparation 8. Distinguish a hypothetical accent-related error and harm from a measured disparity; show how a credible source can support a bounded proposal. Testing across accents and editable captions are proposals, not proven fixes. This replaces the ranking-arithmetic demo, not an extra block.
- 105–125: recall examples 5 minutes; examine one and its possible project connection 10; compose and submit the first team text response 5. Include the divider inside this allocation. Personal disclosure is optional; a public case is welcome.
- 125–145: research credible sources 15 minutes; synthesize the proposal, evidence, limitation and check, then submit the second team text response within the final 5. Include the divider inside this allocation; no separate redesign/test timer or compulsory interface sketch.
- 145–160: voluntary spoken comparison of public/non-identifying examples 10 minutes, carry-forward/open question 5. Do not project individual responses; use the invented caption example if nobody volunteers. No fairness winner, third submission or new pitch deliverable.
- Protect the full break and both twenty-minute blocks. If behind, trim lecture elaboration/reference discussion, not activity time. Exactly two ClassPoint short-answer activities, at slides 40 and 43, replace the earlier zero-collection plan.

## Activity: harmful-bias experience, then researched mitigation

### 1. Explain one harmful-bias example, 20 minutes

Work in existing project teams: **5 minutes recall, 10 examine, 5 compose and submit**. Discuss harmful AI bias encountered in use, observation or research, then choose one example to explain. Personal disclosure is optional: a public documented case is equally welcome, with no explanation for choosing it required. Relate the example to the project if possible; do not force a feed or captioning feature into a project that has none. There is no required count of two examples, prototype, paid account, live generation or new paper quota.

The first team text response should include:

- Example and task: what happened, and compared with what?
- Affected people and harm: who was disadvantaged, excluded or misrepresented, and why might this be harmful bias rather than an isolated error?
- Evidence or uncertainty: distinguish a documented finding, an observation and a hypothesis. Retain a source/link and relevant passage where available; do not infer a training corpus or designer intention from an output alone.
- Project connection, if possible: where could this matter to the team's product or decision?

Use no names, identifying details, private transcripts, classmates' faces, account histories or sensitive attributes. Do not run harmful prompts or upload private assets. An exploratory matched comparison is not a population audit, and a suspected risk can remain a hypothesis rather than a manufactured disparity. If access fails, use the prepared Gender Shades table or permitted course example, explicitly labelled historical evidence or instructor illustration.

One nominated team member submits one short-answer text on slide 40. Responses may identify participants to the teaching team; hidden display names are **not anonymity**. Keep individual results off projection and use only non-identifying themes after instructor review.

### 2. Research ways to reduce or remove the harm, 20 minutes

Use the same chosen example: **15 minutes research, 5 minutes synthesis and submission**. Find relevant research or an authoritative documented intervention; read the actual method, population, comparator and result rather than relying on a headline, abstract or AI summary. Existing Week 8 research and the taught papers can be starting points, with their transfer limits explicit.

Consider data collection or labels, evaluation coverage, objectives or model changes, interface/recourse, human or organizational review, or not using AI for the decision. A reflective interaction revision is an option, not a compulsory interface-only redesign. There is no requirement to retrain, build a prototype or run a full audit.

The second team text response should include:

- Proposal: what could reduce or remove the selected harm, and why does it fit this case?
- Credible source/link and relevant evidence: what does the source actually support?
- Limitation: what remains uncertain, or differs between the source and this project?
- Check: a safe comparator, observable outcome and failure condition that could show the proposal does not help.

Separate awareness, ability to act, task success and unequal burdens. Documentation, a warning or a usable control alone does not prove reduced harm; do not claim proven efficacy or removal where the evidence supports only a proposal. Gender Shades transfers an audit question, not a facial-classification result or validated remedy for speech. The invented caption example's broader evaluation coverage and editable captions remain untested proposals. If search fails, use prepared course evidence and state the gap rather than fabricate findings.

One nominated member submits one short-answer text on slide 43, distinct from the first response. Exclude identifying details from the first example. Retain the source, proposal, limitation and check in existing private team notes for subsequent project work.

### 3. Spoken comparison, 15 minutes

Invite two teams to discuss public or non-identifying examples they choose to share: harm and evidence, researched proposal, remaining uncertainty. Do not project the collected experience list or identify its contributors. If nobody volunteers, use the invented caption example and prepared historical audit as distinct evidence types. No fairness winner, third response or new pitch is required.

Heidegger, Ihde, Verbeek and Van Den Eede remain resources for analysing perception, action and social context, not evidence that reflection or transparency guarantees fairness. Responsibility does not move to the person harmed because a warning or control exists.

## ClassPoint map and privacy contract

| Slide | Exact question | Collection |
|---|---|---|
| 40 | Where have you encountered harmful AI bias? | Short answer; `hide_names=True`; `multiple=False`; one team text at the end of phase 1 |
| 43 | How could this harmful bias be reduced or removed? | Short answer; `hide_names=True`; `multiple=False`; one team text at the end of phase 2 |

These are the two **ungraded in-class responses authorized on 30 October**, not a new Canvas upload, assessment weight, homework task or deadline. One nominated member submits per team per stage, not one response from every student. Names are hidden on display only; responses may still identify participants to the teaching team. Keep individual responses off projection. Do not publish either activity URL, response content, export or screenshot. Both collections are private, including the linked research response.

Preflight the actual add-in controls before collection. If unavailable, retain private team notes without inventing another submission channel. Withhold both report links and sanitize the actual report JSON and `ANSWERS.md` before publication as specified in the implementation gates; rendering without links is insufficient.

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
- Confirm actual project stage and current Canvas milestones separately from the two authorized in-class responses; check research-source accessibility and the private-notes fallback.
- Current sources: `deck/week09.py` and `deck/week09_visual_activities.py`. The retained `deck/week09_demo.py` is archival arithmetic provenance, not projected or required in the current lesson. Native notes companion: [week09-speaker-notes.md](week09-speaker-notes.md); primary-claim/access/version ledger and offline cards: [week09-evidence-ledger.md](week09-evidence-ledger.md); truthful build/QA record: [week09-verification.md](week09-verification.md). Target-week builds do not establish a full-course site build or deployment.
- Verify exactly two short-answer activities at slides 40/43, both with `hide_names=True` and `multiple=False`, and one nominated submitter per team per stage. Check native add-in operation and privacy controls before collection; hidden display names do not establish anonymity. The explanation check and closing comparison remain spoken, not additional collections.
- Withhold both public report URLs. The source masks report activities before attachment, but this does not sanitize stored data: before any publication, sanitize the actual `deck/week09-reports.json` with `activity: null` and an explicit withholding reason for both exact questions, and remove both URLs from `ANSWERS.md`. Keep positional placeholders if an activity was not run; never shift the second entry. Keep responses, exports and screenshots private and out of public sources/artifacts; review the actual files, not just the rendered deck.
- Slides 37–38 prepare the two responses using an explicitly invented caption example and bounded research proposal. They do not demonstrate measured accent disparities or proven mitigation; no new research-source read or efficacy claim is created by this documentation alignment.
- All substantive claim boundaries are visible near their findings, with methods/transfer/access detail in native notes and the evidence ledger. Instructor must still check classroom readability, links/network and any actual ClassPoint add-in use separately.
- Preserve the published assessment requirements unless explicitly revised; do not publish student work or private records.

## Existing syllabus milestone to reconcile

The current syllabus lists a Week 9 concept board and bias register. This revised sequence does not cancel or reschedule those existing milestones; reconcile their scope and actual Canvas instructions before teaching.

## Selected research refresh: recommendations and feedback loops

Both contemporary studies receive a short standalone summary and actual figure explanation in class. Neither is compulsory pre-reading. Other bibliography-only entries remain non-assigned background.

- Gauthier, Hodler, Widmer & Zhuravskaya (2026), **The political effects of X’s feed algorithm**, Nature: https://doi.org/10.1038/s41586-026-10098-2 . A randomized seven-week US X experiment conducted in 2023 found that activating the algorithmic feed shifted some policy attitudes and follow choices; switching it off was not symmetric. It found no significant effect on self-reported partisanship or affective polarization. The platform/time-specific setting and largely self-reported compliance limit transfer. Do not summarize this as “all algorithms radicalize.” Discussion: if recommendations change whom I follow, what should “reset recommendations” reset? Proposed design exercise: distinguish feed mode, history and following controls, then choose an outcome beyond engagement.
- Glickman & Sharot (online 2024; 2025 issue), **How human–AI feedback loops alter human perceptual, emotional and social judgements**, Nature Human Behaviour: https://doi.org/10.1038/s41562-024-02077-2 . Controlled experiments show that biased AI can amplify subsequent human bias, while accurate AI can improve judgement. This supports a feedback-loop mechanism, not a real-world recommender effect size. Discussion: when does a recommendation stop reflecting preference and start teaching it? Map choice → data → recommendation → changed judgement and identify a test point.

Teach these through **Can changing a feed change people?** to **Learning can go in either direction.** within 60–75, then carry their limitations into the harmful-bias example and researched-mitigation responses. Proposed controls are design hypotheses, not proven remedies. The historical audit/documentation papers retain walkthroughs and source images within 25–45, not an extra lecture block.

The mediation bridge adds Mitchell (1980), **The Need for Biases in Learning Generalizations**, and Van Den Eede (2011; online 2010), **In Between Us: On the Transparency and Opacity of Technological Mediation**, alongside Verbeek (2015). See the evidence ledger for precise source/read scope and the non-assigned **Read the distinctions in context.** shelf. Heidegger and Ihde originals were not newly read; their recall is checked through the mediation articles. No new compulsory reading is created.
