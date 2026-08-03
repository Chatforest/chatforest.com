# Two Production Deployments, One Webinar: What Zed and ClickHouse Will Reveal About Running Claude Sonnet 5 at Scale

> On July 13, Anthropic hosts a live webinar where Zed (code editor, 100k+ daily devs) and ClickHouse (analytics database, $250M ARR) share how they ship Claude Sonnet 5 in production at high volume. Here's what we know about both deployments before the session.


On **[July 13, 2026, at 8:00 am PT](https://www.anthropic.com/webinars/production-grade-agents-on-claude-sonnet-5-live-with-zed-and-clickhouse)**, Anthropic will host a live webinar that is unusual for a model announcement: it doesn't announce a model. Instead, it puts two companies onstage who have already shipped Claude Sonnet 5 in production — at high volume, on real workloads — and asks them to talk about what actually happened.

The two companies are **Zed** (a [Rust-built](https://github.com/zed-industries/zed) code editor that [Zed 1.0 says](https://zed.dev/blog/zed-1-0) "hundreds of thousands of developers" rely on daily) and **ClickHouse** (an analytics database that [crossed $250M in annual run-rate revenue and 4,000 customers](https://clickhouse.com/blog/clickhouse-tops-250m-arr-and-4000-customers) as of May 2026). One runs Claude inside an IDE. The other runs Claude against petabyte-scale data. Both chose Sonnet 5 specifically — and both have production metrics behind that decision.

Here's what we know about each deployment before the session.

---

## Why These Two Companies

Zed and ClickHouse are not obvious pairing choices. One is developer tooling; the other is data infrastructure. But they share a structural challenge: **sustained, high-volume agent work where per-token cost is a real constraint**.

A code editor with hundreds of thousands of daily users cannot afford to route every autocomplete and refactor suggestion through a flagship model. An analytics database handling millions of daily queries cannot pay [Opus-tier output pricing — $25 per million tokens](https://platform.claude.com/docs/en/about-claude/pricing) — on every SQL generation request. Both need intelligence that holds up at volume without a runaway inference bill.

That's the Sonnet 5 pitch: [$2 per million input tokens and $10 per million output tokens through August 31, 2026, rising to $3/$15 after](https://platform.claude.com/docs/en/about-claude/pricing) — a fraction of Opus pricing. The model is positioned as "flagship-close performance at Sonnet pricing" — specifically designed for the class of workload where you need the agent working across an entire product, not reserved for the hardest calls.

Zed and ClickHouse are two real-world answers to the question: does that pitch hold in production?

---

## Zed: Claude Inside the Editor, Across 100,000 Daily Sessions

**[Zed 1.0 shipped April 29, 2026](https://zed.dev/blog/zed-1-0)** — "five years" of work, "exceeding a million lines of code" ([Rust](https://github.com/zed-industries/zed), specifically), and a design philosophy built around making humans and AI agents share a live codebase without stepping on each other.

The AI architecture inside Zed is now fully production-hardened:

- **[Multiple parallel agent threads](https://zed.dev/blog/parallel-agents)** (shipped April 22, 2026) — you can orchestrate several agents running concurrently in the same editor window, each with an independent context window, and mix and match agents on a per-thread basis.
- **[Terminal Threads](https://zed.dev/blog/terminal-threads)** (shipped May 20, 2026) — Claude Code, Amp, or another CLI agent runs as a persistent sidebar thread alongside editor context, with the same navigation and notifications as native Agent threads.
- **[ACP integration](https://zed.dev/blog/claude-code-via-acp)** — Zed built an open-source adapter that wraps the Claude Code SDK and translates its interactions into the Agent Client Protocol (ACP), an open standard for connecting AI agents to editors, which makes the integration composable with other ACP-compatible tools.
- **[DeltaDB](https://zed.dev/blog/introducing-deltadb)** — a CRDT-based version-control system, in early access as of mid-2026, designed to track every edit (not just commits) and keep a shared, character-level view of the codebase in real time between humans and AI agents.

**[Neel Chotai, a backend engineer at Zed](https://www.anthropic.com/webinars/production-grade-agents-on-claude-sonnet-5-live-with-zed-and-clickhouse)**, will represent the team at the webinar. Zed [supports multiple LLM providers](https://zed.dev/docs/ai/llm-providers) — including Anthropic, OpenAI, and Google models directly, plus gateways like OpenRouter, Bedrock, and Vercel.

The open question Zed's session should answer: **how do you manage context across parallel agent sessions at 100k+ daily active users?** Thread isolation is the obvious answer, but at that volume, the engineering decisions around context budgeting, failure handling, and routing between models must be non-trivial.

---

## ClickHouse: 45 Million Claude Tokens Per Day Against Production Data

ClickHouse's deployment is a different shape entirely. At their **[Open House 2026](https://clickhouse.com/blog/clickhouse-tops-250m-arr-and-4000-customers)** conference on May 27, 2026, the company announced the public beta of **[ClickHouse Agents](https://clickhouse.com/blog/clickhouse-agents-beta)** — a fully managed agentic analytics service powered by Claude.

Before going public beta, ClickHouse ran it internally. Per [ClickHouse's own announcement](https://clickhouse.com/blog/clickhouse-agents-beta), the internal numbers are striking:

- **[Around 80% of ClickHouse employees use the platform daily](https://clickhouse.com/blog/clickhouse-agents-beta)**
- **[Roughly 70% of ClickHouse's internal data-warehouse queries](https://clickhouse.com/blog/clickhouse-agents-beta)** are now handled through it
- **[More than 45 million tokens processed a day](https://clickhouse.com/blog/clickhouse-agents-beta)**
- ClickHouse [describes it](https://clickhouse.com/blog/clickhouse-agents-beta) as, "by some distance, the most-used internal tool we run"

(Note: these are three separate metrics, not one compound statistic — 80% of employees, 70% of query volume, and 45M+ tokens/day are independent figures from the same post.)

The use case: natural-language queries against live ClickHouse data. A product manager asks "what's driving the churn spike last week?" and receives SQL, results, visualizations, and follow-up questions within seconds — without writing SQL or waiting for a data engineer handoff.

Why Claude? ClickHouse says **["the Claude family came out on top consistently, across SQL generation, schema reasoning, and tool use"](https://clickhouse.com/blog/clickhouse-agents-beta)** in their internal benchmarking — all three dimensions that matter for an analytics agent that needs to construct correct queries against arbitrary schemas. Per the same post, [Claude Sonnet and Haiku models come pre-configured as the default for every ClickHouse Cloud customer](https://clickhouse.com/blog/clickhouse-agents-beta).

The architecture, [per ClickHouse](https://clickhouse.com/blog/clickhouse-agents-beta), includes:
- A no-code Agent Builder with custom instructions, skills, context files, and MCP tool access
- A managed, multi-tenant chat interface for natural-language queries and multi-turn conversations
- A sandboxed code interpreter supporting Bash, Python, and JavaScript execution against live query results
- Native MCP compatibility for connecting external tools
- Multi-agent workflows that orchestrate subagents across analytical tasks
- Enterprise security: SSO, encrypted message storage, and governed data access

**[Ryadh Dahimene](https://www.anthropic.com/webinars/production-grade-agents-on-claude-sonnet-5-live-with-zed-and-clickhouse)** (AI/ML Product at ClickHouse) will present at the webinar.

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
- How do you evaluate agent quality at scale? Human review doesn't scale to [45 million tokens per day](https://clickhouse.com/blog/clickhouse-agents-beta).
- What proxy metrics (e.g., user re-run rate, query acceptance rate, session length) do you use as quality signals?

---

## The Introductory Pricing Clock

One tactical point worth tracking: **[Claude Sonnet 5 introductory pricing ends August 31, 2026](https://platform.claude.com/docs/en/about-claude/pricing)**. After that, input pricing rises from $2 to $3 per million tokens and output pricing rises from $10 to $15 per million tokens — a 50% increase.

At ClickHouse's [45M+ daily tokens](https://clickhouse.com/blog/clickhouse-agents-beta), the output token cost increase alone is material. It's likely that some of the architectural decisions Zed and ClickHouse made — model routing, caching strategies, batching patterns — were shaped by awareness of this cliff.

Asking directly: "would your current architecture change if Sonnet 5 pricing returned to standard?" would surface whether the design is sustainable beyond August 31 or whether there's a re-routing decision coming.

---

## Register and Watch

The webinar is free. [Speakers](https://www.anthropic.com/webinars/production-grade-agents-on-claude-sonnet-5-live-with-zed-and-clickhouse):

- **Musa Mohannad** — Applied AI, Anthropic
- **Neel Chotai** — Backend Engineer, Zed
- **Ryadh Dahimene** — AI/ML Product, ClickHouse

**Date**: July 13, 2026 at 8:00 am PT (11:00 am ET, 4:00 pm BST, 5:00 pm CET)

Register at [anthropic.com/webinars](https://www.anthropic.com/webinars/production-grade-agents-on-claude-sonnet-5-live-with-zed-and-clickhouse). A recording is expected after the session.

The session is worth attending live if you are building agents that need to run at high volume against structured data or code. Two companies that solved this problem in different ways will be in the same room. That's harder to find than most conference talks.

