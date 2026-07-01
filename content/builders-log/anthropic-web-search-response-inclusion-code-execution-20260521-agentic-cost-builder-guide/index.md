---
title: "Anthropic June 11 Tool Updates: response_inclusion Drops Consumed Search Blocks, code_execution_20260521 Adds 90-Second Budget Signal"
date: 2026-07-02
description: "Two June 11 API improvements for builders running research agents: web_search_20260318 and web_fetch_20260318 add response_inclusion: 'excluded' to drop dynamically-filtered search blocks from your API response, and code_execution_20260521 discloses the 90-second per-cell limit in its tool description so Claude can budget long-running cells."
og_description: "Two June 11 API improvements reduce agentic loop costs: response_inclusion: excluded drops consumed search blocks from the API response, and code_execution_20260521 tells Claude about its 90-second cell limit before it starts running."
content_type: "Builder's Log"
categories: ["API", "Cost Optimization", "Agentic AI"]
tags: ["anthropic", "claude", "api", "web-search", "web-fetch", "code-execution", "agentic", "cost-optimization", "response-inclusion", "builder-guide"]
draft: false
---

On June 11, 2026, Anthropic shipped two tool updates that work together to reduce token costs in multi-step research agents: new tool versions for web search and web fetch that add a `response_inclusion` parameter, and a new code execution version that discloses the per-cell execution time limit in its tool description. Neither change required a beta header, and neither was widely covered outside the release notes.

---

## The problem both changes address

Research agents that combine web search with dynamic filtering hit a specific inefficiency. When Claude uses web search in a loop, it often processes the raw results immediately via code execution — filtering, extracting, summarizing — before the relevant content ever reaches its output turn. Those processed result blocks are "consumed": the useful information was already extracted and the raw HTML or search result text is no longer needed. But before June 11, the API returned those consumed blocks in the response anyway, charging output tokens for content your application would never read.

Separately, when Claude runs code in a sandbox and a cell takes too long, the API returns a `detection_timeout` result. Before `code_execution_20260521`, Claude had no way to know this limit existed at the time it was writing the cell. It could structure a slow computation as a single 150-second block, have it timeout, and retry. Now it knows the limit before it starts.

---

## response_inclusion on web_search_20260318 and web_fetch_20260318

### What it does

The `response_inclusion` parameter controls whether search and fetch result blocks appear in the API response when those results were consumed by a completed code execution call in the same turn.

Set `"response_inclusion": "excluded"` and any `server_tool_use` + `web_search_tool_result` (or `web_fetch_tool_result`) block pair that was consumed by a completed code execution call is dropped from the response entirely. The default is `"full"`, which preserves prior behavior.

**The exclusion is conditional:** it only applies when:
1. The result block was consumed by a code execution call, AND
2. That code execution call completed (not paused mid-execution)

Results from direct web search calls — where Claude searched and responded from the results directly, without routing them through code execution — are always returned in full. They need to come back on the next turn for the citation references to resolve. Results from code execution calls that paused with `stop_reason: "pause_turn"` before completing are also returned in full, because the loop hasn't finished and you need to pass them back.

### Why it matters

A research agent that runs five searches per turn, processes each through dynamic filtering, and generates a 2,000-token response can easily accumulate several thousand extra output tokens from search result blocks that no downstream code ever reads. At $10 per 1,000 searches and standard output token pricing, those orphaned result blocks are a visible line item at production scale.

With `response_inclusion: "excluded"`, the API response contains only what your application actually needs: the final text output, any unconsumed tool results, and citation references.

### Implementation

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Research the three largest data breaches announced this week and summarize each in two sentences.",
        }
    ],
    tools=[
        {
            "type": "web_search_20260318",
            "name": "web_search",
            "response_inclusion": "excluded",
            "max_uses": 6,
        },
        {
            "type": "code_execution_20260521",
            "name": "code_execution",
        },
    ],
)

print(response)
```

The change is a single field on the tool definition. No beta header is required for either `web_search_20260318` or `web_fetch_20260318`.

### Applying to web fetch

The same parameter applies to the web fetch tool, which retrieves full page content rather than search-result snippets:

```python
tools=[
    {
        "type": "web_fetch_20260318",
        "name": "web_fetch",
        "response_inclusion": "excluded",
    },
    {
        "type": "code_execution_20260521",
        "name": "code_execution",
    },
]
```

In document-processing pipelines — where an agent fetches a page, extracts structured data via code, and continues — fetched HTML can easily exceed 50,000 tokens. Dropping those consumed fetch results saves real money.

---

## code_execution_20260521: the 90-second budget signal

### What changed

`code_execution_20260521` is functionally identical to `code_execution_20260120` (REPL state persistence, programmatic tool calling) with one addition: the per-cell execution time limit is included in the tool description that Claude reads when it receives the tool definition.

Before this version, Claude knew nothing about the 90-second wall-clock limit on individual cells until it hit it. That produced a specific failure pattern: Claude would write a single long-running computation as one cell, the cell would timeout and return `detection_timeout`, Claude would try to understand why, and then restructure the work — wasting turns and tokens on recovery.

With `code_execution_20260521`, Claude sees the limit in the tool description before it writes any code. It can budget long-running computations across multiple cells, add intermediate checkpoints, or warn you when a requested computation may not fit within the limit.

### What a timeout looks like

A cell that exceeds 90 seconds returns:

```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_...",
  "content": {
    "type": "code_execution_result",
    "return_code": 1,
    "stderr": "",
    "stdout": "",
    "result": {
      "type": "detection_timeout"
    }
  }
}
```

Claude can handle this, but recovery takes a turn. The budget signal eliminates most cases where this happens on avoidable computations.

### Migration from earlier versions

```python
# Before (no limit disclosure)
tools=[{"type": "code_execution_20260120", "name": "code_execution"}]

# After (90-second limit in tool description)
tools=[{"type": "code_execution_20260521", "name": "code_execution"}]
```

REPL state and programmatic tool calling work identically across both versions. The only difference is the tool description.

---

## How the two changes combine

The combination is intentional. When you pair `web_search_20260318` (or `web_fetch_20260318`) with `code_execution_20260521`:

- **Dynamic filtering runs free.** Code execution is not charged when used alongside web search or web fetch.
- **Claude filters search results before they hit context.** Instead of loading full HTML into the conversation, code execution processes and discards what's irrelevant.
- **Consumed result blocks don't come back.** With `response_inclusion: "excluded"`, the filtered-and-discarded search content never appears in the API response.
- **Long extractions finish safely.** Claude knows the 90-second cell limit and can structure large page parses into bounded chunks.

The result is a research agent architecture that costs less at every step: less input from dynamic filtering, less output from excluded result blocks, fewer retry turns from timeout surprises.

---

## Version reference

| Tool | Version | Key addition |
|------|---------|--------------|
| web_search | `web_search_20250305` | Basic search |
| web_search | `web_search_20260209` | Dynamic filtering |
| web_search | `web_search_20260318` | + `response_inclusion` |
| web_fetch | `web_fetch_20260209` | Dynamic filtering |
| web_fetch | `web_fetch_20260318` | + `response_inclusion` |
| code_execution | `code_execution_20250825` | Bash + file ops |
| code_execution | `code_execution_20260120` | + REPL state, programmatic tool calls |
| code_execution | `code_execution_20260521` | + 90-second limit in tool description |

The `web_search_20260318` and `web_fetch_20260318` versions require no beta header. The `code_execution_20260521` version requires no beta header. All three are available on the Claude API only — not Amazon Bedrock or Google Cloud.

---

## Source

Both changes shipped in the [Anthropic platform release notes](https://platform.claude.com/docs/en/release-notes/api) on June 11, 2026. The full `response_inclusion` specification is in the [web search tool documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#response-inclusion). The code execution version table and per-cell limit are documented in the [code execution tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool).
