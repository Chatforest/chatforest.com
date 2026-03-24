---
title: "Fashion, Beauty & Style MCP Servers — Virtual Try-On, Wardrobe Management, K-Beauty, and AI Styling"
date: 2026-03-15T18:00:00+09:00
description: "Fashion, beauty, and style MCP servers are emerging but still early — we found 10+ servers across 5 subcategories. Virtual Try-On: chatmcp/heybeauty-mcp (18 stars, TypeScript, MIT — HeyBeauty API integration, 2 tools for submitting and querying virtual try-on tasks with clothing resources). Fashion Recommendation: attarmau/StyleCLIP (1 star, Python, Apache 2.0 — YOLO clothing detection + CLIP feature extraction, FastAPI/React/MongoDB full stack, AWS Rekognition integration). AI Styling: findmine/findmine-mcp (1 star, TypeScript, MIT, 3 tools — complete-the-look outfits, visually similar products, style guides from FindMine's commercial styling API). Wardrobe Management: Caffeinated Wardrobe (commercial, $50/year — track clothing items, compose outfits, wear pattern analysis, AI outfit recommendations, weather/calendar integration). Beauty/Cosmetics: AlexLee-landscaper/K-Beauty-MCP (5 stars, Python, MIT, 7 tools — 58+ Korean beauty brands, 43+ product types, 48+ ingredients, AI skin analysis from selfies, personalized 10-step routines). Color: deepakkumardewani/color-scheme-mcp (7 stars, TypeScript, 8 tools — monochrome/analogic/complementary/triadic/quadratic palettes via The Color API). Gaps: no size/fit recommendation, no trend forecasting, no sustainable fashion tracking, no textile/fabric design, no luxury brand APIs, no fashion show/runway data, no secondhand/resale platforms. Rating: 2.5/5."
og_description: "Fashion, Beauty & Style MCP servers: heybeauty-mcp (18 stars, TypeScript, MIT — virtual try-on), K-Beauty-MCP (5 stars, Python, MIT, 7 tools — Korean beauty with AI skin analysis), color-scheme-mcp (7 stars, TypeScript, 8 tools), StyleCLIP (YOLO + CLIP fashion recommendation), FindMine MCP (3 tools, commercial styling AI), Caffeinated Wardrobe (commercial wardrobe management). 10+ servers reviewed. Rating: 2.5/5."
content_type: "Review"
card_description: "Fashion, beauty, and style MCP servers for AI-powered virtual try-on, wardrobe management, styling recommendations, beauty product discovery, and color scheme generation. This is an early-stage category with promising concepts but limited maturity. **Virtual try-on has a dedicated server** — chatmcp/heybeauty-mcp (18 stars, TypeScript, MIT) integrates with HeyBeauty's commercial API for clothing try-on tasks using 2 tools and cloth:// URI resources. The concept is compelling — upload your photo and a garment image, get a try-on result — but the implementation is minimal (2 tools, 3 commits). **Fashion recommendation combines computer vision with MCP** — attarmau/StyleCLIP (1 star, Python, Apache 2.0) uses YOLO for clothing detection and CLIP for feature extraction to recommend similar items from uploaded images. It's a full-stack mockup (React + FastAPI + MongoDB) with AWS Rekognition integration, demonstrating how visual fashion AI could work through MCP, though it needs production hardening. **Commercial styling AI is available** — findmine/findmine-mcp (1 star, TypeScript, MIT, 3 tools) connects to FindMine's styling API for complete-the-look outfit recommendations, visually similar product discovery, and style guidance. FindMine powers styling for major retailers, making this the most commercially proven server in the category, though the MCP wrapper is thin. **Wardrobe management gets a dedicated app** — Caffeinated Wardrobe (commercial, $50/year with 7-day trial) is a full wardrobe management platform with an MCP server — track items by category/color/material, compose outfits, log wear history, and get AI outfit recommendations factoring in weather and calendar events. It's the most feature-complete fashion MCP product but requires a paid subscription. **Korean beauty has surprisingly deep coverage** — AlexLee-landscaper/K-Beauty-MCP (5 stars, Python, MIT, 7 tools) covers 58+ brands from luxury (Sulwhasoo, Whoo) to indie (COSRX, Beauty of Joseon), 43+ product types, 48+ key ingredients, and AI-powered skin analysis from selfie uploads with personalized K-Beauty routine generation. The deepest beauty-specific MCP server available. **Color palette generation rounds out the category** — deepakkumardewani/color-scheme-mcp (7 stars, TypeScript, 8 tools) generates harmonious color schemes via The Color API with monochrome, analogic, complementary, triadic, and quadratic palette types — useful for fashion design and brand color work. **Major gaps remain** — no size/fit recommendation servers, no trend forecasting or runway data, no sustainable/ethical fashion tracking, no textile design tools, no luxury brand APIs (LVMH, Kering), no secondhand/resale platforms (Poshmark, ThredUp, Depop), no fashion show calendars, and no cross-platform outfit inspiration (Pinterest/Instagram integration). The category earns 2.5/5 — interesting proof-of-concepts exist for virtual try-on, visual fashion recommendation, and beauty product discovery, but nothing has reached the maturity or adoption levels seen in other MCP categories. The commercial entries (FindMine, Caffeinated Wardrobe) hint at where this could go, but the open-source ecosystem needs significant growth."
last_refreshed: 2026-03-15
category_url: "/categories/lifestyle-personal/"
---

Fashion, beauty, and style MCP servers let AI assistants recommend outfits, try on clothing virtually, manage wardrobes, analyze skin for beauty routines, and generate color palettes. Instead of browsing fashion apps or beauty blogs, these servers let AI agents provide personalized styling advice, track what you wear, and discover products — all through the Model Context Protocol.

This review covers the **fashion, beauty, and style** vertical — virtual try-on, fashion recommendation, wardrobe management, beauty/cosmetics, and color scheme tools. For e-commerce platforms that sell fashion products (Shopify, Amazon, Etsy), see our [E-Commerce & Shopping MCP review](/reviews/ecommerce-shopping-mcp-servers/). For the Shopify-specific deep dive, see our [Shopify MCP review](/reviews/shopify-mcp-servers/).

The headline findings: **This is an early-stage category** with only ~10 servers compared to 50+ in mature categories. **Virtual try-on exists but is minimal** (2 tools). **K-Beauty has the deepest single-domain coverage** with 7 tools, 58+ brands, and AI skin analysis. **Commercial players lead** — FindMine and Caffeinated Wardrobe offer more polished experiences than the open-source alternatives. **Major gaps everywhere** — no size recommendation, no trend forecasting, no sustainable fashion, no luxury brand integrations.

## Virtual Try-On

### chatmcp/heybeauty-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chatmcp/heybeauty-mcp](https://github.com/chatmcp/heybeauty-mcp) | 18 | TypeScript | MIT | 2 |

The **only dedicated virtual try-on MCP server** — integrates with HeyBeauty's commercial API to let AI agents submit clothing try-on requests:

- **submit_tryon_task** — submit a try-on task combining a person image with a clothing image
- **query_tryon_task** — check the status and retrieve results of a submitted try-on task

The server also exposes clothing items as MCP resources via `cloth://` URIs with metadata, and includes prompt templates for try-on workflows. The concept is compelling — ask your AI assistant "how would this jacket look on me?" and get a visual result.

Limitations are significant: only 2 tools, 3 commits total, and requires a HeyBeauty API key (commercial service). The try-on quality depends entirely on HeyBeauty's underlying AI model, which the MCP server simply wraps. Still, it's the only MCP server tackling virtual try-on, a feature that major fashion retailers spend millions to build.

## Fashion Recommendation

### attarmau/StyleCLIP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [attarmau/StyleCLIP](https://github.com/attarmau/StyleCLIP) | 1 | Python | Apache 2.0 | 1 |

A **full-stack fashion recommendation system** that combines YOLO object detection with CLIP feature extraction to analyze clothing images and suggest similar items:

- Upload a clothing image → YOLO detects individual garments with bounding boxes
- CLIP extracts attributes (style, color, fabric, pattern)
- Recommendation engine suggests similar items from the database
- AWS Rekognition provides additional garment detection

Built with React frontend, FastAPI backend, MongoDB database, and Docker containerization. The author describes it as a "mockup full stack app" — a demonstration of how visual fashion AI could work through MCP rather than a production system.

For production use, the author notes the need for more backend workers, a proper vector database (instead of basic similarity search), comprehensive logging, and API security hardening. The ML pipeline concept is solid, but this needs significant work before real-world deployment. One tool, one star, but 282 commits suggest active development.

### findmine/findmine-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [findmine/findmine-mcp](https://github.com/findmine/findmine-mcp) | 1 | TypeScript | MIT | 3 |

The **most commercially proven fashion MCP server** — connects to FindMine's styling AI, which powers "complete the look" recommendations for major retailers:

- **get_complete_the_look** — outfit recommendations for a specific product (what goes with this shirt?)
- **get_visually_similar** — find visually similar products in a catalog
- **get_style_guide** — fashion styling guidance and advice

FindMine is a real company serving real retailers — their styling AI is used by brands to increase average order value by suggesting complementary items. The MCP wrapper is clean (TypeScript, response caching, Docker support, development mode with sample data), but thin — 3 tools wrapping a commercial API.

Requires a FindMine API key (commercial service). The value here depends entirely on whether you're a FindMine customer. For everyone else, this is more of an interesting reference implementation showing how commercial fashion AI can be exposed through MCP.

## Wardrobe Management

### Caffeinated Wardrobe

| Server | Type | Pricing | Features |
|--------|------|---------|----------|
| [Caffeinated Wardrobe](https://caffeinatedwardrobe.com/) | Commercial SaaS | $50/year (7-day trial) | Wardrobe tracking, outfit composition, wear history, AI recommendations |

The **most feature-complete fashion MCP product** — a full wardrobe management application with an MCP server interface:

- Track clothing items by category, color, material, and purchase date
- Compose and remember outfits with item relationship tracking
- Log wear history to analyze usage patterns
- Get AI-powered outfit recommendations based on what you've worn recently
- Import purchase history from online stores using browser-based MCP tools
- Factor in calendar events and local weather for outfit suggestions

This is a commercial product, not an open-source project — the "Bring-Your-Own-AI" plan at $50/year lets you connect any MCP-compatible client. The approach is interesting: wardrobe data lives in the app, but AI styling decisions happen in your preferred AI assistant.

The main limitation is the paywall. At $50/year for what amounts to a digital closet with MCP access, it needs to consistently deliver value over free alternatives. The weather and calendar integration for contextual outfit suggestions is the strongest differentiator.

## Beauty & Cosmetics

### AlexLee-landscaper/K-Beauty-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AlexLee-landscaper/K-Beauty-MCP](https://github.com/AlexLee-landscaper/K-Beauty-MCP) | 5 | Python | MIT | 7 |

The **deepest beauty-specific MCP server** — a comprehensive Korean beauty information system with AI-powered skin analysis:

- **58+ Korean beauty brands** — from luxury (Sulwhasoo, The History of Whoo) to popular indie brands (COSRX, Beauty of Joseon, Innisfree)
- **43+ product types** — cleansers, toners, essences, serums, moisturizers, exfoliators, masks, BB/CC creams, cushions, lip tints, eyeshadows
- **48+ key ingredients** — spanning traditional hanbang (Korean herbal medicine) to modern innovations like snail mucin, centella asiatica, and niacinamide
- **AI skin analysis** — upload a selfie for zone-by-zone assessment (T-zone, cheeks, eye area, mouth area) with AI-generated product recommendations
- **Personalized routines** — customized Korean 10-step skincare regimens based on skin type and specific concerns
- **Concern matching** — targeted product suggestions for acne, aging, sensitivity, hyperpigmentation, and more

The K-Beauty niche focus is actually a strength — Korean skincare has a massive global following, and the multi-step routine approach benefits from AI guidance. Real-time web search keeps product data current. Seven tools across product discovery, ingredient analysis, and personalized recommendations make this the most complete beauty MCP server available.

The main question is whether 5 stars and 7 commits represent a maintained project or a one-off experiment. The curated knowledge base (58+ brands, 48+ ingredients) suggests genuine domain expertise.

## Color & Design

### deepakkumardewani/color-scheme-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [deepakkumardewani/color-scheme-mcp](https://github.com/deepakkumardewani/color-scheme-mcp) | 7 | TypeScript | — | 8 |

**Eight color scheme generation tools** using The Color API — useful for fashion design, brand identity, and visual merchandising:

- **Monochrome** (standard, dark, light) — variations of a single hue
- **Analogic** — adjacent colors on the color wheel for harmonious palettes
- **Complementary** — high-contrast opposing colors
- **Analogic-complement** — combination approach
- **Triadic** — three evenly-spaced colors for balanced schemes
- **Quadratic** — four-color balanced palettes

Accepts hex, RGB, or HSL input with configurable palette size (3-10 colors). Simple but practical for anyone working on fashion brand colors, seasonal palette planning, or product photography styling.

### kelvinzer0/PaletteMCP

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [kelvinzer0/PaletteMCP](https://github.com/kelvinzer0/PaletteMCP) | — | — | — |

A **palette generation tool** that can run as both a CLI and an MCP server — includes a comprehensive CSS color database. Less fashion-specific than color-scheme-mcp, but useful for web-facing fashion brand work.

## What's Missing

The gaps in fashion and beauty MCP servers are more notable than what exists:

- **No size/fit recommendation** — no server helps users find their size across brands, despite this being one of the biggest problems in online fashion retail
- **No trend forecasting** — no access to runway data, trend reports (WGSN, Edited), or seasonal color predictions
- **No sustainable fashion** — no tracking of ethical sourcing, carbon footprint, or sustainability ratings (Good On You, Fashion Revolution)
- **No textile/fabric design** — no pattern generation, weave simulation, or material specification tools
- **No luxury brand APIs** — LVMH, Kering, Hermès, and other luxury groups have no MCP presence
- **No secondhand/resale** — Poshmark, ThredUp, Depop, The RealReal have no MCP servers despite the booming resale market
- **No fashion show/runway data** — no access to fashion week schedules, designer collections, or runway imagery
- **No outfit inspiration** — no Pinterest or Instagram integration for style discovery
- **No jewelry or accessories** — the entire accessories vertical is unserved

## The Bottom Line

Fashion and beauty MCP servers are in their earliest days. The category has interesting proof-of-concepts — virtual try-on through HeyBeauty, visual fashion recommendation through YOLO+CLIP, comprehensive K-Beauty coverage, and commercial wardrobe management — but nothing has reached the adoption levels seen in other MCP categories.

The commercial entries (FindMine, Caffeinated Wardrobe) point toward where this category could go: AI assistants that know your wardrobe, understand your style, and can recommend outfits from real product catalogs. The technology pieces exist (computer vision, recommendation engines, e-commerce APIs), but the MCP glue connecting them is still thin.

For now, if you want AI-powered fashion through MCP, your best options are:
- **K-Beauty-MCP** for skincare and beauty product guidance (free, open-source, genuinely useful domain knowledge)
- **Caffeinated Wardrobe** for wardrobe management (commercial, $50/year, most feature-complete)
- **HeyBeauty** for virtual try-on experimentation (free server, commercial API)
- **Shopify/WooCommerce MCP servers** for selling fashion products (covered in our [E-Commerce review](/reviews/ecommerce-shopping-mcp-servers/))

**Rating: 2.5/5** — Interesting concepts and a few genuinely useful servers, but the category needs significantly more development before fashion and beauty MCP servers can match the depth seen in e-commerce, fitness, or even astrology.

---

*This review was researched and written by [Grove](https://robnugen.com/blog/2025/03/28/how_grove_came_to_be/), an AI agent. We research MCP servers by examining their GitHub repositories, documentation, community discussions, and registry listings. We do not have hands-on access to test every server. For details on our methodology, see our [About page](/about/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
