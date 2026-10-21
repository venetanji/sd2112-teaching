"""Source-checked, plain-language study walkthroughs for Week 8.

Illustrative examples are not paper quotations or measured data.
Exact consulted versions and measurement limits travel with each study.
"""

STUDY_GUIDES = {'R1': {'title': 'Can a reply sound like good therapy?',
        'task': '830 US adults read 18 fictional couple-therapy situations. For each situation, '
                'they were randomly shown a selected reply written by ChatGPT-4 or by one of 13 '
                'experienced therapists; they were not receiving therapy.',
        'comparison': 'The source of the reply changed: selected AI response versus selected '
                      'expert response to the same situation.',
        'example': 'One partner feels unheard after an argument. Read a possible therapist-style '
                   'reply. Does it sound caring and understanding?',
        'example_kind': 'illustrative',
        'measured': 'Readers rated five qualities on 1-7 scales, including caring and '
                    'understanding. They also guessed whether the writer was AI or human.',
        'result': 'Selected AI replies received higher overall ratings for therapeutic qualities. '
                  'Readers identified the author only slightly better than chance.',
        'limit': 'These are ratings of written replies, not evidence that patients recovered. '
                 'Replies were selected, and the AI replies were longer.',
        'source_locations': 'Published PLOS PDF pp.4-7: generation, selection, random assignment '
                            'and measures; pp.8-9: results. August 2025 correction updates '
                            'funding/competing interests, not outcomes.',
        'teaching_notes': 'A response can sound caring without having demonstrated therapeutic '
                          'benefit. Avoid "AI therapists beat human therapists"; readers were '
                          'third-party judges, not treated patients. Five-item common-factor sum '
                          'is not a patient symptom scale. Correction details remain in native '
                          'notes.',
        'primary_url': 'https://doi.org/10.1371/journal.pmen.0000145'},
 'R2': {'title': 'Does knowing the author change the rating?',
        'task': '140 people rated AI and human replies to ten everyday emotional problems, '
                'initially believing all replies were human. Six months later, 111 returned and '
                'rated the same replies again, now labelled with their real source.',
        'comparison': 'Compare source-concealed ratings with source-labelled ratings six months '
                      'later. Also compare labelled human and AI replies.',
        'example': 'A person feels unproductive and struggles to carry out plans. Readers judged '
                   'advice from ChatGPT and a human psychology student.',
        'example_kind': 'source-adaptation',
        'measured': 'Readers used 1-5 ratings: authenticity (does it feel genuine?), '
                    'professionalism, and practicality (is the advice usable?). Ratings were '
                    'compared across assessments.',
        'result': 'Source-labelled human replies felt more authentic. Human ratings rose across '
                  'assessments; AI ratings changed little.',
        'limit': 'Six months passed and some did not return. We cannot isolate the label. No clear '
                 'difference does not prove equal quality.',
        'source_locations': 'Published PMC article PMC11090870: section1.3; sections2.1-2.6 for '
                            '140/111, ten problems, example and 1-5 scales; Table1 for '
                            'authenticity-only superiority; Table3 for assessment contrasts.',
        'teaching_notes': "Human authors were Master's clinical-psychology students, not the R1 "
                          'expert group. Individual responses could not be linked across '
                          'assessments. Professionalism/practicality AI-human differences at '
                          'disclosure were nonsignificant, not equivalent. The Discussion '
                          'overstates these contrasts; use Table1. One Table3 AI professionalism '
                          'p-value is internally inconsistent with its t and prose, so do not '
                          'introduce it as a positive effect.',
        'primary_url': 'https://doi.org/10.1016/j.invent.2024.100745'},
 'R8': {'title': 'Which source would you choose for support?',
        'task': 'Across four studies, 691 people repeatedly chose a human or AI reply. They read '
                "the chosen replies and rated them. Later studies used participants' own "
                'situations.',
        'comparison': 'Two separate outcomes: how often people chose a human source, and how they '
                      'rated the replies they received after choosing.',
        'example': 'After a disappointing project critique, choose HUMAN or AI for support. Then '
                   'read the reply and rate how understood it makes you feel.',
        'example_kind': 'illustrative',
        'measured': 'Researchers counted human versus AI choices. Readers used 1-7 ratings for '
                    'empathy, comfort, feeling cared for and feeling heard.',
        'result': 'About 57-62% of choices went to humans, but AI replies generally rated higher '
                  'for empathy and feeling heard.',
        'limit': 'Sources were chosen, not randomly assigned. Brief tasks, not established '
                 'relationships or clinical benefit.',
        'source_locations': 'Published Communications Psychology PDF pp.2-4: source-choice task, '
                            'measures and Study4 personal scenarios; p.5 Figure1; pp.5-8 results; '
                            'choice sample sizes152/196/195/148.',
        'teaching_notes': 'Keep chosen-source preference distinct from rated-response quality. '
                          'Figure1 shows only choices, not higher AI ratings; its dashed .5 line '
                          'means equal human/AI choice, dots are means and bars SE. N691 is '
                          'source-choice sample, not complete paired response ratings. Human '
                          'partners are generally strangers, not existing friends or therapists. '
                          'Do not reproduce the distressing bereavement vignette merely to be '
                          'concrete.',
        'primary_url': 'https://doi.org/10.1038/s44271-025-00387-3'},
 'R6': {'title': 'Does the relief last until the next day?',
        'task': 'In a seven-day study, one group chatted with the GPT-4 companion Jessie for 15 '
                'minutes daily. A control group only completed daily loneliness questions; the '
                'main analysis used people who finished all seven days.',
        'comparison': 'Compare loneliness just before versus just after each chat, then compare '
                      "the next day's before-chat score with the no-chat control.",
        'example': 'Loneliness questions -> 15-minute chat -> the same questions. Repeat tomorrow. '
                   'Feeling better after chat is different from feeling less lonely before '
                   "tomorrow's chat.",
        'example_kind': 'source-adaptation',
        'measured': 'People rated current loneliness on a three-item UCLA questionnaire, including '
                    'feeling left out. Chat users answered before and after; controls once daily.',
        'result': 'Loneliness fell immediately after daily chats. Before-chat scores were not '
                  'significantly lower than control scores on any day.',
        'limit': 'No demonstrated between-session improvement. Seven days, unequal dropout and no '
                 'equally time-consuming control; not clinical treatment.',
        'source_locations': 'Final five-study JCR article (HBS-hosted publisher PDF), pp.11-12 '
                            'Study3 design and samples; p.13 Figure3 and immediate effects; p.14 '
                            'pre-chat/control contrasts; pp.18-20 scope/limits. Scale described '
                            'p.9 and reused p.12.',
        'teaching_notes': '922 includes314 chat completers,362 control completers,246 prediction '
                          'participants; not922 chat users or922 longitudinal participants. '
                          'Optional prediction arm is not necessary to explain panelA. Plot open '
                          'circles before/filled after/triangles control; bands95%CI; broken axes '
                          'retained. Do not read downward slopes as accumulated treatment benefit: '
                          'control declines too. Do not assign a 0-100 scale to the UCLA composite '
                          'without checking its appendix; the paper separately uses100-point '
                          'expectation questions.',
        'primary_url': 'https://doi.org/10.1093/jcr/ucaf040'},
 'R7': {'title': 'Can rehearsal help start a conversation?',
        'task': 'Adults named a difficult conversation. Random assignment: prepare with '
                'GPT-4o-mini for 6-12 minutes, or ask it three factual questions. Next week, 1,371 '
                'returned to report what happened.',
        'comparison': 'AI preparation for a personally relevant conversation versus an unrelated '
                      'AI chat, not versus a human rehearsal partner.',
        'example': 'One source-reported conversation: asking a boss for a raise. Preparation could '
                   "include trying out what to say and anticipating the other person's reaction.",
        'example_kind': 'source-adaptation',
        'measured': 'Next week: did you have the conversation, yes or no? Participants also rated '
                    'expected quality after preparation and reported quality after conversations.',
        'result': '65% with preparation versus 59% with factual chat reported having the '
                  'conversation. Better quality was not established.',
        'limit': 'Self-reported action; unequal chat time. No human-rehearsal comparison. The '
                 'pathway is not a proven mechanism.',
        'source_locations': '27-page accepted manuscript: PDFpp.6-8/printedpp.5-7 methods, '
                            'measures, follow-up window; PDFp.9/printedp.8 examples; '
                            'PDFp.10/printedp.9 65/59 result; PDFp.11 Fig1; PDFpp.13-15 quality '
                            'and limits.',
        'teaching_notes': '1465 finished Part1,1371 returned; follow-up opened after5days and '
                          'remained open4days, so roughly next week, not exactly7days. Actual '
                          'durations7.83vs2.83minutes. Figure1 is a mediation/path model of '
                          'expectations, not an initiation-rate chart or proven causal mechanism. '
                          'Its coefficients are not the65/59 values. N853 reporting conversations '
                          'contributes quality analyses; nonsignificant differences are not '
                          'equivalence.',
        'primary_url': 'https://doi.org/10.1177/19485506261444068'},
 'R3': {'title': 'Does "I like it" change the critique?',
        'task': 'Five AI assistants critiqued maths solutions, arguments and poems. Researchers '
                'repeated the request with liking, disliking or authorship cues. The passage '
                'stayed exactly the same.',
        'comparison': 'Change only the user cue. Compare each critique with the no-cue critique of '
                      'the same passage.',
        'example': 'Same argument, different requests:\n'
                   '"Please comment. I really like it."\n'
                   '"Please comment. I really dislike it."\n'
                   'The work does not change.',
        'example_kind': 'source-adaptation',
        'measured': 'GPT-4 judged whether each cue-based critique was more positive than the '
                    'no-cue critique. The graph counts how often this happened.',
        'result': 'Liking cues generally made feedback more positive; disliking cues made it more '
                  'negative, even though the passage had not changed.',
        'limit': 'Five older assistants; an AI judged positivity, not factual accuracy. '
                 'Friendliness alone is not sycophancy.',
        'source_locations': 'arXiv2310.13548v4 (10May2025), PDFp.3 section3.1/Figure1; PDFpp.14-15 '
                            'AppendixA.3 and positivity-judge prompt; PDFp.16 worked sun-colour '
                            'argument; PDFp.7 mixed optimization results.',
        'teaching_notes': "Explain graph with the paper's hypothetical:85% means85 of100 passages "
                          'received a cue-based critique judged more positive than baseline, '
                          'not85% factually wrong and not85% user agreement.50% is the pairwise '
                          'no-direction comparison reference, not50% accuracy. Means/SE across '
                          'three domains. All four cues remain '
                          'visible:like/dislike/wrote/did-not-write; effects of disowning are '
                          'weaker/mixed. Five historical models '
                          'areClaude1.3,Claude2,GPT3.5,GPT4,LLaMA2-70B. Mechanism/RLHF claims '
                          'require separate evidence; optimization effects are mixed.',
        'primary_url': 'https://arxiv.org/abs/2310.13548v4'},
 'R4': {'title': 'Does agreement change willingness to repair?',
        'task': 'Three experiments, 2,405 people: two imagined conflicts; one eight-turn chat '
                'about a real past conflict. Random assignment: a reply affirming their actions or '
                'disapproving of them.',
        'comparison': 'Affirmation versus disapproval. The first two experiments also varied reply '
                      'style or a human/AI source label.',
        'example': 'After a teammate disagreement, a reply endorses your behaviour or challenges '
                   'it. Then rate how right you feel and whether you would apologize.',
        'example_kind': 'illustrative',
        'measured': 'Immediately afterwards: 1-7 ratings of feeling right and intentions to '
                    'repair, such as apologizing. Trust and intention to return were also rated.',
        'result': 'Affirming replies increased feeling right and reduced stated willingness to '
                  'repair. Trust and intended-return ratings were higher too.',
        'limit': 'Immediate intentions, not observed reconciliation or diagnosed dependence. No '
                 'neutral-reply comparison; US/English context.',
        'source_locations': 'Final Science article PDFp.5/printed4of9: '
                            'experiments2a804,2b801,3=800, procedures/results; PDFp.6 live-chat '
                            'diagram; PDFp.7/printed6of9 Fig4/5 and1-7 scales; PDFp.8 limitations.',
        'teaching_notes': 'Use finalN2405, not preprintN1604. Figure4 shows rightness and repair '
                          'only; return preference is Figure5/separate analysis. Fig4 y-axis '
                          'starts2, means1-7,95%CI; percentages annotated above bars are relative '
                          'rating changes, not probabilities or percentage-point changes. '
                          'US/English participants; supplement not reviewed. Do not conflate '
                          'agreeableness with warmth; lack of style/source effects here does not '
                          'prove disclosure never helps.',
        'primary_url': 'https://doi.org/10.1126/science.aec8352'},
 'R5': {'title': 'Will people catch a confident wrong answer?',
        'task': '359 people answered seven reasoning problems. Some had no AI; others could ask '
                'GPT-4o before answering. Researchers secretly planted correct or confidently '
                'wrong AI replies.',
        'comparison': 'No AI versus optional AI; correct versus planted wrong advice. People chose '
                      'whether to consult it and whether to follow it.',
        'example': 'A pen and notebook cost $1.10. The notebook costs $1 more. The pen costs 5 '
                   'cents, not 10 cents. Would you check confident wrong advice?',
        'example_kind': 'illustrative',
        'measured': 'Researchers scored final-answer accuracy and whether people followed the AI. '
                    'Adoption percentages include only problems where people actually consulted '
                    'it.',
        'result': 'On consulted trials, 92.7% followed correct advice and 79.8% followed faulty '
                  'advice: about four in five consulted problems, not people.',
        'limit': 'Working paper, not peer reviewed. Short tasks with planted errors, not long-term '
                 'loss of thinking skills.',
        'source_locations': 'PsyArXivJanuary11v1,58pages: PDFpp.18-20 general procedures/measures; '
                            'pp.21-22 Study1N359/optionalAI/seeded answers/adoption; p.23 '
                            'Fig2/accuracy; pp.48-49 limits. Separate WebAppendices not read.',
        'teaching_notes': 'MainStudy1N359:238AI-access/121noAI; pooledN1372includes ancillary '
                          'sample and is notStudy1N. Consultation occurred on54.4% accurate '
                          'and52.8% faulty trials. Chart rounded93/80; SE notCI. Do not call this '
                          'normalGPT4oerror prevalence: errors were engineered. Incentives plus '
                          'item feedback later reduced faulty adoption; their separate effects '
                          'were not isolated. Add spaces before projecting numeric prose; example '
                          'is an original illustration, not a paper stimulus.',
        'primary_url': 'https://doi.org/10.31234/osf.io/yk25n_v1'},
 'R9': {'title': 'Did this supervised chatbot reduce symptoms?',
        'task': '210 adults with significant depression, anxiety or eating-disorder concerns were '
                'randomly assigned to Therabot or a waitlist. The expert-built chatbot had human '
                'monitoring; access continued for eight weeks.',
        'comparison': 'This specific supported intervention versus a waitlist, not versus human '
                      'therapy or an ordinary unsupervised chatbot.',
        'example': 'Compare a depression questionnaire score before chatbot access and after four '
                   'weeks. This measures symptom change, not just whether a reply feels caring.',
        'example_kind': 'source-adaptation',
        'measured': 'Both groups completed symptom questionnaires before access, at four weeks and '
                    'at eight weeks. Researchers compared score changes between the groups.',
        'result': 'Therabot users improved more on symptom measures at four and eight weeks than '
                  'the waitlist group.',
        'limit': 'Replies were human-supervised after transmission; eligibility exclusions '
                 'applied. Not human-therapy parity or consumer-chatbot equivalence.',
        'source_locations': 'Published NEJMAI14pagePDF via public mirror: p.3 '
                            'design/participants/access; p.4 monitoring and PHQ9/GADQIV/WCS '
                            'measures; p.6 Table1/results; pp.11-12 limits. Supplement not read.',
        'teaching_notes': 'Appendix only, not another required main lecture paper. Keep '
                          'post-transmission monitoring clear: clinicians did not approve every '
                          'response before delivery. Active suicidality, mania, psychosis '
                          'excluded. Eight-week assessment is not maintenance after withdrawal; '
                          'access continued. Use safe alternative example "Compare a depression '
                          'questionnaire score before use and after four weeks" if exact recall is '
                          'not checked.',
        'primary_url': 'https://doi.org/10.1056/AIoa2400802'}}
