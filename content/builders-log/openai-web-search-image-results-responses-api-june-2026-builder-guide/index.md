---
title: "OpenAI Web Search Image Results: Grounding Responses in Current Visuals"
date: 2026-07-02
description: "OpenAI's web search tool in the Responses API now returns image results alongside text results as of June 9, 2026. Set search_content_types to include image and receive image_url, thumbnail_url, source page, and caption fields per result."
og_description: "Use search_content_types=[\"image\",\"text\"] to ground your agent's response in current web visuals — product photos, landmarks, event imagery, and visual references delivered via web_search_call results."
content_type: "Builder's Log"
categories: ["OpenAI", "Agents", "Developer Tools"]
tags: ["openai", "web-search", "responses-api", "image-search", "multimodal", "builder-guide", "june-2026", "api", "grounding"]
---

OpenAI expanded the web search tool in the Responses API on June 9, 2026. In addition to text results, web search can now return image results — enabling agents to ground responses in current web visuals without requiring a separate image search integration. Part of our **[Builder's Log](/builders-log/)**.

---

## What Changed

The built-in web search tool previously returned only text results: links, titles, snippets, and source metadata. As of June 9, image results are available as a first-class output type. The agent can search for and return image URLs from the web, directly via the same tool call that retrieves text.

This matters for use cases where the answer is visual: product photos, event imagery, place photos, technical diagrams, and anything where current web images add context that text cannot.

---

## Enabling Image Results

Add `search_content_types` to the web search tool definition:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input=[{"role": "user", "content": "Show me what the new iPhone 17 Ultra looks like."}],
    tools=[{
        "type": "web_search",
        "search_content_types": ["image", "text"],
        "image_settings": {
            "max_results": 5,
            "caption": True,
        },
    }],
)
```

`search_content_types` accepts `"text"`, `"image"`, or both. Omitting it defaults to text-only, matching prior behavior. No beta header or separate feature flag is needed.

---

## Response Structure

Image results appear in the `web_search_call` item, separate from the assistant message. Parse the results from the tool call response, not from the model's text output:

```python
for item in response.output:
    if item.type == "web_search_call":
        for result in item.results:
            if result.type == "image_result":
                print("Image URL:", result.image_url)
                print("Source page:", result.source_website_url)
                print("Thumbnail:", result.thumbnail_url)
                print("Caption:", result.caption)
```

Each `image_result` object contains:

| Field | Description |
|---|---|
| `image_url` | Canonical URL of the image |
| `source_website_url` | The page where the image was found |
| `thumbnail_url` | Smaller preview URL, when available |
| `caption` | Short description of the image, when available |

`thumbnail_url` and `caption` are optional — they'll be `None` when the source page doesn't provide them. Check before using.

---

## What the Model Does With Image Results

The model receives the image metadata as structured content in the tool result, the same way it receives text result snippets. It can:

- Reference the image URLs in its response text
- Describe what the images show (based on the caption field)
- Select which images are most relevant to surface to the user
- Incorporate image URLs into markdown or HTML output

The model does not download or visually process the images during generation — it works from the metadata. If you need the model to *see* and interpret the image content, you would need to separately fetch the image and pass it as a vision input in a follow-up turn.

---

## `image_settings` Options

```python
"image_settings": {
    "max_results": 10,    # Maximum number of image results to return (default unspecified)
    "caption": True,      # Request caption text alongside image URLs
}
```

Both fields are optional. When `caption` is `False` or omitted, the `caption` field on results will be `None` even when the source provides one.

---

## Display Patterns

**Inline image grid in a chat interface:**
```python
image_results = [
    r for item in response.output
    if item.type == "web_search_call"
    for r in item.results
    if r.type == "image_result"
]

html_images = "".join(
    f'<a href="{r.source_website_url}"><img src="{r.thumbnail_url or r.image_url}" '
    f'alt="{r.caption or ""}"></a>'
    for r in image_results
    if r.image_url
)
```

**Passing image URLs back to the model for vision analysis:**
```python
# After retrieving image URLs, pass them back for visual interpretation
followup = client.responses.create(
    model="gpt-5.5",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Based on these search results, describe what you see."},
                *[
                    {"type": "image_url", "image_url": {"url": r.image_url}}
                    for r in image_results[:3]  # limit to 3 for context budget
                    if r.image_url
                ],
            ],
        }
    ],
)
```

---

## Use Cases

**Product research agents:** Retrieve current product photos alongside reviews and pricing — useful when catalog images are outdated or product isn't in your own database.

**Travel and places:** Ground destination recommendations with photos of landmarks, hotels, or neighborhoods, sourced from the current web rather than static assets.

**News and events:** Surface images from recent news coverage to accompany text summaries, giving users a visual anchor to breaking events.

**Technical documentation:** When answering questions about physical hardware, interface screenshots, or UI states that change over time, retrieve current screenshots rather than relying on static documentation images.

---

## What Image Search Does Not Provide

- **Image content analysis during search:** The model doesn't "see" the retrieved images while composing the initial response. It knows the URL, caption, and source page — not the visual content.
- **Filtered-by-visual-content search:** You can't search for "images where the sky is blue" — the underlying web search operates on indexed metadata and alt text, not visual similarity.
- **Guaranteed freshness:** Image search retrieves from the live web index, but the index may lag by hours to days for very recent events.
- **License information:** No licensing metadata is returned. Responsibility for rights review is on the caller.

---

## Combining Image and Text Results

When both content types are requested, image and text results appear in the same `item.results` list, distinguished by `result.type`:

```python
for item in response.output:
    if item.type == "web_search_call":
        text_results = [r for r in item.results if r.type == "text_result"]
        image_results = [r for r in item.results if r.type == "image_result"]

        print(f"Text results: {len(text_results)}")
        print(f"Image results: {len(image_results)}")
```

The ratio of text to image results in the response is determined by the model's search strategy and the web search index — it won't be a fixed split even when both types are enabled.
