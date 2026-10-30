"""Week 10: design a product with AI inside, through the Double Diamond."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import attach_reports, PAPER
from deckgen.layouts import title, content, two_col, activity, statement, figure_slide, finalize
from course import footer
import week10_figures as F

S = []
DC = 'https://www.designcouncil.org.uk/resources/the-double-diamond/'
PAPER_URL = 'https://doi.org/10.1017/S0890060426100304'
VERBEEK = 'https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf'
# Proposed relative times, not accepted speaker slots or a confirmed school visit.
BLOCKS = [
    (0, 15, 'Weeks 8-9 bridge and Double Diamond', 1, 7),
    (15, 60, 'Guest cases: Zhibin and four PhD researchers', 8, 8),
    (60, 70, 'Case discussion', 9, 9), (70, 85, 'Break', 10, 10),
    (85, 100, 'Four-phase project map', 11, 13),
    (100, 130, 'Develop and prototype', 14, 19),
    (130, 155, 'Voluntary peer walkthrough', 20, 22),
    (155, 165, 'Revise and share', 23, 25),
    (165, 180, 'Provisional school ESFQ reserve', 26, 26),
]

S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 10',
    'Design with\nAI inside.', 'The Double Diamond. Decisions, data and consequences.', size=126,
    notes='0-15 opening, slides 1-7 together. One minute here; two minutes each on the six following slides. The focus approved by Giovanni is designing a product or service with AI inside, not using AI to accelerate the designer\'s workflow. Giovanni is confirmed absent. Zhibin and four PhD researchers are intended contributors; their topics, individual allocations, speaking order, acceptance and facilitation roles remain to confirm. Relative timings are a proposal, not a confirmed rota. No new submission, deadline or grading criterion.'))
S.append(two_col('BRIDGE / WEEKS 8 AND 9', 'From material to design decisions.',
    ['WEEK 8 / AI AS DESIGN MATERIAL', 'What does the product decide for a person?',
     'How does it shape what they notice and do?', 'Who keeps judgment, control and responsibility?'],
    ['WEEK 9 / DATA, BIAS AND PRIVACY', 'What data makes that decision possible?',
     'Whose patterns and perspectives are represented?', 'What harm could follow, and how could we reduce it?'],
    right_font='body', left_size=34, right_size=34, lang=None,
    notes='Two minutes. Reconnect to Week 8\'s using-versus-incorporating distinction and mediation: the AI-enabled product shapes perception, action and relationships, not just output speed. Week 9 adds learned patterns versus harmful bias, data and privacy considerations. Not every learned distinction is a harmful bias; ask who is disadvantaged in this application, by which mechanism and consequence. Research-backed mitigation is a hypothesis to test in context, not a promise that harm can always be removed. Use existing project evidence and bias notes, not a new reading quota.'))
S.append(figure_slide('FRAMEWORK / OUR APPLICATION: PRODUCTS WITH AI INSIDE', 'Two diamonds. Four kinds of work.',
    F.source_image('design-council-double-diamond.png', 'Official Design Council Double Diamond: Discover, Define, Develop, Deliver'), bg=PAPER,
    body=['Discover and Define: understand the need; decide the role of AI.',
          'Develop and Deliver: explore interactions; test, improve and monitor. Return when evidence changes.'],
    caption=f'[Design Council: The Double Diamond]({DC}), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Official diagram, unchanged.',
    notes='Two minutes. The official Design Council framework distinguishes Discover, Define, Develop and Deliver; divergence opens possibilities and convergence focuses choices. The AI-product questions on the following slides are our teaching application, not claims that the Design Council prescribes this AI checklist. The official PNG is unchanged, with CC BY 4.0 attribution. This is a framework, not measured evidence of better outcomes. It is iterative: testing may reopen the problem. The older AI-as-design-tool study is optional context after the timed route, not the lesson\'s central evidence.'))
S.append(content('DISCOVER / NEED, CONTEXT, PEOPLE, DATA', 'Whose experience changes?', [
    'Understand the need before assuming AI is the answer.',
    'Ask what the product would make visible, easy or difficult.',
    'Find missing perspectives and evidence about affected people.',
    'Ask what data exists, who it represents and whether it may be used.',
], body_size=36,
    notes='Two minutes. Connect Week 8 mediation to Week 9 representation and privacy. A fictional cafe chooser is the running example, not a researched user need: a time-limited commuter might need comparison, not automated choice. Identify affected people beyond the primary user, including those ranked or excluded. A generated persona is not evidence from those people. Accessible data is not automatically accurate, representative or permitted for this purpose. Record unknowns rather than invent research; use saved source passages if offline.'))
S.append(content('DEFINE / AI ROLE, BOUNDARIES, EVIDENCE', 'What should the AI decide?', [
    'State the need and why AI belongs in the product.',
    'Separate the model output, the product rule and the human choice.',
    'Define useful outcomes, unacceptable harms and data limits.',
    'Choose the assumption whose failure would change the design.',
], body_size=36,
    notes='Two minutes. Make the AI\'s role explicit: ranking cafe options is different from automatically choosing or booking one. The model may estimate a match, a written product rule may filter opening hours, and the person may make the final choice. This reconnects Machine A/Machine B without adding a technical lecture. Compare a simpler or non-AI baseline to justify the AI role; that comparison does not remove the project requirement to incorporate AI. Success includes the intended user outcome and its distribution, not only engagement or a model score. Record harms and boundaries before testing.'))
S.append(content('DEVELOP / ALTERNATIVES, CONTROL, FAILURE', 'Design more than the happy path.', [
    'Compare interactions and levels of AI autonomy.',
    'Make uncertainty and the basis of a suggestion understandable.',
    'Design correction, rejection and recovery from a poor output.',
    'Minimise data; examine biased results and who bears the cost.',
], body_size=36,
    notes='Two minutes. Explore meaningfully different responses, not only different screen colours. For the fictional cafe product, compare an automatic first choice with an editable comparison card. Consider explanations that a person can use, missing evidence, inappropriate suggestions and a usable fallback. An override button is not a complete ethics solution: who notices the problem, does the correction work, and who must do extra labour? Data minimisation, representation and potential harm travel through the prototype, rather than waiting for an end-of-process ethics slide.'))
S.append(content('DELIVER / TEST, RECOVER, MONITOR, RETURN', 'Test the interaction and the AI.', [
    'A paper simulation tests the interface, not model reliability.',
    'Check useful outcomes and failures across relevant contexts.',
    'Plan recovery, responsibility and privacy-safe monitoring.',
    'New evidence may send you back to Discover or Define.',
], body_size=36,
    notes='Two minutes. Separate interface comprehension from actual model behaviour and longer-term product consequences. Future model evaluation needs relevant cases, baselines and attention to who benefits or fails; do not fabricate benchmarks from a classmate walkthrough. Discuss feedback, correction, rollback or a non-AI route, and who acts on a reported failure. Monitoring is a plan, not permission to collect personal data. Today\'s classroom task does not deploy a product, establish safety or authorize high-stakes validation. All four phases revisit data, bias and mediation.'))
S.append(content('GUEST CASES / PROPOSED 15-60 / TOPICS AND ORDER TO CONFIRM', 'Show the AI inside the product.', [
    'Intended contributors: Zhibin + four PhD researchers.',
    'Need -> AI role -> design decision -> evidence or failure.',
    'Connect each case to relevant Double Diamond phases.',
    'Listen for a decision you could reconsider in your own project.',
], body_size=36,
    notes='Proposed 45-minute collective case block, not five confirmed individual bookings. Zhibin and four PhD researchers are the instructor\'s intended contributors. Their names beyond Zhibin, titles, examples, demos, order, acceptance and individual minutes remain unconfirmed. Do not assign one speaker per phase. Brief them to show a product/service with AI inside: the need, the AI\'s function, data and human roles, choices through relevant phases, a failure or piece of evidence that changed the design, and an unresolved limitation. Tool-use examples alone are not the focus. No claims about speakers\' actual work are supplied here. Confirm allocations before class; do not silently consume workshop time.'))
S.append(content('CASE DISCUSSION / PROPOSED 60-70', 'Which decision would you question?', [
    'Which phase changed when the speaker found new evidence?',
    'What did the AI decide, and what remained with a person?',
    'Who might be poorly represented, excluded or exposed?',
    'Which lesson transfers to your project, and which may not?',
], body_size=36,
    notes='Ten minutes including speaker questions. Discuss specific cases actually presented, not invented study findings. Ask for the task, affected people, evidence and limits behind a claim. Bring Week 8 mediation and Week 9 harm/data reasoning into the same design decision. A speaker\'s successful example does not establish transfer to every team\'s users. If a case does not demonstrate AI incorporated in a product, explicitly distinguish it from today\'s product focus instead of changing the brief.'))
S.append(statement('Break.\n15 minutes.', eyebrow_text='PROPOSED 70-85 / RELATIVE CLASS TIME', size=120,
    notes='Protect the full fifteen-minute break. Announce an actual return time only after the timetable is confirmed. The following workshop starts with existing project material and paper; no new account, subscription or installation is required. Speaker overruns must be managed against the confirmed case allocations, not silently paid for by the break or the voluntary test.'))
S.append(activity('01 / MAP YOUR AI PRODUCT', 15, 'Four phases. One product.', [
    '0-4 / Need, affected people, data and missing evidence.',
    '4-8 / AI role, human choice, useful outcomes and harms.',
    '8-12 / Alternatives, failure paths and evaluation needs.',
    '12-15 / Choose one consequential uncertainty to test.',
], notes='85-100, one fifteen-minute block across slides 11-13. Each team makes a four-phase map of its own product with AI inside, in its existing workspace. This is not four full research phases completed in fifteen minutes. Record known decisions, evidence, risks and unknowns; choose the most consequential unresolved assumption. A concept, sketch or working interaction is an acceptable starting point. Carry forward Weeks 8-9 research and bias notes, and one relevant guest insight with transfer limits. No new upload or assessment.'))
S.append(two_col('SAME MAP BLOCK / EVIDENCE + DECISION + RISK + NEXT CHECK', 'Make the whole process visible.',
    ['DISCOVER', 'Person, need, affected people; data source and missing voices.',
     'DEFINE', 'Why AI? Model output, product rules, human choice; success and harms.'],
    ['DEVELOP', 'Alternative interactions; data limits, uncertainty and recovery.',
     'DELIVER', 'Interface test, model evaluation, responsibility and monitoring.'],
    right_font='body', left_size=34, right_size=34, lang=None,
    notes='Within the same fifteen minutes. For each phase, record one decision, its evidence or assumption, an important risk and the next check. The map is a working design aid, not a new compulsory poster section. Draw arrows back when uncertainty crosses phases: a harmful ranking may require revisiting data or the product\'s objective, not only changing a label. The product should incorporate AI; a non-AI baseline remains a useful comparator and fallback. Do not treat a generated persona or a guest example as direct evidence of this team\'s users.'))
S.append(content('SAME MAP BLOCK / USE WEEKS 8-9 EVIDENCE', 'A plausible idea is not a finding.', [
    'Open the source passage: who, task, comparison and outcome?',
    'Separate a finding, an assumption and a generated suggestion.',
    'Which evidence concerns your intended people and context?',
    'Write the strongest counterargument and the next evidence gap.',
], body_size=36,
    notes='Use within the map block, especially its final uncertainty choice. A generated summary is not the source; inspect the relevant passage if available. Note source version, access and limits. With no network, use saved project passages; with no evidence, write unknown rather than fabricate a finding. Not every learned pattern is harmful: specify a potential disadvantage, its mechanism and affected people, then consider research-backed mitigation. Keep disagreement in the map. No private sources, names or personal notes are collected.'))
S.append(activity('02 / DEVELOP AND PROTOTYPE', 30, 'Build only enough to learn.', [
    '0-5 / Sketch two responses; choose the uncertain decision.',
    '5-10 / Write a task and what would change your mind.',
    '10-25 / Build request, AI output, choice and recovery.',
    '25-30 / Label simulation; rehearse a neutral task.',
], notes='100-130, one thirty-minute block across slides 14-19. Substeps total thirty minutes. Start from the four-phase map, not an assumed polished prototype. Compare two interactions or autonomy levels, choose one uncertainty, define the test, then make the minimum useful prototype. Paper, role-play, Figma or existing code is fine. Teams with code should isolate one interaction, not add broad features. Show the AI\'s role, the person\'s choice, data boundary and at least one poor-output recovery path. Label simulated AI before participation.'))
S.append(two_col('SAME DEVELOP BLOCK / CHOOSE AN ALTERNATIVE', 'Test the decision, not the decoration.',
    ['FICTIONAL CAFE PRODUCT', 'A / AI chooses one cafe automatically.',
     'B / AI ranks options; the person edits constraints and chooses.',
     'Compare with a simple non-AI baseline where relevant.'],
    ['ONE UNCERTAINTY', 'Can a person understand a reason and reject an unsuitable suggestion?',
     'PAPER CANNOT SHOW', 'Actual model reliability, ranking accuracy or real-world safety.'],
    right_font='body', left_size=32, right_size=32, lang=None,
    notes='First five minutes of Develop. This is an invented example, not research or a guest\'s product. Compare what changes in the person\'s agency and burden, not just screen styling. The baseline helps justify AI and may offer recovery; it does not rewrite the project as a non-AI product. Choose an observable uncertainty such as comprehension, correction or recovery. Satisfaction alone does not establish effectiveness or safety. The task must match the question you can actually investigate today.'))
S.append(content('SAME DEVELOP BLOCK / TEST CONTRACT', 'Decide what would change your mind.', [
    'Task: compare two fictional options; choose one or reject both.',
    'Observe: stated reason, hesitation, correction and help needed.',
    'Revise if: a reason is mistaken or rejection needs coaching.',
    'This is a design trigger, not a validated threshold.',
], body_size=36,
    notes='Minutes 5-10 of Develop. Teams replace this fictional ten-minute cafe scenario with their own ordinary low-risk task. Write the prompt, comparison and observable outcome before testing. This is formative work, not a controlled experiment: order, familiarity and a tiny convenience sample limit attribution. Do not invent percentage targets or claim that a successful walkthrough establishes model quality, accessibility or long-term benefit. Record what result would challenge the preferred design.'))
S.append(two_col('SAME DEVELOP BLOCK / PAPER FALLBACK', 'Three cards are enough.',
    ['1 / REQUEST', 'Fictional commuter: ten minutes, two cafe options. No real account or location.',
     '2 / AI SUGGESTION', 'Two invented options and reasons. SIMULATED AI - prepared by the team.'],
    ['3 / CHOICE + RECOVERY', 'Change constraints, choose another, reject both or continue without AI.',
     'Prepare one unsuitable suggestion and its recovery path.',
     'No device, login, purchase or model call is needed.'],
    right_font='body', left_size=32, right_size=32, lang=None,
    notes='Minutes 10-25 of Develop. Make simulation visible before the task; a teammate reveals a prepared next card after the person acts, not a covert model impersonation. Invented cafe names, reasons and attributes are scenario props, not actual recommendations. One mismatch could violate the fictional time constraint. Test how the interface handles it, not an invented model failure rate. No need to spend workshop time installing tools or connecting a live model.'))
S.append(F.mediation_checkpoint(VERBEEK,
    notes='Same Develop block; support slide, not extra time. Verbeek\'s Beyond Interaction (2015), pp.28-31, is the established Week 8 conceptual lens: technologies shape perception and action, not merely serve fixed intentions. The fictional cafe example is our application, not a study from the essay. Ask who notices a poor suggestion, who must correct it and whether refusal is meaningful. Correction, rejection and fallback are design hypotheses, not proven safeguards. An override button alone does not settle wider consequences or responsibility.'))
S.append(content('SAME DEVELOP BLOCK / WEEK 9 CHECKPOINT', 'Keep data and harm in the design.', [
    'What input is necessary? What could you avoid collecting?',
    'Who might receive a worse or unsuitable suggestion, and why?',
    'How would someone correct data, challenge output or recover?',
    'Test a mitigation; do not claim that bias has been removed.',
], body_size=36,
    notes='Use during building and the final five-minute rehearsal, not as another activity. Carry the relevant Week 9 harm example and proposed mitigation into a concrete interaction. A smaller data footprint does not automatically make a product fair, and a visible explanation does not prove accuracy. Do not equate learned patterns with harmful bias: identify a contextual disadvantage and mechanism. Use synthetic inputs; no identifiable or sensitive data. A product-level control cannot substitute for evaluating underlying model/data behaviour.'))
S.append(activity('03 / VOLUNTARY PEER WALKTHROUGH', 25, 'Give the task. Then watch.', [
    '0-3 / Explain simulation, voluntary participation, right to stop.',
    '3-11 / Test. 11-19 / Swap if willing. 19-25 / Compare notes.',
    'Declining is fine: use an internal walkthrough.',
    'No recording, names, sensitive stories or transactions.',
], notes='130-155, one twenty-five-minute block across slides 20-22. The 3+8+8+6 checkpoints total twenty-five minutes. Invite another team locally, explain simulated behaviour and allow anyone to decline, pause or stop. An internal walkthrough is an alternative, with weaker outsider evidence and clearly labelled. Use synthetic, low-risk scenarios only. Do not collect names, recordings, personal stories or health/legal/financial data. Consent is for classroom learning, not publication. Stop intrusive or unsafe scenarios; do not initiate recruitment or high-stakes validation.'))
S.append(two_col('SAME WALKTHROUGH BLOCK / NEUTRAL SCRIPT', 'Do not teach the answer.',
    ['SAY', 'This is a simulated interface. You can stop at any time.',
     'Use these fictional options to make a choice, or reject both.', 'What would you do next?'],
    ['AVOID', 'Click the explanation so you can trust our AI.', 'You like this version better, right?',
     'Observe difficulty before helping; record any help.'],
    right_font='body', left_size=32, right_size=32, lang=None,
    notes='Leave visible during the walkthrough if useful. Use a neutral task that permits rejection, not a script guiding the person to the desired outcome. A think-aloud request can change behaviour; a pause is not automatically confusion. Ask after the attempt what a label meant and what the person expected. If comparing variants, record order and familiarity; this exercise cannot isolate causal effects. A helpful facilitator must not turn coached success into an unassisted outcome.'))
S.append(two_col('SAME WALKTHROUGH BLOCK / KEEP NOTES PRIVATE', 'Observation is not interpretation.',
    ['OBSERVATION / INVENTED EXAMPLE', 'Person chose B, then asked where the quiet claim came from.',
     'Reject was found only after a hint.', 'Record task, action, outcome and any help; no names.'],
    ['INTERPRETATION / TENTATIVE', 'The explanation may not show its evidence clearly.',
     'NEXT CHECK', 'Try a source label and visible rejection; test again.'],
    right_font='body', left_size=32, right_size=32, lang=None,
    notes='Use the final six minutes to compare observer and test-lead notes. The text is an invented example, not actual classroom results. A classmate is not automatically an intended user. Distinguish observation from inference and interface behaviour from model quality. Satisfaction alone is insufficient; a failure can reflect task wording or prototype limits. Preserve one outcome that challenged expectations and explicitly record missing evidence. Keep test notes in the existing private team workspace.'))
S.append(activity('04 / REVISE AND SHARE', 10, 'One changed decision. Its evidence.', [
    '0-5 / Revise one consequential decision; keep before/after.',
    '5-8 / Share evidence and limits with a neighbouring team.',
    '8-10 / Record the next check and who should act.',
], notes='155-165, one ten-minute block across slides 23-25. The 5+3+2 checkpoints total ten minutes. Return to the four-phase map: revise the relevant need, AI role, data choice, interaction or recovery path. A defensibly retained decision is acceptable if evidence and limits are explicit. Share locally rather than create a full-room pitch queue. No new collection, grade or deadline. If the ESFQ reserve is unused, use it for extra revision and feedback rather than extend beyond three hours.'))
S.append(content('SAME REVISION BLOCK / DELIVER IS NOT THE END', 'What still needs a real test?', [
    'Separate interface evidence from actual model performance.',
    'Name missing users, contexts, harmful outcomes and data checks.',
    'Plan feedback, privacy-safe monitoring, recovery and responsibility.',
    'No clinical, legal or high-stakes validation here.',
], body_size=36,
    notes='During revision, plan the next evidence without pretending it was gathered today. A simulated interface cannot establish recommendation quality or fairness, and classmates do not represent all affected people. Name who would review failures and what would trigger rollback, correction or reframing. Monitoring must respect purpose and data limits; this classroom plan is not permission to collect personal data, recruit people or deploy a high-stakes system. Return to Discover/Define when the problem or objective, not just the interface, is wrong.'))
S.append(content('FINISH / EXISTING PROJECT WORKSPACE', 'Keep the reasoning, not just the screen.', [
    'Keep: four-phase map + evidence + test + before/after.',
    'State: changed ___ because ___; not established ___.',
    'Prototype v1 milestone still applies. Check Canvas instructions.',
    'No new graded submission or deadline.',
], body_size=36,
    notes='Final two minutes of revision/sharing. The intended outcome is a map of the AI-enabled product across four phases, key decisions and risks, and a prototype/walkthrough of the most consequential uncertainty. Keep observation, interpretation, simulation and unknowns separate. This feeds existing project research, poster and mediation reasoning without adding compulsory assessed sections. Preserve the syllabus Prototype v1 milestone and actual Canvas instructions. No student test notes or records belong in public course sources.'))
S.append(content('PROVISIONAL RESERVE / 15 MINUTES / PLACEMENT TO CONFIRM', 'School ESFQ: if confirmed.', [
    '15 minutes reserved provisionally; placement to confirm.',
    'Visit not yet confirmed. Follow confirmed school instructions.',
    'Move the reserve if needed; unused time: revision and feedback.',
], body_size=37, bg=PAPER,
    notes='165-180 is a planning placeholder, not a confirmed school visit. Giovanni is confirmed absent; confirm the date, facilitation coverage and school arrangement. If the visit moves, move its reserve and recalculate the proposed sequence while protecting the break and workshop. Do not shorten a confirmed school slot. If no visit occurs, use these fifteen minutes for revision and feedback. No special survey or assessment is invented.'))
S.append(content('REFERENCE SHELF / OUTSIDE THE TIMED ROUTE', 'Framework, mediation and course evidence.', [
    f'[Design Council: The Double Diamond]({DC}) - framework; official diagram CC BY 4.0.',
    f'[Verbeek (2015), Beyond Interaction]({VERBEEK}) - Week 8 mediation lens.',
    'Weeks 8-9 project research and bias notes: check passages and transfer limits.',
    f'[S\u00f6zen & B\u00f6rek\u00e7i (2026), AI EDAM 40, e9]({PAPER_URL}) - optional AI-as-design-tool context, not AI-product validation.',
], body_size=32,
    notes='Untimed reference shelf, not extra assigned reading. The following two preserved study slides are optional background only: they concern designers using AI tools, not evaluation of products with AI inside. Do not use them as evidence of AI-product benefit, safety or reliability. Primary source checks, licences and access limits remain in week10-references.md. The phase-specific AI-product prompts are the course\'s teaching synthesis of the framework and Weeks 8-9, not empirical results from the optional study.'))
S.append(F.study_setup(PAPER_URL,
    notes='Optional background, outside the 180-minute route. This study concerns AI as a design tool, not evaluation of AI-enabled products. Primary final Cambridge PDF methods pp.4-7 and results/discussion pp.13-16 were checked in the previous evidence pass; no new re-audit is claimed here. 88 valid AI-user survey responses from 103 replies to 3,004 invitations; 10 selected professional designers in Turkiye used chosen tools on a lunchbox task in May-June 2024. Low response, self-selection and sector limits; coding primarily first author with second-author checking and no formal inter-rater reliability. No randomized no-AI comparison. Do not infer superior outcomes, saved time or AI-product validation.'))
S.append(F.study_result(PAPER_URL,
    notes='Optional background, outside the timed route. Preserved authentic Figure 5, final Cambridge 19-page PDF, p.16: the top-panel crop keeps four phases and activity labels; crop provenance and full local figure remain in deck/assets/week10/. Widths are not measured time shares, participant counts or effect sizes. This maps how selected designers used AI tools, not model performance or consequences of an AI-enabled product. Persona generation is an observed practice, not evidence about real users. Retain CC BY 4.0 attribution and the clickable article; no extra workshop or reading requirement.'))

attach_reports(S, Path(__file__).resolve().parent / 'week10-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 10',
            slides=finalize(S, footer(10)), pdf='SD2112-week10.pdf')
