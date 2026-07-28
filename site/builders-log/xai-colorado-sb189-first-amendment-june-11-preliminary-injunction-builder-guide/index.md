# xAI's First Amendment Gambit: What the June 11 Filing Could Do to Every State AI Law

> On or before June 11, xAI must file a preliminary injunction against Colorado's replacement AI disclosure law (SB 189). If the court grants it, that ruling could constitutionally invalidate AI transparency mandates across the country. Here's what builders need to understand.


On April 27, 2026, U.S. Magistrate Judge Cyrus Y. Chung of the U.S. District Court for the District of Colorado granted a joint motion by xAI and Colorado Attorney General Philip J. Weiser's office to stay enforcement of Colorado's AI Act (SB 24-205) while xAI's constitutional challenge proceeds. The U.S. Department of Justice, which had moved to intervene in the case three days earlier as plaintiff-intervenor, is now also a party. ([Minute order, No. 1:26-cv-01515-DDD-CYC](https://www.courtlistener.com/docket/73171074/x-ai-llc-v-weiser/) · [DOJ press release](https://www.justice.gov/opa/pr/justice-department-intervenes-xai-lawsuit-challenging-colorados-algorithmic-discrimination) · [HR Dive](https://www.hrdive.com/news/colorado-ai-bias-law-unconstitutional-elon-musks-xai/817258/) · [Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/de3ad9de/xai-sues-doj-intervenes-enforcement-of-colorado-ai-act-suspended))

That stay covered Colorado's original AI Act (SB 24-205), which was subsequently repealed and replaced by a narrower disclosure law, SB 189, signed by Governor Jared Polis on May 14, 2026. ([SB26-189, Colorado General Assembly](https://leg.colorado.gov/bills/sb26-189) · [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/05/colorado-governor-signs-sb-189)) The stay order set a condition: xAI must submit a preliminary injunction motion within 28 days after final adoption of any legislation replacing SB 24-205. That deadline falls on or around June 11, 2026. ([Minute order, No. 1:26-cv-01515-DDD-CYC](https://www.courtlistener.com/docket/73171074/x-ai-llc-v-weiser/) · [Bloomberg Law](https://news.bloomberglaw.com/daily-labor-report/colorado-ai-safeguards-law-halted-as-musks-xai-seeks-injunction))

xAI has given no indication it intends to drop the lawsuit.

---

## Two Laws, One Constitutional Theory

The original Colorado AI Act (SB 24-205), enacted in 2024, was the first comprehensive state law regulating the development and deployment of AI systems. It was a sprawling piece of regulation — risk assessments, algorithmic discrimination liability, mandatory impact assessments submitted to the Attorney General, bias audits, human review rights. Industry groups and the Trump administration argued it was too proscriptive, and it was repealed before taking effect — replaced, under litigation pressure and federal intervention, with something far lighter. ([Skadden](https://www.skadden.com/insights/publications/2026/06/colorado-repeals-and-replaces-its-ai-act))

SB 189, which takes effect January 1, 2027 ([bill text, SB26-189](https://leg.colorado.gov/bill_files/116489/download)), requires:

- **Deployers** to give consumers a "clear and conspicuous notice" when covered automated decision-making technology (ADMT) influences a consequential decision, and to provide a plain-language explanation within 30 days of an adverse outcome
- **Developers** to supply deployers with documentation of the ADMT: intended uses, known harmful uses, training data categories
- **Both parties** to retain records for three years

The algorithmic discrimination framework is gone. The bias audit mandate is gone. The AG submission requirement is gone.

What xAI still objects to: the mandatory notice and documentation requirements. Even as a disclosure law — even stripped of the anti-discrimination mandates — SB 189 compels companies to say things about their AI systems. That, xAI argues, is the constitutional problem.

---

## The First Amendment Theory

xAI's core argument, filed against the original law on April 9, 2026 ([Complaint, Case No. 1:26-cv-01515](https://www.courthousenews.com/wp-content/uploads/2026/04/grok-ai-bill-colorado-complaint.pdf)), rests on a single contested distinction in First Amendment doctrine: the difference between **commercial speech** and **private speech**.

**If AI disclosures are commercial speech**: Courts apply intermediate scrutiny under the *Zauderer* standard — the government must show the disclosure is reasonably related to a substantial government interest, is accurate, and is not unduly burdensome. Under this framework, disclosure requirements routinely survive. A court that views "we used AI in this decision" as a factual consumer disclosure would apply this test, and SB 189 would likely pass.

**If AI disclosures are private speech**: Courts apply strict scrutiny. The government must show the law is narrowly tailored to a compelling state interest, and it can rarely meet that bar. xAI argues that AI model design — including how it represents what its models do or don't do — is protected private speech, citing *303 Creative v. Elenis*, 600 U.S. 570 (2023) ([opinion](https://www.supremecourt.gov/opinions/22pdf/21-476_c185.pdf)). Under strict scrutiny, SB 189 would almost certainly fail.

This is not a settled question. Different circuits have applied different scrutiny levels to disclosure mandates in different commercial contexts. The closest precedent on AI specifically comes from California.

---

## The California Precedent That Cuts Against xAI

In a parallel case, xAI challenged California's AB 2013, which requires generative AI developers to publish public summaries of their training datasets. On March 4, 2026, U.S. District Judge Jesus G. Bernal denied xAI's preliminary injunction. ([Order, Case No. 2:25-cv-12295-JGB-SSCx](https://cdn.arstechnica.net/wp-content/uploads/2026/03/xAI-v-Bonta-Order-Denying-Preliminary-Injunction-3-4-26.pdf) · [CourtListener docket](https://www.courtlistener.com/docket/72086154/xai-llc-v-rob-bonta/))

Judge Bernal found AB 2013 likely regulates commercial speech and applied **Central Hudson intermediate scrutiny** rather than the stricter *Zauderer* standard xAI sought, concluding that xAI had shown only a "distinct possibility," not a likelihood, of success on the merits. The law stands, and xAI has appealed to the Ninth Circuit. (The case continues on the merits at the district court; enforcement is not stayed.) ([Order](https://cdn.arstechnica.net/wp-content/uploads/2026/03/xAI-v-Bonta-Order-Denying-Preliminary-Injunction-3-4-26.pdf))

If the Colorado court follows Judge Bernal's reasoning: SB 189's consumer notice and documentation requirements are factual commercial disclosures, intermediate scrutiny applies, and xAI's PI motion fails. SB 189 takes effect January 1, 2027.

If the Colorado court accepts xAI's private speech theory: strict scrutiny applies, and SB 189 — even as a transparency-only law — is likely unconstitutional. This would create a direct district court split with *xAI v. Bonta*, and set up expedited appellate review.

---

## Why the DOJ Intervention Matters

The Department of Justice's Complaint in Intervention, filed April 24, 2026, raises two claims against SB 24-205, both under the Equal Protection Clause of the Fourteenth Amendment: that the law compels developers and deployers to discriminate on the basis of race, sex, and religion to avoid disparate-impact liability, and that it unlawfully authorizes discrimination when done to "increase diversity." (The compelled-speech, First Amendment theory belongs to xAI's own complaint, not the DOJ's.) ([DOJ Complaint in Intervention](https://www.justice.gov/crt/media/1437846/dl) · [DOJ press release](https://www.justice.gov/opa/pr/justice-department-intervenes-xai-lawsuit-challenging-colorados-algorithmic-discrimination)) Legal commentators have called it the first time the DOJ has intervened in litigation challenging a state AI law. ([Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/de3ad9de/xai-sues-doj-intervenes-enforcement-of-colorado-ai-act-suspended)) The DOJ's complaint invokes Executive Order 14365, which directs federal agencies to identify and challenge "onerous" state AI laws. ([EO 14365, Federal Register](https://www.federalregister.gov/documents/2025/12/16/2025-23092/ensuring-a-national-policy-framework-for-artificial-intelligence))

The DOJ is expected to file a companion motion against SB 189 as well. This means the preliminary injunction motion against Colorado's disclosure law will carry the weight of the federal government's constitutional position.

A district court ruling here — either direction — will land differently than a two-party PI dispute. If the Colorado court and the California court reach opposite conclusions about the scrutiny level applicable to state AI disclosures, that circuit tension will likely reach the Tenth Circuit or Ninth Circuit within 18 months.

---

## What SB 189 Actually Requires of Builders (and Its Key Carve-Out)

Before assessing litigation risk, builders operating in or for Colorado consumers need to understand what SB 189 actually covers. ([Bill text, SB26-189](https://leg.colorado.gov/bill_files/116489/download))

**ADMT scope trigger**: Technology must (1) process personal data using computation to generate predictions, recommendations, classifications, rankings, or scores AND (2) "materially influence" a consequential decision. "Materially influence" means a non-de minimis factor affecting an outcome. The law is not triggered by AI tools that merely assist a human decision-maker without influencing the outcome.

**Covered domains**: Employment, education, financial services, insurance, healthcare, residential real estate, essential government services.

**The LLM carve-out**: Consumer-facing large language models are explicitly excluded from SB 189's ADMT definition *provided that*: (1) the tool is not marketed for use in consequential decision-making in the seven covered domains, and (2) the deployer maintains an acceptable use policy that prohibits such use.

This carve-out is meaningful. A general-purpose AI assistant, coding tool, or content generation product would fall outside SB 189 — as long as the builder does not market it for lending, hiring, or healthcare decisions, and publishes an acceptable use policy saying so.

**If you are in scope**: Deployers must build notification pipelines (point-of-interaction notice when ADMT influences a decision) and 30-day adverse decision explanation workflows. Developers must supply documentation. Both must retain records for three years. All of this must be operational by January 1, 2027 — unless stayed.

---

## Three Scenarios for Builders

**Scenario 1 — PI granted, SB 189 stayed**
The Colorado court accepts xAI's private speech argument and grants the preliminary injunction. SB 189 is suspended pending a ruling on the merits. Builders in Colorado's covered domains get more time. More importantly, the ruling creates constitutional uncertainty for comparable AI disclosure mandates other states have enacted, such as Connecticut's AI Responsibility and Transparency Act. ([DLA Piper](https://www.dlapiper.com/en-us/insights/publications/2026/05/unpacking-connecticuts-new-ai-law)) If the ruling survives on appeal, a cascade of stays across state AI disclosure laws becomes possible.

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
| April 9, 2026 | [xAI files suit](https://www.courthousenews.com/wp-content/uploads/2026/04/grok-ai-bill-colorado-complaint.pdf) against Colorado SB 24-205 |
| April 24, 2026 | [DOJ moves to intervene](https://www.justice.gov/opa/pr/justice-department-intervenes-xai-lawsuit-challenging-colorados-algorithmic-discrimination) with Equal Protection claims — reportedly [DOJ's first such intervention](https://www.nortonrosefulbright.com/en-us/knowledge/publications/de3ad9de/xai-sues-doj-intervenes-enforcement-of-colorado-ai-act-suspended) against a state AI law |
| April 27, 2026 | [Federal magistrate stays enforcement](https://www.courtlistener.com/docket/73171074/x-ai-llc-v-weiser/) of SB 24-205 |
| May 14, 2026 | [Governor Polis signs SB 189](https://leg.colorado.gov/bills/sb26-189) (replacement disclosure law) |
| June 11, 2026 | xAI/DOJ preliminary injunction filing deadline against SB 189 — deadline passed; no public reporting of a withdrawal |
| January 1, 2027 | [SB 189 effective date](https://leg.colorado.gov/bill_files/116489/download) (absent a court stay) |

---

## Context: Existing Coverage

This article covers the active litigation against SB 189. For the full history of how Colorado's original AI Act was written, contested, and repealed, see [America's First AI Law Is Dead](/reviews/colorado-ai-act-sb24-205-repeal-sb26-189-disclosure-framework-2026/).

For the federal layer — how EO 14365 directed the DOJ to challenge state AI laws, and what that means for builders across all states — see [The Federal-State AI Showdown](/builders-log/trump-ai-eo-federal-preemption-state-laws-compliance-builder-guide/).

