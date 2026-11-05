"""Keep the isolated variant faithful to the supplied project evidence."""
from pathlib import Path
import subprocess
import unittest
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_REVISION = '2330036350ed76a8433e8a6ac9b9fcb267412ccf'


def text(slide):
    parts = [r.text for e in slide.els if hasattr(e, 'paras')
             for p in e.paras for r in p.runs]
    parts += [ET.fromstring(e.svg).get('aria-label', '') for e in slide.els
              if e.name == 'phase-subtitle']
    return ' '.join(parts)


class NicoloVariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from deck.week10_nicolo import S, CASE_START, CASE_SPEAKING_MINUTES, CASE_QA_MINUTES
        cls.full_slides = S
        # Content-only view keeps speaking allocations separate from section covers.
        cls.slides = [s for s in S[1:-1] if s.title != 'Proposed AI Redesign']
        cls.start = CASE_START-1
        cls.minutes = CASE_SPEAKING_MINUTES
        cls.qa = CASE_QA_MINUTES

    def slide(self, title):
        return next(s for s in self.slides if s.title == title)

    def test_separate_original_sources_are_byte_unchanged(self):
        for name in ('deck/week10.py', 'deck/week10_figures.py',
                     'lessons/week10-lesson-plan.md', 'lessons/week10-speaker-notes.md',
                     'lessons/week10-speaker-brief.md'):
            self.assertEqual((ROOT/name).read_bytes(), subprocess.check_output(
                ['git', 'show', ORIGINAL_REVISION+':'+name], cwd=ROOT), name)

    def test_requested_opening_cover_and_simple_closing(self):
        from deck.week10_nicolo import CASE_START
        self.assertEqual(len(self.full_slides), 18)
        self.assertEqual(CASE_START, 9)
        cover, closing = self.full_slides[0], self.full_slides[-1]
        self.assertEqual(cover.title, 'Double Diamond \U0001f48e\U0001f48e')
        self.assertIn('Double Diamond', text(cover))
        diamonds = next(e for e in cover.els if e.name == 'dd-cover-diamonds')
        self.assertIn('\U0001f48e\U0001f48e', diamonds.svg)
        self.assertEqual(closing.title, 'thanks!')
        self.assertEqual(len(closing.els), 1)
        thanks = closing.els[0]
        self.assertEqual(text(closing), 'thanks!')
        self.assertEqual(thanks.paras[0].align, 'c')
        self.assertEqual(thanks.valign, 'm')
        self.assertEqual((thanks.x+thanks.w/2, thanks.y+thanks.h/2), (960, 540))
        self.assertEqual(thanks.paras[0].runs[0].size, 48)

    def test_structure_and_case_budget(self):
        self.assertEqual(self.start, 8)
        self.assertEqual(len(self.slides), 15)
        self.assertEqual(len(self.minutes), len(self.slides)-self.start)
        self.assertEqual(sum(self.minutes)+self.qa, 10)
        self.assertEqual(self.qa, 2)
        for phase, slide in zip(('DISCOVER', 'DEFINE', 'DEVELOP', 'DELIVER'), self.slides[1:5]):
            self.assertIn(phase.lower(), text(slide).lower())

    def test_revised_discover_and_deliver(self):
        discover = text(self.slides[1])
        for value in ('How do users value privacy?', 'What data are they willing to share?', 'What data can be fed to AI?'):
            self.assertIn(value, discover)
        self.assertIn('Willingness is not permission', self.slides[1].notes)
        deliver = text(self.slides[4])
        for value in ('wishes', 'priorities', 'why', 'how'):
            self.assertIn(value, deliver.lower())
        self.assertIn('cannot establish human usability', self.slides[4].notes)

    def test_case_has_four_source_mapped_phases_and_no_fabricated_research(self):
        from deck.week10_nicolo_case import PAPER_STEPS, POSITIVE_QUOTES, WISH_QUOTES
        case = self.slides[self.start:self.start+4]
        self.assertEqual([s.title.split(' / ')[0] for s in case],
                         ['Discover', 'Define', 'Develop', 'Deliver'])
        for slide in self.slides[self.start:self.start+4]:
            self.assertFalse(slide.cp or slide.report)
            self.assertFalse(any(e.name == 'pending-asset' for e in slide.els))
        for slide, files in zip(case, [('3.pdf', '5.pdf'), ('7.pdf',),
                                       ('8.pdf', '9.pdf'), ('16.pdf', '17.pdf')]):
            for name in files:
                self.assertIn(name, slide.notes)
            self.assertIn('PDF page 1', slide.notes)
        for step in PAPER_STEPS:
            self.assertIn(step, text(case[0]))
        self.assertEqual(sum(e.name == 'paper-workflow-return' for e in case[0].els), 1)
        for value in ('Inexperienced Lab Analyst', 'Cumbersome workflows', 'Transcription errors'):
            self.assertIn(value, text(case[0]))
        for value in ('Streamline interactions', 'Fit into current workflows',
                      'Provide a clear information system on tracked samples',
                      'Task Completion Rate', 'Ease of use / Time on Task'):
            self.assertIn(value, text(case[1]))
        for value in ('Barcode scanner as primary input', 'First Draft',
                      'No validation on the source container'):
            self.assertIn(value, text(case[2]))
        self.assertIn('nullifying the gain in efficiency', case[2].notes)
        self.assertEqual(sum(e.name == 'portfolio-predefined-list-draft' for e in case[2].els), 1)
        for quote in POSITIVE_QUOTES:
            self.assertIn(quote, text(case[3]))
        for quote in POSITIVE_QUOTES+WISH_QUOTES:
            self.assertIn(quote, case[3].notes)
        for value in ('30%', 'faster than', 'manual workflows', '1 Click',
                      'to prepare and submit', 'a sample list', 'Improvement wishes'):
            self.assertIn(value, text(case[3]))
        self.assertIn('not results of the AI redesign', case[3].notes)
        self.assertIn('Do not conflate 30% faster with 30% less completion time', case[3].notes)
        self.assertIn('calculation method are not supplied', case[3].notes)
        quotes = next(e for e in case[3].els if e.name == 'participant-positive-quotes')
        self.assertTrue(all(r.italic for p in quotes.paras for r in p.runs))

    def test_retained_product_media_bytes_are_unchanged(self):
        for name in ('deck/assets/week10/nicolo-current-product.png',
                     'deck/assets/week10/nicolo-product-video-poster.png',
                     'site/week10-nicolo-media/product-video-poster.png',
                     'site/week10-nicolo-media/product-demo.mp4'):
            actual = subprocess.check_output(['git', 'hash-object', name], cwd=ROOT).strip()
            reviewed = subprocess.check_output(['git', 'rev-parse', '2fdb10f:'+name], cwd=ROOT).strip()
            self.assertEqual(actual, reviewed, name)

    def test_original_screen_and_complete_video_share_deliver(self):
        from deck.week10_nicolo import SCREEN_RATIO
        from deck.week10_nicolo_case import SCREEN_CAPTION
        video = self.slides[11]
        screenshots = [e for s in self.slides for e in s.els
                       if e.name == 'current-product-screenshot']
        self.assertEqual(len(screenshots), 1)
        self.assertIn(screenshots[0], video.els)
        self.assertLessEqual(abs(screenshots[0].h-screenshots[0].w/SCREEN_RATIO), .5)
        self.assertEqual(screenshots[0].fit, 'contain')
        self.assertIn(SCREEN_CAPTION, text(video))
        self.assertEqual(len(video.html_only), 1)
        player = video.html_only[0]
        self.assertEqual((player.cw, player.ch), (1920, 1080))
        self.assertAlmostEqual(player.w/player.h, 16/9)
        self.assertIn('49.365-second video', video.notes)
        self.assertIn('video.controls = true', player.code)
        self.assertIn('video.autoplay = false', player.code)
        self.assertNotIn('video.autoplay = true', player.code)
        self.assertIn('video.muted = true', player.code)
        self.assertIn("parent.Reveal.on('slidechanged'", player.code)
        self.assertEqual(self.minutes[3], 2)
        self.assertGreater(self.minutes[3]*60, 49.365)

    def test_three_ordered_ai_concepts_are_proposals_not_validated_results(self):
        from hashlib import sha256
        from deck.week10_nicolo_case import ASSETS
        for i, slide in enumerate(self.slides[12:], 1):
            self.assertTrue(slide.title.startswith('AST / '))
            self.assertIn('PROPOSED AI REDESIGN / AST', text(slide))
            self.assertNotRegex(text(slide), r'ASL-[123]')
            self.assertIn('PROPOSED AI REDESIGN', text(slide))
            image = next(e for e in slide.els if e.name == f'asl-{i}-concept')
            self.assertEqual(Path(image.src), ASSETS/f'nicolo-asl-{i}.png')
            self.assertEqual(image.fit, 'contain')
            import json
            manifest = json.loads((ASSETS/'nicolo-portfolio-sources.json').read_text())
            self.assertEqual(sha256(Path(image.src).read_bytes()).hexdigest(),
                             manifest['aiConceptImages'][i-1]['sha256'])
            self.assertIn('not a working system', slide.notes)
            self.assertIn('not scientific conclusions', slide.notes)
            self.assertIn('does not verify successful transfer', slide.notes)
            self.assertNotIn('30%', text(slide))
        self.assertIn('Mirror-like UI with overlays', text(self.slides[12]))
        self.assertIn('recognised barcode and container type', text(self.slides[13]))
        for value in ('registers the transfer', 'voice recognition', 'Vision Language Model', 'function calling'):
            self.assertIn(value, text(self.slides[14]))
        self.assertIn('not an AI redesign', self.slides[8].notes)

    def test_case_phase_headers_reclaim_subtitle_space(self):
        for slide in self.slides[8:12]:
            self.assertNotIn('phase-subtitle', [e.name for e in slide.els])
            maps = [e for e in slide.els if e.name == 'phase-navigation']
            self.assertEqual(len(maps), 1)
            self.assertLessEqual(maps[0].y+maps[0].h, 350)
            content = [e for e in slide.els if e.name in
                       ('portfolio-lab-photo', 'portfolio-predefined-list-draft', 'current-product-screenshot')]
            self.assertTrue(all(e.y >= 350 for e in content))
        discover = self.slides[8]
        by_name = {e.name: e for e in discover.els}
        intro, labels = by_name['transfer-problem-context'], by_name['transfer-problem-labels']
        self.assertLessEqual(labels.y-(intro.y+intro.h), 10)
        photo = by_name['portfolio-lab-photo']
        self.assertLess(photo.w, 500)
        workflow_top = by_name['paper-workflow-heading'].y
        workflow_bottom = by_name['paper-workflow-return'].y+by_name['paper-workflow-return'].h
        self.assertLess(abs((workflow_top+workflow_bottom)/2-((photo.y+photo.h)+1000)/2), 14)
        develop = {e.name: e for e in self.slides[10].els}
        for name in ('draft-constraints-caption', 'draft-constraints-body'):
            self.assertLess(develop[name].x, 1000)
        image, principle = develop['portfolio-predefined-list-draft'], develop['ideal-ux-principle']
        self.assertEqual((image.x, image.w), (principle.x, principle.w))
        self.assertGreaterEqual(principle.y, image.y+image.h)
        deliver = self.slides[11]
        self.assertNotIn('Ease of use / Learnability', text(deliver))
        self.assertNotIn('Original video /', text(deliver))
        labels = [e for e in deliver.els if hasattr(e, 'paras') and
                  ''.join(r.text for p in e.paras for r in p.runs) in
                  ('Quantitative findings', 'Qualitative findings', 'Improvement wishes')]
        self.assertEqual(len(labels), 3)
        self.assertEqual(len({e.y for e in labels}), 1)
        self.assertEqual(deliver.html_only[0].hint, '')

    def test_ast_maps_highlight_the_whole_solution_space(self):
        from PIL import Image
        from deck.week10_nicolo_figures import phase_map
        expected = ['#FFFFFF', '#FFFFFF', '#246E70', '#246E70']
        for slide in self.full_slides[14:17]:
            maps = [e for e in slide.els if e.name == 'phase-navigation']
            self.assertEqual(len(maps), 1)
            nav = maps[0]
            self.assertEqual((nav.x, nav.y, nav.w, nav.h), (1620, 184, 180, 88))
            svg = ET.fromstring(nav.svg)
            ns = {'svg': 'http://www.w3.org/2000/svg'}
            self.assertEqual([p.get('fill') for p in svg.findall('svg:polygon', ns)], expected)
            self.assertIn('Develop and Deliver', nav.svg)
            self.assertIn('CC BY 4.0', slide.notes)
            heading = next(e for e in slide.els if e.name == 'variant-heading')
            self.assertLessEqual(heading.x+heading.w, nav.x)
            with Image.open(nav.png) as im:
                rgb = im.convert('RGB')
                for x, color in zip((68, 124, 236, 292), ((255, 255, 255),)*2+((36, 110, 112),)*2):
                    self.assertEqual(rgb.getpixel((round(x*rgb.width/360), round(88*rgb.height/176))), color)
        for phase in ('discover', 'define', 'develop', 'deliver'):
            svg, _ = phase_map(phase)
            self.assertEqual(svg.count('fill="#246E70"'), 1)
        neutral, _ = phase_map()
        self.assertNotIn('fill="#246E70"', neutral)

    def test_deliver_caption_compact_metrics_and_quote_spacing(self):
        from deck.week10_nicolo_case import SCREEN_CAPTION
        self.assertEqual(SCREEN_CAPTION, 'Workbench Tablet Device')
        slide = self.slides[11]
        self.assertNotIn('Time on Task', text(slide))
        self.assertNotIn('Original Software Product', text(slide))
        speed = next(e for e in slide.els if e.name == 'reported-speed')
        clicks = next(e for e in slide.els if e.name == 'reported-clicks')
        self.assertEqual(speed.paras[0].runs[0].size, 44)
        self.assertEqual(clicks.paras[0].runs[0].size, 36)
        self.assertLessEqual(clicks.y+clicks.h, 972)
        quotes = next(e for e in slide.els if e.name == 'participant-positive-quotes')
        self.assertEqual(quotes.h, 138)
        self.assertEqual([p.before for p in quotes.paras], [0, 10, 10])
        self.assertTrue(all(p.lh == 1.08 for p in quotes.paras))
        from PIL import Image
        for i in range(1, 4):
            image = next(e for e in self.slides[11+i].els if e.name == f'asl-{i}-concept')
            with Image.open(image.src) as original:
                self.assertEqual(original.size, (2420, 1525))
                self.assertEqual(original.format, 'PNG')
            self.assertLessEqual(abs(image.h-image.w*1525/2420), .5)

    def test_video_loops_with_scoped_space_and_cleanup(self):
        code = self.slides[11].html_only[0].code
        for value in ('video.loop = true', "event.code !== 'Space'", 'event.repeat',
                      'event.stopImmediatePropagation()',
                      "parent.window.addEventListener('keydown', onKey, true)",
                      "parent.window.removeEventListener('keydown', onKey, true)",
                      "chip.style.display = 'none'"):
            self.assertIn(value, code)

    def test_deliver_precise_spacing_and_redesign_cover_order(self):
        slide = self.full_slides[12]
        self.assertTrue(slide.title.startswith('Deliver'))
        image = next(e for e in slide.els if e.name == 'current-product-screenshot')
        video = slide.html_only[0]
        self.assertEqual(video.x-(image.x+image.w), 32)
        self.assertEqual((video.y, video.w, video.h), (350, 720, 405))
        self.assertEqual((image.y, image.h), (video.y, video.h))
        self.assertLessEqual(abs(image.w-image.h*2420/1525), .5)
        self.assertEqual(image.fit, 'contain')
        caption = next(e for e in slide.els if e.name == 'current-product-caption')
        self.assertEqual(caption.x-(video.x+video.w), 32)
        self.assertEqual(caption.x+caption.w, 1800)
        self.assertEqual(caption.y+caption.h/2, video.y+video.h/2)
        self.assertEqual(caption.valign, 'm')
        labels = [e for e in slide.els if hasattr(e, 'paras') and
                  ''.join(r.text for p in e.paras for r in p.runs) in
                  ('Quantitative findings', 'Qualitative findings', 'Improvement wishes')]
        self.assertEqual([e.y for e in labels], [800, 800, 800])
        self.assertEqual(next(e for e in slide.els if e.name == 'reported-speed').y, 842)
        self.assertEqual(next(e for e in slide.els if e.name == 'reported-clicks').y, 910)
        self.assertEqual(next(e for e in slide.els if e.name == 'participant-positive-quotes').y, 844)
        self.assertEqual(next(e for e in slide.els if e.name == 'participant-improvement-wishes').y, 844)
        cover = self.full_slides[13]
        self.assertEqual(cover.title, 'Proposed AI Redesign')
        self.assertEqual(cover.bg, '#000B1C')
        self.assertIn('Proposed AI Redesign', text(cover))
        self.assertEqual([s.title for s in self.full_slides[14:17]], [
            'AST / Mirror-like UI with overlays',
            'AST / Automatic sample selection',
            'AST / Registering the transfer'])
        self.assertEqual(self.full_slides[17].title, 'thanks!')

    def test_transfer_comment_and_bold_ai_challenges_are_vertically_balanced(self):
        from deck.week10_nicolo_case import AI_CHALLENGES
        slide = self.full_slides[16]
        detail = next(e for e in slide.els if e.name == 'concept-detail')
        challenge = next(e for e in slide.els if e.name == 'ai-challenges')
        value = ' '.join(r.text for p in challenge.paras for r in p.runs)
        self.assertEqual(value, AI_CHALLENGES)
        self.assertEqual(AI_CHALLENGES, 'AI Challenges: "Control + Interactivity"')
        self.assertTrue(all(r.font == 'xbold' for p in challenge.paras for r in p.runs))
        self.assertIn(AI_CHALLENGES, slide.notes)
        self.assertEqual((detail.x, detail.w), (challenge.x, challenge.w))
        self.assertEqual(challenge.y-(detail.y+detail.h), 20)
        self.assertEqual((detail.y+challenge.y+challenge.h)/2, (512+696)/2)
        self.assertEqual(challenge.y+challenge.h, 696-32)
        for other in self.full_slides[14:16]:
            self.assertNotIn('ai-challenges', [e.name for e in other.els])

    def test_section_footers_and_case_cover(self):
        from deck.week10_nicolo_case import CASE_TITLE
        for i, slide in enumerate(self.slides):
            footer = next(e for e in slide.els if e.name == 'chrome-footer')
            value = ''.join(r.text for p in footer.paras for r in p.runs)
            self.assertEqual(value, 'Double Diamond' if i < 7 else CASE_TITLE)
            self.assertNotIn('NICOLO VARIANT', text(slide))
        cover = next(e for e in self.slides[7].els if e.name == 'case-cover-title')
        self.assertEqual(''.join(r.text for p in cover.paras for r in p.runs), CASE_TITLE)

    def test_document_voice_and_case_separator(self):
        self.assertEqual([s.title for s in self.slides[:7]], [
            'Double Diamond', 'Discover', 'Define', 'Develop', 'Deliver',
            'An iterative and imperfect process', 'Stakeholder management'])
        for phrase in ('Spend enough time understanding your users',
                       'You cannot expect the user to be exactly like you',
                       'Do not assume the problem'):
            self.assertIn(phrase, text(self.slides[1]))
        self.assertIn('design does not happen in a vacuum', text(self.slides[6]).lower())
        self.assertEqual(self.slides[7].title, 'UX Design for Analytical Laboratory Software')
        self.assertIn('CASE STUDY', text(self.slides[7]))
        self.assertIn('within', self.slides[7].notes)

    def test_opening_definition_explanation_and_diagram_labels(self):
        from deck.week10_nicolo import DD_DEFINITION
        expected = ('The\u00a0Double Diamond\u00a0is a visual representation of the design and innovation process. '
                    'It\u2019s a simple way to describe the steps taken in any design\u00a0and innovation\u00a0project, '
                    'irrespective of methods and tools used.')
        self.assertEqual(DD_DEFINITION, expected)
        slide = self.slides[0]
        definition = next(e for e in slide.els if e.name == 'dd-definition')
        self.assertEqual(''.join(r.text for p in definition.paras for r in p.runs),
                         '\u201c'+expected+'\u201d')
        opening = text(slide)
        self.assertNotIn('Presenting it in three layers', opening)
        self.assertNotIn('dd-opening-explanation', [e.name for e in slide.els])
        diagram = next(e for e in slide.els if e.name == 'dd-official-diagram')
        self.assertEqual(diagram.w, round(1080*.9))
        self.assertEqual(diagram.x+diagram.w/2, 960)
        labels = [e for e in slide.els if e.name == 'dd-space-label']
        self.assertEqual(len(labels), 2)
        for label, name, center in zip(labels, ('Problem Space', 'Solution Space'), (246, 694)):
            self.assertEqual(label.paras[0].runs[0].text, name)
            self.assertAlmostEqual(label.x+label.w/2, diagram.x+diagram.w*center/936)
            self.assertLessEqual(label.y+label.h, diagram.y)

    def test_experience_is_impersonal_in_slides_and_notes(self):
        import re
        from deck.week10_nicolo_case import POSITIVE_QUOTES, WISH_QUOTES
        for slide in self.slides:
            content = text(slide)+' '+slide.notes
            for quote in POSITIVE_QUOTES+WISH_QUOTES:
                content = content.replace(quote, '')
            self.assertIsNone(re.search(r'\b(I|my|me|mine|myself|we|our|ours)\b',
                                        content))
        for slide in self.slides[1:5]:
            self.assertIn('INDUSTRY EXAMPLE', text(slide))
            self.assertNotIn('INDUSTRY EXPERIENCE', text(slide))
        self.assertIn('Five usability tests were run', text(self.slides[4]))

    def test_engineer_role_except_unchanged_slide07(self):
        import re
        self.assertIn('an Engineer', text(self.slides[3]))
        for i, slide in enumerate(self.slides):
            if i != 6:
                self.assertIsNone(re.search(r'\bdevelopers?\b', text(slide)+' '+slide.notes, re.I))
        old = subprocess.check_output(['git', 'show', '847e965:deck/week10_nicolo.py'],
                                      cwd=ROOT, text=True)
        current = (ROOT/'deck/week10_nicolo.py').read_text()
        start = "S.append(three('DOUBLE DIAMOND / COLLABORATION'"
        stop = 'The following case'
        self.assertEqual(old[old.index(start):old.index(stop)],
                         current[current.index(start):current.index('The following four-phase case')])

    def test_notes_companion_matches_current_slides(self):
        companion = (ROOT/'lessons/week10-nicolo-speaker-notes.md').read_text()
        expected = ''.join(f'## {i:02d} / {s.title}\n\n{s.notes}\n\n'
                           for i, s in enumerate(self.full_slides, 1)).rstrip()+'\n'
        self.assertEqual(companion[companion.index('## 01 /'):], expected)

    def test_phase_subtitles_maps_and_reading_order(self):
        from deck.week10_nicolo import PHASES
        from deck.week10_nicolo_figures import phase_map, THINKING_MODES
        for i, (space, phase) in enumerate(PHASES):
            phase_index = i % 4
            slide = self.slides[i+1]
            self.assertIn('divergent thinking' if phase_index in (0, 2) else 'convergent thinking', text(slide))
            subtitle = next(e for e in slide.els if e.name == 'phase-subtitle')
            root = ET.fromstring(subtitle.svg)
            self.assertEqual(root.get('aria-label'), space+' \u25c6 '+THINKING_MODES[phase])
            self.assertEqual(root.get('aria-label'), root.get('aria-label').lower())
            texts = list(root.iter('{http://www.w3.org/2000/svg}tspan'))
            row = root.find('{http://www.w3.org/2000/svg}text')
            for setting in ('font-optical-sizing:none', 'font-feature-settings:normal',
                            'text-rendering:geometricPrecision'):
                self.assertIn(setting, row.get('style'))
            self.assertTrue(all(not t.tail for t in texts))
            self.assertEqual([t.text for t in texts], [space, '\u25c6', THINKING_MODES[phase]])
            self.assertEqual([t.get('fill') for t in texts], ['#5A626B', '#246E70', '#5A626B'])
            self.assertAlmostEqual(float(texts[1].get('font-size')), 34/3)
            self.assertLess(float(texts[1].get('y')), float(texts[0].get('y')))
            self.assertEqual(float(texts[1].get('dx')), float(texts[2].get('dx')))
            self.assertLessEqual(float(texts[1].get('dx')), 14)
            self.assertLessEqual(subtitle.x+subtitle.w, 1440)
            self.assertNotIn('\u2022', text(slide))
            title = next(e for e in slide.els if e.name == 'variant-heading')
            self.assertGreaterEqual(subtitle.y, title.y+title.h)
            maps = [e for e in slide.els if e.name == 'phase-navigation']
            self.assertEqual(len(maps), 1)
            self.assertLessEqual(maps[0].w, 400)
            self.assertLessEqual(maps[0].y+maps[0].h, 400)
            svg, _ = phase_map(phase)
            self.assertNotIn('<text', svg)
            self.assertEqual(svg.count('fill="#246E70"'), 1)
            self.assertIn('after Design Council', slide.notes)
            names = [e.name for e in slide.els]
            self.assertLess(names.index('phase-subtitle'), names.index('phase-navigation'))

    def test_iteration_map_has_no_accent_and_phase_durations_are_explicit(self):
        slide = self.slides[5]
        maps = [e for e in slide.els if e.name == 'phase-navigation']
        self.assertEqual(len(maps), 1)
        self.assertEqual((maps[0].x, maps[0].y, maps[0].w, maps[0].h), (1440, 210, 360, 176))
        self.assertNotIn('#246E70', maps[0].svg)
        self.assertEqual(maps[0].svg.count('fill="#FFFFFF"'), 4)
        self.assertIn('The phases do not all take the same amount of time.', text(slide))
        self.assertIn('do not represent equal durations', slide.notes)
        title = next(e for e in slide.els if e.name == 'variant-heading')
        self.assertLessEqual(title.x+title.w, maps[0].x)
        columns = [e for e in slide.els if e.name.startswith('column-')]
        self.assertTrue(all(e.y > maps[0].y+maps[0].h for e in columns))

    def test_links_notes_privacy_and_geometry(self):
        links = [r.url for e in self.slides[0].els if hasattr(e, 'paras')
                 for p in e.paras for r in p.runs if r.url]
        self.assertIn('https://www.designcouncil.org.uk/resources/the-double-diamond/', links)
        self.assertIn('https://creativecommons.org/licenses/by/4.0/', links)
        for slide in self.slides:
            self.assertGreater(len(slide.notes), 180)
            self.assertFalse(slide.cp or slide.report)
            self.assertNotIn('ESFQ', text(slide))
            for e in slide.els:
                if not all(hasattr(e, k) for k in ('x', 'y', 'w', 'h')):
                    continue
                self.assertGreaterEqual(e.x, 0)
                self.assertGreaterEqual(e.y, 0)
                self.assertLessEqual(e.x+e.w, 1920)
                self.assertLessEqual(e.y+e.h, 1080)
                if not e.name.startswith('chrome-'):
                    self.assertLessEqual(e.y+e.h, 1000)


if __name__ == '__main__':
    unittest.main()
