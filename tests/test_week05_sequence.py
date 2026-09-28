import unittest
import xml.etree.ElementTree as ET

from deck.week05 import S
from deck import week05_figures as F


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
            "A prompt guides an iterative image-generation pipeline.",
            "A VAE moves between pixels and a compact latent.",
            "Generation reverses the gradual noising process.",
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
            "A prompt guides an iterative image-generation pipeline.",
            "A VAE moves between pixels and a compact latent.",
            "Generation reverses the gradual noising process.",
            "The agent can look, make, and look again.",
        )
        for title in titles:
            slide = next((slide for slide in S if title in slide_text(slide)), None)
            self.assertIsNotNone(slide, title)
            self.assertTrue(any(type(element).__name__ == "Figure" for element in slide.els), title)

    def test_expanded_generation_theory_has_diagrams_before_the_agent_bridge(self):
        titles = (
            "A prompt guides an iterative image-generation pipeline.",
            "A VAE moves between pixels and a compact latent.",
            "Generation reverses the gradual noising process.",
            "The agent can look, make, and look again.",
        )
        slides = [slide_text(slide) for slide in S]
        positions = []
        for title in titles:
            index = next((i for i, text in enumerate(slides) if title in text), None)
            self.assertIsNotNone(index, title)
            self.assertTrue(
                any(type(element).__name__ == "Figure" for element in S[index].els),
                title,
            )
            positions.append(index)
        self.assertEqual(positions, sorted(positions))

    def test_vae_uses_a_tapered_encoder_and_decoder_with_a_sampled_distribution(self):
        svg, _ = F.vae_latent()
        root = ET.fromstring(svg)
        polygons = root.findall(".//{http://www.w3.org/2000/svg}polygon")
        tapered = 0
        for polygon in polygons:
            points = [
                tuple(map(float, point.split(",")))
                for point in polygon.attrib["points"].split()
            ]
            if len(points) == 4 and points[0][1] != points[1][1]:
                tapered += 1
        self.assertGreaterEqual(tapered, 2)
        for label in ("ENCODER", "mean", "log variance", "SAMPLE", ">z<", "DECODER"):
            self.assertIn(label, svg)

    def test_text_conditioning_diagram_connects_prompt_noise_to_generated_image(self):
        svg, _ = F.text_conditioning()
        for label in (
            "PROMPT",
            "TEXT ENCODER",
            "TEXT FEATURES",
            "DENOISING MODEL",
            "INITIAL LATENT",
            "VAE",
            "DECODER",
            "OUTPUT IMAGE",
        ):
            self.assertIn(label, svg)

    def test_existing_iteration_activity_remains_in_the_deck(self):
        text = "\n".join(slide_text(slide) for slide in S)
        self.assertIn("Change one thing. Compare. Decide.", text)
        self.assertIn("35 min", text)


if __name__ == "__main__":
    unittest.main()
