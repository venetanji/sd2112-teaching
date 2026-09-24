# SD2112 · Week 4 lesson plan

**Language machines: from rules to agents** · three-hour lecture-workshop (about 170 minutes of class plus a 10-minute break) · deck: `week04-classpoint.pptx` (45 slides, from the *Build PowerPoints* workflow artifact or a local build) · web: `venetanji.github.io/sd2112-teaching/week04/` (`SD2112-week04.pdf` next to it)

## Purpose of this session

For us:

1. Reconnect the first three weeks through **Machine A** (written rules) and **Machine B** (patterns learned from examples); let students carry that distinction into language.
2. Separate a theory of human language from a language program: Chomsky's generative grammar and Universal Grammar are theories about linguistic structure and acquisition; ELIZA applies hand-written patterns.
3. Explain the move from recurrent state to transformer attention, and follow a prompt from tokens and embeddings to next-token generation, instruction tuning, and a user-facing chatbot.
4. Distinguish a fixed question-answering workflow from an agent that can choose a tool, inspect its result, and continue or stop; show how a harness shapes that loop.
5. Let students observe the harness in a live demo, then run and revise one bounded design task. Brief Challenge 3 and the Week 7 individual reflection.

For students, by the end of the class they can:

- contrast a written language rule with a pattern learned from examples;
- describe the difference between Chomsky's account of human language acquisition and an explicit grammar or program;
- explain, at a high level, how an RNN carries state, how a transformer uses attention, and how a language model generates a reply one token at a time;
- distinguish a fixed retrieve-and-answer path from an agent loop that selects tools based on observations;
- identify what an agent harness lets a system see and do, what it records, and where a person can intervene;
- preserve a prompt, an unedited draft, and a considered edit as evidence for Challenge 3 and the reflection.

## The 2025 reference

The 2025 Week 4 PDF/summary is from **SD5913's programming-for-designers course**, so treat it as a teaching reference, not as a prior SD2112 syllabus. Its sequence moves from input and buttons through loops, polling, events/callbacks and browser interfaces, then into local and remote LLM chatbots and agent frameworks (LangChain, LangGraph, Langflow and n8n). Carry forward the most useful bridge: an agent still runs inside ordinary program control flow. The harness owns the loop, routes calls and returns observations; the model may choose the next action. That makes the agent legible as a designed system rather than a disembodied chatbot.

The current SD2112 sequence assumes the programming exercises are not the goal today. Keep the old material as a short analogy in the speaker notes and spend the classroom time on language, tools, control and design judgement.

## Before class (TAs, from 30 minutes before)

| Who | Task |
|---|---|
| Nicolò | Classroom PC: open `week04-classpoint.pptx` and keep the join code visible on slide 1. Fire the short-answer and multiple-choice activities once, then reset them. Open the Week 4 web deck as backup; speaker notes are under `S`. |
| Amber | Post the Week 4 deck and PDF to Canvas with the Challenge 3 brief. Once Gio supplies the Week 7 reflection submission link, include it in the Canvas announcement. |
| WU Zhao, MA Jie | Help students join ClassPoint and pair up; during the exercise, help with access to the demo harnesses, keep tasks bounded and ask students to capture one tool result. |
| Gio | Choose two or three harnesses for the demo and test logins, tool access and visible traces. Create the Week 7 Canvas reflection submission link and share it with Amber for posting. Use the same low-risk task across demos where practical. |

## Run of show

| Time | Slides | Segment | What happens | ClassPoint | Notes |
|---|---:|---|---|---|---|
| 0:00 | 1–7 | Welcome and recall | Video warm-up; Machine A/B; map weeks 1–3 onto rules, examples and actions. | Short answer | Ask what a language model predicts. Let the responses identify what needs a quick explanation. |
| 0:10 | 8–13 | Machine A · language as rules | Chomsky; generative rules; a deliberately small phrase tree; ELIZA's DOCTOR script; one pattern and its transformation. | Multiple choice | Keep the distinction precise: Universal Grammar is a theory about human language acquisition, not a computer grammar. ELIZA applies authored rules; its fluency does not prove understanding. |
| 0:30 | 14–18 | Machine B · learned sequences | RNN state; RNN vs transformer; tokenisation, embeddings, attention and next-token generation; base vs instruction-tuned models. | | Ask students to narrate one generation loop from prompt to stop token. Mention hallucination and sycophancy as reasons to check claims against evidence. |
| 1:00 | 19–22 | Question answering → agents | Retrieval-augmented answers; fixed FAQ, one-pass RAG and agent; distinguish a chat interface from an agent. | Multiple choice | A fixed retrieve-and-answer path can be a workflow. Retrieval can also be a tool an agent chooses. |
| 1:15 | 23–28 | Agent loop and harness | Goal, model, tool call, observation, next turn; tool boundaries; failure modes; harness as the designed system around the model. | | Use the 2025 programming-course bridge: event loops and callbacks are familiar control structures; today the model may select a next action inside the harness's loop. |
| 1:35 | 29 | **Break, 10 min** | Keep demo tools ready; students return to pairs. | | |
| 1:45 | 30–32 | Live demos | Gio demos two or three harnesses before the exercise. Students track task, context, tools, control, trace and stop condition. | | Use the same low-risk brief if the harnesses allow it. Do not use private or client-confidential material. |
| 2:00 | 33–36 | **Exercise: one task, one agent loop** | Pairs define a bounded design task (8 min), run and record one tool call (15 min), change one condition and compare the second run (12 min), with transitions. | | One device per pair. The exercise is about the system and the choices it makes, not a contest for the best output. |
| 2:38 | 37–38 | Debrief | Compare where judgement mattered, what the harness exposed, and what needs a person. Keep prompt, trace, output and edit. | Multiple choice | Invite two or three concrete examples. |
| 2:45 | 39–45 | Challenge 3, reflection, close | Brief Challenge 3 for Week 5; explain the Week 7 reflection, evidence requirement, Canvas link and rubric; preview image/video/layout and audio/music weeks. | | Gio creates the Canvas submission link. End with the designer's role in setting goals, tools, boundaries and judgement. |

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

The assignment asks for about 1,000 words on **the role of AI in the student's creative process**, with particular attention to rule-based and adaptive systems. Students must use at least three of their own Week 2–6 experiments and include images; connect those examples to course ideas, tools or readings; and end with a short process note on using AI to write the reflection. They should name the tools and check every fact and source. The approved rubric is 30% concepts, 30% argument, 20% evidence, 10% clarity and 10% originality. The process note is required; a missing note lowers the clarity criterion by one grade band. Submission is through the Week 7 Canvas link, which Gio will create.

## ClassPoint questions

| Slide | Type | Question | Use |
|---:|---|---|---|
| 3 | Short answer | From the LLM video: what can a language model predict? | Surface what students retained from the playlist video. |
| 13 | Multiple choice | What is ELIZA doing in this example? | Check that students recognise pattern matching and a written transformation. |
| 22 | Multiple choice | A bot searches one policy page, then writes one answer. Is it an agent? | Check fixed workflow vs dynamically selected tools. |
| 37 | Multiple choice | Where did your design judgement matter most? | Debrief the goal, permission and verification choices. |

## Sources and teaching material

- The Week 2 and Week 3 slide decks and lesson plans: the course's rule/spec and learned-example foundations.
- 2025 SD5913 Week 4 PDF and summary: the progression from ordinary control flow and browser interactions to LLM chat and agent frameworks.
- Chomsky, *Aspects of the Theory of Syntax* (1965); Weizenbaum, “ELIZA” (1966); Elman, “Finding Structure in Time” (1990); Vaswani et al., “Attention Is All You Need” (2017); Lewis et al., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” (2020); Yao et al., “ReAct” (2022).
- Anthropic, [“Building Effective AI Agents”](https://www.anthropic.com/engineering/building-effective-agents); Anthropic, [“Scaling Managed Agents”](https://www.anthropic.com/engineering/managed-agents); OpenAI, [“The Next Evolution of the Agents SDK”](https://openai.com/index/the-next-evolution-of-the-agents-sdk/).
