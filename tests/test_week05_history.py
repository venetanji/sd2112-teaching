import unittest
from pathlib import Path

from deck import week05_history as H


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = (
    "Machine A: design the procedure.",
    "Bense: can aesthetic form be described systematically?",
    "Nake: the artist programs possibilities.",
    "A new machine. A familiar argument.",
    "There should be no Computer Art.",
)


def slide_text(slide):
    return " ".join(
        run.text
        for element in slide.els
        if hasattr(element, "paras")
        for paragraph in element.paras
        for run in paragraph.runs
    )


class Week05HistoryTests(unittest.TestCase):
    def test_exactly_five_slides_in_approved_order(self):
        slides = H.slides()
        self.assertEqual(len(slides), 5)
        self.assertEqual(tuple(slide.title for slide in slides), EXPECTED)

    def test_visual_evidence_includes_both_nake_artworks_and_procedure_diagram(self):
        slides = H.slides()
        images = [element for slide in slides for element in slide.els if type(element).__name__ == "Image"]
        figures = [element for slide in slides for element in slide.els if type(element).__name__ == "Figure"]
        image_paths = {Path(image.src).name for image in images}
        self.assertIn("nake-homage-to-paul-klee-1965.jpg", image_paths)
        self.assertIn("nake-walk-through-raster-1966.jpg", image_paths)
        self.assertGreaterEqual(len(figures), 1)
        for image in images:
            self.assertTrue(Path(image.src).is_file(), image.src)

    def test_machine_a_bense_nake_and_public_debate_content_is_precise(self):
        slides = H.slides()
        text = " ".join(slide_text(slide) for slide in slides)
        text += " " + " ".join(
            element.svg
            for slide in slides
            for element in slide.els
            if type(element).__name__ == "Figure"
        )
        for phrase in (
            "person", "program", "plotter", "chance", "information",
            "generative aesthetics", "Hommage to Paul Klee", "Walk-Through-Raster",
            "Cybernetic Serendipity", "Zagreb", "market", "mystification",
            "new methods", "social communication",
        ):
            self.assertIn(phrase.casefold(), text.casefold())
        self.assertNotIn("entropy is beauty", text.casefold())
        self.assertNotRegex(text, r"\b[RD]\[\]")

    def test_history_slides_have_source_notes_and_fit_above_footer(self):
        for slide in H.slides():
            self.assertGreater(len(slide.notes), 100)
            self.assertTrue(any(url in slide.notes for url in ("https://", "http://")))
            for element in slide.els:
                if hasattr(element, "paras"):
                    self.assertLessEqual(element.y + element.h, 995, slide.title)

    def test_bense_explains_uncertainty_without_using_it_as_a_beauty_score(self):
        text = slide_text(H.slides()[1])
        for phrase in ('uncertainty', 'unpredictability', 'beautiful'):
            self.assertIn(phrase, text)
        self.assertNotIn('ENTROPY ≠ BEAUTY', text)

    def test_nake_essay_has_visible_author_date_and_clickable_reading(self):
        slide = H.slides()[4]
        self.assertIn('FRIEDER NAKE', slide_text(slide))
        self.assertIn('1971', slide_text(slide))
        links = [r.url for e in slide.els if hasattr(e, 'paras') for p in e.paras for r in p.runs]
        self.assertIn('https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/', links)

    def test_new_slides_do_not_create_classpoint_activities(self):
        for slide in H.slides():
            self.assertFalse(slide.cp)


if __name__ == "__main__":
    unittest.main()
