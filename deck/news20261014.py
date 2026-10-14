"""Optional dated news opener for the next SD2112 session.
Kept separate from already-taught Week 6 and the unmerged historic course rewrite.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen.layouts import title, finalize
from news_20261014 import news_slides

S = [title("SD2112 · NEWS · 14 OCTOBER 2026", "What changed this week?",
           "Agents, interactive answers and editable motion", size=100,
           notes="Optional four-minute opener for the next session. Keep the full "
                 "30-minute, 40-question quiz and the existing brainstorming, team "
                 "formation and team video-mark activity. News is not new assessed "
                 "quiz content. No changes to numbering, deadlines or rubrics.")]
S.extend(news_slides("SD2112"))
DECK = dict(title="SD2112 · AI news · 14 October 2026",
            pdf="SD2112-news20261014.pdf",
            slides=finalize(S, "SD2112 · AI NEWS · 14 OCT 2026"))
