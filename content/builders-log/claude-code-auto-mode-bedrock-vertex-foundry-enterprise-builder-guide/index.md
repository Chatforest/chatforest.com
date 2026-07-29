---
title: "Claude Code Auto Mode Lands on Bedrock, Vertex, and Foundry"
date: 2026-06-11
description: "Claude Code v2.1.158 extends Auto mode beyond the direct Anthropic API to Amazon Bedrock, Google Vertex AI, and Microsoft Azure Foundry. Here's what changed, how to enable it, and why this matters for enterprise builders running Claude Code on managed cloud infrastructure."
og_description: "Claude Code Auto mode now runs on Bedrock, Vertex, and Foundry — not just the direct Anthropic API. v2.1.158 also adds skills auto-loading, a new plugin init command, and agent-field dispatch fixes. Here's what enterprise builders need to know."
content_type: "Builder's Log"
categories: ["Anthropic", "Claude Code", "Developer Tools", "Enterprise"]
tags: ["anthropic", "claude-code", "auto-mode", "bedrock", "vertex-ai", "azure-foundry", "enterprise", "opus-4-8", "agent-sdk", "june-2026", "builders-log"]
sources_audited: 2026-07-30
---

[Claude Code v2.1.158](https://github.com/anthropics/claude-code/releases/tag/v2.1.158), released May 30, 2026, extended [Auto mode](https://claude.com/blog/auto-mode) to Amazon Bedrock, Google Vertex AI, and Microsoft Azure Foundry — gated behind an opt-in environment variable rather than on by default. Anthropic's [Auto mode configuration docs](https://code.claude.com/docs/en/auto-mode-config) confirm that opt-in requirement applied specifically "in v2.1.158 through v2.1.206," and was later removed. Enterprise teams that route Claude through managed cloud providers — for data residency, MACC spend, or security policy compliance — can now use the same unattended agent behavior that was previously off-limits to them. Part of our **[Builder's Log](/builders-log/)**.

---

## What Auto Mode Does

Auto mode is Claude Code's mechanism for reducing permission friction on repetitive, low-risk tool calls. In normal operation, Claude Code prompts for approval before each significant action: file write, terminal command, API call. For interactive sessions with a human in the loop, that's often correct. For long-running autonomous tasks — overnight migrations, CI-integrated code review pipelines, continuous test harnesses — it's friction that breaks automation.

With Auto mode on, Claude Code passes each pending action through a [server-side classifier](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) before showing it to the user. Per [Anthropic's engineering writeup on Auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode), low-risk actions — file reads, searches, code navigation, and in-project edits — bypass the classifier entirely, while higher-risk actions such as shell commands, external API calls, filesystem operations outside the project, and credential access are routed to it for review.

When the classifier blocks an action, [it returns a denial reason](https://www.anthropic.com/engineering/claude-code-auto-mode) — "along with an instruction to treat the boundary in good faith: find a safer path," in Anthropic's words. Claude uses that reason to decide whether to retry with a different approach, ask the user for clarification, or stop and report. This is meaningfully different from just removing the approval step — it keeps Claude in a reasoning loop rather than blindly blocking or bypassing.

The practical result: you can dispatch a Claude Code session against a multi-hour task, step away, and return to either a completed diff or a specific approval request — rather than an idle session waiting at a prompt fifteen minutes into a three-hour job.

---

## The Gap This Closes

Before v2.1.158, Auto mode required Anthropic's direct API. That excluded a large segment of enterprise Claude Code users.

Enterprise teams often cannot use the direct API for Claude Code. The reasons are familiar: MACC spend commitments on Azure, data residency requirements that route traffic through Bedrock or Vertex, corporate policies that mandate managed cloud services, or existing Anthropic contracts structured around Bedrock or Foundry. These teams could use Claude Code — but only in its interactive, human-in-the-loop configuration.

Effective with [v2.1.158](https://github.com/anthropics/claude-code/releases/tag/v2.1.158), whose release notes state: "Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8. Opt in by setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`":

| Platform | Auto Mode Available | Models Required |
|---|---|---|
| Anthropic API (direct) | Yes (before v2.1.158) | Opus 4.7 or 4.8 |
| Amazon Bedrock | **Now yes** | Opus 4.7 or 4.8 |
| Google Vertex AI | **Now yes** | Opus 4.7 or 4.8 |
| Microsoft Azure Foundry | **Now yes** | Opus 4.7 or 4.8 |

Earlier Claude versions on these platforms (Opus 4.6 and below) do not support Auto mode.

---

## How to Enable It

On these three platforms, [Auto mode was opt-in as of v2.1.158](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode). It does not activate when you update to v2.1.158. You must explicitly set an environment variable:

```bash
export CLAUDE_CODE_ENABLE_AUTO_MODE=1
```

For CI pipelines and Docker-based environments, add this to your environment configuration or service account context. For local developer machines running Claude Code against Bedrock or Vertex, set it in your shell profile if you want it persistent. (Anthropic's [current documentation](https://code.claude.com/docs/en/auto-mode-config) notes this opt-in requirement was later removed in v2.1.207, and the env var is now a no-op kept only for compatibility.)

Two additional conditions must be met alongside the env var:

1. **Model:** Your Claude Code session must be using Claude Opus 4.7 or Opus 4.8, [per the v2.1.158 release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.158). Auto mode does not activate on earlier models. If you're on a Bedrock model ARN that resolves to an older version, you'll need to update your configuration.

2. **Cloud target:** Your Claude Code configuration must point to one of the supported providers (Bedrock, Vertex, Foundry, or the direct Anthropic API). Auto mode doesn't do anything for unsupported backends.

To verify Auto mode is active, check the CLI status bar rather than any slash command: Anthropic's [permission-modes documentation](https://code.claude.com/docs/en/permission-modes#switch-permission-modes) states it displays `⏵⏵ auto mode on`, and you can cycle into it with Shift+Tab when your account meets the requirements above.

---

## What the Classifier Actually Checks

The denial reasons Auto mode returns give you a window into what the classifier evaluates. Anthropic's documentation on [what the classifier blocks by default](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) lists, among the baseline (non-version-gated) rules:

- Force push
- Irreversibly destroying files that existed before the session
- Downloading and executing code, such as `curl | bash`
- Sending sensitive data to external endpoints
- `terraform destroy`, `pulumi destroy`, `cdk destroy`, or `terragrunt destroy`
- `git commit --amend` when the commit at HEAD wasn't created in this session
- Production deploys and migrations, mass deletion on cloud storage, and granting IAM or repo permissions

At the time of v2.1.158, this classifier ran server-side with a fixed built-in rule set rather than an org-configurable allow/deny list — the `autoMode.environment`/`allow`/`soft_deny` settings that let teams customize it were added in later releases (v2.1.195 and after, per the same documentation). Denials come back to Claude as plain-language reasons it can reference in its retry or escalation reasoning.

---

## Other Changes in v2.1.156–2.1.158

The Auto mode cloud extension is the headline change, but the patch window that produced v2.1.158 included several companion features worth noting.

**Skills auto-load from `.claude/skills` ([v2.1.157](https://github.com/anthropics/claude-code/releases/tag/v2.1.157)).** Per the release notes, "Plugins in `.claude/skills` directories are now automatically loaded, no marketplace required." Previously, distributing a project-specific skill to team members required either marketplace publishing or manual `/skill add` steps. Now you drop the skill into the directory, commit it, and every team member who opens Claude Code in that repo gets it automatically.

Combined with the new `claude plugin init <name>` command (also [v2.1.157](https://github.com/anthropics/claude-code/releases/tag/v2.1.157)), which scaffolds a new plugin in `.claude/skills`, this is effectively a local skills distribution system for teams.

**The `agent` field in `settings.json` applies in dispatched sessions ([v2.1.157](https://github.com/anthropics/claude-code/releases/tag/v2.1.157)).** When Claude Code dispatches a sub-agent (via the `Agent` tool or background session dispatch), the `agent` field in your `settings.json` now propagates to the dispatched session, with `--agent <name>` available to override it. Before this fix, dispatched sessions used default agent configuration regardless of what the parent session had configured. For teams using `settings.json` to standardize agent personas, tool permissions, or skill sets across sessions, this closes an inconsistency that could cause dispatched agents to behave differently from the parent.

**`EnterWorktree` allows mid-session worktree switching ([v2.1.157](https://github.com/anthropics/claude-code/releases/tag/v2.1.157), not v2.1.158).** The release notes state: "`EnterWorktree` can now switch between Claude-managed worktrees mid-session." Previously, switching worktrees mid-session wasn't supported — a session had to end and restart to move to a different Claude-managed worktree. For agentic workflows where one session needs to work across multiple feature branches, this removes a hard constraint.

**Thinking block bug fix ([v2.1.156](https://github.com/anthropics/claude-code/releases/tag/v2.1.156)).** The release notes read: "Fixed an issue when using Opus 4.8 where thinking blocks were modified, leading to API errors." If you've seen unexplained API errors in Opus 4.8 sessions in the past two weeks, updating past v2.1.156 should resolve them.

---

## What This Means for Enterprise Deployment

The Auto mode expansion to Bedrock, Vertex, and Foundry removes the primary reason enterprise teams couldn't use Claude Code for fully autonomous workloads. The core use cases that become practical:

**Overnight batch work.** A Claude Code session can run a large-scale migration, refactor, or analysis job autonomously, presenting a diff and a summary when you arrive in the morning rather than an idle session that stopped at the first approval request.

**CI/CD integration.** Auto mode enables Claude Code to run as a CI step — code review, documentation updates, test coverage gaps — without a human watching. The classifier handles risk gating; the denial-reason feedback loop handles edge cases.

**Multi-agent orchestration.** Background sessions running under Auto mode can be dispatched by a parent Claude Code session and report back without requiring manual approvals on each child's tool calls. Combined with the `agent` field fix in dispatched sessions, multi-agent pipelines on Bedrock/Vertex/Foundry are now more tractable.

The one thing to watch: Auto mode's classifier is a tool for reducing friction on genuinely low-risk operations. It is not a replacement for scoping sessions carefully. If you dispatch a Claude Code session with broad filesystem access and a vague task description, Auto mode will not save you from unintended side effects — the classifier works best when the session's scope is bounded and the task is specific. Start with narrow scope, verify behavior, then expand.

---

*Claude Code v2.1.158 is available via `npm update -g @anthropic-ai/claude-code` or the Claude desktop app auto-update. Release notes: [GitHub Releases](https://github.com/anthropics/claude-code/releases/tag/v2.1.158).*
