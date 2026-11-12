"""Week 12 original conceptual figures, using editable native slide elements.

These are teaching illustrations, not observed data or model-internals traces.
Text and shapes remain native in PowerPoint and semantic in mobile reading mode.
"""
from pathlib import Path

from deckgen import INK, PAPER, Image
from deckgen.layouts import content, T, Rect

TEAL = '#246E70'
ASSETS = Path(__file__).resolve().parent / 'assets' / 'week12'


def paper_frame(eyebrow, heading, notes):
    """Use the approved course paper-title and citation grid."""
    slide = content(eyebrow, heading, [], title_size=72, notes=notes)
    slide.els = slide.els[:2]
    heading_el = slide.els[1]
    heading_el.x, heading_el.y, heading_el.w, heading_el.h = 120, 184, 1680, 140
    heading_el.name = 'paper-title'
    return slide


def paper_block(slide, x, y, width, label, value, height, size=34, name=''):
    slide.els.extend([
        T(x, y, width, 34, label, 'mono', 23, TEAL, name=name + '-label'),
        T(x, y + 52, width, height, value, 'body', size, INK,
          lh=1.2, name=name + '-body'),
    ])


def paper_pair(eyebrow, heading, images, reading, caption, notes,
                  guide, second_reading=None):
    """Replace the compressed abstract with a task/analysis then result pair."""
    from week12_studies import GUIDES
    key = next(k for k in GUIDES if k in eyebrow.split(' / '))
    g = GUIDES[key]
    extra = (' Targeted primary-source recheck, 22 October 2026: ' +
             g['location'] + ' This pair replaces the compressed summary within '
             'the existing teaching allocation, not extra class minutes.')
    task = paper_frame(eyebrow + ' / TASK + EVIDENCE', g['title'], notes + extra)
    for x, y, label, value, height, name in [
        (120, 348, g['task_label'], g['task'], 210, 'study-task'),
        (120, 676, g['comparison_label'], g['comparison'], 190, 'study-comparison'),
        (1020, 348, g['example_label'], g['example'], 210, 'study-example'),
        (1020, 676, g['measure_label'], g['measured'], 190, 'study-measurement'),
    ]:
        paper_block(task, x, y, 780, label, value, height, name=name)
    task.els.append(T(120, 956, 1680, 38, reading, 'mono', 21, INK, lh=1.1))

    result = paper_frame(eyebrow + ' / FINDING + LIMIT', heading, notes + extra)
    for i, (name, *_unused) in enumerate(images):
        if len(images) == 1:
            x, y, w, h = 120, 348, 1010, 385
        else:
            x, y, w, h = 120, 348 + i * 205, 1010, 185
        result.els.append(Image(x, y, w, h, str(ASSETS / name), fit='contain',
                                name='paper-excerpt-' + name))
    result.els.append(T(120, 760, 1010, 115, guide, 'body', 29, INK, lh=1.2))
    for y, label, value, height, name in [
        (348, g['result_label'], g['result'], 160, 'study-result'),
        (580, 'WHAT IT DOES NOT SHOW', g['limit'], 160, 'study-limit'),
        (812, 'FOR YOUR PROJECT', g['design'], 90, 'study-design'),
    ]:
        paper_block(result, 1190, y, 610, label, value, height, size=32, name=name)
    result.els.extend([
        T(120, 884, 1010, 64, caption, 'mono', 22, TEAL, lh=1.1),
        T(120, 956, 1680, 38, reading, 'mono', 21, INK, lh=1.1),
    ])
    if second_reading:
        task.els.append(T(120, 914, 1680, 34, second_reading, 'mono', 21, TEAL))
    return [task, result]


def stages(eyebrow, heading, items, caption, notes):
    """Interleave each stage and its account for native/mobile reading order."""
    slide = content(eyebrow, heading, [], bg=PAPER, title_size=64, notes=notes)
    slide.els = slide.els[:2]
    width, gap = 390, 40
    for i, (label, action, detail) in enumerate(items):
        x = 120 + i * (width + gap)
        slide.els.extend([
            Rect(x, 355, width, 110, TEAL),
            T(x + 24, 377, width - 48, 66, label, 'xbold', 35, '#FFFFFF', valign='m'),
            T(x, 505, width, 92, action, 'xbold', 37, INK, lh=1.15),
            T(x, 630, width, 212, detail, 'body', 31, INK, lh=1.24),
        ])
        if i < len(items) - 1:
            slide.els.append(T(x + width, 385, gap, 56, '>', 'mono', 34, TEAL, align='c'))
    slide.els.append(T(120, 900, 1680, 70, caption, 'body', 27, TEAL, lh=1.2))
    return slide


def agent_loop():
    return stages('MECHANISM / SIMPLIFIED AFTER YAO ET AL., REACT',
        'A tool result becomes the next input.', [
            ('OBSERVE', 'Read the state.', 'A request, available evidence and the last tool result enter the context.'),
            ('PROPOSE', 'Choose a next step.', 'The model proposes an answer or a tool call. A proposal is not permission.'),
            ('CHECK + ACT', 'The harness decides.', 'Written rules check the allowed tool and scope before executing an action.'),
            ('INSPECT', 'Continue or stop.', 'Read the actual result. Return to observation, or stop and report a failure.'),
        ], 'Conceptual loop: INSPECT -> OBSERVE. Checks shown here are our design addition, not a safety result.',
        'Mechanism source: Yao et al., ReAct, ICLR 2023, arXiv:2210.03629v3, sections 2-4 and Figure 1. Full primary text read. ReAct interleaves generated reasoning/action traces with observations in specific benchmark environments. This figure is our simplified harness-level teaching account, not a diagram of hidden cognition. The explicit permission checkpoint is a proposed design boundary, not a claim that the paper validates it. A tool may read data or change state; both can have consequences. The loop must have a stop condition and a failure path. Historical Week 12 PDF27 labels its thought/action/observation loop "Agent prompt"; we retain the loop idea but not that misleading label. PDF29 is diffusion, not an agent. Ask: where would the product prevent a second attempt from duplicating an action? About four minutes within 10-40.')


def privacy_flow():
    return stages('DESIGN HYPOTHESIS / FICTIONAL PHOTO-SHARING AID',
        'Privacy controls must be usable before sharing.', [
            ('CAPTURE', 'Choose the input.', 'Use a fictional photo. State whether any remote processing would occur.'),
            ('REVIEW', 'Hear what is present.', 'Offer a nonvisual account of detected content and uncertainty. Allow correction.'),
            ('EDIT OR REFUSE', 'Keep a real choice.', 'Try redaction, recapture or cancel. Do not imply every private detail was found.'),
            ('SHARE', 'Confirm the recipient.', 'Preview what leaves and to whom. Explain retention and the limits of recall.'),
        ], 'Proposed flow, not tested protection. Remote analysis can disclose data before a later Share button.',
        'Our teaching hypothesis motivated by Sharma et al. (2025), author preprint v2, sections 4-6. Interviews establish practices and design preferences, not the effectiveness of this flow, redaction or on-device processing. A cloud-based preview has already transmitted the input: confirmation before public sharing does not undo provider disclosure. Make the data boundary explicit, including bystanders and the cost of asking a helper. A screen-reader description of a control does not establish that a real person can use it effectively. Do not ask sighted classmates to simulate blindness; ask them to identify an untested access requirement and plan participatory evaluation with appropriate participants and consent. No personal photos, camera activation, cloud upload or third-party account is needed. About four minutes within 40-65.')


def incident_map(source_url):
    """Schematic roadway relation from NTSB, not a scale drawing or crash photo."""
    slide = content('CASE / ROAD SPLIT / NOT TO SCALE',
                    'Autosteer followed the wrong path.', [], bg=PAPER, title_size=65,
                    notes='This is an original schematic course diagram based on NTSB HAR-20/01 pp. 1-6 and Figure 5, not a reproduction of the road geometry or a source image. At the US-101/SR-85 split, Autosteer moved a 2017 Model X from a continuing HOV lane toward the painted gore, a nontravel area dividing the highway from the exit. The vehicle struck a previously damaged crash attenuator at the end of the median. The log locates the steering input about 5.9 seconds before collision and impact at about 71 mph. The drawn paths and spacing are illustrative; the exit lane is above the continuing lane to indicate the left-side branch; orange highlights the nontravel gore rather than claiming an orange road marking, and black labels the damaged attenuator. No coordinate, exact lane width, or alternative route is claimed. Source: ' + source_url)
    slide.els = slide.els[:2]
    slide.els.extend([
        Rect(120, 385, 1680, 112, '#D9E3E6'),
        Rect(120, 560, 1680, 112, '#D9E3E6'),
        T(155, 405, 1530, 65, 'SR-85 exit (left) ->', 'mono', 30, INK),
        T(155, 580, 1510, 65, 'US-101 continues ->', 'mono', 30, INK),
        Rect(905, 510, 525, 35, '#ED6D24'),
        T(920, 695, 850, 60, 'ORANGE = GORE / NOT A TRAVEL LANE', 'mono', 28, TEAL),
        Rect(1430, 500, 80, 110, INK),
        T(1320, 795, 490, 90, 'BLACK = DAMAGED ATTENUATOR', 'mono', 28, INK),
        T(220, 785, 1040, 55, 'Model X: from US-101 -> left into gore -> barrier', 'body', 37, INK),
        T(120, 925, 1680, 45, f'[NTSB HAR-20/01 / pp. 1-6]({source_url})', 'mono', 22, TEAL),
    ])
    return slide
