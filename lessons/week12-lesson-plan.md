# SD2112 · Week 12 lesson plan

**Ethics II: agency, trust, accountability and the mock showcase review** · planning draft · October 21, 2026

## Status and continuity

The latest direction is for Weeks 11–12 to focus more on ethics and related issues. This Week 12 option uses language interfaces and agents as a concrete setting for agency, trust and accountability, then applies those questions to a mock showcase review. Historical slides may be updated or replaced and supplemented with more recent papers; they are not immutable. It builds on Week 8 humanizing AI, Week 9 recommendation/bias decisions, Week 10 reframing/tests and Week 11 research/curation. It should not repeat the whole Week 8 empathy/sycophancy lecture.

No finished Week 12 deck exists on current main. The unmerged [PR #3](https://github.com/venetanji/sd2112-teaching/pull/3) contains an older deck/plan with useful mechanisms but unconfirmed Blackboard, printing and final-quiz instructions. Treat it as source material, not approved logistics. Week 8 PR #21 is separate active work and remains untouched.

The original 70-page 2025 Week 12 PDF has now been recovered and visually inspected. Pages 8–53 broadly recap the course; pages 54–66 provide the distinctive closing synthesis on language interfaces, rules/data, curation and authorship/ownership; pages 67–69 concern the fair and research. Page 27 is a thought/action/observation loop, not a literal agent prompt template. Page 29 depicts a diffusion pipeline, not an autonomous agent. The old four-group feedback instruction and 2025 exam date on pages 4–5 must not silently become 2026 requirements.

## Purpose

Students should make their product's capabilities, limits and consequential actions legible. They then test whether another team can understand the product, evidence and trade-offs from its communication without an oral rescue.

Learning goals:

- Distinguish a rule-based response, generated response and tool-mediated action.
- Explain why fluent language or an explanation is not by itself proof of correctness.
- Identify what a person can inspect, correct, approve, refuse or undo.
- Use the existing rubric to improve the poster, video and mediation-brief story.
- State a prioritized final revision and an unresolved evidence gap honestly.

Additional ethics outcome: identify affected people and competing values, explain who can contest an outcome, and state who remains accountable when the product fails.

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

1. Ethics II: agency, trust and accountability.
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
12. Cecil et al.: do explanations improve error detection or merely persuade? Distinguish the tested advice task from universal claims.
13. Sharma et al.: independence from helpers versus privacy from providers; accessible inspect, redact, refuse and leave controls.
14. Uncertainty and escalation: what the product should not claim to handle.
15. Testing boundaries: ordinary, ambiguous and failure situations.
16. Worked comparison: same product promise, two different interface contracts.
17. Keep the user's goal visible, not just the model's response.
18. Mock review: use the actual project brief and rubric, including research and ethical/sociological impact.
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
- Who benefits or bears a failure, which values conflict, who can contest the result, and who remains answerable?
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

Use the current syllabus's project components: A0 poster, 3–5 minute video and one-page mediation brief, together worth 40% of the course. The published syllabus also lists a 20% whole-course final quiz in Week 13, but the latest direction is showcase-first. Reconcile that policy item explicitly before announcing any quiz or writing operational instructions. If retained, confirm question count, duration, platform, permitted resources, accessibility/accommodations and contingencies. The midterm's 40-question/30-minute/open-book rules and the old PR's 30-question/35-minute rules are not authority for the final.

No assessment/deadline changes, deck rendering, live-system test, merge or deployment are part of this planning document. Keep public repository content limited to planning and sources, not student work or quiz answers.

## Existing syllabus milestone to reconcile

The current syllabus lists final poster and video ready in Week 12. This formative mock review does not cancel that existing milestone or move its deadline; confirm the actual Canvas instructions before teaching.

## Ethics-led discussion options and recent evidence

Recommended question: **what may the product invite a person to trust or delegate, and who remains answerable?** Contrast beneficial support with over-reliance, manipulative affirmation and opaque action. Alternative focus: **what meaningful choice remains when the interface is effortless?** Use disclosure, refusal, correction and recovery as concrete design questions, not a universal checklist that proves safety.

Candidate recent readings already discussed for the course:

- Cheng et al. (2026), **Sycophantic AI decreases prosocial intentions and promotes dependence**, https://doi.org/10.1126/science.aec8352 . Use the final study version and measured outcomes; do not infer universal long-term effects. If covered in Week 8, revisit only the product-accountability implication.
- Maheshka, Folk & Dunn (2026), **Harnessing Artificial Intelligence to Facilitate Difficult Conversations**, https://doi.org/10.1177/19485506261444068 . A complementary example of support for real-world human interaction; not proof of better conversation quality or superiority to human preparation.
- Wenger, Cameron & Inzlicht (2026), **People choose to receive human empathy despite rating AI empathy higher**, https://doi.org/10.1038/s44271-025-00387-3 . Distinguish response rating, chosen relationship and clinical effectiveness.

Choose the strongest pair for the students' actual projects, avoid reteaching all Week 8 studies, and add fresher relevant research where it improves the question. The mock review should ask who gains, who can contest the result, who bears a failure and which claim lacks evidence. No source choice or ethical position is a newly assessed requirement.

## Selected research refresh: calibrated reliance and accessible privacy

Use these non-Week-8 examples as the preferred ethics pair; the empathy/sycophancy papers above remain optional continuity. Use one excerpt plus one background reading, not an additional mandatory reading load.

- Cecil, Lermer, Hudecek, Sauer & Gaube (2024), **Explainability does not mitigate the negative impact of incorrect AI advice in a personnel selection task**, Scientific Reports: https://doi.org/10.1038/s41598-024-60220-5 . Five preregistered experiments found that incorrect advice harmed performance; the tested heatmap/chart explanations did not reliably reduce overreliance. This does not mean all explanations are useless. Discussion: does an explanation help people catch errors, or merely persuade them? In a fictional low-stakes classroom scenario, test whether people reject deliberately wrong advice rather than measuring trust alone. Do not perform real personnel selection or infer employment decisions from student data.
- Sharma et al. (2025), **“Before, I Asked My Mom, Now I Ask ChatGPT”: Visual Privacy Management with Generative AI for Blind and Low-Vision People**, ASSETS: https://doi.org/10.1145/3663547.3746335 ; author preprint: https://arxiv.org/html/2507.00286v2 . Interviews with 21 blind and low-vision participants explore privacy/independence trade-offs and desired retention, redaction and accessibility controls. These are experiences and preferences, not tested safeguard efficacy. Discussion: can AI increase privacy from helpers while reducing privacy from providers? Sketch an accessible capture-review-share flow with nonvisual privacy feedback and attention to bystander data. Use fictional images/data rather than collecting private material.

Integrate at the explanation/control discussion and mock-review prompts, replacing generic examples rather than extending class time. Proposed controls and tests are teaching hypotheses, not validated remedies. Review who benefits, who can contest a result, who bears failure and what evidence is missing.
