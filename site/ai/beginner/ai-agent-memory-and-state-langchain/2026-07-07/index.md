# AI Agent Memory and State Management — LangChain / LangGraph — Beginner Guide (as of 07 Jul 2026)

> How to manage memory and persistent state in LangChain agents and LangGraph graphs — written for people new to AI. Covers which memory tool to start with, how to keep conversation history across sessions, which old APIs to stop using, and a critical security update — accurate as of July 2026.


<!-- This file lands at content/ai/beginner/ai-agent-memory-and-state-langchain/2026-07-07/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag. -->

# AI Agent Memory and State Management — LangChain / LangGraph — Beginner Guide (as of 07 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **07 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Before you start — key ideas explained simply

**LangChain** is a Python library that makes it easier to build applications powered by large language models (LLMs — AI models like GPT or Claude).

**LangGraph** is an extension of LangChain. It lets you build an **agent** — an AI program that can take a series of steps to complete a task — by describing the steps as a **graph**. A graph is just a map: it shows the steps (called **nodes**) and the arrows between them (called **edges**). LangGraph saves the agent's progress at every step automatically. That saved snapshot is called a **checkpoint**.

**Memory** in this context means: "does the agent remember what was said before?" Without memory, every message is a blank slate. With memory, the agent can refer back to earlier parts of the conversation.

**State** means: "what information is the agent currently holding?" The state is everything the agent knows right now — the conversation history, any facts it has looked up, any results from tools it has called.

---

## Practice: Choose the right memory storage for where you are in development — start with the simplest one and upgrade when you need to

**Do:** Use the storage option that matches your situation. LangGraph calls these storage tools **checkpointers** — they save ("checkpoint") the state of your agent automatically.

- **Just testing or building a demo?** Use `InMemorySaver`. It requires no setup and keeps everything in your computer's RAM.
- **Building something for yourself on one computer?** Use `SqliteSaver` / `AsyncSqliteSaver`. SQLite is a lightweight file-based database that lives in a single file on your disk.
- **Running a real service that multiple users will access at the same time?** Use `PostgresSaver` / `AsyncPostgresSaver`. PostgreSQL (often called "Postgres") is a full database server designed to handle many simultaneous connections.

Here is the simplest working example using the in-memory option:

```python
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver.from_conn_string(":memory:")  # swap for PostgresSaver in prod
agent = create_react_agent(model, tools, checkpointer=checkpointer)
```

⚠️ **WARNING — Postgres silent failure.** If you connect to PostgreSQL manually, you MUST include `autocommit=True` and `row_factory=dict_row`. If you leave these out, the checkpointer will fail silently — it gives no error, but your agent's memory will not be saved. You will lose data with no warning. The correct connection code is:

```python
import psycopg
from langgraph.checkpoint.postgres import PostgresSaver

conn = psycopg.connect(
    "postgresql://user:pass@host/db",
    autocommit=True,          # REQUIRED — without this, saves silently fail
    row_factory=psycopg.rows.dict_row,  # REQUIRED — without this, saves silently fail
)
checkpointer = PostgresSaver(conn)
```

**A note on package names.** LangGraph v0.2 split checkpointers into their own separate Python packages: `langgraph-checkpoint-sqlite` and `langgraph-checkpoint-postgres`. If you are importing checkpointers from the main `langgraph` package and have not updated in a while, you may be running older, unpatched code. Install the separate packages to get the latest fixes.

🕒 **verify live** — `langgraph-checkpoint-postgres` was at **3.1.0** (released 2026-05-12, confirmed PyPI 2026-07-07); `langgraph-checkpoint-sqlite` was at 3.1.0 (released 2026-05-12). Check [pypi.org/project/langgraph-checkpoint-postgres](https://pypi.org/project/langgraph-checkpoint-postgres/) before pinning.

**Why this matters for a beginner:** `InMemorySaver` stores everything in RAM. The moment your program stops, all conversation history is gone. When you are ready to build something real — or when you restart the program and want the agent to remember past conversations — you need SQLite (for single-user local apps) or Postgres (for multi-user services). Getting this wrong costs you history silently; the agent just starts every conversation from scratch without telling you why.

**Sources:** [www.langchain.com/blog/langgraph-v0-2](https://www.langchain.com/blog/langgraph-v0-2) (2024) · [redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) (2025-03-28, updated 2026-06-01) · [pypi.org/project/langgraph-checkpoint-postgres](https://pypi.org/project/langgraph-checkpoint-postgres/) (confirmed 2026-07-07)

**Confidence:** independently-corroborated

---

## Practice: Use thread_id for one conversation; use a separate store for facts you want to remember across all future conversations

**Do:** Every conversation in LangGraph needs a label — called a **thread_id** (a "thread" is one conversation, and the "id" is just a unique name you give it). Pass the thread_id like this:

```python
result = graph.invoke(
    {"messages": [HumanMessage(content="Hello")]},
    config={"configurable": {"thread_id": "user-abc-session-1"}}
)
```

That's all you need for the agent to remember earlier messages within that same conversation.

However, when a user starts a **new** conversation (a new thread), the agent starts fresh — it does not automatically carry over what it learned last time. If you want the agent to remember things across different conversations — for example, a user's name or preferences — you must save those facts to a separate storage system called a **BaseStore** (a "base store" is just a general-purpose key-value database). You give each entry a **namespace** — think of a namespace as a folder label — and store user-specific facts under `("memories", user_id)` where `user_id` is a unique ID for that person.

The simplest BaseStore for development is `InMemoryStore`. For real deployments, swap it for `PostgresStore`, `RedisStore`, or `MongoDBStore`.

**Important:** `InMemoryStore` loses all stored facts the moment your program stops. Swap it for a persistent store before going to production.

**Why this matters for a beginner:** The checkpointer (conversation memory) and the BaseStore (long-term facts) are two completely separate systems. Beginners often assume that "the agent remembers everything" once they add a checkpointer — but that memory only exists inside one conversation thread. A returning user with a new thread_id gets a blank slate unless you explicitly save facts to the BaseStore. Getting this wrong means users have to re-introduce themselves every time they start a new chat.

**Sources:** [focused.io/lab/persistent-agent-memory-in-langgraph](https://focused.io/lab/persistent-agent-memory-in-langgraph) (Focused.io) · [atlan.com/know/long-term-memory-langchain-agents](https://atlan.com/know/long-term-memory-langchain-agents/) (Atlan) · [redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) (2025-03-28, updated 2026-06-01)

**Confidence:** independently-corroborated

---

## Practice: Stop using ConversationBufferMemory and ConversationSummaryMemory — migrate to LangGraph checkpointing

**Do:** If you followed an older LangChain tutorial and your code imports `ConversationBufferMemory`, `ConversationSummaryMemory`, or `RunnableWithMessageHistory`, those are deprecated (officially abandoned and no longer maintained). Replace them with a LangGraph checkpointer using this minimal migration pattern:

```python
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver.from_conn_string(":memory:")  # swap for PostgresSaver in prod
agent = create_react_agent(model, tools, checkpointer=checkpointer)
```

If you are not using LangGraph graphs — for example, if you are using plain **LCEL** (LangChain Expression Language — a way of chaining LangChain steps together without building a full graph) — there is no official first-party migration path. You can manage a message history list yourself or use a framework-agnostic store.

**Why this matters for a beginner:** `ConversationBufferMemory` was deprecated at LangChain v0.3.1. `RunnableWithMessageHistory` was deprecated at v0.3. Both classes still exist in a compatibility package called `langchain_classic` in the current LangChain 1.x (current version: 1.3.11, June 2026), but they are not being fixed or updated. Removal is planned for v2.0.0 — 🕒 verify live. These classes were built before LangChain supported tool-calling agents properly, which means they can behave incorrectly with modern AI models. Continuing to use them means you are building on a foundation that will eventually be deleted and that may already be misbehaving silently.

**Note from one independent source (db0.ai):** There is a fair criticism that tying memory to any specific framework creates fragility, because LangChain has already redesigned itself twice. If you are not using LangGraph, keeping a simple list of messages yourself may be more durable than any framework's memory class.

**Sources:** [atlan.com/know/long-term-memory-langchain-agents](https://atlan.com/know/long-term-memory-langchain-agents/) (Atlan) · [db0.ai/blog/langchain-memory-deprecated](https://db0.ai/blog/langchain-memory-deprecated) (independent) · [pypi.org/project/langchain](https://pypi.org/project/langchain) (confirmed current 1.3.11, 2026-06-22, PyPI 2026-07-07) · [reference.langchain.com/python/langchain-classic/memory/buffer/ConversationBufferMemory](https://reference.langchain.com/python/langchain-classic/memory/buffer/ConversationBufferMemory) (LangChain reference docs, confirmed 2026-07-07)

**Confidence:** independently-corroborated

---

## Practice: Update LangGraph checkpointer packages immediately — CVEs disclosed in 2025-2026 allow RCE

⚠️ **WARNING — Active security vulnerabilities.** Four **CVEs** (a CVE is an officially numbered security vulnerability — "Common Vulnerabilities and Exposures") have been found in self-hosted LangGraph deployments. Two of them allow **RCE** — Remote Code Execution — meaning an attacker on the internet can run arbitrary commands on your server. This is as serious as it gets.

**Step 1 — Check what you have installed.** Run this command in your terminal:

```bash
pip show langgraph langgraph-checkpoint-sqlite langgraph-checkpoint
```

This will print the installed version of each package. Compare the numbers to the safe versions listed below.

**Step 2 — Upgrade.** Run:

```bash
pip install --upgrade langgraph langgraph-checkpoint-sqlite langgraph-checkpoint
```

**Step 3 — Set a safety flag.** Add this line to your `.env` file (a `.env` file is a plain text file in your project folder where you store settings) or set it as a shell environment variable:

```
LANGGRAPH_STRICT_MSGPACK=true
```

**What are the vulnerabilities? (Plain English)**

- **CVE-2025-67644** — An attacker can manipulate filter inputs to the SQLite checkpointer to run arbitrary SQL (this is called SQL injection). Fixed in `langgraph-checkpoint-sqlite >= 3.0.1`. Current version is 3.1.0 (released 2026-05-12). 🕒 verify live.
- **CVE-2026-28277** — The SQL injection above can be chained with an unsafe **msgpack** deserialization step (msgpack is a data-packing format; "deserialization" means unpacking stored data back into Python objects — if done unsafely, an attacker can sneak executable code into those objects). Together these allow full RCE. Fixed in `langgraph >= 1.0.10`. The current version is **1.2.7** (released 2026-06-30) — upgrade to current. Upgrading `langgraph >= 1.0.10` automatically pulls in a patched `langgraph-checkpoint >= 3.0.0` as a dependency, so you do not need to pin `langgraph-checkpoint` separately unless you have it pinned to an older version yourself.
- **CVE-2025-64439** (CVSS 7.4 — a severity score out of 10; 7.4 is "High") — RCE via `JsonPlusSerializer` in `langgraph-checkpoint < 3.0.0`. Fixed by the same upgrade: `langgraph >= 1.0.10`.
- **CVE-2026-27022** — SQL injection in the **JavaScript/npm** package `@langchain/langgraph-checkpoint-redis`. Fix: `npm install @langchain/langgraph-checkpoint-redis@>=1.0.2`. **This CVE does NOT affect the Python pip package** `langgraph-checkpoint-redis` (which is in the 0.x line and is a separate package). If you are using only Python, you are not exposed to this CVE.

🕒 **verify live** — version numbers above are accurate as of 2026-07-07. Check the CVE advisories and PyPI for any subsequent patches before pinning.

**Why this matters for a beginner:** These vulnerabilities affect self-hosted deployments only. LangSmith's hosted platform uses PostgreSQL and is not affected by the SQLite/Redis issues. The deserialization risk (CVE-2026-28277) applies to anyone accepting external input into checkpoints — even if you do not intentionally expose history filtering to end users. If you built a demo that is accessible from the internet and have not upgraded, it may already be vulnerable.

**Sources:** [research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer](https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/) (2026, Check Point Research) · [github.com/advisories/GHSA-wwqv-p2pp-99h5](https://github.com/advisories/GHSA-wwqv-p2pp-99h5) (GitHub Advisory) · [pypi.org/project/langgraph](https://pypi.org/project/langgraph/) (confirmed 1.2.7, 2026-07-07) · [vulnerability.circl.lu/vuln/cve-2026-27022](https://vulnerability.circl.lu/vuln/cve-2026-27022) (CIRCL — confirms npm ecosystem for CVE-2026-27022)

**Confidence:** independently-corroborated

---

## Practice: Keep the data your agent stores between steps small, simple, and JSON-friendly — and test it

**Do:** LangGraph tracks your agent's current data in something called a **state schema** — a definition of all the fields the agent is allowed to store during its run. Define this using Python's `TypedDict` (a built-in Python way to describe what keys and value types a dictionary should have). Only include fields that the agent actually uses in later steps.

Avoid storing these types directly in state, because they cannot be saved to a database automatically:

- `set` — replace with `list`
- `bytes` (raw binary data) — replace with a base64 string: `import base64; base64.b64encode(my_bytes).decode()`
- `datetime` (Python date/time objects) — replace with an ISO-8601 string: `from datetime import datetime; datetime.now().isoformat()`
- Custom Python classes, functions, or streaming objects

Add a test to your project that verifies the state can be turned into JSON without crashing:

```python
import json
json.dumps(sample_state)  # if this raises an error, your state has non-serializable fields
```

For stronger safety, use Pydantic's `BaseModel` (a popular Python library for data validation) at the boundaries between steps — where one node passes data to the next — while keeping the top-level state as `TypedDict`. This "hybrid" pattern catches bad data early.

**Why this matters for a beginner:** Every time your agent moves from one step to the next, LangGraph serializes (converts to a storable format) your entire state and saves it to the checkpointer. `InMemorySaver` (the development option) accepts almost anything, including types that cannot be saved to a real database. This means your code can appear to work perfectly in development and then crash the moment you switch to SQLite or Postgres in production. One real-world case saw a state balloon to 180 KB per checkpoint because it was storing full document text inside the state — Postgres writes slowed to 400 ms per step. Keep the state lean and serialization-safe from the start.

**Sources:** markaicode.com/errors/langgraph-json-parse-error-fix/ (unlinked — 403 bot-protection, confirmed live via WebFetch) · [shazaali.substack.com/p/type-safety-in-langgraph-when-to](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to) · [www.swarnendu.de/blog/langgraph-best-practices](https://www.swarnendu.de/blog/langgraph-best-practices/)

**Confidence:** independently-corroborated

---

## Practice: Use LangMem to extract long-term memories from conversations — but never call it inline during a live response

**Do:** If you want your agent to learn facts from past conversations and carry them forward — for example, remembering that a user prefers short answers, or building up a history of things they have mentioned — install the `langmem` package:

```bash
pip install -U langmem
```

Connect it to LangGraph's BaseStore using `create_manage_memory_tool` and `create_search_memory_tool`. **Always run memory consolidation as a background or batch task, not while the user is waiting for a response.**

LangMem supports three types of memory:
- **Semantic memory** — stored facts and preferences ("this user lives in Berlin")
- **Episodic memory** — records of past conversations used as examples for future responses
- **Procedural memory** — rules that evolve over time to improve how the agent responds (its "system prompt" updates itself)

⚠️ **WARNING — Do not call LangMem inline.** LangMem's p95 search latency (the time it takes to search memories at the 95th-percentile of requests, measured on the LOCOMO benchmark) is **59.82 seconds**. If you call it while the user is waiting for a reply, your app will feel completely broken. Use it only in background jobs or deferred consolidation loops.

⚠️ **WARNING — LangMem is experimental and may have compatibility issues.** The package is pre-1.0 (latest PyPI release was **0.0.30**, published 2025-10-27, as of 2026-07-07 — eight months without a PyPI release). The GitHub repository shows active development through June 2026 but no new formal releases. There is an open GitHub issue (#130) requesting a new PyPI release for LangGraph 1.0+ compatibility. Before using LangMem in any project, verify that version 0.0.30 works with your installed LangGraph (current: 1.2.7). Treat it as experimental infrastructure — its API may change.

🕒 **verify live** — check [pypi.org/project/langmem](https://pypi.org/project/langmem/) and [github.com/langchain-ai/langmem](https://github.com/langchain-ai/langmem) (issue #130 specifically) for current version and compatibility status before adopting.

**Why this matters for a beginner:** LangMem is the most capable tool for building agents that genuinely learn from experience. However, it is also the riskiest choice for beginners: it is pre-release, may not be compatible with the current LangGraph, and has search times that will make your app unusable if called at the wrong moment. Start with the simpler BaseStore practices above and add LangMem only when you have a specific need for it.

**Sources:** [www.langchain.com/blog/langmem-sdk-launch](https://www.langchain.com/blog/langmem-sdk-launch) (2025-02-18) · [langchain-ai.github.io/langmem/concepts/conceptual_guide](https://langchain-ai.github.io/langmem/concepts/conceptual_guide/) (LangMem docs) · [atlan.com/know/long-term-memory-langchain-agents](https://atlan.com/know/long-term-memory-langchain-agents/) (independent — source of the LOCOMO p95 figure)

**Confidence:** independently-corroborated (p95 figure is p95 *search* latency on LOCOMO benchmark, not "memory extraction" latency)

---

## Practice: Add vector search to the BaseStore when your agent needs to find relevant memories — not just recent ones

**Do:** Once an agent has accumulated many past interactions, injecting all of them into every response becomes too slow and noisy. Instead, extend the BaseStore with a **vector search** backend — a database that finds entries by meaning rather than by exact keyword match. Options include `RedisStore` (via `langgraph-checkpoint-redis`), `MongoDBStore` (via `langgraph-store-mongodb`), or a custom store wrapping a vector database such as Pinecone, Weaviate, or Chroma.

When embedding (converting text into numbers the vector database can compare) entries, use the same AI embedding model at both write time and search time. Using different models at write vs. read time silently degrades search quality. Search like this:

```python
store.search(namespace, query=str(user_message))
```

**Why this matters for a beginner:** This is an advanced topic — most beginners do not need it. For a single-user application with a short conversation history, simple recency filtering (keeping the last N messages) is cheaper and simpler. Vector search is worth adding only when you have hundreds of past conversations and need the agent to find the few most relevant ones for the current question. Adding it early adds cost per query and architectural complexity without benefit.

**Sources:** [redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) (2025-03-28, updated 2026-06-01) · [www.mongodb.com/company/blog/product-release-announcements/powering-long-term-memory-for-agents-langgraph](https://www.mongodb.com/company/blog/product-release-announcements/powering-long-term-memory-for-agents-langgraph) (MongoDB) · medium.com/@anil.jain.baba/long-term-agentic-memory-with-langgraph-824050b09852 (independent, unlinked — 403 bot-protection, confirmed live via WebFetch)

**Confidence:** independently-corroborated

---

## Practice: Give thread_id a meaningful structure — and delete old checkpoints before your database fills up

**Do:** Treat `thread_id` as a meaningful label, not a random number. For applications with multiple users or multiple organizations, use a compound format such as:

```
tenant-{tenantId}:user-{userId}:session-{sessionId}
```

For example: `tenant-acme:user-42:session-8f3a`.

Also set up a policy to delete old checkpoints. LangGraph does not do this for you automatically. You will need to run a query directly against your database, for example in Postgres:

```sql
DELETE FROM checkpoints WHERE thread_ts < now() - interval 'N days'
```

Replace `N` with the number of days you want to keep checkpoints (for example, 30 for 30 days).

**Why this matters for a beginner:** Without a meaningful thread_id format, you cannot tell which saved conversations belong to which users when something goes wrong — debugging becomes guesswork. Without a deletion policy, the checkpoint table grows forever. A database that fills up will stop accepting new writes, which will silently break your agent's memory again.

**Note:** The specific naming convention shown above comes from community sources, not official LangChain documentation. The right pruning policy depends on your privacy rules and debugging needs. There is no single official answer here.

**Sources:** [www.swarnendu.de/blog/langgraph-best-practices](https://www.swarnendu.de/blog/langgraph-best-practices/) · [sparkco.ai/blog/mastering-langgraph-checkpointing-best-practices-for-2025](https://sparkco.ai/blog/mastering-langgraph-checkpointing-best-practices-for-2025)

**Confidence:** thin (two community blogs; no official LangChain guidance on thread_id naming conventions was locatable in this session)

---

## Practice: In the BaseStore, use the user's ID as the folder label — and use stable keys for facts that should overwrite, not accumulate

**Do:** When saving facts to the BaseStore, always group them under the user's identity:

```python
namespace = ("memories", user_id)
```

For facts that should replace the old value when updated — for example, a user's current city — use a fixed key name (such as `"location"`) rather than a random ID. This acts as an overwrite (sometimes called an "upsert").

For facts that should accumulate — for example, every product a user has mentioned — use a unique ID (such as a UUID) so new entries do not overwrite old ones.

**Why this matters for a beginner:** If you use a random key for every fact you save, you will end up with dozens of entries like "user lives in Tokyo" and "user lives in Berlin" with no way to tell which is current. The agent may then tell a user something that was true six months ago. Using a fixed key for mutable (changeable) facts ensures the agent always uses the latest value. You have to decide consciously which facts are "replace the old one" vs. "keep adding new entries" — LangGraph does not make this decision for you.

**Sources:** [focused.io/lab/persistent-agent-memory-in-langgraph](https://focused.io/lab/persistent-agent-memory-in-langgraph) (Focused.io) · [redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) (code examples show namespace/key pattern)

**Confidence:** independently-corroborated

---

## Held pending fixes (not publish-ready)

- ConversationSummaryMemory deprecation confirmation: the official LangChain API reference page redirect-looped; could not confirm from primary docs. Classified as deprecated alongside ConversationBufferMemory via secondary sources only. ⚠ PENDING
- ShallowRedisSaver coverage: reduces storage by storing only the latest checkpoint; only one passing mention fetched — needs dedicated follow-up. ⚠ PENDING

---

## CHANGELOG

### Re-leveled by rings-beginner-author for beginner track (2026-07-07)

Source: technical best-practices entry dated 2026-07-07 (0 fabrications; 13 corrections applied by RingS panel). Re-leveled for `track: beginner`, `audience: "people new to AI"`. No new facts or URLs introduced. All source URLs copied verbatim. Summary of changes from technical to beginner version:

- Added "Before you start" section defining LangChain, LangGraph, graphs, nodes, edges, checkpoints, memory, and state in plain language.
- Expanded every jargon term on first use: checkpointer, BaseStore, namespace, thread_id, TypedDict, LCEL, msgpack, CVE, RCE, CVSS, serialization, deserialization, vector search, embedding, upsert, episodic/semantic/procedural memory.
- Reordered advice to lead with the simplest default path (InMemorySaver → SqliteSaver → PostgresSaver) before mentioning alternatives.
- Strengthened "why it matters" for each practice to name the concrete failure it prevents (silent data loss, stale facts, app crash in production, security breach).
- All ⚠️ WARNING blocks preserved and expanded with plain-English explanations of the risk (Postgres silent failure, LangMem inline latency, LangMem experimental status, CVE/RCE).
- All 🕒 verify live tags preserved verbatim.
- CVE security section: all four CVEs kept, all pip commands kept verbatim, all version numbers kept verbatim. Added step-by-step structure (Step 1 check, Step 2 upgrade, Step 3 set flag) and plain-English explanation of each CVE.
- Held pending section kept unchanged.
- CHANGELOG from grading panel kept as the second section below this note.

### CHANGELOG (grading → technical entry, 2026-07-07)

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

