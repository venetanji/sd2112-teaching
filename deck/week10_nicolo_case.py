"""Four-phase account of the existing product, from the supplied portfolio pages."""
from pathlib import Path

from deckgen import INK, PAPER, Image
from deckgen.figures import Canvas
from deckgen.layouts import T, Rect, Figure, _slide, eyebrow, live, place_sketch
import week10_figures as F
from week10_nicolo_figures import phase_map, phase_subtitle, PHASE_NAMES
from week10_nicolo_media import PRODUCT_VIDEO

CASE_TITLE = 'UX Design for Analytical Laboratory Software'
CASE_SPEAKING_MINUTES = [2, 1.5, 2, 2.5]
CASE_QA_MINUTES = 2
SCREEN_RATIO = 2420/1525
ASSETS = Path(__file__).resolve().parent/'assets/week10'
PRODUCT_SCREEN = ASSETS/'nicolo-current-product.png'
SCREEN_CAPTION = 'Original Software Product / Workbench Tablet Device'
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
    space = 'problem space' if index < 2 else 'solution space'
    width, subtitle_svg, subtitle_png = phase_subtitle(space, phase)
    svg, png = phase_map(phase)
    s.els += [eyebrow(120, 96, 'CASE STUDY / '+context.upper(), TEAL),
              T(120, 184, 1200, 100, phase.title(), 'xbold', 88, INK,
                lh=.95, spc=-.03, name='variant-heading'),
              Figure(120, 306, width, 48, subtitle_svg, subtitle_png,
                     name='phase-subtitle'),
              Figure(1440, 210, 360, 176, svg, png, name='phase-navigation')]
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
        'Proposed speaking allocation: two minutes, including the case cover. '
        'Source: 3.pdf and 5.pdf, PDF page 1 in each. Target User: Inexperienced Lab Analyst. '
        'Sample transfers using paper or digital systems often lead to cumbersome workflows and transcription errors. '
        'The five paper-based steps reproduce the source wording and order: '+'; '.join(PAPER_STEPS)+'. '
        'The return arrow preserves the source diagram\'s repetition for the next sample. '
        'The laboratory photograph is the original embedded photograph from 5.pdf, not a generated reconstruction. '
        'This is the existing project context, not an AI redesign or evidence of a measured error reduction. '
        'Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; Discover highlighted.')
    s.els += [Image(120, 430, 500, 333, str(ASSETS/'nicolo-lab-context.jpg'), 'contain',
                    name='portfolio-lab-photo'),
              T(700, 414, 1100, 32, 'Target User', 'mono', 22, ORANGE),
              T(700, 466, 1100, 70, 'Inexperienced Lab Analyst', 'xbold', 44, INK),
              T(700, 560, 1100, 90,
                'Sample transfers using paper or digital systems often lead to:',
                'body', 32, INK, lh=1.2),
              T(700, 680, 1100, 90, 'Cumbersome workflows\nTranscription errors',
                'xbold', 36, INK, lh=1.15),
              T(120, 796, 1680, 30, 'Paper-based', 'mono', 22, TEAL)]
    for i, step in enumerate(PAPER_STEPS):
        x = 120+i*344
        s.els += [T(x, 834, 304, 26, f'{i+1:02d}', 'mono', 20, ORANGE),
                  T(x, 874, 304, 96, step, 'body', 24, INK, lh=1.2,
                    name=f'paper-step-{i+1}')]
        if i < 4:
            s.els.append(T(x+310, 894, 30, 44, '\u2192', 'body', 28, GREY))
    svg, png = paper_return()
    s.els.append(Figure(120, 974, 1680, 20, svg, png, name='paper-workflow-return'))
    slides.append(s)

    s = case_frame(1, 'Leading principles',
        'Proposed speaking allocation: one and a half minutes. Source: 7.pdf, PDF page 1. '
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
        s.els += [Rect(x, 416, 520, 2, '#BBBCB9'),
                  T(x, 442, 520, 30, f'{i+1:02d}', 'mono', 22, ORANGE),
                  T(x, 500, 520, 170, title, 'xbold', 38, INK, lh=1.08),
                  T(x, 700, 520, 174, question, 'body', 29, INK, lh=1.25),
                  T(x, 912, 520, 56, metric, 'mono', 22, TEAL,
                    name=f'principle-metric-{i+1}')]
    slides.append(s)

    s = case_frame(2, 'Re-thinking input devices',
        'Proposed speaking allocation: two minutes. Sources: 8.pdf and 9.pdf, PDF page 1 in each. '
        'Re-thinking input devices: How to streamline the interactions at the lab bench? '
        'Barcode scanner as primary input. Using barcode scanner inputs to change the focus automatically to the next input field in the UI. '
        'The source schematic links Human, Input Devices, Physical Assets and Computer, de-emphasizing touch and mouse inputs. '
        'Single Transfer (Tablet Redesign): Iteration 2 - Predefined sample list. The pictured screen is the actual historical first draft, not the current product or an AI redesign. '
        'Sequential constraints: Caused additional time spent in searching for the next sample in the rack, nullifying the gain in efficiency. '
        'Higher risk of mistakes: no validation on the source container. '
        'For an ideal UX, the software should adapt to the user\u2019s actions and mental patterns, and not the other way around. '
        'The original magenta arrows show imposed field order; the task and sample names are source placeholders, not real laboratory records. '
        'Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; Develop highlighted.')
    s.els += [T(120, 414, 800, 54, 'Re-thinking input devices', 'xbold', 40, INK),
              T(120, 494, 800, 86, 'How to streamline the interactions at the lab bench?',
                'body', 30, INK, lh=1.2),
              T(120, 608, 800, 92, 'Barcode scanner as primary input', 'xbold', 36, INK,
                lh=1.08),
              T(120, 730, 800, 142,
                'Using barcode scanner inputs to change the focus automatically to the next input field in the UI.',
                'body', 31, INK, lh=1.22),
              T(1000, 414, 800, 40, 'Iteration 2 - Predefined sample list', 'mono', 23, TEAL),
              Image(1000, 464, 600, round(600*1072/1700),
                    str(ASSETS/'nicolo-predefined-list-draft.png'), 'contain',
                    name='portfolio-predefined-list-draft'),
              T(1000, 846, 800, 26, 'Sequential constraints / First Draft', 'mono', 18, ORANGE),
              T(1000, 880, 800, 50,
                'Additional time spent searching for the next sample.\nNo validation on the source container.',
                'body', 22, INK, lh=1.12),
              Rect(120, 938, 1680, 56, PAPER, name='case-principle-strip'),
              T(140, 944, 1640, 46,
                'For an ideal UX, the software should adapt to the user\u2019s actions and mental patterns, and not the other way around.',
                'body', 22, INK, lh=1.04)]
    slides.append(s)

    notes = (
        'Proposed speaking allocation: two and a half minutes, including the complete 49.365-second video. '
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
        'The original tablet screenshot remains uncropped at its 2420:1525 aspect ratio. The original 1920x1080 video remains complete, silent, untrimmed, without autoplay or looping. '
        'Both are on this Deliver slide, replacing the earlier dedicated video slide to meet the four-slide case request. '
        'The four case slides total eight speaking minutes including this full video, followed by two minutes of Q&A within ten minutes. '
        'The earlier unfilled AI-redesign placeholders are deferred for now, not presented as completed work. '
        'Navigation map: simplified redraw after Design Council, The Double Diamond, CC BY 4.0; Deliver highlighted.')
    s = case_frame(3, 'Validating the Experience', notes)
    s.els += [T(120, 392, 650, 28, 'Validating the Experience', 'mono', 20, ORANGE),
              Image(120, 428, 650, round(650/SCREEN_RATIO), str(PRODUCT_SCREEN), 'contain',
                    name='current-product-screenshot'),
              T(120, 850, 650, 56, SCREEN_CAPTION, 'mono', 20, TEAL,
                lh=1.15, name='current-product-caption'),
              T(120, 914, 650, 26, 'Ease of use / Learnability', 'mono', 20, ORANGE),
              T(120, 946, 650, 48,
                'Task-based usability testing with a follow up semi-structured interview',
                'body', 20, INK, lh=1.15)]
    place_sketch(s, live('nicolo-product-video', PRODUCT_VIDEO, 1920, 1080,
                         hint='Play the original 49-second product video'),
                 (820, 428, 544, 306),
                 F.source_image('nicolo-product-video-poster.png',
                                'Original product promotional video, still at 25 seconds'))
    s.els += [T(820, 748, 550, 26, 'Original video / 49 seconds / no audio', 'mono', 18, TEAL),
              T(820, 790, 440, 28, 'Qualitative findings', 'mono', 20, ORANGE),
              T(820, 834, 440, 142,
                '\n'.join('\u201c'+q+'\u201d' for q in POSITIVE_QUOTES),
                'body', 24, INK, lh=1.15, name='participant-positive-quotes'),
              T(1330, 790, 470, 28, 'Improvement wishes', 'mono', 20, ORANGE),
              T(1330, 834, 470, 142,
                'Add weight and volume information to the container.\nSplit and merge samples in the system.',
                'body', 24, INK, lh=1.15, name='participant-improvement-wishes'),
              T(1440, 414, 360, 88, '30%', 'xbold', 72, TEAL,
                name='reported-speed'),
              T(1440, 510, 360, 66, 'faster than\nmanual workflows', 'body', 26, INK,
                lh=1.12),
              T(1440, 582, 360, 26, 'Time on Task', 'mono', 18, GREY),
              T(1440, 622, 360, 84, '1 Click', 'xbold', 64, TEAL,
                name='reported-clicks'),
              T(1440, 718, 360, 58, 'to prepare and submit\na sample list', 'body', 24, INK,
                lh=1.15)]
    slides.append(s)
    return slides
