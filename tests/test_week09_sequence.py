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
        self.assertEqual(len(self.slides), 43)
        self.assertEqual(self.slides[29].title, 'Break.\n15 minutes.')
        self.assertEqual(self.slides[33].title, 'Investigate your existing decision.')
        self.assertEqual(self.slides[35].title, 'Change one decision inside your product.')
        self.assertEqual(self.slides[39].title, 'Keep the evidence and the open question.')
        self.assertTrue(all('REFERENCE SHELF' in text(s) for s in self.slides[40:]))

    def test_protected_break_research_and_redesign(self):
        for pos, phrase in [(29, '15 minutes'), (33, '30 min'), (35, '30 min')]:
            self.assertIn(phrase, text(self.slides[pos]))
        plan = (ROOT / 'lessons/week09-lesson-plan.md').read_text()
        for interval in ('75–90', '90–105', '105–135', '135–165', '165–180'):
            self.assertIn(interval, plan)
        self.assertIn('twenty minutes redesign then ten test planning', self.slides[35].notes)

    def test_no_new_collection_or_deadline_and_existing_milestone_preserved(self):
        self.assertFalse(any(s.cp for s in self.slides))
        self.assertIn('No new submission or deadline', text(self.slides[35]))
        finish = text(self.slides[39])
        for phrase in ('concept board + bias register', 'Canvas', 'no new mark, upload or deadline'):
            self.assertIn(phrase, finish)

    def test_mechanisms_and_uncertainty_are_explicit(self):
        self.assertIn('unobserved, not disliked', text(self.slides[9]))
        self.assertIn('NOT LEARNED', text(self.slides[8]))
        self.assertIn('cosine(Q,A) = 0.8', text(self.slides[8]))
        self.assertIn('Near does not mean true, fair', text(self.slides[8]))
        self.assertIn('faithful', self.slides[11].notes)

    def test_task_first_walkthroughs_and_authentic_figures(self):
        from deck.week09 import REFS, STUDY_GUIDES
        walkthroughs = [s for s in self.slides if any(getattr(e, 'name', '') == 'study-task-body' for e in s.els)]
        self.assertEqual(len(walkthroughs), len(REFS))
        self.assertEqual(set(STUDY_GUIDES), set(REFS))
        for slide in walkthroughs:
            for name in ('study-task', 'study-comparison', 'study-example', 'study-measurement'):
                label = next(e for e in slide.els if getattr(e, 'name', '') == name+'-label')
                body = next(e for e in slide.els if getattr(e, 'name', '') == name+'-body')
                self.assertEqual(body.y-label.y, 52)
        r1 = text(walkthroughs[0]); r4 = text(walkthroughs[1]); r5 = text(walkthroughs[2])
        self.assertIn('NOT A PARTICIPANT EXPERIMENT', r1)
        self.assertIn('INSTRUCTOR ILLUSTRATION', r1)
        self.assertIn('1,270', r4)
        self.assertIn('own denominator', r4)
        self.assertIn('DOCUMENTATION PROPOSAL / NOT AN EXPERIMENT', r5)
        self.assertIn('No experiment', r5)
        self.assertIn('n=2,387', text(walkthroughs[3]))
        self.assertIn('0-100%', text(walkthroughs[4]))
        self.assertIn('ADAPTED FROM METHODS', text(walkthroughs[4]))
        self.assertEqual(sum(s.bg == '#246E70' for s in self.slides), 4)
        images = [e for s in self.slides for e in s.els if getattr(e, 'name', '') == 'paper-image']
        self.assertEqual(len(images), 8)
        self.assertTrue(all(Path(e.src).is_file() for e in images))
        for slide in self.slides:
            for el in slide.els:
                if getattr(el, 'name', '') == 'paper-title':
                    self.assertEqual((el.x,el.y,el.w,el.h),(120,184,1680,140))
                    self.assertEqual(el.paras[0].runs[0].size,72)
                if getattr(el, 'name', '') == 'paper-citation':
                    self.assertEqual(el.y,956)
                    self.assertLessEqual(el.y+el.h,1000-6)
        self.assertIn('No significant partisanship', self.slides[24].notes)
        self.assertIn('DIFFERENT n=50', self.slides[27].notes)

    def test_source_crops_and_mobile_order_are_verifiable(self):
        import hashlib, json
        records = json.loads((ROOT / 'deck/assets/week09/provenance.json').read_text())
        self.assertEqual(len(records), 11)
        for record in records:
            path = ROOT / 'deck/assets/week09' / record['asset']
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record['sha256'])
            self.assertTrue(record['source_url'].startswith('https://'))
        slide = next(s for s in self.slides if s.title == 'Following is not just a feed setting.')
        names = [getattr(e, 'name', '') for e in slide.els]
        image_indices = [i for i, name in enumerate(names) if name == 'paper-image']
        explanation = next(i for i, e in enumerate(slide.els) if getattr(e, 'x', None) == 120 and getattr(e, 'y',None) == 780)
        self.assertLess(max(image_indices), explanation)

    def test_distribution_specific_rights_assessment_is_not_false_clearance(self):
        import json
        records = json.loads((ROOT/'deck/assets/week09/provenance.json').read_text())
        for r in records:
            review = r['distribution_review_20261022']
            self.assertIn('public', review['intended_distribution'])
            if r['paper'] in ('R1', 'R2', 'R5'):
                self.assertTrue(review['basis_supported'])
                self.assertIn('section 39(1)', review['basis'])
                self.assertIn('section 39(2)', review['basis'])
                self.assertIn('GATED', review['historical_author_review']['public_reuse_status'])
                self.assertTrue(review['sufficient_acknowledgment']['title'])
                self.assertTrue(review['sufficient_acknowledgment']['authors'])
                self.assertIn('Not blanket legal clearance', review['boundary'])
            if r['paper'] in ('R2', 'R5'):
                self.assertIn('SUPPORTED_BOUNDED_EXCEPTION', review['public_reuse_status'])
                self.assertIsNone(review['remaining_artifact_condition'])
                self.assertTrue(review['sufficient_acknowledgment']['standalone_native_verified'])
                self.assertIn('Full source title is absent', review['historical_acknowledgment_condition'])
            if r['paper'] == 'R1':
                self.assertIn('SUPPORTED_BOUNDED_EXCEPTION', review['public_reuse_status'])
            if r['paper'] == 'R2':
                self.assertIn('CC BY-NC-ND 4.0', review['licence'])
                self.assertIn('no licence permission', review['licence'])
        readme = (ROOT/'deck/assets/week09/README.md').read_text()
        for phrase in ('FAQ 16', 'FAQ 17', 'FAQ 18', 'potential market',
                       'standalone', 'not permission', 'title and author'):
            self.assertIn(phrase, readme)

    def test_standalone_credits_mobile_locator_and_worked_register(self):
        visible = '\n'.join(text(s) for s in self.slides)
        self.assertIn("The political effects of X's feed algorithm", visible)
        self.assertIn('Gauthier, Hodler, Widmer & Zhuravskaya', visible)
        self.assertIn('Datasheets for Datasets', visible)
        self.assertIn('Gebru et al.', visible)
        chart = self.slides[24]
        self.assertIn('Switch ON / OFF', text(chart))
        self.assertNotIn('Left: turn algorithm', text(chart))
        notes = next(s.notes for s in self.slides if s.title == 'Who might this revision miss?')
        for phrase in ('Worked row / instructor illustration', 'false positive=',
                       'false negative=', 'Proposed recourse=', 'not a new submission'):
            self.assertIn(phrase, notes)

    def test_primary_links_are_native_runs(self):
        urls = [r.url for s in self.slides for e in s.els if hasattr(e, 'paras')
                for p in e.paras for r in p.runs if r.url]
        from deck.week09 import REFS
        for _, url in REFS.values():
            self.assertIn(url, urls)
        licence_url = 'https://creativecommons.org/licenses/by/4.0/'
        self.assertEqual(urls.count(licence_url), 7)
        self.assertEqual(len(urls), 24)

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
        self.assertIn('INVENTED', text(self.slides[30]))
        self.assertIn('Relevance: 9', text(self.slides[30]))
        self.assertIn('Novelty: 1', text(self.slides[30]))
        self.assertIn('B: disliked', text(self.slides[9]))
        for phrase in ('7.4', '7.0', '5.6', '5.0', '7.5', '7.1', '4.5', '3.4'):
            self.assertIn(phrase, text(self.slides[31]))
        self.assertIn('Do not present this weighted rule as a learned recommender', self.slides[30].notes)
        self.assertIn('No evidence that B is fairer', self.slides[31].notes)

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
                        self.assertLessEqual(e.y + e.h, 994 if getattr(e, 'name', '') == 'paper-citation' else 990)
            if s.chrome:
                self.assertEqual(sum(getattr(e, 'name', '') == 'chrome-footer' for e in s.els), 1)
                number = next(e for e in s.els if getattr(e, 'name', '') == 'chrome-num')
                self.assertEqual(number.paras[0].runs[0].text, f'{i:02d}')

    def test_published_week_is_registered_and_linked(self):
        conf = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertEqual(conf['course']['decks'].count('week09'), 1)
        self.assertEqual([w for w in conf['course']['decks'] if w in [f'week{i:02d}' for i in range(1,9)]],
                         [f'week{i:02d}' for i in range(1,9)])
        self.assertTrue(any(n['href'] == 'week09/' for n in conf['nav']))
        homepage = (ROOT / 'site/index.html').read_text()
        self.assertIn('href="week09/"', homepage)
        self.assertIn('href="week09/SD2112-week09.pdf"', homepage)
        self.assertEqual(self.deck['pdf'], 'SD2112-week09.pdf')

    def test_exported_notes_and_native_links_if_built(self):
        for name in ('week09.pptx', 'week09-classpoint.pptx'):
            path = ROOT / 'export' / name
            if not path.exists():
                self.skipTest('build artifacts not present')
            with zipfile.ZipFile(path) as z:
                slides = [n for n in z.namelist() if __import__('re').match(r'ppt/slides/slide\d+\.xml$', n)]
                self.assertEqual(len(slides), 43)
                for i, s in enumerate(self.slides, 1):
                    root = E.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml'))
                    texts = [''.join(p.itertext()) for p in root.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}t')]
                    self.assertIn(s.notes, texts)
                rels = '\n'.join(z.read(n).decode() for n in z.namelist() if n.endswith('.rels'))
                self.assertIn('https://doi.org/10.1038/s41586-026-10098-2', rels)
                self.assertIn('https://creativecommons.org/licenses/by/4.0/', rels)


if __name__ == '__main__':
    unittest.main()
