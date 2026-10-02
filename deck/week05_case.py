"""Three evidence-led slides on an SD2112 agent/media co-creation case."""
from pathlib import Path

from deckgen import INK, PAPER, ORANGE
from deckgen.core import Image
from deckgen.layouts import Rect, T, content


ASSETS = Path(__file__).resolve().parent / "assets"
TEAL = "#246E70"
LINE = "#D5DCDA"
WHITE = "#FFFFFF"


def _slide(title, notes):
    slide = content("CASE REFLECTION · SD2112 CO-CREATION", title, [],
                    bg=PAPER, title_size=55, notes=notes)
    # Keep the deck's shared header, but replace its generic empty body with case-specific content.
    slide.els = slide.els[:2]
    return slide


def _stage(slide, x, label, detail, image=None, dark=False):
    color = INK if dark else WHITE
    slide.els.append(Rect(x, 378, 500, 390, color))
    if image:
        slide.els.append(Image(x + 30, 393, 440, 320, str(ASSETS / image), "contain"))
    else:
        slide.els.append(T(x + 32, 422, 436, 250, detail, "body", 31, "#FFFFFF" if dark else INK, lh=1.28))
    slide.els.append(T(x + 20, 786, 460, 42, label, "monomed", 24, TEAL))


def _case_brief():
    slide = _slide(
        "The brief emerged through choices.",
        "Evidence and interpretation: the source mark, forest treatment, and brighter forest edit are actual course-team image iterations from September 2026. The forest variant shifted the brief from preserving a plain mark toward combining its recognizable form with a material and setting; the brighter edit was a selected human-directed refinement, not an untouched first output. Compare what remained (the a-like form) with what changed (the chalk-ring dot, forest image, contrast). Do not call this a finalized course logo or imply that the model independently authored the evolving brief. Source: SD2112 course-team logo refinement record, 28 September 2026; the brighter edit is the saved selection #4. Ask what the next brief should protect. This is one compact case reflection, not an extra activity.")
    _stage(slide, 120, "01 · CLEAN MARK", "", "week05-logo-original.png")
    _stage(slide, 710, "02 · FOREST VARIANT", "", "week05-logo-before-brightening.png", dark=True)
    _stage(slide, 1300, "03 · BRIGHTER EDIT", "", "week05-logo-brighter-edit.png", dark=True)
    for x in (635, 1225):
        slide.els.append(T(x, 525, 55, 60, "→", "xbold", 42, ORANGE))
    for x, caption in ((120, "A recognizable form to keep."),
                       (710, "A setting and material enter."),
                       (1300, "A chosen refinement—not a finish.")):
        slide.els.append(T(x + 14, 842, 470, 78, caption, "body", 28, INK))
    slide.els.append(T(120, 951, 1680, 43,
                       "The mark did not arrive fully formed. What entered the brief after seeing a candidate?",
                       "xbold", 31, INK))
    return slide


def _repair_choice():
    slide = _slide(
        "A better prompt was not always the right repair.",
        "Evidence and interpretation: the team's saved video iterations document rejection of a five-logo montage and a watercolor/origami direction; the paper-burning route also needed review against the intended transformation. In V8, flames appeared inside the letter counter and along its front edge. The correction was not another broad prompt rewrite: replace only the paper-burn transition, specifying a front-facing, top-to-bottom burn, while preserving the other approved scenes and constraints. V9 is the delivered revision and review pending; it remained pending human review; do not call it accepted or claim scientifically accurate combustion. Keep the distinction between what the saved version visibly attempted and our interpretation of why the workflow repair was better targeted. Source: SD2112 video revision record, September 2026, versions V8 and V9. No new render is implied by this slide.")
    columns = [
        (120, "EARLIER ITERATIONS", "Rejected montage.\nCoherent origami repair.\nLater, a burn to refine.", "#FFF4EB"),
        (710, "V8 · OBSERVED MISS", "Flames inside the counter\nand along the front edge.", WHITE),
        (1300, "V9 · TARGETED CHANGE", "Replace only that transition:\nfront-facing, top → bottom.", "#E5F1EF"),
    ]
    slide.els.append(T(120, 340, 1680, 55,
                       "When the failure is in the transition, change the transition.",
                       "xbold", 31, INK))
    for i, (x, label, body, fill) in enumerate(columns):
        slide.els.append(Rect(x, 416, 500, 330, fill))
        slide.els.append(T(x + 28, 452, 440, 46, label, "monomed", 24, TEAL))
        slide.els.append(T(x + 28, 532, 440, 175, body, "body", 32, INK, lh=1.25))
        if i < len(columns) - 1:
            slide.els.append(T(x + 515, 535, 55, 60, "→", "xbold", 42, ORANGE))
    slide.els.append(T(120, 805, 1680, 75,
                       "Prompt repair? Reference repair? Workflow repair? Choose from the failure you can point to.",
                       "xbold", 31, INK))
    slide.els.append(T(120, 900, 1680, 55,
                       "V9 delivered · review pending · not a claim of final acceptance",
                       "monomed", 24, TEAL))
    slide.els.append(T(120, 947, 1680, 40,
                       "What did you delegate—and what did you insist on keeping?",
                       "body", 27, INK))
    return slide


def _contribution_map():
    slide = _slide(
        "What did the agent actually contribute?",

        "Interpretive map of the documented workflow, not a claim that an agent made the final creative decision. Human contribution: set intent, critique iterations, and approve or reject directions. The coding agent (Machine B) coordinated tools and recalled a versioned brief across iterations; memory supported continuity but did not guarantee accurate recall, so saved artifacts and version checks remained necessary. Media models proposed image/video material and motion. Code/assembly (Machine A) handled sequence assembly and audio/frame-preservation operations in the later revision workflow. The human judged what to keep; V9 acceptance was still pending. Keep tool roles distinct: coordinating a tool is not the same as generating its media, and code-based assembly is not authorship of every pixel. Sources: SD2112 September 2026 co-creation and video revision records; exact replacement-frame and preservation checks recorded 30 September. The validation concerned 95 replacement frames in the specified interval and unchanged hashes for the other 1,345 lossless master frames plus preserved soundtrack; it does not establish bit-identical lossy review MP4 pixels.")
    boxes = [
        (120, "HUMAN", "Intent · critique\napproval / rejection", "#FFF4EB"),
        (470, "AGENT · MACHINE B", "Tool calls\nVersioned brief", "#E5F1EF"),
        (820, "MEDIA MODELS", "Propose images\nand motion", WHITE),
        (1170, "CODE · MACHINE A", "Assembly · audio\nframe preservation", "#E5F1EF"),
        (1520, "HUMAN · JUDGES", "What actually\nworks?", "#FFF4EB"),
    ]
    for i, (x, label, body, fill) in enumerate(boxes):
        slide.els.append(Rect(x, 440, 270, 270, fill))
        slide.els.append(T(x + 14, 477, 242, 60, label, "monomed", 24, TEAL))
        slide.els.append(T(x + 14, 555, 242, 115, body, "body", 27, INK, lh=1.24))
        if i < len(boxes) - 1:
            slide.els.append(T(x + 285, 535, 54, 60, "→", "xbold", 38, ORANGE))
    slide.els.append(T(120, 770, 1680, 58,
                       "A chain of proposals and decisions—not one autonomous author.",
                       "xbold", 32, INK))
    slide.els.append(T(120, 850, 1680, 70,
                       "V9 was delivered for review. Its final acceptance was not established.",
                       "body", 28, INK))
    return slide


def slides():
    """Return the three approved case/reflection slides for insertion in Week 5."""
    return [_case_brief(), _repair_choice(), _contribution_map()]
