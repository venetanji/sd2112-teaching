"""Text-free phase maps for the separate contributor deck."""
from deckgen.figures import Canvas

PHASE_NAMES = ('discover', 'define', 'develop', 'deliver')


def phase_map(phase):
    """Simplified Double Diamond after Design Council; color only the active half."""
    if phase not in PHASE_NAMES:
        raise ValueError(f'Unknown Double Diamond phase: {phase}')
    c = Canvas(360, 176)
    c.svg.append(f'<title>Double Diamond navigation: {phase.title()} highlighted</title>')
    halves = [
        [(12, 88), (96, 4), (96, 172)],
        [(96, 4), (180, 88), (96, 172)],
        [(180, 88), (264, 4), (264, 172)],
        [(264, 4), (348, 88), (264, 172)],
    ]
    for name, points in zip(PHASE_NAMES, halves):
        c.poly(points, '#246E70' if name == phase else '#FFFFFF', '#222222', 2)
    return c.finish('week10-nicolo-map-'+phase)
