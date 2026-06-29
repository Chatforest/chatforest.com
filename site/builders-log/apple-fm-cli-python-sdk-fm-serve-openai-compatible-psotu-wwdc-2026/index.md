# Apple's `fm` CLI Runs a Local OpenAI-Compatible Server: The PSOTU Details Most WWDC Recaps Skipped

> The June 9 Platforms State of the Union shipped two things most WWDC recaps missed: a Python SDK for Foundation Models and a CLI with an `fm serve` command that runs a Chat Completions-compatible API server on your Mac. Here's what builders need to know.


The WWDC 2026 keynote on June 8 covered the press story: Siri AI, per-category routing, iPhone Fold. The Platforms State of the Union on June 9 covered the developer story, and two announcements in particular are missing from most WWDC recaps.

The first: a Python SDK for Foundation Models — `pip install apple-fm-sdk` — that brings on-device Apple AI to Python scripting on macOS. The second, more significant: `fm serve`, a CLI command that spins up a local Chat Completions-compatible API server backed by the on-device model. That second one matters for every builder who already uses an OpenAI-compatible client.

Part of our **[Builder's Log](/builders-log/)**.

---

## The `fm` CLI

macOS 27 ships with `fm` pre-installed — a command-line interface for the Foundation Models framework. It is not a developer preview. It ships with the OS.

The full command surface:

| Command | What it does |
|---|---|
| `fm respond` | Generate a single response inline or via pipe |
| `fm chat` | Start an interactive session |
| `fm serve` | Start a local Chat Completions API server |
| `fm token-count` | Count tokens for a prompt or instructions |
| `fm schema` | Generate a JSON schema for structured generation |
| `fm available` | Check model availability on the current device |
| `fm quota-usage` | Check quota usage |

Key flags across commands:
- `--model system` (default, on-device Neural Engine)
- `--model pcc` (Private Cloud Compute)
- `--stream` — streaming output
- `--instructions` — system instructions

### `fm respond` for scripting

The scripting use case is immediate. Pipelines that currently call an external API can redirect to the local model:

```bash
fm respond 'Summarize the following:' < report.txt
cat changelog.md | fm respond 'Extract the breaking changes'
fm respond --stream --instructions 'You are a release note writer' 'Summarize these commits'
```

No API key. No network. No cost. The latency is hardware-bound, not network-bound.

### `fm serve`: the one that matters most

`fm serve` starts a local HTTP server that speaks the Chat Completions API format. Any client already compatible with OpenAI's API — including every major LLM framework, most agent scaffolds, and every tool built on the Chat Completions spec — can point at this server and use the on-device model without modification.

```bash
fm serve --model system --stream
```

This means:

- **LangChain, LlamaIndex, or any OpenAI-compatible client:** change the `base_url` to `http://localhost:PORT`, set `model` to `apple/foundation-models`, no other changes
- **Cursor, VS Code extensions, or any IDE tool that supports local inference:** can use the on-device model as a provider
- **Agent scaffolds:** can route tasks to on-device Apple Intelligence via the same interface used for GPT-5 or Claude

The model is a 20B parameter sparse architecture (Apple Foundation Model 3, AFM 3) with 1–4B active parameters per prompt, using Instruction-Following Pruning. Full weights in flash, shared experts in DRAM. For comparison benchmarks: AFM 3 outperforms 9B dense models on math and coding tasks at a fraction of the active-parameter cost.

The practical implication: `fm serve` makes AFM 3 a drop-in local inference option for any existing OpenAI-compatible workflow on a Mac with an M-series chip.

---

## The Python SDK

The Python SDK ships separately from the CLI and covers scripting and data processing workflows.

**Install:** `pip install apple-fm-sdk`  
**Python:** 3.10+  
**Platform:** macOS 26.0+ only  
**GitHub:** [apple/python-apple-fm-sdk](https://github.com/apple/python-apple-fm-sdk)  
**License:** Apache-2.0  

Note: the Python SDK does **not** run on Linux. The foundation for Linux support is in Swift — server-side Swift applications can use the Foundation Models framework on Linux via Swift's open-source runtime. The Python package is macOS-only.

### Basic usage

```python
import apple_fm_sdk as fm
import asyncio

async def main():
    model = fm.SystemLanguageModel()
    available, reason = model.is_available()
    if not available:
        print(f"Model unavailable: {reason}")
        return

    session = fm.LanguageModelSession(
        instructions="You are a helpful assistant",
        model=model
    )
    response = await session.respond("Summarize the key risks in this contract.")
    print(response)

asyncio.run(main())
```

### Image input (v0.2.0+)

```python
image = fm.ImageAttachment(path=image_path)
response = await session.respond(["Identify the components in this diagram:", image])
```

### Error types to handle

- `ExceededContextWindowSizeError`
- `GuardrailViolationError`
- `AssetsUnavailableError`
- `GenerationError`

### Current limitations

The Python SDK does **not** expose streaming, tool calling, or guided generation — these are Swift-framework capabilities not yet surfaced in the Python layer. For those features, use the `fm serve` approach with an OpenAI-compatible client that handles streaming natively, or use the Swift framework directly.

Apple's repo states it is not currently accepting contributions.

---

## Private Cloud Compute: Free for Small Developers

PCC — Private Cloud Compute, Apple's server-side inference infrastructure — is now free for developers who qualify for the **App Store Small Business Program**: fewer than 2 million first-time App Store downloads, enrolled in the program.

Both the `fm` CLI and the Python SDK can target PCC:

```bash
fm respond --model pcc 'Your prompt here'
```

```python
model = fm.SystemLanguageModel(backend="pcc")  # exact parameter name may vary
```

If a developer exceeds the 2 million download threshold, Apple provides a 6-month migration window before access is removed. Same window applies if you leave the Small Business Program.

No rate limits or token quotas for the free tier were announced at PSOTU.

This closes a meaningful gap for indie developers: previously, deploying Apple Intelligence features that required the cloud path (longer context, heavier processing) had no clear free tier. Now it does, for the developers most likely to be building early experiments.

---

## Foundation Models Open Source

Apple open-sourced the Foundation Models framework utilities package at PSOTU — covering transcript management, the skill API, and Chat Completions interfacing. The Python SDK repo is already live under Apache-2.0.

Timeline for the full open-source release: "later this summer." No specific date.

Important scope clarification: the model weights are **not** being open-sourced. The open-source commitment covers the framework code — the glue, the APIs, the utilities — not AFM 3 itself.

---

## What This Changes for Builders

**If you use OpenAI-compatible clients:** `fm serve` makes the on-device Apple model available to your existing tooling with a URL change. Try it on tasks where latency, privacy, or API cost matters — build summaries, local extraction, document processing where the data shouldn't leave the machine.

**If you write Python automation on macOS:** `apple-fm-sdk` gives you Foundation Models access without Swift. No new language, no Xcode required. Useful for scripting workflows, CI pipelines on Apple silicon, local ML preprocessing.

**If you deploy server-side Swift:** Foundation Models framework now runs on Linux via Swift's open-source runtime. Apple AI in your backend, without macOS.

**If you're in the Small Business Program:** free PCC access is available now. Call `--model pcc` in the CLI or set the backend parameter in the SDK. Check your download count.

---

## What's Already Covered Elsewhere

Two things from PSOTU are covered in separate articles and not repeated here:

- The **Universal LanguageModel protocol in Swift** — write once, swap between Apple FM, Claude, and Gemini without code changes — is covered in our article on [Anthropic's Claude Swift package for Apple's Foundation Models protocol](/builders-log/claude-foundation-models-swift-ios27-language-model-protocol-provider-guide/)
- The **complete Foundation Models Swift API** — structured outputs, tool calling, fine-tuning, multimodal — is in our [Foundation Models iOS 27 builder guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/)

The CLI, Python SDK, `fm serve`, and PCC free tier are what the June 9 PSOTU added beyond the keynote.

