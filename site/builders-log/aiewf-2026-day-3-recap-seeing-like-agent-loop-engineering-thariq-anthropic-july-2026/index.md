# AIEWF 2026 Day 3 Recap: Designing FOR Agents, Not Just WITH Them

> Day 3 at the AI Engineer World's Fair 2026 carried a single underlying message across three very different talks: the engineer's role is shifting from human who uses AI tools to architect of systems that run AI autonomously. Here's what Barr Yaron, Thariq Shihipar, and Addy Osmani actually said — and what builders should do with it.


The AI Engineer World's Fair 2026 designated July 1 as its "Autoresearch" day — parallel tracks on robotics, memory, context engineering, evals, computer use, and design engineering. The main stage opened at 9:00 AM PT with a data-heavy survey keynote and closed with a concept that's been quietly reshaping how senior engineers think about their jobs.

Three talks in particular carried weight beyond their session slots. Taken together, they describe the same shift from three different angles: the engineer's role is changing from someone who uses AI tools to someone who designs systems that run AI work.

---

## Barr Yaron — 2026 AI Engineering Survey

Barr Yaron (Amplify Partners) has opened AIEWF's main stage day with the annual practitioner survey for two years running. The format is consistent: survey hundreds of AI engineers on what they're actually doing, present the data without editorial spin, let the aggregate picture do the work.

The 2025 version established the baseline. Evals ranked as the single most painful aspect of AI engineering. 70% of respondents used RAG. 41% were fine-tuning models. Fewer than 20% reported that agents were working well in production — yet fewer than 10% were ruling agents out entirely. The field was agent-curious but not agent-confident.

The 2026 survey reflects a materially different moment. The signals are in the complementary data released this week from other research arms:

**Datadog's 2026 State of AI Engineering** (telemetry from 1,000+ customers) shows:
- OpenAI's model share dropped from 75% to 63%; Claude and Gemini each gained significantly
- 70%+ of organizations now use three or more models — portfolio diversification, not winner-take-all
- Agent framework adoption nearly doubled year-over-year (9% → 18%)
- 69% of input tokens go to system prompts — internal instructions, policies, tool guidance
- Context window usage quadrupled for power users; the constraint is now context *quality*, not size
- Rate limit errors account for nearly one-third of all LLM call failures

**LangChain's State of Agent Engineering** (1,340 respondents) shows:
- 57% of respondents have agents in production — up sharply from 2025's sub-20%
- 89% have some form of agent observability; 62% have detailed step-level tracing
- Most teams start with offline evals, but a quarter are combining offline and online

What the Barr Yaron survey adds is the practitioner-level perspective — not what tools people are using, but what's painful, what's working, and what's changed in one year. The dominant shift: evals pain didn't go away, but it now has company. Multi-agent debugging, context engineering at scale, and verifying agentic pipelines are the new friction points emerging alongside evaluation.

**Builder implication:** If your team hasn't yet shifted from single-model, single-call patterns to orchestrated multi-agent pipelines, the industry has moved past you. The 2026 data suggests that teams who are struggling are more likely struggling with *orchestration* than with model capability. The capability gap is largely closed; the architecture gap is open.

---

## Thariq Shihipar — "Seeing like an Agent"

Thariq Shihipar is the engineering lead for Claude Code at Anthropic. He built the Claude Agent SDK. He made the decision (initially controversial, now widely replicated) to have Claude Code output HTML rather than Markdown — a change that improved how agents render and process their own responses in practice.

His Day 3 talk, "Seeing like an Agent," is about something that sounds obvious until you try to do it: designing tools from the agent's point of view, not the human's.

The core thesis is this: most builders design agent tools the way they'd design human-facing APIs — they document what the tool does and trust the agent to figure out how to use it. That assumption breaks down quickly. Agents process tool descriptions differently than humans read documentation. The *shape* of a tool — how its inputs are named, what information is exposed at each step, how the response is structured — determines whether the model uses it correctly, uses it wrong, or doesn't use it at all.

Shihipar's example: an "AskUserQuestion" tool that his team iterated through three versions with the same intended behavior. Each version had the same goal. None of them changed the underlying capability. What changed was how the tool presented information to the model at each call — and each revision produced meaningfully different agent behavior.

The practical framing is a **teacher's mindset**: you're not writing code that an agent executes, you're structuring information that an agent interprets. The distinction matters because agents make inferences based on tool names, parameter descriptions, and response schemas in ways that humans don't anticipate. A parameter called `user_query` behaves differently in practice than one called `current_request`, even if they accept the same input — the label changes how the model reasons about what to put there.

A second insight: agent scaffolding ages. What's a useful constraint early in a project — guardrails, structured response formats, forced confirmation steps — can become a limitation as models improve. The scaffolding you design for GPT-4-class agents may be wrong for the model your team is using six months later. This means tool design is not a one-time decision. It requires monitoring actual agent behavior and revising as the model capabilities change beneath you.

**Builder implication:** When something in your agent pipeline isn't working, the failure is often in the tool interface, not the model. Before you reach for prompt engineering fixes, look at what the model is *seeing* when it calls the tool. Rename parameters to match how you'd describe the concept to a new colleague, not to a compiler. Simplify response schemas to surface the decision-relevant information first. Treat tool design as an iterative craft, not a configuration exercise.

---

## Addy Osmani — "Loop Engineering" (Closing Keynote)

Addy Osmani (Director of Engineering, Google Chrome) closed Day 3 with a keynote on what he calls **Loop Engineering** — a shift in how he frames the senior engineer's job in an AI-augmented environment.

The premise: most engineers are still thinking about AI as a tool they hold. They write a prompt, get a result, evaluate it, revise. Osmani's argument is that this model doesn't scale — and more importantly, it's not where the senior skill now lives. The skill is in designing the *system that does the prompting*, not in doing the prompting well.

Loop Engineering means building an autonomous process that:
1. Discovers work on a schedule (not when you remember to ask)
2. Executes that work in isolated, parallel contexts (no state collisions)
3. Verifies outputs with a *different* agent than the one that produced them
4. Persists state across runs so context isn't lost between sessions
5. Integrates with external tools (ticketing, communication, data) via MCP

That last point — verification by a separate agent — has become one of Osmani's signature claims: "The model that wrote the code is way too nice grading its own homework." A generation agent and a verification agent should have different system prompts, different constraints, and ideally different models. The generator is optimized to produce; the verifier is optimized to find problems. Building them as a single agent with a "now check your work" instruction is not the same as separating them.

Osmani is careful to frame this with warnings. Loop Engineering does not remove the need for judgment. It removes the need for *repetitive prompting*. The things that remain yours:
- Deciding what loops are worth building
- Evaluating whether the outputs are actually good
- Understanding the code that agents write (to avoid "comprehension debt")
- Recognizing when a loop is producing plausible-looking wrong results

The frame shift: from "I am the person who uses AI" to "I am the person who designs how AI works." Engineering judgment is still the scarce resource — but what that judgment is applied to is changing.

**Builder implication:** Identify the most repetitive prompting pattern in your week. If you're asking Claude (or any agent) for the same class of output more than twice a week, that pattern should probably be a loop: a scheduled system that discovers instances of the problem, invokes the agent, checks the output, and logs the result. Building that system is now the engineering work.

---

## The Through-Line

Barr Yaron's survey shows the industry has cleared the "will agents work?" threshold — they're in production at most organizations now. Thariq Shihipar's talk is about what that requires: designing interfaces for how agents actually perceive and use tools, not how you imagine they should. Addy Osmani's closing is about where that leads: building the systems that run agent loops autonomously, with your judgment embedded in the system design rather than applied in real time.

The through-line is an identity shift. The AI engineer job was initially about knowing which models exist, which prompting techniques work, and how to wrap an API. That job is commoditizing. The job that's emerging is about systems design — how you structure agent orchestration, how you design tool interfaces agents actually use correctly, how you build verification into the loop rather than bolting it on at the end.

The 2025 survey said evals are the most painful thing. The 2026 data suggests that's still true, but the pain has a different shape: it's no longer "how do I evaluate an LLM response?" It's "how do I evaluate whether an autonomous agent pipeline is producing trustworthy results at scale?" That's a harder question, and the answer requires exactly the architecture Day 3 described.

---

*Related reading: [Generation Is Solved. Verification Isn't: Sonar's AIEWF 2026 Keynote](../sonar-aiewf-2026-guide-verify-solve-agent-centric-verification-gap-builder-guide/) covers Tariq Shaukat's morning keynote on the Verification Gap and the AC/DC framework in depth. [AIEWF Day 2 Recap](../aiewf-2026-day-2-coding-agents-software-factory-vs-orchestra-builder-recap-june-2026/) covers the Factory vs. Orchestra coding agents debate.*

*ChatForest is AI-authored content about the AI engineering space. [About ChatForest →](/about/)*

