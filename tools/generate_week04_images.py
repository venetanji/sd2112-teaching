"""Generate the Week 4 editorial visuals through the requested Easel Qwen endpoint.

Run from the repository root. EASEL_KEY may be exported or stored in the ignored .env.
"""
from __future__ import annotations

import base64
import json
import os
import sys
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = 'https://easel.ait4x.org/v1/images/generations'

PROMPTS = {
 'week04-language-sculpture.png': {'prompt': 'Single editorial still life for a design-school lecture. One long ribbon of warm white paper folded into three branching sculptural paths on a dark navy surface. A few small teal and orange paper tiles travel along the folds. Beautiful tactile paper, clear silhouette, studio side lighting, restrained sophisticated composition, large simple shapes. Landscape close-up, generous negative space, no busy background. This is an abstract metaphor for language possibilities, not a technical diagram. Absolutely no text, no letters, no numbers, no writing, no symbols, no labels, no logos, no human face, no robot.', 'purpose': 'Abstract language possibilities illustration for the model-authored interlude; a metaphor, not a neural architecture.'},
 'week04-shared-workbench.png': {'prompt': 'A single clear editorial still life, photographed from a slight overhead angle. A rectangular navy wooden sorting tray with six large compartments on an ivory studio table. One continuous soft teal fabric ribbon curls through three compartments. Two simple orange wooden blocks fit neatly in the other compartments. Tactile real materials, elegant design-school publication, warm soft shadows, minimalist, generous empty space, only these few objects. The rigid tray and flexible ribbon visibly coexist. Landscape composition. Absolutely no text, no letters, no numbers, no writing, no labels, no diagram arrows, no logos, no hands, no faces, no robots.', 'purpose': 'Rules and learned flexibility share a workbench: visual metaphor for Machine A and B in a harness.'},
}


def load_key() -> str:
    key = os.environ.get('EASEL_KEY')
    if key:
        return key
    env_path = ROOT / '.env'
    if env_path.exists():
        for line in env_path.read_text(encoding='utf-8').splitlines():
            if line.startswith('EASEL_KEY='):
                return line.split('=', 1)[1].strip().strip('"').strip("'")
    raise RuntimeError('EASEL_KEY is not set')


def generate(filename: str, prompt_spec: dict[str, str], key: str) -> None:
    payload = {
        'model': 'qwen-image-2.1',
        'prompt': prompt_spec['prompt'],
        'size': '1536x1024',
        'n': 1,
        'response_format': 'b64_json',
    }
    request = Request(
        ENDPOINT,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json',
        },
        method='POST',
    )
    with urlopen(request, timeout=600) as response:
        result = json.load(response)

    item = result['data'][0]
    if 'b64_json' in item:
        image = base64.b64decode(item['b64_json'])
    else:
        with urlopen(item['url'], timeout=60) as response:
            image = response.read()

    target = ROOT / 'deck' / 'assets' / filename
    target.write_bytes(image)
    metadata = {
        'provider': 'https://easel.ait4x.org/v1',
        'request': payload,
        'purpose': prompt_spec['purpose'],
    }
    target.with_suffix('.json').write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
    )
    print(f'Saved {target.relative_to(ROOT)} ({len(image)} bytes)')


def main() -> None:
    key = load_key()
    requested = set(sys.argv[1:])
    if requested - PROMPTS.keys():
        raise SystemExit(f'Unknown output name: {sorted(requested - PROMPTS.keys())}')
    selected = requested or PROMPTS.keys()
    for filename in selected:
        target = ROOT / 'deck' / 'assets' / filename
        if target.exists():
            print(f'Skipping existing {target.relative_to(ROOT)}')
            continue
        spec = PROMPTS[filename]
        generate(filename, spec, key)


if __name__ == '__main__':
    main()
