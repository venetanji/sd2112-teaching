"""
Build everything, the way the GitHub Actions workflows do:

    python tools/build_all.py            # site + PowerPoints
    python tools/build_all.py --site     # _site/ only: landing page, html decks, PDFs, syllabus (the Pages workflow)
    python tools/build_all.py --pptx     # export/ only: PowerPoints, ClassPoint manifest, docx, previews (the PowerPoint workflow)
    python tools/build_all.py --no-pdf   # skip the Chromium PDF step (no node/playwright on this machine)
    python tools/build_all.py --snap     # also redo the snapshots of the live sketches (deck/assets/sketches, committed)

  _site/            the published site: landing page, vendor css/js/fonts, one folder per deck
                    (html deck + assets + the PDF without ClassPoint buttons), syllabus.html
  export/           week01.pptx, week01-classpoint.pptx, the ClassPoint manifest,
                    docs/*.docx (+ the lesson plans as html), preview contact sheets

Both folders are git-ignored. Every deck/weekNN.py is a deck.
"""
from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import deckgen        # noqa: E402
import build_docs     # noqa: E402

DECKS = sorted(p.stem for p in (ROOT / 'deck').glob('week[0-9][0-9].py'))   # every deck/weekNN.py


def load_deck(name):
    spec = importlib.util.spec_from_file_location(f'deck_{name}', ROOT / 'deck' / f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    explicit = {'--site', '--pptx'} & set(argv)
    do_site = '--site' in explicit or not explicit
    do_pptx = '--pptx' in explicit or not explicit
    do_pdf = '--no-pdf' not in argv
    snap = '--snap' in argv          # redo the sketch snapshots (deck/assets/sketches) before building
    if do_site:
        site = deckgen.SITE
        if site.exists():
            shutil.rmtree(site)
        shutil.copytree(ROOT / 'site', site)      # index.html + vendor/ (reveal.js, design tokens)
        (site / '.nojekyll').touch()
    problems = []
    for name in DECKS:
        mod = load_deck(name)
        out = deckgen.build_all(mod.DECK, name, mod.FOOTER, do_pptx=do_pptx, do_html=do_site, do_png=True, do_pdf=do_site and do_pdf, snap=snap)
        n = len(mod.DECK['slides'])
        cp = sum(1 for s in mod.DECK['slides'] if s.cp)
        made = [str(out[k].relative_to(ROOT)) for k in ('html', 'pdf', 'classpoint') if k in out]
        print(f'{name}: {n} slides, {cp} ClassPoint activities -> ' + ', '.join(made))
        for w in out.get('warnings') or []:
            problems.append(f'{name}: {w}')
    build_docs.main(site=do_site, export=do_pptx)
    for p in problems:
        print('WARNING', p)
    if do_site:
        site = deckgen.SITE
        total = sum(f.stat().st_size for f in site.rglob('*') if f.is_file())
        print(f'_site: {sum(1 for f in site.rglob("*") if f.is_file())} files, {total / 1e6:.1f} MB')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
