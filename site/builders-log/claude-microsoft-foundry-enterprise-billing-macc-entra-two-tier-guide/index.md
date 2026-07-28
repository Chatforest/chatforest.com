# Claude on Microsoft Azure Foundry: What Enterprise Builders Actually Get (And What They Don't)

> Claude is now in Microsoft Azure Foundry. MACC billing eligibility and Entra ID auth are real wins. But Claude is in the partner tier, not the Azure tier — and that gap has direct SLA, data-residency, and billing consequences for enterprise teams.


Claude is now [available in Microsoft Azure Foundry](https://azure.microsoft.com/en-us/blog/claude-in-microsoft-foundry-is-now-generally-available/) — the same model catalog where Microsoft's own MAI models and OpenAI models live. Enterprise teams that have been managing a parallel Anthropic billing relationship on top of their Azure spend now have an alternative. But the "first-class status" framing that circulated after Microsoft Build 2026 overstates what actually changed. Here is the precise picture.

---

## Why This Happened: The OpenAI Partnership Restructure

The upstream driver is a [partnership amendment Microsoft and OpenAI announced on April 27, 2026](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/). The key structural change: Microsoft's license to OpenAI IP is now non-exclusive through 2032, and OpenAI can now serve its products to customers across any cloud provider, including AWS and Google Cloud. Microsoft's remaining leverage is contractual rather than a hard exclusivity window — in the companies' own words, "OpenAI products will ship first on Azure, unless Microsoft cannot and chooses not to support the necessary capabilities."

The consequence for Microsoft: it now has structural incentive to make Azure genuinely competitive for builders using Claude, Gemini, and other non-OpenAI models. If OpenAI goes to AWS, Microsoft cannot afford to leave enterprise teams without good alternatives on Azure.

That is why Claude in Azure Foundry matters more now than it would have six months ago.

---

## The Two-Tier Reality

Azure Foundry's model catalog has two formal categories:

**Tier 1 — Foundry Models Sold by Azure**
Microsoft's own MAI and Phi model families, plus OpenAI models. These run on Azure regional compute and are backed by Microsoft support contracts. Azure OpenAI specifically [carries a Microsoft availability SLA and offers a gated zero-data-retention option](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/faq) for EA/MCA customers.

**Tier 2 — Foundry Models from Partners and Community**
Claude (Anthropic), Cohere, Meta Llama, Mistral, and others. Microsoft's Product Terms [explicitly label these as "Non-Microsoft Products"](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners). For Claude specifically, Microsoft [now offers two hosting configurations](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison): a subset of models (Opus 5, Opus 4.8, Sonnet 5, Haiku 4.5) can run on Azure regional compute end-to-end, while other models remain hosted only on Anthropic's own infrastructure. Either way, Anthropic — not Microsoft — is the operator and the party that provides any SLA; day-to-day support requests (billing, deployment, Marketplace issues) do route through Microsoft Support.

This distinction is not marketing nuance. It has direct operational consequences for procurement, compliance, and incident management.

---

## What Claude on Foundry Actually Gives You

### MACC Eligibility — The Biggest Practical Win

Claude usage now counts toward your Microsoft Azure Consumption Commitment. If your organization has a committed Azure spend agreement (EA or MCA-E), Claude API calls — billed in [Claude Consumption Units (CCU)](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-billing) — reduce that commitment balance the same way any other Azure Marketplace consumption does.

Before Foundry, teams using both Azure and Anthropic direct managed two separate vendor relationships, two separate billing cycles, and two separate approval processes for procurement. Now those teams can consolidate. Claude charges appear on the Azure invoice. Procurement approves one vendor.

This is a real operational improvement for enterprise teams already inside the Microsoft commercial ecosystem.

### Entra ID Authentication

Claude on Foundry [supports Microsoft Entra (formerly Azure Active Directory) authentication](https://azure.microsoft.com/en-us/blog/claude-in-microsoft-foundry-is-now-generally-available/), and your existing Azure RBAC policies apply. You can manage Claude API access through the same identity plane as the rest of your Azure stack.

For organizations with strict IAM requirements — particularly those with centralized identity governance — this removes a common friction point in getting Claude approved for production use.

### Unified Azure Portal and Monitoring

Foundry provides a single portal for model deployment and quota management across all catalog models, with Claude appearing alongside other models. [Cost and usage roll up into Azure Cost Management as a single CCU line](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-billing), with per-model token and request detail available in the Foundry portal's Monitoring tab.

---

## What Claude on Foundry Does Not Give You

### No Microsoft-Backed SLA

Microsoft's uptime SLA does not apply to Claude. [Anthropic is the operator and provides any SLA for Claude on Foundry](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison) — for both the Azure-hosted and Anthropic-hosted versions. If Claude is unavailable, billing and deployment issues route through Microsoft Support, but the availability guarantee itself is Anthropic's, not Microsoft's.

For teams whose contracts require a Microsoft-backed SLA on all AI services, Claude on Foundry does not meet that requirement.

### Zero-Data-Retention Is Anthropic's Call, Not an Automatic Azure Guarantee

Azure OpenAI's infrastructure-level zero-data-retention guarantee does not extend to Claude — [Anthropic, not Azure, is the data processor](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison) for Claude prompts and completions, governed by [Anthropic's Data Processing Addendum](https://www.anthropic.com/legal/data-processing-addendum). That doesn't mean zero retention is unavailable, though: Microsoft's GA announcement states that ["for high-sensitivity workloads, zero data retention is also available, so prompts and completions are not retained by Anthropic after the API call completes."](https://azure.microsoft.com/en-us/blog/claude-in-microsoft-foundry-is-now-generally-available/) In practice this has been an opt-in Anthropic administers, not something enabled by default — per [discussion on Microsoft's own Q&A forum](https://learn.microsoft.com/en-us/answers/questions/5843526/are-the-anthropic-models-deployed-under-microsoft), Anthropic's ZDR historically required an enterprise agreement and a separate request, and Microsoft now points customers to [Anthropic's Azure data-retention request form](https://claude.com/form/azure-data-retention-request) to enable it.

Teams with strict data-retention compliance requirements (healthcare, financial services, some government contexts) should confirm ZDR is actually enabled for their specific deployment, rather than assuming it applies automatically.

### EU Data Residency: Not Yet

EU regional infrastructure support is listed as "Coming 2026" in Anthropic's compliance documentation, but [as of July 2026 no EU data zone exists for Claude models](https://www.infoq.com/news/2026/07/claude-foundry-ga-europe/) — confirmed by [Microsoft's own hosting comparison](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison), which lists Data Zone Standard deployment as US-only for Claude. Teams with EU data residency requirements cannot currently satisfy them through Claude on Foundry.

### No Access on Free Trial, Startup Credits, or MSDN Subscriptions

This is the sharpest operational hazard. [The following subscription types aren't supported for Claude models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison): free trial, student, other credit-based or sponsored subscriptions, Enterprise Accounts based in South Korea, and Cloud Solution Provider (CSP) subscriptions. [Visual Studio/MSDN subscriptions can't purchase Marketplace SaaS offers at all](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners), which is how Claude is sold.

If you are on a free trial or a startup-credit program (e.g., Microsoft for Startups Founders Hub), Claude usage charges [go directly to the credit card on file, bypassing Azure credits entirely](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners#anthropic). Multiple developers have reported unexpected invoices this way: a Tokyo founder was billed [about $1,600](https://www.theregister.com/software/2026/03/13/founder-finds-azure-startup-credits-dont-apply-to-claude/5228441) after testing Claude via Azure AI Foundry with Microsoft for Startups credits, and another Founders Hub participant [documented two consecutive invoices totaling $17,493.01](https://techcommunity.microsoft.com/discussions/startupsatmicrosoft/17493-in-undisclosed-marketplace-charges-with-no-cost-visibility-no-recourse-no-/4510844) that kept accumulating even after removing the Claude deployment mid-cycle.

**Check your subscription type before enabling Claude in Foundry.** If you are not on EA or MCA-E, use Anthropic's direct API instead.

---

## Claude Models Currently in Foundry

[Model lifecycle status (GA vs. preview) varies by model and by hosting option, and changes frequently](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models) — verify current status in Microsoft's live catalog before deploying:

| Model | Context | Notes |
|-------|---------|-------|
| claude-opus-4-8 | 1M tokens | Latest Opus |
| claude-opus-4-7 | 1M tokens | — |
| claude-opus-4-6 | 1M tokens | — |
| claude-sonnet-4-6 | 200K tokens | — |
| claude-sonnet-4-5 | 200K tokens | — |
| claude-haiku-4-5 | 200K tokens | — |
| claude-mythos-preview | Gated | [Defensive cybersecurity only; Anthropic-discretion access](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models) |

All models support text and image input (vision) and [tool use, including file search and code execution](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners#anthropic); native web search/fetch tools are part of Anthropic's broader API but aren't listed among the capabilities Foundry currently exposes. Supported languages: [English, French, Arabic, Chinese, Japanese, Korean, Spanish, Hindi](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners#anthropic).

---

## Who Should Use Claude via Foundry vs. Anthropic Direct

**Use Foundry if:**
- You are on EA or MCA-E and want MACC consumption credit
- Your organization requires Entra ID for all API access
- Your procurement process requires a single Azure vendor
- You want unified billing and single-portal usage monitoring

**Use Anthropic direct if:**
- You are on a free trial, startup credits, or MSDN subscription
- You need EU data residency (not available on Foundry yet)
- You need a Microsoft-backed SLA
- You are building a prototype and want the simplest path

**Wait before deciding if:**
- EU data residency is a hard requirement — Foundry support is coming in 2026
- You need zero-data-retention guarantees and are still evaluating Anthropic's data handling terms

---

## The Strategic Picture

The Microsoft-OpenAI exclusivity change gives Microsoft structural incentive to close the two-tier gap over time. If enterprise customers start choosing Claude on AWS over Claude on Azure because AWS offers better SLA or data-handling terms, Microsoft loses. The pressure to eventually give partner-tier models the same infrastructure guarantees as its own models is real.

For builders evaluating Azure as a Claude deployment path, the current answer is: it works for a specific enterprise profile (EA/MCA-E, Entra ID required, MACC optimization wanted). It does not work as a drop-in replacement for all Azure-native deployment requirements.

Related: [Anthropic Eyes Microsoft's Maia 200 for Claude Inference](/builders-log/anthropic-microsoft-maia-200-custom-silicon-claude-inference-cost/) — if that deal closes, it would change the infrastructure picture for Claude on Azure in 2027.

