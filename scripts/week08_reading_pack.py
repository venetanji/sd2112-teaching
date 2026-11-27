"""Collect Week 8 papers for local reading; keep full PDFs out of the public site."""
import argparse
import html
from pathlib import Path
import re
import sys
from urllib.parse import urljoin
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deck'))
from week08_studies import STUDY_GUIDES, EXTENSION_GUIDES

# Versions and download routes recorded in the existing full-text evidence audits.
PAPERS = {
    'R1': ('When ELIZA meets therapists: A Turing test for the heart and mind',
           'https://doi.org/10.1371/journal.pmen.0000145',
           'https://journals.plos.org/mentalhealth/article/file?id=10.1371/journal.pmen.0000145&type=printable',
           'journal.pmen.0000145.pdf'),
    'R2': ('Revealing the source: How awareness alters perceptions of AI and human-generated mental health responses',
           'https://doi.org/10.1016/j.invent.2024.100745',
           'https://pmc.ncbi.nlm.nih.gov/articles/PMC11090870/', 'PMC11090870.pdf'),
    'R3': ('Towards Understanding Sycophancy in Language Models (arXiv v4)',
           'https://arxiv.org/abs/2310.13548v4', 'https://arxiv.org/pdf/2310.13548v4', '2310.13548v4.pdf'),
    'R4': ('Sycophantic AI decreases prosocial intentions and promotes dependence',
           'https://doi.org/10.1126/science.aec8352',
           'https://s3.amazonaws.com/media.mediapost.com/uploads/science.aec8352.pdf', 'science.aec8352.pdf'),
    'R5': ('Thinking-Fast, Slow, and Artificial (January 11 v1; working paper)',
           'https://doi.org/10.31234/osf.io/yk25n_v1', 'https://osf.io/download/9gxaq/', 'yk25n-v1.pdf'),
    'R6': ('AI companions reduce loneliness (final five-study article)',
           'https://doi.org/10.1093/jcr/ucaf040',
           'https://www.hbs.edu/ris/Publication%20Files/AI%20Companions%20Reduce%20Loneliness%2011.7.2025_57451c02-8047-4e0d-abfc-55841f64166d.pdf',
           'ucaf040.pdf'),
    'R7': ('Harnessing artificial intelligence to facilitate difficult conversations (accepted manuscript)',
           'https://doi.org/10.1177/19485506261444068',
           'https://www.dropbox.com/scl/fi/z0khdhugidncm3vca0hql/Maheshka-et-al..pdf?rlkey=l7y1pr20t8ays7solhsmplidd&dl=1',
           'Maheshka-et-al..pdf'),
    'R8': ('People choose to receive human empathy despite rating AI empathy higher',
           'https://doi.org/10.1038/s44271-025-00387-3',
           'https://michael-inzlicht.squarespace.com/s/People-choose-to-receive-human-empathy.pdf', 's44271-025-00387-3.pdf'),
    'R9': ('Randomized trial of a generative AI chatbot for mental health treatment',
           'https://doi.org/10.1056/AIoa2400802', 'https://gwern.net/doc/psychiatry/depression/2025-heinz.pdf', '2025-heinz.pdf'),
    'R10': ("Understanding U.S. Users' Security and Privacy Transparency Needs for Consumer-Facing Generative AI",
            'https://www.usenix.org/conference/soups2026/presentation/cao',
            'https://www.usenix.org/system/files/soups2026-cao.pdf', 'soups2026-cao.pdf'),
    'R11': ('Interaction Techniques that Encourage Longer Prompts Can Improve Psychological Ownership when Writing with AI (v3)',
            'https://doi.org/10.1145/3831423.3831427', 'https://arxiv.org/pdf/2507.03670v3', '2507.03670v3.pdf'),
    'R12': ('Analyzing the integration of generative AI in the design process through the double-diamond framework',
            'https://doi.org/10.1017/S0890060426100304',
            'https://www.cambridge.org/core/journals/ai-edam/article/analyzing-the-integration-of-generative-ai-in-the-design-process-through-the-doublediamond-framework/F527231A155A48F597CD28E2B1F3B2F0',
            'S0890060426100304.pdf'),
    'R13': ('Exploring cognitive presence patterns in GenAI-integrated six-hat thinking technique scaffolded discussion: an epistemic network analysis',
            'https://doi.org/10.1186/s41239-025-00545-x',
            'https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-025-00545-x.pdf', 's41239-025-00545-x.pdf'),
}
GUIDES = dict(STUDY_GUIDES, **EXTENSION_GUIDES)
EXTRAS = {
    'R1-correction': ('R1 funding and competing-interest correction',
                      'https://journals.plos.org/mentalhealth/article/file?id=10.1371/journal.pmen.0000426&type=printable'),
    'Verbeek-2015': ('Beyond interaction: A short introduction to mediation theory',
                     'https://ris.utwente.nl/ws/portalfiles/portal/6973415/p26-verbeek.pdf'),
}


def retrieve_pdf(url):
    with urlopen(Request(url, headers={'User-Agent': 'SD2112-reading-pack/1.0'}), timeout=25) as response:
        data, final_url = response.read(), response.url
    if data.startswith(b'%PDF-'):
        return data
    # Publisher landing pages may advertise an ordinary, publicly accessible PDF.
    page = data.decode('utf-8', errors='replace')
    tags = re.findall(r'<meta\b[^>]*>', page, re.I)
    for tag in tags:
        if re.search(r'name=[\"\']citation_pdf_url[\"\']', tag, re.I):
            match = re.search(r'content=[\"\']([^\"\']+)', tag, re.I)
            if match:
                return retrieve_direct(urljoin(final_url, html.unescape(match[1])))
    if 'pmc.ncbi.nlm.nih.gov' in final_url:
        match = re.search(r'href=[\"\']([^\"\']*pdf/[^\"\']+\.pdf)[\"\']', page, re.I)
        if match:
            return retrieve_direct(urljoin(final_url, html.unescape(match[1])))
    raise ValueError('The public route returned a page rather than a PDF')


def retrieve_direct(url):
    with urlopen(Request(url, headers={'User-Agent': 'SD2112-reading-pack/1.0'}), timeout=25) as response:
        data = response.read()
    if not data.startswith(b'%PDF-'):
        raise ValueError('Download is not a PDF')
    return data


def recap_markdown():
    lines = ['# Week 8: the papers in plain language', '',
             'Read the example first, then ask what was measured. Examples are teaching adaptations, '
             'not verbatim study prompts. R1-R8 form the main discussion; R9-R13 are optional or later readings.', '']
    for key, (title, source, download, _) in PAPERS.items():
        guide = GUIDES[key]
        lines += [f'## {key}: {title}', '', f'**Imagine the study:** {guide["example"]}', '',
                  f'**What they did:** {guide["task"]}', '',
                  f'**What they measured:** {guide["measured"]}', '',
                  f'**What they found:** {guide["result"]}', '',
                  f'**Keep in mind:** {guide["limit"]}', '',
                  f'[Paper / publication record]({source}) | [Full-text route]({download})', '']
    lines += ['## R1 correction and mediation reading', '']
    for title, url in EXTRAS.values():
        lines += [f'- [{title}]({url})']
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--offline', action='store_true', help='Collect existing PDFs only')
    parser.add_argument('--from-dir', action='append', type=Path, default=[])
    parser.add_argument('--output', type=Path, default=ROOT / 'export' / 'week08-reading')
    parser.add_argument('--write-recaps', action='store_true', help='Refresh the published recap source')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    recap = recap_markdown()
    if args.write_recaps:
        (ROOT / 'lessons' / 'week08-paper-recaps.md').write_text(recap, encoding='utf-8')
    (args.output / 'RECAPS.md').write_text(recap, encoding='utf-8')
    status, missing = ['# Week 8 local reading pack', '',
                       'Open RECAPS.md for an example, finding and limitation for every paper.', ''], 0
    entries = [(key, row[0], row[2], row[3]) for key, row in PAPERS.items()]
    entries += [(key, title, url, key + '.pdf') for key, (title, url) in EXTRAS.items()]
    for key, title, url, original_name in entries:
        path = args.output / (key + '.pdf')
        error = 'Not available locally; download with network access or use the source link'
        if not path.exists():
            for folder in args.from_dir:
                candidate = folder / original_name
                if candidate.is_file() and candidate.read_bytes().startswith(b'%PDF-'):
                    path.write_bytes(candidate.read_bytes())
                    break
        if not path.exists() and not args.offline:
            try:
                path.write_bytes(retrieve_pdf(url))
            except (OSError, ValueError) as exc:
                error = str(exc)
        available = path.is_file() and path.read_bytes().startswith(b'%PDF-')
        state = f'[Open local PDF]({path.name})' if available else f'PENDING: {error}'
        provenance = args.output / (key + '-provenance.txt')
        if available and provenance.is_file():
            state += f' ([copy details]({provenance.name}))'
        missing += not available
        status += [f'- **{key}: {title}** - {state}. [Source]({url})']
        print(f'{key}: {"available" if available else "pending"}')
    (args.output / 'README.md').write_text('\n'.join(status) + '\n', encoding='utf-8')
    import markdown
    (args.output / 'index.html').write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8"><title>Week 8 reading pack</title>'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<style>body{max-width:75ch;margin:40px auto;padding:0 20px;font:18px/1.6 Georgia,serif;'
        'color:#000b1c;background:#f6f7f5}a{color:#246e70}h2{margin-top:3em}</style><main>' +
        markdown.markdown('\n'.join(status)) + markdown.markdown(recap) + '</main></html>', encoding='utf-8')
    print(f'{len(entries) - missing}/{len(entries)} PDFs available in {args.output}')
    return 1 if missing else 0


if __name__ == '__main__':
    raise SystemExit(main())
