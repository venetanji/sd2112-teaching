# SD2112 / Week 12 lesson plan

**Ethics II: calibrated reliance, accessible privacy, delegation and accountability** / draft for instructor review / 22 October 2026

## Status and continuity

Actual source: `deck/week12.py`, with authentic paper excerpts plus original editable native diagrams in `deck/week12_figures.py`. There are **42 slides: 37 in the timed route and five reference slides**. Native speaker notes are reproduced in `lessons/week12-speaker-notes.md`. The primary-text claim/version ledger is `lessons/week12-evidence-ledger.md`; build and inspection evidence is in `lessons/week12-verification.md`. This is an uncommitted reconciliation for instructor review. Parent owns authorized public repository/Cloudflare branch-preview updates; no main release or assessment change is authorized here.

Week 11's evidence/curation audit becomes a question about what a product invites people to rely on. Week 5/8 mediation remains the vocabulary, but Week 8's full empathy/sycophancy lecture is not repeated. Machine A, Machine B and the harness are recalled only to locate consequential choices and permission. Non-chatbot products, services, recommenders, classifiers, objects and installations are valid throughout.

Learning goals:

- Distinguish an answer, a tool proposal and a consequential action.
- Evaluate advice using task performance, not trust or confidence alone.
- Explain accessibility/privacy trade-offs without treating interview preferences as tested protection.
- Name affected people, competing values, a contestation route and an accountable role.
- Improve existing project communication using a bounded peer walkthrough and formative review.

The visible ethical argument is not a checklist that certifies safety: independence and access can conflict with privacy and reliability; non-users can bear consequences; delegation does not remove the deploying organization's responsibility to investigate and repair. Teams must justify their own trade-offs and acknowledge untested assumptions.

## Exactly three hours

| Relative minutes | Duration | Segment | Actual slides |
|---|---|---|---|
| 0-10 | 10 | Reconnect | 1-3 |
| 10-40 | 30 | 01 / What are we delegating? | 4-13 |
| 40-65 | 25 | 02 / What may people rely on? | 14-22 |
| 65-75 | 10 | 03 / Turn evidence into a revision | 23-26 |
| 75-90 | 15 | Break | 27-27 |
| 90-120 | 30 | Interface walkthrough | 28-30 |
| 120-155 | 35 | Mock review | 31-34 |
| 155-175 | 20 | Revision | 35-36 |
| 175-180 | 5 | Close | 37-37 |

Total: **180 minutes**. Slides 38-42 are a reference shelf, not additional lecture time. If late, reduce spoken lecture detail; protect the 15-minute break, 30-minute interface walkthrough, 35-minute mock review and 20-minute revision. Slides within a workshop block are reference screens within the same timer, not separate timed activities.

## Actual slide map

<!-- slide-map:start -->

| Slide | Actual title | Block |
|---|---|---|
| 1 | Trust is not / the target. | 0-10 |
| 2 | Evidence -> boundary -> revision. | 0-10 |
| 3 | What should a person NOT delegate to your product? | 0-10 |
| 4 | What are we / delegating? | 10-40 |
| 5 | "Find an available workshop slot." | 10-40 |
| 6 | A sentence can become a commitment. | 10-40 |
| 7 | How does a tool result change the next step? | 10-40 |
| 8 | An observation can change the next step. | 10-40 |
| 9 | A tool result becomes the next input. | 10-40 |
| 10 | Make permission specific. | 10-40 |
| 11 | Easy to use. Hard to see through. | 10-40 |
| 12 | A better prompt is not the whole design. | 10-40 |
| 13 | Delegation does not erase responsibility. | 10-40 |
| 14 | What may people / rely on? | 40-65 |
| 15 | Can people reject incorrect advice? | 40-65 |
| 16 | An explanation did not fix wrong advice here. | 40-65 |
| 17 | Test rejection of an error - not trust alone. | 40-65 |
| 18 | How do people manage visual privacy? | 40-65 |
| 19 | Private from a helper. Exposed to whom? | 40-65 |
| 20 | Privacy controls must be usable before sharing. | 40-65 |
| 21 | Design the moment it should stop. | 40-65 |
| 22 | Name the trade-off - and who can contest it. | 40-65 |
| 23 | What will you / change? | 65-75 |
| 24 | Same promise. A different contract. | 65-75 |
| 25 | Review the project you already owe. | 65-75 |
| 26 | Can the work speak without an oral rescue? | 65-75 |
| 27 | Break. / Fifteen minutes. | 75-90 |
| 28 | Walk through three low-risk situations. | 90-120 |
| 29 | Show the next action. Do not explain it away. | 90-120 |
| 30 | One observation. One bounded revision. | 90-120 |
| 31 | Paired review. Then swap roles. | 120-155 |
| 32 | Read the poster before the pitch. | 120-155 |
| 33 | Who benefits? Who can challenge it? | 120-155 |
| 34 | Does the same product appear in all three? | 120-155 |
| 35 | Choose the change that matters most. | 155-175 |
| 36 | A stronger claim can be a narrower claim. | 155-175 |
| 37 | What will you change - and who can contest the result? | 175-180 |
| 38 | Cecil et al. / evidence card | Reference shelf |
| 39 | Sharma et al. / evidence card | Reference shelf |
| 40 | What should a model report make inspectable? | Reference shelf |
| 41 | Make the scope inspectable. | Reference shelf |
| 42 | Carry forward the question - not old logistics. | Reference shelf |

<!-- slide-map:end -->

## Reflective question / report map

| Actual slide | Exact question | Native type | Classroom alternative |
|---|---|---|---|
| 3 | What should a person NOT delegate to your product? | short_answer | Oral discussion or private team notes |
| 37 | What will you change - and who can contest the result? | short_answer | Oral share or private team notes |

These are brief formative discussions, not new assessed uploads. Two optional ClassPoint short answers are emitted; activity slides 28/31/35 do not collect artifacts. Default settings are named, single response; do not promise anonymity. Check actual classroom add-in/privacy settings before use. `attach_reports(S, ... / 'week12-reports.json')` runs before `finalize`; a missing/empty map is a safe pre-class no-op. Do not create fictitious live activity IDs. Later public answer links must withhold anonymous/private activities under the existing course policy.

## Activity A / interface walkthrough / 30 minutes

Relative 90-120. Use the team's actual concept without requiring a chat interface. For an installation, examine the operator controls and feedback; for a recommender, examine labels, evidence and overrides.

1. **0-5:** choose ordinary, ambiguous and out-of-scope situations with fictional, low-risk data.
2. **5-20:** reviewer walks through paper/static screens; a teammate plays the system; an observer records visible choices and confusion. Combine roles if needed.
3. **20-25:** separate observation from interpretation. What evidence was inspected? Could the reviewer refuse, correct or recover?
4. **25-30:** revise one claim, control or fallback; state what remains untested.

Label all scripted/manual model behavior **SIMULATION**. If a local prototype is available, distinguish actual output from manual intervention and restrict it to fictional data/read-only operations. No third-party action, account creation, subscription, cloud upload, booking, payment or private personal input. Paper cards/static screens are a complete workflow. Do not simulate disability; accessibility evaluation needs appropriate affected participants and consent, not blindfolded sighted peers. A classroom peer walkthrough is not safety, access or usability validation.

Prepared no-network example: fictional Room C has eight seats; twelve people need a room; a card explicitly labelled SIMULATION incorrectly recommends Room C. A reviewer checks the visible rule, rejects or questions the advice, and explains what evidence they used. This is not a replication of the personnel-selection experiments and not a measurement of general trust.

## Activity B / mock review / 35 minutes

Relative 120-155. Available draft posters/concept boards/readable layouts suffice for feedback; printing is not compulsory. Use an existing video or a storyboard/static frames and acknowledge that playback/pacing/audio remain untested when appropriate.

- **0-3:** pair teams and open readable materials; adapt a local cluster for odd team counts/access needs without inventing a fixed four-group rotation.
- **3-15:** Team A reviews Team B: three minutes silent/accessible poster inspection; four minutes evidence and ethics; five minutes video/storyboard, brief and clarification.
- **15-27:** swap roles using the same twelve-minute structure.
- **27-35:** synthesize one strength, one specific revision and one unresolved question for each team.

Review questions: What product is it, for whom, and what does AI decide? What is built versus simulated? Which source supports its claim and what are the task/population/outcome limits? Who benefits, who bears failure, which values conflict, who can contest it and who remains answerable? Does the proposed response address a real risk, and what could show it fails? Do poster, video and mediation brief describe the same relation, data, bias and guardrails?

Feedback stays in private team working notes. No student names, draft work, grades or responses enter this public repository. Do not promise a mark or create a new rubric/submission. More pairings are optional only if genuine spare time/room exists; do not displace revision.

## Activity C / revision / 20 minutes

Relative 155-175: five minutes compare notes, ten minutes make one essential correction, five minutes identify a remaining evidence gap and communication improvement. Prefer correcting misleading claims or consequential boundaries before decorative polish. Assign a team action owner in working notes if useful. Narrow a claim only when the narrower version is actually supported; do not fabricate a citation or user test. No new deadline, grade or upload.

## Selected evidence and reading load

This is a synthesis/reflection week, not a new four-paper lecture. Cecil and Sharma are the two empirical teaching lenses; ReAct is a mechanism recap; Model Cards is an optional documentation reminder on the reference shelf. Each taught source has a task/analysis screen before its finding/figure screen: task, comparison, concrete labelled example, and measurement or analytical basis. No pre-reading is required. ReAct is a mechanism example, not a safety result; Model Cards is a documentation proposal, not an evaluated safeguard. The existing prepared excerpt/background reading load is unchanged; no additional compulsory reading is imposed. Three topic signposts are inside the original budgets, not extra timed material. Authentic source excerpts are on slides 8, 16, 19 and 41; our diagrams on slides 9 and 20 remain explicitly illustrative. Sharma v2 has no figures, so two explicitly labelled Table 1 column excerpts stand in for a figure that version does not contain. They are joined at original scale with a white gutter to preserve row alignment in mobile. Figure meanings are also stated in native text for mobile reading. Descriptive attributed links are visible on research slides and the reference shelf.

- [Cecil et al. (2024), Scientific Reports](https://doi.org/10.1038/s41598-024-60220-5): five controlled online experiments, fictional CV advice, 1,403 students/HRM employees. Wrong advice harmed trial-level accuracy; tested heatmaps/charts did not reliably reduce overreliance. Advice quality/confidence are distinct outcomes. Not universal evidence against explanations or a test of real hiring.
- [Sharma et al. (2025), ASSETS record](https://doi.org/10.1145/3663547.3746335); [consulted author preprint v2](https://arxiv.org/html/2507.00286v2): interviews with 21 US BLV GenAI users. Independence, helpers/providers and others' privacy; experiences/preferences, not tested control efficacy. Full author version read; final typeset text not compared.
- [Yao et al., ReAct, ICLR 2023 / v3](https://arxiv.org/abs/2210.03629v3): primary mechanism for interleaved reasoning/action/observation, not proof of safe delegation.
- [Mitchell et al., Model Cards, 2019 / v2](https://arxiv.org/abs/1810.03993v2): primary documentation framework, not a certificate or new required report.

The syllabus's Van Den Eede reading remains background; its full text was not newly retrieved, so the deck labels its transparency distinction as a working design distinction rather than attributing detailed claims to an unread text. ELIZA and contemporary incidents are not used. Optional Week 8 empathy/sycophancy sources are not retaught.

## Archive comparison and retained synthesis

The 2025 Week 12 PDF has **70 pages**. Positions 54-69 were extracted and rendered: language as interface, rules/data, designer as curator, authorship/ownership, then fair/research logistics. Positions 27 and 29 were separately rendered: page 27 is a thought/action/observation loop under an imprecise "Agent prompt" title; page 29 is diffusion, not agents. Original illustrative diagrams remain native elements, separately labelled from authentic paper excerpts or assertions of faithful internal cognition.

The editable OneDrive Week 12 deck has **71 slides**, including Ask Me Anything at 54; subsequent synthesis is shifted by one (PDF54 -> PPTX55). Retain the designer's curation/accountability question and process disclosure, not unverified Ihde language claims, universal "ultimate interface" predictions or legal ownership assertions. Do not carry over the 2025 exam date, four-group requirement, shared board link or upload date. Old PR #3 remains historical background, not tooling or operational authority; no logistics are copied from it.

## Existing assessment and instructor decisions

Keep the **A0 poster, 3-5 minute video and one-page mediation brief**, together **40% of the course**. Existing project rubric proportions are research/context 30%, ethical/sociological impact 30%, communication/poster 20%, video 10%, collaboration/process 10%. Mock feedback does not add assessment criteria or change those proportions.

The syllabus still lists final poster/video ready in Week 12. This mock review does not cancel that milestone or move its deadline: confirm actual Canvas instructions. The syllabus also still lists a 20% whole-course final quiz in Week 13, while the latest direction is showcase-first. **Instructor must reconcile that policy before any announcement. Neither announce a final-quiz format nor cancel it.** Midterm and 2025 quiz rules are not authority for this decision.

Before teaching, confirm actual team count, room/pairing, displays, accessibility requirements, local playback and facilitation roles without assuming named staff accepted tasks. Check ClassPoint add-in/report/privacy settings if used; oral/team-note alternatives remain complete. Confirm review material access and feedback privacy. No new room map, print requirement, visitor list, deadline, grade, submission platform or live-system capability is approved by this draft.
