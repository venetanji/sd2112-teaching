"""Separate contributor draft: DD introduction and an evidence-pending product case."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import INK, PAPER
from deckgen.layouts import T, Rect, _slide, eyebrow, figure_slide, finalize
import week10_figures as F

DC = 'https://www.designcouncil.org.uk/resources/the-double-diamond/'
S = []
CASE_START = 7
CASE_SPEAKING_MINUTES = [1, 1, 1, 1.5, 1.5, 1.5, .5]
CASE_QA_MINUTES = 2
TEAL = '#246E70'
GREY = '#5A626B'
ORANGE = '#C74600'


def frame(code, heading, notes):
    s = _slide(notes=notes, title=heading)
    s.els += [eyebrow(120, 96, code, TEAL),
              T(120, 184, 1680, 140, heading, 'xbold', 72, INK,
                lh=.95, spc=-.03, name='variant-heading')]
    return s


def strip(s, label, text, y=796):
    s.els += [Rect(120, y, 1680, 170, PAPER, name='context-strip'),
              T(148, y+18, 1624, 32, label, 'mono', 22, TEAL, name='context-label'),
              T(148, y+66, 1624, 88, text, 'body', 30, INK,
                lh=1.2, name='context-body')]
    return s


def three(code, heading, items, label, summary, notes):
    s = frame(code, heading, notes)
    for i, (kicker, title, body) in enumerate(items):
        x = 120+i*580
        s.els += [Rect(x, 358, 520, 2, '#BBBCB9'),
                  T(x, 384, 520, 36, kicker, 'mono', 22, ORANGE,
                    name=f'column-{i}-label'),
                  T(x, 438, 520, 92, title, 'xbold', 42, INK,
                    lh=1.05, name=f'column-{i}-heading'),
                  T(x, 558, 520, 202, body, 'body', 31, INK,
                    lh=1.25, name=f'column-{i}-body')]
    return strip(s, label, summary)


def slot(s, x, y, w, h, label, heading, detail):
    """An explicitly empty media space, not a reconstructed product screenshot."""
    s.els += [Rect(x, y, w, h, PAPER, '#BBBCB9', name='pending-asset'),
              T(x+24, y+24, w-48, 60, label, 'mono', 21, TEAL),
              T(x+24, y+104, w-48, 114, heading, 'xbold', 38, INK, lh=1.05),
              T(x+24, y+240, w-48, h-264, detail, 'body', 29, GREY, lh=1.2)]


# A / Introduction. Its duration is intentionally not invented from the case slot.
S.append(figure_slide('A1 / NICOLO / SEPARATE INTRODUCTION DRAFT',
    'Explore. Focus. Explore. Focus.',
    F.source_image('design-council-double-diamond.png',
                   'Unmodified official Design Council Double Diamond diagram'),
    body=['Problem space: Discover + Define. Solution space: Develop + Deliver.',
          'Diverge to explore possibilities. Converge to make a reasoned choice.'],
    caption=f'[Design Council: The Double Diamond]({DC}) / [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Official diagram, unchanged.',
    notes='Introduction, separate from the ten-minute case including Q&A. Its duration and facilitator are not set here. The official Design Council describes Discover as understanding rather than assuming the problem, Define as using insights to reframe the challenge, Develop as exploring answers and co-design, and Deliver as small-scale testing, rejecting and improving. Problem/solution space is our plain-language explanation. This framework does not establish that any particular sequence guarantees success. The following slides keep three layers distinct: principle, Nicolo\'s attributed professional account, and proposed AI uses today. Source: official Design Council page, checked 3 November 2026; image already retained with CC BY 4.0 provenance in the course.'))

S.append(three('A2 / DISCOVER / PEOPLE, CONTEXT AND AI EXPECTATIONS',
    'Understand their world. Not your assumptions.', [
        ('PRINCIPLE', 'Learn before proposing.',
         'Meet affected people. Explore tasks, context, attitudes to AI and whose perspective is missing.'),
        ('MY EXPERIENCE', 'An unfamiliar domain.',
         'Learning chemistry and analytical-lab work came before making software UX decisions.'),
        ('POTENTIAL GENAI USE', 'Explore permitted evidence.',
         'Use AI to organise approved observations and suggest questions. Check against original material.'),
    ], 'WEEKS 8-9 / RESEARCH USERS\' AI NEEDS AND DATA BOUNDARIES',
    'How do users value privacy? What will they share? What may enter AI, stay local, or never be captured?',
    'Use Nicolo\'s replacement document as an attributed account, not an independent audit of his employer. His unfamiliarity with analytical laboratories is the example. Following his feedback, foreground target users\' AI-related needs: expected benefits, willingness to share different types of data, privacy concerns, trust, acceptable automation and acceptable places of processing. Willingness is not permission to use data: check applicable consent, organizational rules, ownership and confidentiality; distinguish collection, inference, retention and sharing. Ask which people and contexts are missing from research. Do not feed a whole research folder into a service by default; use only the minimum permitted material in an approved environment. Removing names does not establish anonymity. Synthetic personas or role-play may suggest questions but cannot replace evidence from actual users, especially in a specialist domain. Week 8: AI cues, mediation and control; Week 9: Useful does not mean necessary, data boundaries and representation.'))

S.append(three('A3 / DEFINE / EVIDENCE INTO A FOCUSED CHALLENGE',
    'Choose the challenge. Keep the evidence.', [
        ('PRINCIPLE', 'Make priorities explicit.',
         'Synthesize findings into a clear challenge, with user needs, business needs and unresolved assumptions.'),
        ('MY EXPERIENCE', 'A clearer workflow goal.',
         'Priorities: speed, efficiency, ease of use and support for less-experienced operators.'),
        ('POTENTIAL GENAI USE', 'Compare possible framings.',
         'Draft journeys or profiles from evidence. Label inferred details and verify them with people.'),
    ], 'WEEK 9 / A MEASURABLE PROXY IS NOT THE WHOLE USER GOAL',
    'Fewer clicks can help. Also ask whether people can complete the right task, understand it and recover.',
    'The historical goals here are those in Nicolo\'s document; the detailed current product UX goals and their evidence will arrive later for Section B. Do not equate fewer clicks with usability in every setting. Define synthesizes and focuses; it is not an algorithm that discovers a single objectively best option. AI can draft a user journey or organize findings, but a generated quote, goal or persona detail is not research evidence. Keep traceability to actual observations and distinguish user wishes, business demands, safety requirements and feasibility. Week 9\'s value-versus-proxy example transfers as a question, not as proof about this laboratory product.'))

S.append(three('A4 / DEVELOP / CO-DESIGN AND ALTERNATIVES',
    'Explore different experiences. Together.', [
        ('PRINCIPLE', 'Do not polish the first idea.',
         'Compare meaningful alternatives with users, designers, developers and product stakeholders.'),
        ('MY EXPERIENCE', 'Bring other perspectives in.',
         'Recurring design discussions and a co-design workshop with a product manager and developer.'),
        ('POTENTIAL GENAI USE', 'Prototype beyond the visual.',
         'Explore workflows, interactions and media. AI-generated code is a prototype, not production readiness.'),
    ], 'WEEK 8 / DESIGN THE AI\'S ROLE AND THE PERSON\'S CONTROL',
    'Using AI to make a prototype differs from AI inside the product. Can the person question, correct, reject and recover?',
    'This combines the document\'s Develop account and Week 8 agency/calibrated trust. The workshop and recurring discussions are attributed to Nicolo, with no invented participants or outcomes. Generate diverse responses to the same problem, not only cosmetic screen changes. Prototypes can be paper, interactive software or media; use only enough fidelity to answer the question. Generated code needs technical, security, accessibility and integration review; do not describe it as a complete product merely because it runs. If AI is incorporated in the proposed product, make the model action, written rule and retained human decision explicit. An override button alone does not establish meaningful agency. No AI features are invented for the pending case.'))

S.append(three('A5 / DELIVER / TEST, LISTEN AND PRIORITISE',
    'What works? What do people want next?', [
        ('PRINCIPLE', 'Test and ask why.',
         'Observe realistic tasks. Ask what worked, what did not, what people wish for and why it matters.'),
        ('MY EXPERIENCE', 'Test across development.',
         'Usability tests and comparisons informed iteration: positive findings and wishes for improvement.'),
        ('POTENTIAL GENAI USE', 'Assist analysis, not validation.',
         'Compare AI-assisted themes with your own analysis. Return to users and original evidence.'),
    ], 'WEEKS 8-9 / OUTCOMES, FAILURES AND THE PRIORITY OF USER WISHES',
    'Which wish matters most, to whom and in what context? Compare importance with observed failures and task outcomes.',
    'Reflect Nicolo\'s request to emphasize wishes and their priorities, not only failure detection. During testing, collect observed task behaviour separately from stated satisfaction and desired improvements. Ask why/how, clarify the need behind a requested feature, and ask users to prioritize wishes; keep minority and context-dependent needs visible rather than using a simple majority as a universal rule. Priority is a design judgment informed by user importance, observed severity, organizational constraints and feasibility, not an AI-generated ranking presented as users\' wishes. The document reports five usability-testing activities across the lifecycle, including comparisons; no participant count, effect size or new study result is invented. AI-assisted coding or synthesis needs checks against source records, permission and contradictory evidence. Agent walkthroughs or synthetic users can expose possible issues but cannot establish human usability, fairness, safety or model reliability.'))

S.append(three('A6 / ITERATION / RETURN WHEN THE EVIDENCE CHANGES',
    'The diamonds are not a one-way road.', [
        ('RETURN TO DISCOVER', 'A missing need appears.',
         'Testing reveals an unfamiliar context. Learn about it before deciding what to change.'),
        ('RETURN TO DEFINE', 'The goal needs reframing.',
         'A proposed solution does not address what matters. Revisit the challenge and priorities.'),
        ('RETURN TO DEVELOP', 'An interaction needs work.',
         'Compare a revised response, then test again. Record what changed and what remains uncertain.'),
    ], 'REAL-WORLD PRACTICE / PROTECT LEARNING UNDER CONSTRAINTS',
    'Time and budget are limited. Prioritise the uncertainty that could change the design, not just the next feature.',
    'These are illustrative routes, not claims that every project follows all three. The official Design Council page explicitly describes returning to earlier work and early making/testing within discovery. Nicolo\'s document emphasizes iteration and practical prioritization. Preserve that professional insight without making the unsupported universal claim that only the second diamond creates business value. Discovery can prevent expensive wrong commitments. The official diagram remains unchanged on A1; this slide supplies our explanation rather than a modified official diagram. No introduction duration is silently added to the ten-minute case allowance.'))

S.append(three('A7 / STAKEHOLDERS / FROM DESIGN PROCESS TO AI PRODUCT',
    'Good design needs more than one viewpoint.', [
        ('PEOPLE USING IT', 'Need, context and priorities.',
         'Include intended and affected people. Classmates and generated personas are not substitutes.'),
        ('PEOPLE BUILDING IT', 'Capabilities and constraints.',
         'Designers, developers and product stakeholders negotiate alternatives, integration and trade-offs.'),
        ('PEOPLE RESPONSIBLE', 'Data, access and consequences.',
         'Identify who can permit data use, support a failure and approve a change in the real setting.'),
    ], 'TRANSITION / TWO DIFFERENT AI CLAIMS',
    'AI helping me design: a process choice. AI inside the product: a change to the user\'s experience and responsibilities.',
    'Close the introduction with Nicolo\'s stakeholder-management emphasis. The categories are teaching prompts, not invented confirmed roles in his project. Users are not a final sign-off step: they matter throughout the process, alongside collaboration with design, engineering and management. Communicating findings is a design skill, but stakeholder agreement is not independent user evidence. Make the transition explicit: the retrospective AI-tool possibilities in A2-A5 are not claims those tools were used historically; Section B will consider proposed AI-enabled product features with context-specific constraints. Section A can be reviewed independently while B awaits approved assets.'))


# B / Case storyboard: visible pending labels prevent a draft from posing as evidence.
s = frame('B1 / CASE STORYBOARD / 10 MIN TOTAL INCLUDING Q&A',
    'Today: how does the product work?',
    'Proposed speaking allocation: one minute. The entire Section B has eight speaking minutes plus two for Q&A, not eight plus an unlimited discussion. This is a storyboard awaiting Nicolo\'s portfolio slides, approved product images, intended-use video, target users and context. Extract relevant material only after receipt and permission review. Do not invent a product name, workflow, user quote, laboratory scene or screenshot. Use a short permitted video excerpt or offline still sequence only if the content and slot support it. Current device and workflow must stay distinct from the proposed AI redesign. Private/company material must not be placed in repository history or an unauthenticated preview without permission.')
slot(s, 120, 358, 1050, 400, 'CURRENT PRODUCT / MATERIAL PENDING', 'Approved portfolio screenshot',
     'Intended users, setting and current workflow will come from your source material.')
slot(s, 1220, 358, 580, 400, 'INTENDED USE / MATERIAL PENDING', 'Images or video',
     'Use only the relevant permitted excerpt. No fabricated product demonstration.')
S.append(strip(s, 'CASE STATUS / NOT YET A COMPLETE PRESENTATION',
    'Screenshots, context, UX goals and sharing permissions are pending. The original Week 10 presentation is unchanged.'))

S.append(three('B2A / CURRENT PRODUCT / QUALITATIVE EVIDENCE PENDING',
    'What works, and what should improve?', [
        ('POSITIVE FINDING 1', 'Awaiting a real finding.',
         'Add an observation and its task/context. No invented participant quote or success claim.'),
        ('POSITIVE FINDING 2', 'Awaiting a real finding.',
         'Use a distinct positive finding from the supplied portfolio or research material.'),
        ('WISHES FOR IMPROVEMENT', 'Awaiting wishes and priority.',
         'Record what users wanted, why it mattered and which improvements they prioritized.'),
    ], 'ONE PROPOSED SPEAKING MINUTE / KEEP OBSERVATION AND INTERPRETATION DISTINCT',
    'Evidence -> UX goal -> improvement priority. Preserve context, disagreement and remaining questions.',
    'Nicolo asks for a couple of positive qualitative findings plus wishes for improvements before the quantitative slide. These slots deliberately contain no fake quotes or positive results. Await the source observations, method, intended users, task and permission to share. Distinguish the person\'s stated wish from designer interpretation; relate each to the actual UX goals when supplied. Do not imply all users agreed or infer prevalence from a handful of anecdotes. Proposed speaking allocation: one minute.'))

s = frame('B2B / CURRENT PRODUCT / SPEAKER-REPORTED FIGURES',
    'Reported gains. Context still matters.',
    'Proposed speaking allocation: one minute. Nicolo supplied two historical current-product statements in chat: 30% faster than manual workflows, and one click to prepare and submit a sample list. He will provide context later. These are attributed claims awaiting the actual task, comparator, timing definition, method, sample, uncertainty, source and sharing clearance; they are not independently verified. Do not conflate 30% faster with 30% less completion time: the original definition and calculation must be checked. Clarify where the one-click action begins and ends and what setup/preparation remains outside it. Do not show an invented chart, sample size or confidence interval. These figures do not measure the proposed AI redesign and must not become its claimed benefit.')
for x, number, detail in [(120, '30%', 'Reported faster than manual workflows'),
                           (1000, '1 click', 'Reported to prepare and submit a sample list')]:
    s.els += [Rect(x, 358, 800, 400, PAPER),
              T(x+32, 390, 736, 150, number, 'xbold', 112, INK, lh=1),
              T(x+32, 590, 736, 110, detail, 'body', 36, INK, lh=1.2)]
S.append(strip(s, 'ATTRIBUTED TO NICOLO / NOT INDEPENDENTLY VERIFIED / NOT AI REDESIGN RESULTS',
    'Await task, baseline, measurement method, action boundaries, source and permission. Do not infer a study design.'))

s = frame('B3A / PROPOSED AI REDESIGN / NOT IMPLEMENTED',
    'Before and after: one consequential change.',
    'Proposed speaking allocation: one and a half minutes. Nicolo requests one before/after slide followed by a separate three-screen sequence. Use the genuine current screen and his proposed redesign, not a reconstruction presented as a product artifact. Both are pending. Connect the change to a supplied UX goal and clarify the AI action, retained human decision and failure route. No feature, measured improvement, screenshot or specific interaction is invented by these empty spaces. The after view must stay labelled proposed even if it later becomes a convincing high-fidelity mockup.')
slot(s, 120, 358, 800, 400, 'BEFORE / CURRENT PRODUCT', 'Current screen pending',
     'Show the real workflow and relevant UX friction.')
slot(s, 1000, 358, 800, 400, 'AFTER / PROPOSED, NOT IMPLEMENTED', 'Redesign screen pending',
     'Annotate the AI-enabled change against an actual UX goal.')
S.append(strip(s, 'ANNOTATION CONTRACT',
    'What does AI do? What still needs a person? What happens when the output is wrong, unavailable or rejected?'))

s = frame('B3B / PROPOSED AI EXPERIENCE / THREE-SCREEN SEQUENCE',
    'Show the experience, not just a feature.',
    'Proposed speaking allocation: one and a half minutes. Nicolo explicitly asks for a sequence of three annotated screenshots on this slide. Screens are pending: do not invent their actions or order. Populate them from his approved proposed flow, then make annotations legible and connect them to actual UX goals. Identify AI work, human choice and a recovery/uncertainty condition where those occur in the real proposal. Keep all three screenshots as proposed, not implemented, and distinguish synthetic placeholders from actual screenshots. Provide full explanation in native notes rather than crowding the images.')
for i in range(3):
    slot(s, 120+i*580, 358, 520, 400, f'PROPOSED SCREEN {i+1} / PENDING',
         f'Flow step {i+1}', 'Approved screenshot and precise on-slide annotations to follow.')
S.append(strip(s, 'WAITING FOR THE ACTUAL PROPOSED FLOW',
    'Use three supplied screens in order. Annotate the user action, the AI contribution and the relevant UX goal.'))

S.append(three('B4A / FEASIBILITY / CONTEXT IS PART OF THE DESIGN',
    'A lab is not a frictionless demo.', [
        ('ENVIRONMENT + CAMERAS', 'Can it work here?',
         'Check low light, camera placement and occlusion. Is image capture permitted and appropriate in this lab?'),
        ('SYSTEMS + CONNECTIVITY', 'Can it fit this site?',
         'Check legacy integration, digital readiness, network reliability, cloud policy and an offline route.'),
        ('DEVICE + PROCESSING', 'What must change?',
         'Assess compute, memory, power, latency and device adaptation. Local versus cloud processing has trade-offs.'),
    ], 'POTENTIAL CONSTRAINTS TO INVESTIGATE / NOT A COMPLETED TECHNICAL AUDIT',
    'Ask users, lab operations, IT and engineering. Validate feasibility in the intended setting, not only at a desk.',
    'Proposed speaking allocation: one and a half minutes. Nicolo wants environmental and implementation constraints to demonstrate why understanding users and context matters. Treat low light, lab camera restrictions, cloud/digital readiness, compute and device adaptation as potential constraints, not verified characteristics of the specific site or universal facts about modern laboratories. Do not claim that all labs are currently unready for digital/cloud systems or that an industry trend was audited. Ask what this site can support: permissions, confidentiality and camera field of view; lighting/occlusion; actual systems interfaces, approved processing and reliability; measured target hardware latency, memory and power. On-device processing may reduce some transfers but is not automatically private or feasible. Cloud processing can create connectivity, latency and policy issues; requirements and implementation need actual technical review. PPE, cleaning and safety issues may be explored if relevant, not assumed. Tie each confirmed constraint back to the UX goal and a test, fallback or scope change.'))

S.append(three('B4B / PROPOSED EVALUATION + Q&A',
    'Would this improve the experience here?', [
        ('USEFUL OUTCOME', 'Test the UX goal.',
         'Compare current and proposed workflows on a relevant task, with a meaningful baseline.'),
        ('FAILURE + CONTROL', 'Test difficult conditions.',
         'Check errors, low light, disconnection, rejection and recovery where relevant to the actual proposal.'),
        ('USER PRIORITY', 'Ask what matters next.',
         'Combine observed outcomes with users\' wishes, their priorities and the burden of the change.'),
    ], 'PROPOSED .5-MINUTE CLOSE + 2 MINUTES Q&A / TOTAL CASE SLOT: 10 MINUTES',
    'Which user need or environmental constraint could change this AI redesign most, and how would we investigate it?',
    'Half-minute close, followed by two minutes of Q&A within the same ten-minute case slot. Total proposed speaking allocations for B1-B4B are eight minutes. This is a bounded evaluation plan, not proof of benefit or deployment readiness. Metrics, task and comparator must be specified after the actual current UX goals and redesign are provided. Do not reuse the historical 30% and one-click statements as predictions of AI benefits. Distinguish interface comprehension, actual model/device performance and the user\'s ability to complete a meaningful task in context. State what could disconfirm the proposal, including unequal burdens and an unusable fallback. The proposed audience question is optional facilitation, not a new assessed task or submission.'))

DECK = dict(title='SD2112 / Week 10 / Nicolo separate contributor draft',
            slides=finalize(S, 'SD2112 / AI IN DESIGN / WEEK 10 / NICOLO VARIANT'),
            pdf='SD2112-week10-nicolo.pdf')
