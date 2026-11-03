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
        self.assertEqual(self.start, 8)
        self.assertEqual(len(self.slides), 15)
        self.assertEqual(len(self.minutes), len(self.slides)-self.start)
        self.assertEqual(sum(self.minutes)+self.qa, 10)
        self.assertEqual(self.qa, 2)
        for phase, slide in zip(('DISCOVER', 'DEFINE', 'DEVELOP', 'DELIVER'), self.slides[1:5]):
            self.assertIn(phase.lower(), text(slide).lower())

    def test_revised_discover_and_deliver(self):
        discover = text(self.slides[1])
        for value in ('How do users value privacy?', 'What data are they willing to share?', 'What data can be fed to AI?'):
            self.assertIn(value, discover)
        self.assertIn('Willingness is not permission', self.slides[1].notes)
        deliver = text(self.slides[4])
        for value in ('wishes', 'priorities', 'why', 'how'):
            self.assertIn(value, deliver.lower())
        self.assertIn('cannot establish human usability', self.slides[4].notes)

    def test_case_has_no_fabricated_assets_or_research(self):
        for slide in self.slides[self.start:]:
            self.assertFalse(slide.cp or slide.report)
        self.assertIn('positive qualitative findings', self.slides[9].notes)
        metrics = text(self.slides[10])
        for value in ('30%', '1 click', 'context pending', 'not results of the AI redesign'):
            self.assertIn(value, metrics)
        self.assertIn('Do not conflate 30% faster with 30% less completion time', self.slides[10].notes)
        self.assertEqual(sum(e.name == 'pending-asset' for e in self.slides[11].els), 2)
        self.assertEqual(sum(e.name == 'pending-asset' for e in self.slides[12].els), 3)
        for i in (11, 12):
            self.assertIn('PROPOSED', text(self.slides[i]))
            self.assertFalse(any(e.kind == 'image' and not e.name.startswith('chrome-')
                                 for e in self.slides[i].els))

    def test_context_specific_constraints_are_questions_not_industry_facts(self):
        projected = text(self.slides[13])
        for value in ('low light', 'image capture permitted', 'digital readiness',
                      'cloud policy', 'compute', 'device adaptation',
                      'Potential constraints'):
            self.assertIn(value.lower(), projected.lower())
        self.assertIn('not verified characteristics', self.slides[13].notes)

    def test_document_voice_and_case_separator(self):
        self.assertEqual([s.title for s in self.slides[:7]], [
            'Double Diamond', 'Discover', 'Define', 'Develop', 'Deliver',
            'An iterative and imperfect process', 'Stakeholder management'])
        for phrase in ('Spend enough time understanding your users',
                       'You cannot expect the user to be exactly like you',
                       'Do not assume the problem'):
            self.assertIn(phrase, text(self.slides[1]))
        self.assertIn('design does not happen in a vacuum', text(self.slides[6]).lower())
        self.assertEqual(self.slides[7].title, 'Software UX Design')
        self.assertIn('CASE STUDY', text(self.slides[7]))
        self.assertIn('within', self.slides[7].notes)

    def test_phase_subtitles_maps_and_reading_order(self):
        from deck.week10_nicolo import PHASES
        from deck.week10_nicolo_figures import phase_map
        for i, (space, phase) in enumerate(PHASES):
            slide = self.slides[i+1]
            self.assertIn('divergent thinking' if i in (0, 2) else 'convergent thinking', text(slide))
            subtitle = next(e for e in slide.els if e.name == 'phase-subtitle')
            self.assertIn(space+' \u2022 '+phase, text(slide))
            title = next(e for e in slide.els if e.name == 'variant-heading')
            self.assertGreaterEqual(subtitle.y, title.y+title.h)
            maps = [e for e in slide.els if e.name == 'phase-navigation']
            self.assertEqual(len(maps), 1)
            self.assertLessEqual(maps[0].w, 400)
            self.assertLessEqual(maps[0].y+maps[0].h, 400)
            svg, _ = phase_map(phase)
            self.assertNotIn('<text', svg)
            self.assertEqual(svg.count('fill="#246E70"'), 1)
            self.assertIn('after Design Council', slide.notes)
            names = [e.name for e in slide.els]
            self.assertLess(names.index('phase-subtitle'), names.index('phase-navigation'))

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
