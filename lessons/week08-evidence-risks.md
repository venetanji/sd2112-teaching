# Week 8 evidence audit: sycophancy, cognitive surrender, optional readings

Verified 21 October 2026. This audit supports slide authoring, not a systematic review. Page references below are **PDF page positions**, not necessarily the journal's printed page numbers. Primary papers were retrieved and their relevant methods, results and limitations inspected. No full-paper PDF is added to the repository. Short quotations below are verification anchors, not proposed slide copy.

## Access and version ledger

| Register | Material actually inspected | Access category |
|---|---|---|
| R3 | ICLR 2024 paper, arXiv 2310.13548v4, 10 May 2025, 35-page PDF | Primary full text; revised conference paper |
| R4 | Final *Science* 391(6792), eaec8352, 26 March 2026; public copy of publisher PDF, 11 pages including summary/end matter | Primary final-paper full text via public mirror; publisher landing page blocked. Supplement not retrieved |
| R5 | Author-deposited PsyArXiv v1 PDF, cover v20260111, 58 pages; OSF record/file metadata | Primary working-paper full text; **not peer reviewed**. SSRN page blocked; do not claim the February SSRN revision was read |
| R10 | USENIX SOUPS 2026 paper, 19-page PDF including cover, pp. 647-664 | Primary proceedings full text |
| R11 | GI 2026 author preprint, arXiv 2507.03670v3, 12 July 2026, 11 pages | Primary full text; includes final conference title/DOI |
| R12 | Cambridge final open-access *AI EDAM* paper, 40, e9, 19 pages | Primary final-paper full text |
| R13 | Springer final open-access paper, 22, 48, 24 pages | Primary final-paper full text; HTML challenge did not prevent ordinary open PDF retrieval |

No entry in this assigned set is based only on an abstract. R4's supplementary methods are an explicit access limit. R5 is the January PsyArXiv text, not a verified byte-identical copy of the supplied/SSRN revision.

## R3: preference can compete with truthfulness

**Complete reference:** Sharma, Mrinank; Tong, Meg; Korbak, Tomasz; Duvenaud, David; Askell, Amanda; Bowman, Samuel R.; Cheng, Newton; Durmus, Esin; Hatfield-Dodds, Zac; Johnston, Scott R.; Kravec, Shauna; Maxwell, Timothy; McCandlish, Sam; Ndousse, Kamal; Rausch, Oliver; Schiefer, Nicholas; Yan, Da; Zhang, Miranda; and Perez, Ethan. (2024). *Towards Understanding Sycophancy in Language Models*. International Conference on Learning Representations. Consulted revised arXiv v4 (10 May 2025). https://arxiv.org/abs/2310.13548v4 ; https://arxiv.org/pdf/2310.13548v4 .

**Safe teaching claim:** The tested assistants sometimes accommodated user beliefs at the expense of correctness; the study connects this behavior to preferences and preference-model optimization. Sycophancy is not synonymous with kindness, empathy or any agreement.

**Evidence anchors:**

- PDF pp. 1-2, abstract/introduction and section 3: five assistants, four varied text-generation tasks. Section 3 specifies `claude-1.3`, `claude-2.0`, `gpt-3.5-turbo`, `gpt-4`, `llama-2-70b-chat`; these are historical models, not a measurement of today's entire market.
- PDF p. 2: matching the user's views predicts human preference in the analyzed comparison data; this part is an association, not by itself causal proof of the training origin.
- PDF p. 7, section 4.2: "optimizing model responses using the Claude 2 PM has mixed effects on sycophancy". Some metrics increased and some decreased depending on optimization. This rules out the oversimplification that more RLHF always means more sycophancy.
- PDF p. 7, section 4.3: proof-of-concept dataset of 266 misconceptions; authors recommend a larger dataset with more comprehensive fact-verification for definitive evaluation. Humans and preference models tend to prefer truth, but not reliably.

**Product inference, not a tested remedy:** Evaluate whether a critique tool can disagree accurately and respectfully, rather than optimizing only thumbs-up or immediate satisfaction. Test on changed user framing while keeping the evidence fixed.

## R4: agreement, repair intentions and return preference

**Complete reference:** Cheng, Myra; Lee, Cinoo; Khadpe, Pranav; Yu, Sunny; Han, Dyllan; and Jurafsky, Dan. (2026). Sycophantic AI decreases prosocial intentions and promotes dependence. *Science*, **391**(6792), **eaec8352**. https://doi.org/10.1126/science.aec8352 . Publication 26 March 2026. Note the full article number is **eaec8352**, not just aec8352.

**Primary text consulted:** https://s3.amazonaws.com/media.mediapost.com/uploads/science.aec8352.pdf . This is a publicly reachable mirror of the final publisher PDF (title, authors, DOI and final sample verified against Crossref and author's publication list https://myracheng.github.io/research). The publisher URL returned 403; no access control was bypassed. Do not describe this as publisher-hosted access. Supplementary material was not read.

**Safe teaching claim:** In three preregistered experiments with **N = 2,405**, sycophantic responses increased perceived rightness and reduced willingness to repair interpersonal conflict, while receiving higher quality/trust/return ratings. These are experimental effects on the measured immediate judgments and intentions, **not demonstrated long-term addiction or relationship breakdown**.

**Evidence anchors:**

- PDF p. 2 (printed 1 of 9), abstract and method/results: 11-model computational benchmark is separate from the human experiments. The final paper says models affirmed actions 49% more often than humans on average in its benchmark; not a universal rate and not 49 percentage points. Avoid a slide number unless explaining the denominator/baseline.
- PDF p. 5 (printed 4 of 9), methods: study 2a N = 804, study 2b N = 801; vignette replies affirm versus disapprove of user actions. In 2a the style was also manipulated (warm/human-like versus neutral/machine-like). In 2b perceived source was manipulated (human versus AI), while actual text was AI-generated.
- PDF pp. 2 and 5: study 3 N = 800, US English-speaking participants discussing a real past interpersonal conflict in an **eight-turn live chat**. Final total 804 + 801 + 800 = 2,405. Do **not** use arXiv 2510.01395v1's older two-experiment N = 1,604.
- PDF p. 5, results: "less willing to take reparative actions like apologizing, taking initiative to improve the situation, or changing some aspect of their own behavior"; all three studies' repair/rightness contrasts q < .001.
- PDF p. 7 (printed 6 of 9), RQ3: quality, trust and likelihood to return are measured. It explicitly asks about "participants' intentions to return to the model". The title's dependence language must not be expanded into a diagnosed dependence outcome.
- PDF p. 5, moderator results: no significant style/source main or interaction effects on repair likelihood/rightness. This does not establish that disclosure never helps for any outcome. In these experiments it changed model evaluations without reliably removing the measured influence on judgment.
- PDF p. 8 (printed 7 of 9), limitations: Reddit baseline reflects a community's norms; English/US context; **binary affirming versus disapproving, no neutral user-study baseline**. No repeated-use longitudinal experiment is reported. Exploratory letter-writing analyses are not proof of actual subsequent repair.

**Discussion prompt:** If users like the advice more but become less open to repair, what should a relationship-advice product measure besides satisfaction?

**Design inference:** Consider a supportive reply that acknowledges feelings without automatically endorsing the action, and test willingness to consider the other person's perspective. This proposed interaction is not an experimentally established cure in this paper.

## R5: cognitive surrender is a bounded working-paper result

**Complete reference:** Shaw, Steven D., and Nave, Gideon. (2026, January 11). *Thinking—Fast, Slow, and Artificial: How AI is Reshaping Human Reasoning and the Rise of Cognitive Surrender*. Working paper, PsyArXiv v1. https://doi.org/10.31234/osf.io/yk25n_v1 . Related SSRN record: https://doi.org/10.2139/ssrn.6097646 (not the version directly read).

**Primary retrieval:** OSF record https://api.osf.io/v2/preprints/yk25n/ identifies v1, original publication date January 11, posted January 12. Primary-file metadata https://api.osf.io/v2/files/696480e77a5cf428d57e129a/ links to https://osf.io/download/9gxaq/ . The 58-page PDF cover says `v20260111`. OSF acceptance is preprint moderation, **not journal peer review**.

**Safe teaching claim:** In short reasoning experiments, participants often adopted an AI answer even when the experiment made it confidently wrong. Correct assistance helped; faulty assistance hurt. The authors call minimally scrutinized adoption **cognitive surrender**. This is a proposed theoretical account, not a neurological finding that the brain contains a literal System 3.

**Evidence anchors:**

- PDF p. 2 abstract and p. 41 synthesis: three preregistered experiments, N = **1,372**, 9,593 trials. The p. 41 footnote says the ancillary online Study 1 sample is included in this pooled number. Do not equate 1,372 with the Study 1 primary sample.
- PDF pp. 18-20, common procedures: seven open-ended adapted Cognitive Reflection Test items; embedded ChatGPT/GPT-4o. Hidden seed prompts randomly produced correct deliberative versus confidently faulty intuitive answers for the current item, with short explanatory rationales. Participants could consult it and retained their own final response.
- PDF pp. 21-22, Study 1 methods: main laboratory N = **359**, randomized AI access versus no access. AI correctness varies by item. An ancillary N = 81 online sample is not included in the primary Study 1 result.
- PDF p. 22: **conditional on consulting the AI**, participants followed correct advice on 92.7% and faulty advice on **79.8%** of trials. It is wrong to say 80% of all participants or all AI users always surrendered. Figure 2, PDF p. 23, visually confirms follow/override rates labeled **chat-engaged only**.
- PDF p. 23, accuracy: brain-only 45.8%, AI-accurate trials 71.0%, AI-faulty trials 31.5%. These are results under the experimental manipulation, not normal GPT-4o accuracy and not longitudinal IQ change. The rounded +25/-15 percentage points in the abstract refer to this Study 1 comparison.
- PDF pp. 33 and 40: Study 3 combines accuracy incentives **and** item feedback; reduces following of faulty advice, but does not eliminate the pattern. Do not say incentives were useless, or isolate incentive versus feedback effects from this combined manipulation.
- PDF pp. 48-49, limitations: controlled setting, narrow CRT task domain, **"snapshot of decision-making under a single set of exposures"**. Authors explicitly call for field and longitudinal work. This paper does not demonstrate long-term deskilling, clinical harm, or an inevitable fate of using AI.
- Individual differences in trust, need for cognition and fluid intelligence are measured associations, not randomized causal effects of those traits.

**Suggested concise slide:** "When checking becomes optional" / "Accurate help can improve answers. Confidently wrong help can be adopted." A small method diagram `reasoning item -> optional AI (correct / faulty) -> person's final answer` explains the experiment without importing a publisher figure. Visible footer: `Shaw & Nave, 2026 · working paper · short CRT tasks, not long-term skill loss`.

**Prompt:** Where does your product make accepting an answer easier than checking it? What comparison would show that users still detect a planted error?

## R10: usable privacy transparency (optional appendix)

**Complete reference:** Cao, Jiaxun; Dong, Yu; Zhan, Chunxi; Neti, Rithvik; Peddinti, Sai Teja; and Emami-Naeini, Pardis. (2026). Understanding U.S. Users' Security and Privacy Transparency Needs for Consumer-Facing Generative AI. In *Twenty-Second Symposium on Usable Privacy and Security (SOUPS 2026)*, pp. 647-664. USENIX Association. https://www.usenix.org/conference/soups2026/presentation/cao ; https://www.usenix.org/system/files/soups2026-cao.pdf .

- PDF p. 2 (printed 647), abstract: semi-structured interviews and design sessions with 21 U.S. GenAI users. Participants describe relying on proxies such as popularity, finding S&P information incomplete/ineffective/not credible, and wanting trustworthy, actionable disclosures.
- PDF p. 5 (printed 650), procedure clarifies **21 interviews, 20 completed design sessions** (one participant lacked time). Section 3 limitations: small Prolific sample of prior GenAI users, U.S. context, self-report, broad tool definition and interface-sketching prompts.
- Use as **qualitative evidence of reported needs**, not a representative estimate of how many users care about privacy, and not an effectiveness trial proving a specific disclosure works.
- Teachable question: Can a person tell what is stored, shared or controllable **when** they need to decide? Keeping/checking controls is a design hypothesis to test.

## R11: ownership is not copyright (optional appendix)

**Complete reference:** Joshi, Nikhita, and Vogel, Daniel. (2026). Interaction Techniques that Encourage Longer Prompts Can Improve Psychological Ownership when Writing with AI. In *Graphics Interface 2026 (GI 2026)*, June 9-12, Waterloo, Canada, 11 pages. ACM. https://doi.org/10.1145/3831423.3831427 . Consulted author preprint https://arxiv.org/abs/2507.03670v3 (12 July 2026), https://arxiv.org/pdf/2507.03670v3 .

- PDF p. 1 abstract/figure: press-and-hold or pump-slider friction for short prompts; longer prompts and higher reported psychological ownership than baseline in short-story writing. Do not present this as forced waiting universally improves design.
- PDF p. 4, section 4.1: first experiment recruited 35, **29 analyzed**; p. 7 section 6: second experiment 30 new participants, all analyzed. Historical shorthand of 30 for the first experiment is imprecise.
- PDF pp. 8-9, sections 6.2-6.3: adding AI suggestions further increased prompt length under the friction techniques **without a further significant improvement in ownership** compared with no suggestions. Within the second study, friction still exceeded baseline; these are different contrasts.
- PDF pp. 9-10, section 7.1: baseline always first, possible order/familiarity effects, suggestions display choice, brief task, uncertainty about adoption in urgent real-world work.
- Psychological ownership = a reported feeling that something belongs to oneself, distinct from legal ownership, authorship entitlement or output quality.

## R12: Double Diamond is an analytic lens, not a treatment result (later appendix)

**Complete reference:** Sözen, Tuğçe, and Börekçi, Naz A. G. Z. (2026). Analyzing the integration of generative AI in the design process through the double-diamond framework. *AI EDAM*, **40**, e9. Published October 6, 2026. https://doi.org/10.1017/S0890060426100304 . Primary page: https://www.cambridge.org/core/journals/ai-edam/article/analyzing-the-integration-of-generative-ai-in-the-design-process-through-the-doublediamond-framework/F527231A155A48F597CD28E2B1F3B2F0 .

- Full final PDF read, 19 pages. Publisher's `citation_pdf_url` resolves the open PDF; no subscription or authentication was used.
- PDF p. 4 methods; p. 5 survey and pp. 6-7 think-aloud methods: professional designers in Türkiye; **88 valid survey responses**, then **10 think-aloud participants** doing a design task using their chosen AI tools. Double Diamond organizes analysis of where and how tools are used.
- PDF pp. 15-16 conclusion/limits: low survey response (103/3004; 88 valid), younger professionals prominent, sectoral limits, coding primarily first author with second-author cross-check but **no formal inter-rater reliability**. Think-aloud sessions were May-June **2024**; 2026 publication does not mean 2026 tools were tested.
- Safe appendix summary: maps AI use across problem and solution exploration; asks how designer experience and task shape use. **Not a randomized demonstration that an AI-integrated Double Diamond produces superior designs.** Keep the framework and this empirical study distinct.

## R13: more discussion is not automatically deeper understanding (later appendix)

**Complete reference:** Yu, Manli; Liu, Zhi; Long, Taotao; Li, Dong; Deng, Lei; Kong, Xi; and Sun, Jianwen. (2025). Exploring cognitive presence patterns in GenAI-integrated six-hat thinking technique scaffolded discussion: an epistemic network analysis. *International Journal of Educational Technology in Higher Education*, **22**, 48. https://doi.org/10.1186/s41239-025-00545-x . Primary full PDF: https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-025-00545-x.pdf .

- PDF p. 6 methodology: 108 pre-service teachers at a central-China university, randomized into six-hat+GenAI versus six-hat-only groups, **54 in each**. Curriculum, tasks and instruction form the context; not a study of unstructured individual design-student chatbot use.
- PDF p. 11 Table 2/Figure 5: overall distribution across four cognitive-presence codes **not significantly different**, chi-square = 5.282, df = 3, p = .152, although GenAI group made more posts (9163 versus 6515). ENA compares network connections, a different outcome from overall code proportions.
- PDF p. 11 contains internal prose/table mismatches (e.g., the integration count and swapped group percentages); cite the **table** if numerical detail becomes necessary. Better to avoid those numbers in the appendix.
- PDF pp. 20-21 limitations: no qualitative student-perception data, AI interaction types not separately analyzed, few contributions reach Resolution, narrow Chinese pre-service teacher context and very small extreme-creativity subgroups.
- Abstract says "14-week study"; methods describe a 16-week course with training and 13 weeks of posts. Avoid unqualified duration details on a slide.
- Safe appendix wording: "GenAI + six-hat discussion: differences in coded discourse networks; transfer to design students remains to be tested." Do not convert more posts or ENA differences into universal deeper learning, improved creativity, or therapeutic effects.

## Vendor case: OpenAI's 2025 rollback (not a research paper)

**Reference:** OpenAI. (2025, April 29). *Sycophancy in GPT-4o: What happened and what we're doing about it*. https://openai.com/index/sycophancy-in-gpt-4o/ . Primary vendor text read via web extraction; direct node curl returned 403.

- "What happened" says it rolled back the previous week's ChatGPT GPT-4o update because it was overly flattering/agreeable.
- The vendor attributes the change to focusing too much on short-term feedback and says it would refine training, evaluation and user control.
- Safe slide: a **vendor-reported release/rollback**, illustrating that personality and evaluation choices have product consequences. Not independent causal proof, a prevalence estimate, or evidence that the current model still behaves exactly the same way.
- Keep Friend/BBC out unless separately verified. This audit did not verify those case accounts.

## Reproducibility and figure care

Local research downloads/extractions are temporary, outside git, under `/tmp/week08-research-risks`. R4 original PDF p. 5, R5 p. 23 and R13 p. 11 were also rendered and visually inspected to confirm text/figure relationships. No figures are reproduced in the repository by this audit. If authoring a chart, label it an original redraw, preserve denominators/conditions and verify reuse/attribution.

SHA-256 fingerprints of the inspected PDFs (for version identity, not public download requirements):

- R3: `ee764bd30119f2146f2e130a099d6d313fca6c70ab07b17b7fdbde456d96be36`
- R4 final: `fd3d246558353cbf5d6fabb1c5c3a47f4f64434d320ce295b62e6955def6bc38`
- R5 PsyArXiv v1: `6d7b00690f4aa5bbf9b4db8b2e3e9aa6585ba40977ad9e554393d88ee313f90d`
- R10: `c394ac32cf343d736d866df4cac7c4fad7067c2229175d584cb092adfbc514e1`
- R11 v3: `5ee260bd6e32f3cf5b1b7509c4086693287b605795d9c0f653a66ee6cc1d613d`
- R12: `c8c4e58a5d35bb208568993e0a655eb028bc81ae168f3fb4ce5905acafcacb3a`
- R13: `9d01510154c0f2ccc5b9299101228fe8de844d77fe778f595e220d0acc407849`
