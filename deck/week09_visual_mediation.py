"""Original Week 9 diagrams; run this module to regenerate the panel PNGs."""
from pathlib import Path
from math import atan2, cos, sin
from PIL import Image as Raster, ImageDraw, ImageFont
import deckgen
from deckgen.core import Image
from deckgen.layouts import T, content

ASSETS = Path(__file__).parent / 'assets/week09/visual-mediation'
INK, TEAL, ORANGE = '#000B1C', '#246E70', '#ED6D24'
PALE, GRAY, WHITE = '#EAF2F2', '#76818A', '#FFFFFF'
FONT = Path(deckgen.__file__).parent / 'fonts/Inter-Variable.ttf'


class Drawing:
    """Deterministic 2x artwork; separate panels reflow on mobile."""
    def __init__(self, width=800, height=510):
        self.words = []
        self.im = Raster.new('RGB', (width*2, height*2), WHITE)
        self.d = ImageDraw.Draw(self.im)

    def line(self, points, fill=INK, width=5):
        self.d.line([(int(x*2), int(y*2)) for x,y in points], fill=fill, width=width*2, joint='curve')

    def rect(self, box, fill=PALE, outline=None, width=3, radius=0):
        fn = self.d.rounded_rectangle if radius else self.d.rectangle
        kw = dict(fill=fill, outline=outline, width=width*2)
        if radius: kw['radius'] = radius*2
        fn(tuple(int(v*2) for v in box), **kw)

    def ellipse(self, box, fill=PALE, outline=None, width=3):
        self.d.ellipse(tuple(int(v*2) for v in box), fill=fill, outline=outline, width=width*2)

    def text(self, x, y, text, size=36, color=INK):
        f = ImageFont.truetype(str(FONT), size*2)
        self.d.text((x*2,y*2), text, font=f, fill=color, anchor='mm')
        self.words.extend(text.split())

    def arrow(self, start, end, color=TEAL, width=6):
        self.line([start,end],color,width)
        a=atan2(end[1]-start[1],end[0]-start[0])
        pts=[end,(end[0]-20*cos(a-.45),end[1]-20*sin(a-.45)),(end[0]-20*cos(a+.45),end[1]-20*sin(a+.45))]
        self.d.polygon([(int(x*2),int(y*2)) for x,y in pts],fill=color)

    def person(self,x,y,color=INK,scale=1):
        r=20*scale
        self.ellipse((x-r,y-r,x+r,y+r),color)
        self.line([(x,y+28*scale),(x,y+108*scale)],color,8)
        self.line([(x-34*scale,y+63*scale),(x,y+42*scale),(x+34*scale,y+63*scale)],color,7)
        self.line([(x-30*scale,y+155*scale),(x,y+108*scale),(x+30*scale,y+155*scale)],color,7)

    def save(self,name):
        self.im.save(ASSETS/(name+'.png'))
        return len(self.words)


def bias_panels():
    a=Drawing(520)
    a.text(260,36,'INDUCTIVE BIAS',31,TEAL)
    for x,y in [(90,330),(180,270),(265,205),(355,150),(430,95)]:
        a.ellipse((x-10,y-10,x+10,y+10),INK)
    a.line([(65,370),(445,90)],TEAL,6)
    a.line([(65,370),(160,335),(260,155),(350,190),(445,90)],ORANGE,5)
    a.text(260,455,'How to generalize?',31)
    b=Drawing(520)
    b.text(260,36,'LEARNED PATTERN',31,TEAL)
    for i in range(3):
        x=50+i*150
        b.rect((x,150,x+125,325),PALE,INK)
        b.rect((x+10,175,x+115,205),TEAL)
        b.rect((x+42,220,x+83,325),INK)
    b.text(260,390,'Repeated dark centres',30)
    b.text(260,455,'Not automatically unfair',29)
    c=Drawing(520)
    c.text(260,36,'HARMFUL BIAS',31,TEAL)
    c.person(100,130); c.person(320,130)
    c.arrow((140,230),(230,230)); c.arrow((360,230),(445,230))
    c.line([(210,255),(230,280),(270,210)],TEAL,7)
    c.line([(427,207),(473,253)],ORANGE,7)
    c.line([(427,253),(473,207)],ORANGE,7)
    c.text(260,390,'Unequal consequences',31)
    c.text(260,455,'Who is affected?',31)
    return [('bias-assumptions',a),('bias-pattern',b),('bias-harm',c)]


def relation_panels():
    panels=[]
    for kind in range(3):
        a=Drawing(520)
        a.text(260,35,['HEIDEGGER','IHDE','VERBEEK'][kind],33,TEAL)
        a.person(70,170,INK,.7)
        if kind==0:
            a.rect((200,170,285,290),WHITE,'#B8D7D6',2,radius=12)
            a.ellipse((370,155,475,260),PALE,TEAL)
            a.arrow((115,220),(355,220))
            a.text(260,365,'Attention to the task',31)
        elif kind==1:
            a.rect((195,140,280,305),PALE,TEAL,4,radius=12)
            a.arrow((115,220),(185,220)); a.arrow((290,220),(350,220))
            a.ellipse((370,130,465,225),TEAL)
            a.ellipse((390,265,425,300),'#B8D7D6')
            a.text(260,365,'Amplify / reduce',31)
        else:
            a.rect((195,140,280,305),PALE,TEAL,4,radius=12)
            a.arrow((115,220),(185,220)); a.arrow((290,220),(415,145),TEAL,8)
            a.arrow((290,220),(415,300),GRAY,3)
            a.ellipse((425,120,470,165),TEAL)
            a.ellipse((425,275,470,320),PALE,GRAY)
            a.text(260,365,'Shape possible actions',30)
        a.text(260,455,'Person / technology / world',25,GRAY)
        panels.append((['equipment-attention','mediated-perception','mediated-action'][kind],a))
    return panels


def transparency_panels():
    a=Drawing()
    a.text(400,36,'IN USE',36,TEAL)
    a.person(120,180,INK,1.1)
    a.rect((310,130,470,335),WHITE,'#B8D7D6',3,radius=18)
    a.rect((580,125,740,330),PALE)
    a.rect((610,160,710,200),TEAL)
    a.arrow((175,230),(565,230))
    a.text(400,450,'The task comes forward',36)
    b=Drawing()
    b.text(400,36,'IN REFLECTION',36,TEAL)
    b.person(105,180,INK,1.1)
    b.rect((300,140,470,335),PALE,TEAL,5,radius=18)
    b.arrow((160,230),(280,230))
    for x,y,label in [(620,105,'Data'),(650,240,'Choices'),(620,375,'Effects')]:
        b.line([(475,230),(x-65,y)],ORANGE,4); b.text(x,y,label,32)
    b.text(400,450,'The context comes forward',34)
    return [('transparency-use',a),('transparency-context',b)]


def phone(a,x,kind):
    a.rect((x,80,x+300,425),WHITE,INK,4,radius=25)
    a.text(x+150,112,'Workshops',32)
    a.rect((x+20,145,x+280,250),PALE,radius=8)
    a.ellipse((x+45,170,x+95,190),ORANGE)
    a.rect((x+45,180,x+95,218),ORANGE,radius=8)
    a.text(x+180,183,'Ceramics',28)
    a.text(x+175,222,'Top pick',25,TEAL)
    if kind=='before':
        a.rect((x+20,280,x+280,330),TEAL,radius=10)
        a.text(x+150,305,'Book',28,WHITE)
    elif kind=='after':
        a.text(x+150,281,'Why this?',28,TEAL)
        a.rect((x+20,310,x+280,352),PALE,TEAL,radius=7)
        a.text(x+150,332,'Edit access needs',25)
        a.text(x+150,388,'Browse all',28,TEAL)
    else:
        a.rect((x+20,280,x+280,340),'#FCEADD',ORANGE,radius=8)
        a.text(x+150,310,'Access unknown',26)
        a.text(x+150,385,'Report / correct',27,TEAL)


def interface_panels():
    a=Drawing(); a.text(400,32,'BEFORE / ACCEPT',34,TEAL)
    phone(a,250,'before'); a.text(400,475,'Selection stays hidden',31)
    b=Drawing(); b.text(400,32,'AFTER / QUESTION + RESPOND',32,TEAL)
    phone(b,250,'after'); b.text(400,475,'Same model. More ways to act.',32)
    return [('workshop-before',a),('workshop-after',b)]


def responsibility_panels():
    a=Drawing(); a.text(400,32,'A WARNING IS NOT RECOURSE',32,TEAL)
    phone(a,245,'warning'); a.text(400,475,'Can someone recover a suitable option?',30)
    b=Drawing(); b.text(400,32,'DESIGNER RESPONSIBILITY REMAINS',30,TEAL)
    b.person(110,170,INK,.85)
    b.text(110,125,'Person',27)
    b.rect((290,130,490,310),PALE,TEAL,radius=18)
    b.text(390,180,'Usable',33); b.text(390,235,'control?',33)
    b.arrow((165,230),(275,230)); b.arrow((510,230),(615,230))
    b.person(685,170,TEAL,.85)
    b.text(685,125,'Designer',27,TEAL)
    b.line([(685,340),(685,385),(110,385),(110,335)],ORANGE,5)
    b.arrow((110,365),(110,335),ORANGE)
    b.text(400,475,'Check access, burden and consequences',30)
    return [('warning-recourse',a),('responsibility-loop',b)]


SPECS={
    'Learning is selective. Is it unfair?': (
        ['bias-assumptions','bias-pattern','bias-harm'],
        'Learning needs assumptions. Harm needs evidence.',
        'Original illustrations: alternative generalizations through points; schematic storefronts with repeated dark centres; unequal access outcomes. The storefront icons are not study outputs. The unequal outcomes are a question to investigate, not measured evidence.'),
    'Using a tool also shapes our experience.': (
        ['equipment-attention','mediated-perception','mediated-action'],
        'Related questions, not identical theories.',
        'Three original teaching schemas: absorbed task attention; amplification and reduction; shaped possibilities for action. Instructor diagrams, not original philosopher notation.'),
    'Transparent in which sense?': (
        ['transparency-use','transparency-context'],
        'Double vision: use the tool and examine its mediation.',
        'An attention arrow passes through faint equipment toward a task; a second makes the interface and its data, choices and effects focal. Instructor paraphrase of Van Den Eede use/context, not a transparency scale or model-internals diagram.'),
    'Pause. Compare. Choose differently.': (
        ['workshop-before','workshop-after'],
        'Illustrative interface; effectiveness is not established.',
        'Fictional workshop-finder before/after. The revised sketch exposes why a suggestion appears, editable access needs and browse-all. The model need not change; neither access labels nor these controls are validated.'),
    'Who might this revision miss?': (
        ['warning-recourse','responsibility-loop'],
        'Awareness alone is not a fairness fix.',
        'Fictional access-unknown warning and recourse control; a person-control-designer responsibility loop. This asks whether the person can recover a suitable option, rather than declaring the feature effective.'),
}


def generate():
    ASSETS.mkdir(parents=True,exist_ok=True)
    counts={}
    for fn in (bias_panels,relation_panels,transparency_panels,interface_panels,responsibility_panels):
        for name,drawing in fn(): counts[name]=drawing.save(name)
    return counts


def preserve_body(slide,description):
    prior=' '.join(r.text for e in slide.els if hasattr(e,'paras')
                   for p in e.paras for r in p.runs)
    slide.notes+='\n\nVisual revision: '+description+' Original projected explanation for teaching: '+prior
    kicker=next(e for e in slide.els if getattr(e,'y',None)==96)
    label=' '.join(r.text for p in kicker.paras for r in p.runs)
    # A two-column body can begin above y=330; rebuild the frame, not a y-cutoff.
    slide.els=content(label,slide.title,[],title_size=68).els


def storefront(slide):
    preserve_body(slide,'Historical source images from Lion, Concept Formation in Computational Creativity, chapter 5 Figures 5.1 and 5.3. Photograph credited to Miller and Lion (2022). The photograph is one study example, not the sole training input; the two 128px FastGAN samples are original historical outputs, not new generations. Provenance: deck/assets/week05-thesis-sources.md. Repeated dark centres illustrate a learned regularity, not evidence of discrimination.')
    base=Path(__file__).parent/'assets'
    slide.els += [
        T(120,350,800,45,'ONE STUDY PHOTOGRAPH','mono',29,TEAL),
        Image(120,415,800,420,str(base/'week05-thesis-storefront.jpg'),'contain',name='mediation-study-photo',placeholder='One study photograph of a Hong Kong storefront, not the sole training input.'),
        T(1000,350,800,45,'TWO HISTORICAL FASTGAN OUTPUTS','mono',28,TEAL),
        Image(1000,415,380,380,str(base/'week05-thesis-fastgan-1.jpg'),'contain',name='mediation-study-output-1',placeholder='First historical FastGAN storefront sample, original 128-pixel image.'),
        Image(1420,415,380,380,str(base/'week05-thesis-fastgan-2.jpg'),'contain',name='mediation-study-output-2',placeholder='Second historical FastGAN storefront sample, original 128-pixel image.'),
        T(120,875,1680,55,'Selected examples, not all humanity. Pattern does not establish discrimination.','body',32,INK),
        T(120,950,1680,35,'Lion / thesis ch.5, figs.5.1 + 5.3 / photograph: Miller & Lion (2022)','mono',21,TEAL),
    ]


def apply_visuals(slides):
    """Call before finalization; original explanations remain in native notes."""
    for slide in slides:
        key=slide.title.replace('\n',' ')
        if key=='Whose humanity does AI reflect?':
            storefront(slide)
        elif key in SPECS:
            names,takeaway,description=SPECS[key]
            preserve_body(slide,description)
            n=len(names); width=520 if n==3 else 800; gap=60 if n==3 else 80
            for i,name in enumerate(names):
                src=ASSETS/(name+'.png')
                if not src.exists(): raise FileNotFoundError(f'Regenerate visual assets: {src}')
                slide.els.append(Image(120+i*(width+gap),350,width,510,str(src),'contain',name='mediation-visual-'+name,placeholder=description))
            slide.els.append(T(120,900,1680,65,takeaway,'body',34,INK,lh=1.15,name='visual-takeaway'))


if __name__=='__main__':
    counts=generate()
    for title,(names,takeaway,_) in SPECS.items():
        print(sum(counts[n] for n in names)+len(takeaway.split()),title)
