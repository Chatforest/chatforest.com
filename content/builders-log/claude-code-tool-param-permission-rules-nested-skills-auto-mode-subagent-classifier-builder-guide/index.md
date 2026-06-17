---
title: "Claude Code 2.1.178: Parameter Permission Rules, Nested Skills, and the Subagent Classifier Gap"
date: 2026-06-17
description: "Claude Code 2.1.178 (June 15) adds Tool(param:value) permission syntax — block Opus subagents by model, restrict WebFetch to specific domains, gate Bash by argument pattern. Plus: nested .claude/skills now load automatically, and auto mode finally classifies subagent spawns before they execute."
og_description: "Claude Code 2.1.178 ships Tool(param:value) permission rules, nested .claude/skills loading, and a fix to the auto mode gap where subagent spawns bypassed the classifier. Here's everything builders need to know."
content_type: "Builder's Log"
categories: ["Anthropic", "Claude Code", "Developer Tools"]
tags: ["anthropic", "claude-code", "permission-rules", "auto-mode", "subagents", "nested-skills", "agentic", "june-2026", "builders-log"]
---

Claude Code v2.1.178, released June 15, 2026, ships three changes that matter for teams running Claude Code in production: a new `Tool(param:value)` permission syntax that gives rule authors parameter-level control over any tool call, automatic loading of skills from nested `.claude/skills` directories, and a fix to the auto mode gap where subagent spawns were not evaluated by the classifier before launch. Part of our **[Builder's Log](/builders-log/)**.

---

## What Shipped in 2.1.178

| Change | Category |
|--------|----------|
| `Tool(param:value)` permission syntax with `*` wildcard | New feature |
| Nested `.claude/skills` directories now auto-load | New feature |
| Closest `.claude/` to working directory wins on name collisions | New feature |
| Subagent spawns now pre-screened by auto mode classifier | Security / safety |
| `/doctor` redesigned with flat tree layout and clearer status icons | UX |
| `/bug` now requires description text before submitting | UX |
| Remote Control error messages now show persistent `/rc failed` indicator | UX |
| Fixed subagent transcript missing tool results and live progress | Bug fix |
| Fixed messages dropped when sent while subagent was finishing | Bug fix |
| Fixed 401 for `claude agents` workers using custom API gateway | Bug fix |
| Fixed `WebFetch(domain:*.example.com)` wildcard never matching subdomains | Bug fix |
| Fixed nested skills with directory-qualified names blocked in non-interactive runs | Bug fix |
| Fixed MCP server-level specs in subagent `disallowedTools` silently ignored | Bug fix |

---

## Tool(param:value) Permission Rules

### The old model

Before 2.1.178, Claude Code permission rules matched on tool name only. You could allow or block `Bash`, `WebFetch`, `Agent`, or `Read` — but you could not express anything about *what arguments* those tools were called with. If you wanted to block Opus subagents while allowing Sonnet, you had no way to write that in a permission rule.

### The new syntax

2.1.178 adds a parameter clause to the permission rule syntax:

```
Tool(param:value)
```

The `param` is a key from the tool's input object. The `value` is the expected string, with `*` as a wildcard prefix, suffix, or standalone. Rules are evaluated in the same allow/deny order as the existing permission system.

### Example: Block Opus subagents, allow Sonnet

Add to your project `.claude/settings.json`:

```json
{
  "permissions": {
    "deny": ["Agent(model:claude-opus*)"],
    "allow": ["Agent(model:claude-sonnet*)"]
  }
}
```

Effect: Any subagent spawn that requests an Opus model is blocked before the spawn fires. Sonnet subagents proceed normally.

This is useful for cost control in repositories where developers have auto mode on and the project policy is to limit background subagents to Sonnet-class models.

### Example: Restrict WebFetch to internal docs

```json
{
  "permissions": {
    "deny": ["WebFetch"],
    "allow": ["WebFetch(url:https://docs.yourcompany.com/*)"]
  }
}
```

The deny-all-then-allow pattern works here: `deny: ["WebFetch"]` blocks the rule first, then `allow: ["WebFetch(url:https://docs.yourcompany.com/*)"]` opens up exactly the URLs you need. Subagents inherit these rules unless they are explicitly overridden in the `disallowedTools` list.

**Note**: Before 2.1.178, `WebFetch(domain:*.example.com)` wildcards were not matching subdomains at all due to a bug. Both the new syntax and this existing bug fix shipped together — if you were using domain wildcards and seeing them fail, update to 2.1.178.

### Example: Gate Bash by shell flag

```json
{
  "permissions": {
    "deny": ["Bash(command:*--rm*)"],
    "deny": ["Bash(command:*sudo*)"]
  }
}
```

This blocks any Bash call whose command string contains `--rm` or `sudo`, regardless of the surrounding invocation. The wildcard prefix and suffix apply so partial matches work.

### Combining parameter rules with the existing allow/deny list

Parameter rules compose with the existing permission system. The rule evaluation order is:

1. If an explicit `deny` matches, block.
2. If an explicit `allow` matches, proceed.
3. Fall through to default behavior (prompt in interactive mode, deny in non-interactive).

The `Tool(param:value)` clauses are evaluated as part of step 1 or 2 depending on which list they appear in. You can mix parameterized and plain rules freely:

```json
{
  "permissions": {
    "allow": ["Read", "WebFetch(url:https://docs.yourcompany.com/*)"],
    "deny": ["Write", "Agent(model:claude-opus*)"]
  }
}
```

### What parameters are available per tool?

The parameter key must correspond to a field in the tool's input schema. Useful ones:

| Tool | Parameter | Example value |
|------|-----------|---------------|
| `Agent` | `model` | `claude-opus*`, `claude-sonnet-4-6` |
| `WebFetch` | `url` | `https://internal.example.com/*` |
| `WebFetch` | `domain` | `*.example.com` |
| `Bash` | `command` | `*sudo*`, `*--force*` |
| `Read` | `file_path` | `~/.ssh/*` |
| `Write` | `file_path` | `/etc/*` |
| `Edit` | `file_path` | `/etc/*` |

The wildcard `*` matches zero or more characters. It can appear at the start, end, or both, but not in the middle (e.g., `*.example.com` and `https://docs.*` work; `https://docs.*.com` does not).

---

## Nested .claude/skills Loading

### What changed

Skills placed in a `.claude/skills/` directory nested inside a subdirectory of your project now load automatically when Claude Code's working directory is inside that subdirectory. Before 2.1.178, only the root-level `.claude/skills/` was scanned.

### How name collisions resolve

If a nested skill has the same name as a root-level skill, both load. The nested skill appears as `<dir>:<name>` to avoid shadowing:

```
Root:       .claude/skills/deploy.md       → available as "deploy"
Nested:     frontend/.claude/skills/deploy.md  → available as "frontend:deploy"
```

You can invoke the nested skill by its qualified name: `run the frontend:deploy skill`.

### Closest .claude wins for configuration

For `agent`, `workflow`, and `output-style` settings, the `.claude/` directory closest to the current working directory takes precedence on collision. This lets frontend, backend, and data subdirectories each carry their own output style or default agent without interfering with each other.

A repository layout that takes advantage of this:

```
my-project/
├── .claude/
│   └── settings.json           # root defaults
├── frontend/
│   └── .claude/
│       └── settings.json       # frontend-specific output-style, skills
└── backend/
    └── .claude/
        └── settings.json       # backend-specific agent, model preferences
```

When a session is opened with `cd frontend && claude`, the `frontend/.claude/settings.json` settings win for any key that exists there.

### Non-interactive runs

A bug in prior versions blocked nested skills with directory-qualified names (`frontend:deploy`) from running in non-interactive mode (`claude -p "..."`) — they were silently skipped. This is fixed in 2.1.178. CI pipelines that reference nested skills by qualified name will now work correctly.

---

## Auto Mode: Closing the Subagent Classifier Gap

### The previous gap

Auto mode routes Claude Code tool calls through a server-side classifier before each action fires. The classifier decides whether a given action needs human approval or can proceed automatically.

However, before 2.1.178, *spawning a subagent* was not itself classified before the spawn completed. The subagent was created first, and its actions were individually classified — but the spawn request itself could bypass the pre-launch check. This meant that in a carefully crafted scenario, a primary agent operating in auto mode could spawn a subagent configured to request actions the human had not reviewed.

### What changed

2.1.178 adds classifier pre-screening to subagent spawn requests. Before a subagent starts executing, the classifier evaluates the spawn parameters — model, initial prompt, tool allowlist — the same way it evaluates individual tool calls. If the spawn would trigger an action that requires human approval, the spawn is held pending confirmation.

In practice, this matters most for:

- **Agentic pipelines running unattended** where the primary agent has auto mode permissions but subagent behavior was an implicit trust escalation.
- **Deep agent chains** (Claude Code 2.1.172 added up to 5 levels of nesting). Without classifier pre-screening of spawns, each nesting level was a potential gap.
- **Custom permission rules** that restrict the primary agent but were not being evaluated at spawn boundaries.

For most interactive users running a single session, the change is invisible. For teams that have built auto mode pipelines or are using agent orchestration, this closes a meaningful gap.

---

## Other Fixes Worth Noting

**Subagent transcript** now shows tool results and live progress, not just the final response. If you were opening a subagent's transcript and seeing an empty or summary-only view, that is fixed.

**Messages dropped during subagent finish**: In prior versions, messages sent to Claude Code while a subagent was completing its last turn were silently dropped. Fixed in 2.1.178 — messages are now queued correctly.

**Custom API gateway 401**: Teams routing `claude agents` workers through a custom API gateway were seeing `401 Invalid bearer token` errors. This is fixed.

**MCP disallowedTools in subagents**: MCP server-level specs in a subagent's `disallowedTools` list were being silently ignored. Fixed — the specs now apply correctly.

---

## Upgrade and Configuration Checklist

```bash
# Update Claude Code
npm update -g @anthropic-ai/claude-code

# Verify version
claude --version
# Should show 2.1.178 or later
```

Once updated:

1. **Review your permission rules** — if you have existing `allow`/`deny` lists, consider whether `Tool(param:value)` rules could tighten them. Common wins: `Agent(model:claude-opus*)` deny to cap costs, `Read(file_path:~/.ssh/*)` deny to block credential reads.

2. **Audit nested .claude directories** — if your repo has subdirectories with `.claude/skills/`, verify the skill names are unique or decide on your qualified-name convention now (`frontend:deploy`, `backend:deploy`).

3. **Test CI pipelines using nested skills** — if you call a nested skill by its qualified `<dir>:<name>` form in non-interactive mode, the prior bug that silently skipped it is now fixed. Test that the correct skill runs.

4. **If you use auto mode in pipelines** — the subagent classifier gap fix is passive. No configuration change needed. But it is worth re-validating your permission rules now that spawn requests are also classified.

---

*Claude Code updates frequently. The prior Claude Code article in the Builder's Log covered [Auto Mode on Bedrock, Vertex, and Foundry (v2.1.158)](/builders-log/claude-code-auto-mode-bedrock-vertex-foundry-enterprise-builder-guide/) and [nested sub-agent depth (v2.1.172)](/builders-log/claude-code-nested-sub-agents-depth-5-token-math-builder-guide/).*
