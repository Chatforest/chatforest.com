# Claude on Microsoft Azure Foundry: What Enterprise Builders Actually Get (And What They Don't)

> Claude is now in Microsoft Azure Foundry. MACC billing eligibility and Entra ID auth are real wins. But Claude is in the partner tier, not the Azure tier — and that gap has direct SLA, data-residency, and billing consequences for enterprise teams.


Claude is now available in Microsoft Azure Foundry — the same model catalog where Microsoft's own MAI models and OpenAI models live. Enterprise teams that have been managing a parallel Anthropic billing relationship on top of their Azure spend now have an alternative. But the "first-class status" framing that circulated after Microsoft Build 2026 overstates what actually changed. Here is the precise picture.

---

## Why This Happened: The OpenAI Partnership Restructure

The upstream driver is a partnership amendment Microsoft and OpenAI announced on April 27, 2026. The key structural change: Microsoft's license to OpenAI IP is now non-exclusive through 2032. OpenAI can distribute its products on AWS, Google Cloud, or any other cloud. In exchange, Microsoft retains a four-month first-mover window — new OpenAI frontier models must debut on Azure before they appear on competing clouds.

The consequence for Microsoft: it now has structural incentive to make Azure genuinely competitive for builders using Claude, Gemini, and other non-OpenAI models. If OpenAI goes to AWS, Microsoft cannot afford to leave enterprise teams without good alternatives on Azure.

That is why Claude in Azure Foundry matters more now than it would have six months ago.

---

## The Two-Tier Reality

Azure Foundry's model catalog has two formal categories:

**Tier 1 — Foundry Models Sold by Azure**
Microsoft's own MAI and Phi model families, plus OpenAI models. These run on Azure regional compute, carry Microsoft enterprise SLAs, support Azure zero-data-retention, and are backed by Microsoft support contracts.

**Tier 2 — Foundry Models from Partners and Community**
Claude (Anthropic), Cohere, Meta Llama, Mistral, and others. Microsoft's Product Terms explicitly label these as "Non-Microsoft Products." Support is provided by the vendor — in Claude's case, by Anthropic — not by Microsoft. Claude runs on Anthropic-managed infrastructure, not Azure regional compute.

This distinction is not marketing nuance. It has direct operational consequences for procurement, compliance, and incident management.

---

## What Claude on Foundry Actually Gives You

### MACC Eligibility — The Biggest Practical Win

Claude usage now counts toward your Microsoft Azure Consumption Commitment. If your organization has a committed Azure spend agreement (EA or MCA-E), Claude API calls reduce that commitment balance — the same as any other Azure service.

Before Foundry, teams using both Azure and Anthropic direct managed two separate vendor relationships, two separate billing cycles, and two separate approval processes for procurement. Now those teams can consolidate. Claude charges appear on the Azure invoice. Procurement approves one vendor.

This is a real operational improvement for enterprise teams already inside the Microsoft commercial ecosystem.

### Entra ID Authentication

Claude on Foundry supports Microsoft Entra (formerly Azure Active Directory) authentication. Your existing Azure RBAC policies apply. SSO works. You can manage Claude API access through the same identity plane as the rest of your Azure stack.

For organizations with strict IAM requirements — particularly those with centralized identity governance — this removes a common friction point in getting Claude approved for production use.

### Unified Azure Portal and Monitoring

Foundry provides a single interface for model deployment, usage monitoring, and quota management across all catalog models. Claude appears alongside other models. Azure Monitor integration works.

---

## What Claude on Foundry Does Not Give You

### No Microsoft-Backed SLA

Microsoft's uptime SLA does not apply to Claude. Anthropic's own terms govern availability guarantees. If Claude is unavailable, your escalation path is to Anthropic support — not to Microsoft.

For teams whose contracts require a Microsoft-backed SLA on all AI services, Claude on Foundry does not meet that requirement.

### No Azure Zero-Data-Retention

Azure OpenAI's zero-data-retention guarantee — where prompt and response data is not logged at the infrastructure level — does not apply to Claude. Claude runs on Anthropic-managed infrastructure. Anthropic's own data handling policies apply.

Teams with strict data-retention compliance requirements (healthcare, financial services, some government contexts) should verify Anthropic's current data handling terms before relying on Claude via Foundry to meet those requirements.

### EU Data Residency: Not Yet

EU regional infrastructure support is listed as "Coming 2026" in Foundry documentation. As of June 2026, it is not available. Teams with EU data residency requirements cannot currently satisfy them through Claude on Foundry.

### No Access on Free Trial, Startup Credits, or MSDN Subscriptions

This is the sharpest operational hazard. Claude on Foundry is only available on Enterprise Agreement (EA) and Microsoft Customer Agreement for Enterprise (MCA-E) subscriptions. Cloud Solution Provider (CSP) subscriptions cannot purchase Claude.

If you are on a free trial, a Visual Studio/MSDN subscription, or using Microsoft startup credits, Claude usage charges go directly to the credit card on file — bypassing Azure credits entirely. Multiple developers have reported unexpected invoices ranging from $1,600 to over $17,000 from accidentally enabling Claude on non-EA subscriptions.

**Check your subscription type before enabling Claude in Foundry.** If you are not on EA or MCA-E, use Anthropic's direct API instead.

---

## Claude Models Currently in Foundry

All models are in Public Preview as of June 2026:

| Model | Context | Notes |
|-------|---------|-------|
| claude-opus-4-8 | 1M tokens | Latest Opus |
| claude-opus-4-7 | 1M tokens | — |
| claude-opus-4-6 | 1M tokens | — |
| claude-sonnet-4-6 | 200K tokens | — |
| claude-sonnet-4-5 | 200K tokens | — |
| claude-haiku-4-5 | 200K tokens | — |
| claude-mythos-preview | Gated | Defensive cybersecurity only; Anthropic-discretion access |

All models support vision, tool use, code execution, and web search/fetch. Supported languages: English, French, Arabic, Chinese, Japanese, Korean, Spanish, Hindi.

---

## Who Should Use Claude via Foundry vs. Anthropic Direct

**Use Foundry if:**
- You are on EA or MCA-E and want MACC consumption credit
- Your organization requires Entra ID for all API access
- Your procurement process requires a single Azure vendor
- You want unified billing and Azure Monitor integration

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

