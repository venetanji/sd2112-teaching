"""Fail on a lost weekly registration; print changed weeks for read-only PR builds."""
import argparse
import ast
import json
from pathlib import Path
import re
import subprocess
import tomllib


def registered(root):
    names = tomllib.loads((root / 'deckgen.toml').read_text())['course']['decks']
    if len(names) != len(set(names)):
        raise ValueError('Duplicate deck registration')
    if any(not re.fullmatch(r'[A-Za-z0-9_-]+', n) for n in names):
        raise ValueError('Invalid deck name')
    missing = [n for n in names if not (root / 'deck' / (n + '.py')).is_file()]
    unlisted = sorted(p.stem for p in (root / 'deck').glob('week[0-9][0-9].py') if p.stem not in names)
    if missing or unlisted:
        raise ValueError(f'Missing sources: {missing}; unregistered weekly sources: {unlisted}. Preserve the union when resolving branches.')
    return names


def dependencies(root, name, seen=None):
    seen = set() if seen is None else seen
    path = root / 'deck' / (name + '.py')
    if not path.is_file() or name in seen:
        return seen
    seen.add(name)
    for node in ast.walk(ast.parse(path.read_text())):
        modules = []
        if isinstance(node, ast.Import):
            modules = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            modules = [node.module or ''] + [a.name for a in node.names]
        for module in modules:
            dependencies(root, module.removeprefix('deck.').split('.')[0], seen)
    return seen


def affected(root, names, paths):
    changed_modules = {Path(p).stem for p in paths if p.startswith('deck/') and p.endswith('.py')}
    selected = {n for n in names if dependencies(root, n) & changed_modules}
    for path in paths:
        match = re.search(r'week\d{2}', path)
        if match and match[0] in names:
            selected.add(match[0])
    # Shared assets/toolchain/site changes can affect every deck. Unknown-only
    # changes also fail safe to a complete build rather than silently doing none.
    shared = any(p.startswith(('deck/assets/', 'site/')) or p == 'requirements.txt' for p in paths)
    return names if shared or not selected else [n for n in names if n in selected]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Git base SHA used only for changed-week selection')
    parser.add_argument('--output', help='Write the JSON list for the build step')
    args = parser.parse_args()
    root = Path.cwd()
    names = registered(root)
    if args.base:
        paths = subprocess.check_output(['git', 'diff', '--name-only', args.base, 'HEAD'], text=True).splitlines()
        names = affected(root, names, paths)
    data = json.dumps(names)
    if args.output:
        Path(args.output).write_text(data + '\n')
    print(data)


if __name__ == '__main__':
    main()
