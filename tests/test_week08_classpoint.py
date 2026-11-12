"""Week 8's three activities and private-response report boundary."""
from pathlib import Path
import json
import runpy
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def text(slide):
    return ' '.join(r.text for e in slide.els if hasattr(e, 'paras')
                    for p in e.paras for r in p.runs)


class Week08ClassPointTests(unittest.TestCase):
    def load(self, entries=None):
        if entries is None:
            return runpy.run_path(str(ROOT / 'deck/week08.py'))
        from deckgen.reports import load as real_load
        with patch('deckgen.reports.load', side_effect=lambda source:
                   entries if isinstance(source, Path) else real_load(source)):
            return runpy.run_path(str(ROOT / 'deck/week08.py'))

    def test_three_native_activities_in_the_requested_order(self):
        from deckgen.classpoint import activity
        deck = self.load()
        questions = [s for s in deck['S'] if s.cp]
        self.assertEqual([deck['S'].index(s) + 1 for s in questions], [9, 10, 45])
        self.assertEqual([s.cp['type'] for s in questions],
                         ['multiple_choice', 'short_answer', 'short_answer'])
        poll, follow, paper = questions
        self.assertIn('deep secret', poll.title)
        self.assertIn('would not tell a human', poll.title)
        self.assertEqual(poll.cp['choices'], ['A', 'B'])
        self.assertIn('Yes', text(poll))
        self.assertIn('No', text(poll))
        for s in (poll, follow):
            self.assertIn('Optional', text(s))
            self.assertIn('skip', text(s))
            self.assertIn('identify you', text(s))
            self.assertIn('Do not publish', s.notes)
            self.assertFalse(getattr(s, 'report', None))
        self.assertIn('not the secret', text(follow))
        self.assertIn('No names', text(follow))
        self.assertIn('Each person', text(paper))
        self.assertIn('different paper', text(paper))
        self.assertIn('URL', text(paper))
        self.assertIn('relevant', text(paper))
        self.assertLess(deck['S'].index(paper), next(i for i, s in enumerate(deck['S'])
                        if s.title == 'Change a claim before adding a feature.'))
        mc = activity(poll.cp)
        self.assertEqual(mc['ActivityType'], 0)
        self.assertFalse(mc['IsQuizMode'])
        self.assertFalse(mc['ActivityBase']['mcIsAllowSelectMultiple'])
        self.assertFalse(mc['ActivityBase']['HasCorrectAnswers'])
        self.assertEqual(mc['ActivityBase']['mcCorrectAnswers']['$values'], [])
        for s, hidden in ((follow, True), (paper, False)):
            model = activity(s.cp)
            self.assertEqual(model['ActivityType'], 1)
            self.assertEqual(model['ActivityBase']['isNamesHidden'], hidden)
            self.assertFalse(model['ActivityBase']['isMultipleSubmissionsAllowed'])

    def test_private_reports_cannot_be_published_even_if_ids_are_supplied(self):
        base = self.load()
        questions = [s for s in base['S'] if s.cp]
        self.assertEqual(len(questions), 3)
        urls = [f'https://example.invalid/week08-{i}' for i in range(3)]
        entries = [{'question': s.title, 'activity': url}
                   for s, url in zip(questions, urls)]
        deck = self.load(entries)
        actual = [s for s in deck['S'] if s.cp]
        self.assertFalse(getattr(actual[0], 'report', None))
        self.assertFalse(getattr(actual[1], 'report', None))
        self.assertEqual(actual[2].report, urls[2])
        for s in deck['S']:
            links = [r.url for e in s.els if hasattr(e, 'paras')
                     for p in e.paras for r in p.runs]
            self.assertNotIn(urls[0], links)
            self.assertNotIn(urls[1], links)
        self.assertEqual(entries[0]['activity'], urls[0])

    def test_empty_and_withheld_reports_are_safe(self):
        for entries in ([], [{'activity': None, 'question': s.title}
                            for s in self.load()['S'] if s.cp]):
            deck = self.load(entries)
            self.assertTrue(all(not getattr(s, 'report', None) for s in deck['S']))

    def test_count_and_private_question_drift_still_fail(self):
        questions = [s for s in self.load()['S'] if s.cp]
        self.assertEqual(len(questions), 3)
        entries = [{'activity': None, 'question': s.title} for s in questions]
        for wrong_count in (entries[:-1], entries + [entries[-1]]):
            with self.assertRaisesRegex(ValueError, 'drifted apart'):
                self.load(wrong_count)
        for i in range(3):
            changed = [dict(e) for e in entries]
            changed[i] = {'activity': 'https://example.invalid/private', 'question': 'Changed question'}
            with self.assertRaisesRegex(ValueError, 'now asks'):
                self.load(changed)

    def test_saved_report_file_never_contains_personal_activity_ids(self):
        source = ROOT / 'deck/week08-reports.json'
        entries = json.loads(source.read_text()) if source.exists() else []
        if entries:
            self.assertEqual(len(entries), 3)
            for entry in entries[:2]:
                self.assertIsNone(entry['activity'])
                self.assertIn('withheld', entry)


if __name__ == '__main__':
    unittest.main()
