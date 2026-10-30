"""Week 9: recommendation mechanisms -> bounded evidence -> project revision."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import (title, content, cards, statement, two_col, activity,
                             finalize, T, Rect, section, _slide, eyebrow)
from deckgen.core import Image
from course import footer
from week09_demo import ITEMS, rank

S = []
REFS = {
    'R1': ('Covington, Adams & Sargin / RecSys 2016', 'https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/'),
    'R2': ('Gauthier et al. / Nature 2026', 'https://doi.org/10.1038/s41586-026-10098-2'),
    'R3': ('Glickman & Sharot / online 2024, issue 2025', 'https://doi.org/10.1038/s41562-024-02077-2'),
    'R4': ('Buolamwini & Gebru / Gender Shades, 2018', 'https://proceedings.mlr.press/v81/buolamwini18a.html'),
    'R5': ('Gebru et al. / Datasheets, 2021 manuscript', 'https://arxiv.org/abs/1803.09010v8'),
}


def source(key):
    name, url = REFS[key]
    citation = f'[{key} / {name}]({url})'
    if key in ('R3', 'R4'):
        citation += ' · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)'
    return citation


def native_table(eyebrow, heading, headers, rows, widths, notes, bottom):
    """Native text and rectangles remain readable/editable in PowerPoint."""
    slide = content(eyebrow, heading, [], title_size=68, notes=notes)
    x0, y0, row_h = 120, 360, 88
    for row_num, row in enumerate([headers, *rows]):
        x = x0
        for value, width in zip(row, widths):
            fill = INK if row_num == 0 else ('#EAF2F2' if row_num % 2 else PAPER)
            slide.els += [Rect(x, y0 + row_num * row_h, width - 4, row_h - 4, fill),
                          T(x + 18, y0 + row_num * row_h + 12, width - 40, row_h - 24,
                            str(value), 'monomed' if row_num == 0 else 'body',
                            27 if row_num == 0 else 32, '#FFFFFF' if row_num == 0 else INK,
                            lh=1.15, valign='m')]
            x += width
    slide.els.append(T(120, 900, 1680, 75, bottom, 'body', 29, INK, lh=1.2))
    return slide


def pipeline():
    slide = content('10-35 / MECHANISM / ORIGINAL TEACHING SCHEMA',
                    'The feed is several decisions.', [], title_size=68,
        notes='About three minutes within 10-35 after the R1 summary and figure. Walk a fictional creative-event feed from the available pool to what is actually seen. Candidate selection retrieves a subset; ranking orders it against an objective; presentation determines visibility; interaction becomes possible feedback. A highly relevant item cannot rank if it was excluded upstream. R1 section 2 and Figure 2 support candidate-generation versus ranking as a historical architecture. The five-stage drawing is an instructor synthesis, not a diagram of current YouTube, TikTok or Spotify. Different systems may combine stages, insert business rules or use no learned model. Ask which stage belongs to Machine A, B or A+B; explicit eligibility rules can surround a learned ranker.')
    nodes = [('POOL', 'What exists?'), ('CANDIDATES', 'What is eligible?'),
             ('RANK', 'What comes first?'), ('PRESENT', 'What gets seen?'),
             ('FEEDBACK', 'What is recorded?')]
    for i, (label, prompt) in enumerate(nodes):
        x = 120 + i * 340
        slide.els += [Rect(x, 395, 310, 235, '#EAF2F2'),
                      T(x + 20, 425, 270, 48, label, 'monomed', 27, '#246E70'),
                      T(x + 20, 500, 270, 95, prompt, 'xbold', 36, INK, lh=1.1)]
        if i < 4:
            slide.els.append(T(x + 311, 473, 29, 50, '>', 'mono', 32, INK))
    slide.els += [T(120, 700, 1680, 100, 'Feedback can change later suggestions.\nPeople may change too; this is not inevitable.', 'body', 36, INK, lh=1.25),
                  T(120, 886, 1680, 65, source('R1'), 'body', 27, '#246E70')]
    return slide


from week09_studies import STUDY_GUIDES


def paper_frame(key, heading, phase, notes):
    """Week-owned grid aligned with the approved Week 8 paper explanations."""
    slide = _slide('#FFFFFF', notes, title=heading)
    slide.els += [eyebrow(120, 96, phase + ' / ' + key, '#246E70'),
                  T(120, 184, 1680, 140, heading, 'xbold', 72, INK,
                    lh=.95, spc=-.03, name='paper-title')]
    return slide


def paper_block(slide, x, y, width, label, value, height, name):
    slide.els += [T(x, y, width, 34, label, 'mono', 23, '#246E70', name=name+'-label'),
                  T(x, y+52, width, height, value, 'body', 34, INK,
                    lh=1.2, name=name+'-body')]


def paper_summary(key, heading, notes):
    # Replace the old abstract, rather than concatenate another summary slide.
    guide = STUDY_GUIDES[key]
    slide = paper_frame(key, heading, guide['kind'], notes +
        ' Targeted primary recheck 22 Oct 2026: ' + guide['source_locations'] +
        ' ' + guide['teaching_notes'] +
        ' This explanation replaces the old abstract within its existing allocation; no extra minutes.')
    for x, y, label, value, height, name in [
        (120,348,guide['task_label'],guide['task'],225,'study-task'),
        (120,676,guide['comparison_label'],guide['comparison'],180,'study-comparison'),
        (1020,348,guide['example_label'],guide['example'],225,'study-example'),
        (1020,676,guide['measurement_label'],guide['measured'],190,'study-measurement'),
    ]:
        paper_block(slide,x,y,780,label,value,height,name)
    slide.els.append(T(120,956,1680,38,source(key),'mono',21,INK,lh=1.1,name='paper-citation'))
    return slide


def paper_figure(key, heading, asset, label, explanation, notes):
    slide = paper_frame(key, heading, 'READ THE SOURCE / RESULT + LIMIT', notes)
    if key == 'R2':
        # Separate authentic conditions fill phone width instead of shrinking both plots.
        for x, asset, caption in [
            (120, 'gauthier-fig4-on.png', 'Switch ON / Figure 4 / assembled excerpt'),
            (990, 'gauthier-fig4-off.png', 'Switch OFF / Figure 4 / shared labels repeated'),
        ]:
            slide.els += [Image(x, 335, 810, 390,
                str(Path(__file__).parent / 'assets/week09' / asset), 'contain', name='paper-image'),
                T(x,730,810,38,caption,'mono',23,'#246E70',lh=1.1)]
        for i, line in enumerate(explanation):
            slide.els.append(T(120+i*575,780,530,155,line,'body',31,INK,lh=1.2))
        slide.els.append(T(120,956,1680,38,source(key),'mono',21,INK,lh=1.1,name='paper-citation'))
        return slide
    slide.els.append(Image(120, 335, 1080, 540,
                           str(Path(__file__).parent / 'assets/week09' / asset), 'contain',
                           name='paper-image', placeholder=label))
    for i, line in enumerate(explanation):
        slide.els.append(T(1260, 355 + i * 172, 540, 148, line, 'body', 31, INK, lh=1.2))
    slide.els += [T(120, 884, 1080, 64, label, 'mono', 20, '#246E70', lh=1.2),
                       T(120, 956, 1680, 38, source(key), 'mono', 21, INK, lh=1.1, name='paper-citation')]
    return slide


def paper_pair_results():
    slide = paper_frame('R3', 'Learning can go in either direction.',
                    'THE RESULT / NOT A RECOMMENDER EFFECT SIZE',
                    notes='Figure 2e,g, authentic separate crops from the published HTML full-size Figure 2; each preserves axes, values, error bars and panel letter. Left n=50 biased-algorithm follow-up; right a DIFFERENT n=50 accurate-algorithm follow-up. The vertical axes measure different outcomes: induced signed bias versus accuracy improvement (baseline error minus current error); do not compare their heights as one common scale. Horizontal axis is five interaction blocks within a task, not days or years. Error bars are standard errors of the mean, not individual ranges. Charts concern independent estimates before the current advice; no field-feed, lasting effect or mitigation established. Use about two minutes within 60-75, then compare study contexts. Primary URL https://www.nature.com/articles/s41562-024-02077-2/figures/2 .')
    for x, asset, caption in [(120, 'glickman-fig2e.png', 'e / Biased advice: bias grew.\nBias minus baseline (percentage points); n=50.'),
                               (990, 'glickman-fig2g.png', 'g / Accurate advice: estimates improved.\nBaseline error minus current error; n=50.')]:
        slide.els.append(Image(x, 345, 810, 460, str(Path(__file__).parent / 'assets/week09' / asset), 'contain', name='paper-image'))
        slide.els.append(T(x, 812, 810, 85, caption, 'body', 29, INK, lh=1.2))
    slide.els += [T(120, 910, 1680, 38, 'Figure 2e,g / separate n=50 groups; bars = standard errors; x = five task blocks.', 'mono', 21, '#246E70'),
                       T(120, 956, 1680, 38, source('R3'), 'mono', 21, INK, lh=1.1, name='paper-citation')]
    return slide


# 0-10: reconnect, without recollecting Week 7 or Week 8 work.
S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 09',
    'Inside the feed.', 'Recommendations. Bias. The decisions that shape the next choice.',
    notes='Three-hour draft class: research -> AI-product analysis -> existing team project. Main route is slides 1-28; slides 29-31 are a reference shelf, not additional lecture time. Relative minutes: 0-10 opening; 10-35 mechanism; 35-60 objectives/bias; 60-75 research; 75-90 break; 90-105 controlled ranking demo; 105-135 research/evidence audit; 135-165 redesign and test; 165-180 comparison. Preserve all protected blocks. No date, submission, mark or deadline is announced. The syllabus still lists Week 9 concept board/bias register and Week 10 recommendation systems: this draft follows the intended revised sequence but does not amend the syllabus. Instructor must reconcile Canvas and timetable before teaching.'))
S.append(content('0-10 / CONTINUE YOUR EXISTING PROJECT', 'What did your product promise?', [
    'Keep your concept and Week 8 research.',
    'What did the person expect?',
    'Locate one selection, ranking or suggestion.',
    'A sketch is enough. No feed required.',
], body_size=36, notes='About four minutes within the opening. Recall Week 8 humanizing AI and mediation: an apparently friendly adviser or invisible background system shapes what a person can notice and choose. Reuse the existing evidence, not a new team pitch or mandatory prototype. Ask for one concrete moment of use. Products can rank design alternatives, route requests or suggest actions without a scrolling feed. Teams open their own work privately; no projection of personal records and no new upload.'))
S.append(statement('Selected for you.\nBy whose objective?',
    eyebrow_text='DISCUSS / USER GOAL / SYSTEM PROXY / PERSON LEFT OUT', size=104, bg=PAPER,
    notes='Remaining opening minutes: pairs name a user goal, the system action and a possible proxy. Example: find a suitable workshop versus maximize click probability. These are instructor-authored examples, not claims about a named service. Return to this distinction after mechanisms. A recommendation is part of the product, not just an algorithm hidden behind a neutral screen.'))

# 10-35: mechanism before moral judgement.
S.append(pipeline())
S.append(two_col('CONTENT-BASED FILTERING / ILLUSTRATIVE', 'Similar to what you liked.', [
    'Describe items by features: genre, pace, mood.',
    'Compare features with previously liked items.',
    'Similar genre is not the right film for every night.',
], ['EXAMPLE', 'Liked: a quiet science-fiction film.',
    'Candidate: another film with those features.',
    'Still unknown: mood, availability, accessibility and why the person liked it.'],
    right_font='body', left_size=34, right_size=32,
    notes='About three minutes within 10-35. Teach the principle, not a claim that every recommender uses hand-labelled genres. Features can be explicit metadata or learned vectors; hybrid systems combine signals. Distinguish the item-feature relation from collaborative filtering on slide 10. Do not infer a permanent identity from one click. The example is synthetic and simplified. Historical PDF/PPTX slide 31 makes this distinction; retain it with clearer limits.'))
S.append(two_col('EMBEDDINGS / NUMBERS, NOT AN ESSENCE', 'Near depends on the representation.', [
    'An embedding is a vector of numbers.',
    'Model + training data + metric define what is near.',
    'Near does not mean true, fair or suitable.',
], ['HAND-SET UNIT VECTORS / NOT LEARNED',
    'Query Q = [1, 0]', 'Item A = [0.8, 0.6]; cosine(Q,A) = 0.8',
    'Item B = [0, 1]; cosine(Q,B) = 0',
    'A is nearer by cosine here. Change the representation: the relation can change.'],
    right_font='body', left_size=34, right_size=30,
    notes='About three minutes within 10-35. Recall CLIP/latent representations in Week 5. In the tiny hand-set example all vectors have length one, so their dot product equals cosine similarity; higher cosine means more similar, not smaller distance in every metric. Do not call these two hand-set coordinates an actual trained embedding or a map of personality. R1 section 3.1 defines learned user/video vectors, supporting the representation concept but not this synthetic arithmetic. Historical slide 27 visually relates query/document vectors to a similarity metric; this revision makes the metric and toy status explicit.'))
S.append(native_table('COLLABORATIVE FILTERING / MADE-UP INTERACTIONS',
    'Learn from a pattern of choices.', ['PERSON', 'FILM A', 'FILM B', 'FILM C'],
    [('You', 'A: liked', 'B: liked', 'C: ?'), ('Person P', 'A: liked', 'B: liked', 'C: liked'),
     ('Person Q', 'A: ?', 'B: disliked', 'C: liked')], [600, 360, 360, 360],
    'About three minutes within 10-35. A nearest-neighbour intuition: another person with overlapping preferences liked C, so C is a candidate for you. This table is not enough to guarantee preference or to fit a production model. Question marks mean unobserved, not negative. Collaborative filtering can instead learn latent factors; it need not explicitly find a human look-alike. R1 section 2 describes collaborative candidate generation using coarse behaviour/history; this is an original pedagogical simplification, not its algorithm or real user data.',
    '? means unobserved, not disliked. A shared history suggests a candidate, not certainty.'))
S.append(cards('COLD START / SPARSE DATA', 'What can the system honestly infer?', [
    ('NEW PERSON', 'No history yet.', 'Ask an optional preference, offer a useful default, or let the person browse.'),
    ('NEW ITEM', 'Few interactions.', 'Use item information or explore. Popularity alone can leave new items unseen.'),
    ('MISSING SIGNAL', 'No click is ambiguous.', 'Was it irrelevant, inaccessible, unseen, or simply not needed today?'),
], text_size=31, notes='About three minutes within 10-35. Cold start is limited evidence about a new person/item; sparse data also affects established users. The interventions are candidate design choices, not universally effective remedies. R1 introduction and section 3 discuss freshness, sparse implicit feedback and modelling uncertainty around satisfaction. Separate absence of interaction from dislike and from absence of demand. Ask which fields the proposed product truly needs to collect rather than demanding more data by default.'))
S.append(content('SPOKEN REFLECTION / NO COLLECTION', 'A reason is not the whole mechanism.', [
    '"Because you liked Film A."',
    'Does this explain selection, order or visibility?',
    'Which hidden choice matters?',
    'What evidence makes the explanation faithful?',
], body_size=36, notes='Final four minutes of the mechanism block. Brief pair exchange; take two spoken answers. This is not an attention-check quiz or ClassPoint submission. A plausible natural-language explanation need not be faithful to the actual ranker. Candidate generation, ranking rules and display can all contribute. Request a product decision, evidence and interpretation rather than a vocabulary definition. Transition: even a faithful explanation does not tell us whether the objective is worthwhile.'))

# 35-60: explicit objectives, missing people, labour and data boundaries.
S.append(cards('35-60 / VALUE VERSUS PROXY', 'A click is not the user goal.', [
    ('GOAL', 'Find a useful event.', 'Does this help the person do what they came to do?'),
    ('PROXY', 'Predict a click.', 'Easy to log, but an accidental click or a misleading title can score well.'),
    ('CHECK', 'Look beyond the click.', 'Ask about task success, unwanted exposure and who is poorly served.'),
], text_size=32, notes='About two minutes within 35-60. Fictional event product, not a measured outcome. R1 introduction calls implicit feedback noisy and section 4 contrasts click/watch-time objectives; do not present its 2016 watch-time objective as current YouTube policy. A proxy is not necessarily useless or malicious. It is incomplete relative to the human goal and may create incentives. Teams should state one goal and one candidate measure without assuming the measure proves welfare.'))
S.append(two_col('FEEDBACK / A PRODUCT CAN TEACH A PREFERENCE', 'The next screen changes the next data.', [
    'Exposure -> choice -> recorded signal -> next suggestion.',
    'People may learn, adapt or follow someone new.',
    'The interface helps create its next data.',
], ['ORIGINAL CONCEPTUAL LOOP', 'choice -> recorded signal -> next suggestion -> changed choice',
    'NOT A MEASURED UNIVERSAL LAW', 'The size, direction and persistence of any effect require evidence.'],
    right_font='body', left_size=34, right_size=31,
    notes='About two minutes within 35-60. Draw the return arrow verbally: suggestions shape available actions, not just mirror an independent preference. The loop is conceptual, not a claim that every iteration increases bias or polarization. R2 tests a field intervention; R3 tests controlled judgement learning. Their different evidence will prevent treating this diagram as an empirical effect size. Even unchanged preferences can produce different clicks if visibility changes; a behavioural change does not by itself prove changed beliefs.'))
S.append(content('EXPLORATION / EXPOSURE', 'Diversity is a decision to specify.', [
    'Different topic, creator, viewpoint or format?',
    'Exploration can expose previously unseen options.',
    'A slider is not proof of reduced polarization.',
    'Test exposure, usable control and the user goal.',
], body_size=36, notes='About two minutes within 35-60. Retain the historical 2025 slide 49 slider/explore-button idea as a design hypothesis, not a proven remedy. Diversity is not one scalar moral property: a topic-diverse list can still omit a community, show unsafe content or overwhelm a person. R1 introduction discusses exploration/exploitation for freshness, not a fairness guarantee. Ask whether exploration should be optional, explained or constrained; do not prescribe a universal setting.'))
S.append(cards('BIAS / LOCATE A DECISION, NOT JUST A BAD OUTPUT', 'Where can a pattern become a problem?', [
    ('COLLECTION + LABELS', 'Who is represented?', 'Who is missing? Who decides what counts as relevant, safe or successful?'),
    ('OBJECTIVE + RULES', 'Who gains visibility?', 'What gets rewarded, filtered out or treated as an acceptable error?'),
    ('INTERACTION', 'Who gets reinforced?', 'Whose past exposure becomes evidence for what should be shown next?'),
], text_size=31, notes='About two minutes within 35-60. Four entry points grouped into three visual cards: collection, labels, objectives and interaction. These are useful analysis handles, not an exhaustive or mutually exclusive taxonomy. Historical slide 43 gives four bias types; avoid implying only malicious design produces unequal effects. Gender Shades (R4, Table 4) found intersectional error disparities in three historical commercial binary gender classifiers: it is not a face-identification/recommender experiment, a definition of anyone\'s gender or a current vendor audit. Its transferable lesson is to inspect relevant groups and errors rather than an overall average alone. R5 sections 3.2-3.5 offer documentation questions; documentation does not establish fairness. Link and fuller audit context are in the reference shelf.'))
S.append(content('PRIVACY / A DATA BOUNDARY IS A DESIGN CHOICE', 'Useful does not mean necessary.', [
    'Collect. Infer. Retain. Share. Different decisions.',
    'Which field or inference can you avoid?',
    'What changes after correction, refusal or deletion?',
    'Removing names does not establish anonymity.',
], body_size=35, notes='About three minutes, with remaining 35-60 time for questions. R5 composition/collection/maintenance questions cover identifiability, consent and retention. This is design analysis, not jurisdiction-specific legal advice, a promise that deletion is technically immediate or an empirical re-identification rate. Optional Netflix de-anonymization paper remains background only; no attack procedure or number is asserted without reading its assumptions. Ask about downstream copies/inferences as well as source records. Teams must use synthetic examples, not collect classmates\' histories or put user records in tools/prompts.'))

# 60-75: standalone summaries precede the actual paper figures.
S.append(paper_summary('R2', 'Can changing a feed change people?',  'About two minutes for this summary, then three for the actual figure, within 60-75. Published open-access Nature article retrieved 21 Oct 2026: online 18 Feb 2026, volume 652 pp. 416-423. Read Design, Impact, Discussion and Methods including figure captions. 6,043 completed baseline, 4,965 completed post-survey (main sample), 2,387 shared follow data. July-September 2023, average 7 weeks + 1 day. Random assignment within initial feed groups permits intention-to-treat comparisons, not a randomized lifetime exposure history. Activation versus staying chronological shifted conservative policy-priority/current-event indices and conservative activist following; removal in initially algorithmic users did not produce comparable reversals. Authors support a following/exposure mechanism but acknowledge unobserved differences between initial-feed groups may contribute to asymmetry. Do not say the whole mechanism was independently randomized or that all algorithms radicalize. Most compliance self-report, 599 post-survey extension users, no transfer to current X or Hong Kong users established. Supplementary PDF/replication not independently reviewed or reproduced. Reset design is our hypothesis, not a validated remedy.'))
S.append(paper_figure('R2', 'Following is not just a feed setting.', 'gauthier-fig4.png',
    'Figure 4 / condition excerpts / axes + legend / 2026', [
    'Switch ON / OFF = algorithm activated / removed. Blue = basic analysis; orange = adjusted for prior characteristics.',
    'X = change in standard deviations, not percent. Bars = 90/95% CIs; crossing zero leaves no-change plausible.',
    'Conservative activist following rose. Survey: no clear polarization change. A reset remains untested.',
], 'Figure 4, publisher full-size image, https://www.nature.com/articles/s41586-026-10098-2/figures/4. Two assembled condition excerpts: authentic top political-leaning/activist rows and their corresponding original x-axes; unchanged full shared legend proportionally resized below each. Right excerpt repeats original shared row labels. White gutters identify assembly; no data redrawn. Earlier three faithful crops retained in assets as historical provenance. Omitted news/entertainment/official rows are not implied absent; full figure linked. n=2,387 consenting follow-data participants, not all 4,965 survey completers. Units are standardized intention-to-treat effects; blue unconditional and orange covariate-adjusted estimates; bars 90%/95% confidence intervals. Follow the conservative activist row, not every coefficient. Random assignment is within initial feed settings; prior lifetime exposure was not randomized. No significant partisanship/affective-polarization effect in Figure 2. Product reset remains a hypothesis, not a tested remedy. Use about three minutes after the two-minute summary, within 60-75.'))
S.append(paper_summary('R3', 'Can advice change your next judgement?',  "About two minutes for this summary, then one procedure and two results minutes, within 60-75. Published online 18 Dec 2024, NHB 9, 345-359 (2025). Publisher full HTML retrieved; Results, Discussion and Methods reviewed. Overall n=1,401 includes supplementary experiments, not a single feed sample. Focus on experiment 2: 120 Prolific participants estimated moving-dot direction, first alone then with accurate, rightward-biased or noisy hard-coded algorithms in counterbalanced order. Algorithm output was revealed after participants' own estimate/weighting. Later independent estimates shifted in the biased condition; accurate advice improved accuracy. Follow-up n=50 per biased/accurate condition examined repeated interaction. This is not merely copying the current displayed answer. It is also not a news-ranking experiment or proof of lasting everyday preference change. Experiment 1 uses a CNN/emotion task; experiment 3 uses Stable Diffusion 2.1 image exposure (not a current model benchmark). The narrative has a reversed-label sentence in Results under input/perception; Fig. 1 caption and Methods distinguish the conditions correctly. No numerical label-effect claim used here. Supplement PDF/computational fits not independently checked or reproduced."))
S.append(paper_figure('R3', 'Estimate first. See the advice later.', 'glickman-fig2abc.png',
    'Figure 2a-c / published HTML / online 2024', [
    'a: estimate moving dots alone. b: three different advice patterns.',
    'c: estimate and choose a weight BEFORE seeing the current advice.',
    'A later independent estimate can reveal learning, rather than copying this answer.',
], 'Authentic contiguous crop of Figure 2 panels a-c, not a recreated experiment. https://www.nature.com/articles/s41562-024-02077-2/figures/2 . Published main HTML consulted in full including Methods. Main experiment n=120 Prolific participants; 30 baseline trials then counterbalanced accurate, rightward-biased and noisy hard-coded algorithms, 30 trials each. The distributions in b are the paper schematic algorithm response patterns, not a new empirical plot. Use one minute to explain the procedure; no in-class experiment is being run.'))
S.append(paper_pair_results())
S.append(native_table('COMPARE EVIDENCE / NOT "ALL FEEDS POLARIZE"',
    'Different studies answer different questions.', ['STUDY', 'SYSTEM / TIME', 'WHAT TO CARRY FORWARD'],
    [('R2 / field', 'X / 7 weeks', 'Mode and following can differ.'),
     ('R3 / controlled', 'Task algorithms / sessions', 'Later judgement can change.'),
     ('Your product', 'New context / unknown', 'Treat the transfer as a hypothesis.')],
    [360, 590, 730],
    'Remaining evidence-block minutes before break. Ask teams to name population, system, comparator, outcome and time before asserting a filter bubble or an echo chamber. These terms overlap in ordinary use but do not name one measured outcome. R2 found no significant affective-polarization/partisanship effect despite other changes; R3 establishes controlled learning mechanisms, not field effect sizes. A null is not proof of universal absence, and a positive result is not universal presence. R2\'s main article discusses contrasting prior Meta results; that citation is background, not independently re-reviewed here. Do not claim a fresh systematic review or consensus. Use one methods/results excerpt in discussion, not two new compulsory full papers.',
    'Ask: platform / population / comparator / outcome / time. Keep the mismatch visible.'))
S.append(statement('Break.\n15 minutes.', eyebrow_text='75-90 / PROTECTED BREAK / RELATIVE CLASS TIME', size=120,
    notes='Preserve the full fifteen-minute break. Announce the actual return clock time in class once the timetable is confirmed. Next is one fifteen-minute controlled demo, then thirty minutes research and thirty minutes redesign/test. Open slides 31-32; the full fallback is native and needs no login, network or learned model.'))

# 90-105: reproducible arithmetic, with the whole fallback already on screen.
S.append(native_table('90-105 / CONTROLLED DEMO / ALL VALUES INVENTED',
    'Same four items. Two scoring rules.', ['ITEM', 'RELEVANCE', 'NOVELTY'],
    [(f'{key} / {label}', f'Relevance: {rel}', f'Novelty: {nov}') for key, label, rel, nov in ITEMS], [840, 420, 420],
    'First seven minutes of one fifteen-minute demo. Scores 0-10 are invented by the instructor for a fictional creative-workshop feed: relevance means fit to a prior interest; novelty means difference from that prior interest. Neither is estimated from people. Same four candidates, no filtering, personalization training, click simulation, accounts or network. Ask for a prediction: which two items enter the top two under each rule? Rule A = 0.8 relevance + 0.2 novelty; rule B = 0.3 relevance + 0.7 novelty. Compute A by hand: 0.8*9+0.2*1=7.4 under rule A; 0.3*9+0.7*1=3.4 under rule B. Optional local terminal: .venv/bin/python deck/week09_demo.py. All values, formulas and results are already native on these slides; if terminal/code fails, continue on paper without changing the activity budget. Do not present this weighted rule as a learned recommender or as study data.',
    'A = 0.8 relevance + 0.2 novelty.   B = 0.3 relevance + 0.7 novelty.'))
S.append(two_col('SAME 15-MINUTE DEMO / STATIC RESULTS = CODE RESULTS',
    'The objective changes the shortlist.',
    ['RULE A / RELEVANCE WEIGHT 0.8'] + [f'{i}. {key} / {label} / {score:.1f}' for i, (key, label, score) in enumerate(rank('0.8'), 1)] + ['Top two: A + B'],
    ['RULE B / RELEVANCE WEIGHT 0.3'] + [f'{i}. {key} / {label} / {score:.1f}' for i, (key, label, score) in enumerate(rank('0.3'), 1)] + ['Top two: D + C'],
    right_font='body', left_size=31, right_size=31,
    notes='Remaining eight minutes of the same fifteen-minute block. Both lists are generated from week09_demo.py at import, not transcribed separately. Decimal arithmetic, deterministic ID tie-break and input validation make the local script reliable. Rule A scores A7.4 B7.0 C5.6 D5.0; rule B scores D7.5 C7.1 B4.5 A3.4. Hold candidates and scores fixed: only weights change. This isolates a scoring choice in the toy setup, not real user utility. Ask what did NOT change: candidate pool, feature definitions, who chose the scores and missing needs/accessibility. No evidence that B is fairer, safer, more satisfying or less polarizing. A native/PDF/handout reader has the whole calculation and outcome. Teams can reproduce one row on paper and choose an outcome to test in the real project.'))

# 105-135: one protected research block across two slides.
S.append(activity('01 / RESEARCH + EVIDENCE AUDIT', 30,
    'Investigate your existing decision.', [
    'Start with the team\'s Week 8 papers and one uncertainty about its product.',
    'Closely read one relevant claim; compare 2-3 accumulated sources where feasible.',
    'Look for alternative explanations and contrary evidence, not a verdict to copy.',
    'No relevant full text? Record the gap and narrow the claim. No new paper quota for marks.',
], notes='105-135, one thirty-minute block over slides 34-35. Suggested internal checkpoints: five minutes question/keywords, fifteen close reading/access, ten evidence card and comparison. A team with no feed examines its own selection/ranking/adaptation decision rather than inventing a feature. Manual route: open PolyU Library or a primary DOI, verify title/authors/version, find Methods and Results, follow references. No automated gated access, new service account or private project/user data in search prompts. Agents may suggest citations only if humans open and verify them. If network/library fails, use R2 Design/Discussion or R3 experiment 2 from the prepared evidence ledger, explicitly as a prepared example, not live discovery. Keep all work in existing team notes; no upload.'))
S.append(content('SAME 30-MINUTE BLOCK / EVIDENCE CARD', 'What does the paper actually support?', [
    'Citation + primary link + version + access: abstract only or full text.',
    'People / system / task / comparator / outcome / duration.',
    'One supporting passage with page or section + finding + limitation.',
    'Our inference: what transfers to this product, and what does not?',
], body_size=36, notes='Leave visible during reading. Use actual passage locations, not agent-invented page numbers. An HTML subheading can replace a PDF page. A vendor description, a systematic review and a primary experiment serve different evidential purposes. One strong relevant paper is better than three irrelevant abstracts. Abstract-only access should stay labelled; do not infer unobserved procedures. Prepared offline card in lessons/week09-evidence-ledger.md includes primary passage, method and limit for R2/R3. That ledger is instructor-authored extraction, not a substitute for the full paper or a new assignment.'))

# 135-165: one protected redesign/test block.
S.append(activity('02 / REDESIGN + TEST', 30, 'Change one decision inside your product.', [
    'Draw the existing selection or recommendation and one revised version.',
    'State the user goal, system proxy and one data field or inference to avoid.',
    'Link the revision to a paper, its limitation and your design hypothesis.',
    'Keep the sketch and test in team notes. No new submission or deadline.',
], notes='135-165, one thirty-minute block over slides 36-38: twenty minutes redesign then ten test planning, as in the approved activity foundation. Redesign one objective, data boundary, explanation or usable control; not a whole new product. Retaining a choice with stronger evidence can be a valid revision. The group proposal/concept board/bias register already in the syllabus are not cancelled or rescheduled here. Confirm actual Canvas instructions separately. If the class runs late, trim lecture/debrief detail rather than the fifteen-minute break, thirty-minute research or thirty-minute redesign/test.'))
S.append(cards('SAME 30-MINUTE BLOCK / BENEFITS AND BURDENS', 'Who might this revision miss?', [
    ('PERSON', 'Who benefits?', 'Name the intended user and context. Who is absent from your evidence?'),
    ('CONSEQUENCE', 'Who absorbs an error?', 'An irrelevant suggestion, denied opportunity and harmful inference are not the same cost.'),
    ('RECOURSE', 'What can be done?', 'Sketch a correction, override, explanation or fallback that is actually usable.'),
], text_size=31, notes='This is part of the twenty-minute redesign portion, not a third timer. Ask who contributes data/labour, who gets visibility and who bears errors. Relevant groups need not map to the demographic categories in Gender Shades. Do not collect sensitive attributes merely to fill a template; identify an evidence gap and plan an ethical check. A proposed control is not automatically mitigation: can a person find it, understand it and see whether it changed anything? Paper sketches are sufficient. No private participant research is required today. Worked row / instructor illustration, not a new submission: decision=rank workshops; data=tagged catalogue and prior clicks; missing perspective=people with access needs absent from our evidence; false positive=an inaccessible option ranked suitable; false negative=a suitable option hidden. Proposed recourse=editable access constraints plus browse-all and correction. Test whether a person can recover a suitable option; neither access labels nor control effectiveness are established. This adapts the archived bias-register scaffold to the current fictional example within the same redesign time.'))
S.append(content('SAME 30-MINUTE BLOCK / FINAL 10 MINUTES', 'What result would change your mind?', [
    'Compare [current decision] with [revised decision] in a safe, relevant task.',
    'Observe [one outcome] for [intended users/context], not only clicks or liking.',
    'State a failure condition: if [result], we will [change or remove the decision].',
    'Name what this test still cannot establish. A toy ranking is not a fairness audit.',
], body_size=35, notes='Final ten minutes of the thirty-minute redesign/test block. Example design hypothesis: an optional unfamiliar-event control helps people discover suitable events without losing task success. Candidate outcomes: chosen event fits stated constraints, unwanted exposure, ability to understand and undo a selection; compare baseline/revised under similar conditions. Do not imply a classroom sketch can establish causal effectiveness in every population. Plan only; no demand to recruit participants, expose people to harmful content or collect new sensitive data. An explicit failure condition and transfer boundary matter more than statistical jargon.'))

# 165-180: compare reasoning, preserve open questions.
S.append(two_col('165-180 / COMPARE TWO TEAMS / SPOKEN', 'Compare decisions, not ethical slogans.', [
    'Team 1: decision -> evidence -> limit -> revision -> test.',
    'Team 2: what differs in the user, context, objective or consequence?',
    'Name a trade-off you cannot erase by calling the design "fair".',
], ['LISTEN FOR', 'Does the source support the claim?', 'Can the user actually act on the control?',
    'What remains missing?', 'No universal fairness metric or winner is declared.'],
    right_font='body', left_size=35, right_size=32,
    notes='About ten minutes. Invite two teams, with permission, to describe reasoning without disclosing personal/user data. One minute explanation each, then compare differences and discuss. Do not add a required pitch deck, ClassPoint upload, grade or public answer link. Listen for context and method rather than polished production. If no teams volunteer, use the fictional workshop toy and compare a relevance objective with a novelty objective; explicitly label it an instructor example.'))
S.append(content('CARRY FORWARD / INTO REFRAMING AND PROTOTYPING', 'Keep the evidence and the open question.', [
    'Save the citation, passage, limitation, revised decision and proposed test.',
    'Next: use the evidence to reframe what the product should do, then prototype it.',
    'Existing syllabus: concept board + bias register. Confirm scope and timing on Canvas.',
    'Today creates no new mark, upload or deadline.',
], body_size=36, notes='Final five minutes. Ask one spoken closing question: what did evidence make you less certain about, and what can you now test? The intended revised sequence moves into Double Diamond reframing/testing; no date or syllabus amendment is made by this deck. The published syllabus currently lists recommendations in Week 10 and concept board/bias register in Week 9. Instructor must reconcile these with Canvas and the separately drafted Week 10 material. Preserve the existing group assessment and deliverables. Team work stays private unless existing approved channels require otherwise.'))

# Reference shelf: available when a question needs it, not extra timed instruction.
S.append(content('NON-ASSIGNED / REFERENCE SHELF / R1 / HISTORICAL SYSTEM', 'Candidate generation is not ranking.', [
    source('R1'),
    'Deep Neural Networks for YouTube Recommendations. RecSys 2016, pp. 191-198.',
    'Section 2 + Figure 2: retrieve candidates, then rank a smaller set.',
    'Section 4: a historical watch-time objective, not a map of today\'s product.',
], body_size=33, notes='Primary full eight-page PDF retrieved from Google research archive and consulted for sections 1-4 and Figure 2. DOI 10.1145/2959100.2959190. R1 is mechanism background, not current product documentation, independent audit or proof of social effects. The simplified collaborative matrix and hand-set vector arithmetic in this deck are instructor-authored, not reproduced training examples. No production benchmark is asserted.'))
S.append(content('NON-ASSIGNED / REFERENCE SHELF / R2 + R3 / PRIMARY FULL TEXTS', 'Read the design, not just the headline.', [
    '[R2 / Gauthier, Hodler, Widmer & Zhuravskaya (2026)](https://doi.org/10.1038/s41586-026-10098-2)',
    "The political effects of X's feed algorithm. Nature 652, 416-423. Design; Impact; Methods.",
    source('R3'),
    'Nature Human Behaviour 9, 345-359 (2025); online 18 Dec 2024. Results experiment 2; Methods.',
], body_size=32, notes='Both publisher HTML full texts accessed 21 Oct 2026. Gauthier, Hodler, Widmer and Zhuravskaya; Glickman and Sharot. Evidence ledger records passage locations, comparator/outcome/time and transfer limits. Supplementary PDFs and data/code replication were not independently reviewed. A full-text consultation is not replication or a systematic review. Prepare one short excerpt from either paper for the timed comparison rather than assigning both as compulsory new homework.'))
S.append(content('NON-ASSIGNED / REFERENCE SHELF / AUDIT + DOCUMENTATION', 'An average can hide a relevant difference.', [
    source('R4'),
    '2018 audit: unequal intersectional errors in three binary gender classifiers. Not face identification or a recommender test.',
    '[R5 / Gebru et al. / Datasheets for Datasets / 2021 manuscript](https://arxiv.org/abs/1803.09010v8)',
    'Dataset questions: composition, collection, labels, uses and maintenance. Documentation is not proof of fairness.',
], body_size=32, notes='Gender Shades, PMLR 81, 1-15 (2018), Table 4 and dataset/limitations sections. Historical commercial versions, parliamentary-portrait benchmark and binary gender labels: do not generalize to current vendors or define gender identity from an image. R5 arXiv 1803.09010v8, 1 Dec 2021, manuscript consulted, distinct from asserting identical typesetting to the CACM version. Read sections 3.2-3.7. Source scope for privacy/labour is documentation questions, not legal advice or universal labour statistics. Historical Week 9 PDF/PPTX pp./slides 40-41 visually feature Joy Buolamwini/AJL; this deck replaces uncaptioned historical imagery with a primary audit and correct task boundaries.'))

# Section dividers take seconds inside existing blocks, not extra activity time.
old = S
by_title = {slide.title: slide for slide in old}
S = old[:3]
S.append(section('01 / 10-35 / MECHANISM', 'How a feed selects.',
                 'From the available pool to what you actually see.', bg='#246E70',
                 notes='Ten-second transition within the existing twenty-five-minute mechanism block. The opening asks whose objective; now distinguish selecting candidates, ordering and showing them. The next paper is explained in class: no pre-reading is assumed. Allocate about two minutes to its summary, two to its figure, then abbreviate the original mechanism examples; preserve the spoken reflection.'))
S.append(paper_summary('R1', 'How does YouTube narrow the choice?',  'Full eight-page RecSys 2016 primary PDF read, including sections 1-5, figures and evaluation tables. Section 2 and Figure 2 on PDF p.2 distinguish candidate generation and ranking; sections 3.5 and 4.3 report offline improvements. Live A/B evaluation is discussed but this is not an independent social-outcome trial. Figure 2 is an architecture, not an empirical effect-size chart. Paper question: scale personalized recommendations to a vast changing video corpus. Transfer: inspect which pool an item can enter before debating its final rank. About two minutes within 10-35.'))
S.append(paper_figure('R1', 'First retrieve. Then rank.', 'covington-fig2.png',
    'Figure 2 / PDF p.2 / RecSys 2016', [
    'Millions -> hundreds -> dozens: the reported architecture, not measured social effects.',
    'Engineers compare prediction errors and engagement metrics, not wellbeing. This is a 2016 system.',
    'Design question: can an excluded item reach the ranker? The figure cannot establish fairness.',
], 'Authentic Figure 2 crop from https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf , PDF position 2 of 8, original 2016 paper. Cropped only surrounding prose/caption; arrows and every diagram label remain intact. Retains the tiny original output thumbnails; these are historical illustrations, not a current app screenshot. Architecture alone establishes neither fairness nor wellbeing. Source classroom-use permission on p.1 retained in asset provenance register. About two minutes, then original teaching schema shows interface/presentation and feedback beyond the two-network architecture.'))
S += old[3:9]
S.append(section('02 / 35-60 / OBJECTIVES + DATA', 'Whose errors count?',
    'From noisy proxies to the people hidden by averages.', bg='#246E70',
    notes='Ten-second transition within 35-60. Keep the goal/proxy distinction; compress the illustrative discussion to make room for a historical audit and a documentation proposal. These are different kinds of paper, neither a live recommendation experiment. All source context is supplied in class. Preserve the fifteen-minute break and downstream team blocks.'))
S += old[9:13]
S.append(paper_summary('R4', 'Who disappears inside an average?',  'Full fifteen-page PMLR PDF read, main text including audit methods, Tables 4-5, discussion and references; supplement not separately reviewed. April-May 2017 system versions; PPB 1,270 individuals from six parliaments. Labels are the study constrained binary categories; paper section 3.4 explicitly criticizes the reductionist view. Section 4.4 and Table 4 p.9 support the disparity. The classifier training data were not disclosed, so the audit does not isolate the cause. About two minutes within 35-60.'))
S.append(paper_figure('R4', 'Read the error row, not just the average.', 'gender-shades-table4.png',
    'Table 4 / PDF p.9 / PMLR 2018', [
    'DF/DM = darker female/male; LF/LM = lighter female/male: the study labels.',
    'IBM error row: All 12.1%; DF 34.7%; LM 0.3%. Percent wrong within each group, not all faces.',
    '2017 systems and constrained portraits, not face identification. Error causes and current performance are unknown.',
], 'Authentic full Table 4 crop from https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf , PDF p.9 of 15. All table rows/headers retained; no invented chart or selective reshaping. Explain only error rate (1-TPR); PPV/TPR/FPR remain visible but are not a new statistics lesson. Table describes 2017 versions, not current vendor comparisons. PPB n=1,270; table subgroup denominators differ. Binary perceived labels and relatively fixed-pose parliamentary portraits limit transfer; gender identity cannot be inferred from appearance. About two minutes.'))
S.append(paper_summary('R5', 'What should travel with a dataset?',  'Full arXiv:1803.09010v8 manuscript read, dated 1 Dec 2021, 18 PDF pages, including example appendix. Sections 1-2 explain the motivation and iterative development with product-team/colleague/legal feedback, not a randomized effectiveness trial. Sections 3.2-3.7 provide questions; section 4 p.11 says datasheets are not a complete solution and notes dynamic-data and overhead challenges. Do not conflate version/typesetting with CACM publication. About two minutes, followed by the collection excerpt.'))
S.append(paper_figure('R5', 'Ask who did the work.', 'datasheets-collection-excerpt.png',
    'Section 3.3 excerpt / PDF p.7 / arXiv v8', [
    'An actual question from the paper: who collected the data, and how were they paid?',
    'Apply it to collection, labels and correction in your own product.',
    'A question makes labour visible; answering it does not certify fairness or legal compliance.',
], 'Authentic document excerpt, NOT a figure or empirical result: one complete collection/compensation question from section 3.3, PDF p.7 of 18, arXiv:1803.09010v8, 1 Dec 2021. https://arxiv.org/pdf/1803.09010v8 . Other surrounding questions cover validation, sampling and consent. Main paper has no empirical labour-effect chart to reproduce. About one minute; connect to data boundaries, keeping all questions contextual and optional rather than a newly required submission template.'))
S += old[13:14]  # privacy; labour is now taught through the actual source excerpt.
S.append(section('03 / 60-75 / FEEDBACK EVIDENCE', 'A feed can change us.',
    'Two studies. Different tasks. Bounded conclusions.', bg='#246E70',
    notes='Ten-second transition inside the original fifteen-minute evidence block. Move from auditing a system output to studying changes in people. Explain one field experiment and one controlled task, each with a standalone summary before reading its authentic figures. Budget five minutes R2, five R3, remaining time comparison/transition. No additional homework reading or lecture time.'))
start = next(i for i, slide in enumerate(old) if slide.title == 'Can changing a feed change people?')
S += old[start:]
# Fourth divider starts protected project work without a new timer.
idx = next(i for i, slide in enumerate(S) if slide.title == 'Investigate your existing decision.')
S.insert(idx, section('04 / 105-165 / EVIDENCE TO DESIGN', 'Change one decision.',
    'Research 30 min. Redesign + test 30 min.', bg='#246E70',
    notes='Ten-second orientation within 105-135, not extra time. The toy ranking changed only a weight. Now use an actual relevant source to justify or challenge a decision in the existing team project. Preserve thirty minutes research and thirty minutes redesign/test (twenty plus ten). No ClassPoint, mark, upload or deadline is added; current Canvas concept-board/bias-register scope remains to be confirmed.'))
# Reference shelf supplies links only; not assigned or additional paper instruction.
for slide in S:
    if 'REFERENCE SHELF' in ''.join(r.text for e in slide.els if hasattr(e, 'paras') for p in e.paras for r in p.runs):
        slide.notes = 'NON-ASSIGNED BACKGROUND / untimed reference shelf. ' + slide.notes
S[0].notes = 'Three-hour draft; standalone paper summaries assume no pre-reading. Four topic dividers are transitions within existing budgets, not extra segments. ' + S[0].notes.replace('Main route is slides 1-28; slides 29-31 are a reference shelf, not additional lecture time.', 'Main route ends before the three-slide non-assigned reference shelf; see the updated lesson map.')

# Keep section kickers above the footer band without changing shared layouts.
for slide in S:
    if slide.bg == '#246E70':
        for element in slide.els:
            if getattr(element, 'y', None) == 940:
                element.y = 930

attach_reports(S, Path(__file__).resolve().parent / 'week09-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 09',
            slides=finalize(S, footer(9)), pdf='SD2112-week09.pdf')
