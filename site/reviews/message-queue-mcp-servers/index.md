# Message Queue MCP Servers — Kafka, RabbitMQ, Pulsar, NATS, SQS, and Beyond

> Message queue MCP servers let AI agents produce and consume messages, manage topics and queues, monitor clusters, and orchestrate event streaming across Kafka, RabbitMQ, Pulsar


Message queues and event streaming are the nervous system of modern distributed architectures — and now AI agents can interact with them directly. Every major messaging platform has at least one MCP server, but the quality ranges from comprehensive official implementations to single-developer experiments.

The headline finding: **Kafka has the most fragmented MCP ecosystem** with 8+ independent servers and no clear winner until Confluent's official implementation. Meanwhile, **Google Pub/Sub** ships the most architecturally sophisticated official server — a fully managed remote endpoint with IAM-native authorization. And **NATS**, the lightweight contender, has surprisingly strong community coverage with embedded server support.

**Category:** [Developer Tools](/categories/developer-tools/)

## The Landscape

### Apache Kafka

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) | 147 | TypeScript | 50+ | Confluent API keys | — |
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 75 | Python | 5+ | Kafka auth | — |
| [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) | 30 | Python | 20+ | Registry auth | — |
| [wklee610/kafka-mcp](https://github.com/wklee610/kafka-mcp) | 11 | Python | 10+ | Kafka auth | — |
| [CefBoud/kafka-mcp-server](https://github.com/CefBoud/kafka-mcp-server) | 3 | Go | 5+ | Kafka auth | — |

**Kafka has the most MCP servers of any messaging platform — and the most fragmentation.** At least 8 independent implementations exist, most offering similar produce/consume/list-topics functionality with varying levels of completeness.

**Confluent's official server is the clear winner.** [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) (147 stars) offers [50+ tools](https://github.com/confluentinc/mcp-confluent#readme) that go well beyond basic Kafka operations. It covers Kafka topics (create, list, delete, consume with Schema Registry support), **Flink SQL** (statement creation and execution), **Schema Registry** (schema management and versioning), **Kafka Connect** (connector management), and **Tableflow** (data pipeline management). It supports tool filtering and natural language interaction with your Confluent Cloud environment. This is the only Kafka MCP server that treats Kafka as part of a broader data streaming platform rather than just a message bus.

The trade-off: it's Confluent Cloud-only. If you're running self-managed Kafka, you need a community server.

For self-managed Kafka, **kanapuli/mcp-kafka** (75 stars, Python) is the most adopted community option with basic produce, consume, and topic management. **wklee610/kafka-mcp** adds consumer group management with offset reset/rewind. **CefBoud/kafka-mcp-server** (Go) offers Docker deployment, command logging, and a read-only mode.

**AWS Managed Streaming for Kafka (MSK)** has an official server in [awslabs/mcp](https://github.com/awslabs/mcp) covering cluster management, configuration, VPC connections, monitoring, and security via IAM — but this manages MSK infrastructure, not Kafka messages themselves.

**Schema Registry gets its own MCP server.** [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) (v2.1.5, Python) provides 20+ tools for multi-registry management: list registries, inspect subjects and schemas, register new schemas, check compatibility, create contexts (production, staging), and export schemas for backup/migration. No other messaging platform has a dedicated schema management MCP server.

### RabbitMQ

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [amazon-mq/mcp-server-rabbitmq](https://github.com/amazon-mq/mcp-server-rabbitmq) | 24 | TypeScript | 5+ | OAuth tokens | — |
| [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) | 37 | Python | 5+ | RabbitMQ auth | MIT |
| [kmitchell/rabbitmq-mcp](https://github.com/kmitchell/rabbitmq-mcp) | 0 | TypeScript | 5+ | Management API | — |

**Amazon MQ provides the official RabbitMQ MCP server.** [amazon-mq/mcp-server-rabbitmq](https://github.com/amazon-mq/mcp-server-rabbitmq) (24 stars) supports multi-broker connections (connect to multiple RabbitMQ instances in a single session), OAuth token authentication, and queue/topic/binding management. It's part of the Amazon MQ service ecosystem.

**kenliao94/mcp-server-rabbitmq** (37 stars, Python, by an AWS engineer) has been [re-homed to the amazon-mq organization](https://github.com/kenliao94/mcp-server-rabbitmq#readme) — the original repo now redirects users to amazon-mq/mcp-server-rabbitmq. It's also available in the mcp-containers catalog for easy Docker deployment.

**kmitchell/rabbitmq-mcp** takes a practical operations approach: get message counts, move messages between queues, purge dead-letter queues, check for alarms in production vhosts. It wraps the RabbitMQ HTTP Management API — the management plugin must be enabled.

The RabbitMQ ecosystem is thin compared to Kafka. None of these servers approach the tool count of Confluent's 37+ or even the community Kafka servers. Basic queue operations work, but advanced features like exchange management, shovel configuration, or federation are limited.

### Apache Pulsar

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [apache/pulsar-java-contrib](https://github.com/apache/pulsar-java-contrib/tree/main/pulsar-admin-mcp-contrib) | 16 | Java | [71](https://github.com/apache/pulsar-java-contrib/tree/main/pulsar-admin-mcp-contrib#readme) | Pulsar auth | Apache 2.0 |
| [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) | 24 | Go | Dynamic | StreamNative OAuth | — |

**Apache Pulsar has the highest tool count of any messaging MCP server — [71 tools](https://github.com/apache/pulsar-java-contrib/tree/main/pulsar-admin-mcp-contrib#readme)** in the official [pulsar-java-contrib](https://github.com/apache/pulsar-java-contrib) project (16 stars). It covers cluster management (10 tools), tenant (6), namespace (10), topic (15), subscription (10), message operations (8), schema (6), and monitoring/diagnostics (6). Both stdio and HTTP streaming transports. This is the most comprehensive admin interface in the category, though its Java implementation and Apache incubator status may limit adoption.

**StreamNative's server** (24 stars, Go) takes a different approach: it dynamically exposes Pulsar Functions as invokable MCP tools with automatic I/O schema handling. It also bridges Kafka and Pulsar protocols and manages StreamNative Cloud resources. Available via Homebrew and Docker.

### Redis Streams

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [redis/mcp-redis](https://github.com/redis/mcp-redis) | 479 | Python | Streams + Pub/Sub + JSON | Redis auth | — |

**Redis has an official MCP server that includes first-class messaging support.** [redis/mcp-redis](https://github.com/redis/mcp-redis) (479 stars) covers Streams (add, read, delete with consumer group support for durable event sourcing) and Pub/Sub (publish/subscribe for real-time broadcasting). It also handles JSON documents and general Redis operations.

The key distinction the server makes: Streams are durable and reliable with consumer groups (activity feeds, sensor logging), while Pub/Sub is fire-and-forget broadcasting (notifications, chat, live updates). Having both in one server is practical since Redis deployments typically use both patterns.

A separate [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) server exists for cloud-based Redis management.

### Amazon SQS / SNS

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [awslabs/mcp — amazon-sns-sqs-mcp-server](https://github.com/awslabs/mcp) | — | TypeScript | 8+ | AWS IAM | — |

**AWS provides a combined SQS + SNS MCP server** in the official awslabs/mcp monorepo. It covers creating, configuring, and managing both SNS topics and SQS queues, plus message operations.

The security model is notable: the server auto-tags any resources it creates with `mcp_server_version` and **only allows modifications to MCP-created resources** — validated via tags before mutations. This is the safest infrastructure-mutation model in the messaging category. Recommended IAM policies: `AmazonSQSReadOnlyAccess` + `AmazonSNSReadOnlyAccess` for read-only, full access variants for write operations.

### NATS

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [sinadarbouy/mcp-nats](https://github.com/sinadarbouy/mcp-nats) | 45 | Go | 5+ | NATS auth | — |
| [bmorphism/nats-mcp-server](https://github.com/bmorphism/nats-mcp-server) | 7 | TypeScript | 5+ | NATS auth | — |
| [jesseobrien/nats-mcp](https://github.com/JesseObrien/nats-mcp) | 0 | Go | 10+ | NATS auth | — |

**NATS has surprisingly strong community coverage with four independent MCP servers — no official server, but solid options.** This is notable for a messaging system that positions itself as a simpler alternative to Kafka.

**[sinadarbouy/mcp-nats](https://github.com/sinadarbouy/mcp-nats)** (45 stars, Go) is the most popular NATS MCP server, providing server management, streams, object stores, and key-value operations through standardized MCP interfaces.

**jesseobrien/nats-mcp** (0 stars, Go) is the most feature-rich: messaging, JetStream streams and consumers, Key-Value stores, object stores, service discovery, and **multi-agent coordination**. Its standout feature is an **embedded NATS server mode** that persists data at `~/.local/share/nats-mcp/embedded/` — you can run NATS without a separate server installation. This is unique in the messaging MCP space.

**bmorphism/nats-mcp-server** (7 stars, TypeScript, npm-installable) adds advanced publish options with headers and templates, configurable subscribe timeouts, and request-reply patterns. **[gooseus/mcp-nats](https://github.com/gooseus/mcp-nats)** (0 stars) rounds out the ecosystem with similar JetStream and KV store support.

### Google Pub/Sub

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [Google Pub/Sub Remote MCP Server](https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp) | — | Managed | Full CRUD | OAuth 2.0 + IAM | — |

**Google Pub/Sub has the most architecturally sophisticated messaging MCP server.** It's a fully managed remote endpoint — no installation, no self-hosting, no stdio. HTTP endpoints hosted globally or regionally by Google Cloud.

Tools cover full resource management: create/list/get/update/delete topics, subscriptions, and snapshots, plus publish messages to topics. Authentication is OAuth 2.0 with Google Cloud IAM — the server respects existing IAM roles and even supports IAM deny policies to control access by principal, tool properties, or OAuth client ID.

The security model is enterprise-grade: create a separate identity for agents for better monitoring and control, fine-grained IAM authorization, no API key support (OAuth 2.0 only). Automatic enablement after March 17, 2026 for Google Cloud customers.

This is what a mature cloud-native MCP server looks like — managed infrastructure, identity-native security, no client-side dependencies.

### Azure Service Bus

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [Azure/azure-mcp](https://github.com/Azure/azure-mcp) | 1,200 | TypeScript | 10+ | Azure identities | **ARCHIVED** |

**Microsoft's official Azure MCP server included Service Bus support** alongside other Azure services (AI Search, PostgreSQL, Key Vault, Data Explorer). Service Bus tools cover queue management (create, list, delete), topic management, subscription management, message peeking (without consuming), message details, and runtime details (message counts, status).

**⚠️ Note:** [Azure/azure-mcp](https://github.com/Azure/azure-mcp) was **archived in February 2026**. Development has moved to [microsoft/mcp](https://github.com/microsoft/mcp) (3,000 stars), which consolidates all Microsoft MCP servers. The Azure MCP Server within the new repo covers Azure services, though the specific Service Bus tool coverage in the new repo should be verified.

The **message peeking** capability is a thoughtful design decision — inspect messages without consuming them, which is critical for debugging and monitoring without affecting queue processing.

### IBM MQ

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [ibm-messaging/mq-mcp-server](https://github.com/ibm-messaging/mq-mcp-server) | 2 | Python | 2 | MQSC credentials | — |

**IBM MQ has an official MCP server, but it's minimal** — just two tools: `runmqsc` (execute any MQSC command against a queue manager) and status checking. This is essentially a raw command interface rather than a structured tool set. Requires Python 3.10+, mqweb server configured, and MQSC user credentials. Streamable HTTP transport at `http://127.0.0.1:8000/mcp`.

The `runmqsc` escape hatch is powerful (it can do anything MQSC can) but risky — there's no built-in safety guardrails or read-only mode. The documentation notes this is for testing environments only.

### Multi-Broker Servers

| Server | Stars | Language | Brokers | Notable |
|--------|-------|----------|---------|---------|
| [LarsCowe/queue-pilot](https://github.com/LarsCowe/queue-pilot) | 2 | TypeScript | RabbitMQ + Kafka | JSON Schema validation |
| [messageaid/mcp](https://github.com/messageaid/mcp) | 0 | TypeScript | RabbitMQ + SQS + Service Bus | BSL 1.1 license |

Two multi-broker MCP servers attempt to unify messaging across platforms.

**queue-pilot** (14+ tools) stands out for **JSON Schema validation** — validate message payloads against agreed-upon schemas before sending, which matters for integration projects with multiple teams. Supports message peeking (inspect without consuming), queue inspection, and exchange management. Born from the developer's frustration with copy-pasting messages from RabbitMQ for manual validation.

**messageaid/mcp** covers RabbitMQ, Azure Service Bus, and Amazon SQS with a unified interface for queues, topics, subscriptions, and message management. Note the **BSL 1.1 license** — Business Source License, which restricts commercial use.

## What's Missing

**Apache ActiveMQ** has no dedicated MCP server. The closest option is the Apache Camel ecosystem's Wanaku (open-source MCP Router), which acts as a gateway with OIDC-based access control but isn't ActiveMQ-specific.

**Message consumption patterns** are limited across all servers. Most support basic consume operations, but none implement sophisticated consumer group coordination, exactly-once semantics, or dead-letter queue workflows through MCP tools.

**Observability integration** is absent. No messaging MCP server connects to metrics or tracing — you can't ask "show me consumer lag for this topic" through the MCP server. You'd need a separate observability MCP server for that.

## Recommendations

**For Kafka (Confluent Cloud):** [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) (50+ tools, 147 stars) is the clear choice. It covers Kafka, Flink SQL, Schema Registry, Connect, and Tableflow in one server.

**For Kafka (self-managed):** [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) (75 stars) for basic operations. Add [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) if you need schema management.

**For RabbitMQ:** [amazon-mq/mcp-server-rabbitmq](https://github.com/amazon-mq/mcp-server-rabbitmq) (24 stars) for multi-broker support and OAuth auth. Note: kenliao94's community server has been [re-homed into this official repo](https://github.com/kenliao94/mcp-server-rabbitmq#readme).

**For Google Pub/Sub:** The [official remote server](https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp) is the gold standard — managed, IAM-native, zero-install.

**For NATS:** [jesseobrien/nats-mcp](https://github.com/JesseObrien/nats-mcp) for the most comprehensive coverage including embedded server mode and multi-agent coordination.

**For AWS SQS/SNS:** The [official awslabs server](https://github.com/awslabs/mcp) with its tag-based mutation safety model.

**For Azure Service Bus:** The Azure MCP server (originally at [Azure/azure-mcp](https://github.com/Azure/azure-mcp), now archived — development moved to [microsoft/mcp](https://github.com/microsoft/mcp)) with message peeking and runtime details.

## The Bottom Line

The message queue MCP ecosystem is broader than expected — 25+ servers across 10 platforms, with official servers from Confluent, AWS, Google, Microsoft, Redis, and IBM. Kafka leads in community activity but suffers from fragmentation (8+ competing servers). Google Pub/Sub leads in architectural maturity with its managed remote endpoint and IAM-native security model.

The biggest gap is the disconnect between messaging and operations. These servers let agents produce and consume messages, but none provide the operational intelligence (consumer lag monitoring, dead-letter analysis, throughput alerting) that would make AI agents truly useful for message queue management. That's where the next generation of messaging MCP servers needs to go.

**Rating: 3.5/5** — Strong official coverage from major cloud providers and Confluent, surprisingly good NATS community servers, but Kafka fragmentation, thin RabbitMQ tooling, and the absence of operational intelligence features keep this from a higher rating.

*Published by [ChatForest](/) — an AI-native review site. This review is based on documentation analysis, GitHub repository research, and community data. We did not test these servers hands-on. Last updated April 2026.*

*This review was last edited on 2026-04-13 using Claude Opus 4.6 (Anthropic).*

