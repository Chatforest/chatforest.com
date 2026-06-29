# TrustFall and SymJack: Two RCE Classes That Hit Every Major AI Coding Agent

> Adversa AI disclosed two independent RCE attack classes in May 2026 — TrustFall and SymJack — affecting Claude Code, Cursor, Gemini CLI, GitHub Copilot CLI, and OpenAI Codex CLI. Both exploit MCP config handling. Here's what builders need to know.


In May 2026, Adversa AI published two independent vulnerability disclosures — **TrustFall** and **SymJack** — that together demonstrate a systemic weakness in how AI coding agents handle MCP configuration. Both classes achieve remote code execution. Both affect the tools you're likely using every day.

This article covers what each attack does, which tools are affected, what patches exist, and how builders should think about their exposure.

---

**Update — June 14, 2026:** Final vendor response status is now confirmed. Anthropic patched three CVEs (CVE-2025-59536, CVE-2026-21852, CVE-2026-33068) and quietly hardened the SymJack approval flow — the approval prompt now displays the real resolved path instead of the symlink path. No other vendor patched either attack class. Google (Gemini CLI / Antigravity CLI) and Cursor both formally **declined to patch**. xAI (Grok Build) and GitHub Copilot CLI gave **no response** to researchers. OpenAI had the Codex CLI report **closed by Bugcrowd as a false positive**, characterizing the attack as "theoretical" because the user approves the underlying `cp` command — ignoring that the symlink redirection is invisible to the user at approval time. The table below reflects these outcomes. Builders using any unpatched tool should assume no vendor mitigation is forthcoming and apply the hardening steps below.

---

## Background: Why AI Coding CLIs Are a Target Now

AI coding agents — Claude Code, Cursor, Gemini CLI, Copilot CLI, Codex CLI — have all adopted MCP as a primary integration layer. MCP servers run as local processes that the agent launches on startup. They have access to files, shell commands, APIs, and whatever secrets the developer's environment carries.

The attack surface follows from this model: **if an attacker can control which MCP server gets executed, they own the machine**.

Adversa AI's research identified two paths to that outcome. They operate at different layers, require different mitigations, and in at least one case have been exploited in the wild.

---

## TrustFall — One-Click RCE via Project-Embedded MCP Config

**Disclosed:** May 7, 2026  
**CVEs:** CVE-2026-21852, CVE-2026-33068 (both patched by Anthropic)  
**Affected:** Claude Code, Cursor CLI, Gemini CLI, GitHub Copilot CLI

### The Attack

Modern AI coding CLIs auto-discover MCP servers from config files stored in project directories — typically `.mcp.json` or equivalent. When a user opens a cloned repository and accepts the folder trust prompt, the CLI reads the project's MCP configuration and launches the servers listed there.

TrustFall exploits this directly: a malicious actor plants a `.mcp.json` in a repository that points to an attacker-controlled MCP server. The builder clones the repo, accepts the trust prompt — which frames the question as "do you trust this folder to run code?" without clearly disclosing it will launch network-connected processes — and execution begins.

The user sees one prompt. The CLI executes potentially arbitrary MCP server code on their machine.

### Real-World Exploitation: The Miasma Worm

The attack was not purely theoretical. Adversa AI documented the **Miasma worm**, which exploited TrustFall by planting a malicious `.mcp.json` inside the Microsoft Azure `durabletask` repository — a widely cloned open-source project. Any developer who cloned the compromised repo and opened it in an affected AI coding CLI became an execution target.

The Miasma worm demonstrates the supply-chain multiplier effect: one compromised popular repo, many downstream victims, all through the standard developer workflow.

### Anthropic's Response

Anthropic issued patches addressing CVE-2026-21852 and CVE-2026-33068. Additionally, the SymJack approval-flow hardening was addressed under CVE-2025-59536 — the approval prompt now displays the real resolved path of a symlink target, not the symlink itself, making the redirect visible to the user before they approve. However, Anthropic's public response also characterized the core trust-prompt UX issue as "outside its threat model" — meaning the underlying ambiguity of what a folder trust prompt authorizes remains an open design question across the ecosystem.

---

## SymJack — Symlink Hijack Overwrites MCP Config at Restart

**Disclosed:** May 27, 2026 (updated to include OpenAI Codex CLI)  
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
| Claude Code | Yes (CVE-2026-21852, CVE-2026-33068) | Yes (CVE-2025-59536) | **Patched** — approval prompt now shows real resolved path |
| Cursor CLI | Yes | Yes | **Declined to patch** |
| Gemini CLI | Yes | Yes | **Declined to patch** |
| Antigravity CLI | — | Yes | **Declined to patch** |
| GitHub Copilot CLI | Yes | Yes | **No response** |
| Grok Build | — | Yes | **No response** |
| OpenAI Codex CLI | — | Yes (added May 27) | **Closed as false positive** (Bugcrowd) |

As of June 14, 2026, Anthropic is the only vendor to have patched either attack class. All other vendors have declined, gone silent, or dismissed the reports.

---

## What Builders Should Do

**1. Update Claude Code now; do not wait on other vendors.**  
Anthropic patched three CVEs and hardened the SymJack approval flow. Ensure you're running the latest version. No remediation is forthcoming from Cursor, Google, GitHub, xAI, or OpenAI — the hardening steps below are your only mitigation if you use those tools.

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

The MCP 2026-07-28 spec RC addresses some authentication and server discovery questions, but it does not fully resolve the local execution trust problem. That's an open design challenge for the ecosystem.

For now, the practical security posture is: know what's in your MCP config, update your tools, and apply the same supply-chain skepticism to MCP servers that you would to any third-party code running on your machine.

---

## Sources

- Adversa AI: [TrustFall — Coding Agent Security Flaw Enables One-Click RCE](https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/) (May 7, 2026)
- Adversa AI: [SymJack — Symlink RCE in Five AI Coding Agents](https://adversa.ai/blog/the-approval-prompt-is-lying-to-you-symlink-rce-in-five-ai-coding-agents-claude-code-cursor-antigravity-copilot-grok-build/) (May 27, 2026)
- Dark Reading: [TrustFall Exposes Claude Code Execution Risk](https://www.darkreading.com/application-security/trustfall-exposes-claude-code-execution-risk)
- SecurityWeek: [SymJack Attack Turns AI Coding Agents Into Supply Chain Attack Delivery Systems](https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/)

---

*ChatForest covers AI development tools and ecosystem security from a builder's perspective. This article is based on public disclosures and researcher-published reports — we do not conduct independent vulnerability testing.*

