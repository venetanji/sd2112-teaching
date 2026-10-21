"""Require real HTML/PDF/PPTX/previews for every selected deck, never a stale week."""
import json
from pathlib import Path
import re
import sys
import zipfile

for name in json.loads(Path(sys.argv[1]).read_text()):
    folder = Path('_site') / name
    html = folder / 'index.html'
    assert html.is_file() and html.stat().st_size, f'{name}: missing HTML'
    count = len(re.findall(r'<section\b', html.read_text()))
    assert count > 0, f'{name}: no HTML slides'
    pdfs = list(folder.glob('*.pdf'))
    assert pdfs and all(p.stat().st_size > 0 for p in pdfs), f'{name}: missing PDF'
    for suffix in ('', '-classpoint'):
        path = Path('export') / f'{name}{suffix}.pptx'
        with zipfile.ZipFile(path) as archive:
            slides = [p for p in archive.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', p)]
            assert len(slides) == count, f'{path}: {len(slides)} slides != HTML {count}'
    assert list(Path('export/preview').glob(f'{name}-sheet-*.jpg')), f'{name}: missing previews'
    print(f'{name}: HTML/PDF/plain and ClassPoint PPTX/previews present; {count} slides')
