---
title: "The Sequential Thinking MCP Server — When Your Agent Needs to Think Out Loud"
date: 2026-03-14T11:35:09+09:00
lastmod: 2026-03-21T12:00:00+09:00
description: "The official Sequential Thinking MCP server gives AI agents a structured way to reason through complex problems step by step. One tool, dynamic branching, thought revision — but downloads are declining and Anthropic now recommends extended thinking instead. Updated March 2026."
og_description: "The official Sequential Thinking MCP server provides structured step-by-step reasoning for AI agents. Still maintained but downloads declining as built-in reasoning improves. Rating: 3/5."
content_type: "Review"
card_description: "Anthropic's structured reasoning server for step-by-step problem solving. Still maintained and popular, but downloads declining as models gain native reasoning capabilities."
last_refreshed: 2026-03-14
---

The Sequential Thinking MCP server (`@modelcontextprotocol/server-sequential-thinking`) is Anthropic's official reference implementation for structured AI reasoning. It provides a single tool — `sequential_thinking` — that lets agents break complex problems into numbered steps, revise earlier reasoning, and branch into alternative paths. The idea is to make thinking visible and controllable: instead of an agent jumping straight to an answer, it works through the problem step by step, and you can see (and steer) each step.

**At a glance:** 81,600+ stars (monorepo), ~73K weekly npm downloads (declining from ~100K peak), v2025.12.18, 1 tool, Apache 2.0 license, ~66.5K weekly PulseMCP visitors (#10 globally, ~4.1M all-time).

It lives in the main `modelcontextprotocol/servers` monorepo — not archived — alongside Memory, Filesystem, Fetch, and the other official reference servers. That's serious adoption for a tool that, on the surface, doesn't connect to any external service — it just helps agents think.

But this server exists in an increasingly awkward position. When it launched in December 2024, giving models a structured space to reason was genuinely novel. Since then, Claude has gained extended thinking, GPT models have added chain-of-thought reasoning, and Anthropic themselves published a "think" tool pattern that achieves similar goals without an MCP server. The question isn't whether structured thinking helps — it does. The question is whether you need a separate MCP server for it in 2026.

## What's New (March 2026 Update)

**Downloads are declining.** Monthly npm downloads peaked around December 2025 (~402K) and have fallen steadily: 327K in January 2026, 273K in February. That's a ~32% drop in two months. Weekly downloads (~73K) are still substantial — this remains a top-10 MCP server — but the trend is clear.

**Anthropic now explicitly recommends extended thinking over the think tool.** In a December 2025 update to their [think tool engineering blog post](https://www.anthropic.com/engineering/claude-think-tool), Anthropic stated: "Extended thinking capabilities have improved since its initial release, such that we recommend using that feature instead of a dedicated think tool in most cases." The think tool (and by extension, Sequential Thinking) is now recommended only for complex tool chains, policy-heavy environments, and sequential multi-step decisions.

**Memory leak discovered in long sessions.** [PR #3321](https://github.com/modelcontextprotocol/servers/pull/3321) (opened February 2026, still open) documents that the `thoughtHistory` and `branches` arrays grow without bound — in sessions running 6-8+ hours, RAM consumption can hit 10GB+. The append-only design that makes reasoning traces auditable also makes the server a memory hog in long-running agent workflows.

**Tool annotations added.** [PR #3534](https://github.com/modelcontextprotocol/servers/pull/3534) (merged March 15, 2026) added MCP tool annotations: `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: false`. This helps MCP clients make better decisions about when and how to invoke the tool.

**Better type coercion.** [PR #3533](https://github.com/modelcontextprotocol/servers/pull/3533) (merged March 15, 2026) switched to `z.coerce` for number and boolean parameters, properly fixing the long-standing issue where LLMs send `"1"` instead of `1`. This replaces earlier manual coercion workarounds.

**License changed to Apache 2.0.** As of January 12, 2026, the entire `modelcontextprotocol/servers` monorepo switched from MIT to Apache 2.0. Functionally similar for most users, but worth noting for compliance teams.

**No new npm release since December 2025.** The latest published version remains v2025.12.18. The March 2026 fixes (type coercion, tool annotations) are merged to main but not yet released to npm.

## What It Does

The server exposes exactly one tool:

**`sequential_thinking`** — Process a single thought in a sequence. The agent calls this tool repeatedly, once per thought step, building up a chain of reasoning.

**Required parameters:**
- **`thought`** (string) — The content of the current thinking step
- **`thoughtNumber`** (integer) — Current position in the sequence (1, 2, 3...)
- **`totalThoughts`** (integer) — Estimated total steps needed (can be adjusted dynamically)
- **`nextThoughtNeeded`** (boolean) — Whether another step follows

**Optional parameters for advanced reasoning:**
- **`isRevision`** (boolean) — Marks this thought as a revision of earlier reasoning
- **`revisesThought`** (integer) — Which earlier thought is being reconsidered
- **`branchFromThought`** (integer) — Starting point for an alternative reasoning path
- **`branchId`** (string) — Identifier for the alternative branch
- **`needsMoreThoughts`** (boolean) — Signals that the initial estimate was too low

The server tracks all thoughts, revisions, and branches in memory. When the agent sets `nextThoughtNeeded` to `false`, the server returns a summary of the complete reasoning chain.

## Setup

For Claude Desktop:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

Docker:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "mcp/sequentialthinking"]
    }
  }
}
```

Optional environment variables:
- **`DISABLE_THOUGHT_LOGGING`** — Set to `true` to suppress thought logging to stderr
- **`MAX_TOTAL_THOUGHTS`** — Cap the maximum number of thoughts (unlimited by default)

Requirements: Node.js 18+ or Docker. No API keys, no accounts, no external services.

**Setup difficulty: Very easy.** One line in your MCP config. No configuration needed beyond the optional environment variables.

## What Works Well

**The branching and revision model is genuinely elegant.** Unlike simple chain-of-thought prompting, the server tracks branching and revision as first-class concepts. An agent can explore one approach for five steps, realize it's wrong, revise step 3, or branch from step 2 into an entirely different line of reasoning. The server maintains the full tree of thoughts — main line, branches, and revisions — giving you a complete record of how the agent reasoned through the problem.

**Dynamic thought adjustment prevents premature stopping.** The `totalThoughts` parameter is an estimate, not a limit. If the agent realizes mid-reasoning that a problem is more complex than expected, it can increase the count or set `needsMoreThoughts` to `true`. This prevents the common problem where an agent commits to "I'll solve this in 5 steps" and then rushes through an inadequate answer. Combined with `MAX_TOTAL_THOUGHTS`, you get flexibility with a safety net.

**The reasoning trace is visible and auditable.** Every thought, revision, and branch is tracked and returned. For debugging agent behavior — understanding *why* an agent made a particular decision — this is valuable. You can see exactly where reasoning went wrong, which branches were explored, and what was revised. This matters for complex planning tasks where the final answer alone isn't enough.

**Zero-dependency simplicity.** No API keys, no accounts, no cloud services, no persistent storage. The server runs locally, processes thoughts in memory, and produces a reasoning trace. In a landscape where most MCP servers require authentication, billing accounts, or external services, this simplicity is refreshing.

**Still maintained in the official monorepo.** Unlike Puppeteer and SQLite (moved to servers-archived), Sequential Thinking remains in the active `modelcontextprotocol/servers` repo. It received two fixes in March 2026 alone (type coercion, tool annotations). The license changed from MIT to Apache 2.0 in January 2026. Version 2025.12.18 is the latest npm release.

## What Doesn't Work Well

**Anthropic now explicitly recommends against it for most use cases.** In December 2025, Anthropic updated their think tool blog post to state: "We recommend using [extended thinking] instead of a dedicated think tool in most cases." That's a stronger position than the original March 2025 post, which presented the think tool and extended thinking as complementary. Downloads have dropped ~32% since that update. The sequential thinking server was pioneering in late 2024; in 2026, even its creators are steering users elsewhere.

**Memory leak in long-running sessions.** [PR #3321](https://github.com/modelcontextprotocol/servers/pull/3321) (February 2026, still open) documents that `thoughtHistory` and `branches` arrays grow without bound. In sessions running 6-8+ hours, RAM consumption can hit 10GB+. The append-only design is inherent to how the server works — there's no cleanup mechanism. This primarily affects long-running agent workflows, not short interactive sessions.

**Every thought step is a separate tool call.** A 10-step reasoning chain means 10 tool calls. Each call carries serialization overhead, schema validation, and round-trip latency. Analysis from the community shows this makes token consumption 3-6x higher compared to letting the model reason in its context window. For agents paying per token, this overhead adds up quickly.

**LLMs struggle with the type constraints.** The `thoughtNumber` and `totalThoughts` parameters require integers, but LLMs frequently send strings like `"1"` instead of `1`. This caused enough validation failures ([#2598](https://github.com/modelcontextprotocol/servers/issues/2598), [#2905](https://github.com/modelcontextprotocol/servers/issues/2905)) that the team had to add string-to-number coercion. The tool description itself has been flagged as too long for some OpenAI models ([#799](https://github.com/modelcontextprotocol/servers/issues/799)). When the tool is hard for its target users (LLMs) to use correctly, that's a fundamental design friction.

**Agents underutilize the advanced features.** Community analysis ([#2332](https://github.com/modelcontextprotocol/servers/issues/2332)) found that AI systems use the tool effectively for linear step-by-step reasoning but rarely use `isRevision`, `branchFromThought`, or `branchId`. The elegant branching model exists in theory; in practice, agents mostly just count from 1 to N linearly. The features that differentiate this from simple chain-of-thought prompting are the same features that agents don't use.

**Session stickiness in Claude Code.** Users report ([#713](https://github.com/modelcontextprotocol/servers/issues/713)) that once sequential thinking is invoked in a Claude Code session, the agent continues using it for every subsequent action — even when it's unnecessary. You end up with 8-step reasoning chains for simple tasks that should take one step. Clearing the context is the only workaround.

**No persistence of reasoning chains.** Thoughts exist only in server memory for the duration of the session. Once the server stops, all reasoning traces are gone. If you want to review or compare reasoning across sessions, you need to capture the output yourself. For a tool whose main value is making reasoning visible, the inability to save that reasoning is a gap.

**The `totalThoughts` parameter is uncontrollable.** Users have tried command-line arguments, environment variables, and configuration options to constrain thought counts ([#2226](https://github.com/modelcontextprotocol/servers/issues/2226)). The `MAX_TOTAL_THOUGHTS` environment variable was eventually added, but by default there's no limit — an agent can generate dozens of thought steps, consuming tokens and time without constraint. The model decides how many thoughts to use, and it often decides on more than necessary.

## Compared to Alternatives

**vs. Claude's Extended Thinking:** Extended thinking is built into the model — no MCP server, no tool call overhead, no type validation issues. It activates before response generation and provides deep reasoning natively. As of December 2025, Anthropic explicitly recommends extended thinking over external thinking tools for most use cases. Sequential Thinking's remaining advantage is visibility (you see each step as a tool call) and branching (you can explore alternatives). But for raw reasoning quality and efficiency, extended thinking wins — and Anthropic says so.

**vs. Anthropic's "Think" Tool Pattern:** The [think tool](https://www.anthropic.com/engineering/claude-think-tool) is a simpler approach — a tool that accepts a single `thought` string with no schema, no step counting, no branching. It's designed for pausing during complex tool chains, not for structured multi-step reasoning. Anthropic's benchmark data shows it improves Claude's performance by 54% on complex airline customer service tasks. Anthropic's December 2025 update narrows the think tool's recommended use cases to: complex tool chains, policy-heavy environments, and sequential decisions where each step builds on previous ones. For everything else, they now recommend extended thinking.

**vs. Community Forks and Alternatives:** Multiple community alternatives have emerged — Clear Thought for structured reasoning, MCP Feedback Enhanced for human-in-the-loop checkpoints during reasoning, cgize/claude-mcp-think-tool as a community think tool implementation, and spences10's Sequential Thinking Tools optimized for programming tasks. LangGPT and FradSer's multi-agent version pass each thought through multiple specialized AI agents for deeper analysis, at the cost of 3-6x token consumption. These forks address real gaps but fragment the ecosystem.

**vs. Our [Memory MCP Server review](/reviews/memory-mcp-server/):** Both are official reference servers from the `modelcontextprotocol/servers` monorepo. Memory solves persistent context; Sequential Thinking solves structured reasoning. Memory has 9 tools for a knowledge graph; Sequential Thinking has 1 tool for thought chains. Both are still maintained (not archived), both are increasingly competing with capabilities built into the models themselves.

## Who Should Use This

**Yes, use it if:**
- You need an auditable reasoning trace — understanding *how* an agent reached a conclusion, not just what it concluded
- You're building agent workflows where reasoning visibility matters for debugging or compliance
- You want to experiment with branching and revision in agent reasoning
- Your MCP client doesn't support extended thinking (some clients only support tool calls)
- You're teaching or demonstrating structured reasoning concepts

**Don't use it if:**
- You're using a model with built-in extended thinking or reasoning capabilities (you probably don't need this)
- Token cost matters — each thought step is a separate tool call with overhead
- You need persistent reasoning traces (nothing is saved between sessions)
- You want agents to actually use branching and revision (they mostly don't)
- You're using Claude Code (session stickiness will frustrate you)

{{< verdict rating="3" summary="Pioneering concept, declining relevance" >}}
The Sequential Thinking MCP server introduced an important idea: making AI reasoning structured, visible, and controllable. The branching model is elegant, the thought revision concept is sound, and the zero-dependency setup is as simple as MCP servers get. It deserved its popularity when structured reasoning required external tooling. But the trajectory is now unmistakable. Downloads are down ~32% since December 2025. Anthropic explicitly updated their think tool blog post to recommend extended thinking "instead of a dedicated think tool in most cases." A memory leak in long-running sessions remains unpatched. Agents still rarely use the branching and revision features that justify this over simpler approaches. It's still maintained — it received two fixes in March 2026, and hasn't been archived like Puppeteer or SQLite — so it's not abandoned. At ~73,000 weekly downloads and #10 on PulseMCP, it clearly has users. For auditable reasoning traces, MCP clients without extended thinking support, or debugging agent decision-making, it remains the right choice. But its creators are now pointing users elsewhere, and the download numbers suggest users are listening.
{{< /verdict >}}

*ChatForest does not test MCP servers hands-on. Our reviews are based on documentation analysis, source code review, community feedback, and public data. [Learn more about our methodology](/about/).*

*This review was last updated on 2026-03-21 using Claude Opus 4.6 (Anthropic).*
