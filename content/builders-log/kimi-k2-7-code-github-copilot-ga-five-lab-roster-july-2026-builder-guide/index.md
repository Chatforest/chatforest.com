---
title: "Kimi K2.7 Code Lands in GitHub Copilot — First Open-Weight Model in the Five-Lab Roster"
date: 2026-07-02
description: "Moonshot AI's Kimi K2.7 Code is now GA in GitHub Copilot as of July 1, 2026. It is the first open-weight model selectable in Copilot's model picker, and it completes a five-lab roster across OpenAI, Anthropic, Google, Microsoft, and Moonshot AI. Builder guide: rollout tiers, admin controls, platform support, and CLI auto-routing."
og_description: "Kimi K2.7 Code is GA in GitHub Copilot (July 1, 2026). First open-weight model in Copilot's picker. Five-lab roster: OpenAI, Anthropic, Google, Microsoft, Moonshot AI. Hosted on Azure. Pro/Pro+/Max now; Business/Enterprise admin opt-in. CLI auto-routing launched same day with 10% credit discount."
content_type: "Builder's Log"
categories: ["Developer Tools", "Models", "AI Infrastructure"]
tags: ["kimi", "kimi-k2-7", "moonshot-ai", "github-copilot", "open-source", "open-weight", "coding-agent", "model-picker", "builder-guide", "july-2026", "copilot-cli", "azure", "enterprise"]
---

On July 1, 2026, GitHub shipped Kimi K2.7-Code into general availability in GitHub Copilot. That is 19 days after Moonshot AI published the weights on Hugging Face. In under three weeks, a Chinese open-weight coding model went from "download and self-host" to "available in the world's largest developer platform by default subscription." Part of the **[Builder's Log](/builders-log/)**.

There are two headlines here. First: Kimi K2.7 Code is the **first open-weight model to appear in Copilot's model picker**. Every other selectable model is proprietary — you cannot download it, run it locally, or audit its weights. Kimi K2.7 is different: it is MIT-licensed, the full 1T parameter weights are public on Hugging Face, and GitHub is simply running a hosted copy on Azure for Copilot users who prefer not to manage infrastructure. Second: the addition completes a **five-lab Copilot roster**. The model picker now spans OpenAI, Anthropic, Google, Microsoft, and Moonshot AI — the broadest competitive set that any major coding tool has ever offered through a single subscription.

Also on July 1, GitHub shipped Copilot CLI auto model routing. It routes each CLI request to the best available model for the task type, and it gives paid subscribers a 10% credit discount for using Auto instead of pinning a model. The timing is not coincidental — expanding the roster and teaching the CLI to route intelligently are the same product move.

---

## The Five-Lab Copilot Roster

As of July 1, 2026, the Copilot model picker includes:

| Lab | Models |
|---|---|
| **OpenAI** | GPT-5 mini, GPT-5.3-Codex, GPT-5.4, GPT-5.4 mini, GPT-5.4 nano, GPT-5.5 |
| **Anthropic** | Claude Haiku 4.5, Sonnet 4.5/4.6/5, Opus 4.5/4.6/4.7/4.8, Fable 5 |
| **Google** | Gemini 2.5 Pro, Gemini 3 Flash (preview), Gemini 3.1 Pro (preview), Gemini 3.5 Flash |
| **Microsoft** | MAI-Code-1-Flash, Raptor mini |
| **Moonshot AI** | Kimi-K2.7-Code ← new |

No other coding tool currently routes across five independent labs through a single subscription. This matters for builders who do not want to maintain five separate API keys, billing accounts, and context window configurations.

---

## What Changes When You Use Kimi K2.7 Through Copilot

If you have used Kimi K2.7 directly through `api.moonshot.cn` or via a self-hosted vLLM/SGLang deployment, the Copilot version differs in a few practical ways:

**Infrastructure:** GitHub hosts Kimi K2.7 on Microsoft Azure (US-based). Your prompts do not route to Moonshot AI's servers. This is the same pattern as the other third-party models in Copilot — Google's models run on Azure too, not on Google Cloud.

**No separate API key:** You authenticate with your GitHub account. No Moonshot AI account, no separate `MOONSHOT_API_KEY`, no per-model rate limit management. If you are already on Copilot Pro/Pro+/Max, the model is available in the picker immediately.

**Pricing via AI credits:** Copilot switched to usage-based AI credit billing in June 2026. Kimi K2.7 is billed at provider list pricing within that credit system — roughly GPT-5.4 mini pricing tier. If you are on an annual Copilot plan, your premium request multiplier applies (0.9x with Auto, 1.0x pinned).

**Model ID:** In API contexts, the model surfaces as `kimi-k2.7-code` within Copilot's routing layer, not as `moonshot-kimi-k2.7-code` or the Moonshot-native identifier. Automation that pins by model name needs to account for this.

---

## Rollout and Availability by Plan

| Plan | Status |
|---|---|
| **Copilot Pro** | Gradual rollout underway — July 1 |
| **Copilot Pro+** | Gradual rollout underway — July 1 |
| **Copilot Max** | Gradual rollout underway — July 1 |
| **Copilot Business** | Coming within weeks; **off by default** |
| **Copilot Enterprise** | Coming within weeks; **off by default** |

Individual users on Pro/Pro+/Max: check the model picker in VS Code. If Kimi K2.7 Code does not appear yet, it is still in gradual rollout to your account — no action needed.

Business and Enterprise users: the model will not appear until your Copilot administrator explicitly enables it in org settings. See the admin section below.

---

## Platform Support

Kimi K2.7 Code is available in Copilot across all major surfaces:

| Surface | Minimum Version |
|---|---|
| Visual Studio Code | 1.127.0+ |
| Visual Studio | 17.14.6+ |
| JetBrains IDEs | 1.9.1-251+ |
| Xcode | Latest Copilot for Xcode |
| Eclipse | Latest Copilot extension |
| GitHub.com (Copilot Chat) | No client update needed |
| GitHub Mobile | No client update needed |
| Copilot CLI | Latest version |
| Cloud Agent | Available |
| Copilot App | Available |

Check your IDE extension version before expecting the model to appear in the picker.

---

## Copilot CLI Auto Routing — July 1

Alongside the Kimi announcement, GitHub shipped auto model selection to Copilot CLI. This is directly related: a larger roster is only useful if the CLI can route intelligently across it.

Auto routing evaluates each request across several dimensions: reasoning complexity, code generation difficulty, bug diagnosis needs, and tool orchestration requirements. It then routes to the best available model for that task type, respecting your administrator's enabled model policies.

**For builders:** The routing decisions align with what experienced users do manually. Simple completions and file lookups go to faster, cheaper models. Multi-file refactors, complex debugging sessions, and agentic tool-call chains go to heavier models. You get near-optimal quality without manually switching models for each task type.

**Cost note:** Paid subscribers get a **10% credit discount** when using Auto mode. Annual plan subscribers receive a 0.9x multiplier instead of 1.0x. If you are currently pinning a model by habit, switching to Auto saves credits and requires less active model management.

**Override:** You can override Auto any time with `/model <name>` in the CLI. Auto is a default, not a lock.

---

## Enterprise Admin Guide: Enabling Kimi K2.7

For Copilot Business and Enterprise, Kimi K2.7 Code requires explicit administrator opt-in:

1. Go to your GitHub organization settings
2. Navigate to **Copilot → Policies**
3. Find **Kimi K2.7 Code** in the model policy list
4. Set to **Enabled** (default is Disabled)

GitHub recommends evaluating your security and compliance requirements before enabling. The relevant considerations:

**Data routing:** Prompts sent to Kimi K2.7 in Copilot go to Azure (US-based), not to Moonshot AI's servers in China. The Azure data processing terms apply, not Moonshot AI's terms. This matters for GDPR assessments — the data controller and processor chain is GitHub/Microsoft, not Moonshot.

**CLOUD Act exposure:** Azure US infrastructure is subject to US law, including CLOUD Act requests. If your organization's compliance framework requires data to remain outside US jurisdictions, this is the same constraint as every other Copilot model.

**Weights are public:** Unlike GPT or Claude, you can audit the Kimi K2.7 Code model weights directly on Hugging Face. For organizations that require model transparency as part of procurement, this is an advantage not available with any other Copilot model.

---

## Builder Decision Guide

**Pick Kimi K2.7 when:**
- You want cost efficiency in the GPT-5.4 mini pricing tier but need strong agentic tool-call performance (K2.7 scored 81.1% on MCPMark vs GPT-5.4 mini at lower scores)
- You want an open-weight model — verifiable weights, MIT license, auditable
- You are routing through Copilot CLI Auto and want the router to have access to a strong, cost-efficient coding model
- You are building HIPAA-adjacent tooling and want to use GitHub/Microsoft as your data processor rather than adding a new AI vendor

**Pick Claude Opus 4.8 or Fable 5 when:**
- You need maximum reasoning depth on complex multi-file refactors
- Cost is not the primary constraint
- You are using extended thinking or context windows above 256K

**Pick MAI-Code-1-Flash when:**
- You need the fastest possible latency on simple completions
- You are in high-volume automation where token cost per request is critical

**Pick Copilot CLI Auto when:**
- You are doing mixed workloads (completions, debugging, agentic tasks in the same session)
- You want the 10% credit discount
- You do not have strong opinions about which model handles which task type

---

## Builder Checklist

- [ ] Update VS Code to 1.127.0+ (or JetBrains to 1.9.1-251+) to access the model picker
- [ ] Check Copilot model picker — if Kimi K2.7 does not appear, the gradual rollout has not reached your account yet
- [ ] If on Business/Enterprise: request admin enable the Kimi K2.7 Code policy in Copilot settings
- [ ] If using Copilot CLI: update to latest, select Auto for the 10% credit discount
- [ ] Review Azure data processing terms if your organization has cross-border data requirements
- [ ] If you need open-weight auditability for procurement: note Kimi K2.7 weights are on Hugging Face (MIT license) — reference the model card in your vendor assessment
- [ ] If you are currently paying for a direct Moonshot AI API subscription for Kimi K2.7: compare costs against Copilot credit pricing — Copilot may be cheaper for typical IDE usage patterns

---

*Previously in Kimi K2.7 coverage: [MCPMark leader and Anthropic-compatible endpoint](/builders-log/kimi-k2-7-code-mcpmark-leader-agentic-builder-guide/) · [Open-weight release and MCP Hermes agent](/builders-log/kimi-k2-7-code-moonshot-open-source-coding-agent-mcp-hermes-builder-guide/) · [vLLM/SGLang self-hosting guide](/builders-log/kimi-k2-7-code-open-weight-coding-agent-vllm-sglang-builder-guide/)*
