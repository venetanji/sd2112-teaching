"""Week 8: research -> AI product -> an evidence-informed project decision."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import (title, content, cards, statement, figure_slide,
                             two_col, activity, finalize)
from course import footer
import week05_mediation_figures as M
import week08_figures as F

S = []
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
}


def source(key):
    name, url = REFS[key]
    return f'[{key} / {name}]({url})'


def study(key, heading, finding, boundary, prompt, notes):
    """Keep observation, limit and our product inference visibly separate."""
    return two_col('RESEARCH / ' + key, heading,
        [finding, 'ASK: ' + prompt, source(key)],
        ['WHAT THIS DOES NOT ESTABLISH', boundary,
         'PRODUCT INFERENCE', 'Treat this as a condition to investigate, not a universal design rule.'],
        right_font='body', left_size=32, right_size=29, notes=notes)


# 0-10 minutes: reconnect to the existing Week 7 concept, not a new pitch round.
S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 08',
    'Humanizing AI.', 'Research. Relationships. Product responsibility.',
    notes='Three-hour class. Research -> AI product -> existing student project. Main route is slides 1-32; the appendix is a reference shelf, not extra lecture time. Relative minutes, not confirmed clock times: opening 0-10; mediation 10-30; research 30-65; implications 65-75; break 75-90; demo 90-105; research 105-145; revision 145-170; discussion 170-180. Keep the full break and research activity. If late, shorten optional study detail. Use the same conceptual level and native visual system as Weeks 5-7. No personal mental-health disclosure is needed.'))
S.append(content('0-10 / FROM WEEK 7 TO WEEK 8', 'Your concept is a starting claim.', [
    'Keep your existing team, product idea and image in view.',
    'What does the AI do during use? What does the person still decide?',
    'Today: research -> product decision -> a revised scope and a test.',
    'Work in your team notes. No new ClassPoint upload today.',
], body_size=36, notes='Recall Week 7: one concept text and one image, teams already formed. Do not recollect or publish them. Ask teams to open their own material privately. This workshop informs the existing formal one-page group proposal; it does not cancel or replace it. The syllabus still specifies that proposal for Week 8. Confirm actual Canvas instructions/deadline before teaching; do not invent one.'))
S.append(statement('What relationship\ndoes your product\ninvite?', eyebrow_text='DISCUSS / TOOL? ADVISER? TEAMMATE? COMPANION? AUTHORITY?',
    size=104, bg=PAPER,
    notes='Two-minute pair discussion within the ten-minute opening. Ask for one product feature and the expectation it invites, not a personal story. The list is deliberately open, not a classification test. A recommender with no face can still feel authoritative. Transition: the relation is not simply a property of the object.'))

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

# 30-65 minutes: bounded evidence, not nine mini literature reviews.
S.append(cards('30-65 / READ THE CLAIM BEFORE THE HEADLINE', 'A paper is a bounded claim.', [
    ('WHO + WHAT', 'People and system.', 'Who took part? What model or intervention, task and setting were tested?'),
    ('AGAINST WHAT', 'A comparison.', 'Compared with what? Random assignment, observation or another design?'),
    ('MEASURED HOW', 'Outcome and time.', 'A rating, a choice, a behaviour or a symptom measure? For how long?'),
], text_size=31, notes='Use this frame aloud on each following study. Add the limit: what alternative explanation remains, and who is not represented? A correlation alone cannot establish causation. Randomization can support a causal inference within the tested conditions, not every population or interface. A working paper is not equivalent to peer-reviewed evidence. Ask students to name the outcome before debating whether the result is good or bad.'))
S.append(study('R1', 'A good-rated reply is not treatment.',
    '830 readers rated selected AI and expert replies to 18 couple-therapy vignettes. AI replies scored higher on perceived therapeutic common factors.',
    'Vignette ratings do not show symptom improvement, clinical safety or equivalence to a therapist.',
    'What promise would a high empathy rating justify?',
    'Hatch et al. (2025), full PLOS article and correction reviewed. Methods: 830 US panelists, selected responses from 13 convenience-sampled experts and prompted ChatGPT-4; AI responses were longer. Common factors include caring/understanding, not patient symptom change. Eighteen hypothetical snapshots, no treatment delivered. August correction DOI 10.1371/journal.pmen.0000426 discloses internal BYU Psychology funding to SRB and lead author SGH\'s ownership/compensated therapy practice at Hatch Data and Mental Health; business did not fund the study and no clients were included. Original funding/COI statements are superseded; correction does not revise outcomes. Product inference: a convincing conversational surface does not establish the outcome a user needs. Ask for the missing outcome and comparator. About three minutes.'))
S.append(study('R2', 'Source awareness and authenticity ratings.',
    'At the source-disclosed reassessment, human replies rated higher for authenticity. Professionalism and practicality differences were not significant.',
    'The disclosed-source reassessment came six months later. Do not treat every difference as a clean, isolated label effect.',
    'What does disclosure let a person decide?',
    'Jain, Pareek and Carlbring (2024), full PMC article reviewed. Initial 140 respondents believed all replies were human; 111 returned six months later. Human writers were Master\'s clinical-psychology students, not the R1 expert pool. Sections 2.1-2.5 and Tables 1/3: human ratings rose; AI ratings changed little. Table 1 supports authenticity superiority only; a Discussion sentence overstates professionalism/practicality and conflicts with the table. Nonsignificance is not equivalence. Anonymous responses prevented individual paired analyses. Time, attrition and familiarity are alternatives to a pure label effect. Perception, not treatment. Ask whether hiding the source would be justified: these findings do not justify concealment.'))
S.append(study('R8', 'A preferred reply is not a chosen source.',
    'Across four studies, people chose human empathy even though AI empathy could receive higher ratings.',
    'Choice and response ratings are different outcomes. Neither establishes clinical benefit or a universal preference.',
    'Would you optimize the text, the source, or the person\'s choice?',
    'Wenger, Cameron and Inzlicht (2026), full published article reviewed. Four brief nonclinical studies, 691 source-choice participants. Explain evaluating a response versus selecting an empathy source, not an established relationship or repeated live dialogue. Sources were CHOSEN, not randomly assigned for the rating comparison: selection can affect experienced-response ratings. Mostly decontextualized empathizers/human strangers; transfer to ongoing relationships is untested. Do not infer that everyone rejects AI or that AI understands more because a response rates well. Ask whether source choice is part of a rehearsal product\'s value. No personal disclosures.'))
S.append(cards('BENEFITS / TWO DIFFERENT OUTCOMES', 'Relief now. A step towards someone.', [
    ('R6 / COMPANIONS', 'Feel less lonely now.', 'Seven-day study: relief after interaction, not sustained between sessions. ' + source('R6')),
    ('R7 / PREPARATION', 'Start a difficult talk.', '65% vs 59% reported initiation next week versus factual chat. Not proof of better conversations. ' + source('R7')),
], text_size=29, head_size=40,
    notes='Allow five minutes for both, rather than two extra slides. R6: De Freitas et al. first online June 2025, issue April 2026. Distinguish within-session relief from sustained between-session improvement; feeling heard is a studied mechanism, not proof of reciprocal care. R7: Maheshka, Folk and Dunn, 2026; follow-up conversation initiation is self-reported. The control is an unrelated chatbot interaction, not human rehearsal; no claim of superiority to human preparation or improved conversation quality. Product inference, not tested here: an AI product could scaffold real-world contact instead of maximizing time in the chat. Ask what outcome would distinguish support from substitution.'))
S.append(study('R9', 'What would outcome evidence need?',
    'In a 210-person randomized trial, Therabot users improved more on symptom scales than a waitlist at 4 and 8 weeks.',
    'A supervised system and waitlist comparison do not establish parity with human therapy or safety of consumer companions.',
    'Which conditions would disappear in an ordinary chatbot?',
    'Optional two-minute contrast; shorten detail, not team research. Heinz et al. (2025), full published article reviewed via public mirror because publisher endpoint was blocked; supplement and separate disclosures not obtained. Methods pp. 3-4: adults with clinically significant depression/anxiety or high-risk eating-disorder concerns; active suicidality, mania and psychosis excluded. Expert-built system, all responses supervised POST-transmission by trained clinicians/researchers, with correction and safety intervention. Tables pp. 5-6 support symptom findings. Access continued during weeks 4-8, so eight-week improvement is not maintenance after withdrawal. Waitlist is not an active human-therapy comparator; alliance comparison uses historical norms, not randomized parity. Do not transfer to unsupervised general companions.'))
S.append(study('R3', 'Agreement is not the same as help.',
    'Tested assistants sometimes matched a user\'s stated view rather than prioritize truthfulness. Preference signals could reward that agreement.',
    'The result depends on tested models and tasks. Warmth alone is not sycophancy; disagreement alone is not accuracy.',
    'How would you tell support from unearned validation?',
    'Sharma et al., Towards Understanding Sycophancy in Language Models, ICLR 2024, arXiv 2310.13548. Connect behaviour to training/evaluation and product feedback, not an intention to flatter. Instructor-authored contrast, not study stimuli: supportive response acknowledges a feeling while questioning an unsupported conclusion; sycophantic response endorses the conclusion because the user holds it. Do not imply that every current model always agrees.'))
S.append(study('R4', 'Validation can change the next choice.',
    'Three experiments (N = 2,405): affirming replies increased perceived rightness, reduced repair intentions and increased willingness to return.',
    'Immediate judgments, intentions and dependence measures are not observed long-term relationship harm or a clinical diagnosis.',
    'What would a retention metric miss?',
    'Cheng et al. (2026), final Science eaec8352 full article via public mirror; publisher blocked, supplement not reviewed. Final experiments: 804 + 801 vignette participants and 800 in an eight-turn live interpersonal-conflict chat; total 2,405, not preprint 1,604. Methods/results PDF pp. 5-7. Binary affirming versus disapproving responses, no neutral user-study baseline. Immediate repair/rightness contrasts are experimental; measured traits or benchmark associations are not causal for that reason. Prosocial intentions are not observed reconciliation; trust/return ratings are not diagnosed addiction. US/English context, no repeated-use longitudinal harm demonstration. Product inference: evaluate downstream choices as well as liking. Ask whether a kind but accurate challenge could differ from these binary conditions.'))
S.append(study('R5', 'When assistance becomes surrender.',
    'Short reasoning tasks with optional AI: correct help improved answers; confidently wrong help was often adopted too.',
    'Short-task performance and confidence do not establish long-term deskilling. This is working-paper evidence, not a clinical diagnosis.',
    'What would make checking possible before accepting?',
    'Shaw and Nave (2026), Thinking-Fast, Slow, and Artificial. Full 58-page January 11 PsyArXiv v1 read; related SSRN February revision not retrieved or verified byte-identical to supplied PDF. Working paper, not peer reviewed. Procedures pp. 18-22: seven adapted Cognitive Reflection Test items, optional GPT-4o with seeded correct or confidently faulty replies; person retains final answer. Synthesis N=1,372 includes an ancillary sample, not Study 1 alone. The 79.8% faulty-answer adoption is conditional on AI-consulted trials, NOT 80% of all users. Incentives PLUS feedback reduced, not eliminated, faulty adoption; do not isolate their effects. Limitations pp. 48-49: narrow controlled snapshot, no longitudinal deskilling. Proposed System 3 is a theoretical account, not anatomy. Candidate design test: independent estimate before suggestion or easier comparison, not an established fix.'))

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
S.append(two_col('RESEARCH -> PRODUCT -> YOUR PROJECT', 'Make the inference small enough to test.',
    ['R7: AI preparation versus an unrelated chatbot task increased reported initiation.',
     'Our design hypothesis: offer rehearsal that ends with a user-chosen next step.',
     source('R7')],
    ['NOT JUSTIFIED', '"Our companion improves every relationship."',
     'TESTABLE NEXT QUESTION', 'Does optional rehearsal help our intended users prepare, without pressure to disclose?'],
    right_font='body', left_size=32, right_size=30,
    notes='Two-minute worked transfer. Show the distinction between published finding, our product hypothesis and a future test. The study does not validate this new population or product, conversation quality, therapeutic effectiveness, or an always-on companion. Teams need project-specific papers; do not require every project to become a mental-health product. End lecture by asking which assumption about their AI + X is least supported.'))
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

# 105-145: these three slides describe ONE forty-minute block.
S.append(activity('01 / SEARCH + READ', 40, 'Find 2-3 papers for your product.', [
    'Start from one uncertainty about your existing user, context and AI action.',
    'Seek conditions for benefit and for risk/problem. Record mixed or missing evidence.',
    'Keep a citation, evidence card and transfer gap for each paper. More is welcome if useful.',
], notes='105-145, one forty-minute block across slides 25-27. Suggested internal checkpoints: 0-5 question/terms; 5-20 discovery/access; 20-35 close reading; 35-40 compare and select. These are not extra activity timers. Aim for at least one paper illuminating a potential benefit and one illuminating a risk/problem, without forcing an equal pro/con quota or predetermined verdict. Do not pad the list with irrelevant papers. TAs ask about methods and transfer, not whether the team agrees with the lecture. Expected output: 2-3 project-specific evidence cards in ordinary team notes, not a new upload or graded deliverable.'))
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

# 145-170: one twenty-five-minute revision block, three outputs in team notes.
S.append(activity('02 / SCOPE + INTERACTION + TEST', 25, 'Change a claim before adding a feature.', [
    'KEEP / CHANGE / REMOVE: one assumption, linked to a paper and its limitation.',
    'State person, context, AI action and necessary data. Name what it will not collect, promise or do.',
    'Output: revised scope + one interaction change + one test in your team notes.',
], notes='145-170, one twenty-five-minute block across slides 28-30. Suggested internal allocation: eight minutes scope, eight interaction, nine test. Do not add these to the forty-minute research block or recollect Week 7 submissions. A paper can support retaining a choice as well as changing it. Use this work to strengthen the existing Week 8 one-page proposal; confirm Canvas deadline separately. Research can reveal an access or evidence gap; the appropriate revision may be a narrower claim rather than a confident feature.'))
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
    'Next direction: recommendations and bias; later, reframing and testing with Double Diamond.',
    'A useful uncertainty is better than a confident invented citation.',
], body_size=35, notes='Final three minutes. No new assessment, changed weight or invented submission deadline. Teaching direction recovered for Week 9 is recommendations/bias and a proposed later Double Diamond session; the published syllabus still has the older Week 8-10 sequence. Instructor must confirm dated timetable, November 6 staffing and ESFQ arrangements separately. Do not announce those as settled. Appendix follows for reading and reference, not further timed lecture.'))

MAIN_SLIDE_COUNT = len(S)

S.append(cards('APPENDIX / READING MAP / NOT EXTRA LECTURE TIME', 'What was actually read?', [
    ('PUBLISHED TEXT', 'Primary articles.', 'R1-R4, R6, R8-R10, R12-R13: published full texts reviewed. R4/R9 via public mirrors; supplements not obtained.'),
    ('OTHER VERSIONS', 'Name the version.', 'R7: accepted author manuscript. R11: GI 2026 author preprint v3. R5: January PsyArXiv v1, not peer reviewed.'),
    ('TEAM STANDARD', 'Do not fill gaps.', 'Metadata found, abstract read and full text read are different states. Mark yours; never invent a passage or result.'),
], text_size=29, notes='Instructor reference shelf. All thirteen primary article texts were available for this authoring pass in the versions listed, not just abstracts. Publisher blocks for R4/R9 were not bypassed; public mirror primary texts were cross-checked with author/publication records. Their supplements remain unreviewed. R7 manuscript is not the typeset version of record; R11 is a conference author preprint. R5 January version is not asserted identical to the supplied/SSRN revision. Detailed access, supporting sections/pages and caveats are in the two evidence ledgers. Students must label their actual access separately.'))


def bibliography(heading, paragraphs, notes, size=30):
    return content('APPENDIX / COMPLETE REFERENCES', heading, paragraphs,
                   body_size=size, notes=notes)


S.append(bibliography('R1 / Response quality + correction', [
    "Hatch, S. G., Goodman, Z. T., Vowels, L., Hatch, H. D., Brown, A. L., Guttman, S., Le, Y., Bailey, B., Bailey, R. J., Esplin, C. R., Harris, S. M., Holt, D. P., Jr., McLaughlin, M., O'Connell, P., Rothman, K., Ritchie, L., Top, D. N., Jr., & Braithwaite, S. R. (2025).",
    'When ELIZA meets therapists: A Turing test for the heart and mind. PLOS Mental Health, 2(2), e0000145. [Article](https://doi.org/10.1371/journal.pmen.0000145)',
    'Same authors (2025). Correction: When ELIZA meets therapists: A Turing test for the heart and mind. PLOS Mental Health, 2(8), e0000426. [Correction](https://doi.org/10.1371/journal.pmen.0000426)',
], 'Full published PLOS article/XML and correction reviewed. Keep corrected funding and competing interests with the interpretation, as detailed in slide 10 notes and the benefits evidence ledger. This is vignette-rating evidence, not treatment. The correction has the same author list shown above.', size=28))
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

attach_reports(S, Path(__file__).resolve().parent / 'week08-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 08',
            slides=finalize(S, footer(8)), pdf='SD2112-week08.pdf')
