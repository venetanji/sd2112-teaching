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
        self.assertEqual([i for _, _, a, b, _ in self.timing for i in range(a, b + 1)], list(range(1, 38)))
        self.assertEqual(len(self.slides), 42)
        for first, minutes in [(28, 30), (31, 35), (35, 20)]:
            self.assertIn(f'{minutes} min', text(self.slides[first - 1]))
        self.assertEqual(self.slides[26].title, 'Break.\nFifteen minutes.')

    def test_actual_slide_map_and_notes_match_all_slides(self):
        mapping = self.plan.split('<!-- slide-map:start -->')[1].split('<!-- slide-map:end -->')[0]
        rows = re.findall(r'^\| (\d+) \| (.*?) \| (.*?) \|$', mapping, re.M)
        self.assertEqual(len(rows), len(self.slides))
        companion = (ROOT / 'lessons/week12-speaker-notes.md').read_text()
        sections = re.split(r'^## \d+ / .*?\n\n', companion, flags=re.M)[1:]
        self.assertEqual(len(sections), 42)
        for i, (s, row, note) in enumerate(zip(self.slides, rows, sections), 1):
            self.assertEqual(row[:2], (str(i), s.title.replace('\n', ' / ')))
            self.assertEqual(note.strip(), s.notes.strip())
            self.assertGreater(len(s.notes.split()), 55, s.title)

    def test_sequence_papers_break_activities_close_and_reference_shelf(self):
        self.assertEqual(self.slides[15].title, 'An explanation did not fix wrong advice here.')
        self.assertEqual(self.slides[18].title, 'Private from a helper. Exposed to whom?')
        self.assertEqual(self.slides[27].title, 'Walk through three low-risk situations.')
        self.assertEqual(self.slides[30].title, 'Paired review. Then swap roles.')
        self.assertEqual(self.slides[34].title, 'Choose the change that matters most.')
        self.assertTrue(all('REFERENCE SHELF' in text(s) for s in self.slides[37:]))

    def test_evidence_is_bounded_on_visible_slides_not_just_notes(self):
        cecil = text(self.slide('Can people reject incorrect advice?'))
        for phrase in ('1,403', '16 fictional CVs', '75% correct', 'percentage of trials', '1-7', 'ILLUSTRATION'):
            self.assertIn(phrase, cecil)
        sharma = text(self.slide('How do people manage visual privacy?'))
        for phrase in ('21 US', 'one-hour', 'thematic coding', 'not a population percentage', 'ADAPTED FROM THE SOURCE'):
            self.assertIn(phrase, sharma)
        self.assertIn('not proof of equal effects', text(self.slide('An explanation did not fix wrong advice here.')))
        self.assertIn('not tested for effectiveness', text(self.slide('Private from a helper. Exposed to whom?')))
        self.assertIn('Proposed flow, not tested protection', text(self.slide('Privacy controls must be usable before sharing.')))
        self.assertIn('Remote analysis can disclose data', text(self.slide('Privacy controls must be usable before sharing.')))
        self.assertIn('not proven safer', text(self.slide('Same promise. A different contract.')))

    def test_low_risk_complete_static_workflow_and_nonchatbot_validity(self):
        activity = self.slides[27]
        for phrase in ('paper/static', 'SIMULATION', 'ordinary, ambiguous', 'out-of-scope'):
            self.assertIn(phrase, text(activity))
        for phrase in ('No third-party actions', 'Paper cards and static screens', 'classifiers', 'installations'):
            self.assertIn(phrase, activity.notes)
        self.assertIn('A physical product, recommender or visual system', text(self.slides[11]))
        self.assertIn('without disability simulation', text(self.slides[28]))
        self.assertIn('No new deadline, grade or upload', text(self.slides[34]))

    def test_ethical_argument_names_people_values_contestation_accountability(self):
        visible = text(self.slides[21])
        for phrase in ('housemate', 'independence', 'privacy', 'correct', 'challenge', 'answerable role'):
            self.assertIn(phrase, visible)
        review = text(self.slides[32])
        for phrase in ('affected people', 'competing values', 'not the user', 'contestation route', 'accountable role'):
            self.assertIn(phrase, review)

    def test_preserve_project_and_no_new_final_quiz_announcement(self):
        visible = text(self.slides[24])
        for phrase in ('A0 poster', '3-5 minute video', 'One-page mediation brief', '40%',
                       'research 30%', 'impact 30%', 'communication 20%', 'Video 10%', 'documentation 10%'):
            self.assertIn(phrase, visible)
        self.assertNotIn('final quiz', ' '.join(text(s).lower() for s in self.slides[:37]))
        self.assertIn('Neither announce a final-quiz format nor cancel it', self.plan)
        self.assertIn('does not cancel that milestone', self.plan)

    def test_only_two_reflective_questions_no_workshop_artifact_collection(self):
        activities = [(i, s) for i, s in enumerate(self.slides, 1) if s.cp]
        self.assertEqual([i for i, _ in activities], [3, 37])
        for i, s in activities:
            self.assertEqual(s.cp['type'], 'short_answer')
            self.assertFalse(s.cp['multiple'])
            self.assertFalse(s.cp['hide_names'])
            self.assertIn(s.title, self.plan)
        self.assertFalse(any(s.cp for s in self.slides[27:36]))

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
        questions = [s.title for s in self.slides if s.cp]
        valid = [{'activity': None, 'question': q} for q in questions]
        with self.assertRaises(ValueError):
            self.load_with_mapping(valid + [valid[0]])
        for index in range(2):
            changed = [dict(e) for e in valid]
            changed[index]['question'] = 'changed'
            with self.assertRaises(ValueError):
                self.load_with_mapping(changed)
        self.assertFalse(any(s.report for s in self.load_with_mapping([]).S))

    def test_clickable_attributed_exact_version_readings(self):
        from deck.week12 import REFS
        urls = {r.url for s in self.slides for e in s.els if hasattr(e, 'paras')
                for p in e.paras for r in p.runs if r.url}
        for _, url in REFS.values():
            self.assertIn(url, urls)
        self.assertIn('https://arxiv.org/html/2507.00286v2', urls)

    def test_sharma_reading_links_are_separate_native_paragraphs(self):
        for slide in (self.slide('How do people manage visual privacy?'), self.slides[38]):
            paragraphs = [p for e in slide.els if hasattr(e, 'paras') for p in e.paras]
            final = [p for p in paragraphs if any(r.url == 'https://doi.org/10.1145/3663547.3746335'
                                                  for r in p.runs)]
            author = [p for p in paragraphs if any(r.url == 'https://arxiv.org/html/2507.00286v2'
                                                   for r in p.runs)]
            self.assertEqual(len(final), 1)
            self.assertEqual(len(author), 1)
            self.assertIsNot(final[0], author[0])

    def test_original_native_diagrams_bounds_and_semantic_order(self):
        for index, labels in [(8, ['OBSERVE', 'PROPOSE', 'CHECK + ACT', 'INSPECT']),
                              (19, ['CAPTURE', 'REVIEW', 'EDIT OR REFUSE', 'SHARE'])]:
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

    def test_source_pairs_grid_and_documentation_not_evaluated_safeguard(self):
        from PIL import Image
        from deck.week12_studies import GUIDES
        titles = [s.title for s in self.slides]
        for key, result_title in [('R3', 'An observation can change the next step.'),
                                  ('R1', 'An explanation did not fix wrong advice here.'),
                                  ('R2', 'Private from a helper. Exposed to whom?'),
                                  ('R4', 'Make the scope inspectable.')]:
            task, result = self.slide(GUIDES[key]['title']), self.slide(result_title)
            self.assertEqual(titles.index(task.title) + 1, titles.index(result.title))
            for slide in (task, result):
                header = next(e for e in slide.els if e.name == 'paper-title')
                self.assertEqual((header.x, header.y, header.w, header.h), (120, 184, 1680, 140))
                self.assertEqual(header.paras[0].runs[0].size, 72)
                self.assertTrue(any(e.y == 956 for e in slide.els))
                for e in slide.els:
                    if e.name.endswith('-label') and e.name.startswith('study-'):
                        body = next(x for x in slide.els if x.name == e.name.replace('-label', '-body'))
                        self.assertEqual(body.y - e.y, 52)
            for image in [e for e in result.els if e.kind == 'image']:
                with Image.open(image.src) as crop:
                    self.assertGreater(crop.width, 100)
            self.assertIn('PDF p.', text(result))
        framework = text(self.slide(GUIDES['R4']['title']))
        self.assertIn('not a participant experiment', framework)
        self.assertIn('not a causal safety comparison', framework)
        self.assertIn('not a tested safeguard', text(self.slide('Make the scope inspectable.')))
        self.assertIn('Line = 70.61% baseline; bars = standard errors', text(self.slide('An explanation did not fix wrong advice here.')))
        self.assertIn('N328 (214 advice recipients)', text(self.slide('An explanation did not fix wrong advice here.')))
        self.assertIn('Table 1 prompts, not findings', text(self.slide('Private from a helper. Exposed to whom?')))
        self.assertIn('not a safety result', text(self.slide('A tool result becomes the next input.')))
        for heading in ('What are we\ndelegating?', 'What may people\nrely on?', 'What will you\nchange?'):
            self.assertFalse(self.slide(heading).cp)
        self.assertTrue((ROOT / 'deck/assets/week12/provenance.md').is_file())

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
        self.assertEqual(config['course']['decks'][:8],
                         [f'week{i:02d}' for i in range(1, 9)])
        self.assertFalse(any(n['href'] == 'week12/' for n in config['nav']))
        self.assertEqual(self.deck['pdf'], 'SD2112-week12.pdf')
        self.assertFalse((ROOT / 'deck/week12-reports.json').exists())


if __name__ == '__main__':
    unittest.main()
