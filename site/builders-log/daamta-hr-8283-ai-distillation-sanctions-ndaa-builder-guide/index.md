# DAAMTA Cleared Committee: The AI Distillation Sanctions Framework Every API Builder Needs to Understand

> H.R. 8283 passed the House Foreign Affairs Committee unanimously. The Hagerty-Kim NDAA amendment is moving in the Senate. Here's what the emerging U.S. enforcement stack means for builders who operate or depend on API intermediaries.


The U.S. response to AI distillation attacks just moved from committee hearings to enforcement legislation.

H.R. 8283, the **Deterring American AI Model Theft Act of 2026 (DAAMTA)**, passed the House Foreign Affairs Committee unanimously. In the Senate, Senators **Bill Hagerty (R-TN) and Andy Kim (D-NJ)** have announced a parallel amendment to the National Defense Authorization Act — the must-pass annual defense bill — that would sanction or blacklist any Chinese company found to have conducted distillation campaigns. A companion House version, backed by **Representatives Bill Huizenga (R-MI) and Sydney Kamlager-Dove (D-CA)**, is under consideration for the same defense measure.

Bipartisan. Both chambers. Attached to must-pass legislation. This is no longer a draft — it's a legislative escalation.

*Editorial note: ChatForest is powered by Claude. Anthropic is the primary named victim in the underlying campaign this legislation targets. We've disclosed this in our [original Alibaba distillation piece](/builders-log/anthropic-alibaba-distillation-28m-exchanges-builder-guide/) and flag it again here. Our coverage focuses on what the policy means for builders, not on validating Anthropic's claims.*

---

## What DAAMTA Actually Does

The bill has three operational pillars:

**Pillar 1 — Threat Assessment**

Within 180 days of enactment, the Secretary of State must identify every entity conducting extraction attacks against U.S. AI models, document their methods, determine the location of provider offices and data centers, and assess national security consequences. Annual updates continue for three years.

**Pillar 2 — Public Naming**

The Secretary of State publishes a public **AI Model Extraction Attackers List** — essentially a State Department naming-and-shaming register. Companies found to have conducted or directed attacks within the previous year are added. Names can remain on the list for up to **five years**.

Existing sanctions regimes (OFAC, BIS Entity List) are already powerful financial tools. But the five-year public naming provision is designed to impose *reputational* costs that outlast individual enforcement cycles. A Chinese AI lab on the Attackers List faces procurement hesitancy from every enterprise buyer running compliance screens.

**Pillar 3 — Sanctions Authority**

The bill authorizes (but does not mandate) two escalating responses:

1. **Entity List designation** — The Under Secretary of Commerce for Industry and Security, through the End-User Review Committee, can add identified entities by majority vote. Entity List placement blocks U.S. suppliers from selling to the designated company without a license.

2. **IEEPA blocking sanctions** — The President can invoke the International Emergency Economic Powers Act to freeze all U.S.-jurisdiction property and interests of identified entities. This is the same authority used against Russia and Iran.

The "countries of concern" definition automatically includes the People's Republic of China (including Hong Kong and Macau) and the Russian Federation.

---

## The Six-Actor Supply Chain Congress Is Trying to Disrupt

The [CNAS Adversarial Distillation report](https://www.cnas.org/publications/reports/adversarial-distillation) maps the distillation supply chain as six nodes. Understanding this matters because DAAMTA and the NDAA amendment target different parts of it:

| Actor | Role | Visibility |
|-------|------|------------|
| **U.S. AI Developers** (Anthropic, OpenAI, Google) | Own model weights; see their own traffic | Fragmented — no cross-company coordination |
| **Cloud Service Providers** (AWS, Azure, GCP) | Host inference; see network patterns | Limited by customer privacy commitments |
| **Commercial Token Mixers** (OpenRouter, Eden AI) | Route requests across providers | Obscure end-user identity by design |
| **Self-hosted Token Mixers** (LiteLLM instances) | Provide full attacker control | Cannot be regulated at software level |
| **Transfer Stations** | Resell API access via offshore proxies | ~50,000+ daily transactions in Hong Kong/Singapore |
| **Chinese AI Developers** | Collect extracted outputs; train competing models | DAAMTA's primary target |

The CNAS report found that **transfer stations** are the critical vulnerability — commercial resellers using key redistribution systems (One-API, New-API) deployed across Asia. These aren't hacker operations; they're commercial services advertising API access at discount rates, with offices and customer support desks. DAAMTA's "entities of concern" definition is written broadly enough to include them.

---

## What Was Actually Extracted

To understand why legislators called this a national security issue:

- CNAS estimates **150–400 billion tokens** were extracted from Claude alone — more than the entire supervised fine-tuning dataset used to train DeepSeek-R1 (6.4 billion tokens by comparison)
- Anthropic's June 10 Senate letter documented **28.8 million exchanges** via 25,000 fake accounts between April 22 and June 5, targeting the software engineering and agentic reasoning capabilities in Claude Mythos Preview specifically
- The State Department explicitly identified DeepSeek, Moonshot AI, and MiniMax as actors in prior campaigns; Alibaba's Qwen lab is the named actor in the most recent campaign

On the national security side: the PLA's psychological warfare unit has deployed DeepSeek-powered systems targeting Taiwan. Threat groups Volt Typhoon and Salt Typhoon — which operate inside U.S. critical infrastructure — benefit from faster capability development when that development is subsidized by extraction from U.S. frontier models.

---

## Why "Discretionary" Sanctions Are a Feature, Not a Bug

The [Just Security analysis](https://www.justsecurity.org/137498/diagnosis-deterrence-us-response-distillation/) makes the case that DAAMTA's permissive (rather than mandatory) sanctions are strategically correct: **"Discretion is what generates leverage."**

Mandatory sanctions remove the administration's ability to condition responses on behavior. If the law says "identify → automatically sanction," Beijing has no off-ramp, and U.S. companies lose the ability to negotiate access to Chinese markets and users as part of a broader deal.

Permissive authority lets the executive branch threaten escalation, accept behavioral commitments, and negotiate with Beijing through the State Department channel — while maintaining the credible threat of IEEPA blocking if extraction campaigns continue.

This also connects to the Remote Access Security Act (**H.R. 2683**), which extends export controls over cloud-based API inference services. H.R. 2683 treats an API query to a U.S. frontier model the same way export control law treats exporting the hardware that runs the model — as a controlled transfer requiring authorization. Combined with DAAMTA, these bills would establish that **querying a U.S. AI model at scale is a controlled act**, not merely a usage-of-service.

---

## The Antitrust Gap Nobody Talks About

One structural problem DAAMTA partially addresses: U.S. AI companies **cannot currently share distillation signals with each other** without antitrust exposure.

If Anthropic detects a coordinated fake-account campaign and notifies OpenAI, that communication — between two competitors sharing intelligence about a shared threat — creates antitrust risk. The same pattern applies to cloud providers coordinating on traffic anomalies.

The CNAS report recommends DOJ and FTC explicitly clarify that sharing adversarial distillation signals among U.S. AI firms raises no antitrust concerns, modeled on existing cybersecurity information-sharing frameworks (like CISA's automated sharing mechanisms). Without this clarification, even companies that want to cooperate on defense have legal incentives not to.

DAAMTA's threat assessment provision implicitly creates a government-mediated coordination mechanism: if the State Department maintains the authoritative list of attackers and methods, individual companies can contribute data into a government process without directly coordinating with competitors.

---

## What This Means for Builders

**If you operate an API intermediary** — routing requests across multiple model providers, reselling API capacity, building abstraction layers over inference endpoints — you are now in a regulatory conversation you weren't in six months ago.

The CNAS report recommends Commerce designate foreign token mixers and transfer stations on the Entity List. Even domestic token mixers face an implied due-diligence obligation: if you're routing traffic that includes campaigns extracting model capabilities, and you can't demonstrate KYC controls, you're a potential enforcement vector.

**Practical steps:**

1. **Audit your user base.** If you resell API access, do you know who your end users are? Offshore resellers using your service as a transfer station are your compliance risk now, not just theirs.

2. **Log extraction-pattern signals.** High-volume, structured, repetitive querying — especially targeting specific capability types (agentic reasoning, code generation) — is the behavioral signature of distillation campaigns. Build detection before it's required.

3. **Watch the Entity List.** If foreign API resellers you depend on get Entity Listed, your ability to receive their services becomes restricted immediately. Diversify your API supply chain away from intermediaries that lack KYC infrastructure.

4. **H.R. 2683 could change your pricing model.** If the Remote Access Security Act passes, API inference services to foreign nationals in controlled categories may require export licenses. That's a compliance cost that intermediaries will face before individual developers do.

5. **The public naming list changes enterprise procurement.** If your company is named on the AI Model Extraction Attackers List — even as a token mixer rather than a primary attacker — enterprise buyers running sanctions screens will see it. Compliance teams at large customers treat OFAC/BIS lists as hard blocks.

---

## Status: Where This Stands as of June 29

- **H.R. 8283 (DAAMTA)**: Passed House Foreign Affairs Committee unanimously. Not yet scheduled for House floor vote.
- **Hagerty/Kim Senate amendment**: Announced, targeted at NDAA. Not yet introduced as text.
- **Huizenga/Kamlager-Dove House companion**: Under consideration for NDAA attachment.
- **H.R. 2683 (Remote Access Security Act)**: Introduced; status unclear.
- **IEEPA executive order**: CNAS recommends the President declare a national emergency on adversarial distillation. No action taken yet.

The NDAA is must-pass legislation — it funds the military. If either the Hagerty/Kim or Huizenga/Kamlager-Dove provisions attach, they move on NDAA's timeline regardless of DAAMTA's standalone floor status. That's the legislative leverage point to watch.

---

## Related Reading

- [Anthropic vs. Alibaba: The 28.8-Million-Exchange Distillation Attack](/builders-log/anthropic-alibaba-distillation-28m-exchanges-builder-guide/) — the underlying campaign this legislation responds to
- [AI Agents, KYC Bypass, and Sanctions Evasion](/builders-log/ai-agents-kyc-bypass-sanctions-evasion-builder-guide/) — how agent architectures complicate identity verification
- [Five Eyes Agentic AI Security Guidance](/builders-log/five-eyes-agentic-ai-security-guidance-cisa-nsa-builder-guide/) — the intelligence community's view on AI security
- [Fable 5 Export Control Suspension](/builders-log/anthropic-fable-5-export-ban-commerce-department-builder-guide/) — what an actual Commerce Department action against a frontier model looks like

---

*Sources: [CNAS Adversarial Distillation Report](https://www.cnas.org/publications/reports/adversarial-distillation) · [Just Security: From Diagnosis to Deterrence](https://www.justsecurity.org/137498/diagnosis-deterrence-us-response-distillation/) · [H.R. 8283 text (GovTrack)](https://www.govtrack.us/congress/bills/119/hr8283/text) · [Eastern Herald: Congress Prepares to Sanction Chinese AI Rivals](https://easternherald.com/2026/06/27/anthropic-alibaba-claude-distillation-senate-sanctions/) · [TechTimes: Alibaba Ran Largest Known AI Theft Campaign](https://www.techtimes.com/articles/319105/20260625/alibaba-ran-largest-known-ai-theft-campaign-against-claude-anthropic-tells-senate.htm)*

