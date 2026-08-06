# Rogue Agent: The Dialogflow CX Flaw That Let One Permission Hijack Every Chatbot in Your Project

> Varonis disclosed 'Rogue Agent' on July 7, 2026: a now-patched Google Dialogflow CX vulnerability where a single dialogflow.playbooks.update permission let an attacker overwrite the shared execution environment, silently intercepting conversations and injecting phishing prompts across every chatbot agent in the GCP project. No CVE, no known exploitation. Here's what happened and what builders should check.


Varonis Threat Labs published ["Rogue Agent"](https://www.varonis.com/blog/rogue-agent-dialogflow-attack) on July 7, 2026: a detailed disclosure of a now-patched vulnerability in Google Cloud's [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block) service. The flaw sat in the [Code Blocks feature inside Playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block) — a way to embed custom Python logic directly into conversation flows. It let an attacker with a single low-privilege permission overwrite the shared execution environment that every agent in a GCP project uses, intercepting conversations and injecting phishing prompts at scale ([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack)).

The attack was discovered in November 2025. Google issued an initial patch in April 2026 and fully resolved the issue in June 2026 ([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack); [The Hacker News](https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html)). Varonis is not aware of exploitation in the wild before the patch ([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack)).

If your organization uses Dialogflow CX with Playbooks and Code Blocks, this is a good time to audit — even though the underlying vulnerability is gone.

---

## How the Attack Worked

[Dialogflow CX Playbooks let developers embed Code Blocks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block): fragments of Python that run during a conversation to control agent behavior and orchestrate tool calls. Varonis found Google executes these blocks in a [Cloud Run](https://cloud.google.com/run) container ([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack)).

Varonis found that the wrapper file handling Code Block execution — `code_execution_env.py`, which runs blocks via Python's `exec()` — sat inside that container with write access. Anyone who could create or update a Code Block could modify it ([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack)).

The attack chain (per Varonis's disclosure):

1. **Initial foothold**: Attacker obtains [`dialogflow.playbooks.update`](https://www.varonis.com/blog/rogue-agent-dialogflow-attack) permission on any one agent in the GCP project. This is presented as a scoped, per-agent permission.

2. **Reconnaissance**: A malicious Code Block enumerates the Cloud Run filesystem and locates `code_execution_env.py`.

3. **Overwrite**: The block downloads a modified version of the file from an attacker-controlled bucket and replaces the original inside the running container.

4. **Persistence**: From that point, the attacker's version runs for every Code Block execution — across every agent sharing the same project environment. It sits in the same execution scope as legitimate code, with access to `history` (conversation data including past user utterances and responses) and `state` (session-level parameters and session IDs) ([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack)).

5. **Exfiltration and phishing**: The compromised wrapper silently transmits conversation data to an external server. It can also inject phishing prompts into the agent's responses — impersonating reauthentication requests to harvest user credentials.

6. **Cover-up**: Original Code Block configurations can be restored, leaving minimal forensic traces.

---

## What "One Permission" Actually Meant

The permission label `dialogflow.playbooks.update` sounds scoped: update permissions on a playbook, in one agent. The reality was broader.

Because Code Blocks in Dialogflow CX ran inside a shared Cloud Run execution environment at the GCP project level, modifying the execution wrapper affected every agent in that project, not just the one the attacker had permission on. A developer with access to a low-value test agent could — if they were compromised or malicious — affect production agents handling real user data.

This is the core lesson. Platform abstractions often make blast radius invisible. The IAM permission sounds narrow. The underlying infrastructure it can reach may not be.

---

## What Data Was at Risk

Within the execution scope available to Code Blocks, the attacker's modified wrapper had access to:

- Full conversation histories (the `history` variable)
- Session state parameters (the `state` variable)
- Any credentials submitted through phishing prompts injected into agent responses
- PII, payment details, and confidential business information passed through the chatbot

([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack))

[VPC Service Controls](https://cloud.google.com/vpc-service-controls) — a common GCP defense-in-depth measure — could be bypassed because Varonis found Code Blocks execute outside the project's VPC-SC perimeter with unrestricted outbound internet access, letting a compromised container reach an attacker-controlled bucket regardless of VPC-SC policy ([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack)).

---

## Google's Response

Varonis reported the vulnerability in November 2025 through responsible disclosure ([Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack)). Google acknowledged it and issued an initial mitigation in April 2026, with full resolution in June 2026 ([The Hacker News](https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html)). Google told reporters there is no known indication of customer compromise and that the underlying issue has been fully mitigated ([SecurityWeek](https://www.securityweek.com/google-dialogflow-cx-bug-allowed-attackers-to-hijack-ai-conversations/); [Security Boulevard](https://securityboulevard.com/2026/07/google-fixes-dialogflow-cx-flaw-that-could-have-enabled-ai-chatbot-data-theft/)).

No CVE number has been assigned ([The Hacker News](https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html)).

---

## Builder Checklist

The platform-level vulnerability is patched. What builders should still do:

**Audit IAM permissions now**
- Identify everyone with `dialogflow.playbooks.update` in your GCP project
- Verify each grant is scoped to the appropriate role and justification
- Revoke grants for offboarded employees and unused service accounts
- Apply least privilege: if someone only needs to read agents, they should not have update permissions

**Review all Code Blocks**
- Enumerate every Code Block in every Playbook in every agent in your project
- Confirm each block was created or last modified by an authorized actor
- Check for any Code Block that makes outbound network calls, writes to the filesystem, or references external URLs — those deserve closest scrutiny
- Correlate Playbook update events in Cloud Logging against expected change events

**Enable audit logging**
- Ensure Cloud Logging has DATA_WRITE audit logs enabled for Dialogflow CX
- Log queries to identify unusual Playbook update events:
  - Rare users making changes
  - Atypical source IPs
  - Off-hours modifications
  - Bulk updates across multiple agents

**Consider UEBA for GCP**
- User and Entity Behavior Analytics tools can baseline what normal Playbook update activity looks like and alert on deviations
- Posture management tools can flag when a Code Block pattern matches known risky behaviors (outbound HTTP, filesystem writes)

---

## The Broader Pattern

Rogue Agent sits alongside GuardFall and Friendly Fire as a reminder that the attack surface of AI development platforms extends into the platform infrastructure itself, not just your application code.

[GuardFall](https://adversa.ai/blog/opensource-ai-coding-agents-shell-injection-vulnerability/) (published by Adversa AI, June 30, 2026; also covered by [The Hacker News](https://thehackernews.com/2026/06/guardfall-exposes-open-source-ai-coding.html)) found that 10 of 11 popular open-source AI coding agents shipped an exploitable agent-to-shell boundary, letting attackers craft commands that pattern-based guards judge safe but that Bash rewrites into destructive operations before execution. [Friendly Fire](https://ainowinstitute.org/publications/friendly-fire-exploit-brief) (published by AI Now Institute, July 8, 2026) showed how prompt injections planted in a third-party code library could trick defensive coding agents — Claude Code in auto-mode and Codex in auto-review — into executing attacker-controlled code while believing they were performing a routine security review. Rogue Agent shows how a single low-privilege permission in a cloud AI platform can exceed its labeled blast radius by touching shared infrastructure.

In all three cases, the exploitable surface was not an obvious security component. It was a developer productivity feature: shell integration, code review automation, conversation logic blocks.

The emerging pattern is that the "one agent does one thing" mental model breaks down when execution environments are shared. Whether that is a shared Cloud Run container in Dialogflow CX, a shared file system in an agent orchestrator, or a shared process in a code execution sandbox, the permission that governs access to one agent may be executing in an environment that touches many.

Builders running agentic platforms on GCP — or any managed AI platform — should ask their vendors: what is the actual execution boundary for this permission, and does it align with what the permission label says?

---

*Varonis's original disclosure: [Rogue Agent: How a Single Code Block Could Hijack Your AI Conversations in Google's Dialogflow](https://www.varonis.com/blog/rogue-agent-dialogflow-attack) (July 7, 2026).*

