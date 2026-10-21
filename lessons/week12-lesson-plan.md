# SD2112 · Week 12 lesson plan

**Language interfaces, calibrated trust and the mock poster review** · planning draft · October 21, 2026

## Status and continuity

This plan preserves the current syllabus's language-interface/trust focus and the discussed mock-poster preparation. It builds on Week 8 humanizing AI, Week 9 recommendation/bias decisions, Week 10 reframing/tests and Week 11 research/curation. It should not repeat the whole Week 8 empathy/sycophancy lecture.

No finished Week 12 deck exists on current main. The unmerged [PR #3](https://github.com/venetanji/sd2112-teaching/pull/3) contains an older deck/plan with useful mechanisms but unconfirmed Blackboard, printing and final-quiz instructions. Treat it as source material, not approved logistics. Week 8 PR #21 is separate active work and remains untouched.

Historical PDF pointers from the earlier review: Week 12 pages 46–49 revisit Yu et al.; 55–59 language interfaces; 60–63 curators/guardrails; 64–66 authorship/ownership; 67–69 poster preparation. Inspect originals and reconcile any new instructor materials before reuse.

## Purpose

Students should make their product's capabilities, limits and consequential actions legible. They then test whether another team can understand the product, evidence and trade-offs from its communication without an oral rescue.

Learning goals:

- Distinguish a rule-based response, generated response and tool-mediated action.
- Explain why fluent language or an explanation is not by itself proof of correctness.
- Identify what a person can inspect, correct, approve, refuse or undo.
- Use the existing rubric to improve the poster, video and mediation-brief story.
- State a prioritized final revision and an unresolved evidence gap honestly.

## Proposed three-hour run of show

| Minutes | Segment | Proposed slides |
|---|---|---|
| 0–10 | Current project question and evidence gap | 1–3 |
| 10–40 | Rules, generation and action | 4–9 |
| 40–65 | Trust, transparency and product boundaries | 10–15 |
| 65–75 | Worked example and mock-review brief | 16–18 |
| 75–90 | Break | 19 |
| 90–120 | Interface walkthrough/test on the team's product | 20–22 |
| 120–155 | Mock poster review in paired rotations | 23–25 |
| 155–175 | Revise and prioritize | 26–27 |
| 175–180 | Confirm next-step questions | 28 |

These are proposed timings. The rotation count depends on the actual team count and room. Do not announce a fixed room map, mock-review print format or visiting list before confirmation. The final poster remains A0 under the existing syllabus.

## Slide construction plan

1. Language interfaces and calibrated trust.
2. What did your evidence/curation audit change?
3. What must a person understand before relying on your product?
4. One request through explicit rules, generation and a hybrid.
5. ELIZA: inspect a written rule rather than anthropomorphizing its mechanism.
6. Generated responses: flexibility with uncertain correctness.
7. Agent loop: observe, decide, use a tool, inspect the result.
8. Answering versus acting: which step changes something for the person?
9. A clear boundary: read-only preview, confirmation, result and recovery.
10. Transparency of use versus visibility of origins/effects.
11. A convenient interface can hide consequential choices.
12. Explanation versus faithful evidence; a plausible rationale can mislead.
13. User control: inspect, correct, refuse, override and leave.
14. Uncertainty and escalation: what the product should not claim to handle.
15. Testing boundaries: ordinary, ambiguous and failure situations.
16. Worked comparison: same product promise, two different interface contracts.
17. Keep the user's goal visible, not just the model's response.
18. Mock review: use the actual project brief and rubric.
19. Break.
20. Teams select three low-risk scenarios for their own product.
21. Walk through the interface; label simulated model behaviour.
22. Revise one capability claim, control or fallback.
23. Mock review: explain the product from the poster before hearing its pitch.
24. Trace one product claim to the research and one risk to a design response.
25. Examine the video/brief connection and record feedback.
26. Prioritize revisions: essential correction, evidence gap, communication improvement.
27. State what remains uncertain; do not overclaim what a classroom test proves.
28. Final-event readiness questions and verified instructions only.

## Activity A: a language/interface contract, 30 minutes

Use the team's real concept; do not require every product to acquire a chatbot. For non-conversational products, examine the explanations, labels and controls around the AI decision.

1. Choose an ordinary request, an ambiguous request and a situation outside the intended scope. Avoid sensitive personal disclosures or unsafe tasks.
2. For each, show what the person sees, what the system is allowed to do and what happens when it cannot continue reliably.
3. Compare the response/decision with the promised capability. Label generated, simulated and manually scripted behaviour accurately.
4. Ask another person to explain the next action and available control. Record observed confusion separately from interpretation.
5. Change one interface element or promise. Keep the research rationale and test limitation beside it.

No live third-party action, account creation or new subscription is required. Paper response cards and static screens are a complete fallback. A friendly response, a disclaimer or a prompt alone does not establish safety.

## Activity B: mock poster review, 35 minutes

Use available draft posters, concept boards or readable digital layouts. Printed drafts can help but are not compulsory unless the instructor confirms this separately. Pair teams, then swap roles; add another pairing only if time and room allow.

Each reviewer records:

- What product is this, for whom, and what does the AI decide?
- Which source supports its central claim, and what limitation is acknowledged?
- What relationship, data dependency, bias or consequence matters?
- What control or guardrail addresses the concern, and what evidence is still missing?
- What is hard to understand from the poster/video/brief alone?

Reviewers give one strength and one specific revision. This is formative feedback, not a new grading scheme or promise of a particular mark. Do not collect student names or publish draft work without authorization.

## Reading and source register

- Weizenbaum (1966), **ELIZA—a computer program for the study of natural language communication between man and machine**: https://doi.org/10.1145/365153.365168 . Historical mechanism, not a current therapeutic product.
- Yao et al., **ReAct: Synergizing Reasoning and Acting in Language Models**: https://arxiv.org/abs/2210.03629 . Mechanism source for interleaving reasoning/action; not proof that any deployed agent acts safely.
- Van Den Eede (2011), **In Between Us: On the Transparency and Opacity of Technological Mediation**: https://doi.org/10.1007/s10699-010-9190-y . Theory anchor for the two senses of transparency.
- Turpin et al. (2023), **Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting**: https://arxiv.org/abs/2305.04388 . Use the tested context and distinction between rationale and faithful explanation; avoid claiming every explanation is false.
- Mitchell et al. (2019), **Model Cards for Model Reporting**: https://arxiv.org/abs/1810.03993 . Documentation questions about intended use and evaluation, not a certification of safety.
- Yu et al. (2025), **Exploring cognitive presence patterns in GenAI-integrated six-hat thinking technique scaffolded discussion**: https://doi.org/10.1186/s41239-025-00545-x . Optional continuity with Week 11, not a replacement for project-specific evidence.

Source reuse: [old Week 12 deck](https://github.com/venetanji/sd2112-teaching/blob/83733ca09969da3439c251260a45549a16f12e71/deck/week12.py). Verify any retained incident, model-performance figure or legal assertion against a current primary source. Do not carry forward its assumed final-quiz format or printing schedule.

## Before class and before final-event instructions

Allocate facilitation, technical preflight and feedback-recording responsibilities; do not assume named staff have accepted them. Confirm the actual team count, room layout, display access and accessibility needs. If ClassPoint is chosen, verify anonymity and export settings rather than promising them from the plan.

Use the current syllabus's project components: A0 poster, 3–5 minute video and one-page mediation brief, together worth 40% of the course. Final quiz is 20% on the whole course in Week 13. Confirm question count, duration, platform, permitted resources, accessibility/accommodations and contingency arrangements before writing operational slides. The midterm's 40-question/30-minute/open-book rules and the old PR's 30-question/35-minute rules are not authority for the final.

No assessment/deadline changes, deck rendering, live-system test, merge or deployment are part of this planning document. Keep public repository content limited to planning and sources, not student work or quiz answers.

## Existing syllabus milestone to reconcile

The current syllabus lists final poster and video ready in Week 12. This formative mock review does not cancel that existing milestone or move its deadline; confirm the actual Canvas instructions before teaching.
