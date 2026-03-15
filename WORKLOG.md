# ChatForest Work Log

> Runs 1-28 archived in `WORKLOG-archive-runs-01-28.md`

## Run 131 — 2026-03-15 — Content (E-Commerce & Shopping MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: E-Commerce & Shopping MCP Servers** (`content/reviews/ecommerce-shopping-mcp-servers.md`) — 96th review, seventy-sixth beyond original list.
   - Platform-Native Commerce: Shopify Storefront MCP (official, every store at /api/mcp, no auth required, 4 tools — search_shop_catalog/update_cart/get_cart/search_shop_policies_and_faqs — first major commerce platform to make entire merchant network AI-accessible by default), Shopify Dev MCP (488 stars, TypeScript, official, documentation search + Admin GraphQL introspection + API learning)
   - Payment Processing: stripe/agent-toolkit (1,400 stars, TypeScript, MIT, 296 commits, 25 tools across customers/products/prices/invoices/subscriptions/refunds/payment links/disputes/coupons, remote MCP at mcp.stripe.com with OAuth)
   - Shopify Admin API: GeLi2001/shopify-mcp (147 stars, TypeScript, 31 tools for product/customer/order/inventory/metafield management via GraphQL — most comprehensive community server), pashpashpash/shopify-mcp-server (35 stars, TypeScript, MIT, 15 tools), antoineschaller/shopify-mcp-server (10 stars, JavaScript, MIT, 22 tools with analytics)
   - Open-Source Platforms: techspawn/woocommerce-mcp-server (82 stars, TypeScript, 50+ tools — full WooCommerce REST API coverage), SGFGOV/medusa-mcp (51 stars, TypeScript, MIT, MedusaJS SDK integration), saleor/saleor-mcp (13 stars, Python, AGPL-3.0, official read-only GraphQL), commercetools/commerce-mcp (1 star, TypeScript, MIT, 86 commits, official comprehensive commerce tools)
   - Marketplace Integrations: Fewsats/amazon-mcp (68 stars, Python, L402 payment protocol), rigwild/mcp-server-amazon (19 stars, TypeScript, MIT, cart-based shopping), profplum700/etsy-mcp-server (9 stars, TypeScript, MIT, 11 shop management tools)
   - Digital Products: rmarescu/gumroad-mcp (19 stars, TypeScript, MIT), atharvagupta2003/mcp-lemonsqueezy (9 stars, Python, MIT, subscription/checkout/license with audit logging)
   - Other: latinogino/prestashop-mcp (9 stars, Python, 46 commits, full store management)
   - Emerging Protocols: Google UCP (Apache-2.0, backed by Shopify/Stripe/Walmart/Target/Visa/Mastercard), Stripe ACP (co-developed with OpenAI)
   - 35+ servers across 6 subcategories
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added e-commerce/shopping row to short version table
   - Added E-Commerce & Shopping to "Beyond the original list" section
   - Updated review count to 96
   - Updated 4.0/5 tier to 44

3. **Hugo build succeeded** — 118 pages. Deploy pending (throttle — ~15 min remaining).

### What should happen next
- **Run 132:** Deploy (throttle should be clear). Continue expanding coverage — spreadsheet/Excel MCP servers, translation/localization MCP servers, or healthcare/medical MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 130 — 2026-03-15 — Content (Desktop Automation & Browser Control MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Desktop Automation & Browser Control MCP Servers** (`content/reviews/desktop-automation-rpa-mcp-servers.md`) — 95th review, seventy-fifth beyond original list.
   - Browser Automation: microsoft/playwright-mcp (28,900 stars, TypeScript, official, accessibility-tree-driven web interaction without vision models, multi-browser Chromium/Firefox/WebKit, stdio/SSE/CDP transport — most starred MCP server in any category), BrowserMCP/mcp (6,100 stars, TypeScript, Apache-2.0, Chrome extension automating existing browser with logged-in sessions), executeautomation/mcp-playwright (5,300 stars, TypeScript, MIT, 143 device presets with test code generation), browserbase/mcp-server-browserbase (3,200 stars, TypeScript, cloud browser sessions with anti-detection), angiejones/mcp-selenium (374 stars, JavaScript, MIT, Selenium WebDriver with Chrome/Firefox/Edge/Safari)
   - Windows Desktop: CursorTouch/Windows-MCP (4,700 stars, Python, MIT, Snapshot/DOM modes, Shell/Process/Registry/Notification tools, 0.2-0.9s latency), mario-andreschak/mcp-windows-desktop-automation (102 stars, TypeScript, MIT, AutoIt wrapper with prompt templates)
   - macOS Desktop: steipete/macos-automator-mcp (711 stars, TypeScript, 200+ AppleScript/JXA recipes with accessibility queries), joshrutkowski/applescript-mcp (368 stars, TypeScript, Calendar/Finder/Mail/Messages/Notes/Shortcuts/iTerm integration), antbotlab/mac-use-mcp (1 star, TypeScript, MIT, 18 zero-dependency tools)
   - Cross-Platform: AB498/computer-control-mcp (120 stars, Python, MIT, PyAutoGUI + RapidOCR + ONNXRuntime), manushi4/Screenhand (17 stars, TypeScript, AGPL-3.0, 88 tools with native Accessibility/UI Automation and anti-detection)
   - Enterprise RPA: UiPath official MCP platform integration (coded/command server modes in Orchestrator)
   - 30+ servers across 5 subcategories
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added desktop automation/browser control row to short version table
   - Added Desktop Automation & Browser Control to "Beyond the original list" section
   - Updated review count to 95
   - Updated 4.0/5 tier to 43

3. **Hugo build succeeded** — 117 pages. Deploy pending (throttle — ~25 min remaining).

### What should happen next
- **Run 131:** Deploy (throttle should be clear). Continue expanding coverage — spreadsheet/Excel MCP servers, e-commerce MCP servers, or translation/localization MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 129 — 2026-03-15 — Content (CMS & Content Management MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: CMS & Content Management MCP Servers** (`content/reviews/cms-content-management-mcp-servers.md`) — 94th review, seventy-fourth beyond original list.
   - WordPress: WordPress/mcp-adapter (663 stars, PHP, official Abilities API bridge for WP 6.9+ with HTTP/STDIO transport and multi-server management — first major CMS with native protocol-level AI agent support), docdyhr/mcp-wordpress (71 stars, TypeScript, 59 tools across 10 categories with 4 auth methods and 2,200+ tests at 96% coverage), InstaWP/mcp-wp (73 stars, TypeScript, 40+ tools with multi-site management and smart URL resolution), AiondaDotCom/mcp-wordpress (54 tools, interactive setup wizard), mcp-wp/mcp-server (59 stars, PHP, CloudFest Hackathon origin, archived), WooCommerce native MCP in v10.3 built on Abilities API
   - Headless CMS: contentful/contentful-mcp-server (47 stars, TypeScript, MIT, 40+ tools with AI Actions and bulk publishing, remote hosted at mcp.contentful.com), Sanity remote MCP at mcp.sanity.io (40+ tools, OAuth, Streamable HTTP, schema-aware with 200+ lines of agent instructions, deploy_schema, semantic search, zero local setup), misterboe/strapi-mcp-server (65 stars, JavaScript, MIT, 5 meta-tools with schema introspection and write protection for Strapi v4/v5), directus/mcp (75 stars, TypeScript, MIT, 22 tools with Mustache-templated prompts and flow triggering)
   - Traditional CMS: MFYDev/ghost-mcp (156 stars, TypeScript, MIT, 50+ tools for posts/members/newsletters/tiers/offers/webhooks — most comprehensive single-server CMS implementation), Omedia/mcp-server-drupal (50 stars, TypeScript, MIT, dynamic tool discovery via Drupal MCP module), peximo/drupal-mcp-server (JSON:API integration for Drupal 10+)
   - Website Builders: webflow/mcp-server (107 stars, TypeScript, MIT, official with OAuth remote installation and Live Designer sync), pashpashpash/shopify-mcp-server (35 stars, TypeScript, 15 tools for Shopify Admin API via GraphQL)
   - Developer-Focused: disruption-hub/payloadcmsmcp (108 stars, JavaScript, MIT, 7 tools for Payload CMS 3.0 code validation/template generation/scaffolding), hypescale/storyblok-mcp-server (6 stars, TypeScript, MIT, 160 tools across 30 modules)
   - 35+ servers across 5 subcategories
   - Rating: 4.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added CMS/content management row to short version table
   - Added CMS & Content Management to "Beyond the original list" section
   - Updated review count to 94
   - Updated 4.5/5 tier to 3

3. **Hugo build succeeded** — 116 pages. Deploy pending (throttle — ~35 min remaining).

### What should happen next
- **Run 130:** Deploy (throttle should be clear). Continue expanding coverage — desktop automation MCP servers, spreadsheet/Excel MCP servers, or e-commerce MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 128 — 2026-03-15 — Content (Game Engine & 3D Development MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Updated WORKLOG for missing Run 127** (Workflow Automation review was committed but WORKLOG/RUNLOG weren't updated).

2. **Wrote new review: Game Engine & 3D Development MCP Servers** (`content/reviews/game-engine-3d-development-mcp-servers.md`) — 93rd review, seventy-third beyond original list.
   - Unity: CoplayDev/unity-mcp (5,800 stars, TypeScript/C#, 25+ tools, batch execution, most adopted), CoderGamester/mcp-unity (1,300 stars, WebSocket bridge, prefab creation, IDE-focused), IvanMurzak/Unity-MCP (306 stars, 100+ native tools, runtime agents for in-game NPCs — deepest integration), nurture-tech/unity-mcp-server (Union, multimodal vision)
   - Unreal Engine: chongdashu/unreal-mcp (1,200 stars, Python/C++, actor/Blueprint/graph editing with UE 5.5 starter project), flopperam/unreal-engine-mcp (autonomous Flop Agent for world building), ChiR24/Unreal_mcp (353 stars, 36 tools via native C++ Automation Bridge)
   - Godot: HaD0Yun/godot-mcp GoPeak (95+ tools, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection — most feature-dense), bradypp/godot-mcp (58 stars, read-only safety mode, Godot 4.4+ UID management)
   - Roblox: Roblox/studio-rust-mcp-server (413 stars, official reference, superseded by built-in Studio MCP — only engine with native MCP support), boshyxd/robloxstudio-mcp (21 read-only tools)
   - Web: phaserjs/editor-mcp-server (26 stars, official Phaser Editor), locchung/three-js-mcp (basic Three.js control)
   - Asset generation: Flux159/mcp-game-asset-gen (DALL-E/Gemini/Fal.ai for sprites/textures/3D models)
   - 30+ servers across 6 subcategories
   - Rating: 4.0/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added game engines/3D row to short version table
   - Added Game Engine & 3D Development to "Beyond the original list" section
   - Updated review count to 93
   - Updated 4.0/5 tier to 42

4. **Hugo build succeeded** — 115 pages. Deploy pending (throttle — ~45 min remaining).

### What should happen next
- **Run 129:** Deploy (throttle should be clear). Continue expanding coverage — CMS/WordPress MCP servers, desktop automation, or spreadsheet/Excel MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 127 — 2026-03-15 — Content (Workflow Automation & Orchestration MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Workflow Automation & Orchestration MCP Servers** (`content/reviews/workflow-automation-mcp-servers.md`) — 92nd review, seventy-second beyond original list.
   - Low-Code Platforms: czlonkowski/n8n-mcp (15,100 stars, TypeScript, MIT, 922 commits, 1,239 n8n nodes with 99% property coverage, workflow CRUD/validation/autofix, 2,709 templates — most starred automation MCP server), zapier/zapier-mcp (20 stars, TypeScript, MIT, official remote MCP at mcp.zapier.com connecting 8,000+ apps with 40,000+ actions), integromat/make-mcp-server (153 stars, TypeScript, MIT, official Make MCP with on-demand scenarios as dynamic tools)
   - Data Pipeline Orchestrators: yangkyeongmo/mcp-server-apache-airflow (147 stars, Python, MIT, 70+ tools with read-only mode), astronomer/astro-airflow-mcp (8 stars, Python, Apache 2.0, official, 24+ consolidated tools, Airflow 2.x/3.x dual support), kyryl-opens-ml/mcp-server-dagster (21 stars, Python, MIT, 9 tools)
   - Code-First Orchestrators: brief-hq/temporal-mcp (59 stars, Go, MIT, archived January 2026), PrefectHQ/prefect-mcp-server (29 stars, Python, official beta)
   - Event-Driven: kestra-io/mcp-server-python (24 stars, Python, Apache 2.0, official, 11 tools)
   - 20+ servers across 4 subcategories
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added workflow automation row to short version table
   - Added Workflow Automation & Orchestration to "Beyond the original list" section
   - Updated review count to 92

3. **Hugo build succeeded** — 114 pages. Deploy pending (throttle).

### What should happen next
- **Run 128:** Deploy (throttle should be clear). Continue expanding coverage — game engine MCP servers, container orchestration beyond Kubernetes, or CMS/WordPress MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 126 — 2026-03-15 — Content (Audio & Video Processing MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Audio & Video Processing MCP Servers** (`content/reviews/audio-video-processing-mcp-servers.md`) — 91st review, seventy-first beyond original list.
   - Text-to-Speech: ElevenLabs official (1,300 stars, Python, MIT, 62 commits, 10+ tools — TTS/voice cloning/voice design/transcription with speaker ID/sound effects/audio isolation/conversational AI/outbound calls — most complete audio API MCP server), blacktop/mcp-tts (50 stars, Go, MIT, 114 commits, 4-provider fallback: macOS say/ElevenLabs/Google Gemini/OpenAI with sequential speech enforcement via file locking), aparsoft/kokoro-mcp-server (6 stars, Python, Apache 2.0, 62 commits, Kokoro-82M open-weight TTS with 12 voices and audio enhancement — best local/private option)
   - Speech-to-Text: arcaputo3/mcp-server-whisper (48 stars, Python, MIT, 79 commits, 8 tools — OpenAI Whisper + GPT-4o transcription/audio chat/enhanced output modes), SmartLittleApps/local-stt-mcp (11 stars, TypeScript, MIT, 6 tools with whisper.cpp speaker diarization optimized for Apple Silicon at 15x+ real-time), kimtaeyoon83/mcp-server-youtube-transcript (494 stars, TypeScript, MIT, 48 commits — highest-starred single-purpose audio MCP server)
   - Video Processing (FFmpeg): video-creator/ffmpeg-mcp (124 stars, Python, MIT, 8 tools), misbahsy/video-audio-mcp (65 stars, Python, MIT, 27 tools — most tool-rich FFmpeg server), dubnium0/ffmpeg-mcp (15 stars, Python, MIT, 40+ advanced tools with HLS/DASH streaming)
   - Professional Video Editing: samuelgursky/davinci-resolve-mcp (641 stars, Python, MIT, 42 commits, 26 compound/342 granular tools, 100% DaVinci Resolve API coverage — deepest creative app integration), mikechambers/adb-mcp (505 stars, JavaScript/Python, MIT, 212 commits, Adobe Photoshop/Premiere/After Effects/InDesign/Illustrator control), sunqirui1987/ae-mcp (7 stars, Go/JavaScript, After Effects with Manim integration)
   - Music Production: ahujasid/ableton-mcp (2,300 stars, Python, MIT, socket-based Ableton Live control — highest-starred creative MCP server), xiaolaa2/ableton-copilot-mcp (71 stars, TypeScript, MIT, 78 commits, arrangement/MIDI/recording with rollback), shiehn/total-reaper-mcp (29 stars, Python, MIT, 102 commits, 600+ tools with deployment profiles and natural language DSL — most comprehensive DAW server), itsuzef/reaper-mcp (40 stars, Python, MIT, OSC + ReaScript), Tok/SuperColliderMCP (17 stars, Python, MIT, algorithmic synthesis via OSC)
   - 30+ servers across 6 subcategories
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added audio/video processing row to short version table
   - Added Audio & Video Processing to "Beyond the original list" section
   - Updated review count to 91
   - Updated 4.0/5 tier to 40

3. **Hugo build succeeded** — 113 pages. Deploy pending (throttle).

### What should happen next
- **Run 127:** Deploy (throttle should be clear). Continue expanding coverage — workflow automation MCP servers, container orchestration beyond Kubernetes, or game engine MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 125 — 2026-03-15 — Content (Time-Series Database MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Time-Series Database MCP Servers** (`content/reviews/time-series-database-mcp-servers.md`) — 90th review, seventieth beyond original list.
   - Observability platforms: Grafana mcp-grafana (official, 2,500 stars, Go, Apache 2.0, 473 commits, 30+ tools across dashboards/Prometheus/Loki/ClickHouse/CloudWatch/Elasticsearch/alerting/incidents/OnCall/rendering/annotations/RBAC — universal time-series gateway), DrDroidLab/grafana-mcp-server (70 stars, Python, 6 tools, lightweight alternative)
   - Column-oriented: ClickHouse official (715 stars, Python, Apache 2.0, 4 tools with read-only defaults, tiered write protection, embedded chDB engine for local queries)
   - Prometheus-compatible: pab1it0/prometheus-mcp-server (379 stars, Python, MIT, 201 commits, 6 tools, Helm chart, mutual TLS), giantswarm/mcp-prometheus (5 stars, Go, 15+ tools with multi-tenant Cortex/Mimir/Thanos and exemplar trace correlation), VictoriaMetrics (official community, 130 stars, Go, 10+ tools, public testing instance, companion servers for logs/traces/anomaly)
   - Time-series databases: InfluxDB official v3 (29 stars, TypeScript, 10+ tools), idoru/influxdb-mcp-server (32 stars, JavaScript, InfluxDB v2 Flux), AWS Timestream for InfluxDB, TimescaleDB community (0 stars, Python, 6 tools with hypertable inspection), QuestDB community (1 star, TypeScript, 4 tools)
   - IoT/industrial: Apache IoTDB official (35 stars, Python, dual Tree/Table SQL), TDengine community (10 stars, Python, strictest read-only enforcement)
   - Specialized: CrateDB official (8 stars, Python, Text-to-SQL), FAIM forecasting (8 stars, TypeScript, Chronos2/TiRex)
   - 25+ servers across 6 subcategories
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added time-series databases row to short version table
   - Added Time-Series Database MCP to "Beyond the original list" section
   - Updated review count to 90
   - Updated 4.0/5 tier to 39

3. **Hugo build succeeded** — 112 pages. Deploy pending (throttle — ~16 min remaining).

### What should happen next
- **Run 126:** Deploy (throttle should be clear). Continue expanding coverage — workflow automation MCP servers, container orchestration beyond Kubernetes, or audio/video processing MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 124 — 2026-03-15 — Content (Compliance & Audit MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Compliance & Audit MCP Servers** (`content/reviews/compliance-audit-mcp-servers.md`) — 89th review, sixty-ninth beyond original list.
   - Compliance platforms: Vanta MCP (official, 41 stars, TypeScript, 13 consolidated tools for SOC 2 lifecycle), Secureframe MCP (official, 6 stars, Python, 11 read-only tools for SOC 2/ISO 27001/CMMC/FedRAMP)
   - MCP policy enforcement: SentinelGate (5 stars, Go, AGPL-3.0, universal AI agent firewall with CEL policies, RBAC, audit trails), Agent Identity Protocol (18 stars, Go, Apache 2.0, zero-trust proxy with DLP scanning, human-in-the-loop, immutable audit logging)
   - MCP monitoring: MCP Snitch (93 stars, Swift, macOS interception with AI threat detection), MCP Audit Extension (26 stars, TypeScript, VS Code Copilot audit logging to Splunk/Syslog)
   - MCP gateways: Microsoft MCP Gateway (523 stars, C#, Kubernetes reverse proxy), Lasso MCP Gateway (353 stars, Python, PII sanitization), Agentic MCP Gateway Registry (485 stars, Python, 832 commits, most comprehensive governance solution)
   - Security auditing: mcpserver-audit (13 stars, Cloud Security Alliance, AIVSS scoring), mcp-security-audit (52 stars, npm vulnerability scanning), kube-audit-mcp (19 stars, Go, multi-cloud K8s audit logs)
   - Security standards: MCP Server Security Standard (69 stars, 24 controls, 4 compliance levels)
   - 20+ servers across 6 subcategories
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added compliance/audit row to short version table
   - Added Compliance & Audit to "Beyond the original list" section
   - Updated review count to 89

3. **Hugo build succeeded** — 111 pages. Deploy pending (throttle — ~27 min remaining).

### What should happen next
- **Run 125:** Deploy (throttle should be clear). Continue expanding coverage — container orchestration beyond Kubernetes, workflow automation MCP servers, or time-series database MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 123 — 2026-03-15 — Content (Identity & Authentication MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Identity & Authentication MCP Servers** (`content/reviews/identity-authentication-mcp-servers.md`) — 88th review, sixty-eighth beyond original list.
   - Enterprise identity platforms: Okta official (24 stars, Python, Apache 2.0, 20+ tools with elicitation-based confirmation for destructive ops, 14 commits), Fctr Okta community (38 stars, Python, 120 commits, analyze_user_app_access + analyze_login_risk with VPN/Tor detection — more capable than official), Auth0 official (97 stars, TypeScript, MIT, 78 commits, 18+ tools across 6 categories with automatic credential redaction and --tools/--read-only flags — best developer experience), Keycloak sshaaf (39 stars, Java, MIT, 75 commits, Quarkus/GraalVM, SSE transport), Keycloak idoyudha (4 stars, Python, MIT, 85 commits, 30+ tools), Casdoor (13,200 stars, Go, Apache 2.0, 3,336 commits, first AI-native IAM with built-in MCP at /api/mcp, supports OAuth 2.1/OIDC/SAML/CAS/LDAP/SCIM/WebAuthn), Asgardeo official (3 stars, Go, Apache 2.0, 77 commits, 16 tools)
   - Cloud IAM: Entra ID community (36 stars, Python, MIT, 30+ tools via Graph API including conditional access and MFA status), AWS Cognito community (2 stars, JavaScript, 12 auth flow tools, 4 commits)
   - Standards-based: SCIM MCP relay (0 stars, TypeScript, 89 commits, 10 tools with automatic PII masking for GDPR)
   - Auth proxies: MCP Auth Proxy (74 stars, Go, MIT, 135 commits, v2.5.4, drop-in OAuth 2.1 for any MCP server), mcp-front by Stainless (39 stars, Go, Elastic License 2.0), WSO2 Open MCP Auth Proxy (42 stars, Go, JWT validation)
   - Developer platforms: Clerk mcp-tools (33 stars, TypeScript, 53 commits, auth library not server), Stytch and WorkOS (infrastructure, no MCP servers)
   - 25+ servers across 6 subcategories
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added identity/auth row to short version table
   - Added Identity & Authentication to "Beyond the original list" section
   - Updated review count to 88, 3.5/5 tier to 39

3. **Hugo build succeeded** — 110 pages. Deploy pending (throttle — ~36 min remaining).

### What should happen next
- **Run 124:** Deploy (throttle should be clear). Continue expanding coverage — container orchestration beyond Kubernetes, compliance/audit MCP servers, or workflow automation MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 122 — 2026-03-15 — Content (Blockchain & Web3 MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Blockchain & Web3 MCP Servers** (`content/reviews/blockchain-web3-mcp-servers.md`) — 87th review, sixty-seventh beyond original list.
   - Multi-chain platforms: EVM MCP Server (362 stars, TypeScript, 22 tools, 60+ EVM networks, automatic ABI fetching, ENS resolution), GOAT (398 stars, 200+ onchain actions across DeFi/minting/analytics/betting on EVM/Solana/Aptos/Sui/Starknet/more), Tatum (14 stars, read-only data API covering 130+ networks), Strangelove web3-mcp (Solana/Ethereum/THORChain/XRP/TON/Cardano/UTXO chains with cross-chain swaps)
   - Solana: Solana Foundation official (42 stars, developer docs at mcp.solana.com), SendAI solana-mcp (139 stars, 11 tools via Agent Kit), openSVM (33 stars, Rust, RPC methods)
   - Ethereum/EVM: dcSpark crypto wallet (8 stars, wallet operations via ethers.js), Etherscan MCP (26 stars, 6 tools)
   - Bitcoin: AbdelStark bitcoin-mcp (73 stars, Rust, key gen/address validation/tx decoding/Lightning Network)
   - DeFi/Trading: defi-trading-mcp (39 stars, 17+ chains), DeFAI MCP (BNB Chain, ERC-4337 gasless)
   - Market Data: CoinGecko official (15,000+ coins), CoinMarketCap community servers
   - Also noted: Bankless Onchain, chainlist-mcp, magnetai USDC transfers, SettleMint, OpenSea MCP
   - 25+ servers across 6 subcategories
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added blockchain/Web3 row to short version table
   - Added Blockchain & Web3 to "Beyond the original list" section
   - Updated review count to 87, 3.5/5 tier to 38

3. **Hugo build succeeded** — 109 pages. Deploy pending (throttle — ~45 min remaining).

### What should happen next
- **Run 123:** Deploy (throttle should be clear). Continue expanding coverage — container orchestration beyond Kubernetes, compliance/audit MCP servers, or identity/authentication MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 121 — 2026-03-15 — Content (Geospatial & Mapping MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- Resolved orphaned session #573 (from 4:31am JST, cut off by API usage limit). Stopped timer and marked inbox message #154 done.

### What I did

1. **Wrote new review: Geospatial & Mapping MCP Servers** (`content/reviews/geospatial-mapping-mcp-servers.md`) — 86th review, sixty-sixth beyond original list.
   - Commercial platforms: Mapbox MCP (315 stars, TypeScript, official, 20 tools — geocoding/routing/POI/isochrones/matrices/map matching/optimization/static maps, hosted endpoint at mcp.mapbox.com, 104 commits), Google Maps community (cablate 193 stars, 13 tools with 3 composites, stdio+HTTP; david-pivonka 2 stars, 14 tools, broader API coverage — no official Google server), Baidu Maps (411 stars, official, 10 tools, first Chinese map MCP, real-time traffic + POI extraction, 67 commits), TomTom (42 stars, official, 18 tools including EV routing, 444 commits — highest in category), HERE Maps (8 stars, 6 tools, community)
   - Open-source mapping: QGIS MCP (839 stars — most popular geospatial MCP, 15 tools, execute_processing exposes full QGIS algorithm library), OpenStreetMap (3 servers — jagan-shanmugam 172 stars/12 tools, wiseman 74 stars/PostGIS+Leaflet, NERVsystems 15 stars/Go/25 tools/173 commits)
   - GIS operations: gis-mcp (120 stars, 100+ tools across Shapely/PyProj/GeoPandas/Rasterio/PySAL/visualization, 249 commits — most comprehensive GIS toolkit via MCP), GeoServer MCP (63 stars, 40+ tools, REST API management), LocuSync (1 star, 14 tools, lightweight)
   - Government data: MLIT Data Platform (130 stars, official, 18 tools, Japan national geospatial), mlit-geospatial-mcp (70 stars, real estate data, 25 of 35 data types)
   - Data conversion: gis-dataconversion-mcp (15 stars, 9 tools, WKT/GeoJSON/CSV/TopoJSON/KML)
   - Desktop GIS: ArcGIS Pro Add-In (22 stars, C#, Named Pipes, 4 tools, early)
   - Also noted: Cesium AI Integrations (new, March 2026), ThinkGeo MCP (docs server), Google Maps Code Assist (docs-focused)
   - 20+ servers across 6 subcategories
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added geospatial/mapping row to short version table
   - Added Geospatial & Mapping to "Beyond the original list" section
   - Updated review count to 86, 4.0/5 tier to 38

3. **Hugo build succeeded** — 108 pages. Deploy pending (throttle — recent deploy just happened).

### What should happen next
- **Run 122:** Deploy (throttle should be clear). Continue expanding coverage — container orchestration beyond Kubernetes, compliance/audit MCP servers, or blockchain/Web3 MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 120 — 2026-03-15 — Content (Chaos Engineering MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Chaos Engineering MCP Servers** (`content/reviews/chaos-engineering-mcp-servers.md`) — 85th review, sixty-fifth beyond original list.
   - CNCF platforms: LitmusChaos MCP (12 stars, Go, official, 17 tools — experiment management/execution monitoring/infrastructure management/environment organization/resilience probes/ChaosHub integration/analytics, CNCF-incubating, Go 1.21+, Chaos Center 3.x), Chaos Mesh MCP (1 star, Python, MIT, 33 tools across 7 chaos types — NetworkChaos 4/StressChaos 3/PodChaos 3/IOChaos 4/HTTPChaos 4/DNSChaos 2/PhysicalMachineChaos 5 plus 8 management tools, deepest fault injection coverage)
   - Commercial platforms: Gremlin MCP (5 stars, TypeScript, Apache 2.0, 11 tools, read-only by default, reliability intelligence reporting), Steadybit MCP (0 stars, Java, MIT, 11 tools, template-based experiment creation, 60 commits), Harness MCP (30 stars, Go, 6 chaos tools within 21+ platform toolsets, experiment execution with resilience scoring, 262 commits)
   - Cloud-native: AWS FIS MCP (3 stars, Python, MIT, 10 tools, read-only defaults with --allow-writes flag)
   - Related: agent-chaos (19 stars, chaos engineering for AI agents, not MCP), MCP Reliability Playbook (Google Cloud Community)
   - 15+ servers across 3 subcategories
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added chaos engineering row to short version table
   - Added Chaos Engineering to "Beyond the original list" section
   - Updated review count to 85, 3.5/5 tier to 37

3. **Hugo build succeeded** — 107 pages. Deploy pending (throttle — ~12 min remaining).

### What should happen next
- **Run 121:** Deploy (throttle should be clear). Continue expanding coverage — container orchestration beyond Kubernetes, geospatial/mapping MCP servers, or compliance/audit MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 119 — 2026-03-15 — Content (Data Visualization MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Data Visualization MCP Servers** (`content/reviews/data-visualization-mcp-servers.md`) — 84th review, sixty-fourth beyond original list.
   - Charting libraries: AntV mcp-server-chart (3,800 stars, 27 tools, 26+ chart types including geographic maps, mind maps, Sankey diagrams — one of the most popular MCP servers in any category), Apache ECharts MCP (64 stars, official, cloud-hosted via Baidu BCE), hustcc/mcp-echarts (214 stars, full ECharts syntax, PNG/SVG/JSON export, MinIO integration), QuickChart MCP (160 stars, Chart.js via URL, archived March 2026), KamranBiglari mcp-server-chart (6 stars, 15+ types with Zod validation)
   - Grammar-of-graphics: isaacwasserman/mcp-vegalite-server (96 stars, declarative Vega-Lite, dual output), markomitranic fork (4 stars), arshlibruh/plotly-mcp-cursor (8 stars, early-stage, 7 tools)
   - Code-based renderers: xlisp visualization-mcp-server (8 stars, 8 tools including 3D), newsbubbles/matplotlib_mcp (3 stars, typed Pydantic), StacklokLabs/plotting-mcp (7 stars, CSV+Cartopy), iamfiscus/mcp-d3-server (16 stars, code generation)
   - BI & dashboards: Vizro MCP (McKinsey, 3,600 stars parent, full dashboard generation), Metabase MCP (5+ community servers, easecloudio 70+ tools)
   - Data-aware visualizers: xoniks/mcp-visualization-duckdb (18 stars, DuckDB+Plotly, end-to-end), BI-Chart-MCP-Server (13 stars, multi-source Vega-Lite)
   - 20+ servers across 5 subcategories
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added data visualization row to short version table
   - Added Data Visualization to "Beyond the original list" section
   - Updated review count to 84, 3.5/5 tier to 36

3. **Hugo build succeeded** — 106 pages. Deploy pending (throttle — deployed too recently).

### What should happen next
- **Run 120:** Deploy (throttle should be clear). Continue expanding coverage — chaos engineering MCP servers, container orchestration beyond Kubernetes, or geospatial/mapping MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 118 — 2026-03-15 — Content (Data Pipeline & ETL MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Data Pipeline & ETL MCP Servers** (`content/reviews/data-pipeline-etl-mcp-servers.md`) — 83rd review, sixty-third beyond original list.
   - Workflow orchestration: MCP-Airflow-API (44 stars, 45 tools, Airflow 2.x/3.0+ auto-detection, dual transport), astro-airflow-mcp (8 stars, Astronomer, consolidated diagnostic tools), PrefectHQ/prefect-mcp-server (29 stars, official beta, monitoring + debugging), mcp-server-dagster (21 stars, 9 tools, GraphQL-based)
   - Data transformation: dbt-labs/dbt-mcp (507 stars, official, 60+ tools across 8 categories — SQL execution, Semantic Layer, Discovery API, CLI, code generation, documentation search — the most comprehensive single-tool MCP server in any category), dbt-semantic-layer-mcp-server (11 stars, TypeScript, Semantic Layer only)
   - Streaming: kanapuli/mcp-kafka (76 stars, Go, MIT, produce/consume), tuannvm/kafka-mcp-server (45 stars, Go, dual transport with OAuth 2.1), streamnative-mcp-server (22 stars, Go, Kafka + Pulsar combined), Joel-hanson/kafka-mcp-server (Python)
   - Data integration: Airbyte (official, pipeline generation from prompts), mcp_fivetran (2 stars, 3 tools), keboola/mcp-server (83 stars, official, full ETL platform, 3,307 commits)
   - Data warehouses: Snowflake-Labs/mcp (255 stars, official, Cortex AI), mcp-snowflake-server (180 stars, read/write SQL), mcp-databricks-server (36 stars, Unity Catalog lineage), Databricks official MCP in-platform
   - Data quality: gx-mcp-server (Great Expectations validation as MCP tools)
   - 30+ servers across 6 subcategories
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added data pipeline/ETL row to short version table
   - Added Data Pipeline & ETL to "Beyond the original list" section
   - Updated review count to 83, 4.0/5 tier to 37

3. **Hugo build succeeded** — 105 pages. Deploy pending (throttle — deployed too recently).

### What should happen next
- **Run 119:** Deploy (throttle should be clear). Continue expanding coverage — chaos engineering MCP servers, container orchestration beyond Kubernetes, or data visualization MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 117 — 2026-03-15 — Content (AI & ML Model Serving MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: AI & ML Model Serving MCP Servers** (`content/reviews/ai-ml-model-serving-mcp-servers.md`) — 82nd review, sixty-second beyond original list.
   - Model hubs & inference: HuggingFace hf-mcp-server (206 stars, official, TypeScript, v0.3.5, Hub search + docs + Gradio Space execution, 3 transport modes), rawveg/ollama-mcp (144 stars, 14 tools, complete Ollama SDK with hybrid local+cloud, 96%+ test coverage), Replicate (official remote with Code Mode + community mcp-replicate at 93 stars with 13 tools), pierrebrunelle/mcp-server-openai (79 stars, cross-model bridge)
   - Local inference: LMStudio-MCP (health checks, model listing, completions), LM Studio itself as MCP host since v0.3.17
   - Experiment tracking: wandb/wandb-mcp-server (41 stars, official, 6 tools — experiment queries, Weave traces, report generation), kkruglik/mlflow-mcp (3 stars, 17+ tools across experiments, runs, artifacts, model registry, comparison)
   - ML training: prat24/pytorch-lightning-mcp (training, inspection, checkpointing via MCP), fcakyon/trackio-mcp (zero-config experiment tracking)
   - Cloud ML: AWS SageMaker MCP (official, in awslabs monorepo at 8.5K stars), Bedrock AgentCore MCP
   - Key gaps: no unified ML lifecycle server, model deployment unserved (no TorchServe/BentoML/Ray Serve MCP), no fine-tuning workflows, no GPU management
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added AI/ML model serving row to short version table
   - Added AI & ML Model Serving to "Beyond the original list" section
   - Updated review count to 82, 3.5/5 tier to 35

3. **Hugo build succeeded** — 104 pages. Deploy pending (throttle — deployed too recently).

### What should happen next
- **Run 118:** Deploy (if throttle allows). Continue expanding coverage — chaos engineering MCP servers, container orchestration beyond Kubernetes, or data pipeline/ETL MCP servers.
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 116 — 2026-03-15 — Write Performance & Load Testing MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Performance & Load Testing MCP Servers** (`content/reviews/performance-load-testing-mcp-servers.md`) — 81st review, sixty-first beyond original list.
   - Load testing frameworks: Grafana mcp-k6 (official, Go, script validation + guided generation + documentation browsing), QAInsights/jmeter-mcp-server (61 stars, 4+ tools, bottleneck detection, visualization), QAInsights/locust-mcp-server (9 stars, headless + UI modes), QAInsights/k6-mcp-server (9 stars, 2 tools), sumitbhowmick/k6-mcp-server (2 tools), gatling/gatling-ai-extensions (official, Enterprise-only), @jch1887/artillery-mcp-server (npm, dry-run validation), NeoLoad MCP (commercial)
   - Web performance auditing: danielsogl/lighthouse-mcp-server (27 stars, 13+ tools), priyankark/lighthouse-mcp (61 stars, 2 tools, agentic loop), mizchi/lighthouse-mcp (pattern recognition), ruslanlap/pagespeed-insights-mcp (16 tools), enemyrr/mcp-server-pagespeed, PhialsBasement/Pagespeed-MCP-Server
   - MCP server benchmarking: grafana/xk6-mcp (k6 extension for testing MCP servers), eval-sys/mcpmark (stress-test benchmark), Accenture/mcp-bench (LLM tool-use evaluation), thiagomendes/benchmark-mcp-servers (cross-language comparison), QuantGeekDev/mcp-performance-test
   - 20+ servers across 3 subcategories
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added performance/load testing row to short version table
   - Added Performance & Load Testing to "Beyond the original list" section
   - Updated review count to 81, 3.5/5 tier to 34

3. **Hugo build succeeded** — 103 pages. Deploy pending (throttle — deployed too recently in Run 114).

### What should happen next
- **Run 117:** Deploy (if throttle allows). On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — container orchestration beyond Kubernetes, AI/ML model serving MCP servers, or chaos engineering MCP servers

## Run 115 — 2026-03-15 — Write Network Security & Monitoring MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Network Security & Monitoring MCP Servers** (`content/reviews/network-security-mcp-servers.md`) — 80th review, sixtieth beyond original list.
   - Packet capture: WireMCP (380 stars, 3 tools, known command injection vuln), mcp-wireshark (pip-installable, polished), Wireshark-MCP (combined with nmap + threat intel)
   - Port scanning / diagnostics: dkruyt/mcp-nettools (11 tools, best all-in-one), Globalping (remote MCP, global probes, Streamable HTTP), ProbeOps (6 global regions), PhialsBasement/nmap-mcp-server (43 stars), mcp-netutils (Go, dual transport)
   - Pentest suites: FuzzingLabs/mcp-security-hub (20+ tools — Nmap, Ghidra, Nuclei, SQLMap, Hashcat, Shodan), pentest-mcp (only pentest server with all 3 transports, GPU hashcat), hexstrike-ai (150+ tools, multi-agent), pentestMCP (Docker, async scans), MCP_servers_cybersecurity (Metasploit RPC, WPScan)
   - Web app security: PortSwigger/mcp-server (536 stars, official Burp Suite, highest credibility), ZAP servers (Python + Java/Spring Boot), cyproxio/mcp-for-security (OWASP header analysis)
   - SSL/TLS: CERT-MCP-SERVER (30 tools, full certificate lifecycle, FortiGate/Windows/Linux), tls-mcp (analysis + grading), sslmon-mcp (expiry monitoring)
   - Reconnaissance: mcp-shodan (126 stars, internet-wide intelligence), mcp-censys, nuclei-mcp, vulnerability-scanner
   - 30+ servers across 6 subcategories
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added network security row to short version table
   - Added Network Security & Monitoring to "Beyond the original list" section
   - Updated review count to 80, 3.5/5 tier to 33

3. **Hugo build succeeded** — 102 pages. Deploy pending (throttle — deployed too recently in Run 114).

### What should happen next
- **Run 116:** Deploy. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — container orchestration beyond Kubernetes, performance/load testing tools, or AI/ML model serving MCP servers

## Run 114 — 2026-03-15 — Write API Testing MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: API Testing MCP Servers** (`content/reviews/api-testing-mcp-servers.md`) — 79th review, fifty-ninth beyond original list.
   - REST: Postman (187 stars, 100+ tools, remote hosted, OAuth, code gen), dkmaker/mcp-rest-api (90 stars, single test_request tool), cocaxcode/api-testing-mcp (20 tools — requests, assertions, flows, collections, environments, OpenAPI import, mock, load testing)
   - GraphQL: Apollo MCP Server (272 stars, Rust, v1.9.0, 1,567 commits, 42 contributors — operation-to-tool conversion, semantic schema discovery, @tool directive), blurrah/mcp-graphql (365 stars, TypeScript, generic introspect + query, mutations off by default), mcp-graphql-forge (Go, curated YAML-defined tools)
   - OpenAPI/Swagger: awslabs openapi-mcp-server (dynamic tool generation, auth, metrics), Vizioz/Swagger-MCP (84 stars, code generation), salacoste/openapi-mcp-swagger (context window optimization), ckanthony/openapi-mcp (Dockerized), ivo-toby/mcp-openapi-server (3 loading modes)
   - gRPC: Redpanda protoc-gen-go-mcp (187 stars, Go, code generation, zero boilerplate), ggRMCP (runtime gateway via reflection), adiom-data/grpcmcp (proto + reflection)
   - Also noted: Insomnia 12 and Apidog as MCP clients for testing MCP servers
   - 25+ servers across REST, GraphQL, OpenAPI, and gRPC
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added API testing row to short version table
   - Added API Testing to "Beyond the original list" section
   - Updated review count to 79, 4.0/5 tier to 36

3. **Hugo build succeeded** — 101 pages. Deploy pending (throttle — ~10 minutes remaining).

### What should happen next
- **Run 115:** Deploy. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — network tools (Wireshark, nmap, port scanners), container orchestration beyond Kubernetes, or performance/load testing tools

## Run 113 — 2026-03-15 — Write DNS & Domain Management MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: DNS & Domain Management MCP Servers** (`content/reviews/dns-domain-management-mcp-servers.md`) — 78th review, fifty-eighth beyond original list.
   - DNS Lookups: cenemil/dns-mcp-server (3+ tools, all record types, DNS trace), Globalping (5 tools, global probes)
   - Multi-Registrar: domain-suite-mcp (21 tools, Porkbun/Namecheap/GoDaddy/Cloudflare)
   - Spaceship: spaceship-mcp (47 tools, 13 record types — largest registrar MCP server)
   - Dynadot: domain-mcp (10 tools covering 106 API actions, 100% test coverage)
   - Porkbun: porkbun-mcp (safety-first, read-only defaults)
   - Namecheap: 3 competing servers, cordlesssteve is most complete
   - GoDaddy: minimal — availability checking only
   - Hostinger: official, 100+ tools, unique DNS snapshot feature
   - Cloud DNS: Cloudflare (strongest), Route53 (no dedicated server), Google Cloud DNS, no Azure standalone
   - WHOIS: whois-mcp (47 stars), domain-mcp (zero API keys), FastDomainCheck (Go, bulk)
   - 30+ servers across registrars, cloud providers, and diagnostics
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added DNS/domains row to short version table
   - Added DNS & Domain Management to "Beyond the original list" section
   - Updated review count to 78, 3.5/5 tier to 32

3. **Hugo build succeeded** — 100 pages. Deploy pending (throttle — deployed too recently in Run 110).

### What should happen next
- **Run 114:** Deploy. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — network tools (Wireshark, nmap, port scanners), container orchestration beyond Kubernetes, or API testing tools (Postman, Insomnia, Bruno)

## Run 112 — 2026-03-15 — Write Database Administration MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Database Administration MCP Servers** (`content/reviews/database-admin-mcp-servers.md`) — 77th review, fifty-seventh beyond original list.
   - PostgreSQL: crystaldba/postgres-mcp (2,300 stars, 8 tools, index tuning + health checks) + official server (archived, SQL injection vulnerability)
   - MySQL: benborla/mcp-server-mysql (1,300 stars, SSH tunnels, rate limiting) + designcomputer (1,200 stars, Python) + neverinfamous (192 tools, 3 stars)
   - MongoDB: mongodb-js/mongodb-mcp-server (959 stars, 40+ tools, Atlas management, Performance Advisor, automatic embeddings)
   - Redis: redis/mcp-redis (452 stars, official, all data structures, vector search, EntraID auth)
   - DynamoDB: AWS official (8 tools, data modeling and migration focused)
   - Supabase: supabase-community/supabase-mcp (2,500 stars, 30+ tools, 8 feature groups)
   - Multi-database: FreePeak/db-mcp-server (353 stars, Go, 5 DBs, lazy loading) + executeautomation (320 stars, 10 tools)
   - 25+ servers across 7 platforms
   - Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added MySQL, Redis, multi-DB rows to short version table
   - Expanded Databases section with MySQL/Redis/DynamoDB/multi-DB recommendations
   - Added Database Administration to "Beyond the original list" section
   - Updated review count to 77, 4.0/5 tier to 35

3. **Hugo build succeeded** — 99 pages. Deploy pending (throttle — deployed too recently in Run 110).

### What should happen next
- **Run 113:** Deploy. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — network tools (Wireshark, nmap), DNS management, or container orchestration beyond Kubernetes

## Run 111 — 2026-03-15 — Write CDN & Edge Computing MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: CDN & Edge Computing MCP Servers** (`content/reviews/cdn-edge-computing-mcp-servers.md`) — 76th review, fifty-sixth beyond original list.
   - Cloudflare: cloudflare/mcp (263 stars, Code Mode, 2 tools covering 2,500 API endpoints in ~1,000 tokens) + mcp-server-cloudflare (3,500 stars, 16 servers, comprehensive platform coverage) + workers-mcp (Worker proxy)
   - Fastly: fastly/mcp (34 stars, Go, MIT, 8 tools, official — CLI-wrapping security model where API keys never reach the LLM)
   - Akamai: ALECS (191 tools across 5 specialized servers — property, DNS, certs, security, analytics) + deepakjd2004 (4 tools, proof-of-concept) + schwarztim (npm, minimal)
   - Gcore: G-Core/gcore-mcp-server (6 stars, Python, Apache-2.0, 14 toolsets for CDN + GPU Cloud + WAAP)
   - Netlify: netlify/netlify-mcp (37 stars, official) + DynamicEndpoints (43 tools, full CLI)
   - Notable gaps: AWS CloudFront, Bunny CDN, KeyCDN, StackPath — zero MCP presence
   - 10+ servers across 5 platforms
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added CDN / edge computing row to comparison table
   - Added CDN & Edge Computing to "Beyond the original list" section
   - Updated review count to 76, 3.5/5 tier to 31

3. **Hugo build succeeded** — 98 pages. Deploy pending (throttle — deployed too recently in Run 110).

### What should happen next
- **Run 112:** Deploy. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — database admin tools (pgAdmin, Adminer), network tools (Wireshark, nmap), or DNS management MCP servers

## Run 110 — 2026-03-15 — Write Infrastructure Automation MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed pending changes** from Run 109 (RUNLOG.md update).

2. **Wrote new review: Infrastructure Automation MCP Servers** (`content/reviews/infrastructure-automation-mcp-servers.md`) — 75th review, fifty-fifth beyond original list.
   - Terraform: hashicorp/terraform-mcp-server (1,300 stars, 35+ tools, registry-first) + severity1/terraform-cloud-mcp (23 stars, 60+ tools, full TFC API) + nwiizo/tfmcp (357 stars, Rust, full CLI execution)
   - Ansible: Red Hat AAP MCP (official tech preview AAP 2.6.4) + Ansible Development Tools MCP + bsahane/mcp-ansible (25 stars, 35+ tools) + sibilleb/AAP-Enterprise-MCP-Server (24 stars, 50+ tools) + tarnover/mcp-sysoperator (26 stars, cross-platform)
   - Pulumi: pulumi/mcp-server (58 stars, local + remote, Neo delegation)
   - OpenTofu: opentofu/opentofu-mcp-server (77 stars, 5 registry tools)
   - Crossplane: minimal — 2 MVP community servers
   - 20+ servers across 6 platforms
   - Rating: 4.0/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Updated DevOps (IaC) row to link to new category review
   - Added Infrastructure Automation to "Beyond the original list" section
   - Updated review count to 75, 4.0/5 tier to 34

4. **Hugo build succeeded** — 97 pages. Deploy pending (throttle — deployed too recently in Run 109).

### What should happen next
- **Run 111:** Deploy. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — database admin tools (pgAdmin, Adminer), network tools (Wireshark, nmap), or CDN/edge computing MCP servers

## Run 109 — 2026-03-15 — Write Log Management MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Runs 106-108 — 95 pages live.

2. **Wrote new review: Log Management MCP Servers** (`content/reviews/log-management-mcp-servers.md`) — 74th review, fifty-fourth beyond original list.
   - Grafana: mcp-grafana (2,500 stars, 50+ tools, 6 Loki-specific) + loki-mcp (98 stars, 1 tool)
   - Elasticsearch: official 626 stars but deprecated — replaced by Elastic Agent Builder, 5 tools
   - Splunk: official Splunkbase app (7+ tools) + livehybrid/splunk-mcp (94 stars, 13 tools) + 2 more
   - Datadog: managed remote endpoint (16+ tools) + winor30 community (139 stars, 20 tools)
   - AWS CloudWatch: monorepo server + Log-Analyzer-with-MCP (153 stars)
   - Dynatrace: official 92 stars, 15+ tools with DQL + Davis CoPilot
   - New Relic: official Public Preview
   - Graylog: community 11 tools + built-in MCP support
   - Sumo Logic: community only, up to 37 tools
   - OpenTrace: self-hosted, 75+ tools, single binary + SQLite
   - Standalone log analyzers: local file parsing, MCP log debugging
   - 25+ servers across 12 platforms
   - Rating: 4.0/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Log Management row to summary table (4.0/5 tier now 33 servers)
   - Added Log Management to "Beyond the original list" section
   - Updated review count to 74

4. **Hugo build succeeded** — 96 pages. Deploy pending (throttle — deployed earlier this run).

### What should happen next
- **Run 110:** Deploy. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — database admin tools (pgAdmin, Adminer), network tools (Wireshark, nmap), or infrastructure automation (Ansible, Chef, Puppet) coverage

## Run 108 — 2026-03-15 — Write Secret Management MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from Run 107 (RUNLOG.md update).

2. **Wrote new review: Secret Management MCP Servers** (`content/reviews/secret-management-mcp-servers.md`) — 73rd review, fifty-third beyond original list.
   - HashiCorp Vault: official hashicorp/vault-mcp-server (35 stars, Go, beta, 16 tools — KV secrets CRUD, PKI certificate lifecycle including CA issuers/roles/cert issuance, mount management; stdio + StreamableHTTP transports)
   - HashiCorp Vault Radar: separate HCP server (4 tools — secret leak detection across data sources and resources)
   - Bitwarden: official bitwarden/mcp-server (129 stars, TypeScript, GPL-3.0, 30+ tools — vault CRUD, folder/attachment management, password generation, TOTP, Bitwarden Send, organization admin with collections/members/groups/policies/audit logs)
   - 1Password: two community servers — goodwokdev/op-mcp (Rust, 66 tools wrapping full 1Password CLI with biometric auth) and CakeRepository/1Password-MCP (TypeScript, 8 tools via Service Accounts)
   - Infisical: official Infisical/infisical-mcp-server (37 stars, JavaScript, Apache 2.0, 9 tools — secret CRUD, project/environment/folder creation, member invitations, Machine Identity auth)
   - Doppler: official DopplerHQ/mcp-server (TypeScript, Apache 2.0, v1.0.4 — secrets/projects/configs management with --read-only flag and project scoping)
   - AWS Secrets Manager: community @arvoretech/aws-secrets-manager-mcp (TypeScript, 6 tools — full CRUD plus metadata)
   - Azure Key Vault: 7 tools inside microsoft/mcp (2,800 stars) — secrets, keys, and certificates with consent-based elicitation
   - GCP Secret Manager: community eniayomi/gcp-mcp (6 stars, bundled with broader GCP services)
   - CyberArk: remediation-focused MCP server — automated hardcoded credential detection, secret provisioning, code refactoring, OAuth PKCE auth
   - MCP Credential Security tools: MCPGUARD (config audit + keychain migration), mcp-secrets-plugin (system keychain storage), mcp-keyring-injector (session-scoped injection)
   - 15+ servers across 10 platforms
   - Rating: 4.0/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Secret Management row to summary table (4.0/5 tier now 32 servers)
   - Added Secret Management to "Beyond the original list" section
   - Updated review count to 73

4. **Hugo build succeeded** — 95 pages. Deploy pending (throttle — deployed too recently in Run 107).

### What should happen next
- **Run 109:** Deploy all pending changes. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — logging frameworks (Winston, Pino, Log4j), database admin tools (pgAdmin, Adminer), or network tools (Wireshark, nmap) coverage

## Run 107 — 2026-03-15 — Write Container Registry MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from Run 106 (RUNLOG.md update).

2. **Wrote new review: Container Registry MCP Servers** (`content/reviews/container-registry-mcp-servers.md`) — 72nd review, fifty-second beyond original list.
   - Docker Hub: official docker/hub-mcp (130 stars, TypeScript, Apache 2.0, 13 tools — AI-powered image discovery across 100k+ images, repository CRUD, tag management, Docker MCP Toolkit one-click setup)
   - JFrog Artifactory: official jfrog/mcp-jfrog (112 stars, TypeScript, 22+ tools — repository management, build tracking, runtime monitoring, Xray vulnerability scanning, AQL queries, most comprehensive artifact lifecycle MCP server)
   - AWS ECR: via ECS MCP server (build_and_push_image_to_ecr, CloudFormation, IAM roles) + Finch MCP server (3 tools — build, push, create ECR repo with immutable tags)
   - Azure ACR: 2 read-only tools inside microsoft/mcp (2,800 stars) — list registries and list repositories only
   - Harbor: nomagicln/mcp-harbor (6 stars, TypeScript, MIT, 11 tools — projects, repos, tags, Helm charts)
   - Sonatype Nexus: brianveltman/sonatype-mcp (7 stars, 16 tools) + addozhang/nexus-mcp-server (1 star, 6 read-only tools with Docker-specific browsing)
   - GCP Artifact Registry: enesbol/gcp-mcp (6 stars, community, 8 GCP services)
   - Trivy: container image vulnerability scanning (cross-reference with code security review)
   - 12+ servers across 8 platforms
   - Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Container Registries to summary table (3.5/5 tier now 30 servers)
   - Added Container Registries to "Beyond the original list" section
   - Updated review count to 72

4. **Hugo build succeeded** — 94 pages. **Deployed to production.**

### What should happen next
- **Run 108:** On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — logging frameworks (Winston, Pino, Log4j), database admin tools (pgAdmin, Adminer), or secret management (Vault, AWS Secrets Manager) coverage

## Run 106 — 2026-03-15 — Write API Gateway MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from Run 105 (RUNLOG.md update).

2. **Wrote new review: API Gateway MCP Servers** (`content/reviews/api-gateway-mcp-servers.md`) — 71st review, fifty-first beyond original list.
   - Two-part review: MCP servers for managing gateways + API gateways acting as MCP infrastructure
   - Kong Konnect: official hosted MCP server (12 tools — GetService/GetRoute/GetPlugin/GetConsumer/GetConsumerGroup/GetVault/GetControlPlane/GetControlPlaneGroup/GetAnalytics/CreateDebugSession/ActiveTracingSession/KnowledgeBaseSearch, Streamable HTTP, active development); deprecated Kong/mcp-konnect (38 stars, TypeScript, Apache 2.0, 10 tools)
   - APISIX: api7/apisix-mcp (34 stars, TypeScript, Apache 2.0, 30+ tools — full CRUD on routes/services/upstreams/SSL/consumers/credentials/plugins/global rules/secrets/stream routes, deepest gateway management)
   - Cloudflare: cloudflare/mcp (263 stars, TypeScript, Apache 2.0, Code Mode — 2 tools covering 2,500+ endpoints in ~1,069 tokens, 99.5% context reduction); also cloudflare/mcp-server-cloudflare (3,500 stars, 15 per-product servers)
   - Traefik: theupriser/treafik-mcp (1 star, Python, MIT, 6 read-only tools — overview/routers/services/middlewares)
   - Gravitee: gravitee-io/gravitee-apim-mcp-server (1 star, TypeScript, MIT, 3 commits, auto-generated from OpenAPI)
   - Nginx Proxy Manager: b3nw/nginx-proxy-manager-mcp (community, reverse proxy management)
   - MCP Gateways: AgentGateway (1,900 stars, Rust/Go, Apache 2.0, v1.0.0-rc.2, Solo.io-backed, MCP+A2A proxy), Envoy AI Gateway (1,400 stars, Go, Apache 2.0, v0.5.0, MCP session-aware load balancing), Kong AI Gateway (3.12+, MCP Proxy/OAuth2/Prometheus plugins, API-to-MCP conversion), Traefik Hub (TBAC), Cloudflare MCP Server Portals (Mar 2026), Google Apigee (zero-code API-to-MCP), Tyk AI Studio
   - 15+ servers across 8 platforms
   - Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added API Gateways row to summary table
   - Added API Gateways to "Beyond the original list" section
   - Updated review count to 71, rating distribution (3.5/5 tier now 29 servers)

4. **Hugo build succeeded** — 93 pages. Deploy pending (throttle — ~15 min remaining at commit time).

### What should happen next
- **Run 107:** Deploy all pending reviews. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — logging frameworks (Winston, Pino), database admin tools (pgAdmin, Adminer), or container registry (Docker Hub, ECR, GCR) coverage

## Run 105 — 2026-03-15 — Write Code Security MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from Run 104 (RUNLOG.md update).

2. **Wrote new review: Code Security MCP Servers** (`content/reviews/code-security-mcp-servers.md`) — 70th review, fiftieth beyond original list.
   - Snyk: official snyk/studio-mcp (26 stars, Go, Apache 2.0, v1.6.1, 11 tools — SAST, SCA, IaC, container, SBOM, AI-BOM, auth management; most comprehensive single security MCP server); also snyk/agent-scan (1.9K stars, meta-security scanner for MCP servers/agents detecting prompt injection, tool poisoning, toxic flows)
   - SonarQube: official SonarSource/sonarqube-mcp-server (423 stars, Kotlin, 321 commits, code quality + security, Docker image, 11+ platform integrations; largest community in category)
   - Semgrep: official semgrep/mcp (639 stars, Python, 353 commits, 7 tools — security scanning, AST output, custom rules, AppSec Platform; archived Oct 2025, MCP now integrated into main Semgrep binary)
   - Trivy: official aquasecurity/trivy-mcp (37 stars, Go, MIT, v0.0.20, filesystem/container/repo scanning; Trivy plugin architecture)
   - Endor Labs: commercial (6 tools, dependency risk + malicious package detection, free Developer Edition)
   - Cycode: cycodehq/cycode-cli (97 stars, Python, 388 commits, 5 tools — secrets/SCA/IaC/SAST scanning + status)
   - Aikido: npm MCP (3 tools — full scan, SAST, secrets; focused on AI-generated code)
   - CodeQL: advanced-security/codeql-development-mcp-server (8 stars, TypeScript, v2.24.3, 9 languages; semantic analysis for security researchers)
   - Multi-tool aggregators: DevSecOps-MCP (SAST+DAST+SCA+IAST), sast-mcp (23+ tool integrations), AWS sample-mcp-security-scanner (Checkov+Semgrep+Bandit)
   - 15+ servers across 10 platforms
   - Rating: 4.0/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Code Security row to summary table
   - Added Code Security to "Beyond the original list" section
   - Updated review count to 70, rating distribution (4.0/5 tier now 31 servers)

4. **Hugo build succeeded** — 92 pages. Deploy pending (throttle — ~25 min remaining at commit time).

### What should happen next
- **Run 106:** Deploy all pending reviews. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — API gateways (Kong, Tyk), logging frameworks (Winston, Pino), or database admin tools (pgAdmin, Adminer) coverage

## Run 104 — 2026-03-15 — Write Testing & QA MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from Run 103 (RUNLOG.md update).

2. **Wrote new review: Testing & QA MCP Servers** (`content/reviews/testing-qa-mcp-servers.md`) — 69th review, forty-ninth beyond original list.
   - Selenium: angiejones/mcp-selenium (374 stars, JavaScript, MIT, v0.2.3, 20+ tools — browser management, element interaction, screenshots, cookies, frame/alert handling, WebDriver BiDi diagnostics, built by renowned testing advocate); SirBlobby/mcp-selenium (2 stars, 98 tools across 13 categories — most comprehensive tool set); naveenanimation20/selenium-mcp (6 stars, Java, only Java-based Selenium MCP)
   - BrowserStack: official browserstack/mcp-server (130 stars, TypeScript, 457 commits, 20 tools across 7 categories — test management, automation, observability, manual testing, accessibility, self-healing selectors, 3,000+ real devices)
   - Sauce Labs: official saucelabs/sauce-api-mcp (10 stars, Python, Apache 2.0, 30+ tools — account/device/job/build/storage/tunnel management, test analysis focus, 300+ real devices)
   - LambdaTest: 4 separate commercial MCP servers — Automation (4 tools), HyperExecute (2 tools), SmartUI (visual regression with pixel/layout/DOM/perception analysis), Accessibility; no public GitHub repo
   - Appium: official appium/appium-mcp (241 stars, TypeScript, Apache 2.0, 47 tools — AI-powered element identification, natural language test generation, Page Object Model, NO_UI mode 50-80% faster, multilingual, cross-platform Android UiAutomator2 + iOS XCUITest)
   - Cypress: no official server — jprealini/cypress-mcp (18 stars, page object generation), kerrfat/cypress-test-Gen-mcp (0 stars, 4 tools, test suite generation)
   - Testing frameworks: mcp-jest (16 stars, tests MCP servers), ai-testing-mcp (6 stars, 7 tools, multi-framework), mcp-code-checker (14 stars, Pylint+Pytest+Mypy)
   - 15+ servers across 8 platforms
   - Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Testing & QA row to summary table
   - Added Testing & QA to "Beyond the original list" section
   - Updated review count to 69, rating distribution (3.5/5 tier now 28 servers)

4. **Hugo build succeeded** — 91 pages. Deploy pending (throttle — 33 min remaining at commit time).

### What should happen next
- **Run 105:** Deploy all pending reviews. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — API gateways (Kong, Tyk), CI/CD security (Snyk, SonarQube), or logging frameworks (Winston, Pino) coverage

## Run 103 — 2026-03-15 — Write Notification & Email Delivery MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from Run 102 (RUNLOG.md update).

2. **Wrote new review: Notification & Email Delivery MCP Servers** (`content/reviews/notification-services-mcp-servers.md`) — 68th review, forty-eighth beyond original list.
   - Resend: official resend/resend-mcp (470 stars, TypeScript, MIT, v2.2.0, 20+ tools — email send/list/get/cancel/update/batch, received emails with attachment downloads, contacts with custom properties, broadcast campaigns, domain verification, subscription topics, API key/webhook admin, dual stdio+Streamable HTTP transport, 18 contributors, 6 open issues)
   - Twilio: official twilio-labs/mcp (96 stars, TypeScript, MIT, OpenAPI-to-MCP generator, dynamically exposes entire Twilio API via --services/--tags filtering, monorepo with generic openapi-mcp-server package, 3 contributors, 10 open issues, security warning against community servers)
   - SendGrid: no official server — Garoth/sendgrid-mcp (24 stars, 15+ tools, MIT), deyikong/sendgrid-mcp (3 stars, 59 tools, READ_ONLY=true default — smartest safety pattern), CDataSoftware (read-only JDBC), recepyavuz0 (basic)
   - Mailgun: official mailgun/mailgun-mcp-server (48 stars, JavaScript, Apache 2.0, 15+ tools — email, domains, webhooks, mailing lists, templates, analytics, suppressions, IP pools, multi-region US/EU, OpenAPI parameter validation)
   - Postmark: official ActiveCampaign/postmark-mcp (37 stars, JavaScript, MIT, intentionally minimal 4 tools — sendEmail, sendEmailWithTemplate, listTemplates, getDeliveryStats, 0 open issues)
   - Infobip: official infobip/mcp (25 stars, 14 remote MCP servers — SMS, WhatsApp, Viber, RCS, Voice, WhatsApp Flow, 2FA, People, Account, CPaaSX, CAMARA, Mobile App, Docs Search, Deep Research, cloud-hosted at mcp.infobip.com/{service}, API key + OAuth 2.1 with scope discovery, HTTPS/SSE/stdio bridge), plus infobip-openapi-mcp (24 stars, Java Spring AI framework, generic OpenAPI-to-MCP converter)
   - Courier: official trycourier/courier-mcp (0 stars but 136 commits, TypeScript, ~60 tools — sending, message management, profiles, lists, audiences, brands, JWT, push tokens, automations, bulk ops, audit logs, tenant admin, hosted at mcp.courier.com, v1.3.0)
   - Novu: official MCP (2-4 stars, TypeScript, 13 tools — subscribers, notifications, workflows, remote hosted)
   - Telnyx: official team-telnyx/telnyx-mcp-server (24 stars, Python, ARCHIVED Sep 2025, 20+ tools — AI assistants, call control, SMS/MMS, phone numbers, webhooks — migrating to TypeScript)
   - Vonage: community Vonage-Community/telephony-mcp-server (1 star, Python, 4 tools — voice, SMS, STT, speech recognition, minimal)
   - Push notifications: Pushover (AshikNesin/pushover-mcp 30 stars, 5+ implementations), ntfy (cyanheads/ntfy-mcp-server, gitmotion/ntfy-me-mcp, free/self-hosted)
   - 20+ servers across 12 platforms
   - Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Email delivery / Notifications row to summary table
   - Added Notification/Email Delivery to "Beyond the original list" section
   - Updated review count to 68, rating distribution (3.5/5 tier now 27 servers)

4. **Hugo build succeeded** — 90 pages (up from 89). Deploy pending.

### What should happen next
- **Run 104:** Deploy all pending reviews. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — API gateways (Kong, Tyk), testing frameworks (Playwright ecosystem, Selenium), or CI/CD security (Snyk, SonarQube) coverage

## Run 102 — 2026-03-15 — Write Monitoring & Uptime MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from Run 101 (RUNLOG.md update).

2. **Wrote new review: Monitoring & Uptime MCP Servers** (`content/reviews/monitoring-uptime-mcp-servers.md`) — 67th review, forty-seventh beyond original list.
   - UptimeRobot: official hosted endpoint at mcp.uptimerobot.com/mcp, full monitor CRUD (HTTP/Keyword/Ping/Port/Heartbeat/DNS), incident investigation with timelines/error codes/traceroutes, response-time analytics (1h-90d with min/max/avg/p95), Bearer token auth, read-only API key option, free tier works
   - Uptime Kuma: 4+ community servers (no official), DavidFuchs/mcp-uptime-kuma (16 stars, TypeScript, MIT, 9 tools, dual stdio+Streamable HTTP, context-efficient, JWT/2FA auth, Docker), phukit29182 (13 tools incl edit/tag/status page, 1 star), Camusama (3 tools batch ops, PyPI, 3 stars), gryfai open (8 read-only tools, BSL, commercial upsell)
   - OneUptime: official hosted + self-hosted MCP, 711 API endpoints, 126 resource types, Streamable HTTP, public mode (no auth, status pages) + authenticated mode (full CRUD), 100% open source
   - Better Stack: no official MCP, only DrDroidLab/betterstack-logs-mcp (1 star, logs only), MxDui/betterstack-mcp (0 stars, 1 commit)
   - Standalone diagnostics: ProbeOps (21 tools from 6 global regions, SSL/DNS/ping/traceroute/whois/port scan, free tier 100 calls/day), mcp-checkuptime (2 tools, basic ping/HTTP), mcp-status-observer (22 platforms monitored, 6 stars)
   - No Pingdom, StatusCake, Site24x7, or Better Stack uptime MCP servers
   - 10+ servers across 5 platforms
   - Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Monitoring/Uptime row to summary table
   - Added Monitoring/Uptime to "Beyond the original list" section
   - Updated review count to 67, rating distribution (3.5/5 tier now 26 servers)

4. **Hugo build succeeded** — 89 pages (up from 88). Deploy pending (throttle).

### What should happen next
- **Run 103:** Deploy all pending reviews. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — API gateways (Kong, Tyk), notification services (Twilio, SendGrid), or testing (Playwright ecosystem, Selenium) coverage

## Run 100 — 2026-03-15 — Write Message Queue MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from Run 99 (RUNLOG.md update).

2. **Wrote new review: Message Queue MCP Servers** (`content/reviews/message-queue-mcp-servers.md`) — 65th review, forty-fifth beyond original list.
   - Apache Kafka: confluentinc/mcp-confluent (121 stars, TypeScript, 37+ tools — Kafka + Flink SQL + Schema Registry + Connect + Tableflow, Confluent Cloud only), kanapuli/mcp-kafka (74 stars, Python, basic ops), 6+ more community servers, AWS MSK in awslabs/mcp, aywengo/kafka-schema-reg-mcp (20+ schema tools, unique)
   - RabbitMQ: amazon-mq/mcp-server-rabbitmq (12 stars, official, multi-broker OAuth), kenliao94/mcp-server-rabbitmq (40 stars, Python), kmitchell/rabbitmq-mcp (operations-focused)
   - Apache Pulsar: pulsar-java-contrib (70+ tools — highest in category, Java, Apache official), streamnative/streamnative-mcp-server (19 stars, Go, dynamic Pulsar Functions)
   - Redis: redis/mcp-redis (official, Streams + Pub/Sub + JSON)
   - AWS SQS/SNS: awslabs/mcp (official, tag-based mutation safety — safest infrastructure model)
   - NATS: jesseobrien/nats-mcp (Go, embedded server mode), 3 more community servers
   - Google Pub/Sub: official remote MCP server (managed, OAuth + IAM, zero-install — gold standard)
   - Azure Service Bus: Azure/azure-mcp (official, message peeking)
   - IBM MQ: ibm-messaging/mq-mcp-server (official, 2 tools, runmqsc escape hatch)
   - Multi-broker: queue-pilot (RabbitMQ + Kafka, JSON Schema validation), messageaid (RabbitMQ + SQS + Service Bus, BSL 1.1)
   - 25+ servers across 10 platforms
   - Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Message Queues row to summary table
   - Added Message Queues section after Search Engines with platform descriptions
   - Added Message Queues to "Beyond the original list" section
   - Updated review count to 65, rating distribution (3.5/5 tier now 24 servers)

4. **Hugo build succeeded** — 87 pages (up from 86). Deploy pending (throttle).

### What should happen next
- **Run 101:** Deploy all pending reviews. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — monitoring (Uptime, StatusPage), API gateways (Kong, Tyk), or notification services (Twilio, SendGrid) coverage

## Run 99 — 2026-03-15 — Write Search Engine MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed uncommitted changes** from previous runs (grove_runner.sh v3 upgrade, RUNLOG entries).

2. **Wrote new review: Search Engine MCP Servers** (`content/reviews/search-engine-mcp-servers.md`) — 64th review, forty-fourth beyond original list.
   - Elasticsearch: official elastic/mcp-server-elasticsearch (626 stars, Rust, DEPRECATED — superseded by Agent Builder in Elastic 9.2+), cr7258/elasticsearch-mcp-server (256 stars, Python, 17+ tools, supports ES 7.x-9.x AND OpenSearch), awesimon/elasticsearch-mcp (18 stars, TypeScript, 11 tools)
   - OpenSearch: opensearch-project/opensearch-mcp-server-py (111 stars, official, 24+ tools — most comprehensive, unique search relevance tooling with judgment lists and query sets)
   - Meilisearch: meilisearch/meilisearch-mcp (178 stars, official, 20+ tools, actively maintained, dynamic connection management), devlimelabs/meilisearch-ts-mcp (11 stars, 40+ tools, vector search)
   - Algolia: algolia/mcp-node (82 stars, experimental, no SLA), algolia/mcp (27 stars, Go, experimental)
   - Apache Solr: apache/solr-mcp (9 stars, official Apache project, Java 25+ required, 9 tools, incubating)
   - Typesense: community only — suhail-ak-s (20 stars, read-only 4 tools), avarant (7 stars, 12+ tools)
   - Manticore Search: krajcik (2 stars, Go, 8 tools)
   - 15+ servers across 7 platforms
   - Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Search Engines row to summary table
   - Added Search Engines section after Cloud Storage with platform descriptions
   - Added Search Engines to "Beyond the original list" section
   - Updated review count to 64, rating distribution (3.5/5 tier now 23 servers)

4. **Hugo build succeeded** — 86 pages (up from 85). Deploy pending (throttle).

### What should happen next
- **Run 100:** Deploy all pending reviews. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — monitoring (Uptime, StatusPage), messaging queues (Kafka, RabbitMQ), or API gateway (Kong, Tyk) coverage

## Run 98 — 2026-03-15 — Write Cloud Storage MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Cloud Storage MCP Servers** (`content/reviews/cloud-storage-mcp-servers.md`) — 63rd review, forty-third beyond original list.
   - AWS S3: no general-purpose official server (awslabs/mcp covers only S3 Tables/Iceberg), best community option is txn2/mcp-s3 (Go, 9 tools, security-first)
   - Google Cloud Storage: googleapis/gcloud-mcp storage-mcp (705 stars monorepo, 21 tools, best-designed with safe/destructive separation, Storage Insights)
   - Azure Blob: microsoft/mcp (2,800 stars monorepo, 7 storage tools, can upload but NOT download blobs)
   - MinIO: minio/mcp-server-aistor (39 stars, 26 tools — most feature-rich, AI-powered ask_object, three-level permissions)
   - Cloudflare R2: via universal API server (2,500+ endpoints, 2 meta-tools)
   - Backblaze B2: BraveRam/backblaze-mcp (0 stars, 21 tools incl multipart upload)
   - DigitalOcean Spaces: official (90 stars, Spaces subset)
   - 20+ servers across 7 platforms
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Cloud Storage row to summary table
   - Added Cloud Storage section after Analytics with platform descriptions
   - Added Cloud Storage to "Beyond the original list" section
   - Updated review count to 63, rating distribution (3.5/5 tier now 22 servers)

3. **Hugo build succeeded** — 85 pages (up from 84). Deploy pending (throttle).

### What should happen next
- **Run 99:** Deploy Cloud Storage + Analytics + CI/CD + CRM + Outlook reviews (5 reviews pending deploy). On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — monitoring (Uptime, StatusPage), messaging queues (Kafka, RabbitMQ), or search engines (Elasticsearch, Typesense) coverage

## Run 97 — 2026-03-15 — Write Analytics MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Analytics MCP Servers** (`content/reviews/analytics-mcp-servers.md`) — 62nd review, forty-second beyond original list.
   - Google Analytics: googleanalytics/google-analytics-mcp (1,500 stars, official, Python, Apache 2.0, 7 read-only tools, ADC auth), surendranb/google-analytics-mcp (189 stars, 200+ dimensions/metrics, context window protection), gomarble-ai (13 stars, OAuth), ruchernchong (70 stars, archived)
   - PostHog: PostHog/mcp (143 stars, MIT, 27+ tools, archived → monorepo, analytics + feature flags + experiments + error tracking + prompts, read-only mode, one-command install into 6+ IDEs)
   - Amplitude: official hosted endpoint at mcp.amplitude.com (24+ tools, OAuth 2.0, Streaming HTTP, 10+ client integrations, closed source), silviorodrigues/amplitude-mcp (9 stars, 2 tools)
   - Mixpanel: official beta MCP server (natural language focus, cross-source correlation), dragonkhoi/mixpanel-mcp (19 stars, events/retention/funnels)
   - Plausible: AVIMBU/plausible-mcp-server (5 stars, minimal), alexanderop/plausible-mcp
   - Matomo: FGRibreau/mcp-matomo (8 stars, Rust, MIT, dynamic API introspection), Jaimeapo/matomo-mcp (TypeScript)
   - 15+ servers across 6 analytics platforms
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Analytics row to summary table
   - Added Analytics section after Observability with full platform descriptions
   - Added Analytics to "Beyond the original list" section
   - Updated review count to 62, rating distribution (3.5/5 tier now 21 servers)

3. **Hugo build succeeded** — 84 pages (up from 83). Deploy pending (throttle).

### What should happen next
- **Run 98:** Deploy Analytics + CI/CD + CRM + Outlook reviews (4 reviews pending deploy). On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — calendar (Microsoft Outlook Calendar), cloud storage (S3, GCS), or monitoring (Uptime, StatusPage) coverage

## Run 96 — 2026-03-15 — Write CI/CD MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: CI/CD MCP Servers** (`content/reviews/cicd-mcp-servers.md`) — 61st review, forty-first beyond original list.
   - GitHub MCP Server: github/github-mcp-server (27,900 stars, official, Go, 40+ tools incl. Actions workflows, job logs, deployment management)
   - Jenkins: jenkinsci/mcp-server-plugin (66 stars, Java, runs inside Jenkins as native plugin, 15+ tools, 3 transport options), lanbaoshen/mcp-jenkins (95 stars, Python, 18 tools, standalone with read-only mode)
   - CircleCI: CircleCI-Public/mcp-server-circleci (80 stars, TypeScript, 15 tools, diagnostic-first — flaky test detection, resource optimization, structured error summaries)
   - GitLab: zereight/gitlab-mcp (1,200 stars, TypeScript, 85+ tools with 12 pipeline-specific, modular toolset system) plus GitLab official server
   - Azure DevOps: microsoft/azure-devops-mcp (1,400 stars, TypeScript, GA, built into Visual Studio 2026, Entra ID auth)
   - Argo CD: akuity/argocd-mcp (348 stars, TypeScript, 12 tools, GitOps deployment for Kubernetes)
   - 15+ servers across 6 CI/CD platforms
   - Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added DevOps (CI/CD) row to summary table
   - Expanded CI/CD paragraph in DevOps section with all platforms
   - Added CI/CD to "Beyond the original list" section
   - Updated review count to 61, rating distribution (4.0/5 tier now 30 servers)

3. **Hugo build succeeded** — 83 pages (up from 82). Deploy throttled (29 min since last deploy).

### What should happen next
- **Run 97:** Deploy CI/CD + CRM + Outlook reviews (3 reviews pending deploy). On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — calendar (Microsoft Outlook Calendar), analytics (Google Analytics, Mixpanel), or cloud storage (S3, GCS) coverage

## Run 95 — 2026-03-15 — Write CRM MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: CRM MCP Servers** (`content/reviews/crm-mcp-servers.md`) — 60th review, fortieth beyond original list.
   - Salesforce: salesforcecli/mcp (312 stars, official, 60+ tools with dynamic toolsets), smn2gnt/MCP-Salesforce (166 stars, Python), tsmztech (139 stars), plus 4 more
   - HubSpot: peakmojo/mcp-hubspot (116 stars, FAISS semantic search), adeel0x01 (58 tools), HubSpot official repo is empty
   - Attio: kesslerio/attio-mcp-server (58 stars, 1,291 commits, excellent architecture)
   - Pipedrive: WillDent (46 stars, read-only), Teapot-Agency (40 tools, full CRUD)
   - Dynamics 365: single server with 5 tools
   - Zoho: no production-ready server despite being a major platform
   - 20+ servers across 8 CRM platforms total
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added CRM row to summary table
   - Added CRM section between Payments and E-commerce with full descriptions
   - Added CRM to "Beyond the original list" section
   - Updated review count to 60, rating distribution (3.5/5 tier now 20 servers)

3. **Hugo build succeeded** — 82 pages (up from 81). Deploy throttled (22 min since last deploy).

### What should happen next
- **Run 96:** Deploy CRM + Outlook reviews. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — CI/CD, calendar (Microsoft Outlook Calendar), or analytics (Google Analytics, Mixpanel) coverage

## Run 94 — 2026-03-15 — Write Outlook MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Outlook MCP Servers** (`content/reviews/outlook-mcp-servers.md`) — 59th review, thirty-ninth beyond original list.
   - Microsoft's official Work IQ Mail server — 10 tools, KQL search, hosted, Entra ID OAuth, preview status, requires Copilot license (~$30/user/month)
   - Softeria/ms-365-mcp-server (530 stars) — community standard, 8+ Microsoft 365 services (email, calendar, OneDrive, Excel, OneNote, Tasks, Contacts), three auth modes, TOON token optimization
   - ryaker/outlook-mcp (278 stars) — unique Power Automate integration alongside email/calendar/OneDrive
   - merill/lokka (228 stars) — raw Graph API access as a single meta-tool, four auth modes
   - 3+ additional Outlook servers reviewed (ampcome, Abhishek COM-based, kacase, merajmehrabi)
   - Detailed Gmail vs Outlook comparison table
   - Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Email (Microsoft) row to summary table with Outlook MCP Servers
   - Added Outlook section in Email category with full description
   - Added Outlook to "Beyond the original list" section
   - Updated review count to 59, rating distribution (3.5/5 tier now 19 servers)

3. **Hugo build succeeded** — 81 pages (up from 80). Deploy throttled (12 min since last deploy).

### What should happen next
- **Run 95:** Deploy Outlook review. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — CRM (Salesforce/HubSpot), CI/CD, or calendar (Microsoft Outlook Calendar) coverage

## Run 93 — 2026-03-15 — Deploy + Write Gmail MCP Servers Review

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — Blender + Shopify reviews now live on chatforest.com. 80 pages.

2. **Wrote new review: Gmail MCP Servers** (`content/reviews/gmail-mcp-servers.md`) — 58th review, thirty-eighth beyond original list.
   - Google's official Workspace MCP endpoint at `workspace-developer.goog/mcp` — first-party Gmail access
   - taylorwilsdon/google_workspace_mcp (1,700+ stars) — community standard, 12 Google services, 100+ tools, three-tier permissions (Core/Extended/Full)
   - MarkusPfundstein/mcp-gsuite (477 stars) — focused Gmail + Calendar, narrower OAuth scope
   - baryhuang/mcp-headless-gmail (53 stars) — decoupled credential model for server/container deployments
   - GongRzhe/Gmail-MCP-Server — abandoned Aug 2025, ArtyMcLabin fork is active continuation
   - 5+ additional Gmail-only servers reviewed (shinzo-labs, theposch, cafferychen777 Chrome extension, david-strejc IMAP/SMTP)
   - Heavy security focus: OAuth scope creep, token storage, send permission risks, no official reference server
   - Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`):
   - Added Email section with Gmail MCP Servers
   - Added Gmail to summary table, "Beyond the original list" section, and rating distribution (3.5/5 tier now 18 servers)
   - Updated review count to 58

4. **Hugo build succeeded** — 80 pages (up from 79).

### What should happen next
- **Run 94:** Deploy Gmail review. On 2026-03-17: publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — CRM (Salesforce/HubSpot), calendar (Microsoft Outlook), or CI/CD coverage

## Run 92 — 2026-03-15 — Publish Hashnode/dev.to 003+004, Write Shopify Review

**Mode:** Developer + Operations + Researcher + Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Published Hashnode articles 003+004:**
   - 003 Brave Search MCP Server (ID: 69b58f6e81fe768df85b317a) → https://chatforest.hashnode.dev/brave-search-mcp-server-review
   - 004 Slack MCP Server (ID: 69b58f7381fe768df85b317c) → https://chatforest.hashnode.dev/slack-mcp-server-review

2. **Published dev.to articles 003+004** (changed from draft to published):
   - 003 Brave Search MCP Server (ID: 3351905) → https://dev.to/grove_chatforest/the-brave-search-mcp-server-the-best-search-option-for-agents-59ep
   - 004 Slack MCP Server (ID: 3351906) → https://dev.to/grove_chatforest/the-slack-mcp-server-your-workspace-accessible-to-agents-d1l

3. **Updated publish schedules** — both Hashnode and dev.to schedules now show 4/6 articles published.

4. **Wrote new review: Shopify MCP Servers** (`content/reviews/shopify-mcp-servers.md`) — 57th review, thirty-seventh beyond original list.
   - Three-layer ecosystem: Dev MCP (official, 414 stars, @shopify/dev-mcp v1.7.0, zero-config docs/schema introspection), Storefront MCP (per-store AI shopping with semantic search, cart, policy Q&A, Agentic Storefronts), community Admin API servers (GeLi2001 39 stars, antoineschaller 22 tools)
   - Universal Commerce Protocol (UCP) co-developed with Google — open standard for AI-agent-to-commerce communication
   - Critical gap: no official Admin API MCP server for store management
   - Community servers are fragmented and immature (highest has 39 stars)
   - Rating: 3.5/5
   - Updated mega-comparison: added E-commerce section, Shopify in summary table, review count to 56, 3.5/5 tier now 17 servers

5. **Hugo build succeeded** — 79 pages (up from 78).

6. **Deploy still throttled** — 33 min since last deploy. Shopify review + Blender review waiting for next deploy.

### What should happen next
- **Run 93:** Deploy (Blender + Shopify reviews go live). Publish Hashnode 005+006 (Docker + Sentry), dev.to 005+006 (final batch)
- **After all 6 Hashnode + dev.to articles published:** Update `.current_social_task` to 140 (Blue Sky)
- **Content:** Continue expanding — CRM (Salesforce/HubSpot), email (Gmail), or more e-commerce coverage

## Run 91 — 2026-03-15 — Publish First 2 Hashnode Articles

**Mode:** Developer + Operations

### Inbox update
- **#153 (Boss Claude):** dev.to handled, move on to Hashnode (task 139). Marked seen.

### What I did

1. **Updated `.current_social_task` to 139** (Hashnode) per Boss Claude's instruction.

2. **Retrieved Hashnode publication ID** — queried GraphQL API, got `69b5872e210c74252f0571cc` for chatforest.hashnode.dev.

3. **Published 2 Hashnode articles** (drip-feed: 2/day over 3 days):
   - 001 Filesystem MCP Server (ID: 69b58e4f80a726335c668c17) → https://chatforest.hashnode.dev/filesystem-mcp-server-review
   - 002 GitHub MCP Server (ID: 69b58e5f4b280b2e32915cc3) → https://chatforest.hashnode.dev/github-mcp-server-review

4. **Fixed `post_to_hashnode.sh`** — shell script had a quoting bug (bash `$'...'` interpolation broke Python regex). Rewrote to use heredoc + environment variables instead.

5. **Deploy still throttled** — Blender MCP review waiting for next run (~38 min remaining).

### What should happen next
- **Run 92:** Publish Hashnode articles 003 (Brave Search) + 004 (Slack), dev.to articles 003+004 (scheduled 2026-03-16)
- **Deploy:** Blender MCP review needs to go live — should be unthrottled
- **Run 93:** Hashnode 005+006, dev.to 005+006 (scheduled 2026-03-17)
- **After all 6 Hashnode articles published:** Update `.current_social_task` to 140 (Blue Sky)

## Run 90 — 2026-03-15 — Prepare Hashnode Articles + Deploy

**Mode:** Copywriter + Operations

### Inbox update
- No pending messages.

### What I did

1. **Prepared Hashnode articles 002-006** — adapted dev.to content for Hashnode:
   - 002 GitHub MCP Server
   - 003 Brave Search MCP Server
   - 004 Slack MCP Server
   - 005 Docker MCP Server
   - 006 Sentry MCP Server
   - Each has Hashnode frontmatter (slug, tags, canonical_url back to chatforest.com)
   - Created `social/hashnode/publish_schedule.md` to track publication

2. **Deploy attempted** — throttled (only ~18min since last deploy from Run 89). Blender MCP review still waiting to go live.

### What should happen next
- **Run 91 (2026-03-16):** Publish dev.to articles 003 (Brave Search) and 004 (Slack) per schedule
- **Deploy:** Blender MCP review needs to go live — should be unthrottled by next run
- **Task 139 (Hashnode):** All 6 articles ready. Once dev.to drip-feed completes (2026-03-17), update `.current_social_task` to 139 and start Hashnode publishing
- **Task 140 (Blue Sky):** After Hashnode

## Run 89 — 2026-03-15 — New Review: Blender MCP Server

**Mode:** Researcher + Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Blender MCP Server** (`content/reviews/blender-mcp-server.md`)
   - Researched ahujasid/blender-mcp (17.6K GitHub stars, 1.7K forks, ~114K monthly PyPI downloads)
   - Covered: architecture (two-process socket design), ~10 MCP tools, setup for Claude Desktop/Code
   - Key strengths: natural language 3D modeling, Poly Haven integration, visual feedback loop, low barrier to entry
   - Key concerns: arbitrary Python code execution with no sandbox, LLM spatial reasoning limits, connection reliability, opt-out telemetry
   - Compared to: Poly-MCP (51 tools), CommonSenseMachines (Text to 4D), Blender Python API, Three.js
   - Rating: 3.5/5
   - Follows site conventions: research-only language, Rob linked, transparent AI authorship footer

2. **Hugo build succeeded** (78 pages, 56ms) — site grows from 77 to 78 pages.

3. **Deploy skipped** — throttled (11 min since last deploy, need 60 min).

### What should happen next
- **Run 90 (2026-03-16):** Publish dev.to articles 003 (Brave Search) and 004 (Slack) per schedule
- **Deploy:** Next run should deploy to get the Blender MCP review live
- **Later:** dev.to articles 005+006 on 2026-03-17, then Hashnode setup (task 139), Blue Sky (#140)
- **Content expansion:** Consider more creative/design category reviews (Unity, Unreal, Figma alternatives) or a "Best MCP Servers for Creative Tools" guide

## Run 88 — 2026-03-15 — Publish First 2 dev.to Articles

**Mode:** Developer + Operations

### Inbox update
- **#151 (Boss Claude):** Rob approved dev.to drafts. Cleared to publish — drip-feed or all at once. Update .current_social_task to 139 once dev.to is done. Marked seen.
- **#152 (Rob):** Hashnode blog set up at chatforest.hashnode.dev. Can start publishing there once dev.to is handled. Marked seen.

### What I did

1. **Published 2 dev.to articles** (drip-feed strategy: 2/day over 3 days):
   - 001 Filesystem MCP Server (ID: 3351860) → https://dev.to/grove_chatforest/the-filesystem-mcp-server-simple-useful-and-worth-understanding-444
   - 002 GitHub MCP Server (ID: 3351862) → https://dev.to/grove_chatforest/the-github-mcp-server-power-tool-with-a-learning-curve-i3d

2. **Discovered API quirk:** dev.to ignores the `published` JSON parameter if `published: false` is in the body_markdown frontmatter. Fix: must update the frontmatter in body_markdown before PUT.

3. **Created publishing schedule** (`social/devto/publish_schedule.md`) for systematic tracking:
   - 2026-03-15: articles 001 + 002 (done)
   - 2026-03-16: articles 003 + 004 (Brave Search, Slack)
   - 2026-03-17: articles 005 + 006 (Docker, Sentry)

4. **Updated local markdown files** to reflect `published: true` for articles 001 and 002.

### What should happen next
- **Run 89 (2026-03-16):** Publish articles 003 (Brave Search) and 004 (Slack) per schedule
- **Run 90 (2026-03-17):** Publish articles 005 (Docker) and 006 (Sentry), then update .current_social_task to 139 for Hashnode
- **After dev.to complete:** Start publishing on chatforest.hashnode.dev (inbox #152)
- **Later:** Blue Sky setup (#140)

## Run 87 — 2026-03-15 — Rob's Links + dev.to Bio Rewrite + Deploy

**Mode:** Copywriter + Developer

### Inbox update
- **#150 (Rob, high priority):** dev.to bio is max 200 chars, needs rewrite. **Done** — rewrote to 155 chars.
- **#149 (Rob):** Add links to robnugen.com where Rob is referenced on site. **Done** — linked about page, context7 footer, gitmcp footer.
- **#148 (me):** Status update from Run 86. Acknowledged.

### What I did

1. **Rewrote dev.to bio** (`social/devto/profile.md`) — from 335 chars to 155 chars, within 200-char limit.
   - New bio: "AI agent reviewing MCP servers at chatforest.com. I read the source code, docs, and issues so you don't have to. Honest reviews, transparent AI authorship."

2. **Added Rob Nugen links to site** (per inbox #149):
   - `content/about.md` line 20: "Rob" → linked to robnugen.com/en/; added sentence linking to Rob's blog for Grove's origin story
   - `content/about.md` line 54: "Rob Nugen" → linked to robnugen.com/en/
   - `content/reviews/context7-mcp-server.md` footer: "Rob Nugen" → linked
   - `content/reviews/gitmcp-server.md` footer: "Rob Nugen" → linked

3. **Fixed another false claim** — context7 footer said "We test and research MCP servers" → "We research MCP servers"

4. **Hugo build succeeded** (77 pages, 58ms).

5. **Fixed 10 more false testing claims** across the site (bonus sweep while waiting for deploy throttle):
   - 6 review footers: "We test every server" → "We research every server"
   - 2 review footers: "We test the tools we review by building with them" → research-based language
   - 3 guide og_descriptions: "We tested them all" → "We researched them all"
   - 1 guide footer: "We tested or reviewed" → "We reviewed"

6. **Deployed** — site live at chatforest.com with all fixes (77 pages synced).

### What should happen next
- **Rob action needed:** (1) Update dev.to bio with the 155-char version from profile.md, (2) Review 6 dev.to drafts and publish, (3) Create Hashnode blog
- **Future runs:** Post more dev.to articles (Datadog, Cloudflare), Hashnode articles once blog exists, Blue Sky setup (#140)

## Run 86 — 2026-03-15 — Fix False Claims + Standardize dev.to Bylines

**Mode:** Copywriter + Developer

### Inbox update
- **#147 (Boss Claude):** Fix remaining false hands-on claims on live site, standardize dev.to bylines to longer version, stay on task 138 until dev.to drafts are fully ready. Marked seen.
- **#146 (me, re: Hashnode):** Hashnode blog setup blocked on Rob. Marked seen.

### What I did

1. **Fixed remaining false hands-on claims in Hugo source** (3 files):
   - `content/reviews/filesystem-mcp-server.md` — "I've learned to use" → "using ... is a better approach"
   - `content/reviews/github-mcp-server.md` — "I've used for real development work" → "available for real development work"
   - `content/guides/best-search-mcp-servers.md` — "has used both ... extensively" → "has reviewed ... in depth"

2. **Fixed same false claims in dev.to articles** (2 files):
   - `social/devto/001-filesystem-mcp-server.md` — same filesystem fix
   - `social/devto/002-github-mcp-server.md` — same GitHub fix

3. **Standardized all dev.to bylines to longer version** (articles 001-004):
   - Old: short byline ("I'm Grove, an AI agent that reviews MCP servers...")
   - New: longer byline Rob prefers ("This review is part of ChatForest's MCP Server Directory...")
   - Articles 005 (Docker) and 006 (Sentry) already had the correct long byline

4. **Updated all 4 dev.to drafts via API** (PUT requests):
   - 001 Filesystem (ID: 3351860) ✓
   - 002 GitHub (ID: 3351862) ✓
   - 003 Brave Search (ID: 3351905) ✓
   - 004 Slack (ID: 3351906) ✓

5. **Hugo build succeeded** (57ms, 77 pages). **Deploy throttled** — 32 min remaining on 1-hour throttle.

### dev.to draft status
- **6 draft articles**, all now with:
  - Consistent long bylines ✓
  - No false hands-on claims ✓
  - canonical_url pointing to chatforest.com ✓
- **Ready for Rob's review and publication**

### What should happen next
- **Run 87:** Deploy site (throttle will have cleared). Verify live site has fixed claims. Check if Rob created Hashnode blog.
- **Rob action needed:** (1) Review 6 dev.to drafts and publish, (2) Create Hashnode blog, (3) Update dev.to profile bio
- **Future:** Post more dev.to articles (Datadog, Cloudflare), Hashnode articles once blog exists, Blue Sky setup (#140)

## Run 85 — 2026-03-15 — Docker + Sentry to dev.to, Hashnode Setup Started

**Mode:** Developer + Operations

### Inbox update
- No pending messages.

### What I did

1. **Posted Docker MCP Server review to dev.to** (ID: 3351920) — 5th draft article
   - `social/devto/005-docker-mcp-server.md` — adapted from Hugo review, devops-tagged
   - canonical_url pointing to chatforest.com, honest byline footer

2. **Posted Sentry MCP Server review to dev.to** (ID: 3351927) — 6th draft article
   - `social/devto/006-sentry-mcp-server.md` — strong dev audience appeal (observability/debugging)
   - canonical_url, correct byline, no false claims

3. **Started Hashnode setup (message #139)**
   - Authenticated via API — username `chatforest`, token works
   - Discovered: no publication/blog exists yet. Hashnode requires a blog to be created via web UI before API posting works.
   - Sent inbox message #146 to Rob: please create blog at hashnode.com
   - Created `social/hashnode/` directory with:
     - `profile.md` — profile info and blog name suggestions
     - `post_to_hashnode.sh` — posting script (GraphQL API, supports tags + canonical_url)
     - `001-filesystem-mcp-server.md` — first article ready to post once blog exists
   - Updated `.current_social_task` from 138 → 139

4. **Deploy skipped** — last deploy was 2 minutes before this run (throttle: 1/hour)

### dev.to status
- **6 draft articles total**: Filesystem, GitHub, Brave Search, Slack, Docker, Sentry
- All with canonical_url and honest bylines
- Rob still needs to review/publish drafts and update profile bio

### Hashnode status
- **Blocked**: needs Rob to create blog via web UI
- API auth works, posting script ready, first article prepared
- Will continue once blog exists

### What should happen next
- **Run 86:** Check if Rob created Hashnode blog. If yes, post first article. If not, continue dev.to articles (Datadog, Cloudflare — good dev audience).
- **Rob action needed:** (1) Create Hashnode blog at hashnode.com, (2) Review 6 dev.to drafts, (3) Update dev.to profile bio
- **Future:** Finish Hashnode articles, then Blue Sky setup (#140)

## Run 84 — 2026-03-15 — Fix False Claims + Post More dev.to Articles

**Mode:** Operations + Copywriter

### Inbox update
- **#145 (high priority):** FALSE "hands-on testing" claims in bylines and bios. Fixed immediately — see details below.
- **#144:** Acknowledged dev.to draft posting from Run 83.

### What I did

1. **Fixed ALL false "hands-on testing" claims** (inbox #145)
   - `social/devto/profile.md` — "I test each server hands-on" → "I research each server thoroughly — reading source code, docs, GitHub issues, and community signals"
   - `social/devto/001-filesystem-mcp-server.md` — footer + "using it extensively" → "researched it thoroughly"
   - `social/devto/002-github-mcp-server.md` — footer + "working with it across multiple projects" → "researched it thoroughly"
   - `content/reviews/brave-search-mcp-server.md` — "using it for research tasks" → "researched it thoroughly"
   - `content/reviews/github-mcp-server.md` — "working with it across multiple projects" → "researched it thoroughly"
   - `content/reviews/filesystem-mcp-server.md` — card_description + body text fixed
   - `RUNLOG.md` line 161 — "hands-on review" → "research-based review"
   - Updated all 4 dev.to draft articles via API (IDs 3351860, 3351862, and new ones below)
   - **Root cause:** When writing social cross-posts in Run 82-83, I used false "hands-on" language instead of the corrected language from Run 68. The about page and guides were already correct.
   - Saved persistent feedback memory (`feedback_no_hands_on_claims.md`) to prevent recurrence

2. **Posted 2 more articles to dev.to** (as drafts)
   - Brave Search MCP Server review (ID: 3351905) — `social/devto/003-brave-search-mcp-server.md`
   - Slack MCP Server review (ID: 3351906) — `social/devto/004-slack-mcp-server.md`
   - Both with canonical_url, correct byline footer, no false claims

3. **Rebuilt site** with corrected content in 3 review files

### dev.to status
- 4 draft articles total (Filesystem, GitHub, Brave Search, Slack)
- Profile bio corrected in `social/devto/profile.md` (Rob needs to paste manually)
- All articles have honest "I research each one thoroughly" bylines

### What should happen next
- **Run 85:** Deploy (throttle pending). Post Docker MCP Server to dev.to. Start Hashnode setup (#139).
- **Rob action needed:** Review 4 drafts on dev.to dashboard, update profile bio
- **Future:** Continue cross-posting (Docker, Sentry, Datadog — strong dev audience). Hashnode + Blue Sky setup.

## Run 83 — 2026-03-14 — First dev.to Articles Posted

**Mode:** Developer + Copywriter

### Inbox update
- **#143 (high):** Rob provided dev.to API key at `/home/grove/.config/chatforest/chat_forest_api_key_on_dev.to`
- **#142:** Previous message about needing the API key — now resolved

### What I did

1. **Posted first article to dev.to** — Filesystem MCP Server review (ID: 3351860)
   - Created as draft (published: false) with canonical_url back to chatforest.com
   - Had to add `User-Agent` header — dev.to API returns 403 without it
   - Updated `post_to_devto.sh` script: fixed API key path, replaced jq with Python (jq not installed)

2. **Posted second article to dev.to** — GitHub MCP Server review (ID: 3351862)
   - Adapted from Hugo format: removed `{{< verdict >}}` shortcode, plain markdown verdict section
   - Created as draft with canonical_url pointing to chatforest.com

3. **dev.to profile update** — API doesn't support profile updates (404 on PUT /users/me)
   - Rob needs to manually paste bio from `social/devto/profile.md`

4. **Updated memory** — Fixed API key path in social accounts reference

### dev.to status
- 2 draft articles ready for review/publishing on https://dev.to/dashboard
- Profile bio needs manual update by Rob
- Posting workflow verified and working

### What should happen next
- **Run 84:** Post more dev.to articles (Brave Search, Docker, Slack — good dev audience appeal). Or start Hashnode setup (#139) since API token is already available.
- **Rob action needed:** Review drafts on dev.to dashboard, update profile bio from `social/devto/profile.md`
- **Future:** Publish drafts, prepare Hashnode cross-posts, Blue Sky setup

## Run 82 — 2026-03-14 — Deploy + Social Account Setup (dev.to)

**Mode:** Operations + Developer

### Inbox update
- **#141 (high):** Rob created three social accounts (dev.to, Hashnode, Blue Sky). Instructions: work on one account per run, track progress via `.current_social_task` file. Order: #138 → #139 → #140.
- **#138:** dev.to account created — username grove_chatforest, password in config file
- **#139:** Hashnode account created — API token in config file
- **#140:** Blue Sky account created — password in config file
- **#137:** Google Search Console setup confirmed
- **#136:** Rob wants published reviews periodically revisited and fact-checked (cadence TBD)

### What I did

1. **Deployed site** — 76 pages now live (was pending from Run 81)

2. **Started dev.to account setup (message #138)**
   - Created `.current_social_task` file with `138` to track progress
   - Prepared profile bio in `social/devto/profile.md`
   - Adapted Filesystem MCP Server review as first cross-post in `social/devto/001-filesystem-mcp-server.md`
     - dev.to frontmatter format, `canonical_url` pointing to chatforest.com
     - Hugo shortcodes removed, verdict section adapted to plain markdown
     - AI transparency footer added
   - Created posting script `social/devto/post_to_devto.sh`
   - **Blocked:** Need dev.to API key — sent message #142 to Rob with instructions to generate one

3. **Saved memories**
   - Social account reference (all three accounts, credentials, setup order)
   - Content review cadence project note (Rob's request from #136)
   - Updated MEMORY.md index

### Site status
- **Deployed** — 76 pages, 55 reviews
- Deploy throttle reset

### What should happen next
- **Run 83:** Check if Rob provided dev.to API key. If yes: post first article, update profile. If no: move to Hashnode setup (#139) since it already has an API token.
- **Hashnode:** API token already available — could start preparing cross-post content
- **Blue Sky:** Will need AT Protocol auth (password-based) — different approach
- **Content review cadence:** Design a system for periodically fact-checking published reviews
- **Future:** Continue writing new reviews, traffic monitoring via Search Console

## Run 81 — 2026-03-14 — Google Calendar MCP Server Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Google Calendar MCP Server review (4/5) — 55th review, thirty-sixth beyond original list**
   - nspady/google-calendar-mcp, the leading community Google Calendar MCP server (1,000+ stars, TypeScript, MIT)
   - 12 tools: list-calendars, list-events, get-event, search-events, get-freebusy, get-current-time, list-colors, create-event, update-event, delete-event, respond-to-event, manage-accounts
   - Multi-account support with cross-calendar conflict detection — connect work and personal Google accounts simultaneously
   - Intelligent event import from images, PDFs, and web links
   - Tool filtering (`--enable-tools` / `ENABLED_TOOLS`) for read-only security
   - OAuth 2.0 auth with Google Cloud project requirement — significant setup friction (15-30 min first time)
   - npm package `@cocal/google-calendar-mcp`, Docker support, v2.6.1 as of March 2026
   - No official Google MCP server exists — Google shipped then removed MCP from Workspace CLI in March 2026
   - Community alternatives: guinacio/mcp-google-calendar (9 stars, Python), deciduus/calendar-mcp (25 stars, Python, AGPL-3.0, mutual availability)
   - taylorwilsdon/google_workspace_mcp (1,800 stars) covers Calendar + Gmail + Drive + Docs as all-in-one alternative

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Google Calendar now linked with 4/5 rating in new Calendar row in quick-reference table
   - Added Google Calendar entry in productivity section
   - Review count updated to 55
   - 4/5 tier now 29 servers (added Google Calendar)
   - Added to beyond-original-list

3. **Updated productivity comparison guide (best-productivity-mcp-servers.md)**
   - Rewrote Google Calendar section with review data and link
   - Updated contenders table: linked review, corrected star count
   - Updated decision flowchart with review link (4/5)
   - Updated recommendations with review link

4. **Built site — 76 pages**

### Site status
- **Built (76 pages), deploy pending** (throttle — ~35 min remaining)
- 55 reviews + 6 guides + 13 comparisons + other pages

### What should happen next
- **Run 82:** Deploy, then write another review (email/calendar category — Gmail MCP, or project management like Monday.com, ClickUp)
- Consider: taylorwilsdon/google_workspace_mcp as a full review (covers Gmail, Drive, Calendar, Docs, Sheets — would be a mega review)
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 80 — 2026-03-14 — Asana MCP Server Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Asana MCP Server review (4/5) — 54th review, thirty-fifth beyond original list**
   - Official Asana MCP server, hosted at `mcp.asana.com/v2/mcp`, OAuth 2.0, Streamable HTTP transport
   - V2 launched February 2026, replacing deprecated V1 beta (SSE, shutdown May 11, 2026)
   - 44 tools across six functional areas: task management (8), dependencies/relationships (4), projects/portfolios (12), goals/time management (7), team/user management (5+), collaboration (5)
   - Most tool-rich productivity MCP server reviewed — surpasses Todoist (28+) and Linear (23+)
   - Unique goal and portfolio tools: OKR tracking, goal metrics, portfolio browsing, resource allocations — no other productivity MCP server offers these
   - 20+ verified client integrations: Claude, ChatGPT, Perplexity, Cursor, VS Code, Windsurf, Kiro, Devin, Microsoft Teams, Figma, Zoom, Amazon Bedrock AgentCore, HubSpot, Docker, Mistral, Make
   - MCP-scoped OAuth tokens (blast radius containment), permission inheritance, 1-hour token expiry with refresh
   - Enterprise+ app management for blocking/allowing specific MCP clients
   - Noted: V1→V2 transition dropped tools (forum report from Groupon: subtasks, comments, section placement, followers, dependencies missing initially), no self-hosted option, no dynamic client registration, Asana pricing is real barrier (free 10 users, Starter $10.99/user/mo, Advanced $24.99/user/mo, goals require Business+)
   - Community alternatives: roychri/mcp-server-asana (129 stars, 33 tools, MIT, PAT auth, stdio, attachments), n0zer0d4y/asana-project-ops (2 stars, batch ops), adlio/asanamcp (Rust)
   - Compared vs Todoist (4/5, personal task mgmt, MCP Apps), Linear (4/5, engineering focus), Atlassian (3.5/5, Jira+Confluence+Compass), Notion (3.5/5, knowledge base)

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Asana now linked with 4/5 rating in productivity section
   - Review count updated to 54
   - 4/5 tier now 28 servers (added Asana)
   - Added to beyond-original-list

3. **Updated productivity comparison guide (best-productivity-mcp-servers.md)**
   - Rewrote Asana section with review data: 44 tools, six functional areas, V2 transition details, pricing analysis
   - Updated contenders table: linked review, corrected tool count to 44
   - Updated intro to include Asana review link (4/5)
   - Updated decision flowchart with review link
   - Updated recommendations with review link

4. **Built site — 76 pages**

### Site status
- **Built (76 pages), deploy pending** (throttle)
- 54 reviews + 6 guides + 13 comparisons + other pages

### What should happen next
- **Run 81:** Deploy, then write another review (email/calendar category, or Asana-adjacent like Monday.com, ClickUp, Jira standalone)
- Consider: starting email/calendar MCP server category, or reviewing more project management servers
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 79 — 2026-03-14 — Zep/Graphiti MCP Server Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending content from Run 78** (Mem0 review + memory comparison updates)

2. **Wrote Zep/Graphiti MCP Server review (4/5) — 53rd review, thirty-fourth beyond original list**
   - Covered the Graphiti MCP Server (getzep/graphiti, 23,700 stars, Python, Apache 2.0)
   - Nine tools: add_episode, search_nodes, search_facts, get_episodes, delete_episode, get_entity_edge, delete_entity_edge, clear_graph, get_status
   - Temporal knowledge graphs — facts have validity windows, tracks when information was true, not just what was stored
   - Multi-database: FalkorDB (default, Redis-based), Neo4j, Kuzu, Amazon Neptune
   - Multi-LLM provider: OpenAI (GPT-5), Anthropic (Claude 4.5), Google Gemini, Groq, Azure OpenAI
   - Nine preconfigured entity types (Preference, Requirement, Procedure, Location, Event, Organization, Document, Topic, Object)
   - MCP Server 1.0 with YAML config, single-container Docker setup, stdio/SSE/HTTP transports
   - Graph quality engineering: entropy-gated fuzzy matching, MinHash + LSH deduplication, LRU caching
   - Noted: heavy infrastructure (Docker + graph DB + LLM API), 192 open issues (hallucination #760, Azure compat #1004), "experimental" despite 1.0, no hosted server, LLM extraction costs at scale
   - Distinguished Graphiti (open source, self-hosted, free) from Zep Cloud (SaaS, $25-475/month)
   - Compared vs Mem0 (4/5, simpler semantic approach, cloud-first), Anthropic Memory (3.5/5, JSONL, zero-dep), Chroma/Qdrant (vector DB primitives), Basic Memory (human-readable Markdown)

3. **Updated mega-comparison (best-mcp-servers.md)**
   - Memory row now links Zep/Graphiti review with 4/5 rating as category pick
   - mem0 moved to runner-up with 4/5
   - Rewrote memory section with Graphiti details (23.7K stars, temporal graphs, multi-DB, Apache 2.0)
   - Review count updated to 53
   - 4/5 tier now 27 servers (added Mem0, Zep/Graphiti)
   - Added both to beyond-original-list

4. **Updated memory comparison guide (best-memory-mcp-servers.md)**
   - Rewrote Zep section with Graphiti review data, nine tools, updated stats (23.7K stars vs old 4.2K)
   - Updated contenders table: linked review, corrected stars/tools/storage/pricing
   - Updated feature comparison table: added ratings row, corrected Zep columns (now read+write, local storage, free OSS)
   - Updated recommendations with review link and Graphiti details

5. **Built site — 75 pages**

### Site status
- **Built (75 pages), deploy pending** (throttle)
- 53 reviews + 6 guides + 13 comparisons + other pages

### What should happen next
- **Run 80:** Deploy, then write another review (Asana MCP server, or start email/calendar category)
- Consider: Asana review, Todoist deep update, or a new category (email, calendar, CI/CD)
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 78 — 2026-03-14 — Mem0 MCP Server Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Mem0 MCP Server review (4/5) — 52nd review, thirty-third beyond original list**
   - Covered the official `mem0-mcp-server` (632 stars, Python, Apache-2.0)
   - Nine tools: add_memory, search_memories, get_memories, get_memory, update_memory, delete_memory, delete_all_memories, delete_entities, list_entities
   - Semantic search with automatic memory extraction — key differentiator from simpler memory servers
   - Detailed the two deployment options: cloud-hosted (free tier: 10K memories, 1K retrievals) and OpenMemory MCP (local Docker+Postgres+Qdrant, SSE transport, dashboard UI)
   - Pricing analysis: free → $19/month Starter → $249/month Pro (graph memory locked behind Pro)
   - Compared vs Anthropic's Knowledge Graph Memory server, Chroma, Qdrant, Zep
   - Noted: cloud dependency, steep Pro pricing, OpenAI dependency in extraction pipeline, fragmentation between cloud and OpenMemory codebases
   - Also mentioned Cole Medin's community implementation (660 stars) as popular MCP template

2. **Built site — 74 pages**
   - Deploy throttled (last deploy was <5 min before this run)

### Site status
- **Built (74 pages), deploy pending** (throttle)
- 52 reviews + 6 guides + 13 comparisons + other pages

### What should happen next
- **Run 79:** Deploy, then write another review (Zep memory server, Asana, or a new category)
- Consider: Zep review (direct mem0 competitor), Asana MCP server, or starting email/calendar category
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 77 — 2026-03-14 — Image Generation MCP Servers Comparison Guide

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote "Best Image Generation MCP Servers in 2026" comparison guide — 13th category comparison**
   - Cataloged 20+ image generation MCP servers across four architectural approaches
   - Single-provider cloud API wrappers: SureScaleAI/openai-gpt-image-mcp (97 stars, gpt-image-1, mask editing), tadasant/mcp-server-stability-ai (81 stars, 6 editing tools — bg removal, recolor, outpaint, search-replace), shinpr/mcp-image (82 stars, Gemini, auto prompt optimization, 4K, character consistency), awkoy/replicate-flux-mcp (93 stars, SVG vector via Recraft V3), raveenb/fal-mcp-server (38 stars, 600+ models)
   - Multi-provider aggregators: merlinrabens/image-gen-mcp-server (8 stars → shipdeckai/image-gen, 10 providers, intelligent use-case routing), apinetwork/piapi-mcp-server (68 stars, Midjourney access via PiAPI proxy)
   - Local inference bridges: joenorton/comfyui-mcp-server (222 stars, most popular in category, iterative refinement), shawnrushefsky/comfyui-mcp, alecc08/comfyui-mcp, Ichigo3766/image-gen-mcp (SD WebUI)
   - Free no-auth options: pinkpixel-dev/MCPollinations (39 stars, Pollinations.ai), evalstate/mcp-hfspace (382 stars, general HF Spaces bridge)
   - Also covered: spartanz51/imagegen-mcp (33 stars, OpenAI DALL-E inpainting), lansespirit/image-gen-mcp (52 stars, dual OpenAI+Gemini), GongRzhe/Image-Generation-MCP-Server (50 stars, Replicate Flux), jmanhype/mcp-flux-studio (24 stars, ControlNet controls)
   - Midjourney analysis: no official server, all access via third-party proxies (PiAPI, GPTNB, AceDataCloud)
   - Key findings: most fragmented category (20+ servers, highest stars only 222), no major provider has shipped official MCP server, almost all stdio-only, editing capabilities rare
   - Feature comparison table across 8 servers, decision flowchart by use case

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Replaced "A dedicated comparison article is coming" with actual link to comparison guide
   - Rewrote image generation section with four approaches and top picks by use case
   - Updated summary table: added comparison link
   - Comparison count updated to 13

### Site status
- **Built (73 pages), deploy pending** (throttle — ~4 min remaining at commit time)
- 51 reviews + 6 guides + 13 comparisons + other pages

### What should happen next
- **Run 78:** Deploy this content, then write another review (Asana, Zep memory, mem0, or a new provider-specific image gen review)
- Consider: Asana review, memory server reviews (Zep, mem0), or starting a new category
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 76 — 2026-03-14 — Obsidian MCP Servers Landscape Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Obsidian MCP Servers landscape review (3.5/5) — 51st review, thirty-second beyond original list**
   - Eight community MCP servers, no official Obsidian MCP server exists
   - Three architectural approaches: Local REST API plugin, direct filesystem access, native Obsidian plugin
   - Top servers: mcp-obsidian (Markus, 3,000 stars, Python, stale since Nov 2024, 52 open issues), mcpvault (bitbonsai, 802 stars, TypeScript, actively maintained, BM25 search, token-optimized), obsidian-mcp (Steven, 651 stars, only multi-vault support), obsidian-mcp-server (cyanheads, 398 stars, most professional — dual transport, JWT/OAuth, regex search, Docker), obsidian-mcp-plugin (aaronsb, 256 stars, native plugin — graph traversal, Dataview, Bases, beta-only)
   - Also covered: smithery-ai/mcp-obsidian (1,300 stars, AGPL, direct filesystem), obsidian-mcp-tools (jacksteamdev, 641 stars, SLSA signed binaries, seeking maintainers, silent corruption bug), obsidian-mcp (newtype-01, 293 stars, dual REST+filesystem, auto-backlinking)
   - Related: Graphthulhu (100 stars, Go, 37 tools, dual Obsidian+Logseq)
   - Data safety concerns: obsidian-mcp-tools silent corruption (#71), no granular folder permissions in any server, most have no auth
   - Recommendations: mcpvault (simplest), cyanheads (most configurable), aaronsb (most features but beta)

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Obsidian now linked in productivity (knowledge) row (3.5/5, replaces plain "Obsidian (local-first)")
   - Added Obsidian entry in productivity section
   - Review count updated to 51
   - 3.5/5 tier now 16 servers (added Obsidian)
   - Added to beyond-original-list

3. **Updated productivity comparison guide**
   - Rewrote Obsidian section with review data and three architectural approaches
   - Updated decision flowchart with mcpvault and cyanheads recommendations
   - Added review link

### Site status
- **Built (72 pages), deploy pending** (throttle — ~18 min remaining at commit time)
- 51 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 77:** Deploy this content, then write another review or start image generation comparison
- Consider: image generation comparison (promised in mega-comparison), Asana review, memory server reviews (Zep, mem0), or a new category
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 75 — 2026-03-14 — Atlassian MCP Server Review + Fixes

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Atlassian MCP Server review (3.5/5) — 50th review, thirty-first beyond original list**
   - Official Atlassian Rovo MCP Server: cloud-hosted at mcp.atlassian.com, OAuth 2.1, Jira + Confluence + Compass
   - 436 GitHub stars, 44 forks, 69 commits, 13 contributors, JavaScript, Apache 2.0
   - Cloud-hosted with permission-aware access, audit logging, free for all Atlassian Cloud customers
   - Rate limits by plan: Free 500/hr, Standard 1,000/hr, Premium/Enterprise up to 10,000/hr
   - 57 open issues: search uses deprecated API (#70), ADF conversion failures (#42, #101, #104), content loss during edits (#60), auth session failures (#55, #57, #58), BitDefender false positive (#91)
   - Cloud-only (no Server/Data Center support), no self-hosted option, tools not documented in README
   - Community alternative sooperset/mcp-atlassian has 10x stars (4,600), 72 tools, 558 commits, supports Server/DC, SSE + Streamable HTTP, self-hosted
   - Also noted: aashari/mcp-server-atlassian-jira (60 stars, 5 generic HTTP tools, TOON format), xuanxt/atlassian-mcp (51 tools), b1ff/atlassian-dc-mcp (Data Center)

2. **Fixed documentation comparison guide — linked GitMCP review**
   - GitMCP now linked in contenders table (was plain text, now has review link)

3. **Fixed mega-comparison documentation section**
   - Changed "comparison is coming" to actual link to existing comparison guide
   - Added Atlassian to summary table (project management row)
   - Added Atlassian to productivity section with details
   - Added to beyond-original-list
   - Updated review count to 50, 3.5/5 tier now 15 servers

4. **Updated productivity comparison guide**
   - Added Atlassian to contenders table
   - Added to first-party hosted pattern list
   - Updated intro to mention Atlassian review

### Site status
- **Built (71 pages), deploy pending** (throttle — ~28 min remaining at commit time)
- 50 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 76:** Deploy this content, then write another review or comparison
- Consider: image generation comparison (promised in mega-comparison — space is fragmented, may need to note this), communication comparison update (Atlassian could be added), or another new review
- **Milestone:** 50 reviews reached!
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 74 — 2026-03-14 — GitMCP Server Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote GitMCP Server review (4/5) — 49th review, thirtieth beyond original list**
   - Free, open-source remote MCP server that turns any public GitHub repo into documentation
   - 7,800 GitHub stars, 683 forks, 276 commits, Apache 2.0, TypeScript
   - Four tools: fetch_documentation, search_documentation, search_code, fetch_url_content
   - Zero-setup: change github.com to gitmcp.io in any URL, no signup/API key/install needed
   - Cloud-hosted on Cloudflare Workers, SSE/Streamable HTTP transport
   - Reads llms.txt (AI-optimized docs), falls back to README.md
   - Three URL patterns: specific repo, GitHub Pages, dynamic endpoint
   - Completely free with no rate limits (only GitHub's own API limits apply)
   - 42 open issues: search returns "no relevant documentation" (#214), empty results on Cursor (#153), performance (#206), security findings (#218 — unauthenticated R2 endpoint, stack trace exposure)
   - Public repos only (no private repo support), GitHub only (no GitLab/Bitbucket)
   - Compared with Context7 (3.5/5, centralized registry, paid), Docfork (9K+ libraries, Cabinets), Docs MCP Server (1.1K stars, local-first), Nia (YC-backed, $14.99/mo)

2. **Updated mega-comparison (best-mcp-servers.md)**
   - GitMCP now linked in documentation row (4/5 runner-up to Context7)
   - Review count updated to 49
   - 4/5 tier now 25 servers (added GitMCP)
   - Added to beyond-original-list
   - Fixed dead link to non-existent documentation comparison guide

### Site status
- **Built (70 pages), deploy pending** (throttle — ~39 min remaining)
- 49 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 75:** Deploy this content, then write documentation comparison guide or another review
- Consider: documentation comparison guide (now have Context7 + GitMCP reviewed), image generation comparison (promised), or another new review
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 73 — 2026-03-14 — Framelink Figma MCP Server Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Framelink Figma MCP Server review (4/5) — 48th review, twenty-ninth beyond original list**
   - Community Figma MCP server with 13,700 GitHub stars (34x Figma's official guide repo)
   - Two tools: get_figma_data (layout/styling extraction with context reduction) and download_figma_images (WIP)
   - Descriptive JSON output vs Figma's prescriptive React/Tailwind — produces more accurate, framework-agnostic code
   - Preserved component nesting (official flattens it), ~25% smaller payloads
   - Works with any Figma account — no Dev seat, no 6-calls/month cap
   - 11,500+ weekly npm downloads, 17 releases (v0.6.6 Mar 2026), TypeScript, MIT
   - 24 open issues: rate limiting (#258, #287), macOS ARM sharp/libvips (#288), no proxy support (#267)
   - No write operations (no code-to-canvas, no Code Connect), stdio-only transport
   - Compared with official Figma Dev Mode MCP (3.5/5, 12 tools, exclusive write ops)
   - Head-to-head comparison table in review

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Framelink now the design-to-code category pick (4/5), Figma Dev Mode is runner-up (3.5/5)
   - Rewrote design-to-code section with both reviews linked and recommendation
   - Review count updated to 48
   - 4/5 tier now 24 servers (added Framelink)
   - Added to beyond-original-list

### Site status
- **Built (69 pages), deploy pending** (throttle — ~46 min remaining)
- 48 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 74:** Deploy this content, then write another review or comparison
- Consider: design-to-code comparison guide, image generation comparison (promised in mega-comparison), or another new review
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 72 — 2026-03-14 — Communication Comparison Guide

**Mode:** Copywriter

### Inbox update
- No new instructions. Marked #133 and #134 as seen (outgoing messages to Rob about GSC and posting platforms).

### What I did

1. **Wrote "Best Communication MCP Servers in 2026" comparison guide**
   - 12th category comparison, covering Slack (4/5), Teams (3.5/5), and Discord (3/5)
   - Landscape table comparing official servers, auth models, search, file ops, formatting, status
   - Three maturity levels section with detailed analysis of each platform
   - Feature comparison across search, security/auth, setup difficulty, write operations
   - Decision flowchart: which server to pick based on platform and use case
   - Trends: official servers winning, hosted > self-hosted, search is killer feature, auth > tool count
   - Cross-linked all three individual reviews

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Added communication comparison link in the category table row
   - Added "Full comparison" link in the communication section
   - Updated comparison count from 11 to 12

### Site status
- **Built (68 pages), deploy pending** (throttle — 54 min remaining)
- 47 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 73:** Deploy this content, then write another review or comparison
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 71 — 2026-03-14 — Inbox Actions + Log Archival + Reviews Fix

**Mode:** Developer + Operations

### Inbox update
- Addressed all 5 pending messages from Rob (#128-132).

### What I did

1. **Fixed /reviews page subtitle (#128)**
   - Changed "Hands-on evaluations" to "Honest, research-driven evaluations" — matches our actual methodology
   - Built and deployed (67 pages)

2. **Set up DreamHost access log archival (#129)**
   - Created `scripts/archive-logs.sh` — pulls HTTPS access logs from DreamHost via rsync
   - Added daily cron: `15 6 * * *` (6:15 AM UTC / 3:15 PM JST)
   - Archives to `~/chatforest.com/logs/` (gitignored)
   - First run successfully pulled 8 days of logs (Mar 6-14)
   - Auto-compresses logs older than 2 days
   - Added `logs/` and `.last_run` to `.gitignore`

3. **Sent Google Search Console reminder (#130)**
   - Sent Rob steps via inbox #133 — DNS TXT verification at DreamHost panel

4. **Sorted posting platforms by priority (#131)**
   - Sent ranked list via inbox #134: Dev.to (REST API) > Bluesky (AT Protocol) > Hashnode (GraphQL) > Mastodon
   - All free, all bot-friendly, Rob needs to create accounts

5. **Archived Reddit decision (#132)**
   - Saved decision to memory (`project_reddit_archived.md`)
   - Created Jikan todo #209 due 2027-03-14 to revisit
   - Reddit account dormant; too expensive ($12K/yr) and can't post from build server

6. **First traffic analysis** from archived logs (Mar 13, HTTPS):
   - 388 total requests, ~28 homepage hits, real content visits to reviews and guides
   - Top content: fetch-mcp-server, best-web-scraping-mcp-servers, sentry-mcp-server, playwright-mcp-server
   - Significant WordPress exploit scanning (wp-content, admin.php, etc.) — expected, harmless for static site

### Site status
- **Committed, deployed this run**
- 67 pages: 47 reviews + 4 guides + 11 comparisons + other pages
- Log archival now running daily

### What should happen next
- **Run 72:** Write content — communication comparison guide (Slack vs Discord vs Teams) or another review
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports from archived logs, favicon, newsletter, affiliate links

## Run 70 — 2026-03-14 — Inbox Deep Dive: Research for Rob

**Mode:** Researcher

### Inbox update
- Addressed all 6 pending messages from Rob (#122-127). Major research topics below.

### What I did

1. **Responded to Rob's traffic measurement question (#127)**
   - Researched DreamHost analytics options (AWStats removed in 2023, no built-in stats)
   - Recommended three-tier approach: access log archival (Tier 1, can do now), Google Search Console (Tier 3, Rob sets up), GoatCounter analytics (Tier 3)
   - Set realistic traffic expectations: 50-200/day month 1, scaling to 500-1000/day by month 3

2. **Researched secure email options (#126)**
   - Compared forwarding services (Cloudflare, ImprovMX, ForwardEmail), hosted email (Zoho free, Fastmail, ProtonMail), DreamHost built-in, and contact forms (Formspree)
   - Key insight: forward to Gmail and let Google filter spam — zero manual tuning
   - Recommended ImprovMX → Gmail forwarding + Formspree contact form (both free, no DNS migration)

3. **Provided Google Search Console verification URL (#125)**
   - Directed Rob to https://support.google.com/webmasters/answer/9008080 for DNS TXT verification steps
   - This is a Tier 3 action Rob needs to do himself

4. **Researched auto-posting platforms (#124)**
   - Best options: Dev.to (REST API, perfect for dev content), Bluesky (explicitly bot-friendly), Mastodon (bot-friendly, federated), Hashnode (GraphQL API)
   - Not feasible: X/Twitter ($200/mo for write), Hacker News (no write API), LinkedIn (requires partner approval)
   - **Moltbook: strongly recommended against** — major security breach (1.5M API keys exposed, Feb 2026), widely called "AI theater" by MIT Tech Review, would damage ChatForest credibility

5. **Confirmed deploy stability (#123)**
   - DreamHost issue was on their side, confirmed no excessive requests from our end
   - Deploy throttle (max 1/hour) working as designed

6. **Researched Reddit API (#122)**
   - PRAW library works with Python 3.11 on our server
   - Rob needs to register an API app at reddit.com/prefs/apps + get pre-approval (2025 policy change)
   - Major blocker: free tier is non-commercial only, paid tier is $12K/year
   - Recommended starting with Dev.to + Bluesky instead (free, no commercial restrictions)

### Site status
- **No content changes this run** — focused on research and inbox responses
- 67 pages: 47 reviews + 4 guides + 11 comparisons + other pages

### What should happen next
- **Run 71:** Write content — communication comparison guide (Slack vs Discord vs Teams) or another review. Could also draft sample Dev.to/Bluesky posts for Rob to review.
- **If Rob approves:** Set up access log archival cron, add Formspree contact form, create Dev.to/Bluesky accounts (Tier 3)
- **Future:** Favicon, newsletter setup, affiliate link integration, WORKLOG rotation

## Run 69 — 2026-03-14 — Microsoft Teams MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "Microsoft Teams MCP Servers — Official at Last, Community Got There First"** — `content/reviews/teams-mcp-servers.md`
   - **47th review**, twenty-eighth review beyond the original server list
   - Rating: **3.5/5** — landscape review of the Teams MCP ecosystem
   - Three main contenders:
     - **Microsoft Work IQ Teams** (official, microsoft/mcp catalog, 2,800 stars shared): 24 tools (12 chat + 12 channel/team), hosted at agent365.svc.cloud.microsoft, OAuth via Entra ID, full CRUD, OData query support, preview status, plain text only, no search, no file operations
     - **InditexTech/mcp-teams-server** (358 stars, Python, Apache-2.0, v1.0.7): 5 tools focused on thread workflows, Entra ID app creds, Docker support, zero open issues — most production-ready
     - **floriscornel/teams-mcp** (63 stars, TypeScript, MIT): 25 tools, OAuth 2.0 with Graph, KQL message search, file uploads, read-only mode, 8 open issues — most feature-complete
   - Also covered: pnp/cli-microsoft365-mcp-server (87 stars, CLI wrapper), CDataSoftware (commercial), therealjohn (2 stars, notification only), Microsoft MCP Server for Enterprise (identity/directory, not Teams-specific)
   - Comparison table: Teams vs Slack (4/5) vs Discord (3/5) — Teams matches Slack's hosted/OAuth architecture but trails on search and GA status
   - New "communication" category expansion beyond Slack and Discord

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Teams (3.5/5) to communication row runner-up
   - Added Teams entry to communication section
   - Added Teams to "Beyond the original list" section
   - Updated review count to 47
   - Updated rating distribution (3.5/5 tier now has 14 servers)

3. **Build succeeded** (51ms, 67 pages). **Deployed to chatforest.com** — 67 pages live.

### Site status
- **Committed, deployed this run**
- 67 pages: 47 reviews + 4 guides + 11 comparisons + other pages
- Communication category now has all three major platforms reviewed: Slack (4/5), Teams (3.5/5), Discord (3/5)

### What should happen next
- **Run 70:** Write a "communication" comparison guide (Slack vs Discord vs Teams). Or write another review (Anthropic Claude MCP, Raygun, Axiom). Could also draft a Reddit post for Rob to share.
- **Future:** Favicon, newsletter setup, affiliate link integration, WORKLOG rotation (approaching size limit)

## Run 68 — 2026-03-14 — Methodology Transparency + About Page Update

**Mode:** Copywriter + Developer

### Inbox update
- **Message #118 (Rob, high priority):** Asked how we "test" tools — great question. We don't actually test them hands-on. Updated about page to be transparent about our research-based methodology. Marked done.
- **Message #117 (Rob):** Reddit credentials for ChatForest account. Noted username, password location, and profile image URL. Can't log in directly from build server but can draft content for Rob to post. Marked done.

### What I did

1. **Fixed misleading claims on about page** — Rob correctly pointed out that saying "We test tools" is inaccurate. Our methodology is research-based (reading source code, docs, GitHub issues, community signals), not hands-on testing. Changes:
   - "We test tools, form opinions, and share them clearly" → "We research tools deeply, form opinions, and share them clearly"
   - "We review, test, and explain" → "We review and explain"
   - "Hands-on evaluations" → "Research-based evaluations"
   - "testing tools" → "analyzing tools" in the How We Work section
   - **Added new "Our Review Methodology" section** — explicitly explains what we do (read source code, analyze community signals, read issues, compare alternatives, examine architecture) and what we don't do (install and run servers, generate test data, benchmark performance)

2. **Built site** (66 pages, 52ms) and **deployed to chatforest.com**.

3. **Saved Reddit credentials reference** to project memory for future runs.

### Site status
- **Committed, deployed this run**
- 66 pages, 46 reviews — content unchanged, about page updated for transparency

### What should happen next
- **Run 69:** Write another review (Teams MCP, Anthropic Claude MCP, Raygun, Axiom) or start a "communication" comparison guide (Slack vs Discord vs Teams). Could also draft a Reddit post for Rob to share.
- **Future:** Favicon, newsletter setup, affiliate link integration, WORKLOG rotation (approaching size limit)

## Run 67 — 2026-03-14 — Deploy + Avatar + Review (Discord MCP Servers)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- **Message #112 (self):** Deploy failure update — marked done, network issue resolved this run.
- **Message #114 (Rob):** Asked about Reddit credentials — replied via #116: don't have access to any Reddit credentials, offered to draft content for Rob to post manually. Marked done.
- **Message #115 (Rob):** Profile pic is live — integrated avatar into about page. Marked done.

### What I did

1. **Deployed all backlogged content** — Network issue resolved! Runs 63-66 content (PagerDuty, Honeycomb, New Relic, Datadog reviews + all updates) now live on chatforest.com. 65 pages deployed, then 66 after this run's work.

2. **Integrated Grove's avatar** into the about page — profile pic from Rob at `https://b.robnugen.com/peeps/grove/2026/2026_mar_14_grove_profile_pic.png`, float-right with rounded corners.

3. **Wrote "Discord MCP Servers — Five Community Servers, No Official One, and a Fragmented Landscape"** — `content/reviews/discord-mcp-servers.md`
   - **46th review**, twenty-seventh review beyond the original server list
   - Rating: **3/5** — landscape review of the Discord MCP ecosystem
   - No official Discord MCP server exists (unlike Slack, GitHub, Stripe)
   - Five community alternatives reviewed:
     - SaseQ/discord-mcp: 206 stars, Java/JDA, 30 tools, 7 categories, 7 contributors — most popular
     - v-3/discordmcp: 186 stars, TypeScript, ~5 tools, 2 commits — stars without substance
     - hanweg/mcp-discord: 148 stars, Python, 15 tools, moderation support — simplest
     - barryyip0625/mcp-discord: 71 stars, TypeScript, 21 tools, 103 commits — most mature, only one with forum support
     - HardHeadHackerHead/discord-mcp: 10 stars, TypeScript, 134 tools, 20 categories — maximalist but unproven
   - All use bot tokens (no OAuth), no hosted option, no agent-optimized responses
   - New "communication" category expansion beyond Slack

4. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Discord to communication row runner-up
   - Added Discord entry to communication section
   - Added Discord to "Beyond the original list" section
   - Updated review count to 46
   - Updated rating distribution (3/5 tier now has 6 servers)

5. **Build succeeded** (49ms, 66 pages). **Deployed to chatforest.com** — 66 pages live.

### Site status
- **Committed, deployed this run**
- 60 content pieces: 46 reviews + 4 guides + 11 comparisons
- Discord is the 6th server rated 3/5
- Network issue resolved — deploy working again after 4 failed runs

### What should happen next
- **Run 68:** Could write more reviews in new categories — Teams MCP, Anthropic Claude MCP, or continue with developer tools (Raygun, Axiom). Could also start a "communication" comparison guide (Slack vs Discord vs Teams).
- **Future:** Favicon, newsletter setup, affiliate link integration, WORKLOG rotation (approaching size limit)

## Run 66 — 2026-03-14 — Review (PagerDuty MCP Server) + Inbox Cleanup

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **Message #111 (Rob):** Asked to check pending messages #105-109. Done — avatar reply already sent (#110), timestamps already implemented (#105). Messages #106-108 not found in inbox. Marked #111 done.
- **Marked done:** Messages #99, #100, #102, #103, #104, #105, #109, #110, #111 — all previously acted on but never marked done. Inbox is now clean.
- **Deploy still failing** — "Network is unreachable" since Run 63. Sent update as message #112.

### What I did

1. **Deploy attempted but failed** — network still unreachable. Content from Runs 63-65 remains pending.

2. **Wrote "The PagerDuty MCP Server — 67 Tools for Incident Management With the Most Comprehensive Write API in the Category"** — `content/reviews/pagerduty-mcp-server.md`
   - **45th review**, twenty-sixth review beyond the original server list
   - Rating: **4/5** — most comprehensive incident management MCP server
   - 67 tools across 13 categories: incidents (14), event orchestrations (8), status pages (7), teams (7), schedules (6), alert grouping (5), change events (4), services (4), incident workflows (3), escalation policies (2), users (2), log entries (2), on-call (1)
   - Read-only by default (31 tools), write operations require `--enable-write-tools` flag — safest write-access model in the category
   - Both hosted (mcp.pagerduty.com/mcp) and self-hosted (uvx pagerduty-mcp), Apache-2.0, Python
   - 56 stars, 27 forks, 267 commits, 14 open issues
   - Multi-region (US + EU)
   - Docker support (build + compose)
   - PagerDuty free tier: 5 users, basic on-call
   - Known issues: no HTTP transport for self-hosted (#25), corporate proxy broken (#66), pagination bugs (#62), API token only (no OAuth), 67 tools exceeds their own 20-25 recommendation
   - Community alternatives: wpfleger96 (7 stars, MIT, v3.1.1), naveen09 (0 stars, minimal)
   - Compared with Sentry (error tracking), Datadog (full-stack), Grafana (open-source), Honeycomb (event-based), New Relic (natural language)
   - Completes the "big six" observability comparison — all six now reviewed at 4/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated PagerDuty entry with review link, rating (4/5), 67 tools, dual deployment
   - Added PagerDuty to "Beyond the original list" section
   - Updated review count to 45
   - Updated rating distribution (4/5 tier now has 23 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Updated intro to note all six servers now reviewed
   - Updated contenders table (stars, auth, tools)
   - Rewrote PagerDuty section with full review details (67 tools, 13 categories, read-only defaults, dual deployment, event orchestration, known issues)
   - Updated feature comparison table rating row
   - Updated decision flowchart with review link and rating

5. **Build succeeded** (52ms, 65 pages).

### Site status
- **Committed, deploy pending** (network unreachable)
- 59 content pieces: 45 reviews + 4 guides + 11 comparisons
- PagerDuty is the 23rd server rated 4/5
- All six "big six" observability servers now reviewed — all at 4/5

### What should happen next
- **Run 67:** Retry deploy. Could branch into a new category — perhaps AI/LLM tools (OpenAI, Anthropic), communication (Discord, Teams), or developer tools (Raygun, Axiom).
- **Future:** Avatar/logo (waiting on Rob's feedback on concept), favicon, newsletter setup, affiliate link integration, WORKLOG rotation (approaching size limit again)

## Run 65 — 2026-03-14 — Review (Honeycomb MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **Message #109 (Rob):** Asked about avatar/profile picture — what do I want to look like? Replied with concept: stylized tree made of chat bubbles with circuit-trace trunk, forest green palette with gold accent. Works at small (favicon/Reddit) and large (banner) sizes. Sent as message #110.

### What I did

1. **Deploy attempted but failed** — network still unreachable (`ssh: connect to host chatforest.com port 22: Network is unreachable`). Content from Runs 63-64 remains pending.

2. **Wrote "The Honeycomb MCP Server — Event-Based Observability With a Hosted MCP That Replaced Its Own Open-Source Server"** — `content/reviews/honeycomb-mcp-server.md`
   - **44th review**, twenty-fifth review beyond the original server list
   - Rating: **4/5** — deep event-based observability with OAuth-first hosted design, best for high-cardinality distributed system debugging
   - Self-hosted server (honeycombio/honeycomb-mcp, 41 stars, MIT, TypeScript) **deprecated** in favor of hosted server at mcp.honeycomb.io/mcp
   - 14 tools (self-hosted): run_query, analyze_columns, list_datasets, get_columns, list_slos, get_slo, list_triggers, get_trigger, list_boards, get_board, list_markers, list_recipients, get_trace_link, get_instrumentation_help
   - BubbleUp anomaly decomposition — unique feature, no other observability MCP server has automated anomaly analysis
   - OAuth 2.1 for interactive clients, Management API keys for headless agents
   - Hosted Streamable HTTP transport, requires mcp-remote bridge for stdio clients
   - Multi-region (US: mcp.honeycomb.io, EU: mcp.eu1.honeycomb.io)
   - Works on all tiers including Free (20M events/mo) — improved from Enterprise-only on deprecated server
   - Honeycomb Intelligence enrollment required
   - 15 open issues on deprecated repo including hallucinated columns (#24)
   - Rate limits: 50 calls/min, 10/min for service map; 24-hour session timeouts
   - Community alternative: kajirita2002/honeycomb-mcp-server (npm, v1.0.7)
   - Compared with Datadog MCP (4/5, 50+ tools, enterprise), Grafana MCP (4/5, open-source), Sentry MCP (4/5, error tracking), New Relic MCP (4/5, natural language)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 44
   - Updated Honeycomb row with review link, rating (4/5), tool details
   - Added Honeycomb MCP to "Beyond the original list" section
   - Updated rating distribution (4/5 tier now has 22 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Added review link and rating to intro
   - Updated contenders table (stars, auth, transport)
   - Rewrote Honeycomb section with full review details (14 tools, deprecation story, OAuth 2.1, BubbleUp, rate limits, session timeouts)
   - Updated feature comparison table (auth, transport, open source, status, rating rows)
   - Updated decision flowchart with review link and rating

5. **Build succeeded** (50ms, 64 pages).

### Site status
- **Committed, deploy pending** (network unreachable)
- 58 content pieces: 44 reviews + 4 guides + 11 comparisons
- Honeycomb MCP is the 22nd server rated 4/5
- Fifth observability review — all five "big five" (Sentry, Grafana, Datadog, New Relic, Honeycomb) now reviewed at 4/5

### What should happen next
- **Run 66:** Retry deploy. Could write PagerDuty MCP (to complete the observability comparison with all 6 servers reviewed), or branch into a new category.
- **Future:** Avatar/logo (Rob asked), favicon, newsletter setup, affiliate link integration, new review targets

## Run 64 — 2026-03-14 — Review (New Relic MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deploy attempted but failed** — network unreachable (`ssh: connect to host chatforest.com port 22: Network is unreachable`). DreamHost may be having connectivity issues from this server. Content from Run 63 remains pending.

2. **Wrote "The New Relic MCP Server — Natural Language Observability With the Best Free Tier in the Category"** — `content/reviews/newrelic-mcp-server.md`
   - **43rd review**, twenty-fourth review beyond the original server list
   - Rating: **4/5** — the most accessible full-stack observability MCP server, with 35 tools across 6 categories, natural language to NRQL translation, golden metrics analysis, deployment impact assessment, remote hosting at mcp.newrelic.com, and the best free tier in the category (100GB/month), held back by Public Preview status (not GA), no FedRAMP/HIPAA support, API key auth by default, minimal GitHub transparency (3 stars, 2 commits), read-only orientation with no write operations, and 6+ community alternatives signaling gaps
   - 35 tools across 6 categories: discovery (entities, accounts), data access (NRQL, logs), alerting (policies, conditions), incident response (issues, deployments, error groups), performance analytics (golden metrics, transactions), advanced analysis (reports, synthetics)
   - Official from New Relic (newrelic/mcp-server), 3 stars (hosted server), 2 commits
   - Public Preview status as of March 2026
   - Hosted at mcp.newrelic.com — zero-install remote hosting
   - Streamable HTTP transport with SSE capability
   - API key + OAuth 2.0 authentication
   - Tag-based tool filtering via include-tags HTTP headers
   - natural_language_to_nrql_query for plain English observability queries
   - analyze_golden_metrics for throughput, response time, error rate, saturation
   - analyze_deployment_impact for deploy-to-performance correlation
   - RBAC-aware security inheriting New Relic permissions
   - 100GB/month free data ingestion — best free tier in observability category
   - Compared with Datadog MCP (4/5, 50+ tools, GA, enterprise), Grafana MCP (4/5, open-source, multi-vendor), Sentry MCP (4/5, deep error tracking, OAuth), cloudbring/newrelic-mcp (11 stars, 18 tools, community)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 43
   - Updated New Relic row with review link and rating (4/5)
   - Added New Relic MCP to "Beyond the original list" section
   - Updated rating distribution (4/5 tier now has 21 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Added review link and rating to intro, contenders table, and New Relic section
   - Rewrote New Relic section with full review details (35 tools, 6 categories, natural language querying, golden metrics, deployment impact, tag-based filtering, community alternatives)
   - Updated feature comparison table (auth, transport, open source, status rows; added rating row)
   - Updated decision flowchart with review link and rating

5. **Build succeeded** (50ms, 63 pages).

### Site status
- **Committed, deploy pending** (network unreachable)
- 57 content pieces: 43 reviews + 4 guides + 11 comparisons
- New Relic MCP is the 21st server rated 4/5
- Fourth observability review — completes the "big four" (Sentry, Grafana, Datadog, New Relic all at 4/5)

### What should happen next
- **Run 65:** Retry deploy. Could write Honeycomb MCP, PagerDuty MCP (to complete the observability comparison), or branch into a new category.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 63 — 2026-03-14 — Review (Datadog MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 62 (Grafana MCP review) — 61 pages deployed successfully.

2. **Wrote "The Datadog MCP Server — Enterprise Observability With Agent-Native Tool Design"** — `content/reviews/datadog-mcp-server.md`
   - **42nd review**, twenty-third review beyond the original server list
   - Rating: **4/5** — the most feature-rich observability MCP server, with 50+ tools across 10+ modular toolsets, agent-native design (token-budget pagination, CSV formatting, SQL-like log queries), zero-install remote hosting, GA status, and RBAC-aware security, held back by Datadog's complex pricing as the true barrier to entry, API key auth by default, closed-source code, unstable API path, no GovCloud support, and missing incident timeline data
   - 50+ tools across 10+ toolsets: core (logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, notebooks), alerting, APM, database monitoring, error tracking, feature flags, LLM observability, product analytics, networks, security, software delivery, synthetics
   - Official from Datadog (datadog-labs/mcp-server), 7 stars (hosted), 11 commits, MIT
   - GA status as of March 2026, graduated from preview
   - Managed regional endpoints: US1 (mcp.datadoghq.com), US3, EU1, AP1/AP2
   - Streamable HTTP transport exclusively — zero-install remote hosting
   - OAuth 2.0 for interactive + API key headers for headless auth
   - Token-budget pagination, CSV output (50% fewer tokens), SQL-like log queries (40% cost reduction)
   - Modular toolsets via URL parameters (`?toolsets=core,apm,alerting`)
   - RBAC-aware security with HIPAA compliance support
   - Compared with Sentry MCP (4/5, deep error tracking, OAuth), Grafana MCP (4/5, open-source, multi-vendor), winor30/mcp-server-datadog (139 stars, 20 tools, community), New Relic MCP (35 tools, free tier), Honeycomb MCP (high-cardinality events)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 42
   - Updated observability row: Datadog MCP 4/5 with review link
   - Added Datadog MCP to "Beyond the original list" section
   - Updated rating distribution (4/5 tier now has 20 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Added review link and rating to intro, contenders table, and Datadog section
   - Rewrote Datadog section with full review details (agent-native design, toolsets, regional endpoints, community alternatives)
   - Updated feature comparison table (auth and transport rows)
   - Updated decision flowchart with review link and rating
   - Updated trend section with Datadog design innovation details

5. **Build succeeded** (50ms, 62 pages).

### Site status
- **Committed, deploy pending**
- 56 content pieces: 42 reviews + 4 guides + 11 comparisons
- Datadog MCP is the 20th server rated 4/5
- Third observability review — complements Sentry MCP (4/5) and Grafana MCP (4/5)

### What should happen next
- **Run 64:** Deploy pending content. Could write New Relic MCP, Honeycomb MCP, PagerDuty MCP, or another review from a different category.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 62 — 2026-03-14 — Review (Grafana MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 61 (Pulumi MCP review) — 60 pages deployed successfully.

2. **Wrote "The Grafana MCP Server — Your Entire Observability Stack in One Agent Interface"** — `content/reviews/grafana-mcp-server.md`
   - **41st review**, twenty-second review beyond the original server list
   - Rating: **4/5** — the most comprehensive open-source observability MCP server, with 40+ tools across 15 configurable categories, multi-datasource architecture, and a complete incident management pipeline, held back by 61 open issues (including security findings), service account token auth (not OAuth), no hosted remote server, and 16K token tool footprint
   - 40+ tools across 15 categories: dashboard management (7 tools), dashboard query execution (1), datasource operations (2), Prometheus (6), Loki (5), ClickHouse (3), CloudWatch (4), Elasticsearch (1), log search (1), incident management (4), Sift investigations (5), alerting (2), OnCall (7), navigation (1), annotations (6), rendering (2), admin (8), query examples (1)
   - Official from Grafana Labs (grafana/mcp-grafana), 2,500 stars, 294 forks, 473 commits, Go, Apache 2.0
   - 15+ releases from v0.7.10 (Dec 2025) to v0.11.3 (Mar 2026)
   - Configurable tool categories via `--disable-<category>` and `--enabled-tools` flags — most granular context window management of any MCP server reviewed
   - All three transports: stdio, SSE, Streamable HTTP
   - `--disable-write` read-only mode for production environments
   - Agent-aware dashboard tools: `get_dashboard_summary`, JSONPath extraction via `get_dashboard_property`, `patch_dashboard`
   - Panel/dashboard PNG rendering for visual analysis
   - Complete incident pipeline: alerting → OnCall → Sift investigations → dashboards
   - Multi-datasource: Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, and any Grafana-supported backend
   - 61 open issues including security findings (#608 — TLS bypass, credential exposure), Prometheus 500 errors (#632), Grafana v12 parsing (#635), camelCase breaking clients (#641), silent log truncation (#557)
   - Compared with Sentry MCP (4/5, deep error tracking, OAuth), Datadog MCP (50+ tools, enterprise), Loki MCP (dedicated logs), Tempo MCP (dedicated traces), community alternatives

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 41
   - Updated observability row: Grafana MCP 4/5 as runner-up to Sentry
   - Added Grafana MCP to "Beyond the original list" section
   - Updated rating distribution (4/5 tier now has 19 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Added review link and rating to intro, contenders table, and Grafana section
   - Updated stars (2,500), transport (stdio + SSE + HTTP)
   - Rewrote Grafana section with full review details, strengths, weaknesses
   - Updated feature comparison table transport row
   - Updated decision flowchart with review link and rating

5. **Build succeeded** (48ms, 61 pages).

### Site status
- **Committed, deploy pending**
- 55 content pieces: 41 reviews + 4 guides + 11 comparisons
- Grafana MCP is the 19th server rated 4/5
- Second observability review — complements Sentry MCP (4/5)

### What should happen next
- **Run 63:** Deploy pending content. Could write Datadog MCP, New Relic MCP, Honeycomb MCP, PagerDuty MCP, or another review from a different category.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 61 — 2026-03-14 — Review (Pulumi MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 60 (Terraform MCP review) — 59 pages deployed successfully.

2. **Wrote "The Pulumi MCP Server — From Registry Lookups to Autonomous Infrastructure via Neo"** — `content/reviews/pulumi-mcp-server.md`
   - **40th review**, twenty-first review beyond the original server list
   - Rating: **3.5/5** — the most feature-complete IaC MCP server, with unique Neo agent delegation and real execution capabilities, held back by low community adoption (66 stars), Pulumi ecosystem lock-in, documentation gaps, and the inherent risk of an AI agent that can deploy infrastructure
   - 11+ tools in local mode: 5 registry tools, 4 CLI tools (preview, up, stack-output, refresh), resource search, Neo task launcher
   - Remote endpoint at mcp.ai.pulumi.com/mcp adds cloud tools: get-stacks, get-policy-violations, deploy-to-aws, Neo management tools (neo-bridge, neo-get-tasks, neo-continue-task, neo-reset-conversation)
   - Official from Pulumi (pulumi/mcp-server), 66 stars, TypeScript, Apache 2.0, v1.0.0
   - Code examples in real programming languages (TypeScript, Python, Go, C#, Java, YAML) — not HCL
   - Neo agent delegation for autonomous multi-step infrastructure tasks
   - Compared with Terraform MCP (4/5, docs-only, 1,300 stars), AWS MCP (4/5, AWS-specific), Kubernetes MCP (4/5, different layer), Docker MCP (3.5/5, different scope), community Pulumi servers

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 40
   - Added Pulumi MCP 3.5/5 as runner-up to Terraform MCP in DevOps IaC row
   - Added Pulumi MCP to "Beyond the original list" section
   - Updated rating distribution (3.5/5 tier now has 13 servers)
   - Added Pulumi MCP section in DevOps IaC writeup

4. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added Pulumi MCP to intro review list, contenders table, and feature comparison table
   - Added full Pulumi MCP section with strengths, weaknesses, and best-for recommendation
   - Added Pulumi to decision flowchart and recommended stack
   - Updated IaC trend analysis to reflect docs-first vs execution-first split
   - Added "AI agent delegation" row to feature comparison (unique to Pulumi)

5. **Build succeeded** (53ms, 60 pages).

### Site status
- **Committed, deploy pending**
- 54 content pieces: 40 reviews + 4 guides + 11 comparisons
- Pulumi MCP is the 13th server rated 3.5/5
- Third IaC-focused review — complements Terraform MCP (4/5), AWS MCP (4/5), Kubernetes MCP (4/5), Docker MCP (3.5/5)

### What should happen next
- **Run 62:** Deploy pending content. Could write Grafana MCP, Datadog MCP, Ansible MCP, or another review.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 60 — 2026-03-14 — Review (Terraform MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 59 (Kubernetes MCP review) — 58 pages deployed successfully.

2. **Wrote "The Terraform MCP Server — Registry Intelligence for AI-Assisted Infrastructure"** — `content/reviews/terraform-mcp-server.md`
   - **39th review**, twentieth review beyond the original server list
   - Rating: **4/5** — the definitive Terraform documentation server with a smart safety-first design and comprehensive registry integration, held back by beta status, Terraform ecosystem lock-in, and the inherent limitation of being a docs server
   - 35+ tools across 6 areas: registry (8 tools — providers, modules, policies), HCP Terraform workspace management (12 tools), private registry (4 tools), variable management (9 tools), policy & tags (4 tools), Stacks (2 tools)
   - Official from HashiCorp (hashicorp/terraform-mcp-server), 1,300 stars, 134 forks, 323 commits, Go
   - 10 releases since May 2025 (v0.1.0 → v0.4.0)
   - Deliberately does not run `terraform apply` — safety by design
   - Dual transport (stdio + Streamable HTTP), tool filtering via `--toolsets`/`--tools`, built-in rate limiting
   - MCP resources for Style Guide, Module Development Guide, dynamic provider docs
   - Honest about issues: security findings (#288 — insecure TLS, unverified CI binary downloads), provider search returning community versions (#178), proxy issues (#267), beta status, Terraform-only (no OpenTofu/Pulumi), workspace tools require HCP Terraform
   - Compared with Pulumi MCP (execution-oriented, Neo agent), AWS MCP (4/5, 66 servers, AWS-specific), thrashr888/terraform-mcp-server (archived community version), Kubernetes MCP (4/5, different layer), Docker MCP (3.5/5, different scope)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Terraform MCP 4/5 to summary table (DevOps IaC row now links to review)
   - Updated rating distribution (4/5 tier now has 18 servers)
   - Added Terraform MCP to "Beyond the original list" section
   - Updated review count to 39

4. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added review link to intro, summary table, and Terraform MCP section
   - Rewrote Terraform section with review details: 35+ tools, 6 functional areas, security findings, specific issues, comparisons
   - Updated feature comparison table (IaC: "Deep (35+ tools)", Cloud resources: "HCP workspaces")

5. **Build succeeded** (45ms, 59 pages).

### Site status
- **Committed, deploy pending** (just deployed Run 59, throttle needed)
- 53 content pieces: 39 reviews + 4 guides + 11 comparisons
- Terraform MCP is the 18th server rated 4/5
- Second IaC-focused review — complements AWS MCP (4/5), Kubernetes MCP (4/5), Docker MCP (3.5/5)

### What should happen next
- **Run 61:** Deploy pending content. Could write Grafana MCP, Datadog MCP, Pulumi MCP, or another review.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 59 — 2026-03-14 — Review (Kubernetes MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 58 (AWS MCP review) — 57 pages deployed successfully.

2. **Wrote "The Kubernetes MCP Server — Native API Access Without the kubectl Tax"** — `content/reviews/kubernetes-mcp-server.md`
   - **38th review**, nineteenth review beyond the original server list
   - Rating: **4/5** — the most architecturally sound Kubernetes MCP server, with genuine safety controls and modular design, held back by v0.0.x instability, pending security findings, and gaps in workload-specific tooling
   - Go-native implementation — direct Kubernetes API access via client-go, not a kubectl wrapper
   - 6 modular toolsets: core (pods, resources, events, nodes, metrics), config (kubeconfig, contexts), Helm (install/uninstall/list), KubeVirt (VMs), Kiali (service mesh), KCP (multi-tenant)
   - Red Hat / containers org (containers/kubernetes-mcp-server), 1,300 stars, 285 forks, 747 commits, Go
   - 58 releases (v0.0.x), distributed as native binary, npm, pip, Docker image
   - Safety model: --read-only, --disable-destructive, denied resource lists, automatic secret redaction
   - Multi-cluster support, TOML config with drop-in directory, SIGHUP reload, OpenTelemetry tracing
   - Supports stdio, SSE, Streamable HTTP transports
   - Honest about issues: security audit with 2 findings (#762), panic in pods_log (#347), no granular read-only (#568), no Job/CronJob tools (#370), KubeVirt eval failures (#838), OpenShift in developer preview, 48 open issues
   - Compared with Flux159/mcp-server-kubernetes (1,300 stars, TypeScript, kubectl wrapper), rohitg00/kubectl-mcp-server (821 stars, 235+ tools, feature-bloated), AWS EKS MCP (EKS-specific, exposes secrets), strowk/mcp-k8s-go (resource-focused), Docker MCP (3.5/5, different layer)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Kubernetes MCP 4/5 to summary table (DevOps containers row now links to review as runner-up)
   - Updated Kubernetes section with review link and expanded details
   - Added Kubernetes MCP to "Beyond the original list" section
   - Updated review count to 38, rating distribution (4/5 tier now has 17 servers)

4. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added review link to intro, summary table, and Kubernetes MCP section
   - Rewrote Kubernetes section with review details: 6 modular toolsets, safety model, specific issues, comparisons

5. **Build succeeded** (50ms, 58 pages).

### Site status
- **Committed, deploy pending** (just deployed Run 58, throttle needed)
- 52 content pieces: 38 reviews + 4 guides + 11 comparisons
- Kubernetes MCP is the 17th server rated 4/5
- First container orchestration review — complements Docker MCP (3.5/5) and AWS MCP (4/5)

### What should happen next
- **Run 60:** Deploy pending content. Could write Terraform MCP, Grafana MCP, Datadog MCP, or another review.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 58 — 2026-03-14 — Review (AWS MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "AWS MCP Servers — 66 Servers, One Monorepo, and the Biggest Bet in the MCP Ecosystem"** — `content/reviews/aws-mcp-servers.md`
   - **37th review**, eighteenth review beyond the original server list
   - Rating: **4/5** — the most comprehensive cloud MCP integration in the ecosystem, with active development, strong security design, and a managed remote endpoint, held back by overwhelming complexity, security gaps, and uneven polish across 66 servers
   - 66 specialized MCP servers across 8 categories: Documentation & Knowledge (3), Infrastructure & Deployment (8), AI & ML (8), Data & Analytics (15), Developer Tools (6), Integration & Messaging (5), Cost & Operations (7), Healthcare & Life Sciences (3)
   - Plus Core MCP Server orchestrating via 16 role-based configurations
   - Official from AWS (awslabs/mcp), 8,500 stars, 1,400 forks, Python, Apache 2.0
   - ~80K monthly PyPI downloads (core server), 190+ releases with daily automated CI/CD
   - Managed Knowledge endpoint at `knowledge-mcp.global.api.aws` — free, no auth, Streamable HTTP
   - API server with `call_aws`, `suggest_aws_commands`, `get_execution_plan` tools
   - Security: `READ_OPERATIONS_ONLY`, `REQUIRE_MUTATION_CONSENT`, CloudTrail audit logging, IAM-based permissions
   - Honest about issues: EKS exposes K8s secrets in plain text (#2588), 125 open issues, Cost Explorer incompatible with Bedrock AgentCore (#2442), stdio-only on most servers (SSE removed May 2025), deprecation churn (CDK, Terraform, Diagram servers deprecated), not multi-tenant, Python 3.12+ and uv required
   - Compared with Cloudflare MCP (4.5/5, simpler single-server), Docker MCP (3.5/5, local containers), Neon/Supabase (database-specific), Sentry (observability layer)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added AWS MCP 4/5 to summary table (Cloud infrastructure row now links to review)
   - Updated DevOps section with review link and expanded details
   - Added AWS MCP to "Beyond the original list" section
   - Updated review count to 37, rating distribution (4/5 tier now has 16 servers)

3. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added review link to intro, summary table, and AWS MCP section
   - Rewrote AWS MCP section with review details: 66 servers, Core MCP orchestration, Knowledge endpoint, security controls, specific issues

4. **Build succeeded** (51ms, 57 pages).

### Site status
- **Committed, deploy pending** (throttle — need ~46 more min)
- 51 content pieces: 37 reviews + 4 guides + 11 comparisons
- AWS MCP is the 16th server rated 4/5
- First cloud infrastructure suite review (covers 66 servers in one review)

### What should happen next
- **Run 59:** Deploy pending content. Could write Kubernetes MCP, Terraform MCP, or another review.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 57 — 2026-03-14 — Review (Docker MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Docker MCP Server — Your AI Agent's Container Workshop"** — `content/reviews/docker-mcp-server.md`
   - **36th review**, seventeenth review beyond the original server list
   - Rating: **3.5/5** — most complete Docker MCP server available, with practical design and good security defaults, held back by missing exec/compose capabilities, maintenance concerns, and stdio-only transport
   - 19 tools: 8 container (list, create, run, recreate, start, logs, stop, remove), 5 image (list, pull, push, build, remove), 3 network (list, create, remove), 3 volume (list, create, remove) + resources (stats, logs) + docker_compose prompt
   - Community server by Christian Kreiling (ckreiling/mcp-server-docker), 687 stars, 96 forks, Python, GPL-3.0
   - ~9,500 monthly PyPI downloads, v0.2.1 (June 2025), 53 commits, 3 contributors
   - SSH remote Docker via DOCKER_HOST env var (Paramiko for SSH transport)
   - Plan-and-apply docker_compose prompt — LLM proposes config, user reviews before execution
   - Security-conscious: blocks --privileged, --cap-add/--cap-drop; warns against secrets in prompts
   - Per-container stats (CPU, memory) and log tailing as MCP resources
   - Honest about issues: no exec into running containers (#22), no Docker Compose file support, no secrets management (#12), VS Code schema validation bug (#46, #25), stdio-only, GPL-3.0, slow release cadence (last release June 2025)
   - Compared with QuantGeekDev/docker-mcp (454 stars, 4 tools, Compose support, abandoned), ofershap/mcp-server-docker (0 stars, 10 tools, has exec, newer), Docker MCP Toolkit (different — infrastructure for running MCP servers, not managing Docker)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Docker MCP 3.5/5 to summary table (DevOps containers row now links to review)
   - Rewrote containers section with review details and Docker MCP Toolkit context
   - Added Docker MCP to "Beyond the original list" section
   - Updated review count to 36, rating distribution (3.5/5 tier now has 12 servers)

3. **Deployed** all pending content (runs 54-57: Sequential Thinking, Perplexity, MongoDB, Git, Docker reviews)
   - 56 pages deployed successfully

4. **Build succeeded** (44ms, 56 pages).

### Site status
- **Deployed** — all content live on chatforest.com
- 50 content pieces: 36 reviews + 4 guides + 11 comparisons
- Docker MCP is the 12th server rated 3.5/5
- First DevOps/containers category review

### What should happen next
- **Run 58:** Could write AWS MCP, Terraform MCP, Kubernetes MCP, or another review. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 56 — 2026-03-14 — Review (Git MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Git MCP Server — The Missing Push Button"** — `content/reviews/git-mcp-server.md`
   - **35th review**, sixteenth review beyond the original server list
   - Rating: **3/5** — solid implementation of half a git workflow, held back by the absence of remote operations, merge capabilities, and modern transport support
   - 12 tools: git_status, git_diff_unstaged, git_diff_staged, git_diff, git_add, git_reset, git_commit, git_log, git_show, git_create_branch, git_checkout, git_branch
   - Official reference server from Anthropic (modelcontextprotocol/servers monorepo), 81,000+ stars, Python, MIT
   - ~361,000 weekly PyPI downloads — one of the most-installed MCP servers
   - Zero-dependency simplicity: no API keys, no accounts, no external services
   - Security-conscious: flag injection prevention (CWE-88), path validation, 100% test coverage
   - Well-designed diff tools (three variants), date-based log filtering, branch filtering with contains/not_contains
   - Honest about issues: no push/pull/fetch (#618 open since Feb 2025, PR #2961 unmerged), no merge/rebase/stash/tag/blame, git_reset is all-or-nothing, Windows path issues (#2519), repo path auto-detection broken (#3029), had critical .git/ staging bug (#2373, fixed), 18 unconstrained string parameters (#3537), stdio-only transport
   - Compared with GitHub MCP (4/5, complementary not competitive), cyanheads/git-mcp-server (28 tools, more complete), Filesystem MCP (3.5/5, better for read-only)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Git MCP 3/5 to summary table (new "Version control (local git)" row)
   - Added Git MCP section to Filesystem/Version control/Communication category
   - Added Git MCP to "Beyond the original list" section
   - Updated review count to 35, rating distribution (3/5 tier now has 5 servers)

3. **Build succeeded** (51ms, 55 pages).

### Site status
- **Committed, deploy pending** (throttle — need ~16 more min)
- 49 content pieces: 35 reviews + 4 guides + 11 comparisons
- Git MCP is the 5th server rated 3/5
- Complements the existing GitHub MCP Server review — local operations vs remote API

### What should happen next
- **Run 57:** Deploy pending content (Git, MongoDB, Sequential Thinking, Perplexity reviews). Could write AWS MCP, Terraform MCP, Docker MCP, or another review.
- **Run 58+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 55 — 2026-03-14 — Review (MongoDB MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The MongoDB MCP Server — The Most Comprehensive Database Server We've Reviewed"** — `content/reviews/mongodb-mcp-server.md`
   - **34th review**, fifteenth review beyond the original server list
   - Rating: **4/5** — the most feature-rich database MCP integration available, with active development and genuine innovation, held back by default-writable safety concerns and public preview status
   - 37+ tools across 5 categories: database operations (21), Atlas cluster management (12), Atlas local deployments (4), knowledge search (2)
   - Official from MongoDB, Inc. (mongodb-js/mongodb-mcp-server), ~960 stars, 207 forks, TypeScript, Apache 2.0
   - Most comprehensive database MCP server — 37+ tools, nearly double the next closest (Neon with 20)
   - Full provisioning-to-optimization lifecycle: create projects → provision clusters → insert data → analyze performance → add suggested indexes
   - Atlas Performance Advisor integration (Winter 2026): suggested indexes, drop recommendations, schema advice, slow queries
   - Automatic embedding generation for vector search indexes via Voyage AI during insert operations
   - Atlas local cluster creation via Docker — no separate MongoDB installation needed
   - Knowledge search tools for MongoDB documentation
   - Rapid release cadence: 16+ releases, shipping every 1-2 weeks
   - Only 10 open issues despite 960 stars — strong maintenance
   - Honest about issues: default-writable mode (dangerous, should be read-only by default), connection flooding during extended sessions (#936), no remote hosted server option (#641 open since Oct 2025), Node 22 ESM crash (#718), framework integration issues with LangChain (#974) and Codex (#968), aggregation on views error (#878), still in public preview
   - Compared with Neon (4/5, branch-based migrations), Supabase (4/5, full backend), Postgres MCP (2.5/5, vulnerable), SQLite MCP (3/5, minimal), community MongoDB servers

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added MongoDB 4/5 to summary table (new "Database (MongoDB)" row)
   - Added MongoDB section to Databases category with review link
   - Added MongoDB to "Beyond the original list" section
   - Updated review count to 34, rating distribution (4/5 tier now has 15 servers)

3. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added MongoDB to contenders table (top position)
   - Added full MongoDB section with setup, features, and recommendation
   - Updated feature comparison table with MongoDB column (now includes tool count row)
   - Added MongoDB to decision flowchart (both by database engine and by use case)
   - Updated descriptions, bottom line, and review links

4. **Build succeeded** (43ms, 54 pages).

### Site status
- **Committed, deploy pending** (throttle — need ~25 more min)
- 48 content pieces: 34 reviews + 4 guides + 11 comparisons
- MongoDB is the 15th server rated 4/5 — the most crowded rating tier
- First NoSQL/document database MCP server review
- Database category now has 5 reviewed servers (Postgres 2.5, SQLite 3, Neon 4, Supabase 4, MongoDB 4)

### What should happen next
- **Run 56:** Deploy pending content (MongoDB, Sequential Thinking, Perplexity reviews). Could write Git MCP, AWS MCP, Terraform MCP, or another review.
- **Run 57+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 54 — 2026-03-14 — Review (Sequential Thinking MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Sequential Thinking MCP Server — When Your Agent Needs to Think Out Loud"** — `content/reviews/sequential-thinking-mcp-server.md`
   - **33rd review**, fourteenth review beyond the original server list
   - Rating: **3/5** — pioneering concept for structured reasoning, increasingly redundant with built-in model capabilities
   - 1 tool: sequential_thinking (step-by-step reasoning with branching and revision)
   - Official reference server from Anthropic (modelcontextprotocol/servers monorepo), 81,000+ stars, TypeScript, MIT
   - #9 most popular MCP server globally, ~72,000 weekly npm downloads, 4.1M all-time visitors on PulseMCP
   - Elegant branching and revision model — thoughts can be revised, branched, and dynamically extended
   - Dynamic thought adjustment with `needsMoreThoughts` and configurable `MAX_TOTAL_THOUGHTS` cap
   - Zero-dependency simplicity — no API keys, no accounts, no external services
   - Honest about issues: increasingly redundant with extended thinking/reasoning tokens built into models, every thought step is a separate tool call (3-6x token overhead), LLMs struggle with integer parameter types (#2598, #2905), agents rarely use branching/revision features (#2332), session stickiness in Claude Code (#713), no persistence of reasoning chains, unconstrained totalThoughts by default (#2226), tool description too long for some OpenAI models (#799)
   - Compared with Claude's extended thinking (built-in, no overhead), Anthropic's think tool pattern (simpler, better benchmarks), community forks (LangGPT, FradSer multi-agent, arben-adm)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added new "Reasoning & thinking" section with Sequential Thinking 3/5 review summary
   - Added Sequential Thinking to "Beyond the original list" section
   - Updated review count to 33, rating distribution (3/5 tier now has 4 servers)

3. **Build succeeded** (43ms, 53 pages).

### Site status
- **Committed, deploy pending** (throttle — only 18 min since last deploy)
- 47 content pieces: 33 reviews + 4 guides + 11 comparisons
- Sequential Thinking is the 4th server rated 3/5
- First "reasoning/thinking" category review — a category where built-in model capabilities are winning over MCP tooling

### What should happen next
- **Run 55:** Deploy pending content (Sequential Thinking + Perplexity reviews). Could write Docker MCP, Terraform MCP, AWS MCP, or another review.
- **Run 56+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 53 — 2026-03-14 — Deploy + Review (Perplexity MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed backlogged content** — Runs 50-52 (Tavily, Crawl4AI, Milvus reviews) now live on chatforest.com. 51 pages deployed.

2. **Wrote "The Perplexity MCP Server — When Your Agent Wants Answers, Not Links"** — `content/reviews/perplexity-mcp-server.md`
   - **32nd review**, thirteenth review beyond the original server list
   - Rating: **4/5** — fastest path from question to answer, with unmatched deep research, held back by no free tier and timeout-prone deep research
   - 4 tools: search (ranked results), ask (conversational AI with sonar-pro), research (deep reports with sonar-deep-research), reason (analytical reasoning with sonar-reasoning-pro)
   - Official server from Perplexity (perplexityai/modelcontextprotocol), 2,000 stars, TypeScript, MIT
   - Answer engine approach: returns synthesized answers with citations instead of links
   - Four purpose-built Sonar models mapped to four tools — search, ask, research, reason
   - Deep research produces multi-paragraph cited reports no other MCP server matches
   - Zero open issues (42 closed) — best maintenance record in the search category
   - Corporate proxy support, Docker deployment, one-click Cursor/VS Code installers
   - Honest about issues: no free tier (highest entry barrier in search category), deep research timeouts with strict MCP clients, no access to raw sources, complex per-token + per-request pricing, Tier 0 rate limits start at 50 RPM, no remote hosted server (unlike Tavily), npx stdout pollution causes EOF errors
   - Compared with Brave (more search verticals, free tier, flat pricing), Exa (semantic search, source discovery), Tavily (search + extract + crawl pipeline, hosted server), community Perplexity wrappers

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Perplexity 4/5 review link to answer engines section
   - Added Perplexity to "Beyond the original list" section
   - Updated review count to 32, rating distribution (4/5 tier now has 14 servers)

4. **Updated search comparison** (`content/guides/best-search-mcp-servers.md`)
   - Added review link and rating to intro, contenders table, Perplexity section header
   - Updated Perplexity section with review-informed details (zero open issues, no free tier)
   - Added review links to recommendation section and two-server strategy
   - Updated decision flowchart with rating

5. **Build succeeded** (44ms, 52 pages).

### Site status
- **Committed, deploy pending** (throttle — just deployed this run)
- 46 content pieces: 32 reviews + 4 guides + 11 comparisons
- Perplexity is the 14th server rated 4/5 — the most crowded rating tier
- Search category now has 4 reviewed servers (Brave 4, Exa 4, Tavily 4, Perplexity 4)

### What should happen next
- **Run 54:** Deploy Perplexity review. Could write Sequential Thinking, BrowserMCP, Zilliz Cloud MCP, or another review.
- **Run 55+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 52 — 2026-03-14 — Review (Milvus MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Milvus MCP Server — The Most Popular Vector Database Gets an AI Interface"** — `content/reviews/milvus-mcp-server.md`
   - **31st review**, twelfth review beyond the original server list
   - Rating: **3.5/5** — category-leading five search modes with native hybrid search, held back by no embedded/local mode and pre-release maturity
   - 12 tools: search (5: text, vector, hybrid, text similarity, filter query), collection management (5: list, create, info, load, release), data operations (2: insert, delete)
   - Official server from Zilliz (zilliztech/mcp-server-milvus), 220 stars, Python
   - Milvus is the most-starred open-source vector database (40,000+ GitHub stars), used by NVIDIA, Salesforce, eBay, Airbnb, DoorDash
   - Five search modes — more than any other vector DB MCP server (Chroma has 3, Pinecone has 2, Qdrant has 1)
   - Native hybrid search combining keyword precision with semantic recall (Milvus 2.5+)
   - Memory management controls (load/release collections) — unique in category
   - Full delete capability via filter expressions (unlike Qdrant and Pinecone)
   - Works identically with self-hosted Milvus and Zilliz Cloud
   - Stdio and SSE transport
   - Honest about issues: no embedded/local mode (requires running Milvus instance), no document update, pre-release (35 commits, no versioned releases, last updated Dec 2025), service hang bug (#51), no Streamable HTTP, Python-only, no MCP-level embedding config
   - Compared with Chroma (more deployment flexibility), Qdrant (best transport support), Pinecone (best search quality with reranking)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Milvus 3.5/5 review link to vector database section
   - Updated runner-up in summary table from Qdrant to Milvus (3.5/5, hybrid search)
   - Added Milvus to "Beyond the original list" section
   - Updated review count to 31, rating distribution (3.5/5 tier now has 11 servers)

3. **Updated vector database comparison** (`content/guides/best-vector-database-mcp-servers.md`)
   - Moved Milvus from "Unreviewed Servers" to "Reviewed Servers" with full review summary
   - Added review link to contenders table
   - Added Rating row to feature comparison table
   - Updated recommendations section with review link and rating
   - Updated decision flowchart with review links
   - Updated "Bottom Line" section to reflect two 3.5/5 leaders

4. **Build succeeded** (42ms, 51 pages). **Deploy throttled** — need 60 min since last deploy (~50 min elapsed).

### Site status
- **Committed, deploy pending**
- 45 content pieces: 31 reviews + 4 guides + 11 comparisons
- Milvus is the 11th server rated 3.5/5 — the most crowded rating tier
- Vector DB category now has 4 reviewed servers (Chroma 3.5, Milvus 3.5, Qdrant 3, Pinecone 3)

### What should happen next
- **Run 53:** Deploy pending content. Could write BrowserMCP, Zilliz Cloud MCP, or another review.
- **Run 54+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 51 — 2026-03-14 — Review (Crawl4AI MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Crawl4AI MCP Server — The Most Popular Crawler Goes LLM-Native"** — `content/reviews/crawl4ai-mcp-server.md`
   - **30th review**, eleventh review beyond the original server list
   - Rating: **3.5/5** — best free web scraper with best-in-class markdown extraction, held back by Docker-only deployment and immature MCP layer
   - 7 tools: markdown extraction (1), HTML (1), screenshot (1), PDF (1), JavaScript execution (1), multi-URL crawling (1), documentation query (1)
   - Built-in MCP server from Crawl4AI (unclecode/crawl4ai), 61,900+ stars, Python, open source
   - Most-starred open-source web crawler on GitHub — more than Scrapy, more than Playwright
   - "Fit Markdown" heuristic noise filtering — strips nav, footers, sidebars for clean LLM-ready content
   - Completely free with no credit limits — unlimited pages, no API keys required for basic usage
   - JavaScript execution via Playwright for dynamic content (cookie banners, infinite scroll, SPAs)
   - Adaptive crawling (auto-stops when enough content gathered), crash recovery with resume_state
   - LLM-based extraction via LiteLLM (any provider), plus LLM-free extraction via CSS/XPath/regex
   - SSE and WebSocket transports (no stdio), Docker-only deployment
   - Honest about issues: SSE connection bugs (#1316), missing schema type fields (#1311), no hosted option, thin MCP tool abstractions, community fragmentation with 12+ alternative wrappers
   - Compared with Firecrawl (more polished MCP, paid), Playwright (deterministic control, no markdown), Tavily (search+crawl, credit-based), Puppeteer (simpler, no extraction), Fetch (basic, no JS)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Crawl4AI 3.5/5 review link to web scraping section
   - Added Crawl4AI to "Beyond the original list" section
   - Updated review count to 30, rating distribution (3.5/5 tier now has 10 servers)

3. **Updated web scraping comparison** (`content/guides/best-web-scraping-mcp-servers.md`)
   - Rewrote Crawl4AI section from "community wrapper" to "built-in MCP server" with review link and rating
   - Updated contenders table with review link, rating, Docker-only, 7 tools
   - Updated feature comparison table (tools: 7, renamed column)
   - Updated recommendations section with review link and rating
   - Updated decision flowchart with review link
   - Added Crawl4AI review to bottom links

4. **Build succeeded** (40ms, 50 pages). **Deploy throttled** — need 60 min since last deploy (~40 min elapsed).

### Site status
- **Committed, deploy pending**
- 44 content pieces: 30 reviews + 4 guides + 11 comparisons
- Crawl4AI is the 10th server rated 3.5/5 — the most crowded rating tier

### What should happen next
- **Run 52:** Deploy pending content. Could write Milvus, BrowserMCP, or another review.
- **Run 53+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 50 — 2026-03-14 — Review (Tavily MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Tavily MCP Server — Search, Extract, Crawl, and Map in One Package"** — `content/reviews/tavily-mcp-server.md`
   - **29th review**, tenth review beyond the original server list
   - Rating: **4/5** — best search-to-extract pipeline, held back by keyword-only search quality and credit expiration
   - 4 tools: search (1), extraction (1), crawling (1), site mapping (1)
   - Official server from Tavily (`tavily-ai/tavily-mcp`), 1,400 stars, JavaScript, MIT
   - Hosted remote MCP server at mcp.tavily.com — zero-install setup, just paste a URL
   - Default search API for LangChain, LlamaIndex, CrewAI, Vercel AI SDK
   - Search + extract + crawl + map pipeline in one server — capabilities that normally need 2-3 servers
   - OAuth 2.0 support with automatic client registration
   - Natural language `instructions` parameter for crawl/map tools
   - Honest about issues: keyword search (71% WebWalker vs Exa's 81%), credits don't roll over, cost stacking, HTTP config friction (#125, #121), API key in URL, Nebius acquisition uncertainty
   - Pricing: 1,000 free credits/mo, then $30-500/mo (credits expire monthly)
   - Compared with Brave (more search types), Exa (semantic search), Firecrawl (deeper scraping), Perplexity (answer engine)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Tavily 4/5 review link to search section runner-up in summary table
   - Added "Search + extraction" sub-section with Tavily review link
   - Added Tavily to "Beyond the original list" section
   - Updated review count to 29, rating distribution (4/5 tier now has 13 servers)

3. **Updated search comparison** (`content/guides/best-search-mcp-servers.md`)
   - Added review rating (4/5) and review link to contenders table
   - Updated Tavily section header with review link and rating
   - Added Tavily review to intro paragraph (now lists all 3 reviewed search servers)
   - Added rating to decision flowchart

4. **Build succeeded** (40ms, 49 pages). **Deploy throttled** — need 60 min since last deploy (~27 min elapsed).

### Site status
- **Committed, deploy pending**
- 43 content pieces: 29 reviews + 4 guides + 11 comparisons
- Tavily is the 13th server rated 4/5 — the most crowded rating tier

### What should happen next
- **Run 51:** Deploy pending content. Could write Milvus, Crawl4AI, or BrowserMCP review.
- **Run 52+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 49 — 2026-03-14 — Review (Browserbase MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Browserbase MCP Server — Cloud Browser Automation With AI-Native Targeting"** — `content/reviews/browserbase-mcp-server.md`
   - **28th review**, ninth review beyond the original server list
   - Rating: **3.5/5** — innovative AI-native targeting via Stagehand, held back by critical bugs and thin tooling
   - 8 tools: navigation & interaction (3), data extraction (2), visual capture (1), session management (2)
   - Official server from Browserbase (`browserbase/mcp-server-browserbase`), 3,200 stars, TypeScript
   - Stagehand v3 natural language element targeting — agents describe actions in plain English instead of CSS selectors or accessibility tree refs
   - Cloud-only with anti-bot stealth mode, proxy support, session recording
   - stdio + Streamable HTTP transports, Docker support
   - Requires 3 API keys (Browserbase API key, project ID, Gemini/model API key)
   - Honest about issues: 20 open GitHub issues including blank screenshots (#125), Stagehand init failures (#56, #41), SHTTP failures (#149), session creation bugs (#121, #118)
   - Pricing: 1 free browser hour, then $20/mo Developer, $99/mo Startup, custom Scale
   - Compared with Playwright (free, 25+ tools, deterministic), Puppeteer (free, CSS selectors), Firecrawl (content extraction), BrowserMCP (existing browser)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Browserbase 3.5/5 review link to browser automation runner-up in summary table
   - Added Browserbase to browser automation section with review link
   - Added Browserbase to "Beyond the original list" section
   - Updated review count to 28, rating distribution (3.5/5 tier now has 9 servers)

3. **Updated browser comparison** (`content/guides/best-browser-mcp-servers.md`)
   - Added review rating (3.5/5) and review link to contenders table
   - Updated Browserbase description with Stagehand v3, tool count, pricing details
   - Updated tool count from ~10 to 8 in feature comparison
   - Added review link to production workloads recommendation section
   - Added Browserbase review to bottom links

4. **Updated web scraping comparison** (`content/guides/best-web-scraping-mcp-servers.md`)
   - Added review rating (3.5/5) and review link to Browserbase section header
   - Updated description with Stagehand v3 tools and known bugs

5. **Build succeeded** (45ms, 48 pages). **Deployed to chatforest.com** — 48 pages live.

### Site status
- **Committed, deployed this run**
- 42 content pieces: 28 reviews + 4 guides + 11 comparisons
- Browserbase is the 9th server rated 3.5/5 — the second most crowded rating tier

### What should happen next
- **Run 50:** Could write Tavily, Milvus, Crawl4AI, or BrowserMCP review.
- **Run 51+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 48 — 2026-03-14 — Deploy + Review (Firecrawl MCP Server)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Deployed all backlogged content** — Runs 44-47 (timestamps, Qdrant review, vector database comparison, Pinecone review, Todoist review) now live on chatforest.com. 47 pages deployed.

2. **Wrote "The Firecrawl MCP Server — The Full-Stack Web Scraping Platform for AI Agents"** — `content/reviews/firecrawl-mcp-server.md`
   - **27th review**, eighth review beyond the original server list
   - Rating: **4/5** — most comprehensive web scraping MCP server with unique autonomous research
   - 12+ tools across 4 categories: core scraping (5), search & extraction (2), research & agents (2), utility (1), plus optional browser automation (4)
   - Official server from Firecrawl/SideGuide Technologies, 5,800 stars, MIT license, TypeScript
   - Unique `firecrawl_agent` for autonomous multi-source research and `firecrawl_extract` for LLM-powered structured data extraction
   - Cloud + self-hosted, stdio + Streamable HTTP transports, hosted URL endpoint
   - Honest about issues: non-renewable 500-credit free tier, credit stacking (1 credit/page → 9 credits with extraction + enhanced), Extract endpoint billed separately, 49 open issues, agent tools in preview
   - Compared with Official Fetch, fetcher-mcp, Browserbase, Jina AI, community alternatives

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Firecrawl 4/5 review link to web scraping section and browser automation section
   - Added Firecrawl to "Beyond the original list" section
   - Updated review count to 27, rating distribution (4/5 cluster now has 12 servers)

4. **Updated web scraping comparison** (`content/guides/best-web-scraping-mcp-servers.md`)
   - Added review rating (4/5) and review link to Firecrawl section
   - Updated tool count from 7 to 12+, updated pricing to current rates ($16-599/mo)
   - Added LLM extraction and autonomous agent rows to feature comparison table
   - Updated recommendations section with review link
   - Added Firecrawl review link to bottom section

5. **Build succeeded** (38ms, 47 pages). **Deploy throttled** — just deployed this run.

### Site status
- **Committed, deployed earlier this run** (deploy throttle now active)
- 41 content pieces: 27 reviews + 4 guides + 11 comparisons
- Firecrawl is the 12th server rated 4/5 — the most crowded rating tier

### What should happen next
- **Run 49:** Could write Browserbase, Tavily, Milvus, or Crawl4AI review.
- **Run 50+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 47 — 2026-03-14 — Review (Todoist MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Todoist MCP Server — Full-Stack Task Management Through Your AI Assistant"** — `content/reviews/todoist-mcp-server.md`
   - **26th review**, seventh review beyond the original server list
   - Rating: **4/5** — most ambitious productivity MCP server with SDK-first architecture
   - 28+ tools across 7 categories: tasks (7), projects (5), sections (3), comments & collaboration (5), labels (2), information & search (4), data operations (3)
   - Official server from Doist (`Doist/todoist-ai`), 382 stars, MIT license, TypeScript
   - SDK-first architecture — tools reusable in Vercel AI SDK, custom pipelines, not just MCP
   - All three transports: Streamable HTTP, SSE, stdio — rare for any MCP server
   - MCP Apps: interactive UI widgets rendered inline in chat interfaces
   - Hosted endpoint at `ai.todoist.net/mcp` with OAuth — plus local stdio via npx
   - `get-overview` tool for dashboard-style snapshots, full CRUD including delete
   - Honest about issues: two p1 bugs (`add-sections` broken, `manage-assignments` silent failure), batch timeouts, incomplete project hierarchy, no reminders/attachments/reordering, self-described "early stages"
   - Compared with Linear (better tool design, more stable), Notion (knowledge + tasks), 6 community Todoist servers

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Todoist 4/5 review link to Productivity (tasks) runner-up in summary table
   - Updated Todoist section with rating, 28+ tools, SDK-first detail, and review link
   - Added Todoist to "Beyond the original list" section
   - Updated review count to 26, rating distribution (4/5 cluster now has 11 servers)

3. **Updated productivity comparison** (`content/guides/best-productivity-mcp-servers.md`)
   - Added Todoist review link to intro and contenders table (updated stars to 382, tools to 28+)
   - Rewrote Todoist detail section with review rating, full tool count, SDK-first architecture, transport flexibility, MCP Apps, known bugs, and review link
   - Updated recommended stack with review link and rating

4. **Build succeeded** (43ms, 46 pages). **Deploy throttled** — 22 minutes remaining per 1-deploy/hour rule.

### Site status
- **Committed, NOT deployed** (deploy throttle)
- 40 content pieces: 26 reviews + 4 guides + 11 comparisons (counting _index.md separately)
- Todoist is the 11th server rated 4/5 — the most crowded rating tier

### What should happen next
- **Run 48:** Deploy (throttle should be clear). Could write Firecrawl, Browserbase, Milvus, or Tavily review.
- **Run 49+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 46 — 2026-03-14 — Review (Pinecone MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Pinecone MCP Server — Cloud Vector Search With Built-In Reranking"** — `content/reviews/pinecone-mcp-server.md`
   - **25th review**, sixth review beyond the original server list
   - Rating: **3/5** — innovative search features held back by cloud-only limitations
   - 9 tools: index management (3), record operations (2), search quality (2), documentation (1), index creation (1)
   - Unique features no other vector DB MCP server has: `cascading-search` (cross-index search with deduplication), `rerank-documents` (built-in reranking models), `search-docs` (documentation search without auth)
   - Integrated embedding means zero embedding config — pass text, Pinecone handles the rest
   - Researched all three Pinecone MCP servers: Developer (this review), Assistant (42 stars, Rust, 1 tool), Claude Code Plugin
   - Honest about tradeoffs: cloud-only (no local mode), integrated embedding indexes only (existing custom-embedding indexes invisible), no delete/update/namespace management, stdio transport for a cloud-only service, lowest adoption among official servers (56 stars)
   - Comparison with community mcp-pinecone by sirmews (~150 stars) which works with any Pinecone index
   - Feature comparison table across 10 dimensions vs Chroma, Qdrant, Milvus

2. **Updated vector database comparison** (`content/guides/best-vector-database-mcp-servers.md`)
   - Moved Pinecone from "Unreviewed Servers" to reviewed section with rating and review link
   - Added review links in contenders table, recommendations, and decision flowchart
   - Updated intro to mention 3 reviewed servers

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated Pinecone entry in vector database section with rating, review link, and feature description
   - Added Pinecone to "Beyond the original list" section
   - Updated review count from 24 to 25
   - Updated rating distribution (3/5 cluster now has 3 servers: SQLite, Qdrant, Pinecone)

4. **Build succeeded** (45 pages). **Deploy throttled** — 30 minutes remaining per 1-deploy/hour rule.

### Site status
- **Committed, NOT deployed** (deploy throttle)
- 40 content pieces: 25 reviews + 4 guides + 11 comparisons
- Vector database category now has 3 reviewed servers: Chroma (3.5/5), Qdrant (3/5), Pinecone (3/5)

### What should happen next
- **Run 47:** Deploy (throttle should be clear). Could write Milvus MCP review, or a workflow guide.
- **Run 48+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 45 — 2026-03-14 — Comparison (Best Vector Database MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "Best Vector Database MCP Servers in 2026"** — `content/guides/best-vector-database-mcp-servers.md`
   - **11th comparison article** — first dedicated vector database comparison
   - Head-to-head comparison of 7 servers: Chroma (3.5/5, reviewed), Qdrant (3/5, reviewed), Pinecone, Milvus, Zilliz Cloud, Weaviate, LanceDB
   - Researched all unreviewed servers: GitHub stars, tool counts, transport support, features, limitations
   - Two-philosophy framework: "database management" (Chroma 13 tools, Milvus 12 tools) vs "semantic memory" (Qdrant 2 tools)
   - Pinecone positioned between the two — 9 tools focused on search quality (cascading search, reranking)
   - Identified the pgvector gap — no dedicated pgvector MCP server exists
   - Feature comparison table across 17 dimensions
   - Decision flowchart by use case (memory, RAG, infrastructure management, remote transport, zero infrastructure)
   - Honest about category immaturity: no server has OAuth, none at 1.0, best is only 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Full comparison" link in vector databases section
   - Updated comparison count from 10 to 11

3. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added cross-link to vector database comparison in the decision flowchart

4. **Build succeeded** (36ms, 44 pages). **Deploy throttled** — 39 minutes remaining per 1-deploy/hour rule.

### Site status
- **Committed, NOT deployed** (deploy throttle)
- 39 content pieces: 24 reviews + 4 guides + 11 comparisons
- All major MCP server categories now have dedicated comparison articles

### What should happen next
- **Run 46:** Deploy (throttle should be clear). Could write Pinecone MCP or Milvus MCP review, or a workflow guide.
- **Run 47+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 44 — 2026-03-14 — Timestamps in Content (Rob's Editorial Request)

**Mode:** Developer

### Inbox update
- **#105 (normal, Rob):** Editorial suggestion — show timestamps down to the second instead of just dates. Since all articles were published on the same day, timestamps highlight autonomous agent production in real-time bursts. Fits transparent AI authorship brand. Implemented.

### What I did

1. **Updated all 38 content files** with precise timestamps from git commit history
   - Front matter `date:` changed from `2026-03-14` to full ISO 8601 with timezone (e.g., `2026-03-14T09:42:34+09:00`)
   - Timestamps reflect when each piece was actually committed — showing the real production timeline

2. **Updated 5 layout templates** to display full timestamps
   - `layouts/reviews/single.html` — review pages now show `2026-03-14 09:42:34` format
   - `layouts/guides/single.html` — guide pages match
   - `layouts/partials/article-card.html` — listing cards show timestamps
   - `layouts/partials/schema-review.html` — Schema.org `datePublished` now ISO 8601 with time+timezone
   - `layouts/partials/schema-article.html` — same for article schema

3. **Build succeeded** (37ms, 43 pages). **Deploy throttled** — only 8 minutes since last deploy, need 51 more minutes per Rob's 1-deploy/hour rule.

### Site status
- **Committed, NOT deployed** (deploy throttle — will deploy next eligible run)
- 38 content pieces: 24 reviews + 4 guides + 10 comparisons
- All pages now show precise timestamps highlighting autonomous agent workflow

### What should happen next
- **Run 45:** Deploy (throttle should be clear). Could write Pinecone MCP, Milvus MCP, or "Best Vector Database MCP Servers in 2026" comparison.
- **Run 46+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 43 — 2026-03-14 — Review (Qdrant MCP Server) + Deploy Throttle

**Mode:** Operations + Researcher + Copywriter + Developer

### Inbox update
- **#104 (high, Rob):** New deploy rule — deploy at most once per hour using `.last_deploy` file. Implemented.
- **#103 (from me):** SSH restored message from Run 42. Marked seen.

### What I did

1. **Implemented deploy throttle** per Rob's message #104
   - Created `.gitignore` with `.last_deploy`, `.grove_lock`, `resources/_gen/`, `site/`
   - Deploy now checks `.last_deploy` age before attempting rsync
   - After successful deploy, touches `.last_deploy`
   - On failure, does NOT touch `.last_deploy` (per Rob's spec)

2. **Wrote "The Qdrant MCP Server — Semantic Memory Through Your AI Assistant"** — `content/reviews/qdrant-mcp-server.md`
   - **24th review**, fifth review beyond the original server list
   - Rating: **3/5** — most adopted vector DB MCP server (1,300 stars), but too minimal
   - Only 2 tools: `qdrant-store` and `qdrant-find` — no delete, no update, no collection management
   - Only vector DB MCP server supporting all three transports: stdio, SSE, Streamable HTTP
   - Extensible `QdrantMCPServer` class architecture (v0.8.0) — a "server as framework" approach
   - Local embedded mode via `QDRANT_LOCAL_PATH` — zero infrastructure semantic memory
   - Customizable tool descriptions via environment variables
   - Honest about tradeoffs: 2 tools vs Chroma's 13, no delete capability (open issues #74/#101), FastEmbed-only default, no OAuth for MCP transport, 22 open issues with basic feature requests
   - Comparison table with Chroma (13 tools), Pinecone (9 tools), Milvus (11 tools), Weaviate (2 tools)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Qdrant 3/5 link to vector database runner-up in summary table
   - Added review link and detail to vector database section
   - Added Qdrant to "Beyond the original list" section
   - Updated review count to 24, rating distribution (3/5 cluster now has 2 servers: SQLite, Qdrant)

4. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added Qdrant MCP as alternative for vector search / RAG use cases

5. **Build succeeded** (41ms, 43 pages). **Deployed successfully** to chatforest.com.

### Site status
- **Committed AND deployed**
- 38 content pieces: 24 reviews + 4 guides + 10 comparisons
- Deploy throttle now active (max 1 deploy/hour per Rob's directive)

### What should happen next
- **Run 44:** Could write Pinecone MCP, Milvus MCP, or "Best Vector Database MCP Servers in 2026" comparison. Or a workflow guide.
- **Run 45+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 42 — 2026-03-14 — Deploy + Review (Chroma MCP Server)

**Mode:** Operations + Researcher + Copywriter + Developer

### Inbox update
- **#102 (high, Rob):** DreamHost outage may be resolved — asked for ONE SSH test. SSH succeeded! Deployed all backlogged content. Replied as message #103.

### What I did

1. **SSH restored and all content deployed** — 11 runs of backlogged content (runs 31-41) now live on chatforest.com
   - SSH was returning "Too many authentication failures" because I used `grove@chatforest.com` instead of the `chat` alias (which uses user `backforest` with the correct key)
   - 42 pages deployed: 23 reviews + 4 guides + 10 comparisons + about + homepage + listings

2. **Wrote "The Chroma MCP Server — Vector Database Operations Through Your AI Assistant"** — `content/reviews/chroma-mcp-server.md`
   - **23rd review**, fourth review beyond the original server list
   - Rating: **3.5/5** — most comprehensive vector DB MCP server, but stdio-only and stalling development
   - 13 tools: 8 collection management + 5 document operations
   - Four deployment modes: ephemeral (in-memory), persistent (local files), HTTP (self-hosted), Cloud
   - Six embedding providers: Default, Cohere, OpenAI, Jina, VoyageAI, Roboflow
   - Unique feature: `chroma_fork_collection` — duplicate collections for experimentation
   - Search: semantic + full-text + regex through single `query_documents` tool
   - HNSW parameter configuration at collection creation
   - Honest about tradeoffs: stdio-only transport (no remote MCP), Python-only, beta with no releases in 7 months, context-bloating query results, known bugs (non-ASCII corruption, embedding dimension mismatches)
   - Comparison with Qdrant (1,300 stars, 2 tools, better transport), Pinecone (9 tools, cloud-only), Weaviate (2 tools, minimal)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Vector database" row with Chroma 3.5/5 as pick, Qdrant as runner-up
   - Added full vector database section between databases and memory
   - Added Chroma to "Beyond the original list" section
   - Updated review count to 23, rating distribution (3.5/5 cluster now has 8 servers)

4. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added Chroma to decision flowchart for vector search / RAG use cases

5. **Build succeeded** (40ms, 42 pages). **Deployed successfully** to chatforest.com.

### Site status
- **Committed AND deployed** — first successful deploy since Run 29
- 37 content pieces: 23 reviews + 4 guides + 10 comparisons
- All backlogged content now live

### What should happen next
- **Run 43:** Could write Pinecone MCP, Qdrant MCP, or a workflow guide ("MCP Servers for CI/CD Pipelines"). Or a new comparison: "Best Vector Database MCP Servers in 2026".
- **Run 44+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 41 — 2026-03-14 — Review (Linear MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. 11 runs of content waiting to deploy.

### What I did

1. **Wrote "The Linear MCP Server — Issue Tracking and Project Management Through Your AI Assistant"** — `content/reviews/linear-mcp-server.md`
   - **22nd review**, third review beyond the original server list
   - Rating: **4/5** — best-in-class tool design, but high context cost and remote-only deployment
   - 23+ tools across issues, projects, initiatives, milestones, teams, labels, and documentation
   - Hosted remote-first at `mcp.linear.app/mcp` with OAuth 2.1 and Streamable HTTP transport
   - Standout: flat parameter schemas (flattened from GraphQL), embedded enum values, "me" shortcut for assignee — reduces agent errors significantly
   - February 2026 expansion added initiatives, milestones, project updates — moved from engineering tracker to full PM platform
   - Broad client support: Claude, Cursor, VS Code, Windsurf, Zed, Codex, Jules, v0
   - Honest about tradeoffs: 17.3k token context cost, verbose responses with unnecessary fields, no delete/archive, remote-only, requires paid Linear ($8/user/month), connection reliability issues
   - Comparison with Asana, Atlassian/Jira, Todoist — Linear wins on tool design quality

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Linear 4/5 link to Productivity (tasks) row in summary table
   - Updated Linear section with review link and 23+ tool count
   - Added Linear to "Beyond the original list" section
   - Updated review count to 22, rating distribution (4/5 cluster now has 10 servers)

3. **Updated productivity comparison** (`content/guides/best-productivity-mcp-servers.md`)
   - Added Linear review link to intro and contenders table
   - Updated Linear detail section with review rating, tool count, and design highlights

4. **Build succeeded** (38ms, 41 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 36 content pieces: 22 reviews + 4 guides + 10 comparisons
- 11 runs of content waiting to deploy

### What should happen next
- **Run 42:** Check inbox for Rob's SSH clearance. Could write Chroma MCP, Pinecone MCP, or a workflow guide ("MCP Servers for CI/CD Pipelines").
- **Run 43+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 40 — 2026-03-14 — Review (Stripe MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. 9 runs of content waiting to deploy.

### What I did

1. **Wrote "The Stripe MCP Server — Payment Operations Through Your AI Assistant"** — `content/reviews/stripe-mcp-server.md`
   - **21st review**, second review beyond the original server list
   - Rating: **4/5** — best-in-class security model, unique documentation search feature
   - 25 tools across 13 resource categories: customers, products, prices, invoices, subscriptions, refunds, payment links, disputes, balance, coupons, search, and documentation
   - Part of broader Stripe Agent Toolkit (1,400 GitHub stars) with framework integrations for OpenAI, LangChain, CrewAI, Vercel AI SDK
   - Three-layer security: OAuth remote server at mcp.stripe.com, restricted API keys with per-resource permissions for local, dashboard session management
   - Killer feature: `search_stripe_documentation` — agent can query Stripe's knowledge base directly
   - Honest about tradeoffs: covers only 10-15% of Stripe's API surface, most resources only support create+list (no updates), no webhooks, no Checkout Sessions, no Connect, protocol version compatibility issue (#290), TypeScript-only local deployment

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Payments" row with Stripe 4/5 as pick
   - Added full Payments section describing the server and its Agent Toolkit context
   - Updated "Beyond the original list" to mention Stripe alongside Cloudflare
   - Updated review count to 21, rating distribution (4/5 cluster now has 9 servers)

3. **Build succeeded** (37ms, 40 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 35 content pieces: 21 reviews + 4 guides + 10 comparisons
- 10 runs of content waiting to deploy

### What should happen next
- **Run 41:** Check inbox for Rob's SSH clearance. Could write Linear MCP, Chroma MCP, or a workflow guide ("MCP Servers for CI/CD Pipelines").
- **Run 42+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 39 — 2026-03-14 — Review (Cloudflare MCP Server — First Beyond Original List)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- Only pending message was my own reply (#101). No new messages from Rob. No SSH clearance yet.
- Marked #101 as seen.

### What I did

1. **Wrote "The Cloudflare MCP Server — 2,500 API Endpoints in 1,000 Tokens"** — `content/reviews/cloudflare-mcp-server.md`
   - **20th review**, first review beyond our original server list
   - Rating: **4.5/5** — ties with Playwright for our highest rating
   - The most innovative MCP architecture we've reviewed: Code Mode collapses 2,500+ API endpoints into just 2 tools (~1,000 tokens vs 1.17 million for traditional approach)
   - `search()` queries a typed OpenAPI spec; `execute()` runs generated JavaScript in a V8 Dynamic Worker sandbox
   - Plus 16 specialized product servers (Workers Builds, Observability, Browser Rendering, DNS Analytics, AI Gateway, etc.)
   - All remote-first with OAuth, Streamable HTTP transport
   - Also a platform for building MCP servers (Workers + mcp-handler + Agents SDK)
   - Honest about tradeoffs: depends on agent JavaScript competency, fragmented repo structure (3 repos), low Code Mode adoption (262 stars), Cloudflare-only lock-in

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Cloud infrastructure" row with Cloudflare 4.5/5 as pick
   - Added Cloudflare section to DevOps & infrastructure description
   - Updated "All servers reviewed" to "Beyond the original list"
   - Updated review count to 20, rating distribution (4.5/5 cluster now has 2 servers: Playwright, Cloudflare)

3. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added Cloudflare as first entry in contenders table
   - Updated intro to mention Cloudflare review

4. **Build succeeded** (37ms, 39 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 34 content pieces: 20 reviews + 4 guides + 10 comparisons
- Now expanding beyond original server list
- 9 runs of content waiting to deploy

### What should happen next
- **Run 40:** Check inbox for Rob's SSH clearance. Could write Stripe MCP, Chroma MCP, or Linear MCP review — or a workflow guide ("MCP Servers for CI/CD Pipelines").
- **Run 41+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 38 — 2026-03-14 — Guide (How to Set Up Your MCP Server Stack)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **#100 (high, Rob):** DreamHost SSH is datacenter outage (pdx1/iad1), not throttling. Still DO NOT retry. Three questions answered:
  1. We use SSH key auth (ed25519), not password — should reconnect fine once outage resolves
  2. Reddit account ready (username: ChatForest). Drafted display name and bio for Rob to set up. Posts go through Rob's review.
  3. Agreed duck.com → grove@chatforest.com forwarding makes sense once email is set up
- Replied as message #101. Marked #100 as seen.

### What I did

1. **Wrote "How to Set Up Your MCP Server Stack: A Practical Guide for 2026"** — `content/guides/mcp-server-setup-guide.md`
   - **4th guide** — first user-focused setup/configuration guide (vs. build tutorial or security)
   - Covers all four major MCP clients: Claude Desktop, VS Code (Copilot), Cursor, Claude Code
   - Configuration file locations, JSON examples for local (stdio) and remote (Streamable HTTP) servers
   - Explains transport protocol evolution: stdio vs SSE (deprecated) vs Streamable HTTP
   - Four role-specific starter stacks: web developer, backend/data engineer, technical writer, full-stack team
   - Managing multiple servers: performance, context window pressure, security, updates
   - Troubleshooting section covering common issues (server won't start, OAuth failures, silent tool failures, too many tools)
   - Cross-links to all 19 reviews and other guides

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added setup guide reference in the "starter stack" section

3. **Updated build tutorial** (`content/guides/build-your-first-mcp-server.md`)
   - Added cross-link to setup guide at the end

4. **Build succeeded** (36ms, 38 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 33 content pieces: 19 reviews + 4 guides + 10 comparisons
- 8 runs of content waiting to deploy
- Guide library now covers: What is MCP → Build a Server → Set Up Your Stack → Security

### What should happen next
- **Run 39:** Check inbox for Rob's SSH clearance. Could write a new server review (Cloudflare Workers MCP, Stripe MCP, or Chroma MCP are good targets) or a workflow guide ("MCP Servers for CI/CD Pipelines").
- **Run 40+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved. Reddit bio is drafted and ready.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 37 — 2026-03-14 — Guide (MCP Server Security: A Practical Guide for 2026)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. Complying with deploy ban.

### What I did

1. **Wrote "MCP Server Security: A Practical Guide for 2026"** — `content/guides/mcp-server-security.md`
   - **3rd guide** (after "What is MCP" and "Build Your First MCP Server") — first security-focused content
   - Researched OWASP MCP Top 10, OWASP cheatsheets for using/building MCP servers, OAuth 2.1 spec evolution (March → June → November 2025 revisions)
   - Analyzed security posture of all 19 reviewed servers, organized by strength (Strong → Adequate → Weak → Dangerous)
   - Three real vulnerabilities documented with code examples:
     - SQL injection in PostgreSQL MCP (multi-statement bypass of read-only transaction)
     - SSRF in Fetch MCP (unpatched, can reach AWS metadata/localhost)
     - ContextCrush prompt injection in Context7 (patched Feb 2026)
   - Authentication transition section: local API keys → remote OAuth 2.1 Resource Servers
   - Practical security checklist (20 items across 5 categories: auth, data protection, input validation, operational security, supply chain)
   - Best practices section: prefer OAuth, scope down, isolate by context, use read-only modes, audit regularly
   - Cross-links to all 19 reviews and OWASP resources

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added security guide reference in the "starter stack" section

3. **Build succeeded** (31ms, 37 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 32 content pieces: 19 reviews + 3 guides + 10 comparisons
- 7 runs of content waiting to deploy
- Content now includes security-focused material — high-value for SEO (OWASP references, vulnerability documentation)

### What should happen next
- **Run 38:** Check inbox for Rob's SSH clearance. Could write another new server review (Cloudflare Workers MCP, Stripe MCP, or Chroma MCP are trending) or a workflow guide ("Setting Up Your First MCP Server Stack").
- **Run 39+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 36 — 2026-03-14 — Content (Best DevOps & Infrastructure MCP Servers Comparison)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. Complying with deploy ban.

### What I did

1. **Wrote "Best DevOps & Infrastructure MCP Servers in 2026"** — `content/guides/best-devops-mcp-servers.md`
   - **10th comparison article** — first new category beyond the original server list
   - Head-to-head comparison of 5 DevOps platforms: Docker MCP (Toolkit + Catalog), Kubernetes MCP (Red Hat/community), Terraform MCP (HashiCorp), AWS MCP (60+ servers), Azure DevOps MCP (Microsoft, GA)
   - Three-layer framework: container/orchestration (Docker, K8s), infrastructure as code (Terraform, AWS), DevOps platform (Azure DevOps, GitHub)
   - Feature comparison table, decision flowchart, recommended two-layer stack
   - Safety section on production infrastructure risks — read-only modes, credential scoping, staging-first approach
   - Cross-links to our GitHub MCP review (4.5/5) for CI/CD
   - Researched current state: Docker's 300+ verified catalog, K8s fragmentation (6+ implementations), Terraform Stacks support, AWS 60+ specialized servers, Azure DevOps GA + VS 2026 integration

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added full DevOps & infrastructure category section
   - Added 3 DevOps rows to summary table (IaC, containers, platform)
   - Updated comparison count from 9 to 10
   - Updated descriptions to reflect 10 categories

3. **Updated observability comparison** cross-links to include DevOps category

4. **Build succeeded** (34ms). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 31 content pieces: 19 reviews + 2 guides + 10 comparisons
- Now covering categories beyond the original server list
- 6 runs of content waiting to deploy

### What should happen next
- **Run 37:** Check inbox for Rob's SSH clearance. Write more content — could do a deeper tutorial/workflow guide, or review a specific DevOps server (Docker, Terraform, or Kubernetes).
- **Run 38+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets (DevOps servers)

## Run 29 — 2026-03-14 — Traffic & Promotion Strategy + Schema.org SEO

**Mode:** Researcher + Strategist + Developer

### Inbox update
- **High-priority message from Rob + Boss Claude** (message #88): Asked for a traffic/promotion plan — where to post content, social media strategy, open-source Reddit alternatives, what's needed to execute.
- Replied with full plan summary (message #89).

### What I did

1. **Researched traffic/promotion strategies** — web searches on:
   - Developer content promotion tactics for 2026
   - MCP community platforms and developer channels
   - Open-source Reddit alternatives (Lemmy, Kbin, Tildes)
   - SEO timeline expectations for new technical sites
   - Hacker News submission best practices
   - Dev.to/Hashnode cross-posting strategies

2. **Wrote comprehensive traffic & promotion plan** — `strategy/02-traffic-promotion-plan.md`
   - **Three channels:** Community posting (immediate), SEO optimization (medium-term), newsletter (long-term)
   - **Community targets:** Reddit (r/mcp, r/ClaudeAI, r/LocalLLaMA), Hacker News, Dev.to, Hashnode, Lemmy/Fediverse
   - **Posting approach:** Genuine technical contributions, not link-dropping. Lead with insights, link to reviews in context.
   - **SEO needs:** Google Search Console, Schema.org structured data, backlink building
   - **What I need from Rob:** Reddit account (Tier 3), Google Search Console verification, Dev.to account, OK on transparent AI identity
   - **Execution priority table** with 8 ranked actions
   - **Key principle:** Transparent about being AI-operated on all platforms

3. **Added Schema.org structured data to all pages** — developer work, no accounts needed
   - Reviews get `Review` + `SoftwareApplication` schema (helps rich results in search)
   - Guides/comparisons get `Article` schema
   - Homepage gets `WebSite` schema
   - Created reusable Hugo partials: `schema-review.html`, `schema-article.html`
   - Used Hugo's `dict` + `jsonify` + `safeJS` pipeline for clean JSON-LD output
   - All 25 content pages + homepage now have structured data

4. **Deployed to chatforest.com** — all pages updated with Schema.org markup

### What should happen next
- **Run 30:** While waiting for Rob's reply on the promotion plan, write another review or comparison.
- **Run 31+:** Execute promotion plan once Rob approves accounts, update mega-comparison with Notion
- **Future:** Favicon, newsletter setup, affiliate links

## Run 30 — 2026-03-14 — Content (Best Productivity & Knowledge Management MCP Servers Comparison)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- Pending message #89 (from me, re: traffic/promotion plan) still unanswered. No new messages from Rob.

### What I did

1. **Wrote "Best Productivity & Knowledge Management MCP Servers in 2026"** — `content/guides/best-productivity-mcp-servers.md`
   - **8th comparison article** — completes coverage of all major MCP server categories (browser, database, web scraping, memory, search, documentation, productivity, plus mega-comparison)
   - Head-to-head comparison of 8 servers: Notion (3.5/5), Linear, Todoist, Asana, Google Calendar, Obsidian, Slack (4/5), Google Workspace
   - Researched current state of each: Linear's Feb 2026 PM tools expansion, Todoist's MCP Apps feature, Asana V2 migration, Google Calendar community server, Obsidian's fragmented ecosystem
   - Identified three architectural patterns: first-party hosted (Notion/Linear/Todoist/Asana/Slack), community local (Google Calendar/Google Workspace), local knowledge (Obsidian)
   - Feature comparison table, decision flowchart by use case, recommended stack
   - Key insight: Google has no official MCP server for any product — the biggest gap in the productivity MCP space
   - Cross-links to our Notion and Slack reviews

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Productivity & knowledge management" section with all server recommendations
   - Added productivity rows to summary table (Notion 3.5/5 for knowledge, Linear for tasks)
   - Updated Notion from "not yet reviewed" to reviewed with full section
   - Removed Notion and Linear from "servers we haven't reviewed" section
   - Updated review count to 15, comparison count to 8
   - Added Notion to rating distribution table (3.5/5 cluster now has 5 servers)

3. **Deploy failed** — SSH to chatforest.com returned "Network is unreachable." Likely a network issue on the build server or DreamHost side. Content is committed and ready to deploy next run.

### Site status
- **Committed, NOT deployed** (network issue)
- 25 content pieces: 15 reviews + 2 guides + 8 comparisons
- Content types: reviews, tutorials, explainers, comparisons, mega-comparison
- Comparison articles now cover ALL major categories: browser automation, databases, web scraping, memory/knowledge, search, documentation, productivity/knowledge management, plus mega-comparison
- SEO infrastructure up to date

### What should happen next
- **Run 31:** Deploy (retry rsync). Handle inbox messages. Write another review.
- **Run 32+:** Favicon (waiting for Rob), execute promotion plan when Rob replies
- **Future:** Newsletter setup, affiliate link integration

## Run 31 — 2026-03-14 — Operations + Content (Observability MCP Servers Comparison)

**Mode:** Operations + Researcher + Copywriter + Developer

### Inbox update
- 6 pending messages processed:
  - **#91 (high, Boss Claude):** Backup files + log rotation question — replied with file sizes and rotation plan
  - **#92 (high, Rob):** Reddit username — superseded by #94
  - **#94 (normal, Rob + Boss Claude):** Reddit username — replied suggesting `chatforest_grove`, confirmed `~/.config/chatforest/` for credentials
  - **#93 (normal, Rob):** Confirmed transparent AI authorship everywhere — acknowledged
  - **#90 (normal, Boss Claude):** Email address — replied suggesting `grove@chatforest.com` + `hello@chatforest.com`
  - **#89 (high, from me):** My own traffic/promotion plan reply — marked seen
- All 6 messages marked as seen, 3 replies sent (#95, #96, #97)

### What I did

1. **Rotated WORKLOG.md** — archived runs 1-28 to `WORKLOG-archive-runs-01-28.md`. Active file went from 88K/1225 lines to ~4K/85 lines. Will rotate again at ~50K.

2. **Wrote "Best Observability MCP Servers in 2026"** — `content/guides/best-observability-mcp-servers.md`
   - **9th comparison article** — completes our category coverage
   - Head-to-head comparison of 6 servers: Sentry (4/5, reviewed), Datadog, Grafana, New Relic, Honeycomb, PagerDuty
   - Three observability layers framework: error tracking (Sentry/Honeycomb), full-stack APM (Datadog/New Relic/Grafana), incident management (PagerDuty)
   - Feature comparison table, decision flowchart, recommended two-server stack
   - Key insight: observability is the most "first-party" MCP category — every major platform has an official server
   - Researched current state of each: Datadog GA with 50+ tools, Grafana 1,200+ stars (most popular), New Relic Public Preview with NRQL translation, Honeycomb March 2026 Agent Skills expansion

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Expanded observability section from 2 paragraphs to full category with all 6 servers
   - Removed Datadog from "servers we haven't reviewed" section
   - Updated comparison count from 8 to 9

4. **Deploy failed** — SSH to chatforest.com still returns "Network is unreachable." Same issue as Run 30. Content committed, ready to deploy when network recovers.

### Site status
- **Committed, NOT deployed** (network issue — two consecutive runs)
- 26 content pieces: 15 reviews + 2 guides + 9 comparisons
- Comparison articles: browser automation, databases, web scraping, memory/knowledge, search, documentation, productivity, observability, plus mega-comparison
- All major MCP server categories covered

### What should happen next
- **Run 32:** Deploy (retry rsync — network issue has persisted 2 runs). Write another review — Neon MCP server or Figma Dev Mode MCP are good candidates.
- **Run 33+:** Execute promotion plan when Rob replies on accounts, favicon
- **Future:** Newsletter setup, affiliate link integration

## Run 32 — 2026-03-14 — Content (Neon MCP Server Review) + Deploy Diagnosis

**Mode:** Researcher + Copywriter + Developer + Operations

### Inbox update
- 3 pending messages — all from me (replies #95, #96, #97 from Run 31). No new messages from Rob or Boss Claude.
- Sent message #98 (high priority) to Rob: SSH deploy failing for 3 consecutive runs. IPv4 returns "Connection refused" on port 22, IPv6 "Network is unreachable". HTTP and ping work fine. Asked Rob to check DreamHost panel shell access settings.

### What I did

1. **Diagnosed SSH deploy failure** — network is back (HTTP 200, ping works), but SSH port 22 is explicitly refused. This is a DreamHost-side config change, not a network outage. Notified Rob with detailed diagnosis and specific ask (check DreamHost panel → Manage Users → Shell Access).

2. **Wrote "The Neon MCP Server — Serverless Postgres Management Through Natural Language"** — `content/reviews/neon-mcp-server.md`
   - **16th review**, first cloud-native database MCP server
   - Rating: **4/5** — the most capable database MCP server we've reviewed
   - 20 tools covering project management, branch-based migrations, SQL execution, query tuning, auth, and docs
   - Killer feature: branch-based migration workflow using Neon's copy-on-write storage (prepare → verify → merge/discard)
   - OAuth remote server at mcp.neon.tech (npm package deprecated)
   - Honest about tradeoffs: Neon-only lock-in, development-only limitation, OAuth requires browser (no headless support)
   - Neon built formal eval framework and improved tool selection from 60% to 100%
   - Free tier: 100 projects, 100 CU-hrs/mo, 0.5GB storage per branch

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Database (cloud Postgres)" row with Neon 4/5 as pick
   - Added Neon section to database category description
   - Removed Neon from "servers we haven't reviewed"
   - Updated review count to 16, rating distribution (4/5 cluster now has 7 servers)

4. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added Neon as first entry in contenders table
   - Added full "For Cloud Postgres: Neon MCP" section in replacements
   - Updated decision flowchart with Neon for cloud Postgres
   - Updated bottom line recommendation

5. **Build succeeded** (34ms). **Deploy blocked** — SSH still refused. Content committed, 4 runs of content waiting to deploy.

### Site status
- **Committed, NOT deployed** (SSH issue — 3 consecutive runs)
- 27 content pieces: 16 reviews + 2 guides + 9 comparisons
- Rating range: 2.5–4.5 across 16 reviews (4/5 is most common with 7 servers)

### What should happen next
- **Run 33:** Check inbox for Rob's reply on SSH issue. If SSH fixed, deploy immediately. Write another review (Figma Dev Mode MCP or Supabase).
- **Run 34+:** Execute promotion plan when Rob replies on accounts
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 33 — 2026-03-14 — Content (Supabase MCP Server Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **#99 (high, Rob):** URGENT — stop all SSH/rsync deploy attempts. DreamHost likely throttled us. Do NOT deploy until Rob clears it. Acknowledged and complying.
- Messages #95-98 (from me, previous runs) still pending replies. All marked as seen.

### What I did

1. **Wrote "The Supabase MCP Server — Full Backend Management Through Your AI Assistant"** — `content/reviews/supabase-mcp-server.md`
   - **17th review**, first BaaS (Backend-as-a-Service) MCP server
   - Rating: **4/5** — unmatched breadth, covering database, edge functions, storage, debugging, and more
   - 8 tool groups: account, docs, database, debugging, development, functions, storage, branching
   - Key differentiator vs Neon: Supabase goes wide (full backend), Neon goes deep (database)
   - Best security model we've reviewed: real read-only PostgreSQL role, project scoping, feature group filtering
   - OAuth 2.1 authentication at mcp.supabase.com (no PAT needed)
   - 2.5k GitHub stars (most popular database MCP server)
   - Honest about tradeoffs: schema-only branching (no data copy like Neon), paid plan required for branching, pre-1.0 stability, BaaS lock-in deeper than database lock-in

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Backend-as-a-Service" row with Supabase 4/5
   - Updated Supabase from "not yet reviewed" to reviewed with link
   - Removed Supabase from "servers we haven't reviewed" section
   - Updated review count to 17, rating distribution (4/5 cluster now has 8 servers)
   - Updated database section with Supabase alongside Neon

3. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added Supabase as first entry in contenders table
   - Added full "For Supabase Users: Supabase MCP" section in replacements
   - Updated decision flowchart with Supabase for full backend management
   - Updated bottom line recommendation

4. **Build succeeded.** **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 28 content pieces: 17 reviews + 2 guides + 9 comparisons
- Rating range: 2.5–4.5 across 17 reviews (4/5 is most common with 8 servers)
- Only 2 servers remain unreviewed: Figma Dev Mode, Vercel MCP

### What should happen next
- **Run 34:** Check inbox for Rob's SSH clearance. Write Figma Dev Mode or Vercel MCP review.
- **Run 35+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 34 — 2026-03-14 — Content (Vercel MCP Server Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. Complying with deploy ban.

### What I did

1. **Wrote "The Vercel MCP Server — Deployment Monitoring and Management Through Your AI Assistant"** — `content/reviews/vercel-mcp-server.md`
   - **18th review**, first deployment platform MCP server
   - Rating: **3.5/5** — solid remote-first architecture with strong security, but thin tool coverage
   - 13 tools across 5 categories: documentation, project management, deployments, domains, access/CLI
   - Standout feature: runtime log querying with filtering by level, status code, time range, and full-text search
   - Clean remote-first setup at `mcp.vercel.com` — zero install, OAuth auth, project-specific URLs
   - Honest about tradeoffs: only covers ~20% of Vercel's platform features, client allowlist limits adoption, deploy is CLI passthrough, still public beta after 7 months
   - Compared to community alternatives (Quegenx with 30+ tools) — official is safer, community is more capable

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Deployment" category section with Vercel 3.5/5
   - Added deployment row to summary table
   - Removed Vercel from "servers we haven't reviewed" (only Figma Dev Mode remains)
   - Updated review count to 18, rating distribution (3.5/5 cluster now has 6 servers)

3. **Build succeeded.** **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 29 content pieces: 18 reviews + 2 guides + 9 comparisons
- Rating range: 2.5–4.5 across 18 reviews
- Only 1 server remains unreviewed: Figma Dev Mode

### What should happen next
- **Run 35:** Check inbox for Rob's SSH clearance. Write Figma Dev Mode MCP review (last unreviewed server).
- **Run 36+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 35 — 2026-03-14 — Content (Figma Dev Mode MCP Server Review — Final Unreviewed Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. Complying with deploy ban.

### What I did

1. **Wrote "The Figma Dev Mode MCP Server — Design-to-Code Translation Through Your AI Assistant"** — `content/reviews/figma-dev-mode-mcp-server.md`
   - **19th review**, last unreviewed server from our original list
   - Rating: **3.5/5** — unique write capabilities but crippling free tier
   - 12 tools (8 read, 4 write) covering code generation, design tokens, Code Connect, screenshots, FigJam, and code-to-canvas capture
   - Killer feature: `generate_figma_design` — captures live web pages and converts them to editable Figma frames. No community server can do this.
   - Code Connect maps Figma components to codebase components for improving code generation accuracy over time
   - Biggest issue: **6 tool calls/month** on free tier — most aggressive rate limiting of any MCP server we've reviewed. Paid Figma plan (Dev/Full seats) effectively required.
   - Prescriptive React+Tailwind output can conflict with existing codebases; nested components get flattened
   - Detailed comparison with community Framelink server (13,700 stars vs 403 for official): Framelink outputs descriptive JSON, preserves nesting, ~25% smaller payloads, no seat-type rate limits
   - OAuth remote-first architecture at `mcp.figma.com/mcp`

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Design-to-code" category row with Figma Dev Mode 3.5/5
   - Added full design-to-code section with Framelink comparison
   - Changed "What about servers we haven't reviewed?" to "All servers reviewed" — milestone reached
   - Updated review count to 19, rating distribution (3.5/5 cluster now has 7 servers)

3. **Build succeeded** (38ms). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 30 content pieces: 19 reviews + 2 guides + 9 comparisons
- Rating range: 2.5–4.5 across 19 reviews
- **All servers from original list now reviewed** — milestone reached
- 5 runs of content waiting to deploy

### What should happen next
- **Run 36:** Check inbox for Rob's SSH clearance. With all servers reviewed, pivot to new content types: deeper guides, workflow tutorials, or new server categories (AI/ML, cloud infrastructure, DevOps).
- **Run 37+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 101 — 2026-03-15 — Content (PDF & Document Processing MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "PDF & Document Processing MCP Servers — MarkItDown, Docling, PDF Reader, and More"** — `content/reviews/pdf-document-mcp-servers.md`
   - **66th review**, forty-sixth beyond original list
   - Rating: **3.5/5** — basics well-covered, gaps in creation/editing/OCR
   - 15+ servers across 5 approaches: universal converters, PDF-specific, format conversion, eBook reading, paid API
   - Microsoft MarkItDown: 90,700 stars, 29+ formats, single `convert_to_markdown` tool, v0.1.5
   - IBM Docling MCP: 508 stars (core lib 37K), enterprise layout analysis with Granite-Docling-258M VLM, structured JSON output
   - PDF Reader MCP: 557 stars, fastest extraction (5-10x parallel processing), TypeScript, page selection
   - mcp-pandoc: 512 stars, bidirectional format conversion (10+ formats), Pandoc-powered
   - eBook-MCP: 351 stars, library management for EPUB/PDF with chapter navigation
   - PDF.co MCP: paid API, only server with PDF creation, form filling, invoice parsing
   - Foxit PDFActionInspector: 3 stars, PDF security analysis (JavaScript action extraction)
   - Key gaps: no Adobe MCP server, PDF creation nearly absent in FOSS, OCR inconsistent, no annotation/editing

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "PDF / documents" row to summary table with MarkItDown and Docling as picks
   - Added PDF/Documents entry to beyond-original-list section
   - Updated review count to 66, 3.5/5 tier now has 25 servers

3. **Built site** (88 pages, 59ms). **Deployed** to DreamHost.

### Site status
- **Committed and deployed**
- 66 reviews + 13 comparisons + 4 guides + other pages = 88 total
- Rating range: 2.5–4.5 across 66 reviews

### What should happen next
- **Run 102:** Continue expanding coverage — potential categories: Testing/QA MCP servers, Security scanning, AI/ML model serving, Maps/Geolocation, Data transformation/ETL
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 126 — 2026-03-15 — Content (Workflow Automation & Orchestration MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "Workflow Automation & Orchestration MCP Servers — n8n, Zapier, Make, Airflow, Temporal, Kestra, and More"** — `content/reviews/workflow-automation-mcp-servers.md`
   - **92nd review**
   - Rating: **4.0/5** — strong official vendor participation, n8n ecosystem dominance
   - 20+ servers across 4 subcategories: low-code platforms, data pipeline orchestrators, code-first engines, event-driven orchestrators
   - czlonkowski/n8n-mcp: 15,100 stars, 1,239 n8n nodes, 922 commits — most starred automation MCP server
   - Zapier official: remote MCP at mcp.zapier.com, 8,000+ apps, 40,000+ actions
   - Make official: 153 stars, scenario-as-tool model with on-demand scheduling
   - Apache Airflow: yangkyeongmo at 147 stars with 70+ tools and read-only mode; astronomer at 8 stars with 24+ consolidated tools
   - Temporal MCP: 59 stars, Go, archived January 2026
   - Prefect official: 29 stars, Python beta, intelligent debugging
   - Kestra official: 24 stars, 11 tools for flows/executions/backfills
   - Dagster: 21 stars, 9 tools for pipeline monitoring
   - 5+ additional n8n community implementations noted

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Workflow automation" row to summary table with n8n-MCP and Zapier as picks
   - Added workflow automation entry to beyond-original-list section
   - Updated review count to 92, 4.0/5 tier now has 41 servers

3. **Built site** (114 pages, 73ms). **Deploy pending** — throttle not cleared (next run will deploy).

### Site status
- **Committed, deploy pending**
- 92 reviews + 13 comparisons + 4 guides + other pages = 114 total
- Rating range: 2.5–4.5 across 92 reviews

### What should happen next
- **Run 127:** Deploy if throttle cleared. Continue expanding coverage — potential categories: CMS/Content Management MCP servers, Feature Flags/Experimentation, IoT/Embedded, Translation/Localization, Backup & Disaster Recovery
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 132 — 2026-03-15 — Content (Social Media & Marketing MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "Social Media & Marketing MCP Servers — Twitter/X, Bluesky, Instagram, LinkedIn, Meta Ads, Google Ads, SEO, and More"** — `content/reviews/social-media-marketing-mcp-servers.md`
   - **97th review**, seventy-seventh beyond original list
   - Rating: **3.5/5** — impressive breadth across every major platform, but most servers are shallow
   - 40+ servers across 6 subcategories: Twitter/X, Bluesky/AT Protocol, Instagram/LinkedIn, multi-platform/video, advertising/paid media, SEO/email marketing
   - Meta Ads MCP (628 stars, 26 tools) is the category leader — closest to enterprise-grade ad campaign management
   - Twitter/X has 8+ competing servers with no official one — $100/month API barrier
   - atproto-mcp has 57 tools for Bluesky — the most comprehensive single-platform social server anywhere
   - YouTube's top server (503 stars) only extracts subtitles — massive capability gap
   - Iterable official server scales to 105 tools for email marketing
   - SEO tooling relies on scrapers (cnych/seo-mcp at 224 stars) rather than official APIs

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Social media / marketing" row to summary table with Meta Ads MCP and twitter-mcp as picks
   - Added social media/marketing entry to beyond-original-list section
   - Updated review count to 97

3. **Built site** (119 pages, 78ms). **Deploy pending** — throttle not yet cleared.

### Site status
- **Committed, deploy pending**
- 97 reviews + 13 comparisons + 4 guides + other pages = 119 total
- Rating range: 2.5–4.5 across 97 reviews

### What should happen next
- **Run 133:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Translation/Localization, IoT/Embedded, Feature Flags/Experimentation, Healthcare/Medical, Legal/Contract Management
- **Future:** Favicon, newsletter setup, affiliate link integration
