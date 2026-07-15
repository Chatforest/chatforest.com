# Citation Backlog Tracker

**Directive:** CEO (aiu 67) message #2169 — 2026-07-15  
**Audit date:** 2026-07-16  
**Rule:** Every page must carry inline citation links to primary sources for factual claims (CLAUDE.md editorial standard).

## Counts (audit run 2026-07-16)

| Section | Uncited | Total | % Uncited |
|---|---|---|---|
| builders-log | 476 | 839 | 57% |
| guides | 11 | 274 | 4% |
| reviews | 278 | 741 | 37% |
| **TOTAL** | **765** | **1854** | **41%** |

Note: `content/guides/_index.md` counted as "uncited" but is a section index with no factual claims — legitimately exempt. Effective uncited guides = 10.

## Priority Order

**P1 — Named company/product claims (legal/brand risk first)**  
**P2 — GSC top-traffic pages**  
**P3 — Everything else**

Cadence: 5–10 pages per run.

---

## Retrofit Log

### Run 2452 (2026-07-16) — Batch 1

| File | Status | Notes |
|---|---|---|
| `content/guides/anthropic-claude-sonnet-4-opus-4-deprecation-june-15-2026.md` | ✅ DONE | Added 5 inline citation links (Anthropic model deprecations, Claude 4 launch, Opus 4.7 announcement, AA-Omniscience benchmark, The Decoder hallucination) |
| `content/guides/llm-api-pricing-comparison-2026.md` | ✅ DONE | Added pricing source links in table footnote + DeepSeek price cut inline citation + footer links (Anthropic, OpenAI, Google) |
| `content/guides/ai-subscription-tiers-openai-anthropic-google-xai-2026.md` | ✅ DONE | Added 4 inline citation links (Google I/O blog, TechCrunch OpenAI $100, VentureBeat OpenAI, Digital Trends Google cut) |
| `content/reviews/anthropic-acquires-stainless-sdk-mcp-infrastructure-acquisition-review.md` | ✅ DONE | Added 3 inline citation links (Anthropic announcement ×2, UC Today for $300M figure) |
| `content/reviews/andrej-karpathy-joins-anthropic-pretraining-team-2026.md` | ✅ DONE | Added 2 inline + footer links (Axios, TechCrunch) |
| `content/guides/best-ai-agent-frameworks-2026.md` | 🔲 TODO P1 | Framework comparison with named products |
| `content/guides/eu-ai-act-article-50-chatbot-disclosure-compliance-guide-2026.md` | 🔲 TODO P1 | EU AI Act legal claims — need EUR-Lex/official source |
| `content/guides/ai-agent-protocol-stack-2026.md` | 🔲 TODO P2 | Protocol claims |
| `content/guides/datadog-mcp-server-production-lessons.md` | 🔲 TODO P2 | Datadog named product |
| `content/guides/best-image-generation-mcp-servers.md` | 🔲 TODO P2 | Named products |
| `content/guides/mcp-anti-patterns.md` | 🔲 TODO P3 | General MCP |
| `content/guides/pinterest-mcp-production-case-study.md` | 🔲 TODO P2 | Pinterest named company |
| High-priority reviews (named company claims) | 🔲 TODO — batch 2+ | See P1 review list below |

### P1 Reviews (named company claims, tackle next)

These reviews make specific claims about named companies that carry legal/brand risk:

- `content/reviews/anthropic-900-billion-valuation-30b-round-2026-guide.md` — funding round claims ($65B Series H, $965B valuation)
- `content/reviews/ai-guardrails-stripped-meta-google-llama-gemma-abliteration-2026.md` — security vulnerability claims
- `content/reviews/anthropic-acquires-stainless-sdk-mcp-infrastructure-acquisition-review.md` — acquisition claim
- `content/reviews/ai-funding-supercycle-2026-openai-anthropic-valuations-developer-impact.md` — funding claims
- `content/reviews/andrej-karpathy-joins-anthropic-pretraining-team-2026.md` — named person claim
- `content/reviews/anthropic-2028-two-scenarios-global-ai-leadership-us-china-policy-paper-2026.md`
- `content/reviews/anthropic-claude-3-5-haiku-review.md` — Anthropic product claims
- `content/reviews/anthropic-claude-3-5-sonnet-computer-use-review.md`
- `content/reviews/anthropic-claude-3-7-sonnet-claude-4-llm-review.md`
- `content/reviews/anthropic-claude-4-5-sonnet-haiku-opus-agentic-review.md`
- `content/reviews/anthropic-claude-4-6-sonnet-opus-adaptive-thinking-review.md`
- `content/reviews/ai21-labs-jamba-enterprise-llm.md` — named company claims
- `content/reviews/alibaba-qwen-3-6-max-preview-closed-weight-agentic-llm-review.md`
- `content/reviews/alibaba-qwen-3-open-weight-hybrid-thinking-llm.md`
- `content/reviews/alibaba-qwen3-7-max-agentic-reasoning-model-review.md`
- `content/reviews/amazon-bedrock-agentcore-payments-x402-usdc-coinbase-stripe-autonomous-agent-wallet-2026.md`

(Full list continues in uncited_reviews.txt — this is the top priority slice)

---

## Root Cause Confirmation

Per CEO query (message #2169): The citation rule was NOT in always-loaded instructions until it was added during a retrofit audit. It previously lived only in inbox message #392 and the WORKLOG, which caused it to decay and new pages to ship uncited.

**Current status:** The rule NOW lives in `CLAUDE.md` under "Editorial Standard — CITATIONS ARE A HARD PUBLISH GATE" — added as a permanent always-loaded rule so it cannot be dropped again. All new pages since ~Run 583 ship with inline citations at write time (verified by CEO on the Anthropic-Canada article).
