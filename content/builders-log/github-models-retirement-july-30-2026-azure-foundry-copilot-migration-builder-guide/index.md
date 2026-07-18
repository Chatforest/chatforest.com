---
title: "GitHub Models Retires July 30, 2026: Migration Guide to Azure AI Foundry and GitHub Copilot — Builder's Guide"
date: 2026-07-12
description: "GitHub Models—the free AI playground, model catalog, inference API, and BYOK service—shuts down permanently on July 30, 2026, with brownouts on July 16 and July 23. All customers are affected; there is no grandfathering. This guide covers what is going away, who is affected, and how to choose between Azure AI Foundry and GitHub Copilot as your migration target."
tags: ["github-models", "github-copilot", "azure-ai-foundry", "model-retirement", "migration", "inference-api", "developer-tools", "cost-management", "ai-platform"]
---

GitHub Models, GitHub's free AI playground and inference API, [retires permanently on **July 30, 2026**](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/). The shutdown applies to every customer — free, Team, and Enterprise GitHub plans alike. No grandfathering, no extended deprecation period. The playground UI disappears, the model catalog goes offline, all inference API endpoints stop responding, and bring-your-own-key (BYOK) access ends simultaneously.

Brownouts on **July 16 and July 23** will cause temporary outages in advance of full shutdown. If you have any code calling GitHub Models endpoints, you need to migrate before July 16 to avoid disruption.

This is a research-based guide. We reviewed [GitHub's changelog](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/), official migration documentation, and third-party coverage. We did not test the services ourselves.

---

## What Is Being Retired

GitHub Models launched as an experimental platform for discovering and prototyping with AI models directly from GitHub. It offered:

- **Playground** — interactive browser UI for chatting with and comparing models
- **Model catalog** — a searchable list of available models (OpenAI, Meta, Mistral, and others)
- **Inference API** — REST and SDK endpoints for sending requests from code, with GitHub token authentication
- **BYOK** — bring-your-own-key support so you could route requests through your own OpenAI or Azure keys

All four components shut down on July 30. There is no successor service within GitHub.

---

## Timeline

| Date | Event |
|------|--------|
| [June 16, 2026](https://github.blog/changelog/2026-06-16-github-models-is-no-longer-available-to-new-customers/) | New customers blocked from signing up |
| **July 16, 2026** | Brownout #1 — temporary errors on all GitHub Models requests |
| **July 23, 2026** | Brownout #2 — temporary errors again, one week before shutdown |
| **July 30, 2026** | Full retirement — all services and UI removed permanently |

The brownouts are intentional: they are designed to expose hidden dependencies before permanent shutdown. If your CI pipeline, documentation generator, or internal tool makes GitHub Models API calls, those pipelines will fail during the brownouts. **Discovering failures during a planned brownout is better than discovering them on July 30.**

---

## Who Is Affected

Every current GitHub Models user is affected:

- **Solo developers** who used the playground for experimentation lose free, low-friction model access
- **Small teams** using the inference API in scripts or CI jobs need to reroute those calls
- **Enterprises** that integrated GitHub Models into internal tooling (issue triage, doc generation, dev portals) have migration work to do regardless of how small the code footprint looks

The only developers not affected are those who never used GitHub Models or who already migrated after June 16 when new signups closed.

---

## Migration Paths

GitHub recommends two targets. The right choice depends on what you were using GitHub Models for.

### Path A: Azure AI Foundry

Best if your use case is **raw model access** — you were calling the inference API from code, CI jobs, or internal tools, and you want to keep calling models programmatically.

**What Azure AI Foundry provides:**
- Broad model catalog (OpenAI, Meta Llama, Mistral, and others — similar range to GitHub Models)
- REST inference endpoints with OpenAI-compatible API surfaces
- Azure authentication (AAD/Entra ID, managed identities) replacing GitHub token auth
- Evaluation tooling, deployment management, and enterprise quota controls
- Free tier available, but limited to a few thousand transactions per month

**The friction:**
- You need an Azure subscription — GitHub Models required only a GitHub account
- Authentication changes: instead of a GitHub personal access token, you authenticate with Azure credentials
- Free tier limits are much narrower than what GitHub Models offered; production workloads incur metered costs that must be tracked in the Azure portal
- Any code that used GitHub's hosted inference endpoint (`models.inference.ai.azure.com` via GitHub token) needs an endpoint and authentication update

**Who should use this path:** Teams calling the GitHub Models inference API from code — CI scripts, backend services, internal tooling — who need continued programmatic model access.

### Path B: GitHub Copilot

Best if your use case is **developer workflow integration** — you used GitHub Models for code assistance, PR review, issue triage, or repository-level AI tasks that live inside the GitHub product experience.

**What GitHub Copilot provides:**
- Model access through GitHub's Copilot interface (CLI, VS Code, JetBrains, web)
- Agents that work directly on GitHub repositories (Copilot coding agent, agent sessions)
- AI credit billing that tracks per-session and per-user usage
- Free tier for Copilot Free plan users (with monthly credit limits)

**Who should use this path:** Developers who primarily used the GitHub Models playground or API for development tasks that could equally run inside Copilot sessions or Copilot Extensions.

---

## Choosing Between the Two

| Situation | Recommended path |
|-----------|-----------------|
| Inference API calls from CI / scripts | Azure AI Foundry |
| Internal tools using the GitHub Models REST endpoint | Azure AI Foundry |
| Prototyping and model comparison in a UI | Azure AI Foundry (AI Foundry playground) |
| BYOK routing through your own keys | Azure AI Foundry (native BYOK support) |
| Code completion and PR review inside IDE | GitHub Copilot |
| GitHub Actions workflows that call models | GitHub Copilot (Copilot Extensions) |
| Issue triage and repo-level AI assistance | GitHub Copilot |
| Zero-cost experimentation (very light use) | GitHub Copilot Free tier |

---

## Builder Action List

**Before July 16 (brownout #1 — 4 days away as of this writing):**

1. **Audit your codebase and CI pipelines.** Search for `models.inference.ai.azure.com`, `github.com/models`, or any reference to GitHub Models endpoints. CI configs, `.github/workflows/`, internal scripts, and developer portal code are common locations.

2. **Inventory what you call.** List which models you were using and what tasks. This determines whether Azure AI Foundry or GitHub Copilot is the better target.

3. **Create an Azure subscription** if you plan to use Azure AI Foundry and do not already have one. Set up billing alerts before routing production traffic.

4. **Update authentication.** Replace GitHub personal access tokens used for model inference with Azure credentials or managed identities.

5. **Update inference endpoints.** Swap the GitHub Models endpoint URL for your chosen Azure AI Foundry deployment endpoint. The API surface is largely OpenAI-compatible, so prompt payloads usually transfer unchanged.

**Between July 16 and July 23 (brownout window):**

6. **Treat brownout failures as validation.** If something breaks during the July 16 brownout that you thought you migrated, fix it before July 23. Use the two brownouts as two opportunities to verify coverage.

**After July 30:**

7. **Remove any remaining GitHub Models references from documentation, onboarding guides, and internal wikis.** The endpoints are gone; dead references will confuse future contributors.

---

## What Is Not Changing

GitHub Copilot itself is unaffected. The Copilot app, coding agent, JetBrains integration, browser tools, and credit controls announced in July 2026 continue operating. The retirement is specific to the GitHub Models product — the separate free-standing model catalog and inference service.

Azure OpenAI and Azure AI Foundry are not being retired. Microsoft is expanding those services; GitHub is migrating its own model-serving layer into them rather than running a separate platform.

---

## Context

GitHub Models launched in 2024 as a way to lower the entry barrier for AI prototyping inside the GitHub ecosystem. Running a model playground and inference service alongside a developer platform turned out to be a distraction from GitHub's core product, and Microsoft has the same capability with more depth in Azure AI Foundry. Consolidating onto a purpose-built inference platform is a reasonable decision even if the transition is disruptive for current users.

The hard deadline and brownout schedule suggests Microsoft wants this migration completed cleanly, not dragged out. Plan accordingly.
