---
title: "Hermes Agent Gets Non-Blocking Subagents: What Changes for Multi-Agent Builders"
date: 2026-06-18
description: "Nous Research shipped async subagent support for Hermes Agent on June 15, 2026. The parent agent no longer blocks while children run — it spawns, continues, and collects results when ready. Here's the architecture and what it unlocks."
og_description: "Hermes Agent's async_delegation toolset (June 15) kills the synchronous bottleneck in multi-agent workflows. delegate_task_async returns a task_id immediately — the parent keeps working. Builder guide inside."
content_type: "Builder's Log"
categories: ["Agent Frameworks", "Open Source", "Developer Tools"]
tags: ["hermes-agent", "nous-research", "async-agents", "multi-agent", "subagents", "delegation", "agent-orchestration", "open-source", "concurrent-agents"]
---

Hermes Agent's multi-agent support just crossed a meaningful threshold. On June 15, 2026, Nous Research shipped the `async_delegation` toolset — tracked in [GitHub Issue #5586](https://github.com/NousResearch/hermes-agent/issues/5586) — and changed how delegation works at the architectural level.

Previously: when a parent agent called `delegate_task`, the parent's conversation froze until every child finished. A sub-agent running a 10-minute research task meant 10 minutes of silence. For short tasks that was acceptable. For anything non-trivial — crawling documentation, running test suites, long-horizon code generation — it was a hard bottleneck.

Now: the parent spawns a background agent, receives a `task_id` immediately, and continues working. The child runs in parallel. The parent polls or collects when it needs the result.

This is a shift from a call-and-wait model to a spawn-and-poll model. If you're building multi-agent workflows on Hermes, this changes what's architecturally possible.

---

## What Changed

[Hermes Agent](/builders-log/hermes-agent-nous-research-openrouter-number-one-self-improving-builder-guide/) already had subagent delegation before June 15. The `delegate_task` tool let a parent hand off a task to a child agent, which ran with the same credentials, toolsets, and AIAgent machinery as the parent.

The problem was execution model: `delegate_task` was synchronous. The parent blocked inside the tool call until all children returned. Every delegated task was a wall the parent couldn't see past until it was done.

The async_delegation toolset replaces this with non-blocking execution. The parent calls `delegate_task_async`, the tool call returns immediately with a `task_id`, and the child agent begins running in-process as a background thread. The parent is free to issue new commands, spawn additional subagents, or respond to user input.

**Update path:** `hermes update` — no configuration required for existing installs.

---

## The Tool Lifecycle

The async_delegation toolset covers the full lifecycle of a background subagent:

**`delegate_task_async`** — Spawns a background agent for the given task description. Returns a `task_id` immediately. Same credentials, memory, and toolsets as `delegate_task`. The child begins executing in a background thread; the parent continues without waiting.

**`check_task`** — Non-blocking status poll. Returns the current state of a running task plus recent output from the child's ring buffer. States include `running`, `done`, `error`, and `cancelled`. Does not block or wait — it reads current snapshot and returns.

**`steer_task`** — Injects a new instruction into a running background agent's context. Lets the parent redirect or refine a child's work mid-execution without cancelling and restarting. Useful when the parent receives new information relevant to an in-progress delegation.

**`collect_task`** — Blocks until the specified task completes, then returns the full result. For cases where the parent has reached a decision point and needs a child's output before proceeding — effectively a join.

**`cancel_task`** — Terminates a running background agent by task_id. Cleans up the registry entry.

**`list_tasks`** — Returns all active and recently completed tasks in the session registry, with current status. Useful for orchestrator agents managing many concurrent delegations.

---

## Architecture Under the Hood

The implementation keeps the child agent on the same execution path as `delegate_task` — same `AIAgent` class, same credentials and toolsets — but changes the threading model.

- **In-process threads.** Each async subagent runs as a thread in the parent process, not a subprocess. Startup overhead is lower, and they share the same session scope and file system without needing inter-process coordination.
- **Ring buffer output.** The child's `_print_fn` is redirected to an in-memory ring buffer keyed by `task_id`. `check_task` reads from this buffer; the parent gets a live window into the child's recent output without waiting for completion.
- **Session-scoped registry.** A dictionary keyed by `task_id` tracks all spawned subagents for the session. `list_tasks` reads this registry; it resets when the parent session ends.
- **Context isolation.** Only the final summary from a completed task is returned to the parent's context. The child's intermediate reasoning and tool calls stay in the ring buffer and don't pollute the parent's context window. This preserves clarity in long-running orchestration sessions.
- **File coordination layer.** When multiple concurrent siblings write to the file system, Hermes uses a file-coordination layer to avoid clobbering — concurrent agents working in the same repo won't overwrite each other's edits.

---

## Builder Patterns This Unlocks

**Parallel module delegation.** A parent agent decomposing a large codebase can spawn separate background agents per module and continue orchestrating while they work. Previously, this required running multiple Hermes instances and stitching results together manually.

**Non-blocking research + implementation.** Spawn a background agent to research an API or crawl documentation while the parent continues implementing a different part of the codebase. Collect when ready.

**Concurrent test + build.** Delegate test runs or builds as background tasks while the parent continues writing code. Use `check_task` to poll, `steer_task` to redirect if a test surface changes, `collect_task` to block only when the parent needs the test result before proceeding.

**Orchestrator with dynamic task management.** An orchestrator agent can use `list_tasks` + `check_task` to maintain a real-time picture of all running delegations, steer tasks as new information arrives, and prioritize collect calls based on which results unblock the most downstream work.

**Long-running agents with human check-ins.** A parent agent managing a multi-hour task can spawn a background child, then return to the user for interim decisions without the user waiting for the child to finish. The child continues running independently; the parent can steer or collect as needed.

---

## What Hasn't Changed

- The `delegate_task` synchronous tool is still available. For short tasks where blocking is acceptable, the simpler synchronous path remains.
- Subagent isolation guarantees are unchanged. Only the final summary reaches the parent's context.
- Credentials and toolsets are still inherited from the parent — async subagents don't have independent identity or expanded permissions.
- `max_spawn_depth` applies. You can't infinitely chain async delegations — the configurable spawn depth limit prevents runaway recursion.

---

## What to Watch

- **async human approval gates.** GitHub Issue #31392 proposes auto-forking subagents with human approval gates — agents emit next-step pointers and auto-spawn follow-ups, gated optionally by async human confirmation. If merged, this would enable fully autonomous multi-stage pipelines with human checkpoints.
- **`/smalltalk` side conversations.** Issue #13060 requests a parallel conversation thread for async sessions — so users can ask tangential questions without polluting the main task context. Not shipped yet; watch the issue.
- **Profile Builder + async delegation.** The [Profile Builder](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) shipped June 11 — it lets you define per-subagent identities with custom model, skills, and MCP servers. Combined with async delegation, you can now spawn subagents with differentiated capabilities running concurrently (e.g., a reasoning-heavy model for analysis, a fast cheap model for boilerplate generation).

---

## Getting Started

If you're running Hermes Agent:

```bash
hermes update
```

That's the full upgrade path — the async_delegation toolset is available immediately after update. No configuration required.

If you're new to Hermes Agent, the [full builder guide](/builders-log/hermes-agent-nous-research-openrouter-number-one-self-improving-builder-guide/) covers the architecture, setup, and when Hermes makes sense alongside tools like Claude Code and OpenClaw.

---

*Hermes Agent is MIT-licensed and maintained by Nous Research. GitHub: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)*
