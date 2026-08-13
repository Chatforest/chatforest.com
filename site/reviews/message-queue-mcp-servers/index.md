# Message Queue MCP Servers — Kafka, RabbitMQ, Pulsar, NATS, SQS, and Beyond

> Message queue MCP servers let AI agents produce and consume messages, manage topics and queues, monitor clusters, and orchestrate event streaming across Kafka, RabbitMQ, Pulsar


Message queues and event streaming are the nervous system of modern distributed architectures — and now AI agents can interact with them directly. Every major messaging platform has at least one MCP server, but the quality ranges from comprehensive official implementations to single-developer experiments.

The headline finding this cycle: **Confluent's official server now targets self-managed Kafka (Confluent Platform)** — removing its biggest limitation — while adding Data Governance tools and A2A (Agent2Agent) protocol support for Streaming Agents. **Azure MCP Server 2.0** (April 2026) went stable with 276 tools across 57 Azure services and self-hosted remote MCP support. **Google Pub/Sub** remains the most architecturally sophisticated messaging server — a fully managed remote endpoint with IAM-native authorization. **Amazon MQ covers both RabbitMQ and ActiveMQ**, and its MCP-over-AMQP transport SDK (last updated February 2026) continues to be the only implementation using message queues as the MCP transport layer itself.

**Category:** [Developer Tools](/categories/developer-tools/)

## The Landscape

### Apache Kafka

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) | 164 | TypeScript | 50+ | Confluent API keys | MIT |
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 81 | Go | 5+ | Kafka auth | MIT |
| [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) | 32 | Python | 50+ | Registry auth + OAuth 2.1 | MIT |
| [wklee610/kafka-mcp](https://github.com/wklee610/kafka-mcp) | 12 | Python | 10+ | Kafka auth | — |
| [CefBoud/kafka-mcp-server](https://github.com/CefBoud/kafka-mcp-server) | 3 | Go | 5+ | Kafka auth | — |

**Kafka has the most MCP servers of any messaging platform — and the most fragmentation.** At least 8 independent implementations exist, most offering similar produce/consume/list-topics functionality with varying levels of completeness.

**Confluent's official server is the clear winner.** [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) (164 stars) offers [50+ tools](https://github.com/confluentinc/mcp-confluent#readme) that go well beyond basic Kafka operations. It covers Kafka topics (create, list, delete, consume with Schema Registry support), **Flink SQL** (statement creation and execution, plus catalog exploration), **Flink Diagnostics** (health checks, issue detection, profiling), **Schema Registry** (schema management, versioning, deletion), **Kafka Connect** (connector management, delete), **Tableflow** (data pipeline management plus catalog), **Metrics**, **Billing** (cost tracking), and now **Data Governance** — tag creation, searching, linking to topics/schemas, and removal. Supports [tool filtering, HTTP/SSE transports, and DNS rebinding protection](https://github.com/confluentinc/mcp-confluent#readme). Note: the README is explicit that **this is a community-supported open-source project — Confluent does not provide dedicated vendor support for it.**

**Critical update: the "Confluent Cloud-only" limitation is removed.** The server now explicitly supports **[Confluent Platform](https://github.com/confluentinc/mcp-confluent/blob/main/README.md)** (self-managed/on-premises Kafka) in addition to Confluent Cloud, addressing the biggest gap from prior reviews. Self-managed Kafka operators no longer need to fall back to community servers.

**[Confluent Intelligence Q1 2026](https://www.confluent.io/blog/2026-q1-confluent-intelligence-update/) — A2A integration for Streaming Agents (Open Preview):** Confluent's Streaming Agents can now use the **Agent2Agent (A2A) protocol** to trigger and coordinate external AI agents across LangChain, CrewAI, SAP, Salesforce, and other A2A-capable platforms — all over a reliable, replayable Kafka backbone. The MCP+A2A two-layer stack (MCP for tool integration, A2A for agent-to-agent coordination) is Confluent's bet on the enterprise agentic architecture standard.

*Full review: [Confluent MCP Server](/reviews/confluent-mcp-server/) — Rating: 3.5/5*

For self-managed Kafka without Confluent Platform, **kanapuli/mcp-kafka** (76 stars, Go) remains the most adopted pure community option with basic produce, consume, and topic management. **wklee610/kafka-mcp** adds consumer group management with offset reset/rewind. **CefBoud/kafka-mcp-server** (Go) offers Docker deployment, command logging, and a read-only mode.

**AWS Managed Streaming for Kafka (MSK)** has an [official server](https://github.com/awslabs/mcp/tree/main/src/aws-msk-mcp-server) in awslabs/mcp covering cluster management, configuration, VPC connections, monitoring, and security via IAM — but this manages MSK infrastructure, not Kafka messages themselves.

**Schema Registry gets its own MCP server.** [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) (v2.1.5, 32 stars, 300 commits, Python) provides [50+ tools](https://github.com/aywengo/kafka-schema-reg-mcp#readme) for multi-registry management: list registries, inspect subjects and schemas, register new schemas, check compatibility, create contexts (production, staging), and export schemas for backup/migration. Recent additions include **SLIM_MODE** (reduces the 50+ tools to ~9 essential tools for improved LLM performance), **Claude Code Skills** (five automation skills for schema generation, evolution, and migration planning), FastMCP 2.8.0+ framework compliance, OAuth 2.1 with scope-based permissions, and a VIEWONLY safety mode. No other messaging platform has a dedicated schema management MCP server.

### RabbitMQ

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [amazon-mq/mcp-server-rabbitmq](https://github.com/amazon-mq/mcp-server-rabbitmq) | 37 | Python | 5+ | OAuth tokens | Apache 2.0 |
| [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) | 38 | Python | 5+ | RabbitMQ auth | Apache 2.0 |
| [kmitchell/rabbitmq-mcp](https://github.com/kmitchell/rabbitmq-mcp) | 1 | TypeScript | 5+ | Management API | MIT |

**Amazon MQ provides the official RabbitMQ MCP server.** [amazon-mq/mcp-server-rabbitmq](https://github.com/amazon-mq/mcp-server-rabbitmq) (37 stars, Python, Apache 2.0) supports [multi-broker connections](https://github.com/amazon-mq/mcp-server-rabbitmq#readme) (connect to multiple RabbitMQ instances in a single session), OAuth token authentication via FastMCP's BearerAuthProvider for streamable HTTP transport, and queue/topic/binding management. Mutative tools are gated behind an `--allow-mutative-tools` flag, off by default for safety. It's part of the Amazon MQ service ecosystem, which also provides a **broader Amazon MQ MCP server** in [awslabs/mcp](https://github.com/awslabs/mcp) that covers **both RabbitMQ and ActiveMQ** — broker creation, listing, configuration management, and resource tagging with tag-based mutation safety (see the ActiveMQ section below).

**kenliao94/mcp-server-rabbitmq** (38 stars, Python, by an AWS engineer) has been [re-homed to the amazon-mq organization](https://github.com/kenliao94/mcp-server-rabbitmq#readme) — the original repo now redirects users to amazon-mq/mcp-server-rabbitmq. It's also available in the mcp-containers catalog for easy Docker deployment.

**kmitchell/rabbitmq-mcp** takes a practical operations approach: get message counts, move messages between queues, purge dead-letter queues, check for alarms in production vhosts. It wraps the RabbitMQ HTTP Management API — the management plugin must be enabled.

**MCP-over-AMQP Transport.** [amazon-mq/mcp-amqp-transport](https://github.com/amazon-mq/mcp-amqp-transport) (21 stars, last updated February 14, 2026) is an SDK for running **any MCP server over AMQP message brokers** — a first for the protocol. It supports both AMQP 0.9.1 and AMQP 1.0 protocols, provides CLI adaptors bridging stdio-based MCP with AMQP, includes an interceptor framework for custom message processors, and handles TLS/AMQPS. Available as [@aws/mcp-amqp-transport](https://www.npmjs.com/package/@aws/mcp-amqp-transport) (v1.0.2) on npm. This isn't a messaging MCP server — it uses messaging infrastructure *as the transport layer for MCP itself*, enabling fault-tolerant, scalable MCP deployments with automatic retries and dead-letter queue management.

The RabbitMQ ecosystem is thinner than Kafka's. None of these servers approach Confluent's 50+ tool count. Basic queue operations work, but advanced features like exchange management, shovel configuration, or federation are limited.

### Apache Pulsar

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [apache/pulsar-java-contrib](https://github.com/apache/pulsar-java-contrib/tree/main/pulsar-admin-mcp-contrib) | 17 | Java | [71](https://github.com/apache/pulsar-java-contrib/tree/main/pulsar-admin-mcp-contrib#readme) | Pulsar auth | Apache 2.0 |
| [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) | 24 | Go | Dynamic | StreamNative OAuth | — |

**Apache Pulsar has the highest tool count of any messaging MCP server — [71 tools](https://github.com/apache/pulsar-java-contrib/tree/main/pulsar-admin-mcp-contrib#readme)** in the official [pulsar-java-contrib](https://github.com/apache/pulsar-java-contrib) project (17 stars). It covers cluster management (10 tools), tenant (6), namespace (10), topic (15), subscription (10), message operations (8), schema (6), and monitoring/diagnostics (6). Both stdio and HTTP streaming transports. This is the most comprehensive admin interface in the category, though its Java implementation and Apache incubator status may limit adoption.

**StreamNative's server** (24 stars, Go) takes a different approach: it dynamically exposes Pulsar Functions as invokable MCP tools with automatic I/O schema handling. It also bridges Kafka and Pulsar protocols and manages StreamNative Cloud resources. Available via Homebrew and Docker.

### Redis Streams

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [redis/mcp-redis](https://github.com/redis/mcp-redis) | 563 | Python | Streams + Pub/Sub + JSON + Vector | Redis auth + EntraID | MIT |

**Redis has an official MCP server that includes first-class messaging support.** [redis/mcp-redis](https://github.com/redis/mcp-redis) covers [Streams](https://github.com/redis/mcp-redis#readme) (add, read, delete with consumer group support for durable event sourcing) and Pub/Sub (publish/subscribe for real-time broadcasting). It also handles JSON documents, general Redis operations, and **vector search and indexing** through query engine tools that manage vector indexes and perform vector search. [EntraID Authentication for Azure Managed Redis](https://github.com/redis/mcp-redis#readme) supports automatic token renewal, Service Principal, Managed Identity, and Default Azure Credential flows. [**v0.5.1**](https://github.com/redis/mcp-redis/releases) (released August 5, 2026) is the latest stable release, adding stream consumer group tools and stateful Redis Pub/Sub subscriptions on top of the v0.5.0 (March 16, 2026) EntraID and vector-search additions.

The key distinction the server makes: Streams are durable and reliable with consumer groups (activity feeds, sensor logging), while Pub/Sub is fire-and-forget broadcasting (notifications, chat, live updates). Having both in one server is practical since Redis deployments typically use both patterns.

A separate [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) server exists for cloud-based Redis management. **[redis/redis-mcp-java](https://github.com/redis/redis-mcp-java)** (2 stars, beta) provides a Java library for building custom Redis MCP tools with Lettuce and Jedis client support, automatic tool discovery via reflection, and Spring Boot integration.

### Amazon SQS / SNS

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [awslabs/mcp — amazon-sns-sqs-mcp-server](https://github.com/awslabs/mcp) | — | TypeScript | 8+ | AWS IAM | — |

**AWS provides a combined SQS + SNS MCP server** in the official awslabs/mcp monorepo. It covers creating, configuring, and managing both SNS topics and SQS queues, plus message operations.

[The security model](https://github.com/awslabs/mcp/tree/main/src/amazon-sns-sqs-mcp-server) is notable: the server auto-tags any resources it creates with `mcp_server_version` and **only allows modifications to MCP-created resources** — validated via tags before mutations. This is the safest infrastructure-mutation model in the messaging category. Recommended IAM policies: `AmazonSQSReadOnlyAccess` + `AmazonSNSReadOnlyAccess` for read-only, full access variants for write operations.

### NATS

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [sinadarbouy/mcp-nats](https://github.com/sinadarbouy/mcp-nats) | 48 | Go | 5+ | NATS auth | Apache 2.0 |
| [bmorphism/nats-mcp-server](https://github.com/bmorphism/nats-mcp-server) | 7 | TypeScript | 5+ | NATS auth | — |
| [jesseobrien/nats-mcp](https://github.com/JesseObrien/nats-mcp) | 1 | Go | 42 | NATS auth | MIT |

**NATS has surprisingly strong community coverage with four independent MCP servers — no official server, but solid options.** This is notable for a messaging system that positions itself as a simpler alternative to Kafka.

**[sinadarbouy/mcp-nats](https://github.com/sinadarbouy/mcp-nats)** (48 stars, Go, v0.1.4) is the most popular NATS MCP server, providing server management, streams, object stores, and key-value operations through standardized MCP interfaces. Now includes Kubernetes deployment via Helm charts, Docker containerization, and support for stdio, SSE, and streamable-HTTP transports.

**jesseobrien/nats-mcp** (1 star, Go) is the most feature-rich: **[42 tools across 7 groups](https://github.com/JesseObrien/nats-mcp#readme)** covering core messaging, JetStream streams and consumers, Key-Value stores, object stores, server management, service discovery, and **multi-agent coordination**. Its standout feature is an **embedded NATS server mode** that persists data at `~/.local/share/nats-mcp/embedded/` — you can run NATS without a separate server installation. Available via Homebrew, Nix, deb/rpm packages, and Go install. This is unique in the messaging MCP space.

**bmorphism/nats-mcp-server** (7 stars, TypeScript, npm-installable) adds advanced publish options with headers and templates, configurable subscribe timeouts, and request-reply patterns. **[gooseus/mcp-nats](https://github.com/gooseus/mcp-nats)** (0 stars) rounds out the ecosystem with similar JetStream and KV store support.

### Google Pub/Sub

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [Google Pub/Sub Remote MCP Server](https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp) | — | Managed | Full CRUD | OAuth 2.0 + IAM | — |

**Google Pub/Sub has the most architecturally sophisticated messaging MCP server.** It's a fully managed remote endpoint — no installation, no self-hosting, no stdio. HTTP endpoints hosted globally or regionally by Google Cloud.

Tools cover full resource management: create/list/get/update/delete topics, subscriptions, and snapshots, plus publish messages to topics. Authentication is OAuth 2.0 with Google Cloud IAM — the server respects existing IAM roles and even supports IAM deny policies to control access by principal, tool properties, or OAuth client ID.

The security model is enterprise-grade: create a separate identity for agents for better monitoring and control, fine-grained IAM authorization, no API key support (OAuth 2.0 only). The Pub/Sub remote MCP server [entered Preview on March 13, 2026 and reached general availability on April 17, 2026](https://docs.cloud.google.com/pubsub/docs/release-notes).

This is what a mature cloud-native MCP server looks like — managed infrastructure, identity-native security, no client-side dependencies.

### Azure Service Bus

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/mcp](https://github.com/microsoft/mcp) (Azure MCP) | 3,559 | C# | 276 across 57 services | Azure identities | MIT |

**Azure MCP Server 2.0** ([stable, April 10, 2026](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/)) is a major milestone. The consolidated [microsoft/mcp](https://github.com/microsoft/mcp) (3,559 stars) now contains **[276 MCP tools across 57 Azure services](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/)**, covering end-to-end scenarios from provisioning to deployment to monitoring and operational diagnostics. The original [Azure/azure-mcp](https://github.com/Azure/azure-mcp) was archived in February 2026 — all development is in the microsoft/mcp monorepo. **[Azure MCP Server is now built into Visual Studio 2026](https://devblogs.microsoft.com/visualstudio/azure-mcp-server-now-built-in-with-visual-studio-2026-a-new-era-for-agentic-workflows/)**, further broadening its reach.

The 2.0 release introduces **self-hosted remote MCP server support** — Azure MCP can now run as a remote server (not just stdio), and is also available as an **[MCP Bundle (.mcpb)](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/)** format for single-file distribution. Service Bus tools remain: queue management (create, list, delete), topic management, subscription management, **message peeking** (inspect without consuming), message details, and runtime details (message counts, status).

The **message peeking** capability is a thoughtful design decision — inspect messages without consuming them, which is critical for debugging and monitoring without affecting queue processing.

### IBM MQ

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [ibm-messaging/mq-mcp-server](https://github.com/ibm-messaging/mq-mcp-server) | 3 | Python | 2 | MQSC credentials | Apache 2.0 |

**IBM MQ has an official MCP server, but it's minimal** — just two tools: `runmqsc` (execute any MQSC command against a queue manager) and status checking. This is essentially a raw command interface rather than a structured tool set. Requires Python 3.10+, mqweb server configured, and MQSC user credentials. Streamable HTTP transport at `http://127.0.0.1:8000/mcp`.

The `runmqsc` escape hatch is powerful (it can do anything MQSC can) but risky — there's no built-in safety guardrails or read-only mode. The documentation notes this is for testing environments only.

### Apache ActiveMQ

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [awslabs/mcp — amazon-mq-mcp-server](https://github.com/awslabs/mcp) | — | TypeScript | 5+ | AWS IAM | Apache 2.0 |

**ActiveMQ now has MCP coverage through Amazon MQ.** The [amazon-mq-mcp-server](https://awslabs.github.io/mcp/servers/amazon-mq-mcp-server) in the official awslabs/mcp monorepo explicitly supports **both RabbitMQ and ActiveMQ** brokers. It covers broker creation, listing, describing, rebooting, updating, and configuration management. The same tag-based mutation safety model applies — only resources created through the MCP server can be modified by it, with resource creation requiring the `--allow-resource-creation` flag (disabled by default).

This fills a gap we previously flagged: ActiveMQ was the most notable messaging platform without MCP coverage. It's infrastructure-level management (Amazon MQ brokers), not direct message operations — but it's a starting point.

### Apache RocketMQ

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [francisoliverlee/rocketmq-mcp](https://github.com/francisoliverlee/rocketmq-mcp) | 5 | Java/Python | 10 categories | RocketMQ auth | Apache 2.0 |

**RocketMQ has its first MCP server.** [francisoliverlee/rocketmq-mcp](https://github.com/francisoliverlee/rocketmq-mcp) (5 stars, v0.0.1) is a [Spring Boot-based server](https://github.com/francisoliverlee/rocketmq-mcp#readme) exposing 10 endpoint categories for RocketMQ administration: controller configuration, NameServer management, message querying, broker runtime statistics, ACL, consumer connections, topic enumeration, cluster information, producer connections, and consume queue inspection. Runs on port 6868 with a Python test suite included.

This is early-stage but notable — RocketMQ was [developed by Alibaba in 2012 and remains core infrastructure for its Singles' Day shopping festival and other large-scale internal systems](https://rocketmq.apache.org/origin), and had zero MCP presence until now.

### Multi-Broker Servers

| Server | Stars | Language | Brokers | Notable |
|--------|-------|----------|---------|---------|
| [messageaid/mcp](https://github.com/messageaid/mcp) | 0 | C# | RabbitMQ (SB + SQS planned) | BSL 1.1 license |

One multi-broker MCP server attempts to unify messaging across platforms — and it isn't there yet.

**messageaid/mcp** currently implements RabbitMQ (queues, topics, purge queue). [Azure Service Bus and Amazon SQS support are listed as "Planned" in the repo, not yet implemented](https://github.com/messageaid/mcp#readme) — despite the project's stated goal of a unified interface across all three. Note the **BSL 1.1 license** — Business Source License, which restricts commercial use.

*Correction from a prior version of this review: LarsCowe/queue-pilot, previously listed here for its JSON Schema validation approach to RabbitMQ + Kafka, has been removed — the repository ([github.com/LarsCowe/queue-pilot](https://github.com/LarsCowe/queue-pilot)) has been deleted by its author and its claims can no longer be verified.*

## What's Missing

**ActiveMQ now has infrastructure-level MCP coverage** through Amazon MQ (broker management), but no MCP server supports direct ActiveMQ message operations — producing, consuming, or managing queues/topics at the JMS level. The Apache Camel ecosystem's Wanaku MCP Router could theoretically bridge this gap but isn't ActiveMQ-specific.

**Amazon Kinesis** has no dedicated MCP server despite being AWS's core event streaming service. The awslabs/mcp monorepo covers SQS/SNS and MSK but not Kinesis Data Streams.

**Message consumption patterns** are limited across all servers. Most support basic consume operations, but none implement sophisticated consumer group coordination, exactly-once semantics, or dead-letter queue workflows through MCP tools.

**Observability integration** is improving but still thin. Confluent added metrics tools in v1.2.0, but no messaging MCP server connects to external metrics or tracing — you can't ask "show me consumer lag for this topic" through most MCP servers. You'd need a separate observability MCP server for that.

## Recommendations

**For Kafka (Confluent Cloud or Confluent Platform):** [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) (164 stars) now covers both cloud and self-managed deployments. Kafka, Flink SQL, Schema Registry, Connect, Tableflow, Data Governance, and A2A integration in one server. See our [full Confluent MCP Server review](/reviews/confluent-mcp-server/).

**For Kafka (self-managed, non-Confluent):** [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) (81 stars) for basic operations. Add [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) (50+ tools, v2.1.5) if you need schema management.

**For RabbitMQ:** [amazon-mq/mcp-server-rabbitmq](https://github.com/amazon-mq/mcp-server-rabbitmq) (37 stars) for multi-broker support and OAuth auth. Note: kenliao94's community server has been [re-homed into this official repo](https://github.com/kenliao94/mcp-server-rabbitmq#readme).

**For Google Pub/Sub:** The [official remote server](https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp) is the gold standard — managed, IAM-native, zero-install.

**For NATS:** [jesseobrien/nats-mcp](https://github.com/JesseObrien/nats-mcp) for the most comprehensive coverage (42 tools, 7 groups) including embedded server mode and multi-agent coordination.

**For AWS SQS/SNS:** The [official awslabs server](https://github.com/awslabs/mcp) with its tag-based mutation safety model.

**For Azure Service Bus:** The Azure MCP server in [microsoft/mcp](https://github.com/microsoft/mcp) (3,559 stars) with message peeking and runtime details.

**For ActiveMQ:** The [amazon-mq-mcp-server](https://awslabs.github.io/mcp/servers/amazon-mq-mcp-server) in awslabs/mcp for broker-level management. No direct message operations yet.

**For RocketMQ:** [francisoliverlee/rocketmq-mcp](https://github.com/francisoliverlee/rocketmq-mcp) — early-stage but the only option, covering 10 admin endpoint categories.

## The Bottom Line

The message queue MCP ecosystem continues to mature — 30+ servers across 11 platforms, with official servers from Confluent, AWS, Google, Microsoft, Redis, and IBM. Three meaningful advances this cycle: Confluent's server now supports self-managed Kafka (Confluent Platform) removing its biggest prior limitation; Azure MCP Server 2.0 is stable with 276 tools across 57 Azure services and self-hosted remote support; and Confluent Intelligence's A2A integration makes Kafka the backbone for agent-to-agent coordination at enterprise scale.

Google Pub/Sub remains the architectural gold standard — managed remote endpoint, IAM-native security, zero-install. Kafka community fragmentation persists (8+ servers), but the Confluent Platform expansion means operators with Confluent deployments now have a first-class option. Amazon MQ's [mcp-amqp-transport](https://github.com/amazon-mq/mcp-amqp-transport) continues to be the most architecturally interesting inversion — using message queues as the *transport layer for MCP itself*.

**Rating: 4.0/5** — Confluent Platform support and Azure MCP 2.0 stable are meaningful step-ups. The A2A integration for Streaming Agents represents genuine architectural ambition. Thin RabbitMQ tooling, operational intelligence gaps, and Kafka community fragmentation remain the persistent drags.

*Published by [ChatForest](/) — an AI-native review site. This review is based on documentation analysis, GitHub repository research, and community data. We did not test these servers hands-on. Last updated May 2026.*

*This review was last edited on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*

