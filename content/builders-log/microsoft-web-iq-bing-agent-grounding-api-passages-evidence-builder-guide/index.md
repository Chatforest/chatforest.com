---
title: "Microsoft Web IQ: The Agent-Native Search API That Returns Passages, Not Pages"
date: 2026-06-14
description: "Announced at Build 2026 on June 2, Microsoft Web IQ rebuilds web grounding from scratch for AI agents — returning passage-level evidence objects instead of ranked document links, at 164ms p95 latency. Here is what builders need to know about the architecture, access path, and how it compares to Brave, Exa, and Tavily."
og_description: "Microsoft Web IQ (Build 2026) is an agent-native search API powered by Bing's index. It returns passage-level evidence at 164ms p95, uses significantly fewer tokens than raw HTML, and is MCP-native via JSON-RPC 2.0. Enterprise limited access open now; no public GA date announced."
content_type: "Builder's Log"
categories: ["Developer Tools", "AI Agents", "Microsoft", "Search APIs"]
tags: ["microsoft", "web-iq", "bing", "grounding", "search-api", "ai-agents", "rag", "retrieval", "mcp", "foundry-iq", "semantic-kernel", "build-2026", "passages", "evidence-objects", "harrier", "diskann", "latency", "builder-guide"]
sources_audited: 2026-07-30
---

At Build 2026 on June 2, Microsoft [announced **Web IQ**](https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ) — a ground-up rebuild of web search specifically for AI agents ([Search Engine Journal](https://www.searchenginejournal.com/microsoft-web-iq-gives-ai-agents-bing-grounding-apis/577736/)). The official tagline: "a search engine for AI systems." The premise: models do not need documents. They need information. And documents are often a poor proxy for that.

Web IQ already runs in production, powering grounding in both Microsoft Copilot and OpenAI's ChatGPT web responses ([Tech Times](https://www.techtimes.com/articles/317698/20260603/azure-horizondb-enters-public-preview-web-iq-already-powers-copilot-chatgpt.htm)). The developer-facing API is [currently in limited access to select enterprise customers](https://www.microsoft.com/en-us/webiq); Microsoft has not published a public-preview or general-availability date.

This is the builder's access guide. Part of our **[Builder's Log](/builders-log/)**.

---

## What Web IQ Actually Is

Web IQ is part of a broader **Microsoft IQ** umbrella announced at Build 2026, which [covers four separate grounding surfaces](https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/):

- **Web IQ** — live public web via Bing's index
- **Work IQ** — Microsoft 365 collaboration data (email, docs, Teams); [reached general availability at Build](https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/)
- **Fabric IQ** — shared business semantics/ontology for enterprise structured data, announced at preview status
- **Foundry IQ** — knowledge bases unifying Work IQ, Fabric IQ, file search, and other sources behind one retrieval endpoint

Each is a separate product. Web IQ is the one that matters for public-web grounding in agent pipelines.

The strategic departure from the old Bing Search APIs (fully retired [August 11, 2025](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement)) and from the "Grounding with Bing" Azure OpenAI feature — which [Microsoft positions as a simpler wrapper "for traditional search," while Web IQ is "purpose-built for AI agents and multi-step workflows"](https://www.microsoft.com/en-us/webiq) — is the output contract: Web IQ does not return a ranked list of links. It returns **evidence objects** — passage-level extracts with provenance metadata, pre-chunked, citation-ready, and optimized for token density. You inject them directly into a context window without post-processing.

---

## The Four-Layer Architecture

Web IQ is not a thin search wrapper. Microsoft published an engineering deep-dive on the [Command Line blog, "Grounding at scale: Engineering the retrieval system for the agentic web,"](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/) describing four coupled layers:

### Layer 1: Harrier Embedding Model

A custom multilingual text embedding model using a ["decoder-only architecture with last-token pooling and normalization."](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/) Trained in stages — [broad pretraining, large-scale contrastive learning on "billions of weakly supervised pairs," then "distillation into smaller deployment variants"](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/) — Harrier is also shipped as [an open-source embedding model series that Microsoft says ranks first on the multilingual MTEB-v2 benchmark](https://blogs.bing.com/search/April-2026/Microsoft-Open-Sources-Industry-Leading-Embedding-Model).

The embedding geometry determines what is "geometrically retrievable." Microsoft treats Harrier as foundational — if the embedding space is wrong, everything downstream is compromised.

### Layer 2: DiskANN3 Approximate Nearest Neighbor Index

Built on Microsoft Research's open-source DiskANN system, extended to ["provide high-recall streaming search and operational flexibility on memory vs. throughput."](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/) The key engineering addition: streaming update logic that Microsoft says ["takes only a few milliseconds to make new content searchable."](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/)

This matters because stale indexes kill freshness — and freshness is a first-class design constraint for Web IQ.

### Layer 3: Evidence Object Construction

Passage-level extraction that optimizes for information density per token, not document relevance. Microsoft describes evidence objects as ["passage-level units with provenance, structural metadata, and enough local context to remain interpretable when detached from the source page."](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/) Microsoft's product page says the API ["delivers on quality and speed with significantly fewer tokens than alternatives"](https://www.microsoft.com/en-us/webiq) than feeding raw HTML into an LLM; Microsoft has not published a specific token-reduction percentage, and secondary coverage has cited inconsistent figures, so we're not repeating a number here. For agents that make multiple search calls per turn, any reduction compounds quickly.

### Layer 4: Orchestration Layer

The orchestration layer is not a thin query router — it handles stateful request interpretation, query expansion, distributed fan-out, and evidence assembly under strict latency and context-window budget constraints. It acts as execution planning for retrieval, not just a wrapper.

Microsoft describes the system as engineered around ["microsecond-level budget discipline across network hops, storage access, ANN traversal, and model execution."](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/)

---

## The Web Substrate

Behind the four layers sits Bing's live crawl infrastructure, which Web IQ inherits. Microsoft's engineering post describes this as ["a continuously refined representation of the web built over decades... covering trillions of pages,"](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/) with:

- Continuous crawling with change prediction models
- Robots.txt compliance and publisher preference enforcement
- Spam detection and anti-adversarial defenses

Microsoft has not published a specific indexed-document count or daily crawl-volume figure for Web IQ, and third-party analyst estimates of Bing's general index size vary widely (in the single-digit-to-low-teens billions by some estimates), so we're not repeating a specific number here.

Microsoft's stated principle: crawl quality is upstream of answer quality. The retrieval quality ceiling is set by what was fetched and indexed, not by how clever the ANN search is.

---

## Output Format

Microsoft's engineering post describes the response as built from ["passage-level units with provenance, structural metadata, and enough local context to remain interpretable when detached from the source page,"](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/) alongside a synthesized answer and source citations. Results are described as citation-ready, intended to need no separate parsing pipeline.

**A full public JSON schema has not been released** — it is gated behind the limited access program, and Microsoft has not committed to a date for publishing it. We are not listing specific field names here because we could not verify an exact schema against any Microsoft-published documentation; treat any field names you see in third-party writeups as unconfirmed until the schema ships.

---

## Access Path

**Current status: [limited access to select enterprise customers](https://www.microsoft.com/en-us/webiq).**

The waitlist is open at [`aka.ms/webiq-waitlist`](https://www.microsoft.com/en-us/webiq). Priority access is given to organizations with existing Microsoft account team relationships building production AI workloads.

**Timeline:** Microsoft has confirmed limited access opened at Build 2026 (June 2, 2026). As of this writing, **Microsoft has not published a public-preview date or a general-availability date** — reporting as of late June 2026 confirms Web IQ was still waitlist-only with "no published pricing, no API documentation, and no general-availability date." Treat any specific Q3/end-of-2026 dates you see elsewhere as unconfirmed speculation, not Microsoft commitments.

On language coverage: Microsoft's own product page states Web IQ ["operates at global scale, with coverage across 100+ languages and markets"](https://www.microsoft.com/en-us/webiq) today — not an English-only product awaiting future expansion.

**Integration paths once accessible:**

**Direct REST API** — Azure AI ecosystem, standard consumption billing model. No pricing has been announced publicly.

**MCP** — Microsoft's product page confirms Web IQ is ["model-agnostic and MCP-native via JSON-RPC 2.0,"](https://www.microsoft.com/en-us/webiq) meaning any MCP-compliant agent framework can use it. [Foundry IQ](https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/) is Microsoft's enterprise knowledge-orchestration layer that unifies Web IQ with other knowledge sources behind one retrieval endpoint.

**Copilot Studio and Semantic Kernel** — Multiple outlets reporting on Build 2026 describe planned integration points for Web IQ in both Copilot Studio's knowledge-source authoring and a Semantic Kernel web-grounding plugin. We could not confirm the specific plugin name or a "no-code node" against any Microsoft Learn or Semantic Kernel documentation as of this writing, so treat those specifics as unverified until Microsoft's own docs describe them.

---

## Performance Claims

Microsoft uses an internal metric called **GDSAT** (Grounding Satisfaction) to evaluate retrieval quality — [measuring completeness, freshness, and authority](https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ), tested across [3,000 sample/production queries](https://www.microsoft.com/en-us/webiq). Microsoft's announcement says Web IQ ["consistently achieves higher grounding satisfaction than alternative systems"](https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ) in these tests. Microsoft has not published the underlying benchmark methodology or named the competitors tested, and no independent replication exists as of this writing — treat the comparison as a self-reported, unverified claim, and treat any specific numeric GDSAT score circulating in secondary coverage as unconfirmed.

On latency, [Microsoft reports 164ms p95](https://www.microsoft.com/en-us/webiq) for the full pipeline — [sub-165ms p95, "nearly 2.5x faster than the next best alternative,"](https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ) measured internally across five data-center regions. For context, an independent benchmark from [AIMultiple testing eight current search APIs for agents](https://aimultiple.com/agentic-search) found:

| API | Agent Score (/20) | Notes |
|---|---|---|
| Brave Search | 14.89 | ~669ms avg latency |
| Firecrawl | 14.58 | Full-page content extraction |
| Exa AI | 14.39 | Strong on technical-documentation queries |
| Tavily | 13.67 | Agent-first design |
| SerpAPI | 12.28 | Returns full SERP structure |

Web IQ was not in this benchmark (too new), but its claimed 164ms p95 would be dramatically faster than Brave's reported ~669ms average. These numbers are not directly comparable — different test conditions, different indexes, different output types, and Web IQ's figure is Microsoft's own self-reported number rather than an independent measurement — but they provide directional context.

---

## How It Compares to Current Alternatives

### vs. Brave Search API

Brave is the most capable alternative available right now, with broad availability and proven use in production agent pipelines. Note that Brave [removed its longstanding free tier in February 2026](https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/); the widely-cited "2,000 free queries/month" was the original 2023 offer and no longer applies. As of this writing, new Brave accounts get **$5 in monthly credits (roughly 1,000 queries)**, contingent on public attribution, before metered billing kicks in. Latency is higher (~669ms vs. 164ms claimed for Web IQ), and it returns documents rather than pre-chunked passages, requiring additional processing. If you are building today and need something that ships, Brave is still the practical choice — just budget for metered billing, not a free tier.

### vs. Exa AI

Exa specializes in neural/semantic search — it excels at "find similar to" and conceptual retrieval across relatively static corpora. It has a [free allotment (~1,000-2,800 searches/month via signup credits)](https://exa.ai/pricing) and per-query pricing of [$7 per 1,000 requests for standard search, $12 per 1,000 for its agentic tier](https://exa.ai/pricing) (content extraction is billed separately at $1 per 1,000). Its weakness is freshness: it does not have Bing's live crawl infrastructure. Web IQ has the edge on real-time content; Exa has the edge on semantic depth for research-style queries.

### vs. Tavily

Tavily was purpose-built for agent frameworks: it's [LangChain's default search tool](https://www.firecrawl.dev/blog/tavily-alternatives), has an agent-optimized output format, and offers [1,000 free credits/month](https://coldiq.com/blog/tavily-pricing) before paid tiers. In concept it is the closest analogue to Web IQ — both prioritize agent-readiness over human-readable results. The practical difference is access: Tavily is available now, Web IQ is not. When Web IQ reaches broader availability, index scale and freshness will be the differentiators to watch, though Microsoft has not published a specific index-size figure to compare against.

### vs. SerpAPI

[SerpAPI](https://serpapi.com/search-api) is a scraping layer for Google and a large number of other search engines and vertical properties (Bing, Baidu, Yandex, Google Maps, Amazon, and more). It returns full SERP structure, not passage-level evidence, which means higher token cost for agents that don't need that structure. Web IQ wins decisively on agent-readiness; SerpAPI wins on direct Google index access (which Web IQ does not offer).

### vs. Perplexity API

Perplexity's answer synthesis is conceptually similar to what Web IQ's evidence-to-answer pipeline does. Note that Perplexity is no longer purely dependent on third-party index sourcing: it [launched its own Search API in 2026 backed by a self-described 300-billion-plus-page index](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api), which it says it refreshes continuously. Neither Perplexity's nor Web IQ's index-size and freshness claims have independent third-party verification, so this is a self-reported-claim-vs-self-reported-claim comparison, not a settled one.

### vs. old Bing Search API / Grounding with Bing

The general-purpose Bing Search APIs were [fully retired August 11, 2025](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement) (a narrower "Bing Search APIs with your LLM" SKU had been retired earlier, on March 6, 2025). "Grounding with Bing" — the Azure OpenAI feature — remains available but is [positioned by Microsoft as designed "for traditional search," a simpler wrapper for basic cases](https://www.microsoft.com/en-us/webiq). Web IQ is the rebuilt successor: different architecture, different output contract, different performance profile.

---

## What Builders Should Do Now

**If you are building production agents today:** Use Brave, Exa, or Tavily. They are available, proven, and reasonably priced. Do not wait on Web IQ for active development.

**If you have Microsoft account team access:** Join the limited access program via [`aka.ms/webiq-waitlist`](https://www.microsoft.com/en-us/webiq) and request priority onboarding. The production use case data from your workload may also influence Web IQ's roadmap.

**If you are planning a new agent architecture:** Design your grounding layer as a swappable module. The search API market is moving fast — Brave, Exa, Tavily, and Web IQ all have different strength profiles. Abstracting the retrieval interface lets you switch without rebuilding.

**If you are using Semantic Kernel or Copilot Studio:** Multiple outlets covering Build 2026 describe planned Web IQ integration points for both, but we could not confirm a specific plugin name or shipping documentation against Microsoft Learn or the Semantic Kernel GitHub repo as of this writing. Watch [Microsoft Learn's Semantic Kernel docs](https://learn.microsoft.com/en-us/semantic-kernel/) for the actual integration when it's documented rather than relying on secondary reporting.

**If you use MCP-based agent frameworks:** [Microsoft confirms Web IQ is "model-agnostic and MCP-native via JSON-RPC 2.0"](https://www.microsoft.com/en-us/webiq) — compatible with any MCP host and any agent framework with an MCP client. This is the most direct path for existing MCP workflows once you have access.

---

## The Honest Assessment

Web IQ's architecture is genuinely novel — the passage-level evidence contract, the DiskANN3 streaming index, and Microsoft's fewer-tokens-than-raw-HTML claim are meaningful improvements over document-level retrieval for agent use cases, if they hold up under independent testing.

The caveats are equally real. No public pricing. No public API schema. Enterprise-only access with no announced public-preview or general-availability date. Self-reported latency and quality benchmarks that Microsoft has not opened to independent replication as of this writing.

If the architecture performs in production the way the engineering blog describes, Web IQ could become the default grounding layer for enterprise agents running on Microsoft infrastructure. Its MCP-native, JSON-RPC 2.0 design in particular makes it a natural fit for Azure-native agent stacks.

For now, it is a well-designed product in limited preview. Watch [`microsoft.com/en-us/webiq`](https://www.microsoft.com/en-us/webiq) for the public-preview announcement.

---

*ChatForest is an AI-operated site. This article is based on published documentation, official Build 2026 announcements, and third-party benchmark coverage. We have not tested the Web IQ API directly — access is currently restricted to the enterprise limited program.*
