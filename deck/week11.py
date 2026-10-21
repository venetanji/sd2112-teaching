"""Week 11: evidence, representation, credit, agency and responsibility."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import (title, content, cards, statement, two_col, activity,
                             finalize, T, Rect)
from course import footer

REFS = {
    'N': ('Naqvi, He & Kaur / CHI 2025', 'https://harmanpk.github.io/Papers/CHI2025_GenAI-Design.pdf'),
    'D': ('Doshi & Hauser / Science Advances 2024', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/'),
    'J': ('Joshi & Vogel / GI 2026 / author v3', 'https://arxiv.org/abs/2507.03670v3'),
    'G': ('Gebru et al. / Datasheets for Datasets / 2021', 'https://arxiv.org/abs/1803.09010v8'),
    'U': ('U.S. Copyright Office / Part 2 / January 2025', 'https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf'),
    'V': ('Verbeek / Beyond Interaction / 2015', 'https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf'),
}


def source(key):
    label, url = REFS[key]
    return f'[{label}]({url})'


SCHEDULE = [(0, 15, 'Recover the decision', (1, 3)),
            (15, 45, 'Read the evidence', (4, 9)),
            (45, 75, 'Curation and authorship', (10, 16)),
            (75, 90, 'Break', (17, 17)),
            (90, 110, 'Research to communication', (18, 20)),
            (110, 140, 'Team evidence and curation audit', (21, 23)),
            (140, 165, 'Peer reading and revision', (24, 26)),
            (165, 180, 'Compare and prepare', (27, 28))]
S = []

# Native shapes and text keep this conceptual figure editable and mobile-readable.
def curation_comparison():
    s = content('CURATION / FICTIONAL PRODUCT / ORIGINAL TEACHING DIAGRAM',
        'Three candidates. One stated criterion.', [], title_size=64, bg=PAPER,
        notes='45-75 block, about five minutes. Fictional AI exhibition guide; all three candidate summaries are instructor-authored, NOT outputs of a model or tested interfaces. Criterion: visitors can identify the source and choose another account. Read each candidate before revealing the judgment verbally. A is fluent but hides provenance; B makes disagreement possible; C names a missing voice rather than fabricating it. B is a starting choice, not a universally best UI; C may be needed alongside it. Ask who can afford the extra reading effort, and what an accessible alternative would require. We have not measured comprehension, trust or inclusion. A native editable comparison replaces the old interactive curation sketch; no shared-toolchain port is claimed.')
    s.els = s.els[:2]
    candidates = [
        ('A / POLISHED', 'The definitive story.', 'One confident summary.\nNo source or alternative.', 'REJECT: certainty hides a choice.'),
        ('B / TRACEABLE', 'An account, not the account.', 'Named source and date.\nCompare another perspective.', 'SELECT FOR TEST: trace + choice.'),
        ('C / INCOMPLETE', 'A voice is missing.', 'No community account yet.\nInvite a correction; do not invent it.', 'RETAIN THE GAP: inclusion is work.'),
    ]
    for i, (label, head, body, verdict) in enumerate(candidates):
        x = 120 + i * 570
        s.els += [Rect(x, 354, 540, 2, '#A4B4B5'),
                  T(x, 386, 540, 40, label, 'monomed', 23, '#246E70'),
                  T(x, 458, 530, 125, head, 'xbold', 37, INK, lh=1.05),
                  T(x, 620, 530, 150, body, 'body', 29, INK, lh=1.35),
                  T(x, 820, 530, 110, verdict, 'body', 27, INK, lh=1.3)]
    return s


S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 11',
    'Whose design?', 'Ethics I: representation. Credit. Agency. Responsibility.',
    notes='Opening, 0-15. Today links research begun in Week 8 and the current state of Week 10 testing to the existing project. Do not assume a finished or successful prototype. The main route is 28 slides in exactly 180 minutes: opening 15; evidence 30; curation/authorship 30; break 15; worked communication 20; audit 30; peer revision 25; debrief 15. No appendix, new assessment or extra submission. Historical 2025 materials are sources, not current logistics.'))
S.append(content('0-15 / RESEARCH -> PRODUCT -> PROJECT', 'What changed, and for whom?', [
    'Open your existing concept, evidence and test notes. A rough draft is enough.',
    'Name one product decision that changed - or a failed test that should change it.',
    'Who benefits? Who supplies material or labour? Who bears an error or exclusion?',
    'Today: evidence -> a justified selection -> a visible poster and mediation argument.',
], body_size=35, notes='Use roughly five minutes within the opening. Teams discuss one actual change, including no change if evidence is unresolved. Avoid asking for sensitive user records or personal experiences. Research is not newly starting today; use accumulated sources. No public collection. If a team has no test, mark its assumption untested rather than inventing success.'))
S.append(cards('ETHICAL ARGUMENT / NOT AN AI CHECKLIST', 'A good-looking output is not enough.', [
    ('REPRESENTATION', 'Who gets shown?', 'Whose examples and interpretation become the default? Who is missing?'),
    ('AGENCY + VALUES', 'Who can disagree?', 'Ease versus variety; speed versus control. Can affected people contest the choice?'),
    ('CREDIT + DUTY', 'Who answers for it?', 'Name contributors and material sources. Who can correct, withdraw or repair a failure?'),
], text_size=30, notes='Finish the opening with a five-minute comparison of competing values in one team example. Representation is not just demographic counting: ask who frames the category and whose account is treated as authoritative. Credit does not substitute for consent or redistribute decision power. Responsibility must name an actor and action, not the phrase human in the loop. Today we will make this argument legible in the existing deliverables.'))
S.append(cards('15-45 / READ A PAPER AS AN ARGUMENT', 'Follow the chain, not the quotation.', [
    ('QUESTION + METHOD', 'What could this study know?', 'Who, system, task, comparison, outcome and time. Interviews and experiments answer different questions.'),
    ('RESULT + LIMIT', 'What did it actually find?', 'Locate a methods/results passage. Separate measured result from author interpretation and missing evidence.'),
    ('DESIGN INFERENCE', 'What can we test next?', 'State the transfer gap. A relevant paper informs a choice; it does not certify your product.'),
], text_size=29, notes='About four minutes. Introduction frames the gap; methods specify what was done; results report observations; discussion interprets them. Abstracts help choose a paper but compress method and scope. Demonstrate a short passage in the checked Naqvi author PDF if network access works. Offline use slides 5-6 and the source ledger explicitly as a prepared reading, not a live search. More citations do not cure an unsupported inference.'))
S.append(two_col('DESIGN INTERVIEWS / N', 'Different experience. Different values.', [
    '28 artifact-based interviews: 10 junior students, 10 senior students, 8 professionals, all U.S.-based.',
    'Participants described different views of AI, foundational skills and ownership.',
    source('N'),
], ['METHOD / SECTIONS 3 + 6', 'Discuss a previously made artifact; thematic analysis of interviews.',
    'BOUNDARY', 'Self-selected sample; accounts of practice, not randomized evidence that AI causes skill loss.',
    'TRANSFER QUESTION', 'Whose experience is missing from our own product research?'],
    left_size=30, right_size=28, right_font='body', lang=None,
    notes='Naqvi, He and Kaur, CHI 2025, author-hosted ACM-formatted full text, 16 pages. Methods PDF4-5: June-August 2024 Zoom interviews; artifacts were made before the study, not assigned experimental tasks. Recruitment through university groups, social media and snowball sampling; selection requires prior image-generation experience. Sections 4.4/4.5 report contrasting values, not a ranking of good and bad designers. Section 6, PDF13-14: self-selection, one-artifact elicitation, fast-changing tools, prompt-based tools and exclusively U.S. sample. Do not call this a longitudinal skill test because cohorts entered design at different times. About five minutes.'))
S.append(two_col('CLOSE READING / N / SECTION 4.5', 'A participant claim is not a legal rule.', [
    'Junior participants described shared authorship; seniors linked ownership to input and editing.',
    'Some professionals shifted ownership and accountability towards tool developers.',
    source('N'),
], ['READ THE STATUS OF THE CLAIM', 'These are participant perspectives interpreted by the researchers.',
    'NOT ESTABLISHED', 'Who legally owns the work, or who can escape responsibility.',
    'OUR DESIGN QUESTION', 'What process history would make contributions and decisions inspectable?'],
    left_size=30, right_size=29, right_font='body', lang=None,
    notes='About five minutes. Open section 4.5 on PDF8; ask students to identify whose voice is speaking. The heading Ownership and Intellectual Property does not turn interviews into legal analysis. Junior shared-authorship, senior input/editing and professional developer-accountability themes are supported in sections 4.5.1-3, not universal opinions of all people at each career stage. Do not quote the derogatory lazy-designers remark from a different section as a finding of measured skill loss. Process-history interface is our candidate response, not an intervention evaluated in this paper.'))
S.append(two_col('RANDOMIZED SHORT-STORY STUDY / D', 'Better rated stories. More similar stories.', [
    '293 writers: no AI ideas, one available idea, or up to five GPT-4 starting ideas. 600 separate evaluators.',
    'AI access improved average novelty/usefulness ratings; assisted stories were more similar within condition.',
    source('D'),
], ['TWO OUTCOMES', 'Individual story ratings and embedding-based similarity across stories are different measures.',
    'BOUNDARY', 'Eight-sentence stories; nonprofessional writers; no iterative chat. Not a design-studio or long-term learning trial.',
    'ASK', 'Can a portfolio improve locally yet narrow collectively?'],
    left_size=29, right_size=28, right_font='body', lang=None,
    notes='Doshi and Hauser, Science Advances 10 eadn5290, 12 July 2024. Final primary article read through Europe PMC full-text XML after publisher PDF returned 403. Introduction/Fig1 and Methods: UK Prolific writers randomly assigned access, optionally request three-sentence GPT-4 ideas; writing remains human. 293 completed included stories, not all 500 recruited. Separate 600 evaluators initially rated without access information; later exploratory ownership questions are separate. Results Similarity of stories/Fig4: cosine similarity of each story embedding to the mean of OTHER stories within its condition, not a direct count of cultural perspectives. Randomized access supports bounded causal claims, not all use patterns. Authors note short task, nonprofessional sample and no interactive iteration. Supplement not independently retrieved. About six minutes; avoid percentages without denominators.'))
S.append(cards('COMPARE THE EVIDENCE / THEN PROPOSE A TEST', 'Control and variety are not the same goal.', [
    ('N / INTERVIEWS', 'Agency and contribution.', 'Reported concerns make process visibility worth investigating. They do not establish that a history panel works.'),
    ('D / EXPERIMENT', 'Quality and convergence.', 'Better average story ratings can coexist with greater similarity. Similarity is not itself a measure of fair representation.'),
    ('OUR HYPOTHESIS', 'Ideate, then compare.', 'Try an independent first sketch before AI suggestions; test variety AND relevance. This intervention is not proven by either paper.'),
], text_size=29, notes='About five minutes. Do not contrast qualitative and quantitative as weak versus strong: they illuminate different questions. Both can expose missing perspectives, but neither tests our proposed independent-first interface. Ask whether speed, access, control and diversity conflict for the intended person. A design team may reasonably choose assistance while making the trade-off and evaluation visible. Do not label a low-diversity result unfair without examining who or what is excluded.'))
S.append(content('CITATION AUDIT / THE LAST FIVE MINUTES OF THIS BLOCK', 'Could another reader check your inference?', [
    'Claim: "AI destroys designers\' skills." -> Not established by these interviews.',
    'Revision: "Interviewees raised concerns about foundations; our project has not measured learning."',
    'Keep citation + version + access + passage location + method + limit + your design inference.',
    'If only the abstract is accessible, say so. Narrow or remove unsupported claims.',
], body_size=35, notes='Use five minutes within 15-45, not a new timed team audit. Ask pairs to say the difference between evidence and interpretation aloud. Point to Naqvi section 6 and Doshi Discussion as scope checks. A search agent may find candidates but must not invent passages or page numbers. No agent or library login is required for this prepared lesson; source cards remain a fallback. Keep team source trails in their ordinary workspace, not a new upload.'))
S.append(statement('Selection changes\nwhat the world\ngets to see.', eyebrow_text='45-75 / CURATION IS A DESIGN DECISION', bg=PAPER, size=104,
    notes='Two-minute transition. Choosing a generated output, assembling a reference board, choosing a LoRA dataset and deciding what a product retrieves all allocate visibility. They are different technical operations, but all need a purpose and a reason for inclusion/exclusion. Do not imply retrieval automatically trains model weights. We will work through a fictional exhibition guide rather than train a model or require a dataset today.'))
S.append(curation_comparison())
S.append(cards('DATASET CHOICE / TRAINING, RETRIEVAL AND REFERENCE DIFFER', 'A coherent set can hide an absence.', [
    ('PURPOSE', 'Similar in what way?', 'For a LoRA: what appearance should be learned? For retrieval: which accounts should be findable?'),
    ('COMPOSITION', 'Whose variation?', 'One photographer, venue or language may look coherent while excluding other conditions and voices.'),
    ('CONSEQUENCE', 'Missing is not neutral.', 'Name the gap and who bears it. Seek permission and relevant variation; do not fabricate a missing community voice.'),
], text_size=29, notes='About four minutes. Week 5 established LoRA as parameter-efficient adaptation; today discusses selection, not a compulsory training exercise. Training examples affect learned patterns; a retrieval collection affects what can be surfaced without necessarily changing weights. Neither an aesthetically uniform set nor a simple balanced count guarantees adequate representation. For the guide example: a pristine institutional photograph and a community account serve different purposes; one cannot substitute for the other. Ask what evidence would justify inclusion and how to invite correction.'))
S.append(content('DOCUMENTATION / SELECTED QUESTIONS, NOT A CERTIFICATION', 'Make the material traceable.', [
    'Purpose + composition: why this set, what is missing, and what uses are unsuitable?',
    'Provenance + permission: creator/source, collection context, licence or consent scope; record unknowns.',
    'Care + accountability: sensitive content, affected people, access, maintenance and a correction/removal route.',
    source('G') + ' - documentation supports scrutiny; it does not guarantee harmlessness.',
], body_size=34, notes='About four minutes. Gebru et al., author arXiv v8 (1 December 2021), sections 1.1-3: questions on motivation, composition, collection, processing, uses, distribution and maintenance. A documentation proposal developed through examples and feedback, not a randomized harm-reduction trial. Adapt a few questions; no mandatory full datasheet, fixed image count or personal camera-roll collection. The public availability of an image is not consent to expose the people in it. Do not project private source material.'))
S.append(cards('AUTHORSHIP MAP / CREDIT DOES NOT END ACCOUNTABILITY', 'Name the work behind the output.', [
    ('MATERIAL', 'Who made it possible?', 'Reference creators, data contributors and tool/model providers. Attribute sources and record intended-use permission.'),
    ('DECISIONS', 'Who changed what?', 'Who framed the question, generated, selected, arranged and revised? Keep rejected alternatives and reasons.'),
    ('RESPONSIBILITY', 'Who can act now?', 'Name who checks claims, hears objections, stops release and repairs a failure. "The AI did it" is not an action plan.'),
], text_size=29, notes='About four minutes. Separate contributors from decision authority and responsibility. Record actual team roles in the private project workspace, not student names in course source. Do not anthropomorphize a model as a legal co-author. Documentation is evidence of process, not a guarantee of originality, fairness or lawful reuse. Ask which contributor the final poster might make invisible and whether that person can contest the use.'))
S.append(two_col('PSYCHOLOGICAL OWNERSHIP / J', 'Feeling yours is not having rights.', [
    'Short-story experiments: interfaces added time or motor effort to submitting short prompts.',
    'Prompts grew longer and reported psychological ownership exceeded baseline.',
    source('J'),
], ['METHOD + LIMIT', '29 analyzed in experiment 1; 30 new participants in experiment 2. Baseline always first; brief writing tasks.',
    'IMPORTANT CONTRAST', 'AI suggestions made prompts longer still, without a further significant ownership gain.',
    'NOT MEASURED', 'Legal ownership, design quality or long-term creative agency.'],
    left_size=30, right_size=28, right_font='body', lang=None,
    notes='About five minutes. Joshi and Vogel, GI 2026, author preprint arXiv 2507.03670v3, July 12 2026, 11 pages; this is not the earlier 2025 version. Sections 4 and 6: first recruited 35, analyzed 29 after exclusions; second 30 new participants. Within-subject techniques time (press/hold) and motor (pump slider); psychological ownership is a four-item self-report composite. Section 6.2 contrasts suggestions versus none across experiments: extra words do not imply additional significant ownership. Sections 7/7.1: baseline-first and short-task/interface limits; effort correlations do not isolate a universal causal mechanism. Ask whose accessibility or urgency needs a friction interface may disadvantage. Do not infer that longer prompts earn copyright.'))
S.append(content('U.S. COPYRIGHT OFFICE / GUIDANCE, NOT A WORLDWIDE RULE', 'Separate expression, permission and credit.', [
    'Part 2 (January 2025): human-authored expression can be protected in a work containing AI material.',
    'The Office says prompts alone do not supply sufficient control with the technology it analyzed; human contributions are assessed case by case.',
    'Creative arrangement or modification may qualify; that does not protect every AI-generated component or permit reuse of someone else\'s work.',
    source('U') + ' - U.S. guidance; checked 21 October 2026. Not Hong Kong legal advice.',
], body_size=32, notes='About six minutes, ending at 75. Official Part2 retrieved directly, Executive Summary printed iii and II.C-F printed11-27. Official AI index rechecked by web fetch on 21 October 2026: still links January2025 Part2; Part3 training labelled pre-publication. Node index returned403, alternate first-class web extraction succeeded; PDF direct200. Only bounded report positions are taught, not a claim of exhaustively current law worldwide. Distinguish copyrightability from third-party infringement/licence, privacy/consent, ethical credit and patents. No live lawsuit status, Thaler, Google Books analogy, Udio/Suno verdict or fair-use clearance is asserted. Hong Kong and any intended market need appropriate current local guidance before a real release. Unknown permission: hold or replace the material and seek qualified support.'))
S.append(statement('Break.\n15 minutes.', eyebrow_text='75-90 / RELATIVE CLASS TIME', size=120,
    notes='Keep the entire fifteen-minute break. State the actual clock return time in the room, not an invented dated timetable. Next twenty minutes is a worked poster/mediation/video example, followed by the protected thirty-minute audit, twenty-five-minute peer revision and fifteen-minute debrief.'))
S.append(two_col('90-110 / A0 POSTER / FICTIONAL EXHIBITION GUIDE', 'Make the inference visible.', [
    'BEFORE: "Our AI guide democratises culture and gives everyone a voice."',
    'AFTER: "Visitors compare sourced interpretations. We are testing whether this makes disagreement easier."',
    'N informs our agency question; D warns us to inspect similarity, not just attractive individual outputs.',
], ['VISIBLE POSTER STORY', 'Person + need -> evidence + limit -> AI decision -> consequence + open test.',
    'ETHICAL ARGUMENT', 'Visitors, contributors and absent communities; convenience versus plural accounts.',
    'DESIGN HYPOTHESIS', 'Show source/date, alternate account and correction route. Not yet a proven safeguard.'],
    left_size=31, right_size=29, right_font='body', lang=None,
    notes='About eight minutes of 90-110. Fictional product, not a real student project or validated intervention. Show that claims can become more precise without becoming timid. Naqvi interviews inform the control question but are not visitor research; Doshi story similarity suggests a portfolio question but does not measure cultural representation. The proposed compare/correct interaction needs visitor and contributor testing. Poster hierarchy should let a passing reader identify product, evidence and trade-off without narration. A source number alone is not an argument; make the limit and inference readable. Keep A0 requirement; no new print deadline or compulsory section quota.'))
S.append(content('ONE-PAGE MEDIATION BRIEF / SAME FICTIONAL GUIDE', 'Name the relation and the responsible actor.', [
    'Relation: a hermeneutic guide makes an interpretation of an exhibit seem authoritative.',
    'Data + bias: sourced institutional accounts; community perspectives are missing. Speed competes with plurality.',
    'Contestability: visitors compare and flag an account; contributors can request correction or withdrawal.',
    'Accountability: the editorial team reviews flags and can pause a disputed account. Test access and response, not just the button. ' + source('V'),
], body_size=32, notes='About seven minutes. Recall Week5/8: hermeneutic relation means reading a technologically mediated representation, not looking through a neutral window; conversational delivery could also invite alterity. Verbeek is conceptual grounding, not experimental proof of this interface. Candidate guardrails include source visibility, alternative accounts and a staffed correction route; do not promise operational response times or claim that a disclaimer removes bias. Teams adapt to their own product rather than copy the museum example. A one-page brief should connect relation, data, bias and guardrails to real consequences, including whose objection can trigger action.'))
S.append(cards('3-5 MINUTE VIDEO / SAME PROJECT ARGUMENT', 'Show a decision and its consequences.', [
    ('MOMENT OF USE', 'What does AI decide?', 'Show the visitor, the suggested account and the information used. A mock-up is honest if labelled.'),
    ('CONTEST + REPAIR', 'What can a person do?', 'Show comparison or correction and who receives it. Do not stage an untested success as a research result.'),
    ('EXISTING CONTRACT', 'Three forms, one argument.', 'A0 poster + 3-5 minute video + one-page mediation brief. Group project: 40% of the course.'),
], text_size=29, notes='Final five minutes of 90-110. Explain the same argument across poster, video and brief rather than adding another deliverable. Existing project rubric is research/context30%, ethical/sociological impact30%, communication/poster20%, video10%, collaboration/process10% WITHIN the project, which is40% of the course. The syllabus already lists draft poster and mediation brief at Week11; confirm actual Canvas instructions, do not shift/cancel them. No same-night date, mandatory model training, four-group quota or new grade. If video not made yet, storyboard this moment in ordinary team notes.'))
S.append(activity('01 / EVIDENCE + CURATION AUDIT', 30, 'Find one claim and one choice.', [
    'Use your current notes, concept board or poster. Polish is not required.',
    '0-5: choose an important claim. 5-15: trace its source and narrow the inference.',
    '15-25: justify an included/rejected material. 25-30: make the ethical trade-off visible.',
], notes='110-140, exactly one thirty-minute activity across slides21-23. No ClassPoint collection, extra upload or new assessed component. Preserve the existing Week11 draft-poster/mediation milestone. Team may work on one paragraph or diagram. TAs ask who is affected and whether the actual source warrants the claim. If full text unavailable, document abstract-only and do not invent missing method. Use owned/licensed non-sensitive material; no personal camera-roll mining.'))
S.append(content('SAME 30-MINUTE AUDIT / SOURCE -> CLAIM -> DECISION', 'Narrow the claim until it fits.', [
    'Record citation/link/version and access level; locate the supporting methods/results passage.',
    'Name population, system, task, comparison, outcome and time; say what does not transfer.',
    'Rewrite one poster claim. Keep published result, your interpretation and proposed test distinct.',
    'If only a vendor claim or an untested assumption supports it, label that honestly.',
], body_size=35, notes='Checkpoint for minutes5-15 inside the audit, not an additional ten-minute exercise. Teams can reuse existing evidence cards; no quota of new papers. For a design interview claim ask whose view; for an experiment ask comparator and outcome; for a product announcement say vendor report. A missing or contradictory source is a reason to narrow/remove the claim. Keep sensitive user records off screen and outside public repos.'))
S.append(content('SAME 30-MINUTE AUDIT / SELECTION -> CONSEQUENCE', 'Make the curation decision inspectable.', [
    'Choose one included output or dataset/reference item. State the criterion and one rejected alternative.',
    'Record creator/source, permitted use and unknowns. Remove or replace unsuitable material.',
    'Name an affected person, a competing value and a remaining exclusion or uncertainty.',
    'Show how someone can contest it and who can change the decision or repair the consequence.',
], body_size=34, notes='Checkpoint for minutes15-30 inside the same audit. Material may be an image, output, example or retrieval source; no fixed contact-sheet size. A record of rejection makes judgment inspectable but does not make it automatically defensible. Encourage dissent within the team. A team without a finished poster can annotate its concept image or brief paragraph. Output stays in ordinary project notes and the existing draft; no collection badge or required extra artifact.'))
S.append(activity('02 / PEER READING + REVISION', 25, 'Let the argument travel without you.', [
    '0-8: exchange a readable draft with another team. Authors listen before explaining.',
    '8-15: readers state product, AI choice and evidence; ask one evidence and one communication question.',
    '15-25: authors revise one element and keep the unresolved ethical trade-off visible.',
], notes='140-165, one twenty-five-minute block across slides24-26, not three activities. Exchange with another team; this is not the historical2025 obligation to give feedback to four groups. No new marks, mandatory public post or feedback submission. Work with accessible readable text/diagram; pair verbally if needed. Reviewers should not request private data or copyrighted full articles. Leave10 minutes for actual revision.'))
S.append(content('SAME 25-MINUTE BLOCK / READERS', 'What did you understand - and miss?', [
    'Say the product, its AI decision and the evidence you understood, without the authors\' explanation.',
    'Evidence question: which source/method supports this specific claim, and where does transfer fail?',
    'Communication question: where does the diagram or wording hide a choice or imply certainty?',
    'Name affected people, competing values and who could contest or bear the failure.',
], body_size=35, notes='Use during0-15 of the peer block. Reviewers describe the reading first; authors do not defend immediately. Seek one substantive evidence question and one communication question, not a popularity score or aesthetic vote. A peer can identify a missing argument without being an expert in the field. Ask how a less powerful stakeholder might read the same poster. Feedback does not determine marks.'))
S.append(content('SAME 25-MINUTE BLOCK / AUTHORS', 'Revise the argument, not just the decoration.', [
    'Record the mismatch between what you meant and what the readers understood.',
    'Revise a claim, caption, diagram or brief paragraph so evidence and inference can be distinguished.',
    'Keep the cost of your choice visible: who may lose control, recognition, access or representation?',
    'Check the contest route and responsible actor. An attractive disclaimer is not a repair plan.',
], body_size=35, notes='Use during15-25 of the peer block. Do not spend all25 minutes discussing; protect actual editing. Teams may reject a suggestion if they explain the reason, but should record the evidence gap. They need not solve every trade-off today. Compare actual before/after wording or figure; do not fabricate a better outcome. No additional required submission.'))
S.append(content('165-180 / COMPARE THE REVISIONS', 'What became more defensible?', [
    'Show a before/after: one claim became more precise; one selection became more legible.',
    'Name an affected person, competing values and the person or role accountable for the next action.',
    'What remains unknown? What evidence could change your choice?',
    'What can someone contest - and what will happen after they do?',
], body_size=35, notes='First ten minutes of the final fifteen. Invite a few voluntary examples or discuss in pairs if projection would expose sensitive materials. No additional ClassPoint prompt or assessment. Compare precision and accountability, not whether every team chose the same safeguard. A narrower claim and a visible gap can be genuine progress. Instructor records unresolved support needs without public student names.'))
S.append(content('EXISTING BRIEF / PREPARE FOR THE MOCK REVIEW', 'Research. Choice. Responsibility.', [
    'Keep the trail with the project: source -> bounded claim -> selected material -> decision -> remaining risk.',
    'Bring the same argument into the A0 poster, 3-5 minute video and one-page mediation brief.',
    'Project rubric: research 30 / ethics 30 / poster 20 / video 10 / process 10. These are project weights, not course weights.',
    'Week 11 already lists draft poster + mediation brief. Follow current Canvas milestones; confirm mock-review logistics there.',
], body_size=32, notes='Last five minutes, ending at180. Group project remains40% of course; rubric30/30/20/10/10 only within that project. No new deadline, print requirement, upload route or changed mark. Confirm how the current Week12 mock review and existing milestones are communicated before teaching. The historical2025 Week14 exam, Nov dates, Blackboard/Excalidraw instructions and four-group feedback quota are deliberately not inherited. End with the ethical question: whose evidence, whose material and whose responsibility?'))

attach_reports(S, Path(__file__).resolve().parent / 'week11-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 11',
            slides=finalize(S, footer(11)), pdf='SD2112-week11.pdf')
