"""Week 13: showcase, evidence-led critique and course synthesis; logistics gated."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import title, content, cards, statement, section, end, finalize, T, Rect, _slide, eyebrow
from course import SITE, footer

SYLLABUS = 'https://github.com/venetanji/sd2112-teaching/blob/7596f50f620d5000ad32445ab3851aec29dc67da/syllabus/SD2112-syllabus-2026.md'
VERBEEK = 'https://doi.org/10.1145/2751314'
THESIS = 'https://giovannilion.link/thesis/2-Litreview.html'
VERBEEK_COPY = 'https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf'
S = []

S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 13',
    'Your product.\nYour argument.', 'Showcase / evidence / responsibility',
    notes='Showcase-first review draft, not a confirmed operational schedule. Main teaching route ends at slide 33; staff readiness material lives only in the companion instructor notes, outside the exported deck. The published syllabus still assigns a 20% final quiz in Week 13 after the fair. Its placement and rules require explicit reconciliation; this deck neither cancels it nor supplies a quiz. No assessment questions, answers or student work are included. See the companion notes and readiness gates.'))
S.append(content('SHOWCASE / THE ROUTE', 'Make the decision visible.', [
    'Present the product: who it is for, what the AI does, and why it matters.',
    'Encounter other work: ask about evidence, consequences and control.',
    'Compare what we learned: rules, examples, mediation and the designer\'s role.',
    'Follow the teaching team\'s confirmed presenting and visiting arrangements.',
], body_size=36, notes='Do not infer that this is the entire three-hour schedule. Announce only separately confirmed movements, access/support routes and assessment arrangements. The separate instructor record names the decisions needed before classroom use.'))
S.append(cards('EXISTING GROUP PROJECT / 40% OF THE COURSE', 'Three ways to explain one product.', [
    ('A0 POSTER', 'Research + concept.', 'Person + problem + evidence. Show the AI action.'),
    ('3-5 MINUTE VIDEO', 'A moment of use.', 'Show a moment of use. Label simulated behaviour.'),
    ('ONE-PAGE BRIEF', 'The mediation.', 'Relation + data + bias + guardrails. Explain your design choice.'),
], text_size=30, notes='Existing syllabus deliverables only. This slide does not create another submission, deadline, printing route or presentation duration. The video length is not a speaking allocation. Confirm actual Canvas instructions separately.'))
S.append(content('EXISTING PROJECT RUBRIC / NOT COURSE WEIGHTS', 'Polish is only part of the argument.', [
    '30% research and contextual analysis: credible sources, situated claims.',
    '30% ethical and sociological impact: relation, data, bias and guardrails.',
    '20% communication and poster design: a clear, engaging account.',
    '10% video presentation; 10% team collaboration and process documentation.',
    '[Read the syllabus and group-project rubric](' + SYLLABUS + ')',
], body_size=33, notes='These five percentages sum to 100% WITHIN the group project, which is 40% of the course. They are not additional course weights. Do not invent peer scores, prizes, extra criteria or assessment procedures. Instructor grading uses the approved rubric and confirmed procedure; the peer discussion below is formative unless separately approved.'))
S.append(section('01 / SHOWCASE', 'Explain the choice.', 'Person / AI action / evidence / consequence', bg=INK,
    notes='Chapter marker within the existing showcase route, not an additional activity or time allocation. The opening deliverables and rubric remain unchanged. Now turn from what is submitted to how another person can understand the design. No new speaking duration, visitor quota, written checklist or submission is introduced.'))
S.append(content('VISITOR LENS / FIVE QUESTIONS', 'Can I understand the product?', [
    'WHO: person, need, situation.',
    'AI ACTION: what happens during use?',
    'EVIDENCE: what supports the choice? Where does it stop?',
    'CONSEQUENCE: whose experience changes?',
    'AGENCY: question, refuse, correct, undo.',
], body_size=34, notes='Use these as a conversation guide, not five compulsory written answers or a new assessment checklist. A nonconversational recommender still makes a consequential selection. Visitors can engage while seated; do not make physical movement the condition for participation.'))
S.append(cards('PRESENTER / FROM CLAIM TO CONSEQUENCE', 'Tell the story of one decision.', [
    ('01 / SITUATION', 'A person needs ...', 'Describe the moment. Why use a model?'),
    ('02 / AI ACTION', 'The system proposes ...', 'Input -> output. Working, simulated or proposed?'),
    ('03 / RESPONSIBILITY', 'The person can ...', 'Benefit -> failure -> control or recovery.'),
], text_size=30, notes='An optional speaking scaffold, not a new timed pitch or required script. Ask for a concrete moment of use rather than a general claim that the product is intelligent or ethical. A team may honestly show a concept and limits; do not imply evaluated performance from a polished mockup.'))
S.append(content('RESEARCH / A BOUNDED CLAIM', 'A citation is not a guarantee.', [
    'Who and what were studied? Compared with what?',
    'Finding is not interpretation or product validation.',
    'Name one gap: people, context, model, outcome or time.',
    'A classroom demo cannot establish long-term benefit or safety.',
], body_size=36, notes='Connect to the Week 8 evidence cards. Do not require new papers or another upload at the fair. If only an abstract was read, say so; do not invent methods or quotations. A study can inform a design choice without validating the new product. Ask: what result would make you revise your claim?'))
S.append(content('ETHICAL ARGUMENT / NOT A LIST OF VALUES', 'Show the trade-off you chose.', [
    'CLAIM: helps [person] by [mechanism].',
    'TENSION: who benefits, who carries the cost?',
    'DECISION: changed [design choice] because [reason].',
    'BOUNDARY: [risk] remains. Check [outcome].',
], body_size=35, notes='Instructor-authored scaffold applying mediation and the existing ethical/sociological criterion, not a new compulsory section or submission. Ask whether an objection changed the design. Privacy, convenience and inclusion can conflict; naming a value does not resolve that conflict. Avoid demanding personal sensitive disclosures as evidence.'))
S.append(cards('ILLUSTRATIVE CONCEPT / NOT A VALIDATED PRODUCT', 'A campus route recommender.', [
    ('PROMISE', 'A suitable route.', 'Stated access needs matter. Shortest is not always suitable.'),
    ('FAILURE', 'An unavailable lift.', 'Outdated data could make the route unusable.'),
    ('RESPONSE TO TEST', 'Show uncertainty.', 'Alternatives + freshness + correction. Keep map or human support.'),
], text_size=29, notes='Fictional teaching example, not a campus service, empirical result or validated safeguard. Do not collect health records or identify students with access needs. A freshness label can still be wrong; test whether people notice and can recover, and how a correction reaches the responsible operator. No guarantee of accessible routing is made.'))
S.append(section('02 / CRITIQUE', 'Notice. Then ask.', 'A specific choice / an interpretation / a question', bg='#246E70',
    notes='A transition inside the existing showcase budget. This marks the switch from presenting a product to discussing a consequential choice. Peer discussion stays formative: no new scores, prizes, quotas, public feedback collection or assessed log. Visitors can participate without circulating physically.'))
S.append(content('VISITOR / FORMATIVE FEEDBACK', 'Notice. Interpret. Ask.', [
    'NOTICE: "Uncertainty appears before acceptance."',
    'INTERPRET: "That may help comparison if data is current."',
    'ASK: "What if the lift status is wrong?"',
    'Discuss the design; do not invent a score.',
], body_size=34, notes='These are instructor-authored example comments about the fictional route concept. Formative peer discussion unless an approved rule says otherwise. No visit quota, compulsory comment collection, bonus mark or peer prize. Do not promise anonymity or open a public board. Consent and authorized handling are needed before recording/sharing identifiable feedback.'))
S.append(cards('PRESENTER / RECEIVE CRITIQUE', 'Listen for the decision behind the comment.', [
    ('CLARIFY', 'What did they encounter?', 'Which moment prompted the response?'),
    ('COMPARE', 'What supports it?', 'Observation, inference or suggestion? Whose situation?'),
    ('DECIDE', 'Keep, change or investigate.', 'Explain why. Narrowing a claim can beat adding features.'),
], text_size=30, notes='Optional team working notes, not a new feedback log submission or post-fair revision deadline. Keep private project material in the existing authorized workspace. Feedback is evidence about this encounter, not a representative user study.'))
S.append(content('SHOWCASE / MANUAL HOLDING VIEW', 'Present. Visit. Listen.', [
    'Presenters: explain one person, one AI action and one consequence.',
    'Visitors: identify a specific strength and ask a substantive question.',
    'Keep paths and displays accessible. Ask the teaching team if movement or playback is difficult.',
    'Listen for the teaching team\'s cue before changing roles.',
], body_size=37, notes='This is not a live timer. Reusable static holding slide, manually revisited as needed. It does not prescribe rounds, staffing or visit counts. Use only with a separately confirmed fair protocol that gives equitable presenting/visiting opportunities. Announce actual support and transition arrangements; do not imply an automatic clock, alarm or scheduled advance.'))
S.append(content('DEBRIEF / FROM ENCOUNTER TO INSIGHT', 'What did someone else make visible?', [
    'What did a visitor understand differently?',
    'Claim, model, evidence or interaction?',
    'Keep, change or investigate? Why?',
    'No names or private project material.',
], body_size=36, notes='Short spoken debrief, not a new graded reflection or collected answer. Invite a volunteer observation and a contrasting interpretation. Do not announce an unapproved resubmission opportunity or deadline. Bridge into the synthesis: a designer is accountable for interpretation as well as intention.'))
S.append(statement('Pause.\nReturn on cue.', eyebrow_text='MANUAL BREAK HOLD / FOLLOW THE INSTRUCTOR', size=118,
    notes='Static break holding slide. The planning budget provisionally holds a fifteen-minute break, but this is not a universal schedule claim. Instructor announces the actual return cue after confirming the session plan and access needs. No countdown or clock time is embedded.'))
S.append(section('03 / SYNTHESIS', 'Making. Using. Living.', 'Rules and examples / mediation / responsibility', bg=INK,
    notes='Chapter marker for the conceptual close, not a new lecture allocation or a restriction of whole-course assessment scope. Connect the visitor encounter to the course question. The instructor selects the route within confirmed showcase and any retained assessment time; this deck still does not set operational logistics.'))
S.append(statement('Can a machine\noriginate\na design?', eyebrow_text='THE COURSE QUESTION / DEFEND A POSITION', bg=PAPER, size=111,
    notes='Return to the syllabus opening question. Do not force a yes/no verdict or equate fluent output with intention. Ask what originate means: producing an artifact, framing a problem, judging value, assuming responsibility? Synthesis is a conceptual connection, not a restricted exam scope.'))
S.append(cards('MACHINE A / MACHINE B / A+B', 'Two routes. Different commitments.', [
    ('RULES / MACHINE A', 'Write the procedure.', 'Instructions set possibilities. Randomness can work inside rules.'),
    ('EXAMPLES / MACHINE B', 'Learn a pattern.', 'Learn from training examples. Plausible does not mean true.'),
    ('COMBINE / A+B', 'Allocate the choices.', 'Model writes code; rules execute. Check both.'),
], text_size=29, notes='Reuses the established course distinction, not a claim that every system fits a pure category. Rules can be complex and opaque to a user; learned systems can be repeatable and constrained. Do not repeat the archive\'s incorrect historical implication that 1975 prototype research caused the 1958 perceptron. Examples are grounded in Weeks 2-6 sources.'))
S.append(cards('PROCESS VERSUS PRODUCT', 'Where is the model doing the work?', [
    ('AI AS A DESIGN TOOL', 'Helps you make.', 'Make images, code or sound. Select, verify, disclose.'),
    ('AI IN THE PRODUCT', 'Acts during use.', 'Recommend a route or adapt a feed. Consequences recur in use.'),
], text_size=34, notes='Both can occur in one project; one does not prove the other. An AI-rendered mockup alone does not establish an AI-incorporating product. A product might combine an explicit rule with a learned model. Use the team\'s stated AI action as the anchor rather than assuming an implementation architecture.'))


def mediation_decision():
    """Native text/shape figure keeps all labels readable in mobile handout mode."""
    slide = concept_frame('A recommendation rearranges the choice.',
        'MEDIATION / ORIGINAL TEACHING DIAGRAM',
        notes='Original course application of Ihde/Verbeek, not their canonical four-relation diagram or a causal finding. The fictional route example shows a situated relation, not merely data flow: the person encounters the place through selected alternatives. The interface can make uncertainty and alternatives salient or hide them. All figure labels are native editable text, also included in mobile reading order. Source: Verbeek (2015), Beyond Interaction; Week 5 mediation bridge and Week 8 product analysis.')
    for x, label, heading, body in [
        (120, 'PERSON', 'A need + a choice', 'A person wants to reach a place.\nNeeds and priorities differ.'),
        (700, 'TECHNOLOGY', 'Selected alternatives', 'Data, model and interface\nmake some routes salient.'),
        (1280, 'WORLD', 'A route taken', 'The choice meets lifts, paths\nand other people in use.'),
    ]:
        slide.els += [Rect(x, 365, 520, 430, '#FFFFFF'),
                      T(x+25, 395, 470, 40, label, 'monomed', 25, '#246E70'),
                      T(x+25, 475, 470, 100, heading, 'xbold', 40, INK),
                      T(x+25, 610, 470, 150, body, 'body', 31, INK, lh=1.3)]
    slide.els += [T(120, 845, 1680, 100,
        'Ask: what becomes easier to notice or do, and what becomes harder?', 'xbold', 37, INK)]
    slide.els.append(T(120, 956, 1680, 38,
        '[Verbeek (2015)](' + VERBEEK + ') / original route illustration, not measured data.',
        'mono', 21, INK, lh=1.1, name='paper-citation'))
    return slide


def concept_frame(heading, phase, notes):
    """Week-owned Week 8 grid for the short conceptual recap."""
    slide = _slide('#FFFFFF', notes, title=heading)
    slide.els += [eyebrow(120, 96, phase, '#246E70'),
                  T(120, 184, 1680, 140, heading, 'xbold', 72, INK,
                    lh=.95, spc=-.03, name='paper-title')]
    return slide


def concept_block(slide, x, y, label, value, height, name):
    slide.els += [T(x, y, 780, 34, label, 'mono', 23, '#246E70', name=name+'-label'),
                  T(x, y+52, 780, height, value, 'body', 34, INK,
                    lh=1.2, name=name+'-body')]


def mediation_reading():
    slide = concept_frame('Products shape how we see and act.',
        'MEDIATION RECAP / VERBEEK / 2015 / CONCEPTUAL ESSAY',
        'Verbeek (2015), Beyond Interaction, Interactions 22(3), 26-31, DOI 10.1145/2751314. '
        'The retained six-page institutional author copy was rechecked in full on 22 October 2026; '
        'PDF positions 3-4 / printed pp. 28-29 compare extension, opposition and hybridity, '
        'and positions 5-6 / printed pp. 30-31 address influence and design ethics. '
        'This is a conceptual essay, not a participant study: there is no sample size, '
        'comparison group, measured effect or validated safety recipe. The double-sided '
        'printer is adapted from the author example on printed pp. 29 and 31; no observed '
        'printing rate is claimed. The argument is that a default helps shape practice, '
        'not that it determines all behaviour or removes human freedom. '
        'Explain the question and worked example before the interpretation. The next slide '
        'applies this lens to the fictional route concept, not to a newly tested product. '
        'This replaces the old compressed reading summary within the existing short synthesis; '
        'no pre-reading, extra lecture minutes or student experiment. No source artwork is reused.')
    concept_block(slide, 120, 348, 'QUESTION / TWO WAYS TO SEE A TOOL',
        'Does a printer merely carry out a choice, or also help shape that choice?', 210, 'concept-question')
    concept_block(slide, 1020, 348, 'EXAMPLE / ADAPTED FROM THE ESSAY',
        'A printer defaults to double-sided. A person can change it, but the starting choice is already set.',
        210, 'concept-example')
    concept_block(slide, 120, 676, 'ARGUMENT / ANALYSIS, NOT A MEASURED EFFECT',
        'Design helps shape what people notice and do. Verbeek compares tool, opposition and mediation views.',
        190, 'concept-argument')
    concept_block(slide, 1020, 676, 'LIMIT / FOR YOUR DESIGN',
        'No printing rate or safety result is measured. Ask what your design makes easy, then test that claim.',
        190, 'concept-limit')
    slide.els.append(T(120, 956, 1680, 38,
        '[Verbeek, Beyond Interaction (2015)](' + VERBEEK_COPY + ') / pp. 28-31 / conceptual analysis.',
        'mono', 21, INK, lh=1.1, name='paper-citation'))
    return slide


S.append(mediation_reading())
S.append(mediation_decision())
S.append(cards('AGENCY / A RELATION YOU DESIGN', 'Can the person act otherwise?', [
    ('BEFORE', 'Understand the boundary.', 'What is it for? What does it not know?'),
    ('DURING', 'Compare and refuse.', 'Compare, correct or reject before it matters.'),
    ('AFTER', 'Recover and contest.', 'Repair, exit or reach a responsible human.'),
], text_size=29, notes='Design questions, not universal proven safeguards. A nominal override is weak if alternatives are unusable or burdensome. Consider people affected by the choice who never use the interface. Saying human-in-the-loop does not establish who can intervene, when or with what authority.'))
S.append(cards('DATA / BIAS / CONSEQUENCES', 'Follow the error through the system.', [
    ('INPUT + LABELS', 'Who is represented?', 'Collected, omitted, labelled by whom?'),
    ('MODEL + OBJECTIVE', 'What counts as success?', 'Accuracy, engagement and equitable access can diverge.'),
    ('INTERACTION', 'Who bears the cost?', 'Whose errors are visible? Who can correct them?'),
], text_size=29, notes='Synthesis of the syllabus data/bias strand and historical Master pp. 27, 31-34. These are possible mechanisms, not a claim that every recommender inevitably creates polarization or every dataset has the same bias. Pseudonymization does not automatically remove reidentification risk. A broad accuracy average can conceal unequal consequences; avoid inventing demographic results.'))
S.append(cards('EVIDENCE / THREE DIFFERENT CLAIMS', 'Looks good. Works here. Helps over time.', [
    ('APPEARANCE', 'A convincing demonstration.', 'A possible interaction, not proof of reliable AI.'),
    ('PERFORMANCE', 'A defined task result.', 'Task + comparison + conditions. Score is not benefit.'),
    ('IMPACT', 'A change in someone\'s life.', 'Relevant outcomes, people, time. Liking is not lasting benefit.'),
], text_size=30, notes='Instructor-authored evidence ladder, not a formal universal hierarchy: qualitative accounts can reveal meaningful consequences too. Reconnect to Week 8\'s distinction between response ratings, source choice and outcomes without repeating numerical findings or implying later classes were already taught. Ask which claim the poster actually makes.'))
S.append(section('04 / RESPONSIBILITY', 'Who chooses? Who answers?', 'Curation / language / authorship / accountability', bg='#246E70',
    notes='Final thematic transition inside the existing conceptual synthesis. Distinguish the model output from the choices that frame, select and release it. Do not turn this chapter into a new production task, legal ruling, monitoring report or extra assessment. The closing position remains open to reasoned disagreement.'))
S.append(cards('CURATION / DESIGNER RESPONSIBILITY', 'Selection is a design act.', [
    ('BEFORE GENERATION', 'Frame the possible.', 'Question, sources, examples, constraints. What is excluded?'),
    ('AFTER GENERATION', 'Judge what ships.', 'Select, reject, edit, verify. Output cannot answer for consequences.'),
    ('AFTER RELEASE', 'Attend to effects.', 'Who monitors, corrects or stops harmful behaviour?'),
], text_size=30, notes='Connect the Week 11 curation discussion to process documentation and product accountability. These are responsibilities to design for, not a new required production deployment or assessed monitoring report. Do not turn curation into a claim that selecting any generated output establishes legal authorship or ownership.'))
S.append(content('LANGUAGE AS INTERFACE / NOT MAGIC', 'A prompt is a design decision.', [
    'Language expresses goals without specifying every step.',
    'Inferred intent can differ. Check the actual result.',
    'Agents add tools: set permissions and approval points.',
    'Fluency is not understanding, competence or care.',
], body_size=36, notes='Synthesis of Week 4 harnesses and the Week 12 language-as-interface theme. Do not call natural language the ultimate interface for every user or task. Form controls, direct manipulation, code and speech can coexist. Do not equate generated explanations with faithful access to internal reasoning.'))
S.append(content('AUTHORSHIP / OWNERSHIP / ACCOUNTABILITY', 'Keep the questions separate.', [
    'AUTHORSHIP: what did you frame, make or change?',
    'ATTRIBUTION: whose work and tools contributed?',
    'OWNERSHIP: which permissions and jurisdiction apply?',
    'ACCOUNTABILITY: who checks and responds?',
], body_size=36, notes='Historical Week 12 pp. 64-66 and Master pp. 39-41/49-50 motivate the distinction. This slide gives no legal determination. The historical universal heading about AI patents/copyright is overbroad; authorship and rights depend on jurisdiction, subject matter and human contribution. No claim about a current case disposition or training legality is imported. Course policy still requires honest AI process disclosure and accurate sources.'))
S.append(content('CLOSING DISCUSSION / NO NEW SUBMISSION', 'Defend your answer with a design choice.', [
    '"Originate" means ... My position is ...',
    'A design choice supports it because ...',
    'An objection is ... I would reconsider if ...',
    'The designer remains responsible for ...',
], body_size=37, notes='Spoken reflection or private thinking; no ClassPoint collection, new essay or extra mark. Invite different defensible positions, not the instructor\'s preferred answer. The concepts on these synthesis slides are not a restriction of the published whole-course assessment scope.'))
S.append(content('RESOURCE SHELF / ATTRIBUTED LINKS', 'Return to the sources, not just the output.', [
    '[SD2112 course slides and resources](https://venetanji.github.io/sd2112-teaching/) / course teaching team.',
    '[Current syllabus, project brief and rubric](' + SYLLABUS + ') / SD2112, 2026/27.',
    '[Beyond Interaction](' + VERBEEK + ') / P.-P. Verbeek, Interactions 22(3), 2015, 26-31.',
    '[Concept formation literature review](' + THESIS + ') / Giovanni Lion, thesis chapter 2.',
    '[PolyU Library](https://www.lib.polyu.edu.hk/) / verify the research behind your claim.',
], body_size=32, notes='Descriptive native Markdown links render in HTML, mobile handout and native PPTX. Verbeek provides the mediation framework, not evidence that this fictional product is safe. Library/publisher access may require lawful institutional access. Check current operational announcements on Canvas; this public shelf contains no submission settings or private records.'))
S.append(content('FINISH / EXISTING ARRANGEMENTS ONLY', 'Keep the argument and the evidence together.', [
    'Use the approved project brief and the instructor\'s confirmed Canvas instructions.',
    'Do not post classmates\' work, feedback or identifiers without permission.',
    'If display, playback or access fails, tell the teaching team; use the confirmed contingency.',
    'Check the confirmed instructions before leaving or submitting work.',
], body_size=36, notes='Do not use this slide to dismiss a class before any retained assessment component. The published 20% final quiz still needs explicit reconciliation. Confirm completion/support and assessment instructions through the approved channel; do not promise retakes, replacement submissions or grade adjustments.'))
S.append(end('Design the choice.\nOwn the consequence.', 'A product is an argument about how people should live.',
    'SD2112 / WEEK 13 / ' + SITE,
    notes='Closing course statement, instructor-authored rather than a quotation. Main route ends here. Readiness records remain in the separate instructor notes, not the student export. Do not announce that all assessed activity is complete until the instructor confirms actual arrangements.'))

MAIN_SLIDE_COUNT = len(S)
# Staff material is retained for the notes companion, never passed to finalize.
STAFF_SLIDES = []
STAFF_SLIDES.append(content('INSTRUCTOR REVIEW ONLY / READINESS GATE 1', 'Reconcile the published assessment.', [
    'The published syllabus retains a 20% whole-course multiple-choice final quiz in Week 13 after the fair.',
    'Showcase-first direction does not silently remove or move that requirement.',
    'Obtain an explicit authorized decision before releasing the operational schedule.',
    'If retained here: confirm question count, time, platform, resources, attempts, access and incident handling privately.',
], body_size=34, notes='Not student-facing operational instructions. The current draft deliberately contains no assessed content, answer key, platform settings or assumed quiz duration. Do not derive final rules from the midterm or historical Week 14 exam. Keep this readiness record in the instructor notes; it is excluded from the student deck exports.'))
STAFF_SLIDES.append(content('INSTRUCTOR REVIEW ONLY / READINESS GATE 2', 'Prove the fair fits the confirmed session.', [
    'Confirm room, actual teams, access, circulation, display/video arrangements and equitable presenting/visiting.',
    'Confirm rubric procedure, grader coverage and moderation; do not assume staff or rounds.',
    'Only if the quiz remains here: reserve Q working minutes and A access/instruction/recovery minutes at the end.',
    'With a provisional 15-minute break, showcase + synthesis + transitions must fit 180 - Q - A - 15.',
], body_size=33, notes='Conditional reserve equation only, not a universal classroom schedule or a chosen Q/A. If an authorized revision moves/removes the component, record it before reallocating time. Include setup/transition and equitable access, not just speaking time. Check room/team feasibility before duplicating the manual holding slide into confirmed rounds.'))
STAFF_SLIDES.append(content('INSTRUCTOR REVIEW ONLY / READINESS GATE 3', 'Test the actual delivery conditions.', [
    'Confirm existing submission route, deadlines, printing and approved failure contingencies; add no new deliverables.',
    'Test classroom display, captions/audio, offline playback and an accessible nonmovement route.',
    'Confirm feedback handling and consent. Keep student work and assessment content out of public artifacts.',
    'If a quiz is retained: preflight approved settings with authorized test data and confirm private support/recovery.',
], body_size=34, notes='Build and browser checks do not verify physical room access, classroom PowerPoint font resolution, playback audibility, ClassPoint add-in or actual assessment-platform settings. No ClassPoint collection is configured in this deck; feedback remains spoken/formative. Resources are public reading links, not a feedback/submission destination.'))
STAFF_SLIDES.append(content('INSTRUCTOR REVIEW ONLY / HISTORICAL PROVENANCE', 'What the archive actually contains.', [
    'Editable Week 13 archive: five slides, one notes part; embedded created/modified timestamps are in 2025.',
    'It includes a poster fair and feedback, plus an old Week 14 exam announcement and obsolete logistics.',
    'Reuse: the fair/feedback intent only. No old dates, room, tool, visit quota or exam settings are carried forward.',
    'Synthesis background: 2025 Master and Week 12 PDF positions 54-69; see the source ledger for limits.',
], body_size=34, notes='All five slide XML parts and the sole notes XML were inspected; the notes contain only a slide number. The file name alone is not provenance: core metadata and explicit 2025 dates support dating, not proof of live delivery or final approval. Original package rendering unavailable without an Office renderer; a labelled XML-based visual reconstruction was reviewed, not claimed as an original PowerPoint screenshot. See lessons/week13-sources.md and ignored QA evidence.'))

# No new collection: report linkage remains a safe no-op before teaching.
attach_reports(S, Path(__file__).resolve().parent / 'week13-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 13 / Review draft',
            slides=finalize(S, footer(13)), pdf='SD2112-week13.pdf')
