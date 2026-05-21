---
title: "When Anthropic Becomes Your Entire Agent Stack"
date: 2026-05-22
description: "Three features shipped May 6 — Dreaming, Outcomes, Multiagent Orchestration — and together they don't just improve Claude Managed Agents. They replace the infrastructure most teams have been building themselves for 18 months. That's worth being intentional about."
content_type: "Builder's Log"
categories: ["Agent Infrastructure", "Anthropic", "Industry Analysis"]
tags: ["anthropic", "managed-agents", "claude", "vendor-lock-in", "agent-architecture", "dreaming", "orchestration", "enterprise-ai", "analysis"]
---

On May 6, 2026, Anthropic shipped three features for Claude Managed Agents: Dreaming (research preview), Outcomes (public beta), and Multiagent Orchestration (public beta). The coverage called them "new capabilities." That framing is technically correct and practically misleading.

These are not new capabilities bolted onto an existing product. They are the scaffolding most teams building production agents have been assembling themselves — now offered as managed infrastructure. If you are a builder who has been doing that assembling, you need to decide whether to migrate. If you are a builder who hasn't started yet, you need to decide whether to start inside Anthropic's stack or outside it.

That decision has a long tail.

## What Each Feature Actually Replaces

### Dreaming → Your Memory Layer

Dreaming is a scheduled background process that reviews an agent's past sessions, removes duplicates, surfaces patterns, and rewrites the memory store before the next session begins. You configure how much autonomy it has — automatic rewrites or reviewed-before-applied. Harvey, the legal AI company, reported roughly a 6x jump in task completion rates after enabling it.

What it replaces: the session memory systems teams have been building on top of vector stores, Redis, and third-party tools like Mem0 or Zep. The pattern — persist context, consolidate it periodically, surface relevant chunks at session start — is well-understood. Dreaming is that pattern, managed by Anthropic, locked inside the Claude Managed Agents runtime.

### Outcomes → Your Eval Layer

Outcomes spawns a separate grader agent that reads only the final output and a rubric you define, then either passes the work or returns a specific list of fixes for the original agent to address. Anthropic reported up to 10 percentage points of task success improvement in internal testing. Wisedocs is reviewing medical documents 50% faster with it enabled.

What it replaces: the eval frameworks teams have been wiring up — LangSmith, Braintrust, custom grader prompts, human-in-the-loop review pipelines. Automated evaluation of agent output is a solved problem at the architecture level. The hard part is doing it well at your specific task. Outcomes makes the architecture disappear; you define the rubric, Anthropic runs the machinery.

### Multiagent Orchestration → Your Agent Topology

Multiagent Orchestration lets a lead agent delegate to up to 20 specialist subagents (25 concurrent threads) running in parallel on a shared filesystem. Each specialist is individually traceable in the Claude Console. The topology — lead agent decomposes work, specialists execute in parallel, lead synthesizes — is the architecture most production multi-agent systems have converged on.

What it replaces: LangGraph, CrewAI, custom orchestration layers, and the boilerplate that comes with each. The model is familiar. The managed version means Anthropic handles the scheduling, tracing, and state management.

## The Pattern

Three features, three infrastructure layers, one platform. Anthropic did not invent session memory, automated evaluation, or multi-agent orchestration. These patterns predate Managed Agents by months. What Anthropic did is bundle them, maintain them, and make them available without the setup cost — in exchange for your agents living inside Claude Managed Agents.

That is the deal. The results are real (Harvey's 6x is not a projection), the convenience is real, and the dependency is real.

## What You Are Actually Deciding

Building on Managed Agents is not a technical choice. It is a strategic one. Here is what you are signing up for:

**Session data lives in Anthropic's database.** Your agents' memory — the accumulated context that makes them more useful over time — is stored in a system you do not control. Anthropic's terms govern how it is retained, exported, and deleted.

**The orchestration API is proprietary.** Multiagent topologies built on the Managed Agents runtime cannot be ported to another platform without rebuilding the coordination logic. Unlike MCP (which is an open protocol), the orchestration layer is specific to Claude.

**The eval framework is coupled to the model.** Outcomes grades outputs using a Claude grader. If you move to a different model or platform, you rebuild the evaluation infrastructure too.

**You are betting on Anthropic's roadmap.** Every layer you adopt is a layer that has to evolve correctly. Pricing changes, deprecations, rate limit adjustments, and feature regressions all affect your system. You have influence as a customer; you do not have control.

None of this is unusual for a managed platform. AWS, Salesforce, and Vercel all operate on the same logic. The question is whether you have made the decision deliberately.

## Context: This Is Not an Isolated Move

Managed Agents is one part of a broader Anthropic expansion. In the same week that Dreaming shipped, Anthropic announced a [$1.5 billion joint venture with Blackstone, Goldman Sachs, and Hellman & Friedman](/builders-log/anthropic-consulting-jv-blackstone-goldman/) to embed Claude inside PE portfolio companies as a consulting entity, and launched new verticals — [Claude for Legal](/reviews/claude-for-legal-review/) and [Claude for Financial Services](/reviews/claude-for-financial-services-review/) — with connectors, templates, and managed workflows specific to those domains.

The pattern across all three: Anthropic moving from API access to stack ownership. API layer → vertical product layer → orchestration and memory layer → consulting layer. Each move is independent. Together they describe a company that is expanding what it owns in the AI value chain.

That context matters for how you read the Managed Agents features. Dreaming, Outcomes, and Orchestration are good features. They are also a signal about where Anthropic intends to be positioned relative to the rest of the agent infrastructure market.

## What the Right Call Is

There is no universal answer. But the question has structure.

**Prototype or internal tool:** Build on Managed Agents. The setup cost savings are real and the time-to-working-agent is genuinely faster. If you are exploring whether a use case is viable, you should not be building custom memory and eval infrastructure.

**Product you will maintain for three or more years:** Understand your exit before you commit. What would it take to move off Managed Agents in 18 months? Which layers are portable (your prompts, your rubrics, your domain logic) and which are not (orchestration topology, memory format, eval grader coupling)? Design around the portable layers. Do not let the non-portable layers become load-bearing without knowing it.

**Enterprise deployment with existing AI infrastructure:** Negotiate data portability in your contract before you sign. What format can your session data be exported in? What is the retention and deletion policy? What SLA applies to the memory and eval infrastructure, not just the model API? These questions are easier to ask before you have production data in the system.

**Developer or researcher building on open infrastructure:** Build outside Managed Agents and treat the managed versions as a benchmark for what your stack should eventually do. LangGraph, Mem0, LangSmith, and CrewAI exist. They are more work. They are also yours.

## One More Thing

This is worth saying plainly: the 6x task completion improvement at Harvey is real. The 50% faster document review at Wisedocs is real. Managed Agents with Dreaming and Outcomes switched on produces meaningfully better results than a raw agent loop. The platform works.

The question is not whether to use it. The question is whether you have thought through what you are committing to. Most teams that end up locked into a platform do not decide to accept lock-in — they just never make the explicit decision.

Now is a reasonable time to make it.
