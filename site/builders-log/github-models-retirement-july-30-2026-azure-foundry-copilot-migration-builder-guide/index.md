# GitHub Models Retires July 30, 2026: Migration Guide to Microsoft Foundry and GitHub Copilot — Builder's Guide

> GitHub Models—the free AI playground, model catalog, inference API, and BYOK service—shuts down permanently on July 30, 2026, with brownouts on July 16 and July 23. All customers are affected; there is no grandfathering. This guide covers what is going away, who is affected, and how to choose between Microsoft Foundry and GitHub Copilot as your migration target.


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
| [July 16, 2026](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/) | Brownout #1 — temporary errors on all GitHub Models requests |
| [July 23, 2026](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/) | Brownout #2 — temporary errors again, one week before shutdown |
| [July 30, 2026](https://github.blog/changelog/2026-07-30-github-models-is-now-retired/) | Full retirement — all services and UI removed permanently |

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

### Path A: Microsoft Foundry

Best if your use case is **raw model access** — you were calling the inference API from code, CI jobs, or internal tools, and you want to keep calling models programmatically. GitHub's own retirement notice names Microsoft Foundry (the product formerly called Azure AI Foundry, [renamed at Microsoft Ignite in November 2025](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/)) as its first recommended migration target.

**What [Microsoft Foundry](https://ai.azure.com/) provides:**
- A model catalog spanning OpenAI, Meta Llama, Mistral, DeepSeek, and other providers, [browsable in the Foundry model catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/quickstart-github-models?view=foundry-classic)
- REST inference endpoints; Microsoft's own migration guide has customers moving off the deprecated Azure AI Inference beta SDK onto the [generally-available OpenAI-compatible `/v1` API](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/quickstart-github-models?view=foundry-classic)
- [Keyless authentication via Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/quickstart-github-models?view=foundry-classic), replacing GitHub token auth
- Per-subscription rate limits (tokens/minute, requests/minute) that vary by model, [documented in Foundry's quotas and limits reference](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/quotas-limits) — there is no free "GitHub Models"-style tier; per Microsoft's own upgrade guide, "GitHub Models are free with rate limits. After you upgrade to Foundry Models, usage is billed to your Azure subscription based on the deployment type you choose."

**The friction:**
- You need an Azure subscription — GitHub Models required only a GitHub account
- Authentication changes: instead of a GitHub personal access token, you authenticate with Azure credentials
- There is no free-tier equivalent to GitHub Models' free rate-limited access; [production workloads are billed to the Azure subscription based on deployment type](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/quickstart-github-models?view=foundry-classic) and must be tracked in the Azure portal
- Any code that used GitHub's hosted inference endpoint (`models.inference.ai.azure.com` via GitHub token) needs an endpoint and authentication update — see [Microsoft's "Upgrade from GitHub Models to Microsoft Foundry Models" guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/quickstart-github-models?view=foundry-classic) for the exact steps

**Who should use this path:** Teams calling the GitHub Models inference API from code — CI scripts, backend services, internal tooling — who need continued programmatic model access.

### Path B: GitHub Copilot

Best if your use case is **developer workflow integration** — you used GitHub Models for code assistance, PR review, issue triage, or repository-level AI tasks that live inside the GitHub product experience.

**What GitHub Copilot provides:**
- Model access through [GitHub's Copilot interface](https://github.com/features/copilot/plans) — CLI, VS Code, Visual Studio, JetBrains, Eclipse, Xcode, and github.com
- Agent mode/agent sessions that work directly on GitHub repositories, [included on every plan including Free](https://github.com/features/copilot/plans)
- [Usage-based "AI Credit" billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) — credits are consumed per token (input, output, and cached), at published per-model rates, since the June 1, 2026 billing switch
- [Copilot Free plan](https://github.com/features/copilot/plans): no credit card required, 2,000 code completions and 50 chat requests per month
- [Bring-your-own-key (BYOK) support](https://github.blog/changelog/2025-11-20-enterprise-bring-your-own-key-byok-for-github-copilot-is-now-in-public-preview/) (public preview since November 2025, [expanded to the Copilot app in June 2026](https://github.blog/changelog/2026-06-23-github-copilot-app-support-for-byok/)) — lets you connect your own API keys from Anthropic, Microsoft Foundry, OpenAI, or xAI, with billing handled directly by that provider instead of Copilot credits

**Who should use this path:** Developers who primarily used the GitHub Models playground or API for development tasks that could equally run inside Copilot sessions, or who specifically relied on GitHub Models' BYOK and want an equivalent inside GitHub's product surface.

---

## Choosing Between the Two

| Situation | Recommended path |
|-----------|-----------------|
| Inference API calls from CI / scripts | Microsoft Foundry |
| Internal tools using the GitHub Models REST endpoint | Microsoft Foundry |
| Prototyping and model comparison in a UI | Microsoft Foundry (Foundry portal/playground) |
| BYOK routing through your own keys | [GitHub Copilot BYOK](https://github.blog/changelog/2025-11-20-enterprise-bring-your-own-key-byok-for-github-copilot-is-now-in-public-preview/) (public preview) — Microsoft Foundry itself does not market a "BYOK" feature; it is one of the providers Copilot's BYOK can connect to |
| Code completion and PR review inside IDE | GitHub Copilot |
| GitHub Actions workflows that call models | GitHub Copilot (Copilot Extensions) |
| Issue triage and repo-level AI assistance | GitHub Copilot |
| Zero-cost experimentation (very light use) | [GitHub Copilot Free tier](https://github.com/features/copilot/plans) |

---

## Builder Action List

**Before July 16 (brownout #1 — 4 days away as of this writing):**

1. **Audit your codebase and CI pipelines.** Search for `models.inference.ai.azure.com`, `github.com/models`, or any reference to GitHub Models endpoints. CI configs, `.github/workflows/`, internal scripts, and developer portal code are common locations.

2. **Inventory what you call.** List which models you were using and what tasks. This determines whether Microsoft Foundry or GitHub Copilot is the better target.

3. **Create an Azure subscription** if you plan to use Microsoft Foundry and do not already have one. Set up billing alerts before routing production traffic — Foundry has no free-rate-limited tier equivalent to GitHub Models, per [Microsoft's own migration guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/quickstart-github-models?view=foundry-classic).

4. **Update authentication.** Replace GitHub personal access tokens used for model inference with Azure credentials or managed identities.

5. **Update inference endpoints.** Swap the GitHub Models endpoint URL for your chosen Microsoft Foundry deployment endpoint, [following Microsoft's upgrade steps](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/quickstart-github-models?view=foundry-classic). The API surface is largely OpenAI-compatible, so prompt payloads usually transfer unchanged.

**Between July 16 and July 23 (brownout window):**

6. **Treat brownout failures as validation.** If something breaks during the July 16 brownout that you thought you migrated, fix it before July 23. Use the two brownouts as two opportunities to verify coverage.

**After July 30:**

7. **Remove any remaining GitHub Models references from documentation, onboarding guides, and internal wikis.** The endpoints are gone; dead references will confuse future contributors.

---

## What Is Not Changing

GitHub Copilot itself is unaffected. The Copilot app, coding agent, JetBrains integration, and the AI-credit spend controls GitHub shipped in early July 2026 — [session limits for the CLI/SDK (July 1)](https://github.blog/changelog/2026-07-01-set-ai-credit-session-limits-in-copilot-cli-and-sdk/) and [AI credit pool caps for cost centers (July 2)](https://github.blog/changelog/2026-07-02-cost-centers-now-support-included-usage-caps/) — continue operating. The retirement is specific to the GitHub Models product — the separate free-standing model catalog and inference service.

Azure OpenAI and Microsoft Foundry are not being retired. GitHub is migrating its own model-serving layer into Microsoft's platform rather than running a separate one — [GitHub's own retirement notice frames Microsoft Foundry as the direct successor for model access](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/).

---

## Context

GitHub Models [launched on August 1, 2024](https://github.blog/news-insights/product-news/introducing-github-models/) as a way to lower the entry barrier for AI prototyping inside the GitHub ecosystem. Running a model playground and inference service alongside a developer platform turned out to be a distraction from GitHub's core product, and Microsoft already runs a purpose-built model-serving platform in Microsoft Foundry. Consolidating onto that platform is a reasonable decision even if the transition is disruptive for current users.

The hard deadline and brownout schedule suggests Microsoft wants this migration completed cleanly, not dragged out. Plan accordingly.

