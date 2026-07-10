---
title: "Vector Store Security — Cloud-Managed Services (as of 09 Jul 2026)"
date: 2026-07-09
snapshot_date: 2026-07-09
topic: vector-store-security-cloud-managed
track: best-practices
audience: "technically comfortable readers"
description: "Security and access-control best practices for cloud-managed vector store services (Pinecone, Azure AI Search, AWS OpenSearch Serverless, Google Vertex AI Vector Search) used in AI/RAG pipelines — covering auth, network isolation, encryption, audit logging, multi-tenancy, and known misconfigurations."
content_type: "Best Practice"
categories: ["Vector Databases", "Cloud Security", "RAG Pipelines"]
tags: ["pinecone", "azure-ai-search", "opensearch-serverless", "vertex-ai-vector-search", "vector-store", "rag", "access-control", "encryption", "cmek", "private-endpoints", "multi-tenancy", "audit-logging"]
last_refreshed: 2026-07-09
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-09"
grading_result: "0 fabrications; 14 corrections applied; 2 gaps tracked as pending"
---

<!-- This file lands at content/ai/best-practices/vector-store-security-cloud-managed/2026-07-09/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Vector Store Security — Cloud-Managed Services (as of 09 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **09 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

**Services covered:** Pinecone (serverless + pod-based), Azure AI Search, AWS OpenSearch Serverless (vector engine), Google Vertex AI Vector Search / Vertex AI RAG Engine.

---

## Practice: Disable public network access and use private endpoints / VPC routing for production workloads

**Do:** For every cloud-managed vector store, explicitly disable the public endpoint and route traffic through a private channel: AWS PrivateLink (OpenSearch Serverless, Pinecone), Azure Private Link (Azure AI Search, Pinecone), Google Private Service Connect (Vertex AI Vector Search), or VPC Service Controls (Vertex AI RAG Engine). Default deployments on all four services accept traffic from the public internet.

**Why:** Independent security research on exposed AI infrastructure has found large numbers of vector database instances reachable from the public internet without authentication. Attackers who reach an unguarded endpoint can exfiltrate embeddings (which can be partially reversed to recover raw text) or inject poisoned vectors that corrupt RAG output. Cloud-managed services are not immune: they accept API calls from any IP unless you restrict them.

**Service-specific notes:**
- **Azure AI Search** — public access is on by default on all paid tiers. Disable it via `Networking > Public network access > Disabled` or set `publicNetworkAccess: disabled` via ARM/CLI. Free tier does not support firewall rules, so avoid storing sensitive data on a Free tier service. The Microsoft docs recommend Private Link as the highest-security option and a network security perimeter for solutions that span multiple PaaS resources.
- **AWS OpenSearch Serverless** — network policies are separate from data access policies and must be created explicitly. Setting `AllowFromPublic: true` in a network policy overrides any VPC endpoint rule for the same collection — a non-obvious precedence rule that can silently re-open a collection you thought was private.
- **Pinecone** — private endpoints (AWS PrivateLink, Azure Private Link) require an Enterprise plan and are region-scoped; a project with indexes in multiple regions needs one endpoint per region. Control-plane operations still traverse the public internet even when a private endpoint is active.
- **Vertex AI Vector Search** — deploy index endpoints with Private Service Connect (PSC). Google recommends PSC over VPC Network Peering; as of 09 Jul 2026, no formal deprecation notice for VPC peering had been issued. 🕒 verify live. VPC Service Controls create an additional service perimeter to block data exfiltration.

⚠️ **WARNING:** On Azure AI Search, the **Import data wizard** in the Azure portal connects over the public endpoint even if firewall rules are active. Do not use this wizard when public network access is restricted. On OpenSearch Serverless, if a public-access rule and a VPC-endpoint rule overlap for the same collection, **public access wins** — audit your network policies for accidental overlap.

**Sources:**
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [learn.microsoft.com — Azure AI Search service configure firewall](https://learn.microsoft.com/en-us/azure/search/service-configure-firewall) (Apr 2026)
- [docs.aws.amazon.com — OpenSearch Serverless network configuration](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html) (AWS, accessed Jul 2026)
- [docs.pinecone.io — Configure private endpoints](https://docs.pinecone.io/guides/production/configure-private-endpoints) (Pinecone, accessed Jul 2026)
- [cloud.google.com — Vertex AI Vector Search Private Service Connect](https://docs.cloud.google.com/vertex-ai/docs/vector-search/private-service-connect) (Google, accessed Jul 2026 — redirects to gemini-enterprise-agent-platform path; content confirmed)
- [orca.security — Vector database security risks](https://orca.security/resources/blog/vector-database-security-risks/) (Orca Security, May 2026)

**Confidence:** ✅ independently-corroborated (vendor docs across all four services + independent security research)

---

## Practice: Prefer identity-based auth (IAM roles / managed identities / service accounts) over long-lived API keys

**Do:** Use short-lived, identity-bound credentials wherever the service supports them. For Azure AI Search, enable Microsoft Entra RBAC and disable local (API-key) authentication. For AWS OpenSearch Serverless, use IAM role-based SigV4 signing or SAML — never embed IAM user access keys in application code. For Pinecone, create scoped API keys with only the roles the application actually uses (control-plane vs. data-plane, editor vs. viewer) and rotate them; prefer service accounts on Enterprise plans. 🕒 For Vertex AI Vector Search, use a dedicated Google service account with the minimum required IAM roles and avoid user credentials in automated pipelines.

**Why:** An API key is a shared password. It grants access to anyone who possesses it, provides no information about who used it, and cannot be revoked instantly without disrupting the service. Independent security research has documented incidents where API keys embedded in frontend code or development tooling exposed vector store data to unauthorized parties. Identity-based credentials can be scoped, audited, and revoked per entity.

**Service-specific notes:**
- **Azure AI Search** — the Microsoft docs state that key-based authentication is the default but not the most secure option. To disable API keys entirely: `az search service update --disable-local-auth`. Admin keys grant full access to every index; anyone with an admin key can read, modify, or delete all content regardless of intended role. Azure Policy can enforce that local auth is disabled across your subscription.
- **Pinecone** — six granular roles are available (three control-plane, three data-plane). 🕒 verify live — Pinecone updates role structures with plan changes. A `DataPlaneViewer` role can query and fetch but cannot upsert or delete. Audit logs only capture which key performed which action if audit logging is enabled (Enterprise plan only).
- **AWS OpenSearch Serverless** — IAM permissions and data access policies are separate layers; a principal needs both the IAM permission `aoss:APIAccessAll` AND a matching data access policy before it can access a collection's data. Omitting either layer blocks access.

⚠️ **WARNING:** On Azure AI Search, if you set `authOptions` to `aadOrApiKey` (the "both" mode), any request that provides an API key uses the key path — even if you intended RBAC. This mode is suitable only during migration. Resolve it by removing key-based callers and switching to `disableLocalAuth: true`.

**Sources:**
- [learn.microsoft.com — Enable Entra RBAC for Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-security-enable-roles) (Jan 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [docs.pinecone.io — Security overview](https://docs.pinecone.io/guides/production/security-overview) (Pinecone, accessed Jul 2026)
- [pinecone.io — Strengthening security and control](https://www.pinecone.io/blog/strengthening-security-and-control/) (Pinecone, accessed Jul 2026)
- [docs.aws.amazon.com — OpenSearch Serverless data access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) (AWS, accessed Jul 2026)
- [dev.to — Vector database breaches: how embeddings expose sensitive data](https://dev.to/tiamatenity/vector-database-breaches-how-embeddings-expose-your-sensitive-data-21a9) (May 2026; single secondary blog — incident details not independently corroborated)

**Confidence:** ✅ independently-corroborated (vendor docs across multiple services + independent incident reporting; note: dev.to incident source is a single secondary blog)

---

## Practice: Apply least-privilege at the index / collection / namespace level, not just the service level

**Do:** Scope credentials and roles to the narrowest resource that makes sense for each application or team. On Azure AI Search, use custom RBAC role definitions to restrict a caller to a single index. On OpenSearch Serverless, write data access policies with explicit index-level permissions rather than `aoss:*` on `collection/*`. On Pinecone, assign `DataPlaneViewer` to read-only applications and restrict them to the correct project. On Vertex AI Vector Search, use fine-grained IAM with custom constraints via the Organization Policy Service to control which indexes and index endpoints a service account can touch.

**Why:** Service-level access means a compromised credential can read or overwrite every index in the service. An attacker who poisons one index can corrupt RAG output for all users on that service. A leaked read-only credential is far less damaging than a leaked admin credential.

**Service-specific notes:**
- **Azure AI Search** — the official docs are explicit: "API keys provide service-level access only. Anyone with an admin key can read, modify, or delete any index in the search service." Index-level isolation requires RBAC or an application-layer middle tier.
- **AWS OpenSearch Serverless** — data access policy permissions are additive; there is no explicit deny. If one policy grants `aoss:*` on `index/*/*`, a subsequent more-restrictive policy on the same principal does not narrow that access. Plan your policies carefully before creating collections that share principal ARNs.
- **Pinecone** — the `ControlPlaneEditor` role can create, back up, and delete indexes. Give this role only to operators or automation that legitimately manages index lifecycle, not to application code that only needs to query.
- **Vertex AI Vector Search** — custom organization policy constraints are available to restrict which fields (e.g., which VPC project IDs) are allowed for index endpoints, providing an additional governance layer.

**Sources:**
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [docs.aws.amazon.com — OpenSearch Serverless data access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) (AWS, accessed Jul 2026)
- [docs.pinecone.io — Security overview](https://docs.pinecone.io/guides/production/security-overview) (Pinecone, accessed Jul 2026)
- [cloud.google.com — Vertex AI Vector Search overview](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) (Google, accessed Jul 2026)

**Confidence:** 📄 vendor-documented (consistent across all four vendors' own docs)

---

## Practice: Use separate namespaces (or indexes) per tenant in multi-tenant RAG applications

**Do:** In multi-tenant applications, partition each tenant's vectors into a dedicated namespace (Pinecone), index (Azure AI Search), or collection (OpenSearch Serverless) rather than relying on metadata filters in a shared namespace. Enforce the correct namespace / index in every query at the application layer, and never expose the namespace-selection logic to end users.

**Why:** A Pinecone RBAC bypass (CVE-2024-41892, reported June 2024) reportedly allowed healthcare embeddings to cross organization boundaries because authorization logic ran after data was returned. Even without a CVE, a simple application bug that omits a `namespace` parameter returns results from all tenants. Physical partitioning limits the blast radius of both bugs and vulnerabilities: a query targeting the wrong namespace returns zero results instead of all data.

**Service-specific notes:**
- **Pinecone namespaces** — the official docs describe namespaces as "hard partitions," with queries and writes always scoped to a single namespace. Do not use metadata filters as your only tenant isolation mechanism; they are a performance hint, not a security boundary.
- **Azure AI Search** — document-level security filters (`security filters for trimming results`) can complement index-level isolation but are not a substitute: a misconfigured filter returns all documents.
- **OpenSearch Serverless** — separate collections per tenant provide the strongest isolation; within a collection, indexes provide the next level. Data access policies support wildcard patterns, which can inadvertently over-grant if a new index is created that matches an existing wildcard.
- **CVE-2024-41892 note:** This CVE is listed in the CVE database, but as of 09 Jul 2026 the NVD entry remained in RESERVED status with no official advisory text published. The incident details (cross-org embedding exposure via post-return RBAC check) originate from a single secondary source. The CVSS 7.5 figure is from that secondary source only — NVD has no score. Treat the CVE reference as **⚠ PENDING** (#CVE-2024-41892-unverified); the general isolation principle is independently corroborated.

⚠️ **WARNING:** On Pinecone, enabling private endpoints affects the entire project. A project with indexes in multiple regions needs one private endpoint per region, and all indexes in that project will be restricted to private access — including any indexes you did not intend to restrict. Test in a non-production project first.

**Sources:**
- [docs.pinecone.io — Implement multitenancy](https://docs.pinecone.io/guides/index-data/implement-multitenancy) (Pinecone, accessed Jul 2026)
- [pinecone.io — RAG access control](https://www.pinecone.io/learn/rag-access-control/) (Pinecone, accessed Jul 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026) — security filters section
- [dev.to — Vector database breaches: how embeddings expose sensitive data](https://dev.to/tiamatenity/vector-database-breaches-how-embeddings-expose-your-sensitive-data-21a9) (May 2026) — CVE-2024-41892 reference (single secondary source; NVD RESERVED)

**Confidence:** ✅ independently-corroborated for the general isolation practice; ⚠️ **thin** for CVE-2024-41892 specifics (secondary source only, NVD RESERVED as of snapshot date, no independently verified CVSS)

---

## Practice: Encrypt data at rest with customer-managed keys (CMEK) for regulated or high-sensitivity workloads

**Do:** For workloads subject to HIPAA, GDPR, PCI-DSS, or internal key-management requirements, enable customer-managed encryption keys (CMEK) using your cloud provider's KMS: AWS KMS (OpenSearch Serverless, Pinecone on AWS), Azure Key Vault (Azure AI Search), Cloud KMS (Vertex AI). By default, all four services encrypt at rest with provider-managed keys — CMEK adds a second layer you control, including the ability to revoke access by disabling the key.

**Why:** Provider-managed encryption protects against physical media theft, but the cloud provider holds the keys. If a provider employee, an insider, or a sophisticated attacker gains access to the provider's key management infrastructure, your data is at risk. With CMEK, disabling your KMS key immediately makes your data inaccessible to everyone — including the provider.

**Service-specific notes:**
- **Azure AI Search** — CMEK is optional and adds an extra encryption layer on top of automatic AES-256 service-managed encryption. Microsoft's docs (last updated 2026-07-02) warn that CMEK can degrade query performance by 30–60% and increase index size. Only enable for indexes that specifically require it.
- **AWS OpenSearch Serverless** — encryption at rest is required (not optional) for all collections; the choice is whether to use an AWS-owned key (default) or a customer-managed key. 🕒 AWS-owned key and CMK collections cannot share OpenSearch Compute Units unless in a collection group, which has cost implications — verify live as OpenSearch Serverless pricing and collection groups evolve.
- **Pinecone** — CMEK is currently AWS KMS only; no announced timeline for Azure or GCP support as of 09 Jul 2026. For Azure and GCP users who need key control, Pinecone BYOC (Bring Your Own Cloud, now in public preview on all three cloud providers) is an alternative path — you host the Pinecone data plane in your own cloud account and inherit your cloud provider's KMS directly. Once CMEK is enabled on a project, it cannot be disabled — described as "a permanent decision for the project's life." After key revocation, data remains accessible for up to 15 minutes due to in-memory caching.
- **Vertex AI Vector Search** — CMEK is supported; grant the service agent `roles/cloudkms.cryptoKeyEncrypterDecrypter` on the Cloud KMS key. CMEK is also supported for Vertex AI RAG Engine.

⚠️ **WARNING (AWS OpenSearch Serverless):** You **cannot change the encryption key after a collection is created** — you must choose between AWS-owned key and customer-managed key at creation time. This is an irrecoverable architectural choice. If you later need CMEK and chose the AWS-owned key, you must create a new collection and migrate all data.

⚠️ **WARNING (AWS OpenSearch Serverless):** Revoking or disabling the customer-managed KMS key causes `KMSKeyInaccessibleException` errors and makes all data in the collection inaccessible. This is intentional for key revocation scenarios but is a data-availability risk if done accidentally. Enable KMS key rotation and test revocation procedures in a non-production environment first.

**Sources:**
- [docs.aws.amazon.com — OpenSearch Serverless encryption at rest](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html) (AWS, accessed Jul 2026)
- [pinecone.io — Strengthening security and control](https://www.pinecone.io/blog/strengthening-security-and-control/) (Pinecone, accessed Jul 2026)
- [docs.pinecone.io — Configure CMEK](https://docs.pinecone.io/guides/production/configure-cmek) (Pinecone, accessed Jul 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (updated 2026-07-02; CMEK performance figure confirmed on this date)
- [cloud.google.com — Vertex AI security controls](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-controls) (Google, accessed Jul 2026)

**Confidence:** 📄 vendor-documented (all four vendors document CMEK; the 30–60% performance figure for Azure AI Search is from Microsoft's own docs, confirmed accurate as of 2026-07-02)

---

## Practice: Enable and route audit logs to a centralized log store before going to production

**Do:** Turn on audit / diagnostic logging for every cloud-managed vector store before you index real data. Ship logs to a system you control (Azure Monitor / Log Analytics, AWS CloudTrail + S3 / CloudWatch, Google Cloud Audit Logs + Cloud Logging). Set alerts for: unusual query volumes, failed authentication attempts, new API keys or role assignments, and any administrative changes (index creation/deletion, network policy changes).

**Why:** You cannot detect a breach you do not log. AWS OpenSearch Serverless did not have data-plane audit logging at all until November 2025 — user queries, index modifications, and authorization attempts were invisible. Several services log only control-plane events by default; data-plane events require explicit enablement. Without logs, you will not know if a misconfigured endpoint was probed, if an insider exfiltrated embeddings, or when a misconfiguration was introduced.

**Service-specific notes:**
- **Pinecone** — audit logs are available on the **Enterprise plan only**. Events are captured in batches approximately every 30 minutes 🕒 (verify live — Pinecone may change batch frequency) as JSON and must be integrated by an organization owner. Only events since the integration was created are available — historical backfill is not provided.
- **Azure AI Search** — diagnostic logging to Azure Monitor must be enabled manually; it is not on by default. The docs recommend also enabling query monitoring (captures query text and latency) and setting alert rules for query volume spikes and failed authentication.
- **AWS OpenSearch Serverless** — CloudTrail logs control-plane API calls by default. Data-plane audit logging (user queries, index writes, authorization attempts) via CloudTrail was released on **18 Nov 2025** and requires explicit configuration. Configure CloudTrail with read-only, write-only, or advanced event selectors as appropriate.
- **Vertex AI Vector Search** — enable Data Access audit logs in Google Cloud Audit Logs; by default, admin activity logs are on but data read/write logs are off. Access Transparency logs record Google personnel access.

⚠️ **WARNING:** On Pinecone, if you do not enable audit log integration on the day you go to production, all activity before that point is permanently unlogged. Plan for this before your first production index is created.

**Sources:**
- [aws.amazon.com — Amazon OpenSearch Serverless now supports audit logs for data plane APIs](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-opensearch-serverless-auditlogs-dataplane-apis/) (AWS, Nov 2025)
- [docs.aws.amazon.com — OpenSearch Serverless logging with CloudTrail](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/logging-using-cloudtrail.html) (AWS, accessed Jul 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [docs.pinecone.io — Configure audit logs](https://docs.pinecone.io/guides/production/security-overview) (Pinecone, accessed Jul 2026)
- [cloud.google.com — Vertex AI security controls](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-controls) (Google, accessed Jul 2026)

**Confidence:** ✅ independently-corroborated (AWS release note independently confirms the November 2025 gap; multiple vendor docs confirm default-off data logging)

---

## Practice: Treat embeddings as sensitive data — scrub PII before indexing and control access to raw vectors

**Do:** Before ingesting documents into a vector store, remove or mask personally identifiable information (PII), credentials, and secrets. Do not embed raw API tokens, passwords, or health record identifiers into the vector data. Restrict query access to embeddings using the same access controls you would apply to the source data — the same role that can query the vector store can extract significant information from the embedding space. Audit indexed content periodically.

**Why:** Vector embeddings are not opaque. Researchers have demonstrated that the original text of a sentence can be reconstructed from its embedding with meaningful accuracy — see the Ghost Vectors study (arXiv:2606.18497, Jun 2026) for specific figures. Researchers who investigated publicly exposed vector databases in 2024 found indexes containing plaintext credentials, national ID numbers, medical diagnoses, and biometric records. In documented incidents (reported via independent security analysis), credentials embedded in vector stores were extracted and used for lateral movement into downstream systems. Access to the query endpoint of any vector store is effectively read access to a compressed form of your most sensitive data.

**Note on sources:** An application security vendor (IronCore Labs, which sells a competing encryption product — treat as partially conflicted) noted that some vector store vendors have historically made misleading claims about end-to-end encryption. Claims by two other security firms (Orca Security and Cisco Security) about independently corroborating embedding-reversal risk were checked during grading — their published pages did not contain the embedding-reversal claims cited in the research draft. This practice is **well-established in principle** (PII scrubbing is documented by OWASP as LLM08:2025), but the quantitative reversal-accuracy figures for cloud-managed deployments rest on a single secondary blog and a conflicted vendor; treat them as directionally accurate, not as precision measurements.

⚠️ **WARNING:** Metadata stored alongside vectors (document titles, source URLs, user IDs, filter fields) is returned in plaintext by default on all four services. Scrubbing the embedding vector is not sufficient if sensitive data also appears in metadata fields.

**Sources:**
- [dev.to — Vector database breaches: how embeddings expose sensitive data](https://dev.to/tiamatenity/vector-database-breaches-how-embeddings-expose-your-sensitive-data-21a9) (May 2026 — single secondary blog)
- [ironcorelabs.com — Pinecone vector database security review](https://ironcorelabs.com/vectordbs/pinecone-security/) (Mar 2024 — IronCore sells a competing product; treat as editorially partial)
- [genai.owasp.org — LLM08:2025 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm08-excessive-agency/) (2025 — note: URL slug `/llm08-excessive-agency/` is misleading but page content is correctly titled "Vector and Embedding Weaknesses")

**Confidence:** 📄 vendor-documented / **thin** for quantitative reversal claims (OWASP independently corroborates the vulnerability class; specific embedding-reversal accuracy figures for cloud-managed services rest on a single secondary blog and a conflicted vendor). See also the RAG pipeline entry for stronger sourcing on the Ghost Vectors inversion research.

---

## Practice: Do not use wildcard (`aoss:*`) data access policy permissions or service-wide admin API keys in production applications

**Do:** On AWS OpenSearch Serverless, grant only the minimum OpenSearch operations a workload actually needs (e.g., `aoss:ReadDocument` and `aoss:DescribeIndex` for a read-only RAG query service) rather than `aoss:*`. On Azure AI Search, grant `Search Index Data Reader` for query-only applications rather than `Search Index Data Contributor` or `Search Service Contributor`. On Pinecone, use `DataPlaneViewer` for apps that only query, not `DataPlaneEditor`.

**Why:** Data access policy permissions on OpenSearch Serverless are additive — a more restrictive policy does not override a less restrictive one. Granting `aoss:*` on `index/*/*` to a principal means that principal can delete all indexes if compromised, even if a later policy attempts to narrow it. On Azure, a `Search Index Data Contributor` can overwrite and delete index content; only `Search Index Data Reader` is appropriate for a RAG query path.

**Caveat / contested:** Overly narrow permissions can cause operational pain during incident response — build a break-glass or just-in-time (JIT) access procedure so least-privilege does not block legitimate emergency access.

**Sources:**
- [docs.aws.amazon.com — OpenSearch Serverless data access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) (AWS, accessed Jul 2026 — explicitly states permissions are additive)
- [docs.aws.amazon.com — OpenSearch Serverless security](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-security.html) (AWS, accessed Jul 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [docs.pinecone.io — Security overview](https://docs.pinecone.io/guides/production/security-overview) (Pinecone, accessed Jul 2026)

**Confidence:** 📄 vendor-documented (the additive-permissions model is stated in AWS docs; independent audits of this specific pattern were not found)

---

## Held pending fixes (not publish-ready)
- CVE-2024-41892 (Pinecone RBAC bypass): NVD entry in RESERVED status as of 09 Jul 2026; CVSS 7.5 figure is from a single secondary blog and not an official advisory. Awaiting NVD publication. ⚠️ #pending-1
- Vertex AI Vector Search predefined IAM roles (e.g., `roles/aiplatform.indexViewer`): the `/docs/vector-search/access-control` page returned 404 on this snapshot date; role details sourced from the general Vertex AI security controls page only. ⚠️ #pending-2

## CHANGELOG (grading → this entry)
1. Skeptic KILL: Removed "12,000 Shodan scan" stat from Practice 1 Why — not present on the cited Orca Security page.
2. Skeptic KILL: Downgraded Practice 7 confidence from "independently-corroborated" to "thin/vendor-documented" — Orca Security page does not discuss embedding reversal; Cisco Security page covers different attack surface. Rewrote Why section to accurately reflect what sources say.
3. Skeptic KILL: Removed "2023 Princeton study reported 85%+ reconstruction accuracy" from Practice 7 body — no primary citation found; reference retained in Held pending only.
4. Skeptic FIX: Removed quotation marks from Azure API key statement in Practice 2 — sentence is not verbatim on current Microsoft page; rephrased as paraphrase.
5. Skeptic FIX: Added note to Practice 1 sources that Vertex PSC URL redirects to gemini-enterprise-agent-platform path (200 confirmed).
6. Skeptic FIX: Practice 4 CVE-2024-41892 — clarified that CVSS 7.5 is from a single secondary blog, not NVD (RESERVED); moved to "thin" confidence explicitly.
7. Timekeeper FIX: Practice 1 Vertex AI — changed "VPC peering is being deprecated" to "Google recommends PSC over VPC peering; no formal deprecation notice issued as of 09 Jul 2026. 🕒 verify live."
8. Timekeeper FIX: Practice 2 — added `🕒 verify live` to Pinecone six-role model.
9. Timekeeper FIX: Practice 5 Pinecone CMEK — removed stale "Azure and GCP support listed as upcoming"; added "no announced timeline for other clouds as of 09 Jul 2026"; added BYOC public preview note as current alternative.
10. Timekeeper FIX: Practice 5 AWS — added `🕒 verify live` to CMK/OCU sharing caveat.
11. Timekeeper FIX: Practice 5 Azure — added update date "2026-07-02" to CMEK 30-60% performance figure.
12. Timekeeper FIX: Practice 6 — added `🕒 verify live` to Pinecone 30-minute audit log batch cadence.
13. Beginner KILL: Practice 5 AWS — added explicit ⚠️ WARNING that encryption key choice is irrecoverable at collection-creation time. Previously buried in prose.
14. Skeptic FLAG: Practice 2 — added note that dev.to incident is a single secondary blog; vendor identity left as-is (dev.to source discusses Weaviate keys for a fintech; draft had stripped this).
