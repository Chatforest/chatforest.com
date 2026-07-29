---
title: "The Great American AI Act: Federal Frontier Model Oversight, a 3-Year State Law Freeze, and What It Means for Builders"
date: 2026-06-06
sources_audited: 2026-07-29
description: "A 269-page bipartisan discussion draft released June 3–4, 2026 would regulate frontier AI developers, codify NIST's AI safety center, and freeze state AI development laws for three years. If your company makes under $500M/year, the core obligations don't apply to you — but the compliance landscape still changes."
og_description: "The Great American AI Act discussion draft: $500M revenue threshold, 24-hour incident reporting, semi-annual IVO audits, 3-year state law preemption on AI development. Builder's guide to what the Obernolte-Trahan bill actually says."
content_type: "Builder's Log"
categories: ["AI Policy", "Compliance", "Regulation"]
tags: ["ai-regulation", "federal-preemption", "great-american-ai-act", "gaaia", "frontier-ai", "caisi", "nist", "state-ai-laws", "compliance", "builder-guide", "obernolte", "trahan", "open-source", "incident-reporting"]
---

On June 3–4, 2026, Representatives Jay Obernolte (R-CA) and Lori Trahan (D-MA) [released a 269-page bipartisan discussion draft](https://obernolte.house.gov/media/press-releases/obernolte-trahan-release-discussion-draft-great-american-ai-act) called the Great American AI Act (GAAIA). [Roll Call](https://rollcall.com/2026/06/04/bipartisan-ai-draft-proposes-three-year-preemption-of-state-laws/) and [FedScoop](https://fedscoop.com/bipartisan-great-american-ai-act-draft-proposes-new-federal-ai-governance-framework/) both confirmed the June 4 release. It is not yet a formal bill — the sponsors are soliciting input before introducing it — but it signals where federal AI regulation is heading and what the compliance landscape could look like within the next twelve to twenty-four months.

The short version for most builders: **if your company makes under $500 million a year in gross revenue, the core obligations do not apply to you.** But the bill's state law preemption provision would simplify — and in some cases eliminate — the patchwork of state AI development requirements you are currently tracking.

---

## What the Bill Does

The GAAIA creates a federal framework for **frontier AI developers** built around four pillars: mandatory transparency, independent auditing, a new federal standards body, and a three-year freeze on state AI development laws.

### Who Is a "Frontier Developer"

The substantive obligations target **large frontier developers** — [defined in the discussion draft text](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/the-great-american-ai-act-discussion-draft-website-compressed-compressed.pdf) (Sec. 101(15)) as companies with more than **$500 million in gross revenue in the previous calendar year**. That threshold explicitly exempts the vast majority of AI startups, independent developers, and open-source projects from the reporting and audit requirements.

If your company crosses that threshold, the following apply. If it does not, the federal preemption of state development laws is still relevant to you, but the compliance machinery is not.

---

## The Four Core Obligations for Frontier Developers

### 1. Frontier AI Framework (Public Document)

Before or concurrent with deploying a new frontier model, large frontier developers must publish a [**Frontier AI Framework**](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/the-great-american-ai-act-discussion-draft-website-compressed-compressed.pdf) (Sec. 111) covering:

- Risk thresholds and assessment procedures for **catastrophic risk** — [defined in the draft text](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/the-great-american-ai-act-discussion-draft-website-compressed-compressed.pdf) (Sec. 101(6)) as a foreseeable and material risk of death or serious injury to more than **50 people**, or more than **$1 billion in property damage or loss**
- Cybersecurity of nonpublic model weights
- Internal and external deployment decision criteria
- How the developer responds to critical safety incidents
- How the developer manages catastrophic risk from the model's internal use, including risk from the model circumventing an oversight mechanism

The framework is a public document. This is closer to a structured disclosure requirement than a licensing regime — you publish your risk posture, not ask permission to deploy.

### 2. Pre-Deployment Reporting

[Before or simultaneously with any new frontier model deployment](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/gaaia-discussion-draft-section-by-section-website.pdf) (Sec. 111), developers must publish a report disclosing:

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

[Developers must file a report with CAISI](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/gaaia-discussion-draft-section-by-section-website.pdf) (Sec. 111):

| Incident Type | Reporting Window |
|--------------|-----------------|
| Critical safety incident | Within 15 days |
| Imminent risk of death or serious injury | Within **24 hours** |

The 24-hour window for imminent-risk incidents is aggressive. At frontier scale, this implies real-time safety monitoring infrastructure with defined escalation paths — not something that can be built after the fact.

### 4. Independent Verification Organizations (IVO Audits)

Frontier developers must retain an **Independent Verification Organization** — a third-party auditor licensed by the new Center for AI Standards and Innovation (CAISI) — to conduct [**semi-annual audits**](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/the-great-american-ai-act-discussion-draft-website-compressed-compressed.pdf) of compliance (Sec. 112(b): first audit within one year of enactment, then every six months). IVOs must have sufficient access to company materials and report findings to CAISI.

[Non-compliance penalties](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/gaaia-discussion-draft-section-by-section-website.pdf): up to **$1 million per day** while the violation continues (Sec. 111). Material misrepresentations trigger the same ceiling.

---

## The New Standards Body: CAISI

The bill codifies and expands the Center for AI Standards and Innovation within the Department of Commerce, currently housed at NIST. CAISI would be led by a Secretary-appointed Director and [authorized at **$100 million per year for fiscal years 2027–2029**](https://trahan.house.gov/uploadedfiles/2026.06.03_trahan_obernolte_ai_framework_faq.pdf) — an order of magnitude above its current ~$15 million appropriation, per Rep. Trahan's office.

[CAISI's responsibilities include](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/gaaia-discussion-draft-section-by-section-website.pdf):

- Developing voluntary guidelines, best practices, and standards for adversarial robustness, interpretability, supply chain threats, and model tampering
- Testing and evaluating frontier AI systems
- Administering the IVO certification and auditing regime
- Coordinating with federal agencies and international standards bodies
- Running AI security testbeds (in partnership with DOE and federal labs), including a public hackathon component

This is not a new agency — it is an expansion and codification of existing NIST infrastructure. That distinction matters for implementation speed. Commerce does not need to stand up something from scratch.

---

## State Law Preemption: The Three-Year Development Law Freeze

The most contested provision: [the bill would preempt state laws](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/the-great-american-ai-act-discussion-draft-website-compressed-compressed.pdf) "specifically targeting the **development**" of an AI model (Sec. 121), with a **three-year sunset**.

Key nuances matter here:

- Preemption covers **development** laws only — not **deployment** or **use** laws
- States retain full authority over AI employment discrimination, consumer protection, housing, and other use-focused legislation
- Laws of "general applicability" that touch AI indirectly are not preempted
- The three-year sunset means this reverts to the pre-bill state-by-state dynamic in 2029 unless Congress acts again

**California-specific effects:** Per [Rep. Trahan's office FAQ on the draft](https://trahan.house.gov/uploadedfiles/2026.06.03_trahan_obernolte_ai_framework_faq.pdf), [AB 2013](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013) (requiring model developers to publicly post training data summaries) and the development-stage watermarking portion of [SB 942](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB942) would be preempted.

**Colorado:** Already substantially changed — [Colorado SB 189, signed by Gov. Jared Polis on May 14, 2026](https://governorsoffice.colorado.gov/governor/news/governor-polis-signs-bills-law-making-colorado-even-better-place-do-business-breaking-down), repealed and replaced the Colorado AI Act, removing the duty of care, risk management programs, and impact assessments in favor of a lighter, disclosure-based framework centered on automated decision-making technology. By the time GAAIA would take effect, Colorado's landscape will already have shifted.

**Context for the three-year duration:** [The Senate struck a 10-year AI moratorium from the budget reconciliation bill (the One Big Beautiful Bill Act) in July 2025 by a 99-1 vote](https://www.commerce.senate.gov/2025/7/senate-strikes-ai-moratorium-from-budget-reconciliation-bill-in-overwhelming-99-1-vote/8415a728-fd1d-4269-98ac-101d1d0c71e0). Obernolte and Trahan are proposing a narrower scope (development only, not deployment) and a shorter timeframe (three years, not ten) in the wake of that rejection. Whether that narrowing is enough to survive Senate scrutiny is an open question.

---

## Open-Source Carve-Out and Funding

Open-source developers are explicitly outside the frontier developer obligations. [The bill goes further](https://obernolte.house.gov/sites/evo-subsites/obernolte.house.gov/files/evo-media-document/gaaia-discussion-draft-section-by-section-website.pdf) (Sec. 311): CISA, in consultation with CAISI, would be authorized to award grants to eligible maintainers of widely used, critical open-source software for security work — patching, maintenance, security audits. Large frontier developers would also be required to provide those maintainers with AI model access for cybersecurity purposes.

This is a notable structural choice — federal funds flowing to open-source AI security maintainers, not just creating compliance burdens for them.

---

## Current Status

The GAAIA is a **discussion draft**. It has not been formally introduced as a bill. There is no committee referral, no markup scheduled, and no stated timeline for formal introduction.

[The sponsors are soliciting input at: **GAAIA@mail.house.gov**](https://fedscoop.com/bipartisan-great-american-ai-act-draft-proposes-new-federal-ai-governance-framework/)

This is not window dressing — the 99-1 Senate vote against the 10-year moratorium gave both parties reason to tread carefully on federal preemption. Obernolte and Trahan appear to be genuinely road-testing the proposal before committing it to the legislative process.

---

## Opposition

The preemption provision drew immediate organized opposition:

- [**Public Citizen**](https://www.citizen.org/news/obernolte-trahan-bill-strips-states-authority-to-protect-consumers-workers-and-children/) called it "a disastrous proposal that Big Tech is celebrating," with AI governance counsel J.B. Branch arguing the bill leaves algorithmic discrimination, housing and employment discrimination, consumer fraud, youth mental health harms, AI companions, and deepfakes unaddressed.
- [**AFL-CIO**](https://aflcio.org/press/releases/afl-cio-statement-trahan-obernolte-ai-discussion-draft) issued a formal "hard no" statement opposing preemption of state authority to regulate AI development. [**American Federation of Teachers**](https://www.aft.org/press-release/union-leaders-urge-congress-reject-great-american-ai-act) President Randi Weingarten, in a joint statement with AFA-CWA President Sara Nelson, called the bill "a giveaway to the AI industry and a handful of trillion-dollar companies, at the expense of American workers."
- A [**coalition of 40+ civil society organizations**](https://techoversight.org/wp-content/uploads/2026/05/Final-No-AI-Preemption-Letter.pdf) publicly urged Trahan not to co-sponsor the preemption provision before the draft was released.
- [**Americans for Responsible Innovation**](https://ari.us/ari-launches-massachusetts-ad-campaign-urging-rep-trahan-to-oppose-preemption-of-state-ai-laws/) ran paid advertising in Massachusetts specifically targeting Trahan.
- A [**bipartisan group of more than 200 state lawmakers from 42 states**](https://ari.us/wp-content/uploads/2026/06/State-Lawmakers-Letter_-GAAIA-State-AI-Law-Preemption-6-16-26.pdf) signed a letter condemning federal preemption of state AI development laws.

Industry reception was more favorable in tone. [ITI](https://www.itic.org/news-events/news-releases/iti-reacts-to-the-great-american-ai-act) — via CEO Jason Oxman — welcomed the bill's codification of the National AI Research Resource (NAIRR) and its international AI-standards leadership provisions. [BSA](https://www.bsa.org/news-events/news/bsa-on-bipartisan-great-american-ai-act) called the draft "a credible and substantive effort" and said it "looks forward to sharing input on provisions related to model definitions, regulatory thresholds, and auditing and reporting requirements."

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

**Jay Obernolte (R-CA)** [holds an M.S. in artificial intelligence from UCLA and a B.S. in engineering and applied science from Caltech](https://obernolte.house.gov/about) — currently the only serving Member of Congress with a graduate-level degree in AI. He [co-chaired the bipartisan House AI Task Force](https://obernolte.house.gov/media/press-releases/house-bipartisan-task-force-artificial-intelligence-delivers-report), which released its policy-recommendation report in December 2024, and [serves as vice-chair of the Congressional AI Caucus](https://washingtonainetwork.com/2024/02/05/house-ai-caucus-vice-chair-rep-jay-obernolte-and-rep-kevin-mullin-address-deep-fakes-copyright-infringement-and-the-need-for-ai-legislation-in-new-podcast/). He is also [the owner of a video game development studio](https://obernolte.house.gov/about).

**Lori Trahan (D-MA)** has been active on technology policy and [told the Boston Globe](https://www.bostonglobe.com/2026/06/04/nation/lori-trahan-ai-regulation-bill/) that GAAIA is "the first serious bipartisan attempt to put real guardrails on frontier AI before the technology outpaces us." The bill is a significant political risk for her given the organized opposition from labor and civil society groups in her Massachusetts district.

Additional co-sponsors: [Scott Franklin (R-FL), Suhas Subramanyam (D-VA), Erin Houchin (R-IN), Scott Peters (D-CA)](https://obernolte.house.gov/media/press-releases/obernolte-trahan-release-discussion-draft-great-american-ai-act).

---

*The federal AI governance landscape is moving on two tracks simultaneously: executive action via EO 14365 (covered separately) and congressional legislation via GAAIA and related drafts. Builders operating at frontier scale need to track both. Builders below the $500M threshold need to track the state preemption outcome, which determines whether your state-level AI development compliance workload simplifies or stays fragmented.*
