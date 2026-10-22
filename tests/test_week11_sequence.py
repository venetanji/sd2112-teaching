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
        from deck.week11 import S, SCHEDULE, REFS, DECK, PAPER_SUMMARIES, MAIN_SLIDE_COUNT
        cls.slides, cls.schedule, cls.refs, cls.deck = S, SCHEDULE, REFS, DECK
        cls.summaries, cls.main_count = PAPER_SUMMARIES, MAIN_SLIDE_COUNT

    def by_title(self, title):
        return next(s for s in self.slides if s.title == title)

    def test_exact_180_minute_route_and_protected_blocks(self):
        self.assertEqual((self.main_count,len(self.slides)),(36,37))
        self.assertEqual([(a,b) for a,b,_,_ in self.schedule],[(0,15),(15,45),(45,75),(75,90),(90,110),(110,140),(140,165),(165,180)])
        self.assertEqual(sum(b-a for a,b,_,_ in self.schedule),180)
        self.assertEqual([i for _,_,_,(a,b) in self.schedule for i in range(a,b+1)],list(range(1,37)))
        self.assertEqual(self.slides[22].title,'Break.\n15 minutes.')
        self.assertIn('30 min',slide_text(self.by_title('Find one claim and one choice.')))
        self.assertIn('25 min',slide_text(self.by_title('Let the argument travel without you.')))
        self.assertFalse(any(s.cp or s.report for s in self.slides))

    def test_each_taught_source_has_task_example_and_basis_before_result(self):
        self.assertEqual(set(self.summaries),set('NDGJUV'))
        for key,g in self.summaries.items():
            for field in ('task','comparison','example','measured'):
                self.assertGreater(len(g[field].split()),10)
            self.assertEqual(g['conceptual'],key in 'GUV')
        n=slide_text(self.by_title('What did designers describe?'))
        for term in ('28 U.S.','10 junior','10 senior','8 professionals','June-August 2024','themes','SOURCE ADAPTATION'):
            self.assertIn(term,n)
        d=slide_text(self.by_title('Write a story. Change the starting help.'))
        for term in ('293','eight-sentence','600','1 (not at all) to 9','0 to 100','SOURCE ADAPTATION'):
            self.assertIn(term,d)
        j=slide_text(self.by_title('Would you type more to avoid friction?'))
        for term in ('29 analyzed','30 new','Baseline first','0-100','ILLUSTRATIVE EXAMPLE'):
            self.assertIn(term,j)
        for task,result in [('What did designers describe?','A participant view is not a legal rule.'),('Write a story. Change the starting help.','Higher ratings can accompany convergence.'),('What must a dataset explain?','Document the choice, including the unknowns.'),('Would you type more to avoid friction?','More input can feel more yours.'),('Which human expression is protected?','Separate protection, permission and credit.')]:
            self.assertLess(self.slides.index(self.by_title(task)),self.slides.index(self.by_title(result)))
        self.assertIn('philosophical',self.summaries['V']['measured'])
        self.assertIn('not a randomized',self.summaries['G']['measured'])
        self.assertIn('not a participant experiment',self.summaries['U']['task'])
        self.assertIn('OUR HYPOTHESIS',slide_text(self.by_title('Control and variety are not the same goal.')))
        self.assertIn('Not proven',slide_text(self.by_title('Control and variety are not the same goal.')))

    def test_ethics_is_visible_not_only_in_notes(self):
        for title in ('A good-looking output is not enough.','Make the curation decision inspectable.','What did you understand - and miss?','What became more defensible?'):
            text=slide_text(self.by_title(title)).lower()
            self.assertTrue('who' in text or 'affected' in text)
            self.assertTrue('contest' in text or 'disagree' in text)
        text=' '.join(slide_text(s).lower() for s in self.slides)
        for phrase in ('representation','competing values','accountability','permission','rejected alternative'):
            self.assertIn(phrase,text)
        brief=slide_text(self.by_title('Name the relation and the responsible actor.'))
        self.assertIn('editorial team',brief);self.assertIn('can pause',brief)

    def test_assessment_and_jurisdiction_are_preserved(self):
        text=' '.join(slide_text(s) for s in self.slides)
        for phrase in ('A0 poster','3-5 minute video','one-page mediation brief','40%','30 / ethics 30 / poster 20 / video 10 / process 10','not course weights','current Canvas milestones','not Hong Kong legal advice'):
            self.assertIn(phrase,text)
        for phrase in ('Nov 30','Nov 28','Week 14','Blackboard','Excalidraw','Thaler','Google Books'):
            self.assertNotIn(phrase,text)
        self.assertIn('Unknown reuse permission',slide_text(self.by_title('Separate protection, permission and credit.')))
        self.assertIn('OFFICE POSITION',slide_text(self.by_title('Separate protection, permission and credit.')))
        self.assertIn('REPORTED THEMES / NOT CAUSAL',slide_text(self.by_title('A participant view is not a legal rule.')))

    def test_visible_attributed_links_and_native_curation_reading_order(self):
        links=[r.url for s in self.slides for e in s.els if hasattr(e,'paras') for p in e.paras for r in p.runs if r.url]
        self.assertTrue({v[1] for v in self.refs.values()}.issubset(set(links)))
        s=slide_text(self.by_title('Three candidates. One stated criterion.'))
        self.assertLess(s.index('REJECT:'),s.index('B / TRACEABLE'))
        self.assertLess(s.index('SELECT FOR TEST:'),s.index('C / INCOMPLETE'))
        self.assertIn('not a universally best',self.by_title('Three candidates. One stated criterion.').notes)

    def test_public_review_assets_and_bibliography(self):
        import hashlib,json
        records=json.loads((ROOT/'deck/assets/week11/provenance.json').read_text())
        self.assertEqual(len(records),5)
        for r in records:
            self.assertEqual(hashlib.sha256((ROOT/'deck/assets/week11'/r['asset']).read_bytes()).hexdigest(),r['sha256'])
            for field in ('primary_url','rights_basis','rights_url','distribution','version','location','changes'):
                self.assertTrue(r[field])
            self.assertIn('public GitHub PR',r['distribution'])
        self.assertEqual(sum(getattr(e,'name','')=='paper-image' for s in self.slides for e in s.els),4)
        self.assertIn('OPTIONAL BIBLIOGRAPHY',slide_text(self.slides[-1]))
        self.assertIn('Density',self.by_title('Similar to what? Read the axis.').notes)

    def test_joshi_mobile_uses_one_authentic_panel_with_omissions_disclosed(self):
        import hashlib, json
        from PIL import Image
        result = self.slides[19]
        self.assertEqual(result.title, 'More input can feel more yours.')
        images = [e for e in result.els if getattr(e, 'name', '') == 'paper-image']
        self.assertEqual(len(images), 1)
        image = images[0]
        self.assertEqual(Path(image.src).name, 'joshi-fig1a-motor.png')
        self.assertEqual((image.x, image.y, image.w, image.h), (120,348,1010,515))
        self.assertEqual(image.url, self.refs['J'][1])
        text = slide_text(result)
        for term in ('Fig. 1(a) crop', 'Motor-cost example', '(b)/(c) omitted', 'Full figure: source link', 'CC BY 4.0'):
            self.assertIn(term, text)
        self.assertIn('Normal submit versus hold-button or pump-slider', slide_text(self.slides[18]))
        for term in ('113 reps', 'not a universal requirement or study result', 'Panels (b)', 'omitted for legibility'):
            self.assertIn(term, result.notes)
        records=json.loads((ROOT/'deck/assets/week11/provenance.json').read_text())
        record=next(r for r in records if r['asset']=='joshi-fig1a-motor.png')
        self.assertEqual(record['crop_pixels'], [172,664,706,1202])
        self.assertEqual(record['render_dpi'], 240)
        self.assertEqual(record['render_dimensions'], [2040,2640])
        self.assertEqual(record['version'], 'arXiv 2507.03670v3')
        self.assertEqual(record['rights_url'], 'https://creativecommons.org/licenses/by/4.0/')
        with Image.open(ROOT/'deck/assets/week11'/record['asset']) as cropped:
            self.assertEqual(cropped.size, (534,538))
        self.assertEqual(hashlib.sha256((ROOT/'deck/assets/week11'/record['asset']).read_bytes()).hexdigest(),record['sha256'])

    def test_common_paper_grid_and_reading_order(self):
        for s in self.slides:
            titles=[e for e in s.els if getattr(e,'name','')=='paper-title']
            if not titles:continue
            e=titles[0]
            self.assertEqual((e.x,e.y,e.w,e.h),(120,184,1680,140))
            self.assertEqual(e.paras[0].runs[0].size,72)
            for label in [e for e in s.els if getattr(e,'name','').endswith('-label')]:
                body=next(e for e in s.els if getattr(e,'name','')==label.name.replace('-label','-body'))
                self.assertEqual(body.y-label.y,52)
            self.assertTrue(any(getattr(e,'y',0)==956 for e in s.els))

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
        self.assertEqual(notes.count('\n## '),37)

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
                            self.assertLessEqual(e.y+e.h,1000)


if __name__=='__main__':
    unittest.main()
