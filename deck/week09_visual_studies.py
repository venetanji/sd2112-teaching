"""Original teaching diagrams; source figures remain on the following slides."""
from pathlib import Path
import random

from deckgen import INK
from deckgen.core import Image
from deckgen.layouts import T

ASSETS = Path(__file__).parent / 'assets/week09/visual-studies'
TEAL, PALE, ORANGE = '#246E70', '#EAF2F2', '#ED6D24'

PANELS = {
    'R1': ('Millions of videos -> hundreds of candidates -> dozens ranked.',
           [('WHAT IT DOES', 'Pick possible videos, then order them.'),
            ('INVENTED EXAMPLE', 'Pick 100 workshops; show 10. If pottery misses the 100, ranking cannot rescue it.'),
            ('DESIGN LESSON', 'Check what gets left out before ranking.')],
           '2016 system: compared model and feed versions. Engagement is not wellbeing.'),
    'R2': ('Within each initial feed: random assignment to switch or stay.',
           [('WHAT THEY DID', 'Randomly switch or keep US users\' feeds for about 7 weeks.'),
            ('ILLUSTRATIVE EXAMPLE', 'Two people start with newest-first feeds. One switches; one stays. Compare who they follow.'),
            ('WHAT THEY CHECKED', 'Survey answers + followed accounts.')],
           'Survey: 4,965. Following: n=2,387. Earlier feed histories were not randomized.'),
    'R3': ('Moving dots -> own estimate and weight -> reveal advice.',
           [('WHAT THEY DID', '120 people guess how many dots move right, then receive advice.'),
            ('WORKED EXAMPLE', 'Your guess: 53%. Advice: 73%.\nMix 40% of yours + 60% of advice = 65%.'),
            ('LEARNING CHECK', 'Does your next unaided guess change?')],
           'ADAPTED FROM METHODS / 0-100% estimates; accurate, biased or noisy advice. Not a feed experiment.'),
    'R4': ('Same classifier tested across four benchmark groups; each group has its own denominator.',
           [('WHAT THEY DID', 'Test 3 gender classifiers on 1,270 portraits in 2017. Compare groups.'),
            ('INVENTED EXAMPLE', '5 wrong labels out of 100 tested = 5% error.'),
            ('FAIR COMPARISON', 'Compare percentages, not raw error counts.')],
           'Historical binary labels; not identification. Dots are not sample counts.'),
    'R5': ('Dataset plus a record of people, collection, uses and limits.',
           [('WHAT THEY PROPOSE', 'Send a dataset with its backstory, not just its records.'),
            ('INVENTED EXAMPLE', 'A workshop is tagged "relevant". Who chose that label? Who paid them?'),
            ('DESIGN LESSON', 'Record what is known - and what is missing.')],
           'No experiment established improved fairness.'),
}

FIGURE_COPY = {
    'First retrieve. Then rank.': [
        'Millions -> hundreds -> dozens.\nArchitecture, not an effect size.',
        '2016 system.\nPrediction and engagement, not wellbeing.',
        'Excluded upstream?\nRanking cannot rescue it.'],
    'Following is not just a feed setting.': [
        'Switch ON / OFF: ranking.\nBlue: basic analysis.\nOrange: accounts for prior\nparticipant differences.',
        'Units: standard deviations.\nBars show uncertainty.\nCrossing zero: no change\nis still plausible.',
        'Switch ON: more conservative\nactivist follows. Survey: no\nclear polarization change.\nReset not tested.'],
    'Estimate first. See the advice later.': [
        'a: estimate moving dots.\nb: three advice patterns.',
        'c: estimate + choose weight\nBEFORE seeing advice.',
        'Later independent estimates:\nlearning, not current-answer copying.'],
    'Read the error row, not just the average.': [
        'DF/DM: darker female/male.\nLF/LM: lighter female/male.',
        'IBM error: All 12.1%.\nDF 34.7% / LM 0.3%.\nWithin-group rates.',
        '2017 binary classification.\nNot identification.\nCauses/current rates unknown.'],
    'Ask who did the work.': [
        'Who collected the data?\nHow were they paid?',
        'Trace collection,\nlabels and correction.',
        'Documentation makes questions visible.\nIt does not certify fairness.'],
}


def render_assets():
    """Deterministic raster assets with deliberately sparse, large labels."""
    from PIL import Image as PILImage, ImageDraw, ImageFont
    import deckgen
    font_path = Path(deckgen.__file__).parent / 'fonts/Inter-Variable.ttf'
    ASSETS.mkdir(parents=True, exist_ok=True)
    for key in PANELS:
        image = PILImage.new('RGB', (1100, 660), 'white')
        d = ImageDraw.Draw(image)

        def text(x, y, label, size=44, fill=INK, anchor='mm'):
            d.text((x, y), label, font=ImageFont.truetype(str(font_path), size), fill=fill, anchor=anchor)

        def box(bounds, label, fill=PALE, size=44):
            d.rounded_rectangle(bounds, radius=18, fill=fill)
            text((bounds[0]+bounds[2])/2, (bounds[1]+bounds[3])/2, label, size)

        def arrow(x1, y1, x2, y2):
            import math
            d.line((x1, y1, x2, y2), fill=TEAL, width=7)
            a=math.atan2(y2-y1,x2-x1)
            d.polygon([(x2,y2),(x2-22*math.cos(a-.5),y2-22*math.sin(a-.5)),
                       (x2-22*math.cos(a+.5),y2-22*math.sin(a+.5))],fill=TEAL)

        if key == 'R1':
            for y, width, label in [(25,1000,'Millions'),(240,720,'Hundreds'),(455,440,'Dozens')]:
                left=(1100-width)//2
                d.polygon([(left,y),(left+width,y),(left+width-55,y+150),(left+55,y+150)], fill=PALE)
                text(550,y+75,label,60)
                if y<455: arrow(550,y+164,550,y+203)
        elif key == 'R2':
            text(550,32,'Initial feed',44)
            for y, start, switch in [(100,'Newest first','Ranked feed'),(390,'Ranked feed','Newest first')]:
                box((15,y+55,440,y+180),start,size=42)
                arrow(455,y+115,620,y+35); arrow(455,y+115,620,y+210)
                box((640,y-10,1080,y+95),switch,size=42)
                box((640,y+155,1080,y+260),'Stay',size=44)
        elif key == 'R3':
            d.rounded_rectangle((50,40,440,400),radius=22,fill=INK)
            rng=random.Random(9)
            for _ in range(100):
                x,y=rng.randint(75,415),rng.randint(65,375)
                d.ellipse((x-3,y-3,x+3,y+3),fill='white')
            text(245,455,'Moving dots',44)
            arrow(470,210,600,210)
            box((625,55,1080,210),'Estimate',size=50)
            box((625,245,1080,400),'Choose weight',size=44)
            arrow(855,420,855,490)
            box((625,510,1080,640),'Reveal advice',fill='#FBE8DD',size=44)
        elif key == 'R4':
            text(550,45,'Same classifier',52)
            for label,x,y in [('Darker female',50,130),('Darker male',585,130),('Lighter female',50,405),('Lighter male',585,405)]:
                d.rounded_rectangle((x,y,x+465,y+225),radius=18,fill=PALE)
                text(x+232,y+42,label,40)
                for j in range(12):
                    cx=x+105+(j%4)*85;cy=y+100+(j//4)*44
                    d.ellipse((cx-13,cy-13,cx+13,cy+13),fill=TEAL)
            # Identical illustrative groups show comparison structure, not counts/rates.
        else:
            for y in (130,210,290):
                d.rounded_rectangle((60,y,370,y+100),radius=12,fill=TEAL)
                for x in (110,170,230,290): d.ellipse((x,y+40,x+12,y+52),fill='white')
            text(215,465,'Records',50)
            text(490,270,'+',76,TEAL)
            d.rounded_rectangle((610,65,1060,590),radius=18,fill=PALE)
            text(835,130,'Context',52)
            for y,label in [(245,'People'),(335,'Collection'),(425,'Uses'),(515,'Limits')]:
                text(835,y,label,44)
        image.save(ASSETS/f'{key.lower()}.png')


def apply_visuals(slides):
    for slide in slides:
        if slide.title in FIGURE_COPY:
            old=' '.join(r.text for e in slide.els if hasattr(e,'paras') for p in e.paras for r in p.runs)
            slide.notes += '\nFull figure explanation retained from projection: ' + old
            explanations=[e for e in slide.els if hasattr(e,'paras') and
                          ((e.x==1260 and e.y in (355,527,699)) or e.y==780)]
            assert len(explanations)==3, slide.title
            for element,copy in zip(explanations,FIGURE_COPY[slide.title]):
                size = 31 if slide.title == 'Following is not just a feed setting.' else 33
                element.paras=T(element.x,element.y,element.w,element.h,copy,'body',size,INK,lh=1.2).paras
        if not any(getattr(e,'name','') == 'study-task-body' for e in slide.els):
            continue
        citation = next(e for e in slide.els if getattr(e,'name','') == 'paper-citation')
        key = citation.paras[0].runs[0].text.split(' / ')[0]
        alt, panels, limit = PANELS[key]
        previous=' '.join(r.text for e in slide.els if hasattr(e,'paras') for p in e.paras for r in p.runs)
        slide.notes += '\nFull walkthrough retained from projected text: ' + previous
        slide.notes += '\nVisual: original instructor diagram, not a source figure or measured data.'
        if key == 'R4':
            slide.notes += ' DF/DM/LF/LM are the study darker/lighter female/male labels. Equal dot arrays illustrate grouping only, NOT sample counts or error rates.'
        slide.els = [e for e in slide.els if getattr(e,'name','') in ('paper-title','paper-citation') or getattr(e,'y',0)<150]
        slide.els.remove(citation)
        slide.els.append(Image(120,335,1050,535,str(ASSETS/f'{key.lower()}.png'),'contain',
                               name='study-diagram',placeholder=alt))
        for i,(label,value) in enumerate(panels):
            y=350+i*180
            slide.els += [T(1230,y,570,40,label,'mono',25,TEAL),
                          T(1230,y+45,570,120,value,'body',32,INK,lh=1.15)]
        slide.els += [T(120,900,1680,48,limit,'body',29,INK,lh=1.1),citation]


if __name__ == '__main__':
    render_assets()
