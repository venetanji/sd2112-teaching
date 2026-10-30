"""Week 9 team text submissions: native activities and private report boundary.

Artifact checks inspect existing exports, never build them. Rebuild Week 9 before
running these after a source revision; missing artifacts are explicitly skipped.
"""
from copy import deepcopy
from html.parser import HTMLParser
from pathlib import Path
import json
import posixpath
import re
import runpy
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as E
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'deck/week09-reports.json'
QUESTIONS = {
    40: 'Where have you encountered harmful AI bias?',
    43: 'How could this harmful bias be reduced or removed?',
}
NS = {
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'rel': 'http://schemas.openxmlformats.org/package/2006/relationships',
}


class ActivityBadges(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slide = None
        self.badges = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section' and 'data-slide' in attrs:
            self.slide = int(attrs['data-slide'])
        if 'data-classpoint' in attrs:
            self.badges.append((self.slide, attrs))

    def handle_endtag(self, tag):
        if tag == 'section':
            self.slide = None


class Week09ClassPointTests(unittest.TestCase):
    def load(self, entries=None):
        if entries is None:
            return runpy.run_path(str(ROOT / 'deck/week09.py'))
        from deckgen.reports import load as real_load

        def injected(source):
            # attach_reports loads the already-sanitized list a second time.
            if isinstance(source, (str, Path)) and Path(source).resolve() == REPORTS:
                return entries
            return real_load(source)

        with patch('deckgen.reports.load', side_effect=injected):
            return runpy.run_path(str(ROOT / 'deck/week09.py'))

    def entries(self):
        return [{'question': title, 'activity': f'https://example.invalid/week09-{position}'}
                for position, title in QUESTIONS.items()]

    def assert_no_reports(self, slides):
        for slide in slides:
            self.assertFalse(slide.report)
            for element in slide.els:
                for paragraph in getattr(element, 'paras', []):
                    for run in paragraph.runs:
                        self.assertFalse(run.url and ('example.invalid/week09' in run.url
                                                     or 'app.classpoint.io/activity/' in run.url))

    def assert_settings(self, metadata):
        self.assertEqual(metadata['type'], 'short_answer')
        self.assertIs(metadata['hide_names'], True)
        self.assertIs(metadata['multiple'], False)

    def assert_native_settings(self, model):
        self.assertEqual(model['ActivityType'], 1)
        self.assertIs(model['IsQuizMode'], False)
        self.assertIsNone(model['ActivityId'])
        native = model['ActivityBase']
        self.assertIn('ShortAnswerActivity', native['$type'])
        self.assertEqual(native['activityType'], 'Short Answer')
        self.assertIs(native['isNamesHidden'], True)
        self.assertIs(native['isMultipleSubmissionsAllowed'], False)
        self.assertIsNone(native['gradingInstructions'])
        self.assertIsNone(native['activityId'])

    def test_only_two_native_short_answers_in_requested_order(self):
        from deckgen.classpoint import activity
        slides = self.load()['S']
        actual = {i: slide for i, slide in enumerate(slides, 1) if slide.cp}
        self.assertEqual(list(actual), list(QUESTIONS))
        for position, slide in actual.items():
            self.assertEqual(slide.title.replace('\n', ' '), QUESTIONS[position])
            self.assert_settings(slide.cp)
            self.assert_native_settings(activity(slide.cp))
        self.assert_no_reports(slides)

    def test_private_report_ids_are_withheld_without_mutating_input(self):
        entries = self.entries()
        original = deepcopy(entries)
        deck = self.load(entries)
        self.assert_no_reports(deck['S'])
        self.assertEqual(entries, original)
        adapter = deck['protected_report_entries']
        masked = adapter(entries)
        self.assertEqual(entries, original)
        self.assertEqual(len(masked), 2)
        for raw, safe in zip(entries, masked):
            self.assertIsNot(raw, safe)
            self.assertEqual(safe['question'], raw['question'])
            self.assertIsNone(safe['activity'])
            self.assertTrue(safe.get('withheld'))

    def test_sanitization_precedes_the_only_attachment_on_fresh_slides(self):
        from deckgen import attach_reports as real_attach
        seen = []

        def checked_attach(slides, source, *args, **kwargs):
            self.assert_no_reports(slides)
            self.assertIsInstance(source, list)
            self.assertEqual([e['question'] for e in source], list(QUESTIONS.values()))
            self.assertTrue(all(e['activity'] is None and e.get('withheld') for e in source))
            seen.append(deepcopy(source))
            return real_attach(slides, source, *args, **kwargs)

        with patch('deckgen.attach_reports', side_effect=checked_attach):
            deck = self.load(self.entries())
        self.assertEqual(len(seen), 1)
        self.assert_no_reports(deck['S'])

    def test_missing_empty_and_explicitly_withheld_reports_are_safe(self):
        entries = [{'question': title, 'activity': None, 'withheld': 'private team response'}
                   for title in QUESTIONS.values()]
        for fixture in ([], entries):
            with self.subTest(fixture=fixture):
                self.assert_no_reports(self.load(fixture)['S'])
        deck = self.load([])
        self.assertEqual(deck['protected_report_entries'](ROOT / 'nonexistent-week09-reports.json'), [])

    def test_count_and_each_private_question_drift_still_fail_without_mutation(self):
        entries = self.entries()
        for fixture in (entries[:-1], entries + [dict(entries[-1])]):
            original = deepcopy(fixture)
            with self.assertRaisesRegex(ValueError, 'drifted apart'):
                self.load(fixture)
            self.assertEqual(fixture, original)
        for index in range(2):
            for activity_id in (None, 'https://example.invalid/private'):
                fixture = deepcopy(entries)
                fixture[index] = {'question': 'Changed question', 'activity': activity_id}
                original = deepcopy(fixture)
                with self.subTest(index=index, activity=activity_id):
                    with self.assertRaisesRegex(ValueError, 'now asks'):
                        self.load(fixture)
                    self.assertEqual(fixture, original)

    def test_saved_reports_contain_only_withheld_placeholders(self):
        entries = json.loads(REPORTS.read_text()) if REPORTS.exists() else []
        if entries:
            self.assertEqual([e['question'] for e in entries], list(QUESTIONS.values()))
            for entry in entries:
                self.assertIsNone(entry['activity'])
                self.assertTrue(entry.get('withheld'))

    def artifact(self, relative):
        path = ROOT / relative
        if not path.exists():
            self.skipTest(f'{relative} missing; build Week 9 to verify emitted artifacts')
        # Existing, stale files must fail instead of silently validating an old deck.
        sources = [*ROOT.glob('deck/week09*.py'), ROOT / 'requirements.txt', ROOT / 'deck/course.py']
        if REPORTS.exists():
            sources.append(REPORTS)
        self.assertGreaterEqual(path.stat().st_mtime_ns,
                                max(source.stat().st_mtime_ns for source in sources),
                                f'{relative} predates Week 9 inputs; rebuild before export verification')
        return path

    def test_exported_manifest_positions_types_and_settings(self):
        path = self.artifact('export/week09-activities.json')
        manifest = {int(k): v for k, v in json.loads(path.read_text()).items()
                    if not k.startswith('_')}
        self.assertEqual(sorted(manifest), list(QUESTIONS))
        slides = self.load()['S']
        for position, metadata in manifest.items():
            self.assert_settings(metadata)
            self.assertEqual(metadata, slides[position - 1].cp)

    def test_exported_html_has_exactly_two_private_activity_badges(self):
        path = self.artifact('_site/week09/index.html')
        parser = ActivityBadges()
        parser.feed(path.read_text())
        self.assertEqual([position for position, _ in parser.badges], list(QUESTIONS))
        self.assertTrue(all('href' not in attrs for _, attrs in parser.badges))
        self.assertNotIn('app.classpoint.io/activity/', path.read_text())

    def test_exported_classpoint_buttons_follow_real_tag_relationships(self):
        path = self.artifact('export/week09-classpoint.pptx')
        with zipfile.ZipFile(path) as archive:
            slide_parts = [name for name in archive.namelist()
                           if re.fullmatch(r'ppt/slides/slide\d+\.xml', name)]
            self.assertEqual(len(slide_parts), 51)
            activity_positions, used_tags = [], set()
            for part in sorted(slide_parts, key=lambda name: int(re.search(r'slide(\d+)\.', name)[1])):
                position = int(re.search(r'slide(\d+)\.', part)[1])
                slide = E.fromstring(archive.read(part))
                rel_part = f'ppt/slides/_rels/slide{position}.xml.rels'
                rels = {rel.attrib['Id']: rel.attrib for rel in E.fromstring(archive.read(rel_part))}
                tag_rels = {rid: rel for rid, rel in rels.items() if rel['Type'].endswith('/tags')}
                buttons = [pic for pic in slide.findall('.//p:pic', NS)
                           if pic.find('p:nvPicPr/p:cNvPr', NS).get('name') == 'btnInknoeActivityCp2']
                references = slide.findall('.//p:tags', NS)
                if position not in QUESTIONS:
                    self.assertEqual((len(buttons), len(tag_rels), len(references)), (0, 0, 0))
                    continue
                activity_positions.append(position)
                self.assertEqual((len(buttons), len(tag_rels), len(references)), (1, 1, 1))
                tags = buttons[0].findall('.//p:tags', NS)
                self.assertEqual(len(tags), 1)
                rid = tags[0].get(f'{{{NS["r"]}}}id')
                self.assertIn(rid, tag_rels)
                tag_part = posixpath.normpath(posixpath.join('ppt/slides', tag_rels[rid]['Target']))
                self.assertNotIn(tag_part, used_tags)
                used_tags.add(tag_part)
                models = [tag for tag in E.fromstring(archive.read(tag_part)).findall('p:tag', NS)
                          if tag.get('name') == 'ACTIVITYMODEL']
                self.assertEqual(len(models), 1)
                self.assert_native_settings(json.loads(models[0].get('val')))
                image = buttons[0].find('p:blipFill/a:blip', NS)
                image_rel = rels[image.get(f'{{{NS["r"]}}}embed')]
                self.assertTrue(image_rel['Type'].endswith('/image'))
                image_part = posixpath.normpath(posixpath.join('ppt/slides', image_rel['Target']))
                self.assertTrue(archive.read(image_part))
            self.assertEqual(activity_positions, list(QUESTIONS))
            all_model_parts = {name for name in archive.namelist() if name.startswith('ppt/tags/')
                               and b'ACTIVITYMODEL' in archive.read(name)}
            self.assertEqual(all_model_parts, used_tags)

    def test_exported_plain_powerpoint_has_no_activity_models_or_buttons(self):
        path = self.artifact('export/week09.pptx')
        with zipfile.ZipFile(path) as archive:
            for name in archive.namelist():
                if name.endswith(('.xml', '.rels')):
                    content = archive.read(name)
                    self.assertNotIn(b'ACTIVITYMODEL', content, name)
                    self.assertNotIn(b'btnInknoeActivityCp2', content, name)
                    if name.endswith('.rels'):
                        self.assertFalse(any(rel.get('Type', '').endswith('/tags')
                                             for rel in E.fromstring(content)), name)


if __name__ == '__main__':
    unittest.main()
