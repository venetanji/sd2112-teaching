"""Week 9: learned patterns -> harmful bias -> mediation -> reflective use."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import attach_reports, INK, PAPER
from deckgen.reports import load as load_reports
from deckgen.layouts import (title, content, cards, statement, two_col, activity,
                             finalize, T, Rect, section, _slide, eyebrow)
from deckgen.core import Image
from course import footer
from week09_mediation import bias_distinction, mediation_slides, philosophy_reference
from week09_visual_studies import apply_visuals as visualize_studies
from week09_visual_activities import apply_visuals as visualize_activities
from week09_visual_mediation import apply_visuals as visualize_mediation
from week09_visual_mechanisms import apply_visuals as visualize_mechanisms

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
    slide = content('10-25 / MECHANISM / ORIGINAL TEACHING SCHEMA',
                    'The feed is several decisions.', [], title_size=68,
        notes='About two minutes within 10-25 after the R1 summary and figure. Walk a fictional creative-event feed from the available pool to what is actually seen. Candidate selection retrieves a subset; ranking orders it against an objective; presentation determines visibility; interaction becomes possible feedback. A highly relevant item cannot rank if it was excluded upstream. R1 section 2 and Figure 2 support candidate-generation versus ranking as a historical architecture. The five-stage drawing is an instructor synthesis, not a diagram of current YouTube, TikTok or Spotify. Different systems may combine stages, insert business rules or use no learned model. Ask which stage belongs to Machine A, B or A+B; explicit eligibility rules can surround a learned ranker.')
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
    'Inside the feed.', 'AI bias, technological mediation and reflective use.',
    notes='160-minute teaching allocation; hard finish 13:20: patterns -> bias -> mediation -> examples -> reflective use. Main route ends before the non-assigned reference shelf; see the current lesson map. Relative minutes: 0-10 opening; 10-25 mechanism; 25-45 objectives/bias; 45-60 mediation; 60-75 research; 75-90 break; 90-105 worked example and research preparation; 105-125 harmful-bias text response; 125-145 researched mitigation text response; 145-160 comparison. Preserve the break and two twenty-minute blocks. Start the first activity no later than 12:25 and the second no later than 12:45; finish submissions by 13:05 and discussion/carry-forward by 13:20. Earlier completion is buffer, not permission to lengthen the activities. Relative minutes are allocations, not an inferred class start time. Two ungraded in-class text responses are collected; no new Canvas upload, mark or deadline is introduced. Class date: Friday 30 October 2026, confirmed by Giovanni on 28 October. The syllabus still lists Week 9 concept board/bias register and Week 10 recommendation systems: this revised sequence does not amend assessment requirements. Confirm current milestone scope on Canvas.'))
S.append(content('TODAY / FROM EXAMPLES TO REFLECTIVE USE', 'What shapes the next choice?', [
    'See how a system selects, ranks and learns.',
    'Distinguish a learned pattern from an unfair outcome.',
    'Ask how technology changes what we notice and do.',
    'Find harmful bias. Research ways to reduce it.',
], body_size=36, notes='Opening orientation within 0-10. Keep the existing team project and Week 8 research as resources, not entry requirements. A sketch is enough; students may analyse a documented AI example even if their project has no feed. Introduce the route: mechanisms, bias, mediation, feedback evidence, then two team text responses: a harmful-bias example and researched mitigation. No new pitch, paper quota, Canvas upload or assessment weight. The class is Friday 30 October 2026, confirmed by Giovanni on 28 October; actual Canvas milestone scope remains separate.'))
S.append(statement('Selected for you.\nBy whose objective?',
    eyebrow_text='DISCUSS / USER GOAL / SYSTEM PROXY / PERSON LEFT OUT', size=104, bg=PAPER,
    notes='Remaining opening minutes: pairs name a user goal, the system action and a possible proxy. Example: find a suitable workshop versus maximize click probability. These are instructor-authored examples, not claims about a named service. Return to this distinction after mechanisms. A recommendation is part of the product, not just an algorithm hidden behind a neutral screen.'))

# 10-25: mechanism before moral judgement.
S.append(pipeline())
S.append(two_col('CONTENT-BASED FILTERING / ILLUSTRATIVE', 'Similar to what you liked.', [
    'Describe items by features: genre, pace, mood.',
    'Compare features with previously liked items.',
    'Similar genre is not the right film for every night.',
], ['EXAMPLE', 'Liked: a quiet science-fiction film.',
    'Candidate: another film with those features.',
    'Still unknown: mood, availability, accessibility and why the person liked it.'],
    right_font='body', left_size=34, right_size=32,
    notes='About one minute within 10-25. Teach the principle, not a claim that every recommender uses hand-labelled genres. Features can be explicit metadata or learned vectors; hybrid systems combine signals. Distinguish the item-feature relation from collaborative filtering on slide 10. Do not infer a permanent identity from one click. The example is synthetic and simplified. Historical PDF/PPTX slide 31 makes this distinction; retain it with clearer limits.'))
S.append(two_col('EMBEDDINGS / NUMBERS, NOT AN ESSENCE', 'Near depends on the representation.', [
    'An embedding is a vector of numbers.',
    'Model + training data + metric define what is near.',
    'Near does not mean true, fair or suitable.',
], ['HAND-SET UNIT VECTORS / NOT LEARNED',
    'Query Q = [1, 0]', 'Item A = [0.8, 0.6]; cosine(Q,A) = 0.8',
    'Item B = [0, 1]; cosine(Q,B) = 0',
    'A is nearer by cosine here. Change the representation: the relation can change.'],
    right_font='body', left_size=34, right_size=30,
    notes='About two minutes within 10-25. Recall CLIP/latent representations in Week 5. In the tiny hand-set example all vectors have length one, so their dot product equals cosine similarity; higher cosine means more similar, not smaller distance in every metric. Do not call these two hand-set coordinates an actual trained embedding or a map of personality. R1 section 3.1 defines learned user/video vectors, supporting the representation concept but not this synthetic arithmetic. Historical slide 27 visually relates query/document vectors to a similarity metric; this revision makes the metric and toy status explicit.'))
S.append(native_table('COLLABORATIVE FILTERING / MADE-UP INTERACTIONS',
    'Learn from a pattern of choices.', ['PERSON', 'FILM A', 'FILM B', 'FILM C'],
    [('You', 'A: liked', 'B: liked', 'C: ?'), ('Person P', 'A: liked', 'B: liked', 'C: liked'),
     ('Person Q', 'A: ?', 'B: disliked', 'C: liked')], [600, 360, 360, 360],
    'About two minutes within 10-25. A nearest-neighbour intuition: another person with overlapping preferences liked C, so C is a candidate for you. This table is not enough to guarantee preference or to fit a production model. Question marks mean unobserved, not negative. Collaborative filtering can instead learn latent factors; it need not explicitly find a human look-alike. R1 section 2 describes collaborative candidate generation using coarse behaviour/history; this is an original pedagogical simplification, not its algorithm or real user data.',
    '? means unobserved, not disliked. A shared history suggests a candidate, not certainty.'))
S.append(cards('COLD START / SPARSE DATA', 'What can the system honestly infer?', [
    ('NEW PERSON', 'No history yet.', 'Ask an optional preference, offer a useful default, or let the person browse.'),
    ('NEW ITEM', 'Few interactions.', 'Use item information or explore. Popularity alone can leave new items unseen.'),
    ('MISSING SIGNAL', 'No click is ambiguous.', 'Was it irrelevant, inaccessible, unseen, or simply not needed today?'),
], text_size=31, notes='About one minute within 10-25. Cold start is limited evidence about a new person/item; sparse data also affects established users. The interventions are candidate design choices, not universally effective remedies. R1 introduction and section 3 discuss freshness, sparse implicit feedback and modelling uncertainty around satisfaction. Separate absence of interaction from dislike and from absence of demand. Ask which fields the proposed product truly needs to collect rather than demanding more data by default.'))
S.append(content('SPOKEN REFLECTION / NO COLLECTION', 'A reason is not the whole mechanism.', [
    '"Because you liked Film A."',
    'Does this explain selection, order or visibility?',
    'Which hidden choice matters?',
    'What evidence makes the explanation faithful?',
], body_size=36, notes='Final three minutes of the mechanism block, including transitions. Brief pair exchange; take two spoken answers. This is not an attention-check quiz or ClassPoint submission. A plausible natural-language explanation need not be faithful to the actual ranker. Candidate generation, ranking rules and display can all contribute. Request a product decision, evidence and interpretation rather than a vocabulary definition. Transition: even a faithful explanation does not tell us whether the objective is worthwhile.'))

# 25-45: explicit objectives, missing people, labour and data boundaries.
S.append(cards('25-45 / VALUE VERSUS PROXY', 'A click is not the user goal.', [
    ('GOAL', 'Find a useful event.', 'Does this help the person do what they came to do?'),
    ('PROXY', 'Predict a click.', 'Easy to log, but an accidental click or a misleading title can score well.'),
    ('CHECK', 'Look beyond the click.', 'Ask about task success, unwanted exposure and who is poorly served.'),
], text_size=32, notes='About two minutes within 25-45. Fictional event product, not a measured outcome. R1 introduction calls implicit feedback noisy and section 4 contrasts click/watch-time objectives; do not present its 2016 watch-time objective as current YouTube policy. A proxy is not necessarily useless or malicious. It is incomplete relative to the human goal and may create incentives. Teams should state one goal and one candidate measure without assuming the measure proves welfare.'))
S.append(two_col('FEEDBACK / A PRODUCT CAN TEACH A PREFERENCE', 'The next screen changes the next data.', [
    'Exposure -> choice -> recorded signal -> next suggestion.',
    'People may learn, adapt or follow someone new.',
    'The interface helps create its next data.',
], ['ORIGINAL CONCEPTUAL LOOP', 'choice -> recorded signal -> next suggestion -> changed choice',
    'NOT A MEASURED UNIVERSAL LAW', 'The size, direction and persistence of any effect require evidence.'],
    right_font='body', left_size=34, right_size=31,
    notes='About two minutes within 25-45. Draw the return arrow verbally: suggestions shape available actions, not just mirror an independent preference. The loop is conceptual, not a claim that every iteration increases bias or polarization. R2 tests a field intervention; R3 tests controlled judgement learning. Their different evidence will prevent treating this diagram as an empirical effect size. Even unchanged preferences can produce different clicks if visibility changes; a behavioural change does not by itself prove changed beliefs.'))
S.append(content('EXPLORATION / EXPOSURE', 'Diversity is a decision to specify.', [
    'Different topic, creator, viewpoint or format?',
    'Exploration can expose previously unseen options.',
    'A slider is not proof of reduced polarization.',
    'Test exposure, usable control and the user goal.',
], body_size=36, notes='About two minutes within 25-45. Retain the historical 2025 slide 49 slider/explore-button idea as a design hypothesis, not a proven remedy. Diversity is not one scalar moral property: a topic-diverse list can still omit a community, show unsafe content or overwhelm a person. R1 introduction discusses exploration/exploitation for freshness, not a fairness guarantee. Ask whether exploration should be optional, explained or constrained; do not prescribe a universal setting.'))
S.append(cards('BIAS / LOCATE A DECISION, NOT JUST A BAD OUTPUT', 'Where can a pattern become a problem?', [
    ('COLLECTION + LABELS', 'Who is represented?', 'Who is missing? Who decides what counts as relevant, safe or successful?'),
    ('OBJECTIVE + RULES', 'Who gains visibility?', 'What gets rewarded, filtered out or treated as an acceptable error?'),
    ('INTERACTION', 'Who gets reinforced?', 'Whose past exposure becomes evidence for what should be shown next?'),
], text_size=31, notes='About two minutes within 25-45. Four entry points grouped into three visual cards: collection, labels, objectives and interaction. These are useful analysis handles, not an exhaustive or mutually exclusive taxonomy. Historical slide 43 gives four bias types; avoid implying only malicious design produces unequal effects. Gender Shades (R4, Table 4) found intersectional error disparities in three historical commercial binary gender classifiers: it is not a face-identification/recommender experiment, a definition of anyone\'s gender or a current vendor audit. Its transferable lesson is to inspect relevant groups and errors rather than an overall average alone. R5 sections 3.2-3.5 offer documentation questions; documentation does not establish fairness. Link and fuller audit context are in the reference shelf.'))
S.append(content('PRIVACY / A DATA BOUNDARY IS A DESIGN CHOICE', 'Useful does not mean necessary.', [
    'Collect. Infer. Retain. Share. Different decisions.',
    'Which field or inference can you avoid?',
    'What changes after correction, refusal or deletion?',
    'Removing names does not establish anonymity.',
], body_size=35, notes='About two minutes within 25-45; keep one minute across this block for transitions. Questions can continue during the activity. R5 composition/collection/maintenance questions cover identifiability, consent and retention. This is design analysis, not jurisdiction-specific legal advice, a promise that deletion is technically immediate or an empirical re-identification rate. Optional Netflix de-anonymization paper remains background only; no attack procedure or number is asserted without reading its assumptions. Ask about downstream copies/inferences as well as source records. Teams must use synthetic examples, not collect classmates\' histories or put user records in tools/prompts.'))

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
    notes='Preserve the full fifteen-minute break. Announce the actual return clock time in class. Keep the 13:20 hard finish in view. Next is a fifteen-minute worked preparation for two text submissions, not the earlier ranking-arithmetic demo. Then teams have twenty minutes to identify harmful bias and twenty minutes to research possible mitigation. No account or live AI test is needed for the preparation.'))

# 90-105: prepare the two responses with an explicitly invented example.
S.append(content('90-105 / WORKED EXAMPLE / INVENTED, NOT STUDY DATA',
    'From an experience to a harmful-bias claim.', [],
    notes='First seven minutes of the fifteen-minute preparation. Invented example: an automatic-caption system repeatedly mishears a particular accent, so a viewer misses important instructions. This is a hypothetical design scenario, not a new measured disparity or an assertion about a current product. Ask what was observed, who is disadvantaged, and what comparison would help distinguish harmful bias from an isolated error. A personal encounter can motivate investigation but cannot establish the frequency, cause or population rate. Relate it to the team project where relevant; do not force a captioning feature into it. Students may use a public documented case instead of disclosing their own experience. No names, private transcripts or identifying details.'))
S.append(content('SAME 15-MINUTE PREPARATION / RESEARCH TO RESPONSE',
    'From a source to a mitigation proposal.', [],
    notes='Remaining eight minutes: model how to turn research into a bounded proposal, not a promise to eliminate every bias. For the invented caption case, search for evidence on recognition errors across accents and possible remedies, then read the relevant method, population and result rather than citing only an abstract or an AI summary. Comparing error rates across groups transfers the audit question taught in Gender Shades, not its facial-classification result to speech. Testing broader evaluation coverage and offering editable captions are proposals here, not validated interventions. Students can consider data, labels, objective, model, interface, human review or not using AI for the decision. Explain what each source supports, why it fits this case, and what still needs testing. The next two blocks collect one short-answer response per team each.'))

# 105-125: one team text response on harmful bias, with optional personal disclosure.
S.append(activity('01 / EXPERIENCE + PROJECT / TEXT SUBMISSION', 20,
    'Where have you encountered harmful AI bias?', [
    'Recall examples from your experience; a public case is also welcome.',
    'Explain one: what happened, who was harmed, and why it may be bias.',
    'Relate it to your project if possible; distinguish observation from hypothesis.',
    'One team text response. No names, private details or transcripts.',
], cp={'type': 'short_answer', 'hide_names': True, 'multiple': False},
    notes='105-125, one twenty-minute block: five minutes recalling examples, ten examining one and its possible project relevance, five composing the first text submission. In existing project groups, discuss examples of harmful AI bias encountered in use, observation or research; choose one to explain clearly. Personal experience is optional: use a public documented case instead, with no explanation for that choice required. No required paid account, live generation, harmful prompt or new personal data. A comparison supports inquiry; an isolated output does not establish a systematic rate or a training-data cause. One nominated team member submits one short-answer text for the team at the end of this block; do not ask every member to duplicate it. Response: example, affected people/harm, evidence or uncertainty, and project connection if possible. This is an ungraded in-class response, not a new Canvas deadline. Responses may identify you to the teaching team; hidden display names do not make them anonymous. Do not publish activity URLs, responses, exports or screenshots. Keep individual results off projection; discuss only non-identifying themes after instructor review. Preflight the actual add-in controls before collection; if unavailable, retain private team notes without inventing another upload channel.'))
S.append(content('FIRST RESPONSE / EVIDENCE + HARM', 'What makes this an example of bias?', [
    'Observation: what happened, and compared with what?',
    'Interpretation: which pattern or assumption might explain it?',
    'Consequence: who was disadvantaged, excluded or misrepresented?',
    'Uncertainty: what else could explain it? How does it relate to your project?',
], body_size=36, notes='Leave this guide visible during the first activity. A stereotype in a generated image, uneven classification errors or an exclusion in ranked options make different claims. Label documented finding, our observation and our hypothesis separately. For a public source retain its link/version and relevant passage; for an existing safe test record model/version/date and invented input when available, without uploading private transcripts. One matched pair remains exploratory, not a population audit. Do not infer the training corpus or intention from an output alone. Do not expose private accounts, faces, histories or sensitive attributes. A team may describe a public case instead of personal experience. The first short-answer submission belongs to slide 40; this slide is guidance, not another collection.'))

# 125-145: research-backed proposals, not a compulsory interface-only redesign.
S.append(activity('02 / RESEARCH + MITIGATION / TEXT SUBMISSION', 20,
    'How could this harmful bias be reduced or removed?', [
    'Research your chosen example using credible sources.',
    'Suggest ways to reduce or remove the harmful bias; explain why they fit.',
    'Consider data, model, interaction, human review or not using AI.',
    'One team text response: proposal + source/link + evidence + limitation.',
], cp={'type': 'short_answer', 'hide_names': True, 'multiple': False},
    notes='125-145, one twenty-minute block: fifteen minutes research then five minutes synthesis and the second text submission. Keep the chosen harmful-bias example from the first response. Find relevant research or an authoritative documented intervention; check the actual claim, context, comparator and outcome. Week 8 sources or the readings already taught can be starting points, but explain their transfer limits. Suggest ways harmful bias might be mitigated or removed: data collection or labels, evaluation coverage, objectives or model, interface and recourse, organizational review, or not using AI for this decision. No requirement to retrain a model, build a prototype or confine the proposal to reflective interface use. Cite the source/link supporting the proposal and say what remains uncertain. Documentation, awareness and an explanation alone do not prove reduced harm. Give a simple check that could disconfirm the proposal. One nominated member submits one short-answer text per team, distinct from the first response, during this block. Ungraded; no new Canvas deadline or assessment weight. Do not include identifying personal details from the first example. Responses may identify you; hidden names are not anonymity. Do not publish activity URLs, responses, exports or screenshots; keep individual results off projection. If search access fails, use the prepared course sources and state the gap rather than invent evidence.'))
S.append(cards('MITIGATION / BENEFITS AND BURDENS', 'Who might this revision miss?', [
    ('HARM', 'What changes?', 'Target the harmful outcome, not just whether the system looks fairer.'),
    ('RESPOND', 'What can the person do?', 'Comparison, correction or an alternative must be usable.'),
    ('RESPONSIBILITY', 'Who still must act?', 'A warning does not transfer responsibility to the person harmed.'),
], text_size=31, notes='Use inside the research block, not another timer or submission. A proposal can act on data, model, interface or the decision to use AI. Ask whether any control is understandable, accessible and consequential, and whether it shifts effort to those already disadvantaged. Worked row / instructor illustration, not a new submission: decision=rank workshops; data=tagged catalogue and prior clicks; missing perspective=people with access needs absent from the evidence; false positive=an inaccessible option ranked suitable; false negative=a suitable option hidden. Proposed recourse=editable access constraints, browse-all and correction. Check whether people can recover suitable options, and whether the access labels themselves are reliable. This is a hypothesis, not evidence that a control removes discrimination.'))
S.append(content('SECOND RESPONSE / EVIDENCE + LIMIT', 'How would you check whether it helps?', [
    'Link the source to the proposed change: what does it actually support?',
    'Compare harm before and after, or against a suitable alternative.',
    'Check who benefits, who is still excluded and who carries extra work.',
    'Name a failure condition. Awareness alone is not a fairness fix.',
], body_size=35, notes='Use the final five minutes of the second block to synthesize the researched proposal and submit it; this is not an extra test-planning activity. A concise response names the proposed change, source/link, relevant evidence, transfer limitation and a way to check whether harm falls. Plan a safe comparison rather than recruit participants or run a full audit now. Separate awareness, ability to act, task success and unequal burdens. A source about classification does not automatically validate a speech or recommendation intervention; a vendor claim is not an independent effectiveness study. If the available evidence does not establish removal, say reduction is a hypothesis to test. No additional submission beyond the second short answer on slide 43.'))

# 145-160: compare the two responses without displaying personal experiences.
S.append(content('145-160 / COMPARE EXAMPLES + RESEARCH / SPOKEN',
    'From harmful bias to a researched response.', [],
    notes='About ten minutes: invite teams to discuss only non-identifying or public examples they choose to share. Compare the harm and its evidence, the proposed mitigation and supporting source, and the remaining uncertainty. Do not display the personal-experience response list or identify who supplied an example. No fairness winner, extra pitch, third submission or grade. If nobody volunteers, use the invented caption example and the prepared historical audit as clearly different evidence types. Reflective use is one possible response, not a compulsory remedy or proof of reduced harm.'))
S.append(content('FINISH BY 13:20 / INTO REFRAMING AND PROTOTYPING', 'Keep the example and the open question.', [
    'Learning is selective. Harmful bias needs evidence and context.',
    'Keep the example, researched response and what remains untested.',
    'Reflective use can change mediation; it does not guarantee fairness.',
    'Two in-class text responses. Existing concept board + bias register: check Canvas.',
], body_size=35, notes='Final five minutes. Carry the example, source, proposed mitigation, limitation and check into existing project notes, reframing and prototyping. Two ungraded in-class ClassPoint text responses were requested by Giovanni on 30 October; this replaces the earlier no-collection plan. No new Canvas upload, mark or deadline is introduced. The concept-board/bias-register milestone remains subject to current Canvas instructions. Identifying a harmful pattern, adding a transparency label or making a proposal is not proof that harm has been removed. Both response collections remain private and must not receive public report links.'))

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
S = old[:3]
S.append(section('01 / 10-25 / HOW SYSTEMS SELECT', 'How a feed selects.',
                 'From the available pool to what you actually see.', bg='#246E70',
                 notes='Ten-second transition within the existing fifteen-minute mechanism block. The opening asks whose objective; now distinguish selecting candidates, ordering and showing them. The next paper is explained in class: no pre-reading is assumed. Allocate two minutes to the summary, one to its figure, eight across pipeline/filtering/vectors/cold start, and three to reflection; transitions use the remaining minute. Do not read every bullet.'))
S.append(paper_summary('R1', 'How does YouTube narrow the choice?',  'Full eight-page RecSys 2016 primary PDF read, including sections 1-5, figures and evaluation tables. Section 2 and Figure 2 on PDF p.2 distinguish candidate generation and ranking; sections 3.5 and 4.3 report offline improvements. Live A/B evaluation is discussed but this is not an independent social-outcome trial. Figure 2 is an architecture, not an empirical effect-size chart. Paper question: scale personalized recommendations to a vast changing video corpus. Transfer: inspect which pool an item can enter before debating its final rank. About two minutes within 10-25.'))
S.append(paper_figure('R1', 'First retrieve. Then rank.', 'covington-fig2.png',
    'Figure 2 / PDF p.2 / RecSys 2016', [
    'Millions -> hundreds -> dozens: the reported architecture, not measured social effects.',
    'Engineers compare prediction errors and engagement metrics, not wellbeing. This is a 2016 system.',
    'Design question: can an excluded item reach the ranker? The figure cannot establish fairness.',
], 'Authentic Figure 2 crop from https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf , PDF position 2 of 8, original 2016 paper. Cropped only surrounding prose/caption; arrows and every diagram label remain intact. Retains the tiny original output thumbnails; these are historical illustrations, not a current app screenshot. Architecture alone establishes neither fairness nor wellbeing. Source classroom-use permission on p.1 retained in asset provenance register. About one minute, then original teaching schema shows interface/presentation and feedback beyond the two-network architecture.'))
S += old[3:9]
S.append(section('02 / 25-45 / WHEN PATTERNS BECOME PROBLEMS', 'Whose errors count?',
    'From noisy proxies to the people hidden by averages.', bg='#246E70',
    notes='Ten-second transition within 25-45. Keep the goal/proxy distinction; compress the illustrative discussion to make room for a historical audit and a documentation proposal. These are different kinds of paper, neither a live recommendation experiment. All source context is supplied in class. Preserve the fifteen-minute break and downstream team blocks.'))
S.append(bias_distinction())
S += old[9:13]
S.append(paper_summary('R4', 'Who disappears inside an average?',  'Full fifteen-page PMLR PDF read, main text including audit methods, Tables 4-5, discussion and references; supplement not separately reviewed. April-May 2017 system versions; PPB 1,270 individuals from six parliaments. Labels are the study constrained binary categories; paper section 3.4 explicitly criticizes the reductionist view. Section 4.4 and Table 4 p.9 support the disparity. The classifier training data were not disclosed, so the audit does not isolate the cause. About two minutes within 25-45.'))
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
S += mediation_slides()
S.append(section('04 / 60-75 / HOW SYSTEMS CHANGE US', 'A feed can change us.',
    'Two studies. Different tasks. Bounded conclusions.', bg='#246E70',
    notes='Ten-second transition inside the original fifteen-minute evidence block. Move from auditing a system output to studying changes in people. Explain one field experiment and one controlled task, each with a standalone summary before reading its authentic figures. Budget five minutes R2, five R3, remaining time comparison/transition. No additional homework reading or lecture time.'))
start = next(i for i, slide in enumerate(old) if slide.title == 'Can changing a feed change people?')
S += old[start:]
# Dividers remain inside the protected twenty-minute work blocks.
idx = next(i for i, slide in enumerate(S) if slide.title == 'Where have you encountered harmful AI bias?')
S.insert(idx, section('05 / 105-125 / FIRST TEXT RESPONSE', 'Find and question harmful bias.',
    'Experience. Harm. A possible project connection.', bg='#246E70',
    notes='Ten-second orientation inside the first twenty-minute block, not extra time. Students discuss examples of harmful bias from experience or a public case and explain one clearly. A project connection is encouraged, not compulsory. Personal disclosure is optional and identifying details are excluded. One nominated member submits the first text response for the team at the end of the block. Keep results private; hidden display names do not establish anonymity.'))
idx = next(i for i, slide in enumerate(S) if slide.title == 'How could this harmful bias be reduced or removed?')
S.insert(idx, section('06 / 125-145 / SECOND TEXT RESPONSE', 'Research ways to reduce the harm.',
    'Find evidence. Propose a response. Say what remains untested.', bg='#246E70',
    notes='Ten-second transition within the second twenty-minute block. Research ways to mitigate or remove the chosen harmful bias; use fifteen minutes research and five minutes synthesis/submission. Do not restrict responses to an interface sketch. Consider data, objectives, model, interaction, human review or avoiding AI for the decision. The second short answer needs supporting sources and a limitation, not a claim of guaranteed elimination. No extra minutes or assessment deadline.'))
S.append(philosophy_reference())
# Reference shelf supplies links only; not assigned or additional paper instruction.
for slide in S:
    if 'REFERENCE SHELF' in ''.join(r.text for e in slide.els if hasattr(e, 'paras') for p in e.paras for r in p.runs):
        slide.notes = 'NON-ASSIGNED BACKGROUND / untimed reference shelf. ' + slide.notes
S[0].notes = 'Class ends at 13:20; standalone paper summaries assume no pre-reading. Topic dividers are transitions within their blocks, not extra minutes. ' + S[0].notes

# Keep section kickers above the footer band without changing shared layouts.
for slide in S:
    if slide.bg == '#246E70':
        for element in slide.els:
            if getattr(element, 'y', None) == 940:
                element.y = 930

visualize_studies(S)
visualize_activities(S)
visualize_mediation(S)
visualize_mechanisms(S)

def protected_report_entries(source):
    """Both linked responses can contain experience details; never publish them."""
    entries = [dict(entry) for entry in load_reports(source)]
    for entry in entries:
        entry['activity'] = None
        entry['withheld'] = 'private team bias response; do not publish'
    return entries


attach_reports(S, protected_report_entries(Path(__file__).resolve().parent / 'week09-reports.json'))
DECK = dict(title='SD2112 / AI in Design / Week 09',
            slides=finalize(S, footer(9)), pdf='SD2112-week09.pdf')
