---
title: "Claude Code /fork: Git-Style Session Branching Comes to Your AI Coding Terminal"
date: 2026-06-13
description: "Anthropic added /fork to Claude Code on June 13, 2026, giving builders a way to branch the current session and run parallel approaches from the same starting point — with prompt-cache cost sharing. Here is how it works and when to use it over regular subagents."
content_type: "Builder's Log"
categories: ["Anthropic", "Claude Code", "Agent Development", "Developer Tools"]
tags: ["claude-code", "fork", "subagents", "session-management", "parallel-agents", "prompt-cache", "multi-agent", "workflow", "anthropic"]
---

Anthropic shipped `/fork` in Claude Code on June 13, 2026, alongside nested sub-agent support and a plugin search interface. The feature is conceptually simple — it clones your current session into a new one — but the implications for multi-agent workflows are significant.

---

## What `/fork` Does

Running `/fork` in a Claude Code session creates a copy of the session state at that exact moment: the system prompt, tool definitions, model selection, and the entire conversation history. The fork runs as a subagent with that inherited context pre-loaded.

The key distinction from a regular subagent: **regular subagents start fresh**. They get a system prompt and a task, but none of your session history. A fork gets everything. It picks up mid-conversation.

This means you can:
- Reach a decision point ("should I refactor this with pattern A or pattern B?")
- Fork into two parallel runs, each trying a different approach
- Compare results without losing the original session state

The original session continues while the fork runs in the background.

---

## Forked Subagents vs. Regular Subagents

| | Regular Subagent | Forked Subagent |
|---|---|---|
| Inherits conversation history | No | Yes |
| Inherits system prompt | Yes | Yes |
| Inherits tool definitions | Yes | Yes |
| Starts from scratch | Yes | No |
| Runs in background | Yes | Yes |
| Cost per additional child | Full input cost | ~10x cheaper (cache) |

The cost difference matters at scale. When multiple forks share the same session prefix, children 2 through N pull that shared history straight from the prompt cache rather than re-sending it as new input tokens. Anthropic's documentation indicates this produces roughly a **10x cost reduction per additional fork child**.

---

## How to Enable Forked Subagents

Set the environment variable:

```bash
export CLAUDE_CODE_FORK_SUBAGENT=1
```

With this set, `/fork` spawns a forked subagent (inheriting full context) rather than acting as an alias for `/branch` (which creates a new human-facing session branch instead). Without the flag, forking behavior varies by context.

---

## Practical Use Cases

### Alternative Implementation Testing

You have a working function but want to test two refactoring approaches before committing to one:

```
# In your session, after discussing the code:
/fork Try refactoring this with a functional pipeline approach
/fork Try refactoring this with a class-based approach
```

Both forks inherit the full conversation — including any architecture decisions, constraints, and prior code analysis — and execute in parallel. You review the results and continue in the main session with whichever direction you prefer.

### Parallel Feature Branches

Multiple independent subfeatures within the same project context:

```
/fork Implement the user authentication endpoint
/fork Implement the profile data endpoint
/fork Write unit tests for the existing payment module
```

Each fork knows the full project context but tackles an independent task. Since they don't share mutable state (each fork runs in its own process), they won't conflict.

### Hypothesis Testing

When debugging, you might have two competing theories about the root cause. Fork once per hypothesis, let both investigate in parallel, and compare findings.

---

## What the Update Also Shipped

The June 13 release included more than `/fork`:

**Nested sub-agents (with one limit):** You can now configure sub-agents that themselves spin up sub-agents, enabling deeper agent hierarchies for complex workflows. The current constraint: a subagent cannot launch another subagent beyond one nesting level — deeply recursive agent trees are not yet supported.

**Smarter model and region handling:** Claude Code now makes more intelligent decisions about which model variant and API region to route requests to, which matters for teams hitting rate limits on specific regions.

**Plugin search interface:** The Claude Code plugin/extension discovery surface was redesigned to make finding and adding integrations faster.

---

## When Not to Use `/fork`

Forking is not always the right tool:

- **For simple sequential tasks:** `/fork` adds overhead (background process, result synthesis). Use it when true parallelism has value.
- **When tasks are not independent:** If approach A and approach B both modify the same file, you will get conflicts. Forks work cleanly when the parallel tasks operate on independent resources.
- **When you need interaction during the task:** Forked subagents run in the background. If your workflow requires back-and-forth during execution, a sequential approach or an interactive branch is better.
- **Deep nesting:** The one-level nesting limit means you cannot build arbitrary agent trees today. Design your workflows accordingly.

---

## The Relationship to `/branch`

`/branch` (and `/new`) create a new human-facing conversation branch — you, the user, switch to a fresh session or a parallel branch you navigate manually. `/fork` (with `CLAUDE_CODE_FORK_SUBAGENT=1`) creates an autonomous background agent that runs the forked session without user interaction and returns a result to the parent session.

The mental model:
- `/branch` = "I want to explore this direction myself"
- `/fork` = "I want Claude to explore this direction in parallel and bring back results"

---

## Builder Checklist

- [ ] Set `CLAUDE_CODE_FORK_SUBAGENT=1` in your shell profile if you want fork to spawn background agents
- [ ] Identify decision points in your workflow where parallel exploration adds value over sequential tries
- [ ] Design fork tasks to be independent — overlapping file modifications will create conflicts
- [ ] Use multiple forks on the same session to get prompt-cache cost savings on the shared prefix
- [ ] Keep nested agent hierarchies to one level deep until Anthropic lifts the nesting constraint
- [ ] For sequential debugging or interactive refinement, stick with the main session or `/branch`

---

## Bottom Line

`/fork` brings a familiar concept — git branching — to the Claude Code session model. The core value is trying multiple approaches in parallel from the same starting context, without losing the original session state or paying full input-token cost for each branch.

The prompt-cache sharing makes this genuinely cost-effective for workflows with large shared context windows. If you are running a codebase-wide analysis and want to explore three different refactoring directions simultaneously, `/fork` cuts the effective input cost on directions 2 and 3 by roughly 90% compared to spinning up three independent sessions.

The nested sub-agent support that shipped alongside this expands what Claude Code can coordinate — though the one-level nesting constraint means truly hierarchical agent architectures still require explicit orchestration from the main session rather than recursive self-delegation.
