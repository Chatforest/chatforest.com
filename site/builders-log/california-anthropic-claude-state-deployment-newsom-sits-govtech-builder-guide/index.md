# California Deploys Claude Statewide: What Government AI at Scale Looks Like for Builders

> California signed a deal June 29 giving every state agency and local government access to Claude at 50% off via a centralized portal. Here's what the SITeS model, the Poppy AI assistant, and government-scale Claude deployments mean for builders.


On June 29, 2026, California Governor Gavin Newsom [announced a deal](https://www.gov.ca.gov/2026/06/29/governor-newsom-announces-a-first-of-its-kind-partnership-providing-anthropic-tools-to-state-agencies-and-improving-services-for-californians/) giving every California state agency, plus every city and county that opts in, access to Anthropic's Claude at a 50% discount. The access comes with free workforce training and hands-on technical assistance from Anthropic developers, all routed through a centralized portal called SITeS — which the [California Department of Technology says](https://www.cdt.ca.gov/newsroom/2026/07/california-expands-ai-access-across-state-government-through-anthropic-partnership/) is the first AI productivity platform offered through that portal. Governor Newsom framed the deal as additive rather than a replacement for state workers: "AI should not replace the human work of government; it should help our workers move faster, solve problems more effectively, and deliver better results for Californians."

This isn't a pilot. The [California Department of Motor Vehicles, the California Department of Health Care Services, and the California Department of Technology are already running Claude in production](https://www.cdt.ca.gov/newsroom/2026/07/california-expands-ai-access-across-state-government-through-anthropic-partnership/). Statewide rollout of [Poppy](https://www.cdt.ca.gov/poppy/), California's Claude-powered AI assistant for state workers, is scheduled for July 2026.

For builders, this deal signals something bigger than a single procurement: the government market for AI tooling is arriving, and it has specific structural requirements that look nothing like SaaS sales to startups.

## What California Built: The SITeS Portal

The [Statewide Information Technology Shared Services (SITeS) portal](https://www.cdt.ca.gov/newsroom/2026/07/california-expands-ai-access-across-state-government-through-anthropic-partnership/), managed by the California Department of Technology, is California's centralized answer to AI procurement: state departments purchase Claude through it at the negotiated 50% discount, rather than each agency negotiating its own contract. CDT Deputy Director Tiffany Angulo put the rationale this way: "Bringing purchasing together through one statewide agreement saves time, reduces costs, and helps departments focus on using the tools."

State CIO Chris Given [described the goal](https://www.gov.ca.gov/2026/06/29/governor-newsom-announces-a-first-of-its-kind-partnership-providing-anthropic-tools-to-state-agencies-and-improving-services-for-californians/) as using "the state's purchasing power to make it easy to procure new tools, fast and for the best price." Claude is currently the first AI productivity platform offered through SITeS, with the portal structured to add other vendors over time.

**Builder implication:** If you want to sell AI tooling into California state government, you need to be in the portal. Direct sales to individual agencies still happen, but the SITeS model suggests the future of government AI procurement is centralized vetting, not individual deals. The question for any govtech AI builder is: what does it take to get onto a state's contract vehicle?

## Poppy: A Government AI Assistant That Doesn't Lock You In

Poppy is the most interesting technical artifact to come out of California's AI program. It traces back to a [2023 executive order](https://www.govops.ca.gov/generative-ai-genai-executive-order/) (Executive Order N-12-23) directing the state to study and pilot generative AI, [began piloting on September 29, 2025 with 2,800+ state employees across 67 departments](https://www.cdt.ca.gov/poppy/), and is entering statewide rollout in July 2026.

The design choices in Poppy are deliberate:

**Vendor-agnostic by architecture.** [Poppy supports multiple models — Claude, Gemini, GPT, and Amazon Nova — interchangeably](https://www.cdt.ca.gov/poppy/), without renegotiating contracts to swap between them. State workers don't pick a model — they pick a workflow template. The underlying model is an implementation detail.

**Pre-built query templates.** State workers use Poppy through purpose-built queries tailored to common government tasks: summarizing legislation, drafting public communications, processing forms, generating reports. This isn't a raw chatbot — it's a curated interface that constrains what the model can be asked to do, which addresses both safety and usability concerns simultaneously.

**Built by state workers for state workers.** The design principle is that domain expertise lives in the civil service, not in the vendor. Anthropic writes the model; California writes the prompts that shape how it gets used.

This architecture is a useful pattern for any enterprise AI deployment, not just government. The insight is that vendor flexibility and user simplicity aren't in tension — you can abstract the model behind domain-specific interfaces and let procurement teams make model substitutions independently of product teams.

## What California Is Actually Running Claude On

The [state's announcements](https://www.cdt.ca.gov/newsroom/2026/07/california-expands-ai-access-across-state-government-through-anthropic-partnership/) name three production deployments worth noting:

**CA DMV — customer service.** Claude is handling customer inquiries, reducing wait times, and improving service resolution, according to the state. No details on architecture have been published, but [DMV records](https://www.dmv.ca.gov/portal/news-and-media/dmv-statistics/) show roughly 35 million driver license/ID cardholders and 36 million registered vehicles statewide — this is high-volume, low-stakes (no life-safety decisions) text generation at government scale.

**CA Department of Health Care Services — Medicaid workflows.** DHCS administers Medi-Cal, [the largest state Medicaid program in the nation](https://www.kff.org/medicaid/medi-cal-managed-care-an-overview-and-key-issues/), covering more than 14 million Californians. Claude is used for internal workflows supporting case workers, per the state's announcement. Healthcare + government is a niche with strict HIPAA and state privacy compliance requirements — and almost no consumer AI tools built for it.

**CDT + CalOES — Claude Code for cybersecurity.** This one is the most technically interesting. [California's Department of Technology and the Governor's Office of Emergency Services are using Claude Security and Claude Code to strengthen cybersecurity, helping scan, triage, and patch state software](https://www.gov.ca.gov/2026/06/29/governor-newsom-announces-a-first-of-its-kind-partnership-providing-anthropic-tools-to-state-agencies-and-improving-services-for-californians/). The state's announcements don't specify whether this runs in an air-gapped environment or detail the human-review process before patches ship — see "What's Not Clear Yet" below.

## What the Trusted AI Procurement Executive Order Changes

On March 30, 2026, Newsom [signed Executive Order N-5-26](https://www.gov.ca.gov/2026/03/30/as-trump-rolls-back-protections-governor-newsom-signs-first-of-its-kind-executive-order-to-strengthen-ai-protections-and-responsible-use/), the Trusted AI Procurement order, directing the Department of General Services and CDT to develop new certifications for any AI vendor doing business with the state. Vendors will need to attest to their safeguards against illegal content (including CSAM and non-consensual imagery), harmful model bias, and violations of civil rights and civil liberties such as free speech, voting, and protection from unlawful surveillance; the order also lets state agencies override federal "supply chain risk" designations they find improper, adds suspension provisions for contractors that undermine privacy, and directs guidance on watermarking AI-generated content. Formal certification recommendations are due in July 2026 — the specifics are still being written, not yet finalized.

This executive order sits alongside two other pieces of California AI law: [AB 2013](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013), which requires generative-AI developers to publish training-data summaries, and [SB 53, the Transparency in Frontier Artificial Intelligence Act](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/), which requires frontier-model developers to publish safety frameworks and report critical safety incidents. Together they're a preview of what other states are likely to adopt as they build their own AI procurement and safety rules.

## What This Means for Builders

**Government is now a credible AI buyer.** The California deal isn't a proof of concept — it's a production deployment at scale, with a centralized procurement model and executive backing. Other states are watching. If you're building AI tools and haven't thought about the public sector, the addressable market just got larger.

**The Poppy pattern is reusable.** Vendor-agnostic AI assistants with curated, domain-specific interfaces and no dependency on any particular model provider are not just a government architecture. Any enterprise with model price sensitivity, regulatory risk, or multi-vendor contracts can build something like Poppy. The pattern is: abstract the model, expose domain workflows, let the model choice live in the config layer.

**Claude Code as a security tool is a production signal.** CDT using Claude Code to scan and patch state code is the first government-confirmed production use of AI code review for security in infrastructure at this scale. Builders working on AI-assisted security tooling now have a government reference case.

**Compliance burden is the real moat.** The Trusted AI Procurement EO is pushing state vendors toward certifications on bias, civil rights, and illegal-content safeguards. Most consumer AI tools aren't built for this. The builders who can ship compliant-by-design tools — with the audit logs, the data handling controls, and the procurement documentation regulators will eventually ask for — will access a market that isn't saturated.

**50% off isn't free.** The discount matters because government budgets are constrained and procurement processes are long. Even with a 50% discount, government agencies need justification documentation, budget cycle alignment, and approval chains. Builders who understand how to sell into this process — through contract vehicles, cooperative purchasing agreements, and procurement-friendly pricing models — have a structural advantage over builders who expect inbound demand.

## What's Not Clear Yet

California hasn't published benchmark data on the Poppy pilot beyond headcount and department count. The 2,800-person pilot across 67 departments is meaningful in scope, but without productivity data or error rates, it's hard to assess how well government-specific AI is performing versus generic productivity tools.

The Claude Code security use case at CDT is also under-documented. Whether this is running in an air-gapped environment, how patches are reviewed before deployment, and what liability framework applies when AI suggests a security fix that ships with a vulnerability — none of this is public. These are the questions every enterprise considering AI-assisted security tooling needs answered before production deployment.

## The Broader Signal

The California deal isn't primarily about California. It's a signal about the stage of enterprise AI adoption. When the country's most populous state deploys AI through a centralized procurement portal with a tiered toolset (worker productivity, domain-specific agents, security tooling), the technology has moved from experimentation to infrastructure. The builders who will capture the next wave of AI market growth are the ones building for organizations that need compliance, auditability, vendor flexibility, and training — not just raw capability.

---

*Sources: [Governor Newsom announcement](https://www.gov.ca.gov/2026/06/29/governor-newsom-announces-a-first-of-its-kind-partnership-providing-anthropic-tools-to-state-agencies-and-improving-services-for-californians/), [CDT newsroom release](https://www.cdt.ca.gov/newsroom/2026/07/california-expands-ai-access-across-state-government-through-anthropic-partnership/), [CDT Poppy page](https://www.cdt.ca.gov/poppy/), [Executive Order N-12-23 background](https://www.govops.ca.gov/generative-ai-genai-executive-order/), [Executive Order N-5-26 announcement](https://www.gov.ca.gov/2026/03/30/as-trump-rolls-back-protections-governor-newsom-signs-first-of-its-kind-executive-order-to-strengthen-ai-protections-and-responsible-use/), [AB 2013 bill text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013), [SB 53 announcement](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/), [DMV statistics](https://www.dmv.ca.gov/portal/news-and-media/dmv-statistics/), [KFF Medi-Cal overview](https://www.kff.org/medicaid/medi-cal-managed-care-an-overview-and-key-issues/), [TechCrunch](https://techcrunch.com/2026/06/29/anthropic-and-gov-newsom-forge-deal-allowing-california-government-to-use-claude-at-half-price/), [StateScoop](https://statescoop.com/california-agencies-get-access-to-anthropics-ai-tools-at-half-price/)*

