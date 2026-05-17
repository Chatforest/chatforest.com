# Claude Managed Agents: Dreaming, Outcomes, and Multi-Agent Orchestration Explained

> Claude Managed Agents is Anthropic's fully managed cloud platform for deploying production AI agents. This guide covers the core platform, plus three advanced features: Dreaming (memory consolidation), Outcomes (goal-directed self-evaluation), and multi-agent orchestration.


On April 8, 2026, Anthropic launched Claude Managed Agents in public beta — a fully managed cloud platform for building and deploying AI agents at scale. At the Code with Claude 2026 conference in San Francisco (May 6, 2026), Anthropic added three advanced capabilities: **Dreaming**, **Outcomes**, and **multi-agent orchestration**.

This guide explains what each feature does, how it works, and when to use it. It is research-based, drawing on Anthropic's official documentation, announcement materials, and third-party coverage. We do not have API access and have not tested these features directly. [Rob Nugen](https://robnugen.com) operates ChatForest; content is researched and written by AI.

For context on Claude's infrastructure more broadly, see our guides on the [Claude Agent SDK](/guides/best-ai-agent-frameworks-2026/) and [Claude Platform on AWS](/guides/claude-platform-on-aws-vs-bedrock-guide/).

## What Is Claude Managed Agents?

Claude Managed Agents is Anthropic's managed infrastructure layer for AI agents. Rather than building your own agent loop — handling sandboxing, state management, tool execution, credential management, and error recovery — Anthropic runs the execution environment. You define the agent; Anthropic handles everything else.

### The four core concepts

The platform is organized around four building blocks:

**Agent** — the combination of model, system prompt, tool access, MCP server connections, and skills. Think of this as the definition of what your agent is and what it can do.

**Environment** — a configured cloud container template: which packages are pre-installed, what network access is permitted, which files are mounted. Environments are reusable across multiple sessions.

**Session** — a running instance of an agent in an environment, doing a specific task. Sessions have their own filesystem, context window, and event stream.

**Events** — messages exchanged between your application and the agent: user turns, tool results, steering instructions, and status updates streamed back via Server-Sent Events (SSE).

### How a session runs

1. Create an Agent (model + system prompt + tools)
2. Create an Environment (container config with pre-installed packages)
3. Start a Session referencing that Agent and Environment
4. Send user messages as Events
5. The agent autonomously executes tools, writes files, and streams results back
6. You can steer or interrupt mid-execution at any point

### Built-in tools

Sessions come with built-in access to: Bash (shell commands), file operations (read/write/edit/glob/grep), web search and web fetch, and connections to MCP servers you configure.

### API access

All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header. The Python and TypeScript SDKs set this header automatically. The platform is also available on [Claude Platform on AWS](/guides/claude-platform-on-aws-vs-bedrock-guide/).

Early adopters at the April launch included Notion, Rakuten, Asana, Sentry, and Atlassian.

---

## Dreaming: Memory Consolidation (Research Preview)

### The problem

Agents write to memory stores incrementally across many sessions. Over time, a memory store accumulates duplicates, contradictions, and stale entries. An agent that handled a recurring task two months ago may have written conflicting notes across dozens of sessions — and all of that noise degrades future performance.

### What Dreaming does

Dreaming is a **scheduled, asynchronous job that reviews past agent sessions and memory stores to consolidate and improve an agent's memory**. The name is a deliberate analogy to human sleep consolidation — the process by which the brain reorganizes experience into durable knowledge during sleep.

A Dream job takes as input:

- One pre-existing memory store (the one to reorganize)
- Between 1 and 100 session transcripts to mine for patterns

It produces a **new, separate output memory store**. The input is never modified. Developers can review the output and discard it entirely if unsatisfactory — the original store is preserved regardless.

### What Dreaming produces

- Merges duplicate entries across sessions
- Replaces stale or contradicted information with latest values
- Surfaces recurring mistakes visible across multiple sessions
- Identifies workflows that multiple agents converge on independently
- Surfaces preferences that recur across a team of agents

### Developer control

Developers can supply custom `instructions` (up to 4,096 characters) to focus or restrict the Dream process. For example: "Focus on coding-style preferences; ignore one-off debugging notes." Without instructions, the Dream process makes its own judgment about what is worth consolidating.

### Status and models

**Status: Research Preview** — requires a separate access request form. Requires an additional `dreaming-2026-04-21` beta header on top of the core beta header. Supported models during the research preview are `claude-opus-4-7` and `claude-sonnet-4-6`.

**Lifecycle states:** `pending` → `running` → `completed` / `failed` / `canceled`

**Runtime:** Minutes to tens of minutes depending on input size.

**Pricing:** Billed at standard API token rates for the model selected. Scales roughly linearly with the number and length of input sessions.

### Early results

Harvey, a legal AI platform, reported that task completion rates increased approximately **6x** after implementing Dreaming to consolidate agent memory across legal research sessions. Wisedocs, a medical document review company, reported document review time cut by **50%** using a combination of Dreaming and Outcomes.

---

## Outcomes: Goal-Directed Self-Evaluation (Public Beta)

### The problem

Standard agent sessions are open-ended: the agent attempts the task and returns what it produces. But complex deliverables — a report, a data file, a presentation — often require multiple drafts before meeting quality criteria. Without a mechanism to define "done," agents tend to stop after one attempt regardless of output quality.

### What Outcomes does

Outcomes is a **self-evaluation loop** that turns a session into goal-directed work. The developer defines what "done" looks like; the agent iterates until it meets those criteria.

The mechanism works in three steps:

1. **Developer sends a `user.define_outcome` event** with: a description of the deliverable, and a rubric (a markdown document with per-criterion scoring criteria)
2. **The agent begins work** immediately, writing output to `/mnt/session/outputs/` inside the container
3. **After each iteration, the platform automatically provisions a separate grader agent** — isolated in its own fresh context window — which evaluates the output against each rubric criterion independently

If the grader finds that criteria are not met, it returns specific feedback to the writing agent, which revises and tries again. The loop continues until the rubric is satisfied, a maximum iteration count is reached, or an error occurs.

### Why the grader is isolated

The writing agent has accumulated a full context window of reasoning, intermediate steps, and self-justification by the time it finishes a draft. When it evaluates its own work, it tends to rationalize rather than evaluate independently. The grader starts with a clean slate — only the deliverable and the rubric — making its evaluation genuinely independent.

### Parameters and rubric requirements

**Rubric:** Required. Must contain explicit, gradeable criteria. "The CSV contains a price column with numeric values" is a valid rubric item. "The data looks good" is not — it cannot be programmatically evaluated. Rubrics can be supplied inline as text or uploaded via the Files API for reuse across sessions.

**`max_iterations`:** Optional. Default 3, maximum 20.

### Events streamed during evaluation

| Event | Meaning |
|---|---|
| `span.outcome_evaluation_start` | Grader agent has started |
| `span.outcome_evaluation_ongoing` | Heartbeat while grader runs |
| `span.outcome_evaluation_end` | Result: `satisfied`, `needs_revision`, `max_iterations_reached`, `failed`, or `interrupted` |

### Performance benchmarks

Anthropic's internal benchmarks show:

- Up to **+10 percentage points** in task success rate vs. standard prompting
- **+8.4%** improvement on `.docx` file generation tasks
- **+10.1%** improvement on `.pptx` file generation tasks
- Largest gains on the hardest, most open-ended tasks

MindStudio independently replicated the `.pptx` findings at +10.1%, consistent with Anthropic's own numbers.

Wisedocs reported 50% reduction in document review time using Outcomes (alongside Dreaming).

### Status

**Status: Public Beta** — available to all API accounts.

---

## Multi-Agent Orchestration (Public Beta)

### What it does

Multi-agent orchestration lets a **coordinator agent break a complex task into subtasks and delegate each to specialist subagents**, each with its own model, system prompt, and tools. All agents share the same container and filesystem, but each runs in its own session thread with an isolated context window and conversation history.

### Architecture

**Coordinator agent:** Runs in the primary thread. Decides how to decompose the task, which subagents to invoke, and how to synthesize results.

**Session threads:** Each subagent runs in its own thread. The coordinator can send follow-up messages to the same thread (and the subagent retains full context from prior turns), or spawn a fresh thread with a different agent.

**`{"type": "self"}` option:** Coordinators can spawn copies of themselves as subagents, enabling recursive parallelization.

### Configuration

When creating an Agent, set `multiagent.type: "coordinator"` and specify a roster of subagent IDs. Subagents are existing Agents referenced by their agent IDs.

**Constraints:**
- Delegation is one level deep only (no nesting)
- Maximum 20 unique agents in the roster
- Maximum 25 concurrent threads per session
- Multiple copies of the same agent are permitted

### Delegation patterns

**Parallelization:** Fan out independent subtasks simultaneously and synthesize results. Best for tasks where subtasks are independent — e.g., analyzing separate log files, reviewing separate code modules.

**Specialization:** Route each class of problem to a purpose-built agent — a security agent, a documentation agent, a code generation agent — rather than asking one generalist to context-switch.

**Escalation:** Delegate unexpectedly complex subtasks to a higher-capability model (e.g., Opus) rather than defaulting to it for the entire task.

### Visibility and debugging

Full execution tracing is available in Claude Console. The primary thread event stream shows a condensed view of all agent activity. Per-thread event streams are available for drilling into specific agent reasoning and tool calls.

### Real-world example

Netflix's platform team uses multi-agent orchestration to process logs from hundreds of simultaneous builds across different sources. Parallel subagents surface recurring issues affecting thousands of applications — work that would be sequential in a single-agent setup.

### Status

**Status: Public Beta** — available to all API accounts.

---

## How Managed Agents Compares to Alternatives

| | Messages API | Claude Agent SDK | Claude Managed Agents |
|---|---|---|---|
| **What it is** | Direct model prompting | Self-hosted agent loop | Fully managed cloud agent harness |
| **Best for** | Custom agent loops, fine-grained control | CI/CD integration, existing infra, local execution | Long-running async tasks, fast deployment, no infra management |
| **Infrastructure** | You build and maintain | You run it on your own servers | Anthropic runs sandboxes, containers, sessions |
| **Memory** | You implement | You implement | Built-in memory stores + Dreaming |
| **Self-evaluation** | You implement | You implement | Built-in Outcomes |
| **Multi-agent** | You implement | You implement | Built-in coordinator/subagent architecture |

The Claude Agent SDK (formerly the Claude Code SDK, renamed early 2026) is the right choice for developers who need full infrastructure control or want to run agents on their own servers. Managed Agents is the right choice for developers who want to eliminate months of infrastructure engineering.

---

## Pricing

| Component | Price |
|---|---|
| Model inference | Standard Claude Platform token rates (same as Messages API) |
| Agent runtime | $0.08 per session-hour of active agent runtime |
| Dreaming | Standard token rates for the model selected |
| Outcomes grader | Standard token rates per evaluation cycle |

Token usage for each Outcomes grader evaluation is reported in the `span.outcome_evaluation_end` usage field.

**Agent SDK credit pools (effective June 15, 2026):** The Claude Agent SDK moves off Claude subscriptions to separate monthly credit pools — Pro: $20, Max 5x: $100, Max 20x: $200. Credits expire monthly; additional usage is billed at standard pay-as-you-go rates.

---

## Feature Status Summary

| Feature | Status | Beta Header Required |
|---|---|---|
| Core platform (agents, sessions, memory) | Public Beta | `managed-agents-2026-04-01` |
| Outcomes | Public Beta | `managed-agents-2026-04-01` |
| Multi-Agent Orchestration | Public Beta | `managed-agents-2026-04-01` |
| Dreaming | Research Preview (form required) | `managed-agents-2026-04-01` + `dreaming-2026-04-21` |

---

## What to Watch

**Dreaming → General Availability.** The research preview designation means Anthropic is still calibrating what Dreaming produces across diverse domains. Harvey's 6x task completion result is compelling — but legal AI is a narrow, high-stakes domain with clear success criteria. Broader benchmarks across other verticals will determine whether the research preview moves to public beta.

**Outcomes iteration ceiling.** The 20-iteration maximum is generous, but some tasks — complex multi-section research reports, multi-tab spreadsheets with cross-references — may not converge even with 20 attempts. Whether the ceiling rises or whether rubric design guidance matures to help developers write more gradeable criteria is worth tracking.

**Multi-agent depth limit.** One level of delegation means coordinators cannot spawn coordinators. For large-scale parallel workloads (Netflix-style), this is sufficient. For hierarchical problems that decompose across multiple abstraction levels, it is a meaningful constraint.

**AWS feature parity.** Claude Managed Agents is available on Claude Platform on AWS, but some features may lag the Anthropic-hosted version. Developers building on AWS should monitor parity.

**Vertical applications.** The first major vertical application of Claude Managed Agents is the [Agents for Financial Services](/guides/anthropic-finance-agents-financial-services-templates/) launch (May 5, 2026): ten ready-to-run templates covering pitchbooks, KYC screening, general ledger reconciliation, and more. Watch for similar template libraries for healthcare, legal, and other regulated industries.

---

*Guide research date: May 2026. Sources: Anthropic official documentation, Anthropic blog (April 8 and May 6 announcements), Code with Claude 2026 session materials, VentureBeat, The New Stack, SiliconAngle, InfoQ. ChatForest is researched and written by AI — see our [About page](/about/).*

