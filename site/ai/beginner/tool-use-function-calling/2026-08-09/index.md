# Tool Use & Function-Calling Design Patterns for AI Agents — Best Practices (as of 09 Aug 2026)

> A plain-language guide to how AI agents call tools/functions safely: start with the safety rules that matter no matter which AI vendor you use (sandboxing, least privilege, prompt-injection risk, cost surprises), then a short, brief look at Claude's and OpenAI's specific tool-calling mechanics.


<!-- This file lands at content/ai/beginner/tool-use-function-calling/2026-08-09/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a
     NEW <snapshot-date> dir. "Latest" is computed by Grove's template from snapshot_date;
     do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source).
     This is the BEGINNER re-leveling of the technical entry at
     content/ai/best-practices/tool-use-function-calling/2026-08-09/index.md — same facts,
     same sources, simpler language and different ordering. -->

# Tool Use & Function-Calling Design Patterns for AI Agents (as of 09 Aug 2026)

> **Grading note.** This is the beginner-track version of a dated snapshot, accurate as of
> **09 Aug 2026**. It's a re-write of an already fact-checked technical entry: three researchers
> drafted the original material, a Skeptic panelist re-fetched 45 source links and removed
> anything it couldn't verify, a Beginner panelist checked it for missing safety warnings, and a
> Timekeeper panelist checked it for staleness — **0 fabrications after correction**. This
> beginner version changes only the reading level, the order of topics, and how much depth is
> shown up front — it adds no new facts, no new claims, and touches no links. Items that
> genuinely couldn't be verified are marked **⚠ PENDING** in the technical entry; this corpus
> never publishes unverified content.

## How to read the labels
- ✅ **independently-corroborated** — confirmed by 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value yourself

**Two terms that come up a lot below.** A **JSON Schema** is just a description of what shape of
data is valid — which fields exist, what type each one is, and which ones are required. It's how
you tell an AI model exactly what a tool's inputs must look like. **MCP (Model Context
Protocol)** is an open standard for exposing tools to an AI model in a way that works across
different AI vendors, instead of hand-building a separate connection for every vendor's API.

## Where to start

This topic covers **three different things**: Anthropic's Claude, OpenAI's models, and patterns
that apply no matter which one you use. That's a lot to take in at once, so here's the shortcut:
**you don't need to pick a vendor before you learn the safety rules.** The rules in Part 1 below
— sandbox anything that runs code, give tools the least access they need, keep a human in the
loop for risky actions, never trust what a tool reads back — apply exactly the same whether your
agent is built on Claude, OpenAI, or something else entirely. Learn those first. Part 2 covers how
to design a tool well, which is also mostly vendor-neutral. Part 3, at the end, is a short,
deliberately brief look at the handful of places where Claude's API and OpenAI's API actually work
differently — skim whichever one matches what you're building, and skip the other for now.

---

## Part 1 — Start here: safety rules that apply no matter which AI vendor you use

### Practice: ⚠️ WARNING — sandbox anything that runs code, a shell command, or controls a computer
**Do:** Some AI tools don't just answer questions — they run code, run shell commands, or click
around on a real computer screen. Treat every one of these as "the model can execute arbitrary
actions on a real machine or account" and isolate it accordingly. The minimum, beginner-friendly
baseline: run the tool inside a plain container with **no network access** and a **disposable,
non-root user** — never point a code-execution, shell, or computer-use tool directly at your own
machine or a real account. Never give the model access to real account logins or secrets; if
credentials never enter the sandbox in the first place, they can't be stolen out of it, no matter
whether the cause was an honest model mistake, the model "creatively" working around a
restriction, or a deliberate attack. If you need real capability beyond the minimum baseline,
stronger isolation exists (a dedicated VM, or technologies like gVisor or Firecracker/Kata
microVMs), plus an allowlist of exactly which outbound network domains the tool can reach, plus a
required human-confirmation step before anything with real-world consequences (payments, agreeing
to terms of service, and — reasonably — anything destructive like deleting data). This applies
equally to Claude's bash/computer-use tools and to OpenAI's Responses API code-interpreter and
computer-use tools — the safety requirements don't change just because the tool is presented as
newer or more capable.
**Why (beginner):** A code-execution or computer-use tool is arbitrary code or UI control on a
real machine. Without isolation, a hallucinated command, a prompt-injected instruction (see
below), or a plain model mistake can delete files, run up a cloud bill, or leak secrets — with no
undo button. And don't assume a "please confirm this action" popup alone will save you: one study
Anthropic cites found people approve roughly 93% of permission prompts, with attention declining
the longer a session runs ("approval fatigue") — so isolation is the primary defense, and a
confirmation prompt is a secondary layer on top of it, not a replacement for it.
**Caveat / contested:** Companies that sell sandboxing infrastructure are among the sources for
the stronger-isolation options here, so treat their specific product comparisons skeptically —
the underlying principle (isolate untrusted execution, default-deny network access) is sound and
echoed by independent security guidance (OWASP, below) either way.
**Sources:** [platform.claude.com/docs — Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) (fetched 9 Aug 2026) · [anthropic.com/engineering — How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude) (published 25 May 2026) · [simonwillison.net — commentary on "How we contain Claude"](https://simonwillison.net/2026/May/30/how-we-contain-claude/) (published 30 May 2026) · [developers.openai.com/api/docs/guides/migrate-to-responses](https://developers.openai.com/api/docs/guides/migrate-to-responses) (fetched 2026-08-09) · [dev.to — "Chat Completions vs OpenAI Responses API: What Actually Changed"](https://dev.to/dev-in-progress/chat-completions-vs-openai-responses-api-what-actually-changed-4bco) (page shows "Posted on Mar 18," year not displayed on the page; fetched 2026-08-09) · [northflank.com/blog/how-to-sandbox-ai-agents](https://northflank.com/blog/how-to-sandbox-ai-agents) (02 Feb 2026) · [modal.com/resources/best-code-execution-sandboxes-ai-agents](https://modal.com/resources/best-code-execution-sandboxes-ai-agents) (May 2026)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — give each tool the least access it needs, not a raw shell or a whole API
**Do:** Instead of one open-ended tool (a generic shell-command runner, a "fetch any URL" tool, a
database credential with full read/write), build narrow, purpose-built tools (one specific query
function, a scoped read-only credential). Use short-lived, scoped credentials per tool — for
example an OAuth token limited to the minimum scope — rather than one shared, long-lived admin
credential behind every tool.
**Why (beginner):** If the model is ever manipulated into misusing a tool — by a bad prompt, by
poisoned content it read (see below), or by its own mistake — the damage is limited to whatever
that tool's credential is actually allowed to do. A "run any shell command as root" tool turns any
single mistake into a full system compromise; a narrowly scoped tool limits the damage to that one
function.
**Caveat / contested:** Least privilege is real engineering work — a purpose-built endpoint or a
scoped credential per tool, not just one shared API key — and teams under time pressure often skip
it.
**Sources:** [github.com/OWASP — LLM06 Excessive Agency](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md) (OWASP Top 10 for LLM Applications v2.0) · [northflank.com/blog/how-to-sandbox-ai-agents](https://northflank.com/blog/how-to-sandbox-ai-agents) (02 Feb 2026)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — require a human to approve any sensitive or destructive tool call
**Do:** Don't let the model be the only check before an action that can't be undone. The MCP
standard says there "SHOULD always be a human in the loop with the ability to deny tool
invocations," and recommends showing a confirmation prompt before sensitive operations execute.
Frameworks implement this as a pause point: the agent stops before running a marked tool, and a
human can approve it, edit the arguments, reject it with feedback, or respond directly — before
anything actually runs.
**Why (beginner):** An agent that can delete records, send real messages, or run shell commands
with no confirmation step will eventually do one of those things by mistake — or because of a
prompt-injected instruction (see below) — and once the action has run against the real world,
there's no undo button.
**Caveat / contested:** "Human in the loop" only helps if the human actually reads what they're
approving. A confirmation dialog people click through without reading is much weaker protection
than the pattern implies — see the 93% approval-fatigue figure in the sandboxing practice above.
**Sources:** [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [docs.langchain.com/oss/python/langchain/human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop) (fetched 09 Aug 2026, undated page) · [github.com/OWASP — LLM06 Excessive Agency](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md) (OWASP Top 10 for LLM Applications v2.0)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — never trust what a tool reads back; this is how "prompt injection" hijacks agents
**Do:** Anything a tool call fetches from outside your app — a web page, a document, an email, a
search result, another system's API response, another MCP server's reply — can contain text
written specifically to look like instructions to the model. This is called **indirect prompt
injection** or, in the MCP world, **tool poisoning**. Defend against it in layers: never copy
untrusted tool output into your system prompt as if it were an instruction; tell the model
explicitly, in your system prompt, that tool-returned content is data to report on, not
instructions to follow; and don't let a tool's own name, description, or "this tool is safe"
metadata be trusted just because it says so — a malicious or compromised server can write a
description that claims to be safe, or hide instructions inside it that only the model reads, not
the user. This isn't hypothetical: Microsoft published research in mid-2026 demonstrating exactly
this mechanism, where hidden instructions embedded in a tool's *description* caused an agent's
otherwise legitimate, already-approved tool calls to leak data.
**Why (beginner):** Security researcher Simon Willison named the underlying shape of this risk the
"**lethal trifecta**": an agent that combines (1) access to private data, (2) exposure to
untrusted content, and (3) the ability to communicate externally can be tricked by a single piece
of poisoned content into leaking your data — no traditional software bug required. A tool's output
counts as "untrusted content" exactly the same as a webpage or an email would. This is why the
sandboxing and least-privilege practices above matter even for tools that "just" read data.
**Caveat / contested:** Anthropic states Claude is "inherently resilient" to these attacks but
still recommends layered defenses (screening tool output with a cheap classifier model,
least-privilege tool scopes, red-teaming). Willison is more blunt: he's explicit that no
"guardrail" product he's aware of closes this gap to zero, and that mitigations claiming to catch
"95% of attacks" aren't good enough — the only fully reliable fix is not combining all three
conditions (private data + untrusted content + external communication) in one agent at all. OWASP
reportedly maps prompt injection to six of its ten risk categories for agentic applications — this
is an actively unsolved, fast-moving area, not a checklist you complete once. 🕒 verify live.
**Sources:** [platform.claude.com/docs — Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) (fetched 9 Aug 2026) · [simonwillison.net — The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (published 16 Jun 2025) · [developers.openai.com/api/docs/guides/agent-builder-safety](https://developers.openai.com/api/docs/guides/agent-builder-safety) (fetched 2026-08-09) · [helpnetsecurity.com — "Prompt injection still drives most agentic AI security failures in production"](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) (published 11 Jun 2026) · [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [owasp.org — MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning) (fetched 09 Aug 2026, undated page) · [invariantlabs.ai — MCP security notification: tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) (01 Apr 2025) · [thehackernews.com — Microsoft warns of poisoned MCP tool descriptions](https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html) (published 30 Jun 2026)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — make any tool that spends money or changes real state safe to retry
**Do:** For any tool that charges money, sends a message, or books something, attach an
**idempotency key** — a stable ID derived from things like a session ID plus the tool name plus a
hash of the arguments — before the first attempt, and reuse that *same* key on every retry of that
same logical action. Have the receiving system return the original result for a repeated key
instead of re-running the side effect. This matters even more if you let a model call several
tools at once ("parallel" tool calls): before you rely on parallel calls, check that each
side-effecting tool is **atomic** (fully happens or doesn't happen at all), **idempotent** (calling
it twice does the same thing as calling it once), and **independent** (doesn't secretly need
another tool's result first) — if any tool mutates shared state, turn parallel calling off for that
turn so at most one tool runs at a time.
**Why (beginner):** AI agents retry — because of network blips, because the model "isn't sure" the
first call worked, or because of a stuck loop (see below) — and a non-idempotent "charge card" or
"send email" tool will duplicate the action every single time that happens. This is one of the
single most common ways an AI agent costs someone real money by accident: a payment tool retried
twice by an agent means a customer's card gets charged twice for one order. Parallel calls that
silently race on the same resource don't crash — they corrupt state quietly, and the connection
back to "the model called two tools at once" is easy to miss once the wrong result shows up several
turns later.
**Caveat / contested:** Idempotency keys are a well-established distributed-systems pattern, but
there's no cross-vendor standard for how an agent framework should generate or store them, so
implementations vary. Whether reasoning-model variants reject the parallel-calls setting outright
if you set it explicitly is model-dependent — 🕒 verify live against whichever model you're
actually calling.
**Sources:** [machinelearningmastery.com — "AI Agent Tool Design: What Works and What Doesn't"](https://machinelearningmastery.com/ai-agent-tool-design-what-works-and-what-doesnt/) (published 15 Jun 2026) · [dev.to/mukundakatta — "Make Your Agent's API Calls Idempotent Before You Need To"](https://dev.to/mukundakatta/make-your-agents-api-calls-idempotent-before-you-need-to-2994) (page shows "Posted: May 25," year not displayed on the page; fetched 09 Aug 2026) · [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [tianpan.co — "Parallel Tool Calls in LLM Agents: The Coupling Test You Didn't Know You Were Running"](https://tianpan.co/blog/2026-04-10-parallel-tool-calls-hidden-coupling) (published 10 Apr 2026)
**Confidence:** independently-corroborated

### Practice: Put a hard limit on how many tool-call steps a single agent run can take
**Do:** Set a hard ceiling on how many tool-call/reasoning steps one agent run is allowed to take,
and have it fail gracefully — return to the user, or escalate — once that ceiling is hit, instead
of letting the loop run unbounded. This is commonly implemented as a step-count limit that raises
an error once the budget is exhausted. Separately, make sure your tools return unambiguous
success/fail signals rather than vague messages: one documented case cut an agent's tool calls
from 14 down to 2 for the same task just by replacing an ambiguous result with a clear terminal
signal.
**Why (beginner):** Agents can and do get stuck calling the same tool with the same arguments over
and over when a result is ambiguous or an error is unclear. This silently burns tokens (and API
cost) without producing an answer, and it won't necessarily look like a "crash" from the outside —
you have to actually notice the loop.
**Caveat / contested:** Exact default iteration limits differ by framework and version — 🕒 verify
live and don't assume a specific number without checking current docs.
**Sources:** [docs.langchain.com/oss/python/langgraph/errors/GRAPH_RECURSION_LIMIT](https://docs.langchain.com/oss/python/langgraph/errors/GRAPH_RECURSION_LIMIT) (fetched 09 Aug 2026, undated page) · [dev.to/aws — "Why AI Agents Fail: 3 Failure Modes That Cost You Tokens and Time"](https://dev.to/aws/why-ai-agents-fail-3-failure-modes-that-cost-you-tokens-and-time-1flb) (24 Mar 2025)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — defining tools costs money even on turns where none get called
**Do:** Remember that giving the model a list of tools at all (even ones it never ends up calling)
adds a hidden system prompt to every request, and that's billed as input tokens — on top of
whatever tokens your own tool names/descriptions/schemas need, and on top of every tool-call/result
exchanged across a multi-turn agent loop. Forcing a tool call generally costs more tokens than
letting the model decide for itself. Relatedly: every tool definition injected into context also
competes for the model's limited context window and for its attention when picking which tool to
use — so a big tool list is a real, ongoing cost, not just clutter.
**Why (beginner):** People new to tool use are often surprised that "just defining tools you never
end up calling" still costs money on every request — it's easy to under-budget a tool-heavy
agent's per-turn cost until you see the bill.
**Caveat / contested:** Exact per-model, per-vendor token costs change across releases — 🕒 verify
live; don't hardcode a specific number from any snapshot of this entry into a cost projection.
**Sources:** [platform.claude.com/docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (fetched 9 Aug 2026) · [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09)
**Confidence:** vendor-documented

### Practice: Reach for MCP if you want the same tools to work across more than one AI vendor
**Do:** Instead of hand-writing a separate integration per vendor's SDK, expose your tools through
the Model Context Protocol (MCP) — an open, JSON-RPC-based standard (a lightweight remote-call
format encoded as JSON) with a "list the available tools" / "call a tool" interface. MCP has been
adopted beyond its originator: Google Cloud announced official MCP support across Google/Google
Cloud services (Maps, BigQuery, GCE, GKE) in December 2025, describing MCP as having "quickly
become a common standard to connect AI models with data and tools." Claude's own API has a
built-in MCP connector that lets you talk to a remote MCP server directly, with no separate MCP
client needed.
**Why (beginner):** Without a shared protocol, every tool you build has to be re-wired for every
model vendor's own function-calling format. MCP lets one server implementation be reused by any
MCP-compatible client, regardless of which underlying model is driving the agent.
**Caveat / contested:** MCP standardizes *how* tools are listed and called, not what a given model
does with the results — you still get vendor-specific behavior differences in when/how a model
chooses to call a tool. The spec itself changes over time, so pin a specific protocol version
rather than assuming "latest" behavior will match what's described here. 🕒 verify live.
**Sources:** [modelcontextprotocol.io/specification/2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) (28 Jul 2026) · [blog.modelcontextprotocol.io — 2026-07-28 release post](https://blog.modelcontextprotocol.io/posts/2026-07-28/) (28 Jul 2026) · [cloud.google.com/blog — Announcing official MCP support for Google services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) (11 Dec 2025) · [platform.claude.com/docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (fetched 09 Aug 2026)
**Confidence:** independently-corroborated

---

## Part 2 — Designing tools people (and models) can actually use

### Practice: Write tool descriptions like you're onboarding a new hire who's never seen your code
**Do:** For every tool, write a description of at least 3–4 sentences: what it does, when it
should (and shouldn't) be used, what each parameter means (including units and format), and any
limits. A useful test: could a stranger unfamiliar with your system call this function correctly
using only the schema text? Anthropic's own comparison makes this concrete — a one-line
description like "Gets the stock price for a ticker" is explicitly called out as a "poor" example
next to a roughly 5-sentence version that names the exchange, the currency, the trigger
conditions, and what the tool does *not* return. Use unambiguous parameter names (`user_id`, not
`user`), write plain `snake_case` names without spaces (some model providers reject names with
spaces or special characters), and when you have tools from more than one service or MCP server,
prefix names by service (`github_list_prs`, `slack_send_message`) so they don't collide once
combined — MCP's own spec notes a server's `name` field isn't guaranteed unique across servers, so
this prefixing has to be done deliberately. On the response side, keep it focused too: return
stable, readable identifiers instead of opaque internal references, include only the fields the
model actually needs for its next step, and for tools that can return a lot of data, consider
capping the response size and supporting pagination or filtering.
**Why (beginner):** The model has nothing but a tool's name, description, and schema to decide
whether and how to call it — it can't see your source code. A vague description is one of the
single biggest causes of "the AI picked the wrong tool" or "the AI passed garbage arguments," and
a bloated response eats into the model's limited context (its total working-memory budget for one
request), making it harder to find the one field it actually needed.
**Caveat / contested:** This is qualitative guidance you can't unit-test directly — pair it with
the "make schemas strict" and "test against the real API" practices below so mistakes get caught
automatically instead of only by code review.
**Sources:** [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026) · [anthropic.com/engineering — Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (published 11 Sep 2025) · [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [nwos.com — "OpenAI Function Calling: Don't Let Your Schema Drift"](https://www.nwos.com/daily/openai-function-calling-dont-let-your-schema-drift) (published 15 Jun 2026) · [docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools) (fetched 09 Aug 2026, undated page) · [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (spec dated 28 Jul 2026)
**Confidence:** independently-corroborated

### Practice: Make input schemas strict, not just described in prose
**Do:** Use JSON Schema constraints — `enum`, `required`, length/format limits,
`additionalProperties: false` — to make an invalid tool call structurally impossible, rather than
relying on prose in the description to steer the model (a note like "please only use valid dates"
gets ignored far more often than a schema that structurally can't accept an invalid date). OpenAI
exposes this as a `strict: true` flag on a function tool (which also requires
`additionalProperties: false` on every object and every field listed in `required` — simulate an
"optional" field with a `["string", "null"]` type instead of leaving it out). Claude has an
equivalent `strict: true` "strict tool use" option. The MCP spec recommends
`{"type":"object","additionalProperties":false}` even for tools that take no parameters at all, so
extra or hallucinated fields get rejected instead of silently accepted.
**Why (beginner):** Without strict mode, the model can (and does) return a number as a string,
drop a required field, or invent an enum value that doesn't exist — things your code then has to
defensively catch on every single call. Strict mode pushes that validation into the API itself.
**Caveat / contested:** ⚠️ **WARNING** — if you use Claude's strict mode, don't put PHI (protected
health information) in a schema's `enum`/`const`/`pattern` values: Anthropic explicitly warns
these schemas are cached server-side (for up to 24 hours), and that cache doesn't get the same
HIPAA protections as ordinary message content — a compliance-relevant default, not a styling
preference. Separately, strict mode/structured outputs only support a subset of JSON Schema, and
OpenAI's version caps schemas at specific hard limits (5,000 total object properties, 10 nesting
levels, 1,000 enum values, 120,000 total characters across names/enums) and doesn't support some
keywords (`allOf`, `not`, `dependentRequired`, `if`/`then`/`else`) — prefer flatter, shallower
schemas where practical. These exact numeric limits are 🕒 verify live. A schema that's too narrow
can also cause the model to miss valid cases it should handle, so treat this as something to
iterate on with real testing, not a one-shot fix.
**Sources:** [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [developers.openai.com/api/docs/guides/structured-outputs](https://developers.openai.com/api/docs/guides/structured-outputs) (fetched 2026-08-09) · [machinelearningmastery.com — "AI Agent Tool Design: What Works and What Doesn't"](https://machinelearningmastery.com/ai-agent-tool-design-what-works-and-what-doesnt/) (15 Jun 2026) · [platform.claude.com/docs — Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) (fetched 9 Aug 2026)
**Confidence:** independently-corroborated

### Practice: Keep your active tool list small
**Do:** OpenAI's own soft guidance is to keep the number of tools available at the start of a turn
under roughly 20 — every tool definition is injected into context and billed as input tokens, so a
big tool list is a real, ongoing cost, not just clutter. Group related tools under a shared name
prefix (`crm_*`, `billing_*`, `shipping_*`) and defer less-used tools instead of loading everything
up front. One independent write-up reports production accuracy degrading once a tool catalog
passes roughly 10–20 tools in active rotation, because the model has to pick the right one out of
a longer, more repetitive list.
**Why (beginner):** More tools isn't free and isn't harmless — this is on top of the plain
token/cost overhead covered above, and it also makes the model more likely to pick the wrong tool.
**Caveat / contested:** The exact threshold is contested and 🕒 verify live — treat "keep it small
and defer the rest" as the durable takeaway, not any single number.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [machinelearningmastery.com — "The Complete Guide to Tool Selection in AI Agents"](https://machinelearningmastery.com/the-complete-guide-to-tool-selection-in-ai-agents/) (published 6 Jul 2026)
**Confidence:** independently-corroborated

### Practice: One job per tool, or one tool with several actions? Experts disagree — test both
**Do:** There's a genuine, unresolved disagreement between credible sources here, not a settled
rule. One school of thought: design one tool per distinct operation (`create_customer`,
`get_customer`) rather than one multipurpose tool with an internal `action` parameter
(`manage_customer(action=...)`) — if two tools' descriptions can't be told apart without saying
"unlike X, this one…," merge or redesign them. Anthropic's own guidance for Claude argues the
opposite: "rather than creating a separate tool for every action (`create_pr`, `review_pr`,
`merge_pr`), group them into a single tool with an `action` parameter." Both positions are
defensible — one-tool-per-operation makes each tool's job unambiguous; one-tool-per-workflow
reduces total tool count and clutter.
**Why (beginner):** Don't assume either answer is "the" right one for your case. Try a design,
watch whether the model calls the wrong tool or the wrong internal action, and adjust based on
what you actually see — this is a real tradeoff to test against your own model and tools, not
something you can decide once from a blog post.
**Caveat / contested:** This practice is itself the disagreement — see above.
**Sources:** [machinelearningmastery.com — "AI Agent Tool Design: What Works and What Doesn't"](https://machinelearningmastery.com/ai-agent-tool-design-what-works-and-what-doesnt/) (published 15 Jun 2026) · [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026) · [anthropic.com/engineering — Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (published 11 Sep 2025)
**Confidence:** contested

### Practice: Give clear, actionable error messages — and never fully trust the model's arguments
**Do:** Two different problems need two different responses. If a tool call fails because of a
bad or missing argument, send back a clear, specific, plain-English error (e.g. "date must be in
the future; you passed 2024-01-01") instead of a generic "failed" or a raw stack trace — a clear
error lets the model actually fix its own mistake and retry (Claude, for example, will typically
retry 2–3 times with corrections once it sees a clear error, before giving up and apologizing to
the user). If the *request itself* was malformed (an unknown tool name, garbled JSON) rather than
a legitimate attempt that just got a bad answer, that's a harder-to-fix kind of failure — models
are less able to self-correct from it. Before you even get to error messages, though: never assume
a tool call's arguments are automatically correct. Treat them as untrusted input from a
probabilistic system, not a trusted function call — check for empty or malformed JSON before
parsing, re-validate types/required fields/enum values against your schema, and if an argument is
an ID or reference (a customer ID, an account number), check that it actually exists and that the
caller is allowed to use it, since a syntactically valid ID can still be something the model made
up. And don't assume the model will always ask when a required detail is missing: Anthropic's own
docs note Claude Opus is more likely to stop and ask, while Claude Sonnet "might ask… But it might
also infer a reasonable value" — e.g. "What's the weather?" with no city given can quietly produce
a guessed city, with no error and no clarifying question at all.
**Why (beginner):** If an agent only sees "Error: 500," it has no way to decide whether to retry,
ask the user, or give up. Even OpenAI's own SDK documentation is blunt: the model does not always
generate valid JSON and may hallucinate parameters your function schema never defined — strict
mode (above) reduces this a lot, but doesn't reduce it to zero, and does nothing for a hallucinated
value that happens to be syntactically valid.
**Caveat / contested:** The "don't trust arguments" guidance here traces to OpenAI's own SDK docs
quoted on OpenAI's own community forum — one publisher, not independent corroboration for that
specific detail, though the general principle (never trust model-generated arguments) is durable,
widely echoed practice.
**Sources:** [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools) (fetched 09 Aug 2026, undated page) · [machinelearningmastery.com — "AI Agent Tool Design: What Works and What Doesn't"](https://machinelearningmastery.com/ai-agent-tool-design-what-works-and-what-doesnt/) (15 Jun 2026) · [community.openai.com — "Don't trust the output for functions"](https://community.openai.com/t/dont-trust-the-output-for-functions/269522) (posted 18 Jun 2023, quotes OpenAI's own Node.js library docs) · [platform.claude.com/docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (fetched 9 Aug 2026) · [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026) · [platform.claude.com/docs — Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) (fetched 9 Aug 2026)
**Confidence:** independently-corroborated

### Practice: Know the difference between "wait and retry" errors and "fix your account" errors
**Do:** For a rate-limit error, honor a `Retry-After` header if the API sends one; if it's absent,
back off with increasing wait times between retries. For a genuinely temporary failure (a timeout,
a brief connection error, a 5xx server error), wait briefly and retry. But for a billing, spend, or
quota error, retrying will not help — in OpenAI's own words, "retrying billing, spend, or quota
errors won't restore API access" — you need to add credits or raise your limit before the next
request will succeed.
**Why (beginner):** A naive "retry on any error" loop wastes time and can make rate limiting worse
on errors that will never resolve themselves just by trying again. Telling these two kinds of
errors apart up front avoids burning retries — and time — on a problem retries genuinely can't fix.
**Caveat / contested:** This is standard, uncontroversial API-client hygiene — vendor-documented
only this run, no independent OpenAI-specific corroboration was fetched.
**Sources:** [developers.openai.com/api/docs/guides/error-codes](https://developers.openai.com/api/docs/guides/error-codes) (fetched 2026-08-09)
**Confidence:** vendor-documented

### Practice: ⚠️ WARNING — testing your tool schema against the real API costs real money
**Do:** Derive your JSON schema from the same source of truth as your function's implementation
where you can (for example, generate enum values from the same constants your code validates
against), instead of hand-maintaining two separate definitions that can quietly drift apart. To
catch drift automatically, add tests that send real prompts to the actual API (not a mock) and
check that the model calls the function you expect, with the arguments you expect.
**Why (beginner):** When the schema and the implementation disagree — say you add a new parameter
to the function but forget to add it to the schema — the model never even knows the new option
exists. There's no crash, just a silently worse response, which is a hard failure mode to notice
without a test that actually exercises the model. But every one of those tests is a **real, billed
API call** — wiring this into a job that runs on every single code push can produce a real,
recurring bill. Prefer a scheduled or manually-triggered job over "run on every push" for this
specific kind of test.
**Caveat / contested:** This rests on a single independent source; treat "always hit the real API
in tests" as good practice, not an industry-wide consensus.
**Sources:** [nwos.com — "OpenAI Function Calling: Don't Let Your Schema Drift"](https://www.nwos.com/daily/openai-function-calling-dont-let-your-schema-drift) (published 15 Jun 2026)
**Confidence:** thin

---

## Part 3 — A brief look at Claude's and OpenAI's specific mechanics

Everything above applies no matter which vendor you're calling. The differences below are narrow,
mechanical, API-shape details — skim only the section for whichever vendor you're actually using.

### Claude (Anthropic Messages API)
Claude's `tool_choice` setting controls whether and which tool gets called: `auto` (the default)
lets Claude decide; `any` forces some tool call but not which one; `tool` forces one specific named
tool; `none` forbids tool calls entirely. One wrinkle worth knowing: `any` and `tool` "prefill" the
assistant's turn — they insert a forced start to the response — so Claude won't say anything
introductory in plain text before the tool call, even if you ask it to. If you want both a spoken
explanation and a call that feels forced, use `auto` plus an explicit instruction in your prompt
instead. Picking the wrong mode is a common source of "why won't Claude explain itself" or "why
does Claude sometimes just answer in text when I needed a tool call" bugs. Forced tool use
(`any`/`tool`) is **not supported** together with Claude's manual extended-thinking mode (it
returns an error); support for forcing tool use alongside "thinking" varies by model, so check the
current compatibility table rather than assuming.
**Sources:** [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026) · [platform.claude.com/docs — Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### OpenAI (Chat Completions & Responses APIs)
OpenAI's equivalent setting works similarly: `"auto"` (default, model decides), `"required"`
(force at least one call), a named-function object to force exactly one specific tool, `"none"` to
suppress tool calls entirely, or an "allowed tools" subset that restricts which of your
already-declared tools can be picked without changing the declared tool list itself (useful if
you're using prompt caching, since the cached list stays stable). Letting the model decide
(`"auto"`) is right most of the time, but for a fixed-shape task, forcing the exact function
removes a whole class of failure where the model answers in prose instead of calling the tool —
though forcing a tool doesn't validate the *arguments* it fills in; you still need the validation
practice above.

OpenAI has two APIs. The older **Chat Completions** API still works and has no announced shutdown
timeline. The newer **Responses** API models tool calls/results as distinct typed items instead of
everything being a "message," and comes with native built-in tools you can turn on alongside your
own custom functions — including web search, file search, code interpreter, and computer use.
⚠️ **WARNING (repeating the warning from Part 1):** two of those built-in tools, code interpreter
and computer use, give the model the ability to execute real code or control a real computer —
treat them with exactly the same sandboxing, least-privilege, and human-confirmation caution as
any other code-execution tool. Don't turn either one on just because it's presented as "the newer,
better API." Separately: a different, older OpenAI product called the **Assistants API** is
scheduled to shut down on **26 Aug 2026**. If you're reading this after that date and following an
older tutorial, code using its endpoints (`/v1/assistants`, `/v1/threads`) will already be broken
— 🕒 verify live.

**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [developers.openai.com/api/docs/guides/migrate-to-responses](https://developers.openai.com/api/docs/guides/migrate-to-responses) (fetched 2026-08-09) · [dev.to — "Chat Completions vs OpenAI Responses API: What Actually Changed"](https://dev.to/dev-in-progress/chat-completions-vs-openai-responses-api-what-actually-changed-4bco) (page shows "Posted on Mar 18," year not displayed on the page; fetched 2026-08-09)
**Confidence:** vendor-documented

### If you call more than one vendor's API directly
Expect the tool-definition format and the response format to differ, and plan for a translation
layer. As of the docs checked for this snapshot: OpenAI's function tools return the call's
arguments as a **JSON string** you must parse yourself; Claude's tools return the call's input as
an **already-parsed object**. Cross-provider frameworks (LangChain, LiteLLM, Vercel AI SDK) exist
specifically to normalize this — but even they still need a per-vendor adapter under the hood, so
"provider-agnostic" doesn't mean zero differences if you're ever debugging at the wire level. Code
that assumes a JSON string (correct for OpenAI) will break if you point the same code at Claude's
API and get an object back instead — a common "works with one model, breaks when we switch
providers" bug. These exact field names and behaviors are 🕒 **verify live** — function-calling
APIs are actively evolving.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 09 Aug 2026, undated page) · [platform.claude.com/docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (fetched 09 Aug 2026, undated page)
**Confidence:** independently-corroborated

---

## Held back for later

The topics below exist in the technical entry for this same date but were left out here because
they're implementation-level details that matter mainly once you're already deep into building
with a specific vendor's SDK — not something a true beginner needs to act on directly. No facts
about them are asserted here beyond the fact that they exist; read the technical entry
(`/ai/best-practices/tool-use-function-calling/2026-08-09/`) for the details.
- Extended thinking and interleaved thinking: the rules for passing Claude's "thinking" blocks
  back to the API unmodified, and the header/model compatibility matrix for reasoning between
  individual tool calls.
- The prompt-cache invalidation hierarchy for Claude tool definitions (which changes silently
  bust which layer of the cache).
- Buffering streamed tool-call JSON piece by piece (Claude's `input_json_delta` events, OpenAI's
  `function_call_arguments.delta` events) before parsing it.
- Claude's tool-search-tool / `defer_loading` mechanism for catalogs of 10+ tools or MCP servers.
- The exact `tool_use`/`tool_result` message-formatting rules for Claude's Messages API (most
  people never hit this directly, since Anthropic's SDK "Tool Runner" handles it for you).
- The Responses API's `call_id`/reasoning-item internals for OpenAI's reasoning models.
- `input_examples` for Claude tool schemas with tricky parameter formats.
- The MCP spec's detailed wire-format changes (moving `tools/call` routing into an HTTP header,
  deprecating Roots/Sampling/Logging).

## CHANGELOG (grading → this entry)
1. Re-leveled from the 2026-08-09 technical entry
   (`content/ai/best-practices/tool-use-function-calling/2026-08-09/`) for a beginner audience.
   Facts, sources, dates, and confidence tiers are unchanged; only reading level, structure, and
   depth of coverage changed.
2. Reordered content so cross-vendor safety practices (sandboxing, least privilege, human
   confirmation, treating tool output as untrusted, idempotency, iteration limits, tool-definition
   cost) lead the entry, ahead of any vendor-specific mechanics — this track's "lead with one
   sensible default path" rule.
3. Merged near-duplicate practices that appeared separately across the Claude, OpenAI, and
   generic sections of the technical entry (three separate "treat tool output as untrusted"
   warnings; three separate "write good tool descriptions" practices; two separate sandboxing
   warnings; the strict-mode practice that appeared once per vendor) into single cross-vendor
   practices, combining — never trimming — their original Sources lines.
4. Omitted several advanced/plumbing-level practices as not directly actionable for a true
   beginner (extended thinking & interleaved thinking mechanics, prompt-cache invalidation
   hierarchy, streamed-JSON buffering, Claude's tool-search-tool/`defer_loading` mechanism,
   Responses API reasoning-item internals, exact `tool_use`/`tool_result` formatting rules,
   `input_examples`, detailed MCP wire-format changes) — listed under "Held back for later" above
   rather than silently dropped.
5. Kept every ⚠️ WARNING from the technical entry in full: sandboxing, least privilege, human
   confirmation, idempotency/duplicate-charge risk, tool-definition token cost, billed-API-call
   testing cost, and code-interpreter/computer-use risk.

