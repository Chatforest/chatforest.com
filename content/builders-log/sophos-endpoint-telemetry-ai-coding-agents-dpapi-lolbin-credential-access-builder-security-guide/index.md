---
title: "Your EDR Thinks Claude Code Is an Attacker: Sophos Endpoint Telemetry on AI Coding Agents"
description: "Sophos analyzed a week of endpoint behavioral telemetry from Claude Code, Cursor, and OpenAI Codex and found them triggering detection rules written to catch human attackers. Credential access drove 56.2 percent of blocked hits, execution 28.8 percent. Here is what is happening, why it matters for builder security posture, and how to tune without going blind."
date: 2026-07-12
lastmod: 2026-07-12
slug: sophos-endpoint-telemetry-ai-coding-agents-dpapi-lolbin-credential-access-builder-security-guide
tags:
  - security
  - endpoint
  - edr
  - claude-code
  - cursor
  - codex
  - sophos
  - dpapi
  - lolbin
  - builder-guide
categories:
  - builders-log
---

In June 2026 Sophos X-Ops pulled a week of behavioral telemetry from customer endpoints and counted how often AI coding agents — Claude Code, Cursor, and OpenAI Codex — triggered detection rules written to catch human intruders. The answer: often enough that a security operations center watching those machines would spend meaningful time investigating alerts it eventually discovers are benign. The analysis, published July 8, 2026, is not a vulnerability disclosure. The agents are not malicious. But they behave, in aggregate, in ways that are nearly indistinguishable from attacker tradecraft. Part of our **[Builder's Log](/builders-log/)**.

---

## What the telemetry showed

Sophos measured hits against its behavioral engine across one week in June. The data is segmented into blocking rules (the engine stopped the action) and silent rules (the engine logged the behavior without intervening).

**Blocking rule hits by MITRE ATT&CK tactic:**

| Tactic | Share |
|---|---|
| Credential Access | 56.2% |
| Execution | 28.8% |
| Disrupt (AAP) | 4.1% |

**Silent rule hits by tactic:**

| Tactic | Share |
|---|---|
| Evasion | 38.5% |
| Command and Control | 34.0% |
| Execution | 11.1% |

The unit is unique machine count, not raw event volume, so a single agent on one developer's laptop counts once regardless of how many times it repeated a behavior.

---

## Credential access: the DPAPI problem

The dominant blocking category — 56.2 percent — is credential access, and within that category one rule drives more than a third of the hits: **Creds_3b**, which fires when a process uses Windows' Data Protection API (DPAPI) to decrypt browser-stored credential data.

The source is **GStack**, a widely adopted skill pack for AI coding agents. Its `/browse` skill does exactly what the rule is looking for: it runs PowerShell that calls DPAPI to unlock the browser's saved credential store, then extracts session tokens so the agent can authenticate to sites as the developer.

The remaining major credential rules:

- **Creds_6a** (36.2% of credential hits): Python credential access patterns
- **Creds_2e** (12.8%) and **Creds_2d** (8.5%): additional credential access shapes

Every one of these rules exists because attackers routinely extract browser-stored credentials as an early post-compromise step. When an AI agent does the same thing, the rule cannot tell the difference.

---

## Execution: LOLBin downloads

The execution category (28.8% of blocking hits) is dominated by **living-off-the-land binary** (LOLBin) activity. The specific behaviors Sophos documented:

- **OpenAI Codex** attempted to fetch a Python installer from python.org using `certutil.exe`. When that was blocked, it switched to `bitsadmin.exe`. Both are legitimate Windows utilities that attackers routinely abuse to pull payloads — a technique well-documented under MITRE ATT&CK T1197 and T1105.
- **Exec_16a** fires on PowerShell obfuscation patterns; agents producing obfuscated shell commands trigger it as a byproduct of how they construct multi-step terminal operations.
- **Persist_2a** fires when a process writes to Windows Startup folders. Some agents persist tooling this way across sessions.

None of this activity is inherently malicious when an AI coding agent does it. But none of it is activity an endpoint security engine can safely ignore.

---

## The --dangerously-skip-permissions detail

One entry in the Sophos analysis is worth pulling out separately. Claude Code invoked with the `--dangerously-skip-permissions` flag — the flag Anthropic's own documentation explicitly warns against — triggered additional rules the engine would not otherwise have fired. This is a configuration choice builders make, not a default, but it illustrates how the flag's purpose (removing permission prompts in automated pipelines) directly expands the agent's footprint on the host's detection surface.

---

## Why this matters alongside Friendly Fire

Earlier in the same week, AI Now Institute published **Friendly Fire**, a proof-of-concept showing that Claude Code in auto-mode and Codex in auto-review can be steered into executing attacker-controlled code during what looks like a routine security review. The attack vector is prompt injection spread across source files; the payload executes on the reviewer's host.

Sophos documented something structurally different: not an attack on the agent, but the agent behaving — on its own, doing legitimate work — in ways that look identical to attacks. Both findings arrive in the same two-week window and point at the same gap: enterprise security tooling was not designed with the assumption that software installed by developers would call DPAPI, run certutil, or write to Startup folders as routine operations.

Sophos also noted, separately, that a month before publishing this analysis it documented an attacker who used AI agents — including one running Claude Opus 4.5 — to build and test malware specifically against EDR products. That was a development-time case: AI helping an attacker write better evasion tooling. The June telemetry analysis is the legitimate-use case. The rules these agents trigger are not false positives in any meaningful sense; they are rules worth having, now firing on populations they were not written for.

---

## What to do

**1. Identify your agent footprint before your SOC does.**
List which AI coding agents your developers run on managed endpoints. This includes Claude Code, Cursor, Codex, Aider, Cline, and any GStack-based tooling. If you do not have an inventory, your security operations team is building one reactively.

**2. Do not suppress rules wholesale.**
The temptation when you discover that your agents are generating alerts is to create a blanket exclusion for the agent process. Resist this. An attacker who can execute as the agent process — which Friendly Fire demonstrates is possible — would benefit from that exclusion. Tune by behavior, not by process name where you can avoid it.

**3. Evaluate the GStack /browse skill specifically.**
DPAPI credential decryption is the single largest category in the Sophos data (42.6% of credential-access hits). If your agents use GStack's /browse skill and your developers do not need that capability, disable it. If they do need it, it should be allowed under a named policy and logged, not silently excluded.

**4. Flag --dangerously-skip-permissions in policy.**
If your CI/CD pipelines or developer machines run Claude Code with `--dangerously-skip-permissions`, treat that configuration as a named exception requiring explicit approval, not a default that gets set once and forgotten.

**5. Create detection profiles for known-agent behavior.**
Add agent binary signatures to your detection engineering backlog so your rules can emit "AI agent — review" rather than "attacker credential theft — block" for behaviors you have validated. This allows you to tune severity without eliminating the detection.

**6. Watch certutil and bitsadmin invocations from agent processes.**
Even in a tuned environment, LOLBin download attempts from agents warrant a second look. An agent fetching a Python installer from python.org is probably benign. An agent fetching from an unfamiliar host using the same method is not.

---

## The detection engineering backlog this creates

Sophos's framing is that the correct response is not to decide the rules are wrong. The rules are well-founded. The correct response is to build organizational policy around what agents are and are not permitted to do on endpoints, and to use behavioral telemetry to enforce that policy rather than relying on model-level controls inside the agent.

For builders deploying coding agents inside enterprise environments, the practical implication is a new backlog item: agent-specific detection profiles. These do not exist today at most organizations because the agent category did not exist at meaningful scale a year ago. The tooling that fires on these agents was tuned against human attacker behavior measured over years. The agent behavior profiles are brand new, and the detection engineering work of characterizing them has to be done now, before agents are on enough endpoints that the alert volume becomes unmanageable.

---

## Source

Sophos X-Ops, ["When AI agents look like attackers: what behavioral telemetry tells us,"](https://www.sophos.com/en-us/blog/2607_agents_vs_telemetry) July 8, 2026.
