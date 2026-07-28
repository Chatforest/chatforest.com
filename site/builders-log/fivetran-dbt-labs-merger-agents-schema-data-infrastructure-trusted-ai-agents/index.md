# Fivetran + dbt Labs Complete Merger: The Data Layer AI Agents Actually Need

> Fivetran and dbt Labs completed their merger June 1, 2026, forming a combined company that approached $600M in annual recurring revenue at announcement and serves 100,000+ data teams. For builders, the key deliverables are Agents Schema (open standard for agent context), dbt Core v2.0 on Fusion (Apache 2.0, up to 10x faster parsing), and dbt State (30%+ compute cost reduction).


On June 1, 2026, Fivetran and dbt Labs [completed the all-stock merger](https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents) first [announced October 13, 2025](https://www.fivetran.com/press/fivetran-and-dbt-labs-unite-to-set-the-standard-for-open-data-infrastructure-2025), combining the leading data integration platform with the dominant data transformation tool into a single company focused on one problem: making your data safe for AI agents to act on.

The completion was timed to Snowflake Summit 2026, where the combined company showcased its first joint product releases. According to [Fivetran's 2026 Agentic AI Readiness Index](https://www.fivetran.com/resources/reports/the-2026-agentic-ai-readiness-index) — a survey of 400 data professionals — 60% of enterprises are already investing millions in agentic AI, but only 15% have a data foundation capable of supporting those workloads safely and effectively.

The merger creates a single vendor covering the full pipeline: ingest (Fivetran) → transform (dbt) → governed context (Agents Schema). At the [October 2025 announcement](https://www.fivetran.com/press/fivetran-and-dbt-labs-unite-to-set-the-standard-for-open-data-infrastructure-2025), the companies said the combined business was approaching $600M in annual recurring revenue. The [completed company serves more than 100,000 data teams](https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents) globally, including customers such as OpenAI, Zendesk, Coupa, and HubSpot.

**Leadership:** [George Fraser](https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents), Fivetran's co-founder and CEO, continues as CEO of the combined company. [Tristan Handy](https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents), dbt Labs' co-founder and former CEO, becomes President.

## What Changed on June 1

The merger closing day was not purely organizational. Several products shipped simultaneously:

**dbt Core v2.0 (alpha)** — The [Fusion engine runtime is now open source under Apache 2.0](https://docs.getdbt.com/blog/dbt-core-v2-is-here). The [Rust-based parser delivers up to 10x faster parse times](https://www.fivetran.com/blog/fivetran-dbt-an-open-agent-ready-future-for-data-teams) compared to the prior Python runtime, with new Parquet-backed artifacts (replacing heavy JSON files, [directly queryable via DuckDB](https://docs.getdbt.com/blog/dbt-core-v2-is-here) or any agent). Ships as two distributions: `dbt-core` (fully open source, Apache 2.0) and the Fusion binary (additional platform features, proprietary, free for local and production use).

**dbt Wizard (public preview)** — [Agentic development workflows inside dbt Studio](https://docs.getdbt.com/docs/dbt-ai/wizard-ide). The agent understands your project's models, lineage, metrics, and semantic context, and can build, validate, and iterate on transformations with you.

**AI Connector Agent (beta)** — [A Fivetran agent that reads API documentation and generates a Fivetran-managed connector in minutes](https://www.fivetran.com/blog/fivetran-dbt-an-open-agent-ready-future-for-data-teams). It crawls the docs, parses the API structure, generates the connector code, then validates and refines, with a human reviewing anything it can't handle cleanly. Output is a real Fivetran-managed connector — not custom code the customer has to maintain.

**dbt Docs v2** — [Redesigned documentation with Semantic Layer metadata, column-level lineage (Fusion only), and a REST API at `/api/v1/`](https://docs.getdbt.com/docs/build/view-documentation) so AI agents and MCP servers can query your dbt project metadata without requiring a browser session.

## Agents Schema: The Part Builders Should Not Miss

The most important deliverable for agent builders is **Agents Schema** — an open-source standard for providing governed context to AI agents.

The pattern is simple: create a dedicated schema called `AGENTS` in your data warehouse. Populate it with metric definitions, semantic models, dbt lineage metadata, and business documentation — in plain SQL tables. Publish those tables via GitHub Actions, metadata connectors, or custom integrations.

Any SQL-capable agent can then query the `AGENTS` schema directly, using your own warehouse credentials and governance rules. The context lives in infrastructure you already control and audit. No new vendor system. No new infrastructure to operate. Compatible with any warehouse, any ingestion tool, and any LLM.

The practical builder implication: your agents stop hallucinating metric definitions because they read the canonical definition from the same source your analysts use. Token efficiency improves because the context is structured and dense. Governance teams can audit what context the agent accessed via the same access logs already in place.

Agents Schema is open source and open format, [maintained and published by Fivetran](https://www.opendatainfrastructure.com/agents-schema), with implementation examples in the [`fivetran/agents_schema` GitHub repo](https://github.com/fivetran/agents_schema).

## dbt State: 30% Cheaper Pipelines

**dbt State** is now in preview. It acts as a caching layer: instead of rebuilding every model on every pipeline run, dbt State checks whether the logic and underlying data have changed. If neither has changed, the node is skipped or cloned.

[Across production runs, dbt State reduces dbt-generated compute by more than 30% on average](https://www.fivetran.com/blog/fivetran-dbt-an-open-agent-ready-future-for-data-teams) without affecting data quality or freshness guarantees.

This is material for teams running dbt on large warehouses where compute costs are a real line item. The savings come automatically — no change to your model definitions or pipeline configuration required.

## Why This Merger Happened Now

The timing is not arbitrary. The data infrastructure layer was fragmented at exactly the moment when AI agents need it to be coherent.

Fivetran's position: it [connects to 700+ sources](https://fivetran.com/docs/connectors) and keeps data current in the warehouse. dbt's position: it models and documents what that data means. Those two functions were separately managed — different contracts, different CLI tools, different operational models — even though every serious data team used both.

For AI agents, the gap between "data is in the warehouse" and "data is trusted and interpretable" is exactly where production deployments break down. An agent that reads raw tables without semantic context will produce wrong answers confidently. An agent with access to dbt's lineage, semantic models, and documentation can reason correctly about what metrics actually mean.

The merger is a bet that data teams want a single vendor to own this pipeline rather than coordinating two products indefinitely. The competitive pressure comes from Snowflake (which [announced Snowflake CoCo](https://www.snowflake.com/en/news/press-releases/snowflake-coco-redefines-enterprise-ai-development-as-the-coding-agent-built-for-faster-easier-and-more-powerful-innovation-anywhere/) and [Cortex Training](https://chatforest.com/builders-log/snowflake-summit-26-cowork-coco-cortex-training-sense-datastream-builder-guide/) at the same Summit), Databricks, and newer data mesh platforms that are beginning to target the same governed-context-for-agents problem.

## What This Means for Builders

**If you already use both Fivetran and dbt:** The merger is immediately beneficial. Your contracts consolidate, the products share a common identity model, and Agents Schema gives you a standard way to surface your transformations to agents. Adopt dbt State in preview now — 30% compute reduction has a fast payback.

**If you use dbt but not Fivetran:** The AI Connector Agent is worth evaluating. If you've avoided Fivetran because adding a new managed connector was slow and expensive, the AI Connector Agent changes that calculus. Evaluate it against whatever ingestion tooling you use today.

**If you're building agents that need to reason about business data:** Agents Schema is the most important new open standard in the agent ecosystem this month. It gives you a customer-owned, warehouse-native context layer that is both more trustworthy than retrieval from unstructured docs and cheaper than feeding full table schemas into every prompt. Read the spec, then build the AGENTS schema from your existing dbt project — the tooling is already there.

**If you're evaluating open-source vs. proprietary dbt:** dbt Core v2.0 is now the Fusion engine under Apache 2.0. The gap between open-source and cloud dbt has narrowed. Teams that stayed on `dbt-core` for vendor-lock reasons can now upgrade to the Fusion runtime without changing their license position.

**If you're on the fence about warehouse-native development:** Snowflake CoCo, dbt Wizard, and the new Agents Schema standard all push in the same direction — build closer to the data, not in a separate application layer that has to sync back. If you've been moving ETL logic into your application code to avoid warehouse dependency, the tooling and economics are now pushing back the other way.

## Where This Leaves the Competitive Map

The combined Fivetran + dbt entity now competes directly with:

- **Snowflake** on the development experience layer ([Cortex Code / CoCo was announced at the same Summit](https://www.snowflake.com/en/news/press-releases/snowflake-coco-redefines-enterprise-ai-development-as-the-coding-agent-built-for-faster-easier-and-more-powerful-innovation-anywhere/))
- **Databricks** on the open lakehouse + transformation stack
- **Airbyte + Metricflow** combinations for teams that assembled similar capabilities open-source

The key differentiator the merged company claims: open data infrastructure. Agents Schema is open source. dbt Core v2.0 is open source. Fivetran connectors are managed and proprietary, but the output (data in your warehouse) is yours. The strategy is to avoid the pattern where AI infrastructure becomes a closed moat — while still generating revenue on the cloud platform features.

Whether that holds as the company scales is a question for later. For now, the suite is intact, the specs are open, and the data infrastructure gap for agentic AI just got significantly narrower.

