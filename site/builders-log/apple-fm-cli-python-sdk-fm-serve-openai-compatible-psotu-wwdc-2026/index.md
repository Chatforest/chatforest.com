# Apple's `fm` CLI and Python SDK Bring Foundation Models to Your Terminal: What PSOTU Actually Shipped

> The June 9 Platforms State of the Union shipped a Python SDK for Foundation Models and an `fm` command-line tool with chat, respond, and schema subcommands. Here's what's confirmed in Apple's own sessions and docs — and what some recaps got wrong.


The WWDC 2026 keynote on June 8 covered the press story, including a Siri AI overhaul built on Apple Intelligence ([CNBC live coverage](https://www.cnbc.com/2026/06/08/apple-wwdc-2026-live-updates.html)). The Platforms State of the Union (PSOTU) on June 9 covered the developer story, including a Python SDK and command-line tool for Foundation Models that most WWDC recaps skipped ([MacRumors PSOTU recap](https://www.macrumors.com/2026/06/09/apple-outlines-major-ai-and-developer-tool-updates/); [PSOTU session, Apple Developer](https://developer.apple.com/videos/play/wwdc2026/102/)).

The first: a Python SDK for Foundation Models — `pip install apple-fm-sdk` — that brings on-device Apple AI to Python scripting on macOS. The second: `fm`, a CLI that ships with macOS 27 for prompting the on-device model from the terminal. A correction up front: some WWDC coverage (including an earlier draft of this article) described an `fm serve` subcommand that runs a local OpenAI-compatible Chat Completions server. That claim does not appear in Apple's own WWDC26 session dedicated to the `fm` CLI, in Apple's Foundation Models framework news session, in the `python-apple-fm-sdk` repo or docs, or in Apple's developer.apple.com index — see the correction below.

Part of our **[Builder's Log](/builders-log/)**.

---

## The `fm` CLI

macOS 27 ships with `fm` pre-installed — a command-line tool for terminal-based prompting and automation against the Foundation Models framework ([WWDC26 Session 334, "Build AI-powered scripts with the fm CLI and Python SDK"](https://developer.apple.com/videos/play/wwdc2026/334/); independent walkthrough at [Mac O'Clock](https://medium.com/macoclock/apples-fm-is-here-run-apple-foundation-models-from-your-terminal-on-macos-26-no-beta-required-33fa0932f22c)).

The command surface Apple actually demonstrated in that session:

| Command | What it does |
|---|---|
| `fm respond` | Generate a single response inline or via pipe |
| `fm chat` | Start an interactive session (supports `/model` to switch to Private Cloud Compute, `/save` to save a conversation) |
| `fm schema` | Generate a JSON schema for structured generation (e.g. `fm schema object --name ... --string ... --array`) |

Flags confirmed in that session: `--model pcc` (route to Private Cloud Compute instead of the on-device default), `--image <file>` (attach an image to a prompt), `--instructions` (system instructions), `--schema <file.json>` (structured output), and `--help`.

**Correction:** an earlier version of this piece also listed `fm serve`, `fm token-count`, `fm available`, `fm quota-usage`, and a `--stream` CLI flag as part of the shipped command surface. None of those appear in Apple's own session on the `fm` CLI, and a direct search of developer.apple.com turns up nothing for `fm serve`. Third-party developers have since built community wrappers that layer an OpenAI-compatible endpoint on top of the real `fm chat`/`fm respond` commands — for example [`fm-proxy`](https://github.com/gregbarbosa/fm-proxy) and [`apple-to-openai`](https://github.com/ZPVIP/apple-to-openai) — but those are third-party projects, not something Apple shipped. We've cut the fabricated commands rather than publish them as fact.

### `fm respond` for scripting

The scripting use case is real and demonstrated on-camera: piping documents into the model and getting a response back.

```bash
fm respond "Provide a basic regex in Swift to parse an email address"
fm respond "What apps are the user actively using in this screenshot?" --image Screenshot.png --model pcc
```

No API key, no network round-trip for the on-device path — latency is hardware-bound rather than network-bound for `--model system` (the default).

The on-device default is **AFM 3 Core**, a 3-billion-parameter dense model. Apple's larger on-device model, **AFM 3 Core Advanced** (20B parameters, sparse, 1–4B active parameters per prompt via a technique Apple calls Instruction-Following Pruning), is unlocked on Apple's most capable Apple silicon rather than being the universal default ([Apple Machine Learning Research: "Introducing the Third Generation of Apple's Foundation Models"](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models)). `--model pcc` instead routes to the server-side **AFM 3 Cloud** family running on Private Cloud Compute.

---

## The Python SDK

The Python SDK ships separately from the CLI and covers scripting and data-processing workflows.

**Install:** `pip install apple-fm-sdk`
**Python:** 3.10+
**Platform:** macOS 26.0+, Apple silicon
**Xcode:** 26.0+ required (with command-line tools installed and the Xcode/Apple SDKs license accepted) — using it still requires Xcode on the machine, contrary to what an earlier draft of this article claimed
**GitHub:** [apple/python-apple-fm-sdk](https://github.com/apple/python-apple-fm-sdk)
**Docs:** [apple.github.io/python-apple-fm-sdk](https://apple.github.io/python-apple-fm-sdk/getting_started.html)
**License:** Apache-2.0

Note: the Python SDK does **not** run on Linux. The Foundation Models *framework* itself, however, is expanding to Linux separately via a Swift-only utilities package (more below) — that path is Swift, not this Python package ([apple/foundation-models-utilities](https://github.com/apple/foundation-models-utilities)).

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

### What the SDK actually supports

Apple's own session and docs confirm the Python SDK supports **streaming** text generation, **tool calling** (via a `fm.Tool` base class), and **guided generation** with structured output via the `@fm.generable` decorator — the same capability set as the Swift framework, exposed to Python ([WWDC26 Session 334](https://developer.apple.com/videos/play/wwdc2026/334/); [SDK docs](https://apple.github.io/python-apple-fm-sdk/getting_started.html)). An earlier draft of this article claimed the opposite — that streaming, tool calling, and guided generation were *not* yet exposed in Python. That was wrong; it's been corrected.

### Error types to handle

The SDK's `GenerationError` family includes `exceededContextWindowSize`, `guardrailViolation`, and `assetsUnavailable` variants, mirroring the Swift framework's own `LanguageModelSession.GenerationError` cases ([SDK error reference](https://apple.github.io/python-apple-fm-sdk/api/errors.html); [Swift docs](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/generationerror/exceededcontextwindowsize(_:))).

### Contributions

Apple's repo states: "This project is not yet taking contributions."

---

## Private Cloud Compute: Free for Small Developers

Private Cloud Compute (PCC) — Apple's server-side inference infrastructure — is now free, with no cloud API cost, for developers enrolled in the **App Store Small Business Program** with fewer than 2 million first-time App Store downloads across their apps ([developer.apple.com/private-cloud-compute](https://developer.apple.com/private-cloud-compute/); [App Store Small Business Program](https://developer.apple.com/app-store/small-business-program/)).

```bash
fm respond --model pcc 'Your prompt here'
```

If a developer subsequently exceeds the 2-million-download threshold, or leaves the Small Business Program, Apple notifies them and gives a **6-month window** to migrate to an alternative before PCC access is removed ([developer.apple.com/private-cloud-compute](https://developer.apple.com/private-cloud-compute/)). There is no paid tier to fall back to beyond that window — larger developers still pay for PCC access separately.

No rate limits or token quotas for the free tier appear on Apple's PCC page as of this writing.

This closes a meaningful gap for indie developers: previously, deploying Apple Intelligence features that required the cloud path had no clear free tier. Now it does, for developers still under the download threshold.

---

## Foundation Models Open Source

Apple has already open-sourced a **Foundation Models framework utilities package**, `foundation-models-utilities`, under Apache-2.0 — it runs on Apple platforms and select Linux distributions ([apple/foundation-models-utilities](https://github.com/apple/foundation-models-utilities)). It ships a `Skills` API for grouping reusable instructions/tools, history-management modifiers for transcript growth, and a `ChatCompletionsLanguageModel` adapter that lets Swift code call *out to* any server implementing the Chat Completions REST API — a client, not a server Apple hosts.

The **full framework** (not just the utilities package) is targeted for open source "later this summer," per Apple's Foundation Models framework news session — no specific date given ([WWDC26 Session 241, "What's new in the Foundation Models framework"](https://developer.apple.com/videos/play/wwdc2026/241/)). Model weights are **not** part of that commitment — AFM 3 itself stays closed.

---

## What This Changes for Builders

**If you write Python automation on macOS:** `apple-fm-sdk` gives you Foundation Models access — including streaming, tool calling, and guided generation — without writing Swift. You still need Xcode installed to satisfy the SDK's license/toolchain requirement, even though you're writing Python.

**If you script from the shell:** `fm respond` and `fm chat` put the on-device model a terminal command away, with no API key and no per-call network cost.

**If you deploy server-side Swift:** the open-source `foundation-models-utilities` package (Skills API, transcript management, a Chat Completions *client* adapter) already runs on select Linux distributions; the full framework is expected to follow this summer.

**If you're in the Small Business Program:** free PCC access is available now via `--model pcc` in the CLI or the SDK's PCC backend option. Check your download count against the 2-million threshold.

**If you were expecting an Apple-hosted OpenAI-compatible server:** that isn't what Apple shipped. Third-party proxies exist that wrap the real `fm chat`/`fm respond` commands, but treat those as community tooling, not an Apple guarantee.

---

## What's Already Covered Elsewhere

Two things from PSOTU are covered in separate articles and not repeated here:

- The **Universal LanguageModel protocol in Swift** — write once, swap between Apple FM, Claude, and Gemini without code changes — is covered in our article on [Anthropic's Claude Swift package for Apple's Foundation Models protocol](/builders-log/claude-foundation-models-swift-ios27-language-model-protocol-provider-guide/)
- The **complete Foundation Models Swift API** — structured outputs, tool calling, fine-tuning, multimodal — is in our [Foundation Models iOS 27 builder guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/)

The CLI, Python SDK, and PCC free tier are what the June 9 PSOTU added beyond the keynote — verified here against Apple's own sessions, repos, and docs rather than secondary recaps.

