# Context Management for AI Coding Agents — Best Practices (as of 06 Aug 2026)

> How coding agents actually fill, compact, and isolate their fixed context windows — the framework-agnostic mechanics plus Claude Code, OpenAI Codex CLI, and Google Gemini CLI specifics, including the caching and cost traps that quietly drain a budget.


<!-- This file lands at content/ai/best-practices/context-management-for-coding-agents/2026-08-06/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a
     NEW <snapshot-date> dir. "Latest" is computed by Grove's template from snapshot_date;
     do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Context Management for AI Coding Agents (as of 06 Aug 2026)

> **Grading note.** A dated snapshot — accurate as of **06 Aug 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by four pupils (one framework-agnostic
> foundations slice, plus one per ecosystem — Claude Code, OpenAI Codex CLI, Google Gemini
> CLI) on 06 Aug 2026, adversarially re-fetched by the Skeptic panelist the same day (0
> fabricated URLs, but a recurring pattern of real sources with invented numbers/quotes
> attached — 3 KILL-level corrections below), reviewed for novice-safety by the Beginner
> panelist, and checked for staleness/completeness by the Timekeeper panelist. Items still
> unverifiable are marked **⚠ PENDING** — this corpus does not publish unverified content.
> **0 fabrications after correction.**

## How to read the labels
- ✅ **independently-corroborated** — confirmed by 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value yourself

---

## Part 0 — Foundations (apply to *any* coding agent)

These mechanics hold regardless of which CLI or vendor you use.

### Practice: Know what actually counts toward "the context window" before you reason about it

**Do:** Treat "context window" as the total token budget for **one model call** — system
prompt + tool/function definitions + every prior turn's messages (including tool results,
images, documents) + the model's own output for that turn, including any hidden
"thinking"/reasoning tokens. It is not the model's training data, and it is not unlimited
memory across a whole project — it resets (or gets compacted) per session. As of 06 Aug 2026
🕒 **verify live**, current frontier models used by coding agents commonly ship 200K–1M+
token windows: Anthropic's Claude Sonnet 5 and Opus 5 default to a 1M-token window (200K on
older Sonnet 4.5/Haiku-class models) with up to 128K output tokens — and Anthropic's
newest, most coding-capable tier, **Claude Fable 5** (GA 9 Jun 2026, with a restricted
sibling Claude Mythos 5), also ships the same 1M-token window; OpenAI's GPT-5.6-series
models list a 1.05M-token context window with a 128K max output; Google's Gemini 3-series
models (`gemini-3.1-pro-preview`, `gemini-3-flash-preview`) list **1M input / 64K output**,
with `gemini-3.1-flash-lite` at the same 1M/64K, alongside the still-active Gemini 2.5
series. Exact figures change between model releases and are worth re-checking against the
vendor's own model page before you budget a session.

**Why (beginner):** If you don't know what's actually filling up your budget, you can't
explain why a session suddenly starts acting "dumber" or refuses to continue — it's usually
not a bug, it's the window filling up with old tool output, file contents, and reasoning you
don't see.

**Caveat / contested:** These are per-model API limits, not what a given CLI tool actually
lets you use in practice (see the next practice — the tool-imposed usable budget is often
much smaller than the model's advertised maximum). On Claude models, whether previous
"thinking" blocks are kept or stripped from context depends on the specific model version,
which changes how fast a session's budget fills.

**Sources:** [Claude Platform Docs — Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 06 Aug 2026) · [Claude Platform Docs — What's new in Claude Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5) (fetched 06 Aug 2026) · [Claude Platform Docs — Pricing](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 06 Aug 2026, Fable 5/Mythos 5 pricing and windows) · [developers.openai.com — Models (GPT-5.6 series)](https://developers.openai.com/api/docs/models) (fetched 06 Aug 2026) · [Google AI for Developers — Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3) (fetched 06 Aug 2026) · [Google AI for Developers — Long context](https://ai.google.dev/gemini-api/docs/long-context) (updated 22 Jun 2026, fetched 06 Aug 2026)

**Confidence:** vendor-documented (each vendor documents only its own numbers — three
vendors independently publishing specs is not the same as independent corroboration of any
single figure)

---

### Practice: Plan for the *effective* usable context, not the advertised maximum

**Do:** Assume the number on a model's marketing page is a ceiling, not a working budget.
Coding-agent CLIs typically reserve a chunk of the window for output and safety margin, and
real-world accuracy on retrieval-style tasks falls off well before the hard limit. One
documented example: OpenAI's own specs list a 1.05M-token window for the GPT-5.6 series, but
Codex CLI itself caps usable input at **272,000 tokens** inside a 400,000-token session
budget (128K reserved for output, plus a 5% safety buffer) — roughly a quarter of the
advertised maximum (this cap was tightened from 372,000 tokens on 18 Jul 2026 via a
billing-metadata fix, not a model downgrade — the underlying model still has its full 1.05M
window). Separately, Chroma Research (an independent AI-infrastructure company whose
commercial product is retrieval, so it has a direct interest in "big windows don't work as
advertised" being true) tested 18 models across Anthropic, OpenAI, Google, and Alibaba and
found performance "varies significantly as input length changes, even on simple tasks" —
the study does **not** publish a single headline percentage-shortfall figure, so don't quote
one; the finding to take away is that accuracy degradation starts well before you hit the
wall, not a specific number. Budget sessions to the smaller, real number, and start
summarizing/compacting well before you approach it.

**Why (beginner):** "This model has a 1-million-token context window" does not mean you can
safely fill it with a million tokens of your repo and expect reliable answers — in practice,
both the tool and the model itself behave much better with a lot of headroom left.

**Caveat / contested:** The exact usable fraction is tool- and task-specific (varies by CLI
version, task type, and how "accuracy" is measured) and changes fast as vendors tune default
reserves — treat any specific percentage as a snapshot, not a permanent ratio. 🕒 verify live.

**Sources:** [Codex Knowledge Base — "The Context Window Gap"](https://codex.danielvaughan.com/2026/07/20/context-window-gap-codex-cli-gpt56-advertised-vs-effective-budget-compaction-strategy/) (20 Jul 2026, independent blog, fetched 06 Aug 2026) · [developers.openai.com — Models](https://developers.openai.com/api/docs/models) (fetched 06 Aug 2026, confirms the 1.05M/128K figures) · [GitHub issue #32486 — Codex context-window billing metadata](https://github.com/openai/codex/issues/32486) (fetched 06 Aug 2026, confirms the 372K→272K change on 18 Jul 2026) · [Chroma Research — Context Rot](https://www.trychroma.com/research/context-rot) (14 Jul 2025, fetched 06 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: Treat "context rot" (lost-in-the-middle) as a real, measured failure mode — not a myth

**Do:** Design prompts and agent loops assuming models do not use every token in the window
equally. Put the most task-critical instructions and facts near the **start or end** of the
context, not buried in the middle of a long tool-output dump, and don't assume a bigger
window fixes retrieval accuracy on its own. Chroma's July 2025 study of 18 models (including
Claude, GPT, Gemini, and Qwen families) found performance varies significantly as input
length grows "even on simple tasks," and that structural coherence can *hurt* — shuffled
context sometimes outperformed logically-organized context. Anthropic's own engineering
guidance (29 Sep 2025) independently describes the same phenomenon and recommends curating
what's in context rather than maximizing how much is stuffed in. A 2025 arXiv paper (Oct
2025, "Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs")
offers one explanation: the "U-shaped" primacy/recency bias may be an emergent side effect
of how models are pretrained on long- vs. short-term memory-style tasks, not a simple
engineering bug — meaning it likely won't just disappear as models scale.

**Why (beginner):** If your agent seems to "forget" an instruction you gave 40 messages ago
even though it's technically still in the transcript, that's not a hallucination bug — it's
a documented, measured pattern. Repeat critical constraints close to the end of the context
(e.g., right before asking the model to act) rather than assuming "I said it once, it's in
there."

**Caveat / contested:** The precise shape of the effect is still being refined and is an
active research area, not a settled constant — results differ by task type (retrieval vs.
reasoning vs. code generation). Treat the "U-shape" as a real, documented pattern whose exact
boundary conditions (e.g. at what fraction of the window it starts to bite) are not yet
pinned down by a single agreed-upon source.

**Sources:** [Chroma Research — Context Rot](https://www.trychroma.com/research/context-rot) (14 Jul 2025, fetched 06 Aug 2026) · [Anthropic Engineering — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (29 Sep 2025, fetched 06 Aug 2026) · [arXiv 2510.10276 — Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs](https://arxiv.org/abs/2510.10276) (11 Oct 2025, fetched 06 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: Use compaction/summarization to survive long sessions, but know exactly what it can silently drop

**Do:** When a session approaches its usable budget, compact (summarize) rather than either
hard-stopping or blindly truncating old turns. Anthropic's server-side compaction and Claude
Cookbook guidance describe the pattern generically: the model is asked to produce a
high-fidelity summary of everything so far, and that summary replaces the raw history —
preserving "architectural decisions and unresolved issues" while discarding
redundant/verbose output, and is explicitly "lossy by design." Independently, an analysis of
OpenAI's Codex CLI describes the same core pattern ("single-layer handoff summary": once
tokens exceed a threshold, the whole conversation is sent back to the model to produce a
summary that physically replaces the original history) and is explicit that this is
"inherently lossy but predictable." Both sources agree compaction is currently the standard
answer to "the conversation is about to hit the wall," and both flag it as a lossy operation,
not a free one.

**Why (beginner):** After your agent auto-compacts, don't assume everything you told it
earlier survived intact. A summary is a *lossy* rewrite generated by the same model that
might already be confused — it can drop a constraint you gave 100 messages ago, or worse,
"smooth over" a detail into something that sounds plausible but isn't what you actually said
(a compressed hallucination). Re-state hard constraints (e.g. "never touch the payments
module," "always run tests before committing") right after a compaction event, and treat
anything you truly cannot afford to lose as belonging in a file on disk, not just in chat
history.

**Caveat / contested:** Vendors differ on trigger thresholds and whether compaction is
automatic or must be manually invoked (e.g., a `/compact` command); some tools let you supply
custom compaction instructions to protect domain-specific details, which is worth doing for
anything safety- or correctness-critical. This is a fast-moving, tool-specific implementation
detail — 🕒 verify live against your specific tool's docs.

**Sources:** [Claude Platform Docs — Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 06 Aug 2026) · [Claude Cookbook — Context engineering: memory, compaction, and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools) (fetched 06 Aug 2026) · [Codex Knowledge Base — "The Context Window Gap"](https://codex.danielvaughan.com/2026/07/20/context-window-gap-codex-cli-gpt56-advertised-vs-effective-budget-compaction-strategy/) (20 Jul 2026, independent blog, fetched 06 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: Push bulky or exploratory work into isolated sub-agents; bring back only the conclusion

**Do:** When a task involves a lot of "burn context to figure something out" work (searching
a large codebase, reading many files, trying several failed approaches), delegate it to a
sub-agent that gets its own separate context window, and have it return only a short,
condensed result (on the order of a few hundred to ~2,000 tokens) to the parent/coordinator.
The parent keeps a short running log instead of the sub-agent's full transcript of tool
calls, dead ends, and intermediate reasoning. This is a general context-isolation design
pattern, not one specific tool's trick: Anthropic's own engineering guidance describes
sub-agents "each explor[ing] extensively but return[ing] condensed summaries," an
independent Oct 2025 write-up on Claude Code sub-agents describes the same mechanic (the
coordinator gets "a concise resulting context... included into the original conversation"
instead of a full transcript), and an independent 2026 academic paper analyzing Claude
Code's architecture separately identifies "subagent delegation and orchestration" as one of
the system's core context-management mechanisms.

**Why (beginner):** If you ask an agent to "explore the whole codebase and figure out where X
is handled," doing that in the main conversation can burn a huge fraction of your context
budget on searching and dead ends before it even starts the real task. Delegating that
exploration to a sub-agent (or a fresh sub-task) keeps your main session's budget for the
actual work, at the cost of some duplicated setup/tool overhead for each sub-agent spun up.

**Caveat / contested:** Sub-agents cost real tokens (and, on paid APIs, real money) of their
own — isolation trades "one big context" for "several separate contexts," which is a net win
for reliability and focus but is not free. The condensed summary a sub-agent returns is
itself subject to the same lossy-compaction risk described above: a bad summary from a
sub-agent can quietly misinform the parent.

**Sources:** [Anthropic Engineering — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (29 Sep 2025, fetched 06 Aug 2026) · [Rich Snapp — Context Management with Subagents in Claude Code](https://www.richsnapp.com/article/2025/10-05-context-management-with-subagents-in-claude-code) (05 Oct 2025, independent, fetched 06 Aug 2026) · [arXiv 2604.14228 — Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems](https://arxiv.org/abs/2604.14228) (v2, 02 Jul 2026, fetched 06 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: Use prompt caching to cut cost/latency for repeated context — but know a cache is fragile

**Do:** For any prompt prefix that repeats across calls (a large system prompt, a repo's
worth of loaded context, a long conversation history), turn on prompt caching rather than
paying full price to reprocess it every turn. Both Anthropic and OpenAI implement the same
general pattern: cache a prefix of the prompt, and if a later request sends an **identical**
prefix (byte-for-byte) up to a cache "breakpoint," the cached version is reused at a steep
discount instead of being recomputed; if even one byte differs before that point, the match
fails and everything from there is billed and processed at full rate. As of 06 Aug 2026 🕒
verify live: on Anthropic's API, cache reads cost ~10% of base input price, 5-minute-TTL
(time-to-live — how long the cached copy stays warm before it expires) cache writes cost
~1.25x base input price, and a 1-hour TTL option costs ~2x base input price; on OpenAI's
newer models, cache writes for GPT-5.6+ cost 1.25x the uncached rate while reads remain
discounted, with cache retention of "at least 30 minutes." Anthropic also confirms that
Claude's 1M-token context window (Claude 4.6 and later models) is billed at flat standard
per-token pricing with no extra "long context" surcharge — caching, not window size, is the
main cost lever. Minimum cacheable prefix sizes range roughly **512–4,096 tokens** depending
on model (512 for the current flagship tier — Opus 5, Fable 5, Mythos 5 — up to 4,096 for
older Opus/Haiku models on Anthropic's side; OpenAI documents a strict 1,024-token minimum).

**Why (beginner):** Prompt caching is a cost/speed optimization, not a memory feature — it
does not make an agent "remember" anything beyond its normal context window, and any edit
anywhere in the cached prefix (even fixing a typo in a system prompt) breaks the cache for
everything after that point, silently making the next request slower and pricier than you
might expect until the cache rebuilds.

**Caveat / contested:** Cache TTLs, minimum prefix sizes, and pricing multipliers are vendor-
and model-specific and change often — treat every number here as 🕒 verify live against
current vendor docs before relying on it for a cost estimate.

**Sources:** [Claude Platform Docs — Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (fetched 06 Aug 2026) · [Claude Platform Docs — Pricing](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 06 Aug 2026) · [developers.openai.com — Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) (fetched 06 Aug 2026)

**Confidence:** vendor-documented (Anthropic and OpenAI each document only their own product's mechanics)

---

### Practice: Choose retrieval (RAG) vs. "load the whole repo into context" based on repo size and query shape — not by default habit

**Do:** For small-to-medium repos, or questions that genuinely need cross-file reasoning (a
rename that touches many call sites, understanding a subsystem end-to-end), loading the
relevant files directly into context tends to preserve structure (imports, types, call
sites) that chunked retrieval (RAG — Retrieval-Augmented Generation: fetching only the
most-relevant chunks of a larger corpus instead of loading everything) can lose. For large
repos, or narrow factual questions ("where is X defined," "what does function Y do"),
retrieval-first (index the repo, fetch only the relevant chunks) avoids paying token cost
for code the model doesn't need and avoids diluting the context with irrelevant files —
which, per context rot, can itself hurt accuracy. Google's own Gemini long-context guidance
explicitly advises providing relevant information directly in context rather than using
RAG/token-filtering when the model's context window can hold it, citing "robust in-context
learning" — while an independent analysis (Redis engineering blog) confirms that plain
transformer attention cost is dominated by an O(n²) term in sequence length ("doubling your
context length roughly quadruples the computational requirements for attention"), and that a
hybrid "retrieve-then-load-full-context" pattern is increasingly common in production
agentic systems.

**Why (beginner):** There's no universal right answer to "should my coding agent search the
codebase or just read the whole thing?" — it depends on whether the repo fits comfortably in
the budget you're willing to spend, and whether the question needs to see everything at once
or just needs to find one specific thing. When in doubt for a large repo, start with targeted
reads/searches rather than dumping the whole tree into context "to be safe" — a full-context
dump is often slower, pricier, and (per context rot) not actually more reliable.

**Caveat / contested:** This is a fast-evolving, actively-debated area (as reflected in the
"RAG is dead" vs. "RAG is essential" framing common in vendor and independent commentary);
the guidance above reflects the trade-off consensus as of mid-2026, not a settled law —
re-check as both retrieval tooling and context window sizes keep moving. (An earlier draft of
this practice cited a specific RAG "recall" percentage attributed to the Redis source below;
on re-fetch that figure was not on the page — it measured agreement-rate between two
approaches, not RAG's recall — and has been removed rather than republished uncorrected.)

**Sources:** [Google AI for Developers — Long context](https://ai.google.dev/gemini-api/docs/long-context) (updated 22 Jun 2026, fetched 06 Aug 2026) · [Redis — RAG vs large context window: the real trade-offs for AI apps](https://redis.io/blog/rag-vs-large-context-window-ai-apps/) (06 Feb 2026, updated 01 Jun 2026, fetched 06 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: ⚠️ Long sessions and big contexts can quietly cost real money — budget and monitor, don't assume "bigger window" is a free upgrade

**Do:** Because attention cost scales roughly quadratically with context length (meaning
cost grows much faster than the context length itself, not in direct proportion to it), and
because every tool result, file read, and prior turn stays billable until it's compacted or
cleared, a long-running coding session on a large-context model can accumulate cost far
faster than a naive "tokens x price" estimate suggests — especially if the agent re-reads
large files or re-fetches the same web page repeatedly instead of reusing what's already in
context. Anthropic's own API explicitly warns that a fetched web page can consume tens of
thousands of tokens (their own numbers: ~2,500 tokens for an average 10 KB page, ~25,000 for
a 100 KB doc page, ~125,000 for a 500 KB PDF) and exposes a `max_content_tokens` guard
specifically to protect against "inadvertently fetching large content that would consume
excessive tokens." Set a tool-level or CLI-level budget/cap, watch token-usage output as a
session runs, and compact or start fresh proactively rather than waiting for a cost surprise
or a hard context-limit error.

**Why (beginner):** ⚠️ This is the "costs money" beginner-safety flag for this whole topic:
an agent left running unattended in a big-context session, especially one that keeps
re-reading the same large files or fetching the same pages instead of remembering it already
has them, can rack up a bill much faster than a short back-and-forth chat would suggest.
Don't assume "I have a 1M-token window" means "I can leave this running all day for free" —
check your provider's usage dashboard, not just your intuition.

**Caveat / contested:** Exact per-token costs, free-tier allowances, and safety-guard
parameters (like `max_content_tokens`) are vendor- and model-specific and change frequently —
🕒 verify live before relying on any number here for a budget decision.

**Sources:** [Claude Platform Docs — Pricing (web fetch tool, code execution, long-context pricing)](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 06 Aug 2026) · [Redis — RAG vs large context window: the real trade-offs for AI apps](https://redis.io/blog/rag-vs-large-context-window-ai-apps/) (06 Feb 2026, updated 01 Jun 2026, fetched 06 Aug 2026) — corroborates the quadratic-cost/latency claim independently

**Confidence:** independently-corroborated

---

## Part 1 — Claude Code

> All slash commands below (`/compact`, `/clear`, `/context`, `/memory`, `/model`, `/resume`,
> etc.) are typed **inside the running `claude` interactive session**, not at the Ubuntu bash
> prompt — typing `/compact` directly into bash will just get you a "no such file or
> directory" error, since bash reads a leading `/` as an absolute path.

### Practice: Know what loads into context before you type anything

**Do:** Before your first prompt, Claude Code already loaded the system prompt, every
applicable CLAUDE.md file (managed policy, user, project, local), the first 200 lines/25KB of
the project's auto-memory `MEMORY.md`, MCP (Model Context Protocol — the standard Claude Code
uses to connect external tools/servers) tool names, and skill (a reusable, invokable
instruction bundle Claude Code can load on demand) one-line descriptions. Run `/context` at
any point in a session for a live breakdown by category, and `/memory` to list your memory
file locations (including project/user CLAUDE.md entries for files that don't exist yet —
use `/context`, not `/memory`, to see what actually loaded into the current session).

**Why (beginner):** New users assume the context window only holds "what I typed." In
reality a meaningful chunk (project docs, prior learnings, tool listings) is spent before
your first message even lands, and that budget is what makes a long CLAUDE.md or a lot of
MCP servers expensive turn after turn.

**Caveat / contested:** The built-in `Explore` and `Plan` subagents deliberately skip
CLAUDE.md and git status to stay cheap; every other subagent loads the full CLAUDE.md
hierarchy. Token figures Anthropic shows in its own interactive walkthrough are explicitly
"illustrative," not guaranteed.

**Sources:** [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Keep CLAUDE.md lean — target under ~200 lines

**Do:** Treat CLAUDE.md as expensive, always-loaded working memory, not documentation. Put
only what Claude needs in *every* session (build commands, conventions, project layout, hard
"always do X" rules). Move anything topic-specific into `.claude/rules/` with `paths:`
frontmatter (loads only when matching files are touched) or into a skill (loads only when
invoked). Anthropic's own `/init`/`/doctor` tooling will propose trims that cut content
Claude can re-derive from the codebase.

**Why (beginner):** A bloated CLAUDE.md doesn't just burn tokens on every single message —
independent testing and Anthropic's own docs agree that longer files reduce how reliably
Claude actually follows the rules in them ("lost in the middle"). A short file Claude
reliably obeys beats a long one it skims.

**Caveat / contested:** Anthropic's official guidance says "target under 200 lines per
CLAUDE.md file," and two independent write-ups checked directly against this figure both say
the same thing ("under about 200 lines," "aim for under ~200 lines") — all three sources
agree; treat 200 as the number, not a range, and re-verify 🕒 if you're citing it as a hard
rule rather than a rule of thumb.

**Sources:** [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 06 Aug 2026) · [iwoszapar.com — Claude Code Best Practices: 8 Rules I Learned the Hard Way](https://www.iwoszapar.com/p/claude-code-best-practices) (published 19 Jun 2026, updated 05 Aug 2026) · [dev.to/nishilbhave — CLAUDE.md Best Practices: The Complete 2026 Guide](https://dev.to/nishilbhave/claudemd-best-practices-the-complete-2026-guide-435j) (posted 29 May 2026, edited 09 Jul 2026, fetched 06 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: Don't expect a mid-session CLAUDE.md edit to apply immediately

**Do:** If you (or Claude) edit the project-root or user-level CLAUDE.md while a session is
running, know that Claude Code read it once at session start and is holding that version in
memory. The edit is saved to disk but has **no effect** on the running session until the next
`/clear`, `/compact`, or restart. (Nested CLAUDE.md files and path-scoped rules are the
exception: they load lazily the first time a matching file is read, so an edit made before
that first load does take effect.)

**Why (beginner):** This is a common "why is Claude ignoring the CLAUDE.md rule I just added?"
trap. It isn't a bug — it's how Claude Code protects the prompt cache from recomputing on
every edit — but it will confuse anyone who expects live reloads.

**Caveat / contested:** None found; this is a deliberate design choice Anthropic documents
plainly.

**Sources:** [code.claude.com/docs/en/prompt-caching](https://code.claude.com/docs/en/prompt-caching) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Compact deliberately, at a task boundary, with a focus instruction — don't wait for the automatic pass

**Do:** Run `/compact` yourself between tasks (e.g. `/compact focus on the auth bug fix`)
rather than letting Claude Code's automatic compaction fire mid-task. You can also add a
"Compact instructions" section to CLAUDE.md to steer what every compaction preserves — for
example:
```
## Compact instructions
Always preserve: the exact failing test names, the file paths we've already
edited this session, and any decision to reject an approach (with why).
```
or widen the buffer with `/autocompact <token-count>` so auto-compact triggers later or
earlier than the model's default — e.g. `/autocompact 50000` reserves a smaller trailing
buffer (auto-compact fires closer to the true hard limit, so you get more usable
conversation before it triggers, but a large single turn near the end risks tipping the
session over the hard limit and erroring instead of compacting gracefully), while a larger
number like `/autocompact 200000` compacts earlier and more often, trading conversation
length for a bigger safety margin.

**Why (beginner):** Auto-compact happens automatically so a full context window doesn't kill
your session — that part is a safety net, not a bug. But independent write-ups consistently
report that when compaction fires mid-debugging (mid-stack-trace, mid-refactor), the
resulting summary drops exactly the details you were relying on, and Claude can start
guessing at the wrong file. Compacting at a moment *you* choose gives you a say in what the
summary keeps.

**Caveat / contested:** The precise auto-compact trigger threshold is model- and
version-dependent and has changed over time (one independent report from Dec 2025 describes a
shift from a ~90%+ threshold to ~75% with a larger completion buffer); Anthropic's own docs
describe the default as "compacts when the conversation reaches the model's context limit"
unless a session type or setting compacts earlier. 🕒 verify live — treat any specific
percentage as a snapshot, not a guarantee.

**Sources:** [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [okhlopkov.com — Claude Code /compact: What It Does, What Survives](https://okhlopkov.com/claude-code-compaction-explained/) (fetched 06 Aug 2026, no publish date shown) · [bytebell.ai — Claude Code Keeps Compacting and Losing My Work](https://bytebell.ai/blog/claude-code-compacting-losing-work/) (published 18 Mar 2026) · [hyperdev.matsuoka.com — How Claude Code Got Better by Protecting More Context](https://hyperdev.matsuoka.com/p/how-claude-code-got-better-by-protecting) (published 10 Dec 2025)

**Confidence:** independently-corroborated

---

### Practice: Know exactly what /compact keeps and what it drops

**Do:** Before relying on compaction, understand Anthropic's own preserved/dropped table: the
system prompt and output style are untouched (they're not part of message history);
project-root CLAUDE.md and unscoped rules are re-read from disk and re-injected; auto memory
is re-injected; **rules with `paths:` frontmatter and nested subdirectory CLAUDE.md files are
lost until a matching file is read again**; invoked skill bodies are re-injected but capped
(5,000 tokens/skill, 25,000 tokens total, oldest dropped first, truncated from the end); the
skill *description* index does not reload — only skills you actually invoked survive.

**Why (beginner):** If an instruction "disappears" after `/compact`, it's almost always one
of two things: it was only ever said in conversation (never written to CLAUDE.md), or it
lived in a nested/path-scoped file that hasn't reloaded yet. Knowing the table tells you
where to put a rule if it must survive compaction — at the project root, not three folders
down.

**Caveat / contested:** This is Anthropic's own documented mechanism and, as far as this
research could confirm, the specific preserved/dropped table is not independently re-verified
by a third party — treat the exact numbers (token caps, etc.) as 🕒 verify live and
version-gated.

**Sources:** [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Treat compaction as lossy and occasionally silent — don't bet a long debugging session on it

**Do:** For anything you can't afford to re-derive (exact line numbers, "we agreed to use
middleware not decorators," why you rejected the first approach), write it to CLAUDE.md or
commit it to git rather than trusting it survives in conversation history. Watch for signs
Claude got "dumber" right after a compaction message — that's often a real signal the summary
dropped something load-bearing, not just a feeling.

**Why (beginner):** Two independent write-ups (plus Anthropic's own "detailed instructions
from early in the conversation may be lost" admission) describe the same failure mode:
compaction summarizes away specifics, Claude starts working from a vaguer picture, and — in
reported worst cases — edits the wrong file or repeats a mistake it had already been
corrected on before compaction. One independently-verified GitHub issue reportedly describes
rules being followed before compaction and violated 100% of the time after.

**Caveat / contested:** These are user-reported anecdotes and blog analysis, not a controlled
study — treat "100% violation rate" and similar figures as illustrative, not a measured
statistic. Anthropic frames this as an expected tradeoff (summarize or hit a hard wall), not
a defect.

**Sources:** [golev.com — Claude Saves Tokens, Forgets Everything](https://golev.com/post/claude-saves-tokens-forgets-everything/) (published 15 Jan 2026) · [bytebell.ai — Claude Code Keeps Compacting and Losing My Work](https://bytebell.ai/blog/claude-code-compacting-losing-work/) (published 18 Mar 2026) · [code.claude.com/docs/en/how-claude-code-works](https://code.claude.com/docs/en/how-claude-code-works) (fetched 06 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: Use /clear, not /compact, when switching to genuinely unrelated work

**Do:** When you're done with one task and starting something with no shared context, run
`/clear` to reset to zero rather than `/compact`, which still leaves a summary of the old
task taking up space (and cache-invalidates the conversation layer either way). Use `/rename`
before clearing if you might want to `/resume` the old session later.

**Why (beginner):** `/compact` is for continuing the *same* task with a smaller footprint;
`/clear` is for starting a *different* task. Stale context from an unrelated prior task
crowds out the files you actually need next and costs tokens on every following message for
no benefit.

**Caveat / contested:** None found — this distinction is consistent across vendor docs and
independent commentary.

**Sources:** [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 06 Aug 2026) · [okhlopkov.com — Claude Code /compact: What It Does, What Survives](https://okhlopkov.com/claude-code-compaction-explained/) (fetched 06 Aug 2026, no publish date shown)

**Confidence:** independently-corroborated

---

### Practice: Delegate large/verbose exploration to subagents to protect the main context budget

**Do:** Send research that would flood your main conversation — reading many files, grepping
across a codebase, running a test suite, fetching documentation, processing logs — to a
subagent (via the `Agent` tool, which Claude Code renamed from "Task" to "Agent" as of
v2.1.63; old `Task(...)` references still work as aliases). The subagent gets a fresh,
separate context window; only its final summary (plus a small metadata trailer) returns to
your main conversation. Anthropic's own numbers in its interactive example show a subagent
reading ~6,100 tokens of files and returning only ~420 tokens to the parent (Anthropic
labels this example "illustrative," not a guaranteed ratio).

**Why (beginner):** This is one of the biggest levers beginners underuse. Instead of "read
every file in this directory and tell me what's wrong," ask Claude to delegate that
read-heavy investigation to a subagent — the file contents pile up in a context window you
never have to pay to keep around.

**Caveat / contested:** ⚠️ **WARNING** — running many subagents in parallel that each return
a detailed result can still consume significant main-context tokens on return; Anthropic's
own docs warn about this directly. For truly large parallel workloads, look at "agent teams"
instead, where each worker keeps an independent context window.

**Sources:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) (fetched 06 Aug 2026) · [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [hyperdev.matsuoka.com — How Claude Code Got Better by Protecting More Context](https://hyperdev.matsuoka.com/p/how-claude-code-got-better-by-protecting) (published 10 Dec 2025) · [iwoszapar.com — Claude Code Best Practices: 8 Rules I Learned the Hard Way](https://www.iwoszapar.com/p/claude-code-best-practices) (published 19 Jun 2026, updated 05 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: Know the subagent limits before you plan around them

**Do:** Design workflows knowing Claude Code's default caps (all changeable via environment
variables — on Ubuntu, set one with `export CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION=100` in
your shell profile, e.g. `~/.bashrc`, then restart your shell or `source` the file — and all
🕒 verify live since they're version-gated): subagents can nest up to **3 layers** deep below
the main conversation by default (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`; this default has
changed across versions — v2.1.172-v2.1.216 allowed up to five layers, v2.1.217-v2.1.218
capped it at one, v2.1.219 raised it to the current default of three); a session can spawn at
most **200 subagents total** by default (`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`); at most
**20 subagents can run concurrently** by default (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`).
Independent reporting confirms these defaults were genuinely in flux again as recently as
21–24 Jul 2026 (briefly capped concurrency, disabled nesting outright, then reinstated
depth-3) before settling at the values above — don't hard-code a number into automation
without checking your installed version. A non-fork subagent never inherits your main
conversation's auto memory or history — it starts genuinely fresh (except the built-in
Explore/Plan agents, and except a "fork," which deliberately inherits everything).

**Why (beginner):** If you're chaining subagents (reviewer → verifier → fixer) and something
silently stops delegating, you may have hit the depth or count limit rather than hit a bug.
And if you expect a subagent to "remember" something from earlier in your session without
being told, it won't — each spawn starts cold unless you explicitly gave it persistent
`memory:` scope.

**Caveat / contested:** These exact defaults have changed repeatedly across recent Claude Code
versions, including as recently as three weeks before this snapshot — treat every number here
as a live value to re-check, not a fact to memorize.

**Sources:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) (fetched 06 Aug 2026) · [digitalapplied.com — Claude Code Put Guardrails on Its Own Agent Fleets](https://www.digitalapplied.com/blog/claude-code-subagent-depth-limits-budget-caps-2026) (Aug 2026)

**Confidence:** vendor-documented (the current default values); the recent-churn history is independently-corroborated

---

### Practice: Don't confuse Claude Code's /compact with Anthropic's separate API-level context management features

**Do:** If you're building your own agent directly on the Messages API (not using the Claude
Code CLI), Anthropic offers distinct server-side primitives: beta **server-side compaction**
(`compact-2026-01-12` beta header, `compact_20260112` strategy, default trigger at 150,000
input tokens, configurable), the **context editing** API (tool-result clearing, thinking-block
clearing), and the generally-available **memory tool** (`memory_20250818`, client-executed
file operations under `/memories` that your application implements). None of these are the
same mechanism as Claude Code's CLI `/compact` — Claude Code implements its own compaction
client-side and does not expose the API's `compact_20260112` strategy as a toggle.

**Why (beginner):** It's easy to read an Anthropic engineering blog post about "compaction" or
"the memory tool" and assume it describes what Claude Code does when you type `/compact`.
They're related concepts solving the same underlying problem (fixed context window,
long-running agent) but are different products aimed at different audiences (API developers
building custom agents vs. Claude Code's own CLI users).

**Caveat / contested:** Server-side compaction and task budgets are explicitly in **beta** as
of this writing — 🕒 verify live for header names, default trigger values, and model support
before depending on them in production.

**Sources:** [platform.claude.com/docs/en/build-with-claude/compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) (fetched 06 Aug 2026) · [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (fetched 06 Aug 2026) · [platform.claude.com/docs/en/build-with-claude/context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Match your expectations of context-window size to the actual model, and confirm which one Claude Code is using

**Do:** Context window size depends on the *model*, not on Claude Code itself. As of this
writing, most current-generation models — **Claude Sonnet 5, Opus 5 (GA 24 Jul 2026), Claude
Fable 5 and its restricted sibling Mythos 5 (GA 9 Jun 2026), Opus 4.6 and later, Sonnet
4.6** — default to a **1M-token** context window on the Claude API and major cloud providers
with no beta header required and no long-context price surcharge; older/smaller models (e.g.
Claude Sonnet 4.5, Haiku) are capped at **200K tokens**. Some hosting paths (certain
Bedrock/Google Cloud/Microsoft Foundry deployments) still run some models at a 200K window
even where the model otherwise supports 1M; on some models, 1M is a selectable `[1m]` variant
rather than simply the automatic default (Sonnet 5 runs at 1M with no variant to select). Run
`/model` in Claude Code to see and switch your active model — you can select Fable 5 directly
with `--model claude-fable-5`.

**Why (beginner):** "Claude's context window" is not one fixed number — assuming 200K (the
number most beginner tutorials still quote) when you're actually on a 1M-token model, or vice
versa, will throw off any estimate of how much you can paste in or how soon you'll hit
auto-compact. It's also easy to miss that Claude Fable 5 — currently Anthropic's most capable,
most coding-focused tier — exists at all if you're only skimming for "Sonnet" and "Opus."

**Caveat / contested:** 🕒 verify live — model names, default context sizes, and which
hosting paths get the larger window change frequently; treat every number above as a snapshot
for 06 Aug 2026, not a permanent fact.

**Sources:** [platform.claude.com/docs/en/build-with-claude/context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 06 Aug 2026) · [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 06 Aug 2026, Fable 5/Mythos 5) · [platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Understand how prompt caching turns "large context" into "large recurring bill" — and what silently breaks the cache

**Do:** ⚠️ **WARNING** — Claude Code resends your full conversation history on every turn and
relies on server-side prompt caching to make that cheap; several ordinary actions invalidate
that cache and force a full, expensive, uncached reprocess of the entire conversation on the
very next turn: **switching models or effort level mid-session**, **turning on fast mode**,
**denying an entire tool**, **enabling or disabling a plugin that provides MCP servers**,
**upgrading Claude Code** (rebuilds on the first turn after restart), and **resuming a
session after the cache has expired** (idle longer than the TTL — 1 hour on a Claude
subscription, 5 minutes by default on an API key/cloud provider, or once you're on usage
credits). An MCP server connecting, disconnecting, or changing its tool list is **not**
automatically on this list — Claude Code's default "deferred tools" behavior on supported
models means a server change only appends new content and doesn't disturb what's already
cached; full invalidation there only happens if tool search is disabled/unavailable or a
tool is set to `alwaysLoad`, forcing it into the cached prefix. This list is not exhaustive —
check the vendor doc for the current complete set. Compacting itself is comparatively cheap
while the cache is warm, but compacting a very old, cold session is one of the most expensive
single actions you can trigger.

**Why (beginner):** This is where "why did that one message cost so much / take so long"
comes from. None of these triggers are obvious from the terminal — a model switch "feels
free" until the next, much slower turn. Pick your model and effort level at the start of a
session and avoid changing them mid-task if you're cost-sensitive.

**Caveat / contested:** None found — this is Anthropic's own detailed accounting of its
caching mechanics; no independent source was found disputing it, but none was found
double-checking the specific numbers either.

**Sources:** [code.claude.com/docs/en/prompt-caching](https://code.claude.com/docs/en/prompt-caching) (fetched 06 Aug 2026) · [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Push large/verbose tool output out of context with hooks, code-intelligence plugins, or subagents rather than letting Claude read it raw

**Do:** If a command routinely produces huge output (a full test run, a multi-thousand-line
log file), don't let Claude read it raw into context. One concrete option: add a
`PostToolUse` hook in `.claude/settings.json` that pipes a command's raw output through a
filter (e.g. `grep -E 'FAIL|ERROR'`) before Claude ever sees it, so a 5,000-line test run
becomes the 10 lines that actually matter. Alternatively, install a code-intelligence plugin
so "go to definition" replaces grep-then-read-several-candidates, or delegate the whole
operation to a subagent so the verbose output lives in a context window you discard.

**Why (beginner):** Independent analysis of Claude Code sessions has estimated that raw
file/log reading can account for 60-80% of context consumption in a typical long session,
which is also what forces premature compaction. Vague prompts like "investigate the
codebase" make this worse, prompting the agent to read far more files than the task actually
needs.

**Caveat / contested:** The "60-80%" figure is a single blog's estimate, not a measured
benchmark across many sessions — treat it as directional, not exact.

**Sources:** [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 06 Aug 2026) · [bytebell.ai — Claude Code Keeps Compacting and Losing My Work](https://bytebell.ai/blog/claude-code-compacting-losing-work/) (published 18 Mar 2026) · [iwoszapar.com — Claude Code Best Practices: 8 Rules I Learned the Hard Way](https://www.iwoszapar.com/p/claude-code-best-practices) (published 19 Jun 2026, updated 05 Aug 2026)

**Confidence:** independently-corroborated

---

### Practice: Remember that every new session starts with an empty context window — only CLAUDE.md and auto memory carry over

**Do:** Each `claude` invocation (a genuinely new session, as opposed to `--continue`/
`--resume`) begins with a fresh, empty context window. Nothing from a previous session's
conversation is present unless it was written to CLAUDE.md or to Claude's own auto-memory
(`MEMORY.md` plus topic files, on by default, capped at 200 lines/25KB for what auto-loads).
Use `claude --continue`/`--resume`/the `/resume` picker to reopen the *same* session under the
same ID and keep appending; use `--fork-session`/`/branch` (or `/subtask` for an in-session
fork) to copy history into a *new* session ID without disturbing the original.

**Why (beginner):** Beginners sometimes assume Claude "remembers the project" between
separate terminal sessions the way a human colleague would. It doesn't, unless you or Claude
wrote that knowledge down somewhere that reloads — CLAUDE.md for things you want to state as
rules, auto memory for things Claude picked up on its own.

**Caveat / contested:** File-edit checkpoints (`Esc` `Esc` / `/rewind`) are a separate
mechanism from context/session management — they let you undo file changes and remain
available across a resume, but they don't restore conversation context, and a restore skips
symlinked/hard-linked files.

**Sources:** [code.claude.com/docs/en/how-claude-code-works](https://code.claude.com/docs/en/how-claude-code-works) (fetched 06 Aug 2026) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

## Part 2 — OpenAI Codex CLI

> All slash/at-commands below (`/compact`, `/agent`, `/status`) are typed **inside the
> running `codex` interactive session**, not at the Ubuntu bash prompt.

### Practice: Know what auto-compaction actually keeps — plan around the loss, don't fight it

**Do:** When a Codex CLI session's token usage crosses a threshold, Codex silently summarizes
the conversation and replaces most of the history. What survives, per two of three
independent technical write-ups that examined the open-source `codex-rs` code (a third
describes a materially different retention rule — see caveat): (1) one summary "handoff"
message — an encrypted server-side blob for OpenAI-hosted models, or a plaintext
`_summary`-prefixed message for other providers — plus (2) roughly the last ~20,000 tokens of
your own recent messages. Everything else (prior assistant replies, tool output, file
contents already read) is discarded. Don't assume compaction remembers a constraint you
mentioned once, ten tool calls ago — restate anything critical in your next message if you're
not sure it survived.

**Why (beginner):** Long-running agent sessions can't hold an unlimited transcript — the
model has a fixed context window. Codex's fix (like other coding agents) is to periodically
compress the conversation into a short summary so it can keep going. That summary is written
by an LLM and is lossy by design; if it misses a detail, that detail is effectively gone for
the rest of the session.

**Caveat / contested:** The three independent technical write-ups examined do **not** fully
agree: two describe the "summary + ~20K-token tail of recent user messages" mechanic above,
but a third (justin3go, Apr 2026) instead describes Codex physically deleting all assistant
replies and tool-related messages while preserving **all** user messages verbatim, with no
20K-token cap mentioned. None of this is spelled out in OpenAI's own docs — the mechanics
come from independent reverse-engineering, not an OpenAI blog post explaining the design, and
OpenAI's own docs confirm the underlying `/responses/compact` endpoint exists without
describing Codex CLI's specific retention policy.

**Sources:** [Codex CLI Context Compaction: Architecture, Configuration, and Managing Long Sessions](https://codex.danielvaughan.com/2026/03/31/codex-cli-context-compaction-architecture/) (Daniel Vaughan, 31 Mar 2026, updated 05 Aug 2026) · [Context Compaction Research: Claude Code, Codex CLI, OpenCode, Amp (gist)](https://gist.github.com/badlogic/cd2ef65b0697c4dbe2d13fbecb0a0a5f) (Mario Zechner, 02 Dec 2025) · [Shedding Heavy Memories: Context Compaction in Codex, Claude Code, and OpenCode](https://justin3go.com/en/posts/2026/04/09-context-compaction-in-codex-claude-code-and-opencode) (Justin3go, Apr 2026) · [Compaction — OpenAI API docs](https://developers.openai.com/api/docs/guides/compaction) (OpenAI, fetched 06 Aug 2026)

**Confidence:** independently-corroborated for the general "summary replaces most of history" mechanic; the specific ~20K-token tail figure is corroborated by two of three sources, contradicted by the third

---

### Practice: Trigger `/compact` yourself at a natural checkpoint, with instructions, instead of letting it fire mid-task

**Do:** Run `/compact` manually when you finish a logical chunk of work (a passing test, a
merged sub-feature) rather than waiting for auto-compaction to hit mid-tool-call. In current
Codex CLI (v0.117.x and later, per independent testing), you can queue follow-up instructions
during a manual compact without losing them, e.g. `/compact Focus particularly on the
authentication refactor and the three failing tests`.

**Why (beginner):** If you let the context fill up on its own, compaction can fire in the
middle of a multi-step tool call, and the summary writer has no idea which of the last
hundred lines of diff output mattered. Compacting on your own terms, with a hint about what's
important, produces a better summary and a cleaner spot to resume from.

**Caveat / contested:** The `/compact <instructions>` feature and its version number come
from one independent technical blog re-reading the CLI's changelog and source; it is
plausible but not confirmed by an OpenAI changelog entry we could fetch directly. The exact
mechanism (does the instruction get "threaded into the summarization prompt," as a stronger
reading might suggest, or simply queued so it isn't lost?) is not fully specified by the
source — treat "queued so you don't lose it" as the confirmed claim.

**Sources:** [Codex CLI Context Compaction: Architecture, Configuration, and Managing Long Sessions](https://codex.danielvaughan.com/2026/03/31/codex-cli-context-compaction-architecture/) (Daniel Vaughan, 31 Mar 2026, updated 05 Aug 2026)

**Confidence:** thin (single source for the specific `/compact <instructions>` syntax and version number; the general existence of a manual `/compact` command is corroborated elsewhere but the instruction-queueing detail is not)

---

### Practice: Keep AGENTS.md short and let the discovery chain do the organizing, don't write one giant file

**Do:** Codex reads `AGENTS.md` once per run (once per launched CLI session) before doing any
work, walking from your Codex home directory (`~/.codex`) down through the git root to your
current directory, checking for `AGENTS.override.md` then `AGENTS.md` at each level, and
concatenating what it finds — files closer to your working directory take precedence because
they're appended later in the combined prompt. The combined size defaults to a 32 KiB cap
(`project_doc_max_bytes`; 64 KiB is documented as an example of a higher value, not a
ceiling); Codex stops adding files once it hits the configured limit, silently. Keep the root
file to the common cases and high-level conventions, and push anything workflow-specific into
nested subdirectory files instead of one long document.

**Why (beginner):** Everything in AGENTS.md gets loaded into the context window before the
model does any work — it isn't optional background, it's tokens you're spending on every
single run. Independent testing has found verbose AGENTS.md files can actively hurt: one
report describes an agent reading a full service-topology write-up meant for architecture
decisions, pulling in ~80K tokens of irrelevant context for a two-line config change, and
getting confused about which service owned the setting.

**Caveat / contested:** OpenAI's own docs describe the size cap and precedence order but
don't give an explicit line-count recommendation. The "100-150 lines" guidance below comes
from an independent AI-coding-tool vendor's own testing (a different product, not
Codex-specific), so treat the exact number as a rule of thumb rather than an OpenAI-verified
figure.

**Sources:** [Custom instructions with AGENTS.md — ChatGPT Learn](https://learn.chatgpt.com/docs/agent-configuration/agents-md) (OpenAI, fetched 06 Aug 2026) · [A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all.](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files) (Augment Code / Slava Zhenylenko, 22 Apr 2026, updated 18 Jun 2026)

**Confidence:** independently-corroborated (official OpenAI docs on structure/size cap + an independent vendor's field testing on optimal length and the cost of bloat)

---

### Practice: Use `codex resume` / `codex fork` instead of re-typing context into a new session — but know it can't undo an earlier compaction's losses

**Do:** Every Codex CLI session is saved automatically as a JSONL (a line-delimited JSON log
format) "rollout" transcript under `~/.codex/sessions/`. `codex resume` reopens the picker of
recent sessions in the current repo (or `--all` across directories, `--last` to skip straight
to the most recent), and appends new turns to that same transcript, carrying forward the
model's plan history and prior approvals. Use `codex fork` (branch from a past session
without touching the original) when you want to try an alternative approach without losing
the original thread; `codex unarchive` restores a session that had been archived (moved out
of the active picker) back to resumable status.

**Why (beginner):** Resuming means you don't have to re-explain the whole task history to a
fresh session — the tool reconstructs the conversational state for you. But if that session
already went through one or more auto-compactions, the detail lost during compaction is gone
from the transcript too; resume replays what's there, it doesn't recover what was already
summarized away.

**Caveat / contested:** OpenAI's own docs confirm `codex resume` exists but describe it in a
single line, without documenting `--all`, `--last`, `codex fork`, `codex unarchive`, or the
`~/.codex/sessions/` path directly — all of that flag- and path-level detail rests on one
independent technical blog, not an OpenAI-authored reference. Treat the existence of
resume/fork as vendor-confirmed and the specific flags/lifecycle as independently-sourced
only.

**Sources:** [Codex CLI — ChatGPT Learn](https://learn.chatgpt.com/docs/codex/cli) (OpenAI, fetched 06 Aug 2026) · [Codex CLI Session Lifecycle: Archive, Resume, Fork, and Compact Management](https://codex.danielvaughan.com/2026/06/05/codex-cli-session-lifecycle-archive-resume-fork-compact-management/) (Daniel Vaughan, 05 Jun 2026, updated 05 Jul 2026)

**Confidence:** thin (the specific flags and session-file lifecycle rest on a single independent source; only the bare existence of `resume` is vendor-confirmed)

---

### Practice: Delegate read-heavy exploration to subagents to keep the main thread's context clean — don't use them for conflicting writes

**Do:** Ask Codex to delegate focused work to specialized agents for parallelizable,
read-heavy tasks (codebase exploration, running down a bug across several files, checking an
API's docs) — each spawned subagent gets its own clean context window and works
independently; the main thread waits for all requested subagents, then folds their distilled
findings (not raw logs/tool output) back into one consolidated response. Use `/agent` to
inspect or switch between running agent threads. Reserve subagents for tasks that don't need
to see each other's intermediate work, and avoid running several agents that edit the same
files concurrently.

**Why (beginner):** If one agent had to read every file and every test log itself, your main
session's context would fill up fast with noise you don't need for the final answer.
Subagents let exploration happen "off to the side" and only the conclusions come back, which
uses less of your main context — at the cost of more total tokens burned across all the
agents combined.

**Caveat / contested:** Codex's official docs are explicit that "subagent workflows consume
more tokens than comparable single-agent runs" and warn that agents editing code
simultaneously "can create conflicts and increase coordination overhead" — this is a
tradeoff, not a free win. Independent testing (not in OpenAI's own docs, which instead
document a related `max_concurrent_threads_per_session` setting) adds that deep, multi-level
subagent fan-out multiplies token usage and latency at each level, and that sequential
subagent pipelines (reproduce → debug → fix) tend to fail because information degrades at
each handoff, whereas genuinely parallel, independent subagent tasks work well.

**Sources:** [Subagents — ChatGPT Learn](https://learn.chatgpt.com/docs/agent-configuration/subagents) (OpenAI, fetched 06 Aug 2026) · [A field guide to multi-agent code review with custom subagents](https://harnez.ai/posts/multi-agent-code-review-codex/) (harnez.ai, 10 May 2026)

**Confidence:** independently-corroborated

---

### Practice: Watch for the "re-read spiral" on large files — extract instead of reading whole files, and if you're mid-spiral, stop it now

**Do:** Because compaction discards previously-read file contents (see above), an agent that
keeps needing the same large file will re-read it in full after every compaction, which
refills the context, which triggers another compaction, in a self-reinforcing loop. This has
been reported repeatedly by users, including as recently as 20 Jul 2026. Mitigate by asking
Codex to extract relevant sections with `grep`/`sed`-style targeted reads instead of loading
whole large files, and keeping genuinely large files (config specs, generated schemas) out of
routine re-reads. **If you notice a session has compacted 3+ times with no forward progress:
press Ctrl+C to interrupt the CLI immediately** rather than letting it keep running — don't
wait and watch, since each additional loop iteration burns more quota with nothing to show
for it. After interrupting, either start a fresh session, or use `codex fork` from a saved
checkpoint captured before the spiral began if you want to preserve earlier, good progress.

**Why (beginner):** This is a real, still-open failure mode, not a hypothetical: independent
bug reports describe a single 610 KB OpenAPI spec file being re-read 53 times in one session
(a reported 10-20x token multiplier), and separate forum reports of an "infinite compaction
loop" running overnight, with one user reporting it consumed their entire weekly usage limit
on a single stuck task. Because Codex CLI usage is capped per 5-hour window and per week on
ChatGPT Plus/Pro/Business plans, a stuck loop like this can cost you real, non-refundable
quota, not just time — so the moment you notice repeated compaction with no progress, stop
the process rather than hoping it recovers on its own.

**Caveat / contested:** These are user-filed GitHub issues and forum threads, not an OpenAI
acknowledgment of a systemic bug — the maintainers' resolution status on the underlying
issues reviewed here is mixed (one closed with no visible fix note, one still open as a
feature request for "pinned files" retention). A specific "~80% of a monthly quota" figure
and a "v0.112 / xhigh-reasoning-effort" attribution circulated in earlier drafts of this
research but could not be located in any of the three primary sources below on direct
re-fetch, and have been dropped rather than republished unsupported. Treat this as an ongoing
risk to manage, not a bug that's definitely fixed as of this writing.

**Sources:** [GitHub issue #14120 — "codex just compacts repeatedly for hours at a time before it is able to make a change"](https://github.com/openai/codex/issues/14120) (reported 09 Mar 2026, closed) · [GitHub issue #16839 — "Compaction-aware context retention for frequently re-read files"](https://github.com/openai/codex/issues/16839) (filed 05 Apr 2026, open) · [OpenAI Developer Community — "Codex Infinite Context Automatically Compacted Loop Consumed Over 50% of My Usage"](https://community.openai.com/t/codex-infinite-context-automatically-compacted-loop-consumed-over-50-of-my-usage/1387585) (posted 20 Jul 2026) · [Codex CLI Context Compaction: Architecture, Configuration, and Managing Long Sessions](https://codex.danielvaughan.com/2026/03/31/codex-cli-context-compaction-architecture/) (Daniel Vaughan, updated 05 Aug 2026)

**Confidence:** independently-corroborated (three separate user-filed reports on different platforms, spanning March–July 2026, describing the same mechanism, plus an independent technical write-up explaining why it happens); ⚠️ **WARNING** — this failure mode can consume a large fraction of a paid usage quota, including an entire weekly cap in one documented report, with no work product to show for it

---

### Practice: Treat the model's context-window size and its pricing tier as a moving target — check it live, don't assume more tokens means better answers

**Do:** 🕒 **verify live.** As of 06 Aug 2026, OpenAI's own models page lists **GPT-5.6 Sol,
Terra, and Luna** each at **1,050,000-token context / 128,000-token max output**; OpenAI's
desktop-app documentation describes Sol as the default "Power setting" model (the CLI itself
is not explicitly documented as defaulting to Sol, so treat "Sol" as the recommended, not
confirmed-default, CLI model), and OpenAI has announced GPT-5.4 and GPT-5.4 mini retire from
Codex for ChatGPT-signed-in users on **31 Aug 2026** (roughly 3.5 weeks after this snapshot —
this line needs re-checking in any refresh published after that date). Separately, and
distinct from Codex CLI's own 272,000-token effective-context cap (see the earlier "effective
context" practice), OpenAI's own GPT-5.5 model page documents that requests exceeding
roughly 272,000 input tokens on **GPT-5.5 specifically** are billed at a 2x input / 1.5x
output surcharge for the whole request — this pricing rule is not confirmed for GPT-5.6 in
the page fetched this run, so don't assume it applies unscoped to the current model
generation.

**Why (beginner):** Model names, context limits, and prices in this space change every few
weeks, and Codex CLI will silently start recommending or defaulting to a new model. A number
that's accurate today may be wrong by the time you read this — always sanity-check the live
figure rather than trusting a cached one, including this one.

**Caveat / contested:** Independent research (Chroma Research, an AI infrastructure company
whose commercial product is retrieval, not affiliated with OpenAI) tested 18 frontier models,
including GPT-family models, and found accuracy "varies significantly as input length
changes, even on simple tasks" — a general LLM finding, not Codex-CLI-specific testing, and
Chroma's own report does not publish a single headline percentage figure for this, so no
specific number is asserted here. It directly argues against "just dump more into context" as
a strategy regardless.

**Sources:** [Models — ChatGPT Learn](https://learn.chatgpt.com/docs/models) (OpenAI, fetched 06 Aug 2026) · [developers.openai.com — Models](https://developers.openai.com/api/docs/models) (OpenAI, fetched 06 Aug 2026, confirms 1.05M/128K for Sol/Terra/Luna directly) · [GPT-5.5 — OpenAI API model docs](https://developers.openai.com/api/docs/models/gpt-5.5) (OpenAI, fetched 06 Aug 2026; 272K surcharge scoped to GPT-5.5) · [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot) (Chroma Research, 14 Jul 2025, fetched 06 Aug 2026)

**Confidence:** vendor-documented for the model/pricing figures; independently-corroborated for the general "accuracy degrades with input length" caution

---

### Practice: Pick the least-permissive sandbox/approval mode that gets the job done — never reach for `--yolo` outside a disposable environment

**Do:** Codex CLI's sandbox has three modes — `read-only` (no writes), `workspace-write` (the
default for trusted repos: read/write inside the project directory and temp dirs, plus safe
commands like `ls`/`find`), and `danger-full-access` (no filesystem or network boundary at
all). Layered on top, the approval policy (`untrusted` / `on-request`, the default / `never`)
controls when Codex pauses to ask before acting. ⚠️ The full flag for removing both
protections is `--dangerously-bypass-approvals-and-sandbox` (aliased `--yolo`); `--full-auto`
is a narrower, now **deprecated** (with a compatibility path) convenience flag that forces
`workspace-write` with auto-approval and overrides any `--sandbox` flag you also pass. Default
to `workspace-write` + `on-request` for normal work, and only use `danger-full-access`/
`--yolo` inside a container or VM you're prepared to lose.

**Why (beginner):** ⚠️ **WARNING.** `danger-full-access` means Codex can read and write
anything on your machine and reach the network with no confirmation prompts — official docs
describe it as "Elevated Risk." It is not a beginner default and shouldn't be reached for just
to avoid answering approval prompts; opening a malicious or compromised project in that mode
means trusting the model with the same filesystem and network access you personally have, with
no sandbox boundary stopping it from acting on that access.

**Caveat / contested:** More permissive modes also mean more verbose tool output (broader
command output, more files touched) flowing back into the transcript on every turn, which —
per the compaction mechanics above — fills the context window faster and can bring on
auto-compaction sooner. Neither source we fetched explicitly quantifies this token-cost side
effect; it's an inference from how the sandbox and compaction docs describe their respective
behaviors, so we're not asserting it as independently measured.

**Sources:** [Agent approvals & security — ChatGPT Learn](https://learn.chatgpt.com/docs/agent-approvals-security) (OpenAI, fetched 06 Aug 2026) · [How Codex CLI Flags Actually Work (Full-Auto, Sandbox, and Bypass)](https://www.vincentschmalbach.com/how-codex-cli-flags-actually-work-full-auto-sandbox-and-bypass/) (Vincent Schmalbach, 15 Jan 2026)

**Confidence:** independently-corroborated for the mode names, the flag, the deprecation note, and the risk framing; thin/inference-only for the "more permissive mode = faster context fill" side effect noted in the caveat

---

## Part 3 — Google Gemini CLI

> ⚠️ **Scope note, read first:** at Google I/O on 19 May 2026 Google announced it is retiring
> the standalone **Gemini CLI** for free and paid consumer tiers in favor of a new
> **Antigravity CLI**, effective **18 June 2026** — with no announced grace period; the
> `gemini` binary simply stops answering requests on affected accounts (any cron job — a
> Linux scheduled task — or CI/CD script that shells out to `gemini` breaks that day). Only
> accounts with a paid Gemini Code Assist Standard/Enterprise license, Gemini Code Assist for
> GitHub, or a paid Gemini API key keep the old CLI working past that date. Everything below
> describes the Gemini CLI mechanics as documented; see the last practice for what carries
> over to Antigravity CLI and what could not be independently verified there. 🕒 verify live —
> check which tier you're on before relying on any of this in automation. All slash/at-commands
> below (`/memory`, `/compress`, `/clear`, `/chat`, `@subagent_name`) are typed **inside the
> running `gemini` session**, not at the Ubuntu shell prompt.

### Practice: Know what's already in context before you type anything — GEMINI.md loads on every turn

**Do:** Gemini CLI assembles instructional context hierarchically and re-sends it with every
prompt: a global file at `~/.gemini/GEMINI.md` (rules for every project), project-root and
ancestor `GEMINI.md` files, and subdirectory `GEMINI.md` files that load "just-in-time" when
the CLI's tools touch that directory. The CLI footer shows a count of currently loaded context
files. Run `/memory show` at any point to see the full, concatenated text actually being sent
to the model, and `/memory refresh` to force a re-scan after you (or Gemini) edit a
`GEMINI.md` file mid-session. The default filename is configurable via `context.fileName` in
`settings.json` if you want a different name or multiple files.

**Why (beginner):** New users assume the model only sees what they type. In Gemini CLI a
real, often-invisible chunk of every turn is spent on `GEMINI.md` content loaded from three
different locations — and editing that file on disk does **not** retroactively change turns
you've already sent; you need `/memory refresh` (or a fresh session) for it to take effect.

**Caveat / contested:** None found on the loading mechanism itself. No official guidance
quantifies how many tokens this typically consumes, so treat "how much of my budget is
GEMINI.md eating" as something to check yourself with `/memory show` and `/stats`, not
something vendor docs give you a number for.

**Sources:** [github.com/google-gemini/gemini-cli — GEMINI.md docs](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md) (fetched 06 Aug 2026) · [geminicli.com/docs/cli/tutorials/memory-management](https://geminicli.com/docs/cli/tutorials/memory-management/) (fetched 06 Aug 2026) · [aipositive.substack.com — A Look at Context Engineering in Gemini CLI](https://aipositive.substack.com/p/a-look-at-context-engineering-in) (Paul Datta, published 18 Sep 2025, independent)

**Confidence:** independently-corroborated

---

### Practice: Keep GEMINI.md lean, modular, and reviewed — it's always-loaded working memory, not a wiki

**Do:** Google's own tutorial recommends keeping GEMINI.md instructions "actionable and
relevant to code generation," using negative constraints ("explicitly telling the agent what
*not* to do... is often more effective than vague positive instructions"), and reviewing the
file periodically to remove outdated rules. Break large files into smaller pieces with the
`@file.md` import syntax (relative or absolute paths) instead of one giant file. Keep the
global `~/.gemini/GEMINI.md` for truly universal rules and push project-specific detail down
into the project-root and subdirectory files so it doesn't bleed into unrelated projects.

**Why (beginner):** Every line in every loaded GEMINI.md file is resent on every single
prompt, whether or not it's relevant to the current task — a bloated file is a recurring tax
on every turn's budget, not a one-time cost. Segregating global vs. project content also stops
a rule you wrote for one project from quietly nudging your behavior on an unrelated one.

**Caveat / contested:** No official numeric line/size limit is published for GEMINI.md
(unlike some competing tools that publish a target line count) — this is a qualitative
recommendation, not an enforced or measured cap.

**Sources:** [geminicli.com/docs/cli/tutorials/memory-management](https://geminicli.com/docs/cli/tutorials/memory-management/) (fetched 06 Aug 2026) · [github.com/google-gemini/gemini-cli — GEMINI.md docs](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md) (fetched 06 Aug 2026)

**Confidence:** vendor-documented (all cited sources are Google-affiliated — geminicli.com and the google-gemini GitHub org are both official Google properties)

---

### Practice: Use /compress deliberately, and understand it replaces the whole history with one summary

**Do:** Run `/compress` to "replace the entire chat context with a summary" when a long
session is getting unwieldy or you're approaching the model's limit — it frees space "for
more discussion without starting from scratch." Gemini CLI also compresses automatically: the
base mechanism triggers off `model.compressionThreshold` (a fraction of context usage,
default **0.5**, requires restart to change) and, as of CLI **v0.38.0** (14 Apr 2026), an
additional "Context Compression Service" can route file content through **FULL / PARTIAL /
SUMMARY / EXCLUDED** tiers — but that newer service sits behind **experimental, off-by-default**
settings (`experimental.contextManagement`, `experimental.generalistProfile`, both default
`false`), so most installs are still running on the older, simpler threshold-based
auto-compress. Check `/stats` → `model` to watch token counts before you hit either trigger.

**Why (beginner):** Unlike some competing tools that preserve a structured table of what
survives, Gemini's `/compress` is a single, wholesale rewrite of the conversation into a
summary — there's no partial/selective compaction to reason about, which is simpler but also
means you lose fine detail in one shot. Knowing the default threshold (50% of the context
budget) tells you roughly how much runway you have before it fires unasked.

**Caveat / contested:** 🕒 verify live — the newer Context Compression Service is explicitly
experimental and its defaults/behavior may change as Google refines it; the setting names
above are confirmed against Gemini CLI's own configuration reference and the merging pull
request, but their on/off status and thresholds change across releases. Separately, one P0
bug (GitHub issue #16213, filed 09 Jan 2026, closed via PR #16914) reported the CLI
repeatedly attempting compression every turn without actually shrinking context — resolved,
but a reminder that an endless "Compressing chat history..." loop is a known-and-fixed
failure mode, not something to just wait out indefinitely if you hit it on an old build.

**Sources:** [geminicli.com/docs/reference/commands](https://geminicli.com/docs/reference/commands/) (fetched 06 Aug 2026) · [geminicli.com/docs/reference/configuration](https://geminicli.com/docs/reference/configuration/) (fetched 06 Aug 2026) · [geminicli.com/docs/changelogs](https://geminicli.com/docs/changelogs/) (fetched 06 Aug 2026) · [github.com/google-gemini/gemini-cli/pull/24483](https://github.com/google-gemini/gemini-cli/pull/24483) (merged 02 Apr 2026) · [github.com/google-gemini/gemini-cli/issues/16213](https://github.com/google-gemini/gemini-cli/issues/16213) (filed 09 Jan 2026, closed)

**Confidence:** vendor-documented

---

### Practice: Write anything precious to GEMINI.md or /memory add — don't trust it to survive compression

**Do:** GEMINI.md content and facts saved with `/memory add <text to remember>` — replace the
placeholder with your own text; the command appends it to your **global** `~/.gemini/GEMINI.md`
under a `## Gemini Added Memories` heading (not the project file) — are explicitly protected
from `/compress` and automatic compression: they're re-read from disk, not from conversation
history, so they survive a summary pass untouched. Everything else in the conversation — exact
line numbers, "we tried X and rejected it," intermediate reasoning — is fair game to be
summarized away. If a fact must outlive compression, put it in GEMINI.md or `/memory add` it;
don't rely on it staying in the transcript.

**Why (beginner):** This is the practical version of "why did Gemini forget what we agreed
five minutes ago" — if it wasn't written to a file the CLI reloads, a compression pass can
legitimately drop it as a "detail," not a bug.

**Caveat / contested:** Independent commentary reports the flip side isn't perfectly reliable
either: one write-up notes facts added via `/memory add` "aren't consistently recalled" by
users in practice, even though they're technically protected from compression — treat
`/memory add` as "protected from compression" and "always perfectly obeyed" as two different
claims; only the first is well-documented.

**Sources:** [yet-another-changelog.ai (Vibe Coding Academy) — Gemini CLI Auto Context Compression](https://www.yet-another-changelog.ai/changelog/gemini-cli-automatic-context-compression-service) (fetched 06 Aug 2026, independent) · [geminicli.com/docs/tools/memory](https://geminicli.com/docs/tools/memory/) (fetched 06 Aug 2026, documents the `save_memory` tool behind `/memory add`)

**Confidence:** independently-corroborated

---

### Practice: Use /clear for a genuine fresh start; use /compress to keep going on the same task

**Do:** When you're switching to fully unrelated work, run `/clear` rather than `/compress`.
The project's own merged pull requests confirm `/clear` clears the model's context window, not
just the terminal display, while preserving your up-arrow input history so you can still
recall previous prompts you typed.

**Why (beginner):** `/compress` is for shrinking the footprint of the *same* task; `/clear`
is for genuinely starting over. Using `/compress` when you meant to start fresh leaves a
stale summary of the old task quietly consuming budget and biasing the model toward the wrong
problem.

**Caveat / contested:** None found in this snapshot's re-verification.

**Sources:** [geminicli.com/docs/reference/commands](https://geminicli.com/docs/reference/commands/) (fetched 06 Aug 2026) · [github.com/google-gemini/gemini-cli/pull/14182](https://github.com/google-gemini/gemini-cli/pull/14182) (merged 01 Dec 2025, fetched 06 Aug 2026) · [github.com/google-gemini/gemini-cli/issues/10601](https://github.com/google-gemini/gemini-cli/issues/10601) (opened 06 Oct 2025, closed by that PR)

**Confidence:** vendor-documented

---

### Practice: Checkpoint long or multi-day sessions with /chat save, /chat resume, and /chat list

**Do:** Use `/chat save <tag>` to persist the full conversation state to a project-specific
checkpoint (default location `~/.gemini/tmp/<project_hash>/` on Linux/macOS,
`C:\Users\<YourUsername>\.gemini\tmp\<project_hash>\` on Windows), `/chat resume <tag>` to
pick it back up, and `/chat list` to see what's saved — all scoped to "that same project," so
a tag saved in one repo isn't visible from another.

**Why (beginner):** For work that spans days or that you want to branch (try approach A,
save, try approach B from the same starting point), this beats leaving one enormous terminal
session open — you get a named restore point instead of hoping the scrollback is still there.

**Caveat / contested:** None found; the project-scoping (can't resume a chat saved in a
different project) is a real limitation to plan around, not a bug.

**Sources:** [geminicli.com/docs/reference/commands](https://geminicli.com/docs/reference/commands/) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Delegate exploration and parallel work to subagents so it never enters the main context window

**Do:** Gemini CLI ships built-in subagents (`generalist`, `cli_help`, `codebase_investigator`,
and an opt-in `browser_agent` requiring Chrome 144+, disabled by default) and lets you define
custom ones as Markdown files with YAML frontmatter (a structured metadata block at the top of
a Markdown file, delimited by `---` lines) under `.gemini/agents/*.md` (project) or
`~/.gemini/agents/*.md` (user), with fields for `name`, `description`, `kind` (local/remote),
`tools` (with wildcards like `*`, `mcp_*`), `mcpServers` (which MCP — Model Context Protocol —
servers the subagent can reach), `model`, `temperature` (a 0-to-1-ish setting controlling how
random/varied the model's word choices are — lower is more predictable, higher is more
varied; leave it at the default unless you have a specific reason to change it), `max_turns`,
and `timeout_mins`. Invoke one explicitly with `@subagent_name your task`, or let the main
agent pick one automatically when a task matches its description. Each subagent "runs in its
own isolated context loop" — its conversation history and tool output never bloat the main
agent's context; only its final summary comes back as a tool result.

**Why (beginner):** This is one of the biggest levers for keeping a long session usable:
instead of having the main agent read dozens of files or run a whole test suite inline (which
permanently occupies your main context budget), hand that off to a subagent and only pay for
the summary it hands back.

**Caveat / contested:** Google's own announcement frames this explicitly as a fix for
"context rot" and "context pollution," and independent trade-press coverage of the same
launch corroborates the mechanics (isolated context window, tool restriction, parallel
dispatch) while also noting rougher edges: one early-adopter comment quoted in that coverage
says "Google should invest more in stability and UI/UX for gemini-cli. At the moment, the
experience, even with the Pro plan, is quite poor" — treat subagents as a real, documented
capability with genuine early-days rough edges, not a flawless feature.

**Sources:** [geminicli.com/docs/core/subagents](https://geminicli.com/docs/core/subagents/) (fetched 06 Aug 2026) · [developers.googleblog.com — Subagents have arrived in Gemini CLI](https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/) (published 15 Apr 2026) · [infoq.com — Subagents in Gemini CLI Enable Task Delegation and Parallel Agent Workflows](https://www.infoq.com/news/2026/04/subagents-gemini-cli/) (published 20 Apr 2026, independent)

**Confidence:** independently-corroborated

---

### Practice: Know the subagent guardrails before you design a workflow around them

**Do:** Plan around documented defaults: a subagent forced-returns after **30 turns**
(`max_turns`) or **10 minutes** (`timeout_mins`) unless you raise them in its frontmatter;
subagents **cannot call other subagents** (recursion is blocked to prevent infinite loops and
runaway token usage); a subagent with no `tools:` list "inherits all tools from the parent
session" rather than starting restricted; and switching models with `/model` for your main
session does **not** override whatever model a subagent is configured to use — expect to see
other models show up in usage/`/stats` reports even after you manually picked one for
yourself.

**Why (beginner):** If a chain of delegated subagents silently stops working partway through,
it may be the recursion block or a turn/timeout cap, not a bug. And if your bill shows a
model you didn't select, check what your subagents are configured to use before assuming
something's wrong.

**Caveat / contested:** These are the documented defaults as of this snapshot; like most CLI
configuration, they're 🕒 verify live — check your installed version's docs before hard-coding
a number into automation.

**Sources:** [geminicli.com/docs/core/subagents](https://geminicli.com/docs/core/subagents/) (fetched 06 Aug 2026) · [geminicli.com/docs/cli/model](https://geminicli.com/docs/cli/model/) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Don't assume you know the context window size or that caching is something you configure — check the model, and know caching is automatic

**Do:** Context window size depends on which model Gemini CLI's `/model` "Auto" routing picked
for you, not on the CLI itself. Google's official Gemini 3 spec page lists **1M-token input /
64K-token output** for `gemini-3.1-pro-preview` and `gemini-3-flash-preview`, and the same
1M/64K for `gemini-3.1-flash-lite`; the still-active Gemini 2.5 series includes **Gemini 2.5
Flash at a documented 1M-token context window** (confirmed on Google's own pricing page).
Separately, Gemini's **implicit context caching** is "enabled by default for all Gemini 2.5
and newer models" at the API level — there is nothing to turn on, and Gemini CLI does not
expose manual cache management to you. Google states cost savings are passed through
automatically when a request hits a cache: **10% of the standard input-token rate** for the
cached portion (confirmed against Gemini 2.5 Flash: $0.03 cached vs. $0.30 standard; Gemini
2.5 Pro: $0.125 cached vs. $1.25 standard — both exactly 10%), plus a per-hour storage charge
($1.00/1M tokens/hour for Flash, $4.50/1M tokens/hour for Pro), which mainly helps when you
repeatedly send similar large context (e.g. the same big file) in back-to-back turns.

**Why (beginner):** Beginners sometimes assume "large context window" is a fixed, universal
number, or that they need to manually enable caching the way you might with a raw API
integration — neither is true inside Gemini CLI. The model auto-routing picks a model for
you, and caching is invisible plumbing, not a switch you flip.

**Caveat / contested:** 🕒 verify live, hard — context-window and cache-pricing figures are
exactly the kind of fast-moving, version-specific spec this research team has previously
found misquoted in blog posts (an earlier draft of this practice cited a "roughly 20%" cache
discount figure that, on re-fetch, did not match either the caching docs, which state no
percentage, or the pricing page, which shows 10% — corrected above). This pupil could not
independently confirm a Gemini 3.1 Pro-specific context-window figure beyond the official 1M
figure now available on Google's Gemini 3 spec page; a separately-circulating "2M" figure for
Gemini 3.1 Pro could not be traced to an official page and should be treated as unconfirmed.

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing) (fetched 06 Aug 2026) · [ai.google.dev/gemini-api/docs/gemini-3](https://ai.google.dev/gemini-api/docs/gemini-3) (fetched 06 Aug 2026) · [ai.google.dev/gemini-api/docs/caching](https://ai.google.dev/gemini-api/docs/caching) (fetched 06 Aug 2026) · [ai.google.dev/gemini-api/docs/long-context](https://ai.google.dev/gemini-api/docs/long-context) (fetched 06 Aug 2026)

**Confidence:** vendor-documented

---

### Practice: Budget for "thinking token" and context-reload cost blowups on long agentic sessions

**Do:** ⚠️ **WARNING** — agentic terminal sessions burn tokens differently than chat: the CLI
rereads files, replays diffs, and restuffs context on every turn, and current "thinking"
models bill their (invisible) reasoning tokens at full output-token rates, which one cost
analysis puts at **70-85% of the total output bill** on complex reasoning tasks. That same
analysis documented a real-world case from the Google AI Developer forum describing a user's
daily cost jumping from a few thousand KRW to 150,000-200,000 KRW (roughly $100-140) despite
*decreased* usage, driven by unbudgeted thinking-token volume after migrating to a
thinking-capable model. Watch `/stats` → `model` for token counts during long sessions, favor
`/compress` and subagent delegation to cut reread volume, and don't assume "fewer requests"
means "lower bill" once a thinking model is involved.

**Why (beginner):** This is the practical, out-of-pocket version of "context management" —
the same mechanics that make long sessions unwieldy (constant rereading, growing history) also
directly drive your bill on metered plans, and thinking-token costs in particular are easy to
miss because they don't show up as visible output.

**Caveat / contested:** Both the 70-85% figure and the KRW anecdote come from a single
publisher (a second source checked for this snapshot discusses the same general mechanism —
"output tokens, including the model's thinking tokens, cost several times more than input" —
but does not contain either specific number). Treat this as one detailed, internally-consistent
cost analysis, not independently cross-checked figures, and treat the specific percentages and
the KRW example as illustrative of a real, plausible pattern rather than a guaranteed
multiplier for your own workload.

**Sources:** [cloudzero.com/blog/gemini-pricing](https://www.cloudzero.com/blog/gemini-pricing/) (published 16 Jul 2026, updated 30 Jul 2026)

**Confidence:** thin (single publisher for the specific figures; the general cost mechanism is directionally corroborated elsewhere)

---

### Practice: Know that Gemini CLI itself is being superseded — check which tool you're actually documenting against

**Do:** As of this snapshot, Google is actively moving users off Gemini CLI onto
**Antigravity CLI** (a Go-based rewrite). Google's own migration guidance says Agent Skills,
Hooks, Subagents, and Extensions "carry over" conceptually (Extensions become Antigravity
plugins), and Antigravity's own changelog documents its own version of context-window
management independently of anything covered above — e.g. a **"context-compaction boundary"
indicator** added in CLI v1.1.3 (16 Jul 2026) so you can see where a previous compaction
happened, and its own asynchronous, isolated-context subagent model. This pupil confirmed
these specifics directly against Google's own `antigravity.google` docs and changelog, but
found no independent (non-Google) commentary analyzing Antigravity's context-management
mechanics in depth at initial research time — independent write-ups have begun to appear
since (e.g. describing a reported ~135,000-token auto-compaction trigger), but those were
surfaced only via search rather than a direct fetch this run and are not confirmed to the bar
this corpus requires, so that specific figure is not asserted as fact here — treat every
Antigravity-specific detail in this paragraph as vendor-sourced (or emerging/unconfirmed)
rather than independently verified.

**Why (beginner):** If you're reading Gemini CLI material (including this entry) after 18
June 2026 on a free or paid consumer-tier account, the `gemini` binary may no longer respond
at all — before troubleshooting a "broken" Gemini CLI, check whether you're actually supposed
to be on Antigravity CLI now. Enterprise Gemini Code Assist licenses, Gemini Code Assist for
GitHub, and paid Gemini API keys are the documented exceptions that keep the old CLI usable
past that date.

**Caveat / contested:** Independent tech-news coverage (a publisher separate from Google)
confirms the deprecation date and no-grace-period behavior, so that part is
independently-corroborated; the specific Antigravity context-management mechanics described
above remain vendor-sourced/thin, and could change quickly given how new the product is.

**Sources:** [developers.googleblog.com — An important update: transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) (published 19 May 2026) · [inventivehq.com — Gemini CLI Is Being Retired on June 18 — Meet Antigravity CLI](https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration) (published 13 Jun 2026, independent) · [antigravity.google/changelog](https://antigravity.google/changelog) (fetched 06 Aug 2026) · [antigravity.google/docs/cli/subagents](https://antigravity.google/docs/cli/subagents) (fetched 06 Aug 2026)

**Confidence:** contested (the deprecation/timeline facts are independently-corroborated; the Antigravity context-management mechanics are vendor-sourced/thin — split confidence, don't treat this whole entry as one uniform tier)

---

## Held pending fixes (not publish-ready as fact)

- **Antigravity CLI's precise context-management mechanics** (auto-compaction trigger token
  count, nested-subagent handling) — independent commentary is starting to appear but was only
  surfaced via search, not a direct fetch, this run; needs a follow-up fetch of a genuinely
  independent source before a specific figure (e.g. a ~135,000-token trigger) can be published
  as fact. ⚠ PENDING (#antigravity-independent-source-needed)
- **Antigravity CLI's actual default model** — reported by secondary sources as Gemini 3.5
  Flash, but not confirmed against an official Antigravity spec page this run. ⚠ PENDING
  (#antigravity-default-model-needs-live-fetch)
- **No independent (non-Anthropic) corroboration** was found for the specific mechanics of
  Claude's "context awareness" token-budget injection (`<budget:token_budget>` /
  `<system_warning>` tags) — mentioned only in passing above, deliberately not published as a
  standalone practice since it would rest on a single vendor source at the foundations
  (cross-tool) level. ⚠ PENDING (#claude-context-awareness-tags-single-source)
- **Codex CLI weekly/5-hour usage-limit numbers per ChatGPT plan tier** were only found on
  third-party pricing-aggregator blogs of uncertain reliability during research; not cited at
  the confidence bar this corpus requires. ⚠ PENDING (#codex-usage-limits-need-primary-source)
- **OpenAI's `openai.com/index/gpt-5-1-codex-max/` announcement** (reportedly describing an
  earlier Codex model as "the first model natively trained to operate across multiple context
  windows through compaction") returned HTTP 403 on every fetch attempt and was dropped per
  sourcing rules rather than cited from a search snippet. ⚠ PENDING
  (#codex-max-native-compaction-needs-fetchable-source)
- **Auto memory (`MEMORY.md`) as a Claude Code persistence mechanism distinct from CLAUDE.md**
  could only be verified against Anthropic's own docs this run; no independent (non-Anthropic)
  commentary discussing it in depth was located. ⚠ PENDING (#claude-auto-memory-needs-independent-source)

## CHANGELOG (grading → this entry)

1. [Skeptic KILL] Foundations: removed a fabricated "effective context fell short by up to
   99%" attribution to Chroma's Context Rot study — the only "99%" on that page is an
   unrelated inter-rater agreement score, and "effective context" doesn't appear on the page
   at all. Rewrote the practice around what Chroma actually measured (accuracy varies
   significantly with input length), with no invented percentage.
2. [Skeptic KILL] Foundations: removed a fabricated "60-70% recall" statistic attributed to a
   Redis blog post — the only ~60% figure on that page is an agreement rate between RAG and
   long-context answers, not a recall measurement. Deleted the claim; kept the two things the
   source actually supports (O(n²) attention/latency, the hybrid retrieve-then-load pattern).
3. [Skeptic KILL] Codex CLI: removed a fabricated quote ("across all experiments") and a
   fabricated "30-50%" degradation figure attributed to the same Chroma study — the real page
   says "across all models"/"across the GPT, Gemini, and Qwen model families," with no
   percentage. Rewrote without invented numbers and cross-referenced the corrected Foundations
   practice instead of repeating a second fabricated statistic drawn from the same source.
4. [Skeptic KILL] Gemini CLI: corrected a wrong context-cache discount figure — the draft said
   "roughly 20%"; Google's own pricing page shows cached input at exactly 10% of standard rate
   for both Flash ($0.03 vs $0.30) and Pro ($0.125 vs $1.25). Re-cited the storage charge to
   the pricing page (the caching page states no percentage or storage number at all).
5. [Skeptic FIX] Foundations: corrected the prompt-cache minimum-prefix range from
   "1,024–4,096" to "512–4,096" tokens (512 applies to the current flagship tier — Opus 5,
   Fable 5, Mythos 5).
6. [Skeptic FIX] Foundations: relabeled two practices from "independently-corroborated" to
   "vendor-documented" — multiple vendors each reporting their own numbers isn't independent
   corroboration of any single figure.
7. [Skeptic FIX] Foundations: removed an unconfirmed "~50%-full threshold" specific from the
   context-rot caveat — the cited arXiv paper doesn't state that threshold.
8. [Skeptic FLAG] Foundations: clarified that Chroma is a vector-database vendor with a
   commercial interest in this finding, not a neutral "independent research group" — applied
   the same clarification everywhere Chroma is cited (Foundations and Codex CLI sections).
9. [Skeptic FLAG] Foundations: dropped an unverifiable "20 Mar 2026" publish date on the
   Anthropic Cookbook citation.
10. [Skeptic FIX] Claude Code: corrected CLAUDE.md size guidance from a manufactured
    "under 200-300 lines" disagreement to "under ~200 lines" — all three sources (Anthropic's
    own docs plus two independent blogs) agree on 200 exactly.
11. [Skeptic FIX] Claude Code: corrected the prompt-cache/MCP claim — an MCP server
    connecting or disconnecting mid-session does *not* bust the cache by default (deferred
    tools, the default, only appends); full invalidation only happens when tools load directly
    into the prefix.
12. [Skeptic FIX] Claude Code: removed an unsupported quoted phrase ("two hundred files") not
    found in any cited source; kept the supported 60-80%-of-context statistic.
13. [Skeptic FLAG] Claude Code: swapped the `/memory` vs. `/context` description — `/context`
    shows what's actually loaded; `/memory` lists file locations, including files that don't
    exist yet.
14. [Skeptic FLAG] Claude Code: noted the cache-invalidation list isn't exhaustive and added
    the previously-missing "enabling/disabling a plugin that provides MCP servers" trigger.
15. [Skeptic FLAG] Claude Code: added the Claude-Code-specific nuance that on some models 1M
    tokens is a selectable `[1m]` variant rather than simply the automatic default.
16. [Skeptic FIX] Codex CLI: removed an unsupported "can exfiltrate anything available" quote
    — the cited source never uses the word "exfiltrate" and makes no credential-theft claim;
    kept its actual sandbox-semantics content.
17. [Skeptic FIX] Codex CLI: added that `--full-auto` is documented by OpenAI as deprecated
    (with a compatibility path) — the draft had presented it as a live, unqualified flag.
18. [Skeptic FIX] Codex CLI: rescoped the 272K-token 2x/1.5x pricing surcharge to GPT-5.5
    specifically (where OpenAI's own page attaches it), keeping it clearly distinct from
    Codex CLI's own, separately-sourced 272K effective-context cap.
19. [Skeptic FIX] Codex CLI: downgraded the "OpenAI's own docs confirm resume and its flags"
    claim — OpenAI's docs confirm only that `resume` exists in one line; the flag-level detail
    rests on a single independent technical blog.
20. [Skeptic FIX] Codex CLI: corrected "three independent commentators converge" on compaction
    retention to "two of three," noting the third source (justin3go) describes a materially
    different retention rule (no 20K-token tail; all user messages preserved verbatim).
21. [Skeptic FIX] Codex CLI: re-cited the 1.05M-token/128K-output figures directly to OpenAI's
    own models page rather than leaning only on secondary sources, resolving an internal
    inconsistency with the Foundations section of this same entry.
22. [Skeptic FLAG] Codex CLI: softened "GPT-5.6 Sol as Codex CLI's default recommended model"
    to "recommended" — OpenAI's own wording scopes "default" to the desktop app, not the CLI.
23. [Skeptic FLAG] Codex CLI: removed unlocated specifics ("~80% of a monthly quota," "v0.112,"
    "xhigh-reasoning-effort") absent from the cited GitHub issues/forum thread; kept the two
    figures that are present (the 10-20x token multiplier on a 53x-reread file; a separate
    report of an entire weekly usage cap lost).
24. [Skeptic FLAG] Codex CLI: changed "raisable to 64 KiB" to "documented as an example" —
    OpenAI's docs show that value as an example, not a documented ceiling.
25. [Skeptic FLAG] Codex CLI: tightened the `/compact <instructions>` description to match the
    source's actual claim ("queue follow-up instructions") rather than a stronger
    "threaded into the summarization prompt" framing.
26. [Skeptic FLAG] Codex CLI: noted `max_depth` is not in OpenAI's own subagent docs (which
    instead document `max_concurrent_threads_per_session`) — the depth-multiplier claim comes
    from independent testing only.
27. [Skeptic FIX] Gemini CLI: fixed the `/memory add` citation (the originally-cited page
    doesn't document `add`) and corrected "appended to the global or project GEMINI.md" — it
    appends only to the global `~/.gemini/GEMINI.md`.
28. [Skeptic FIX] Gemini CLI: removed a fabricated hedge-quote about `/clear`'s public
    documentation not found on the cited page; kept only the PR-confirmed behavior.
29. [Skeptic FIX] Gemini CLI: corrected Context Compression Service tier names from
    "full/snippet/summary/excluded" to the PR's actual "FULL/PARTIAL/SUMMARY/EXCLUDED."
30. [Skeptic FIX] Gemini CLI: relabeled the thinking-token cost practice from
    "independently-corroborated" to "thin" — both headline figures come from one publisher
    only; the second cited source doesn't contain them.
31. [Skeptic FIX] Gemini CLI: independence audit — relabeled "Keep GEMINI.md lean" from
    "independently-corroborated" to "vendor-documented" (all cited sources are
    Google-affiliated).
32. [Skeptic FLAG] Gemini CLI: dropped "via a summarization sub-agent" (not in the cited PR)
    from the Context Compression Service description.
33. [Skeptic FLAG] Gemini CLI: dropped the unsupported "no advance in-CLI warning" clause from
    the Antigravity transition scope note (only "no grace period" is documented).
34. [Skeptic FLAG] Gemini CLI: aligned the scope-note wording with Google's actual phrase
    ("free and paid consumer tiers," not "free/individual-tier").
35. [Skeptic FLAG] Gemini CLI: named the publisher behind yet-another-changelog.ai ("Vibe
    Coding Academy") since it's a load-bearing non-Google source.
36. [Timekeeper FIX] Added Claude Fable 5 / Mythos 5 (GA 9 Jun 2026, 1M-token window,
    selectable via `--model claude-fable-5`) to the Anthropic model landscape in both the
    Foundations and Claude Code sections — the original draft's "Sonnet 5 and Opus 5" framing
    omitted the current top tier.
37. [Timekeeper FIX] Resolved the "held pending" Gemini 3 context-window gap using a
    live-fetched official page: gemini-3.1-pro-preview and gemini-3-flash-preview both 1M
    input/64K output, gemini-3.1-flash-lite the same 1M/64K.
38. [Beginner FIX] Added a one-line note near the top of each tool-specific section stating
    that slash/at-commands are typed inside the running interactive session, not at the
    Ubuntu bash prompt — a recurring ambiguity flagged across all three tool drafts.
39. [Beginner FIX] Claude Code: gave `/autocompact` a concrete example value and explained the
    tradeoff of setting it too high vs. too low.
40. [Beginner FIX] Claude Code: added an example "Compact instructions" CLAUDE.md snippet
    instead of naming the feature with nothing to copy.
41. [Beginner FIX] Claude Code: gave the hook/plugin mitigation for large tool output one
    concrete example (a `PostToolUse` hook piping output through `grep`) instead of naming
    mechanisms with zero setup detail.
42. [Beginner FIX] Claude Code: added a one-line `export VAR=value` explanation next to the
    subagent-limit environment variables.
43. [Beginner FIX] Codex CLI: gave the "re-read spiral" mitigation a literal recovery action
    (Ctrl+C to interrupt, then start fresh or fork from a pre-spiral checkpoint) instead of
    the vague "stop and start fresh."
44. [Beginner FIX] Gemini CLI: added a one-line explanation of `temperature` as a randomness
    setting in the custom-subagent frontmatter fields.
45. [Beginner FLAG] Expanded first-use jargon across all four sections: RAG, TTL, MCP,
    "skill," YAML frontmatter, JSONL, cron/CI-CD.
46. Two of four original "held pending" items resolved (Claude Fable 5/Mythos 5, Gemini 3
    context windows, both above); remaining unresolved gaps retained below with updated
    framing; the emerging (but only search-surfaced, not directly fetched) Antigravity
    auto-compaction-trigger figure and Antigravity's reported default model are explicitly
    **not** asserted as fact per this corpus's fetch-don't-recall sourcing rule.

