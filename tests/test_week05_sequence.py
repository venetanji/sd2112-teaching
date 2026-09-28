import unittest

from deck.week05 import S


def slide_text(slide):
    return " ".join(
        run.text
        for element in slide.els
        if hasattr(element, "paras")
        for paragraph in element.paras
        for run in paragraph.runs
    )


class Week05SequenceTests(unittest.TestCase):
    def test_model_to_agent_story_precedes_the_existing_workshop(self):
        titles = [
            "GANs learn a visual distribution—not a description.",
            "CLIP brings words and images into a shared space.",
            "Diffusion turns conditioned noise into an image.",
            "The agent can look, make, and look again.",
            "Ask an agent to help sharpen your prompt.",
        ]
        slides = [slide_text(slide) for slide in S]
        for title in titles:
            self.assertTrue(any(title in text for text in slides), title)
        positions = [next(i for i, text in enumerate(slides) if title in text) for title in titles]
        self.assertEqual(positions, sorted(positions))

    def test_each_technical_bridge_slide_has_a_figure(self):
        titles = (
            "GANs · TWO MODELS IN COMPETITION",
            "CLIP brings words and images into a shared space.",
            "Diffusion turns conditioned noise into an image.",
            "The agent can look, make, and look again.",
        )
        for title in titles:
            slide = next((slide for slide in S if title in slide_text(slide)), None)
            self.assertIsNotNone(slide, title)
            self.assertTrue(any(type(element).__name__ == "Figure" for element in slide.els), title)

    def test_existing_iteration_activity_remains_in_the_deck(self):
        text = "\n".join(slide_text(slide) for slide in S)
        self.assertIn("Change one thing. Compare. Decide.", text)
        self.assertIn("35 min", text)


if __name__ == "__main__":
    unittest.main()
