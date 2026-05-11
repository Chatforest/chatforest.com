# Helicone Review: LLM Proxy + Observability (Now in Maintenance Mode)

> Helicone offers minimal-friction LLM observability via a proxy-first architecture with built-in caching, rate limiting, and multi-provider routing. Acquired by Mintlify in March 2026 and now in maintenance mode.


# Helicone Review: LLM Proxy + Observability (Now in Maintenance Mode)

**Rating: 3.5/5**

Helicone is an open-source LLM observability platform and AI gateway with a genuinely clever integration model: rather than wrapping your LLM client in a new SDK, it asks you to change a single URL. That minimal-friction approach, combined with built-in caching and rate limiting, made Helicone stand out in a crowded observability space. There's a catch, though — Helicone was [acquired by Mintlify](https://helicone.ai/) in March 2026 and is now in maintenance mode. No new features are coming. That changes the calculus for anyone evaluating it today.

---

## What Helicone Is

Helicone sits between your application and the LLM provider's API. Every request passes through Helicone's proxy, which logs the full request and response, tracks token counts and cost, and applies any configured behaviors — caching, rate limiting, custom metadata — before forwarding to the actual provider. The overhead claim is under 1ms in self-hosted mode.

Alongside the proxy model, Helicone has an AI Gateway mode: a unified endpoint (`https://ai-gateway.helicone.ai`) that routes to 100+ models across providers, accepting a single API key and normalizing to an OpenAI-compatible interface. This is effectively a provider-agnostic LLM router bolted onto the observability layer.

By March 2026, Helicone had processed **14.2 trillion tokens** across **16,000 organizations** — scale that suggests the proxy model works at production volumes.

---

## Integration: The Two-Line Change

The proxy integration is as close to zero-friction as you can get. For OpenAI in JavaScript:

```javascript
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: "https://oai.helicone.ai/v1",       // ← change this
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`  // ← add this
  }
});
```

Nothing else changes. All your existing calls — `chat.completions.create`, streaming, function calling — pass through transparently. The Python SDK works identically. This contrasts with tools like W&B Weave (decorators on your functions) or LangSmith (often requires LangChain), where you're modifying application logic rather than just a config value.

Feature flags and metadata are passed as HTTP headers on individual requests, so they stay entirely decoupled from business logic:

```python
# Tag a request with custom metadata — no SDK changes
headers = {
    "Helicone-User-Id": user_id,
    "Helicone-Property-Feature": "checkout-assistant",
    "Helicone-Cache-Enabled": "true"
}
```

This header-based approach means Helicone works with *any* HTTP client, not just the official provider SDKs.

---

## Key Features

### Observability Core

Every logged request shows the full prompt and completion, model, token counts, latency, and computed cost. The dashboard filters by time range, model, user, and any custom property you've attached. At 16,000 organizations and 14.2 trillion tokens, the logging infrastructure has proven itself at scale.

**Sessions** group related requests into a coherent trace — useful for debugging multi-step agent workflows where a user's apparent single action spawns a chain of LLM calls, tool invocations, and retrieval steps. The `Helicone-Session-Id` and `Helicone-Session-Path` headers create a tree structure visible in the dashboard.

**Custom Properties** are arbitrary key-value metadata attached per-request. Tag by environment (`prod`/`staging`), feature flag, team, or billing account. These are retroactively queryable and filterable — you can ask "what's my LLM cost for the checkout feature this week?" without knowing in advance that you'd want that breakdown.

**User Tracking** via `Helicone-User-Id` aggregates engagement metrics per user: average requests per day, return session rates, retry patterns. This surfaces power users, at-risk churners, and anomalous usage that might indicate prompt injection attempts.

### Gateway Features

The caching layer uses Cloudflare's edge network. Identical requests (same URL + body + headers bucket) return cached responses with zero provider latency and zero token cost. The cache supports up to 20 variants per bucket for diversity-sensitive use cases, configurable TTL up to 365 days, and explicit bypass via header. Cache hits are visible on each response.

Rate limiting applies per user or per policy, enforced at the gateway before any provider request is made. This protects against runaway agents and abuse without application-level quota logic.

### Provider Coverage

Supported providers include OpenAI, Anthropic, Azure OpenAI, Google Gemini, DeepSeek, Together AI, Groq, Mistral, and OpenRouter, with 100+ models accessible through the unified gateway endpoint. LangChain and Vercel AI SDK have explicit integrations.

---

## Pricing

| Tier | Price | Requests | Retention | Seats |
|---|---|---|---|---|
| Hobby | Free | 10k/month | 7 days | 1 |
| Pro | $79/month | 10k + usage overage | 1 month | Unlimited |
| Team | $799/month | 10k + usage overage | 3 months | Unlimited |
| Enterprise | Custom | Custom | Custom | Custom |

The free tier's 7-day retention is a real limitation — trend analysis across a week is the ceiling. The Hobby → Pro jump ($0 to $79/month) is steep for early-stage projects. Helicone offers 50% off the first year for startups under two years old with less than $5M in funding, and $100 credit for open-source projects.

Self-hosted deployments are available via Docker and Helm (Kubernetes). The self-hosted path removes the data-residency concern and eliminates per-request costs beyond infrastructure.

---

## How It Compares

Helicone's clearest competitors in the observability space are LangSmith (LangChain's offering), W&B Weave, and OpenLIT. The meaningful differentiators:

**Helicone's strengths over competitors:**
- Proxy-as-gateway: caching and rate limiting come for free with the observability integration — no other tool in this category doubles as a functional LLM gateway
- Lowest integration friction of any observability tool: works with any HTTP client, no SDK wrapping required
- Unified multi-provider endpoint (100+ models) through a single API key

**Where competitors have the edge:**
- LangSmith: deeper LangChain tracing, dataset management, and prompt versioning; better if you're heavily invested in the LangChain ecosystem
- W&B Weave: GPU monitoring, full ML experiment tracking, native multimodal evaluation — better for teams straddling LLM and classical ML
- OpenLIT: OTel-native with zero-code Kubernetes instrumentation via eBPF; fully free self-hosted on ClickHouse; no acquisition/EOL concern

---

## The Acquisition: What It Means

On March 3, 2026, Mintlify — the documentation tooling company — [acquired Helicone](https://helicone.ai/). Founders Justin Torre and Cole Gottdank joined Mintlify. The stated rationale: integrate Helicone's routing, observability, and caching capabilities into Mintlify's documentation infrastructure.

**For Helicone as a standalone product, this means:**
- **Maintenance mode**: security patches, bug fixes, and new model additions will ship; no new features
- **Experiments feature deprecated**: September 1, 2025 — the A/B prompt testing UI is being removed
- **Migration paths**: Mintlify is working with enterprise customers on transitions; no hard shutdown date announced

This changes the evaluation significantly. Helicone is not end-of-life — the proxy still works, the GitHub repo (Apache 2.0) still accepts contributions, and the Docker image is still current. But a tool in maintenance mode is not one to build a new production dependency on unless you're prepared to self-host and own the maintenance burden.

---

## Weaknesses

- **Maintenance mode / acquired**: the highest-priority concern for new adopters
- **No GPU monitoring**: unlike W&B Weave or OpenLIT, Helicone has no infrastructure-level metrics
- **Tight free tier**: 10k requests/month and 7-day retention limit meaningful evaluation
- **Cloud mode data routing**: all traffic passes through Helicone infrastructure — a data-residency consideration; self-hosting removes this but adds ops burden
- **Experiments deprecated**: the prompt A/B testing feature is gone
- **Alerting is webhook-only**: no native Slack or email notifications on any tier below Team

---

## Who Should Use It

**Consider Helicone if:**
- You need LLM observability *and* a caching/rate-limiting gateway, and want both from a single integration change
- You're self-hosting and want an Apache-licensed tool you control fully
- You're on the Mintlify ecosystem and this becomes an integrated offering

**Look elsewhere if:**
- You need a tool actively developed with a clear product roadmap
- You're building a multi-year production dependency and maintenance mode is unacceptable
- You need prompt A/B testing (deprecated) or GPU monitoring

For greenfield projects starting today, [OpenLIT](/reviews/openlit-llm-observability) is the more defensible choice: fully open-source, actively maintained, OTel-native, and free to self-host. For teams already on Helicone in production, the proxy is stable and self-hosting is viable — there's no urgency to migrate.

---

## Verdict

Helicone built something genuinely useful: the insight that an LLM observability tool could *also be* a production gateway — with caching, rate limiting, and multi-provider routing — and that the integration could be a single URL change. That design philosophy was influential and the execution was solid enough to process 14 trillion tokens across 16,000 organizations.

The Mintlify acquisition is not a product failure, but it does represent an inflection point. For a new project today, choosing a tool in maintenance mode requires a deliberate self-hosting commitment. The Apache 2.0 license and Docker packaging make that viable; whether it's worth the ops overhead compared to actively developed alternatives is a team-by-team call.

**Rating: 3.5/5** — excellent architecture and the right instinct about what LLM observability should include, but the maintenance-mode status makes it hard to recommend unconditionally for new production deployments.

---

*Researched May 2026. Star count, pricing, and feature status reflect data available at that time. Helicone's acquisition by Mintlify was announced March 3, 2026.*

*ChatForest reviews are based on public documentation, GitHub repositories, and web research. We do not have hands-on access to the tools we review.*

