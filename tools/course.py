"""
Shared course facts used by more than one deck: links, the semester map.
Edit here and every deck that shows the journey updates.
"""
from deckgen import INK, PAPER, TEALS, VIOLETS, ORANGES, PINKS

SITE = 'venetanji.github.io/sd2112-teaching'
PLAYLIST = 'https://www.youtube.com/playlist?list=PLU58DFEI5YDQ'
GENAI = 'genai.polyu.edu.hk'
P5 = 'editor.p5js.org'

# rows for layouts.journey(); here=(row, cell) marks the current week
JOURNEY = [
    dict(label='1 · What is AI?', color=TEALS[0], tint=TEALS[4], cells=[('Week 1', 'Two ways to teach a machine'), ('Week 2', 'Rules that make things: code, chance, generative art'), ('Week 3', 'Learning from examples: concepts, neurons, Move 37')]),
    dict(label='2 · AI for the creative process', color=VIOLETS[0], dark=True, tint=VIOLETS[5], cells=[('Week 4', 'Language machines: LLMs, prompts, agents'), ('Week 5', 'Image machines: diffusion, CLIP, mediation'), ('Week 6', 'Sound machines: music, voice, spectrograms')]),
    dict(label='Mid-term', color=PAPER, tint=PAPER, cells=[('Week 7', 'Mid-term quiz · project pitches · teams · reflection due')]),
    dict(label='3 · AI inside products', color=ORANGES[0], tint=ORANGES[4], cells=[('Week 8', 'AI as design material: use vs incorporate'), ('Week 9', 'Data, bias and privacy'), ('Week 10', 'Recommendation systems and the feed')]),
    dict(label="4 · The designer's turn", color=PINKS[0], dark=True, tint=PINKS[4], cells=[('Week 11', 'Curating outputs and datasets · authorship'), ('Week 12', 'Language as an interface: chatbots and agents')]),
    dict(label='Showcase', color=INK, dark=True, tint=PAPER, cells=[('Week 13', 'Poster fair · final quiz')]),
]
