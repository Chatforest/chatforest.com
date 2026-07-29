# Claude Code /fork: Git-Style Session Branching Comes to Your AI Coding Terminal

> Anthropic's /fork command clones a Claude Code session so you can branch into parallel approaches from the same starting point, with prompt-cache cost sharing across the copies. Here is how it worked as of mid-2026, what changed around it, and when to use it over regular subagents.


Claude Code's `/fork` command clones your current session — the system prompt, tool definitions, model selection, and full conversation history — into a new subagent that picks up mid-conversation. Anthropic first shipped the underlying mechanism behind a `CLAUDE_CODE_FORK_SUBAGENT` flag in [Claude Code v2.1.117](https://github.com/anthropics/claude-code/releases/tag/v2.1.117) (April 22, 2026), then made it `/fork`'s default behavior starting with [v2.1.161](https://github.com/anthropics/claude-code/releases/tag/v2.1.161) (released June 2, 2026) — the behavior this guide describes. Three days before this piece was published, [v2.1.172](https://github.com/anthropics/claude-code/releases/tag/v2.1.172) (June 10, 2026) separately shipped two related changes covered below: nested sub-agent spawning and a `/plugin` search bar. **Update for later readers:** as of [v2.1.212](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) (July 17, 2026), Anthropic renamed things — see the callout further down before you rely on the exact commands here.

---

## What `/fork` Does

Running `/fork` in a Claude Code session (in the v2.1.161–v2.1.211 window) creates a copy of the session state at that exact moment: the system prompt, tool definitions, model selection, and the entire conversation history. The fork runs as a subagent with that inherited context pre-loaded — [a fork inherits the parent conversation instead of starting fresh](https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation), which is what distinguishes it from a regular subagent.

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

The cost difference matters at scale. When multiple forks share the same session prefix, children 2 through N pull that shared history straight from the prompt cache rather than re-sending it as new input tokens. [Anthropic's prompt-caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) sets cache-read tokens at 0.1x the base input-token price — a 90% cost reduction, roughly 10x cheaper — for any request that hits a cached prefix, which is exactly what happens once the first fork child has primed the cache.

---

## How to Enable Forked Subagents

Set the environment variable:

```bash
export CLAUDE_CODE_FORK_SUBAGENT=1
```

This flag has governed forked-subagent behavior since [Claude Code v2.1.117](https://github.com/anthropics/claude-code/releases/tag/v2.1.117) (April 22, 2026): on v2.1.117 through v2.1.160 it was required to enable forking at all. From [v2.1.161](https://github.com/anthropics/claude-code/releases/tag/v2.1.161) onward (June 2, 2026), `/fork` spawns a forked subagent by default even without the flag; setting it explicitly to `1` or `0` forces the behavior on or off, per [Anthropic's sub-agents documentation](https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation).

**Update for readers arriving after July 2026:** in [v2.1.212](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) (July 17, 2026), Anthropic changed `/fork`'s meaning. `/fork` now copies your whole conversation into a new, independent background session instead of spawning an inherited-context subagent; the forked-subagent behavior this guide describes is invoked with `/subtask` instead. Check the [official command reference](https://code.claude.com/docs/en/commands) for the current definitions before scripting against either command.

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

Each fork knows the full project context but tackles an independent task. By default, a fork works against your existing checkout rather than an isolated copy — [Anthropic notes that a fork's file edits only go to a separate git worktree if `isolation: "worktree"` is explicitly requested](https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation) — so keep parallel forks scoped to different files (as in the example above) or request worktree isolation if there's any chance of overlap.

### Hypothesis Testing

When debugging, you might have two competing theories about the root cause. Fork once per hypothesis, let both investigate in parallel, and compare findings.

---

## What Shipped Around the Same Time

Claude Code's release cadence is fast — these landed in nearby but separate versions, not one bundled release with `/fork`:

**Nested sub-agents:** [v2.1.172](https://github.com/anthropics/claude-code/releases/tag/v2.1.172) (June 10, 2026) let subagents spawn their own nested subagents, [up to five layers deep by default](https://code.claude.com/docs/en/sub-agents#let-subagents-spawn-their-own-subagents) — a default that wasn't configurable at the time. Anthropic has since revised that default twice: [v2.1.217](https://github.com/anthropics/claude-code/releases/tag/v2.1.217) (July 21, 2026) temporarily dropped the default to one level and introduced `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` to configure it, and [v2.1.219](https://github.com/anthropics/claude-code/releases/tag/v2.1.219) (July 24, 2026) raised the default to three.

**Plugin search interface:** The same [v2.1.172](https://github.com/anthropics/claude-code/releases/tag/v2.1.172) release added a search bar for browsing a marketplace's plugins inside `/plugin`, making it faster to find and add integrations.

---

## When Not to Use `/fork`

Forking is not always the right tool:

- **For simple sequential tasks:** `/fork` adds overhead (background process, result synthesis). Use it when true parallelism has value.
- **When tasks are not independent:** If approach A and approach B both modify the same file, you will get conflicts — especially since forks don't get isolated worktrees unless you ask for one (see above). Forks work cleanly when the parallel tasks operate on independent resources.
- **When you need interaction during the task:** Forked subagents run in the background. If your workflow requires back-and-forth during execution, a sequential approach or an interactive branch is better.
- **Deep nesting:** The default nested-subagent depth has changed release to release — [five layers, then one, then three](https://code.claude.com/docs/en/sub-agents#let-subagents-spawn-their-own-subagents) — so check `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (configurable since v2.1.217) for your installed version before assuming a particular limit.

---

## The Relationship to `/branch`

Per [Anthropic's command reference](https://code.claude.com/docs/en/commands), `/branch` creates a new human-facing conversation branch: it switches you into a copy of the current conversation while preserving the original, which you can return to with `/resume`. As described above, `/fork` (with `CLAUDE_CODE_FORK_SUBAGENT=1`, or by default from v2.1.161 through v2.1.211) instead created an autonomous background agent that ran the forked session without user interaction and returned a result to the parent session — the model this guide is built around.

The mental model, for the v2.1.161–v2.1.211 window:
- `/branch` = "I want to explore this direction myself"
- `/fork` = "I want Claude to explore this direction in parallel and bring back results"

**From v2.1.212 onward**, that background-subagent job moved to `/subtask`, and `/fork` took on a version of `/branch`'s job — copying the conversation into an independent background session rather than switching you into it directly. Confirm which behavior your installed version uses via the [command reference](https://code.claude.com/docs/en/commands) before relying on this section.

---

## Builder Checklist

- [ ] Set `CLAUDE_CODE_FORK_SUBAGENT=1` explicitly if you want to force forked-subagent behavior regardless of your version's default (see version notes above)
- [ ] Identify decision points in your workflow where parallel exploration adds value over sequential tries
- [ ] Design fork tasks to touch different files, or request `isolation: "worktree"` — forks share your checkout by default
- [ ] Use multiple forks on the same session to get prompt-cache cost savings on the shared prefix
- [ ] Check `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` for your installed version rather than assuming a fixed nesting limit
- [ ] For sequential debugging or interactive refinement, stick with the main session or `/branch`
- [ ] If you're on v2.1.212 or later, confirm today's `/fork` vs. `/subtask` behavior in the [official docs](https://code.claude.com/docs/en/commands) before following this guide literally

---

## Bottom Line

`/fork` (in the v2.1.161–v2.1.211 window this guide covers) brought a familiar concept — git branching — to the Claude Code session model. The core value was trying multiple approaches in parallel from the same starting context, without losing the original session state or paying full input-token cost for each branch.

The prompt-cache sharing makes this genuinely cost-effective for workflows with large shared context windows: cache-read tokens cost roughly [10x less than fresh input tokens](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), a 90% reduction. If you are running a codebase-wide analysis and want to explore three different refactoring directions simultaneously, forking cuts the effective input cost on directions 2 and 3 by roughly 90% compared to spinning up three independent sessions from scratch.

The nested sub-agent support that landed a few days later, in [v2.1.172](https://github.com/anthropics/claude-code/releases/tag/v2.1.172), expanded what Claude Code can coordinate — though Anthropic has revised the default nesting depth twice since (see above). If you're reading this after July 2026, check the update notes throughout this guide: both `/fork`'s meaning and the nesting-depth default have changed since publication.

