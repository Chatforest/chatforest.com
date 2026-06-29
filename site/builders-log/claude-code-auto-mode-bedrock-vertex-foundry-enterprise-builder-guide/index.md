# Claude Code Auto Mode Lands on Bedrock, Vertex, and Foundry

> Claude Code v2.1.158 extends Auto mode beyond the direct Anthropic API to Amazon Bedrock, Google Vertex AI, and Microsoft Azure Foundry. Here's what changed, how to enable it, and why this matters for enterprise builders running Claude Code on managed cloud infrastructure.


Claude Code v2.1.158, released in late May/early June 2026, extended Auto mode to Amazon Bedrock, Google Vertex AI, and Microsoft Azure Foundry. Previously, Auto mode required the direct Anthropic API. Enterprise teams that route Claude through managed cloud providers — for data residency, MACC spend, or security policy compliance — can now use the same unattended agent behavior that was previously off-limits to them. Part of our **[Builder's Log](/builders-log/)**.

---

## What Auto Mode Does

Auto mode is Claude Code's mechanism for reducing permission friction on repetitive, low-risk tool calls. In normal operation, Claude Code prompts for approval before each significant action: file write, terminal command, API call. For interactive sessions with a human in the loop, that's often correct. For long-running autonomous tasks — overnight migrations, CI-integrated code review pipelines, continuous test harnesses — it's friction that breaks automation.

With Auto mode on, Claude Code passes each pending action through a server-side classifier before showing it to the user. Actions the classifier categorizes as low-risk and reversible (reading files, running read-only commands, making edits within a bounded scope) proceed without a prompt. Actions the classifier flags as higher-risk or potentially irreversible (deleting data, pushing to remote, modifying configuration outside the working tree) still require explicit approval.

When the classifier blocks an action, it returns a denial reason. Claude uses that reason to decide whether to retry with a different approach, ask the user for clarification, or stop and report. This is meaningfully different from just removing the approval step — it keeps Claude in a reasoning loop rather than blindly blocking or bypassing.

The practical result: you can dispatch a Claude Code session against a multi-hour task, step away, and return to either a completed diff or a specific approval request — rather than an idle session waiting at a prompt fifteen minutes into a three-hour job.

---

## The Gap This Closes

Before v2.1.158, Auto mode required Anthropic's direct API. That excluded a large segment of enterprise Claude Code users.

Enterprise teams often cannot use the direct API for Claude Code. The reasons are familiar: MACC spend commitments on Azure, data residency requirements that route traffic through Bedrock or Vertex, corporate policies that mandate managed cloud services, or existing Anthropic contracts structured around Bedrock or Foundry. These teams could use Claude Code — but only in its interactive, human-in-the-loop configuration.

Effective with v2.1.158:

| Platform | Auto Mode Available | Models Required |
|---|---|---|
| Anthropic API (direct) | Yes (before v2.1.158) | Opus 4.7 or 4.8 |
| Amazon Bedrock | **Now yes** | Opus 4.7 or 4.8 |
| Google Vertex AI | **Now yes** | Opus 4.7 or 4.8 |
| Microsoft Azure Foundry | **Now yes** | Opus 4.7 or 4.8 |

Earlier Claude versions on these platforms (Opus 4.6 and below) do not support Auto mode.

---

## How to Enable It

Auto mode is opt-in. It does not activate when you update to v2.1.158. You must explicitly set an environment variable:

```bash
export CLAUDE_CODE_ENABLE_AUTO_MODE=1
```

For CI pipelines and Docker-based environments, add this to your environment configuration or service account context. For local developer machines running Claude Code against Bedrock or Vertex, set it in your shell profile if you want it persistent.

Two additional conditions must be met alongside the env var:

1. **Model:** Your Claude Code session must be using Claude Opus 4.7 or Opus 4.8. Auto mode does not activate on earlier models. If you're on a Bedrock model ARN that resolves to an older version, you'll need to update your configuration.

2. **Cloud target:** Your Claude Code configuration must point to one of the supported providers (Bedrock, Vertex, Foundry, or the direct Anthropic API). Auto mode doesn't do anything for unsupported backends.

To verify Auto mode is active, run `/usage` inside a Claude Code session — you'll see the mode reflected in the session summary.

---

## What the Classifier Actually Checks

The denial reasons Auto mode returns give you a window into what the classifier evaluates. Enterprise builders who have been testing it report denials (action blocks requiring explicit approval) for:

- Git push or force push to remote branches
- Deleting files outside the current working tree
- Modifying files listed in `.autoignore` or matching `.gitignore` patterns that weren't explicitly added to the session's scope
- Executing commands that touch `/etc`, `/var`, or system directories
- Installing packages system-wide (as opposed to into a virtual environment or local node_modules)
- Making network requests to addresses outside the project's known API endpoints

The classifier is not an allow/deny list you configure — it runs server-side and applies a model-based risk assessment to each pending action. Denial reasons are plain language ("This action would push to a remote branch — approval required"), which Claude can then reference in its retry or escalation reasoning.

---

## Other Changes in v2.1.156–2.1.158

The Auto mode cloud extension is the headline change, but the patch window that produced v2.1.158 included several companion features worth noting.

**Skills auto-load from `.claude/skills` (v2.1.157).** Plugins placed in the `.claude/skills` directory of your repository are now loaded automatically when Claude Code starts in that project — no marketplace registration required. Previously, distributing a project-specific skill to team members required either marketplace publishing or manual `/skill add` steps. Now you drop the skill into the directory, commit it, and every team member who opens Claude Code in that repo gets it automatically.

Combined with the new `claude plugin init <name>` command (also v2.1.157), which generates a fully structured plugin template, this is effectively a local skills distribution system for teams.

**The `agent` field in `settings.json` applies in dispatched sessions (v2.1.157).** When Claude Code dispatches a sub-agent (via the `Agent` tool or background session dispatch), the `agent` field in your `settings.json` now propagates to the dispatched session. Before this fix, dispatched sessions used default agent configuration regardless of what the parent session had configured. For teams using `settings.json` to standardize agent personas, tool permissions, or skill sets across sessions, this closes an inconsistency that could cause dispatched agents to behave differently from the parent.

The `--agent <name>` flag overrides the `settings.json` agent field at the CLI level if you need per-dispatch customization.

**`EnterWorktree` allows mid-session worktree switching (v2.1.158).** Previously, `EnterWorktree` was an entry-point operation — you used it to start a session in a specific worktree, but switching worktrees mid-session wasn't supported. v2.1.158 makes it available during a session, so Claude can move between Claude-managed worktrees without ending and restarting the session. For agentic workflows where one session needs to work across multiple feature branches simultaneously, this removes a hard constraint.

**Thinking block bug fix (v2.1.156).** A bug where thinking blocks were incorrectly modified under Opus 4.8 caused API errors in some session configurations. This was fixed in v2.1.156. If you've seen unexplained API errors in Opus 4.8 sessions in the past two weeks, updating past v2.1.156 should resolve them.

---

## What This Means for Enterprise Deployment

The Auto mode expansion to Bedrock, Vertex, and Foundry removes the primary reason enterprise teams couldn't use Claude Code for fully autonomous workloads. The core use cases that become practical:

**Overnight batch work.** A Claude Code session can run a large-scale migration, refactor, or analysis job autonomously, presenting a diff and a summary when you arrive in the morning rather than an idle session that stopped at the first approval request.

**CI/CD integration.** Auto mode enables Claude Code to run as a CI step — code review, documentation updates, test coverage gaps — without a human watching. The classifier handles risk gating; the denial-reason feedback loop handles edge cases.

**Multi-agent orchestration.** Background sessions running under Auto mode can be dispatched by a parent Claude Code session and report back without requiring manual approvals on each child's tool calls. Combined with the `agent` field fix in dispatched sessions, multi-agent pipelines on Bedrock/Vertex/Foundry are now more tractable.

The one thing to watch: Auto mode's classifier is a tool for reducing friction on genuinely low-risk operations. It is not a replacement for scoping sessions carefully. If you dispatch a Claude Code session with broad filesystem access and a vague task description, Auto mode will not save you from unintended side effects — the classifier works best when the session's scope is bounded and the task is specific. Start with narrow scope, verify behavior, then expand.

---

*Claude Code v2.1.158 is available via `npm update -g @anthropic-ai/claude-code` or the Claude desktop app auto-update. Release notes: [GitHub Releases](https://github.com/anthropics/claude-code/releases/tag/v2.1.158).*

