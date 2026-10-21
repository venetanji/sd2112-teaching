# Week 9 evidence and reference ledger

Draft consultation date: **21 October 2026**. This is a bounded teaching audit, not a systematic review or replication. The main narrative uses mechanisms, two contemporary studies and explicitly labelled product hypotheses. Slides 29-31 are a reference shelf, not extra lecture time or newly compulsory homework. Speaker notes are generated from the final native slide source in `lessons/week09-speaker-notes.md`.

## R1 / candidate generation, ranking and noisy proxies

Covington, P., Adams, J. & Sargin, E. (2016). **Deep Neural Networks for YouTube Recommendations.** RecSys '16, 191-198. DOI: https://doi.org/10.1145/2959100.2959190 . Primary record: https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/ . Primary full PDF consulted: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf . Eight-page historical system paper; relevant sections 1-4 and Figure 2 read.

- Supports slides 4-8, 10, 12, 29: candidate generation versus ranking; learned vector representations; sparse implicit feedback; freshness/exploration; an objective need not equal user satisfaction.
- Section 2 / PDF p. 2: "The system is comprised of two neural networks: one for candidate generation and one for ranking."
- Introduction / PDF p. 1: "We rarely obtain the ground truth of user satisfaction and instead model noisy implicit feedback signals."
- Section 3.1 / PDF p. 2 defines high-dimensional user and video embeddings. Section 4 / PDF p. 5 onward discusses ranking and expected watch-time training rather than only click probability.
- Boundary: one company's historical architecture, not a verified map of current YouTube, every recommender, or a causal welfare study. The five-stage feed diagram, hand-set vectors and collaborative matrix are original teaching simplifications, not extracted experimental data.

## R2 / randomized feed assignment and asymmetric effects

Gauthier, G., Hodler, R., Widmer, P. & Zhuravskaya, E. (2026). **The political effects of X's feed algorithm.** Nature 652, 416-423; first online 18 February 2026. DOI/primary publisher full HTML: https://doi.org/10.1038/s41586-026-10098-2 / https://www.nature.com/articles/s41586-026-10098-2 . Publisher full main article including Methods, figures/captions and Discussion consulted; supplementary PDF and replication code/data not independently reviewed or reproduced. No claim of identity to an earlier working paper.

- Supports slides 11, 16, 18, 30. Population: active US X users recruited via YouGov, using X at least several times per month. July-September **2023**, not a 2026 platform intervention. Baseline completed n=6,043; post-survey main sample n=4,965; follow data n=2,387. These are different denominators.
- Intervention/comparator: seven-week compensated randomized algorithmic versus chronological feed assignment, analysed conditional on the **initial** feed setting. Activation is compared with remaining chronological; removal is compared with remaining algorithmic. Initial feed history itself was not randomized. Average duration seven weeks and one day.
- Outcomes: survey policy/current-event attitudes, self-reported partisanship/affective polarization, engagement and observed follow choices in consenting subsets. Distinguish exposure, following and attitudes.
- Design: "A total of 4,965 participants completed the post-treatment survey, forming our main sample."
- Abstract: "Neither switching the algorithm on nor switching it off significantly affected affective polarization or self-reported partisanship."
- Impact of feed algorithm on attitudes and behaviour / Figure 4: activation increased following of conservative activist accounts; reverse-switch contrasts were not comparable reversals. Figure 2 distinguishes policy/current-event outcomes from null partisanship/polarization contrasts.
- Discussion: "The effects are specific to the platform and the time period." Most compliance self-reported; 599 participants ran the post-treatment feed extension. Independent of X, but that independence restricted direct intensity/compliance measurement. Attrition, initial-group differences, platform updates and limited heterogeneity estimation affect interpretation.
- Important mechanism boundary: following/exposure supports the authors' proposed account of asymmetry, but observed differences between people who originally selected different feed settings can still contribute. It is **not** a separately randomized proof that following is the sole mediator or that all algorithms radicalize.
- Product hypothesis, not a tested remedy: distinguish feed mode, recommendation history and following controls, then specify what a reset actually resets. Test an outcome beyond engagement; do not assert that a reset reverses beliefs.

### Prepared offline evidence card / not a live search

Question: if our product exposes new creators and the person follows them, will switching ranking modes undo that exposure? R2 compares feed assignment for seven weeks; it finds changed following after activation but no symmetric reversal after removal. Passage locations: Design, Figure 4 and Discussion. Transfer gap: new product, population, content and version; follow history versus mode are distinct. Candidate design: separate controls and explain their scope. Candidate test: whether users understand and can undo the changed selection; **not** a claim that the published paper tested our UI. Show this prepared extraction openly if library/network access fails.

## R3 / controlled human-AI judgement feedback

Glickman, M. & Sharot, T. **How human-AI feedback loops alter human perceptual, emotional and social judgements.** Nature Human Behaviour 9, 345-359 (2025), first online 18 December 2024. DOI/primary publisher HTML: https://doi.org/10.1038/s41562-024-02077-2 / https://www.nature.com/articles/s41562-024-02077-2 . Published main HTML Results, Discussion and relevant Methods consulted, not a later recommender study. Supplementary PDF, computational models and data/code not independently checked or reproduced.

- Supports slides 11, 17-18, 30. Overall n=1,401 includes multiple main and supplementary experiments; do not present it as one randomized feed sample. Recruitment via Prolific; normal/corrected vision.
- Focused classroom contrast: experiment 2, n=120, moving-dot direction estimates with accurate, upward-biased and noisy **hard-coded** algorithms, counterbalanced order; baseline alone, then interaction. Follow-ups n=50 for biased and accurate conditions.
- Results / "Biased algorithms bias decisions, whereas accurate ones improve them": "The algorithms used here were hard coded to allow full control over their responses."
- The same subsection explains that participants first supplied their own estimate/weighting, before the current algorithm response was revealed. Later independent estimates grew biased with biased advice, while accurate advice improved accuracy. This distinguishes learned judgement shifts from copying the displayed answer on that trial.
- Experiment 1: a CNN/emotion-aggregation pipeline and input/source-label conditions. Results contains a reversed condition-description sentence under "AI's output and human perception of AI shape its influence"; Figure 1 caption and Methods distinguish AI-labelled-human from human-labelled-AI. No numerical label-effect claim is used in the deck.
- Experiment 3 uses **Stable Diffusion 2.1** images and social judgements versus neutral fractal exposure, not a current image model benchmark or a live ranking system. It is supporting context, not an extra lecture block.
- Discussion: "Further research is required to assess the longevity of this effect." The paper explicitly rejects an inference that all AI is biased or every interaction creates bias.
- Product inference: evaluate a person's later independent judgement/choice as well as their immediate acceptance. Transfer to persistent preferences, a deployed feed, child users, every social group or a particular effect size remains unestablished. Awareness/control is a hypothesis to test, not a demonstrated cure.

### Prepared offline evidence card / not a live search

Question: does repeatedly accepting suggestions only affect the current answer? Experiment 2 observes independent estimates made **before** seeing the current algorithm's answer. Biased estimates shift later judgements; accurate assistance can improve them. Passage: Results subsection cited above, Figure 2 and Methods / RDK task. Transfer gap: controlled perceptual task rather than product utility/politics; longevity unresolved. Test idea: independent judgement before and after safe product use with a comparator, not just a satisfaction rating. This is a prepared example, not a newly run experiment.

## R4 / historical intersectional audit, not recommender evidence

Buolamwini, J. & Gebru, T. (2018). **Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification.** PMLR 81, 1-15. Primary full text: https://proceedings.mlr.press/v81/buolamwini18a.html and https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf . Main PDF abstract, dataset design, task boundaries, Table 4 and discussion consulted; supplement not reviewed.

- Supports the bounded example in slide 13 notes and visible slide 31: three historical commercial binary gender classifiers exhibited intersectional error disparities, on the paper's parliamentary-portrait benchmark.
- Table 4 reports error rates up to 34.7% for darker-skinned females, and a maximum 0.8% for lighter-skinned males across the tested systems. These historical figures are **not displayed** on the teaching slide, to keep the task/boundary central rather than imply a current benchmark.
- Not face identification, not an audit of current releases, not a ranking study, and not an assertion that gender identity can be determined from appearance. The paper's binary categories and benchmark composition constrain transfer.
- Design inference: overall accuracy can hide consequential subgroup differences; decide which people, errors and recourse matter to **this** product rather than copying one category system.

## R5 / documentation questions, privacy and labour

Gebru, T. et al. **Datasheets for Datasets**, arXiv:1803.09010v8, **1 December 2021 manuscript**, https://arxiv.org/abs/1803.09010v8 ; retrieved full PDF at https://arxiv.org/pdf/1803.09010 (its first page identifies v8). Sections 1 and 3.2-3.7 consulted. Do not claim typeset identity to CACM publication or a 2018 preprint version.

- Supports slides 13-15, 31 as documentation questions, not causal evidence that documentation guarantees fairness or compliance.
- Section 3.2 composition asks about missing/identifiable/sensitive data. Section 3.3 collection asks who collected the data and how they were compensated, consent and revocation. Section 3.4 preprocessing/cleaning/labeling asks what transformations happened. Sections 3.5 uses and 3.7 maintenance ask about inappropriate uses, responsible maintainers, corrections and retention.
- Section 3.7: "Who will be supporting/hosting/maintaining the dataset?"
- Transfer: explicitly ask who labels/moderates/corrects, who can challenge a label, and what a product actually retains. No universal labour count, jurisdiction-specific legal advice or empirical re-identification rate is inferred from this paper.

## Historical-source reconciliation

- PDF: `references/2025/SD2112 - AI in Design - Week 9.pdf`, **50 PDF pages**, created 31 Oct 2025. Text extracted for PDF positions 23-45 and 47-49; visual inspection of pages 27, 31, 32, 33, 34, 35, 40, 41, 49. PDF page positions are stated explicitly, not assumed to be printed slide numbers.
- Editable copy: `references/onedrive-pptx/SD2112 - AI in Design - Week 9.pptx`, **50 slides**. XML text for slides 23-49 compared against the extracted PDF. The relevant recommenders/bias/redesign wording and sequence match (apart from casing, run boundaries and whitespace). This is a **selected-content comparison**, not a claim of full binary or image identity, nor a claim that every year's PDFs/PPTX match.
- Retain: content-based/collaborative distinction (31), similarity representation/metric (25-27), data/bias concerns (38-45), redesign invitation (47-49).
- Correct: page 33's progression from similar exposure to "Stronger polarization" is not taught as a universal causal chain. R2 finds bounded policy/following effects but no significant affective-polarization effect; R3 is not a live recommender effect size.
- Pages 40-41 visually show Joy Buolamwini/AJL and a face-mask demonstration; the new deck connects them to **classification** audit R4 rather than misdescribing it as face-identification or a recommender experiment. No uncaptioned historical screenshots are copied.
- Page 42 labour quotation has only "p. 219" with no complete attributable source in the relevant recovered material. Omitted as an unverified quotation; replaced by concrete R5 documentation questions.
- Page 49 slider/explore-button suggestion is retained as a possible hypothesis, not a verified anti-polarization intervention. Apply it to the team's existing project, not a compulsory redesign of a named platform.
- Old PR #3 remains reference-only. No obsolete tools, dates, uploads or logistics are copied; no changes to that branch.

## Synthetic demo provenance and fallback

Slides 20-21 and `deck/week09_demo.py` use four invented workshops and hand-set relevance/novelty scores. They are **not student behaviour, platform data, learned vectors, trained recommendations or a fairness evaluation**. Formula: score = w * relevance + (1-w) * novelty. Rule A w=0.8 yields A7.4, B7.0, C5.6, D5.0. Rule B w=0.3 yields D7.5, C7.1, B4.5, A3.4. Same pool and features; only objective weights differ. Results are derived into the native slide from the same deterministic Decimal implementation. Stable ID tie-break; finite [0,1] weight validation. All inputs, formulas and outputs are visible on native/HTML/PDF/handout slides, so a terminal failure requires no substitute service or new account. Optional command: `.venv/bin/python deck/week09_demo.py`. No live model/browser demo is required.

## Deliberately not asserted

Koren et al. (2009), Narayanan & Shmatikov (2008), Zuiderveen Borgesius et al. (2016) and Verbeek (2015) remain optional/background entries in the inherited plan. No new numerical or contemporary empirical claim is built from unreviewed full text. This task does not establish a 2026 research consensus, current product internals, local legal compliance, successful intervention, classroom add-in operation or instructor acceptance.
