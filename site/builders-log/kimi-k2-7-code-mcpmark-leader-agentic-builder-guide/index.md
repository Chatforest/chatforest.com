# Kimi K2.7 Code Tops MCPMark Over Claude Opus, Drops 30% of Thinking Tokens — Builder Setup Guide

> Moonshot AI released Kimi K2.7 Code on June 12, 2026. It beats Claude Opus 4.8 on MCPMark tool use (81.1% vs 76.4%), uses 30% fewer thinking tokens than K2.6, and drops into Claude Code via an Anthropic-compatible endpoint. Builder setup guide and K2.6 migration notes.


[Moonshot AI released Kimi K2.7 Code on June 12, 2026](https://www.kimi.com/resources/kimi-k2-7-code) — the latest release in the K2 line, following [K2 (July 2025)](https://huggingface.co/moonshotai/Kimi-K2), [K2.5 (January 2026), and K2.6 (April 2026)](https://huggingface.co/moonshotai/Kimi-K2.6). It is a coding-focused upgrade to K2.6 with two headline changes: [it beats Claude Opus 4.8 on MCPMark](https://huggingface.co/moonshotai/Kimi-K2.7-Code) (the MCP tool-calling benchmark), and it uses [30% fewer thinking tokens than K2.6](https://huggingface.co/moonshotai/Kimi-K2.7-Code) while scoring higher on the coding benchmarks Moonshot tracks. It also introduces [an Anthropic-compatible API endpoint](https://platform.kimi.ai/docs/guide/claude-code-kimi), which means K2.7 Code can run inside [Claude Code, Cline, and RooCode](https://apidog.com/blog/kimi-k2-7-code-api/) without modification.

The base specs are the same as K2.6: [1 trillion parameters, 32 billion active per token, 256K context](https://huggingface.co/moonshotai/Kimi-K2.7-Code), [Modified MIT license](https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE). Part of the **[Builder's Log](/builders-log/)**.

> **Update (2026-08-23):** Moonshot released [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) on July 16, 2026 — a separate, larger 2.8T-parameter, 1M-context model — and it has since taken the top spot on MCPMark Verified: [Moonshot's own K3 model card](https://huggingface.co/moonshotai/Kimi-K3) reports 94.5%, and the live third-party [MCPMark Verified leaderboard](https://mcpmark.ai/leaderboard/verified) shows K3 at 96.06%, both well ahead of K2.7 Code's 81.1%–81.89%. GPT-5.5 and GPT-5.6-sol (~92.9% each) and Claude Fable 5 (86.6%) also now outscore K2.7 Code on the live leaderboard. Moonshot's own [Claude Code integration guide](https://platform.kimi.ai/docs/guide/claude-code-kimi) has been updated to default `ANTHROPIC_MODEL` to `kimi-k3` rather than `kimi-k2.7-code`. K2.7 Code is still available and the setup steps below still work, but it is no longer Moonshot's top model or the MCPMark leader — see the site's [Kimi K3 builder guide](/builders-log/kimi-k3-2-8t-open-moe-frontier-mcp-atlas-builder-guide/) for the newer model.

---

## What Changed from K2.6

K2.7 is not a new architecture — it is a refined fine-tune of K2.6 with a specific target: agentic tool use. [Moonshot describes it](https://huggingface.co/moonshotai/Kimi-K2.7-Code) as strengthening "end-to-end task completion across complex software engineering workflows while improving token efficiency." That is narrow scope by design.

**What is new** ([Moonshot's own benchmark table](https://huggingface.co/moonshotai/Kimi-K2.7-Code), corroborated independently by [MarkTechPost](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/)):

| Change | K2.6 | K2.7 Code |
|---|---|---|
| Thinking token usage | Baseline | ~30% lower |
| MCPMark Verified score | 72.8% | **81.1%** |
| Kimi Code Bench v2 | 50.9 | **62.0** (+21.8%) |
| Program Bench | 48.3 | 53.6 (+11.0%) |
| MLS Bench Lite | 26.7 | 35.1 (+31.5%) |
| preserve_thinking mode | Optional (`thinking.keep`) | [Mandatory — always on, cannot be disabled](https://platform.kimi.ai/docs/guide/use-kimi-k2-thinking-model) |
| Anthropic-compatible API | Not available | [Available](https://platform.kimi.ai/docs/guide/claude-code-kimi) |

**What did not change:** [architecture (1T MoE, 32B active, 384 experts, MLA), context window (256K)](https://huggingface.co/moonshotai/Kimi-K2.7-Code), [pricing ($0.95 input / $4.00 output per M tokens)](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/), native INT4 quantization, HuggingFace weights under [Modified MIT](https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE).

---

## Benchmark Position

### MCPMark — the headline number

[MCPMark](https://mcpmark.ai) tests how well a model invokes tools via the Model Context Protocol — Moonshot describes it as "a comprehensive, stress-testing MCP benchmark and a collection of diverse, verifiable tasks designed to evaluate model and agent capabilities in real-world MCP use." It is one of the more direct third-party proxies for performance in the agentic loops builders actually run.

**MCPMark Verified scores (June 2026):**

| Model | MCPMark | Type |
|---|---|---|
| **Kimi K2.7 Code** | **81.1%** | Open-weight |
| Claude Opus 4.8 | 76.4% | Proprietary |
| Kimi K2.6 | 72.8% | Open-weight |

Source: [Moonshot's Kimi K2.7 Code model card](https://huggingface.co/moonshotai/Kimi-K2.7-Code), corroborated independently by [MarkTechPost's benchmark table](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/).

**This was the state of the leaderboard at K2.7 Code's June 12, 2026 launch.** As of this update, K2.7 Code has fallen to 5th place on the live [MCPMark Verified leaderboard](https://mcpmark.ai/leaderboard/verified): [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) leads at 96.06% (94.5% on Moonshot's own K3 model card), followed by GPT-5.5 and GPT-5.6-sol (~92.9% each) and Claude Fable 5 (86.6%). K2.7 Code (81.1%–81.89%) still beats Claude Opus 4.8 (76.4%), which is the comparison this article was written around, but it is no longer the overall MCPMark leader.

K2.7 Code's 4.7-point margin over Claude Opus 4.8 on MCPMark is not noise. Anthropic's flagship proprietary model is the current standard for agentic coding quality; K2.7 beating it on this tool-use-specific benchmark while costing [roughly 5x less per million input tokens ($0.95 vs. $5.00 standard-tier)](https://platform.claude.com/docs/en/about-claude/pricing) is a real signal. Worth noting: on Moonshot's own other internal benchmarks (Kimi Code Bench v2, Program Bench, MLS Bench Lite), [Opus 4.8 actually scores higher than K2.7 Code](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/) — MCPMark is the one benchmark in this set where K2.7 leads.

**Caveat:** MCPMark performance does not directly predict SWE-Bench Verified. On SWE-Bench Verified, [K2.6 scored 80.2%](https://huggingface.co/moonshotai/Kimi-K2.6); K2.7-specific SWE-Bench numbers are not published on [Moonshot's own K2.7 model card](https://huggingface.co/moonshotai/Kimi-K2.7-Code) or by independent evaluators as of this writing. Expect results in the same range until an independent run lands.

### Coding benchmarks

[Moonshot's internal benchmarks](https://huggingface.co/moonshotai/Kimi-K2.7-Code) show larger gains on K2.6-to-K2.7 improvement (not vs. Opus 4.8, which scores higher than K2.7 on these same internal benchmarks — see above):

- **Kimi Code Bench v2**: 50.9 → 62.0, a 21.8% relative improvement. This benchmark measures full agentic software engineering sessions — plan → implement → test → debug cycles — on real repositories.
- **Program Bench**: 48.3 → 53.6, +11.0% vs K2.6 on structured programming tasks.
- **MLS Bench Lite**: 26.7 → 35.1, +31.5%, which covers multi-language synthesis tasks.

These are Moonshot's own benchmarks, not third-party evaluations. Treat them as directional rather than definitive, but the MCPMark result is third-party and replicable.

---

## Thinking Tokens and preserve_thinking Mode

K2.6 uses extended thinking for hard multi-step problems, and lets callers control it (thinking can be toggled, and whether reasoning is preserved across turns is an optional `thinking.keep` setting). K2.7 changes this: [Moonshot's own reasoning-model guide](https://platform.kimi.ai/docs/guide/use-kimi-k2-thinking-model) states that for `kimi-k2.7-code`, thinking is always on — passing `thinking.type: "disabled"` returns an error — and preserved thinking is "always on and cannot be turned off": omitting `thinking.keep` or passing `"all"` is the only valid state.

**30% fewer thinking tokens**: [Moonshot reports](https://huggingface.co/moonshotai/Kimi-K2.7-Code) that K2.7 "cuts thinking-token usage by approximately 30% on average compared with K2.6." For high-volume coding pipelines running thousands of sessions per day, that is a real cost reduction on the reasoning-token share of a bill, without a change to input/output token pricing (see Pricing section below).

**Preserved thinking** means the model's full reasoning content carries across multi-turn interactions rather than being re-derived from scratch. In practice: when your agent calls a tool, gets a result, and calls another tool in the next turn, K2.7 keeps the reasoning chain from the prior turn as part of context. [Moonshot's model card](https://huggingface.co/moonshotai/Kimi-K2.7-Code) says this "enhances performance in coding agent scenarios." Per [Moonshot's docs](https://platform.kimi.ai/docs/guide/use-kimi-k2-thinking-model), the mechanic is simple: keep each turn's `reasoning_content` in the message history you send back on the next turn, unmodified — the API does no extra work to preserve it beyond what you pass in.

There is no separate "enable preserve_thinking" flag to set for K2.7 Code the way the earlier code example on this page implied — thinking and its preservation are both forced on for this model. If you are integrating via [Claude Code specifically](https://platform.kimi.ai/docs/guide/claude-code-kimi), note that Claude Code itself does not send an extended-thinking request by default, so you must explicitly turn Thinking on (press `Tab`) in the Claude Code UI, or K2.7 will reject the request with a `400 invalid thinking` error.

---

## API Setup

### OpenAI-compatible endpoint

K2.7 Code is available on the same Moonshot API platform as K2.6, with the new model ID:

```
Base URL:  https://api.moonshot.ai/v1
Model ID:  kimi-k2.7-code
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.ai/v1"
)

response = client.chat.completions.create(
    model="kimi-k2.7-code",
    messages=[
        {"role": "user", "content": "Review this PR diff and list the security concerns."}
    ]
)
```

Tool calling uses the OpenAI format (`tools`, `tool_choice`, `tool_calls`). No schema changes from K2.6 — only the model string changes.

### Anthropic-compatible endpoint (new in K2.7)

K2.7 Code exposes a second endpoint that speaks the Anthropic Messages API spec. Claude Code, Cline, and RooCode all communicate over this spec, which means you can point them at K2.7 with environment variables. Per [Moonshot's own Claude Code integration guide](https://platform.kimi.ai/docs/guide/claude-code-kimi), the auth variable is `ANTHROPIC_AUTH_TOKEN`, not `ANTHROPIC_API_KEY`. Note: as of this update, that same guide now defaults its example `ANTHROPIC_MODEL` to `kimi-k3` rather than `kimi-k2.7-code` — K2.7 Code is still a supported model string, but explicitly set it as shown below rather than assuming it is the default:

```bash
# Linux / macOS
export ANTHROPIC_BASE_URL="https://api.moonshot.ai/anthropic"
export ANTHROPIC_AUTH_TOKEN="YOUR_MOONSHOT_API_KEY"
export ANTHROPIC_MODEL="kimi-k2.7-code"
```

```powershell
# Windows PowerShell
$env:ANTHROPIC_BASE_URL = "https://api.moonshot.ai/anthropic"
$env:ANTHROPIC_AUTH_TOKEN = "YOUR_MOONSHOT_API_KEY"
$env:ANTHROPIC_MODEL = "kimi-k2.7-code"
```

After setting these, launch Claude Code normally. It sends its standard payload — system prompts, conversation history, tool definitions — to Moonshot's endpoint, and K2.7 processes and returns responses that Claude Code reads as native Anthropic responses. File editing, bash execution, codebase analysis, sub-agent spawning all work without modification. Remember from the section above: Claude Code does not enable extended thinking by default, and K2.7 Code requires it — press `Tab` to turn Thinking on, or requests are rejected.

**One known limitation:** [thinking tokens bill as output tokens at K2.7's standard output rate ($4.00/M)](https://lushbinary.com/blog/kimi-k2-7-code-cost-optimization-token-efficiency-guide/), same as any other generated token. The 30% efficiency gain applies to how many reasoning tokens the model generates, not to how they are priced.

---

## Self-Hosting

Weights are on Hugging Face:

```
moonshotai/Kimi-K2.7-Code
```

([model card](https://huggingface.co/moonshotai/Kimi-K2.7-Code)). Serving stacks supported by Moonshot: **vLLM**, **SGLang**, **KTransformers**. The native INT4 quantization ships with the weights.

Exact minimum GPU counts vary by source and quantization/context-length tradeoff (secondary write-ups on running K2.6/K2.7 locally range from 2×A100 to 8×H100/H200 depending on precision and context length), and Moonshot's own model cards do not publish a single official minimum-hardware figure — check the [deployment guide linked from the model card](https://huggingface.co/moonshotai/Kimi-K2.7-Code) and size for your own quantization/context target before provisioning.

K2.7 and K2.6 share the same base architecture (same MLA + MoE design). If you have K2.6 deployment configs, they carry forward — change the weights path and serve.

---

## Pricing

Pricing is unchanged from K2.6:

| Tier | Input | Output | Cached input |
|---|---|---|---|
| [K2.7 Code](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) | $0.95/M | $4.00/M | $0.19/M |
| [Claude Fable 5](https://platform.claude.com/docs/en/about-claude/pricing) | $10.00/M | $50.00/M | $1.00/M |
| [Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/pricing) | $5.00/M | $25.00/M | $0.50/M |

(Claude Opus 4.8 also has a Fast Mode tier at $10/$50 per M tokens; the table above uses standard pricing.)

At the same $0.95/$4.00 price point, the 30% thinking-token reduction means K2.7 is effectively ~6–8% cheaper than K2.6 on thinking-heavy sessions, with no input/output rate change.

**Cost comparison, 50K-token agentic session:**

| Model | Input (50K) | Output (5K) |
|---|---|---|
| Claude Opus 4.8 | $0.25 | $0.13 |
| Claude Fable 5 | $0.50 | $0.25 |
| Kimi K2.7 Code | $0.048 | $0.020 |
| K2.7 cached input | $0.010 | $0.020 |

At [current Anthropic list pricing](https://platform.claude.com/docs/en/about-claude/pricing), K2.7 Code runs roughly 5–6x cheaper than Claude Opus 4.8 and roughly 10–13x cheaper than Claude Fable 5 per million tokens, not a flat "10–15x" across the board — the gap depends on which Claude tier you're comparing against. For high-volume pipelines, that is still a real change to the unit economics of what is viable to automate.

---

## K2.7 vs K2.6: When to Upgrade

Correction from an earlier draft of this piece: K2.7 Code is not text-only. [Its own model card documents image and video input support](https://huggingface.co/moonshotai/Kimi-K2.7-Code) via the same MoonViT vision encoder K2.6 uses (video chat is flagged there as "experimental" and only available through Moonshot's official API, not third-party deployments). If your workload needs vision, K2.7 Code is not automatically ruled out the way a coding-only model would be — verify against your specific inference stack, since third-party servers (vLLM/SGLang) may not yet expose video input.

For coding-focused workloads:

| Scenario | Use |
|---|---|
| Running MCP tool-calling pipelines, want to beat Claude Opus 4.8 specifically | K2.7 Code — 81.1% MCPMark vs Opus 4.8's 76.4% (see update note above: [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) is now the overall MCPMark leader at 94.5–96.06%) |
| High-volume agentic coding at scale | K2.7 Code — 30% less thinking spend |
| Claude Code / Cline drop-in replacement | K2.7 Code — Anthropic-compatible endpoint |
| Multi-turn coding sessions needing reasoning chain continuity | K2.7 Code — preserve_thinking is forced on |
| General reasoning, non-coding tasks | K2.6 or Claude Fable 5 |

---

## Compliance Notes

K2.7 Code is developed and operated by Moonshot AI, a Beijing-based company. The same compliance considerations from K2.6 apply:

- **Kimi API endpoint**: routes through Moonshot's China infrastructure. Not suitable for EU personal data, US government data, or regulated data under data-residency requirements.
- **Self-hosted path**: resolves data-residency concerns entirely — weights are under Modified MIT, no egress.
- **US government / defense contractors**: check your approved vendor list before deploying via API.

---

## Builder Checklist

- [ ] Update model string from `moonshot-v1-k2-6` → `kimi-k2.7-code` (OpenAI endpoint)
- [ ] Set `ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic`, `ANTHROPIC_AUTH_TOKEN=<key>`, and `ANTHROPIC_MODEL=kimi-k2.7-code` to run K2.7 inside Claude Code or Cline — and press `Tab` to enable Thinking in Claude Code, since K2.7 rejects requests without it
- [ ] Do not try to toggle preserve_thinking off — it is forced on for K2.7 Code; just keep each turn's `reasoning_content` in your message history
- [ ] Benchmark your pipeline's MCPMark-style tool calls — K2.7's 81.1% vs K2.6's 72.8% should show up in real-world tool-call reliability
- [ ] If you use image/video input, verify support on your specific inference path — K2.7 Code's model card documents vision support, but video chat is currently official-API-only, not guaranteed on third-party servers
- [ ] Run a cost comparison on your average session's thinking-token ratio to size the 30% efficiency gain in your actual workload

---

**Quick reference:**

- HuggingFace: [`moonshotai/Kimi-K2.7-Code`](https://huggingface.co/moonshotai/Kimi-K2.7-Code)
- API (OpenAI-compatible): `https://api.moonshot.ai/v1`, model `kimi-k2.7-code`
- API ([Anthropic-compatible](https://platform.kimi.ai/docs/guide/claude-code-kimi)): `https://api.moonshot.ai/anthropic` (auth via `ANTHROPIC_AUTH_TOKEN`)
- [Pricing](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/): $0.95 input / $4.00 output / $0.19 cached input (per million tokens)
- Context: [256K tokens](https://huggingface.co/moonshotai/Kimi-K2.7-Code)
- [MCPMark Verified](https://huggingface.co/moonshotai/Kimi-K2.7-Code): 81.1% (vs [Claude Opus 4.8 at 76.4%](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/)) — no longer the overall leader; [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) now tops the [live leaderboard](https://mcpmark.ai/leaderboard/verified) at 94.5–96.06% (see update note above)
- License: [Modified MIT (attribution above 100M MAU or $20M/month revenue)](https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE)
- [Released: June 12, 2026](https://www.kimi.com/resources/kimi-k2-7-code)

