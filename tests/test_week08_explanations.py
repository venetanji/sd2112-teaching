"""Each paper teaches a concrete task and outcome before interpreting its figure."""
import unittest


def text(slide):
    return ' '.join(r.text for e in slide.els if hasattr(e, 'paras')
                    for p in e.paras for r in p.runs)


class Week08ExplanationTests(unittest.TestCase):
    def test_each_study_has_a_task_measurement_then_result(self):
        from deck.week08 import S, REFS, STUDY_GUIDES
        for key, guide in STUDY_GUIDES.items():
            with self.subTest(paper=key):
                task = next(s for s in S if s.title == guide['title'])
                result = S[S.index(task) + 1]
                for phrase in ('WHAT THEY DID', 'WHAT THEY COMPARED', 'WHAT THEY MEASURED'):
                    self.assertIn(phrase, text(task))
                for field in ('task', 'comparison', 'example', 'measured'):
                    self.assertIn(' '.join(guide[field].split()), text(task))
                    self.assertGreater(len(guide[field].split()), 5)
                for field in ('result', 'limit'):
                    self.assertIn(guide[field], text(result))
                self.assertIn('WHAT THEY FOUND', text(result))
                self.assertIn('WHAT IT DOES NOT SHOW', text(result))
                if guide['example_kind'] == 'illustrative':
                    self.assertIn('ILLUSTRATIVE EXAMPLE', text(task))
                self.assertIn(guide['source_locations'], task.notes)
                self.assertTrue(any(r.url == REFS[key][1] for e in task.els if hasattr(e, 'paras')
                                    for p in e.paras for r in p.runs))

    def test_paper_title_and_block_grids_are_consistent(self):
        from deck.week08 import S
        headers = [e for s in S for e in s.els if getattr(e, 'name', '') == 'paper-title']
        self.assertEqual(len(headers), 25)  # nine pairs, two figure details, transfer, four recaps
        for e in headers:
            self.assertEqual((e.x, e.y, e.w, e.h), (120, 184, 1680, 140))
            self.assertEqual(e.paras[0].runs[0].size, 72)
        for s in S:
            blocks = {e.name: e for e in s.els if getattr(e, 'name', '').startswith('study-')}
            for name in ('study-task', 'study-comparison', 'study-example', 'study-measurement',
                         'study-result', 'study-limit', 'study-design'):
                if name + '-body' in blocks:
                    self.assertEqual(blocks[name + '-body'].y - blocks[name + '-label'].y, 52)

    def test_examples_do_not_erase_key_measurement_boundaries(self):
        from deck.week08 import STUDY_GUIDES
        self.assertIn('repeatedly', STUDY_GUIDES['R8']['task'])
        self.assertIn('57-62% of choices', STUDY_GUIDES['R8']['result'])
        self.assertIn('does not prove equal', STUDY_GUIDES['R2']['limit'])
        self.assertIn('GPT-4', STUDY_GUIDES['R3']['measured'])
        self.assertIn('not factual accuracy', STUDY_GUIDES['R3']['limit'])
        self.assertIn('65%', STUDY_GUIDES['R7']['result'])
        self.assertIn('59%', STUDY_GUIDES['R7']['result'])
        self.assertIn('consult', (STUDY_GUIDES['R5']['result'] + STUDY_GUIDES['R5']['limit']).lower())
        self.assertIn('intent', STUDY_GUIDES['R4']['measured'].lower())
        self.assertIn('between', STUDY_GUIDES['R6']['limit'].lower())

    def test_optional_papers_have_examples_and_measurement_boundaries(self):
        from deck.week08 import S, MAIN_SLIDE_COUNT, EXTENSION_GUIDES
        for key, guide in EXTENSION_GUIDES.items():
            slide = next(s for s in S if s.title == guide['title'])
            self.assertGreaterEqual(S.index(slide), MAIN_SLIDE_COUNT)
            for field in ('example', 'task', 'measured', 'result', 'limit'):
                self.assertIn(guide[field], text(slide))
        self.assertIn('qualitative', EXTENSION_GUIDES['R10']['measured'])
        self.assertIn('copyright', EXTENSION_GUIDES['R11']['limit'])
        self.assertIn('no randomized', EXTENSION_GUIDES['R12']['measured'].lower())
        self.assertIn('did not differ significantly', EXTENSION_GUIDES['R13']['result'])

    def test_opening_map_and_concrete_transfer(self):
        from deck.week08 import S
        self.assertIn('Where we are', S[1].title)
        self.assertEqual(S[2].title, 'Today')
        slide = next(s for s in S if s.title == 'From a finding to a product test.')
        visible = text(slide)
        for phrase in ('1 / FINDING', '2 / FEATURE IDEA', '3 / PROPOSED TEST',
                       '65%', '59%', 'R7 did not test it', 'Next week'):
            self.assertIn(phrase, visible)
        self.assertIn('comparator differs', slide.notes)
