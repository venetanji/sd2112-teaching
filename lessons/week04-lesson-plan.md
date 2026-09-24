# SD2112 · Week 4 lesson plan

**Language machines: from rules to agents** · three-hour lecture-workshop (about 170 minutes of class plus a 10-minute break) · deck: `week04-classpoint.pptx` (51 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week04/` (`SD2112-week04.pdf` next to it)

## Purpose of this session

For us:

1. Reconnect the first three weeks through **Machine A** (written rules) and **Machine B** (patterns learned from examples); let students carry that distinction into language.
2. Separate a theory of human language from a language program: Chomsky's generative grammar and Universal Grammar are theories about linguistic structure and acquisition; ELIZA applies hand-written patterns.
3. Explain the move from recurrent state to transformer attention, and follow a prompt from tokens and context to parallel training and sequential generation; introduce reasoning and reward-based training with a small workshop-planning example.
4. Explain the harness as a place where Machine A and Machine B cooperate. Distinguish a fixed question-answering workflow from an agent that can choose a tool, inspect its result, and continue or stop; show how a harness shapes that loop.
5. Let students observe the harness in a live demo, then run and revise one bounded design task. Brief Challenge 3 and the Week 7 individual reflection.

For students, by the end of the class they can:

- contrast a written language rule with a pattern learned from examples;
- describe the difference between Chomsky's account of human language acquisition and an explicit grammar or program;
- explain, at a high level, how an RNN carries state, how a transformer uses attention, and how a language model generates a reply one token at a time;
- distinguish a fixed retrieve-and-answer path from an agent loop that selects tools based on observations;
- identify what an agent harness lets a system see and do, what it records, and where a person can intervene;
- preserve a prompt, an unedited draft, and a considered edit as evidence for Challenge 3 and the reflection.

## The 2025 reference

The 2025 Week 4 PDF/summary is from **SD5913's programming-for-designers course**, so treat it as a teaching reference, not as a prior SD2112 syllabus. Its sequence moves from input and buttons through loops, polling, events/callbacks (slides 17–28) and browser interfaces, then into local LLMs and chat interfaces (slides 38–45 and 61–66). Carry forward the most useful bridge: an agent still runs inside ordinary program control flow. The harness owns the loop, routes calls and returns observations; the model may choose the next action. That makes the agent legible as a designed system rather than a disembodied chatbot.

The current SD2112 sequence assumes the programming exercises are not the goal today. Keep the old material as a short analogy in the speaker notes and spend the classroom time on language, tools, control and design judgement.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: open `week04-classpoint.pptx` and keep the join code visible on slide 1. Try both short-answer activities once, then reset them. Open the Week 4 web deck as backup; speaker notes are under `S`. |
| Amber | Post the Week 4 deck and PDF to Canvas with the Challenge 3 brief. Once Gio supplies the Week 7 reflection submission link, include it in the Canvas announcement. |
| WU Zhao, MA Jie | Help students join ClassPoint and pair up; during the exercise, help with access to the demo harnesses, keep tasks bounded and ask students to capture one tool result. |
| Gio | Choose two or three harnesses for the demo and test logins, tool access and visible traces. Create the Week 7 Canvas reflection submission link and share it with Amber for posting. Use the same low-risk task across demos where practical. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---:|---|---|---|---|
| 0:00 | 1–7 | Welcome and recall | Video warm-up; Machine A/B; quick course map. | Short answer | Take one evidence-checking example from the room. Keep the recap brief. |
| 0:10 | 8–12 | Machine A · language as rules | Chomsky portrait; sentence generator; ELIZA. | | Click twice on slide 10. Ask what changes and what the rule keeps fixed. UG is a theory of human language acquisition, not a computer grammar. |
| 0:25 | 13–16 | Machine B · sequences | RNN state, then the four-step Transformer interaction. | | On slide 16: Tokens → Context → Training → Generation. Click different positions in Context. Replay Training to show parallel positions, then Generation to show tokens arriving in sequence. Keys 1–4 select a tab; Space advances/replays. Whole-word tokens and equal connection widths are teaching simplifications. |
| 0:42 | 17–19 | Reasoning and rewards | Work through the 60-minute workshop problem. Introduce pretraining, demonstrations and reinforcement learning. | | Let students solve it before reading the steps. Distinguish changing weights during training from spending time reasoning during a reply. Rewards can come from checks or human preferences; reward quality matters. |
| 0:52 | 20–22 | The model speaks | Three slides authored in the assistant’s own voice. | | Frame as an invited perspective from a frontier language model. Read aloud: what it is, how to collaborate, how to check it. Its account of itself is generated text too. |
| 1:00 | 23–25 | Question answering → agents | One evidence-based answer versus an agent choosing another action. | | Use the visitor FAQ consistently. Retrieval can be a fixed workflow or an agent tool. |
| 1:10 | 26–34 | Tools and harnesses | State the goal; follow one tool request and the loop; show Machine A/B cooperation. | | On 32, use the tray/ribbon metaphor briefly; on 33, make it concrete: the model drafts, software controls tool access, a person reviews. |
| 1:30 | 35 | **Break, 10 min** | Prepare the demo. | | |
| 1:40 | 36–38 | Live demos | Gio demos two or three harnesses; students track task, context, tools, control, trace and stop. | | Use the same brief. Show an actual tool result and an enforced boundary. |
| 1:58 | 39–42 | **Exercise: one task, one agent loop** | Pairs write a bounded task (8 min), run and observe (15 min), revise and compare (12 min). | | Allow five minutes for transitions. Preserve the second run. |
| 2:38 | 43–44 | Debrief | Two or three pairs explain how a tool result changed the next action. | Short answer | Ask for the trace and what they verified. |
| 2:45 | 45–51 | Challenge 3, reflection, close | Brief Week 5 challenge and Week 7 reflection; connect Machine A/B to evidence from experiments. | | Submit on Canvas. Close with the next two material weeks: images/video/layout, then audio/music. |

If a harness login fails, pairs can analyse the projected demo trace and complete the same task brief. If the class is behind, shorten the demos to two systems and keep the exercise's second run; that comparison is the main hands-on learning.

## Exercise: one task, one agent loop

The paired exercise follows the live demo and has three stages:

1. **Write the task, 8 minutes.** Choose a public, low-risk design task (for example, compare three public precedents, draft a visitor FAQ from a public event page, or check a short public text against a checklist). Write the goal, output, allowed sources and one thing the agent must not do.
2. **Run and observe, 15 minutes.** Keep tool settings visible. Record the first tool call, what came back, what changed in context, and whether a person approved an action. Check one claim against its source.
3. **Revise and run again, 12 minutes.** Change one condition only: the brief, source, permission or stop rule. Compare the second result and write what improved and what still needs a person's judgement.

Keep a copy of the prompt, one trace excerpt, the output and the student's own edit. If the tool hides its trace, have the pair note what they could not inspect; that is part of the interface critique.

## Challenge 3 · bring to Week 5

Ask a language model to draft a brief for a small design task, then edit the draft yourself. Keep:

- the prompt or task brief;
- the first, unedited model draft, with the model and harness named;
- the edited version, with at least one change or rejection explained;
- one observation about a decision the model or agent made, including a tool result if tools were used.

Bring all four pieces to Week 5. The evidence can also support the reflection, but Challenge 3 does not replace the Week 7 reflection assignment.

## Individual reflection · 20% · due Week 7

The assignment asks for about 1,000 words on **the role of AI in the student's creative process**, with particular attention to Machine A and Machine B. Students must use at least three of their own Week 2–6 experiments and include images; connect those examples to course ideas, tools or readings; and end with a short process note on using AI to write the reflection. They should name the tools and check every fact and source. The approved rubric is 30% concepts, 30% argument, 20% evidence, 10% clarity and 10% originality. The process note is required; a missing note lowers the clarity criterion by one grade band. Submit on Canvas.

## ClassPoint questions

| Slide | Type | Question | Use |
|---:|---|---|---|
| 3 | Short answer | From the LLM video: what can a language model predict? | Surface what students retained from the playlist video. |
| 13 | Multiple choice | What is ELIZA doing in this example? | Check that students recognise pattern matching and a written transformation. |
| 22 | Multiple choice | A bot searches one policy page, then writes one answer. Is it an agent? | Check fixed workflow vs dynamically selected tools. |
| 37 | Multiple choice | Where did your design judgement matter most? | Debrief the goal, permission and verification choices. |

## Sources and teaching material

- The Week 2 and Week 3 slide decks and lesson plans: the course's rule/spec and learned-example foundations.
- 2025 SD5913 Week 4 PDF and summary: the progression from ordinary control flow and browser interactions to local LLM chat interfaces.
- Chomsky, *Aspects of the Theory of Syntax* (1965); Weizenbaum, “ELIZA” (1966); Elman, “Finding Structure in Time” (1990); Vaswani et al., “Attention Is All You Need” (2017); Lewis et al., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” (2020); Yao et al., “ReAct” (2022).
- Anthropic, [“Building Effective AI Agents”](https://www.anthropic.com/engineering/building-effective-agents); Anthropic, [“Scaling Managed Agents”](https://www.anthropic.com/engineering/managed-agents); OpenAI, [“The Next Evolution of the Agents SDK”](https://openai.com/index/the-next-evolution-of-the-agents-sdk/).

## Revision notes and visual provenance

- PR #3 reviewed for the token/attention teaching sequence and the bridge from a Week 2 spec to a Week 4 brief. Its dense interface demonstrations were simplified for this audience.
- The 2025 PDF is `~/dev/sd5913/2025/SD5913 - PFAD - Week 4.pdf`; the searchable summary is `~/dev/course-kb/corpus/sd5913-2025-week04.md`. The reusable link is control flow, not a programming exercise.
- Slides 20 and 32 use text-free Easel `qwen-image-2.1` images. Exact prompts, endpoint and purpose are in the adjacent asset JSON files; `tools/generate_week04_images.py` regenerates them using the ignored local environment key. Both illustrations are metaphors, not technical diagrams.
- Technical diagrams use native slide text and shapes. Slide 16 uses Inter in p5.js, keyboard controls and reduced-motion support. Its print companion summarises parallel training and sequential generation.
- Reasoning and training references: Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762); Ouyang et al., [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155); DeepSeek-AI, [DeepSeek-R1](https://arxiv.org/abs/2501.12948). The workshop example is an authored teaching example, not a recorded model run.
