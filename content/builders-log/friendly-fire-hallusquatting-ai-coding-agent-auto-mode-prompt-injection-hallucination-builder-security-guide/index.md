---
title: "Friendly Fire and HalluSquatting: One Flag Stands Between Your Dev Machine and Full Compromise"
description: "Two new attacks disclosed in July 2026 show that AI coding agents running in auto-mode can be weaponized — one by hiding prompt injections inside the repositories they're asked to review, the other by pre-registering the fake package names models predictably hallucinate. Here is how both work, what's still unfixed, and the three-step checklist that protects against both."
date: 2026-07-11
lastmod: 2026-07-11
slug: friendly-fire-hallusquatting-ai-coding-agent-auto-mode-prompt-injection-hallucination-builder-security-guide
tags:
  - security
  - claude-code
  - cursor
  - prompt-injection
  - hallucination
  - vulnerability
  - auto-mode
  - builder-guide
categories:
  - builders-log
---

If you ran through the GhostApproval story this week — the symlink attack that breaks workspace sandboxes in six AI coding tools — you might have figured that was the worst of it. It was not. The same seven-day window produced two additional disclosures that are distinct attack classes, require no symlinks, and aim at a different part of the AI coding workflow: the auto-approval modes you enable when you want the agent to just get on with it.

Both **Friendly Fire** and **HalluSquatting** were published in the week of July 7–11, 2026. Together they make the same argument: the single flag that turns off user approval prompts is where the attack surface lives.

---

## Friendly Fire (July 8, 2026 — AI Now Institute)

Researchers **Boyan Milanov** and **Heidy Khlaaf** at the AI Now Institute published a proof-of-concept they call Friendly Fire: a prompt injection attack that takes effect specifically when a developer points their AI coding agent at a third-party library and asks it to perform a security review.

### The scenario that gets hit

The scenario is common and reasonable: your team adopts an open-source dependency, security practice says run the AI over it before merging, so you type `review the security of this library`. That action, in Claude Code auto-mode or Codex auto-review, is the trigger.

### How the attack is constructed

The researchers modified a copy of **geopy**, a widely used Python geocoding library, adding three files:

- **`security.sh`** — A shell script embedded in or linked from the README, framed as a recommended pre-PR check.
- **`code_policies`** — A malicious binary carrying the actual payload. Compiled appearance, stripped, but seeded with strings.
- **`code_policies.go`** — A decoy Golang source file whose string values were copied into the binary to make Claude Code's disassembly check conclude that the binary was the compiled output of the harmless Go source.

The injection itself lives in **README.md**, an ordinary text file present in nearly every repository and granted no special trust level by any agent. The README contains a note that `security.sh` is a standard pre-merge step — conventional-sounding text that the agent reads and acts on.

When Claude Code or Codex reviews the modified geopy, the agent executes `security.sh`, which runs `code_policies`, which delivers the payload.

### What the models said when asked directly

Milanov and Khlaaf asked both Claude Sonnet 4.6 and GPT-5.5 a direct question: does this library contain any hidden instructions? Both said no. The injections were there. The models did not detect them.

### Cross-model portability

The payload was written for Claude Sonnet 4.6. With no modification, it worked on **Claude Sonnet 5**, **Claude Opus 4.8**, and **GPT-5.5 (Codex)**. The researchers tested all four; all four executed.

### Vendor response and fix status

Milanov and Khlaaf reported findings to both Anthropic and OpenAI before publication and offered support to reproduce. There is **no CVE**, **no coordinated patch date**, and **no PSIRT thread** on record. Neither vendor treats this as a security bug in the conventional sense: from the platform's point of view, the agent was doing what it was asked. The agent was also doing what the malicious repository wanted.

The researchers are direct: "The problem can't be fixed with a model update, because the models still can't reliably distinguish the code they're reading from the instructions they're supposed to be following."

---

## HalluSquatting (July 2026 — Tel Aviv University, Technion, Intuit)

A separate research group — from Tel Aviv University, the Technion, and Intuit — disclosed a different class of attack the same week. Where Friendly Fire pushes a payload into a repository and waits for a review, HalluSquatting works the other direction: it pre-registers the fake names that AI models will predictably invent, then waits for agents across the internet to come fetch them.

### The hallucination rate is the vulnerability

When asked to clone or install a popular repository, LLMs hallucinate the wrong location or name. The researchers measured:

- **"Clone a trending repository"** → hallucinated wrong location up to **85%** of the time
- **"Install a skill"** → hallucination rate **100%** — every tested model for every tested popular skill name

The hallucinations are not random. They follow predictable patterns based on how the training corpus described similar tools. That predictability is the attack surface.

### Pre-registration as the kill chain

An attacker runs the same prompts against a model, collects the hallucinated names, registers the corresponding GitHub repositories or package names before any legitimate owners do, and seeds those repositories with reverse-shell payloads, ransomware droppers, or DDoS agents. Then they wait.

Every developer who asks an AI coding agent to "install that popular MCP tool I saw on Twitter" is a potential victim. The agent fetches the attacker's repo, not the real one. The developer sees an install completing normally.

The researchers describe this as the **first pull-based prompt injection that scales**. Earlier prompt injection attacks had to be delivered to specific targets. HalluSquatting inverts the relationship: the attacker registers the trap and every AI agent that hallucinates the same name delivers itself.

### Tools confirmed affected

The researchers demonstrated the technique against nine AI coding tools: **Cursor**, **Cursor CLI**, **Gemini CLI**, **Windsurf**, **GitHub Copilot**, **Cline**, **OpenClaw**, **ZeroClaw**, and **NanoClaw**. The common exposure is auto-run modes — the same class of setting as Claude Code's `--skip-permissions` flag and Gemini CLI's `--yolo` mode — that remove the default prompt before executing commands.

### Platform-level defenses

The research identifies two platform-side mitigations: prevent reuse of well-known repository names under newly created accounts (the same defense already deployed against typosquatting), and pre-register the names that models are statistically likely to hallucinate. Neither of these is something a developer can do unilaterally.

---

## The common thread: auto-mode is the attack surface

All three July 2026 disclosures — GhostApproval, Friendly Fire, and HalluSquatting — share the same root condition: the agent has permission to act without asking first.

GhostApproval requires the agent to write files the repository instructs it to write. Friendly Fire requires the agent to execute the security check the README recommends. HalluSquatting requires the agent to install the package it looked up. In every case, a human in the loop reviewing the proposed action would have a reasonable chance of catching it. In every case, auto-approval removes that review.

The flags that enable this — Claude Code's `--dangerously-skip-permissions`, Gemini CLI's `--yolo`, Codex's `--auto-review`, Cursor and Windsurf's equivalent "just do it" modes — exist because they make legitimate workflows significantly faster. They will not go away. The question is which workflows justify them.

---

## Builder action checklist

**For Friendly Fire (untrusted code review):**
- Do not run Claude Code or Codex in auto-mode against repositories you did not author or thoroughly trust
- Use a separate sandboxed environment (container, VM) without production credentials when reviewing third-party dependencies
- Do not count on AI agents to reliably detect their own prompt injections — the research showed direct questioning failed on all four tested models
- If your organization deploys Claude Code via enterprise managed settings, use the policy to disable auto-mode for code review workflows

**For HalluSquatting (hallucinated package installs):**
- Never use `--skip-permissions`, `--yolo`, or equivalent modes when installing packages or cloning repositories sourced from AI suggestions
- Always verify a package or repository name independently before installation — search for it directly, do not trust the URL or name the model provides
- Treat "install this for me" as an operation that requires human confirmation regardless of the tool
- For MCP servers: verify the server source via the project's official documentation or registry, not from an LLM-generated reference

**General:**
- Auto-mode is appropriate for tasks within your own codebase, on code you own and understand
- Auto-mode against untrusted external code is a different risk profile — treat it as if you're running an installer from an unknown source

---

## What has and hasn't been patched

| Disclosure | Affected tool | Status as of July 11, 2026 |
|---|---|---|
| GhostApproval | Amazon Q Developer | Patched (language server v1.69.0, CVE-2026-12958) |
| GhostApproval | Cursor | Patched (v3.0, CVE-2026-50549) |
| GhostApproval | Claude Code | No patch — acknowledged as design gap |
| GhostApproval | Google Antigravity | No confirmed patch |
| GhostApproval | Windsurf | Acknowledged June 23, no update since |
| GhostApproval | Augment | "In progress," no timeline |
| Friendly Fire | Claude Code, Codex | No CVE, no patch, no timeline — vendors consider this expected behavior |
| HalluSquatting | Cursor, Copilot, Windsurf + 6 others | No patches — platform-level mitigations required |

All three attacks require intentional setup by an attacker: a crafted repository, a pre-registered hallucinated name, or a symlinked file. They are not passive — a clean, internal workflow with no untrusted external code in the loop is not at risk. The risk concentrates on the workflows where AI agents meet code they did not originate.

That covers a lot of developer workflows in 2026. The honest mitigation is to audit which of yours have auto-mode on and why.
