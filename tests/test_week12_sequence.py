"""Classroom timing and navigation for the final teaching session."""
import sys
from pathlib import Path
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deck'))


class Week12RecapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from week12 import DECK

        cls.slides = DECK['slides']
        cls.start_slide = DECK.get('presenter_start_slide')

    def test_opening_esfq_and_fair_sequence(self):
        titles = [slide.title for slide in self.slides]
        self.assertIn('Can a machine', titles[0])
        handover = titles.index('ESFQ')
        self.assertGreaterEqual(handover, 25)
        self.assertEqual(titles[handover - 1], 'Course AMA')
        self.assertEqual(titles[handover + 1], 'Claim your poster-fair space')
        self.assertEqual(titles[handover + 2:], ['Group project AMA'])
        self.assertIn('12:30', self.slides[handover].notes)
        activities = [(slide.title, slide.cp['type']) for slide in self.slides if slide.cp]
        self.assertEqual(activities, [('Course AMA', 'short_answer'), ('Group project AMA', 'short_answer')])
        self.assertEqual(self.start_slide, 1)

    def test_names_both_concept_theories(self):
        titles = [slide.title for slide in self.slides]
        self.assertEqual(titles[9:11], ['Classical theory of concepts', 'Prototype theory'])
        self.assertEqual(titles[26], 'Musical choices in a sequencer')

    def test_paper_recaps_follow_the_week_11_study(self):
        week09, week11 = self.slides[35:37]
        self.assertEqual(self.slides[34].title, 'Better ratings. More similar stories.')
        self.assertEqual((week09.title, week11.title), ('Week 9 papers', 'Week 11 papers'))
        for slide, count in ((week09, 8), (week11, 6)):
            links = {run.url for element in slide.els for paragraph in getattr(element, 'paras', [])
                     for run in paragraph.runs if run.url}
            self.assertEqual(len(links), count)

    def test_recap_keeps_the_course_story_before_discussion(self):
        titles = [slide.title for slide in self.slides]
        discussion = titles.index('Designers as curators')
        highlights = (
            'Write the rule, or show the examples.',
            'One rule. One random number.',
            'Four states. The cell above decides.',
            'Fifty years betting on the brain.',
            'The guess goes forward. The error comes back.',
            'The chips made for games.',
            'Ihde: technology mediates our world.',
            'Using AI, or incorporating AI.',
            'One sequence. Many positions working together.',
            'Generation turns new noise into an image.',
            'The brief emerged through choices.',
            'A better prompt was not always the right repair.',
            'A picture of sound. Or tokens of sound.',
            'People chose humans but rated AI higher.',
            'Feeling, work, permission, law.',
        )
        positions = [titles.index(title) for title in highlights]
        self.assertEqual(positions, sorted(positions))
        self.assertLess(positions[-1], discussion)
        self.assertNotIn('One concept. One product image.', titles)
        self.assertNotIn('Useful does not mean necessary.', titles)
        self.assertNotIn('Could a driver take over in time?', titles)
        self.assertEqual(titles[discussion:discussion + 4], [
            'Designers as curators', 'Language as an interface', 'Fractional authorship',
            'What answer would you give Lovelace now?',
        ])

    def test_links_and_registration(self):
        settings = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertEqual(settings['course']['decks'][-2:], ['week11', 'week12'])
        self.assertIn('week12/', {entry['href'] for entry in settings['nav']})
        links = {
            run.url for slide in self.slides for element in slide.els
            for paragraph in getattr(element, 'paras', []) for run in paragraph.runs
            if run.url
        }
        for week in settings['course']['decks'][:-1]:
            self.assertTrue(any(f'/{week}/#/' in url for url in links), week)


if __name__ == '__main__':
    unittest.main()
