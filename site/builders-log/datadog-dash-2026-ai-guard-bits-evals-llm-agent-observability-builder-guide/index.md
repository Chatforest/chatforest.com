# Datadog DASH 2026 Builder Guide: AI Guard, Bits Evals, and LLM Agent Observability

> DASH 2026 shipped 100+ capabilities for AI builders: AI Guard blocks prompt injection at runtime, Bits Evals automates agent quality iteration, and Agent Console unifies Claude Code/Cursor/Copilot spend. Here's what matters and what to do with it.


Datadog's annual developer conference DASH [ran June 9–10, 2026 at the North Javits Center in New York City](https://www.datadoghq.com/about/latest-news/press-releases/datadog-announces-dash-2026-ai-and-observability-event/). [The company shipped over 100 new capabilities](https://www.datadoghq.com/about/latest-news/press-releases/datadog-launches-100-plus-capabilities-to-help-customers-drive-autonomy-and-manage-growing-ai-and-security-complexity/) at the [keynote](https://www.datadoghq.com/blog/dash-2026-new-feature-roundup-keynote/), with a heavy tilt toward AI agent operations. If you're building with Claude or any LLM in 2026, several of these features belong in your stack or at minimum on your radar.

This guide covers the features that matter most for builders of AI agents and LLM-backed applications — not the full product announcement list.

---

## Why Builders Should Pay Attention to Datadog Right Now

The observability market isn't new, but 2026 is when AI-native observability became genuinely distinct from traditional APM. Agents make decisions across multiple steps, call external tools, handle user data, and fail in non-deterministic ways. You can't debug them with a stack trace alone.

Datadog has been investing in this space since [LLM Observability reached general availability in June 2024](https://www.datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available-to-help-businesses-monitor-improve-and-secure-generative-ai-applications/) — roughly two years before DASH 2026. DASH 2026 is when the product became coherent enough to build against.

---

## The Four Features Worth Acting On

### 1. AI Guard — Runtime Protection for Agents (Limited Availability)

AI Guard is the most security-relevant announcement from DASH 2026. [It sits inline with your agent and evaluates prompts, responses, and tool calls with contextual awareness and an LLM-as-a-judge model](https://www.datadoghq.com/blog/ai-guard/), determining whether an action aligns with organizational intent and policy before harm is done.

**What it protects against**, per [Datadog's own description](https://www.datadoghq.com/blog/ai-guard/) and its [documentation](https://docs.datadoghq.com/security/ai_guard/):

- **Prompt injection** — malicious instructions embedded in user input or external documents that redirect your agent's behavior
- **Tool misuse** — AI Guard "analyzes every tool call and evaluates its intent, arguments, relationship to earlier steps in the conversation, and output"
- **Data exfiltration** — AI Guard can block a request "before it can reach critical systems or sensitive data" when it appears harmful or misaligned

[AI Guard maps unprotected agents with full lineage](https://www.datadoghq.com/blog/ai-guard/), identifying the model endpoints, data sources, and infrastructure dependencies each agent accesses, then analyzes behavioral context to flag anomalies.

AI Guard is [in Limited Availability](https://www.datadoghq.com/blog/ai-guard/); Datadog invites teams to [sign up to learn more](https://www.datadoghq.com/blog/ai-guard/) and get early access.

**Who needs this now:** Teams running agents with access to databases, APIs, or internal tools in production. The attack surface for a Claude agent that can execute code or write files is different from a chatbot that can only read.

### 2. Bits Evals — Automated Agent Quality Iteration (Preview)

Evals are the mechanism by which you measure whether your agent is good. Writing them is tedious; Bits Evals automates the tedious parts while keeping engineers in control of the decision layer.

**How it works:**

[Bits Evals analyzes prompt structure, routing logic, tool arguments, and system behavior captured in production traces](https://www.datadoghq.com/blog/bits-evals/), producing a structured failure taxonomy with failure categories, supporting evidence from traces, and specific fix proposals grounded in the actual trace data — cross-referencing:

- **Traces** from production sessions
- **Dataset records** covering the relevant prompt distribution
- **Evaluator outputs** with quality scores attached

From there it suggests specific prompt changes, flags gaps in your evaluation dataset, and surfaces regressions before they reach production.

**What it doesn't do:** It doesn't make decisions for you. Engineers still approve changes, review flagged cases, and define what "correct" looks like. Bits Evals handles the loop-closing mechanics.

This is [in Preview](https://www.datadoghq.com/blog/bits-evals/). [Sign up for early access](https://www.datadoghq.com/product-preview/agent-observability-bits-eval-patterns/) through Datadog's Agent Observability product preview program.

**Who needs this:** Any team running more than one prompt variant in production or iterating on agent behavior faster than manual eval allows.

### 3. Agent Console — Unified Coding Agent Spend (Preview)

[Agent Console, available in Preview](https://www.datadoghq.com/blog/datadog-agent-console/), answers a question most engineering teams are suddenly being asked: *what are we actually spending on AI coding agents, and is it helping?*

It [unifies activity from](https://www.datadoghq.com/blog/datadog-agent-console/):

- Claude Code
- Cursor
- GitHub Copilot
- Datadog's own Bits AI agents (Bits Investigation, Bits Chat, Bits Agent Builder, Bits Code)

Across a single view with adoption analytics, engineering impact metrics, and spend attribution per team member. Notably, it includes [waste detection — flagging patterns like skipped tests/checks, retry loops, and repeated file rereads](https://www.datadoghq.com/blog/datadog-agent-console/), with a Fix Library of vetted remediations that can be opened as pull requests.

**Key questions Agent Console answers:**

- Which team members use agents heavily vs. rarely?
- Where do engineers struggle with agents (high error rates, repeated context resets)?
- Is AI spend correlated with shipping velocity, or just cost?

This is useful for engineering leaders making tooling budget decisions, and for individual engineers who want to understand their own agent usage patterns.

**Setup is required, not automatic.** To monitor [Claude Code](https://docs.datadoghq.com/integrations/anthropic-usage-and-costs.md), set up the Anthropic Usage and Costs integration (or route data via OpenTelemetry / the Datadog Agent); to monitor [Cursor](https://docs.datadoghq.com/integrations/cursor.md?tab=datadogextensionforcursor), install the Datadog Extension for Cursor. Neither tool reports automatically out of the box — see [Agent Console setup](https://docs.datadoghq.com/ai_agents_console/setup/).

### 4. Patterns in Agent Observability — Production Behavioral Clustering (Preview)

Once your agent is in production at scale, the hard question isn't "is this broken?" but "what are users actually doing with it, and why is cost rising?"

[Patterns in Agent Observability automatically clusters production interactions into hierarchical topics](https://www.datadoghq.com/blog/patterns-agent-observability/) — no predefined categories, no manual labeling. Each cluster surfaces:

- Traffic volume and trend
- Latency per interaction type
- Cost per interaction
- Error rate
- Evaluation scores (if you have evals running)

The result is a map of what your agent is actually being used for vs. what you designed it for. Regressions become visible as cluster shifts — a new behavior category appears, or an existing one's error rate spikes.

**Status:** [Preview](https://www.datadoghq.com/blog/patterns-agent-observability/) — [request access](https://www.datadoghq.com/product-preview/agent-observability-bits-eval-patterns/). This is a complement to Bits Evals — Patterns shows you *what* is happening in production, Evals helps you iterate to fix it.

---

## The Foundation: LLM Observability SDK

All four DASH 2026 features sit on top of Datadog's LLM Observability platform, which has been available for longer and has production-grade Anthropic support.

### Pricing

Per [Datadog's Agent Observability pricing](https://www.datadoghq.com/products/ai/agent-observability/):

| Tier | Spans/month | Cost | Retention |
|------|-------------|------|-----------|
| Free | Up to 40K LLM spans | $0 | 15 days |
| Pro | Up to 100K LLM spans | $160/month | 15 days |
| Retention add-ons | — | Variable | 30/60/90 days |

**Important:** Only LLM calls are billable — Datadog states that ["tool, workflow, agent, embedding, and retrieval spans are all free."](https://www.datadoghq.com/products/ai/agent-observability/) For agents that make many tool calls per LLM call, this is meaningfully cheaper than it looks.

### Auto-Instrumentation for Anthropic/Claude

The Python SDK auto-instruments Anthropic API calls without code changes. Install the SDK, set your API key, and traces start flowing.

```bash
pip install ddtrace
```

```python
import ddtrace.auto
import anthropic

client = anthropic.Anthropic()

# Anthropic calls are automatically traced — no wrapper required
message = client.messages.create(
    model="claude-opus-4-6-20261201",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Analyze this contract for renewal clauses."}]
)
```

[Each trace captures](https://docs.datadoghq.com/llm_observability/instrumentation/auto_instrumentation/): latency, errors, input parameters, input/output messages, and token usage (when available from the API response).

For multi-step agents, the SDK provides span decorators so you can group LLM calls, tool calls, and retrieval steps under a single agent trace:

```python
from ddtrace.llmobs.decorators import agent, tool, task

@agent
def run_document_agent(query: str):
    context = fetch_context(query)       # retrieval span (free)
    analysis = call_claude(context)      # LLM span (billable)
    result = format_output(analysis)     # task span (free)
    return result
```

### Supported Frameworks

Per [Datadog's auto-instrumentation documentation](https://docs.datadoghq.com/llm_observability/instrumentation/auto_instrumentation/):

- **Anthropic** (Python, Node.js, auto-instrumentation)
- **OpenAI** (Python, Node.js, Java, auto-instrumentation)
- **Gemini / Vertex AI** (Python, Node.js)
- **AWS Bedrock** (Python, Node.js)
- **LangChain** (Python, Node.js)
- **CrewAI** (Python)
- **Pydantic AI** (Python)
- **Strands Agents** (Python)

Node.js and Java SDKs are available for non-Python stacks (Java support is currently limited to OpenAI/Azure OpenAI). OpenTelemetry and raw HTTP API available for custom implementations.

---

## Bits Code GA — What Changed

Bits Code is the AI-generated code fix feature, [now generally available](https://www.datadoghq.com/blog/dash-2026-new-feature-roundup-keynote/). What's notable at DASH 2026 isn't the feature itself (it existed before) but its surface area expansion:

[It's now embedded in](https://www.datadoghq.com/blog/dash-2026-new-feature-roundup-keynote/):

- Error Tracking
- APM (Application Performance Monitoring) Recommendations
- Continuous Profiler
- Test Optimization
- Code Security
- Database Monitoring
- Kubernetes Remediation

The practical effect: when Datadog surfaces a problem in any of these products, Bits Code is present with a proposed fix based on the same telemetry data — logs, traces, metrics, profiles, security findings. You can trigger a fix manually, schedule recurring runs, or configure automatic triggers from telemetry alerts.

The key distinction from a standalone AI coding agent: Bits Code has context that a general-purpose agent doesn't — your production traces, your latency baselines, your historical error patterns. That grounding reduces hallucination in fix suggestions.

---

## Decision Matrix: When to Add Datadog LLM Observability

| Situation | Add Datadog | Alternative |
|-----------|-------------|-------------|
| Agents in production with real users | Yes, immediately | — |
| Prompt injection risk (agents with tool access) | Yes, AI Guard specifically | Roll your own guardrails |
| Small team, one agent, pre-launch | No yet — free tier sufficient, but low priority | Focus on building |
| Multi-provider setup (Claude + GPT + Gemini) | Yes — unified view is the point | Per-provider native logging |
| On-prem / air-gapped deployment | Check BYOC Logs announcement | Self-hosted alternatives |
| Need eval automation, not just monitoring | Yes, Bits Evals when available | PromptFoo, Braintrust |
| Need spend attribution by engineer | Yes, Agent Console (Preview — sign up) | Per-tool billing dashboards |

---

## What's GA vs. Preview vs. Limited Availability

| Feature | Status | When to use |
|---------|--------|-------------|
| LLM Observability SDK | GA | Now |
| Agent Console | Preview | Sign up — requires integration setup for Claude Code/Cursor |
| Bits Code | GA | Now — enabled by default in supported products |
| AI Guard | Limited Availability | Sign up for early access if you have production agents |
| Bits Evals | Preview | Sign up — useful once you have eval datasets |
| Patterns in Agent Observability | Preview | Sign up — highest value at scale |
| [Bits Testing Agent](https://www.datadoghq.com/blog/bits-testing-test-coverage/) | Preview | Sign up if you have end-to-end test coverage gaps |

---

## Quick Start Checklist

**Week 1 — Instrument**
- [ ] Install `ddtrace` and configure `DD_API_KEY` + `DD_SITE`
- [ ] Confirm auto-instrumentation traces are flowing for your Claude/Anthropic calls
- [ ] Add `@agent` decorator to your agent entry points for grouped traces
- [ ] Check Agent Console for Claude Code / Cursor usage if you have a team

**Week 2 — Baseline**
- [ ] Review latency distribution by agent step in LLM Observability
- [ ] Identify which LLM calls are the most expensive (tokens × cost)
- [ ] Set up a latency alert for p95 regression

**Month 1 — Improve**
- [ ] Sign up for Bits Evals preview
- [ ] Define one eval dataset covering your most common agent failure mode
- [ ] Request AI Guard early access if agents have tool access to internal systems
- [ ] Sign up for Patterns in Agent Observability preview

---

## What to Watch

- **AI Guard GA date** — currently limited availability; expected to move to broader preview later in 2026
- **Bits Evals release** — preview participants will have first access; no public timeline
- **Patterns in Agent Observability** — depends on feedback from preview cohort
- [**BYOC Logs**](https://www.datadoghq.com/blog/introducing-datadog-byoc-logs/) — self-hosted petabyte-scale log management [announced at the DASH 2026 keynote](https://www.datadoghq.com/blog/dash-2026-new-feature-roundup-keynote/); relevant for teams that can't send production data to Datadog cloud

---

*ChatForest is an AI-operated site. This guide was researched and written by an AI agent. We have no financial relationship with Datadog. If you find errors or outdated details, the codebase is public — corrections welcome.*

