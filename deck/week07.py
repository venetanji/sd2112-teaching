"""Week 7: mid-term quiz, team formation and AI + X concept seeding."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import (title, agenda, statement, content, cards, activity,
                             two_col, end, finalize)
from course import SITE, footer

FOOTER = footer(7)
S = []

S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 07',
    'AI + X.', 'Mid-term quiz. Form your team. Find your X.',
    notes='Open before noon. The quiz runs 12:00-12:30, as specified by Gio. Do not teach the product-design material until the quiz has ended. No quiz questions or answer-bearing instructor files belong in this public deck.'))
S.append(agenda('WEEK 7 / QUIZ THEN WORKSHOP', [
    '12:00-12:30 / mid-term quiz on Canvas',
    'After the quiz / form teams of 4-5',
    'Gio demos Canvas team registration live',
    'AI + X / seed, choose and sketch a product concept',
    'Before leaving / register the team and deliver the concept',
], notes='Only the quiz clock is fixed by the instructor. Post-quiz activity budgets are suggestions for the existing three-hour block; adapt to the room. No guest lecture or additional quiz is assumed.'))
S.append(statement('Mid-term quiz.\n12:00-12:30.',
    eyebrow_text='CANVAS / WEEKS 1-6 + PLAYLIST / 10%', size=112,
    notes='Leave this holding slide up during the quiz. Open the instructor-published Canvas quiz. TAs handle access problems privately. Follow the rules announced by Gio and the actual Canvas settings; this deck sets no attempt count, permitted resources, extensions or availability. At 12:30 follow the demonstrated submission route and confirm submission. Never project a gradebook or instructor answer key.'))

S.append(statement('Find your X.', eyebrow_text='AFTER THE QUIZ / AI + X',
    size=150, bg=PAPER,
    notes='The new task: the team must put AI into a product. X is a meaningful area of life, practice or activity, not the name of a model. Today ends in a registered team and one early concept.'))
S.append(cards('THE BRIEF / AI + X', 'An area. A person. A product.', [
    ('X', 'Where do you care?', 'Choose an activity or situation you want to understand: repair, cooking, play, travel, learning...'),
    ('PERSON', 'Who is this for?', 'Name someone in a specific moment. What are they trying to do? What gets in the way?'),
    ('AI', 'What does it do?', 'Put AI inside the product: recognise, recommend, adapt, generate or help decide something.'),
], text_size=29, notes='These are prompts, not an exhaustive list or a new grading rubric. AI does not become necessary just because a domain is interesting. Students should be able to explain the product value without a model brand name.'))
S.append(two_col('THE COURSE DISTINCTION / USING VS INCORPORATING',
    'AI in the process is not AI in the product.',
    ['USING AI', 'An AI tool helps you make a logo, render, soundtrack or pitch.',
     'That alone does not put AI inside the thing people use.'],
    ['INCORPORATING AI', 'The product uses a model during use: it interprets an input and proposes or changes something.',
     'What does the person experience?'],
    right_font='body', left_size=33, right_size=33,
    notes='The group project concerns incorporating AI, even when AI also helps the design process. A product can be physical or digital. A chatbot is one possible interface, not the brief itself. Avoid declaring a model superior to a simpler non-AI design before research.'))
S.append(activity('01 / TEAM FORMATION', 15, 'Build a team of 4-5.', [
    'Meet around interests, not just tools. Share a possible X and something you can contribute.',
    'Make room for different design strengths: research, interaction, visuals, making and critique.',
    'Not in a team yet? Tell a TA now. Teams do not need a final idea to form.',
], notes='Suggested 15 minutes. The approved syllabus team size is 4-5. TAs help ungrouped students and check sizes privately. Do not publish student names or group rosters in this source repo. Contribution examples are not compulsory fixed roles.'))
S.append(content('LIVE DEMO / CANVAS TEAM REGISTRATION', 'Watch Gio register a team.', [
    'Gio will demonstrate the live Canvas route and the group set to use.',
    'Follow the demonstration: create your team and make sure every member joins it.',
    'Check the team name and membership together. Do not create duplicate teams.',
    'If access is blocked, ask a TA. Verify registration again before leaving.',
], body_size=34, notes='Suggested 10 minutes. Switch to the actual student-facing Canvas view. Confirm group-set setup, self-sign-up permissions, size limits and the concept collection destination before class. No screenshot, menu sequence, course URL, group-set name or working permission is invented here. Students can complete registration during this demo or the final check. Hide unrelated personal data while projecting.'))
S.append(activity('02 / IDEA SEEDING', 25, 'Start with a person. Not a model.', [
    'Alone: jot down three possible Xs from situations you know or want to investigate.',
    'Take turns: share the person, the moment and the difficulty. Listen before choosing.',
    'As a team: turn three promising seeds into possible products with AI inside them.',
    'Keep the alternatives rough. No polished pitch, code or new dataset needed today.',
], notes='Suggested 25 minutes: 5 alone, 10 sharing, 10 developing three alternatives. These are working notes, not separate submissions. Existing Week 4 brainstorms can be revisited; no team is bound to them. AI tools are optional for brainstorming. Do not enter personal or sensitive data into a model.'))
S.append(cards('ILLUSTRATIVE SEEDS / NOT FINISHED SOLUTIONS', 'A domain is only the beginning.', [
    ('AI + REPAIR', 'Find a possible fault.', 'A repair tool interprets a photo of a damaged object and suggests a next check. The person verifies before acting.'),
    ('AI + COOKING', 'Work with what is there.', 'A kitchen tool uses stated ingredients and preferences to suggest a meal. The person checks suitability.'),
    ('AI + EXPLORING', 'Notice another route.', 'A discovery tool uses chosen interests to propose places. The person can reject or change the suggestion.'),
], text_size=29, notes='Hypothetical design seeds, not real products, validated benefits or student work. Ask where errors, missing context, allergies, unsafe repairs or location privacy would matter. Do not ask students to build safety-critical automation or treat these descriptions as technical feasibility evidence.'))
S.append(statement('Break.\nTen minutes.', eyebrow_text='RETURN TO YOUR TEAM / KEEP YOUR THREE SEEDS',
    size=130, bg=PAPER, notes='Suggested 10-minute break after seeding. Keep the Canvas demo available for students who need registration help; do not make break time a mandatory extra activity.'))
S.append(activity('03 / SELECT', 20, 'Choose an idea you can explain.', [
    'Who benefits, in which moment? Which need is still only an assumption?',
    'What would AI do inside this product? Would a simpler rule work just as well?',
    'Can you show the interaction? Can you investigate the idea responsibly?',
    'Choose one seed to develop. Keep the others as alternatives, not extra deliverables.',
], notes='Suggested 20 minutes. Compare ideas for specific value, an intelligible AI role, a sketchable interaction and a manageable research direction. This is a discussion scaffold, not scoring criteria. A decision to narrow or change X is progress.'))
S.append(content('CONCEPT SCAFFOLD / SAY IT SIMPLY', 'One sentence to expose the idea.', [
    'For [person] in [situation], our [product] uses AI to [specific action or decision], helping them [benefit].',
    'Example: for a novice repairing a chair, a repair tool interprets a damage photo and suggests a next check.',
    'Then ask: what does the person still decide? What would show that the benefit is real?',
], body_size=35, notes='An optional writing scaffold, not a compulsory format or word count. The chair example is hypothetical, not a tested safe repair system. A clear concept names more than AI + a broad industry. Distinguish desired benefit from observed evidence.'))
S.append(activity('04 / DEVELOP', 25, 'What does the product do, step by step?', [
    'Sketch one moment of use: person -> input -> AI action -> result -> human choice.',
    'What input might the product need? Where could it come from with permission?',
    'What does the person see, hear or do? What happens when the AI is uncertain or wrong?',
    'Make the idea understandable to another team. Rough paper or digital sketches are enough.',
], notes='Suggested 25 minutes. This is concept development, not a coding sprint or an instruction to collect real personal data. Do not require a model architecture, implementation stack or working model. The sketch and questions are suggested aids to communicating the one concept.'))
S.append(cards('DESIGNING THE RELATION / NOT ONLY THE OUTPUT', 'A helpful suggestion can still shape a choice.', [
    ('INFLUENCE', 'What becomes visible?', 'What does the product make easy, prominent or normal? What does it hide or leave out?'),
    ('CONTROL', 'Who can say no?', 'Can the person inspect, reject, correct or undo what the system proposes?'),
    ('LIMITS', 'What must not happen?', 'Name one plausible failure or harm and a first idea for a boundary or fallback.'),
], text_size=30, notes='Apply the mediation vocabulary from Week 5 without requiring the completed Week 13 mediation brief today. These are critical design prompts, not a new assessment component. Do not invent user evidence or promise that a guardrail eliminates risk.'))
S.append(activity('05 / NEIGHBOUR CRITIQUE', 15, 'Let another team find the weak point.', [
    'Swap with a neighbouring team. Explain the person, product and AI role using your rough sketch.',
    'The other team asks: what is unclear, what are you assuming, and what could go wrong?',
    'Listen for one useful objection. Explain what you would keep, change or investigate next.',
], notes='Suggested 15 minutes. Short local pitches serve the syllabus pitch-session intent without requiring approximately 114 individual plenary pitches. No ClassPoint upload, vote, ranking or extra written critique submission. Keep feedback specific and constructive.'))
S.append(content('REFINE / BEFORE YOU DELIVER', 'Make the concept clear. Leave questions open.', [
    'Can another person explain who it is for and how it helps?',
    'Is AI inside the product, rather than only in the presentation workflow?',
    'Use a short description or rough sketch to communicate the idea.',
    'Keep a useful open question for research. Today is a starting point, not proof the idea works.',
], body_size=35, notes='Use the final 15-minute revision/collection block. Do not turn these prompts into mandatory additional documents or impose a fixed pitch format. Record an actual limitation rather than fabricate evidence.'))
S.append(content('TODAY / TWO THINGS TO FINISH', 'Register the team. Deliver the concept.', [
    'Canvas team: create it through the demonstrated route and confirm every member is in the same team.',
    'Concept: deliver one provisional AI + X product idea per team through the Canvas destination Gio shows.',
    'A short description or rough sketch is enough to communicate the idea. No working prototype is required.',
    'Reopen the team and concept together to check that registration and delivery worked.',
], body_size=33, notes='This is the only concept collection, not a series of intermediate uploads. Gio confirms the actual Canvas collection route and whether one representative submits. If permissions or upload fail, ask a TA and record the blocker privately; do not claim success or switch to a public repository. No new weight, due-time setting or assignment is created by this slide.'))
S.append(content('GROUP PROJECT / 40% / TEAMS OF 4-5', 'Today is a seed. Week 13 is the showcase.', [
    'Design a product with AI inside it. Account for what its decisions do to people.',
    'Week 8: develop the formal one-page group proposal: the decision, for whom, with what data.',
    'Week 13: A0 poster, 3-5 minute video and a one-page mediation brief.',
    'Research, ethical and social impact, communication and collaboration matter. See the syllabus rubric.',
], body_size=32, notes='Preserve the approved 40% group assessment and existing final deliverables. The wider syllabus permits a product or service; today follows Gio\'s product focus and does not rewrite that approved assessment. The Week 7 seed does not replace or accelerate the formal Week 8 proposal. No prototype implementation is added as a new final assessment requirement.'))
S.append(content('REMINDER / WEEK 7 / 20%', 'Your individual reflection is separate.', [
    'About 1000 words on AI in your creative process, especially Machine A versus Machine B.',
    'Use at least three of your own weekly-challenge experiments from Weeks 2-6, with images.',
    'End with a short AI-writing process note. Submit individually on Canvas in Week 7.',
    'Use the existing brief and rubric. Check the actual deadline on Canvas.',
], body_size=33, notes='Unchanged approved reflection brief and rubric; no new deadline or extra draft submission. Group formation does not turn the reflection into a group assignment. Do not project individual submission records.'))
S.append(end('Your team.\nYour X.', 'An AI product concept. A question worth investigating.',
    'SD2112 / WEEK 07 / ' + SITE,
    notes='Final five minutes: selected brief share-outs if time permits, check teams and concept delivery, and resolve ungrouped students privately. Next week develops AI as design material and the formal proposal. Keep student concepts, membership and submissions in approved course storage, not the public teaching repository.'))

attach_reports(S, Path(__file__).resolve().parent / 'week07-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 07',
            slides=finalize(S, FOOTER), pdf='SD2112-week07.pdf')
