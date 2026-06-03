---
title: "NY A3411B Is Heading to Hochul's Desk. Every GenAI Builder Has 90 Days After She Signs."
date: 2026-06-04
slug: ny-a3411b-genai-disclosure-bill-builder-ui-compliance-guide
description: "New York's A3411B passed both legislative chambers on March 9, 2026. It requires every owner, operator, and licensee of a generative AI system to display a clear disclosure notice in the UI. This is not a frontier-developer law — it applies to you. Here's what it says and what to build."
tags:
  - regulation
  - new-york
  - compliance
  - genai
  - ui
  - disclosure
  - builders-log
categories:
  - builders-log
---

New York's RAISE Act gets all the press. It's a serious law — 72-hour incident reporting to the DFS, quarterly risk assessments, mandatory registration for frontier model developers. But it covers six companies.

**A3411B covers everyone else.**

On March 9, 2026, the New York legislature passed the Artificial Intelligence Disclosure Act — Assembly Bill A3411B — with broad bipartisan support. It is waiting on Governor Hochul's desk. She signed the RAISE Act. There is no public indication she will veto this one.

When she signs it, a 90-day clock starts. At the end of that clock, if you operate any generative AI system accessed by users in New York, you need a disclosure notice in your UI. One line. Mandatory.

---

## What A3411B Actually Says

The operative requirement is straightforward:

> Any owner, licensee, or operator of a generative artificial intelligence system shall clearly and conspicuously display, on the user interface of such system, a notice stating that generative AI outputs may be inaccurate.

Three things matter in that sentence:

**"Owner, licensee, or operator"** — The law captures the full distribution chain. The model developer is one layer. The API user (you) is another. If you wrap Claude, GPT-5, Gemini, or any other generative model in a product and ship it to users, you are an operator. You are covered whether you built the model or not.

**"Generative artificial intelligence system"** — The bill defines generative AI broadly: systems that produce novel text, images, audio, video, or other outputs from patterns learned during training. Chatbots, copilots, summarization tools, image generators, coding assistants — all in scope. An AI feature inside a larger product counts.

**"Clearly and conspicuously"** — This is the design requirement. The notice must be actually noticeable, not buried in a terms-of-service link at page bottom. The bill does not prescribe exact placement, font size, or language beyond the substance — but "clear and conspicuous" is a legal standard courts have interpreted in consumer protection contexts to mean: a reasonable user would not miss it.

---

## How It Differs from the RAISE Act

The RAISE Act and A3411B are companion legislation aimed at different layers of the AI stack.

| | RAISE Act | A3411B |
|---|---|---|
| **Who it covers** | Frontier model developers ($500M revenue, 10^26 FLOPs) | All owners/operators/licensees of GenAI systems |
| **What it requires** | Registration, safety protocols, incident reporting, DFS oversight | UI disclosure notice |
| **Effective date** | January 1, 2027 | 90 days after signing |
| **Target entities** | ~6 companies | Thousands of builders |
| **Enforcement** | NY Department of Financial Services | TBD via AG or civil action |

The RAISE Act is an enterprise compliance program for AI infrastructure companies. A3411B is a consumer protection measure for everyone building AI products. If you are shipping a GenAI feature to users, A3411B is the one that applies to your roadmap.

---

## The 90-Day Window

A3411B takes effect 90 days after Governor Hochul signs it. There is no staged rollout, no grace period for small developers, no revenue threshold. The law passed both chambers. The policy intent is clear. Builders who want to be compliant on day one should be implementing now.

What you need to do before the deadline:

1. **Audit your UI surfaces** — Identify every interface where users interact with generative AI output. This includes embedded chat features, document copilots, AI-generated summaries, image generators, and code completions displayed to users.

2. **Design the disclosure element** — The notice needs to be clear and conspicuous. Reasonable implementation options:
   - A persistent one-line banner at the top or bottom of the AI interaction surface
   - A badge or tooltip attached to AI-generated content
   - A disclosure displayed before the first AI interaction in a session, with persistent access thereafter
   - An inline label adjacent to generated content ("AI-generated · may be inaccurate")

3. **Draft the disclosure copy** — The bill specifies the substance: that generative AI outputs may be inaccurate. The exact wording is not mandated. Common formulations in production today:
   - *"AI-generated content may be inaccurate. Verify important information."*
   - *"This response was generated by AI and may contain errors or outdated information."*
   - *"Powered by AI. Outputs may be inaccurate — always review before acting."*

4. **Confirm it survives mobile** — "Clear and conspicuous" on desktop may not translate to mobile without intentional design. Test your disclosure on the smallest screen your users access.

5. **Update your privacy policy or terms** — Reference the disclosure requirement for legal alignment. This is not required by the bill but is standard practice for consumer-facing compliance documentation.

---

## New York's Jurisdictional Reach

A3411B applies to users in New York. In practice, this means most builders shipping a consumer or B2B SaaS product in the US need to comply — carving out New York users from a UI feature is not a realistic enforcement boundary.

New York has approximately 20 million residents. The New York City metro area alone is the largest market for technology products in the United States. For any product with meaningful US user distribution, this law sets your disclosure standard nationally.

This is the same dynamic that made California's CCPA the de facto US privacy standard for most companies. New York's AI disclosure requirement will function similarly: you will implement it everywhere rather than maintain a state-specific variant.

---

## What the Notice Does Not Do

A3411B is a disclosure requirement, not an accuracy standard. It does not:

- Require that AI outputs meet a quality or accuracy threshold
- Create liability for incorrect AI outputs
- Mandate human review before delivery
- Restrict which use cases can use generative AI
- Apply to internal enterprise tools with no external user interface

If your AI system is used entirely within your organization by employees who understand what they are using, the consumer protection logic of the bill arguably does not apply — though the plain text of "operator" is broad enough that legal counsel should confirm your specific situation.

The law also does not specify how long the disclosure must persist. A reasonable interpretation is that it should be visible whenever users are interacting with AI-generated content, not just displayed once at account creation.

---

## Relationship to Other Disclosure Requirements

A3411B is part of an accelerating pattern of required AI disclosures across jurisdictions. Builders planning compliance should review the full landscape:

**Already in effect:**
- **EU AI Act, Article 52** — GPAI system providers must label AI-generated content (effective August 2026 for most provisions). Requires machine-readable watermarking in addition to UI disclosure for some content types.
- **California AB 2013 (2024)** — Requires "synthetic media" disclosures for AI-generated political content. Narrower scope than A3411B.
- **FTC guidance on AI transparency** — Not legally binding, but the FTC has treated undisclosed AI in consumer interactions as a deceptive practice in enforcement actions.

**Coming in 2027:**
- **New York RAISE Act** — Frontier developers must publish pre-deployment transparency reports accessible to the public. Builds on the disclosure foundation A3411B establishes at the UI layer.
- **Illinois SB 315** — Annual third-party safety audits for frontier developers, effective January 1, 2027. Focuses on the model layer, not the product layer.

The trend is consistent: every jurisdiction that has moved on AI regulation has included some form of disclosure or transparency requirement. A3411B is New York's entry at the product layer. Builders who implement clean, clearly designed disclosure practices now will be ahead of the next wave.

---

## What To Do Today

A3411B is not yet law. But it passed both chambers of the New York legislature by wide margins. The path to a signed bill is short.

If you ship a product with generative AI features to users in New York — which, practically, means if you ship to US users — the action items are:

- Add A3411B compliance to your engineering roadmap with a 90-day buffer from today
- Design your disclosure element now, before you are doing it under deadline pressure
- Pick a disclosure copy standard and apply it consistently across your product
- If you are a platform offering AI features to downstream builders (not just end users), determine whether your terms of service require your customers to implement their own disclosures or whether you cover them

The disclosure is not technically complex. It is one element in your UI. The window is the issue — when a governor signs a bill, 90 days moves faster than most product roadmaps.

---

*Related: [New York's RAISE Act Is Already Signed — the Three-State AI Compliance Stack You Need to Know](/builders-log/new-york-raise-act-frontier-ai-compliance-builder-guide/)*
