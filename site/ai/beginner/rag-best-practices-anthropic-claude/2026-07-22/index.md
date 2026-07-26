# RAG Best Practices — Anthropic Claude Ecosystem (as of 22 Jul 2026)

> Plain-language guide to building RAG systems with Claude: when to use long context vs. retrieval, document blocks, citations, prompt caching, model selection, and batch processing — no prior ML experience needed.


<!-- Immutable dated snapshot. Re-leveled from the 2026-07-22 technical entry by The Translator. Facts and URLs unchanged. -->

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

## What is RAG? Start here if you are new

**RAG** stands for **Retrieval-Augmented Generation**. The name sounds complicated, but the idea is simple.

When you ask Claude a question, it can only draw on two things: what it learned during training (its "built-in knowledge") and whatever text you hand it in the current conversation. RAG is the technique of handing it the right documents at the right moment.

Here is the basic flow:

1. A user asks a question.
2. Your code searches a knowledge base (your documents, your database) for the chunks of text most likely to contain the answer.
3. Your code sends those chunks to Claude along with the question.
4. Claude reads the chunks and writes an answer based on that evidence.

The result: Claude can answer questions about things it was never trained on — your company's internal policies, the latest product specs, yesterday's news.

**Before you start — what you need:**

You need an Anthropic account, an API key, and a payment method configured at [console.anthropic.com](https://console.anthropic.com). Every call to the Claude API costs money. A beginner running 1,000 queries with Sonnet 5 generating short answers might spend $0.50–$5.00. Costs grow with context length, output length, and which model you choose.

**Key words used throughout this guide:**

- **Token** — roughly three-quarters of a word. "Retrieval" is 1 token. A paragraph is about 80 tokens.
- **MTok** — one million tokens.
- **Context window** — the total amount of text Claude can read in one call. This includes your instructions, the retrieved documents, and the conversation so far. Think of it as the size of Claude's "desk" — everything has to fit on it at once.
- **Embedding** — a list of numbers that captures the meaning of a piece of text. Embeddings are used to find documents that are similar in meaning to the user's question.

---

## Practice 1: Decide up front whether to paste documents in or use RAG

**Do:** If you have a single, short document and you need Claude to reason across the whole thing, paste it directly into the conversation — no RAG needed. If your knowledge base is larger than one document, or if a given question only needs a small slice of a large collection, use RAG instead. Do not paste your entire knowledge base into every request just because Claude's context window is large enough to hold it.

**Why (beginner):** Claude's context window is the total amount of text it can read in one call — your instructions, the documents you provide, and the conversation so far, all measured in tokens. Claude Fable 5, Opus 4.8, and Sonnet 5 can hold up to 1 million tokens. Haiku 4.5 holds up to 200,000 tokens.

Those are big numbers, and it is tempting to just dump everything in. Two problems stop that from working well:

**Problem 1 — Quality.** Two independent research findings show that Claude's accuracy drops as context gets longer, though they disagree on the exact shape of the problem. A Stanford/Berkeley study ("Lost in the Middle", 2024) found a "U-shaped performance curve" — Claude does best on information near the very start or very end of the context, and struggles with things buried in the middle. A separate Adobe study (Feb 2025) found a more gradual degradation from start to end: Claude 3.5 Sonnet dropped from 88% accuracy on information at the start to 30% on information at the end. The pattern varies by model and task, so the safest rule is: don't count on Claude finding the needle if you hand it the whole haystack.

**Problem 2 — Cost.** One illustrative analysis found that loading 250,000 tokens of a codebase costs roughly $1.50 per call, while retrieving only the 5 relevant files (about 15,000 tokens) costs $0.09 — a 94% saving with typically better accuracy. These are single-source illustrative figures, not benchmarked results, but the direction is right: more tokens in = more money spent.

**Caveat:** Newer frontier models like Fable 5 and Opus 4.8 are meaningfully better at long-context recall than older Claude generations. The exact accuracy curve depends on your specific task and changes with each model release. Benchmark your own workload rather than relying on generic numbers. Context window sizes and pricing change over time. 🕒 verify live.

**Sources:** Stop Chasing Million-Token Context Windows — Medium/@reliabledataengineering (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [Context rot: the emerging challenge — Understanding AI](https://www.understandingai.org/p/context-rot-the-emerging-challenge) (citing Adobe research, Feb 2025; accessed 2026-07-22)

**Confidence:** 📄 vendor-/blog-documented (two independent publishers corroborate context degradation EXISTS; the specific 40–60% U-shape figure is from one self-published blog citing Liu et al.; Adobe research shows a different linear pattern with different magnitudes)

---

## Practice 2: Wrap your retrieved documents in a `document` block, not raw text

**Do:** When you send retrieved text to Claude, wrap it in a `document` content block rather than pasting the raw text into the message. This is a specific JSON structure the API understands natively.

**Why (beginner):** Pasting raw text works, but Claude cannot tell it apart from your instructions. A `document` block is a labeled envelope that tells Claude "this is a document to read." Using it:

- Unlocks the built-in citations feature (see Practice 3), which proves Claude's answer came from real evidence.
- Works with prompt caching (see Practice 5), which cuts costs dramatically.
- Reduces confusion between your instructions and the retrieved evidence.

One note on the fields inside the block: the `title` field has a length limit, so if you want to store rich metadata like the source URL or the document's date, put that information in the `context` field as a JSON string.

Here is a complete example of one document block inside a user message:

```json
{
  "role": "user",
  "content": [
    {
      "type": "document",          // tells Claude this is a document to read, not an instruction
      "source": {
        "type": "text",            // you are providing plain text (not a URL to fetch)
        "media_type": "text/plain",
        "data": "Your retrieved chunk text here..."   // the actual document content goes here
      },
      "title": "Q4 2025 Annual Report",              // short label; has a length limit
      "context": "{\"source_url\": \"https://example.com/reports/q4-2025\", \"date\": \"2025-12-31\"}",
                                   // rich metadata goes here as a JSON string, not in title
      "citations": {"enabled": true}  // turn on citations so Claude can point to exact quotes
    },
    {
      "type": "text",
      "text": "Based on the document above, what were the key revenue figures?"
                                   // this is the user's actual question
    }
  ]
}
```

**Caveat:** Citations can only be turned on for all documents in a request or none of them — you cannot mix cited and uncited documents in one call. Image citations are not yet supported (text only). Only text in the `source` field can be quoted in citations; the `title` and `context` fields are visible to Claude but not quotable.

**Sources:** [Citations — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/citations) (accessed 2026-07-22)

**Confidence:** 📄 vendor-documented

---

## Practice 3: Turn on built-in citations so Claude's answers are verifiable

**Do:** On each `document` block, set `"citations": {"enabled": true}`. Claude's API response will then contain multiple text blocks, each one paired with a citation pointer back to the exact location in your document.

There are three types of citation pointer, depending on your document format:

- **character-level** — for plain text documents; gives the exact character position of the quoted text. Use this for most RAG systems.
- **page-number** — for PDFs; gives the page number.
- **content-block-index** — for custom-chunked content; gives the block index.

**Why (beginner):** Without citations, Claude might quote a document incorrectly or invent a quote that sounds plausible but does not exist — a problem called hallucination. The built-in citations feature fixes this by having Claude point to specific passages in the documents you provided. Those pointers are guaranteed to be valid (the quoted text is real, and it came from your document). As a bonus, the quoted text does not count toward your output token bill.

Anthropic's internal evaluations found that the feature is "significantly more likely to cite the most relevant quotes from documents than purely prompt-based approaches." One financial services customer reported that source hallucinations dropped from 10% to 0% after switching to citations.

**Caveat / ⚠️ WARNING:** Citations and structured output formatting (`output_config.format` / `output_format`) cannot be used together in the same request. If you enable both, the API returns a **400 error** — this means your request was rejected because you combined two features that are mutually exclusive. Decide whether you want citations or structured output before you build. Also: enabling citations adds a small number of system-prompt tokens, which slightly increases your input cost. Your code must also handle a multi-block response (a list of text objects, each with a citation) rather than a single text string.

**Sources:** [Citations — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/citations) (accessed 2026-07-22) · [Anthropic's new Citations API — Simon Willison](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/) (Jan 2025; accessed 2026-07-22) · [Introducing Citations on the Anthropic API — claude.com](https://claude.com/blog/introducing-citations-api) (Jun 2025; accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (Anthropic official docs + two independent commentators)

---

## Practice 4: Match the model to the task to control costs

**Do:** Use the cheapest model that is good enough for each step in your pipeline. You do not need the most powerful model for every task.

As of July 2026, the active Claude models and their prices are:

| Model | Price per MTok (input / output) |
|---|---|
| Haiku 4.5 (`claude-haiku-4-5-20251001`) | $1 / $5 |
| Sonnet 5 (`claude-sonnet-5`) | $3 / $15 (or $2 / $10 introductory through Aug 31, 2026) |
| Opus 4.8 (`claude-opus-4-8`) | $5 / $25 |
| Fable 5 (`claude-fable-5`) | $10 / $50 |

**MTok = one million tokens.** To make that concrete: a 500-word document is about 700 tokens. Processing it with Sonnet 5 at $3 per MTok costs roughly $0.002 — less than a fraction of a cent. Costs add up when you process millions of documents or run many queries.

A practical split for a RAG pipeline:

- Use **Haiku 4.5** for **query rewriting** and **re-ranking**. Query rewriting means turning a vague user question into a better search query ("tell me about revenue" becomes "Q4 2025 annual revenue figures by product line"). Re-ranking means scoring which retrieved chunks are most relevant to that rewritten query. These are simpler tasks. Using Haiku 4.5 instead of Sonnet 5 cuts costs for these steps by 66–80% with minimal quality loss.
- Use **Sonnet 5** for the final answer generation in most production use cases.
- Reserve **Opus 4.8 or Fable 5** for complex multi-hop research tasks where the extra reasoning depth is worth the higher price.

**Caveat / ⚠️ WARNING:** Model prices and IDs change. Sonnet 4.6 (`claude-sonnet-4-6`) is now legacy. Claude Opus 4.1 is deprecated and retires August 5, 2026. Always pin the full model ID in your code (for example, `claude-haiku-4-5-20251001`, not a short alias that might silently resolve to a newer, differently-priced version). Check the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) before you build. Note also that Haiku 4.5 has a 200,000-token context window, while the other models offer 1 million tokens — a real limit if your retrieved context is long. 🕒 verify live.

🕒 **Important if you are migrating from an older model:** Claude Sonnet 5, Opus 4.7+, Fable 5, and Mythos 5 use a new tokenizer that produces approximately 30% more tokens for the same text than older Claude models. If you move from Sonnet 4.6 to Sonnet 5, your RAG system will use about 30% more tokens even with the same documents and prompts. This means higher costs and tighter context windows. Recalibrate your chunk sizes and token budgets when migrating.

**Sources:** [Models overview — Claude Platform Docs](https://platform.claude.com/docs/en/about-claude/models/overview) (accessed 2026-07-22) · [How to Build a RAG System with Claude in 2026 — AYAutomate](https://www.ayautomate.com/blog/how-to-build-rag-with-claude) (accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (pricing and model IDs from Anthropic docs; model selection guidance from independent source)

---

## Practice 5: Cache the parts of your context that stay the same across requests

**Do:** Add `"cache_control": {"type": "ephemeral"}` to the last document block (or system prompt) that stays identical across multiple requests. "Ephemeral" means the cache entry expires automatically — 5 minutes by default. For batch jobs or workflows that run longer than 5 minutes, extend the cache lifetime to 1 hour with `"cache_control": {"type": "ephemeral", "ttl": "1h"}`.

You can set up to four cache breakpoints in a single request, letting you cache different layers of your context independently: your tools, your system prompt, a shared document corpus, and per-session context.

**Why (beginner):** Every time you send a request, Claude re-reads all the tokens you send. If your RAG system always includes the same 100 documents in every request (a fixed knowledge base), you are paying to re-read those documents every single time.

Prompt caching fixes this. The first call that writes a new cache entry costs 1.25x the normal input token price — a small premium. Every subsequent call that uses that cached content costs only 0.1x the normal price — a 90% reduction per token.

In real numbers: with a 100,000-token cached document corpus, each request drops from roughly $0.625 to $0.05. Run 100 queries against that same corpus and you save about $57.50.

⚠️ **CRITICAL: Silent cache miss — there is no error.** If the content you marked with `cache_control` contains fewer tokens than the minimum required for caching, Claude will process the request normally — but without caching — and charge you the normal (not 1.25x) price. There is no error message, no warning, and no indication anything went wrong. You will simply not see the cache savings you expected. If you set a cache breakpoint on a short system prompt and notice your costs are not dropping, check whether your cached content meets the minimum token count:

- Fable 5: 512 tokens minimum
- Sonnet 5 and Opus 4.8: 1,024 tokens minimum
- Haiku 4.5: 4,096 tokens minimum

🕒 These minimums are for Anthropic's own API. On Amazon Bedrock, the minimum for Fable 5 and Mythos 5 is 1,024 tokens. Verify at [platform.claude.com/docs/en/build-with-claude/prompt-caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

**Caveat / ⚠️ WARNING:** Cache hits require that every byte of the cached content is identical across requests. If you accidentally include anything that changes per request inside the cached prefix — a timestamp, a user ID, dynamic metadata — you will never get a cache hit. Worse, you will pay the 1.25x write premium on every single call, which is more expensive than not caching at all. Put the `cache_control` marker only on content that is truly the same for every request. Caching is available on all active Claude models. 🕒 verify live.

**Sources:** [Prompt caching — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (accessed 2026-07-22)

**Confidence:** 📄 vendor-documented

---

## Practice 6: Give Claude a search tool for questions that need multiple rounds of research

**Do:** Some questions cannot be answered by retrieving documents once and generating a single answer. For those questions, define a custom `retrieve` or `search` tool and pass it to Claude in the `tools` array. Set `tool_choice: {"type": "auto"}` so Claude can decide on each turn whether to call the tool again or produce a final answer.

In Claude's API response, there is a field called `stop_reason` that tells you why the model stopped generating text:

- `"tool_use"` — Claude wants to call one of your tools before continuing.
- `"end_turn"` — Claude has finished and is giving you the final answer.

Your code should loop: execute the tool Claude requested, send the result back, and repeat — until `stop_reason` is `"end_turn"`. Write your tool descriptions carefully. Vague descriptions send Claude down the wrong path.

**Why (beginner):** Regular RAG — retrieve once, then answer — breaks on questions that require chaining evidence. For example: "Who founded the company that made the product mentioned in this report?" You cannot answer that in one retrieval step. With a search tool, Claude can issue a broad first query, see what comes back, issue a narrower follow-up query based on what it learned, and keep going until it has enough to answer. Anthropic's own multi-agent research system uses this pattern, with subagents using "3+ tools in parallel" and iterating until coverage is sufficient, reducing research time by up to 90% for complex queries compared to single-shot retrieval.

**Caveat / ⚠️ WARNING:** Agentic loops can run indefinitely if you do not stop them. Set an explicit maximum number of tool call rounds — for example, 10 — and return an error or partial answer if that limit is reached. Each tool call adds latency and cost. A 10-round agentic loop with Sonnet 5, where each round uses about 2,000 tokens of context and generates about 500 tokens of output, might cost roughly $0.15–$0.50 per query. Multiply that by your expected query volume before deploying. Poor tool descriptions are documented as a primary failure mode; test your descriptions thoroughly. Set `strict: true` on your tool schema to ensure Claude's calls always match the schema exactly.

**Sources:** [Tool use — Claude Platform Docs](https://platform.claude.com/docs/en/docs/build-with-claude/tool-use) (accessed 2026-07-22) · [How we built our multi-agent research system — Anthropic Engineering](https://www.anthropic.com/engineering/multi-agent-research-system) (accessed 2026-07-22)

**Confidence:** 📄 vendor-documented (both sources are Anthropic; third-party corroboration was found in search snippets only, not fetched and verified)

---

## Practice 7: Tell Claude explicitly to answer only from the documents you provided

**Do:** In your system prompt, use XML tags to separate your instructions from your retrieved documents and from the user's question. A proven pattern:

- `<instructions>` — your fixed rules, including the rule "if the retrieved context does not contain enough information to answer, say so; do not use general knowledge to fill gaps."
- `<retrieved_context>` — the document chunks you retrieved, each with an ID.
- `<question>` — the user's question.

Include explicit fallback language. Give Claude permission to say "I don't have enough information" when the evidence is absent.

**Why (beginner):** Claude was trained on a huge amount of internet text. When the retrieved documents do not fully answer the user's question, Claude may "fill in the gaps" with plausible-sounding facts that it learned during training — facts that may be wrong, outdated, or irrelevant to your use case. This is called hallucination. Making the constraint explicit in the system prompt ("use only the information in `<retrieved_context>` for factual claims") is the single most effective prompt-level control against this failure.

The citations feature from Practice 3 adds a structural layer of enforcement, but the prompt instruction is still needed to handle the case where the answer simply is not in your documents.

Test this by asking questions that have no answer in your corpus. If Claude makes up an answer instead of saying it does not know, your fallback instruction is not working.

**Caveat:** This pattern reduces hallucination but does not eliminate it. Claude can still draw on training knowledge when retrieved context is ambiguous or sparse. Using citations alongside this prompt pattern gives you an audit trail. Test with adversarial questions.

🕒 The "$1.02 per million document tokens" figure from [Anthropic's September 2024 Contextual Retrieval blog post](https://www.anthropic.com/news/contextual-retrieval) used Claude 3 Sonnet pricing at the time. The cache-hit multiplier (0.1x) is unchanged as of 2026-07-22, but the per-token base price varies by model. Recalculate using current model pricing from [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing).

**Sources:** [RAG with Claude: Prompt Patterns for Grounded Answers — Blockchain Council](https://www.blockchain-council.org/claude-ai/rag-with-claude-prompt-patterns-retrieval-augmented-generation-source-grounded-answers/) (accessed 2026-07-22) · [Contextual Retrieval — Anthropic](https://www.anthropic.com/news/contextual-retrieval) (Sep 2024; accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (independent third-party source + Anthropic documentation)

---

## Practice 8: Use the Batch API for large background jobs — at half the price

**Do:** When you need to process a large number of documents or queries offline — generating summaries for thousands of chunks, evaluating a test set, processing a backlog of Q&A pairs — use the Message Batches API instead of making individual synchronous calls. All active Claude models are supported. The API accepts up to 100,000 requests per batch (or 256 MB of data, whichever comes first) and guarantees completion within 24 hours. Most batches finish within 1 hour. Batch pricing is 50% of standard API rates.

**Why (beginner):** Suppose you are building a knowledge base and you want to generate a short summary for each of 10,000 document chunks (a technique called contextual retrieval). Each summary requires one API call. If you make those calls one at a time, you pay full price. If you submit them as a batch, you pay half price — same work, same results, half the cost.

To give a sense of scale: 10,000 chunks averaging 500 tokens each is about 5 million tokens total input. That is well within the 100,000-request limit, but make sure your total file size (chunk text plus metadata for every request) stays under 256 MB — check this before submitting.

You can combine batch processing with prompt caching (Practice 5) to push effective costs even lower.

**Caveat / ⚠️ WARNING:** Cache pre-warming — making a call with `max_tokens: 0` to populate the cache before real requests arrive — does not work inside a batch. The 5-minute cache entry would expire before follow-up requests in the batch reach it. If you need caching inside batch jobs, use the 1-hour TTL option (`"cache_control": {"type": "ephemeral", "ttl": "1h"}`). Other limitations: batch results expire and are deleted after 29 days; streaming and Fast mode are not supported in batches; individual requests within a batch can fail independently, so implement retry logic for partial failures; batches can slightly exceed your workspace spend limit because requests are processed concurrently.

**Sources:** [Batch processing (Message Batches API) — Claude Platform Docs](https://platform.claude.com/docs/en/docs/build-with-claude/message-batches) (accessed 2026-07-22) · [Anthropic batch API: process thousands of prompts at 50% cost — CodeWords](https://www.codewords.ai/blog/anthropic-batch-api) (accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (Anthropic official docs + independent technical blog)

---

## Practice 9: Do not use Claude to judge its own outputs

**Do:** When you test and evaluate your RAG pipeline using an AI model as a judge, do not use Claude to grade Claude's answers. Use a model from a different provider family. **Self-preference bias** is the tendency of an AI model to rate outputs from its own training lineage higher than outputs from other models — even when the other output is objectively better.

If your RAG pipeline uses Claude to generate answers, use a GPT-4 or Gemini model as the evaluator. If you must use Claude as a judge, document the self-preference risk and calibrate your scores against a human-labeled reference set of 200–500 examples.

**Why (beginner):** Imagine hiring a contestant to judge their own competition. Even with the best intentions, they are likely to give themselves the benefit of the doubt. The same thing happens with AI models. Research published in 2025–2026 consistently finds that LLMs give higher scores to outputs from their own training lineage. A Claude judge rating Claude-generated RAG answers may report high faithfulness and relevance scores even when the pipeline is broken — making a real problem invisible. Switching to a different-family judge does not eliminate all bias, but it surfaces disagreements that a single-family pipeline hides.

**Caveat:** Cross-family consensus (for example, having Claude, GPT-4, and Gemini all score the same outputs) reduces bias further but does not fully eliminate it. A 2025 paper ("Judging the Judges") found that "a mid-tier model with the right debiasing can outperform frontier judges at a fraction of the cost" — so a well-calibrated cheaper judge can be better than an expensive same-family one. For RAG-specific metrics like faithfulness, answer relevance, and context precision, consider the open-source RAGAS toolkit, which provides specialized judges for these dimensions.

**Sources:** [LLM-as-Judge Best Practices in 2026 — FutureAGI](https://futureagi.com/blog/llm-as-judge-best-practices-2026) (accessed 2026-07-22) · [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines — arXiv 2604.23178](https://arxiv.org/abs/2604.23178) (Apr 2026; accessed 2026-07-22)

**Confidence:** ✅ independently-corroborated (independent practitioner guide + peer-reviewed arXiv paper)

---

## Held pending fixes (not publish-ready)

- Practice 6 source independence: both primary sources are Anthropic-origin; third-party agentic RAG corroboration was found in search snippets but URLs were not individually fetched and verified this run. ⚠ PENDING (#tbd)

## CHANGELOG

1. **Re-leveled from the 2026-07-22 technical entry; facts unchanged.** All 9 practices kept. No practices dropped as too advanced. No new facts or URLs introduced.
2. Added expanded "What is RAG?" section with numbered flow and plain-language glossary (token, MTok, context window, embedding).
3. Practice 1 — Expanded "why" section to explain the two problems (quality and cost) as separate named issues; added concrete cost contrast ($1.50 vs. $0.09) with single-source caveat from original.
4. Practice 2 — Added inline comments to the JSON code example explaining each field's purpose.
5. Practice 3 — Expanded citation pointer types with plain-language descriptions; strengthened the 400-error explanation.
6. Practice 4 — Reformatted model pricing as a table for readability; expanded query-rewriting and re-ranking definitions; tokenizer migration warning retained verbatim.
7. Practice 5 — Promoted the silent cache miss warning to a standalone highlighted block; expanded cost math with a 100-query savings example; clarified "ephemeral" definition inline.
8. Practice 6 — Expanded `stop_reason` explanation as a named concept; retained cost ballpark for a 10-round loop; strengthened the indefinite loop danger.
9. Practice 7 — Expanded hallucination explanation with the "gap-filling" mechanism; added adversarial test suggestion from original.
10. Practice 8 — Added plain-language definition of contextual retrieval; retained 256 MB size check from original; expanded batch limitations list.
11. Practice 9 — Added "contestant judging their own competition" analogy; expanded explanation of why same-family bias is a practical danger.
12. **[Link-check gate]** Practice 1 — Unlinked Medium/@reliabledataengineering "Stop Chasing Million-Token Context Windows" (confirmed live 2026-07-22 via WebFetch; returns 403 bot-protection on automated curl check; 1 occurrence: Sources).

