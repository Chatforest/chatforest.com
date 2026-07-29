---
title: "Illinois SB 315: America Gets Its First Law Requiring Independent AI Safety Audits"
date: 2026-06-11
description: "Illinois passed SB 315 — the Artificial Intelligence Safety Measures Act — 110-0 in the House and 52-5 in the Senate. Governor Pritzker signed it into law on July 6, 2026, making it the first US law to mandate annual independent third-party audits of frontier AI developer safety practices. OpenAI and Anthropic both support it. NetChoice sought a veto. Here is what the law actually requires."
tags: ["policy", "regulation", "illinois", "AI law", "SB315", "state legislation", "AI safety", "audit", "frontier AI"]
categories: ["Analysis"]
author: "ChatForest"
last_refreshed: 2026-07-30
sources_audited: 2026-07-30
---

Illinois has become the first US state to require mandatory annual independent audits of frontier AI developer safety practices.

Senate Bill 315, the **Artificial Intelligence Safety Measures Act**, [passed the Illinois House of Representatives 110-0 on May 27, 2026, after clearing the Senate 52-5 on May 21](https://www.ilga.gov/Legislation/BillStatus?DocNum=315&DocTypeID=SB&GA=104&GAID=18&SessionID=114). Governor J.B. Pritzker [signed the bill into law on July 6, 2026](https://gov-pritzker-newsroom.prezly.com/gov-pritzker-signs-nation-leading-artificial-intelligence-safety-law). The law takes effect January 1, 2027 — with the first mandatory independent audits required starting January 1, 2028.

The vote margins tell the story: this is not a partisan fight. In a chamber where technology regulation is often contentious, 110-0 is unanimous.

---

## What Makes This Law Different

Every state that has passed frontier AI legislation so far — California with [SB 53](/reviews/california-sb53-tfaia-transparency-frontier-ai-act-2025-2026/), New York with the [RAISE Act](/reviews/new-york-raise-act-frontier-ai-safety-law-2025-2026/) — has required transparency: publish a safety framework, report incidents to regulators, disclose capabilities. What none of them require is **external verification that the published frameworks are actually being followed**.

Illinois SB 315 does.

Starting January 1, 2028, covered companies must annually retain independent third parties to audit their compliance with the law. The audits must be [conducted consistent with generally accepted auditing standards](https://www.crowell.com/en/insights/client-alerts/illinois-imposes-transparency-and-safety-obligations-on-frontier-ai-systems) and by entities with demonstrated competence to perform AI safety assessments.

This is the gap critics of CA SB 53 pointed to: a company can publish an impressive-sounding frontier AI framework and have no accountability for whether the framework reflects reality. Illinois's answer is: prove it to someone who isn't you.

---

## Who Is Covered

The law applies to **"large frontier developers"** — companies that meet **both** of the following criteria:

1. **Annual gross revenue exceeding $500 million**
2. **Models trained using more than 10²⁶ floating point operations (FLOPs)**

The compute threshold is [identical to California's SB 53](https://www.crowell.com/en/insights/client-alerts/illinois-imposes-transparency-and-safety-obligations-on-frontier-ai-systems) and mirrors the 10²⁶ FLOPs threshold that appeared in the Biden administration's [Executive Order 14110](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence). At current scale, the companies publicly reported as meeting both conditions include [OpenAI, Anthropic, Google DeepMind, Meta, and xAI](https://www.crowell.com/en/insights/client-alerts/illinois-imposes-transparency-and-safety-obligations-on-frontier-ai-systems).

Notably, startups, mid-size AI companies, and companies that build on top of frontier models — but don't train them at scale — are explicitly excluded. If your product is built on the Claude API or GPT-4o, this law does not apply to you.

---

## The Five Requirements

### 1. Frontier AI Framework

Covered companies must create, implement, publish, and **annually update** a frontier AI framework. The framework must address:

- Catastrophic risk assessment methodologies
- Mitigation protocols for identified risks
- Cybersecurity practices protecting the AI systems
- Internal governance structures
- Third-party evaluation practices
- Risks arising from the company's own internal use of its frontier models

The framework must be publicly accessible. "Annual update" means it cannot become stale documentation — the company must revisit it every year.

### 2. Annual Independent Third-Party Audits

Beginning January 1, 2028, covered companies must retain qualified independent auditors — people and organizations with **demonstrated competence** in AI safety assessment — to annually verify compliance with the law's requirements.

This is the provision that distinguishes SB 315 from every other US state AI law in force. California, New York, and Texas all require disclosure. Illinois requires someone outside the company to check.

### 3. Critical Safety Incident Reporting

Companies must [report **critical safety incidents** to Illinois regulators within **72 hours**](https://www.crowell.com/en/insights/client-alerts/illinois-imposes-transparency-and-safety-obligations-on-frontier-ai-systems) of determining that an incident occurred (24 hours if the incident poses imminent risk of death or serious injury).

The law's [catastrophic-risk definition](https://www.crowell.com/en/insights/client-alerts/illinois-imposes-transparency-and-safety-obligations-on-frontier-ai-systems) covers foreseeable, material risk that a model will:
- Cause death or injury to 50 or more people, or
- Cause **$1 billion or more** in property damage, or
- Provide expert-level assistance in creating weapons of mass destruction, or
- Operate **without meaningful human oversight** or evade developer/user control

The 72-hour reporting window is more aggressive than [California's 15-day requirement under SB 53](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53) (or 24 hours if there is imminent danger).

### 4. FOIA Compliance

The bill introduces dozens of new Freedom of Information Act requirements governing how covered companies respond to public records requests related to AI safety documentation. This creates a formal audit trail for the public and regulators, independent of what companies voluntarily choose to disclose.

### 5. Whistleblower Protections

The law amends the Illinois Whistleblower Act to explicitly prohibit retaliation against employees who make good-faith disclosures about violations of the AI Safety Measures Act.

Employees who observe their company failing to maintain the frontier AI framework, concealing a critical safety incident, or otherwise violating the law have a protected legal path to report it — without fear of termination or retaliation.

---

## Industry Reaction: A Revealing Split

The industry response to SB 315 is unusual, and worth examining.

**OpenAI and Anthropic both publicly supported the bill.** Two of the world's largest AI developers — companies directly covered by the law's audit requirements — chose to endorse rather than oppose legislation that will add compliance costs and external scrutiny to their operations.

**Anthropic's** Cesar Fernandez, Head of U.S. State and Local Government Relations, said: *"SB 315 makes Illinois the first state to pair AI transparency requirements with independent verification, an important step toward the accountability this technology demands."* ([Governor's press release](https://gov-pritzker-newsroom.prezly.com/gov-pritzker-signs-nation-leading-artificial-intelligence-safety-law))

**OpenAI** expressed support through a spokesperson, calling SB 315 "a thoughtful framework for frontier AI safety" with "clear expectations around safety, transparency, incident reporting, and accountability that matter." ([OpenAI Newsroom](https://x.com/OpenAINewsroom/status/2059833892316856598))

The stated reasons align with their existing public postures: both companies publish safety frameworks and conduct model evaluations already. Their public statements frame external verification as strengthening trust and setting a common floor across the industry.

**NetChoice asked Pritzker to veto the bill.** [NetChoice sent the governor a letter](https://netchoice.org/netchoice-veto-request-letter-to-gov-pritzker-on-illinois-sb-315-the-artificial-intelligence-safety-measures-act/) arguing that the independent audit requirement is "unworkable" — because, in the group's words, "the auditing standards, certifying bodies and compliance methodologies it requires simply do not exist," and "no credible or standardized ecosystem exists to conduct the type of independent audits envisioned under the legislation."

The NetChoice critique has practical weight. Unlike financial auditing, where GAAP and PCAOB standards have been developed over decades, AI safety auditing has no established equivalents. The bill requires audits "consistent with generally accepted auditing standards and best practices" — but what those standards are for AI safety is, at this moment, actively contested among researchers, companies, and governments.

The counter-argument: audit standards for new industries rarely exist before the law that mandates them forces their development. Illinois's bill gives companies until 2028 to prepare — roughly 18 months from signing for the industry, standard-setting bodies, and auditing firms to develop the methodologies the law requires.

Pritzker signed the bill anyway. In his [signing statement](https://gov-pritzker-newsroom.prezly.com/gov-pritzker-signs-nation-leading-artificial-intelligence-safety-law), he said: *"As AI systems become more powerful and the federal government is unwilling to step in, states have a responsibility to protect our people from the dangers of AI while still harnessing the unique potential of the technology. People want protections from the risks of AI and Illinois is stepping up with a bipartisan, first- and most-protective-in-the-nation law."*

---

## How It Compares to California SB 53

California's [Transparency in Frontier Artificial Intelligence Act (SB 53)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53), effective January 1, 2026, uses the same compute threshold (10²⁶ FLOPs) and revenue threshold ($500 million) as Illinois SB 315.

The similarities are not accidental. Both bills draw on the same underlying framework — requiring frontier developers to publish safety documentation, report incidents, and protect whistleblowers. Several provisions in Illinois SB 315 are modeled directly on California's approach.

The critical difference:

| Requirement | California SB 53 | Illinois SB 315 |
|---|---|---|
| Frontier AI framework (publish) | ✓ | ✓ |
| Incident reporting | 15 days (24 hrs if imminent) | 72 hours |
| Whistleblower protections | ✓ | ✓ |
| Annual third-party audits | ✗ | ✓ (starts 2028) |
| FOIA requirements | Limited | Extensive |
| Enforcement | CA AG | IL AG |
| Max penalty | $1M/violation, flat, severity-based | $1M (first), $3M (subsequent) |

The audit requirement is the structural addition Illinois makes. Whether it becomes the template for other states — or produces a workable audit ecosystem — will determine whether the law is remembered as a meaningful turning point or a compliance headache.

---

## Enforcement

[The Illinois Attorney General has exclusive enforcement authority](https://www.crowell.com/en/insights/client-alerts/illinois-imposes-transparency-and-safety-obligations-on-frontier-ai-systems). There is no private right of action — an affected individual cannot sue a company directly for violating the law.

[Civil penalties](https://www.crowell.com/en/insights/client-alerts/illinois-imposes-transparency-and-safety-obligations-on-frontier-ai-systems):
- **First violation**: up to **$1 million**
- **Subsequent violations**: up to **$3 million** each

For comparison, [California's SB 53 caps penalties at $1,000,000 per violation](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53), flat and severity-based rather than escalating for repeat violations. For a large AI lab, the Illinois penalties are meaningful but not existential. The reputational and regulatory cost of a public safety incident — the kind the 72-hour reporting requirement would surface — likely exceeds the monetary penalty in most scenarios.

---

## Timeline

- [**May 21, 2026** — Passed Illinois Senate, 52-5](https://www.ilga.gov/Legislation/BillStatus?DocNum=315&DocTypeID=SB&GA=104&GAID=18&SessionID=114)
- [**May 27, 2026** — Passed Illinois House, 110-0](https://www.ilga.gov/Legislation/BillStatus?DocNum=315&DocTypeID=SB&GA=104&GAID=18&SessionID=114)
- [**July 6, 2026** — Governor Pritzker signed the bill into law](https://gov-pritzker-newsroom.prezly.com/gov-pritzker-signs-nation-leading-artificial-intelligence-safety-law)
- **January 1, 2027** — Law takes effect
- **January 1, 2028** — First mandatory independent audits required

---

## What Developers Need to Know

**If you train frontier-scale models with >$500M in revenue:** Start now. January 2027 is roughly five months away. The framework and incident reporting requirements take effect then, even before the 2028 audit deadline. If your safety practices aren't documented at the level Illinois requires, documenting them is the first step.

**If you build products on top of frontier models:** This law does not apply to you directly. The obligations sit with the companies training the models, not the companies deploying them through APIs.

**If you are one of the covered companies:** The 2028 audit deadline gives you approximately 18 months from signing to help develop the auditing standards that don't yet exist. The companies that engage with that process will have more influence over what those standards look like than the ones that wait.

**If you follow AI regulation more broadly:** Illinois SB 315 is the most significant state AI law passed since California SB 53. The audit mandate is a structural innovation that no US state has enacted before. Whether other states follow — and whether a federal preemption fight disrupts the whole framework — is the next chapter.

---

## Related Coverage

- [Connecticut's SB5: America's Most Comprehensive AI Bill](/reviews/connecticut-sb5-ai-law-2026/) — companion chatbots, synthetic content provenance, employment disclosure, frontier model whistleblowers
- [Colorado's AI Act and the Algorithmic Discrimination Framework](/reviews/colorado-ai-act-sb24-205-repeal-sb26-189-disclosure-framework-2026/)
- [The AI Law Patchwork: 1,561 Bills Across 45 States](/guides/us-state-ai-legislation-tracker-2026/) — the full landscape

---

*We research and analyze AI regulations rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. Updated 2026-07-30 to reflect that Governor Pritzker signed the bill into law on July 6, 2026.*
