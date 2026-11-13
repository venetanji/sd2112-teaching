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
        self.assertEqual((self.main_count, len(self.slides)), (36, 38))
        self.assertEqual([(start, end) for start, end, _, _ in self.schedule],
                         [(0,10),(10,15),(15,25),(25,40),(40,62),(62,75),
                          (75,90),(90,105),(105,115),(115,145),(145,165),(165,180)])
        self.assertEqual(sum(end-start for start,end,_,_ in self.schedule), 180)
        self.assertEqual([n for _,_,_,(start,end) in self.schedule for n in range(start,end+1)],
                         list(range(1,self.main_count+1)))
        pause = self.slides.index(self.slide('Break.\n15 minutes.'))
        self.assertEqual(self.slides[pause+1].title, 'Group project: ask me anything.')
        self.assertFalse(any(s.report for s in self.slides))

    def test_final_exercise_collects_one_group_text_response(self):
        submission = self.slide('Show the change, not a checklist.')
        self.assertEqual([s for s in self.slides if s.cp],
                         [self.slide('Group project: ask me anything.'), submission])
        self.assertEqual(submission.cp,
                         {'type': 'short_answer', 'hide_names': False, 'multiple': False})
        self.assertIn('One person per group', text(submission))
        self.assertIn('submit', text(submission).lower())
        self.assertLess(self.slides.index(self.slide('Explain it. Hear a question. Improve it.')),
                        self.slides.index(submission))

    def test_ama_collects_questions_immediately_after_break(self):
        pause = self.slides.index(self.slide('Break.\n15 minutes.'))
        ama = self.slides[pause+1]
        self.assertEqual(ama.title, 'Group project: ask me anything.')
        self.assertEqual(ama.cp,
                         {'type': 'short_answer', 'hide_names': False, 'multiple': True})
        self.assertIn('Submit your questions in ClassPoint', text(ama))

    def test_four_topics_have_their_own_sections_and_plain_example(self):
        topics = ['Mediation', 'Curation and power', 'Agency and\nauthorship', 'Responsibility']
        for i, heading in enumerate(topics, 1):
            sl = self.slide(heading)
            self.assertIn(f'TOPIC {i} / 4', text(sl))
            self.assertEqual(sl.bg, '#000B1C')
        indexes = [self.slides.index(self.slide(t)) for t in topics]
        self.assertEqual(indexes, sorted(indexes))
        self.assertLess(indexes[0], self.slides.index(self.slide('Which story does the guide tell?')))
        self.assertLess(indexes[1], self.slides.index(self.slide('Write a story. Change the starting help.')))
        self.assertLess(indexes[2], self.slides.index(self.slide('What did designers describe?')))
        self.assertLess(indexes[3], self.slides.index(self.slide('A complaint is not a verdict.')))
        example = text(self.slide('Which story does the guide tell?'))
        for term in ('fishing boat', 'museum', 'family', 'not invent'):
            self.assertIn(term, example)
        visible = ' '.join(map(text, self.slides))
        for stale in ('institutional account', 'community account', 'explicit gap', 'Team evidence and curation audit'):
            self.assertNotIn(stale, visible)
        self.assertIn('metal detector', self.slide('The tool frames what we notice.').notes)

    def test_diagrams_show_relationships_not_repeated_row_tables(self):
        expected = {
            'The tool frames what we notice.': ('mediation-', 3, 2),
            'Choosing one story leaves another out.': ('curation-', 3, 2),
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
                             ('Write a story. Change the starting help.', 'Better ratings. More similar stories.'),
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
        case = [self.slide(t) for t in ('A complaint is not a verdict.', 'Four questions, not one ruling.', 'Settlement is not universal clearance.')]
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

    def test_one_topic_activity_and_unchanged_project_contract(self):
        intro = text(self.slide('Choose one topic. Improve one thing.'))
        for phrase in ('Choose ONE', 'ONE part', 'one problem', 'one change'):
            self.assertIn(phrase, intro)
        prompts = text(self.slide('Use one question to guide your change.'))
        for phrase in ('MEDIATION', 'CURATION AND POWER', 'AGENCY AND AUTHORSHIP', 'RESPONSIBILITY'):
            self.assertIn(phrase, prompts)
        for heading in ('Find one claim and one choice.', 'Narrow the claim until it fits.',
                        'Make the curation decision inspectable.', 'Let the argument travel without you.'):
            self.assertFalse(any(s.title == heading for s in self.slides))
        self.assertIn('60-second', text(self.slide('Make your change.')))
        self.assertIn('30 min', text(self.slide('Make your change.')))
        ending = text(self.slide('Keep the change. Keep the question.'))
        for phrase in ('A0 poster', '3-5 minute video', 'one-page mediation brief', '40%',
                       'current Canvas milestones', 'Week 12', 'Week 13: quiz + posters'):
            self.assertIn(phrase, ending)
        self.assertIn('not an extra deliverable', self.slide('Keep the change. Keep the question.').notes)
        all_text = ' '.join(map(text, self.slides))
        for term in ('Nov 30', 'Week 14', 'Blackboard', 'Excalidraw'):
            self.assertNotIn(term, all_text)

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
            for label in [e for e in s.els if getattr(e, 'name', '').startswith('study-') and getattr(e, 'name', '').endswith('-label')]:
                body = next(e for e in s.els if getattr(e, 'name', '') == label.name.replace('-label', '-body'))
                self.assertEqual(body.y - label.y, 42 if any(getattr(e, 'name', '') == 'finding-panel' for e in s.els) and label.x == 1190 else 52)
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

    def test_findings_have_distinct_native_highlight_panels(self):
        results = ['A participant view is not a legal rule.', 'Better ratings. More similar stories.',
                   'Document the choice, including the unknowns.', 'More input can feel more yours.',
                   'Separate protection, permission and credit.']
        for heading in results:
            els = {getattr(e, 'name', ''): e for e in self.slide(heading).els}
            self.assertIn('finding-panel', els)
            self.assertIn('finding-accent', els)
            self.assertGreaterEqual(els['finding-text'].paras[0].runs[0].size, 34)
        self.assertIn('WHAT DESIGNERS REPORTED', text(self.slide(results[0])))
        self.assertIn('THE PROPOSAL', text(self.slide(results[2])))
        self.assertIn('THE OFFICE POSITION', text(self.slide(results[4])))

    def test_news_then_deep_question_before_theory(self):
        question = self.slides.index(self.slide('If AI makes the work,\nwhat makes it yours?'))
        self.assertEqual(question, 3)
        self.assertTrue(all('NEWS' in text(s) for s in self.slides[1:3]))
        self.assertEqual(self.slides[question+1].title, 'Mediation')
        self.assertTrue(all(any(r.url for e in s.els if hasattr(e, 'paras') for p in e.paras for r in p.runs)
                            for s in self.slides[1:3]))

    def test_news_keeps_dates_values_and_resignation_boundary(self):
        market = text(self.slide('AI markets are unsettled.'))
        for value in ('12 NOVEMBER 2026', '-4.3%', '-0.39%', '+5.9%', '+5.5%'):
            self.assertIn(value, market)
        leadership = text(self.slide('Jensen Huang steps down.'))
        for phrase in ('resigned', 'Colette Kress', 'interim CEO', 'not retirement', 'not confirmed'):
            self.assertIn(phrase, leadership)
        self.assertIn('https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition',
                      self.slide('Jensen Huang steps down.').notes)

    def test_ci_builds_before_export_dependent_tests(self):
        workflow = (ROOT / '.github/workflows/news-preview.yml').read_text()
        self.assertLess(workflow.index("subprocess.run(['deckgen', 'build', *decks]"),
                        workflow.index('python -m unittest discover -s tests -v'))

    def test_report_hook_rejects_drift(self):
        import deckgen
        original = deckgen.attach_reports
        with patch('deckgen.attach_reports', lambda slides, path: original(slides, [], quiet=True)):
            self.assertFalse(any(s.report for s in runpy.run_path(str(ROOT / 'deck/week11.py'))['S']))
        with patch('deckgen.attach_reports', lambda slides, path: original(slides, [{'activity': 'synthetic', 'question': 'Not real'}] * 3, quiet=True)):
            with self.assertRaisesRegex(ValueError, '3 activities but 2 ClassPoint'):
                runpy.run_path(str(ROOT / 'deck/week11.py'))
    def test_built_exports_match_deck(self):
        paths = (ROOT / '_site/week11/index.html', ROOT / 'export/week11.pptx',
                 ROOT / 'export/week11-classpoint.pptx')
        if not any(path.exists() for path in paths):
            self.skipTest('Week 11 exports are not part of this selected-week build')
        for path in paths:
            self.assertTrue(path.exists(), f'build Week 11 exports before running this suite: {path}')
            self.assertGreater(path.stat().st_size, 10000)
        from zipfile import ZipFile
        with ZipFile(ROOT / 'export/week11.pptx') as z:
            slides = [n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')]
            self.assertEqual(len(slides), len(self.slides))
            self.assertIn(b'Whose design?', z.read('ppt/slides/slide1.xml'))


if __name__ == '__main__':
    unittest.main()
