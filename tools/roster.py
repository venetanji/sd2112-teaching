"""
ClassPoint saved-class roster from a list of student IDs.

    python tools/roster.py ids.csv classpoint/roster-2026-classpoint.csv

ids.csv: one student ID per line (e.g. 25088695d). The roster uses the last four
digits and the letter, upper-case (8695D), the convention used in the 2025 gradebook.
Both files are student data and are git-ignored: keep them out of the repository.
"""
import csv
import sys
from pathlib import Path


def main(src, dst):
    ids = [line.strip() for line in Path(src).read_text().splitlines() if line.strip()]
    short = [i[-5:].upper() for i in ids]
    dupes = {s for s in short if short.count(s) > 1}
    if dupes:
        sys.exit(f'short-ID collision: {sorted(dupes)} — use more digits for these students')
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    with open(dst, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Name'])
        w.writerows([s] for s in short)
    print(f'{len(short)} names -> {dst}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
