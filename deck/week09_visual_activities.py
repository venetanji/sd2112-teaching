"""Short projected instructions; full facilitation remains in native notes."""
from deckgen import INK
from deckgen.layouts import T, Rect, content

TEAL = '#246E70'


def retain(slide):
    old = ' '.join(r.text for e in slide.els if hasattr(e,'paras') for p in e.paras for r in p.runs)
    slide.notes += '\nSupporting detail moved off the projection: ' + old


def steps(slide, items, caption, kicker='WORK THROUGH THE COMPARISON'):
    retain(slide)
    activity = slide.bg == '#F6AD00'
    if activity:
        slide.els = [e for e in slide.els if getattr(e,'y',999)<200]
        if slide.cp:
            slide.els[0].name = 'question-eyebrow'
        slide.els.append(T(120,230,1680,180,slide.title,'xbold',68,INK,lh=1.05))
    else:
        slide.els = content(kicker,slide.title,[],title_size=68).els
    count=len(items); step=1680//count
    for i,(label,prompt) in enumerate(items):
        x=120+i*step
        slide.els += [Rect(x,450,step-35,325,'#FFFFFF' if activity else '#EAF2F2'),
                      T(x+24,470,step-85,80,f'{i+1:02d}','xbold',64,TEAL),
                      T(x+24,570,step-85,72,label,'xbold',36,INK,lh=1.05),
                      T(x+24,665,step-85,90,prompt,'body',30,INK,lh=1.15)]
        if i<count-1:
            slide.els.append(T(x+step-31,570,30,70,'>','mono',32,TEAL))
    if slide.cp:
        slide.els.append(T(120,820,1340,155,caption,'body',30,INK,lh=1.15))
    else:
        slide.els.append(T(120,850,1680,110,caption,'body',34,INK,lh=1.2))


def apply_visuals(slides):
    for slide in slides:
        if slide.title == 'From an experience to a harmful-bias claim.':
            steps(slide,[('Observation','Auto-captions miss an accent.'),
                         ('Harm','Important instructions are lost.'),
                         ('Project','Could our project exclude speakers?')],
                  'Invented example, not a measured finding. Compare cases before claiming a pattern.',
                  kicker='90-105 / WORKED EXAMPLE / INVENTED, NOT STUDY DATA')
        elif slide.title == 'From a source to a mitigation proposal.':
            steps(slide,[('Research','Find evidence relevant to this harm.'),
                         ('Propose','Change data, model or interaction.'),
                         ('Check','Compare harm before and after.')],
                  'Caption example: test across accents + allow corrections. Proposals, not proven fixes.',
                  kicker='SAME 15-MINUTE PREPARATION / RESEARCH TO RESPONSE')
        elif slide.title == 'Where have you encountered harmful AI bias?':
            steps(slide,[('Recall','Your experience or a public case'),('Explain','What happened? Who was harmed?'),
                         ('Connect','Relate it to your project if possible')],
                  'One team text response. Personal disclosure is optional.\n'
                  'No names or private details. You may use a public case.\n'
                  'Responses may identify you; not anonymous. Ungraded.')
        elif slide.title == 'How could this harmful bias be reduced or removed?':
            steps(slide,[('Research','Find credible sources for this case'),('Suggest','Ways to reduce or remove the harm'),
                         ('Submit','Proposal + source/link + evidence + limit')],
                  'One team text response: 15 min research + 5 min synthesis.\n'
                  'No names or private details. Responses may identify you.\n'
                  'Not anonymous. Ungraded; no new Canvas deadline.')
        elif slide.title == 'What makes this an example of bias?':
            steps(slide,[('Observation','Compared with what?'),('Interpretation','Which pattern?'),
                         ('Consequence','Who is affected?'),('Uncertainty','What else explains it?')],
                  'A visible difference is a starting point, not yet an explanation.')
        elif slide.title == 'How would you check whether it helps?':
            steps(slide,[('Evidence','What does your source support?'),('Compare','Does the harm fall? For whom?'),
                         ('Limit','What would show the proposal failed?')],
                  'Name a failure condition. Awareness alone is not a fairness fix.')
        elif slide.title == 'From harmful bias to a researched response.':
            steps(slide,[('Example','Harm + project connection'),('Research','Proposed response + source'),
                         ('Uncertainty','What remains to be tested?')],
                  'Discuss public or non-identifying examples only. No third submission.')
