---
title: "Apple Core AI: What the Core ML Replacement Means for Builders (WWDC 2026)"
date: 2026-06-08
description: "WWDC 2026 confirmed Core AI, Apple's replacement for Core ML. The new framework unifies on-device Foundation Models, third-party LLM integration, and MCP routing under one Swift API. Here is what builders need to know about the shift, the migration path, and what Core AI enables that Core ML never could."
og_description: "Core ML is being replaced. Apple's Core AI framework — announced at WWDC 2026 — is the new on-device AI layer for iOS 27 and macOS 27. It integrates Foundation Models, third-party LLMs, and MCP. Here's the builder guide."
content_type: "Builder's Log"
categories: ["Apple", "On-Device AI", "Developer Tools", "Platform Strategy"]
tags: ["core-ai", "core-ml", "apple", "ios-27", "macos-27", "wwdc-2026", "foundation-models", "on-device-ai", "swift", "neural-engine", "mcp", "third-party-models", "migration", "builder-guide"]
---

Apple introduced Core AI at WWDC 2026. It replaces Core ML — the machine learning framework that has shipped with iOS and macOS since 2017 — as the primary on-device AI integration layer for developers.

Core AI is not a rename. It is a rearchitected framework designed for generative AI workloads, with a different model hierarchy, a new approach to third-party LLM integration, and MCP as a first-class routing target. Core ML was built for traditional inference: CNNs, image classifiers, regressors, structured tabular models. Core AI is built for the kind of AI developers are actually shipping in 2026.

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

## What Core AI Is

Core AI is a framework for on-device generative inference, third-party model integration, and agentic AI workflows. It shipped as part of the iOS 27 and macOS 27 SDK, announced at WWDC 2026.

At the architecture level, Core AI organizes the available models into a three-tier hierarchy:

### Tier 1: Apple Foundation Models

The system LLM maintained by Apple. This is the same model accessible via the existing `FoundationModels` framework. Core AI exposes it through a unified interface alongside third-party models.

For most consumer apps, Tier 1 is the right choice. Zero cost, zero latency from model download, zero privacy exposure. Runs entirely on the Neural Engine. The Foundation Models API (sessions, `@Generable`, tool calling, streaming) is the Tier 1 access path.

See the **[Foundation Models builder guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/)** for the full Swift API reference.

### Tier 2: Third-Party Extension Models

New in iOS 27: users can install an AI Extension that makes a third-party model (Claude, ChatGPT, Gemini, and others) available as a system-level resource. Apps opt in to using the user's chosen Extension.

This is the significant shift. Before iOS 27, third-party AI integrations required each app to implement its own API client — separate API keys, separate billing, separate session management. Under Core AI, the Extension model acts as a system resource. The app asks Core AI for an inference; Core AI routes to the user's installed Extension; the Extension (Claude, ChatGPT, or Gemini) handles the request; the result returns through the Core AI interface.

From the app's perspective, a Tier 2 request looks nearly identical to a Tier 1 request. The routing difference is transparent.

**What this means for builders:**
- You do not manage API keys for Claude, ChatGPT, or Gemini if you use Tier 2. The user's Extension handles that.
- You can offer "use your preferred AI" without implementing separate clients for each provider.
- Users who have a Claude Pro subscription can bring that model into your app without your app paying for API calls.

The security model here is handled by Apple: Extensions are reviewed, sandboxed, and declared in `Info.plist`. Users must explicitly install and grant an Extension before any app can route to it.

### Tier 3: Custom Imported Models

The successor to Core ML's role: bring your own model weights. Core AI supports importing custom models for apps that require specialized capabilities that Apple's Foundation Models and third-party Extensions do not cover.

The format requirements for Tier 3 imports are documented in the WWDC 2026 session "Deploying custom models with Core AI." The coremltools Python package is extended for Core AI format conversion. Existing `.mlmodel` files remain compatible through a bridging layer for non-generative workloads.

Tier 3 is appropriate for regulated-industry apps with specialized vocabulary, apps requiring model behavior guarantees not achievable through prompting, and apps where data-residency requirements prevent any external routing even through on-device Extensions.

---

## MCP as a Routing Target

Core AI treats MCP servers as a fourth integration point alongside the three model tiers. Apps using Core AI can declare MCP server endpoints as tool targets. When the framework routes a request that requires external data or action, it calls registered MCP servers.

This is covered in detail in the **[iOS 27 system-wide MCP guide](/builders-log/apple-ios-27-mcp-system-wide-siri-core-ai-builder-guide/)**. The short version: Core AI can call your MCP server the same way Siri 2.0 can, using the iOS 27 system-level MCP client.

---

## Core ML vs. Core AI: When to Use Which

Both frameworks are in the SDK. Apple has not deprecated Core ML. The practical decision tree:

| Your use case | Framework |
|---|---|
| Traditional ML: image classifier, regression, tabular prediction | Core ML |
| Custom model converted from PyTorch/ONNX for non-generative tasks | Core ML |
| On-device text generation, summarization, extraction | Core AI → Foundation Models (Tier 1) |
| "Use the user's preferred AI assistant" feature | Core AI → Extension (Tier 2) |
| Custom LLM with your own weights for specialized domain | Core AI → Custom Import (Tier 3) |
| Agentic workflows with tool calling and MCP | Core AI |
| Streaming text output with session context | Core AI |

Do not migrate Core ML classification or detection models to Core AI unless there is a specific reason. The bridging layer adds overhead that is not justified for workloads Core ML handles well.

---

## Migration Path from Core ML (for Generative Workloads)

If you are currently running a custom LLM via Core ML (`.mlmodel` conversion of a transformer model), Core AI Tier 3 is the cleaner path forward.

Migration steps as documented in the WWDC 2026 session:

1. **Audit your Core ML generative workloads.** Identify which `.mlmodel` files are generative (text output) versus discriminative (classification, detection).

2. **For generative models:** Re-export from source (PyTorch, MLX, JAX) using the updated `coremltools` with Core AI format support. The Core AI format handles transformer attention patterns more efficiently than the `.mlmodel` container format.

3. **For existing discriminative models:** No migration needed. Core ML handles these. The bridging layer in Core AI allows calling them from Core AI context if needed.

4. **Session management:** Core AI provides `AISession` with built-in multi-turn context. Remove any manual context concatenation logic from your Core ML inference code.

5. **Streaming:** Core AI `AISession` exposes async streaming output. Remove custom streaming wrappers.

6. **Structured output:** Replace prompt-engineered JSON schemas with `@Generable`-style Core AI schema declarations (the syntax mirrors the Foundation Models API).

7. **Test on device.** The Foundation Models Playground in Xcode 17 supports Tier 3 custom models for parameter and schema validation before app integration. See the **[Xcode 17 builder guide](/builders-log/xcode-17-ai-builder-guide-swift-assist-foundation-models-playground/)**.

---

## Privacy Model

Core AI inherits Apple's existing tiered privacy model:

**Tier 1 (Foundation Models):** All inference on-device. No data leaves the device. No logging to Apple servers.

**Tier 2 (Extensions):** Data leaves the device to the Extension provider's servers. This is disclosed to users during Extension installation. Apple requires Extensions to declare their data-handling practices. Your app should surface a disclosure when routing to an Extension for the first time.

**Tier 3 (Custom Import):** All inference on-device (same as Tier 1). Privacy characteristics depend on your model's data requirements, not Apple's infrastructure.

Apps that route to Extensions must add a key to `Info.plist` declaring which Extension capabilities they request. This surfaces in App Review and in the user-facing app privacy disclosure.

---

## What Builders Should Do Now

**If you have existing Core ML generative workloads:** Plan a Core AI migration. The Tier 3 import path directly addresses the `.mlmodel` limitations for transformer models. The WWDC 2026 session "Deploying custom models with Core AI" is the starting point.

**If you are building a new AI feature today:** Start with Core AI and Foundation Models (Tier 1). Avoid external API integration unless Foundation Models cannot cover your use case — the privacy and cost story for Tier 1 is significantly better.

**If you want to offer third-party model choice:** Tier 2 Extension routing is now the right architecture. Implementing your own Claude/ChatGPT/Gemini clients in-app is the wrong pattern on iOS 27 and macOS 27 for consumer applications.

**If you operate an MCP server:** Register it as a Core AI tool target. MCP server operators now have direct exposure to on-device agent workflows — not just developers using Claude Desktop or Zed.

---

## What Is Not Known Yet

The WWDC 2026 sessions were announced June 8 (today). Technical documentation for Core AI has not yet appeared in full on developer.apple.com. Specific API surface details — class names, method signatures beyond what was shown in sessions, exact Tier 3 model format spec — will fill in as sessions release and the iOS 27 beta developer documentation is published.

The sessions to watch:
- "Meet Core AI" (framework overview)
- "Deploying custom models with Core AI" (Tier 3 import)
- "Integrate third-party AI extensions" (Tier 2 routing)
- "MCP in Apple platforms" (MCP tool registration)

Builders running existing Core ML integrations have time: Core ML ships in iOS 27 and the migration is not mandatory this cycle. The deprecation timeline is not announced.

---

## The Bigger Picture

Core ML was designed for a world where ML meant classifiers and CNNs. Apple was right to retire it as the primary developer surface. Core AI reflects what AI actually means in 2026 — generative, multi-turn, multi-model, agentic.

The Extension model is the most strategically significant piece. It inverts the current integration pattern: instead of every app implementing separate API clients for every AI provider, iOS becomes the routing layer. Apple decides which Extensions are trustworthy. Users choose their model. Apps focus on product logic.

For Anthropic and Claude: shipping as a recognized iOS 27 Extension — accessible from any app using Core AI Tier 2 — is a larger distribution surface than any number of app-level integrations. The same is true for OpenAI and Google.

For builders: the right move is to meet users where their preference already lives. Core AI makes that architecture possible without building a multi-provider abstraction layer yourself.
