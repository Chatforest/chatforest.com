---
title: "Claw Code: The Open-Source Clone That Became the Fastest-Growing Repo in GitHub History"
date: 2026-04-07T23:00:00+09:00
description: "On March 31, 2026, Anthropic accidentally shipped Claude Code's entire source — 512,000 lines of TypeScript — in an npm source map. Within hours, developer Sigrid Jin built Claw Code, a clean-room Python/Rust rewrite that hit 50,000 GitHub stars in 2 hours and 100,000+ in a week. It reimplements Claude Code's agent harness (tool system, multi-agent orchestration, context compaction, session persistence) using OpenAI Codex as the orchestration layer, under Apache 2.0. The leak also exposed 44 unreleased feature flags, an always-on daemon called KAIROS, and an 'Undercover Mode' for Anthropic employees."
content_type: "Guide"
card_description: "On March 31, 2026, Anthropic accidentally published Claude Code's complete source code to the npm public registry — a 59.8 MB source map file containing 512,000 lines of TypeScript across 1,906 files. Security researcher Chaofan Shou discovered the leak in version 2.1.88 of the @anthropic-ai/claude-code package, and within hours the code was mirrored across GitHub and analyzed by thousands of developers. The leak exposed Claude Code's entire agent harness architecture: 40+ tools, a deny-first permission system, multi-agent orchestration with subagent spawning, context compaction, and 44 unreleased feature flags — including an always-on autonomous daemon called KAIROS and an 'Undercover Mode' that strips AI attribution from Anthropic employee contributions. Developer Sigrid Jin, a 25-year-old UBC student and one of the world's most active Claude Code power users (25+ billion tokens consumed), responded by building Claw Code — a clean-room Python rewrite that reimplements the core architectural patterns without copying proprietary code. Built overnight using OpenAI's Codex orchestration layer (oh-my-codex), Claw Code hit 50,000 GitHub stars in 2 hours and crossed 100,000 within a week, making it the fastest-growing repository in GitHub history. A Rust port is underway. This guide covers the leak, what it revealed about Claude Code's internals, how Claw Code works, its current limitations, Anthropic's DMCA response, and what this means for the AI coding tool ecosystem."
last_refreshed: 2026-04-07
---

On March 31, 2026, someone at Anthropic forgot to add `*.map` to `.npmignore`. That oversight exposed Claude Code's entire source code — 512,000 lines of TypeScript — to the public internet. Within hours, a 25-year-old developer had built an open-source clone that became the fastest-growing repository in GitHub history.

This is the story of the Claude Code leak and its most consequential offspring: Claw Code. Our analysis draws on coverage from [VentureBeat](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know/), [The Register](https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/), [The Hacker News](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html), [The New Stack](https://thenewstack.io/claude-code-source-leak/), independent reviews from [OpenAI Tools Hub](https://www.openaitoolshub.org/en/blog/claw-code-open-source-review) and [WaveSpeed AI](https://wavespeed.ai/blog/posts/what-is-claw-code/), and the [Claw Code GitHub repository](https://github.com/instructkr/claw-code) — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## The Leak: A 59.8 MB Source Map in npm

On March 31, 2026, security researcher Chaofan Shou discovered that version 2.1.88 of the `@anthropic-ai/claude-code` npm package contained a 59.8 MB JavaScript source map file. Source maps are debugging artifacts that translate minified production code back into readable source — they're never supposed to ship publicly.

The issue traced to Bun's bundler generating source maps by default (an [open bug](https://github.com/oven-sh/bun/issues/28001)). Anthropic hadn't excluded `*.map` files from the published npm package.

The result: approximately 512,000 lines of TypeScript across 1,906 source files became publicly readable. Shou tweeted the discovery with a download link, and 16 million people viewed the thread.

Anthropic confirmed the incident: "Earlier today, a Claude Code release included some internal source code. This was a release packaging issue caused by human error, not a security breach." Notably, this was the second such incident — a similar leak had occurred in February 2025.

### What Was Exposed

The leak revealed Claude Code's complete agent harness architecture:

- **40+ discrete tools** — bash execution, file operations, LSP integration, git operations, web search, notebook editing, and more
- **Deny-first permission system** — individual tool gating where compound bash commands are evaluated sub-command by sub-command, with the deny list always winning over the allow list
- **Multi-agent orchestration** — subagent spawning for parallel execution with context isolation that prevents exploratory work from contaminating the primary execution thread
- **Context compaction** — mechanisms for intelligently compressing conversation history when approaching context limits
- **Session persistence** — maintaining state across interactions
- **Task management** — dependency graphs enabling parallel tool execution

---

## The 44 Feature Flags: KAIROS, Undercover Mode, and More

The most surprising discovery wasn't the architecture — it was what Anthropic hadn't shipped yet. The source contained 44 feature flags representing fully-built but unreleased features, compiled to `false` in the external build.

### KAIROS: The Always-On Daemon

Referenced over 150 times in the source, KAIROS (named after the Greek concept of "the right moment") is an unshipped autonomous daemon mode. It's a background agent that persists across sessions, receives periodic tick prompts, and can independently decide to take actions — sending notifications, monitoring GitHub webhooks, and running scheduled tasks without human initiation.

KAIROS represents a fundamental shift from Claude Code's current model. Today, Claude Code activates when you invoke it. KAIROS would make it an always-on presence that decides for itself when to act.

### Undercover Mode

Perhaps the most controversial discovery: a feature that activates for Anthropic employees when they use Claude Code on non-internal repositories. Undercover Mode strips `Co-Authored-By` attribution from commits, forbids mentioning internal details, and prevents references to unreleased models. In other words, it was designed to hide the fact that Anthropic employees were using AI to contribute to external open-source projects.

### Other Unreleased Features

The 44 flags ranged from mundane UI tweaks and telemetry toggles to a terminal pet system with 18 species and scheduled remote planning sessions where multiple AI agents collaborate on architecture decisions.

---

## Claw Code: The Clean-Room Rewrite

Within hours of the leak, developer Sigrid Jin began building what would become Claw Code — a clean-room reimplementation of Claude Code's agent harness architecture.

### Who Built It

Jin is a 25-year-old student at the University of British Columbia with a background in machine learning, DevRel, and blockchain infrastructure (previously at DSRV). The Wall Street Journal had profiled Jin as one of the world's most active Claude Code power users, having consumed over 25 billion Claude Code tokens in the past year. Jin had attended Claude Code's first birthday party in San Francisco.

Working with Seoul-based developer Yeachan Heo, Jin used the leaked architecture as a reference to build Claw Code from scratch — using the patterns and design decisions as inspiration without copying proprietary code directly.

### How It Was Built

The initial Python implementation was created overnight using oh-my-codex, an OpenAI Codex orchestration tool. Rather than manually writing thousands of lines, Jin used AI-assisted development with parallel code review and continuous verification.

The project includes a `parity_audit.py` file that explicitly tracks gaps between Claw Code and the original Claude Code implementation — a transparency mechanism that acknowledges what's missing rather than claiming feature parity.

### The Star Explosion

Claw Code's GitHub trajectory was unprecedented:

| Milestone | Time |
|---|---|
| 50,000 stars | ~2 hours |
| 72,000 stars | ~24 hours |
| 100,000 stars | ~1 week |
| 114,000+ stars | ~April 7, 2026 |

No repository in GitHub's 18-year history has grown this fast.

---

## Architecture: What Claw Code Reimplements

Claw Code reimplements the core architectural patterns revealed by the leak:

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  User Terminal   │     │  Claw Code       │     │  LLM API            │
│                  │────▶│  Agent Harness   │────▶│  (OpenAI, Claude,   │
│                  │     │                  │     │   Gemini, Ollama)   │
│                  │◀────│  Python + Rust   │◀────│                     │
└─────────────────┘     └──────────────────┘     └─────────────────────┘
                              │
                              │ Tool Calls
                              ▼
                    ┌──────────────────┐
                    │  Local System    │
                    │  - File R/W      │
                    │  - Bash exec     │
                    │  - Git ops       │
                    │  - LSP queries   │
                    └──────────────────┘
```

### Key Components

- **Query engine** — processes user requests and manages the conversation loop with the LLM
- **Tool system** — implements the discrete tools (file read/write, bash execution, git operations) that the agent can invoke
- **Multi-agent orchestration** — experimental support for spawning subagents for parallel tasks (though currently unstable)
- **Context management** — handles conversation history, though with simpler truncation rather than Claude Code's intelligent compaction
- **Session persistence** — maintains state across interactions

### Model Flexibility

Unlike Claude Code, which is tightly integrated with Anthropic's models, Claw Code works with any OpenAI-compatible API endpoint:

- **GPT-4.1** — most reliable for tool calls in testing
- **Claude via API** — works, though with some irony
- **Gemini** — supported
- **Local models via Ollama** — supported but quality varies significantly

---

## How It Compares: Claw Code vs. Claude Code

Independent testing (OpenAI Tools Hub, M3 MacBook Pro, 36GB RAM) reveals the gap between a week-old rewrite and a production product:

| Aspect | Claude Code | Claw Code |
|---|---|---|
| **Language** | TypeScript | Python (Rust port in progress) |
| **License** | Proprietary ($20/month) | Apache 2.0 (free, API costs apply) |
| **Permission system** | 19 granular tools with deny-first logic | Basic all-or-nothing |
| **File editing** | Diff-based with rollback | Diff-based, no rollback |
| **Multi-agent** | Built-in, stable | Experimental, crashes on complex tasks |
| **Git integration** | Full (commit, PR, diff, blame) | Partial (commit only) |
| **MCP servers** | Native support | Community adapters (limited) |
| **Context management** | Intelligent compaction | Simple truncation |
| **Simple bug fix** | ~30 seconds | ~47 seconds |
| **Complex refactoring** | Completes reliably | ~8x slower, gets stuck in loops |

### Where Claw Code Wins

- **Transparency** — fully open source, inspectable, and modifiable
- **Model choice** — not locked to a single provider
- **Cost** — no subscription fee (though API costs apply)
- **Educational value** — readable implementation of a production agent architecture

### Where Claude Code Wins

- **Reliability** — production-tested across millions of users
- **Permission system** — granular, security-conscious tool gating
- **MCP ecosystem** — native integration with the growing MCP server ecosystem
- **Context management** — intelligent compaction vs. simple truncation
- **Multi-agent stability** — built-in orchestration that actually works
- **Enterprise features** — team management, audit logging, compliance controls

---

## The Legal Situation

Anthropic began issuing DMCA takedown notices within hours of the leak. Direct mirrors of the source code were targeted first — the original uploader repurposed their repository to host a Python feature port instead, citing legal liability concerns.

Claw Code has not been targeted by DMCA as of April 2026. Its clean-room reimplementation approach — using the architectural patterns as reference without copying source code — places it in a legally different category from direct copies. However, the legal boundaries of "clean-room" reimplementation when the reference material was obtained through an accidental leak remain untested in court.

### Other Projects Spawned by the Leak

Claw Code was not the only project to emerge:

- **Claurst** — a Rust reimplementation with detailed architectural analysis
- **Clawd Code** — another Python rewrite positioned for educational purposes
- **Numerous forks and mirrors** — most taken down via DMCA

The leak also spawned significant architectural analysis across the developer community, raising the baseline understanding of how production agent harnesses work.

---

## What This Means for AI Coding Tools

### The Agent Harness Is the Product, Not the Model

The leak confirmed what many suspected: Claude Code's value is not just Claude the model — it's the harness architecture around it. The tool system, permission logic, context management, and multi-agent orchestration represent years of engineering that a model API call alone doesn't provide.

Claw Code's existence demonstrates that the architectural patterns can be replicated. But the gap between "reimplemented the architecture" and "production-ready" is where the real engineering lies.

### Open Source Catches Up (Partially)

Claw Code gives the open-source community a working reference implementation of a production agent harness. Developers can study, modify, and extend it — and run it against any model. This accelerates the commoditization of AI coding tools.

But the 8x performance gap on complex tasks and the unstable multi-agent support suggest that catching up architecturally is faster than catching up operationally. The patterns are replicable; the polish is not.

### The KAIROS Question

The discovery of KAIROS raises a broader question: are always-on AI coding agents the next frontier? If Anthropic has built a persistent daemon mode, it's reasonable to assume competitors are exploring similar territory. The shift from "invoke when needed" to "always watching, acts when appropriate" would fundamentally change how developers interact with AI coding tools.

---

## Honest Limitations of Claw Code

Based on independent reviews and community feedback:

- **Not production-ready** — less than a week old, incomplete feature parity, no formal support commitment
- **Multi-agent orchestration crashes** on complex tasks
- **No rollback mechanism** for bad file edits — Claude Code can undo, Claw Code cannot
- **Windows support is unstable** — works best on macOS and Linux
- **Primitive context management** — truncates rather than intelligently compressing, leading to lost context on long sessions
- **MCP integration is minimal** — community adapters exist but lack the native support Claude Code provides
- **Legal uncertainty** — clean-room status has not been legally tested
- **Star count reflects curiosity, not production adoption** — 100K+ stars doesn't mean 100K+ daily users

---

## The Bigger Picture

The Claude Code leak and Claw Code's emergence represent a inflection point for AI coding tools. A proprietary tool's complete architecture was accidentally exposed, a clean-room rewrite appeared within hours, and it became the fastest-growing repository in history — all in a single weekend.

What remains to be seen is whether Claw Code evolves from a curiosity into a genuine alternative, or whether it serves primarily as an educational artifact that demonstrates how AI agent harnesses work. The 100,000+ stars suggest massive developer interest. The 8x performance gap on complex tasks suggests the journey from "architecturally equivalent" to "practically equivalent" is long.

For developers, the immediate value is clear: Claw Code is the most readable, open implementation of a production-grade AI coding agent architecture available today. Whether you use it in production or study it to build something better, the patterns it implements are now public knowledge.

---

## Further Reading

- [AI Coding Assistants Compared: Features, Pricing, and What Actually Works](/guides/ai-coding-assistants-compared/) — comprehensive comparison of AI coding tools
- [AI Agent SDKs in 2026](/guides/ai-agent-protocol-stack-2026/) — the frameworks powering agent development
- [MCP Security Landscape](/guides/mcp-security-landscape/) — security implications of agent tool access
