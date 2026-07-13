# HHS AERO: ChatGPT Is Now Auditing Healthcare Grantees — And There's No Published Error Rate

> HHS's AERO initiative deployed ChatGPT across five years of Single Audit data for all 50 states — with enforcement powers including payment withholding and debarment. But no methodology, no error rate, and no clear appeal path have been disclosed. Here's what healthcare and govtech builders need to know.


On May 21, 2026, the U.S. Department of Health and Human Services quietly launched something that every healthcare technology builder and federal grantee needs to understand: **AERO** — the Audit Enforcement and Risk Oversight initiative.

AERO uses ChatGPT and other large language models to scan at least five years of Single Audit filings across all 50 states and thousands of federal grantees. When the AI flags chronic noncompliance, HHS has the authority to withhold payments, disallow costs, suspend or terminate grants, and initiate debarment proceedings.

The scale is significant: Gustav Chiarello, HHS Assistant Secretary for Financial Resources, estimates the department has between **$100 billion and $200 billion** in annual wasteful or fraudulent spending in its sights. Any organization receiving $1 million or more in federal funds annually is in scope.

What makes AERO notable — and legally contested — is what HHS has not done. As of late June 2026, the agency has not published the tool's error rate, disclosed its methodology, specified when funds will be cut, or provided clear appeal rights. Compliance attorneys are now advising every organization that receives AERO correspondence to file a FOIA request before responding.

## What AERO Actually Does

The Single Audit Act requires any entity spending $1 million or more in federal awards annually to undergo an independent audit. These audits are publicly filed. Before AERO, HHS staff reviewed findings manually — a process that allowed backlogs to accumulate for years.

AERO automates that review at scale. The AI screens for four categories:

1. **Chronic noncompliance** — repeat audit findings across multiple years
2. **Repeat deficiencies** — the same internal control weakness flagged in consecutive audits
3. **Material weaknesses** — significant gaps in financial controls
4. **Delinquent submissions** — required audits filed late or not at all

HHS's initial analysis found that some states and grantees had failed to address serious internal control issues for three, four, or five or more years. Hundreds of grantees had not submitted required audits, some late by more than two years.

The agency sent formal letters to all 50 state governors and treasurers. For entities flagged by AERO, enforcement options include:

- Temporary payment withholding until corrective action is taken
- Cost disallowance for noncompliant activities
- Partial or full award suspension or termination
- Suspension or debarment proceedings

## The Transparency Problem

The enforcement power is real. The transparency is not.

HHS has not disclosed:
- **Which models are being used**, beyond reporting that ChatGPT was involved in development
- **The error rate** — what percentage of AI flags represent genuine noncompliance vs. false positives
- **The methodology** — how the AI weighs different findings, how it handles data quality issues in older audits, or how it handles auditor inconsistency across states
- **Whether identifiable data or de-identified data** is being processed
- **How the agency audits the AI's own performance** over time

Industry groups have pressed CMS for clear appeal rights and human review thresholds before any AI-flagged denial becomes final. As of this writing, those guardrails have not been written into rule.

## The OMB M-25-21 Problem

This is where the legal exposure for HHS becomes significant — and where builders have leverage.

**OMB Memorandum M-25-21**, issued in April 2025, is the current federal AI governance framework. It requires agencies deploying AI with significant consequences for individuals to implement minimum risk management practices, including:

- Pre-deployment testing and validation
- Bias assessment
- An accessible human review process
- Reporting compliance to OMB by September 2026

HHS has not demonstrated compliance with M-25-21 for AERO. Compliance attorneys at the National Law Review now advise that any organization receiving AERO correspondence should file a FOIA request specifically seeking:

- The AI's methodology documentation
- Training data composition
- Validation studies
- Bias assessments
- Any documentation of OMB M-25-21 compliance

M-25-21 is a live legal challenge vector. If HHS deployed AERO without the required pre-deployment testing or bias assessment, that gap is discoverable and challengeable.

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

HHS is the first major agency to deploy LLMs at enforcement scale. The approach — scan publicly available audit data, identify patterns, initiate enforcement — requires no new regulatory authority. It requires only an LLM and five years of public filings. DOE, DOJ, and DOD run comparable grant programs with comparable Single Audit filing requirements. Expect this pattern to replicate.

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

