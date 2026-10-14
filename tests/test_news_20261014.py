"""Offline content/geometry checks for the dated news opener."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "deck"))
from news_20261014 import news_slides

class NewsTests(unittest.TestCase):
    def test_seven_sourced_non_assessed_items(self):
        for course in ("SD5913", "SD2112"):
            slides = news_slides(course)
            self.assertEqual(len(slides), 7)
            self.assertEqual(slides[0].title, "Gemini 4 Argon")
            for slide in slides:
                self.assertFalse(slide.cp)
                self.assertIn("Primary source: https://", slide.notes)
                self.assertIn("not assessed", slide.notes)
                self.assertEqual(slide.els[2].h, 340)
                self.assertTrue(any(el.kind == "text" and el.y == 908 for el in slide.els))

if __name__ == "__main__":
    unittest.main()
