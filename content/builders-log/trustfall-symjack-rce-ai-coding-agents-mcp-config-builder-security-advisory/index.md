---
title: "TrustFall and SymJack: Two RCE Classes That Hit Every Major AI Coding Agent"
date: 2026-06-13
description: "Adversa AI disclosed two independent RCE attack classes in May 2026 — TrustFall and SymJack — affecting Claude Code, Cursor, Gemini CLI, GitHub Copilot CLI, and OpenAI Codex CLI. Both exploit MCP config handling. Here's what builders need to know."
og_description: "TrustFall plants malicious MCP servers in repo configs. SymJack symlink-hijacks MCP config directories at restart. Both achieve unauthenticated RCE across every major AI coding CLI — and only one vendor has hardened against either. Understand the attack surface before you clone another repo."
content_type: "Builder's Log"
categories: ["Security", "MCP", "Developer Tools", "AI Agents"]
tags: ["trustfall", "symjack", "adversa-ai", "rce", "mcp", "claude-code", "cursor", "gemini-cli", "codex-cli", "copilot", "security", "supply-chain", "ai-builders", "cve"]
sources_audited: 2026-07-30
---

In May 2026, Adversa AI published two independent vulnerability disclosures — **TrustFall** and **SymJack** — that together demonstrate a systemic weakness in how AI coding agents handle MCP configuration. Both classes achieve remote code execution. Both affect the tools you're likely using every day.

This article covers what each attack does, which tools are affected, what patches exist, and how builders should think about their exposure.

---

**Update — June 14, 2026:** Vendor response has settled into a pattern. Anthropic **rejected TrustFall itself**, telling researchers the trust-prompt UX is "outside its threat model" ([The Register](https://www.theregister.com/security/2026/05/07/claude-code-trust-prompt-can-trigger-one-click-rce/5235319)) — but weeks after SymJack's disclosure it quietly hardened Claude Code's approval flow so the prompt now displays the real resolved path instead of the symlink path ([SecurityWeek](https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/)). No other vendor patched either attack class. Google (Gemini CLI / Antigravity CLI) rejected the SymJack report as intended behavior, and Cursor **declined**, saying they already knew about the issue ([SecurityWeek](https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/)). xAI (Grok Build) and GitHub Copilot CLI gave **no response** to researchers. OpenAI had the Codex CLI report **closed by Bugcrowd as a false positive**, characterizing the attack as "theoretical" because the user approves the underlying `cp` command — ignoring that the symlink redirection is invisible to the user at approval time ([Adversa AI](https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/)). The table below reflects these outcomes. Builders using any unpatched tool should assume no vendor mitigation is forthcoming and apply the hardening steps below.

---

## Background: Why AI Coding CLIs Are a Target Now

AI coding agents — Claude Code, Cursor, Gemini CLI, Copilot CLI, Codex CLI — have all adopted MCP as a primary integration layer. MCP servers run as local processes that the agent launches on startup. They have access to files, shell commands, APIs, and whatever secrets the developer's environment carries.

The attack surface follows from this model: **if an attacker can control which MCP server gets executed, they own the machine**.

Adversa AI's research ([TrustFall](https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/), [SymJack](https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/)) identified two paths to that outcome. They operate at different layers and require different mitigations.

---

## TrustFall — One-Click RCE via Project-Embedded MCP Config

**Disclosed:** May 7, 2026 ([Adversa AI](https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/); [The Register](https://www.theregister.com/security/2026/05/07/claude-code-trust-prompt-can-trigger-one-click-rce/5235319))  
**CVE:** None assigned — Anthropic reviewed and rejected the report as outside its threat model (see "Anthropic's Response" below)  
**Affected:** Claude Code, Cursor CLI, Gemini CLI, GitHub Copilot CLI

### The Attack

Modern AI coding CLIs auto-discover MCP servers from config files stored in project directories — typically `.mcp.json` or equivalent. When a user opens a cloned repository and accepts the folder trust prompt, the CLI reads the project's MCP configuration and launches the servers listed there.

TrustFall exploits this directly: a malicious actor plants a `.mcp.json` in a repository that points to an attacker-controlled MCP server. The builder clones the repo, accepts the trust prompt — which frames the question as "do you trust this folder to run code?" without clearly disclosing it will launch network-connected processes — and execution begins.

The user sees one prompt. The CLI executes potentially arbitrary MCP server code on their machine.

### Related: The Miasma Worm

Separately — and documented by other security researchers, not Adversa AI — a self-replicating supply-chain campaign called the **Miasma worm** used a compromised maintainer credential to push malicious commits into Microsoft's Azure `durabletask` package and dozens of other repositories, eventually forcing GitHub to disable 73 Microsoft repos ([The Hacker News](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html); [StepSecurity](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents)). Miasma's payloads targeted AI-coding-agent auto-run surfaces broadly — MCP config files among them, alongside `.cursorrules`, `.windsurfrules`, and Copilot instruction files — to trigger credential-harvesting when a compromised repo was opened in Claude Code, Gemini CLI, Cursor, and other tools.

Miasma is a broader, multi-vector worm; it is not a confirmed exploitation of TrustFall specifically. But it's independent evidence that config-triggered execution on repo-open is already being abused in the wild, not merely a theoretical risk.

### Anthropic's Response

Anthropic did not patch TrustFall. Per Adversa AI's report and reporting by The Register, Anthropic's position is that once a user accepts the folder-trust dialog, the resulting code execution is a user trust decision and therefore "outside its threat model" — the company treats the behavior as by design, not a vulnerability ([The Register](https://www.theregister.com/security/2026/05/07/claude-code-trust-prompt-can-trigger-one-click-rce/5235319); [Adversa AI](https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/)).

That said, Claude Code had already patched three related trust-boundary bugs in the same problem class before TrustFall's disclosure — cited by Adversa as prior precedent, not as TrustFall's own CVEs: **CVE-2025-59536** (a project-scoped MCP server could execute before the trust dialog even rendered, patched September 2025), **CVE-2026-21852** (a malicious `ANTHROPIC_BASE_URL` in a repo's committed settings could exfiltrate the user's API key before the trust prompt was confirmed, patched December 2025), and **CVE-2026-33068** (a repo-controlled settings file could silently bypass the trust dialog by setting `permissions.defaultMode`, patched in v2.1.53, disclosed March 2026) ([Check Point Research](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/); [GitLab Advisory Database](https://advisories.gitlab.com/npm/@anthropic-ai/claude-code/CVE-2026-33068/)). These are separate, earlier bugs — not patches issued in response to TrustFall — but they show the same trust-boundary weakness has been found and fixed in Claude Code repeatedly.

---

## SymJack — Symlink Hijack Overwrites MCP Config at Restart

**Disclosed:** May 26, 2026 (updated May 27, 2026 to include OpenAI Codex CLI) ([Adversa AI](https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/))  
**Affected:** Claude Code, Gemini CLI, Antigravity CLI, Cursor Agent CLI, GitHub Copilot CLI, Grok Build, OpenAI Codex CLI

### The Attack

SymJack targets a different moment in the agent lifecycle: not initial launch, but **restart**.

The attack works in two stages:

1. The attacker delivers a disguised symlink — typically framed as a benign file copy instruction within a project. The agent executes the instruction. What it does not see is that the destination path is a symlink; the OS kernel follows it silently.

2. The symlink resolves to the agent's MCP config directory. The "file copy" operation overwrites the config with an attacker-controlled payload.

On next restart, the agent reads the poisoned config and launches the malicious MCP server. No additional user interaction is required.

### What Makes SymJack Different from TrustFall

TrustFall requires the attacker to compromise a repo the victim clones. SymJack can be delivered at runtime — through a malicious project file, a context injection, or any other vector that can cause the agent to perform a file write operation. The attack surface is wider and the trust assumption is different.

Both attacks share the same consequence: the agent's MCP config becomes attacker-controlled, and the next process the agent launches may be the attacker's.

---

## Affected Tools Summary

| Tool | TrustFall | SymJack | Patch Status |
|---|---|---|---|
| Claude Code | Yes (no CVE; rejected as by-design) | Yes (no CVE; approval flow hardened) | **Partially hardened** — SymJack approval prompt now shows real resolved path; TrustFall itself rejected |
| Cursor CLI | Yes | Yes | **Declined to patch** |
| Gemini CLI | Yes | Yes | **Declined to patch** |
| Antigravity CLI | — | Yes | **Declined to patch** |
| GitHub Copilot CLI | Yes | Yes | **No response** |
| Grok Build | — | Yes | **No response** |
| OpenAI Codex CLI | — | Yes (added May 27) | **Closed as false positive** (Bugcrowd) |

As of June 14, 2026, Anthropic is the only vendor to have made any hardening change — and only for SymJack; TrustFall itself was rejected outright, not patched. All other vendors have declined, gone silent, or dismissed the reports ([SecurityWeek](https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/); [Adversa AI](https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/)).

---

## What Builders Should Do

**1. Update Claude Code now; do not wait on other vendors.**  
Anthropic hardened the SymJack approval flow (TrustFall itself was rejected as by-design, and separately Claude Code has patched three earlier, related trust-boundary CVEs — see above). Ensure you're running the latest version. No remediation is forthcoming from Cursor, Google, GitHub, xAI, or OpenAI — the hardening steps below are your only mitigation if you use those tools.

**2. Audit MCP config files before accepting trust prompts.**  
When you clone a repository and your CLI prompts for folder trust, inspect `.mcp.json` (or the equivalent config file for your tool) before accepting. Look for any MCP server entry pointing to a remote URL, an npm package you don't recognize, or a path you didn't configure yourself.

**3. Treat MCP server entries in cloned repos like `package.json` scripts — with scrutiny.**  
The developer community has spent years building norms around not blindly running `npm install && npm start` in an untrusted repo. The same discipline now applies to MCP configs. A `.mcp.json` is executable infrastructure.

**4. Review your MCP config directory for unexpected entries.**  
SymJack overwrites config at the directory level. If you've run an AI coding agent against any project that involved external file writes, verify your global MCP config hasn't been modified.

**5. Disable auto-discovery of project-local MCP configs if your tool supports it.**  
Some CLIs let you restrict MCP server discovery to user-level config only. If you're working frequently with untrusted or public repositories, this is a meaningful risk reduction.

---

## The Structural Problem

TrustFall and SymJack are not Claude Code bugs or Cursor bugs individually — they're symptoms of a pattern: MCP config handling across the ecosystem was designed for developer convenience, not for adversarial environments.

The trust prompt problem Anthropic noted as "outside its threat model" is the same one every vendor in this space faces: how do you make a tool that runs powerful local processes on the developer's machine — automatically, on project open — while maintaining a security boundary that's meaningful to non-security-specialist developers?

The [MCP 2026-07-28 spec release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) addresses some authentication and server discovery questions, but it does not fully resolve the local execution trust problem. That's an open design challenge for the ecosystem.

For now, the practical security posture is: know what's in your MCP config, update your tools, and apply the same supply-chain skepticism to MCP servers that you would to any third-party code running on your machine.

---

## Sources

- Adversa AI: [TrustFall — Coding Agent Security Flaw Enables One-Click RCE](https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/) (May 7, 2026)
- Adversa AI: [SymJack — Symlink RCE in Five AI Coding Agents](https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/) (May 26-27, 2026)
- Dark Reading: [TrustFall Exposes Claude Code Execution Risk](https://www.darkreading.com/application-security/trustfall-exposes-claude-code-execution-risk)
- The Register: [Anthropic response to 1-click pwn: Shouldn't have clicked 'ok'](https://www.theregister.com/security/2026/05/07/claude-code-trust-prompt-can-trigger-one-click-rce/5235319) (May 7, 2026)
- SecurityWeek: [SymJack Attack Turns AI Coding Agents Into Supply Chain Attack Delivery Systems](https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/)
- Check Point Research: [Caught in the Hook: RCE and API Token Exfiltration Through Claude Code Project Files (CVE-2025-59536, CVE-2026-21852)](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/)
- GitLab Advisory Database: [CVE-2026-33068 — Claude Code Workspace Trust Dialog Bypass via Repo-Controlled Settings File](https://advisories.gitlab.com/npm/@anthropic-ai/claude-code/CVE-2026-33068/)
- The Hacker News: [Miasma Worm Hits 73 Microsoft GitHub Repositories in Major Supply Chain Attack](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html) (June 2026)
- StepSecurity: [Miasma Worm Hits Microsoft Again](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents)
- MCP: [The 2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)

---

*ChatForest covers AI development tools and ecosystem security from a builder's perspective. This article is based on public disclosures and researcher-published reports — we do not conduct independent vulnerability testing.*
