"""Week 12 schedule, evidence boundaries, privacy and native export contracts."""
from pathlib import Path
import importlib.util
import re
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(r.text for el in slide.els if hasattr(el, 'paras')
                    for p in el.paras for r in p.runs)


class Week12Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week12 import S, DECK, TIMING
        cls.slides, cls.deck, cls.timing = S, DECK, TIMING
        cls.plan = (ROOT / 'lessons/week12-lesson-plan.md').read_text()

    def slide(self, title):
        matches = [s for s in self.slides if s.title == title]
        self.assertEqual(len(matches), 1, title)
        return matches[0]

    def load_with_mapping(self, entries):
        from deckgen import attach_reports
        calls = []
        def inject(slides, path):
            calls.append(path)
            return attach_reports(slides, entries, quiet=True)
        spec = importlib.util.spec_from_file_location('week12_test_load', ROOT / 'deck/week12.py')
        module = importlib.util.module_from_spec(spec)
        with patch('deckgen.attach_reports', side_effect=inject):
            spec.loader.exec_module(module)
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0].name, 'week12-reports.json')
        return module

    def test_180_minutes_and_protected_workshop(self):
        self.assertEqual([(a,b) for a,b,*_ in self.timing],
                         [(0,10),(10,40),(40,65),(65,75),(75,90),(90,120),
                          (120,155),(155,175),(175,180)])
        self.assertEqual(sum(b-a for a,b,*_ in self.timing), 180)
        self.assertEqual([i for _,_,first,last,_ in self.timing for i in range(first,last+1)],list(range(1,35)))
        self.assertEqual(len(self.slides),36)
        for i,minutes in [(25,30),(28,35),(32,20)]:
            self.assertIn(f'{minutes} min',text(self.slides[i-1]))
        self.assertEqual(self.slides[23].title,'Break.\nFifteen minutes.')
        self.assertEqual([self.slides[i-1].title for i in (25,28,32)],
                         ['Walk through three low-risk situations.',
                          'Paired review. Then swap roles.', 'Choose the change that matters most.'])

    def test_plan_map_and_speaker_notes_agree(self):
        mapping=self.plan.split('<!-- slide-map:start -->')[1].split('<!-- slide-map:end -->')[0]
        rows=re.findall(r'^\| (\d+) \| (.*?) \| (.*?) \|$',mapping,re.M)
        companion=(ROOT/'lessons/week12-speaker-notes.md').read_text()
        sections=re.split(r'^## \d+ / .*?\n\n',companion,flags=re.M)[1:]
        self.assertEqual(len(rows),36)
        self.assertEqual(len(sections),36)
        for i,(slide,row,note) in enumerate(zip(self.slides,rows,sections),1):
            self.assertEqual(row[:2],(str(i),slide.title.replace('\n',' / ')))
            self.assertEqual(note.strip(),slide.notes.strip())
            self.assertGreater(len(slide.notes.split()),55,slide.title)

    def test_case_system_evidence_procedure_and_design_boundaries(self):
        visible=' '.join(text(s) for s in self.slides[7:15])
        for phrase in ('Autopilot was', 'Autosteer', 'Traffic-Aware Cruise Control',
                       'NTSB', '-5.9 S', '-3.9 S', '71 mph',
                       'no jury finding', 'not a liability verdict', 'NOT TO SCALE'):
            self.assertIn(phrase.lower(),visible.lower())
        self.assertIn('Full Self-Driving (Supervised)',self.slides[7].notes)
        self.assertIn('not a test of an alternative interface',self.slides[10].notes)
        self.assertIn('not retroactive proof',self.slides[14].notes)
        self.assertIn('did not obtain the civil docket',self.slides[13].notes)
        self.assertIn('2024',self.slides[13].notes)
        self.assertNotIn('driver at fault therefore design absolved',visible.lower())
        self.assertIn('not a population rate',visible.lower()+' '+text(self.slides[19]).lower())

    def test_case_visuals_are_editable_and_semantically_ordered(self):
        diagram=self.slides[9]
        self.assertFalse(any(el.kind=='image' for el in diagram.els))
        self.assertIn('schematic',diagram.notes)
        self.assertIn('not to scale',text(diagram).lower())
        top = next(e for e in diagram.els if getattr(e, 'x', None) == 155 and getattr(e, 'y', None) == 405)
        lower = next(e for e in diagram.els if getattr(e, 'x', None) == 155 and getattr(e, 'y', None) == 580)
        self.assertIn('SR-85 exit (left)',' '.join(r.text for p in top.paras for r in p.runs))
        self.assertIn('US-101 continues',' '.join(r.text for p in lower.paras for r in p.runs))
        self.assertIn('ORANGE = GORE',text(diagram))
        self.assertIn('BLACK = DAMAGED ATTENUATOR',text(diagram))
        for slide,labels in [(self.slides[5],['GOAL','EVIDENCE','PERMISSION','RESULT']),
                             (self.slides[10],['-5.9 S','-3.9 S','APPROACH','IMPACT']),
                             (self.slides[12],['DRIVER','TESLA','ROAD','REGULATOR'])]:
            visible=' '.join(r.text for e in slide.els[2:] if hasattr(e,'paras') for p in e.paras for r in p.runs)
            self.assertEqual([visible.index(v) for v in labels], sorted(visible.index(v) for v in labels))
            self.assertEqual(sum(e.kind=='rect' and e.y==355 for e in slide.els),4)

    def test_study_task_figure_limit_and_one_taught_paper(self):
        from deck.week12_studies import GUIDES
        task=self.slide(GUIDES['R1']['title'])
        result=self.slide('An explanation did not fix wrong advice here.')
        self.assertEqual(self.slides.index(task)+1,self.slides.index(result))
        for phrase in ('1,403','16 fictional CVs','75% correct','percentage of trials','1-7','ILLUSTRATION'):
            self.assertIn(phrase,text(task))
        for phrase in ('not proof of equal effects','Two pooled contrasts','70.61% baseline','CC BY 4.0'):
            self.assertIn(phrase,text(result))
        self.assertEqual(len([e for e in result.els if e.kind=='image' and e.name.startswith('paper-excerpt')]),1)
        self.assertEqual(sum(e.kind=='image' and e.name.startswith('paper-excerpt') for s in self.slides for e in s.els),1)
        self.assertIn('SIMULATION',text(self.slides[18]))
        self.assertIn('not a proven safety solution',text(self.slides[20]))
        self.assertTrue((ROOT/'deck/assets/week12/provenance.md').exists())

    def test_only_two_reflections_and_static_nonchatbot_workflow(self):
        activities=[(i,s) for i,s in enumerate(self.slides,1) if s.cp]
        self.assertEqual([i for i,_ in activities],[3,34])
        for i,s in activities:
            self.assertEqual(s.cp['type'],'short_answer')
            self.assertFalse(s.cp['multiple'])
            self.assertFalse(s.cp['hide_names'])
            self.assertIn(s.title,self.plan)
        self.assertFalse(any(s.cp for s in self.slides[24:33]))
        for phrase in ('paper/static','SIMULATION','ordinary, ambiguous','out-of-scope'):
            self.assertIn(phrase,text(self.slides[24]))
        self.assertIn('classifiers, recommenders, physical objects and installations',self.slides[24].notes)
        self.assertIn('without disability simulation',text(self.slides[25]))
        self.assertIn('No new deadline, grade or upload',text(self.slides[31]))
        self.assertIn('A0 poster',text(self.slides[21]))
        self.assertNotIn('final quiz',' '.join(text(s).lower() for s in self.slides[:34]))
        self.assertIn('Week 13 is the confirmed quiz and poster session',self.slides[33].notes)
        self.assertNotIn('reconcile Week 13 policy',self.slides[33].notes)
        self.assertIn('mock-review activity slide',self.slides[30].notes)
        self.assertIn('revision activity',self.slides[32].notes)
        self.assertNotIn('slide 31',self.slides[30].notes)
        self.assertNotIn('slide 35',self.slides[32].notes)

    def test_report_hook_rejects_drift_and_withholds(self):
        questions=[s.title for s in self.slides if s.cp]
        valid=[{'activity':None,'question':q} for q in questions]
        self.assertFalse(any(s.report for s in self.load_with_mapping(valid).S))
        for entries in (valid[:1],valid+[valid[0]],
                        [valid[0],{'activity':None,'question':'changed'}]):
            with self.assertRaises(ValueError): self.load_with_mapping(entries)
        module=self.load_with_mapping([{'activity':'synthetic-not-live','question':questions[0]},valid[1]])
        self.assertTrue([s for s in module.S if s.cp][0].report.endswith('synthetic-not-live'))
        self.assertFalse([s for s in module.S if s.cp][1].report)

    def test_links_and_native_bounds(self):
        from deck.week12 import REFS
        urls={r.url for s in self.slides for e in s.els if hasattr(e,'paras')
              for p in e.paras for r in p.runs if r.url}
        for _,url in REFS.values(): self.assertIn(url,urls)
        for slide in self.slides:
            for el in slide.els:
                if all(hasattr(el,a) for a in ('x','y','w','h')):
                    self.assertGreaterEqual(el.x,0)
                    self.assertGreaterEqual(el.y,0)
                    self.assertLessEqual(el.x+el.w,1921)
                    self.assertLessEqual(el.y+el.h,1081)


if __name__=='__main__': unittest.main()
