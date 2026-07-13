# AI Agent Memory and State Management — LangChain / LangGraph (as of 07 Jul 2026)

> How to manage memory and persistent state in LangChain agents and LangGraph graphs — covering checkpointers, cross-thread stores, deprecated memory APIs, LangMem, retrieval-augmented memory, state schema design, and production pitfalls — accurate as of July 2026.


<!-- This file lands at content/ai/best-practices/ai-agent-memory-and-state-langchain/2026-07-07/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag. -->

# AI Agent Memory and State Management — LangChain / LangGraph (as of 07 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **07 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

> **Prerequisites:** This entry assumes familiarity with Python, pip, and database concepts (SQL, connection strings). If you are brand new to AI agents, start with the framework-agnostic memory entry first. In LangGraph, an agent is built as a **graph** — a set of steps (nodes) connected by transitions (edges). LangGraph saves ("checkpoints") the state of this graph automatically at every node transition so conversations can survive crashes and support human-in-the-loop pauses.

---

## Practice: Match your checkpointer to your deployment tier (InMemorySaver → SqliteSaver → PostgresSaver)

**Do:** Use `InMemorySaver` only in tests and demos; use `SqliteSaver` / `AsyncSqliteSaver` for single-process local development; use `PostgresSaver` / `AsyncPostgresSaver` for any production multi-worker service.

When creating a Postgres connection manually, you **must** set `autocommit=True` and `row_factory=dict_row` or the checkpointer silently breaks with no error:

```python
import psycopg
from langgraph.checkpoint.postgres import PostgresSaver

conn = psycopg.connect(
    "postgresql://user:pass@host/db",
    autocommit=True,          # REQUIRED
    row_factory=psycopg.rows.dict_row,  # REQUIRED
)
checkpointer = PostgresSaver(conn)
```

Note that LangGraph v0.2 split checkpointers into separate packages (`langgraph-checkpoint-sqlite`, `langgraph-checkpoint-postgres`). If you are still importing from the monolithic `langgraph` package you may be running older, unpatched code.

🕒 **verify live** — `langgraph-checkpoint-postgres` was at **3.1.0** (released 2026-05-12, confirmed PyPI 2026-07-07); `langgraph-checkpoint-sqlite` was at 3.1.0 (released 2026-05-12). Check [pypi.org/project/langgraph-checkpoint-postgres](https://pypi.org/project/langgraph-checkpoint-postgres/) before pinning.

**Why:** LangGraph checkpoints the entire graph state at every step so a conversation can survive crashes, support human-in-the-loop pauses, and allow time-travel debugging. `InMemorySaver` vanishes when the process exits. `SqliteSaver` is file-based and fine for one process but locks under concurrent writes. `PostgresSaver` is designed for multi-worker deployments — it uses connection pooling, pipeline-mode writes, and cursor-based pagination for efficient history reads.

**Sources:** [www.langchain.com/blog/langgraph-v0-2](https://www.langchain.com/blog/langgraph-v0-2) (2024) · [redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) (2025-03-28, updated 2026-06-01) · [pypi.org/project/langgraph-checkpoint-postgres](https://pypi.org/project/langgraph-checkpoint-postgres/) (confirmed 2026-07-07)

**Confidence:** independently-corroborated

---

## Practice: Use `thread_id` for session scope; use `user_id` + a BaseStore for cross-session scope — never confuse the two

**Do:** Pass `{"configurable": {"thread_id": "<session-id>"}}` as the `config` argument to scope the checkpointer to one conversation:

```python
result = graph.invoke(
    {"messages": [HumanMessage(content="Hello")]},
    config={"configurable": {"thread_id": "user-abc-session-1"}}
)
```

For facts you want to survive into *future* sessions (preferences, user profile data), write them explicitly to a `BaseStore` (InMemoryStore / PostgresStore / RedisStore) under a `("memories", user_id)` namespace.

**Why:** The checkpointer and the store are two separate systems. The checkpointer holds the running state of one thread; when a user starts a new thread (new session) that history is not automatically carried over. The store is explicitly keyed by user identity, not thread identity. If you store user preferences in the checkpointer under `thread_id`, a returning user with a new session will get a blank slate.

**Caveat:** The `InMemoryStore` still loses data on process restart — swap it for `PostgresStore`, `RedisStore`, or `MongoDBStore` before going to production.

**Sources:** [focused.io/lab/persistent-agent-memory-in-langgraph](https://focused.io/lab/persistent-agent-memory-in-langgraph) (Focused.io) · [atlan.com/know/long-term-memory-langchain-agents](https://atlan.com/know/long-term-memory-langchain-agents/) (Atlan) · [redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) (2025-03-28, updated 2026-06-01)

**Confidence:** independently-corroborated

---

## Practice: Stop using ConversationBufferMemory and ConversationSummaryMemory — migrate to LangGraph checkpointing

**Do:** If your codebase imports `ConversationBufferMemory`, `ConversationSummaryMemory`, or `RunnableWithMessageHistory` from `langchain`, replace them with a LangGraph checkpointer. Example minimal migration:

```python
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver.from_conn_string(":memory:")  # swap for PostgresSaver in prod
agent = create_react_agent(model, tools, checkpointer=checkpointer)
```

For pure LCEL chains that are not graphs, consider a framework-independent memory layer or a simple message-history list you manage yourself.

**Why:** `ConversationBufferMemory` was deprecated at LangChain v0.3.1 and `RunnableWithMessageHistory` was deprecated in v0.3. As of LangChain 1.x (current: 1.3.11, June 2026), both classes still exist in `langchain_classic` for backwards compatibility but are not maintained. Removal is planned for v2.0.0 — 🕒 verify live. They were designed before the modern Chat Model API existed, cannot work reliably with tool-calling agents, and store state only in process memory.

**Caveat / contested:** One independent source (db0.ai) argues that coupling memory to *any* framework layer — including LangGraph — creates fragility when frameworks redesign themselves (as already happened twice). Developers with non-LangGraph LCEL pipelines are largely left without a first-party migration target. If you are not using LangGraph, you may need to manage message history manually or use a framework-agnostic store.

**Sources:** [atlan.com/know/long-term-memory-langchain-agents](https://atlan.com/know/long-term-memory-langchain-agents/) (Atlan) · [db0.ai/blog/langchain-memory-deprecated](https://db0.ai/blog/langchain-memory-deprecated) (independent) · [pypi.org/project/langchain](https://pypi.org/project/langchain) (confirmed current 1.3.11, 2026-06-22, PyPI 2026-07-07) · [reference.langchain.com/python/langchain-classic/memory/buffer/ConversationBufferMemory](https://reference.langchain.com/python/langchain-classic/memory/buffer/ConversationBufferMemory) (LangChain reference docs, confirmed 2026-07-07)

**Confidence:** independently-corroborated

---

## Practice: Update LangGraph checkpointer packages immediately — CVEs disclosed in 2025-2026 allow RCE

⚠️ **WARNING — Active security vulnerabilities.** Four CVEs affect self-hosted LangGraph deployments. Before checking if you are vulnerable, run:

```bash
pip show langgraph langgraph-checkpoint-sqlite langgraph-checkpoint
```

To upgrade Python packages:

```bash
pip install --upgrade langgraph langgraph-checkpoint-sqlite langgraph-checkpoint
```

Then set in your `.env` file or shell environment:

```
LANGGRAPH_STRICT_MSGPACK=true
```

**CVEs and affected packages (Python/pip ecosystem unless noted):**

- **CVE-2025-67644** — SQL injection in `SqliteSaver.list()` via user-controlled filter parameters. Fix: `langgraph-checkpoint-sqlite >= 3.0.1`. 🕒 current: 3.1.0 (2026-05-12).
- **CVE-2026-28277** — Unsafe msgpack deserialization chaining with the SQLite SQLi for RCE. Fix: `langgraph >= 1.0.10` (minimum floor; current: **1.2.7**, released 2026-06-30 — upgrade to current). Upgrading `langgraph >= 1.0.10` transitively upgrades `langgraph-checkpoint >= 3.0.0` as a dependency; you do not need to pin `langgraph-checkpoint` separately unless you have a pinned transitive dependency.
- **CVE-2025-64439** (CVSS 7.4) — RCE via `JsonPlusSerializer` in `langgraph-checkpoint < 3.0.0`. Fix: upgrade `langgraph >= 1.0.10` as above (pulls in a patched `langgraph-checkpoint`).
- **CVE-2026-27022** — SQL injection in the **JavaScript/npm** package `@langchain/langgraph-checkpoint-redis`. Fix: `npm install @langchain/langgraph-checkpoint-redis@>=1.0.2`. **This CVE does NOT affect the Python pip package** `langgraph-checkpoint-redis` (which is in the 0.x line and is a separate package). Python developers are not exposed to this CVE via pip.

🕒 **verify live** — version numbers above are accurate as of 2026-07-07. Check the CVE advisories and PyPI for any subsequent patches before pinning.

**Why:** These affect self-hosted deployments only. LangSmith's hosted platform uses PostgreSQL and is not affected by the SQLite/Redis issues. CVE-2026-28277's deserialization risk applies to anyone accepting external input into checkpoints, even if you do not expose history filtering to end users.

**Sources:** [research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer](https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/) (2026, Check Point Research) · [github.com/advisories/GHSA-wwqv-p2pp-99h5](https://github.com/advisories/GHSA-wwqv-p2pp-99h5) (GitHub Advisory) · [pypi.org/project/langgraph](https://pypi.org/project/langgraph/) (confirmed 1.2.7, 2026-07-07) · [vulnerability.circl.lu/vuln/cve-2026-27022](https://vulnerability.circl.lu/vuln/cve-2026-27022) (CIRCL — confirms npm ecosystem for CVE-2026-27022)

**Confidence:** independently-corroborated

---

## Practice: Keep state schemas minimal and fully JSON-serializable — test round-trip serialization in CI

**Do:** Define LangGraph graph state using `TypedDict` (or Pydantic `BaseModel` for validated node boundaries). Include only fields that downstream nodes actually read. Replace `set` with `list`, `bytes` with base64 strings (`import base64; base64.b64encode(my_bytes).decode()`), and `datetime` with ISO-8601 strings (`from datetime import datetime; datetime.now().isoformat()`). Add a CI test that `json.dumps(sample_state)` succeeds without error.

**Why:** Every node transition serializes the entire state to the checkpointer store. Storing raw LLM responses with usage metadata, full document corpora, or custom objects can balloon checkpoint sizes. One production postmortem reported a 180 KB per-checkpoint state at 50 documents, causing PostgreSQL writes to climb to 400 ms per step. Non-serializable types (sets, raw bytes, custom classes, functions, streams) pass silently through `InMemorySaver` in development but crash at runtime against `PostgresSaver` or `SqliteSaver` — a common source of hard-to-diagnose production failures.

**Caveat / contested:** Using `TypedDict` gives zero runtime validation — incorrect data flows through undetected. Use Pydantic `BaseModel` for inputs/outputs at node boundaries while keeping the top-level graph state as `TypedDict` (the hybrid pattern). One source (shazaali.substack.com) recommends exactly this hybrid.

**Sources:** markaicode.com/errors/langgraph-json-parse-error-fix/ (unlinked — 403 bot-protection, confirmed live via WebFetch) · [shazaali.substack.com/p/type-safety-in-langgraph-when-to](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to) · [www.swarnendu.de/blog/langgraph-best-practices](https://www.swarnendu.de/blog/langgraph-best-practices/)

**Confidence:** independently-corroborated

---

## Practice: Use LangMem for cross-session long-term memory extraction — but only for non-latency-sensitive workloads

**Do:** If you need agents to learn from past conversations (extract user preferences, build episodic examples — records of past conversations — evolve system prompts), install `langmem` (`pip install -U langmem`). Wire it to LangGraph's `BaseStore` with `create_manage_memory_tool` and `create_search_memory_tool`. Run memory consolidation as a background / batch task, not inline with user responses.

**Why:** LangMem (launched 2025-02-18) provides three memory types: semantic (stored facts and preferences), episodic (few-shot examples from past conversations), and procedural (evolving system prompt rules). It integrates natively with LangGraph's long-term memory layer.

**Caveat / contested:** ⚠️ **WARNING** — LangMem's p95 search latency (LOCOMO benchmark) is 59.82 seconds. Calling it inline during a user-facing conversation will produce unacceptable wait times. Use it in background jobs or deferred consolidation loops only.

The package is pre-1.0 (latest PyPI release was **0.0.30**, published 2025-10-27, as of 2026-07-07 — eight months without a PyPI release). The GitHub repo shows active commits through June 2026 but no formal tagged releases. There is an open GitHub issue (#130) requesting a new PyPI release for LangGraph 1.0+ compatibility — until resolved, verify that 0.0.30 works with your installed LangGraph (current: 1.2.7) before shipping. Treat as experimental infrastructure that may change API surfaces.

🕒 **verify live** — check [pypi.org/project/langmem](https://pypi.org/project/langmem/) and [github.com/langchain-ai/langmem](https://github.com/langchain-ai/langmem) (issue #130 specifically) for current version and compatibility status before adopting.

**Sources:** [www.langchain.com/blog/langmem-sdk-launch](https://www.langchain.com/blog/langmem-sdk-launch) (2025-02-18) · [langchain-ai.github.io/langmem/concepts/conceptual_guide](https://langchain-ai.github.io/langmem/concepts/conceptual_guide/) (LangMem docs) · [atlan.com/know/long-term-memory-langchain-agents](https://atlan.com/know/long-term-memory-langchain-agents/) (independent — source of the LOCOMO p95 figure)

**Confidence:** independently-corroborated (p95 figure is p95 *search* latency on LOCOMO benchmark, not "memory extraction" latency)

---

## Practice: Add vector-search retrieval to the BaseStore for semantic episodic memory at scale

**Do:** When an agent needs to retrieve *relevant* past interactions rather than *all* past interactions, extend the `BaseStore` with a vector-search backend. Options include `RedisStore` (via `langgraph-checkpoint-redis`), `MongoDBStore` (via `langgraph-store-mongodb`), or a custom store wrapping Pinecone / Weaviate / Chroma. Embed the query with the same embedding model used at write time — using different models at write vs. read time silently degrades search quality — then call `store.search(namespace, query=str(user_message))` to retrieve semantically relevant memories.

**Why:** Storing all past interactions and injecting them wholesale into the context window does not scale — at several hundred conversations the prompt becomes too long and noisy. Vector search lets the agent retrieve only the few most relevant memories for the current query, keeping the context window focused.

**Caveat / contested:** Vector retrieval adds embedding cost per query and per write. For simple single-user applications with short histories, keyword or recency-based filtering is usually sufficient and cheaper. Hybrid storage (vector DB for semantic ops + relational DB for metadata filtering) adds architectural complexity that is only warranted at scale.

**Sources:** [redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) (2025-03-28, updated 2026-06-01) · [www.mongodb.com/company/blog/product-release-announcements/powering-long-term-memory-for-agents-langgraph](https://www.mongodb.com/company/blog/product-release-announcements/powering-long-term-memory-for-agents-langgraph) (MongoDB) · medium.com/@anil.jain.baba/long-term-agentic-memory-with-langgraph-824050b09852 (independent, unlinked — 403 bot-protection, confirmed live via WebFetch)

**Confidence:** independently-corroborated

---

## Practice: Structure thread_id meaningfully for multi-tenant systems — prune old checkpoints by policy

**Do:** Treat `thread_id` as a first-class key scoped to a specific conversation instance. For multi-tenant systems, use a compound format such as `tenant-{tenantId}:user-{userId}:session-{sessionId}`. Implement a checkpoint pruning policy (e.g. delete threads older than N days) to prevent unbounded database growth. LangGraph does not provide a built-in pruning API — you will need to issue a direct database query or `DELETE FROM checkpoints WHERE thread_ts < now() - interval 'N days'` against your backing store.

**Why:** Without a meaningful `thread_id` convention, you cannot reliably associate checkpoints with the right user or session, debugging becomes guesswork, and the checkpoint table grows without bound.

**Caveat / contested:** The specific naming convention (`tenant:user:session`) is a recommendation from community sources and is not an official LangChain standard. The pruning policy details (TTL, archiving strategy) depend on your compliance and debugging requirements and are not prescribed by LangGraph.

**Sources:** [www.swarnendu.de/blog/langgraph-best-practices](https://www.swarnendu.de/blog/langgraph-best-practices/) · [sparkco.ai/blog/mastering-langgraph-checkpointing-best-practices-for-2025](https://sparkco.ai/blog/mastering-langgraph-checkpointing-best-practices-for-2025)

**Confidence:** thin (two community blogs; no official LangChain guidance on thread_id naming conventions was locatable in this session)

---

## Practice: Namespace BaseStore entries by user_id (not thread_id) and use deterministic keys to prevent stale-fact accumulation

**Do:** When writing to the `BaseStore`, always namespace by user identity: `namespace = ("memories", user_id)`. For facts that should overwrite older versions (e.g. the user's current city), use a deterministic key derived from the fact category (e.g. `"location"`) rather than a random UUID. Reserve random UUIDs for facts that should accumulate (e.g. each product the user has mentioned).

**Why:** Using a random UUID for every write causes stale or contradictory facts to accumulate silently — the store grows with dozens of entries like "user lives in Tokyo" and "user lives in Berlin" with no way to know which is current. Deterministic keys for mutable facts act as an upsert: the new value overwrites the old one.

**Caveat / contested:** Deterministic keys work for single-valued facts but are wrong for collections. The pattern requires you to explicitly model which facts are "last writer wins" vs. "append only" — LangGraph does not automate this. LangMem's background consolidation can help manage it at the cost of the latency overhead noted in the LangMem practice above.

**Sources:** [focused.io/lab/persistent-agent-memory-in-langgraph](https://focused.io/lab/persistent-agent-memory-in-langgraph) (Focused.io) · [redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) (code examples show namespace/key pattern)

**Confidence:** independently-corroborated

---

## Held pending fixes (not publish-ready)

- ConversationSummaryMemory deprecation confirmation: the official LangChain API reference page redirect-looped; could not confirm from primary docs. Classified as deprecated alongside ConversationBufferMemory via secondary sources only. ⚠ PENDING
- ShallowRedisSaver coverage: reduces storage by storing only the latest checkpoint; only one passing mention fetched — needs dedicated follow-up. ⚠ PENDING

## CHANGELOG (grading → this entry)

1. **Skeptic/Timekeeper KILL-1 (CVE Redis pin non-existent on PyPI):** The draft instructed `pip install langgraph-checkpoint-redis >= 1.0.2` — that version does not exist on PyPI (package tops out at 0.5.0 as of 2026-07-07). Root cause: CVE-2026-27022 is in the **JavaScript/npm** package `@langchain/langgraph-checkpoint-redis`, not the Python pip package. Corrected: removed Python pip instruction for Redis; split CVE guidance by ecosystem with explicit npm fix; added pip commands for checking installed versions and upgrading; confirmed via CIRCL advisory and Snyk that CVE-2026-27022 is SNYK-JS-LANGCHAINLANGGRAPHCHECKPOINTREDIS (npm ecosystem).
2. **Timekeeper KILL-3 (ConversationBufferMemory removal timeline):** Original stated "scheduled for removal at v1.0.0." LangChain v1.0 shipped October 2025 — the class was NOT removed; it was moved to `langchain_classic`. Corrected to: "exists in `langchain_classic` in LangChain 1.x (current: 1.3.11); removal planned for v2.0.0."
3. **Beginner L-3 (KILL — Postgres silent failure):** Moved `autocommit=True` and `row_factory=dict_row` requirement into the Do section with a correct code snippet. Original had this critical requirement only in a caveat after the main instructions.
4. **Beginner L-2 (KILL — CVE missing runnable commands):** Added `pip show` check command and `pip install --upgrade` command for the CVE practice. Original gave version numbers but no runnable commands.
5. **Skeptic FIX-4 (LangMem latency description):** Changed "memory extraction" to "p95 search latency (LOCOMO benchmark)" — the 59.82s figure is a benchmark search number, not memory extraction time.
6. **Skeptic FIX-5 (LangMem "pre-configured"):** Softened "pre-configured in all LangGraph Platform deployments" to "integrates natively with LangGraph's long-term memory layer" — the "pre-configured" claim was not supported by the cited launch blog.
7. **Timekeeper FIX-1 (postgres version date anchor):** Added explicit "as of 2026-07-07" date anchor for version 3.1.0.
8. **Timekeeper FIX-2 (langgraph version floor vs. target):** Added "minimum floor; current: 1.2.7 (2026-06-30)" to prevent readers from targeting an old release.
9. **Timekeeper FIX-3 (LangMem compatibility):** Added date anchor "0.0.30 as of 2026-07-07" and noted GitHub issue #130 about LangGraph 1.0+ compatibility.
10. **Timekeeper FLAG-6 (transitive dependency clarification):** Added note that upgrading `langgraph >= 1.0.10` transitively pulls in a patched `langgraph-checkpoint`; users don't need to pin it separately unless they have a pinned transitive dependency.
11. **Beginner L-1 (prerequisites):** Added Prerequisites box at the top of the file.
12. **Beginner L-4/L-5/L-6:** Added graph/edge/node explanation; added complete `graph.invoke()` call with `config`; added minimal `create_react_agent` code example with `SqliteSaver`.
13. **Beginner L-7 (LangMem jargon):** Added inline definitions of semantic, episodic, and procedural memory in the LangMem practice.
14. **Link-check gate (2026-07-08):** markaicode.com/errors/langgraph-json-parse-error-fix/ returned 403 (bot-protection; confirmed live via WebFetch). Unlinked to plain text; citation retained.
15. **Link-check gate (2026-07-08):** medium.com/@anil.jain.baba/long-term-agentic-memory-with-langgraph-824050b09852 returned 403 (bot-protection; confirmed live via WebFetch). Unlinked to plain text; citation retained. All other 20 URLs: 200.

