"""Four reorderable, optional audience Q&A collections, separate from TA talks."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import INK, WHITE, PAPER, attach_reports
from deckgen.layouts import Image, Rect, T, _slide, eyebrow, finalize
from course import footer

JOIN_URL = 'https://www.classpoint.app/'
JOIN_QR = 'week10/qa-classpoint-join.png'
REPORTS = Path(__file__).resolve().parent / 'week10_qa-reports.json'
# File order is navigation only, not an agreed speaking rota.
SPEAKERS = ('Nicol\u00f2 Azzolin', 'Amber', 'WU Zhao', 'MA Jie')
ACCENTS = ('#246E70', '#C74600', '#146AB5', '#00544C')
S = []


def audience_questions(name, accent):
    prompt = f'Questions for {name}'
    s = _slide(WHITE, title=prompt,
               cp={'type': 'short_answer', 'hide_names': False, 'multiple': True},
               notes=(f'After {name}\'s presentation, open this speaker\'s Short Answer activity '
                      'with the real ClassPoint button in PowerPoint Slide Show. Participation '
                      'is optional and not graded; audience members may send more than one '
                      'question, one question per submission. No anonymity is promised: names '
                      'may be visible to the presenter and in reports. Ask about the work, '
                      'not private or identifying information. The static QR opens only '
                      f'{JOIN_URL}; announce/show the current class code from the actual '
                      'ClassPoint presenter session. This file contains no live code. '
                      'Close collection and select relevant questions for discussion; do not '
                      'award stars or use quiz/grading controls. Reorder the four slides to '
                      'match the confirmed presentations; the source order is not a speaking '
                      'agreement. Review any responses before displaying or sharing them. '
                      'Follow lessons/week10-qa-presenter-guide.md for the add-in smoke test '
                      'and report mapping; native tag verification is not a live submission test.'))
    s.els += [
        eyebrow(120, 96, 'WEEK 10 / AUDIENCE Q&A / SHORT ANSWER', '#5C6470',
                name='question-eyebrow'),
        T(120, 196, 1120, 50, 'Questions for', 'body', 38, '#5C6470', lh=1.2),
        T(120, 268, 1120, 130, name, 'black', 92, INK, lh=.98, spc=-.035,
          name='qa-speaker'),
        Rect(120, 430, 1080, 5, accent, name='qa-accent'),
        T(120, 484, 1080, 180, 'What would you\nlike to ask?', 'xbold', 78, INK,
          lh=1.02, spc=-.025),
        T(120, 714, 1080, 96, 'Optional. Not graded.\nOne question per response; send more if you wish.',
          'body', 32, INK, lh=1.35, name='qa-participation'),
        T(120, 848, 1080, 80, 'Names may be visible.\nKeep questions about the work, not private details.',
          'body', 28, '#5C6470', lh=1.35, name='qa-privacy'),
        Rect(1270, 240, 530, 615, PAPER, name='qa-join-panel'),
        T(1300, 266, 470, 48, 'SCAN TO JOIN', 'monomed', 25, accent,
          lh=1.2, align='c', spc=.1),
        Image(1340, 330, 390, 390, JOIN_QR, 'contain',
              name='qa-join-qr', url=JOIN_URL),
        T(1300, 734, 470, 42, f'[classpoint.app]({JOIN_URL})', 'body', 28, INK,
          lh=1.2, align='c', name='qa-join-link'),
        T(1300, 788, 470, 56, 'Enter the live class code\nshown by the presenter.',
          'body', 23, '#5C6470', lh=1.2, align='c', name='qa-live-code'),
    ]
    return s


for speaker, accent in zip(SPEAKERS, ACCENTS):
    S.append(audience_questions(speaker, accent))

attach_reports(S, REPORTS)
DECK = dict(title='SD2112 / Week 10 / Audience Q&A',
            slides=finalize(S, footer(10)), pdf='SD2112-week10-qa.pdf')
