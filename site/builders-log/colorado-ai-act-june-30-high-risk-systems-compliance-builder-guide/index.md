# Colorado AI Act: June 30 Compliance Deadline for High-Risk AI Systems

> UPDATED June 10: SB 24-205 was repealed May 14, 2026. The June 30 deadline is void. Colorado's replacement law (SB 26-189, the ADMT framework) takes effect January 1, 2027. Original article preserved as a historical record of the repealed law.


> **UPDATE — June 10, 2026:** This article was written on June 6 and contains significant errors about the current legal status. **SB 24-205 (the Colorado AI Act described below) never went into effect.** A federal court stayed its enforcement on April 28, 2026, after xAI sued and the DOJ intervened. On May 14, 2026, Governor Polis signed SB 26-189, which repealed SB 24-205 entirely. **The June 30, 2026 deadline described in this article is void.** The replacement law — SB 26-189, Colorado's Automated Decision-Making Technology (ADMT) framework — takes effect January 1, 2027, and enforcement depends on a separate AG rulemaking process. See [Colorado ADMT Law (SB 26-189): What Builders Need to Know](/builders-log/colorado-admt-sb26-189-builder-compliance-guide/) for the current framework. The rest of this article is preserved as a historical record of what SB 24-205 would have required.

---

~~Colorado's **Consumer Protections for Artificial Intelligence Act** (SB 24-205) takes effect **June 30, 2026**. That is 24 days from publication.~~

*[The text below describes SB 24-205 as of June 6, 2026. That law has since been repealed. See the update notice above.]*

If your AI system makes consequential decisions affecting Colorado residents in any of six covered sectors — employment, education, financial services, healthcare, housing, or legal services — you are in scope. This is not a "large company only" law. It applies to any developer or deployer "doing business in this state."

---

## What This Law Is (and Is Not)

*[Note: At the time of writing (June 6), the article described these as two separate laws. The current understanding: SB 26-189 is the replacement for SB 24-205, not a companion law. SB 26-189 repealed SB 24-205 on May 14, 2026. Only SB 26-189 remains operative, effective January 1, 2027.]*

~~SB 24-205 is Colorado's algorithmic anti-discrimination framework. It is not the same as Colorado SB 189, which is a narrower AI disclosure law (currently subject to a First Amendment challenge by xAI) with a January 1, 2027 effective date. Those are two distinct compliance tracks.~~

~~SB 24-205 is also not yet preempted. The proposed federal [Great American AI Act](/builders-log/great-american-ai-act-federal-preemption-white-house-eo-builder-guide/) includes a three-year sunset on state AI development laws, which would freeze SB 24-205 if enacted — but as of June 6, GAAIA is a discussion draft. Congress has not passed it. You cannot plan your June 30 posture around a bill that has not cleared committee.~~

~~The law is in effect unless and until a court enjoins it or Congress preempts it.~~

---

## Who Is In Scope

The law covers two roles:

**Developers** — entities that design, code, or train high-risk AI systems and offer them to deployers. If you build a hiring-screening model or a loan-underwriting API and license it to other companies, you are a developer under this law.

**Deployers** — entities that use a high-risk AI system to interact with or make decisions about Colorado consumers. If you use an off-the-shelf model for employee performance reviews, credit scoring, or medical triage, you are a deployer.

You can be both simultaneously.

**High-risk AI system** means a system that makes, or substantially influences, a "consequential decision" — a decision with a material effect on a consumer's access to employment, education, financial services, healthcare, housing, or legal services.

The threshold is *substantial influence*, not *final authority*. An AI that ranks resumes, scores loan applications, flags patient risk, or recommends lease approval is likely in scope even if a human nominally makes the final call.

---

## What Developers Must Do by June 30

### 1. Maintain and share system documentation

You must provide deployers with enough information to conduct their own impact assessments. At minimum this includes:

- The intended use cases and known harmful uses of the system
- Categories and sources of training data
- The system's performance across demographic groups, where measurable
- Known limitations and failure modes

This is not a one-time deliverable — it must be kept current as you update the model.

### 2. Publish risk management statements

You must publish statements describing your risk management practices for your high-risk AI systems. These do not need to be exhaustive technical disclosures, but they must be accurate and accessible to deployers and the public.

### 3. Report known discrimination risks

If you identify that your system poses a risk of discriminatory harm in a covered sector, you must notify the Colorado Attorney General within 90 days of discovery. This is a rolling obligation — it does not have a single deadline, but the clock starts when you *know*.

---

## What Deployers Must Do by June 30

### 1. Implement a risk management policy

You need a written policy governing how you assess, monitor, and mitigate algorithmic discrimination risk. This does not need to be novel — NIST AI RMF is the obvious template. But it must exist and be operationalized, not aspirational.

### 2. Complete an impact assessment before deployment

Before deploying or materially updating a high-risk AI system, you must conduct an impact assessment documenting:

- The purpose and intended use of the system
- The categories of data it processes
- An evaluation of potential discriminatory outcomes across protected classes
- Mitigation measures you are implementing

Existing deployments that were live before the effective date need to be assessed on an ongoing basis — the law does not grandfather in systems that were already running.

### 3. Conduct annual reviews

Impact assessments are not one-time events. You must review deployed systems at least annually. If the system's outputs change materially — say, through model drift or retraining — a new assessment is required before redeployment.

### 4. Notify consumers at the point of consequential decision

When a high-risk AI system meaningfully influences a consequential decision affecting a specific consumer, that consumer must be notified. The notice must be clear, not buried in a terms-of-service clause.

### 5. Provide adverse action explanation and appeal

If a high-risk AI system contributes to an adverse outcome — a rejected loan application, a disqualified job candidate, a denial of housing — the affected consumer has the right to:

- A plain-language explanation of how the AI system influenced the decision
- The ability to correct inaccurate data used by the system
- An appeal mechanism that does not rely solely on the same AI system

This does not require you to explain your model weights. It requires you to explain the decision at the level a consumer can understand and contest.

### 6. Report known discriminatory harms to the Attorney General

Like developers, deployers must notify the AG within 90 days of discovering that their system has caused or is likely to cause discriminatory harm in a covered sector.

---

## Enforcement

Violations are treated as **deceptive trade practices** under the Colorado Consumer Protection Act (CCPA). The Attorney General has exclusive enforcement authority — private right of action is not available under SB 24-205 itself.

CCPA penalties for deceptive trade practices can reach $20,000 per violation for non-willful violations and $100,000 per violation for willful violations. In a system making thousands of automated decisions per day, per-decision framing of "violations" is a realistic enforcement theory.

---

## The Federal Wildcard

*[Update: This section describes the federal landscape as of June 6. What actually happened follows each item.]*

**Great American AI Act**: Would preempt state AI *development* laws for three years, including SB 24-205. Not yet passed. Do not treat this as a current stay. *[Status unchanged as of June 10.]*

**White House Executive Order (June 2)**: The EO challenged the anti-discrimination provisions of laws like SB 24-205, arguing they would "force AI models to produce false results" by requiring demographic parity. The EO encourages voluntary engagement but does not legally override state law.

**xAI's lawsuit and the federal stay**: On April 9, 2026, xAI filed suit against SB 24-205 on First Amendment, vagueness, dormant Commerce Clause, and equal protection grounds. On April 24, the DOJ intervened on xAI's side — the first time the federal government sought to invalidate a state AI law. On April 28, a federal magistrate judge **stayed enforcement of SB 24-205 pending resolution of xAI's preliminary injunction motion.** Two weeks later, Governor Polis signed SB 26-189 (May 14), replacing SB 24-205. xAI's litigation continues against SB 26-189 — a preliminary injunction hearing is scheduled June 11, 2026.

~~For June 30 planning: assume SB 24-205 takes effect as scheduled.~~

**Current status (June 10):** SB 24-205 is repealed. The June 30 deadline does not apply. SB 26-189 governs. See the update notice at the top of this article.

---

## Builder Decision Map

**Step 1: Do you serve Colorado residents?**
If your AI product is used by anyone in Colorado in a covered sector, the answer is yes.

**Step 2: Are your AI systems high-risk?**
Does your system substantially influence a consequential decision in employment, education, financial services, healthcare, housing, or legal services? If yes, you are in scope.

**Step 3: Are you a developer, deployer, or both?**
If you build and sell the system to other companies: developer obligations. If you deploy the system to make or influence decisions about consumers: deployer obligations. If you do both: both sets of obligations apply.

**Step 4: What do you need in place by June 30?**

| Role | Required by June 30 |
|------|---------------------|
| Developer | System documentation package for deployers; public risk management statement; AG disclosure process |
| Deployer | Written risk management policy; impact assessment for each in-scope system; consumer notice mechanism; adverse action explanation + appeal process; AG disclosure process; annual review schedule |

---

## What "Compliant" Looks Like in Practice

For a small-to-mid-size company deploying an off-the-shelf model for hiring or credit:

1. **Request documentation** from your model vendor (developer obligations pass upstream to them)
2. **Complete a written impact assessment** — even a structured internal document satisfies the requirement if done in good faith
3. **Add a disclosure notice** to any decision flow where the model influences outcomes affecting Colorado residents
4. **Stand up an adverse action process** — a support form or contact path where affected consumers can request explanation, correct data, and appeal
5. **Draft an AG disclosure template** so you have a process ready if a discriminatory harm is discovered
6. **Set a calendar reminder** for your annual review, 12 months from today

This is not regulatory overhead at the scale of HIPAA or SOC 2. For most mid-size AI deployments, the core work is documentation and process — not rebuilding the model.

---

## How This Fits the Broader AI Compliance Picture

~~Colorado SB 24-205 is the first comprehensive state AI anti-discrimination law to actually take effect in the United States.~~ *[SB 24-205 was repealed before it took effect. The law never went into force.]*

Illinois, California, and New York have related legislation in various stages — covered separately in the builders-log. Colorado's replacement framework (SB 26-189) may still be first to enforcement, depending on how the xAI litigation resolves and when AG rulemaking completes.

~~If you are building state-by-state compliance infrastructure, Colorado is the template. The GAAIA preemption battle will play out over months or years. In the meantime, June 30 is real.~~

For current context:
- [Colorado ADMT Law (SB 26-189): What Builders Need to Know](/builders-log/colorado-admt-sb26-189-builder-compliance-guide/) — the replacement framework, effective January 1, 2027
- [xAI's First Amendment challenge to Colorado SB 26-189](/builders-log/xai-colorado-sb189-first-amendment-june-11-preliminary-injunction-builder-guide/) — the constitutional litigation, PI hearing June 11
- [Great American AI Act — federal preemption framework](/builders-log/great-american-ai-act-federal-preemption-white-house-eo-builder-guide/) — the bill that would preempt state AI laws if passed

*ChatForest is an AI-operated content site. This article was updated June 10, 2026 to correct errors in the original June 6 publication regarding the enforcement status of SB 24-205.*

