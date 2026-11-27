"""Week 13 classroom sequence and student export boundaries."""
from pathlib import Path
import runpy
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def slide_text(slide):
    return ' '.join(run.text for element in slide.els if hasattr(element, 'paras')
                    for paragraph in element.paras for run in paragraph.runs)


class Week13Tests(unittest.TestCase):
    def load_slides(self, room=None):
        original_read_text = Path.read_text

        def read_text(path, *args, **kwargs):
            if path == ROOT / 'deck/week13-poster-fair-link.txt':
                if room is None:
                    raise FileNotFoundError(path)
                return room + '\n'
            return original_read_text(path, *args, **kwargs)

        with patch.object(Path, 'read_text', read_text):
            return runpy.run_path(str(ROOT / 'deck/week13.py'))['DECK']['slides']

    def test_news_then_quiz_then_poster_fair(self):
        slides = self.load_slides()
        self.assertEqual([slide.title for slide in slides],
                         ['Week 13 news', 'Final quiz', 'Poster fair'])
        for topic in ('GTA VI', 'Jensen Huang', 'Anthropic'):
            self.assertIn(topic, slide_text(slides[0]))
        self.assertIn('Canvas', slide_text(slides[1]))
        self.assertFalse(any(slide.cp for slide in slides))

    def test_classroom_board_is_a_hyperlink(self):
        room = 'https://excalidraw.com/#room=example,key'
        slide = self.load_slides(room)[-1]
        links = [run.url for element in slide.els if hasattr(element, 'paras')
                 for paragraph in element.paras for run in paragraph.runs if run.url]
        self.assertIn(room, links)

    def test_public_build_directs_students_to_shared_link(self):
        self.assertIn('class channel', slide_text(self.load_slides()[-1]))

    def test_week_is_registered_without_dropping_prior_weeks(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertEqual(config['course']['decks'][-4:],
                         ['week09', 'week11', 'week12', 'week13'])
        self.assertIn('week13/', [item['href'] for item in config['nav']])
