"""Source-led product case and three contributor-supplied proposed AI concepts."""
from pathlib import Path

from deckgen import INK, PAPER, Image
from deckgen.figures import Canvas
from deckgen.layouts import T, Rect, Figure, _slide, eyebrow, live, place_sketch
import week10_figures as F
from week10_nicolo_figures import phase_map, PHASE_NAMES
from week10_nicolo_media import PRODUCT_VIDEO

CASE_TITLE = 'UX Design for Analytical Laboratory Software'
CASE_SPEAKING_MINUTES = [1.25, 1, 1.25, 2, .5, .75, 1.25]
CASE_QA_MINUTES = 2
SCREEN_RATIO = 2420/1525
ASSETS = Path(__file__).resolve().parent/'assets/week10'
PRODUCT_SCREEN = ASSETS/'nicolo-current-product.png'
SCREEN_CAPTION = 'Workbench Tablet Device'
TEAL, GREY, ORANGE = '#246E70', '#5A626B', '#C74600'
PAPER_STEPS = [
    'Find the right sample in the sample rack by checking labels',
    'Note down the sample container on the lab notebook',
    'Assign a new label to an empty container',
    'Note down target sample container on the lab notebook',
    'Pipette sample from source container to target container',
]
POSITIVE_QUOTES = [
    'The system is quite fast',
    'I like that I can see the history of any sample I scan',
    'It\u2019s self-explanatory',
]
WISH_QUOTES = [
    'I would like to be able to add weight and volume information to the container',
    'I would like to have the possibility to split and merge samples in the system',
]


def case_frame(index, context, notes):
    phase = PHASE_NAMES[index]
    s = _slide(title=phase.title()+' / '+context, notes=notes)
    svg, png = phase_map(phase)
    s.els += [eyebrow(120, 96, 'CASE STUDY / '+context.upper(), TEAL),
              T(120, 184, 1200, 100, phase.title(), 'xbold', 88, INK,
                lh=.95, spc=-.03, name='variant-heading'),
              Figure(1440, 164, 360, 176, svg, png, name='phase-navigation')]
    return s


def paper_return():
    c = Canvas(1680, 20)
    c.svg.append('<title>Repeat the paper-based transfer workflow from the first step</title>')
    c.line(1528, 1, 1528, 14, GREY, 2)
    c.line(1528, 14, 152, 14, GREY, 2)
    c.line(152, 14, 152, 2, GREY, 2)
    c.poly([(146, 8), (152, 1), (158, 8)], GREY)
    return c.finish('week10-nicolo-paper-return')


def build_case():
    slides = []
    s = case_frame(0, 'Background',
        'Proposed speaking allocation: one minute and fifteen seconds, including the case cover. '
        'Source: 3.pdf and 5.pdf, PDF page 1 in each. Target User: Inexperienced Lab Analyst. '
        'Sample transfers using paper or digital systems often lead to cumbersome workflows and transcription errors. '
        'The five paper-based steps reproduce the source wording and order: '+'; '.join(PAPER_STEPS)+'. '
        'The return arrow preserves the source diagram\'s repetition for the next sample. '
        'The laboratory photograph is the original embedded photograph from 5.pdf, not a generated reconstruction. '
        'This is the existing project context, not an AI redesign or evidence of a measured error reduction. '
        'Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; Discover highlighted.')
    s.els += [Image(120, 350, 440, 293, str(ASSETS/'nicolo-lab-context.jpg'), 'contain',
                    name='portfolio-lab-photo'),
              T(640, 350, 1160, 32, 'Target User', 'mono', 22, ORANGE),
              T(640, 398, 1160, 70, 'Inexperienced Lab Analyst', 'xbold', 44, INK),
              T(640, 484, 1160, 80,
                'Sample transfers using paper or digital systems often lead to:',
                'body', 32, INK, lh=1.2, name='transfer-problem-context'),
              T(640, 568, 1160, 90, 'Cumbersome workflows\nTranscription errors',
                'xbold', 36, INK, lh=1.15, name='transfer-problem-labels'),
              T(120, 712, 1680, 30, 'Paper-based', 'mono', 22, TEAL,
                name='paper-workflow-heading')]
    for i, step in enumerate(PAPER_STEPS):
        x = 120+i*344
        s.els += [T(x, 754, 304, 26, f'{i+1:02d}', 'mono', 20, ORANGE),
                  T(x, 794, 304, 116, step, 'body', 26, INK, lh=1.2,
                    name=f'paper-step-{i+1}')]
        if i < 4:
            s.els.append(T(x+310, 832, 30, 44, '\u2192', 'body', 28, GREY))
    svg, png = paper_return()
    s.els.append(Figure(120, 928, 1680, 20, svg, png, name='paper-workflow-return'))
    slides.append(s)

    s = case_frame(1, 'Leading principles',
        'Proposed speaking allocation: one minute. Source: 7.pdf, PDF page 1. '
        'The three guiding principles and their evaluation dimensions are preserved. '
        'Streamline interactions: How to remove non-essential interactions with the software that add unnecessary effort? '
        'Task Completion Rate. Fit into current workflows: How to fit the new software experience into current workflows without disrupting them? '
        'Ease of use and Time on Task. Provide a clear information system on tracked samples: '
        'How to present the most crucial information without the need of additional interactions? Task Completion Rate. '
        'These are leading principles and evaluation dimensions, not claims that every metric improved. '
        'Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; Define highlighted.')
    principles = [
        ('Streamline interactions',
         'How to remove non-essential interactions with the software that add unnecessary effort?',
         'Task Completion Rate'),
        ('Fit into current workflows',
         'How to fit the new software experience into current workflows without disrupting them?',
         'Ease of use / Time on Task'),
        ('Provide a clear information system on tracked samples',
         'How to present the most crucial information without the need of additional interactions?',
         'Task Completion Rate'),
    ]
    for i, (title, question, metric) in enumerate(principles):
        x = 120+i*580
        s.els += [Rect(x, 350, 520, 2, '#BBBCB9'),
                  T(x, 382, 520, 30, f'{i+1:02d}', 'mono', 22, ORANGE),
                  T(x, 442, 520, 170, title, 'xbold', 38, INK, lh=1.08),
                  T(x, 646, 520, 174, question, 'body', 29, INK, lh=1.25),
                  T(x, 870, 520, 56, metric, 'mono', 22, TEAL,
                    name=f'principle-metric-{i+1}')]
    slides.append(s)

    s = case_frame(2, 'Re-thinking input devices',
        'Proposed speaking allocation: one minute and fifteen seconds. Sources: 8.pdf and 9.pdf, PDF page 1 in each. '
        'Re-thinking input devices: How to streamline the interactions at the lab bench? '
        'Barcode scanner as primary input. Using barcode scanner inputs to change the focus automatically to the next input field in the UI. '
        'The source schematic links Human, Input Devices, Physical Assets and Computer, de-emphasizing touch and mouse inputs. '
        'Single Transfer (Tablet Redesign): Iteration 2 - Predefined sample list. The pictured screen is the actual historical first draft, not the current product or an AI redesign. '
        'Sequential constraints: Caused additional time spent in searching for the next sample in the rack, nullifying the gain in efficiency. '
        'Higher risk of mistakes: no validation on the source container. '
        'For an ideal UX, the software should adapt to the user\u2019s actions and mental patterns, and not the other way around. '
        'The original magenta arrows show imposed field order; the task and sample names are source placeholders, not real laboratory records. '
        'Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; Develop highlighted.')
    s.els += [T(120, 350, 800, 54, 'Re-thinking input devices', 'xbold', 40, INK),
              T(120, 424, 800, 80, 'How to streamline the interactions at the lab bench?',
                'body', 30, INK, lh=1.2),
              T(120, 520, 800, 88, 'Barcode scanner as primary input', 'xbold', 36, INK,
                lh=1.08),
              T(120, 624, 800, 120,
                'Using barcode scanner inputs to change the focus automatically to the next input field in the UI.',
                'body', 31, INK, lh=1.22),
              T(120, 778, 800, 30, 'Sequential constraints / First Draft', 'mono', 22, ORANGE,
                name='draft-constraints-caption'),
              T(120, 826, 800, 112,
                'Additional time spent searching for the next sample.\nNo validation on the source container.',
                'body', 27, INK, lh=1.2, name='draft-constraints-body'),
              T(1000, 350, 800, 40, 'Iteration 2 - Predefined sample list', 'mono', 23, TEAL),
              Image(1000, 400, 780, round(780*1072/1700),
                    str(ASSETS/'nicolo-predefined-list-draft.png'), 'contain',
                    name='portfolio-predefined-list-draft'),
              T(1000, 916, 780, 78,
                'For an ideal UX, the software should adapt to the user\u2019s actions and mental patterns, and not the other way around.',
                'body', 22, INK, lh=1.1, name='ideal-ux-principle')]
    slides.append(s)

    notes = (
        'Proposed speaking allocation: two minutes, including one complete 49.365-second video pass. The video starts automatically, muted, and loops until paused; Space toggles playback. '
        'Sources: 16.pdf and 17.pdf, PDF page 1 in each, plus the original screenshot and promotional video supplied earlier. '
        'Gather qualitative data on the experience: Ease of use and Learnability. Task-based usability testing with a follow up semi-structured interview. '
        'Positive participant quotations: '+'; '.join(POSITIVE_QUOTES)+'. '
        'Improvement wishes, not implemented capabilities: '+'; '.join(WISH_QUOTES)+'. '
        'The projected wishes shorten the introductory words but retain the requested capabilities; all complete quotations are preserved here. '
        'Gather measurable gains in efficiency and speed: Number of Clicks and Time on Task. '
        '16.pdf calls this comparative testing with manual and digital workflow; 17.pdf calls it Comparative Testing between Manual and Automated Workflow. '
        'Reported portfolio outcomes: 30% faster than manual workflows (Time on Task); 1 Click to prepare and submit a sample list. '
        'These are reported current-product outcomes, not results of the AI redesign. Do not conflate 30% faster with 30% less completion time. '
        'Participant count, task/sample count, raw timings, baseline click count, study date, uncertainty and calculation method are not supplied; do not invent them. '
        'The one-click statement is limited to preparing and submitting a sample list, not the whole sample-transfer workflow. '
        'The original tablet screenshot remains uncropped at its 2420:1525 aspect ratio. The original 1920x1080 video remains complete, silent, untrimmed, autoplaying silently and looping continuously until paused. Space toggles play/pause. '
        'Both are on this Deliver slide, replacing the earlier dedicated video slide to meet the four-slide case request. '
        'The seven case-content slides total eight speaking minutes including one full video pass, followed by two minutes of Q&A within ten minutes. Pause the loop after one pass to preserve that budget. '
        'The following three slides present the supplied AI redesign as a proposed concept, not an implemented or validated system. '
        'Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; Deliver highlighted.')
    s = case_frame(3, 'Validating the Experience', notes)
    s.els += [Image(120, 350, 580, round(580/SCREEN_RATIO), str(PRODUCT_SCREEN), 'contain',
                    name='current-product-screenshot'),
              T(120, 730, 580, 56, SCREEN_CAPTION, 'mono', 20, TEAL,
                lh=1.15, name='current-product-caption')]
    place_sketch(s, live('nicolo-product-video', PRODUCT_VIDEO, 1920, 1080),
                 (900, 350, 720, 405),
                 F.source_image('nicolo-product-video-poster.png',
                                'Original product promotional video, still at 25 seconds'))
    s.els += [T(120, 812, 500, 28, 'Quantitative findings', 'mono', 20, ORANGE),
              T(120, 854, 144, 54, '30%', 'xbold', 44, TEAL, name='reported-speed'),
              T(284, 854, 336, 60, 'faster than manual workflows', 'body', 25, INK,
                lh=1.15),
              T(120, 922, 148, 44, '1 Click', 'xbold', 36, TEAL, name='reported-clicks'),
              T(284, 918, 336, 54, 'to prepare and submit a sample list', 'body', 24, INK,
                lh=1.1),
              T(700, 812, 500, 28, 'Qualitative findings', 'mono', 20, ORANGE),
              T(700, 856, 500, 138,
                '\n'.join('\u201c'+q+'\u201d' for q in POSITIVE_QUOTES),
                'body', 25, INK, lh=1.08, italic=True, name='participant-positive-quotes'),
              T(1280, 812, 520, 28, 'Improvement wishes', 'mono', 20, ORANGE),
              T(1280, 856, 520, 138,
                'Add weight and volume information to the container.\nSplit and merge samples in the system.',
                'body', 26, INK, lh=1.15, name='participant-improvement-wishes')]
    quotes = next(e for e in s.els if e.name == 'participant-positive-quotes')
    for paragraph in quotes.paras[1:]:
        paragraph.before = 10
    slides.append(s)
    slides.extend(build_ai_concept())
    return slides


def build_ai_concept():
    concepts = [
        ('ASL-1', 'Mirror-like UI with overlays',
         'Mirror-like UI with overlays.',
         'A live camera view with interface elements overlaid on the workbench view.',
         'Computer Vision (CV / CNN)',
         'Recognise containers and actions in the camera view.'),
        ('ASL-2', 'Automatic sample selection',
         'AI automatically selects the sample in the UI based on the recognised barcode and container type.',
         'The selected sample and its transfer history remain visible alongside the container.',
         'Computer Vision + barcode decoding',
         'Recognise the container type and decode its barcode to identify the sample.'),
        ('ASL-3', 'Registering the transfer',
         'AI recognises dispensing into the vial and registers the transfer in the transfer history.',
         'A comment on the sample is also added. The user can edit it with voice recognition.',
         'Vision Language Model + Voice Recognition',
         'Draft sample comments with a VLM. Use voice recognition + function calling to control the software and edit AI-generated data.'),
    ]
    slides = []
    for i, (code, title, body, detail, technology, explanation) in enumerate(concepts, 1):
        notes = (
            f'Proposed speaking allocation: {CASE_SPEAKING_MINUTES[i+3]:g} minutes. '
            f'{code}: {body} {detail} AI technologies: {technology}. {explanation} '
            'Source: the contributor-supplied ASL concept image and explanation, 4 November 2026. '
            'This is a proposed AI redesign illustrated by a static mockup, not a working system, validated outcome or current-product capability. '
            'The proposed experience aims to fit the software to the analyst\'s actions, reduce manual selection and preserve a visible sample history. '
            'Computer Vision can include CNN-based container/action recognition; decoding a barcode does not inherently require a CNN. '
            'Camera use, privacy, low light, occlusion, reflections, local processing power and integration with existing laboratory systems need site-specific assessment. '
            'Recognising a likely dispensing action does not verify successful transfer, correct volume, chemical identity, purity or absence of contamination. '
            'Source-target association, duplicate-event prevention and confirmation/correction for uncertain events must be designed and tested. '
            'VLM comments are editable draft visual observations, not scientific conclusions. The ASL-3 mockup\'s recommendation requiring additional processing is unvalidated and must not be treated as a laboratory instruction. '
            'Voice recognition transcribes the user; function calling requests validated software actions with appropriate user control. '
            'A manual correction path and traceable edits are needed. Evaluate with actual analysts in the actual workbench context before claiming an efficiency or accuracy improvement.'
        )
        s = _slide(title=code+' / '+title, notes=notes)
        s.els += [eyebrow(120, 96, 'PROPOSED AI REDESIGN / '+code, TEAL),
                  T(120, 184, 1680, 100, title, 'xbold', 64, INK,
                    lh=.95, spc=-.03, name='variant-heading'),
                  Image(120, 330, 1040, round(1040/SCREEN_RATIO),
                        str(ASSETS/f'nicolo-asl-{i}.png'), 'contain', name=f'asl-{i}-concept'),
                  T(1220, 344, 580, 168, body, 'xbold', 34, INK, lh=1.14,
                    name='concept-explanation'),
                  T(1220, 532, 580, 128, detail, 'body', 29, INK, lh=1.2),
                  Rect(1220, 696, 580, 2, '#BBBCB9'),
                  T(1220, 722, 580, 28, 'AI technologies', 'mono', 21, ORANGE),
                  T(1220, 772, 580, 76, technology, 'xbold', 28, TEAL, lh=1.14),
                  T(1220, 868, 580, 126, explanation, 'body', 25, INK, lh=1.2)]
        slides.append(s)
    return slides
