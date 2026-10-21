"""Week 9: recommendation mechanisms -> bounded evidence -> project revision."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import (title, content, cards, statement, two_col, activity,
                             finalize, T, Rect)
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
    return f'[{key} / {name}]({url})'


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
        notes='About five minutes. Walk a fictional creative-event feed from the available pool to what is actually seen. Candidate selection retrieves a subset; ranking orders it against an objective; presentation determines visibility; interaction becomes possible feedback. A highly relevant item cannot rank if it was excluded upstream. R1 section 2 and Figure 2 support candidate-generation versus ranking as a historical architecture. The five-stage drawing is an instructor synthesis, not a diagram of current YouTube, TikTok or Spotify. Different systems may combine stages, insert business rules or use no learned model. Ask which stage belongs to Machine A, B or A+B; explicit eligibility rules can surround a learned ranker.')
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
    slide.els += [T(120, 700, 1680, 100, 'Feedback can change later candidates and ranks.\nThe person may also change what they want or whom they follow.', 'body', 36, INK, lh=1.25),
                  T(120, 886, 1680, 65, source('R1'), 'body', 27, '#246E70')]
    return slide


# 0-10: reconnect, without recollecting Week 7 or Week 8 work.
S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 09',
    'Inside the feed.', 'Recommendations. Bias. The decisions that shape the next choice.',
    notes='Three-hour draft class: research -> AI-product analysis -> existing team project. Main route is slides 1-28; slides 29-31 are a reference shelf, not additional lecture time. Relative minutes: 0-10 opening; 10-35 mechanism; 35-60 objectives/bias; 60-75 research; 75-90 break; 90-105 controlled ranking demo; 105-135 research/evidence audit; 135-165 redesign and test; 165-180 comparison. Preserve all protected blocks. No date, submission, mark or deadline is announced. The syllabus still lists Week 9 concept board/bias register and Week 10 recommendation systems: this draft follows the intended revised sequence but does not amend the syllabus. Instructor must reconcile Canvas and timetable before teaching.'))
S.append(content('0-10 / CONTINUE YOUR EXISTING PROJECT', 'What did your product promise?', [
    'Keep your team concept, image and Week 8 research in view.',
    'What relationship did the interface invite? What did the person expect?',
    'Now locate one decision: what is selected, ranked, suggested or hidden?',
    'A sketch is enough. Do not add a feed if your product does not need one.',
], body_size=36, notes='About four minutes within the opening. Recall Week 8 humanizing AI and mediation: an apparently friendly adviser or invisible background system shapes what a person can notice and choose. Reuse the existing evidence, not a new team pitch or mandatory prototype. Ask for one concrete moment of use. Products can rank design alternatives, route requests or suggest actions without a scrolling feed. Teams open their own work privately; no projection of personal records and no new upload.'))
S.append(statement('Selected for you.\nBy whose objective?',
    eyebrow_text='DISCUSS / USER GOAL / SYSTEM PROXY / PERSON LEFT OUT', size=104, bg=PAPER,
    notes='Remaining opening minutes: pairs name a user goal, the system action and a possible proxy. Example: find a suitable workshop versus maximize click probability. These are instructor-authored examples, not claims about a named service. Return to this distinction after mechanisms. A recommendation is part of the product, not just an algorithm hidden behind a neutral screen.'))

# 10-35: mechanism before moral judgement.
S.append(pipeline())
S.append(two_col('CONTENT-BASED FILTERING / ILLUSTRATIVE', 'Similar to what you liked.', [
    'Describe items by features: a film might be science fiction, comic or slow-paced.',
    'Compare a candidate with features of items a person has liked.',
    'Feature choice matters: similar genre is not necessarily the right film tonight.',
], ['EXAMPLE', 'Liked: a quiet science-fiction film.',
    'Candidate: another film with those features.',
    'Still unknown: mood, availability, accessibility and why the person liked it.'],
    right_font='body', left_size=34, right_size=32,
    notes='About four minutes. Teach the principle, not a claim that every recommender uses hand-labelled genres. Features can be explicit metadata or learned vectors; hybrid systems combine signals. Distinguish the item-feature relation from collaborative filtering on slide 7. Do not infer a permanent identity from one click. The example is synthetic and simplified. Historical PDF/PPTX slide 31 makes this distinction; retain it with clearer limits.'))
S.append(two_col('EMBEDDINGS / NUMBERS, NOT AN ESSENCE', 'Near depends on the representation.', [
    'An embedding represents an item or query as a vector of numbers.',
    'A model, training data and similarity metric determine which items are near.',
    'Near in this space does not mean true, fair, suitable or psychologically similar.',
], ['HAND-SET UNIT VECTORS / NOT LEARNED',
    'Query Q = [1, 0]', 'Item A = [0.8, 0.6]; cosine(Q,A) = 0.8',
    'Item B = [0, 1]; cosine(Q,B) = 0',
    'A is nearer by cosine here. Change the representation: the relation can change.'],
    right_font='body', left_size=34, right_size=30,
    notes='About four minutes. Recall CLIP/latent representations in Week 5. In the tiny hand-set example all vectors have length one, so their dot product equals cosine similarity; higher cosine means more similar, not smaller distance in every metric. Do not call these two hand-set coordinates an actual trained embedding or a map of personality. R1 section 3.1 defines learned user/video vectors, supporting the representation concept but not this synthetic arithmetic. Historical slide 27 visually relates query/document vectors to a similarity metric; this revision makes the metric and toy status explicit.'))
S.append(native_table('COLLABORATIVE FILTERING / MADE-UP INTERACTIONS',
    'Learn from a pattern of choices.', ['PERSON', 'FILM A', 'FILM B', 'FILM C'],
    [('You', 'A: liked', 'B: liked', 'C: ?'), ('Person P', 'A: liked', 'B: liked', 'C: liked'),
     ('Person Q', 'A: ?', 'B: disliked', 'C: liked')], [600, 360, 360, 360],
    'About four minutes. A nearest-neighbour intuition: another person with overlapping preferences liked C, so C is a candidate for you. This table is not enough to guarantee preference or to fit a production model. Question marks mean unobserved, not negative. Collaborative filtering can instead learn latent factors; it need not explicitly find a human look-alike. R1 section 2 describes collaborative candidate generation using coarse behaviour/history; this is an original pedagogical simplification, not its algorithm or real user data.',
    '? means unobserved, not disliked. A shared history suggests a candidate, not certainty.'))
S.append(cards('COLD START / SPARSE DATA', 'What can the system honestly infer?', [
    ('NEW PERSON', 'No history yet.', 'Ask an optional preference, offer a useful default, or let the person browse.'),
    ('NEW ITEM', 'Few interactions.', 'Use item information or explore. Popularity alone can leave new items unseen.'),
    ('MISSING SIGNAL', 'No click is ambiguous.', 'Was it irrelevant, inaccessible, unseen, or simply not needed today?'),
], text_size=31, notes='About four minutes. Cold start is limited evidence about a new person/item; sparse data also affects established users. The interventions are candidate design choices, not universally effective remedies. R1 introduction and section 3 discuss freshness, sparse implicit feedback and modelling uncertainty around satisfaction. Separate absence of interaction from dislike and from absence of demand. Ask which fields the proposed product truly needs to collect rather than demanding more data by default.'))
S.append(content('SPOKEN REFLECTION / NO COLLECTION', 'A reason is not the whole mechanism.', [
    'Your interface says: "Because you liked Film A."',
    'Which decision does that explain: retrieval, order, visibility, or all three?',
    'Name one hidden choice that matters to the person.',
    'What evidence would you need before displaying that explanation?',
], body_size=36, notes='Final four minutes of the mechanism block. Brief pair exchange; take two spoken answers. This is not an attention-check quiz or ClassPoint submission. A plausible natural-language explanation need not be faithful to the actual ranker. Candidate generation, ranking rules and display can all contribute. Request a product decision, evidence and interpretation rather than a vocabulary definition. Transition: even a faithful explanation does not tell us whether the objective is worthwhile.'))

# 35-60: explicit objectives, missing people, labour and data boundaries.
S.append(cards('35-60 / VALUE VERSUS PROXY', 'A click is not the user goal.', [
    ('GOAL', 'Find a useful event.', 'Does this help the person do what they came to do?'),
    ('PROXY', 'Predict a click.', 'Easy to log, but an accidental click or a misleading title can score well.'),
    ('CHECK', 'Look beyond the click.', 'Ask about task success, unwanted exposure and who is poorly served.'),
], text_size=32, notes='About four minutes. Fictional event product, not a measured outcome. R1 introduction calls implicit feedback noisy and section 4 contrasts click/watch-time objectives; do not present its 2016 watch-time objective as current YouTube policy. A proxy is not necessarily useless or malicious. It is incomplete relative to the human goal and may create incentives. Teams should state one goal and one candidate measure without assuming the measure proves welfare.'))
S.append(two_col('FEEDBACK / A PRODUCT CAN TEACH A PREFERENCE', 'The next screen changes the next data.', [
    'Show an item -> a person notices or chooses -> log an interaction -> update later suggestions.',
    'Exposure affects what can be clicked. A person may also learn, adapt or change whom they follow.',
    'Observed behaviour is partly shaped by the earlier interface.',
], ['ORIGINAL CONCEPTUAL LOOP', 'choice -> recorded signal -> next suggestion -> changed choice',
    'NOT A MEASURED UNIVERSAL LAW', 'The size, direction and persistence of any effect require evidence.'],
    right_font='body', left_size=34, right_size=31,
    notes='About four minutes. Draw the return arrow verbally: suggestions shape available actions, not just mirror an independent preference. The loop is conceptual, not a claim that every iteration increases bias or polarization. R2 tests a field intervention; R3 tests controlled judgement learning. Their different evidence will prevent treating this diagram as an empirical effect size. Even unchanged preferences can produce different clicks if visibility changes; a behavioural change does not by itself prove changed beliefs.'))
S.append(content('EXPLORATION / EXPOSURE', 'Diversity is a decision to specify.', [
    'Different from what: topic, creator, viewpoint, format, or familiarity?',
    'Exploration can reveal an option that past behaviour never made visible.',
    'A "diversity" slider does not itself prove reduced bias or polarization.',
    'Test the actual exposure, the person\'s control and the outcome they care about.',
], body_size=36, notes='About four minutes. Retain the historical 2025 slide 49 slider/explore-button idea as a design hypothesis, not a proven remedy. Diversity is not one scalar moral property: a topic-diverse list can still omit a community, show unsafe content or overwhelm a person. R1 introduction discusses exploration/exploitation for freshness, not a fairness guarantee. Ask whether exploration should be optional, explained or constrained; do not prescribe a universal setting.'))
S.append(cards('BIAS / LOCATE A DECISION, NOT JUST A BAD OUTPUT', 'Where can a pattern become a problem?', [
    ('COLLECTION + LABELS', 'Who is represented?', 'Who is missing? Who decides what counts as relevant, safe or successful?'),
    ('OBJECTIVE + RULES', 'Who gains visibility?', 'What gets rewarded, filtered out or treated as an acceptable error?'),
    ('INTERACTION', 'Who gets reinforced?', 'Whose past exposure becomes evidence for what should be shown next?'),
], text_size=31, notes='About five minutes. Four entry points grouped into three visual cards: collection, labels, objectives and interaction. These are useful analysis handles, not an exhaustive or mutually exclusive taxonomy. Historical slide 43 gives four bias types; avoid implying only malicious design produces unequal effects. Gender Shades (R4, Table 4) found intersectional error disparities in three historical commercial binary gender classifiers: it is not a face-identification/recommender experiment, a definition of anyone\'s gender or a current vendor audit. Its transferable lesson is to inspect relevant groups and errors rather than an overall average alone. R5 sections 3.2-3.5 offer documentation questions; documentation does not establish fairness. Link and fuller audit context are in the reference shelf.'))
S.append(two_col('HUMAN LABOUR / DATA IS MADE AND MAINTAINED', 'Who keeps the system working?', [
    'Someone may collect, label, clean, moderate, correct and maintain the data.',
    'Ask whose judgement becomes a label, who can dispute it, and who absorbs errors.',
    'Do not assume an automated-looking interface means nobody is doing the work.',
], ['PROJECT QUESTION', 'Who labels "good advice" or "relevant" in your product?',
    'What support, correction route and maintenance would that role require?', source('R5')],
    right_font='body', left_size=34, right_size=30,
    notes='About four minutes. R5 section 3.3 asks who collected data and how they were compensated; sections 3.4 and 3.7 ask about preprocessing/labels and maintenance. This supports asking concrete labour questions, not a numerical estimate of all AI workers. The historical slide 42 quotation gives only a page number with no recoverable source attribution; do not repeat it as a verified quotation. No claim that every system uses the same labour arrangement. A team may decide it cannot safely provide a proposed feature without a qualified human role; that is a legitimate product revision.'))
S.append(content('PRIVACY / A DATA BOUNDARY IS A DESIGN CHOICE', 'Useful does not mean necessary.', [
    'List what is collected, inferred, retained and shared. These are different actions.',
    'Which field can the product avoid? Could a temporary preference replace a stored profile?',
    'Can a person correct, decline or delete it? What would actually change afterwards?',
    'Do not treat removal of names as proof that behaviour is anonymous.',
], body_size=35, notes='Final four minutes. R5 composition/collection/maintenance questions cover identifiability, consent and retention. This is design analysis, not jurisdiction-specific legal advice, a promise that deletion is technically immediate or an empirical re-identification rate. Optional Netflix de-anonymization paper remains background only; no attack procedure or number is asserted without reading its assumptions. Ask about downstream copies/inferences as well as source records. Teams must use synthetic examples, not collect classmates\' histories or put user records in tools/prompts.'))

# 60-75: two studies, distinct systems, outcomes and causal scope.
S.append(two_col('60-75 / R2 / X FIELD EXPERIMENT IN 2023', 'Changing the feed can change following.', [
    'Seven-week randomized assignment: algorithmic versus chronological feed for active US X users.',
    'Activating the algorithm shifted some policy attitudes and follow choices. Switching it off was not symmetric.',
    source('R2'),
], ['BOUNDARY', 'No significant effect on self-reported partisanship or affective polarization.',
    'Platform and period matter. Compliance was largely self-reported.',
    'DESIGN QUESTION', 'Should a reset address mode, history, following, or each separately?'],
    right_font='body', left_size=32, right_size=30,
    notes='About six minutes. Published open-access Nature article retrieved 21 Oct 2026: online 18 Feb 2026, volume 652 pp. 416-423. Read Design, Impact, Discussion and Methods including figure captions. 6,043 completed baseline, 4,965 completed post-survey (main sample), 2,387 shared follow data. July-September 2023, average 7 weeks + 1 day. Random assignment within initial feed groups permits intention-to-treat comparisons, not a randomized lifetime exposure history. Activation versus staying chronological shifted conservative policy-priority/current-event indices and conservative activist following; removal in initially algorithmic users did not produce comparable reversals. Authors support a following/exposure mechanism but acknowledge unobserved differences between initial-feed groups may contribute to asymmetry. Do not say the whole mechanism was independently randomized or that all algorithms radicalize. Most compliance self-report, 599 post-survey extension users, no transfer to current X or Hong Kong users established. Supplementary PDF/replication not independently reviewed or reproduced. Reset design is our hypothesis, not a validated remedy.'))
S.append(two_col('R3 / CONTROLLED JUDGEMENT TASKS / 2024-25', 'People can learn a system\'s bias.', [
    'In controlled experiments, biased algorithms shifted later independent human judgements.',
    'Accurate algorithms could improve judgement instead.', source('R3'),
], ['WHAT WAS TESTED', 'Emotion aggregation, moving-dot estimates and social judgements, not a live feed.',
    'WHAT REMAINS OPEN', 'Long-term persistence and the size of any recommender effect.',
    'DESIGN QUESTION', 'Measure the next independent choice, not only acceptance of a suggestion.'],
    right_font='body', left_size=33, right_size=30,
    notes='About five minutes. Published online 18 Dec 2024, NHB 9, 345-359 (2025). Publisher full HTML retrieved; Results, Discussion and Methods reviewed. Overall n=1,401 includes supplementary experiments, not a single feed sample. Focus on experiment 2: 120 Prolific participants estimated moving-dot direction, first alone then with accurate, upward-biased or noisy hard-coded algorithms in counterbalanced order. Algorithm output was revealed after participants\' own estimate/weighting. Later independent estimates shifted in the biased condition; accurate advice improved accuracy. Follow-up n=50 per biased/accurate condition examined repeated interaction. This is not merely copying the current displayed answer. It is also not a news-ranking experiment or proof of lasting everyday preference change. Experiment 1 uses a CNN/emotion task; experiment 3 uses Stable Diffusion 2.1 image exposure (not a current model benchmark). The narrative has a reversed-label sentence in Results under input/perception; Fig. 1 caption and Methods distinguish the conditions correctly. No numerical label-effect claim used here. Supplement PDF/computational fits not independently checked or reproduced.'))
S.append(native_table('COMPARE EVIDENCE / NOT "ALL FEEDS POLARIZE"',
    'Different studies answer different questions.', ['STUDY', 'SYSTEM / TIME', 'WHAT TO CARRY FORWARD'],
    [('R2 / field', 'X / 7 weeks', 'Mode and following can differ.'),
     ('R3 / controlled', 'Task algorithms / sessions', 'Later judgement can change.'),
     ('Your product', 'New context / unknown', 'Treat the transfer as a hypothesis.')],
    [360, 590, 730],
    'Final four minutes before break. Ask teams to name population, system, comparator, outcome and time before asserting a filter bubble or an echo chamber. These terms overlap in ordinary use but do not name one measured outcome. R2 found no significant affective-polarization/partisanship effect despite other changes; R3 establishes controlled learning mechanisms, not field effect sizes. A null is not proof of universal absence, and a positive result is not universal presence. R2\'s main article discusses contrasting prior Meta results; that citation is background, not independently re-reviewed here. Do not claim a fresh systematic review or consensus. Use one methods/results excerpt in discussion, not two new compulsory full papers.',
    'Ask: platform / population / comparator / outcome / time. Keep the mismatch visible.'))
S.append(statement('Break.\n15 minutes.', eyebrow_text='75-90 / PROTECTED BREAK / RELATIVE CLASS TIME', size=120,
    notes='Preserve the full fifteen-minute break. Announce the actual return clock time in class once the timetable is confirmed. Next is one fifteen-minute controlled demo, then thirty minutes research and thirty minutes redesign/test. Open slides 20-21; the full fallback is native and needs no login, network or learned model.'))

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
], notes='105-135, one thirty-minute block over slides 22-23. Suggested internal checkpoints: five minutes question/keywords, fifteen close reading/access, ten evidence card and comparison. A team with no feed examines its own selection/ranking/adaptation decision rather than inventing a feature. Manual route: open PolyU Library or a primary DOI, verify title/authors/version, find Methods and Results, follow references. No automated gated access, new service account or private project/user data in search prompts. Agents may suggest citations only if humans open and verify them. If network/library fails, use R2 Design/Discussion or R3 experiment 2 from the prepared evidence ledger, explicitly as a prepared example, not live discovery. Keep all work in existing team notes; no upload.'))
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
], notes='135-165, one thirty-minute block over slides 24-26: twenty minutes redesign then ten test planning, as in the approved activity foundation. Redesign one objective, data boundary, explanation or usable control; not a whole new product. Retaining a choice with stronger evidence can be a valid revision. The group proposal/concept board/bias register already in the syllabus are not cancelled or rescheduled here. Confirm actual Canvas instructions separately. If the class runs late, trim lecture/debrief detail rather than the fifteen-minute break, thirty-minute research or thirty-minute redesign/test.'))
S.append(cards('SAME 30-MINUTE BLOCK / BENEFITS AND BURDENS', 'Who might this revision miss?', [
    ('PERSON', 'Who benefits?', 'Name the intended user and context. Who is absent from your evidence?'),
    ('CONSEQUENCE', 'Who absorbs an error?', 'An irrelevant suggestion, denied opportunity and harmful inference are not the same cost.'),
    ('RECOURSE', 'What can be done?', 'Sketch a correction, override, explanation or fallback that is actually usable.'),
], text_size=31, notes='This is part of the twenty-minute redesign portion, not a third timer. Ask who contributes data/labour, who gets visibility and who bears errors. Relevant groups need not map to the demographic categories in Gender Shades. Do not collect sensitive attributes merely to fill a template; identify an evidence gap and plan an ethical check. A proposed control is not automatically mitigation: can a person find it, understand it and see whether it changed anything? Paper sketches are sufficient. No private participant research is required today.'))
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
S.append(content('REFERENCE SHELF / R1 / HISTORICAL SYSTEM', 'Candidate generation is not ranking.', [
    source('R1'),
    'Deep Neural Networks for YouTube Recommendations. RecSys 2016, pp. 191-198.',
    'Section 2 + Figure 2: retrieve candidates, then rank a smaller set.',
    'Section 4: a historical watch-time objective, not a map of today\'s product.',
], body_size=33, notes='Primary full eight-page PDF retrieved from Google research archive and consulted for sections 1-4 and Figure 2. DOI 10.1145/2959100.2959190. R1 is mechanism background, not current product documentation, independent audit or proof of social effects. The simplified collaborative matrix and hand-set vector arithmetic in this deck are instructor-authored, not reproduced training examples. No production benchmark is asserted.'))
S.append(content('REFERENCE SHELF / R2 + R3 / PRIMARY FULL TEXTS', 'Read the design, not just the headline.', [
    source('R2'),
    'Nature 652, 416-423 (2026). Design; Impact; Discussion; Methods.',
    source('R3'),
    'Nature Human Behaviour 9, 345-359 (2025); online 18 Dec 2024. Results experiment 2; Methods.',
], body_size=32, notes='Both publisher HTML full texts accessed 21 Oct 2026. Gauthier, Hodler, Widmer and Zhuravskaya; Glickman and Sharot. Evidence ledger records passage locations, comparator/outcome/time and transfer limits. Supplementary PDFs and data/code replication were not independently reviewed. A full-text consultation is not replication or a systematic review. Prepare one short excerpt from either paper for the timed comparison rather than assigning both as compulsory new homework.'))
S.append(content('REFERENCE SHELF / AUDIT + DOCUMENTATION', 'An average can hide a relevant difference.', [
    source('R4'),
    '2018 audit: unequal intersectional errors in three binary gender classifiers. Not face identification or a recommender test.',
    source('R5'),
    'Dataset questions: composition, collection, labels, uses and maintenance. Documentation is not proof of fairness.',
], body_size=32, notes='Gender Shades, PMLR 81, 1-15 (2018), Table 4 and dataset/limitations sections. Historical commercial versions, parliamentary-portrait benchmark and binary gender labels: do not generalize to current vendors or define gender identity from an image. R5 arXiv 1803.09010v8, 1 Dec 2021, manuscript consulted, distinct from asserting identical typesetting to the CACM version. Read sections 3.2-3.7. Source scope for privacy/labour is documentation questions, not legal advice or universal labour statistics. Historical Week 9 PDF/PPTX pp./slides 40-41 visually feature Joy Buolamwini/AJL; this deck replaces uncaptioned historical imagery with a primary audit and correct task boundaries.'))

attach_reports(S, Path(__file__).resolve().parent / 'week09-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 09',
            slides=finalize(S, footer(9)), pdf='SD2112-week09.pdf')
