# Vector Store Security — RAG Pipeline (as of 09 Jul 2026)

> Cross-cutting security best practices for RAG pipelines using vector stores — explained for people new to AI. Covers embedding privacy, retrieval-time access control, data poisoning, prompt injection, audit logging, and GDPR deletion, with plain-language explanations and concrete code examples.


<!-- This file lands at content/ai/beginner/vector-store-security-rag-pipeline/2026-07-09/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->


# Vector Store Security — RAG Pipeline (as of 09 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **09 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## What is a RAG pipeline?

A RAG pipeline (Retrieval-Augmented Generation) is a way of making an AI chatbot smarter by giving it access to your own documents. Instead of only knowing what it learned during training, the AI can search a private library of files at question time and include relevant passages in its answer.

The "vector store" (also called a vector database) is where those documents live. Before storing a document, the system converts it into a list of numbers called an **embedding** — a mathematical fingerprint of the text's meaning. When a user asks a question, the system converts the question into its own embedding and finds the most similar documents in the store.

This guide explains the security pitfalls in that pipeline and what to do about them.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: Treat embeddings as sensitive data — do not embed raw personal information

**The core idea:** Embeddings look like harmless numbers. They are not. Researchers have shown that those numbers can be partially reversed back into the original text — meaning personal data you thought was protected may be recoverable by an attacker with the right tools.

**Do:** Before you load any document into a vector store, remove or replace personally identifiable information (PII) — names, Social Security numbers, medical record numbers, email addresses, and similar data. Use context-preserving masking: replace a name like "John Smith" with a consistent placeholder like `[PERSON_1]` rather than just `[REDACTED]`. The consistent placeholder lets the AI still understand that two mentions of the same person are connected, while the name itself is never stored. Treat the resulting embeddings with the same care as the source text — if the text is sensitive, the embedding is too.

If you already have a vector store with personal data in it, read Practice 8 (hard deletion) before assuming you can simply delete it.

**Why this matters:**

Embeddings are not one-way hashes like passwords. A June 2026 research paper nicknamed "Ghost Vectors" (arXiv:2606.18497) found that even after documents were "deleted" from three popular vector databases — ChromaDB, FAISS, and Weaviate — the underlying numbers remained physically readable on disk. Using a tool called Vec2Text (a model that reconstructs text from embeddings), the researchers recovered:

- 25.5% of person names
- 46.4% of geographic locations
- 100% of structured medical markers (patient age and gender)

The failure that gets prevented: a data breach where an attacker reads your vector database files and reconstructs patient names or medical details that you believed were safely stored as "just math."

OWASP (the Open Web Application Security Project, a widely-cited security standards body) named this class of problem LLM08:2025 (Vector and Embedding Weaknesses). 🕒 The list of affected databases (ChromaDB, FAISS, Weaviate) comes from a single Jun 2026 preprint — verify live as independent replication may change the scope.

**Caveat / contested:** Masking before embedding slightly degrades retrieval quality for queries that target the masked fields. Some systems instead encrypt the vectors in the application layer rather than masking the source text — this preserves the original for authorized decryption but adds key-management complexity. The "Ghost Vectors" paper proposes an Epoch Key Rotation defense (encrypting with AES-256-CTR and destroying the key on deletion), but this is newly published (Jun 2026) — 🕒 verify live whether your vector store supports it natively or whether production tooling exists.

**Sources:**
- [arxiv.org — Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases (arXiv:2606.18497)](https://arxiv.org/html/2606.18497v1) (Jun 2026; 25.5%/46.4%/100% figures confirmed)
- [promptfoo.dev — Embedding inversion privacy leak](https://promptfoo.dev/lm-security-db/vuln/embedding-inversion-privacy-leak-bd566a31) (Mar 2025; qualitative corroboration)
- [galileo.ai — LLM embedding security: risks and defenses](https://galileo.ai/blog/llm-embedding-security-risks-defenses) (Jul 2025; qualitative corroboration)
- [genai.owasp.org — LLM08:2025 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm08-excessive-agency/) (2025 — note: URL slug `/llm08-excessive-agency/` is a platform inconsistency; page title and content correctly cover "Vector and Embedding Weaknesses")
- [ironcorelabs.com — OWASP LLM Top 10 2025 update](https://ironcorelabs.com/blog/2025/owasp-llm-top10-2025-update/) (Jan 2025)

**Confidence:** ✅ independently-corroborated for the vulnerability class (OWASP + multiple research publications); Ghost Vectors specific figures (25.5%/46.4%/100%) are from a single Jun 2026 preprint (🕒 verify live for independent replication); percentage figures for general text inversion are not stated in promptfoo or galileo sources

---

## Practice 2: Check access permissions at search time, not just when documents are loaded

**The core idea:** When documents enter your vector store, they lose their original file permissions (the settings that say "only Alice can read this"). The vector store knows nothing about who is allowed to see what — unless you tell it at every search. Most systems do not do this by default.

**Do:** When you load each document into the vector store, save its access permissions as metadata alongside the vector (for example, store the user roles, team ID, or sensitivity label as extra fields on each document chunk). Then, every time a user asks a question, apply a filter that restricts the search to only chunks that user is allowed to see. The filter must happen during the search — not after.

Here is a concrete Python example. Both patterns below use a `vector_store.similarity_search()` call, but only one of them is safe:

```python
# WRONG: search first, filter afterward
# Unauthorized document chunks have already entered the AI's context
results = vector_store.similarity_search(query, k=10)
filtered = [r for r in results if r.metadata["role"] in user_roles]

# RIGHT: filter at search time
# Unauthorized chunks are never retrieved at all
results = vector_store.similarity_search(
    query,
    k=10,
    filter={"role": {"$in": user_roles}, "tenant_id": current_tenant}
)
```

The `filter` argument above tells the vector store to only search among documents that match the user's roles and tenant. The exact argument name and syntax varies by vector database — check your vendor's documentation for the equivalent.

⚠️ **WARNING — dangerous default:** Most vector database software development kits (SDKs — the code libraries you use to talk to the database) default to returning the top results with no access filter at all. A freshly configured RAG demo will return every document in the index to every user. Always add role and tenant filters before deploying to any multi-user environment.

**Why this matters:** When a document enters the vector pipeline it loses its native permissions. If you retrieve first and filter afterward, unauthorized document chunks have already entered the AI's context window (the text the AI can see when forming its answer), where they can leak through the AI's output even if you try to remove them afterward.

The failure prevented: a user in one team asks a question and the AI answers with confidential information from another team's documents, because no filter was applied at search time.

**Caveat / contested:** Pre-filtering on metadata requires that the metadata accurately reflects current permissions. If a user's access is revoked after the document was indexed, the vector store's metadata must be updated at the same time — otherwise stale metadata silently over-grants access. Keeping permissions in sync automatically (for example, by subscribing to automatic notifications — called webhooks — sent by SharePoint, Google Drive, or your identity system whenever permissions change) is recommended but adds complexity to the pipeline.

**Sources:**
- [protecto.ai — Data security in RAG systems: best practices](https://www.protecto.ai/blog/data-security-in-rag-systems-best-practices/) (Apr 2026)
- [kiteworks.com — RAG pipeline security best practices for 2026](https://www.kiteworks.com/cybersecurity-risk-management/rag-pipeline-security-best-practices/) (Mar 2026)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)
- [daxa.ai — Secure RAG in enterprise environments](https://www.daxa.ai/blogs/secure-retrieval-augmented-generation-rag-in-enterprise-environments) (Aug 2025)

**Confidence:** ✅ independently-corroborated (multiple independent publishers converge on retrieval-time enforcement)

---

## Practice 3: Use physically separate storage areas per tenant — do not rely on a filter tag alone

**The core idea:** If your RAG system serves multiple customers or teams (called "tenants"), you need more than a `tenant_id` label on each document. A single forgotten filter anywhere in your code could expose all tenants' data to each other.

**Do:** In multi-tenant RAG systems, give each tenant their own physically separate index, collection, or namespace (one per tenant) rather than mixing everyone's data in one shared index and relying on a filter to separate them. For highly sensitive tenants, use completely separate database instances.

Before going live with any multi-tenant system, run "canary tests": insert a uniquely identifiable test document into one tenant's area and then run queries as a different tenant, confirming that the test document never appears in the results.

⚠️ **WARNING:** The word "namespace" does not mean the same thing at every vendor. Some vendors document namespaces as a "logical partition" that still shares the same underlying storage and index structures — meaning a bug or misconfiguration can breach the boundary. When reading your vendor's documentation, look for guarantees like "complete data isolation," "separate storage," or "no cross-namespace reads possible." If the docs say only "logical partition" without those guarantees, treat it as a filter-only approach (and see why that is risky above). 🕒 verify live.

**Why this matters:** A metadata filter ("only return docs where `tenant_id = ACME`") relies entirely on your application never forgetting to attach that filter. One bug, one misconfigured SDK call, or one prompt injection attack (see Practice 5) that alters the query can silently return all tenants' data to a single user.

The failure prevented: a multi-tenant SaaS product where one customer's support query accidentally surfaces confidential documents belonging to a completely different customer.

**Caveat / contested:** Physical per-tenant isolation substantially increases infrastructure cost and management overhead at scale. Some enterprise architectures "heavily favor the Pool pattern" (one shared database with FGAC — Fine-Grained Access Control, meaning permissions enforced at the database engine level rather than only in application code) when cost matters. This is safe only when FGAC is enforced at the database engine level — for example, via JWT-driven backend roles (JWT = JSON Web Token, a signed string that proves the user's identity and carries their permission claims) — not purely in your application code.

**Sources:**
- [truto.one — Multi-tenant RAG data isolation: the 2026 enterprise architecture guide](https://truto.one/blog/how-to-architect-strict-data-isolation-in-multi-tenant-rag-pipelines/) (May 2026)
- [beyondscale.tech — Vector database security: RAG compliance & monitoring guide](https://beyondscale.tech/blog/vector-database-security-rag-compliance-monitoring) (May 2026)
- [aws.amazon.com — Multi-tenant RAG with Amazon Bedrock and Amazon OpenSearch using JWT](https://aws.amazon.com/blogs/machine-learning/multi-tenant-rag-implementation-with-amazon-bedrock-and-amazon-opensearch-service-for-saas-using-jwt/) (Jul 2025)
- [csoonline.com — Securing RAG pipelines in enterprise SaaS](https://www.csoonline.com/article/4163888/securing-rag-pipelines-in-enterprise-saas.html) (date unverified — CSO Online articles are typically dated; date not found in research)

**Confidence:** ✅ independently-corroborated (multiple independent publishers; AWS vendor pattern corroborated by independent security guides)

---

## Practice 4: Treat every document as untrusted — validate and sanitize before indexing

**The core idea:** RAG pipelines commonly assume that documents in the knowledge base are safe because "they came from our own system." That assumption is wrong. An attacker who can add a document to your knowledge base — or whose document you index from the web — can hide malicious instructions inside it.

**Do:** Before you chunk and embed any document, run it through several protective layers:

1. **Format-break:** Convert PDFs to images first, then use OCR (optical character recognition, software that reads text from images) to extract the text. This strips invisible text, hidden macros, and embedded objects that a text extractor would otherwise silently pass to the AI. If you are on AWS, the [AWS Security Blog (Nov 2024)](https://aws.amazon.com/blogs/security/securing-the-rag-ingestion-pipeline-filtering-mechanisms/) provides a working example using AWS Textract and Comprehend — start there.
2. **Language-confidence scoring:** Flag content that appears obfuscated or encoded.
3. **Instruction-pattern detection:** Classify chunks for text that looks like commands directed at an AI (see Practice 5).
4. **PII and toxicity scanning:** Scan for personal data and harmful content before embedding.

Additionally: generate a SHA-256 hash (a unique fingerprint) of each accepted document and store it. Verify the hash before retrieval to detect tampering. Accept documents only from sources you explicitly allow. Store the original documents in WORM storage — Write-Once-Read-Many, meaning storage that cannot be edited after writing. Examples include AWS S3 Object Lock, Azure Blob immutable storage, and Google Cloud Storage retention policy.

**Why this matters:** Real attack vectors include:
- PDFs with white-on-white invisible text (invisible to a human reviewer, but parsed by the text extractor)
- Document metadata fields such as Author or Subject in DOCX/PDF that get appended to extracted text before chunking
- PowerPoint speaker notes that are invisible in the presentation but extracted by parsers

A real-world attack called EchoLeak (CVE-2025-32711, severity 9.3 out of 10 per Microsoft / 7.5 per NIST — scores differ because Microsoft as the vendor assigned a higher rating than NIST independently calculated) exploited exactly this path via Microsoft 365 Copilot. In that attack, an attacker hid instructions in a document shared via Teams. When Copilot processed the document, it followed the hidden instructions and sent the user's private data to the attacker.

The failure prevented: an attacker poisons your knowledge base with a single document, causing your AI to leak secrets or act on the attacker's instructions whenever a user triggers that document's retrieval.

**Caveat / contested:** Format-breaking via OCR introduces processing delays and can reduce extraction quality for complex layouts (tables, mathematical notation). Language-confidence scoring is a probabilistic heuristic — it may flag legitimate multilingual documents. Apply these filters in an asynchronous (background) processing queue rather than in the live request path.

**Sources:**
- [aws.amazon.com/blogs/security — Securing the RAG ingestion pipeline: filtering mechanisms](https://aws.amazon.com/blogs/security/securing-the-rag-ingestion-pipeline-filtering-mechanisms/) (Nov 2024)
- [tianpan.co — Document injection: the prompt injection vector inside every RAG pipeline](https://tianpan.co/blog/2026-04-15-document-injection-rag-pipeline) (Apr 2026)
- [christian-schneider.net — RAG security: the forgotten attack surface](https://christian-schneider.net/blog/rag-security-forgotten-attack-surface/) (Feb 19, 2026)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)
- nvd.nist.gov — CVE-2025-32711 EchoLeak (https://nvd.nist.gov/vuln/detail/CVE-2025-32711 — bot-protected, confirmed live Jul 2026) (NVD, fetched Jul 2026; NIST score 7.5 HIGH, Microsoft CNA score 9.3 CRITICAL)

**Confidence:** ✅ independently-corroborated (AWS Security blog + independent security researchers + OWASP)

---

## Practice 5: Defend against injected instructions hiding in retrieved documents

**The core idea:** An attacker does not need to hack your server. They can plant instructions inside a document — a public web page, a shared file, a database record. When a user's question causes that document to be retrieved, the hidden instructions enter the AI's view and can redirect what it does. OWASP rates this the number-one LLM risk (LLM01:2025 Prompt Injection).

**Do:** Wrap all retrieved document chunks in explicit delimiters that label them as untrusted data in the AI's system prompt:

```
<retrieved_document source="X" trust="untrusted">
... chunk text here ...
</retrieved_document>
```

After the retrieved content block, repeat your system instructions — do not put them only at the top. Scan retrieved chunks for instruction-pattern keywords before including them. Limit retrieved chunks to 3–5 at a time to reduce the attack surface. For high-stakes workflows, add a post-retrieval check using a second AI call to verify whether any chunk appears to contain instructions directed at the model.

Important: these delimiters reduce risk but do not eliminate it. A determined attacker can craft injections that evade keyword filters. Multiple overlapping defenses (defense-in-depth) are required.

**Why this matters:** Research published at USENIX Security 2025 (called PoisonedRAG) showed that as few as five carefully crafted documents placed among millions can manipulate AI responses for targeted queries with over 90% success. Real incidents include:

- **Slack AI (August 2024):** Malicious instructions in a public channel message were retrieved as context and used to leak private channel data.
- **ChatGPT Memory (September 2024):** A poisoned memory entry achieved persistent data exfiltration.

The failure prevented: a user asks an innocent question; the AI retrieves a document containing hidden instructions; the AI is redirected to send the user's data to an attacker or to answer in a way the attacker chose.

**Caveat / contested:** There is currently no guaranteed fix for indirect prompt injection — OWASP's own documentation on LLM01:2025 acknowledges this explicitly. Defense-in-depth (multiple overlapping layers) is the only currently recommended posture. Research on automated detection is active but not yet mature enough to rely on alone.

**Sources:**
- [genai.owasp.org — LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) (2025)
- [christian-schneider.net — RAG security: the forgotten attack surface](https://christian-schneider.net/blog/rag-security-forgotten-attack-surface/) (Feb 19, 2026)
- [tianpan.co — Document injection: the prompt injection vector inside every RAG pipeline](https://tianpan.co/blog/2026-04-15-document-injection-rag-pipeline) (Apr 2026)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)
- [aquilax.ai — Indirect prompt injection in RAG systems and AI agents](https://aquilax.ai/blog/indirect-prompt-injection-rag-agents) (no date listed)

**Confidence:** ✅ independently-corroborated (OWASP + multiple independent researchers; no fool-proof fix exists — contested on effectiveness of specific mitigations)

---

## Practice 6: Control who can write to the vector store and watch for poisoning

**The core idea:** Data poisoning is when an attacker secretly modifies your knowledge base so that specific questions return attacker-controlled answers. There is no error message — the AI just starts lying in targeted ways.

**Do:** Separate the credentials (usernames, API keys, tokens) used for different operations:
- The service that adds documents gets a write-only credential.
- The service that answers user questions gets a read-only credential.
- Administrative tasks require separate credentials plus multi-factor authentication (MFA — requiring a second proof of identity beyond a password).

Allow only explicitly authorized pipelines to write to the vector store — no one-off API writes in production. Monitor for unusual patterns: the beyondscale.tech guide (May 2026) recommends alerting on more than 500 distinct vector records retrieved in a 10-minute window, and on any documents added outside your defined ingestion schedule. Rotate API keys regularly — 90-day intervals are an industry-standard baseline (verify your organization's specific policy).

**Why this matters:** Academic research (Poison-RAG, arXiv:2501.11759, Jan 2025) demonstrates that targeted manipulation of document metadata can improve a poisoning attack's effectiveness by up to 50%. Research at USENIX Security 2025 (PoisonedRAG) showed that five poisoned documents in a million-document database achieve over 90% response manipulation for targeted queries.

Poisoning is especially dangerous because it is silent. There is no runtime error, and ordinary quality metrics may not catch it.

The failure prevented: an attacker with access to your ingestion pipeline inserts false documents; your AI starts giving dangerous or misleading answers to specific questions without any error being raised.

**Caveat / contested:** Monitoring embedding distribution statistics can detect large-scale poisoning but is unlikely to catch subtle, targeted attacks affecting only a small fraction of the index. Academic defenses (RADAR, arXiv:2605.22041, and SeCon-RAG, arXiv:2510.09710) show promise but 🕒 verify live whether production-ready tooling exists for your stack — this field is moving quickly.

**Sources:**
- [arxiv.org — Poison-RAG: Adversarial data poisoning attacks on RAG in recommender systems (arXiv:2501.11759)](https://arxiv.org/abs/2501.11759) (Jan 2025)
- [christian-schneider.net — RAG security: the forgotten attack surface](https://christian-schneider.net/blog/rag-security-forgotten-attack-surface/) (Feb 19, 2026)
- [beyondscale.tech — Vector database security: RAG compliance & monitoring guide](https://beyondscale.tech/blog/vector-database-security-rag-compliance-monitoring) (May 2026)
- [pluralsight.com — How to secure RAG applications](https://www.pluralsight.com/resources/blog/ai-and-data/how-to-secure-rag-applications-AI) (Mar 2025)

**Confidence:** ✅ independently-corroborated (academic research + independent practitioner guides)

---

## Practice 7: Log every document retrieval — session-level logging is not enough for compliance

**The core idea:** Every time your RAG pipeline searches the vector store and returns document chunks to the AI, that is a data access event — legally equivalent to a person opening a file. Most RAG systems log only one entry per conversation, not one entry per document retrieved. That gap can put you out of compliance with regulations like HIPAA, GDPR, and SOX.

**Regulations in plain language:**
- **HIPAA** — applies if your app handles patient health records in the United States. It requires 6-year retention of access logs for electronic protected health information (ePHI).
- **GDPR** — applies if you handle personal data of people in the European Union.
- **SOX (Sarbanes-Oxley ITGC)** — may apply if you are building for a publicly traded company.

When in doubt, ask your legal team which regulations apply to your use case.

**Do:** For every RAG query, write a structured log record that captures: requesting identity (the user or service account making the query), timestamp, tenant or namespace, query text or its hash, the name and identifier of every chunk returned, result count, and the final model output.

Store these logs in an append-only store that cannot be edited after writing — WORM storage (Write-Once-Read-Many). Under HIPAA, retain logs for 6 years. Forward logs to a SIEM (Security Information and Event Management — software that collects and alerts on logs, examples include Splunk, Microsoft Sentinel, and Datadog) and configure alerts for bulk retrieval, out-of-hours access, or access to documents outside a user's normal scope.

**Where to add this logging in your code:** Add logging in the function that calls your vector store's similarity search or query method. In LangChain, subclass `VectorStoreRetriever` and override `_get_relevant_documents`. In LlamaIndex, use a `QueryPipelineEventListener` or wrap the retriever node. The log record must fire after you know which chunks were returned — instrument at the retrieval result level, not at the query dispatch level.

**Why this matters:** Under HIPAA §164.312(b), GDPR Article 4(2), and SOX ITGC, a RAG retrieval is a data access event with the same logging obligations as a human opening a file. A query that retrieves 40 document chunks must generate 40 access records, not one.

⚠️ **WARNING:** Most vector database clients do not produce compliance-grade access logs by default. You must add this instrumentation yourself. Without per-document logging, a regulator reviewing your RAG deployment will find tens of thousands of unrecorded data access events.

The failure prevented: a compliance audit reveals that your AI accessed thousands of patient or customer records with no audit trail, exposing your organization to significant regulatory liability.

**Caveat / contested:** Per-document logging at high query volumes can generate very large log volumes and adds latency if done synchronously. Use asynchronous log shipping and log aggregation pipelines. Hashing the query text (instead of logging the full text) reduces the risk of storing PII in the audit log itself — though this reduces forensic detail, so weigh the tradeoff for your threat model.

**Sources:**
- [kiteworks.com — AI data access compliance: RAG retrieval logging risks](https://www.kiteworks.com/regulatory-compliance/rag-compliance-data-access-logging/) (Mar 2026; HIPAA §164.312(b) per-record content confirmed; kiteworks.com is a single vendor source — treat quantitative statistics from this source as vendor-reported, not independently verified)
- [beyondscale.tech — Vector database security: RAG compliance & monitoring guide](https://beyondscale.tech/blog/vector-database-security-rag-compliance-monitoring) (May 2026)
- [protecto.ai — Data security in RAG systems: best practices](https://www.protecto.ai/blog/data-security-in-rag-systems-best-practices/) (Apr 2026)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)

**Confidence:** ✅ independently-corroborated (multiple independent publishers on logging; compliance framework requirements cited from primary sources)

---

## Practice 8: Delete vectors completely — marking a record as deleted is not enough for GDPR

**The core idea:** Vector databases often have a "soft delete" — they mark a record as deleted but leave the underlying numbers on disk. This does not satisfy GDPR's right-to-erasure requirement, and the data can still be reconstructed by an attacker who gains file access.

HNSW is the index structure used by most vector databases (ChromaDB, FAISS, Weaviate, and others). It lives in RAM during operation but persists to disk as files. Soft deletion updates a flag in those files but does not overwrite the actual vector data.

**Do:** When a document must be deleted (a user requests erasure of their data, a document expires, or a tenant is offboarded), verify with your vector database vendor whether the deletion API performs a hard (physical) delete — where the data is actually overwritten or removed — or only a soft (logical) delete — where the data is merely flagged as inactive.

If your database supports only soft deletion, use application-layer encryption as an equivalent: encrypt the vectors before writing them to the store, and destroy the encryption key when the data must be deleted. Without the key, the remaining numbers are unreadable.

After deletion, verify it by attempting to reconstruct the deleted data as part of your compliance testing.

⚠️ **WARNING:** If your organization uses vector databases and processes personal data under GDPR, you may currently be non-compliant with right-to-erasure requests without knowing it. Audit your deletion implementation before assuming compliance.

**Why this matters:** The "Ghost Vectors" study (arXiv:2606.18497, Jun 2026) showed that default deletion in ChromaDB, FAISS, and Weaviate leaves vectors physically intact on disk. Using the Vec2Text tool (which reconstructs text from embeddings), researchers recovered 25.5% of person names, 46.4% of geographic locations, and 100% of patient age and gender from structured medical data — months after deletion. Backup snapshots retain identical recovery quality, extending the window indefinitely. 🕒 The list of affected databases comes from a single Jun 2026 preprint — verify live as independent replication may change the scope.

GDPR Article 17 requires erasure to be verifiable and irreversible.

The failure prevented: a user submits a GDPR erasure request; you mark their records as deleted; six months later a breach reveals their data was readable the whole time.

**Caveat / contested:** The "Ghost Vectors" paper proposes Epoch Key Rotation (AES-256-CTR encryption with key destruction on deletion) as the defense, claiming 0% PII recovery and 0.005 ms per-record deletion latency. This is a June 2026 preprint — 🕒 verify live whether it has been independently replicated. As of this snapshot date, there is no off-the-shelf implementation of this approach for most vector databases — consult your vendor or a security engineer before relying on it.

**Sources:**
- [arxiv.org — Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases (arXiv:2606.18497)](https://arxiv.org/html/2606.18497v1) (Jun 2026)
- [promptfoo.dev — Embedding inversion privacy leak](https://promptfoo.dev/lm-security-db/vuln/embedding-inversion-privacy-leak-bd566a31) (Mar 2025; corroborates the inversion-risk class, not the specific soft-delete finding)

**Confidence:** ✅ independently-corroborated for the vulnerability class (arXiv preprint + independent security DB entry confirm the inversion risk); the specific epoch-key-rotation mitigation is `thin` (single preprint, Jun 2026, not yet independently replicated); affected-database list (ChromaDB/FAISS/Weaviate) is 🕒 verify live

---

## Practice 9: Keep permissions in sync — a stale permission is an access control hole

**The core idea:** The permissions stored alongside your vectors (which user can see which document) are a copy of the permissions from the original source system. If permissions change in the source system — a user is fired, a document is re-classified as confidential — but the vector store is not updated, the old access rules remain in effect silently.

**Do:** Store source-document permissions (user roles, group memberships, document classification labels, data-owner claims) in each chunk's vector store metadata at ingestion time. Subscribe to automatic notifications — called webhooks — sent by upstream systems (SharePoint, Google Drive, CRM, LDAP) whenever permissions change. When a notification arrives, update or delete the affected vector chunks immediately — do not wait for a scheduled re-index.

Implement cascading deletion: when a source document is deleted or access is revoked, all derived chunks from that document must be removed from the vector store. Process each deletion notification safely even if it arrives more than once (the technical term is "idempotent processing" — meaning the operation produces the same result whether it runs once or ten times).

**Why this matters:** Access control in a RAG pipeline is only as current as the metadata stored alongside each vector. If an employee is terminated and their file access is revoked in your HR system, but the vector store still has their data indexed with that employee's old access level, queries will continue surfacing that data to users who should no longer see it.

The failure prevented: an employee's access to confidential projects is revoked but their project documents remain fully retrievable by their former account because the vector store was never updated.

**Caveat / contested:** Webhook-driven real-time sync is significantly more complex than batch re-indexing and requires upstream systems to support webhooks. If your source systems do not support webhooks, use a short re-sync interval (for example, hourly) with chunk-hash comparison to detect changes. This leaves a window of potential over-exposure between syncs.

**Sources:**
- [truto.one — Multi-tenant RAG data isolation: the 2026 enterprise architecture guide](https://truto.one/blog/how-to-architect-strict-data-isolation-in-multi-tenant-rag-pipelines/) (May 2026)
- [csoonline.com — Securing RAG pipelines in enterprise SaaS](https://www.csoonline.com/article/4163888/securing-rag-pipelines-in-enterprise-saas.html) (date unverified)
- [cheatsheetseries.owasp.org — RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) (no date listed)

**Confidence:** ✅ independently-corroborated (multiple independent publishers)

---

## Held pending fixes (not publish-ready)
- Ghost Vectors epoch-key-rotation mitigation: single Jun 2026 preprint, not yet independently replicated; no production implementation confirmed for covered databases ⚠ #pending-1
- OWASP RAG Security Cheat Sheet and christian-schneider.net article: no publish date found on the OWASP page; christian-schneider.net date (Feb 19, 2026) confirmed by Skeptic grader. OWASP date remains unresolved. ⚠ #pending-2

---

## CHANGELOG

### From technical entry (grading panel, 2026-07-09)
1. Skeptic KILL: Practice 1 — removed unsourced "50–70% or more of words" and "80–99% clinical reconstruction accuracy" figures. Only Ghost Vectors figures (25.5%/46.4%/100%) retained.
2. Skeptic KILL: Practice 3 — removed fabricated "95% of benign queries triggered cross-tenant leakage" statistic.
3. Skeptic KILL: Practice 7 — removed "organizations experiencing AI-related breaches were three times more likely to have lacked query-level access logging" statistic. Added single-vendor caveat for kiteworks as source.
4. Skeptic FIX: Practice 4 — added note that CVE-2025-32711 CVSS is a split score: Microsoft CNA = 9.3 CRITICAL, NIST = 7.5 HIGH. Added direct NVD link.
5. Skeptic FIX: Practice 1 — corrected OWASP LLM08 URL slug inconsistency noted.
6. Timekeeper FIX: Practice 1 — added `🕒 verify live` caveat to Ghost Vectors database scope.
7. Timekeeper FIX: Practice 5 — added "no date listed" annotation to aquilax.ai citation.
8. Timekeeper FIX: Practices 2, 4, 5, 7, 9 — added "no date listed" annotation to OWASP RAG Security Cheat Sheet citations.
9. Timekeeper FIX: Practice 4 — added direct NVD advisory URL for CVE-2025-32711.
10. Timekeeper FIX: Practices 4, 5, 6 — updated christian-schneider.net to "Feb 19, 2026."
11. Timekeeper FLAG: Practice 6 — added `🕒 verify live` to RADAR/SeCon-RAG citations.
12. Timekeeper FLAG: Practice 9 — noted csoonline.com article date is unverified.
13. Beginner KILL: Practice 2 — added pseudo-code example contrasting wrong (retrieve-then-filter) vs. right (filter-at-retrieval-time) patterns. (Applied in this beginner version.)
14. Beginner KILL: Practice 7 — added "Where to instrument" section with LangChain and LlamaIndex guidance. (Applied in this beginner version.)
15. Beginner FIX: Practice 9 — replaced "idempotently" with "safely even if it arrives more than once"; replaced "webhook" with "automatic notification sent by upstream systems when something changes." (Applied in this beginner version.)

### Re-leveling applied by rings-beginner-author (2026-07-09, from technical entry dated 2026-07-09)

**Jargon expanded on first use (grading FIX items):**
- HNSW: "the index structure used by most vector databases — lives in RAM during operation but persists to disk as files"
- Vec2Text: "a tool that reconstructs text from embeddings"
- WORM: "Write-Once-Read-Many — storage that cannot be edited after writing"

### Link-check gate (this file)
- 1 non-200 URL unlinked to plain text (nvd.nist.gov CVE-2025-32711 — 403/bot-protection; confirmed live via WebFetch Jul 2026). Citation retained.
- SIEM: "Security Information and Event Management — software that collects and alerts on logs, examples include Splunk, Microsoft Sentinel, and Datadog"
- FGAC: "Fine-Grained Access Control, meaning permissions enforced at the database engine level rather than only in application code"
- JWT: "JSON Web Token, a signed string that proves the user's identity and carries their permission claims"
- webhook: "automatic notification sent by one system to another when something changes"
- idempotent: replaced with "safe to process more than once" in context
- PII: "personally identifiable information"
- OWASP: "the Open Web Application Security Project, a widely-cited security standards body"
- OCR: "optical character recognition, software that reads text from images"
- MFA: "multi-factor authentication — requiring a second proof of identity beyond a password"
- HIPAA, GDPR, SOX: all given plain-language applicability guidance
- ePHI: "electronic protected health information"
- SDK: "software development kit — the code library you use to talk to the database"
- CVE/CVSS: CVE-2025-32711 given plain-language description of what the attacker could do

**Plain-language leads added (grading FIX items):**
- Practice 1: added "The core idea" opening before research details; added pointer to Practice 8 for deletion risk
- Practice 2: added explanation of why post-retrieval filtering is unsafe; added "the failure prevented" pattern
- Practice 3: added plain-language warning about "namespace" meaning; added guidance on what to look for in vendor docs
- Practice 4: added plain-language description of EchoLeak attack chain; called out AWS Textract/Comprehend directly in Do
- Practice 5: added "reduces risk but does not eliminate it" in Do before delimiter guidance; added "the failure prevented"
- Practice 6: added "the failure prevented"
- Practice 7: added plain-language regulation applicability; added "the failure prevented"
- Practice 8: added plain-language explanation of soft-delete vs. hard-delete; added "the failure prevented"
- Practice 9: added "the failure prevented"

**Context-preserving masking explained (grading FIX item):** Practice 1 now explains with the John Smith / [PERSON_1] example.

**Concrete WORM examples added (grading FIX item):** Practice 4 now lists AWS S3 Object Lock, Azure Blob immutable storage, Google Cloud Storage retention policy.

**Paper citations simplified for beginners (grading FIX items):** RADAR and SeCon-RAG arXiv IDs retained (they are in sources) but flagged as academic / not-yet-production rather than presented as actionable guidance.

**RAG pipeline concept introduced:** Added "What is a RAG pipeline?" section at top for readers completely new to the concept. Facts drawn only from the technical entry's implicit context.
