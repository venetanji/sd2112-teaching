"""Week 9 structure, bounded evidence, native fallback and export contracts."""
from decimal import Decimal
from pathlib import Path
import runpy
import tomllib
import unittest
from unittest.mock import patch
import zipfile
import xml.etree.ElementTree as E

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(r.text for e in slide.els if hasattr(e, 'paras')
                    for p in e.paras for r in p.runs)


class Week09Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week09 import S, DECK
        cls.slides, cls.deck = S, DECK

    def test_main_route_and_reference_shelf(self):
        self.assertEqual(len(self.slides), 31)
        self.assertEqual(self.slides[18].title, 'Break.\n15 minutes.')
        self.assertEqual(self.slides[21].title, 'Investigate your existing decision.')
        self.assertEqual(self.slides[23].title, 'Change one decision inside your product.')
        self.assertEqual(self.slides[27].title, 'Keep the evidence and the open question.')
        self.assertTrue(all('REFERENCE SHELF' in text(s) for s in self.slides[28:]))

    def test_protected_break_research_and_redesign(self):
        for pos, phrase in [(18, '15 minutes'), (21, '30 min'), (23, '30 min')]:
            self.assertIn(phrase, text(self.slides[pos]))
        plan = (ROOT / 'lessons/week09-lesson-plan.md').read_text()
        for interval in ('75–90', '90–105', '105–135', '135–165', '165–180'):
            self.assertIn(interval, plan)
        self.assertIn('twenty minutes redesign then ten test planning', self.slides[23].notes)

    def test_no_new_collection_or_deadline_and_existing_milestone_preserved(self):
        self.assertFalse(any(s.cp for s in self.slides))
        self.assertIn('No new submission or deadline', text(self.slides[23]))
        finish = text(self.slides[27])
        for phrase in ('concept board + bias register', 'Canvas', 'no new mark, upload or deadline'):
            self.assertIn(phrase, finish)

    def test_mechanisms_and_uncertainty_are_explicit(self):
        self.assertIn('unobserved, not disliked', text(self.slides[6]))
        self.assertIn('NOT LEARNED', text(self.slides[5]))
        self.assertIn('cosine(Q,A) = 0.8', text(self.slides[5]))
        self.assertIn('does not mean true, fair', text(self.slides[5]))
        self.assertIn('faithful', self.slides[8].notes)

    def test_evidence_visible_limits(self):
        r2, r3 = text(self.slides[15]), text(self.slides[16])
        for phrase in ('2023', 'Seven-week', 'active US', 'No significant effect', 'self-reported', 'not symmetric'):
            self.assertIn(phrase, r2)
        for phrase in ('controlled', 'Accurate algorithms', 'not a live feed', 'Long-term persistence'):
            self.assertIn(phrase.lower(), r3.lower())
        self.assertIn('not a face-identification/recommender', self.slides[12].notes)

    def test_primary_links_are_native_runs(self):
        urls = [r.url for s in self.slides for e in s.els if hasattr(e, 'paras')
                for p in e.paras for r in p.runs if r.url]
        from deck.week09 import REFS
        for _, url in REFS.values():
            self.assertIn(url, urls)
        self.assertEqual(len(urls), 9)

    def test_toy_arithmetic_outputs_and_boundaries(self):
        from deck.week09_demo import ITEMS, rank
        self.assertEqual(len(ITEMS), 4)
        self.assertEqual([(a, c) for a, b, c in rank('0.8')],
                         [('A', Decimal('7.4')), ('B', Decimal('7.0')), ('C', Decimal('5.6')), ('D', Decimal('5.0'))])
        self.assertEqual([(a, c) for a, b, c in rank('0.3')],
                         [('D', Decimal('7.5')), ('C', Decimal('7.1')), ('B', Decimal('4.5')), ('A', Decimal('3.4'))])
        self.assertEqual([r[0] for r in rank('0.5')][:2], ['C', 'D'])
        self.assertEqual(rank(0), rank('0'))
        self.assertEqual(rank(1), rank('1'))
        for w in (-1, 2, 'NaN', 'Infinity'):
            with self.assertRaises(ValueError):
                rank(w)
        self.assertIn('INVENTED', text(self.slides[19]))
        self.assertIn('Relevance: 9', text(self.slides[19]))
        self.assertIn('Novelty: 1', text(self.slides[19]))
        self.assertIn('B: disliked', text(self.slides[6]))
        for phrase in ('7.4', '7.0', '5.6', '5.0', '7.5', '7.1', '4.5', '3.4'):
            self.assertIn(phrase, text(self.slides[20]))
        self.assertIn('Do not present this weighted rule as a learned recommender', self.slides[19].notes)
        self.assertIn('No evidence that B is fairer', self.slides[20].notes)

    def test_report_hook_invocation_and_stale_mapping_rejection(self):
        from deckgen import attach_reports
        calls = []
        def empty(slides, source):
            calls.append(Path(source).name)
            return attach_reports(slides, [], quiet=True)
        with patch('deckgen.attach_reports', side_effect=empty):
            loaded = runpy.run_path(str(ROOT / 'deck/week09.py'))
        self.assertEqual(calls, ['week09-reports.json'])
        self.assertFalse(any(s.report for s in loaded['S']))
        def stale(slides, source):
            return attach_reports(slides, [{'activity': None, 'question': 'synthetic stale entry'}], quiet=True)
        with patch('deckgen.attach_reports', side_effect=stale):
            with self.assertRaisesRegex(ValueError, 'drifted apart'):
                runpy.run_path(str(ROOT / 'deck/week09.py'))

    def test_companion_matches_every_native_note_and_plan_title(self):
        companion = (ROOT / 'lessons/week09-speaker-notes.md').read_text()
        plan = (ROOT / 'lessons/week09-lesson-plan.md').read_text()
        for i, s in enumerate(self.slides, 1):
            self.assertIn(f'## {i:02d} / {s.title.replace(chr(10), " ")}', companion)
            self.assertIn(s.notes, companion)
            self.assertIn(s.title.replace('\n', ' '), plan)
            self.assertGreater(len(s.notes), 250)

    def test_native_geometry_footer_and_reading_order(self):
        for i, s in enumerate(self.slides, 1):
            for e in s.els:
                if all(hasattr(e, a) for a in ('x', 'y', 'w', 'h')):
                    self.assertGreaterEqual(e.x, 0)
                    self.assertGreaterEqual(e.y, 0)
                    self.assertLessEqual(e.x + e.w, 1920)
                    self.assertLessEqual(e.y + e.h, 1080)
                    if s.chrome and not getattr(e, 'name', '').startswith('chrome-'):
                        self.assertLessEqual(e.y + e.h, 990)
            if s.chrome:
                self.assertEqual(sum(getattr(e, 'name', '') == 'chrome-footer' for e in s.els), 1)
                number = next(e for e in s.els if getattr(e, 'name', '') == 'chrome-num')
                self.assertEqual(number.paras[0].runs[0].text, f'{i:02d}')

    def test_only_build_list_extended_not_navigation(self):
        conf = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertEqual(conf['course']['decks'].count('week09'), 1)
        self.assertEqual(conf['course']['decks'][:7],
                         [f'week{i:02d}' for i in range(1, 8)])
        self.assertFalse(any(n['href'] == 'week09/' for n in conf['nav']))
        self.assertEqual(self.deck['pdf'], 'SD2112-week09.pdf')

    def test_exported_notes_and_native_links_if_built(self):
        for name in ('week09.pptx', 'week09-classpoint.pptx'):
            path = ROOT / 'export' / name
            if not path.exists():
                self.skipTest('build artifacts not present')
            with zipfile.ZipFile(path) as z:
                slides = [n for n in z.namelist() if __import__('re').match(r'ppt/slides/slide\d+\.xml$', n)]
                self.assertEqual(len(slides), 31)
                for i, s in enumerate(self.slides, 1):
                    root = E.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml'))
                    texts = [''.join(p.itertext()) for p in root.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}t')]
                    self.assertIn(s.notes, texts)
                rels = '\n'.join(z.read(n).decode() for n in z.namelist() if n.endswith('.rels'))
                self.assertIn('https://doi.org/10.1038/s41586-026-10098-2', rels)


if __name__ == '__main__':
    unittest.main()
