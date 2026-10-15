"""Week 7: concept recap, mid-term quiz and two 20-minute team steps."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports
from deckgen.layouts import title, agenda, statement, content, activity, question, end, finalize
from course import SITE, footer
from news_20261014 import news_slides
from week07_recap import recap_slides

FOOTER = footer(7)
S = []

S.append(title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 07',
    'AI + X.', 'This week in AI. Recap. Quiz. Your team and product.',
    notes='This week in AI opens this same Week 7 deck; choose news slides as an optional pre-class opener. Class starts at 11:30 with the twenty-slide recap, then ClassPoint questions from 11:45 until noon. The Canvas quiz remains 12:00-12:30. No quiz questions or answer keys belong in this public deck.'))
NEWS = news_slides('SD2112')
S.extend(NEWS)
S.append(agenda('WEEK 7 / RECAP THEN QUIZ THEN TEAMS', [
    '11:30-11:45 / Weeks 1-6 / twenty key concept slides',
    '11:45-12:00 / ask me anything / send your questions',
    '12:00-12:30 / mid-term quiz on Canvas',
    'Gio demos Canvas team registration live',
    'Step 1 / twenty minutes / one core-concept text per team',
    'Step 2 / twenty minutes / one product image per team',
], notes='Fifteen-minute recap, then fifteen minutes for questions before the noon test. Team formation and registration are included in Step 1, not separate timed activities. The two workshop steps total forty minutes including both submissions.'))

RECAP = recap_slides(first_number=len(S) + 1)
S.extend(RECAP)
S.append(question('short_answer', 'Ask me anything.',
    hint='What would you like to clarify?\nSend your questions on ClassPoint until 12:00.',
    eyebrow_text='11:45-12:00 / BEFORE THE QUIZ / YOUR QUESTIONS',
    cp={'type': 'short_answer', 'hide_names': False, 'multiple': True},
    notes='After the fifteen-minute recap, collect student questions until noon. Read and discuss them live; students may send more than one question. This is a question inbox, not a graded response or a team concept submission. Stop at 12:00 and give the quiz its full thirty minutes.'))
S.append(statement('Mid-term quiz.\n12:00-12:30.',
    eyebrow_text='CANVAS / WEEKS 1-6 + PLAYLIST / 10%', size=112,
    notes='Start at noon after the recap and questions. Leave this holding slide up for the full thirty-minute Canvas quiz, 12:00-12:30. Confirm actual Canvas availability and announce the rules. TAs handle access problems privately. Confirm submission before introducing the team workshop.'))

S.append(content('AFTER THE QUIZ / AI + X / TEAMS OF 4-5',
    'One concept. One product image.', [
    'Choose an area of life or practice, a person and a situation that matter to your team.',
    'The product must incorporate AI: what does it recognise, recommend, adapt or generate during use?',
    'Step 1: form and register your team; submit one short core-concept text.',
    'Step 2: make and submit one image showing the product and a moment of use.',
], body_size=33, notes='Brief the two steps together. AI may help make the image, but the product itself must use AI. A physical or digital product is welcome. This is a provisional idea, not the formal Week 8 proposal.'))
S.append(content('LIVE DEMO / CANVAS TEAM REGISTRATION',
    'Watch Gio register a team.', [
    'Gio demonstrates the actual Canvas group set and registration route live.',
    'In Step 1, form a team of 4-5 and make sure every member joins the same Canvas team.',
    'Choose one representative to send both ClassPoint submissions, identifying the same team.',
    'If you need a team or access help, tell a TA as Step 1 begins.',
], body_size=33, notes='Keep the instructor demo brief, before the forty-minute workshop timer. Confirm the real group set and self-registration permissions before class. Show ClassPoint text and image collection routes; no additional Canvas concept upload. Do not invent menu steps or project unrelated personal records.'))
S.append(activity('01 / CORE CONCEPT', 20,
    'Form your team. State the idea.', [
    'Form a team of 4-5 around a shared interest. Follow the demo to register on Canvas.',
    'Choose one direction: for [person] in [situation], our [product] uses AI to [action], helping them [benefit].',
    'Name what the person still decides and one assumption you need to investigate.',
    'One representative submits one short core-concept text on ClassPoint, with the team name.',
], eyebrow_text='TEAM TEXT', cp={'type': 'short_answer', 'hide_names': False, 'multiple': False},
    notes='Twenty minutes total: suggested five to form/register, ten to choose and describe one concept, five to submit/check. One text per team, not one per student. Working notes and alternatives are not extra submissions. TAs support ungrouped students immediately. Check Canvas membership during this step. No new word count, grading weight or formal proposal requirement.'))
S.append(activity('02 / PRODUCT IMAGE', 20,
    'Show the product in use.', [
    'Sketch, mock up or generate one image showing your product in use, not just its logo.',
    'Show the person and product. Label the AI action and what the person decides.',
    'The same representative uploads one image on ClassPoint with the team name. Reopen it to check.',
], eyebrow_text='TEAM IMAGE', cp={'type': 'image_upload', 'hide_names': False},
    notes='Twenty minutes total: suggested fifteen to make and discuss the image, five to upload and reopen it. One image per team; no presentation deck, video, working prototype or extra critique upload. Paper sketch photographed on a phone is sufficient; no new AI account is required. Generating the visual is using AI in the design process, distinct from the AI action inside the proposed product. Record tools and supplied assets honestly in the team working notes.'))
S.append(content('FINISH / TWO SUBMISSIONS PER TEAM',
    'Check the text, image and team.', [
    'One core-concept text and one product image are visible in the two ClassPoint activities.',
    'Both carry the same team name and describe the same provisional AI + X product.',
    'Every member has joined the same Canvas team. Reopen it together to check.',
    'If submission or registration failed, ask a TA before leaving.',
], body_size=34, notes='These checks belong inside the two twenty-minute steps. Do not add another collection or mandatory critique round. Use remaining class time for optional feedback, discussion and access support. Keep membership and submissions out of this public repository.'))
S.append(content('GROUP PROJECT / 40% / TEAMS OF 4-5',
    'Today is a seed. Week 13 is the showcase.', [
    'Design a product with AI inside it. Account for what its decisions do to people.',
    'Week 8: develop the formal one-page group proposal: the decision, for whom, with what data.',
    'Week 13: A0 poster, 3-5 minute video and a one-page mediation brief.',
    'Research, ethical and social impact, communication and collaboration matter. See the syllabus rubric.',
], body_size=32, notes='Preserve the approved forty-percent group assessment and final deliverables. The broader syllabus permits a product or service; today follows the product focus. The Week 7 text and image seed the formal Week 8 proposal.'))
S.append(content('REMINDER / WEEK 7 / 20%',
    'Your individual reflection is separate.', [
    'About 1000 words on AI in your creative process, especially Machine A versus Machine B.',
    'Use at least three of your own weekly-challenge experiments from Weeks 2-6, with images.',
    'End with a short AI-writing process note. Submit individually on Canvas in Week 7.',
    'Use the existing brief and rubric. Check the actual deadline on Canvas.',
], body_size=33, notes='Existing reflection brief, weight and rubric; no new deadline or extra draft submission.'))
S.append(end('Your team.\nYour X.', 'One core concept. One image of an AI product.',
    'SD2112 / WEEK 07 / ' + SITE,
    notes='Resolve ungrouped students and collection blockers privately. Remaining time can support optional local sharing and feedback. Next week develops the formal proposal.'))

for slide in S:
    if slide.cp:
        # Activity layouts need the same report-link anchor as question layouts.
        slide.els[0].name = 'question-eyebrow'
attach_reports(S, Path(__file__).resolve().parent / 'week07-reports.json')
DECK = dict(title='SD2112 / AI in Design / Week 07',
            slides=finalize(S, FOOTER), pdf='SD2112-week07.pdf')
