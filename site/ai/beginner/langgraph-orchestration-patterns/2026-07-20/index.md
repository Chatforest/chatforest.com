# AI Agent Orchestration — LangGraph — Beginner Guide (as of 20 Jul 2026)

> A plain-language guide to building AI agent workflows with LangGraph: how to store state safely, pause for human approval, remember things across conversations, and avoid the mistakes that cost money or lose data.


<!-- content/ai/beginner/langgraph-orchestration-patterns/2026-07-20/index.md — IMMUTABLE snapshot.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented = official vendor docs only. -->

# AI Agent Orchestration — LangGraph — Beginner Guide (as of 20 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **20 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

**What is LangGraph?** LangGraph is an open-source Python library for building AI agents that follow a defined sequence of steps. Think of it as a flowchart engine where each box ("node") can call an AI model, run a tool, or wait for a human to respond. The flowchart is called a **graph**, and the data that flows through it is called **state**.

**Current stable version:** LangGraph 1.2.9 (released 10 Jul 2026, requires Python 3.10 or newer, free and open-source). 🕒 **verify live**

**LangGraph 1.0 GA:** October 22, 2025 — first stable major release. Key migration notes are in the final section.

## Before you start — things you must have

- **Python 3.10 or newer** on your machine. Some async (background-task) features need Python 3.11 or newer — see the streaming section.
- **Install LangGraph** by running `pip install langgraph` in your terminal, or `pip install --upgrade langgraph` if you already have an older version.
- **An LLM provider API key** — for example, `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`. An API key is a password that lets your code call an AI model over the internet.
- **Set a spending limit.** LLM calls cost real money. Before running any code that calls an AI model, go to your provider's billing dashboard and set a hard spending cap. A runaway loop can generate a large bill in minutes.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers agree
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value before trusting it

---

## Practice: Define your graph's data using TypedDict; save Pydantic for data coming from outside

**What is "state"?** Every node in LangGraph reads and writes a shared Python dictionary called **state**. You define its shape (which keys exist, what type each value is) before building the graph.

**Do:** Define your `StateGraph` schema — the blueprint for your state dictionary — using Python's built-in `TypedDict`. Only use Pydantic's `BaseModel` at the edges of your system: when data arrives from a user form, an API call, or a database read that you do not control.

A minimal example of a TypedDict state:

```python
from typing import TypedDict

class AgentState(TypedDict):
    messages: list
    user_id: str
```

**Why (beginner):** `TypedDict` gives your code editor live warnings when you pass the wrong kind of data (for example, a number where a string is expected), at no extra cost when your program runs. Pydantic does the same checks but also checks every value at runtime, which is useful when you cannot trust the incoming data. Inside the graph, all nodes are code you wrote, so the extra runtime cost of Pydantic is usually wasted. Use the right tool for the right place.

**Caveat / contested:** Some practitioners recommend Pydantic everywhere for stricter guarantees. One independent guide (Easton Dev, Apr 2026) explicitly recommends Pydantic with `extra='forbid'` to stop unexpected fields from sneaking into state. The community consensus — TypedDict inside the graph, Pydantic at the edges — is a pragmatic middle ground, not an official rule from the LangGraph docs.

**Sources:** [shazaali.substack.com — Type Safety in LangGraph: When to Use TypedDict vs. Pydantic](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to) (fetched 2026-07-20) · [eastondev.com — LangGraph Agent Architecture](https://eastondev.com/blog/en/posts/ai/20260424-langgraph-agent-architecture/) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use reducers to merge results when two nodes write to the same field at the same time

**What is a "reducer"?** A reducer is a small function that tells LangGraph how to combine two values for the same state field when more than one node writes to it simultaneously. Without a reducer, one result silently overwrites the other.

**Do:** When you build a graph where multiple nodes run at the same time (for example, two parallel web searches), annotate any shared field with a reducer using Python's `Annotated` type. LangGraph ships a built-in reducer called `add_messages` for conversation message lists. For your own data types, write a custom reducer.

```python
from typing import Annotated
import operator
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]   # built-in: merges and deduplicates messages
    search_results: Annotated[list, operator.add]  # custom: concatenates two lists
```

**Why (beginner):** LangGraph runs sibling nodes in a "superstep" — concurrently, like two workers doing tasks side by side. Without a reducer, whichever worker finishes last wins and the earlier result is thrown away silently. `add_messages` also deduplicates by message ID, which prevents ghost duplicate messages if you ever replay from a saved checkpoint. LangGraph will not warn you if you forget a reducer — the data loss is silent.

**Caveat / contested:** `add_messages` only works with LangChain's `HumanMessage` / `AIMessage` objects. For anything else — plain dictionaries, numbers, domain objects — you must write your own reducer. Forgetting to do this when nodes run in parallel is a silent data-loss bug.

**Sources:** medium.com/cwan-engineering — Building Multi-Agent Systems with LangGraph (fetched 2026-07-20) · [eastondev.com — LangGraph Agent Architecture](https://eastondev.com/blog/en/posts/ai/20260424-langgraph-agent-architecture/) (fetched 2026-07-20) · [aipractitioner.substack.com — Scaling LangGraph Agents: Parallelization, Subgraphs, and Map-Reduce Trade-Offs](https://aipractitioner.substack.com/p/scaling-langgraph-agents-parallelization) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use fixed edges when the next step is always the same; use conditional edges when the next step depends on what just happened

**What is an "edge"?** An edge is a connection between two nodes in the graph. It tells LangGraph "after node A finishes, go to node B." Without edges, the graph does not know what to do next.

**Do:** Use a **fixed edge** when node A always leads to node B, no exceptions:

```python
graph.add_edge("node_a", "node_b")
```

Use a **conditional edge** when the next step depends on what the AI model decided — for example, whether it wants to call a tool or give a final answer:

```python
def route(state):
    if state["needs_tool"]:
        return "tool_node"
    return "end"

graph.add_conditional_edges("ai_node", route, {"tool_node": "tool_node", "end": END})
```

The routing function receives the current state and returns a key that maps to the next node.

**Why (beginner):** Fixed edges are simpler, faster, and show up clearly in LangGraph Studio's visual debugger. Conditional edges are what make an agent "intelligent" — they let the graph branch based on what the AI decided. Using a conditional edge where a fixed one would work adds complexity for no benefit.

**Caveat / contested:** A newer pattern called `Command` lets a node return `Command(goto="next_node")` directly, replacing the need to declare conditional edges at build time. Multiple independent sources describe this as cleaner for human-in-the-loop flows, but it makes the graph structure less visible because edges are no longer listed in one place. Both patterns are supported by LangGraph.

**Sources:** [docs.langchain.com/oss/python/langgraph/interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) (fetched 2026-07-20) · medium.com/@shuv.sdr — LangGraph Architecture and Design (fetched 2026-07-20) · [dev.to/jamesbmour — Interrupts and Commands in LangGraph](https://dev.to/jamesbmour/interrupts-and-commands-in-langgraph-building-human-in-the-loop-workflows-4ngl) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Choose the right checkpointer for your stage — and never use InMemorySaver in production

**What is a "checkpointer"?** A checkpointer saves a complete snapshot of the graph's state after every node runs. This is how the agent remembers what happened, survives a server restart, and can be paused and resumed. Without a checkpointer, every call to the graph starts completely fresh — no memory, no recovery.

**Do:** Pick the checkpointer that matches where you are:

| Stage | Checkpointer | What it means |
|---|---|---|
| Writing tests / throwaway demo | `InMemorySaver` | Zero setup. State disappears when the process stops. |
| Local development where you want durability | `SqliteSaver` | Saves to a file. Survives restarts. One writer at a time only. |
| Production (real users, multiple workers) | `PostgresSaver` / `AsyncPostgresSaver` | Handles many simultaneous users. Durable. Queryable. |

Pass the checkpointer when you compile the graph:

```python
from langgraph.checkpoint.memory import InMemorySaver
import uuid

checkpointer = InMemorySaver()   # swap for SqliteSaver or PostgresSaver in real deployments
graph = my_graph_builder.compile(checkpointer=checkpointer)

# Always give each conversation its own unique thread_id
config = {"configurable": {"thread_id": str(uuid.uuid4())}}
result = graph.invoke({"messages": [...]}, config=config)
```

**Why (beginner):** The checkpointer is what turns a one-shot script into a real agent. Without it, a crash at step 5 of a 10-step workflow means starting from scratch. The difference between `InMemorySaver` and `PostgresSaver` is the difference between "works in a notebook demo" and "works when your server reboots at 3 AM."

**Caveat / contested:**

⚠️ **WARNING — InMemorySaver in production:** state is gone forever when the server stops. Every conversation history stored in memory disappears on every server restart. Real users lose their data. Do not use it in production.

⚠️ **WARNING — do not reuse the same thread_id across different users.** Each `thread_id` is a shared state bucket. If two users share a thread_id, they will see each other's conversation history. Generate a fresh `str(uuid.uuid4())` for every new conversation.

⚠️ **WARNING — SqliteSaver is single-writer only.** It uses a serialized write lock. If two users hit your server at the same time, one write will fail. Do not use SqliteSaver for any server that handles more than one user at a time.

Additional caveat: the official docs note that `thread_id` values must be kept under 255 characters when using PostgresSaver. Concatenating long user IDs and session IDs without checking length is a silent production bug. Checkpoints also accumulate indefinitely — prune old checkpoints periodically to prevent unbounded database growth.

**Sources:** [docs.langchain.com/oss/python/langgraph/persistence](https://docs.langchain.com/oss/python/langgraph/persistence) (fetched 2026-07-20) · [sparkco.ai — Mastering LangGraph Checkpointing: Best Practices for 2025](https://sparkco.ai/blog/mastering-langgraph-checkpointing-best-practices-for-2025) (fetched 2026-07-20) · medium.com/@vignesh_2710 — What is a Checkpointer in LangGraph (fetched 2026-07-20) · [eastondev.com — LangGraph Agent Architecture](https://eastondev.com/blog/en/posts/ai/20260424-langgraph-agent-architecture/) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use `interrupt()` to pause your agent and wait for a human; treat `interrupt_before` / `interrupt_after` as debugging tools only

**What is "human-in-the-loop"?** Human-in-the-loop (HITL) means the agent stops mid-workflow and waits for a person to approve, correct, or supply something before continuing. A common example: the agent is about to send an email — pause and ask the user "Is this OK to send?"

**The default path — use `interrupt()`:**

Call `interrupt(payload)` inside a node function. The graph pauses, saves its state (a checkpointer is required for this), and returns the payload to whatever code called the graph. When the human responds, resume the graph by passing `Command(resume=user_response)` on the next invocation.

```python
from langgraph.types import interrupt, Command

def review_node(state):
    # Pause here and send the draft to the human
    human_decision = interrupt({"draft": state["draft_email"]})
    # Execution resumes here after the human responds
    if human_decision["approved"]:
        return {"send": True}
    return {"send": False}
```

To resume after the human approves:

```python
result = graph.invoke(Command(resume={"approved": True}), config=config)
```

**For debugging only:** use `graph.compile(interrupt_before=["node_name"])` or `interrupt_after` to set static breakpoints when stepping through your graph to find bugs. The official docs explicitly say these are "not recommended for human-in-the-loop workflows."

**Why (beginner):** `interrupt()` was introduced in December 2024 as a simpler way to add human oversight. It lets you place multiple pause points inside one node, pass structured data as the pause message, and dynamically change where the graph goes next after the human responds.

**Caveat / contested:**

⚠️ **WARNING — do not wrap `interrupt()` in a bare `try/except` block.** `interrupt()` works by raising a special internal signal that LangGraph catches to pause execution. If you write a broad `except Exception:` block around it, Python catches and swallows that signal before LangGraph can see it. The result: your agent continues without pausing for approval, bypassing your human oversight gate completely. This is a silent safety failure — the code runs, but the human check never happens.

⚠️ **WARNING — side effects before `interrupt()` re-execute on resume.** When a graph resumes after an interrupt, the entire node restarts from the beginning. Any code that already ran before the `interrupt()` call — sending an email, charging a credit card, writing a database record — will run again. This causes duplicate emails, double charges, and duplicate database records. Design nodes so that side effects happen after the `interrupt()` call, not before it.

**Sources:** [docs.langchain.com/oss/python/langgraph/interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) (fetched 2026-07-20) · [langchain.com/blog — Making it Easier to Build Human-in-the-Loop Agents with interrupt](https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt) (fetched 2026-07-20) · medium.com/@areebahmed575 — LangGraph's interrupt() Function (fetched 2026-07-20) · [dev.to/jamesbmour — Interrupts and Commands in LangGraph](https://dev.to/jamesbmour/interrupts-and-commands-in-langgraph-building-human-in-the-loop-workflows-4ngl) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Build large workflows by composing subgraphs; each subgraph is a self-contained mini-graph

**What is a "subgraph"?** A subgraph is a complete, compiled `StateGraph` that you plug into a parent graph as if it were a single node. The parent graph does not see the internal steps — it just calls the subgraph and gets back a result.

**Do:** When a group of agents belongs together (for example, a research team made of a planner, a searcher, and a synthesizer), compile them as their own `StateGraph` and add that compiled graph as a node in the parent. If the parent and subgraph share at least one state field with the same name and type, LangGraph passes data automatically. When the state shapes are different, write a wrapper node — a plain Python function — that translates the parent's state into what the subgraph expects, calls the subgraph, and translates the result back.

**Why (beginner):** Subgraphs keep large workflows manageable. Each subgraph compiles and tests independently — you can run it in isolation before wiring it into the parent. The parent graph treats the entire subgraph as a black box with a single entry and exit point.

**Caveat / contested:** Shared state field names create hidden coupling. If you rename a field in the parent graph, the subgraph silently stops receiving that data at runtime — there is no compile-time error. Using separate state schemas with explicit translation nodes is more typing but easier to change later.

**Sources:** [dev.to/sreeni5018 — LangGraph Subgraphs: A Guide to Modular AI Agents Development](https://dev.to/sreeni5018/langgraph-subgraphs-a-guide-to-modular-ai-agents-development-31ob) (fetched 2026-07-20) · medium.com/fundamentals-of-artificial-intelligence — Subgraph in LangGraph (fetched 2026-07-20) · [aipractitioner.substack.com — Scaling LangGraph Agents: Parallelization, Subgraphs, and Map-Reduce Trade-Offs](https://aipractitioner.substack.com/p/scaling-langgraph-agents-parallelization) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Stream tokens word-by-word for chat UIs; stream step updates to show progress

**What is "streaming"?** By default, LangGraph returns the agent's full response only after every step finishes — the user stares at a blank screen for 5–30 seconds. Streaming sends partial results as they are produced.

**The two modes to know first:**

- `stream_mode="messages"` — yields tokens one by one as the AI model generates them. Use this for a chat interface where you want words to appear as the AI "types." Returns `(message_chunk, metadata)` tuples.
- `stream_mode="updates"` — yields the state change after each node finishes. Use this to show the user "now searching the web…" or "now writing the summary…" as the agent progresses through steps.

Call the async streaming method (`astream`) for production code:

```python
async for chunk in graph.astream({"messages": [...]}, config=config, stream_mode="updates"):
    print(chunk)
```

You can combine both modes in LangGraph 1.1 or newer:

```python
stream_mode=["messages", "updates"]
```

For the most detail — every internal callback, every token deep inside a nested subgraph — use `astream_events(version="v2")`. Always pass `version="v2"`; the v1 format is being phased out.

**Why (beginner):** Even a simple "step indicator" powered by `stream_mode="updates"` is a large improvement over a blank screen. For a chat UI, `stream_mode="messages"` makes the agent feel fast and responsive even when the underlying model is slow.

**Caveat / contested:** ⚠️ **WARNING — Python 3.10 async limitation:** `get_stream_writer()` (used for sending custom data from inside a node with `stream_mode="custom"`) does not work in async contexts on Python 3.10. Pass the writer as an explicit function parameter instead of using the global helper. If you need `stream_mode="custom"`, upgrade to Python 3.11. 🕒 **verify live** — LangGraph 1.2.x introduced a new content-block-centric streaming API (v3) as a beta feature. It is unstable; no independent write-up confirmed its stability as of the grading date. Do not build production code on it yet.

**Sources:** [docs.langchain.com/oss/python/langgraph/streaming](https://docs.langchain.com/oss/python/langgraph/streaming) (fetched 2026-07-20) · [langchain.com/blog — From Token Streams to Agent Streams](https://www.langchain.com/blog/token-streams-to-agent-streams) (fetched 2026-07-20) · [stuart.mchattie.net — Streaming State and Tokens in LangGraph](https://stuart.mchattie.net/posts/2026/05/16/streaming-in-langgraph/) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: When building a multi-agent system, start with a supervisor pattern — one agent in charge, others as specialists

**What is a "multi-agent system"?** A multi-agent system is a graph where multiple AI agents work together. One common shape is the supervisor pattern: one "manager" agent reads the user's request, decides which specialist to call, and assembles the final answer.

**Do:** Build a supervisor node — either an LLM call or a routing function — that receives the user's request, picks which specialist agent to call next, and synthesizes the final answer. Each specialist is either a subgraph or a set of nodes. Route between them using conditional edges or `Command(goto=...)` from the supervisor. Use a stronger AI model for the supervisor (for example, Claude Sonnet 5 or an equivalent) and a lighter, cheaper model for worker agents where deep reasoning is less important.

**Why (beginner):** A supervisor gives you one clear place to look when something goes wrong. If the agent produces a wrong answer, you check the supervisor's routing decision first. The alternative — peer-to-peer patterns where agents pass messages directly to each other in any order — is the hardest architecture to debug and the easiest to accidentally turn into an infinite loop. As one guide puts it: "Don't start with multi-agent because it sounds sophisticated."

**Caveat / contested:** A supervisor is a single point of failure — if it misroutes the request, everything downstream is wrong. For tasks that are genuinely non-linear (creative collaboration, iterative critique loops), peer-to-peer or Reflection/Critic Loop patterns may be more natural. Cost awareness: each agent hand-off adds 1–3 seconds of latency and at least one extra LLM call, which costs money.

**Sources:** medium.com/@timarkanta.sharma — Architecting Multi-Agent Systems with LangGraph (fetched 2026-07-20) · medium.com/cwan-engineering — Building Multi-Agent Systems with LangGraph (fetched 2026-07-20) · [latenode.com — LangGraph Multi-Agent Orchestration: Complete Framework Guide](https://latenode.com/blog/ai-frameworks-technical-infrastructure/langgraph-multi-agent-orchestration/langgraph-multi-agent-orchestration-complete-framework-guide-architecture-analysis-2025) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use LangSmith Deployment for fast prototyping; self-host when you need data privacy or lower costs

**What is LangSmith Deployment?** LangSmith Deployment is Langchain's managed cloud service for running LangGraph agents in production. It handles the servers, database, and scaling for you. (Note: this product was previously named "LangGraph Cloud" and then "LangGraph Platform" before being renamed "LangSmith Deployment" in October 2025. The rename is complete. Old names may still appear in search results.)

**Do:** If you want to ship quickly and have no rules about where your data must live, use LangSmith Deployment's managed Cloud SaaS tier. It provides one-click GitHub deployment, autoscaling up to 10 containers, and a 30-endpoint REST API — no need to set up your own Postgres database, Redis cache, or container infrastructure.

If you work in a regulated industry, have data-residency requirements, or want to run the AI model on your own hardware (for example, vLLM running on your own server), self-host the open-source LangGraph server instead.

**Why (beginner):** The managed cloud removes the biggest operational burden for a beginner: you do not need to configure and maintain a production database and container cluster. You write the agent code; Langchain runs the infrastructure.

**Caveat / contested:**

⚠️ **WARNING — looping graphs can generate large bills on managed deployment.** A multi-agent graph running in a loop can execute thousands of nodes very quickly. At $0.001 per node, an uncapped loop is expensive. Set hard turn limits and cost limits in your graph before deploying to LangSmith Deployment.

🕒 **verify live** — the $0.001/node and $39/user/month LangSmith Plus figures came from a blog post (ZenML, fetched 2026-07-20). Check the current pricing at [langchain.com/langsmith](https://www.langchain.com/langsmith) before committing to any paid tier.

Additional notes: self-hosting requires you to manage Postgres and Redis yourself — factor in that operational cost. BYOC (Bring Your Own Cloud, where Langchain runs on infrastructure in your own cloud account) is an Enterprise-tier-only feature. The autoscaling figure of up to 10 containers comes from a third-party deployment guide (cohorte.co, fetched 2026-07-20) — verify against the live LangSmith docs.

**Sources:** [langchain.com/blog — LangGraph Platform is now Generally Available](https://www.langchain.com/blog/langgraph-platform-ga) (fetched 2026-07-20) · [zenml.io/blog — LangGraph Pricing Guide](https://www.zenml.io/blog/langgraph-pricing) (fetched 2026-07-20) · [cohorte.co — Navigating LangGraph's Deployment Landscape](https://cohorte.co/blog/navigating-langgraphs-deployment-landscape-picking-the-right-fit-for-your-ai-projects) (fetched 2026-07-20) · [changelog.langchain.com — Product naming changes: LangSmith Deployment](https://changelog.langchain.com/announcements/product-naming-changes-langsmith-deployment-and-langsmith-studio) (found via live search, 2026-07-20)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use LangMem for long-term memory across sessions — but not for live chat where the user is waiting

**What is LangMem?** LangGraph's built-in checkpointer gives your agent short-term memory within a single conversation thread. LangMem is an add-on library that gives your agent long-term memory across many separate conversations — for example, remembering that a specific user always prefers concise answers, even a week later on a completely new thread.

**What LangMem remembers:**
- **Semantic memory** — facts and user preferences ("this user is a Python developer")
- **Episodic memory** — examples of past interactions the agent can learn from
- **Procedural memory** — instructions that the agent rewrites into its own system prompt as it learns over time

**Do:** Add LangMem on top of LangGraph's `BaseStore`. Use `create_manage_memory_tool` and `create_search_memory_tool`, and pass them to `create_agent` (see the migration section for the correct import). Configure the store with an **embedding index** — this converts text into numbers (vectors) so the agent can search memories by meaning rather than exact words. For development, use `InMemoryStore`; swap to `PostgresStore` for production. Store memories under the user's ID, not the thread ID, so they survive across conversation threads.

**Why (beginner):** Without LangMem, your agent starts fresh every time a user opens a new conversation — no context about who they are or what they prefer. LangMem is what lets an agent say "You mentioned last week you prefer bullet points — here's that format."

**Caveat / contested:**

⚠️ **WARNING — LangMem is too slow for live conversations.** One independent benchmark (Atlan, fetched 2026-07-20) measured LangMem's p95 latency (the slowest 5% of requests) at **59.82 seconds** on memory consolidation tasks. That guide explicitly states: do not deploy LangMem for interactive user-facing agents. Use LangMem only for background jobs that run after a conversation ends (for example, a nightly memory-consolidation task). For real-time memory needs, alternatives like Mem0 (0.200s p95) or Zep are better choices.

LangMem version 0.0.30 (October 2025) is still pre-1.0 as of this snapshot — the API may change in a future release. 🕒 **verify live** — the version number may have advanced since this was written.

**Sources:** [langchain-ai.github.io/langmem/concepts/conceptual_guide/](https://langchain-ai.github.io/langmem/concepts/conceptual_guide/) (fetched 2026-07-20) · [atlan.com — Long-Term Memory LangChain Agents: LangGraph and LangMem Guide](https://atlan.com/know/long-term-memory-langchain-agents/) (fetched 2026-07-20) · medium.com/@astropomeai — LangMem: Long-Term Memory for AI Agents (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated (latency warning; core integration pattern is vendor-documented)

---

## Practice: If you used `create_react_agent`, migrate to `create_agent` — and pin your version before upgrading

**What changed?** LangGraph 1.0 (released October 22, 2025) moved and renamed the function used to build simple tool-calling agents:

| Old (before 1.0) | New (1.0 and later) |
|---|---|
| `from langgraph.prebuilt import create_react_agent` | `from langchain.agents import create_agent` |
| `create_react_agent(..., prompt="You are a helpful assistant")` | `create_agent(..., system_prompt="You are a helpful assistant")` |

**Do:** Update your import and rename both the function and the `prompt=` keyword argument to `system_prompt=`. Using the old `prompt=` keyword with the new `create_agent` function produces a `TypeError` at runtime.

To upgrade LangGraph:

```
pip install --upgrade langgraph
```

Or if you use uv:

```
uv pip install --upgrade langgraph
```

After upgrading, pin to the exact version that passes your tests in production:

```
langgraph==1.2.9
```

**Why (beginner):** LangGraph kept backward compatibility everywhere in 1.0 except this one deprecation. However, the PyPI release history shows that at least two patch releases in 2026 were yanked (pulled back) after causing bugs: version 1.2.3 (a merging strategy regression) and 1.1.7 (a custom callback handler bug). Pinning to a known-good version and upgrading deliberately — not automatically — protects you from landing on a yanked or broken release.

**Caveat / contested:** The old import (`from langgraph.prebuilt import create_react_agent`) issues a deprecation warning before it breaks — it will not silently fail on the first upgrade. However, using the old `prompt=` keyword with the new `create_agent` function will fail immediately with a `TypeError`. Fix both in the same change. The yanked-version notes come from brief PyPI release notes, not detailed post-mortems; the full scope of impact of those yanked releases is not fully characterized. 🕒 **verify live** before upgrading any minor version in production.

**Sources:** [pypi.org/project/langgraph/](https://pypi.org/project/langgraph/) (fetched 2026-07-20) · [langchain.com/blog — LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones](https://www.langchain.com/blog/langchain-langgraph-1dot0) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented (1.0 migration facts)

---

## Held pending fixes (not publish-ready)

- LangGraph 1.2.x streaming v3 API (content-block-centric) — marked beta at time of research; no independent third-party write-up found. ⚠ PENDING
- LangMem p95 latency benchmark methodology — single source (Atlan); benchmark conditions and date not fully specified. ⚠ PENDING
- LangSmith Deployment exact current pricing — check [langchain.com/langsmith](https://www.langchain.com/langsmith) before committing. ⚠ PENDING

## CHANGELOG

1. Re-leveled from the 2026-07-20 technical entry by rings-beginner-author; facts and URLs unchanged.
2. Added plain-language definitions before each practice ("What is a checkpointer?", "What is streaming?", etc.) to orient readers new to AI and the command line.
3. Added a complete minimal code example in each practice section where the technical entry had a concept but no inline example (TypedDict state, reducer annotation, fixed vs. conditional edges, checkpointer + thread_id, interrupt/resume, streaming astream call, migration table).
4. Led each practice with ONE clear default path; alternatives mentioned at the end of each section rather than interleaved.
5. Expanded "Why (beginner)" in every practice to name the concrete failure the practice prevents (lost conversation history, duplicate charges, bypassed approval gate, unexpected billing, etc.).
6. All six ⚠️ WARNINGs from the technical entry kept verbatim and promoted to their own labeled paragraphs for visibility.
7. All 🕒 verify live notes kept verbatim.
8. All Sources and Confidence labels kept verbatim — no URLs added, removed, or rewritten.
9. Subgraphs and multi-agent supervisor practices kept; no practices dropped as too advanced (all were made accessible through added definitions and examples).
10. **Link-check gate:** 7 Medium.com URLs returned 403 (Cloudflare bot-protection; pages confirmed live). Unlinked to plain text per policy (8 occurrences total): medium.com/cwan-engineering, medium.com/@shuv.sdr, medium.com/@vignesh_2710, medium.com/@areebahmed575, medium.com/fundamentals-of-artificial-intelligence, medium.com/@timarkanta.sharma, medium.com/@astropomeai. Citations retained.

