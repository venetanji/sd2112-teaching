"""Week 13: showcase content, policy boundaries, native geometry and report hook."""
from pathlib import Path
from unittest.mock import patch
import runpy
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(run.text for el in slide.els if hasattr(el, 'paras')
                    for para in el.paras for run in para.runs)


class Week13Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week13 import S, DECK, MAIN_SLIDE_COUNT, STAFF_SLIDES
        cls.slides, cls.deck, cls.main = S, DECK, MAIN_SLIDE_COUNT
        cls.staff = STAFF_SLIDES

    def slide(self, title):
        matches = [s for s in self.slides if s.title == title]
        self.assertEqual(len(matches), 1, title)
        return matches[0]

    def test_student_exports_exclude_staff_readiness_material(self):
        self.assertEqual(len(self.deck['slides']), 33)
        exported = ' '.join(text(s) for s in self.deck['slides'])
        self.assertNotIn('INSTRUCTOR REVIEW ONLY', exported)
        for phrase in ('Reconcile the published assessment', 'READINESS GATE',
                       'This draft supplies', 'not a live timer',
                       'This draft announces'):
            self.assertNotIn(phrase, exported)

    def test_actual_route_and_instructor_appendix(self):
        self.assertEqual((len(self.slides), self.main), (33, 33))
        self.assertEqual(len(self.staff), 4)
        for s in self.staff:
            self.assertIn('INSTRUCTOR REVIEW ONLY', text(s))
        order = ['Can I understand the product?', 'A campus route recommender.',
                 'Notice. Interpret. Ask.', 'Present. Visit. Listen.',
                 'What did someone else make visible?', 'Two routes. Different commitments.',
                 'A recommendation rearranges the choice.', 'Selection is a design act.',
                 'Defend your answer with a design choice.']
        indexes = [self.slides.index(self.slide(t)) for t in order]
        self.assertEqual(indexes, sorted(indexes))

    def test_existing_deliverables_and_project_subweights(self):
        t = text(self.slide('Three ways to explain one product.'))
        for phrase in ('40%', 'A0', '3-5', 'ONE-PAGE', 'mediation'):
            self.assertIn(phrase.lower(), t.lower())
        t = text(self.slide('Polish is only part of the argument.'))
        for phrase in ('30% research', '30% ethical', '20% communication', '10% video', '10% team', 'NOT COURSE WEIGHTS'):
            self.assertIn(phrase.lower(), t.lower())

    def test_no_new_collection_and_report_noop(self):
        self.assertFalse(any(s.cp or s.report for s in self.slides))
        from deckgen import attach_reports as real_attach
        calls = []

        def record(slides, path):
            calls.append(path)
            return real_attach(slides, [])

        with patch('deckgen.attach_reports', side_effect=record):
            runpy.run_path(str(ROOT / 'deck/week13.py'))
        self.assertEqual(calls, [ROOT / 'deck/week13-reports.json'])

    def test_report_drift_is_not_silenced_by_deck(self):
        from deckgen import attach_reports as real_attach

        def drift(slides, path):
            return real_attach(slides, [{'activity': None, 'question': 'Synthetic unrun question'}])

        with patch('deckgen.attach_reports', side_effect=drift):
            with self.assertRaisesRegex(ValueError, '1 activities but 0 ClassPoint slides'):
                runpy.run_path(str(ROOT / 'deck/week13.py'))

    def test_zero_collection_does_not_create_anonymity_or_peer_marks(self):
        t = text(self.slide('Notice. Interpret. Ask.'))
        self.assertIn('FORMATIVE', t)
        self.assertIn('do not invent a score', t)
        self.assertIn('No visit quota', self.slide('Notice. Interpret. Ask.').notes)
        self.assertIn('not a new feedback log submission', self.slide('Listen for the decision behind the comment.').notes)

    def test_manual_holds_have_no_fake_timing(self):
        hold = self.slide('Present. Visit. Listen.')
        self.assertIn('cue', text(hold))
        self.assertIn('not a live timer', hold.notes)
        self.assertIn('manually', hold.notes)
        self.assertIn('Static', self.slide('Pause.\nReturn on cue.').notes)
        for s in self.slides:
            self.assertFalse(getattr(s, 'sketch', None))
        self.assertNotIn('countdown', text(hold).lower())

    def test_published_quiz_remains_unresolved_without_invented_rules(self):
        t = text(next(s for s in self.staff if s.title == 'Reconcile the published assessment.'))
        for phrase in ('20%', 'whole-course', 'Week 13', 'authorized decision'):
            self.assertIn(phrase, t)
        main_text = ' '.join(text(s) for s in self.slides[:self.main])
        for banned in ('30-question', '35-minute', '26 teams', 'five graders', 'four rounds',
                       'peer prize', 'Blackboard', '11:30', 'Z209'):
            self.assertNotIn(banned, main_text)
        conditional = text(next(s for s in self.staff if s.title == 'Prove the fair fits the confirmed session.'))
        self.assertIn('Only if', conditional)
        self.assertIn('180 - Q - A - 15', conditional)
        self.assertNotIn('Q =', conditional)

    def test_synthesis_is_not_an_exam_scope_restriction(self):
        for name in ('Two routes. Different commitments.', 'Where is the model doing the work?',
                     'A recommendation rearranges the choice.', 'Can the person act otherwise?',
                     'Follow the error through the system.', 'Selection is a design act.',
                     'A prompt is a design decision.', 'Keep the questions separate.'):
            self.slide(name)
        notes = ' '.join(s.notes for s in self.slides)
        self.assertIn('not a restriction', notes)
        self.assertIn('not a new', notes)

    def test_fictional_example_and_native_diagram_boundaries(self):
        example = self.slide('A campus route recommender.')
        self.assertIn('NOT A VALIDATED PRODUCT', text(example))
        self.assertIn('Fictional teaching example', example.notes)
        figure = self.slide('A recommendation rearranges the choice.')
        labels = [text(figure).index(v) for v in ('PERSON', 'TECHNOLOGY', 'WORLD')]
        self.assertEqual(labels, sorted(labels))
        self.assertIn('not their canonical', figure.notes)

    def test_native_geometry_and_every_slide_has_useful_notes(self):
        for s in self.slides:
            self.assertGreater(len(s.notes), 150, s.title)
            for el in s.els:
                if s.chrome and hasattr(el, 'paras') and not el.name.startswith('chrome-'):
                    self.assertGreaterEqual(el.x, 0, s.title)
                    self.assertGreaterEqual(el.y, 0, s.title)
                    self.assertLessEqual(el.x + el.w, 1920, s.title)
                    self.assertLessEqual(el.y + el.h, 1000, s.title)

    def test_descriptive_resources_use_native_urls(self):
        shelf = self.slide('Return to the sources, not just the output.')
        urls = [r.url for e in shelf.els if hasattr(e, 'paras') for p in e.paras for r in p.runs if r.url]
        self.assertEqual(len(urls), 5)
        self.assertIn('https://doi.org/10.1145/2751314', urls)
        self.assertTrue(any('/syllabus/' in u for u in urls))

    def test_conceptual_reading_is_self_contained_not_an_experiment(self):
        slide = self.slide('Products shape how we see and act.')
        visible = text(slide)
        for phrase in ('CONCEPTUAL ESSAY', 'QUESTION', 'EXAMPLE / ADAPTED FROM THE ESSAY',
                       'printer defaults to double-sided', 'ARGUMENT / ANALYSIS',
                       'No printing rate or safety result is measured'):
            self.assertIn(phrase, visible)
        self.assertLess(visible.index('EXAMPLE'), visible.index('ARGUMENT / ANALYSIS'))
        self.assertIn('not a participant study', slide.notes)
        self.assertIn('printed pp. 29 and 31', slide.notes)
        self.assertFalse(any(getattr(e, 'src', None) for e in slide.els if not getattr(e, 'name', '').startswith('chrome-')))
        self.assertLess(self.slides.index(slide), self.slides.index(self.slide('A recommendation rearranges the choice.')))

    def test_conceptual_common_grid(self):
        for title in ('Products shape how we see and act.', 'A recommendation rearranges the choice.'):
            slide = self.slide(title)
            heading = next(e for e in slide.els if e.name == 'paper-title')
            self.assertEqual((heading.x, heading.y, heading.w, heading.h), (120, 184, 1680, 140))
            self.assertEqual(heading.paras[0].runs[0].size, 72)
            citation = next(e for e in slide.els if e.name == 'paper-citation')
            self.assertEqual((citation.x, citation.y, citation.w), (120, 956, 1680))
        slide = self.slide('Products shape how we see and act.')
        for name in ('concept-question', 'concept-example', 'concept-argument', 'concept-limit'):
            label = next(e for e in slide.els if e.name == name+'-label')
            body = next(e for e in slide.els if e.name == name+'-body')
            self.assertEqual(body.y-label.y, 52)

    def test_topic_sections_and_reduced_projected_copy(self):
        titles = ('Explain the choice.', 'Notice. Then ask.', 'Making. Using. Living.',
                  'Who chooses? Who answers?')
        indices = [self.slides.index(self.slide(t)) for t in titles]
        self.assertEqual(indices, sorted(indices))
        for title in ('Can I understand the product?', 'Two routes. Different commitments.',
                      'Can the person act otherwise?', 'Follow the error through the system.',
                      'A prompt is a design decision.'):
            self.assertLessEqual(len(text(self.slide(title)).split()), 65, title)

    def test_notes_companion_preserves_exact_native_transcript(self):
        notes = (ROOT / 'lessons/week13-notes.md').read_text()
        for i, slide in enumerate(self.slides, 1):
            self.assertIn(f'### {i:02d} / ' + slide.title.replace('\n', ' '), notes)
            self.assertIn(slide.notes, notes)

    def test_staff_record_preserves_all_readiness_text_outside_export(self):
        notes = (ROOT / 'lessons/week13-notes.md').read_text()
        for slide in self.staff:
            self.assertIn(slide.title, notes)
            self.assertIn(slide.notes, notes)
            for el in slide.els:
                if hasattr(el, 'paras'):
                    for para in el.paras:
                        phrase = ''.join(run.text for run in para.runs)
                        if phrase and not phrase.startswith('INSTRUCTOR REVIEW ONLY'):
                            self.assertIn(phrase, notes)
        self.assertTrue(all(s not in self.deck['slides'] for s in self.staff))

    def test_week13_registration_and_document_synchronization(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week13', config['course']['decks'])
        self.assertFalse(any('week13' in n['href'] for n in config['nav']))
        plan = (ROOT / 'lessons/week13-lesson-plan.md').read_text()
        for phrase in ('33 main-route', 'Four staff-only', '180 - Q - A - 15', 'Unresolved', 'formative'):
            self.assertIn(phrase, plan)
        for name in ('week13-notes.md', 'week13-sources.md', 'week13-verification.md'):
            self.assertTrue((ROOT / 'lessons' / name).exists())


if __name__ == '__main__':
    unittest.main()
