import unittest
import xml.etree.ElementTree as ET

from deckgen.core import pil_font
from deck.week05 import F

NS = '{http://www.w3.org/2000/svg}'


class Week05DiagramAlignmentTests(unittest.TestCase):
    def test_single_line_labels_are_visually_centered_in_their_shapes(self):
        cases = ((F.diffusion_training, 'VAE ENCODER', 132.5),
                 (F.diffusion_generation, 'VAE DECODER', 270),
                 (F.diffusion_generation, 'TEXT FEATURES', 55))
        for diagram, text, expected in cases:
            with self.subTest(label=text):
                root = ET.fromstring(diagram()[0])
                label = next(t for t in root.iter(NS + 'text') if t.text == text)
                font = pil_font('semibold', round(float(label.attrib['font-size']) * 2))
                top, bottom = font.getbbox(text)[1::2]
                ascent = font.getmetrics()[0]
                center = float(label.attrib['y']) + ((top + bottom) / 2 - ascent) / 2
                self.assertAlmostEqual(center, expected, delta=0.6)

    def test_random_input_has_padding_and_nonoverlapping_neighbors(self):
        root = ET.fromstring(F.gan_adversaries()[0])
        polygons = [[tuple(map(float, point.split(',')))
                     for point in polygon.attrib['points'].split()]
                    for polygon in root.iter(NS + 'polygon')]
        boxes = [points for points in polygons if points[0][1] == 215]
        box = boxes[0]
        label = next(t for t in root.iter(NS + 'text') if t.text == 'RANDOM INPUT')
        font = pil_font('semibold', round(float(label.attrib['font-size']) * 2))
        width = font.getlength(label.text) / 2
        self.assertGreaterEqual((box[1][0] - box[0][0] - width) / 2, 28)
        for left, right in zip(boxes, boxes[1:]):
            self.assertGreaterEqual(right[0][0] - left[1][0], 50)
