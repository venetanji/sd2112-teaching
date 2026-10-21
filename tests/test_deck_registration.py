"""Registration and changed-week CI selection must survive combining weekly PRs."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('registration', Path(__file__).resolve().parents[1] / 'scripts/check_deck_registration.py')
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'deck').mkdir()
        self.config(['week07', 'week08'])
        for name in ('week07', 'week08'):
            (self.root / 'deck' / (name + '.py')).write_text('S=[]\n')

    def config(self, names):
        import json
        (self.root / 'deckgen.toml').write_text('[course]\ndecks=' + json.dumps(names))

    def test_union_keeps_both_weeks(self):
        self.assertEqual(M.registered(self.root), ['week07', 'week08'])

    def test_lost_registration_fails(self):
        self.config(['week08'])
        with self.assertRaisesRegex(ValueError, 'unregistered.*week07'):
            M.registered(self.root)

    def test_missing_source_and_duplicates_fail(self):
        self.config(['week07', 'week09'])
        with self.assertRaisesRegex(ValueError, 'Missing sources'):
            M.registered(self.root)
        self.config(['week07', 'week07'])
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            M.registered(self.root)

    def test_new_week_and_its_test_select_that_week(self):
        self.assertEqual(M.affected(self.root, ['week07', 'week08'], ['deck/week08.py', 'tests/test_week08_sequence.py', 'deckgen.toml']), ['week08'])

    def test_imported_helper_selects_all_dependents(self):
        for name in ('week07', 'week08'):
            (self.root / 'deck' / (name + '.py')).write_text('import shared\n')
        (self.root / 'deck/shared.py').write_text('import inner\n')
        (self.root / 'deck/inner.py').write_text('import shared\n')
        self.assertEqual(M.affected(self.root, ['week07', 'week08'], ['deck/inner.py']), ['week07', 'week08'])

    def test_assets_and_unknown_changes_build_everything(self):
        for path in ('deck/assets/a.png', 'requirements.txt', 'scripts/check_deck_registration.py'):
            self.assertEqual(M.affected(self.root, ['week07', 'week08'], [path]), ['week07', 'week08'])


if __name__ == '__main__':
    unittest.main()
