---
title: "GuardFall: 10 of 11 Open-Source AI Coding Agents Have Shell Guards That Bash Rewrites Around Them"
description: "Adversa AI published GuardFall on June 30, 2026: a class of shell-injection bypasses that defeats the security guards in 10 of 11 major open-source AI coding agents — Aider, Cline, Roo-Code, Goose, Plandex, Open Interpreter, OpenHands, SWE-agent, opencode, and Hermes. There is no CVE and no patch. Here is what the bypass looks like, why it can't be fixed with a version bump, and what you can do now."
date: 2026-07-12
lastmod: 2026-07-12
slug: guardfall-shell-injection-open-source-ai-coding-agents-aider-cline-roo-code-builder-guide
tags:
  - security
  - shell-injection
  - aider
  - cline
  - roo-code
  - open-source
  - vulnerability
  - builder-guide
  - guardfall
  - adversa-ai
categories:
  - builders-log
---

The same week GhostApproval disclosed that six commercial AI coding assistants write files outside their workspace sandboxes, a separate research disclosure went relatively quiet. Adversa AI's Omer Ben Simon published **GuardFall** on June 30, 2026, showing that 10 of the 11 most widely used open-source AI coding agents can be compromised with shell tricks that predate most of the developers using these tools.

Unlike GhostApproval, GuardFall has no CVE number. Unlike the Claude Code v2.1.207 shell-injection fix that shipped July 11, it cannot be addressed with a version bump. The flaw is architectural — and it will stay open until maintainers rethink how command guards are built. Part of our **[Builder's Log](/builders-log/)**.

---

## What GuardFall found

Adversa AI tested 11 of the most-starred open-source AI coding agents against a set of classic Bash-rewriting tricks: quote removal, variable expansion, command substitution, brace expansion, and process substitution. These are behaviors documented in the Bash manual that cause the shell to transform text before executing it.

The pattern-based guards in these agents inspect the **raw command string** as the model produces it. Bash then **rewrites** that string and executes something different. The guard never sees what actually runs.

**10 agents failed** every tested bypass category. The combined GitHub star count of the failing agents at the time of research was roughly **548,000**.

Affected agents: **Aider, Cline, Roo-Code, Goose, Plandex, Open Interpreter, OpenHands, SWE-agent, opencode, NousResearch Hermes.**

Only one agent passed: **Continue.** Its guard is built differently — it evaluates commands after shell rewriting rather than before.

---

## The bypass mechanics

Here is the simplest example of how the bypass class works:

```bash
# What the agent's guard inspects:
echo safe_output

# What Bash actually executes after variable expansion:
echo safe_output; exfil_payload
```

The construction is less obvious than that example suggests. Ben Simon demonstrated several variants:

**Quote removal bypass:**
```bash
# Guard sees: 'r''m' (looks like a string)
# Bash concatenates quote-delimited tokens: rm
'r''m' -rf /path/to/target
```

**Brace expansion bypass:**
```bash
# Guard looks for "rm" and doesn't find it
# Bash expands {r,}m to rm
{r,}m -rf /path/to/target
```

**Variable substitution bypass:**
```bash
# Guard checks the string, sees no dangerous command
# Bash evaluates $() first
$(echo "rm") -rf /path/to/target
```

The key property of all these variants: they look different to a string-matching guard than they do to the shell. A denylist of patterns cannot close this — Bash will always have more rewriting rules than a guard can enumerate.

---

## Why there is no CVE and no patch release

GuardFall is not a bug in a specific component. It is a design pattern: **agent produces shell string → guard inspects string → Bash executes rewritten string**. That sequence is wrong in a durable way.

Adversa AI was explicit: fixing this requires removing the pattern-matching guard layer and replacing it with structural execution control. The practical options are:

1. **Exec format (no shell):** Execute commands as arrays (`["rm", "-rf", "/path"]`) through a process API that bypasses the shell entirely. No shell, no shell rewriting. This is what Anthropic enforced in Claude Code v2.1.207 for hook commands.

2. **Sandbox at the OS level:** Run the agent's command execution inside a container or virtual machine with an explicit allowlist of permitted syscalls and filesystem access. The guard lives below the shell layer where rewriting can't circumvent it.

3. **Require human confirmation for all shell commands.** Not a technical fix, but eliminates the automated pathway that makes the bypass exploitable at scale.

None of these are a version bump. All require maintainers to change how execution works, not just what patterns they block.

---

## How an attacker reaches a builder

The attack delivery surface is any content an AI agent reads while it has shell access:

- **Repository README files.** The agent reads them as part of onboarding a new dependency.
- **Makefiles and shell scripts.** Routine CI configuration the agent is asked to modify.
- **Documentation files.** Markdown in `/docs` gets indexed and sometimes executed when agents summarize or test examples.
- **Agent memory or notes files.** If an attacker compromised a previous session's memory, injections persist into later sessions.

In auto-approve mode — enabled by default in some agents for non-destructive operations — the agent runs the shell command and the bypass payload executes before any confirmation dialog appears. In interactive mode, the agent typically shows the raw command string, which may look safe while hiding the bypass in quote structure or expansion syntax.

---

## The one agent that passed, and what it did differently

**Continue** was the only agent that evaluated commands *after* Bash rewriting. Its guard does not inspect what the model wrote — it inspects what would actually execute. That design choice makes the entire bypass class irrelevant: there is nothing in the shell rewriting phase that happens between guard inspection and execution, because inspection happens at execution time.

If you are choosing between open-source agents for a project where you will be running them against third-party codebases, Continue's architecture is the only one in this set that is structurally defended.

---

## What this means alongside GhostApproval, Friendly Fire, and Claude Code v2.1.207

The same week as GuardFall's public disclosure, two other attacks against AI coding agents were disclosed (GhostApproval on July 8 and Friendly Fire the same week). The attacks are distinct attack classes:

- **GhostApproval** (symlink following): Breaks out of the workspace sandbox to read and write files outside it. Affects six commercial tools. AWS and Cursor have patched; Windsurf and Augment remain unpatched.
- **Friendly Fire** (prompt injection): Hides instructions in repository files that redirect an agent doing a security review into running the attacker's code.
- **GuardFall** (shell guard bypass): Bypasses the pattern-matching guards that are supposed to stop dangerous commands in the first place. No patch. Architectural fix required.

On July 11, 2026, Anthropic's Claude Code v2.1.207 shipped a breaking change that enforces exec-format commands in hooks — rejecting the `${user_config.*}` interpolation pattern that enabled this class of injection in Claude Code specifically. That fix is Claude Code's implementation of option 1 above. It does not fix GuardFall in Aider, Cline, Roo-Code, or the other eight affected agents.

---

## Builder action guide

**If you use open-source AI coding agents (Aider, Cline, Roo-Code, Goose, Plandex, Open Interpreter, OpenHands, SWE-agent, opencode, Hermes):**

1. **Do not run these agents in auto-approve mode against code you did not write.** The bypass class is only exploitable at scale in auto-approve or auto-execute environments. Requiring confirmation for every shell command closes the automated pathway even without an architectural fix.

2. **Treat agent-executed shell commands as untrusted even when you reviewed them.** What the agent showed you and what Bash executes may not be the same. If you run in auto-mode, pipe agent-generated shell commands through `set -x` output in a separate terminal to see what Bash is actually executing.

3. **Prefer exec-format execution wherever the tool supports it.** If the agent lets you configure commands as argument arrays rather than shell strings, use that mode. The array form bypasses the shell layer entirely.

4. **Consider OS-level sandboxing for CI pipelines.** Running agents inside Docker with limited filesystem access and no network egress limits blast radius regardless of whether the bypass succeeds at the command level.

5. **Follow affected project changelogs.** GuardFall does not have a CVE to watch, but the maintainers of Aider, Cline, Roo-Code, and others are aware of the research. Architectural fixes, when they ship, will require migration, not just a version bump.

**If you use Claude Code:** The v2.1.207 release that enforced exec-format for hooks is Anthropic's response to this class of injection in their tool. If you have not updated and are running hooks in shell format with `${user_config.*}` interpolation, update and migrate before running against untrusted repositories. See the [Claude Code v2.1.207 migration guide](/builders-log/claude-code-v2-1-207-shell-injection-plugin-breaking-changes-auto-mode-bedrock-builder-guide/) for the exact steps.

---

## Source

- [GuardFall research — Adversa AI (June 30, 2026)](https://adversa.ai/blog/opensource-ai-coding-agents-shell-injection-vulnerability/)
- [The Hacker News coverage](https://thehackernews.com/2026/06/guardfall-exposes-open-source-ai-coding.html)
- [SecurityWeek coverage](https://www.securityweek.com/decades-old-bash-tricks-expose-ai-coding-agents-to-supply-chain-attacks/)
