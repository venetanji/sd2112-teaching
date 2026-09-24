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
                             journey, activity, two_col, image_full, finalize)
from course import SITE, PLAYLIST, JOURNEY, footer     # noqa: E402


FOOTER = footer(4)
HERE = Path(__file__).resolve().parent
S = []


def full_diagram(eyebrow_text, caption, figure, notes=''):
    """Give a code-drawn diagram a full-slide image area and a short footer label."""
    _svg, png = figure
    return image_full(png, eyebrow_text, caption, notes=notes,
                      fit='contain', bg=PAPER)


# ───────────────────────── 00 · open and recall ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 04 · LECTURE + WORKSHOP',
               'Language machines. From rules to agents.',
               'Week 4 — the first of three tool weeks.',
               notes='Join code on screen. This is the first of three classes on AI as material in a creative process: language and agents today, image/video/layout next week, audio/music in week 6. Start by asking what they took from the 3Blue1Brown video assigned last week.'))

S.append(agenda('SD2112 · WEEK 04', [
    'Two ways to teach a machine: a short recap',
    'Language as rules: Chomsky and ELIZA',
    'Language as examples: RNNs and transformers',
    'Question answering, then agents',
    'What an agent harness controls',
    'Watch the demos · try one bounded task',
    'Challenge 3 and the Week 7 reflection',
], notes='The first half moves from the rules/examples recap through language models and question answering. After the break, Gio demos the harnesses chosen for the exercise; pairs run one bounded design task and compare what the system chose, what its tools returned, and where a person stayed in control. Finish with Challenge 3 and the individual reflection due in week 7.'))

S.append(question('short_answer', 'From the LLM video: what can a language model predict?',
                  hint='One idea you can explain now · one question you still have.',
                  eyebrow_text='00 · QUICK REWIND · 3BLUE1BROWN',
                  notes='Two minutes, short answers. Read a few aloud. Expect: the next token, not an answer from a database; what remains unclear is attention, training, or how it gets from text to a reply. Use that to decide where to slow down in the transformer section.'))

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
                     'Chomsky argued that a grammar should describe the structures and rules that let speakers form and understand sentences they have never heard before.',
                     'Universal Grammar (UG) is his proposal that humans bring innate constraints to language learning. It is a theory about human language acquisition, not a computer program or a list of English rules.',
                     'For this course, the useful link is the emphasis on structure: language can be described by rules that generate many sentences.',
                 ],
                 body_size=28,
                 notes='Chomsky’s generative grammar begins with the question of how a finite system can account for indefinitely many sentences. His account of Universal Grammar is a theoretical proposal about the human language faculty and what learners bring to acquisition. Do not equate UG with symbolic AI: the link to Machine A is that rules and structure are made explicit.'))

S.append(full_diagram('01 · A TOY GRAMMAR',
                      'Phrase structure shows one way rules build a sentence.', W4.grammar_tree(),
                      notes='Read the tree top to bottom. S is a sentence; NP and VP are categories; the leaves are the words. The categories are not the words themselves. Chomsky’s work is a much richer theory of linguistic competence; the diagram is a teaching example, not a depiction of Universal Grammar.'))

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

S.append(question('multiple_choice', 'What is ELIZA doing in this example?',
                  ['Retrieving a passage from a knowledge base',
                   'Matching a pattern and applying a written transformation',
                   'Learning a new grammar from this conversation',
                   'Choosing a web tool and checking its result'],
                  eyebrow_text='01 · QUICK CHECK · MACHINE A',
                  notes='B. The rule is authored in the script and applied to the input. C and D are later mechanisms; A describes a retrieval system. This poll checks the distinction before moving to machine B.'))


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

S.append(full_diagram('02 · TRANSFORMER · CAUSAL SELF-ATTENTION',
                      'Attention looks back; generation stays one token at a time.', W4.transformer_mask(),
                      notes='The teal cells indicate positions available to each token; dark cells mark future positions masked in a causal decoder. Transformers made training across positions easier to parallelize. GPT-style generation remains autoregressive, one token at a time.'))

S.append(cards('02 · TRANSFORMERS · 2017',
               'Attention lets a token use its context.',
    [
        ('1 · TOKENISE', 'Split text into tokens.',
         'The model processes token IDs, not a sentence as a single object.'),
        ('2 · ATTEND', 'Mix information across positions.',
         'Each token can use relevant earlier context; the weights are learned.'),
        ('3 · PREDICT', 'Estimate the next-token distribution.',
         'Choose or sample a token, append it, and repeat.'),
    ], text_size=23,
    notes='Vaswani and colleagues introduced the Transformer in 2017 for machine translation. The paper’s architecture replaces recurrence with attention and feed-forward layers. Keep the short version: tokens, attention, next-token prediction. The next two weeks reuse this idea in image and sound systems.'))

S.append(content('02 · THE GENERATION LOOP',
                 'A fluent reply is built one token at a time.',
                 [
                     'Text is split into token IDs, then mapped to learned vectors (embeddings). Transformer layers use context to update those representations.',
                     'The model estimates a distribution over next tokens. A decoding rule selects one; it is added to the context and the step repeats.',
                     'A base model learns to continue text; an instruction-tuned model gets additional training to respond to requests.',
                     'A chat product may add prompts, retrieval and tools. Fluent text can still be unsupported (hallucination) or mirror a user’s view (sycophancy): check claims against evidence.',
                 ],
                 body_size=26,
                 notes='Use the pipeline as the recap: token IDs map to learned vectors; attention layers transform them using context; the model predicts a next-token distribution and decoding selects one token. “Next word” is shorthand because tokenizers split text differently. A base model is trained to continue text; instruction tuning adds training for following requests. The chat interface can add system prompts, retrieval and tools. Hallucination and sycophancy are failure modes of generated answers, not properties that retrieval automatically fixes: ask students to check an answer against its source.'))


# ───────────────────────── 03 · from answers to agents ─────────────────────────
S.append(section('03', 'Question answering → agents',
                 'retrieve · answer · act · observe', bg=INK,
                 notes='A question-answering bot and an agent may share a language model. What changes is the system around it: evidence, tools, a loop, and control.'))

S.append(full_diagram('03 · QUESTION ANSWERING',
                      'Retrieve evidence, then generate an answer.', W4.qa_pipeline(),
                      notes='The figure shows a fixed retrieval-and-answer path. Sources can be shown in an interface, but citations depend on the system. The following cards compare a ruled FAQ, one-pass RAG, and an agent that can choose what to do next.'))

S.append(cards('03 · THREE ANSWERING SYSTEMS',
               'A tool call alone does not make a system an agent.',
    [
        ('RULED FAQ', 'Search a prepared set.',
         'Explicit triggers and responses; predictable, narrow coverage.'),
        ('RAG · ONE PASS', 'Retrieve, then generate.',
         'Search brings passages into context; the model writes one answer.'),
        ('AGENT', 'Choose, act, observe, continue.',
         'The system can choose a next tool or stop based on what happened.'),
    ], text_size=22,
    notes='Anthropic’s useful architectural distinction: a workflow follows predefined code paths; an agent directs its own process and tool use. Real systems can combine both. Ask which of the three changes the route while it is running.'))

S.append(question('multiple_choice', 'A help bot searches one policy page, then writes one answer. Is it an agent?',
                  ['Yes. Any system with a language model is an agent.',
                   'Not necessarily. A fixed search-and-answer path can be a workflow.',
                   'No. Agents cannot use retrieval.',
                   'Yes, because its answer may sound conversational.'],
                  eyebrow_text='03 · QUICK CHECK · QA OR AGENT?',
                  notes='B. Retrieval can be one fixed step. An agent is distinguished here by dynamically choosing its process or tools, not by having a chat interface.'))


# ───────────────────────── 04 · agent loop and harness ─────────────────────────
S.append(section('04', 'The agent',
                 'a model that can choose a tool and go again', bg=VIOLET,
                 notes='Now the model can affect a system outside its reply. The loop and the harness become part of the design.'))

S.append(full_diagram('04 · THE AGENT LOOP',
                      'Observe the result; continue, ask, or stop.', W4.agent_loop(),
                      notes='Walk the arrows: goal and limits; model; tool call; observation. Connect this to the 2025 programming slides: input handling, polling, event loops and callbacks already gave us the control structures; the agent harness runs a loop in which the model can select the next action from the latest observation. The model does not replace the program around it. A search result or file output is new evidence, not automatically trusted truth. The stopping rule, tool access, and approval point are design decisions.'))

S.append(cards('04 · TOOLS ARE ACTIONS',
               'The model chooses; the harness performs.',
    [
        ('SEARCH', 'Find evidence.',
         'The agent proposes a query; the search tool returns pages or passages.'),
        ('FILES / DATA', 'Read or transform material.',
         'Access is limited to the workspace the harness exposes.'),
        ('CREATE / SEND', 'Change the world outside the chat.',
         'Writes, purchases, messages and publishing deserve explicit review.'),
    ], text_size=22,
    notes='Keep the boundary concrete. A model can propose a tool call, but the harness decides what is available and executes it. Read-only search is different from writing files or sending something to another person. For the exercise, stay with low-risk tasks and visible outputs.'))

S.append(content('04 · WHEN THE LOOP GOES WRONG',
                 'More steps can compound a small mistake.',
                 [
                     'A wrong assumption can send the agent to the wrong source or file.',
                     'An agent may treat an untrusted page or document as an instruction.',
                     'A tool can fail, return stale information, or expose more data than the task needs.',
                     'A useful harness makes the working context visible, limits permissions, logs actions, and gives people a way to approve or stop.',
                 ],
                 body_size=28,
                 notes='This is not a warning slide detached from design. It is the reason to observe the harness in the demo. Tools and memory expand what the model can do; permissions, sandboxing, logging, and checkpoints set the boundary. Ask where the boundary sits in each tool Gio shows.'))

S.append(full_diagram('04 · THE AGENT HARNESS',
                      'The harness sets context, tools, permissions, and review.', W4.harness_map(),
                      notes='Anthropic describes a harness as the loop calling the model and routing tool calls to infrastructure. For this class, use the wider working view in the diagram: goal and context, memory, tools, sandbox, permissions, logs, and a human checkpoint. Product interfaces hide some of this and expose other parts.'))

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
    notes='Allow about fifteen minutes for the live demo. Gio chooses two or three harnesses available for this class. Use the same low-risk task if the systems allow it. Name the task, the tool boundary, what the interface shows, and the step where a person can intervene. If logins are not available to all, pairs can still analyse the demo trace and complete the brief worksheet.'))

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

S.append(question('multiple_choice', 'Where did your design judgement matter most?',
                  ['Choosing the goal and constraints',
                   'Choosing what the agent could access',
                   'Checking the sources and the result',
                   'All three'],
                  eyebrow_text='06 · DEBRIEF · MULTIPLE CHOICE',
                  notes='Two minutes. There is no single correct answer; ask for one example from each choice. The last option is the synthesis: design decisions happened before, during, and after the model’s run.'))

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
                 notes='Brief the Week 7 assessment. The Canvas submission link is not available in this deck yet: Gio will create the assignment and post the link. Make the requirement and due week clear today.'))

S.append(two_col('08 · DUE WEEK 7 · SUBMIT ON CANVAS',
                 'The role of AI in your creative process.',
                 [
                     'About 1,000 words.',
                     'Take a clear position on how AI changes your creative process.',
                     'Pay particular attention to the difference between rule-based and adaptive systems.',
                     'Use evidence from at least three of your own weekly experiments from weeks 2–6; include images.',
                 ],
                 [
                     'Connect your examples to course concepts, tools or readings.',
                     'End with a short process note saying how you used AI to write the reflection.',
                     'Name the tools you used. Check every fact and source; fabricated citations fail the assignment.',
                     'Submission: Canvas · Week 7. Gio will post the Canvas link.',
                 ],
                 left_size=30, right_size=25,
                 notes='Use the approved syllabus brief: about 1,000 words on the role of AI in the student’s creative process, especially rule-based versus adaptive systems; at least three of the five weekly experiments from weeks 2–6, with images; short AI process note; due week 7 on Canvas. Gio: create the Canvas assignment and add its link to the course communication before the submission window opens.'))

S.append(cards('08 · HOW IT IS MARKED',
               'The reflection rewards evidence and a clear position.',
    [
        ('30%', 'Concepts', 'Rule-based and adaptive systems, explained accurately.'),
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
