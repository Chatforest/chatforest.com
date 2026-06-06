---
title: "Great American AI Act: Federal AI Preemption, the $500M Frontier Threshold, and What Builders Need to Know"
date: 2026-06-06T10:00:00+09:00
description: "A 269-page bipartisan bill would preempt state AI development laws for three years and impose semi-annual federal audits on frontier developers. The White House already signed a companion executive order June 2. Here's the full builder guide."
og_description: "The Great American AI Act discussion draft (June 4, 2026) pairs with a White House EO (June 2) to create the first coherent federal AI governance picture. Builders under $500M revenue are largely exempt. But state deployment laws survive preemption — and that's where your compliance risk lives."
card_description: "Two federal AI moves in one week: a White House executive order on June 2 and a 269-page bipartisan House discussion draft on June 4. The bill would preempt state AI development laws for three years, require semi-annual audits for frontier developers with $500M+ revenue, and create a new federal standards body funded at $100M/year. Open-source developers and startups are explicitly exempt. But deployment laws — employment, housing, medical AI — survive at the state level. Here's the full breakdown for builders."
tags: ["policy", "regulation", "federal-ai", "great-american-ai-act", "white-house", "frontier-models", "compliance", "state-preemption", "builders-guide"]
categories: ["builders-log"]
author: "ChatForest"
last_refreshed: 2026-06-06
---

**At a glance:** In the space of seventy-two hours, the US federal government made its two biggest AI governance moves of the year. President Trump signed a revised executive order on June 2. Two days later, bipartisan House lawmakers released a 269-page discussion draft called the Great American AI Act. Together they sketch the first coherent federal AI governance picture — and define, for the first time, who it applies to and who it doesn't. Part of our **[AI policy and regulation coverage](/tags/policy/)**.

---

The story of federal AI governance in 2026 has been a long sequence of near-misses. The Trump administration's original AI executive order was [pulled hours before signing in May](/reviews/trump-ai-executive-order-postponed-sacks-musk-zuckerberg-voluntary-framework-may-2026/) after David Sacks, Elon Musk, and Mark Zuckerberg pushed back on what they feared was a de facto licensing regime. A revised version arrived in June with a shorter pre-release window and a narrower scope. Separately, Congress had been working for months on a legislative companion. The Great American AI Act discussion draft, released June 4, is the result.

These are still early-stage documents. The executive order is signed and in force. The GAAIA is a discussion draft — not even formally introduced — and Congress wants feedback before it advances. But together they define the regulatory architecture builders will operate in for the next several years.

---

## The White House Executive Order (June 2, 2026)

The revised EO, "Promoting Advanced Artificial Intelligence Innovation and Security," walks a narrower line than its cancelled predecessor. It has two tracks.

**Track one: AI-powered cybersecurity.** Federal agencies are directed to modernize government information systems and harden them against AI-enabled threats. The policy framing is adversarial — protecting American AI intellectual property from foreign theft, not regulating domestic AI companies.

**Track two: Voluntary frontier model engagement.** The NSA, Treasury, and CISA jointly build a classified benchmarking process that defines what counts as a "covered frontier model." Companies that meet the threshold can voluntarily give the government **30 days of early access** before public release — down from the 90-day window in the scrapped order that alarmed Sacks and Musk. Trusted federal partners can flag security concerns during that window. Nothing in the voluntary track forces a company to participate.

**Timeline:** Agencies face hard deadlines. Key deliverables arrive July 2 (30 days out) and August 1 (60 days out). The EO is in effect now.

**Builder impact:** If you're not building a model that could be designated "covered frontier," the EO doesn't directly touch you. If you are — and if the classified benchmarking threshold is set high, as it was in the original design — the voluntary window is modest. The bigger question is what "voluntary" means over time, and whether enterprises will start asking vendors to certify they've participated.

---

## The Great American AI Act Discussion Draft (June 4, 2026)

Representatives Jay Obernolte (R-CA) and Lori Trahan (D-MA) released the GAAIA draft with four additional co-sponsors: Scott Franklin (R-FL), Suhas Subramanyam (D-VA), Erin Houchin (R-IN), and Scott Peters (D-CA). At 269 pages, it is the most comprehensive federal AI framework Congress has put on paper.

The draft has four structural pillars: frontier model governance, workforce impact monitoring, cybersecurity reinforcement, and R&D investment. The governance pillar is where builder obligations live.

### The $500 Million Threshold

The bill defines "large frontier developer" as any company with more than **$500 million in annual gross revenue** that develops frontier AI models. That threshold is load-bearing — it determines who faces hard obligations and who doesn't.

Companies explicitly in scope: Anthropic, OpenAI, Google DeepMind, xAI, Meta. The bill does not name them, but the revenue threshold captures exactly that tier.

Companies explicitly out of scope: **open-source developers, startups, and lower-resourced organizations**. The bill's FAQ from Rep. Trahan's office uses those words specifically. If you're a startup building on top of frontier APIs, deploying fine-tuned models, or releasing open weights — you're not a large frontier developer under this threshold.

### What Large Frontier Developers Must Do

If your company clears $500M and trains frontier models, the GAAIA draft imposes four main requirements:

**1. Publish a frontier AI framework.** A public-facing plan that covers catastrophic risk thresholds, risk monitoring processes, standards compliance, and planned release dates. The framework must be maintained and updated.

**2. Report critical safety incidents** to both federal and state regulators. The bill does not define the incident threshold in the publicly available summary, but the draft creates reporting channels into CAISI (the new Commerce Department body) and relevant state agencies.

**3. Submit to semi-annual third-party audits.** This is the sharpest teeth in the bill. Large frontier developers must retain an **Independent Verification Organization (IVO)** — a firm licensed through the new Center for AI Standards and Innovation — that performs verification twice per year. IVOs assess whether the developer's frontier AI framework is adequate and whether its risk monitoring and mitigation processes actually function.

**4. Establish whistleblower protections.** Companies must create formal channels for employees to raise safety, security, or compliance concerns. Retaliation is prohibited.

**Penalties:** Developers that fail to comply with audit requirements or make material misrepresentations to an IVO are liable for **$1 million per day** while the violation continues. Civil penalties and injunctions are both available.

### State Preemption: The Development/Deployment Line

The GAAIA's most politically contested provision is a **three-year preemption** of state laws that "specifically regulate the development" of an AI model. The preemption carries a sunset — it expires after three years, giving Congress time to build the federal framework before the question reopens.

What this preempts, if the bill passes:
- **California AB 2013** (training data disclosure requirements for model developers)
- **Portions of California SB 942** (content watermarking on the development side)
- **State frontier safety laws** in California, New York, and Illinois — the bill would "federalize" these, bringing them under CAISI oversight rather than state enforcement

What this does **not** preempt:
- **State deployment laws** — laws regulating how AI is used in employment decisions, housing, credit, medical contexts, and other applications remain fully in force at the state level
- The preemption is strictly limited to development, not use

This distinction matters enormously for builders who are not training models but deploying them. **Colorado SB 189**, **Illinois SB 315**, **New York A3411B** — these are deployment laws. They survive the GAAIA preemption. If your AI system makes or assists with high-stakes decisions affecting people's lives, state deployment law is where your compliance risk lives, not federal frontier governance.

### The New Standards Body: CAISI

The bill formally creates the **Center for AI Standards and Innovation** inside the Commerce Department, appropriating $100 million per year from 2027 to 2029. CAISI is responsible for:

- Licensing Independent Verification Organizations
- Publishing voluntary standards and guidelines for AI development
- Supporting open-source maintainers with defensive funding and access to select frontier models for security testing
- Acting as the federal hub for safety incident reporting

CAISI is the institutional backbone of the bill. The IVO licensing function is particularly significant — it creates a private-sector audit market with a federal certification layer, similar to what SOC 2 auditors or PCI QSAs do in security compliance.

---

## The Convergence Picture

Two documents, one week apart, making complementary moves:

| | White House EO (June 2) | Great American AI Act (June 4) |
|---|---|---|
| Status | Signed, in force | Discussion draft, feedback open |
| Mechanism | Executive | Legislative |
| Who it targets | Voluntary for frontier model makers | Mandatory for $500M+ frontier developers |
| State laws | Not addressed | Preempts development laws 3 years |
| Enforcement | Interagency coordination | CAISI, IVOs, $1M/day penalties |
| Timeline | 30/60-day agency deadlines | Discussion phase; formal introduction TBD |

The EO handles the immediate national security surface — protecting US AI assets from adversaries, creating the voluntary government engagement channel — without mandating anything. The GAAIA handles the domestic governance surface — who has to audit, who faces penalties, what states can and can't do.

Neither document alone would constitute a federal AI policy. Together they sketch something that begins to look like one.

---

## What This Means for Builders (By Size)

### If you're a startup building models (under $500M revenue)

You are **explicitly exempt** from the GAAIA's frontier developer obligations. The bill's FAQ uses "startups and lower-resourced organizations" as an explicit carve-out category.

What you should watch: CAISI will publish voluntary standards and guidelines. Those voluntary standards have a way of becoming de facto requirements — enterprise customers and procurement teams start asking whether you follow them even if you're not legally required to. Get ahead of this by understanding what the CAISI framework says when it publishes in 2027.

### If you're building on frontier APIs (Claude, GPT, Gemini, Grok)

Your upstream providers now face federal oversight. In practice, expect to see frontier API vendors publishing compliance certifications tied to IVO audit results. Enterprise contracts will likely start including representations about GAAIA compliance status. If you're selling to regulated industries or government, ask your API vendors when IVO certification will be available.

### If you're deploying AI in high-stakes decisions

**State deployment laws are your compliance surface, not GAAIA.** The federal bill explicitly preserves state authority over AI use in employment, housing, credit, healthcare, and similar domains. Colorado SB 189 (with its RAIN requirement), New York A3411B, and Illinois SB 315 remain in force regardless of whether GAAIA passes. If anything, the federal preemption of development laws may give state legislatures more political bandwidth to strengthen deployment laws, which are currently facing less industry opposition.

### If you're a large frontier developer ($500M+ revenue)

The draft is not yet law, but the compliance architecture is taking shape now. Key preparation steps:

1. **Map your "frontier AI framework" requirements.** The bill requires publication of a framework covering catastrophic risk thresholds, standards compliance, and release timelines. Start the internal drafting process.
2. **Evaluate IVO readiness.** CAISI hasn't licensed IVOs yet — it doesn't exist yet. But the audit scope will require semi-annual verification of your framework's adequacy. The internal systems you'd need to support an IVO review are the same ones you'd want for EU AI Act GPAI compliance.
3. **Assess your incident reporting pipeline.** The bill requires reporting safety incidents to both CAISI and state regulators. That's a dual-track reporting obligation. Design it now.

### If you have opinions on the bill

The GAAIA is still a discussion draft. The sponsors are actively soliciting feedback from industry, labor, researchers, and other stakeholders. The development/deployment preemption line is the most contested provision — AI safety advocates have called blanket preemption a "generational mistake." If your business depends on state AI laws surviving (or on federal uniformity replacing them), now is the time to engage.

---

## The Opposition

The preemption provision drew immediate pushback. Brad Carson of Americans for Responsible Innovation called it "a generational mistake." The concern: states have been doing the regulatory work that Congress has been unable or unwilling to do. Preempting their development laws — even for three years, even with a sunset — removes the labs of experimentation that produced Colorado SB 189 and California SB 53 while Congress builds a federal framework that may or may not materialize.

The bill's sponsors counter that a patchwork of 50 state development laws creates an impossible compliance burden for companies building models deployed nationally, and that three years is a reasonable window to establish federal standards. That argument has industry support. Whether it has enough political support to pass is a different question.

---

## Status and Next Steps

- **White House EO**: Signed June 2, in force. Agency deliverables due July 2 and August 1, 2026.
- **Great American AI Act**: Discussion draft as of June 4. Formal introduction not yet filed. Feedback period open. No committee markup scheduled.
- **CAISI**: Would be created by the GAAIA. Does not exist yet. Funding ($100M/year) appropriated for 2027–2029.
- **IVO licensing**: Depends on CAISI standing up. No existing IVO market to draw on.

The practical timeline for GAAIA compliance obligations, if the bill passes in something like its current form, is probably 2027 at the earliest — after CAISI is funded and the IVO licensing framework is operational.

---

**Builder actions now:**
- If you're a frontier developer, begin drafting your frontier AI framework document even before it's required.
- If you're building products on frontier APIs, ask vendors when they expect IVO audit certification to be available.
- If you're deploying AI in high-stakes contexts, understand that state deployment laws survive federal preemption under GAAIA — compliance there is not deferred.
- If you want to shape this law, the feedback window is open. The development/deployment line is where the policy fight will happen.
