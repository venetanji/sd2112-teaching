"""Week 8: timing, evidence boundaries and research-first project work."""
from pathlib import Path
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(run.text for el in slide.els if hasattr(el, 'paras')
                    for p in el.paras for run in p.runs)


class Week08Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week08 import S, DECK, MAIN_SLIDE_COUNT
        cls.slides, cls.deck, cls.main_count = S, DECK, MAIN_SLIDE_COUNT

    def test_main_route_and_break_preserve_the_recovered_budget(self):
        self.assertEqual(self.main_count, 32)
        self.assertEqual(len(self.slides), 42)
        self.assertEqual(self.slides[20].title, 'Break.\n15 minutes.')
        self.assertIn('75-90', text(self.slides[20]))
        self.assertIn('40 min', text(self.slides[24]))
        self.assertIn('25 min', text(self.slides[27]))
        self.assertIn('170-180', text(self.slides[30]))

    def test_research_precedes_scope_and_does_not_collect_new_submissions(self):
        self.assertIn('2-3 papers', text(self.slides[24]))
        self.assertIn('mixed or missing', text(self.slides[24]))
        self.assertIn('Read beyond the abstract', self.slides[25].title)
        self.assertIn('CHANGE / REMOVE', text(self.slides[27]))
        self.assertFalse(any(s.cp for s in self.slides))
        self.assertIn('one-page proposal', text(self.slides[31]))
        self.assertIn('necessary data', text(self.slides[27]))

    def test_reviewed_causal_and_relationship_boundaries_remain_on_main_route(self):
        self.assertEqual(self.slides[10].title, 'Source awareness and authenticity ratings.')
        self.assertIn('six months', text(self.slides[10]))
        self.assertEqual(self.slides[11].title, 'A preferred reply is not a chosen source.')
        self.assertIn('not randomly assigned', self.slides[11].notes)
        self.assertIn('not an established relationship', self.slides[11].notes)
        self.assertIn('Seven-day', text(self.slides[12]))
        self.assertIn('65% vs 59%', text(self.slides[12]))

    def test_appendix_covers_all_thirteen_papers_and_notes_companion_matches(self):
        appendix = ' '.join(text(s) for s in self.slides[self.main_count:])
        for i in range(1, 14):
            self.assertIn(f'R{i}', appendix)
        notes = (ROOT / 'lessons/week08-speaker-notes.md').read_text()
        for i, slide in enumerate(self.slides, 1):
            self.assertIn(f'## {i:02d} / ' + slide.title.replace('\n', ' '), notes)
            self.assertIn(slide.notes, notes)

    def test_confirmed_teaching_arc_is_not_a_provisional_schedule(self):
        finish = self.slides[31]
        for phrase in ('Week 9: recommendations and bias', 'Week 10: interactive Double Diamond',
                       'Weeks 11-12: ethics', 'Week 13: showcase'):
            self.assertIn(phrase, text(finish))
        self.assertIn('instructor is absent', finish.notes)
        for phrase in ('exact dates', 'coverage person', 'ESFQ', 'quiz policy'):
            self.assertIn(phrase, finish.notes)
        self.assertNotIn('proposed later Double Diamond', finish.notes)
        for file in ('week08-lesson-plan.md', 'week08-references.md'):
            companion = (ROOT / 'lessons' / file).read_text()
            for phrase in ('Week 9', 'Week 10', 'Week 13', 'confirmed'):
                self.assertIn(phrase, companion)

    def test_recovered_r2_and_r8_shorthand_preserves_the_audited_limits(self):
        plan = (ROOT / 'lessons/week08-lesson-plan.md').read_text()
        r2 = next(line for line in plan.splitlines() if line.startswith('11. '))
        r8 = next(line for line in plan.splitlines() if line.startswith('12. '))
        for phrase in ('six-month', 'attrition', 'does not isolate', 'authenticity'):
            self.assertIn(phrase, r2)
        for phrase in ('chosen, not randomly assigned', 'established relationships'):
            self.assertIn(phrase, r8)
        register = (ROOT / 'lessons/week08-references.md').read_text()
        self.assertIn('does not isolate a causal disclosure effect', register)
        self.assertIn('chosen, not randomly assigned', register)

    def test_manual_demo_and_access_limits_are_explicit(self):
        demo = ' '.join(text(s) + s.notes for s in self.slides[21:24])
        for phrase in ('manual', 'abstract', 'Scopus', 'metadata', 'offline', 'NOT preflighted'):
            self.assertIn(phrase, demo)
        self.assertTrue((ROOT / 'lessons/week08-demo-fallback.md').exists())

    def test_claim_boundaries_and_primary_links(self):
        from deck.week08 import REFS
        research = ' '.join(text(s) + s.notes for s in self.slides[8:17])
        for phrase in ('working paper', 'long-term deskilling', 'waitlist',
                       'six months', 'correlation', 'correction', 'intentions'):
            self.assertIn(phrase, research)
        for key, (_, url) in REFS.items():
            self.assertIn(url, (ROOT / 'deck/week08.py').read_text())
        self.assertIn('10.1371/journal.pmen.0000426', research)

    def test_every_slide_has_substantive_notes_and_fits_the_canvas(self):
        for slide in self.slides:
            with self.subTest(title=slide.title):
                self.assertGreater(len(slide.notes), 120)
                for el in slide.els:
                    if all(hasattr(el, a) for a in ('x', 'y', 'w', 'h')):
                        self.assertGreaterEqual(el.x, 0)
                        self.assertGreaterEqual(el.y, 0)
                        self.assertLessEqual(el.x + el.w, 1921)
                        self.assertLessEqual(el.y + el.h, 1081)
                        if hasattr(el, 'paras') and el.y < 1000:
                            self.assertLessEqual(el.y + el.h, 1000)
                if getattr(slide, 'chrome', True):
                    for name in ('chrome-footer', 'chrome-num'):
                        self.assertEqual(sum(getattr(e, 'name', '') == name for e in slide.els), 1)

    def test_registered_without_changing_the_syllabus_or_report_contract(self):
        cfg = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week08', cfg['course']['decks'])
        self.assertEqual(self.deck['pdf'], 'SD2112-week08.pdf')
        self.assertIn('attach_reports(S,', (ROOT / 'deck/week08.py').read_text())


if __name__ == '__main__':
    unittest.main()
