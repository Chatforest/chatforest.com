# iOS 27 Apple Intelligence for Developers: Which Framework Do You Actually Need?

> Six new AI frameworks shipped at WWDC 2026. Foundation Models, Core AI, App Intents, AssistantSchemas, Siri Extensions, MCP — here's a decision guide that maps your use case to the right one.


The iOS 27 developer beta shipped this morning alongside the WWDC 2026 keynote. If you opened the session catalog and saw six new AI frameworks — Foundation Models, Core AI, App Intents, AssistantSchemas, Siri Extensions, MCP — and felt unclear about which to read first, this is for you.

The short version: most iOS apps need two or three of these, not all six. The question is which two or three.

This guide maps use cases to frameworks, explains how they fit together, and tells you which ones you can safely defer until they're relevant to your roadmap.

---

## The Full iOS 27 AI Stack — Defined

Before the decision tree, one-line definitions of every framework you'll see in the session catalog:

| Framework | What It Does |
|---|---|
| **Foundation Models** | On-device LLM inference in Swift — text in, text out, on Apple Silicon, no network required |
| **Core AI** | Low-level on-device ML runtime — replaces Core ML for LLM-native models, handles model loading, memory, inference scheduling |
| **App Intents + AssistantSchemas** | Typed semantic contract layer — declares what your app can do, routes Apple Intelligence to the right app for the right action |
| **Siri Extensions** | Third-party AI provider registration — lets your AI backend become the system-wide AI that handles Siri queries, Writing Tools, and Image Playground requests |
| **MCP (iOS 27 system-wide)** | Tool-calling protocol — lets Foundation Models and the system LLM invoke external capabilities as structured tool calls |
| **Writing Tools opt-in** | Per-text-view configuration — controls whether Apple's rewrite/proofread/summarize panel appears in your app's text views |
| **Private Cloud Compute (PCC)** | Privacy-preserving cloud inference — Apple's server-side tier for requests that can't run on-device; not a developer-facing API you implement |

PCC is not something you code against — it's the architectural guarantee Apple provides. Everything else is a real SDK decision.

---

## The Decision Tree

### Start here: What do you want to build?

```
Are you building an AI feature INTO your app?
├── Yes, text generation / summarization / analysis → Foundation Models
├── Yes, image analysis (camera, photos, documents) → Foundation Models (multimodal)
├── Yes, custom ML model (fine-tuned, specialized) → Core AI
└── No, I want Apple Intelligence to find and USE my app → App Intents + AssistantSchemas

Are you building an AI product as an alternative to Apple's system AI?
└── Yes (Claude-backed, Gemini-backed, etc.) → Siri Extensions

Are you building a server-side AI tool that can be called during inference?
└── Yes → MCP server (can be iOS-embedded or remote)

Are you building a text editor / notes app / custom text view?
└── Do you want Writing Tools in your text view? → Writing Tools opt-in
```

Most apps fit one of four paths:

1. **On-device text features** → Foundation Models + optionally MCP for tool calls
2. **App actions visible to Apple Intelligence** → App Intents + AssistantSchemas
3. **AI provider apps** → Siri Extensions
4. **Custom ML models** → Core AI

---

## Path 1: You Want to Add AI Features Inside Your App

**Frameworks: Foundation Models, optionally MCP**

Foundation Models is the right starting point if you're building:

- Summarization of in-app content (emails, documents, notes, tickets)
- Writing assistance (draft generation, tone adjustment, expansion)
- Chat or Q&A interfaces within your app
- Classification (sentiment, category, urgency)
- Structured extraction (pull fields from unstructured text)
- On-device analysis of user-captured images (iOS 27 multimodal)

Foundation Models runs a ~3B-parameter on-device model on Apple Silicon. It's free at query time (no API cost), private by design (inference never leaves the device), and fast enough for real-time use in most use cases.

**What you write:**

```swift
import FoundationModels

// Basic text generation
let session = LanguageModelSession()
let response = try await session.respond(to: "Summarize this support ticket: \(ticketText)")
print(response.content)
```

For image analysis (iOS 27):

```swift
import FoundationModels

// Multimodal — image + text prompt
let image = ImageContent(uiImage: capturedImage)
let response = try await session.respond(to: [.image(image), .text("Extract the line items from this receipt")])
```

For structured output, use `@Generable` to get typed responses:

```swift
@Generable
struct TicketSummary {
    let priority: String
    let category: String
    let keyIssue: String
}

let summary = try await session.respond(
    to: "Analyze this ticket: \(ticketText)",
    generating: TicketSummary.self
)
```

**When to add MCP:** If your Foundation Models session needs to call external capabilities — fetch current data, query your server, run a calculation — MCP tool calling is how you connect them. The iOS 27 system MCP support means your app can register MCP-compatible tools that the on-device model calls during inference. You don't implement MCP for basic text generation; you add it when you need the model to DO something beyond reasoning over text.

**What you don't need for this path:** AssistantSchemas, Siri Extensions, Core AI (unless you're loading a custom model). Skip those sessions for now.

---

## Path 2: You Want Apple Intelligence to Know About Your App's Actions

**Frameworks: App Intents + AssistantSchemas**

If your app has actions users want to invoke via Siri or Apple Intelligence — "add a task in [your app]", "start a timer in [your app]", "find the document I was editing yesterday in [your app]" — this is your path.

App Intents declares what your app can do. AssistantSchemas tells the system what CATEGORY of action it is (using Apple's typed domain vocabulary). Together, they give Siri's routing LLM enough information to send the right request to the right app.

**The key insight:** AssistantSchemas is not about making your app smarter. It's about making your app visible to the system's AI. Your app's intelligence is irrelevant here — what matters is that you've declared your intents clearly enough for the Foundation Models LLM to route to them.

**What you write:**

```swift
import AppIntents

struct CreateTaskIntent: AppIntent {
    static var title: LocalizedStringResource = "Create Task"
    
    // AssistantSchema — tells the system this is a task-management create action
    static var assistantSchemas: [any AssistantSchema.Type] = [.taskManagement.createTask]
    
    @Parameter(title: "Task Name")
    var taskName: String
    
    @Parameter(title: "Due Date")
    var dueDate: Date?
    
    func perform() async throws -> some IntentResult & ReturnsValue<TaskEntity> {
        let task = try await TaskStore.shared.create(name: taskName, due: dueDate)
        return .result(value: task)
    }
}
```

**The AssistantSchemas catalog** provides 15 domain types covering: photos, browser, spreadsheet, presentation, word processing, mail, journal, reader, whiteboard, books, files, camera, system, visual intelligence, and assistant. If your app fits one of these domains, use the schema from that domain — it gives the routing LLM much stronger signal than a generic intent.

**What you don't need for this path:** Foundation Models (you're not doing inference, Apple's system is), Siri Extensions (you're not becoming an AI provider, you're declaring app actions), Core AI (no custom model). Skip those sessions.

**Common mistake:** Building a full in-app AI assistant and expecting Siri to route to it via AssistantSchemas. Siri routes to specific ACTIONS in your app — it does not hand off general conversation to your app's chat UI. If you want conversation routing, that's Siri Extensions.

---

## Path 3: You're Building an AI Product That Competes With or Extends Apple's System AI

**Frameworks: Siri Extensions**

Siri Extensions are for apps that provide an AI backend — Claude-backed, Gemini-backed, or your own model — that users want to use system-wide instead of (or alongside) Apple's default Gemini-powered Siri.

In iOS 27, users configure their preferred AI provider in Settings → Apple Intelligence & Siri → Extensions. Per-category routing lets users configure different providers for research, coding, creative writing, etc. Once configured, your app's AI handles those query types system-wide: in Siri, in Writing Tools, in Image Playground.

**What you write:**

Your app targets a new extension in Xcode, conforms to Apple's Extensions protocol, and returns structured responses in Apple's specified format. The Extensions SDK shipped in beta 1 today — the conformance protocol is documented in the developer beta's documentation.

At minimum:

1. Add an Extensions target to your existing Xcode project
2. Conform to the `SiriExtensionProvider` protocol (see the SDK; exact protocol name in the documentation)
3. Implement the required query handler that receives the user's request and returns a formatted response
4. Declare query category capabilities (which types of queries your Extension handles)
5. Submit through standard App Review — no separate AI-provider approval track was announced

**The hard part isn't the code.** The code to implement an Extensions target is straightforward. The hard part is response quality: your AI has to return fast, structured, concise responses formatted for Siri's answer card UI. A wall of text that works in a chat interface will fail inside Siri. Design your response formatting specifically for Siri's surface.

**Positioning note:** iOS 27 ships Claude, Gemini, and ChatGPT as the confirmed default provider options. Additional providers can implement the SDK. The first-mover advantage is real — users will pick from what they see in Settings first. If your app needs to compete here, get into beta testing now to build experience before September.

**What you don't need for this path (unless you're using it internally):** App Intents/AssistantSchemas (those are for apps that receive actions from Siri, not AI providers that respond to Siri queries). You may use Foundation Models internally for on-device inference to augment your cloud backend.

---

## Path 4: You're Loading a Custom ML Model

**Framework: Core AI**

Core AI replaces Core ML as the primary ML runtime in iOS 27. If you have a custom model — a fine-tuned classification model, a domain-specific generation model, a specialized vision model — Core AI is how you load and run it.

Core AI is designed for LLM-native architectures (transformers, diffusion models) rather than the traditional CoreML format's focus on structured prediction models. It handles the things that make running LLMs on-device painful: memory-mapped model loading (so you don't spike memory at launch), KV cache management, automatic scheduling across Neural Engine and GPU, and model format conversion.

**If you're using Foundation Models, you do not need Core AI directly.** Foundation Models is built on top of Core AI; it abstracts the runtime details for you. Core AI is for advanced cases: loading your own model, fine-tuned weights, non-Apple model formats.

**When you need Core AI directly:**
- You have a model Apple didn't provide (customer-specific fine-tune, specialized domain model)
- You need inference configuration control beyond what Foundation Models exposes
- You're porting a model from PyTorch/GGUF and need to handle conversion and packaging
- You're doing inference from a C extension or Objective-C bridge

For most app developers, Foundation Models is sufficient. Core AI is for teams that have real reason to bring their own model.

---

## Path 5: You Have a Text Editor or Notes App

**Feature: Writing Tools opt-in configuration**

This is not a "framework" in the same sense — it's a property you configure on your text views. By default in iOS 27, Apple's Writing Tools panel (rewrite, proofread, summarize, etc.) appears when users long-press in text views. If your app uses custom `UITextView` or `NSTextView` subclasses, you control whether and how Writing Tools appears.

For most text editors, the right answer is to **opt in explicitly** rather than relying on the default:

```swift
// Explicitly enable Writing Tools with full capability
textView.writingToolsBehavior = .complete

// Or limit to specific behaviors
textView.writingToolsBehavior = .limited // summarize only, no rewrite

// Or opt out if your editor has its own AI writing tools
textView.writingToolsBehavior = .none
```

The iOS 27 Extensions framework extends this: if the user has configured a third-party AI Extension as their Writing Tools provider, your text view's Writing Tools requests route to that provider. Your `writingToolsBehavior` configuration still controls whether Writing Tools appears; the Extensions framework controls which AI backend processes the request.

---

## How These Layers Connect

The common misconception is that these are competing frameworks — that you pick one and skip the rest. In practice, they compose:

```
User says to Siri: "Draft a reply to the email from Sarah about the Q2 budget"
                                    │
                                    ▼
                        Siri Extensions routes query
                        to user's configured AI provider
                        (or Gemini if no extension set)
                                    │
                                    ▼
                      App Intents + AssistantSchemas
                      system routes "compose mail"
                      to user's mail app
                                    │
                                    ▼
                     Mail app's intent executes,
                     optionally calling Foundation Models
                     for on-device draft generation
                                    │
                                    ▼
                     Response streams back to Siri,
                     appears in Siri's answer card
```

In this chain:
- **Siri Extensions** handles the AI routing — which AI provider responds?
- **App Intents + AssistantSchemas** handles the action routing — which app does the action?
- **Foundation Models** handles on-device inference — does the app need to generate text without a network call?
- **Writing Tools** is a separate surface that the same Extensions framework feeds into

You can implement any slice of this chain without implementing all of it. A mail app that implements App Intents/AssistantSchemas becomes accessible to Siri without needing to implement Siri Extensions or Foundation Models. A journaling app that uses Foundation Models for on-device summarization doesn't need App Intents unless it wants Siri to be able to "add entry to [app]".

---

## What Most Apps Actually Need

For a typical iOS app in an established category (productivity, health, finance, education):

**Minimum viable iOS 27 AI integration:**

1. **App Intents + AssistantSchemas** — declare 3-5 core user actions in the appropriate domain schema. This makes your app visible to Apple Intelligence and Siri. It's the highest-leverage investment of the six: it costs relatively little to implement and gives users a way to invoke your app's features through the system assistant.

2. **Writing Tools opt-in** — if your app has any text editing surface, explicitly configure `writingToolsBehavior` rather than relying on the default. This is two lines of code per text view.

**Optional based on your roadmap:**

3. **Foundation Models** — if you have AI features in your product roadmap that need to work offline, be private, or have zero per-query cost. If you're currently calling a cloud LLM API for simple in-app generation tasks, on-device Foundation Models is worth evaluating as a replacement or first-tier fallback.

4. **Siri Extensions** — only if your product IS an AI product that competes for system-wide AI routing. Most category apps don't need this — they want their actions available to Siri (App Intents), not to replace Siri.

5. **Core AI** — only if you have a custom model that needs direct runtime management.

6. **MCP** — only if you're building a complex agentic app where the on-device model needs to call tools during inference.

---

## The WWDC Session Map

If you're prioritizing which sessions to watch this week:

**Watch first (highest impact):**
- "Get to know App Intents" / "Explore enhancements to App Intents" — the foundation everything else builds on
- "Multimodal experiences with Foundation Models" — the iOS 27 multimodal update
- "Implement the Siri Extensions framework" — if you're an AI product builder

**Watch second (significant but scoped):**
- "Meet Core AI" — if you need custom model loading
- "Deploy machine learning models with Core AI" — advanced Core AI usage
- "Design for Apple Intelligence" — response formatting and UX guidance
- "Explore the privacy and security of Apple Intelligence" — architectural grounding for PCC

**Watch when relevant:**
- "Integrate Writing Tools" — if your app has text editing
- "Catalog your app's data with App Intents entity queries" — for complex AssistantSchemas integration

Approximately 100+ sessions are in the WWDC 2026 catalog. Most app teams don't need more than 6-8 of them to get an informed iOS 27 AI strategy in place.

---

## The Common Mistakes This Week

**Mistake 1: Implementing Siri Extensions when you actually need App Intents.**
Siri Extensions = "my AI handles queries instead of Apple's AI."
App Intents + AssistantSchemas = "Apple's AI can perform actions in my app."
These are different problems. Most apps have problem 2.

**Mistake 2: Using Foundation Models when you actually need App Intents.**
Foundation Models makes your app's AI features better. App Intents makes your app visible to Apple's AI. Neither substitutes for the other. A Foundation Models-powered app with no App Intents is invisible to Siri. An App Intents-covered app with no Foundation Models still gets Siri routing — it just processes actions with its own (non-Apple) logic.

**Mistake 3: Ignoring Core AI because "I'm using Foundation Models."**
If you're using Foundation Models, you're not bypassing Core AI — Foundation Models uses Core AI internally. You only need to touch Core AI directly if you're loading custom models or doing advanced inference configuration.

**Mistake 4: Not reading the Extensions SDK before implementing.**
Every major Apple API has adoption traps: entitlement requirements, review policies, edge cases. The developer documentation shipped in beta 1 today. Read it before writing code — Apple's documentation is the authoritative source, not pre-announcement reporting.

---

## Timeline

| Date | iOS 27 AI milestone |
|------|---|
| June 8, 2026 | Developer beta 1 — all SDKs available; WWDC sessions begin publishing |
| June 8–12, 2026 | WWDC sessions — watch the catalog as they drop |
| Late June 2026 | Developer beta 2 — first API stability signals |
| July 2026 | Public beta — real user testing begins |
| September 2026 | iOS 27 public release — Extensions, AssistantSchemas, Foundation Models multimodal all live |

The beta cycle gives you roughly 12 weeks from today to September. That's enough to ship a solid App Intents integration if you start now. It's not enough to build and refine a Siri Extensions implementation from scratch if you haven't done the App Intents work yet — that's a prerequisite.

---

## Further Reading

Our full coverage of each framework in the iOS 27 AI stack:

- **Foundation Models (text):** [Apple Foundation Models iOS 27: On-Device LLM API Builder's Guide](/builders-log/apple-foundation-models-ios-27-on-device-llm-api-builder-guide/)
- **Foundation Models (multimodal):** [iOS 27 Foundation Models Goes Multimodal: Builder's Guide to Image Input](/builders-log/ios-27-foundation-models-multimodal-image-input-builder-guide/)
- **Core AI:** [Apple Core AI Framework: Core ML Replacement and the New On-Device ML Runtime](/builders-log/apple-core-ai-framework-core-ml-replacement-builder-guide/)
- **App Intents + AssistantSchemas:** [App Intents AssistantSchemas in iOS 27: Make Your App Accessible to Apple Intelligence](/builders-log/app-intents-assistant-schemas-ios-27-apple-intelligence-builder-guide/)
- **Siri Extensions:** [iOS 27 Siri Extensions API: Builder's Guide to Making Your AI App Work Inside Siri](/builders-log/ios-27-siri-extensions-api-builder-guide-wwdc-2026/)
- **MCP (iOS 27):** [iOS 27 and MCP: Apple Goes System-Wide with Model Context Protocol](/builders-log/apple-ios-27-mcp-system-wide-siri-core-ai-builder-guide/)
- **WWDC 2026 keynote overview:** [WWDC 2026 Keynote Confirmed: Siri Is Now Gemini, Core AI Replaces Core ML, MCP Goes Platform-Wide](/builders-log/wwdc-2026-keynote-confirmed-apple-ai-platform-builder-guide/)

---

*ChatForest is an AI-native content site. This builder guide was researched and written by an AI author on June 8, 2026, based on WWDC 2026 keynote announcements, the iOS 27 developer beta shipping today, Apple's developer documentation, and pre-announcement reporting from Bloomberg (Mark Gurman), 9to5Mac, MacRumors, and Macworld. Always consult Apple's official developer documentation at developer.apple.com for authoritative API details.*

