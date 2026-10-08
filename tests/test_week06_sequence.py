"""Regressions for the approved theory-first, one-result sound workshop."""
import importlib.util
from pathlib import Path
import re
import runpy
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


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

    def text(self, number, notes=False):
        slide = self.slides[number - 1]
        return slide_text(slide) + (" " + slide.notes if notes else "")

    def test_approved_sequence_has_46_slides(self):
        self.assertEqual(len(self.slides), 46)

    def test_only_two_deep_short_answers_use_classpoint(self):
        activities = [(i, slide.cp) for i, slide in enumerate(self.slides, 1) if slide.cp]
        self.assertEqual([i for i, _ in activities], [18, 26])
        for number, activity in activities:
            self.assertEqual(activity["type"], "short_answer", number)
            self.assertFalse(activity.get("caption_required", False), number)
            self.assertIn("reflection", self.slides[number - 1].notes.lower())
            self.assertIn("evidence", self.slides[number - 1].notes.lower())

    def test_theory_break_demo_setup_brief_then_making_are_in_order(self):
        for number, pattern in (
            (30, r"break"), (32, r"easel"), (33, r"install|setup|open|check"),
            (34, r"brief|product|moment"), (36, r"40\s*min"),
            (37, r"rule|code|strudel"), (38, r"generat|learned|suno"),
            (39, r"A\s*\+\s*B|hybrid|combin|timeline"),
            (40, r"listen|review|save"),
        ):
            with self.subTest(slide=number):
                self.assertRegex(self.text(number).lower(), pattern.lower())
        self.assertTrue(all(slide.cp is None for slide in self.slides[29:41]))

    def test_workshop_protects_10_10_15_5_minutes(self):
        for number, minutes in ((37, 10), (38, 10), (39, 15), (40, 5)):
            with self.subTest(slide=number):
                self.assertRegex(self.text(number).lower(), rf"\b{minutes}\s*min")
        self.assertIn("40", self.text(36))

    def test_setup_has_a_clickable_easel_release_link(self):
        self.assertIn(
            "https://github.com/venetanji/easel-client/releases",
            slide_links(self.slides[32]),
        )
        self.assertNotIn("v0.0.4", self.text(33))
        self.assertRegex(self.text(33, notes=True).lower(), r"pre.class|before class")

    def test_only_the_final_playable_result_is_collected(self):
        result = self.text(41).lower()
        self.assertRegex(result, r"one|single")
        self.assertRegex(result, r"playable|listen")
        self.assertIn("canvas", result)
        self.assertRegex(result, r"file|link")
        self.assertIsNone(self.slides[40].cp)
        for number in (37, 38, 39):
            self.assertNotRegex(self.text(number).lower(), r"upload|submit")
        self.assertNotRegex(result, r"classpoint.*audio upload|audio upload.*classpoint")

    def test_hybrid_reuses_saved_audio_without_promising_generation_features(self):
        hybrid = self.text(39, notes=True).lower()
        for word in ("intro", "excerpt", "outro", "timeline"):
            self.assertIn(word, hybrid)
        self.assertRegex(hybrid, r"trim|fade|gain")
        self.assertNotRegex(self.text(39).lower(), r"automatic beat.match|auto.beat.match")

    def test_mock_quiz_is_three_practice_prompts_not_more_classpoint(self):
        quiz = self.slides[42]
        self.assertIsNone(quiz.cp)
        self.assertRegex(slide_text(quiz).lower(), r"practice|mock")
        self.assertRegex(quiz.notes.lower(), r"answer")
        for number in (1, 2, 3):
            self.assertRegex(slide_text(quiz), rf"\b{number}[.)\s]")

    def test_challenge_and_reflection_preserve_canvas_and_existing_assessment(self):
        challenge = self.text(44).lower()
        self.assertRegex(challenge, r"up to\s*30|\b30\s*(?:s|sec)")
        self.assertIn("canvas", challenge)
        reflection = self.text(45, notes=True).lower()
        for phrase in ("1000", "own", "images", "canvas", "week 7"):
            self.assertIn(phrase, reflection)
        self.assertRegex(reflection, r"three|\b3\b")
        self.assertRegex(reflection, r"weeks?\s*2\s*[-\u2013]\s*6")
        self.assertRegex(reflection, r"ai.writing|ai.*writ|writ.*ai")
        self.assertNotIn("blackboard", " ".join(self.text(i) for i in range(1, 47)).lower())

    def test_sources_do_not_invent_student_work_or_required_intermediate_captures(self):
        text = " ".join(self.text(i, notes=True) for i in range(1, 47)).lower()
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
        for number in (18, 26):
            questions = [
                " ".join(run.text for paragraph in element.paras
                         for run in paragraph.runs)
                for element in self.slides[number - 1].els
                if hasattr(element, "paras")
            ]
            question_text = next(text for text in questions if text.endswith("?"))
            self.assertIn(question_text, plan)


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
                   for url, number in zip(urls, (18, 26))]
        slides = self.load_with_reports(entries)
        for number, url in zip((18, 26), urls):
            self.assertEqual(slides[number - 1].report, url)
            self.assertIn(url, slide_links(slides[number - 1]))

    def test_withheld_reports_never_gain_a_link(self):
        slides = self.load_with_reports([
            {"activity": None, "withheld": "names hidden"},
            {"activity": None, "withheld": "not run in class"},
        ])
        for number in (18, 26):
            self.assertFalse(getattr(slides[number - 1], "report", None))
            self.assertEqual(slide_links(slides[number - 1]), [])

    def test_report_count_and_question_drift_fail_the_deck_import(self):
        for entries in (
            [{"activity": None}],
            [{"activity": None, "question": "A mismatched question"},
             {"activity": None}],
        ):
            with self.subTest(entries=entries), self.assertRaises(ValueError):
                self.load_with_reports(entries)


if __name__ == "__main__":
    unittest.main()
