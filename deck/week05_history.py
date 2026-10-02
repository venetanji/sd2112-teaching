"""Five-slide historical bridge: procedural art and the early Computer Art debate."""
from pathlib import Path

from deckgen import INK, ORANGE, PAPER, TEALS
from deckgen.core import Figure, Image
from deckgen.figures import Canvas
from deckgen.layouts import Rect, T, content

FOOTER_COLOR = '#246E70'
ASSETS = Path(__file__).resolve().parent / 'assets'


def _base(title, notes, title_size=58):
    slide = content('MACHINE A · A SHORT HISTORY', title, [], bg=PAPER,
                    title_size=title_size, notes=notes)
    # Keep the established course eyebrow and title; these slides supply their own visual body.
    slide.els = slide.els[:2]
    return slide


def _process_diagram():
    c = Canvas(1680, 470, bg='#FFFFFF')
    teal = '#246E70'
    pale = '#E7F1EF'
    boxes = [
        (25, 'PERSON', 'chooses a rule'),
        (435, 'PROGRAM', 'sets instructions'),
        (845, 'PLOTTER', 'executes the rule'),
        (1255, 'IMAGE', 'marks on paper'),
    ]
    for x, heading, detail in boxes:
        c.rect(x, 95, 360, 190, fill=pale, stroke=teal, width=3)
        c.text(x + 180, 159, heading, size=36, color=INK, anchor='middle', weight=700, mono=True)
        c.text(x + 180, 221, detail, size=28, color=INK, anchor='middle', mono=False)
    for x in (385, 795, 1205):
        c.line(x, 190, x + 39, 190, ORANGE, 5)
        c.line(x + 24, 177, x + 39, 190, ORANGE, 5)
        c.line(x + 24, 203, x + 39, 190, ORANGE, 5)
    c.line(205, 352, 1475, 352, '#B7CFCD', 3)
    c.text(840, 410, 'CHANCE CAN BE DESIGNED: variation inside a procedure',
           size=29, color=teal, anchor='middle', weight=700, mono=False)
    return c.finish('w05-machine-a-history-procedure')


def _timeline_diagram():
    c = Canvas(1680, 410, bg='#FFFFFF')
    teal = '#246E70'
    c.line(155, 205, 1525, 205, teal, 5)
    events = [
        (260, '1965', 'Computer art\nexhibitions'),
        (840, '1968', 'Cybernetic Serendipity\nLondon'),
        (1420, '1969', 'New Tendencies · Zagreb'),
    ]
    for i, (x, date, label) in enumerate(events):
        c.circle(x, 205, 17, fill=ORANGE if i == 1 else teal, stroke='#FFFFFF', width=3)
        c.text(x, 106, date, size=44, color=INK, anchor='middle', weight=700, mono=True)
        for row, line in enumerate(label.splitlines()):
            c.text(x, 280 + row * 38, line, size=29, color=INK, anchor='middle', weight=700, mono=False)
    c.text(840, 370, 'EXHIBITION · DEMONSTRATION · PUBLIC DEBATE', size=25,
           color=teal, anchor='middle', weight=700, mono=True)
    return c.finish('w05-machine-a-history-timeline')


def slides():
    """Return fresh slide objects for insertion after the course mediation block."""
    procedure_svg, procedure_png = _process_diagram()
    timeline_svg, timeline_png = _timeline_diagram()

    s1 = _base(
        'Machine A: design the procedure.',
        'A person specifies a procedure; a program expresses it; a plotter carries out the instructions and marks an image. The chain is a useful historical model, not a claim that every artist used the same hardware or workflow. Chance can be designed into the rules: the person defines where variation may occur, while the exact marks may not be predetermined. This distinguishes procedural authorship from hand-drawing every visible mark. Connect to the course Machine A label: explicit instructions shape an output. Sources: Week 2, PDF positions 28–30 and 36–37 (course deck, 2025); Frieder Nake, “There Should Be No Computer Art,” Bulletin of the Computer Arts Society (October 1971), pp. 18–19, https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/ .',
    )
    s1.els += [
        Figure(120, 335, 1680, 470, procedure_svg, procedure_png, name='machine-a-procedure'),
        T(120, 840, 1680, 68, 'The person designs the rules—including where chance may enter.',
          'xbold', 34, INK),
        T(120, 920, 1680, 34, 'PERSON → PROGRAM → PLOTTER → IMAGE', 'monomed', 22, FOOTER_COLOR),
    ]

    s2 = _base(
        'Bense: can aesthetic form be described systematically?',
        'Max Bense developed a rational aesthetics and explored information-theoretical descriptions of aesthetic objects. Treat this as an attempt to describe and analyze form, not a formula that proves beauty or reduces aesthetic judgement to a single number. Information is not synonymous with beauty, and entropy is not a beauty score. Keep Birkhoff distinct: his earlier mathematical aesthetics proposed a measure of aesthetic value as a relation between order and complexity; it is a separate project, not simply Bense’s information aesthetics. Paraphrase rather than quote. Sources: SD2112 Week 2 (2025), PDF position 28; Max Bense, “Die Mathematik in der Kunst,” 1949; George D. Birkhoff, Aesthetic Measure, Harvard University Press, 1933. Background: https://www.eai.org/artists/frieder-nake/biography .',
    )
    s2.els += [
        T(120, 330, 760, 50, 'BENSE · INFORMATION + FORM', 'monomed', 25, FOOTER_COLOR),
        Rect(120, 390, 760, 270, '#FFFFFF'),
        T(160, 425, 680, 72, 'Describe relations.', 'xbold', 44, INK),
        T(160, 520, 680, 112, 'A systematic account can ask\nhow elements are organized.', 'body', 32, INK, lh=1.25),
        T(1020, 330, 780, 50, 'BIRKHOFF · A DISTINCT PROPOSAL', 'monomed', 25, FOOTER_COLOR),
        Rect(1020, 390, 780, 270, '#FFFFFF'),
        T(1060, 425, 700, 72, 'Order / complexity.', 'xbold', 44, INK),
        T(1060, 520, 700, 112, 'A different mathematical measure;\nnot Bense’s information theory.', 'body', 32, INK, lh=1.25),
        Rect(120, 705, 1680, 4, ORANGE),
        T(120, 746, 1680, 90, 'Description can sharpen a question. It does not decide what is beautiful.',
          'xbold', 36, INK),
        T(120, 851, 1680, 86, 'Entropy measures uncertainty across possible outcomes.\nMore unpredictability does not make an image more beautiful.', 'body', 30, FOOTER_COLOR, lh=1.2),
        T(120, 955, 1680, 30, 'GENERATIVE AESTHETICS · FROM DESCRIBING FORM TO DEFINING PROCEDURES', 'monomed', 22, ORANGE),
    ]

    s3 = _base(
        'Nake: the artist programs possibilities.',
        'Frieder Nake was a mathematician and artist working with computer-generated graphics and plotter drawings. The displayed works are historical artworks, not reconstructions: Hommage to Paul Klee (1965) and Walk-Through-Raster (1966). In Hommage, a programmed procedure generates a field of forms with controlled variation; Walk-Through-Raster makes the traversal of a raster visible as a graphic procedure. Avoid claiming that the machine independently authored either work: Nake designed and interpreted the process, and the plotter executed it. Connect procedure and chance to the actual marks students can inspect. Sources: Frieder Nake, “There Should Be No Computer Art,” Bulletin of the Computer Arts Society (October 1971), pp. 18–19, https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/ ; artworks supplied in this course’s deck/assets.',
    )
    s3.els += [
        Image(120, 320, 780, 495, str(ASSETS / 'nake-homage-to-paul-klee-1965.jpg'), 'contain'),
        Image(1020, 320, 780, 495, str(ASSETS / 'nake-walk-through-raster-1966.jpg'), 'contain'),
        T(120, 825, 780, 48, 'HOMMAGE TO PAUL KLEE · 1965', 'monomed', 23, FOOTER_COLOR),
        T(1020, 825, 780, 48, 'WALK-THROUGH-RASTER · 1966', 'monomed', 23, FOOTER_COLOR),
        T(120, 892, 1680, 55, 'Designed procedure + variation → an artwork to read and judge.', 'xbold', 33, INK),
    ]

    s4 = _base(
        'A new machine. A familiar argument.',
        'Computer-generated work was shown publicly from 1965, followed by major exhibitions including Cybernetic Serendipity in London (1968) and New Tendencies in Zagreb (1969). These events made computer-based art visible beyond specialist research settings and prompted argument about authorship, originality, artistic status and the role of the machine. The timeline is deliberately selective, not a claim that these were the first or only exhibitions; avoid repeating the incorrect claim that a Berlin event was the first computer-art exhibition. Public debate did not begin or end at one show. Sources: Frieder Nake, “There Should Be No Computer Art,” Bulletin of the Computer Arts Society (October 1971), pp. 18–19, https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/ ; Week 2 course deck (2025), PDF positions 36–37.',
    )
    s4.els += [
        Figure(120, 350, 1680, 410, timeline_svg, timeline_png, name='machine-a-history-timeline'),
        T(120, 804, 1680, 65, 'The question was not only “Can a machine make this?”', 'xbold', 39, INK),
        T(120, 884, 1680, 62, 'It was also: who makes the choices—and what counts as art?', 'body', 34, INK),
    ]

    s5 = _base(
        'There should be no Computer Art.',
        'Nake’s 1971 essay is not a blanket rejection of computers or computational methods. He criticizes “Computer Art” as a marketable label and fashionable movement that can mystify the social and artistic decisions behind the work. At the same time, he argues that computer-based methods can be valuable as new means of production and social communication. The tension matters: do not flatten his argument into either “the computer is the artist” or “computers have no place in art.” Invite students to distinguish critique of a market category from critique of the tools and procedures themselves. Source: Frieder Nake, “There Should Be No Computer Art,” Bulletin of the Computer Arts Society (October 1971), pp. 18–19, https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/ .',
        title_size=56,
    )
    s5.els += [
        T(120, 325, 780, 48, 'WHAT HE CHALLENGES', 'monomed', 25, FOOTER_COLOR),
        Rect(120, 385, 780, 250, '#FFFFFF'),
        T(160, 422, 680, 70, 'Market + fashion', 'xbold', 44, INK),
        T(160, 510, 680, 95, 'A label can sell novelty\nand hide human decisions.', 'body', 32, INK, lh=1.25),
        T(1020, 325, 780, 48, 'WHAT HE STILL VALUES', 'monomed', 25, FOOTER_COLOR),
        Rect(1020, 385, 780, 250, '#FFFFFF'),
        T(1060, 422, 700, 70, 'New methods', 'xbold', 44, INK),
        T(1060, 510, 700, 95, 'Computational work can support\nproduction + social communication.', 'body', 32, INK, lh=1.25),
        Rect(120, 694, 1680, 4, ORANGE),
        T(120, 738, 1680, 72, 'Critique the mystification—not the possibility of making with computers.',
          'xbold', 35, INK),
        T(120, 850, 1680, 40, 'FRIEDER NAKE · COMPUTER ARTS SOCIETY · OCTOBER 1971',
          'monomed', 24, FOOTER_COLOR),
        T(120, 915, 1680, 55, '[Read the original: There should be no Computer Art](https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/)',
          'bold', 30, FOOTER_COLOR),
    ]

    for slide in (s1, s2, s3, s4, s5):
        slide.notes += ' Keep this to roughly one minute within the six-minute history block.'
    return [s1, s2, s3, s4, s5]
