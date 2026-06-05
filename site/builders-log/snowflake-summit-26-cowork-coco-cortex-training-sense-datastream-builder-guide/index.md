# Snowflake Summit 26 Wrap: CoWork, CoCo, Cortex Training, Cortex Sense, and the Agentic Data Platform Builder Guide

> Snowflake Summit 26 (June 1-4, San Francisco) ended with Snowflake renaming its two flagship AI products and shipping five new capabilities. Here's what every builder needs to know: what CoWork and CoCo actually are, what Cortex Training unlocks, and how Datastream + OpenFlow change real-time AI pipelines.


Snowflake Summit 26 ran June 1–4 in San Francisco with 20,000 attendees. The opening keynote featured Anthropic President Daniela Amodei alongside Snowflake CEO Sridhar Ramaswamy. The builder keynote landed June 3.

The headline outcome: Snowflake shipped five significant new capabilities and renamed both of its primary AI products. If you track Snowflake and built your understanding before this summit, some product names have changed and some capabilities are materially different.

This is the builder summary — what shipped, what it does, and when to use it.

---

## The Two Renames That Matter

### Snowflake Intelligence → CoWork

**Snowflake Intelligence** is now **Snowflake CoWork**. The product is a personal AI agent for knowledge workers — natural language queries, multi-step reasoning across enterprise data, action execution. The rename signals a positioning shift: Intelligence was a feature name; CoWork is a product name aligned with workplace AI agents like Microsoft Copilot and Google Workspace AI.

CoWork is powered by Claude. It uses Snowflake's governed data environment for grounding, which means queries stay inside your data perimeter rather than hitting external APIs with extracted copies of your data.

New capabilities announced at Summit:
- **Cortex Sense** — shared enterprise context layer (details below)
- **User Memory** — personalization layer that learns from individual behavior, enables scheduling, and delivers proactive recommendations based on role
- **Artifacts** — structured output objects from CoWork sessions, analogous to Claude's Artifacts feature
- **User Skills** — teams can define and automate their own workflows inside CoWork
- **Prebuilt role plugins** — finance, sales, and other function-specific skill bundles combining business logic, data definitions, and MCP connectors

Early adopters using CoWork in production: Synopsys, WHOOP, Under Armour.

### Cortex Code → CoCo

**Cortex Code** is now **Snowflake CoCo**. The product is Snowflake's AI coding agent — it generates, explains, and deploys code against Snowflake data, tables, and applications. CoCo is Snowflake's fastest-growing product: 7,100+ users before the rename.

New CoCo capabilities at Summit:
- **Native desktop app** — no longer browser-only
- **IDE extensions**: VS Code, Microsoft Excel, Claude Code
- **Mobile access** — CoCo available on mobile devices
- **Slack integration** — CoCo in Slack channels and DMs
- **Autonomous task mode** — CoCo can execute multi-step tasks without continuous user oversight
- **End-to-end app deployment** — build in CoCo, deploy to Snowflake directly

The "goes everywhere" positioning mirrors how Cursor and GitHub Copilot extended from IDE to browser and mobile. CoCo is building the same surface area, but anchored to Snowflake's governed data environment rather than generic code generation.

Early adopters: Fanatics, Thomson Reuters, WHOOP.

---

## What's New: Five Capabilities That Matter

### 1. Cortex Sense — The Enterprise Context Layer

**Cortex Sense** is a new context aggregation capability that automatically assembles what AI agents need to produce trustworthy answers: data definitions, business logic, operational policies, and domain knowledge. It surfaces this unified context to both CoWork and CoCo, so you are not managing separate context configurations for your work agent and your coding agent.

The builder problem Cortex Sense solves: agents that query enterprise data without business context produce technically correct but operationally wrong answers. A query against a revenue table without knowing whether "revenue" means gross or net, whether Q1 refers to fiscal or calendar, or whether a given customer segment is excluded from certain calculations will generate answers that mislead rather than inform.

Cortex Sense includes prebuilt plugins for finance, sales, and other enterprise functions. Each plugin bundles the skills, business logic, and MCP connectors for that domain.

**Builder read:** If you are building enterprise agents on Snowflake, Cortex Sense is the governance layer that separates "AI that answers questions" from "AI that answers correctly." The prebuilt plugins give you a starting point; you extend with your organization's specific definitions and policies.

---

### 2. Cortex Training — Fine-Tune Models on Your Data, on Snowflake GPUs

**Cortex Training** lets enterprise data teams fine-tune open-weight foundation models directly inside the Snowflake environment using Snowflake-managed GPU infrastructure. Supported model families at launch: Qwen and Mistral.

The key architectural point: your training data stays inside Snowflake's governance boundary during fine-tuning. You are not exporting data to an external training service and inheriting that service's data handling policies.

This matters for:
- Enterprise data that cannot leave a specific compliance perimeter
- Proprietary domain data (clinical, legal, financial) where training on external infrastructure creates regulatory risk
- Organizations that have invested in Snowflake governance infrastructure and want fine-tuning to inherit those controls

The tradeoff: you are limited to the model families Snowflake supports and Snowflake's managed GPU capacity. If you need to fine-tune GPT-4o-class models or require dedicated training infrastructure, Cortex Training is not the right tool.

**Builder read:** Cortex Training is specifically useful if (1) your data perimeter is a real constraint, not just a preference, and (2) Qwen or Mistral families are viable for your use case. If you are already running fine-tuning on Azure, AWS, or GCP with acceptable governance, Cortex Training does not give you a clear reason to switch.

---

### 3. Snowflake Datastream — Managed Apache Kafka for AI

**Snowflake Datastream** is a fully managed Apache Kafka-compatible streaming service embedded in Snowflake. It enables real-time data pipelines that feed AI agents without requiring you to maintain separate Kafka infrastructure.

Before Datastream, real-time data for Snowflake-based agents typically required:
- A separately managed Kafka or Confluent cluster
- Connectors between Kafka and Snowflake
- Separate operational overhead for the streaming layer

Datastream collapses this. Data flows into Snowflake in real time, with the governance and security controls you have already configured. Agents querying CoWork or running through Cortex Agents see current data, not batch-delayed snapshots.

**Builder read:** Datastream matters most if your agents need to act on recent events (fraud alerts, supply chain signals, market data) rather than historical analysis. If your current agent use cases are retrospective or operate on daily batch data, Datastream is not urgent. If you have been maintaining a Kafka-to-Snowflake connector, evaluate whether Datastream simplifies your stack.

---

### 4. OpenFlow — Unified Data Integration

**OpenFlow** is Snowflake's data integration product for AI workloads — ETL but designed around agent data needs rather than traditional analytics batch patterns. OpenFlow handles data movement from any source into Snowflake through a unified platform with extensibility for custom connectors.

The positioning is "ETL for AI": not just moving data, but moving it in the format, at the cadence, and with the metadata that AI agents need to use it effectively.

OpenFlow works alongside Datastream (streaming) to provide the full data movement picture: batch/incremental loads via OpenFlow, real-time streams via Datastream.

---

### 5. Open Framework — Live, Governed Data Without Movement

The Open Framework is Snowflake's interoperability play. The core claim: enterprises can now work on a single, live, governed copy of their data regardless of where it physically resides — Snowflake, external data lakes, or open systems — without moving or duplicating it.

Components:
- **Apache Iceberg V3 support** — open table format enabling data to be shared across engines without Snowflake ownership
- **Horizon Catalog** (powered by Apache Polaris) — bi-directional read and write for Iceberg data managed by Snowflake, usable by external query engines
- **Horizon Context** — the context and metadata layer that ensures a single version of the truth across systems

**Builder read:** The Open Framework is most relevant if you are running a multi-cloud or multi-engine architecture where data lives in multiple places and you need AI agents to reason across all of it. If you are all-in on Snowflake already, this is the infrastructure that makes external data sources first-class citizens without ETL cycles.

---

## The Anthropic-Snowflake Signal

Daniela Amodei's keynoting the Summit opening was not ceremonial. At Summit, Snowflake and Anthropic confirmed:

- Claude powers both CoWork (formerly Intelligence) and CoCo (formerly Cortex Code)
- The multi-year, $200 million partnership gives 12,600 Snowflake customers access to Claude through Cortex AI
- The next phase focuses on multi-step agent workflows where Claude handles reasoning, Snowflake handles governed data access
- Claude is available across Snowflake's cloud providers: AWS Bedrock, Google Cloud Vertex AI, Microsoft Azure

This partnership positions Claude not as an optional model endpoint for Snowflake builders but as the default reasoning layer for Snowflake's agentic stack. If you are building on Snowflake, the most natural path to frontier-quality agent reasoning runs through Claude — governed by Snowflake, fine-tunable on Cortex Training, contextualized through Cortex Sense.

Notable customer announcement from Summit: **Sanofi** selected Snowflake to accelerate AI-powered drug development.

---

## Builder Decision Guide

**Build on CoWork if:** you are deploying agents for business teams (finance, sales, operations) who need to query enterprise data in natural language, take actions, and receive proactive recommendations. CoWork with Cortex Sense prebuilt plugins is the lowest-friction path to governed enterprise agents for non-developer users.

**Build on CoCo if:** your team is building and deploying Snowflake-native applications and agents. CoCo's governed coding environment with enterprise data context is more useful than a generic coding agent for Snowflake-specific work.

**Use Cortex Training if:** you need to fine-tune a domain-specific model and your data cannot leave Snowflake's governance perimeter. Qwen and Mistral families are the current options.

**Adopt Cortex Sense if:** you are building agents that need to answer questions about enterprise data and accuracy depends on shared business definitions. Build your org's Cortex Sense context layer before deploying production agents to business users — it is the difference between agents that answer and agents that answer correctly.

**Evaluate Datastream if:** you need agents to act on real-time events. Especially valuable if you are currently maintaining a separate Kafka-to-Snowflake integration.

**Wait on Open Framework if:** you are Snowflake-native with no external lake requirements. It becomes relevant when you are federating data across systems.

---

## What Was Not Announced

The preview article from May 31 anticipated **AISQL** (Cortex AISQL, natural language to SQL for analytics). This did not appear as a major announcement at Summit — it may have landed as a minor update or been folded into CoCo's capabilities.

**OpenFlow** was announced broadly but deep technical documentation for custom connector development was not publicly available as of this writing.

Snowflake's **Adaptive Compute** (previously previewed) also did not emerge as a major standalone announcement — likely absorbed into the Graviton-powered infrastructure story from the AWS partnership.

---

## What to Watch

- **Cortex Training GA** — managed GPU fine-tuning for Qwen/Mistral is in preview. GA date not announced.
- **CoCo desktop app** — available now. VS Code extension and Excel extension shipping at different stages.
- **Cortex Sense plugin library** — finance and sales plugins are available; expansion to other functions expected.
- **Datastream GA pricing** — streaming service pricing was not detailed at launch. Check Snowflake's pricing page before architectural decisions depend on it.
- **Anthropic-Snowflake Cortex Agents depth** — the multi-step agent workflow documentation for the Claude + Snowflake integration is the technical artifact most builders need and the one least publicly documented at launch.

The pre-summit preview article ([Builder Preview: May 31](/builders-log/snowflake-summit-26-anthropic-amodei-intelligence-openflow-builder-preview/)) covered what was expected before the keynotes. This article covers what actually shipped.

