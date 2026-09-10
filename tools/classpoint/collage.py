"""
A collage of the pictures the room uploaded to a ClassPoint image-upload activity.

    python tools/classpoint/collage.py OUT.jpg ACTIVITY_ID [ACTIVITY_ID ...] [--cols 15] [--cell 128]

Reads the public activity page (app.classpoint.io/activity/<id>), takes only the response
image URLs out of it, fetches them, fits each into a square cell and tiles them into a grid.
Nothing else from the page is kept: no names, no ids, no order that could be traced back
to a person. The result is a picture for a slide, and it is what gets committed.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import io
import re
import sys
import urllib.request

from PIL import Image, ImageOps

PAGE = 'https://app.classpoint.io/activity/{}'
IMG = re.compile(r'https://cpfile\d*\.blob\.core\.windows\.net/user/resp-[0-9a-f-]+\.(?:png|jpe?g|webp)', re.I)


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={'User-Agent': 'sd2112-collage'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def image_urls(activity):
    html = fetch(PAGE.format(activity)).decode('utf-8', 'replace')
    seen, out = set(), []
    for m in IMG.finditer(html):
        u = m.group(0)
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def thumb(url, cell, tries=3):
    for i in range(tries):
        try:
            im = Image.open(io.BytesIO(fetch(url))).convert('RGB')
            return ImageOps.fit(im, (cell, cell), Image.LANCZOS)
        except Exception as e:      # a cut-off download is retried; a broken upload must not sink the wall
            if i == tries - 1:
                print(f'  skipped {url[-40:]}: {e}', file=sys.stderr)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('activities', nargs='+')
    ap.add_argument('--cols', type=int, default=15)
    ap.add_argument('--cell', type=int, default=128)
    ap.add_argument('--gap', type=int, default=4)
    a = ap.parse_args()
    urls = []
    for act in a.activities:
        u = image_urls(act)
        print(f'{act}: {len(u)} pictures')
        urls += u
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        tiles = [t for t in ex.map(lambda u: thumb(u, a.cell), urls) if t is not None]
    rows = -(-len(tiles) // a.cols)
    w = a.cols * a.cell + (a.cols + 1) * a.gap
    h = rows * a.cell + (rows + 1) * a.gap
    wall = Image.new('RGB', (w, h), (255, 255, 255))
    for i, t in enumerate(tiles):
        r, c = divmod(i, a.cols)
        wall.paste(t, (a.gap + c * (a.cell + a.gap), a.gap + r * (a.cell + a.gap)))
    wall.save(a.out, quality=86, optimize=True)
    print(f'{a.out}: {len(tiles)} pictures, {a.cols} x {rows}, {w} x {h}')


if __name__ == '__main__':
    main()
