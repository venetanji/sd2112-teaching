"""Four-TA Q&A contracts; real pinned native export and synthetic report fixtures."""
from copy import deepcopy
from html.parser import HTMLParser
from pathlib import Path
import json
import posixpath
import re
import runpy
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as E
import zipfile

from PIL import Image as PILImage

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'deck/week10_qa.py'
REPORTS = ROOT / 'deck/week10_qa-reports.json'
NAMES = ('Nicol\u00f2 Azzolin', 'Amber', 'WU Zhao', 'MA Jie')
JOIN_URL = 'https://www.classpoint.app/'
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}


def text(slide):
    return ' '.join(r.text for el in slide.els for p in getattr(el, 'paras', [])
                    for r in p.runs)


def urls(slide):
    return [r.url for el in slide.els for p in getattr(el, 'paras', [])
            for r in p.runs if r.url]


class Badges(HTMLParser):
    def __init__(self):
        super().__init__()
        self.badges = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'data-classpoint' in attrs:
            self.badges.append(attrs)


class Week10QATests(unittest.TestCase):
    @staticmethod
    def load(entries=None):
        if entries is None:
            return runpy.run_path(str(SOURCE))
        from deckgen.reports import load as real_load

        def injected(source):
            if isinstance(source, (str, Path)) and Path(source).resolve() == REPORTS:
                return deepcopy(entries)
            return real_load(source)

        with patch('deckgen.reports.load', side_effect=injected):
            return runpy.run_path(str(SOURCE))

    @classmethod
    def setUpClass(cls):
        from deckgen import configure
        from deckgen.core import build_html, build_pptx
        from deckgen import classpoint
        configure(ROOT)
        cls.deck = cls.load()
        cls.temp = tempfile.TemporaryDirectory(prefix='sd2112-week10-qa-test-')
        cls.addClassCleanup(cls.temp.cleanup)
        cls.out = Path(cls.temp.name)
        cls.plain, cls.manifest = build_pptx(cls.deck['DECK'], cls.out / 'qa.pptx',
                                             footer='SD2112 / WEEK 10')
        cls.native = classpoint.build(cls.plain, footer='SD2112 / WEEK 10',
                                     activities=cls.manifest)
        cls.html = build_html(cls.deck['DECK'], cls.out / 'html')

    def entries(self):
        return [{'question': 'Questions for ' + name,
                 'activity': f'https://example.invalid/qa-{index}'}
                for index, name in enumerate(NAMES)]

    def assert_native(self, model):
        self.assertEqual(model['ActivityType'], 1)
        self.assertIs(model['IsQuizMode'], False)
        self.assertIsNone(model['ActivityId'])
        native = model['ActivityBase']
        self.assertIn('ShortAnswerActivity', native['$type'])
        self.assertEqual(native['activityType'], 'Short Answer')
        self.assertIs(native['isMultipleSubmissionsAllowed'], True)
        self.assertIs(native['isNamesHidden'], False)
        self.assertIsNone(native['gradingInstructions'])
        self.assertIsNone(native['activityId'])
        self.assertIs(native['StartWithSlide'], False)
        self.assertEqual(native['countdown'], 0)

    def test_four_distinct_ta_slides_and_optional_ungraded_contract(self):
        from deckgen.classpoint import activity
        slides = self.deck['S']
        self.assertEqual(len(slides), 4)
        self.assertEqual([s.title for s in slides], ['Questions for ' + n for n in NAMES])
        self.assertEqual(self.deck['DECK']['slides'], slides)
        for name, slide in zip(NAMES, slides):
            self.assertIn(name, text(slide))
            for phrase in ('Optional. Not graded.', 'One question per response',
                           'send more if you wish', 'Names may be visible',
                           'Enter the live class code', 'shown by the presenter'):
                self.assertIn(phrase, text(slide))
            self.assertNotIn('anonymous', text(slide).lower())
            self.assertIn('not a speaking agreement', slide.notes)
            self.assertEqual(slide.cp, {'type': 'short_answer', 'hide_names': False,
                                       'multiple': True})
            self.assert_native(activity(slide.cp))
            self.assertFalse(slide.report)

    def test_qr_asset_and_each_visible_join_link_require_live_code(self):
        path = ROOT / 'deck/assets' / self.deck['JOIN_QR']
        with PILImage.open(path) as image:
            self.assertEqual(image.format, 'PNG')
            self.assertEqual(image.width, image.height)
            self.assertGreaterEqual(image.width, 390)
            self.assertEqual(image.info['Destination'], JOIN_URL)
            # A four-module white quiet zone surrounds the generated code.
            rgb = image.convert('RGB')
            self.assertEqual(rgb.crop((0, 0, 64, image.height)).getextrema(),
                             ((255, 255), (255, 255), (255, 255)))
        for slide in self.deck['S']:
            qr = [e for e in slide.els if e.name == 'qa-join-qr']
            self.assertEqual(len(qr), 1)
            self.assertEqual((qr[0].src, qr[0].url), (self.deck['JOIN_QR'], JOIN_URL))
            self.assertIn(JOIN_URL, urls(slide))
            self.assertLess(qr[0].y + qr[0].h, 880)
            self.assertIn('This file contains no live code', slide.notes)

    def test_reports_match_real_invocation_and_do_not_mutate_fixtures(self):
        entries = self.entries()
        original = deepcopy(entries)
        slides = self.load(entries)['S']
        self.assertEqual(entries, original)
        for slide, entry in zip(slides, entries):
            self.assertEqual(slide.report, entry['activity'])
            self.assertIn(entry['activity'], urls(slide))

    def test_attachment_happens_once_before_finalize_on_fresh_slides(self):
        from deckgen import attach_reports as real_attach
        from deckgen.layouts import finalize as real_finalize
        calls = []

        def attach(slides, source, *args, **kwargs):
            self.assertEqual(source, REPORTS)
            self.assertTrue(all(not s.report for s in slides))
            self.assertFalse(any(el.name == 'chrome-footer' for s in slides for el in s.els))
            calls.append('attach')
            return real_attach(slides, source, *args, **kwargs)

        def finalize(slides, footer):
            self.assertEqual(calls, ['attach'])
            calls.append('finalize')
            return real_finalize(slides, footer)

        with patch('deckgen.attach_reports', side_effect=attach), \
                patch('deckgen.layouts.finalize', side_effect=finalize):
            self.load(self.entries())
        self.assertEqual(calls, ['attach', 'finalize'])

    def test_missing_empty_null_and_unrun_reports_are_safe(self):
        from deckgen.reports import load
        self.assertEqual(load(self.out / 'not-created-reports.json'), [])
        withheld = [{'question': 'Questions for ' + name, 'activity': None,
                     'withheld': 'unrun or private collection'} for name in NAMES]
        for entries in ([], withheld):
            for slide in self.load(entries)['S']:
                self.assertFalse(slide.report)
                self.assertFalse(any('example.invalid' in u for u in urls(slide)))
        mixed = self.entries()
        mixed[1] = withheld[1]
        slides = self.load(mixed)['S']
        self.assertFalse(slides[1].report)
        self.assertEqual(slides[2].report, mixed[2]['activity'])

    def test_report_count_and_each_question_drift_fail_even_if_withheld(self):
        entries = self.entries()
        for fixture in (entries[:-1], entries + [dict(entries[-1])]):
            with self.assertRaisesRegex(ValueError, 'drifted apart'):
                self.load(fixture)
        for index in range(4):
            for activity in (None, 'https://example.invalid/not-a-real-response'):
                fixture = deepcopy(entries)
                fixture[index] = {'question': 'Changed question', 'activity': activity}
                original = deepcopy(fixture)
                with self.subTest(index=index, activity=activity):
                    with self.assertRaisesRegex(ValueError, 'now asks'):
                        self.load(fixture)
                    self.assertEqual(fixture, original)
        reordered = deepcopy(entries)
        reordered[0], reordered[1] = reordered[1], reordered[0]
        with self.assertRaisesRegex(ValueError, 'now asks'):
            self.load(reordered)

    def test_emitted_manifest_and_html_supported_short_answer_badges(self):
        entries = {int(k): v for k, v in json.loads(self.manifest.read_text()).items()
                   if not k.startswith('_')}
        self.assertEqual(sorted(entries), [1, 2, 3, 4])
        self.assertEqual(list(entries.values()), [s.cp for s in self.deck['S']])
        html = self.html.read_text()
        parser = Badges()
        parser.feed(html)
        self.assertEqual(len(parser.badges), 4)
        self.assertTrue(all(b.get('class') == 'cp' for b in parser.badges))
        self.assertEqual(html.count('data-classpoint><b></b>Short answer</div>'), 4)
        self.assertTrue(all('href' not in b for b in parser.badges))
        self.assertNotIn('app.classpoint.io/activity/', html)
        self.assertEqual(len(re.findall(r'<section\b[^>]*data-slide=', html)), 4)

    def test_native_real_button_tag_and_qr_relationships_on_all_four_slides(self):
        qr_bytes = (ROOT / 'deck/assets' / self.deck['JOIN_QR']).read_bytes()
        with zipfile.ZipFile(self.native) as archive:
            slide_parts = sorted(n for n in archive.namelist()
                                 if re.fullmatch(r'ppt/slides/slide\d+\.xml', n))
            self.assertEqual(len(slide_parts), 4)
            used_tags = set()
            for position, part in enumerate(slide_parts, 1):
                root = E.fromstring(archive.read(part))
                rels = {r.get('Id'): r.attrib for r in E.fromstring(
                    archive.read(f'ppt/slides/_rels/slide{position}.xml.rels'))}
                buttons = [p for p in root.findall('.//p:pic', NS)
                           if p.find('p:nvPicPr/p:cNvPr', NS).get('name') == 'btnInknoeActivityCp2']
                self.assertEqual(len(buttons), 1)
                tag_refs = buttons[0].findall('.//p:tags', NS)
                self.assertEqual(len(tag_refs), 1)
                rid = tag_refs[0].get(f'{{{NS["r"]}}}id')
                self.assertTrue(rels[rid]['Type'].endswith('/tags'))
                tag_part = posixpath.normpath(posixpath.join('ppt/slides', rels[rid]['Target']))
                self.assertNotIn(tag_part, used_tags)
                used_tags.add(tag_part)
                models = [t for t in E.fromstring(archive.read(tag_part)).findall('p:tag', NS)
                          if t.get('name') == 'ACTIVITYMODEL']
                self.assertEqual(len(models), 1)
                self.assert_native(json.loads(models[0].get('val')))
                images = []
                for pic in root.findall('.//p:pic', NS):
                    blip = pic.find('p:blipFill/a:blip', NS)
                    rid = blip.get(f'{{{NS["r"]}}}embed')
                    image_part = posixpath.normpath(posixpath.join('ppt/slides', rels[rid]['Target']))
                    images.append((pic, archive.read(image_part)))
                qr = [pic for pic, data in images if data == qr_bytes]
                self.assertEqual(len(qr), 1)
                click = qr[0].find('p:nvPicPr/p:cNvPr/a:hlinkClick', NS)
                self.assertIsNotNone(click)
                self.assertEqual(rels[click.get(f'{{{NS["r"]}}}id')]['Target'], JOIN_URL)
                self.assertEqual(sum(data == qr_bytes for _, data in images), 1)
                self.assertIn('Inter Black', archive.read(part).decode())
            all_models = {n for n in archive.namelist() if n.startswith('ppt/tags/')
                          and b'ACTIVITYMODEL' in archive.read(n)}
            self.assertEqual(all_models, used_tags)
            # The pinned native master has course chrome, not a live join/session QR.
            for part in [n for n in archive.namelist() if n.startswith(('ppt/slideMasters/',
                                                                                     'ppt/slideLayouts/'))]:
                self.assertNotIn(JOIN_URL.encode(), archive.read(part))

    def test_plain_export_has_no_fake_native_activity_buttons_or_models(self):
        with zipfile.ZipFile(self.plain) as archive:
            for name in archive.namelist():
                if name.endswith(('.xml', '.rels')):
                    data = archive.read(name)
                    self.assertNotIn(b'ACTIVITYMODEL', data)
                    self.assertNotIn(b'btnInknoeActivityCp2', data)


if __name__ == '__main__':
    unittest.main()
