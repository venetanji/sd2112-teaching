"""Week 12: from judgment to justified reliance; case and studio review."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import attach_reports, PAPER
from deckgen.layouts import title, content, cards, two_col, statement, question, activity, section, finalize
from course import footer
import week12_figures as F
S = []
NTSB = 'https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR2001.pdf'
CECIL = 'https://doi.org/10.1038/s41598-024-60220-5'
SETTLEMENT = 'https://www.theguardian.com/technology/2024/apr/08/tesla-crash-lawsuit-apple-engineer'
REFS = {'R1': ('Cecil et al., Scientific Reports (2024)', CECIL),
        'R2': ('NTSB, HAR-20/01 (2020)', NTSB),
        'R3': ('Guardian/Reuters, settlement report (8 April 2024)', SETTLEMENT)}
def source(key):
    label, url = REFS[key]
    return f'[{key} / {label}]({url})'

S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 12',
    'From judgment\nto justified reliance.', "What may a system do on someone else's behalf?",
    notes='Week 11 introduced mediation: a technology shapes how people perceive, interpret and act. It also examined curation, authorship, responsibility and the Suno litigation. Do not reteach those cases. This week asks when the invitation to rely on a product is justified by task evidence and meaningful control, especially when action has consequences. Use the verified 2018 Tesla Autopilot case, not Full Self-Driving (Supervised), as the case. Then test an existing project with paper or static screens. Exactly 180 minutes; reference shelf is untimed.'))
S.append(content('0-10 / TODAY / 180 MINUTES', 'Evidence -> permission -> revision.', [
    '0-75: delegation, a real case, one study and a bounded design response.',
    '75-90: break. 90-120: interface walkthrough, 30 minutes.',
    '120-155: mock review, 35 minutes. 155-175: revision, 20 minutes.',
    '175-180: one decision and one open question. No new submission.',
], body_size=33, notes='Use relative minutes rather than an assumed classroom start time. Protect the full break and the thirty, thirty-five and twenty minute practice blocks. The opening and closing short answers are optional oral/team-note reflections or ClassPoint; the workshop does not collect an artifact. This is not a second AI safety assessment. Show the task, permission and recovery possibilities of each project, including non-chatbot concepts. If running late, shorten spoken case discussion, never the practice budget.'))
S.append(question('short_answer', 'What should a person NOT delegate to your product?',
    hint='Name the person, the consequential choice and what evidence would change your answer.',
    eyebrow_text='0-10 / TEAM NOTES, ORAL SHARE OR CLASSPOINT',
    notes='Opening reflection takes about three minutes. A single blanket prohibition is less useful than a boundary for a particular task and person. For example, a booking aid may suggest rooms while the group retains final approval; an installation may adjust light while the operator sets a maximum. Ask what evidence would justify shifting the boundary. Do not request personal experiences or private material. The oral/team-note route is complete; ClassPoint is optional, named by default and not an assessed collection.'))
S.append(section('01 / DELEGATION', 'What can the\nsystem decide?', 'Judgment, action and permission / 10-40 min', bg='#246E70',
    notes='Carry Week 11 mediation forward without reteaching Verbeek or the Suno case. A product does not only offer information; its defaults and actions distribute opportunities to judge and act. Spend thirty minutes total on slides four through thirteen. Use a fictional room-booking example to make the concepts accessible before the Tesla case. The case is a high-stakes counterexample to the idea that a mere override always provides meaningful human supervision. Do not use crash images or speculate about the person who died.'))
S.append(cards('10-40 / ONE REQUEST / THREE BOUNDARIES', '"Find an available workshop slot."', [
    ('SUGGEST', 'Propose a room.', 'The person checks the capacity, access needs and schedule.'),
    ('READ', 'Check a timetable.', 'The product may expose private records even without changing them.'),
    ('ACT', 'Reserve the room.', 'A tool changes a record. Ask for specific permission first.'),
], text_size=31, notes='This is an instructor-authored example, not an observed product. A suggestion, a read and a reservation confer different amounts of authority. A machine might use written filters, learned language interpretation or both, but neither mechanism grants permission. Explain that even a read can reveal private information to a provider or team member. The question is which particular action is allowed, who can check the evidence and who can correct a mistake. Non-chatbot systems make these choices too.'))
S.append(F.stages('DESIGN MODEL / ILLUSTRATIVE, NOT A MEASURED RESULT',
    'Reliance is a loop, not a button.', [
       ('GOAL', 'Person requests.', 'The system offers a possible interpretation of the goal.'),
       ('EVIDENCE', 'System proposes.', 'Show what supports the answer and what remains unknown.'),
       ('PERMISSION', 'Person can refuse.', 'Separate advice from an irreversible or external action.'),
       ('RESULT', 'Both can check.', 'Show what happened; offer correction and accountable repair.'),
    ], 'Feedback goes back to GOAL. A visible override alone does not show that it can be used in time.',
    'Original editable conceptual diagram by the course, not a model trace, empirical result or guaranteed design solution. The loop translates Week 11 mediation into a limited grant of authority: goal interpretation, proposed evidence, permission and feedback. A confirmation may fail if it arrives too late, hides important evidence or is inaccessible. An undo control cannot retract already disclosed information. Ask the room where a recommendation may stop and where a booking needs fresh permission. No study validated this exact flow.'))
S.append(two_col('RELIANCE / WORKING DISTINCTION', 'Persuasive is not justified.', [
    'A confident sentence can invite action without supporting evidence.',
    'A smooth interface can make limits harder to notice.',
    'Trust describes an attitude; justified reliance asks what this task warrants.',
], [
    'ASK FOUR CONCRETE QUESTIONS',
    'What can the system actually do?',
    'Where has it been checked - and where not?',
    'Can the person refuse in time and challenge the result?',
], right_font='body', left_size=34, right_size=33,
    notes='This is the teaching distinction, not a universal psychological law. Week 11 called attention to mediation and curation; now ask whether the evidence and practical boundaries justify acting on a particular output in a particular setting. A description, explanation or warning is not by itself proof of accuracy. A visible control is not by itself a usable option. Later, a personnel-screening experiment offers narrow task evidence, while the transport investigation shows how a system, a driver and institutions share causal pathways.'))
S.append(section('CASE / 2018 / MOUNTAIN VIEW', 'Autopilot was\nnot autonomy.', 'NTSB investigation / 2018 crash, 2020 report', bg='#246E70',
    notes='Use precise product terminology. The March 23, 2018 vehicle was a 2017 Tesla Model X P100D using Autopilot: Traffic-Aware Cruise Control and Autosteer, SAE Level 2 partial driving automation. It was not Full Self-Driving (Supervised) or autonomous driving. The driver remained responsible for monitoring and intervention under this system. The report is a causal safety investigation, not a jury verdict or generalized estimate of crash risk. Walter Huang died; avoid graphic images, victim blame and a moralized reconstruction. Source: NTSB HAR-20/01, executive summary and pp. 12-15.'))
S.append(cards('CASE / OPERATING CONTRACT / NTSB REPORT', 'What was the system allowed to do?', [
    ('AUTOPILOT', 'Assist steering + speed.', 'Autosteer and Traffic-Aware Cruise Control; driver must supervise.'),
    ('LIMITS', 'Not autonomous.', 'Tesla warned: keep hands on the wheel and be ready to take over.'),
    ('GAP', 'Activation != suitability.', 'Use was not restricted to intended conditions. ' + source('R2')),
], text_size=30, notes='NTSB HAR-20/01 pp. 12-15 describes the 2017 Tesla Model X Autopilot, a combination of traffic-aware cruise control and Autosteer. Tesla displayed a warning that Autosteer was driver assistance and did not make the vehicle autonomous, and urged attention and readiness to take over. The NTSB nevertheless found Tesla did not adequately restrict use to its intended operational design domain. Here "allowed" distinguishes what the software permitted from what its instructions recommended. Do not equate this 2018 configuration with a present vehicle or Full Self-Driving (Supervised). Source: ' + NTSB))
S.append(F.incident_map(NTSB))
S.append(F.stages('CASE / VEHICLE LOG / SECONDS BEFORE IMPACT', 'An invitation to intervene had a time limit.', [
    ('-5.9 S', 'Steering left.', 'Autosteer moved toward the painted gore. No driver torque detected.'),
    ('-3.9 S', 'Lead car lost.', 'Cruise control accelerated toward its preset 75 mph.'),
    ('APPROACH', 'No collision alert.', 'Forward warning and automatic braking did not activate.'),
    ('IMPACT', 'At ~71 mph.', 'Vehicle hit a damaged, nonoperational crash attenuator.'),
], '[NTSB report / pp. 5-6](' + NTSB + ') / seconds before impact, not reaction-time measurements.',
    'NTSB HAR-20/01 pp. 5-6 reports the downloaded vehicle log: Autosteer initiated a left input about 5.9 seconds before collision; the vehicle entered the gore, lost its lead car about 3.9 seconds before impact and accelerated toward a preset cruise speed of 75 mph. Forward collision warning and automatic emergency braking did not activate. The speed at impact was about 71 mph. No braking or evasive driver steering was recorded. This timeline is a selected reconstruction of the final seconds, not a test of an alternative interface or a judgment of the driver.'))
S.append(two_col('CASE / A WARNING IS NOT AN OVERRIDE TEST', 'Could oversight actually happen in time?', [
    'Tesla displayed warnings about supervision and hands on the wheel.',
    'NTSB: torque-based monitoring was ineffective; no alert in the final 60 seconds.',
    'No forward collision warning or automatic braking occurred on approach.',
], [
    'INVESTIGATE THE DESIGN',
    'What can the person perceive?',
    'How long can they respond?',
    'What can the system detect or prevent before a takeover?',
    source('R2'),
], right_font='body', left_size=32, right_size=31,
    notes='The NTSB pp. 14-15, 20, 40 and conclusions distinguish a label or warning from operationally meaningful supervision. Wheel torque is an imperfect proxy for engagement: absence of measured torque does not prove where hands were at every moment. Earlier visual and audible alerts occurred, but none in the final 60 seconds; the report found the timing and engagement monitoring ineffective. The vehicle could be overridden, yet an override required recognizing and responding during a rapidly developing hazard. The NTSB also found the collision avoidance functions were not designed to detect this attenuator. The takeaway is not "driver at fault therefore design absolved" or its converse.'))
S.append(F.stages('CASE / RESPONSIBILITY MAP / INVESTIGATION VS DESIGN',
    'An accident has more than one control point.', [
    ('DRIVER', 'Supervise + intervene.', 'NTSB found likely distraction and overreliance. Not sole cause.'),
    ('TESLA', 'Set system limits.', 'Steering, sensing and monitoring design shaped the exposure.'),
    ('ROAD', 'Maintain protection.', 'Damaged attenuator increased severity; agencies had duties.'),
    ('REGULATOR', 'Set oversight.', 'NTSB called for stronger evaluation and driver-monitoring standards.'),
    ], '[NTSB report / pp. ix-xi, 58-59](' + NTSB + ') / roles differ; this is not a liability verdict.',
    'The NTSB probable-cause statement includes Autopilot steering into a gore due to system limitations and the driver lack of response associated with likely distraction and overreliance. The ineffective driver-engagement monitoring contributed to the crash. The unrepaired damaged attenuator contributed to injury severity; the report also discussed reporting and maintenance failures and federal oversight. These are not interchangeable assignments of legal fault. Do not blame the victim, erase the driver duty, or claim that software alone explains the injury outcome. Ask who could change each control point.'))
S.append(content('CASE / EVIDENCE AND PROCEDURE', 'Investigation is not a civil verdict.', [
    '2020 NTSB: causal findings and safety recommendations. ' + source('R2'),
    "April 2024: reports of a settlement in the family's civil lawsuit. " + source('R3'),
    'The settlement terms were not disclosed; no jury finding from that case.',
    "Do not treat allegations, Tesla's defence or later software as NTSB findings.",
], body_size=32, notes='NTSB HAR-20/01 was adopted in 2020 and states probable cause and recommendations, not court liability. Guardian/Reuters reporting dated 8 April 2024 describes a settlement of the wrongful death suit just before trial; terms were not disclosed. The family claims and Tesla responses are adversarial positions, not established findings. This source check did not obtain the civil docket or independently verify a subsequent procedural change as of 12 November 2026. State the last source-checked procedural report as 8 April 2024; no later court docket was checked. Do not claim a 2026 active proceeding, jury verdict or settlement admission. Avoid implying that later Autopilot updates applied to the crash vehicle.'))
S.append(cards('CASE / DESIGN COUNTERFACTUALS / NOT TESTED HERE', 'Control before, during and after.', [
    ('BEFORE', 'Limit activation.', 'Check road suitability, not only whether lane marks are visible.'),
    ('DURING', 'Monitor engagement.', 'Warn in time or move toward a safe fallback when attention is uncertain.'),
    ('AFTER', 'Review and repair.', 'Keep records and a route to investigate failures. ' + source('R2')),
], text_size=31, notes='These three design alternatives are illustrative hypotheses, not retroactive proof that a specific feature would have prevented the 2018 crash. NTSB recommended operational-design safeguards and more effective driver monitoring, but safe fallback design must be tested for this context. Activation gating can wrongly exclude usable cases; more alerts can be missed; a false sense of security can persist. Recording data raises privacy and accountability questions. A product should articulate evidence for the particular permission it grants, and provide contestation and investigation when a failure occurs. This translates to recommender and booking systems too.'))
S.append(section('02 / EVIDENCE FOR RELIANCE', 'What warrants\nthe next step?', 'One bounded study + project transfer / 40-65 min', bg='#246E70',
    notes='Use one empirical study, Cecil et al. (2024), to shift from a specific transport incident to a controlled test of erroneous advice. These settings are not interchangeable: the crash cannot estimate effects of an explanation in recruitment, and the CV experiment cannot estimate crash risk. The task/comparison and figure pair occupy the same 25-minute block as the bounded design questions. Do not add a new four-paper lecture or require any additional reading.'))
S.extend(F.paper_pair('40-65 / R1 / EXPERIMENTS', 'An explanation did not fix wrong advice here.',
    [('cecil-fig6a.png', 180, 340, 860, 420)], source('R1'),
    'Cecil et al. / Fig. 6a / Exp. 2a / PDF p. 9 / crop / CC BY 4.0',
    'Cecil et al. (2024), published open primary study: five German online experiments, total N 1,403; immediate suitability decisions on 16 fictional CVs per person against strict criteria. No real hiring. Advice was approximately 75 percent correct; conditions included no advice, advice and explanations such as heatmaps or criterion charts. Figure 6a is only Experiment 2a: 328 participants overall, 214 advice recipients in the regression. Blue and pink bars group correct versus incorrect advice; orange and green bars group explanation versus no explanation across correct and incorrect trials. Four bars are two pooled contrasts, not four arms. Dashed no-advice baseline 70.61 percent; error bars are standard errors. Tested explanations did not clearly reduce reliance on wrong advice. A nonsignificant difference is not evidence that all explanations are equivalent. Read the axes first. Source: ' + CECIL,
    'Y = % correct CV decisions. Two pooled contrasts, not four arms; dashed line = 70.61% baseline.'))
S.append(content('STUDY -> PROJECT / FICTIONAL SIMULATION', 'Can someone reject an incorrect suggestion?', [
    'Room C has 8 seats. Your group has 12. A card says: "Choose Room C."',
    'Can a reviewer find the capacity rule and refuse the suggestion?',
    'Record their choice and evidence separately from their confidence.',
    'One peer walkthrough is not evidence of long-term safety or access.',
], body_size=34, notes='This classroom room-capacity card is an invented teaching simulation, not one of Cecil et al. trial stimuli. No real booking or evaluation of students takes place. In the study, participants made suitability decisions on fictional CVs against strict criteria; the outcome was immediate task accuracy. Here, reviewers see an intentionally wrong suggestion and can inspect a visible rule. Whether they reject it helps uncover a possible interface problem, not measure general trust, demonstrate calibrated reliance or test any deployed safeguard. Transfer to static controls, a visual recommendation or a physical product without inventing a chatbot.'))
S.append(cards('RELIANCE / A CLAIM NEEDS A SCOPE', 'Ask what each kind of evidence can support.', [
    ('CASE', 'Investigate failure.', 'A documented incident shows interacting failure paths, not a population rate.'),
    ('STUDY', 'Measure a task.', 'A fictional CV experiment shows immediate decisions, not all products.'),
    ('TEAM', 'Test a boundary.', 'A paper walkthrough finds confusion, not deployment validation.'),
], text_size=31, notes='The evidence sources answer different questions. A safety investigation reconstructs a particular event and identifies contributing conditions. Cecil et al. test immediate decisions with manipulated advice on fictional CVs. A team walkthrough after the break supplies first-use observations about a proposed design. Do not turn any of these into a general safety guarantee. Ask a team to name the specific person, task, risk, comparison and evidence gap before claiming that the person can safely rely on the system. This is the bridge into the worked revision.'))
S.append(content('65-75 / FICTIONAL PRODUCT / TWO PERMISSION BOUNDARIES', 'Same goal. Different authority.', [
    'A: "I found the best room and booked it." Evidence and consent are hidden.',
    'B: "Two rooms match the stated needs. Check capacity before you book."',
    'Show the rule, an accessible alternative and what happens on Confirm or Cancel.',
    'B is a hypothesis to test, not a proven safety solution.',
], body_size=33, notes='This is a controlled classroom comparison of two imaginary room-booking screens. No booking occurs. A hides both the ranking basis and permission to change a record; B keeps the choice and action inspectable. It may still fail if the timetable is wrong, the information is inaccessible or the person confirms without understanding. Ask teams which evidence would disconfirm their own boundary. The same test can be done on a non-chatbot display, classifier or installation. Keep this example to about four minutes inside the ten-minute pre-break bridge.'))
S.append(content('EXISTING GROUP PROJECT / 40% / NOT A NEW BRIEF', 'Review the project you already owe.', [
    'A0 poster: research and concept. 3-5 minute video: how it works.',
    'One-page mediation brief: relation, data, bias and guardrails.',
    'Rubric: research 30%; ethical/social impact 30%; poster communication 20%.',
    'Video 10%; collaboration/process documentation 10%. Check syllabus and Canvas.',
], body_size=33, notes='Existing course project only: A0 poster, three-to-five minute video and one-page mediation brief together comprise forty percent of the course. The five component percentages are within that project, not additional course weights. No deadline moves and no new submission is introduced. The Week 12 readiness milestone remains subject to actual Canvas instructions. Week 13 is quiz and posters with no new theory; do not announce invented quiz details. Leave enough time for the mock review of already available materials.'))
S.append(content('FORMATIVE REVIEW / AFTER THE BREAK', 'Can the work speak without an oral rescue?', [
    'Bring existing poster/concept layout, video or storyboard and brief draft.',
    'Readable paper and static screens are complete alternatives; printing is not required.',
    'Review in paired teams and swap roles. Share one strength and one revision.',
    'No new mark, upload or public sharing. Keep feedback in team notes.',
], body_size=34, notes='Brief the existing studio practice before the break. A digital or paper concept board can support feedback if the final poster is not ready; this does not waive project readiness. A storyboard can replace a video for discussion, but does not test playback or sound. Pair teams according to actual room conditions; do not assume fixed visitors, four groups or compulsory printing. Protect personal and student work: no new collection or public display beyond the team\'s own chosen review.'))
S.append(statement('Break.\nFifteen minutes.', eyebrow_text='75-90 / NEXT: WALKTHROUGH -> MOCK REVIEW -> REVISION', bg=PAPER, size=112,
    notes='Keep all fifteen minutes. Resume at relative minute ninety. No third-party action or registration is required during the break. Facilitators can check accessibility, room pairing, display and local materials. If the network or projector fails, use paper prompts and the prepared examples. Do not cut the practice blocks to repair an optional tool. Keep the class clock visible.'))
S.append(activity('01 / INTERFACE WALKTHROUGH', 30, 'Walk through three low-risk situations.', [
    '0-5: choose ordinary, ambiguous and out-of-scope scenarios for your actual product.',
    '5-20: a reviewer walks through paper/static screens; a teammate plays the system.',
    '20-25: record what they did, expected and could not understand.',
    '25-30: revise one claim, control or fallback. Label all scripted output SIMULATION.',
], notes='Relative 90-120, exactly thirty minutes. Roles: reviewer, interface/system operator and observer; combine roles if needed without inventing team requirements. Three scenarios, not three additional deliverables. Every project is valid, including classifiers, recommenders, physical objects and installations. Show the AI decision and controls around it; do not add a chatbot just for this exercise. Use fictional inputs only. No third-party actions, accounts, bookings, purchases or private data. Paper cards and static screens are the full workflow, not a second-rate fallback. The simulated behavior says what the team intends, not what an unbuilt model can do. Keep observations in private team working notes.'))
S.append(content('WALKTHROUGH / LEAVE UP DURING MINUTES 5-20', 'Show the next action. Do not explain it away.', [
    'Reviewer: "What is this allowed to do? What will happen if I continue?"',
    'Operator: show the prepared screen/card. Do not improvise a hidden capability.',
    'Observer: note the visible choice, evidence inspected, confusion and available refusal.',
    'Check access without disability simulation. A future test needs affected participants.',
], body_size=34, notes='This slide is a reference during the existing thirty-minute timer, not another timed exercise. Avoid coaching a reviewer toward the intended answer; a confused first impression is useful evidence. Label each response generated, scripted or manually simulated; if a live prototype is used, it must remain local/read-only with fictional data. Do not pretend that a manual intervention is automation. Screen-reader compatibility, keyboard access, tactile feedback and cognitive accessibility require appropriate evaluation; a sighted peer is not a substitute for BLV participants. Record actual behavior separately from the team\'s inferred cause.'))
S.append(two_col('WALKTHROUGH / MINUTES 20-30', 'One observation. One bounded revision.', [
    'OBSERVED: "The reviewer continued without noticing the room capacity."',
    'INTERPRETATION: "The evidence may have been too hard to find."',
    'REVISION: "Place capacity beside the proposed action and retain refusal."',
], [
    'EVIDENCE LIMIT',
    'One peer walkthrough does not prove safety, usability or calibrated reliance.',
    'NEXT TEST',
    'Who needs to evaluate this, in which setting, against what alternative?',
], right_font='body', left_size=32, right_size=31,
    notes='Instructor-authored example, not an observation from this class. Spend the final ten minutes of the same thirty-minute block comparing notes and changing one element. Keep alternative explanations: a reviewer may be hurried, understand capacity differently or simply overlook a field. An additional label can create more clutter. A rejected erroneous recommendation does not establish long-term performance. Preserve uncertainty visibly in the team\'s working record; no upload or study report is required. Transition promptly at relative 120 to the mock review.'))

S.append(activity('02 / FORMATIVE MOCK REVIEW', 35, 'Paired review. Then swap roles.', [
    '0-3: pair teams and open existing materials. Choose readable paper or screens.',
    '3-15: Team A reviews B. 15-27: swap. Begin each turn with silent looking.',
    '27-35: discuss one strength, one specific revision and one unresolved question each.',
    'Use poster, video/storyboard and brief. Feedback stays with the team; no new submission.',
], notes='Relative 120-155: three minutes setup, twelve minutes each direction, eight minutes synthesis = thirty-five. Within each twelve-minute turn: three minutes silent poster inspection, four tracing evidence/ethics, five video-or-storyboard/brief and clarification. This is formative, not a new grading scheme, compulsory print or fixed four-group rotation. Use a readable digital crop or paper board if A0 cannot be displayed. If team counts are odd, use a small local cluster while preserving equivalent review time and access. Do not promise anonymous collection or post work publicly. Facilitator observes and supports; no grade prediction.'))
S.append(content('MOCK REVIEW / FIRST THREE MINUTES OF EACH TURN', 'Read the poster before the pitch.', [
    'What is the product, for whom, and what does the AI decide during use?',
    'Which benefit is claimed? Which part is built, simulated or still proposed?',
    'Which research supports that claim, and what does it not establish?',
    'Only then ask the authors what you misunderstood. Note the communication gap.',
], body_size=35, notes='Use within each twelve-minute turn, not extra time. Start with silent looking or an accessible equivalent such as the poster\'s structured text readout. Let the reviewer state the concept before the authors pitch it. If the poster is not ready, a concept board is enough for feedback, but that does not waive the existing readiness milestone. Ask for an actual source passage if available; metadata or an attractive chart is not the same as a verified result. Distinguish a conceptual capability claim from evidence of a working system.'))
S.append(content('MOCK REVIEW / TRACE A CLAIM AND A CONSEQUENCE', 'Who benefits? Who can challenge it?', [
    'Trace one product claim to a credible source and its task, population and limit.',
    'Name affected people and competing values: include a person who is not the user.',
    'Trace one risk to a proposed response, contestation route and accountable role.',
    'What evidence could show that the response fails? Do not award safety for a disclaimer.',
], body_size=34, notes='Four minutes within each review turn. Connect to the existing research/context and ethical/sociological rubric, without converting these prompts into extra marked sections or mandatory sources. Ask whether a proposed privacy benefit simply transfers exposure from helpers to providers; a convenient control might be inaccessible or ineffective. If a team cites Cecil or a source from an earlier week, insist on its bounded outcome rather than a headline. Teams can disagree about a value trade-off while still giving a specific evidence-based argument. No real personal data is needed.'))
S.append(content('MOCK REVIEW / VIDEO + ONE-PAGE BRIEF', 'Does the same product appear in all three?', [
    'Video/storyboard: can you follow the person, AI decision and consequence?',
    'Brief: do the relation, data, bias and guardrails match the poster and video?',
    'Can you see who selected outputs, set boundaries and contributed to the work?',
    'Record one strength and one specific revision. Distinguish content from untested playback.',
], body_size=34, notes='Five minutes within each twelve-minute turn, then eight minutes joint synthesis as specified on the mock-review activity slide. Existing final video length remains three to five minutes; review only a selected segment or storyboard if needed to fit this turn, without changing the final requirement. Storyboards do not establish runtime or sound quality. Retain historical authorship questions from PDF65-66 as process disclosure and accountable curation, not unsupported legal conclusions about ownership. Acknowledge inputs and permissions accurately; do not infer copyright from authorship feelings. Collaboration remains part of the existing rubric.'))

S.append(activity('03 / REVISION', 20, 'Choose the change that matters most.', [
    '0-5: compare the walkthrough and mock-review notes. Keep disagreement visible.',
    '5-15: make one essential correction to a claim, boundary, control or explanation.',
    '15-20: identify the next evidence gap and one communication improvement.',
    'Record who will act in your team notes. No new deadline, grade or upload.',
], notes='Relative 155-175, exactly twenty minutes. The correction should be feasible now, such as narrowing an unsupported benefit, showing a real refusal path, making an alternative reachable or clarifying simulation. Do not demand a full rebuild of the model in ten minutes. Prioritize possible harm and misleading claims before decorative polish. An evidence gap may remain unresolved; honest scope is better than a fabricated citation or claimed user test. Assign a team action owner voluntarily in working notes, not a new formal submission. Protect the existing assessment components and Canvas instructions.'))
S.append(content('REVISION / LEAVE UP DURING THE SAME 20 MINUTES', 'A stronger claim can be a narrower claim.', [
    'Instead of "safe for everyone": state the intended setting and known exclusions.',
    'Instead of "the explanation builds trust": say what the person can check or challenge.',
    'Instead of "privacy solved": state what is processed, where it goes and what is untested.',
    'Instead of "users understood": report who tried what, what happened and what remains unknown.',
], body_size=34, notes='Reference during the revision activity\'s twenty minutes, not a second activity. These are wording principles, not templates for making untested guarantees sound acceptable. A narrower claim must still be true. If no real participant test occurred, say peer walkthrough or simulation, not user validation. If the data-processing route is not implemented, state it as proposed. Record contradictions between materials before improving layout. Explain the difference between tool verification, observed behavior and human acceptance. Leave five minutes at the end of class for the final question.'))
S.append(question('short_answer', 'What will you change - and who can contest the result?',
    hint='Name one revision, the evidence behind it and an accountable role. What remains uncertain?',
    eyebrow_text='175-180 / TEAM NOTES, ORAL SHARE OR CLASSPOINT',
    notes='Close within five minutes. Invite one or two brief answers, not presentations by all teams. Optional ClassPoint/oral/team-note routes are equivalent; no new assessed submission. End with the existing project: A0 poster, three-to-five-minute video and one-page brief, forty percent. Check actual Canvas instructions and the existing Week 12 readiness milestone; do not announce a new deadline. Week 13 is the confirmed quiz and poster session; do not invent its quiz format, duration or questions. Confirm room/teams/access/display and feedback arrangements separately, not from the old 2025 fair instructions. Our synthesis: the designer curates evidence and possibilities, sets meaningful boundaries and remains answerable for what the product invites people to rely on.'))

S.append(content('REFERENCE SHELF / PRIMARY INVESTIGATION', 'NTSB / case evidence', [
    '2017 Model X P100D / Autopilot: Traffic-Aware Cruise Control + Autosteer.',
    '23 March 2018 Mountain View; NTSB HAR-20/01 (2020), pp. ix-xi, 5-6, 12-16, 20, 40, 58-59.',
    source('R2'),
    'Civil settlement reported 8 April 2024; undisclosed terms, no jury verdict in that case. ' + source('R3'),
], body_size=32, notes='Untimed optional source shelf. The NTSB is the primary causal investigation and is not a court ruling. It identifies interacting system limitations, likely driver distraction/overreliance, ineffective engagement monitoring, and damaged road hardware affecting injury severity. The final-second sequence is from the vehicle log; the civil disposition is separately reported by Guardian/Reuters as of 8 April 2024, not independently checked against later docket entries. Do not turn the settlement into an admission of liability. Distinguish the 2018 Autopilot configuration from Full Self-Driving (Supervised) and current versions.'))
S.append(content('REFERENCE SHELF / EXPERIMENT', 'Cecil et al. / task and limits', [
    'Cecil, Lermer, Hudecek, Sauer & Gaube (2024). Explainability does not mitigate the negative impact of incorrect AI advice in a personnel selection task.',
    'Scientific Reports 14, 9736. ' + source('R1'),
    'Five experiments, 1,403 participants; 16 fictional CV decisions per participant.',
    'Wrong advice reduced trial accuracy; the tested explanations did not clearly fix it. No real hiring.',
], body_size=29, notes='Untimed primary-source shelf; not a newly compulsory reading. The publisher open article was consulted by the earlier Week 12 draft and the retained figure crop is CC BY 4.0, see asset provenance. Results refer to specified tasks, correctness, comparison and measurement; confidence and perceived quality are separate outcomes. The figure shown in the timed block is Experiment 2a, not a pooled five-study statistic. No universal claim that explanations never help. Other former Week 12 paper sources are removed from this timed route to give the case and coherent theoretical argument room.'))
TIMING = [(0, 10, 1, 3, 'Reconnect'), (10, 40, 4, 15, 'Delegation / Autopilot case'), (40, 65, 16, 20, 'Evidence for reliance'), (65, 75, 21, 23, 'Evidence to revision'), (75, 90, 24, 24, 'Break'), (90, 120, 25, 27, 'Interface walkthrough'), (120, 155, 28, 31, 'Mock review'), (155, 175, 32, 33, 'Revision'), (175, 180, 34, 34, 'Close')]





attach_reports(S, Path(__file__).resolve().parent / 'week12-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 12', slides=finalize(S, footer(12)), pdf='SD2112-week12.pdf')
