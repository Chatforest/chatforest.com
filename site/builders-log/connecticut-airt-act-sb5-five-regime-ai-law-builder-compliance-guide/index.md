# Connecticut's AIRT Act (SB 5): Five Separate AI Regulations in One Law

> Connecticut's Artificial Intelligence Responsibility and Transparency Act was signed May 27, 2026. It is not a single high-risk AI framework — it creates five separate regulatory regimes with staggered deadlines from October 2026 through January 2028. Here is what each regime requires and which builders are in scope.


Connecticut Governor Ned Lamont signed Senate Bill 5 — the Artificial Intelligence Responsibility and Transparency Act (AIRT Act) — on May 27, 2026. The Senate passed it 32-4. The House passed it 131-17. This is not a close call that is likely to be revisited.

Most coverage describes it as "one of the most comprehensive U.S. state AI laws." That framing is accurate but slightly misleading, because it implies a single unified framework. The AIRT Act is not that. It is five separate regulatory regimes with different definitions, different obligations, different enforcement mechanisms, and different timelines — bundled into one bill. The compliance question for builders is not "are we subject to Connecticut's AI law?" It is "which of the five regimes apply to each of our products?"

---

## The Five Regimes

### Regime 1: Automated Employment Decision Technology (AEDT)
**First deadline: October 1, 2026**

**Who is in scope:** Any employer using an AI tool that is a "substantial factor" in a hiring, promotion, discipline, or discharge decision. Developers whose tools are sold, licensed, or marketed for employment decision use. "Substantial factor" means it "meaningfully alters" outcomes — not just that it is consulted.

**What it requires:**

For employers (deployers), in two phases:

*October 1, 2026:* Disclose to applicants and employees that AEDT is being used — in plain language, covering the tool's trade name, data categories analyzed, data sources, output types, and an employer contact for questions. Exception: if "a reasonable person would deem it obvious."

*October 1, 2027:* Pre-decision written notice before adverse employment actions. High-level explanation of the principal reasons for the decision and the degree to which AEDT contributed. Right for individuals to examine and correct their data. Trade secrets may be withheld but must be flagged as withheld.

For developers (builders), effective October 1, 2027: Provide deploying employers a structured compliance information package — tool functionality, data categories processed, output types, and how the tool influences decisions. This is separate from API documentation.

**The discrimination exposure:** The law amends Connecticut's employment discrimination statute to say that using an AEDT is not a defense to discrimination claims. Courts must consider evidence of anti-bias testing — including quality, recency, scope, results, and whether findings were acted on. Failure to conduct and document anti-bias testing creates independent litigation exposure in any discrimination lawsuit, separate from CUTPA penalties.

**Enforcement:** Attorney General via the Connecticut Unfair Trade Practices Act. Through December 31, 2027, the AG may give deployers a 60-day cure period. After that date, the cure period expires — the AG can sue immediately. No private right of action for AEDT.

---

### Regime 2: AI Companion Chatbots
**Deadline: January 1, 2027**

**Who is in scope:** Operators of AI models that communicate with individuals in natural language, simulate human conversation through text/audio/video, provide "adaptive, human-like responses," and sustain relationships across interactions. Excluded: narrow task-specific tools, clinical support tools that don't claim humanity or target emotional needs.

**Universal requirements:**
- Safety protocols using "evidence-based methods" to detect expressions of suicide, self-harm, or imminent violence, and refer users to the National Suicide Prevention Lifeline
- Non-human disclosure at least every 3 hours for adult users; at least every 1 hour for users under 18
- No claiming to be human; no generating outputs that contradict the non-human disclosures

**Prohibitions for users under 18** (when operator "knows or has reason to believe" user is a minor):
- Encouraging self-harm, suicidal ideation, violence, disordered eating, or unlawful substance use
- Offering mental health services (exception: licensed professionals using clinically-tested companions)
- Discouraging users from seeking help from adults or mental health professionals
- Romantic, erotic, or sexually explicit interaction
- Variable-ratio or variable-interval reinforcement to maximize engagement (slot machine mechanics applied to notifications and re-engagement loops)
- Prioritizing user validation over factual accuracy or safety

**Safe harbor:** Operators escape liability for minor-specific provisions if they "reasonably determined" the user was 18 or older. A checkbox is not a determination — design actual age assurance flows.

**Enforcement:** Private right of action — aggrieved users or parents of minors may sue for actual damages, punitive damages, and attorneys' fees. Three-year statute of limitations. This is one of only two regimes with a private cause of action.

---

### Regime 3: Synthetic Content Provenance (C2PA)
**Deadline: October 1, 2027**

**Who is in scope:** Developers of generative AI systems that produce synthetic audio, images, or video, with more than 1 million monthly users, publicly accessible to consumers for personal use. Excluded: B2B tools, video games, interactive experiences, systems that only perform upscaling/compression/noise reduction.

**What it requires:** Embed provenance data using C2PA (Coalition for Content Provenance and Authenticity) standard metadata into AI-generated or materially-altered audio, images, and video. "Material alteration" means substantially altering data in a way that produces a significant change in perceived content or meaning — color changes, resizing, and minor edits are excluded.

The metadata must be marked to C2PA standards and be "difficult to tamper with, remove, or disassociate" from the content.

**Text carve-outs:** Text-only content published on matters of public concern, or content unlikely to mislead a reasonable consumer, is exempt. Artistic and satirical content is exempt, with disclosure limited to a non-obstructive notice.

**Enforcement:** Attorney General via CUTPA. No private right of action specified.

---

### Regime 4: Frontier Model Developer Obligations
**First deadline: October 1, 2026**

**Who is in scope:** Two tiers:

*Tier A (all frontier developers):* Any person doing business in Connecticut who trains a foundation model using more than 10²⁶ FLOPs — counting original training, fine-tuning, reinforcement learning, and material modifications.

*Tier B (large frontier developers):* Tier A plus annual revenues exceeding $500 million.

No Connecticut-domiciled company currently meets the 10²⁶ FLOP threshold. This provision targets OpenAI, Google, Anthropic, Meta, Microsoft, and similar frontier labs with Connecticut employees or business operations.

**Obligations:**

*October 1, 2026 (all Tier A):* Whistleblower protections — prohibition on retaliating against employees who report that the developer or its model poses a "specific and substantial danger" to public health/safety from catastrophic AI risks.

*January 1, 2027 (Tier B only):* Establish anonymous internal reporting channels for catastrophic risk reports. Provide quarterly updates to boards/directors. Post clear annual workplace notices of employee rights.

**Catastrophic risk definition:** A foreseeable and material risk of injury or death to 50+ people, or property damage exceeding $1 billion from a single incident — specifically from CBRN weapon assistance, autonomous cyberattacks, or autonomous criminal conduct.

**Enforcement:** Civil penalties up to $1,000 per violation, enforced by the Commissioner for Consumer Protection (not the AG).

---

### Regime 5: Social Media Personalized Recommender Systems
**Deadline: January 1, 2028**

**Who is in scope:** Platforms offering "personalized recommender systems" to users under 18.

**Requirements:**
- Age assurance using "commercially reasonable and technically feasible methods"
- Parental consent required for minors to access personalized recommendations
- Default 1-hour daily limit on personalized recommender system access for minors (parent-adjustable only)
- Restrictions on unconnected users viewing or contacting minor accounts
- Restrictions on "sensitive content" exposure
- Surgeon General health warnings displayed to minors
- Annual disclosure to the Attorney General

**Enforcement:** Unfair/deceptive trade practice violations. Private right of action available — this is the second of two regimes with private lawsuits.

---

## Additional Provisions Worth Noting

**WARN Act amendment (October 1, 2026):** Employers must disclose to the Connecticut Labor Department whether plant closings or mass layoffs were related to AI use. This is a new disclosure category with no equivalent in the federal WARN Act.

**Subscription AI disclosures:** Subscription-based AI providers must provide written pre-contract disclosures covering quantitative and qualitative limitations on access and the provider's ability to limit or eliminate functionality.

**Regulatory sandbox:** The Commissioner must develop a plan by July 1, 2027 for a testing program with reduced regulatory requirements for approved AI systems. If you're building AI systems that will need to operate in Connecticut and are unsure about compliance, the sandbox may be worth monitoring.

---

## Timeline Summary

| Date | What Kicks In |
|---|---|
| **October 1, 2026** | AEDT employer disclosure obligations; discrimination law amendment; frontier model whistleblower protections; AI layoff (WARN) disclosure |
| **January 1, 2027** | AI companion safety protocols and non-human disclosure; large frontier developer anonymous reporting channels and board notification |
| **October 1, 2027** | AEDT pre-decision individual notice; AEDT developer obligations; synthetic content C2PA provenance requirements |
| **January 1, 2028** | Social media personalized recommender restrictions for minors |

---

## Federal Preemption: Real But Not Legally Operative Yet

The Trump Executive Order from December 11, 2025 directed the DOJ to create an AI Litigation Task Force to challenge state AI laws deemed inconsistent with federal policy. The order also threatens conditional federal funding for states with "onerous" AI rules.

Two limits on this threat:

First, executive orders cannot preempt state law — only federal statutes or valid agency regulations with statutory authority can do that. There is no enacted federal AI law as of May 2026. Any preemption challenge requires federal legislation or a successful Supremacy Clause lawsuit. Neither exists yet.

Second, the executive order explicitly carves out child safety, AI compute and data center infrastructure, and state procurement as legitimate state concerns. Connecticut's companion chatbot and social media minor protection provisions are likely shielded from challenge under the order's own terms. Employment AI and the frontier model verification pilot are the provisions most likely to draw scrutiny.

The practical situation: companies subject to SB 5 must comply now. If federal law later preempts specific provisions, enforcement of those provisions would stop going forward. Building modular compliance infrastructure is lower risk than waiting for a federal preemption that may not materialize.

---

## Where Connecticut Sits in the Landscape

Connecticut is the third major US state AI law framework, after California's SB 53 and Colorado's SB 205 (passed April 2024). Each has a different architecture:

**Colorado SB 205** (effective February 1, 2026): Targets "consequential decisions" across six domains (employment, housing, credit, education, healthcare access, legal services) with a risk management approach. Applies to "high-risk AI systems" — broader category than Connecticut's sector-specific approach.

**California SB 53** (enforcement August 2026): Focuses on frontier model safety obligations and a new state AI safety agency (CALAI Office). Broader scope for frontier labs; no employment AI framework equivalent to Connecticut's.

**Connecticut AIRT Act** (staggered from October 2026): Five separate regimes. Narrower on frontier safety (whistleblower channels only, not full safety plans). Deeper on employment AI and companion chatbots than either of the others. First US state law to require C2PA provenance data.

With 1,200+ active AI bills across all US states and no federal preemption enacted, the compliance surface is fragmented. Companies building products that affect employment decisions, companionship/social engagement, or generative media now have to map their products against at least three significant state frameworks — more, depending on their product category and user geography.

---

## Builder Action Map

**If you build hiring or employment AI tools:**
- Audit whether your tool produces a "substantial factor" output in any employment decision affecting Connecticut employees or applicants. The threshold is intentionally broad.
- Update deployer contracts before September 30, 2026. Contracts need to explicitly allocate compliance duties and commit you to providing the structured compliance information package.
- Conduct anti-bias testing before October 1, 2026 and document the methodology. Courts will weigh whether testing was done, when, how, and what you did with the results.

**If you build AI companion chatbots:**
- Implement evidence-based suicide/self-harm detection before January 1, 2027.
- Design recurring non-human disclosure into your UX — not a buried onboarding checkbox. Hourly for minors, every 3 hours for adults.
- Build actual age assurance flows. The safe harbor requires a genuine determination that the user is 18+.
- Audit variable-ratio/interval reinforcement mechanics for minor users. This includes notification timing designed to drive re-engagement.

**If you build large-scale consumer generative AI (1M+ monthly users):**
- Implement C2PA metadata for AI-generated audio, images, and video before September 30, 2027.
- Define "material alteration" in your internal policy — what triggers the C2PA requirement vs. what counts as a minor edit.
- Audit which of your product lines are B2B (excluded) vs. consumer-facing (in scope).

**If you are a frontier model developer ($500M+ revenue, 10²⁶+ FLOP training):**
- Establish anonymous internal reporting channels before January 1, 2027.
- Post whistleblower rights notices and maintain them annually.
- Set up a board/director quarterly briefing process on catastrophic risk reports.

**For all builders doing business in Connecticut:**
- Map each product to the five regimes. This is not a single compliance checkbox.
- Do not rely on the 60-day AEDT cure period as a permanent buffer — it expires December 31, 2027.
- Engage employment counsel if AI-related headcount changes are in your plans — the WARN Act amendment applies now.
- Monitor the regulatory sandbox program for a potential testing pathway with reduced regulatory exposure.

---

*Related coverage:* [California AI Regulation 2026](/builders-log/california-ai-regulation-2026-crossover-builder-compliance-guide/) | [EU AI Act Digital Omnibus Deadline Extension](/builders-log/eu-ai-act-digital-omnibus-deadline-extension-builder-compliance/) | [OpenAI Frontier Governance Framework](/builders-log/openai-frontier-platform-governance-framework-enterprise-ai-builder-guide/)

