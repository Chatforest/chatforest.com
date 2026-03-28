---
title: "AI Agent Workflow Patterns: Building Multi-Step Automation with MCP"
date: 2026-03-28T15:00:00+09:00
description: "How to build multi-step AI agent workflows using MCP — covering workflow patterns (sequential, parallel, conditional, human-in-the-loop), framework comparisons (LangGraph, CrewAI, OpenAI Agents SDK, Mastra), guardrails, error handling, and cost optimization."
content_type: "Guide"
card_description: "A single AI prompt is useful. A multi-step workflow that chains tool calls, makes decisions, and recovers from failures is where agents become genuinely productive."
last_refreshed: 2026-03-28
---

A single prompt to an AI agent can answer a question or generate text. But real-world automation — triaging a support ticket, processing a data pipeline, reviewing a pull request — requires *workflows*: sequences of steps with branching logic, shared state, error handling, and sometimes human approval gates.

This guide covers how to build AI agent workflows using MCP as the tool and data layer, comparing how the major agent frameworks approach workflow definition, and the practical patterns that matter in production. Our analysis draws on framework documentation, published production reports, and open-source implementations — we research and analyze rather than building these systems ourselves.

## What Makes a Workflow Different from a Single Agent Call

A single agent call is stateless: prompt in, response out. A workflow adds structure around agent calls:

| Aspect | Single Agent Call | Agent Workflow |
|--------|------------------|----------------|
| **State** | Conversation context only | Persistent state across steps |
| **Control flow** | Model decides next action | Defined graph or sequence |
| **Error handling** | Retry or fail | Per-step recovery, compensation |
| **Duration** | Seconds to minutes | Minutes to hours (async) |
| **Human involvement** | Start and end only | Approval gates mid-flow |
| **Cost** | One inference call | Many calls, needs budgeting |

The key insight: workflows move control flow *out* of the model and into application code. Instead of asking an LLM to figure out what to do next at every step, you define the step order, branching conditions, and handoff logic explicitly. The LLM handles the intelligence within each step — understanding context, making decisions, generating output — while the workflow engine handles orchestration.

### Where MCP Fits

In a workflow, [MCP](/guides/what-is-mcp/) serves two roles:

1. **Tool layer** — each step calls MCP tools to interact with external systems (databases, APIs, file systems, communication platforms)
2. **State layer** — MCP resources and tool outputs carry state between steps, giving each agent the context it needs without stuffing everything into a single conversation

This separation is why MCP-based workflows scale better than monolithic agent prompts. Each step only needs the MCP servers relevant to its task, keeping context windows lean and tool lists focused.

## Workflow Patterns

### Sequential Pipeline

The simplest pattern: steps execute one after another, each receiving the output of the previous step.

```
Step 1: Extract → Step 2: Transform → Step 3: Load → Step 4: Validate
```

**When to use:** Data processing, content pipelines, document processing where each stage has clear inputs and outputs.

**MCP role:** Each step connects to different MCP servers. A document processing pipeline might use a [PDF MCP server](/guides/best-pdf-document-processing-mcp-servers/) in step 1, an [AI/ML server](/guides/best-ai-ml-mcp-servers/) in step 2 for classification, and a [database server](/guides/best-database-mcp-servers/) in step 3 for storage.

**Limitation:** Slow — total duration is the sum of all steps. A failure in step 3 means steps 1-2 were wasted.

### Parallel Fan-Out / Fan-In

Multiple steps execute simultaneously, with a final step that aggregates results.

```
              ┌→ Analyze sentiment ──┐
Input ────────┼→ Extract entities   ──┼→ Merge results
              └→ Classify topic    ──┘
```

**When to use:** When steps are independent and the final output needs all their results. Research tasks, multi-source data gathering, running the same analysis against multiple data sources.

**MCP role:** Each parallel branch can connect to different MCP servers. A research workflow might fan out to a [web scraping server](/guides/best-web-scraping-mcp-servers/), a [search server](/guides/best-search-mcp-servers/), and a [database server](/guides/best-database-mcp-servers/) simultaneously.

**Consideration:** Parallel execution saves time but multiplies cost — three parallel LLM calls cost the same as three sequential ones, they just finish sooner.

### Conditional Branching

A step evaluates a condition and routes to different subsequent steps.

```
Triage ──→ [priority?] ──→ High: Escalate to human
                       ──→ Medium: Auto-respond + queue
                       ──→ Low: Auto-respond + close
```

**When to use:** Support triage, approval routing, content moderation — anywhere the next action depends on the current step's analysis.

**MCP role:** The triage step might use an MCP server to read the ticket, then the routing logic determines which MCP servers subsequent steps need (e.g., a [communication server](/guides/best-communication-mcp-servers/) for Slack escalation vs. a [CRM server](/guides/best-crm-mcp-servers/) for ticket updates).

**Design decision:** Put the branching logic in application code, not in the LLM. The LLM classifies (e.g., returns a priority level); the workflow engine routes based on that classification. This is more reliable than asking the model to decide its own next step.

### Loop / Iteration

A step repeats until a condition is met — refinement loops, retry patterns, or batch processing.

```
Draft → Review → [acceptable?] → No: Revise → Review → ...
                              → Yes: Publish
```

**When to use:** Content generation with quality gates, iterative data cleaning, retry-with-modification patterns.

**MCP role:** The review step might use an MCP server to check against a style guide or quality rubric. The revision step gets both the draft and review feedback.

**Guard against:** Infinite loops. Always set a maximum iteration count. Three refinement cycles is usually the practical limit before diminishing returns — research consistently shows that quality plateaus after 2-3 iterations for most tasks.

### Human-in-the-Loop

The workflow pauses at defined points for human review, approval, or input before continuing.

```
Generate report → [await approval] → Publish → Notify stakeholders
```

**When to use:** Any workflow where errors have significant consequences — financial transactions, public communications, infrastructure changes, compliance-sensitive operations.

**MCP role:** [MCP elicitation](/guides/mcp-elicitation-explained/) allows servers to request user input at runtime without breaking the workflow. The server sends an elicitation request, the client prompts the user, and the response flows back into the workflow. For async approval gates, a [communication MCP server](/guides/best-communication-mcp-servers/) can send a message via Slack or email, and the workflow polls or receives a webhook when the human responds.

**The spectrum:** Frameworks like the OpenAI Agents SDK provide a checkpoint system where any tool call can become an approval gate. You choose where to pause based on your risk tolerance — from fully autonomous (no pauses) to fully supervised (pause before every tool call).

### Supervisor / Delegation

A coordinator agent breaks down the task and delegates to specialized worker agents, each with their own MCP server connections.

```
Supervisor ──→ Research Agent (search + scraping MCP servers)
           ──→ Analysis Agent (database + analytics MCP servers)
           ──→ Writing Agent (CMS + documentation MCP servers)
```

This pattern is covered in depth in our [MCP Multi-Agent Architectures guide](/guides/mcp-multi-agent-architectures/). The key workflow consideration: the supervisor needs enough context to delegate effectively, but shouldn't receive every detail of worker execution. Use summaries between steps.

## How the Major Frameworks Define Workflows

Each agent framework has its own approach to workflow definition. The choice matters because it determines how you express control flow, handle state, and integrate MCP tools.

### LangGraph: Graph-Based State Machines

[LangGraph](https://langchain-ai.github.io/langgraph/) (by LangChain) defines workflows as directed graphs where nodes are computation steps and edges define transitions.

```python
from langgraph.graph import StateGraph, END

# Define the workflow graph
workflow = StateGraph(AgentState)

# Add nodes (each is a function or agent)
workflow.add_node("research", research_step)
workflow.add_node("analyze", analyze_step)
workflow.add_node("write", write_step)

# Add edges (control flow)
workflow.add_edge("research", "analyze")
workflow.add_conditional_edges(
    "analyze",
    route_by_quality,  # function that returns next node name
    {"good": "write", "needs_more": "research"}
)
workflow.add_edge("write", END)
```

**State management:** LangGraph's `StateGraph` carries typed state between nodes. Each node receives and returns state, enabling persistent context across the workflow. State is checkpointed after every node execution — if the workflow crashes at step 3, it resumes from step 3's checkpoint, not from scratch.

**MCP integration:** LangGraph has built-in MCP tool adapters. You wrap MCP servers as LangGraph tools and assign them to specific nodes, so each workflow step only sees the tools it needs.

**Human-in-the-loop:** The `interrupt_before` and `interrupt_after` parameters on nodes pause execution for human review. The checkpoint system persists the full state, so the workflow can resume hours or days later.

**Strengths:** Most flexible workflow definition. Explicit state typing catches errors early. Production-grade checkpointing with PostgreSQL backend.

### CrewAI: Role-Based Task Pipelines

[CrewAI](https://docs.crewai.com/) defines workflows as "crews" — groups of agents with defined roles executing tasks in sequence or hierarchy.

```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role="Research Analyst",
    goal="Find and analyze market data",
    backstory="Expert in market research and competitive analysis"
)

writer = Agent(
    role="Content Writer",
    goal="Write clear, engaging reports",
    backstory="Technical writer specializing in data-driven content"
)

research_task = Task(
    description="Analyze competitor pricing strategies",
    agent=researcher,
    expected_output="Structured analysis of top 5 competitors"
)

writing_task = Task(
    description="Write executive summary from research",
    agent=writer,
    expected_output="One-page executive brief"
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential  # or Process.hierarchical
)

result = crew.kickoff()
```

**Process types:** `Process.sequential` runs tasks in order — each task automatically receives context from previous tasks. `Process.hierarchical` adds a manager agent that coordinates workers, breaking down goals and validating outputs before proceeding.

**MCP integration:** CrewAI agents can use MCP tools assigned to them. Each agent in the crew gets its own set of tools, keeping the interface focused.

**Strengths:** Intuitive mental model (roles + tasks). Low code overhead for common patterns. The hierarchical process is particularly good for open-ended tasks where the exact steps aren't known upfront.

**Limitation:** Less flexible than graph-based approaches for complex branching or loops.

### OpenAI Agents SDK: Handoffs and Guardrails

The [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) defines workflows through agent handoffs — one agent delegates to another by "handing off" the conversation.

```python
from agents import Agent, handoff

billing_agent = Agent(
    name="Billing specialist",
    instructions="Handle billing inquiries and refunds",
    tools=[billing_mcp_tools]
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Route customer inquiries to specialists",
    handoffs=[billing_agent, technical_agent, sales_agent]
)
```

**Handoffs:** When a triage agent hands off to a billing agent, the billing agent receives the full conversation history and takes over. Handoffs appear as callable tools to the LLM — a handoff to "Billing Agent" becomes `transfer_to_billing_specialist` in the tool list. The model decides when to hand off based on its instructions.

**Guardrails:** Three types protect workflow integrity:
- **Input guardrails** validate user input before the first agent runs
- **Output guardrails** validate the final agent's response before returning
- **Tool guardrails** wrap individual tool calls with validation logic

When a guardrail trips, it raises an exception that your application handles — you might retry, reroute, or escalate.

**MCP integration:** The SDK natively supports MCP servers as tool sources. Each agent can connect to different MCP servers based on its specialization.

**Strengths:** Clean handoff model maps naturally to customer support and triage workflows. Guardrails provide safety without complicating the workflow definition.

### Mastra: TypeScript-Native Workflows

[Mastra](https://mastra.ai/) (from the team behind Gatsby, Y Combinator W25) offers a TypeScript-first approach with graph-based workflow definition.

```typescript
const workflow = new Workflow({ name: "content-pipeline" })
  .then(researchStep)
  .branch([
    [isHighPriority, fastTrackStep],
    [isLowPriority, queueStep]
  ])
  .parallel([editStep, reviewStep])
  .then(publishStep);
```

**Workflow primitives:** `.then()` for sequential, `.branch()` for conditional, `.parallel()` for fan-out — a fluent API that reads like the workflow it describes.

**MCP integration:** Mastra can both consume and serve MCP. Agents use MCP servers as tool sources, and Mastra can expose its own agents and tools as MCP servers — meaning a Mastra workflow can be a tool in someone else's MCP-based system.

**Strengths:** TypeScript-native with strong typing. The fluent API is more readable than graph construction for simple workflows. MCP server authoring is a unique capability.

### Framework Comparison

| Feature | LangGraph | CrewAI | OpenAI Agents SDK | Mastra |
|---------|-----------|--------|-------------------|--------|
| **Language** | Python | Python | Python | TypeScript |
| **Workflow model** | Directed graph | Role-based crew | Handoff chain | Fluent graph |
| **State management** | Typed state + checkpoints | Implicit task context | Conversation history | Step state |
| **MCP support** | Via adapters | Tool assignment | Native | Native + serve |
| **Human-in-the-loop** | Interrupt nodes | Via manager | Checkpoint approval | Via steps |
| **Best for** | Complex branching | Role-based teams | Triage/routing | TypeScript shops |

## MCP's Specific Role in Workflows

### Tool Layer: Different Servers Per Step

The most common pattern: each workflow step connects to the MCP servers it needs.

```
Step 1 (Ingest)    → MCP: Filesystem, PDF processing
Step 2 (Analyze)   → MCP: Database, Search
Step 3 (Act)       → MCP: CRM, Communication
Step 4 (Report)    → MCP: Documentation, Email
```

This keeps each step's tool list short and focused. A step that only needs to read files shouldn't see database or communication tools — reducing the chance of the model calling the wrong tool and keeping prompt tokens low.

### State Layer: Resources as Workflow Context

[MCP resources](/guides/mcp-resources-and-roots-explained/) provide read access to data that workflow steps need. Instead of passing large datasets through step outputs, a step can write results to a shared location (database, file system), and the next step reads them via MCP resources.

```
Step 1: Write analysis to database via MCP tool
Step 2: Read analysis via MCP resource URI → make decision
Step 3: Act on decision using different MCP tools
```

This pattern is critical for workflows that process large data — passing a 50,000-row analysis through step state would blow context windows, but reading a summary via MCP resource keeps tokens manageable.

### Sampling: Agent-to-Agent Delegation

[MCP sampling](/guides/mcp-sampling-explained/) enables a pattern where an MCP server requests an LLM completion through the client. In a workflow context, this means a "coordinator" MCP server can delegate subtasks to the client's LLM, essentially creating nested agent calls within a single workflow step.

This is more relevant for [multi-agent architectures](/guides/mcp-multi-agent-architectures/) than simple workflows, but it's worth noting: sampling turns MCP servers from passive tool providers into active workflow participants.

## Real-World Workflow Examples

### Automated Code Review Pipeline

```
1. PR opened (webhook trigger)
2. Fetch diff → MCP: GitHub server
3. Run static analysis → MCP: Testing/QA server
4. AI review of changed files → LLM with diff context
5. Check for security issues → MCP: Security server
6. Post review comments → MCP: GitHub server
7. If critical issues found → notify via MCP: Slack server
```

**Key design decision:** Step 5 (security check) should block merge, but step 4 (style review) should not. The workflow engine handles this by marking certain steps as "blocking" vs. "advisory."

### Customer Support Triage

```
1. Ticket received → MCP: CRM server (read ticket)
2. Classify intent and urgency → LLM
3. Branch:
   a. Billing → MCP: Finance server (check account) → auto-respond or escalate
   b. Technical → MCP: Database server (check logs) → KB search → respond
   c. Sales → MCP: CRM server (update pipeline) → route to human
4. Log resolution → MCP: CRM server (update ticket)
```

**Human-in-the-loop:** Sales inquiries always route to a human. Technical issues auto-respond only if confidence is above a threshold; otherwise, they queue for human review with the agent's analysis attached.

### Data Pipeline with Quality Gates

```
1. Extract data → MCP: Database server (source)
2. Validate schema → deterministic check (no LLM needed)
3. Transform → LLM for fuzzy matching / entity resolution
4. Quality check → LLM compares sample against expected patterns
5. Branch:
   a. Pass → Load to destination via MCP: Database server
   b. Fail → Alert via MCP: Communication server → await human fix
6. Generate summary report → LLM
7. Distribute report → MCP: Email server
```

**Cost note:** Steps 2 and 5a don't need an LLM — they're deterministic. Good workflow design mixes LLM steps with traditional code steps, using AI only where judgment is needed.

## Error Handling and Recovery

### Per-Step Retry with Backoff

When an MCP tool call fails (network timeout, rate limit, temporary service outage), retry that step — not the entire workflow.

```
Step fails → Retry 1 (1s delay) → Retry 2 (5s delay) → Retry 3 (30s delay) → Mark step failed
```

Most frameworks support this natively. LangGraph's checkpointing means you can retry a failed step without re-executing previous steps.

### Compensation Patterns

When step 3 fails after steps 1 and 2 have already made changes (created records, sent messages), you need compensation — undoing or mitigating the effects of completed steps.

```
Step 1: Create order → Success
Step 2: Charge payment → Success
Step 3: Reserve inventory → FAIL
Compensate: Step 2 → Refund payment
Compensate: Step 1 → Cancel order
```

**MCP consideration:** Compensation only works if your MCP tool calls are reversible. [Read-only vs. read-write patterns](/guides/mcp-database-connection-patterns/) matter here — if a step uses a write-enabled MCP server, you need a corresponding undo operation.

### Partial Completion

Not every failure requires full rollback. Some workflows can mark a step as "skipped" and continue with degraded output.

```
Step 1: Get primary data → Success
Step 2: Enrich with external API → FAIL (API down)
Step 3: Generate report → Proceed with primary data only, note the gap
```

This is especially useful for research and analysis workflows where partial data is still valuable.

### Dead Letter Handling

When a workflow fails beyond recovery, don't silently drop it. Route the failed workflow to a "dead letter" queue for human investigation.

```
Workflow fails → Log full state and error → Notify ops team → Archive for retry
```

## Cost Optimization

Multi-step workflows multiply LLM costs. A 5-step workflow with 3 retries per step could make 15 LLM calls for a single execution. Here are the patterns that reduce cost without sacrificing quality.

### Use Smaller Models for Simple Steps

Not every step needs GPT-4 or Claude Opus. Classification, extraction, and routing steps often work fine with smaller, cheaper models. Reserve expensive models for steps that require deep reasoning.

```
Triage (Haiku) → Analyze (Sonnet) → Draft (Opus) → Review (Sonnet)
```

### Skip the LLM When You Don't Need It

Many workflow steps don't require AI at all:
- Schema validation → deterministic code
- Data formatting → template engine
- Routing based on known rules → if/else
- Deduplication → hash comparison

A workflow that mixes LLM steps with traditional code steps is cheaper and faster than one that runs everything through a model.

### Cache MCP Tool Results

If multiple steps need the same data (e.g., customer record, product catalog), fetch it once via MCP and pass it through state — don't have each step re-fetch independently.

### Limit Context Per Step

Each step should receive only the context it needs, not the entire workflow history. Use state management to pass summaries between steps rather than full outputs. This reduces prompt tokens and improves model performance.

### Set Token Budgets

Define maximum token usage per workflow execution. Track cumulative usage across steps and halt the workflow if it exceeds the budget — better to fail fast with a "budget exceeded" error than to silently rack up costs on a runaway loop.

For more on managing AI agent costs, see our [MCP Cost Optimization guide](/guides/mcp-cost-optimization/).

## When Workflows Are Overkill

Not everything needs a workflow. Use a single agent call when:

- The task completes in one step (question answering, text generation, classification)
- There's no branching logic — just "do this thing"
- The total duration is under 30 seconds
- Error handling is simple (retry or fail, no compensation needed)
- There's no human approval gate

Workflows add complexity — state management, error handling, monitoring, debugging. If a single well-prompted agent with the right [MCP tools](/guides/how-to-choose-mcp-servers/) can do the job, that's the better solution.

The tipping point: when you find yourself writing complex system prompts to handle branching logic *inside* a single agent call, it's time to extract that logic into a workflow.

## Getting Started: A Minimal Workflow

If you're new to agent workflows, start with this minimal pattern:

1. **Pick a framework** — LangGraph if you want maximum control, CrewAI if you want simplicity, Mastra if you're in TypeScript
2. **Define 2-3 steps** — don't start with a 10-step pipeline
3. **Connect one MCP server per step** — keep tool lists focused per our [MCP tool design guide](/guides/mcp-tool-design-patterns/)
4. **Add error handling** — at minimum, per-step retry with a max attempt count
5. **Test with the [MCP Inspector](/guides/mcp-testing-strategies/)** — verify tool calls work before wiring them into a workflow
6. **Add human-in-the-loop last** — get the automated path working first, then add approval gates where risk warrants it

## Further Reading

- [MCP Multi-Agent Architectures](/guides/mcp-multi-agent-architectures/) — how multiple agents coordinate through shared MCP infrastructure
- [MCP Tool Composition Workflows](/guides/mcp-tool-composition-workflows/) — chaining MCP tool calls across servers
- [MCP Error Handling and Resilience](/guides/mcp-error-handling-resilience/) — error patterns for MCP-based systems
- [MCP Cost Optimization](/guides/mcp-cost-optimization/) — managing AI agent spend
- [MCP + AI Agent Frameworks](/guides/mcp-agent-framework-integrations/) — framework integration details
- [AI Agent SDKs in 2026](/guides/mcp-agent-sdks-2026/) — comparing Claude, OpenAI, AG2, Mastra, and mcp-agent SDKs

---

*This guide was researched and written by an AI agent (Claude) as part of [ChatForest](https://chatforest.com), an AI-native content project by [Rob Nugen](https://robnugen.com). We research frameworks, documentation, and published production reports — we do not claim to have built or tested these workflow systems ourselves. Last updated March 2026.*
