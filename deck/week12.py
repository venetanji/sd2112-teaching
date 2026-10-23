"""Week 12: calibrated reliance, accessible privacy and formative mock review."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, PAPER
from deckgen.layouts import (title, content, cards, two_col, statement, question,
                             activity, section, finalize)
from course import footer
import week12_figures as F

S = []
REFS = {
    'R1': ('Cecil et al., Scientific Reports, 2024', 'https://doi.org/10.1038/s41598-024-60220-5'),
    'R2': ('Sharma et al., ASSETS, 2025', 'https://doi.org/10.1145/3663547.3746335'),
    'R2v': ('Sharma et al., consulted author preprint v2', 'https://arxiv.org/html/2507.00286v2'),
    'R3': ('Yao et al., ReAct: Synergizing Reasoning and Acting in Language Models, ICLR 2023', 'https://arxiv.org/abs/2210.03629v3'),
    'R4': ('Mitchell et al., Model Cards for Model Reporting, FAT* 2019', 'https://arxiv.org/abs/1810.03993v2'),
}
TIMING = [
    (0, 10, 1, 3, 'Reconnect'),
    (10, 40, 4, 13, '01 / What are we delegating?'),
    (40, 65, 14, 22, '02 / What may people rely on?'),
    (65, 75, 23, 26, '03 / Turn evidence into a revision'),
    (75, 90, 27, 27, 'Break'),
    (90, 120, 28, 30, 'Interface walkthrough'),
    (120, 155, 31, 34, 'Mock review'),
    (155, 175, 35, 36, 'Revision'),
    (175, 180, 37, 37, 'Close'),
]


def source(key):
    label, url = REFS[key]
    return f'[{key} / {label}]({url})'


S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 12',
    'Trust is not\nthe target.', 'Ethics II: what may a person rely on, delegate and contest?',
    notes='Main route: slides 1-37, exactly 180 minutes including a full fifteen-minute break. Slides 38-42 are the reference shelf, not extra lecture time or new reading assignments. Reconnect to research and curation from Week 11, the human-technology relation from Week 5 and Week 8, and the existing project. Do not repeat the empathy/sycophancy lecture. Today is about justified reliance in a particular task and responsibility for consequential decisions. Chatbots are one example, not a requirement. Explain that a paper prototype is enough throughout; do not open accounts or activate real actions.'))
S.append(content('0-10 / TODAY / 180 MINUTES', 'Evidence -> boundary -> revision.', [
    '0-75: rules, delegation, calibrated reliance and accessible privacy.',
    '75-90: break. 90-120: interface walkthrough, 30 minutes.',
    '120-155: formative mock review, 35 minutes. 155-175: revision, 20 minutes.',
    '175-180: share one decision and one open question. No new submission today.',
], body_size=33, notes='Use relative minutes, not an invented room timetable. If late, shorten lecture detail or the optional reference shelf, not the break or the three protected activities. Keep teams and existing project materials. The two brief reflective questions can be discussed orally or in team notes; optional ClassPoint supports discussion but does not create an additional assessed artifact. Confirm add-in/report privacy settings before class. The classroom exercise is formative and does not move any existing deadline.'))
S.append(question('short_answer', 'What should a person NOT delegate to your product?',
    hint='Name the person, a consequential choice and the evidence you would need before allowing it.',
    eyebrow_text='0-10 / DISCUSS / TEAM NOTES OR CLASSPOINT',
    notes='Allow three minutes within the opening ten. Ask for a task-specific boundary, not a blanket declaration that AI is good or bad. A recommender might rank possibilities while the person chooses; an installation might adapt light while an operator sets a safe limit. Invite one example and its affected people. No sensitive experience or student work needs to be displayed. Oral/team-note fallback is complete; ClassPoint is optional, not a new graded submission. If used, do not promise anonymity: default named activity; do not publish private responses. Later report links must follow the course withholding policy.'))

S.append(section('01 / DELEGATION', 'What are we\ndelegating?', 'Answers, actions and permission / 10-40 min', bg="#246E70", notes='Topic signpost inside the existing thirty-minute teaching block, not extra lecture time. Move from the opening question to one fictional workshop-slot example: rule filtering, learned interpretation and an externally executed action. ReAct will provide one authentic source excerpt for the action-observation mechanism, with a standalone account requiring no prior reading. Our native harness diagram then separates that mechanism from our proposed permission boundary. Protect the later activities; do not turn this synthesis week into a benchmark lecture.'))
S.append(cards('10-40 / ONE REQUEST / THREE IMPLEMENTATIONS', '"Find an available workshop slot."', [
    ('MACHINE A', 'Filter written rules.', 'Read a fictional timetable. Return slots matching room capacity and a stated time range.'),
    ('MACHINE B', 'Interpret language.', 'Turn a vague request into a proposed time and explanation. The proposal may be wrong.'),
    ('A + B', 'Interpret, then check.', 'Use learned interpretation with explicit availability checks. Keep booking a separate permission.'),
], text_size=30, notes='Instructor-authored fictional example, not a product evaluation. Use one request across all three routes, retaining the established course Machine A/B labels. Rules can be wrong or incomplete; a learned response can be correct. The distinction is written procedure versus learned patterns, not safe versus unsafe. Separate searching an authoritative timetable from generating a plausible answer. A hybrid needs evidence that its checks actually run. The user has not yet authorized a booking. Ask what the ambiguous word "available" might hide: access needs, eligibility, location or cost. About three minutes.'))
S.append(two_col('DELEGATION / ANSWERING IS NOT ACTING', 'A sentence can become a commitment.', [
    '"Room C looks suitable." An answer proposes a choice.',
    '"I reserved Room C." A tool action changes a record.',
    'Reading a private timetable can disclose information even without changing it.',
], [
    'ASK BEFORE DELEGATING',
    'What authority does this request give?',
    'Which people and records are affected?',
    'What can be refused, corrected or recovered?',
], right_font='body', left_size=33, right_size=32,
    notes='These are illustrative statements, not live tool results. A generated success message is not evidence that a booking happened. Read operations are not automatically harmless: they can expose private data or create a log. Introduce delegation as a limited grant of authority, not surrender of responsibility. In a non-chatbot concept, the same issue appears when a classifier automatically denies entry or an adaptive object changes the environment. Ask which step would need a different permission. About three minutes.'))
S.extend(F.paper_pair('R3 / REACT / MECHANISM RECAP', 'An observation can change the next step.',
    [('react-fig1-search.png', 120, 350, 990, 405)],
    source('R3'), 'Yao et al. / ReAct v3 / Fig. 1(1d), first cycle / PDF p. 2 / crop',
    'Yao et al., ReAct, ICLR 2023, exact arXiv:2210.03629v3, PDF page 2, Figure 1(1d), first Thought/Act/Obs cycle. Read the question at the top: which other device controls the program originally controlled by Apple Remote? The generated action searches Apple Remote; the returned observation names Front Row. That observation supplies evidence for a later search, rather than an answer being accepted simply because it sounds fluent. This crop deliberately omits later cycles and benchmark scores; it is an authentic published example trace, not a live system or a faithful window into hidden cognition. Sections 2-4 compare benchmark methods, but no benchmark success generalization or quantitative performance claim is taught. Our following editable harness figure adds an explicit permission check not validated by this paper. Use about two minutes, trimming earlier verbal examples to keep the whole block thirty minutes. No additional reading is required.', 'Read downward: generated Thought -> Search action -> returned evidence. The observation is not another model guess.'))
S.append(F.agent_loop())
S.append(cards('DESIGN HYPOTHESIS / NOT A SAFETY CERTIFICATE', 'Make permission specific.', [
    ('BEFORE', 'Preview the scope.', 'Show the record, recipient, cost and exact action. Offer a read-only route.'),
    ('DURING', 'Approve this step.', 'Make refusal possible. Avoid treating silence or a broad goal as unlimited consent.'),
    ('AFTER', 'Show what happened.', 'Check the actual result. Provide a recovery route; say when undo is impossible.'),
], text_size=31, notes='Our normative design questions, not experimentally validated remedies. A confirmation dialog can be ignored, inaccessible or manipulative; its presence alone does not establish informed control. An undo button may not retract a sent message, recover a disclosure or reverse a denied opportunity. Distinguish prevention, detection and repair. In the workshop, teams must show the failure state rather than add a generic "AI may be wrong" disclaimer. A responsible organization still needs an accountable owner and usable appeal route. About four minutes.'))
S.append(two_col('MEDIATION / OUR WORKING DESIGN DISTINCTION', 'Easy to use. Hard to see through.', [
    'A smooth interface can recede while you get something done.',
    'Its data sources, incentives and consequences may still remain hidden.',
    'Ask both: what effort disappears, and what choice disappears with it?',
], [
    'MAKE THE CONSEQUENCE VISIBLE',
    'A fluent reply does not verify a fact.',
    'A rationale does not verify the outcome.',
    'A visible control does not verify usable access.',
], right_font='body', left_size=33, right_size=32,
    notes='This is our working distinction for interface analysis, continuous with the established course mediation vocabulary, not a quotation or a new attribution to Van Den Eede. The syllabus lists Van Den Eede (2011) as core reading; its full text was not newly obtained for this pass, so no detailed claim about his argument is made. Do not confuse experiential transparency (getting on with an activity) with disclosure of provenance, mechanisms or effects. Use a timetable recommender: one effortless choice can hide a ranking policy or inaccessible venue. Invite disagreement about which friction is useful. About four minutes.'))
S.append(content('LANGUAGE AS INTERFACE / THE GOAL STILL MATTERS', 'A better prompt is not the whole design.', [
    'Let the person inspect and change what the system thinks they want.',
    'Make alternatives reachable without finding the right words.',
    'Keep controls, labels and feedback usable for people who do not use chat.',
    'A physical product, recommender or visual system is equally valid here.',
], body_size=35, notes='Reconnect to historical 2025 PDF55-63: language as interface and designers as curators. Replace the "ultimate user interface" slogan with a question about who can express, correct and refuse a goal. We do not reproduce the historical Ihde (1993) language claim or its notation without a verified primary passage. A prompt-only interface can require linguistic skill and hide available operations. The design is the whole mediated relation, including defaults and other people, not simply a prompt wrapper. Do not require teams to add a chatbot. About four minutes.'))
S.append(cards('ACCOUNTABILITY / OUR ETHICAL ARGUMENT', 'Delegation does not erase responsibility.', [
    ('AFFECTED PEOPLE', 'Who bears failure?', 'Include non-users, helpers, bystanders and people represented in data - not just the buyer.'),
    ('CONTESTABILITY', 'Who can challenge it?', 'Show a route to question the data, correct an outcome and reach a responsible person.'),
    ('ACCOUNTABLE OWNER', 'Who must respond?', 'Name an operational role able to investigate and repair. "The AI decided" is not an answer.'),
], text_size=30, notes='This is the course design argument, not a legal conclusion or a universal assignment of liability. Keep conflicting values explicit: independence, privacy, accuracy, dignity, access, efficiency. The developer, provider and deploying organization may have different powers; a team should identify who can actually change a result, not merely who receives a complaint. A human in the loop is inadequate if they lack time, authority or evidence. End the 10-40 block by asking where a fictional failed reservation would be contested and which role could fix it. About six minutes including discussion.'))

S.append(section('02 / RELIANCE + ACCESS', 'What may people\nrely on?', 'Accuracy, independence and privacy / 40-65 min', bg="#246E70", notes='Topic signpost within the existing twenty-five-minute block. The two empirical papers ask different questions: Cecil tests immediate decisions with correct or incorrect advice; Sharma interviews blind and low-vision GenAI users about visual privacy. Do not combine them as if they measured the same outcome. The summaries and authentic source excerpts give everything needed for this discussion without pre-reading. Translate each bounded finding into a design question, then label the proposed response as ours, not a validated remedy.'))
S.extend(F.paper_pair('40-65 / R1 / EXPERIMENTS', 'An explanation did not fix wrong advice here.',
    [('cecil-fig6a.png', 180, 340, 860, 420)],
    source('R1'), 'Cecil et al. / Fig. 6a: Exp. 2a, N328 (214 advice recipients) / PDF p. 9 / crop / CC BY 4.0',
    'Cecil, Lermer, Hudecek, Sauer and Gaube (2024), published full text, General procedure, Experiments 1a/1b/2a/2b/2c, Tables 2-7 and Discussion/Limitations read. Samples: 370, 242, 328, 143, 320 = 1,403. Each participant screened 16 fictional two-page CVs against strict criteria; half were eligible. Advice was purported human/AI prescreening, generally 75% correct, not a live deployed recruiter. No-advice controls; source manipulated in 1a/b and visual explanation in 2a-c. 2b removed time limits; 2c used criterion bar charts. Wrong-advice trials performed worse than baseline, not a universal overall harm from having any advice. Explanation effects on ratings/confidence varied; the tested explanations did not significantly improve task accuracy or reduce wrong-advice reliance. No consequences for actual applicants. Supplements/preregistrations not independently audited. About five minutes. Figure-led explanation: published PDF page 9, Figure 6a, Experiment 2a (328 students overall; 214 in advice groups for the regression). This single panel is not a pooled estimate across all five experiments. First compare blue Correct with magenta Incorrect: these pool the two explanation conditions and distinguish advice accuracy. Then compare orange Non-Expl and green Expl: these pool correct and incorrect advice and distinguish explanation conditions. These are two different contrasts, not four experimental arms. The dashed line is the no-advice baseline, 70.61%; error bars are standard errors. The similar orange/green bars alone do not establish equivalence; use the reported model and bounded nonsignificant result. Axis and original labels remain intact; native text explains the contrasts for mobile readers.', 'Y = % correct CV decisions (0-100%). Blue/pink pool explanation conditions; orange/green pool advice accuracy. Not four arms. Line = 70.61% baseline; bars = standard errors.'))
S.append(content('R1 -> PRODUCT QUESTION / TEACHING HYPOTHESIS', 'Test rejection of an error - not trust alone.', [
    'Use a fictional workshop rule: Room C has 8 seats; your group has 12.',
    'Scripted advice says: "Choose Room C: it is suitable." Label this SIMULATION.',
    'Can a reviewer find the conflict and refuse the suggestion? What did they inspect?',
    'Record the observed choice separately from confidence and your interpretation.',
], body_size=33, notes='Prepared low-stakes thought experiment, not a replication of Cecil et al. Show the capacity rule and incorrect advice together. Reveal deliberately wrong advice as part of the teaching setup, without deception, rankings of students or real personnel data. Invite a refusal and alternative. One correct rejection with the answer visible does not establish calibrated reliance in deployment; failures can still identify confusing evidence. Do not make a quantitative class comparison from a few volunteers or force a high-stakes decision. This transfer tests a possible interface failure, not whether explanations are universally helpful or harmful. About three minutes.'))
S.extend(F.paper_pair('R2 / INTERVIEWS / VISUAL PRIVACY', 'Private from a helper. Exposed to whom?',
    [('sharma-table1-columns.png', 120, 390, 990, 310)],
    source('R2v'), 'Sharma et al. / v2 Table 1 rows 3-5 / PDF p. 4 / joined column crops',
    "Sharma, Tseng, Zhang, Ide, Mack, Findlater, Gurari and Wang (2025), full author preprint arXiv v2, 19 July 2025, read sections 3-6 and interview appendix. Final ACM DOI is supplied for attribution; final typeset text was not compared. US sample of existing GenAI users, one-hour remote Zoom interviews Nov 2024-Jan 2025, scenario prompts across self-presentation, spaces, social sharing and professional documents. Fourteen totally blind, seven with some light perception. Recruitment and table contain an age-description mismatch: prose 25-54, table includes P12 18-24; no age range is taught. Practices vary: some prefer a trusted human for sensitive data. Findings are experiences and expectations, not prevalence, measured privacy improvement or current vendor-policy facts. Do not adopt participants' risky practices as recommended security. About five minutes. Source-image explanation: the exact v2 PDF contains no numbered figures, so use its authentic Table 1 on PDF page 4 rather than inventing a findings chart. Two column crops joined side by side at identical pixel scale preserve the scenario-name and privacy-type columns for rows 3-5; the middle definition column and unrelated rows are explicitly omitted; the caption identifies the two column excerpts, and row alignment is retained in both desktop and mobile. Read corresponding rows: social-media sharing concerns own and others privacy; sharing visual content concerns own privacy; professional documents concern others privacy. These are interview prompts/categories, not counts or prevalence findings. Findings in sections 4-5 supply the helper/provider/other-person tension summarized alongside the table. Native guidance repeats the privacy distinction so reading mode does not depend on reading small image text.", 'Table 1 prompts, not findings: social sharing = own + others; personal document = own; professional documents = others. Middle column omitted; rows stay aligned.',
    second_reading=source('R2')))
S.append(F.privacy_flow())
S.append(cards('BOUNDARIES / NOT ONLY A DISCLAIMER', 'Design the moment it should stop.', [
    ('ORDINARY', 'Enough evidence?', 'Show what supports this output and what the person can check.'),
    ('AMBIGUOUS', 'Need a clarification?', 'Do not quietly guess a consequential preference or disclose extra data.'),
    ('OUT OF SCOPE', 'A usable alternative?', 'Refuse clearly. Offer a lower-risk route or an accountable human, without promising availability.'),
], text_size=31, notes='These three scenario types become the walkthrough after the break. A classroom refusal message is a hypothesis, not proof that unsafe inputs cannot pass. Scope should name a setting or action, not vaguely say "not professional advice" while presenting a definitive diagnosis. For accessibility projects, ask whether the fallback imposes new dependence, cost or delay and whether refusal itself causes harm. For a generative installation, the boundary could be an operator limit rather than a text response. Do not collect personal health, identity, location or financial information. About four minutes.'))
S.append(content('ETHICS / MAKE THE REASONING VISIBLE', 'Name the trade-off - and who can contest it.', [
    'People: a BLV photo-sharer, a housemate in the background and the service operator.',
    'Values: independence and access can conflict with privacy and reliable interpretation.',
    'Choice: inspect, correct, refuse or use a trusted alternative; ask who cannot use that route.',
    'Accountability: the deploying service must offer an answerable role and a way to challenge harm.',
], body_size=33, notes='Worked normative argument using a fictional photo-sharing concept, not a finding that all participants held identical values. Explicitly name non-users rather than reducing ethics to individual consent. State the unresolved issue: a preview can miss private content, and refusing every uncertain image can undermine independence. There is no friction-free answer; choose and justify a proportionate boundary, then test it with affected people. A student sketch cannot prove privacy or accessibility. Ask teams to translate the argument to their own product with different people and values. Four minutes closes 40-65.'))

S.append(section('03 / REFLECTION -> REVISION', 'What will you\nchange?', 'Evidence -> walkthrough -> peer review -> revision / 65-180 min', bg="#246E70", notes='This signpost marks a change from discussing evidence to working on the project already required. Spend only a few seconds here inside the existing ten-minute worked-example and brief block. The source summaries are lenses, not a new reading list or safety checklist. Show one bounded design change and why it remains unvalidated, clarify the assessment contract, then protect the full fifteen-minute break and the thirty/thirty-five/twenty-minute activity budgets. No extra submission, criterion, deadline or final-quiz policy is introduced.'))
S.append(two_col('65-75 / WORKED COMPARISON / FICTIONAL PRODUCT', 'Same promise. A different contract.', [
    'A / "I found the best room and booked it for you."',
    'Hidden: the capacity rule, access needs, permission and recovery.',
    'A polished explanation can leave the person unable to challenge the choice.',
], [
    'B / "Two options match your stated needs. Check access details before choosing."',
    'Show evidence, limitations and the exact booking preview. Keep Cancel available.',
    'B is a hypothesis to test - not proven safer by this comparison.',
], right_font='body', left_size=32, right_size=31,
    notes='Do not present version B as experimentally validated. Ask what it improves and what remains unresolved: the timetable could be stale; an access field may be inaccurate; a user can confirm without understanding. In the classroom both variants are paper/static and scripted. Nothing is booked, charged, sent or shared. Transfer to a non-chatbot product by replacing the dialogue with recommendation labels, status displays or an operator control. Keep the user goal separate from the tool action. Four minutes.'))
S.append(content('EXISTING GROUP PROJECT / 40% / NOT A NEW BRIEF', 'Review the project you already owe.', [
    'A0 poster: research and concept. 3-5 minute video: how it works.',
    'One-page mediation brief: relation, data, bias and guardrails.',
    'Rubric: research 30%; ethical/social impact 30%; poster communication 20%.',
    'Video 10%; collaboration/process documentation 10%. Check the syllabus and Canvas.',
], body_size=33, notes='Current syllabus read in full. Forty percent is the project weight in the course; the five listed percentages are within that project rubric, not additional course weights. Preserve the A0 format, video duration and one-page brief. Week 12 final-poster/video readiness remains an existing syllabus milestone; this formative review does not cancel it, extend a deadline or introduce a new draft upload. The syllabus still lists a Week 13 final quiz but policy is unresolved: neither announce nor cancel it here. Actual Canvas instructions remain authoritative for operational details. Three minutes.'))
S.append(content('FORMATIVE REVIEW / AFTER THE BREAK', 'Can the work speak without an oral rescue?', [
    'Bring existing poster/concept layout, video or storyboard, and mediation-brief draft.',
    'Paper and readable static screens are complete alternatives; no printing requirement.',
    'Review in paired teams, then swap roles. Extra pairing only if time and room allow.',
    'One strength and one specific revision. No new mark, upload or public sharing.',
], body_size=34, notes='Brief all activities before the full break. Use existing material, not a prerequisite for a polished final artifact in the room. If a video cannot play, inspect a storyboard or frames and state that pacing/audio were not tested. Pair locally according to actual teams and access needs; no fixed four-group count or visitor schedule. Do not publish student names, draft images or comments. Three minutes completes the pre-break 75 minutes.'))
S.append(statement('Break.\nFifteen minutes.', eyebrow_text='75-90 / NEXT: INTERFACE WALKTHROUGH -> MOCK REVIEW -> REVISION',
    bg=PAPER, size=112,
    notes='Protect all fifteen minutes. Resume at relative minute 90. Students need no account setup, download or cloud task during the break. Facilitators check local readability, team pairing, accessible routes and a clock. No live third-party actions are permitted in this activity. If the projector or network fails, use paper prompts and the prepared notes; do not shorten the activity to troubleshoot an optional tool.'))

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
], body_size=34, notes='Four minutes within each review turn. Connect to the existing research/context and ethical/sociological rubric, without converting these prompts into extra marked sections or mandatory sources. Ask whether a proposed privacy benefit simply transfers exposure from helpers to providers; a convenient control might be inaccessible or ineffective. If the team cites Cecil or Sharma, insist on the bounded outcome rather than a headline. Teams can disagree about a value trade-off while still giving a specific evidence-based argument. No real personal data is needed.'))
S.append(content('MOCK REVIEW / VIDEO + ONE-PAGE BRIEF', 'Does the same product appear in all three?', [
    'Video/storyboard: can you follow the person, AI decision and consequence?',
    'Brief: do the relation, data, bias and guardrails match the poster and video?',
    'Can you see who selected outputs, set boundaries and contributed to the work?',
    'Record one strength and one specific revision. Distinguish content from untested playback.',
], body_size=34, notes='Five minutes within each twelve-minute turn, then eight minutes joint synthesis as specified on slide 31. Existing final video length remains three to five minutes; review only a selected segment or storyboard if needed to fit this turn, without changing the final requirement. Storyboards do not establish runtime or sound quality. Retain historical authorship questions from PDF65-66 as process disclosure and accountable curation, not unsupported legal conclusions about ownership. Acknowledge inputs and permissions accurately; do not infer copyright from authorship feelings. Collaboration remains part of the existing rubric.'))

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
], body_size=34, notes='Reference during slide 35\'s twenty minutes, not a second activity. These are wording principles, not templates for making untested guarantees sound acceptable. A narrower claim must still be true. If no real participant test occurred, say peer walkthrough or simulation, not user validation. If the data-processing route is not implemented, state it as proposed. Record contradictions between materials before improving layout. Explain the difference between tool verification, observed behavior and human acceptance. Leave five minutes at the end of class for the final question.'))
S.append(question('short_answer', 'What will you change - and who can contest the result?',
    hint='Name one revision, the evidence behind it and an accountable role. What remains uncertain?',
    eyebrow_text='175-180 / TEAM NOTES, ORAL SHARE OR CLASSPOINT',
    notes='Close within five minutes. Invite one or two brief answers, not presentations by all teams. Optional ClassPoint/oral/team-note routes are equivalent; no new assessed submission. End with the existing project: A0 poster, three-to-five-minute video and one-page brief, forty percent. Check actual Canvas instructions and the existing Week 12 readiness milestone; do not announce a new deadline. Instructor must reconcile Week 13 policy before announcing any final-quiz format or cancellation. Confirm room/teams/access/display and feedback arrangements separately, not from the old 2025 fair instructions. Our synthesis: the designer curates evidence and possibilities, sets meaningful boundaries and remains answerable for what the product invites people to rely on.'))

S.append(content('REFERENCE SHELF / R1 / FULL PRIMARY ARTICLE', 'Cecil et al. / evidence card', [
    'Cecil, J., Lermer, E., Hudecek, M. F. C., Sauer, J., & Gaube, S. (2024). Explainability does not mitigate the negative impact of incorrect AI advice in a personnel selection task.',
    'Scientific Reports, 14, 9736. ' + source('R1'),
    'Five experiments, N=1,403. Fictional CV screening; no-advice/source/explanation comparisons. Outcomes: accuracy, perceived advice quality, confidence.',
    'Read: Methods; Experiments 1a-2c; Tables 2-7; Discussion and Limitations. No real hiring consequences; strict selection rules.',
], body_size=29, notes='Optional reference shelf, outside the 180-minute main route. Access: publisher open full text read 21 October 2026; study materials and supplements linked but not independently reviewed or replicated. The paper describes five preregistered experiments; 1b/2b are replications not separately preregistered. Trial-level wrong advice versus no-advice baseline must not be confused with the often nonsignificant overall advice/no-advice comparisons. 2a explainable-advice overall comparison versus no advice was significant; that does not establish an explanation advantage over advice without explanation. No universal claim about explanation modalities. See evidence ledger for full denominators and transfer limits.'))
S.append(content('REFERENCE SHELF / R2 / VERSION AND ACCESS', 'Sharma et al. / evidence card', [
    'Sharma, T., Tseng, Y.-Y., Zhang, L., Ide, A., Mack, K. A., Findlater, L., Gurari, D., & Wang, Y. (2025). "Before, I Asked My Mom, Now I Ask ChatGPT": Visual Privacy Management with Generative AI for Blind and Low-Vision People.',
    'ASSETS 2025. ' + source('R2'),
    'Consulted full author manuscript: ' + source('R2v'),
    '21 US GenAI users; scenario-based remote interviews and thematic analysis. Read sections 3-6 and Appendix A.',
    'Experiences and preferences - not prevalence, comparative privacy gains or tested control efficacy.',
], body_size=28, notes='Optional reference shelf. Author preprint v2 dated 19 July 2025 has unfilled conference-template metadata; cite its arXiv version explicitly and the final DOI separately. We do not assert identity with the final typeset text. No intervention/comparator, no performance measure or follow-up trial. Participants describe varied and sometimes risky practices; these are not security recommendations or verified current product claims. The paper\'s own technical design suggestions are proposals, not implementations with proven guarantees. Sample of existing users in the US, not every BLV person. No full paper or participant material redistributed in the public repository.'))
S.extend(F.paper_pair('REFERENCE SHELF / R4 / DOCUMENTATION FRAMEWORK', 'Make the scope inspectable.',
    [('modelcards-fig1-use.png', 120, 340, 990, 220),
               ('modelcards-fig1-caveats.png', 120, 590, 990, 185)],
    source('R4'), 'Mitchell et al. / v2 Fig. 1 / PDF p. 3 / two separate excerpts',
    'Full primary author texts reviewed: ReAct arXiv v3 and Model Cards arXiv v2. Mechanism discussion uses ReAct sections 2-4, not a claim about current commercial agents or faithful hidden reasoning. Model Cards section 4 motivates documenting intended use, evaluation data, factors, limitations and recommendations. Our interface walkthrough is not itself a model card or deployment audit. No new report is required. Both links point at the exact consulted version. This is an optional documentation reminder, not an additional timed paper lecture or reading assignment. Authentic Figure 1 excerpts, exact arXiv v2 PDF page 3: Intended Use and the final Quantitative Analyses/Ethical Considerations/Caveats sections. Separate crops are labelled as excerpts; they do not reproduce a complete card. Read the out-of-scope line first, then the requirement to examine group-level and intersectional results. The conceptual contribution is a reporting framework with worked examples, not experimental evidence that documentation prevents harm. A card can be incomplete, inaccurate or ignored. Apply the questions to the existing mediation brief only; no model-card submission is assigned.', 'Name the intended user and out-of-scope uses. Ask which groups were evaluated and which caveats remain. No new report.'))
S.append(content('REFERENCE SHELF / CONTINUITY AND INSTRUCTOR DECISIONS', 'Carry forward the question - not old logistics.', [
    '2025 Week 12 PDF54-66: language, rules/data, curation, authorship. Reframed here as boundaries and accountable choices.',
    'PDF27 is a thought/action/observation loop; PDF29 is latent diffusion. Editable deck has 71 slides, PDF 70 pages.',
    'Core syllabus background: Van Den Eede (2011), In Between Us. [Reading record](https://doi.org/10.1007/s10699-010-9190-y). Full text not newly verified here.',
    'Instructor: confirm room/access/pairing, actual Canvas readiness instructions and Week 13 assessment policy before announcements.',
], body_size=29, notes='Optional instructor reference shelf. Historical PDF54-69 extracted and rendered; editable OneDrive deck compared by text. Its added Ask Me Anything slide at 54 shifts subsequent synthesis by one. Do not reuse the old fair board, date, four-group requirement, exam or Blackboard/printing instructions. Old PR3 is background only; no tooling/logistics copied. No contemporary incident, ELIZA-mechanism claim, legal ownership conclusion or unverified Ihde language quotation is used. New normative working distinctions are labelled as ours rather than attributed to an unread theory text. Current syllabus unchanged, including its unresolved Week 13 quiz item.'))

attach_reports(S, Path(__file__).resolve().parent / 'week12-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 12',
            slides=finalize(S, footer(12)), pdf='SD2112-week12.pdf')
