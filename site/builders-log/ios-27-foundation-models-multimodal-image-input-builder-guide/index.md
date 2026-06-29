# iOS 27 Foundation Models Goes Multimodal: Builder's Guide to Image Input on Apple Silicon

> WWDC 2026 confirmed: the Foundation Models framework in iOS 27 now accepts image input. The on-device model can analyze photos, screenshots, documents, and camera frames — on-device, privately, no network required. Here's what builders need to know.


The Foundation Models framework in iOS 27 now accepts image input.

WWDC 2026 confirmed what had been anticipated since the framework shipped in iOS 26: Apple's on-device language model is no longer text-only. Apps can now pass images — photos, screenshots, documents, camera frames, UI captures — alongside text prompts, and the model processes both together, on-device, without sending data to any network.

This matters in ways that go beyond convenience. For apps that process user photos, medical images, receipts, identity documents, or proprietary business data, "on-device" is not a marketing claim — it is the only viable architecture. Foundation Models multimodal makes that architecture available in Swift with a handful of API calls.

This guide covers what was announced at WWDC 2026, the API surface, the use cases it actually enables, the ones it doesn't, and how to choose between Foundation Models vision and Apple's existing vision frameworks.

---

## What Was Announced at WWDC 2026

The Foundation Models framework shipped in iOS 26 (WWDC 2025) as a text-only API giving Swift apps direct access to Apple's on-device language model — roughly 3 billion parameters, running entirely on the Neural Engine with no network requirement. The initial API covered structured text generation, tool calling, schema-constrained output, and session context.

WWDC 2026 adds image input as a first-class capability. Key announcements:

**`ImageContent` type in the Foundation Models API.** Prompts can now include `ImageContent` alongside text, in any order. The model processes the combined input as a single context.

**Camera, photo library, and file input.** `ImageContent` can be initialized from a `UIImage`, a `CGImage`, a `CVPixelBuffer` (for live camera frames), or a file URL. Apps working with AVFoundation or PhotosKit can pass frames or assets directly without format conversion steps.

**On-device processing only.** Image analysis in Foundation Models does not route to Private Cloud Compute. The on-device model handles it entirely. Unlike text requests that may route to PCC for larger context or reasoning tasks, image input is explicitly processed locally in iOS 27.

**Privacy-appropriate disclosure.** Apple updated the Apple Intelligence disclosure UI to distinguish between text-only and multimodal interactions. Apps using image input surface a separate disclosure point in Apple's system-level Privacy Nutrition Labels for AI features.

**New WWDC session:** "Multimodal experiences with Foundation Models" in the WWDC26 session catalog covers the API, model capabilities, performance characteristics, and testing workflows.

---

## The API Surface

Foundation Models multimodal builds on the same session-based API introduced in iOS 26. Existing text-only integrations require minimal changes.

### Adding image input to a session prompt

```swift
import FoundationModels

let session = LanguageModelSession()

// From UIImage
let image = UIImage(named: "receipt.jpg")!
let imageContent = ImageContent(image: image)

let response = try await session.respond(to: [
    .text("Extract the total amount, merchant name, and date from this receipt."),
    .image(imageContent)
])

print(response.content)
```

The prompt parts array accepts text and image content in any order. The model processes the full context — text before the image, image, text after the image — as a unified input.

### Passing camera frames

For live camera analysis using AVFoundation:

```swift
// In your AVCaptureVideoDataOutputSampleBufferDelegate
func captureOutput(_ output: AVCaptureOutput,
                   didOutput sampleBuffer: CMSampleBuffer,
                   from connection: AVCaptureConnection) {
    guard let pixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }

    Task {
        let imageContent = ImageContent(pixelBuffer: pixelBuffer)
        let response = try await session.respond(to: [
            .text("Describe what you see."),
            .image(imageContent)
        ])
        // Update UI with response
    }
}
```

The `CVPixelBuffer` initializer is designed for the capture pipeline — no intermediate `UIImage` conversion required.

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

let response = try await session.respond(
    to: [
        .text("Extract this receipt's data."),
        .image(ImageContent(image: receiptImage))
    ],
    generating: ReceiptData.self
)

let receipt = response.content
// receipt.merchantName, receipt.totalAmount, etc.
```

Structured extraction from images — receipts, business cards, forms, labels — is cleaner than parsing free-text responses and eliminates prompt engineering for output format.

---

## What the Model Can Do

The on-device Foundation Models model is approximately 3 billion parameters — small by cloud LLM standards, but within the range of capable multimodal small models. The WWDC session on multimodal experiences is candid about capability boundaries.

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
- **Long-range image understanding** — the on-device context window affects how much of a large image's detail the model can process. The WWDC session specifies a maximum image resolution for optimal performance (tiled at higher resolutions).
- **Multi-image comparison** — the iOS 27 release supports one image per prompt turn. Multi-image input is documented as a post-launch update.

---

## Privacy Model

Privacy is the primary reason to choose Foundation Models over cloud vision APIs. Understanding the privacy model matters for both implementation decisions and user-facing communications.

**On-device only, no exceptions.** Unlike text processing in Foundation Models — where complex requests may route to Private Cloud Compute when the on-device model is insufficient — image input is processed entirely on-device in iOS 27. Apple's WWDC session states this explicitly: image content never leaves the device, regardless of request complexity.

**No persistent storage.** The Foundation Models session holds context in memory during the session. When the session ends, the context is cleared. Images passed to the model are not written to disk by the framework.

**App sandbox applies.** Your app provides the image; the Foundation Models framework processes it within your app's process. The image is not accessible to other apps or system processes beyond what your app explicitly controls.

**Privacy Nutrition Label requirement.** Apps using Foundation Models with image input must update their App Store Privacy Nutrition Labels to reflect image data processing. Apple's reviewer guidelines, updated for iOS 27, include specific guidance for AI feature disclosures.

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
    let imageContent = ImageContent(cgImage: cropped)
    let description = try await session.respond(to: [
        .text("What document is this? What does it say?"),
        .image(imageContent)
    ])
}
```

---

## Performance Characteristics

The WWDC session on multimodal Foundation Models includes benchmark data for common use cases on supported devices. Key points before you start building:

**Device requirements.** Foundation Models (text and image) requires Apple Silicon — A17 Pro or later on iPhone, M1 or later on Mac. A17 Pro excludes some 2023 non-Pro iPhone models. Plan your minimum deployment target accordingly.

**Cold start vs. warm session.** The first Foundation Models request in a session initializes the model on the Neural Engine — latency is higher than subsequent requests in the same session. For camera-frame analysis use cases, initialize the session before the camera session starts.

**Resolution scaling.** The model internally scales input images to its training resolution. Passing a 48MP photo provides no accuracy benefit over a scaled version. Use `ImageContent(image:targetSize:)` to hint at a target resolution before model ingestion — this reduces memory and pre-processing time. The WWDC session specifies the recommended target size for maximum accuracy vs. minimum latency tradeoffs.

**Streaming with image input.** Image analysis supports `session.streamResponse(to:)` the same as text requests. For long descriptions or extraction tasks, streaming lets you update the UI progressively rather than waiting for the complete response.

**Concurrent requests.** The Neural Engine handles one Foundation Models request at a time. If your app submits concurrent requests — text session and image session simultaneously — they are queued. Design your app to avoid unnecessary concurrency in the Foundation Models layer.

---

## Testing in Foundation Models Playground

Xcode 17's Foundation Models Playground added image input support alongside the multimodal API.

In Playground, you can:
- Drag-drop images into the prompt editor alongside text
- Test structured extraction schemas with real images
- View the model's raw output and parsed `@Generable` result side by side
- Use the Metrics panel to see per-request latency, token count, and Neural Engine utilization for image vs. text-only requests

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

The iOS 27 developer beta is available at developer.apple.com as of June 8. To get started with Foundation Models multimodal:

1. **Install the iOS 27 beta.** Foundation Models vision is available on physical devices with A17 Pro or later. The Simulator does not run the on-device model.

2. **Open Foundation Models Playground in Xcode 17.** Test your target document or image type before writing app code. Build intuition for what the model handles well.

3. **Identify your highest-value extraction task.** Start with one use case — the document type your users most often photograph — rather than building a general-purpose vision layer.

4. **Add `ImageContent` to an existing session.** If your app already uses Foundation Models for text, the image API is additive. Extend an existing session rather than building a separate integration.

5. **Update your Privacy Nutrition Label.** If you ship, App Review will check for the updated disclosure. Add the image data processing entry before submitting for review.

6. **Watch the WWDC session.** "Multimodal experiences with Foundation Models" covers capability benchmarks, resolution guidance, and the multi-image roadmap. It is in the WWDC26 session catalog at developer.apple.com/wwdc26.

---

Foundation Models started as a text API. As of iOS 27, it is a multimodal platform — and one that processes images entirely on-device. For builders whose apps work with documents, photos, forms, or camera input, the use cases are immediate. The privacy model is the strongest available on any mobile platform. And it runs in Swift, without a network request, on hardware your users already own.

---

*ChatForest covers AI tools and platforms for builders. This article reflects WWDC 2026 announcements and the iOS 27 developer beta. The Foundation Models framework is evolving — check developer.apple.com/wwdc26 for the authoritative session content and API documentation.*

