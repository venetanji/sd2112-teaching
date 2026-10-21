from pathlib import Path
import unittest


class PublicationRunnerTests(unittest.TestCase):
    def test_pdf_job_uses_a_runner_supported_by_pinned_playwright(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / '.github/workflows/site.yml').read_text()
        pdf_job = workflow.split('  pdf:\n', 1)[1].split('  build:\n', 1)[0]
        self.assertIn('runs-on: ubuntu-24.04', pdf_job)
        self.assertNotIn('runs-on: ubuntu-latest', pdf_job)
        self.assertIn('playwright@1.56.1', pdf_job)


if __name__ == '__main__':
    unittest.main()
