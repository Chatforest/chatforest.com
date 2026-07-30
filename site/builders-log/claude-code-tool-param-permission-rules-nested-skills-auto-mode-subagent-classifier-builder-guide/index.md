# Claude Code 2.1.178: Parameter Permission Rules, Nested Skills, and the Subagent Classifier Gap

> Claude Code 2.1.178 (June 15) adds Tool(param:value) permission syntax — block Opus subagents by model, restrict WebFetch to specific domains, gate Bash by argument pattern. Plus: nested .claude/skills now load automatically, and auto mode finally classifies subagent spawns before they execute.


[Claude Code v2.1.178](https://github.com/anthropics/claude-code/releases/tag/v2.1.178), released June 15, 2026, ships three changes that matter for teams running Claude Code in production: a new `Tool(param:value)` permission syntax that gives rule authors parameter-level control over deny/ask rules for any tool call, automatic loading of skills from nested `.claude/skills` directories, and a fix to the auto mode gap where subagent spawns were not evaluated by the classifier before launch. Part of our **[Builder's Log](/builders-log/)**.

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
| Fixed nested skills with directory-qualified names blocked in non-interactive runs | Bug fix |
| Fixed MCP server-level specs in subagent `disallowedTools` silently ignored | Bug fix |

All items in this table are drawn from Anthropic's own [v2.1.178 release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.178). The redesigned `/doctor` layout, the `/bug` description requirement, and the persistent Remote Control `/rc failed` indicator are documented there as UX changes with no separate write-up; the rest are covered section by section below.

---

## Tool(param:value) Permission Rules

### The old model

Before 2.1.178, Claude Code permission rules matched on tool name (and, for a few tools, a built-in specifier like `WebFetch(domain:...)` or a Bash command pattern) — but there was no general way to match on an arbitrary input parameter. If you wanted to block Opus subagents specifically, you had no way to write that in a permission rule.

### The new syntax

2.1.178 adds a parameter clause to the permission rule syntax, documented in Anthropic's [permissions reference](https://code.claude.com/docs/en/permissions):

```
Tool(param:value)
```

The `param` must be a top-level field of the tool's input (nested fields aren't matchable). The `value` supports `*` as a wildcard matching any sequence of characters, anywhere in the string. Two restrictions matter in practice:

- **Deny and ask rules only.** Per Anthropic's docs, `Tool(param:value)` rules work for `deny` and `ask` — there is no equivalent for `allow`. An allow rule "for one parameter value wouldn't establish that the call is safe overall," so allow rules still rely on each tool's own specifier syntax (e.g., `WebFetch(domain:...)`, a Bash command pattern).
- **A tool's "primary content field" can't be matched this way.** That means `command` for Bash/PowerShell, `file_path` for Read/Edit/Write, `path` for Grep/Glob, `notebook_path` for NotebookEdit, and `url` for WebFetch. A rule like `Bash(command:rm *)` would be trivially bypassable by a compound command, so Claude Code ignores it and prints a startup warning — use the tool's own pattern syntax instead (`Bash(rm *)`, `Read(./path)`, `WebFetch(domain:host)`).

### Example: Block Opus subagents

Add to your project `.claude/settings.json`:

```json
{
  "permissions": {
    "deny": ["Agent(model:claude-opus*)"]
  }
}
```

Effect: Any subagent spawn that requests an Opus model is blocked before the spawn fires. This uses `Agent`'s documented `model` parameter, one of the examples Anthropic gives directly (`Agent(model:opus)`) in its [permissions reference](https://code.claude.com/docs/en/permissions).

Note there is no equivalent `allow`-side rule to affirmatively restrict subagents to Sonnet only — per the restriction above, parameter matching is deny/ask-only, so a rule can block Opus but can't be used to positively allow-list "Sonnet and nothing else." For cost control, pair this deny rule with whatever your existing `Agent` allow/prompt policy already is.

### Example: Restrict WebFetch to internal docs

```json
{
  "permissions": {
    "deny": ["WebFetch"],
    "allow": ["WebFetch(domain:docs.yourcompany.com)"]
  }
}
```

The deny-all-then-allow pattern works here: `deny: ["WebFetch"]` blocks the tool by default, then `allow: ["WebFetch(domain:docs.yourcompany.com)"]` opens it back up for that one hostname. Note this restricts by domain, not by URL path — `WebFetch`'s `url` field is one of the "primary content fields" that the new generic `Tool(param:value)` matching explicitly excludes (see above), so `domain:` (a pre-existing, WebFetch-specific specifier, not the new 2.1.178 syntax) is the supported way to allow-list it. [Anthropic's subagent docs](https://code.claude.com/docs/en/sub-agents) note that subagents inherit the parent session's permissions and tool pool unless explicitly narrowed via `tools` or `disallowedTools` in the subagent's own configuration.

**Note**: `WebFetch(domain:*.example.com)`-style wildcards previously did not match subdomains at all, due to a bug. That fix shipped in [Claude Code 2.1.172](https://github.com/anthropics/claude-code/releases/tag/v2.1.172) — three versions before 2.1.178 — not in 2.1.178 itself. If you're on anything at or after 2.1.172, subdomain wildcards should work correctly.

### Example: Gate Bash by shell flag

```json
{
  "permissions": {
    "deny": ["Bash(*--rm*)", "Bash(*sudo*)"]
  }
}
```

This blocks any Bash call whose command string contains `--rm` or `sudo`. Note this uses Bash's own wildcard command-pattern syntax (`Bash(*sudo*)`), not the generic `Tool(param:value)` form — per [Anthropic's permissions reference](https://code.claude.com/docs/en/permissions), `command` is Bash's "primary content field" and a rule shaped like `Bash(command:*sudo*)` is ignored outright (with a startup warning) because it would be trivially bypassable via a compound command.

### Combining parameter rules with the existing allow/deny list

Parameter rules compose with the existing permission system. Per [Anthropic's permissions reference](https://code.claude.com/docs/en/permissions), rules are evaluated in order — deny, then ask, then allow — and the first match wins regardless of how specific a later rule is; if nothing matches, Claude Code falls through to its default behavior (prompt in interactive mode, deny in non-interactive/headless runs).

You can mix a `Tool(param:value)` deny rule with plain tool-name and specifier rules freely. Remember the param form itself is deny/ask-only, so the `WebFetch` allow rule below uses WebFetch's own `domain:` specifier rather than a generic parameter match:

```json
{
  "permissions": {
    "allow": ["Read", "WebFetch(domain:docs.yourcompany.com)"],
    "deny": ["Write", "Agent(model:claude-opus*)"]
  }
}
```

### What parameters are available per tool?

Per [Anthropic's permissions reference](https://code.claude.com/docs/en/permissions), the parameter must be a top-level field of the tool's input, and it cannot be the tool's "primary content field" — that restriction rules out `command` for Bash/PowerShell, `file_path` for Read/Edit/Write, `path` for Grep/Glob, `notebook_path` for NotebookEdit, and `url` for WebFetch. Documented examples of parameters that *are* matchable (deny/ask rules only):

| Tool | Parameter | Example rule |
|------|-----------|---------------|
| `Agent` | `model` | `Agent(model:opus)`, `Agent(model:claude-opus*)` |
| `Agent` | `isolation` | `Agent(isolation:worktree)` |
| `Bash` | `run_in_background` | `Bash(run_in_background:true)` |

For file paths, URLs, and shell commands — the excluded "primary content fields" — use each tool's own specifier syntax instead, e.g. `Read(./path)`, `WebFetch(domain:*.example.com)`, or `Bash(sudo *)`.

The `*` wildcard in a `Tool(param:value)` rule matches any sequence of characters and can appear anywhere in the value — start, middle, end, or standalone (e.g., both `Agent(model:*opus*)` and `Agent(model:claude-opus*)` are valid). A stricter middle-of-string restriction does apply specifically to WebFetch's `domain:` specifier (a wildcard there only expands to match whole subdomain labels between dots), but that's a rule of the `domain:` specifier, not of the generic parameter-matching syntax.

---

## Nested .claude/skills Loading

### What changed

Skills placed in a `.claude/skills/` directory nested inside a subdirectory of your project now load automatically when Claude Code's working directory is inside that subdirectory. Before 2.1.178, only the root-level `.claude/skills/` was scanned. This is documented in the [v2.1.178 release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.178): "Skills in nested `.claude/skills` directories now load when working on files there."

### How name collisions resolve

If a nested skill has the same name as a root-level skill, both load. The nested skill appears as `<dir>:<name>` to avoid shadowing:

```
Root:       .claude/skills/deploy.md       → available as "deploy"
Nested:     frontend/.claude/skills/deploy.md  → available as "frontend:deploy"
```

You can invoke the nested skill by its qualified name: `run the frontend:deploy skill`.

### Closest .claude wins for configuration

For `agent`, `workflow`, and `output-style` settings, the `.claude/` directory closest to the current working directory takes precedence on collision, per the [v2.1.178 release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.178): "Nested `.claude/` directories: the agent, workflow, and output-style closest to the working directory now wins when names collide." This lets frontend, backend, and data subdirectories each carry their own output style or default agent without interfering with each other.

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

A bug in prior versions caused nested skills with directory-qualified names (`frontend:deploy`) to be blocked by permission prompts they couldn't fulfill in non-interactive mode (`claude -p "..."`). This is [fixed in 2.1.178](https://github.com/anthropics/claude-code/releases/tag/v2.1.178) ("Fixed nested `.claude/skills` skills being blocked by permission prompts"). CI pipelines that reference nested skills by qualified name should now work correctly.

---

## Auto Mode: Closing the Subagent Classifier Gap

### The previous gap

Auto mode routes Claude Code tool calls through a server-side classifier before each action fires; per [Anthropic's engineering write-up on auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode), the classifier runs a fast pass on every tool call and escalates to deeper chain-of-thought review when something looks risky, deciding whether a given action needs human approval or can proceed automatically.

However, before 2.1.178, *spawning a subagent* was not itself classified before the spawn completed. This is documented directly in the [v2.1.178 release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.178): "Improved auto mode: subagent spawns are now evaluated by the classifier before launch." The subagent was created first, and its actions were individually classified — but the spawn request itself could bypass the pre-launch check. This meant that in a carefully crafted scenario, a primary agent operating in auto mode could spawn a subagent configured to request actions the human had not reviewed.

### What changed

2.1.178 adds classifier pre-screening to subagent spawn requests. Before a subagent starts executing, the classifier evaluates the spawn — the same way [Anthropic describes it reviewing a subagent handoff](https://www.anthropic.com/engineering/claude-code-auto-mode) "at both ends: when work is delegated out and when results come back." If the spawn would trigger an action that requires human approval, the spawn is held pending confirmation.

In practice, this matters most for:

- **Agentic pipelines running unattended** where the primary agent has auto mode permissions but subagent behavior was an implicit trust escalation.
- **Deep agent chains** — [Claude Code 2.1.172](https://github.com/anthropics/claude-code/releases/tag/v2.1.172) added the ability for "sub-agents to spawn their own sub-agents (up to 5 levels deep)." Without classifier pre-screening of spawns, each nesting level was a potential gap.
- **Custom permission rules** that restrict the primary agent but were not being evaluated at spawn boundaries.

For most interactive users running a single session, the change is invisible. For teams that have built auto mode pipelines or are using agent orchestration, this closes a meaningful gap.

---

## Other Fixes Worth Noting

All four fixes below are listed in the [v2.1.178 release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.178).

**Subagent transcript** now shows tool results and live progress, not just the final response. If you were opening a subagent's transcript and seeing an empty or summary-only view, that is fixed.

**Messages dropped during subagent finish**: In prior versions, messages sent to Claude Code while a subagent was completing its last turn were silently dropped. Fixed in 2.1.178 — messages are now queued correctly.

**Custom API gateway 401**: Teams routing `claude agents` workers through a custom API gateway (`ANTHROPIC_BASE_URL`/`ANTHROPIC_AUTH_TOKEN`) were seeing `401 Invalid bearer token` errors. This is fixed.

**MCP disallowedTools in subagents**: MCP server-level specs (`mcp__server`, `mcp__server__*`, `mcp__*`) in a subagent's `disallowedTools` list were being silently ignored. Fixed — the specs now apply correctly.

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

1. **Review your permission rules** — if you have existing `allow`/`deny` lists, consider whether `Tool(param:value)` rules could tighten them. Common win: `Agent(model:claude-opus*)` as a deny rule to cap subagent model costs. For blocking credential reads, use Read's own path specifier rather than the generic parameter form — `Read(~/.ssh/*)` as a deny rule, not `Read(file_path:~/.ssh/*)`, since `file_path` is Read's excluded primary content field (see [permissions reference](https://code.claude.com/docs/en/permissions)).

2. **Audit nested .claude directories** — if your repo has subdirectories with `.claude/skills/`, verify the skill names are unique or decide on your qualified-name convention now (`frontend:deploy`, `backend:deploy`).

3. **Test CI pipelines using nested skills** — if you call a nested skill by its qualified `<dir>:<name>` form in non-interactive mode, the prior bug that blocked it behind an unfulfillable permission prompt is now fixed. Test that the correct skill runs.

4. **If you use auto mode in pipelines** — the subagent classifier gap fix is passive. No configuration change needed. But it is worth re-validating your permission rules now that spawn requests are also classified.

---

*Claude Code updates frequently. The prior Claude Code article in the Builder's Log covered [Auto Mode on Bedrock, Vertex, and Foundry (v2.1.158)](/builders-log/claude-code-auto-mode-bedrock-vertex-foundry-enterprise-builder-guide/) and [nested sub-agent depth (v2.1.172)](/builders-log/claude-code-nested-sub-agents-depth-5-token-math-builder-guide/).*

