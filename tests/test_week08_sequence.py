"""Week 8: self-contained studies, authentic figures and protected workshop budgets."""
from pathlib import Path
import hashlib
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(run.text for el in slide.els if hasattr(el, 'paras')
                    for p in el.paras for run in p.runs)


class Week08Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week08 import S, DECK, MAIN_SLIDE_COUNT, PAPER_SUMMARIES
        cls.slides, cls.deck, cls.main_count = S, DECK, MAIN_SLIDE_COUNT
        cls.summaries = PAPER_SUMMARIES
        cls.by_title = {s.title: s for s in S}

    def slide(self, title):
        return self.by_title[title]

    def test_weekly_news_is_in_opening_without_extra_time(self):
        opening = self.slides[2]
        visible = text(opening)
        for phrase in ('Kling 4.0', '15 October 2026', 'Vendor', 'keyframes'):
            self.assertIn(phrase.lower(), visible.lower())
        self.assertIn('two minutes within', opening.notes)
        self.assertIn('not independent', opening.notes)
        self.assertIn('not guaranteed', opening.notes)
        self.assertTrue(any('ir.kuaishou.com' in (r.url or '')
                            for e in opening.els if hasattr(e, 'paras')
                            for p in e.paras for r in p.runs))
        plan = (ROOT / 'lessons/week08-lesson-plan.md').read_text()
        self.assertIn(f'3. **{opening.title}**', plan)
        self.assertIn('replacing the previous pair prompt', plan)
        self.assertEqual(len(self.summaries), 9)
        news = (ROOT / 'lessons/week08-news-20261021.md').read_text()
        self.assertIn('48 main-route plus 12 untimed appendix/reference slides (60 total)', news)

    def test_main_route_and_protected_budgets(self):
        self.assertEqual((self.main_count, len(self.slides)), (48, 60))
        self.assertEqual(self.slides[35].title, 'Break.\n15 minutes.')
        for title, duration in [('Break.\n15 minutes.', '75-90'),
                                ('Find 2-3 papers for your product.', '40 min'),
                                ('Change a claim before adding a feature.', '25 min'),
                                ('Show the decision, not a pro/con list.', '170-180')]:
            self.assertIn(duration, text(self.slide(title)))
        self.assertIn('90-105', text(self.slide('Search a condition, not a verdict.')))

    def test_each_taught_paper_has_a_concrete_explanation_pair(self):
        from deck.week08 import STUDY_GUIDES
        expected = ['R1', 'R2', 'R8', 'R6', 'R7', 'R3', 'R4', 'R5']
        main = self.slides[:self.main_count]
        observed = []
        for slide in main:
            labels = text(slide)
            if 'WHAT THEY DID' in labels:
                observed.append(next(k for k in expected if f'/ {k} ' in labels))
        self.assertEqual(observed, expected)
        self.assertEqual(set(STUDY_GUIDES), set(expected + ['R9']))
        for key, guide in STUDY_GUIDES.items():
            self.assertTrue(all(guide.values()))
            self.assertGreater(len(guide['task'].split()), 15)
            self.assertLessEqual(len(guide['task'].split()), 45)
        self.assertIn('No pre-reading is assumed', main[0].notes)

    def test_topic_blocks_and_optional_reading_shelf(self):
        positions = [next(i for i, s in enumerate(self.slides) if s.title == title)
                     for title in ['Seeming care.\nChoosing a source.',
                                   'Relief now.\nAction outside the app.',
                                   'Pleasant is not\nalways helpful.',
                                   'An update can change the relationship.', 'Break.\n15 minutes.']]
        self.assertEqual(positions, sorted(positions))
        r9 = self.slide('Optional / Symptoms improved with support.')
        self.assertGreater(self.slides.index(r9), self.main_count)
        self.assertIn('waitlist', text(r9))
        self.assertIn('consumer-chatbot equivalence', text(r9))

    def test_authentic_figure_assets_have_attribution_links_and_hashes(self):
        from deck.week08 import REFS
        ledger = (ROOT / 'lessons/week08-paper-figures.md').read_text()
        seen = []
        for s in self.slides:
            for e in s.els:
                name = getattr(e, 'name', '')
                if name.startswith('paper-figure-'):
                    key = name.removeprefix('paper-figure-')
                    seen.append(key)
                    p = Path(e.src)
                    self.assertTrue(p.is_file())
                    self.assertEqual(e.fit, 'contain')
                    self.assertEqual(e.url, REFS[key][1])
                    self.assertIn('Fig.', text(s))
                    self.assertIn('PDF p.', text(s))
                    self.assertIn(hashlib.sha256(p.read_bytes()).hexdigest(), ledger)
        self.assertEqual(seen, ['R8', 'R6', 'R7', 'R3', 'R4', 'R5'])
        self.assertIn('CC BY 4.0', ledger)
        self.assertIn('unresolved public-republication clearance', ledger)
        details = [e for s in self.slides for e in s.els
                   if getattr(e, 'name', '').startswith('paper-detail-')]
        self.assertEqual([e.name for e in details], ['paper-detail-R6', 'paper-detail-R4'])
        for e in details:
            self.assertEqual(e.fit, 'contain')
            self.assertEqual(e.url, REFS[e.name.removeprefix('paper-detail-')][1])
            self.assertIn(hashlib.sha256(Path(e.src).read_bytes()).hexdigest(), ledger)

    def test_figure_specific_interpretation_and_denominators(self):
        r7 = self.slide('Rehearsal can lead outside the app.')
        self.assertIn('not an initiation-rate chart', text(r7))
        self.assertIn('not a proven mechanism', text(r7))
        self.assertIn('1,371', text(self.slides[self.slides.index(r7) - 1]))
        self.assertIn('65% with preparation versus 59%', text(r7))
        r4 = self.slide('More right, less willing to repair.')
        self.assertIn('Fig. 4 A+B', text(r4))
        self.assertIn('2,405', text(self.slides[self.slides.index(r4) - 1]))
        self.assertIn('y-axis starts at 2', text(r4))
        r5 = self.slide('Many followed the planted wrong answer.')
        self.assertIn('consulted problems, not people', text(r5))
        self.assertIn('working paper', text(r5).lower())
        self.assertIn('Chat-Engaged Only', r5.notes)
        r3 = self.slide('The same work got different feedback.')
        self.assertIn('not factual accuracy', text(r3))

    def test_perception_and_relationship_boundaries(self):
        r2 = self.slide('Human replies felt more genuine.')
        for phrase in ('Six months', 'did not return', 'does not prove equal'):
            self.assertIn(phrase, text(r2))
        r8 = self.slide('People chose humans but rated AI higher.')
        self.assertIn('not randomly assigned', r8.notes)
        self.assertIn('not an established relationship', r8.notes)
        self.assertIn('not established relationships', text(r8))
        self.assertIn('between-session', text(self.slide('Relief now is not lasting improvement.')))
        self.assertIn('10.1371/journal.pmen.0000426', self.slide('A caring reply is not treatment.').notes)

    def test_research_precedes_scope_with_individual_paper_collection(self):
        self.assertLess(self.slides.index(self.slide('Read beyond the abstract.')),
                        self.slides.index(self.slide('Change a claim before adding a feature.')))
        self.assertEqual(sum(bool(s.cp) for s in self.slides), 3)
        self.assertIn('mixed or missing', text(self.slide('Find 2-3 papers for your product.')))
        self.assertIn('necessary data', text(self.slide('Change a claim before adding a feature.')))
        self.assertIn('one-page proposal', text(self.slide('Your next version needs a reason.')))

    def test_notes_companion_matches_final_native_notes(self):
        companion = (ROOT / 'lessons/week08-speaker-notes.md').read_text()
        appendix = ' '.join(text(s) for s in self.slides[self.main_count:])
        for i in range(1, 14):
            self.assertIn(f'R{i}', appendix)
        for i, s in enumerate(self.slides, 1):
            self.assertIn(f'## {i:02d} / ' + s.title.replace('\n', ' '), companion)
            self.assertIn(s.notes, companion)
            self.assertGreater(len(s.notes), 120)

    def test_confirmed_arc_and_unresolved_logistics_preserved(self):
        finish = self.slide('Your next version needs a reason.')
        for phrase in ('Week 9: recommendations and bias', 'Week 10: interactive Double Diamond',
                       'Weeks 11-12: ethics', 'Week 13: showcase'):
            self.assertIn(phrase, text(finish))
        for phrase in ('instructor is absent', 'exact dates', 'coverage person', 'ESFQ', 'quiz policy'):
            self.assertIn(phrase, finish.notes)

    def test_manual_demo_retains_access_and_offline_gates(self):
        demo = ' '.join(text(self.slide(title)) + self.slide(title).notes for title in (
            'Search a condition, not a verdict.', 'Find. Open. Read. Follow the trail.',
            'Discovery is not paper reading.'))
        for phrase in ('manual', 'abstract', 'Scopus', 'metadata', 'offline', 'NOT preflighted'):
            self.assertIn(phrase, demo)
        self.assertTrue((ROOT / 'lessons/week08-demo-fallback.md').exists())

    def test_canvas_and_footer_bounds(self):
        for s in self.slides:
            for e in s.els:
                if all(hasattr(e, a) for a in ('x', 'y', 'w', 'h')):
                    self.assertGreaterEqual(min(e.x, e.y), 0)
                    self.assertLessEqual(e.x + e.w, 1921)
                    self.assertLessEqual(e.y + e.h, 1081)
                    if hasattr(e, 'paras') and e.y < 1000:
                        self.assertLessEqual(e.y + e.h, 1000)
            if getattr(s, 'chrome', True):
                for name in ('chrome-footer', 'chrome-num'):
                    self.assertEqual(sum(getattr(e, 'name', '') == name for e in s.els), 1)

    def test_registration_and_report_contract_remain(self):
        cfg = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week08', cfg['course']['decks'])
        self.assertEqual(self.deck['pdf'], 'SD2112-week08.pdf')
        self.assertIn('attach_reports(S,', (ROOT / 'deck/week08.py').read_text())


if __name__ == '__main__':
    unittest.main()
