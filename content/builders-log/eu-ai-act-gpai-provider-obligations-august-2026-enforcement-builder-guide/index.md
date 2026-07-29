---
title: "EU AI Act GPAI Provider Obligations: August 2, 2026 Enforcement Deadline Builder Guide"
date: 2026-06-06
description: "GPAI provider obligations under the EU AI Act are NOT delayed. August 2, 2026 is when the Commission's enforcement powers activate. Documentation, training data summaries, EU SEND submissions, systemic risk notification — here's what builders need to do and who is actually on the hook."
og_description: "EU AI Act GPAI enforcement activates August 2, 2026. High-risk AI deadlines were extended — GPAI was not. Technical documentation, training data summaries, EU SEND platform submissions, systemic risk adversarial testing (≥10^25 FLOPs). Fines up to €15M or 3% global revenue. Builder compliance checklist inside."
content_type: "Builder's Log"
categories: ["AI Policy", "Enterprise AI", "Industry Analysis"]
tags: ["eu-ai-act", "gpai", "compliance", "regulation", "foundation-model", "enterprise", "august-2026", "eu-send", "systemic-risk", "builder-guide", "policy"]
sources_audited: 2026-07-29
---

The most-cited fact about the EU AI Act's Digital Omnibus amendments is that high-risk AI compliance deadlines were extended 12–16 months. That is true. What is less prominently stated: **GPAI model obligations were explicitly carved out of the extensions.** They are in force now and [enforcement activates August 2, 2026](https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/).

If you are building, fine-tuning, or distributing a general-purpose AI model — or building on top of one and are wondering whether your stack makes you a "provider" — this is your August 2 checklist.

---

## What Happens on August 2, 2026

The [EU AI Act's GPAI provisions](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) (Chapter V, Articles 51–56) entered into application on **August 2, 2025**, one year after [the Regulation entered into force](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) on August 1, 2024. That first year was a compliance ramp: the substantive obligations applied, but [Article 101 — the Commission's power to fine GPAI providers — was explicitly carved out of the August 2025 application date and only takes effect on the Regulation's general August 2, 2026 application date](https://artificialintelligenceact.eu/article/113/).

On **August 2, 2026**, the European Commission's enforcement powers over GPAI providers fully activate:

- The [**AI Office**](https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/) (established within the Commission) can investigate GPAI providers, demand documentation, and impose fines
- Fines for GPAI providers under [**Article 101**](https://artificialintelligenceact.eu/article/101/): **up to €15 million or 3% of total worldwide annual turnover**, whichever is higher — this single ceiling covers both non-compliance with a documentation request and supplying incorrect, incomplete, or misleading information; there is no separate lower fine tier for GPAI providers specifically

The [Digital Omnibus deal](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) extended deadlines for Annex III high-risk AI applications (employment screening, credit scoring, education access — standalone products) to **December 2, 2027**, and high-risk AI embedded in regulated products (medical devices, machinery, vehicles) to **August 2, 2028**. **GPAI obligations (Articles 51–56) were left out of the extension package** and remain on the original schedule.

---

## Who Is a GPAI Provider

A [**general-purpose AI model**](https://artificialintelligenceact.eu/article/3/) is defined in [Article 3(63) of the AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) as a model trained with a large amount of data using self-supervision at scale, that displays significant generality and can competently perform a wide range of distinct tasks, and that can be integrated into a variety of downstream systems or applications. In practice: any foundation model — large language model, multimodal model, code model — accessible via API or direct download to EU users qualifies.

A [**GPAI provider**](https://artificialintelligenceact.eu/article/3/) is anyone who develops a GPAI model or has one developed and **places it on the EU market under its own name**, per the Article 3(3) provider definition. This includes:

- Companies offering GPAI APIs to EU customers, even from outside the EU — [Article 2 gives the Act extraterritorial reach where a third-country provider's AI system output is used in the Union](https://artificialintelligenceact.eu/article/2/)
- Open-weight model publishers whose models are actively downloaded in the EU
- Companies that fine-tune or substantially modify an existing GPAI model and release the modified version

**Downstream API integrators** — builders using Claude, GPT, Gemini, or other GPAI models via API to build products — are **not** GPAI providers under the Act. Provider liability sits with whoever placed the model on the market; a party that merely uses an AI system under its own authority is instead a [**deployer** under Article 3(4)](https://artificialintelligenceact.eu/article/3/). If you call the Anthropic API to build a customer support bot, you are a deployer, not a GPAI provider.

The exception that matters for builders: **substantial modification**. Under [Article 25](https://artificialintelligenceact.eu/modifying-ai-under-the-eu-ai-act/), if a downstream developer meaningfully changes a model's weights, architecture, or intended-use boundaries and makes the modified model available to others, they may become the provider of the modified GPAI model — inheriting obligations for the modification itself, not the whole model. The [Commission's July 18, 2025 guidelines on GPAI obligations](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers) give an indicative rule of thumb: if the compute used for the modification exceeds roughly one-third of the original model's training compute, the modifier is generally treated as the provider of the resulting model.

---

## What All GPAI Providers Must Do

These obligations apply to all GPAI models with meaningful EU market presence, regardless of training compute or capability threshold:

### 1. Technical Documentation

Maintain up-to-date technical documentation covering:

- **Model architecture**: layers, parameters, training approach
- **Training data**: categories of training data, sources, data governance practices, whether copyrighted material was included and under what legal basis
- **Evaluation results**: benchmark performance, known limitations, failure modes
- **Intended purpose**: what the model was trained for, intended deployment contexts
- **Known harmful uses**: documented misuse patterns and any implemented safeguards
- **Contact information**: a point of contact for the AI Office to reach the provider

The documentation standard is specified in [Annex XI, referenced by Article 53(1)(a) of the AI Act](https://artificialintelligenceact.eu/annex/11/), and includes architecture, training methodology, data sources, computational resources used, and known or estimated energy consumption. The Commission has published a documentation template as part of its [GPAI guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers); using it is not mandatory but is offered as a recommended format.

### 2. EU Copyright Compliance Policy

Under [Article 53(1)(c)](https://artificialintelligenceact.eu/article/53/), GPAI providers must implement a policy on compliance with EU copyright law, including [Directive (EU) 2019/790](https://eur-lex.europa.eu/eli/dir/2019/790/oj/eng) (the Copyright in the Digital Single Market Directive). In practice this means:

- A published statement that the provider has complied with the text-and-data mining provisions
- Opt-out mechanisms for rights holders (if training on web data)
- Documentation of which data categories were used and under what legal basis

The Act does not require that all training data be licensed — it requires that providers have a policy and implement it. For GPAI models placed on the market before August 2, 2025, [providers have until August 2, 2027 to bring documentation into compliance](https://artificialintelligenceact.eu/article/113/); models placed on the market on or after August 2, 2025 must comply immediately.

### 3. Training Data Summary Publication

Under [Article 53(1)(d)](https://artificialintelligenceact.eu/article/53/), publish a summary of the training data used in the model, using the [template published by the AI Office](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers). This is distinct from the full technical documentation — it is a publicly accessible document that rights holders, researchers, and downstream deployers can consult. The summary must cover data categories, approximate data volumes by category, and data collection methods.

### 4. EU SEND Platform Submission

Submit the required documentation and notifications to the **EU SEND** platform operated by the AI Office. This is how the Commission [tracks which GPAI models, particularly systemic-risk models, are on the EU market](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers) and receives serious-incident reports and Safety and Security Framework/Model Report submissions.

SEND has been operating since GPAI obligations took effect on August 2, 2025. August 2, 2026 does not change SEND's availability — it changes whether the AI Office can fine a provider found not to have submitted.

---

## What Systemic-Risk GPAI Providers Must Additionally Do

Under [Article 51](https://artificialintelligenceact.eu/article/51/), a GPAI model is presumed to have systemic risk if it was trained using more than **10^25 FLOPs** of compute, or if the AI Office designates it as systemic risk based on capability evaluation against the criteria in [Annex XIII](https://artificialintelligenceact.eu/annex/13/) (reach, integration into critical infrastructure, etc.).

In practice, this threshold is understood to cover the most capable frontier models from major labs, though providers do not routinely disclose exact training-compute figures, so which specific current model releases cross it is not something this piece can confirm. Most fine-tunes and smaller models do not cross this threshold unless designated.

Systemic-risk providers must additionally:

### 5. Adversarial Testing (Red-Teaming)

Under [Article 55](https://artificialintelligenceact.eu/article/55/), conduct, document, and report on model evaluation, including adversarial testing:

- Test for dangerous capabilities: CBRN assistance, cyberweapons generation, large-scale manipulation
- Test for systemic risks: cascading failures across interconnected deployments, critical infrastructure vulnerabilities
- Testing must be proportionate to the risk and reflect the state of the art; the Act does not set a fixed testing cadence
- Testing may involve independent external experts

### 6. Serious Incident Reporting

Under [Article 55(1)(c)](https://artificialintelligenceact.eu/article/55/), keep track of, document, and report **serious incidents** to the AI Office **without undue delay**:

- A serious incident is defined (Article 3) as a malfunction or misuse of the model that results in, or is reasonably likely to result in, death, serious injury, significant disruption to critical infrastructure, property damage, or violation of fundamental rights
- Reporting is to the AI Office, which coordinates with national competent authorities
- The Act itself does not set fixed day-counts for GPAI systemic-risk reports (that specific 2/10/15-day tiering is what [Article 73](https://artificialintelligenceact.eu/article/73/) sets for high-risk AI *system* providers, a related but separate obligation); the [GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) operationalizes the Article 55 "without undue delay" standard with a severity-based reporting template
- Providers must maintain an incident log accessible to the AI Office on request

### 7. Cybersecurity Measures

Under [Article 55(1)(d)](https://artificialintelligenceact.eu/article/55/), implement and document model-level cybersecurity measures:

- Adversarial robustness testing (prompt injection, data poisoning, model extraction resistance)
- Access controls for model weights and fine-tuning infrastructure
- Documentation of security measures submitted to the AI Office

### 8. Energy Efficiency Reporting

As part of the [Annex XI technical documentation](https://artificialintelligenceact.eu/annex/11/), report and publish energy consumption data:

- Training energy consumption (known or estimated, based on computational resources used where the exact figure is unknown)
- Inference energy per token or per request (estimated or measured)
- The Commission has run a [targeted consultation on standardizing energy-consumption measurement](https://digital-strategy.ec.europa.eu/en/consultations/targeted-consultation-measuring-energy-consumption-and-emissions-ai-models-and-systems) — the initial requirement is to report, not to meet a specific threshold

---

## The Code of Practice

The [**GPAI Code of Practice**](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) is a voluntary compliance framework developed jointly by AI providers, civil society organizations, and the AI Office, and was [published in final form on July 10, 2025](https://www.wsgr.com/en/insights/eu-releases-final-code-of-practice-for-general-purpose-ai-models.html) — ahead of the August 2, 2025 date GPAI obligations took effect. It is not legally required, but:

- Under [Article 56](https://artificialintelligenceact.eu/article/56/), providers may rely on the Code to demonstrate compliance with Articles 53 and 55 obligations until harmonised standards are published
- Providers who are not signatories must demonstrate compliance through other means
- An EU spokesperson said companies that decline to sign "may be exposed to more regulatory scrutiny by the AI Office," though the mandatory AI Act obligations apply regardless of signature ([The Register, July 18, 2025](https://www.theregister.com/2025/07/18/meta_declines_eu_ai_guidelines/))

[Anthropic, Google, OpenAI, Mistral, and Cohere are among the Code's signatories](https://artificialintelligenceact.eu/introduction-to-code-of-practice/). **Meta is a notable exception: it publicly declined to sign**, with its chief global affairs officer stating the Code "introduces a number of legal uncertainties for model developers, as well as measures which go far beyond the scope of the AI Act" ([The Register, July 18, 2025](https://www.theregister.com/2025/07/18/meta_declines_eu_ai_guidelines/)). Declining to sign the Code does not exempt Meta from the AI Act's binding GPAI obligations themselves — it only means Meta must show compliance without the Code's presumption-of-conformity shortcut.

If you are a GPAI provider who has not yet engaged with the Code, the time to sign and begin aligning documentation practices is now, not in September.

---

## What API-First Builders Actually Need to Know

If you build on GPAI models via API (Anthropic, OpenAI, Google, etc.) and do not modify or redistribute model weights, your GPAI compliance exposure is minimal. The Act is explicit that deployers who use GPAI via API are not providers.

Three scenarios where this changes:

**Scenario 1: You fine-tune and re-distribute.** If you fine-tune a foundation model and offer the fine-tuned model to others (via API, download, or enterprise contract), you may become a GPAI provider of the modified model. The threshold is not bright-line: the [Commission's guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers) use the roughly-one-third-of-original-training-compute rule of thumb described above, and whether a narrow, in-house-only fine-tune (domain adaptation, tone adjustment) crosses it remains a grey area that [legal commentators are still tracking](https://www.softwareseni.com/fine-tuning-foundation-models-under-the-eu-ai-act-when-customisation-triggers-provider-obligations/). If you are licensing the fine-tune to third parties, you are more clearly in provider territory.

**Scenario 2: You aggregate and serve.** If you operate an LLM routing layer that serves EU customers — calling multiple GPAI models on their behalf — you are almost certainly a deployer, not a provider. You do not place models on the market; you access them. Your obligation is to verify that the models you route through are compliant GPAI providers.

**Scenario 3: You build an AI product that can be used as a component.** If your AI product can itself be used as an AI component by downstream developers — i.e., if your product's AI capabilities are accessible via API to other builders — you may have a GPAI provider analysis to do. This depends on whether your output system constitutes a "general-purpose AI model" or a purpose-specific application. An application that happens to have an API does not automatically become a GPAI model; a general-purpose AI assistant that third parties embed into their products may.

---

## Action Checklist: Before August 2, 2026

**All GPAI providers:**

- [ ] Complete Annex XI technical documentation for all models with EU market presence
- [ ] Publish training data summary (publicly accessible URL)
- [ ] Document and publish EU copyright compliance policy
- [ ] Submit documentation to EU SEND platform
- [ ] Review Code of Practice and consider signing (strongly recommended)
- [ ] Assign a point of contact for AI Office inquiries

**Systemic-risk GPAI providers (≥10^25 FLOPs or AI Office designation):**

- [ ] Complete adversarial testing (third-party or AI Office validation)
- [ ] Submit testing results to AI Office
- [ ] Establish a serious-incident reporting process meeting the Article 55 "without undue delay" standard, per the GPAI Code of Practice's severity-based reporting template
- [ ] Document cybersecurity measures for model weights and inference infrastructure
- [ ] Report training energy consumption data
- [ ] Begin inference energy measurement or estimation

**API-first builders using GPAI:**

- [ ] Confirm that your primary GPAI providers (Anthropic, OpenAI, Google, etc.) are compliant under the Act — check their published transparency documentation
- [ ] Assess whether any fine-tuning or model redistribution in your stack creates provider exposure
- [ ] If you build developer-facing AI components: perform the provider vs. deployer analysis above
- [ ] Update any EU enterprise customer agreements to reflect that your AI stack sits on compliant GPAI providers

---

## One Horizon Past August 2

The August 2, 2026 activation is the enforcement start, not the end of GPAI compliance work.

During the 2025–2026 compliance-ramp year, the [AI Office described its own posture as collaborative](https://ai-act-service-desk.ec.europa.eu/en/faq?amp=&combine=&faq_category_id=69) — it treats "technical compliance dialogues" with providers as its first tool of choice, reserving fines for cases where those dialogues aren't sufficient. Whether that same relatively light touch continues after August 2, 2026, and for which providers, is not something this piece can predict. But the documentation requirements are ongoing, and the audit clock starts ticking on August 2. Non-compliance discovered in a later audit will be measured against obligations that began in August 2025.

High-risk AI applications built on GPAI models have their own [compliance calendar](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) (December 2, 2027 for standalone, August 2, 2028 for embedded). If your product uses a GPAI model as a component in a high-risk use case — credit scoring, hiring automation, access to essential services — start the Annex III analysis now, even though enforcement is further out. The documentation requirements for Annex III draw heavily on the GPAI technical documentation already required. Building one GPAI documentation package now reduces duplicated work later.

The EU AI Act is the first comprehensive AI regulation with enforcement teeth. August 2, 2026 is when those teeth engage.
