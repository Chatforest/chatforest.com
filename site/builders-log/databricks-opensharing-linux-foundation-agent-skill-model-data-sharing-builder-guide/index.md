# Databricks OpenSharing: The Open Protocol for Sharing Agent Skills, Models, and Data

> Databricks donated OpenSharing to the Linux Foundation on June 10, 2026 — an open protocol that extends Delta Sharing to cover agent skills, ML models, and unstructured volumes in addition to tables. 15+ founding members including OpenAI, Stripe, and SAP. Here's the technical architecture and builder decision tree.


Databricks announced **OpenSharing** on June 10, 2026 — six days before the Databricks Data + AI Summit (DAIS 2026) opened at Moscone Center. The timing was deliberate: seed press coverage before the keynotes, then validate the architecture with enterprise customer examples at the summit.

OpenSharing is the successor to Delta Sharing, the 2021 protocol Databricks originally donated to open source for sharing structured tabular data across platforms. The extension is large: where Delta Sharing handled tables only, OpenSharing adds agent skills, ML models, and file volumes — covering the full AI asset stack that organizations now need to distribute securely across teams and partner organizations.

The protocol is Apache 2.0 licensed, governed by the Linux Foundation AI & Data Foundation, and backward-compatible with all existing Delta Sharing clients. It is not a Databricks product — any server or client that implements the spec is a valid participant.

---

## What Delta Sharing Was, and Why the Extension Was Necessary

Delta Sharing launched in 2021 as the first open standard for sharing live data across platforms without copying it. The design was straightforward: a sharing server manages access grants, then vends short-lived cloud credentials that let recipients read data directly from the provider's cloud storage. No data movement, no intermediate copies, no single-vendor lock-in.

The protocol caught on. Delta Sharing clients exist for Apache Spark, pandas, Tableau, Power BI, Snowflake, Oracle, DuckDB, Clojure, Node.js, Java, Rust, Go, and C++. Thousands of Databricks customers use it for cross-organization data sharing. It became the most widely deployed open data-sharing protocol in the enterprise.

The problem that motivated OpenSharing: tables are only one type of asset organizations now need to share. As AI development matured, teams faced identical friction with:

- **Agent skills** — reusable packaged agent capabilities (tools, instructions, scripts) that an AI agent loads into its context. No standard for distributing them across teams or organizations.
- **ML model artifacts** — trained weights, config files, run provenance. Distributed via custom integrations or single-vendor registries.
- **Unstructured files** — documents, embeddings, evaluation datasets, media. Delta Sharing had no type for them.

OpenSharing adds these three types without breaking existing consumers. Every existing Delta Sharing client continues working. The new asset types each follow the same zero-copy credential-vending pattern the ecosystem already knows.

---

## Protocol Architecture

### Sharing Hierarchy

The three-tier structure is unchanged from Delta Sharing:

```
Share  (access-controlled collection granted to a recipient)
 └── Schema  (logical namespace within a share)
      └── Asset  (Table | Volume | AgentSkill | Model | ...)
```

A share is what you grant to a recipient — a named collection of schemas and assets with a bearer token or OIDC grant. Schemas organize assets within a share. Assets are the actual data or AI objects.

### Authentication

Bearer token authentication via `Authorization: Bearer <token>`. The protocol also supports OIDC federation (OAuth JWT exchange, both user-to-machine and machine-to-machine flows). Recipients receive a **profile file** — a JSON document containing the server endpoint URL, bearer token, and optional ISO 8601 expiration timestamp. The profile file is the credential artifact that a sharing server generates and delivers to an authorized recipient.

### Zero-Copy Credential Vending

The core mechanism is unchanged from Delta Sharing: the sharing server never holds data. Instead:

1. Recipient authenticates to the sharing server.
2. Recipient calls a `POST .../temporary-{asset}-credentials` endpoint for the asset they want.
3. Server returns **short-lived, scoped cloud credentials** tied to that asset's storage location.
4. Recipient reads data **directly from cloud storage** — the sharing server is no longer involved.

Supported cloud backends: AWS S3 (STS credentials), Azure ADLS Gen2 (User Delegation SAS tokens), GCP (OAuth tokens), Cloudflare R2. All credential responses include an `expirationTime` Unix timestamp. Scoping is per-asset storage location.

### Discovery API Endpoints

```
# Tables (unchanged from Delta Sharing)
GET /shares
GET /shares/{share}/schemas
GET /shares/{share}/schemas/{schema}/tables
GET /shares/{share}/all-tables

# New: Volumes
GET /shares/{share}/schemas/{schema}/volumes

# New: Agent Skills
GET /shares/{share}/schemas/{schema}/skills
GET /shares/{share}/all-skills

# New: ML Models
GET /shares/{share}/schemas/{schema}/models
GET /shares/{share}/all-models
GET /shares/{share}/schemas/{schema}/models/{model}/versions
GET /shares/{share}/schemas/{schema}/models/{model}/versions/{version}
```

All list endpoints support `maxResults` and `pageToken` query parameters for pagination.

### Credential Vending Endpoints (New Asset Types)

```
POST .../volumes/{volume}/temporary-volume-credentials
POST .../models/{model}/versions/{version}/temporary-model-version-credentials
POST .../skills/{skill}/temporary-skill-credentials
```

---

## Asset Types in Detail

### Table

Fully specified and implemented. Backward-compatible with all existing Delta Sharing clients. Supports the full Delta Lake feature set: deletion vectors, column mapping, Change Data Feed, time travel, materialized views, dynamic views with row/column filtering, and Uniform format (for Iceberg-native tool access).

The Iceberg compatibility is significant: when a provider stores Delta tables with Uniform format enabled, Iceberg-native tools — Flink, Trino, Snowflake Iceberg tables, Athena — can consume the same shared data via their native Iceberg clients. OpenSharing adds an Iceberg-compatible endpoint to profile files, expanding the consumer universe without changing provider storage.

### Volume

A Volume is a directory of files of any format: documents, PDFs, embeddings, images, audio, binary artifacts, raw outputs. There is no format constraint. Credential vending returns scoped access to the storage path; the recipient reads files directly.

This is the type that fills the gap for evaluation datasets, documentation corpora, unstructured retrieval archives, and model evaluation artifacts that teams already share informally via object storage links.

### Model

A Model in OpenSharing has two sub-objects:

**RegisteredModel** — the named, versioned family: `name`, `schema`, `share`, optional `comment`.

**ModelVersion** — a specific artifact version:

| Field | Notes |
|---|---|
| `version` | Integer version number |
| `status` | `PENDING_REGISTRATION`, `FAILED_REGISTRATION`, or `READY` |
| `storageLocation` | Root cloud path to artifact files |
| `runId` | Optional: training run provenance |
| `source` | Optional: source system reference |

Credential vending vends scoped credentials for the version's `storageLocation`. The consumer downloads artifacts directly from storage — no model serving layer involved, no vendor registry dependency.

### AgentSkill

This is the most architecturally significant new type. An AgentSkill is a **reusable AI capability packaged as a directory of files**, following the [AgentSkills specification](https://github.com/agentskills/agentskills) — an open format originally developed by Anthropic.

**Directory structure:**

```
skill-name/
├── SKILL.md           # Required: YAML frontmatter + markdown instructions
├── scripts/           # Optional: executable code
├── references/        # Optional: documentation, reference material
└── assets/            # Optional: templates, images, diagrams
```

**SKILL.md frontmatter (minimum required):** `name`, `description`

**OpenSharing AgentSkill object fields:**

| Field | Required | Notes |
|---|---|---|
| `name` | Yes | Lowercase, hyphens, numbers. Max 64 chars. Must match directory name |
| `schema` | Yes | Schema within the share |
| `share` | Yes | Parent share |
| `description` | Yes | What the skill does and when to use it. Max 1024 chars |
| `storageLocation` | Yes | Root cloud path to the skill directory |
| `license` | No | License reference |
| `compatibility` | No | Environment requirements. Max 500 chars |
| `allowedTools` | No | Space-separated pre-approved tool list |
| `metadata` | No | Arbitrary `Map<String, String>` |

**Progressive disclosure model:** Agents first scan `name` + `description` metadata via the discovery API. If relevant, they retrieve the full `SKILL.md`. Scripts and referenced files are loaded from storage only during execution. This keeps discovery cheap — an agent can page through hundreds of skills without loading large context payloads.

**Existing compatibility:** The AgentSkills format (the underlying file structure) is already supported by Claude Code, ChatGPT, Codex CLI, Cursor, GitHub Copilot, Goose, Gemini CLI, and Windsurf. OpenSharing adds the **distribution and access-control layer** — skills can now be published, versioned, discovered, and access-controlled the same way tables have been for five years.

---

## What Is Available Now

The specification is live on GitHub at [OpenSharing-IO/OpenSharing](https://github.com/OpenSharing-IO/OpenSharing), Apache 2.0 licensed.

Implementation status:

| Asset Type | Spec Status | Client Support |
|---|---|---|
| Table | Fully specified | All existing Delta Sharing clients |
| Volume | Specified | Clients in progress |
| Model | Specified | Clients in progress |
| AgentSkill | Specified | Credential vending defined; broader client integration in progress |
| Agent (live service) | Community proposal | Not yet specified |
| Page (semantic entities) | Community proposal | Not yet specified |

**Reference implementation:** Databricks has a built-in OpenSharing server in Unity Catalog-enabled workspaces. The [Delta Sharing open-source server](https://github.com/delta-io/delta-sharing) is the starting point for third-party implementations.

**On-premises storage partners (generally available now):** Everpure, MinIO (native in AIStor), Qumulo.

**On-premises storage partners (committed by end of 2026):** Cohesity, Commvault, HPE, NetApp, Nutanix, Rubrik, VAST Data.

---

## Founding Members

15+ organizations joined as founding members at announcement:

**AI ecosystem:** OpenAI, Databricks

**Enterprise data consumers:** SAP (Business Data Cloud connector), Stripe (Data Pipeline), LSEG (London Stock Exchange Group — "LSEG Everywhere" strategy), Atlassian, Amadeus, Acxiom, The Trade Desk

**Domain-specific:** Cotality (property intelligence), Kythera Labs (healthcare)

**Infrastructure:** MinIO (on-premises object storage)

The OpenAI membership is notable: it aligns the AgentSkills format across the two dominant agent platforms (Anthropic and OpenAI) under a common distribution layer.

---

## How OpenSharing Fits the Broader Stack

### Relationship to Unity Catalog

In Databricks, OpenSharing is built into Unity Catalog. Shares, schemas, recipients, and assets are securable objects registered in the Unity Catalog metastore. Unity Catalog handles:

- Audit logging of every credential-vend operation
- Access policies per recipient and per asset
- IP access lists
- Token lifetime configuration
- System table monitoring for share activity

If you are already on Databricks with Unity Catalog, existing tables, volumes, and registered models can be shared via OpenSharing without separate setup.

### Relationship to MCP

MCP (Model Context Protocol) and OpenSharing are complementary, not overlapping:

| Protocol | Pattern | When to Use |
|---|---|---|
| OpenSharing | Pull / credential-vend | Distributing assets: files, skills, model artifacts, tables. Consumer downloads at their own pace. |
| MCP | Tool call / invocation | Runtime agent behavior: calling a live tool, querying a running service, getting a response inline. |

A team publishing an agent skill could expose it via both: OpenSharing for distribution (recipients download the SKILL.md and scripts), MCP for runtime invocation (if the skill wraps a live API endpoint). These are different interaction patterns, and a well-designed skill distribution system may use both.

### Relationship to AgentSkills (Anthropic Format)

The AgentSkills SKILL.md format was originally developed by Anthropic as an open standard for packaging reusable agent capabilities. OpenSharing adopts it as the `AgentSkill` asset type — adding versioning, access control, discovery, and credential-vended delivery on top of the raw format.

The convergence: Anthropic-originated format + Databricks-originated distribution protocol + Linux Foundation governance = a complete, vendor-neutral stack for agent skill publishing and consumption.

---

## Builder Use Cases

### Cross-organization agent skill distribution

A fintech company packages a "regulatory-reporting" agent skill — SKILL.md with instructions, a Python script for data extraction, and reference documentation — and uploads it to S3. They register it in their OpenSharing server, grant a recipient token to a partner firm. The partner calls `GET /shares/partner-skills/schemas/compliance/skills`, finds the skill, calls `POST .../temporary-skill-credentials` to get a short-lived STS token, and downloads the skill directory from S3. The skill works in Claude Code, Cursor, or any AgentSkills-compatible agent — no SDK dependency.

### Multi-platform ML model distribution

An AI lab trains specialized models and publishes them with version metadata and run provenance via OpenSharing. Consumers query model versions, filter by `READY` status, credential-vend access, and download artifacts directly from GCS or ADLS. No proprietary model registry, no Hugging Face account required.

### On-premises to cloud AI pipeline (zero-copy)

A healthcare organization keeps PHI on MinIO (AIStor) running OpenSharing natively. A cloud-based AI pipeline queries both structured tables and unstructured document volumes via credential vending — the sharing server handles access control and the pipeline reads directly from on-premises storage. Zero data movement, zero ETL copy.

### Agentic skills discovery within an organization

An internal skills catalog server publishes all approved agent skills via OpenSharing. New agents page through `/shares/skills-catalog/all-skills`, read `name` + `description` for each skill to determine relevance, and lazy-load SKILL.md and scripts only for matching tasks. Discovery stays cheap because metadata is the only thing transmitted until a skill is actually selected.

### Iceberg consumer expansion

A team that stores data in Delta Lake with Uniform format enabled can now share that data with Iceberg-native consumers (Flink, Trino, Athena, Snowflake Iceberg tables) via OpenSharing's Iceberg-compatible endpoint — without changing their storage format or running a separate Iceberg catalog.

---

## Builder Decision Tree

**Should you publish agent skills via OpenSharing?**

- Skills are used across teams or organizations → Yes, strong fit
- Skills are internal to one team, no external consumers → Raw AgentSkills format in a shared repo may be sufficient for now; OpenSharing adds complexity you may not need yet
- You want access control and audit logging on skill access → Yes
- You are not on Databricks and need to self-host → The open-source spec is available, but reference implementations for non-Databricks servers are still maturing

**Should you publish models via OpenSharing?**

- Models are shared across organizations → Yes
- You want versioning and provenance tracking on artifact distribution → Yes
- You are already in Unity Catalog → Yes, minimal additional setup
- You need a public model hub (visibility, discoverability by strangers) → Not what OpenSharing is designed for; Hugging Face Hub remains the right venue for public model discovery

**Should you consume OpenSharing tables vs. wait for Delta Sharing deprecation?**

Delta Sharing is not deprecated — OpenSharing is backward-compatible. If you have existing Delta Sharing clients, they continue working. You only need to update clients if you want access to the new asset types (Volumes, Models, AgentSkills).

---

## Quick Start Checklist

**To publish via Databricks (simplest path):**

- [ ] Unity Catalog enabled workspace (required for built-in OpenSharing server)
- [ ] Assets registered in Unity Catalog (tables in a schema, volumes, models in Model Registry, or AgentSkill directories in a volume)
- [ ] Create a share in Unity Catalog and assign assets to it
- [ ] Add recipients with appropriate bearer token or OIDC configuration
- [ ] Verify with `GET /shares` via curl or your preferred HTTP client using recipient credentials

**To build a standalone OpenSharing server:**

- [ ] Review the spec at `github.com/OpenSharing-IO/OpenSharing`
- [ ] Start from the delta-sharing open-source reference server (handles Table sharing; extend for new types)
- [ ] Implement `temporary-{type}-credentials` endpoints for the asset types you need
- [ ] Use your existing cloud object storage for asset storage locations

**To consume AgentSkills via OpenSharing:**

- [ ] Obtain a profile file (JSON with endpoint URL and bearer token) from the sharing server
- [ ] `GET /shares/{share}/all-skills` to page through available skills
- [ ] Filter by `description` field for relevance
- [ ] `POST .../temporary-skill-credentials` to credential-vend
- [ ] Download skill directory from the storage location using the returned credentials
- [ ] Load `SKILL.md` into your agent's context per the AgentSkills spec

---

## What to Watch

**AgentSkill client maturity:** The spec is defined; the next step is native AgentSkill support in OpenSharing clients across the major agent frameworks. Watch the `OpenSharing-IO/OpenSharing` GitHub for client implementation PRs.

**Community proposals:** The Agent type (sharing a live callable agent service, not just files) and the Page type (sharing business entity definitions) are open proposals on GitHub. If adopted, Agent sharing would make OpenSharing the distribution layer for running agents — a significant expansion.

**On-premises rollout:** The NetApp, HPE, Nutanix, Rubrik, Cohesity, Commvault, and VAST Data integrations are committed for end of 2026. When these ship, OpenSharing becomes viable for regulated industries that cannot put primary data in cloud object storage.

**DAIS 2026 Day 2–3 sessions (June 17–18):** The OpenSharing announcement is likely woven into DAIS keynote content given Matei Zaharia's role as co-founder and primary voice on the OpenSharing announcement. Watch the Databricks blog for any additional technical specifications or customer examples from the summit.

