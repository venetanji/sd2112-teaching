"""Week 11 theory-first route, evidence boundaries and export integrity."""
from pathlib import Path
import hashlib
import json
import runpy
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(run.text for el in slide.els if hasattr(el, 'paras')
                    for para in el.paras for run in para.runs)


class Week11Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week11 import S, SCHEDULE, DECK, REFS, MAIN_SLIDE_COUNT
        cls.slides, cls.schedule, cls.deck, cls.refs, cls.main_count = S, SCHEDULE, DECK, REFS, MAIN_SLIDE_COUNT

    def slide(self, heading):
        return next(slide for slide in self.slides if slide.title == heading)

    def test_timing_protected_blocks_and_full_route(self):
        self.assertEqual((self.main_count, len(self.slides)), (36, 37))
        self.assertEqual([(start, end) for start, end, _, _ in self.schedule],
                         [(0, 28), (28, 46), (46, 60), (60, 75), (75, 90),
                          (90, 110), (110, 140), (140, 165), (165, 180)])
        self.assertEqual(sum(end - start for start, end, _, _ in self.schedule), 180)
        self.assertEqual([n for _, _, _, (start, end) in self.schedule for n in range(start, end + 1)],
                         list(range(1, 37)))
        self.assertEqual(self.slides[22].title, 'Break.\n15 minutes.')
        self.assertIn('30 min', text(self.slide('Find one claim and one choice.')))
        self.assertIn('25 min', text(self.slide('Let the argument travel without you.')))
        self.assertFalse(any(s.cp or s.report for s in self.slides))

    def test_theory_precedes_papers_and_reuses_single_example(self):
        self.assertEqual([s.title for s in self.slides[:7]], ['Whose design?',
            'Start with one decision.', 'The tool frames what we notice.',
            'Selection makes a world visible.', 'Trace four different decisions.',
            'Feeling, work, permission, law.', 'Name who can answer.'])
        opening = ' '.join(map(text, self.slides[:7])).lower()
        for term in ('source', 'tool framing', 'interpret, then act', 'included', 'excluded',
                     'editorial choice', 'generate', 'select', 'revise', 'authorise',
                     'feel', 'contribute', 'permission', 'protection',
                     'accountable actor', 'correct or withdraw'):
            self.assertIn(term, opening)
        self.assertIn('fictional', self.slides[1].notes.lower())
        self.assertIn('metal detector', self.slides[2].notes)
        self.assertLess(self.slides.index(self.slide('Name who can answer.')),
                        self.slides.index(self.slide('What did designers describe?')))
        self.assertIn('Three candidates', self.slides[24].title)
        self.assertEqual(sum(s.title == 'A tool also changes what we notice.' for s in self.slides), 0)

    def test_diagrams_show_relationships_not_repeated_row_tables(self):
        expected = {
            'The tool frames what we notice.': ('mediation-', 3, 2),
            'Selection makes a world visible.': ('curation-', 3, 2),
            'Trace four different decisions.': ('agency-', 4, 3),
            'Name who can answer.': ('responsibility-', 4, 3),
            'A complaint is not a verdict.': ('suno-timeline-', 3, 2),
        }
        for title, (prefix, panel_count, arrow_count) in expected.items():
            s = self.slide(title)
            names = [getattr(e, 'name', '') for e in s.els]
            panels = [n for n in names if n.startswith(prefix) and n.endswith('-panel')]
            arrows = [n for n in names if n.startswith(prefix) and n.endswith('-arrow')]
            self.assertEqual(len(panels), panel_count, title)
            self.assertGreaterEqual(len(arrows), arrow_count, title)
            self.assertFalse(any(n.endswith('-body') for n in names))
            if title != 'Name who can answer.':
                self.assertLess(names.index(panels[0]), names.index(arrows[0]))
        names = [getattr(e, 'name', '') for e in self.slide('Name who can answer.').els]
        for n in ('responsibility-editor-panel', 'responsibility-editor-action',
                  'responsibility-feedback-line', 'responsibility-feedback-arrow',
                  'responsibility-return-arrow'):
            self.assertIn(n, names)
        ownership = self.slide('Feeling, work, permission, law.')
        self.assertEqual(sum(getattr(e, 'name', '').startswith('ownership-') and
                             getattr(e, 'name', '').endswith('-panel') for e in ownership.els), 4)

    def test_studies_task_before_result_and_not_causal_overclaims(self):
        for task, result in [('What did designers describe?', 'A participant view is not a legal rule.'),
                             ('Write a story. Change the starting help.', 'Higher ratings can accompany convergence.'),
                             ('What must a dataset explain?', 'Document the choice, including the unknowns.'),
                             ('Would you type more to avoid friction?', 'More input can feel more yours.'),
                             ('Which human expression is protected?', 'Separate protection, permission and credit.')]:
            self.assertLess(self.slides.index(self.slide(task)), self.slides.index(self.slide(result)))
        for title, terms in [('What did designers describe?', ('28 U.S.', '10 junior', '10 senior', '8 professionals', 'themes')),
                             ('Write a story. Change the starting help.', ('293', '600', '1 (not at all) to 9', '0 to 100')),
                             ('Would you type more to avoid friction?', ('29 analyzed', '30 new', 'Baseline first', '0-100')),
                             ('Which human expression is protected?', ('not a participant experiment', 'not Hong Kong legal advice'))]:
            for term in terms:
                self.assertIn(term.lower(), text(self.slide(title)).lower())
        self.assertIn('not a randomized', text(self.slide('What must a dataset explain?')))
        self.assertIn('do not infer that longer prompts earn copyright', self.slide('More input can feel more yours.').notes.lower())

    def test_suno_claims_are_attributed_and_status_is_bounded(self):
        case = self.slides[19:22]
        self.assertEqual([s.title for s in case], ['A complaint is not a verdict.',
                         'Four questions, not one ruling.', 'Settlement is not universal clearance.'])
        visible = ' '.join(map(text, case))
        for term in ('Universal', 'Sony', 'Warner', 'allege', 'fair use', 'settled',
                     'training', 'copyrightability', 'similarity', 'credit',
                     'latest status unverified', 'universal clearance'):
            self.assertIn(term.lower(), (visible + ' '.join(s.title for s in case)).lower())
        self.assertIn('not a verdict', case[0].title)
        self.assertIn('June 5 2026', case[2].notes)
        self.assertIn('unverified', case[2].notes)
        self.assertIn('5 June 2026', text(case[2]))
        self.assertNotIn('Sept. 2026 indexed filing', text(case[2]))
        self.assertNotIn('DISPUTED', text(case[2]))
        self.assertIn('Hong Kong', case[1].notes)
        links = [r.url for s in case for e in s.els if hasattr(e, 'paras')
                 for p in e.paras for r in p.runs if r.url]
        self.assertIn('https://www.riaa.com/wp-content/uploads/2024/06/Suno-complaint-file-stamped20.pdf', links)
        self.assertIn('https://www.wmg.com/news/warner-music-group-and-suno-forge-groundbreaking-partnership', links)
        self.assertIn('https://www.reuters.com/legal/litigation/musicians-union-sues-record-labels-over-ai-licensing-2026-06-05/', links)

    def test_project_contract_and_week12_handover(self):
        all_text = ' '.join(map(text, self.slides))
        for term in ('A0 poster', '3-5 minute video', 'one-page mediation brief', '40%',
                     'current Canvas milestones', '30 / ethics 30 / poster 20 / video 10 / process 10',
                     'WEEK 12', 'delegat'):
            self.assertIn(term.lower(), all_text.lower())
        for term in ('Nov 30', 'Week 14', 'Blackboard', 'Excalidraw', 'Tesla crashes'):
            self.assertNotIn(term, all_text)
        self.assertIn('Week 13 is quiz and posters', self.slides[-2].notes)

    def test_citations_assets_and_native_geometry(self):
        links = [r.url for s in self.slides for e in s.els if hasattr(e, 'paras')
                 for p in e.paras for r in p.runs if r.url]
        self.assertTrue({v[1] for v in self.refs.values()}.issubset(set(links)))
        records = json.loads((ROOT / 'deck/assets/week11/provenance.json').read_text())
        for record in records:
            self.assertEqual(hashlib.sha256((ROOT / 'deck/assets/week11' / record['asset']).read_bytes()).hexdigest(), record['sha256'])
            for field in ('primary_url', 'rights_basis', 'rights_url', 'distribution', 'version', 'location', 'changes'):
                self.assertTrue(record[field])
        self.assertEqual(sum(getattr(e, 'name', '') == 'paper-image'
                             for s in self.slides for e in s.els), 4)
        for slide in self.slides:
            for e in slide.els:
                if all(hasattr(e, key) for key in ('x', 'y', 'w', 'h')):
                    self.assertGreaterEqual(e.x, 0)
                    self.assertGreaterEqual(e.y, 0)
                    self.assertLessEqual(e.x + e.w, 1920)
                    self.assertLessEqual(e.y + e.h, 1080)
                    if slide.chrome and not getattr(e, 'name', '').startswith('chrome-'):
                        self.assertLessEqual(e.y + e.h, 1000)

    def test_repeated_paper_grid_and_authentic_joshi_crop(self):
        from PIL import Image
        for s in self.slides:
            titles = [e for e in s.els if getattr(e, 'name', '') == 'paper-title']
            if not titles:
                continue
            t = titles[0]
            self.assertEqual((t.x, t.y, t.w, t.h), (120, 184, 1680, 140))
            self.assertEqual(t.paras[0].runs[0].size, 72)
            for label in [e for e in s.els if getattr(e, 'name', '').endswith('-label')]:
                body = next(e for e in s.els if getattr(e, 'name', '') == label.name.replace('-label', '-body'))
                self.assertEqual(body.y - label.y, 52)
        result = self.slide('More input can feel more yours.')
        image = next(e for e in result.els if getattr(e, 'name', '') == 'paper-image')
        self.assertEqual(Path(image.src).name, 'joshi-fig1a-motor.png')
        self.assertEqual((image.x, image.y, image.w, image.h), (120, 348, 1010, 515))
        record = next(r for r in json.loads((ROOT / 'deck/assets/week11/provenance.json').read_text())
                      if r['asset'] == 'joshi-fig1a-motor.png')
        self.assertEqual(record['crop_pixels'], [172, 664, 706, 1202])
        self.assertEqual(record['render_dimensions'], [2040, 2640])
        self.assertEqual(record['rights_url'], 'https://creativecommons.org/licenses/by/4.0/')
        with Image.open(ROOT / 'deck/assets/week11' / record['asset']) as cropped:
            self.assertEqual(cropped.size, (534, 538))
        self.assertIn('Panels (b)', result.notes)
        self.assertIn('(b)/(c) omitted', text(result))

    def test_native_notes_and_companion_are_parallel(self):
        notes = (ROOT / 'lessons/week11-speaker-notes.md').read_text()
        self.assertEqual(notes.count('\n## '), len(self.slides))
        for i, s in enumerate(self.slides, 1):
            self.assertGreater(len(s.notes.split()), 35, (i, s.title))
            self.assertIn(s.notes, notes)
        self.assertIn('week11', tomllib.loads((ROOT / 'deckgen.toml').read_text())['course']['decks'])
        self.assertEqual(self.deck['pdf'], 'SD2112-week11.pdf')

    def test_ci_builds_before_export_dependent_tests(self):
        workflow = (ROOT / '.github/workflows/news-preview.yml').read_text()
        self.assertLess(workflow.index("subprocess.run(['deckgen', 'build', *decks]"),
                        workflow.index('python -m unittest discover -s tests -v'))

    def test_report_hook_and_clean_export(self):
        import deckgen
        original = deckgen.attach_reports
        with patch('deckgen.attach_reports', lambda slides, path: original(slides, [], quiet=True)):
            self.assertFalse(any(s.report for s in runpy.run_path(str(ROOT / 'deck/week11.py'))['S']))
        with patch('deckgen.attach_reports', lambda slides, path: original(slides, [{'activity': 'synthetic', 'question': 'Not real'}], quiet=True)):
            with self.assertRaisesRegex(ValueError, '1 activities but 0 ClassPoint'):
                runpy.run_path(str(ROOT / 'deck/week11.py'))
        for path in (ROOT / '_site/week11/index.html', ROOT / 'export/week11.pptx',
                     ROOT / 'export/week11-classpoint.pptx'):
            self.assertTrue(path.exists(), f'build Week 11 exports before running this suite: {path}')
            self.assertGreater(path.stat().st_size, 10000)
        from zipfile import ZipFile
        with ZipFile(ROOT / 'export/week11.pptx') as z:
            slides = [n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')]
            self.assertEqual(len(slides), len(self.slides))
            self.assertIn(b'Whose design?', z.read('ppt/slides/slide1.xml'))


if __name__ == '__main__':
    unittest.main()
