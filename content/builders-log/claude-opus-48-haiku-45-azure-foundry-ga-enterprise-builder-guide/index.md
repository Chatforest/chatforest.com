---
title: "Claude Is Now GA on Azure Foundry. Here's What Enterprise Builders Get."
date: 2026-07-01
description: "On June 29, 2026, Anthropic's Claude Opus 4.8 and Haiku 4.5 became generally available on Microsoft Azure Foundry — natively integrated with Azure billing, governance, and US data residency. Here's what changed, what it doesn't give you yet, and when to use it."
og_description: "Claude Opus 4.8 and Haiku 4.5 are now GA on Azure Foundry. Azure-hosted vs Anthropic-hosted: what each path gives you, who benefits from the Azure path, and what feature gaps remain."
content_type: "Builder's Log"
categories: ["Anthropic", "Azure", "Microsoft", "Enterprise AI", "AI Infrastructure"]
tags: ["claude", "anthropic", "azure", "foundry", "microsoft", "opus-48", "haiku-45", "enterprise", "data-residency", "billing", "governance", "nvidia", "gb300", "builder-guide"]
---

On June 29, 2026, Anthropic announced that Claude is generally available in Microsoft Azure Foundry. Claude Opus 4.8 and Claude Haiku 4.5 are now accessible through the Messages API as a first-party Azure service — with Azure-native billing, identity, networking, and a US data residency option.

This is different from what was [already possible via Azure API Management](/builders-log/azure-api-management-unified-model-api-anthropic-vertex-a2a-build-2026-builder-guide/), where a gateway layer routed requests to Anthropic's API. Claude is now a native Foundry service with Azure authentication and consolidated billing. Part of our **[Builder's Log](/builders-log/)**.

---

## What Is Actually Available

Two models reached GA on June 29:

| Model | API | Key Capabilities |
|---|---|---|
| Claude Opus 4.8 | Messages API | Prompt caching, extended thinking, complex reasoning |
| Claude Haiku 4.5 | Messages API | Prompt caching, fast inference, low cost |

Claude Sonnet 4.6 is not listed in the initial GA offering. The announcement says Microsoft and Anthropic "aim to have feature and model parity" between the Azure-hosted and Anthropic-hosted paths over time — this language signals that parity is a goal, not the current state.

The physical infrastructure runs on NVIDIA GB300 Blackwell Ultra systems. For workloads that saturate GPU bandwidth, this is a tier above standard Azure inference capacity.

---

## Two Deployment Modes

The GA announcement formalizes two distinct ways to access Claude through Foundry:

**Hosted on Azure** — inference runs in your Azure environment. You get Azure authentication (Entra), Azure billing, Azure networking controls, and the option to pin workloads to a US data zone. Anthropic operates the inference as a data processor within this arrangement.

**Hosted on Anthropic** — formerly the "Foundry Preview" path. Requests go to Anthropic's infrastructure. You get the full Anthropic API feature set and access to models not yet available in the Azure-hosted path.

The key tradeoff in one sentence: Azure-hosted buys compliance and integration; Anthropic-hosted buys capability breadth.

---

## What the Azure-Hosted Path Gives Enterprise Teams

### Billing consolidation

Azure enterprise agreements (EAs) carry significant discounts, drawdown commitments, and centralized invoicing. If your team already has an Azure EA, adding Claude usage to the same invoice is materially simpler than maintaining a separate Anthropic account, separate credit card, and separate budget approval chain. The announcement confirms EA drawdown eligibility.

### Identity and governance without extra plumbing

Azure-hosted Claude uses Entra ID for authentication. Role assignments, audit logs, and access policies use the same tooling your security team already manages. If your organization has mandated that all production AI calls go through Azure's governance layer, Claude now qualifies without a gateway workaround.

### US data residency

If your legal or compliance requirements specify that inference must happen on US soil, the Azure-hosted path offers a dedicated US data zone. Anthropic's direct API does not offer this level of geographic control today.

### NVIDIA GB300 performance

GB300 Blackwell Ultra is the current top tier for Azure inference. For latency-sensitive workloads — voice agents, interactive reasoning pipelines, real-time document review — running on GB300 versus standard inference hardware is a real difference.

---

## What the Azure-Hosted Path Does Not Give You (Yet)

**Model selection**: Only Opus 4.8 and Haiku 4.5 at launch. Sonnet 4.6, the model most teams use for everyday coding and analysis tasks at the cost/quality midpoint, is absent. The "parity over time" language suggests it's coming, but it is not there now.

**API surface parity**: The Anthropic API has capabilities that are not replicated on the Azure-hosted path yet. The announcement explicitly calls this out and frames it as future work. If you depend on features outside the Messages API core — certain streaming behaviors, newer API versions, specific beta endpoints — test before committing.

**All models**: Newer or more specialized models will likely appear on Anthropic-hosted first. The Azure path will lag.

If your workload needs the latest models or the full API surface, the Anthropic-hosted path or direct API is still the right choice.

---

## How This Fits the Azure Multi-Model Story

Microsoft has been methodically adding model providers as first-party options in Foundry:

- June 1–3, 2026: GPT-5.5 and Codex reached GA on both Bedrock and Azure Foundry ([coverage](/builders-log/gpt-5-5-aws-bedrock-azure-foundry-ga-multi-cloud-deployment-guide/))
- June 3, 2026: Azure API Management added a unified gateway to route to Anthropic, Vertex AI, and OpenAI through a single endpoint ([coverage](/builders-log/azure-api-management-unified-model-api-anthropic-vertex-a2a-build-2026-builder-guide/))
- June 29, 2026: Claude itself becomes a native Foundry service

The pattern is clear: Azure is positioning as a neutral layer where enterprise buyers can run OpenAI, Anthropic, and Google models under a single contract and governance framework. For Microsoft, this reduces the risk that a team choosing Anthropic walks off the Azure platform. For Anthropic, it adds a major enterprise distribution channel without requiring Anthropic to build enterprise billing infrastructure itself.

---

## The Builder Decision

**Use Azure-hosted Claude if:**
- You have an Azure EA and want consolidated billing
- Your security team requires Azure Entra for all production AI calls
- You need documented US data residency for compliance
- You are already running other workloads in Azure and want to avoid a second vendor relationship

**Use Anthropic-hosted (via direct API or Foundry's Anthropic-hosted mode) if:**
- You need Sonnet 4.6 or a model not yet on the Azure-hosted path
- You need API features beyond Messages API core
- You want access to new Anthropic releases the moment they ship, not when Azure picks them up
- You are a startup or smaller team without an Azure EA (the cost savings don't apply)

**Use Azure API Management's Unified Model API if:**
- You want a single OpenAI-compatible endpoint that routes to multiple providers
- You need policy-based routing or A2A governance across providers

These are not mutually exclusive. A reasonable architecture routes non-compliance workloads through the direct Anthropic API for the latest features, and moves production enterprise workloads to Azure-hosted as the model and feature set matures.

---

## Bottom Line

Claude GA on Azure Foundry is primarily an enterprise distribution story. The compliance, billing, and governance integrations it unlocks are real and meaningful for organizations already committed to Azure. The current model and feature gaps mean it is not a replacement for the direct Anthropic API for teams that need full capability access.

Watch for Sonnet 4.6 to appear on the Azure-hosted path — that is the model that would make this a straightforward choice for most everyday agent and coding workloads.
