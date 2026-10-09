"""Regressions for the approved demo-to-reference workshop revision."""
import base64
import unittest
from urllib.parse import unquote

from test_week06_sequence import slide_text, slide_links


class Week06RevisionTests(unittest.TestCase):
    def setUp(self):
        from deck.week06 import S
        self.slides = S

    def test_four_musical_layers_each_have_a_seeded_editor_link(self):
        for layer in ('Rhythm', 'Bass', 'Harmony', 'Melody'):
            matches = [s for s in self.slides if s.title.startswith(layer + ':')]
            self.assertEqual(len(matches), 1, layer)
            links = [u for u in slide_links(matches[0]) if u.startswith('https://strudel.cc/#')]
            self.assertEqual(len(links), 1, layer)
            code = base64.b64decode(unquote(links[0].split('#', 1)[1])).decode()
            self.assertIn('setcpm(100/4)', code)
            self.assertIn('stack(', code)

    def test_editor_link_round_trips_utf8_and_uses_official_fragment_encoding(self):
        from deck.week06 import editor_link
        code = 'note("c4 e4") // caf\u00e9'
        fragment = editor_link(code).split('#', 1)[1]
        self.assertNotIn('=', fragment)
        self.assertEqual(base64.b64decode(unquote(fragment)).decode(), code)

    def test_editor_mini_notation_uses_parsed_not_literal_quotes(self):
        from deck.week06 import PARTS
        for name, code in PARTS:
            self.assertRegex(code, r'^note\("[^"\n]+"\)', name)

    def test_questions_follow_actual_making_and_saving(self):
        questions = [i for i, s in enumerate(self.slides) if s.cp]
        self.assertEqual(len(questions), 2)
        saved = next(i for i, s in enumerate(self.slides) if s.title == 'Check the final result—not just the preview.')
        self.assertTrue(all(i > saved for i in questions))

    def test_reference_workshop_reuses_students_exported_demo(self):
        reference = next(s for s in self.slides if s.title == 'Transform your demo—not an unrelated prompt.')
        text = slide_text(reference).lower()
        self.assertIn('reference', text)
        self.assertIn('exported', text)
        self.assertIn('suno', text)
        all_text = ' '.join(slide_text(s) for s in self.slides)
        self.assertNotIn('0–4 s', all_text)
        self.assertIn('GarageBand', all_text)

    def test_live_frequency_analysis_exists_without_microphone_access(self):
        from deck.week06 import ANALYSIS_CODE
        self.assertIn('createAnalyser', ANALYSIS_CODE)
        self.assertIn('getFloatFrequencyData', ANALYSIS_CODE)
        self.assertIn('getFloatTimeDomainData', ANALYSIS_CODE)
        self.assertNotIn('getUserMedia', ANALYSIS_CODE)
        self.assertIn('slide:stop', ANALYSIS_CODE)

    def test_rights_distinguish_reference_output_and_copyright(self):
        text = ' '.join(slide_text(s) for s in self.slides).lower()
        for phrase in ('original demo', 'non-commercial', 'approved download', 'copyright', 'easel/provider'):
            self.assertIn(phrase, text)


if __name__ == '__main__':
    unittest.main()
