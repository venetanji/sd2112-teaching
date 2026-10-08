import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image
from deckgen.core import pil_font
from deck import week06_figures as F

NS = '{http://www.w3.org/2000/svg}'
FIGURES = ('w06_waveform', 'w06_spectrogram_how', 'w06_midi',
           'w06_grid_score', 'w06_generate_test', 'w06_two_roads', 'w06_sound_spec',
           'w06_written_score', 'w06_strudel_pattern')


def text_bounds(label):
    font = pil_font('monomed' if 'JetBrains' in label.attrib['font-family']
                    else 'semibold', round(float(label.attrib['font-size']) * 2))
    x, y = float(label.attrib['x']), float(label.attrib['y'])
    width = font.getlength(label.text) / 2
    anchor = label.attrib['text-anchor']
    x -= width / 2 if anchor == 'middle' else width if anchor == 'end' else 0
    left, top, right, bottom = font.getbbox(label.text)
    ascent = font.getmetrics()[0]
    return x + left / 2, y + (top - ascent) / 2, x + right / 2, y + (bottom - ascent) / 2


class Week06FiguresTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rendered = {name: getattr(F, name)() for name in FIGURES}

    def test_all_public_figures_render_svg_and_png(self):
        for name, (svg, png) in self.rendered.items():
            with self.subTest(figure=name):
                root = ET.fromstring(svg)
                self.assertEqual(root.tag, NS + 'svg')
                self.assertTrue(Path(png).is_file())
                with Image.open(png) as image:
                    self.assertEqual(image.size, (int(root.attrib['width']) * 2,
                                                  int(root.attrib['height']) * 2))

    def test_labels_are_legible_and_within_figure(self):
        for name, (svg, _) in self.rendered.items():
            root = ET.fromstring(svg)
            w, h = float(root.attrib['width']), float(root.attrib['height'])
            for label in root.iter(NS + 'text'):
                with self.subTest(figure=name, text=label.text):
                    self.assertGreaterEqual(float(label.attrib['font-size']), 22)
                    x0, y0, x1, y1 = text_bounds(label)
                    self.assertGreaterEqual(x0, 8)
                    self.assertGreaterEqual(y0, 8)
                    self.assertLessEqual(x1, w - 8)
                    self.assertLessEqual(y1, h - 8)

    def test_shapes_and_lines_stay_inside_figure(self):
        for name, (svg, _) in self.rendered.items():
            root = ET.fromstring(svg)
            w, h = float(root.attrib['width']), float(root.attrib['height'])
            for shape in root.iter():
                points = []
                if shape.tag == NS + 'polygon':
                    points = [tuple(map(float, point.split(',')))
                              for point in shape.attrib['points'].split()]
                elif shape.tag == NS + 'line':
                    points = [(float(shape.attrib['x1']), float(shape.attrib['y1'])),
                              (float(shape.attrib['x2']), float(shape.attrib['y2']))]
                elif shape.tag == NS + 'circle':
                    x, y, r = (float(shape.attrib[a]) for a in ('cx', 'cy', 'r'))
                    points = [(x - r, y - r), (x + r, y + r)]
                for x, y in points:
                    self.assertTrue(4 <= x <= w - 4 and 4 <= y <= h - 4,
                                    (name, shape.tag, x, y))

    def test_nodes_have_measured_padding_and_centered_labels(self):
        for name, (svg, _) in self.rendered.items():
            root = ET.fromstring(svg)
            for group in root.iter(NS + 'g'):
                if group.attrib.get('data-node') != 'true':
                    continue
                x, y, w, h = (float(group.attrib[a]) for a in
                               ('data-x', 'data-y', 'data-w', 'data-h'))
                for label in group.iter(NS + 'text'):
                    x0, y0, x1, y1 = text_bounds(label)
                    self.assertGreaterEqual(x0 - x, 18, (name, label.text))
                    self.assertGreaterEqual(x + w - x1, 18, (name, label.text))
                    self.assertGreaterEqual(y0 - y, 12, (name, label.text))
                    self.assertGreaterEqual(y + h - y1, 12, (name, label.text))
                    self.assertAlmostEqual((y0 + y1) / 2,
                                           float(label.attrib['data-cy']), delta=0.6)

    def test_sound_representations_do_not_claim_to_be_loudness(self):
        waveform = self.rendered['w06_waveform'][0]
        spectrogram = self.rendered['w06_spectrogram_how'][0]
        self.assertIn('amplitude', waveform)
        self.assertIn('not perceptual loudness', waveform)
        self.assertIn('magnitude', spectrogram)
        self.assertIn('Separate illustrative examples', spectrogram)
        self.assertNotIn('dark = loud', spectrogram)
        self.assertNotIn('louder', spectrogram)
        self.assertIn('MIDI carries events, not sound', self.rendered['w06_midi'][0])

    def test_neighboring_pipeline_nodes_leave_space_for_arrows(self):
        for name in ('w06_generate_test', 'w06_two_roads', 'w06_sound_spec'):
            root = ET.fromstring(self.rendered[name][0])
            rows = {}
            for group in root.iter(NS + 'g'):
                x, y, w = (float(group.attrib[a]) for a in
                            ('data-x', 'data-y', 'data-w'))
                rows.setdefault(y, []).append((x, w))
            for boxes in rows.values():
                boxes.sort()
                for (x, w), (next_x, _) in zip(boxes, boxes[1:]):
                    self.assertGreaterEqual(next_x - x - w, 40, name)

    def test_sample_count_matches_the_dots_actually_drawn(self):
        root = ET.fromstring(self.rendered['w06_waveform'][0])
        count = len(list(root.iter(NS + 'circle')))
        self.assertEqual(count, 133)
        self.assertIn(f'{count} samples at 44,100 samples/s', self.rendered['w06_waveform'][0])

    def test_written_score_still_matches_the_live_seed_and_timing(self):
        from deck.week06 import SEQ_CODE
        import json
        import re
        seed = json.loads(re.search(r'let grid = (\[.*?\]);', SEQ_CODE, re.S)[1])
        self.assertEqual(seed, F.WRITTEN_SEED)
        root = ET.fromstring(self.rendered['w06_written_score'][0])
        active = [(int(n.attrib['data-row']), int(n.attrib['data-step']))
                  for n in root.iter(NS + 'polygon') if n.attrib.get('data-active') == '1']
        self.assertEqual(active, [(r, s) for r, row in enumerate(seed)
                                 for s, on in enumerate(row) if on])
        for text in ('C4', 'E4', 'G4', 'B4', '100 BPM', '0.3 s', '2.4 s'):
            self.assertIn(text, self.rendered['w06_written_score'][0])
        self.assertIn('bpm = 100', SEQ_CODE)
        self.assertIn('60/bpm/2', SEQ_CODE)

    def test_strudel_still_matches_the_four_note_sine_pattern(self):
        from deck.week06 import STR_CODE
        self.assertIn(".note('c4 e4 g4 b4')", STR_CODE)
        self.assertIn(".s('sine')", STR_CODE)
        svg = self.rendered['w06_strudel_pattern'][0]
        for text in ('C4', 'E4', 'G4', 'B4', 'sine', 'One cycle'):
            self.assertIn(text, svg)
        self.assertNotIn('kick', svg)
        self.assertNotIn('16 steps', svg)

    def test_documented_audio_roads_keep_phase_and_codec_distinct(self):
        svg = self.rendered['w06_two_roads'][0]
        for label in ('Historic Riffusion v1', 'MAGNITUDE PICTURE',
                      'PHASE RECONSTRUCTION', 'Griffin-Lim', 'MusicGen',
                      'CODEC TOKENS', 'PREDICT TOKENS', 'CODEC DECODE'):
            self.assertIn(label, svg)
        self.assertNotIn('INVERSE FOURIER', svg)
        self.assertNotIn('a table, a die', svg)

    def test_random_rules_and_handwritten_table_remain_machine_a(self):
        svg = self.rendered['w06_generate_test'][0]
        for label in ('MACHINE A', 'handwritten', 'random', 'Illustrative', 'not learned'):
            self.assertIn(label, svg)
        self.assertNotIn('GPT', svg)
        self.assertTrue(all(abs(sum(row) - 1) < 1e-9 for row in F.TRANSITIONS))


if __name__ == '__main__':
    unittest.main()
