"""Weekly downloads contain only that week's generated teaching material."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/prepare_weekly_artifacts.py'


class WeeklyArtifactsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.out = self.root / 'packages'
        spec = importlib.util.spec_from_file_location('weekly_artifacts', SCRIPT)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.write('deckgen.toml', '[course]\ndecks=["week08", "week09"]\n')
        for deck in ('week08', 'week09'):
            for suffix in ('.pptx', '-classpoint.pptx', '-activities.json'):
                self.write('export/' + deck + suffix)
            self.write(f'export/preview/{deck}-sheet-1.jpg')
            self.write(f'export/docs/{deck}-speaker-notes.docx')
            self.write(f'export/docs/{deck}-speaker-notes.html')

    def write(self, name, content='generated fixture'):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def test_selected_week_contains_slides_pdf_notes_and_previews(self):
        selected = self.write('selected.json', '["week09"]')
        self.write('_site/week09/SD2112-week09.pdf')
        self.write('export/week08-reading/private-paper.pdf')
        self.write('export/docs/syllabus.docx')
        packages = self.module.prepare(self.root, self.out, selected)
        self.assertEqual([p['deck'] for p in packages], ['week09'])
        package = packages[0]
        folder = Path(package['root'])
        self.assertEqual({str(Path(p).relative_to(folder)) for p in package['files']}, {
            'week09.pptx', 'week09-classpoint.pptx', 'week09-activities.json',
            'SD2112-week09.pdf', 'preview/week09-sheet-1.jpg',
            'docs/week09-speaker-notes.docx', 'docs/week09-speaker-notes.html',
        })
        self.assertTrue(all(Path(p).is_file() for p in package['files']))
        self.assertEqual(json.loads((self.out / 'manifest.json').read_text()), packages)

    def test_default_roster_packages_all_weeks_without_pdf_requirement(self):
        packages = self.module.prepare(self.root, self.out)
        self.assertEqual([p['deck'] for p in packages], ['week08', 'week09'])
        self.assertFalse(any(p.endswith('.pdf') for package in packages for p in package['files']))

    def test_missing_or_empty_required_outputs_fail_instead_of_partial_download(self):
        missing = self.root / 'export/week09-classpoint.pptx'
        missing.unlink()
        with self.assertRaisesRegex(ValueError, 'week09-classpoint.pptx'):
            self.module.prepare(self.root, self.out)
        missing.write_text('')
        with self.assertRaisesRegex(ValueError, 'week09-classpoint.pptx'):
            self.module.prepare(self.root, self.out)

    def test_invalid_roster_fails_before_packaging(self):
        for data in ('[]', '["week09", "week09"]', '["../week09"]', '["week10"]', '{}'):
            selected = self.write('selected.json', data)
            with self.subTest(data=data), self.assertRaises(ValueError):
                self.module.prepare(self.root, self.out, selected)


if __name__ == '__main__':
    unittest.main()
