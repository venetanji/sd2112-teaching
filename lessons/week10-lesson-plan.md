# SD2112 · Week 10 lesson plan

**Reframe, prototype, test: the Double Diamond with evidence** · implemented slide draft · October 21, 2026

## Status and intent

Giovanni has explicitly confirmed he is absent in Week 10. The session is to be interactive, centered on Double Diamond reframing, prototyping and testing, rather than a substitute lecture. The earlier discussion places it on November 6; the dated timetable still needs confirmation. This is a proposed facilitation plan for review, not a confirmed staff rota or dated timetable. Coverage and the school's 15-minute ESFQ arrangement remain unconfirmed. Do not contact or assign colleagues through this document.

The current syllabus's Week 10 recommendation topic is being considered earlier, in Week 9. This draft preserves that intended sequence without modifying the syllabus, existing project milestones or assessments. The unmerged [whole-course PR #3](https://github.com/venetanji/sd2112-teaching/pull/3) does not implement this new workshop: its Week 10 is a recommendation lecture. Week 8 work in [PR #21](https://github.com/venetanji/sd2112-teaching/pull/21) stays separate and untouched.

## Purpose

Turn the evidence accumulated in Weeks 8–9 into a better-framed product question and a small test. The goal is not to make every team polish an assumed existing prototype. Teams can enter with a concept, a sketch or a working interaction and choose a suitable test of the riskiest assumption.

Students should leave able to explain:

- What evidence changed their understanding of the problem.
- What remains an assumption, and whose perspective is missing.
- Why the chosen prototype is sufficient for a particular test.
- What they observed, what it does not establish, and what to change next.

## Source spine

- Design Council, **The Double Diamond**: https://www.designcouncil.org.uk/resources/the-double-diamond/ . Discover, Define, Develop and Deliver frame the work. The official diagram is CC BY 4.0; preserve attribution if reused. Use iteration, not a rigid linear checklist.
- Sözen & Börekçi (2026), **Analyzing the integration of generative AI in the design process through the double-diamond framework**: https://doi.org/10.1017/S0890060426100304 . Discuss the specific study after reading its methods; the paper and the framework are different kinds of source.
- Verbeek (2015), **Beyond Interaction**: https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf . Keep the relationship and consequences in view while changing the interface.
- Each team's research from Weeks 8–9: relevant passages and limitations, not merely a bibliography. The Week 8 register retains cognitive-surrender, sycophancy, beneficial-use and transparency studies; use only those that fit the team's product.

Historical source pointers: last year's Week 8 pages 27–29 introduced Double Diamond. Last year's Week 10 had recap material and a guest slide; that is not evidence of a newly booked guest. The original 19-page 2025 Week 10 PDF has now been recovered and visually inspected: page 5 is a Scrum/Git/Docker title, pages 6–16 recap recommendations/bias, and page 18 introduces Ball Cheung. This is not evidence of a full technical lecture or a current guest booking.

## Before class: allocate and confirm

- Confirm who facilitates, who supports teams, and who handles timing and equipment. No named person's acceptance is presumed.
- Confirm the ESFQ visit and where its 15 minutes fall. The school handles it; do not invent special assessment or survey materials.
- Ask teams to have their existing concept and research notes available through the already approved class channel. Do not create a new deadline here.
- Prepare paper, pens and a simple test-note template. Digital tools are optional. No new AI account, model subscription or working code is required.
- Choose an ordinary low-risk demonstration, such as comparing two ways to explain a recommendation. Do not simulate diagnosis, make real purchases or expose personal data.

## Proposed three-hour allocation

The 15-minute ESFQ slot is reserved provisionally; its placement below is not confirmed. If it moves, move it rather than shortening it. If it does not occur, use the reserved time for revision and facilitator feedback.

| Minutes | Segment | Actual slides |
|---|---|---|
| 0-15 | Provisional school ESFQ reserve | 1 |
| 15-30 | Framing | 2-6 |
| 30-55 | Reframe | 7-10 |
| 55-75 | Develop | 11-13 |
| 75-90 | Break | 14 |
| 90-115 | Prototype | 15-17 |
| 115-145 | Test | 18-20 |
| 145-165 | Revise | 21-22 |
| 165-180 | Share | 23-24 |

## Actual native slide map

The deck has 25 slides: 24 in the timed run (including the holding slide) and one untimed reference shelf. Each activity timer covers its following support slides, not additional time.

| Slide | Actual title |
|---|---|
| 1 | School ESFQ: if confirmed. |
| 2 | Reframe. Prototype. Test. |
| 3 | Start where your project is. |
| 4 | A plausible idea is not a finding. |
| 5 | Two diamonds. Four kinds of work. |
| 6 | AI can enter more than one phase. |
| 7 | Reopen the problem, not just the file. |
| 8 | Read the passage again. |
| 9 | Change the question. |
| 10 | Keep the disagreement. |
| 11 | Two responses. One uncertainty. |
| 12 | Test the decision, not the decoration. |
| 13 | Decide what would change your mind. |
| 14 | Break. 15 minutes. |
| 15 | Build only enough to learn. |
| 16 | Three cards are enough. |
| 17 | Can the person say no? |
| 18 | Give the task. Then watch. |
| 19 | Do not teach the answer. |
| 20 | Observation is not interpretation. |
| 21 | Change one consequential decision. |
| 22 | Who still needs to be heard? |
| 23 | One changed decision. Its evidence. |
| 24 | Keep the learning, not just the screen. |
| 25 | Framework. Study. Mediation. |

## Materials and collection contract

- `deck/week10.py` is the native source; `deck/week10_figures.py` draws the attributed framework adaptation.
- Detailed facilitation script: `lessons/week10-speaker-notes.md`, generated from the actual native speaker notes.
- Claim/access ledger and prepared offline card: `lessons/week10-references.md`.
- Zero ClassPoint activities and no new upload. `attach_reports` is retained before finalization; a missing report file is a safe no-op. No fabricated reports are created.
- Three-card paper/manual fallback is on slide 16; all AI responses are visibly simulated. Voluntary peer test protocol is on slides 18-20.
- Local build/QA evidence and unresolved delivery checks: `lessons/week10-verification.md`.

## Detailed team protocol

### Reframe, 25 minutes

Read the project's research notes. Separate evidence about the intended users from evidence about a different population or product. Mark one unsupported assumption. Write: “For [person in context], the problem is [need], not simply [feature we wanted to build].” Record the strongest counterargument to the team's initial framing.

### Choose alternatives and a test, 20 minutes

Draw two possible responses, including a non-AI or lower-autonomy option where relevant. Choose a single uncertainty to investigate. Specify the task and observable behaviour before building. Do not use satisfaction alone as proof that a decision is correct, safe or effective.

### Prototype, 25 minutes

Build only enough to expose the uncertainty. A paper sequence can test comprehension; a manually supplied example can test a choice. Label any Wizard-of-Oz/simulated AI behaviour and do not imply model performance was measured. A team with existing code should avoid broad new features during the time box.

### Test, 30 minutes

Exchange with another team if appropriate. Explain the activity and allow anyone to decline. Use synthetic scenarios, not sensitive personal stories. Give the task without coaching a preferred answer; observe where the participant hesitates, misunderstands or loses control. The facilitator should stop unsafe or intrusive scenarios. Notes must distinguish direct observation from the team's inference.

### Revise and share, 35 minutes

Change one design decision, retain one finding that did not support the team's expectations, and state the next uncertainty. An inconclusive result is useful if it improves the next test. Keep a short before/after sketch and evidence note in the existing project workspace; this is not a new graded submission.

## Facilitation prompts and contingencies

- “What evidence makes you say that?”
- “Could a simpler prototype answer the same question?”
- “What result would make you change your mind?”
- “Did you test the model or the interface, and how do you know?”
- If access fails, switch to paper. Do not spend the workshop installing tools.
- If the project is underdeveloped, test the problem framing or comprehension, not a fictional finished system.
- If a test needs clinical, legal or other high-stakes validation, record that need and use an ordinary low-risk classroom question instead. This workshop does not confer such validation.

## Review gates

Confirm the actual calendar, coverage, ESFQ slot and team starting points. Reconcile new instructor-supplied materials. Preserve the existing assessment brief and deadlines. The authorized implementation pass now provides a 25-slide native deck, synchronized notes and local builds. This remains an uncommitted local draft, not a deployment or accepted facilitation rota. See `week10-verification.md` for actual checks and remaining classroom verification. Keep student records and test notes out of the public repository.

## Existing syllabus milestone to reconcile

The current syllabus lists prototype v1 in Week 10. Allowing different starting fidelities in this workshop does not cancel that existing milestone or move its deadline; reconcile the workshop outcome and actual Canvas instructions with the instructor.
