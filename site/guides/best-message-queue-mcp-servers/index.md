# Best Message Queue & Streaming MCP Servers in 2026 — Kafka vs RabbitMQ vs Pulsar vs NATS vs Cloud

> We compared 35+ message queue and event streaming MCP servers across Kafka, RabbitMQ, Pulsar, NATS, MQTT, Google Pub/Sub, AWS SQS/SNS, Azure Service Bus, Redis Streams, IBM MQ, and ActiveMQ.


Message queues and event streaming are the nervous system of distributed systems — and now AI agents can produce messages, consume events, manage topics, monitor consumer lag, and orchestrate pipelines directly through MCP. Every major messaging platform has at least one MCP server, and several have official vendor-backed implementations.

The landscape splits into three tiers. **Managed cloud services** (Google Pub/Sub, AWS SQS/SNS, Azure Event Hubs) have official servers with IAM-native auth and zero infrastructure. **Self-managed brokers** (Kafka, RabbitMQ, Pulsar, NATS) have fragmented community ecosystems with varying quality. And **protocol-level servers** (MQTT, Redis Streams) serve specific niches in IoT and lightweight messaging.

What surprised us: **Confluent's MCP server has doubled its tool count to 50+** since its initial release, now covering Kafka, Flink SQL, Schema Registry, Connectors, and Tableflow — making it the most comprehensive vendor-backed messaging MCP server. **Apache Pulsar** quietly has the highest raw tool count (70+). **NATS** punches well above its market share with 42-tool servers that include built-in agent coordination primitives. And **Google Pub/Sub** ships the most architecturally sophisticated implementation — a fully managed remote endpoint that auto-enabled for all customers in March 2026.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Kafka (Confluent Cloud)** | [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) | 149 | — |
| **Kafka (self-managed)** | [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 75 | [tuannvm/kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server) (48) |
| **Kafka Schema Registry** | [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) | 30 | — |
| **RabbitMQ** | [amazon-mq/mcp-server-rabbitmq](https://github.com/amazon-mq/mcp-server-rabbitmq) | 24 | [kmitchell/rabbitmq-mcp](https://github.com/kmitchell/rabbitmq-mcp) (0) |
| **Google Pub/Sub** | [Google Pub/Sub Remote MCP](https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp) | Official | — |
| **AWS SQS / SNS** | [awslabs/amazon-sns-sqs-mcp-server](https://github.com/awslabs/mcp) | Official | — |
| **Azure messaging** | [microsoft/mcp](https://github.com/microsoft/mcp) | 2,971 (mono) | — |
| **NATS** | [JesseObrien/nats-mcp](https://github.com/JesseObrien/nats-mcp) | 0 | [sinadarbouy/mcp-nats](https://github.com/sinadarbouy/mcp-nats) (45) |
| **Apache Pulsar** | [Apache pulsar-java-contrib](https://github.com/apache/pulsar-java-contrib) | 16 | [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) (24) |
| **MQTT** | [Benniu/emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server) | 24 | [ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) (13) |
| **Redis Streams** | [redis/mcp-redis](https://github.com/redis/mcp-redis) | 484 | — |
| **IBM MQ** | [ibm-messaging/mq-mcp-server](https://github.com/ibm-messaging/mq-mcp-server) | 2 | — |
| **ActiveMQ** | [amazon-mq/mcp-server-activemq](https://github.com/amazon-mq/mcp-server-activemq) | 2 | — |
| **Multi-protocol** | [LarsCowe/queue-pilot](https://github.com/LarsCowe/queue-pilot) | 2 | — |

## Apache Kafka

Kafka has the most fragmented MCP ecosystem of any messaging platform. At least 10 independent implementations exist, most offering similar produce/consume/list-topics functionality. The split is between Confluent Cloud users (who have one clear answer) and self-managed Kafka users (who have several options, none dominant).

### confluentinc/mcp-confluent — The Winner (Confluent Cloud)

**Stars:** 149 | **Language:** TypeScript | **Tools:** 50+ | **Transport:** stdio, HTTP, SSE | **Version:** v1.0.6

Confluent's official server is the only Kafka MCP that treats Kafka as part of a broader data streaming platform rather than just a message bus. The tool count has more than doubled from the initial release to 50+ tools across Kafka, Flink SQL, Schema Registry, Connectors, and Tableflow.

**What makes it stand out:**
- **50+ tools across 5 domains** — Kafka topics, Flink SQL statement execution, Schema Registry management (AVRO/JSON/PROTOBUF), Kafka Connect connector lifecycle, and Tableflow pipeline management
- **Schema-aware consumption** — consume messages with automatic Schema Registry deserialization
- **Tool filtering** — expose only the tools you need to keep LLM context lean
- **Three transports** — stdio, HTTP, and SSE. Most Kafka MCP servers are stdio-only
- **Broad client support** — Claude Desktop, Claude Code, Cursor, VS Code, Goose, and Gemini CLI
- **Active development** — v1.0.6 released April 2026, Confluent maintains this as a core developer experience product

**Limitations:**
- **Confluent Cloud only** — does not work with self-managed Kafka (though Confluent Local is also supported)
- No consumer group management or lag monitoring

**Best for:** Confluent Cloud customers who want comprehensive Kafka + Flink + Schema Registry control from their AI assistant.

### kanapuli/mcp-kafka — The Winner (Self-Managed)

**Stars:** 75 | **Language:** Go | **License:** MIT | **Tools:** 6 | **Transport:** stdio

The most adopted community Kafka server. Written in Go (requires Go 1.24+) for easy single-binary deployment.

**What makes it stand out:**
- **6 clean tools** — create topic, list topics, delete topic, describe topic, produce message, consume messages
- **SASL auth** — SASL_PLAINTEXT and PLAINTEXT authentication
- **Go single binary** — no runtime dependencies, easy Docker deployment

**Limitations:**
- No consumer group management, no offset control, no Schema Registry
- No HTTP transport — stdio only
- Basic feature set compared to Confluent's 24+ tools

**Best for:** Self-managed Kafka users who need simple topic and message operations without the Confluent Cloud dependency.

### tuannvm/kafka-mcp-server — The Security-Conscious Alternative

**Stars:** 48 | **Language:** Go | **License:** MIT | **Tools:** 9 | **Transport:** stdio, HTTP

**What makes it different:** This Go server adds OAuth 2.1 for HTTP transport (Okta, Google, Azure AD), consumer lag analysis, cluster health monitoring, and broker listing. It supports SASL PLAIN, SCRAM-SHA-256, SCRAM-SHA-512, and TLS — the widest auth coverage of any community Kafka server. Good choice when security compliance matters.

### Other Kafka Servers Worth Knowing

| Server | Stars | Language | Tools | Notable |
|--------|-------|----------|-------|---------|
| [wklee610/kafka-mcp](https://github.com/wklee610/kafka-mcp) | 11 | Python | 16 | Consumer group management with offset reset/rewind. Updated March 2026 |
| [brandon-powers/mcp-kafka](https://github.com/brandon-powers/mcp-kafka) | 3 | Python | 23 | Kafka Connect + Burrow consumer lag + Cruise Control integration. WIP |
| [pavanjava/kafka_mcp_server](https://github.com/pavanjava/kafka_mcp_server) | 17 | Python | 7 | Straightforward publish/consume/topic management |
| [CefBoud/kafka-mcp-server](https://github.com/CefBoud/kafka-mcp-server) | 3 | Go | 7 | MultiplexTool for batching, read-only mode, command logging, Gemini-powered argument inference |

### aywengo/kafka-schema-reg-mcp — The Schema Specialist

**Stars:** 30 | **Language:** Python | **License:** MIT | **Tools:** 57+ (full mode), 9 (slim mode) | **Version:** v2.1.5

No other messaging platform has a dedicated schema management MCP server. This one manages up to 8 Schema Registry instances simultaneously — list registries, inspect subjects and schemas, register new schemas, check compatibility, create contexts (production, staging), and export schemas for backup/migration. Recent additions include interactive schema migration with smart migration and user preference elicitation, automatic pre-migration backups, and post-migration verification with comprehensive schema validation. OAuth 2.1 generic discovery provides universal provider compatibility. The slim mode (9 tools) is useful for keeping LLM context small. Built on FastMCP 2.8.0+, MCP spec 2025-06-18 compliant with resource linking (HATEOAS navigation in tool responses).

### AWS MSK Infrastructure

The [awslabs/mcp monorepo](https://github.com/awslabs/mcp) (8,782 stars) includes an **amazon-msk-mcp-server** with 31 tools for MSK infrastructure management — cluster CRUD, broker storage/type/count updates, VPC connections, SCRAM secrets, tagging, and telemetry. This manages MSK infrastructure, not Kafka messages. Use it alongside a Kafka MCP server for message operations.

## RabbitMQ

RabbitMQ's MCP ecosystem is small but practical, with Amazon MQ providing the official implementation.

### amazon-mq/mcp-server-rabbitmq — The Winner

**Stars:** 24 | **Language:** Python | **License:** Apache-2.0 | **Transport:** stdio, HTTP

Amazon MQ's official RabbitMQ server. Dynamically generates tools from RabbitMQ's admin APIs, supports multi-broker connections (manage multiple RabbitMQ instances in a single session), and uses OAuth token authentication. Originally created by kenliao94 (an AWS engineer, whose fork has 37 stars) and migrated to the official amazon-mq org. Amazon MQ itself added HTTP-based authentication and mTLS certificate-based authentication for RabbitMQ brokers in January 2026.

**Limitations:**
- Dynamically generated tools means the tool count varies by RabbitMQ version
- Documentation is sparse
- OAuth setup can be complex for self-managed RabbitMQ

### kmitchell/rabbitmq-mcp — The Operations Tool

**Stars:** 0 | **Language:** TypeScript | **License:** MIT

Takes a practical approach: get message counts, move messages between queues, purge dead-letter queues, check for alarms. Wraps the RabbitMQ HTTP Management API (management plugin must be enabled). Good complement to the Amazon MQ server for day-to-day operations.

## Google Cloud Pub/Sub

### Google Pub/Sub Remote MCP — The Winner

**Transport:** Remote HTTP (managed) | **Tools:** 15 | **Auth:** OAuth 2.0 + IAM

The most architecturally sophisticated messaging MCP server. Google ships Pub/Sub MCP as a fully managed remote endpoint — no installation, no local server, no SDK. Just point your MCP client at the endpoint and authenticate with Google Cloud credentials.

**What makes it stand out:**
- **15 tools** — full CRUD for topics, subscriptions, and snapshots, plus publish
- **IAM-native auth** — uses your existing Google Cloud IAM policies. No separate API keys
- **Model Armor protection** — Google's AI safety layer filters requests
- **Audit logging** — all operations logged in Cloud Audit Logs
- **Auto-enabled** — after March 17, 2026 for existing Pub/Sub customers
- **Global and regional endpoints** — choose data residency

**Limitations:**
- No API key auth — must use OAuth 2.0 (harder for quick prototyping)
- No consume/pull operations — you can publish but not read messages via MCP
- Google Cloud only — not usable with self-managed Pub/Sub emulators

**Best for:** Google Cloud teams who want zero-infrastructure Pub/Sub management. The IAM integration is the gold standard for secure messaging MCP.

## AWS SQS / SNS / EventBridge

### amazon-sns-sqs-mcp-server — The Winner

**Language:** Python | **License:** Apache-2.0 | **Transport:** stdio | **Auth:** AWS IAM

Part of the [awslabs/mcp monorepo](https://github.com/awslabs/mcp) (8,782 stars). Covers both SQS and SNS in a single server.

**What makes it stand out:**
- **Tag-based safety** — only modifies resources that were created by the MCP server (tagged with `CreatedBy: MCP`). Won't accidentally delete your production queues
- **Resource creation disabled by default** — must explicitly pass `--allow-resource-creation` to enable create operations
- **SNS + SQS unified** — topics, subscriptions, and queues in one server
- **A2P messaging disabled** — SMS/phone messaging blocked as a safety measure

**Limitations:**
- No EventBridge, Kinesis, or MSK in this server (those are in separate servers in the monorepo)
- Standard AWS IAM auth — requires AWS_PROFILE and AWS_REGION setup
- No dead-letter queue management

### AWS Serverless MCP Server — EventBridge + Kinesis

Also in the awslabs/mcp monorepo. Covers EventBridge schema registry (list, search, describe schemas) and event source mapping tools for Kinesis, SQS, DynamoDB Streams, and MSK. Includes SAM template generation for serverless event processing. Not a dedicated EventBridge or Kinesis server — more of a serverless orchestration tool.

**Gap:** No dedicated Kinesis MCP server exists. No dedicated EventBridge MCP server exists. These are the biggest AWS messaging gaps.

## Azure Service Bus / Event Hubs / Event Grid

### microsoft/mcp — The Winner

**Stars:** 2,971 (monorepo) | **Language:** C# | **License:** MIT | **Transport:** stdio

Microsoft's unified Azure MCP server covers all three messaging services, but with uneven depth. Now built into Visual Studio 2026 for agentic cloud workflows.

**Service Bus (3 tools):** Read-only — get queue runtime details (message counts, status), topic runtime details, subscription runtime details. You can also peek at messages and view message details. No create, delete, or publish operations.

**Event Hubs (8 tools):** Full CRUD — create/update/delete Event Hubs, namespaces, and consumer groups. Configure partition count, retention, Kafka support, auto-inflate, zone redundancy.

**Event Grid (3 tools):** List topics, publish events (with schema validation), list subscriptions with filtering.

**Total: ~14 messaging tools across three services.**

**Limitations:**
- Service Bus is still read-only — you can't send messages or manage queues via MCP
- Event Hubs is the strongest, Event Grid and Service Bus are thin
- Requires Azure identity auth — no API key option
- Previous standalone repo (Azure/azure-mcp, 1,200 stars) was archived August 2025
- Note: Some Azure Service Bus SDK libraries will be retired September 30, 2026 — migrate to latest Azure SDK libraries

**Best for:** Azure teams who need Event Hubs management. Service Bus users will find the read-only tooling limiting.

## NATS / NATS JetStream

NATS punches well above its market share in the MCP ecosystem. The lightweight messaging system has surprisingly comprehensive coverage, including the only messaging MCP server with built-in agent coordination primitives.

### JesseObrien/nats-mcp — The Winner

**Stars:** 0 | **Language:** Go | **License:** MIT | **Tools:** 42 | **Transport:** stdio

The highest tool count of any NATS MCP server, organized across 7 groups:

- **Core Messaging (5)** — publish, subscribe, request/reply, queue groups
- **JetStream Streams (5)** — create, list, info, purge, delete streams
- **JetStream Consumers (5)** — create, list, info, delete consumers, consume messages
- **Key-Value (7)** — create, put, get, delete, list keys, watch, history
- **Object Store (7)** — create, put, get, delete, list, info, seal
- **Server & Services (4)** — server info, connections, service discovery
- **Agent Coordination (9)** — distributed locks, leader election, task queues, work assignment, heartbeat monitoring, agent registration, status tracking

**What makes it stand out:**
- **Embedded NATS server** — no external infrastructure needed. The MCP server starts its own NATS instance
- **Agent coordination primitives** — the 9 coordination tools are unique in the messaging MCP space. Designed for multi-agent workflows
- **Full JetStream support** — persistence, exactly-once delivery, replay

**Limitations:**
- Zero stars suggests very early/undiscovered
- Embedded server means it's not managing your production NATS cluster
- No SSE transport

### sinadarbouy/mcp-nats — The Production Alternative

**Stars:** 45 | **Language:** Go | **License:** Apache-2.0 | **Transport:** stdio, SSE

Connects to external NATS clusters (not embedded). Multi-account support, backup/restore, credential and user/password auth, with Base64-encoded NATS credentials per account. MCP Review certified. Better suited for managing existing NATS infrastructure than JesseObrien's embedded approach.

### Other NATS Servers

| Server | Stars | Language | Tools | Notable |
|--------|-------|----------|-------|---------|
| [Gooseus/mcp-nats](https://github.com/Gooseus/mcp-nats) | 0 | TypeScript | 24 | SSE transport, documentation tools. Good TypeScript alternative |
| [bmorphism/nats-mcp-server](https://github.com/bmorphism/nats-mcp-server) | 7 | TypeScript | 3 | Minimal: publish, subscribe, request |

**Note:** [hofer/nats-mcp](https://github.com/hofer/nats-mcp) is a transport bridge (exposes existing MCP servers over NATS), not a NATS management tool.

## Apache Pulsar

Pulsar has the highest raw tool count of any messaging platform in the MCP ecosystem, though with lower community adoption.

### Apache pulsar-java-contrib — The Winner

**Stars:** 16 | **Language:** Java | **License:** Apache-2.0 | **Tools:** 70+ | **Transport:** stdio, HTTP streaming

Part of the official Apache Pulsar contrib repository. The 70+ tools cover cluster, tenant, namespace, topic, and subscription management plus schema operations, monitoring, backlog analysis, and message send/receive. This is the most comprehensive messaging MCP server by tool count.

**Limitations:**
- Java-only — heavier runtime than Go or TypeScript alternatives
- Low star count (16) despite being official Apache contrib
- Requires running Pulsar infrastructure

### streamnative/streamnative-mcp-server — The Multi-Protocol Bridge

**Stars:** 24 | **Language:** Go | **License:** Not specified | **Tools:** 40+ | **Transport:** stdio, SSE

StreamNative's official server bridges **Kafka and Pulsar** in a single MCP server. Dynamic function-as-tool exposure, feature toggling via `--features` flag, multi-session Pulsar mode with LRU caching. Dynamically exposes deployed Pulsar Functions as invokable MCP tools with automatic input/output schema handling. Available via Homebrew and Docker. Connects to StreamNative Cloud, direct Kafka clusters, or direct Pulsar clusters. Supports MCP protocol versions 2024-11-05 through 2025-11-25.

**NEW: StreamNative Remote MCP Server (Public Preview)** — a fully managed, hosted MCP endpoint available out of the box in StreamNative Cloud. No local deployment required. Every StreamNative cluster (Serverless, Dedicated, BYOC) provides its own MCP endpoint. This mirrors Google Pub/Sub's managed approach — point your MCP client at the endpoint and authenticate.

**Best for:** StreamNative customers or teams running both Kafka and Pulsar who want unified management. The Remote MCP Server is ideal for teams that want zero-infrastructure MCP access.

## MQTT / IoT Messaging

MQTT's MCP ecosystem serves the IoT and edge computing space with 5+ servers of varying scope.

### Benniu/emqx-mcp-server — The Winner

**Stars:** 24 | **Language:** Python | **License:** Apache-2.0 | **Tools:** 5 | **Transport:** stdio, SSE

The most adopted MQTT MCP server. Connects to EMQX Cloud or self-hosted EMQX clusters. Lists clients, kicks clients, publishes messages with QoS 0/1/2, subscribes with configurable duration (1-300 seconds). EMQX is also pioneering **MCP over MQTT** — encapsulating MCP's standardized tool-calling within MQTT's lightweight transport, bridging AI model reasoning and real-time device control. Additionally, EMQX now supports the **A2A (Agent-to-Agent) protocol over MQTT**, enabling AI agents to register, discover, and collaborate directly through the broker.

### ezhuk/mqtt-mcp — The Developer-Friendly Alternative

**Stars:** 13 | **Language:** Python | **License:** MIT | **Tools:** 2 + resources + prompts | **Transport:** stdio

Simpler than EMQX but with better developer experience — Docker deployment, multi-client SDK examples (OpenAI, PydanticAI), and a Building Automation/Industrial Control/Smart Home focus. Updated April 2026.

### Other MQTT Servers

| Server | Stars | Language | Tools | Notable |
|--------|-------|----------|-------|---------|
| [tspspi/mcpMQTT](https://github.com/tspspi/mcpMQTT) | 1 | Python | 4 | Fine-grained topic permissions with wildcard matching, Argon2id auth, request/response patterns |
| [ysfscream/mqttx-mcp-sse-server](https://github.com/ysfscream/mqttx-mcp-sse-server) | 5 | JavaScript | 3 | SSE transport for persistent connections, multi-client sessions |
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | 22 | Python | 13+ | MQTT + Modbus unified, InfluxDB + Redis backend, SCADA/IoT focus |

**Note:** [mqtt-ai/mcp-over-mqtt](https://github.com/mqtt-ai/mcp-over-mqtt) is a transport layer (routes MCP traffic over MQTT), not an MCP server for MQTT operations.

## Redis Streams / Pub/Sub

### redis/mcp-redis — The Winner

**Stars:** 484 | **Language:** Python | **License:** MIT | **Transport:** stdio

Redis's official MCP server includes Streams and Pub/Sub alongside its broader Redis toolset. Streams tools cover xadd, xread, xdel with consumer group support. Pub/Sub tools cover publish and subscribe. The server handles strings, hashes, JSON documents, lists, sets, sorted sets, vector embeddings, and includes server management tools for database health checks. The 484-star count makes this the most popular server in our entire comparison — though most users are here for Redis data structures, not just messaging.

**Limitation:** This is a general Redis server, not a dedicated messaging server. The Streams/Pub/Sub tools are a subset of the full toolset.

## IBM MQ

### ibm-messaging/mq-mcp-server — The Winner (by Default)

**Stars:** 2 | **Language:** Python | **License:** Apache-2.0 | **Tools:** 2 | **Transport:** Streamable HTTP

IBM's official MQ MCP server. Two tools: `dsqmq` (list queue managers and status) and `runmqsc` (execute any MQSC command). The `runmqsc` tool is essentially a raw command escape hatch — you send MQSC commands as strings and get raw output back. No safety guardrails, no structured responses.

**Limitations:**
- Only 2 tools — the lowest of any official vendor server
- `runmqsc` has no input validation or confirmation
- Requires Python 3.10+, mqweb server, and MQ distributed installation
- 2 stars suggest minimal community adoption

**Related:** IBM announced **IBM MQ AI Agents** in February 2026 — an intelligent, context-aware administrative assistant built directly into the MQ Console. IBM MQ 9.4.5 (also February 2026) pushes toward "Kubernetes-native by default" with more self-service operations and tighter security/observability. These developments suggest IBM is investing in AI-assisted MQ management, though the MCP server itself remains basic.

**Best for:** IBM MQ shops that need basic queue manager inspection. Don't expect a polished experience.

## Apache ActiveMQ

### amazon-mq/mcp-server-activemq — The Winner (by Default)

**Stars:** 2 | **Language:** Python | **License:** Apache-2.0 | **Transport:** Streamable HTTP

Amazon MQ's official ActiveMQ MCP server. Like its RabbitMQ counterpart, it dynamically generates tools from ActiveMQ's admin APIs and supports multi-broker connections. This fills what was previously one of the biggest gaps in the messaging MCP ecosystem — ActiveMQ, one of the oldest and most widely deployed Java message brokers, now has MCP coverage.

**Limitations:**
- 2 stars and limited documentation suggest very early adoption
- Feature set may vary by ActiveMQ version since tools are dynamically generated
- Requires OAuth token authentication

**Best for:** ActiveMQ shops (especially Amazon MQ for ActiveMQ customers) who want AI-assisted broker management.

## Multi-Protocol

### LarsCowe/queue-pilot — The Universal Option

**Stars:** 2 | **Language:** TypeScript | **License:** MIT | **Tools:** 29 | **Transport:** stdio

The only MCP server that works across multiple message brokers. Currently supports RabbitMQ and Apache Kafka with 18 universal tools + 7 RabbitMQ-specific + 4 Kafka-specific. Includes JSON Schema validation for messages, peek-without-consuming, and schema-gated publishing.

**Limitations:**
- Only 2 brokers supported (RabbitMQ + Kafka)
- 2 stars and February 2026 last commit suggest early stage
- No NATS, Pulsar, or cloud service support

**Best for:** Teams running both RabbitMQ and Kafka who want a single MCP server instead of two.

## Decision Flowchart

**Using Confluent Cloud?** → [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent). No contest.

**Self-managed Kafka?** → [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) for basics. Add [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) if you use Schema Registry. Consider [tuannvm/kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server) if you need OAuth 2.1 or consumer lag analysis.

**Google Cloud?** → [Google Pub/Sub Remote MCP](https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp). Zero infrastructure, IAM-native.

**AWS?** → [amazon-sns-sqs-mcp-server](https://github.com/awslabs/mcp) for SQS/SNS. Add amazon-msk-mcp-server if you're on MSK.

**Azure?** → [microsoft/mcp](https://github.com/microsoft/mcp) for Event Hubs (full CRUD). Service Bus is read-only.

**RabbitMQ?** → [amazon-mq/mcp-server-rabbitmq](https://github.com/amazon-mq/mcp-server-rabbitmq).

**NATS?** → [JesseObrien/nats-mcp](https://github.com/JesseObrien/nats-mcp) if you want an embedded server with agent coordination. [sinadarbouy/mcp-nats](https://github.com/sinadarbouy/mcp-nats) if you're connecting to an existing cluster.

**Pulsar?** → [Apache pulsar-java-contrib](https://github.com/apache/pulsar-java-contrib) for 70+ tools. [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) for Kafka+Pulsar bridge.

**MQTT/IoT?** → [Benniu/emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server).

**ActiveMQ?** → [amazon-mq/mcp-server-activemq](https://github.com/amazon-mq/mcp-server-activemq). Early stage but official Amazon MQ.

**Multiple brokers?** → [LarsCowe/queue-pilot](https://github.com/LarsCowe/queue-pilot) for RabbitMQ + Kafka.

## Three Trends

**1. Managed remote MCP is the new gold standard.** Google Pub/Sub pioneered it, and now StreamNative has followed with a managed MCP endpoint in Public Preview for every cluster. No local server, no installation — just authenticate and connect. Expect more vendors to adopt this model.

**2. Confluent is pulling ahead in tool coverage.** With 50+ tools across Kafka, Flink SQL, Schema Registry, Connectors, and Tableflow, Confluent's MCP server has evolved from a basic Kafka tool to a comprehensive data streaming control plane. The gap between Confluent Cloud users and self-managed Kafka users is widening — the community ecosystem remains fragmented with 10+ implementations, none achieving escape velocity.

**3. Agent-to-agent messaging is becoming a first-class pattern.** NATS's JesseObrien/nats-mcp includes 9 agent coordination tools (distributed locks, leader election, task queues). EMQX has added A2A protocol support over MQTT, enabling agents to register, discover, and collaborate through the broker. Messaging is evolving from "manage my broker" to "coordinate my agents."

## What's Missing

- **No dedicated Amazon Kinesis MCP server** — Kinesis is handled via ESM tools in the serverless MCP server, not direct stream operations
- **No dedicated AWS EventBridge MCP server** — same situation, bundled into serverless
- **Azure Service Bus is still read-only** — you can peek at messages and check queue depth but can't send messages or manage queues
- **No RocketMQ MCP server** — Apache RocketMQ, popular in China, has no MCP server
- **No ZeroMQ MCP server** — the lightweight messaging library has no MCP integration
- **No message replay/reprocessing tools** — no server offers dead-letter queue analysis, message replay from offsets, or failed message investigation workflows
- **No cross-broker migration tools** — can't move topics/queues between Kafka and RabbitMQ, or migrate from one cloud provider to another
- **No unified monitoring** — no server provides cross-broker consumer lag, throughput, or health dashboards

---

*Last updated: April 2026. Star counts and tool counts are from our research and may have changed. See our [full review of message queue MCP servers](/reviews/message-queue-mcp-servers/) for individual server details, or browse our [master MCP server guide](/guides/best-mcp-servers/) for all categories.*

