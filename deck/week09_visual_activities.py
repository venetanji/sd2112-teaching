"""Short projected instructions; full facilitation remains in native notes."""
from deckgen import INK
from deckgen.layouts import T, Rect, content

TEAL = '#246E70'


def retain(slide):
    old = ' '.join(r.text for e in slide.els if hasattr(e,'paras') for p in e.paras for r in p.runs)
    slide.notes += '\nSupporting detail moved off the projection: ' + old


def steps(slide, items, caption):
    retain(slide)
    activity = slide.bg == '#F6AD00'
    if activity:
        slide.els = [e for e in slide.els if getattr(e,'y',999)<200]
        slide.els.append(T(120,230,1680,180,slide.title,'xbold',68,INK,lh=1.05))
    else:
        slide.els = content('WORK THROUGH THE COMPARISON',slide.title,[],title_size=68).els
    count=len(items); step=1680//count
    for i,(label,prompt) in enumerate(items):
        x=120+i*step
        slide.els += [Rect(x,450,step-35,325,'#FFFFFF' if activity else '#EAF2F2'),
                      T(x+24,470,step-85,80,f'{i+1:02d}','xbold',64,TEAL),
                      T(x+24,570,step-85,72,label,'xbold',36,INK,lh=1.05),
                      T(x+24,665,step-85,90,prompt,'body',30,INK,lh=1.15)]
        if i<count-1:
            slide.els.append(T(x+step-31,570,30,70,'>','mono',32,TEAL))
    slide.els.append(T(120,850,1680,110,caption,'body',34,INK,lh=1.2))


def apply_visuals(slides):
    for slide in slides:
        if slide.title == 'Find two examples of AI bias.':
            steps(slide,[('Find two','Documented or safe examples'),('Choose one','Compare the evidence'),
                         ('Question it','Who is affected? What is unknown?')],
                  'Keep: system + task + source/input + output + comparison. No personal data.')
        elif slide.title == 'Change how the person can respond.':
            steps(slide,[('Before','Sketch the current interaction'),('After','Make a choice visible and usable'),
                         ('Compare','20 min redesign + 10 min test plan')],
                  'Compare, question, correct, override or refuse. No new submission or deadline.')
        elif slide.title == 'What makes this an example of bias?':
            steps(slide,[('Observation','Compared with what?'),('Interpretation','Which pattern?'),
                         ('Consequence','Who is affected?'),('Uncertainty','What else explains it?')],
                  'A visible difference is a starting point, not yet an explanation.')
        elif slide.title == 'What changes in the interaction?':
            steps(slide,[('Original','One safe task'),('Revised','A meaningful response'),
                         ('Compare','Success, burden, exclusion')],
                  'Name a failure condition. Awareness alone is not a fairness fix.')
        elif slide.title == 'From spotting bias to changing the relation.':
            steps(slide,[('Show','Example + comparison'),('Explain','Consequence + uncertainty'),
                         ('Change','What can the person do now?')],
                  'Does the revision change agency, or just add a label?')
