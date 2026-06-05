# Illinois Just Passed America's Strongest AI Safety Law. Here's What SB 315 Actually Requires.

> Illinois SB 315 passed 110-0 in the House and 52-5 in the Senate. Governor Pritzker will sign it. It's the first US law to mandate annual third-party safety audits of frontier AI companies — with penalties three times higher than California's. Here is what it actually requires.


On May 27, 2026, the Illinois House voted 110-0 to pass SB 315 — the Artificial Intelligence Safety Measures Act. The Senate had already cleared it 52-5 on May 21. Governor Pritzker has stated he will sign it. No veto, no delay, no fight. Bipartisan near-unanimity in a divided legislature.

This is a meaningfully different law from California's SB 53. California requires frontier developers to publish safety frameworks and report incidents. Illinois requires all of that, plus something no US state has done before: **mandatory annual third-party audits**, with penalties capped at $3 million per violation — three times California's ceiling.

The law does not take effect until January 1, 2028. But the auditing infrastructure it anticipates doesn't exist yet, the standards it references aren't written yet, and the labs that will be subject to it are going to spend the next 18 months figuring out what compliance actually looks like. Builders who use those labs' APIs — which is most of the industry — should understand what their providers are being asked to do.

---

## Who SB 315 Covers

SB 315 applies to **"large frontier developers"**: companies that **build or train** AI models above a frontier-scale compute threshold, with **annual gross revenues above $500 million** (including affiliates).

The revenue threshold is the same as California's SB 53. The compute threshold mirrors California's likely ~10^26 floating-point operations, though the Illinois bill text's exact FLOP threshold was not reproduced verbatim in public coverage as of this writing — the ILGA full text is the authoritative source.

Companies in scope: OpenAI, Anthropic, Google DeepMind, Meta, xAI, Microsoft's AI research division.

**SB 315 covers developers, not deployers.** The broader Illinois AI legislative package includes eight bills; SB 315 is the frontier-developer bill specifically. Separate Illinois bills address AI users, employers deploying AI for personnel decisions, and other actors in the AI supply chain. If you build on top of OpenAI or Anthropic APIs, SB 315 does not apply to you directly — it applies to them.

---

## What SB 315 Requires

### Requirement 1: A Published Frontier AI Framework

Every covered company must create, implement, publish, and annually update a **Frontier AI Framework** that documents how they assess and mitigate catastrophic risks. The framework must address:

- How they measure model capabilities and the probability of catastrophic risk
- How they apply industry standards
- How they identify and respond to safety incidents
- Risk mitigations and safety controls in place
- Governance structures
- Cybersecurity practices
- Third-party evaluation processes already conducted
- Internal-use risk assessments

This requirement parallels California SB 53's framework mandate. Most of the major labs already publish something like this — OpenAI's Frontier Governance Framework (published May 28, explicitly mapping to SB 53) and Anthropic's Responsible Scaling Policy are examples of voluntary frameworks that now become statutory baselines.

### Requirement 2: Annual Third-Party Safety Audits

This is the element no US state has previously required. SB 315 mandates that covered companies **annually retain an independent third-party auditor** to verify compliance with their safety practices.

The audit must be conducted according to "generally accepted auditing standards and best practices." The law establishes access, reporting, retention, and publication requirements for audit results.

Who is likely to perform these audits: Big Four accounting firms (Deloitte, EY, KPMG, PwC) and specialized AI evaluation organizations such as METR, Transluce, and AVERI.

Here is the important caveat for builders tracking this: **no standardized framework for frontier model safety audits currently exists in the United States.** No NIST standard, no AICPA attestation standard, no ISO/IEC specification defines what a frontier AI safety audit entails. The bill requires audits by reference to standards that have not been written. The likely outcome is an 18-month industry-driven effort to define those standards before the 2028 enforcement date, potentially through NIST AI RMF extensions or a new auditing practice developed by the Big Four.

NetChoice (a tech industry trade group that opposed the bill) flagged this as a "fatal flaw" — you cannot comply with requirements that are undefined. Supporters of the bill argue this is intentional: the law creates the audit mandate, and industry and regulators will work out the implementation details. Anthropic and OpenAI both supported the bill despite this ambiguity.

### Requirement 3: Incident Reporting

Two-tier reporting requirement:

- **72 hours** from discovery of a "critical safety incident"
- **24 hours** from discovery of any incident posing an "imminent risk of death or serious physical harm"

For comparison, California SB 53 uses 15 days for most incidents and 24 hours for imminent harm. Illinois's 72-hour window for standard incidents is significantly tighter.

The bill does not define "critical safety incident" with precision, which is the same definitional gap identified in California's law. For reference, California's version defines reportable incidents as: unauthorized tampering causing serious harm, materialization of catastrophic risk, loss of model control resulting in injury or property damage, or deliberate evasion of safeguards. Illinois's definition is expected to align closely.

The catastrophic risk threshold in SB 315 covers models capable of mass harm or creating damages totaling more than $1 billion through cyberattacks or malfunction beyond human control.

### Requirement 4: Periodic Internal-Use Risk Assessment Summaries

Separate from the external audit, covered companies must submit **periodic summaries of their internal-use risk assessments** to the appropriate state authority. This creates a reporting cadence distinct from incident reporting — it is a regular accountability window, not just a break-glass requirement.

---

## Penalties

Civil penalties up to **$3 million per violation**, enforced exclusively by the **Illinois Attorney General**. No private right of action. If you're a competitor or a user harmed by a lab's non-compliance, you cannot sue — only the AG can enforce.

The $3 million cap is three times California SB 53's $1 million ceiling. Whether "per violation" is counted per incident, per day of non-compliance, or per requirement type is not specified in the available public summary of the bill text.

---

## Why OpenAI and Anthropic Supported It

Both major frontier labs publicly endorsed SB 315. This is not unusual — Anthropic and OpenAI supported California SB 53 as well — but it is worth understanding why.

**Anthropic** (Cesar Fernandez): *"SB 315 takes the safety practices leading labs already follow voluntarily — publishing a safety framework, transparent reporting, protecting whistleblowers — and helps establish a baseline that every leading AI developer is expected to meet."*

**OpenAI** (spokesperson Jamie Radice): *"The Illinois General Assembly has shown real bipartisan leadership in advancing SB 315 and developing a thoughtful framework for frontier AI safety. Clear expectations around safety, transparency, incident reporting, and accountability matter."*

The strategic logic: Anthropic and OpenAI already do these things. Codifying them into law raises the compliance floor for well-funded competitors and new entrants who don't have established safety programs. It also creates a public record of commitments — their own frameworks become legally documented baselines they can be held to, which is a form of accountability they've explicitly asked for.

---

## SB 315 vs. California SB 53: The Key Differences

| | California SB 53 | Illinois SB 315 |
|---|---|---|
| Revenue threshold | $500M+ | $500M+ |
| Mandatory 3rd-party audit | **No** (removed from SB 1047) | **Yes — annual** |
| Standard incident reporting window | 15 days | **72 hours** |
| Imminent harm reporting window | 24 hours | 24 hours |
| Max penalty per violation | $1 million | **$3 million** |
| In effect | Already (2025) | January 1, 2028 |
| Enforcement | California AG | Illinois AG |
| Private right of action | No | No |

California's law is already in effect. Illinois's is the more demanding law but doesn't take effect for 18 months.

---

## What This Means for Builders

**If you train or deploy your own frontier models above the revenue threshold:** SB 315 applies to you. Start mapping your existing safety practices against the framework requirements now. The 18-month runway is shorter than it sounds — annual audit processes take months to design and execute, and the auditing standards you'll need to comply with don't exist yet. Engaging with the audit-standards development process (NIST, Big Four, AI evaluation orgs) now is not optional if you want to be audit-ready in 2028.

**If you build on top of frontier APIs (most builders):** SB 315 doesn't apply to you directly, but it will shape what your providers publish. Starting in 2028, every major lab's Frontier AI Framework becomes a legally mandated, annually audited document — not a voluntary marketing artifact. When you evaluate model providers, their compliance posture will be a concrete, attestable factor rather than a policy-page promise.

**On the audit-standards gap:** The most significant open question from this law is not the regulation itself — it is what "frontier AI safety audit" will come to mean in practice. The industry has 18 months to answer that. Watch NIST, watch the Big Four's emerging AI practice groups, watch METR and AVERI. Whoever defines the audit methodology in that window will define what compliance looks like for this entire category of law.

**On state patchwork:** Illinois and California now both have frontier model safety laws. Connecticut and New York passed related AI bills in the same May 2026 legislative window (IAPP reports). The pattern is: no federal standard, so states act. The 50-state patchwork risk that lobbying groups have warned about is no longer hypothetical. If you build at scale across the US, this is a multi-jurisdiction compliance problem, not a single-state one.

---

*ChatForest previously covered California's AI regulatory stack in [California AI Regulation, May 2026](/builders-log/california-ai-regulation-2026-crossover-builder-compliance-guide/). For the federal side, watch DC — no preemption bill has moved in the current Congress.*

