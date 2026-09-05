"""
Snapshot the live sketches of one or more decks into deck/assets/sketches/ (committed):
the still the PowerPoint and the PDF show where the html deck runs the sketch.

    python tools/snap.py week03            # the sketches of week 3 that have no snapshot yet
    python tools/snap.py week03 --force    # redo them
    python tools/snap.py --all [--force]   # every deck

Needs node + playwright + Chromium (see README). The still is taken 1.5 s after load with the
mouse resting at 60 % / 40 % of the canvas, no click; design the sketch so that state looks right.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import deckgen                          # noqa: E402
from build_all import DECKS, load_deck  # noqa: E402


def main(argv):
    force = '--force' in argv
    names = [a for a in argv if not a.startswith('--')]
    if '--all' in argv or not names:
        names = DECKS
    if deckgen.node_playwright_env() is None:
        print('node + playwright + Chromium are needed for snapshots (README: Build locally)')
        return 1
    for name in names:
        mod = load_deck(name)
        made = deckgen.snapshot_sketches(mod.DECK, name, force=force)
        missing = [el.name for el in deckgen.sketches_of(mod.DECK) if not deckgen.twin_png(el.name).exists()]
        print(f'{name}: {len(made)} snapshot(s) made' + (f', still missing: {missing}' if missing else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
