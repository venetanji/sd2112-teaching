"""The isolated contributor variant must not turn pending case material into evidence."""
from pathlib import Path
import subprocess
import unittest
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_REVISION = '2330036350ed76a8433e8a6ac9b9fcb267412ccf'


def text(slide):
    parts = [r.text for e in slide.els if hasattr(e, 'paras')
             for p in e.paras for r in p.runs]
    parts += [ET.fromstring(e.svg).get('aria-label', '') for e in slide.els
              if e.name == 'phase-subtitle']
    return ' '.join(parts)


class NicoloVariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week10_nicolo import S, CASE_START, CASE_SPEAKING_MINUTES, CASE_QA_MINUTES
        cls.slides = S
        cls.start = CASE_START
        cls.minutes = CASE_SPEAKING_MINUTES
        cls.qa = CASE_QA_MINUTES

    def slide(self, title):
        return next(s for s in self.slides if s.title == title)

    def test_separate_original_sources_are_byte_unchanged(self):
        for name in ('deck/week10.py', 'deck/week10_figures.py',
                     'lessons/week10-lesson-plan.md', 'lessons/week10-speaker-notes.md',
                     'lessons/week10-speaker-brief.md'):
            self.assertEqual((ROOT/name).read_bytes(), subprocess.check_output(
                ['git', 'show', ORIGINAL_REVISION+':'+name], cwd=ROOT), name)

    def test_structure_and_case_budget(self):
        self.assertEqual(self.start, 8)
        self.assertEqual(len(self.slides), 16)
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
        self.assertIn('positive qualitative findings', self.slide('Qualitative findings').notes)
        metrics_slide = self.slide('Quantitative findings')
        metrics = text(metrics_slide)
        for value in ('30%', '1 click', 'context pending', 'not results of the AI redesign'):
            self.assertIn(value, metrics)
        self.assertIn('Do not conflate 30% faster with 30% less completion time', metrics_slide.notes)
        before = self.slide('Before and after')
        flow = self.slide('The redesigned experience')
        self.assertEqual(sum(e.name == 'pending-asset' for e in before.els), 1)
        self.assertEqual(sum(e.name == 'pending-asset' for e in flow.els), 3)
        self.assertEqual(sum(e.name == 'current-product-screenshot' for e in before.els), 1)
        for slide in (before, flow):
            self.assertIn('PROPOSED', text(slide))
            self.assertFalse(any(e.kind == 'image' and not e.name.startswith('chrome-')
                                 and e.name != 'current-product-screenshot' for e in slide.els))

    def test_screen_aspect_ratios_and_dedicated_video(self):
        from deck.week10_nicolo import SCREEN_RATIO
        for title in ('How the current product works', 'Before and after', 'The redesigned experience'):
            for e in self.slide(title).els:
                if e.name in ('pending-asset', 'current-product-screenshot'):
                    self.assertLessEqual(abs(e.h-e.w/SCREEN_RATIO), .5)
                    if e.kind == 'image':
                        self.assertEqual(e.fit, 'contain')
        video = self.slide('The product in use')
        self.assertEqual(self.slides.index(video), 9)
        self.assertEqual(len(video.html_only), 1)
        player = video.html_only[0]
        self.assertEqual((player.cw, player.ch), (1920, 1080))
        self.assertAlmostEqual(player.w/player.h, 16/9)
        self.assertIn('49.365-second video', video.notes)
        self.assertIn('video.controls = true', player.code)
        self.assertNotIn('autoplay = true', player.code)
        self.assertIn("parent.Reveal.on('slidechanged'", player.code)
        self.assertEqual(self.minutes[1], 1)
        self.assertGreater(self.minutes[1]*60, 49.365)

    def test_context_specific_constraints_are_questions_not_industry_facts(self):
        slide = self.slide('Technical constraints')
        projected = text(slide)
        for value in ('low light', 'image capture permitted', 'digital readiness',
                      'cloud policy', 'compute', 'device adaptation',
                      'Potential constraints'):
            self.assertIn(value.lower(), projected.lower())
        self.assertIn('not verified characteristics', slide.notes)

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

    def test_opening_definition_explanation_and_diagram_labels(self):
        from deck.week10_nicolo import DD_DEFINITION
        expected = ('The\u00a0Double Diamond\u00a0is a visual representation of the design and innovation process. '
                    'It\u2019s a simple way to describe the steps taken in any design\u00a0and innovation\u00a0project, '
                    'irrespective of methods and tools used.')
        self.assertEqual(DD_DEFINITION, expected)
        slide = self.slides[0]
        definition = next(e for e in slide.els if e.name == 'dd-definition')
        self.assertEqual(''.join(r.text for p in definition.paras for r in p.runs),
                         '\u201c'+expected+'\u201d')
        opening = text(slide)
        self.assertNotIn('Presenting it in three layers', opening)
        self.assertNotIn('dd-opening-explanation', [e.name for e in slide.els])
        diagram = next(e for e in slide.els if e.name == 'dd-official-diagram')
        self.assertEqual(diagram.w, round(1080*.9))
        self.assertEqual(diagram.x+diagram.w/2, 960)
        labels = [e for e in slide.els if e.name == 'dd-space-label']
        self.assertEqual(len(labels), 2)
        for label, name, center in zip(labels, ('Problem Space', 'Solution Space'), (246, 694)):
            self.assertEqual(label.paras[0].runs[0].text, name)
            self.assertAlmostEqual(label.x+label.w/2, diagram.x+diagram.w*center/936)
            self.assertLessEqual(label.y+label.h, diagram.y)

    def test_experience_is_impersonal_in_slides_and_notes(self):
        import re
        for slide in self.slides:
            self.assertIsNone(re.search(r'\b(I|my|me|mine|myself|we|our|ours)\b',
                                        text(slide)+' '+slide.notes))
        for slide in self.slides[1:5]:
            self.assertIn('INDUSTRY EXAMPLE', text(slide))
            self.assertNotIn('INDUSTRY EXPERIENCE', text(slide))
        self.assertIn('Five usability tests were run', text(self.slides[4]))

    def test_engineer_role_except_unchanged_slide07(self):
        import re
        self.assertIn('an Engineer', text(self.slides[3]))
        for i, slide in enumerate(self.slides):
            if i != 6:
                self.assertIsNone(re.search(r'\bdevelopers?\b', text(slide)+' '+slide.notes, re.I))
        old = subprocess.check_output(['git', 'show', '847e965:deck/week10_nicolo.py'],
                                      cwd=ROOT, text=True)
        current = (ROOT/'deck/week10_nicolo.py').read_text()
        start = "S.append(three('DOUBLE DIAMOND / COLLABORATION'"
        stop = "S.append(section('CASE STUDY'"
        self.assertEqual(old[old.index(start):old.index(stop)],
                         current[current.index(start):current.index(stop)])

    def test_notes_companion_matches_current_slides(self):
        companion = (ROOT/'lessons/week10-nicolo-speaker-notes.md').read_text()
        expected = ''.join(f'## {i:02d} / {s.title}\n\n{s.notes}\n\n'
                           for i, s in enumerate(self.slides, 1)).rstrip()+'\n'
        self.assertEqual(companion[companion.index('## 01 /'):], expected)

    def test_phase_subtitles_maps_and_reading_order(self):
        from deck.week10_nicolo import PHASES
        from deck.week10_nicolo_figures import phase_map, THINKING_MODES
        for i, (space, phase) in enumerate(PHASES):
            slide = self.slides[i+1]
            self.assertIn('divergent thinking' if i in (0, 2) else 'convergent thinking', text(slide))
            subtitle = next(e for e in slide.els if e.name == 'phase-subtitle')
            root = ET.fromstring(subtitle.svg)
            self.assertEqual(root.get('aria-label'), space+' \u25c6 '+THINKING_MODES[phase])
            texts = list(root.iter('{http://www.w3.org/2000/svg}tspan'))
            row = root.find('{http://www.w3.org/2000/svg}text')
            for setting in ('font-optical-sizing:none', 'font-feature-settings:normal',
                            'text-rendering:geometricPrecision'):
                self.assertIn(setting, row.get('style'))
            self.assertTrue(all(not t.tail for t in texts))
            self.assertEqual([t.text for t in texts], [space, '\u25c6', THINKING_MODES[phase]])
            self.assertEqual([t.get('fill') for t in texts], ['#5A626B', '#246E70', '#5A626B'])
            self.assertAlmostEqual(float(texts[1].get('font-size')), 34/3)
            self.assertLess(float(texts[1].get('y')), float(texts[0].get('y')))
            self.assertEqual(float(texts[1].get('dx')), float(texts[2].get('dx')))
            self.assertLessEqual(float(texts[1].get('dx')), 14)
            self.assertLessEqual(subtitle.x+subtitle.w, 1440)
            self.assertNotIn('\u2022', text(slide))
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

    def test_iteration_map_has_no_accent_and_phase_durations_are_explicit(self):
        slide = self.slides[5]
        maps = [e for e in slide.els if e.name == 'phase-navigation']
        self.assertEqual(len(maps), 1)
        self.assertEqual((maps[0].x, maps[0].y, maps[0].w, maps[0].h), (1440, 210, 360, 176))
        self.assertNotIn('#246E70', maps[0].svg)
        self.assertEqual(maps[0].svg.count('fill="#FFFFFF"'), 4)
        self.assertIn('The phases do not all take the same amount of time.', text(slide))
        self.assertIn('do not represent equal durations', slide.notes)
        title = next(e for e in slide.els if e.name == 'variant-heading')
        self.assertLessEqual(title.x+title.w, maps[0].x)
        columns = [e for e in slide.els if e.name.startswith('column-')]
        self.assertTrue(all(e.y > maps[0].y+maps[0].h for e in columns))

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
