# EU AI Act GPAI Provider Obligations: August 2, 2026 Enforcement Deadline Builder Guide

> GPAI provider obligations under the EU AI Act are NOT delayed. August 2, 2026 is when the Commission's enforcement powers activate. Documentation, training data summaries, EU SEND submissions, systemic risk notification — here's what builders need to do and who is actually on the hook.


The most-cited fact about the EU AI Act's Digital Omnibus amendments is that high-risk AI compliance deadlines were extended 12–16 months. That is true. What is less prominently stated: **GPAI model obligations were explicitly carved out of the extensions.** They are in force now and enforcement activates August 2, 2026.

If you are building, fine-tuning, or distributing a general-purpose AI model — or building on top of one and are wondering whether your stack makes you a "provider" — this is your August 2 checklist.

---

## What Happens on August 2, 2026

The EU AI Act's GPAI provisions (Chapter V, Articles 51–56) entered into force on **August 2, 2025** — one year after the Act was published. That first year was a compliance ramp: obligations were in place, enforcement wasn't.

On **August 2, 2026**, the European Commission's enforcement powers over GPAI providers fully activate:

- The **AI Office** (established within the Commission) can investigate GPAI providers, demand documentation, and impose fines
- Fines for GPAI-related violations: **up to €15 million or 3% of total worldwide annual turnover**, whichever is higher
- For providing false, incomplete, or misleading information: up to €7.5 million or 1% of worldwide annual turnover

The Digital Omnibus deal extended deadlines for Annex III high-risk AI applications (employment screening, credit scoring, education access — standalone products) until December 2027 and embedded AI until August 2028. **GPAI was untouched.** This was deliberate: the Parliament insisted on keeping GPAI obligations on schedule, and the Council agreed.

---

## Who Is a GPAI Provider

A **general-purpose AI model** is defined in the AI Act as a model trained on large amounts of data using self-supervision at scale, that can perform a wide range of tasks, and that can be integrated into downstream systems. In practice: any foundation model — large language model, multimodal model, code model — accessible via API or direct download to EU users qualifies.

A **GPAI provider** is anyone who **places a GPAI model on the EU market**. This includes:

- Companies offering GPAI APIs to EU customers (even from outside the EU — the Act's geographic scope follows where the model's outputs are used)
- Open-weight model publishers whose models are actively downloaded in the EU
- Companies that fine-tune or substantially modify an existing GPAI model and release the modified version

**Downstream API integrators** — builders using Claude, GPT, Gemini, or other GPAI models via API to build products — are **not** GPAI providers under the Act. Provider liability sits with whoever placed the model on the market. If you call the Anthropic API to build a customer support bot, you are a deployer, not a GPAI provider.

The exception that matters for builders: **substantial modification**. If a downstream developer meaningfully changes a model's weights, architecture, or intended-use boundaries and makes the modified model available to others, they may become the provider of the modified GPAI model. The AI Office has not yet published formal guidance on what counts as "substantial" — the Code of Practice process will likely address this.

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

The documentation standard is specified in Annex XI of the AI Act. The AI Office published a template; it is not required but serves as a safe harbor for format.

### 2. EU Copyright Compliance Policy

GPAI providers must implement a policy on compliance with EU copyright law, including Directive 2019/790 (the Copyright in the Digital Single Market Directive). In practice this means:

- A published statement that the provider has complied with the text-and-data mining provisions
- Opt-out mechanisms for rights holders (if training on web data)
- Documentation of which data categories were used and under what legal basis

The Act does not require that all training data be licensed — it requires that providers have a policy and implement it. For open-weight models trained before the August 2025 GPAI effective date, the AI Office has indicated it will evaluate good-faith compliance efforts rather than retroactive perfection.

### 3. Training Data Summary Publication

Publish a summary of the training data used in the model. This is distinct from the full technical documentation — it is a publicly accessible document that rights holders, researchers, and downstream deployers can consult. The summary must cover data categories, approximate data volumes by category, and data collection methods.

### 4. EU SEND Platform Submission

Submit the technical documentation to the **EU SEND** (Single Electronic Notification and Documentation) platform operated by the AI Office. This is how the Commission tracks which GPAI models are on the EU market.

The SEND platform went live in Q1 2026. Providers who placed models on the EU market before that date had a grace period to submit. As of June 2026, new model placements require submission before or concurrent with EU market access.

---

## What Systemic-Risk GPAI Providers Must Additionally Do

A GPAI model is classified as **systemic risk** if it was trained using more than **10^25 FLOPs** of compute, or if the AI Office designates it as systemic risk based on capability evaluation (reach, integration into critical infrastructure, etc.).

In practice, this threshold covers GPT-4-class and above models, the current Anthropic Claude 4.x series, Gemini 3.x series, and the most capable open-weight releases. Most fine-tunes and smaller models do not cross this threshold unless designated.

Systemic-risk providers must additionally:

### 5. Adversarial Testing (Red-Teaming)

Conduct, document, and submit results of adversarial testing:

- Test for dangerous capabilities: CBRN assistance, cyberweapons generation, large-scale manipulation
- Test for systemic risks: cascading failures across interconnected deployments, critical infrastructure vulnerabilities
- Testing must occur before EU market placement and periodically thereafter (the Code of Practice specifies annual cycles)
- Testing must be performed or validated by a qualified third party or by the AI Office itself

### 6. Serious Incident Reporting

Report **serious incidents** to the AI Office without undue delay:

- A serious incident is defined as a malfunction or misuse of the model that results in (or is reasonably likely to result in) death, serious injury, significant disruption to critical infrastructure, property damage, or violation of fundamental rights
- Reporting is to the AI Office, which coordinates with national competent authorities
- The initial report must be made within 15 days of becoming aware; a full report within 30 days
- Providers must maintain an incident log accessible to the AI Office on request

### 7. Cybersecurity Measures

Implement and document model-level cybersecurity measures:

- Adversarial robustness testing (prompt injection, data poisoning, model extraction resistance)
- Access controls for model weights and fine-tuning infrastructure
- Documentation of security measures submitted to the AI Office

### 8. Energy Efficiency Reporting

Report and publish energy consumption data:

- Training energy consumption (kWh, location of compute)
- Inference energy per token or per request (estimated or measured)
- The AI Office is developing standardized reporting templates — the initial requirement is to report, not to meet a specific threshold

---

## The Code of Practice

The **GPAI Code of Practice** is a voluntary compliance framework developed jointly by AI providers, civil society organizations, and the AI Office through 2025–2026. It is not legally required, but:

- Compliance with the Code creates a **presumption of conformity** with GPAI obligations — meaning if you are audited, the AI Office starts from the assumption that you are compliant
- Providers who are not signatories bear the burden of demonstrating compliance through other means
- The AI Office stated publicly that non-signatories will receive more scrutiny during the first enforcement cycle

Major AI providers — Anthropic, Google, OpenAI, Meta, Mistral, Cohere — have signed the Code or are in the process of doing so. The Code was finalized in May 2026. The full text is available via the EU AI Office at the European Commission's Digital Single Market portal.

If you are a GPAI provider who has not yet engaged with the Code, the time to sign and begin aligning documentation practices is now, not in September.

---

## What API-First Builders Actually Need to Know

If you build on GPAI models via API (Anthropic, OpenAI, Google, etc.) and do not modify or redistribute model weights, your GPAI compliance exposure is minimal. The Act is explicit that deployers who use GPAI via API are not providers.

Three scenarios where this changes:

**Scenario 1: You fine-tune and re-distribute.** If you fine-tune a foundation model and offer the fine-tuned model to others (via API, download, or enterprise contract), you may become a GPAI provider of the modified model. The threshold is not bright-line. If your fine-tune is narrow (domain adaptation, tone adjustment) and you are serving it only to your own product's users, the AI Office has indicated this is likely deployer territory. If you are licensing the fine-tune to third parties, you are in provider territory.

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
- [ ] Establish serious incident reporting process (15-day initial / 30-day full report)
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

The AI Office's first-year enforcement posture is expected to focus on the largest providers and on SEND platform registration — not on smaller developers. But the documentation requirements are ongoing, and the audit clock starts ticking on August 2. Non-compliance discovered in a 2027 audit will be measured against obligations that began in August 2025.

High-risk AI applications built on GPAI models have their own compliance calendar (December 2027 for standalone, August 2028 for embedded). If your product uses a GPAI model as a component in a high-risk use case — credit scoring, hiring automation, access to essential services — start the Annex III analysis now, even though enforcement is two years out. The documentation requirements for Annex III draw heavily on the GPAI technical documentation already required. Building one GPAI documentation package now reduces duplicated work later.

The EU AI Act is the first comprehensive AI regulation with enforcement teeth. August 2, 2026 is when those teeth engage.

