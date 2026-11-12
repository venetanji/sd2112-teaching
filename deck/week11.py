"""Week 11: evidence, representation, credit, agency and responsibility."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import (title, content, cards, statement, two_col, activity,
                             finalize, T, Rect, Image, section, _slide, eyebrow)
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



PAPER_SUMMARIES = {}
PAPER_ASSETS = Path(__file__).resolve().parent / 'assets/week11'


def paper_frame(key, heading, phase, notes):
    """Week-owned implementation of the approved Week 8 paper grid."""
    s = _slide('#FFFFFF', notes, title=heading)
    s.els += [eyebrow(120, 96, phase + ' / ' + key, '#246E70'),
              T(120, 184, 1680, 140, heading, 'xbold', 72, INK,
                lh=.95, spc=-.03, name='paper-title')]
    return s


def paper_block(s, x, y, width, label, value, height, name):
    s.els += [T(x, y, width, 34, label, 'mono', 23, '#246E70', name=name+'-label'),
              T(x, y+52, width, height, value, 'body', 34, INK,
                lh=1.2, name=name+'-body')]


def paper_task(key, heading, task, comparison, example, measured, notes,
               example_kind='ILLUSTRATIVE EXAMPLE / NOT STUDY WORDING', conceptual=False):
    s = paper_frame(key, heading, 'THE ARGUMENT' if conceptual else 'THE STUDY', notes)
    labels = ('QUESTION + APPROACH', 'WHAT IS ANALYZED', example_kind, 'BASIS / NOT A PARTICIPANT EXPERIMENT') if conceptual else ('WHAT THEY DID', 'WHAT THEY COMPARED', example_kind, 'WHAT THEY MEASURED')
    for x,y,label,value,height,name in [
        (120,348,labels[0],task,210,'study-task'),
        (120,676,labels[1],comparison,154,'study-comparison'),
        (1020,348,labels[2],example,210,'study-example'),
        (1020,676,labels[3],measured,190,'study-measurement')]:
        paper_block(s,x,y,780,label,value,height,name)
    s.els.append(T(120,956,1680,38,source(key),'mono',21,INK,lh=1.1))
    PAPER_SUMMARIES[key] = dict(task=task,comparison=comparison,example=example,measured=measured,conceptual=conceptual)
    return s


def paper_result(key, heading, finding, limit, design, notes, asset=None, caption=None):
    s = paper_frame(key,heading,'THE RESULT' if key in 'NDJ' else 'WHAT THE ARGUMENT SUPPORTS',notes)
    if asset:
        s.els.append(Image(120,348,1010,515,str(PAPER_ASSETS/asset),'contain',name='paper-image',url=REFS[key][1]))
        s.els.append(T(120,884,1010,64,caption,'mono',20,'#246E70',lh=1.2))
        for y,label,value,name,height in [(348,'OFFICE POSITION' if key == 'U' else 'FINDING',finding,'study-result',170),(602,'LIMIT',limit,'study-limit',135),(812,'FOR YOUR DESIGN',design,'study-design',90)]:
            paper_block(s,1190,y,610,label,value,height,name)
    else:
        for x,y,label,value,height,name in [(120,348,'REPORTED THEMES / NOT CAUSAL' if key == 'N' else 'ARGUMENT / NOT A MEASURED EFFECT',finding,210,'study-result'),(1020,348,'WORKED EXAMPLE / INSTRUCTOR ILLUSTRATION',design,210,'study-example'),(120,676,'WHAT IT DOES NOT ESTABLISH',limit,180,'study-limit')]:
            paper_block(s,x,y,780,label,value,height,name)
    s.els.append(T(120,956,1680,38,source(key),'mono',21,INK,lh=1.1))
    return s


def paper_figure(key, heading, asset, explanation, location, notes):
    s = paper_frame(key,heading,'READ THE FIGURE',notes)
    s.els += [Image(120,332,1680,540,str(PAPER_ASSETS/asset),'contain',name='paper-image',url=REFS[key][1]),
              T(120,884,1680,64,explanation,'body',27,INK,lh=1.15),
              T(120,956,1680,38,source(key)+' / '+location,'mono',21,INK,lh=1.1)]
    return s

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
    notes='Opening, 0-15. Today links research begun in Week 8 and the current state of Week 10 testing to the existing project. Do not assume a finished or successful prototype. The main route is 32 slides plus one optional historical appendix in exactly 180 minutes: opening 15; evidence 30; curation/authorship 30; break 15; worked communication 20; audit 30; peer revision 25; debrief 15. The appendix is optional background, not pre-reading. No new assessment or extra submission. Historical 2025 materials are sources, not current logistics.'))
S.append(content('0-15 / RESEARCH -> PRODUCT -> PROJECT', 'What changed, and for whom?', [
    'Open the existing project. A rough draft is enough.',
    'Which decision changed? Which failed test should change it?',
    'Who benefits, supplies material, or bears an error?',
    'Evidence -> selection -> a defensible argument.',
], body_size=35, notes='Use roughly five minutes within the opening. Teams discuss one actual change, including no change if evidence is unresolved. Avoid asking for sensitive user records or personal experiences. Research is not newly starting today; use accumulated sources. No public collection. If a team has no test, mark its assumption untested rather than inventing success.'))
S.append(cards('ETHICAL ARGUMENT / NOT AN AI CHECKLIST', 'A good-looking output is not enough.', [
    ('REPRESENTATION', 'Who gets shown?', 'Whose examples and interpretation become the default? Who is missing?'),
    ('AGENCY + VALUES', 'Who can disagree?', 'Ease versus variety; speed versus control. Can affected people contest the choice?'),
    ('CREDIT + DUTY', 'Who answers for it?', 'Name contributors and material sources. Who can correct, withdraw or repair a failure?'),
], text_size=30, notes='Finish the opening with a five-minute comparison of competing values in one team example. Representation is not just demographic counting: ask who frames the category and whose account is treated as authoritative. Credit does not substitute for consent or redistribute decision power. Responsibility must name an actor and action, not the phrase human in the loop. Today we will make this argument legible in the existing deliverables.'))
S.append(cards('15-45 / READ A PAPER AS AN ARGUMENT', 'Follow the chain, not the quotation.', [
    ('QUESTION + METHOD', 'What could this study know?', 'Who? What task? What comparison? Interviews and experiments ask different questions.'),
    ('RESULT + LIMIT', 'What did it actually find?', 'Find the passage. Separate observation, interpretation and missing evidence.'),
    ('DESIGN INFERENCE', 'What can we test next?', 'Name the transfer gap. A paper informs a choice; it cannot certify your product.'),
], text_size=29, notes='About two minutes. Introduction frames the gap; methods specify what was done; results report observations; discussion interprets them. Abstracts help choose a paper but compress method and scope. Demonstrate a short passage in the checked Naqvi author PDF if network access works. Offline use slides 5-6 and the source ledger explicitly as a prepared reading, not a live search. More citations do not cure an unsupported inference.'))
S.append(paper_task('N', 'What did designers describe?', '28 U.S. participants discussed an AI image they had already made: 10 junior students, 10 senior students and 8 professionals. Interviews took 30-45 minutes in June-August 2024.', 'The researchers compared themes across experience groups. Nobody was assigned to use or avoid AI; no skill test was run.', 'A source-described artifact began as a kayaker photograph, was transformed with AI, then manually colour-edited. What work would the final image hide?', 'Interview transcripts were coded into themes about practice, values and ownership. These are reported experiences, not a score or a causal test of skill loss.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. Naqvi, He and Kaur, CHI 2025, author-hosted ACM-formatted full text, 16 pages. Methods PDF4-5: June-August 2024 Zoom interviews; artifacts were made before the study, not assigned experimental tasks. Recruitment through university groups, social media and snowball sampling; selection requires prior image-generation experience. Sections 4.4/4.5 report contrasting values, not a ranking of good and bad designers. Section 6, PDF13-14: self-selection, one-artifact elicitation, fast-changing tools, prompt-based tools and exclusively U.S. sample. Do not call this a longitudinal skill test because cohorts entered design at different times. About four minutes within the Naqvi pair. Source-adapted text example from Fig. 1(d), PDF9; image omitted because public-republication permission is not established. An interview artifact: AI-transformed kayak photograph, then manually colour-edited. The final image hides that process.', example_kind='SOURCE ADAPTATION / FIG. 1(d), PDF 9'))
S.append(paper_result('N', 'A participant view is not a legal rule.', 'Juniors described shared authorship; seniors linked ownership to input/editing; professionals discussed developer responsibility.', 'Self-selected U.S. accounts do not establish legal rights or caused skill loss.', 'Make contributions visible; test whether people can contest the choice.', 'About three minutes within the Naqvi pair. Open section 4.5 on PDF8; ask students to identify whose voice is speaking. The heading Ownership and Intellectual Property does not turn interviews into legal analysis. Junior shared-authorship, senior input/editing and professional developer-accountability themes are supported in sections 4.5.1-3, not universal opinions of all people at each career stage. Do not quote the derogatory lazy-designers remark from a different section as a finding of measured skill loss. Process-history interface is our candidate response, not an intervention evaluated in this paper. No participant artwork is reproduced in this public-review set. The source-adapted kayak workflow on the preceding slide illustrates why process history matters without treating an interview theme as a legal judgment.'))
S.append(paper_task('D', 'Write a story. Change the starting help.', '293 UK writers produced an eight-sentence story for young readers. Random assignment: no AI ideas, access to one, or up to five GPT-4 starting ideas.', 'Writers wrote their own story. 600 separate evaluators each rated six stories before learning about AI access.', 'One assigned topic was an adventure on the open seas. AI supplied a starting idea, not an iterative conversation or the finished eight sentences.', 'Readers rated novelty and audience/publishing usefulness from 1 (not at all) to 9 (extremely). Researchers also compared story embeddings: similarity from 0 to 100.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. Doshi and Hauser, Science Advances 10 eadn5290, 12 July 2024. Final primary article read through Europe PMC full-text XML after publisher PDF returned 403. Introduction/Fig1 and Methods: UK Prolific writers randomly assigned access, optionally request three-sentence GPT-4 ideas; writing remains human. 293 completed included stories, not all 500 recruited. Separate 600 evaluators initially rated without access information; later exploratory ownership questions are separate. Results Similarity of stories/Fig4: cosine similarity of each story embedding to the mean of OTHER stories within its condition, not a direct count of cultural perspectives. Randomized access supports bounded causal claims, not all use patterns. Authors note short task, nonprofessional sample and no interactive iteration. Supplement not independently retrieved. Task and result share eight minutes, followed by the two-minute similarity detail; avoid percentages without denominators. The following authentic Fig. 2A crop shows rating differences from human-only. The separate similarity detail retains the top Fig. 4A panel. Source adaptations are not invented observations.', example_kind='SOURCE ADAPTATION / METHODS'))
S.append(paper_result('D', 'Higher ratings can accompany convergence.', 'AI access raised average novelty and usefulness ratings. The two AI conditions also produced more similar stories.', 'A short writing task, not studio learning; similarity does not count cultural voices.', 'Inspect the portfolio, not only its best item.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. Doshi and Hauser, Science Advances 10 eadn5290, 12 July 2024. Final primary article read through Europe PMC full-text XML after publisher PDF returned 403. Introduction/Fig1 and Methods: UK Prolific writers randomly assigned access, optionally request three-sentence GPT-4 ideas; writing remains human. 293 completed included stories, not all 500 recruited. Separate 600 evaluators initially rated without access information; later exploratory ownership questions are separate. Results Similarity of stories/Fig4: cosine similarity of each story embedding to the mean of OTHER stories within its condition, not a direct count of cultural perspectives. Randomized access supports bounded causal claims, not all use patterns. Authors note short task, nonprofessional sample and no interactive iteration. Supplement not independently retrieved. Task and result share eight minutes, followed by the two-minute similarity detail; avoid percentages without denominators. The following authentic Fig. 2A crop shows rating differences from human-only. The separate similarity detail retains the top Fig. 4A panel. Source adaptations are not invented observations.', asset='doshi-f2-novelty-usefulness.png', caption='Doshi & Hauser (2024), Fig. 2A crop, CC BY 4.0. Dots: differences from human-only; bars: uncertainty.'))
S.append(cards('COMPARE THE EVIDENCE / THEN PROPOSE A TEST', 'Control and variety are not the same goal.', [
    ('N / INTERVIEWS', 'Agency and contribution.', 'Reported concerns suggest a question about control. No interface remedy was tested.'),
    ('D / EXPERIMENT', 'Quality and convergence.', 'Higher ratings can coexist with greater similarity. Similarity is not fairness.'),
    ('OUR HYPOTHESIS', 'Ideate, then compare.', 'Try independent sketches before AI suggestions. Test variety AND relevance. Not proven by these papers.'),
], text_size=29, notes='About five minutes. Do not contrast qualitative and quantitative as weak versus strong: they illuminate different questions. Both can expose missing perspectives, but neither tests our proposed independent-first interface. Ask whether speed, access, control and diversity conflict for the intended person. A design team may reasonably choose assistance while making the trade-off and evaluation visible. Do not label a low-diversity result unfair without examining who or what is excluded.'))
S.append(content('CITATION AUDIT / THE LAST FIVE MINUTES OF THIS BLOCK', 'Could another reader check your inference?', [
    'Claim: "AI destroys designers\' skills." -> Not established by these interviews.',
    '"Interviewees raised concerns; we have not measured learning."',
    'Keep source, passage, method, limit and your inference.',
    'Abstract only? Say so. Narrow or remove the claim.',
], body_size=35, notes='Use five minutes within 15-45, not a new timed team audit. Ask pairs to say the difference between evidence and interpretation aloud. Point to Naqvi section 6 and Doshi Discussion as scope checks. A search agent may find candidates but must not invent passages or page numbers. No agent or library login is required for this prepared lesson; source cards remain a fallback. Keep team source trails in their ordinary workspace, not a new upload.'))
S.append(statement('Selection changes\nwhat the world\ngets to see.', eyebrow_text='45-75 / CURATION IS A DESIGN DECISION', bg=PAPER, size=104,
    notes='Two-minute transition. Choosing a generated output, assembling a reference board, choosing a LoRA dataset and deciding what a product retrieves all allocate visibility. They are different technical operations, but all need a purpose and a reason for inclusion/exclusion. Do not imply retrieval automatically trains model weights. We will work through a fictional exhibition guide rather than train a model or require a dataset today.'))
S.append(curation_comparison())
S.append(cards('DATASET CHOICE / TRAINING, RETRIEVAL AND REFERENCE DIFFER', 'A coherent set can hide an absence.', [
    ('PURPOSE', 'Similar in what way?', 'Training: what should be learned? Retrieval: what should be found?'),
    ('COMPOSITION', 'Whose variation?', 'One photographer, venue or language can hide missing voices.'),
    ('CONSEQUENCE', 'Missing is not neutral.', 'Name the gap and who bears it. Seek permission; never invent a community voice.'),
], text_size=29, notes='About four minutes. Week 5 established LoRA as parameter-efficient adaptation; today discusses selection, not a compulsory training exercise. Training examples affect learned patterns; a retrieval collection affects what can be surfaced without necessarily changing weights. Neither an aesthetically uniform set nor a simple balanced count guarantees adequate representation. For the guide example: a pristine institutional photograph and a community account serve different purposes; one cannot substitute for the other. Ask what evidence would justify inclusion and how to invite correction.'))
S.append(paper_task('G', 'What must a dataset explain?', 'Gebru and colleagues propose documentation to help people judge a dataset before using it. They refined questions over roughly two years using examples and feedback.', 'They tried questions on face-image and movie-review datasets, then revised them using product-team, researcher and legal feedback.', 'A review dataset may suit sentiment research. Does that make it suitable for judging a person? Purpose, collection context and missing information matter.', 'This is a documentation proposal with a development process, not a randomized harm-reduction trial. The examples expose unanswered questions, not a safety score.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The question and application share four minutes. Gebru et al., author arXiv v8 (1 December 2021), sections 1.1-3: questions on motivation, composition, collection, processing, uses, distribution and maintenance. A documentation proposal developed through examples and feedback, not a randomized harm-reduction trial. Adapt a few questions; no mandatory full datasheet, fixed image count or personal camera-roll collection. The public availability of an image is not consent to expose the people in it. Do not project private source material. The source example informed the questions; its facsimile is omitted because public-republication permission is not established. Our guide application is an instructor illustration, not an evaluated datasheet.', conceptual=True))
S.append(paper_result('G', 'Document the choice, including the unknowns.', 'Record purpose, contents, collection, uses and maintenance. Explain why a set fits this use; label what is unknown.', 'Documentation supports scrutiny. It does not establish consent, fairness or harmlessness.', 'For our fictional guide: institutional accounts only; community accounts missing. Name who can correct or withdraw an account.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The question and application share four minutes. Gebru et al., author arXiv v8 (1 December 2021), sections 1.1-3: questions on motivation, composition, collection, processing, uses, distribution and maintenance. A documentation proposal developed through examples and feedback, not a randomized harm-reduction trial. Adapt a few questions; no mandatory full datasheet, fixed image count or personal camera-roll collection. The public availability of an image is not consent to expose the people in it. Do not project private source material. The source example informed the questions; its facsimile is omitted because public-republication permission is not established. Our guide application is an instructor illustration, not an evaluated datasheet.'))
S.append(cards('AUTHORSHIP MAP / CREDIT DOES NOT END ACCOUNTABILITY', 'Name the work behind the output.', [
    ('MATERIAL', 'Who made it possible?', 'Name creators, data contributors and providers. Record permission.'),
    ('DECISIONS', 'Who changed what?', 'Who framed, generated, selected and revised? Keep rejected alternatives.'),
    ('RESPONSIBILITY', 'Who can act now?', 'Who checks, hears objections and repairs? "The AI did it" is no plan.'),
], text_size=29, notes='About four minutes. Separate contributors from decision authority and responsibility. Record actual team roles in the private project workspace, not student names in course source. Do not anthropomorphize a model as a legal co-author. Documentation is evidence of process, not a guarantee of originality, fairness or lawful reuse. Ask which contributor the final poster might make invisible and whether that person can contest the use.'))
S.append(paper_task('J', 'Would you type more to avoid friction?', '29 analyzed participants wrote story prompts using three interfaces. A second experiment repeated the task with 30 new participants and added AI suggestions.', 'Normal submit versus hold-button or pump-slider for short prompts. Baseline first; time/motor order randomized.', 'An instructor example: expand a brief story idea, or keep it short and spend effort submitting it. This is not a prompt-length copyright test.', 'Prompt words were counted. Four self-reports about ownership, responsibility and connection were averaged on a 0-100 scale. A higher score means feeling more ownership.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The task and result share seven minutes. Joshi and Vogel, GI 2026, author preprint arXiv 2507.03670v3, July 12 2026, 11 pages; this is not the earlier 2025 version. Sections 4 and 6: first recruited 35, analyzed 29 after exclusions; second 30 new participants. Within-subject techniques time (press/hold) and motor (pump slider); psychological ownership is a four-item self-report composite. Section 6.2 contrasts suggestions versus none across experiments: extra words do not imply additional significant ownership. Sections 7/7.1: baseline-first and short-task/interface limits; effort correlations do not isolate a universal causal mechanism. Ask whose accessibility or urgency needs a friction interface may disadvantage. Do not infer that longer prompts earn copyright. Source image on result slide: Fig. 1(a) / PDF1 / author v3, motor-cost panel only; authentic pixel crop under CC BY 4.0, not our diagram or an outcome chart. Read the example: the progress bar must be green; write more words or move the slider up and down repeatedly. The pictured 113 reps is this interface example, not a universal requirement or study result. Panels (b) press-and-hold and (c) AI suggestions are omitted for legibility; comparisons remain on the task slide. The image and primary citation link to the full source figure. Added friction can also burden users.'))
S.append(paper_result('J', 'More input can feel more yours.', 'Time/motor: longer prompts, higher reported ownership. Suggestions added words, not a clear further ownership gain.', 'Baseline-first order and brief tasks limit inference. No legal rights were measured.', 'Test contribution AND accessibility costs.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The task and result share seven minutes. Joshi and Vogel, GI 2026, author preprint arXiv 2507.03670v3, July 12 2026, 11 pages; this is not the earlier 2025 version. Sections 4 and 6: first recruited 35, analyzed 29 after exclusions; second 30 new participants. Within-subject techniques time (press/hold) and motor (pump slider); psychological ownership is a four-item self-report composite. Section 6.2 contrasts suggestions versus none across experiments: extra words do not imply additional significant ownership. Sections 7/7.1: baseline-first and short-task/interface limits; effort correlations do not isolate a universal causal mechanism. Ask whose accessibility or urgency needs a friction interface may disadvantage. Do not infer that longer prompts earn copyright. Source image on result slide: Fig. 1(a) / PDF1 / author v3, motor-cost panel only; authentic pixel crop under CC BY 4.0, not our diagram or an outcome chart. Read the example: the progress bar must be green; write more words or move the slider up and down repeatedly. The pictured 113 reps is this interface example, not a universal requirement or study result. Panels (b) press-and-hold and (c) AI suggestions are omitted for legibility; comparisons remain on the task slide. The image and primary citation link to the full source figure. Added friction can also burden users.', asset='joshi-fig1a-motor.png', caption='Joshi & Vogel (2026), Fig. 1(a) crop / v3, PDF 1. CC BY 4.0. Motor-cost example; (b)/(c) omitted. Full figure: source link.'))
S.append(paper_task('U', 'Which human expression is protected?', 'The U.S. Copyright Office Part 2 report (January 2025) analyzes copyrightability using law, policy and responses to its public inquiry. It is not a participant experiment.', 'It compares assistance, prompts, human expression and creative editing. Third-party reuse permission is a separate question.', 'An instructor example: a designer arranges a poster and edits generated material. Ask separately what human expression is protectable and whether the inputs may be reused.', 'The basis is legal/policy analysis, not an ownership-feeling scale. Human contributions require case-by-case assessment. U.S. guidance, not Hong Kong legal advice.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The legal question and position share eight minutes, ending at 75. Official Part2 retrieved directly, Executive Summary printed iii and II.C-F printed11-27. Official AI index rechecked by web fetch on 21 October 2026: still links January2025 Part2; Part3 training labelled pre-publication. Node index returned403, alternate first-class web extraction succeeded; PDF direct200. Only bounded report positions are taught, not a claim of exhaustively current law worldwide. Distinguish copyrightability from third-party infringement/licence, privacy/consent, ethical credit and patents. No live lawsuit status, Thaler, Google Books analogy, Udio/Suno verdict or fair-use clearance is asserted. Hong Kong and any intended market need appropriate current local guidance before a real release. Unknown permission: hold or replace the material and seek qualified support. Source image: Executive Summary / PDF8 / iii / January 2025; reproduced crop, not our diagram. Actual Executive Summary excerpt: protectable human expression is distinct from purely generated material. Not an experiment.', conceptual=True))
S.append(paper_result('U', 'Separate protection, permission and credit.', 'Prompts alone: insufficient control with the tools analyzed. Human expression or creative editing may qualify case by case.', 'Not all generated parts are protected. No permission to copy others; not worldwide law.', 'Unknown reuse permission? Hold or replace the material; seek advice.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The legal question and position share eight minutes, ending at 75. Official Part2 retrieved directly, Executive Summary printed iii and II.C-F printed11-27. Official AI index rechecked by web fetch on 21 October 2026: still links January2025 Part2; Part3 training labelled pre-publication. Node index returned403, alternate first-class web extraction succeeded; PDF direct200. Only bounded report positions are taught, not a claim of exhaustively current law worldwide. Distinguish copyrightability from third-party infringement/licence, privacy/consent, ethical credit and patents. No live lawsuit status, Thaler, Google Books analogy, Udio/Suno verdict or fair-use clearance is asserted. Hong Kong and any intended market need appropriate current local guidance before a real release. Unknown permission: hold or replace the material and seek qualified support. Source image: Executive Summary / PDF8 / iii / January 2025; reproduced crop, not our diagram. Actual Executive Summary excerpt: protectable human expression is distinct from purely generated material. Not an experiment.', asset='copyright-summary-excerpt.png', caption='U.S. Copyright Office, Part 2 (Jan. 2025), Executive Summary, PDF 8 / iii. Federal text; not a figure.'))
S.append(statement('Break.\n15 minutes.', eyebrow_text='75-90 / RELATIVE CLASS TIME', size=120,
    notes='Keep the entire fifteen-minute break. State the actual clock return time in the room, not an invented dated timetable. Next twenty minutes is a worked poster/mediation/video example, followed by the protected thirty-minute audit, twenty-five-minute peer revision and fifteen-minute debrief.'))
S.append(two_col('90-110 / A0 POSTER / FICTIONAL EXHIBITION GUIDE', 'Make the inference visible.', [
    'BEFORE: "Our AI guide gives everyone a voice."',
    'AFTER: "Visitors compare sourced accounts. Does disagreement become easier?"',
    'N: ask about agency. D: inspect the whole portfolio.',
], ['VISIBLE POSTER STORY', 'Need -> evidence + limit -> AI choice -> consequence.',
    'ETHICAL ARGUMENT', 'Visitors, contributors, absent communities. Convenience versus plurality.',
    'DESIGN HYPOTHESIS', 'Source, alternate account, correction route. Still a hypothesis.'],
    left_size=31, right_size=29, right_font='body', lang=None,
    notes='About six minutes of 90-110. Fictional product, not a real student project or validated intervention. Show that claims can become more precise without becoming timid. Naqvi interviews inform the control question but are not visitor research; Doshi story similarity suggests a portfolio question but does not measure cultural representation. The proposed compare/correct interaction needs visitor and contributor testing. Poster hierarchy should let a passing reader identify product, evidence and trade-off without narration. A source number alone is not an argument; make the limit and inference readable. Keep A0 requirement; no new print deadline or compulsory section quota.'))
S.append(content('ONE-PAGE MEDIATION BRIEF / SAME FICTIONAL GUIDE', 'Name the relation and the responsible actor.', [
    'Relation: the guide makes one interpretation seem authoritative.',
    'Data: institutional sources; missing community voices. Speed versus plurality.',
    'Contest: visitors compare and flag; contributors request correction.',
    'Accountability: the editorial team reviews flags and can pause an account. Test the response. ' + source('V'),
], body_size=32, notes='About five minutes. Recall Week5/8: hermeneutic relation means reading a technologically mediated representation, not looking through a neutral window; conversational delivery could also invite alterity. Verbeek is conceptual grounding, not experimental proof of this interface. Candidate guardrails include source visibility, alternative accounts and a staffed correction route; do not promise operational response times or claim that a disclaimer removes bias. Teams adapt to their own product rather than copy the museum example. A one-page brief should connect relation, data, bias and guardrails to real consequences, including whose objection can trigger action.'))
S.append(cards('3-5 MINUTE VIDEO / SAME PROJECT ARGUMENT', 'Show a decision and its consequences.', [
    ('MOMENT OF USE', 'What does AI decide?', 'Show the visitor, AI choice and source. Label any mock-up.'),
    ('CONTEST + REPAIR', 'What can a person do?', 'Show contest and response. Do not stage an untested success.'),
    ('EXISTING CONTRACT', 'Three forms, one argument.', 'A0 poster + 3-5 minute video + one-page mediation brief. Group project: 40% of the course.'),
], text_size=29, notes='Final five minutes of 90-110. Explain the same argument across poster, video and brief rather than adding another deliverable. Existing project rubric is research/context30%, ethical/sociological impact30%, communication/poster20%, video10%, collaboration/process10% WITHIN the project, which is40% of the course. The syllabus already lists draft poster and mediation brief at Week11; confirm actual Canvas instructions, do not shift/cancel them. No same-night date, mandatory model training, four-group quota or new grade. If video not made yet, storyboard this moment in ordinary team notes.'))
S.append(activity('01 / EVIDENCE + CURATION AUDIT', 30, 'Find one claim and one choice.', [
    'Use your current notes, concept board or poster. Polish is not required.',
    '0-5: choose an important claim. 5-15: trace its source and narrow the inference.',
    '15-25: justify an included/rejected material. 25-30: make the ethical trade-off visible.',
], notes='110-140, exactly one thirty-minute activity across slides25-27. No ClassPoint collection, extra upload or new assessed component. Preserve the existing Week11 draft-poster/mediation milestone. Team may work on one paragraph or diagram. TAs ask who is affected and whether the actual source warrants the claim. If full text unavailable, document abstract-only and do not invent missing method. Use owned/licensed non-sensitive material; no personal camera-roll mining.'))
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
], notes='140-165, one twenty-five-minute block across slides28-30, not three activities. Exchange with another team; this is not the historical2025 obligation to give feedback to four groups. No new marks, mandatory public post or feedback submission. Work with accessible readable text/diagram; pair verbally if needed. Reviewers should not request private data or copyrighted full articles. Leave10 minutes for actual revision.'))
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

# Dividers use lecture airtime; protected project work and the break are unchanged.
_original = S
S = _original[:3]
S.append(section('01 / 15-45 / EVIDENCE', 'Read the claim.', 'A study is not a permission slip.', bg=INK, notes='One minute inside the existing thirty-minute evidence block. Teach the interview task and randomized writing comparison before interpreting findings. No pre-reading, extra activity or experiment is added. Keep the last five minutes for the existing citation audit.'))
S += _original[3:]
# Insert a similarity detail only after the Doshi task and bounded result.
index = next(i for i,s in enumerate(S) if s.title == 'Higher ratings can accompany convergence.') + 1
S.insert(index,paper_figure('D','Similar to what? Read the axis.','doshi-f4-story-similarity.png','Fig. 4A, top: x = embedding similarity (0-100); y = density, not people. Black: no AI; blue: one idea; red: five. Curves further right mean greater similarity.','Fig. 4A / top-panel crop / CC BY 4.0','Use two minutes within the existing evidence block. The authentic crop retains the top-panel axes and legend assembled below it at the same scale. Similarity compares each story with the average embedding of OTHER stories within its condition; it is not a count of cultural perspectives or a long-term skill measure. Density shows a distribution, not a participant count. Bottom AI-idea panel and coefficient panel are not taught here.'))
index = next(i for i,s in enumerate(S) if s.title == 'Selection changes\nwhat the world\ngets to see.')
S.insert(index,section('02 / 45-75 / CURATION + AUTHORSHIP','Choose. Credit. Answer.','Selection changes what others can see.',bg=INK,notes='One minute inside the original thirty-minute curation and authorship block. Preserve the fictional three-candidate comparison, documentation proposal, ownership experiment and U.S. legal distinction. These sources answer different kinds of questions. Keep all fifteen minutes of the break and all existing project work.'))
# The divider replaces the redundant selection statement, not the fictional comparison.
del S[index+1]
index = next(i for i,s in enumerate(S) if s.title == 'Make the inference visible.')
S.insert(index,section('03 / 90-110 / MAKE THE ARGUMENT VISIBLE','Design the relation.','One argument across poster, brief and video.',bg=INK,notes='One minute inside the existing twenty-minute worked-communication block. The preceding break remains intact. Verbeek is philosophical grounding, not an intervention trial. Keep one argument across the existing A0 poster, three-to-five-minute video and one-page brief; no new marks or submission.'))
# Place the conceptual explanation before its worked application.
v = paper_task('V', 'A tool also changes what we notice.', 'Verbeek argues that technology shapes human-world relations, not merely efficient interaction. Designers shape what people perceive and how they can act.', 'Embodiment, reading a representation, interaction, background: different relations, not experimental conditions.', 'Verbeek uses a metal detector: a beep represents metal we cannot directly see. Our fictional guide similarly presents an interpretation, not the exhibit itself.', 'This is a philosophical lens, not a participant experiment or a measured safeguard. It helps ask who gains authority; it cannot prove that our interface is fair.', 'Verbeek 2015, Beyond Interaction, author-hosted six-page copy. Targeted recheck of PDF3-5 / printed28-30: human-world relations and hermeneutic metal-detector example. Philosophical analysis, not participant research. The fictional guide is our application; a correction route has not been experimentally validated by this source. Use three minutes inside the twenty-minute communication block.', example_kind='SOURCE EXAMPLE + INSTRUCTOR APPLICATION', conceptual=True)
index = next(i for i,s in enumerate(S) if s.title == 'Make the inference visible.')
S.insert(index,v)
for chapter in S:
    if chapter.title in ('Read the claim.','Choose. Credit. Answer.','Design the relation.'):
        chapter.els[-1].y = 926
MAIN_SLIDE_COUNT = len(S)
S.append(content('OPTIONAL BIBLIOGRAPHY / NOT PRE-READING / NOT TIMED','Historical context, if useful.',['Yu et al. (2025): structured six-hat discussions and cognitive-presence networks in pre-service teachers.','[Open the historical primary paper](https://doi.org/10.1186/s41239-025-00545-x)','Bibliography only; not a new taught experiment or a universal learning claim.'],body_size=34,notes='Optional bibliography outside the 180-minute route, not assigned pre-reading or an additional taught study. The historical 2025 Week11 source used this six-hat paper. No new numeric, learning or causal claim relies on it. Read its actual methods before teaching it in a future revision; do not inherit exam dates or old logistics.'))

def position(heading):
    return next(i for i,s in enumerate(S,1) if s.title == heading)

SCHEDULE = [(0,15,'Recover the decision',(1,3)),
            (15,45,'Read the evidence',(4,position('Could another reader check your inference?'))),
            (45,75,'Curation and authorship',(position('Choose. Credit. Answer.'),position('Break.\n15 minutes.')-1)),
            (75,90,'Break',(position('Break.\n15 minutes.'),position('Break.\n15 minutes.'))),
            (90,110,'Research to communication',(position('Design the relation.'),position('Show a decision and its consequences.'))),
            (110,140,'Team evidence and curation audit',(position('Find one claim and one choice.'),position('Make the curation decision inspectable.'))),
            (140,165,'Peer reading and revision',(position('Let the argument travel without you.'),position('Revise the argument, not just the decoration.'))),
            (165,180,'Compare and prepare',(position('What became more defensible?'),position('Research. Choice. Responsibility.')))]
for sl in S:
    sl.notes = sl.notes.replace('32 slides plus one optional historical appendix',str(MAIN_SLIDE_COUNT)+' slides plus one optional bibliography')
    sl.notes = sl.notes.replace('slides25-27','the audit slides').replace('slides28-30','the peer-reading slides')

# Reassemble the timed route around a theory-first question, rather than
# presenting each paper as a successive lecture topic.
previous = {s.title: s for s in S}

def theory_slide(kicker, heading, rows, explanation):
    s = content(kicker, heading, [], title_size=64, bg=PAPER, notes=explanation)
    s.els = s.els[:2]
    for i, (tag, point, consequence) in enumerate(rows):
        y = 350 + i * 190
        s.els += [Rect(120, y, 1680, 2, '#A4B4B5'),
                  T(120, y + 27, 290, 45, tag, 'monomed', 25, '#246E70'),
                  T(425, y + 22, 575, 100, point, 'xbold', 37, INK, lh=1.08),
                  T(1040, y + 22, 760, 116, consequence, 'body', 29, INK, lh=1.24)]
    return s

def diagram_frame(kicker, heading, notes):
    s = content(kicker, heading, [], title_size=64, bg=PAPER, notes=notes)
    s.els = s.els[:2]
    return s


def diagram_node(s, x, y, w, h, label, heading, detail, name, fill='#FFFFFF'):
    s.els += [Rect(x, y, w, h, fill, name=name+'-panel'),
              T(x+27, y+27, w-54, 38, label, 'monomed', 22, '#246E70', name=name+'-label'),
              T(x+27, y+88, w-54, 120, heading, 'xbold', 38, INK, lh=1.08, name=name+'-title'),
              T(x+27, y+224, w-54, h-242, detail, 'body', 28, INK, lh=1.2, name=name+'-detail')]


def diagram_arrow(s, x, y, direction='→', name='flow'):
    s.els.append(T(x, y, 66, 80, direction, 'body', 54, '#246E70',
                   align='c', name=name+'-arrow'))

intro = title('SD2112 / WEEK 11',
    'Whose design?', 'From making outputs to making judgments.',
    notes='0-3 minutes. Open with a decision the class heard about in the Week 10 guest session, not an assumed prototype or test outcome. Ask: if an AI tool offered three descriptions, who decides which account visitors see? This week analyzes mediation, curation, authorship and responsibility before reading selected research and the Suno dispute. The guide throughout is fictional; no generated text is presented as observed evidence. No new assignment or pre-reading.')
guest = theory_slide('0-28 / THE QUESTION / FICTIONAL EXHIBITION GUIDE', 'Start with one decision.', [
    ('INPUT', 'Three possible accounts.', 'An exhibition guide could present an institutional account, a community account or an explicit gap.'),
    ('CHOICE', 'Which one appears first?', 'The team chooses what visitors can read, compare and question.'),
    ('COST', 'Who is left out?', 'The contributor, visitor or absent community may bear the consequence.')],
    '3-6 minutes. Connect to a decision from the guest lecture, without claiming guests tested the students\' work. The three accounts are original teaching possibilities, not screenshots, observations or actual machine outputs. Ask who can disagree and what evidence would change the choice. Do not turn this into a new submission. Optional 11 November supplement: Adobe announced beta creative agents and preview connectivity on 10 November 2026; this vendor announcement is not evidence of quality or a classroom test. If useful, substitute a three-minute paper-sketch example inside this opening; do not add time. https://news.adobe.com/news/2026/11/adobe-transforms-creative-cloud-tools')
mediation = diagram_frame('0-28 / MEDIATION / VERBEEK 2015', 'The tool frames what we notice.',
    '6-11 minutes. Reconnect Peter-Paul Verbeek, Beyond Interaction (2015), printed pp. 28-30, to the Week 5 and Week 8 discussion of mediation. His metal detector illustrates a hermeneutic relation: a beep mediates how a person reads unseen metal. Our guide similarly mediates interpretation, but the three-step layout is an instructor illustration, not Verbeek\'s measured model. Do not claim fluent text causes trust; ask what must be tested. Primary text: https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf')
for i, node in enumerate([
    ('01 / SOURCE', 'An account exists.', 'A named, dated account of the exhibit.'),
    ('02 / TOOL FRAMING', 'The guide summarises.', 'Selection and fluent wording can hide another account.'),
    ('03 / VISITOR', 'Interpret, then act.', 'Can a visitor compare sources or flag an error?')]):
    x = 120 + i * 580
    diagram_node(mediation, x, 360, 500, 440, *node, f'mediation-{i+1}')
    if i < 2:
        diagram_arrow(mediation, x+510, 528, name=f'mediation-{i+1}-to-{i+2}')
mediation.els.append(T(120, 837, 1680, 66, 'Mediation changes what can be noticed and done; it is not a direct view of the exhibit.',
                       'body', 31, INK, name='mediation-inference'))
mediation.els.append(T(120, 951, 1680, 40, source('V'), 'mono', 21, INK))
curation = diagram_frame('0-28 / CURATION / CHOICE HAS POWER', 'Selection makes a world visible.',
    '11-16 minutes. Selection is not a neutral final click: training sets, retrieval collections, reference boards and final displayed outputs allocate visibility in different technical ways. The fictional guide uses a retrieval/display decision, not model retraining. The criterion is inspectable provenance and a genuine alternative; it is a proposed design choice, not proven to achieve fairness.')
diagram_node(curation, 120, 380, 500, 410, 'INCLUDED / VISIBLE', 'Sourced account.',
             'Why this account? Name the source and selection criterion.', 'curation-include')
diagram_arrow(curation, 627, 520, name='curation-include-to-choice')
diagram_node(curation, 700, 380, 500, 410, 'EDITORIAL CHOICE', 'What appears first?',
             'A team selects the guide text; a polished summary is not neutral.', 'curation-choice', '#E2EDEB')
diagram_arrow(curation, 1207, 520, name='curation-choice-to-gap')
diagram_node(curation, 1280, 380, 500, 410, 'EXCLUDED / MISSING', 'Name the gap.',
             'Do not invent an absent voice. Invite correction by a contributor.', 'curation-gap')
curation.els.append(T(120, 832, 1680, 72, 'Representation is an editorial choice: visibility for one account can obscure another.',
                      'body', 31, INK, name='curation-tradeoff'))
agency = diagram_frame('0-28 / AGENCY + AUTHORSHIP / ORIGINAL CONTRIBUTION MAP', 'Trace four different decisions.',
    '16-21 minutes. Generation, selection, revision and authorization are different forms of action. A machine proposing a draft does not remove the upstream creator or the person who approves release. The diagram is an instructor contribution map, not a legal authorship determination. Use the fictional guide: the team chooses a sourced account and records why it rejected an unsourced fluent one.')
for i, node in enumerate([
    ('01 / GENERATE', 'Tool proposes.', 'Creators and sources precede the prompt.'),
    ('02 / SELECT', 'Designer chooses.', 'Reject the unsourced, fluent account.'),
    ('03 / REVISE', 'Designer edits.', 'Check provenance and change the claim.'),
    ('04 / AUTHORISE', 'Team releases.', 'Name who can answer an objection.')]):
    x = 120 + i * 430
    diagram_node(agency, x, 362, 380, 428, *node, f'agency-{i+1}')
    if i < 3:
        diagram_arrow(agency, x+382, 526, name=f'agency-{i+1}-to-{i+2}')
agency.els.append(T(120, 835, 1680, 70, 'An output has a contribution trail; the model is not the person who authorises display.',
                    'body', 31, INK, name='agency-trail'))
ownership = diagram_frame('0-28 / FOUR DISTINCT QUESTIONS', 'Feeling, work, permission, law.',
    '21-25 minutes. Four questions: felt ownership, actual credited contribution, permission to use another person\'s work, and copyright protection for human expression. The last two do not follow from how hard someone worked or how much they liked the output. US Copyright Office Part 2 (January 2025) addresses US copyrightability, not Hong Kong rights or licenses to train. Joshi and Vogel measure feelings in short prompting tasks; the study does not establish legal rights. Explain each without an automatic yes/no answer.')
for i, node in enumerate([
    ('01 / FEEL', 'Does it feel mine?', 'A reported feeling is not a copyright certificate.'),
    ('02 / CONTRIBUTE', 'Who did what?', 'Credit sources, selection, edits and review.'),
    ('03 / PERMISSION', 'May we reuse it?', 'Check rights and consent for the material.'),
    ('04 / PROTECTION', 'What is protected?', 'Human expression is a separate legal question.')]):
    x = 120 + (i % 2) * 855
    y = 350 + (i // 2) * 300
    label, heading, detail = node
    ownership.els += [Rect(x, y, 825, 270, '#FFFFFF', name=f'ownership-{i+1}-panel'),
        T(x+28, y+27, 765, 35, label, 'monomed', 23, '#246E70', name=f'ownership-{i+1}-label'),
        T(x+28, y+91, 765, 65, heading, 'xbold', 39, INK, name=f'ownership-{i+1}-title'),
        T(x+28, y+175, 765, 70, detail, 'body', 28, INK, name=f'ownership-{i+1}-detail')]
responsibility = diagram_frame('0-28 / RESPONSIBILITY / DISTRIBUTED DOES NOT MEAN LOST', 'Name who can answer.',
    '25-28 minutes. Accountability is a role plus an action, not a claim that a human was somewhere in the loop. Multiple contributors and a model do not erase the publishing team\'s responsibility to respond. The proposed correction route has not been validated with visitors or contributors. This is the transition from the conceptual spine to empirical and documentary evidence.')
for i, node in enumerate([
    ('BEFORE / TEAM', 'Check the source.', 'Verify provenance and permitted use.'),
    ('DURING / GUIDE', 'Show the limits.', 'Visitors can compare another account.'),
    ('AFTER / VISITOR', 'Raise an objection.', 'A contributor can contest a claim.')]):
    x = 120 + i * 580
    diagram_node(responsibility, x, 350, 500, 355, *node, f'responsibility-{i+1}')
    if i < 2:
        diagram_arrow(responsibility, x+510, 480, name=f'responsibility-{i+1}-to-{i+2}')
diagram_arrow(responsibility, 1500, 705, '↓', 'responsibility-objection-to-editor')
responsibility.els += [Rect(1080, 789, 700, 142, '#E2EDEB', name='responsibility-editor-panel'),
    T(1104, 802, 655, 45, 'ACCOUNTABLE ACTOR / EDITORIAL TEAM', 'monomed', 23, '#246E70', name='responsibility-editor-label'),
    T(1104, 856, 655, 68, 'Pause, correct or withdraw.', 'xbold', 36, INK, name='responsibility-editor-action'),
    Rect(196, 864, 876, 4, '#246E70', name='responsibility-feedback-line'),
    T(120, 834, 76, 74, '←', 'body', 54, '#246E70', name='responsibility-feedback-arrow'),
    T(225, 885, 820, 40, 'Return to source record and displayed account.', 'body', 27, INK, name='responsibility-feedback-label'),
    T(136, 709, 66, 80, '↑', 'body', 54, '#246E70', name='responsibility-return-arrow')]

def suno_case(kicker, heading, rows, notes, citation=None):
    s = theory_slide(kicker, heading, rows, notes)
    if citation:
        s.els.append(T(120, 951, 1680, 40, citation, 'mono', 20, INK, lh=1.1))
    return s

suno1 = diagram_frame('60-75 / SUNO / US COURT RECORD', 'A complaint is not a verdict.',
    '60-65 minutes. Primary case: UMG Recordings et al. v. Suno, No. 1:24-cv-11611, D. Mass.; original complaint, Document 1 filed June 24 2024, PDF pp. 1-3, 8-16. These are plaintiffs\' allegations, not findings. Suno\'s answer, Document 28 filed August 1 2024, located by docket-indexed primary filing but host PDF returned 403; fair-use position corroborated by Reuters on August 1 2024: https://www.reuters.com/legal/litigation/music-ai-startups-suno-udio-slam-record-label-lawsuits-court-filings-2024-08-01/ . Warner Music Group\'s November 25 2025 primary announcement says its litigation with Suno settled and new licensed models were planned. It does not establish that every Suno model or all historical training was licensed. First ask who supplied recordings, who decided to train, who could grant permission and who might receive credit. Do not treat a US lawsuit as Hong Kong law. Last directly read primary records: complaint and Warner release on November 12 2026; response identified but full filing not retrieved.')
for i, node in enumerate([
    ('PLAINTIFFS / JUN 2024', 'Complaint.', 'Universal, Sony + Warner allege unlicensed training copies.'),
    ('DEFENDANT / AUG 2024', 'Answer.', 'Suno disputes liability; argues US fair use.'),
    ('PARTY DEAL / NOV 2025', 'Settlement.', 'Warner + Suno announce a licensed-model partnership.')]):
    x = 120 + i * 580
    diagram_node(suno1, x, 350, 500, 430, *node, f'suno-timeline-{i+1}', '#FFFFFF' if i<2 else '#E2EDEB')
    if i < 2:
        diagram_arrow(suno1, x+510, 515, name=f'suno-timeline-{i+1}-to-{i+2}')
suno1.els += [T(120, 824, 1680, 70, 'An allegation, a defence and a settlement are different kinds of evidence.',
                  'body', 31, INK, name='suno-timeline-distinction'),
    T(120, 951, 1680, 40,
      '[2024 complaint](https://www.riaa.com/wp-content/uploads/2024/06/Suno-complaint-file-stamped20.pdf) / [2025 Warner statement](https://www.wmg.com/news/warner-music-group-and-suno-forge-groundbreaking-partnership)',
      'mono', 20, INK, lh=1.1)]
suno2 = suno_case('60-75 / SUNO / KEEP QUESTIONS APART', 'Four questions, not one ruling.', [
    ('TRAINING', 'What recordings were copied?', 'The complaint alleges unlicensed training copies; legality is contested.'),
    ('OUTPUT', 'Is a generated song protected?', 'Human contribution to a new song is a different copyrightability question.'),
    ('SIMILARITY + CREDIT', 'Does it resemble a track?', 'Specific resemblance, attribution and payment are separate factual and ethical questions.')],
    '65-70 minutes. The original complaint includes output-imitation examples as support for its training allegations; reproducing an example would not itself resolve copying, similarity, fair use or entitlement to credit. US Copyright Office Part 2 January 2025 analyzes protection of human expressive contributions case by case, separate from permission to use training recordings. Warner\'s settlement is an agreement between parties, not an adjudication of all these issues. Avoid an invented song, waveform, artist screenshot or categorical judgment. In Hong Kong or another market, seek current local advice for a real release.',
    '[Complaint / alleged examples](https://www.riaa.com/wp-content/uploads/2024/06/Suno-complaint-file-stamped20.pdf) / '+source('U'))
suno3 = diagram_frame('60-75 / CASE STATUS / VERIFIED BOUNDARY', 'Settlement is not universal clearance.',
    '70-75 minutes. Do not describe the Universal/Sony case as finally resolved or definitively pending as of today: no authoritative current docket access. A filing indexed as Case 1:26-cv-14275, Document 1 filed September 18 2026, could not be retrieved from this environment (403). Reuters June 5 2026 reported Universal\'s Suno case was ongoing then; that is the last corroborated status, not a live November status. Warner\'s own November 25 2025 release confirms its separate settlement. The 2026 filing is a lead for instructor verification before class, not a newly established court finding. Mark uncertainty explicitly. Ask what record of input source, permission, output selection and revision the fictional guide team would need; do not turn the dispute into legal advice.')
diagram_node(suno3, 120, 365, 800, 420, 'WARNER / VERIFIED 25 NOV 2025', 'Settled with Suno.',
             'Their release reports a licensing partnership; it covers their dispute, not every label.',
             'suno-warner', '#E2EDEB')
diagram_node(suno3, 980, 365, 800, 420, 'UNIVERSAL + SONY / STATUS BOUNDARY',
             'Latest status unverified.',
             'Reuters reported Universal ongoing on 5 June 2026; that is not a live status check. Sony was a plaintiff in 2024.',
             'suno-other-parties')
suno3.els += [T(120, 828, 1680, 76, 'Design question: who records sources, permission, selection and credit for a public work?',
                 'body', 31, INK, name='suno-design-trail'),
    T(120, 951, 1680, 40,
      '[Warner agreement](https://www.wmg.com/news/warner-music-group-and-suno-forge-groundbreaking-partnership) / [Reuters / June 2026](https://www.reuters.com/legal/litigation/musicians-union-sues-record-labels-over-ai-licensing-2026-06-05/)',
      'mono', 20, INK, lh=1.1)]

for heading in ('What did designers describe?', 'A participant view is not a legal rule.',
                'Write a story. Change the starting help.', 'Higher ratings can accompany convergence.',
                'Similar to what? Read the axis.', 'Control and variety are not the same goal.'):
    previous[heading].notes = '28-46 minutes / selected evidence after the theory spine. ' + previous[heading].notes
    previous[heading].notes = previous[heading].notes.replace('About four minutes within the Naqvi pair', 'About three minutes within the Naqvi pair').replace('About three minutes within the Naqvi pair', 'About two minutes for the Naqvi result') if heading == 'A participant view is not a legal rule.' else previous[heading].notes
    if heading == 'What did designers describe?':
        previous[heading].notes = previous[heading].notes.replace('About four minutes within the Naqvi pair', 'About three minutes for the Naqvi task')
    previous[heading].notes = previous[heading].notes.replace('Task and result share eight minutes', 'Task and result share seven minutes').replace('task and result share eight minutes', 'task and result share seven minutes')
    if heading == 'Control and variety are not the same goal.':
        previous[heading].notes = previous[heading].notes.replace('About five minutes', 'About four minutes')
for heading in ('What must a dataset explain?', 'Document the choice, including the unknowns.',
                'Would you type more to avoid friction?', 'More input can feel more yours.',
                'Which human expression is protected?', 'Separate protection, permission and credit.'):
    previous[heading].notes = '46-60 minutes / selected support and complication. ' + previous[heading].notes
    previous[heading].notes = previous[heading].notes.replace('The task and result share seven minutes', 'The task and result share five minutes').replace('The legal question and position share eight minutes, ending at 75', 'The legal question and position share four minutes, ending by 60').replace('question and application share four minutes', 'question and application share five minutes')
    previous[heading].notes = previous[heading].notes.replace('45-75 block', '46-60 block')
    previous[heading].notes = previous[heading].notes.replace(
        'No live lawsuit status, Thaler, Google Books analogy, Udio/Suno verdict or fair-use clearance is asserted.',
        'This Office report alone establishes no Suno verdict, training fair-use clearance or local legal status.')
guest.notes += " This guide is fictional throughout; no student's guest-session outcome is assumed."
suno3.notes += ' Exact present procedural status remains unverified on 12 November 2026.'
worked_choice = previous['Three candidates. One stated criterion.']
worked_choice.notes = '90-110 minutes / worked communication example after the break. ' + worked_choice.notes.replace('45-75 block, about five minutes.', 'About four minutes.')
previous['Make the inference visible.'].notes = previous['Make the inference visible.'].notes.replace('About six minutes of 90-110', 'About five minutes of 90-110')
S = [intro, guest, mediation, curation, agency, ownership, responsibility,
     previous['What did designers describe?'], previous['A participant view is not a legal rule.'],
     previous['Write a story. Change the starting help.'], previous['Higher ratings can accompany convergence.'],
     previous['Similar to what? Read the axis.'], previous['Control and variety are not the same goal.'],
     previous['What must a dataset explain?'], previous['Document the choice, including the unknowns.'],
     previous['Would you type more to avoid friction?'], previous['More input can feel more yours.'],
     previous['Which human expression is protected?'], previous['Separate protection, permission and credit.'],
     suno1, suno2, suno3, previous['Break.\n15 minutes.']]
S += [previous[x] for x in ('Design the relation.', 'Three candidates. One stated criterion.',
    'Make the inference visible.', 'Name the relation and the responsible actor.',
    'Show a decision and its consequences.', 'Find one claim and one choice.',
    'Narrow the claim until it fits.', 'Make the curation decision inspectable.',
    'Let the argument travel without you.', 'What did you understand - and miss?',
    'Revise the argument, not just the decoration.', 'What became more defensible?',
    'Research. Choice. Responsibility.')]
S[-1].notes += ' Week 12 follows this handover by examining delegated action, justified reliance, transparency and contestability with investigated Tesla incidents. Do not imply a verdict about those incidents in Week 11. Week 13 is quiz and posters, not another theory lecture.'
S[-1].els.append(T(120, 907, 1660, 46, 'WEEK 12 / When may we delegate a decision - and how can it be challenged?', 'monomed', 24, '#246E70'))
MAIN_SLIDE_COUNT = len(S)
S.append(previous['Historical context, if useful.'])
SCHEDULE = [(0,28,'Mediation, curation, agency and responsibility',(1,7)),
            (28,46,'Agency and collective diversity studies',(8,13)),
            (46,60,'Documentation, felt ownership and US copyrightability',(14,19)),
            (60,75,'Suno primary case and disputed status',(20,22)),
            (75,90,'Break',(23,23)), (90,110,'Research to communication',(24,28)),
            (110,140,'Team evidence and curation audit',(29,31)),
            (140,165,'Peer reading and revision',(32,34)),
            (165,180,'Compare and prepare',(35,36))]
attach_reports(S, Path(__file__).resolve().parent / 'week11-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 11',
            slides=finalize(S, footer(11)), pdf='SD2112-week11.pdf')
