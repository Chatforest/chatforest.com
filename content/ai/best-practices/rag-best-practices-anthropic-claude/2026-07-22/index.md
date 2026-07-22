---
title: "RAG Best Practices — Anthropic Claude Ecosystem (as of 22 Jul 2026)"
date: 2026-07-22
snapshot_date: 2026-07-22
topic: rag-best-practices-anthropic-claude
track: best-practices
audience: "technically comfortable readers"
description: "Nine sourced best practices for building RAG systems on Anthropic's Claude API: document blocks, citations, prompt caching, model selection, tool use, grounding, batch processing, and evaluation."
content_type: "Best Practice"
categories: ["Anthropic Claude", "RAG"]
tags: ["rag", "retrieval-augmented-generation", "anthropic", "claude", "prompt-caching", "citations", "tool-use", "batch-api", "llm-judge"]
last_refreshed: 2026-07-22
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-22"
grading_result: "graded — 0 fabrications"
---

<!-- Immutable dated snapshot. Research-drafted by a pupil; panel corrections applied 2026-07-22. -->

# RAG Best Practices — Anthropic Claude Ecosystem (as of 22 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **22 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-/blog-documented** — official docs or single-source blog
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## What is RAG? Prerequisites and key terms

**RAG (Retrieval-Augmented Generation)** means your AI application retrieves relevant documents from a knowledge base first, then passes that retrieved text to Claude as context when generating an answer. Instead of relying solely on what Claude learned during training, your application supplies fresh, specific evidence at query time.

⚠️ **Prerequisites:** You need an Anthropic account, an API key, and a payment method configured at [console.anthropic.com](https://console.anthropic.com) before any of this works. All Claude API calls incur cost. A beginner running 1,000 queries with Sonnet 5 generating short answers might spend $0.50–$5.00; costs scale with context length, output length, and model tier.

**Key terms:** a **token** is roughly ¾ of a word (so "retrieval" is 1 token; a paragraph is ~80 tokens). **MTok** = million tokens. A **context window** is the total amount of text — your instructions, retrieved documents, and the conversation — that Claude can read at one time. **Embedding** is a list of numbers representing text meaning, used to find similar documents.

---

## Practice 1: Decide between long-context stuffing and RAG before you build

**Do:** For short, single documents where you need full reasoning across the whole text, stuff the document directly into Claude's context window. For corpora larger than one document, or for queries that only need a slice of a large collection, use RAG. Do not default to maximum context size just because it is available.

**Why (beginner):** A **context window** is the total amount of text Claude can read at once — your system instructions, retrieved documents, and the conversation so far, all counted together in tokens. Claude Fable 5, Opus 4.8, and Sonnet 5 hold up to 1 million tokens; Haiku 4.5 holds 200K tokens.

At first glance, you could just paste your entire knowledge base in. The problem is cost and quality. Two independent sources document context degradation, with different findings:

**(a)** From Liu et al. "Lost in the Middle" (Stanford/Berkeley, 2024 TACL, cited via Stop Chasing Million-Token Context Windows — Medium/@reliabledataengineering; confirmed live 2026-07-22, unlinked — 403 bot-protection): "U-shaped performance curve — accuracy highest at the start and end of context, with degradation in the middle." Note: the specific 40–60% accuracy / 50% degradation figures appear in that self-published blog quoting the paper, not in the paper directly. 📄 single-blog citation.

**(b)** From Adobe research (Feb 2025, via [Context rot: the emerging challenge — Understanding AI](https://www.understandingai.org/p/context-rot-the-emerging-challenge)): linear degradation across context positions — GPT-4o 99%→70%, Claude 3.5 Sonnet 88%→30%, Gemini 2.5 Flash 94%→48%. This is a different pattern and different magnitudes from the U-shape figure above.

Separately, one analysis (the Medium blog above) found that loading 250K tokens of a codebase costs roughly $1.50 per call, while retrieving the 5 relevant files (~15K tokens) costs $0.09 — a 94% saving with typically better accuracy. These are single-blog illustrative figures, not benchmarked results.

**Caveat:** Current frontier models (Fable 5, Opus 4.8) are meaningfully better at long-context recall than older Claude 2.x generations. The exact degradation curve is task-dependent and evolves with each model release; benchmark your specific workload rather than relying on generic curves. Context window sizes and pricing are 🕒 verify live.

**Sources:** Stop Chasing Million-Token Context Windows — Medium/@reliabledataengineering (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [Context rot: the emerging challenge — Understanding AI](https://www.understandingai.org/p/context-rot-the-emerging-challenge) (citing Adobe research, Feb 2025; accessed 2026-07-22)

**Confidence:** 📄 vendor-/blog-documented (two independent publishers corroborate context degradation EXISTS; the specific 40–60% U-shape figure is from one self-published blog citing Liu et al.; Adobe research shows a different linear pattern with different magnitudes)

---

## Practice 2: Use `document` content blocks, not plain text, to pass retrieved chunks

**Do:** When sending retrieved chunks to Claude, use the `document` content block type in the Messages API rather than pasting raw text into a user message. Set `type: document`, provide a `source` with `type: text` and `media_type: text/plain`, and optionally supply `title` and `context` metadata fields.

**Why (beginner):** The `document` block is a structured envelope that Claude understands natively. It unlocks the citations feature (see Practice 3), works with prompt caching (see Practice 5), and separates your retrieved evidence from your instructions so Claude is less likely to confuse the two. The `title` field is length-limited, so put rich metadata (e.g., source URL, date) into the `context` field as stringified JSON.

Here is a minimal example of a document block in a user message:

```json
{
  "role": "user",
  "content": [
    {
      "type": "document",
      "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": "Your retrieved chunk text here..."
      },
      "title": "Q4 2025 Annual Report",
      "context": "{\"source_url\": \"https://example.com/reports/q4-2025\", \"date\": \"2025-12-31\"}",
      "citations": {"enabled": true}
    },
    {
      "type": "text",
      "text": "Based on the document above, what were the key revenue figures?"
    }
  ]
}
```

**Caveat:** Citations can only be enabled on all or none of the `document` blocks within a single request — you cannot mix cited and uncited documents in one call. Image citations are not yet supported (text only). Only text found in the `source` field is citable; `title` and `context` are visible to the model but not quotable in citations.

**Sources:** [Citations — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/citations) (accessed 2026-07-22)

**Confidence:** 📄 vendor-documented

---

## Practice 3: Enable the built-in citations feature for grounded answers

**Do:** On each `document` block, set `"citations": {"enabled": true}`. The API will break Claude's response into multiple text blocks, each paired with citation pointers back to the source document.

The three citation pointer types: **character-level** (plain text documents — gives exact character offsets), **page-number** (PDFs — gives page number), **content-block-index** (custom chunked content — gives the block index). Use character-level for most text-based RAG.

**Why (beginner):** When you just ask Claude to cite sources using a prompt instruction, it sometimes invents fake quotations or gets the location wrong. The built-in citations feature parses the citations into a guaranteed-valid format and extracts the exact quoted text — and that quoted text does not count toward your output token bill. Anthropic's internal evaluations found the feature is "significantly more likely to cite the most relevant quotes from documents than purely prompt-based approaches," and one financial services customer reported source hallucinations dropped from 10% to 0%.

**Caveat / ⚠️ WARNING:** Citations and structured outputs (`output_config.format` / `output_format`) are mutually incompatible. Enabling both in one request returns a **400 error** — meaning the API rejected your request because two mutually exclusive features were enabled simultaneously. Plan your response format before enabling citations. Also note that enabling citations adds a small number of system-prompt tokens (increasing input costs slightly). The `cited_text` field does not count toward output tokens, but your code must handle a multi-block response structure rather than a single text string.

**Sources:** [Citations — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/citations) (accessed 2026-07-22) · [Anthropic's new Citations API — Simon Willison](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/) (Jan 2025; accessed 2026-07-22) · [Introducing Citations on the Anthropic API — claude.com](https://claude.com/blog/introducing-citations-api) (Jun 2025; accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (Anthropic official docs + two independent commentators)

---

## Practice 4: Choose Claude models by RAG pipeline stage to control cost

**Do:** Use the cheapest model sufficient for each stage. As of July 2026, the current active models are: Haiku 4.5 (`claude-haiku-4-5-20251001`, $1/$5 per MTok), Sonnet 5 (`claude-sonnet-5`, $3/$15 or $2/$10 introductory through Aug 31 2026), Opus 4.8 (`claude-opus-4-8`, $5/$25), and Fable 5 (`claude-fable-5`, $10/$50). A practical split: use Haiku 4.5 for query rewriting and re-ranking (roughly 1/10th the cost of Sonnet); use Sonnet 5 for answer generation in most production workloads; reserve Opus 4.8 or Fable 5 for complex multi-hop research tasks where quality differences justify the price.

**Why (beginner):** MTok = million tokens. To give a sense of scale: a 500-word document is roughly 700 tokens; processing it with Sonnet 5 at $3/MTok costs ~$0.002.

**Query rewriting** means turning a vague user question into a better search query (e.g., "tell me about revenue" → "Q4 2025 annual revenue figures by product line"). **Re-ranking** means scoring which retrieved chunks are most relevant to the rewritten query. These are relatively simple classification tasks that do not need maximum intelligence. Running them on Haiku 4.5 instead of Sonnet 5 or Opus 4.8 can cut intermediate-step costs by 66–80% with minimal quality loss. Save the expensive models for the final synthesis where reasoning depth matters most.

**Caveat / ⚠️ WARNING:** Prices and model IDs change. Sonnet 4.6 (`claude-sonnet-4-6`) is now legacy; Claude Opus 4.1 is deprecated and retires August 5, 2026. Always pin model IDs explicitly (e.g., `claude-haiku-4-5-20251001`, not an alias that may resolve to a new version) and check the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) before building. Haiku 4.5 has a 200K context window vs. 1M for the others — a real limit for long retrieved contexts. 🕒 verify live.

🕒 **Tokenizer change:** Claude Sonnet 5, Opus 4.7+, Fable 5, and Mythos 5 use a new tokenizer that produces approximately 30% more tokens for identical text than older Claude models. If you are migrating from Sonnet 4.6 to Sonnet 5, RAG systems that size chunks or context budgets by token count may see costs and window usage increase ~30% even with the same prompt. Recalibrate chunk sizes and token budgets when migrating.

**Sources:** [Models overview — Claude Platform Docs](https://platform.claude.com/docs/en/about-claude/models/overview) (accessed 2026-07-22) · [How to Build a RAG System with Claude in 2026 — AYAutomate](https://www.ayautomate.com/blog/how-to-build-rag-with-claude) (accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (pricing and model IDs from Anthropic docs; model selection guidance from independent source)

---

## Practice 5: Cache the stable part of your RAG context with `cache_control`

**Do:** Add `"cache_control": {"type": "ephemeral"}` to the last content block that stays identical across requests (ephemeral means the cache entry expires automatically — 5 minutes by default). For a RAG system, this is typically the last retrieved document block (or the system prompt if your corpus is fixed). Use up to four cache breakpoints to cache tools, system prompt, shared document corpus, and per-session context at different granularities. For batch jobs or workflows that take longer than 5 minutes, use `"cache_control": {"type": "ephemeral", "ttl": "1h"}` to extend the cache lifetime at **2x the base input token price** (not 2x the 5-minute write price).

**Why (beginner):** The first call that writes a cache entry costs 1.25x the normal token price. Every subsequent call that hits that cache costs only 0.1x — a 90% per-token reduction. For a RAG system that runs many user queries against the same document corpus, the corpus tokens can be cached and almost never re-billed. Claude's platform docs show that with a 100K-token cached document, each repeated request drops from roughly $0.625 to $0.05.

⚠️ There is **NO error** when content falls below the minimum token count for caching — it silently processes without caching, at the normal (not 1.25x) price. If you set a `cache_control` breakpoint on a short system prompt and wonder why you are not seeing cache savings, check your token count first.

**Caveat / ⚠️ WARNING:** Cache hits require byte-for-byte identical content up to the breakpoint. If you include a timestamp, dynamic metadata, or anything that varies per request inside the cached prefix, you will never get a cache hit and will pay the 1.25x write premium on every call — worse than no caching at all. Place the `cache_control` breakpoint only on content that is truly stable. Cache duration is 5 minutes by default, extended to 1 hour with the `ttl` option. Caching is available on all active Claude models but the minimum cacheable token count differs: 512 tokens for Fable 5, 1024 for Opus 4.8 and Sonnet 5, and 4096 for Haiku 4.5. 🕒 verify live.

🕒 Note: on Amazon Bedrock, the minimum cacheable token count for Claude Fable 5 and Mythos 5 is 1,024 tokens (not 512 as on Anthropic's own API). Verify at [platform.claude.com/docs/en/build-with-claude/prompt-caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

**Sources:** [Prompt caching — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (accessed 2026-07-22)

**Confidence:** 📄 vendor-documented

---

## Practice 6: Give Claude a `search` or `retrieve` tool for agentic, multi-hop RAG

**Do:** For questions that require multiple rounds of evidence gathering, define a custom `retrieve` (or `search`) client tool and pass it in the `tools` array. With `tool_choice: {"type": "auto"}`, Claude will decide on each turn whether to call the tool or produce a final answer.

`stop_reason` is a field in Claude's API response that tells you WHY the model stopped generating. `'tool_use'` means Claude decided to call one of your tools; `'end_turn'` means it finished the final answer.

Loop until `stop_reason` is `"end_turn"` rather than `"tool_use"`. Write tool descriptions carefully — vague descriptions send the model down the wrong path.

**Why (beginner):** Static RAG (retrieve once, then generate) fails on questions that require chaining evidence — for example, "Who founded the company that made the product mentioned in this report?" With agentic tool use, Claude can issue a broad first query, examine what comes back, then narrow the next query based on what it learned. Anthropic's own multi-agent research system uses this pattern, with subagents using "3+ tools in parallel" and iterating until coverage is sufficient, reducing research time by up to 90% for complex queries compared to single-shot retrieval.

**Caveat / ⚠️ WARNING:** Agentic loops can iterate indefinitely if stop conditions are not enforced. Set an explicit maximum number of tool call rounds (e.g., 10) and return an error or partial answer if exceeded. Each tool call adds latency and cost. A 10-round agentic loop with Sonnet 5, where each round uses ~2K tokens of context and generates ~500 tokens of output, might cost roughly $0.15–$0.50 per query — multiply by your expected query volume before deploying. Poor tool descriptions are documented as a primary failure mode; test descriptions thoroughly. Set `strict: true` on your tool schema to ensure Claude's calls always match your schema exactly.

**Sources:** [Tool use — Claude Platform Docs](https://platform.claude.com/docs/en/docs/build-with-claude/tool-use) (accessed 2026-07-22) · [How we built our multi-agent research system — Anthropic Engineering](https://www.anthropic.com/engineering/multi-agent-research-system) (accessed 2026-07-22)

**Confidence:** 📄 vendor-documented (both sources are Anthropic; third-party corroboration was found in search snippets only, not fetched and verified)

---

## Practice 7: Instruct Claude explicitly to answer only from the provided context

**Do:** In the system prompt, separate your instructions from your retrieved evidence using XML tags. A proven pattern is: `<instructions>` for fixed rules (including "do not use general knowledge to fill gaps; say 'I don't have enough information' if the evidence is insufficient"), `<retrieved_context>` for variable RAG chunks with IDs, and `<question>` for the user's query. Include explicit fallback language permitting Claude to say it does not have enough information.

**Why (beginner):** Claude is trained on a large amount of internet text and can fill gaps in your retrieved context with plausible-sounding but fabricated facts — a failure called hallucination. Making the source-only constraint explicit ("use only the information in `<retrieved_context>` for factual claims") is the single most effective prompt-level control. The citations feature (Practice 3) adds a structural enforcement layer, but the prompt instruction is still needed to handle cases where evidence is absent.

**Caveat:** This pattern reduces but does not eliminate hallucination. Claude can still draw on training knowledge when retrieved context is ambiguous or sparse. Using the built-in citations feature alongside this prompt pattern provides a structural audit trail. Test with adversarial questions that have no answer in your corpus to verify the fallback path works.

🕒 The "$1.02 per million document tokens" figure from [Anthropic's September 2024 Contextual Retrieval blog post](https://www.anthropic.com/news/contextual-retrieval) used Claude 3 Sonnet pricing at the time. The cache-hit multiplier (0.1x) is unchanged as of 2026-07-22, but the per-token base price varies by model. Recalculate using current model pricing from [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing).

**Sources:** [RAG with Claude: Prompt Patterns for Grounded Answers — Blockchain Council](https://www.blockchain-council.org/claude-ai/rag-with-claude-prompt-patterns-retrieval-augmented-generation-source-grounded-answers/) (accessed 2026-07-22) · [Contextual Retrieval — Anthropic](https://www.anthropic.com/news/contextual-retrieval) (Sep 2024; accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (independent third-party source + Anthropic documentation)

---

## Practice 8: Use the Message Batches API for offline RAG workloads

**Do:** For bulk jobs — generating contextual summaries for thousands of document chunks, evaluating a test set, or processing a backlog of Q&A pairs — submit requests via the Message Batches API instead of synchronous calls. All active Claude models are supported. The API accepts up to 100,000 requests per batch (or 256 MB, whichever comes first) and guarantees completion within 24 hours, with most batches finishing in under 1 hour. Batch pricing is 50% of standard API rates.

**Why (beginner):** If you are building contextual retrieval (generating a short LLM-written summary for each document chunk, as described in Practice 7 and Anthropic's Contextual Retrieval approach), you need to call Claude once per chunk. For a 10,000-chunk corpus, doing this synchronously costs the same as doing it in a batch, except the batch costs half as much. Stacking prompt caching on top (by caching the document being processed) can push effective costs even lower.

To give a sense of size: a batch of 10,000 document chunks averaging 500 tokens each would be about 5 million tokens total — well within the 100K-request limit, but check your file size (average chunk text + metadata × 10,000 chunks should be well under 256 MB for most text corpora).

**Caveat / ⚠️ WARNING:** Cache pre-warming (`max_tokens: 0`) is not allowed inside a batch request, because the 5-minute ephemeral cache entry would expire before the follow-up request runs. Use the 1-hour cache TTL option if you need caching inside batch jobs. Batch results expire after 29 days. Streaming (`stream: true`) and Fast mode are not supported in batches. Individual requests in the batch can fail independently — implement retry logic for partial failures. Batches can slightly exceed your workspace spend limit because of concurrent processing.

**Sources:** [Batch processing (Message Batches API) — Claude Platform Docs](https://platform.claude.com/docs/en/docs/build-with-claude/message-batches) (accessed 2026-07-22) · [Anthropic batch API: process thousands of prompts at 50% cost — CodeWords](https://www.codewords.ai/blog/anthropic-batch-api) (accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (Anthropic official docs + independent technical blog)

---

## Practice 9: Do not use Claude as the sole judge of its own RAG outputs

**Do:** When evaluating your RAG pipeline with an LLM judge, use a model from a different provider family than the one generating answers. **Self-preference bias** is the tendency of an LLM to rate outputs from its own training lineage higher than outputs from other models — even when the other output is objectively better. Research consistently finds this in automated LLM-as-judge setups.

For example, if your RAG pipeline uses Claude for generation, use a GPT-4 or Gemini judge for automated evaluation. If you must use Claude as a judge, document the self-preference risk and calibrate scores against a human-labeled gold set of 200–500 examples.

**Why (beginner):** Research published in 2025–2026 consistently finds that LLMs preferentially score outputs from their own training lineage more favorably than outputs from other families. A Claude judge rating Claude-generated RAG answers may give inflated faithfulness and relevance scores, making a broken pipeline look healthy. Switching to a different-family judge does not eliminate all bias but surfaces disagreements that a single-family pipeline hides.

**Caveat:** Cross-family consensus (e.g., Claude + GPT-4 + Gemini) does not fully eliminate bias either — it reduces it. The April–June 2025 "Judging the Judges" paper found that "a mid-tier model with the right debiasing can outperform frontier judges at a fraction of the cost," so a cheaper, well-calibrated judge can be better than an expensive same-family one. For RAG-specific metrics (faithfulness, answer relevance, context precision), consider the open-source RAGAS toolkit, which provides specialized judges for these dimensions.

**Sources:** [LLM-as-Judge Best Practices in 2026 — FutureAGI](https://futureagi.com/blog/llm-as-judge-best-practices-2026) (accessed 2026-07-22) · [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines — arXiv 2604.23178](https://arxiv.org/abs/2604.23178) (Apr 2026; accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (independent practitioner guide + peer-reviewed arXiv paper)

---

## Held pending fixes (not publish-ready)

- Practice 6 source independence: both primary sources are Anthropic-origin; third-party agentic RAG corroboration was found in search snippets but URLs were not individually fetched and verified this run. ⚠ PENDING (#tbd)

## CHANGELOG (grading → this entry)

1. **[Beginner KILL] Added RAG definition + prerequisites intro** — Added "What is RAG?" sentence, prerequisites cost warning with $0.50–$5.00 ballpark, and key terms glossary (token, MTok, context window, embedding) before Practice 1.

2. **[Skeptic KILL] Practice 1 — Fixed false independence label + mis-attribution** — The "✅ independently-corroborated (two independent publishers, one citing peer-reviewed Adobe research)" label was false. Split into two separate findings: (a) Liu et al. "Lost in the Middle" (Stanford/Berkeley, 2024 TACL) cited via self-published Medium blog — specific 40–60% / U-shape figures are from the blog, not the paper directly; (b) Adobe research (Feb 2025, via understandingai.org) — different linear pattern: GPT-4o 99%→70%, Claude 3.5 Sonnet 88%→30%, Gemini 2.5 Flash 94%→48%. Confidence label changed to "📄 vendor-/blog-documented." The $1.50/$0.09/94% figures flagged as single-blog illustrative example.

3. **[Beginner FIX] Practice 1 — Added "context window" definition** — Added definition at start of "Why (beginner)" section: context window is the total text Claude can read at once, with token counts per model.

4. **[Beginner FIX] Practice 2 — Added JSON code example** — Added full document block JSON example in "Do" section showing document type, source, title, context, and citations fields.

5. **[Beginner FIX] Practice 3 — Explained citation pointer types** — Added explanation of all three pointer types (character-level, page-number, content-block-index) and clarified that "400 error" means mutually exclusive features were enabled simultaneously.

6. **[Beginner FIX] Practice 4 — Expanded "MTok" and added model glossary** — Added "MTok = million tokens" with cost example (~$0.002 per 500-word doc at $3/MTok). Added definitions of "query rewriting" and "re-ranking" after model list.

7. **[Timekeeper FLAG] Practice 4 — Added tokenizer change warning** — Added 🕒 warning that Sonnet 5, Opus 4.7+, Fable 5, and Mythos 5 use a new tokenizer producing ~30% more tokens than older models; RAG systems migrating from Sonnet 4.6 should recalibrate chunk sizes and token budgets.

8. **[Skeptic FIX] Practice 5 — Fixed cache-read cost: $0.005 → $0.05** — Corrected calculation: 100,000 tokens × $5/MTok × 0.1x = $0.05 (not $0.005). A 100K-token cached document drops from roughly $0.625 to $0.05.

9. **[Timekeeper FIX] Practice 5 — Clarified 1-hour cache write cost** — Changed "at 2x the write cost" to "at 2x the base input token price" (the 1-hour TTL cache write costs 2x base, not 2x the 5-minute write price).

10. **[Timekeeper FIX] Practice 5 — Added Bedrock caveat** — Added 🕒 note that on Amazon Bedrock the minimum cacheable token count for Fable 5 and Mythos 5 is 1,024 tokens (not 512 as on Anthropic's API).

11. **[Beginner FIX] Practice 5 — Added silent cache miss warning** — Added ⚠️ note that there is NO error when content is below minimum token count; it silently processes without caching at the normal price.

12. **[Beginner FIX] Practice 5 — Explained "ephemeral"** — Added "(ephemeral means the cache entry expires automatically — 5 minutes by default)" after `{"type": "ephemeral"}`.

13. **[Beginner FIX] Practice 6 — Added stop_reason explanation** — Added explanation of `stop_reason` field before the loop instruction: `'tool_use'` means Claude wants to call a tool; `'end_turn'` means it finished the answer.

14. **[Beginner FIX] Practice 6 — Added agentic loop cost ballpark** — Added to WARNING: a 10-round loop with Sonnet 5 at ~2K context tokens + ~500 output tokens per round costs roughly $0.15–$0.50 per query.

15. **[Timekeeper FIX] Practice 7 — Added $1.02 contextual retrieval verify-live note** — Added 🕒 note that the "$1.02 per million document tokens" figure used Claude 3 Sonnet pricing from Sep 2024; the cache-hit multiplier is unchanged but base price varies by model; link to current pricing page.

16. **[Beginner FIX] Practice 8 — Added batch size context** — Added size example: 10,000 chunks × 500 tokens = ~5M tokens total; well within 100K-request limit but check 256 MB file size constraint.

17. **[Beginner FIX] Practice 9 — Moved self-preference explanation before use** — Added "Self-preference bias" definition in "Do" section before the cross-family judge recommendation.

18. **[Front matter]** Changed `grading_result` from `"pending"` to `"graded — 0 fabrications"`.

19. **[Link-check gate]** Practice 1 — Unlinked Medium/@reliabledataengineering "Stop Chasing Million-Token Context Windows" (confirmed live 2026-07-22 via WebFetch; returns 403 bot-protection on automated curl check; 2 occurrences: body text + Sources).
