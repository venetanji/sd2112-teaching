"""
SD2112 · Artificial Intelligence in Design · Week 04 — the slide spec.

From explicit rules to learned language models to systems that act through tools.
The class opens with the machine A / machine B distinction, then moves from
Chomsky and ELIZA through RNNs, transformers and question-answering to agent
loops and the harness around them. The exercise follows the lecturer's live
harness demonstrations: one bounded design task, one observed run, one revision.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import week04_figures as W4                          # noqa: E402
from deckgen import attach_reports, build_all, INK, PAPER, VIOLET, YELLOWS  # noqa: E402
from deckgen.layouts import (title, end, agenda, section, statement, content, cards, question,
                             journey, activity, two_col, image_full, live, sketch_slide,
                             Rect, T, eyebrow, finalize)
from deckgen.core import Image
from course import SITE, PLAYLIST, JOURNEY, footer     # noqa: E402


FOOTER = footer(4)
HERE = Path(__file__).resolve().parent
S = []


def full_diagram(eyebrow_text, title_text, figure, notes='',
                 header_bg=PAPER, eyebrow_color=None, title_color=None):
    """Keep diagrams large while laying their header and title in deck-native text."""
    _svg, png = figure
    slide = image_full(png, '', '', notes=notes, fit='contain', bg=PAPER)
    image = slide.els[0]
    text_color = title_color or INK
    header_text_color = eyebrow_color or '#5C6470'
    slide.els = [
        image,
        Rect(120, 40, 1680, 180, header_bg),  # covers the older raster heading/title
        eyebrow(120, 78, eyebrow_text, header_text_color),
        T(120, 126, 1680, 80, title_text, 'xbold', 54, text_color,
          lh=0.96, spc=-0.03),
    ]
    slide.chrome = True
    return slide


def visual_flow(eyebrow_text, title_text, steps, takeaway, notes='', loop=False):
    """Large native text and shapes: the complete diagram occupies the slide body."""
    slide = content(eyebrow_text, title_text, [], notes=notes, title_size=60, bg=PAPER)
    slide.els = slide.els[:2]
    for i, (label, heading, body) in enumerate(steps):
        x = 120 + i * 580
        slide.els += [Rect(x, 350, 520, 420, '#FFFFFF'),
                      T(x+32, 380, 456, 55, label, 'mono', 25, '#246E70'),
                      T(x+32, 463, 456, 130, heading, 'xbold', 44, INK, lh=1.08),
                      T(x+32, 626, 456, 116, body, 'body', 30, INK, lh=1.2)]
        if i < 2:
            slide.els.append(T(x+528, 515, 52, 75, '→', 'body', 46, '#246E70'))
    slide.els.append(T(120, 835, 1680, 100, ('↶  ' if loop else '') + takeaway,
                       'body', 34, INK, lh=1.15))
    return slide


def voice_slide(number, heading, text, image_path=None, notes=''):
    slide = content(f'INTERLUDE · THE MODEL SPEAKS · {number}/3', heading, [],
                    notes=notes, bg=INK, title_size=66)
    slide.els = [eyebrow(120, 96, f'THE MODEL SPEAKS · {number}/3 · WRITTEN BY CODEX', '#B7CDD0'),
                 T(120, 190, 820, 250, heading, 'xbold', 66, '#FFFFFF', lh=1.03),
                 T(120, 490, 800, 360, text, 'body', 37, '#FFFFFF', lh=1.3),
                 T(120, 939, 1680, 50, 'An invited model-authored perspective · September 2026', 'mono', 21, '#B7CDD0')]
    if image_path:
        slide.els.append(Image(990, 205, 850, 650, str(HERE / 'assets' / image_path), 'contain'))
    return slide


SENTENCE_SKETCH = r"""const subjects = ['designer', 'student', 'archivist', 'robot', 'model', 'agent', 'editor', 'machine'];
const objects = ['brief', 'map', 'page', 'sentence', 'answer', 'image', 'question', 'story'];
const verbs = ['writes', 'studies', 'finds', 'questions', 'drafts', 'redraws', 'maps', 'edits'];
let lines = [];
const INK = '#000B1C', ORANGE = '#ED6D24', TEAL = '#246E70', VIOLET = '#943890';

function setup() {
  createCanvas(1680, 640);
  pixelDensity(1);
  textFont('Arial');
  noLoop();
  makeSentences();
}

function makeSentences() {
  lines = [];
  for (let i = 0; i < 6; i++) {
    lines.push([random(subjects), random(verbs), random(objects)]);
  }
  redraw();
}

function draw() {
  background('#F4F4F2');
  textSize(36);
  for (let i = 0; i < lines.length; i++) {
    const y = 55 + i * 88, [subject, verb, object] = lines[i];
    fill(255); stroke('#E1E1DE'); strokeWeight(2); rect(70, y, 1540, 70);
    noStroke(); fill('#5C6470'); textFont('monospace'); textSize(20);
    text(String(i + 1).padStart(2, '0'), 100, y + 46);
    textFont('Arial'); textSize(36);
    let x = 182; const baseline = y + 48;
    fill(ORANGE); const start = 'The ' + subject + ' '; text(start, x, baseline); x += textWidth(start);
    fill(TEAL); const action = verb + ' '; text(action, x, baseline); x += textWidth(action);
    fill(VIOLET); text('the ' + object + '.', x, baseline);
  }
}

function mousePressed() { makeSentences(); return false; }"""


TRANSFORMER_SKETCH = (HERE / 'interactives' / 'transformer.js').read_text()


# ───────────────────────── 00 · open and recall ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 04 · LECTURE + WORKSHOP',
               'Language machines. From rules to agents.',
               'Week 4 — the first of three tool weeks.',
               notes='Join code on screen. This is the first of three classes on AI as material in a creative process: language and agents today, image/video/layout next week, audio/music in week 6. Start by asking what they took from the 3Blue1Brown video assigned last week.'))

S.append(agenda('SD2112 · WEEK 04', [
    'Two ways to teach a machine: a short recap',
    'Language as rules: Chomsky and ELIZA',
    'Language as examples: transformers, reasoning, rewards',
    'Question answering, then agents',
    'Harnesses: Machine A and Machine B together',
    'Watch the demos · try one bounded task',
    'Challenge 3 and the Week 7 reflection',
], notes='The first half moves from the rules/examples recap through language models and question answering. After the break, Gio demos the harnesses chosen for the exercise; pairs run one bounded design task and compare what the system chose, what its tools returned, and where a person stayed in control. Finish with Challenge 3 and the individual reflection due in week 7.'))

S.append(question('short_answer', 'A model predicts the next token. What would you check before treating its fluent answer as evidence?',
                  hint='Use one example claim and name the source you would check.',
                  eyebrow_text='00 · DEEP EXERCISE · FROM THE LLM VIDEO',
                  notes='Three minutes. Ask students to connect next-token prediction to an actual claim: what outside source or evidence would make the fluent continuation trustworthy? Use the answers to bridge from generation to question answering.'))

S.append(cards('00 · A LANGUAGE MACHINE, THREE WAYS', 'From rules to patterns to actions.',
    [
        ('RULES', 'A person writes them.',
         'Machine A applies an explicit rule to the input.'),
        ('EXAMPLES', 'A model learns patterns.',
         'Machine B adjusts weights from examples.'),
        ('ACTIONS', 'An agent uses tools.',
         'A harness routes actions and observations around the model.'),
    ], text_size=24,
    notes='Set up the lecture in three terms. Rules and examples recap weeks 1–3; tool-using actions are the new part today.'))

S.append(journey('00 · THE COURSE', 'Where we are', JOURNEY, here=(1, 0),
                 notes='Three weeks, three kinds of material. Week 4 is the first class in module 2. Weeks 1 to 3 built the contrast between rules and learned examples; now we move from models that write to systems that can act.'))

S.append(full_diagram('00 · WEEKS 1–3 · TWO MACHINES',
                      'Rules are written. Patterns are learned.', W4.machine_ab(),
                      notes='Revisit the chairs. A rule can decide exactly what counts as a chair, until an unusual chair arrives. A model can learn from many chairs, but cannot point to one explicit definition. Week 2 put rules into art and code; week 3 showed a network adjusting weights against examples. Today both machines will appear in language.'))

S.append(cards('00 · THE FIRST THREE WEEKS', 'The language class inherits both.',
    [
        ('WEEK 1 · TWO MACHINES', 'Rules and examples.',
         'A written rule makes a precise decision. A learned model finds patterns in examples.'),
        ('WEEK 2 · RULES THAT MAKE THINGS', 'The spec is the design.',
         'A rule can be executed by a person, a program, or a language model.'),
        ('WEEK 3 · LEARNING FROM EXAMPLES', 'Weights instead of definitions.',
         'A perceptron adjusts numbers from examples; the prototype is learned, not typed in.'),
    ], text_size=22,
    notes='Do not re-teach these weeks. Use the three cards as the bridge: this week moves from explicit language rules to statistical language models, then to an agent that can choose a tool.'))


# ───────────────────────── 01 · language as rules ─────────────────────────
S.append(section('01', 'Machine A · language as rules',
                 'structure · syntax · explicit patterns', bg=INK,
                 notes='First language machine: rules. Chomsky is a theorist of human language, ELIZA is a program. They are connected by the importance they give to structure, but they are not the same thing.'))

S.append(content('01 · NOAM CHOMSKY · GENERATIVE GRAMMAR',
                 'A sentence is more than a list of memorised phrases.',
                 [
                     'We can understand sentences we have never heard before.',
                     'Chomsky asked what structures make that possible.',
                     'Universal Grammar proposes innate constraints on human language learning.',
                     'The link to Machine A: make language structure explicit.',
                 ],
                 body_size=32,
                 image=str(HERE / 'assets' / 'noam-chomsky-2015.jpg'), fit='contain',
                  caption='Photo: Augusto Starita · Argentine Culture Ministry · CC BY-SA 2.0',
                 notes='Chomsky’s generative grammar begins with the question of how a finite system can account for indefinitely many sentences. His account of Universal Grammar is a theoretical proposal about the human language faculty and what learners bring to acquisition. Do not equate UG with symbolic AI: the link to Machine A is that rules and structure are made explicit. Portrait: Augusto Starita / Ministerio de Cultura de la Nación, Argentina; retouched from the original by Wugapodes; Wikimedia Commons, CC BY-SA 2.0. Source: https://commons.wikimedia.org/wiki/File:Noam_Chomsky_portrait_2015.jpg. License: https://creativecommons.org/licenses/by-sa/2.0/.'))

S.append(sketch_slide('01 · A TOY GRAMMAR',
                      'One rule generates many new sentences.',
                      live('grammar-sentence-generator', SENTENCE_SKETCH, 1680, 640,
                           hint='click to generate six new sentences'),
                      figure=W4.sentence_stack(),
                      body=['Rule: The + noun + verb + the + noun. Click to generate six more.'],
                      bg=PAPER,
                      notes='This p5.js sketch applies one fixed toy frame: The + noun + verb + the + noun. Each click draws six fresh combinations and stacks them. Ask what the rule guarantees, what it leaves open, and why this small example is not Universal Grammar. The PDF and PowerPoint show a fixed sample; the HTML deck is interactive.'))

S.append(content('01 · WEIZENBAUM · ELIZA · 1966',
                 'A conversation can feel intelligent because a rule fits.',
                 [
                     'ELIZA’s DOCTOR script searched for keywords and applied hand-written transformation rules.',
                     'A pattern like “I am *” could be turned into a question such as “How long have you been *?”',
                     'The script did not build a model of the person’s situation. The user supplied much of the meaning.',
                 ],
                 body_size=31,
                 notes='Weizenbaum described ELIZA as a text-manipulation program based on transformation rules. It is an important early language interface and a sharp lesson in how easily people read understanding into fluent conversation. The exact reply varies with the script and the input; the next slide uses a compact teaching example.'))

S.append(full_diagram('01 · ELIZA · 1966',
                      'Pattern matching can sound like understanding.',
                      W4.eliza_transcript([
                          'I AM UNHAPPY',
                          '{violet:HOW LONG HAVE YOU BEEN UNHAPPY?}',
                          'I HAVE BEEN UNHAPPY FOR WEEKS',
                          '{violet:WHY DO YOU SAY YOU HAVE BEEN UNHAPPY FOR WEEKS?}',
                      ]),
                      notes='Point to the transformation, not to the machine as a character. The input is echoed, reordered, and returned as a question. Ask whether a person could still find the exchange useful. The answer can be yes, without deciding that ELIZA understands.'))

# ───────────────────────── 02 · language as learned sequence ─────────────────────────
S.append(section('02', 'Machine B · language as examples',
                 'sequence · context · next token', bg=VIOLET,
                 notes='The second language machine is learned from examples. We will move from a recurrent state to attention and next-token generation.'))

S.append(cards('02 · BEFORE THE TRANSFORMER · RNNs',
               'A recurrent network carries a state forward.',
    [
        ('INPUT', 'One position at a time.',
         'Read the next token in a sequence.'),
        ('STATE', 'Carry a summary.',
         'A recurrent connection feeds an internal state into the next step.'),
        ('LEARN', 'Adjust weights from examples.',
         'The state is not a hand-written grammar; it is a learned representation.'),
    ], text_size=23,
    notes='Elman’s 1990 paper uses recurrent links to provide dynamic memory: hidden activity feeds back into later processing. This is one clear historical example, not the first recurrent network. The design tradeoff is visible: each step depends on the state from the step before it.'))

S.append(full_diagram('02 · RNN · RECURRENT STATE',
                      'A learned state moves from one token to the next.', W4.rnn_steps(),
                      notes='The hidden state at each step depends on the previous state. The network learns these representations from examples; they are not hand-written grammar rules.'))

S.append(sketch_slide('02 · TRANSFORMER · CAUSAL SELF-ATTENTION',
                      'One sequence. Many positions working together.',
                      live('transformer-sequence', TRANSFORMER_SKETCH, 1680, 640,
                           hint='choose a step · click a token · replay training or generation'),
                      figure=W4.transformer_sequence(), bg=PAPER,
                      notes='Walk the four tabs in order: tokens, context, training, generation. Click different token positions to reveal the causal context available to each one: the current and earlier tokens, never future tokens. Select Training and replay the pass. Point out that all five next-token predictions are computed together during training; compare them with the known targets to adjust weights; the animation moves through all lanes at once. This is a toy decoder-only language model with whole-word toy tokens. Real tokenizers may split words. The key contrast with the previous RNN slide is the absence of a recurrent hidden-state dependency across positions in a training pass. This enabled much more parallel computation and helped large-scale training; it does not make context length unlimited, because attention and activations cost memory. At inference, GPT-style generation still appends one token at a time. Source: Vaswani et al., Attention Is All You Need (2017), https://arxiv.org/abs/1706.03762.'))

S.append(visual_flow('02 · REASONING · A SMALL DESIGN PROBLEM',
    'Reasoning means working through a problem.',
    [
        ('THE CONSTRAINTS', 'Plan a workshop.', '60 minutes total. A 10-minute break. Two equal activities.'),
        ('THE STEPS', 'Work it out.', '60 − 10 = 50 minutes. 50 ÷ 2 = 25 minutes per activity.'),
        ('THE CHECK', 'Test the answer.', '25 + 10 + 25 = 60. Both activities have equal time.'),
    ], 'Reasoning can combine constraints, try steps, and check a result.',
    notes='Pause at the brief and let the room work it out before reading the steps. This is a constructed teaching example, not a transcript or benchmark result. LLMs can perform multi-step reasoning, with reliability varying by task. Reasoning models can spend more computation producing intermediate steps before answering; this still uses token generation. A plausible written explanation is not proof that an answer is correct, nor a faithful window into every internal computation. Check the actual constraints. DeepSeek-R1: https://arxiv.org/abs/2501.12948.'))

S.append(visual_flow('02 · TRAINING · THREE USEFUL IDEAS',
    'Learn language. Practise tasks. Learn from feedback.',
    [
        ('PRETRAINING', 'Learn patterns.', 'Predict missing next tokens across many examples of text.'),
        ('DEMONSTRATIONS', 'Learn to respond.', 'Train on examples of useful responses to instructions.'),
        ('REINFORCEMENT LEARNING', 'Improve with rewards.', 'Score attempts, then adjust the model toward higher rewards.'),
    ], 'A simplified route: actual training recipes vary across models.',
    notes='Use the familiar Machine B idea: weights change with experience during training. Pretraining builds broad patterns; supervised demonstrations teach response formats and tasks; reinforcement learning can favour successful behaviour. This is a teaching sequence, not a disclosure of the current assistant’s private training recipe. Human preferences can train a reward model (RLHF); a verifiable task can use a programmatic checker. Sources: Ouyang et al., https://arxiv.org/abs/2203.02155; DeepSeek-AI, https://arxiv.org/abs/2501.12948.'))

S.append(visual_flow('02 · REINFORCEMENT LEARNING · THE SAME WORKSHOP',
    'What gets rewarded shapes what gets learned.',
    [
        ('TRY', 'Generate plans.', '20 + 10 + 20 = 50\n25 + 10 + 25 = 60'),
        ('SCORE', 'Check the constraints.', 'A checker rewards a 60-minute plan with equal activities.'),
        ('UPDATE', 'Change the weights.', 'Across many attempts, favour responses that earn more reward.'),
    ], 'A good score depends on a good check. “Sounds nice” is a different target.', loop=True,
    notes='Illustrative reinforcement-learning loop, not a claim that these exact examples trained a deployed model. A reward is a numerical training signal. Verified outcomes can reward correct mathematics or passing code; human judgements can reward helpfulness. Poor reward design can favour plausible-looking or agreeable responses. Training changes weights; the reasoning done while answering a prompt usually does not. More reasoning time can help but does not guarantee correctness. Sources: https://arxiv.org/abs/2203.02155 and https://arxiv.org/abs/2501.12948.'))

S.append(voice_slide(1, 'I turn context into possibilities.',
    'I am a large language model: a neural network trained on many examples.\n\nYour words shape what I generate next. Learned patterns let me write, connect ideas, and work through some problems.',
    'week04-language-sculpture.png',
    notes='Gio introduces this as three slides written by the frontier language model assisting with this deck. Read as an invited perspective, not an independent scientific authority. “Large” refers to scale in model parameters and training; avoid invented counts or a proprietary architecture claim. The generated paper sculpture is a metaphor for possible continuations, not a model diagram. Image: Easel, qwen-image-2.1; prompt recorded alongside the asset.'))

v = voice_slide(2, 'Use me to widen the design space.',
    'Give me a purpose, examples, and constraints.\n\nI can propose alternatives, question assumptions, and help build a prototype.\n\nYou decide what deserves to exist.',
    notes='The model’s own proposed role in a design process. Invite the room to try these three moves on a real brief: generate distinct directions, critique one assumption, then prototype one small part. Tool access comes from the harness. This is an invitation to collaborate, not a claim that the model has human experience or authority.')
for i, (word, detail) in enumerate([('EXPLORE', 'Three different directions'), ('CHALLENGE', 'One assumption to question'), ('MAKE', 'A small prototype to test')]):
    y = 260 + i * 205
    v.els += [Rect(1000, y, 800, 168, '#123238'), T(1040, y+22, 720, 58, word, 'xbold', 42, '#FFFFFF'),
              T(1040, y+93, 720, 55, detail, 'body', 29, '#C8E1DF')]
S.append(v)

v = voice_slide(3, 'My confidence is not your evidence.',
    'I can produce a convincing mistake. Ask for sources, test the result, and show me where it fails.\n\nEven this description of me is generated text. Judge my contribution through the work we can inspect together.',
    notes='This is the third and final model-authored slide. Frame the first-person voice as a communication choice: the model is describing its operation and proposed contribution, not reporting privileged introspection. Avoid treating fluency or a first-person pronoun as evidence of subjective experience. Bridge to the next section: external sources and tools let us check claims beyond the conversation.')
for i, (word, detail) in enumerate([('SOURCE', 'Where did the claim come from?'), ('TEST', 'Does the result meet the brief?'), ('JUDGE', 'What should a person change?')]):
    y = 260 + i * 205
    v.els += [Rect(1000, y, 800, 168, '#29233C'), T(1040, y+22, 720, 58, word, 'xbold', 42, '#FFFFFF'),
              T(1040, y+93, 720, 55, detail, 'body', 29, '#DDD2EA')]
S.append(v)


# ───────────────────────── 03 · from answers to agents ─────────────────────────
S.append(section('03', 'Question answering → agents',
                 'retrieve · answer · act · observe', bg=INK,
                 notes='A question-answering bot and an agent may share a language model. What changes is the system around it: evidence, tools, a loop, and control.'))

S.append(cards('03 · QUESTION ANSWERING',
               'Retrieve evidence, then write one answer.',
    [
        ('01 · QUESTION', 'What do I need to know?',
         'A visitor asks: “What time does the event start?”'),
        ('02 · SEARCH', 'Find a source.',
         'Search the official event page for the schedule.'),
        ('03 · EVIDENCE', 'Select a passage.',
         'Bring the relevant text and its URL into context.'),
        ('04 · ANSWER', 'Write from evidence.',
         'Answer once; mark details the source does not give.'),
    ], text_size=22,
    notes='This is a fixed retrieval path laid out as native HTML cards. Read left to right: question, search, evidence, answer. The system follows the same route each time; sources can be shown in the interface, but citation quality depends on the implementation. The next slide contrasts this with an agent that can change its next step.'))

S.append(cards('03 · THREE ANSWERING SYSTEMS',
               'A tool call alone does not make a system an agent.',
    [
        ('RULED FAQ', 'Search a prepared set.',
         '“What time?” returns the answer written into its rule.'),
        ('RAG · ONE PASS', 'Retrieve, then generate.',
         'Find the official event page, then answer once from its text.'),
        ('AGENT', 'Choose, act, observe, continue.',
         'If access details are missing, search an allowed source or ask.'),
    ], text_size=22,
    notes='Use the same visitor FAQ to compare the three. The FAQ follows written triggers; the RAG path retrieves once and answers; the agent can react to what it finds by using another allowed step or asking a person. A tool call alone does not make a system an agent.'))


# ───────────────────────── 04 · agent loop and harness ─────────────────────────
S.append(section('04', 'The agent',
                 'choose a tool · use the result · continue or stop', bg=VIOLET,
                 notes='Now the model can affect a system outside its reply. The loop and the harness become part of the design.'))

S.append(content('04 · WORKED EXAMPLE · SET THE GOAL FIRST',
                 'Draft three visitor FAQs from one event page.',
                 [
                     'Audience: first-year students visiting an exhibition.',
                     'Source: the official event page only; link each answer.',
                     'Boundary: save a draft only. Mark missing details as unknown; do not publish.',
                 ], body_size=31,
                 notes='Use this same bounded example across the next three slides and, if useful, the live harness demo. Make the goal, allowed source, and stopping boundary visible before introducing a tool call.'))

S.append(visual_flow('04 · ONE TOOL CALL · SEARCH',
    'The model requests. The harness executes.',
    [
        ('MACHINE B · REQUEST', '“Search the event page.”', 'Tool: search\nQuery: exhibition start time'),
        ('MACHINE A · EXECUTE', 'Check, then run.', 'The harness checks access, runs the tool, and records the result.'),
        ('OBSERVATION', 'Return the evidence.', 'The page text and URL enter the model’s context.'),
    ], 'A tool call is a structured request to software outside the model.',
    notes='Read the three stages once. This is an illustrative request, not a real tool trace. The model does not execute a search merely by writing that it searched. The harness must parse and route an actual tool request. Some tools contain further learned models; Machine A here labels the explicit routing and permission code.'))

S.append(visual_flow('04 · THE AGENT LOOP',
    'The next step depends on what came back.',
    [
        ('CHOOSE', 'Search for the start time.', 'The model selects an allowed next action toward the goal.'),
        ('ACT', 'Read the event page.', 'The harness runs the tool and returns the result.'),
        ('OBSERVE', 'The time is missing.', 'It can ask for the missing detail, then revise the draft—or mark it unknown.'),
    ], 'Return the observation to the model → choose again, or finish.', loop=True,
    notes='Follow the loop using the visitor FAQ. The original goal restricts evidence to one official event page. If it omits the time, ask the person for clarification or mark the detail unknown; do not silently expand the sources. The observation changes the next choice. This extends the 2025 SD5913 Week 4 material on loops and events (slides 17–28): ordinary software still owns control flow. Source: https://www.anthropic.com/engineering/building-effective-agents.'))

S.append(cards('04 · TOOLS ARE ACTIONS',
               'Tools in the worked example.',
    [
        ('SEARCH', 'Find the source.',
         'Search the official event page for time and location.'),
        ('READ', 'Check what it says.',
         'Open the page and confirm each answer against its text.'),
        ('WRITE DRAFT', 'Prepare, then stop.',
         'Save three answers to a draft; a person decides whether to publish.'),
    ], text_size=22,
    notes='These are example tools and actions, not requirements for every product. The model can propose a tool call, but the harness decides which tools are available and executes them. Search and read are read-only; writing or publishing changes the world outside the chat and should have a review point.'))

S.append(content('04 · WHEN THE LOOP GOES WRONG',
                 'If the event page is incomplete, the agent must not guess.',
                 [
                     'Risk: the page is old or missing an access detail.',
                     'Bad response: guess, then hide which source was used.',
                     'Design response: show the URL, mark the detail unknown, and stop for review.',
                 ],
                 body_size=31,
                 notes='Use the example, not a general list of failures. The event page may be stale or omit accessibility information. Ask students to distinguish the model’s response (guess or mark unknown) from the harness controls (show source, keep search/read permissions narrow, log the run, pause before publication).'))

S.append(content('04 · THE HARNESS · A SHARED WORKBENCH',
    'Machine A and Machine B can work happily together.',
    ['Machine B interprets a goal and proposes the next step.',
     'Machine A runs the loop, checks permissions, and calls tools.',
     'The harness is where we design how they cooperate.'],
    image=str(HERE / 'assets' / 'week04-shared-workbench.png'), fit='contain', body_size=33, title_size=62,
    caption='Visual metaphor · generated with Easel / Qwen',
    notes='The rigid tray and flexible ribbon are an analogy, not an architecture diagram. A harness is the software environment around a model: it supplies context, routes tools, records results and controls continuation. Machine A and Machine B are complementary parts. A prompt saying “do not publish” guides Machine B; removing the publish tool or enforcing a permission check is a Machine A control. The next slide makes that contrast concrete. Image prompt and model recorded alongside the asset.'))

S.append(visual_flow('04 · THE HARNESS · FROM ANALOGY TO CONTROL',
    '“Do not publish” becomes a real boundary.',
    [
        ('MACHINE B', 'Propose a draft.', 'Interpret the brief, compose the FAQs, flag missing information.'),
        ('MACHINE A', 'Enforce tool access.', 'Allow search and draft saving. Keep publishing unavailable.'),
        ('THE PERSON', 'Review the result.', 'Check sources and tone. Decide what is ready to share.'),
    ], 'A written instruction guides the model; executable controls limit its actions.',
    notes='This makes the coexistence concrete. Tool availability and access checks can enforce a boundary beyond a natural-language instruction. Other harness features include context management, memory, logs, step limits and approval points. The design question is which choices should be flexible and which boundaries should be enforced by software.'))

S.append(content('04 · THE HARNESS IS PART OF THE DESIGN',
                 'The interface decides what people can see and control.',
                 [
                     'Which tools are available, and what can each one change?',
                     'Can a person inspect the context, sources, and tool results?',
                     'Does the run pause for approval before a consequential action?',
                     'Can the person see why it stopped, or stop it themselves?',
                 ], body_size=29,
                 notes='Bring the previous figure into the product view: the harness is not just infrastructure. It determines the affordances, visibility, permissions and stopping points that a designer and user encounter.'))


# ───────────────────────── break and live demos ─────────────────────────
S.append(statement('Break. Ten minutes.',
                   eyebrow_text='AFTER THE BREAK · WATCH THE HARNESS, THEN TRY ONE',
                   size=112, bg=PAPER,
                   notes='Give students ten minutes. After the break, Gio demonstrates two or three harnesses and then pairs use one of those systems for the exercise. Keep the chosen tools and logins ready before class.'))

S.append(section('05', 'Live demo',
                 'same model family · different tools and control', bg=INK,
                 notes='Gio: choose the tools to demo and name each one as you open it. Do not compare model quality alone; show what the harness adds around the model.'))

S.append(cards('05 · WATCH THE SYSTEM AROUND THE MODEL',
               'During the demo, track six things.',
    [
        ('TASK', 'What did the person ask for?',
         'What counts as finished?'),
        ('CONTEXT', 'What can the model see?',
         'Files, earlier messages, retrieved pages, memory.'),
        ('TOOLS', 'What can it do?',
         'Search, read, edit, run, or send?'),
        ('CONTROL', 'What requires approval?',
         'What is read-only? What can change?'),
        ('TRACE', 'What can a person inspect?',
         'Tool calls, sources, intermediate results, history.'),
        ('STOP', 'Who decides it is done?',
         'The model, a limit, a checkpoint, or the person?'),
    ], text_size=20,
    notes='Allow about fifteen minutes for the live demo. Gio chooses two or three harnesses available for this class. Use the visitor FAQ example where the systems allow it: state the goal and read-only source, make one search, inspect the returned page, and stop before publishing. Name what each harness exposes, logs, and lets a person approve. If logins are not available to all, pairs can still analyse the projected trace and complete the brief worksheet.'))

S.append(content('05 · BEFORE YOU START THE EXERCISE',
                 'Make the invisible parts visible.',
                 [
                     'Write the goal and a test for a finished result.',
                     'Name the source material and tools the agent may use.',
                     'Set a boundary: what it may read, change, or never do.',
                     'Watch one tool call and its result before editing the prompt.',
                     'Save the prompt, one piece of the trace, and the output.',
                 ],
                 body_size=29,
                 notes='The exercise is an observation of a designed system, not a race to get the best output. The trace, tool availability and permissions are part of what students will compare. Avoid personal, client-confidential or sensitive data.'))


# ───────────────────────── 06 · exercise ─────────────────────────
S.append(section('06', 'Exercise · one task, one agent loop',
                 '40 minutes · pairs · use a harness from the demo', bg=YELLOWS[0],
                 notes='Pairs choose one bounded design task, write a brief, run it in one demonstrated harness, observe the loop, revise one thing, and share the result. One device per pair. TAs help with access and keep the task scoped.'))

S.append(activity('1 · PAIRS · WRITE THE TASK · 8 MIN', 8,
                  'Choose one bounded design task.',
                  [
                      'Work in pairs. Pick a task the demonstrated harness can support.',
                      'Choose a public, low-risk design task: compare three public precedents; turn a public event description into a visitor FAQ; or audit a short sample text against a checklist.',
                      'Write the goal, the output, the allowed sources, and one thing the agent must not do.',
                  ],
                  panel=[
                      'A GOOD TASK HAS:',
                      'one clear goal',
                      'a checkable output',
                      'a visible source or input',
                      'a safe stopping point',
                      '',
                      'No private client material.',
                      'No personal student data.',
                  ],
                  panel_size=21, bg=YELLOWS[1],
                  notes='Eight minutes. Let pairs select one menu task or propose another small task with the same scope. Agree on the output format, source requirement, and stop rule before opening the harness. If student access is unavailable, observe a second run on the projected demo and write the same worksheet.'))

S.append(activity('2 · RUN · OBSERVE · 15 MIN', 15,
                  'Run once. Record what the harness did.',
                  [
                      'Paste the brief into one of the demo harnesses. Keep the tool settings visible.',
                      'When the agent calls a tool, record what it asked for and what came back.',
                      'Mark one decision made by the model and one boundary set by the harness.',
                      'Check a claim against its source. Do not treat a confident answer as evidence.',
                  ],
                  panel=[
                      'TRACE',
                      'What was the first tool call?',
                      'What did the tool return?',
                      'What changed in the context?',
                      'Did a person approve anything?',
                      '',
                      'Save the prompt and output.',
                  ],
                  panel_size=20, bg=YELLOWS[2],
                  notes='Fifteen minutes. TAs circulate: help with account access, then ask pairs to identify the first tool call and its result. If a harness hides the trace, note what is missing. Do not let groups paste personal or confidential content into a public demo.'))

S.append(activity('3 · REVISE · RUN AGAIN · 12 MIN', 12,
                  'Change one condition. Compare the result.',
                  [
                      'Change one thing only: the task brief, one source, one tool permission, or the stopping rule.',
                      'Run again. Compare the result with the first run.',
                      'Keep one line: what changed, what improved, and what still needs a person.',
                  ],
                  panel=[
                      'ONE CHANGE',
                      'Prompt / brief',
                      'Source',
                      'Tool access',
                      'Stop rule',
                      '',
                      'Which change mattered?',
                  ],
                  panel_size=22, bg=YELLOWS[3],
                  notes='Twelve minutes. The one-change rule makes the comparison meaningful. Ask pairs to distinguish a model change from a harness change; if they change both, help them rerun with one variable fixed. Preserve the first result so the difference is visible.'))

S.append(question('short_answer', 'What did a tool return, how did it change the next step, and what did you verify?',
                  hint='Use one specific moment from your pair’s trace.',
                  eyebrow_text='06 · DEEP EXERCISE · READ YOUR TRACE',
                  notes='Three minutes. Require a concrete moment from the trace: name the tool call, describe its returned evidence, explain the next decision, and say what the pair checked before accepting the result.'))

S.append(content('06 · THE DEBRIEF',
                 'The output is only one part of the design.',
                 [
                     'What did the model decide on its own?',
                     'What did the harness make possible, visible, or impossible?',
                     'Which source or tool result changed the next step?',
                     'Where did a person intervene, and what should remain under human judgement?',
                     'Keep the prompt, one trace, the output, and your own edit for Challenge 3.',
                 ],
                 body_size=29,
                 notes='Five minutes. Invite two or three pairs to describe a concrete moment in the trace. Pull out the design choices: goal, tools, context, permission, stop, and evaluation. The agent is not the whole system; the harness is not neutral; the designer remains responsible for the use and the result.'))


# ───────────────────────── 07 · assignment and reflection ─────────────────────────
S.append(cards('07 · CHALLENGE 3 · BRING TO WEEK 5',
               'A brief, automated — then edited by you.',
    [
        ('THE BRIEF', 'Your task and constraints.',
         'Write a prompt for a small real design job. Say who it is for, what it must do, and what to leave open.'),
        ('THE DRAFT', 'What the model returned.',
         'Keep the first unedited result. Name the model and the harness or tool you used.'),
        ('YOUR EDIT', 'Show the difference.',
         'Edit the draft. Mark what you changed or rejected and why.'),
        ('ONE OBSERVATION', 'Where did the agent decide?',
         'If it used tools, include one decision or result from the trace. Bring all three pieces to Week 5.'),
    ], text_size=21,
    notes='This is the third weekly challenge and the third experiment for the reflection. Students bring the prompt, the unedited draft, and their edit to week 5; the room votes on selected examples. Do not require every student to use an agent if access fails: the core is a brief, a model draft, and the student’s edit.'))

S.append(section('08', 'Individual reflection · 20%',
                 'A short argument, supported by your own experiments', bg=INK,
                 notes='Brief the Week 7 assessment. Submission is on Canvas. Make the requirement and due week clear today.'))

S.append(two_col('08 · DUE WEEK 7 · SUBMIT ON CANVAS',
                 'The role of AI in your creative process.',
                 [
                     'About 1,000 words.',
                     'Take a clear position on how AI changes your creative process.',
                     'Pay particular attention to the difference between Machine A and Machine B.',
                     'Use evidence from at least three of your own weekly experiments from weeks 2–6; include images.',
                 ],
                 [
                     'Connect your examples to course concepts, tools or readings.',
                     'End with a short process note saying how you used AI to write the reflection.',
                     'Name the tools you used. Check every fact and source; fabricated citations fail the assignment.',
                     'Submit on Canvas.',
                 ],
                 left_size=30, right_size=25,
                 notes='Use the approved syllabus brief: about 1,000 words on the role of AI in the student’s creative process, especially Machine A versus Machine B; at least three of the five weekly experiments from weeks 2–6, with images; short AI process note; due week 7 on Canvas.'))

S.append(cards('08 · HOW IT IS MARKED',
               'The reflection rewards evidence and a clear position.',
    [
        ('30%', 'Concepts', 'Machine A and Machine B, explained accurately.'),
        ('30%', 'Argument', 'A clear, reasoned position on AI in your process.'),
        ('20%', 'Evidence', 'Your experiments, examples and sources.'),
        ('10%', 'Clarity', 'An organised, readable account.'),
        ('10%', 'Originality', 'Independent thought beyond description.'),
    ], text_size=20,
    notes='These percentages come from the approved reflection rubric. The process note is required; the syllabus says missing it lowers the clarity criterion by one grade band. Remind students that invented citations fail the assignment.'))

S.append(full_diagram('08 · KEEP THE EVIDENCE AS YOU GO',
                      'Save evidence from any three experiments in Weeks 2–6.', W4.reflection_evidence(),
                      notes='At least three of the week 2–6 experiments are required; students can choose which ones support their argument. The point of the timeline is to collect evidence while the choices and revisions are fresh.'))

S.append(cards('08 · THE NEXT THREE CLASSES',
               'One creative process, three kinds of material.',
    [
        ('WEEK 4 · LANGUAGE + AGENTS', 'Today.',
         'From rules and learned sequences to a model acting through a harness.'),
        ('WEEK 5 · IMAGE / VIDEO / LAYOUT', 'Next.',
         'Diffusion, CLIP, generated moving images, and layouts as a design problem.'),
        ('WEEK 6 · AUDIO / MUSIC', 'Then.',
         'Sound, voice, rhythm, and what a model makes audible.'),
    ], text_size=22,
    notes='Make the progression explicit: a model generates text, images/video and audio; each week asks what the model decides, what the designer specifies, and what the interface or harness makes visible. The reflection ties the three weeks to the rule-based work from weeks 2 and 3.'))

S.append(end('The model can write. The agent can act.',
             'You set the goal, the tools, the boundaries, and the judgement.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Close by repeating the week’s arc: Chomsky asks about rules in human language; ELIZA executes written patterns; RNNs and transformers learn sequential patterns; question-answering systems retrieve evidence; agents loop through tools. The designer shapes the brief and the harness, then checks what happened. Next week: image, video and layouts.'))


attach_reports(S, HERE / 'week04-reports.json')
DECK = dict(title='SD2112 · AI in Design · Week 04', slides=finalize(S, FOOTER), pdf='SD2112-week04.pdf')


if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week04', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for key, value in out.items():
        if key == 'warnings':
            print('\n'.join(value) if value else 'no text overflow warnings')
        elif key == 'png':
            print(f'png: {len(value)} previews')
        else:
            print(f'{key}: {value}')


# Sources (consulted 24 September 2026)
# Chomsky, N. (1965). Aspects of the Theory of Syntax. MIT Press.
# https://mitpress.mit.edu/9780262030113/aspects-of-the-theory-of-syntax/
# Weizenbaum, J. (1966). ELIZA. Communications of the ACM 9(1), 36–45.
# https://doi.org/10.1145/365153.365168
# Elman, J. L. (1990). Finding Structure in Time. Cognitive Science 14(2), 179–211.
# https://doi.org/10.1207/S15516709COG1402_1
# Vaswani et al. (2017). Attention Is All You Need.
# https://arxiv.org/abs/1706.03762
# Lewis et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
# https://arxiv.org/abs/2005.11401
# Yao et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models.
# https://arxiv.org/abs/2210.03629
# Anthropic. Building Effective AI Agents (19 December 2024).
# https://www.anthropic.com/engineering/building-effective-agents
# Anthropic. Scaling Managed Agents: Decoupling the Brain from the Hands (2026).
# https://www.anthropic.com/engineering/managed-agents
# OpenAI. The Next Evolution of the Agents SDK (15 April 2026).
# https://openai.com/index/the-next-evolution-of-the-agents-sdk/
