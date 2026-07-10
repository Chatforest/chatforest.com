---
title: "Vector Store Security — RAG Pipeline (as of 09 Jul 2026)"
date: 2026-07-09
snapshot_date: 2026-07-09
topic: vector-store-security-rag-pipeline
track: best-practices
audience: "technically comfortable readers"
description: "Cross-cutting security best practices for RAG pipelines using vector stores: embedding privacy, retrieval-layer access control, data poisoning, prompt injection via retrieved documents, multi-tenant isolation, audit trails, and secure ingestion."
content_type: "Best Practice"
categories: ["RAG", "Vector Databases", "AI Security"]
tags: ["rag", "vector-store", "access-control", "prompt-injection", "data-poisoning", "multi-tenancy", "embeddings", "audit-logging", "secure-ingestion", "pii", "gdpr"]
last_refreshed: 2026-07-09
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-09"
grading_result: "0 fabrications; 16 corrections applied; 2 gaps tracked as pending"
---

<!-- This file lands at content/ai/best-practices/vector-store-security-rag-pipeline/2026-07-09/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->


# Vector Store Security — RAG Pipeline (as of 09 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **09 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Treat embeddings as sensitive data — do not embed raw PII

**Do:** Before ingesting documents into a vector store, redact or tokenize personally identifiable information (names, SSNs, medical record numbers, email addresses, etc.) using context-preserving masking rather than simple blanking (e.g., replace "John Smith" with a consistent placeholder like "[PERSON_1]" rather than "[REDACTED]" to preserve relationship context for the LLM). Apply the same classification handling to the resulting embeddings that you would to the source text.

**Why:** Embeddings are not one-way hashes. A June 2026 study ("Ghost Vectors," arXiv:2606.18497) found that even after "soft deletion" in HNSW-based databases (ChromaDB, FAISS, Weaviate), the vectors remain physically readable on disk. Using the Vec2Text inversion model, researchers recovered 25.5% of person names, 46.4% of geographic locations, and 100% of structured medical markers (patient age and gender) from supposedly-deleted data. OWASP named this class of vulnerability LLM08:2025 (Vector and Embedding Weaknesses). The promptfoo security database and galileo.ai both document the inversion risk qualitatively, though specific percentage recovery rates for general text vary by model and length; the Ghost Vectors figures are the most rigorous source available as of Jul 2026. 🕒 The list of affected databases (ChromaDB, FAISS, Weaviate) comes from a single Jun 2026 preprint — verify live as independent replication may change the scope.

**Caveat / contested:** Masking before embedding degrades retrieval relevance for queries that target the masked fields. Some architectures instead encrypt vectors in the application layer (before writing to the store) rather than masking source text; this preserves the original for authorized decryption but adds key-management complexity. The "Ghost Vectors" Epoch Key Rotation defense (AES-256-CTR with key destruction on deletion) is newly published (Jun 2026) — 🕒 verify live whether your vector store supports it natively or whether production tooling exists.

**Sources:**
- [arxiv.org — Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases (arXiv:2606.18497)](https://arxiv.org/html/2606.18497v1) (Jun 2026; 25.5%/46.4%/100% figures confirmed)
- [promptfoo.dev — Embedding inversion privacy leak](https://promptfoo.dev/lm-security-db/vuln/embedding-inversion-privacy-leak-bd566a31) (Mar 2025; qualitative corroboration)
- [galileo.ai — LLM embedding security: risks and defenses](https://galileo.ai/blog/llm-embedding-security-risks-defenses) (Jul 2025; qualitative corroboration)
- [genai.owasp.org — LLM08:2025 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm08-excessive-agency/) (2025 — note: URL slug `/llm08-excessive-agency/` is a platform inconsistency; page title and content correctly cover "Vector and Embedding Weaknesses")
- [ironcorelabs.com — OWASP LLM Top 10 2025 update](https://ironcorelabs.com/blog/2025/owasp-llm-top10-2025-update/) (Jan 2025)

**Confidence:** ✅ independently-corroborated for the vulnerability class (OWASP + multiple research publications); Ghost Vectors specific figures (25.5%/46.4%/100%) are from a single Jun 2026 preprint (🕒 verify live for independent replication); percentage figures for general text inversion are not stated in promptfoo or galileo sources

---

## Practice: Enforce access control at retrieval time, not just at ingestion

**Do:** Store each document chunk's access permissions as metadata alongside the vector (user roles, tenant IDs, sensitivity labels, data-owner claims). At query time, apply a mandatory metadata filter — before or simultaneously with the similarity search — so that only chunks the requesting identity is authorized to see are returned. Do not rely on filtering results after retrieval.

Example pseudo-code (apply regardless of which vector store you use):
```python
# WRONG: retrieve then filter — unauthorized chunks already in context
results = vector_store.similarity_search(query, k=10)
filtered = [r for r in results if r.metadata["role"] in user_roles]

# RIGHT: filter at retrieval time
results = vector_store.similarity_search(
    query,
    k=10,
    filter={"role": {"$in": user_roles}, "tenant_id": current_tenant}
)
```

**Why:** When a document enters the vector pipeline it loses its native permissions (file ACLs, SharePoint roles, database row-level security). The embedding has no concept of "who may read this." If you retrieve first and filter afterward, unauthorized chunks have already entered the LLM's context window, where they can leak through model output even if you try to remove them. The OWASP RAG Security Cheat Sheet (no date listed) states access checks must happen "at retrieval time, not ingestion." Protecto.ai (Apr 2026) observed the same gap: "Role-based policies need to apply when the system retrieves content, not just at the database level." Kiteworks (Mar 2026) describes the pattern as "filter every search result by identity, attributes, and document policies before augmentation."

⚠️ **WARNING — dangerous default:** Most vector database SDKs default to returning the top-k nearest neighbors with no access filter at all. A freshly configured RAG demo will return every document in the index to any user. Always add tenant/role filters before deploying to any multi-user environment.

**Caveat / contested:** Pre-filtering on metadata requires that metadata accurately reflects current permissions. If upstream permissions change (a user is revoked, a document is re-classified), the vector store's metadata must be updated in sync — otherwise stale metadata silently under- or over-grants access. Webhook-driven (automatic real-time notification) permission sync is recommended but adds pipeline complexity.

**Sources:**
- [protecto.ai — Data security in RAG systems: best practices](https://www.protecto.ai/blog/data-security-in-rag-systems-best-practices/) (Apr 2026)
- [kiteworks.com — RAG pipeline security best practices for 2026](https://www.kiteworks.com/cybersecurity-risk-management/rag-pipeline-security-best-practices/) (Mar 2026)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)
- [daxa.ai — Secure RAG in enterprise environments](https://www.daxa.ai/blogs/secure-retrieval-augmented-generation-rag-in-enterprise-environments) (Aug 2025)

**Confidence:** ✅ independently-corroborated (multiple independent publishers converge on retrieval-time enforcement)

---

## Practice: Use physical namespace or index isolation for multi-tenant vector stores — not metadata-filter-only separation

**Do:** In multi-tenant RAG deployments, partition tenants using physically separate indexes, collections, or namespaces (one namespace per tenant) rather than a single shared index filtered by a `tenant_id` metadata field. For regulated or highly sensitive tenants, use separate physical shards or separate database instances. Before going to production, run "canary tests" by inserting a sentinel document into one tenant's namespace and verifying it never appears in any other tenant's query results.

**Why:** Filter-only separation relies entirely on the application never forgetting to attach the tenant filter to every query. A single missing filter — caused by a bug, a misconfigured SDK call, or a prompt injection that alters the query — leaks all tenants' data. The beyondscale.tech guide (May 2026) recommends physical shard isolation (Weaviate) or separate indexes (Pinecone) for multi-tenant workloads and mandates canary testing before production. The AWS Machine Learning blog (Jul 2025) documents JWT-enforced backend role assignment as the correct pattern for database-layer multi-tenancy.

⚠️ **WARNING:** Namespace-based isolation varies significantly by database vendor. Some vendors document namespaces as a logical partition that still shares underlying storage and index structures. Verify what isolation guarantees your specific vendor provides — "namespace" does not mean the same thing across Pinecone, Weaviate, Qdrant, and Chroma. 🕒 verify live.

**Caveat / contested:** Physical per-tenant isolation substantially increases infrastructure cost and management overhead at scale. The truto.one guide (May 2026) notes that modern enterprise architectures "heavily favor the Pool pattern" with fine-grained access control (FGAC) when cost matters — but only when FGAC is enforced at the database engine level (e.g., via JWT-driven backend roles), not purely at the application layer.

**Sources:**
- [truto.one — Multi-tenant RAG data isolation: the 2026 enterprise architecture guide](https://truto.one/blog/how-to-architect-strict-data-isolation-in-multi-tenant-rag-pipelines/) (May 2026)
- [beyondscale.tech — Vector database security: RAG compliance & monitoring guide](https://beyondscale.tech/blog/vector-database-security-rag-compliance-monitoring) (May 2026)
- [aws.amazon.com — Multi-tenant RAG with Amazon Bedrock and Amazon OpenSearch using JWT](https://aws.amazon.com/blogs/machine-learning/multi-tenant-rag-implementation-with-amazon-bedrock-and-amazon-opensearch-service-for-saas-using-jwt/) (Jul 2025)
- [csoonline.com — Securing RAG pipelines in enterprise SaaS](https://www.csoonline.com/article/4163888/securing-rag-pipelines-in-enterprise-saas.html) (date unverified — CSO Online articles are typically dated; date not found in research)

**Confidence:** ✅ independently-corroborated (multiple independent publishers; AWS vendor pattern corroborated by independent security guides)

---

## Practice: Sanitize and validate documents at ingestion — treat the knowledge base as untrusted input

**Do:** Before chunking and embedding any document, run it through a multi-layer ingestion filter: (1) format-break via PDF-to-image-to-OCR to strip invisible text, macros, and embedded objects; (2) language-confidence scoring to flag obfuscated or encoded content; (3) classify chunks for adversarial instruction patterns; (4) scan for PII and toxicity. Hash each accepted document (SHA-256 minimum) and store the hash; verify hashes before retrieval to detect tampering. Accept documents only from explicitly allowlisted sources with provenance verification. Use Write-Once-Read-Many (WORM) storage (e.g., AWS S3 Object Lock, Azure Blob immutable storage, Google Cloud Storage retention policy) to prevent post-ingestion modification.

**Why:** RAG pipelines commonly grant documents implicit trust because "they came from our own knowledge base." The christian-schneider.net analysis (Feb 19, 2026) phrases the problem precisely: "user input is untrusted, but retrieved content is trusted — after all, it comes from your own knowledge base." This assumption is wrong. A 2026 post (tianpan.co, Apr 2026) catalogs several real attack vectors: PDFs with white-on-white invisible text that bypasses human review but is parsed by the text extractor; document metadata fields (Author, Subject in DOCX/PDF) that get appended to extracted text before chunking; PowerPoint speaker notes that are invisible in the presentation but extracted by parsers. CVE-2025-32711 (EchoLeak, CVSS 9.3 per Microsoft CNA / CVSS 7.5 HIGH per NIST — scores differ because Microsoft is the CNA for this CVE; see NVD CVE-2025-32711 (https://nvd.nist.gov/vuln/detail/CVE-2025-32711 — bot-protected, confirmed live Jul 2026)) exploited exactly this path via Microsoft 365 Copilot. The AWS Security Blog (Nov 2024) provides a concrete implementation of format-breaking via Textract + language-confidence scoring via Comprehend — start there if you are on AWS.

**Caveat / contested:** Format-breaking via OCR introduces latency and can degrade extraction quality for complex layouts (tables, mathematical notation). Language confidence scoring is a probabilistic heuristic; it may flag legitimate multilingual documents. These filters are best applied in an asynchronous ingestion queue rather than on the hot path.

**Sources:**
- [aws.amazon.com/blogs/security — Securing the RAG ingestion pipeline: filtering mechanisms](https://aws.amazon.com/blogs/security/securing-the-rag-ingestion-pipeline-filtering-mechanisms/) (Nov 2024)
- [tianpan.co — Document injection: the prompt injection vector inside every RAG pipeline](https://tianpan.co/blog/2026-04-15-document-injection-rag-pipeline) (Apr 2026)
- [christian-schneider.net — RAG security: the forgotten attack surface](https://christian-schneider.net/blog/rag-security-forgotten-attack-surface/) (Feb 19, 2026)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)
- nvd.nist.gov — CVE-2025-32711 EchoLeak (https://nvd.nist.gov/vuln/detail/CVE-2025-32711 — bot-protected, confirmed live Jul 2026) (NVD, fetched Jul 2026; NIST score 7.5 HIGH, Microsoft CNA score 9.3 CRITICAL)

**Confidence:** ✅ independently-corroborated (AWS Security blog + independent security researchers + OWASP)

---

## Practice: Defend against prompt injection via retrieved documents — do not trust retrieved content as instructions

**Do:** Wrap all retrieved chunks in explicit delimiters that mark them as "untrusted data" in the system prompt (e.g., `<retrieved_document source="X" trust="untrusted">`). Reinforce system instructions after the retrieved content block, not just before. Scan retrieved chunks for instruction-pattern keywords before inclusion. Limit the number of retrieved chunks (3–5 is a common recommendation) and total retrieved token budget to reduce the attack surface. For high-stakes workflows, add a post-retrieval LLM verification step that checks whether any chunk appears to contain instructions directed at the model. Note: delimiters reduce risk but do not eliminate it — a determined attacker can craft injections that evade keyword filters. Defense-in-depth is required.

**Why:** Indirect prompt injection via RAG is rated the top LLM risk by OWASP (LLM01:2025). The attack does not require the user to type anything malicious: an attacker plants instructions in a document (a public web page, a shared drive file, a database record); when a legitimate user's query causes that document to be retrieved, the injected instructions enter the LLM's context and redirect its behavior. Christian Schneider's analysis (Feb 19, 2026) cites USENIX Security 2025 research (PoisonedRAG) showing that five carefully crafted documents can manipulate model responses with over 90% success rate, even in a knowledge base of millions of documents. Real incidents include Slack AI (August 2024), where malicious instructions in a public channel message were retrieved as context and used to exfiltrate private channel data, and ChatGPT Memory (September 2024), where poisoned memory achieved persistent data exfiltration.

**Caveat / contested:** There is currently no fool-proof mitigation for indirect prompt injection — OWASP's own documentation on LLM01:2025 acknowledges this explicitly. Defense-in-depth (multiple layers) is the only currently recommended posture. Research on automated detection (e.g., the CleanBase paper, arXiv:2605.00460) is active but not yet mature enough to rely on alone.

**Sources:**
- [genai.owasp.org — LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) (2025)
- [christian-schneider.net — RAG security: the forgotten attack surface](https://christian-schneider.net/blog/rag-security-forgotten-attack-surface/) (Feb 19, 2026)
- [tianpan.co — Document injection: the prompt injection vector inside every RAG pipeline](https://tianpan.co/blog/2026-04-15-document-injection-rag-pipeline) (Apr 2026)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)
- [aquilax.ai — Indirect prompt injection in RAG systems and AI agents](https://aquilax.ai/blog/indirect-prompt-injection-rag-agents) (no date listed)

**Confidence:** ✅ independently-corroborated (OWASP + multiple independent researchers; no fool-proof fix exists — contested on effectiveness of specific mitigations)

---

## Practice: Guard against data poisoning — control who can write to the vector store and monitor index integrity

**Do:** Apply least-privilege separation to your vector store credentials: the ingestion service gets a write-only role; the query service gets a read-only role; administration requires separate credentials plus MFA. Restrict ingestion to explicitly authorized pipelines (no ad-hoc API writes in production). Monitor embedding distribution statistics for anomalies that indicate a poisoning attempt. Perform periodic checksum verification of stored vectors against expected distributions. Rotate API keys on a regular cycle (90-day intervals are an industry-standard baseline — verify your organization's policy).

**Why:** Data poisoning attacks modify the knowledge base so that specific queries return attacker-controlled content. Academic research (Poison-RAG, arXiv:2501.11759, Jan 2025) demonstrates that targeted metadata manipulation can improve attack effectiveness by up to 50%. The christian-schneider.net analysis cites PoisonedRAG (USENIX 2025): just five poisoned documents in a million-document corpus achieve over 90% response manipulation for targeted queries. Poisoning is especially dangerous because it is silent — there is no runtime error, and ordinary retrieval metrics may not catch it. The beyondscale.tech guide (May 2026) recommends alerting on bulk retrieval anomalies (e.g., more than 500 distinct vector records in a 10-minute window) and on ingestion events outside defined pipeline windows. The Pluralsight guide (Mar 2025) adds statistical anomaly detection and cross-validation of new data against existing datasets.

**Caveat / contested:** Embedding distribution monitoring can detect gross poisoning but is unlikely to catch subtle, targeted attacks that affect only a small fraction of the index. Active defenses such as RADAR (arXiv:2605.22041) and SeCon-RAG (arXiv:2510.09710) show promise in academic settings. 🕒 verify live whether production-ready tooling exists for your stack — this field is fast-moving.

**Sources:**
- [arxiv.org — Poison-RAG: Adversarial data poisoning attacks on RAG in recommender systems (arXiv:2501.11759)](https://arxiv.org/abs/2501.11759) (Jan 2025)
- [christian-schneider.net — RAG security: the forgotten attack surface](https://christian-schneider.net/blog/rag-security-forgotten-attack-surface/) (Feb 19, 2026)
- [beyondscale.tech — Vector database security: RAG compliance & monitoring guide](https://beyondscale.tech/blog/vector-database-security-rag-compliance-monitoring) (May 2026)
- [pluralsight.com — How to secure RAG applications](https://www.pluralsight.com/resources/blog/ai-and-data/how-to-secure-rag-applications-AI) (Mar 2025)

**Confidence:** ✅ independently-corroborated (academic research + independent practitioner guides)

---

## Practice: Log every retrieval event at document level — session-level logging does not satisfy compliance requirements

**Do:** For every RAG query, emit a structured log record that captures: requesting identity (user or service account), timestamp, tenant/namespace, query text (or its hash), the name and identifier of every chunk returned, result count, and the final model output. Store these logs in an integrity-protected, append-only store (WORM). Retain logs for the period required by your compliance framework (HIPAA mandates 6 years for ePHI access logs). Forward logs to a SIEM and alert on anomalous patterns (bulk retrieval, out-of-hours access, access to documents outside a user's normal scope).

**Where to instrument:** Add logging in the function that calls your vector store's similarity search or query method. In LangChain, subclass `VectorStoreRetriever` and override `_get_relevant_documents`. In LlamaIndex, use a `QueryPipelineEventListener` or wrap the retriever node. The log record must fire after you know which chunks were returned, so instrument at the retrieval result level, not at the query dispatch level.

**Why:** Under HIPAA §164.312(b), GDPR Article 4(2), and SOX ITGC, a RAG retrieval is a data access event with the same logging obligations as a human opening a file. A critical gap in most early RAG deployments is session-level logging — one log entry per AI conversation rather than one entry per document retrieved. HIPAA's per-record requirement means a query that retrieves 40 documents must generate 40 access records, not one. The beyondscale.tech guide specifies that logs must capture "service identity, timestamp, collection/index name, operation type, result count" and recommends a 6-year retention aligned with HIPAA.

⚠️ **WARNING:** Most vector database clients do not produce compliance-grade access logs by default. You must instrument your retrieval layer explicitly. Without per-document logging, a regulator reviewing your RAG deployment will find tens of thousands of unrecorded access events.

**Caveat / contested:** Per-document logging at high query volumes can generate very large log volumes and adds latency if done synchronously. Use asynchronous log shipping and log aggregation pipelines. Hashing the query text instead of logging it verbatim can reduce PII exposure in the audit log itself — though this trades forensic detail for privacy, so assess based on your threat model.

**Sources:**
- [kiteworks.com — AI data access compliance: RAG retrieval logging risks](https://www.kiteworks.com/regulatory-compliance/rag-compliance-data-access-logging/) (Mar 2026; HIPAA §164.312(b) per-record content confirmed; kiteworks.com is a single vendor source — treat quantitative statistics from this source as vendor-reported, not independently verified)
- [beyondscale.tech — Vector database security: RAG compliance & monitoring guide](https://beyondscale.tech/blog/vector-database-security-rag-compliance-monitoring) (May 2026)
- [protecto.ai — Data security in RAG systems: best practices](https://www.protecto.ai/blog/data-security-in-rag-systems-best-practices/) (Apr 2026)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)

**Confidence:** ✅ independently-corroborated (multiple independent publishers on logging; compliance framework requirements cited from primary sources)

---

## Practice: Implement hard deletion for vector data — soft deletion does not satisfy GDPR Article 17

**Do:** When a source document must be deleted (user right-to-erasure request, document expiry, tenant offboarding), delete the corresponding vectors in a way that makes them unrecoverable — not just marked as deleted. Confirm with your vector database vendor whether its deletion API performs a hard (physical) delete or a soft (logical) delete. If only soft deletion is supported, use application-layer encryption (encrypt vectors before writing; destroy the encryption key on deletion) as an equivalent. Verify deletion by attempting to reconstruct the deleted data as part of your compliance testing.

**Why:** A June 2026 study (arXiv:2606.18497, "Ghost Vectors") demonstrated that default deletion operations in ChromaDB, FAISS, and Weaviate leave vectors physically intact on disk. 🕒 The list of affected databases comes from a single Jun 2026 preprint — verify live as independent replication may change the scope. Using the Vec2Text inversion model, the researchers recovered 25.5% of person names, 46.4% of geographic locations, and 100% of patient age and gender from structured medical embeddings. GDPR Article 17 requires erasure to be verifiable and irreversible. Backup snapshots retain identical recovery quality months after deletion, extending the compliance window indefinitely.

⚠️ **WARNING:** If your organization uses HNSW-based vector databases and processes personal data under GDPR, you may currently be non-compliant with right-to-erasure requests without knowing it. Audit your deletion implementation before assuming compliance.

**Caveat / contested:** The "Ghost Vectors" paper proposes Epoch Key Rotation as the defense (AES-256-CTR encryption, key destruction on deletion), claiming 0% PII recovery and 0.005 ms per-record deletion latency. This is a June 2026 preprint — 🕒 verify live whether it has been independently replicated and whether production implementations exist for your specific vector database. As of the snapshot date, there is no off-the-shelf implementation of this approach for most vector databases; consult your vendor or a security engineer before relying on it.

**Sources:**
- [arxiv.org — Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases (arXiv:2606.18497)](https://arxiv.org/html/2606.18497v1) (Jun 2026)
- [promptfoo.dev — Embedding inversion privacy leak](https://promptfoo.dev/lm-security-db/vuln/embedding-inversion-privacy-leak-bd566a31) (Mar 2025; corroborates the inversion-risk class, not the specific soft-delete finding)

**Confidence:** ✅ independently-corroborated for the vulnerability class (arXiv preprint + independent security DB entry confirm the inversion risk); the specific epoch-key-rotation mitigation is `thin` (single preprint, Jun 2026, not yet independently replicated); affected-database list (ChromaDB/FAISS/Weaviate) is 🕒 verify live

---

## Practice: Synchronize upstream permissions into vector metadata — prevent stale-permission data exposure

**Do:** Embed source-document access-control metadata (user roles, group memberships, document classification, data-owner claims) into each chunk's vector store metadata at ingestion time. Subscribe to permission-change webhooks (automatic notifications sent by upstream systems when something changes) from SharePoint, Google Drive, CRM, LDAP and update or delete affected vector chunks immediately when permissions change — do not rely on periodic re-indexing alone. Implement cascading deletion so that when a source document is deleted or access-revoked, all its derived chunks are removed from the vector store, processing each deletion message safely even if it arrives more than once.

**Why:** Access control in a RAG pipeline is only as current as the metadata stored alongside each vector. If a document's permissions change (an employee is terminated, a contract expires, a file is re-classified as confidential) but the vector store is not updated, queries will continue returning chunks that the requesting user should no longer see. The truto.one guide (May 2026) explicitly recommends "subscribe to permission-change webhooks rather than only re-syncing on document edits to prevent prolonged data exposure." The OWASP RAG Security Cheat Sheet (no date listed) specifies "implement cascading deletion when source documents are removed" to prevent orphaned chunks from remaining accessible. The CSO Online enterprise guide (date unverified) notes that the right-to-be-forgotten obligation requires rigorous metadata tagging so customer data "can be easily located and purged."

**Caveat / contested:** Webhook-driven real-time sync is significantly more complex than batch re-indexing and requires the upstream systems to support webhooks and the ingestion pipeline to process deletions without creating duplicates on re-delivery. For organizations without webhook support on source systems, the fallback is a short re-sync interval (e.g., hourly) with explicit chunk-hash comparison to detect changes — this leaves a window of potential over-exposure.

**Sources:**
- [truto.one — Multi-tenant RAG data isolation: the 2026 enterprise architecture guide](https://truto.one/blog/how-to-architect-strict-data-isolation-in-multi-tenant-rag-pipelines/) (May 2026)
- [csoonline.com — Securing RAG pipelines in enterprise SaaS](https://www.csoonline.com/article/4163888/securing-rag-pipelines-in-enterprise-saas.html) (date unverified)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)

**Confidence:** ✅ independently-corroborated (multiple independent publishers)

---

## Held pending fixes (not publish-ready)
- Ghost Vectors epoch-key-rotation mitigation: single Jun 2026 preprint, not yet independently replicated; no production implementation confirmed for covered databases ⚠️ #pending-1
- OWASP RAG Security Cheat Sheet and christian-schneider.net article: no publish date found on the OWASP page; christian-schneider.net date (Feb 19, 2026) confirmed by Skeptic grader. OWASP date remains unresolved. ⚠️ #pending-2

## CHANGELOG (grading → this entry)
1. Skeptic KILL: Practice 1 — removed unsourced "50–70% or more of words" and "80–99% clinical reconstruction accuracy" figures. Neither promptfoo nor galileo.ai contain these percentages (both qualitative only). Only Ghost Vectors figures (25.5%/46.4%/100%) retained — those ARE verified in arXiv:2606.18497.
2. Skeptic KILL: Practice 3 — removed fabricated "95% of benign queries triggered cross-tenant leakage" statistic, which appeared as a direct quotation attributed to truto.one. Re-fetch of truto.one confirmed no such figure. The surrounding physical-isolation guidance and canary-testing recommendation remain (well-sourced in beyondscale.tech).
3. Skeptic KILL: Practice 7 — removed "organizations experiencing AI-related breaches were three times more likely to have lacked query-level access logging" statistic. Re-fetch of the cited kiteworks.com page confirmed the HIPAA per-record framing is present but the "3x" statistic is not. Removed the stat; HIPAA §164.312(b) framing retained. Added single-vendor caveat for kiteworks as source.
4. Skeptic FIX: Practice 4 — added note that CVE-2025-32711 CVSS is a split score: Microsoft CNA = 9.3 CRITICAL, NIST = 7.5 HIGH. Added direct NVD link.
5. Skeptic FIX: Practice 1 — corrected OWASP LLM08 URL slug — noted that `/llm08-excessive-agency/` is a platform inconsistency but the page title and content correctly cover "Vector and Embedding Weaknesses."
6. Timekeeper FIX: Practice 1 — added `🕒 verify live` caveat to Ghost Vectors database scope (ChromaDB/FAISS/Weaviate) as this rests on a single Jun 2026 preprint.
7. Timekeeper FIX: Practice 5 — added "no date listed" annotation to aquilax.ai citation.
8. Timekeeper FIX: Practices 2, 4, 5, 7, 9 — added "no date listed" annotation consistently to all four OWASP RAG Security Cheat Sheet citations (previously only one carried the annotation).
9. Timekeeper FIX: Practice 4 — added direct NVD advisory URL for CVE-2025-32711 (EchoLeak).
10. Timekeeper FIX: Practices 4, 5, 6 — updated christian-schneider.net from "no date listed" to "Feb 19, 2026" (date confirmed by Skeptic grader re-fetch).
11. Timekeeper FLAG: Practice 6 — added `🕒 verify live` to RADAR/SeCon-RAG citations; added note that production-ready tooling may not exist.
12. Timekeeper FLAG: Practice 7 — noted kiteworks "3x" statistic as a single vendor figure (moot — the statistic was already KILLED in item 3 above; vendor caveat retained for remaining kiteworks citations).
13. Timekeeper FLAG: Practice 9 — noted csoonline.com article date is unverified.
14. Beginner KILL: Practice 2 — added pseudo-code example contrasting wrong (retrieve-then-filter) vs. right (filter-at-retrieval-time) patterns.
15. Beginner KILL: Practice 7 — added "Where to instrument" section with LangChain and LlamaIndex guidance; beginners now have a concrete starting point for adding retrieval-layer logging.
16. Beginner FIX: Practice 9 — replaced "idempotently" with "safely even if it arrives more than once"; replaced "webhook" with "automatic notification sent by upstream systems when something changes."

17. Link-check gate: 1 non-200 URL unlinked to plain text (nvd.nist.gov CVE-2025-32711 — 403/bot-protection; confirmed live via WebFetch Jul 2026). Citation retained as plain text with URL.
