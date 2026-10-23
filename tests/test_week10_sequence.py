"""Week 10's timing, evidence boundaries, report hook and native geometry."""
import ast
from copy import deepcopy
from pathlib import Path
import runpy
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(r.text for e in slide.els if hasattr(e, 'paras')
                    for p in e.paras for r in p.runs)


class Week10Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week10 import S, DECK, BLOCKS
        cls.slides, cls.deck, cls.blocks = S, DECK, BLOCKS

    def test_actual_sequence_and_complete_budget(self):
        self.assertEqual(len(self.slides), 26)
        self.assertEqual([(b[0], b[1]) for b in self.blocks],
                         [(0,15),(15,30),(30,55),(55,75),(75,90),
                          (90,115),(115,145),(145,165),(165,180)])
        self.assertEqual([b[1]-b[0] for b in self.blocks],
                         [15,15,25,20,15,25,30,20,15])
        self.assertEqual(sum(b[1]-b[0] for b in self.blocks), 180)
        self.assertEqual([(b[3], b[4]) for b in self.blocks],
                         [(1,1),(2,7),(8,11),(12,14),(15,15),
                          (16,18),(19,21),(22,23),(24,25)])
        self.assertEqual([s.title for s in self.slides[7:11]],
                         ['Reopen the problem, not just the file.', 'Read the passage again.',
                          'Change the question.', 'Keep the disagreement.'])
        self.assertIn('15 minutes', text(self.slides[14]))
        self.assertEqual([s.title for s in self.slides if 'min' in text(s) and s.bg == '#F6AD00'],
                         [self.slides[i].title for i in (7,11,15,18,21,23)])

    def test_provisional_school_reserve_and_assessment_contract(self):
        hold = text(self.slides[0])
        for term in ('if confirmed', 'provisionally', 'not yet confirmed', 'revision and feedback'):
            self.assertIn(term, hold)
        self.assertIn('Giovanni is confirmed absent', self.slides[0].notes)
        all_text = ' '.join(text(s) for s in self.slides)
        for phrase in ('Prototype v1', 'No new graded submission or deadline', 'Canvas instructions'):
            self.assertIn(phrase, all_text)
        self.assertNotIn('November 6', all_text)
        self.assertNotIn('Ball Cheung', all_text)
        self.assertFalse(any(s.cp or s.report for s in self.slides))

    def test_simulation_ethics_and_observable_outcomes_are_visible(self):
        all_text = ' '.join(text(s) for s in self.slides)
        for term in ('SIMULATED AI', 'No device, login, purchase or model call',
                     'voluntary participation', 'right to stop', 'Declining is fine',
                     'No recording, names, sensitive stories', 'Observation is not interpretation',
                     'Actual model reliability', 'not a validated threshold',
                     'No clinical, legal or high-stakes validation'):
            self.assertIn(term, all_text)
        notes = ' '.join(s.notes for s in self.slides)
        self.assertIn('satisfaction alone', notes.lower())
        self.assertIn('internal walkthrough', notes)
        self.assertIn('not automatically an intended user', notes)

    def test_primary_sources_and_visible_native_links(self):
        urls = [r.url for s in self.slides for e in s.els if hasattr(e, 'paras')
                for p in e.paras for r in p.runs if r.url]
        for url in ('https://doi.org/10.1017/S0890060426100304',
                    'https://www.designcouncil.org.uk/resources/the-double-diamond/',
                    'https://creativecommons.org/licenses/by/4.0/'):
            self.assertIn(url, urls)
        self.assertIn('2024', text(self.slides[5]))
        self.assertIn('not an AI/no-AI causal trial', text(self.slides[5]))
        self.assertIn('no formal inter-rater reliability', self.slides[5].notes)
        self.assertIn('Official diagram, unchanged', text(self.slides[4]))
        self.assertIn('CC BY 4.0', text(self.slides[4]))

    def test_study_task_recording_result_and_provenance(self):
        setup = text(self.slides[5])
        for term in ('WHAT THEY DID', 'WHAT THEY COMPARED', 'WHAT THEY RECORDED',
                     'ADAPTED FROM THE STUDY', '88 AI-user survey responses',
                     '10 selected professionals', 'lunchbox', '2024', '2026 PUBLICATION'):
            self.assertIn(term, setup)
        self.assertNotIn('WHAT THEY FOUND', setup)
        result = self.slides[6]
        for term in ('WHAT THEY FOUND', 'WHAT IT DOES NOT SHOW', 'neither time shares',
                     'nor participant counts', 'Top-panel crop; no redraw', 'CC BY 4.0'):
            self.assertIn(term, text(result))
        images = [e for e in result.els if e.kind == 'image' and e.name == 'paper-figure']
        self.assertEqual(len(images), 1)
        self.assertEqual(Path(images[0].src).name, 'sozen-borekci-2026-fig5-overview.png')
        self.assertEqual(images[0].fit, 'contain')
        lens = text(self.slides[17])
        for term in ('CONCEPTUAL LENS', 'NOT A PARTICIPANT STUDY', 'OUR EXAMPLE / NOT FROM',
                     'TRY IN YOUR PROTOTYPE', 'design hypotheses, not proven safeguards'):
            self.assertIn(term, lens)
        ledger = (ROOT / 'lessons/week10-references.md').read_text()
        self.assertEqual(ledger.count('## V1 /'), 1)
        for term in ('public GitHub', 'Cloudflare', 'CC BY 4.0', 'not a restricted/local-only'):
            self.assertIn(term, ledger)

    def test_repeated_paper_geometry_matches_week08(self):
        for slide in (self.slides[i] for i in (5,6,17)):
            heading = next(e for e in slide.els if e.name == 'paper-title')
            self.assertEqual((heading.x, heading.y, heading.w, heading.h), (120,184,1680,140))
            self.assertEqual(heading.paras[0].runs[0].size, 72)
            citation = next(e for e in slide.els if e.name == 'paper-citation')
            self.assertEqual(citation.y, 956)
            for label in (e for e in slide.els if e.name.endswith('-label')):
                body = next(e for e in slide.els if e.name == label.name[:-6]+'-body')
                self.assertEqual(body.y-label.y, 52)

    def test_report_hook_invocation_is_real_and_zero_collection_is_explicit(self):
        import deckgen
        with patch('deckgen.attach_reports', wraps=deckgen.attach_reports) as hook:
            runpy.run_path(str(ROOT / 'deck/week10.py'))
        hook.assert_called_once()
        slides, path = hook.call_args.args
        self.assertEqual(Path(path).name, 'week10-reports.json')
        self.assertEqual(deckgen.attach_reports(deepcopy(slides), [], quiet=True), 0)
        with self.assertRaises(ValueError):
            deckgen.attach_reports(deepcopy(slides),
                                   [{'activity': None, 'question': 'synthetic unrun'}], quiet=True)

    def test_build_registration_does_not_change_navigation(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week10', config['course']['decks'])
        self.assertFalse(any(n['href'] == 'week10/' for n in config['nav']))
        self.assertEqual(self.deck['pdf'], 'SD2112-week10.pdf')
        source = (ROOT / 'deck/week10.py').read_text()
        ast.parse(source)
        self.assertIn('attach_reports(S,', source)

    def test_every_slide_has_notes_and_content_stays_above_footer(self):
        for i, s in enumerate(self.slides, 1):
            with self.subTest(slide=i):
                self.assertGreater(len(s.notes), 150)
                for e in s.els:
                    if not all(hasattr(e, k) for k in ('x','y','w','h')):
                        continue
                    self.assertGreaterEqual(e.x, 0)
                    self.assertGreaterEqual(e.y, 0)
                    self.assertLessEqual(e.x+e.w, 1920)
                    self.assertLessEqual(e.y+e.h, 1080)
                    if s.chrome and not getattr(e, 'name', '').startswith('chrome-'):
                        self.assertLessEqual(e.y+e.h, 1000)

    def test_plan_map_and_notes_match_final_slide_sources(self):
        plan = (ROOT / 'lessons/week10-lesson-plan.md').read_text()
        notes = (ROOT / 'lessons/week10-speaker-notes.md').read_text()
        for i, s in enumerate(self.slides, 1):
            title = s.title.replace('\n', ' ')
            self.assertIn(f'| {i} | {title} |', plan)
            self.assertIn(f'## {i:02d} / {title}', notes)
            self.assertIn(s.notes, notes)


if __name__ == '__main__':
    unittest.main()
