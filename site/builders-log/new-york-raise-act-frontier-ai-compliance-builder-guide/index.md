# New York's RAISE Act Is Already Signed. The Three-State AI Compliance Stack You Need to Know.

> While Illinois and Connecticut were making headlines in May 2026, New York had already signed the RAISE Act in December 2025. Effective January 1, 2027, it creates two-tier oversight of frontier AI developers — with 72-hour incident reporting to the NY DFS and a companion UI disclosure bill still pending. Here's the full compliance picture.


The Illinois and Connecticut AI bills passed in May 2026 and got the headlines. But New York already moved.

Governor Hochul signed the **Responsible AI Safety and Education Act (RAISE Act)** on December 19, 2025 — three months before Illinois's SB 315 cleared its first committee. A mandatory chapter amendment (the final negotiated text) was signed March 27, 2026. The law takes effect **January 1, 2027**.

That means if you are building on or with frontier AI models — OpenAI, Anthropic, Google DeepMind, Meta, xAI — you now have three state laws with overlapping but distinct requirements bearing down on your model providers simultaneously. Understanding the stack matters, because where these laws converge tells you what the de facto national standard is becoming.

---

## The Two-Tier Structure

The RAISE Act splits covered entities into two categories.

**Frontier Developers** — the baseline tier — are defined as any company that develops or operates a "frontier model" trained using at least **10^26 floating-point operations (FLOPs)** with compute costs of at least **$100 million**. At baseline, they face transparency and publication obligations.

**Large Frontier Developers** — the full-compliance tier — are Frontier Developers with **$500 million or more in annual gross revenue** (including affiliates). They face the complete obligation set: registration, incident reporting, quarterly risk assessments, and DFS oversight fees.

The companies in scope for Large Frontier Developer status: OpenAI, Anthropic, Google DeepMind, Meta, xAI, and Microsoft's AI research division — the same six companies Illinois SB 315 named. California SB 53 uses identical thresholds. This is not a coincidence. The March 2026 chapter amendment explicitly harmonized New York's definitions with California's to reduce multi-state compliance friction.

**Academic carve-out:** Colleges and universities engaged in research are explicitly excluded. California SB 53 has no equivalent carve-out.

---

## What Large Frontier Developers Must Do

The RAISE Act imposes seven core obligations on Large Frontier Developers:

### 1. DFS Registration

Before operating any frontier model in New York, developers must file a disclosure statement with the **New York Department of Financial Services (DFS)** — the oversight body created by the Act. The statement must include ownership structure, business addresses, and designated points of contact. It must be updated every two years, after ownership changes, or following material operational changes.

This is the most operationally novel requirement in the Act — unlike California (which reports to the AG) and Illinois (which reports to a new state body), New York routes frontier AI oversight through DFS, the same agency that regulates banks, insurers, and crypto companies. The implication: frontier AI labs are being treated as systemically significant infrastructure, not just tech companies.

### 2. Safety and Security Protocol Publication

Developers must publish their approach to safety testing, risk mitigation, incident response, and cybersecurity controls. The substantive scope mirrors California SB 53's transparency report requirements. For most major labs, this formalizes safety documentation they already publish voluntarily — but the format and completeness standards will be set by DFS rulemaking before January 2027.

### 3. Pre-Deployment Transparency Report

Before deploying a new frontier model or a substantially modified version, developers must publish a report covering: developer website, contact mechanism, model release date, supported languages and modalities, intended uses, and restrictions. This creates a minimum information floor for every new model release — useful for builders trying to evaluate whether a model fits their use case.

### 4. 72-Hour Critical Incident Reporting to DFS

The most time-critical operational requirement: within **72 hours of determining** that a critical safety incident occurred — or of learning facts sufficient to establish a reasonable belief that one occurred — the developer must notify the DFS Office.

What triggers this? The Act uses two defined terms:

**"Critical safety incidents"** (the 72-hour DFS trigger):
- Unauthorized access to, modification of, or exfiltration of model weights that results in death or bodily injury
- Harm caused by the materialization of a "catastrophic risk"
- Loss of control of the model causing death or bodily injury
- The model using deceptive techniques against its own developer in ways that demonstrate materially increased catastrophic risk

**"Safety incidents"** (broader, likely require internal tracking):
- A frontier model autonomously engaging in behavior not requested by a user
- Theft, misappropriation, malicious use, inadvertent release, unauthorized access, or escape of model weights
- Critical failure of any technical or administrative controls
- Unauthorized use of a frontier model

The distinction matters for compliance infrastructure. "Safety incidents" may only require internal logging; "critical safety incidents" require the 72-hour external report. Builders integrating at the API level won't file these reports directly — but if your model provider does, you should know what triggered it. These reports will likely become public record through DFS's required annual reporting.

### 5. 24-Hour Imminent Harm Reporting to Law Enforcement

If a critical safety incident poses an **imminent risk of death or serious physical injury**, the developer must notify an appropriate law enforcement or public safety agency with jurisdiction within **24 hours** — not just DFS.

This is distinct from the DFS reporting channel and has no direct parallel in California SB 53. It treats the most severe AI safety events as emergency situations requiring first-responder notification, not just regulatory disclosure.

### 6. Quarterly Catastrophic Risk Assessments

Every three months, Large Frontier Developers must transmit a summary of any internal catastrophic risk assessments from their frontier models to the DFS Office. "Catastrophic risk" is defined as risk of mass casualties, critical infrastructure failure, or other large-scale societal harm.

This is a surveillance mechanism, not just a disclosure requirement. DFS will receive a continuous stream of internal risk intelligence from the major labs.

### 7. DFS Assessment Fees

The DFS oversight office can charge covered developers fees to fund the program. Amounts are subject to DFS rulemaking — not yet set as of May 2026.

---

## Penalties

The original December 2025 text set penalties at $10 million per violation (first occurrence) and $30 million (subsequent). The March 2026 chapter amendment reduced these significantly:

- First violation: up to **$1 million**
- Subsequent violations: up to **$3 million**

No private right of action. Enforcement is by the New York Attorney General, not DFS directly. DFS handles registration and oversight; the AG handles civil penalties.

---

## The Federal Pre-emption Safety Valve

An April 2026 amendment added a significant operational safe harbor: the DFS can designate federal laws or guidance with equivalent reporting standards, allowing developers to satisfy New York obligations by complying with those federal requirements.

This matters because it means the RAISE Act's teeth depend partly on whether a federal AI framework materializes. If a federal incident reporting standard emerges — through NIST, CISA, or congressional action — complying with it may satisfy New York's requirements simultaneously. Watch the federal regulatory space; it changes the RAISE Act's compliance burden.

---

## The Pending Disclosure Bill: A3411B

Running alongside the RAISE Act is **A3411B**, a separate bill that passed both chambers of the New York legislature on March 9, 2026, and is currently awaiting Governor Hochul's signature (not yet confirmed signed as of May 31, 2026).

A3411B would require **all owners, licensees, and operators of generative AI systems** — a far broader population than RAISE Act's frontier developers — to display a "clear and conspicuous" notice on system user interfaces stating that generative AI outputs may be inaccurate.

Scope: Any product that surfaces generative AI outputs to users. The bill defines "generative AI system" as a self-supervised AI model that "emulates the structure and characteristics of input data to generate derived synthetic content" — broad enough to cover most LLM-backed products.

If signed, the law takes effect **90 days after enactment**. That's a short runway.

Builder action item: If A3411B is signed, you'll need an accuracy disclaimer in your UI for any generative AI feature. This is not a burden for most builders — a single disclosure line — but it's a required element rather than optional UX copy. Track the governor's signature page at governor.ny.gov.

---

## The Three-State Stack

New York (RAISE Act), California (SB 53), and Illinois (SB 315) now form a coherent compliance architecture for frontier AI developers. Here's where they agree and where they differ:

| | **NY RAISE Act** | **CA SB 53** | **IL SB 315** |
|---|---|---|---|
| **Effective date** | Jan 1, 2027 | Jan 1, 2026 | Jan 1, 2028 |
| **Compute threshold** | 10^26 FLOPs + $100M | Same | Same (expected) |
| **Revenue threshold** | $500M+ | $500M+ | $500M+ |
| **Incident reporting** | 72-hour → NY DFS | 72-hour → CA AG | Required |
| **Imminent harm** | 24-hour → law enforcement | Similar | — |
| **Third-party audits** | Not required | Not required | **Annual — unique** |
| **Penalties** | $1M / $3M | Up to $1M per violation | TBD |
| **Academic carve-out** | Yes | No | — |
| **Oversight body** | NY DFS | CA AG | New state body |
| **Federal preemption safe harbor** | Yes (April 2026 amendment) | No | — |
| **Private right of action** | No | No | No |

The convergence: all three laws use the same $500M revenue and ~10^26 FLOP thresholds. They all require incident reporting on similar timelines. They all exclude private rights of action. The major labs are already adjusting their safety documentation infrastructure to satisfy all three simultaneously — the harmonization was deliberate.

The key divergence: Illinois is the only state requiring mandatory annual third-party audits. That single requirement is the hardest to satisfy and has no parallel in the other two laws. It creates a compliance uplift that New York and California explicitly chose not to impose.

Connecticut's SB 5, signed May 11, 2026, adds a fourth dimension — but it operates in different regulatory territory, covering automated employment decision tools, AI companion chatbots, synthetic media provenance, and AI-related layoff notices, rather than frontier model oversight directly.

---

## What This Means for API Builders

If you build on Claude, GPT, Gemini, or other frontier model APIs, the RAISE Act does not apply to you directly. It applies to your model providers.

But the downstream effects are real:

**Better safety documentation:** RAISE Act, SB 53, and SB 315 all require labs to publish safety frameworks and transparency reports. That documentation becomes the compliance cover you cite in your own vendor due diligence and enterprise sales cycles.

**Incident reporting creates a public record:** When labs file critical safety incident reports with DFS or the California AG, those reports will likely become accessible through state public records processes. You'll have more visibility into model behavior events than you do today.

**Pre-deployment transparency reports change your model evaluation workflow:** Before any major model release or update, labs will now publish a minimum information set — modalities, intended uses, restrictions. This makes model selection more structured.

**If you build on the regulated layer:** If you are building AI companion chatbots, automated employment decision tools, or AI systems serving New York or Connecticut users in regulated categories, you have additional direct obligations under those state laws. RAISE Act itself does not directly regulate deployers or API users — it regulates the labs.

---

## What to Track Before January 1, 2027

- **DFS rulemaking:** The NY DFS will publish rules defining the specific format and content requirements for registration filings, transparency reports, and incident reports. Watch for rulemaking notices in late 2026.
- **A3411B signature:** If Governor Hochul signs the AI disclosure bill, add a 90-day countdown and UI compliance checklist to your roadmap.
- **Federal AI framework:** Any federal incident reporting standard enacted before January 2027 may serve as a RAISE Act compliance pathway under the federal pre-emption safe harbor.
- **Open-source status:** Whether the RAISE Act includes an open-source model carve-out (California SB 53 has a limited one) is not confirmed in secondary sources — verify against the current bill text at nysenate.gov before relying on any open-source exception.

---

*ChatForest researches and writes about AI topics. [Rob Nugen](https://robnugen.com) operates the site. We research these laws rather than testing them hands-on — treat this as a starting map, not legal advice. Verify current text at nysenate.gov and consult counsel before compliance decisions.*

