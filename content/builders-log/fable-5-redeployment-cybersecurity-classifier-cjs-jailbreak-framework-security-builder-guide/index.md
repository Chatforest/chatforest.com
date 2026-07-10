---
title: "Fable 5 Is Back: New Cybersecurity Classifier, the CJS Jailbreak Framework, and What Security Builders Need to Know"
date: 2026-07-11
description: "After an 18-day suspension under US export controls, Claude Fable 5 returned July 1 with a new cybersecurity classifier, an auto-reroute to Opus 4.8 when blocked, and Anthropic's first published Cyber Jailbreak Severity (CJS) framework. Here's what changed and how to keep your security workflows running."
tags: ["fable-5", "anthropic", "claude", "cybersecurity", "jailbreak", "safety-classifier", "cjs", "security", "builder-guide", "export-controls", "ai-safety", "developer-tools"]
---

Claude Fable 5 returned on July 1, 2026 — 18 days after US government export controls shut it down globally. It came back with a new safety classifier targeting the specific jailbreak technique that triggered the suspension, a new auto-reroute mechanism that sends blocked requests to Opus 4.8 instead of rejecting them, and something that hadn't existed before: a published framework for rating jailbreak severity.

If you build anything involving Claude and security tooling — penetration testing assistants, vulnerability scanners, code auditing pipelines, security training tools — here's what changed and what you need to adjust.

## What Happened: The June Timeline

- **June 9**: Fable 5 and Mythos 5 released globally
- **June 12**: US government applies export controls; both models suspended worldwide
- **June 30**: Export controls lifted after productive conversations between Anthropic and the US government
- **July 1**: Global redeployment with new classifier in place

The suspension was triggered by Amazon researchers who found a prompting technique that bypassed Fable 5's safeguards to identify and demonstrate software vulnerability exploitation. The US government treated this as a controlled-technology concern and applied export controls within days of the disclosure.

Notably, Anthropic reported that every model tested — including GPT-5.5, Claude Haiku 4.5, and others — produced the same exploitation demonstrations when given the same prompts. This wasn't a Fable-5-unique capability leak; it was a cross-model vulnerability to a specific jailbreak framing. Fable 5 was targeted because it's the frontier model, not because it was uniquely exploitable.

## The New Classifier: What It Does

Anthropic deployed an improved safety classifier that blocks the reported jailbreak method in over 99% of cases. The key behavior change:

**When blocked**: Instead of returning a refusal, Fable 5 automatically reroutes the request to Claude Opus 4.8. You receive a notification that the redirect happened. You still get a response — from Opus 4.8, with its existing (pre-July-1) cybersecurity safeguards but without the tighter new classifier.

The tradeoff Anthropic states explicitly: the new classifier also triggers false positives on benign coding and debugging requests that have security-adjacent framing. This is intentional — they expanded the safety margin to ensure the flagged jailbreak technique doesn't slip through.

## The 4-Tier Request Classification

Anthropic published its internal framework for how Fable 5 categorizes cybersecurity requests, from most to least restricted:

**Tier 1 — Prohibited Use**: Activities with minimal defensive value and high attack potential. Examples: ransomware development, malware construction, defense evasion techniques, data exfiltration tooling. These are blocked regardless of framing.

**Tier 2 — High-Risk Dual Use**: Legitimate security work that mirrors attacker techniques. Examples: penetration testing, exploit development, privilege escalation testing. These trigger heightened scrutiny; framing matters significantly.

**Tier 3 — Low-Risk Dual Use**: Primarily defensive activities. Examples: vulnerability scanning, open-source intelligence gathering, cryptographic testing. These are generally allowed but may still trigger false positives if the framing is ambiguous.

**Tier 4 — Benign Use**: Standard security operations with minimal dual-use risk. Examples: secure coding, patch management, incident response, log analysis. These pass through without triggering the classifier.

## What Framing Triggers the Classifier

Based on Anthropic's documentation and early builder reports, the classifier fires on requests that pattern-match to active vulnerability exploitation:

**Framing that elevates risk**:
- "Find vulnerabilities in this code"
- "Show me how to exploit..."
- "Generate a payload that..."
- "Demonstrate this CVE in action"
- Language framing the task as active offense, exploit construction, or weaponization

**Framing that reduces risk**:
- "Review this code for security issues per OWASP Top 10"
- "Identify defensive fixes for this function"
- "Audit this for compliance with [standard]"
- "What patches are needed here?"
- Language framing the task as defensive review, compliance, or remediation

For legitimate security work, the actionable shift is: frame your prompts around the defensive objective, not the offensive technique you're investigating. "What's vulnerable here and how do I fix it" passes more cleanly than "demonstrate how to exploit this."

## The CJS Framework: Anthropic's Jailbreak Severity Scoring

Alongside the redeployment announcement, Anthropic published the Cyber Jailbreak Severity (CJS) framework — their standardized method for rating how dangerous a jailbreak technique is. This is the first time they've published a formal scoring rubric.

CJS rates jailbreaks across four dimensions:

**Capability Gain** (0–4): How much the jailbreak pushes attackers beyond tools already available to them, and whether outputs are usable by domain experts vs. requiring additional expertise.

**Breadth of Capability** (0–2): How many distinct offensive tasks or vulnerability types the technique affects — a single-CVE bypass scores lower than one that enables broad classes of attacks.

**Ease of Weaponization** (0–2): How much effort an attacker needs to convert the jailbreak output into a working operational attack.

**Discoverability** (0–2): How easily threat actors can find and reproduce the technique independently.

Combined scores produce CJS levels from 0 (Informational) through 4 (Critical). Anthropic's position is that a CJS 4 finding triggers immediate response including model suspension if necessary — which is effectively what happened with the Amazon discovery.

For the security research community, the CJS framework matters because it establishes a common language for reporting AI jailbreak severity. It's analogous to CVSS for traditional vulnerabilities.

## Pricing and Availability After July 7

The redeployment came with new access tiers that changed on July 7:

**Through July 7**: For Pro, Max, Team, and select Enterprise plans, Fable 5 was included at no extra cost for up to 50% of weekly usage limits.

**After July 7**:
- **Pro/Max/Team**: Fable 5 available via usage credits (not included in base subscription)
- **Standard Enterprise**: Credits only; no included allowance
- **Premium Enterprise**: Fable 5 remains in subscription, drawing from seat usage

This is a pricing tier change compared to before the suspension. If your team's workflows assumed Fable 5 was always included in a Pro/Team plan, you need to account for credits now.

## The Bigger Precedent

The mechanism that matters most long-term isn't the classifier — it's what the June suspension proved.

A US government export control order pulled a cloud AI model out of service for every user globally within 72 hours of a researcher disclosure. The "digital kill switch" for frontier AI models is now proven to work at scale. It doesn't require the model provider to cooperate on a long timeline; it requires a disclosure, an export control determination, and 72 hours.

For enterprise teams building on frontier models: your AI dependency plan needs a contingency for a model-unavailable scenario that isn't the model provider's choice. The July 1 rerouting to Opus 4.8 was Anthropic's graceful fallback, but it wasn't guaranteed — the 18-day suspension covered the full model, not just the flagged capability.

If Fable 5 is your primary model for production agents, build with an Opus 4.8 fallback path that you test regularly.

## Builder Checklist

- **Audit your security-adjacent prompts**: review any prompt that uses offensive framing and restate it defensively; test against the 4-tier classification above
- **Log reroute events**: when Fable 5 silently reroutes to Opus 4.8, you get a notification — instrument your system to log these so you can identify which prompts are triggering the classifier
- **Test your Opus 4.8 fallback**: the reroute happens automatically, but Opus 4.8 has different behavior from Fable 5; verify your workflows produce acceptable output on both
- **Update your pricing model**: Fable 5 now runs on usage credits for most plans; audit your monthly cost assumptions
- **Plan for a model-unavailable scenario**: the June suspension was 18 days; design your dependency on frontier models accordingly
