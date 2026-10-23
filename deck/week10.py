"""Week 10: evidence-based reframe / prototype / voluntary peer test workshop."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import title, content, two_col, activity, statement, figure_slide, finalize
from course import footer
import week10_figures as F

S = []
DC = 'https://www.designcouncil.org.uk/resources/the-double-diamond/'
PAPER_URL = 'https://doi.org/10.1017/S0890060426100304'
VERBEEK = 'https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf'
# Relative time is deliberate: date, staffing and the school's visit are unconfirmed.
BLOCKS = [
    (0, 15, 'Provisional school ESFQ reserve', 1, 1),
    (15, 30, 'Framing', 2, 7), (30, 55, 'Reframe', 8, 11),
    (55, 75, 'Develop', 12, 14), (75, 90, 'Break', 15, 15),
    (90, 115, 'Prototype', 16, 18), (115, 145, 'Test', 19, 21),
    (145, 165, 'Revise', 22, 23), (165, 180, 'Share', 24, 25),
]

S.append(content('PROVISIONAL RESERVE / 15 MINUTES / PLACEMENT TO CONFIRM',
    'School ESFQ: if confirmed.', [
    '15 minutes reserved provisionally; school placement to confirm.',
    'Visit not yet confirmed. Follow confirmed school instructions.',
    'Move the reserve if needed; unused time: revision and feedback.',
], body_size=37, bg=PAPER,
    notes='0-15 is a planning placeholder, not a statement that school staff are present, have accepted or will visit at this time. Giovanni is confirmed absent; coverage is unconfirmed. Confirm date, facilitators and school placement before class. No survey is invented here. Preserve all workshop blocks and the break; an unused reserve becomes revision/feedback, not a new assessment.'))
S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 10',
    'Reframe.\nPrototype. Test.', 'The Double Diamond with evidence.', size=132,
    notes='15-30 framing block, six slides total. No pre-reading is assumed. Keep the framework, study summary and figure to six minutes together; this is not an added lecture block. Giovanni is absent; no named substitute is assumed. Use relative times until calendar and coverage are confirmed. This is a facilitated workshop, not a replacement recommendation lecture. By the end, each team can explain evidence -> changed question -> prototype -> observation -> revision. No new submission, deadline or grading criterion.'))
S.append(content('15-30 / OPEN YOUR EXISTING TEAM WORK', 'Start where your project is.', [
    'Start with a concept, sketch or working interaction.',
    'Open Weeks 8-9 evidence + one unresolved assumption privately.',
    'Keep decisions in your team workspace. No new upload.',
    'Prototype v1 milestone still applies. Check Canvas instructions.',
], body_size=35, notes='Two minutes. Ask teams to locate one source and one unresolved assumption. Do not collect private notes or require a polished interface. Existing prototype teams should test one uncertain interaction, not add features. The syllabus still lists Prototype v1 in Week 10; instructor must reconcile implementation with actual Canvas instructions, not silently move the milestone.'))
S.append(two_col('EVIDENCE / A FICTIONAL WORKED EXAMPLE', 'A plausible idea is not a finding.',
    ['ASSUMPTION / The commuter needs an AI cafe chooser.',
     'SCENARIO / Ten minutes. Two cafe options.',
     'Invented teaching example, not research evidence.'],
    ['MISSING / Quiet for whom, and when?',
     'TEST / Can they compare reasons and reject an option?',
     'Paper tests comprehension, not actual cafe quietness.'],
    right_font='body', left_size=33, right_size=31, lang=None,
    notes='Three minutes. Avoid inventing study results for the cafe example. A source may support a broad concern without establishing this user need. Ask which evidence about intended users the team actually has, versus a design hypothesis, a prepared scenario or generated persona. Observable task behaviour is evidence about that test only.'))
S.append(figure_slide('FRAMEWORK / OPEN UP, THEN FOCUS', 'Two diamonds. Four kinds of work.', F.source_image('design-council-double-diamond.png', 'Official Design Council Double Diamond: Discover, Define, Develop, Deliver'), bg=PAPER,
    body=['Discover: explore evidence. Define: focus the question.',
          'Develop: explore responses. Deliver: test and improve. Return when evidence changes.'],
    caption=f'[Design Council: The Double Diamond]({DC}), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Official diagram, unchanged.',
    notes='Two minutes. Official Design Council resource checked October 21, 2026: Discover understands rather than assumes the problem; Define reframes the challenge; Develop explores different responses; Deliver tests small-scale solutions, rejects and improves. The original official Design Council PNG is reproduced unchanged under CC BY 4.0. It is a framework, not measured data. The teaching recap sits outside the image. Divergence opens possibilities; convergence focuses choices. Do not repeat the 2025 Week 8 page 29 claim equating divergence with doing the thing right and convergence with doing the right thing: those slogans do not define the distinction. Testing can send us back to Discover/Define.'))
S.append(F.study_setup(PAPER_URL, notes='Two minutes; no pre-reading. Question: how do professionals integrate AI? Explain survey versus selected observed task before the finding. The study/result pair explains the task and what was coded before interpreting the map; it is not assigned reading. Primary final Cambridge open PDF read: methods pp.4-7, results/discussion pp.13-16 and Figure 5 p.16 visually inspected. 88 valid AI-user survey responses from 103 replies to 3,004 invitations; 10 selected professional designers in Turkiye in May-June 2024 think-aloud sessions using chosen tools on a lunchbox task. Low response, self-selection/experience/sector limits; coding primarily first author with second-author checking and no formal inter-rater reliability. These sample counts are context, not effect estimates. No randomized no-AI comparator, so do not infer superior outcomes or time savings. Application: AI can suggest an alternative question, but it cannot replace evidence from affected people. Distinguish use of AI in designing from AI incorporated in the product.'))
S.append(F.study_result(PAPER_URL, notes='Two minutes, completing the SAME 15-minute framing block. Actual Figure 5, final Cambridge 19-page PDF, PDF/printed p.16. Top-panel crop preserves the four phases and activity labels; the dense lower list is omitted for projection, not reconstructed. The complete local crop and source provenance are in deck/assets/week10/. Read left to right: AI appeared in problem exploration as well as solution work. Do not interpret triangle width as measured time, participant count or benefit. Persona generation is an observed practice, not validation of synthetic users. Application to this workshop: consider an alternative framing but check real evidence before adopting it. Use the clickable article for the full figure; no pre-reading or additional workshop time.'))
S.append(activity('01 / REFRAME', 25, 'Reopen the problem, not just the file.', ['0-7 / Evidence versus assumption.', '7-15 / Person, context, need, missing voice.', '15-22 / Rewrite the question. 22-25 / Counterargument.'], notes='30-55, one 25-minute block across slides 8-11. The checkpoints partition this block, not extra timers. Paper and pens suffice. Circulate: What evidence makes you say that? If there is no research, write unknown rather than fabricate a finding. Teams can test comprehension of a problem statement today, while identifying missing external research. Facilitation detail retained from the prior slide: 0-7 min: compare your strongest relevant finding with the assumption it does not settle. 7-15 min: name the person, context, need and a missing perspective. 15-22 min: rewrite the question without assuming your favourite feature is the answer. 22-25 min: state what changed and the strongest counterargument.'))
S.append(content('SAME REFRAME BLOCK / EVIDENCE CARD', 'Read the passage again.', [
    'PASSAGE / Source, version, page. Full text or abstract?',
    'METHOD / Who? Task? Comparison? Outcome? When?',
    'FINDING / What is supported? What is not?',
    'GAP / Whose context or perspective is missing?',
], body_size=36,
    notes='Within the first seven minutes. Use research from Weeks 8-9 rather than assigning another reading quota. A generated summary is not the source; open the supporting passage if available. With no network, use saved team passages or the prepared primary-paper card in week10-references.md. Label access gaps; do not turn a different sample into evidence of this team\'s users. No sources or personal notes are uploaded.'))
S.append(two_col('SAME REFRAME BLOCK / DEFINE', 'Change the question.',
    ['BEFORE / FEATURE-FIRST', 'How might we build a cafe recommender?',
     'AFTER / NEED-FIRST', 'How might a time-limited commuter compare options and understand why each is suggested?'],
    ['YOUR TEMPLATE', 'For [person in context], the problem is [need], not simply [feature].',
     'Which finding supports that need? What contradicts our first idea?',
     'Example only: the commuter need is still a hypothesis.'],
    right_font='body', left_size=32, right_size=31, lang=None,
    notes='Use during minutes 7-22 of reframing. The narrower question still leaves non-AI and lower-autonomy responses possible. Do not describe it as validated by the paper. Ask whose problem gets easier, whose labour or control becomes invisible, and what an affected person might dispute. This keeps mediation in view while avoiding a new philosophy lecture.'))
S.append(content('SAME REFRAME BLOCK / DECISION CHECKPOINT', 'Keep the disagreement.', [
    'We used to think ___. The evidence makes us reconsider ___.',
    'Our revised question is ___. We still assume ___.',
    'The strongest counterargument is ___. A missing perspective is ___.',
    'Choose a reader, sketcher, test lead and observer; share roles if needed.',
], body_size=38,
    notes='Final three minutes of the same block. Invite a short within-team explanation, not a compulsory public pitch. A team can retain its question if it explains why the evidence did not warrant change. Record dissent, not artificial consensus. Roles are workshop roles only; do not change assessed contribution requirements.'))
S.append(activity('02 / DEVELOP', 20, 'Two responses. One uncertainty.', ['0-7 / Sketch two different responses.', '7-12 / Compare autonomy. 12-17 / Choose one risk.', '17-20 / Write the test contract.'], notes="55-75, one twenty-minute block across slides 12-14. Two differently coloured screens are not necessarily different responses. Cafe example: automatic single choice versus a comparison card with editable constraints. Ask what changes in the person's role. The project still incorporates AI; a non-AI alternative is a comparator, not a rewritten assessment brief. Facilitation detail retained from the prior slide: 0-7 min: draw two meaningfully different responses to your revised question. 7-12 min: compare an AI option with a non-AI or lower-autonomy route where relevant. 12-17 min: choose the assumption whose failure would most change the design. 17-20 min: write the test contract before you build."))
S.append(two_col('SAME DEVELOP BLOCK / SELECT A RISK', 'Test the decision, not the decoration.',
    ['WEAK: do people like the screen?', 'BETTER: can someone compare the reasons and reject an unsuitable suggestion?',
     'Choose one uncertainty: comprehension, choice, correction or recovery.'],
    ['WHAT PAPER CAN SHOW', 'Where a participant looks, what they interpret, what they choose and whether they find an exit.',
     'WHAT PAPER CANNOT SHOW', 'Actual model reliability, recommendation accuracy or real-world safety.'],
    right_font='body', left_size=33, right_size=31, lang=None,
    notes='During selection. A satisfaction question may add context, but satisfaction alone is not proof of accuracy, safety or effectiveness. Existing code also requires an explicit task and comparator. Do not require an artificial quantitative score from one classmate. The chosen observation must correspond to the uncertainty, not simply be easy to collect.'))
S.append(content('SAME DEVELOP BLOCK / TEST CONTRACT', 'Decide what would change your mind.', [
    'Person + context: a volunteer classmate in a fictional ten-minute cafe scenario.',
    'Task + comparison: choose an option and explain why; compare two explanation cards.',
    'Observe: first choice, stated reason, hesitation, rejection and help needed.',
    'Revise if: the reason is mistaken or rejection needs coaching. This is a design trigger, not a validated threshold.',
], body_size=34,
    notes='Final three minutes of Develop. Teams replace the example with their own ordinary low-risk task. Write a neutral prompt and a result that would challenge the design before looking at outcomes. The example comparison is formative, not a controlled experiment: order, familiarity and tiny convenience samples limit attribution. Do not manufacture a percentage pass target. Keep this contract beside the prototype.'))
S.append(statement('Break.\n15 minutes.', eyebrow_text='75-90 / RELATIVE CLASS TIME', size=120,
    notes='Protect the full break. Announce an actual return time only after the timetable is confirmed. On return, paper, pens and prepared synthetic cards are enough. Do not spend the break creating accounts or installing tools.'))
S.append(activity('03 / PROTOTYPE', 25, 'Build only enough to learn.', ['0-5 / Choose the simplest useful format.', '5-18 / Build task, choice and fallback.', '18-23 / Label simulation. 23-25 / Rehearse.'], notes='90-115, one 25-minute block across slides 16-18. Fidelity follows the uncertainty, not prestige. Paper works with no tool account or network. Existing code teams freeze broad new features and isolate the tested interaction. A manually supplied response can test the interface promise but cannot establish model capability. If the prototype is unfinished, test a single paper decision rather than lose the test block. Facilitation detail retained from the prior slide: 0-5 min: choose paper sequence, role-play, clickable flow or existing code. 5-18 min: make the task, suggestion, choice and fallback visible. 18-23 min: label simulated AI and prepare an unsuitable-result card. 23-25 min: rehearse the neutral task prompt; remove extra features.'))
S.append(two_col('SAME PROTOTYPE BLOCK / MANUAL FALLBACK', 'Three cards are enough.',
    ['1 / REQUEST', 'Fictional commuter: ten minutes; compare two cafes. No real location or account.',
     '2 / SUGGESTION', 'Two invented options with visible reasons. Label: SIMULATED AI - prepared by the team.'],
    ['3 / CONTROL + RECOVERY', 'Show change constraints, choose another, reject all or continue without AI.',
     'A teammate reveals the next card after the participant acts.',
     'No device, login, purchase or model call is needed.'],
    right_font='body', left_size=32, right_size=31, lang=None,
    notes='Use within the build block, or print this slide as a three-card starter. Make the simulation visible to the participant BEFORE the task. The teammate follows a prepared branch, not a covert model impersonation. Invented cafe names and attributes are scenario props, not factual recommendations. Prepare one mismatch such as a suggestion outside the stated time constraint. Describe only its interface effects; do not imply measured hallucination rates.'))
S.append(F.mediation_checkpoint(VERBEEK, notes='Same prototype block, final checkpoint; no extra lecture time or assumed pre-reading. Verbeek, Beyond Interaction, 2015, pp.28-31 (PDF positions 3-6), conceptual essay: technologies mediate human-world relations, shaping perception and action, not merely serving fixed intentions. The cafe recommendation is our application, not an empirical example from the essay. The essay discusses multiple relations and types of influence; this recap does not reduce mediation to an override button. Ask who does the work of noticing a bad suggestion, what becomes less visible, and whether refusal is meaningful before acceptance. Correction/rejection/fallback are hypotheses for the next walkthrough, not a validated remedy or an AI/no-AI result. The essay has no necessary data figure for this brief recap; no unrelated illustration is substituted.'))
S.append(activity('04 / VOLUNTARY PEER TEST', 30, 'Give the task. Then watch.', ['0-5 / Explain simulation, voluntary participation, right to stop.', '5-15 / Test. 15-25 / Swap if willing.', '25-30 / Compare notes. Declining is fine: internal walkthrough.', 'Synthetic scenarios only. No recording, names, sensitive stories or transactions.'], notes='115-145, one thirty-minute block across slides 19-21. Pair teams locally; no centralized student roster or new research recruitment. Consent is for a classroom walkthrough, not publication. Anyone may decline, pause or stop without pressure. No audio/video, personal health/legal/financial issues or sensitive data. Stop intrusive or unsafe tests; switch to an ordinary interface question. Internal walkthrough is an alternative with weaker outsider evidence, clearly labelled. Facilitation detail retained from the prior slide: 0-5 min: invite another team; explain simulation, voluntary participation and the right to stop. 5-15 min: one team tests while the other observes; 15-25 min: swap if willing. 25-30 min: compare notes. Declining is fine: use an internal walkthrough instead. Use synthetic, low-risk scenarios. No recording, names, sensitive stories or real transactions.'))
S.append(two_col('SAME TEST BLOCK / NEUTRAL SCRIPT', 'Do not teach the answer.',
    ['SAY', 'This is a simulated interface. You can stop at any time.',
     'Imagine you have ten minutes. Use these cards to choose an option, or reject both.',
     'What would you do next?'],
    ['AVOID', 'Click the explanation so you can trust our AI.',
     'You like this version better, right?',
     'If stuck, note the difficulty before helping. Mark any help in the notes.'],
    right_font='body', left_size=32, right_size=31, lang=None,
    notes='Leave this on screen during walkthroughs if useful. The prompt permits rejection and does not demand a preferred answer. A think-aloud request may change behaviour; silence is also an observation. Do not interpret every pause as confusion without checking. After the attempt, ask what a label meant and what they expected. If two variants are compared, note order/familiarity; this small classroom exercise cannot isolate causal effects.'))
S.append(two_col('SAME TEST BLOCK / NOTE TEMPLATE', 'Observation is not interpretation.',
    ['OBSERVATION / DIRECT', 'Participant chose B, then asked where the quiet claim came from.',
     'They found reject only after a hint. No names or identifiable quotes.',
     'These are invented examples, not classroom results.'],
    ['INTERPRETATION / TENTATIVE', 'The explanation may not show its evidence clearly.',
     'NEXT MOVE', 'Try a source label and a visible reject option; test again.',
     'Record task, action, outcome, help and uncertainty.'],
    right_font='body', left_size=32, right_size=31, lang=None,
    notes='Use the final five minutes to compare observer and test-lead notes. Record behaviour as specifically as possible without identifiers. Satisfaction can be noted separately, never substituted for task outcome. A classmate is not automatically an intended user; a single successful task does not prove accessibility, long-term benefit, safety or model performance. A failure may be due to the task wording or the prototype, not only the participant. Keep notes local.'))
S.append(activity('05 / REVISE', 20, 'Change one consequential decision.', ['0-5 / What challenged the test contract?', '5-15 / Change one consequential decision.', '15-20 / Before/after + next uncertainty. No invented findings.'], notes='145-165, one twenty-minute block across slides 22-23. Deliver means testing and improving, not declaring a classroom mock-up ready to ship. It may be right to return to Define. Preserve one observation that did not support the preferred concept. If there was no external volunteer, state internal walkthrough rather than peer validation. Do not overwrite the original sketch; the before/after explains learning. Facilitation detail retained from the prior slide: 0-5 min: compare observation with your test contract. What challenged you? 5-15 min: revise one question, explanation, choice, boundary or recovery path. 15-20 min: make a before/after sketch and state the next uncertainty. An inconclusive result is useful. Do not invent a positive finding.'))
S.append(content('SAME REVISE BLOCK / LIMITS AND NEXT EVIDENCE', 'Who still needs to be heard?', [
    'Classmates are not necessarily intended users.',
    'Next evidence: affected users, research or real model evaluation?',
    'No clinical, legal or high-stakes validation here.',
    'Name the evidence gap. Do not invent results or recruit.',
], body_size=36,
    notes='During revision, distinguish interface comprehension from real recommendation quality and outcomes over time. Teams must not begin high-stakes or sensitive participant testing here. Planning future evidence does not authorize recruitment or collection. Ask what result would make them abandon the concept, not only improve it. Research gaps should travel into the poster and mediation argument honestly.'))
S.append(activity('06 / SHARE', 15, 'One changed decision. Its evidence.', ['0-5 / Prepare a before/after explanation.', '5-12 / Exchange evidence and limits with neighbours.', '12-15 / Record: changed ___ because ___; not established ___.'], notes='165-180, one fifteen-minute block across slides 24-25. Neighbour sharing scales to the cohort without a full-room presentation queue. Voluntary spoken examples may replace some neighbour discussion within the same time. Do not collect another artifact or impose a pitch grade. If the reserve was unused, add feedback/revision there rather than extending beyond three hours. Facilitation detail retained from the prior slide: 0-5 min: prepare a short before/after explanation in your team. 5-12 min: exchange with a neighbouring team; compare evidence and limits. 12-15 min: record what changed and what remains unresolved. Use: We changed ___ because we observed ___. This does not establish ___.'))
S.append(content('FINISH / EXISTING PROJECT WORKSPACE', 'Keep the learning, not just the screen.', [
    'Keep: question + source + test contract + before/after.',
    'Separate observation, interpretation, simulation and uncertainty.',
    'Use the trail in your existing research, poster and mediation brief.',
    'No new graded submission or deadline. Syllabus + Canvas still apply.',
], body_size=36,
    notes='Final three minutes of Share, not another activity. Check each team has a changed or defensibly retained decision and an uncertainty, not only a screenshot. Never put student notes, names, recordings or test data in the public repository. Confirm Prototype v1 expectations with the instructor before delivery; this draft does not change them. Leave facilitator, actual date and school ESFQ placement as explicit pre-class decisions.'))
S.append(content('REFERENCE SHELF / NOT EXTRA TIMED READING', 'Framework. Study. Mediation.', [
    f'[Design Council: The Double Diamond]({DC}) - framework; official diagram under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).',
    f'[Sözen & Börekçi (2026), AI EDAM 40, e9]({PAPER_URL}) - professional designers\' practices; not proof of better outcomes.',
    f'[Verbeek (2015), Beyond Interaction, Interactions 22(3), 26-31]({VERBEEK}) - established course mediation reading.',
    'Use your project-specific Weeks 8-9 evidence; check passages and transfer limits.',
], body_size=32,
    notes='Untimed reference shelf. Full citation and passage ledger: lessons/week10-references.md. Original research author names: Tugce Sozen and Naz A. G. Z. Borekci (diacritics recorded in the reference companion). The official framework and the empirical study have different evidential roles. The archive is historical context only; no guest or old November 30 deadline is carried forward.'))

attach_reports(S, Path(__file__).resolve().parent / 'week10-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 10',
            slides=finalize(S, footer(10)), pdf='SD2112-week10.pdf')
