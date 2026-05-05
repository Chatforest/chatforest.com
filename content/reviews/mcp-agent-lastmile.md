---
title: "mcp-agent — The MCP-First Python Agent Framework That Implements Every Anthropic Agent Pattern"
date: 2026-05-05T26:00:00+09:00
description: "mcp-agent reviewed: an Apache-2.0 Python framework from lastmile-ai that implements all Anthropic 'Building Effective Agents' patterns using MCP as its foundation. 8.1K stars. Rating: 4.0/5."
og_description: "mcp-agent (8.1K stars, Apache-2.0, Python): the MCP-first agent framework from lastmile-ai. Implements every Anthropic 'Building Effective Agents' pattern — basic, parallel fan-out, routing, orchestrator-workers, evaluator-optimizer — as composable AugmentedLLM objects. Supports Anthropic, OpenAI, Gemini, AWS Bedrock, Azure, Ollama. Optional Temporal integration for durable pause/resume/retry workflows without code changes. v0.2.6, pre-1.0 but actively developed. Rating: 4.0/5."
content_type: "Review"
card_description: "mcp-agent (8.1K stars, v0.2.6, Apache-2.0, Python) is a Python agent framework built on MCP from day one — not a server, but the thing that orchestrates agents that talk to servers. Its vision: MCP is all you need to build agents. The core abstraction is AugmentedLLM: an LLM with a collection of MCP servers attached. Every workflow pattern (orchestrator, evaluator, router) is itself an AugmentedLLM, so patterns compose and chain naturally. The library implements all six patterns from Anthropic's 'Building Effective Agents' paper: basic augmented LLM, parallel fan-out/fan-in, routing/bucketing, orchestrator-workers, evaluator-optimizer, and multi-agent handoffs (OpenAI Swarm-compatible). Switch any workflow to durable execution by setting execution_engine=temporal — no agent code changes, just pause/resume/retry/human-input guaranteed by Temporal's workflow engine. Supports Anthropic (Claude), OpenAI, Google Gemini, AWS Bedrock, Azure OpenAI, and Ollama (via OpenAI compat). Full MCP capability coverage: Tools, Resources, Prompts, Notifications, OAuth, Sampling, Elicitation, Roots. Install with pip install mcp-agent or scaffold via uvx mcp-agent init. Companion tools: mcp-eval (evaluation framework) and openai-agents-mcp (OpenAI Agents SDK extension). Pre-1.0 with some rough edges — Orchestrator/AugmentedLLM composition issues, max tool response size not configurable, OpenRouter partial support. Part of our **Developer Tools** category. Rating: 4.0/5."
last_refreshed: 2026-05-05
categories: ["/categories/developer-tools/"]
---

Most of this site reviews MCP servers — the tools that expose capabilities to AI agents. mcp-agent sits one level above: it is the framework that orchestrates those agents, connecting them to MCP servers and implementing the patterns that make agents actually useful in production.

At **8,100 stars** with an Apache-2.0 license and a thesis that "MCP is all you need to build agents," mcp-agent from [lastmile-ai](https://github.com/lastmile-ai) is one of the most architecturally coherent entries in the agent framework space. It was built for MCP from day one — not retrofitted. Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) |
| **Stars** | ~8,100 |
| **Forks** | 817 |
| **License** | Apache-2.0 |
| **Language** | Python |
| **Version** | v0.2.6 (PyPI) |
| **Last updated** | January 25, 2026 |
| **Author** | lastmile-ai |
| **Install** | `pip install mcp-agent` or `uvx mcp-agent` |
| **Docs** | docs.mcp-agent.com |

---

## What It Does

Where mcp-use (reviewed previously) is a client library focused on connecting an LLM to MCP servers in the fewest lines of code, mcp-agent is a framework for building production-grade multi-step agents that use MCP as their tool layer. The distinction matters: mcp-agent handles orchestration, composition, durability, and workflow patterns — not just a single agent loop.

The foundational abstraction is **AugmentedLLM**: an LLM attached to a set of MCP servers. An AugmentedLLM knows what tools are available from each connected server, routes tool calls appropriately, and manages the conversation loop. Every workflow pattern in the framework is itself an AugmentedLLM, which means patterns are composable by design — you can nest an evaluator inside an orchestrator, or chain a router into a parallel fan-out, without wiring anything together manually.

---

## The Six Agent Patterns

mcp-agent implements every pattern from Anthropic's [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) paper:

**Basic Augmented LLM** — Single agent with access to MCP tools. The entry point; one LLM, one or more MCP servers, a task to complete.

**Parallel Fan-Out / Fan-In** — Multiple specialized agents run concurrently on sub-problems; results are aggregated by a synthesizer. Useful for research tasks, code review across modules, or any problem that parallelizes naturally.

**Routing / Bucketing** — An LLM classifier reads incoming requests and routes them to the most appropriate agent or MCP server. Handles intent classification and workload distribution without hard-coded conditionals.

**Orchestrator-Workers** — A planner agent decomposes a goal into sub-tasks and delegates each to a worker agent. The orchestrator coordinates; workers execute. Suitable for long-horizon tasks where the steps cannot be enumerated upfront.

**Evaluator-Optimizer** — An agent generates output; a separate evaluator agent scores or critiques it; the generator iterates until the evaluator approves. Implements quality control loops that would otherwise require manual checkpointing.

**Multi-Agent Handoffs** — Agents transfer control between each other using a protocol compatible with OpenAI Swarm. Enables hand-off-style workflows where different specialists own different phases of a task.

All six patterns use the same AugmentedLLM interface, so switching from a basic agent to an orchestrator-workers setup is a matter of wrapping, not rewriting.

---

## Durable Execution with Temporal

The framework's most distinctive feature is optional **Temporal integration**. Add `execution_engine: temporal` to your workflow config and your agent gains:

- **Pause and resume** — workflows survive process restarts and infrastructure interruptions
- **Automatic retries** — transient failures are retried without custom error-handling code
- **Human-in-the-loop** — workflows can pause and surface a tool call that waits for external input before continuing
- **Durable history** — every step is logged in Temporal's event history, giving full replay capability

The key design choice: switching to Temporal requires no changes to agent or workflow code. The same patterns that run in-process locally run durably in Temporal without modification. This makes it practical to build an agent that works in development and then deploy it with production-grade durability.

The trade-off is operational overhead: Temporal requires running a Temporal server (self-hosted or Temporal Cloud), which is a non-trivial dependency for teams who just want a simple agent.

---

## LLM Support

mcp-agent provides AugmentedLLM implementations for:

- **Anthropic** — Claude 3.5+
- **OpenAI** — GPT-4o, o4, and reasoning models
- **Google Gemini**
- **AWS Bedrock** (Anthropic via Bedrock)
- **Azure OpenAI**
- **Ollama** — via OpenAI compatibility endpoint (community-supported)
- **OpenRouter** — partial support; some models report tool-use endpoint errors

The LLM provider is a configuration choice, not a code change. Every workflow pattern works with any supported provider.

---

## MCP Capability Coverage

Unlike some frameworks that support MCP Tools only, mcp-agent handles the full MCP specification:

- **Tools** — function-call interface
- **Resources** — file and data access
- **Prompts** — reusable prompt templates
- **Notifications** — server-push events
- **OAuth** — authenticated server connections
- **Sampling** — server-initiated LLM calls
- **Elicitation** — structured human input requests
- **Roots** — filesystem scope declarations

This completeness matters if you are connecting to MCP servers that use Resources or Prompts rather than just Tools.

---

## Installation and CLI

```bash
pip install mcp-agent
# or
uvx mcp-agent init    # scaffold a new project
uvx mcp-agent deploy my-agent  # deploy
```

The `uvx` path is zero-install: no virtual environment setup, just run and it fetches the right version. The `init` command scaffolds a project with example configs for different workflow patterns.

### Companion Tools

**[mcp-eval](https://github.com/lastmile-ai/mcp-eval)** — A lightweight evaluation framework for MCP servers built on mcp-agent. Useful for testing server behavior and agent quality against defined benchmarks.

**[openai-agents-mcp](https://github.com/lastmile-ai/openai-agents-mcp)** — An extension package for OpenAI's Agents SDK that adds MCP support, for teams already invested in the OpenAI ecosystem.

---

## Known Limitations

**Pre-1.0 stability** — v0.2.6 means the API surface is still evolving. Breaking changes between minor versions are possible.

**Max tool response size** — There is no built-in way to limit how large a tool response can be before it is sent to the LLM context. Servers that return very large responses (e.g., 500K tokens) can cause LLM API errors. Workarounds exist in user code, but configurable limits are not yet built in.

**Orchestrator + AugmentedLLM composition** — A known issue: when an AugmentedLLM is passed as a worker to an Orchestrator, the Orchestrator fails to enumerate server names because AugmentedLLMs do not expose that attribute. The workaround is to use base Agent objects rather than composed AugmentedLLMs as Orchestrator workers.

**OpenRouter partial support** — Some OpenRouter model endpoints report errors about not supporting tool use when accessed through mcp-agent's OpenAI-compatible path.

**Temporal overhead** — The durable execution story requires running Temporal infrastructure. For simple use cases, this is significantly more than needed.

---

## How It Compares

| Framework | MCP-first | Temporal | Patterns | LLM-agnostic |
|---|---|---|---|---|
| **mcp-agent** | Yes (built for MCP) | Yes | 6 patterns | Yes |
| mcp-use | Yes | No | Basic ReAct | Yes (LangChain) |
| LangGraph | No (added later) | No | Graph-based | Yes |
| CrewAI | No | No | Role-based | Yes |
| OpenAI Agents SDK | No | No | Handoffs | OpenAI only |

The key differentiator: mcp-agent treats MCP as the architecture, not an integration. All orchestration flows through MCP tool calls. This makes it significantly more compatible with the growing MCP server ecosystem than frameworks that added MCP as an afterthought.

---

## Who Should Use This

**Best fit:**
- Developers building multi-step agents in Python who want structured workflow patterns without designing everything from scratch
- Teams who need Temporal-backed durable execution for production agent workflows
- Anyone building on the Anthropic "Building Effective Agents" patterns and wanting a reference implementation

**Not the right fit:**
- Developers who need a single-agent LLM-to-MCP connection with minimal overhead (consider mcp-use instead)
- Teams who need a stable, versioned API before they can adopt (wait for 1.0)
- Projects that cannot take on a Temporal dependency for production durability

---

## Rating: 4.0 / 5

mcp-agent delivers real architectural value: MCP-native from day one, six composable agent patterns, multi-provider LLM support, and an optional Temporal path that is genuinely novel. The "MCP is all you need" thesis holds up — the framework demonstrates that complex multi-agent coordination is achievable with clean, composable primitives and no graph DSL.

The deductions are for pre-1.0 stability: the Orchestrator/AugmentedLLM composition bug, the missing max tool response size configuration, and OpenRouter rough edges are minor but real. The Temporal dependency is a feature for production teams and an obstacle for everyone else.

At 8,100 stars with Apache-2.0 licensing and active development, mcp-agent is the most complete MCP-first agent framework available today. If you are building Python agents that use MCP tools and need patterns beyond basic ReAct, it deserves serious consideration.
