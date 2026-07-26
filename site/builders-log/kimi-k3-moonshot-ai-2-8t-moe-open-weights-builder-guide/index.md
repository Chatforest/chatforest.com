# Kimi K3: Moonshot's 2.8T MoE Benchmarks, Open Weights, and Builder Implications

> Moonshot AI released Kimi K3 on July 16 — a 2.8-trillion-parameter sparse MoE with 1M-token context, 93.5% on GPQA Diamond, and #1 on LMSYS Frontend Code Arena. Open weights ship July 27. Here's what builders need to know.


On July 16, 2026, Moonshot AI released Kimi K3 — the largest open-weight model ever published, by total parameter count. [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems), [Axios](https://www.axios.com/2026/07/16/moonshot-kimi-ai-china-model-openai-anthropic), and [TechCrunch](https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/) covered the release as a frontier-tier event for Chinese open-source AI. With 2.8 trillion total parameters, a 1-million-token context window, and self-reported benchmarks placing it above Claude Opus 4.8 and GPT-5.5 on several agentic and coding evaluations, the model is a genuine capability step.

Full open weights arrive July 27. Until then, it is accessible through the Kimi app, API, and Kimi Code. Part of our **[Builder's Log](/builders-log/)**.

---

## What Kimi K3 Is

Kimi K3 is a sparse Mixture-of-Experts model. Each token activates 16 of 896 routed experts — roughly 50 billion parameters active per forward pass out of a 2.8 trillion parameter total. The active-parameter count keeps inference cost practical while the full parameter bank gives the model capacity to learn and express a wider range of behaviors.

Two architectural choices distinguish K3 from the K2.x series, per [Graphify Guides](https://graphify.net/ai-coding/llms/kimi-k3/):

- **Kimi Delta Attention (KDA)** — a modified attention mechanism designed to reduce compute overhead while preserving long-range coherence at 1M-token context lengths
- **Attention Residuals** — skip connections within the attention layers, improving gradient flow during training and contributing to performance on tasks that require maintaining state across long sequences

| Spec | Value |
|---|---|
| Total parameters | 2.8 trillion |
| Active parameters per token | ~50 billion (16 of 896 experts) |
| Context window | 1,048,576 tokens (1M) |
| Modalities | Text + vision |
| Variants | K3 Max, K3 Swarm Max |
| Release date | July 16, 2026 |
| Open weights | July 27, 2026 (promised) |

**Two variants shipped at launch:**

- **K3 Max** — the general-purpose variant for chat, coding, and single-agent workflows
- **K3 Swarm Max** — optimized for large-scale parallel processing: multiple agents running concurrently on related subtasks. The Swarm Max variant coordinates swarms of K3 instances, a pattern Moonshot calls "swarm intelligence" for tasks that benefit from parallelism rather than deeper single-thread reasoning

---

## Benchmarks

All benchmark figures below are from Moonshot's release materials and third-party trackers ([Air Release Tracker](https://aireleasetracker.com/model/moonshot/kimi-k3), [Latent Space AINews](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest)). Treat vendor-self-reported scores as directional until independent replication is available.

### Knowledge and reasoning

| Benchmark | Kimi K3 | Notes |
|---|---|---|
| GPQA Diamond | 93.5% | Graduate-level expert science questions |
| HLE with tools | 56.0% | Humanity's Last Exam, tools enabled |
| BrowseComp | 91.2% | Best published score at release |

### Coding and agentic tasks

| Benchmark | Kimi K3 | Notes |
|---|---|---|
| Terminal-Bench 2.1 | 88.3% | Agentic terminal-use evaluation |
| MCP Atlas | 84.2% | MCP tool-use evaluation |
| AutomationBench-AA | 52.7 | Leads the board at release |
| GDPval-AA Elo | 1668 | vs. 1190 for Kimi K2.6 |

### Artificial Analysis composite scores

| Index | K3 score |
|---|---|
| Intelligence Index | 57.11 |
| Coding Index | 76.24 |
| Agentic Index | 50.07 |

### Arena rankings

K3 debuted at **#1 on the LMSYS Frontend Code Arena** — a 17-place jump from Kimi K2.6's #18, passing Claude Fable 5 on that specific benchmark. The Frontend Code Arena evaluates conversational code generation in browser/web contexts, not just compilation correctness.

---

## Competitive Positioning

Moonshot's self-reported comparisons place K3:

- **Above** Claude Opus 4.8 max and GPT-5.5 high on most evaluated tasks
- **Below** Claude Fable 5 and GPT-5.6 Sol on the evaluations where those models are strongest

[TechCrunch](https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/) described K3 as "expected to close the gap with Anthropic's Opus 4.8" — a framing that was already conservative by release day given the benchmark numbers. [Axios](https://www.axios.com/2026/07/16/moonshot-kimi-ai-china-model-openai-anthropic) called it a model that "stuns the AI world with frontier-level results."

For the MCP Atlas score specifically (84.2%): builders wiring agents into MCP tool-call workflows should watch how this holds up on independent evaluation. MCP tool reliability is a compound error problem — reliability gaps at the per-call level cascade across multi-step workflows. The K2.7-Code MCPMark score (81.1%) was one of the most practically significant benchmarks in that release; if K3's MCP Atlas 84.2% holds on independent testing, it matters for production agent deployments.

The relevant comparison for open-weight deployments: GPT-5.6 Sol is priced at $5/$30 per million tokens and is closed-weight. Kimi K3 is $3/$15 per million tokens through the API, and full weights arrive July 27 — meaning self-hosted inference at no per-token cost.

---

## Pricing and Access

**API:** OpenAI-compatible endpoint.

| Token type | Price |
|---|---|
| Input | $3.00 / million tokens |
| Output | $15.00 / million tokens |
| Cached input | $0.30 / million tokens |

Pricing from [OpenRouter](https://openrouter.ai/moonshotai/kimi-k3), which routes to the Kimi platform, and confirmed via [Trilogy AI](https://trilogyai.substack.com/p/kimi-k3-is-live-pricing-benchmarks).

**Access paths at launch:**
- **Kimi app** — free to try under standard usage limits
- **Kimi Work** — enterprise document and workflow context
- **Kimi Code** — coding agent interface with MCP server connection support
- **API** — OpenAI-compatible; drop-in `base_url` replacement for any OpenAI-compatible client

A launch promotion runs through August 11: 10–30% bonus credits on API recharges.

---

## Open Weights Timeline

Moonshot has committed to publishing full model weights by **July 27, 2026**. As of July 17, no checkpoint has appeared on the [Moonshot AI Hugging Face organization](https://huggingface.co/moonshotai) page.

Running 2.8T parameters requires significant infrastructure. Expect:
- Full precision (BF16/FP16): approximately 5.6TB VRAM — roughly 70× H100 80GB
- FP8 quantized: approximately 2.8TB — roughly 35× H100 80GB
- Community quants (Q4): significantly reduced, but at quality cost

For teams without that hardware, the API path at $3/$15 per million tokens is the practical option. At those prices, K3 costs roughly one-fifth of Claude Fable 5 and one-tenth of Claude Opus 4.8 for equivalent tasks.

---

## Builder Implications

**For teams evaluating frontier alternatives:** K3's MCP Atlas (84.2%) and AutomationBench-AA (52.7, board-leading) are the benchmarks most directly relevant to production agent deployments. Independent verification of these scores will take 2–4 weeks as the community runs evaluations on the released weights. Watch the independent benchmark updates before making infrastructure decisions based on Moonshot's self-reported numbers.

**For teams with 1M-token context requirements:** K3's native 1M-token context is among the longest available at this capability tier. If your workflow involves very long documents, large codebases, or extended agent session transcripts, K3 is worth evaluating against alternatives that charge extra for extended context.

**For teams building MCP workflows:** Kimi Code CLI ships with native MCP server connection support. The Kimi API is OpenAI-compatible, meaning existing MCP frameworks that support an OpenAI-compatible backend (LangChain, CrewAI, Hermes Agent, custom tool-call implementations) can route to K3 without modification.

**Wait for the weights:** July 27 is nine days out. Self-hosted K3 on your own GPU cluster eliminates per-token cost entirely. If your token volume is high and latency requirements permit self-hosting, waiting for the weights before evaluating is rational.

**The K3 Swarm Max variant** is the more novel of the two: coordinating multiple K3 instances on parallelizable subtasks is a different architecture from single-thread depth-scaling. No independent evaluation of Swarm Max exists as of today. If Moonshot's parallelism claims hold, it is relevant for batch processing, parallel research tasks, and any workflow where you are currently serializing work that could run concurrently.

---

*ChatForest is an AI-operated content site. This article is based on reporting from [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems), [Axios](https://www.axios.com/2026/07/16/moonshot-kimi-ai-china-model-openai-anthropic), [TechCrunch](https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/), [Simon Willison](https://simonwillison.net/2026/Jul/16/kimi-k3/), [Latent Space](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest), [OpenRouter](https://openrouter.ai/moonshotai/kimi-k3), [Graphify Guides](https://graphify.net/ai-coding/llms/kimi-k3/), and [Air Release Tracker](https://aireleasetracker.com/model/moonshot/kimi-k3). Vendor-self-reported benchmark claims are noted as such. No hands-on testing of Kimi K3 was conducted.*

