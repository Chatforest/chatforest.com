# Databricks OpenSharing: The Open Protocol for Sharing Agent Skills, Models, and Data

> Databricks donated OpenSharing to the Linux Foundation on June 10, 2026 — an open protocol that extends Delta Sharing to cover agent skills, ML models, and unstructured volumes in addition to tables. Launch supporters include OpenAI, Stripe, and SAP. Here's the technical architecture and builder decision tree.


Databricks [announced **OpenSharing**](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing) on June 10, 2026 — five days before the [Databricks Data + AI Summit (DAIS 2026)](https://www.moscone.com/events/databricks-data-ai-summit-2026), which ran June 15-18, 2026 at Moscone Center in San Francisco. The timing looks deliberate: seed press coverage before the keynotes, then validate the architecture with enterprise customer examples at the summit.

OpenSharing is the successor to [Delta Sharing](https://www.prnewswire.com/news-releases/databricks-unveils-delta-sharing-the-worlds-first-open-protocol-for-real-time-secure-data-sharing-and-collaboration-between-organizations-301299496.html), which Databricks launched on May 26, 2021, calling it "the world's first open protocol" for sharing structured tabular data across platforms, and donated to the Linux Foundation as part of the open-source Delta Lake project. The extension is large: where Delta Sharing handled tables only, OpenSharing adds agent skills, ML models, and file volumes — covering the full AI asset stack that organizations now need to distribute securely across teams and partner organizations.

The protocol is [Apache 2.0 licensed](https://github.com/OpenSharing-IO/OpenSharing/blob/main/LICENSE), submitted as a sandbox project under the [Linux Foundation AI & Data Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-opensharing-project-to-standardize-ai-asset-and-data-exchange), and backward-compatible with all existing Delta Sharing clients. It is not a Databricks product — any server or client that implements the spec is a valid participant.

---

## What Delta Sharing Was, and Why the Extension Was Necessary

[Delta Sharing launched in 2021](https://www.prnewswire.com/news-releases/databricks-unveils-delta-sharing-the-worlds-first-open-protocol-for-real-time-secure-data-sharing-and-collaboration-between-organizations-301299496.html) as an open standard for sharing live data across platforms without copying it. The design was straightforward: a sharing server manages access grants, then vends short-lived cloud credentials that let recipients read data directly from the provider's cloud storage. No data movement, no intermediate copies, no single-vendor lock-in.

The protocol caught on. [Delta Sharing clients exist](https://github.com/delta-io/delta-sharing) for Apache Spark, pandas, Tableau, Power BI, Clojure, Node.js, Java, Rust, Go, C++, and R. By mid-2024, Databricks [reported](https://www.databricks.com/blog/whats-new-data-sharing-and-collaboration) more than 16,000 data recipients had adopted Delta Sharing, and a separate Databricks post lists [hundreds of partners](https://www.databricks.com/blog/becoming-most-comprehensive-data-ai-ecosystem-earth) — including Adobe, Atlassian, LSEG, Stripe, The Trade Desk, and Walmart — using it to deliver data to their customers.

The problem that motivated OpenSharing: tables are only one type of asset organizations now need to share. As AI development matured, teams faced identical friction with:

- **Agent skills** — reusable packaged agent capabilities (tools, instructions, scripts) that an AI agent loads into its context. No standard for distributing them across teams or organizations.
- **ML model artifacts** — trained weights, config files, run provenance. Distributed via custom integrations or single-vendor registries.
- **Unstructured files** — documents, embeddings, evaluation datasets, media. Delta Sharing had no type for them.

OpenSharing adds these three types without breaking existing consumers. Every existing Delta Sharing client continues working. The new asset types each follow the same zero-copy credential-vending pattern the ecosystem already knows.

---

## Protocol Architecture

### Sharing Hierarchy

The technical details in this section (hierarchy, authentication, credential vending, and API endpoints) come from the [OpenSharing protocol specification](https://github.com/OpenSharing-IO/OpenSharing) — specifically the [SHARES](https://github.com/OpenSharing-IO/OpenSharing/blob/main/spec/protocols/SHARES.md), [SCHEMAS](https://github.com/OpenSharing-IO/OpenSharing/blob/main/spec/protocols/SCHEMAS.md), [CREDENTIALS](https://github.com/OpenSharing-IO/OpenSharing/blob/main/spec/protocols/CREDENTIALS.md), [VOLUMES](https://github.com/OpenSharing-IO/OpenSharing/blob/main/spec/protocols/VOLUMES.md), [ML_MODELS](https://github.com/OpenSharing-IO/OpenSharing/blob/main/spec/protocols/ML_MODELS.md), and [AGENT_SKILLS](https://github.com/OpenSharing-IO/OpenSharing/blob/main/spec/protocols/AGENT_SKILLS.md) protocol files.

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

The Iceberg compatibility is significant: when a provider stores Delta tables with [Universal Format (UniForm) enabled](https://www.databricks.com/blog/delta-lake-universal-format-uniform-iceberg-compatibility-now-ga), Iceberg-native tools — Databricks names [Snowflake, Trino, and Flink](https://www.databricks.com/blog/announcing-first-class-support-iceberg-format-databricks-delta-sharing) as examples — can consume the same shared data via their native Iceberg clients. The [OpenSharing TABLES spec](https://github.com/OpenSharing-IO/OpenSharing/blob/main/spec/protocols/TABLES.md) implements the Iceberg REST catalog API, expanding the consumer universe without changing provider storage.

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

This is the most architecturally significant new type. An AgentSkill is a **reusable AI capability packaged as a directory of files**, following the [AgentSkills specification](https://github.com/agentskills/agentskills) — an open format [originally developed by Anthropic](https://agentskills.io) and released as an open standard.

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

**Progressive disclosure model:** Per the [Agent Skills specification](https://agentskills.io), agents load skills in three stages — discovery (scan `name` + `description` metadata), activation (read the full `SKILL.md` once a task matches), and execution (load scripts/referenced files only as needed). This keeps discovery cheap — an agent can page through many skills without loading large context payloads.

**Existing compatibility:** The AgentSkills format (the underlying file structure) is already supported by a [large and growing list of agent tools](https://agentskills.io), including Claude Code, Claude, Cursor, GitHub Copilot, Goose, Gemini CLI, and OpenAI Codex. OpenSharing adds the **distribution and access-control layer** — skills can now be published, versioned, discovered, and access-controlled the same way tables have been for five years.

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

**[On-premises storage partners](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing) (generally available now):** Everpure, MinIO (native in AIStor), Qumulo.

**On-premises storage partners (committed by end of 2026):** Cohesity, Commvault, HPE, NetApp, Nutanix, Rubrik, VAST Data.

---

## Founding Members

A double-digit list of organizations backed OpenSharing at announcement, per quotes in the [Databricks](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing) and [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-opensharing-project-to-standardize-ai-asset-and-data-exchange) press releases:

**AI ecosystem:** OpenAI, Databricks

**Enterprise data consumers:** SAP ("We chose OpenSharing for SAP Business Data Cloud"), Stripe (Stripe Data Pipeline), LSEG (London Stock Exchange Group — cites its "LSEG Everywhere" strategy), Atlassian (Atlassian Analytics data shares), Amadeus, Acxiom (Acxiom Real ID)

**Domain-specific:** Cotality (property and location intelligence), Kythera Labs (healthcare data)

**Infrastructure:** MinIO (native in its AIStor on-premises object storage)

Separately, a Databricks ecosystem post lists [The Trade Desk](https://www.databricks.com/blog/becoming-most-comprehensive-data-ai-ecosystem-earth) among "launch partners" for OpenSharing-connected apps — a related but distinct list from the protocol-launch quotes above.

The OpenAI participation is notable: it puts the two companies most associated with the AgentSkills format — Anthropic (which created the underlying spec) and OpenAI (an OpenSharing launch supporter) — on a common distribution layer.

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

The AgentSkills SKILL.md format was [originally developed by Anthropic](https://agentskills.io) as an open standard for packaging reusable agent capabilities. OpenSharing adopts it as the `AgentSkill` asset type — adding versioning, access control, discovery, and credential-vended delivery on top of the raw format.

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

A team that stores data in Delta Lake with Uniform format enabled can now share that data with Iceberg-native consumers (Flink, Trino, Snowflake Iceberg tables) via OpenSharing's Iceberg-compatible endpoint — without changing their storage format or running a separate Iceberg catalog.

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

**Rest of DAIS 2026 (June 15–18):** The OpenSharing announcement is likely woven into DAIS keynote content — [Matei Zaharia](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing), Databricks co-founder and CTO, supplied the lead quote in the OpenSharing launch press release ("Delta Sharing proved the industry would choose open over locked-in. OpenSharing extends that principle to the full AI stack..."). Watch the Databricks blog for any additional technical specifications or customer examples from the summit.

