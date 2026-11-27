"""Week 13 news, final quiz, and poster fair."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from deckgen.layouts import content, finalize
from course import footer

ROCKSTAR = 'https://www.rockstargames.com/newswire/article/39akk424a9oo53/grand-theft-auto-vi-now-available'
NVIDIA = 'https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director'
ANTHROPIC = 'https://www.anthropic.com/news/ipo-close'

room_file = HERE / 'week13-poster-fair-link.txt'
try:
    room_url = room_file.read_text().strip()
except FileNotFoundError:
    room_url = ''

board = (f'[Open the Excalidraw poster fair]({room_url})' if room_url else
         'Open the Excalidraw link shared in the class channel.')

slides = [
    content('SD2112 / 27 NOVEMBER 2026', 'Week 13 news', [
        f'[GTA VI]({ROCKSTAR}) is out on PS5 and Xbox Series X|S.',
        f'[NVIDIA]({NVIDIA}) reinstated Jensen Huang as CEO on 23 Nov.',
        f'[Anthropic]({ANTHROPIC}) began trading on Nasdaq on 19 Nov. Its IPO priced at $83 a share.',
    ], image=str(HERE / 'assets/week13/gta-vi-official.jpg'), fit='contain',
        caption=f'[Official Rockstar launch artwork]({ROCKSTAR})', body_size=38,
        notes='Ask what impressed or disappointed students about GTA VI. '
              'NVIDIA also reinstated Huang as president and board director. '
              'Anthropic reported $93.5B in gross IPO proceeds, including the option and selling shareholders. '
              'Move to the quiz after the news.'),
    content('SD2112 / WEEK 13', 'Final quiz', [
        'Open the final quiz in Canvas when instructed.',
        '50 multiple-choice questions. Choose one answer per question.',
    ], body_size=48,
        notes='Announce the time limit and permitted resources before students begin. '
              'Leave this slide up until the quiz closes.'),
    content('SD2112 / WEEK 13', 'Poster fair', [
        board,
        'Find your group and add your poster preview and full-size link.',
        'Add viewing links for your video and mediation brief.',
        'Visit another group and ask them about a design decision.',
    ], body_size=43,
        notes='Ask one editor per group to add material to its existing space. '
              'Check that another group can view the links. Final submissions go through Canvas.'),
]

DECK = dict(title='SD2112 / AI in Design / Week 13', slides=finalize(slides, footer(13)),
            pdf='SD2112-week13.pdf', presenter_start_slide=1)
