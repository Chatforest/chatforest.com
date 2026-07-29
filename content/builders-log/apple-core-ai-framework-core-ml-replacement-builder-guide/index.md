---
title: "Apple Core AI: What the Core ML Replacement Means for Builders (WWDC 2026)"
date: 2026-06-08
description: "WWDC 2026 confirmed Core AI, Apple's new on-device model deployment framework and the practical successor to Core ML for custom generative models. It is a separate framework from Foundation Models, which is where Apple's own on-device model and third-party LLM integration actually live. Here is what builders need to know about the split, the migration path, and what each framework is actually for."
og_description: "Core ML is being replaced for generative workloads. Apple's Core AI framework — announced at WWDC 2026 — is the new on-device model deployment layer for iOS 27 and macOS 27. It's a different framework from Foundation Models, which handles LLM sessions and third-party model integration. Here's the builder guide."
content_type: "Builder's Log"
categories: ["Apple", "On-Device AI", "Developer Tools", "Platform Strategy"]
tags: ["core-ai", "core-ml", "apple", "ios-27", "macos-27", "wwdc-2026", "foundation-models", "on-device-ai", "swift", "neural-engine", "third-party-models", "migration", "builder-guide"]
sources_audited: 2026-07-29
---

[Apple introduced Core AI at WWDC 2026](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/), describing it as ["a brand-new framework designed to be the best way to run models on device."](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/) It takes over Core ML's role — [the machine learning framework that has shipped with iOS and macOS since 2017](https://9to5mac.com/2026/03/01/apple-replacing-core-ml-with-modernized-core-ai-framework-for-ios-27-at-wwdc/) — for developers deploying their own custom generative models on-device. Apple's own [Core AI developer documentation](https://developer.apple.com/documentation/coreai) and the ["Meet Core AI"](https://developer.apple.com/videos/play/wwdc2026/324/) WWDC session are the primary references for what follows.

Core AI is not a rename. It is a [rearchitected framework designed for generative AI workloads](https://www.infoq.com/news/2026/06/apple-core-ai-wwdc/) — a modern Swift API plus a Python conversion toolchain for bringing your own model weights on-device, [built to scale from small models up to a 70-billion-parameter LLM](https://developer.apple.com/videos/play/wwdc2026/324/) across the CPU, GPU, and Neural Engine. Core ML was built for traditional inference: CNNs, image classifiers, regressors, structured tabular models. Core AI is built for the kind of generative on-device AI developers are actually shipping in 2026. **Note on scope, corrected in this audit:** an earlier version of this guide described Core AI as an umbrella that also contained Apple's own assistant model, third-party LLM routing, and MCP tool-calling. Apple's own Core AI documentation and WWDC session describe none of that — those capabilities belong to a separate, related framework, Foundation Models, covered below. We've rewritten the relevant sections to match Apple's primary sources rather than the earlier, broader claim.

Both frameworks coexist in the SDK for now. Core ML is not deprecated. But the signal from Apple is clear: new generative AI integrations belong in Core AI. Part of our **[Builder's Log](/builders-log/)**.

---

## What Core ML Did (and Where It Stopped)

Core ML shipped in 2017. Its job was to take a trained model — a `.mlmodel` file — and run inference on-device using the Neural Engine, GPU, or CPU. It was excellent for the models of its era: MobileNet, SqueezeNet, image classifiers, depth estimation, pose detection.

The Core ML workflow:
1. Convert a model to `.mlmodel` format (via coremltools)
2. Add the file to your Xcode project
3. Call the generated Swift class with your input
4. Read the prediction output

This worked well for traditional ML. It did not work well for generative AI:

- **No concept of sessions or multi-turn context.** Core ML ran one inference at a time. Building a multi-turn conversation required re-concatenating context manually every request.
- **No streaming output.** Core ML returned a complete prediction. Token-by-token streaming — the expected UX for any text generation feature — required custom infrastructure layered on top.
- **No structured output schema.** Getting an LLM to return valid JSON required prompt engineering or post-processing, not a framework primitive.
- **No tool calling.** Core ML could not express the concept of calling a function mid-inference.
- **`.mlmodel` format friction for LLMs.** Converting a modern LLM to `.mlmodel` was nontrivial. The format was designed for CNNs, not transformer architectures with hundreds of billions of parameters in mixture-of-experts configurations.

Apple developers who wanted to ship generative AI features in 2024–2025 had two choices: call the Foundation Models API (Apple's own model, no customization) or call an external API (OpenAI, Anthropic, Google) and ship no on-device capability. Core AI is Apple's answer to the middle ground.

---

## What Core AI Actually Is

Per Apple's own ["Meet Core AI" session](https://developer.apple.com/videos/play/wwdc2026/324/), Core AI is ["the inference framework powering on-device Apple Intelligence"](https://developer.apple.com/videos/play/wwdc2026/324/), now opened up for third-party developers. It shipped as part of the iOS 27 and macOS 27 SDK, announced at WWDC 2026. Its job is on-device model deployment: converting a model you own, loading it, and running inference against it — locally, "with no server and no cost per token."

The workflow, as demonstrated in Apple's sessions:

1. Convert a model (for example, from PyTorch via `torch.export`) to Apple's `.aimodel` format using the new `coreai-torch` Python package.
2. Load it in Swift with the `AIModel` type.
3. Get a runnable `InferenceFunction` from it.
4. Pass data in and out via `NDArray`, calling `InferenceFunction.run()`.

This is confirmed directly in ["Meet Core AI,"](https://developer.apple.com/videos/play/wwdc2026/324/) with companion sessions on the same API surface: [Dive into Core AI model authoring and optimization](https://developer.apple.com/videos/play/wwdc2026/325/) (custom Metal kernels, compression strategies) and [Integrate on-device AI models into your app using Core AI](https://developer.apple.com/videos/play/wwdc2026/326/).

**This is a narrower job than an earlier version of this guide described.** Core AI is not an umbrella containing Apple's own assistant model, third-party LLM routing, and MCP tool-calling — Apple's own documentation and session content describe none of a three-tier hierarchy, an `AISession` type, or MCP integration inside Core AI. Those pieces belong to a different, related framework: Foundation Models.

### Foundation Models: where LLM sessions and third-party models actually live

Multi-turn context, streaming output, structured output via `@Generable`, and tool calling are [Foundation Models framework](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/) features, not Core AI features. Foundation Models predates WWDC 2026 (it shipped with iOS 26) and was expanded this year: per Apple's newsroom announcement, it ["now serves as a single native Swift API that supports more powerful on-device models with image input, support for server models, and the ability to build custom skills,"](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/) and developers can "leverage models of their choice, like Claude and Gemini."

The mechanism, per the WWDC session ["Bring an LLM provider to the Foundation Models framework,"](https://developer.apple.com/videos/play/wwdc2026/339/) is a public `LanguageModel` protocol: ["Anthropic and Google will soon extend the Foundation Models framework with Swift packages of their own, making state-of-the-art Claude and Gemini models available to all Swift developers."](https://developer.apple.com/videos/play/wwdc2026/339/) A developer picks a model explicitly in code — Apple's own on-device model, a Private Cloud Compute model, or (once a provider's package ships) a third-party model — and passes it into a `LanguageModelSession`.

**Correction to an earlier draft of this guide:** we previously claimed builders "do not manage API keys for Claude, ChatGPT, or Gemini" if they used a Core AI "Extension" tier. That is contradicted by Apple's own session, which walks through developers managing provider API keys/tokens directly and recommends [Keychain-backed storage or a sign-in flow](https://developer.apple.com/videos/play/wwdc2026/339/) rather than hardcoding them — the opposite of "the user's Extension handles that." We've removed the claim.

Separately, Apple is also letting users choose a third-party AI provider (reported to include Claude, ChatGPT, and Gemini) for **Siri, Writing Tools, and Image Playground** specifically — a system-feature-level setting, not a general-purpose routing API third-party apps can call into. We could not find an Apple newsroom post, developer-documentation page, or WWDC session describing this in Apple's own words — only secondary reporting — so we're not presenting it here as a builder-facing API. If your app needs an "any provider" architecture on iOS 27, the confirmed path is the Foundation Models `LanguageModel` protocol above, where you supply and manage your own provider credentials.

### Custom imported models

For model needs Apple's own model and Foundation Models' third-party providers don't cover, Core AI's `.aimodel` / `AIModel` / `InferenceFunction` pipeline (above) is the actual replacement for the old `.mlmodel` conversion workflow on generative workloads. Existing `.mlmodel` files continue to work through Core ML, which Apple has not deprecated.

This path fits regulated-industry apps with specialized vocabulary, apps requiring model behavior guarantees not achievable through prompting alone, and apps where data-residency requirements rule out any provider whose inference runs off-device.

---

## MCP: What's Confirmed and What Isn't

An earlier version of this guide claimed Core AI treats MCP servers as a "fourth integration point" that apps can declare as tool targets. We could not find that claim in Apple's Core AI documentation, the "Meet Core AI" session, or the WWDC 2026 newsroom post, so we're removing it rather than repeating it uncited. What WWDC 2026 did confirm is MCP support in **Xcode 27** for development tooling — an `mcpbridge` component that lets MCP-compliant agents connect to the IDE — which is a developer-tooling feature, not a documented Core AI runtime capability for shipping apps. See the **[iOS 27 system-wide MCP guide](/builders-log/apple-ios-27-mcp-system-wide-siri-core-ai-builder-guide/)** for what's confirmed about MCP elsewhere on Apple's platforms.

---

## Core ML vs. Core AI: When to Use Which

Both frameworks are in the SDK. Apple has not deprecated Core ML. The practical decision tree:

| Your use case | Framework |
|---|---|
| Traditional ML: image classifier, regression, tabular prediction | Core ML |
| Custom model converted from PyTorch/ONNX for non-generative tasks | Core ML |
| On-device text generation using Apple's system model | Foundation Models (`SystemLanguageModel`) |
| Integrating a specific third-party model (Claude, Gemini) you configure yourself | Foundation Models (provider Swift package + your API credentials) |
| Streaming text output with a multi-turn session, or structured (`@Generable`) output | Foundation Models (`LanguageModelSession`) |
| Custom LLM with your own weights not covered by Apple's or a provider's model | Core AI (`AIModel` / `InferenceFunction`) |

Do not migrate Core ML classification or detection models to Core AI unless there is a specific reason — Core AI's toolchain and format target generative, transformer-style workloads, and re-converting a classifier or detector isn't justified for workloads Core ML already handles well.

---

## Migration Path from Core ML (for Generative Workloads)

If you are currently running a custom LLM via Core ML (`.mlmodel` conversion of a transformer model), Core AI is the cleaner path forward for the deployment side. For anything session-based — multi-turn context, streaming, structured output — you're moving to the Foundation Models framework, not Core AI, whether or not the underlying model is Apple's or your own.

Migration steps, based on the API surface confirmed in [Apple's "Meet Core AI" and "Dive into Core AI model authoring and optimization"](https://developer.apple.com/videos/play/wwdc2026/324/) sessions:

1. **Audit your Core ML generative workloads.** Identify which `.mlmodel` files are generative (text output) versus discriminative (classification, detection).

2. **For generative models:** Re-export from source (for example, PyTorch via `torch.export`) using the new `coreai-torch` Python package, which converts to Apple's `.aimodel` format — this is a new tool, not an extension of the existing `coremltools`.

3. **For existing discriminative models:** No migration needed. Core ML continues to handle these; Apple has not announced a deprecation timeline.

4. **Session management, streaming, structured output:** These are Foundation Models features (`LanguageModelSession`, `@Generable`), not Core AI features. If your generative workload needs them, plan around the Foundation Models API — see the **[Foundation Models builder guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/)** — rather than expecting Core AI to provide a session layer. Core AI's confirmed API surface is lower-level: `AIModel`, `InferenceFunction`, and `NDArray` for direct tensor in/out.

5. **Test on device.** Use Xcode's tooling for your generative-model workflow; see the **[Xcode 17 builder guide](/builders-log/xcode-17-ai-builder-guide-swift-assist-foundation-models-playground/)** for what's confirmed there. We removed a claim from an earlier draft that the Foundation Models Playground specifically validates Core AI custom models — we could not verify that detail against a primary source.

---

## Privacy Model

Privacy characteristics depend on which framework and which model you're using — not on a single "Core AI privacy tier," which an earlier draft of this guide incorrectly implied:

**Core AI (your own custom model):** [Inference runs entirely on-device](https://developer.apple.com/videos/play/wwdc2026/324/), on the CPU, GPU, or Neural Engine, "with no server and no cost per token." Privacy characteristics beyond that depend on what your own model and app code do with the data — Apple's infrastructure isn't in the loop.

**Foundation Models — Apple's system model:** Also on-device by default.

**Foundation Models — a third-party provider (Claude, Gemini, etc.):** Once a provider's Swift package ships and you integrate it, requests go to that provider's servers under whatever terms and credentials you configure — this is a standard third-party API integration from a privacy standpoint, not an on-device-private path. Disclose this to your users accordingly.

We removed a claim from an earlier draft about an `Info.plist` key for declaring "Extension capabilities" — we could not find this documented by Apple and are not confident it describes anything real.

---

## What Builders Should Do Now

**If you have existing Core ML generative workloads:** Plan a Core AI migration for the model-deployment side. The [`coreai-torch` conversion path](https://developer.apple.com/videos/play/wwdc2026/324/) directly addresses the `.mlmodel` limitations for transformer models. ["Meet Core AI"](https://developer.apple.com/videos/play/wwdc2026/324/) is the starting point.

**If you are building a new AI feature today:** Start with Apple's own model via Foundation Models (`SystemLanguageModel`) — on-device, no per-token cost. Reach for Core AI only if you have custom weights Apple's model or a provider's Swift package doesn't cover.

**If you want to offer third-party model choice:** Use the Foundation Models `LanguageModel` protocol and [providers' Swift packages as they ship](https://developer.apple.com/videos/play/wwdc2026/339/), and manage your own credentials as Apple's session recommends (Keychain-backed token storage or a sign-in flow). We removed an earlier claim that a "Tier 2 Extension" routing layer would handle this for you — we could not verify that such an app-facing routing API exists.

---

## What Is Not Known Yet

At the time this guide was first published (June 8, WWDC keynote day), full technical documentation for Core AI had not yet appeared on developer.apple.com. This audit pass (July 2026) confirms the sessions have since aired and [Core AI documentation is live](https://developer.apple.com/documentation/coreai). Still open: exact `.aimodel` format spec details, Core ML deprecation timeline (not announced), and the final shape of any Foundation Models third-party provider packages from Anthropic and Google, which [Apple said were coming "soon"](https://developer.apple.com/videos/play/wwdc2026/339/) but had not shipped as of this session.

The real sessions to watch, corrected from an earlier draft that listed titles which don't match Apple's actual program:
- ["Meet Core AI"](https://developer.apple.com/videos/play/wwdc2026/324/) (framework overview)
- ["Dive into Core AI model authoring and optimization"](https://developer.apple.com/videos/play/wwdc2026/325/) (custom model authoring, compression)
- ["Integrate on-device AI models into your app using Core AI"](https://developer.apple.com/videos/play/wwdc2026/326/) (app integration)
- ["Bring an LLM provider to the Foundation Models framework"](https://developer.apple.com/videos/play/wwdc2026/339/) (third-party model integration — this is a Foundation Models session, not a Core AI session)

Builders running existing Core ML integrations have time: Core ML ships in iOS 27 and the migration is not mandatory this cycle. The deprecation timeline is not announced.

---

## The Bigger Picture

Core ML was designed for a world where ML meant classifiers and CNNs. Core AI, narrowly, gives custom-model developers a modern replacement for that specific job — generative-model conversion and on-device deployment, not the whole AI story.

The more strategically significant piece, per Apple's own account, is the [Foundation Models `LanguageModel` protocol opening up to third-party providers](https://developer.apple.com/videos/play/wwdc2026/339/): ["Anthropic and Google will soon extend the Foundation Models framework with Swift packages of their own, making state-of-the-art Claude and Gemini models available to all Swift developers."](https://developer.apple.com/videos/play/wwdc2026/339/) That's a real, sourced, significant shift for builders who want multi-provider support without hand-rolling every client — even though, per the same session, you still manage your own credentials for whichever provider you add.

For builders: the practical move on iOS 27 is Foundation Models for anything session-based (Apple's model or a provider's, once its package ships) and Core AI only for custom weights nothing else covers. We're not asserting a bigger "Extension economy" narrative here — an earlier draft did, based on a routing architecture we could not verify against Apple's own sources.
