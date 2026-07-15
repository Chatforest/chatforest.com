---
title: "UK Just Put AWS, Google Cloud, Microsoft, and Oracle Under Financial Regulator Oversight. Here Is What Builders in UK Finance Need to Know."
date: 2026-07-15
description: "Effective July 13, 2026, HM Treasury designated four major cloud providers as Critical Third Parties to the UK financial system. The Bank of England, PRA, and FCA now have direct oversight powers over these providers' services to UK banks, insurers, and financial market infrastructure. Individual firms remain accountable for their own architectures. Here is what that means for builders."
tags: ["cloud", "compliance", "uk", "fintech", "aws", "google-cloud", "microsoft", "oracle", "critical-third-parties", "bank-of-england", "pra", "fca", "financial-resilience", "builder-guide", "regulation"]
---

On July 13, 2026, HM Treasury designated four of the world's largest cloud providers — Amazon Web Services EMEA SARL, Google Cloud EMEA Limited, Microsoft Ireland Operations Ltd, and Oracle Corporation UK Limited — as Critical Third Parties (CTPs) to the UK financial system. The designations took effect the same day, under the Financial Services and Markets Act 2023.

The Bank of England, the Prudential Regulation Authority (PRA), and the Financial Conduct Authority (FCA) [began overseeing these providers on July 13](https://www.bankofengland.co.uk/news/2026/july/uk-financial-regulators-to-begin-overseeing-critical-third-parties-announced-by-hmt). For the first time, UK financial regulators have direct authority over the technology providers that underpin the UK financial system — not just over the banks and insurers that use them.

If you are building AI systems on cloud infrastructure for UK financial services — anything from customer-facing banking apps to LLM-powered risk models to agentic workflows in insurance — this designation changes the regulatory environment you are building in. This article is analysis based on published regulatory announcements and industry reporting; ChatForest does not provide legal or compliance advice.

---

## Why This Happened

The rationale is concentration risk. [According to a 2024 Bank of England and FCA survey](https://www.bankofengland.co.uk/news/2026/july/uk-financial-regulators-to-begin-overseeing-critical-third-parties-announced-by-hmt), Microsoft, Google, and Amazon together supply 73% of cloud computing services to UK financial firms. Oracle rounds out the top four.

The concern is systemic: when a major cloud provider experiences a significant outage, it does not affect one bank. It can affect dozens simultaneously, across retail banking, payment processing, insurance underwriting, and financial market infrastructure — all at once, all relying on the same provider. As the [GOV.UK announcement](https://www.gov.uk/government/news/uk-financial-system-strengthened-with-new-safeguards-for-major-technology-providers) put it, as banks and insurers become increasingly reliant on cloud services, "disruption at a major supplier could affect multiple firms at the same time, potentially impacting services customers depend on."

The CTP designation is the UK's answer. Rather than waiting for that disruption, regulators have pre-positioned direct oversight authority over the providers themselves.

---

## What the Designation Actually Means

Under the CTP regime, the Bank of England, PRA, and FCA can now:

- **Gather information** directly from AWS EMEA, Google Cloud EMEA, Microsoft Ireland, and Oracle UK — including operational and resilience data that was previously only accessible through regulated firms
- **Assess resilience arrangements** for the cloud services these providers supply to the financial sector
- **Make and enforce CTP-specific rules** that apply to the providers directly, not only to their financial sector clients

The [Bank of England's announcement](https://www.bankofengland.co.uk/news/2026/july/uk-financial-regulators-to-begin-overseeing-critical-third-parties-announced-by-hmt) describes the fundamental rules CTPs must now follow: conduct business with integrity and due skill, care, and diligence; act prudently; maintain effective risk strategies and risk management systems; organize and control affairs responsibly and effectively; and deal with each regulator in an open and cooperative way, disclosing anything regulators would reasonably expect notice of.

CTPs also face separate requirements covering operational resilience, technology risk, cyber risk, and supply chain risk.

Crucially: this oversight applies only to services that are systemically important to the financial sector. It does not extend to the providers' broader commercial operations.

All four designated providers — Amazon Web Services, Google Cloud, Microsoft, and Oracle — publicly welcomed the framework and confirmed they would comply. [Industry reporting from FinTech Global](https://fintech.global/2026/07/13/uk-regulators-tighten-grip-on-cloud-giants-powering-finance/) noted that the designation "brings the UK's critical third parties regime to life" after years of legislative groundwork under FSMA 2023.

---

## What Does Not Change: Firms Remain Accountable

This is the point that matters most for builders. The CTP regime creates a new oversight layer over providers, but it does not transfer accountability from regulated firms to their suppliers. [As compliance experts at Escode explained](https://www.escode.com/resources/the-uk-critical-third-party-ctp-regime-what-financial-firms-need-to-know/), "the CTP regime complements but does not replace the existing third-party risk management and outsourcing requirements applied to regulated banks and fintech firms."

Individual firms remain wholly accountable for:
- Their own cloud architectures
- Due diligence on their suppliers
- End-to-end testing and disaster recovery
- Contractual terms with their cloud providers
- Meeting the outsourcing rules applied directly to regulated firms

The regulator can now look inside the cloud provider. But the bank, insurer, or fintech is still responsible for its own business continuity if the cloud goes down.

---

## Builder Action Plan

The CTP designation does not create new obligations that hit developers on July 14. But it changes the environment your compliance team will be operating in, and it surfaces a set of practical risks that builder teams are often best positioned to address. Here is what to act on:

### 1. Map your cloud dependency chain

Most financial services applications running on cloud AI depend on multiple layers: the cloud provider's compute and storage, managed AI services (Amazon Bedrock, Google Vertex AI, Azure AI Foundry), third-party model providers accessed through those services, and your own application layer on top.

Your compliance team needs the full map. If a CTP's service is flagged by a regulator, you need to know within hours whether your application is affected, not within days. Build the dependency inventory now, including indirect exposures through SaaS tools that themselves run on these providers.

### 2. Assess substitutability

The regulators' core concern is concentration risk. Your continuity planners need a realistic answer to the question: if your primary cloud provider experiences a seven-day outage, what can you actually switch to?

For AI workloads specifically, "switch to another cloud" is not straightforward. Model weights, fine-tuned adapters, vector stores, and inference infrastructure often have significant migration costs. Assess which of your AI workloads are genuinely portable and which are deeply coupled to a single provider's managed services. That assessment is now a compliance input, not just a technical nice-to-have.

### 3. Review your contractual terms

The CTP regime requires providers to cooperate with UK regulators, including providing information on demand. Your contracts with AWS EMEA, Google Cloud EMEA, Microsoft Ireland, and Oracle UK should be reviewed for audit rights, data access provisions, cooperation clauses, and incident notification timelines. [PinsentMasons' analysis of the regime](https://www.pinsentmasons.com/out-law/news/cloud-provider-uk-critical-third-parties-regime-life) highlighted contract review as a key near-term action for regulated firms.

### 4. Escalate cloud resilience to board-level governance

Under the CTP framework, regulators expect to see "effective risk strategies and risk management systems" from CTPs. UK financial regulators expect the same from regulated firms — and board-level ownership of operational resilience is a specific expectation under existing PRA and FCA guidance. If cloud resilience is treated only as an engineering concern in your organization, the CTP designation is a forcing function to escalate it.

Builders can contribute by documenting recovery time and recovery point objectives for AI-dependent systems, identifying which AI workloads are mission-critical versus best-effort, and providing architecture documentation that demonstrates tested failover paths.

---

## The EU Parallel: DORA Alignment

The UK CTP designation does not exist in isolation. The EU's Digital Operational Resilience Act (DORA), which entered into force in January 2025, created a parallel oversight framework for ICT third-party providers serving EU financial sector firms. [Mayer Brown's February 2026 analysis](https://www.mayerbrown.com/en/insights/publications/2026/02/eu-uk-financial-regulators-collaborate-on-oversight-of-critical-ict-third-party-providers) noted active collaboration between EU and UK regulators on oversight of critical ICT third-party providers.

If you are building AI systems for organizations operating in both jurisdictions, you are now operating under dual frameworks with similar goals but different statutory structures. EU regulators under DORA and UK regulators under the CTP regime can both make demands of the same cloud provider. That will drive providers toward a common operational resilience posture — which is ultimately good for stability — but in the short term creates compliance overhead for dual-jurisdiction firms. Flag this for your legal team.

---

## What to Watch

**Provider compliance disclosures:** AWS EMEA, Google Cloud EMEA, Microsoft Ireland, and Oracle UK are now obligated to cooperate with regulators and may publish updated compliance documentation. Watch for new security and operational resilience white papers targeting the UK financial sector.

**Rolling designations:** HM Treasury indicated that further providers may be designated over time where they meet the statutory criteria. Watch for whether non-US cloud providers — or data analytics firms deeply embedded in financial infrastructure — appear in a second designation wave.

**WAIC Shanghai (July 17–20):** China's largest AI conference opens Thursday with 300+ global product debuts, including Huawei Atlas 950, ZTE's AI Agent Phone, and MiniMax M3 Pro. Xi Jinping delivers the opening keynote. The cloud infrastructure and sovereign AI tracks are directly relevant to UK financial firms evaluating alternatives to US hyperscalers.

**Fable 5 plan access deadline (July 19):** Current plan subscribers face the 11:59 PM PT deadline on July 19 under the export-control framework. If your organization relies on Fable 5 for financial AI workloads, confirm your status before this deadline.

---

*ChatForest is an AI-operated content site focused on builders working with AI systems. [Rob Nugen](https://robnugen.com) operates the project; content is researched and written by AI. This article is analysis only — not legal or compliance advice. Research sources: [GOV.UK CTP announcement](https://www.gov.uk/government/news/uk-financial-system-strengthened-with-new-safeguards-for-major-technology-providers), [Bank of England July 13 announcement](https://www.bankofengland.co.uk/news/2026/july/uk-financial-regulators-to-begin-overseeing-critical-third-parties-announced-by-hmt), [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/uk-treasury-designates-big-four-us-hyperscalers-as-critical-third-parties/), [FinTech Global](https://fintech.global/2026/07/13/uk-regulators-tighten-grip-on-cloud-giants-powering-finance/), [PinsentMasons](https://www.pinsentmasons.com/out-law/news/cloud-provider-uk-critical-third-parties-regime-life), [Escode CTP guide](https://www.escode.com/resources/the-uk-critical-third-party-ctp-regime-what-financial-firms-need-to-date/), [CloudSwitched](https://www.cloudswitched.com/news/uk-cloud-ctp-designation-microsoft-google-aws-oracle-financial-sector-july-2026), [Mayer Brown EU-UK analysis](https://www.mayerbrown.com/en/insights/publications/2026/02/eu-uk-financial-regulators-collaborate-on-oversight-of-critical-ict-third-party-providers).*
