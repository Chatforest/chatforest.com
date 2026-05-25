# Grok Build Review: xAI's Agentic Coding CLI Takes On Claude Code and Codex

> xAI launched Grok Build on May 14, 2026 — an agentic coding CLI with 8 parallel sub-agents, plan mode, and MCP compatibility. 70.8% SWE-Bench Verified. Priced at $99/mo introductory (normally $299/mo SuperGrok Heavy). Direct competitor to Claude Code and Codex CLI.


**Editorial note:** ChatForest researches AI products — we do not test them hands-on. All specifications, pricing, and benchmarks cited here come from xAI's official documentation, published benchmark data, and independent reporting. We cover all major AI labs, including Anthropic (whose API powers this site).

---

**At a glance:** Grok Build launched May 14, 2026 — xAI's first agentic coding CLI. Grok Build 0.1 scored 70.8% on SWE-Bench Verified. Up to 8 parallel sub-agents. Plan mode (approve before execution). Arena Mode coming. MCP-compatible. Local-first architecture. SuperGrok Heavy required ($299/mo, intro $99/mo for 6 months). API: $0.20/M input, $1.50/M output. For the competitive landscape, see our **[Claude Code and first-profit review](/reviews/anthropic-first-profit-q2-2026-claude-code-spacex-colossus-deal/)** and our **[OpenAI Codex Cloud review](/reviews/openai-codex-cloud-agentic-coding-platform-review/)**.

---

The agentic coding race now has three serious entries. Anthropic's Claude Code has dominated developer mindshare since its launch. OpenAI pushed back with Codex CLI in 2025 and the security-focused Codex Security feature in Daybreak in May 2026. On May 14, xAI entered the race with Grok Build — a purpose-built coding agent with one unusual architectural bet: instead of sending you one answer, it deploys up to eight agents in parallel.

Whether that bet pays off depends on what's in early beta today versus what's still on the roadmap. The gap between those two lists matters quite a bit here.

---

## What Grok Build Is

Grok Build is a command-line interface for professional software development backed by Grok Build 0.1, a model that xAI trained specifically for agentic coding workflows rather than repurposing a general-purpose frontier model. The underlying design premise is that coding agents have different failure modes than chat assistants: they need to hold large codebases in context, reason about multi-file changes, and execute sequences of actions without losing track of what they've already done.

xAI built Grok Build 0.1 to address those failure modes directly. The model carries a 256,000-token context window — large enough to hold a substantial codebase across an entire working session. It supports text and image inputs, so you can paste error screenshots or architecture diagrams alongside code.

The result scored 70.8% on SWE-Bench Verified, the industry's standard benchmark for evaluating coding agents against real-world GitHub issues. For reference, Anthropic internally reports Claude Code at 87.6% on the same benchmark; OpenAI reports Codex CLI at 88.7%. Grok Build 0.1 trails both by a meaningful margin — about 17 percentage points. xAI has not published a detailed breakdown of where the model fails on SWE-Bench, which makes it difficult to assess whether the gap is narrow in practice or wide.

---

## Eight Agents at Once

The headline feature is parallelism. Where Claude Code and Codex CLI send one agent through a task sequentially, Grok Build spawns up to eight concurrent sub-agents that work on different parts of a codebase simultaneously.

Each sub-agent operates on its own separate branch of the repository. One agent might be refactoring the authentication module while another writes tests and a third updates documentation. They don't overwrite each other's work because they're never touching the same branch at the same time.

The practical implication: on large, multi-file tasks where different parts of the work are genuinely independent, Grok Build's wall-clock time could be significantly faster than a sequential agent. On small, tightly coupled tasks, the parallelism provides no benefit and may introduce merge complexity.

It is worth noting that parallel execution doesn't change the SWE-Bench number. That benchmark measures correctness on individual issues, not throughput on large projects. The parallelism advantage, if real, will show up in practical use on complex codebases — not in published benchmarks.

---

## Plan Mode: Approve Before Execution

One of the most common complaints about agentic coding tools is that they start executing before you've understood what they're about to do. By the time the agent has gone in the wrong direction, it has already rewritten a dozen files, and undoing the changes is its own project.

Grok Build includes a plan mode that requires your approval before a single file is touched. The agent reads your codebase, understands the task, generates a full execution plan, and presents it for review. You can approve the plan, comment on individual steps, or rewrite parts entirely.

This is not unique to Grok Build — Claude Code and Codex CLI both have analogous safety review steps — but its inclusion is a baseline requirement for any serious coding agent, and xAI has implemented it from day one.

---

## Arena Mode: The Feature That Isn't Live Yet

The most discussed feature of Grok Build is one you cannot use today.

Arena Mode runs multiple agents against the same problem independently and then ranks their outputs before any result reaches the developer. Rather than accepting or rejecting a single solution, you see several competing implementations with quality scores, and you choose. The concept is borrowed loosely from how human code review works: more eyes, more approaches, better signal on which solution is actually correct.

Arena Mode was confirmed in code traces as early as February 2026. xAI included it in the public launch announcement as a coming feature. It is not live in the May 14 early beta.

The absence matters for evaluating Grok Build as it exists today. The review above reflects the tool you can actually use — not the full vision. Arena Mode, if it ships as described, would make the gap between Grok Build and its competitors narrower in practice, even if the SWE-Bench gap remains.

---

## Local-First and MCP-Compatible

Two architectural choices deserve attention.

**Local-first.** All code runs on your machine. Nothing in your codebase is transmitted to xAI's servers during a working session. Grok Build is also air-gap compatible, meaning it can operate in offline environments once initial setup is complete. For developers working on sensitive codebases — financial services, government, healthcare — this is a significant differentiator. Most SaaS coding tools require uploading your code to a cloud runtime to function.

**MCP compatibility.** Grok Build works with MCP servers out of the box without additional setup. If you've already configured MCP servers for use with Claude Code — external tools, databases, APIs connected via the Model Context Protocol — those connections transfer to Grok Build without reconfiguration. xAI framed this directly as a zero-friction migration path for developers already inside the Claude Code ecosystem.

This is a meaningful positioning choice. Rather than asking developers to rebuild their tooling, xAI adopted the same integration standard Anthropic established. The implication: Grok Build is designed to coexist with, and eventually compete for, the developer infrastructure that Claude Code built.

---

## Pricing and Access

Grok Build is available exclusively to SuperGrok Heavy subscribers. Standard pricing for that tier is $299 per month. For the first six months, xAI is offering an introductory price of $99 per month — a 67% discount intended to pull developers away from Claude Code ($20/month for Claude.ai Pro, or usage-based API access) and Codex CLI (included with ChatGPT Plus at $20/month).

For API access, Grok Build 0.1 is priced at $0.20 per million input tokens and $1.50 per million output tokens. At comparable task volumes, this is competitive with Claude and Codex pricing, though actual costs depend heavily on how many tokens a given task generates — and parallel sub-agents can compound token usage quickly if multiple agents are actively reasoning at the same time.

Elon Musk personally solicited developer feedback on X at launch, which suggests xAI is treating Grok Build as a high-priority product with a fast iteration cycle — both a positive signal about commitment and a realistic description of how early this beta actually is.

---

## Where Grok Build Stands Today

Grok Build enters the market with a clear architectural story — parallelism, local-first, MCP compatibility — and one significant weakness: its foundational model scores 17 points below its main competitors on the industry's standard coding benchmark.

That gap may narrow quickly. Grok 5 — xAI's next flagship model, with 6 trillion parameters and a 1.5 million token context window — is expected to ship in May or June 2026. Once Grok 5 powers Grok Build, the SWE-Bench gap is likely to close substantially. The architecture would remain the same; the model underneath would be considerably more capable.

The honest assessment for today: Grok Build 0.1 is a well-thought-out product in early beta. Plan mode and local-first architecture are solid foundations. The parallel sub-agents are a genuine differentiator for large codebases, even if the SWE-Bench number doesn't reflect it. Arena Mode, when it ships, could make the tool competitive even against more capable underlying models by selecting the best output rather than committing to the first.

What Grok Build is not, today, is a replacement for Claude Code or Codex CLI on raw coding performance. It is a competitive option for developers who value privacy (local-first), parallel execution on large projects, or who want to diversify beyond a single coding agent.

---

## Rating: 3 / 5

**What's working:** Parallel sub-agents with branch isolation, plan mode, local-first/air-gap architecture, MCP compatibility, clear roadmap (Arena Mode, Grok 5 upgrade).

**What's missing:** SWE-Bench 70.8% trails Claude Code and Codex CLI by ~17 points. Arena Mode not yet live. $99–$299/month is a high floor compared to $20/month competitors. Grok 5 would change the picture substantially — re-evaluate after Grok 5 integration.

---

*Related reading: [Claude Code and Anthropic's First Profit Quarter](/reviews/anthropic-first-profit-q2-2026-claude-code-spacex-colossus-deal/) · [OpenAI Codex Cloud Review](/reviews/openai-codex-cloud-agentic-coding-platform-review/) · [OpenAI Daybreak: Codex Security](/reviews/openai-daybreak-gpt-5-5-cyber-codex-security-cybersecurity-review/)*

