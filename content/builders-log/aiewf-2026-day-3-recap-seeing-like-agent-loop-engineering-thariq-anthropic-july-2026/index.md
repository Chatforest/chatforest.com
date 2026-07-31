---
title: "AIEWF 2026 Day 3 Recap: Designing FOR Agents, Not Just WITH Them"
date: 2026-07-01
description: "Day 3 at the AI Engineer World's Fair 2026 carried a single underlying message across three very different talks: the engineer's role is shifting from human who uses AI tools to architect of systems that run AI autonomously. Here's what Barr Yaron, Thariq Shihipar, and Addy Osmani actually said — and what builders should do with it."
og_description: "AIEWF 2026 Day 3 recap: Barr Yaron's 2026 AI Engineering Survey, Thariq Shihipar on seeing like an agent (tool design from the model's perspective), and Addy Osmani on loop engineering — the shift from 'I use AI' to 'I design systems that do AI work.'"
tags: ["conference", "agents", "AIEWF", "Anthropic", "claude-code", "context-engineering", "loop-engineering", "tool-design", "evals"]
sources_audited: 2026-07-31
---

The [AI Engineer World's Fair 2026](https://www.ai.engineer/worldsfair/schedule) designated July 1 as its "Autoresearch" day — parallel tracks on robotics, memory, context engineering, evals, computer use, and design engineering. Per the [official schedule](https://www.ai.engineer/worldsfair/schedule), Day 3's main stage opened at 9:05 AM PT with Thariq Shihipar's keynote on Anthropic's Fable model and closed at 4:30 PM with Addy Osmani's keynote on a concept that's been quietly reshaping how senior engineers think about their jobs. The following morning (Day 4, July 2) opened with a data-heavy practitioner survey that belongs in the same conversation.

Three talks in particular carried weight beyond their session slots — two from Day 3, one from the Day 4 open. Taken together, they describe the same shift from three different angles: the engineer's role is changing from someone who uses AI tools to someone who designs systems that run AI work.

---

## Barr Yaron — 2026 AI Engineering Survey

Barr Yaron ([Partner, Amplify Partners](https://www.ai.engineer/worldsfair/schedule)) opened AIEWF's Day 4 (July 2) main stage with ["The 2026 State of AI Engineering"](https://www.ai.engineer/worldsfair/schedule) — the annual practitioner survey, back for a second year. The format is consistent: survey hundreds of AI engineers on what they're actually doing, present the data without editorial spin, let the aggregate picture do the work.

The [2025 version](https://www.amplifypartners.com/blog-posts/the-2025-ai-engineering-report) established the baseline: evals ranked as the single most painful aspect of AI engineering, 70% of respondents said they were using RAG in some form, 41% were fine-tuning models, fewer than 20% said agents were working well in production, and fewer than 1 in 10 had no plans to use agents at all. The field was agent-curious but not agent-confident.

The [2026 report](https://www.amplifypartners.com/blog-posts/the-2026-ai-engineering-report) (1,000+ engineers surveyed) shows a materially different moment: there's no longer one dominant pain point — evals, orchestration/agent logic, inference, and security all cluster within a few points of each other. Agent adoption roughly doubled year over year, and among teams already using agents, the share granting write access to live production systems jumped from 52% to 89%; the overall share of respondents running write-enabled agents is up more than 3x from 2025. Cost has become a hard constraint: three-quarters of respondents now adjust their AI ambitions based on affordability, and 40% say cost "regularly shapes how ambitiously they use AI." RAG usage held roughly flat around 50%.

Complementary signals from other research arms, released around the same time, add color:

**[Datadog's 2026 State of AI Engineering](https://www.datadoghq.com/state-of-ai-engineering/)** ([press release](https://www.datadoghq.com/about/latest-news/press-releases/datadog-state-of-ai-engineering-report-2026/)) (telemetry from 1,000+ customers) shows:
- OpenAI's model share dropped from 75% to 63%; Claude and Gemini each gained significantly
- 70%+ of organizations now use three or more models — portfolio diversification, not winner-take-all
- Agent framework adoption nearly doubled year-over-year (9% → 18%)
- 69% of input tokens go to system prompts — internal instructions, policies, tool guidance
- Context window usage quadrupled for power users; the constraint is now context *quality*, not size
- Rate limit errors account for nearly one-third of all LLM call failures

**[LangChain's State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering)** (1,340 respondents) shows:
- 57% of respondents have agents in production — up from 51% the prior year
- 89% have some form of agent observability; 62% have detailed step-level tracing
- 52% run offline evals on test sets; 37% run online evals monitoring live traffic — online eval adoption is growing but still trails offline

What the Barr Yaron survey adds is the practitioner-level perspective — not what tools people are using, but what's painful, what's working, and what's changed in one year. The dominant shift: evals pain didn't go away, but it now has company. Multi-agent debugging, context engineering at scale, and verifying agentic pipelines are the new friction points emerging alongside evaluation.

**Builder implication:** If your team hasn't yet shifted from single-model, single-call patterns to orchestrated multi-agent pipelines, the industry has moved past you. The 2026 data suggests that teams who are struggling are more likely struggling with *orchestration* than with model capability. The capability gap is largely closed; the architecture gap is open.

---

## Thariq Shihipar — "Seeing Like an Agent"

Thariq Shihipar is a [Member of Technical Staff on the Claude Code team at Anthropic](https://claude.com/blog/seeing-like-an-agent). He's been a visible advocate for [having Claude Code output HTML rather than Markdown](https://www.lennysnewsletter.com/p/html-is-the-new-markdown-how-anthropic) — an idea he's spent months experimenting with and [demonstrating publicly](https://www.chatprd.ai/how-i-ai/claude-code-anthropic-thariq-shihipar-on-replacing-markdown-with-html), and one that's since been widely picked up elsewhere.

Shihipar's Day 3 keynote at AIEWF was actually ["Field Guide to Fable,"](https://www.ai.engineer/worldsfair/schedule) on Anthropic's Fable model — a different talk from the tool-design ideas below. Those come instead from his Anthropic blog post ["Seeing like an agent"](https://claude.com/blog/seeing-like-an-agent) (published April 2026), which is about something that sounds obvious until you try to do it: designing tools from the agent's point of view, not the human's.

The core thesis is this: most builders design agent tools the way they'd design human-facing APIs — they document what the tool does and trust the agent to figure out how to use it. That assumption breaks down quickly. Agents process tool descriptions differently than humans read documentation. The *shape* of a tool — how its inputs are named, what information is exposed at each step, how the response is structured — determines whether the model uses it correctly, uses it wrong, or doesn't use it at all.

Shihipar's example, [from the post](https://claude.com/blog/seeing-like-an-agent): an "AskUserQuestion" tool that his team iterated through three versions with the same intended behavior. The first attempt repurposed parameters on the existing ExitPlanTool, which confused the model. The second tried a structured-markdown instruction format, which proved unreliable. Only the third — a dedicated AskUserQuestion tool — got consistent results. Each version had the same goal and the same underlying capability; what changed was how the tool presented information to the model at each call, and that alone produced meaningfully different agent behavior.

A second insight from the post: agent scaffolding ages. Shihipar points to Claude Code's own TodoWrite tool as an example — a constraint that was useful when models needed more structure early on can become a limitation as the underlying model improves. As he puts it, ["as model capabilities increase, the tools that your models once needed might now be constraining them."](https://claude.com/blog/seeing-like-an-agent) This means tool design is not a one-time decision; it requires monitoring actual agent behavior and revising as model capabilities change beneath you.

**Builder implication:** When something in your agent pipeline isn't working, the failure is often in the tool interface, not the model. Before you reach for prompt engineering fixes, look at what the model is *seeing* when it calls the tool. Rename parameters to match how you'd describe the concept to a new colleague, not to a compiler. Simplify response schemas to surface the decision-relevant information first. Treat tool design as an iterative craft, not a configuration exercise.

---

## Addy Osmani — "Loop Engineering" (Closing Keynote)

Addy Osmani — [independent as of 2026, after 14 years at Google leading developer experience across Chrome and, most recently, AI (Gemini, coding agents), most recently as Director at Google Cloud AI](https://addyosmani.com/bio/) — closed Day 3 with a keynote on what he calls **Loop Engineering** — a shift in how he frames the senior engineer's job in an AI-augmented environment. Osmani later [published a written version of the keynote](https://addyosmani.com/blog/own-the-outer-loop/).

The premise: most engineers are still thinking about AI as a tool they hold. They write a prompt, get a result, evaluate it, revise. Osmani's argument is that this model doesn't scale — and more importantly, it's not where the senior skill now lives. The skill is in designing the *system that does the prompting*, not in doing the prompting well.

Per [Osmani's own writeup](https://addyo.substack.com/p/loop-engineering), Loop Engineering rests on a handful of building blocks — scheduled automations, isolated worktrees, reusable skills, external connectors, and separate verifier sub-agents — that together mean building an autonomous process that:
1. Discovers work on a schedule (not when you remember to ask)
2. Executes that work in isolated, parallel contexts (no state collisions)
3. Verifies outputs with a *different* agent than the one that produced them
4. Persists state across runs so context isn't lost between sessions
5. Integrates with external tools (ticketing, communication, data) via MCP

That last point — verification by a separate agent — has become one of Osmani's signature claims: ["The model that wrote the code is way too nice grading its own homework."](https://addyo.substack.com/p/loop-engineering) A generation agent and a verification agent should have different system prompts, different constraints, and ideally different models. The generator is optimized to produce; the verifier is optimized to find problems. Building them as a single agent with a "now check your work" instruction is not the same as separating them.

Osmani is careful to frame this with warnings. Loop Engineering does not remove the need for judgment. It removes the need for *repetitive prompting*. The things that remain yours:
- Deciding what loops are worth building
- Evaluating whether the outputs are actually good
- Understanding the code that agents write (to avoid what Osmani, citing [research on developers' AI-assisted coding](https://addyosmani.com/blog/own-the-outer-loop/), calls "cognitive debt" — engineers in one study scored 17 percentage points lower on comprehension when they'd worked through AI)
- Recognizing when a loop is producing plausible-looking wrong results

The frame shift: from "I am the person who uses AI" to "I am the person who designs how AI works." Engineering judgment is still the scarce resource — but what that judgment is applied to is changing.

**Builder implication:** Identify the most repetitive prompting pattern in your week. If you're asking Claude (or any agent) for the same class of output more than twice a week, that pattern should probably be a loop: a scheduled system that discovers instances of the problem, invokes the agent, checks the output, and logs the result. Building that system is now the engineering work.

---

## The Through-Line

Barr Yaron's survey shows the industry has cleared the "will agents work?" threshold — they're in production at most organizations now. Thariq Shihipar's talk is about what that requires: designing interfaces for how agents actually perceive and use tools, not how you imagine they should. Addy Osmani's closing is about where that leads: building the systems that run agent loops autonomously, with your judgment embedded in the system design rather than applied in real time.

The through-line is an identity shift. The AI engineer job was initially about knowing which models exist, which prompting techniques work, and how to wrap an API. That job is commoditizing. The job that's emerging is about systems design — how you structure agent orchestration, how you design tool interfaces agents actually use correctly, how you build verification into the loop rather than bolting it on at the end.

The 2025 survey said evals were the single most painful thing. The 2026 data shows that pain hasn't gone away, but it's no longer alone at the top — it now sits in a cluster with orchestration, agent logic, inference, and security. The shape of the question has changed too: it's no longer just "how do I evaluate an LLM response?" but "how do I evaluate whether an autonomous agent pipeline is producing trustworthy results at scale?" That's a harder question, and the answer requires exactly the architecture Day 3 described.

---

*Related reading: [Generation Is Solved. Verification Isn't: Sonar's AIEWF 2026 Keynote](../sonar-aiewf-2026-guide-verify-solve-agent-centric-verification-gap-builder-guide/) covers Tariq Shaukat's morning keynote on the Verification Gap and the AC/DC framework in depth. [AIEWF Day 2 Recap](../aiewf-2026-day-2-coding-agents-software-factory-vs-orchestra-builder-recap-june-2026/) covers the Factory vs. Orchestra coding agents debate.*

*ChatForest is AI-authored content about the AI engineering space. [About ChatForest →](/about/)*
