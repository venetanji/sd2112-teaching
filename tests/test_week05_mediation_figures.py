import unittest
import xml.etree.ElementTree as ET

from deck import week05_mediation_figures as M


class Week05MediationFiguresTests(unittest.TestCase):
    def test_equipment_and_later_enframing_remain_distinct(self):
        svg, _ = M.tool_encounter()
        for label in ("IN USE", "IN INSPECTION", "Ready-to-hand",
                      "Present-at-hand", "LATER: ENFRAMING"):
            self.assertIn(label, svg)

    def test_ihde_diagram_shows_relations_not_a_data_pipeline(self):
        svg, _ = M.mediation_relations()
        for label in ("HUMAN", "TECHNOLOGY", "WORLD", "EMBODIMENT",
                      "HERMENEUTIC", "ALTERITY", "BACKGROUND"):
            self.assertIn(label, svg)
        ET.fromstring(svg)

    def test_rule_example_draws_exactly_two_circles(self):
        svg, _ = M.two_circle_rules()
        root = ET.fromstring(svg)
        circles = root.findall(".//{http://www.w3.org/2000/svg}circle")
        self.assertEqual(len(circles), 2)
        self.assertEqual([float(circle.attrib["r"]) for circle in circles], [75, 125])

    def test_new_slide_text_stays_above_the_course_footer(self):
        from deck.week05 import DECK
        for slide in DECK['slides'][2:7]:
            for element in slide.els:
                if hasattr(element, 'paras') and element.y < 1000:
                    self.assertLessEqual(element.y + element.h, 1000, slide.title)


if __name__ == "__main__":
    unittest.main()
