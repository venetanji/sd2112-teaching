"""Original, reproducible Week 9 teaching illustrations (not study evidence).

Run this module with the course Python to regenerate its PNG assets. No external
images, copyrighted film posters, user records or generative service are used.
"""
from pathlib import Path
import math

import deckgen
from deckgen.core import Image
from deckgen.layouts import content, T
from PIL import Image as PILImage, ImageDraw, ImageFont

ASSETS = Path(__file__).parent / 'assets/week09/visual-mechanisms'
INK, TEAL, ORANGE = '#000B1C', '#246E70', '#ED6D24'
PALE, GRAY = '#EAF2F2', '#68747E'
FONT = Path(deckgen.__file__).parent / 'fonts/Inter-Variable.ttf'


def font(size):
    return ImageFont.truetype(str(FONT), size)


def label(draw, xy, text, size=42, fill=INK, anchor='mm'):
    draw.text(xy, text, font=font(size), fill=fill, anchor=anchor)


def arrow(draw, start, end, fill=TEAL, width=8):
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    points = [end] + [(end[0] - 23 * math.cos(angle + delta),
                       end[1] - 23 * math.sin(angle + delta))
                      for delta in (-.48, .48)]
    draw.polygon(points, fill=fill)


def canvas(w=840, h=540):
    image = PILImage.new('RGB', (w, h), '#FFFFFF')
    return image, ImageDraw.Draw(image)


def save(image, name):
    ASSETS.mkdir(parents=True, exist_ok=True)
    image.save(ASSETS / (name + '.png'))


def film(draw, box, variant):
    """Original film-poster-like thumbnails: scene geometry, no actual film."""
    x, y, w, h = box
    draw.rounded_rectangle((x, y, x+w, y+h), radius=22, fill=INK)
    for sx, sy in ((.15,.18),(.78,.12),(.88,.45),(.25,.4),(.56,.22)):
        draw.ellipse((x+w*sx-3,y+h*sy-3,x+w*sx+3,y+h*sy+3),fill='#FFFFFF')
    draw.ellipse((x+w*.35,y+h*.18,x+w*.67,y+h*.51),fill='#64C2C3')
    draw.polygon([(x,y+h),(x+w*.24,y+h*.57),(x+w*.52,y+h*.86),
                  (x+w*.82,y+h*.51),(x+w,y+h*.72),(x+w,y+h)], fill=TEAL)
    if variant:
        draw.rectangle((x+w*.43,y+h*.62,x+w*.6,y+h*.9),fill='#F0C2A5')
        draw.ellipse((x+w*.39,y+h*.54,x+w*.64,y+h*.69),fill=ORANGE)
    else:
        draw.ellipse((x+w*.43,y+h*.63,x+w*.61,y+h*.9),fill='#F0C2A5')


def films():
    for name, heading, variant in [('film-liked','LIKED',False),
                                    ('film-candidate','CANDIDATE',True)]:
        im,d = canvas()
        label(d,(420,42),heading,36,TEAL)
        film(d,(60,100,320,365),variant)
        for i, text in enumerate(('SCI-FI','QUIET','SLOW')):
            y=160+i*105
            d.rounded_rectangle((420,y-35,800,y+35),radius=30,fill=PALE)
            label(d,(610,y),text,42)
        save(im,name)


def vectors():
    im,d = canvas()
    ox,oy,scale=160,430,320
    # Coordinates are exactly Q=(1,0), A=(.8,.6), B=(0,1).
    arrow(d,(ox-25,oy),(750,oy),GRAY,3)
    arrow(d,(ox,oy+25),(ox,55),GRAY,3)
    d.arc((ox-scale,oy-scale,ox+scale,oy+scale),270,360,fill='#BCD1D1',width=4)
    for text,point,color in [('Q',(1,0),INK),('A',(.8,.6),ORANGE),('B',(0,1),TEAL)]:
        ex,ey=ox+scale*point[0],oy-scale*point[1]
        arrow(d,(ox,oy),(ex,ey),color,8)
        d.ellipse((ex-9,ey-9,ex+9,ey+9),fill=color)
        pos={'Q':(ex+45,ey-30),'A':(ex+40,ey-30),'B':(ex+40,ey)}[text]
        label(d,pos,text,54,color)
    label(d,(ox-35,oy+30),'0',30,GRAY)
    label(d,(470,500),'HAND-SET / NOT LEARNED',32,TEAL)
    save(im,'unit-vectors')


def goal_proxy():
    im,d=canvas()
    label(d,(420,42),'HUMAN GOAL',36,TEAL)
    # Hands-on workshop scene: two participants and a completed object.
    d.rounded_rectangle((75,95,765,450),radius=28,fill=PALE)
    for x in (240,600):
        d.ellipse((x-39,145,x+39,223),fill=INK)
        d.rounded_rectangle((x-62,234,x+62,355),radius=28,fill=TEAL)
    d.rectangle((125,330,715,365),fill='#B68B67')
    d.rectangle((155,365,180,430),fill='#B68B67')
    d.rectangle((660,365,685,430),fill='#B68B67')
    d.polygon([(365,330),(380,285),(450,285),(475,330)],fill=ORANGE)
    d.arc((384,254,451,309),180,360,fill=ORANGE,width=12)
    label(d,(420,493),'Make something useful.',43)
    save(im,'workshop-goal')
    im,d=canvas()
    label(d,(420,42),'SYSTEM PROXY',36,TEAL)
    d.rounded_rectangle((175,95,665,450),radius=28,fill=INK)
    d.rounded_rectangle((200,120,640,425),radius=10,fill='#FFFFFF')
    d.rectangle((220,145,620,260),fill=ORANGE)
    label(d,(420,203),'CLICK!',70,'#FFFFFF')
    for y,w in ((292,340),(322,250),(352,300)):
        d.rounded_rectangle((235,y,235+w,y+12),radius=5,fill='#D9E1E4')
    d.polygon([(515,320),(515,405),(537,386),(558,425),(578,414),
               (557,376),(586,371)],fill=INK)
    label(d,(420,493),'A click can mislead.',43)
    save(im,'workshop-proxy')


def feedback():
    im,d=canvas(1680,540)
    nodes=[(290,130,'EXPOSURE'),(1260,130,'CHOICE'),
           (1260,410,'SIGNAL'),(290,410,'NEXT FEED')]
    arrow(d,(555,130),(995,130))
    arrow(d,(1260,205),(1260,335))
    arrow(d,(995,410),(555,410))
    arrow(d,(290,335),(290,205))
    for x,y,text in nodes:
        d.rounded_rectangle((x-245,y-68,x+245,y+68),radius=28,fill=PALE)
        label(d,(x,y),text,58)
    label(d,(780,270),'PEOPLE MAY CHANGE TOO',43,TEAL)
    save(im,'feedback-loop')


def thumbnail(d, box, kind):
    x,y,w,h=box
    d.rounded_rectangle((x,y,x+w,y+h),radius=12,fill=PALE)
    if kind==0:
        d.ellipse((x+w*.25,y+h*.15,x+w*.75,y+h*.85),fill=ORANGE)
        d.rectangle((x+w*.25,y+h*.15,x+w*.75,y+h*.3),fill=PALE)
    elif kind==1:
        d.polygon([(x+w*.1,y+h*.85),(x+w*.45,y+h*.15),
                   (x+w*.6,y+h*.55),(x+w*.8,y+h*.3),(x+w*.95,y+h*.85)],fill=TEAL)
    else:
        d.rectangle((x+w*.2,y+h*.3,x+w*.8,y+h*.72),fill=INK)
        d.ellipse((x+w*.4,y+h*.35,x+w*.62,y+h*.65),fill='#64C2C3')
        d.rectangle((x+w*.3,y+h*.2,x+w*.5,y+h*.3),fill=INK)


def diversity():
    for name,heading,varied in [('feed-repeat','ONE PATTERN',False),
                                 ('feed-varied','MORE DIMENSIONS',True)]:
        im,d=canvas()
        label(d,(420,42),heading,36,TEAL)
        for i in range(3):
            x=35+i*270
            thumbnail(d,(x,110,230,210),i if varied else 0)
            text=['TOPIC','CREATOR','FORMAT'][i] if varied else 'POTTERY'
            label(d,(x+115,370),text,34)
            d.ellipse((x+85,420,x+145,480),fill=[TEAL,ORANGE,INK][i] if varied else TEAL)
        save(im,name)


def regenerate():
    films(); vectors(); goal_proxy(); feedback(); diversity()


def _image(name,x,y,w,h,alt):
    return Image(x,y,w,h,str(ASSETS/(name+'.png')),'contain',
                 name='mechanism-illustration',placeholder=alt)


def _pair(left,right,alt_left,alt_right):
    return [_image(left,120,335,810,520,alt_left),
            _image(right,990,335,810,520,alt_right)]


def apply_visuals(slides):
    """Replace five dense slide bodies; retain the explanation in native notes."""
    specs = {
        'Similar to what you liked.': ('CONTENT MATCHING / INVENTED FILMS',
            _pair('film-liked','film-candidate',
                  'An original quiet science-fiction film illustration, tagged sci-fi, quiet, slow.',
                  'A different original film illustration with matching sci-fi, quiet, slow features.'),
            'Matching features suggest a candidate, not tonight\'s perfect film.'),
        'Near depends on the representation.': ('EMBEDDINGS / TOY GEOMETRY',[
            _image('unit-vectors',120,335,810,520,
                   'Unit vectors Q=(1,0), A=(0.8,0.6), B=(0,1). A points nearer Q than B.'),
            T(1020,390,780,74,'Q = [1, 0]','monomed',40,INK),
            T(1020,490,780,112,'A = [0.8, 0.6]\ncosine(Q,A) = 0.8','body',38,ORANGE),
            T(1020,635,780,112,'B = [0, 1]\ncosine(Q,B) = 0','body',38,TEAL)],
            'Near does not mean true, fair or suitable.'),
        'A click is not the user goal.': ('VALUE / MEASURE',
            _pair('workshop-goal','workshop-proxy',
                  'Two people making an object together: the goal is a useful workshop.',
                  'A pointer clicking a bright event card: the measurable proxy is a click.'),
            'Measure task success, not just clicks.'),
        'The next screen changes the next data.': ('FEEDBACK / CONCEPTUAL LOOP',[
            _image('feedback-loop',120,335,1680,540,
                   'Exposure leads to choice, recorded signal and the next feed, which changes exposure.')],
            'Possible feedback, not a measured universal law.'),
        'Diversity is a decision to specify.': ('EXPOSURE / ILLUSTRATIVE FEEDS',
            _pair('feed-repeat','feed-varied',
                  'Three repeated pottery cards and the same creator marker.',
                  'Varied original pottery, landscape and camera images with different creator markers.'),
            'More variety is not proof of reduced polarization.'),
    }
    for heading,(kicker,body,takeaway) in specs.items():
        matches=[s for s in slides if s.title.replace('\n',' ')==heading]
        if len(matches)!=1:
            raise ValueError(f'Expected one mechanism slide: {heading}')
        slide=matches[0]
        old=' '.join(r.text for e in slide.els if hasattr(e,'paras')
                     for p in e.paras for r in p.runs)
        slide.notes += (' Original projected explanation retained after visual revision: '+old+
            ' Visual provenance: original instructor-authored geometric illustrations, generated '
            'by week09_visual_mechanisms.py with Pillow. Fictional films, workshop and feeds; '
            'no study data, real interface screenshot or empirical outcome is depicted.')
        frame=content(kicker,heading,[],title_size=68,notes=slide.notes)
        frame.els += body + [T(120,900,1680,78,takeaway,'body',36,INK,
                               name='mechanism-takeaway')]
        slide.els=frame.els
        slide.bg=frame.bg


if __name__ == '__main__':
    regenerate()
