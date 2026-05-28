---
title: "Canada Ruled ChatGPT Was Built on Broken Privacy Law. Here's What Builders Need to Know."
date: 2026-05-28
description: "On May 6, four Canadian privacy regulators released findings from a three-year joint investigation into OpenAI's ChatGPT. The core ruling: scraping public internet data does not constitute valid consent for AI training. Builders deploying AI in Canada should read this carefully."
og_description: "Canada's four privacy regulators jointly found OpenAI violated federal and provincial privacy law in developing ChatGPT. Six specific violations. BC and Alberta said the problem is unresolvable. The federal OPC conditionally resolved it. Key precedent: public internet data ≠ implied consent for novel AI training purposes. What this means for builders with Canadian users."
content_type: "Builder's Log"
categories: ["AI Policy", "Enterprise AI", "Industry Analysis"]
tags: ["privacy", "regulation", "canada", "pipeda", "openai", "chatgpt", "training-data", "compliance", "enterprise", "governance", "consent", "data-protection", "analysis"]
---

On May 6, 2026, four Canadian privacy regulators released the results of a joint three-year investigation into OpenAI's ChatGPT. The Office of the Privacy Commissioner of Canada (OPC), plus counterparts in British Columbia, Alberta, and Quebec, concluded that **OpenAI violated Canadian privacy law** in how it collected training data and how it handled user information.

The regulatory outcome was split: the federal OPC called it "conditionally resolved," while BC and Alberta called it "well-founded but unresolved" — meaning they believe the violation cannot be fixed without retroactively obtaining consent that was never obtained.

For builders deploying AI products in Canada, this ruling rewrites several assumptions that have been standard operating procedure since the industry began.

---

## What the Investigation Found

The joint probe identified six categories of violation:

**1. Overcollection.** OpenAI scraped personal information — health data, political views, children's information — far beyond what was necessary for any specific purpose the company could clearly articulate at the time of collection.

**2. Invalid consent.** The core finding: individuals whose information appeared on the public internet did not meaningfully consent to that information being used to train a large language model. The regulators found this was "an extremely novel, not widely understood practice" at the time — which matters legally because implied consent depends on reasonable expectations.

**3. No retention or deletion policies.** ChatGPT launched commercially in late 2022 without formal policies governing how long personal information would be retained or when it would be deleted.

**4. Deceptive opt-out design.** Until April 2024, users who wanted to opt out of having their chat history used for model training had to disable chat history entirely — losing the ability to return to previous conversations. The regulators flagged this as a design pattern that coerces consent by attaching a feature cost to opting out.

**5. Inaccuracy involving real people.** ChatGPT generated false statements about real, identifiable individuals. OpenAI launched with known hallucination rates and no systematic mechanism to detect or correct false outputs about specific people.

**6. Inadequate access and correction rights.** Individuals had limited practical ability to access, correct, or delete their personal information that had been incorporated into model training.

---

## The Ruling's Pivotal Legal Reasoning

The most significant part of PIPEDA Findings #2026-002 is not the list of violations — it is the underlying legal reasoning about **what counts as valid consent for internet-scraped data**.

Under PIPEDA (Canada's federal private-sector privacy law) and its provincial equivalents, organizations can rely on **implied consent** for collecting and using personal information in some circumstances. The question is whether the use falls within the reasonable expectations of the individuals whose data was collected.

The regulators ruled that it does not — at least for AI training at scale. Their reasoning:

> "Individuals whose information was scraped by OpenAI would not have reasonably expected that information posted publicly on the Internet could be collected and used to train its models, a practice which was extremely novel and not widely understood at the time."

This is a meaningful legal standard. It doesn't say that scraping public internet data is always invalid under privacy law — it says that **novelty of purpose defeats implied consent**. A person who posts on a public forum in 2019 is not implicitly consenting to uses of that data that didn't exist as a mainstream commercial practice when they posted.

---

## Why the Provincial Split Matters

The federal OPC found the complaint "conditionally resolved" — meaning OpenAI agreed to implement fixes, and the OPC accepted those commitments as sufficient under PIPEDA.

British Columbia and Alberta reached a harder conclusion: **well-founded but unresolved**. Their reasoning is that their provincial privacy statutes are more explicit than PIPEDA about consent requirements, and that:

> "OpenAI's models are based on scraped data for which it has not obtained — and cannot obtain — valid consent."

The "cannot obtain" language is the significant part. BC and Alberta are not saying OpenAI failed to follow a correctable procedure. They are saying that **the underlying training data problem cannot be remedied after the fact**, because you cannot go back to billions of internet users and obtain retroactive consent for data that was already used.

This creates an unresolved legal cloud in those provinces over AI products trained on internet-scraped data. The provincial regulators did not issue an enforcement order, but the finding is on record.

---

## What OpenAI Committed To

To satisfy the federal OPC's "conditionally resolved" standard, OpenAI agreed to implement several measures:

- **Personal information filtering**: A tool that detects and masks identifying information — names, phone numbers, and similar data — in publicly accessible training datasets
- **Enhanced correction and deletion protocols**: Improved mechanisms for individuals to request correction or deletion of personal information
- **Formal retention policy**: A documented schedule governing how long personal information is held and when it is disposed of
- **Transparency improvements**: Clearer disclosure about what data is collected and how it is used

The OPC will monitor compliance. If OpenAI fails to implement commitments, the OPC can refer the matter to the Federal Court.

---

## What This Means for Builders

The ruling creates five practical questions for any AI builder with Canadian users:

**1. Do you know what data your models (or your vendors' models) were trained on?**

If you are building on top of a foundation model trained on internet-scraped data, the BC/Alberta finding creates at least a theoretical compliance exposure in those provinces. This is unlikely to result in enforcement against an application developer right now — but enterprise procurement teams and legal departments in regulated industries will ask.

**2. Are your consent mechanisms collecting actual consent, or relying on implied consent for novel uses?**

The Canadian regulators drew a clear line: implied consent fails when the use case is unfamiliar to the average person. If you are collecting user data and using it to train or fine-tune a model, "it's in our terms of service" is not sufficient. You need explicit, granular, separate consent for model training.

**3. Do you have a retention policy?**

The finding that ChatGPT launched without any formal data retention or deletion policies is a compliance failure that most enterprise procurement checklists now include. If you do not have one, write one before your next enterprise deal.

**4. Is your opt-out design clean?**

The deceptive design finding is about tying opt-out from data training to loss of features. Don't do this. Consent to use data for model training should be separable from consent to use a product's features.

**5. Can your users correct or delete their information?**

Canadian privacy law gives individuals the right to access, correct, and delete their personal information. If your product incorporates user data into model behavior — even through fine-tuning or retrieval — you need a mechanism for users to exercise those rights.

---

## Context: Where This Sits in the Regulatory Landscape

The Canada ruling is not the first finding that ChatGPT-era AI training violated privacy law, but it is the most comprehensive investigation by a federal privacy authority in a major Western democracy to have been fully completed and published.

Italy's Garante suspended ChatGPT temporarily in March 2023 before reinstating it with conditions. Several EU data protection authorities launched investigations under GDPR. The UK ICO published guidance but no binding findings.

Canada's investigation is significant because it is:

- **Completed**: A full published decision, not an ongoing probe
- **Multi-jurisdictional**: Four regulators jointly coordinated
- **Specific**: Six named violations with accompanying reasoning
- **Precedential**: The "novelty defeats implied consent" reasoning will be cited in other jurisdictions

The ITIF (Information Technology and Innovation Foundation), a US policy organization, argued that Canada's ruling "sets a bad precedent" by making AI training on publicly available data legally risky. That critique is correct as a description: the ruling does make that type of training legally riskier in Canada. Whether it is good or bad policy is a separate question.

---

## The Bottom Line

Canada's four privacy regulators spent three years examining how ChatGPT was built and concluded that the process broke the law at multiple points. The most important finding is not procedural — it is the core ruling that publicly available data on the internet does not constitute implied consent for novel AI training uses that individuals could not have reasonably anticipated.

BC and Alberta went further: they said this problem is not fixable after the fact.

If you are building AI products for Canadian users, or procuring AI services for a Canadian enterprise, this ruling is the clearest statement yet of what your vendors are legally expected to have done with their training data — and what you are expected to do with user data you collect going forward.

---

*Filed under AI Policy and Enterprise AI. Related: [CAISI and US Government AI Testing](/builders-log/caisi-frontier-ai-government-testing-enterprise-builders/), [Anthropic/Pentagon and the Supply Chain Designation Controversy](/builders-log/anthropic-managed-agents-lock-in/).*
