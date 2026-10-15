"""Twenty concept slides selected from the taught Weeks 1-6 decks."""
from copy import deepcopy
from importlib import import_module

from deckgen.layouts import add_chrome


SELECTION = {
    1: (
        # deckgen truncates statement titles to 60 characters in the outline.
        'Intelligent-like output or behaviour, achieved through compu',
        'Write the rule, or show the examples.',
        'Using AI, or incorporating AI.',
    ),
    2: (
        'Exact. Explainable. Brittle.',
        'Same rule, three seeds.',
        'One spec. Three executors.',
    ),
    3: (
        'A concept is its best examples.',
        'A neuron is a weighted vote.',
        'The guess goes forward. The error comes back.',
        'Two inputs. One new space.',
    ),
    4: (
        'One sequence. Many positions working together.',
        'A tool call alone does not make a system an agent.',
        'Thought \u2192 Action \u2192 Observation',
    ),
    5: (
        'Ihde: technology mediates our world.',
        'CLIP brings words and images into a shared space.',
        'Training teaches a denoiser to remove noise.',
        'Generation turns new noise into an image.',
    ),
    6: (
        'A spectrogram keeps the changing spectrum.',
        'MIDI describes events. It contains no sound.',
        'A picture of sound. Or tokens of sound.',
    ),
}


def recap_slides():
    slides = []
    for week, titles in SELECTION.items():
        source = import_module(f'week{week:02d}').S
        for title in titles:
            matches = [slide for slide in source if slide.title == title]
            if len(matches) != 1:
                raise ValueError(f'Expected one Week {week} recap slide: {title!r}')
            original = matches[0]
            slide = deepcopy(original)
            # Imported decks already have their original footers and slide numbers.
            slide.els = [el for el in slide.els
                         if not getattr(el, 'name', '').startswith('chrome-')]
            slide.cp = None
            slide.report = ''
            slide.notes = f'Week {week} concept recap before the quiz. ' + slide.notes
            add_chrome(slide, len(slides) + 3, f'SD2112 / WEEK 07 / RECAP WEEK {week:02d}')
            slide.chrome = False
            slides.append(slide)
    return slides
