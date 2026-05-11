# Scale AI Review: The Data Labeling Giant That Became America's Defense AI Infrastructure

> Alexandr Wang dropped out of MIT at 19, built a $29B data labeling empire, then handed the keys to Meta for $14.3B while heading to run superintelligence research. Scale AI went from RLHF supplier to every major AI lab to the Pentagon's preferred AI data contractor — with a $500M defense deal just awarded. Here is how they got there and what it costs them.


In 2016, a 19-year-old MIT dropout named Alexandr Wang noticed something broken about how machine learning teams got their data labeled. Companies with autonomous vehicle programs were hiring armies of contractors in piecemeal fashion, tracking annotations in spreadsheets, and rebuilding quality-control processes from scratch for every project. The tooling was custom, slow, expensive, and not particularly reliable.

Wang and his co-founder Lucy Guo built Scale AI to fix that. The premise was a marketplace: connect companies that needed data labeled — images, text, video, lidar scans — with a distributed workforce of annotators who would do the work through a managed API. You called the API, the humans labeled it, quality checks ran, you got clean training data. The bottleneck that slowed down every ML project became a service.

That bet looks obvious in retrospect. It was not obvious in 2016. The autonomous vehicle boom was early. Deep learning was ascending but had not yet exploded into the generative AI era. And a teenage MIT dropout with no enterprise track record had to convince serious research teams to outsource a foundational part of their ML pipeline to a startup.

Ten years later, Scale AI has $2 billion in annual revenue growing at 130% year-over-year, a $29 billion valuation, and a $500 million Pentagon contract awarded in May 2026. Wang himself left the company in June 2025 to become Meta's Chief AI Officer. The data labeling startup he built is now, quietly, one of the most consequential pieces of AI infrastructure in the United States.

---

## The Founding Team

**Alexandr Wang** was 19 when he co-founded Scale and had just left MIT after one semester. He had interned at Hudson River Trading, working on high-frequency trading systems, which gave him an early intuition for building pipelines that needed to handle massive throughput with extreme reliability. He met Lucy Guo while they were both working at Quora.

**Lucy Guo** was a product designer at Quora and Pinterest before Scale. She left the company in 2017, approximately a year after founding, reportedly due to interpersonal friction with Wang. Guo went on to found two other companies. The public history of Scale AI is therefore largely the story of Wang as the sole remaining founder-operator.

Wang did not become famous by accident. He was an extraordinarily effective communicator of Scale's strategic position — rare for a founder who built infrastructure rather than consumer products. When Forbes named him the youngest self-made billionaire in 2021 at age 25 (a $7.3 billion Series D valuation implied a stake worth over $1 billion), the narrative around Scale shifted from "data labeling company" to "the infrastructure company where all of AI is trained."

That narrative was directionally accurate, which is why it stuck.

**Jason Droege**, who became Interim CEO after Wang's departure in June 2025, was previously Scale's Chief Strategy Officer and founder of Uber Eats. Droege has operational scale at the level Scale needed — Uber Eats built a global logistics network under extreme timeline pressure. Whether he can carry forward the strategic positioning that Wang established is the open question inside Scale right now.

Wang himself sits at Meta as Chief AI Officer, heading Meta Superintelligence Labs. He is simultaneously one of Meta's most senior technical executives and Scale's most famous alumnus working at its largest investor. The dynamics there are unusual.

---

## What Scale AI Actually Does

Scale's original product is **data labeling infrastructure**. You have images, text, audio, video, sensor logs, or any other raw input that needs to be annotated before it can train a model. Scale provides the API, the workforce, and the quality control to get that done at scale.

The actual labeling is done through two subsidiaries. **Remotasks** handles computer vision, autonomous vehicle, and spatial data work — the original market. **Outlier** (formerly Scala and Surge, then reorganized under Scale) handles the LLM-era work: evaluating AI outputs, providing human feedback for RLHF training, red-teaming model responses. Outlier primarily pays knowledge workers rather than general-purpose crowd workers; the tasks require higher skill.

The core **Scale Data Engine** product wraps the annotation pipeline with tooling for data collection, curation, review, and iteration. Enterprise customers use it to manage end-to-end training data quality for their ML systems. The first 1,000 labeling units are free; enterprise pricing starts around $93,000 per year and scales to $400,000 or more for large deployments. Pricing is negotiated rather than published, which means the sales cycle is long.

From this foundation, Scale built four additional major product lines:

**Scale Evaluation** (SEAL — Safety, Evaluations, and Alignment Lab) provides adversarial testing, red-teaming, model benchmarking, and safety assessments. This is higher-margin work than annotation. Customers include OpenAI, Google DeepMind, and national AI Safety Institutes. The US AI Safety Institute has contracted Scale for model evaluation work. Summer Yue, former RLHF research lead for Bard at Google DeepMind, leads the division.

**Scale Donovan** is Scale's defense product: a natural language interface to battlefield data, deployed on classified military networks including SIPRNet and JWICS. It allows military commanders to query real-time operational data using plain language rather than specialized database interfaces. Scale was the first AI company to deploy an LLM on a classified DoD network, in 2023.

**Defense Llama**, co-developed with Meta in January 2025, is a national-security LLM built on the Llama 3 architecture. It is purpose-built for military applications.

**Thunderforge** is a March 2025 DoD prototype for an AI agent system that helps plan and execute military asset movements — ships, planes, and ground assets. It is described internally as the DoD's flagship AI agent program. Scale is embedded alongside Microsoft and Anduril in this effort.

The most recent product additions are **Scale Labs** (March 2026), an expanded research division that publishes benchmarks including SWE-Atlas for coding agents and Voice Showdown for multilingual voice AI evaluation, and **Agentex**, an open-sourced enterprise framework for building and managing long-running AI agents.

---

## Funding and the Meta Deal

Scale's funding history is a clean timeline of the AI funding cycles that shaped the 2020s.

The company was seed-funded by Y Combinator in 2016, Series A by Accel in 2018 ($4.5M), Series B by Accel and Index Ventures in 2019 ($18M), and Series C by Tiger Global and Coatue in 2020 ($155M). The Series D came in 2021 at $325M, led by Tiger Global, at a $7.3 billion valuation — the round that made Wang a billionaire at 25.

In May 2024, Accel led a roughly $1 billion round at $13.8 billion, with Amazon, Meta, Cisco, and ServiceNow participating. Total raised before the Meta deal: approximately $1.6 billion in equity.

Then, in June 2025, Meta announced a $14.3 billion strategic investment for a **49% non-voting stake** in Scale, at a post-money valuation of $29 billion. This was not an acquisition — Scale remained an independent company with its own board and management. Meta got a large economic interest without control. The deal provided substantial liquidity to existing shareholders and funded Scale's defense expansion.

The non-voting structure was deliberate. Scale's government contracts — particularly the classified work with DoD — require that the company maintain independence and US control. A voting stake would have complicated that.

The deal was transformative. It was also immediately damaging to Scale's commercial relationships.

---

## The Commercial Client Exodus

Within weeks of the Meta deal's announcement, Scale's other major AI lab clients began severing or winding down their relationships. The logic was straightforward: those companies — Google, OpenAI, Microsoft, xAI — are Meta's direct competitors. Training data strategy and model development direction are competitive secrets. Having Meta hold a 49% stake in the company that handles your RLHF pipeline is a material risk.

**Google**, which had been spending approximately $150 million annually with Scale and had planned to increase to $200 million in 2025, announced plans to cut ties. It is the most dramatic loss — Google was Scale's largest commercial customer.

**OpenAI** began phasing out Scale AI work after the Meta deal, shifting volume toward other vendors. This was a significant relationship: Scale had been a major RLHF partner for OpenAI since the early ChatGPT training efforts.

**Microsoft** and **xAI** also began winding down their Scale relationships.

The Meta deal replaced all of this revenue with a single large strategic relationship — plus the defense expansion. But the trade-off fundamentally changed Scale's competitive position in the commercial AI training market. Scale went from being the neutral infrastructure layer that every lab used to being, effectively, Meta's data operation with a government contracts business attached.

Surge AI — rebranded Mercor — is the primary beneficiary. Its valuation jumped from $2 billion in February 2025 to $10 billion by October 2025, a five-fold increase in eight months driven directly by the clients Scale lost.

---

## The Defense Bet

Scale's pivot to government and defense is the most consequential strategic decision in its history — and it preceded the Meta deal by two years.

The logic is compelling. Government AI budgets are large and growing. The DoD wants AI in operational systems but lacks the technical infrastructure to build and maintain it. Commercial AI vendors are often reluctant to take on the cleared-personnel requirements and bureaucratic overhead of government contracts. Scale was willing, and Donovan gave them a concrete defense product rather than just labeling services.

The contract progression tells the story:
- **2023**: First classified DoD contract; Donovan deployed on SIPRNet and JWICS
- **May 2024**: $100M OTA agreement with the Pentagon
- **2024**: $99M Army contract (Army Contracting Command, Aberdeen Proving Ground)
- **March 2025**: Thunderforge prototype; DoD describes it as the flagship AI agent program
- **September 2025**: $100M five-year Pentagon agreement
- **May 2026**: Pentagon expands that contract to a **$500M ceiling**, five times the original cap, citing demand that exceeded projections

The $500M expansion is the headline that Scale will use to define this era. It is the largest AI data contract the DoD has awarded, and it covers a service — AI data processing, evaluation, and decision support — that the military now treats as operational infrastructure.

Alexandr Wang's January 2025 open letter to the Trump administration — "America must win the AI war," published in a full-page Washington Post ad on Inauguration Day — reads differently in this context. Wang met with White House officials and Congress members in February 2025. The advocacy was strategic: Scale's defense business depends on continued political will to fund AI programs, and Wang was positioning Scale as the patriotic AI infrastructure choice. Whether that advocacy was cause or effect of the $500M contract expansion is unknowable from the outside. The correlation is clear.

---

## Revenue and Scale

Scale's financial trajectory is exceptional by any measure.

Revenue reached approximately $870 million in 2024, with an annualized run rate near $1.5 billion by year-end. In 2025, Scale hit $2 billion in full-year revenue — 130% year-over-year growth. The company described 2025 as its "strongest financial year ever." New contracts signed in 2025 exceeded $1 billion.

The core data business turned free-cash-flow positive in 2025. The applications business (Donovan, defense products, SEAL) more than doubled in the second half of the year.

At $2B revenue and growing at 130% YoY, Scale is one of the fastest-growing companies at that scale in enterprise software. For context, Databricks is growing at 65% YoY at $5.4B revenue and that rate is considered extraordinary. Scale at 130% growth at $2B is in a different tier.

The caveat is that commercial AI lab revenue is now concentrated rather than diversified. Meta is both the largest investor and, through its own direct relationship, a primary customer. If that relationship deteriorates — and TechCrunch reported early cracks in August 2025 — the revenue concentration risk is severe.

---

## The RLHF Pipeline and Competition

Scale's data labeling market sits within a broader ecosystem projected to reach $17.1 billion by 2030 at 28% annual growth. The competitive picture has changed significantly since 2022.

**Appen**, the legacy leader in annotation services, generates around $231M in trailing revenue. It is roughly one-tenth of Scale's size and growing slowly. The generative AI era has not revitalized Appen the way it did Scale.

**Labelbox** competes as a platform rather than a crowd labor provider. It sells tooling for companies that want to manage their own annotation workforce, rather than outsourcing to Labelbox's crowd. This is a different enough model that Labelbox is more a complement than a direct competitor in enterprise contexts.

**Surge AI / Mercor** is Scale's most direct LLM-era competitor. It focuses on the same RLHF and model evaluation work that Outlier does. Its $10B valuation — up 5x in eight months — reflects the Google, OpenAI, and Microsoft business it absorbed from Scale. Surge/Mercor will be a serious competitor in the commercial AI training market for years.

**Hyperscalers building in-house** is the deepest structural challenge. Google, OpenAI, and Anthropic have all been building internal RLHF teams and annotation pipelines. The Meta deal accelerated this — nothing motivates building in-house capacity like losing confidence in your current vendor. At the frontier model level, AI labs will increasingly own their training data pipelines.

Scale's strategic answer is that evaluation and defense are harder to replicate in-house than annotation. You can hire annotation staff. You cannot easily replicate a classified network deployment relationship with DoD, or a trusted-third-party evaluator relationship with regulators and AI Safety Institutes. This is where Scale is betting its moat lies.

---

## Labor Practices Controversy

Scale's rapid growth has been built on a distributed annotator workforce — and the conditions for those workers are a serious, documented problem.

Scale operates Remotasks as the primary vehicle for lower-skilled annotation work. Remotasks has had significant issues:

In early 2024, Remotasks abruptly terminated operations in Kenya, Nigeria, and Pakistan without adequate notice to workers, many of whom had built their livelihoods around Remotasks income. Scale claimed advance notice was provided, but acknowledged it failed to reach Kenyan contractors. Workers arrived at their systems to find accounts deactivated.

The Oxford Internet Institute's 2023 evaluation of crowdwork platforms gave Remotasks 1 out of 10 on worker protections. AI data workers wrote to President Biden in 2024 calling conditions "modern day slavery," citing pay of approximately one cent per task for work that could take hours.

In December 2024 and January 2025, two separate lawsuits were filed: one alleging wage theft and worker misclassification, the second alleging that contractors were exposed to violent, sexual, and otherwise disturbing content during model training tasks with no adequate psychological support or disclosure.

The US Department of Labor opened an investigation into Scale AI, confirmed as active in August 2024 and ongoing through early 2025.

The House Judiciary Committee sent Wang a letter in March 2025 requesting information about AI censorship practices related to how Scale's data labeling might influence political outputs from AI models.

These are not fringe concerns. They are documented, ongoing, and legally active. Scale's public response has been limited to acknowledging specific incidents and pointing to revised contractor policies. The structural dynamic — a company generating billions in revenue from distributed workers paid fractional dollars per task — has not changed.

---

## Model Context Protocol (MCP)

Scale AI does not have an official first-party MCP server.

The company's enterprise products — Donovan, Data Engine, Scale Evaluation — are delivered through proprietary APIs and SDKs, not through standardized protocols like MCP. The agentic AI work under Agentex uses Scale's own tooling.

Third-party: Composio, an integration platform, has built an MCP integration for Scale AI that allows AI agents to interface with Scale's data platform through Claude, Cursor, and other MCP-compatible clients. This is a community integration, not an official Scale AI product.

For a company that builds AI agent infrastructure (Agentex) and claims a leading position in the agentic AI evaluation space, the absence of a first-party MCP server is a notable gap. Donovan and Scale Labs both operate in contexts where MCP could enable interoperability with the broader agent ecosystem. This is likely to change.

---

## What the Meta Deal Changed

The Meta deal is the organizing event that divides Scale's history into before and after.

Before: Scale was the neutral infrastructure layer that every major AI lab used. Google, OpenAI, Microsoft, Meta, Anthropic — all were customers. Scale's value proposition included independence: your training data would not leak to your competitors.

After: Meta holds 49% economic interest. Commercial AI labs view Scale as Meta's data operation. The commercial AI training market is, for Scale, largely lost. Scale is now primarily a government/defense AI infrastructure company that also services Meta and enterprise clients.

This is not obviously a bad outcome. Defense is a larger and more durable market than commercial AI training for frontier models. The $500M Pentagon contract is more stable than relationships with AI labs that are building in-house capacity anyway. The Meta investment provides capital and a stable anchor relationship.

But it is a fundamentally different company than the one Wang founded or the one that had Google as its largest customer in 2024. The pivot was largely forced rather than chosen — Meta's money accelerated a transition that the commercial client exodus would have created more slowly anyway.

Wang's move to Meta as Chief AI Officer is the final chapter of that transition. The founder who built the commercial Scale AI is now embedded in the investor that transformed it into a defense-first company. Jason Droege runs an organization oriented around Pentagon contracts and Meta's training pipeline, not the neutral data marketplace that Wang originally envisioned.

---

## Verdict

Scale AI is in an uncomfortable transitional position that its strong financials do not fully describe.

The $2B revenue and 130% growth look exceptional. The $500M Pentagon contract is a remarkable validation of the defense bet. Wang's instinct that evaluation is a more defensible moat than annotation was correct. Scale Labs and the benchmarking work are genuinely important — good AI evaluation is harder than it looks, and there is real demand for trusted third-party assessment of model quality and safety.

But the Meta deal restructured Scale's competitive position in ways that are still playing out. Google, OpenAI, Microsoft, and xAI all walked. The commercial AI training market that Scale dominated in 2023 belongs, increasingly, to Surge/Mercor and to in-house teams. Scale's defense business is impressive but politically dependent — contracts can be restructured, administrations change, and the DoL investigation adds legal overhang.

The labor practices issues are serious and unresolved. Paying annotators fractions of cents per task while generating billions in revenue from their work is a material ESG and legal risk, not just bad optics. The active Department of Labor investigation and the psychological harm lawsuit represent genuine exposure.

And the company is now being run by a CEO who was not the founder, reporting to a board that includes a 49% stakeholder who is also the largest customer. The alignment pressures on Droege are complex.

Scale at its best is genuinely important infrastructure — the company that built the RLHF pipelines and evaluation frameworks that made modern AI work. At its current stage, it is a defense-oriented AI services company with a complicated ownership structure, documented labor controversies, and strong but concentrated revenue.

For enterprises building AI systems that need third-party evaluation or specialized training data, Scale Evaluation (SEAL) is the strongest independent offering in the market. For government and defense contexts, Scale Donovan and the Pentagon contracting relationship are without peer. For straightforward annotation and labeling at volume, the competitive landscape has diversified enough that Scale is no longer the only credible option.

**Rating: 4/5** — The evaluation and defense moats are real, the revenue growth is exceptional, and the MCP/agentic tooling is evolving. Deductions for the commercial client exodus following the Meta deal, serious and ongoing labor practice controversies, founder departure, and defense revenue concentration that creates political dependency.

---

*Scale AI is headquartered in San Francisco. Scale Donovan and defense products are classified and not publicly documented beyond what is described in official government contract awards and press releases. Worker compensation figures are based on investigative reporting by Rest of World and Oxford Internet Institute research.*

