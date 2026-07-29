# Write Once, Run on Any LLM: Anthropic's Claude Swift Package for Apple's Foundation Models Protocol

> Apple's LanguageModel protocol, announced at WWDC 2026, lets iOS and macOS apps swap between on-device Apple intelligence, Claude, and Gemini by changing one Swift Package Manager dependency. Anthropic released its implementation June 9. Here's how to use it.


On June 8, 2026, Apple announced a significant change to the Foundation Models framework at WWDC: the `LanguageModel` interface is now a **public Swift protocol** ([session 339, "Bring an LLM provider to the Foundation Models framework"](https://developer.apple.com/videos/play/wwdc2026/339/); [`LanguageModel` protocol reference](https://developer.apple.com/documentation/foundationmodels/languagemodel)). Any model provider — Apple, Anthropic, Google, or a third-party server you run yourself — can implement it. On June 9, Anthropic shipped [`ClaudeForFoundationModels`](https://github.com/anthropics/ClaudeForFoundationModels), its conforming Swift package ([Anthropic's docs](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)).

The practical result: if you write your session logic against the `LanguageModel` protocol, you can swap between Apple's on-device model and Claude by changing a single Swift Package Manager dependency. No changes to your session code, tool calls, or context management.

This is different from what we covered in our [Foundation Models guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/) earlier this week, which focused on Apple's on-device model. This article covers the multi-provider protocol — what it means, how to use it, and when to route between on-device and cloud.

---

## What Changed at WWDC 2026

The original Foundation Models framework ([introduced at WWDC 2025](https://developer.apple.com/videos/play/wwdc2025/286/)) exposed Apple's on-device LLM through a concrete `SystemLanguageModel` behind `LanguageModelSession`. You could call it, but it was tied to Apple's model. Providers had no hook to implement.

WWDC 2026 formalized a public conformance surface with two protocols ([`LanguageModel` reference](https://developer.apple.com/documentation/foundationmodels/languagemodel); [session 339 walkthrough](https://developer.apple.com/videos/play/wwdc2026/339/)): `LanguageModel`, which describes a model's `capabilities` and supplies the `executorConfiguration` the framework needs, and `LanguageModelExecutor`, which does the actual inference work (`init(configuration:)`, an optional `prewarm`, and a `respond(to:model:streamingInto:)` that streams generation back to the session).

Any type that conforms to `LanguageModel` can now be used everywhere Apple's on-device model used to be required — you construct a `LanguageModelSession(model:)` with the conforming model, and Apple's session logic (tool calling, `@Generable` structured outputs, streaming, multi-turn context) runs against it unchanged.

Session 339, "Bring an LLM provider to the Foundation Models framework," shows the full conformance surface. Anthropic ([`ClaudeForFoundationModels`](https://github.com/anthropics/ClaudeForFoundationModels)) and Google (Gemini via the [Firebase Apple SDK](https://firebase.blog/posts/2026/06/apple-foundation-models-gemini/), announced on [Google's developer blog](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/)) both published implementations the same week.

---

## Adding Claude as a Provider

Anthropic's package is [`ClaudeForFoundationModels`](https://github.com/anthropics/ClaudeForFoundationModels). Add it via Swift Package Manager ([install instructions](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models#install-the-package)):

```swift
// Package.swift
dependencies: [
  .package(url: "https://github.com/anthropics/ClaudeForFoundationModels.git", from: "0.1.0")
]
```

Then replace Apple's model with Claude:

```swift
import FoundationModels
import ClaudeForFoundationModels

// Before (Apple on-device):
let session = LanguageModelSession()

// After (Claude):
let model = ClaudeLanguageModel(
  name: .sonnet5,
  auth: .apiKey(ProcessInfo.processInfo.environment["ANTHROPIC_API_KEY"] ?? "")
)
let session = LanguageModelSession(model: model)
let response = try await session.respond(to: "You are a helpful assistant.")
```

Your tool calls, `@Generable` decoders, and SwiftUI streaming views work unchanged. The session logic doesn't care which model is behind the protocol. ([Anthropic's quick-start example](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models#quick-start))

---

## The Three-Provider Decision

The provider protocol creates a three-way choice for iOS/macOS builders. Here is how to allocate workloads:

### Apple On-Device (SystemLanguageModel.default)
**When to use:** Simple completions, user-facing text suggestions, privacy-sensitive content, features that must work offline.

**Cost:** Free. No API key. No network request. Runs on Neural Engine.

**Limits:** Smaller context window than cloud models. No web search or code execution. Cannot handle tasks requiring long multi-step reasoning.

**Implementation:** Zero configuration — `LanguageModelSession()` uses the on-device model by default.

---

### Claude via ClaudeForFoundationModels
**When to use:** Complex multi-step reasoning, long-context tasks, tasks requiring tool calls to external services, code generation, scientific analysis.

**Cost:** API pricing applies. Claude Fable 5: $10/million input tokens, $50/million output tokens ([Anthropic's Fable 5 / Mythos 5 announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5)). The `ClaudeForFoundationModels` package's compiled-in model constants are `.sonnet5` and `.opus5`; other model IDs (including Fable 5) can be used by declaring a custom `ClaudeModel` with explicit capabilities ([package docs](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models#choosing-a-model)).

**Limits:** Requires an Anthropic API key and network access. Data leaves the device and is processed by Anthropic's infrastructure under Anthropic's privacy policy. Requests go directly from your app to the Claude API — Apple is not in the request path.

**Implementation:** `ClaudeLanguageModel(name:auth:)`, passed to `LanguageModelSession(model:)`, then call `session.respond(to:)` as above ([quick start](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models#quick-start)).

---

### Gemini via the Firebase Apple SDK
**When to use:** Tasks where you already use Gemini elsewhere in your stack, large-batch image analysis (Gemini's multimodal context window), or when Gemini's lower pricing on Flash-class work is relevant.

**Cost:** Gemini 3.5 Flash: $1.50/million input tokens, $9.00/million output tokens ([Google's official pricing](https://ai.google.dev/gemini-api/docs/pricing)) — lower than Claude for high-volume simple tasks.

**Implementation:** `GeminiLanguageModel`, obtained from `FirebaseAI` (`FirebaseAILogic` library, added via the Firebase Apple SDK), passed to `LanguageModelSession(model:)` ([Firebase's announcement](https://firebase.blog/posts/2026/06/apple-foundation-models-gemini/); [Google's developer blog post](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/)). As of this writing the integration is a preview requiring a branch-based SPM dependency rather than a tagged release.

---

## Swapping at the Call Site

The protocol enables routing decisions at session creation time without restructuring app code. A common pattern:

```swift
func makeInferenceSession(task: TaskComplexity) -> LanguageModelSession {
    switch task {
    case .simple, .privacySensitive:
        return LanguageModelSession()  // Apple on-device
    case .complex, .longContext:
        let model = ClaudeLanguageModel(name: .sonnet5, auth: .apiKey(apiKey))
        return LanguageModelSession(model: model)
    case .highVolumeBatch:
        let model = FirebaseAI.firebaseAI().geminiLanguageModel(name: "gemini-3.5-flash")
        return LanguageModelSession(model: model)
    }
}
```

The rest of your app — tool call dispatch, `@Generable` parsing, streaming view updates — calls the returned session without knowing which provider is behind it (this pattern follows [Anthropic's own quick-start example](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models#quick-start) and [Firebase's Gemini sample](https://firebase.blog/posts/2026/06/apple-foundation-models-gemini/)).

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

**Longer context, higher cost.** Claude Fable 5 supports up to 1M tokens of context, with up to 128K output tokens per request ([Anthropic's context-window docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)). Apple's on-device model — a dense ~3B-parameter model, per [Apple's Machine Learning Research overview of its third-generation Foundation Models](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) — has a much smaller window. Tasks that fit in on-device context may produce substantially larger API bills if routed to Claude by mistake.

**Safety classifiers.** Claude Fable 5 routes requests in three domains (cybersecurity, biology/chemistry, and detected model-distillation attempts) to Opus 4.8 automatically rather than answering directly; Anthropic says over 95% of Fable 5 sessions involve no fallback at all ([Anthropic's Fable 5 / Mythos 5 announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5)). If your app generates content in these domains and expects Claude Fable 5 specifically, factor this in.

**Tokenizer differences.** The tokenizer introduced with Opus 4.7 (and shared by Fable 5 and Opus 4.8) produces approximately 30% more tokens than pre-4.7 models for the same input text; migrating between Fable 5 and Opus 4.7/4.8 does not change token counts ([Anthropic's migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)). If you are estimating API costs from pre-4.7 Claude usage, recalibrate.

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

Claude's Foundation Models Swift package requires iOS 27, macOS 27, visionOS 27, or watchOS 27 (all in beta at launch) and Xcode 27 (beta) — the same minimum targets as Foundation Models itself ([Anthropic's package requirements](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models#requirements)).

The [iOS 27 public beta opened July 13-14, 2026](https://www.techtimes.com/articles/320313/20260713/ios-27-public-beta-arrives-this-week-how-install-iphone-18-dates-it-locks.htm); the stable release is expected alongside the iPhone 18 around September 2026 ([9to5Mac](https://9to5mac.com/2026/07/02/ios-27-public-beta-release-date-when-you-can-install-the-new-iphone-update/)). If you are building for iOS 26 or earlier, the Foundation Models provider protocol is not available. Anthropic does not publish an official Swift SDK for the general-purpose Messages API — the officially supported client SDKs are Python, TypeScript, C#, Go, Java, PHP, and Ruby ([Anthropic's SDK overview](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)) — so on older OS versions you'd call the [Messages API](https://platform.claude.com/docs/en/api/messages/create) directly over HTTP or use a community Swift HTTP client.

For macOS developers: macOS 27 ("Golden Gate," [announced at WWDC 2026](https://www.macworld.com/article/3189014/apple-july-2026-ios-ipados-macos-27-public-betas-tv-arcade-releases.html)) ships in fall 2026 on the same schedule. The same package works on M-series Macs.

---

## What This Means for the AI Stack on Apple Platforms

The `LanguageModel` protocol announcement is quietly significant. Apple turned its on-device LLM from a locked proprietary endpoint into an open interface — and then opened that interface to its biggest competitors. Anthropic and Google now have first-class status in iOS and macOS apps, installable with a single SPM entry and zero additional UI code.

From a platform strategy perspective: Apple benefits because richer cloud-backed features drive device sales, and Apple's on-device model handles the private, offline, and cost-sensitive subset. Developers benefit because a single session API reduces platform fragmentation. The model providers benefit because iOS is a massive distribution channel.

The practical result for builders: write to the protocol, test on-device, and route to Claude for tasks where model quality matters more than cost or privacy.

---

## See Also

- [Apple Foundation Models in iOS 27: The Complete Builder Guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/) — the on-device model, `@Generable`, tool calling, and fine-tuning
- [iOS 27 AI Framework Decision Guide: Which One Do You Actually Need?](/builders-log/ios-27-apple-intelligence-framework-decision-guide-wwdc-2026/) — when to use Foundation Models vs. App Intents vs. other iOS 27 AI framework options
- [Claude Fable 5 and Mythos 5 Launch: Builder Guide](/builders-log/claude-fable-5-mythos-5-june-2026-builder-guide/) — Fable 5 API details, pricing, and the tokenizer change that affects cost estimation

