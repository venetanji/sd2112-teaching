"""Week 10 authentic source-image embedding and retained framework adaptation."""
from deckgen.figures import Canvas
from deckgen.core import pil_font
from pathlib import Path
from base64 import b64encode
from html import escape
from PIL import Image as PILImage


def source_image(filename, description):
    """Embed the same unmodified source pixels in HTML and native previews."""
    path = Path(__file__).resolve().parent / 'assets' / 'week10' / filename
    with PILImage.open(path) as image:
        w, h = image.size
    encoded = b64encode(path.read_bytes()).decode('ascii')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" '
           f'viewBox="0 0 {w} {h}" role="img" aria-label="{escape(description)}">'
           f'<title>{escape(description)}</title>'
           f'<image width="{w}" height="{h}" href="data:image/png;base64,{encoded}"/>'
           '</svg>')
    return svg, str(path)


def diamond():
    c = Canvas(1680, 540, bg='#F4F4F2')
    def label(x, cy, text, size=32, color='#000B1C'):
        f = pil_font('semibold', round(c.s(size)))
        top, bottom = f.getbbox(text)[1::2]
        baseline = cy + (f.getmetrics()[0] - (top + bottom) / 2) / c.s(1)
        c.text(x, baseline, text, size=size, color=color, weight=600, anchor='middle')
    for x in (80, 850):
        for a, b in [((x, 255), (x+350, 80)), ((x+350, 80), (x+700, 255)),
                     ((x+700, 255), (x+350, 430)), ((x+350, 430), (x, 255))]:
            c.line(*a, *b, '#246E70', 7)
        c.line(x+350, 93, x+350, 417, '#BBBCB9', 2)
    for x, phase, detail in [(255, 'DISCOVER', 'Explore evidence'), (605, 'DEFINE', 'Focus the question'),
                              (1025, 'DEVELOP', 'Explore responses'), (1375, 'DELIVER', 'Test and improve')]:
        label(x, 230, phase, 30)
        label(x, 277, detail, 20)
    label(430, 35, 'PROBLEM SPACE', 26)
    label(1200, 35, 'SOLUTION SPACE', 26)
    label(840, 495, 'Open up possibilities. Focus a decision. Return when evidence changes.', 29)
    return c.finish('week10-double-diamond')


# Week-owned grid follows the approved Week 8 paper title and label spacing.
from deckgen import INK
from deckgen.layouts import T, Image, _slide, eyebrow


def paper_frame(heading, phase, notes):
    s = _slide('#FFFFFF', notes, title=heading)
    s.els += [eyebrow(120, 96, phase, '#246E70'),
              T(120, 184, 1680, 140, heading, 'xbold', 72, INK,
                lh=.95, spc=-.03, name='paper-title')]
    return s


def paper_block(s, x, y, width, label, value, height, name):
    s.els += [T(x, y, width, 34, label, 'mono', 23, '#246E70', name=name+'-label'),
              T(x, y+52, width, height, value, 'body', 34, INK,
                lh=1.2, name=name+'-body')]


def study_setup(url, notes):
    s = paper_frame('Where did designers use AI?',
                    'OPTIONAL CONTEXT / AI AS A DESIGN TOOL / 2026 PUBLICATION', notes)
    paper_block(s, 120, 348, 780, 'WHAT THEY DID',
                '88 AI-user survey responses in Türkiye; 10 selected professionals then designed a lunchbox while thinking aloud, using tools they chose.',
                215, 'study-task')
    paper_block(s, 120, 676, 780, 'WHAT THEY COMPARED',
                'Reported uses and observed design activities, mapped to four phases. This was not an AI/no-AI causal trial.',
                190, 'study-comparison')
    paper_block(s, 1020, 348, 780, 'ADAPTED FROM THE STUDY / TASK',
                'Develop a user persona and a lunchbox concept. Consider food types, compartments, lids and locks; explain your decisions as you work.',
                215, 'study-example')
    paper_block(s, 1020, 676, 780, 'WHAT THEY RECORDED',
                'Which tools were used for which functions, and how designers worked with them. Tool use: 2024; not a 2026 product test.',
                190, 'study-measurement')
    s.els.append(T(120, 956, 1680, 38,
                   f'[Sözen & Börekçi (2026), AI EDAM 40, e9 / methods pp.4-7]({url})',
                   'mono', 21, INK, lh=1.1, name='paper-citation'))
    return s


def study_result(url, notes):
    s = paper_frame('Both problem and solution work.',
                    'OPTIONAL CONTEXT / NOT A STUDY OF AI-ENABLED PRODUCTS', notes)
    asset = Path(__file__).resolve().parent/'assets'/'week10'/'sozen-borekci-2026-fig5-overview.png'
    s.els.append(Image(120, 348, 1010, 430, str(asset), 'contain',
                       name='paper-figure', url=url))
    paper_block(s, 1190, 348, 610, 'WHAT THEY FOUND',
                'AI appeared in problem exploration as well as ideas, evaluation and presentation.',
                170, 'study-result')
    paper_block(s, 1190, 632, 610, 'WHAT IT DOES NOT SHOW',
                'No proof of better designs or saved time. Selected AI users; not all designers.',
                170, 'study-limit')
    s.els += [T(120, 806, 1010, 118,
                'Read left to right across four phases. Widths are neither time shares nor participant counts. Consider alternatives; verify user needs.',
                'body', 30, INK, lh=1.2, name='figure-reading'),
              T(120, 956, 1680, 38,
                f'[Sözen & Börekçi (2026), Fig. 5, p. 16]({url}) / CC BY 4.0. Top-panel crop; no redraw.',
                'mono', 21, INK, lh=1.1, name='paper-citation')]
    return s


def mediation_checkpoint(url, notes):
    s = paper_frame('Can the person say no?',
                    'SAME DEVELOP BLOCK / VERBEEK (2015) / CONCEPTUAL LENS', notes)
    paper_block(s, 120, 348, 780, 'THE ARGUMENT / NOT A PARTICIPANT STUDY',
                'Technology helps shape what people notice, understand and do. A product is not just a neutral channel for a fixed intention.',
                215, 'concept-argument')
    paper_block(s, 1020, 348, 780, 'OUR EXAMPLE / NOT FROM THE ESSAY',
                'A cafe recommendation makes one option prominent. Other options and the reasons for choosing them can become harder to notice.',
                215, 'concept-example')
    paper_block(s, 120, 676, 780, 'TRY IN YOUR PROTOTYPE',
                'Make correction, rejection and a non-AI route findable. Who must notice a bad suggestion, and how can they recover?',
                190, 'concept-application')
    paper_block(s, 1020, 676, 780, 'WHAT THIS DOES NOT ESTABLISH',
                'These are design hypotheses, not proven safeguards. An override button alone does not settle the consequences of a design.',
                190, 'concept-limit')
    s.els.append(T(120, 956, 1680, 38,
                   f'[Verbeek (2015), Beyond Interaction / pp.28-31]({url})',
                   'mono', 21, INK, lh=1.1, name='paper-citation'))
    return s
