"""Reading downloads must not save challenge pages as PDFs or lose the paper map."""
import importlib.util
from io import BytesIO
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('reading_pack', ROOT / 'scripts/week08_reading_pack.py')
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class Response(BytesIO):
    url = 'https://example.org/article/'


class ReadingPackTests(unittest.TestCase):
    def test_challenge_page_is_not_saved_as_pdf(self):
        with patch.object(M, 'urlopen', return_value=Response(b'<html>Please log in</html>')):
            with self.assertRaisesRegex(ValueError, 'rather than a PDF'):
                M.retrieve_pdf('https://example.org/article/')

    def test_pdf_metadata_can_precede_the_name_attribute(self):
        page = b'<meta content="/paper.pdf?x=1&amp;y=2" name="citation_pdf_url">'
        with patch.object(M, 'urlopen', side_effect=[Response(page), Response(b'%PDF-1.7\n')]) as request:
            self.assertEqual(M.retrieve_pdf('https://example.org/article/'), b'%PDF-1.7\n')
            self.assertEqual(request.call_args_list[1].args[0].full_url, 'https://example.org/paper.pdf?x=1&y=2')

    def test_recaps_cover_every_paper_with_the_audited_example_and_limit(self):
        self.assertEqual(set(M.PAPERS), {f'R{i}' for i in range(1, 14)})
        recap = M.recap_markdown()
        for key, guide in M.GUIDES.items():
            self.assertIn(f'## {key}:', recap)
            self.assertIn(guide['example'], recap)
            self.assertIn(guide['limit'], recap)

    def test_homepage_links_the_deck_pdf_and_public_recaps(self):
        page = (ROOT / 'site/index.html').read_text(encoding='utf-8')
        for href in ('week08/', 'week08/SD2112-week08.pdf', 'week08-papers.html'):
            self.assertIn(f'href="{href}"', page)
        self.assertNotIn('WEEKS 08', page)
