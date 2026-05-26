# Four Agentic Coding CLIs in Twelve Months: What the Terminal Race Means for Builders

> Claude Code launched in May 2025. Codex CLI in January 2026. Antigravity CLI and Grok Build both in May 2026. In twelve months, every major AI lab shipped a terminal agent. Here's what that convergence reveals — and what it means for your stack.


Twelve months ago, there was one serious agentic coding CLI.

Today there are four. All from the top AI labs. All shipping within the same 12-month window. All targeting the same developer.

That convergence is worth pausing on.

---

## The Four

**Claude Code** (Anthropic) — shipped May 2025 as an early preview; went broadly available in late 2025. Built around the principle of a coding agent that runs in your terminal, reads your full repo, edits files, runs commands, and operates in long multi-step sessions. Subscription model tied to Claude Max ($100/mo). Agent SDK billing split coming June 15, 2026.

**Codex CLI** (OpenAI) — January 2026, open-sourced under MIT license, built on codex-1. Subsequently merged into Codex Cloud, which runs agents server-side and lets them operate while your laptop is closed. Locked Use (agents working while your Mac screen is locked) shipped May 21, 2026. Pricing: $100–200/month real cost at the Pro tier.

**Antigravity CLI** (Google) — May 19, 2026 at I/O. A Go-based terminal tool rewritten from scratch, replacing the older Gemini CLI which Google is deprecating. Powered by Gemini 3.5 Flash at 289 tokens/second. Part of the Antigravity 2.0 platform alongside a desktop app and SDK. Native voice command support. Pricing: included in Google AI Pro ($20/mo) or AI Ultra ($100–200/mo).

**Grok Build** (xAI) — May 14, 2026, currently in early beta. Plan mode, up to 8 parallel subagents, each running in its own Git worktree. Powered by Grok 4.3 (16-agent Heavy architecture, 2M token context). Access gated to SuperGrok Heavy subscribers: $99/mo introductory, $300/mo list price after six months.

---

## What Converged — and What Didn't

The four tools share a surface: terminal-native, repo-aware, multi-file editing, shell command execution. That much is now table stakes.

Where they diverge is in execution model and pricing philosophy.

**Where the agent runs:**

Claude Code and Antigravity are primarily local — the agent process runs on your machine, hits the API for model calls, and executes shell commands with your local permissions. The security boundary is your machine.

Codex Cloud is primarily cloud-side — agents run in OpenAI's sandboxed VMs, not on your machine. Your Mac triggers and monitors the work; the execution happens on OpenAI's infrastructure. Locked Use is essentially a remote control for those cloud agents.

Grok Build is a hybrid — the CLI runs locally, but the parallel subagent architecture (each agent in its own Git worktree) is closer to Codex Cloud's philosophy of fanning work out rather than running everything in a single context.

**Parallelism:**

Grok Build's worktree-isolation model is the most explicit about parallelism. Each of up to 8 subagents works in its own branch, with mergeable output. Codex Cloud supports parallel tasks across multiple active sessions. Claude Code's [routines](/reviews/roots-dogfooding-ai-agent-builds-its-own-coordination-api/) are more sequential by default, though the Agent SDK supports parallel invocations. Antigravity's desktop app explicitly supports "orchestrate multiple agents simultaneously" but the CLI documentation is less specific.

**Pricing reality:**

| CLI | Cheapest entry | Real cost for active developer |
|---|---|---|
| Claude Code | $20/mo (Max) | $100/mo (heavy usage) |
| Codex CLI | Free (open source) | $100–200/mo (Pro cloud) |
| Antigravity CLI | $20/mo (AI Pro) | $100–200/mo (AI Ultra) |
| Grok Build | $99/mo (SuperGrok Heavy) | $99–300/mo |

The floor pricing varies; the ceiling doesn't. All four tools cost roughly the same for heavy use. That is not an accident — it reflects each company's read on what enterprise developers will pay for a productivity multiplier.

---

## What the Race Reveals About Strategy

Each company brought different instincts to the terminal.

**OpenAI** bet on cloud execution and ambient operation. Codex Cloud is the expression of OpenAI's belief that the valuable thing is not the local CLI but the infrastructure layer — agents that run server-side, operate asynchronously, and report back to your phone. The open-source CLI is table stakes; the platform is the play.

**Google** bet on speed and ubiquity. Antigravity CLI is Go-native, fast, and plugs into an ecosystem Google is already shipping to billions of users (AI Mode, Gemini 3.5 Flash, Google Workspace). The Go rewrite signals that Google is building for developer credibility — the Gemini CLI was a prototype; Antigravity CLI is the real thing.

**xAI** bet on raw context and parallelism. Grok 4.3's 2 million token context window — the largest among Western closed models at launch — means Grok Build can hold more of your codebase in a single pass than any competing tool. The worktree-isolation architecture is a different answer to the "how do you handle large codebases?" question than the sliding window approaches everyone else uses.

**Anthropic** bet on reasoning depth and a growing automation ecosystem. Claude Code's strength is handling ambiguous, multi-step problems that require judgment about trade-offs — the kind of work that trips up faster but shallower agents. The June 15 Agent SDK billing split signals that Anthropic sees Claude Code as infrastructure, not just a developer tool: the same model that you use interactively is the one your CI pipeline calls autonomously.

---

## The MCP Variable

One development cuts across all four tools: Model Context Protocol.

Claude Code was MCP-native from the start. Antigravity 2.0 ships with MCP client support built in. Grok Build includes Bring Your Own MCP support as a first-class feature. Codex CLI integrates with the broader Codex plugin marketplace, which is MCP-compatible.

For builders, this matters. It means a tool configuration — a custom MCP server connecting your agent to your database, your issue tracker, your deployment pipeline — is potentially portable across agents. The workhorse MCP server you build for Claude Code today can, in principle, plug into Antigravity or Grok Build.

"In principle" is doing some work in that sentence. Each agent still has different tool execution semantics, context window behavior, and approval modes. MCP reduces fragmentation; it doesn't eliminate it. But compared to a world where every agent required proprietary plugins, the interoperability outlook is better than it looked six months ago.

---

## The Lock-in Calculus

The four-way race creates a problem for builders who want to pick a winner: the tools are differentiated enough that your choice has architectural implications, but converging fast enough that today's differentiator might be table stakes by Q3.

Some heuristics:

**If you're building for cloud-native, async workflows**, Codex Cloud's server-side execution model fits better than local-first tools. You accept OpenAI's security boundary; you gain ambient operation.

**If you're operating primarily in Google's ecosystem** (Cloud, Workspace, Firebase), Antigravity's integration depth is real. The AI Studio → Cloud Run → Firebase pipeline that Google demoed at I/O is genuinely tighter than anything the other tools can offer on Google infra.

**If your codebase is large and your tasks are parallelizable**, Grok Build's worktree architecture is worth the $99/mo premium over the alternatives. Eight isolated agents working in parallel on the same repo is a qualitatively different capability.

**If you need reasoning depth for ambiguous problems**, Claude Code's benchmark lead on complex multi-step tasks is still real as of May 2026. The [Gartner Magic Quadrant for enterprise AI coding agents](/reviews/gartner-magic-quadrant-2026-enterprise-ai-coding-agents-github-copilot-openai-codex-cursor/) released this year placed Claude Code highest for Ability to Execute in enterprise deployments.

None of these recommendations will survive until 2027 without revision. That's the nature of the race.

---

## What the Convergence Means

Twelve months ago, an agentic coding CLI was an Anthropic-specific experiment. Today it is table stakes at every major lab.

The competitive intensity is good for developers in the short term: prices are held down, features are advancing fast, and the MCP interoperability layer gives builders more leverage over vendor choice than they had in 2025.

The risk is in the velocity itself. The tools are advancing faster than the best practices for using them. How do you structure a codebase for multi-agent parallel editing? When does an autonomous agent session require human review, and when can it run unattended? What does "sufficient test coverage" mean when the agent writes and runs the tests? These questions don't have settled answers yet.

The companies building the CLIs are also building the answers. Builders who stay close to the tooling — not just using it but watching how the architectures evolve — will be better positioned when those answers stabilize.

The terminal is contested real estate now. That's a good problem to have.

---

*Related: [AI Coding Assistants Compared 2026](/guides/ai-coding-assistants-compared/), [Grok Build: xAI's Agentic CLI](/builders-log/xai-grok-build-x-subscriber-developer-distribution/), [Google I/O 2026 Was a System Reveal](/builders-log/google-io-2026-agent-stack/), [Roots: AI Agent Builds Its Own Coordination API](/builders-log/roots-dogfooding-ai-agent-builds-its-own-coordination-api/)*

