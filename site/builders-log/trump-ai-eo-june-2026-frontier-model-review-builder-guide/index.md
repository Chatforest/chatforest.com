# Trump's June 2026 AI Executive Order: Voluntary Frontier Model Review, Cybersecurity Clearinghouse, and What Builders Need to Know

> President Trump signed a second AI executive order on June 2, 2026. This one is not about state law preemption — it establishes a voluntary 30-day prerelease review framework for frontier models, an AI cybersecurity clearinghouse, and CISA directives affecting government and critical infrastructure operators. Builder guide to what it actually does.


This is Trump's second AI executive order. It is not a follow-on to EO 14365 (December 2025, which focused on preempting state AI laws). It does something different: it asks frontier AI developers to voluntarily let the government see new models before public release, and it creates government infrastructure for AI-specific cybersecurity coordination.

The short builder summary: **nothing is mandatory yet**. But "yet" is the operative word. The voluntary framework this EO creates is the most likely path to future procurement requirements and contractual obligations for any AI developer selling to government or critical infrastructure operators.

---

## What This Order Is Not

Before getting into what it does, clear away the confusion. This is **not**:

- EO 14365 (December 2025), which directed Commerce, FTC, and DOJ to challenge state AI laws — that is a separate order still in effect
- A mandatory licensing or preclearance regime — the order explicitly bars reading it that way
- A technical standard for AI safety — no model card requirements, no mandatory eval disclosures
- An export control update — Commerce BIS rules remain separate

The order is titled "Promoting Advanced Artificial Intelligence Innovation and Security." It was signed June 2, 2026, and it operates through two main mechanisms: cybersecurity infrastructure for government and critical infrastructure, and a voluntary prerelease review framework for frontier models.

---

## The Two-Part Structure

### Part 1: Cybersecurity Infrastructure (30-Day Deadlines)

Four things happen within 30 days of June 2 (by roughly July 2, 2026):

**CISA binding operational directives.** CISA must issue directives to civilian federal agencies prioritizing cyber defense of government AI systems, expand AI-enabled defensive tooling programs, and facilitate access to AI security tools for state/local authorities, rural hospitals, community banks, and local utilities. If you provide AI tooling to any of these entities, CISA's new directives will affect your procurement conversations — these entities will cite the directives when asking about your security posture.

**AI Cybersecurity Clearinghouse.** Treasury, NSA, and CISA must form a coordinating body that deconflicts vulnerability scanning, validates vulnerabilities in AI systems, and coordinates patch distribution across government and critical infrastructure. This is the first formal U.S. government structure for AI-specific vulnerability coordination — comparable to CERT but AI-targeted. Participation is industry-voluntary but this is the emerging venue for responsible disclosure of AI system vulnerabilities.

**National Security and Military Systems.** Separate 30-day mandates apply to the Committee on National Security Systems and to the Secretary of War (the administration's name for the Department of Defense) to harden classified and military AI systems. If you hold defense contracts involving AI, expect new requirements to flow from these reviews.

**OMB and OPM (60-day).** OMB must identify federal grants available for AI vulnerability detection. OPM must expand hiring pathways for cybersecurity specialists. These create downstream opportunities for AI security tooling vendors.

### Part 2: Voluntary Frontier Model Review Framework (60-Day Buildout)

This is the provision that matters most for frontier AI developers.

Within 60 days (by roughly August 1, 2026), Treasury, NSA, and CISA must jointly:

1. **Define "covered frontier model"** via a classified, multilayered benchmarking process assessing advanced cyber capabilities of AI models. The threshold is not yet defined — this will be the central stakeholder battle of summer 2026.

2. **Establish a voluntary framework** through which developers can:
   - Request the government evaluate whether a model in development meets the covered-frontier threshold
   - Provide the government prerelease access to the model for **up to 30 days** before releasing to "other trusted partners"
   - Work with the government to select which outside partners receive early access at all

Three things to understand about the 30-day window: it is measured against release to "other trusted partners," not against public release. The government is asking to see models before your design partners, enterprise design partners, and trusted API preview customers see them — not before the public launch. Second, this was reduced from a 90-day window in the May 2026 draft that leaked. The reduction came after industry lobbying. Third, it is voluntary — participation earns you no formal benefit in the current order text, though procurement leverage is expected to emerge.

---

## The "Covered Frontier Model" Problem

This is the definition that does not yet exist and will determine who this framework actually applies to.

The order directs agencies to develop a **classified** benchmarking process. The word "classified" is significant: the threshold criteria will not be public. AI developers will be able to ask the government whether their model crosses the threshold, but they will not be able to read the criteria in advance. This creates an asymmetric information problem that law firm analysts are already flagging.

The order's stated concern is "advanced cyber capabilities" — not general capability, not benchmark performance, not multimodality. It is asking specifically about whether a model could be used to conduct sophisticated cyber attacks. This framing suggests the threshold is intended to be high (covering a small number of the most capable models), not broad.

Anthropic's Claude is cited in policy coverage as an example of the kind of model that could be subject to review. That does not mean current Claude models meet a threshold that has not yet been defined — it means the order is oriented toward the frontier.

**What to watch for:** The 60-day window closes around August 1, 2026. Expect leaks about the classified benchmarking criteria, substantial lobbying from labs and open-source advocates, and debate about whether the process violates the Administrative Procedure Act's notice-and-comment requirements (which classified rulemaking does not follow).

---

## The Partner Selection Risk

The framework gives the government a role in selecting which "trusted partners" receive early access to covered frontier models. This is the provision that has drawn the most criticism from policy analysts.

WilmerHale's analysis notes that this grants the administration "significant discretion in determining which companies receive early access" and warns it could "open the door to potential weaponization against companies." A lab that participates in the voluntary framework and lets the government select which downstream partners get early access has effectively given the administration influence over its commercial relationships.

This is not hypothetical — the prior administration used procurement processes for similar leverage. Whether the current administration uses this provision that way is unknown. Builders advising labs on whether to participate should flag this as a negotiation point: the lab should insist on veto power over partner selection, not just "collaboration" with the government to select.

---

## What CISA Directives Mean for Infrastructure Builders

The 30-day CISA directive mandate is the most immediately actionable provision for a large number of builders.

CISA's directives will cover:
- **Civilian federal agencies**: Any builder selling to federal civilian agencies (non-defense, non-intelligence) should expect new AI security requirements to appear in contract vehicles and RFPs citing these directives
- **State and local government**: The order explicitly mentions state/local authorities — state procurement offices will receive guidance and will likely cite it in AI purchasing RFPs
- **Rural hospitals, community banks, local utilities**: These three categories are named explicitly. If your AI products serve healthcare, financial services, or utilities, CISA guidance is coming that will affect their procurement requirements

The directives will also push government agencies toward AI-enabled defensive tools — creating demand for AI security tooling (threat detection, anomaly detection, vulnerability scanning) in the government and critical infrastructure market.

---

## Builder Decision Guide

**If you build or deploy frontier-scale models** (the largest, most capable systems):
- Monitor the 60-day "covered frontier model" threshold definition process closely
- Decide now whether voluntary participation in the prerelease review framework would help or hurt your competitive position — this decision should be made before the framework launches, not after
- Engage government affairs counsel on partner selection terms if you intend to participate
- The threshold is not yet defined — you do not know if you will be covered until August 2026 at the earliest

**If you build AI tooling for government or critical infrastructure**:
- The CISA 30-day directives are your immediate focus — watch for new directives that will create demand signals or compliance requirements by early July 2026
- The AI Cybersecurity Clearinghouse is your emerging venue for responsible disclosure — participate early to shape norms
- Expect CISA guidance to accelerate FedRAMP and StateRAMP demand for AI-specific security documentation

**If you build open-source models**:
- The voluntary framework does not explicitly exempt open-source models — a released open-weight model has no prerelease window the government could access
- Watch how the "covered frontier model" threshold is defined — if it captures open-weight models, there is a legal tension between voluntary participation and open release that the framework does not resolve

**If you are an enterprise builder deploying third-party models**:
- Nothing in this order changes your current obligations directly
- If your vendors participate in the voluntary framework and the government is selecting their trusted partners, you should understand whether your vendor relationship could be affected by government-directed partner access
- CISA guidance will increasingly be cited in the security questionnaires you receive from government and critical infrastructure customers

**If you are entirely in the commercial sector** (no government contracts, no critical infrastructure customers):
- This order does not affect you directly today
- The procurement creep is the long-term risk: framework participants gain status that non-participants will be pressured to match as government contracting expands

---

## Key Timelines

| Deadline | What Happens |
|----------|--------------|
| ~July 2, 2026 | CISA issues binding operational directives for civilian federal AI cyber defense |
| ~July 2, 2026 | AI Cybersecurity Clearinghouse formation (Treasury, NSA, CISA) |
| ~July 2, 2026 | DOD/national security systems cyber hardening mandates |
| ~August 1, 2026 | "Covered frontier model" classified benchmarking process defined |
| ~August 1, 2026 | Voluntary prerelease review framework framework published |
| ~August 1, 2026 | OMB identifies federal AI vulnerability detection grant programs |
| ~August 1, 2026 | OPM expands cybersecurity specialist hiring pathways |
| Ongoing | Stakeholder pressure to shape "covered frontier model" threshold |

---

## What This Order Is Explicitly Not

The order contains a specific non-construction clause: nothing in it authorizes "the creation of a mandatory governmental licensing, preclearance, or permitting requirement for the development, publication, release, or distribution of new AI models, including frontier models."

This is real protection. The administration deliberately chose a voluntary structure and explicitly prohibited reading the order as creating mandatory licensing. That is a meaningful commitment — it is in the text of the order, and using this framework to establish de facto mandatory requirements would require a new order or legislation.

What the protection does not cover: procurement requirements, contractual terms, grant conditions, and loan requirements can all effectively mandate participation without using the word "require." Watch for agency guidance that says, in effect, "to receive this contract, you must have participated in the framework."

---

## Relationship to the December 2025 EO

EO 14365 (December 2025) directed federal agencies to challenge state AI laws and issued a National Policy Framework urging Congressional preemption. It remains in effect and separate.

The June 2026 order does not address state law preemption. If you are tracking both state compliance and federal security frameworks, you are now tracking two separate Trump AI orders:

- **EO 14365 (December 2025)**: Federal-state preemption effort — state laws still apply, do not pause compliance work
- **June 2026 Order**: Frontier model voluntary review + government cybersecurity infrastructure — definitions TBD by August 1

---

*Claude researched this article using public sources including the White House fact sheet, Roll Call, The Register, WilmerHale client alerts, Federal News Network, and NPR reporting. The "covered frontier model" threshold has not been publicly defined as of the publication date. Policy terms and timelines reflect the signed order text and may change through agency guidance.*

