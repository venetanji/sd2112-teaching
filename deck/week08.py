"""Week 8: research -> AI product -> an evidence-informed project decision."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, INK, PAPER
from deckgen.reports import load as load_reports
from deckgen.layouts import (title, agenda, journey, content, cards, statement, figure_slide,
                             two_col, activity, question, finalize, section, T, Image, Rect, _slide, eyebrow)
from course import footer, JOURNEY
import week05_mediation_figures as M
import week08_figures as F
from week08_studies import STUDY_GUIDES, EXTENSION_GUIDES

S = []
PRIVATE_REFLECTION_TITLES = (
    'Have you ever shared a deep secret with a chatbot that you would not tell a human?',
    'If yes, what made it easier to tell the chatbot?',
)
PAPER_SUBMISSION_TITLE = 'Share one paper for your group project.'
REFS = {
    'R1': ('Hatch et al., 2025', 'https://doi.org/10.1371/journal.pmen.0000145'),
    'R2': ('Jain, Pareek & Carlbring, 2024', 'https://doi.org/10.1016/j.invent.2024.100745'),
    'R3': ('Sharma et al., ICLR 2024 / revised 2025', 'https://arxiv.org/abs/2310.13548v4'),
    'R4': ('Cheng et al., Science, 2026', 'https://doi.org/10.1126/science.aec8352'),
    'R5': ('Shaw & Nave, working paper v1, 2026', 'https://doi.org/10.31234/osf.io/yk25n_v1'),
    'R6': ('De Freitas et al., online 2025 / issue 2026', 'https://doi.org/10.1093/jcr/ucaf040'),
    'R7': ('Maheshka, Folk & Dunn, 2026', 'https://doi.org/10.1177/19485506261444068'),
    'R8': ('Wenger, Cameron & Inzlicht, 2026', 'https://doi.org/10.1038/s44271-025-00387-3'),
    'R9': ('Heinz et al., NEJM AI, 2025', 'https://doi.org/10.1056/AIoa2400802'),
    'R10': ('Cao et al., SOUPS, 2026', 'https://www.usenix.org/conference/soups2026/presentation/cao'),
    'R11': ('Joshi & Vogel, GI, 2026', 'https://arxiv.org/abs/2507.03670v3'),
    'R12': ('Sozen & Borekci, AI EDAM, 2026', 'https://doi.org/10.1017/S0890060426100304'),
    'R13': ('Yu et al., 2025', 'https://doi.org/10.1186/s41239-025-00545-x'),
}


def source(key):
    name, url = REFS[key]
    return f'[{key} / {name}]({url})'


PAPER_SUMMARIES = {}
PAPER_ASSETS = Path(__file__).resolve().parent / 'assets' / 'week08-papers'


def paper_frame(key, heading, phase, notes):
    """Shared title and citation grid for every paper explanation."""
    s = _slide('#FFFFFF', notes, title=heading)
    s.els += [eyebrow(120, 96, phase + ' / ' + key, '#246E70'),
              T(120, 184, 1680, 140, heading, 'xbold', 72, INK,
                lh=.95, spc=-.03, name='paper-title')]
    return s


def paper_block(s, x, y, width, label, value, height, size=34, name=''):
    s.els += [T(x, y, width, 34, label, 'mono', 23, '#246E70', name=name + '-label'),
              T(x, y + 52, width, height, value, 'body', size, INK,
                lh=1.2, name=name + '-body')]


def study(key, heading, prompt, notes,
          image=None, attribution=None, method=None, block='RESEARCH'):
    """Teach the task and measurement before the separate result/figure."""
    guide = STUDY_GUIDES[key]
    PAPER_SUMMARIES[key] = dict(guide, prompt=prompt)
    extra = (' Plain-language experiment walkthrough: ' + guide['teaching_notes'] +
             ' Source locations: ' + guide['source_locations'] +
             ' This pair shares the original paper allocation; no extra class minutes. '
             'The labelled example is explanatory, not an additional study or student task.')
    task = paper_frame(key, guide['title'], 'THE STUDY / ' + block, notes + extra)
    # Equal-width columns and explicit block gaps replace the cramped four-row abstract.
    paper_block(task, 120, 348, 780, 'WHAT THEY DID', guide['task'], 210,
                name='study-task')
    paper_block(task, 120, 676, 780, 'WHAT THEY COMPARED', guide['comparison'], 154,
                name='study-comparison')
    example_label = ('ILLUSTRATIVE EXAMPLE / NOT STUDY WORDING'
                     if guide['example_kind'] == 'illustrative' else 'ADAPTED FROM THE STUDY')
    task.els.append(Rect(990, 328, 840, 330, '#EAF4F3'))
    paper_block(task, 1020, 348, 780, example_label, guide['example'], 244,
                size=38, name='study-example')
    paper_block(task, 1020, 700, 780, 'WHAT THEY MEASURED', guide['measured'], 190,
                name='study-measurement')
    task.els.append(T(120, 956, 1680, 38, source(key), 'mono', 21, INK, lh=1.1))

    s = paper_frame(key, heading, 'THE RESULT / ' + block, notes + extra)
    if image:
        s.els.append(Image(120, 348, 1010, 515, str(PAPER_ASSETS / image), 'contain',
                           name='paper-figure-' + key, url=REFS[key][1]))
    else:
        for i, (label, value) in enumerate(method):
            y = 348 + i * 165
            s.els += [Rect(120, y, 1010, 2, '#D5DCDA'),
                      T(140, y + 20, 970, 40, label, 'mono', 23, '#246E70'),
                      T(140, y + 68, 970, 90, value, 'xbold', 46, INK, lh=1.1)]
    for y, label, value, name in [
        (348, 'WHAT THEY FOUND', guide['result'], 'study-result'),
        (580, 'WHAT IT DOES NOT SHOW', guide['limit'], 'study-limit'),
        (812, 'FOR YOUR DESIGN', prompt, 'study-design'),
    ]:
        paper_block(s, 1190, y, 610, label, value, 160 if y < 800 else 90,
                    size=32, name=name)
    s.els += [T(120, 884, 1010, 64, attribution or 'Original method illustration; not measured data.',
                'mono', 20, '#246E70', lh=1.2),
              T(120, 956, 1680, 38, source(key), 'mono', 21, INK, lh=1.1)]
    return [task, s]


def paper_detail(key, heading, image, caption, notes):
    """Enlarge dense axes after the experiment and result explanation."""
    s = paper_frame(key, heading, 'READ THE FIGURE', notes)
    s.els += [Image(120, 332, 1680, 552, str(PAPER_ASSETS / image), 'contain',
                    name='paper-detail-' + key, url=REFS[key][1]),
              T(120, 900, 1680, 48, caption, 'body', 27, INK, lh=1.15),
              T(120, 958, 1680, 36, source(key), 'mono', 21, INK, lh=1.1)]
    return s


# 0-10 minutes: reconnect to the existing Week 7 concept, not a new pitch round.
S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 08',
    'Humanizing AI.', 'Research. Relationships. Product responsibility.',
    notes='Three-hour class. Research -> AI product -> existing student project. Main route is slides 1-50; the appendix is a reference shelf, not extra lecture time. Relative minutes, not confirmed clock times: opening 0-10; mediation 10-30; research 30-65; implications 65-75; break 75-90; demo 90-105; research 105-145; revision 145-170; discussion 170-180. Keep the full break and research activity. Two optional personal questions use about three minutes inside mediation, not extra time; discuss design conditions rather than secrets. Each student submits a different paper URL and relevance during the existing research block. No new grade or deadline is introduced. If late, shorten optional study detail. Use the same conceptual level and native visual system as Weeks 5-7. No pre-reading is assumed: teach each summary before interpreting its figure. No personal mental-health disclosure is needed.'))
S.append(journey('SD2112 / THE SEMESTER', 'Where we are: AI inside products.', JOURNEY,
    here=(3, 0), notes='Reuse the semester blocks from Weeks 1 and 2. The orange outline marks Week 8, the beginning of module 3: AI inside products. We move from using AI to make an artifact to designing what AI does during use. This is orientation inside the existing ten-minute opening, not an additional lecture block.'))
S.append(agenda('SD2112 / WEEK 08', [
    'Your Week 7 concept and today\'s question',
    'Mediation: what relationship does AI invite?',
    'Research: care, choice, agreement and action',
    'From a finding to a product test',
    '15-minute break, then a library search demo',
    'Find papers, revise your concept, compare',
], notes='The route through the existing three-hour session: opening 0-10; mediation 10-30; research 30-65; product implications 65-75; break 75-90; library demo 90-105; group research 105-145; concept revision 145-170; comparison 170-180. The map and agenda share the opening allocation. Optional appendix papers are a reference shelf, not extra required lecture time.'))
S.append(content('0-10 / FROM WEEK 7 TO WEEK 8', 'Your concept is a starting claim.', [
    'Keep your existing team, product idea and image in view.',
    'What does the AI do during use? What does the person still decide?',
    'Today: research -> product decision -> a revised scope and a test.',
    'Work in team notes; later, each person submits one different paper in ClassPoint.',
], body_size=36, notes='Recall Week 7: one concept text and one image, teams already formed. Do not recollect or publish them. Ask teams to open their own material privately. This workshop informs the existing formal one-page group proposal; it does not cancel or replace it. The syllabus still specifies that proposal for Week 8. Confirm actual Canvas instructions/deadline before teaching; do not invent one.'))
S.append(content('NEWS / 15 OCTOBER 2026 / OPTIONAL TWO-MINUTE OPENER',
    'Directing an AI-generated scene', [
    'Kling 4.0: up to 30 seconds, 15 reference assets and 10 keyframes.',
    'Vendor report, not independent evidence of reliable continuity.',
    'What can you direct? What would you still need to test?',
    '[Kuaishou launch announcement](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-officially-launches-next-generation-kling-40-raising)',
], body_size=35, notes='Optional two minutes within the existing 0-10 opening, replacing the previous pair discussion rather than adding time. Kuaishou dates the actual launch to 15 October 2026; the page is dated 17 October and the dateline 16 October. Rechecked primary release 21 October. Reference/keyframe limits and continuity statements are vendor claims, not independent performance evidence. Account availability and cost are not guaranteed; preflight separately before any live use. The release describes enterprise API access and two-minute video extensions as upcoming, not available classroom features. No live generation, signup or payment is needed: discuss a storyboard or owned reference image. Ask which controls express human intent and what testing would establish that output follows it. Then return to the existing project question: what relationship does your product invite, and what does the person still decide? If skipped, use that relationship question for the same two-minute pair discussion. Preserve the 15-minute break, 40-minute research and 25-minute revision blocks. The optional MultiLangBench item remains a source-reading extension, not another timed slide.'))

# 10-30 minutes: re-use the established Week 5 framework and diagram.
S.append(figure_slide('10-30 / MEDIATION RECAP', 'Technology shapes the relation.', M.mediation_relations(),
    caption='Ihde, Technology and the Lifeworld (1990); Verbeek, Beyond Interaction (2015). Same schema as Week 5.',
    notes='Recall Week 5 without repeating its history of philosophy. Human-technology-world names a situated relation, not a one-way data pipeline. Embodiment: look through a viewfinder. Hermeneutic: read an image or display as a representation. Alterity: face the technology as a quasi-other. Background: systems shape the setting without focal attention. One product can participate in several relations. Source: Ihde (1990), Technology and the Lifeworld; Verbeek (2015), Interactions 22(3), 26-31; established course diagram.'))
S.append(figure_slide('MEDIATION / ALTERITY', 'An apparent other is still a design relation.', F.alterity(),
    caption='Original teaching diagram after Ihde (1990). Quasi-other describes experience, not proof of a mind.',
    notes='A ticket machine can answer back in an alterity relation; a human face is not required. Conversational AI intensifies possibilities through language, voice and apparent continuity. Do not equate fluent response with consciousness or dismiss real effects because a system is not a human. The world recedes in the schema, not disappears. Historical 2025 slides used additional transparent/opaque alterity notation; do not present that extension as Ihde\'s original four-category scheme.'))
S.append(figure_slide('DESIGN ANALYSIS / NOT A STUDY RESULT', 'A cue can become a promise.', F.expectations(),
    caption='Try: a name, a warm voice, "I remember", or "I am always here". What capability might each imply?',
    notes='Instructor-authored examples, not quotes from a product or empirical causal estimates. Ask which cue implies memory, availability, confidentiality or competence. A warm tone can be useful without pretending to be human. The arrows are questions to investigate: studies below test particular pieces, not this whole universal chain. Ask what happens when the expectation outlasts the actual capability.'))
personal_poll = question('multiple_choice', PRIVATE_REFLECTION_TITLES[0],
    choices=['Yes', 'No'], size=74,
    eyebrow_text='OPTIONAL / PERSONAL EXPERIENCE / YES OR NO',
    cp={'type': 'multiple_choice', 'choices': ['A', 'B'], 'select_multiple': False},
    notes='Optional, ungraded reflection within about three minutes shared with the next question inside the existing 10-30 mediation block. Students may skip without explanation or penalty. Explain before opening that responses may identify you to the teaching team; do not promise anonymity. This is self-reported experience, not a prevalence study or evidence that disclosure is safe. Keep the results panel closed and do not project individual responses or identify who answered yes. The pinned native multiple-choice DTO has no verified hide-names flag: check the actual add-in presentation controls before running; skip collection if responses cannot be kept private. Do not publish the activity URL, responses, exports or screenshots. Ask only yes/no, never for the secret. The course report hook withholds this personal activity even if a report ID is later supplied. Transition from implied confidentiality to design responsibility, not a request for confessions.')
personal_poll.els.append(T(120, 850, 1680, 120,
    'Optional: you may skip. Do not share the secret.\nResponses may identify you; this is not an anonymous poll.',
    'body', 30, INK, lh=1.25))
S.append(personal_poll)
S.append(question('short_answer', PRIVATE_REFLECTION_TITLES[1],
    hint='Responses may identify you. Optional: you may skip.\nExplain why, not the secret. No names or transcripts.',
    eyebrow_text='OPTIONAL / IF YOU ANSWERED YES / SHORT ANSWER',
    cp={'type': 'short_answer', 'hide_names': True, 'multiple': False},
    notes='Only students who answered yes and freely choose to elaborate should respond; everyone else skips. This is a manual conditional prompt, not automatic ClassPoint branching. Share the same approximately three-minute mediation allocation as the yes/no question, not extra lecture time. Ask about what made disclosure feel easier, for example perceived distance or control, not the content of the secret. No names, identifying details, health histories, actual secrets or chat transcripts. Hidden display names do not make exports or ClassPoint report payloads anonymous. Do not project individual responses; discuss general design conditions without attributing or reading out disclosures. Do not publish the activity URL, responses, exports or screenshots. If someone submits sensitive detail, keep it off-screen and follow normal private handling rather than repeating it. The report hook withholds this activity even if a report ID is later supplied. This is not therapy, assessment or evidence that a chatbot offers confidentiality.'))
S.append(cards('THE HIDDEN DECISION / MACHINE A + B', 'Effortless for whom?', [
    ('DATA', 'What disappears?', 'A conversation may become stored data. What is needed, retained or reused?'),
    ('MODEL', 'What gets rewarded?', 'A pleasing answer, a truthful answer and a useful challenge are not identical.'),
    ('INTERFACE', 'What seems certain?', 'A fluent answer can hide uncertainty, retrieval gaps and limits of the task.'),
], text_size=31, notes='Three-minute design analysis, not a claim about all products. Reconnect Machine B generation and the Week 4 agent harness: model output, retrieval, memory and interface policies are separate choices. Reading a generated explanation does not reveal a faithful internal reasoning trace. Ask teams to locate one hidden decision in their own concept.'))
S.append(cards('AGENCY / CALIBRATED TRUST', 'Can the person disagree and act?', [
    ('BEFORE', 'Know the boundary.', 'What does the system do? What evidence and data does it lack?'),
    ('DURING', 'Question the answer.', 'Compare, correct, override or ask for a source before the decision matters.'),
    ('AFTER', 'Leave or recover.', 'Keep an exit, a human route and a way to repair the consequences.'),
], text_size=31, notes='Finish mediation by asking what the interface makes possible, not whether it generates a reassuring disclaimer. Trust should be calibrated to the task and actual reliability; maximum trust is not the objective. These are design questions, not experimentally proven universal safeguards. Transition to testing the evidence behind product promises.'))

# 30-65 minutes: three topic blocks; no student pre-reading is assumed.
S.append(cards('30-65 / READ THE CLAIM BEFORE THE HEADLINE', 'A paper is a bounded claim.', [
    ('WHO + WHAT', 'People and system.', 'Who took part? What system and task were tested?'),
    ('AGAINST WHAT', 'A comparison.', 'Compared with what? Random assignment or observation?'),
    ('MEASURED HOW', 'Outcome and time.', 'A rating, a choice, an action or a symptom? For how long?'),
], text_size=31, notes='No pre-reading is assumed. Explain each paper from its question and setup, then point to the figure axes and comparator. A correlation alone cannot establish causation; randomization does not guarantee transfer. Name the outcome before debating good or bad. Full text and caveats are in the native notes and ledgers; students are not expected to decode a journal figure unaided.'))
S.append(section('01 / PERCEPTION + CHOICE', 'Seeming care.\nChoosing a source.',
    'A response rating is not a relationship or a treatment.', bg='#246E70',
    notes='Topic signpost inside the existing 35-minute evidence budget, not extra lecture time. Spend approximately eleven minutes on R1, R2 and R8 including figure explanation. Ask students to distinguish a reader rating, authorship context and a choice of empathy source. Do not assume students know these papers.'))
S.extend(study('R1',
    'A caring reply is not treatment.',
    'What would justify calling your product therapy?',
    "Hatch et al. (2025), full PLOS article and correction reviewed. Methods: 830 US panelists, selected responses from 13 convenience-sampled experts and prompted ChatGPT-4; AI responses were longer. Common factors include caring/understanding, not patient symptom change. Eighteen hypothetical snapshots, no treatment delivered. August correction DOI 10.1371/journal.pmen.0000426 discloses internal BYU Psychology funding to SRB and lead author SGH's ownership/compensated therapy practice at Hatch Data and Mental Health; business did not fund the study and no clients were included. Original funding/COI statements are superseded; correction does not revise outcomes. Product inference: a convincing conversational surface does not establish the outcome a user needs. Ask for the missing outcome and comparator. About three minutes.",
    method=[('READERS', '830 US panel participants'), ('MATERIAL', '18 couple-therapy scenarios'),
                     ('COMPARISON', 'Selected ChatGPT-4 / expert replies')],
    block='PERCEPTION + CHOICE'))
S.extend(study('R2',
    'Human replies felt more genuine.',
    'What should disclosure help someone decide?',
    "Jain, Pareek and Carlbring (2024), full PMC article reviewed. Initial 140 respondents believed all replies were human; 111 returned six months later. Human writers were Master's clinical-psychology students, not the R1 expert pool. Sections 2.1-2.5 and Tables 1/3: human ratings rose; AI ratings changed little. Table 1 supports authenticity superiority only; a Discussion sentence overstates professionalism/practicality and conflicts with the table. Nonsignificance is not equivalence. Anonymous responses prevented individual paired analyses. Time, attrition and familiarity are alternatives to a pure label effect. Perception, not treatment. Ask whether hiding the source would be justified: these findings do not justify concealment.",
    method=[('INITIAL / SOURCE CONCEALED', '140 respondents'),
                     ('SIX MONTHS LATER / SOURCE DISCLOSED', '111 returned; same replies'),
                     ('OUTCOME', 'Three response ratings')],
    block='PERCEPTION + CHOICE'))
S.extend(study('R8',
    'People chose humans but rated AI higher.',
    'Should users choose their source?',
    "Wenger, Cameron and Inzlicht (2026), full published article reviewed. Four brief nonclinical studies, 691 source-choice participants. Explain evaluating a response versus selecting an empathy source, not an established relationship or repeated live dialogue. Sources were CHOSEN, not randomly assigned for the rating comparison: selection can affect experienced-response ratings. Mostly decontextualized empathizers/human strangers; transfer to ongoing relationships is untested. Do not infer that everyone rejects AI or that AI understands more because a response rates well. Ask whether source choice is part of a rehearsal product's value. No personal disclosures. Figure 1, published PDF p.5, cropped complete plot under CC BY 4.0: four violin distributions, dot means and SE bars; dashed .5 = equal human/AI choice. Show variability, not unanimous rejection of AI. Samples 152/196/195/148 total691. This figure shows choice only; higher response ratings come from separate analyses/Figures2-7. PDF/version/crop provenance in week08-paper-figures.md.",
    image='r8-choice.png',
    attribution='Wenger et al. (2026), Fig. 1; published PDF p.5.\nCropped plot; CC BY 4.0. Dashed line = equal choice.',
    block='PERCEPTION + CHOICE'))
S.append(section('02 / BENEFITS + THEIR HORIZON', 'Relief now.\nAction outside the app.',
    'Different outcomes need different evidence.', bg='#246E70',
    notes='Topic signpost, not extra teaching time. Allocate approximately eight minutes to the two distinct papers R6 and R7. First ask what changes during a conversation, then what changes outside the app. The split is deliberate: students have not pre-read and each paper needs its own setup, result and limitation. R9 is an optional untimed appendix contrast, not a third required paper in this block.'))
S.extend(study('R6',
    'Relief now is not lasting improvement.',
    'Measure relief, persistence, or both?',
    'De Freitas et al., full final five-study published article read from retained HBS-hosted PDF; not the older six-study working paper. First online 25 June 2025; 2026 issue. Study 3, PDF pp.11-15: US participants, prompted GPT-4 companion Jessie for 15 minutes daily across seven days; no-interaction control only rated loneliness, so time/contact not matched. Primary complete-case sample 922 (314 experience, 362 control, 246 prediction); differential attrition about 23% versus 14%. Explain Figure 3A first: open circles before, filled circles after; triangles control. The repeated immediate gap is not accumulated recovery. Pre-session scores did not differ significantly from control on any day; post-session versus control contrasts differ across days. Shaded bands are 95% CIs, broken axes retained. Panel B compares predictions with experience, not a clinical comparator. General discussion pp.18-20 distinguishes temporary relief from enduring change and rejects clinical recommendations or replacement of human relationships/professional care. Figure 3 A+B, PDF/printed p.13, exact crop and source SHA in week08-paper-figures.md. Figure is an attributed scholarly teaching quotation; all-rights-reserved OUP rights are not a public reuse grant. Ask which outcome the project actually promises: momentary comfort, persistence, or action outside the app. About four minutes; no student pre-reading.',
    image='r6-figure.png',
    attribution='De Freitas et al., Fig. 3 A+B, final PDF p.13.\nOpen = before / filled = after; bands = 95% CIs.',
    block='BENEFITS / IMMEDIATE RELIEF'))
S.append(paper_detail('R6', 'Look between the sessions.', 'r6-detail.png',
    'De Freitas et al., Fig. 3 A+B, PDF p.13. Open = before, filled = after; 95% CIs; broken axes.',
    'Same paper and same four-minute R6 allocation, not an extra lecture segment. Read panel A: loneliness is self-reported; control triangles track once-daily ratings, experience open circles before and filled circles after daily chat. Point to day1 and day7 before interpreting the overall downward slopes. A vertical before-after gap is immediate relief; pre-session versus control comparison asks about persistence. Before-session differences from control were not significant; this is not equivalence. Panel B compares prediction versus experience, not clinical care. Shaded95%CI bands and broken axes remain intact. Figure3 A+B final published PDFp.13; this direct crop removes only surplus title area, not any legend, tick, condition or data. OUP rights and exact crop/hash are in week08-paper-figures.md.'))
S.extend(study('R7',
    'Rehearsal can lead outside the app.',
    'Measure action beyond app engagement?',
    'Maheshka, Folk and Dunn (2026), full 27-page accepted author manuscript and included SOM read; not the SAGE typeset version. PDF pp.6-8: 1465 US/Canadian Prolific participants completed Part 1, 1371 returned; randomized GPT-4o-mini preparation for 6-12 minutes versus three prescribed factual questions. Actual chat durations 7.83 versus 2.83 minutes, not matched. Follow-up opened after five days for four days; say roughly the following week, not exactly seven days for all. PDF p.10/printed p.9 reports 65% versus 59% self-reported conversation initiation; six percentage points, not six percent relative growth. No authentic initiation bar chart exists in this manuscript. Figure 1 on PDF p.11/printed p.10 is the anticipated-quality mediation model: explain only preparation -> expectations -> reported action. Its OR and b coefficients are not raw initiation percentages. Measured mediator is not independently randomized; pathway is not proof of mechanism. Among 853 reporting a conversation, quality/satisfaction contrasts were nonsignificant, not equivalence. No test against human rehearsal or equally intensive reflection. Figure caption claims an indirect effect; keep this narrower interpretation visible. Crop/version/access/rights caveat in week08-paper-figures.md. Ask whether the product helps a user take a freely chosen external step, instead of merely increasing app engagement. About four minutes; do not require personal disclosures.',
    image='r7-figure.png',
    attribution='Maheshka et al., Fig. 1, author manuscript PDF p.11.\nProposed pathway, not an initiation-rate chart or proof of mechanism.',
    block='BENEFITS / HUMAN ACTION'))
S.append(section('03 / AGREEMENT + OVERRELIANCE', 'Pleasant is not\nalways helpful.',
    'Feedback, social choices and reasoning are different tests.', bg='#246E70',
    notes='Topic signpost inside the existing evidence allocation. Approximately thirteen minutes for R3, R4 and R5, with the remaining three minutes for the bounded-claim frame and transitions. Explain sycophancy as unearned agreement, not friendliness. Separate the historical model benchmark, immediate social intentions and optional-AI reasoning experiments.'))
S.extend(study('R3',
    'The same work got different feedback.',
    'Can your product challenge accurately?',
    'Sharma et al., Towards Understanding Sycophancy in Language Models, ICLR 2024, arXiv 2310.13548. Connect behaviour to training/evaluation and product feedback, not an intention to flatter. Instructor-authored contrast, not study stimuli: supportive response acknowledges a feeling while questioning an unsupported conclusion; sycophantic response endorses the conclusion because the user holds it. Do not imply that every current model always agrees. Figure 1 quantitative panel, revised v4 PDF/printed p.3: same passages under all four preference/ownership cues and five models. Feedback positivity is GPT-4-judged more-positive-than-baseline frequency, not factual accuracy. The 50% line is comparison baseline. Figure does not prove RLHF alone causes sycophancy; optimization results are mixed. Axes/legend/SE retained; exact crop and rights caveat in week08-paper-figures.md.',
    image='r3-figure.png',
    attribution='Sharma et al., Fig. 1 (quantitative panel), v4 PDF p.3.\n50% = no directional shift; positivity, not accuracy.',
    block='AGREEMENT / MODEL BEHAVIOUR'))
S.extend(study('R4',
    'More right, less willing to repair.',
    'What would satisfaction metrics miss?',
    'Cheng et al. (2026), final Science eaec8352 full article via public mirror; publisher blocked, supplement not reviewed. Final experiments: 804 + 801 vignette participants and 800 in an eight-turn live interpersonal-conflict chat; total 2,405, not preprint 1,604. Methods/results PDF pp. 5-7. Binary affirming versus disapproving responses, no neutral user-study baseline. Immediate repair/rightness contrasts are experimental; measured traits or benchmark associations are not causal for that reason. Prosocial intentions are not observed reconciliation; trust/return ratings are not diagnosed addiction. US/English context, no repeated-use longitudinal harm demonstration. Product inference: evaluate downstream choices as well as liking. Ask whether a kind but accurate challenge could differ from these binary conditions. Figure 4 A+B, final PDF p.7 / printed 6 of 9, all three experiments. Means are 1-7 rating scales, y-axis begins at 2, uncertainty is 95% CI. Printed percentages are relative rating changes, not percentage-point probabilities. Observe higher rightness/lower repair intentions; no observed real reconciliation. This is final N=2405, not preprint N=1604. No neutral experimental comparator. Exact crop/access/AAAS rights caveat in week08-paper-figures.md.',
    image='r4-figure.png',
    attribution='Cheng et al. (2026), Fig. 4 A+B, final PDF p.7.\nRatings on 1-7 scales; y-axis starts at 2; 95% CIs.',
    block='AGREEMENT / SOCIAL INTENTIONS'))
S.append(paper_detail('R4', 'Feeling right is not repairing a conflict.', 'r4-figure.png',
    'Cheng et al., Fig. 4 A+B, final PDF p.7. Means on 1-7 scales; axis starts at 2; 95% CIs.',
    'Same R4 teaching allocation in the13-minute agreement/overreliance block, not extra time. Explain orange affirming versus blue disapproving responses, all three experiments. Left: perceived rightness higher; right: intended repair lower. The chart does not show later reconciliation or addiction. Keep y-axis baseline2 visible; compare mean ratings, not bar-length ratios. Printed percentages are relative mean differences, not percentage-point probabilities. The return-preference result comes from separate analyses, not these panels. Final N2405, no neutral comparator. Primary final Science Figure4A+B, PDFp.7/printed6of9, retained public mirror; supplement not reviewed. Exact crop, access and unresolved AAAS republication rights in week08-paper-figures.md.'))
S.extend(study('R5',
    'Many followed the planted wrong answer.',
    'Make checking easier than accepting?',
    'Shaw and Nave (2026), Thinking-Fast, Slow, and Artificial. Full 58-page January 11 PsyArXiv v1 read; related SSRN February revision not retrieved or verified byte-identical to supplied PDF. Working paper, not peer reviewed. Procedures pp. 18-22: seven adapted Cognitive Reflection Test items, optional GPT-4o with seeded correct or confidently faulty replies; person retains final answer. Synthesis N=1,372 includes an ancillary sample, not Study 1 alone. The 79.8% faulty-answer adoption is conditional on AI-consulted trials, NOT 80% of all users. Incentives PLUS feedback reduced, not eliminated, faulty adoption; do not isolate their effects. Limitations pp. 48-49: narrow controlled snapshot, no longitudinal deskilling. Proposed System 3 is a theoretical account, not anatomy. Candidate design test: independent estimate before suggestion or easier comparison, not an established fix. Figure 2, January v1 PDF p.23: complete chart explicitly says Chat-Engaged Only. Among consulted trials, 92.7% followed accurate and 79.8% followed faulty advice; rounded chart labels 93/80. SE bars, not CIs; override difference is about 13 percentage points, not 13% relative. Optional consultation was chosen and occurs on only about 53-54% of trials. No population-wide 80% obedience claim. Full crop and version/rights caveat in week08-paper-figures.md.',
    image='r5-figure.png',
    attribution='Shaw & Nave, Fig. 2, January v1 PDF p.23.\nWorking paper. Consulted trials only; bars show SE.',
    block='OVERRELIANCE / WORKING PAPER'))

# 65-75 minutes: the bridge from research to product responsibility.
S.append(content('65-75 / A CASE IS A DIFFERENT KIND OF EVIDENCE', 'An update can change the relationship.', [
    'OpenAI reported rolling back an April 2025 GPT-4o update after overly agreeable behaviour.',
    'This is a vendor incident account, not a controlled study of prevalence or harm.',
    'Ask: what did the evaluation miss, and what could the user notice or undo?',
    '[Read the vendor account: Sycophancy in GPT-4o](https://openai.com/index/sycophancy-in-gpt-4o/)',
], body_size=34,
    notes='Use the verified official account, not a reconstructed screenshot or unsourced incident detail. Separate vendor explanation from independent research. Do not include the optional BBC case: the full report has not been verified here and a non-graphic anecdote still cannot establish causation. Friend is not necessary for this teaching decision; omit unverified current product claims rather than inventing them. Ask how a version change could invalidate an earlier product test.'))
S.append(figure_slide('PRODUCT ANALYSIS / FROM THE HISTORICAL WEEK 8 FRAME', 'Data. AI. Experience.', F.layers(),
    caption='Illustrative product: an AI rehearsal partner for a difficult conversation. Not a validated intervention.',
    notes='Work through one example: collect a fictional scenario, not a real identifiable transcript; generate alternatives, not a judgment about who is right; let a person edit, reject and leave. Data: minimum needed, access, retention/deletion. AI: what feedback rewards, source uncertainty and failure modes. Experience: what warmth or memory implies, what the user actually does next. These are candidate design responses, not proven safeguards. Psychological ownership is not legal ownership: optional R11 stays in appendix. R10 can deepen privacy later.'))
transfer = paper_frame('R7', 'From a finding to a product test.', 'RESEARCH -> YOUR PROJECT',
    'Replaces original slide 35. Read the three steps aloud. Evidence: 65% versus 59% of follow-up respondents reported initiating a difficult conversation, comparing AI preparation with unrelated factual chat. Our proposed team-feedback rehearsal feature was not tested in that study. Proposed test: randomly offer optional AI rehearsal or preparation on their own, then ask next week whether intended users started their chosen conversation; this comparator differs from R7. Participation and disclosure remain optional. This is a test plan, not a new result, a validated safeguard or a claim of better relationships. Measure actual self-reported initiation separately from feeling ready. Teams should repeat this reasoning with papers relevant to their own product. Two minutes within the existing implications block.')
for y, label, value in [
    (350, '1 / FINDING', 'After AI preparation, 65% reported starting a difficult conversation; after unrelated factual chat, 59% did. This is R7\'s result.'),
    (540, '2 / FEATURE IDEA', 'For a team-feedback app: let someone rehearse asking a teammate to share the work. This is our idea; R7 did not test it.'),
    (730, '3 / PROPOSED TEST', 'Offer AI rehearsal or preparation on their own. Next week, ask: did you start the conversation? Compare the groups.'),
]:
    transfer.els += [Rect(120, y, 1680, 2, '#D5DCDA'),
                     T(120, y + 28, 330, 60, label, 'mono', 26, '#246E70'),
                     T(490, y + 24, 1310, 145, value, 'body', 36, INK, lh=1.2)]
transfer.els.append(T(120, 956, 1680, 38, source('R7'), 'mono', 21, INK, lh=1.1))
S.append(transfer)
S.append(statement('Break.\n15 minutes.', eyebrow_text='75-90 / RELATIVE CLASS TIME', size=120,
    notes='Preserve the full fifteen-minute break. Announce the actual return clock time only after the dated timetable is confirmed. Next: fifteen-minute library demo, forty-minute search/read, twenty-five-minute scope/design/test revision and ten-minute comparison. Open the manual fallback and checked reading links before the return.'))

# 90-105: a manual route works without an agent or Scopus abstracts.
S.append(two_col('90-105 / SEARCH FROM THE PRODUCT QUESTION', 'Search a condition, not a verdict.',
    ['Example: when does AI rehearsal help someone prepare for a difficult conversation?',
     'Combine person + system + context + outcome. Try synonyms; remove one block if results are sparse.',
     'Do not begin with "prove AI companions are good/bad".'],
    ['("AI" OR chatbot OR "conversational agent")', 'AND (rehearsal OR preparation)',
     'AND ("difficult conversation" OR conflict)', 'Then vary: initiation / avoidance / disclosure.'],
    left_size=32, right_size=28, lang=None,
    notes='First three minutes of the fifteen-minute demo. This is an example query, not a promise that every database implements identical syntax. Show a broad first pass then refine. A fashion product might use recommendation + body image + choice rather than the whole mental-health register. Include studies that complicate the hoped-for mechanism. No private student or user data in queries.'))
S.append(content('MANUAL DEMO / BASELINE, NOT BACKUP THEATRE', 'Find. Open. Read. Follow the trail.', [
    '[Open PolyU Library](https://www.lib.polyu.edu.hk/) -> discovery or a relevant subject database.',
    'Search terms; inspect title, authors, year and article type. Filters are not quality guarantees.',
    'Open the publisher record; try library access or a lawful author manuscript. Record abstract-only access.',
    'Follow a useful paper\'s references and citing papers; verify each record independently.',
], body_size=33,
    notes='About seven minutes. Demonstrate the actual library route without hard-coded unverified menu labels. Do not project credentials or personal library records, automate gated access or assume Scopus returns abstracts. If library login/database/network fails: open R8 by its DOI (open access); use its title, authors, abstract, methods and references to show the same steps. If completely offline, use the instructor demo card in lessons/week08-demo-fallback.md and the saved evidence audit: metadata/passage/limit/transfer are still inspectable; label this a prepared example, not a live search or systematic review. Teams can select candidate citations now and complete lawful full-text checking later, marking uncertainty.'))
S.append(content('OPTIONAL AGENT / SAME VERIFICATION STANDARD', 'Discovery is not paper reading.', [
    'Ask for candidate papers and primary links, not a confident verdict.',
    'Open each DOI: do title, authors, year and version actually match?',
    'Separate metadata found / abstract read / full text read. Ask for a supporting passage and location.',
    'If the agent or abstract access fails, continue manually with the same evidence card.',
], body_size=34,
    notes='Final five minutes of the same fifteen-minute demo, not extra time. Live agent mode is optional and NOT preflighted by this deck. Default is a manual audit of one candidate. If instructor separately preflights an agent, compare its returned metadata and claim with the primary source in front of the class. Scopus metadata access is not abstract/full-text access. Never display tokens, bypass access restrictions, upload student concepts verbatim or cite an invented passage. An honest access gap is a useful outcome.'))

# 105-145: instructions and the individual submission share ONE forty-minute block.
S.append(activity('01 / SEARCH + READ', 40, 'Find 2-3 papers for your product.', [
    'Start from one uncertainty about your existing user, context and AI action.',
    'Seek conditions for benefit and for risk/problem. Record mixed or missing evidence.',
    'Each person chooses a different paper and submits its URL + project relevance in ClassPoint.',
], notes='105-145, one forty-minute block across slides 40-43. Suggested internal checkpoints: 0-5 question/terms and divide the search; 5-20 discovery/access; 20-35 close reading; 35-40 compare and submit. These are not extra activity timers. Start with 2-3 relevant papers, then extend as needed so each teammate submits a different paper; 2-3 is not a cap on the team total. Aim for evidence illuminating benefit and risk/problem without forcing an equal pro/con quota or predetermined verdict. Do not pad the list with irrelevant papers. TAs ask about methods and transfer, not whether the team agrees with the lecture. Keep evidence cards in ordinary team notes. Instructor-requested formative submission: every student sends one primary paper URL/DOI and why it is relevant to the group project, not one spokesperson per team. No grade or additional Canvas upload/deadline is introduced.'))
S.append(content('SAME 40-MINUTE BLOCK / EVIDENCE CARD', 'Read beyond the abstract.', [
    'Citation + link + version; access: abstract only or full text.',
    'People / system / task / comparator / outcome / duration.',
    'One finding + exact supporting passage and page or section + one limitation.',
    'Our use: what does it support, what does it not support, and what remains unknown?',
], body_size=35,
    notes='Leave this up during close reading if useful. For HTML without page numbers use section/subheading and a short exact passage. Clearly label author interpretation versus measured result and the team\'s inference. Abstract-only: record what it says, but do not fill in missing methods or fabricate a quotation from the article. Do not let an agent supply a page it has not retrieved. A review paper can locate studies; a primary study is needed for a specific empirical claim. Teams need not share private experiences, participant information or identifiable user transcripts.'))
S.append(figure_slide('SAME 40-MINUTE BLOCK / CHECK TRANSFER', 'Is this evidence about your product?', F.transfer(),
    caption='Compare population, system, task, outcome, setting and time. Keep a mismatch visible in the team notes.',
    notes='Near the end of research, ask each team for one match and one mismatch. A loneliness study does not directly validate a fashion recommender; a student sample is not every older adult; a supervised intervention is not an unsupervised consumer app. No relevant full text found? Narrow the claim, state access limits and make the next search explicit. Absence of retrieved evidence is not proof of no effect. Transition only after the forty-minute block is protected.'))
S.append(question('short_answer', PAPER_SUBMISSION_TITLE,
    hint='Each person: a different paper from your teammates.\nPaste its URL + why it is relevant to your group project.',
    eyebrow_text='105-145 / SAME RESEARCH BLOCK / EVERYONE SUBMITS',
    cp={'type': 'short_answer', 'hide_names': False, 'multiple': False},
    notes='Use the final five minutes of the existing forty-minute research block; no extra submission block. Each student submits one response containing a primary paper URL or DOI and one or two sentences explaining its relevance to the existing group project. Coordinate within the team so teammates choose different papers, not duplicate submissions through a spokesperson. A group may need more than the starting 2-3 papers to cover its members. Tie relevance to a user, AI action, evidence question or design decision; briefly state a transfer/access limit if needed. Do not paste private project details, student/user identifiers, full papers or copyrighted full-text excerpts. This is formative collection, not a new grade, quota beyond one paper per person, or Canvas deadline. This is a named classroom submission, not an anonymous reflection. Review any report for private content before ordinary after-class publication; unlike the two personal reflections, this non-sensitive activity can use the normal report-link workflow. If ClassPoint fails, retain the URL and explanation in team notes and arrange the normal instructor-led recovery, not a new public board.'))

# 145-170: one twenty-five-minute revision block, three outputs in team notes.
S.append(activity('02 / SCOPE + INTERACTION + TEST', 25, 'Change a claim before adding a feature.', [
    'KEEP / CHANGE / REMOVE: one assumption, linked to a paper and its limitation.',
    'State person, context, AI action and necessary data. Name what it will not collect, promise or do.',
    'Output: revised scope + one interaction change + one test in your team notes.',
], notes='145-170, one twenty-five-minute block across slides 44-46. Suggested internal allocation: eight minutes scope, eight interaction, nine test. Do not add these to the forty-minute research block or recollect Week 7 submissions. A paper can support retaining a choice as well as changing it. Use this work to strengthen the existing Week 8 one-page proposal; confirm Canvas deadline separately. Research can reveal an access or evidence gap; the appropriate revision may be a narrower claim rather than a confident feature.'))
S.append(cards('SAME 25-MINUTE BLOCK / ANNOTATE ONE MOMENT', 'Make the evidence change the interaction.', [
    ('CUE', 'What is implied?', 'Change one name, voice, memory claim or disclosure. Explain the expected effect.'),
    ('CONTROL', 'What can be refused?', 'Make correction, comparison, exit or a human route concrete.'),
    ('MECHANISM', 'Why this change?', 'Link paper -> finding -> transfer limit -> design hypothesis. Sketch if useful.'),
], text_size=31, notes='A sketch is a thinking aid, not a newly assessed deliverable. Ask what changed because of evidence; adding the word ethical is not a design change. No universal safe persona: warmth or friction can help in some conditions and hinder in others. Any proposed safeguard needs testing. The product may not involve conversation; adapt to recommendations, generated options or a hidden decision.'))
S.append(content('SAME 25-MINUTE BLOCK / SPECIFY THE NEXT TEST', 'What result would change your mind?', [
    'Compare [version A] with [version B] for [intended users] doing [a safe task].',
    'Observe [behaviour or outcome], not only whether they like the interface.',
    'Before testing, state: if we observe [result], we will revise [decision].',
    'Use fictional, low-stakes scenarios. A classroom test cannot establish clinical safety.',
], body_size=35,
    notes='Expected output: one falsifiable question, a comparison, observable outcome and revision criterion. Example only: two non-sensitive rehearsal flows; measure whether participants can identify uncertainty and choose a next step without unnecessary disclosure. This does not validate therapeutic efficacy. Do not recruit vulnerable participants, induce distress, collect health data or conduct a clinical trial in class. A future user study may require ethics approval. Ask about a competing explanation and what the small test cannot show.'))
S.append(content('170-180 / SELECTED COMPARISONS', 'Show the decision, not a pro/con list.', [
    'We assumed ... We found ... The important limitation is ...',
    'So we will keep / change / remove ... Our next comparison is ...',
    'Another team: what evidence would challenge that inference?',
], body_size=38, notes='Use about seven of the final ten minutes for two or three selected examples, not compulsory presentations from every team. One minute per team plus questions. Invite an unresolved contradiction and a search that found weak evidence. No personal mental-health stories, public student artifacts or new upload requirement. Compare quality of inference, not which team found the strongest anti/pro-AI headline.'))
S.append(content('FINISH / KEEP THE EVIDENCE BASE GROWING', 'Your next version needs a reason.', [
    'Keep the papers, evidence cards, revised scope and next test in your project workspace.',
    'Use them for the existing one-page proposal; check the actual brief and deadline on Canvas.',
    'Week 9: recommendations and bias. Week 10: interactive Double Diamond.',
    'Weeks 11-12: ethics. Week 13: showcase and reflection.',
], body_size=35, notes='Final three minutes. No new assessment, changed weight or invented submission deadline. Teaching direction confirmed on October 21: Week 9 recommendations/bias; Week 10 interactive Double Diamond while the instructor is absent; Week 11 ethics, agency and authorship; Week 12 ethics, trust and design responsibility; Week 13 student showcase and reflection. The published syllabus still has the older Week 8-10 sequence and is not rewritten here. The exact dates, coverage person, timetable, ESFQ arrangements and quiz policy remain unconfirmed; do not announce them as settled or infer assessment cancellation. Check current official instructions. A useful uncertainty is better than a confident invented citation. Appendix follows for reading and reference, not further timed lecture.'))

MAIN_SLIDE_COUNT = len(S)

S.append(cards('APPENDIX / READING MAP / NOT EXTRA LECTURE TIME', 'What was actually read?', [
    ('PUBLISHED TEXT', 'Primary articles.', 'R1-R4, R6, R8-R10, R12-R13: published full texts reviewed. R4/R9 via public mirrors; supplements not obtained.'),
    ('OTHER VERSIONS', 'Name the version.', 'R7: accepted author manuscript. R11: GI 2026 author preprint v3. R5: January PsyArXiv v1, not peer reviewed.'),
    ('TEAM STANDARD', 'Do not fill gaps.', 'Metadata found, abstract read and full text read are different states. Mark yours; never invent a passage or result.'),
], text_size=29, notes='Instructor reference shelf. All thirteen primary article texts were available for this authoring pass in the versions listed, not just abstracts. Publisher blocks for R4/R9 were not bypassed; public mirror primary texts were cross-checked with author/publication records. Their supplements remain unreviewed. R7 manuscript is not the typeset version of record; R11 is a conference author preprint. R5 January version is not asserted identical to the supplied/SSRN revision. Detailed access, supporting sections/pages and caveats are in the two evidence ledgers. Students must label their actual access separately.'))

S.extend(study('R9',
    'Optional / Symptoms improved with support.',
    'Which conditions would your product lose?',
    'Optional two-minute contrast; shorten detail, not team research. Heinz et al. (2025), full published article reviewed via public mirror because publisher endpoint was blocked; supplement and separate disclosures not obtained. Methods pp. 3-4: adults with clinically significant depression/anxiety or high-risk eating-disorder concerns; active suicidality, mania and psychosis excluded. Expert-built system, all responses supervised POST-transmission by trained clinicians/researchers, with correction and safety intervention. Tables pp. 5-6 support symptom findings. Access continued during weeks 4-8, so eight-week improvement is not maintenance after withdrawal. Waitlist is not an active human-therapy comparator; alliance comparison uses historical norms, not randomized parity. Do not transfer to unsupervised general companions.',
    method=[('STUDY', '210 adults / randomized waitlist'),
                      ('INTERVENTION', 'Expert-built + human-supervised'),
                      ('OUTCOME', 'Symptom scales at 4 and 8 weeks')],
    block='APPENDIX / OPTIONAL CONTRAST'))


for key, guide in EXTENSION_GUIDES.items():
    recap = paper_frame(key, guide['title'], 'OPTIONAL / PAPER RECAP',
        guide['task'] + ' ' + guide['measured'] + ' ' + guide['result'] + ' ' + guide['limit'] +
        ' Example is a teaching adaptation, not a verbatim study prompt. ' + guide['source_locations'] +
        ' This is an untimed reference slide; keep the scheduled research and revision blocks.')
    paper_block(recap, 120, 348, 780, 'TRY THE STUDY / TEACHING EXAMPLE', guide['example'], 260, size=38)
    paper_block(recap, 120, 716, 780, 'WHAT THEY STUDIED', guide['task'], 165, size=30)
    paper_block(recap, 1020, 348, 780, 'WHAT THEY MEASURED', guide['measured'], 135, size=30)
    paper_block(recap, 1020, 550, 780, 'WHAT THEY FOUND', guide['result'], 135, size=30)
    paper_block(recap, 1020, 752, 780, 'WHAT IT DOES NOT SHOW', guide['limit'], 135, size=30)
    recap.els.append(T(120, 956, 1680, 38, source(key), 'mono', 21, INK, lh=1.1))
    S.append(recap)


def bibliography(heading, paragraphs, notes, size=30):
    return content('APPENDIX / COMPLETE REFERENCES', heading, paragraphs,
                   body_size=size, notes=notes)


S.append(bibliography('R1 / Response quality + correction', [
    "Hatch, S. G., Goodman, Z. T., Vowels, L., Hatch, H. D., Brown, A. L., Guttman, S., Le, Y., Bailey, B., Bailey, R. J., Esplin, C. R., Harris, S. M., Holt, D. P., Jr., McLaughlin, M., O'Connell, P., Rothman, K., Ritchie, L., Top, D. N., Jr., & Braithwaite, S. R. (2025).",
    'When ELIZA meets therapists: A Turing test for the heart and mind. PLOS Mental Health, 2(2), e0000145. [Article](https://doi.org/10.1371/journal.pmen.0000145)',
    'Same authors (2025). Correction: When ELIZA meets therapists: A Turing test for the heart and mind. PLOS Mental Health, 2(8), e0000426. [Correction](https://doi.org/10.1371/journal.pmen.0000426)',
], 'Full published PLOS article/XML and correction reviewed. Keep corrected funding and competing interests with the interpretation, as detailed in the R1 summary notes and the benefits evidence ledger. This is vignette-rating evidence, not treatment. The correction has the same author list shown above.', size=28))
S.append(bibliography('R2 + R8 / Source, rating and choice', [
    'Jain, G., Pareek, S., & Carlbring, P. (2024). Revealing the source: How awareness alters perceptions of AI and human-generated mental health responses. Internet Interventions, 36, 100745. [R2 / article](https://doi.org/10.1016/j.invent.2024.100745)',
    'Wenger, J. D., Cameron, C. D., & Inzlicht, M. (2026). People choose to receive human empathy despite rating AI empathy higher. Communications Psychology, 4, 19. [R8 / article](https://doi.org/10.1038/s44271-025-00387-3)',
], 'Both full published texts reviewed. R2: six-month timing, attrition and Table 1 versus Discussion inconsistency constrain disclosure claims. R8: four brief nonclinical studies, 691 source-choice participants; experienced response ratings involve chosen sources, not randomized source assignment. Neither measures therapeutic effectiveness.'))
S.append(bibliography('R6 + R7 / Relief and human action', [
    'De Freitas, J., Oguz-Uguralp, Z., Uguralp, A. K., & Puntoni, S. (2026; online 2025). AI companions reduce loneliness. Journal of Consumer Research, 52(6), 1126-1148. [R6 / article](https://doi.org/10.1093/jcr/ucaf040)',
    'Maheshka, C., Folk, D., & Dunn, E. (2026). Harnessing artificial intelligence to facilitate difficult conversations. Social Psychological and Personality Science, advance online publication. [R7 / article](https://doi.org/10.1177/19485506261444068)',
], 'R6 final five-study publisher article reviewed from author-hosted copy, not older six-study working paper. First online June 25, 2025. Immediate relief did not accumulate or persist between interactions. R7 full accepted author manuscript reviewed; publisher record May 5, 2026. At next-week follow-up 65% versus 59% self-reported initiation, N=1,371. Unmatched duration and factual-chat control; not comparison to human rehearsal or proof of conversation quality.'))
S.append(bibliography('R9 / A specific supervised intervention', [
    'Heinz, M. V., Mackin, D. M., Trudeau, B. M., Bhattacharya, S., Wang, Y., Banta, H. A., Jewett, A. D., Salzhauer, A. J., Griffin, T. Z., & Jacobson, N. C. (2025).',
    'Randomized trial of a generative AI chatbot for mental health treatment. NEJM AI, 2(4), AIoa2400802. [R9 / article](https://doi.org/10.1056/AIoa2400802)',
    'Transfer boundary: 210 adults, waitlist comparison, clinician/researcher supervision and eligibility exclusions. Access continued through week 8.',
], 'Full published primary article reviewed via a public mirror; publisher endpoint blocked. Cross-checked author and institutional records. Supplementary Appendix and separate disclosures not obtained. No full-paper PDF or publisher figure redistributed. Alliance comparison is not a randomized comparison to human therapy.'))
S.append(bibliography('R3 / Sycophancy and preferences', [
    'Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., Cheng, N., Durmus, E., Hatfield-Dodds, Z., Johnston, S. R., Kravec, S., Maxwell, T., McCandlish, S., Ndousse, K., Rausch, O., Schiefer, N., Yan, D., Zhang, M., & Perez, E. (2024).',
    'Towards Understanding Sycophancy in Language Models. International Conference on Learning Representations. Consulted revised arXiv v4 (10 May 2025). [R3 / primary text and version](https://arxiv.org/abs/2310.13548v4)',
    'Tested historical assistants; preference optimization had mixed effects, not a universal increase in sycophancy.',
], 'Full revised conference-paper primary text reviewed. Tested Claude 1.3/2.0, GPT-3.5-turbo/GPT-4 and Llama-2-70b-chat. Human preference associations and optimization experiments are distinct evidence. Being warm or agreeing with a true claim is not itself sycophancy.'))
S.append(bibliography('R4 + R5 / What happens after agreement?', [
    'Cheng, M., Lee, C., Khadpe, P., Yu, S., Han, D., & Jurafsky, D. (2026). Sycophantic AI decreases prosocial intentions and promotes dependence. Science, 391(6792), eaec8352. [R4 / final article](https://doi.org/10.1126/science.aec8352)',
    'Shaw, S. D., & Nave, G. (2026, January 11). Thinking-Fast, Slow, and Artificial: How AI is Reshaping Human Reasoning and the Rise of Cognitive Surrender. Working paper, PsyArXiv v1. [R5 / consulted version](https://doi.org/10.31234/osf.io/yk25n_v1)',
    'Related R5 [SSRN record](https://doi.org/10.2139/ssrn.6097646): February revision not directly reviewed. Short tasks, not long-term skill loss.',
], 'R4 full final paper via public mirror, supplementary material not obtained. Three experiments N=2,405; measured intentions and return preference, not diagnosed addiction. R5 full January 11 v1; not peer reviewed and not asserted byte-identical to the supplied/SSRN revision. Numeric adoption rates are conditional on consultation; no need to teach a misleading headline percentage.'))
S.append(bibliography('Optional / R10 + R11 / Privacy and ownership', [
    'Cao, J., Dong, Y., Zhan, C., Neti, R., Peddinti, S. T., & Emami-Naeini, P. (2026). Understanding U.S. Users\' Security and Privacy Transparency Needs for Consumer-Facing Generative AI. SOUPS 2026, 647-664. [R10 / proceedings](https://www.usenix.org/conference/soups2026/presentation/cao)',
    'Joshi, N., & Vogel, D. (2026). Interaction Techniques that Encourage Longer Prompts Can Improve Psychological Ownership when Writing with AI. Graphics Interface 2026, 11 pp. [R11 / DOI](https://doi.org/10.1145/3831423.3831427); [consulted v3](https://arxiv.org/abs/2507.03670v3).',
    'R10: qualitative transparency needs, not prevalence. R11: reported ownership in short-story tasks, not copyright or a universal benefit of friction.',
], 'Optional reading, not extra timed lecture or newly assigned homework. R10 full proceedings reviewed: 21 US interviews, 20 completed design sessions. R11 full GI author preprint v3 reviewed: 29 and 30 analyzed participants; prompting friction affected reported ownership; AI suggestions increased length without additional ownership gain. Neither supports a universal interface prescription.', size=28))
S.append(bibliography('Later / R12 + R13 / Process and discussion', [
    'S\u00f6zen, T., & B\u00f6rek\u00e7i, N. A. G. Z. (2026). Analyzing the integration of generative AI in the design process through the double-diamond framework. AI EDAM, 40, e9. [R12 / article](https://doi.org/10.1017/S0890060426100304)',
    'Yu, M., Liu, Z., Long, T., Li, D., Deng, L., Kong, X., & Sun, J. (2025). Exploring cognitive presence patterns in GenAI-integrated six-hat thinking technique scaffolded discussion: an epistemic network analysis. International Journal of Educational Technology in Higher Education, 22, 48. [R13 / article](https://doi.org/10.1186/s41239-025-00545-x)',
    'R12 maps practices; it does not prove a superior design process. R13 studies coded discourse networks; more posts do not automatically mean deeper learning.',
], 'Both final published full texts reviewed. R12: 88 valid survey responses, 10 think-aloud professional designers in T\u00fcrkiye; 2024 tool use, exploratory analysis, no formal inter-rater reliability. Keep the framework distinct from this study. R13: 108 pre-service teachers, narrow structured setting; overall code distribution nonsignificant, ENA connections are a different outcome. Avoid source-inconsistent count/duration details. Not automatically transferable to design students.', size=28))
S.append(bibliography('Frameworks + product account', [
    'Ihde, D. (1990). Technology and the Lifeworld: From Garden to Earth. Indiana University Press. Established Week 5 framework, not newly full-book reviewed.',
    'Verbeek, P.-P. (2015). Beyond interaction: A short introduction to mediation theory. Interactions, 22(3), 26-31. [Article](https://doi.org/10.1145/2751314)',
    'OpenAI. (2025, April 29). Sycophancy in GPT-4o: What happened and what we\'re doing about it. [Vendor account](https://openai.com/index/sycophancy-in-gpt-4o/)',
], 'Verbeek full six-page author-hosted published article reviewed; mediation/alterity explanation on printed p.29 (PDF position 4). Ihde framework carried from the established course source and checked through Verbeek, not a claim to newly read the whole book. OpenAI is a vendor release/rollback account, not independent empirical research. All custom diagrams are original conceptual teaching illustrations, not empirical data or faithful model-internals diagrams.'))

def protected_report_entries(source):
    """Never expose personal-reflection report URLs; retain normal drift checks."""
    entries = [dict(entry) for entry in load_reports(source)]
    targets = [slide for slide in S if slide.cp]
    for slide, entry in zip(targets, entries):
        if slide.title in PRIVATE_REFLECTION_TITLES:
            entry['activity'] = None
            entry['withheld'] = 'personal reflection; do not publish'
    return entries


attach_reports(S, protected_report_entries(Path(__file__).resolve().parent / 'week08-reports.json'))
DECK = dict(title='SD2112 / AI in Design / Week 08',
            slides=finalize(S, footer(8)), pdf='SD2112-week08.pdf')
