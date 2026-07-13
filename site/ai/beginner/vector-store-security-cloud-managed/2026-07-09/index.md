# Vector Store Security — Cloud-Managed Services (as of 09 Jul 2026)

> Security and access-control best practices for cloud-managed vector stores (Pinecone, Azure AI Search, AWS OpenSearch Serverless, Google Vertex AI) explained for people new to AI — covering dangerous defaults, authentication, encryption, and audit logging in plain language.


<!-- This file lands at content/ai/beginner/vector-store-security-cloud-managed/2026-07-09/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Vector Store Security — Cloud-Managed Services (as of 09 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **09 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.
> Re-leveled for beginner readers by rings-beginner-author; facts unchanged from the technical entry.

## What is a vector store?

A vector store (also called a vector database) is a special kind of database used in AI applications. When you feed text into an AI — documents, emails, help articles — the AI turns each piece of text into a list of numbers called an **embedding** (or **vector**). The vector store saves these numbers so the AI can quickly find the most relevant chunks when a user asks a question. This is the foundation of a pattern called **RAG (Retrieval-Augmented Generation)**: retrieve relevant chunks from the vector store, then generate an answer.

This guide covers four popular cloud-managed vector store services: **Pinecone**, **Azure AI Search**, **AWS OpenSearch Serverless**, and **Google Vertex AI Vector Search**. "Cloud-managed" means the database runs on someone else's servers — you configure it through a web dashboard or API, not by installing software yourself.

## How to read the labels

- ✅ **independently-corroborated** — 2+ independent publishers confirmed this
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break things, or expose your data
- 🕒 **verify live** — this detail changes often; check the current value before acting

---

## Practice 1: Block public internet access and route traffic through a private network connection

**Do:** Every cloud-managed vector store accepts traffic from the public internet by default. Before going to production, explicitly turn off that public access and route traffic through a private channel instead. The private channel options are:

- **AWS OpenSearch Serverless** — create a VPC endpoint (AWS PrivateLink)
- **Azure AI Search** — enable Azure Private Link
- **Pinecone** — configure a private endpoint (AWS PrivateLink or Azure Private Link; requires Enterprise plan)
- **Google Vertex AI Vector Search** — use Private Service Connect (PSC); also consider VPC Service Controls

**Plain-language glossary for this practice:**
- **VPC (Virtual Private Cloud):** A private section of a cloud provider's network that is invisible to the public internet. Only machines you put inside it can talk to each other by default.
- **Private endpoint / PrivateLink / Private Service Connect:** A connection that lets machines inside your VPC talk to a cloud service (like a vector store) without that traffic ever leaving the private network or touching the public internet.
- **VPC Service Controls:** An extra Google Cloud security boundary that prevents data from being copied out, even by authorized users.

**Where to actually make this change:**

- **Azure AI Search** — In the Azure portal, open your search service, go to **Settings > Networking > Public network access**, and set it to **Disabled**. Or run this command in the Azure CLI (the `az` command-line tool): `az search service update --name <your-service-name> --resource-group <your-resource-group> --public-network-access disabled`
- **AWS OpenSearch Serverless** — In the AWS Console, open OpenSearch Serverless, choose **Network policies**, and create a new policy that routes your collection through a VPC endpoint. Do not leave `AllowFromPublic: true` — see the warning below.
- **Pinecone** — In the Pinecone console under your project settings, follow the "Configure private endpoints" guide (link in sources). You must be on an Enterprise plan.
- **Vertex AI Vector Search** — When creating or updating an index endpoint, choose the Private Service Connect option. Follow the PSC guide linked in sources. 🕒 verify live — Google may update this path.

**Why this matters for beginners:** Security researchers who study AI infrastructure have found large numbers of vector database instances reachable from the public internet with no password. Attackers who reach an unguarded endpoint can steal your embeddings (which can be partially reversed to recover the original text) or inject corrupted data that poisons your AI's answers. Cloud-managed services are not protected just because they are "in the cloud" — they accept API calls from any computer on the internet unless you restrict them.

**Additional notes:**
- **Azure AI Search Free tier** does not support firewall rules — do not store sensitive data on a Free tier service.
- **Pinecone private endpoints** require one endpoint per region. A project with indexes in multiple regions needs one endpoint per region. Control-plane operations (creating or deleting indexes) still use the public internet even when a private endpoint is active.
- **Vertex AI Vector Search** — Google recommends Private Service Connect over the older VPC Network Peering option. As of 09 Jul 2026, no formal deprecation notice for VPC peering had been issued. 🕒 verify live.

⚠️ **WARNING (Azure AI Search):** The **Import data wizard** in the Azure portal connects over the public endpoint even if you have turned off public access. Do not use this wizard if you have restricted public network access — it will connect anyway and bypass your firewall rules.

⚠️ **WARNING (AWS OpenSearch Serverless):** If a public-access rule and a VPC-endpoint rule both apply to the same collection, **public access wins**. This is a non-obvious rule that can silently re-open a collection you thought was private. After creating your network policy, audit your settings to make sure there is no accidental public-access rule overlapping your collection.

**Sources:**
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [learn.microsoft.com — Azure AI Search service configure firewall](https://learn.microsoft.com/en-us/azure/search/service-configure-firewall) (Apr 2026)
- [docs.aws.amazon.com — OpenSearch Serverless network configuration](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html) (AWS, accessed Jul 2026)
- [docs.pinecone.io — Configure private endpoints](https://docs.pinecone.io/guides/production/configure-private-endpoints) (Pinecone, accessed Jul 2026)
- [cloud.google.com — Vertex AI Vector Search Private Service Connect](https://docs.cloud.google.com/vertex-ai/docs/vector-search/private-service-connect) (Google, accessed Jul 2026 — redirects to gemini-enterprise-agent-platform path; content confirmed)
- [orca.security — Vector database security risks](https://orca.security/resources/blog/vector-database-security-risks/) (Orca Security, May 2026)

**Confidence:** ✅ independently-corroborated (vendor docs across all four services + independent security research)

---

## Practice 2: Use identity-based logins instead of long-lived shared API keys

**Do:** Use short-lived, identity-bound credentials wherever the service supports them, instead of copying and pasting API keys into your application code.

- **Azure AI Search** — Enable Microsoft Entra RBAC (see glossary below) and turn off local (API-key) authentication. Command: `az search service update --name <your-service-name> --resource-group <your-resource-group> --disable-local-auth`
  - **Prerequisite:** You need the Azure CLI installed and logged in (`az login`) and pointing at the right subscription (`az account set --subscription <your-subscription-id>`). If you get `az: command not found`, install the Azure CLI first.
- **AWS OpenSearch Serverless** — Use IAM role-based access with SigV4 signing (see glossary) or SAML. Never paste IAM user access keys directly into application code.
- **Pinecone** — Create scoped API keys that only have the roles the application actually needs (see role names below). Rotate keys periodically. On Enterprise plans, use service accounts instead.
- **Vertex AI Vector Search** — Use a dedicated Google service account with the minimum required IAM roles. Do not use personal user credentials in automated pipelines.

**Plain-language glossary for this practice:**
- **API key:** A shared password string (often starting with something like `sk-...`) that grants access to whoever holds it. Anyone with the key can act as you.
- **IAM (Identity and Access Management):** The system cloud providers use to decide who can do what. Instead of a shared password, IAM ties access to a specific identity (a person, a server, or an application) that can be revoked individually.
- **Entra RBAC:** Azure's identity-based permission system. "Entra" is Microsoft's identity platform (formerly called Azure Active Directory). "RBAC" means Role-Based Access Control — access is granted by role (like "reader" or "editor"), not by a shared key.
- **SigV4 signing:** The way AWS applications prove their identity in API calls. Your AWS SDK or framework typically handles this automatically when you configure an IAM role — you do not manually sign requests.
- **SAML:** A standard for letting users log in with an existing corporate identity (like your company's Google Workspace or Microsoft account) instead of a separate password.
- **Control-plane vs. data-plane:** Control-plane operations manage the database itself (create an index, delete an index, change settings). Data-plane operations work with the data inside (insert vectors, query vectors). You can — and should — give an application only data-plane access if it does not need to manage indexes.
- **Service account:** An identity that represents an application rather than a human. Cloud providers let you create service accounts, assign them limited permissions, and let your application use them to authenticate without a shared password.

**Why this matters for beginners:** An API key is a shared password. Anyone who finds it — in your code repository, in a log file, in a screenshot — can use it as if they were you. They can read your data, overwrite it, or delete it. Identity-based credentials can be scoped to one specific application, audited (you can see what they did), and revoked instantly without disrupting other services. Security researchers have documented incidents where API keys embedded in frontend code or developer tooling exposed vector store data to unauthorized parties.

**Pinecone roles (six available — 🕒 verify live, Pinecone updates these):**
- `DataPlaneViewer` — can query and fetch, cannot insert or delete
- `DataPlaneEditor` — can insert and delete vectors
- `DataPlaneAdmin` — full data-plane control
- `ControlPlaneViewer`, `ControlPlaneEditor`, `ControlPlaneAdmin` — manage indexes themselves

**Azure AI Search note:** Admin keys grant full access to every index. Anyone with an admin key can read, modify, or delete all content regardless of their intended role.

**AWS OpenSearch Serverless note:** IAM permissions and data access policies are two separate layers. A principal needs both the IAM permission `aoss:APIAccessAll` AND a matching data access policy before it can access a collection's data. Omitting either layer blocks access completely.

⚠️ **WARNING (Azure AI Search):** If you set `authOptions` to `aadOrApiKey` (the "both" mode — meaning Azure will accept either an Entra identity or an API key), any request that provides an API key uses the key path, even if you intended to use Entra RBAC. This mode is suitable only during migration while you move callers over. Once all callers use Entra, switch to `disableLocalAuth: true` to fully remove the key path.

**Sources:**
- [learn.microsoft.com — Enable Entra RBAC for Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-security-enable-roles) (Jan 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [docs.pinecone.io — Security overview](https://docs.pinecone.io/guides/production/security-overview) (Pinecone, accessed Jul 2026)
- [pinecone.io — Strengthening security and control](https://www.pinecone.io/blog/strengthening-security-and-control/) (Pinecone, accessed Jul 2026)
- [docs.aws.amazon.com — OpenSearch Serverless data access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) (AWS, accessed Jul 2026)
- [dev.to — Vector database breaches: how embeddings expose sensitive data](https://dev.to/tiamatenity/vector-database-breaches-how-embeddings-expose-your-sensitive-data-21a9) (May 2026; single secondary blog — incident details not independently corroborated)

**Confidence:** ✅ independently-corroborated (vendor docs across multiple services + independent incident reporting; note: dev.to incident source is a single secondary blog)

---

## Practice 3: Limit each application's access to only the specific index it needs

**Do:** Scope credentials and roles to the narrowest resource that makes sense. Do not give an application that only reads from one index the ability to read — or write to — every index in your service.

- **Azure AI Search** — Use custom RBAC role definitions (in the Azure portal under Access Control / IAM for your search service) to restrict a caller to a single index. Alternatively, use an application-layer middle tier that proxies queries.
- **AWS OpenSearch Serverless** — Write data access policies that name specific indexes: for example, grant `aoss:ReadDocument` and `aoss:DescribeIndex` on `index/my-collection/my-index` rather than `aoss:*` on `collection/*`. These are typed in the AWS Console under OpenSearch Serverless > Data access policies, or in a JSON policy document via the API.
- **Pinecone** — Assign `DataPlaneViewer` to applications that only query. Reserve `ControlPlaneEditor` (which can create, back up, and delete indexes) for operators or automation that legitimately manages index lifecycle.
- **Vertex AI Vector Search** — Use fine-grained IAM with custom organization policy constraints via the Organization Policy Service to control which indexes a service account can touch.

**Plain-language glossary for this practice:**
- **Least privilege:** The security principle of giving each user or application the minimum access needed to do its job, and nothing more.
- **ARN (Amazon Resource Name):** AWS's way of uniquely identifying a resource. An ARN looks like `arn:aws:aoss:us-east-1:123456789012:collection/my-collection`. In data access policies, "principal ARN" means the identity (user, role, or service) you are granting access to.
- **aoss: actions:** AWS OpenSearch Serverless uses short action codes prefixed with `aoss:` (e.g., `aoss:ReadDocument`) to describe specific operations. You list which actions a principal is allowed to perform.
- **Organization Policy Service:** A Google Cloud feature that lets administrators set rules across their entire organization — for example, "no service account may create a Vector Search endpoint outside of these approved projects."

**Why this matters for beginners:** Service-level access means a compromised credential can read or overwrite every index in the entire service. An attacker who poisons one index can corrupt AI answers for all your users. A leaked read-only credential is far less damaging than a leaked admin credential.

**Important AWS note:** Data access policy permissions on OpenSearch Serverless are additive — there is no "deny" that overrides a broader "allow." If one policy grants `aoss:*` on `index/*/*`, a later more-restrictive policy on the same principal does not narrow that access. Plan your policies carefully before you create collections.

⚠️ **WARNING:** On Azure AI Search, API keys provide service-level access only. Anyone with an admin key can read, modify, or delete any index in the search service. Index-level isolation requires RBAC or an application-layer proxy — you cannot scope an API key to a single index.

**Sources:**
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [docs.aws.amazon.com — OpenSearch Serverless data access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) (AWS, accessed Jul 2026)
- [docs.pinecone.io — Security overview](https://docs.pinecone.io/guides/production/security-overview) (Pinecone, accessed Jul 2026)
- [cloud.google.com — Vertex AI Vector Search overview](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) (Google, accessed Jul 2026)

**Confidence:** 📄 vendor-documented (consistent across all four vendors' own docs)

---

## Practice 4: Give each customer their own namespace (or index) in multi-tenant apps

**Do:** If you are building an application where multiple customers share the same AI system, do not mix all customers' data in one shared namespace and rely on filters to separate them. Instead, put each customer's vectors in their own dedicated partition:

- **Pinecone** — use a separate **namespace** for each tenant (a namespace is Pinecone's built-in hard partition)
- **Azure AI Search** — use a separate **index** for each tenant
- **AWS OpenSearch Serverless** — use separate **collections** for the strongest isolation; within a collection, separate **indexes** are the next level

Enforce the correct namespace or index in every query at the application layer — in your server-side code, not in client-side code that a user could modify.

**Plain-language glossary for this practice:**
- **Multi-tenant:** One application serves multiple customers (tenants). Each customer should see only their own data.
- **Namespace (Pinecone):** A hard partition inside a Pinecone index. Queries and writes are always scoped to one namespace — data from other namespaces is not returned.
- **Metadata filter:** A condition you add to a query like "only return results where `customer_id = 123`." This is a performance tool, not a security boundary — a bug in your code can omit the filter, returning everyone's data.
- **CVE (Common Vulnerabilities and Exposures):** A public database of known security vulnerabilities. Each entry gets a number like CVE-2024-41892. The number alone identifies the vulnerability; it does not tell you how severe it is. Severity is rated on a CVSS score (0–10, where 10 is the most severe).

**Why this matters for beginners:** A simple application bug that forgets to include a namespace or filter parameter returns results from all tenants. A published vulnerability (CVE-2024-41892, reported June 2024) reportedly allowed healthcare embeddings to cross organization boundaries in Pinecone because authorization logic ran after data was already returned. (Note: as of 09 Jul 2026, the official CVE database entry for CVE-2024-41892 remained in RESERVED status with no official advisory text published. The CVSS 7.5 severity figure comes from a single secondary source, not the official database. The general isolation principle is independently corroborated.) Physical partitioning limits the blast radius: a query targeting the wrong namespace returns zero results instead of all data.

**Do not use metadata filters as your only tenant isolation mechanism.** They are a performance hint, not a security boundary. A misconfigured filter returns all documents.

**OpenSearch Serverless note:** Data access policies support wildcard patterns. A wildcard that inadvertently matches a new index name can over-grant access. Audit your policies when you add new indexes.

**Azure AI Search note:** Document-level security filters can complement index-level isolation but are not a substitute. A misconfigured filter returns all documents.

⚠️ **WARNING (Pinecone private endpoints and multi-tenant projects):** Enabling private endpoints on a Pinecone project affects the entire project — all indexes in all regions are restricted to private access. A project with indexes in multiple regions needs one private endpoint per region. Test in a non-production project first, because all indexes in the project will be affected, including any you did not intend to restrict.

**Sources:**
- [docs.pinecone.io — Implement multitenancy](https://docs.pinecone.io/guides/index-data/implement-multitenancy) (Pinecone, accessed Jul 2026)
- [pinecone.io — RAG access control](https://www.pinecone.io/learn/rag-access-control/) (Pinecone, accessed Jul 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026) — security filters section
- [dev.to — Vector database breaches: how embeddings expose sensitive data](https://dev.to/tiamatenity/vector-database-breaches-how-embeddings-expose-your-sensitive-data-21a9) (May 2026) — CVE-2024-41892 reference (single secondary source; NVD RESERVED)

**Confidence:** ✅ independently-corroborated for the general isolation practice; ⚠️ **thin** for CVE-2024-41892 specifics (secondary source only, NVD RESERVED as of snapshot date, no independently verified CVSS)

---

## Practice 5: Use customer-managed encryption keys for sensitive or regulated workloads

**Do:** By default, all four services encrypt your data at rest using keys managed by the cloud provider. For most use cases that is fine. But if your application handles regulated data, you should enable CMEK (Customer-Managed Encryption Keys) using your cloud provider's key management service.

**Do I need this?** A simple test: if your app handles medical records, financial data, or personal data from EU residents, you likely need CMEK (or must consult legal/compliance).

- **AWS OpenSearch Serverless** — Choose "customer managed key" when creating the collection. Use AWS KMS to create the key first.
- **Azure AI Search** — Enable CMEK in service settings; use Azure Key Vault to store the key.
- **Pinecone** — Enable CMEK in project settings; currently AWS KMS only. For Azure or GCP, see the BYOC option (below).
- **Vertex AI Vector Search** — Grant the service agent `roles/cloudkms.cryptoKeyEncrypterDecrypter` on your Cloud KMS key when creating the index.

**Plain-language glossary for this practice:**
- **Encryption at rest:** Your data is scrambled (encrypted) while it is sitting on a disk. Only someone with the key can read it. All four services do this automatically.
- **Provider-managed keys:** The cloud provider holds the encryption key. Your data is protected from physical disk theft, but the provider can theoretically access it.
- **CMEK (Customer-Managed Encryption Keys):** You create the encryption key in your own key management account and tell the cloud service to use it. If you disable or delete your key, the data becomes inaccessible to everyone — including the provider.
- **KMS (Key Management Service):** The cloud provider's system for creating and storing encryption keys. AWS calls it AWS KMS; Azure calls it Azure Key Vault; Google calls it Cloud KMS.
- **AES-256:** A widely used encryption algorithm. "256" refers to the key length in bits — a longer key is harder to break. This is what Azure AI Search uses by default.
- **HIPAA, GDPR, PCI-DSS:** US health data law, EU personal-data law, and payment-card industry standard. If any apply to your app, ask your legal team whether CMEK is required.
- **BYOC (Bring Your Own Cloud):** A Pinecone option (currently in public preview on all three cloud providers as of 09 Jul 2026) where you host the Pinecone data plane in your own cloud account. This lets you inherit your cloud provider's KMS directly, which is the current alternative path for Pinecone users on Azure or GCP who need key control.
- **OpenSearch Compute Units (OCUs):** The billing unit for compute capacity in OpenSearch Serverless. AWS-owned key and customer-managed key collections cannot share OCUs unless in a collection group. 🕒 verify live — pricing details change.

**Why this matters for beginners:** Provider-managed encryption protects against physical media theft, but the cloud provider holds the keys. With CMEK, you can revoke access immediately by disabling your key — even the cloud provider cannot read your data after that. The trade-off: CMEK adds operational complexity, and on Azure AI Search it can degrade query performance by 30–60% and increase index size (per Microsoft's own docs, confirmed 2026-07-02). Only enable CMEK for indexes that specifically require it.

**Pinecone CMEK note:** Once CMEK is enabled on a project, it cannot be disabled — this is described as "a permanent decision for the project's life." After you revoke a key, data remains accessible for up to 15 minutes due to in-memory caching.

⚠️ **WARNING (AWS OpenSearch Serverless — irrecoverable choice):** You **cannot change the encryption key after a collection is created.** You must choose between an AWS-owned key (default) and a customer-managed key at the moment you create the collection. If you later need CMEK and chose the AWS-owned key, you must create a new collection and migrate all your data. There is no way to change this after the fact. Make this decision before you create the collection.

⚠️ **WARNING (AWS OpenSearch Serverless — accidental data loss):** Revoking or disabling your customer-managed KMS key causes `KMSKeyInaccessibleException` errors and makes all data in the collection inaccessible. This is the intended behavior when you want to revoke access, but it is a serious risk if done accidentally. Enable automatic KMS key rotation and test your revocation procedure in a non-production environment before relying on it in production.

**Sources:**
- [docs.aws.amazon.com — OpenSearch Serverless encryption at rest](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html) (AWS, accessed Jul 2026)
- [pinecone.io — Strengthening security and control](https://www.pinecone.io/blog/strengthening-security-and-control/) (Pinecone, accessed Jul 2026)
- [docs.pinecone.io — Configure CMEK](https://docs.pinecone.io/guides/production/configure-cmek) (Pinecone, accessed Jul 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (updated 2026-07-02; CMEK performance figure confirmed on this date)
- [cloud.google.com — Vertex AI security controls](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-controls) (Google, accessed Jul 2026)

**Confidence:** 📄 vendor-documented (all four vendors document CMEK; the 30–60% performance figure for Azure AI Search is from Microsoft's own docs, confirmed accurate as of 2026-07-02)

---

## Practice 6: Turn on audit logging before you index any real data

**Do:** Turn on diagnostic and audit logging for every cloud-managed vector store before you store real user data. Ship the logs to a system you control. Set alerts for: unusual query volumes, failed authentication attempts, new API keys or role assignments, and any administrative changes (index creation or deletion, network policy changes).

Where to send logs:
- **Azure AI Search** — Azure Monitor / Log Analytics (enable under Diagnostic settings in the portal)
- **AWS OpenSearch Serverless** — AWS CloudTrail + S3 or CloudWatch (enable data-plane audit logging explicitly — see below)
- **Google Vertex AI Vector Search** — Google Cloud Audit Logs + Cloud Logging (enable Data Access audit logs)
- **Pinecone** — Enterprise plan only; configure the audit log integration in your organization settings (must be done by an organization owner — the top-level account, not a project member)

**Plain-language glossary for this practice:**
- **Audit log:** A record of who did what and when. For a vector store, this includes: who queried, what they searched for, who created or deleted an index, who changed access settings.
- **Diagnostic logging / data-plane logging:** Logs about the data operations (queries, writes, deletes). Many services log only administrative operations by default; data-plane logs must be turned on separately.
- **CloudTrail:** AWS's service that records API calls made to AWS services. Logs control-plane operations by default; data-plane logging requires extra configuration.
- **CloudWatch:** AWS's monitoring and alerting service. You can ship CloudTrail logs to CloudWatch and set alarms.
- **Log Analytics / Azure Monitor:** Microsoft's log collection and querying service. Azure AI Search can send its diagnostic logs here.
- **SIEM (Security Information and Event Management):** Software that collects logs from many sources and alerts you to suspicious patterns. Examples include Splunk, Microsoft Sentinel, and Datadog. You do not need a SIEM to start — routing logs to CloudWatch or Log Analytics is a good first step.
- **Access Transparency logs (Google):** A separate log type that records when Google personnel access your data.

**Why this matters for beginners:** You cannot detect a breach you do not log. AWS OpenSearch Serverless did not have data-plane audit logging at all until November 2025 — before that, user queries, index modifications, and authorization attempts were completely invisible. Several services log only administrative events by default; logs of actual data access require explicit enablement. Without logs, you will not know if a misconfigured endpoint was probed, if an insider copied your embeddings, or when a security setting was changed.

**Service-specific notes:**
- **Pinecone** — Audit logs are available on the **Enterprise plan only**. Events are captured in batches approximately every 30 minutes 🕒 (verify live — Pinecone may change batch frequency) and delivered as JSON. Only events since the integration was created are captured — there is no historical backfill.
- **Azure AI Search** — Diagnostic logging to Azure Monitor is not on by default. Enable it in the portal under Diagnostic settings. The docs also recommend enabling query monitoring (which captures query text and latency) and setting alert rules for query volume spikes and failed authentication.
- **AWS OpenSearch Serverless** — CloudTrail logs control-plane API calls by default. Data-plane audit logging (user queries, index writes, authorization attempts) was released on **18 Nov 2025** and requires explicit configuration. In the AWS Console, go to CloudTrail and configure event selectors for OpenSearch Serverless data events.
- **Vertex AI Vector Search** — Admin activity logs are on by default. Data read/write logs are off by default — enable them under Google Cloud Audit Logs > Data Access in the IAM & Admin console.

⚠️ **WARNING (Pinecone):** If you do not enable the audit log integration on the day you go to production, all activity before that point is permanently unlogged — there is no way to retrieve it later. Set up audit logging before your first production index is created, and make sure you are logged in as the organization owner (not a project member) when you do so.

**Sources:**
- [aws.amazon.com — Amazon OpenSearch Serverless now supports audit logs for data plane APIs](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-opensearch-serverless-auditlogs-dataplane-apis/) (AWS, Nov 2025)
- [docs.aws.amazon.com — OpenSearch Serverless logging with CloudTrail](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/logging-using-cloudtrail.html) (AWS, accessed Jul 2026)
- [learn.microsoft.com — Azure AI Search security best practices](https://learn.microsoft.com/en-us/azure/search/search-security-best-practices) (Mar 2026)
- [docs.pinecone.io — Configure audit logs](https://docs.pinecone.io/guides/production/security-overview) (Pinecone, accessed Jul 2026)
- [cloud.google.com — Vertex AI security controls](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-controls) (Google, accessed Jul 2026)

**Confidence:** ✅ independently-corroborated (AWS release note independently confirms the November 2025 gap; multiple vendor docs confirm default-off data logging)

---

## Practice 7: Treat embeddings as sensitive data — remove personal information before indexing

**Do:** Before feeding documents into a vector store, remove or mask personally identifiable information (PII), credentials, and secrets. Do not embed raw API tokens, passwords, or health record identifiers into the vector data. Apply the same access controls to the query endpoint of your vector store that you would apply to the raw documents themselves. Periodically audit what has been indexed.

For tools to detect PII in text before indexing, search for "PII scrubbing library" for your programming language. Well-known options include Microsoft Presidio and spaCy's named-entity recognition. (These are suggestions to search for — this guide does not endorse specific tools; choose based on your needs.)

**Why this matters for beginners:** Vector embeddings are not opaque blobs of random numbers. Researchers have demonstrated that the original text of a sentence can be reconstructed from its embedding with meaningful accuracy. Researchers who investigated publicly exposed vector databases in 2024 found indexes containing plaintext credentials, national ID numbers, medical diagnoses, and biometric records. Access to the query endpoint of any vector store is effectively read access to a compressed form of your most sensitive data.

**A note on the evidence:** OWASP (the Open Web Application Security Project, a widely respected non-profit) independently documents this vulnerability class as LLM08:2025 — Vector and Embedding Weaknesses. The quantitative accuracy figures for how well text can be recovered from embeddings rest on a single secondary blog and a source with a conflict of interest; treat them as directionally accurate, not as precision measurements.

⚠️ **WARNING:** Metadata stored alongside vectors — document titles, source URLs, user IDs, filter fields — is returned in plaintext by default on all four services. Scrubbing the embedding vector is not sufficient if sensitive data also appears in metadata fields. Check every field you store alongside your vectors.

**Sources:**
- [dev.to — Vector database breaches: how embeddings expose sensitive data](https://dev.to/tiamatenity/vector-database-breaches-how-embeddings-expose-your-sensitive-data-21a9) (May 2026 — single secondary blog)
- [ironcorelabs.com — Pinecone vector database security review](https://ironcorelabs.com/vectordbs/pinecone-security/) (Mar 2024 — IronCore sells a competing product; treat as editorially partial)
- [genai.owasp.org — LLM08:2025 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm08-excessive-agency/) (2025 — note: URL slug `/llm08-excessive-agency/` is misleading but page content is correctly titled "Vector and Embedding Weaknesses")

**Confidence:** 📄 vendor-documented / **thin** for quantitative reversal claims (OWASP independently corroborates the vulnerability class; specific embedding-reversal accuracy figures for cloud-managed services rest on a single secondary blog and a conflicted vendor). See also the RAG pipeline entry for stronger sourcing on the Ghost Vectors inversion research.

---

## Practice 8: Do not use wildcard ("allow everything") permissions in production

**Do:** Grant only the minimum operations a workload actually needs. Avoid "allow everything" wildcard permissions.

- **AWS OpenSearch Serverless** — Grant only `aoss:ReadDocument` and `aoss:DescribeIndex` (for a read-only RAG query service) rather than `aoss:*`. Set these in the AWS Console under OpenSearch Serverless > Data access policies, or in a JSON policy document via the CLI.
- **Azure AI Search** — Assign `Search Index Data Reader` to query-only applications rather than `Search Index Data Contributor` (which can overwrite and delete index content) or `Search Service Contributor`. Set these in the portal under your search service > Access Control (IAM) > Add role assignment.
- **Pinecone** — Use `DataPlaneViewer` for apps that only query, not `DataPlaneEditor`.

**Plain-language glossary for this practice:**
- **Wildcard permission (`aoss:*`):** A shorthand that grants all possible operations. Convenient to set up, dangerous in production — a compromised credential can do anything.
- **Least-privilege roles:** Pre-defined permission sets that grant only specific operations. `Search Index Data Reader` on Azure, for example, lets you query but not modify.
- **Break-glass / just-in-time (JIT) access:** An emergency procedure that grants elevated permissions temporarily, only when needed, and automatically revokes them. This prevents the situation where you gave everyone admin access "just in case" — you give normal accounts minimal access and have a documented process for emergency escalation.

**Why this matters for beginners:** Permissions on AWS OpenSearch Serverless are additive — a broader permission granted by one policy cannot be narrowed by a later more-restrictive policy on the same identity. Granting `aoss:*` means that even if you later try to restrict that identity, the wildcard stands. On Azure, `Search Index Data Contributor` lets an application overwrite or delete all your indexed content; only `Search Index Data Reader` is appropriate for a RAG query path.

**Caveat:** Overly narrow permissions can block legitimate emergency access. Before you restrict permissions, build a break-glass procedure (a documented way for an authorized person to get temporary elevated access in an emergency) so that least-privilege does not block you when you need to respond to an incident.

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

---

## CHANGELOG

### Grading corrections applied in the technical entry (before re-leveling)

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
14. Skeptic FLAG: Practice 2 — added note that dev.to incident is a single secondary blog; vendor identity left as-is.

### Beginner re-level changes (rings-beginner-author, re-leveled from the 2026-07-09 technical entry; facts unchanged)

Applied all findings from `grading/2026-07-09/beginner.md` section `## cloud-managed.md`:

- **[FIX] Practice 1 — VPC/private endpoint jargon:** Added plain-language glossary defining VPC, private endpoint, PrivateLink, Private Service Connect, and VPC Service Controls on first use.
- **[FIX] Practice 1 — concrete first steps:** Added "Where to actually make this change" section with specific UI paths and CLI commands for all four services (Azure portal path + CLI command; AWS Console path; Pinecone console reference; Vertex AI endpoint option).
- **[FIX] Practice 1 — WARNING rephrasing:** Replaced "high-security environments" with "if you have restricted public network access — it will connect anyway" for clarity.
- **[FIX] Practice 2 — SigV4/SAML/control-plane/data-plane jargon:** Added plain-language glossary defining API key, IAM, Entra RBAC, SigV4 signing, SAML, control-plane vs. data-plane, and service account.
- **[FIX] Practice 2 — CLI prerequisite:** Added note that the `az` CLI must be installed, logged in, and pointing at the right subscription before the `az search service update` command will work.
- **[FLAG] Practice 2 — aadOrApiKey/RBAC/Entra in WARNING:** Added parenthetical "(Entra RBAC = Azure's identity-based permission system, as opposed to the old shared-key approach)" in the WARNING.
- **[FIX] Practice 3 — RBAC/ARN/Organization Policy Service jargon:** Added plain-language glossary defining least privilege, ARN, aoss: actions, and Organization Policy Service.
- **[FLAG] Practice 4 — CVE/CVSS terminology:** Added explanation that CVE = Common Vulnerabilities and Exposures (a public database) and CVSS is a severity score on a 0–10 scale.
- **[FLAG] Practice 4 — Pinecone private endpoint WARNING placement:** The WARNING about Pinecone private endpoints affecting the entire project is now present in both Practice 1 (where private endpoints are first introduced) via the Pinecone-specific notes, and in Practice 4 as a standalone ⚠️ WARNING, as the grading file noted a beginner may apply Practice 1 before reaching Practice 4.
- **[FIX] Practice 5 — CMEK/KMS/HIPAA/AES-256/OCU jargon:** Added plain-language glossary and a simple test ("if your app handles medical records, financial data, or EU personal data, you likely need CMEK").
- **[KILL] Practice 5 — irrecoverable AWS key choice:** Promoted "cannot change encryption key after collection creation" from buried prose to a standalone ⚠️ WARNING block with explicit language about the irrecoverable nature of the choice.
- **[FIX] Practice 6 — CloudTrail/CloudWatch/SIEM/diagnostic logging jargon:** Added plain-language glossary defining audit log, diagnostic logging, CloudTrail, CloudWatch, Log Analytics, SIEM (with examples: Splunk, Sentinel, Datadog), and Access Transparency logs.
- **[FLAG] Practice 6 — "organization owner" clarified:** Added note that Pinecone audit log integration must be set up by the organization owner (top-level account), not a project member.
- **[FIX] Practice 7 — removed unverified 85%+ figure from body text:** Body text no longer presents a precision statistic as established fact; language is "meaningful accuracy" consistent with what sources actually support.
- **[FLAG] Practice 7 — PII scrubbing tools:** Added mention of Microsoft Presidio and spaCy as examples of PII-detection libraries a beginner can search for, with explicit note that these are suggestions, not endorsements.
- **[FLAG] Practice 8 — role assignment navigation:** Added "where to navigate" context for Azure (Access Control / IAM > Add role assignment) and AWS (OpenSearch Serverless > Data access policies). Added plain-language definition of "break-glass / JIT access."

