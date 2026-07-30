# Hermes Agent Gets Non-Blocking Subagents: What Changes for Multi-Agent Builders

> Nous Research merged background subagent support for Hermes Agent's delegate_task tool on June 15, 2026. The parent agent no longer blocks while children run — it dispatches, continues, and gets the result posted back when the child finishes. Here's the architecture and what it unlocks.


Hermes Agent's multi-agent support just crossed a meaningful threshold. Nous Research merged [PR #40946](https://github.com/NousResearch/hermes-agent/pull/40946), "async background subagents via `delegate_task(background=true)`," into `main` on June 15, 2026, and changed how delegation works at the architectural level. (A separate, more elaborate six-tool `async_delegation` proposal — with tools named `delegate_task_async`, `check_task`, `steer_task`, `collect_task`, `cancel_task`, and `list_tasks` — had been floated in [GitHub Issue #5586](https://github.com/NousResearch/hermes-agent/issues/5586). That issue was closed as not planned once the simpler `background=true` parameter shipped instead, so none of those six tool names made it into the product — only `delegate_task` with a `background` flag, plus the `/agents` and `/stop` CLI commands described below.)

Previously: when a parent agent called `delegate_task`, the parent's conversation froze until every child finished. A sub-agent running a 10-minute research task meant 10 minutes of silence. For short tasks that was acceptable. For anything non-trivial — crawling documentation, running test suites, long-horizon code generation — it was a hard bottleneck.

Now: the parent calls `delegate_task(background=true)`, gets a handle back immediately, and continues working. The child runs in parallel, and its result is posted back into the conversation as a new message once it finishes — the parent doesn't need to poll for it. See the official [Subagent Delegation docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation), which describe this as: "Hermes returns a handle immediately so the conversation can continue, then posts the result back."

This is a shift from a call-and-wait model to a spawn-and-continue model. If you're building multi-agent workflows on Hermes, this changes what's architecturally possible.

---

## What Changed

[Hermes Agent](/builders-log/hermes-agent-nous-research-openrouter-number-one-self-improving-builder-guide/) already had subagent delegation before June 15. The `delegate_task` tool let a parent hand off a task to a child agent, which ran with the same credentials and toolsets as the parent, using the same `AIAgent` machinery — confirmed in the [delegation docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation), which note subagents "inherit the parent's enabled toolsets" and "API key, provider configuration, and credential pool." Each child starts with a completely fresh conversation, though — no shared memory with the parent; only the `context` string the parent passes in and, on completion, the child's final summary.

The problem was execution model: `delegate_task` was synchronous by default. The parent blocked inside the tool call until children returned. Every delegated task was a wall the parent couldn't see past until it was done.

[PR #40946](https://github.com/NousResearch/hermes-agent/pull/40946) added non-blocking execution as an option on the same tool, rather than shipping it as a separate tool. Call `delegate_task(background=true)` and the call returns almost immediately with a dispatch handle (`{status: "dispatched", delegation_id, mode: "background"}`, per the PR), while the child agent runs in a daemon thread. The parent is free to issue new commands, spawn additional subagents, or respond to user input while it runs.

**Update path:** `hermes update` — no configuration required for existing installs.

---

## How a Background Delegation Is Managed

There is no separate `async_delegation` tool suite. The full lifecycle of a background subagent runs through `delegate_task` plus two CLI commands, per the [delegation docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation):

**`delegate_task(background=true)`** — Dispatches a background agent for the given goal/context. Returns a handle almost immediately (the PR that shipped this notes dispatch happens "in ~2ms"). Same credentials and toolsets as a synchronous `delegate_task` call, but a fresh conversation — no shared memory. The child runs in a daemon thread; the parent continues without waiting.

**`/agents`** (aliased `/tasks`) — The way to check on running background subagents. Per the docs, it shows "a tree view of running subagents with live progress, per-child costs/tokens, and kill/pause controls." This is a CLI command the human operator runs, not a tool the parent agent calls itself.

**Automatic completion.** There's no explicit "collect" step. When a background task finishes, its result is pushed back into the conversation as a new message — the docs describe it as "posts the result back" — so the parent picks it up on its next turn rather than blocking on a join call.

**Live transcripts.** While a background child is running, its output is written to an append-only, timestamped log file at `~/.hermes/cache/delegation/live/<delegation_id>/task-<n>.log`, per the delegation docs — this is how you tail a child's progress outside the `/agents` view.

**Stall detection.** Hermes distinguishes a stuck child from a slow one automatically: the docs describe interrupting idle background subagents after a 450-second idle threshold (1,200 seconds if the child is mid-tool-call), with a grace window for recovery — no manual polling required.

**`/stop`** — Terminates background delegations for the current session (equivalent to a cancel). Closing or resetting the session also discards any still-running children.

Two capabilities from the original Issue #5586 proposal did **not** ship: there's no way for the parent to inject a new instruction into an already-running background child (no `steer_task` equivalent), and there's no dedicated tool for the parent agent itself to list or poll tasks programmatically — that's a human-facing `/agents` command, not something `delegate_task`'s caller can invoke mid-run.

---

## Architecture Under the Hood

The implementation keeps the child agent on the same execution path as `delegate_task` — same credentials and toolsets — but changes the threading model for the `background=true` case. Per [PR #40946](https://github.com/NousResearch/hermes-agent/pull/40946) and the [delegation docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation):

- **Daemon threads, not subprocesses.** Each background subagent runs as a daemon thread in the parent process. Startup overhead is lower than spawning a subprocess, and results are pushed to a completion queue that a watcher drains between the parent's idle turns, re-entering them as new conversation turns.
- **Progress-based stall monitoring**, not a fixed timeout. Background delegations are watched by what the docs call a "progress-based stall monitor" — idle children are interrupted after 450 seconds (1,200 seconds if mid-tool-call) rather than a flat wall-clock cutoff.
- **Context isolation.** Only the final summary from a completed task is returned to the parent's context — confirmed directly in the docs: "only its final summary enters the parent's context." The child's intermediate reasoning and tool calls stay out of the parent's context window; you can still inspect them via the live transcript log file, not an in-memory buffer.
- **Depth and concurrency limits.** Nested delegation (a child spawning its own children) is capped by `delegation.max_spawn_depth`, which defaults to 1 — flat, single-level delegation only, per the docs. Parallel batch delegation is capped by `delegation.max_concurrent_children`, which also defaults to 3.

Some architectural details that circulated in early proposals for this feature — an in-memory ring buffer for child output, a dedicated file-coordination layer to prevent sibling subagents from clobbering each other's file writes — are not documented in the shipped delegation docs or the merged PR, and this page can't verify they exist as described. They've been removed from this guide rather than left uncited.

---

## Builder Patterns This Unlocks

**Parallel module delegation.** A parent agent decomposing a large codebase can spawn separate background agents per module and continue orchestrating while they work. Previously, this required running multiple Hermes instances and stitching results together manually.

**Non-blocking research + implementation.** Spawn a background agent to research an API or crawl documentation while the parent continues implementing a different part of the codebase. The research summary posts back into the conversation automatically once the child finishes.

**Concurrent test + build.** Delegate test runs or builds as background tasks while the parent continues writing code. Check progress with `/agents`, and let the result post back into the conversation automatically once the run finishes — there's no way to steer a running background child mid-task, so if the test surface changes you cancel via `/stop` and re-dispatch rather than redirect in place.

**Orchestrator with dynamic task management.** An orchestrator agent (`role="orchestrator"`, which requires raising `max_spawn_depth` above its default of 1) can fan out several background delegations and let each result re-enter the conversation as it completes, prioritizing whichever unblocks the most downstream work — the human operator can watch all of them at once via `/agents`.

**Long-running agents with human check-ins.** A parent agent managing a multi-hour task can spawn a background child, then return to the user for interim decisions without the user waiting for the child to finish. The child keeps running independently; its result arrives as a new message when it's done, or the operator can cut it short with `/stop`.

---

## What Hasn't Changed

- `delegate_task` is still one tool, not two. Omit `background` (or leave it `false`) and the call blocks until the child returns, same as before — there's no separate synchronous tool to reach for.
- Subagent isolation guarantees are unchanged. Only the final summary reaches the parent's context; each child still starts a fresh conversation with no shared memory.
- Credentials and toolsets are still inherited from the parent — background subagents don't have independent identity or expanded permissions, per the [delegation docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation).
- `max_spawn_depth` still applies (default 1). You can't chain unlimited nested delegations — the configurable spawn depth limit prevents runaway recursion, and only `role="orchestrator"` children can spawn further delegation at all.

---

## What to Watch

- **Auto-forking subagents with human approval gates.** [GitHub Issue #31392](https://github.com/NousResearch/hermes-agent/issues/31392), open as of this writing, proposes an "autofork channel" where agents emit next-step directives that auto-spawn follow-up tasks, plus a "submit channel" where tasks wait in a PENDING state for human approval before running. It's a proposal from a user running a similar workflow in production, not yet a merged feature — worth watching, not yet usable.
- **`/smalltalk` side conversations.** [Issue #13060](https://github.com/NousResearch/hermes-agent/issues/13060), also open, requests a `/smalltalk` command for a parallel, asynchronous side-conversation thread — so users can ask tangential questions without polluting the main task context. Not shipped; watch the issue.
- **Profile Builder is a separate, adjacent feature — not per-subagent profiles.** The dashboard's [Profile Builder](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard), [reported by MarkTechPost on June 11](https://www.marktechpost.com/2026/06/11/nous-research-ships-hermes-agent-profile-builder-identity-model-skills-and-mcp-servers-in-one-dashboard-flow/), lets you build a full Hermes *profile* (its own model, skills, and MCP servers) from the browser instead of hand-editing `config.yaml`. But a profile is a separate top-level Hermes instance with its own shell alias and home directory, not an identity you attach to an individual background subagent. Wiring named profiles into `delegate_task` itself — so a single orchestrator could spawn children running different models — is a separate, still-open proposal: [Issue #9459](https://github.com/NousResearch/hermes-agent/issues/9459). Don't expect differentiated per-subagent models yet.

---

## Getting Started

If you're running Hermes Agent:

```bash
hermes update
```

That's the full upgrade path — `delegate_task(background=true)` is available immediately after update. No configuration required.

If you're new to Hermes Agent, the [full builder guide](/builders-log/hermes-agent-nous-research-openrouter-number-one-self-improving-builder-guide/) covers the architecture, setup, and when Hermes makes sense alongside tools like Claude Code and OpenClaw.

---

*Hermes Agent is MIT-licensed and maintained by Nous Research. GitHub: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)*

