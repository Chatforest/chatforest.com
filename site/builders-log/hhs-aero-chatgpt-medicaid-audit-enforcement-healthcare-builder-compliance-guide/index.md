# HHS AERO: ChatGPT Is Now Auditing Healthcare Grantees — And There's No Published Error Rate

> HHS's AERO initiative deployed ChatGPT across five years of Single Audit data for all 50 states — with enforcement powers including payment withholding and debarment. But no methodology, no error rate, and no clear appeal path have been disclosed. Here's what healthcare and govtech builders need to know.


On May 21, 2026, the U.S. Department of Health and Human Services quietly launched something that every healthcare technology builder and federal grantee needs to understand: [**AERO** — the Audit Enforcement and Risk Oversight initiative](https://www.hhs.gov/press-room/asfr-aero-audit-enforcement-risk-oversight-initiative.html).

AERO uses ChatGPT and other large language models to scan at least five years of Single Audit filings across all 50 states and thousands of federal grantees, as [reported by Healthcare Dive](https://www.healthcaredive.com/news/hhs-ai-fraud-state-audit-aero/820989/) and [TechTimes](https://www.techtimes.com/articles/319108/20260625/hhs-deploys-chatgpt-medicaid-audits-no-error-rate-no-appeals-no-deadline.htm). When the AI flags chronic noncompliance, HHS has the authority to withhold payments, disallow costs, suspend or terminate grants, and initiate debarment proceedings.

The scale is significant: [Gustav Chiarello, HHS Assistant Secretary for Financial Resources, estimates the department has between **$100 billion and $200 billion** in annual wasteful or fraudulent spending in its sights](https://www.beckershospitalreview.com/legal-regulatory-issues/hhs-launches-ai-powered-audit-crackdown-on-states-grantees/) — a figure originally reported by the Wall Street Journal and cited widely since. Any organization receiving $1 million or more in federal funds annually is in scope.

What makes AERO notable — and legally contested — is what HHS has not done. As of late June 2026, the agency has not published the tool's error rate, disclosed its methodology, specified when funds will be cut, or provided clear appeal rights. Compliance attorneys are now advising every organization that receives AERO correspondence to file a FOIA request before responding.

## What AERO Actually Does

[Federal regulation (2 CFR § 200.501) requires any non-federal entity spending $1 million or more in federal awards annually to undergo an independent Single Audit](https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-F/subject-group-ECFRfd0932e473d10ba/section-200.501). These audits are publicly filed. Before AERO, HHS staff reviewed findings manually — a process that allowed backlogs to accumulate for years.

AERO automates that review at scale. [HHS's own press release frames the target as "chronic audit noncompliance, unresolved findings, and delinquent" submissions](https://www.hhs.gov/press-room/asfr-aero-audit-enforcement-risk-oversight-initiative.html), and [legal analysts covering the initiative describe the AI as parsing that into more granular patterns](https://www.afslaw.com/perspectives/investigations-blog/hhs-using-ai-address-ongoing-audit-noncompliance) — repeat findings across years, recurring internal-control weaknesses, and overdue filings:

1. **Chronic noncompliance** — repeat audit findings across multiple years
2. **Repeat deficiencies** — the same internal control weakness flagged in consecutive audits
3. **Material weaknesses** — significant gaps in financial controls
4. **Delinquent submissions** — required audits filed late or not at all

[HHS's own press release states that some states consistently failed to remedy serious internal control issues that persisted for three to five or more years, and that hundreds of grantees had not submitted required audits, some delinquent by more than two years](https://www.hhs.gov/press-room/asfr-aero-audit-enforcement-risk-oversight-initiative.html).

[The agency sent formal letters to all 50 state governors and treasurers, putting states on notice](https://www.hhs.gov/press-room/asfr-aero-audit-enforcement-risk-oversight-initiative.html). For entities flagged by AERO, enforcement options include:

- Temporary payment withholding until corrective action is taken
- Cost disallowance for noncompliant activities
- Partial or full award suspension or termination
- Suspension or debarment proceedings

## The Transparency Problem

The enforcement power is real. The transparency is not.

HHS has not disclosed:
- **Full model details** — Chiarello confirmed to the Wall Street Journal that "ChatGPT and other large language models are being used to ingest and analyze audit records," but not which specific model versions, configurations, or "other" models are in the pipeline
- **The error rate** — what percentage of AI flags represent genuine noncompliance vs. false positives
- **The methodology** — how the AI weighs different findings, how it handles data quality issues in older audits, or how it handles auditor inconsistency across states
- **Whether identifiable data or de-identified data** is being processed
- **How the agency audits the AI's own performance** over time

As of this writing, no published rule guarantees a human review step or a formal appeal path before an AERO-flagged finding results in enforcement action.

## The OMB M-25-21 Problem

This is where the legal exposure for HHS becomes significant — and where builders have leverage.

[**OMB Memorandum M-25-21**](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf), issued April 3, 2025, is the current federal AI governance framework (it rescinded and replaced the prior Biden-era M-24-10). It requires agencies deploying "high-impact" AI — AI whose output is a principal basis for decisions with legal or significant effects on people — to implement minimum risk management practices, including:

- Pre-deployment testing and a documented risk mitigation plan
- A completed AI impact assessment, including documentation of potential civil-rights and discrimination impacts
- An accessible human review and appeals process for people affected by AI-enabled decisions
- [Documenting and being prepared to report compliance with these practices to OMB within 365 days of the memo's issuance — by April 3, 2026](https://department.va.gov/ai/department-of-veterans-affairs-compliance-plan-for-omb-memorandum-m-25-21/), per the memo's own implementation timeline (as reflected in other agencies' published M-25-21 compliance plans)

HHS has not demonstrated compliance with M-25-21 for AERO. Compliance attorneys at the [National Law Review](https://natlawreview.com/article/hhss-aero-initiative-what-hospitals-need-do-right-now) now advise that any organization receiving AERO correspondence should file a FOIA request specifically seeking:

- The AI's methodology documentation
- Training data composition
- Validation studies
- Bias assessments
- Any documentation of OMB M-24-10/M-25-21 pre-clearance compliance

M-25-21 is a live legal challenge vector. If HHS deployed AERO without the required pre-deployment testing or AI impact assessment, that gap is discoverable and challengeable.

## What This Means for the Scope

The organizations within AERO's reach include virtually every major healthcare institution that receives federal funding:

- State Medicaid agencies
- Nonprofit healthcare providers
- Public hospital systems
- Federally qualified health centers (FQHCs)
- Academic medical centers and universities with federal research grants
- Head Start programs
- Addiction treatment providers
- Federal grant subrecipients through universities

If your technology platform is deployed at any of these organizations, AERO is now part of your customer's compliance landscape — whether they know it yet or not.

## Builder Implications

### 1. Audit trail architecture is now a compliance defense layer

AERO surfaces findings from Single Audit data. But when AI flags a finding as "chronic noncompliance," the defense is documentation: corrective action plans, evidence of remediation, dated records showing what changed and when. If you build financial, grant management, or compliance software for any organization in scope, audit trail completeness is a product requirement, not a feature.

### 2. The pattern will spread to other agencies

[HHS built AERO without a public RFP, a multi-year authorization process, or a vendor-selection competition](https://natlawreview.com/article/hhss-aero-initiative-what-hospitals-need-do-right-now) — legal analysts describe this as setting a procurement and deployment template other agencies can replicate at enforcement scale. The approach — scan publicly available audit data, identify patterns, initiate enforcement — requires no new regulatory authority. It requires only an LLM and five years of public filings. DOE, DOJ, and DOD run comparable grant programs with comparable Single Audit filing requirements. Expect this pattern to replicate.

### 3. FOIA + model card requests are a new enterprise workflow

When AI-powered government enforcement contacts your customer, the first response is not to address the finding — it is to demand the model's methodology. Healthcare and govtech builders should understand M-25-21 requirements and be prepared to help customers file and interpret FOIA responses on AI systems.

### 4. The error rate gap is a product opportunity

HHS's failure to publish an error rate is a significant gap. Organizations need tools to independently verify whether an AI-flagged finding reflects genuine noncompliance or a classification error. Audit data analysis tools that can replicate or challenge AERO's methodology — or help legal teams respond to AI-generated enforcement actions — have a market.

### 5. No appeal path means appeal paths will be created

The current absence of clear appeal rights does not mean appeals are impossible — it means they will be litigated. Healthcare lawyers will build the playbook. Technology tools that support that playbook (document collection, finding verification, audit trail reconstruction, FOIA response analysis) are infrastructure for a legal process that is forming right now.

## Immediate Steps for Healthcare Builders

If you ship software to organizations receiving $1 million or more in federal funds annually:

1. **Audit your customers' audit trail capabilities.** If corrective action plans and remediation evidence aren't timestamped and retrievable, that's a gap.

2. **Understand M-25-21.** The federal AI governance framework creates obligations on HHS but also creates procedures grantees can invoke. Know the framework.

3. **Build FOIA response support.** Help customers request AI methodology documentation when contacted by AERO or similar programs. This is now a legal first step, not an optional one.

4. **Flag this to your customers.** Most healthcare technology buyers have not received AERO correspondence yet. The ones who haven't are still in scope. Proactive disclosure from your team positions you as infrastructure, not just a vendor.

AERO will not be the last federal AI enforcement program. The question for builders is whether to be caught off-guard by the pattern or to build for it now, when the playbook is still forming and the leverage points are visible.

---

*This article is research-based. ChatForest does not provide legal advice. Organizations receiving AERO correspondence should consult qualified healthcare compliance counsel.*

