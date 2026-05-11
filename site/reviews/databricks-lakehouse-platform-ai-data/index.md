# Databricks Review: The AMPLab Spinout That Became the Enterprise AI Platform

> Apache Spark's creators built a $134B data platform used by 10,000+ enterprises. MLflow, Delta Lake, Unity Catalog — Databricks invented much of the open infrastructure that modern AI runs on. $5.4B ARR, 65%+ YoY growth, cash-flow positive, and eyeing a potentially record-breaking IPO. Here is what they built and whether it's worth it.


In 2009, a UC Berkeley PhD student named Matei Zaharia noticed something frustrating about Hadoop MapReduce. It worked well for one-shot batch jobs but was terrible for anything iterative — machine learning algorithms, interactive queries, anything that needed to touch the same data multiple times. Every iteration wrote intermediate results to disk. It was slow by design.

Zaharia spent the next few years building something faster. He called it Spark. By 2013, it was an Apache Top-Level Project and the fastest framework for large-scale data processing. The paper describing Spark received the ACM SIGOPS Hall of Fame Award in 2023 — the Turing Award of systems research.

That same year, seven AMPLab colleagues incorporated Databricks, Inc. to commercialize what they had built. Their pitch was simple: Spark is foundational infrastructure, enterprises need it, and they should not have to figure out how to run it themselves.

Twelve years later, Databricks is a $134 billion company with $5.4 billion in annual recurring revenue, growing at 65% year-over-year, free-cash-flow positive, and preparing for what would be the largest enterprise software IPO in history. They still have all three core founders in the executive suite. And they have expanded well beyond Spark.

---

## The Founding Team

Seven co-founders built Databricks, an unusually large founding group — but the density reflects their academic origins. All seven came from UC Berkeley's AMPLab (Algorithms, Machines, and People Lab), where they had been researching the intersection of large-scale distributed systems and machine learning before those topics had much overlap in industry.

**Ali Ghodsi** is CEO. He was a professor at UC Berkeley and at KTH Royal Institute of Technology in Stockholm before co-founding Databricks. He is Iranian-Swedish — born in Tehran, educated in Sweden. He has been the primary face of the company's growth and its rare willingness to take on Snowflake, AWS, Google, and Microsoft simultaneously in public.

**Matei Zaharia** is CTO. He created Apache Spark and MLflow. His academic work on distributed systems — now at MIT as a professor — continues to influence Databricks's product direction. He has the unusual quality of being a practitioner-researcher whose systems are actually used at scale.

**Ion Stoica** is Executive Chairman. He is a full professor at UC Berkeley and co-founded Anyscale, the company commercializing the Ray distributed computing framework, which he also co-created. His dual roles — active professor and executive chairman of a $134B company — are genuinely unusual.

The remaining co-founders — Reynold Xin, Patrick Wendell, Andy Konwinski, and Arsalan Tavakoli-Shiraji — contributed to both the technical and business foundations. Konwinski left day-to-day operations but was also a co-founder of Databricks competitor and customer Perplexity AI (he stepped back from Perplexity as well). Xin led architecture work on Spark and Databricks's SQL engine.

The full retention of original leadership — CEO, CTO, and Executive Chairman all still active founders — is extraordinary for a company twelve years old with 8,000 employees. It gives Databricks an unusual coherence of vision and avoids the "founder's departure" disruption that kills many mature startups.

---

## What Databricks Actually Does

The core product is the **Databricks Data Intelligence Platform** — what the company calls a Lakehouse.

The "lakehouse" concept, which Databricks coined, describes a specific architectural choice: take the flexibility and low cost of a data lake (raw files on cloud storage, typically S3 or Azure Blob) and add the reliability and performance guarantees of a data warehouse (ACID transactions, schema enforcement, query optimization). The result handles both the data engineering workloads (ETL, streaming, transformation) and the analytics workloads (SQL queries, BI, reporting) that organizations previously ran on separate systems.

In practice, this means customers use one platform to ingest raw data from operational systems, transform it into clean tables, run SQL analytics against it, build machine learning models on it, and now deploy AI agents that query it. The platform runs on all three major cloud providers — AWS, Azure, and GCP — and this cloud-agnosticism is a meaningful selling point for enterprises that have committed to multiple clouds or want negotiating leverage with their provider.

---

## The Open-Source Foundation

Databricks has funded the development of three open-source projects that became foundational infrastructure. This strategy — create the standard, then build the commercial layer on top — is the most effective approach to enterprise software moats.

**Apache Spark** is the origin. It is now the world's most widely used large-scale data processing framework. Databricks engineers remain among the top committers. The open-source project creates an enormous installed base of organizations that run Spark on their own infrastructure, and a smaller but significant portion of them eventually want a managed version — which is Databricks.

**Delta Lake** was created by Databricks in 2017 and donated to the Linux Foundation in 2019. It is a storage layer that adds ACID transactions, schema enforcement, schema evolution, and time travel (the ability to query historical versions of a table) to data lake storage. Delta Lake uses Apache Parquet files under the hood, which means it is not a proprietary format — the data remains accessible without Databricks. This was a calculated choice: customers are more willing to adopt a system where their data is not locked in.

**MLflow** was created by Matei Zaharia and released in 2018 as an open-source ML lifecycle platform. It handles experiment tracking (comparing model runs), model registry (versioning and staging trained models), and deployment. It now has 30 million monthly downloads and is backed by the Linux Foundation. MLflow 3.0, released in June 2025, was redesigned for generative AI — adding agent tracing, LLM evaluation, and observability for models deployed anywhere. You do not need Databricks to run MLflow. Its ubiquity is precisely the point: MLflow is the standard, Databricks is where you run it most conveniently.

More recently, Databricks open-sourced **Unity Catalog** (2024), the governance layer for managing access control, lineage, and discovery across all data assets. Open-sourcing a governance product may seem counterintuitive for a commercial company, but it positions Unity Catalog as the standard against which Snowflake's competing Horizon product is measured.

---

## Product Suite

The core platform has expanded into a full product family:

**Databricks SQL** is the SQL analytics layer, built on the **Photon** query engine — a vectorized engine written in C++ rather than JVM, which delivers significantly faster query performance than standard Spark SQL. Databricks SQL crossed $1 billion ARR as a standalone product line.

**Unity Catalog** is the governance layer. It manages access control, data lineage, audit logging, quality monitoring, and discovery for all data assets: Delta tables, Iceberg tables, unstructured files, ML models, functions, and MCP servers. It works with fine-grained permissions down to the row and column level.

**Mosaic AI** is the machine learning and AI platform, expanded significantly by the 2023 acquisition of MosaicML. It includes:

- **Model Training**: Train and fine-tune foundation models on enterprise data using the infrastructure developed for training GPT-4-class models.
- **MLflow**: Fully integrated, with GenAI-specific tracing and evaluation.
- **Agent Framework**: Build and deploy production AI agents backed by Unity Catalog data and security policies. GA'd in March 2025.
- **Agent Bricks**: Launched June 2025. Describe a task in natural language, connect enterprise data sources, and the system auto-generates synthetic training data, evaluates multiple approaches, and produces an optimized agent without writing architecture code.
- **Vector Search**: Managed vector database with a storage-optimized tier that handles billions of vectors at significantly lower cost than dedicated vector databases.
- **Genie**: Natural language interface for querying structured data. Ask business questions in plain English; Genie translates them to SQL, executes, and returns cited answers.

**Lakebase** (February 2026) adds OLTP to the platform. Via the acquisition of Neon, Databricks now offers serverless PostgreSQL fully integrated with the lakehouse — allowing transactional write workloads to coexist with analytical and ML workloads on the same data infrastructure.

---

## The Acquisitions

Databricks has made 17 acquisitions in twelve years. The most significant:

**MosaicML** ($1.3–1.4 billion, June 2023) was the pivotal deal. MosaicML had built infrastructure for training large foundation models efficiently — their MPT (MosaicML Pre-trained Transformer) series had demonstrated that high-quality models could be trained at a fraction of what OpenAI spent. The acquisition gave Databricks enterprise-grade model training capabilities and rebranded as Mosaic AI. It is the core of the company's generative AI product line.

**Tabular** (>$1 billion, June 2024) was founded by the original creators of Apache Iceberg — the competing open table format to Delta Lake. Rather than fighting a format war, Databricks acquired the competition. The result was Delta Lake's UniForm layer, which lets Delta tables be read as Iceberg tables by any Iceberg-compatible system. Snowflake's embrace of Iceberg was partly a defensive move against Delta Lake; Databricks responded by buying the people who invented Iceberg.

**Neon** (~$1 billion, May 2025) is a serverless PostgreSQL startup. The acquisition closed the OLTP gap — Databricks could handle analytical queries at any scale but had no transactional database. With Lakebase, a customer can now run their application database, data warehouse, and ML platform on a single vendor's infrastructure.

---

## The Snowflake Rivalry

No account of Databricks makes sense without addressing Snowflake. The comparison has defined enterprise data platform marketing for five years.

The original positioning was clear: Snowflake was for SQL analytics and business intelligence; Databricks was for big data engineering and machine learning. They served different buyers — Snowflake appealed to data analysts and SQL developers, Databricks appealed to data engineers and ML practitioners. Both were right that the other was not a direct competitor.

That ended around 2021–2022, when both companies expanded aggressively into the other's territory. Databricks built Databricks SQL and a collaborative notebook interface that appealed to analysts. Snowflake built Snowpark (Python in Snowflake) and acquired ML tooling. Both started calling themselves AI companies.

By 2026, the revenue figures are nearly identical — both near $5 billion ARR — but the growth trajectories have diverged sharply. Databricks is growing at 65%+ year-over-year. Snowflake is growing at 25–30%. The valuation gap reflects this: Databricks is valued at $134 billion as a private company while Snowflake's public market cap is approximately $50–60 billion.

The more important divergence is structural. Databricks has been free-cash-flow positive. Snowflake has been posting significant operating losses while growing more slowly. This combination — slower growth and worse unit economics — is difficult to explain to public market investors.

Databricks has also moved further toward the OLTP layer (Lakebase) that Snowflake has no answer for, while Snowflake's Iceberg strategy was partially neutralized by the Tabular acquisition. The rivalry continues, but the momentum has shifted.

---

## DBRX: Databricks's Open-Source LLM

In March 2024, Databricks released DBRX — a 132-billion-parameter open-weights large language model built by the Mosaic AI team.

DBRX uses a fine-grained Mixture-of-Experts (MoE) architecture. Unlike standard MoE models like Mixtral, which use a coarser routing, DBRX activates 36 billion parameters per forward pass across a more granular set of experts. The model was trained on 12 trillion tokens and achieves up to 2x faster inference than LLaMA 2 70B at comparable quality.

At release in March 2024, DBRX outperformed GPT-3.5, LLaMA 2 70B, and Grok-1 on standard benchmarks including MMLU, HumanEval, and commonsense reasoning. It was competitive with Gemini 1.0 Pro.

The benchmark context matters. The open-source LLM space has moved extremely fast. Llama 3, Mistral Large 3, and Qwen series models have been released since March 2024 and DBRX no longer represents the frontier of open-weights capability. Databricks has not released a DBRX 2. The company's apparent strategy is to position Mosaic AI's model training infrastructure for enterprise fine-tuning rather than competing directly in the frontier model race. Customers are expected to train their own models on Databricks infrastructure rather than primarily use DBRX off-the-shelf.

---

## MCP Integration

Databricks launched full Model Context Protocol (MCP) support in late 2025, and its implementation is among the most complete in enterprise software.

The offering includes **Managed MCP Servers** — hosted servers exposing Unity Catalog functions, Vector Search indexes, Genie Spaces, and custom functions to any MCP-compatible client. Enterprises can point Claude, Copilot, or any MCP client at a Databricks MCP server and give the AI access to governed enterprise data without writing custom integration code. Access control flows through Unity Catalog — permissions, audit logging, and lineage carry through to MCP calls.

The **MCP Catalog** (November 2025) is a discovery and governance layer for MCP servers themselves. Enterprises can publish, discover, and manage MCP servers within Databricks Marketplace, alongside pre-built connectors, ML models, and datasets.

The strategic logic is straightforward: if AI agents become the primary interface through which enterprise knowledge workers access data, the question of which data systems agents can reach becomes decisive. Databricks controlling the lakehouse layer and the MCP governance layer positions them as the infrastructure on which enterprise AI agents run.

---

## Funding and Financial Position

Databricks has raised approximately $20 billion across 14 rounds.

The Series J in late 2024 ($10 billion at a $62 billion valuation) was one of the largest private financing rounds in technology history. It was led by Thrive Capital and included Andreessen Horowitz, DST Global, GIC, Insight Partners, and others. Meta joined as a strategic investor when the round closed in January 2025.

The Series K (August 2025, $1 billion) was reported to be 20x oversubscribed — indicating substantial institutional demand that the company chose not to fully satisfy.

The Series L (December 2025, $4 billion at a $134 billion valuation) set the current benchmark. A subsequent $2 billion debt round in January 2026 brings total recent capital to approximately $7 billion across equity and debt.

On financial fundamentals:
- $5.4 billion ARR as of early 2026
- 65%+ year-over-year growth at that scale
- AI product line alone exceeds $1.4 billion ARR run-rate (~26% of total)
- Databricks SQL line exceeds $1 billion ARR separately
- Subscription gross margins exceed 80%
- Free cash flow positive over the trailing 12 months

The combination of 65% revenue growth and positive free cash flow at $5.4 billion scale is unusual. Very few software companies have ever grown this fast while generating cash, at this revenue level. The most direct comparable is Salesforce in its peak growth years, but Salesforce never achieved these growth rates at this revenue base.

Ali Ghodsi told CNBC in December 2025 he would "not rule out a 2026 IPO." Analysts expect an S-1 filing in the second half of 2026. At current metrics, a Databricks IPO would very likely be the largest enterprise software public offering in history.

---

## What the Platform Costs

Databricks uses a consumption-based pricing model via **Databricks Units (DBUs)** — normalized compute units billed by the second.

DBU pricing varies significantly by workload type: basic compute is approximately $0.07 per DBU, while GPU-accelerated enterprise workloads run $0.65 per DBU or higher. Customers also pay separately to their cloud provider (AWS, Azure, or GCP) for underlying virtual machines, storage, and egress. The "two-bill" dynamic — one to Databricks, one to the cloud — frequently surprises customers calculating total cost of ownership.

Three subscription tiers — Standard, Premium, and Enterprise — gate access to Unity Catalog governance, row/column-level security, audit logging, advanced ML lifecycle tooling, and enterprise support. Enterprise pricing is negotiated.

Typical spend ranges from approximately $500 per month for small data teams to millions of dollars annually for large enterprises with continuous processing workloads. For mid-market companies without dedicated data engineers, the cost and implementation complexity often make simpler alternatives more practical.

---

## Real Enterprise Deployments

With 10,000+ customers, Databricks has documented implementations across industries:

**Mastercard** built GenAI-powered customer support and an AI onboarding assistant on the platform. Unity Catalog provides governance across their global data operations.

**T-Mobile** processes hundreds of terabytes daily for network optimization and energy management, with Databricks as the core platform for data-intensive workloads.

**Fox Sports** built "Cleatus AI" — a natural language sports assistant that queries live statistics and generates on-air graphics via Genie.

**BP** deployed Unity Catalog for enterprise-wide data governance across multiple cloud environments.

**Mahindra & Mahindra** built a generative AI financial analyst that reduced routine task time by 70%.

The common pattern: Databricks serves as the platform on which enterprises build AI and analytics applications, not as an end-user interface. It is infrastructure for builders.

---

## What's Good

**Open-source credibility is genuine.** Databricks didn't just use open source as marketing. They created Apache Spark, Delta Lake, and MLflow — all now Linux Foundation or Apache projects — and continue contributing. This history means customers trust that their data formats will not be locked in.

**Financial fundamentals are exceptional.** 65%+ growth at $5.4 billion ARR while free-cash-flow positive is a rare combination. The business is not dependent on continued venture financing to operate.

**Expanding TAM.** The platform has grown from data engineering to SQL analytics to ML to AI agents to OLTP (Lakebase). Each expansion increases potential contract size and makes it harder for customers to justify adding a competing vendor.

**Open-source MCP is a strategic advantage.** First-mover enterprise MCP governance with Unity Catalog backing is a defensible position as AI agents become the primary data access layer.

**All three founders still running the company.** Leadership continuity at this scale and age is uncommon and has preserved strategic coherence across the product line.

---

## What's Not

**Cost unpredictability.** The DBU model combined with cloud provider billing makes total cost of ownership difficult to calculate in advance. This is a frequent complaint in enterprise procurement cycles and one Snowflake actively exploits in sales.

**Steep learning curve.** Effective use requires fluency across SQL, Python or Scala, distributed systems concepts, and MLOps practices. Small teams without dedicated data engineers often struggle.

**Not analyst-friendly.** The interface is built for data engineers and ML practitioners. Business analysts and non-technical users who want drag-and-drop experiences, embedded dashboards, or PowerPoint-style outputs are underserved. Snowflake's interface is more polished for this persona.

**DBRX has aged.** The March 2024 model was competitive at release but the open-source frontier has moved quickly. Databricks has not released a successor. This may be by design — the platform's value is in training infrastructure, not in shipping a frontier model — but customers evaluating the AI platform on model quality are looking elsewhere.

**Private company opacity.** Revenue figures and growth rates are press release numbers, not audited public financials. No independent verification is currently possible.

---

## Verdict

Databricks has earned its position as the central infrastructure layer for enterprise data and AI.

The open-source foundation — Spark, Delta Lake, MLflow — is the most durable competitive moat in enterprise software because it is genuinely not exclusive to Databricks. Competitors can run these tools too; customers choose Databricks because it manages them better, integrates them more completely, and adds governance that would be expensive to build independently. That is the right kind of moat: not lock-in, but meaningful operational advantage.

The financial picture is straightforwardly strong. At $5.4 billion ARR, growing at 65%, with positive free cash flow and institutional demand that oversubscribed the Series K 20 times, Databricks is not a story about potential — it is a story about a business that works.

The weaknesses are real. Cost complexity is a genuine operational burden, not a marketing problem. The learning curve limits the addressable market to organizations with data engineering sophistication. DBRX's aging is a real gap for customers who want a frontier model in their lakehouse, not just fine-tuning infrastructure.

The rating reflects a platform that is the clear enterprise choice for data-intensive organizations with the technical capacity to use it, priced appropriately for what it delivers, built on infrastructure that the industry as a whole depends on.

**Rating: 4/5.** The best enterprise data platform currently available for organizations with data engineering capacity. The cost complexity and non-technical user experience limitations are genuine, not hypothetical.

---

*ChatForest covers AI companies, tools, and ecosystems. Our reviews are based on public information, technical documentation, and independent research. We have no commercial relationship with Databricks.*

