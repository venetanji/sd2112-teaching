"""Week 7: recap coverage/order, bounded team activity and collection integrity."""
import ast
from copy import deepcopy
from importlib import import_module
from pathlib import Path
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]


def slide_text(slide):
    return ' '.join(run.text for el in slide.els if hasattr(el, 'paras')
                    for paragraph in el.paras for run in paragraph.runs)


class Week07Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week07 import DECK, RECAP, S
        cls.slides, cls.deck, cls.recap = S, DECK, RECAP

    def slide(self, title):
        matches = [s for s in self.slides if s.title == title]
        self.assertEqual(len(matches), 1, title)
        return matches[0]

    def test_twenty_original_concept_slides_cover_all_six_weeks_before_quiz(self):
        from week07_recap import SELECTION
        self.assertEqual(set(SELECTION), set(range(1, 7)))
        self.assertEqual(len(self.recap), 20)
        self.assertEqual(self.slides[2:22], self.recap)
        quiz = self.slide('Mid-term quiz.\n12:00-12:30.')
        self.assertEqual(self.slides.index(quiz), 23)
        for phrase in ('Canvas', 'Weeks 1-6', '10%', '12:00-12:30'):
            self.assertIn(phrase.lower(), slide_text(quiz).lower())
        self.assertLess(self.slides.index(quiz), self.slides.index(self.slide('One concept. One product image.')))
        for week, titles in SELECTION.items():
            originals = import_module(f'week{week:02d}').S
            for title in titles:
                original, = (s for s in originals if s.title == title)
                selected = self.slide(title)
                self.assertIsNot(selected, original)
                self.assertFalse(selected.cp)
                self.assertFalse(selected.report)
                self.assertIn(f'RECAP WEEK {week:02d}', slide_text(selected))
                self.assertIn(f'WEEK {week:02d}', slide_text(original))
                self.assertEqual([e for e in selected.els if not getattr(e, 'name', '').startswith('chrome-')],
                                 [e for e in original.els if not getattr(e, 'name', '').startswith('chrome-')])

    def test_question_inbox_follows_recap_until_noon_before_quiz(self):
        inbox = self.slide('Ask me anything.')
        self.assertEqual(self.slides.index(inbox), 22)
        self.assertEqual(inbox.cp['type'], 'short_answer')
        self.assertTrue(inbox.cp['multiple'])
        for phrase in ('11:45-12:00', 'ClassPoint', 'until 12:00'):
            self.assertIn(phrase, slide_text(inbox))
        plan = (ROOT / 'lessons/week07-lesson-plan.md').read_text(encoding='utf-8')
        for phrase in ('11:30-11:45', '11:45-12:00', '12:00-12:30'):
            self.assertIn(phrase, plan)

    def test_only_two_twenty_minute_team_submissions_follow_demo(self):
        activities = [s for s in self.slides if s.cp]
        self.assertEqual([s.cp['type'] for s in activities], ['short_answer', 'short_answer', 'image_upload'])
        activities = activities[1:]
        self.assertLess(self.slides.index(self.slide('Watch Gio register a team.')),
                        self.slides.index(activities[0]))
        for slide in activities:
            text = slide_text(slide)
            self.assertIn('20 min', text)
            self.assertIn('team', text)
            self.assertIn('representative', text)
            self.assertIn('ClassPoint', text)
        self.assertFalse(activities[0].cp['multiple'])
        self.assertIn('Canvas', slide_text(activities[0]))
        self.assertIn('4-5', slide_text(activities[0]))
        self.assertIn('one short core-concept text', slide_text(activities[0]))
        self.assertIn('one image', slide_text(activities[1]))

    def test_report_links_attach_to_inbox_and_both_team_collections(self):
        from deckgen import attach_reports
        activities = deepcopy([s for s in self.slides if s.cp])
        entries = [{'activity': f'week07-test-{i}', 'question': s.title}
                   for i, s in enumerate(activities)]
        self.assertEqual(attach_reports(activities, entries, quiet=True), 3)
        self.assertTrue(all(s.report for s in activities))
        self.assertFalse(any(s.report for s in self.slides if s.cp))

    def test_product_brief_and_finish_match_the_two_outputs(self):
        text = slide_text(self.slide('One concept. One product image.')).lower()
        for phrase in ('incorporate ai', 'during use', 'text', 'image'):
            self.assertIn(phrase, text)
        finish = slide_text(self.slide('Check the text, image and team.'))
        for phrase in ('one product image', 'core-concept text', 'same team name', 'Canvas'):
            self.assertIn(phrase, finish)
        plan = (ROOT / 'lessons/week07-lesson-plan.md').read_text(encoding='utf-8')
        self.assertIn('not the formal Week 8 proposal', plan)
        self.assertIn('No new assessment weight', plan)
        self.assertIn('No separate Canvas concept submission', plan)

    def test_existing_assessments_are_preserved(self):
        project = slide_text(self.slide('Today is a seed. Week 13 is the showcase.'))
        for phrase in ('40%', 'A0 poster', '3-5 minute video', 'one-page mediation brief', 'Week 8'):
            self.assertIn(phrase, project)
        reflection = slide_text(self.slide('Your individual reflection is separate.'))
        for phrase in ('20%', '1000', 'at least three', 'Weeks 2-6', 'images', 'Canvas', 'AI-writing process note'):
            self.assertIn(phrase, reflection)

    def test_week_and_news_are_registered_and_report_hook_is_retained(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text(encoding='utf-8'))
        for name in ('week07', 'news20261014'):
            self.assertIn(name, config['course']['decks'])
            self.assertTrue(any(n['href'] == name + '/' for n in config['nav']))
        site = (ROOT / 'site/index.html').read_text(encoding='utf-8')
        self.assertIn('href="week07/"', site)
        self.assertIn('week07/SD2112-week07.pdf', site)
        source = (ROOT / 'deck/week07.py').read_text(encoding='utf-8')
        tree = ast.parse(source)
        self.assertTrue(any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                            and n.func.id == 'attach_reports' for n in ast.walk(tree)))
        self.assertIn('week07-reports.json', source)
        self.assertEqual(self.deck['pdf'], 'SD2112-week07.pdf')

    def test_elements_fit_canvas_with_single_footer_and_number(self):
        for slide in self.slides:
            with self.subTest(title=slide.title):
                if getattr(slide, 'chrome', True) or slide in self.recap:
                    self.assertIn('WEEK 07', slide_text(slide))
                    for name in ('chrome-footer', 'chrome-num'):
                        self.assertEqual(sum(getattr(e, 'name', '') == name for e in slide.els), 1)
                for el in slide.els:
                    if all(hasattr(el, a) for a in ('x', 'y', 'w', 'h')):
                        self.assertGreaterEqual(el.x, 0)
                        self.assertGreaterEqual(el.y, 0)
                        self.assertLessEqual(el.x + el.w, 1921)
                        self.assertLessEqual(el.y + el.h, 1081)


if __name__ == '__main__':
    unittest.main()
