"""Week 12 timing, bounded evidence, fallback, native geometry and report hooks."""
from pathlib import Path
import importlib.util
import re
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(r.text for el in slide.els if hasattr(el, 'paras')
                    for p in el.paras for r in p.runs)


class Week12Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week12 import S, DECK, TIMING
        cls.slides, cls.deck, cls.timing = S, DECK, TIMING
        cls.plan = (ROOT / 'lessons/week12-lesson-plan.md').read_text()

    def slide(self, title):
        matches = [s for s in self.slides if s.title == title]
        self.assertEqual(len(matches), 1, title)
        return matches[0]

    def load_with_mapping(self, entries):
        from deckgen import attach_reports
        calls = []

        def inject(slides, path):
            calls.append(path)
            return attach_reports(slides, entries, quiet=True)

        spec = importlib.util.spec_from_file_location('week12_test_load', ROOT / 'deck/week12.py')
        module = importlib.util.module_from_spec(spec)
        with patch('deckgen.attach_reports', side_effect=inject):
            spec.loader.exec_module(module)
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0].name, 'week12-reports.json')
        return module

    def test_exact_180_minutes_and_protected_blocks(self):
        self.assertEqual([(a, b) for a, b, *_ in self.timing],
                         [(0, 10), (10, 40), (40, 65), (65, 75), (75, 90),
                          (90, 120), (120, 155), (155, 175), (175, 180)])
        self.assertEqual(sum(b - a for a, b, *_ in self.timing), 180)
        self.assertEqual([i for _, _, a, b, _ in self.timing for i in range(a, b + 1)], list(range(1, 31)))
        self.assertEqual(len(self.slides), 34)
        for first, minutes in [(21, 30), (24, 35), (28, 20)]:
            self.assertIn(f'{minutes} min', text(self.slides[first - 1]))
        self.assertEqual(self.slides[19].title, 'Break.\nFifteen minutes.')

    def test_actual_slide_map_and_notes_match_all_slides(self):
        mapping = self.plan.split('<!-- slide-map:start -->')[1].split('<!-- slide-map:end -->')[0]
        rows = re.findall(r'^\| (\d+) \| (.*?) \| (.*?) \|$', mapping, re.M)
        self.assertEqual(len(rows), len(self.slides))
        companion = (ROOT / 'lessons/week12-speaker-notes.md').read_text()
        sections = re.split(r'^## \d+ / .*?\n\n', companion, flags=re.M)[1:]
        self.assertEqual(len(sections), 34)
        for i, (s, row, note) in enumerate(zip(self.slides, rows, sections), 1):
            self.assertEqual(row[:2], (str(i), s.title.replace('\n', ' / ')))
            self.assertEqual(note.strip(), s.notes.strip())
            self.assertGreater(len(s.notes.split()), 55, s.title)

    def test_sequence_papers_break_activities_close_and_reference_shelf(self):
        self.assertEqual(self.slides[10].title, 'An explanation did not fix wrong advice here.')
        self.assertEqual(self.slides[12].title, 'Private from a helper. Exposed to whom?')
        self.assertEqual(self.slides[20].title, 'Walk through three low-risk situations.')
        self.assertEqual(self.slides[23].title, 'Paired review. Then swap roles.')
        self.assertEqual(self.slides[27].title, 'Choose the change that matters most.')
        self.assertTrue(all('REFERENCE SHELF' in text(s) for s in self.slides[30:]))

    def test_evidence_is_bounded_on_visible_slides_not_just_notes(self):
        cecil = text(self.slides[10])
        for phrase in ('1,403', 'fictional CVs', 'accuracy', 'Heatmaps/charts', 'not show that all explanations are useless'):
            self.assertIn(phrase, cecil)
        sharma = text(self.slides[12])
        for phrase in ('21', 'US', 'interviews', 'thematic analysis', 'not tested for effectiveness'):
            self.assertIn(phrase, sharma)
        self.assertIn('Proposed flow, not tested protection', text(self.slides[13]))
        self.assertIn('Remote analysis can disclose data', text(self.slides[13]))
        self.assertIn('not proven safer', text(self.slides[16]))

    def test_low_risk_complete_static_workflow_and_nonchatbot_validity(self):
        activity = self.slides[20]
        for phrase in ('paper/static', 'SIMULATION', 'ordinary, ambiguous', 'out-of-scope'):
            self.assertIn(phrase, text(activity))
        for phrase in ('No third-party actions', 'Paper cards and static screens', 'classifiers', 'installations'):
            self.assertIn(phrase, activity.notes)
        self.assertIn('A physical product, recommender or visual system', text(self.slides[8]))
        self.assertIn('without disability simulation', text(self.slides[21]))
        self.assertIn('No new deadline, grade or upload', text(self.slides[27]))

    def test_ethical_argument_names_people_values_contestation_accountability(self):
        visible = text(self.slides[15])
        for phrase in ('housemate', 'independence', 'privacy', 'correct', 'challenge', 'answerable role'):
            self.assertIn(phrase, visible)
        review = text(self.slides[25])
        for phrase in ('affected people', 'competing values', 'not the user', 'contestation route', 'accountable role'):
            self.assertIn(phrase, review)

    def test_preserve_project_and_no_new_final_quiz_announcement(self):
        visible = text(self.slides[17])
        for phrase in ('A0 poster', '3-5 minute video', 'One-page mediation brief', '40%',
                       'research 30%', 'impact 30%', 'communication 20%', 'Video 10%', 'documentation 10%'):
            self.assertIn(phrase, visible)
        self.assertNotIn('final quiz', ' '.join(text(s).lower() for s in self.slides[:30]))
        self.assertIn('Neither announce a final-quiz format nor cancel it', self.plan)
        self.assertIn('does not cancel that milestone', self.plan)

    def test_only_two_reflective_questions_no_workshop_artifact_collection(self):
        activities = [(i, s) for i, s in enumerate(self.slides, 1) if s.cp]
        self.assertEqual([i for i, _ in activities], [3, 30])
        for i, s in activities:
            self.assertEqual(s.cp['type'], 'short_answer')
            self.assertFalse(s.cp['multiple'])
            self.assertFalse(s.cp['hide_names'])
            self.assertIn(s.title, self.plan)
        self.assertFalse(any(s.cp for s in self.slides[20:29]))

    def test_actual_report_hook_attaches_and_withholds_synthetic_mapping(self):
        questions = [s for s in self.slides if s.cp]
        entries = [{'activity': 'week12-synthetic-not-live', 'question': questions[0].title},
                   {'activity': None, 'question': questions[1].title, 'withheld': 'synthetic private'}]
        module = self.load_with_mapping(entries)
        mapped = [s for s in module.S if s.cp]
        self.assertEqual(mapped[0].report, 'https://app.classpoint.io/activity/week12-synthetic-not-live')
        self.assertFalse(mapped[1].report)
        self.assertTrue(any(r.url == mapped[0].report for e in mapped[0].els if hasattr(e, 'paras')
                            for p in e.paras for r in p.runs))
        self.assertFalse(any(s.report for s in self.slides))

    def test_actual_report_hook_rejects_count_and_text_drift_and_empty_is_safe(self):
        for entries in ([{'activity': 'synthetic'}],
                        [{'activity': 'synthetic', 'question': 'changed'}, {'activity': None}]):
            with self.assertRaises(ValueError):
                self.load_with_mapping(entries)
        self.assertFalse(any(s.report for s in self.load_with_mapping([]).S))

    def test_clickable_attributed_exact_version_readings(self):
        from deck.week12 import REFS
        urls = {r.url for s in self.slides for e in s.els if hasattr(e, 'paras')
                for p in e.paras for r in p.runs if r.url}
        for _, url in REFS.values():
            self.assertIn(url, urls)
        self.assertIn('https://arxiv.org/html/2507.00286v2', urls)

    def test_sharma_reading_links_are_separate_native_paragraphs(self):
        for slide in (self.slides[12], self.slides[31]):
            paragraphs = [p for e in slide.els if hasattr(e, 'paras') for p in e.paras]
            final = [p for p in paragraphs if any(r.url == 'https://doi.org/10.1145/3663547.3746335'
                                                  for r in p.runs)]
            author = [p for p in paragraphs if any(r.url == 'https://arxiv.org/html/2507.00286v2'
                                                   for r in p.runs)]
            self.assertEqual(len(final), 1)
            self.assertEqual(len(author), 1)
            self.assertIsNot(final[0], author[0])

    def test_original_native_diagrams_bounds_and_semantic_order(self):
        for index, labels in [(5, ['OBSERVE', 'PROPOSE', 'CHECK + ACT', 'INSPECT']),
                              (13, ['CAPTURE', 'REVIEW', 'EDIT OR REFUSE', 'SHARE'])]:
            slide = self.slides[index]
            visible = text(slide)
            positions = [visible.index(label) for label in labels]
            self.assertEqual(positions, sorted(positions))
            self.assertEqual(sum(e.kind == 'rect' and e.y == 355 for e in slide.els), 4)
            for el in slide.els:
                if getattr(el, 'name', '').startswith('chrome-'):
                    continue
                if hasattr(el, 'paras'):
                    self.assertLessEqual(el.y + el.h, 1000)

    def test_all_native_geometry_and_footer_chrome(self):
        for i, slide in enumerate(self.slides, 1):
            with self.subTest(slide=i, title=slide.title):
                for el in slide.els:
                    if all(hasattr(el, a) for a in ('x', 'y', 'w', 'h')):
                        self.assertGreaterEqual(el.x, 0)
                        self.assertGreaterEqual(el.y, 0)
                        self.assertLessEqual(el.x + el.w, 1921)
                        self.assertLessEqual(el.y + el.h, 1081)
                if getattr(slide, 'chrome', True):
                    for name in ('chrome-footer', 'chrome-num'):
                        self.assertEqual(sum(getattr(e, 'name', '') == name for e in slide.els), 1)
                    self.assertIn('WEEK 12', text(slide))

    def test_only_week12_build_registration_no_navigation_change(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertEqual(config['course']['decks'].count('week12'), 1)
        self.assertEqual(config['course']['decks'][:7],
                         [f'week{i:02d}' for i in range(1, 8)])
        self.assertFalse(any(n['href'] == 'week12/' for n in config['nav']))
        self.assertEqual(self.deck['pdf'], 'SD2112-week12.pdf')
        self.assertFalse((ROOT / 'deck/week12-reports.json').exists())


if __name__ == '__main__':
    unittest.main()
