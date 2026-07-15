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
| `content/guides/best-ai-agent-frameworks-2026.md` | ✅ DONE (Run 2454) | PyPI stats links (LangGraph, OpenAI Agents SDK); LangChain State of AI Agent Engineering report; DSPy Shopify 550× (dspy.ai/community/use-cases); DSPy arXiv 2310.03714; CAMEL-AI arXiv 2303.17760 + OWL GAIA score (github.com/camel-ai/owl); Haystack Airbus + Lufthansa case study links + deepset.ai/case-studies; smolagents GAIA #1 (HuggingFace blog); OpenAI Agents SDK docs + Swarm GitHub |
| `content/guides/eu-ai-act-article-50-chatbot-disclosure-compliance-guide-2026.md` | ✅ DONE (Run 2453) | Article 50 official EU link, Digital Omnibus (White & Case), C2PA + Code of Practice, penalties link |
| `content/guides/ai-agent-protocol-stack-2026.md` | 🔲 TODO P2 | Protocol claims |
| `content/guides/datadog-mcp-server-production-lessons.md` | ✅ DONE (Run 2453) | GA press release (GlobeNewswire), engineering blog (datadoghq.com), docs link, AWS DevOps Agent GA blog |
| `content/guides/best-image-generation-mcp-servers.md` | 🔲 TODO P2 | Named products |
| `content/guides/mcp-anti-patterns.md` | 🔲 TODO P3 | General MCP |
| `content/guides/pinterest-mcp-production-case-study.md` | ✅ DONE (Run 2453) | Pinterest Engineering Blog (Medium), InfoQ coverage |
| High-priority reviews (named company claims) | 🔲 TODO — batch 2+ | See P1 review list below |

### Run 2453 (2026-07-16) — Batch 2

| File | Status | Notes |
|---|---|---|
| `content/guides/eu-ai-act-article-50-chatbot-disclosure-compliance-guide-2026.md` | ✅ DONE | Article 50 primary text (EU Service Desk + artificialintelligenceact.eu), Digital Omnibus (White & Case), C2PA (c2pa.org), Code of Practice (EC digital-strategy), penalties link |
| `content/reviews/anthropic-900-billion-valuation-30b-round-2026-guide.md` | ✅ DONE | Anthropic.com/news/series-h, CNBC, TechCrunch, Ramp AI Index (ramp.com), Bloomberg/Zoom stake, footer hyperlinked |
| `content/reviews/ai-guardrails-stripped-meta-google-llama-gemma-abliteration-2026.md` | ✅ DONE | Irish Times + eWeek coverage inline, Heretic GitHub link (github.com/p-e-w/heretic), footer sources hyperlinked |
| `content/guides/datadog-mcp-server-production-lessons.md` | ✅ DONE | GA announcement (GlobeNewswire), engineering blog + docs (datadoghq.com), AWS DevOps Agent GA blog (aws.amazon.com), MTTR/accuracy stats linked |
| `content/guides/pinterest-mcp-production-case-study.md` | ✅ DONE | Pinterest Engineering Blog (Medium), InfoQ coverage inline and footer |
| `content/builders-log/waic-2026-xi-keynote-huawei-atlas-950-china-ai-governance-builder-preview/index.md` | ✅ DONE | CGTN, Global Times, faq.com.tw (Xi keynote), SCMP (Atlas 950), George Chen Substack, Digitimes (ZTE AI phone) |

---

### Run 2454 (2026-07-16) — Batch 3

| File | Status | Notes |
|---|---|---|
| `content/guides/best-ai-agent-frameworks-2026.md` | ✅ DONE | PyPI stats (langgraph, openai-agents), LangChain State of AI Agent Engineering report, DSPy Shopify 550× source (dspy.ai/community/use-cases), DSPy arXiv 2310.03714, CAMEL-AI arXiv 2303.17760, OWL GAIA 69.09% (github.com/camel-ai/owl), Haystack Airbus + Lufthansa case studies + deepset.ai/case-studies, smolagents GAIA #1 (huggingface.co/blog/beating-gaia), OpenAI Agents SDK official docs + Swarm GitHub |

---

### P1 Reviews (named company claims, tackle next)

These reviews make specific claims about named companies that carry legal/brand risk:

- `content/reviews/anthropic-900-billion-valuation-30b-round-2026-guide.md` — ✅ DONE (Run 2453): Anthropic.com announcement, CNBC, TechCrunch, Ramp AI Index, Bloomberg/Zoom stake
- `content/reviews/ai-guardrails-stripped-meta-google-llama-gemma-abliteration-2026.md` — ✅ DONE (Run 2453): Irish Times, eWeek links in body; Heretic GitHub link; footer sources hyperlinked
- `content/reviews/anthropic-acquires-stainless-sdk-mcp-infrastructure-acquisition-review.md` — ✅ DONE (Run 2452)
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
