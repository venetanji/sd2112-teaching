"""
SD2112 · Artificial Intelligence in Design · Week 01 — the slide spec.

    python deck/week01.py            # builds docs/week01/, export/week01*.pptx, export/preview/
    python deck/week01.py --html     # only the html deck

One spec, three outputs (see tools/deckgen.py). Edit text here, rebuild, done.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures as F                                   # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, GREEN, BLUE, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, image_full, timeline,   # noqa: E402
                     journey, activity, video, assessment, team, two_col, figure_slide, finalize)

COURSE = 'SD2112'
FOOTER = 'SD2112 · AI IN DESIGN · WEEK 01'
SITE = 'venetanji.github.io/sd2112-teaching'
PLAYLIST = 'https://www.youtube.com/playlist?list=PLU58DFEI5YDQ'
A = ROOT / 'deck' / 'assets'
CHAIRS = [f'ai-chair-{i}.jpg' for i in range(1, 5) if (A / f'ai-chair-{i}.jpg').exists()] or [f'two-circles-{i}.png' for i in (36, 37, 38, 39)]
CIRCLES = [f'two-circles-{i}.png' for i in range(36, 48)]

S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 01 · LECTURE',
               'Artificial intelligence in design.',
               'Week 1 — the journey, and two ways to teach a machine.',
               notes='Welcome. Say the course code. ClassPoint join code is on the screen from 30 minutes before class; Nicolò and Amber are at the front helping people join. Everyone joins with the last four digits and the letter of their student ID.'))

S.append(agenda('SD2112 · WEEK 01', [
    'Why are we here?', 'Who are we?', 'The journey', 'What is AI?',
    'AI in design, now', "The designer's turn", 'Activity: teach the machine', 'How this course works',
], notes='Eight stops. Point out the interactive moments: five ClassPoint questions in the first half, the activity capture, and two at the end that tell us what you expect. About ninety minutes with a short break after stop four.'))

# ───────────────────────── 01 · why are we here ─────────────────────────
S.append(question('word_cloud', 'AI in design. One word.',
                  hint="The first word that comes to mind. No right answer — we read the biggest words aloud.",
                  eyebrow_text='01 · QUESTION · WORD CLOUD',
                  notes='ClassPoint word cloud, one word each. Leave it on screen for a minute. Read the three biggest words aloud and keep them — we come back to them at the end when we ask "what is your X". Expect: tool, cheating, fast, fake, future, Midjourney, ChatGPT.'))

S.append(section('01', 'Why are we here?', 'AI is in the tools, in the products, and in the job',
                 notes='Chapter one. Three reasons this course exists, all three are about you, not about the technology.'))

S.append(cards('01 · WHY ARE WE HERE', 'Three things changed', [
    ('THE TOOLS', 'Your tools have models inside them.',
     'Generative fill in Photoshop. Layouts in Figma. A brief written with a chatbot at 2 a.m. You already work with AI, whether you chose to or not.'),
    ('THE PRODUCTS', 'Your products have models inside them.',
     'Feeds, filters, recommendations, assistants. The thing you design increasingly decides, on its own, what each person sees. Someone has to design that.'),
    ('THE JOB', 'Your job is moving.',
     'From making every artefact by hand to choosing, briefing, curating and setting the rules. What a designer is for is being renegotiated this decade. Better to be in the room.'),
], notes='Tools, products, job. The first is about process — weeks 1 to 6. The second is about the product — weeks 8 to 12. The third is the question that runs underneath the whole course.'))

# ───────────────────────── 02 · who are we ─────────────────────────
S.append(section('02', 'Who are we?', 'Your team · and you', notes='Chapter two. The team first, then three quick questions about you.'))

S.append(content('02 · WHO IS TEACHING YOU', 'I study how machines form concepts.',
                 ['Giovanni Lion. PhD in computational creativity: how a machine ends up with an idea of "chair", and what that does to makers.',
                  '- Two years operating Sophia at Hanson Robotics. It rebooted minutes before a show. It came back.',
                  '- Musical Fruitstand: fruit you can play. A-Eye: the audience repainted live at M+. Featherman: a game with WWF Mai Po.',
                  '- One photo of me, three models, three styles.'],
                 images=['gio-avatar-1.jpg', 'gio-avatar-2.jpg', 'gio-avatar-3.jpg', 'ada-lovelace-generated.png'],
                 caption='Top: one photo of me through three image models. Bottom right: "Ada Lovelace at her machine", a diffusion model, 2025.',
                 body_size=30,
                 notes='Economics, then robotics, then a PhD on concept formation in computational creativity. The point of the avatars: the same photo through three models gives three different styles — the model, not the photo, decides the look. Ada at the bottom right is also generated; she is on the next slide as a real quote.'))

S.append(team('02 · YOUR TEAM THIS SEMESTER', 'Four people. Use them.', [
    ('Giovanni Lion', 'Lecturer', ['Lectures, briefs, grading. Questions in class first, then email.', 'giovannilion.link'], INK, 'GL', True),
    ('Nicolò', 'Teaching assistant', ['In the room **30 minutes before** and **30 minutes after** every class.', 'Tools, accounts, code, the weekly challenges. Also built the course video playlist.'], TEAL, 'N', False),
    ('Amber', 'Teaching assistant', ['In the room **30 minutes before** and **30 minutes after** every class.', 'Assignments, group project, feedback on your work in progress.'], ORANGE, 'A', False),
    ('ZHOU Zhibin', 'Class coordinator', ['Attendance and absences, admin, anything about the class as a whole.', '**Cannot come? Tell Zhibin before class.** That is what keeps your participation mark.'], VIOLET, 'ZZ', True),
], notes='Nicolò and Amber are here half an hour before and half an hour after every class — that hour is where laptops get fixed and assignments get unstuck. Zhibin coordinates: if you cannot come, tell Zhibin before class, not after. Participation is attendance plus ClassPoint activity.'))

S.append(question('multiple_choice', 'Which studio are you closest to?', [
    'Communication or advertising design', 'Product or industrial design', 'Interaction, digital or media design', 'Environment, interior, social — or something else',
], eyebrow_text='02 · WHO ARE YOU · MULTIPLE CHOICE',
    notes='ClassPoint multiple choice. Show the split. We use it to pick examples: if the room is mostly communication design we lean on type, layout and campaigns; if product, on chairs and parametric form; if interaction, on feeds and chatbots.'))

S.append(question('multiple_choice', 'How much have you used AI in your design work?', [
    'Never, or once to try it', 'Sometimes — for ideas, images, or text', 'Every week; it is part of my workflow', 'I have built something with a model or an API',
], eyebrow_text='02 · WHO ARE YOU · MULTIPLE CHOICE',
    notes='ClassPoint. This is the level check. If most of the room is A or B, weeks 4 and 5 go slower on the tools. If many are D, we pair them with beginners in the challenges. No judgement either way; say so.'))

S.append(question('multiple_choice', 'Have you written code?', [
    'No', 'A little — p5.js, Python, HTML or CSS', 'Comfortably',
], eyebrow_text='02 · WHO ARE YOU · MULTIPLE CHOICE',
    notes='ClassPoint. Week 2 has a small p5.js workshop: rules that make pictures. Nobody needs to know how to code, but we need to know how many do. If more than a third say C, the week-2 exercise gets a harder second half.'))

# ───────────────────────── 03 · the journey ─────────────────────────
S.append(section('03', 'The journey', '13 weeks · four modules · one question', notes='Chapter three: the whole semester on one slide, then the one question that runs through it.'))

S.append(journey('03 · THE SEMESTER', 'Where we are going', [
    dict(label='1 · What is AI?', color=TEALS[0], tint=TEALS[4], cells=[('Week 1', 'Two ways to teach a machine'), ('Week 2', 'Rules that make things: code, chance, generative art'), ('Week 3', 'Learning from examples: concepts, neurons, Move 37')]),
    dict(label='2 · AI for the creative process', color=VIOLETS[0], dark=True, tint=VIOLETS[5], cells=[('Week 4', 'Language machines: LLMs, prompts, agents'), ('Week 5', 'Image machines: diffusion, CLIP, mediation'), ('Week 6', 'Sound machines: music, voice, spectrograms')]),
    dict(label='Mid-term', color=PAPER, tint=PAPER, cells=[('Week 7', 'Mid-term quiz · project pitches · teams · reflection due')]),
    dict(label='3 · AI inside products', color=ORANGES[0], tint=ORANGES[4], cells=[('Week 8', 'AI as design material: use vs incorporate'), ('Week 9', 'Data, bias and privacy'), ('Week 10', 'Recommendation systems and the feed')]),
    dict(label="4 · The designer's turn", color=PINKS[0], dark=True, tint=PINKS[4], cells=[('Week 11', 'Curating outputs and datasets · authorship'), ('Week 12', 'Language as an interface: chatbots and agents')]),
    dict(label='Showcase', color=INK, dark=True, tint=PAPER, cells=[('Week 13', 'Poster fair — group projects'), ('Week 14', 'Final quiz')]),
], here=(0, 0), notes='Four modules. Weeks 1 to 3: what AI is, in two flavours — rules and examples. Weeks 4 to 6: the tools you will use in your own process; each week ends with a small making challenge. Week 7: quiz, pitches, teams. Weeks 8 to 10: AI as a material inside the product you design. Weeks 11 and 12: what is left for the designer. Week 13 poster fair. You are here.'))

S.append(quote('"The Analytical Engine has no pretensions whatever to originate anything. It can do whatever we know how to order it to perform."',
               'Ada Lovelace, Note G, 1843 — the first published program, for a machine that was never built',
               image='ada-lovelace-portrait.jpg', fit='cover', size=64,
               notes='1843. Lovelace writes the first program for Babbage\'s engine, and in the same notes the first objection to machine creativity: it only does what we order. Turing answered her in 1950; we spend thirteen weeks on the answer. The course question: can a machine originate a design? By week 13 you should have an answer you can defend, either way.'))

S.append(statement('Can a machine originate a design? By week 13 you will have an answer you can defend.', eyebrow_text='03 · THE QUESTION', size=104,
                   notes='Say it plainly. Either answer is acceptable in this course, as long as it is argued with what we learn. The reflection assignment is exactly this question, in your own practice.'))

# ───────────────────────── 04 · what is AI ─────────────────────────
S.append(section('04', 'What is AI?', 'A definition · two machines · one chair', notes='Chapter four. First their definitions, then ours, then the two machines.'))

S.append(question('short_answer', 'What is AI? One sentence, your own words.',
                  hint='Do not look it up. Write what you actually think it is.',
                  eyebrow_text='04 · QUESTION · SHORT ANSWER',
                  notes='ClassPoint short answer. Give it 90 seconds. Read four or five aloud, pick ones that disagree: "a program that thinks", "a tool that copies", "statistics". All of them are half right. Then our working definition.'))

S.append(statement('Intelligent-like output or behaviour, achieved through computation.', eyebrow_text='04 · A WORKING DEFINITION · GIO, 2025', size=110,
                   notes='Our working definition. Three words matter: "intelligent-like" — we judge the output, not the inside; "behaviour" — it can be an action, not only a picture; "computation" — it runs on a Turing machine, so it can be copied, scaled and sold.'))

S.append(content('04 · INTELLIGENT, OR CREATIVE?', 'Intelligent is not the same as creative.',
                 ['Wiggins, 2006: computational creativity is "the performance of tasks which, if performed by a human, would be deemed creative."',
                  'The trick: it judges the **output**, not the process.',
                  '- Intelligent: solves the problem you set.',
                  '- Creative: makes something you did not order, and you still want it.',
                  'Lovelace said the second is impossible. Hold that until Move 37.'],
                 image='alan-turing.png', fit='cover', body_size=30,
                 caption='Alan Turing. 1936: every computer is a Turing machine. 1950: "Can machines think?" becomes the imitation game.',
                 notes='Wiggins\' definition is agent-agnostic: creativity is in the eye of the audience. That is why this is a design question and not only an engineering one. Turing 1936 gives us the machine; 1950 replaces "can machines think" with the imitation game — judge the behaviour.'))

S.append(image_full('babbage-analytical-engine.jpg', '1837 · CHARLES BABBAGE · THE ANALYTICAL ENGINE',
                    'A computer is a physical thing: brass and steel, cut by hand. This one was designed and never finished. Lovelace programmed it anyway.',
                    notes='Babbage\'s Analytical Engine, trial model, Science Museum London. Physical, mechanical, made by craftsmen. A computer is a machine that follows rules — which is exactly what Lovelace meant.'))

S.append(statement('Two ways to teach a machine what a chair is.', eyebrow_text='04 · TWO MACHINES', size=124,
                   notes='The heart of the course, in one object. Chairs, because every design school has a chair canon and because everybody thinks they know what one is.'))

S.append(figure_slide('04 · TWO MACHINES', 'Write the rule, or show the examples.', F.two_machines(),
                      caption='Machine A: symbolic AI, 1956 onwards — definitions, logic, expert systems. Machine B: machine learning, 1958 / 1986 / 2012 — statistics over examples.',
                      notes='Left: give the machine a definition and it applies it. Exact, explainable, brittle — it will never accept a beanbag. Right: give it twelve thousand labelled photos and it develops a feel for chair-ness. Fluent, fuzzy, and it cannot tell you why. Every AI you will meet this semester is one of these, or a mix.'))

S.append(content('04 · MACHINE A · RULES', 'One rule. Twelve chairs.',
                 ['Every chair here comes from the same six numbers: seat height, seat width, back height, back angle, number of legs, splay.',
                  '- Change a number, get a chair. It can make a million and every one is a chair by definition.',
                  '- It can never make a beanbag. The definition does not know beanbags exist.',
                  'This is parametric design — Grasshopper, variable fonts, CSS grid. Week 2 is this: rules that make things.'],
                 figure=F.parametric_chairs(),
                 caption='chair(seat=0.45, width=0.62, back=0.6, angle=8, legs=4, splay=0.05) — the same function, twelve times',
                 body_size=30,
                 notes='Rules generate. Product designers know this as parametric design; type designers as variable fonts; web designers as a grid system. The strength and the limit are the same thing: nothing outside the rule can ever appear.'))

S.append(content('04 · MACHINE B · EXAMPLES', 'Ask a model for "a chair". Four times.',
                 ['No rule anywhere. A diffusion model saw millions of pictures with the word "chair" nearby and learned a feel for it.',
                  '- Four requests, four chairs, and they are all the **same** chair: four legs, a back, wood, a bit of mid-century.',
                  '- It cannot tell you why. It can tell you what is typical.',
                  'Weeks 3 and 5 are this: learning from examples, and what the examples do to the result.'],
                 images=CHAIRS,
                 caption='Prompt: "a chair, studio product photograph, plain white background" — one fast text-to-image model, four seeds, September 2026.',
                 body_size=30,
                 notes='Generated today with a small, fast model and the same prompt four times. Notice how similar they are. Nobody told the model what a chair is; it learned what is typical. That word — typical — is the bridge to the next slide.'))

S.append(activity('DRAW', '15 sec', 'Draw a chair. Fifteen seconds. Hold it up.',
                  ['Pen, paper, no thinking. When the time is up, hold the drawing above your head and look around the room.'],
                  bg=PAPER, eyebrow_text='04 · ONE MINUTE',
                  notes='Fifteen seconds. Then everyone holds it up. Almost every drawing is the same chair: four legs, a back, seen from the side or the front. That is the prototype — you did what the model did. Eleanor Rosch showed this in 1975: concepts are organised around typical members, not definitions.'))

S.append(figure_slide('04 · ROSCH, 1975 · TYPICALITY', 'Concepts have a middle and an edge.', F.typicality_scale(),
                      body=['Typical members are named first, learned first, recognised faster. The edge is where the definition breaks: is a bean bag a chair? a swing? the rock you sat on at lunch?'],
                      caption='Rosch & Mervis 1975 — family resemblance, not necessary and sufficient conditions. Machine A lives on the definition. Machine B lives in the middle. Designers work at the edge.',
                      notes='The rule-machine cannot hold the edge: any definition of chair either lets in the rock or throws out the beanbag. The example-machine lives in the middle: it reproduces the typical. Design is the art of leaving the prototype without leaving the concept — a chair that is still a chair, but nobody has seen. Neither machine does that on its own. Week 3 goes deeper: classical theory versus prototype theory, GOFAI versus connectionism.'))

S.append(content('04 · MACHINE B · AT THE EDGE', 'Ask for the edge. Get the middle.',
                 ['I asked the same model for "an object that is barely still a chair, an unusual seat that stretches the definition".',
                  '- It gave me this. A chair. Slightly more designed. Four legs and a back.',
                  '- A model trained on examples pulls towards the typical. The edge is where its examples run out.',
                  'The designer\'s job starts exactly where the model\'s confidence ends.'],
                 image='ai-chair-edge.jpg', fit='cover', body_size=30,
                 caption='Prompt: "an object that is barely still a chair, an unusual seat that stretches the definition of chair, studio product photograph". Same model, one seed.',
                 notes='The most honest slide in the deck: I asked for the edge and got the prototype. Bigger models do better, but the pull is the same. Prompting is negotiating with the middle; design is deciding where the edge is. Week 5 shows how to push a model off the prototype: references, ControlNet, fine-tuning on your own work.'))

S.append(question('multiple_choice', 'Which of these is a chair?', [
    'A bean bag', 'A tree stump you sit on', 'Both', 'Neither',
], eyebrow_text='04 · QUICK CHECK · MULTIPLE CHOICE',
    notes='ClassPoint. There is no correct answer and the split proves the point: the concept is fuzzy, and the room disagrees at the edge. Whoever wrote the rule on the previous slide has to live with the beanbag.'))

S.append(cards('04 · SAME APP, TWO MACHINES', 'You already use both, every day.', [
    ('PHOTOSHOP · 1990s', 'Auto Levels',
     'A rule: stretch the histogram until the darkest pixel is black and the lightest is white. Same input, same output, forever. Machine A.'),
    ('PHOTOSHOP · 2010', 'Content-Aware Fill',
     'An algorithm (PatchMatch) that searches the image for patches that fit the hole. Clever rules, no training. Still machine A.'),
    ('PHOTOSHOP · 2023', 'Generative Fill',
     'A diffusion model trained on Adobe Stock invents what belongs in the hole. Fluent, surprising, sometimes wrong. Machine B.'),
], notes='Three features, one menu, thirty years. Two are rule-based, one is learned. Ask: which one would you trust for a client\'s product shot, and why? The answer is a design decision, not a technical one. Week 3 makes this distinction precise: rule-based versus adaptive systems.'))

S.append(timeline('04 · HOW WE GOT HERE', 'Two lines, one hundred and eighty years.', [
    ('1843', 'Lovelace, Note G', 'The first program — and the first objection: it cannot originate.'),
    ('1950', 'Turing asks', '"Can machines think?" becomes: can you tell the difference?'),
    ('1965', 'Nake & Nees', 'A plotter draws from a program, in a gallery. Rules make art.'),
    ('1986', 'Backprop', 'Rumelhart, Hinton, Williams: networks learn from examples.'),
    ('2012', 'AlexNet', 'Deep learning wins at seeing. GPUs and the web made it possible.'),
    ('2016', 'Move 37', 'AlphaGo plays a move no human would. Creative, or alien?'),
    ('2022', 'ChatGPT · Stable Diffusion', 'Machine B reaches everyone, through a text box.'),
    ('2026', 'You', 'Both machines in every tool. The designer decides which, and when.'),
], notes='Two lines braided together: rules (Lovelace, Turing, Nake) and examples (backprop, AlexNet, diffusion). The second line took sixty years to work; it needed the web for data and gaming for GPUs. Week 2 is the rules line; week 3 the examples line.'))

S.append(image_full('nake-homage-to-paul-klee-1965.jpg', '1965 · FRIEDER NAKE · HOMAGE TO PAUL KLEE',
                    'A program drew this. Screenprint after a plotter drawing, 49 x 49 cm. It hangs in the V&A. Bense called it information aesthetics: beauty from rules, on purpose.',
                    fit='contain', bg=WHITE,
                    notes='1965, Stuttgart. Nake and Nees show plotter drawings in a gallery — the first computer art exhibition. Max Bense\'s idea: aesthetics as mathematics, art from a formal procedure. Notice the design move: the program, not the pencil, becomes the material. Week 2 you write one of these.'))

S.append(content('04 · MACHINE B · HOW IT LEARNS', 'A guess, a correction, a million times.',
                 ['Rosenblatt\'s perceptron, 1958: connections that adjust when the guess is wrong. Ignored for thirty years.',
                  '- 1986: backpropagation makes deep networks trainable (Rumelhart, Hinton, Williams). Hinton: Nobel Prize in Physics, 2024.',
                  '- 2012: AlexNet, trained on a million labelled photos, wins at seeing. The web gave the examples, gaming gave the chips.',
                  '- 2017: transformers, the architecture inside every chatbot. Week 4.'],
                 figure=F.perceptron(),
                 body_size=28,
                 notes='Keep this light: a network is a pile of adjustable connections; training is showing an example, measuring how wrong the guess was, and nudging every connection a little. Repeat a million times. The design point: the examples are the material. Who chose them? Week 9.'))

S.append(video('2016 · ALPHAGO · WATCH BEFORE WEEK 3', 'Move 37.', 'WXuK6gekU1Y',
               ['Game two against Lee Sedol. AlphaGo plays a move the commentators call a mistake. It was not.',
                '- Trained on human games, then on millions of games against itself. Nobody ordered move 37.',
                '- Lovelace\'s objection meets a counter-example. Or an alien way of thinking that only looks creative.',
                'Watch the documentary before week 3. It is on the course playlist.'],
               thumb='yt/WXuK6gekU1Y.jpg',
               notes='Play the move-37 chapter if there is time. Ask: is this creative? Wiggins says judge the output — the experts were astonished. The counter: it is intelligent, and alien, and has no idea what it did. This debate is week 3, and it is the debate under the whole course.'))

S.append(image_full('edmond-de-belamy.jpg', '2018 · OBVIOUS · EDMOND DE BELAMY',
                    'Sold at Christie\'s for US$432,500. Signed, bottom right, with the loss function of the network that made it. Who is the author? Week 11.',
                    notes='Belamy, 2018: a GAN trained on 15,000 portraits; the signature is the training formula. Christie\'s sold it for 432,500 dollars. The authorship question — the collective, the coder who wrote the model, the painters in the dataset — is week 11.'))

# ───────────────────────── 05 · AI in design, now ─────────────────────────
S.append(section('05', 'AI in design, now', 'Using it · incorporating it · three cases', bg=ORANGES[0],
                 notes='Chapter five: the distinction that organises the semester, and three cases from the last two years.'))

S.append(cards('05 · THE DISTINCTION THAT ORGANISES THE COURSE', 'Using AI, or incorporating AI.', [
    ('WEEKS 1 – 6 · THE PROCESS', 'Using AI',
     ['AI as a tool in **how** you design: a brief drafted with a chatbot, a moodboard from a diffusion model, generative fill, layouts from Figma Make.',
      'You stay the author. You become the curator, the briefer, the editor.']),
    ('WEEKS 8 – 12 · THE PRODUCT', 'Incorporating AI',
     ['AI as a material in **what** you design: a feed, a recommendation, an assistant, a filter — the product decides something for each person, on its own.',
      'You design a behaviour, not a picture. Data, bias, trust and accountability become design problems.']),
], notes='Using versus incorporating. Using is about practice — how you make. Incorporating is about the outcome — what you make. The first half of the course is the first, the second half the second. The designer\'s role is different in each: curator versus system architect.'))

S.append(cards('05 · THREE CASES', 'What it looks like when it ships.', [
    ('USING · 2024', 'Coca-Cola remakes its holiday ad with generative video',
     'The trucks, the snow, the faces: made with generative video tools and finished by hand. Viewers noticed — the reception split. What did the audience see that the model did not? Craft is now a question of what you let through.'),
    ('INCORPORATING · SINCE 2017', 'Netflix chooses a different poster for each viewer',
     'The same film, several pieces of artwork; a model picks the one you are most likely to click. The poster designer no longer makes one image — they design a **space** of images and the rules for choosing.'),
    ('AI AS THE PRODUCT · 2024–25', 'The Humane AI Pin',
     'A wearable whose entire interface was an assistant. Beautiful hardware, launched at US$699, discontinued within a year. A model is not a product. The interaction, the trust and the failure states still have to be designed.'),
], text_size=24, notes='Three cases, three roles. Coca-Cola: using — and the audience judged the craft. Netflix: incorporating — the designer designs a space of options and a rule for choosing. Humane: AI as the whole product — a warning that a model is not an experience. Ask the room for one more case from the last month; there is always one.'))

S.append(question('short_answer', 'Where did AI touch your design work this week?',
                  hint='One example: a tool you used, a feed that chose for you, a product that answered back. A link if you have one.',
                  eyebrow_text='05 · QUESTION · SHORT ANSWER',
                  notes='ClassPoint short answer, two minutes. This replaces the old scavenger hunt: everyone has an example on their phone. Sort a few live into "using" and "incorporating". Keep the list — it seeds the week-3 categorising exercise.'))

S.append(content('05 · THE COURSE PLAYLIST · BY NICOLÒ', 'Fifteen videos, in the order we need them.',
                 ['[youtube.com/playlist?list=PLU58DFEI5YDQ](https://www.youtube.com/playlist?list=PLU58DFEI5YDQ)',
                  '- **Before week 3:** AlphaGo. Illiac Suite (1957), Cage\'s Water Walk (1960), Tinguely\'s Homage to New York (1960), Kaprow\'s Fluids (1967).',
                  '- **Week 4:** large language models, explained briefly (3Blue1Brown).',
                  '- **Week 5:** diffusion, how AI images work, CLIP, autoencoders, UNet, text-to-video, ComfyUI.',
                  '- **Week 6:** AI sound and music. **Week 12:** generative vs rules-based chatbots.'],
                 image='yt/gXOIkT1-QWY.jpg', fit='cover',
                 caption='John Cage, Water Walk, 1960: a score of timed instructions, performed on live television. Rules, chance and a bathtub.',
                 body_size=28,
                 notes='Nicolò compiled the playlist from every video in the slides. Each week names the ones to watch before class; quizzes draw on them. This week: AlphaGo, and the four art pieces — they are short, and they are week 2\'s argument that art has been made from rules and chance since before computers.'))

# ───────────────────────── 06 · the designer's turn ─────────────────────────
S.append(section('06', "The designer's turn", 'Technology is never neutral · neither is design', bg=PINKS[0],
                 notes='Chapter six, short: the philosophical spine of the course, in three slides. Verbeek is the reading for week 5.'))

S.append(quote('"Designing things is designing human existence."',
               'Peter-Paul Verbeek, Beyond Interaction: A Short Introduction to Mediation Theory, Interactions, 2015 — the reading for week 5',
               size=88,
               notes='Verbeek, 2015, written for interaction designers. Technologies do not sit between a ready-made human and a ready-made world; they shape both. The double-sided printer default decides how much paper a company uses. A feed decides what a city talks about. Designers materialise morality.'))

S.append(figure_slide('06 · IHDE · VERBEEK · TECHNOLOGICAL MEDIATION', 'The thing in between is never neutral.', F.mediation(),
                      body=['You do not see the world and then use a tool. You see the world through the tool: glasses, a camera, a feed, a fill. Week 5 gives you Ihde\'s four relations and a vocabulary for designing them.'],
                      caption='Ihde 1990, Verbeek 2015. Embodiment (through), hermeneutic (reading), alterity (facing), background — and the AI versions of each.',
                      notes='Don Ihde\'s human – technology – world. Every AI feature sits in the middle and changes both ends: what you perceive and what you do. When the filter picks the poster, the viewer\'s world has been designed. Week 5 works through the four relations with AI examples; the group project asks you to name which one you are building.'))

S.append(cards('06 · WHAT IS LEFT FOR YOU', 'Designers as…', [
    ('OUTPUTS', 'Curators of what ships',
     'A model makes a hundred. You choose one, and you answer for it. Not everything generated should be released.'),
    ('DATASETS', 'Curators of what it learns',
     'Choose the examples and you choose the prototype. Fine-tune on your own work and the model learns your edge, not the internet\'s middle. Week 11.'),
    ('RULES', 'Setters of guardrails',
     'Decide what the machine may not do, when a human must be in the loop, how it fails in front of a person. Machine A protecting people from machine B.'),
    ('STORY', 'Tellers of the process',
     'Clients, users and juries will ask how it was made. Documenting the human decisions is now part of the design. Your reflection starts this.'),
], notes='Four roles, all four graded in this course: the reflection is the story, the group project is outputs plus rules, week 11 is datasets. The old fear — "will AI replace designers" — is the wrong question. The right one: which of these four do you want to be good at?'))

# ───────────────────────── 07 · activity ─────────────────────────
S.append(section('07', 'Teach the machine what a chair is', '8 minutes · pen and paper · no software', bg=YELLOWS[0],
                 notes='The activity. Think-pair-square: one minute alone, two in pairs, four in fours, then one line per four into ClassPoint. TAs walk the room and keep time.'))

S.append(activity('1 — ALONE', 1, 'Write the rule.',
                  ['Define "chair" so that a machine could apply it, with no judgement of its own. One sentence: **X is a chair if ___.**',
                   'Be strict. A rule that admits everything is useless. Pen and paper, silent.'],
                  bg=YELLOWS[0],
                  notes='One minute, silent, paper. Necessary and sufficient conditions — the classical theory of concepts, though they do not need the name yet.'))

S.append(activity('2 — IN PAIRS', 2, 'Break the rule.',
                  ['Swap sentences with your neighbour. Find **one thing that passes their rule and is not a chair**, and **one chair that fails it.**',
                   'Write both down under the rule. Whoever\'s rule survives longest wins nothing; the point is that neither survives.'],
                  bg=YELLOWS[1],
                  notes='Two minutes. Typical breakers: the rock, the beanbag, the swing, the wheelchair, the throne, a sofa cut in half. The point lands when they see that every rule leaks at the edge.'))

S.append(activity('4 — TWO PAIRS', 4, 'Now teach it with examples instead.',
                  ['Join the pair behind you. Four people, one machine. Pick the **five photographs** you would show it to teach "chair". Then one **hard no**: something that looks like a chair and is not.',
                   'Decide together: what does the machine learn if all five are office chairs? Whose chairs are missing? One person writes.'],
                  bg=YELLOWS[2],
                  notes='Four minutes in fours. This is dataset curation. Push them: five examples is a design decision — which cultures, which centuries, which bodies. The hard negative is the guardrail. One scribe per four.'))

S.append(question('short_answer', 'Scribes only. One line per four.',
                  hint='RULE broke on: ___ · FIVE EXAMPLES: ___ · HARD NO: ___',
                  example='e.g. "broke on: a swing · examples: Thonet 14, monobloc, a throne, a wheelchair, a kindergarten chair · hard no: a stepladder"',
                  eyebrow_text='07 · CAPTURE · 2 MIN · SHORT ANSWER',
                  cp={'type': 'short_answer', 'hide_names': False, 'multiple': False},
                  notes='ClassPoint short answer, scribes only: about 28 lines, not 114. Read three aloud. Keep them: week 3 uses the rules as classical-theory examples, week 9 uses the example lists as a bias exercise.'))

S.append(content('07 · WHAT JUST HAPPENED', 'You built both machines.',
                 ['Eight minutes, no software. The rule-writers hit every problem of the classical theory of concepts — Plato\'s problem, fuzziness, the counter-example. Week 3.',
                  'The example-pickers hit dataset bias and curation: five chairs decide what "chair" means. Weeks 9 and 11.',
                  'A machine can apply the rule. A machine can learn from the examples.',
                  '**It cannot decide which examples. That was you.**'],
                 body_size=34,
                 notes='Mirror of the whole course. The rule and the examples are both machines; the choice of examples and the choice of rule are design. Say the last line slowly.'))

# ───────────────────────── 08 · how this course works ─────────────────────────
S.append(section('08', 'How this course works', 'Assessment · assignments · weekly challenges · rules', bg=VIOLET,
                 notes='Chapter eight: the admin. Five components, two assignments, the weekly challenges, the rules on attendance and on AI use.'))

S.append(assessment('08 · ASSESSMENT', 'Five components.', [
    ('10%', 'Participation', 'Come to class, or tell Zhibin before you cannot. Answer in ClassPoint. Stars count.', False),
    ('20%', 'Individual reflection', 'Weeks 1–6: experiment with AI in your own process. ~1000 words, due week 7.', False),
    ('10%', 'Mid-term quiz', 'Multiple choice, week 7. Concepts from weeks 1–6 and the playlist.', False),
    ('40%', 'Group project', 'Design a product that incorporates AI. Poster A0 + 3–5 min video + one-page mediation brief. Poster fair, week 13.', True),
    ('20%', 'Final quiz', 'Multiple choice, week 14. The whole course.', False),
], notes='Five parts. The group project is the big one; it starts in week 7 when teams form. Quizzes are multiple choice and draw on the lectures and the playlist. Participation: attendance plus ClassPoint stars — being here and answering.'))

S.append(content('08 · INDIVIDUAL REFLECTION · 20% · DUE WEEK 7', 'Use AI in your own process for six weeks. Then argue.',
                 ['**Topic:** the role of AI in your creative process — with particular attention to the difference between rule-based and adaptive systems.',
                  '- About 1000 words, submitted on Blackboard.',
                  '- Evidence: at least three of your own experiments from the weekly challenges, with images.',
                  '- A short **process note** at the end: how you used AI to make the reflection itself. Allowed, expected, disclosed.',
                  'Graded on understanding (30), argument (30), evidence (20), clarity (10), originality (10). Rubric on Blackboard.'],
                 body_size=32,
                 notes='The reflection is the course question in your own practice. The two machines are the lens: which of your tools are rules, which are learned, and what did each do to your process. Three experiments minimum — the weekly challenges give you five. AI use in writing it is fine and must be disclosed.'))

S.append(content('08 · GROUP PROJECT · 40% · DUE WEEK 13', 'Design a product that incorporates AI.',
                 ['Teams of four to five, formed in week 7. A product or service in which a model **decides something for each person** — and your account of what that does to them.',
                  '- **Poster, A0:** the research and the design concept, shown at the poster fair.',
                  '- **Video, 3–5 min:** how the product works, for someone who has never seen it.',
                  '- **Mediation brief, one page:** which human–technology relation you are building, what data it needs, where it is biased, and the guardrails.',
                  'Rubric: research and context (30), ethical and social impact (30), poster (20), video (10), teamwork and process (10).'],
                 body_size=32,
                 notes='Forty percent. Not a prototype competition: the rubric rewards research depth and the ethical account more than polish. The mediation brief is new this year: one page that names the relation (Ihde), the data, the bias and the guardrails — the vocabulary of weeks 5, 9 and 11.'))

S.append(cards('08 · WEEKLY CHALLENGES · WEEKS 2 – 6', 'Make one thing a week.', [
    ('WEEK 2', 'A picture from rules', 'A p5.js sketch. One rule, one random number, your own picture.'),
    ('WEEK 3', 'A dataset of ten', 'Ten images that teach a machine one concept from your studio. Say what it would learn wrong.'),
    ('WEEK 4', 'A brief, automated', 'A design brief drafted by a language model from your prompt, then edited by you. Show both.'),
    ('WEEK 5', 'An image you could not draw', 'Generated, iterated, and critiqued: what did the model decide that you did not?'),
    ('WEEK 6', 'Thirty seconds of sound', 'A sound or music snippet for a product. Where did control stay with you?'),
], head_size=30, text_size=22, notes='Small, weekly, low stakes. Bring it to the next class; the room votes; the winners get shown and a participation star. All five become evidence for the reflection. Nicolò and Amber help before and after class.'))

S.append(cards('08 · THE RULES', 'Three rules.', [
    ('ATTENDANCE', 'Come, or say so before.',
     'Participation is attendance plus ClassPoint. If you cannot come, tell ZHOU Zhibin before the class starts. Silent absence costs the mark; a message does not.'),
    ('AI USE', 'Allowed. Disclosed. Yours.',
     'Use any model, in any assignment. Say which, and how, in a process note. You are the author: you answer for accuracy, for sources, and for taste. Invented citations fail the assignment.'),
    ('ROOM', '30 minutes before, 30 after.',
     'Nicolò and Amber are in the room before and after every class. Laptops, accounts, tools, drafts. That hour is the tutorial.'),
], notes='Three rules, no small print. The AI rule is the important one: allowed and disclosed, and you remain responsible. The TA hour before and after class is where the practical help lives.'))

S.append(content('08 · BEFORE NEXT WEEK', 'Four things to set up, one thing to watch.',
                 ['- **ClassPoint:** you are in. Same name every week — the last four digits and the letter of your student ID, e.g. 8695D.',
                  '- **Blackboard:** the course page, submissions, the rubric, these slides.',
                  '- **p5.js web editor:** a free account at editor.p5js.org. Week 2 is rules that draw.',
                  '- **One image tool** you can log into: Firefly, Bing Image Creator, or another. Week 5 needs it; week 3 helps to have it.',
                  '- **Watch:** AlphaGo (90 min) and the four short art films on the playlist. Bring a laptop next week.'],
                 body_size=32,
                 notes='Concrete homework. The slides live on the course site and on Blackboard. The AlphaGo film is the one long thing; the four art films are short.'))

S.append(question('word_cloud', "What's your X? One word.",
                  hint='What do you want to make with AI this semester? A poster, a chair, a game, a brand, a film, a service — one word.',
                  eyebrow_text='08 · QUESTION · WORD CLOUD',
                  notes='ClassPoint word cloud to close, like the opening one. Compare the two clouds: the first was what AI is; this is what you want from it. Screenshot both — they go into the week 2 recap.'))

S.append(question('short_answer', 'One hope and one worry.',
                  hint='About AI in your own design work. Names are hidden. Two short lines.',
                  eyebrow_text='08 · QUESTION · SHORT ANSWER · ANONYMOUS',
                  cp={'type': 'short_answer', 'hide_names': True, 'multiple': False},
                  notes='Anonymous. This is the expectation check: read the worries, not the hopes. Common ones — cheating, losing skills, copyright, jobs — each maps to a week. Tell them which.'))

S.append(end('See you next week. Rules that make things.',
             'Bring a laptop. Watch AlphaGo. Draw another chair.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: rules that make things — Nake, Nees, LeWitt, Cage, and your first p5.js sketch. Nicolò and Amber stay for 30 minutes.'))

DECK = dict(title='SD2112 · AI in Design · Week 01', slides=finalize(S, FOOTER))

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week01', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')
