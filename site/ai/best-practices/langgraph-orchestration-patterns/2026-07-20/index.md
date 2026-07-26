# AI Agent Orchestration — LangGraph — Best Practices (as of 20 Jul 2026)

> Practical best practices for building orchestrated AI agent workflows with LangGraph: state schema design, checkpointing, human-in-the-loop, streaming, subgraphs, LangSmith Deployment, and LangMem integration.


<!-- content/ai/best-practices/langgraph-orchestration-patterns/2026-07-20/index.md — IMMUTABLE snapshot.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented = official vendor docs only. -->

# AI Agent Orchestration — LangGraph (as of 20 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **20 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

**Current stable version:** LangGraph 1.2.9 (released 10 Jul 2026, Python ≥3.10, MIT). 🕒 **verify live**

**LangGraph 1.0 GA:** October 22, 2025 — first stable major release. Key migration notes in the final section.

## Prerequisites

- Python ≥3.10 (some async features require ≥3.11 — see the streaming section).
- `pip install langgraph` or `pip install --upgrade langgraph` to upgrade.
- An LLM provider API key (e.g., `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`).
- Understand that LLM calls cost real money — running agent loops without guards can generate large bills quickly. Set a hard spending limit on your API provider's billing dashboard before running any production code.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Choose TypedDict for internal graph state; reserve Pydantic for system boundaries

**Do:** Define your `StateGraph` schema with `TypedDict` (Python stdlib) for the internal state that flows between nodes. Use Pydantic `BaseModel` only at external boundaries — API inputs, user-submitted data, database reads — where runtime validation is worth the overhead.

**Why (beginner):** `TypedDict` gives IDE autocompletion and static type checking (your editor warns you when you pass the wrong kind of data) with zero runtime cost. Pydantic gives field-by-field validation at runtime, which is useful when you do not control the incoming data — for example, when a user submits a form. Inside the graph, data flows between nodes you wrote and control, so the runtime overhead of Pydantic is usually unnecessary.

**Caveat / contested:** Some practitioners recommend Pydantic throughout for stricter guarantees. One independent guide (Easton Dev, Apr 2026) explicitly recommends Pydantic with `extra='forbid'` to prevent field pollution in the state. The hybrid approach — TypedDict inside, Pydantic at edges — appears in multiple independent sources as the pragmatic compromise. Note: the official docs do not give a single authoritative rule here; this recommendation is based on community consensus.

**Sources:** [shazaali.substack.com — Type Safety in LangGraph: When to Use TypedDict vs. Pydantic](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to) (fetched 2026-07-20) · [eastondev.com — LangGraph Agent Architecture](https://eastondev.com/blog/en/posts/ai/20260424-langgraph-agent-architecture/) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use reducers (annotated fields) to merge parallel node outputs — do not rely on last-writer-wins

**Do:** When multiple nodes can update the same state field simultaneously (e.g., parallel web searches, fan-out patterns), annotate the field with a reducer function using `Annotated[list, operator.add]` or the built-in `add_messages` reducer. A **reducer** is a function that tells LangGraph how to combine concurrent writes into a single result. This tells LangGraph how to merge concurrent writes rather than silently overwriting one result with another.

**Why (beginner):** LangGraph runs sibling nodes in a "superstep" — concurrently, like parallel tasks. Without a reducer, whichever node writes last wins and earlier results are lost. `add_messages` also deduplicates by message ID, preventing ghost duplicates if you replay a checkpoint. The official docs treat this as a fundamental concept, not an advanced feature.

**Caveat / contested:** `add_messages` is designed for `HumanMessage`/`AIMessage` lists. For custom data types (dicts, domain objects) you must write your own reducer function. Failing to do so when nodes run in parallel is a silent data-loss bug — LangGraph will not warn you.

**Sources:** medium.com/cwan-engineering — Building Multi-Agent Systems with LangGraph (fetched 2026-07-20) · [eastondev.com — LangGraph Agent Architecture](https://eastondev.com/blog/en/posts/ai/20260424-langgraph-agent-architecture/) (fetched 2026-07-20) · [aipractitioner.substack.com — Scaling LangGraph Agents: Parallelization, Subgraphs, and Map-Reduce Trade-Offs](https://aipractitioner.substack.com/p/scaling-langgraph-agents-parallelization) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use conditional edges for dynamic routing; use fixed edges for deterministic flow

**Do:** An **edge** in LangGraph is a connection that tells the graph what node to run after the current one finishes. Add a fixed edge (`graph.add_edge(a, b)`) when node A always hands off to node B. Add a conditional edge (`graph.add_conditional_edges(node, routing_fn, {key: target_node})`) when the next step depends on the current state — for example, routing to a tool-calling node or an end node based on whether the LLM requested a tool. The routing function receives the current state and must return a key that maps to one of the listed target nodes.

**Why (beginner):** Fixed edges are simpler, faster, and easier to trace in LangGraph Studio's visual debugger. Conditional edges allow the graph to branch at runtime, which is what makes multi-agent orchestration flexible. Mixing them up (adding a conditional edge where a fixed one suffices) adds complexity without benefit.

**Caveat / contested:** The `Command` primitive (introduced alongside `interrupt()` in late 2024) can replace conditional edges entirely — a node returns `Command(goto="next_node")` instead of the routing function returning a key. Multiple independent sources describe this as a cleaner pattern for dynamic routing in human-in-the-loop flows, but it makes the graph structure less visible because edges are no longer declared at compile time. One guide (DEV Community, James Mour, fetched 2026-07-20) recommends avoiding explicit conditional edges for router nodes in favour of Command-based routing. Contested on style grounds; both patterns are supported.

**Sources:** [docs.langchain.com/oss/python/langgraph/interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) (fetched 2026-07-20) · medium.com/@shuv.sdr — LangGraph Architecture and Design (fetched 2026-07-20) · [dev.to/jamesbmour — Interrupts and Commands in LangGraph](https://dev.to/jamesbmour/interrupts-and-commands-in-langgraph-building-human-in-the-loop-workflows-4ngl) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Match your checkpointer to your deployment tier — never use InMemorySaver in production

**Do:** Pick the checkpointer that fits your deployment:

| Stage | Checkpointer | Why |
|---|---|---|
| Unit tests / throwaway prototype | `InMemorySaver` | Zero setup; state is gone forever when the process stops |
| Local dev with durability needed | `SqliteSaver` | File-backed; survives process restart; single-writer only |
| Production (multi-worker) | `PostgresSaver` / `AsyncPostgresSaver` | Concurrent-safe, durable, queryable |

Pass the checkpointer when compiling the graph: `graph.compile(checkpointer=saver)`. Always supply a `thread_id` in the config when invoking, so each conversation or workflow run has isolated state history. Generate unique thread IDs with `str(uuid.uuid4())` — do not reuse the same ID across users or sessions, as they will share state.

**Why (beginner):** A checkpointer saves a full snapshot of the graph state after every node execution. Without one, the agent has no memory between calls and cannot be resumed after a crash or server restart. The difference between `InMemorySaver` and `PostgresSaver` is the difference between "works in a notebook demo" and "works when your server reboots at 3 AM."

**Caveat / contested:** ⚠️ **WARNING — `InMemorySaver` in production:** state is gone forever when the server stops. If a user's conversation history is stored only in memory, they lose it on every server restart. ⚠️ **WARNING — PostgresSaver thread_id length:** the official docs note that thread_id values must be kept under 255 characters to avoid database errors. Concatenating long user IDs and session IDs without checking length is a silent production bug. `SqliteSaver` uses a serialized write lock, making it unsuitable for concurrent multi-process deployments even if it technically persists to disk — "two users at the same time" will break. Checkpoints accumulate indefinitely — prune old checkpoints periodically to prevent unbounded database growth.

**Sources:** [docs.langchain.com/oss/python/langgraph/persistence](https://docs.langchain.com/oss/python/langgraph/persistence) (fetched 2026-07-20) · [sparkco.ai — Mastering LangGraph Checkpointing: Best Practices for 2025](https://sparkco.ai/blog/mastering-langgraph-checkpointing-best-practices-for-2025) (fetched 2026-07-20) · medium.com/@vignesh_2710 — What is a Checkpointer in LangGraph (fetched 2026-07-20) · [eastondev.com — LangGraph Agent Architecture](https://eastondev.com/blog/en/posts/ai/20260424-langgraph-agent-architecture/) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use `interrupt()` for human-in-the-loop; treat `interrupt_before`/`interrupt_after` as debugging tools only

**Do:** For production human-in-the-loop (HITL) workflows — tool-call approval, content review, multi-turn user input — call `interrupt(payload)` inside a node function. The graph pauses, persists its state, and returns the payload to the caller. Resume by passing `Command(resume=user_response)` on the next invocation. A checkpointer is mandatory for this to work.

For step-through debugging only, use `graph.compile(interrupt_before=["node_name"])` or `interrupt_after` to set static breakpoints.

**Why (beginner):** The LangGraph team introduced `interrupt()` in December 2024 as a simpler, more Pythonic pattern for human-in-the-loop workflows. It lets you place multiple interrupt points anywhere inside a single node function, pass structured data (dicts, lists) as the pause payload, and use `Command(goto=...)` to dynamically change routing after the human responds. The official docs explicitly state that `interrupt_before`/`interrupt_after` are "not recommended for human-in-the-loop workflows" — they are primarily for testing and debugging.

**Caveat / contested:** ⚠️ **WARNING — do not wrap `interrupt()` in a bare `try/except` block.** The function works by raising a special internal exception that the LangGraph runtime catches to pause execution. A broad `except Exception` block will catch and suppress that signal, **bypassing your human oversight gate completely** — the agent will continue without pausing for approval. ⚠️ **WARNING — side effects before `interrupt()` re-execute on resume:** when execution resumes after an interrupt, the entire node restarts from the beginning. Any side effects (sending an email, charging a payment, writing a database record) that ran before the interrupt will execute again. Design nodes to be idempotent or move side effects after the interrupt call — failure to do this causes duplicate emails, double charges, and duplicate records.

**Sources:** [docs.langchain.com/oss/python/langgraph/interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) (fetched 2026-07-20) · [langchain.com/blog — Making it Easier to Build Human-in-the-Loop Agents with interrupt](https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt) (fetched 2026-07-20) · medium.com/@areebahmed575 — LangGraph's interrupt() Function (fetched 2026-07-20) · [dev.to/jamesbmour — Interrupts and Commands in LangGraph](https://dev.to/jamesbmour/interrupts-and-commands-in-langgraph-building-human-in-the-loop-workflows-4ngl) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Compose subgraphs with shared-key schemas when possible; use wrapper nodes when schemas differ

**Do:** Encapsulate a cohesive group of agents (e.g., a research team: planner + searcher + synthesizer) as a compiled `StateGraph` and add it as a single node in the parent graph. If the parent and subgraph share at least one state key with the same name and type, LangGraph routes data automatically. When schemas differ, wrap the subgraph call in a regular node function that transforms state going in and out.

**Why (beginner):** Subgraphs keep large workflows manageable. Each subgraph compiles independently, can be unit-tested in isolation, and can be maintained by a different team. The parent graph treats the entire subgraph as a black box with a single entry and exit point.

**Caveat / contested:** Shared state keys create implicit coupling between parent and subgraph — renaming a key in one breaks the other silently at runtime rather than at compile time. Isolated state schemas with explicit transformation nodes are more verbose but easier to evolve independently.

**Sources:** [dev.to/sreeni5018 — LangGraph Subgraphs: A Guide to Modular AI Agents Development](https://dev.to/sreeni5018/langgraph-subgraphs-a-guide-to-modular-ai-agents-development-31ob) (fetched 2026-07-20) · medium.com/fundamentals-of-artificial-intelligence — Subgraph in LangGraph (fetched 2026-07-20) · [aipractitioner.substack.com — Scaling LangGraph Agents: Parallelization, Subgraphs, and Map-Reduce Trade-Offs](https://aipractitioner.substack.com/p/scaling-langgraph-agents-parallelization) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use `stream_mode="messages"` for token-by-token output; use `stream_mode="updates"` for step visibility

**Do:** When building a chat UI that needs tokens to appear word-by-word, call `graph.astream(..., stream_mode="messages")` — this yields `(message_chunk, metadata)` tuples as the LLM produces them. To show the user what step the agent is on (e.g., "calling tool X"), use `stream_mode="updates"` which yields state deltas after each node completes. Combine modes: `stream_mode=["messages", "updates"]` works in LangGraph ≥1.1 with the v2 stream format.

Reserve `astream_events(version="v2")` for cases where you need every internal callback event — individual tokens deep inside nested subgraphs, tool invocations, LangSmith spans. It is the most powerful but also the most verbose API. Always pass `version="v2"` — the v1 format is inconsistent and being phased out.

**Why (beginner):** Without streaming, the user stares at a blank screen while the LLM generates — often 5–30 seconds. Even a simple spinner powered by `stream_mode="updates"` is a big UX improvement.

**Caveat / contested:** ⚠️ **WARNING — Python < 3.11 async limitation:** `get_stream_writer()` (for emitting custom data from nodes in `stream_mode="custom"`) is not available in async contexts on Python 3.10. Pass the writer as an explicit function parameter instead. 🕒 **verify live** — LangGraph 1.2.x introduced a content-block-centric streaming API (v3) as beta — treat as unstable until it reaches stable status; no independent third-party write-up confirmed as of grading date.

**Sources:** [docs.langchain.com/oss/python/langgraph/streaming](https://docs.langchain.com/oss/python/langgraph/streaming) (fetched 2026-07-20) · [langchain.com/blog — From Token Streams to Agent Streams](https://www.langchain.com/blog/token-streams-to-agent-streams) (fetched 2026-07-20) · [stuart.mchattie.net — Streaming State and Tokens in LangGraph](https://stuart.mchattie.net/posts/2026/05/16/streaming-in-langgraph/) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: For multi-agent orchestration, start with a supervisor pattern; add peer-to-peer only when genuinely needed

**Do:** Build a supervisor node (an LLM or routing function) that receives the user request, decides which specialist agent to invoke next, and synthesizes the final answer. Each specialist is a subgraph or a set of nodes. Route using conditional edges or `Command(goto=...)` from the supervisor. Use a stronger model for the supervisor (e.g., Claude Sonnet 5 or an equivalent) and a lighter model for worker agents where reasoning depth is less critical.

**Why (beginner):** A supervisor gives you one clear point of control and makes failures easy to diagnose — if results are wrong, you look at the supervisor's routing decision first. Peer-to-peer "collaborative" patterns where agents pass messages directly to each other are the hardest architecture to debug and the easiest to get into an infinite loop. As one guide notes: "Don't start with multi-agent because it sounds sophisticated."

**Caveat / contested:** Supervisor patterns have a single point of failure: if the supervisor misroutes, everything downstream is wrong. For genuinely non-linear tasks (creative collaboration, iterative critique loops), peer-to-peer or Reflection/Critic Loop patterns (agent produces output → critic evaluates → agent revises) may be more natural. Cost awareness: each agent hop adds 1–3 seconds of latency and at least one additional LLM call.

**Sources:** medium.com/@timarkanta.sharma — Architecting Multi-Agent Systems with LangGraph (fetched 2026-07-20) · medium.com/cwan-engineering — Building Multi-Agent Systems with LangGraph (fetched 2026-07-20) · [latenode.com — LangGraph Multi-Agent Orchestration: Complete Framework Guide](https://latenode.com/blog/ai-frameworks-technical-infrastructure/langgraph-multi-agent-orchestration/langgraph-multi-agent-orchestration-complete-framework-guide-architecture-analysis-2025) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use LangSmith Deployment (managed cloud) for fast prototyping; self-host for data privacy or cost control

**Do:** If you need to ship quickly and have no data-residency constraints, use LangSmith Deployment's managed Cloud SaaS tier — it provides 1-click GitHub deployment, autoscaling up to 10 containers, and a 30-endpoint REST API. For regulated industries, cost-sensitive workloads, or when you want to route nodes to a local model server (e.g., vLLM on localhost), self-host using the open-source LangGraph server.

**Why (beginner):** The managed cloud eliminates the need to provision Postgres, Redis, and container infrastructure yourself.

**Caveat / contested:** ⚠️ **WARNING — looping costs on managed deployment:** a multi-agent graph running in a loop can execute thousands of nodes very quickly. At $0.001/node, an uncapped loop is expensive. Set hard turn and cost limits in your graph before deploying. 🕒 **verify live** — the $0.001/node and $39/user/month LangSmith Plus figures were from a blog post (ZenML, fetched 2026-07-20); check the LangSmith pricing page at [langchain.com/langsmith](https://www.langchain.com/langsmith) before committing. The product was renamed from "LangGraph Cloud" → "LangGraph Platform" → **"LangSmith Deployment"** (and LangGraph Studio → LangSmith Studio) as of October 2025; this rename is complete, not partial. Documentation under older names may still be found in search results. Self-hosting requires managing Postgres + Redis yourself; factor in operational cost. BYOC (Bring Your Own Cloud) is Enterprise-tier only. Autoscaling up to 10 containers is noted in cohorte.co's deployment guide (fetched 2026-07-20) — verify against live LangSmith docs.

**Sources:** [langchain.com/blog — LangGraph Platform is now Generally Available](https://www.langchain.com/blog/langgraph-platform-ga) (fetched 2026-07-20) · [zenml.io/blog — LangGraph Pricing Guide](https://www.zenml.io/blog/langgraph-pricing) (fetched 2026-07-20) · [cohorte.co — Navigating LangGraph's Deployment Landscape](https://cohorte.co/blog/navigating-langgraphs-deployment-landscape-picking-the-right-fit-for-your-ai-projects) (fetched 2026-07-20) · [changelog.langchain.com — Product naming changes: LangSmith Deployment](https://changelog.langchain.com/announcements/product-naming-changes-langsmith-deployment-and-langsmith-studio) (found via live search, 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use LangMem for cross-session long-term memory, but not for latency-sensitive user-facing agents

**Do:** Add LangMem on top of LangGraph's `BaseStore` to give your agent persistent memory across separate sessions. Use `create_manage_memory_tool` and `create_search_memory_tool`, pass them to `create_agent` (note: was `create_react_agent` pre-1.0, now in `langchain.agents`), and configure the store with an embedding index (required for semantic search — an embedding index converts text into vectors for similarity search). For development, use `InMemoryStore`; swap to `PostgresStore` for production. Namespace memories by user ID, not thread ID, so that memories survive across conversation threads.

LangMem supports three memory types: **semantic** (facts and user preferences), **episodic** (past interaction examples), and **procedural** (agent-rewritten system prompt instructions that evolve over time).

**Why (beginner):** LangGraph's checkpointer gives short-term, thread-scoped memory. LangMem gives long-term, cross-session memory — the agent remembers that this user prefers concise answers, even a week later on a new thread.

**Caveat / contested:** ⚠️ **WARNING — latency.** One independent benchmark (Atlan, fetched 2026-07-20) reports LangMem p95 latency at 59.82 seconds on memory consolidation workloads (LOCOMO benchmark). The guide explicitly states: do not deploy for interactive user-facing agents. Alternatives like Mem0 (0.200s p95) or Zep are better for real-time applications. LangMem is better suited to background processing jobs that run after a conversation ends. LangMem version 0.0.30 (October 2025) is still pre-1.0 as of this research date — API may change. 🕒 **verify live** — version may have advanced.

**Sources:** [langchain-ai.github.io/langmem/concepts/conceptual_guide/](https://langchain-ai.github.io/langmem/concepts/conceptual_guide/) (fetched 2026-07-20) · [atlan.com — Long-Term Memory LangChain Agents: LangGraph and LangMem Guide](https://atlan.com/know/long-term-memory-langchain-agents/) (fetched 2026-07-20) · medium.com/@astropomeai — LangMem: Long-Term Memory for AI Agents (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated (latency warning; core integration pattern is vendor-documented)

---

## Practice: Migrate from `langgraph.prebuilt` to `langchain.agents`; pin your version and test before upgrading

**Do:** If you are using anything from `langgraph.prebuilt` (e.g., `create_react_agent` imported from there), migrate those imports to `langchain.agents` — this is the primary breaking change in LangGraph 1.0 (October 22, 2025). Note that the function was also renamed: `create_react_agent` → `create_agent`, and the `prompt` parameter was renamed to `system_prompt`. To upgrade:

```
pip install --upgrade langgraph       # standard
# or, if you use uv: uv pip install --upgrade langgraph
```

Pin to a specific minor version in production (`langgraph==1.2.9`) and run your full test suite before upgrading, because at least two patch releases were yanked in 2026 for regressions (1.2.3 for a merging strategy regression; 1.1.7 for a custom callback handler bug).

**Why (beginner):** LangGraph maintained full backward compatibility at 1.0 except for this deprecation. However, the PyPI release history shows yanked patch releases — versions that were pulled after causing bugs. Using a pinned, known-good version in production and upgrading deliberately (not automatically) protects you from these.

**Caveat / contested:** The migration from `create_react_agent` (in `langgraph.prebuilt`) to `create_agent` (in `langchain.agents`) is a deprecation — it issues a warning before breaking — but using the old `prompt=` keyword argument with the new function will produce a TypeError. Fix: rename `prompt=` to `system_prompt=` in the same change. The yanked-version reasons come from brief PyPI release notes, not detailed post-mortems; scope of impact of the yanked releases is not fully characterized. 🕒 **verify live** before upgrading any minor version in production.

**Sources:** [pypi.org/project/langgraph/](https://pypi.org/project/langgraph/) (fetched 2026-07-20) · [langchain.com/blog — LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones](https://www.langchain.com/blog/langchain-langgraph-1dot0) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented (1.0 migration facts)

---

## Held pending fixes (not publish-ready)

- LangGraph 1.2.x streaming v3 API (content-block-centric) — marked beta at time of research; no independent third-party write-up found. ⚠ PENDING
- LangMem p95 latency benchmark methodology — single source (Atlan); benchmark conditions and date not fully specified. ⚠ PENDING
- LangSmith Deployment exact current pricing — check [langchain.com/langsmith](https://www.langchain.com/langsmith) before committing. ⚠ PENDING

## CHANGELOG (grading → this entry)

1. **Skeptic KILL:** Pydantic "validation fires only on inputs to the first node" claim removed — not found in any of the four fetched sources including two official LangGraph docs pages. The surrounding recommendation (TypedDict inside, Pydantic at boundaries) remains.
2. **Skeptic FIX:** jamesbmour "quote" converted from quotation marks to a paraphrase (the original text was not verbatim-matched on the page).
3. **Skeptic FIX:** "10 containers" autoscaling attributed to cohorte.co (not the GA blog, which does not give a container count).
4. **Skeptic FLAG:** interrupt() "successor" framing — changed to "simpler pattern introduced in December 2024" without attributing the "successor" label to the blog post.
5. **Timekeeper KILL-L1:** "LangGraph Platform" → "LangSmith Deployment" throughout; rename described as complete (not partial). Changelog.langchain.com source added.
6. **Timekeeper KILL-L3:** Migration section now specifies that `create_react_agent` → `create_agent` (function renamed) and `prompt=` → `system_prompt=` (parameter renamed). Using old names with new function produces a TypeError.
7. **Timekeeper FIX-L2:** Pricing page URL now directs to LangSmith pricing page.
8. **Timekeeper FIX-L4:** LangMem 0.0.30 version line marked `verify live`.
9. **Beginner KILL-L1:** Prerequisites section added (Python version, LangGraph install, API key, billing cap).
10. **Beginner KILL-L2:** InMemorySaver "ephemeral by design" now states "state is gone forever when the server stops."
11. **Beginner KILL-L3:** interrupt() try/except consequence upgraded to "bypassing your human oversight gate completely."
12. **Beginner KILL-L4:** Cost WARNING added to LangSmith Deployment section (looping graphs can execute thousands of nodes).
13. **Beginner KILL-L5:** interrupt() side-effect re-execution elevated from caveat to ⚠️ WARNING label.
14. **Beginner FIX-L9:** Migration command now uses `pip install --upgrade langgraph` as primary; uv given as alternative.
15. **Beginner FIX-L4:** thread_id usage now includes `str(uuid.uuid4())` example and warning about sharing IDs across users.
16. **Link-check gate:** 7 Medium.com URLs returned 403 (Cloudflare bot-protection; pages confirmed live via WebFetch). Unlinked to plain text per policy (8 occurrences total across 7 unique URLs): medium.com/cwan-engineering, medium.com/@shuv.sdr, medium.com/@vignesh_2710, medium.com/@areebahmed575, medium.com/fundamentals-of-artificial-intelligence, medium.com/@timarkanta.sharma, medium.com/@astropomeai. Citations retained.

