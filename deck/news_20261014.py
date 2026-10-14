"""Dated classroom news, checked against primary sources on 14 October 2026.
Shared content for this week's programming and design discussions.
No API calls, accounts, autoplay, assessment questions or benchmark rankings.
"""
from deckgen import T, Rect, INK, MUTED, TEAL
from deckgen.layouts import content

GOOGLE = "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/"
GEMINI = "https://gemini.google/release-notes/"
HAIKU = "https://www.anthropic.com/claude-haiku-5-5"
OPENAI = "https://openai.com/index/gpt-6-for-everyone/"
MOTION = "https://claude.com/resources/articles/dashboards-and-motion"

def news_slides(course="SD5913"):
    """Seven optional discussion slides; no ClassPoint/quiz activity IDs."""
    design = course == "SD2112"
    rows = [
        ("13 OCT 2026 · GOOGLE", "Gemini 4 Argon", [
            "Complex coding and spatial reasoning; Google shows Blender / Three.js demos.",
            "Released: paid API, Gemini Pro / Ultra; Antigravity access for Ultra.",
            "Vendor demos and performance claims; not an independent class test.",
        ], "Which design choices would you keep control of?" if design else
           "What tests would prove the generated 3D scene works?",
         GOOGLE, "Announcement + 3D demos",
         "Proprietary model, not open weights. Optional: open the desk-to-racing-game demo. "
         "Do not imply this was tested in class. The same date also brought Antigravity "
         "integration into Gemini on macOS: " + GEMINI),
        ("7 OCT 2026 · ANTHROPIC", "Haiku 5.5: choose the job", [
            "Small model with adjustable effort for narrow, repeated agent tasks.",
            "Released on Claude Platform, AWS, Google Cloud and Azure.",
            "Larger Claude models remain stronger for complex coding in vendor tests.",
        ], "Which small production task could you delegate and check?" if design else
           "Which task needs a bigger model, and which needs a clear test?",
         HAIKU, "Release + evaluation conditions",
         "Proprietary model, not open weights. Compare correctness, latency and total cost "
         "on the same task; model size alone is not a quality guarantee."),
        ("7 OCT 2026 · OPENAI", "An answer can be an interface", [
            "GPT-6 Intelligent UI creates interactive diagrams, forms and small tools.",
            "Chat rollout: paid plans from 7 October; Free / Go from 8 October.",
            "Enterprise access depends on admin settings. Check the generated behaviour.",
        ], "Does the interaction explain something a static image cannot?" if design else
           "Ask for frequency / amplitude sliders. How would you test them?",
         OPENAI, "Release + availability",
         "This release concerns Chat; it does not change Work or Codex models. "
         "Optional instructor demo: a silent waveform explorer. Check labelled axes, "
         "frequency doubling and amplitude scaling. Keep any sound off by default. "
         "Generated UI can still be wrong; a polished surface is not verification."),
        ("8 OCT 2026 · ANTHROPIC", "Motion you can edit", [
            "Claude Motion animates text, charts, shapes and images as editable code.",
            "MP4 export; Team / Enterprise beta. Enterprise admins must enable it.",
            "Code-based animation, not a video-generation model producing footage.",
        ], "When would editable animation serve your team video mark?" if design else
           "Which animation properties should remain explicit in code?",
         MOTION, "Product announcement + demo",
         "Proprietary product beta. Optional: show the official explainer example. "
         "Discuss timing and editability without claiming a classroom result. "
         "No student subscription or live generation is required."),
        ("STATUS CHECK · 14 OCT 2026 · MELTY", "Games become remix material", [
            "Windows launcher for mods and mashups of games you already own.",
            "Give Claude Code or Codex its instructions to build and publish a mashup.",
            "Free download; compatibility and safety claims need checking per mod.",
        ], "What makes a mashup a new creative work?" if design else
           "Which behaviours would you test before sharing a game mod?",
         "https://melty.gg/", "Melty: examples + requirements",
         "The official page provides no exact launch date; 14 October is our status-check "
         "date, not a release date. Show the page examples rather than installing in class. "
         "Owning a game does not by itself resolve permissions to redistribute assets. "
         "Do not infer that Melty uses REA or that arbitrary game pairs work."),
        ("11 OCT 2026 · PHOTOCRAFT 0.7.0", "Rebuilding creative tools", [
            "ArtCraft lists 13 Rust creative apps, from image editing to audio.",
            "PhotoCraft 0.7.0: downloadable desktop builds; Apache-2.0 source.",
            "The lineup is early alpha / in development; familiar UI is not feature parity.",
        ], "What must a replacement preserve: habits, files or results?" if design else
           "How would you test file compatibility beyond a similar interface?",
         "https://getartcraft.com/apps", "ArtCraft: lineup + application links",
         "Concrete release: https://github.com/storytold/photocraft/releases/tag/v0.7.0 "
         "published 11 October 2026. License verified from the PhotoCraft repository; "
         "do not assume every app has that same license. The site advertises agent access "
         "via CLI, JSON or MCP. These apps are not classroom-tested replacements. "
         "No evidence here establishes that ArtCraft uses REA."),
        ("11 OCT 2026 · REA 6.4.0", "If agents can inspect software...", [
            "REA connects agents to app / binary analysis through MCP and a CLI.",
            "MIT-licensed tool; 6.4 adds Android inspection and analysis improvements.",
            "Evidence can support reimplementation; inferred behaviour still needs tests.",
        ], "Where is your line between inspiration, compatibility and copying?" if design else
           "What evidence separates a compatible implementation from a clone?",
         "https://github.com/morluto/rea", "REA: source, examples + limitations",
         "Release: https://github.com/morluto/rea/releases/tag/rea-agents-6.4.0 "
         "published 11 October 2026. Native analysis needs a supported provider such as "
         "Ghidra, Hopper or IDA; a tool's MIT license grants no rights over its targets. "
         "Discussion: distinguish observing behaviour, independently implementing a feature, "
         "copying source/assets, and bypassing access controls. Ask who benefits, who is credited, "
         "and which permissions need checking. This is an ethics/design discussion, not legal advice. "
         "Optional safe exercise: observe a teacher-owned toy interface, write an input/output "
         "specification and edge-case tests, then implement independently without viewing source. "
         "Do not claim this proves a legal clean-room process."),
    ]
    slides = []
    for date, heading, points, prompt, url, label, note in rows:
        slide = content("AI NEWS · " + date, heading, points,
                        body_size=36, title_size=70,
                        notes="Checked 14 October 2026. Optional one-minute discussion; "
                              "not assessed or required quiz material. " + note +
                              " Primary source: " + url)
        # Keep the source and discussion prompt out of the body text region.
        slide.els[-1].h = 340
        slide.els.extend([
            Rect(120, 748, 1680, 2, "#D7D9D7"),
            T(120, 780, 1680, 100, prompt, "xbold", 40, INK, lh=1.12),
            T(120, 908, 1680, 48, "[" + label + "](" + url + ")",
              "body", 28, TEAL, lh=1.2),
        ])
        slides.append(slide)
    return slides
