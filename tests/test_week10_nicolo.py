"""The isolated contributor variant must not turn pending case material into evidence."""
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_REVISION = '2330036350ed76a8433e8a6ac9b9fcb267412ccf'


def text(slide):
    return ' '.join(r.text for e in slide.els if hasattr(e, 'paras')
                    for p in e.paras for r in p.runs)


class NicoloVariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week10_nicolo import S, CASE_START, CASE_SPEAKING_MINUTES, CASE_QA_MINUTES
        cls.slides = S
        cls.start = CASE_START
        cls.minutes = CASE_SPEAKING_MINUTES
        cls.qa = CASE_QA_MINUTES

    def test_separate_original_sources_are_byte_unchanged(self):
        for name in ('deck/week10.py', 'deck/week10_figures.py',
                     'lessons/week10-lesson-plan.md', 'lessons/week10-speaker-notes.md',
                     'lessons/week10-speaker-brief.md'):
            self.assertEqual((ROOT/name).read_bytes(), subprocess.check_output(
                ['git', 'show', ORIGINAL_REVISION+':'+name], cwd=ROOT), name)

    def test_structure_and_case_budget(self):
        self.assertEqual(self.start, 7)
        self.assertEqual(len(self.slides), 14)
        self.assertEqual(len(self.minutes), len(self.slides)-self.start)
        self.assertEqual(sum(self.minutes)+self.qa, 10)
        self.assertEqual(self.qa, 2)
        for phase, slide in zip(('DISCOVER', 'DEFINE', 'DEVELOP', 'DELIVER'), self.slides[1:5]):
            self.assertIn(phase, text(slide))

    def test_revised_discover_and_deliver(self):
        discover = text(self.slides[1])
        for value in ('How do users value privacy?', 'What will they share?', 'What may enter AI'):
            self.assertIn(value, discover)
        self.assertIn('Willingness is not permission', self.slides[1].notes)
        deliver = text(self.slides[4])
        for value in ('wishes', 'priority', 'to whom', 'task outcomes'):
            self.assertIn(value, deliver.lower())
        self.assertIn('cannot establish human usability', self.slides[4].notes)

    def test_case_has_no_fabricated_assets_or_research(self):
        for slide in self.slides[self.start:]:
            self.assertFalse(slide.cp or slide.report)
        self.assertIn('positive qualitative findings', self.slides[8].notes)
        metrics = text(self.slides[9])
        for value in ('30%', '1 click', 'NOT INDEPENDENTLY VERIFIED', 'NOT AI REDESIGN RESULTS'):
            self.assertIn(value, metrics)
        self.assertIn('Do not conflate 30% faster with 30% less completion time', self.slides[9].notes)
        self.assertEqual(sum(e.name == 'pending-asset' for e in self.slides[10].els), 2)
        self.assertEqual(sum(e.name == 'pending-asset' for e in self.slides[11].els), 3)
        for i in (10, 11):
            self.assertIn('PROPOSED', text(self.slides[i]))
            self.assertFalse(any(e.kind == 'image' and not e.name.startswith('chrome-')
                                 for e in self.slides[i].els))

    def test_context_specific_constraints_are_questions_not_industry_facts(self):
        projected = text(self.slides[12])
        for value in ('low light', 'image capture permitted', 'digital readiness',
                      'cloud policy', 'compute', 'device adaptation',
                      'NOT A COMPLETED TECHNICAL AUDIT'):
            self.assertIn(value.lower(), projected.lower())
        self.assertIn('not verified characteristics', self.slides[12].notes)

    def test_links_notes_privacy_and_geometry(self):
        links = [r.url for e in self.slides[0].els if hasattr(e, 'paras')
                 for p in e.paras for r in p.runs if r.url]
        self.assertIn('https://www.designcouncil.org.uk/resources/the-double-diamond/', links)
        self.assertIn('https://creativecommons.org/licenses/by/4.0/', links)
        for slide in self.slides:
            self.assertGreater(len(slide.notes), 180)
            self.assertFalse(slide.cp or slide.report)
            self.assertNotIn('ESFQ', text(slide))
            for e in slide.els:
                if not all(hasattr(e, k) for k in ('x', 'y', 'w', 'h')):
                    continue
                self.assertGreaterEqual(e.x, 0)
                self.assertGreaterEqual(e.y, 0)
                self.assertLessEqual(e.x+e.w, 1920)
                self.assertLessEqual(e.y+e.h, 1080)
                if not e.name.startswith('chrome-'):
                    self.assertLessEqual(e.y+e.h, 1000)


if __name__ == '__main__':
    unittest.main()
