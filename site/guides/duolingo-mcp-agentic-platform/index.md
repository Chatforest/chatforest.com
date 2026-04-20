# Duolingo's Agentic AI Platform: 180+ MCP Tools, No-Code Workflows, and an Enterprise Slackbot

> Duolingo built an enterprise AI Slackbot with 180+ MCP tools and a no-code agentic workflow platform on Temporal — enabling any employee to create AI coding agents in under 5 minutes. Here's the full architecture breakdown.


Duolingo isn't just a language-learning app anymore. Behind the scenes, its DevXAI team has built one of the most ambitious enterprise MCP deployments documented to date: an internal AI Slackbot connecting 180+ MCP tools, plus a no-code platform that lets any employee — not just engineers — create and deploy AI coding agents in under five minutes.

Aaron Wang, Software Engineer on Duolingo's DevXAI team, presented the Slackbot architecture as a [keynote at MCP Dev Summit North America 2026](https://mcpdevsummitna26.sched.com/) on April 2. Separately, Duolingo has published detailed engineering blog posts on their [agentic workflow platform](https://blog.duolingo.com/agentic-workflows/) and [feature flag removal agent](https://blog.duolingo.com/buildingaiagents/), and open-sourced a [Slack MCP server](https://github.com/duolingo/slack-mcp) for the community.

This guide synthesizes all four sources into a comprehensive case study. Our analysis draws on Duolingo's published blog posts, the MCP Dev Summit schedule, and the open-source repository — we research and analyze rather than testing implementations hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

For related context, see our guides on [Pinterest's MCP Production Case Study](/guides/pinterest-mcp-production-case-study/), [Datadog's MCP Server Design Lessons](/guides/datadog-mcp-server-production-lessons/), [MCP in Production](/guides/mcp-in-production/), and [MCP Dev Summit 2026](/guides/mcp-dev-summit-2026-guide/).

---

## The Two Systems

Duolingo's MCP story has two distinct but related pieces:

| System | Purpose | Scale |
|--------|---------|-------|
| **AI Slackbot** | Employee-facing assistant for Q&A, alert triage, incident debugging, system navigation | 180+ MCP tools |
| **Agentic Workflow Platform** | No-code system for creating AI coding agents that automate repetitive engineering tasks | <5 min to create simple agents |

Both systems reflect the same organizational bet: MCP as the standard integration layer between AI and internal tools.

---

## The AI Slackbot: 180+ MCP Tools

### What It Does

Duolingo's AI Slackbot is an enterprise assistant that helps employees across the company:

- **Find answers** in help channels — surfacing institutional knowledge from Slack history
- **Triage alerts** — routing and prioritizing operational notifications
- **Debug incidents** — pulling context from multiple systems to accelerate root cause analysis
- **Navigate internal systems** — acting as a unified interface to Duolingo's internal tooling

The 180+ MCP tools give the Slackbot read and action access to a wide range of internal systems. While Duolingo hasn't published the full tool list, the scope — help channels, alerting, debugging, internal systems — implies connections to monitoring, code repositories, documentation, ticketing, and communication platforms.

### Why 180+ Tools Is Notable

Most enterprise MCP deployments documented to date operate at far smaller scales:

| Company | MCP Tools | Context |
|---------|-----------|---------|
| **Duolingo** | 180+ | Internal Slackbot assistant |
| **Pinterest** | ~20 across multiple servers | Engineering automation |
| **Datadog** | ~16 core + 13 optional toolsets | External developer tool |

Duolingo's 180+ tool count is significant because it tests MCP at a scale where tool selection becomes a core challenge. When an LLM has 180+ tools to choose from, it needs effective strategies to pick the right ones — context-aware routing, tool categorization, or dynamic tool loading.

### The Open-Source Slack MCP Server

Duolingo open-sourced one piece of this infrastructure: [duolingo/slack-mcp](https://github.com/duolingo/slack-mcp), an OAuth-based multi-user Slack MCP server with HTTP transport.

**Capabilities:**

| Tool | Description |
|------|-------------|
| `slack_get_channel_messages` | Retrieve messages from channels |
| `slack_get_thread_replies` | Get conversation thread replies |
| `slack_search_messages` | Advanced message search with filters |
| `slack_get_users` | List workspace users or get specific profiles |
| `slack_get_channels` | List channels or get detailed info |

**Technical design choices:**

- **Read-only** — no write permissions, reducing blast radius
- **OAuth 2.1** — proper multi-user authentication (requires 11 Slack scopes)
- **HTTP transport** — production-ready, not STDIO-bound
- **Multi-user** — individual authentication tokens per user

The read-only design is intentional and aligns with a principle we've seen at Pinterest and other enterprise deployments: start with read access, add write access only where human-in-the-loop approval is in place.

---

## The Agentic Workflow Platform

### The Problem

Before the platform, creating an AI coding agent at Duolingo meant writing custom code. Each agent had its own integration logic, its own way of cloning repos, creating PRs, and handling LLM failures. This approach didn't scale — only engineers who understood the full stack could build agents, and each one took days of custom development.

### The Architecture

Duolingo's platform has three core components:

```
┌─────────────────────────────────────────────────┐
│           JSON Workflow Definitions              │
│   (no-code forms: prompt + repo + parameters)   │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│            CodingAgent Library                   │
│   (unified abstraction over Codex + Claude)      │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│          Temporal Orchestration                   │
│   (durability, retries, timeouts per activity)   │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│         MCP Servers + Shared Infrastructure      │
│   (GitHub MCP, Atlassian MCP planned, bot PRs)   │
└─────────────────────────────────────────────────┘
```

### Component 1: JSON Workflow Definitions

The no-code interface lets any employee define a workflow by filling out a JSON form:

- **Prompt** — what the agent should do
- **Target repository** — which codebase to modify
- **Parameters** — optional configuration (branch name, file patterns, etc.)

For workflows that follow common patterns (clone → modify → commit → PR), employees can create an agent in **under 5 minutes**. More complex multi-step workflows take **1–2 days**.

Workflows are merged into a central repository and automatically appear in internal tooling, accessible company-wide.

### Component 2: CodingAgent Library

The CodingAgent library abstracts multiple LLM providers behind a single interface:

- **OpenAI Codex** — via Codex CLI
- **Anthropic Claude** — via Claude Code SDK

Switching between providers requires only changing an enum parameter. This lets teams experiment with different models without rewriting agent code — a practical solution to the fast-moving model landscape.

### Component 3: Temporal Orchestration

[Temporal](https://temporal.io/) handles workflow orchestration, solving a critical problem for LLM-based workflows: **non-determinism**.

LLM calls can fail, time out, or produce unexpected results. Without orchestration, a failure midway through a multi-step workflow would restart the entire process. Temporal provides:

- **Per-activity retries** — each step has its own timeout and retry policy
- **Durability** — workflow state survives process restarts
- **Isolation** — a failed LLM call in step 3 doesn't restart steps 1 and 2

This is the same pattern we've seen in [Pinterest's MCP deployment](/guides/pinterest-mcp-production-case-study/), where Airflow MCP servers orchestrate multi-step workflows. The lesson: production MCP systems need workflow orchestration, whether through Temporal, Airflow, or similar tools.

### MCP Integration

MCP extends the platform's capabilities beyond code manipulation:

- **GitHub MCP** — already in production. Agents with GitHub MCP access can reference other codebases while modifying their own, significantly improving cross-repository problem-solving.
- **Atlassian MCP** — planned. Would connect agentic workflows to project management, documentation, and issue tracking beyond the codebase.

The MCP integration follows the standard pattern: MCP servers provide tool access, the CodingAgent library decides when to use them, and Temporal ensures reliable execution.

### Shared Infrastructure

The platform includes centralized infrastructure that individual agents don't need to build:

- **GitHub App token** — a single bot identity for creating PRs, with centralized permission control
- **Repository cloning utilities** — shared libraries for common git operations
- **Slack notifications** — status updates pushed to relevant channels
- **API key management** — environment variable-based credential handling

---

## The Feature Flag Removal Agent

Duolingo's most documented agent use case is automated feature flag removal — a task every engineering team dreads.

### Why Feature Flags Accumulate

Feature flags start as temporary toggles for safe rollouts. They accumulate because removing them requires:

1. Finding all code paths that reference the flag
2. Determining which branch is the "winner" (enabled vs. disabled)
3. Removing dead code paths
4. Updating tests
5. Creating and merging a PR

Each flag removal is straightforward but tedious. Engineers deprioritize it, and technical debt grows.

### How the Agent Works

Using the agentic workflow platform, Duolingo built an agent that handles the full lifecycle:

1. **Input:** Flag name and the winning branch
2. **Agent action:** Clones the repository, finds all references, removes the flag and dead code paths, updates tests
3. **Output:** A pull request ready for human review

The agent uses Codex CLI (or Claude Code SDK) for the code reasoning and modification, with Temporal managing the workflow durability.

### What's Notable

This isn't a demo — it's a production system handling a real engineering maintenance task. The agent creates PRs that go through standard code review, maintaining human oversight. The pattern — **AI generates, humans approve** — is consistent across all of Duolingo's agentic tools.

Other documented agent use cases include:

- **Experiment launch/shutdown** — automating A/B test lifecycle management
- **Terraform infrastructure changes** — modifying infrastructure-as-code with automated PR creation

---

## Architecture Lessons

### Lesson 1: Abstraction Over LLM Providers

Duolingo's CodingAgent library solves a problem that will only grow: model lock-in. By abstracting Codex and Claude behind a single interface, they can:

- Switch models per-workflow based on task fit
- Benchmark new models against existing workflows
- Avoid rewriting agents when providers change APIs

This pattern — a unified agent abstraction layer — is worth watching as the model landscape continues to fragment.

### Lesson 2: Temporal for LLM Workflows

The choice of Temporal for orchestration is architecturally significant. Most MCP demos show single-shot tool calls. Production systems need:

- Multi-step workflows with intermediate state
- Retry logic that doesn't restart from scratch
- Timeouts that prevent runaway LLM calls from consuming resources
- Audit trails for compliance

Temporal provides all of these. The broader lesson: **production MCP deployments need a workflow orchestration layer**, not just a tool-calling layer.

### Lesson 3: No-Code ≠ No Engineering

Duolingo's "no-code" claim has a specific scope. The 5-minute agent creation works for common patterns (clone → modify → commit → PR). Complex multi-step workflows still take 1–2 days and likely require engineering support.

This is honest framing. The platform lowers the barrier for routine automation while preserving the ability to build complex agents when needed.

### Lesson 4: 180 Tools Requires Tool Management

With 180+ MCP tools, tool selection becomes a first-class problem. Approaches to managing large tool sets include:

- **Tool categorization** — grouping tools by domain (what [Datadog calls "toolsets"](/guides/datadog-mcp-server-production-lessons/))
- **Dynamic tool loading** — loading only relevant tools based on conversation context
- **Tool descriptions** — well-crafted descriptions that help the LLM pick correctly
- **Routing layers** — pre-classifying user intent before presenting tool options

Duolingo's specific approach to this problem wasn't detailed in published materials, but the 180+ count means they've had to solve it.

---

## Gaps and Open Questions

Duolingo's published materials leave several questions unanswered:

| Question | Status |
|----------|--------|
| **Error rates** for AI-generated PRs | Not published |
| **Cost per agent run** | Not published |
| **Percentage of PRs merged without modification** | Not published |
| **How the Slackbot selects from 180+ tools** | Not detailed |
| **Security model for tool access** | Not detailed |
| **Observability beyond Slack notifications** | Not detailed |
| **Docker-in-Docker constraint** on Temporal | Was expected to resolve by early 2026 |

These gaps are normal for first-generation case studies. As with Pinterest's initial blog post, expect more operational detail to emerge over time.

---

## Comparison: Enterprise MCP Deployments

| Dimension | Duolingo | Pinterest | Datadog |
|-----------|----------|-----------|---------|
| **MCP tool count** | 180+ | ~20 | ~16 core + 13 toolsets |
| **Primary use case** | Internal assistant + code automation | Engineering automation | External developer tool |
| **Architecture** | Centralized Slackbot + workflow platform | Domain-specific servers + registry | Remote hosted server |
| **Orchestration** | Temporal | Airflow MCP server | — |
| **Human oversight** | PR review for code changes | Elicitation-based approval | — |
| **Auth model** | OAuth 2.1 (Slack MCP) | JWT + service mesh | OAuth 2.1 |
| **Open source** | [slack-mcp](https://github.com/duolingo/slack-mcp) | — | — |
| **LLM providers** | Codex + Claude | Not published | Not applicable |

---

## What This Means for the MCP Ecosystem

Duolingo's deployment validates three trends we've been tracking:

**1. MCP is becoming internal infrastructure, not just developer tooling.** Duolingo's Slackbot isn't for developers — it's for anyone in the company who needs to find information, triage alerts, or navigate internal systems.

**2. The no-code agentic workflow pattern is emerging.** Duolingo, Pinterest, and others are building platforms that let non-specialist employees create MCP-powered automations. This shifts MCP from a developer tool to an organizational capability.

**3. 100+ tool deployments are real.** With 180+ tools, Duolingo pushes past the scale where simple tool lists work. Expect to see more work on tool selection, categorization, and dynamic loading as enterprises hit similar scale.

---

## Further Reading

- [Duolingo Blog: Agentic Workflows](https://blog.duolingo.com/agentic-workflows/) — the no-code platform architecture
- [Duolingo Blog: Building AI Agents](https://blog.duolingo.com/buildingaiagents/) — the feature flag removal agent
- [duolingo/slack-mcp on GitHub](https://github.com/duolingo/slack-mcp) — open-source Slack MCP server
- [MCP Dev Summit 2026 Schedule](https://mcpdevsummitna26.sched.com/) — Aaron Wang's keynote session
- [Pinterest's MCP Production Case Study](/guides/pinterest-mcp-production-case-study/) — similar enterprise deployment
- [Uber's MCP Gateway](/guides/uber-mcp-gateway-agentic-engineering/) — centralized gateway turning any endpoint into an MCP server
- [Datadog's MCP Server Design Lessons](/guides/datadog-mcp-server-production-lessons/) — tool design at scale
- [MCP in Production](/guides/mcp-in-production/) — patterns across enterprise deployments

