"""Stage one download per built week, excluding other weeks and local reading packs."""
import argparse
import json
from pathlib import Path
import re
import shutil
import tomllib


def prepare(root, output, decks_file=None):
    root, output = Path(root).resolve(), Path(output).resolve()
    registered = tomllib.loads((root / 'deckgen.toml').read_text())['course']['decks']
    decks = json.loads(Path(decks_file).read_text()) if decks_file else registered
    if (not isinstance(decks, list) or not decks
            or any(not isinstance(d, str) or not re.fullmatch(r'week\d{2}', d) for d in decks)
            or len(set(decks)) != len(decks) or any(d not in registered for d in decks)):
        raise ValueError('Expected a nonempty list of unique registered weeks')

    contents = []
    for deck in decks:
        export = root / 'export'
        files = [(export / (deck + suffix), Path(deck + suffix))
                 for suffix in ('.pptx', '-classpoint.pptx', '-activities.json')]
        previews = sorted((export / 'preview').glob(f'{deck}-sheet-*.jpg'))
        if not previews:
            raise ValueError(f'{deck}: missing preview sheets')
        files += [(p, Path('preview') / p.name) for p in previews]
        for extension in ('docx', 'html'):
            files += [(p, Path('docs') / p.name)
                      for p in sorted((export / 'docs').glob(f'{deck}-*.{extension}'))]
        files += [(p, Path(p.name)) for p in sorted((root / '_site' / deck).glob('*.pdf'))]
        for source, _ in files:
            if not source.is_file() or source.stat().st_size == 0:
                raise ValueError(f'{deck}: missing or empty output {source.name}')
        contents.append((deck, files))

    # A fresh directory prevents stale files from entering a later run's download.
    output.mkdir(parents=True, exist_ok=False)
    packages = []
    for deck, files in contents:
        folder = output / deck
        staged = []
        for source, relative in files:
            target = folder / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            staged.append(str(target))
        packages.append(dict(deck=deck, root=str(folder), files=staged))
    (output / 'manifest.json').write_text(json.dumps(packages) + '\n')
    return packages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--decks-file', help='Optional JSON list from changed-week selection')
    args = parser.parse_args()
    packages = prepare(Path.cwd(), args.output, args.decks_file or None)
    print('Weekly downloads: ' + ', '.join(p['deck'] for p in packages))


if __name__ == '__main__':
    main()
