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
    def test_model_to_agent_story_precedes_the_three_route_workshop(self):
        titles = [
            "GANs learn a visual distribution—not a description.",
            "CLIP brings words and images into a shared space.",
            "A prompt guides an iterative image-generation pipeline.",
            "A VAE moves between pixels and a compact latent.",
            "Training teaches a denoiser to remove noise.",
            "Generation turns new noise into an image.",
            "The agent can look, make, and look again.",
            "One identity. Three ways of making it.",
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
            "Training teaches a denoiser to remove noise.",
            "Generation turns new noise into an image.",
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
            "Training teaches a denoiser to remove noise.",
            "Generation turns new noise into an image.",
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

    def test_three_route_activity_replaces_old_separate_exercises(self):
        text = "\n".join(slide_text(slide) for slide in S)
        for label in ("One identity. Three ways of making it.", "40 min",
                      "Code the mark.", "Generate an interpretation.",
                      "Keep the form. Borrow the surface."):
            self.assertIn(label, text)
        self.assertNotIn("35 min", text)
        self.assertNotIn("Ask an agent to help sharpen your prompt.", text)

    def test_showcase_lecture_break_setup_and_workshop_are_in_order(self):
        slides = [slide_text(slide) for slide in S]
        titles = ("One mark. Three routes.", "How did words begin to guide image generation?",
                  "After the break: make it yours.", "Install. Open. Check.",
                  "Make a mark that represents you.", "One identity. Three ways of making it.")
        positions = [next(i for i, text in enumerate(slides) if title in text) for title in titles]
        self.assertEqual(positions, sorted(positions))

    def test_workshop_timing_and_machine_roles_are_explicit(self):
        slides = [slide_text(slide) for slide in S]
        for title, duration in (("Code the mark.", "10 min"),
                                ("Generate an interpretation.", "10 min"),
                                ("Keep the form. Borrow the surface.", "15 min")):
            self.assertTrue(any(title in text and duration in text for text in slides), title)
        text = " ".join(slides)
        self.assertIn("COMPARE · 5 MIN", text)
        self.assertIn("Machine B writes the code; Machine A executes it.", text)
        self.assertIn("Three.js is optional", text)
        self.assertIn("not a generated 3D model", " ".join(slide.notes for slide in S))

    def test_lesson_plan_protects_making_time_after_setup(self):
        from pathlib import Path
        plan = Path(__file__).resolve().parents[1].joinpath("lessons/week05-lesson-plan.md").read_text()
        for label in ("10 + 10 + 15 + 5 = 40", "Start the 40-minute clock only after",
                      "0:00–0:05", "0:05–1:00", "1:00–1:10", "1:10–1:25",
                      "1:25–2:05", "Three.js is optional"):
            self.assertIn(label, plan)

    def test_deep_question_bridges_theory_and_student_decisions(self):
        slides = [slide_text(slide) for slide in S]
        question = "If CLIP can match the words 'a chair' to a picture, why can't CLIP draw that chair?"
        index = next(i for i, text in enumerate(slides) if question in text)
        self.assertLess(
            next(i for i, text in enumerate(slides) if "Generation turns new noise into an image." in text),
            index,
        )
        self.assertLess(
            index,
            next(i for i, text in enumerate(slides) if "The agent can look, make, and look again." in text),
        )

    def test_logo_case_shows_original_and_exploratory_variant(self):
        slide = next(slide for slide in S if "What changed when we remade our course mark?" in slide_text(slide))
        images = [element for element in slide.els if type(element).__name__ == "Image"]
        self.assertEqual(len(images), 2)
        self.assertTrue(all(__import__("pathlib").Path(image.src).is_file() for image in images))

    def test_generated_lantern_is_a_concrete_example_after_the_pipeline(self):
        slides = [slide_text(slide) for slide in S]
        index = next(i for i, text in enumerate(slides) if "The model gives you a candidate—not a decision." in text)
        images = [element for element in S[index].els if type(element).__name__ == "Image" and "week05-lantern" in element.src]
        self.assertEqual(len(images), 1)
        self.assertIn("week05-lantern-easel.jpg", images[0].src)
        self.assertIn("A prompt guides an iterative image-generation pipeline.", slides[index - 1])

    def test_latent_process_distinguishes_training_and_generation(self):
        vae = F.vae_latent()[0]
        training = F.diffusion_training()[0]
        generation = F.diffusion_generation()[0]
        self.assertIn("DISTRIBUTION", vae)
        for label in ("VAE ENCODER", "CLEAN LATENT", "ADD NOISE", "NOISY LATENT", "DENOISER"):
            self.assertIn(label, training)
        for label in ("NEW NOISY LATENT", "DENOISER", "FINAL LATENT", "VAE DECODER", "OUTPUT IMAGE"):
            self.assertIn(label, generation)
        self.assertNotIn("EXAMPLE IMAGE", generation)
        self.assertIn("reconstruction illustrates VAE training", " ".join(slide_text(slide) for slide in S))

    def test_clip_and_evidence_question_are_visible(self):
        self.assertIn("mismatched pairs", F.clip_shared_space()[0])
        self.assertIn("What would require evidence?", " ".join(slide_text(slide) for slide in S))

    def test_training_shows_prediction_comparison_and_weight_update(self):
        svg, _ = F.diffusion_training()
        for label in ("PREDICT NOISE", "COMPARE", "KNOWN NOISE", "UPDATE WEIGHTS", "NOISY LATENT  zt"):
            self.assertIn(label, svg)

    def test_generation_has_repeated_updates_before_decoding(self):
        svg, _ = F.diffusion_generation()
        self.assertIn("REPEAT LATENT UPDATE", svg)
        self.assertIn("FINAL LATENT", svg)
        self.assertNotIn("only the VAE decoder makes pixels", svg)

    def test_demo_separates_media_generation_from_html_authoring(self):
        text = " ".join(slide_text(slide) for slide in S)
        for label in ("Easel Client", "HTML", "flow matching", "Machine B writes the code"):
            self.assertIn(label, text)
        notes = " ".join(slide.notes for slide in S)
        self.assertIn("https://github.com/venetanji/easel-client", notes)

    def test_video_case_is_a_discussion_not_an_invented_success_trace(self):
        slide = next(slide for slide in S if "What stayed wrong after a better prompt?" in slide_text(slide))
        self.assertIn("Gio", slide.notes)
        self.assertIn("chat", slide.notes)
        self.assertIn("not", slide.notes)

    def test_lesson_plan_classpoint_mapping_matches_deck(self):
        from pathlib import Path
        plan = Path(__file__).resolve().parents[1].joinpath("lessons/week05-lesson-plan.md").read_text()
        for i, slide in enumerate(S, 1):
            if slide.cp:
                self.assertIn(f"| {i} | Short answer |", plan)
                self.assertIn(slide.title, plan)

    def test_workshop_alignment_preserves_the_syllabus_challenge(self):
        from pathlib import Path
        syllabus = Path(__file__).resolve().parents[1].joinpath("syllabus/SD2112-syllabus-2026.md").read_text()
        self.assertIn("40-minute identity workshop", syllabus)
        self.assertIn("**Challenge 4:** a layout you could not design, generated, iterated and critiqued.", syllabus)


if __name__ == "__main__":
    unittest.main()
