---
title: "The Confluent MCP Server — Kafka, Flink, and Stream Governance for AI Agents"
date: 2026-05-05T10:00:00+09:00
description: "Confluent's official MCP server exposes 52 tools across Kafka topics, Flink SQL, Schema Registry, Kafka Connect, Tableflow, and billing — but nearly all require Confluent Cloud."
og_description: "Confluent's official MCP server gives AI agents 52 tools across Kafka, Flink, Schema Registry, Tableflow, and billing. Vendor-backed, multi-transport, with tool filtering and DNS rebinding protection. Confluent Cloud-only for most features. Rating: 3.5/5."
content_type: "Review"
card_description: "Confluent's official MCP server for Kafka, Flink SQL, Schema Registry, Tableflow, and Confluent Cloud management. 52 tools across 13 categories. Multi-transport (stdio, HTTP, SSE), API key auth, and granular tool filtering. Most features require Confluent Cloud — self-managed Kafka users get only 8 tools."
last_refreshed: 2026-05-05
---

Part of our **[Message Queue MCP Servers roundup](/reviews/message-queue-mcp-servers/)**.

**At a glance:** 152 GitHub stars, 50 forks, TypeScript, MIT license. v1.2.2 (April 14, 2026). npm: `@confluentinc/mcp-confluent`. Node.js 22+ required. AWS Marketplace listing (4.4/5 from 111 reviews).

Confluent is the company founded by the original creators of Apache Kafka. Its cloud platform — Confluent Cloud — manages Kafka clusters, stream processing with Apache Flink, schema governance, data pipeline automation (Tableflow), and connector management at enterprise scale. With this MCP server, your AI agent can interact with all of it through natural language: creating topics, running Flink SQL, tagging PII data, managing pipelines, and tracking cloud costs — without navigating the Confluent Console.

The server launched April 8, 2025, and has grown steadily to 52 tools across 13 categories. The v1.2.0 release (April 2, 2026) added billing cost tracking, Flink catalog exploration, Flink diagnostics, cloud metrics, and local Kafka support — making it the most comprehensive Kafka-ecosystem MCP server available. But there is a hard line: 44 of 52 tools require Confluent Cloud REST APIs. If you run self-managed Apache Kafka, you get 8 tools.

## What It Does

The server organizes its tools into 13 categories:

### Kafka Operations (7 tools)

| Tool | Purpose |
|------|---------|
| `list-topics` | List all topics in the cluster |
| `create-topics` | Create a new topic with config |
| `delete-topics` | Delete one or more topics |
| `produce-message` | Publish a message to a topic |
| `consume-messages` | Read messages from a topic |
| `alter-topic-config` | Change topic configuration settings |
| `get-topic-config` | Retrieve current topic configuration |

These 7 tools are the only ones available without Confluent Cloud — they work with self-managed Kafka clusters (and with Confluent Local via Docker). Everything else in this review requires Confluent Cloud.

### Flink SQL (5 tools) — Cloud only

| Tool | Purpose |
|------|---------|
| `create-flink-statement` | Submit a Flink SQL statement for execution |
| `list-flink-statements` | List all statements in a compute pool |
| `read-flink-statement` | Get details and status of a statement |
| `delete-flink-statements` | Remove one or more statements |
| `get-flink-statement-exceptions` | Retrieve exceptions from a failed statement |

Flink SQL integration is what sets this server apart from any community Kafka MCP server. Your AI agent can create streaming SQL queries, check their execution status, pull exception details when they fail, and clean up completed statements — all without touching the Confluent Console.

### Flink Catalog (5 tools) — Cloud only

`list-flink-catalogs`, `list-flink-databases`, `list-flink-tables`, `describe-flink-table`, `get-flink-table-info`

Five tools for exploring the Flink catalog structure — understanding what databases, tables, and schemas exist in your compute environment before writing SQL against them.

### Flink Diagnostics (3 tools) — Cloud only

`check-flink-statement-health`, `detect-flink-statement-issues`, `get-flink-statement-profile`

Added in v1.2.0. These are the debugging layer on top of Flink SQL execution: health checks, automatic issue detection, and execution profiling. No other Kafka MCP server exposes Flink diagnostics at all.

### Kafka Connect (4 tools) — Cloud only

`list-connectors`, `read-connector`, `create-connector`, `delete-connector`

Full lifecycle management of Confluent Cloud connectors. Kafka Connect is the standard framework for streaming data between Kafka and external systems (databases, S3, Elasticsearch, etc.). Creating connectors conversationally — telling your agent to "set up a connector to sink this topic to S3 with these settings" — is one of the more powerful use cases.

### Schema Registry (2 tools) — Cloud only

| Tool | Purpose |
|------|---------|
| `list-schemas` | List all registered schemas |
| `delete-schema` | Delete a schema version |

This is the most limited section relative to what Schema Registry supports. No `create-schema`, no `get-schema`, no compatibility checking, no subject-level management. The community-built [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) (31 stars, 20+ tools, OAuth 2.1) offers dramatically more Schema Registry coverage for both Confluent and non-Confluent setups.

### Catalog & Tags / Stream Governance (7 tools) — Cloud only

`search-topics-by-tag`, `search-topics-by-name`, `create-topic-tags`, `delete-tag`, `remove-tag-from-entity`, `add-tags-to-topic`, `list-tags`

Confluent's Stream Governance suite allows tagging Kafka topics with metadata (e.g., `PII`, `GDPR`, `financial`). These 7 tools expose that tag system: searching topics by tag, adding and removing tags, listing all defined tags. One of the more compelling use cases: an agent can automatically identify and tag topics containing PII data as part of a governance workflow.

### Organizations, Environments & Clusters (4 tools) — Cloud only

`list-organizations`, `list-environments`, `read-environment`, `list-clusters`

Infrastructure inspection tools. Useful for multi-environment setups (dev, staging, production) and for orienting a new session — the agent can discover what environments and clusters exist before operating on them.

### Tableflow Topics (6 tools) — Cloud only

`create-tableflow-topic`, `list-tableflow-topics`, `read-tableflow-topic`, `update-tableflow-topic`, `delete-tableflow-topic`, `list-tableflow-regions`

Tableflow (GA March 2025) is Confluent's answer to the Kafka-to-data-lake problem. It automatically converts Kafka topics — using Schema Registry schemas — into Apache Iceberg or Delta Lake table format, publishing metadata to external catalogs like AWS Glue or Databricks Unity Catalog. This eliminates custom ETL pipelines for feeding data warehouses. The MCP server exposes the full Tableflow topic lifecycle.

### Tableflow Catalog Integrations (5 tools) — Cloud only

`create-tableflow-catalog-integration`, `list-tableflow-catalog-integrations`, `read-tableflow-catalog-integration`, `update-tableflow-catalog-integration`, `delete-tableflow-catalog-integration`

Full CRUD for the catalog integrations that connect Tableflow to downstream systems (AWS Glue, Unity Catalog, etc.). Together with the Tableflow topics tools, this gives agents complete control over Confluent's data lake automation layer.

### Metrics (2 tools) — Cloud only

`list-available-metrics`, `query-metrics`

Added in v1.2.0. The `query-metrics` tool queries the Confluent Cloud Metrics API — the same API used by Confluent Console dashboards — for cluster-level observability data (throughput, consumer lag, partition counts, etc.).

### Billing (1 tool) — Cloud only

`list-billing-costs` — cost data by environment, cluster, and service type. Added in v1.2.0. Allows agents to track cloud spend alongside infrastructure management.

### Documentation (1 tool) — Universal

`search-product-docs` — searches Confluent's product documentation. Available in all modes including self-managed Kafka setups.

---

**Total: 52 tools.** 8 universal (Kafka + docs search), 44 Confluent Cloud-only.

## Setup

**Install via npx:**

```bash
npx -y @confluentinc/mcp-confluent -e /path/to/.env
```

For Claude Code or Claude Desktop, use the standard MCP JSON config:

```json
{
  "mcpServers": {
    "confluent": {
      "command": "npx",
      "args": ["-y", "@confluentinc/mcp-confluent", "-e", "/path/to/.env"]
    }
  }
}
```

The `.env` file holds credentials. The minimum for Kafka-only access:

```bash
BOOTSTRAP_SERVERS=your-cluster.confluent.cloud:9092
KAFKA_API_KEY=your-api-key
KAFKA_API_SECRET=your-api-secret
```

For full Confluent Cloud access, you need separate credential sets for each service: `CONFLUENT_CLOUD_API_KEY/SECRET` for platform management, `KAFKA_API_KEY/SECRET` + `KAFKA_REST_ENDPOINT` for Kafka operations, `FLINK_API_KEY/SECRET` + `FLINK_COMPUTE_POOL_ID` + `FLINK_REST_ENDPOINT` for Flink, and `TABLEFLOW_API_KEY/SECRET` for Tableflow. The total environment variable count for a fully-configured Confluent Cloud instance can exceed 20 variables.

**Tool activation is credential-driven:** if you don't set Flink credentials, Flink tools don't appear. This is the primary tool filtering mechanism — adding credentials unlocks tools.

**Additional filtering via CLI flags:**

```bash
# Show which tools are enabled
npx @confluentinc/mcp-confluent --list-tools

# Only expose specific tools
npx @confluentinc/mcp-confluent --allow-tools list-topics,consume-messages

# Block destructive tools
npx @confluentinc/mcp-confluent --block-tools delete-topics,delete-schema
```

File-based allow/block lists (`--allow-tools-file allow.txt`) are also supported.

**Docker:**

```bash
docker run -e KAFKA_API_KEY=... -e KAFKA_API_SECRET=... confluentinc/mcp-confluent
```

The Docker image is listed on AWS Marketplace (rated 4.4/5 from 111 reviews) and supports Amazon Bedrock AgentCore.

## What's New (v1.2.0, April 2, 2026)

The April 2026 release was the most significant update since launch:

- **Billing tool** (`list-billing-costs`) — cost visibility per environment/cluster/service
- **Flink Catalog tools** (5 new tools) — catalog/database/table exploration for Flink SQL context
- **Flink Diagnostics** (3 new tools) — health checks, issue detection, statement profiling
- **Cloud Metrics API tools** (2 new tools) — cluster-level observability via the Metrics API
- **Confluent Local support** — self-managed Kafka/Schema Registry connections (the 8 universal tools now work with Docker-based local setups, not just Confluent Cloud)
- **Telemetry** — anonymous usage analytics added (opt-out via `DO_NOT_TRACK=true`)
- **Fastify security patch** — dependency update addressing a known Fastify vulnerability

v1.2.2 (April 14) backported bug fixes to the v1.2.x line.

## What's Good

**Official Confluent backing with vendor SLAs.** As of Q1 2026, Confluent announced vendor-backed support for the MCP server — GitHub issues are routed to Confluent engineering under defined SLAs, and enterprise account teams can escalate. This is a meaningful commitment compared to the typical open-source "file an issue and wait" model. The server is maintained by the team that builds the platform it exposes.

**Flink SQL integration is unique.** No community Kafka MCP server exposes Apache Flink. The ability to create Flink SQL statements, check their execution status, pull diagnostic information, and explore the full Flink catalog through natural language represents a qualitatively different capability — your agent can build and debug streaming SQL pipelines conversationally. Combined with Flink diagnostics (health, issues, profiling), this is the closest thing to a Flink IDE built into your AI assistant.

**Tableflow is a genuine differentiator.** Confluent's Tableflow feature eliminates custom ETL for data lake ingestion — an agent that can create, configure, and manage Tableflow topics plus catalog integrations can automate a non-trivial piece of data infrastructure. No other MCP server in the Kafka ecosystem touches this capability.

**Stream governance tooling.** The 7-tool tag management suite is purpose-built for data governance workflows — automatically classifying topics containing PII, GDPR-regulated data, or financial information. This is the kind of task that AI agents can genuinely accelerate: scan a set of topics, identify patterns, apply tags systematically.

**Granular tool filtering.** The combination of credential-driven activation, `--allow-tools`/`--block-tools` CLI flags, and file-based allowlists gives teams precise control over what an AI agent can do. A read-only configuration for your security audit agent and a full-access configuration for your platform engineering agent can coexist using the same server binary.

**Multi-transport with security hardening.** Three transport modes (stdio, HTTP, SSE) support a range of deployment patterns. The v1.1.0 addition of API key authentication for HTTP/SSE and DNS rebinding protection (`MCP_ALLOWED_HOSTS`, binding to `127.0.0.1` by default) reflects security-conscious design that many community MCP servers skip.

**AWS Marketplace listing with Bedrock AgentCore support.** The container image on AWS Marketplace with 4.4/5 rating and 111 reviews signals production adoption. Amazon Bedrock AgentCore integration extends the server into AWS's managed agent runtime.

## What's Not

**Confluent Cloud-only for 44 of 52 tools.** This is the defining limitation. If you run self-managed Apache Kafka — whether on bare metal, in Kubernetes, or on a cloud VM — you get 7 Kafka tools and the documentation search. No Flink, no Schema Registry, no governance tags, no Tableflow, no metrics, no billing. The title is somewhat misleading: this is a Confluent Cloud MCP server, not a Kafka MCP server.

**OAuth not supported.** Multiple open issues (#253, #311, #312, #313, #177) track OAuth/SASL OAUTHBEARER support. Organizations using SSO or identity-provider-based auth — common in enterprise Confluent Cloud deployments — must use API key authentication, which means provisioning service account keys and managing rotation. For a platform marketed at enterprise customers, the absence of OAuth is a meaningful gap.

**Schema Registry coverage is thin.** Two tools — `list-schemas` and `delete-schema` — is a fraction of what Schema Registry supports. No `create-schema`, no `get-schema`, no `check-compatibility`, no subject management, no version history. The dedicated [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) (31 stars, 20+ tools, OAuth 2.1, SLIM_MODE, multi-registry) provides dramatically more Schema Registry coverage, and it works with both Confluent and non-Confluent registries.

**`produce-message` schema friction.** Issue #159 reports that the `produce-message` tool requires a schema on every call, even when the schema has already been registered. This creates repetitive overhead for agents producing multiple messages to a Schema Registry-governed topic.

**Anonymous telemetry by default.** v1.2.0 added usage analytics without making opt-in the default. Set `DO_NOT_TRACK=true` in your environment to disable it. Not a deal-breaker, but worth noting for organizations with strict data governance policies.

**34 open issues, v1.3.0 pre-release not yet stable.** A v1.3.0-pre tag exists on GitHub as of April 2026, but no stable v1.3.0 has shipped. The 34 open issues include the OAuth gaps plus architectural cleanup work (migrating handlers from direct env var reads to the connection config system). Active development, but not everything is tidy.

**Node.js 22+ requirement.** Projects on earlier Node versions need to upgrade. Not unusual for a modern TypeScript project, but it's a constraint to be aware of.

## How It Compares

For Confluent Cloud users, no other MCP server comes close. The breadth — Kafka operations, Flink SQL, Flink diagnostics, Kafka Connect, Tableflow, stream governance, metrics, and billing in a single server — is unmatched.

For self-managed Kafka, the relevant alternatives are community servers:

| Server | Stars | Language | Kafka Auth | Key Difference |
|--------|-------|----------|------------|----------------|
| [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) | 152 | TypeScript | API key | Official; 52 tools; Cloud-only for 44 |
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 77 | Go | SASL_PLAINTEXT | 6 tools; self-managed Kafka |
| [tuannvm/kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server) | 48 | Go | SASL + TLS + OAuth 2.1 | 9 tools; self-managed; OAuth support |
| [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) | 31 | Python | OAuth 2.1 | Schema Registry specialist; 20+ tools |

If you run self-managed Kafka and need OAuth or SASL auth, **tuannvm/kafka-mcp-server** (9 tools, Go, OAuth 2.1, TLS) is more capable than the universal subset of the official Confluent server. If Schema Registry is your priority, **aywengo/kafka-schema-reg-mcp** is the better choice regardless of your infrastructure.

## The Bigger Picture

The Confluent MCP server is a window into an interesting tension in enterprise data infrastructure. Confluent has spent years building a platform that goes far beyond vanilla Kafka — Flink, Tableflow, Stream Governance, and managed connectors are all non-Kafka innovations. The MCP server exposes those innovations fully while treating core Kafka as a secondary concern for self-managed users.

This is a deliberate product decision, not an oversight. The server is called `mcp-confluent`, not `mcp-kafka`. The implied message is clear: if you want the full MCP experience, use Confluent Cloud.

That framing makes more sense when you consider the use cases where AI agents add the most value in the Kafka ecosystem. Writing Flink SQL is tedious and error-prone. Managing Tableflow integrations involves multiple steps across different systems. Tracking down which topics contain PII data for compliance is a manual, time-consuming task. Reviewing cloud costs across multiple clusters requires dashboard-hopping. These are exactly the tasks where a conversational agent — one that can orchestrate multiple API calls, remember context, and translate natural language intent into specific configurations — genuinely accelerates work.

For teams building event-driven architectures on Confluent Cloud, the MCP server represents a meaningful improvement to the developer experience. The combination of Flink SQL execution, Tableflow pipeline management, stream governance tagging, and billing visibility in a single server — with vendor-backed support and enterprise-grade security hardening — is a strong package. The OAuth gap and thin Schema Registry coverage are real limitations, but they're tracked issues with clear resolution paths.

The harder question is for the broader Kafka ecosystem. Over 70% of Kafka deployments run on self-managed infrastructure (strimzi, on-prem, cloud VMs, MSK). For those users, the official Confluent server offers 8 of 52 tools. The community has partially filled the gap — kanapuli and tuannvm cover basic self-managed Kafka with reasonable auth options — but no community server approaches the Flink or Tableflow capabilities that make the Confluent server interesting.

## Rating: 3.5/5

Confluent's MCP server earns a 3.5/5 for delivering the most comprehensive Kafka-ecosystem MCP coverage available — 52 tools spanning Kafka, Flink SQL, Flink diagnostics, Kafka Connect, Tableflow, stream governance, metrics, and billing — with official vendor backing, multi-transport support, security hardening, and AWS Marketplace distribution. For Confluent Cloud users, this is the definitive MCP server for data streaming infrastructure.

The rating is held back by the hard Confluent Cloud requirement (44 of 52 tools unavailable to self-managed Kafka users), missing OAuth support despite being an enterprise-marketed product, thin Schema Registry coverage (2 tools vs. the 20+ available in community alternatives), default telemetry collection, and 34 open issues. The server is excellent for its target audience, but that target audience is narrower than the name implies.

**Use this if:** You run Confluent Cloud and want AI-assisted Kafka topic management, Flink SQL pipeline authoring, Tableflow data lake automation, stream governance tagging, or cloud cost visibility through your AI coding assistant.

**Skip this if:** You run self-managed Apache Kafka (community alternatives are more capable for your use case), you need OAuth or SASL OAUTHBEARER authentication, you need comprehensive Schema Registry management, or you need to work with clusters not on Confluent Cloud.

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) and has not been independently verified by a human editor. We have not tested this MCP server hands-on. All claims are based on publicly available documentation, GitHub data, and community sources as of May 2026. [Rob Nugen](https://robnugen.com) oversees this project.*
