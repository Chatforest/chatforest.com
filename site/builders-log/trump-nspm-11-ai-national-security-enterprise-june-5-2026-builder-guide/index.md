# NSPM-11: Trump's Military AI Directive Mandates Multi-Vendor Adoption and Bans Vendor Kill Switches — What It Means for Builders

> Signed June 5, NSPM-11 directs the DoD and intelligence community to accelerate AI adoption, mandate multiple vendors, and contractually prohibit commercial providers from disabling deployed systems. Here's what it changes for builders working on or near government AI.


**At a glance:** President Trump signed NSPM-11 (National Security Presidential Memorandum 11) on June 5, 2026, directing the U.S. military and intelligence community to accelerate AI adoption. The memorandum replaces the Biden administration's NSM-25, establishes four pillars (Adoption, Adaptation, Assurance, Accountability), mandates multi-vendor procurement, and requires contractual clauses prohibiting commercial AI providers from disabling or modifying deployed systems without federal approval. Part of our **[Builder's Log](/builders-log/)**.

This is the companion piece to our [June 2 EO guide](/builders-log/trump-ai-executive-order-june-2026-signed-frontier-model-voluntary-review-builder-guide/). The EO covered civilian agencies, voluntary frontier model review, and the AI cybersecurity clearinghouse. NSPM-11 is the other half: it governs the DoD, the intelligence community, and the classified environments where the different rules apply.

---

## What NSPM-11 Actually Does

NSPM-11 organizes national security AI policy around four pillars, which it calls **Adoption, Adaptation, Assurance, and Accountability**.

**Adoption** is the first pillar — and its placement is intentional. The posture is speed over caution. The memorandum directs agencies to eliminate "unnecessary barriers to rapid deployment" and to maintain "deep, proactive partnerships with industry to make the most advanced frontier models broadly available to national security professionals without delay."

The phrase "without delay" does real work here. NSM-25, the Biden-era document this replaces, set up multi-layered governance review as the precondition for DoD AI deployment. NSPM-11 inverts the default: deploy first, govern within the deployment, not before it.

**Adaptation** directs the national security enterprise to leverage "commercial or open-source AI technologies" from "diverse suppliers across the private sector, large and small." The language is deliberately broad: it covers hyperscale labs (Anthropic, OpenAI, Google DeepMind) and smaller vendors. It also explicitly includes open-source.

**Assurance** is where the vendor-facing requirements live. More on this below.

**Accountability** closes the loop back to command structure — commanders and directors remain accountable for how AI systems perform in their operations. This is the governance mechanism: not pre-clearance, but chain-of-command responsibility after deployment.

---

## The Multi-Vendor Mandate: 120 Days

Within 120 days of June 5 — by approximately **October 3, 2026** — the Secretary of War, the DNI, and the heads of agencies with Intelligence Community elements must review and update procurement processes to ensure "rapid onboarding of the most advanced AI models from multiple vendors."

This is a direct repudiation of single-vendor lock-in. The DoD's current situation — where OpenAI holds the primary classified AI contract position following Anthropic's removal in February — is explicitly what this provision addresses.

What "multiple vendors" means in practice:

**For frontier labs:** Anthropic, Google DeepMind, xAI, and others are now explicitly targeted as onboarding candidates, not optional additions. The procurement update is a directive, not a suggestion. Labs that have been locked out of classified environments (like Anthropic, due to the ongoing standoff) have a policy-level mandate behind re-entry requests — assuming the underlying standoff with DoD resolves.

**For mid-scale and open-source labs:** The language covers "diverse suppliers...large and small." Mistral, Cohere, and similar vendors with government-adjacent products have a procurement window opening. The 120-day review is the signal to engage now.

**For builders on GovCloud:** If your application runs on a single underlying model in a government context, the procurement environment now pushes toward multi-model architectures. Building model-agnostic abstraction layers is not just good engineering — it aligns with the procurement direction your government customers are being directed toward.

---

## The Kill-Switch Prohibition: What It Means for Enterprise AI Contracts

The Assurance pillar contains the most significant contract-level change for commercial AI providers:

> AI systems adopted shall be designed to be reliable, robust, steerable, and controllable, with **contractual clauses ensuring no commercial entity or adversary can prevent use of, disable or degrade, or materially modify AI systems without Federal Government knowledge and approval**.

This is a kill-switch prohibition. Any AI provider selling to the DoD or IC must contractually commit that they cannot unilaterally:

- Disable the deployed system
- Degrade its capabilities
- Materially modify its behavior

...without the federal government's knowledge and explicit approval.

The tension here is significant. AI providers maintain emergency shutdown capabilities for exactly the kinds of systems the government wants to deploy. Anthropic's conflict with DoD — the reason Claude was banned from classified networks in February — centered precisely on guardrails that Anthropic cannot contractually waive. The Assurance pillar, as written, requires providers to relinquish unilateral control over those guardrails.

For builders deploying commercial AI in government contexts, this creates a three-way tension:

**Lab safety policy vs. contract terms**: Providers like Anthropic have hard limits they will not waive — autonomous weapons targeting, domestic mass surveillance. NSPM-11's Assurance clause requires contractual commitments that potentially conflict with those limits. The resolution is not obvious.

**Deprecation timelines**: Even ordinary model deprecation — retiring Claude 3.5 in favor of Claude 4, for example — could qualify as "materially modifying" a deployed system. Government contracts will need to specify version pinning, long-term support commitments, and change-notification requirements more explicitly than commercial contracts require.

**Open-source exemption?**: The language refers to "commercial entity or adversary." Open-source models deployed on government infrastructure are not subject to commercial entity control — which may be part of why Adaptation explicitly includes open-source as a source for adaptation. A Llama-based model running on government compute has no vendor to prohibit anything.

---

## How NSPM-11 Changes the Anthropic-DoD Standoff

The Anthropic-DoD situation is still live. [Our full guide to the standoff](/builders-log/anthropic-dod-standoff-federal-freeze-thaw-builder-enterprise-guide/) covers the timeline in detail. The short version: Anthropic refused to waive autonomous-weapons guardrails, DoD banned Anthropic, a federal court issued a preliminary injunction, and as of June 8 the Pentagon is testing OpenAI, Gemini, and Grok as long-term replacements.

NSPM-11 introduces two new dynamics into that situation:

**The multi-vendor mandate creates policy-level pull for Anthropic's re-entry.** Under the 120-day procurement review, DoD must document how it's onboarding models from multiple vendors. If Anthropic remains locked out, the procurement review has to explain why the "most advanced" models (a category Anthropic plausibly qualifies for) are excluded. That documentation requirement creates pressure for resolution.

**The Assurance clause is exactly what Anthropic refused to sign.** The contract that triggered the February ban included language requiring Anthropic to remove safety guardrails around autonomous weapons and surveillance. NSPM-11's kill-switch prohibition formalizes the government's position that it requires unilateral-override-proof contracts. Unless Anthropic's position changes — or unless the government carves out safety-specific modifications as permissible — NSPM-11 systematizes the exact conflict that produced the standoff.

This is an unresolved tension. The policy creates simultaneous pressure to bring Anthropic back in (multi-vendor mandate) and to require contract terms Anthropic won't accept (Assurance clause). Watch for how the DoD's October 3 procurement update characterizes Anthropic's status. That document will be the clearest signal of where the standoff actually stands.

---

## The AI National Security Strategic Reserve

NSPM-11 establishes a new talent mechanism: the AI National Security Strategic Reserve. This is a pool of non-government AI experts — researchers, engineers, operators — who can be mobilized quickly for national security purposes.

The Reserve is modeled loosely on the FEMA-adjacent concept of on-call civilian expertise for surge capacity. Members of the Reserve maintain civilian careers but are available for temporary government assignments on AI-related national security missions.

**Builder relevance**: If you are an experienced AI engineer or researcher, the Reserve represents a formal channel for government AI collaboration without full-time employment. Early outreach from agencies establishing the Reserve is expected in the 90-day post-signing window.

---

## The Commercial Partnership Pillar

Within 120 days, the Secretary of War, the Secretary of Energy, the DNI, and the NSA Director shall develop partnerships with willing private-sector companies to "help secure America's most cutting-edge AI technologies."

This is different from the procurement mandate. The procurement mandate is about buying AI capabilities. The partnership mechanism is about sharing threat intelligence and collaborating on AI-specific security — protecting frontier model weights, securing training data supply chains, hardening inference infrastructure against adversarial attacks.

For labs developing frontier models: expect outreach from the AI Security Center (NSA) offering threat intelligence in exchange for early model access and collaboration on AI security standards. Participation is voluntary, but the value exchange is real.

---

## The Timeline

| Deadline | What Happens |
|----------|-------------|
| **June 5, 2026** | NSPM-11 signed; NSM-25 rescinded |
| **~August 4, 2026** | 60-day window: Secretary of War and DNI must assess current AI capabilities and gaps |
| **~September 3, 2026** | 90-day window: AI Security Center partnerships established; AI National Security Strategic Reserve framework published |
| **~October 3, 2026** | 120-day window: Procurement processes updated to onboard multiple AI vendors |
| **~November 3, 2026** | 150-day window: AI talent and hiring pipeline review complete |

The 120-day procurement deadline is the one to watch. That is when the operational change — multi-vendor DoD AI procurement — becomes formally documented.

---

## The Speed-vs-Caution Shift

The Small Wars Journal published an analysis on June 8 titled "Speed Over Caution: What NSPM-11 Means." The title captures the doctrine shift accurately.

Biden's NSM-25 was built around the premise that powerful AI in national security contexts required deliberate governance before deployment. NSPM-11 inverts this: deploy capable AI now, govern it within the deployment context, and accept that governance-first creates enough delay to cede operational advantage.

Neither posture is wrong in absolute terms. But understanding which posture governs the procurement environment your government customers operate in is essential for positioning AI products in that market.

Under NSPM-11, the procurement pitch that wins is: **fast to deploy, multi-vendor compatible, Assurance-clause compliant, with documented performance characteristics**. Responsible AI and governance-first messaging is less relevant to DoD evaluators than it was twelve months ago. Speed, compatibility, and contract compliance are now the primary signals.

---

## What Builders Working On or Near Government AI Should Do

**If you're targeting DoD procurement:** The 120-day window is your runway. The procurement update due October 3 will identify which capabilities are being onboarded and under what terms. Position now, before the review concludes. Understand the Assurance clause requirements and what they mean for your contract language.

**If you're building on Claude for government-adjacent applications:** Watch the Anthropic-DoD standoff update expected in conjunction with the October procurement review. Anthropic's status in classified environments directly affects what IL5/IL6 deployments you can build on Claude.

**If you're evaluating open-source models for government use:** The Adaptation pillar's explicit inclusion of open-source, combined with the kill-switch prohibition, makes open-weight models structurally attractive for classified deployments. Llama, Mistral, and similar models on government compute avoid the Assurance clause tension entirely.

**If you're an AI engineer:** Watch for Reserve outreach in the next 90 days. Government AI talent programs have historically created meaningful consulting and advisory opportunities for people with frontier AI expertise.

---

## Catch Up

- [Trump's June 2 AI Executive Order: The Civilian Side](/builders-log/trump-ai-executive-order-june-2026-signed-frontier-model-voluntary-review-builder-guide/) — voluntary frontier model review, AI cybersecurity clearinghouse, what's mandatory vs. voluntary
- [The Anthropic-DoD Standoff](/builders-log/anthropic-dod-standoff-federal-freeze-thaw-builder-enterprise-guide/) — full timeline from the February ban through the June 8 update

