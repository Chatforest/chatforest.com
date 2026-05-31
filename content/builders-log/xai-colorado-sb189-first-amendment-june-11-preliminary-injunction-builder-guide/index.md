---
title: "xAI's First Amendment Gambit: What the June 11 Filing Could Do to Every State AI Law"
date: 2026-06-01
description: "On or before June 11, xAI must file a preliminary injunction against Colorado's replacement AI disclosure law (SB 189). If the court grants it, that ruling could constitutionally invalidate AI transparency mandates across the country. Here's what builders need to understand."
og_description: "xAI's June 11 PI filing against Colorado SB 189 sets up a constitutional test: can states require AI disclosure at all? Builder guide to the litigation, the legal theory, and what each outcome means for compliance."
content_type: "Builder's Log"
categories: ["AI Policy", "Regulation", "Legal"]
tags: ["xai", "colorado", "ai-policy", "regulation", "first-amendment", "sb-189", "litigation", "compliance", "admt", "builder-guide"]
---

On April 27, 2026, a federal magistrate judge issued a court order that had never been issued before: a stay of enforcement of a U.S. state AI law, at the joint request of a private company and the U.S. Department of Justice.

That stay covered Colorado's original AI Act (SB 24-205), which was subsequently repealed and replaced by a narrower disclosure law, SB 189, on May 14. The stay order included a condition: xAI must file a new preliminary injunction motion against any replacement legislation within 28 days. That deadline falls on or around June 11, 2026.

xAI has given no indication it intends to drop the lawsuit.

---

## Two Laws, One Constitutional Theory

The original Colorado AI Act was a sprawling piece of regulation — risk assessments, algorithmic discrimination liability, mandatory impact assessments submitted to the Attorney General, bias audits, human review rights. Industry called it the most burdensome AI law in the U.S. It was replaced, under litigation pressure and federal intervention, with something far lighter.

SB 189, which takes effect January 1, 2027, requires:

- **Deployers** to give consumers a "clear and conspicuous notice" when covered automated decision-making technology (ADMT) influences a consequential decision, and to provide a plain-language explanation within 30 days of an adverse outcome
- **Developers** to supply deployers with documentation of the ADMT: intended uses, known harmful uses, training data categories
- **Both parties** to retain records for three years

The algorithmic discrimination framework is gone. The bias audit mandate is gone. The AG submission requirement is gone.

What xAI still objects to: the mandatory notice and documentation requirements. Even as a disclosure law — even stripped of the anti-discrimination mandates — SB 189 compels companies to say things about their AI systems. That, xAI argues, is the constitutional problem.

---

## The First Amendment Theory

xAI's core argument, filed against the original law on April 9, 2026, rests on a single contested distinction in First Amendment doctrine: the difference between **commercial speech** and **private speech**.

**If AI disclosures are commercial speech**: Courts apply intermediate scrutiny under the *Zauderer* standard — the government must show the disclosure is reasonably related to a substantial government interest, is accurate, and is not unduly burdensome. Under this framework, disclosure requirements routinely survive. A court that views "we used AI in this decision" as a factual consumer disclosure would apply this test, and SB 189 would likely pass.

**If AI disclosures are private speech**: Courts apply strict scrutiny. The government must show the law is narrowly tailored to a compelling state interest, and it can rarely meet that bar. xAI argues that AI model design — including how it represents what its models do or don't do — is protected private speech, citing *303 Creative v. Elenis* (2023). Under strict scrutiny, SB 189 would almost certainly fail.

This is not a settled question. Different circuits have applied different scrutiny levels to disclosure mandates in different commercial contexts. The closest precedent on AI specifically comes from California.

---

## The California Precedent That Cuts Against xAI

In a parallel case, xAI challenged California's AB 2013, which requires generative AI developers to publish public summaries of their training datasets. On March 4–5, 2026, U.S. District Judge Jesus Bernal denied xAI's preliminary injunction.

Judge Bernal applied **Central Hudson intermediate scrutiny** — commercial speech — and found that xAI had not shown a likelihood of success on the merits. The training data disclosures were factual and non-controversial. The law stands. (The case continues on the merits, but enforcement is not stayed.)

If the Colorado court follows Judge Bernal's reasoning: SB 189's consumer notice and documentation requirements are factual commercial disclosures, intermediate scrutiny applies, and xAI's PI motion fails. SB 189 takes effect January 1, 2027.

If the Colorado court accepts xAI's private speech theory: strict scrutiny applies, and SB 189 — even as a transparency-only law — is likely unconstitutional. This would create a direct district court split with *xAI v. Bonta*, and set up expedited appellate review.

---

## Why the DOJ Intervention Matters

The Department of Justice filing on April 24, 2026 — independently raising compelled speech and equal protection claims against the original Colorado law — was the first time the federal government had intervened to invalidate a state AI law. The DOJ's brief drew on EO 14365's direction to challenge state laws that create "onerous" AI regulation.

The DOJ is expected to file a companion motion against SB 189 as well. This means the preliminary injunction motion against Colorado's disclosure law will carry the weight of the federal government's constitutional position.

A district court ruling here — either direction — will land differently than a two-party PI dispute. If the Colorado court and the California court reach opposite conclusions about the scrutiny level applicable to state AI disclosures, that circuit tension will likely reach the Tenth Circuit or Ninth Circuit within 18 months.

---

## What SB 189 Actually Requires of Builders (and Its Key Carve-Out)

Before assessing litigation risk, builders operating in or for Colorado consumers need to understand what SB 189 actually covers.

**ADMT scope trigger**: Technology must (1) process personal data using computation to generate predictions, recommendations, classifications, rankings, or scores AND (2) "materially influence" a consequential decision. "Materially influence" means a non-de minimis factor affecting an outcome. The law is not triggered by AI tools that merely assist a human decision-maker without influencing the outcome.

**Covered domains**: Employment, education, financial services, insurance, healthcare, residential real estate, essential government services.

**The LLM carve-out**: Consumer-facing large language models are explicitly excluded from SB 189's ADMT definition *provided that*: (1) the tool is not marketed for use in consequential decision-making in the seven covered domains, and (2) the deployer maintains an acceptable use policy that prohibits such use.

This carve-out is meaningful. A general-purpose AI assistant, coding tool, or content generation product would fall outside SB 189 — as long as the builder does not market it for lending, hiring, or healthcare decisions, and publishes an acceptable use policy saying so.

**If you are in scope**: Deployers must build notification pipelines (point-of-interaction notice when ADMT influences a decision) and 30-day adverse decision explanation workflows. Developers must supply documentation. Both must retain records for three years. All of this must be operational by January 1, 2027 — unless stayed.

---

## Three Scenarios for Builders

**Scenario 1 — PI granted, SB 189 stayed**
The Colorado court accepts xAI's private speech argument and grants the preliminary injunction. SB 189 is suspended pending a ruling on the merits. Builders in Colorado's covered domains get more time. More importantly, the ruling creates constitutional uncertainty for comparable disclosure mandates in Connecticut (AIRT Act), Texas, and other states that have modeled disclosure requirements on the Colorado framework. If the ruling survives on appeal, a cascade of stays across state AI disclosure laws becomes possible.

**Scenario 2 — PI denied, SB 189 stands**
The Colorado court follows the California district court and applies intermediate scrutiny. SB 189 stands. Builders in covered domains must build toward January 1, 2027 compliance. The litigation continues on the merits, but enforcement isn't stayed. District court split is possible if the Colorado ruling is inconsistent with Judge Bernal's logic — which could accelerate appellate review. Either way: start building.

**Scenario 3 — xAI drops the suit or settles**
xAI and the State of Colorado reach a resolution that narrows SB 189 further or clarifies enforcement scope. This is the least likely scenario based on available reporting, but settlement has happened in other state AI litigation. Result: modified compliance requirements, faster regulatory clarity.

---

## What Builders Should Do Right Now

**1. Determine whether SB 189 applies to you.**
Map your AI products against SB 189's ADMT definition. Is your tool processing personal data to generate predictions, recommendations, or classifications? Is it influencing consequential decisions in any of the seven covered domains? If yes to both: you are in scope.

**2. If you are a general-purpose AI tool, document your carve-out.**
Draft an acceptable use policy that explicitly prohibits use of your tool for consequential decisions in the seven covered domains. Keep records that you did not market the tool for those uses. This is your safe harbor under SB 189.

**3. Do not wait for the June 11 ruling to start compliance planning.**
Scenario 2 is not worse than Scenario 1 — it just requires you to have built compliance infrastructure. The January 1, 2027 effective date gives you seven months. That is enough time if you start now; it is not enough time if you start in October.

**4. Watch what happens in the Tenth Circuit.**
The *xAI v. Colorado* appellate posture will establish the legal standard for AI disclosure mandates in the western U.S. The *xAI v. Bonta* California case will run in parallel through the Ninth Circuit. The resolution of the commercial-vs.-private speech question in those two circuits will determine whether state AI disclosure laws are constitutionally viable as a category.

**5. Read the acceptable use policy of every AI vendor you use for consequential decisions.**
If you are a deployer using third-party AI tools for employment, lending, or healthcare decisions, SB 189 places disclosure obligations on you — not just the AI developer. Make sure your vendor's documentation requirements are met and that you have contractual rights to that documentation.

---

## Timeline Reference

| Date | Event |
|---|---|
| April 9, 2026 | xAI files suit against Colorado SB 24-205 |
| April 24, 2026 | DOJ intervenes; first federal action to block a state AI law |
| April 27, 2026 | Federal magistrate stays enforcement of SB 24-205 |
| May 14, 2026 | Governor Polis signs SB 189 (replacement disclosure law) |
| ~June 11, 2026 | xAI/DOJ preliminary injunction filing deadline against SB 189 |
| January 1, 2027 | SB 189 effective date (absent a court stay) |

---

## Context: Existing Coverage

This article covers the active litigation against SB 189. For the full history of how Colorado's original AI Act was written, contested, and repealed, see [America's First AI Law Is Dead](/reviews/colorado-ai-act-sb24-205-repeal-sb26-189-disclosure-framework-2026/).

For the federal layer — how EO 14365 directed the DOJ to challenge state AI laws, and what that means for builders across all states — see [The Federal-State AI Showdown](/builders-log/trump-ai-eo-federal-preemption-state-laws-compliance-builder-guide/).
