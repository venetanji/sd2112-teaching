"""
Build everything, the way the GitHub Actions workflow does:

    python tools/build_all.py

  _site/            the published site: landing page, vendor css/js/fonts,
                    one folder per deck (html deck + assets + the ClassPoint pptx), syllabus
  export/           week01.pptx, week01-classpoint.pptx, the ClassPoint manifest,
                    docs/*.docx, preview contact sheets

Both folders are git-ignored. Add new decks to DECKS.
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

DECKS = ['week01']


def load_deck(name):
    spec = importlib.util.spec_from_file_location(f'deck_{name}', ROOT / 'deck' / f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    site = deckgen.SITE
    if site.exists():
        shutil.rmtree(site)
    shutil.copytree(ROOT / 'site', site)      # index.html + vendor/ (reveal.js, design tokens)
    (site / '.nojekyll').touch()
    problems = []
    for name in DECKS:
        mod = load_deck(name)
        out = deckgen.build_all(mod.DECK, name, mod.FOOTER)
        n = len(mod.DECK['slides'])
        cp = sum(1 for s in mod.DECK['slides'] if s.cp)
        print(f'{name}: {n} slides, {cp} ClassPoint activities -> {out["html"].relative_to(ROOT)}, {out["download"].relative_to(ROOT)}')
        for w in out.get('warnings') or []:
            problems.append(f'{name}: {w}')
    build_docs.main()
    for p in problems:
        print('WARNING', p)
    total = sum(f.stat().st_size for f in site.rglob('*') if f.is_file())
    print(f'_site: {sum(1 for f in site.rglob("*") if f.is_file())} files, {total / 1e6:.1f} MB')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
