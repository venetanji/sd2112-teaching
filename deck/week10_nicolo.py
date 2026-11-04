"""Separate contributor draft, using Nicolo's document as the writing reference."""
from pathlib import Path
import base64
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import INK, PAPER
from deckgen.layouts import T, Rect, Figure, _slide, eyebrow, finalize
import week10_figures as F
from week10_nicolo_figures import phase_map, phase_subtitle
from week10_nicolo_case import (build_case, CASE_TITLE, CASE_SPEAKING_MINUTES,
                               CASE_QA_MINUTES, SCREEN_RATIO, PRODUCT_SCREEN)

DC = 'https://www.designcouncil.org.uk/resources/the-double-diamond/'
S = []
PHASES = [('problem space', 'discover'), ('problem space', 'define'),
          ('solution space', 'develop'), ('solution space', 'deliver')]
CASE_START = 9
TEAL = '#246E70'
GREY = '#5A626B'
ORANGE = '#C74600'
DD_DEFINITION = (
    'The\u00a0Double Diamond\u00a0is a visual representation of the design and innovation process. '
    'It\u2019s a simple way to describe the steps taken in any design\u00a0and innovation\u00a0project, '
    'irrespective of methods and tools used.'
)


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


def three(code, heading, items, label, summary, notes, neutral_navigation=False):
    s = frame(code, heading, notes)
    if neutral_navigation:
        title = s.els[-1]
        title.w, title.h = 1200, 100
        title.paras[0].runs[0].size = 64
        svg, png = phase_map()
        s.els.append(Figure(1440, 210, 360, 176, svg, png, name='phase-navigation'))
    for i, (kicker, title, body) in enumerate(items):
        x = 120+i*580
        s.els += [Rect(x, 416 if neutral_navigation else 358, 520, 2, '#BBBCB9'),
                  T(x, 442 if neutral_navigation else 384, 520, 36, kicker, 'mono', 22, ORANGE,
                    name=f'column-{i}-label'),
                  T(x, 498 if neutral_navigation else 438, 520,
                    72 if neutral_navigation else 92, title, 'xbold',
                    38 if neutral_navigation else 42, INK,
                    lh=1.05, name=f'column-{i}-heading'),
                  T(x, 582 if neutral_navigation else 558, 520, 202, body, 'body', 31, INK,
                    lh=1.25, name=f'column-{i}-body')]
    return strip(s, label, summary)


def phase_slide(number, items, summary, notes):
    space, phase = PHASES[number]
    s = _slide(notes=notes, title=phase.title())
    svg, png = phase_map(phase)
    subtitle_w, subtitle_svg, subtitle_png = phase_subtitle(space, phase)
    s.els += [eyebrow(120, 96, 'DOUBLE DIAMOND', TEAL),
              T(120, 184, 1200, 100, phase.title(), 'xbold', 88, INK,
                lh=.95, spc=-.03, name='variant-heading'),
              Figure(120, 306, subtitle_w, 48, subtitle_svg, subtitle_png,
                     name='phase-subtitle'),
              Figure(1440, 210, 360, 176, svg, png, name='phase-navigation')]
    for i, (label, body) in enumerate(zip(
            ('GENERAL PRINCIPLES', 'INDUSTRY EXAMPLE', 'POTENTIAL AI USE'), items)):
        x = 120+i*580
        s.els += [Rect(x, 416, 520, 2, '#BBBCB9'),
                  T(x, 442, 520, 36, label, 'mono', 22, ORANGE,
                    name=f'phase-{i}-label'),
                  T(x, 502, 520, 250, body, 'body', 33, INK,
                    lh=1.22, name=f'phase-{i}-body')]
    return strip(s, 'WEEKS 8-9 / AI CONSIDERATIONS', summary)


s = _slide(title='Double Diamond', notes=
    DD_DEFINITION+' The first diamond is the problem space; the second is the solution space. The following slides explain each phase through its general principles, an industry example and potential AI uses. Potential AI uses are proposals for today, not historical claims about the original project. The introduction is separate from the ten-minute case including Q&A; its duration is still open. Source: Design Council, The Double Diamond, CC BY 4.0.')
svg, png = F.source_image('design-council-double-diamond.png',
                          'Unmodified official Design Council Double Diamond diagram')
s.els += [eyebrow(120, 96, 'INTRODUCTION', TEAL),
          T(120, 184, 1680, 90, 'Double Diamond', 'xbold', 64, INK,
            lh=.95, spc=-.03, name='variant-heading'),
          T(120, 286, 1680, 80, '\u201c'+DD_DEFINITION+'\u201d', 'body', 30, INK,
            lh=1.22, name='dd-definition'),
          ]
# The official image's diamond centres are at x=246 and x=694 of its 936 px width.
diagram_x, diagram_y, diagram_w = 474, 454, 972
for label, center in [('Problem Space', 246), ('Solution Space', 694)]:
    s.els.append(T(diagram_x+diagram_w*center/936-200, diagram_y-48, 400, 42,
                   label, 'xbold', 34, INK, align='c', name='dd-space-label'))
s.els += [Figure(diagram_x, diagram_y, diagram_w, round(diagram_w*453/936),
                 svg, png, name='dd-official-diagram'),
          T(120, 956, 1680, 44,
            f'[Design Council: The Double Diamond]({DC}) / [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Official diagram, unchanged.',
            'mono', 18, TEAL, lh=1.2, name='dd-source')]
S.append(s)

S.append(phase_slide(0, [
    'Spend enough time understanding your users. You cannot expect the user to be exactly like you. Do not assume the problem. Use divergent thinking.',
    'The Software UX Design project required time to understand an unfamiliar field: chemistry and analytical laboratories. This was foundational for the rest of the work.',
    'Have a conversation with the research data you are allowed to use. Synthetic users can help with role-play, but cannot replace reaching out to actual users.',
], 'How do users value privacy? What data are they willing to share? What data can be fed to AI?',
    'As designers, when you decide to work on a topic, any topic, it is fundamental to form an understanding of the context and your users. You cannot expect users to have the same needs, mindset or way of thinking as you. Do not assume the problem. Discover uses divergent thinking: you explore different insights and ideas rather than jumping to conclusions. The Software UX Design project required time to understand chemistry and analytical laboratories, an unfamiliar field. Forming that understanding was foundational for the rest of the work. Today, AI could help elaborate on the data gathered from users and support a conversation with that data. First, check what can be shared, with which service, and for what purpose; do not upload the whole research collection by default. Willingness is not permission to use data, and removing names does not establish anonymity. Synthetic-user role-play can help suggest questions, but it cannot replace reaching out to actual users, especially in niche fields. Understand their attitude towards AI, how they use it, how they value privacy and which data they are willing and permitted to share. These are the connections to Weeks 8-9. Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; labels and arrows omitted, inactive phases black and white, Discover highlighted.'))

S.append(phase_slide(1, [
    'Use convergent thinking to narrow down your insights and clearly define the challenge: the problem you want to solve.',
    'Connecting with users and considering business needs helped define the focus: speed, efficiency and ease of use, including for less-experienced operators.',
    'Use AI conversationally to narrow down the topic and draft personas, user profiles or user journeys from your findings. Consider users\' needs regarding AI.',
], 'Define what users need from AI. Saving clicks is useful only if it helps them accomplish the task.',
    'By now you should have gathered a lot of insights and thoughts about a topic. At this stage it is time to clearly define the challenge, the problem you want to solve. Define uses convergent thinking: narrowing down the options and insights gathered during Discover. Reaching this point in the project took time, but the direction became clearer afterwards. Connecting with users and taking business needs into consideration was fundamental. The focus became speed, efficiency and ease of use of the workflow: less time dealing with different tools, and a system that people without extensive expertise could use. Today, AI could be used conversationally to narrow down the topic and produce useful artifacts such as personas, user profiles and user journeys. Keep those artifacts connected to the research: generated details and quotes are not findings from actual users. Consider the needs of users regarding AI, including what it should do and what people still need to decide. Week 9 helps distinguish a proxy such as fewer clicks from the actual user goal. There is not necessarily one objectively best framing; the choice still needs reasoning and evidence. Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; labels and arrows omitted, inactive phases black and white, Define highlighted.'))

S.append(phase_slide(2, [
    'Use divergent thinking to explore different solutions. Co-design with users and other stakeholders. Avoid going with the first thing that comes to your mind.',
    'The design team discussed ideas almost every week. A co-design workshop with the Product Manager and an Engineer brought in other perspectives.',
    'Generate several prototype or media variants. Do not stop at the visual part: think about interactions, sounds, workflows, user contexts and environments.',
], 'When integrating AI into the product, consider what AI does and what the person can understand, change or reject.',
    'Once the problem to solve is defined, it is time to move to the second diamond, the solution space. Use the creative process again to think of different potential solutions. Develop uses divergent thinking: explore possibilities instead of going with the first thing that comes to your mind. Be in touch with users to co-design, and involve Product Managers, other UX Designers, designers from other disciplines and engineers. Different stakeholders give different perspectives. A solution does not need to be perfect: a simple draft, paper sketch or prototype can be enough to communicate ideas. In the design team, ideas were discussed almost every week. A co-design workshop with the Product Manager and an Engineer also helped gather their perspectives. Today, AI could generate prototype or multimedia variants for discussion with the team. In this phase, quantity over quality means exploring alternatives, not ignoring safety or confidentiality. Vibe coding can help build testable software variants; running code is not the same as a production-ready product. Do not stop at visuals: consider interactions, sounds, workflows, user contexts and environments, and different ways AI could be integrated into the product. Following Week 8, consider what AI does, what the person still decides and how they can question, correct or reject an output. Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; labels and arrows omitted, inactive phases black and white, Develop highlighted.'))

S.append(phase_slide(3, [
    'Use convergent thinking to narrow down the options. Test ideas with users and observe them going through tasks: what works and what does not?',
    'Five usability tests were run throughout the product lifecycle, including A/B testing. Key questions: what worked, what did not, and what users wish to improve.',
    'Use AI to assist with data analysis and compare its findings with your own. Synthetic feedback can suggest issues to investigate, not validate the experience.',
], 'Ask why and how. Understand users\' wishes and priorities, alongside what you observe during the tasks.',
    'Once different potential solutions have been found, it is time to test them and see what works and what does not. Deliver uses convergent thinking again: narrow down the options explored in Develop. With usability testing, observe users going through a set of tasks with the prototype; for other design disciplines, compare variants using an appropriate method. Five usability tests were run throughout the product lifecycle, including A/B testing. Getting and validating ideas with users is an essential part of the workflow. Ask directly what worked, what did not work and what their wishes are about the product. Ask about specific aspects of the experience, and remember to ask why and how. Understand the priorities of those wishes; compare what people say with what happens during tasks. Today, AI could assist in data analysis, with its findings compared against the research and the design team\'s analysis. An agent can also role-play a persona or walk through a task, but generated feedback and improvement wishes are not actual users\' findings. Such walkthroughs cannot establish human usability, fairness, safety or model reliability. Test with actual users, and test the AI behaviour as well as the interface. Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; labels and arrows omitted, inactive phases black and white, Deliver highlighted.'))

S.append(three('DOUBLE DIAMOND / ITERATION', 'An iterative and imperfect process', [
    ('DISCOVER AGAIN', 'Understand a new need.',
     'Testing may reveal a user need you did not notice before. Go back to understand the user and the context.'),
    ('DEVELOP AGAIN', 'Revise the idea.',
     'You may need to return to Develop to fix a detail you missed, then test the revised prototype.'),
    ('REAL-WORLD PROJECTS', 'Prioritise your time.',
     'The phases do not all take the same amount of time. A designer needs to prioritise and manage time on a project.'),
], 'ITERATION THROUGHOUT THE PROCESS',
    'You may need to go back to an earlier phase. The Double Diamond is not a fixed sequence of steps.',
    'Although the picture may not show every loop, the Double Diamond is iterative at every phase. Once you have defined the problem, you may still need to go back to discovery and understanding the user. During testing, you may notice different needs or a new need you had not seen before. Go back to Discover to understand the context, or return to Develop to fix a detail. The phases do not all take the same amount of time; the equal-sized halves in this map do not represent equal durations. In the real world, you may never have enough time for everything, so a designer should know how to prioritise and manage time on a project. Obtaining enough time and budget for the first diamond can be difficult. That does not mean only the second diamond creates value: finding out early that you are addressing the wrong problem can prevent wasted development. The introduction duration remains open. Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; labels and arrows omitted, all phases black and white without an accent highlight.', neutral_navigation=True))

S.append(three('DOUBLE DIAMOND / COLLABORATION', 'Stakeholder management', [
    ('USERS', 'Keep users involved.',
     'Users are central throughout the process: understanding their context, co-designing ideas and testing the experience.'),
    ('OTHER PROFESSIONALS', 'Work across disciplines.',
     'Collaborate with other designers, engineers, developers and product managers. They bring different perspectives to the design.'),
    ('COMMUNICATION', 'Share your findings.',
     'Explain what you have learned to the people you work with. Communication is a fundamental skill for designers.'),
], 'DESIGN DOES NOT HAPPEN IN A VACUUM',
    'Involving people from different disciplines helps you develop better designs and move your ideas forward.',
    'Stakeholder management is important throughout the whole Double Diamond process. Design does not happen in a vacuum. In industry, whatever the design discipline, you will deal with different people. Users are central, but collaboration with other designers, engineers and product managers is also fundamental. During Discover, you work mostly with users and share findings with managers. During Define, you may work with other designers, developers or managers to narrow down the problem. During Develop, co-design helps you learn from different perspectives. During Deliver, users test the experience, and you communicate the findings to developers, engineers and managers. Communication is a fundamental skill for designers and an important part of your professional skillset. The following four-phase case explains the existing analytical laboratory software project. The case ends with three concept slides showing a proposed AI redesign.'))

case_cover = _slide(INK, title=CASE_TITLE, notes=
    'The case study is titled '+CASE_TITLE+'. It follows Discover, Define, Develop and Deliver using the supplied portfolio pages. The seven content slides have eight speaking minutes including one complete original video pass, followed by two minutes of Q&A within ten minutes. The cover is included in Discover\'s one-minute-and-fifteen-second allocation. The introduction remains separate, with its duration open. The four phase slides present the existing product; the following three ASL slides present the proposed AI redesign, not validated capabilities.')
case_cover.els += [eyebrow(120, 360, 'CASE STUDY', '#F2ECF5'),
                   T(120, 460, 1680, 330, CASE_TITLE, 'black', 112, '#FFFFFF',
                     lh=.97, spc=-.035, name='case-cover-title'),
                   T(120, 870, 1680, 60, 'discover / define / develop / deliver',
                     'mono', 26, '#F2ECF5', lh=1.2)]
S.append(case_cover)
S.extend(build_case())
intro_cover = _slide(INK, title='Double Diamond \U0001f48e\U0001f48e', notes=
    'Opening cover for the Double Diamond introduction. The requested title is Double Diamond \U0001f48e\U0001f48e. The following slide retains the verbatim definition and official diagram; the cover does not replace that explanation or add speaking time to the case.')
# A course-owned emoji twin avoids missing glyphs in native raster/PPTX exports.
emoji_png = Path(__file__).resolve().parent/'assets/week10/nicolo-cover-diamonds.png'
emoji_data = base64.b64encode(emoji_png.read_bytes()).decode('ascii')
emoji_svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="272" height="128" '
             'role="img" aria-label="\U0001f48e\U0001f48e"><title>\U0001f48e\U0001f48e</title>'
             '<image width="272" height="128" href="data:image/png;base64,'+emoji_data+'"/></svg>')
intro_cover.els += [T(120, 440, 900, 200, 'Double Diamond',
                      'black', 112, '#FFFFFF', lh=1.05, spc=-.025,
                      name='dd-cover-title'),
                   Figure(1004, 440, 272, 128, emoji_svg, str(emoji_png),
                          name='dd-cover-diamonds')]
S.insert(0, intro_cover)
closing = _slide(title='thanks!', chrome=False, notes=
    'A simple closing slide after the proposed AI concept. Invite questions within the existing two-minute Q&A allowance. The separate four-TA ClassPoint Q&A deck can be used for collecting audience questions; this closing slide itself has no collection.')
closing.els.append(T(120, 490, 1680, 100, 'thanks!', 'body', 48, INK,
                     align='c', valign='m', name='closing-thanks'))
S.append(closing)
finalize(S, 'Double Diamond')
for slide in S[CASE_START-1:-1]:
    footer = next(e for e in slide.els if e.name == 'chrome-footer')
    footer.paras[0].runs[0].text = CASE_TITLE

DECK = dict(title='SD2112 / Double Diamond / '+CASE_TITLE,
            slides=S, pdf='SD2112-week10-nicolo.pdf')
