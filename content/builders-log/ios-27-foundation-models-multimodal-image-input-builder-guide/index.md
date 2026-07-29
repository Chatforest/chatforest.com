---
title: "iOS 27 Foundation Models Goes Multimodal: Builder's Guide to Image Input on Apple Silicon"
date: 2026-06-08
description: "WWDC 2026 confirmed: the Foundation Models framework in iOS 27 now accepts image input. The on-device model can analyze photos, screenshots, documents, and camera frames — on-device, privately, no network required. Here's what builders need to know."
og_description: "iOS 27 Foundation Models now accepts image input. Analyze photos, documents, screenshots, and camera frames with the on-device model — completely private, no cloud required. Builder's guide to the multimodal API, privacy model, use cases, and when to use Foundation Models vision vs VisionKit."
content_type: "Builder's Log"
categories: ["Developer Tools", "Apple", "On-Device AI", "Mobile AI"]
tags: ["apple", "ios-27", "foundation-models", "multimodal", "vision", "image-understanding", "on-device-ai", "wwdc-2026", "swift", "builder-guide", "core-ai", "apple-silicon", "privacy"]
sources_audited: 2026-07-29
---

The Foundation Models framework in iOS 27 now accepts image input.

[WWDC 2026 confirmed](https://developer.apple.com/wwdc26/guides/apple-intelligence/) what had been anticipated since the framework shipped in iOS 26: Apple's on-device language model is no longer text-only. Apps can now pass images — photos, screenshots, documents, camera frames, UI captures — alongside text prompts, and the model processes both together, on-device, without sending data to any network.

This matters in ways that go beyond convenience. For apps that process user photos, medical images, receipts, identity documents, or proprietary business data, "on-device" is not a marketing claim — it is the only viable architecture. Foundation Models multimodal makes that architecture available in Swift with a handful of API calls.

This guide covers what was announced at WWDC 2026, the API surface, the use cases it actually enables, the ones it doesn't, and how to choose between Foundation Models vision and Apple's existing vision frameworks.

---

## What Was Announced at WWDC 2026

The Foundation Models framework shipped in iOS 26 (WWDC 2025) as a text-only API giving Swift apps direct access to Apple's on-device language model — a [3-billion-parameter dense model](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models), running entirely on the Neural Engine with no network requirement. The initial API covered structured text generation, tool calling, schema-constrained output, and session context.

WWDC 2026 adds image input as a first-class capability. Key announcements:

**`Attachment` type in the Foundation Models API.** Prompts built with the framework's [prompt builder](https://developer.apple.com/videos/play/wwdc2026/241/) can now include an `Attachment` alongside text, in any order. The model processes the combined input as a single context.

**Camera, photo library, and file input.** Per Apple's WWDC26 session on the framework, an `Attachment` [can be created from a `UIImage`, `NSImage`, `CGImage`, Core Image types, a `CVPixelBuffer` (for live camera frames), or a file URL](https://developer.apple.com/videos/play/wwdc2026/241/). Apps working with AVFoundation or PhotosKit can pass frames or assets directly without format conversion steps.

**On-device processing only.** Apple's [WWDC26 Apple Intelligence guide states](https://developer.apple.com/wwdc26/guides/apple-intelligence/) that multimodal prompts let apps "reason about visual content... all on-device." Unlike text requests, which may route to Private Cloud Compute for larger context or heavier reasoning, image input to the Foundation Models framework is processed locally.

**New WWDC session:** ["What's new in the Foundation Models framework" in the WWDC26 session catalog](https://developer.apple.com/videos/play/wwdc2026/241/) covers the API, model capabilities, performance characteristics, and testing workflows.

---

## The API Surface

Foundation Models multimodal builds on the same session-based API introduced in iOS 26. Existing text-only integrations require minimal changes.

### Adding image input to a session prompt

```swift
import FoundationModels

let session = LanguageModelSession()

// From UIImage, added to the prompt builder as an Attachment
let image = UIImage(named: "receipt.jpg")!

let response = try await session.respond {
    "Extract the total amount, merchant name, and date from this receipt."
    Attachment(image)
}

print(response.content)
```

This is the [prompt-builder pattern Apple demonstrated at WWDC26](https://developer.apple.com/videos/play/wwdc2026/241/): text and `Attachment` values are composed inside the same builder closure, in any order, and the model processes the full context as a unified input.

### Passing camera frames

For live camera analysis using AVFoundation:

```swift
// In your AVCaptureVideoDataOutputSampleBufferDelegate
func captureOutput(_ output: AVCaptureOutput,
                   didOutput sampleBuffer: CMSampleBuffer,
                   from connection: AVCaptureConnection) {
    guard let pixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }

    Task {
        let response = try await session.respond {
            "Describe what you see."
            Attachment(pixelBuffer)
        }
        // Update UI with response
    }
}
```

Apple's session confirms `Attachment` [accepts a `CVPixelBuffer` directly](https://developer.apple.com/videos/play/wwdc2026/241/) — no intermediate `UIImage` conversion required for the capture pipeline.

### Structured output with image input

Foundation Models' structured generation (via `@Generable`) works with image input. This is useful for extraction tasks where you want typed output:

```swift
@Generable
struct ReceiptData {
    let merchantName: String
    let totalAmount: Double
    let transactionDate: String
    let lineItems: [String]
}

let response = try await session.respond(generating: ReceiptData.self) {
    "Extract this receipt's data."
    Attachment(receiptImage)
}

let receipt = response.content
// receipt.merchantName, receipt.totalAmount, etc.
```

Structured extraction from images — receipts, business cards, forms, labels — is cleaner than parsing free-text responses and eliminates prompt engineering for output format. A developer walkthrough of the iOS 27 image API confirms [guided generation "still shapes the output into a `@Generable` type"](https://blakecrosley.com/blog/foundation-models-image-input-ios-27) once an image attachment is added to the prompt.

---

## What the Model Can Do

The on-device Foundation Models model is approximately 3 billion parameters — small by cloud LLM standards, but within the range of capable multimodal small models. The lists below reflect [Apple's own "What's new in the Foundation Models framework" session](https://developer.apple.com/videos/play/wwdc2026/241/) plus independent developer testing of the iOS 27 beta.

**Strong use cases:**

- **Document text extraction** — receipts, invoices, business cards, printed forms, handwritten notes (legible print). The model performs well on OCR-adjacent tasks where the answer is present in the image.
- **Screenshot analysis** — what's on screen, what UI state is visible, what error is displayed. Useful for accessibility tools and automation.
- **Photo captioning and description** — factual description of image content. Suitable for accessibility alt-text generation and photo organization.
- **Label and packaging reading** — product names, ingredient lists, nutrition facts, barcodes alongside text fields.
- **Simple visual Q&A** — "Is there a cat in this photo?" "What color is the car?" "Does this form have a signature?"
- **UI screenshot parsing** — extracting values from app screenshots, status displays, or data visualizations.

**Where the model has limits:**

- **Complex spatial reasoning** — "Count all the people in the crowd" or "What is the exact distance between these two points" exceeds on-device model capability reliably.
- **Medical image interpretation** — radiology, pathology, ophthalmology. The model has no specialized training for these and should not be used for diagnostic purposes.
- **Fine-grained object recognition** — identifying specific plant species, bird species, or rare objects. Use CreateML classification models for domain-specific recognition tasks.
- **Very large images** — the framework accepts [any size or aspect ratio without cropping or padding](https://developer.apple.com/videos/play/wwdc2026/241/), but images are tokenized like any other input, so a very large photo consumes more of the on-device context budget and adds latency — there's no accuracy reason to pass a 48MP photo instead of a reasonably downscaled one.
- **Many images at once** — multiple images can share a single prompt, but they share the same token budget as your text. A developer analysis of the framework's session limits puts the [on-device context window at roughly 4,096 tokens, versus 32K when a request routes to Private Cloud Compute](https://ivanmagda.dev/posts/wwdc26-foundation-models-year-two/), so prompts carrying several images have more room to work with under PCC.

---

## Privacy Model

Privacy is the primary reason to choose Foundation Models over cloud vision APIs. Understanding the privacy model matters for both implementation decisions and user-facing communications.

**On-device, per Apple's own framing.** Unlike text processing in Foundation Models — where complex requests may route to Private Cloud Compute when the on-device model is insufficient — Apple's [WWDC26 Apple Intelligence guide describes multimodal image prompts as processed "all on-device."](https://developer.apple.com/wwdc26/guides/apple-intelligence/)

**No persistent storage.** The Foundation Models session holds context in memory during the session. When the session ends, the context is cleared. Images passed to the model are not written to disk by the framework.

**App sandbox applies.** Your app provides the image; the Foundation Models framework processes it within your app's process. The image is not accessible to other apps or system processes beyond what your app explicitly controls.

**Compared to VisionKit and Core Image.** VisionKit's `ImageAnalyzer` (for Live Text, subject lifting) also runs on-device. The privacy model is comparable. Foundation Models adds language understanding on top of vision recognition — the reason to use Foundation Models is when you need the model to reason about what it sees in natural language, not just detect or classify.

---

## Foundation Models Vision vs. VisionKit vs. CreateML

iOS has three overlapping vision frameworks. Choosing correctly matters for capability, performance, and privacy.

| Task | Best Framework |
|------|----------------|
| OCR / Live Text extraction | VisionKit `ImageAnalyzer` |
| Object detection (known classes) | Vision framework / CreateML |
| Custom image classification | CreateML classifier |
| Face detection, body pose, gaze | Vision framework |
| Natural language Q&A about image content | Foundation Models |
| Document extraction with structured output | Foundation Models + `@Generable` |
| Real-time object recognition, AR | Vision + ARKit |
| Image captioning for accessibility | Foundation Models |
| Specialized domain recognition (medical, industrial) | CreateML with domain data |

The rule of thumb: use Foundation Models when the task requires natural language reasoning about image content. Use Vision framework or VisionKit when the task is detection, classification, or recognition with defined output types. The two are composable — you can run Vision framework for object detection, then pass a crop to Foundation Models for contextual description.

```swift
// Compose Vision detection + Foundation Models description
let request = VNDetectRectanglesRequest()
let handler = VNImageRequestHandler(cgImage: cgImage)
try handler.perform([request])

if let rectangle = request.results?.first {
    let cropped = crop(cgImage, to: rectangle.boundingBox)
    let description = try await session.respond {
        "What document is this? What does it say?"
        Attachment(cropped)
    }
}
```

---

## Performance Characteristics

Apple's ["What's new in the Foundation Models framework"](https://developer.apple.com/videos/play/wwdc2026/241/) session and independent developer testing of the iOS 27 beta point to the following performance characteristics. Key points before you start building:

**Device requirements.** Foundation Models (text and image) requires Apple Silicon. Apple's own compatibility guidance for Apple Intelligence lists [iPhone 15 Pro/Pro Max or later (A17 Pro) and Mac or iPad with M1 or later](https://support.apple.com/en-us/121115). A17 Pro excludes 2023's non-Pro iPhone models. Plan your minimum deployment target accordingly.

**Cold start vs. warm session.** A practical developer write-up of shipping Foundation Models features notes that [a session's first response pays a one-to-two-second "cold start" while the model loads](https://drobinin.com/consulting/foundation-models-apple-intelligence/putting-apple-foundation-models-in-a-real-app/), and that calling `prewarm()` before the user is expected to act — not reactively on first prompt — is what actually hides that latency. For camera-frame analysis use cases, prewarm the session before the camera session starts.

**Resolution scaling.** Images are tokenized like any other input, and larger images cost more tokens and more latency — the [WWDC26 session on the framework](https://developer.apple.com/videos/play/wwdc2026/241/) notes the model accepts any size or aspect ratio without requiring you to crop or pad. In practice, that means downscaling a very large photo yourself before creating the `Attachment` when the task doesn't need full resolution, rather than relying on a built-in resize parameter.

**Streaming with image input.** A developer walkthrough of the iOS 27 image API confirms [streaming "still streams"](https://blakecrosley.com/blog/foundation-models-image-input-ios-27) once an image attachment is part of the prompt — `streamResponse` works the same as it does for text-only requests, letting you update the UI progressively rather than waiting for the complete response.

---

## Testing in Foundation Models Playground

[Xcode 27's Foundation Models Playground](https://developer.apple.com/videos/play/wwdc2026/241/) added image input support alongside the multimodal API. (Note: Apple's iOS/Xcode version numbers moved to match the release year starting with iOS 26/Xcode 26 — the iOS 27 cycle ships with **Xcode 27**, not Xcode 17.)

In Playground, you can:
- Drag-drop images into the prompt editor alongside text
- Test structured extraction schemas with real images
- View the model's raw output and parsed `@Generable` result side by side

For deeper performance profiling — time-to-first-token, tokens-per-second, and where latency goes per request — Xcode 27 also ships an [overhauled Foundation Models instrument in Instruments](https://developer.apple.com/videos/play/wwdc2026/243/) that visualizes the full tool-call loop for both text and image requests.

The Playground is the fastest way to evaluate whether Foundation Models vision can handle your specific document type or use case before writing app code. Run the receipt, form, or label type you plan to support through Playground first — if the model struggles there, it will struggle in your app.

---

## Use Cases Worth Building Now

**Receipt and expense capture.** Pass the camera frame or photo library image, extract structured data with `@Generable`, pre-populate an expense form. No cloud API, no OCR service, no billing.

**Accessibility alt-text generation.** When a user uploads or selects a photo in your app, automatically generate a descriptive alt-text string. Runs on-device, respects the user's image privacy, and works offline.

**Form pre-fill from document photos.** Business card → contact fields. Insurance card → coverage info. Prescription label → medication data. Each is a structured extraction task Foundation Models handles well.

**Screenshot-based support.** Let users attach a screenshot to a support request. Your app analyzes the screenshot on-device before sending the bug report — extracting app state, error messages, or relevant UI data — without sending raw screenshots to your servers.

**Private photo journaling.** Generate natural-language summaries of photo sets for private, on-device journaling apps where cloud upload is not acceptable to users.

**Offline document workflows.** In environments where network access is unavailable or prohibited — regulated industries, air-gapped workflows, field use — Foundation Models vision brings document extraction capability that previously required connectivity.

---

## What to Do Today

The [iOS 27 developer beta released June 8](https://www.macrumors.com/2026/06/05/ios-27-release-date-how-to-install-beta/), immediately after the WWDC keynote. To get started with Foundation Models multimodal:

1. **Install the iOS 27 beta.** Foundation Models vision is available on physical devices with A17 Pro or later. The Simulator does not run the on-device model.

2. **Open Foundation Models Playground in Xcode 27.** Test your target document or image type before writing app code. Build intuition for what the model handles well.

3. **Identify your highest-value extraction task.** Start with one use case — the document type your users most often photograph — rather than building a general-purpose vision layer.

4. **Add `Attachment` to an existing session.** If your app already uses Foundation Models for text, the image API is additive. Extend an existing session's prompt builder rather than building a separate integration.

5. **Watch the WWDC session.** ["What's new in the Foundation Models framework"](https://developer.apple.com/videos/play/wwdc2026/241/) covers the `Attachment` API, capability benchmarks, and resolution guidance. It is in the WWDC26 session catalog at developer.apple.com/wwdc26.

---

Foundation Models started as a text API. As of iOS 27, it is a multimodal platform — and one that processes images entirely on-device. For builders whose apps work with documents, photos, forms, or camera input, the use cases are immediate. The privacy model is the strongest available on any mobile platform. And it runs in Swift, without a network request, on hardware your users already own.

---

*ChatForest covers AI tools and platforms for builders. This article reflects [WWDC 2026 announcements](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/) and the iOS 27 developer beta. The Foundation Models framework is evolving — check [developer.apple.com/wwdc26](https://developer.apple.com/wwdc26/guides/apple-intelligence/) for the authoritative session content and API documentation.*
