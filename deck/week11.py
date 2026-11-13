"""Week 11: evidence, representation, credit, agency and responsibility."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import (title, content, statement, activity,
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
    label = {'N': 'WHAT DESIGNERS REPORTED', 'G': 'THE PROPOSAL',
             'U': 'THE OFFICE POSITION'}.get(key, 'MAIN FINDING')
    if asset:
        s.els.append(Image(120,348,1010,515,str(PAPER_ASSETS/asset),'contain',name='paper-image',url=REFS[key][1]))
        s.els.append(T(120,884,1010,64,caption,'mono',20,'#246E70',lh=1.2))
        s.els += [Rect(1164, 332, 636, 292, '#E2EDEB', name='finding-panel'),
                  Rect(1164, 332, 8, 292, '#ED6D24', name='finding-accent'),
                  T(1190, 354, 580, 34, label, 'monomed', 22, '#246E70', name='finding-label'),
                  T(1190, 404, 580, 198, finding, 'xbold', 34, INK, lh=1.12, name='finding-text')]
        for y, tag, value, name, height in [(660, 'LIMIT', limit, 'study-limit', 120),
                                           (830, 'FOR YOUR DESIGN', design, 'study-design', 76)]:
            s.els += [T(1190, y, 610, 30, tag, 'mono', 22, '#246E70', name=name+'-label'),
                      T(1190, y+42, 610, height, value, 'body', 28, INK, lh=1.15, name=name+'-body')]
    else:
        s.els += [Rect(120, 348, 1680, 250, '#E2EDEB', name='finding-panel'),
                  Rect(120, 348, 10, 250, '#ED6D24', name='finding-accent'),
                  T(156, 374, 1600, 36, label, 'monomed', 24, '#246E70', name='finding-label'),
                  T(156, 437, 1600, 132, finding, 'xbold', 42, INK, lh=1.15, name='finding-text')]
        paper_block(s,120,660,780,'LIMIT',limit,190,'study-limit')
        paper_block(s,1020,660,780,'FOR YOUR DESIGN / EXAMPLE',design,190,'study-example')
    s.els.append(T(120,956,1680,38,source(key),'mono',21,INK,lh=1.1))
    return s


def paper_figure(key, heading, asset, explanation, location, notes):
    s = paper_frame(key,heading,'READ THE FIGURE',notes)
    s.els += [Image(120,332,1680,540,str(PAPER_ASSETS/asset),'contain',name='paper-image',url=REFS[key][1]),
              T(120,884,1680,64,explanation,'body',27,INK,lh=1.15),
              T(120,956,1680,38,source(key)+' / '+location,'mono',21,INK,lh=1.1)]
    return s

S = []

S.append(paper_task('N', 'What did designers describe?', '28 U.S. participants discussed an AI image they had already made: 10 junior students, 10 senior students and 8 professionals. Interviews took 30-45 minutes in June-August 2024.', 'The researchers compared themes across experience groups. Nobody was assigned to use or avoid AI; no skill test was run.', 'A source-described artifact began as a kayaker photograph, was transformed with AI, then manually colour-edited. What work would the final image hide?', 'Interview transcripts were coded into themes about practice, values and ownership. These are reported experiences, not a score or a causal test of skill loss.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. Naqvi, He and Kaur, CHI 2025, author-hosted ACM-formatted full text, 16 pages. Methods PDF4-5: June-August 2024 Zoom interviews; artifacts were made before the study, not assigned experimental tasks. Recruitment through university groups, social media and snowball sampling; selection requires prior image-generation experience. Sections 4.4/4.5 report contrasting values, not a ranking of good and bad designers. Section 6, PDF13-14: self-selection, one-artifact elicitation, fast-changing tools, prompt-based tools and exclusively U.S. sample. Do not call this a longitudinal skill test because cohorts entered design at different times. About four minutes within the Naqvi pair. Source-adapted text example from Fig. 1(d), PDF9; image omitted because public-republication permission is not established. An interview artifact: AI-transformed kayak photograph, then manually colour-edited. The final image hides that process.', example_kind='SOURCE ADAPTATION / FIG. 1(d), PDF 9'))
S.append(paper_result('N', 'A participant view is not a legal rule.', 'Juniors described shared authorship; seniors linked ownership to input/editing; professionals discussed developer responsibility.', 'Self-selected U.S. accounts do not establish legal rights or caused skill loss.', 'Make contributions visible; test whether people can contest the choice.', 'About three minutes within the Naqvi pair. Open section 4.5 on PDF8; ask students to identify whose voice is speaking. The heading Ownership and Intellectual Property does not turn interviews into legal analysis. Junior shared-authorship, senior input/editing and professional developer-accountability themes are supported in sections 4.5.1-3, not universal opinions of all people at each career stage. Do not quote the derogatory lazy-designers remark from a different section as a finding of measured skill loss. Process-history interface is our candidate response, not an intervention evaluated in this paper. No participant artwork is reproduced in this public-review set. The source-adapted kayak workflow on the preceding slide illustrates why process history matters without treating an interview theme as a legal judgment.'))
S.append(paper_task('D', 'Write a story. Change the starting help.', '293 UK writers produced an eight-sentence story for young readers. Random assignment: no AI ideas, access to one, or up to five GPT-4 starting ideas.', 'Writers wrote their own story. 600 separate evaluators each rated six stories before learning about AI access.', 'One assigned topic was an adventure on the open seas. AI supplied a starting idea, not an iterative conversation or the finished eight sentences.', 'Readers rated novelty and audience/publishing usefulness from 1 (not at all) to 9 (extremely). Researchers also compared story embeddings: similarity from 0 to 100.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. Doshi and Hauser, Science Advances 10 eadn5290, 12 July 2024. Final primary article read through Europe PMC full-text XML after publisher PDF returned 403. Introduction/Fig1 and Methods: UK Prolific writers randomly assigned access, optionally request three-sentence GPT-4 ideas; writing remains human. 293 completed included stories, not all 500 recruited. Separate 600 evaluators initially rated without access information; later exploratory ownership questions are separate. Results Similarity of stories/Fig4: cosine similarity of each story embedding to the mean of OTHER stories within its condition, not a direct count of cultural perspectives. Randomized access supports bounded causal claims, not all use patterns. Authors note short task, nonprofessional sample and no interactive iteration. Supplement not independently retrieved. Task and result share eight minutes, followed by the two-minute similarity detail; avoid percentages without denominators. The following authentic Fig. 2A crop shows rating differences from human-only. The separate similarity detail retains the top Fig. 4A panel. Source adaptations are not invented observations.', example_kind='SOURCE ADAPTATION / METHODS'))
S.append(paper_result('D', 'Better ratings. More similar stories.', 'AI access raised average novelty and usefulness ratings. The two AI conditions also produced more similar stories.', 'A short writing task, not studio learning; similarity does not count cultural voices.', 'Inspect the portfolio, not only its best item.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. Doshi and Hauser, Science Advances 10 eadn5290, 12 July 2024. Final primary article read through Europe PMC full-text XML after publisher PDF returned 403. Introduction/Fig1 and Methods: UK Prolific writers randomly assigned access, optionally request three-sentence GPT-4 ideas; writing remains human. 293 completed included stories, not all 500 recruited. Separate 600 evaluators initially rated without access information; later exploratory ownership questions are separate. Results Similarity of stories/Fig4: cosine similarity of each story embedding to the mean of OTHER stories within its condition, not a direct count of cultural perspectives. Randomized access supports bounded causal claims, not all use patterns. Authors note short task, nonprofessional sample and no interactive iteration. Supplement not independently retrieved. Task and result share eight minutes, followed by the two-minute similarity detail; avoid percentages without denominators. The following authentic Fig. 2A crop shows rating differences from human-only. The separate similarity detail retains the top Fig. 4A panel. Source adaptations are not invented observations.', asset='doshi-f2-novelty-usefulness.png', caption='Doshi & Hauser (2024), Fig. 2A crop, CC BY 4.0. Dots: differences from human-only; bars: uncertainty.'))
S.append(paper_task('G', 'What must a dataset explain?', 'Gebru and colleagues propose documentation to help people judge a dataset before using it. They refined questions over roughly two years using examples and feedback.', 'They tried questions on face-image and movie-review datasets, then revised them using product-team, researcher and legal feedback.', 'A review dataset may suit sentiment research. Does that make it suitable for judging a person? Purpose, collection context and missing information matter.', 'This is a documentation proposal with a development process, not a randomized harm-reduction trial. The examples expose unanswered questions, not a safety score.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The question and application share four minutes. Gebru et al., author arXiv v8 (1 December 2021), sections 1.1-3: questions on motivation, composition, collection, processing, uses, distribution and maintenance. A documentation proposal developed through examples and feedback, not a randomized harm-reduction trial. Adapt a few questions; no mandatory full datasheet, fixed image count or personal camera-roll collection. The public availability of an image is not consent to expose the people in it. Do not project private source material. The source example informed the questions; its facsimile is omitted because public-republication permission is not established. Our guide application is an instructor illustration, not an evaluated datasheet.', conceptual=True))
S.append(paper_result('G', 'Document the choice, including the unknowns.', 'Record purpose, contents, collection, uses and maintenance. Explain why a set fits this use; label what is unknown.', 'Documentation supports scrutiny. It does not establish consent, fairness or harmlessness.', 'For our guide: museum facts are available; the fishing family has not been interviewed. Name who can fix errors.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The question and application share four minutes. Gebru et al., author arXiv v8 (1 December 2021), sections 1.1-3: questions on motivation, composition, collection, processing, uses, distribution and maintenance. A documentation proposal developed through examples and feedback, not a randomized harm-reduction trial. Adapt a few questions; no mandatory full datasheet, fixed image count or personal camera-roll collection. The public availability of an image is not consent to expose the people in it. Do not project private source material. The source example informed the questions; its facsimile is omitted because public-republication permission is not established. Our guide application is an instructor illustration, not an evaluated datasheet.'))
S.append(paper_task('J', 'Would you type more to avoid friction?', '29 analyzed participants wrote story prompts using three interfaces. A second experiment repeated the task with 30 new participants and added AI suggestions.', 'Normal submit versus hold-button or pump-slider for short prompts. Baseline first; time/motor order randomized.', 'An instructor example: expand a brief story idea, or keep it short and spend effort submitting it. This is not a prompt-length copyright test.', 'Prompt words were counted. Four self-reports about ownership, responsibility and connection were averaged on a 0-100 scale. A higher score means feeling more ownership.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The task and result share seven minutes. Joshi and Vogel, GI 2026, author preprint arXiv 2507.03670v3, July 12 2026, 11 pages; this is not the earlier 2025 version. Sections 4 and 6: first recruited 35, analyzed 29 after exclusions; second 30 new participants. Within-subject techniques time (press/hold) and motor (pump slider); psychological ownership is a four-item self-report composite. Section 6.2 contrasts suggestions versus none across experiments: extra words do not imply additional significant ownership. Sections 7/7.1: baseline-first and short-task/interface limits; effort correlations do not isolate a universal causal mechanism. Ask whose accessibility or urgency needs a friction interface may disadvantage. Do not infer that longer prompts earn copyright. Source image on result slide: Fig. 1(a) / PDF1 / author v3, motor-cost panel only; authentic pixel crop under CC BY 4.0, not our diagram or an outcome chart. Read the example: the progress bar must be green; write more words or move the slider up and down repeatedly. The pictured 113 reps is this interface example, not a universal requirement or study result. Panels (b) press-and-hold and (c) AI suggestions are omitted for legibility; comparisons remain on the task slide. The image and primary citation link to the full source figure. Added friction can also burden users.'))
S.append(paper_result('J', 'More input can feel more yours.', 'Time/motor: longer prompts, higher reported ownership. Suggestions added words, not a clear further ownership gain.', 'Baseline-first order and brief tasks limit inference. No legal rights were measured.', 'Test contribution AND accessibility costs.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The task and result share seven minutes. Joshi and Vogel, GI 2026, author preprint arXiv 2507.03670v3, July 12 2026, 11 pages; this is not the earlier 2025 version. Sections 4 and 6: first recruited 35, analyzed 29 after exclusions; second 30 new participants. Within-subject techniques time (press/hold) and motor (pump slider); psychological ownership is a four-item self-report composite. Section 6.2 contrasts suggestions versus none across experiments: extra words do not imply additional significant ownership. Sections 7/7.1: baseline-first and short-task/interface limits; effort correlations do not isolate a universal causal mechanism. Ask whose accessibility or urgency needs a friction interface may disadvantage. Do not infer that longer prompts earn copyright. Source image on result slide: Fig. 1(a) / PDF1 / author v3, motor-cost panel only; authentic pixel crop under CC BY 4.0, not our diagram or an outcome chart. Read the example: the progress bar must be green; write more words or move the slider up and down repeatedly. The pictured 113 reps is this interface example, not a universal requirement or study result. Panels (b) press-and-hold and (c) AI suggestions are omitted for legibility; comparisons remain on the task slide. The image and primary citation link to the full source figure. Added friction can also burden users.', asset='joshi-fig1a-motor.png', caption='Joshi & Vogel (2026), Fig. 1(a) crop / v3, PDF 1. CC BY 4.0. Motor-cost example; (b)/(c) omitted. Full figure: source link.'))
S.append(paper_task('U', 'Which human expression is protected?', 'The U.S. Copyright Office Part 2 report (January 2025) analyzes copyrightability using law, policy and responses to its public inquiry. It is not a participant experiment.', 'It compares assistance, prompts, human expression and creative editing. Third-party reuse permission is a separate question.', 'An instructor example: a designer arranges a poster and edits generated material. Ask separately what human expression is protectable and whether the inputs may be reused.', 'The basis is legal/policy analysis, not an ownership-feeling scale. Human contributions require case-by-case assessment. U.S. guidance, not Hong Kong legal advice.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The legal question and position share eight minutes, ending at 75. Official Part2 retrieved directly, Executive Summary printed iii and II.C-F printed11-27. Official AI index rechecked by web fetch on 21 October 2026: still links January2025 Part2; Part3 training labelled pre-publication. Node index returned403, alternate first-class web extraction succeeded; PDF direct200. Only bounded report positions are taught, not a claim of exhaustively current law worldwide. Distinguish copyrightability from third-party infringement/licence, privacy/consent, ethical credit and patents. No live lawsuit status, Thaler, Google Books analogy, Udio/Suno verdict or fair-use clearance is asserted. Hong Kong and any intended market need appropriate current local guidance before a real release. Unknown permission: hold or replace the material and seek qualified support. Source image: Executive Summary / PDF8 / iii / January 2025; reproduced crop, not our diagram. Actual Executive Summary excerpt: protectable human expression is distinct from purely generated material. Not an experiment.', conceptual=True))
S.append(paper_result('U', 'Separate protection, permission and credit.', 'Prompts alone: insufficient control with the tools analyzed. Human expression or creative editing may qualify case by case.', 'Not all generated parts are protected. No permission to copy others; not worldwide law.', 'Unknown reuse permission? Hold or replace the material; seek advice.', 'Teach this plain-English summary before discussion: no pre-reading is assumed. The legal question and position share eight minutes, ending at 75. Official Part2 retrieved directly, Executive Summary printed iii and II.C-F printed11-27. Official AI index rechecked by web fetch on 21 October 2026: still links January2025 Part2; Part3 training labelled pre-publication. Node index returned403, alternate first-class web extraction succeeded; PDF direct200. Only bounded report positions are taught, not a claim of exhaustively current law worldwide. Distinguish copyrightability from third-party infringement/licence, privacy/consent, ethical credit and patents. No live lawsuit status, Thaler, Google Books analogy, Udio/Suno verdict or fair-use clearance is asserted. Hong Kong and any intended market need appropriate current local guidance before a real release. Unknown permission: hold or replace the material and seek qualified support. Source image: Executive Summary / PDF8 / iii / January 2025; reproduced crop, not our diagram. Actual Executive Summary excerpt: protectable human expression is distinct from purely generated material. Not an experiment.', asset='copyright-summary-excerpt.png', caption='U.S. Copyright Office, Part 2 (Jan. 2025), Executive Summary, PDF 8 / iii. Federal text; not a figure.'))

STUDIES = {s.title: s for s in S}

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

mediation = diagram_frame('MEDIATION / VERBEEK 2015', 'The tool frames what we notice.',
    '6-11 minutes. Reconnect Peter-Paul Verbeek, Beyond Interaction (2015), printed pp. 28-30, to the Week 5 and Week 8 discussion of mediation. His metal detector illustrates a hermeneutic relation: a beep mediates how a person reads unseen metal. Our guide similarly mediates interpretation, but the three-step layout is an instructor illustration, not Verbeek\'s measured model. Do not claim fluent text causes trust; ask what must be tested. Primary text: https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf')
for i, node in enumerate([
    ('01 / SOURCE', 'The museum gives facts.', 'The label says when the fishing boat was built.'),
    ('02 / TOOL FRAMING', 'The guide summarises.', 'It tells the museum story, but leaves out the fishing family.'),
    ('03 / VISITOR', 'The visitor reads one story.', "They may learn when it was built, but miss what life on the boat was like.")]):
    x = 120 + i * 580
    diagram_node(mediation, x, 360, 500, 440, *node, f'mediation-{i+1}')
    if i < 2:
        diagram_arrow(mediation, x+510, 528, name=f'mediation-{i+1}-to-{i+2}')
mediation.els.append(T(120, 837, 1680, 66, 'The guide shapes how we understand the boat. It does not just pass on facts.',
                       'body', 31, INK, name='mediation-inference'))
mediation.els.append(T(120, 951, 1680, 40, source('V'), 'mono', 21, INK))
curation = diagram_frame('CURATION / CHOICE HAS POWER', 'Choosing one story leaves another out.',
    '11-16 minutes. Selection is not a neutral final click: training sets, retrieval collections, reference boards and final displayed outputs allocate visibility in different technical ways. The fictional guide uses a retrieval/display decision, not model retraining. The criterion is inspectable provenance and a genuine alternative; it is a proposed design choice, not proven to achieve fairness.')
diagram_node(curation, 120, 380, 500, 410, 'INCLUDED / VISIBLE', 'The museum story.',
             'Facts about the boat are easy to find. The team puts them first.', 'curation-include')
diagram_arrow(curation, 627, 520, name='curation-include-to-choice')
diagram_node(curation, 700, 380, 500, 410, 'EDITORIAL CHOICE', 'What appears first?',
             'The team decides which sources and stories the guide uses.', 'curation-choice', '#E2EDEB')
diagram_arrow(curation, 1207, 520, name='curation-choice-to-gap')
diagram_node(curation, 1280, 380, 500, 410, 'EXCLUDED / MISSING', 'The family story.',
             'If no one has asked the fishing family, say so. Do not invent their story.', 'curation-gap')
curation.els.append(T(120, 832, 1680, 72, 'Choosing what to show also means choosing what people will not see.',
                      'body', 31, INK, name='curation-tradeoff'))
agency = diagram_frame('AGENCY + AUTHORSHIP / ORIGINAL CONTRIBUTION MAP', 'Trace four different decisions.',
    '16-21 minutes. Generation, selection, revision and authorization are different forms of action. A machine proposing a draft does not remove the upstream creator or the person who approves release. The diagram is an instructor contribution map, not a legal authorship determination. Use the fictional guide: the team chooses a sourced account and records why it rejected an unsourced fluent one.')
for i, node in enumerate([
    ('01 / GENERATE', 'Tool proposes.', 'AI writes a draft from the source text.'),
    ('02 / SELECT', 'Designer chooses.', 'Choose a draft that names its source.'),
    ('03 / REVISE', 'Designer edits.', 'Check the facts and rewrite the text.'),
    ('04 / AUTHORISE', 'Team releases.', 'A person approves it for visitors.')]):
    x = 120 + i * 430
    diagram_node(agency, x, 362, 380, 428, *node, f'agency-{i+1}')
    if i < 3:
        diagram_arrow(agency, x+382, 526, name=f'agency-{i+1}-to-{i+2}')
agency.els.append(T(120, 835, 1680, 70, 'AI drafts. People choose, edit and publish. Keep a record of that work.',
                    'body', 31, INK, name='agency-trail'))
ownership = diagram_frame('FOUR DISTINCT QUESTIONS', 'Feeling, work, permission, law.',
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
responsibility = diagram_frame('RESPONSIBILITY / DISTRIBUTED DOES NOT MEAN LOST', 'Name who can answer.',
    '25-28 minutes. Accountability is a role plus an action, not a claim that a human was somewhere in the loop. Multiple contributors and a model do not erase the publishing team\'s responsibility to respond. The proposed correction route has not been validated with visitors or contributors. This is the transition from the conceptual spine to empirical and documentary evidence.')
for i, node in enumerate([
    ('BEFORE / TEAM', 'Check the source.', 'Check the facts and permission to use the text.'),
    ('DURING / GUIDE', 'Show the limits.', 'Say which story is missing.'),
    ('AFTER / VISITOR', 'Raise an objection.', 'A fishing family says the story is wrong.')]):
    x = 120 + i * 580
    diagram_node(responsibility, x, 350, 500, 355, *node, f'responsibility-{i+1}')
    if i < 2:
        diagram_arrow(responsibility, x+510, 480, name=f'responsibility-{i+1}-to-{i+2}')
diagram_arrow(responsibility, 1500, 705, '↓', 'responsibility-objection-to-editor')
responsibility.els += [Rect(1080, 789, 700, 142, '#E2EDEB', name='responsibility-editor-panel'),
    T(1104, 802, 655, 45, 'WHO ACTS? / MUSEUM EDITOR', 'monomed', 23, '#246E70', name='responsibility-editor-label'),
    T(1104, 856, 655, 68, 'Check, correct or remove it.', 'xbold', 36, INK, name='responsibility-editor-action'),
    Rect(196, 864, 876, 4, '#246E70', name='responsibility-feedback-line'),
    T(120, 834, 76, 74, '←', 'body', 54, '#246E70', name='responsibility-feedback-arrow'),
    T(225, 885, 820, 40, 'Update the source and the guide.', 'body', 27, INK, name='responsibility-feedback-label'),
    T(136, 709, 66, 80, '↑', 'body', 54, '#246E70', name='responsibility-return-arrow')]

def suno_case(kicker, heading, rows, notes, citation=None):
    s = theory_slide(kicker, heading, rows, notes)
    if citation:
        s.els.append(T(120, 951, 1680, 40, citation, 'mono', 20, INK, lh=1.1))
    return s

suno1 = diagram_frame('SUNO / US COURT RECORD', 'A complaint is not a verdict.',
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
suno2 = suno_case('SUNO / KEEP QUESTIONS APART', 'Four questions, not one ruling.', [
    ('TRAINING', 'What recordings were copied?', 'The complaint alleges unlicensed training copies; legality is contested.'),
    ('OUTPUT', 'Is a generated song protected?', 'Human contribution to a new song is a different copyrightability question.'),
    ('SIMILARITY + CREDIT', 'Does it resemble a track?', 'Specific resemblance, attribution and payment are separate factual and ethical questions.')],
    '65-70 minutes. The original complaint includes output-imitation examples as support for its training allegations; reproducing an example would not itself resolve copying, similarity, fair use or entitlement to credit. US Copyright Office Part 2 January 2025 analyzes protection of human expressive contributions case by case, separate from permission to use training recordings. Warner\'s settlement is an agreement between parties, not an adjudication of all these issues. Avoid an invented song, waveform, artist screenshot or categorical judgment. In Hong Kong or another market, seek current local advice for a real release.',
    '[Complaint / alleged examples](https://www.riaa.com/wp-content/uploads/2024/06/Suno-complaint-file-stamped20.pdf) / '+source('U'))
suno3 = diagram_frame('CASE STATUS / VERIFIED BOUNDARY', 'Settlement is not universal clearance.',
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


market = diagram_frame('NEWS / 12 NOVEMBER 2026 / US MARKET CLOSE', 'AI markets are unsettled.',
    'Reuters reporting by Caroline Valetkevitch and Marc Jones, syndicated by Euronext, dated 12 November 2026 23:37 (displayed timezone not specified), directly read 13 November. NVIDIA closed 4.3% lower, Nasdaq 0.39% lower, AMD 5.9% higher and Broadcom 5.5% higher. These are one-day changes, not live quotes or a long-run forecast. Reuters describes a volatile session alongside leadership uncertainty and rising Treasury yields; the numbers do not isolate a single cause. Do not call this uniform AI collapse or give investment advice. Ask what dependencies in a design project lie outside the team\'s control. https://live.euronext.com/en/financial-news/wall-street-ends-lower-nvidia-ceo-resigns-us-yields')
for i, (label, value, detail) in enumerate([
    ('NVIDIA', '-4.3%', 'Share price'), ('NASDAQ', '-0.39%', 'Stock index'),
    ('AMD', '+5.9%', 'Share price'), ('BROADCOM', '+5.5%', 'Share price')]):
    x = 120 + i * 430
    market.els += [Rect(x, 370, 390, 340, '#FFFFFF'),
                  T(x+25, 402, 340, 42, label, 'monomed', 26, '#246E70'),
                  T(x+25, 477, 340, 130, value, 'black', 78, INK, lh=1),
                  T(x+25, 636, 340, 45, detail, 'body', 28, INK)]
market.els += [T(120, 778, 1680, 90, 'One trading day. Different directions. Not proof that all AI businesses are collapsing.',
                'body', 36, INK, lh=1.15),
              T(120, 951, 1680, 40, '[Reuters via Euronext / 12 Nov 2026](https://live.euronext.com/en/financial-news/wall-street-ends-lower-nvidia-ceo-resigns-us-yields)', 'mono', 21, INK)]
leadership = diagram_frame('NEWS / NVIDIA ANNOUNCEMENT / 12 NOVEMBER 2026', 'Jensen Huang steps down.',
    'NVIDIA\'s official 12 November 2026 CEO-transition release, directly read 13 November, says Jensen Huang resigned as president, CEO and board member effective immediately. CFO Colette Kress becomes interim CEO and also remains CFO; the board is searching for a permanent successor. The release says resigned, not retired, and does not establish his future retirement plans. Teach the leadership transition without speculating about motive or repeating unrelated personal allegations. NVIDIA says customer commitments and the roadmap should continue; that assurance is a company statement, not an independently verified outcome. Bridge to design: a team controls its own choices but not all infrastructure or provider decisions. https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition')
for i, node in enumerate([
    ('WHAT CHANGED', 'Huang resigned.', 'He left the president, CEO and board roles, effective immediately.'),
    ('WHO LEADS NOW', 'Colette Kress.', 'The CFO becomes interim CEO while also remaining CFO.'),
    ('WHAT IS NEXT', 'A successor search.', 'The board will consider internal and external candidates.')]):
    x = 120 + i * 580
    diagram_node(leadership, x, 350, 500, 430, *node, f'news-leadership-{i+1}')
    if i < 2:
        diagram_arrow(leadership, x+510, 510, name=f'news-leadership-{i+1}')
leadership.els += [T(120, 824, 1680, 76, 'The announcement says resignation, not retirement. Future retirement plans are not confirmed.',
                    'body', 33, INK, lh=1.15),
                  T(120, 951, 1680, 40, '[NVIDIA / official CEO-transition announcement / 12 Nov 2026](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)', 'mono', 21, INK)]
NEWS = [market, leadership]

intro = title('SD2112 / WEEK 11', 'Whose design?',
    'Who chooses? Who gets credit? Who is responsible?',
    notes='Introduce the four questions through current news, then teach four named topics. Week 10 was the guest session: do not assume every group has a tested prototype. The fishing-boat guide is a fictional teaching example. Existing assessment requirements and Canvas milestones remain unchanged; Week 13 is quiz and posters.')
deep_question = statement('If AI makes the work,\nwhat makes it yours?',
    eyebrow_text='OPENING QUESTION / THINK, THEN DISCUSS', size=100, bg=PAPER,
    notes='Use five minutes immediately after the news: one minute thinking, two minutes in pairs, two minutes for a few views. Ask whether typing the prompt, choosing an output, changing it or accepting responsibility makes the difference. Do not settle it as a copyright question: keep control, contribution, feeling and law separate. No public collection or personal disclosure is required. Return to this question at the end.')

suno3.notes += ' Exact current procedural status remains unverified; no new docket check is claimed in this wording revision.'


def topic(number, heading, question):
    s = section(f'TOPIC {number} / 4', heading, question, bg=INK,
        notes=f'Topic {number} of four: {heading.replace(chr(10), " ")}. Explain the question in ordinary language before the example or paper. The section slide introduces this topic, not a separate activity. Students will choose just one of the four topics to apply to their group project later.')
    s.els[-1].y = 926
    return s

example = theory_slide('FICTIONAL EXAMPLE / AN AI MUSEUM GUIDE', 'Which story does the guide tell?', [
    ('MUSEUM', 'Facts about the boat.', 'An old fishing boat is on display. The museum label says when it was built.'),
    ('FISHING FAMILY', 'Life on the boat.', 'The family could explain what it was like to work on the boat.'),
    ('IF NO ONE HAS ASKED', 'Say what is missing.', 'The guide should say the family has not been interviewed. It must not invent their story.')],
    'Use this one concrete example throughout. An AI museum guide explains an old fishing boat. The museum can supply dates and technical facts; a fishing family could describe working life. If no family has been interviewed, that is missing information, not a third story to fabricate. These are fictional possibilities, not real quotations or AI outputs. Ask which story the guide should show first and why.')

ama = content('AFTER THE BREAK / 15 MINUTES', 'Group project: ask me anything.', [
    'What is unclear about your idea, evidence or use of AI?',
    'What is unclear about the poster, video or mediation brief?',
    'What is the one thing your group is stuck on?',
], body_size=40, notes='This slide must immediately follow the full fifteen-minute break. Spend fifteen minutes answering group-project questions. Invite questions verbally or in ordinary team notes; no new public collection. Clarify the current brief and Canvas instructions, not invented deadlines or criteria. Do not project private student data. Park individual troubleshooting for team work if needed, and protect the activity time.')

activity_intro = content('ONE GROUP ACTIVITY / USE YOUR OWN PROJECT', 'Choose one topic. Improve one thing.', [
    'Choose ONE: mediation, curation and power, agency and authorship, or responsibility.',
    'Look at ONE part of your project: a screen, an AI output, or a step in the experience.',
    'Use your topic to spot one problem. Sketch or rewrite one change.',
    'Be ready to explain: what is the problem, what will change, and why?',
], body_size=35, notes='Explain the activity before starting the work timer. Each group chooses one topic, not all four. Work with the project material the group already has: a concept sketch is enough. Students should make one concrete change or clearly labelled proposed change, not write an abstract ethical essay. One annotated sketch or a few sentences in existing project notes is enough; this is not a new submission or assessment.')

prompts = diagram_frame('CHOOSE ONE / THESE ARE FOUR OPTIONS', 'Use one question to guide your change.',
    'Read only the option the group chooses. Mediation concerns how the AI changes what a person notices or understands. Curation concerns what the team selects and leaves out. Agency/authorship concerns who decides and contributes. Responsibility concerns who responds when something goes wrong. More than one may apply, but choose one focus for this exercise. Do not require four analyses.')
for i, (name, question, hint) in enumerate([
    ('01 / MEDIATION', 'What does AI change for the user?', 'What might the person notice, believe or do differently?'),
    ('02 / CURATION AND POWER', 'What have you left out?', 'Which voices, sources or options are missing?'),
    ('03 / AGENCY AND AUTHORSHIP', 'Who makes the important choice?', 'Can a person change the AI output? Whose work gets credit?'),
    ('04 / RESPONSIBILITY', 'Who acts when it goes wrong?', 'How does a person report a problem? Who can fix it?')]):
    x = 120 + (i % 2) * 855; y = 350 + (i // 2) * 300
    prompts.els += [Rect(x, y, 825, 270, '#FFFFFF', name=f'prompt-{i+1}-panel'),
        T(x+28, y+24, 765, 35, name, 'monomed', 22, '#246E70'),
        T(x+28, y+88, 765, 90, question, 'xbold', 36, INK, lh=1.05),
        T(x+28, y+185, 765, 65, hint, 'body', 27, INK, lh=1.12)]

worked = theory_slide('WORKED EXAMPLE / CURATION AND POWER', 'One topic. One problem. One change.', [
    ('OUR PROJECT', 'An AI museum guide.', 'It explains the old fishing boat to visitors.'),
    ('THE PROBLEM', 'Only the museum story.', 'Visitors cannot hear from the people who worked on the boat.'),
    ('OUR CHANGE', 'Add the family story.', 'Ask a fishing family, get permission, and let visitors choose either story. Until then, label it missing.')],
    'Model the same task students will do. We choose curation and power, not all four topics. The problem is that the guide only has museum sources. The proposed change is to ask a fishing family for an account and permission, then provide a clear story choice. Until there is an actual interview and permission, label the missing story rather than simulate a family voice. This proposed interface has not been tested; ask how the team would find out whether it helps.')

work = activity('APPLY ONE TOPIC / GROUP PROJECT', 30, 'Make your change.', [
    '0-5 min: choose one topic and one part of your project.',
    '5-15 min: agree on one problem and who it affects.',
    '15-25 min: sketch or rewrite one change.',
    '25-30 min: prepare a 60-second explanation.',
], notes='Thirty minutes of actual group work. TAs ask which topic the group chose, where it appears in the project, who is affected and what they will change. If a prototype does not exist, annotate a concept sketch. Separate observed problems from assumptions; a proposed change is not a tested success. Keep work in existing project notes or drafts. No extra upload, new grading criterion or required paper search.')

share = activity('SAME ACTIVITY / CHECK YOUR IDEA WITH ANOTHER GROUP', 20, 'Explain it. Hear a question. Improve it.', [
    '0-5 min: each group explains its problem and change in 60 seconds.',
    '5-10 min: ask each other, "How would this change help the person using it?"',
    '10-20 min: improve your sketch or wording.',
], notes='This is the feedback stage of the same activity, not a second audit. Pair with one other group; do not impose a four-group quota. Each team gives a sixty-second explanation, then asks one clarifying question. Reserve the last ten minutes for revision. A team can reject advice with a reason. If pairing is impractical, use a TA or discuss within the group. Nothing new is collected or graded.')

shareback = content('SHARE BACK / 10 MINUTES', 'Show the change, not a checklist.', [
    '"We chose [topic]."',
    '"In our project, the problem is ..."',
    '"We changed ... because ..."',
    '"We still need to find out ..."',
], body_size=40, notes='Invite a few groups to show their actual sketch or wording. Allow one minute per explanation and a short question. Compare how the topic changed a concrete design decision, not which group named the most ethical concepts. Keep assumptions visible, avoid exposing private records and do not imply that a peer-approved sketch has been tested. If projection is unavailable, share verbally.')
closing = content('NEXT / YOUR EXISTING GROUP PROJECT', 'Keep the change. Keep the question.', [
    'Use the improvement in your A0 poster, 3-5 minute video or one-page mediation brief.',
    'Group project: 40% of the course. Follow current Canvas milestones.',
    'Week 12: when should we rely on AI, and who can challenge it?',
    'Week 13: quiz + posters.',
], body_size=36, notes='Use the last five minutes and finish by minute 180. Return to the opening question: if AI makes the work, what makes it yours? Students should now distinguish framing, selection, contribution and responsibility. Existing within-project weights remain research30, ethics30, poster20, video10 and process10; do not invent a quiz format, deadline or submission. The classroom sketch is not an extra deliverable.')

S = [intro, *NEWS, deep_question,
     topic(1, 'Mediation', 'How does AI shape what we understand?'), example, mediation,
     topic(2, 'Curation and power', 'Who chooses what we see?'), curation,
     STUDIES['Write a story. Change the starting help.'], STUDIES['Better ratings. More similar stories.'],
     STUDIES['What must a dataset explain?'], STUDIES['Document the choice, including the unknowns.'],
     topic(3, 'Agency and\nauthorship', 'Who decides? Who gets credit?'), agency, ownership,
     STUDIES['What did designers describe?'], STUDIES['A participant view is not a legal rule.'],
     STUDIES['Would you type more to avoid friction?'], STUDIES['More input can feel more yours.'],
     STUDIES['Which human expression is protected?'], STUDIES['Separate protection, permission and credit.'],
     topic(4, 'Responsibility', 'Who must respond when things go wrong?'), responsibility, suno1, suno2, suno3,
     statement('Break.\n15 minutes.', eyebrow_text='75-90 / RELATIVE CLASS TIME', size=120,
         notes='Protect the entire fifteen-minute break. Give the actual clock return time in class. On return, the very next slide is the fifteen-minute group-project AMA, then one simple topic-application activity. Do not fill the break with additional teaching or required project work.'),
     ama, activity_intro, prompts, worked, work, share, shareback, closing]
MAIN_SLIDE_COUNT = len(S)
S.append(paper_figure('D', 'Similar to what? Read the axis.', 'doshi-f4-story-similarity.png',
    'Fig. 4A, top: x = embedding similarity (0-100); y = density, not people. Black: no AI; blue: one idea; red: five. Further right = more similar stories.',
    'Fig. 4A / top-panel crop / CC BY 4.0',
    'Optional figure detail, outside the timed route. If useful, substitute it within the curation block rather than add time. Similarity compares a story with the mean embedding of OTHER stories in its condition, not a count of cultural perspectives or a measure of long-term skill. Density is not a participant count. The retained authentic top-panel crop includes axes and legend.'))
S.append(content('OPTIONAL REFERENCES / NOT PRE-READING', 'Sources behind today\'s questions.', [
    source('V'), source('N'), source('D'), source('G'), source('J'), source('U'),
], body_size=28, notes='Reference shelf outside the timed route. Links point to the versions recorded in the evidence ledger. No new reading assignment. Empirical findings, conceptual proposals and a US policy report answer different questions; none certifies a student design or supplies worldwide legal permission.'))

def position(heading):
    return next(i for i, s in enumerate(S, 1) if s.title == heading)

SCHEDULE = [
    (0,10,'Welcome and checked news',(1,position(deep_question.title)-1)),
    (10,15,'Opening discussion',(position(deep_question.title),position(deep_question.title))),
    (15,25,'Mediation',(position('Mediation'),position('Curation and power')-1)),
    (25,40,'Curation and power',(position('Curation and power'),position('Agency and\nauthorship')-1)),
    (40,62,'Agency and authorship',(position('Agency and\nauthorship'),position('Responsibility')-1)),
    (62,75,'Responsibility and Suno',(position('Responsibility'),position('Break.\n15 minutes.')-1)),
    (75,90,'Break',(position('Break.\n15 minutes.'),position('Break.\n15 minutes.'))),
    (90,105,'Group-project AMA',(position(ama.title),position(ama.title))),
    (105,115,'One activity: instructions and example',(position(activity_intro.title),position(worked.title))),
    (115,145,'Apply one topic to the project',(position(work.title),position(work.title))),
    (145,165,'Explain and improve the same change',(position(share.title),position(share.title))),
    (165,180,'Share back and next steps',(position(shareback.title),position(closing.title))),
]
# Retain source qualifications, replacing superseded timing text with the current block.
for s in S:
    for phrase in ('Teach this plain-English summary before discussion: no pre-reading is assumed. ',
                   'About four minutes within the Naqvi pair. ', 'About three minutes within the Naqvi pair. ',
                   'The question and application share four minutes. ', 'The task and result share seven minutes. ',
                   'The legal question and position share eight minutes, ending at 75. ',
                   'Task and result share eight minutes, followed by the two-minute similarity detail; avoid percentages without denominators. '):
        s.notes = s.notes.replace(phrase, '')
    for prefix in ('6-11 minutes. ', '11-16 minutes. ', '16-21 minutes. ', '21-25 minutes. ',
                   '25-28 minutes. ', '60-65 minutes. ', '65-70 minutes. ', '70-75 minutes. '):
        s.notes = s.notes.removeprefix(prefix)
    s.notes = s.notes.replace('This is the transition from the conceptual spine to empirical and documentary evidence.',
                            'Connect the correction example to responsibility in the Suno case.')
    s.notes = s.notes.replace('The following authentic Fig. 2A crop', 'The result slide\'s authentic Fig. 2A crop').replace(
        'The separate similarity detail retains', 'The optional similarity detail retains')
for start, end, label, (first, last) in SCHEDULE:
    for s in S[first-1:last]:
        s.notes = f'{start}-{end} minutes / {label}. ' + s.notes
attach_reports(S, Path(__file__).resolve().parent / 'week11-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 11',
            slides=finalize(S, footer(11)), pdf='SD2112-week11.pdf')
