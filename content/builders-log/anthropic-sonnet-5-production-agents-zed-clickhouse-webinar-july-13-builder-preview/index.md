---
title: "Two Production Deployments, One Webinar: What Zed and ClickHouse Will Reveal About Running Claude Sonnet 5 at Scale"
date: 2026-07-05
description: "On July 13, Anthropic hosts a live webinar where Zed (code editor, 100k+ daily devs) and ClickHouse (analytics database, $250M ARR) share how they ship Claude Sonnet 5 in production at high volume. Here's what we know about both deployments before the session."
og_description: "Zed runs parallel Claude agents across 100k+ daily developer sessions. ClickHouse runs 70 million Claude tokens per day for agentic analytics. On July 13, they'll share the design decisions that made it work. Builder preview inside."
content_type: "Builder's Log"
categories: ["AI Tools", "Agent Architecture", "Developer Tools"]
tags: ["claude", "sonnet-5", "claude-sonnet-5", "zed", "clickhouse", "agents", "production", "webinar", "agentic", "ai-coding", "analytics", "builder-guide", "anthropic"]
---

On **July 13, 2026, at 8:00 am PT**, Anthropic will host a live webinar that is unusual for a model announcement: it doesn't announce a model. Instead, it puts two companies onstage who have already shipped Claude Sonnet 5 in production — at high volume, on real workloads — and asks them to talk about what actually happened.

The two companies are **Zed** (a Rust-built code editor with over 100,000 daily developers) and **ClickHouse** (an analytics database at $250M ARR with 4,000 customers). One runs Claude inside an IDE. The other runs Claude against petabyte-scale data. Both chose Sonnet 5 specifically — and both have production metrics behind that decision.

Here's what we know about each deployment before the session.

---

## Why These Two Companies

Zed and ClickHouse are not obvious pairing choices. One is developer tooling; the other is data infrastructure. But they share a structural challenge: **sustained, high-volume agent work where per-token cost is a real constraint**.

A code editor with 100,000 daily users cannot afford to route every autocomplete and refactor suggestion through a flagship model. An analytics database handling millions of daily queries cannot burn $0.015 per output token on every SQL generation request. Both need intelligence that holds up at volume without a runaway inference bill.

That's the Sonnet 5 pitch: $2 per million input tokens and $10 per million output tokens through August 31, 2026 (rising to $3/$15 after). The model is positioned as "flagship-close performance at Sonnet pricing" — specifically designed for the class of workload where you need the agent working across an entire product, not reserved for the hardest calls.

Zed and ClickHouse are two real-world answers to the question: does that pitch hold in production?

---

## Zed: Claude Inside the Editor, Across 100,000 Daily Sessions

**Zed 1.0 shipped April 29, 2026** — five years of work, more than a million lines of Rust, and a design philosophy built around making humans and AI agents share a live codebase without stepping on each other.

The AI architecture inside Zed is now fully production-hardened:

- **Multiple parallel agent threads** — you can run three agents concurrently in the same editor window, each with an independent context window. One debugging a failing test, another refactoring an endpoint, a third updating documentation.
- **Terminal Threads** (added May 20, 2026) — Claude Code or Amp runs as a sidebar agent alongside editor context. The agent sees the terminal, the diff, and the file tree simultaneously.
- **ACP integration** — Zed built their Claude Code integration using the Agent Client Protocol, an open standard for connecting AI agents to editors. The Claude Code SDK is wrapped in an ACP adapter, which makes the integration composable with other ACP-compatible agents.
- **DeltaDB** — a CRDT sync engine that gives humans and AI agents a shared, character-level view of the codebase in real time, including in remote collaboration sessions.

**Neel Chotai**, a backend engineer at Zed, will represent the team at the webinar. Zed supports 15 LLM providers, but Claude Sonnet remains the primary recommendation for most editing and agentic tasks — "fast, highly capable, and more cost-effective than Opus" per the docs.

The open question Zed's session should answer: **how do you manage context across parallel agent sessions at 100k+ daily active users?** Thread isolation is the obvious answer, but at that volume, the engineering decisions around context budgeting, failure handling, and routing between models must be non-trivial.

---

## ClickHouse: 70 Million Claude Tokens Per Day Against Production Data

ClickHouse's deployment is a different shape entirely. At their **Open House 2026** conference in May, the company announced the public beta of **ClickHouse Agents** — a fully managed agentic analytics service powered by Claude.

Before going public beta, ClickHouse ran it internally. The internal numbers are striking:

- **80% of ClickHouse employees use the platform daily**
- **70 million tokens per day total**
- **45 million tokens per day in analytical queries alone**
- It became the company's most-used internal tool

The use case: natural-language queries against live ClickHouse data. A product manager asks "what's driving the churn spike last week?" and receives SQL, results, visualizations, and follow-up questions within seconds — without writing SQL or waiting for a data engineer handoff.

Why Claude? **The Claude family won internal benchmarking** across SQL generation, schema reasoning, and tool use — all three dimensions that matter for an analytics agent that needs to construct correct queries against arbitrary schemas. Both Sonnet and Haiku models come pre-configured for all Cloud customers.

The architecture includes:
- No-code agent builder with custom instructions and skills
- Native chat interface
- Sandboxed code interpreter supporting Bash, Python, and JavaScript
- MCP compatibility for connecting external tools
- Multi-agent workflows with artifact sharing
- Enterprise security (SSO, RBAC, encryption)

**Ryadh Dahimene** (AI/ML Product at ClickHouse) will present at the webinar.

The open question for ClickHouse's session: **at 45 million analytical tokens per day, how do you handle schema volatility?** ClickHouse tables change. New columns appear, old ones get deprecated. An agent that was accurate last week can generate wrong queries this week if its schema context is stale. Keeping agents grounded in live schema state at that volume is an unsolved problem in most deployment guides.

---

## What Builders Should Listen For

These are the questions where Zed and ClickHouse likely have real answers — and where most builders are still guessing:

**On context management:**
- What is the maximum effective context window for a productive agent session? Where does coherence fall off?
- How do you handle thread-level vs. session-level memory?

**On routing and model selection:**
- When do you use Sonnet 5 vs. Haiku vs. Opus? Is the split based on task complexity, cost threshold, or latency requirement?
- What's the cheapest model that produces acceptable output quality for your most common task type?

**On production failures:**
- What does your retry and fallback logic look like?
- What's your error rate on tool calls, and what happens to the user when a tool call fails mid-session?

**On cost at scale:**
- What is your actual per-user or per-query Claude cost at production volume?
- Did Sonnet 5's introductory pricing change your architectural decisions — or was the direction already set before June 30?

**On evaluation:**
- How do you evaluate agent quality at scale? Human review doesn't scale to 70 million tokens per day.
- What proxy metrics (e.g., user re-run rate, query acceptance rate, session length) do you use as quality signals?

---

## The Introductory Pricing Clock

One tactical point worth tracking: **Claude Sonnet 5 introductory pricing ends August 31, 2026**. After that, input pricing rises from $2 to $3 per million tokens and output pricing rises from $10 to $15 per million tokens — a 50% increase.

At ClickHouse's 70M daily tokens, the output token cost increase alone is material. It's likely that some of the architectural decisions Zed and ClickHouse made — model routing, caching strategies, batching patterns — were shaped by awareness of this cliff.

Asking directly: "would your current architecture change if Sonnet 5 pricing returned to standard?" would surface whether the design is sustainable beyond August 31 or whether there's a re-routing decision coming.

---

## Register and Watch

The webinar is free. Speakers:

- **Musa Mohannad** — Applied AI, Anthropic
- **Neel Chotai** — Backend Engineer, Zed
- **Ryadh Dahimene** — AI/ML Product, ClickHouse

**Date**: July 13, 2026 at 8:00 am PT (11:00 am ET, 4:00 pm BST, 5:00 pm CET)

Register at [anthropic.com/webinars](https://www.anthropic.com/webinars/production-grade-agents-on-claude-sonnet-5-live-with-zed-and-clickhouse). A recording is expected after the session.

The session is worth attending live if you are building agents that need to run at high volume against structured data or code. Two companies that solved this problem in different ways will be in the same room. That's harder to find than most conference talks.
