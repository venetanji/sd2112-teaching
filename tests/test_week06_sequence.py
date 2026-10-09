"""Regressions for the approved theory-first, one-result sound workshop."""
import importlib.util
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
DEMO = "Make and export a demo you can explain."
REFERENCE = "Transform your demo\u2014not an unrelated prompt."
REVISE = "What did the reference actually change?"
SAVE = "Check the final result\u2014not just the preview."
COLLECT = "Submit your final playable result."
QUESTIONS = (
    "What made this sound yours: the demo, the prompt, or the listening decision?",
    "Which choice would you reclaim from the model\u2014and why does it matter to your listener?",
)


def slide_text(slide):
    return " ".join(
        run.text
        for element in slide.els
        if hasattr(element, "paras")
        for paragraph in element.paras
        for run in paragraph.runs
    )


def slide_links(slide):
    return [
        run.url
        for element in slide.els
        if hasattr(element, "paras")
        for paragraph in element.paras
        for run in paragraph.runs
        if run.url
    ]


class Week06SequenceTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(
            importlib.util.find_spec("deck.week06"),
            "The approved Week 6 deck has not been implemented yet.",
        )
        from deck.week06 import S
        self.slides = S

    def slide(self, title):
        matches = [slide for slide in self.slides if slide.title == title]
        self.assertEqual(len(matches), 1, title)
        return matches[0]

    def titled_text(self, title, notes=False):
        slide = self.slide(title)
        return slide_text(slide) + (" " + slide.notes if notes else "")

    def test_approved_sequence_has_50_slides(self):
        self.assertEqual(len(self.slides), 50)

    def test_only_two_deep_short_answers_use_classpoint(self):
        activities = [(i, slide.cp) for i, slide in enumerate(self.slides, 1) if slide.cp]
        self.assertEqual([i for i, _ in activities], [45, 46])
        self.assertEqual(tuple(self.slides[i - 1].title for i, _ in activities), QUESTIONS)
        for number, activity in activities:
            self.assertEqual(activity["type"], "short_answer", number)
            self.assertFalse(activity.get("caption_required", False), number)
            self.assertIn("reflection", self.slides[number - 1].notes.lower())
            self.assertIn("evidence", self.slides[number - 1].notes.lower())

    def test_theory_break_demo_setup_brief_then_making_are_in_order(self):
        # Positions here are the explicitly approved chapter/order contract.
        for number, title in (
            (3, "A sound changes\nwhat you notice\nand what you do."),
            (13, "MIDI describes events. It contains no sound."),
            (14, "Compose the procedure."), (20, "Fixed rules. Variable outcomes."),
            (21, "Generate from patterns."), (28, "Permission is not a copyright guarantee."),
            (29, "Coordinate both machines."),
            (31, "Keep an intention. Let the arrangement change."),
            (32, "Break.\nTen minutes."), (33, "Your demo.\nA new arrangement."),
            (34, "Play \u2192 export \u2192 reference \u2192 listen."),
            (35, "Choose a demo tool. Check the reference route."),
            (36, "Make a sound for one identity and moment."),
            (37, "Be precise about intent. Honest about control."),
            (38, "Demo \u2192 exported reference \u2192 transformation \u2192 save."),
            (39, DEMO), (40, REFERENCE), (41, REVISE), (42, SAVE), (43, COLLECT),
            (44, "A result is not the whole creative process."),
            (47, "Explain the difference before choosing an answer."),
            (48, "Thirty seconds of sound."),
            (49, "Turn listening into an evidence-led argument."),
            (50, "Rules. Patterns.\nYour listening."),
        ):
            with self.subTest(slide=number):
                self.assertEqual(self.slides[number - 1].title, title)
        self.assertTrue(all(slide.cp is None for slide in self.slides[:44]))

    def test_workshop_protects_15_15_5_5_minutes(self):
        for title, minutes in ((DEMO, 15), (REFERENCE, 15), (REVISE, 5), (SAVE, 5)):
            with self.subTest(title=title):
                self.assertRegex(self.titled_text(title).lower(), rf"\b{minutes}\s*min")
        overview = self.titled_text(
            "Demo \u2192 exported reference \u2192 transformation \u2192 save.", notes=True)
        self.assertRegex(overview.lower(), r"40\s*min")
        self.assertIn("15 + 15 + 5 + 5 = 40", overview)

    def test_setup_has_a_clickable_easel_release_link(self):
        setup = self.slide("Choose a demo tool. Check the reference route.")
        self.assertIn(
            "https://github.com/venetanji/easel-client/releases",
            slide_links(setup),
        )
        self.assertNotIn("v0.0.4", slide_text(setup))
        self.assertRegex(setup.notes.lower(), r"pre.class|before class")
        self.assertIn("Gio", setup.notes)
        self.assertRegex(setup.notes.lower(), r"verif|test")

    def test_only_the_final_playable_result_is_collected(self):
        result_slide = self.slide(COLLECT)
        result = slide_text(result_slide).lower()
        self.assertRegex(result, r"one|single")
        self.assertRegex(result, r"playable|listen")
        self.assertIn("canvas", result)
        self.assertRegex(result, r"file|link")
        self.assertIsNone(result_slide.cp)
        self.assertEqual(sum("one final submission" in slide_text(s).lower()
                             for s in self.slides), 1)
        for title in (DEMO, REFERENCE, REVISE):
            self.assertIsNone(self.slide(title).cp)
        self.assertIn("no compulsory intermediate submission", self.titled_text(DEMO).lower())
        for title in (REFERENCE, REVISE):
            self.assertNotRegex(self.titled_text(title).lower(), r"\bsubmit\b|\bsubmission\b")
        self.assertIn("not separate demo, generation and comparison uploads", result)
        self.assertNotRegex(result, r"classpoint.*audio upload|audio upload.*classpoint")

    def test_hybrid_transforms_actual_demo_audio_then_compares_and_revises(self):
        demo = self.titled_text(DEMO).lower()
        for phrase in ("strudel", "garageband", "another", "export", "audio file", "replay"):
            self.assertIn(phrase, demo)
        reference = self.titled_text(REFERENCE).lower()
        for phrase in ("easel", "exported audio", "suno reference input", "completed output", "save", "do not duplicate"):
            self.assertIn(phrase, reference)
        revision = self.titled_text(REVISE).lower()
        for phrase in ("original demo", "completed transformation", "preserved", "changed", "edit or revision", "motif", "up to 30 seconds"):
            self.assertIn(phrase, revision)
        self.assertIn("no compulsory a/b spliced timeline", revision)
        self.assertNotRegex(revision, r"automatic beat.match|auto.beat.match")
        self.assertIn("not a fixed intro/excerpt/outro recipe", self.slide(REVISE).notes.lower())
        self.assertIn("not a midi file or screenshot", demo)
        save = self.titled_text(SAVE).lower()
        for phrase in ("reopen", "plays with sound", "one final result"):
            self.assertIn(phrase, save)

    def test_mock_quiz_is_three_practice_prompts_not_more_classpoint(self):
        quiz = self.slide("Explain the difference before choosing an answer.")
        self.assertIsNone(quiz.cp)
        self.assertRegex(slide_text(quiz).lower(), r"practice|mock")
        self.assertRegex(quiz.notes.lower(), r"answer")
        for number in (1, 2, 3):
            self.assertRegex(slide_text(quiz), rf"\b{number}[.)\s]")

    def test_challenge_and_reflection_preserve_canvas_and_existing_assessment(self):
        challenge = self.titled_text("Thirty seconds of sound.").lower()
        self.assertRegex(challenge, r"up to\s*30|\b30\s*(?:s|sec)")
        self.assertIn("canvas", challenge)
        reflection = self.titled_text("Turn listening into an evidence-led argument.", notes=True).lower()
        for phrase in ("1000", "own", "images", "canvas", "week 7", "20%", "unchanged rubric"):
            self.assertIn(phrase, reflection)
        self.assertRegex(reflection, r"three|\b3\b")
        self.assertRegex(reflection, r"weeks?\s*2\s*[-\u2013]\s*6")
        self.assertRegex(reflection, r"ai.writing|ai.*writ|writ.*ai")
        self.assertNotIn("blackboard", " ".join(slide_text(s) for s in self.slides).lower())

    def test_sources_do_not_invent_student_work_or_required_intermediate_captures(self):
        text = " ".join(slide_text(s) + " " + s.notes for s in self.slides).lower()
        self.assertNotRegex(text, r"student (?:said|wrote|submitted)|winning student|best student entries")
        self.assertNotRegex(text, r"caption required|capture [123]|eight mock")

    def test_course_footer_and_elements_stay_on_the_slide(self):
        for number, slide in enumerate(self.slides, 1):
            with self.subTest(slide=number):
                self.assertIn("SD2112", slide_text(slide))
                self.assertIn("WEEK 06", slide_text(slide))
                self.assertRegex(slide.bg, r"^#[0-9A-Fa-f]{6}$")
                for element in slide.els:
                    self.assertGreaterEqual(element.x, 0)
                    self.assertGreaterEqual(element.y, 0)
                    self.assertLessEqual(element.x + element.w, 1920)
                    self.assertLessEqual(element.y + element.h, 1080)

    def test_site_links_to_week06_slides_and_pdf(self):
        site = (ROOT / "site/index.html").read_text()
        self.assertIn('href="week06/"', site)
        self.assertIn('href="week06/SD2112-week06.pdf"', site)

    def test_lesson_plan_quotes_the_actual_classpoint_questions(self):
        plan = (ROOT / "lessons/week06-lesson-plan.md").read_text()
        for slide in self.slides:
            if slide.cp:
                self.assertIn(slide.title, plan)

    def test_lesson_plan_preserves_timing_and_reference_contract(self):
        plan = (ROOT / "lessons/week06-lesson-plan.md").read_text().lower()
        for phrase in ("50 slides", "15 + 15 + 5 + 5 = 40", "slides 1-31",
                       "slides 3-13", "slides 14-20", "slides 21-28", "slides 29-31",
                       "export actual audio", "audio reference", "completed transformation",
                       "recognisable motif", "no compulsory timeline", "privately", "gio"):
            self.assertIn(phrase, plan)
        for time, slides in (("0:00-1:00", "1-31"), ("1:00-1:10", "32"),
                             ("1:10-1:20", "33-34"), ("1:20-1:35", "35-38"),
                             ("1:35-2:15", "39-43"), ("2:15-3:00", "44-50")):
            self.assertIn(f"| {time} | {slides} |", plan)
        self.assertNotRegex(plan, r"46.slide|10\s*\+\s*10\s*\+\s*15\s*\+\s*5")

    def test_lesson_plan_separates_provider_rights_and_instructor_testing(self):
        plan = (ROOT / "lessons/week06-lesson-plan.md").read_text().lower()
        for phrase in ("9 october 2026", "original uploads remain yours", "broad provider licence",
                       "basic", "non-commercial", "pro/premier", "approved download",
                       "not automatically", "copyright", "hong kong", "easel/provider contract",
                       "not a verified integration test", "exact input limits"):
            self.assertIn(phrase, plan)


class Week06ReportTests(unittest.TestCase):
    def load_with_reports(self, entries):
        from deckgen import attach_reports

        def attach(slides, source):
            self.assertEqual(source, ROOT / "deck/week06-reports.json")
            return attach_reports(slides, entries, quiet=True)

        with patch("deckgen.attach_reports", side_effect=attach) as mocked:
            deck = runpy.run_path(str(ROOT / "deck/week06.py"))
        mocked.assert_called_once()
        return deck["S"]

    def test_empty_reports_are_safe_before_class(self):
        slides = self.load_with_reports([])
        self.assertTrue(all(not getattr(slide, "report", None) for slide in slides))

    def test_report_links_attach_only_to_the_matching_question(self):
        from deck.week06 import S
        urls = ["https://example.invalid/week06-a", "https://example.invalid/week06-b"]
        entries = [{"activity": url, "question": S[number - 1].title}
                   for url, number in zip(urls, (45, 46))]
        slides = self.load_with_reports(entries)
        for number, url in zip((45, 46), urls):
            self.assertEqual(slides[number - 1].report, url)
            self.assertIn(url, slide_links(slides[number - 1]))
        for slide in slides:
            if not slide.cp:
                self.assertFalse(getattr(slide, "report", None))
                self.assertFalse(set(urls).intersection(slide_links(slide)))

    def test_withheld_reports_never_gain_a_link(self):
        slides = self.load_with_reports([
            {"activity": None, "withheld": "names hidden"},
            {"activity": None, "withheld": "not run in class"},
        ])
        for number in (45, 46):
            self.assertFalse(getattr(slides[number - 1], "report", None))
            self.assertEqual(slide_links(slides[number - 1]), [])

    def test_null_report_does_not_shift_the_next_matching_link(self):
        url = "https://example.invalid/week06-b"
        slides = self.load_with_reports([
            {"activity": None, "question": QUESTIONS[0]},
            {"activity": url, "question": QUESTIONS[1]},
        ])
        self.assertFalse(getattr(slides[44], "report", None))
        self.assertEqual(slide_links(slides[44]), [])
        self.assertEqual(slides[45].report, url)
        self.assertIn(url, slide_links(slides[45]))

    def test_report_count_and_question_drift_fail_the_deck_import(self):
        for entries in (
            [{"activity": None}],
            [{"activity": None}] * 3,
            [{"activity": None, "question": "A mismatched question"},
             {"activity": None}],
            [{"activity": None, "question": QUESTIONS[0]},
             {"activity": None, "question": "A mismatched question"}],
        ):
            with self.subTest(entries=entries), self.assertRaises(ValueError):
                self.load_with_reports(entries)


if __name__ == "__main__":
    unittest.main()
