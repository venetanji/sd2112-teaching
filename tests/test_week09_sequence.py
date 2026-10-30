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


def teaching_content(slide):
    """Detail can move to notes; short visual labels need not repeat paragraphs."""
    return text(slide) + ' ' + slide.notes + ' ' + ' '.join(
        getattr(e, 'placeholder', '') for e in slide.els)


class Week09Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week09 import S, DECK
        cls.slides, cls.deck = S, DECK

    def slide(self, title):
        matches = [s for s in self.slides if s.title.replace('\n', ' ') == title]
        self.assertEqual(len(matches), 1, f'Expected one slide titled {title!r}')
        return matches[0]

    def test_main_route_and_reference_shelf(self):
        self.assertEqual(len(self.slides), 51)
        # Positions are intentional only for route boundaries, not content checks.
        for position, title in {
            1: 'Inside the feed.', 4: 'How a feed selects.',
            13: 'Whose errors count?', 24: 'Not just a mirror.',
            29: 'A feed can change us.', 36: 'Break. 15 minutes.',
            37: 'Same four items. Two scoring rules.',
            39: 'Find and question bias.', 42: 'Change the interaction.',
            46: 'From spotting bias to changing the relation.',
            47: 'Keep the example and the open question.',
        }.items():
            self.assertEqual(self.slides[position - 1].title.replace('\n', ' '), title)
        self.assertFalse(any('REFERENCE SHELF' in text(s) for s in self.slides[:47]))
        self.assertTrue(all('REFERENCE SHELF' in text(s) for s in self.slides[47:]))
        self.assertEqual([s.title for s in self.slides if s.bg == '#246E70'], [
            'How a feed selects.', 'Whose errors count?', 'Not just a mirror.',
            'A feed can change us.', 'Find and question bias.', 'Change the interaction.',
        ])

    def test_protected_break_research_and_redesign(self):
        for title, phrase in [
            ('Break. 15 minutes.', '15 minutes'),
            ('Find two examples of AI bias.', '30 min'),
            ('Change how the person can respond.', '30 min'),
        ]:
            self.assertIn(phrase, text(self.slide(title)))
        plan = (ROOT / 'lessons/week09-lesson-plan.md').read_text()
        for interval in ('0–10', '10–25', '25–45', '45–60', '60–75',
                         '75–90', '90–105', '105–135', '135–165', '165–180'):
            self.assertIn(interval, plan)
        self.assertIn('twenty minutes redesign then ten test planning',
                      self.slide('Change how the person can respond.').notes)
        self.assertIn('Friday 30 October 2026', plan)
        self.assertIn('confirmed by Giovanni on 28 October 2026', plan)

    def test_no_new_collection_or_deadline_and_existing_milestone_preserved(self):
        self.assertFalse(any(s.cp for s in self.slides))
        self.assertIn('No new submission or deadline', text(self.slide('Change how the person can respond.')))
        finish = text(self.slide('Keep the example and the open question.'))
        for phrase in ('concept board + bias register', 'Canvas', 'no new mark, upload or deadline'):
            self.assertIn(phrase, finish)

    def test_bias_distinctions_and_selected_traces(self):
        distinction = self.slide('Learning is selective. Is it unfair?')
        for phrase in ('INDUCTIVE BIAS', 'LEARNED PATTERN', 'HARMFUL BIAS',
                       'not automatically an error', 'Who is affected'):
            self.assertIn(phrase, teaching_content(distinction))
        for phrase in ('provocation, not a technical definition', 'Statistical bias',
                       'does not excuse preventable discrimination'):
            self.assertIn(phrase, distinction.notes)
        traces = self.slide('Whose humanity does AI reflect?')
        for phrase in ('not all people equally', 'Collection, labels and objectives',
                       'reproduce, transform or amplify'):
            self.assertIn(phrase, teaching_content(traces))
        for phrase in ('synthetic data', 'not a census', 'not by itself proof of discrimination'):
            self.assertIn(phrase, traces.notes)

    def test_mediation_transparency_and_reflective_use_are_bounded(self):
        recall = self.slide('Using a tool also shapes our experience.')
        for phrase in ('HEIDEGGER', 'IHDE', 'VERBEEK'):
            self.assertIn(phrase, teaching_content(recall))
        for phrase in ('not identical theories', 'Do not conflate',
                       'Neither original book was newly read'):
            self.assertIn(phrase, recall.notes)
        transparency = self.slide('Transparent in which sense?')
        for phrase in ('VAN DEN EEDE', 'IN USE', 'IN REFLECTION',
                       'Unnoticed does not mean neutral', 'not the whole context'):
            self.assertIn(phrase, teaching_content(transparency))
        for phrase in ('use/context', 'double vision', 'not quotations',
                       'not translate contextual transparency directly into visible model internals',
                       'transparent alterity'):
            self.assertIn(phrase, transparency.notes)
        reflection = self.slide('Pause. Compare. Choose differently.')
        for phrase in ('without retraining', 'not a validated intervention',
                       'no meaningful response', 'not automatically better'):
            self.assertIn(phrase, reflection.notes)
        self.assertIn('does not guarantee fairness',
                      text(self.slide('Keep the example and the open question.')))

    def test_two_examples_close_comparison_and_concrete_response(self):
        finding = self.slide('Find two examples of AI bias.')
        for phrase in ('Compare two examples', 'Choose one', 'system, task, source or prompt',
                       'Who is favoured, excluded or misrepresented'):
            self.assertIn(phrase, teaching_content(finding))
        for phrase in ('ten minutes finding two examples', 'fifteen comparing',
                       'five identifying uncertainty', 'No required paid account',
                       'existing private team notes'):
            self.assertIn(phrase, finding.notes)
        evidence = self.slide('What makes this an example of bias?')
        for phrase in ('Observation', 'Interpretation', 'Consequence', 'Uncertainty'):
            self.assertIn(phrase, text(evidence))
        for phrase in ('model/version/date', 'exact invented input', 'one pair remains exploratory',
                       'Do not infer the training corpus', "classmates' accounts"):
            self.assertIn(phrase, evidence.notes)
        revision = self.slide('Change how the person can respond.')
        self.assertIn('compare, question, correct, override or refuse', text(revision).lower())
        self.assertIn('no usable response', revision.notes)
        test = self.slide('What changes in the interaction?')
        for phrase in ('original interaction', 'meaningful response', 'failure condition',
                       'Awareness alone is not a fairness fix'):
            self.assertIn(phrase, teaching_content(test))
        self.assertIn('rather than recruit participants', test.notes)
        self.assertIn('Separate awareness, ability to act, task success', test.notes)

    def test_mechanisms_and_uncertainty_are_explicit(self):
        self.assertIn('unobserved, not disliked', text(self.slide('Learn from a pattern of choices.')))
        self.assertIn('NOT LEARNED', teaching_content(self.slide('Near depends on the representation.')))
        self.assertIn('cosine(Q,A) = 0.8', teaching_content(self.slide('Near depends on the representation.')))
        self.assertIn('Near does not mean true, fair', teaching_content(self.slide('Near depends on the representation.')))
        self.assertIn('faithful', self.slide('A reason is not the whole mechanism.').notes)

    def test_task_first_walkthroughs_and_authentic_figures(self):
        from deck.week09 import REFS, STUDY_GUIDES
        walkthroughs = [s for s in self.slides if any(getattr(e, 'name', '') == 'study-diagram' for e in s.els)]
        self.assertEqual(len(walkthroughs), len(REFS))
        self.assertEqual(set(STUDY_GUIDES), set(REFS))
        from deck.week09_visual_studies import PANELS
        for slide in walkthroughs:
            image = next(e for e in slide.els if getattr(e, 'name', '') == 'study-diagram')
            self.assertTrue(Path(image.src).is_file())
            self.assertGreater(image.w * image.h, 500000)
            self.assertTrue(image.placeholder)
            self.assertIn('Full walkthrough retained', slide.notes)
            key = Path(image.src).stem.upper()
            for label, short_copy in PANELS[key][1]:
                self.assertIn(short_copy.replace('\n', ' '), text(slide))
            self.assertIn(PANELS[key][2], text(slide))
            for field in ('task', 'comparison', 'example', 'measured'):
                self.assertIn(STUDY_GUIDES[key][field], slide.notes)
            # Attribution/licence links are not part of the explanation budget.
            explanation = ' '.join(r.text for e in slide.els if hasattr(e, 'paras')
                                   and getattr(e, 'name', '') != 'paper-citation'
                                   for p in e.paras for r in p.runs)
            self.assertLess(len(explanation.split()), 90)
        r1 = teaching_content(self.slide('How does YouTube narrow the choice?'))
        r4 = teaching_content(self.slide('Who disappears inside an average?'))
        r5 = teaching_content(self.slide('What should travel with a dataset?'))
        self.assertIn('NOT A PARTICIPANT EXPERIMENT', r1)
        self.assertIn('INSTRUCTOR ILLUSTRATION', r1)
        self.assertIn('1,270', r4)
        self.assertIn('own denominator', r4)
        self.assertIn('DOCUMENTATION PROPOSAL / NOT AN EXPERIMENT', r5)
        self.assertIn('No experiment', r5)
        self.assertIn('n=2,387', text(self.slide('Can changing a feed change people?')))
        self.assertIn('0-100%', text(self.slide('Can advice change your next judgement?')))
        self.assertIn('ADAPTED FROM METHODS', text(self.slide('Can advice change your next judgement?')))
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
        self.assertIn('No significant partisanship', self.slide('Following is not just a feed setting.').notes)
        self.assertIn('DIFFERENT n=50', self.slide('Learning can go in either direction.').notes)

    def test_source_crops_and_mobile_order_are_verifiable(self):
        import hashlib, json
        records = json.loads((ROOT / 'deck/assets/week09/provenance.json').read_text())
        self.assertEqual(len(records), 11)
        for record in records:
            path = ROOT / 'deck/assets/week09' / record['asset']
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record['sha256'])
            self.assertTrue(record['source_url'].startswith('https://'))
        slide = self.slide('Following is not just a feed setting.')
        names = [getattr(e, 'name', '') for e in slide.els]
        image_indices = [i for i, name in enumerate(names) if name == 'paper-image']
        explanation = next(i for i, e in enumerate(slide.els) if getattr(e, 'x', None) == 120 and getattr(e, 'y',None) == 780)
        self.assertLess(max(image_indices), explanation)

    def test_papers_keep_concrete_plain_english_examples_on_screen(self):
        examples = {
            'How does YouTube narrow the choice?': ('INVENTED EXAMPLE', '100 workshops', 'pottery'),
            'Can changing a feed change people?': ('ILLUSTRATIVE EXAMPLE', 'Two people', 'who they follow'),
            'Can advice change your next judgement?': ('WORKED EXAMPLE', '53%', '73%', '65%', 'unaided'),
            'Who disappears inside an average?': ('INVENTED EXAMPLE', '5 wrong labels', '5% error'),
            'What should travel with a dataset?': ('INVENTED EXAMPLE', 'workshop', 'Who paid them?'),
        }
        for title, phrases in examples.items():
            slide = self.slide(title)
            for phrase in phrases:
                self.assertIn(phrase, text(slide))
            self.assertEqual(sum(getattr(e,'name','') == 'study-diagram' for e in slide.els), 1)
            self.assertIn('not a source figure or measured data', slide.notes)
        self.assertEqual(Decimal('.4')*53 + Decimal('.6')*73, Decimal(65))

    def test_visual_replacements_have_assets_and_no_stale_column(self):
        visual_slides = []
        for slide in self.slides:
            visuals = [e for e in slide.els if getattr(e,'name','').startswith(
                ('study-diagram','mechanism-illustration','mediation-'))]
            if visuals:
                visual_slides.append(slide)
                for image in visuals:
                    self.assertTrue(Path(image.src).is_file())
                    self.assertTrue(image.placeholder)
                    self.assertLessEqual(image.y+image.h, 875)
        self.assertEqual(len(visual_slides), 16)
        transparency = self.slide('Transparent in which sense?')
        self.assertNotIn('IN REFLECTION: can I notice', text(transparency))
        heading = next(e for e in transparency.els if hasattr(e,'paras')
                       and 'Transparent in which sense?' in ' '.join(
                           r.text for p in e.paras for r in p.runs))
        self.assertEqual(heading.w, 1680)
        # Native projection text only; labels inside illustrations are not counted.
        self.assertLess(sum(len(text(s).split()) for s in self.slides), 2800)

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
        chart = self.slide('Following is not just a feed setting.')
        self.assertIn('Switch ON / OFF', text(chart))
        self.assertIn('more conservative', text(chart))
        self.assertIn('Bars show uncertainty', text(chart))
        self.assertIn('Crossing zero: no change', text(chart))
        self.assertNotIn('Left: turn algorithm', text(chart))
        notes = self.slide('Who might this revision miss?').notes
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
        from deck.week09_mediation import MITCHELL, VERBEEK, EEDE
        for url in (MITCHELL, VERBEEK, EEDE):
            self.assertIn(url, urls)
        self.assertEqual(len(urls), 27)

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
        self.assertIn('INVENTED', text(self.slide('Same four items. Two scoring rules.')))
        self.assertIn('Relevance: 9', text(self.slide('Same four items. Two scoring rules.')))
        self.assertIn('Novelty: 1', text(self.slide('Same four items. Two scoring rules.')))
        self.assertIn('B: disliked', text(self.slide('Learn from a pattern of choices.')))
        for phrase in ('7.4', '7.0', '5.6', '5.0', '7.5', '7.1', '4.5', '3.4'):
            self.assertIn(phrase, text(self.slide('The objective changes the shortlist.')))
        self.assertIn('Do not present this weighted rule as a learned recommender', self.slide('Same four items. Two scoring rules.').notes)
        self.assertIn('No evidence that B is fairer', self.slide('The objective changes the shortlist.').notes)

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
        expected = '\n\n'.join(
            f'## {i:02d} / {s.title.replace(chr(10), " ")}\n\n{s.notes}'
            for i, s in enumerate(self.slides, 1)) + '\n'
        self.assertEqual(companion[companion.index('## 01 / '):], expected)
        import re
        mapped_titles = re.findall(r'^\d+\. \*\*(.*?)\*\*', plan, re.MULTILINE)
        self.assertEqual(mapped_titles, [s.title.replace('\n', ' ') for s in self.slides])
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

    def test_only_build_list_extended_not_navigation(self):
        conf = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertEqual(conf['course']['decks'].count('week09'), 1)
        self.assertEqual([w for w in conf['course']['decks'] if w in [f'week{i:02d}' for i in range(1,9)]],
                         [f'week{i:02d}' for i in range(1,9)])
        self.assertFalse(any(n['href'] == 'week09/' for n in conf['nav']))
        self.assertEqual(self.deck['pdf'], 'SD2112-week09.pdf')

    def test_exported_notes_and_native_links_if_built(self):
        for name in ('week09.pptx', 'week09-classpoint.pptx'):
            path = ROOT / 'export' / name
            if not path.exists():
                self.skipTest('build artifacts not present')
            with zipfile.ZipFile(path) as z:
                slides = [n for n in z.namelist() if __import__('re').match(r'ppt/slides/slide\d+\.xml$', n)]
                self.assertEqual(len(slides), len(self.slides))
                for i, s in enumerate(self.slides, 1):
                    root = E.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml'))
                    texts = [''.join(p.itertext()) for p in root.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}t')]
                    self.assertEqual([p for p in s.notes.splitlines() if p], texts)
                rels = '\n'.join(z.read(n).decode() for n in z.namelist() if n.endswith('.rels'))
                self.assertIn('https://doi.org/10.1038/s41586-026-10098-2', rels)
                self.assertIn('https://creativecommons.org/licenses/by/4.0/', rels)


if __name__ == '__main__':
    unittest.main()
