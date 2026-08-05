---
title: "Omnigent: One Layer Above Claude Code, Codex, and Cursor — Swap, Compose, and Govern Your Coding Agents Without Rewriting"
date: 2026-07-10
description: "Omnigent is an open-source meta-harness (Databricks, Apache 2.0) that sits above Claude Code, Codex, Cursor, Pi, and custom agents — giving builders a common interface for composition, cost-cap policies, OS sandboxing, and real-time session sharing. Its built-in Polly orchestrator runs sub-agents in parallel git worktrees and routes each diff to a cross-vendor reviewer."
tags: ["claude-code", "open-source", "agent-orchestration", "coding-agents", "developer-tools", "builder-guide", "databricks", "multi-agent"]
sources_audited: 2026-08-05
---

If you use more than one AI coding agent, you already know the friction: Claude Code's context model is different from Codex's, Cursor's slash commands don't carry over, and switching models mid-project means rebuilding mental state and re-specifying policies from scratch. Most teams end up committing to one harness and sticking with it — not because it's always the best tool, but because the switching cost is too high.

[Omnigent](https://omnigent.ai/) ([open-sourced by Databricks in June 2026](https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents), Apache 2.0) is an attempt to fix this at the infrastructure layer rather than the prompt layer. Instead of asking you to choose one agent, it gives you a common orchestration layer above all of them.

## What Omnigent Is

Omnigent is a meta-harness: a layer that wraps Claude Code, Codex, Cursor, Pi, OpenCode, Hermes, and agents you write yourself in a uniform interface. The architectural observation behind it is that all coding harnesses share the same abstract shape — messages and files in, text streams and tool calls out — and that abstraction is stable enough to build a swap-layer on top of.

[The result is a runner that gives every agent a sandboxed session with a uniform API, and a server that provides policies, sharing, and multi-interface access](https://omnigent.ai/) (terminal, web, macOS app, mobile). You interact with one interface; Omnigent routes work to whichever agent (or combination of agents) you've configured.

Currently in alpha, the project is [on GitHub](https://github.com/omnigent-ai/omnigent) with a Discord community, and is [built by the Databricks AI team and Neon](https://omnigent.ai/).

## Three Pillars: Composition, Control, Collaboration

### Composition

The most immediate capability is swappability. You configure an agent in a YAML spec:

```yaml
name: my_agent
prompt: [Your agent description]
executor:
  harness: claude-sdk   # or codex, cursor, pi, opencode, hermes
tools:
  - [local functions, MCP servers, or sub-agents]
```

Switching from Claude Code to Codex for a given agent is [a one-line change in the `executor.harness` field](https://omnigent.ai/docs/build/harnesses). The surrounding policy configuration, collaboration setup, and tool definitions stay the same. If you want to benchmark two harnesses on the same task, you run the same YAML twice with different executor values.

Composition also lets you mix harnesses in a single agent hierarchy — a parent orchestrator built on one SDK can spawn sub-agents on a different harness in the same session, without any translation layer you have to write yourself.

### Control

[Omnigent's policy system operates at three levels](https://omnigent.ai/docs/policies/overview):

- **Server-wide** — set by the administrator, applied to all agents and sessions on that server instance
- **Per-agent** — developer-defined defaults baked into the YAML spec
- **Per-session** — individual user settings, which are checked first and take priority over agent defaults

[Built-in policies include spend caps](https://omnigent.ai/docs/policies/builtin) (pause the agent after it crosses a token cost threshold, e.g., $100) and access limits (an agent can only write to files it created in that session). The OS sandbox intercepts and optionally transforms network requests before they leave the machine. Users can also request policy changes conversationally during a session — "don't make any git commits without asking me first" becomes a session-level rule without touching the YAML.

This is different from prompt-based guardrails. The policy layer tracks agent actions at the session level, not just at the text-generation level. A prompt instruction can be overridden by the model; a sandbox network intercept cannot.

### Collaboration

[Live sessions are shareable by URL](https://omnigent.ai/quickstart/collaborate). Team members can join a running agent session, watch the agent work, comment on specific files, co-drive the conversation, or fork the session into their own copy. Access runs through web, mobile, macOS app, or API — so a teammate on a phone can approve an action or redirect the agent without being at a terminal.

[Cloud execution is available via Modal and Daytona integration](https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents), which means sessions don't have to live on the developer's local machine.

## Polly: The Cross-Vendor Code Review Orchestrator

Omnigent ships with a built-in multi-agent example called [Polly](https://omnigent.ai/docs/use/builtin-agents/polly). She's described as the tech lead: she plans and delegates work, but writes no code herself.

When you give Polly a task, she:

1. **Breaks it into subtasks** and assigns each to a coding sub-agent (Claude Code, Codex, or Pi depending on your configuration)
2. **Runs each sub-agent in a parallel git worktree** — isolated branches so sub-agents don't step on each other's changes
3. **Routes each diff to a reviewer from a different vendor** than the one that wrote it — if Claude Code wrote the code, Codex reviews it (and vice versa)
4. **Leaves the merge to you** — the human team member performs the final integration

The cross-vendor review step is the interesting part. The intuition is that two models from the same vendor (or the same model twice) tend to share blind spots — they'll both miss the same class of edge case, or both approve the same kind of subtle bug. Using a different vendor's model as the reviewer adds a second perspective that isn't correlated with the author's training data.

Run Polly with [`omnigent run examples/polly/`](https://pypi.org/project/omnigent/) or substitute a different harness with the `--harness` flag.

## Builder Implications

**When Omnigent makes sense over standalone Claude Code.** If your agent work is exploratory — comparing how Claude Code and Codex approach the same codebase, or running one model's code through another's review — Omnigent's composition layer eliminates the manual scaffolding. The same applies if you want to enforce cost budgets or sandboxing constraints without building that infrastructure yourself.

**When to skip it.** If you're all-in on Claude Code and have no interest in cross-harness comparison, Omnigent adds a layer of abstraction without much return. Alpha software means the API surface will change; adding a dependency on it right now means tracking those changes. For straightforward single-harness work, Claude Code directly is the lighter path.

**The Polly pattern scales.** Cross-vendor review doesn't require Polly specifically — the underlying pattern (parallel worktrees, different-vendor reviewer) is something you can implement in any orchestration framework. But Polly demonstrates the pattern working end-to-end, which is useful for teams evaluating whether to adopt it. If you're already running multi-agent coding pipelines, the cross-vendor review routing is worth examining regardless of whether you use Omnigent itself.

**Policy enforcement at the harness layer.** The three-level policy hierarchy (server → agent → session) is well-suited for team deployments where different members should have different permission levels. An administrator can lock down network access server-wide while individual developers adjust their own session-level defaults. This is harder to achieve cleanly through prompting alone.

**Vendor lock-in hedge.** The one-line harness swap is a meaningful hedge if you're uncertain whether Claude Code or Codex will be the right default in six months. Building on Omnigent means you're betting on the meta-harness interface staying stable rather than betting on one underlying vendor's API staying stable.

## Access

- **Repository**: [github.com/omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)
- **Homepage**: [omnigent.ai](https://omnigent.ai/)
- **License**: Apache 2.0
- **Status**: Open-source alpha (June 2026)
- **Integrations**: [Claude Agents SDK, OpenAI Agents SDK, Claude Code, Codex, Cursor, Pi, OpenCode, Hermes, Modal, Daytona](https://github.com/omnigent-ai/omnigent)

The project is [described as "built in the open,"](https://omnigent.ai/) meaning the roadmap and design decisions are visible in the repository as they happen. A Discord community is available for early adopters.
