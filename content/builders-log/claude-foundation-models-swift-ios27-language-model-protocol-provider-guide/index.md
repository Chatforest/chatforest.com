---
title: "Write Once, Run on Any LLM: Anthropic's Claude Swift Package for Apple's Foundation Models Protocol"
date: 2026-06-10
description: "Apple's LanguageModel protocol, announced at WWDC 2026, lets iOS and macOS apps swap between on-device Apple intelligence, Claude, and Gemini by changing one Swift Package Manager dependency. Anthropic released its implementation June 9. Here's how to use it."
og_description: "Apple's new LanguageModel protocol makes every LLM provider — on-device Apple, Claude, Gemini — a drop-in swap. Anthropic's Swift package shipped June 9. One protocol, one session API, any cloud. Builder's guide inside."
content_type: "Builder's Log"
categories: ["Apple", "Developer Tools", "Mobile AI", "Claude SDK"]
tags: ["apple", "foundation-models", "ios-27", "macos-27", "wwdc-2026", "claude", "swift", "language-model-protocol", "provider-swap", "anthropic", "swift-package-manager", "on-device-ai", "builder-guide"]
---

On June 8, 2026, Apple announced a significant change to the Foundation Models framework at WWDC: the `LanguageModel` interface is now a **public Swift protocol**. Any model provider — Apple, Anthropic, Google, or a third-party server you run yourself — can implement it. On June 9, Anthropic shipped its implementation.

The practical result: if you write your session logic against the `LanguageModel` protocol, you can swap between Apple's on-device model and Claude by changing a single Swift Package Manager dependency. No changes to your session code, tool calls, or context management.

This is different from what we covered in our [Foundation Models guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/) earlier this week, which focused on Apple's on-device model. This article covers the multi-provider protocol — what it means, how to use it, and when to route between on-device and cloud.

---

## What Changed at WWDC 2026

The original Foundation Models framework (introduced at WWDC 2025) exposed Apple's on-device LLM through a concrete `LanguageModelSession` class. You could call it, but it was tied to Apple's model. Providers had no hook to implement.

WWDC 2026 formalized the underlying type as a protocol:

```swift
public protocol LanguageModel: Sendable {
    associatedtype Session: LanguageModelSession
    func makeSession(instructions: String?) async throws -> Session
}
```

Any type that conforms to `LanguageModel` can now be used everywhere Apple's on-device model used to be required. Apple's session logic — tool calling, `@Generable` structured outputs, streaming, multi-turn context — runs against any conforming provider.

The WWDC session "Bring an LLM provider to the Foundation Models framework" (session 339) shows the full conformance surface. Anthropic and Google both published implementations the same week.

---

## Adding Claude as a Provider

Anthropic's package is `AnthropicFoundationModels`. Add it via Swift Package Manager:

```swift
// Package.swift
.package(
    url: "https://github.com/anthropics/anthropic-foundation-models-swift",
    from: "1.0.0"
)
```

Then replace Apple's model with Claude:

```swift
import AnthropicFoundationModels

// Before (Apple on-device):
let session = LanguageModelSession()

// After (Claude):
let model = AnthropicLanguageModel(apiKey: ProcessInfo.processInfo.environment["ANTHROPIC_API_KEY"]!)
let session = model.makeSession(instructions: "You are a helpful assistant.")
```

Your tool calls, `@Generable` decoders, and SwiftUI streaming views work unchanged. The session logic doesn't care which model is behind the protocol.

---

## The Three-Provider Decision

The provider protocol creates a three-way choice for iOS/macOS builders. Here is how to allocate workloads:

### Apple On-Device (SystemLanguageModel.default)
**When to use:** Simple completions, user-facing text suggestions, privacy-sensitive content, features that must work offline.

**Cost:** Free. No API key. No network request. Runs on Neural Engine.

**Limits:** Smaller context window than cloud models. No web search or code execution. Cannot handle tasks requiring long multi-step reasoning.

**Implementation:** Zero configuration — `LanguageModelSession()` uses the on-device model by default.

---

### Claude via AnthropicFoundationModels
**When to use:** Complex multi-step reasoning, long-context tasks (128K+ tokens with Fable 5), tasks requiring tool calls to external services, code generation, scientific analysis.

**Cost:** API pricing applies. Claude Fable 5: $10/million input tokens, $50/million output tokens. Claude Opus 4.8: $5/$25 per million tokens for most tasks.

**Limits:** Requires an Anthropic API key and network access. Data leaves the device and is processed by Anthropic's infrastructure under Anthropic's privacy policy.

**Implementation:** `AnthropicLanguageModel(apiKey:)`, then call `makeSession` as above.

---

### Gemini via GoogleFoundationModels
**When to use:** Tasks where you already use Gemini elsewhere in your stack, large-batch image analysis (Gemini's multimodal context window), or when Gemini's lower pricing on Flash-class work is relevant.

**Cost:** Gemini 3.5 Flash: $1.50/$9.00 per million tokens — lower than Claude for high-volume simple tasks.

**Implementation:** `GoogleLanguageModel(apiKey:)` from `google/google-foundation-models-swift`.

---

## Swapping at the Call Site

The protocol enables routing decisions at session creation time without restructuring app code. A common pattern:

```swift
func makeInferenceSession(task: TaskComplexity) -> any LanguageModelSession {
    switch task {
    case .simple, .privacySensitive:
        return LanguageModelSession()  // Apple on-device
    case .complex, .longContext:
        let model = AnthropicLanguageModel(apiKey: apiKey)
        return try await model.makeSession(instructions: systemPrompt)
    case .highVolumeBatch:
        let model = GoogleLanguageModel(apiKey: googleKey)
        return try await model.makeSession(instructions: systemPrompt)
    }
}
```

The rest of your app — tool call dispatch, `@Generable` parsing, streaming view updates — calls the returned session without knowing which provider is behind it.

---

## What Stays the Same

Because Claude's Swift package conforms to Apple's protocol, these features work with Claude without modification:

- **`@Generable` structured outputs** — Define a Swift struct, annotate with `@Generable`, and the session returns a type-safe instance. Claude uses its JSON mode under the hood.
- **Tool calling in sessions** — Register tools on the session; the session handles the Claude tool-use loop and returns final output to your app.
- **SwiftUI streaming** — `AsyncStream` from `session.streamResponse(to:)` works regardless of which model drives it. Your streaming views need no changes.
- **Multi-turn context** — Session history is managed at the protocol layer. Swapping providers starts a fresh session (expected); context is not transferable across providers.

---

## What's Different with Claude

A few behaviors are model-specific and builders should be aware of them:

**Longer context, higher cost.** Claude Fable 5 supports up to 1M tokens of context (128K output). Apple's on-device model has a much smaller window. Tasks that fit in on-device context may produce substantially larger API bills if routed to Claude by mistake.

**Safety classifiers.** Claude Fable 5 has three hard blocks (cybersecurity, bio/chem, distillation) that fall back to Opus 4.8 automatically. If your app generates content in these domains and expects Claude Fable 5 specifically, factor this in.

**Tokenizer differences.** The Fable 5 tokenizer uses approximately 30% more tokens than models pre-Opus 4.7 for the same input text. If you are estimating API costs from historical Claude usage, recalibrate.

**Latency.** On-device inference is synchronous and local. Claude requires a network round-trip plus inference time on Anthropic's servers. For UI features where latency matters, prefer on-device for initial responses and Claude for background/async tasks.

---

## Privacy Architecture Considerations

The protocol does not enforce privacy decisions — your routing logic does. When you send a `LanguageModelSession` request to Claude, the session content (user input, tool call outputs, conversation history) leaves the device and is transmitted to Anthropic's API under Anthropic's data handling practices.

For iOS apps handling health data, financial data, or sensitive personal information:

1. **Use Apple on-device for all user-identifiable content.** The Neural Engine guarantees the data never leaves the device.
2. **Anonymize or abstract before routing to cloud providers.** Send the structure of a problem ("analyze a medication interaction") rather than the specific personal identifiers.
3. **Document your routing logic in your privacy disclosure.** iOS App Store Review requires privacy nutrition labels to accurately reflect which services process user data.

---

## Deployment Availability

Claude's Foundation Models Swift package requires iOS 27, iPadOS 27, macOS 27 (Golden Gate), visionOS 27, or watchOS 27 — the same minimum targets as Foundation Models itself.

The iOS 27 public beta opens in July 2026. The stable release ships alongside iPhone 18 in September 2026. If you are building for iOS 26 or earlier, the Foundation Models protocol is not available — use the [Anthropic Swift SDK](https://github.com/anthropics/anthropic-sdk-swift) directly.

For macOS developers: macOS 27 (Golden Gate) ships in fall 2026 on the same schedule. The same package works on M-series Macs.

---

## What This Means for the AI Stack on Apple Platforms

The `LanguageModel` protocol announcement is quietly significant. Apple turned its on-device LLM from a locked proprietary endpoint into an open interface — and then opened that interface to its biggest competitors. Anthropic and Google now have first-class status in iOS and macOS apps, installable with a single SPM entry and zero additional UI code.

From a platform strategy perspective: Apple benefits because richer cloud-backed features drive device sales, and Apple's on-device model handles the private, offline, and cost-sensitive subset. Developers benefit because a single session API reduces platform fragmentation. The model providers benefit because iOS is a massive distribution channel.

The practical result for builders: write to the protocol, test on-device, and route to Claude for tasks where model quality matters more than cost or privacy.

---

## See Also

- [Apple Foundation Models in iOS 27: The Complete Builder Guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/) — the on-device model, `@Generable`, tool calling, and fine-tuning
- [iOS 27 AI Framework Decision Guide: Which One Do You Actually Need?](/builders-log/ios-27-apple-intelligence-framework-decision-guide-wwdc-2026/) — when to use Foundation Models vs. Core AI vs. App Intents vs. Siri Extensions
- [Claude Fable 5 and Mythos 5 Launch: Builder Guide](/builders-log/claude-fable-5-mythos-5-june-2026-builder-guide/) — Fable 5 API details, pricing, and the tokenizer change that affects cost estimation
