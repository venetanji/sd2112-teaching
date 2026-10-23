# Week 11 evidence and references ledger

Primary audit performed 21 October 2026 for the implemented PR #24 draft; current targeted recheck and public-review decision are dated 22 October below. This is focused primary-text review, not a systematic review, replication or legal clearance. PDF page positions below count from the first PDF page; printed pages are identified separately. Research downloads stay outside git at `/home/venetanji/.openclaw/workspace-sd2112/tmp/weekly-draft-audit-20261021/week11/sources/` and `/home/venetanji/.openclaw/workspace-sd2112/tmp/paper-visual-revision-20261021/week11/sources/`.

## Claim register

### N / qualitative design experience / slides 6-7 and comparison on 11

Syeda Masooma Naqvi, Ruichen He and Harmanpreet Kaur. 2025. **Catalyst for Creativity or a Hollow Trend?: A Cross-Level Perspective on The Role of Generative AI in Design**. CHI '25, 16 pages. DOI: https://doi.org/10.1145/3706598.3713233 . Consulted author-hosted ACM-formatted full text: https://harmanpk.github.io/Papers/CHI2025_GenAI-Design.pdf (direct HTTP 200, 16 pages).

- **Method/context:** PDF4-5, sections 3.1-3.3: 28 artifact-based semi-structured interviews; 10 junior students, 10 senior students, eight professionals. U.S. residents with prior image-generation experience, recruited through targeted outreach/social media/snowball sampling. Interviews in June-August 2024 about an already made artifact; thematic analysis. No assigned AI/no-AI comparator or skill-change follow-up.
- **Result anchor:** PDF8, section 4.5.1-3: junior participants describe shared authorship; seniors link ownership to prompting/editing; professionals discuss developers' contribution and responsibility. The phrase “ownership depended on how much prompting they provided” reports participant perspectives, not the researchers' legal determination.
- **Bounded claim:** participants at different experience levels described different values around AI, skills, ownership and control. Reported concern about foundational skills is not evidence of experimentally caused deskilling. No prevalence claim about all designers.
- **Limits:** section 6, PDF13-14: self-selection, artifact elicitation, fast-changing tools, prompt-based scope and exclusively U.S. sample. Cross-level comparison is not longitudinal tracking of skill loss.
- **Transfer/design hypothesis:** a process-history view may make contributions and choices inspectable. This interface was not evaluated here. Visitor agency in our fictional exhibition guide needs its own evidence.

### D / randomized access to starting ideas / slides 8-10

Anil R. Doshi and Oliver P. Hauser. 2024. **Generative AI enhances individual creativity but reduces the collective diversity of novel content**. *Science Advances* 10(28), eadn5290. https://doi.org/10.1126/sciadv.adn5290 . Final primary full text read through Europe PMC XML: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11244532/fullTextXML ; human-readable primary archive: https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/ . Publisher PDF endpoint returned 403; no bypass was attempted. Supplement not separately reviewed.

- **Method/comparator:** Introduction/Fig.1 and Materials and Methods, “Writer study and experimental conditions”: UK Prolific sample, 293 included eight-sentence stories, random assignment to human-only, access to one, or access to up to five three-sentence GPT-4 starting ideas. 500 recruited is not the analyzed writer count. Access is optional within AI conditions; analysis is intention-to-treat. 600 separate evaluators rate stories initially without AI-access disclosure; later exploratory ownership questions are distinct.
- **Outcomes:** Results, “Baseline versus generative AI conditions” and Fig.2: higher average novelty/usefulness ratings with access. Usefulness is adapted to audience suitability, feasibility as a book and publishability, not general social usefulness. “Similarity of stories” and Fig.4: higher cosine similarity of a story embedding to the average embedding of OTHER stories in the same condition.
- **Bounded visible claim:** average individual ratings can improve while stories within a condition become more similar. No slide percentages; no accidental population denominator, quality/DAT rank or count of cultural perspectives.
- **Limit/time:** Discussion explicitly limits length, writing medium, short-story output, fixed prompts and absence of interactive LLM dialogue. Participants are not professional writers. A short experiment is not long-term learning or a design-studio trial; embedding similarity is not by itself a fairness/representation measure.
- **Transfer/hypothesis:** independent ideation before suggestions is a candidate test, not a tested remedy in either N or D. Measure relevance/quality AND variety; examine who is missing separately.

### J / psychological ownership / slides 19-20

Nikhita Joshi and Daniel Vogel. 2026. **Interaction Techniques that Encourage Longer Prompts Can Improve Psychological Ownership when Writing with AI**. Graphics Interface 2026, June 9-12, Waterloo, 11 pages. DOI: https://doi.org/10.1145/3831423.3831427 . Consulted author preprint https://arxiv.org/abs/2507.03670v3 ; https://arxiv.org/pdf/2507.03670v3 (12 July 2026, direct 200). Version is v3, not the 2025 original.

- **Method:** sections 4 and 6 (PDF4 and PDF7): first experiment 35 recruited, **29 analyzed**; second has **30 new participants**. Short-story prompting with baseline versus time (press-and-hold) or motor (pump-slider) costs for short prompts; psychological ownership is a four-item reported feeling, not a legal measure.
- **Result:** sections 4.5/6.1/7: techniques increase prompt length and psychological ownership over baseline in the tested tasks. Sections 6.2-6.3, PDF8-9: adding suggestions increases prompt length further, **without a further significant ownership gain** versus no suggestions. Different contrasts must not be collapsed.
- **Limit:** section 7.1, PDF9-10: baseline always first; familiarity/order effects possible; brief task and particular suggestions display. Mental effort associations do not prove a single mechanism. No legal rights, design-quality or longitudinal-agency result.
- **Transfer:** prompt length cannot certify authorship, permission or copyright. Friction may burden accessibility/urgency; test rather than prescribe it.

### G / documentation proposal / slides 16-17

Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daume III and Kate Crawford. **Datasheets for Datasets**. Consulted arXiv v8, 1 December 2021, 18 pages: https://arxiv.org/abs/1803.09010v8 ; https://arxiv.org/pdf/1803.09010v8 . Direct PDF 200; primary full text, not a causal intervention study.

Sections 1.1-3, PDF2-12: questions on motivation, composition, collection, processing, uses, distribution and maintenance, developed iteratively using example datasheets and feedback. We adapt selected questions, not require a complete datasheet or imply documentation guarantees harmlessness. A proposed transparency/accountability practice is not measured universal risk elimination.

### U / official U.S. copyrightability report / slides 21-22

U.S. Copyright Office. January 2025. **Copyright and Artificial Intelligence, Part 2: Copyrightability**. Official 52-page report retrieved directly (200): https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf . Executive Summary printed iii (PDF8) and sections II.C-F printed 11-27 support the slide.

- The report distinguishes assistive use, human-authored expression, prompts, expressive inputs and creative modification/arrangement. Its Executive Summary says prompts alone do not provide sufficient control **based on current generally available technology**; human contributions are assessed case by case. It does not grant every generated component protection because a person selected it.
- Official current index https://www.copyright.gov/ai/ rechecked 21 October 2026 via first-class `web_fetch` after direct node index returned 403. The index still links January 2025 Part 2, labels Part 3 training “Pre-publication,” and says a final version is future. Part 3 analysis is not taught here.
- These are the Office's bounded U.S. positions, not a worldwide legal rule, Hong Kong advice or an exhaustive current-law survey. Copyrightability is separate from third-party infringement/licence, ethical credit, privacy/consent and patent law. Obtain appropriate current jurisdiction-specific support before real release.
- **Omitted:** Thaler case updates, Google Books analogy, “transformative use” clearance, Udio/Suno disputes and patent claims. We do not teach unverified case status or infer lawful training/reuse from ownership feelings or prompt length.

### V / conceptual continuity / slides 25 and 27

Peter-Paul Verbeek. 2015. **Beyond Interaction: A Short Introduction to Mediation Theory**. *Interactions* 22(3), 26-31. https://doi.org/10.1145/2751314 ; established course primary reading: https://ris.utwente.nl/ws/files/6973415/p26-verbeek.pdf . Reuses the established Weeks 5/8 mediation vocabulary, not a new empirical effect claim. The exhibition guide is our fictional application of a hermeneutic relation; its alternative-account/correction interface is a hypothesis, not a proven safeguard in Verbeek.

## Historical 2025 comparison and exclusions

- Read **all 29 PDF pages** of `SD2112 - AI in Design - Week 11.pdf`. Extract retained in the QA sources directory. Visually inspected rendered **PDF13** (annotated group-chat collection interface) and **PDF14** (epistemic-network comparison; NOT test scores). Pages8-19 frame the six-hat/cognitive-presence paper;20-25 mix legal/news examples;26-28 concern poster setup and source discovery.
- Extracted all29 editable OneDrive Week11 PPTX slide texts using stdlib ZIP/XML; corresponding slide text matches the PDF at the inspected content level. No claim of pixel or notes equivalence. The Nov2025 exam, Week14 plan, Blackboard/shared-board links and four-group individual feedback rule do not become2026 instructions.
- Yu et al. is optional historical provenance only, bibliography appendix 37, not in the36-slide timed narrative. No new numeric or universal-learning claim relies on it. Historical “top performers do better / low performers remain the same” wording is not repeated; network-code differences are not a universal learning verdict. Week8 evidence audit was read for provenance but is not treated as a substitute for primary texts for the retained studies.
- PR #3 old source is a linked historical reference in the preserved plan, not a toolchain/logistics authority. No old sketch or obsolete tooling is ported. The slide14 comparison is newly authored native geometry/text, explicitly fictional and unmeasured. Current public-review asset selection is narrower than Version B; see the dated rights decision below. No full papers or generated media are added.

## Distinguishing evidence from our product example

The AI exhibition guide, its three candidate descriptions, corrected poster claim and accountability workflow are instructor-authored teaching examples. They are not observed student work, generated model outputs, product screenshots or experimentally validated interfaces. Affected people (visitors/contributors/absent communities), competing values (convenience/plurality), contestability and accountable editorial action are visible on slides, not relegated to notes. Teams adapt the argument to their own project rather than inherit a generic checklist.

## Current revision / 22 October 2026

Targeted primary recheck, not a new full-paper read: retained audit PDFs and final EuropePMC XML/PMC HTML were consulted again. Naqvi PDF4-5 methods and PDF8-9 ownership/artifact captions; Joshi v3 PDF4-9 methods/results including 0-100 composite and baseline-first design; Datasheets v8 PDF2-4 proposal/development; U.S. Part2 PDF8 Executive Summary; Verbeek PDF3-5 / printed28-30 conceptual relations. Naqvi PDF9 and Joshi PDF1 rendered and inspected; authentic Doshi figures inspected. Existing 21 October full-text/historical-review records above remain historical, not represented as fresh checks. No fresh current-law survey is claimed.

| Taught source | Current slides | Task / basis on screen before result |
|---|---|---|
|Naqvi/He/Kaur CHI2025 author copy|6-7|28 artifact interviews, 10/10/8 cohorts; thematic analysis not a skill experiment; source-adapted kayak workflow|
|Doshi/Hauser Science Advances2024 final|8-10|293 eight-sentence writers; randomized no/one/five-idea access; 600 evaluators; 1-9 novelty/usefulness and 0-100 embedding similarity|
|Gebru et al. arXiv1803.09010v8|16-17|Documentation proposal; two example datasets and iterative feedback; fictional retrieval-guide application; no safety score|
|Joshi/Vogel arXiv2507.03670v3 / GI2026|19-20|29 analyzed + 30 new; baseline/time/motor, baseline first; word count and four-item 0-100 ownership feeling; instructor example|
|U.S. Copyright Office Part2 January2025|21-22|Law/policy/public-comment analysis; instructor poster example; copyrightability distinct from reuse permission|
|Verbeek Interactions2015 author copy|25 then27|Conceptual argument; source metal-detector example, fictional guide application; not measured fairness|

Yu stays bibliography-only on37, not a newly explained experiment. The guide candidates, poster, workflow and short-prompt example are instructor illustrations, not measured data or quotations.

### Current public-review rights decision

Actual authorized distribution is a public GitHub PR and Cloudflare review, not local-only teaching. Current asset records include primary URL, exact version, source location, SHA256, modifications and distribution basis.

- Doshi & Hauser, Science Advances10 eadn5290 (2024), Fig2A crop and Fig4A top/legend assembly: final article's CC BY4.0 notice verified in retained primary XML/HTML. Licence: https://creativecommons.org/licenses/by/4.0/ . Visible attribution identifies authors/year/figure and changes. Fig2A dots are differences in ratings from human-only; bars show uncertainty. Exact bar coverage is not specified in the consulted main-text caption, so no95% claim is taught. The enlarged Fig4A top panel preserves similarity/density axes and source legend; density is not participant count. Cropping removes untaught emotional-characteristic and AI-idea comparisons, not contrary observations.
- Joshi & Vogel, GI2026 / author v3, Fig1: CC BY4.0 notice verified on primary PDF1; pixel crop only. The actual interfaces illustrate techniques, not a result graph.
- U.S. Copyright Office Part2, Executive Summary PDF8 / iii: limited original federal-government text, no third-party artwork. 17USC105 excludes U.S. government works from U.S. copyright: https://www.copyright.gov/title17/92chap1.html#105 . This is a documented basis for the review copy, not worldwide legal advice.
- Naqvi Fig1 participant artwork and Gebru/Verbeek facsimile text crops are NOT included in this public-review source set. The Naqvi notice limits server republication; author permission for this distribution is not established. Gebru/Verbeek public-copy access likewise does not establish republication rights. Their VersionB images remain untouched in the original preserved worktree, and are replaced here by attributed summaries/source adaptations and original instructor illustrations. No exception is invented to clear them.

Historical VersionB rights assessment (21 October): it proposed limited attributed classroom excerpts and deferred broader review. That assessment did not cover public PR/Cloudflare distribution and is superseded for this source set by the narrower selection above. Full papers remain private. The public-review asset selection does not authorize release to main.

### P2 correction / Fig. 1(a) authentic interface crop

Re-read retained exact arXiv2507.03670v3 PDF page position 1 (11-page PDF; version/date printed on page), including Fig. 1 caption and CC BY 4.0 notice; visually checked against the 240-dpi render. Fig. 1(a) is motor cost: pump slider; (b) is time cost: press-and-hold; (c) is AI suggestions. Slide 20 now illustrates only (a), a complete 534x538 pixel crop at `(172,664,706,1202)` from 2040x2640 render. Coordinates/hash/changes are in asset provenance. This is an interface example, not a results plot: 113 reps belongs to the pictured prompt, not a universal cost or outcome. Native caption explicitly labels Fig. 1(a) crop, motor-only, (b)/(c) omitted and full-source link. Slide 19 still carries the experiment comparisons; findings, limits, timing and slide count are unchanged. Source/native/companion notes explain omissions and full-figure access. Historical three-panel crop is retained unused; its small text does not meet the mobile actual-source legibility gate.
