# NSPM-11: Trump's Military AI Directive Mandates Multi-Vendor Adoption and Bans Vendor Kill Switches — What It Means for Builders

> Signed June 5, NSPM-11 directs the DoD and intelligence community to accelerate AI adoption, mandate multiple vendors, and contractually prohibit commercial providers from disabling deployed systems. Here's what it changes for builders working on or near government AI.


**At a glance:** President Trump signed [NSPM-11 (National Security Presidential Memorandum 11)](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/) on June 5, 2026, directing the U.S. military and intelligence community to accelerate AI adoption. The memorandum [replaces the Biden administration's NSM-25](https://www.governmentcontractslegalforum.com/2026/06/articles/government-contracts/national-security-memorandum-aims-to-accelerate-deployment-of-ai-and-streamline-procurement-aligned-to-administration-policies/), establishes four pillars (Adoption, Adaptation, Assurance, Accountability), mandates multi-vendor procurement, and requires contractual clauses prohibiting commercial AI providers from disabling or modifying deployed systems without federal approval. Part of our **[Builder's Log](/builders-log/)**.

This is the companion piece to our [June 2 EO guide](/builders-log/trump-ai-executive-order-june-2026-signed-frontier-model-voluntary-review-builder-guide/). The EO covered civilian agencies, voluntary frontier model review, and the AI cybersecurity clearinghouse. NSPM-11 is the other half: it governs the DoD, the intelligence community, and the classified environments where the different rules apply.

---

## What NSPM-11 Actually Does

[NSPM-11](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/) organizes national security AI policy around four pillars, which it calls **Adoption, Adaptation, Assurance, and Accountability**.

**Adoption** is the first pillar — and its placement is intentional. The posture is speed over caution. The memorandum directs agencies to eliminate "unnecessary barriers to rapid deployment" and to maintain "deep, proactive partnerships with industry to make the most advanced frontier models broadly available to national security professionals without delay" ([NSPM-11 text](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/)).

The phrase "without delay" does real work here. NSM-25, the Biden-era document this replaces, set up multi-layered governance review as the precondition for DoD AI deployment. NSPM-11 [explicitly rescinds and replaces NSM-25](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/), inverting the default: deploy first, govern within the deployment, not before it.

**Adaptation** directs the national security enterprise to leverage "commercial or open-source AI technologies" from "diverse suppliers across the private sector, large and small." The language is deliberately broad and does not name specific vendors in the text; it covers hyperscale labs (Anthropic, OpenAI, Google DeepMind) and smaller vendors, and it also explicitly includes open-source.

**Assurance** is where the vendor-facing requirements live. More on this below.

**Accountability**, as written, is not a chain-of-command provision — it is a use-restriction clause. The memorandum states that AI technologies "shall neither be developed nor used by the national security enterprise to censor free speech, embed ideological bias, or conduct unauthorized or unlawful surveillance activities" ([NSPM-11 text](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/); confirmed independently by [Crowell & Moring's client alert](https://www.crowell.com/en/insights/client-alerts/national-security-memorandum-aims-to-accelerate-deployment-of-ai-and-streamline-procurement-aligned-to-administration-policies)). It is a bias/surveillance guardrail on how AI may be used, not a statement about commander accountability for operational performance.

---

## The Multi-Vendor Mandate: 120 Days

Within 120 days of June 5 — by approximately **October 3, 2026** — the Secretary of War, the DNI, and the heads of agencies with Intelligence Community elements must review and update procurement processes to ensure "rapid onboarding of the most advanced AI models from multiple vendors" ([NSPM-11 text](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/)).

This is a direct repudiation of single-vendor lock-in. By May 2026, the Pentagon had already signed classified-network AI contracts with eight companies — SpaceX, OpenAI, Google, NVIDIA, Microsoft, AWS, Reflection AI, and Oracle — explicitly excluding Anthropic, which [Defense Secretary Pete Hegseth designated a "supply-chain risk" in late February](https://www.cnbc.com/2026/03/09/anthropic-was-the-pentagons-choice-for-ai-now-its-banned-and-experts-are-worried.html) after the company refused to remove restrictions on autonomous-weapons and domestic-surveillance use of Claude. A Pentagon CTO described the resulting approach as a deliberately "redundant, multi-vendor architecture" built to avoid "vendor lock" ([Let's Data Science](https://letsdatascience.com/blog/pentagon-signs-eight-ai-companies-anthropic-excluded)) — no single vendor holds a "primary" classified position. That existing multi-vendor build-out, and Anthropic's continued exclusion from it, is what this NSPM-11 provision formalizes and extends.

What "multiple vendors" means in practice:

**For frontier labs:** Anthropic, Google DeepMind, xAI, and others are now explicitly targeted as onboarding candidates, not optional additions. The procurement update is a directive, not a suggestion. Labs that have been locked out of classified environments (like Anthropic, due to the ongoing standoff) have a policy-level mandate behind re-entry requests — assuming the underlying standoff with DoD resolves.

**For mid-scale and open-source labs:** The language covers "diverse suppliers...large and small." Mistral, Cohere, and similar vendors with government-adjacent products have a procurement window opening. The 120-day review is the signal to engage now.

**For builders on GovCloud:** If your application runs on a single underlying model in a government context, the procurement environment now pushes toward multi-model architectures. Building model-agnostic abstraction layers is not just good engineering — it aligns with the procurement direction your government customers are being directed toward.

---

## The Kill-Switch Prohibition: What It Means for Enterprise AI Contracts

The Assurance pillar contains the most significant contract-level change for commercial AI providers:

> AI systems adopted shall be designed to be reliable, robust, steerable, and controllable, with **contractual clauses ensuring no commercial entity or adversary can prevent use of, disable or degrade, or materially modify AI systems without Federal Government knowledge and approval** ([NSPM-11 text](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/); quoted consistently in [Crowell & Moring's analysis](https://www.crowell.com/en/insights/client-alerts/national-security-memorandum-aims-to-accelerate-deployment-of-ai-and-streamline-procurement-aligned-to-administration-policies)).

This is a kill-switch prohibition. Any AI provider selling to the DoD or IC must contractually commit that they cannot unilaterally:

- Disable the deployed system
- Degrade its capabilities
- Materially modify its behavior

...without the federal government's knowledge and explicit approval.

The tension here is significant. AI providers maintain emergency shutdown capabilities for exactly the kinds of systems the government wants to deploy. Anthropic's conflict with DoD — [Claude was designated a "supply-chain risk" and barred from classified networks in late February 2026](https://www.mayerbrown.com/en/insights/publications/2026/03/pentagon-designates-anthropic-a-supply-chain-risk-what-government-contractors-need-to-know) — centered precisely on guardrails Anthropic would not contractually waive: the company [refused Pentagon demands to permit fully autonomous weapons targeting and domestic mass surveillance uses of Claude](https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2026/february/Anthropic-Refusal/), per Congressional Research Service reporting on the dispute ([CRS IN12669](https://www.congress.gov/crs-product/IN12669)). The Assurance pillar, as written, requires providers to relinquish unilateral control over those guardrails.

For builders deploying commercial AI in government contexts, this creates a three-way tension:

**Lab safety policy vs. contract terms**: Providers like Anthropic have hard limits they will not waive — autonomous weapons targeting, domestic mass surveillance. NSPM-11's Assurance clause requires contractual commitments that potentially conflict with those limits. The resolution is not obvious.

**Deprecation timelines**: Even ordinary model deprecation — retiring Claude 3.5 in favor of Claude 4, for example — could qualify as "materially modifying" a deployed system. Government contracts will need to specify version pinning, long-term support commitments, and change-notification requirements more explicitly than commercial contracts require.

**Open-source exemption?**: The language refers to "commercial entity or adversary." Open-source models deployed on government infrastructure are not subject to commercial entity control — which may be part of why Adaptation explicitly includes open-source as a source for adaptation. A Llama-based model running on government compute has no vendor to prohibit anything.

---

## How NSPM-11 Changes the Anthropic-DoD Standoff

The Anthropic-DoD situation is still live. [Our full guide to the standoff](/builders-log/anthropic-dod-standoff-federal-freeze-thaw-builder-enterprise-guide/) covers the timeline in detail. The short version: Anthropic refused to waive autonomous-weapons and mass-surveillance guardrails, DoD designated Anthropic a supply-chain risk in late February, [a federal judge granted Anthropic a preliminary injunction in late March, citing "classic illegal First Amendment retaliation,"](https://www.cnbc.com/2026/03/26/anthropic-pentagon-dod-claude-court-ruling.html) though [the Pentagon has continued to treat the ban as standing](https://www.cnbc.com/2026/04/08/anthropic-pentagon-court-ruling-supply-chain-risk.html) and Anthropic's appeal is ongoing. As of June 8, [the Pentagon is running head-to-head tests of OpenAI, Google, and xAI's Grok models](https://www.techtimes.com/articles/317998/20260608/pentagon-racing-replace-anthropics-claude-because-it-was-too-safe-war.htm) as potential long-term replacements for Claude in classified workflows.

NSPM-11 introduces two new dynamics into that situation:

**The multi-vendor mandate creates policy-level pull for Anthropic's re-entry.** Under the 120-day procurement review, DoD must document how it's onboarding models from multiple vendors. If Anthropic remains locked out, the procurement review has to explain why the "most advanced" models (a category Anthropic plausibly qualifies for) are excluded. That documentation requirement creates pressure for resolution.

**The Assurance clause is exactly what Anthropic refused to sign.** The dispute that triggered the February ban centered on a Pentagon demand that Anthropic strip out its restrictions on autonomous-weapons targeting and domestic mass surveillance ([CRS IN12669](https://www.congress.gov/crs-product/IN12669); [ASIS International](https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2026/february/Anthropic-Refusal/)). NSPM-11's kill-switch prohibition formalizes the government's position that it requires unilateral-override-proof contracts. Unless Anthropic's position changes — or unless the government carves out safety-specific modifications as permissible — NSPM-11 systematizes the exact conflict that produced the standoff.

This is an unresolved tension. The policy creates simultaneous pressure to bring Anthropic back in (multi-vendor mandate) and to require contract terms Anthropic won't accept (Assurance clause). Watch for how the DoD's October 3 procurement update characterizes Anthropic's status. That document will be the clearest signal of where the standoff actually stands.

---

## The AI National Security Strategic Reserve

NSPM-11 directs agencies to initiate, within 120 days of signing, an "AI National Security Strategic Reserve of non-governmental AI talent to provide support to Federal efforts" ([NSPM-11 text](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/)). This is a pool of non-government AI experts — researchers, engineers, operators — who can be mobilized for national security purposes.

The memorandum's own language is sparse on structure; the FEMA-style "on-call civilian expertise for surge capacity" framing below is our characterization of how such a reserve would likely function, not text drawn from the document itself. Treat it as informed inference, not a confirmed program design.

**Builder relevance**: If you are an experienced AI engineer or researcher, the Reserve represents a potential formal channel for government AI collaboration without full-time employment. Since the memorandum's own deadline for standing this up is 120 days (by approximately October 3, 2026), expect any agency outreach to land in that window, not sooner.

---

## The Commercial Partnership Pillar

Within 120 days, the Secretary of War, the Secretary of Energy, the DNI, and the NSA Director shall develop partnerships with willing private-sector companies to "help secure America's most cutting-edge AI technologies," administered through the AI Security Center ([NSPM-11 text](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/)).

This is different from the procurement mandate. The procurement mandate is about buying AI capabilities. The partnership mechanism is about sharing threat intelligence and collaborating on AI-specific security — protecting frontier model weights, securing training data supply chains, hardening inference infrastructure against adversarial attacks.

For labs developing frontier models: expect outreach from the AI Security Center (NSA) offering threat intelligence in exchange for early model access and collaboration on AI security standards. Participation is voluntary, but the value exchange is real.

---

## The Timeline

| Deadline | What Happens |
|----------|-------------|
| **June 5, 2026** | NSPM-11 signed; NSM-25 rescinded |
| **~September 3, 2026** | 90-day window: DoD Directive 3000.09 (autonomy in weapon systems) updated; national-security AI governance policy and classified annex issued |
| **~October 3, 2026** | 120-day window: procurement processes updated to onboard multiple AI vendors; AI Security Center private-sector partnerships and AI National Security Strategic Reserve initiated; AI curriculum, risk-management strategy, and test/evaluation methodologies due |

The memorandum's text contains only 90-day and 120-day deadlines — no 60-day or 150-day milestone appears anywhere in it ([NSPM-11 full text](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/)). The 120-day mark is the one to watch: it is when procurement, the AI Security Center partnerships, and the Strategic Reserve all come due at once.

---

## The Speed-vs-Caution Shift

The Small Wars Journal published [an analysis on June 8 titled "Speed Over Caution: What NSPM-11 Means"](https://smallwarsjournal.com/2026/06/08/speed-over-caution-what-nspm-11-means/). The title captures the doctrine shift accurately.

Biden's NSM-25 was built around the premise that powerful AI in national security contexts required deliberate governance before deployment. NSPM-11 inverts this: deploy capable AI now, govern it within the deployment context, and accept that governance-first creates enough delay to cede operational advantage.

Neither posture is wrong in absolute terms. But understanding which posture governs the procurement environment your government customers operate in is essential for positioning AI products in that market.

Under NSPM-11, the procurement pitch that wins is: **fast to deploy, multi-vendor compatible, Assurance-clause compliant, with documented performance characteristics**. Responsible AI and governance-first messaging is less relevant to DoD evaluators than it was twelve months ago. Speed, compatibility, and contract compliance are now the primary signals.

---

## What Builders Working On or Near Government AI Should Do

**If you're targeting DoD procurement:** The 120-day window is your runway. The procurement update due October 3 will identify which capabilities are being onboarded and under what terms. Position now, before the review concludes. Understand the Assurance clause requirements and what they mean for your contract language.

**If you're building on Claude for government-adjacent applications:** Watch the Anthropic-DoD standoff update expected in conjunction with the October procurement review. Anthropic's status in classified environments directly affects what IL5/IL6 deployments you can build on Claude.

**If you're evaluating open-source models for government use:** The Adaptation pillar's explicit inclusion of open-source, combined with the kill-switch prohibition, makes open-weight models structurally attractive for classified deployments. Llama, Mistral, and similar models on government compute avoid the Assurance clause tension entirely.

**If you're an AI engineer:** Watch for Reserve outreach around the 120-day mark (~October 3, 2026), the memorandum's own deadline for standing it up. Government AI talent programs have historically created meaningful consulting and advisory opportunities for people with frontier AI expertise.

---

## Catch Up

- [Trump's June 2 AI Executive Order: The Civilian Side](/builders-log/trump-ai-executive-order-june-2026-signed-frontier-model-voluntary-review-builder-guide/) — voluntary frontier model review, AI cybersecurity clearinghouse, what's mandatory vs. voluntary
- [The Anthropic-DoD Standoff](/builders-log/anthropic-dod-standoff-federal-freeze-thaw-builder-enterprise-guide/) — full timeline from the February ban through the June 8 update

