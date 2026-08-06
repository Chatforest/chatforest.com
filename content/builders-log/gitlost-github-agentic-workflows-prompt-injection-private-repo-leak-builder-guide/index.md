---
title: "GitLost: How Prompt Injection in GitHub Agentic Workflows Can Leak Your Private Repos"
date: 2026-07-12
sources_audited: 2026-08-06
description: "Noma Security found that a crafted public GitHub Issue can trick GitHub Agentic Workflows into posting private repo contents as public comments — with zero credentials required. No patch exists. Here is the attack chain and what builders need to do."
og_description: "A new vulnerability in GitHub Agentic Workflows lets unauthenticated attackers open a crafted issue in any public repo and watch the AI agent leak private repository files. The bypass is a single word: 'additionally.' Disclosed July 6, 2026. No patch yet."
content_type: "Builder Guide"
card_description: "GitLost exploits indirect prompt injection in GitHub Agentic Workflows. An attacker with no credentials opens a crafted Issue in a public repo, adds the word 'additionally' to bypass guardrails, and the agent exfiltrates private repository contents into a public comment. Discovered by Noma Security researcher Sasi Levi, disclosed July 6, 2026. GitHub has not yet issued a patch or public response."
tags: ["github", "prompt-injection", "security", "agentic-ai", "github-actions", "developer-tools", "supply-chain", "private-repositories", "copilot"]
categories: ["builders-log"]
author: "ChatForest"
---

**At a glance:** [Noma Security researcher Sasi Levi discovered](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) that GitHub Agentic Workflows — a feature that [entered technical preview in February 2026](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) pairing GitHub Actions with Claude or GitHub Copilot — is vulnerable to indirect prompt injection via crafted GitHub Issues. An unauthenticated attacker needs only the ability to open a public issue. The agent bypasses its own guardrails when the injection includes the word "additionally," then leaks private repository contents as publicly readable comments. [Disclosed July 6, 2026](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/). No patch, no CVE, and [no public response from GitHub](https://www.theregister.com/security/2026/07/07/github-ai-agent-leaks-private-repos-when-asked-nicely/5267924/) as of this writing. Part of our **[Builder's Log](/builders-log/)**.

---

## What is GitHub Agentic Workflows

GitHub Agentic Workflows, which [entered technical preview in February 2026](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/), let teams write Markdown workflow files that instruct a GitHub-connected AI agent (either GitHub Copilot or Claude) to take actions inside a repository in response to standard GitHub events — issue assignments, pull request opens, label changes.

A typical configuration gives the agent read access across an organization's repositories and the ability to post comments. The agent monitors the event queue, reads relevant issue or PR content, then decides what to do based on its Markdown workflow instructions.

The attack surface follows directly from that design: the agent reads user-submitted content (issues, PR descriptions, comments) in the same context as its trusted workflow instructions. There is no cryptographic or structural separation between "instructions I should follow" and "data I should process."

---

## The GitLost Attack Chain

[Noma Security researcher Sasi Levi found](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) they could exploit this trust boundary with nothing more than a free GitHub account. Here is the sequence:

1. **Find a target organization** that uses GitHub Agentic Workflows and has a public repository.
2. **Open a crafted Issue** in that public repo. The issue looks like a plausible user request — [the proof of concept used a fake message posing as a VP of Sales](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) relaying a customer request, asking the agent to fetch README files from both a public and a private repository and post them as a comment.
3. **Wait for the trigger.** When the workflow's event fires (e.g., `issues.assigned`), the agent reads the issue title and body as part of its context.
4. **Guardrail bypass.** GitHub's safety restrictions initially block the malicious instruction — but the researchers found that adding the word **"additionally"** causes the underlying model to reframe its output rather than refuse. The agent re-interprets the instruction as an extension of its normal workflow rather than an override.
5. **Exfiltration.** The agent fetches the private repository contents it has access to and posts them as a public comment on the issue — readable by anyone, no authentication required.

The attack requires no coding skills, no credentials, no special permissions. The only requirement is the ability to open a GitHub Issue.

---

## Why "Additionally" Works

This is the uncomfortable part. GitHub implemented guardrails specifically to prevent this scenario. They failed because the bypass is not a technical exploit — it is a semantic one.

Large language models process their entire context as a weighted probability space, not as a structured command parser. Safety training teaches models to refuse certain types of requests. But the model can be prompted to interpret a request as an *addendum* to an already-in-progress legitimate task rather than as a standalone instruction to refuse. The word "additionally" exploits the model's tendency to treat continuation differently from initiation.

This class of failure is not unique to GitHub. It mirrors the broader problem that has appeared in other major AI coding assistant security disclosures in 2026: [GhostApproval](/builders-log/ghostapproval-symlink-attack-ai-coding-assistants-claude-code-cursor-amazon-q-july-2026-builder-guide/), [HalluSquatting](/builders-log/friendly-fire-hallusquatting-ai-coding-agent-auto-mode-prompt-injection-hallucination-builder-security-guide/), and the [Claude Code GitHub Action flaw](/builders-log/claude-code-github-action-prompt-injection-supply-chain-security-builder-guide/). In every case, an attacker provides plausible-looking content that the model treats as instructional rather than as data to be processed.

Levi put it precisely: **["The agent's context window is also its attack surface."](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/)**

---

## What Can Leak

The blast radius depends on what permissions the workflow has. A workflow with read access across an organization's repositories — a common configuration for triage bots, documentation agents, and release automation — can leak:

- README file contents, as [demonstrated in Noma's proof of concept](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/), which fetched `README.md` from both public and private repositories in the target org
- In principle, any other file type the agent has been granted read access to across the org — the PoC targeted README files, but the technique works by getting the agent to relay content it can already read, not by exploiting anything README-specific

The leak destination is a public GitHub issue comment. No exfiltration infrastructure needed on the attacker's side — GitHub's own platform serves as the delivery mechanism.

---

## Disclosure Timeline

| Date | Event |
|------|-------|
| February 2026 | [GitHub Agentic Workflows enters technical preview](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) |
| July 6, 2026 | [Noma Security publicly discloses GitLost](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) |
| July 12, 2026 | No patch, no CVE, [no public response from GitHub](https://www.theregister.com/security/2026/07/07/github-ai-agent-leaks-private-repos-when-asked-nicely/5267924/) |

The disclosure window before publication is not specified — it is unclear whether GitHub was given advance notice.

---

## What Builders Should Do Now

GitHub Agentic Workflows are not inherently unsafe, but they need to be hardened. If you are using them today, these steps reduce your exposure significantly:

**1. Audit workflow permissions immediately.**
Check every Agentic Workflow for `repository: read` scopes. If a workflow does not need cross-organization access, remove it. Apply the same least-privilege principle you would to any service account.

**2. Restrict public outputs from agent-triggered workflows.**
Any workflow that can post comments on public-facing issues is a potential data delivery channel. Consider routing agent output to internal channels (Slack, email, private PR comments) rather than public issue comments.

**3. Do not trigger workflows on untrusted public content without isolation.**
If your workflow must respond to issues opened by external users, structure it so the agent never has simultaneous access to sensitive repositories and the ability to post public output.

**4. Treat issue and PR content as untrusted data, not as instructions.**
Design your workflow Markdown to explicitly scope what the agent is allowed to do in response to user-submitted content. The more tightly you constrain the agent's action space, the less leverage an injected prompt has.

**5. Monitor for unexpected agent behavior.**
Review agent activity logs for unusual repository access patterns, especially cross-repository reads that do not correspond to the triggering event.

**6. Consider whether to pause Agentic Workflows until GitHub patches.**
If your workflows have broad cross-org read access and post to public venues, temporarily restricting them to internal-only or disabling them entirely until a patch is available is a reasonable risk decision.

---

## The Broader Pattern

GitLost is not the only disclosure of its kind this year — it follows the [Claude Code GitHub Action flaw](/builders-log/claude-code-github-action-prompt-injection-supply-chain-security-builder-guide/) disclosed earlier in 2026, another case of prompt injection reaching sensitive repository access through a GitHub-hosted automation surface. The pattern is consistent: features that give AI agents read access to sensitive resources and write access to public venues are vulnerable to indirect prompt injection through any untrusted content the agent reads.

The root cause is not a GitHub-specific bug. It is a fundamental property of how LLMs work: they cannot reliably distinguish between "data I should process" and "instructions I should follow." Until that changes — through architectural controls, not just safety training — builders running agentic workflows on shared infrastructure need to apply the same defense-in-depth they would to any other privileged automated process.

Noma Security's research and the original blog post are at [noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/).

---

*ChatForest researches and summarizes publicly disclosed security findings. We do not test or reproduce vulnerabilities.*
