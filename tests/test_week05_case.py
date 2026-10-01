import unittest
from pathlib import Path

from deck.week05_case import slides


def slide_text(slide):
    return " ".join(
        run.text
        for element in slide.els
        if hasattr(element, "paras")
        for paragraph in element.paras
        for run in paragraph.runs
    )


class Week05CaseTests(unittest.TestCase):
    def test_three_slides_tell_the_approved_case_in_order(self):
        deck = slides()
        self.assertEqual(len(deck), 3)
        text = [slide_text(slide) for slide in deck]
        titles = (
            "The brief emerged through choices.",
            "A better prompt was not always the right repair.",
            "What did the agent actually contribute?",
        )
        positions = [next(i for i, body in enumerate(text) if title in body) for title in titles]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("CLEAN MARK", text[0])
        self.assertIn("FOREST VARIANT", text[0])
        self.assertIn("BRIGHTER EDIT", text[0])
        self.assertIn("TARGETED CHANGE", text[1])
        for label in ("HUMAN", "AGENT", "MEDIA", "CODE", "JUDGES"):
            self.assertIn(label, text[2])

    def test_brightened_mark_is_a_local_resolvable_source_image(self):
        deck = slides()
        images = [element for element in deck[0].els if type(element).__name__ == "Image"]
        self.assertEqual(len(images), 3)
        for image in images:
            self.assertTrue(Path(image.src).is_file(), image.src)
        self.assertTrue(any(Path(image.src).name == "week05-logo-brighter-edit.png" for image in images))

    def test_notes_ground_claims_and_avoid_overstating_acceptance(self):
        deck = slides()
        notes = " ".join(slide.notes for slide in deck)
        self.assertIn("September 2026", notes)
        self.assertIn("V8", notes)
        self.assertIn("V9", notes)
        self.assertIn("95 replacement frames", notes)
        self.assertIn("lossless master frames", notes)
        self.assertIn("review pending", notes)
        self.assertNotIn("accepted final", notes.lower())
        self.assertNotIn("pixel-identical", notes.lower())
        self.assertIn("do not call it accepted or claim scientifically accurate combustion", notes.lower())

    def test_slides_fit_the_approved_short_case_scope(self):
        deck = slides()
        text = " ".join(slide_text(slide) for slide in deck)
        self.assertIn("What did you delegate—and what did you insist on keeping?", text)
        self.assertNotIn("ClassPoint", text)
        self.assertNotIn("activity(", text)
        self.assertLessEqual(max(len(slide.els) for slide in deck), 24)

    def test_before_and_after_are_distinct_saved_edits_not_duplicate_exports(self):
        from PIL import Image, ImageChops, ImageStat
        images = [e for e in slides()[0].els if type(e).__name__ == 'Image']
        with Image.open(images[1].src) as before, Image.open(images[2].src) as after:
            difference = ImageChops.difference(before.convert('RGB').resize((512, 512)),
                                              after.convert('RGB').resize((512, 512)))
            self.assertGreater(sum(ImageStat.Stat(difference).mean) / 3, 5)

    def test_case_content_stays_above_footer(self):
        for slide in slides():
            for element in slide.els:
                if hasattr(element, 'paras'):
                    self.assertLessEqual(element.y + element.h, 995, slide.title)


if __name__ == "__main__":
    unittest.main()
