"""Week 11: bounded evidence, ethical argument, exact timing and native integrity."""
from copy import deepcopy
from pathlib import Path
import runpy
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def slide_text(slide):
    return ' '.join(r.text for e in slide.els if hasattr(e, 'paras')
                    for p in e.paras for r in p.runs)


class Week11Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week11 import S, SCHEDULE, REFS, DECK
        cls.slides, cls.schedule, cls.refs, cls.deck = S, SCHEDULE, REFS, DECK

    def test_exact_180_minute_route_and_protected_blocks(self):
        self.assertEqual(len(self.slides), 28)
        self.assertEqual([(a,b) for a,b,_,_ in self.schedule],
                         [(0,15),(15,45),(45,75),(75,90),(90,110),(110,140),(140,165),(165,180)])
        self.assertEqual(sum(b-a for a,b,_,_ in self.schedule),180)
        self.assertEqual([i for _,_,_,(a,b) in self.schedule for i in range(a,b+1)],list(range(1,29)))
        self.assertEqual(self.slides[16].title,'Break.\n15 minutes.')
        self.assertIn('30 min', slide_text(self.slides[20]))
        self.assertIn('25 min', slide_text(self.slides[23]))
        self.assertFalse(any(s.cp or s.report for s in self.slides))

    def test_research_is_bounded_and_precedes_product_and_project(self):
        n,d,j = map(slide_text,(self.slides[4],self.slides[6],self.slides[14]))
        for phrase in ('28','artifact-based','U.S.','Self-selected','not randomized','skill loss'):
            self.assertIn(phrase,n)
        for phrase in ('293','600','Eight-sentence','no iterative chat','embedding','long-term'):
            self.assertIn(phrase,d)
        for phrase in ('29 analyzed','30 new','Baseline always first','without a further significant','Legal ownership'):
            self.assertIn(phrase,j)
        self.assertIn('OUR HYPOTHESIS',slide_text(self.slides[7]))
        self.assertIn('not proven',slide_text(self.slides[7]))
        self.assertIn('FICTIONAL',slide_text(self.slides[17]))
        self.assertIn('source',slide_text(self.slides[21]).lower())

    def test_ethics_is_visible_not_only_in_notes(self):
        for index in (2,22,24,26):
            text=slide_text(self.slides[index]).lower()
            self.assertTrue('who' in text or 'affected' in text)
            self.assertTrue('contest' in text or 'disagree' in text)
        text=' '.join(slide_text(s).lower() for s in self.slides)
        for phrase in ('representation','competing values','accountability','permission','rejected alternative'):
            self.assertIn(phrase,text)
        self.assertIn('editorial team',slide_text(self.slides[18]))
        self.assertIn('can pause',slide_text(self.slides[18]))

    def test_assessment_and_jurisdiction_are_preserved(self):
        text=' '.join(slide_text(s) for s in self.slides)
        for phrase in ('A0 poster','3-5 minute video','one-page mediation brief','40%','30 / ethics 30 / poster 20 / video 10 / process 10','not course weights','current Canvas milestones'):
            self.assertIn(phrase,text)
        legal=slide_text(self.slides[15])
        for phrase in ('U.S.','January 2025','case by case','21 October 2026','Not Hong Kong legal advice'):
            self.assertIn(phrase,legal)
        for phrase in ('Nov 30','Nov 28','Week 14','Blackboard','Excalidraw','Thaler','Google Books'):
            self.assertNotIn(phrase,text)

    def test_visible_attributed_links_and_native_curation_reading_order(self):
        links=[r.url for s in self.slides for e in s.els if hasattr(e,'paras')
               for p in e.paras for r in p.runs if r.url]
        self.assertEqual(len(links),7)
        self.assertEqual(set(links),{v[1] for v in self.refs.values()})
        s=slide_text(self.slides[10])
        self.assertLess(s.index('REJECT:'),s.index('B / TRACEABLE'))
        self.assertLess(s.index('SELECT FOR TEST:'),s.index('C / INCOMPLETE'))
        self.assertIn('not a universally best',self.slides[10].notes)

    def test_report_hook_invocation_missing_empty_and_count_drift(self):
        import deckgen
        original=deckgen.attach_reports
        for payload in ([],[{'activity':'synthetic-only','question':'Not a real activity'}]):
            calls=[]
            def injected(slides, source):
                calls.append(Path(source).name)
                return original(slides,payload,quiet=True)
            with patch('deckgen.attach_reports',injected):
                if payload:
                    with self.assertRaisesRegex(ValueError,'1 activities but 0 ClassPoint'):
                        runpy.run_path(str(ROOT/'deck/week11.py'))
                else:
                    loaded=runpy.run_path(str(ROOT/'deck/week11.py'))
                    self.assertFalse(any(s.report for s in loaded['S']))
            self.assertEqual(calls,['week11-reports.json'])
        self.assertEqual(original(deepcopy(self.slides), ROOT/'deck/week11-reports.json'),0)

    def test_own_week_only_build_registration_and_notes_companion(self):
        config=tomllib.loads((ROOT/'deckgen.toml').read_text())
        self.assertIn('week11',config['course']['decks'])
        self.assertFalse(any(n['href']=='week11/' for n in config['nav']))
        self.assertEqual(self.deck['pdf'],'SD2112-week11.pdf')
        notes=(ROOT/'lessons/week11-speaker-notes.md').read_text()
        plan=(ROOT/'lessons/week11-lesson-plan.md').read_text()
        for i,s in enumerate(self.slides,1):
            self.assertGreater(len(s.notes.split()),35)
            self.assertIn(s.notes,notes)
            self.assertIn(s.title.replace('\n',' '),plan)
        self.assertEqual(notes.count('\n## '),28)

    def test_geometry_chrome_and_footer_clearance(self):
        for i,s in enumerate(self.slides,1):
            with self.subTest(slide=i):
                if s.chrome:
                    for name in ('chrome-footer','chrome-num'):
                        self.assertEqual(sum(getattr(e,'name','')==name for e in s.els),1)
                for e in s.els:
                    if all(hasattr(e,k) for k in ('x','y','w','h')):
                        self.assertGreaterEqual(e.x,0);self.assertGreaterEqual(e.y,0)
                        self.assertLessEqual(e.x+e.w,1920);self.assertLessEqual(e.y+e.h,1080)
                        if s.chrome and not getattr(e,'name','').startswith('chrome-'):
                            self.assertLessEqual(e.y+e.h,990)


if __name__=='__main__':
    unittest.main()
