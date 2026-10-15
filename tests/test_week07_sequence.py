"""Week 7 instructor brief: quiz, teams and a provisional AI product concept."""
import ast
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
        from deck.week07 import DECK, S
        cls.slides, cls.deck = S, DECK

    def slide(self, title):
        matches = [s for s in self.slides if s.title == title]
        self.assertEqual(len(matches), 1, title)
        return matches[0]

    def test_quiz_precedes_project_teaching(self):
        quiz = self.slide('Mid-term quiz.\n12:00-12:30.')
        self.assertEqual(self.slides.index(quiz), 2)
        for phrase in ('Canvas', 'Weeks 1-6', '10%', '12:00-12:30'):
            self.assertIn(phrase.lower(), slide_text(quiz).lower())
        self.assertLess(self.slides.index(quiz), self.slides.index(self.slide('Find your X.')))
        self.assertFalse(any(s.cp for s in self.slides))

    def test_team_and_live_demo_precede_seeding(self):
        titles = [s.title for s in self.slides]
        sequence = ['Build a team of 4-5.', 'Watch Gio register a team.',
                    'Start with a person. Not a model.', 'Choose an idea you can explain.',
                    'Register the team. Deliver the concept.']
        positions = [titles.index(t) for t in sequence]
        self.assertEqual(positions, sorted(positions))
        demo = slide_text(self.slide(sequence[1]))
        self.assertIn('live', demo.lower())
        self.assertIn('Canvas', demo)

    def test_ai_is_inside_product_not_just_design_workflow(self):
        text = slide_text(self.slide('AI in the process is not AI in the product.')).lower()
        for phrase in ('inside', 'product', 'using ai', 'incorporating ai'):
            self.assertIn(phrase, text)
        self.assertIn('human', slide_text(self.slide('What does the product do, step by step?')).lower())

    def test_collection_is_canvas_team_and_provisional_concept(self):
        text = slide_text(self.slide('Register the team. Deliver the concept.')).lower()
        for phrase in ('canvas', 'team', 'concept', 'provisional'):
            self.assertIn(phrase, text)
        plan = (ROOT / 'lessons/week07-lesson-plan.md').read_text()
        self.assertIn('not the formal Week 8 proposal', plan)
        self.assertIn('No new assessment weight', plan)

    def test_existing_assessments_are_preserved(self):
        project = slide_text(self.slide('Today is a seed. Week 13 is the showcase.'))
        for phrase in ('40%', 'A0 poster', '3-5 minute video', 'one-page mediation brief', 'Week 8'):
            self.assertIn(phrase, project)
        reflection = slide_text(self.slide('Your individual reflection is separate.'))
        for phrase in ('20%', '1000', 'at least three', 'Weeks 2-6', 'images', 'Canvas', 'AI-writing process note'):
            self.assertIn(phrase, reflection)

    def test_week_is_registered_and_has_report_hook(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week07', config['course']['decks'])
        self.assertTrue(any(n['href'] == 'week07/' for n in config['nav']))
        site = (ROOT / 'site/index.html').read_text()
        self.assertIn('href="week07/"', site)
        self.assertIn('week07/SD2112-week07.pdf', site)
        source = (ROOT / 'deck/week07.py').read_text()
        tree = ast.parse(source)
        self.assertTrue(any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                            and n.func.id == 'attach_reports' for n in ast.walk(tree)))
        self.assertIn('week07-reports.json', source)
        self.assertEqual(self.deck['pdf'], 'SD2112-week07.pdf')

    def test_elements_fit_canvas_and_footer_identifies_week(self):
        for slide in self.slides:
            with self.subTest(title=slide.title):
                self.assertIn('WEEK 07', slide_text(slide))
                for el in slide.els:
                    if all(hasattr(el, a) for a in ('x', 'y', 'w', 'h')):
                        self.assertGreaterEqual(el.x, 0)
                        self.assertGreaterEqual(el.y, 0)
                        self.assertLessEqual(el.x + el.w, 1921)
                        self.assertLessEqual(el.y + el.h, 1081)


if __name__ == '__main__':
    unittest.main()
