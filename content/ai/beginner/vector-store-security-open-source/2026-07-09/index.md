---
title: "Vector Store Security — Open-Source Self-Hosted (as of 09 Jul 2026)"
date: 2026-07-09
snapshot_date: 2026-07-09
topic: vector-store-security-open-source
track: beginner
audience: "people new to AI"
description: "Security best practices for self-hosted open-source vector databases (Chroma, Qdrant, Weaviate, Milvus) explained for people new to AI — covering dangerous auth defaults, TLS, Docker isolation, known CVEs (ChromaToast CVSS 10.0, Milvus CVSS 9.3), and patching."
content_type: "Best Practice"
categories: ["Vector Databases", "AI Security", "RAG Pipelines"]
tags: ["chroma", "qdrant", "weaviate", "milvus", "vector-database", "security", "access-control", "authentication", "tls", "rbac", "multi-tenancy", "cve", "self-hosted"]
last_refreshed: 2026-07-09
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-09"
grading_result: "0 fabrications; beginner re-level by rings-beginner-author"
---

<!-- This file lands at content/ai/beginner/vector-store-security-open-source/2026-07-09/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Vector Store Security — Open-Source Self-Hosted (as of 09 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **09 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## What is a vector database and why does this matter?

A **vector database** stores text (or images or audio) converted into lists of numbers called **embeddings**. AI apps — especially RAG pipelines — use these databases to find documents that are similar to a user's question. The four covered here (Chroma, Qdrant, Weaviate, Milvus) are popular open-source options you run on your own server. "Self-hosted" means you are responsible for securing them; there is no managed cloud service doing it for you.

A **RAG pipeline** (Retrieval-Augmented Generation) is the pattern where an AI searches your documents for relevant text and uses it to answer questions. The documents in the vector database often contain sensitive information: customer conversations, internal files, personal data. Leaving the database unsecured means handing all of that to anyone who can reach the server.

## How to read the labels

- ✅ **independently-corroborated** — 2+ independent publishers confirmed this
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: Turn on authentication before connecting any network — all four databases ship with logins disabled

⚠️ **WARNING — dangerous default**

**Do:** Treat every self-hosted Chroma, Qdrant, Weaviate, and Milvus instance as open to the world until you have explicitly enabled authentication. Before connecting any network interface, enable at minimum a static API key or token. Never bind to `0.0.0.0` (the address that means "accept connections from anywhere") before auth is configured.

**For Milvus specifically:** Enable authentication by setting `common.security.authorizationEnabled: true` in your `milvus.yaml` (or the equivalent environment variable `MILVUS_AUTH_ENABLED: true` in Docker deployments). Then **immediately change the default root password** — the default password is literally the word `Milvus`. 🕒 verify live. Change it with the Milvus SDK before doing anything else:

```python
from pymilvus import MilvusClient
client = MilvusClient(uri="http://localhost:19530", token="root:Milvus")
client.update_password(user_name="root", old_password="Milvus", new_password="<your-strong-password>")
```

**For Weaviate specifically:** Do **not** copy tutorial Docker Compose files that include `AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: 'true'` into production. In production, remove that line entirely or set it to `'false'`. The safe value is `'false'` (or simply absent, since `false` is the built-in default). Copy-pasted tutorial compose files are the most common way Weaviate ends up deployed with auth disabled.

**Why (beginner):** All four databases described here start without any login requirement. Anyone who can reach the port — including anyone on the same server, the same Docker network, or (if you expose a port) the entire internet — can read, write, delete, or poison every vector and document stored in the database. The data fed into a RAG pipeline is usually sensitive: customer conversations, internal documents, personal information. An open database hands all of that to the first person who runs a port scan.

Evidence of real-world harm: A survey conducted in April 2025 found 1,170 internet-accessible Chroma instances, of which 406 (roughly one-third) exposed data including personal information from Canva Creators and customer support chat logs from e-commerce companies. Chroma's own documentation states: "By default, Chroma does not require authentication. You must enable it manually."

The same unauthenticated-by-default posture applies to the others:
- **Qdrant** docs: "every interface on the host is reachable without a key or password" in self-hosted mode (in contrast to Qdrant Cloud, which is "always secure by default").
- **Milvus**: "By default, applications can connect to self-hosted Milvus without having to enter a username and password." The default root password is `Milvus`. 🕒 verify live — vendors can change security defaults without a major release.
- **Weaviate**: Anonymous access is not the coded default, but copy-pasted compose examples in tutorials frequently enable it with `AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: 'true'`. Remove this line or set to `'false'` in production.

**Sources:**
- [upguard.com — Open Chroma databases: AI attack surface](https://www.upguard.com/blog/open-chroma-databases-ai-attack-surface) (Dec 2025)
- [qdrant.tech — Secure Qdrant tutorial](https://qdrant.tech/documentation/tutorials-operations/secure-qdrant/) (vendor docs, fetched Jul 2026)
- milvus.io — Authenticate user access (https://milvus.io/docs/authenticate.md — bot-protected, confirmed live Jul 2026) (vendor docs, fetched Jul 2026)
- [docs.weaviate.io — Authentication configuration](https://docs.weaviate.io/deploy/configuration/authentication) (vendor docs, fetched Jul 2026)

**Confidence:** ✅ independently-corroborated (UpGuard independent research + four separate vendor doc confirmations of unauthenticated defaults)

---

## Practice 2: Encrypt traffic with TLS — use a reverse proxy if the database's own TLS is awkward

**Background terms for beginners:**
- **TLS** (Transport Layer Security) is the same encryption standard behind the padlock in your browser. It scrambles data while it travels across a network so eavesdroppers cannot read it.
- A **reverse proxy** is a program (such as nginx or Caddy) that sits in front of your database and handles TLS on its behalf. Caddy is free and obtains certificates automatically from Let's Encrypt.
- A **PEM file** is a text file that contains a TLS certificate or private key. You get one either by running `openssl req -x509 ...` (for testing only) or from a certificate provider like Let's Encrypt (for production).
- A **man-in-the-middle (MitM) attack** is when someone on the network intercepts your traffic and reads it before passing it along — possible when traffic is not encrypted.

**Do:** Encrypt all traffic between your application and the vector database using TLS 1.2 or 1.3. For Qdrant, set `QDRANT__SERVICE__ENABLE_TLS: "true"` with cert/key paths. For Milvus, set `tlsEnabled: true` in `milvus.yaml` and supply `server.pem`/`server.key`/`ca.pem`. For Weaviate, configure TLS at the reverse proxy layer (Weaviate's own TLS docs are sparse). For Chroma, prefer a reverse proxy (nginx or Caddy) for TLS termination rather than Chroma's built-in server, which carries a performance penalty.

If you have never set up TLS certificates before: for testing only, you can generate a self-signed certificate with `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.pem`. For production, obtain a certificate from Let's Encrypt or your cloud provider — do not use self-signed certificates in production (see Caveat below).

**Why (beginner):** Without TLS, an API key sent in a header travels across the network as plain text. Anyone who can observe traffic on the same network — another container, another virtual machine on the same server, anyone on a shared network — can capture the key and use it to authenticate as you. Qdrant's documentation states that when using API key authentication, TLS should also be enabled to protect the key from network sniffing and man-in-the-middle attacks.

**Caveat:** Chroma's cookbook notes that using certificates directly within Chroma's server has a measurable performance impact and that self-signed certificates are not recommended for production. The practical recommendation is TLS termination at nginx or Caddy in front of Chroma. For Qdrant, TLS can alternatively be terminated at a reverse proxy rather than inside Qdrant itself.

**Sources:**
- [qdrant.tech — Secure Qdrant tutorial](https://qdrant.tech/documentation/tutorials-operations/secure-qdrant/) (vendor docs, fetched Jul 2026)
- [cookbook.chromadb.dev — Chroma SSL certificate setup](https://cookbook.chromadb.dev/security/chroma-ssl-cert/) (third-party cookbook, fetched Jul 2026 — performance impact and self-signed caveat confirmed verbatim)
- milvus.io — Data security blog (https://milvus.io/blog/data-security.md — bot-protected, confirmed live Jul 2026) (vendor, fetched Jul 2026)

**Confidence:** 📄 vendor-documented (multiple vendor sources; SSL-proxy pattern corroborated by independent ChromaDB cookbook)

---

## Practice 3: Give each part of your app its own limited credential — never share one admin key everywhere

**Background terms for beginners:**
- **JWT** (JSON Web Token) is a signed string that proves identity and can carry permission claims — for example, "this credential is allowed to read from collection X but cannot write or delete."
- **RBAC** (Role-Based Access Control) is the practice of assigning named roles (like "read-only" or "admin") to users or services, then granting permissions to roles rather than to individual accounts.
- "Minting" a token just means creating one.

**Do:** Issue separate, minimally-scoped credentials to each service that touches the vector database. For Qdrant (v1.9+), enable JWT RBAC (`QDRANT__SERVICE__JWT_RBAC: "true"`) and create JWT tokens scoped to specific collections and operations (read-only `r` or read-write `rw`). Set a separate read-only key (`QDRANT__SERVICE__READ_ONLY_API_KEY`) for query-serving services. For Milvus, create named users and roles with `COLL_RO`/`COLL_RW`/`DB_ADMIN` privilege groups rather than sharing the root account. For Weaviate (v1.29+, generally available Feb 2025; 🕒 current stable is 1.38 — 1.29 is no longer in the supported version window), define custom RBAC roles through `AUTHORIZATION_RBAC_ENABLED: 'true'` and assign them per-user via the management API.

To check your Qdrant version: `curl http://localhost:6333/` — the response includes a `version` field.

**Why (beginner):** A single admin key shared across your data-loading pipeline, your search service, and your monitoring dashboard means one leaked credential compromises everything. Scoped credentials limit blast radius: a compromised read-only key can expose data but cannot corrupt or delete it.

**Caveat:** Qdrant's JWT RBAC requires version 1.9 or later — verify your running version. Milvus RBAC configuration syntax differs slightly across v2.4.x, v2.5.x, and v2.6.x branches; check the version-specific docs. Weaviate's built-in Admin list and RBAC cannot be used simultaneously — pick one scheme and stick to it.

**Sources:**
- [qdrant.tech — Data privacy RBAC article](https://qdrant.tech/articles/data-privacy/) (vendor docs, fetched Jul 2026)
- [qdrant.tech — Secure Qdrant tutorial](https://qdrant.tech/documentation/tutorials-operations/secure-qdrant/) (vendor docs, fetched Jul 2026)
- milvus.io — RBAC documentation (https://milvus.io/docs/rbac.md — bot-protected, confirmed live Jul 2026) (vendor docs, fetched Jul 2026)
- milvus.io — Milvus RBAC explained (https://milvus.io/blog/milvus-rbac-explained-secure-your-vector-database-with-role-based-access-control.md — bot-protected, confirmed live Jul 2026) (vendor blog, fetched Jul 2026)
- [docs.weaviate.io — Configuring RBAC](https://docs.weaviate.io/deploy/configuration/configuring-rbac) (vendor docs, fetched Jul 2026)

**Confidence:** 📄 vendor-documented

---

## Practice 4: Put the database on a private Docker network — never publish its port to the internet

**Background terms for beginners:**
- **Docker** is a tool that runs software inside lightweight isolated boxes called containers.
- A **Docker network** is a virtual local network that connects containers together. Containers on the same Docker network can talk to each other; containers on different networks cannot.
- `0.0.0.0` is an address that means "accept connections from every network interface" — including the public internet if your server has a public IP.
- `127.0.0.1` is the loopback address, meaning "this machine only."
- `--network=host` is a Docker option that removes all network isolation — the container shares the host's network directly. Quick-start guides often include this for convenience; do not use it in production.

**Do:** In Docker Compose, place your vector database container on an internal network shared only with the services that need to reach it. Do not use `ports:` mappings that bind to `0.0.0.0` (the host's all-interfaces address). If you must expose a port for an admin UI, bind it to `127.0.0.1` only. Do not use `--network=host` in production.

Example (Qdrant in Compose):
```yaml
services:
  qdrant:
    image: qdrant/qdrant
    networks:
      - internal
    # No "ports:" block — the app service reaches qdrant via the internal network name

  app:
    networks:
      - internal
      - external   # app needs internet access for embedding API calls

networks:
  internal:
    driver: bridge
    internal: true   # prevents external ingress AND egress for containers on this network only
  external:
    driver: bridge
```

⚠️ **WARNING:** Setting `internal: true` on a Docker network **also blocks outbound internet calls** from all containers on that network — including your vector database container if it ever needs to pull model weights or reach an external embedding API. This can silently break your pipeline in a confusing way. Use a **separate** network (the `external` network in the example above) for components that need internet access. Do not put your app service on the `internal` network alone if it needs to reach external APIs.

**Why (beginner):** Docker's default bridge network exposes all container ports to other containers on that bridge. If you also add a `ports: - "6333:6333"` mapping, the port becomes reachable from the host machine and potentially from the internet if no firewall rule blocks it. Many developers add that mapping "just to test something" and forget to remove it. Using `internal: true` on the vector database's network means no outside entity can reach it directly through Docker networking.

Quick-start guides for all four databases frequently include exposed ports and `--network=host` for convenience — treat these as development-only configurations.

**Sources:**
- [qdrant.tech — Secure Qdrant tutorial](https://qdrant.tech/documentation/tutorials-operations/secure-qdrant/) (vendor docs, network binding guidance)
- [docs.docker.com — Enhanced container isolation](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/) (vendor docs, fetched Jul 2026)
- [upguard.com — Open Chroma databases: AI attack surface](https://www.upguard.com/blog/open-chroma-databases-ai-attack-surface) (Dec 2025 — documented the consequence of exposed ports)

**Confidence:** ✅ independently-corroborated (vendor network-isolation docs + independent UpGuard research documenting real-world exposure)

---

## Practice 5: Patch Milvus immediately if your version is below 2.4.24, 2.5.21, or 2.6.5 — CVE-2025-64513 lets anyone in without a password

**What is a CVE and CVSS?** A **CVE** (Common Vulnerabilities and Exposures) is a numbered security flaw in software — a unique ID so everyone refers to the same bug. A **CVSS** score runs from 0 to 10; 10 means the most critical possible vulnerability.

⚠️ **WARNING — active CVE, CVSS 9.3 CRITICAL**

**Do:** First, check your Milvus version. In a Docker deployment run one of these commands:

```bash
docker inspect <container-name> | grep -i version
```

or call the health endpoint:

```bash
curl http://localhost:9091/api/v1/health
```

The response includes the running version.

If your version falls below 2.4.24, 2.5.21, or 2.6.5, upgrade immediately. As of Jul 2026, Milvus 2.6.x is at v2.6.19 (released Jul 1 2026) — upgrade to the latest patch in your branch, not just the minimum fixed version. 🕒 verify live for the current latest.

If you **cannot upgrade immediately**, strip all `sourceID` headers from inbound requests at your load balancer or API gateway before they reach the Milvus Proxy. If you are running Milvus without a load balancer (for example, a single-server Docker Compose setup), the only safe option is to **upgrade or take the service offline** — the bypass occurs before authentication, so having authentication enabled does not protect you.

**Why (beginner):** CVE-2025-64513, published November 2025 (CVSS 9.3 Critical), is an authentication bypass in the Milvus Proxy. The Proxy checks an incoming header called `sourceID` to decide whether a request is from a trusted internal part of Milvus. An attacker who sends the right value in that header is treated as a trusted internal member — bypassing all authentication and RBAC controls, regardless of whether authentication is enabled. The attacker gains full admin access: they can read, change, or delete all your vectors, and manage all databases and collections.

The affected range is broad: the security advisory lists all versions from approximately 0.10.4 onward as affected, with patches at 2.4.24, 2.5.21, and 2.6.5. **The advisory does not address Milvus 3.0.x** (beta as of May 2026) — neither safe nor affected can be concluded from the advisory for 3.0.x. 🕒 verify live before treating 3.0.x as a safe migration path.

**Sources:**
- [github.com/advisories — GHSA-mhjq-8c7m-3f7p (CVE-2025-64513)](https://github.com/advisories/GHSA-mhjq-8c7m-3f7p) (published Nov 2025)
- nvd.nist.gov — CVE-2025-64513 (https://nvd.nist.gov/vuln/detail/CVE-2025-64513 — bot-protected, confirmed live Jul 2026) (NVD, fetched Jul 2026; CVSS 9.3 confirmed)
- [securityonline.info — CVE-2025-64513 critical authentication bypass in Milvus Proxy](https://securityonline.info/critical-authentication-bypass-vulnerability-found-in-milvus-proxy-cve-2025-64513-cvss-9-3/) (Nov 2025)
- [github.com/milvus-io/milvus — releases](https://github.com/milvus-io/milvus/releases) (fetched Jul 2026; v2.6.19 latest confirmed)

**Confidence:** ✅ independently-corroborated (GitHub Advisory Database + NVD + independent security news coverage)

---

## Practice 6: Do not expose ChromaDB's Python server to any untrusted network — CVE-2026-45829 (ChromaToast) lets an attacker take over the server, and there is no confirmed patch as of 09 Jul 2026

⚠️ **WARNING — unpatched critical remote code execution, CVSS 10.0 CRITICAL**

**What does "remote code execution" mean?** It means an attacker can run their own programs on your server — not just read data, but fully control the machine: install malware, steal API keys stored in environment variables, delete everything.

**Why this bug is especially dangerous:** ChromaDB's Python server has a feature called `trust_remote_code`. When asked to load certain AI models, it downloads and executes code from the internet. CVE-2026-45829 abuses this: an attacker sends a specially crafted HTTP POST to the collection creation endpoint that references a malicious model. ChromaDB loads the model code **before** it checks who sent the request, so the attacker's code runs on the server before authentication ever happens.

**Do:** If you run ChromaDB's Python FastAPI server (any version from 1.0.0 onward), restrict network access to the ChromaDB port to a strictly trusted internal network immediately. Do **not** expose the port to the public internet under any circumstances, and do **not** treat authentication as a compensating control — the attack runs **before** auth is checked.

**NVD (fetched 09 Jul 2026) lists the affected range as all versions 1.0.0 and later, with no upper bound and no confirmed patched version.** Multiple independent sources (BleepingComputer, Hadrian, SecurityWeek) confirm that ChromaDB 1.5.9 (released May 5 2026) remains vulnerable. 🕒 Check the NVD record and ChromaDB's GitHub releases regularly for patch availability.

Consider migrating to the Rust-based ChromaDB server implementation, which is stated to be unaffected. This is a significant undertaking — verify the claim in the official security advisory before relying on it, and consult the ChromaDB migration documentation before attempting it.

The HiddenLayer security team found approximately 73% of internet-exposed ChromaDB instances were running vulnerable versions. The ChromaDB development team had not responded to multiple disclosure attempts as of the publication date. The vulnerability was first reported in November 2025 and re-reported in February 2026.

**Sources:**
- [securityweek.com — Unpatched ChromaDB vulnerability can lead to server takeover](https://www.securityweek.com/unpatched-chromadb-vulnerability-can-lead-to-server-takeover/) (fetched Jul 2026)
- [labs.cloudsecurityalliance.org — CSA research note: ChromaDB RCE](https://labs.cloudsecurityalliance.org/research/csa-research-note-chromadb-rce-ai-vector-database-20260520-c/) (May 2026)
- [thecyberexpress.com — CVE-2026-45829 ChromaToast](https://thecyberexpress.com/cve-2026-45829-chromatoast-chromadb/) (May 2026)
- nvd.nist.gov — CVE-2026-45829 (https://nvd.nist.gov/vuln/detail/CVE-2026-45829 — bot-protected, confirmed live Jul 2026) (NVD, fetched Jul 2026; CVSS 10.0, "version 1.0.0 or later" with no upper bound)
- [bleepingcomputer.com — Max-severity flaw in ChromaDB for AI apps allows server hijacking](https://www.bleepingcomputer.com/news/security/max-severity-flaw-in-chromadb-for-ai-apps-allows-server-hijacking/) (fetched Jul 2026; 1.5.9 confirmed vulnerable)
- [hadrian.io — CVE-2026-45829: ChromaDB Python server pre-auth RCE analysis](https://hadrian.io/blog/cve-2026-45829----chromadb-python-server-hands-you-rce-before-it-asks-who-you-are) (fetched Jul 2026)

**Confidence:** ✅ independently-corroborated (SecurityWeek + Cloud Security Alliance + The Cyber Express + NVD — multiple independent publishers; NVD confirms CVSS 10.0 and open-ended affected range)

---

## Practice 7: Upgrade Weaviate to 1.33.4+ (CVE-2025-67818) and 1.38.0+ (CVE-2026-59093) to close a file-write and a privilege-escalation hole

⚠️ **WARNING — two separate CVEs requiring version upgrades**

**Do:** Check your Weaviate version. In a typical Docker deployment:

```bash
docker inspect <container-name> | grep -i image
```

or look at the container image tag. (Note: `weaviate --version` will not work in a standard Docker deployment — use the Docker inspect method above.)

If you are on Weaviate below 1.33.4, upgrade to close CVE-2025-67818 (a file-writing flaw via backup restore). If you are below 1.38.0, also upgrade to close CVE-2026-59093 (a privilege-escalation flaw). **As of Jul 2026, the currently supported Weaviate versions are 1.36, 1.37, and 1.38** — anyone on 1.33.x has already left the support window; upgrade to 1.38.x.

If you cannot upgrade immediately:
- For CVE-2025-67818: disable backup modules by removing all `backup*` entries from the `enabled_modules` flag.
- For CVE-2025-67819 (a companion path-traversal flaw in Shard Movement): set `REPLICA_MOVEMENT_ENABLED: false`.

**Why (beginner):**

- **CVE-2025-67818** (CVSS score contested — 7.2 per CISA-ADP, 8.7 HIGH per GitHub Advisory Database, "Medium" per Weaviate blog; NVD final score not assigned as of 09 Jul 2026 🕒 verify live): An attacker who can insert data into Weaviate can craft an object name that contains path-traversal characters (for example, `../../etc/crontab` — where `..` means "go up one folder"). When a backup containing that object is restored, Weaviate writes the file to the wrong location, letting the attacker create or overwrite any file the Weaviate process can reach on the server.

- **CVE-2026-59093** (CVSS 8.8 HIGH per NVD CVSS 3.1 / 8.7 HIGH per CVSS 4.0, published Jul 2, 2026): Weaviate does not verify that a user assigning an RBAC role actually holds the permissions granted by that role. A user with only the `assign_and_revoke_users` permission can assign the built-in `admin` role to themselves, achieving full database admin access without originally having it.

**Note on CVE numbers in the mitigation section:** CVE-2025-67818 and CVE-2025-67819 are two related path-traversal flaws documented in the same Weaviate November 2025 security release. CVE-2026-59093 is a separate privilege-escalation flaw from July 2026. Three separate CVE numbers; three separate problems.

**Sources:**
- [weaviate.io — Security release November 2025](https://weaviate.io/blog/weaviate-security-release-november-2025) (Nov 2025; CVE-2025-67818 details + backup module mitigation)
- nvd.nist.gov — CVE-2025-67818 (https://nvd.nist.gov/vuln/detail/CVE-2025-67818 — bot-protected, confirmed live Jul 2026) (published Dec 2025, fetched Jul 2026; CISA-ADP score 7.2)
- [github.com/advisories — GHSA-7v39-2hx7-7c43 (CVE-2025-67818)](https://github.com/advisories/GHSA-7v39-2hx7-7c43) (GitHub Advisory; score 8.7 HIGH)
- nvd.nist.gov — CVE-2026-59093 (https://nvd.nist.gov/vuln/detail/CVE-2026-59093 — bot-protected, confirmed live Jul 2026) (published Jul 2, 2026, fetched Jul 2026; CVSS 8.8/8.7 HIGH confirmed)
- [docs.weaviate.io — Release notes](https://docs.weaviate.io/weaviate/release-notes) (fetched Jul 2026; 1.38.x confirmed as current stable)

**Confidence:** ✅ independently-corroborated (vendor security release + NVD + GitHub Advisory for both CVEs; note CVSS score disagreement on CVE-2025-67818)

---

## Practice 8: Keep different customers' data physically separated — never rely on your app code alone to prevent one customer seeing another's data

**Background terms for beginners:**
- **Multi-tenant** means one system serves multiple customers ("tenants"), each of whom should only see their own data.
- An **HNSW index** (Hierarchical Navigable Small World) is the internal data structure most vector databases use to store and search embeddings. Each index lives in memory (RAM). If you create one per customer, each one occupies RAM even when that customer is not active.
- A **metadata filter** is a condition you add to a search query, like "only return results where `tenant_id == 'customer_A'`."
- An **API gateway** is a service that sits in front of your database and enforces rules before requests get through.

**Do:** Choose one of two architectural patterns and enforce it consistently:

- **Silo (one collection per customer):** Create a separate collection (Qdrant/Weaviate/Milvus) or database (Chroma) per customer. Issue credentials scoped exclusively to that collection. This gives complete data separation at the cost of more infrastructure.
- **Pool (shared collection with filters):** Store all customers in one collection, tag every document chunk with a `tenant_id` metadata field, and enforce a `tenant_id == <current_tenant>` filter on every query. Use your API gateway to extract the customer identity from a verified JWT and inject the filter — never let application code manually append the filter, because a missing filter means one customer sees another customer's data.

In both patterns, enforcement must happen at the database or gateway layer. AI models are non-deterministic and susceptible to prompt injection; system-prompt instructions like "only discuss this customer's data" are not a security control.

**Why (beginner):** If two customers' documents are stored in the same vector database without isolation, a retrieval query from Customer A could pull up Customer B's documents — a data breach. A single code path that forgets the tenant filter is a breach. The Silo pattern avoids filter-omission bugs but scales poorly — 500 customers means 500 HNSW indexes, each consuming RAM even when idle.

**Caveat:** The Pool pattern with metadata filtering requires absolute discipline in application logic to ensure cross-tenant queries are impossible. Modern enterprise architectures often favor Pool combined with fine-grained access control enforced at the database engine level, not purely at the application layer.

**Sources:**
- [truto.one — Multi-tenant RAG data isolation: the 2026 enterprise architecture guide](https://truto.one/blog/how-to-architect-strict-data-isolation-in-multi-tenant-rag-pipelines/) (May 2026)
- [qdrant.tech — Data privacy RBAC + JWT article](https://qdrant.tech/articles/data-privacy/) (vendor docs, fetched Jul 2026)

**Confidence:** ✅ independently-corroborated (independent architectural guide + Qdrant vendor docs)

---

## Practice 9: Protect data on disk with OS-level encryption — these databases do not encrypt stored files themselves

**Do:** Because none of the four databases (Chroma, Qdrant, Weaviate, Milvus) encrypt data at rest in their open-source self-hosted form, protect data at the infrastructure layer using your operating system's or cloud provider's disk encryption. On Linux, this means **LUKS** (Linux Unified Key Setup — a standard tool that encrypts an entire disk partition). On AWS, enable encryption on the EBS volume (Elastic Block Store — the disk attached to your server). On GCP or Azure, enable encrypted persistent disks for the directories where the database stores its index files.

In plain terms: use your server's disk encryption to protect the folder where the database keeps its files.

**Why (beginner):** Encryption at rest protects data if someone physically removes the disk or gains access to a backup snapshot. Without it, anyone with filesystem access to the server can copy the raw index files and read the data offline without going through the database's authentication layer.

**Caveat:** This practice is documented by absence of a feature rather than a positive claim — verify each project's current release notes before assuming no change. The claim that Chroma's underlying database layer has no encryption roadmap comes from a single community GitHub discussion; treat as thin specifically for Chroma's timeline. For Weaviate Cloud and Chroma Cloud managed services, encryption at rest is provided by the managed offering — this practice applies only to self-hosted deployments.

**Sources:**
- [cookbook.chromadb.dev — Security](https://cookbook.chromadb.dev/security/) (third-party, fetched Jul 2026)
- milvus.io — Data security blog (https://milvus.io/blog/data-security.md — bot-protected, confirmed live Jul 2026) (vendor, fetched Jul 2026; TLS only, silent on at-rest encryption)

**Confidence:** thin — verified that none of these databases document built-in at-rest encryption for self-hosted use; verify each project's current release notes before assuming no change

---

## Practice 10: Subscribe to security alerts for each project — all four have had critical vulnerabilities in the past year

**Do:** Set up GitHub watch notifications on these repositories so you hear about new CVEs:

1. Go to the repository page in a browser.
2. Click **Watch** (top right area of the page).
3. Choose **Custom**.
4. Check **Security alerts only**.
5. Click **Apply**.

Repositories to watch:
- [github.com/chroma-core/chroma](https://github.com/chroma-core/chroma) — CVE-2026-45829 unpatched as of 09 Jul 2026
- [github.com/qdrant/qdrant](https://github.com/qdrant/qdrant) — active development; check releases
- [github.com/weaviate/weaviate](https://github.com/weaviate/weaviate) — CVE-2025-67818 (Dec 2025), CVE-2026-59093 (Jul 2026)
- [github.com/milvus-io/milvus](https://github.com/milvus-io/milvus) — CVE-2025-64513 (Nov 2025, CVSS 9.3)

All four have had high-severity or critical issues in the 8-month window between November 2025 and July 2026. These are production data-layer components for AI pipelines that handle sensitive documents; they must be included in your standard vulnerability management program.

**Why (beginner):** Vector databases are new enough that security review is still catching up with their feature surface. The same properties that make them useful for AI — they load model code, process complex embeddings, handle multi-tenant queries — also create new attack surfaces. Four separate critical-to-high CVEs in under a year signals that this software class requires active patching attention.

**Caveat:** 🕒 Release cadences vary: Milvus and Weaviate release frequently (multiple times per month in 2026); Chroma's 1.5.9 release appeared in May 2026 but the ChromaToast vulnerability remained unpatched. A monitoring subscription only helps if you act on alerts within a documented time window (for example, "critical CVEs patched within 7 days").

**Sources:**
- [github.com/advisories — GHSA-mhjq-8c7m-3f7p (Milvus CVE-2025-64513)](https://github.com/advisories/GHSA-mhjq-8c7m-3f7p) (Nov 2025)
- [weaviate.io — Security release November 2025](https://weaviate.io/blog/weaviate-security-release-november-2025) (Nov 2025)
- [labs.cloudsecurityalliance.org — ChromaToast CVE-2026-45829](https://labs.cloudsecurityalliance.org/research/csa-research-note-chromadb-rce-ai-vector-database-20260520-c/) (May 2026)
- nvd.nist.gov — CVE-2026-59093 (https://nvd.nist.gov/vuln/detail/CVE-2026-59093 — bot-protected, confirmed live Jul 2026) (Jul 2026)

**Confidence:** ✅ independently-corroborated (four independent sources documenting separate CVEs across four vendors)

---

## Held pending fixes (not publish-ready)

- Chroma at-rest encryption roadmap claim (DuckDB no encryption plans): sourced from a single GitHub discussion — needs a second source or stays `thin`. ⚠ #pending-1

---

## CHANGELOG

### From the technical entry (grading panel corrections applied before this beginner re-level)
1. Beginner KILL: Practice 1 Milvus — added explicit auth enablement steps (`MILVUS_AUTH_ENABLED: true`, SDK password-change snippet). Previously the danger was named but the fix was not shown.
2. Beginner KILL: Practice 1 Weaviate — stated explicitly that `AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED` must be set to `'false'` or removed. Previously the dangerous setting was identified but the correct production value was not given.
3. Timekeeper KILL: CVE-2026-45829 ChromaToast — changed "1.0.0–1.5.8" (closed range) to "all versions 1.0.0 and later with no confirmed patched version" per NVD record fetched Jul 2026. 1.5.9 confirmed vulnerable by BleepingComputer and Hadrian.
4. Timekeeper KILL: CVE-2026-45829 — added explicit CVSS 10.0 CRITICAL score (NVD confirmed). Previously stated only "CVSS Critical" without a number.
5. Timekeeper FIX: CVE-2026-45829 — sharpened patch-status caveat: "1.5.9 confirmed still vulnerable as of 09 Jul 2026" instead of "verify current patch status."
6. Skeptic KILL: Practice 8 (multi-tenancy) — removed "95% of benign queries triggered cross-tenant leakage" statistic. Not present on truto.one (the cited source) or any other fetched source. Fabricated stat.
7. Skeptic FIX: CVE-2026-59093 CVSS — updated from "0 (pending)" to "8.8 HIGH (CVSS 3.1) / 8.7 HIGH (CVSS 4.0) per NVD" (published Jul 2, 2026). Replaced low-authority akaoma.com tracker with NVD as primary cite.
8. Timekeeper FIX: CVE-2025-64513 Milvus — added note that GHSA advisory does not address 3.0.x (neither safe nor affected confirmed). Added mention of current latest v2.6.19 (released Jul 1 2026); directed readers to upgrade to latest patch, not just the minimum fixed version.
9. Timekeeper FIX: CVE-2025-67818 Weaviate — flagged CVSS score disagreement (CISA-ADP 7.2 vs GitHub Advisory 8.7 vs Weaviate blog "Medium"; NVD final score not assigned). Added `🕒 verify live`.
10. Timekeeper FIX: Weaviate upgrade path — added note that 1.33.x is outside the current supported version window (1.36/1.37/1.38 supported); directed readers to 1.38.x.
11. Timekeeper FIX: Weaviate RBAC note — added "1.29 is no longer in the supported version window; current stable is 1.38."
12. Skeptic FIX: Practice 2 TLS — removed quotation marks around Qdrant TLS warning (not verbatim on cited page); rephrased as paraphrase.
13. Skeptic FLAG: CVE-2025-64513 Milvus affected range — added note that the true lower bound per the advisory is approximately ≥0.10.4; the "2.4.0" threshold in the advisory reflects the minimum supported Milvus series, not the actual first-affected version.
14. Beginner KILL: Practice 4 Docker — added ⚠️ WARNING that `internal: true` also blocks outbound internet calls; added two-network compose example to show how to separate the vector DB's internal network from the app's external network.
15. Beginner KILL: Practice 5 Milvus CVE — added `docker inspect` and health-check API command to check running Milvus version. Added explicit fallback for users without a load balancer: "upgrade or take the service offline."
16. Timekeeper FIX: Added `🕒 verify live` to Milvus default root password "Milvus" — vendor can change security defaults without a major release.
17. Beginner FLAG: Practice 7 Weaviate — clarified version-check method for Docker deployments (`docker inspect` rather than `weaviate --version` which won't work in containers).
18. Timekeeper FLAG: Held-pending-3 (ChromaDB 1.5.9 patch status) promoted to confirmed finding in the main practice text (KILL applied above).

### Beginner re-level (this file) — re-leveled from the 2026-07-09 technical entry; facts unchanged
Applied the following findings from the beginner grading panel (`## open-source.md` section):

- **[KILL] Practice 1 (Milvus auth):** Already fixed in technical entry; preserved SDK snippet and explicit env-var instruction.
- **[KILL] Practice 1 (Weaviate anonymous access):** Already fixed in technical entry; preserved `'false'` instruction.
- **[FIX] Practice 2 (TLS):** Added beginner glossary for TLS, PEM files, reverse proxy (nginx/Caddy), and MitM attacks. Added `openssl` command for generating a test certificate with note that self-signed is not for production.
- **[FIX] Practice 3 (scoped credentials):** Defined JWT, RBAC, and "minting" tokens on first use. Added `curl http://localhost:6333/` version check command.
- **[KILL] Practice 4 (Docker `internal: true`):** Already fixed in technical entry; warning is preserved and strengthened with plain-language explanation.
- **[FIX] Practice 4 (--network=host):** Added plain-language explanation of what `--network=host` does and why it is dangerous.
- **[KILL] Practice 5 (Milvus CVE version check):** Already fixed in technical entry; both version-check commands preserved and highlighted.
- **[FIX] Practice 5 (load balancer assumption):** Explicit fallback instruction for users without a load balancer preserved from technical entry.
- **[FIX] Practice 6 (ChromaDB Rust migration):** Added note that migrating to the Rust server is a significant undertaking requiring consultation with migration documentation.
- **[FLAG] Practice 6 (trust_remote_code):** Added plain-language explanation of the `trust_remote_code` mechanism and how the attack abuses it.
- **[FIX] Practice 7 (Weaviate version check):** Corrected to use `docker inspect` rather than `weaviate --version`; noted why the latter does not work.
- **[FLAG] Practice 7 (CVE number confusion):** Added clarifying note explaining that CVE-2025-67818, CVE-2025-67819, and CVE-2026-59093 are three separate issues.
- **[FIX] Practice 8 (multi-tenancy jargon):** Defined HNSW index (and that it lives in RAM), metadata filter, API gateway, and multi-tenant on first use. Removed "FGAC" / "JWT-scoped access" jargon; replaced with plain language.
- **[FIX] Practice 9 (encryption at rest):** Defined LUKS and EBS; added plain-language summary ("use your server's disk encryption").
- **[FLAG] Practice 10 (GitHub watch steps):** Added numbered step-by-step for how to watch security alerts only on a GitHub repository.
- Added "What is a vector database and why does this matter?" introduction section for readers who are completely new to the topic.
- Added CVE / CVSS definitions on first use (Practice 5).

### Link-check gate (this file)
- 8 non-200 URLs unlinked to plain text (4 × milvus.io, 4 × nvd.nist.gov — all 403/bot-protection; confirmed live via WebFetch Jul 2026). Citations retained.
