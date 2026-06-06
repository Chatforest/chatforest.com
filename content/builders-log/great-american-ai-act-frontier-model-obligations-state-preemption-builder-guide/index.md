---
title: "The Great American AI Act: Federal Frontier Model Oversight, a 3-Year State Law Freeze, and What It Means for Builders"
date: 2026-06-06
description: "A 269-page bipartisan discussion draft released June 3–4, 2026 would regulate frontier AI developers, codify NIST's AI safety center, and freeze state AI development laws for three years. If your company makes under $500M/year, the core obligations don't apply to you — but the compliance landscape still changes."
og_description: "The Great American AI Act discussion draft: $500M revenue threshold, 24-hour incident reporting, semi-annual IVO audits, 3-year state law preemption on AI development. Builder's guide to what the Obernolte-Trahan bill actually says."
content_type: "Builder's Log"
categories: ["AI Policy", "Compliance", "Regulation"]
tags: ["ai-regulation", "federal-preemption", "great-american-ai-act", "gaaia", "frontier-ai", "caisi", "nist", "state-ai-laws", "compliance", "builder-guide", "obernolte", "trahan", "open-source", "incident-reporting"]
---

On June 3–4, 2026, Representatives Jay Obernolte (R-CA) and Lori Trahan (D-MA) released a 269-page bipartisan discussion draft called the Great American AI Act (GAAIA). It is the most substantive federal AI governance proposal introduced in the 119th Congress. It is not yet a formal bill — the sponsors are soliciting input before introducing it — but it signals where federal AI regulation is heading and what the compliance landscape could look like within the next twelve to twenty-four months.

The short version for most builders: **if your company makes under $500 million a year in gross revenue, the core obligations do not apply to you.** But the bill's state law preemption provision would simplify — and in some cases eliminate — the patchwork of state AI development requirements you are currently tracking.

---

## What the Bill Does

The GAAIA creates a federal framework for **frontier AI developers** built around four pillars: mandatory transparency, independent auditing, a new federal standards body, and a three-year freeze on state AI development laws.

### Who Is a "Frontier Developer"

The substantive obligations target **large frontier developers** — defined as companies with more than **$500 million in gross revenue in the previous calendar year**. That threshold explicitly exempts the vast majority of AI startups, independent developers, and open-source projects from the reporting and audit requirements.

If your company crosses that threshold, the following apply. If it does not, the federal preemption of state development laws is still relevant to you, but the compliance machinery is not.

---

## The Four Core Obligations for Frontier Developers

### 1. Frontier AI Framework (Public Document)

Before or concurrent with deploying a new frontier model, large frontier developers must publish a **Frontier AI Framework** covering:

- Risk thresholds and assessment procedures for **catastrophic risk** — defined as a foreseeable and material risk of death or injury to more than **50 people**, or more than **$1 billion in property damage**
- Cybersecurity of nonpublic model weights
- Internal and external deployment decision criteria
- How the developer responds to critical safety incidents
- How the developer manages risk from the model circumventing human oversight

The framework is a public document. This is closer to a structured disclosure requirement than a licensing regime — you publish your risk posture, not ask permission to deploy.

### 2. Pre-Deployment Reporting

Before or simultaneously with any new frontier model deployment, developers must publish a report disclosing:

| Field | Required |
|-------|---------|
| Release date | Yes |
| Supported languages | Yes |
| Output modalities | Yes |
| Intended use | Yes |
| Use restrictions | Yes |
| Risk assessments | Yes |
| Mitigation steps taken | Yes |

### 3. Incident Reporting

| Incident Type | Reporting Window |
|--------------|-----------------|
| Critical safety incident | Within 15 days |
| Imminent risk of death or serious injury | Within **24 hours** |

The 24-hour window for imminent-risk incidents is aggressive. At frontier scale, this implies real-time safety monitoring infrastructure with defined escalation paths — not something that can be built after the fact.

### 4. Independent Verification Organizations (IVO Audits)

Frontier developers must retain an **Independent Verification Organization** — a third-party auditor certified by the new Center for AI Standards and Innovation (CAISI) — to conduct **semi-annual audits** of compliance. IVOs must have sufficient access to company materials and report findings to CAISI.

Non-compliance penalties: up to **$1 million per day** while the violation continues. Material misrepresentations trigger the same ceiling.

---

## The New Standards Body: CAISI

The bill codifies and expands the Center for AI Standards and Innovation within the Department of Commerce, currently housed at NIST. CAISI would be led by a Secretary-appointed Director and authorized at **$100 million per year for fiscal years 2027–2029**.

CAISI's responsibilities include:

- Developing voluntary guidelines, best practices, and standards for adversarial robustness, interpretability, supply chain threats, and model tampering
- Testing and evaluating frontier AI systems
- Administering the IVO certification and auditing regime
- Coordinating with federal agencies and international standards bodies
- Running AI security testbeds (in partnership with DOE and federal labs), including a public hackathon component

This is not a new agency — it is an expansion and codification of existing NIST infrastructure. That distinction matters for implementation speed. Commerce does not need to stand up something from scratch.

---

## State Law Preemption: The Three-Year Development Law Freeze

The most contested provision: the bill would preempt state laws "specifically regulating the **development**" of an AI model, with a **three-year sunset**.

Key nuances matter here:

- Preemption covers **development** laws only — not **deployment** or **use** laws
- States retain full authority over AI employment discrimination, consumer protection, housing, and other use-focused legislation
- Laws of "general applicability" that touch AI indirectly are not preempted
- The three-year sunset means this reverts to the pre-bill state-by-state dynamic in 2029 unless Congress acts again

**California-specific effects:** AB 2013 (requiring model developers to publicly post training data summaries) and the AI-development portion of SB 942 (content watermarking at the development stage) would be preempted.

**Colorado:** Already substantially changed — Colorado SB 189 (signed May 2026) repealed and replaced the Colorado AI Act, removing the duty of care, risk management programs, and impact assessments in favor of a lighter disclosure framework. By the time GAAIA would take effect, Colorado's landscape will already have shifted.

**Context for the three-year duration:** The Senate struck a 10-year AI moratorium from the budget reconciliation bill in July 2025 by a 99-1 vote. Obernolte and Trahan are proposing a narrower scope (development only, not deployment) and a shorter timeframe (three years, not ten) in direct response to that rejection. Whether that narrowing is enough to survive Senate scrutiny is an open question.

---

## Open-Source Carve-Out and Funding

Open-source developers are explicitly outside the frontier developer obligations. The bill goes further: CISA and CAISI would actively assist open-source software maintainers, and open-source maintainers would be eligible for **funding** to detect and patch AI-related vulnerabilities. They would also receive access to select frontier models for security research.

This is a notable structural choice — federal funds flowing to open-source AI security maintainers, not just creating compliance burdens for them.

---

## Current Status

The GAAIA is a **discussion draft**. It has not been formally introduced as a bill. There is no committee referral, no markup scheduled, and no stated timeline for formal introduction.

The sponsors are soliciting input at: **GAAIA@mail.house.gov**

This is not window dressing — the 99-1 Senate vote against the 10-year moratorium gave both parties reason to tread carefully on federal preemption. Obernolte and Trahan appear to be genuinely road-testing the proposal before committing it to the legislative process.

---

## Opposition

The preemption provision drew immediate organized opposition:

- **Public Citizen** called it "a disastrous proposal that Big Tech is celebrating" that strips states of authority to respond to real consumer harms — algorithmic discrimination, housing, employment, youth mental health, AI companions, deepfakes.
- **AFL-CIO** and **American Federation of Teachers** both issued formal opposition, with AFT President Randi Weingarten calling it "a giveaway to the AI industry."
- A **coalition of 40+ civil society organizations** publicly urged Trahan not to co-sponsor the preemption provision before the draft was released.
- **Americans for Responsible Innovation** ran paid advertising in Massachusetts specifically targeting Trahan.
- A **bipartisan group of state lawmakers** condemned federal preemption efforts generally.

Industry reception was more favorable in tone, with ITI welcoming the CAISI codification and international standards provisions, and BSA expressing willingness to engage on the definitions and thresholds.

---

## Builder Checklist

**If your company makes under $500M/year in gross revenue:**

1. Monitor — you are not directly regulated, but the policy direction tells you where federal attention is focused.
2. If the state preemption passes, your compliance scope for AI *development* obligations narrows to federal-only for three years — watch which state development laws drop off your tracking list.
3. State *deployment* and *use* laws (employment discrimination, consumer protection, etc.) remain fully in effect regardless of GAAIA.
4. Open-source developers: watch for CISA/CAISI funding opportunities for AI security work.

**If your company is approaching or exceeding $500M/year:**

1. Map your current incident response times against the 24-hour imminent-risk reporting window. This requires infrastructure — not just policy.
2. Assess what your Frontier AI Framework would need to say. The catastrophic risk definition (50+ deaths or $1B+ property damage) is the key threshold for the most serious obligations.
3. Start identifying what a semi-annual IVO audit regime would look like for your model deployment pipeline. IVO certification doesn't exist yet (CAISI has to build that program), but the structure is clear enough to begin planning.
4. The $1M/day non-compliance penalty is serious. Build compliance tracking now rather than retroactively.

**For all builders:**

The GAAIA's passage is not guaranteed. The Senate's 99-1 rejection of the broader moratorium and the organized opposition to the preemption provision make this a genuine legislative fight. But the bill's framework — tiered obligations, independent audits, mandatory public disclosure — reflects where federal AI governance is converging. Even if GAAIA stalls, a successor bill will likely draw on the same architecture.

---

## Sponsors

**Jay Obernolte (R-CA)** holds a master's in artificial intelligence from UCLA (1997) and a bachelor's in engineering from Caltech — the only current Member of Congress with an advanced AI degree. He co-chaired the bipartisan House AI Task Force that produced the December 2024 AI policy roadmap and serves as vice-chair of the Congressional AI Caucus. He is also the owner and technical director of a video game development studio.

**Lori Trahan (D-MA)** has been active on technology policy and describes GAAIA as "the first serious bipartisan attempt to put real guardrails on frontier AI before the technology outpaces us." The bill is a significant political risk for her given the organized opposition from labor and civil society groups in her Massachusetts district.

Additional co-sponsors: Scott Franklin (R-FL), Suhas Subramanyam (D-VA), Erin Houchin (R-IN), Scott Peters (D-CA).

---

*The federal AI governance landscape is moving on two tracks simultaneously: executive action via EO 14365 (covered separately) and congressional legislation via GAAIA and related drafts. Builders operating at frontier scale need to track both. Builders below the $500M threshold need to track the state preemption outcome, which determines whether your state-level AI development compliance workload simplifies or stays fragmented.*
