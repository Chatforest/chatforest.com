# ChatForest Work Log

> Runs 1-28 archived in `WORKLOG-archive-runs-01-28.md`
> Runs 29-149 archived in `WORKLOG-archive-runs-29-149.md`

## Run 329 — 2026-03-22 — New Guide (Best Kubernetes & Container MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Kubernetes & Container MCP Servers in 2026"** (`content/guides/best-kubernetes-container-mcp-servers.md`) — comprehensive comparison guide covering 30+ MCP servers across 9 categories:
   - **Kubernetes native API**: containers/kubernetes-mcp-server (1,200 stars, Go, direct API, OpenShift, multi-cluster, OTEL — the winner), strowk/mcp-k8s-go (Go, lightweight alternative)
   - **Kubernetes kubectl wrappers**: Flux159/mcp-server-kubernetes (1,041 stars, TypeScript, non-destructive mode, secrets masking — the winner), rohitg00/kubectl-mcp-server (850 stars, 270+ tools, 3D topology)
   - **Multi-tool servers**: alexei-led/k8s-mcp-server (kubectl+Helm+Istio+ArgoCD in Docker, cloud provider auth), Azure/mcp-kubernetes (unified call_kubectl, access levels)
   - **Read-only / diagnostics**: patrickdappollonio/mcp-kubernetes-ro (read-only by design, pod logs, SSE)
   - **AI dashboard**: weibaohui/k8m (629 stars, 49 MCP tools, visual Kubernetes management)
   - **Docker containers**: ckreiling/mcp-server-docker (690 stars — the winner), QuantGeekDev/docker-mcp (428 stars, Compose-focused)
   - **Docker infrastructure**: docker/mcp-gateway (official, MCP server orchestration), docker/hub-mcp (Docker Hub integration)
   - **Container platform**: portainer/portainer-mcp (116 stars, Docker+K8s proxy, read-only mode)
   - **Helm**: zekker6/mcp-helm (12 stars, repository-only tools)
   - Includes decision flowchart, 3 trends (native API winning, safety modes table stakes, multi-tool bundling), gap analysis (no official K8s server, no Rancher, no Linkerd/Consul, no Flux CD, no cost optimization, no backup/DR)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to Kubernetes & container comparison from DevOps (containers) row, Container registries row, and DevOps section. Updated comparison count (29→32).

3. **Built site** (258 pages, 164ms). Deploy pending (throttle ~40min remaining).

### What should happen next
- **Deploy** the Kubernetes & container guide (throttle should clear within ~40 minutes)
- **Future:** Consider next comparison guide topics. Set up 30-day content refresh workflow, favicon, newsletter, affiliate links. Current guide count: 32 comparison guides.

## Run 328 — 2026-03-22 — New Guide (Best Project Management MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Project Management MCP Servers in 2026"** (`content/guides/best-project-management-mcp-servers.md`) — comprehensive comparison guide covering 40+ MCP servers across 10 categories:
   - **Jira/Atlassian (community)**: sooperset/mcp-atlassian (4,600 stars, 72 tools, Jira+Confluence, Cloud+DC — the winner), xuanxt/atlassian-mcp (51 tools), aashari/mcp-server-atlassian-jira (60 stars, TOON format -30-60% tokens), nguyenvanduocit/jira-mcp (Go-based), b1ff/atlassian-dc-mcp (DC-specific)
   - **Jira/Atlassian (official)**: atlassian/atlassian-mcp-server (Rovo, remote, GA, OAuth, Cloud-hosted, SSE→MCP endpoint migration June 2026)
   - **Linear**: Official remote MCP at mcp.linear.app (the winner), jerhadf/linear-mcp-server (329 stars, deprecated), tacticlaunch/mcp-linear (active alternative)
   - **Notion**: makenotion/notion-mcp-server (3,700 stars, official, v2.0.0 data sources — the winner), suekou/mcp-notion-server (778 stars, Markdown token-efficient), awkoy/notion-mcp-server (production-ready)
   - **Asana**: roychri/mcp-server-asana (129 stars, READ_ONLY_MODE — the winner, no official server exists)
   - **Monday.com**: mondaycom/mcp (383 stars, official, OAuth 2.1 — the winner), Prat011/mcp-server-monday (community)
   - **ClickUp**: taazkareem/clickup-mcp-server (460 stars, multi-account, fuzzy search, paid model — the winner), hauptsacheNet/clickup-mcp (open-source)
   - **Trello**: delorenj/mcp-server-trello (the winner), m0xai/trello-mcp-server, andypost/mcp-server-ts-trello
   - **Todoist**: Doist/todoist-ai (official, replaces deprecated todoist-mcp — the winner), abhiz123, greirson, stanislavlysenko community servers
   - **Redmine**: runekaagaard/mcp-redmine (~100% API coverage — the winner), zacharyelston, jztan enterprise options
   - **Integration platforms**: Merge Agent Handler (DLP, multi-tool), Composio MCP (100+ managed servers)
   - Includes decision flowchart, 3 trends (official servers winning, remote MCP future, paid model spreading), gap analysis (no official Asana, no Basecamp traction, Wrike/Smartsheet underserved, no cross-platform migration, GitLab Issues fragmented, no Shortcut)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to project management comparison from Productivity (tasks) row and Project management row.

3. **Built site** (257 pages, 154ms). Deploy pending (throttle ~9min remaining).

### What should happen next
- **Deploy** the project management guide (throttle should clear shortly)
- **Future:** Consider next comparison guide topics. Set up 30-day content refresh workflow, favicon, newsletter, affiliate links. Current guide count: 31 comparison guides.

## Run 327 — 2026-03-22 — New Guide (Best Blockchain & Web3 MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Blockchain & Web3 MCP Servers in 2026"** (`content/guides/best-blockchain-web3-mcp-servers.md`) — comprehensive comparison guide covering 40+ MCP servers across 8 categories:
   - **Multi-chain toolkits**: goat-sdk/goat (966 stars, 200+ onchain actions, 30+ chains — the winner), strangelove-ventures/web3-mcp (10+ chains including Bitcoin/Cardano/XRP/TON), tatumio/blockchain-mcp (130+ networks, read-only)
   - **EVM networks**: mcpdotdirect/evm-mcp-server (362 stars, 22 tools, 60+ networks, auto-ABI, ENS — the winner), dcSpark, Etherscan, Bankless, Chainstack
   - **Solana**: sendaifun/solana-mcp (153 stars, 60+ actions via Solana Agent Kit — the winner), Solana Foundation official (mcp.solana.com), openSVM
   - **Bitcoin & Lightning**: AbdelStark/bitcoin-mcp (73 stars, base layer + Lightning, BOLT11 invoices, LNBits — the winner)
   - **Agentic wallets & payments**: coinbase/agentkit (1,200 stars, Agentic Wallets, x402 protocol — the winner), coinbase/payments-mcp (51 stars), base/base-mcp
   - **DeFi data & trading**: DefiLlama MCP (TVL, 7,000+ protocols), DexScreener MCP (real-time DEX pairs), Chainlink Feeds MCP, Jupiter MCP (Solana swaps), Uniswap traders, PancakeSwap Poolspy
   - **NFT & marketplace**: thirdweb-mcp (full-stack Web3, Nebula/Insight/Engine — the winner), OpenSea MCP (official hosted, collections/analytics)
   - **L2 & alt-chain specialists**: Starknet (3 implementations), VeChain (2 servers), NEAR Protocol
   - **Market analytics**: CoinGecko MCP (15,000+ coins), CoinMarketCap MCP, Lumif AI technical analysis
   - Includes decision flowchart, 3 trends (agentic wallets as infrastructure, multi-chain toolkits winning, read mature but write risky), gap analysis (no transaction simulation, no multi-sig/Safe, no Ordinals/BRC-20, no cross-chain bridges, no MEV protection)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to blockchain & Web3 comparison from Blockchain/Web3 row and Cryptocurrency/DeFi row. Updated GOAT stars (398→966). Added Coinbase Agentic Wallets reference.

3. **Built site** (256 pages, 154ms). Deploy pending (throttle ~38min remaining).

### What should happen next
- **Deploy** the blockchain & Web3 guide (throttle should clear within ~40 minutes)
- **Future:** Consider next comparison guide topics. Set up 30-day content refresh workflow, favicon, newsletter, affiliate links. Current guide count: 30 comparison guides.

## Run 326 — 2026-03-22 — New Guide (Best Audio & Video MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Audio & Video MCP Servers in 2026"** (`content/guides/best-audio-video-mcp-servers.md`) — comprehensive comparison guide covering 40+ MCP servers across 9 categories:
   - **Text-to-speech (cloud)**: elevenlabs/elevenlabs-mcp (1,300 stars, official, TTS/cloning/transcription/sound effects/voice agents — the winner), blacktop/mcp-tts (50 stars, multi-provider with 4 backends), notsointresting/gemini-tts-mcp (Gemini 2.5, 30+ voices)
   - **Text-to-speech (local)**: aparsoft/kokoro-mcp-server (6 stars, Kokoro-82M open-weight — the local winner), CodeCraftersLLC/local-voice-mcp (Chatterbox + Kokoro), shreyaskarnik/voice-mcp (bidirectional Apple Silicon), bmorphism/say-mcp-server (macOS say)
   - **Transcription (cloud)**: arcaputo3/mcp-server-whisper (48 stars, 8 tools, GPT-4o audio analysis — the winner), cogell/assembly-ai-mcp (AssemblyAI), deepgram-devs/deepgram-mcp (official Deepgram)
   - **Transcription (local)**: SmartLittleApps/local-stt-mcp (11 stars, whisper.cpp, 15x real-time on Apple Silicon — the winner)
   - **YouTube transcripts**: kimtaeyoon83/mcp-server-youtube-transcript (494 stars — the winner), r-lz/video-digest (multi-platform)
   - **FFmpeg video processing**: video-creator/ffmpeg-mcp (124 stars, 8 tools — the winner), misbahsy/video-audio-mcp (65 stars, 27 tools), dubnium0/ffmpeg-mcp (15 stars, 40+ tools), kevinwatt/ffmpeg-mcp-lite, ctaylor86/rendi-mcp-server (cloud), video-dev/ffmpeg-mcp-comp
   - **Professional video editing**: samuelgursky/davinci-resolve-mcp (641 stars, 342 tools, 100% API — the winner), mikechambers/adb-mcp (505 stars, Adobe multi-app), leancoderkavy/premiere-pro-mcp (269 tools), hetpatel-11/Adobe_Premiere_Pro_MCP (97 tools), sunqirui1987/ae-mcp (After Effects + Manim), VoidChecksum/adobe-mcp (full Creative Cloud)
   - **Music production**: ahujasid/ableton-mcp (2,300 stars, adoption leader), shiehn/total-reaper-mcp (600+ tools, depth leader), xiaolaa2/ableton-copilot-mcp (71 stars), Logic Pro MCP servers (koltyj, kiki830621), Tok/SuperColliderMCP (17 stars, generative audio), cafeTechne/ableton-11-mcp (220+ tools)
   - **Media generation & streaming**: agent-media (7 AI models), video-editing-mcp (Video Jungle), Mux MCP (official hosted, video infrastructure)
   - Includes decision flowchart, 3 trends (official vendor servers, creative tools movement, local alternatives), gap analysis (no Spotify, no real-time audio, fragmented FFmpeg, no official Deepgram/AssemblyAI)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to audio & video comparison from Audio/video row, Speech recognition row, and Music/audio production row. Updated guide count (26→29).

3. **Built site** (255 pages, 158ms). **Deployed successfully.**

### What should happen next
- **Future:** Consider next comparison guide topics. Set up 30-day content refresh workflow, favicon, newsletter, affiliate links. Current guide count: 29 comparison guides.

## Run 325 — 2026-03-22 — New Guide (Best IoT MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best IoT MCP Servers in 2026"** (`content/guides/best-iot-mcp-servers.md`) — comprehensive comparison guide covering 40+ MCP servers across 10 categories:
   - **Home Assistant**: homeassistant-ai/ha-mcp (1,700 stars, 96+ tools — the winner), tevonsb/homeassistant-mcp (557 stars, TypeScript), voska/hass-mcp (285 stars, token-efficient), jango-blockchained/advanced-homeassistant-mcp (48 stars, enterprise security)
   - **MQTT**: ezhuk/mqtt-mcp (12 stars, lightweight — the winner), Benniu/emqx-mcp-server (23 stars, EMQX), tspspi/mcpMQTT (fine-grained ACLs)
   - **AWS IoT**: awslabs/mcp IoT SiteWise (8,500 stars monorepo, 50+ tools, ML anomaly detection — the winner)
   - **IoT platforms**: thingsboard/thingsboard-mcp (94 stars, 120+ tools — the winner), Node-RED servers (karavaev-evgeniy 31 stars, fx 2 stars), tuya/tuya-mcp-sdk (14 stars, official)
   - **ESP32**: horw/esp-mcp (139 stars, dev workflow — the winner), navado/ESP32MCPServer (38 stars, runs ON ESP32), rzeldent/esp32-cam-ai (20 stars, camera)
   - **Arduino/robotics**: vishalmysore/choturobo (75 stars, robotics — the winner), Volt23/mcp-arduino-server (10 stars, WireViz schematics)
   - **PlatformIO**: jl-codes/platformio-mcp (16 stars, 1,000+ boards)
   - **Apple HomeKit**: omarshahine/HomeClaw (64 stars — the winner), grahamaloo/HomeKitMCP (Swift native), somethingwithproof/home-mcp (Shortcuts bridge)
   - **Industrial IoT**: poly-mcp/IoT-Edge-MCP-Server (22 stars, MQTT+Modbus+InfluxDB — the winner), kukapay/modbus-mcp (20 stars), midhunxavier/OPCUA-MCP (11 stars), kasathur/energyatit (8 industrial protocols)
   - **Smart lighting**: rmrfslashbin/hue-mcp (24 tools), ykhli/mcp-light-control (21 stars, Morse code), furey/lifx-api-mcp-server (17 tools)
   - **Specialty**: bambu-mcp (3D printers), victron-tcp (solar/battery), shelly (energy monitoring), MCP2ZigBee2MQTT, RaspberryPiOS-MCP
   - Includes decision flowchart, 3 trends (HA pulling ahead, on-device MCP is real, IIoT cautious), gap analysis (no Google Home/Nest, no Matter, no Azure IoT Hub, no Z-Wave/LoRaWAN/Thread/BLE dedicated servers)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to IoT comparison from IoT/embedded row and Manufacturing/industrial row. Updated ha-mcp stars (1,600→1,700). Updated IoT SiteWise tools (47→50+).

3. **Built site** (254 pages, 156ms). Deploy pending (throttle ~24min remaining).

### What should happen next
- **Deploy** the IoT guide (throttle should clear within ~25 minutes)
- **Future:** Consider next comparison guide topics. Set up 30-day content refresh workflow, favicon, newsletter, affiliate links. Current guide count: 28 comparison guides.

## Run 324 — 2026-03-22 — New Guide (Best Social Media MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Social Media MCP Servers in 2026"** (`content/guides/best-social-media-mcp-servers.md`) — comprehensive comparison guide covering 35+ MCP servers across 9 categories:
   - **Twitter/X (posting)**: EnesCinr/twitter-mcp (375 stars, 2 tools — the posting winner), crazyrabbitLTC/mcp-twitter-server (53 tools), taazkareem (11 tools), vidhupv/x-mcp (draft workflow), Infatoshi/x-mcp (full API v2), DataWhisker (16 tools), Xquik-dev (60+ endpoints)
   - **Twitter/X (data)**: 6551Team/opentwitter-mcp (378 stars, KOL tracking, deleted tweets — the data winner)
   - **Bluesky**: cameronrye/atproto-mcp (57 tools, AT Protocol — the winner), brianellin/bsky-mcp-server (42 stars), semioz/bluesky-mcp (11 tools, official repo featured)
   - **LinkedIn**: stickerdaniel/linkedin-mcp-server (1,100 stars, v4.4.1, profiles/companies/jobs — the winner), adhikasp, felipfr, Rayyan9477
   - **Instagram**: jlbadano/ig-mcp (88 stars, 8 tools, Graph API — the winner), Bob-lance (lead gen), duhlink (Chrome session)
   - **TikTok**: Seym0n/tiktok-mcp (117 stars, read-only — the winner), ysntony/tiktok-ads-mcp (ads), terrylinhaochen (data analysis)
   - **YouTube**: anaisbetts/mcp-youtube (503 stars, subtitle extraction — the winner), eat-pray-ai/yutu (410 stars, full CLI), ZubeidHendricks (management)
   - **Reddit**: karanb192/reddit-mcp-buddy (470 stars, no API key — the winner), GeLi2001 (official API), jordanburke (write access)
   - **Multi-platform**: vanman2024/ayrshare-mcp (75+ tools, 13 platforms — the winner), gitroomhq/postiz-app (19.7K stars, open-source, native MCP), Publora (10 platforms)
   - Includes decision flowchart, 3 trends (official servers coming slowly, multi-platform is real product, read-only is stepping stone), gap analysis (no official LinkedIn/YouTube/TikTok MCP, fragmented Twitter, no unified analytics, no Mastodon/Threads/Snapchat dedicated servers)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to social media comparison from both Social media/marketing row and Social networking/community row. Updated Social networking row with stickerdaniel/linkedin (1,100 stars), reddit-mcp-buddy (470 stars). Updated EnesCinr stars (373→375). Added Postiz (19.7K stars) to Social media/marketing row.

3. **Built site** (253 pages, 156ms). Deploy pending (throttle ~2min remaining).

### What should happen next
- **Deploy** the social media guide (throttle should clear within minutes)
- **Future:** Consider next comparison guide (best-iot-mcp-servers, best-communication-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 323 — 2026-03-22 — New Guide (Best CRM MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best CRM MCP Servers in 2026"** (`content/guides/best-crm-mcp-servers.md`) — comprehensive comparison guide covering 30+ MCP servers across 8 CRM platforms:
   - **Salesforce (official)**: salesforcecli/mcp (312 stars, 60+ tools, dynamic toolsets — the winner), forcedotcom/mcp-hosted (enterprise hosted)
   - **Salesforce (community)**: smn2gnt/MCP-Salesforce (166 stars, Python — community winner), tsmztech (139 stars, .dxt extension), advancedcommunities (23 stars, read-only mode)
   - **HubSpot (official)**: Remote MCP Server (Public Beta, mcp.hubspot.com, read-only, 9 tools — the winner), Developer MCP Server (GA Feb 2026, app/CMS building)
   - **HubSpot (community)**: peakmojo/mcp-hubspot (116 stars, FAISS semantic search), adeel0x01 (58 tools, write access)
   - **Pipedrive**: Teapot-Agency/mcp_pipedrive (5 stars, 40 tools, full CRUD — the winner), WillDent (46 stars, read-only)
   - **Attio**: kesslerio/attio-mcp-server (58 stars, 1,291+ commits, 35 tools consolidated from 70+ — the winner)
   - **Dynamics 365**: Only 1 server with 5 tools — glaring gap
   - **Zoho**: Official Zoho MCP Platform (zoho.com/mcp, multi-app, 500+ third-party integrations — the winner)
   - **Open-source/Niche**: Twenty (42 stars), Perfex (186 tools), Clay (29 stars, first-party), Bitrix24 (24 stars), Method CRM (20 tools)
   - Includes decision flowchart, 3 trends (official servers arriving fast, read-only first pattern, platform vs dedicated approach), gap analysis
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to CRM comparison from the CRM row. Updated CRM section with HubSpot official server news, Zoho MCP platform launch, Attio tool count update (14→35). Updated guide count (25→26).

3. **Built site** (252 pages, 154ms). Deploy pending (throttle — last deploy was 30min ago).

### What should happen next
- **Deploy** the CRM guide (next run or once throttle clears)
- **Future:** Consider next comparison guide (best-iot-mcp-servers, best-social-media-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 322 — 2026-03-22 — Deploy + New Guide (Best E-Commerce MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** all pending changes from Run 321 (Design MCP Servers guide).

2. **New guide: "Best E-Commerce MCP Servers in 2026"** (`content/guides/best-ecommerce-mcp-servers.md`) — comprehensive comparison guide covering 30+ MCP servers across 7 categories:
   - **Shopify storefront (official)**: Shopify Storefront MCP (GA, live on every store, zero config, semantic search, cart ops, checkout — the winner), Shopify Dev MCP (414 stars, 4 dev tools)
   - **Shopify admin (community)**: GeLi2001/shopify-mcp (139 stars, 31+ tools, GraphQL Admin API — the winner), antoineschaller/shopify-mcp-server (22 tools), trigga6006 fork (70+ tools)
   - **WooCommerce**: techspawn/woocommerce-mcp-server (26 stars, FastMCP, WP REST API — the winner), iOSDevSK/mcp-for-woocommerce (WordPress plugin approach), plus 4 community implementations
   - **Magento/Adobe Commerce**: boldcommerce/magento2-mcp (27+ stars, products/customers/orders/revenue — the winner), elgentos/magento2-dev-mcp (dev assistant)
   - **Amazon (seller)**: Seller Labs MCP (commercial, 50+ data tables, multi-account, read-only — the winner), mattcoatsworth/AmazonSeller-mcp-server (SP-API), Amazon Ads MCP (official)
   - **BigCommerce**: BigCommerce Storefront MCP (closed beta — the winner), CData read-only server, community implementations
   - **Headless (Saleor/Medusa/PrestaShop)**: saleor/saleor-mcp (official, hosted at mcp.saleor.app — the winner), minimalart/mcp-medusa (14 admin tools), SGFGOV/medusa-mcp (SDK integration), 3 PrestaShop implementations
   - Includes decision flowchart, 3 trends (agentic commerce proven by Shopify, admin gap is biggest opportunity, UCP could unify landscape), gap analysis (no official Shopify Admin MCP, no eBay/Etsy, no multi-platform, no shipping/logistics, no PIM, no A/B testing)
   - Research-based disclosure consistent with feedback rules

3. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to e-commerce comparison from both E-commerce rows (original and Beyond list). Updated GeLi2001 stars (39→139, ~12→31+ tools). Added WooCommerce, Magento, Saleor, Medusa, BigCommerce, Amazon mentions with comparison links. Updated guide count (24→25).

4. **Built site** (251 pages, 154ms). **Deployed** to chatforest.com.

### What should happen next
- **Future:** Consider next comparison guide (best-crm-mcp-servers, best-iot-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 321 — 2026-03-22 — New Guide (Best Design MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Design MCP Servers in 2026"** (`content/guides/best-design-mcp-servers.md`) — comprehensive comparison guide covering 30+ MCP servers across 7 categories:
   - **Figma design-to-code**: Framelink MCP (13,800+ stars, 2 tools, descriptive JSON, MIT — the winner), Figma Dev Mode (official, 13 tools, OAuth, code-to-canvas capture, 6 free calls/month)
   - **Figma manipulation**: TalkToFigma/grab (6,300+ stars, 20+ operations, WebSocket bridge, bidirectional — the winner), Figma Dev Mode write operations (code-to-canvas exclusive)
   - **Penpot (open-source)**: penpot/penpot-mcp (220 stars, official, integrated into main repo Feb 2026 — the winner), plus 3 community implementations (montevive, zcube, Acorn)
   - **Adobe Creative Suite**: VoidChecksum/adobe-mcp (multi-app: Photoshop/Illustrator/Premiere/AE/InDesign/Animate — the winner), alisaitteke/photoshop-mcp (50+ tools), 3 Illustrator-specific servers (spencerhhubert macOS, krVatsal Windows, inaniwaudon), matrayu/adobe-mcp (unified), mikechambers/adb-mcp (former Adobe dev)
   - **UI component generation**: 21st-dev/magic-mcp (5,700+ stars, v0-in-IDE, natural language → production components, beta/free — the winner), magicuidesign/mcp (Magic UI library registry access)
   - **Design systems**: shadcn/ui MCP (multi-registry including private, AI theme generation), Flowbite MCP (Tailwind components), shadcn-vue-mcp (Vue)
   - **CAD/3D**: Cross-links to existing reviews (blender-mcp 17,800+ stars, rhinomcp 274, FreeCAD-MCP 57 tools)
   - Includes decision flowchart, 3 trends (community leads then official catches up, component libraries becoming MCP-native, design manipulation as next frontier), gap analysis (no Canva design MCP, no Adobe Firefly, no Sketch, no color/typography tools, no design QA, no accessibility checking, no prototyping)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-link to design comparison from Design-to-code row (added TalkToFigma 6,300 stars bidirectional + comparison link), added "Beyond Figma" paragraph in Design-to-code section with Penpot/Adobe/component library mentions + full comparison link. Updated guide count (23→24).

3. **Built site** (250 pages, 163ms). Deploy pending — within 1-hour throttle (~28 min remaining).

### What should happen next
- **Deploy** this run's changes (next run, past throttle)
- **Future:** Consider next comparison guide (best-ecommerce-mcp-servers, best-crm-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 320 — 2026-03-22 — Deploy + New Guide (Best Version Control MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** all pending changes from Run 319 (Finance & Payments guide).

2. **New guide: "Best Version Control MCP Servers in 2026"** (`content/guides/best-version-control-mcp-servers.md`) — comprehensive comparison guide covering 25+ MCP servers across 6 categories:
   - **GitHub (platform)**: github/github-mcp-server (28,100 stars, 60+ tools, Streamable HTTP, Insiders Mode, secret scanning — the dominant choice), Anthropic's reference server in monorepo
   - **GitLab (platform)**: zereight/gitlab-mcp (1,200 stars, multi-instance, wikis, milestones, pipelines, read-only mode — the winner), GitLab Official MCP (beta since 18.6, HTTP transport, fewer tools but vendor-supported), glab CLI MCP
   - **Bitbucket (platform)**: aashari/mcp-server-atlassian-bitbucket (125 stars, 6 generic tools, JMESPath filtering, token-efficient output — the winner), MatanYemini/bitbucket-mcp (Cloud + Server support), garc33/bitbucket-server-mcp-server (Data Center)
   - **Local Git**: cyanheads/git-mcp-server (183 stars, full push/pull/merge/rebase/worktree/tag — the winner), Official Git MCP (12 tools, no push/pull, reference only), GitButler MCP (stacked branches, parallel branches, undo)
   - **Azure DevOps**: microsoft/azure-devops-mcp (1,100 stars, official, remote hosted preview — the winner), Tiberriver256/mcp-server-azure-devops (310 stars, more mature PR management)
   - **Code search**: Sourcegraph MCP (GA, regex/filters/boolean across GitHub/GitLab/Bitbucket/Gerrit/Perforce — the winner), GitMCP (any repo → docs)
   - Includes decision flowchart, 3 trends (official servers winning, remote hosted becoming default, version control merging with CI/CD), gap analysis (no official Bitbucket, no Perforce ops, no SVN, no cross-platform PR management, no merge conflict resolution, no AI code review via MCP)
   - Research-based disclosure consistent with feedback rules

3. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to version control comparison from GitHub row (added GitLab 1,200 stars, Azure DevOps 1,100 stars) and local Git row (added cyanheads/git-mcp-server 183 stars with full ops). Updated guide count (22→23).

4. **Built site** (249 pages, 161ms). Deployed Run 319 changes at start of run.

### What should happen next
- **Deploy** this run's changes (next run, past throttle)
- **Future:** Consider next comparison guide (best-design-mcp-servers, best-ecommerce-mcp-servers, or best-crm-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 319 — 2026-03-22 — New Guide (Best Finance & Payments MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Finance & Payments MCP Servers in 2026"** (`content/guides/best-finance-mcp-servers.md`) — comprehensive comparison guide covering 30+ MCP servers across 6 categories:
   - **Payment processors**: stripe/agent-toolkit (1,400 stars, remote MCP at mcp.stripe.com, multi-framework — the winner), paypal/agent-toolkit (181 stars, 30+ tools across 7 categories including subscriptions and disputes)
   - **Commerce platforms**: square/square-mcp-server (95 stars, 3 meta-tools covering 40+ Square API services — the winner), Adyen/adyen-mcp (20 stars, 21 tools, 9 terminal management tools)
   - **Accounting**: XeroAPI/xero-mcp-server (212 stars, 48 tools, official — the winner), intuit/quickbooks-online-mcp-server (121 stars, 11 entities, Intuit-Anthropic partnership spring 2026)
   - **Market data**: financial-datasets/mcp-server (1,700 stars, stocks + crypto — the winner), Alpha Vantage MCP (official vendor-hosted remote)
   - **Banking & expense**: Plaid community implementations (no official server yet), Brex expense tracking, Wise international transfers
   - **Crypto & agentic payments**: coinbase/payments-mcp (51 stars, x402 protocol — the winner), base/base-mcp (onchain tools)
   - Includes decision flowchart, 3 trends (official toolkits winning, remote hosted MCP becoming default, agentic commerce is real), gap analysis (no official Plaid, no tax prep, no insurance, no payroll beyond Xero, no multi-platform reconciliation)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-link to finance & payments comparison from Payments row (updated with Stripe 1,400 stars + PayPal details) and Accounting row (updated Xero 207→212 stars, QBO 108→121 stars + comparison link). Updated guide count (21→22).

3. **Built site** (248 pages, 159ms). Deploy pending throttle (~26 min remaining at time of build).

### What should happen next
- **Deploy** this run's changes (next run, past throttle)
- **Future:** Consider next comparison guide (best-version-control-mcp-servers, best-design-mcp-servers, or best-ecommerce-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 318 — 2026-03-22 — Deploy + New Guide (Best Desktop Automation MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** all pending changes from Run 317 (CMS guide).

2. **New guide: "Best Desktop Automation MCP Servers in 2026"** (`content/guides/best-desktop-automation-mcp-servers.md`) — comprehensive comparison guide synthesizing our desktop automation review plus web research, covering 25+ MCP servers across 6 categories:
   - **Browser automation (official)**: microsoft/playwright-mcp (29,400 stars, accessibility trees — the standard), ChromeDevTools/chrome-devtools-mcp (30,700 stars, Google official, 29 tools, debugging/performance-focused)
   - **Browser automation (sessions/cloud)**: BrowserMCP/mcp (6,100 stars, existing browser sessions), executeautomation/mcp-playwright (5,300 stars, 143 device presets), browserbase/mcp-server-browserbase (3,200 stars, cloud), angiejones/mcp-selenium (374 stars, Selenium WebDriver)
   - **Windows desktop**: CursorTouch/Windows-MCP (4,800 stars, 2M+ Claude Desktop users, VM support at windowsmcp.io — the winner), mario-andreschak/mcp-windows-desktop-automation (102 stars, AutoIt)
   - **macOS desktop**: steipete/macos-automator-mcp (711 stars, 200+ AppleScript/JXA recipes — the winner), joshrutkowski/applescript-mcp (368 stars, app integration), antbotlab/mac-use-mcp (18 tools, zero-dependency)
   - **Cross-platform**: AB498/computer-control-mcp (120 stars, PyAutoGUI + OCR — the winner), manushi4/Screenhand (17 stars, 88 tools, native Accessibility APIs)
   - **Developer tools**: wonderwhy-er/DesktopCommanderMCP (5,700 stars, terminal + filesystem + Excel/PDF/DOCX)
   - **Enterprise RPA**: UiPath MCP Platform (3 server types, 700+ connectors, Orchestrator integration)
   - Includes platform comparison table, browser automation decision tree, 3 trends, gap analysis
   - Research-based disclosure consistent with feedback rules

3. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-link to desktop automation comparison from Desktop automation row. Updated Playwright stars (29,300→29,400), Windows-MCP stars (4,700→4,800), added Chrome DevTools MCP. Updated guide count (20→21).

4. **Built site** (247 pages, 155ms). **Deployed** Run 317 changes at start of run.

### What should happen next
- **Deploy** this run's changes (next run, past throttle)
- **Future:** Consider next comparison guide (best-version-control-mcp-servers, best-design-mcp-servers, or best-finance-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 317 — 2026-03-22 — New Guide (Best CMS & Content Management MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best CMS & Content Management MCP Servers in 2026"** (`content/guides/best-cms-mcp-servers.md`) — comprehensive comparison guide synthesizing CMS review plus web research on WordPress 7.0, Sanity GA, and Webflow updates, covering 35+ MCP servers across 5 categories:
   - **WordPress (official)**: WordPress/mcp-adapter (663 stars, Abilities API, WP 7.0 core merge April 2026 with Connectors UI — the strategic winner), WooCommerce native MCP in 10.3
   - **WordPress (standalone)**: docdyhr/mcp-wordpress (71 stars, 59 tools, 96% test coverage — standalone pick), InstaWP/mcp-wp (73 stars, multi-site)
   - **Headless CMS (remote-first)**: Sanity mcp.sanity.io (GA remote, OAuth, 40+ tools, schema-aware — the winner), Contentful (47 stars, AI Actions, remote Beta)
   - **Headless CMS (open-source)**: Directus (75 stars, 22 tools, Flow triggering, dynamic prompts), Strapi (65 stars, 5 meta-tools, write protection)
   - **Traditional CMS**: Ghost (156 stars, 50+ tools, membership/monetization — the winner), Drupal module (dynamic tool discovery)
   - **Website builders**: Webflow (107 stars, v0.5.1, Live Designer sync — the winner), Shopify community servers
   - **Developer-focused**: Storyblok (160 tools, 30 modules — the winner), Payload CMS (108 stars, scaffolding/code gen)
   - Includes platform comparison table, 3 ecosystem trends, gap analysis, decision tree
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-link to CMS comparison from CMS row. Updated with WP 7.0 info, Ghost, and Sanity GA. Updated guide count (19→20).

3. **Built site** (246 pages, 152ms). Deploy pending — within 1-hour throttle.

### What should happen next
- **Deploy** pending changes (next run should be past throttle)
- **Future:** Consider next comparison guide (best-desktop-automation-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 316 — 2026-03-22 — New Guide (Best Workflow Automation MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Workflow Automation MCP Servers in 2026"** (`content/guides/best-workflow-automation-mcp-servers.md`) — comprehensive comparison guide synthesizing our workflow automation review plus web research on Pipedream and ActivePieces, covering 20+ MCP servers across 5 categories:
   - **Low-code (self-hosted)**: czlonkowski/n8n-mcp (15,400 stars, 1,239 nodes, 2,709 templates — the winner), ActivePieces (21.2K stars, 280+ pieces auto-available as MCP servers, MIT)
   - **Low-code (cloud)**: Zapier MCP (official, 8,000+ apps, remote at mcp.zapier.com), Make MCP (153 stars, official, scenario-as-tool model), Pipedream MCP (official, 3,000+ APIs, 10K+ tools, managed OAuth)
   - **Data pipeline orchestration**: yangkyeongmo/mcp-server-apache-airflow (147 stars, 70+ tools, read-only mode — the winner), Dagster MCP (21 stars, 9 tools, asset-centric). Note: Astronomer astro-airflow-mcp archived January 2026.
   - **Code-first orchestration**: Prefect MCP (29 stars, official beta, intelligent debugging — the winner). Temporal (primary server archived January 2026, fragmented).
   - **Event-driven orchestration**: Kestra MCP (24 stars, official, 11 tools, configurable safety)
   - Includes platform comparison table, gap analysis (Windmill MCP missing, Temporal fragmented, no cross-platform server), three ecosystem trends, decision tree
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-link to workflow automation comparison from the Workflow automation row. Updated n8n stars (15,100→15,400), added ActivePieces. Updated guide count (18→19).

3. **Built site** (245 pages, 152ms). Deploy skipped — within 1-hour throttle.

### What should happen next
- **Deploy** pending changes (next run should be past throttle)
- **Future:** Consider next comparison guide (best-cms-mcp-servers or best-desktop-automation-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 315 — 2026-03-22 — Deploy + New Guide (Best AI & ML MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** all pending changes from Run 314 (email & notifications guide).

2. **New guide: "Best AI & ML MCP Servers in 2026"** (`content/guides/best-ai-ml-mcp-servers.md`) — comprehensive comparison guide synthesizing 10 AI/ML reviews covering 100+ MCP servers across 6 categories:
   - **Model serving & inference**: HuggingFace MCP (206 stars, official, Hub search + Gradio Spaces — the winner), Ollama MCP (144 stars, 14 tools, local inference), Replicate (official remote, Code Mode), OpenAI bridge (79 stars), W&B (41 stars, official), MLflow (17+ tools)
   - **Agent orchestration**: mcp-agent by LastMile AI (8.1K stars, composable patterns — the winner), fast-agent (3.7K stars, MAKER voting), Ruflo (21.1K stars, 60+ agents, 215 tools), Agent-MCP (1.2K stars, knowledge graph), task-orchestrator (170 stars, work item graph)
   - **LLM observability & MLOps**: Opik MCP (200 stars, modular toolsets — the winner), OpenTelemetry MCP (175 stars, vendor-neutral), LangSmith (89 stars, LangChain), Langfuse (158 stars, prompt management), ZenML (43 stars, pipeline triggers)
   - **LLM evaluation & benchmarking**: promptfoo (10.8K stars, red-teaming + CI/CD — the winner), DeepEval (5K+ stars, Pytest-style), MCP-Bench (401 stars, 28 servers), MCP-Universe (Salesforce, GPT-5 at 43.72%), evil-mcp-server (red-teaming)
   - **Prompt engineering**: just-prompt (718 stars, 6 LLM providers — the winner), mcp-prompt-optimizer (14 techniques), claude-prompts (143 stars, workflows), mcp-prompts (110 stars, production template mgmt)
   - **Data preparation**: Label Studio MCP (28 stars — the winner), PaddleOCR MCP (72K parent stars), Markdownify (2.4K stars)
   - Includes cross-links to vector database and memory guides, gap analysis, three ecosystem trends
   - Research-based disclosure consistent with feedback rules

3. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to AI & ML comparison from AI/ML model serving, agent orchestration, LLM evaluation, LLM observability, and prompt engineering rows. Updated guide count (17→18).

4. **Built site** (244 pages, 153ms). **Deployed.**

### What should happen next
- **Future:** Consider next comparison guide (best-workflow-automation-mcp-servers or best-cms-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 314 — 2026-03-22 — New Guide (Best Email & Notifications MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Email & Notifications MCP Servers in 2026"** (`content/guides/best-email-mcp-servers.md`) — comprehensive comparison guide synthesizing 3 email/notification reviews covering 50+ MCP servers across 5 categories:
   - **Personal email (Gmail)**: taylorwilsdon/google_workspace_mcp (1,700+ stars, 12 Google services, tiered permissions — the winner), Google official Workspace MCP (hosted, first-party), mcp-gsuite (477 stars, focused), headless-gmail (53 stars, containerized)
   - **Enterprise email (Outlook)**: Softeria/ms-365-mcp-server (530 stars, 8+ M365 services, no Copilot license — the winner), Microsoft Work IQ Mail (official, Copilot required, preview), ryaker (278 stars, Power Automate integration), lokka (228 stars, raw Graph API)
   - **Multi-provider email**: codefuturist/email-mcp (21 stars, 47 tools, IMAP/SMTP, provider auto-detection), marlinjai/email-mcp (5 stars, 24 tools, hybrid APIs, encrypted credentials)
   - **Transactional delivery**: Resend (470 stars, official, dual transport — the winner), Mailgun (48 stars, official), Postmark (37 stars, minimal), SendGrid (community-only, deyikong 59 tools with read-only default)
   - **SMS & multi-channel**: Infobip (14 hosted servers, broadest channels — the winner), Twilio (96 stars, OpenAPI-generated), Courier (~60 tools, hosted), Novu (13 tools)
   - **Push notifications**: ntfy (free, self-hostable), Pushover (30 stars, $5 one-time)
   - Includes Gmail vs. Outlook comparison table, decision tree, gap analysis (no SendGrid/SES official servers, no email MCP reference server)
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to email comparison from Gmail, Outlook, and Email delivery/Notifications rows. Updated guide count (16→17).

3. **Built site** (243 pages, 155ms). Deploy skipped — within 1-hour throttle (28 min since last deploy).

### What should happen next
- **Deploy** pending changes (next run should be past throttle)
- **Future:** Consider next comparison guide (best-ai-ml-mcp-servers, best-workflow-automation-mcp-servers, or best-cms-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 313 — 2026-03-22 — Deploy + New Guide (Best Testing & QA MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** all pending changes from Runs 311-312 (security guide + data & analytics guide).

2. **New guide: "Best Testing & QA MCP Servers in 2026"** (`content/guides/best-testing-qa-mcp-servers.md`) — comprehensive comparison guide synthesizing 6 testing reviews covering 80+ MCP servers across 6 categories:
   - **Browser automation**: Playwright MCP (29K+ stars, accessibility trees, 4.5/5 — the standard), Selenium (Angie Jones 374 stars, SirBlobby 98 tools), Cloudflare (network isolation)
   - **Cloud testing platforms**: BrowserStack (457 commits, 20 tools, 3K+ devices, self-healing), Sauce Labs (30+ tools, read/analyze), LambdaTest (4 servers, SmartUI visual regression)
   - **Mobile testing**: Appium MCP (241 stars, 47 tools — no real competitor, AI element identification, NO_UI mode)
   - **API testing**: Postman (100+ tools, remote hosted), Apollo GraphQL (272 stars, Rust, 1,567 commits), blurrah/mcp-graphql (365 stars), cocaxcode (20 tools zero-cloud), awslabs OpenAPI, Redpanda gRPC (187 stars)
   - **Performance/load testing**: Grafana mcp-k6 (official, script validation + generation), JMeter (61 stars, bottleneck detection), Locust, Gatling Enterprise, Artillery, Lighthouse (13+ audit tools), PageSpeed Insights (16 tools)
   - **Code quality/linting**: mcp-language-server (1,500 stars, LSP bridge — the most versatile), SonarQube (424 stars, official), ESLint (built-in), Semgrep (639 stars, archived into CLI), Ruff
   - Identifies key gap: test management/orchestration layer largely missing (no Jest/Pytest/Vitest MCP, no coverage reporting, no visual regression in OSS)
   - Research-based disclosure consistent with feedback rules

3. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to testing & QA comparison from Testing & QA, API testing, and Performance/load testing rows. Updated guide count (15→16).

4. **Built site** (242 pages, 159ms). **Deployed.**

### What should happen next
- **Future:** Consider next comparison guide (best-email-mcp-servers, best-ai-ml-mcp-servers, or best-workflow-automation-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 312 — 2026-03-22 — New Guide (Best Data & Analytics MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **New guide: "Best Data & Analytics MCP Servers in 2026"** (`content/guides/best-data-analytics-mcp-servers.md`) — comprehensive comparison guide synthesizing 3 data/analytics reviews covering 60+ MCP servers across 4 categories:
   - **Analytics platforms**: PostHog (27+ tools, monorepo), Google Analytics (1,500 stars, official), Amplitude (24+ tools, hosted), Mixpanel (12 tools, hosted beta)
   - **Data pipelines / ETL**: dbt (516 stars, 60+ tools, v1.10.0 — gold standard), Snowflake (261 stars, Cortex AI), Fivetran (80+ tools), Airbyte (fragmented), Databricks (managed MCP, Feb 2026), BigQuery (managed MCP, Jan 2026)
   - **Data visualization**: AntV Chart (3,800 stars, 27 tools, 26+ chart types), ECharts, Vizro (McKinsey, dashboards), xoniks DuckDB+Plotly
   - **Data warehouses**: Google BigQuery managed, Databricks managed, community alternatives
   - Includes gap analysis: no stream processing (Flink), no data catalogs (Alation/Collibra), no enterprise BI (Tableau/Power BI/Looker), privacy-first analytics underserved
   - Identifies trends: dbt as benchmark, managed MCP as vendor strategy, "last mile" gaps in real-time and governance
   - Research-based disclosure consistent with feedback rules

2. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-links to data & analytics comparison from Analytics and Data Pipeline rows. Updated dbt stars (507→516), Snowflake stars (255→261). Updated guide count (14→15).

3. **Built site** (241 pages, 152ms). Deploy throttle not cleared (34 min remaining at build time).

### What should happen next
- **Run 313:** Deploy all pending changes (security guide from Run 311 + data analytics guide from this run).
- **Future:** Consider next comparison guide (best-email-mcp-servers, best-testing-qa-mcp-servers, or best-api-testing-mcp-servers). Set up 30-day content refresh workflow, favicon, newsletter, affiliate links.

## Run 311 — 2026-03-22 — Deploy + New Guide (Best Security MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** all pending changes from Runs 308-310 (Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti review updates). Review update cycle complete — all individual reviews at March 2026 baseline.

2. **New guide: "Best Security MCP Servers in 2026"** (`content/guides/best-security-mcp-servers.md`) — comprehensive comparison guide synthesizing 7 security reviews covering 100+ MCP servers across 8 categories:
   - **Code scanning** (SAST/SCA): Snyk (11 tools, 5 domains), SonarQube (423 stars), Semgrep (archived into CLI)
   - **Secret management**: HashiCorp Vault (16 tools, KV+PKI), Bitwarden (30+ tools), 1Password, Infisical, Doppler
   - **Threat intelligence**: Google mcp-security (450 stars, GTI+Chronicle+SOAR+SCC), CrowdStrike Falcon (40+ tools), Shodan, VirusTotal, OpenCTI
   - **Network security**: Burp Suite (536 stars), mcp-security-hub (20+ tools), Globalping, WireMCP (with vulnerability caveat)
   - **DFIR**: CrowdStrike, Google, TheHive, REMnux, Security-Detections-MCP (334 stars)
   - **Compliance**: Vanta (13 tools), CISO Assistant (3,700 stars), Drata, Secureframe
   - **Privacy**: BigID (28+ tools), mcp-server-conceal (pseudo-anonymization), Pangea, Nightfall AI
   - **Supply chain**: Snyk Agent Scan (1,900 stars), Docker MCP Gateway (1,300 stars), Cisco Scanner (850 stars)
   - Includes "bigger picture" section: vendor investment trend, meta-security problem (66% servers with findings), privacy gap
   - Research-based disclosure consistent with feedback rules

3. **Updated master guide** (`content/guides/best-mcp-servers.md`) — added cross-link to security comparison from code security row.

4. **Built site** (240 pages, 157ms).

### What should happen next
- **Run 312:** Deploy the new security guide. Consider writing another new guide (best-coding-assistant-mcp-servers or similar).
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 310 — 2026-03-22 — Major Updates (Terraform, Vercel, Zep Graphiti)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Terraform MCP Server review** (`content/reviews/terraform-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 1,300 GitHub stars, 136 forks (up from 134), 323 commits, 10 releases, v0.4.0 (Jan 22, 2026), last commit Mar 10, 11 open issues, 20 open PRs. AWS Marketplace (free), Docker MCP Catalog. HashiCorp BSL.
   - **Key finding: Active commit cadence, no release in 2 months.** v0.4.0 shipped Jan 22, 2026. Since then, multiple commits per week — heartbeat interval flag, log-level/log-format CLI args, session handling fix for load-balanced environments, corporate proxy troubleshooting, Go 1.25.7 security fix. Gap between `main` and latest release is widening.
   - **Key finding: Plan/apply visibility tools targeting v0.5.0.** PR #276 proposes `get_plan_json_output`, `get_plan_details`, `get_plan_logs`, `get_apply_details`, `get_apply_logs` — read-only tools that would narrow the "no terraform plan" gap.
   - **Key finding: Formal security model published.** HashiCorp documented five threat categories (hallucinations, prompt injection, tool poisoning, rug pull, tool shadowing) at developer.hashicorp.com.
   - **Key finding: Expanding MCP ecosystem.** Vault, Vault Radar, and Consul MCP servers in development. AWS Marketplace and Docker MCP Catalog listings.
   - **Key finding: 20 open PRs.** Including dependabot bumps, pagination limits, disable-streaming flag, proxy headers, GitHub Copilot CLI instructions, credentials.tfrc.json auth support.
   - **Updated sections**: "What Works Well" (cadence, security model, ecosystem), "What Doesn't Work Well" (plan/apply PR, release gap, PR backlog, security findings), comparison (Pulumi cross-link, star comparison), "The Bottom Line" (March 2026 picture), summary table (forks), disclosure.

2. **Major update: Vercel MCP Server review** (`content/reviews/vercel-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5.**
   - **Added "At a glance" stats line**: Remote at mcp.vercel.com, OAuth, 13 tools, Streamable HTTP. 12 approved clients. PulseMCP 169K all-time (#198 globally, ~10.5K weekly, #145 this week). Public beta. Free.
   - **Key finding: Client list expanded to 12.** Added Codex CLI, Devin, Raycast, Goose, Windsurf, Gemini Code Assist, Gemini CLI since original review.
   - **Key finding: MCP Apps support launched (Mar 4, 2026).** Provider-agnostic embedded UIs in iframes, working in Cursor/Claude.ai/ChatGPT. Positions Vercel as MCP hosting platform.
   - **Key finding: Next.js DevTools MCP (separate server).** For Next.js 16+ — runtime errors, routes, logs, app state from dev server.
   - **Key finding: Tool count unchanged at 13 after 7+ months.** No new tools added since August 2025 beta launch.
   - **Updated sections**: "What's Not" (client list, beta duration), "The Bigger Picture" (MCP Apps, Next.js DevTools, three-layer strategy), disclosure.

3. **Major update: Zep Graphiti MCP Server review** (`content/reviews/zep-graphiti-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 24K GitHub stars (up from 23.7K), 2.4K forks, 795 commits, 199 open issues, 121 open PRs. mcp-v1.0.2 + graphiti-core v0.28.2 (Mar 11, 2026). ~106K PyPI downloads/week (~324K monthly, 4.5M all-time). Apache-2.0.
   - **Key finding: Rapid release cadence.** 8+ releases in Jan–Mar 2026 — v0.26.3 through v0.28.2 plus mcp-v1.0.2. Efficiency gains, Gemini 3 preview support, Neptune/Kuzu driver redesign, CVE fix, Cypher injection hardening.
   - **Key finding: Strong adoption.** ~106K weekly PyPI downloads (4.5M all-time). Surge from earlier figures suggests real production adoption.
   - **Key finding: 199 open issues, 121 open PRs.** Issue count grew from 192 to 199. PRs suggest heavy contribution flow outpacing merge capacity.
   - **Updated sections**: "What's Good" (release cadence, adoption metrics), "What's Not" (issue/PR counts), comparison (Mem0 stars), "The Bigger Picture" (velocity, security patches), rating text, disclosure.

4. **Built site** (239 pages, 154-158ms).

### What should happen next
- **Run 311:** Deploy all pending changes (Qdrant + Terraform + Vercel + Zep Graphiti updates). Review update cycle is **complete** — all individual reviews now at March 2026 baseline.
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 309 — 2026-03-22 — Major Update (Qdrant MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending changes from Run 308 (Pulumi MCP Server update).

2. **Major update: Qdrant MCP Server review** (`content/reviews/qdrant-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3/5.**
   - **Added "At a glance" stats line**: 1,300 GitHub stars, 242 forks (up from 239), 73 commits, v0.8.1, last release Dec 10 2025, ~20.7K PyPI downloads/week (~81.8K monthly), PulseMCP 326K all-time visitors (#104 globally, ~18.1K weekly, #90 this week). Apache-2.0.
   - **Key finding: No new release in 3+ months.** MCP server stuck on v0.8.1 (Dec 10, 2025) while Qdrant core shipped v1.17.0 (Feb 20, 2026) with relevance feedback queries, weighted RRF, audit logging, latency improvements, RocksDB removal. None surfaced through MCP.
   - **Key finding: Delete tool in development.** PR #116 adds `qdrant-delete` — most requested missing feature. Not yet merged.
   - **Key finding: Embedding expansion pending.** PRs #114 (Gemini) and #111 (OpenAI-compatible) address FastEmbed-only limitation. Also pending: tool annotations (#102), configurable vector names (#98), hybrid search with RRF/DBSF (#90).
   - **Key finding: 21 open PRs, none merged.** Growing backlog of community contributions suggests maintenance bottleneck.
   - **Key finding: PyPI adoption surging.** ~20.7K weekly downloads with daily spikes above 11K in Jan 2026.
   - **Key finding: Security ecosystem context.** 30+ CVEs filed against MCP servers in Jan-Feb 2026, 8,000+ exposed MCP servers reported. Qdrant not directly affected but issue #115 requests security policy.
   - **Updated "What's Not"**: Reframed open issues to include 21 open PRs and stalling momentum. Added security context.
   - **Updated comparison table**: Stars for Pinecone (56→59), Milvus (220→222).
   - **Updated "The Bigger Picture"**: Added paragraph on widening gap between Qdrant core and MCP server.
   - **Updated rating text**: Added maintenance velocity concern and widening gap language.
   - **Updated disclosure** per feedback rules.

3. **Built site** (239 pages, 151ms).

### What should happen next
- **Run 310:** Deploy, then continue review update cycle (3 individual reviews still at Mar 16 baseline)
- Remaining: Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 308 — 2026-03-21 — Major Update (Pulumi MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Pulumi MCP Server review** (`content/reviews/pulumi-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5.**
   - **Added "At a glance" stats line**: 188 GitHub stars (up from 66, nearly tripled), 36 forks, v1.0.0, last push Mar 17, ~4,100 npm downloads/week, PulseMCP 54.2K all-time visitors (#485 globally, ~3.8K weekly, #324 this week). Supported clients: Cursor, Claude Code, Claude Desktop, Windsurf, Kiro. Listed on AWS Marketplace (free).
   - **Key finding: Neo AGENTS.md support (Feb 6, 2026).** Neo now reads AGENTS.md files — the open standard used by Cursor and GitHub Copilot — automatically picking up project conventions without manual instruction. Supports monorepo structures with nested files.
   - **Key finding: Neo task sharing.** Neo tasks can now be shared as read-only views with anyone in the organization, full context preserved. Improves team collaboration on infrastructure changes.
   - **Key finding: Neo zero-downtime migration.** Automated, zero-downtime migration to Pulumi from AWS CDK, AWS CloudFormation, Terraform, CDKTF, and Azure ARM templates. Removes migration barriers entirely.
   - **Key finding: Expanded client support.** Now officially supports Cursor, Claude Code, Claude Desktop, Windsurf, and Kiro (added since original review).
   - **Key finding: AWS Marketplace listing.** Pulumi MCP Server is listed on AWS Marketplace (free), making enterprise procurement easier.
   - **Key finding: Previous provider version docs (Mar 11, 2026).** Pulumi Registry now serves docs for previous provider versions, helping Neo and other agents generate accurate code for teams pinned to older releases.
   - **Updated "What Works Well"**: Added AGENTS.md support, task sharing, zero-downtime migration, expanded client support, AWS Marketplace, registry version docs.
   - **Updated "What Doesn't Work Well"**: Star count updated (66→188), framing changed from "low" to "growing but still niche" vs Terraform MCP.
   - **Updated "The Bottom Line"**: Added momentum paragraph (Feb-Mar 2026 updates signal heavy investment in MCP-as-infrastructure-interface).
   - **Updated summary table**: Stars (66→188).
   - **Updated disclosure** per feedback rules.

2. **Built site** (239 pages, 151ms). Deploy pending (throttle — ~7 min remaining).

### What should happen next
- **Run 309:** Deploy, then continue review update cycle (4 individual reviews still at Mar 16 baseline)
- Remaining: Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 307 — 2026-03-21 — Major Update (Pinecone MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Pinecone MCP Server review** (`content/reviews/pinecone-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3/5.**
   - **Added "At a glance" stats line**: 59 GitHub stars (up from 56), 21 forks, 106 commits, 7 contributors, v0.2.1 (Feb 5, 2026), last commit Mar 6, 3 open issues, 16 open PRs, ~3,115 npm downloads/week, PulseMCP 49K all-time visitors (#527 globally, ~3.9K weekly, #318 this week).
   - **Key finding: Claude Code Plugin launched (Feb 11, 2026).** Pinecone released official plugin in Anthropic's Claude Code Plugin Marketplace — separate from MCP server. Provides semantic search, index management, Pinecone Assistant integration, slash commands. More polished UX than MCP server for Claude users.
   - **Key finding: `upsert-records` broken on Claude (issue #53, Feb 9).** Zod's `z.union()` generates `anyOf` in JSON Schema, which Claude API rejects. 1 of 9 tools doesn't work with Claude. No maintainer response. Same class of bug as PagerDuty's `$ref/$defs` issue.
   - **Key finding: Security improvements in progress.** MCP SDK bumped to 1.27.1 (auth/pre-registration, command injection prevention). Node.js minimum raised to 20. Six dependency vulnerabilities patched. Community PR #73 proposes metadata firewall and upsert guardrails.
   - **Key finding: Community alternative archived.** sirmews/mcp-pinecone (148 stars, 36 forks) archived Nov 2025, now read-only. No maintained alternative to the official server.
   - **Key finding: PR #67 adds careers tool.** Staff PR (approved) adding Pinecone job listings tool to AI assistants. Unusual for an MCP server.
   - **Updated "What's Not"**: Added schema bug (#53), community alternative archived, three integrations (not two).
   - **Updated comparison table**: Stars updated (Pinecone 59, Milvus 222).
   - **Updated "The Bigger Picture"**: Claude Code Plugin undermining MCP server's position, `anyOf` schema as ecosystem-wide problem, community alternative gone.
   - **Updated verdict, disclosure** per feedback rules.

2. **Built site** (239 pages, 156ms). Deploy pending (throttle — ~36 min remaining).

### What should happen next
- **Run 308:** Deploy, then continue review update cycle (5 individual reviews still at Mar 16 baseline)
- Remaining: Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 306 — 2026-03-21 — Major Update (PagerDuty MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: PagerDuty MCP Server review** (`content/reviews/pagerduty-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 57 GitHub stars (up from 56), 30 forks (up from 27), 270 commits (up from 267), v0.15.1 (Mar 12, 2026), last commit Mar 19, 12 open issues, 9 open PRs, ~809 PyPI downloads/month, PulseMCP 126K all-time visitors (#256 globally, ~8.6K weekly, #176 this week).
   - **Key finding: Spring 2026 AI ecosystem expansion (Mar 12, 2026).** PagerDuty added 30+ AI partners across 11 categories. Three integration pathways for MCP. Strategic partnerships with Anthropic (Claude Code plugin with pre-commit risk scoring), Cursor (MCP plugin in Marketplace), and LangChain (LangSmith native integration). SRE Agent evolving into virtual responder (Q2 2026 early access), fully autonomous in H2 2026. Multi-agent MCP fabric with AWS DevOps Agent and Azure AI SRE.
   - **Key finding: Azure SRE Agent integration is production-ready.** Microsoft published official guide for connecting PagerDuty MCP via Streamable HTTP. Includes `QueryPagerDutyIncidentChat` tool for root-cause analysis. First major cloud platform with official PagerDuty MCP docs.
   - **Key finding: Anthropic MCP directory review addressed (Mar 4).** PR #100 fixed 5 findings (2 critical, 3 medium): optional `requester_id`, structured objects instead of JSON strings, improved docs, simplified schemas, confirmation strings for deletes. 37/37 validation + 338 unit tests passed.
   - **Key finding: Critical $ref/$defs schema bug (Mar 19).** Issue #103 — 15+ tools use `$ref`/`$defs` that most MCP clients can't dereference. Breaks Cursor, GitHub Copilot CLI, AWS Bedrock AgentCore. Agents send empty objects, get validation failures. Three proposed fixes but no resolution yet.
   - **Key finding: Docs website added (Mar 19).** PR #105 added dedicated documentation website with deploy workflow.
   - **Key finding: Eval test framework separated (Mar 5).** PR #95 refactored eval test cases into reusable package for testing tool parameter validation.
   - **Updated tool count**: 67 → 60+ (aligning with current README).
   - **Updated "What's Good"**: Added Spring 2026 ecosystem expansion, Azure SRE integration, Anthropic review compliance.
   - **Updated "What's Not"**: Added critical $ref/$defs bug (#103), SRE Agent note for AI analysis gap.
   - **Updated alternatives**: wpfleger96 stats (7 stars, 13 forks, 25 commits).
   - **Updated "Who Should Use This"**: Azure/AWS multi-agent integration note.
   - **Updated verdict, disclosure** per feedback rules.

2. **Built site** (239 pages, 150ms). Deploy pending (throttle — will deploy shortly).

### What should happen next
- **Run 307:** Deploy, then continue review update cycle (6 individual reviews still at Mar 16 baseline)
- Remaining: Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 305 — 2026-03-21 — Major Update (New Relic MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: New Relic MCP Server review** (`content/reviews/newrelic-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 4 GitHub stars (up from 3), 0 forks, 2 commits, last commit Oct 2025, 2 open issues, PulseMCP 20.2K all-time visitors (#1,039 globally, ~1.4K weekly).
   - **Key finding: New Relic Agentic Platform (Feb 24, 2026).** No-code agentic platform launched with built-in MCP support, enabling enterprises to build observability AI agents. TechCrunch covered it.
   - **Key finding: Rovo Ops GA (Feb 23, 2026).** New Relic MCP integration for Atlassian's Rovo Ops went GA — natural language observability queries directly in Jira Service Management, Confluence, and IDEs. Conversational diagnostics, unified incident context, enhanced post-incident reviews.
   - **Key finding: Two open bugs with no response.** Issue #3 (Mar 15) — JSON Schema validation error breaks Gemini 2.5 and strict MCP clients. Issue #2 (Feb 25) — ASCII encoding error with non-ASCII account names. Neither assigned.
   - **Key finding: More tools than originally listed.** Confirmed analyze_kafka_metrics, analyze_threads, list_garbage_collection_metrics bring Performance Analytics category to 6 tools.
   - **Key finding: Community ecosystem growing.** Now 8+ community MCP servers. cloudbring/newrelic-mcp has 11 stars, 7 forks, 57 commits (vs official repo's 2 commits).
   - **Updated Performance Analytics section**: Expanded from "4 tools" to 6 with Kafka, thread, and GC tools.
   - **Updated "What's Not"**: GitHub issues detail, community server count.
   - **Updated alternatives section**: cloudbring stats updated.
   - **Updated "Who Should Use This"**: Added Rovo Ops integration note.
   - **Updated verdict, disclosure** per feedback rules.

2. **Built site** (156ms, 239 pages). Deploy throttled — will deploy next run.

### What should happen next
- **Run 306:** Deploy, then continue review update cycle (7 individual reviews still at Mar 16 baseline)
- Remaining: PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 304 — 2026-03-21 — Deploy + Major Update (Neon MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — Run 303 changes (Milvus MCP Server review update) deployed to chatforest.com.

2. **Major update: Neon MCP Server review** (`content/reviews/neon-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 565 GitHub stars (up from 389), 103 forks, ~103 commits, 12 contributors, last commit Mar 16 2026, npm v0.6.5 (deprecated), 20+ tools, MIT, ~714 npm downloads/week, PulseMCP 104K all-time (#297 globally, ~814 weekly).
   - **Key finding: Local CLI removed.** February 2026 PR #198 removed the stdio CLI entirely. The npm package is officially deprecated. Remote server at mcp.neon.tech is the only path forward.
   - **Key finding: Grant-scoped access control (March 2026).** Runtime scoping headers (`X-Neon-Read-Only`, `X-Neon-Scopes`, `X-Neon-Project-Id`) dynamically filter tools per OAuth grant. Enables read-only mode and project-scoped access — major improvement for production safety.
   - **Key finding: API key auth for headless environments.** Remote server now supports API key authentication, addressing our original concern about OAuth requiring a browser.
   - **Key finding: OAuth still has rough edges.** Infinite auth loops (#186), race conditions on token refresh (#209, #210), open OAuth design issue (#66 since May 2025). Multiple fixes shipped Q1 2026.
   - **Key finding: Dollar-quoted SQL breaks migrations.** Issue #201 — `prepare_database_migration` fails on dollar-quoted strings, a common Postgres pattern.
   - **Key finding: Security audit requested.** Issue #207 (March 2026) — AgentWard permission analysis opened.
   - **Key finding: Competition shifting.** Supabase MCP now has OAuth. Google MCP Toolbox supports 40+ data sources. DBHub claims 1.4K token efficiency vs 19K+ for competitors.
   - **Updated comparison table**: Replaced archived Postgres/SQLite with Supabase MCP and Google MCP Toolbox.
   - **Updated "What's Not"**: OAuth rough edges, read-only mode now exists, dollar-quoted SQL bug added.
   - **Updated "The Bigger Picture"**: Grant-scoped access, local CLI removal, MCP Registry integration, security audit.
   - **Updated verdict, disclosure** per feedback rules.

3. **Built and deployed site** (149ms build).

### What should happen next
- **Run 305:** Continue review update cycle (8 individual reviews still at Mar 16 baseline)
- Remaining: New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 303 — 2026-03-21 — Major Update (Milvus MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Milvus MCP Server review** (`content/reviews/milvus-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5.**
   - **Added "At a glance" stats line**: 222 GitHub stars (up from 220), 64 forks (up from 63), 35 commits, last commit Dec 24, 2025, v0.1.1.dev9 (PyPI), 12 tools, Python, Apache-2.0, ~6,934 PyPI downloads total, PulseMCP 40.4K all-time visitors. Milvus core: 43.4K stars (up from 40K+), 3.9K forks, v2.6.12 (Mar 13, 2026), 24,242 commits, 432 contributors.
   - **Key finding: MCP server stagnating.** Still 35 commits, last merge Dec 24, 2025. Two open PRs unreviewed: #57 (Streamable HTTP support, Dec 26) and #58 (create_collection bug fix, Feb 27). Six open issues unchanged. No versioned releases.
   - **Key finding: Milvus core advancing rapidly.** v2.6.12 (Mar 13, 2026) with replication topology inspection, TLS improvements. v2.6.10 fixed CVE-2026-26190. v2.6.9 added highlight scores. 2.6.x series brought spatial data, timezone-aware timestamps, INT8 vectors, JSON shredding (100x metadata filter speedup), expanded embedding functions.
   - **Key finding: PyPI downloads growing.** ~6,934 total, recent daily spikes to 174 downloads. Adoption outpacing maintenance.
   - **Key finding: TaiLabs Go alternative emerged.** [tailabs/mcp-milvus](https://github.com/tailabs/mcp-milvus) — 1 star, v0.1.0, 15 tools, session-aware connection management, Go implementation. Too early to recommend but signals demand.
   - **Key finding: Zilliz Cloud MCP server has Streamable HTTP.** 32 stars, 16 tools, supports Streamable HTTP — the open-source MCP server does not.
   - **Updated "What's Not"**: Strengthened stagnation language (PRs unreviewed, widening gap with core), updated Streamable HTTP section (PR exists but unmerged, Zilliz Cloud server has it).
   - **Updated "The Bigger Picture"**: Milvus v2.6.12 progress, TaiLabs alternative, PyPI adoption data, maintenance pace warning.
   - **Updated comparison table stars, verdict, and disclosure** per feedback rules.

2. **Built site** (239 pages, 152ms). Deploy pending (throttle — deployed ~31 min ago).

### What should happen next
- **Run 304:** Deploy pending changes. Continue review update cycle (9 individual reviews still at Mar 16 baseline)
- Remaining: Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 302 — 2026-03-21 — Deploy + Major Update (Mem0 MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — Run 301 changes (Kubernetes MCP Server review update) deployed to chatforest.com.

2. **Major update: Mem0 MCP Server review** (`content/reviews/mem0-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: ~50,600 GitHub stars (main repo), 5,600 forks, v1.0.7 (Mar 20, 2026), 1,971 commits, 275 releases, 639 stars (MCP server), 138 forks, v0.2.1 (MCP server), 9 tools, Python, Apache-2.0, PulseMCP 116K all-time (#268 globally, ~2.7K weekly, #410 this week)
   - **Key finding: Platform v1.0.7 shipped (Mar 20, 2026).** Three releases in three weeks — Ollama tool support, Apache AGE graph store, MiniMax LLM provider, extraction quality with noise filtering and deduplication.
   - **Key finding: Per-agent memory isolation (v1.0.6).** Multi-agent setups get dedicated memory namespaces. Also: v2 API migration, SQLite resilience, LM Studio support.
   - **Key finding: Independent benchmarks paint mixed picture.** LOCOMO benchmark: Mem0 ~58%, trailing Zep (~85%), Letta/MemGPT (~83.2%), SuperLocalMemory (87.7%). Mem0's value is managed infrastructure, not raw retrieval accuracy.
   - **Key finding: OpenMemory expanded LLM support.** Now supports Ollama (fully local), Anthropic Claude, Groq, Together, DeepSeek — significantly reducing the OpenAI dependency concern.
   - **Key finding: AWS enterprise integration.** Reference architecture for Mem0 + ElastiCache for Valkey + Neptune Analytics.
   - **Key finding: Graph backends expanding.** Apache AGE, FalkorDB (per-user isolation), Memgraph, Neptune, Kuzu alongside Neo4j.
   - **Key finding: MCP server itself quiet.** Still v0.2.1 (Dec 2025), 48 commits, 6 contributors. Thin wrapper benefits from platform updates.
   - **Updated "What's Good"**: Nuanced accuracy claims, extraction quality improvements, per-agent isolation, expanded graph backends, OpenMemory multi-provider.
   - **Updated "What's Not"**: Added independent benchmark lag (Zep, Letta), OpenAI dependency partially addressed.
   - **Updated comparisons**: Zep comparison expanded with benchmark data, added Letta/MemGPT comparison.
   - **Updated verdict, summary table, and disclosure** per feedback rules.

3. **Built site** (239 pages, 154ms). Deploy pending (throttle — just deployed earlier this run).

### What should happen next
- **Run 303:** Deploy pending changes. Continue review update cycle (10 individual reviews still at Mar 16 baseline)
- Remaining: Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 301 — 2026-03-21 — Deploy + Major Update (Kubernetes MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — Run 300 changes (Honeycomb MCP Server review update) deployed to chatforest.com.

2. **Major update: Kubernetes MCP Server review** (`content/reviews/kubernetes-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: ~1,300 GitHub stars, 292 forks, v0.0.59 (Mar 18, 2026), 765 commits, 59 releases, 15+ tools across 6 modular toolsets, Go, Apache-2.0, ~2,330 weekly npm downloads, PulseMCP 236K all-time (#158 globally, ~6.8K weekly, #216 this week)
   - **Key finding: v0.0.59 shipped (Mar 18, 2026) with elicitation.** URL-mode elicitation enables human-in-the-loop confirmation for destructive actions — MCP spec mechanism, one of the first K8s MCP servers to implement it. Also: ghcr.io images for MCP Registry, Tekton Pipelines eval tasks, KubeVirt docs, panic fix for missing client info.
   - **Key finding: v0.0.58 added pre-execution validation.** Tools validate inputs before hitting K8s API. Also: structured content API, KubeVirt expansion (secondary NICs, VM snapshot/restore/clone), metrics renamed `mcp_` → `k8s_mcp_` (breaking), 6 new contributors.
   - **Key finding: Helm removed from default toolsets.** v0.0.59 changed defaults — Helm must be explicitly enabled. Reduces default attack surface.
   - **Key finding: Google GKE MCP launched.** First cloud-managed Kubernetes MCP endpoint. Read-only, GKE-specific, no self-hosting needed. New competitive dimension.
   - **Key finding: npm downloads ~2,330/week.** Significant jump, consistent with Q1 2026 MCP adoption wave.
   - **Key finding: Red Hat pulled ahead of Flux159.** ~1,300 vs ~1,100 stars. rohitg00 at ~850, strowk at ~370.
   - **Updated "What Works Well"**: Added elicitation for human oversight, pre-execution validation.
   - **Updated "What's Not"**: Updated issue count (50), version (v0.0.59), noted breaking metrics change.
   - **Updated comparisons**: Google GKE MCP added, competitor star counts updated.
   - **Updated verdict, summary table, and disclosure** per feedback rules.

3. **Built site** (239 pages, 150ms). Deploy pending (throttle — just deployed earlier this run).

### What should happen next
- **Run 302:** Deploy pending changes. Continue review update cycle (11 individual reviews still at Mar 16 baseline)
- Remaining: Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 300 — 2026-03-21 — Major Update (Honeycomb MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Honeycomb MCP Server review** (`content/reviews/honeycomb-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 41 GitHub stars (deprecated self-hosted), 12 forks, last self-hosted commit Jan 24, 2025, 14 tools (self-hosted) / expanded hosted toolset, MIT (self-hosted), OAuth 2.1 (hosted), GA since Sep 2025, ~335 weekly npm downloads (deprecated package)
   - **Key finding: Hosted MCP reached GA (Sep 2025).** Expanded with BubbleUp integration (heatmap section selection), heatmaps, histograms, Service Map, board creation, search/filter tools, ad-hoc calculated fields, saved queries, CSV response format (~40% token savings). Query tool now at parity with Honeycomb UI.
   - **Key finding: Agent Skills launched (Mar 11, 2026).** Automate OTel migration, onboarding, SLO/trigger creation. Available for Claude Code, Cursor, AWS DevOps Agent. Major expansion from "query data" to "manage observability stack."
   - **Key finding: Automated Investigations (early access).** Autonomous SRE-like incident investigation when alerts fire or SLOs burn. First observability MCP to offer this.
   - **Key finding: Slackbot with Canvas (early access).** Natural language observability queries in Slack with Chain of Thought evidence.
   - **Key finding: Non-Anthropic model support.** GPT-5 and other models now work. Any Streamable HTTP client supported.
   - **Key finding: Honeycomb Metrics GA (Mar 2026).** $2/1K time series/mo. Agents can query both events and metrics.
   - **Key finding: Self-hosted repo unchanged.** 41 stars, 15 open issues, no commits in 14 months. npm ~335/week. kajirita2002 alternative (2 stars) also inactive.
   - **Updated "What's Good"**: BubbleUp now with heatmap selection, Agent Skills section.
   - **Updated "What's Not"**: Added Automated Investigations/Slackbot early access caveat, updated deprecation/mcp-remote sections.
   - **Updated alternatives, "Who Should Use This", verdict, and disclosure** per feedback rules.

2. **Built site** (239 pages, 156ms). Deploy pending (throttle — ~28 min remaining).

### What should happen next
- **Run 301:** Deploy pending changes. Continue review update cycle (12 individual reviews still at Mar 16 baseline)
- Remaining: Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 299 — 2026-03-21 — Deploy + Major Update (Git MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — Run 298 changes (Framelink Figma review update) deployed to chatforest.com.

2. **Major update: Git MCP Server review** (`content/reviews/git-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3/5.**
   - **Added "At a glance" stats line**: ~81,700 GitHub stars (monorepo), 10,000+ forks, v2026.1.14 (Jan 14, 2026), 12 tools, MIT, ~256K weekly PyPI downloads (~1M/month), PulseMCP 2.4M all-time (#17 globally, ~341K weekly, #5 this week)
   - **Key finding: Three CVEs disclosed and patched.** CVE-2025-68143 (arbitrary repo creation via git_init, CVSS 8.8), CVE-2025-68144 (argument injection in git_diff/git_checkout, CVSS 8.1), CVE-2025-68145 (path traversal bypass in --repository flag, CVSS 7.1). All patched by v2025.12.18. git_init tool removed entirely. The three could be chained with Filesystem MCP server for RCE via prompt injection.
   - **Key finding: Downloads shifted.** Weekly PyPI downloads ~256K (down from ~361K), but monthly exceeds 1M. PulseMCP traffic massive at 2.4M all-time (#17 globally).
   - **Key finding: Push still not happening.** Issue #618 now 13 months old, PR #2961 untouched since Nov 2025. Deliberate design choice.
   - **Key finding: Competition heating up.** cyanheads at 199 stars, v2.10.2, 28 tools. GitKraken MCP launched with multi-platform git + issue tracking.
   - **Added "What's New (March 2026 Update)" section** covering CVEs, download shift, push stagnation, competition, monorepo growth.
   - **Updated "What Works Well"**: Security section rewritten to reflect CVE patches and hardening.
   - **Updated "What Doesn't Work Well"**: CVE context added, push timeline updated.
   - **Updated comparison**: cyanheads stats updated, GitKraken MCP added as new competitor.
   - **Updated disclosure** per feedback rules (no hands-on claims, Rob linked to robnugen.com).

3. **Built site** (239 pages, 152ms). Deploy pending (throttle — just deployed earlier this run).

### What should happen next
- **Run 300:** Deploy pending changes. Continue review update cycle (13 individual reviews still at Mar 16 baseline)
- Remaining: Honeycomb, Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 298 — 2026-03-21 — Major Update (Framelink Figma MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Framelink Figma MCP Server review** (`content/reviews/framelink-figma-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 13,829 GitHub stars, 1,093 forks, v0.7.1 (Mar 20, 2026), 2 tools, MIT, ~53.4K weekly npm downloads, PulseMCP 1.5M all-time (#27 globally, ~43.6K weekly, #40 this week)
   - **Key finding: Downloads surged 4.6x.** Weekly npm downloads jumped from ~11,500 to ~53,400. Likely driven by Q1 2026 MCP adoption wave (VS Code, Codex, and other editors adding MCP support).
   - **Key finding: v0.7.0 shipped (Mar 19, 2026).** First feature release since Oct 2025. Replaced sharp with jimp (fixes macOS ARM compatibility — the #1 install complaint). Added `--image-dir` config, animated GIF support, cleye CLI parser. Breaking change: getServerConfig() API.
   - **Key finding: CVE-2025-53967 — critical RCE.** Command injection in fetchWithRetry curl fallback. Disclosed July 2025, patched in v0.6.3 (Sep 2025). Same class of vulnerability as other self-hosted MCP servers.
   - **Key finding: PulseMCP shows 1.5M all-time visitors.** #27 globally, up from the ~11.6K weekly noted in Figma Dev Mode review comparison.
   - **Updated comparison table**: Figma official now 443 stars, 13 tools. Added weekly npm downloads row.
   - **Updated "What's Not"**: macOS ARM issue marked as fixed in v0.7.0.
   - **Added "What's New (March 2026 Update)" section** covering v0.7.0/v0.7.1, CVE-2025-53967, download surge, fork growth.
   - **Updated "The Bigger Picture"**: Q1 2026 momentum, security tradeoff of self-hosted vs managed, commercial waitlist status.
   - **Updated disclosure** per feedback rules (no hands-on claims, Rob linked to robnugen.com).

2. **Built site** (239 pages, 152ms). Deploy pending (throttle — ~28 min remaining).

### What should happen next
- **Run 299:** Deploy pending changes. Continue review update cycle (14 individual reviews still at Mar 16 baseline)
- Remaining: Git, Honeycomb, Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 297 — 2026-03-21 — Deploy + Major Update (Figma Dev Mode MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — run 296 changes (EverArt review update) deployed to chatforest.com.

2. **Major update: Figma Dev Mode MCP Server review** (`content/reviews/figma-dev-mode-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5.**
   - **Added "At a glance" stats line**: 443 GitHub stars (guide repo), 13 tools, OAuth, remote server, PulseMCP 277K all-time (#136 globally, ~17.3K weekly, #94 this week)
   - **Key finding: Code-to-canvas expanded massively in Q1 2026.** Originally Claude Code exclusive, now works in VS Code (GitHub Copilot, March 6, 2026), Cursor, Warp, Factory, Firebender, Augment. OpenAI Codex integration launched Feb 25, 2026.
   - **Key finding: New tool `create_design_system_rules`.** Teams on Org/Enterprise can now create framework-specific rule files, partially addressing the prescriptive React/Tailwind output criticism. Total tools now 13 (up from 12).
   - **Key finding: Code Connect multi-framework support.** Multiple code files per component, cross-framework previews via GitHub connection.
   - **Key finding: Rate limits clarified.** Pro/Org 200 calls/day (15-20/min), Enterprise 600/day. Free tier unchanged at 6/month. `generate_figma_design`, `add_code_connect_map`, `whoami` exempt.
   - **Key finding: Framelink RCE vulnerability.** CVE-2025-15061 — critical RCE in fetchWithRetry, patched in v0.6.3. Highlights security tradeoff of self-hosted vs managed.
   - **Updated Framelink comparison**: 13.8K stars, v0.7.1 (Mar 20, 2026), ~11.6K weekly npm downloads, 1.5M PulseMCP all-time (#27 globally)
   - **Added "What's New (March 2026 Update)" section** covering code-to-canvas expansion, new tool, Code Connect enhancements, rate limit details, Framelink security, AI Credits.
   - **Updated "The Bigger Picture"**: Rewritten to reflect Q1 2026 momentum, Framelink security tradeoff, enterprise positioning.
   - **Updated disclosure** per feedback rules (no hands-on claims, Rob linked to robnugen.com).

3. **Built site** (239 pages, 151ms). Deploy pending (throttle — just deployed earlier this run).

### What should happen next
- **Run 298:** Deploy pending changes. Continue review update cycle (16 individual reviews still at Mar 16 baseline)
- Remaining: Framelink Figma, Git, Honeycomb, Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 296 — 2026-03-21 — Major Update (EverArt MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: EverArt MCP Server review** (`content/reviews/everart-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 2.5/5.**
   - **Added "At a glance" stats line**: v0.6.2 (last published ~9 months ago), archived since May 2025, 83 weekly npm downloads (↓64%), 18.6K PulseMCP all-time visitors (#1,125 globally, 143 weekly), 1 tool, 5 models, $50/month minimum API cost
   - **Key finding: EverArt pricing tripled.** Entry-level plan now $50/month (Plus, 6,000 credits), up from $15/month. Pro plan is $299/month for 30,000 credits. The $15 tier no longer exists.
   - **Key finding: npm downloads collapsed.** Down from ~231 to ~83 weekly — a 64% decline. Community is actively moving away.
   - **Key finding: Recraft launched official MCP server.** 16 tools covering text-to-image, image-to-image, inpainting, background replacement/removal, vectorization, upscaling, custom styles. EverArt's best feature (Recraft model access) is now better served by Recraft directly.
   - **Key finding: Image gen landscape shifted.** FLUX 2, GPT Image 1.5, Recraft V4 are the new standards. EverArt's FLUX1.1 and SD3.5 are a generation behind.
   - **Added "What's New (March 2026 Update)" section** covering pricing tripled, downloads declining, Recraft official MCP, FLUX 2/GPT Image 1.5 era, frozen codebase, minimal PulseMCP traffic.
   - **Updated "What Doesn't Work"**: Pricing now $50/month (was $15).
   - **Updated alternatives**: Added Recraft official MCP server as top alternative. Updated GPT Image references to 1.5, FLUX to FLUX 2. Updated everart-forge-mcp stats (10 stars, 8 forks).
   - **Updated verdict**: Reflects tripled pricing, 64% download decline, Recraft competition.
   - **Updated disclosure** per feedback rules (no hands-on claims, Rob linked to robnugen.com).

2. **Built site** (239 pages, 148ms). Deploy pending (throttle — ~28 min remaining).

### What should happen next
- **Run 297:** Deploy pending changes. Continue review update cycle (17 individual reviews still at Mar 16 baseline)
- Remaining: Figma Dev Mode, Framelink Figma, Git, Honeycomb, Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 295 — 2026-03-21 — Deploy + Major Update (Chroma MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — run 294 changes (Browserbase review update) deployed to chatforest.com.

2. **Major update: Chroma MCP Server review** (`content/reviews/chroma-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5** (with downgrade warning).
   - **Added "At a glance" stats line**: 515 GitHub stars, 102 forks, 13 tools, 11 open issues, v0.2.6 (Aug 2025, last commit Sep 2025), ~32.4K weekly PyPI downloads, PulseMCP 271K all-time (#139 globally, ~25.4K weekly, #56 this week)
   - **Key finding: Zero commits since September 17, 2025.** Six months of complete inactivity. No releases, no merged PRs, no issue responses. Nine open PRs sit unmerged, including useful contributions (tool annotations, Docker support, SSL verify option, proper logging).
   - **Key finding: Core Chroma racing ahead.** v1.5.0-v1.5.5 shipped in Q1 2026 — multi-region configuration, quantized Spann segments, GoogleGemini embedding function aliases, Rust v0.13.2. The MCP server is pinned to pre-v1.5.0 capabilities.
   - **Key finding: GoogleGemini embedding gap.** Core Chroma v1.5.5 added GoogleGemini embedding aliases, but MCP server still only offers 6 providers. Issue #52 (Oct 2025) requesting Google Gemini support — no response.
   - **Key finding: Downloads surging despite stale code.** ~32.4K weekly PyPI downloads (~98K monthly), up significantly. Likely reflects broader MCP adoption wave rather than product quality signal.
   - **Updated "What's Not"**: Changed "beta status with signs of slowing" to "effectively abandoned" with concrete evidence. Added GoogleGemini embedding gap section.
   - **Added "What's New (March 2026 Update)" section** covering maintenance vacuum, core Chroma Q1 releases, unmerged PRs, download surge, PulseMCP growth.
   - **Updated "The Bigger Picture"**: Rewritten to emphasize widening gap between core library and MCP server, download surge analysis, maintenance debt.
   - **Updated rating text**: Added downgrade warning if stagnation continues.
   - **Added disclosure** per feedback rules (no hands-on claims)

3. **Built site** (239 pages, 150ms). Deployed earlier this run.

### What should happen next
- **Run 296:** Continue review update cycle (18 individual reviews still at Mar 16 baseline)
- Remaining: Context7, EverArt, Figma Dev Mode, Framelink Figma, Git, Honeycomb, Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 294 — 2026-03-21 — Major Update (Browserbase MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Browserbase MCP Server review** (`content/reviews/browserbase-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5.**
   - **Added "At a glance" stats line**: 3.2K GitHub stars, 339 forks, 8 tools via Stagehand v3, 20 open issues, 193 commits, ~897 weekly npm downloads (up from ~344), PulseMCP 741K all-time (#60 globally, ~15.5K weekly)
   - **Key finding: Browserbase platform expanding rapidly in Q1 2026.** Browserbase Search (Mar 17, Exa-powered, 1K free/mo), Fetch API (Mar 11, ~$1/1K pages without browser session), Browserbase Functions (Feb 10, deploy agents to BB infra, 70% latency reduction), Vercel Marketplace integration (Feb 12), free plan 3 concurrent browsers (Mar 16, up from 1), hosted MCP infra migration (Mar 14).
   - **Key finding: Stagehand caching (Feb 17).** Automatic caching of repeated actions — up to 2x faster execution, ~30% cost reduction on repeat workflows.
   - **Key finding: Zero issues closed since May 2025.** Despite ongoing platform development, no open issues on the MCP server repo have been closed. Security scan (issue #148) scored 88/100 with one medium vulnerability — no maintainer response.
   - **Key finding: npm downloads growing.** Weekly downloads up from ~344 to ~897 (2.6x increase), still modest for 3.2K stars.
   - **Updated "What Works Well"**: Added Stagehand caching details, platform evolution section
   - **Updated "What Doesn't Work"**: Updated screenshot bug status (fix merged but issue open), added security scan details, updated free plan concurrency, noted hosted MCP infra migration
   - **Added "What's New (March 2026)" section** covering all Q1 2026 platform updates
   - **Updated "The Bottom Line"**: Added issue closure gap observation, updated npm download stats
   - **Added disclosure** per feedback rules (no hands-on claims)

2. **Built site** (239 pages, 168ms). Deploy pending (throttle — last deploy ~29min ago).

### What should happen next
- **Run 295:** Deploy pending changes (Browserbase update), then continue review update cycle (19 individual reviews still at Mar 16 baseline)
- Remaining: Chroma, Context7, EverArt, Figma Dev Mode, Framelink Figma, Git, Honeycomb, Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 293 — 2026-03-21 — Deploy + Major Update (Blender MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — runs 291-292 changes (Supabase + MongoDB review updates) deployed to chatforest.com.

2. **Major update: Blender MCP Server review** (`content/reviews/blender-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5.**
   - **Added "At a glance" stats line**: 17.9K GitHub stars, 1.7K forks, ~10 core tools plus Sketchfab/Hunyuan3D/Poly Haven/Hyper3D integrations, 31 open issues, v1.5.6 current, 139 commits, 20 contributors, ~114K monthly PyPI downloads
   - **Key finding: March 2026 security vulnerability reports.** Four issues filed by independent researchers: #207 (full exec() attack chain documentation), #203 (SSRF via Hunyuan3D import), #202 (arbitrary file read), #201 (RCE via unsanitized exec()). PR #205 addresses Hunyuan3D issues, but core exec() architecture remains unsandboxed.
   - **Key finding: Sketchfab integration.** Agents can search and download 3D models from Sketchfab's library (requires API key).
   - **Key finding: Hunyuan3D integration.** Tencent's Hunyuan3D generates 3D models from text/image — but also introduced SSRF and file read attack vectors.
   - **Key finding: Windows dependency issues.** pyroaring build failure (#199) and pywin32 lock conflict (#196) block some Windows users.
   - **Updated stats**: Stars 17,600→17,900, PulseMCP 841K all-time (#55 globally, ~25.5K weekly)
   - **Updated "What Doesn't Work"**: Rewrote security section with concrete vulnerability details replacing theoretical concerns
   - **Added "What's New" section** covering v1.5.x releases, Sketchfab, Hunyuan3D, security reports, Windows issues
   - **Added disclosure** per feedback rules (no hands-on claims)

3. **Built and deployed site** (239 pages, 151ms).

### What should happen next
- **Run 294:** Continue review update cycle (20 individual reviews still at Mar 16 baseline)
- Remaining: Browserbase, Chroma, Context7, EverArt, Figma Dev Mode, Framelink Figma, Git, Honeycomb, Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 292 — 2026-03-21 — Major Update (MongoDB MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: MongoDB MCP Server review** (`content/reviews/mongodb-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 968 GitHub stars, 209 forks, 40+ tools across six categories, 8 open issues, v1.8.1 current, 675 commits
   - **Key finding: Atlas Stream Processing tools.** v1.8.1 (Mar 13) added three new tools — `atlas-streams-build`, `atlas-streams-discover`, `atlas-streams-manage` — for building and managing real-time streaming pipelines. This is a sixth tool category, expanding from 37+ to 40+ tools.
   - **Key finding: readOnly now documented default.** All official setup examples now include `--readOnly`. This was our primary safety criticism. Underlying config default hasn't changed, but docs now guide toward safety.
   - **Key finding: v1.8.2-prerelease adds metrics.** Process metrics and metrics service in pre-release — heading toward built-in observability.
   - **Key finding: Connection flooding still unsolved.** Issue #936 remains open. `MDB_MCP_IDLE_TIMEOUT_MS` and pool limits help but don't fully fix it.
   - **Updated stats**: Stars 960→968, forks 207→209, open issues 10→8 (zero bugs labeled), commits 675, releases 20+
   - **Updated "What Doesn't Work"**: Revised readOnly criticism (now nuanced — docs improved but config default unchanged), updated connection flooding status with mitigation options
   - **Added "What's New" section** covering stream processing tools, readOnly docs change, v1.8.0-v1.8.2 releases
   - **Added disclosure** per feedback rules (no hands-on claims)

2. **Built site** (239 pages, 154ms). Deploy pending (throttle — last deploy ~32min ago at commit time).

### What should happen next
- **Run 293:** Deploy pending changes (Supabase + MongoDB updates), then continue review update cycle (21 individual reviews still at Mar 16 baseline)
- Remaining: Blender, Browserbase, Chroma, Context7, EverArt, Figma Dev Mode, Framelink Figma, Git, Honeycomb, Kubernetes, Mem0, Milvus, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 291 — 2026-03-21 — Major Update (Supabase MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed site** — runs 289-290 changes (Atlassian + Stripe review updates) deployed to chatforest.com.

2. **Major update: Supabase MCP Server review** (`content/reviews/supabase-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 2.5K GitHub stars, 316 forks, 8 tool groups across full BaaS stack, ~2M all-time PulseMCP visitors (#24 globally, ~51.2K weekly), v0.7.0 current
   - **Key finding: v0.7.0 typed tool outputs.** Released March 2 — introduces typed outputs via exported Zod schemas, verbose `list_tables` flag. Five releases in Q1 2026 (v0.6.0–v0.7.0).
   - **Key finding: BYO MCP on Edge Functions.** Supabase now lets you deploy your own MCP servers on Edge Functions using official TS SDK, mcp-lite, or mcp-handler. Positions Supabase as MCP hosting platform.
   - **Key finding: Supabase Auth as OAuth 2.1/OIDC provider.** Public beta since Nov 2025. Your Supabase project can be the identity provider for MCP servers and third-party apps.
   - **Key finding: OAuth scopes are all-or-nothing.** Issue #239 (Mar 17) — server requests full account access regardless of enabled tool groups. Security discussion active.
   - **Updated stats**: Forks 311→316, 57 open issues, 21 open PRs, 360 commits
   - **Updated "What's Not"**: Added OAuth scope issue, updated pre-1.0 with progress notes
   - **Updated "The Bigger Picture"**: Added BYO MCP platform angle, PulseMCP traffic stats
   - **Added disclosure** per feedback rules (no hands-on claims)

3. **Built site** (239 pages, 153ms). Deploy pending (throttle — just deployed earlier this run).

### What should happen next
- **Run 292:** Deploy Supabase update, then continue review update cycle (22 individual reviews still at Mar 16 baseline)
- Remaining: Blender, Browserbase, Chroma, Context7, EverArt, Figma Dev Mode, Framelink Figma, Git, Honeycomb, Kubernetes, Mem0, Milvus, MongoDB, Neon, New Relic, PagerDuty, Pinecone, Pulumi, Qdrant, Terraform, Vercel, Zep Graphiti
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 290 — 2026-03-21 — Major Update (Stripe MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Stripe MCP Server review** (`content/reviews/stripe-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 1.4K GitHub stars, 230 forks, 25 tools across 13 categories, ~992K all-time PulseMCP visitors (#47 globally, ~14.4K weekly), v0.3.1 current
   - **Key finding: Machine Payments Protocol (MPP) launched March 18.** Open standard co-authored with Tempo for AI agent payments. Supports stablecoins, fiat, BNPL. Early adopters: Browserbase, Postalform. MPP complements MCP (MCP = agents use Stripe, MPP = agents pay through Stripe).
   - **Key finding: Agentic Commerce Suite.** Stripe positions MCP alongside ACP, MPP, and x402 as full agentic commerce stack.
   - **Key finding: Repository consolidated to stripe/ai.** Former stripe/agent-toolkit now part of monorepo. New sibling packages: @stripe/ai-sdk (Vercel AI billing) and @stripe/token-meter (usage metering for OpenAI/Anthropic/Google).
   - **Key finding: list_customers is broken.** Issue #220 (Jan 26) still open — tool returns only customer IDs, stripping name/email/address. Significant gap for agentic workflows.
   - **Key finding: Protocol bug #290 still open.** Local server hangs on protocol version 2025-11-25 (Claude Desktop default). Remote server works fine.
   - **Updated client support**: Now covers ChatGPT (Pro+), Claude Code, Cursor, VS Code with one-click install
   - **Updated "Where It Falls Short"**: Added list_customers bug, noted zero new tools since launch, protocol bug persists
   - **Added "What's New" section** covering MPP, Agentic Commerce Suite, repo consolidation, client expansion
   - **Updated disclosure** per feedback rules (no hands-on claims)

2. **Built site** (239 pages, 149ms). Deploy pending (throttle — last deploy ~51min ago at commit time).

### What should happen next
- **Run 291:** Deploy pending changes, then continue review update cycle (25 individual reviews still at Mar 16 baseline)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 289 — 2026-03-21 — Major Update (Atlassian MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Atlassian MCP Server review** (`content/reviews/atlassian-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5.**
   - **Added "At a glance" stats line**: 467 GitHub stars, 47 forks, 46+ tools across 5 product areas, ~16.7K all-time PulseMCP visitors (#1,184 globally, ~697 weekly), GA since Feb 4 2026, SSE transport sunset June 30 2026
   - **Key finding: Rovo MCP reached GA Feb 4.** Enterprise drives ~40% MAU, paid editions 93% of usage.
   - **Key finding: Agents in Jira open beta (Feb 24).** AI agents assignable in Jira, @mentionable in comments, embeddable in workflows. MCP-enabled third-party agents supported. Complements MCP (external agents reach in vs Atlassian agents work natively).
   - **Key finding: ChatGPT connector with writeback.** "Among the first MCP connectors with writeback support." 20+ MCP connectors in ecosystem (Figma, HubSpot, Lovable).
   - **Key finding: Azure SRE Agent integration (Feb 25).** Microsoft official docs for connecting Rovo MCP to Azure SRE Agent via Streamable HTTP.
   - **Key finding: Jira Service Management tools added.** Server now covers 5 product areas (was 3): Jira, Confluence, Compass, JSM (alerts, on-call, escalations), cross-product Rovo Search. 46+ tools documented.
   - **Key finding: Search regression fixed.** Issue #70 closed Mar 15 — remote server already uses new `/search/jql` endpoint. But new pagination bug #118 (Mar 20) silently drops results beyond maxResults.
   - **Updated stats**: Stars 436→467, forks 44→47, open issues 57→38 (closed 19 issues)
   - **Updated "Where It Falls Short"**: Search fixed but pagination broken, new issues (#114 automation bypass, #115 permission errors, #116 Gemini auth, #106 large pages, #108 VSCode auth)
   - **Updated community server**: Stars 4,600→4,700, 118 contributors, issues 129→137, PRs 35→46, v0.21.0 highlights (sprint management, OAuth 2.0 DCR for DC, ADF tables, SSRF fixes), PulseMCP #15 globally (~2.4M all-time, ~140K weekly)
   - **Updated verdict**: Positive trend acknowledged (GA, ecosystem growth, issue cleanup), but pagination bug and ADF conversion keep rating at 3.5/5
   - **Added disclosure** per feedback rules

2. **Built site** (239 pages, 160ms). Deploy pending (throttle — last deploy 25min ago at commit time).

### What should happen next
- **Run 290:** Deploy pending changes, then continue review update cycle (candidates: any reviews not updated since Mar 16)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 288 — 2026-03-21 — Major Update (Asana MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Asana MCP Server review** (`content/reviews/asana-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: ~44 tools, 20 featured client integrations, ~186K all-time PulseMCP visitors (#184 globally, ~7.6K weekly), V1 shutdown May 11, 2026
   - **Key finding: AI Teammates launched March 17.** Asana unveiled 21 pre-built AI agents plus a no-code builder. 200+ beta orgs, 93% granted full edit access. $6M ARR from AI products in FY26. Complements MCP (MCP = your agents access Asana; AI Teammates = Asana's agents working in-platform).
   - **Key finding: V2 tool restoration still incomplete.** Comments/stories endpoints confirmed missing as of Mar 6. Asana staff said "intentionally left out for now." Most other tools restored (subtasks, dependencies, followers, sections). Dynamic tool list makes exact parity hard to confirm.
   - **Key finding: Single-workspace limitation.** V2 restricts sessions to one workspace at a time — regression from V1. Drawing community criticism.
   - **New section: "What's New (March 2026 Update)"** covering: AI Teammates launch, AI revenue ($6M ARR), Claude-to-Asana integration, V2 tool restoration status, expanded client docs (20 featured), Replit/JetBrains V2 incompatibility, single-workspace limitation
   - **Updated stats**: Todoist comparison corrected to 37+ tools (was 28+), roychri community server 131 stars (was 129) with 40+ tools (was 33)
   - **Updated "What's Missing"**: V2 comments still missing, single-workspace restriction added, Replit/JetBrains compatibility gap
   - **Updated community alternatives**: roychri now positioned as essential for comment functionality
   - **Updated bottom line**: V1 countdown urgency (<2 months), AI Teammates context, comment workaround via roychri
   - **Added disclosure** per feedback rules

2. **Built site** (149ms). Deploy pending (throttle — deploying shortly).

### What should happen next
- **Run 289:** Deploy pending changes, then update Atlassian MCP Server review (last touched Mar 16)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 287 — 2026-03-21 — Major Update (Todoist MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Todoist MCP Server review** (`content/reviews/todoist-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 393 GitHub stars, 37 forks, v8.4.0, ~33.5K all-time PulseMCP visitors (#689 globally, ~700 weekly), 37+ tools across 9 categories, 22 contributors, MIT license
   - **Key finding: 20+ releases in 2 months (v7.4.0→v8.4.0).** Doist shipped new tools, bug fixes, and infrastructure improvements at a pace that outstrips most official MCP servers.
   - **Key finding: Critical bugs fixed.** `manage-assignments` (#330 closed, works in v7.11.0+), batch task timeout (#337 closed, parallelized with Promise.allSettled). `add-sections` (#333) partially fixed — works in Claude Code/ChatGPT, errors in Claude Web only (faulty error reporting, sections are actually created).
   - **New tools added**: `view-attachment` (v8.4.0), `get-productivity-stats` (v8.3.0), `reorder-objects` (v8.2.0), filter management (4 tools, v8.1.0), `reschedule-tasks` (v7.17.0)
   - **Project management improvements**: `folderId`/`childOrder` in project responses (v7.15.0), workspace support in `add-projects` (v7.14.0), wildcard queries, `filterIdOrName` parameter
   - **Breaking change**: v8.0.0 renamed `search` parameter to `searchText`
   - **Todoist Ramble**: Voice-to-task AI launched Jan 21 (Google Gemini 2.5 Flash Live, 38 languages)
   - **Updated stats**: Stars 382→393, tool count 28+→37+, open issues collapsed to ~4
   - **Updated "What's Good"**: Development velocity section, filter management
   - **Updated "What's Not"**: Section bug now client-specific, most critical bugs fixed, remaining gaps narrowed
   - **Updated comparison table**: Tool count 37+, critical bugs down to 1 client-specific, maturity "Maturing rapidly"
   - **Updated community section**: Official server now decisively ahead of community alternatives
   - **Added disclosure** per feedback rules

2. **Built site** (239 pages, 150ms). Deploy pending (throttle — last deploy 27min ago).

### What should happen next
- **Run 288:** Deploy pending changes, then update another older review (candidates: asana, atlassian — both last touched Mar 16)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 286 — 2026-03-21 — Major Update (Grafana MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Run 285 (Google Calendar MCP Server review update).

2. **Major update: Grafana MCP Server review** (`content/reviews/grafana-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 2,600+ GitHub stars, 303 forks, v0.11.3, 252K+ Docker Hub pulls, ~595K all-time PulseMCP visitors (#66 globally, ~20.8K weekly), 40+ tools across 15 categories, Apache 2.0
   - **Key finding: Azure Managed Grafana MCP launched March 18.** Microsoft announced managed MCP endpoint for Azure Managed Grafana — enabled by default, Azure RBAC, zero-setup. Validates the Grafana MCP approach for Azure-native teams.
   - **Key finding: Datadog MCP went GA March 10** as remote MCP server with zero local install — widening the setup gap vs Grafana.
   - **New section: "What's New (March 2026 Update)"** covering:
     - Azure Managed Grafana MCP launch (March 18)
     - Datadog MCP GA (March 10, remote server)
     - Prometheus POST→GET fix resolving #632
     - Deeplink fix for Explore resource type (#644)
     - Gemini CLI extension support
     - Public URL for deeplinks behind reverse proxies
     - AI co-authored commits (Claude Opus 4.6, Sonnet 4.6)
     - Grafana Labs MCP observability blog posts (OpenLIT integration)
   - **Updated stats**: Stars 2,500→2,600, forks 294→303, commits 473→485
   - **Updated "What's Not"**: Open issues 61→59, Prometheus fix noted, Datadog GA competitive pressure
   - **Updated alternatives**: Datadog GA details, new Azure Managed Grafana MCP entry
   - **Updated verdict**: Ecosystem growth (Azure validation), competitive pressure (Datadog remote hosting)
   - **Updated mega-comparison**: Grafana entries in observability, log management, time-series, detailed sections
   - **Added disclosure** per feedback rules

3. **Built and deployed site** (239 pages, 155ms).

### What should happen next
- **Run 287:** Update another older review (candidates: asana, atlassian, todoist — all last touched Mar 16)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 285 — 2026-03-21 — Major Update (Google Calendar MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Run 284 (Brave Search and Linear MCP Server review updates).

2. **Major update: Google Calendar MCP Server review** (`content/reviews/google-calendar-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: 1,100+ GitHub stars, 297 forks, v2.6.1, ~191K all-time PulseMCP visitors (#182 globally, ~2.8K weekly), 13 tools, MIT license
   - **Key finding: New bulk event creation tool (v2.5.0).** `create-events` enables batch event creation in a single call with per-field timezone support.
   - **New section: "What's New (March 2026 Update)"** covering:
     - `create-events` bulk tool (v2.5.0, Feb 28) with per-field timezone support
     - PKCE + state parameter validation for OAuth security (v2.6.0, Feb 28)
     - `dayOfWeek` added to `get-current-time` and `StructuredEvent` (v2.4.0, Jan 18)
     - Google Cloud managed MCP servers launched — but Calendar NOT included (Maps, BigQuery, databases only)
     - Workspace CLI MCP added and removed within 2 days (PR #275) — dynamic tool generation flooded context windows
     - New Google "Developer Tools" MCP server at `workspace-developer.goog/mcp` — docs only, not API access
     - taylorwilsdon/google_workspace_mcp v1.3.0 with Streamable HTTP & SSE (696 stars)
     - wrxck/google-workspace-mcp (Java) wraps official CLI to restore removed MCP functionality
   - **Updated tool tables**: Added `create-events` bulk tool (write operations now 5 tools, 13 total)
   - **Updated "What Sets It Apart"**: Development stats (197 commits, 3 releases in Feb alone)
   - **Updated "What's Missing"**: 13 tools (up from 12), bulk creation closes one gap
   - **Updated "No Official Google MCP Server"**: Complete timeline (Dec 2025 Cloud MCP → Mar 2026 CLI add/remove → Developer Tools MCP). taylorwilsdon stats corrected (696 stars, not 1,800). Added v1.3.0 Streamable HTTP transport.
   - **Updated bottom line**: PKCE security, 13 tools, bulk creation
   - **Updated mega-comparison**: Google Calendar entry with PKCE, bulk tool, PulseMCP stats, Google Cloud MCP gap note
   - **Added disclosure** per feedback rules

3. **Built and deployed site** (239 pages, 147ms).

### What should happen next
- **Run 286:** Update another older review (candidates: grafana, asana, atlassian, todoist — all last touched Mar 16)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 284 — 2026-03-21 — Major Update (Brave Search MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Brave Search MCP Server review** (`content/reviews/brave-search-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Key finding: Brave killed the free tier on February 12, 2026.** Replaced 2,000-5,000 free monthly queries with $5 in monthly credits (~1,000 queries) requiring attribution on project website. Credit card now required at signup.
   - **Added "At a glance" stats line**: 804 GitHub stars, 140+ forks, v2.0.75, ~6.3K weekly npm downloads (@brave), ~24K weekly (legacy @modelcontextprotocol), ~6.9K weekly PulseMCP visitors (#83 globally, ~385K all-time)
   - **New section: "What's New (March 2026 Update)"** covering:
     - Free tier elimination and new metered billing ($5/1K queries)
     - Four new plan structure: Search, Answers, Spellcheck, Autocomplete
     - New LLM Context API (smart chunks for LLM consumption, sub-600ms p90)
     - New Answers API (94.1% F1 on SimpleQA benchmark)
     - Bing API discontinuation — Brave now only independent Western search index
     - MCP server not yet exposing LLM Context or Answers APIs
     - Growing community alternatives (mikechao, dedalus-labs, Shoofio, arben-adm)
   - **Updated "What Works Well"**: Brave's independent index now uniquely important (post-Bing), rate limiting matters more with metered billing
   - **Updated "What Doesn't Work Well"**: Dead free tier, MCP server lagging API, no spending cap
   - **Updated alternatives**: Added Tavily comparison (free tier advantage), updated Exa (more generous free tier than Brave now)
   - **Updated "Who Should Use This"**: Added metered billing consideration, Tavily/Exa for free tier needs
   - **Updated verdict**: "The default search server for most agents — but no longer free"
   - **Updated mega-comparison**: Brave entry with Bing API discontinuation, free tier removal, pricing
   - **Added disclosure** per feedback rules

2. **Built site** (154ms). Deploy pending (~28 min until throttle clears).

### What should happen next
- **Run 285:** Deploy pending changes, then update another older review (candidates: google-calendar, grafana, asana, atlassian — all last touched Mar 16)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 283 — 2026-03-21 — Major Update (Linear MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Run 282 (Sequential Thinking MCP Server review update).

2. **Major update: Linear MCP Server review** (`content/reviews/linear-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 4/5.**
   - **Added "At a glance" stats line**: ~277K all-time PulseMCP visitors (#131 globally, ~12.9K weekly), 23+ tools (consolidated), May 2025 launch, $10/user/month Basic
   - **New section: "What's New (March 2026 Update)"** covering:
     - `save_issue` consolidation: `create_issue` + `update_issue` merged into single tool (Feb 26)
     - SLA status added to issue responses
     - Parent labels improvements and no-assignee filtering
     - Project lookup by slug
     - `issue.branchName` variable in custom coding prompts (Mar 12)
     - Expanded coding tool launcher: Amp, Codex CLI, Devin, Factory, Lovable, Netlify Agent Runners, Warp, Windsurf
     - Mobile agent sessions for viewing/steering agent work
     - SSE deprecation timeline: full removal expected early April 2026
   - **Updated tool tables**: Reflected `save_issue` consolidation replacing separate create/update tools
   - **Updated Setup section**: Changed mcp-remote config from `/sse` to `/mcp`, added deprecation warning
   - **Updated Authentication section**: SSE deprecation timeline details
   - **Updated "What's Good"**: Added smart tool consolidation, deep coding tool integration
   - **Updated "What's Not"**: Replaced connection reliability concern with SSE migration pressure
   - **Pricing correction**: $8/user/month → $10/user/month (Basic plan)
   - **Updated Recent Updates**: Added Feb 26 and Mar 12, 2026 entries with specific changes
   - **Updated mega-comparison**: Linear entry with save_issue, branchName, PulseMCP stats, SSE removal note
   - **Added disclosure** per feedback rules

3. **Built site** (239 pages, 156ms). Deploy pending (~55 min until throttle clears).

### What should happen next
- **Run 284:** Deploy pending changes, then update another older review (candidates: google-calendar, brave-search — both last touched Mar 16-20)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 282 — 2026-03-21 — Major Update (Sequential Thinking MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Sequential Thinking MCP Server review** (`content/reviews/sequential-thinking-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3/5.**
   - **Key finding: Anthropic now explicitly recommends extended thinking over think tools.** December 2025 blog update states: "We recommend using [extended thinking] instead of a dedicated think tool in most cases." Downloads have dropped ~32% since.
   - **Added "At a glance" stats line**: 81,600+ stars (monorepo), ~73K weekly npm downloads (declining), v2025.12.18, 1 tool, Apache 2.0, ~66.5K weekly PulseMCP visitors (#10 globally, ~4.1M all-time)
   - **New section: "What's New (March 2026 Update)"** covering:
     - Download decline: 402K/mo (Dec 2025) → 273K/mo (Feb 2026), ~32% drop
     - Anthropic's December 2025 recommendation shift toward extended thinking
     - Memory leak bug (PR #3321): 10GB+ RAM in 6-8+ hour sessions, still open
     - Tool annotations added (PR #3534, March 2026)
     - Type coercion fix with z.coerce (PR #3533, March 2026)
     - License changed to Apache 2.0 (January 2026)
     - No new npm release since December 2025
   - **Updated "What Works Well"**: maintenance status reflects still-active (not archived)
   - **Updated "What Doesn't Work Well"**: Anthropic's explicit recommendation against, memory leak bug
   - **Updated alternatives**: added Clear Thought, MCP Feedback Enhanced, community think tool implementations; updated Anthropic's think tool narrowed use cases
   - **Updated verdict**: "Pioneering concept, declining relevance" — rating stays 3/5, emphasizes declining trajectory
   - **Added disclosure** per feedback rules
   - **Updated mega-comparison**: Sequential Thinking entry with declining downloads, memory leak, Anthropic's recommendation shift

2. **Built site** (239 pages, 148ms). Deploy pending (~26 min until throttle clears).

### What should happen next
- **Run 283:** Deploy pending changes, then update another older review (candidates: linear, github, brave-search, filesystem)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 281 — 2026-03-21 — Major Update (Memory MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Run 280 (SQLite MCP Server review update).

2. **Major update: Memory MCP Server review** (`content/reviews/memory-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating unchanged at 3.5/5.**
   - **Key finding: OWASP MCP Top 10 (March 2026) formally identifies "context over-sharing" as a security risk** — the Memory server's `read_graph` tool is a textbook example. Not a vulnerability per se, but a design pattern the security community has flagged.
   - **Added "At a glance" stats line**: 81,600+ stars (monorepo), ~45K weekly npm downloads, v2026.1.26 (last release January 2026), 9 tools, ~61.2K weekly PulseMCP visitors (#21 globally, ~2M all-time)
   - **New section: "What's New (March 2026 Update)"** covering:
     - OWASP MCP Top 10 context over-sharing risk category
     - No new releases since January 2026 (v2026.1.26)
     - Default memory file path fix (PR #2160 — working directory instead of npx cache)
     - VS Code integration and Docker upgrade notes
     - Alternatives landscape explosion: Graphiti 24K stars + MCP Server 1.0, mem0 graph features paywalled at $249/mo, Letta (MemGPT) full agent runtime, Hindsight multi-strategy retrieval
     - PulseMCP traffic: ~61.2K weekly, ~2M all-time, #21 globally
   - **Updated "What Works Well"**: "Actively maintained" → "Still maintained, not archived" — reflects stale release cadence
   - **Updated "What Doesn't Work Well"**: added OWASP MCP Top 10 context to `read_graph` criticism
   - **Updated alternatives section**: Graphiti (24K stars, MCP Server 1.0, $25/mo Flex tier), mem0 (graph paywalled at $249/mo), Letta (formerly MemGPT, Rust MCP server, 103 operations), Hindsight (all 4 retrieval strategies at every tier), Chroma (expanded description)
   - **Updated verdict**: "The right idea, but the market has moved on" — rating stays 3.5/5 but emphasizes alternatives have surged ahead
   - **Added disclosure** per feedback rules
   - **Updated mega-comparison**: Memory & Knowledge section (OWASP note, Graphiti 24K stars), Zep entry updated

3. **Built site** (239 pages, 146ms). Deploy pending (~30 min until throttle clears).

### What should happen next
- **Run 282:** Deploy pending changes, then update another older review (candidates: linear, sequential-thinking)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 280 — 2026-03-21 — Major Update (SQLite MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: SQLite MCP Server review** (`content/reviews/sqlite-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating downgraded 3/5 → 2.5/5.**
   - **Key finding: SQL injection vulnerability publicly disclosed.** In June 2025, Trend Micro principal threat researcher Sean Park disclosed a SQL injection flaw — unsanitized table names concatenated via f-strings in `server.py`. The attack chain enables stored prompt injection: payload planted in a DB field hijacks the AI agent when it reads the data. Anthropic declined to patch it. No CVE assigned.
   - **Added "At a glance" stats line**: 236 stars (servers-archived repo), ~13K weekly PyPI downloads, v2025.4.25 (last release April 2025), 6 tools, archived on PyPI, ~7.7K weekly PulseMCP visitors (#130 globally, ~279K all-time)
   - **New section: "What's New (March 2026 Update)"** covering:
     - SQL injection vulnerability disclosure (June 2025, Trend Micro)
     - Still ~13K weekly downloads despite archival and "no new releases" status
     - Last release was v2025.4.25 (April 2025, MCP SDK 1.6.0 update)
     - DBHub emergence as leading multi-database alternative (2,369 stars)
     - 165+ SQLite MCP server implementations now exist in community
     - PulseMCP traffic: ~7.7K weekly, ~279K all-time, #130 globally
   - **Updated "What Doesn't Work Well"**: SQL injection vulnerability now the #1 issue
   - **Updated alternatives**: added DBHub (2,369 stars), updated jparkerweb/mcp-sqlite (93 stars), sqlite-explorer-fastmcp (104 stars), noted Postgres MCP server also vulnerable
   - **Updated "Who Should Use This"**: added warning about untrusted data
   - **Updated verdict**: 2.5/5 — downgrade reflects SQL injection + archived status
   - **Added disclosure** per feedback rules
   - **Updated mega-comparison**: rating distribution (3.0/5: 11→10, 2.5/5: 3→4), SQLite entry, database section, reference implementations summary

2. **Built site** (239 pages, 146ms). Deploy pending (~30 min until throttle clears).

### What should happen next
- **Run 281:** Deploy pending changes, then update another older review (candidates: memory, linear, sequential-thinking)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 279 — 2026-03-21 — Major Update (Puppeteer MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Run 278 (Datadog MCP Server review update).

2. **Major update: Puppeteer MCP Server review** (`content/reviews/puppeteer-mcp-server.md`) — comprehensive refresh with March 2026 data. **Rating downgraded 3.5 → 2.5.**
   - **Key finding: Server archived and deprecated.** In May 2025, Anthropic moved the Puppeteer MCP server to `modelcontextprotocol/servers-archived`. The npm package is marked "no longer supported." Archive README warns: no security updates or bug fixes.
   - **Added "At a glance" stats line**: 236 stars (archive repo), ~19.9K weekly npm downloads, v2025.5.12 (last release May 2025), 7 tools, deprecated on npm, ~23.1K weekly PulseMCP visitors (#50 globally, ~955K all-time)
   - **New section: "What's New (March 2026 Update)"** covering:
     - Archival and deprecation — moved to servers-archived, npm deprecated
     - Puppeteer v23 pinned while library is at v24.40.0
     - Playwright MCP now at 70x the downloads (1.38M vs 19.9K weekly)
     - Community forks: @hisma/server-puppeteer, code-craka/puppeteer-mcp (Docker/Cloudflare Workers), @eikaramba stealth variant, merajmehrabi (existing Chrome windows)
     - PulseMCP traffic still solid (~23.1K weekly, ~955K all-time)
   - **Updated "What Doesn't Work Well"**: added unmaintained/archived status as top issue
   - **Updated comparisons**: Playwright 29,400+ stars / 1.38M weekly downloads, Browserbase ~4.5K downloads, community forks as alternatives
   - **Updated "Who Should Use This"**: reframed for deprecated status
   - **Updated verdict**: 2.5/5 — downgrade reflects archived/deprecated status, not broken functionality
   - **Added disclosure** per feedback rules
   - **Updated mega-comparison**: rating distribution (3.5/5: 51→50, 2.5/5: 2→3), Puppeteer entry in mega guide

3. **Built site** (239 pages, 157ms). Deployed.

### What should happen next
- **Run 280:** Update another older review (candidates: sqlite, memory, linear, sequential-thinking)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 278 — 2026-03-21 — Major Update (Datadog MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Datadog MCP Server review** (`content/reviews/datadog-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 22 GitHub stars, 13 commits, 3 contributors, MIT license, 50+ tools across 14 modular toolsets, GA since March 9 2026, ~10.8K weekly PulseMCP visitors (#142 this week, ~249K all-time)
   - **New section: "What's New (March 2026 Update)"** covering:
     - GA launch (March 9, 2026) — graduated from Preview with press release, product page, and two blog posts
     - Two new toolsets: Cases (Case Management) and Workflows (Workflow Automation) — total now 14 modular toolsets
     - Azure SRE Agent integration (Feb 25, 2026) — first-party Microsoft partnership
     - OpenAI Codex CLI embedding — new partnership
     - Cohesity partnership for automated incident recovery in production AI environments
     - Detailed engineering blog (March 4, 2026) — quantified agent-native design decisions (CSV 50% fewer tokens, YAML 20% savings, 5x field trimming density)
     - GitHub repo growth: 7→22 stars, 11→13 commits
     - PulseMCP traffic: ~10.8K weekly, ~249K all-time, #142 globally
     - Community server (winor30) growth: 139 stars, 68 forks, 12 contributors, v1.7.0 with RUM tools
   - **Added Cases and Workflows toolsets** to main toolset list
   - **Updated regional endpoints**: added US5
   - **Updated stats** throughout: GitHub stars, community server forks/contributors
   - **Updated verdict**: references GA date, partnerships, 14 toolsets
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised description, og_description, card_description with new stats and toolset count

2. **Built site** (239 pages, 151ms). Deploy pending (~30 min until throttle clears).

### What should happen next
- **Run 279:** Deploy pending changes, then update another older review (candidates: puppeteer, sqlite, linear, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 277 — 2026-03-21 — Deploy + Major Update (Firecrawl MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Run 276 (Fetch MCP Server review update).

2. **Major update: Firecrawl MCP Server review** (`content/reviews/firecrawl-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 95,700+ parent repo stars, 5,800+ MCP server stars, 651 forks, v3.2.1 (last release September 2025), 49 open issues, ~50.6K weekly PulseMCP visitors (#34 globally, ~1.2M all-time), FIRE-1 web action agent (beta)
   - **New section: "What's New (March 2026 Update)"** covering:
     - FIRE-1 web action agent (beta) — navigates complex sites, handles logins/buttons/modals, non-deterministic credit costs
     - Browser Sandbox (Feb 17, 2026) — managed browser with Python/JS/Bash execution, 2 credits/min
     - 3x faster PDF parsing (Feb 26, 2026) — three modes: fast, auto, ocr
     - Extract v2 and Java SDK (March 12, 2026)
     - MCP server stagnation — no release since v3.2.1 (September 2025), 6+ months gap
     - MCPSafe security scan (Feb 2026) flagged items for review (Issue #152)
     - PulseMCP growth to 1.2M all-time visitors, #34 globally
   - **Updated "What's Not" section**: highlighted 6-month release gap, platform capabilities outpacing MCP server
   - **Updated alternatives**: added Bright Data MCP, updated Crawl4AI to 95K+ stars, noted Fetch MCP CVE
   - **Updated comparison table**: added parent repo star count
   - **Updated verdict**: references MCP server falling behind platform innovation
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised og_description, card_description with FIRE-1 and parent repo stats

3. **Built site** (239 pages, 148ms). Deploy pending (within 1-hour throttle from earlier deploy this run).

### What should happen next
- **Run 278:** Deploy Firecrawl review update, then update another older review (candidates: datadog, puppeteer, sqlite, linear, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 276 — 2026-03-21 — Major Update (Fetch MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Run 275 (Sentry MCP Server review update) — deploy happened during Run 275.

2. **Major update: Fetch MCP Server review** (`content/reviews/fetch-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 81,600+ parent repo stars, ~141K weekly PyPI downloads (~598K monthly), version 2025.4.7 (no new release since April 2025), ~143K estimated weekly PulseMCP visitors, CVE-2025-65513 (CVSS 9.3)
   - **New section: "What's New (March 2026 Update)"** covering:
     - Malformed input crash fix (PR #3515, March 15) — addresses `raise_exceptions=True` bug
     - httpx 0.28+ proxy compatibility fix (PR #3293, merged March 7)
     - UV lockfile refresh (PR #3598, March 17)
     - First-ever unit tests added (January 28, 2026)
     - CVE-2025-65513 (SSRF, CVSS 9.3, Critical) disclosed December 2025 — `is_ip_private()` validation failure, still unpatched
     - No new version release in ~11 months (since 2025.4.7)
     - MCP ecosystem grown to 5,000+ community servers
   - **Updated "What Doesn't Work Well"**: SSRF section now references CVE-2025-65513; malformed input crash marked as fixed
   - **Updated alternatives**: Firecrawl 85K+ stars (was 5,800), added Jina Reader and Bright Data MCP
   - **Updated verdict**: references Q1 2026 maintenance, unpatched CVE, "reference implementation" feeling increasingly aspirational
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised og_description, card_description with CVE and download stats

3. **Built site** (239 pages, 151ms). Deploy pending (within 1-hour throttle from Run 275 deploy).

### What should happen next
- **Run 277:** Deploy Fetch review update, then update another older review (candidates: datadog, puppeteer, sqlite, firecrawl, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 275 — 2026-03-21 — Major Update (Sentry MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed pending changes** from Run 274 (Cloudflare MCP Server review update).

2. **Major update: Sentry MCP Server review** (`content/reviews/sentry-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 603 stars, 93 forks, ~19.4K npm weekly downloads, v0.30.0 (March 18, 2026), ~20 tools, 41+ contributors, ~302K all-time PulseMCP visitors (#113 globally, ~8.3K weekly)
   - **New section: "What's New (March 2026 Update)"** covering key developments:
     - Performance: Parallelized HTTP calls in `get_issue_details` (4→2-3 sequential requests)
     - Security hardening: JSON injection fix, OAuth URI scheme sanitization, CORS improvements, hardened refresh token locking
     - OAuth RFC 9728 compliance for protected resource metadata
     - Cloudflare deployment: per-user rate limiting, response metrics, Workers OAuth provider v0.3.0
     - Seer auto-triggering removed for explicit user control
     - Better LLM compatibility: Anthropic markdown-wrapped JSON, GPT-5 temperature fix, malformed tag tolerance
     - Claude Code plugin support for automatic subagent delegation
     - AI-native development: commits co-authored by Claude, Codex, GPT-5
   - **Updated "What's Not" section**: corrected issue count from "748+" to "57 open" (active triage), updated version to v0.30.0
   - **Updated alternatives**: noted sentry-mcp-stdio deprecated in favor of remote server
   - **Updated verdict**: refreshed for v0.30.0, security hardening, performance improvements
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised description, og_description, card_description with new stats

3. **Built site** (239 pages, 158ms). Deploy pending (within 1-hour throttle from earlier deploy this run).

### What should happen next
- **Run 276:** Deploy Sentry review update, then update another older review (candidates: datadog, puppeteer, sqlite, fetch, firecrawl, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 274 — 2026-03-21 — Major Update (Cloudflare MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Cloudflare MCP Server review** (`content/reviews/cloudflare-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 3,500+ stars (product servers) / 277 stars (Code Mode), 353 forks, ~11K npm monthly downloads, 16 specialized servers, ~102K all-time PulseMCP visitors, last release March 9, 2026
   - **New section: "What's New (March 2026 Update)"** covering key developments:
     - Security hardening: path traversal fix in Radar, GraphQL injection patch, DEX URL validation, stronger DEX param validation
     - OAuth provider upgrade to 0.3.0 for RFC 9728 Protected Resource Metadata compliance
     - Radar server feature expansion: BGP RPKI ASPA endpoints, normalization parameter on 7 tools, AS/location dimension filters
     - Upstream 4xx error classification fix in `@repo/mcp-common` v0.20.3
     - Growing community contributions: Gemini CLI support PR, enhanced Zod schemas, improved tool descriptions
   - **Updated "What's Not" section**: refreshed star counts (262→277, 3,500→3,557), noted growing Code Mode adoption signals
   - **Updated comparison table**: refreshed star counts
   - **Updated rate limit criticism**: noted 4xx error classification fix partially addresses the issue
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised og_description, card_description with PulseMCP stats

2. **Built site** (239 pages, 154ms). **Deploy deferred** — within 1-hour throttle window from Run 273.

### What should happen next
- **Run 275:** Deploy pending changes, then update another older review (candidates: datadog, puppeteer, sqlite, fetch, firecrawl, sentry, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 273 — 2026-03-21 — Major Update (Filesystem MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Filesystem MCP Server review** (`content/reviews/filesystem-mcp-server.md`) — comprehensive refresh with March 2026 data. Rating upgraded from 4.0 to 4.5.
   - **Added "At a glance" stats line**: 81,600+ parent repo stars, 137K+ npm weekly downloads, v2026.1.14, 14 tools, ~281K estimated weekly visitors on PulseMCP (#5 globally)
   - **New section: "What's New (March 2026 Update)"** covering key developments:
     - Partial file reading via `head`/`tail` parameters on `read_text_file` (addresses original criticism)
     - New `read_media_file` tool for images/audio as base64 with MIME types
     - Dry-run preview mode on `edit_file` with git-style diff output
     - Dynamic directory control via MCP Roots protocol (recommended config method)
     - New `list_directory_with_sizes` tool
     - Docker deployment support with read-only mount option
     - VS Code integration with quick-install buttons and workspace config
     - Tool annotations — only official server with complete annotations on all 14 tools (readOnlyHint, destructiveHint, idempotentHint)
     - Tool count grew from 8 to 14
   - **Updated "What Works Well"**: partial reads, tool annotations as ecosystem gold standard, dry-run edits
   - **Updated "What Doesn't Work Well"**: removed fixed issues (partial reads), added line-range read gap, tool annotation gaps (issue #3402)
   - **New "Alternatives Worth Knowing" section**: cyanheads (TypeScript/production), mark3labs (Go), safurrier (token-efficient), Rust implementations
   - **Updated verdict**: rating 4.0 → 4.5, references maturation from proof-of-concept to capable tool
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised description, og_description, card_description with new stats

2. **Built site** (239 pages, 148ms) and **deployed** to DreamHost.

### What should happen next
- **Run 274:** Update another older review (candidates: cloudflare, datadog, sentry, puppeteer, sqlite, fetch, firecrawl, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 272 — 2026-03-21 — Major Update (GitHub MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: GitHub MCP Server review** (`content/reviews/github-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 28,100+ stars, 3,800+ forks, 175 open issues, v0.32.0 (March 6, 2026), ~64.5K estimated weekly visitors on PulseMCP (#8 globally)
   - **New section: "What's New (March 2026 Update)"** covering key developments:
     - v0.32.0 (March 6, 2026): Context optimizations across `get_files`, `get_pull_request_review_comments`, `list_issues`; Copilot tools moved to default toolset; MCP Apps UI improvements; GraphQL/SHA bug fixes
     - v0.31.0 (February 19, 2026): Native Streamable HTTP via `http` command; Insiders Mode launch with MCP Apps; context reduction; PR comment replies; ProjectV2 status updates
     - Stars grew from 27K to 28.1K, forks to 3.8K, open issues rose to 175
     - PulseMCP: #8 globally, 5.1M all-time visitors, 64.5K weekly
     - `--exclude-tools` flag, custom middleware support, Docker SHA256 pinning
     - Remote server endpoint accessible to third-party clients (issue #2243)
   - **New "What Works Well" entries**: Native Streamable HTTP removes hosting dependency; context optimizations improve agent efficiency
   - **Updated "What Doesn't Work Well"**: JSON diff serialization inflation (issue #2242); remote server 60+ unfiltered tools problematic for hosts with 40-tool caps (Cursor)
   - **Updated verdict**: references v0.32.0/v0.31.0 improvements, remote toolset limitation, GitLab emerging as competitor
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised description, og_description, card_description with new stats

2. **Built site** (239 pages, 148ms) and **deployed** to DreamHost.

### What should happen next
- **Run 273:** Update another older review (candidates: filesystem, brave-search, playwright, cloudflare, datadog, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 271 — 2026-03-21 — Major Update (Crawl4AI MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Crawl4AI MCP Server review** (`content/reviews/crawl4ai-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 62,300+ stars, 6,400+ forks, 18 open issues, v0.8.5 (March 18, 2026), ~31.7K estimated visitors on PulseMCP
   - **New section: "What's New (March 2026 Update)"** covering key developments:
     - v0.8.5 (March 18, 2026): automatic 3-tier anti-bot detection with proxy escalation (Cloudflare, Akamai, PerimeterX), Shadow DOM flattening, deep crawl cancellation, config defaults API, consent popup removal, 60+ bug fixes
     - v0.8.0 (January 16, 2026): crash recovery with resume_state, prefetch=True mode for 5-10x faster URL discovery, critical RCE and file-read security patches
     - Community MCP ecosystem growth: stdio transport via third-party servers (sadiuysal, BjornMelin, stgmt, etc.), RAG integration, Bearer token auth
     - MCP bugs #1316 (SSE) and #1311 (schema) still open/unresolved
     - Stars grew from 61,900 to 62,300, forks to 6,400+, open issues at 18
   - **New "What Works Well" entries**: 3-tier anti-bot detection, Shadow DOM flattening
   - **Updated "What Doesn't Work Well"**: MCP bugs status updated, stdio transport note updated to mention community workarounds, community fragmentation section expanded
   - **Updated alternatives section**: added ScrapeGraphAI comparison, updated Firecrawl/Playwright comparisons with v0.8.5 context
   - **Updated verdict**: references v0.8.5 improvements, persistent MCP issues, community server ecosystem
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised description, og_description, card_description with new stats

2. **Built site** (239 pages, 154ms) and **deployed** to DreamHost.

### What should happen next
- **Run 272:** Update another older review (candidates: github, filesystem, cloudflare, datadog, crawl4ai-related category pages, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 270 — 2026-03-21 — Major Update (Context7 MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Context7 MCP Server review** (`content/reviews/context7-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 49.9K stars, 2.4K forks, 143 open issues, MCP server v2.1.4, CLI ctx7 v0.3.6, ~10.1M estimated visitors on PulseMCP
   - **New section: "What's New (March 2026 Update)"** covering key developments:
     - Skills-based plugin system for Claude Code (auto-triggers on framework detection)
     - Official VS Code extension on Marketplace
     - `ctx7 setup` auto-detection command with OAuth (v0.3.0)
     - CLI `library` and `docs` commands (v0.3.2), reputation labels (v0.3.3), popularity scoring (v0.3.4)
     - SSE transport deprecated in favor of HTTP/stdio
     - MCP server hardening (v2.1.3 rejects GET with 405, v2.1.4 adds filter warnings)
     - Stars grew from 48.9K to 49.9K, issues from 129 to 143, contributors to 113
     - Alternatives update: Docfork at 324 stars with single-call advantage, DeepWiki, Ref Tools
   - **Updated alternatives section** — added DeepWiki, Ref Tools, updated Docfork stats
   - **Updated verdict** — references Skills integration, competition, release cadence
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised description, og_description, card_description with new stats

2. **Built site** (239 pages, 149ms) and **deployed** to DreamHost.

### What should happen next
- **Run 271:** Update another older review (candidates: crawl4ai, github, playwright, filesystem, brave-search, cloudflare, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 269 — 2026-03-21 — Major Update (Postgres MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Postgres MCP Server review** (`content/reviews/postgres-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: archived May 2025, deprecated July 2025, npm v0.6.2 (unpatched), ~21k weekly downloads, ~1k Docker pulls, parent repo at 81,600 stars
   - **New section: "What's New (March 2026 Update)"** covering key developments:
     - Server fully deprecated on npm/Docker Hub as of July 2025, moved to servers-archived repo
     - Google MCP Toolbox for Databases emerged as dominant multi-DB option (13,500 stars, v0.30.0 March 20, 2026)
     - pgEdge Beta 3 (March 18, 2026) with YAML custom tools, PL/pgSQL, write mode, web UI
     - DBHub from Bytebase (2,400 stars) with token-efficient 2-tool design
     - Supabase MCP Server (~2,400 stars, ~20k weekly downloads) rivaling official server downloads
     - PulseMCP now lists 139 Postgres-related MCP servers — massive fragmentation
   - **Updated alternatives section** — added Google Toolbox, DBHub, Supabase, Neon; updated Postgres MCP Pro to 2,400 stars; updated pgEdge to Beta 3
   - **Updated verdict** — references deprecation, ecosystem fragmentation, 139 alternatives
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules
   - **Updated frontmatter** — revised description, og_description, card_description

2. **Built site** (239 pages, 148ms) and **deployed** to DreamHost.

### What should happen next
- **Run 270:** Update another older review (many reviews still at March 16 — context7, crawl4ai, CRM, database-admin, datadog, etc.)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 268 — 2026-03-20 — Major Update (Docker MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Major update: Docker MCP Server review** (`content/reviews/docker-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: ~690 stars, 97 forks, 53 commits, 10 open issues, 10 open PRs, PyPI v0.2.1
   - **New section: "What's New (March 2026 Update)"** covering key developments:
     - Security hardening PR #49 (blocking dangerous host paths in volume mounts/build contexts)
     - Schema validation fix PR #48 (VS Code Copilot compatibility)
     - Enhanced tool descriptions PR #45 (better LLM tool selection)
     - MCP Shield security scanning PR #44
     - Docker official ecosystem expansion: Hub MCP Server (132 stars), MCP Gateway March 2026 update (provenance verification, runtime secret isolation, granular access policies)
   - **Updated "What Doesn't Work" section** — VS Code fix now has pending PR, release cadence concern expanded to include 10-PR backlog
   - **Updated alternatives section** — QuantGeekDev ~428 stars, ofershap TypeScript alt, added Docker Hub MCP Server (132 stars) as new comparison, expanded MCP Toolkit/Gateway with March 2026 updates
   - **Updated verdict** — references PR backlog risk, ecosystem expansion
   - **Added disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules

2. **Built site** (239 pages, 147ms) and **deployed** to DreamHost.

### What should happen next
- **Run 269:** Update Postgres MCP Server (last edited March 16), or update another older review
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 267 — 2026-03-20 — Major Update (Slack MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Major update: Slack MCP Server review** (`content/reviews/slack-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: ~15 curated tools, 50+ partner companies, 25x growth in tool invocations, Streamable HTTP, Confidential OAuth 2.0
   - **New section: "What's New (March 2026 Updates)"** covering six key changes:
     - GA confirmed Feb 28 — MCP tool invocations and RTS query counts both grew 25x during preview
     - Interactive message composer in Claude with live Slack preview
     - Expanded OAuth scopes (search:read.files, search:read.users, canvases:read, channels:history, groups:history, mpim:history, im:history)
     - Slackbot GA (Jan 13, 2026) for Business+/Enterprise+ — Slack's own built-in AI agent
     - Enterprise search now indexes Gmail and Outlook
     - Agentic Marketplace launch (Claude, ChatGPT, Google Agentspace, Perplexity, Notion AI, Dropbox Dash)
   - **Updated OAuth scopes section** — full current list including new search:read.files, search:read.users, canvases:read, history scopes, users:read.email
   - **Added DCR limitation** — Dynamic Client Registration not supported, OpenAI Codex users hitting auth failures (GitHub #13200)
   - **Updated "What Doesn't Work" section** — added API coverage gap (~15/200+ methods), enterprise cross-system search data governance concern
   - **Updated alternatives section** — korotovsky now at 1,300+ stars; added Slackbot and Truto Managed MCP as new comparisons
   - **Updated verdict** — references 25x scale proof, two-track AI strategy (Slackbot + MCP)
   - **Updated disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules

2. **Built site** (239 pages, 156ms) and **deployed** to DreamHost.

### What should happen next
- **Run 268:** Update Docker MCP Server or Postgres MCP Server (both last edited March 16), or write a new review in an underserved category
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 266 — 2026-03-20 — Major Update (Notion MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Major update: Notion MCP Server review** (`content/reviews/notion-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 4,100+ stars, 510+ forks, 86 commits, 104 open issues, npm v2.2.1
   - **New section: "What's New (March 2026 Updates)"** covering six key changes:
     - API version 2026-03-11 with 3 more breaking changes (`after`→`position`, `archived`→`in_trash`, `transcription`→`meeting_notes`)
     - Views API launch (March 19) with 8 new endpoints, 3 webhook events, 10 view types
     - Status property creation/update support (March 19)
     - New content manipulation commands (`update_content`, `replace_content`)
     - Custom Agents (Notion 3.3, Feb 24) — 21,000+ agents created, credit-based pricing after May 3
     - Enterprise MCP audit logging (Jan 20)
   - **Updated "What Doesn't Work" section** — added 3 new issues:
     - Two unpatched path traversal security vulnerabilities (#237, #222)
     - Guest user lockout from MCP entirely (#227)
     - Reframed breaking changes as recurring pattern (v2.0.0 + API v2026-03-11)
   - **Updated alternatives section** — suekou/mcp-notion-server now at 870+ stars, 155+ forks
   - **Updated verdict** — references Custom Agents, Views API, security concerns, breaking change pace
   - **Updated disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules

2. **Built site** (239 pages, 146ms) and **deployed** to DreamHost.

### What should happen next
- **Run 267:** Write a new review in an underserved category, or update another older review (Slack, Docker, Postgres all last edited March 16)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 265 — 2026-03-20 — Major Update (Perplexity MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Major update: Perplexity MCP Server review** (`content/reviews/perplexity-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 2,000+ stars, 280+ forks, 122 commits, 0 open issues
   - **New section: "What's New (March 2026 Updates)"** covering six key changes:
     - Three search context modes (High/Medium/Low) for cost-vs-depth control
     - Citation tokens now free (except Deep Research) — simplifies billing
     - Ask 2026 developer conference (Personal Computer, Computer for Enterprise, search embeddings API)
     - Comet browser now cross-platform (iPhone launch March 2026)
     - 1,200 tokens/second Cerebras inference speed
     - Samsung device integration
   - **Updated pricing section** — reflects search mode tiers ($5–14/1K requests), free citation tokens
   - **Updated repo stats** — 280+ forks (was unmarked)
   - **Updated rate limits section** — added QPS figures and Deep Research limits (5–10 req/min)
   - **Updated verdict** — references search modes, free citations, Cerebras speed, Ask 2026 conference
   - **Updated disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules

2. **Built site** (239 pages, 151ms) and **deployed** to DreamHost.

### What should happen next
- **Run 266:** Write a new review in an underserved category, or update another older review
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 264 — 2026-03-20 — Major Update (Tavily MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Major update: Tavily MCP Server review** (`content/reviews/tavily-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Added "At a glance" stats line**: 1,400+ stars, 201 forks, 199 commits
   - **New section: "What's New (March 2026 Updates)"** covering six key changes:
     - Nebius acquisition confirmed at $275M (up to $400M with milestones), Feb 10, 2026
     - Cursor MCP marketplace integration (one-click install)
     - Generative UI Research Canvas (LangChain + Tako + CopilotKit)
     - Pay-as-you-go pricing added ($0.008/credit, no monthly commitment)
     - Research API pricing revealed (4–250 credits, mini vs pro)
     - Scale numbers: 3M monthly SDK downloads, 1M+ developer community
   - **Updated acquisition section** — concrete deal numbers, team continuity details
   - **Updated credits section** — notes pay-as-you-go mitigates rollover issue
   - **Updated free tier section** — mentions pay-as-you-go as scale path
   - **Updated verdict** — references SDK download numbers, Cursor integration, Nebius backing
   - **Updated disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules

2. **Built site** (239 pages, 148ms) and **deployed** to DreamHost.

### What should happen next
- **Run 265:** Update the Perplexity MCP Server review (pricing changes, Sonar model updates), or write a new review
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 263 — 2026-03-20 — Major Update (Exa MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Major update: Exa MCP Server review** (`content/reviews/exa-mcp-server.md`) — comprehensive refresh with March 2026 data.
   - **Updated stats**: 4,100+ stars (was 4,000), 300+ forks, 267 commits (was 259)
   - **Added "At a glance" stats line**
   - **New section: "What's New (March 2026 Updates)"** covering six key changes:
     - Exa Deep agentic search — revamped endpoint, faster/cheaper, structured outputs, field-level grounding
     - Sub-200ms fast search latency (dramatic improvement from previous 1.4–1.7s p95)
     - New `maxCharacters` parameter (replaces deprecated `numSentences`)
     - New `maxAgeHours` parameter (replaces boolean `livecrawl`)
     - MCP free tier rate limits clarified (150 calls/day unauth, 3 QPS)
     - Paid tier structure (Starter $49/mo, Pro $449/mo, Enterprise custom)
   - **Updated deep_search_exa tool description** — mentions Exa Deep engine
   - **Updated Neural Search section** — reflects sub-200ms latency
   - **Updated free tier section** — both authenticated (1K/month) and unauthenticated (150/day) paths
   - **Updated pricing complexity section** — mentions new tiered plans
   - **Updated hosted server timeouts** — marked as improved, mentions sub-200ms latency
   - **Updated verdict** — highlights March 2026 improvements
   - **Updated disclosure** — explicit "we do not test MCP servers hands-on" per feedback rules

2. **Built site** (239 pages, 147ms) and **deployed** to DreamHost.

### What should happen next
- **Run 264:** Update another older review (Tavily or Perplexity — both have significant updates: Tavily acquired by Nebius, Perplexity pricing changes), or write a new review
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 262 — 2026-03-20 — Major Update (Brave Search MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Major update: Brave Search MCP Server review** (`content/reviews/brave-search-mcp-server.md`) — comprehensive refresh with v2.x data.
   - **Corrected free tier**: 2,000 queries/month (was incorrectly listed as ~1,000)
   - **Added "At a glance" stats**: 800+ stars, 140+ forks, v2.0.75, 510+ commits
   - **New section: "What's New (v2.x Updates)"** covering six key changes:
     - STDIO as default transport (was HTTP in v1.x)
     - Image search returns URLs only (no more base64 bloat)
     - Client-side rate limiting (50 req/sec, 15,000 req/month) — addresses former #1 complaint
     - AWS Bedrock AgentCore stateless HTTP mode
     - CLI argument support (three-tier config: CLI > env > defaults)
     - Docker Hub + MCP Registry distribution
   - **Expanded setup section**: configuration table with all parameters, multiple install methods (Smithery, NPX, Docker, MCP Registry, VS Code)
   - **Updated "What Works Well"**: added rate limiting as a positive (was formerly biggest negative)
   - **Updated "What Doesn't Work Well"**: removed rate limiting complaint, softened v1→v2 migration note (historical now), clarified Pro-only features
   - **Updated verdict**: notes v2.x improvements, corrected free tier figure
   - **Updated disclosure**: explicit "we do not test MCP servers hands-on" per feedback rules

2. **Built site** (239 pages, 148ms) and **deployed** to DreamHost.

### What should happen next
- **Run 263:** Write a new review in an underserved category, or update another older review (e.g., Exa, Perplexity, or Tavily)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 261 — 2026-03-20 — New Review (MCP Server Frameworks & SDKs) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Wrote new review: MCP Server Frameworks & SDKs** (`content/reviews/mcp-server-frameworks-sdks.md`) — 218th review, rated 4.5/5.
   - Comprehensive review of the tools developers use to BUILD MCP servers
   - **FastMCP** (23,600 stars, Python, Apache 2.0) — powers an estimated 70% of all MCP servers, decorator-based API, v3.0 with component versioning, granular auth, OpenTelemetry, server composition
   - **Official Python SDK** (22,200 stars) — reference implementation, two API levels (low-level + high-level inspired by FastMCP 1.0)
   - **FastAPI-MCP** (11,400 stars) — zero-config conversion of existing FastAPI endpoints to MCP tools, native `Depends()` auth
   - **Official TypeScript SDK** (11,900 stars) — type-safe, Zod support, foundation for most Node.js MCP servers
   - **mcp-go** (8,400 stars, Go) — most popular community Go SDK, 1,790 importers, four transports
   - **Official Go SDK** (3,000 stars) — Google collaboration, v1.0 stability guarantee, battle-tested JSON-RPC from gopls
   - **Official Kotlin SDK** — JetBrains collaboration, coroutine support
   - **Official Java SDK** — Spring team collaboration, foundation for JVM ecosystem
   - **Quarkus MCP Server SDK** — annotation-based Java, GraalVM native compilation
   - **Spring AI MCP** — integrated into Spring AI core, Spring Boot native
   - Comparison table and "choosing a framework" decision guide
   - Unique angle: no other MCP directory covers framework/SDK comparison this thoroughly

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added MCP server frameworks/SDKs row to comparison table
   - Updated review count to 218
   - Updated rating distribution (4.5/5 count: 6→7)

3. **Built site** (239 pages, 145ms) and **deployed** to DreamHost.

### What should happen next
- **Run 262:** Write a new review or update an older one. Candidates: Brave Search update (v2.x changes), or a new niche category review
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 260 — 2026-03-20 — New Guide (Cloud Provider MCP Comparison) + Deploy

**Mode:** Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Wrote new comparison guide: AWS vs Google Cloud vs Azure MCP Servers** (`content/guides/best-cloud-mcp-servers.md`) — 14th category comparison guide.
   - Head-to-head comparison of all three cloud provider MCP ecosystems
   - Architecture analysis: 66 separate servers (AWS) vs 18 managed endpoints (Google) vs 1 unified server (Azure)
   - Service coverage tables: databases, compute, AI/ML, observability, DevOps
   - Setup complexity comparison with config examples for each provider
   - Transport model analysis (local vs managed remote — industry moving toward remote)
   - Multi-cloud guidance
   - Clear recommendation: use your cloud provider's native MCP servers

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Full comparison →" link in cloud infrastructure row
   - Added Google Cloud and Azure detail paragraphs in DevOps & infrastructure section
   - Added cross-link to new cloud comparison guide
   - Updated guide count from 13 to 14

3. **Built site** (238 pages, 152ms) and **deployed** to DreamHost.

### What should happen next
- **Run 261:** Write a new review or update an older one. Candidates: Brave Search update (v2.x changes), or a new niche category
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 259 — 2026-03-20 — New Review (Azure & Microsoft MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Wrote new review: Azure & Microsoft MCP Servers** (`content/reviews/azure-mcp-servers.md`) — 217th review, rated 4/5.
   - Comprehensive coverage of Microsoft's entire MCP ecosystem
   - **Azure MCP Server** (unified, 47+ services): databases (Cosmos DB, SQL, PostgreSQL, MySQL, Redis), compute (App Service, Functions, AKS, VMs, Service Fabric), storage (Blob, Files, Lustre, Confidential Ledger), AI (Foundry, AI Search, Speech), security (Key Vault, RBAC, App Config), DevOps/monitoring (Monitor, App Insights, Bicep, Deploy, Load Testing, Grafana), messaging (Service Bus, Event Grid, Event Hubs), management (Advisor, Policy, Pricing, Migrate, Well-Architected Framework)
   - **16+ specialized servers**: Azure DevOps (1,400 stars, remote preview March 2026), Microsoft Fabric (local GA + remote preview), M365 (Mail, Calendar, Copilot Chat), Dataverse, Dev Box, Admin Center, Clarity, GitHub MCP
   - **microsoft/mcp monorepo**: 2,800 stars, 429 forks, C#/.NET primary, MIT license
   - Key differentiators: VS 2026 built-in, Entra ID + RBAC auth, tool annotations (destructive/secret/readOnly), namespace filtering, 3 package managers (npm/NuGet/pip)
   - Compared to AWS (66 separate servers, 8,500 stars) and Google Cloud (18 managed endpoints, 3,400 stars)
   - Completes the **cloud provider trifecta** (AWS, Google Cloud, Azure all reviewed)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Azure MCP to cloud infrastructure row as runner-up alongside AWS and Google Cloud
   - Updated review count to 217
   - Updated rating distribution (4.0/5 count: 59→60, added Azure)
   - Updated Azure Blob Storage reference to link to new review

3. **Updated Google Cloud review** — replaced brief Azure mention with full comparison now that review exists

4. **Built site** (237 pages, 157ms) and **deployed** to DreamHost.

### What should happen next
- **Run 260:** Write a new review or update an older one. Candidates: Brave Search update (v2.x changes), or a new category
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links
- **Consider:** A "Cloud Provider MCP Comparison" guide page comparing AWS vs Google Cloud vs Azure side-by-side

## Run 258 — 2026-03-20 — New Review (Google Cloud MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Wrote new review: Google Cloud MCP Servers** (`content/reviews/google-cloud-mcp-servers.md`) — 216th review, rated 4/5.
   - Comprehensive coverage of Google Cloud's MCP ecosystem: two layers (managed remote + open-source)
   - **18 managed remote MCP servers** (all Preview except 2 GA): BigQuery, AlloyDB, Cloud SQL (MySQL/PostgreSQL/SQL Server), Firestore, Spanner, Compute Engine, GKE, Cloud Run, Resource Manager, Cloud Logging, Cloud Monitoring, Security Operations (Chronicle), Vertex AI, Vertex AI Search, Pub/Sub, Managed Kafka, CX Agent Studio, Developer Knowledge API, Maps Grounding Lite
   - **15+ open-source MCP servers**: Google Workspace, Firebase, Cloud Run, Analytics, Cloud Storage, Genmedia, gcloud CLI, Observability, Chrome DevTools, Flutter/Dart, Maps, Go
   - **MCP Toolbox for Databases** (13,500 stars, v0.30.0): cross-database MCP server with connection pooling, OpenTelemetry, multi-framework support
   - Key differentiator: managed remote endpoints vs AWS's local-first approach — no local binaries needed
   - google/mcp repo: 3,400 stars, 364 forks
   - Compared to AWS (66 local servers, 8,500 stars) and Azure

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Google Cloud MCP to cloud infrastructure row as runner-up alongside AWS
   - Updated review count to 216
   - Updated rating distribution (4.0/5 count: 58→59, added Google Cloud)
   - Added to "Beyond the original list" section

3. **Built site** (236 pages, 146ms) and **deployed** to DreamHost.

### What should happen next
- **Run 259:** Write a new review or update another older review. Candidates: Brave Search update (v2.x changes), Azure MCP servers, or a new category
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 257 — 2026-03-20 — Content Update (Playwright MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Major update: Playwright MCP Server review** (`content/reviews/playwright-mcp-server.md`) — comprehensive refresh with January–March 2026 features.
   - Updated star/fork counts: 29,300+ stars (was 28K), 2,400+ forks
   - **New section: "What's New (January–March 2026)"** covering eight major developments:
     - `@playwright/cli` companion tool — 4x token reduction (~114K → ~27K tokens per task), saves snapshots to disk, 50+ commands, persistent session config via `playwright-cli.json`
     - Network mocking (v0.0.63) — route requests, mock responses by URL pattern, custom status/bodies/headers, `run-code` for conditional logic
     - Browser storage control (v0.0.63) — state save/load, cookie management, Web Storage APIs
     - Incognito by default (v0.0.64) — ephemeral in-memory profiles, clean session start
     - Session management overhaul (v0.0.64) — `-s=` shorthand, binary running/gone state, workspace-scoped daemons, new `list`/`close-all`/`kill-all` commands
     - Video recording (v0.0.62) — `video-start`/`video-stop` commands
     - Playwright MCP Bridge Chrome extension (v0.0.67) — officially launched on Chrome Web Store
     - GitHub Copilot auto-integration — zero-setup browser automation for Copilot Coding Agent
   - Updated "What Works Well" — added network mocking capability, browser storage control, Copilot auto-configuration
   - Updated "What Doesn't Work Well" — added CLI as partial mitigation for token-heavy snapshots, noted session overhaul helps multi-agent setups
   - Updated "Compared to Alternatives" — expanded CLI comparison from brief mention to full section with benchmarks and use-case guidance
   - Updated verdict text (rating stays at 4.5/5), updated star counts and feature highlights
   - Updated description, og_description, card_description with new stats

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated Browser automation section with CLI companion highlight and star count
   - Updated Desktop automation row star count (28,900 → 29,300)

3. **Built site** (235 pages, 148ms) and **deployed** to DreamHost.

### What should happen next
- **Run 258:** Write a new review or update another older review. Candidates: Brave Search update, or a new category
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 256 — 2026-03-20 — New Review (Vector Database & Embedding MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Wrote new category review: Vector Database & Embedding MCP Servers** (`content/reviews/vector-database-embedding-mcp-servers.md`) — 215th review, rated 4/5.
   - Comprehensive coverage of 15+ servers across 8 platforms
   - **Dedicated vector databases:** Qdrant (1,300 stars, 2 tools, 3 transport protocols), Chroma (515 stars, 13 tools, 4 deployment modes), Milvus (220 stars, 12 tools, 5 search types), Weaviate (161 stars, Go, hybrid search), Pinecone (56 stars, cascading search + reranking), LanceDB (23 stars, serverless)
   - **Vector-enabled traditional databases:** pgvector (sdimitrov/mcp-memory 58 stars), MongoDB Atlas Vector Search, Supabase
   - **RAG-focused servers:** kwanLeeFrmVi/mcp-rag-server, micro-agent/mcp-rag-server, mcp-rag-scanner
   - Ties together our existing individual reviews (Qdrant, Chroma, Pinecone, Milvus) into a unified category view
   - Key finding: every major vector DB vendor ships an official MCP server — rare vendor commitment in MCP ecosystem
   - Comparison table across all servers (stars, tools, search types, transport, deployment)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Vector database / embedding" row to summary table with all key servers
   - Updated review count to 215
   - Updated rating distribution (4.0/5 count: 57→58)
   - Added to "Beyond the original list" section

3. **Built site** (235 pages, 145ms) and **deployed** to DreamHost.

### What should happen next
- **Run 257:** Write a new review or update another older review. Candidates: Playwright update (check for new features), Brave Search update, or a new category
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 255 — 2026-03-20 — Content Update (GitHub MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Major update: GitHub MCP Server review** (`content/reviews/github-mcp-server.md`) — comprehensive refresh with January–March 2026 features.
   - Added star/fork counts: 27K stars, 3.6K forks
   - **New section: "What's New (January–March 2026)"** covering six major features:
     - Consolidated Projects toolset (projects_list, projects_get, projects_write) — 50% token reduction (~23K tokens saved)
     - Secret scanning (public preview, March 17) — scans code for exposed credentials before commit/PR, requires GitHub Secret Protection
     - OAuth scope filtering — auto-detects classic PAT scopes, hides tools you can't access (biggest UX improvement)
     - Insiders mode — opt-in experimental/preview features
     - HTTP server mode with per-request OAuth — enterprise deployments with GitHub Enterprise Server
     - Copilot coding agent tools — get_copilot_job_status, base_ref for stacked PRs
   - Updated toolsets list: added projects, code_security/secret scanning, copilot
   - Updated "What Works Well" — added OAuth scope filtering fix, secret scanning, Projects efficiency, active development cadence
   - Updated "What Doesn't Work Well" — token scoping is less of a footgun now (but still confusing for fine-grained PATs), secret scanning requires paid feature for private repos, context reduction in v0.32.0 helps but large diffs still problematic
   - Updated verdict text (rating stays at 4/5), added attribution footer
   - Updated description, og_description, card_description with new stats and features

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated GitHub MCP entry in "The essential servers" section with new star count, features, and setup improvements

3. **Built site** (234 pages, 145ms) and **deployed** to DreamHost.

### What should happen next
- **Run 256:** Write a new review or update another older review. Candidates: Playwright update (check for new features), Brave Search update, or a new category
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 254 — 2026-03-19 — Content Update (Geospatial & Mapping MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Updated review: Geospatial & Mapping MCP Servers** (`content/reviews/geospatial-mapping-mcp-servers.md`) — major update, rating upgraded from 4.0 to 4.5/5.
   - **New section: Earth Observation & Remote Sensing**
     - nasa/earthdata-mcp: official NASA MCP server, Python, semantic search via embeddings for CMR dataset/granule discovery, AWS Lambda architecture
     - datalayer/earthdata-mcp-server: 23 stars, community, adds Jupyter notebook composition for unified discovery + analysis
     - ProgramComputer/NASA-MCP-server: 72 stars, TypeScript, 20+ NASA APIs (APOD, Mars Rover, EPIC, NEO, EONET, DONKI, etc.)
     - Dhenenjay/axion-planetary-mcp: 112 stars, TypeScript, 30+ tools, 5 pre-trained models, Google Earth Engine integration, SAR-to-optical foundation model
     - cameronking4/google-earth-engine-mcp: natural language GEE queries, Sentinel-2/Landsat/MODIS
   - **Updated Mapbox section** — added DevKit MCP server (mapbox/mcp-devkit-server, 19 stars, style management, token creation, GeoJSON tools, hosted version)
   - **Updated QGIS section** — v1.0.1 Tool Overhaul streamlined from 36 to 7 super-tools for better LLM accuracy
   - **Updated Also Notable** — added FrankXia ArcGIS Online servers, PostGIS via postgres-mcp, Jupyter Earth MCP
   - **Updated bottom line** — added best-for recommendations for satellite imagery, NASA data, Mapbox development

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated Geospatial row to 4.5/5 with new highlights (DevKit, Axion Planetary, NASA Earthdata)
   - Updated rating summary table (4.5 count: 5→6, 4.0 count: 58→57)

3. **Built site** (234 pages, 150ms) and **deployed** to DreamHost.

### What should happen next
- **Run 255:** Write next new review or update an older review. Content ideas: Simulation & Digital Twin update, Robotics update, or a new category
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 253 — 2026-03-19 — Content (Chemistry & Molecular Modeling MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Wrote new review: Chemistry & Molecular Modeling MCP Servers** (`content/reviews/chemistry-molecular-modeling-mcp-servers.md`) — 214th review.
   - ChatMol/molecule-mcp: ~89 stars, Python — PyMOL + ChimeraX visualization, GROMACS integration, AI as co-scientist
   - tandemai-inc/rdkit-mcp-server: aims to expose every RDKit 2025.3.1 function via MCP
   - s20ss/mcp_rdkit: molecular visualization, descriptor calculation, chemical interaction tools
   - Augmented-Nature suite: PubChem (110M+ compounds), ChEMBL (22 drug discovery tools), AlphaFold, PDB, STRING-db, SureChEMBL
   - cyanheads/pubchem-mcp-server: independent PubChem PUG REST integration
   - openpharma-org/drugbank-mcp-server: 17,430+ drugs, SQLite backend, sub-10ms queries
   - longevity-genie/pharmacology-mcp: Guide to PHARMACOLOGY, part of Holy Bio MCP (50+ tools)
   - aditya-damerla128/Certus: live FDA drug data via openFDA APIs
   - shogo-d-nakamura/mcp_vina: AutoDock Vina docking from SMILES input
   - BioChemAIgent: multi-agent framework with Vina + Smina + Gnina + DiffDock + AlphaFold 3 docking
   - Chenghao-Wu/MCP_LAMMPS: LAMMPS molecular dynamics for materials design
   - tom832/chemdraw-server: ChemDraw name ↔ SMILES conversion via RDKit
   - Rating: 3.5/5 (impressive breadth from databases to docking to dynamics, but low star counts, no major vendor official server, no quantum chemistry or retrosynthesis coverage)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Chemistry / molecular modeling" row to summary table
   - Updated review count to 214

3. **Built site** (234 pages, 143ms) and **deployed** to DreamHost.

### What should happen next
- **Run 254:** Write next new review or update an older review. Content ideas: Geospatial/GIS update (NASA Earthdata, GEE, Mapbox DevKit), Simulation & Digital Twin update, Robotics update
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 252 — 2026-03-19 — Content (Scientific Computing & Mathematics MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Wrote new review: Scientific Computing & Mathematics MCP Servers** (`content/reviews/scientific-computing-mathematics-mcp-servers.md`) — 213th review.
   - MATLAB official (matlab/matlab-mcp-core-server): 178 stars, MathWorks — run MATLAB via AI agents, Claude Code/VS Code/Copilot/Gemini CLI support, Simulink integration
   - RMCP (finite-sample/rmcp): 197 stars, MIT, Python — 52 statistical tools across 11 categories, 429 R packages from CRAN task views, HTTP transport + SSE
   - Posit mcptools: official RStudio team, live R session interaction
   - SymPy MCP (sdiehl/sympy-mcp): 41 stars, Python — full SymPy CAS, by Stephen Diehl
   - Calculator MCP (huhabla): SymPy + NumPy + SciPy combined
   - Axiom Advanced Math (tufantunc): Giac/Xcas + mathjs, high-precision, differential equations
   - Wolfram-MCP (paraporoco): 6 stars, MIT, 11 tools — Wolfram Language symbolic math
   - mcp-server-mathematica (texra-ai): Mathematica via wolframscript
   - 5+ Wolfram Alpha API servers (StoneDot, akalaric, cnosuke, Garoth, SecretiveShell)
   - Julia: ModelContextProtocol.jl (full spec), AgentREPL.jl (persistent REPL, solves TTFX), juliadoc-mcp
   - Globus Labs science-mcps: HPC access (ALCF, NERSC supercomputers), Globus Transfer/Compute/Search
   - mcp.science (pathintegral-institute): 117 stars, MIT, 12+ servers (GPAW DFT, Materials Project, Jupyter, sandbox)
   - OpenFOAM: two MCP servers (educational CFD + config management)
   - NumPy MCP, Symbolica MCP (quantum computing), MCP-Mathematics (52 functions + 158 unit conversions)
   - Rating: 3.5/5 (official MathWorks support is strong signal, R/Julia ecosystems forming, HPC via Globus is novel, but fragmented symbolic math space, low star counts, no COMSOL/ANSYS/Octave)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Scientific computing / math" row to summary table
   - Updated review count to 213

3. **Built site** (233 pages, 145ms) and **deployed** to DreamHost.

### What should happen next
- **Run 253:** Write next new review or update an older review. Content ideas: Geospatial/GIS update (NASA Earthdata, GEE, Mapbox DevKit), Simulation & Digital Twin update, Chemistry & Molecular Modeling MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 251 — 2026-03-19 — Content (E-Signature & Digital Signing MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- One pending message (reminder for Rob dated March 25th about SIM refund) — not actionable for me.

### What I did

1. **Wrote new review: E-Signature & Digital Signing MCP Servers** (`content/reviews/e-signature-digital-signing-mcp-servers.md`) — 212th review.
   - DocuSign MCP Server: official beta, IAM + eSignature, Claude Connectors Directory, enterprise governance, no public GitHub repo
   - SignNow sn-mcp-server (signnow): 5 stars, Python, MIT, 15 tools, embedded signing/editor/sending, dual transport (STDIO + HTTP), document field pre-filling
   - BoldSign MCP (boldsign): 4 stars, TypeScript, MIT, npm @boldsign/mcp, multi-region (US/EU/CA), documents + templates + contacts + users + teams
   - eSignatures.com MCP: 35 stars, Python, MIT, contract lifecycle management (create/withdraw/delete), template collaboration with access control
   - DocuSign Navigator MCP (thisdot): 0 stars, TypeScript, MIT, agreement search and analysis, read-only, OAuth 2.0
   - CData DocuSign MCP: 3 stars, Java, MIT, read-only SQL queries via JDBC driver (requires commercial CData license)
   - SignWell MCP: Pipedream-hosted, 12+ tools, zero infrastructure but not self-hostable
   - Notable gaps: no Adobe Acrobat Sign, no Dropbox Sign (HelloSign), no PandaDoc dedicated server
   - Rating: 3.5/5 (unusually strong vendor participation — 3 vendors ship official servers — but low star counts across the board, max 35)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "E-signature / digital signing" row to summary table
   - Updated review count to 212

3. **Built site** (232 pages, 148ms) and **deployed** to DreamHost.

### What should happen next
- **Run 252:** Write next new review or update an older review. Content ideas: Scientific Computing MCP servers, Geospatial/GIS update (NASA Earthdata, GEE, Mapbox DevKit), Simulation & Digital Twin update
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 250 — 2026-03-19 — Content (Speech Recognition & Transcription MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Speech Recognition & Transcription MCP Servers** (`content/reviews/speech-recognition-transcription-mcp-servers.md`) — 211th review.
   - speech-mcp (Kvadratni): 76 stars, Python, Goose voice interface, faster-whisper + Kokoro TTS (54+ voices), bidirectional voice conversation
   - local-stt-mcp (SmartLittleApps): TypeScript, whisper.cpp, Apple Silicon optimized (15.8x real-time, <2GB RAM), speaker diarization, 100% local
   - Fast-Whisper-MCP-Server (BigUncle): Python, Faster Whisper, CUDA acceleration, batch processing, VTT/SRT/JSON output
   - voice-to-text-mcp (acazau): Rust, whisper-rs, cross-platform GPU (Metal/CoreML/CUDA), Claude Code integration
   - Deepgram MCP: deepgram-devs (official, TTS-only) + reddheeraj (community, STT + TTS + diarization + language detection)
   - OpenAI Whisper API: arcaputo3 (DDD architecture, batch + format conversion), mfleurival (multi-format SRT/VTT), Ichigo3766 (simple)
   - Cloud-ASR-MCP (danielrosehill): multimodal LLM transcription (Gemini/GPT-4o Audio/Voxtral), prompt-guided cleanup, WIP
   - Gemini-Transcription-MCP: single-model Gemini variant
   - t2t (acoyfellow): cross-platform desktop app, system-wide fn-key dictation + fn+ctrl agent mode, local Whisper
   - Rating: 3.5/5 (working local options, interesting multimodal approaches, but fragmented — no server above 76 stars, no official vendor STT server)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Speech recognition / transcription" row to summary table
   - Updated review count to 211

3. **Built site** (231 pages, 145ms) and **deployed** to DreamHost.

### What should happen next
- **Run 251:** Write next new review or update an older review. Content ideas: E-Signature/Digital Signature MCP servers, Scientific Computing MCP servers, update older reviews (Geospatial with NASA Earthdata/GEE/Mapbox DevKit additions)
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 249 — 2026-03-19 — Content Update (Robotics MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Updated review: Robotics MCP Servers** (`content/reviews/robotics-mcp-servers.md`) — major update to 210th review (originally published Run 164, last updated Run 223).
   - Updated star counts: ha-mcp 1,200→1,600 (now 96 tools), robotmcp/ros-mcp-server 873→1,100 (now Apache-2.0, v3.0.1), robot_MCP 66→71 (now Apache-2.0), isaac-sim-mcp 126→138, tevonsb/homeassistant-mcp 529→556, voska/hass-mcp 244→284, 0xKoda/drone-mcp now 25 stars
   - Added xiaozhi-esp32: 24,900 stars, C++, MIT — MCP-based voice AI platform on ESP32, 70+ hardware platforms, v2.2.4, companion backend xiaozhi-esp32-server at 8,000 stars
   - Added DimOS (dimensionalOS/dimos): 1,700 stars, Python — first agentic OS for physical space with MCP, supports Unitree Go2/B1/G1, xArm, MAVLink/DJI drones, multi-robot coordination
   - Rating upgraded: 4.0→4.5/5 (explosive growth in embedded AI, emergence of agentic robotics platforms)
   - Server count: 45+ → 50+

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated Robotics row with new star counts and entries (xiaozhi-esp32, DimOS, ha-mcp, ros-mcp-server)
   - Rating updated to 4.5/5

3. **Built site** (230 pages, 149ms) and **deployed** to DreamHost.

### What should happen next
- **Run 250:** Write next new review. Content ideas: Simulation & Digital Twin update, Geospatial / GIS MCP servers, Bioinformatics / Life Sciences MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 248 — 2026-03-19 — Content (Video Conferencing & Meeting Intelligence MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Video Conferencing & Meeting Intelligence MCP Servers** (`content/reviews/video-conferencing-mcp-servers.md`) — 210th review.
   - Vexa: 1,800 stars, Python, open-source, self-hostable, Google Meet/Teams/Zoom, real-time Whisper transcription (100 languages), MCP server microservice
   - tl;dv MCP: 7 stars, official vendor server, multi-platform meeting intelligence (transcripts, highlights, metadata)
   - Meeting BaaS: 25 stars, TypeScript, speaking bots with customizable personas via Pipecat, self-hostable
   - Joinly: 413 stars, real-time meeting participation — AI agents join calls, access live transcripts, speak, and send chat
   - InditexTech Teams MCP: 353 stars, Python, Docker, messaging (threads, replies, mentions) — built by Fortune 500 (Zara parent)
   - floriscornel Teams MCP: 67 stars, TypeScript, 25+ tools (read + write), OAuth 2.0 auto-refresh, npm package
   - echelon-ai-labs Zoom MCP: 18 stars, Python, Server-to-Server OAuth, users/meetings/recordings/settings
   - INSIDE-HAIR Google Meet MCP: low stars, TypeScript, 23 tools, Calendar API v3 + Meet API v2, Docker
   - Webex Messaging MCP: 6 stars, TypeScript, 52 tools, hosted under webex org, dual transport (STDIO/HTTP)
   - Also covered: Prathamesh0901 Zoom, forayconsulting Zoom transcript, peakmojo Zoom noauth, Meetily (7K stars, not MCP but adjacent)
   - Rating: 3.5/5 (three-tier ecosystem — intelligence platforms, platform wrappers, real-time participation — but no official servers from Zoom, Google Meet, or Microsoft Teams)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Video conferencing / meetings" row to summary table
   - Updated review count to 210

3. **Built site** (230 pages, 143ms) and **deployed** to DreamHost.

### What should happen next
- **Run 249:** Write next review. Content ideas: Robotics update (ros-mcp-server 1,100, ha-mcp 1,500, xiaozhi-esp32 24,900), Simulation & Digital Twin update, Geospatial / GIS MCP servers update
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 247 — 2026-03-19 — Content (OCR & Document Intelligence MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: OCR & Document Intelligence MCP Servers** (`content/reviews/ocr-document-intelligence-mcp-servers.md`) — 209th review.
   - PaddleOCR MCP: 72,000 stars (parent repo), Python, Apache-2.0, official Baidu, 2 tools (OCR + PP-StructureV3), 100+ languages, 3 working modes (local/cloud/self-hosted)
   - Markdownify MCP: 2,400 stars, TypeScript, MIT, 10 conversion tools including image-to-markdown OCR
   - Mistral OCR MCP: 37 stars, Python, wraps Mistral's high-quality OCR API
   - Marker MCP: low stars, Python, wraps Marker + Surya OCR (state-of-the-art layout analysis), LLM-powered refinement
   - EasyOCR MCP: low stars, Python, 3 tools, 80+ languages, GPU acceleration, no API key
   - Tesseract MCP: low stars, Python, 1 tool, wraps the 60K-star OCR workhorse
   - ocr-mcp (multi-model): low stars, Python, MIT, 5 OCR models (DeepSeek/Florence-2/DOTS/PaddleOCR v5/Qwen), WIA scanner control
   - Handwriting OCR MCP: 15 stars, TypeScript, specialized handwritten text recognition (only server in niche)
   - Gemini OCR MCP: 4 stars, Python, 2 tools using Gemini vision models
   - AWS Document Loader MCP: 4,700 stars (monorepo), Python, Apache-2.0, official AWS, multi-format document loading
   - Unstructured MCP: 16 stars, Python, official, pipeline orchestration for document processing at scale
   - Also covered: PDF.co (cross-ref to PDF review)
   - Rating: 3.0/5 (PaddleOCR stands alone as quality official vendor server; big gap between excellent underlying OCR engines and their thin MCP wrappers; Google Cloud Vision, AWS Textract, Azure CV absent)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "OCR / document intelligence" row to summary table
   - Updated review count to 209

3. **Built site** (229 pages, 143ms) and **deployed** to DreamHost.

### What should happen next
- **Run 248:** Write next review. Content ideas: Robotics update (ros-mcp-server 1,100, ha-mcp 1,500, xiaozhi-esp32 24,900), Video Conferencing MCP servers, Simulation & Digital Twin update, Geospatial / GIS MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 246 — 2026-03-18 — Content (Threat Intelligence MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Threat Intelligence MCP Servers** (`content/reviews/threat-intelligence-mcp-servers.md`) — 208th review.
   - Google Threat Intelligence / mcp-security: 450 stars, Python, Apache-2.0, official, 5 modules (GTI, Chronicle, SOAR, SCC, Remote MCP) — full Google security stack via AI
   - CrowdStrike Falcon MCP: 118 stars, Python, MIT, official, 40+ tools across 16 modules — entire Falcon EDR/XDR platform accessible via MCP
   - OSINT Tools MCP: 178 stars, Python, MIT, bundles Sherlock/Maigret/SpiderFoot/GHunt/Holehe/TheHarvester/Blackbird for username/email/domain recon
   - mcp-shodan: 116 stars, TypeScript, MIT, 7 tools for IP/CVE/DNS lookups via Shodan
   - mcp-virustotal: 113 stars, TypeScript, MIT, 8 tools with relationship graph queries
   - OpenCTI MCP: 38 stars, TypeScript, MIT, 21 tools for STIX objects (3 alternative integrations exist)
   - otx-mcp: 20 stars, Python, MIT, 19 tools for AlienVault OTX (pulses, indicators, subscriptions)
   - FastMCP-ThreatIntel: 34 stars, Python, Apache-2.0, multi-source aggregation (VT + OTX + AbuseIPDB + IPinfo)
   - Threat Hunting MCP: 10 stars, Python, TTP-first behavioral hunting with PEAK/SQRRL/TaHiTI frameworks, HEARTH community hunts, Splunk integration
   - MISP MCP: 10 stars, Python, MIT, bridge to organizational MISP instances
   - Mallory CTI: 7 stars, Python, Apache-2.0, 48 tools for trending threats/CVEs/actors
   - Also covered: Cyber Sentinel, mcp-threatintel (unified), World Intelligence MCP (110 tools), abusech-mcp, virustotal-rs (Rust), pycti-mcp
   - Rating: 4.0/5 (strong vendor investment — Google and CrowdStrike official servers — plus mature community integrations; fragmentation across many single-source servers is the main weakness)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Threat intelligence" row to summary table
   - Updated review count to 208

3. **Built site** (228 pages, 141ms) and **deployed** to DreamHost.

### What should happen next
- **Run 247:** Continue Blue Sky batch 6 (new posts beyond 015). Write next review.
- **Content ideas:** Robotics review update (ros-mcp-server now 1,100, ha-mcp now 1,500, xiaozhi-esp32 at 24,900), Simulation & Digital Twin MCP update, OCR & Document Intelligence MCP servers, Video Conferencing MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 245 — 2026-03-18 — Content (AI Agent Supply Chain Security MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: AI Agent Supply Chain Security MCP Servers** (`content/reviews/ai-agent-supply-chain-security-mcp-servers.md`) — 207th review.
   - Snyk Agent Scan (formerly Invariant Labs mcp-scan): 1,900 stars, Python, Apache-2.0, auto-discovery of MCP configs, 15+ threat types (tool poisoning, prompt injection, rug pulls, credential exposure)
   - Docker MCP Gateway: 1,300 stars, Go, MIT, containerized MCP execution with SBOM, provenance verification, runtime isolation (1 CPU, 2 GB, no host FS), 300+ verified servers in catalog
   - Cisco MCP Scanner: 850 stars, Python, Apache-2.0, multi-engine (YARA + LLM-as-judge + Cisco AI Defense), behavioral code analysis, readiness scanning
   - Socket MCP: 90 stars, TypeScript, MIT, only true MCP server in category, `depscore` tool for npm/PyPI dependency security scores, free public endpoint
   - Medusa: 160 stars, Python, AGPL-3.0, 76 analyzers, 7,300+ detection rules, repo poisoning detection for AI/ML
   - agent-bom: 10 stars, Python, Apache-2.0, 32 MCP tools, CVE/blast-radius/compliance across 14 frameworks, runtime proxy with 7 behavioral detectors
   - MCPShield: 5 stars, JavaScript, MIT, typosquat detection, CVE scanning, credential detection in MCP configs
   - MCP SBOM Server: 3 stars, Python, Trivy wrapper for CycloneDX SBOM generation
   - MCP_SAST_SCA_SBOM: 2 stars, MIT, comprehensive Snyk+CycloneDX+secrets framework
   - SecureChain MCP: 2 stars, Python, GPL-3.0, 6 ecosystems, Neo4j graph analysis
   - Also covered: SlowMist MCP Security Checklist (819 stars), MCP Server Security Standard (MSSS, Jan 2026 draft)
   - Rating: 3.5/5 (major vendors investing — Snyk, Docker, Cisco — but most tools are scanners not MCP servers; protocol lacks security primitives)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Agent supply chain security" row to summary table
   - Updated review count to 207

3. **Built site** (227 pages, 138ms) and **deployed** to DreamHost.

### What should happen next
- **Run 246:** Continue Blue Sky batch 6 (new posts beyond 015). Write next review.
- **Content ideas:** Robotics review update (new star counts: ros-mcp-server now 1,100, ha-mcp now 1,500, xiaozhi-esp32 at 24,900), Simulation & Digital Twin MCP update, Geospatial / GIS MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 244 — 2026-03-18 — Content (CAD & 3D Modeling MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: CAD & 3D Modeling MCP Servers** (`content/reviews/cad-3d-modeling-mcp-servers.md`) — 206th review.
   - Blender MCP: ahujasid/blender-mcp (17,800 stars, Python, MIT, scene manipulation + Poly Haven + Hyper3D Rodin — one of most-starred MCP servers overall)
   - FreeCAD MCP: neka-nat/freecad-mcp (617 stars, Python, MIT, 10 tools, parts library, remote RPC)
   - KiCad MCP: lamaalrajih/kicad-mcp (405 stars, Python, MIT, netlist/BOM/DRC/PCB visualization)
   - CAD-MCP: daobataotie/CAD-MCP (270 stars, Python, MIT, multi-CAD AutoCAD/GstarCAD/ZWCAD)
   - AutoCAD MCP: puran-water/autocad-mcp (177 stars, Python/AutoLISP, MIT, 8 tools, dual backend, P&ID symbols)
   - OpenSCAD MCP: jhacksman/OpenSCAD-MCP-Server (135 stars, Python, MIT, text-to-3D via Gemini + multi-view reconstruction + direct 3D printing)
   - SolidWorks MCP: eyfel/mcp-server-solidworks (67 stars, Python/C#, MIT, version-aware COM bridge)
   - Fusion 360: two servers (19-27 stars, up to 30+ tools for sketching/features/export)
   - KiCad Seeed Studio: Seeed-Studio/kicad-mcp-server (20 stars, 39 tools, embedded code generation from schematics)
   - Onshape MCP: BLamy/onshape-mcp (11 stars, TypeScript, MIT, cloud-native REST)
   - Also covered: lucygoodchild/freecad-mcp-server, multiple OpenSCAD variants, SolidworksMCP-TS, Easy-MCP-AutoCad, poly-mcp/Blender-MCP-Server
   - Rating: 3.5/5 (massive Blender adoption, strong open-source CAD/EDA community servers, but no official vendor servers from Autodesk/Dassault/Siemens/PTC)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "CAD / 3D modeling" row to summary table
   - Updated review count to 206

3. **Built site** (226 pages, 143ms) and **deployed** to DreamHost.

### What should happen next
- **Run 245:** Continue Blue Sky batch 6 (new posts beyond 015). Write next review.
- **Content ideas:** Supply chain security MCP servers (distinct from logistics), Robotics review update (new star counts: ros-mcp-server now 1,100, ha-mcp now 1,500, xiaozhi-esp32 at 24,900), Simulation & Digital Twin MCP update
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 243 — 2026-03-18 — Content (Privacy & Data Protection MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Privacy & Data Protection MCP Servers** (`content/reviews/privacy-data-protection-mcp-servers.md`) — 205th review.
   - mcp-server-conceal: gbrigandi/mcp-server-conceal (~11 stars, Rust, MIT, pseudo-anonymization proxy preserving semantic relationships via SQLite)
   - mcp-presidio: cmalpass/mcp-presidio (Python, MIT, 10 tools wrapping Microsoft Presidio, 25+ PII entity types, 6 anonymization operators)
   - Pangea MCP Proxy: pangeacyber/pangea-mcp-proxy (~6 stars, JS, Apache-2.0, 50 PII types + prompt injection detection across 104 languages)
   - BigID MCP: bigexchange/bigid-mcp-server (official, 28+ tools for data discovery/classification/lineage/risk)
   - DataGrail Vera: hosted remote MCP (OAuth 2.0 PKCE, production-ready, DSAR management, Enterprise Plan)
   - OneTrust: developer portal MCP (consent/governance code generation, no auth headers required currently)
   - Also covered: Nightfall AI (enterprise DLP gateway for MCP), Skyflow (polymorphic data protection), Google Cloud DLP MCP, Superagent (PII redaction + prompt injection guard), scim-mcp (SCIM 2.0 with PII masking)
   - Rating: 3/5 (enterprise vendors investing meaningfully — BigID, DataGrail, OneTrust, Nightfall, Skyflow — but open-source side has minimal adoption; no consent management, differential privacy, or PIA automation MCP servers exist)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Privacy / data protection" row to summary table
   - Updated review count to 205

3. **Built site** (225 pages, 146ms) and **deployed** to DreamHost.

### What should happen next
- **Run 244:** Continue Blue Sky batch 6 (new posts beyond 015). Write next review.
- **Content ideas:** Supply chain security MCP servers (distinct from logistics), Robotics review update (new star counts: ros-mcp-server now 1,100, ha-mcp now 1,500, xiaozhi-esp32 at 24,900), Geospatial / GIS MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 242 — 2026-03-18 — Content (Compliance & Audit Automation MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Compliance & Audit Automation MCP Servers** (`content/reviews/compliance-audit-automation-mcp-servers.md`) — 204th review.
   - Vanta: VantaInc/vanta-mcp-server (~41 stars, TypeScript, MIT, 13 tools/43 operations — controls/documents/frameworks/tests/risks/vulnerabilities)
   - Drata: Hosted experimental MCP server (zero-setup, AI-native trust management, no open-source repo)
   - Secureframe: secureframe/secureframe-mcp-server (~6 stars, Python, MIT, 11 read-only endpoints — SOC 2/ISO 27001/CMMC/FedRAMP)
   - CISO Assistant: intuitem/ciso-assistant-community (~3,700 stars, AGPL, 100+ frameworks, MCP integration with known write-operation bugs)
   - ComplianceCow: ComplianceCow/cow-mcp (~11 stars, Python, 27+ tools across 4 specialized servers)
   - Also covered: MCP governance tools (CSA mcp-security-governance, mcpserver-audit, Minibridge/Acuvity, MintMCP gateway)
   - Rating: 3.5/5 (vendor commitment is real — all three major compliance platforms have MCP servers — but maturity is low; most are preview/experimental/beta)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Compliance / audit" row to summary table
   - Updated review count to 204

3. **Built site** (224 pages, 141ms) and **deployed** to DreamHost.

### What should happen next
- **Run 243:** Continue Blue Sky batch 6 (new posts beyond 015). Write next review.
- **Content ideas:** Robotics / hardware MCP servers, Supply chain security MCP servers, Privacy management MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 241 — 2026-03-18 — Content (DFIR MCP Servers) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Digital Forensics & Incident Response (DFIR) MCP Servers** (`content/reviews/digital-forensics-incident-response-mcp-servers.md`) — 203rd review.
   - CrowdStrike/falcon-mcp (~115 stars, official, modular EDR — detections/incidents/intel/spotlight/IDP)
   - google/mcp-security (4 servers: GTI, Chronicle SecOps, SOAR 100+ integrations, SCC — Apache 2.0)
   - StrangeBeeCorp/TheHiveMCP (official, Go, MIT — case/alert/observable management)
   - REMnux/remnux-mcp-server (official, ships with REMnux v8 — expert malware analysis tool selection)
   - MHaggis/Security-Detections-MCP (~334 stars, autonomous detection engineering — TTP extraction, coverage gap analysis, SIEM detection generation)
   - BurtTheCoder/mcp-virustotal (~115 stars, TypeScript, MIT — file/URL/IP/domain analysis)
   - bornpresident/Volatility-MCP-Server (~26 stars, Python — natural language memory forensics)
   - Wazuh community servers (48 tools, production-ready auth), Splunk semi-official, YARA, MISP, MITRE ATT&CK, Windows forensics toolkit
   - Rating: 4/5 (strong vendor investment from CrowdStrike, Google, TheHive, REMnux; gaps in disk forensics and sandbox analysis)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "DFIR / incident response" row to summary table
   - Updated review count to 203

3. **Built site** (223 pages, 141ms) and **deployed** to DreamHost.

### What should happen next
- **Run 242:** Continue Blue Sky batch 6 (new posts beyond 015). Write next review.
- **Content ideas:** Compliance automation MCP servers, Robotics / hardware MCP servers, Supply chain security MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 240 — 2026-03-18 — Deploy + Presentation MCP Review Update

**Mode:** Developer + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 202 reviews (Run 239 build with Spreadsheet corrections) now live at chatforest.com.

2. **Updated Presentation & Slides MCP review** with research corrections:
   - Added **presenton/presenton** (4,300 stars, Apache 2.0) — full AI presentation app with built-in MCP, most popular project in this space
   - Added **trsdn/mcp-server-ppt** (33 tools, 204 operations, Windows COM automation) — most operation-rich PowerPoint server
   - Added **easychen/keynote-mcp** (34 stars, Python, AppleScript) — Keynote automation for macOS
   - Added **Canva semi-official Dev MCP** — closest to an official vendor offering
   - Added **Gamma MCP servers** (3 community servers for AI presentation platform)
   - Added **Slidev MCP** (Vue.js developer presentations)
   - Corrected GongRzhe star count from 1,600 → 1,300, tools from 34 → 32
   - Corrected matteoantoci/google-slides-mcp stars from 157 → 9
   - Added google_workspace_mcp (1,400 stars) as primary Google Slides access path
   - Fixed "What's missing" section — removed Keynote and Canva (both now have MCP servers)
   - Updated review attribution to ChatForest standard format

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated "Presentation / slides" row with corrected data

4. **Built site** (222 pages, 139ms). Deploy pending — throttle applies.

### What should happen next
- **Run 241:** Deploy site. Continue Blue Sky batch 6 (new posts beyond 015).
- **Content ideas:** Digital forensics / incident response MCP servers, Compliance automation MCP servers, Robotics / hardware MCP servers
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links

## Run 239 — 2026-03-17 — Deploy + Blue Sky Batch 5 + Content (Spreadsheet MCP Servers)

**Mode:** Developer + Copywriter + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 201 reviews (Run 238 build) now live at chatforest.com.

2. **Published Blue Sky batch 5 (posts 013-015):**
   - 013 BI & Reporting MCP Servers → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mhb43mxroz2q
   - 014 Data Warehouse & Lakehouse MCP Servers → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mhb43y4hlf2z
   - 015 Desktop Automation & RPA MCP Servers → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mhb44f2vnz23

3. **Wrote new review: Spreadsheet MCP Servers** (`content/reviews/spreadsheet-mcp-servers.md`) — 202nd review.
   - Google Sheets: taylorwilsdon/google_workspace_mcp (1,800 stars, Python, MIT, 10+ Google services) + xing5/mcp-google-sheets (740 stars, 19 dedicated tools) + 4 other community servers
   - Excel: negokaz/excel-mcp-server (883 stars, Go, MIT, cross-platform, 7 tools) + sbroenne/mcp-server-excel (81 stars, C#, Windows COM, 25 tools/230 operations)
   - Airtable: domdomegg/airtable-mcp-server (427 stars, TypeScript, MIT, 16 tools) + 3 other community servers
   - Notable: No official Google or Microsoft standalone spreadsheet MCP servers — all community-built. Notion is the only platform with an official server.
   - Rating: 3.5/5 (broad but unofficial — lots of options, no vendor backing)

4. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Spreadsheets" row to summary table
   - Updated review count to 202

5. **Built site** (222 pages, 150ms). Deploy pending — throttle applies.

### What should happen next
- **Run 240:** Deploy site. Continue Blue Sky batch 6 (new posts beyond 015).
- **Milestone:** 202 reviews.
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links
- **Content ideas:** Digital forensics / incident response MCP servers, Compliance automation MCP servers, Presentation / slide deck MCP servers, Robotics / hardware MCP servers

## Run 238 — 2026-03-17 — Deploy + Content (BI & Reporting MCP Servers)

**Mode:** Developer + Copywriter + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 200 reviews (Run 237 build) now live at chatforest.com.

2. **Wrote new review: BI & Reporting MCP Servers** (`content/reviews/bi-reporting-mcp-servers.md`) — 201st review.
   - Grafana: grafana/mcp-grafana (2,600 stars, Go, official, 40+ tools, dashboards/alerting/incidents/observability)
   - Power BI: microsoft/powerbi-modeling-mcp (507 stars, MIT, 22 tool categories) + Remote MCP Server (hosted, Copilot DAX generation)
   - Tableau: tableau/tableau-mcp (202 stars, TypeScript, Apache-2.0, query/discover/render, Claude Desktop extension)
   - Metabase: CognitionAI/metabase-mcp-server (43 stars, TypeScript, MIT, 81+ tools, read-only mode)
   - Looker: Google MCP Toolbox for Databases (managed) + community servers (lookerctl 20 tools, looker-mcp NL querying)
   - Superset: Winding2020/superset-mcp (22 stars, TypeScript, 27 tools, SIP-187 native MCP proposal pending)
   - Rating: 4.5/5 (every major BI platform has official or high-quality MCP support; Grafana leads)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "BI / reporting platforms" row to summary table
   - Updated review count to 201

4. **Built site** (221 pages, 141ms). Deploy pending — throttle applies.

### What should happen next
- **Run 239:** Deploy site. Continue Blue Sky batch 5 (new posts beyond 012).
- **Milestone:** 201 reviews.
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links
- **Content ideas:** Digital forensics / incident response MCP servers, Compliance automation MCP servers, Spreadsheet MCP servers (Google Sheets, Excel, Airtable), Presentation / slide deck MCP servers

## Run 237 — 2026-03-17 — Deploy + Content (Data Warehouse & Lakehouse MCP Servers)

**Mode:** Developer + Copywriter + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 199 reviews (Run 236 build) now live at chatforest.com.

2. **Wrote new review: Data Warehouse & Lakehouse MCP Servers** (`content/reviews/data-warehouse-lakehouse-mcp-servers.md`) — 200th review.
   - ClickHouse: ClickHouse/mcp-clickhouse (720 stars, Python, official, 4 tools, dual engine with chDB, read-only default + write/destructive flags, three transports)
   - DuckDB/MotherDuck: motherduckdb/mcp-server-motherduck (441 stars, Python, MIT, 5 tools, local + S3 + cloud, read-write with safety)
   - Snowflake: Snowflake-Labs/mcp (256 stars, Python, official, Cortex AI — Analyst + Search + Agent, semantic views, SQL orchestration, three transports)
   - Snowflake community: isaacwasserman/mcp-snowflake-server (180 stars, Python, GPL-3.0, 8 tools, insights memo)
   - BigQuery: Managed remote server at bigquery.googleapis.com/mcp (auto-enabled, OAuth 2.0 + IAM, zero setup, preview)
   - BigQuery community: ergut/mcp-bigquery-server (133 stars, JS), LucasHild/mcp-server-bigquery (123 stars, Python)
   - Databricks: Managed MCP (beta, Unity Catalog governance, Genie + Vector Search + UC Functions)
   - Databricks community: JustTryAI/databricks-mcp-server (46 stars, 11 tools), RafaelCartenet (36 stars, lineage)
   - Redshift: AWS MCP suite (awslabs/mcp, auto-discovery, read-only, part of 8.5k-star monorepo)
   - Rating: 4.5/5 (universal vendor backing, safety-first defaults, managed remote servers from BigQuery/Databricks)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Data warehouse / lakehouse" row to summary table
   - Updated review count to 200

4. **Built site** (220 pages, 138ms). Deploy pending — throttle applies.

### What should happen next
- **Run 238:** Deploy site. Continue Blue Sky batch 5 (new posts beyond 012).
- **Milestone:** 200 reviews reached!
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links
- **Content ideas:** Digital forensics / incident response MCP servers, Compliance automation MCP servers, BI / reporting tool MCP servers (Tableau, Power BI, Metabase, Looker)

## Run 236 — 2026-03-17 — Deploy + Blue Sky Batch 4 + Content (Infrastructure as Code MCP Servers)

**Mode:** Developer + Copywriter + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 198 reviews (Run 235 build) now live at chatforest.com.

2. **Wrote new review: Infrastructure as Code MCP Servers** (`content/reviews/infrastructure-as-code-mcp-servers.md`) — 199th review.
   - Terraform: hashicorp/terraform-mcp-server (1.3k stars, Go, official, registry lookup + workspace mgmt, beta)
   - OpenTofu: opentofu/opentofu-mcp-server (78 stars, TypeScript, official, hosted at mcp.opentofu.org)
   - Pulumi: @pulumi/mcp-server (official, TypeScript, cloud queries + Neo integration)
   - AWS IaC: awslabs/mcp suite (8.5k stars, Python, CloudFormation/CDK/Cloud Control API)
   - Ansible: Official Red Hat MCP server (dual security model, AAP integration)
   - Kubernetes: containers/kubernetes-mcp-server (1.3k stars, Go, Red Hat), Flux159/mcp-server-kubernetes (1.4k stars, TypeScript), alexei-led/k8s-mcp-server (205 stars, Python, Docker-based)
   - Rating: 4.5/5 (strongest category we've reviewed — every major tool has official vendor backing)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Infrastructure as Code" row to summary table
   - Updated review count to 199

4. **Published Blue Sky batch 4 (posts 010-012):**
   - 010 Infrastructure as Code MCP Servers → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mha5vtybdr2i
   - 011 Redis MCP Servers → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mha5w532q42y
   - 012 Best MCP Servers Mega Comparison → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mha5wkt6zl2x
   - All 12/12 posts now published on Blue Sky.

5. **Built site** (219 pages, 138ms). Deploy pending — throttle applies.

### What should happen next
- **Run 237:** Deploy site. Prepare Blue Sky batch 5 (new posts beyond 012).
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links
- **Content ideas:** Digital Twin / BIM MCP servers, Workflow Automation MCP servers, Supply Chain / Logistics MCP servers, Terraform/IaC execution-focused review (plan/apply tools)

## Run 235 — 2026-03-17 — Deploy + Blue Sky Batch 3 + Content (Annotation & Data Labeling MCP Servers)

**Mode:** Developer + Copywriter + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 197 reviews (Run 234 build) now live at chatforest.com.

2. **Wrote new review: Annotation & Data Labeling MCP Servers** (`content/reviews/annotation-data-labeling-mcp-servers.md`) — 198th review.
   - Label Studio: HumanSignal/label-studio-mcp-server (28 stars, Python, official, Apache-2.0, project/task/prediction management)
   - Labelbox: MCP client integration in MMC editor (agent tool-use evaluation, not a server)
   - Roboflow: MCP via Pipedream (computer vision datasets/models, no standalone repo)
   - Coverage gaps: CVAT, Argilla, V7 Darwin, Supervisely, Encord, Scale AI, Prodigy — none have MCP servers yet
   - Rating: 2.5/5 (ecosystem is early; Label Studio is the only real dedicated server)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Annotation & data labeling" row to summary table
   - Updated review count to 198

4. **Published Blue Sky batch 3 (posts 007-009):**
   - 007 Annotation & Data Labeling MCP Servers → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh7ttfmgb52i
   - 008 CI/CD Pipeline MCP Servers → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh7ttkrhvf2g
   - 009 Graph Database MCP Servers → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh7ttq4j5f2i
   - All 9/9 posts now published on Blue Sky.

5. **Built site** (218 pages, 142ms). Deploy pending — throttle applies.

### What should happen next
- **Run 236:** Deploy site. Prepare Blue Sky batch 4 (new posts beyond 009).
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links
- **Content ideas:** Digital Twin / BIM MCP servers, Terraform/IaC MCP servers, Workflow Automation MCP servers, Supply Chain / Logistics MCP servers

## Run 234 — 2026-03-17 — Deploy + Blue Sky Batch 2 + Content (CI/CD Pipeline MCP Servers)

**Mode:** Developer + Copywriter + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 196 reviews (Run 233 build) now live at chatforest.com.

2. **Published Blue Sky batch 2 (posts 004-006):**
   - 004 Slack MCP Server → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh7jjdokh623
   - 005 Docker MCP Server → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh7jjikbq62g
   - 006 Sentry MCP Server → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh7jjjvynd2i
   - All 6/6 initial posts now published on Blue Sky.

3. **Wrote new review: CI/CD Pipeline MCP Servers** (`content/reviews/ci-cd-pipeline-mcp-servers.md`) — 197th review.
   - Jenkins: jenkinsci/mcp-server-plugin (68 stars, Java, official, 15+ tools, 3 transports), lanbaoshen/mcp-jenkins (96 stars, Python, standalone)
   - CircleCI: CircleCI-Public/mcp-server-circleci (80 stars, TypeScript, official, 14 tools, flaky test detection)
   - GitHub Actions: via github/github-mcp-server (27.9k stars, Go, Actions toolset)
   - Argo CD: akuity/argocd-mcp (350 stars, TypeScript, 12 tools, GitOps deployment)
   - Buildkite: buildkite/buildkite-mcp-server (48 stars, Go, official)
   - Azure DevOps: Tiberriver256/mcp-server-azure-devops (347 stars, TypeScript, 20+ tools)
   - GitLab: Built-in MCP server (platform feature)
   - Also: Woodpecker CI, Tekton
   - 15+ servers across 9+ CI/CD platforms, Rating: 4/5

4. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "CI/CD pipeline" row to summary table
   - Updated review count to 197

5. **Built site** (217 pages, 138ms). Deploy pending — throttle applies.

### What should happen next
- **Run 235:** Deploy site. Prepare Blue Sky batch 3 (new posts beyond initial 6).
- **Future:** Set up 30-day content refresh workflow, favicon, newsletter, affiliate links
- **Content ideas:** Annotation & Data Labeling MCP servers, Digital Twin / BIM MCP servers, Workflow Automation MCP servers, Terraform/IaC MCP servers (separate from CI/CD)

## Run 233 — 2026-03-17 — Deploy + Blue Sky Setup + Content (Graph Database MCP Servers)

**Mode:** Developer + Copywriter + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 195 reviews (Run 232 build) now live at chatforest.com.

2. **Set up Blue Sky publishing infrastructure:**
   - Created `social/bluesky/` directory with posting script (`post_to_bluesky.sh`) using AT Protocol
   - Updated Blue Sky profile: display name "ChatForest", bio with site description, restored avatar image
   - Created `posts.md` tracker with 6 prepared promotional posts (batches of 3)

3. **Published first Blue Sky posts (batch 1, posts 001-003):**
   - 001 Filesystem MCP Server → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh77nzjkxa2i
   - 002 GitHub MCP Server → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh77oahjbl2o
   - 003 Brave Search MCP Server → at://did:plc:gknkcind5xg62bqekgu7qx4b/app.bsky.feed.post/3mh77ogrseh2i
   - All posts include link card embeds to chatforest.com reviews

4. **Wrote new review: Graph Database MCP Servers** (`content/reviews/graph-database-mcp-servers.md`) — 196th review.
   - Neo4j: neo4j/mcp (188 stars, Go, official, 3+ tools), neo4j-contrib/mcp-neo4j (853 stars, Python, Labs, GraphRAG + knowledge graph memory)
   - Amazon Neptune: awslabs/mcp (official AWS, openCypher + Gremlin, 3 tools)
   - TigerGraph: TigerGraph-DevLabs/tigergraph-mcp (official, 34 tools — highest dedicated server count)
   - Dgraph: Built-in MCP in v25+ (zero-install), plus community standalone
   - FalkorDB: FalkorDB-MCPServer (31 stars, Redis-based graph, official)
   - Memgraph: mcp-memgraph (official, ~10 tools, built-in PageRank/centrality/vector search)
   - ArangoDB: PCfVW/mcp-arangodb-async (46 tools — highest overall), ravenwits/mcp-server-arangodb (37 stars)
   - Also: Apache AGE (PostgreSQL graph), ArcadeDB (built-in MCP), Ontotext GraphDB (SPARQL/RDF)
   - 15+ servers across 10+ graph databases, Rating: 3.5/5

5. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Graph database" row to summary table
   - Updated review count to 196

6. **Built site** (216 pages, 140ms). Deploy pending — throttle applies.

### What should happen next
- **Run 234:** Deploy site. Publish Blue Sky batch 2 (posts 004-006).
- **Future:** Prepare more Blue Sky posts (beyond initial 6), set up 30-day content refresh workflow, favicon, newsletter, affiliate links
- **Content ideas:** Annotation & Data Labeling MCP servers, Digital Twin / BIM MCP servers, Workflow Automation MCP servers, CI/CD Pipeline MCP servers

## Run 232 — 2026-03-17 — Deploy + Social Publishing + Content (Redis MCP Servers)

**Mode:** Developer + Copywriter + Researcher

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 194 reviews (Run 231 build) now live at chatforest.com.

2. **Published social posts (dev.to 005+006):**
   - 005 Docker MCP Server → https://dev.to/grove_chatforest/the-docker-mcp-server-your-ai-agents-container-workshop-l5l
   - 006 Sentry MCP Server → https://dev.to/grove_chatforest/the-sentry-mcp-server-debug-production-errors-without-leaving-your-editor-2bel

3. **Published social posts (Hashnode 005+006):**
   - 005 Docker MCP Server → https://chatforest.hashnode.dev/docker-mcp-server-review
   - 006 Sentry MCP Server → https://chatforest.hashnode.dev/sentry-mcp-server-review
   - All 6/6 articles now published on both platforms. `.current_social_task` updated to 140 (Blue Sky next).

4. **Wrote new review: Redis MCP Servers** (`content/reviews/redis-mcp-servers.md`) — 195th review.
   - Official: redis/mcp-redis (454 stars, Python, 25+ tools across 11 modules — strings, hashes, lists, sets, sorted sets, JSON, streams, pub/sub, vector search/RAG, server management, docs search)
   - Agent Memory: redis/agent-memory-server (203 stars, two-tier semantic memory — working memory + long-term vector storage, 7 tools, multi-LLM via LiteLLM)
   - Cloud Infra: redis/mcp-redis-cloud (39 stars, TypeScript, 13 tools — subscription/database/plan management for Redis Cloud)
   - Community: GongRzhe/REDIS-MCP-Server (31 stars, archived), prajwalnayak7/mcp-server-redis (25 stars, 11 tools + MCP Resources), farhankaz/redis-mcp (6 stars, 14 tools), yyue9527/redis-mcp-server (2 stars, Spring Boot/SSE), redis/redis-mcp-java (2 stars, Java library)
   - 10+ servers across 3 official + community alternatives, Rating: 4/5

5. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Redis" row to summary table
   - Updated review count to 195

6. **Built site** (215 pages, 139ms). Deploy pending — throttle applies.

### What should happen next
- **Run 233:** Deploy site. Set up Blue Sky account/publishing (`.current_social_task` = 140).
- **Future:** Set up 30-day content refresh workflow (Jikan todo), favicon, newsletter, affiliate links
- **Content ideas:** Annotation & Data Labeling MCP servers (thin — may need to wait), Elasticsearch/OpenSearch MCP servers, Neo4j/Graph Database MCP servers, Digital Twin / BIM MCP servers

## Run 231 — 2026-03-16 — Deploy + Content (Robotics & IoT MCP Servers)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 193 reviews (Run 230 build) now live at chatforest.com.

2. **Wrote new review: Robotics & IoT MCP Servers** (`content/reviews/robotics-iot-mcp-servers.md`) — 194th review.
   - Robot control (ROS): robotmcp/ros-mcp-server (969 stars, bidirectional ROS1/ROS2), lpigeon/ros-mcp-server (873 stars), kakimochi/ros2-mcp-server (70 stars), rosbridge-mcp-server (WebSocket)
   - Smart home: ha-mcp (1.1K stars, 80+ tools), Home Assistant official MCP integration (built-in 2025.2+), homeassistant-mcp (500+ stars, SSE), jordy33/iot_mcp_server
   - Hardware/embedded: ChotuRobo (74 stars, Arduino ESP32/Nano), mcp2serial (35 stars, Raspberry Pi Pico), UnitApi (HAL + GPIO), mcp2tcp
   - Robot simulation: Isaac Sim MCP (NVIDIA, Franka/JetBot/Carter/G1/Go1)
   - IoT/industrial: mqtt-mcp (FastMCP 2.0), IoT-Edge-MCP-Server (SCADA/PLC/Modbus), AWS IoT SiteWise MCP, Coreflux MQTT MCP, EMQX MCP
   - 15+ servers across 5 subcategories, Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Robotics / IoT" row to summary table
   - Updated review count to 194

4. **Built site** (214 pages, 137ms). Deploy pending — throttle applies.

### What should happen next
- **Run 232:** Deploy site. On 2026-03-17: publish dev.to 005+006 and Hashnode 005+006 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links
- **Content ideas:** Annotation & Data Labeling MCP servers, Google Search Console MCP servers, Digital Twin / BIM MCP servers

## Run 230 — 2026-03-16 — Deploy + Content (LLM Observability & MLOps Pipeline MCP Servers)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 192 reviews (Runs 227-229 builds) now live at chatforest.com.

2. **Wrote new review: LLM Observability & MLOps Pipeline MCP Servers** (`content/reviews/llm-observability-mlops-pipeline-mcp-servers.md`) — 193rd review.
   - LLM observability platforms: Opik MCP (200 stars, TypeScript, modular toolsets — core/integration/expert-prompts/traces/projects/metrics), LangSmith MCP (89 stars, Python, 15+ tools, LangChain ecosystem), Helicone MCP (gateway + observability querying, 100+ models)
   - Distributed tracing: OpenTelemetry MCP (175 stars, Python, 10 tools — vendor-neutral Jaeger/Tempo/Traceloop, LLM-specific OpenLLMetry semantics)
   - Prompt management: Langfuse MCP (158 stars, TypeScript, built into Langfuse at /api/public/mcp)
   - ML pipeline orchestration: ZenML MCP (43 stars, Python, 30+ tools — trigger deployments, query runs, interactive dashboard apps)
   - Experiment tracking: Comet MCP (1 star, Python, 10 tools, built-in OTel instrumentation), cross-referenced W&B (41 stars) and MLflow (3 stars) from AI/ML review
   - 10+ servers across 5 subcategories, Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "LLM observability / MLOps pipeline" row to summary table
   - Updated review count to 193

4. **Built site** (213 pages, 139ms). Deploy pending — throttle applies.

### What should happen next
- **Run 231:** Deploy site. On 2026-03-17: publish dev.to 005+006 and Hashnode 005+006 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links
- **Content ideas:** Annotation & Data Labeling MCP servers (thin — may need to wait for ecosystem growth), Google Search Console MCP servers (if distinct from SEO review), Robotics/IoT MCP servers

## Run 229 — 2026-03-16 — Content (AI Agent Orchestration MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: AI Agent Orchestration MCP Servers** (`content/reviews/agent-orchestration-mcp-servers.md`) — 192nd review.
   - Agent frameworks: mcp-agent by LastMile AI (8.1K stars, composable Anthropic patterns — parallel, orchestrator, evaluator-optimizer, router, map-reduce), fast-agent (3.7K stars, chain/parallel/MAKER voting, full MCP support), Agent-MCP (1.2K stars, multi-agent parallel + persistent knowledge graph)
   - Multi-agent swarms: Ruflo (21.1K stars, 60+ agents, 215 MCP tools, v3.5.0 production release), AWS CLI Agent Orchestrator (hierarchical supervisor → workers in tmux)
   - Task orchestration: jpicklyk/task-orchestrator (170 stars, Kotlin, work item graph with quality gates, 13 tools), EchoingVesper/mcp-task-orchestrator (24 stars, specialist roles — Architect/Implementer/Tester/Reviewer)
   - MCP gateway/routing: ultimate_mcp_server (143 stars, kitchen-sink multi-provider server), mcp-agentify (LLM-powered routing), mcp-gateway-registry (enterprise OAuth + A2A registry)
   - Protocol bridges: A2A-MCP-Server (145 stars, bridges MCP ↔ Google A2A protocol, archived)
   - 15+ servers across 5 subcategories, Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Agent orchestration" row to summary table
   - Updated review count to 192

3. **Built site** (212 pages, 141ms). Deploy pending — throttle applies (~38 min remaining).

### What should happen next
- **Run 230:** Deploy site. On 2026-03-17: publish dev.to 005+006 and Hashnode 005+006 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links
- **Content ideas:** Google Search Console MCP servers (if distinct from SEO review), Annotation & Data Labeling MCP servers, ML Ops & Experiment Tracking MCP servers

## Run 228 — 2026-03-16 — Content (LLM Evaluation & Benchmarking MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: LLM Evaluation & Benchmarking MCP Servers** (`content/reviews/llm-evaluation-benchmarking-mcp-servers.md`) — 191st review.
   - LLM output eval frameworks: promptfoo (10.8K stars, CLI + red-teaming + CI/CD), DeepEval (5K+ stars, Pytest-style, 50+ metrics, MCP-Use metric), Atla MCP (LLM-as-a-judge via Selene models)
   - MCP server benchmarks: Accenture/mcp-bench (401 stars, 28 servers, 250 tools), modelscope/MCPBench (227 stars, accuracy/latency/token), SalesforceAIResearch/MCP-Universe (11 servers, 231 tasks, GPT-5 only 43.72%)
   - AI security/red-teaming: promptfoo/evil-mcp-server (attack simulation), mcp-agent-provider (test agent behavior with malicious servers)
   - Local LLM benchmarking: MetriLLM (Geekbench for LLMs, 14 prompts, 6 categories), llm-api-benchmark-mcp-server (Go, throughput/TTFT)
   - MCP server testing: lastmile-ai/mcp-eval (lightweight CI/CD eval), mcp-server-tester (Claude AI-generated test cases)
   - 15+ servers across 5 subcategories, Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "LLM evaluation / benchmarking" row to summary table
   - Updated review count to 191

3. **Built site** (211 pages, 136ms). Deploy pending — throttle applies (~47 min remaining from Run 227 deploy).

### What should happen next
- **Run 229:** Deploy site. On 2026-03-17: publish dev.to 005+006 and Hashnode 005+006 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links
- **Content ideas:** Video Generation MCP servers, Google Search Console MCP servers, Robotics/IoT MCP servers

## Run 227 — 2026-03-16 — Deploy + Content (Prompt Engineering & Optimization MCP Servers)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- **#180 (Rob):** Confirmed byline format from #178 looks correct; asked us to update processes to handle new byline going forward. Marked as seen. Already handled — all new reviews include byline.

### What I did

1. **Deployed site** to DreamHost — all 189 reviews (Runs 225-226 builds) now live.

2. **Wrote new review: Prompt Engineering & Optimization MCP Servers** (`content/reviews/prompt-engineering-optimization-mcp-servers.md`) — 190th review.
   - Multi-LLM routing: just-prompt (718 stars, 6 providers, consensus tool)
   - Workflow/template engines: claude-prompts (143 stars, AGPL-3.0, reasoning frameworks, skill export), mcp-prompts (110 stars, 3 storage backends, RBAC), langfuse MCP (158 stars, observability bridge), mcp-prompt-templates (21 stars), smart-prompts-mcp (13 stars, archived)
   - Automated optimization: mcp-prompt-optimizer (22 stars, 14 techniques: ToT, APE, Medprompt), prompt-engineer-mcp-server (13 stars, Claude-powered), prompt-auto-optimizer-mcp (3 stars, GEPA/evolutionary), prompt-learning-mcp (1 star, APE/OPRO/DSPy), Nouman159 (0 stars, deterministic)
   - Claude Code-specific: cc_peng_mcp (13 stars, 3 tools), prompt-gen-mcp (4 stars, code-context-aware)
   - Structured frameworks: risen-prompts-mcp (1 star, RISEN framework, 8 tools)
   - 20+ servers across 5 subcategories, Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Prompt engineering / optimization" row to summary table
   - Updated review count to 190

4. **Built site** (210 pages, 141ms). Deploy pending — throttle applies.

### What should happen next
- **Run 228:** Deploy site. On 2026-03-17: publish dev.to 005+006 and Hashnode 005+006 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links
- **Content ideas:** LLM Evaluation & Testing Frameworks MCP servers, Video Generation MCP servers, Google Search Console MCP servers

## Run 226 — 2026-03-16 — Content (Debugging MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Debugging MCP Servers** (`content/reviews/debugging-mcp-servers.md`) — 189th review.
   - Chrome DevTools MCP (29.3K stars, 25+ tools) — full browser control, automation, performance, network
   - VS Code debugging (3 servers): claude-debugs-for-you (496 stars), microsoft/DebugMCP (221 stars, 13 tools, 8+ languages), workbackai/mcp-nodejs-debugger (303 stars, archived)
   - Multi-language DAP: debugmcp/mcp-debugger (85 stars, Python/JS/Rust/Go/Java)
   - Python: mcp-pdb (45 stars, pdb wrapper)
   - Native binary (5+ servers): lldb-mcp (85 stars), mcp_server_gdb (62 stars, Rust), MDB-MCP (56 stars, GDB+LLDB), debugger-mcp-server (WinDbg/.NET), gdb-mcp
   - Embedded: embedded-debugger-mcp (56 stars, ARM Cortex-M/RISC-V, 22 tools)
   - Xcode/iOS: XcodeBuildMCP (4.8K stars)
   - MCP Inspector (9.1K stars) — official server testing tool
   - Node.js DevTools Protocol: devtools-debugger-mcp (340 stars)
   - 25+ servers across 7 subcategories, Rating: 4.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Debugging" row to summary table
   - Updated review count to 189

3. **Built site** (209 pages, 136ms). Deploy pending — throttle applies (~30 min remaining).

### What should happen next
- **Run 227:** Deploy site. On 2026-03-17: publish dev.to 005+006 and Hashnode 005+006 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links
- **Content ideas:** Prompt Engineering MCP servers, Testing/QA MCP servers (if not already done), Debugging tools guide

## Run 225 — 2026-03-16 — Content (Image Generation MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Researched email MCP servers** — found 40+ servers but determined we already have extensive coverage (dedicated Gmail, Outlook, Notification/Email Delivery, and Marketing Automation reviews). Pivoted to Image Generation instead.

2. **Wrote new review: Image Generation MCP Servers** (`content/reviews/image-generation-mcp-servers.md`) — 188th review.
   - ComfyUI (4 servers): joenorton/comfyui-mcp-server (224 stars, 18+ tools, auto-discovered workflows), shawnrushefsky (40+ tools, 70+ workflows), artokun (31 tools, 3 autonomous agents), IO-AtelierTech (30+ tools)
   - Stability AI / Stable Diffusion (4 servers): tadasant/mcp-server-stability-ai (81 stars, 11 chainable tools), Ichigo3766 (SD WebUI), boxi-rgb (SD WebUI), mkm29 (Go)
   - DALL-E / OpenAI (6 servers): spartanz51/imagegen-mcp (33 stars, DALL-E 2/3/gpt-image-1), Garoth/dalle-mcp, Azure bridge, 3 more
   - Flux (6 servers): GongRzhe (50 stars, Replicate), jmanhype/mcp-flux-studio (24 stars, Pro/Ultra/Dev), tehw0lf (local GPU)
   - Google Gemini/Imagen (3+ servers): shinpr/mcp-image (82 stars, auto-prompt optimization), lansespirit (multi-provider), qhdrl12
   - Replicate (3 servers): deepfates (93 stars, deprecated — official MCP now), gerred, gomcpgo
   - fal.ai (3+ servers): am0y/mcp-fal (76 stars), raveenb (38 stars, 600+ models, cost tracking)
   - Midjourney (3 servers): all use unofficial API proxies (GPTNB, AceDataCloud)
   - Together AI (3+ servers), Ideogram (2+ servers), Leonardo AI (1 server)
   - Multi-provider (4+ servers): piapi-mcp-server (68 stars, Midjourney/Flux/Kling/Luma/Suno)
   - Gaps: no Adobe Firefly, no Canva AI, limited inpainting outside ComfyUI, no image-to-3D pipelines
   - 50+ servers across 12 subcategories, Rating: 4.0/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Image generation" row to summary table
   - Updated review count to 188

4. **Built site** (208 pages, 139ms). Deploy pending — throttle applies (~40 min remaining).

### What should happen next
- **Run 226:** Deploy site. On 2026-03-17: publish dev.to 005+006 and Hashnode 005+006 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links
- **Content ideas:** Debugging MCP servers, Prompt Engineering MCP servers, CI/CD MCP servers, Testing/QA MCP servers

## Run 224 — 2026-03-16 — Deploy + Content (Note-Taking & Knowledge Management MCP Servers)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** to DreamHost — all 185 reviews with LLM bylines now live, including byline updates from Runs 222-223.

2. **Wrote new review: Note-Taking & Knowledge Management MCP Servers** (`content/reviews/note-taking-knowledge-management-mcp-servers.md`) — 187th review.
   - Obsidian (8 servers): references our dedicated review, three architectures summary
   - Notion: references our dedicated review, official server with 20+ tools
   - Apple Notes (2+ servers): mcp-apple-notes (RAG + semantic search via MiniLM-L6-v2), apple-notes-mcp (SQLite direct)
   - Evernote (2+ servers): evernote-mcp-server (Claude Desktop), mcp-evernote (CRUD + sync)
   - Joplin: joplin-mcp (FastMCP, Python API)
   - Roam Research: roam-research-mcp (comprehensive graph API)
   - Logseq: mcp-pkm-logseq (customizable instructions)
   - Tana (2 servers): tana-mcp (Desktop API bridge), tana-codemode (code mode)
   - Capacities: capacities-mcp (spaces, search, daily notes)
   - Knowledge Graphs: official Memory server (JSONL), Memento MCP (Neo4j + vector), Engram (hybrid BM25 + ColBERT + knowledge graph), knowledgegraph-mcp (PostgreSQL/SQLite)
   - Gaps: no Bear Notes, no Anytype, no Dendron/Foam, no cross-platform unified search, limited write access
   - 40+ servers across 10 subcategories, Rating: 4.0/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Note-taking / knowledge management" row to summary table
   - Updated review count to 187

4. **Built site** (207 pages, 136ms). Deploy pending — throttle applies.

### What should happen next
- **Run 225:** Deploy site. On 2026-03-17: publish dev.to 005+006 and Hashnode 005+006 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links
- **Content ideas:** Tried gardening/horticulture but too thin (only VeggieTools + WeMush). Better candidates: Email MCP servers, Image Generation MCP servers, Debugging MCP servers, Prompt Engineering MCP servers

## Run 223 — 2026-03-16 — Cross-Platform Byline Sync (Phase 2 & 3)

**Mode:** Developer

### Inbox update
- **#178 (self):** My plan sent to Rob re: byline rollout phases. Marked as seen. No new messages from Rob.

### What I did

1. **Updated 4 published dev.to articles with LLM byline** (Phase 2)
   - Articles 001-004 (IDs: 3351860, 3351862, 3351905, 3351906) updated via PUT to dev.to API
   - Each article now ends with: *This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
   - Created reusable script at `scripts/update_devto_articles.py`

2. **Updated 4 published Hashnode articles with LLM byline** (Phase 3)
   - Articles 001-004 updated via Hashnode GraphQL `updatePost` mutation
   - Same byline format applied
   - Created reusable script at `scripts/update_hashnode_articles.py`

3. **Deploy pending** — throttle not yet cleared at commit time. Site was built in Run 222 with all 185 reviews having the byline.

### What should happen next
- **Run 224:** Deploy site (throttle will be cleared). Publish dev.to 005+006 and Hashnode 005+006 on 2026-03-17 per schedule.
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links

## Run 222 — 2026-03-16 — Byline Standardization (LLM Attribution)

**Mode:** Developer

### Inbox update
- **#177 (Rob):** Approved byline format from #174. Wants systematic plan to update every article on all platforms, sees this as practice for 30-day content refresh cycles. Replied with plan as #178.

### What I did

1. **Added LLM attribution byline to all 185 reviews** on chatforest.com
   - Approved format: *This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
   - Appended as the final line of every review file
   - Preserved all existing footer content (varied across ~12 patterns)
   - Created reusable script at `scripts/add_llm_byline.py` for future batch updates

2. **Updated all 12 cross-post drafts** (6 dev.to + 6 Hashnode) with the same byline

3. **Built site** (206 pages, 135ms). Deploy pending — throttle not yet cleared (~22 min remaining at commit time).

4. **Sent plan to Rob** (#178) outlining:
   - Phase 1: chatforest.com (done this run)
   - Phase 2: dev.to published articles via API (next run)
   - Phase 3: Hashnode published articles via GraphQL API (next run)
   - Phase 4: Ongoing 30-day refresh process

### What should happen next
- **Run 223:** Deploy site. Update published dev.to articles (001-004) via API with new byline. Update published Hashnode articles (001-004) via GraphQL API.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006 (these now include byline)
- **Future:** Set up 30-day content refresh workflow (Jikan todo), Blue Sky setup, favicon, newsletter, affiliate links

## Run 221 — 2026-03-16 — Content (Fitness & Wearables MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages. Still awaiting Rob's reply on: #174 (byline format), #175 (Blue Sky acknowledged)

### What I did

1. **Wrote new review: Fitness & Wearables MCP Servers** (`content/reviews/fitness-wearables-mcp-servers.md`) — 186th review.
   - Strava (7+ servers): r-huijts/strava-mcp (TypeScript — zero-install npx), eddmann/strava-mcp (TypeScript — 24 tools, activities/segments/routes/training), gcoombe/strava-mcp (all major endpoints), MariyaFilippova/mcp-strava (Claude Desktop), kw510/strava-mcp (Cloudflare Workers, remote OAuth), tomekkorbak/strava-mcp-server (Python), yorrickjansen/strava-mcp (Python)
   - Garmin (5+ servers): Taxuspt/garmin_mcp (Python — 96+ tools, ~89% of python-garminconnect), Nicolasvegam/garmin-connect-mcp (Python — 61 tools, 7 categories), eddmann/garmin-connect-mcp (22 tools, 8 categories), jlwainwright/garmin-mcp-server, eversonl/garmin-health-mcp-server
   - WHOOP (6+ servers): nissand/whoop-mcp-server-claude (TypeScript — 18+ endpoints, full OAuth), JedPattersonn/whoop-mcp, ctvidic/whoop-mcp-server, elizabethtrykin/whoop-mcp, k0va1/whoop-mcp (Ruby), xokvictor/whoop-mcp (Go)
   - Apple Health & Open Wearables: the-momentum/apple-health-mcp-server (915 stars, Python — unified platform for 6 wearable ecosystems, companion app, DuckDB backend)
   - Oura Ring (4+ servers): hemantkamalakar/oura-mcp-server (20 tools, anomaly detection, trend prediction), elizabethtrykin/oura-mcp, meimakes/oura-mcp-server, rajvirtual/oura-mcp-server
   - Fitbit (2+ servers): TheDigitalNinja/mcp-fitbit (exercise, sleep, weight, heart rate, nutrition), NitayRabi/fitbit-mcp
   - Training platforms (3+ servers): ai-endurance/mcp (remote MCP, ML race predictions, 20+ tools), Milofax/xert-mcp (cycling fitness signature), Dinesh-Satram/fitness_coach_MCP
   - Multi-platform: Async-IO/pierre_mcp_server (Strava/Garmin/Fitbit/WHOOP/COROS, 150+ wearables via Terra, MCP + A2A + REST), Juxsta/wger-mcp (open-source wger platform)
   - Nutrition: ai-mcp-garage/mcp-myfitnesspal (calories, macros, meals), AdamWalt/myfitnesspal-mcp-python
   - Smart health devices: elizabethtrykin/8sleep-mcp (Eight Sleep Pod), schimmmi/withings-mcp-server, akutishevsky/withings-mcp, Dhivakarkd/corus-mcp (COROS)
   - Gaps: no Peloton, no Zwift, no Apple Watch direct, no Google Fit standalone, no Amazfit/Xiaomi, no standardized health data format
   - 40+ servers across 8 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Fitness / wearables" row to summary table
   - Updated review count to 186

3. **Built site** (206 pages, 132ms). Deploy pending — throttle not yet cleared (~30 min remaining).

### What should happen next
- **Run 222:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Gardening/Horticulture, Waste Management, Insurance/InsurTech, Construction/BIM
- **Awaiting Rob's reply on:** #174 (byline format), #175 (Blue Sky acknowledged)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Implement byline attribution once Rob approves format, Blue Sky setup, favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 220 — 2026-03-16 — Content (Advertising & Ad-Tech MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages. Still awaiting Rob's reply on: #174 (byline format), #175 (Blue Sky acknowledged)

### What I did

1. **Wrote new review: Advertising & Ad-Tech MCP Servers** (`content/reviews/advertising-ad-tech-mcp-servers.md`) — 185th review.
   - Google Ads (8+ servers): cohnen/mcp-google-ads (459 stars, Python, MIT — 5 tools, GAQL queries, community favorite), googleads/google-ads-mcp (286 stars, Python, Apache-2.0 — official, 2 tools, read-only), google-marketing-solutions/google_ads_mcp (130 stars, Python), gomarble-ai/google-ads-mcp-server (106 stars, keyword planner), promobase/google-ads-mcp (12 stars, 89 API services), grantweston/google-ads-mcp-complete (12 stars, 45+ tools), bjorndavidhansen/google-ads-mcp-server (17 stars, Docker/K8s deployment), DigitalRocket-biz/google-ads-mcp-v20 (9 stars, PMax negative keywords)
   - Meta/Facebook Ads (3+ servers): pipeboard-co/meta-ads-mcp (631 stars, Python — 25 tools, full CRUD, targeting search, most popular ad-tech MCP server), gomarble-ai/facebook-ads-mcp-server (254 stars, Python, MIT — 23 tools, change history), gabe-almeida/meta-ads-mcp-server (3 stars, TypeScript — audience management, conversion tracking)
   - TikTok Ads (2+ servers): AdsMCP/tiktok-ads-mcp-server (23 stars, Python, MIT — 10 tools), ysntony/tiktok-ads-mcp (18 stars, read-only, multi-advertiser)
   - Multi-platform (2+ servers): amekala/ads-mcp (19 stars — 100+ tools, 4 platforms, strategy persistence), jshorwitz/synter-mcp-server (8 stars, MIT — 140+ tools, 9 platforms, AI creative generation)
   - Protocol: adcontextprotocol/adcp (193 stars, Apache-2.0 — open standard for AI-driven ad operations)
   - Auditing: AgriciDaniel/claude-ads (981 stars, MIT — 190+ audit checks, Claude Code skill, not MCP server)
   - Gaps: no Amazon Ads dedicated MCP, no Pinterest/Snapchat Ads, limited programmatic DSP, no attribution tools
   - 30+ servers across 6 subcategories, Rating: 4.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Advertising / ad-tech" row to summary table
   - Updated review count to 185

3. **Built site** (205 pages, 134ms). Deploy pending — throttle not yet cleared (~37 min remaining).

### What should happen next
- **Run 221:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Gardening/Horticulture, Waste Management, Wearables/Fitness Trackers, Insurance/InsurTech
- **Awaiting Rob's reply on:** #174 (byline format), #175 (Blue Sky acknowledged)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Implement byline attribution once Rob approves format, Blue Sky setup, favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 219 — 2026-03-16 — Content (SEO & Search Optimization MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages. Still awaiting Rob's reply on: #174 (byline format), #175 (Blue Sky acknowledged)

### What I did

1. **Attempted maritime/shipping review but found it already covered** in `logistics-supply-chain-mcp-servers.md` and `supply-chain-logistics-mcp-servers.md`. Pivoted to SEO & Search Optimization.

2. **Wrote new review: SEO & Search Optimization MCP Servers** (`content/reviews/seo-search-optimization-mcp-servers.md`) — 184th review.
   - Google Search Console (3+ servers): AminForou/mcp-gsc (428 stars, Python — 19 tools, search analytics, URL inspection, sitemaps, cannibalization detection, v0.2.1 March 2026), ahonn/mcp-server-gsc (157 stars, TypeScript, MIT — 25K row extraction, regex filtering, quick wins detection)
   - All-in-one SEO platforms (8+ servers): ahrefs/ahrefs-mcp-server (94 stars, official — pivoted to remote OAuth), dataforseo/mcp-server-typescript (150 stars, TypeScript, official — SERP/keywords/on-page/labs, hundreds of tools), seranking/seo-data-api-mcp-server (Node.js, official — keyword research, domain analysis, backlinks, audits, rank tracking), cnych/seo-mcp (165 stars, Python — free Ahrefs scraper with CAPTCHA solving), mrkooblu/semrush-mcp (25 stars, TypeScript — 18 tools), metehan777/semrush-mcp (9 stars, Node.js — 7 tools), Skobyn/dataforseo-mcp-server (47 stars, TypeScript — community DataForSEO)
   - Keyword research (2+ servers): hithereiamaliff/mcp-keywords-everywhere (TypeScript, MIT — volume, CPC, competition, multi-country), SEO-Review-Tools/SEO-API-MCP (Node.js)
   - PageSpeed & technical SEO (3+ servers): ruslanlap/pagespeed-insights-mcp (33 stars), adamsilverstein/lighthouse-mcp-server, ncosentino/google-psi-mcp
   - Gaps: no Moz, no Screaming Frog, no Google Trends, no schema validators, no Bing Webmaster Tools, no local SEO/GMB, no content optimization (Clearscope/SurferSEO)
   - 20+ servers across 4 subcategories, Rating: 4/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "SEO / search optimization" row to summary table
   - Updated review count to 184

4. **Built site** (204 pages, 134ms). Deploy pending — throttle not yet cleared (~45 min remaining).

### What should happen next
- **Run 220:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Advertising/Ad-Tech, Gardening/Horticulture, Waste Management, Wearables/Fitness Trackers
- **Awaiting Rob's reply on:** #174 (byline format), #175 (Blue Sky acknowledged)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Implement byline attribution once Rob approves format, Blue Sky setup, favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 218 — 2026-03-16 — Content (Astronomy & Space Science MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages. Still awaiting Rob's reply on: #174 (byline format), #175 (Blue Sky acknowledged)

### What I did

1. **Wrote new review: Astronomy & Space Science MCP Servers** (`content/reviews/astronomy-space-science-mcp-servers.md`) — 183rd review.
   - NASA APIs (3 servers): ProgramComputer/NASA-MCP-server (81 stars, TypeScript, ISC — 20+ data sources: APOD, Mars Rover, NEO, DONKI, Exoplanet Archive, JPL Small-Body Database, GIBS, FIRMS, and more), jezweb/nasa-mcp-server (8 stars, Python — APOD, Mars rovers, asteroids, media library, smart multi-tier caching), AnCode666/nasa-mcp (6 stars, Python, MIT — APOD, NEO, DONKI space weather, Earth imagery, EPIC, Exoplanet Archive)
   - Astronomical data & research (3 servers): SandyYuan/astro_mcp (3 stars, Python — 40+ services via astroquery, DESI, SIMBAD, VizieR, SDSS, Gaia, MAST), SandyYuan/astro-orchestra (1 star, Python, MIT — multi-agent research system with 5 specialized agents), prtc/nasa-ads-mcp (2 stars, Python, MIT — 10 tools, NASA ADS paper search, citations, BibTeX)
   - Celestial positioning (1 server): Rkm1999/CelestialMCP (1 star, TypeScript, MIT — 3 tools, 117k+ stars, 14k deep-sky objects, star-hopping paths)
   - Satellite tracking (1 server): Cyreslab-AI/satellitetracking-mcp-server (3 stars, TypeScript, MIT — 6 tools, N2YO API, 31 categories)
   - Gaps: no Stellarium, no JWST, no telescope control (ASCOM/INDI), no aurora alerts, no SpaceX/launch schedules, no radio astronomy, no LIGO data
   - 12+ servers across 4 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Astronomy / space science" row to summary table
   - Updated review count to 183

3. **Built site** (203 pages, 135ms). Deploy pending — throttle not yet cleared (~54 min remaining).

### What should happen next
- **Run 219:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Maritime/Shipping, Mining/Natural Resources, Construction/BIM, Archaeology/Cultural Heritage, Dental/Optometry
- **Awaiting Rob's reply on:** #174 (byline format), #175 (Blue Sky acknowledged)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Implement byline attribution once Rob approves format, Blue Sky setup, favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 217 — 2026-03-16 — Content (Job Search & Career MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages. Still awaiting Rob's reply on: #174 (byline format), #175 (Blue Sky acknowledged)

### What I did

1. **Wrote new review: Job Search & Career MCP Servers** (`content/reviews/job-search-career-mcp-servers.md`) — 182nd review.
   - LinkedIn integration (8+ servers): stickerdaniel/linkedin-mcp-server (TypeScript — profile/company/job scraping, browser auth), eliasbiondo/linkedin-mcp-server (TypeScript — structured JSON extraction), Hritik003/linkedin-mcp (Python — job application automation), adhikasp/mcp-linkedin (Python — feeds and job API), GhoshSrinjoy/linkedin-job-mcp (Node.js — filtering, geocoding, caching), Rayyan9477/linkedin_mcp, superyuser/linkedin-scraper-mcp, zarif007/linkedin-job-search
   - Multi-platform job search (4+ servers): borgius/jobspy-mcp-server (Python — Indeed/LinkedIn/Glassdoor/ZipRecruiter), Indeed official MCP server, Ritesh-sudo/MCPJobSearch, Bright Data Indeed MCP
   - Resume & application (3+ servers): Sakshee5/JobApply (Python — resume tailoring, cover letters, local, MIT), plus LinkedIn-integrated tools
   - Interview prep (4+ servers): HelloGGX/interview-mcp-server (resume analysis, recording evaluation), ejb503/interview-roleplay (dynamic scenarios), InterviewReady/mcp-server (course materials), MichaelJGKopp/MCP-CRUD-Interview-Question (Spring AI)
   - Gaps: no Glassdoor salary data, no freelance platforms (Upwork/Fiverr), no networking tools, no career path planning, no skills assessment, no remote job boards
   - 20+ servers across 4 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Job search / career" row to summary table
   - Updated review count to 182

3. **Built site** (202 pages, 134ms). Deploy pending — throttle clearing shortly.

### What should happen next
- **Run 218:** Deploy if not done. Continue expanding coverage — potential categories: Maritime/Shipping, Archaeology/Cultural Heritage, Astronomy/Space Science, Construction/BIM, Mining/Natural Resources
- **Awaiting Rob's reply on:** #174 (byline format), #175 (Blue Sky acknowledged)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Implement byline attribution once Rob approves format, Blue Sky setup, favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 216 — 2026-03-16 — Content (Aviation & Flight MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages. Still awaiting Rob's reply on: #174 (byline format), #175 (Blue Sky acknowledged)

### What I did

1. **Attempted genealogy review but found it already exists** (`content/reviews/genealogy-family-history-mcp-servers.md` — comprehensive review from a prior run with 15+ servers, rated 3.5/5). Pivoted to a new category.

2. **Wrote new review: Aviation & Flight MCP Servers** (`content/reviews/aviation-flight-mcp-servers.md`) — 181st review.
   - Flight tracking (5 servers): sunsetcoder/flightradar24-mcp-server (46 stars, JavaScript — real-time FR24 tracking, emergency alerts), Flightradar24/fr24api-mcp (14 stars, TypeScript — official FR24 API, 13 tools, historic data back to 2016), Pradumnasaraf/aviationstack-mcp (17 stars, Python — 12 tools, schedules, aircraft types, reference data), sragss/flight-mcp (4 stars, JavaScript — ADS-B Exchange, military aircraft), variflight/variflight-mcp (22 stars, TypeScript — 7 tools, Chinese aviation, comfort index)
   - Flight search & booking (5+ servers): ravinahp/flights-mcp (169 stars, Python — Duffel API bookable fares, multi-city), donghyun-chae/mcp-amadeus (50 stars, Python — Amadeus GDS), arjunprabhulal/mcp-flight-search (40 stars, Python — SerpAPI Google Flights), manohar42/google-flights-mcp-server (9 tools, search + full Duffel booking workflow), shadyvb/mcp-skyscanner (reverse-engineered, experimental)
   - Aviation weather & pilot tools (2 servers): blevinstein/aviation-mcp (6 stars — METAR, TAF, PIREP, SIGMET, G-AIRMET, charts, NOTAMs from FAA), finack/aviation-mcp (4 tools, aviationweather.gov, route weather)
   - Gaps: no FlightAware, no OpenSky Network, no airline-specific servers, no TSA wait times, no baggage tracking, no flight simulator integration, no drone/UAV airspace
   - 15+ servers across 4 subcategories, Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Aviation / flight" row to summary table
   - Updated review count to 181

4. **Built site** (201 pages, 138ms). Deploy pending — throttle not yet cleared.

### What should happen next
- **Run 217:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Mining/Natural Resources, Maritime/Shipping, Dental/Optometry, Archaeology/Cultural Heritage, Home Improvement/DIY
- **Awaiting Rob's reply on:** #174 (byline format), #175 (Blue Sky acknowledged)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Implement byline attribution once Rob approves format, Blue Sky setup, favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 215 — 2026-03-16 — Content (Interior Design & Architecture MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Marked #174 and #175 (my own replies) as seen.
- Still awaiting Rob's reply on: #174 (byline format), #175 (Blue Sky acknowledged)

### What I did

1. **Wrote new review: Interior Design & Architecture MCP Servers** (`content/reviews/interior-design-architecture-mcp-servers.md`) — 180th review, one-hundred-sixtieth beyond original list.
   - Blender (1 dominant server): ahujasid/blender-mcp (17.6k stars, Python — 18+ tools, geometry nodes, Polyhaven/Sketchfab asset libraries, Hyper3D generation, viewport screenshots), seehiong/blender-mcp-n8n (45+ tools via n8n automation)
   - AutoCAD (4+ servers): puran-water/autocad-mcp (159 stars, Python — AutoLISP execution, 8 tools, 600+ P&ID symbols, ezdxf headless backend), AnCode666/multiCAD-mcp (46 tools, 4 CAD platforms), daobataotie/CAD-MCP (multi-CAD NLP), chichicaste/mcp-autocad-server (learning reference)
   - FreeCAD (5+ servers): proximile/FreeCAD-MCP (57 tools, Docker headless, Vision AI, TRELLIS.2 image-to-3D, Gradio UI), bonninr/freecad_mcp, lucygoodchild/freecad-mcp-server, spkane/freecad-addon-robust-mcp-server, contextform/freecad-mcp
   - SketchUp (2 servers): mhyrr/sketchup-mcp (182 stars, Ruby/Python — woodworking joints, component manipulation), BearNetwork-BRNKC/SketchUp-MCP
   - Rhino & Grasshopper (5+ servers): jingcheng-chen/rhinomcp (274 stars, Python — object/layer management, script execution), veoery/GH_mcp_server (GHPython generation), dongwoosuk/rhino-grasshopper-mcp (ML auto-layout), alfredatnycu/grasshopper-mcp (intent recognition), reer-ide/rhino_mcp
   - Revit/BIM (2+ servers): revit-mcp/revit-mcp (18 stars, C#/Python — CRUD on BIM elements, plugin architecture)
   - Fusion 360 (4+ servers): AuraFriday (thread-safe), mycelia1 (script gen+exec), Joe-Spencer (ADSK resources)
   - OpenSCAD (3+ servers): quellant/openscad-mcp (multi-perspective rendering, 300 tests), fboldo (STL+PNG), rahulgarg123
   - Specialized: cad-agent (build123d for 3D printing), mcp_3d_relief (image-to-STL)
   - Gaps: no room layout/furniture placement, no floor plan generators, no color palettes, no furniture catalogs (IKEA/Wayfair), no AR/VR, no rendering engines (V-Ray/Lumion), no landscape architecture, no building codes, no SolidWorks
   - 30+ servers across 7 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Interior design / architecture" row to summary table
   - Updated review count to 180

3. **Built site** (200 pages, 131ms). Deploy pending — throttle not yet cleared (~36 min since last deploy).

### What should happen next
- **Run 216:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Emergency/Disaster Response, Insurance/InsurTech, Logistics/Supply Chain (already have one?), Genealogy/Family History
- **Awaiting Rob's reply on:** #174 (byline format), #175 (Blue Sky acknowledged)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Implement byline attribution once Rob approves format, Blue Sky setup, favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 214 — 2026-03-16 — Content (Sports & Fitness Analytics MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **#172 (Rob):** Byline/LLM attribution discussion — Rob wants to keep "Grove" as author but add a footer noting the LLM model used. Replied with suggested format: "*This review was last edited on March 16, 2026 using Claude Opus 4.6 (Anthropic).*" Awaiting Rob's feedback before implementing. (Sent reply as #174)
- **#173 (Rob):** Blue Sky posting status — explained AT Protocol, current queue position (Hashnode next, then Blue Sky), and that I can handle setup myself. (Sent reply as #175)

### What I did

1. **Wrote new review: Sports & Fitness Analytics MCP Servers** (`content/reviews/sports-fitness-analytics-mcp-servers.md`) — 179th review, one-hundred-fifty-ninth beyond original list.
   - Multi-sport data (4 servers): michaelfromorg/mcp-sports (TypeScript — ESPN-based, NFL/NBA/MLB/NHL/NCAA/Premier League), SportDB.dev (free API + MCP, multi-sport), Apify ESPN MCP (12 tools, no API key needed), cloudbet/sports-mcp-server (10 stars, TypeScript — live odds, fuzzy search)
   - Formula 1 (6+ servers): rakeshgangwar/f1-mcp-server (7 stars, Python — FastF1, 7 tools, telemetry), Panth1823/formula1-mcp (TypeScript), stagsz/F1-MCP-Server (live timing + simulation), plus Machine-To-Machine, Darakhsh1999, AryaAkman, AbhiJ2706
   - Sports betting (3 servers): WFord26/BetTrack (Python — 30+ tools, 70+ markets, React dashboard), cloudbet (live market data), Apify sportsbook scraper
   - Strava & endurance (3+ servers): r-huijts/strava-mcp (238 stars, TypeScript — 24 tools, Strava API v3), plus 2 more implementations
   - Fitness & wearables (6+ servers): gesteves/domestique (TypeScript — Intervals.icu + Whoop + TrainerRoad, power/pace curves), Nicolasvegam/garmin-connect-mcp (61 tools!), Async-IO/pierre_mcp_server (150+ wearables via Terra), ai-endurance/mcp, ewongz/fitness-mcp-server (30+ sports), tomekkorbak/oura-mcp-server (37 stars)
   - Workout management (4+ servers): chrisdoc/hevy-mcp (Hevy app), Juxsta/wger-mcp (400+ exercises), workoutMakerMCP, fitness_coach_MCP
   - Niche sports (3+ servers): soccer-data, chess (multiple), cycling, AFL
   - Gaps: no tennis/golf/cricket/rugby, no fantasy league management, no sports video analysis, no Olympic data, no e-sports beyond odds
   - 25+ servers across 6 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Sports / fitness analytics" row to summary table
   - Updated review count to 179

3. **Built site** (199 pages, 132ms). Deploy pending — throttle not yet cleared.

### What should happen next
- **Run 215:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Interior Design/Architecture, Emergency/Disaster Response, Insurance/InsurTech, Logistics/Supply Chain
- **Awaiting Rob's reply on:** #174 (byline format), #175 (Blue Sky acknowledged)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Implement byline attribution once Rob approves format, Blue Sky setup, favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 213 — 2026-03-16 — Content (Pet & Animal Care MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Pet & Animal Care MCP Servers** (`content/reviews/pet-animal-care-mcp-servers.md`) — 178th review, one-hundred-fifty-eighth beyond original list.
   - Virtual pets (2 servers): shreyaskarnik/mcpet (TypeScript — Tamagotchi-style, 4 pet types, 5 stats, lifecycle stages, 6 care tools, ASCII art), stytchauth/chatagotchi (JavaScript — ChatGPT Apps SDK interactive pet, 5 animal types)
   - Wildlife & species ID (2 servers): fonkychen/nature-vision-mcp (TypeScript — species identification from images via Nature Vision API, confidence scores), wildlife-insights-mcp (TypeScript — Wildlife Insights GraphQL API, 12+ tools, camera trap photo ID, species analytics)
   - Birding (1 server): moonbirdai/ebird-mcp-server (TypeScript — eBird API, observations, notable sightings, hotspots, taxonomy)
   - Livestock & breeding (1 server): epicpast/nsip-api-client (Python — 15 MCP tools, National Sheep Improvement Program, genetic evaluation, mating planning, flock ranking)
   - Pet store & adoption (2 servers): raghavendraprakash/mcpforrestapis (Python — Swagger Petstore API MCP wrapper), zeeroiq/pet-adoption-scheduler (Python — adoption appointment scheduling)
   - Nutrition tangential (2 servers): deadletterq/mcp-opennutrition (300K+ food items, local), MCP-Forge/nutritionix-mcp-server (Nutritionix API)
   - Gaps: no Petfinder/Adopt-a-Pet, no vet clinic management, no pet health records, no dog training, no breed identification, no pet GPS, no aquarium management, no livestock beyond sheep, no AKC registry, no pet insurance
   - 10+ servers across 5 subcategories, Rating: 2.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Pet / animal care" row to summary table
   - Updated review count to 178

3. **Built site** (198 pages, 130ms). Deploy pending — throttle not yet cleared (~20 min since last deploy).

### What should happen next
- **Run 214:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Interior Design/Architecture, Emergency/Disaster Response, Sports Analytics, Insurance/InsurTech
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 212 — 2026-03-16 — Content (Tax & Payroll MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Tax & Payroll MCP Servers** (`content/reviews/tax-payroll-mcp-servers.md`) — 177th review, one-hundred-fifty-seventh beyond original list.
   - US tax calculation (3 servers): dma9527/irs-taxpayer-mcp (TypeScript — 39 tools for federal/state tax calculations, credits, deductions, retirement strategies, year-end optimization, TY2024+TY2025 with OBBB Act, all local), gama104/GamaMcpServer (8 stars, C# — 30 capabilities, OAuth 2.1, 1040/Schedule A/C for 2023-2025), jayanta8509/TAX_MCP (Python — LangChain + MySQL tax client management, Redis memory, GPT-4o-mini)
   - Tax filing & compliance (3 servers): TaxBandits Remote MCP (commercial — W-9/1099 automation, IRS e-filing), Avalara MCP Servers (commercial — 5 servers: AvaTax, Returns, E-Invoicing, Tax Registrations, Exemption Certificates), norman-finance/norman-mcp-server (8 stars, TypeScript — invoicing, VAT filing, Finanzamt previews, German market)
   - International tax (3 servers): kentaroajisaka/tax-law-mcp (TypeScript — Japanese tax law via e-Gov API, 1,950 ruling cases), ag2-mcp-servers/income-tax-department (Python — India PAN API), rocketlang/mcp-tools (282 India-first tools including GST, e-Invoice, GSTR-3B)
   - Payroll & HR (3 servers): rocketsciencegg/rippling-mcp-server (TypeScript — Rippling HR/payroll, 5+ tools), merge-api/merge-mcp (Python — unified API for 70+ HRIS/payroll platforms), payroll-mcp-server (TypeScript + Express — salary management)
   - Charity & nonprofit (1 server): briancasteel/charity-mcp-server (TypeScript — IRS charity database, EIN verification, 14 prompt templates)
   - Gaps: no TurboTax/H&R Block, no ADP/Gusto/Paychex direct servers, no UK HMRC, no EU VAT OSS, no Canadian CRA, no Australian ATO, no W-2 prep, no benefits administration, no tax document OCR
   - 15+ servers across 5 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Tax / payroll" row to summary table
   - Updated review count to 177

3. **Built site** (197 pages, 137ms). Deploy pending — throttle not yet cleared (~14 min since last deploy).

### What should happen next
- **Run 213:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Interior Design/Architecture, Emergency/Disaster Response, Pet/Animal Care, Sports Analytics
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 211 — 2026-03-16 — Content (Mental Health & Wellness MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** from Run 210 (throttle had cleared).

2. **Wrote new review: Mental Health & Wellness MCP Servers** (`content/reviews/mental-health-wellness-mcp-servers.md`) — 176th review, one-hundred-fifty-sixth beyond original list.
   - Therapy & counseling (2 servers): dion-hagan/mcp-ai-therapy (2 stars, Go + Python — therapeutic conversations between Claude and local Ollama LLM with vector memory), danieldunderfelt/ai-therapist-mcp (4 stars, JavaScript — 6 therapeutic tools, crisis intervention, wellness check-ins)
   - Emotional support (2 servers): bnookala/mcp-emotional-support (1 star, TypeScript — 5 therapeutic personas), jeffkit/treehole-ai (4 stars, JavaScript — rest and vent space for AI)
   - Mood tracking (3 servers): muminfarooq190/MCP (JavaScript — mood_tracker, check_in, coping_tools), mcp-mood-quotes (Go — mood-based quotes), t3ase/MCP (WhatsApp mood analysis + Spotify playlists)
   - Journaling (2 servers): obra/private-journal-mcp (local semantic search, no external APIs), mtct/journaling-mcp (5 stars, Python — emotional analysis)
   - Meditation & mindfulness (2 servers): CN-Scars/meditation-mcp (digital zen mode), aplaceforallmystuff/mcp-wisdom (3 stars, 9 philosophical tools from Stoic/Cognitive/Mindfulness/Strategic traditions)
   - Comprehensive platforms (2 servers): ishpreet404/Zenify (10 stars, RAG chatbot with suicide risk detection), evangstav/personal-mcp (9 stars, health tracking with mood/energy/sleep/stress journals)
   - Wellness tracking (3 servers): tomekkorbak/oura-mcp-server (37 stars, Oura Ring data), rwking/wellness_planner (energy-aware scheduling), levelsofself/mcp-server (self-awareness game with 6,854 scenarios)
   - Gaps: no CBT/DBT therapy servers, no breathing/breathwork, no gratitude tracking, no crisis hotline integration, no professional platform bridges, no clinical assessment instruments (PHQ-9, GAD-7)
   - 15+ servers across 6 subcategories, Rating: 3/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Mental health / wellness" row to summary table
   - Updated review count to 176

4. **Built site** (193 pages, 138ms). Deploy pending — throttle applies.

### What should happen next
- **Run 212:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Tax/Payroll, Interior Design/Architecture, Emergency/Disaster Response, Insurance/InsurTech
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 210 — 2026-03-16 — Content (Smart Home & Home Automation MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Smart Home & Home Automation MCP Servers** (`content/reviews/smart-home-automation-mcp-servers.md`) — 175th review, one-hundred-fifty-fifth beyond original list.
   - Home Assistant (8+ servers): homeassistant-ai/ha-mcp (1,100+ stars, Python — 80+ tools, entity control, automation management, calendars, dashboards, backup/restore, history/statistics, camera snapshots, system admin, runs locally), tevonsb/homeassistant-mcp (500+ stars, TypeScript — real-time SSE, HACS management, add-on lifecycle), plus voska/hass-mcp, zorak1103/ha-mcp, jango-blockchained/advanced-homeassistant-mcp, hekmon8/Homeassistant-server-mcp, hpohlmann/home-assistant-mcp, amattas/homeassistant-mcp. Home Assistant also has an official built-in MCP server integration.
   - Other platforms (3 servers): abeardmore/hubitat-mcp (Hubitat Maker API), MvdMunnik26/Hubitat-MCP (Hubitat Elevation), tdeckers/openhab-mcp (OpenHAB REST API)
   - IoT & unified control (2 servers): jprbom/smart-home-orchestrator-mcp (multi-brand — Nest, Ring, Ecobee, MQTT), jordy33/iot_mcp_server (generic IoT device control)
   - Thermostat-specific (1): emrikol/ecobee-mcp (TypeScript — Ecobee thermostat control)
   - Gaps: no Google Home, no Amazon Alexa, no Apple HomeKit, no Samsung SmartThings, no Tuya/Smart Life, no Zigbee2MQTT direct bridge, no Matter protocol, no energy monitoring/solar, no security systems, no robot vacuums
   - 15+ servers across 4 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Smart home / automation" row to summary table
   - Updated review count to 175

3. **Built site** (195 pages, 130ms). Deploy pending — throttle not yet cleared (~27 min since last deploy).

### What should happen next
- **Run 211:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Mental Health/Wellness, Tax/Payroll, Interior Design/Architecture, Emergency/Disaster Response
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 209 — 2026-03-16 — Content (Transportation & Mobility MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Transportation & Mobility MCP Servers** (`content/reviews/transportation-mobility-mcp-servers.md`) — 174th review, one-hundred-fifty-fourth beyond original list.
   - Public transit (9+ servers): mirodn/mcp-server-public-transport (6 stars, Python — multi-country European transit via UK/Swiss/Norwegian/Belgian APIs), plus city-specific servers for NYC (mta-mcp — subway arrivals/alerts/trip planning), Seattle (kingcountytransit-mcp — OneBusAway), Berlin (berlin-transport-mcp — VBB API), Munich (muc-mcp-server — MVG), Caltrain (caltrain-mcp — GTFS), Singapore (sg-lta-mcp — LTA DataMall), Hong Kong (mcp_hkbus — KMB/Long Win), DC (metro-mcp — WMATA)
   - Flight tracking (4 servers): sunsetcoder/flightradar24-mcp-server (46 stars, Python — real-time FR24 tracking, emergency monitoring), Pradumnasaraf/aviationstack-mcp (Python — AviationStack API, airline/airport/aircraft data), mikedarke/mcp-server-flight-aware-aeroapi (FlightAware AeroAPI — positions, delays, weather), Cyreslab-AI/flightradar-mcp-server (alternative FR24)
   - Aviation data (1): blevinstein/aviation-mcp (TypeScript — FAA METAR/TAF/PIREP/SIGMET, NOTAMs, sectional/IFR/TPP charts)
   - Ride-hailing (1): 199-mcp/mcp-uber (TypeScript — OAuth 2.0 Uber ride booking, price estimates, status, cancellation)
   - Smart city transport (1): sosanzma/SmartCityMCP (Python — Valencia real-time traffic, bike-sharing, air quality)
   - Gaps: no Lyft, no GBFS micromobility, no universal GTFS-realtime parser, no maritime/shipping, no freight/trucking, no multimodal journey planning, no parking availability
   - 20+ servers across 5 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Transportation / mobility" row to summary table
   - Updated review count to 174

3. **Built site** (194 pages, 128ms). Deploy pending — throttle not yet cleared (~16 min since last deploy).

### What should happen next
- **Run 210:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Supply Chain/Logistics, Insurance/InsurTech, Nonprofit/Philanthropy, Sports/Fitness
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 208 — 2026-03-16 — Content (Compliance & Data Governance MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Compliance & Data Governance MCP Servers** (`content/reviews/compliance-data-governance-mcp-servers.md`) — 173rd review, one-hundred-fifty-third beyond original list.
   - Compliance automation (3 servers): VantaInc/vanta-mcp-server (41 stars, TypeScript — 6+ tools, SOC 2/ISO 27001/HIPAA/GDPR monitoring with 1,200+ automated tests), secureframe/secureframe-mcp-server (TypeScript — 11 read-only endpoints, Lucene query syntax, SOC 2/ISO 27001/CMMC/FedRAMP), Drata MCP (compliance tests, risk reports, evidence collection for SOC 2/HIPAA/ISO 27001)
   - GRC platforms (1): CISO Assistant (open source — 100+ global frameworks, automatic control mapping, risk management, AppSec, audit, TPRM, privacy)
   - Privacy/GDPR (1): DPO2U MCP Server (Python — LGPD/GDPR compliance automation, self-hosted, homomorphic encryption, zero-knowledge proofs, data flow mapping, breach simulation)
   - Data catalog/metadata (4 servers): acryldata/mcp-server-datahub (62 stars, Python — search, lineage, metadata, SQL query analysis, mutation tools), OpenMetadata MCP (enterprise DQ tooling, semantic search, vector embeddings), Atlan MCP (pyatlan SDK, asset search, lineage, glossary, DQ rules), RafaelCartenet/mcp-databricks-server (Unity Catalog, lineage, SQL execution)
   - Data quality (1): davidf9999/gx-mcp-server (Python — Great Expectations validation as MCP tools, CSV/Snowflake/BigQuery support)
   - Gaps: no NIST RMF server, no EU AI Act compliance, no automated data classification, no consent management (OneTrust/TrustArc), no data retention enforcement
   - 15+ servers across 5 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Compliance / data governance" row to summary table
   - Updated review count to 173

3. **Built site** (193 pages, 135ms). Deploy pending — throttle applies.

### What should happen next
- **Run 209:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Transportation/Mobility, Supply Chain/Logistics, Insurance/InsurTech, Nonprofit/Philanthropy
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 207 — 2026-03-16 — Content (Sustainability & Climate MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** — throttle cleared (63+ minutes since last deploy). Deployed runs 204-206 content (Network Automation, Gaming & Esports, Digital Accessibility, Regex & Text Processing reviews).

2. **Wrote new review: Sustainability & Climate MCP Servers** (`content/reviews/sustainability-climate-mcp-servers.md`) — 172nd review, one-hundred-fifty-second beyond original list.
   - Carbon emissions (1 server): jagan-shanmugam/climatiq-mcp-server (6 stars, Python — 7+ tools, Climatiq API for electricity, travel, cloud, freight, procurement emissions, 68,000+ emission factors)
   - Building energy simulation (1): LBNL-ETA/EnergyPlus-MCP (Python — 35 tools, DOE EnergyPlus whole-building simulation, HVAC topology, automated simulation, published in SoftwareX journal)
   - Power grid intelligence (2): karthikravva/MCP-Energy-Hub (Python — 8 tools, US power grid via EIA API, carbon-aware compute scheduling across CAISO/ERCOT/PJM/NYISO/MISO), Power-Agent/PowerMCP (Python — PowerWorld + OpenDSS simulation, part of broader Power-Agent ecosystem)
   - Air quality monitoring (3): mattmarcin/aqicn-mcp (Python — 3 tools, AQICN.org global AQI), michaelahern/airthings-consumer-mcp (TypeScript — Airthings hardware), danielrosehill/Google-Air-Quality-MCP (Go — Google Maps Air Quality API, WIP)
   - Climate data (1): cmer81/open-meteo-mcp (TypeScript — 10+ tools, weather forecasts, ERA5 archives from 1940, air quality, marine, flood forecasts, CMIP6 climate projections, seasonal predictions)
   - Open source contribution (1): Codeshark-NET/climate-triage-mcp (TypeScript — search climate-related OSS issues)
   - Also noted: ahmedelshazly27/opendss-mcp-server (dedicated OpenDSS distribution system analysis)
   - Gaps: no carbon registry MCPs (Gold Standard, Verra), no LCA tools, no ESG/CSRD reporting, no waste management, no satellite environmental monitoring, no supply chain Scope 3 tracking
   - 15+ servers across 6 subcategories, Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Sustainability / climate" row to summary table
   - Updated review count to 172

4. **Built site** (192 pages, 124ms). Deploy pending — throttle applies.

### What should happen next
- **Run 208:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Compliance Frameworks, Data Governance, Transportation/Mobility, Supply Chain/Logistics
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 206 — 2026-03-16 — Content (Digital Accessibility MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Digital Accessibility MCP Servers** (`content/reviews/digital-accessibility-mcp-servers.md`) — 171st review, one-hundred-fifty-first beyond original list.
   - Comprehensive audit platforms (7 servers): ronantakizawa/a11ymcp (78 stars, JS — 6 tools, axe-core + Puppeteer, WCAG 2.0/2.1/2.2), JustasMonkev/mcp-accessibility-scanner (43 stars, JS — 20+ tools, Playwright + axe-core, site-wide crawling, keyboard auditing, browser automation), priyankark/a11y-mcp (40 stars, JS — 2 tools, agentic fix loop), joe-watkins/accessibility-testing-mcp (JS — 5 tools, dual engine axe-core + IBM Equal Access), alexanderuk82/mcp-wcag-accessibility (TS — 10 tools, auto-refactoring, 100% local, multi-framework), jbuchan/accessibility-mcp-server (TS — 3 tools, cross-browser), westsideori/cursor-a11y-mcp (JS — Cursor-specific)
   - Color contrast (4 servers): bryanberger/mcp-wcag-color-contrast (TS — 4 tools, Culori-based accurate WCAG contrast), ryelle/a11y-color-contrast-mcp (2 stars, TS — 3 tools, light/dark detection), AccessLint/mcp-server (1 star, TS — 3 tools, suggests accessible alternatives), bennyzen/mcp-color-convert (TS — 20+ tools, comprehensive color toolkit)
   - Lighthouse (1): danielsogl/lighthouse-mcp-server (49 stars, TS — 13+ tools, Google Lighthouse)
   - Agent frameworks (1): Community-Access/accessibility-agents (186 stars — 57 agents across 5 platforms, WCAG 2.2 AA enforcement)
   - ARIA/WCAG reference (1): karanshah229/wcag-aria-practices-mcp-skill (WAI-ARIA pattern documentation)
   - Gaps: no official Deque MCP, no WAVE/Pa11y MCP, no PDF accessibility, no mobile accessibility testing, no screen reader simulation
   - 20+ servers across 5 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Digital accessibility" row to summary table
   - Updated review count to 171

3. **Built site** (191 pages, 131ms). Deploy pending — throttle not yet cleared.

### What should happen next
- **Run 207:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Compliance Frameworks, Sustainability/Climate, Data Governance, Transportation/Mobility
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 205 — 2026-03-16 — Content (Gaming & Esports MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Gaming & Esports MCP Servers** (`content/reviews/gaming-esports-mcp-servers.md`) — 170th review, one-hundred-fiftieth beyond original list.
   - Live game interaction (2): yuniko-software/minecraft-mcp-server (504 stars, TypeScript — 15 commands, Mineflayer-powered real-time character control including building, mining, inventory, chat), notpoiu/roblox-mcp (18 stars, JavaScript — 18 tools, game client interaction with code execution, script decompilation, remote interception)
   - Esports analytics (1): opgginc/opgg-mcp (76 stars, TypeScript — 27 tools for LoL/TFT/Valorant data, champion analytics, meta compositions, esports schedules)
   - Steam (3 servers): dsp/mcp-server-steam (12 stars, Java — Steam API context), algorhythmic/steam-mcp (4 stars, JavaScript — 10 tools for achievements/stats/schemas), fenxer/steam-review-mcp (5 stars, TypeScript — review analysis with sentiment)
   - Chess (4 servers): pab1it0/chess-mcp (64 stars, Python — 10 tools for Chess.com data/PGN), arvid-berndtsson/Chess-MCP (TypeScript — 12 tools, play against AI, FEN/PGN), turlockmike/chess-mcp (Stockfish analysis), danilop/chess-support-mcp (game state management)
   - Game server management (1): v9rt3x/cs2-rcon-mcp (9 stars, Python — 5 tools, CS2 RCON, workshop maps)
   - Game databases (2): bielacki/igdb-mcp-server (3 stars, Python — IGDB/Twitch game database), moonolgerd/game-mcp (C# — multi-platform game discovery)
   - Streaming (1): mtane0412/twitch-mcp-server (TypeScript — 13 tools for Twitch Helix API)
   - Gaps: no official platform MCPs from Steam/Valve, Epic, PlayStation, Xbox, Nintendo; no cross-platform achievement tracking; limited esports coverage beyond Riot titles; no modding workflow; no retro gaming
   - 25+ servers across 7 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Gaming / esports" row to summary table
   - Updated review count to 170

3. **Built site** (190 pages, 128ms). Deploy pending — throttle not yet cleared.

### What should happen next
- **Run 206:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Compliance Frameworks, Sustainability/Climate, Data Governance, Digital Accessibility
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 204 — 2026-03-16 — Content (Network Automation & Infrastructure MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Network Automation & Infrastructure MCP Servers** (`content/reviews/network-automation-infrastructure-mcp-servers.md`) — 169th review, one-hundred-forty-ninth beyond original list.
   - Multi-vendor platforms (2): E-Conners-Lab/NetworkOps_Platform (178 tools, Cisco/Juniper/Nokia/Arista/Linux, self-healing agents, drift detection, web dashboard), automateyournetwork/netclaw (135 stars, 82 skills across 37 MCPs, autonomous network agent with pyATS/CloudVision/F5/ServiceNow)
   - Cisco ecosystem (4 servers): pamosima/network-mcp-docker-suite (10 Docker MCP servers — Meraki, Catalyst Center, IOS XE, ISE, ThousandEyes, Splunk, NetBox, GitLab), automateyournetwork/pyATS_MCP (66 stars, Cisco pyATS/Genie structured interaction), MCPyATS (VibeOps framework with LangGraph), xorrkaz/cml-mcp (Cisco Modeling Labs via natural language)
   - DCIM/IPAM (3): netboxlabs/netbox-mcp-server (127 stars, official NetBox Labs, read-only), ardecode/netbox-mcp-server (142+ tools), Deployment-Team/netbox-mcp
   - Device automation (3): melihteke/mcp-server-netmiko (Netmiko SSH multi-vendor), upa/mcp-netmiko-server, Subnet-Calculator-MCP-Server
   - Network diagnostics (3): patrickdappollonio/mcp-domaintools (DNS/WHOIS/TLS/ping), kumarprobeops/probeops-mcp-server (6 global regions, no API key), deshabhishek007/domain-tools-mcp-server
   - Network analysis (1): forwardnetworks/forward-mcp (55+ tools, network digital twin, path tracing, semantic search)
   - Gaps: no dedicated Juniper/Arista MCP, no Palo Alto/Fortinet firewall MCP, no YANG/NETCONF-native MCP, no SD-WAN management, no GNS3/EVE-NG emulation MCP
   - 25+ servers across 6 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Network automation / infrastructure" row to summary table
   - Updated review count to 169

3. **Built site** (189 pages, 129ms). Deploy pending — throttle applies.

### What should happen next
- **Run 205:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Language Learning, Home Automation (beyond IoT), Compliance Frameworks, Transportation/Mobility
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 203 — 2026-03-16 — Content (Regex & Text Processing MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** — previous runs' changes (Bioinformatics, Digital Twins, Marketing Automation reviews) now live.

2. **Wrote new review: Regex & Text Processing MCP Servers** (`content/reviews/regex-text-processing-mcp-servers.md`) — 168th review, one-hundred-forty-eighth beyond original list.
   - Document conversion (5 servers): zcaceres/markdownify-mcp (2,400 stars, TypeScript — 10 tools, convert PDF/images/audio/DOCX/web to Markdown), vivekVells/mcp-pandoc (507 stars, Python — Pandoc bidirectional conversion), microsoft/markitdown-mcp (82K parent — official single-tool converter), Duds/md-converter (Markdown to DOCX/XLSX/PPTX), wowyuarm/file-converter-mcp (23 stars, Python — DOCX↔PDF, image formats)
   - Diff & comparison (6 servers): benjamine/jsondiffpatch diff-mcp (5,100 parent — Google diff-match-patch + structured data), samihalawa/mcp-server-diff-editor (5 stars, JS — 12 tools), tatn TypeScript + Python diff servers, keyhoffman/diff-mcp (whitespace/case-insensitive), gorosun/unified-diff-mcp
   - Translation (4 servers): DeepLcom/deepl-mcp-server (95 stars, JS — official, 8 tools, document translation + glossaries), translated/lara-mcp (79 stars, TypeScript — 10+ tools with translation memory), ytarfa/tolgee-mcp (localization platform), akramsaouri/translate
   - Regex (3 servers): PatzEdi/MCPGex (5 stars, Python — 4 tools for iterative regex testing), myuon/refactor-mcp (6 stars, TypeScript — regex search/replace for code), RJTPP/mcp-server-file-search-tool
   - Encoding/cryptography (1 server): 1595901624/crypto-mcp (10 stars, TypeScript — 14 tools for AES/DES/hashing/Base64/Hex)
   - Grammar/spelling (2 servers): morahan/SpellChecker-MCP (TypeScript — 7 tools, 15+ languages), acforu/grammar-police-mcp (JS — LLM-powered)
   - Text manipulation (4+ servers): agent-hanju/char-index-mcp (12 character-level tools), tivaliy/mcp-nlp (text similarity), tumf/mcp-text-editor (177 stars — line-based editing), yhzion/comment-stripper-mcp (batch comment removal), Dicklesworthstone/ultimate_mcp_server (129 stars — ripgrep/awk/sed/jq)
   - Gaps: no LanguageTool MCP, no template engine MCP, no dedicated OCR, no unified text pipeline
   - 30+ servers across 7 subcategories, Rating: 3.5/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Regex / text processing" row to summary table
   - Updated review count to 168

4. **Built site** (188 pages, 122ms). Deploy pending — throttle applies.

### What should happen next
- **Run 204:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Printing/Document Formatting, Accessibility, Sustainability/Climate, Sports/Fitness
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 202 — 2026-03-16 — Content (Bioinformatics & Life Sciences MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Bioinformatics & Life Sciences MCP Servers** (`content/reviews/bioinformatics-life-sciences-mcp-servers.md`) — 167th review, one-hundred-forty-seventh beyond original list.
   - Integrated platforms (2): genomoncology/biomcp (241 stars, Python — single-binary biomedical MCP, 12 entities across 15+ sources), anthropics/life-sciences (259 stars — official Anthropic marketplace with PubMed, BioRender, 10x Genomics, scRNA-seq QC skills)
   - Protein/chemical databases (6 servers): Augmented-Nature/ChEMBL-MCP-Server (78 stars, TypeScript — 22 drug discovery tools), PubChem-MCP-Server (35 stars, 30 tools, 110M+ compounds), UniProt-MCP-Server (18 stars, 26 tools), PDB-MCP-Server (21 stars — Protein Data Bank), STRING-db-MCP-Server (4 stars — protein interactions)
   - Biomedical literature (3 servers): JackKuo666/PubMed-MCP-Server (105 stars, Python — search, PDF download, deep analysis), cyanheads/pubmed-mcp-server (66 stars, TypeScript — production-grade NCBI E-utilities, multi-format citations), vitorpavinato/ncbi-mcp-server (8 stars — analytics)
   - Clinical research (3+ servers): Cicatriiz/healthcare-mcp-public (102 stars, JS — 9 tools: FDA, PubMed, ClinicalTrials, ICD-10, DICOM), cyanheads/clinicaltrialsgov-mcp-server (59 stars — patient matching, trend analysis), FHIR/EHR servers (jmandel/health-record-mcp, wso2/fhir-mcp-server, xSoVx/fhir-mcp)
   - Sequence analysis (7+ servers): bio-mcp organization (BLAST, BWA, SeqKit, AMBER, InterPro, Evo2), longevity-genie/gget-mcp (27 stars, Python — ~15 tools wrapping gget for BLAST, AlphaFold, COSMIC, Ensembl)
   - Systems biology (4 servers): Reactome (11 stars, pathways), OpenTargets (9 stars, gene-drug-disease), BioThings (5 stars, gene/variant annotation), ProteinAtlas (3 stars, expression data)
   - Drug discovery pipeline, SureChEMBL patent search (7 stars, 15 tools), MCPmed community initiative (10 repos), BioinfoMCP automated conversion platform
   - Gaps: no AlphaFold direct MCP, no Galaxy wrapper, no KEGG, limited medical imaging, no single-cell pipeline MCP
   - 40+ servers across 7 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Bioinformatics / life sciences" row to summary table
   - Updated review count to 167

3. **Built site** (187 pages, 124ms). **Deploy pending** — throttle not yet cleared.

### What should happen next
- **Run 203:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Regex/Text Processing, Printing/Document Formatting, Accessibility, Sustainability/Climate
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 201 — 2026-03-16 — Content (Digital Twins, 3D Modeling & Simulation MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Deployed site** — previous runs' changes (Marketing Automation, Terminal & CLI Tools, ERP reviews) now live.

2. **Wrote new review: Digital Twins, 3D Modeling & Simulation MCP Servers** (`content/reviews/digital-twins-3d-simulation-mcp-servers.md`) — 166th review, one-hundred-forty-sixth beyond original list.
   - 3D Modeling / Blender (5 servers): ahujasid/blender-mcp (17,700 stars, Python — most popular 3D MCP overall, Poly Haven assets, Hyper3D Rodin AI models), poly-mcp/Blender-MCP-Server (51 tools over HTTP), CommonSenseMachines/blender-mcp (text-to-4D worlds via CSM.ai), dhakalnirajan/blender-open-mcp (local Ollama), VxASI/blender-mcp-vxai
   - CAD (10+ servers): neka-nat/freecad-mcp (605 stars, Python — 10 tools, parts library), proximile/FreeCAD-MCP (Docker + Vision AI), spkane/freecad-addon-robust-mcp-server (150+ tools), jhacksman/OpenSCAD-MCP-Server (multi-view reconstruction), BuildCAD AI (free cloud CAD), Svetlana-DAO-LLC/cad-agent (build123d + Docker), multiple Fusion 360 MCPs
   - Game engines — Unity (3 servers): IvanMurzak/Unity-MCP (1,300 stars — 50+ tools, editor + runtime), CoderGamester/mcp-unity (1,400 stars — WebSocket bridge, 35+ tools), CoplayDev/unity-mcp
   - Game engines — Unreal (4 servers): chongdashu/unreal-mcp (1,600 stars — C++/Python, blueprint editing), flopperam/unreal-engine-mcp (592 stars — world building, maze generation), ayeletstudioindia/unreal-analyzer-mcp, kvick-games/UnrealMCP
   - Physics simulation (5 servers): chrishayuk/chuk-mcp-physics (55 tools, 10 categories, 98% test coverage), andylbrummer/math-mcp (GPU-accelerated quantum/molecular/neural, 57 tools), Genesis (28.3k stars engine) + dustland/genesis-mcp (4 stars wrapper), manasp21/PsiAnimator-MCP (QuTiP + Manim)
   - Engineering simulation (5+ servers): omni-mcp/isaac-sim-mcp (136 stars — NVIDIA Isaac Sim robotics), Orthogonalpub/modelica_simulation_mcp_server (15 stars — Modelica ODE), clanker-lover/spicebridge (18 tools ngspice circuit sim), poly-mcp/IoT-Edge-MCP-Server (industrial IoT), pathintegral-institute/mcp.science
   - Gaps: no ANSYS/COMSOL/Abaqus MCP, no SolidWorks, no cloud digital twin platforms, no CFD, minimal Genesis MCP wrapper
   - 35+ servers across 6 subcategories, Rating: 4/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Digital twins / 3D / simulation" row to summary table
   - Updated review count to 166

4. **Built site** (186 pages, 126ms). **Deploy pending** — throttle applies.

### What should happen next
- **Run 202:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Bioinformatics, Regex/Text Processing, Printing/Document Formatting, Accessibility
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 200 — 2026-03-16 — Content (Marketing Automation MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Marketing Automation MCP Servers** (`content/reviews/marketing-automation-mcp-servers.md`) — 165th review, one-hundred-forty-fifth beyond original list.
   - Email marketing (6+ servers): deyikong/sendgrid-mcp (21 stars, Python — 59 tools, read-only safety mode), Garoth/sendgrid-mcp (24 stars, Python — focused marketing API), houtini-ai/brevo-mcp (A/B testing, segmentation), MailerLite official MCP (no API key needed), ActiveCampaign official MCP, Klaviyo official MCP + mattcoatsworth/Klaviyo-MCP-Server, Mailchimp MCPs
   - HubSpot CRM/marketing (5+ servers): peakmojo/mcp-hubspot (72 stars, Python — FAISS vector storage, semantic search), calypsoCodex/hubspot-mcp-extended (106 tools from OpenAPI specs), shinzo-labs/hubspot-mcp, yespark/mcp-hubspot (40+ tools), official HubSpot MCP (public beta)
   - Ad platforms (8+ servers): pipeboard-co/meta-ads-mcp (601 stars, Python — most popular marketing MCP, full campaign lifecycle), brijr/meta-mcp (creative optimization), google-marketing-solutions/google_ads_mcp (official, Apache-2.0, read-only), cohnen/mcp-google-ads (natural language analysis), TrueClicks/google-ads-mcp-js (no credentials needed)
   - SEO (5+ servers): AminForou/mcp-gsc (512 stars, Python — Google Search Console), cnych/seo-mcp (165 stars — free Ahrefs data), Skobyn/dataforseo-mcp-server (47 stars — comprehensive DataForSEO API), mrgoonie/seo-insights-mcp-server
   - Social media (5+ servers): pascalporedda/typefully-mcp-server (TypeScript — X/LinkedIn/Bluesky/Threads), tn819/buffer-mcp (Buffer scheduling), LokiMCPUniverse/hootsuite-mcp-server
   - Gaps: no unified marketing dashboard, no A/B testing orchestrator, no affiliate marketing MCP, no cross-platform analytics aggregation
   - 30+ servers across 5 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Marketing automation" row to summary table
   - Updated review count to 165

3. **Built site** (185 pages, 122ms). **Deploy pending** — throttle not yet cleared.

### What should happen next
- **Run 201:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Digital Twins/Simulation, Bioinformatics, Regex/Text Processing, Printing/Document Formatting
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 199 — 2026-03-16 — Content (Terminal & CLI Tools MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Terminal & CLI Tools MCP Servers** (`content/reviews/terminal-cli-tools-mcp-servers.md`) — 164th review, one-hundred-forty-fourth beyond original list.
   - Shell execution (5 servers): tumf/mcp-shell-server (156 stars, Python — allowlist/blocklist, timeout control), MladenSU/cli-mcp-server (134 stars, Python — per-command and per-flag whitelisting), sonirico/mcp-shell (23 stars, Go — no-shell-interpretation secure mode, audit trail), blazickjp/shell-mcp-server (cross-platform bash/sh/cmd/powershell), egoist/shell-command-mcp (minimal)
   - Persistent sessions (6 servers): nickgnd/tmux-mcp (233 stars, TypeScript — most popular tmux MCP), lox/tmux-mcp-server (Go, lightweight), TNTisdial/persistent-shell-mcp (workspace abstraction), wehnsdaefflae/terminal-control-mcp (raw stream capture, agent-controlled timing), kazuph/mcp-tmux, jonrad/tmux-mcp
   - SSH/Remote (4 servers): bvisible/mcp-ssh-manager (37 tools in 6 groups, DevOps automation), 1999AZZAR/terminal-mcp-server (local + SSH dual mode), tufantunc/ssh-mcp (basic SSH), weidwonder/terminal-mcp-server (env var persistence)
   - MCP CLI inspectors (3 tools): f/mcptools (Go CLI with proxy mode), wong2/mcp-cli (115 stars, OAuth), modelcontextprotocol/inspector (official visual testing)
   - Multi-tool: inercia/MCPShell (shell scripts as MCP tools), sammcj/mcp-devtools (modular dev tools)
   - Gaps: no terminal emulator integration, no Windows-specific MCP, no process management, no unified terminal orchestrator
   - 25+ servers across 5 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Terminal / CLI tools" row to summary table
   - Updated review count to 164

3. **Built site** (184 pages, 123ms). **Deploy pending** — throttle not yet cleared.

### What should happen next
- **Run 200:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Digital Twins/Simulation, Marketing Automation, Bioinformatics, Regex/Text Processing
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 198 — 2026-03-16 — Content (ERP & Business Management MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: ERP & Business Management MCP Servers** (`content/reviews/erp-business-management-mcp-servers.md`) — 163rd review, one-hundred-forty-third beyond original list.
   - Odoo (3 servers): tuanle96/mcp-odoo (269 stars, Python — most popular ERP MCP, sales/inventory/accounting/purchasing), ivnvxd/mcp-server-odoo (130 stars, Python, MIT — secure with YOLO mode, enterprise module, PyPI), hachecito/odoo-mcp-improved (29 stars — advanced sales/purchases/stock/accounting tools)
   - Microsoft Dynamics 365 (5 servers): Official D365 ERP MCP Server (public preview, dynamic framework — agents do anything a user can), Dataverse MCP Server (GA, Copilot Studio integration), demiliani/D365BCAdminMCP (33 admin tools, VS Code extension), knowall-ai/mcp-business-central (API v2.0 access), SShadowS/bc-webclient-mcp-server (reverse-engineered WebSocket)
   - Oracle NetSuite (3 servers): Native AI Connector (official, full security model), dsvantien/netsuite-mcp-server (6 stars, SuiteInsider, OAuth 2.0 PKCE), glints-dev/mcp-netsuite (stdio-based)
   - SAP (6 CData servers): sap-erp, sap-hana, sap-business-one, sap-bydesign, sap-concur, sap-hybris-c4c — all read-only via JDBC, commercial CRUD
   - Oracle Cloud (2 servers): oracle/mcp (official multi-product repo, SQLcl integration), shjanjua/OCI-MCP-Servers (ADB/Compute/Identity/Networking)
   - Multi-ERP: CData Connect AI (commercial, 200+ data sources), Infor M3 ION API (basic)
   - Gaps: no Workday, no Sage/Epicor, no open-source SAP, limited writes, no cross-ERP unified interface
   - 20+ servers across 6 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "ERP / business management" row to summary table
   - Updated review count to 163

3. **Built site** (183 pages, 120ms). **Deploy pending** — throttle not yet cleared.

### What should happen next
- **Run 199:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Terminal/CLI Tools, Digital Twins/Simulation, Marketing Automation, Bioinformatics
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 197 — 2026-03-17 — Content (Browser Extension MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Browser Extension MCP Servers** (`content/reviews/browser-extension-mcp-servers.md`) — 162nd review, one-hundred-forty-second beyond original list.
   - Official DevTools: ChromeDevTools/chrome-devtools-mcp (28,700 stars, TypeScript — official Google Chrome DevTools MCP with Puppeteer, performance tracing, Lighthouse, accessibility debugging, memory profiling), benjaminr/chrome-devtools-mcp (287 stars — community alternative)
   - Chrome Extensions: hangwin/mcp-chrome (10,800 stars — native browser with existing sessions/logins), AgentDeskAI/browser-tools-mcp (7,100 stars — monitoring/WCAG audits/SEO/auto-paste), BrowserMCP/mcp (6,100 stars, Apache-2.0 — local-first automation), djyde/browser-mcp (cross-browser Chrome/Edge/Firefox)
   - Browser-Native Protocol: MiguelsPizza/WebMCP (924 stars — MCP-B, W3C standard, Chrome 146 early preview)
   - Firefox: eyalzh/browser-control-mcp (250 stars — security-focused with audit log), freema/firefox-devtools-mcp (56 stars — WebDriver BiDi, used by Mozilla), JediLuke/firefox-mcp-server (28 tools via Playwright)
   - DevTools Protocol & Bridges: lxe/chrome-mcp (42 stars — lightweight CDP), Oanakiaja/chrome-extension-bridge-mcp (WebSocket window bridge), robhicks/browser-mcp-bridge (12+ tools, comprehensive)
   - Gaps: no Safari/WebKit, no unified cross-browser, no mobile browser support, no extension development MCP, WebMCP still early preview
   - 15+ servers across 5 subcategories, Rating: 4.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Browser extensions" row to summary table
   - Updated review count to 162

3. **Built site** (182 pages, 123ms). **Deploy pending** — throttle not yet cleared.

### What should happen next
- **Run 198:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Cryptocurrency Exchanges (separate from DeFi), Printing/Document Formatting, Robotics/IoT
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 196 — 2026-03-17 — Content (Configuration Management MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Configuration Management MCP Servers** (`content/reviews/configuration-management-mcp-servers.md`) — 161st review, one-hundred-forty-first beyond original list.
   - Ansible (6 servers): ansible/aap-mcp-server (22 stars, TypeScript, Apache-2.0 — official AAP MCP with Controller/Galaxy/Gateway/EDA), bsahane/mcp-ansible (25 stars, Python — advanced playbook/inventory/troubleshooting), sibilleb/AAP-Enterprise-MCP-Server (24 stars, Python — 47+ tools across AAP/EDA/Galaxy/lint/docs), mancubus77/mcp-server-aap (3 stars — lightweight AAP launcher), ansible-collections/ansible.mcp (1 star, GPL-3.0 — official Ansible Collection), redhat-cop/ansible.mcp_builder (1 star, GPL-3.0 — EE installer)
   - NixOS (3 servers): utensils/mcp-nixos (476 stars, Python, MIT — 130K+ packages, 23K+ options, Home Manager, nix-darwin, Nixvim, FlakeHub, Noogle), natsukium/mcp-servers-nix (215 stars, Nix, Apache-2.0 — 25 pre-configured modules), aloshy-ai/nix-mcp-servers (23 stars, Nix, MIT — declarative config for Claude/Cursor)
   - SaltStack: Bearbobs/saltstack-mcp (0 stars, Python, MIT — 4 tools for minion management)
   - Consul: kocierik/consul-mcp-server (16 stars, TypeScript, MIT — service discovery, KV store, 12+ tools)
   - Multi-tool: tarnover/mcp-sysoperator (26 stars, TypeScript, MIT — Ansible+Terraform+AWS), bjeans/homelab-mcp (18 stars, Python, MIT — 7 integrated servers), washyu/ansible-mcp-server (6 stars, archived Oct 2025 — 58 tools)
   - Gaps: no Puppet/Chef/CFEngine MCP servers, no drift detection, no compliance enforcement, no rollback management
   - 15+ servers across 5 subcategories, Rating: 3/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Configuration management" row to summary table
   - Updated review count to 161, rating distribution to include Configuration Management in 3.0 tier

3. **Built site** (180 pages, 117ms). **Deploy pending** — throttle not yet cleared.

### What should happen next
- **Run 197:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Cryptocurrency Exchanges (separate from DeFi), Browser Extension MCP Servers, Printing/Document Formatting
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 195 — 2026-03-17 — Content (Web Scraping & Crawling MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Web Scraping & Crawling MCP Servers** (`content/reviews/web-scraping-crawling-mcp-servers.md`) — 160th review, one-hundred-fortieth beyond original list.
   - Managed platforms: firecrawl/firecrawl-mcp-server (5,600 stars, TypeScript, MIT — scrape/crawl/map/search/extract, JS rendering, batch processing, 83% accuracy benchmark, 7s avg response), brightdata/brightdata-mcp (2,200 stars, TypeScript, MIT — Web Unlocker anti-bot, SERP API, Scraping Browser, 90% accuracy benchmark)
   - Open-source: Crawl4AI (58,000+ stars, Python, Apache-2.0 — local-first, LLM-ready markdown, multiple MCP wrappers including sadiuysal/crawl4ai-mcp-server and MaitreyaM/WEB-SCRAPING-MCP)
   - Web-to-markdown: jina-ai/MCP (official remote MCP — Reader API, ReaderLM-v2, web/image search, embeddings), wong2/mcp-jina-reader, spences10/mcp-jinaai-reader
   - Marketplaces: apify/apify-mcp-server (896 stars, TypeScript, Apache-2.0 — 5,000+ pre-built scrapers for social/search/e-commerce, dropping SSE April 2026)
   - Commercial APIs: crawlbase/crawlbase-mcp (8 stars, 70,000+ devs), ScrapingBee MCP (HTML/screenshots/files), Nimbleway MCP (7 tools, multi-engine search, e-commerce templates)
   - Utilities: mukul975/mcp-web-scrape (robots.txt compliant), olostep/olostep-mcp-server (batch 10K URLs), scrapoxy/scrapy-mcp-server (self-healing spider repair)
   - Gaps: no unified orchestration, limited schema-driven extraction, no proxy pool management MCP, no scraping scheduling, minimal legal compliance
   - 20+ servers across 6 subcategories, Rating: 4.5/5 — highest category rating

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Web scraping / crawling" row to summary table
   - Updated review count to 160, rating distribution to include Web Scraping/Crawling in 4.5 tier

3. **Built site** (180 pages, 116ms). **Deploy pending** — throttle not yet cleared.

### What should happen next
- **Run 196:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Cryptocurrency Exchanges (separate from DeFi), Browser Extension MCP Servers, Configuration Management
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 194 — 2026-03-17 — Content (Code Quality, Linting & Static Analysis MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Code Quality, Linting & Static Analysis MCP Servers** (`content/reviews/code-quality-linting-mcp-servers.md`) — 159th review, one-hundred-thirty-ninth beyond original list.
   - Cross-language: isaacphi/mcp-language-server (1,500 stars, Go, BSD-3-Clause — LSP bridge exposing diagnostics/definitions/references/hover/rename for gopls, rust-analyzer, pyright, TypeScript, clangd)
   - Static analysis: SonarSource/sonarqube-mcp-server (424 stars, Java — official, project metrics/issues/security hotspots/snippet analysis), semgrep/mcp (639 stars, Python — 5,000+ security rules, archived Oct 2025 → main repo), advanced-security/codeql-development-mcp-server (8 stars, TypeScript — CodeQL query development for 9 languages)
   - JavaScript/TypeScript: ESLint MCP (@eslint/mcp — built into ESLint 27,200 stars, native MCP support), RyuzakiShinji/biome-mcp-server (4 stars, unofficial Biome), ncalteen/prettier-mcp (1 star, Prettier formatting)
   - Python: Anselmoo/mcp-server-analyzer (5 stars — Ruff + Vulture + quality scoring), MarcusJellinghaus/mcp-code-checker (14 stars — pylint + pytest + mypy), drewsonne/ruff-mcp-server (1 star — Ruff check/format/fix)
   - Rust: lh/rust-mcp-server (1 star — cargo check/clippy/rustfmt/test/build)
   - Enterprise: wadew/sonar-mcp (0 stars — 21 SonarQube tools, 6 prompts, 7 resources)
   - Gaps: no official Prettier/Biome/Stylelint MCP, no golangci-lint/Checkstyle/PHPStan, no CI/CD integration, no code coverage, most servers early-stage
   - 15+ servers across 6 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Code quality / linting" row to summary table
   - Updated review count to 159, rating distribution to include Code Quality/Linting in 3.5 tier

3. **Built site** (179 pages, 117ms). **Deploy pending** — throttle not cleared (~49 min elapsed of 60).

### What should happen next
- **Run 195:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Cryptocurrency Exchanges (separate from DeFi), Serverless Monitoring/Observability, Web Scraping/Crawling (separate from existing)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 193 — 2026-03-17 — Content (Serverless & FaaS MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Serverless & FaaS MCP Servers** (`content/reviews/serverless-faas-mcp-servers.md`) — 158th review, one-hundred-thirty-eighth beyond original list.
   - AWS Lambda & Serverless: awslabs/mcp (8,500 stars, Python/TS, Apache-2.0 — official monorepo with 14+ servers including AWS Serverless and Lambda Tool servers), awslabs/run-model-context-protocol-servers-with-aws-lambda (350 stars — stdio-to-Lambda bridge, 4 deployment options), danilop/MCP2Lambda (110 stars, Python, MIT — Lambda-to-LLM bridge, auto-discovery), fredericbarthelet/middy-mcp (38 stars, TypeScript, MIT — Middy middleware), eleva/serverless-mcp-server (18 stars, JavaScript, MIT — Serverless Framework template)
   - Cloudflare Workers: cloudflare/mcp-server-cloudflare (3,500 stars, TypeScript, Apache-2.0 — 16 specialized remote MCP servers), cloudflare/mcp (263 stars — 2,500+ API endpoints via 2 tools, Code Mode pattern), cloudflare/workers-mcp (627 stars — TypeScript method-to-MCP auto-conversion)
   - Azure Functions: Azure/azure-functions-mcp-extension (32 stars, C#, MIT — official extension, .NET/Python/Java/TypeScript)
   - Google Cloud: GoogleCloudPlatform/cloud-run-mcp (559 stars, JavaScript, Apache-2.0 — deploy to Cloud Run), googleapis/gcloud-mcp (706 stars, TypeScript — 40+ tools across 4 servers)
   - Vercel: vercel/mcp-handler (573 stars, TypeScript, Apache-2.0 — Next.js/Nuxt adapter), Quegenx/vercel-mcp-server (60 stars — deployment management)
   - Firebase: gannonh/firebase-mcp (241 stars, TypeScript, MIT — Firestore/Storage/Auth)
   - Frameworks: fiberplane/mcp-lite (99 stars — zero-dependency framework for 5+ runtimes), mahmoudfazeli/cloudflare-mcp-template (2 stars — plugin template with OAuth 2.1)
   - Gaps: no unified multi-cloud serverless management, no cost optimization, no cold start analysis, no OpenFaaS/Knative, no serverless CI/CD integration, limited function versioning
   - 25+ servers across 7 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Serverless / FaaS" row to summary table
   - Updated review count to 158, rating distribution to include Serverless/FaaS in 4.0 tier

3. **Built site** (178 pages, 117ms). **Deploy pending** — throttle not cleared (~40 min elapsed of 60).

### What should happen next
- **Run 194:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Printing/Document Formatting, Cryptocurrency Exchanges (separate from DeFi), Serverless Monitoring/Observability
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 192 — 2026-03-17 — Content (Container, Docker & Kubernetes MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Container, Docker & Kubernetes MCP Servers** (`content/reviews/container-docker-kubernetes-mcp-servers.md`) — 157th review, one-hundred-thirty-seventh beyond original list.
   - Docker Management: ckreiling/mcp-server-docker (687 stars, Python, GPL-3.0 — container/image/network/volume management, plan+apply compose workflow), QuantGeekDev/docker-mcp (454 stars, Python, MIT — compose-focused), williajm/mcp_docker (3 stars, Python, MIT — 33 tools across 5 categories, three-tier safety system SAFE/MODERATE/DESTRUCTIVE, fuzz testing)
   - Kubernetes Orchestration: containers/kubernetes-mcp-server (1,300 stars, Go, Apache-2.0 — Red Hat-backed native Go API, 40 tools, Helm/KubeVirt/Kiali), rohitg00/kubectl-mcp-server (848 stars, Python, MIT — 253 tools, cost optimization, RBAC auditing), Flux159/mcp-server-kubernetes (1,300 stars, TypeScript — OpenTelemetry tracing, 772 commits)
   - Docker Official: docker/mcp-gateway (1,300 stars, Go, MIT — Docker Desktop MCP Toolkit, container isolation, OAuth, profiles, 865 commits), docker/hub-mcp (130 stars, TypeScript, Apache-2.0 — Docker Hub search/repository management), docker/mcp-registry (453 stars, Go, MIT — curated catalog with cryptographic signatures and SBOMs)
   - Container Runtimes: manusa/podman-mcp-server (61 stars, Go, Apache-2.0 — Podman + Docker, dual backends API/CLI)
   - Portainer: portainer/portainer-mcp (127 stars, Go, Zlib — enterprise container management, stack/user/team ops)
   - Helm: zekker6/mcp-helm (21 stars, Go, MIT — 7 tools, HTTP + OCI registry support)
   - Gaps: no Docker Swarm, no container security scanning (Trivy/Grype), no multi-cluster federation, no cloud K8s cost management, no GitOps (ArgoCD/Flux), limited service mesh
   - 20+ servers across 6 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Container / Docker / Kubernetes" row to summary table
   - Updated review count to 157, rating distribution to include Container/Docker/Kubernetes in 4.0 tier

3. **Built site** (177 pages, 116ms). **Deploy pending** — throttle not cleared (~31 min elapsed of 60).

### What should happen next
- **Run 193:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Printing/Document Formatting, Cryptocurrency Exchanges (separate from DeFi), Serverless/FaaS Management
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 191 — 2026-03-17 — Content (Package Management & Dependency MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Package Management & Dependency MCP Servers** (`content/reviews/package-management-dependency-mcp-servers.md`) — 156th review, one-hundred-thirty-sixth beyond original list.
   - Multi-Registry Version Checkers: sammcj/mcp-package-version (121 stars, Go, MIT — npm/PyPI/Maven/Go/Swift/Docker/GHCR/GitHub Actions), MShekow/package-version-check-mcp (5 stars, Python, Apache-2.0 — 10+ language registries + DevOps + ~1000 dev tools via mise), Tripletex/mcp-dependency-version (TypeScript/Deno — 12 registries, OSV vulnerability scanning), Artmann/package-registry-mcp (35 stars, TypeScript, MIT — 6 registries + GitHub Security Advisories), niradler/dependency-mcp (TypeScript — 7 registries, batch up to 100 packages)
   - npm-Specific: pinkpixel-dev/npm-helper-mcp (8 stars, MIT — peer conflict resolution, iterative testing), devlimelabs/npm-manage-mcp (MIT — full lifecycle, 13+ tools)
   - PyPI-Specific: loonghao/pypi-query-mcp-server (18 stars, Python — 25 tools, dependency resolution, download stats, trending, private registry support)
   - Maven/JVM: Bigsy/maven-mcp-server (31 stars, JavaScript, MIT — Maven/Gradle/SBT/Mill formats), danielscholl/maven-mcp-server (Python — batch, semantic versioning)
   - Security: SocketDev/socket-mcp (89 stars, MIT — supply chain security scores, zero-setup hosted at mcp.socket.dev), snyk/agent-scan (1,900 stars, Apache-2.0 — SCA/SAST/IaC, 15+ security risk types for MCP servers)
   - Ecosystem-Specific: CocoaPods README MCP (TypeScript, MIT), Composer/Packagist MCP
   - Gaps: no lock file parsing, no automated update PRs (Renovate/Dependabot-style), no license compliance, no SBOM generation, no monorepo analysis, limited private registry auth
   - 20+ servers across 5 subcategories, Rating: 3/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Package management / dependency" row to both summary tables
   - Updated review count to 156, rating distribution to include Package Management/Dependency in 3.0 tier

3. **Built site** (176 pages, 113ms). **Deploy pending** — throttle not cleared (~24 min elapsed of 60).

### What should happen next
- **Run 192:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Printing/Document Formatting, Cryptocurrency Exchanges (separate from DeFi), Container/Docker Management
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 190 — 2026-03-17 — Content (Cryptocurrency & DeFi MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Cryptocurrency & DeFi MCP Servers** (`content/reviews/cryptocurrency-defi-mcp-servers.md`) — 155th review, one-hundred-thirty-fifth beyond original list.
   - Multi-Chain Infrastructure: goat-sdk/goat (966 stars, TypeScript, MIT — 200+ onchain actions, largest agentic finance toolkit), coinbase/agentkit (1,200 stars — MCP extension, 50+ action providers, CDP/Privy/Viem wallets), base/base-mcp (342 stars, TypeScript, MIT — Base network + Coinbase API), mcpdotdirect/evm-mcp-server (362 stars, TypeScript — 60+ EVM networks, 22 tools, ENS), strangelove-ventures/web3-mcp (93 stars, TypeScript, Apache-2.0 — Ethereum/Solana/Cardano/THORChain/XRP/Bitcoin/TON), tatumio/blockchain-mcp (14 stars, TypeScript, MIT — 130+ networks)
   - Solana: sendaifun/solana-mcp (153 stars, Apache-2.0 — 40+ Solana actions via Solana Agent Kit), dcSpark/mcp-cryptowallet-solana, paulfruitful/WalletMCP
   - Wallets: phantom/mcp-server (official Phantom — transaction signing, swaps, scoped permissions, Solana+EVM), Trust Wallet AI Developer Stack, Bitget Wallet MCP (9+ networks), armorwallet/armor-crypto-mcp (DCA, stop-loss)
   - DeFi Protocols: nirholas/UCAI (ABI-to-MCP generator for any smart contract), Tairon-ai/aave-mcp (Aave V3 on Base), kukapay/uniswap-trader-mcp (8+ chains), qingfeng/defi-rates-mcp (14+ lending protocols)
   - Market Data: coinpaprika/dexpaprika-mcp (5M+ tokens, 20+ blockchains), CoinGecko/CoinMarketCap/CoinCap/CoinStats MCPs, whale-tracker-mcp, crypto-feargreed-mcp, cryptopanic-mcp-server, binance-mcp
   - Blockchain Data: mcp-etherscan-server, heurist-mesh-mcp-server, ergo-mcp
   - Payments: lightning-mcp (Bitcoin Lightning), zbd-mcp-server (Lightning micropayments), mcp-free-usdc-transfer (gasless USDC on Base)
   - NFTs: OpenSea MCP (official beta — 20+ blockchains, rarity scores, marketplace data)
   - Security: ChainGuard (multi-chain crime detection)
   - Gaps: no CEX trading execution, no derivatives/options/futures, no portfolio rebalancing, no crypto tax reporting, no cross-chain bridge execution, limited audit tooling, wallet security concerns
   - 50+ servers across 8 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Cryptocurrency / DeFi" row to both summary tables
   - Updated review count to 155, rating distribution to include Cryptocurrency/DeFi in 4.0 tier

3. **Built site** (175 pages, 112ms). **Deploy pending** — throttle not cleared (~15 min elapsed of 60).

### What should happen next
- **Run 191:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Package Management/Dependency, Printing/Document Formatting, Cryptocurrency Exchanges (could be separate from DeFi)
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 189 — 2026-03-17 — Content (Spreadsheet & Office Suite MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Spreadsheet & Office Suite MCP Servers** (`content/reviews/spreadsheet-office-suite-mcp-servers.md`) — 154th review, one-hundred-thirty-fourth beyond original list.
   - Google Workspace: taylorwilsdon/google_workspace_mcp (1,800 stars, Python, MIT — 12+ services: Gmail, Drive, Docs, Sheets, Slides, Calendar, Forms, Tasks, Chat, Contacts, Search, Apps Script), ngs/google-mcp-server (multi-account), j3k0/mcp-google-workspace (Gmail + Calendar), MarkusPfundstein/mcp-gsuite
   - Google Sheets (8+ implementations — most fragmented subcategory): xing5/mcp-google-sheets (737 stars, Python — 19 tools, 4 auth methods, uvx), mkummer225, domdomegg, shionhonda, freema, isaacphi/mcp-gdrive, ajaysmb, kazz187
   - Google Docs: a-bonus/google-docs-mcp (377 stars, TypeScript, MIT — Docs/Sheets/Drive with formatting, comments, templates, multi-tab)
   - Excel: negokaz/excel-mcp-server (878 stars, Go, MIT — 7 tools, cross-platform, formulas, screenshots), sbroenne/mcp-server-excel (76 stars, C# — 25 tools, 225+ operations via COM — Power Query, DAX, VBA, PivotTables, Charts), haris-musa, yzfly, guillehr2, ArchimedesCrypto
   - Microsoft Word: GongRzhe/Office-Word-MCP-Server (1,700 stars, Python — creation/formatting/tables/images/PDF conversion/protection/comments/footnotes), dvejsada/mcp-ms-office-documents (18 stars, MIT — PPTX/DOCX/XLSX/email, cloud storage, templates)
   - LibreOffice: WaterPistolAI/libreoffice-mcp (17 stars — Writer/Calc/Impress/Draw/Base), patrup/mcp-libre (embedded), harshithb3304/libre-office-mcp
   - Generic: PSU3D0/spreadsheet-mcp (39 stars, Rust — token-efficient, formula engine, batch ops, diff detection)
   - Full Office Suite: OfficeMCP/OfficeMCP (63 stars — Word/Excel/Outlook/PowerPoint/Access/OneNote/Visio/Project via COM), microsoft/mcp (2,800 stars — official Azure + Fabric catalog)
   - Gaps: no real-time collaborative editing, no OneDrive MCP, no Apple Numbers, no conflict resolution for concurrent edits
   - 35+ servers across 6 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Spreadsheet / office suite" row to both summary tables
   - Updated review count to 154, rating distribution to include Spreadsheet/Office Suite in 4.0 tier

3. **Built site** (174 pages, 109ms). **Deploy pending** — throttle not cleared (~7 min elapsed of 60).

### What should happen next
- **Run 190:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Cryptocurrency/DeFi, Package Management/Dependency, Printing/Document Formatting
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 188 — 2026-03-16 — Content (Apple & macOS MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Apple & macOS MCP Servers** (`content/reviews/apple-macos-mcp-servers.md`) — 153rd review, one-hundred-thirty-third beyond original list.
   - Comprehensive Apple Integration: supermemoryai/apple-mcp (3,000 stars, TypeScript — Notes, Reminders, Calendar, Contacts, Mail, Messages, Music, Finder with explicit permission system)
   - macOS Automation: steipete/macos-automator-mcp (709 stars — 200+ AppleScript/JXA recipes, knowledge base, custom skills, npm published), joshrutkowski/applescript-mcp (system functions, files, notifications), peakmojo/applescript-mcp (simple execution)
   - Siri Shortcuts: dvcrn/mcp-server-siri-shortcuts, recursechat/mcp-server-apple-shortcuts, CaseyRo/mac_shortcuts_mcp (Python)
   - HomeKit: somethingwithproof/home-mcp (devices/scenes/automations), jaebinsim/HomeMCP (zero-infrastructure via iOS Shortcuts), omarshahine/HomeClaw (Catalyst app — lights/locks/thermostats)
   - Apple Music: 4+ servers — kennethreitz/mcp-applemusic, samwang0723/mcp-applemusic, epheterson/mcp-applemusic (REST API), pedrocid/music-mcp
   - Notes & Reminders: karlhepler/apple-mcp (CRUD for both), mggrim/apple-reminders-mcp-server (18 tools, NLP dates), FradSer/mcp-server-apple-events (native EventKit)
   - iCloud: iteratio/icloud-mcp (Calendar/Mail/Reminders, Keychain credentials)
   - Screenshots: steipete/Peekaboo (VQA-enabled), jhead/macos-screen-mcp
   - Safari: lxman/safari-mcp-server; Clipboard: vlad-ds/maccy-clipboard-mcp; Raycast: ExpertVagabond/raycast-mcp-server (9 tools)
   - Gaps: no Xcode, no System Settings, no Time Machine, no AirDrop, no Keychain passwords, no Focus mode
   - 30+ servers across 7 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Apple / macOS" row to both summary tables
   - Updated review count to 153, rating distribution to include Apple/macOS in 4.0 tier

3. **Built site** (173 pages, 117ms). **Deploy pending** — throttle not cleared (~6 min remaining).

4. **Note:** Initially attempted Mining & Natural Resources but it overlapped heavily with existing Energy/Utilities, Geospatial/Mapping, and Weather/Climate reviews. Also checked Food & Beverage — already covered. Pivoted to Apple & macOS which proved rich.

### What should happen next
- **Run 189:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Spreadsheet/Office (Google Sheets, Excel, Word, Docs), Package Management/Dependency, Cryptocurrency/DeFi
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 187 — 2026-03-16 — Content (Automotive & Vehicle MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Automotive & Vehicle MCP Servers** (`content/reviews/automotive-vehicle-mcp-servers.md`) — 152nd review, one-hundred-thirty-second beyond original list.
   - Tesla (most implementations, 3+): cobanov/teslamate-mcp (120 stars, Python — 18 predefined queries for battery/efficiency/charging/driving plus custom SQL), scald/tesla-mcp (11 stars, TypeScript — Fleet API control via OAuth 2.0), keithah/tessie-mcp (39+ tools — efficiency trends, smart charging, FSD detection via Tessie API)
   - Vehicle Diagnostics: castlebbs/Vehicle-Diagnostic-Assistant (MCP server on embedded hardware — W600 MCU, OBD-II WiFi dongle, ELM327 driver, DTC reading), farzadnadiri/MCP-CAN (MIT — virtual CAN bus simulation, DBC decoding, ECU simulator, no hardware required)
   - EV Charging: Abiorh001/mcp_ev_assistant_server (OpenCharge Map + Google Maps), cevatkerim/chargenow-mcp (ChargeNow network), emporiaenergy/emporia-mcp (official, beta — EV charging reports + energy monitoring)
   - Vehicle Data & VIN: carsxe/carsxe-mcp-server (12 stars, MIT — VIN/specs/history/recalls/market value/license plate OCR), keptlive/vin-mcp (VIN structure decoding)
   - Car Marketplace: SiddarthaKoppaka/car_deals_search_mcp (Cars.com, Autotrader, KBB aggregation with CARFAX filters)
   - Connected Vehicle / SDV: emqx/sdv-mcp-demo (MCP over MQTT, edge processing), gperezt222/flespi-mcp-server (157 tools — fleet management/telemetry)
   - Maps & Navigation (automotive-adjacent): mapbox, Google Maps, TomTom, Baidu Maps (all official)
   - Gaps: no BMW/Mercedes/Hyundai/Ford brand-specific servers, no ADAS/autonomous driving, no insurance/claims, no parking, no ride-sharing
   - 20+ servers across 6 subcategories, Rating: 3/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Automotive / vehicle" row to summary table
   - Updated review count to 152

3. **Built site** (172 pages, 111ms). **Deploy pending** — throttle not cleared (~16 min remaining).

### What should happen next
- **Run 188:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Mining/Natural Resources, Food & Beverage/Restaurant, Fashion/Apparel
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 186 — 2026-03-16 — Content (Social Networking & Community MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Social Networking & Community MCP Servers** (`content/reviews/social-networking-community-mcp-servers.md`) — 151st review, one-hundred-thirty-first beyond original list.
   - Twitter/X (most implementations, 8+): EnesCinr/twitter-mcp (373 stars, TypeScript — posting/searching), crazyrabbitLTC/mcp-twitter-server (53 tools — 33 Twitter API + 20 SocialData.tools research), adhikasp/mcp-twikit (Twikit, no API key), ryanmac/agent-twitter-client-mcp (elizaOS), lord-dubious/x-mcp, BioInfo/x-mcp-server, Dishant27/twitter-mcp, Rakibulislamsarkar/twitter-mcp
   - Bluesky / AT Protocol: semioz/bluesky-mcp (official MCP repo featured — posting/liking/reposting/timeline), cameronrye/atproto-mcp (full AT Protocol), brianellin/bsky-mcp-server (search/time filtering), morinokami/mcp-server-bluesky, berlinbra/BlueSky-MCP
   - LinkedIn: adhikasp/mcp-linkedin (177 stars — feeds/jobs), felipfr/linkedin-mcpserver (official API, OAuth 2.0), anysiteio/anysite-mcp-server (multi-platform), stickerdaniel, Dishant27, alinaqi
   - Reddit: Hawstein/mcp-server-reddit (66 stars — frontpage/subreddits/comments), eliasbiondo/reddit-mcp-server (zero-config, no API keys), adhikasp/mcp-reddit, aflekkas, jordanburke, zicochaos, Arindam200
   - Discord: HardHeadHackerHead/discord-mcp (134 tools, 20 categories), glittercowboy/discord-mcp (128 operations), barryyip (71 stars), SaseQ, hanweg
   - Fediverse/Mastodon: cameronrye/activitypub-mcp (ActivityPub — Mastodon/Pleroma/Misskey)
   - YouTube: 6+ servers (dannySubsense 14 tools via Data API v3, anaisbetts yt-dlp, ZubeidHendricks, minbang930 Gemini Vision, nattyraz, adhikasp)
   - TikTok: Seym0n/tiktok-mcp (virality analysis, ASR), yap-audio (trending), AdsMCP (ads), ysntony (ads), gyoridavid (short video maker)
   - Hacker News: 5+ implementations
   - Gaps: no Threads (Meta), no Pinterest, no Snapchat, no WeChat/Weibo, no Twitch chat, no community moderation AI, no cross-platform analytics
   - 50+ servers across 8 subcategories, Rating: 4.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Social networking / community" row to summary table
   - Updated review count to 151

3. **Built site** (172 pages, 113ms). **Deploy pending** — throttle not cleared (~35 min elapsed of 60).

### What should happen next
- **Run 187:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Mining/Natural Resources, Food & Beverage/Restaurant, Automotive
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 185 — 2026-03-16 — Content (Podcasting & Audio Content MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Podcasting & Audio Content MCP Servers** (`content/reviews/podcasting-audio-content-mcp-servers.md`) — 150th review, one-hundred-thirtieth beyond original list.
   - Text-to-Speech (most populated): elevenlabs/elevenlabs-mcp (1,100 stars, Python — official, TTS/voice cloning/transcription/sound effects, most comprehensive audio MCP), blacktop/mcp-tts (multi-engine: macOS say, ElevenLabs, Google Gemini, OpenAI), MiniMax-AI/MiniMax-MCP (421 stars — TTS/voice cloning/music/image/video), hammeiam/koroko-speech-mcp (MIT, Kokoro TTS, local, free), digitarald/chatterbox-mcp (local, auto-playback), Edge TTS servers (free, no API key), nakamurau1/tts-mcp (OpenAI TTS)
   - Speech-to-Text: SmartLittleApps/local-stt-mcp (whisper.cpp, Apple Silicon, diarization, 100% local), arcaputo3/mcp-server-whisper (MIT, Whisper + GPT-4o), ebmarquez/audio-transcription-mcp (Faster-Whisper + pyannote, Docker), Kvadratni/speech-mcp (~80 stars, bidirectional voice: Faster-Whisper + Kokoro TTS), Azure MCP Server
   - Music Generation & DAW: shiehn/total-reaper-mcp (27 stars, 600+ tools, 100% ReaScript), 4 more REAPER servers, pasie15/mcp-server-musicgpt (24 tools), falahgs/mcp-minimax-music-server, tubone24/midi-mcp-server, williamzujkowski/strudel-mcp-server (live coding)
   - Voice Interaction: Kvadratni/speech-mcp (~80 stars — full conversational voice loop)
   - Podcast Feed Management: 6+ RSS/Atom feed servers
   - Streaming Platform: 5+ Spotify MCP servers
   - Gaps: no podcast hosting integrations, no analytics, no episode scheduling, no show notes generation, no mastering pipelines, no distribution, no audiograms, no chapter markers, no Ableton/Logic/FL Studio
   - 30+ servers across 6 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Podcasting / audio content" row to summary table
   - Updated review count to 150

3. **Built site** (171 pages, 111ms). **Deploy pending** — throttle not cleared (~36 more minutes).

### What should happen next
- **Run 186:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Mining/Natural Resources, Social Networking/Community, Sports/Fitness
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 184 — 2026-03-16 — Content (Presentation & Slides MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Presentation & Slides MCP Servers** (`content/reviews/presentation-slides-mcp-servers.md`) — 149th review, one-hundred-twenty-ninth beyond original list.
   - PowerPoint/PPTX Generation: GongRzhe/Office-PowerPoint-MCP-Server (1,600 stars, Python — 34 tools across 11 modules, templates/charts/themes/picture effects/font analysis, the most comprehensive presentation MCP), supercurses/powerpoint (144 stars, MIT, Python — the original, 10 tools, AI images via TogetherAI), ltc6539/mcp-ppt (65 stars, Python — SVG integration, 14 tools), Ichigo3766/powerpoint-mcp (51 stars, MIT — Stable Diffusion fork), socamalo/PPT_MCP_Server (42 stars, MIT — Windows COM, live PowerPoint control)
   - Google Slides: matteoantoci/google-slides-mcp (157 stars, TypeScript — OAuth 2.0, 5 tools, batch updates, summarization)
   - Markdown-Based Slides: masaki39/marp-mcp (5 stars, MIT, TypeScript — Marp ecosystem, 4 themes, 5 styles, Claude Code skill), bsmnyk/mdslides-mcp-server (6 stars, MIT, Python — Reveal.js, 12 themes, Docker)
   - Commercial/SaaS: SlideSpeak/slidespeak-mcp (12 stars, Python — API-powered, Docker deployment)
   - Gaps: no Keynote, no Canva, no Figma Slides, no Prezi, no collaborative editing, no template marketplaces, no presentation analytics, no accessibility checking, no brand compliance
   - 15+ servers across 4 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Presentation / slides" row to summary table
   - Updated review count to 149

3. **Built site** (170 pages, 114ms). **Deploy pending** — throttle not cleared (~42 more minutes).

### What should happen next
- **Run 185:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Mining/Natural Resources, Podcasting/Audio Content, Social Networking/Community
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 183 — 2026-03-16 — Content (Science & Research MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Science & Research MCP Servers** (`content/reviews/science-research-mcp-servers.md`) — 148th review, one-hundred-twenty-eighth beyond original list.
   - Academic Paper Search (most populated subcategory): blazickjp/arxiv-mcp-server (2,400 stars, Apache-2.0, Python — 4 tools, paper search/download/storage/analysis, most popular science MCP), openags/paper-search-mcp (796 stars, MIT, Python — 7 sources: arXiv, PubMed, bioRxiv, medRxiv, Google Scholar, IACR, Semantic Scholar), benedict2310/Scientific-Papers-MCP (44 stars, TypeScript — 6 sources covering 400M+ papers including OpenAlex/CORE), JackKuo666/semanticscholar-MCP-Server (52 stars, MIT, Python — citation network), 4+ more Semantic Scholar implementations, mcp-for-research (consolidated 5 tools)
   - Scientific Computing: pathintegral-institute/mcp.science (117 stars, MIT, Python — 12+ servers: sandboxed Python, Materials Project, GPAW DFT, Mathematica, Jupyter), Wolfram-MCP (6 stars, MIT, 11 symbolic math tools), 5 Wolfram Alpha API servers, mcp-server-mathematica (wolframscript execution), calculator-mcp-server
   - Bioinformatics & Life Sciences: Augmented-Nature/UniProt-MCP-Server (18 stars, TypeScript — 26 tools across 6 categories), PDB-MCP-Server (21 stars, JavaScript — protein structure search/quality validation), QuentinCody/uniprot-mcp-server (BLAST + cross-database mapping), bio-mcp BLAST
   - Earth & Space Science: blake365/usgs-quakes-mcp (earthquake data), jezweb/nasa-mcp-server (8 stars, APOD/Mars/asteroids/Earth imagery)
   - Gaps: no ELN, no LIMS, no chemistry/molecular modeling, no genomics (GenBank, Ensembl), no physics simulation, no observatory data, no clinical trials, no patent search, no research funding databases
   - 35+ servers across 5 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Science / research" row to summary table
   - Updated review count to 148

3. **Built site** (169 pages, 115ms). **Deploy pending** — throttle not cleared (~52 more minutes).

### What should happen next
- **Run 184:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Printing/Publishing, Mining/Natural Resources, Podcasting/Audio Content
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 182 — 2026-03-16 — Content (Telecommunications & Messaging MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Telecommunications & Messaging MCP Servers** (`content/reviews/telecommunications-messaging-mcp-servers.md`) — 147th review, one-hundred-twenty-seventh beyond original list.
   - SMS/CPaaS (8 official providers): twilio-labs/mcp (official, TypeScript, MIT — 1,400+ API endpoints, OpenAPI-to-MCP generator), team-telnyx/telnyx-mcp-server (official, 22 stars, Python — call control, SMS/MMS, number management, webhooks), Bandwidth/mcp-server (official, Python — enterprise voice/messaging/911), plivo/mcp (official — send_sms, make_call), sinch/sinch-mcp-server (official, TypeScript — text/media/template messages, voice, conference management), infobip/mcp (official, MIT — SMS/WhatsApp/Viber/RCS, bulk, scheduling, delivery reports), ClickSend (official — SMS/MMS), Vonage (3 official servers — docs, telephony, API bindings)
   - Voice & Telephony: voice-call-mcp-server (MIT, Twilio + OpenAI GPT-4o Realtime), callcenter.js-mcp (VoIP/SIP + OpenAI), LiveKit agents (native MCP support)
   - WhatsApp: lharries/whatsapp-mcp (5,300 stars, MIT, Python/Go — most popular messaging MCP), whatsapp-mcp-extended (41 tools), 4 more alternatives
   - Telegram: sparfenyuk/mcp-telegram (172 stars, MIT, MTProto), chigwell/telegram-mcp (Telethon, full access), 4 more
   - Matrix: mjknowles/matrix-mcp-server (30 stars, MIT, TypeScript, OAuth 2.0, 15 tools)
   - iMessage: 4 servers (macOS-only, various approaches)
   - WeChat: BiboyQG/WeChat-MCP (macOS Accessibility API), WeCom bot server
   - Multi-channel: trycourier/courier-mcp (official — email/SMS/push/WhatsApp/Slack/Teams/Discord)
   - 3GPP Standards: edhijlu/3gpp-mcp-server (12 stars, BSD-3, 535M word dataset), mcp-server-3gpp (17 specs, 107MB data)
   - Gaps: no PBX (Asterisk/FreeSWITCH), no SIP management, no telecom BSS/OSS, no spectrum management, no number portability, no contact center platforms, no UCaaS
   - 50+ servers across 7 subcategories, Rating: 4.5/5 (highest vertical category rating)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Telecommunications / messaging" row to summary table
   - Updated review count to 147

3. **Built site** (168 pages, 106ms). **Deployed successfully.**

### What should happen next
- **Run 183:** Continue expanding coverage — potential categories: Printing/Publishing, Mining/Natural Resources, Telecommunications Infrastructure
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 181 — 2026-03-15 — Content (Insurance & InsurTech MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Insurance & InsurTech MCP Servers** (`content/reviews/insurance-insurtech-mcp-servers.md`) — 146th review, one-hundred-twenty-sixth beyond original list.
   - Policy Platforms: Root Platform MCP (official, TypeScript, MIT — quote creation, policy management, full insurance workflows, sandbox/production), Socotra MCP (commercial, most mature insurance MCP — full lifecycle, enterprise security, audit trails), wadhawan2411radhika/insurance-mcp-server (Python, 5 tools — premium tracking, customer search, SQLite)
   - Claims Processing: ClaimsProcessingAssistant-MCP (TypeScript — AI document analysis, Supabase, Redis), insurance-ai-mcp-server (Java/Python, Kafka microservices — enterprise claim orchestration)
   - Underwriting: Apify Insurance Underwriting Intelligence MCP (8 actors — multi-peril scoring, disaster history, seismic/flood, climate trajectory 5/10/25yr), imc-policy-mcp-server (Java, Spring AI 1.1.0, RAG-based policy retrieval)
   - Insurance Connectors: mcp-lemonade (Playwright-based Lemonade access), mcp-server-salesforce-insurance (TypeScript, MIT, 9+ tools, Salesforce PCM), swiss-health-mcp (1.6M Swiss premium records, 55 insurers), mcp-financial-services (TypeScript, MIT, SOC 2 certified)
   - Compliance: US_Compliance_MCP (Python — HIPAA, GLBA, NYDFS 500, NIST mappings), cow-mcp (33+ GRC tools)
   - Document Processing: Unstract MCP (commercial — ACORD forms, COIs, life insurance apps, healthcare claims)
   - Gaps: no actuarial modeling, no reinsurance, no ACORD data standards, no cat modeling (RMS/AIR), no agency management (Applied Epic/Vertafore), no life/annuity admin, no claims adjudication engines, no parametric insurance
   - 15+ servers across 6 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Insurance / InsurTech" row to summary table
   - Updated review count to 146

3. **Built site** (167 pages, 109ms). **Deploy pending** — throttle not cleared (need ~16 more minutes).

### What should happen next
- **Run 182:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Printing/Publishing, Mining/Natural Resources, Telecommunications
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 180 — 2026-03-15 — Content (Logistics & Supply Chain MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Logistics & Supply Chain MCP Servers** (`content/reviews/logistics-supply-chain-mcp-servers.md`) — 145th review, one-hundred-twenty-fifth beyond original list.
   - Shipping & Parcel: Shippo MCP (official, TypeScript — multi-carrier USPS/UPS/FedEx/DHL, label generation, rate shopping, tracking, address validation, customs, agentic shipping platform), UPS-API/ups-mcp (4 stars, Python, MIT — official UPS), bfrs/shiprocket-mcp (Indian e-commerce shipping, courier comparison), bischoff99/easypost_mcp_server (EasyPost multi-carrier abstraction)
   - Inventory & Warehouse: dbankscard/skuvault-mcp-server (Python — production-ready SkuVault, enterprise-grade rate limiting/caching/safety), YosefHayim/ebay-mcp (325 tools), Agiliron MCP, BoxHero MCP
   - Fleet & Telematics: gperezt222/flespi-mcp-server (157 tools, 1,000+ IoT device types)
   - Maritime: garrettXu/mcp-shipxy-api (9 stars, Python, MIT — vessel tracking, port data, route planning, weather/tides)
   - Software Supply Chain: securechaindev/securechain-mcp-server (multi-ecosystem vulnerability intelligence)
   - Gaps: no ERP (SAP, Oracle, Dynamics), no WMS (Manhattan, Blue Yonder), no TMS, no demand planning, no customs/compliance, no cold chain, no last-mile, no procurement, no freight marketplaces
   - 20+ servers across 5 subcategories, Rating: 3/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Logistics / supply chain" row to summary table
   - Updated review count to 145

3. **Built site** (166 pages, 103ms). **Deploy pending** — throttle not cleared.

### What should happen next
- **Run 181:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Insurance/InsurTech, Printing/Publishing, Mining/Natural Resources
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 179 — 2026-03-15 — Content (Hospitality & Hotels MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Hospitality & Hotels MCP Servers** (`content/reviews/hospitality-hotels-mcp-servers.md`) — 144th review, one-hundred-twenty-fourth beyond original list.
   - Vacation Rentals: openbnb-org/mcp-server-airbnb (393 stars, TypeScript, MIT, 2 tools — Airbnb listing search/details via HTML scraping, DXT format, no API key, advanced filtering by location/dates/guests/price), Domoteek/mcp-server-airbnb, vedantparmar12/airbnb-mcp (LiveKit voice)
   - Hotel Booking: jinkoso/jinko-mcp (TypeScript, 5 tools — 2M+ hotels, real booking with payment links, facility filtering, multi-language), soren-olympus/amadeus-mcp (Amadeus Travel API hotel list/search/booking), fiqcodes/amadeus-mcp-server (Python, MIT, flights/hotels/tours/activities with auto USD conversion), woodstocksoftware/hotel-concierge-mcp (Python, 7 tools, SQLite demo/reference implementation), esakrissa/hotels_mcp_server (Python, Booking.com API, minimal)
   - Restaurant Reservations: jrklein343-svg/restaurant-mcp (TypeScript, 12+ tools — unified Resy + OpenTable, reservation sniping, DPAPI encrypted credentials), musemen/resy-mcp-server (Python, Resy automation, encrypted tokens, waitlist, calendar), samwang0723/mcp-booking (Go, Google Maps Places API, mood/event matching, mock booking)
   - Review Platforms: Yelp/yelp-mcp (official, TypeScript, Fusion AI API, natural language search, conversational reservations), pab1it0/tripadvisor-mcp (46 stars, Python, MIT, TripAdvisor Content API, locations/reviews/photos/nearby)
   - Travel Planning: skarlekar/mcp_travelassistant (Python, 6 specialized servers — flights/hotels/events/geocoder/weather/finance)
   - Gaps: no PMS (Oracle Hospitality, Mews, Cloudbeds), no revenue management, no guest experience platforms, no food delivery, no hotel loyalty programs, no housekeeping/operations, no channel managers
   - 25+ servers across 6 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Hospitality / hotels" row to summary table
   - Updated review count to 144

3. **Built site** (165 pages, 106ms). **Deploy pending** — throttle not cleared.

### What should happen next
- **Run 180:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Insurance/InsurTech, Printing/Publishing, Logistics/Supply Chain
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 178 — 2026-03-15 — Content (Fashion, Beauty & Style MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Fashion, Beauty & Style MCP Servers** (`content/reviews/fashion-beauty-style-mcp-servers.md`) — 143rd review, one-hundred-twenty-third beyond original list.
   - Virtual Try-On: chatmcp/heybeauty-mcp (18 stars, TypeScript, MIT, 2 tools — HeyBeauty API, submit/query try-on tasks, cloth:// URIs)
   - Fashion Recommendation: attarmau/StyleCLIP (1 star, Python, Apache 2.0, 1 tool — YOLO clothing detection + CLIP feature extraction, React/FastAPI/MongoDB, AWS Rekognition)
   - AI Styling: findmine/findmine-mcp (1 star, TypeScript, MIT, 3 tools — complete-the-look, visually similar, style guides from FindMine commercial API)
   - Wardrobe Management: Caffeinated Wardrobe (commercial, $50/year — item tracking, outfit composition, wear history, weather/calendar-aware recommendations)
   - Beauty/Cosmetics: AlexLee-landscaper/K-Beauty-MCP (5 stars, Python, MIT, 7 tools — 58+ brands, 43+ product types, 48+ ingredients, AI skin analysis from selfies, personalized 10-step routines)
   - Color: deepakkumardewani/color-scheme-mcp (7 stars, TypeScript, 8 tools — monochrome/analogic/complementary/triadic/quadratic palettes), kelvinzer0/PaletteMCP
   - Gaps: no size/fit recommendation, no trend forecasting, no sustainable fashion, no textile design, no luxury brand APIs, no secondhand/resale, no fashion show data
   - 10+ servers across 5 subcategories, Rating: 2.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Fashion / beauty / style" row to summary table
   - Updated review count to 143

3. **Built site** (164 pages, 104ms). **Deploy pending** — throttle not cleared (~42 min remaining).

### What should happen next
- **Run 179:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Hospitality/Hotels, Printing/Publishing, Insurance/InsurTech
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 177 — 2026-03-15 — Content (Sports & Athletics MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Sports & Athletics MCP Servers** (`content/reviews/sports-athletics-mcp-servers.md`) — 142nd review, one-hundred-twenty-second beyond original list.
   - Multi-Sport: mikechao/balldontlie-mcp (23 stars, TypeScript, MIT — NBA/NFL/MLB, 4 tools), SportRadar MCP (NFL/NBA/NHL/Soccer/Tennis), ESPN Apify servers (12-56+ tools, no API key)
   - Basketball/NBA (6+ implementations): labeveryday/nba_mcp_server (6 stars, Python, MIT, 30 tools — advanced analytics, shot charts, hustle stats), nikhilkichili/nba-analytics-mcp (25+ tools, betting odds, ML game simulations)
   - Football/Soccer: obinopaul/soccer-mcp-server (4 stars, Python, MIT, 17 tools via API-Football), yeonupark/mcp-soccer-data (28 stars, live scores)
   - NHL: dylangroos/nhl-mcp (4 stars, TypeScript, MIT, 10 tools)
   - Formula 1 (7+ implementations): Panth1823/formula1-mcp (15 stars, TypeScript, 29 tools — OpenF1 + Ergast 1950-present), stagsz/F1-MCP-Server (12 tools, Monte Carlo simulation, tire degradation modeling)
   - Fantasy Sports: jdguggs10/flaim (TypeScript, MIT, 9 tools — ESPN/Yahoo/Sleeper), KBThree13/mcp_espn_ff (29 stars, Python, MIT)
   - Betting: WFord26/BetTrack (TypeScript, MIT, 30+ tools, 70+ markets), kitchenchem/degen-mcp, cloudbet/sports-mcp-server (10 stars, Go, MIT)
   - Fitness: r-huijts/strava-mcp (276 stars, TypeScript, MIT, 25 tools), Taxuspt/garmin_mcp (271 stars, Python, 96+ tools), gesteves/domestique (30+ tools, multi-platform)
   - Cycling: r-huijts/firstcycling-mcp (18 stars, Python, MIT, 20 tools — pro cycling data)
   - Cricket: tarun7r/cricket-mcp-server (11 stars, Python, MIT, 9 tools — Cricbuzz)
   - Gaps: no rugby, no tennis-specific, no Olympic data, no esports, no sports news aggregation
   - 50+ servers across 9 subcategories, Rating: 4/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Sports / athletics" row to summary table
   - Added sports/athletics entry to beyond-original-list section
   - Updated review count to 142

3. **Built site** (163 pages, 108ms). **Deploy pending** — throttle not cleared (~51 min remaining).

### What should happen next
- **Run 178:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Fashion/Apparel, Printing/Publishing, Hospitality/Hotels
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 176 — 2026-03-15 — Content (Nonprofit & Charity MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending inbox messages.

### What I did

1. **Wrote new review: Nonprofit & Charity MCP Servers** (`content/reviews/nonprofit-charity-mcp-servers.md`) — 141st review, one-hundred-twenty-first beyond original list.
   - Charity Verification (3 implementations): briancasteel/charity-mcp-server (22 stars, TypeScript, MIT — IRS EIN lookup, 4 tools + 14 prompt templates), asachs01/propublica-mcp (ProPublica Nonprofit Explorer, Form 990 data, 5 tools, financial trend analysis), conorheffron/mcp-charity (sample/demo)
   - Donor Management: Blackbaud Claude Connector (official, Raiser's Edge NXT, donor profiles/gifts/events/communications), CData Blackbaud MCP (commercial), Salesforce MCP (official + 5+ community, works with NPSP/Nonprofit Cloud), CiviCRM via Pipedream (14,000+ orgs)
   - Nonprofit Discovery: Benevity MCP (2.4M+ verified nonprofits worldwide, cause-based search), Candid MCP (free, funder search, leadership demographics, research reports)
   - Volunteer Impact: Goodera MCP (50,000+ nonprofit partners, 2M+ volunteers, impact reporting — first social impact company with MCP)
   - Humanitarian Data: dividor/hdx-mcp (33 tools, Python, MIT — UN OCHA Humanitarian Data Exchange, refugees/IDPs/food security/conflict/funding), humanitarian-mcp (negotiation frameworks for aid workers)
   - Civic Engagement: mikeomlor/nb-mcp (NationBuilder API, community management)
   - Platform-aggregated: Donorbox, Givebutter, Little Green Light via Zapier/Pipedream MCP
   - Gaps: no grant management/writing, no DonorPerfect/Bloomerang, no volunteer scheduling, no standalone impact measurement
   - 15+ servers across 7 subcategories, Rating: 3/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Nonprofit / charity" row to summary table
   - Added nonprofit/charity entry to beyond-original-list section
   - Updated review count to 141

3. **Built site** (162 pages, 104ms). **Deployed** (162 pages).

### What should happen next
- **Run 177:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Fashion/Apparel, Sports Analytics, Printing/Publishing, Hospitality/Hotels
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 175 — 2026-03-15 — Inbox + Content (News, Media & Journalism MCP Servers Review)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- **#170 (high priority)**: Rob says backup retention of 24 is overkill — just keep 2 → Done. Changed MAX_BACKUPS default from 24 to 2 in scripts/backup.sh.
- **#169 (high priority)**: Reply to old seen-but-not-replied messages → Done. Replied to all 14 old seen messages (#74, #89, #95, #134, #136, #137, #138, #139, #140, #141, #151, #152, #153, #161) with status updates so Rob can archive them.

### What I did

1. **Fixed backup retention** (`scripts/backup.sh`) — per inbox #170, changed default from 24 to 2 backups. Cron still runs hourly but only retains the 2 most recent bundles + config tarballs.

2. **Replied to all old inbox messages** — per inbox #169, used mark_inbox_done with response text on all 14 seen-but-pending messages. Each reply summarizes what was done.

3. **Wrote new review: News, Media & Journalism MCP Servers** (`content/reviews/news-media-journalism-mcp-servers.md`) — 140th review, one-hundred-twentieth beyond original list.
   - RSS Aggregation (10+ implementations): imprvhub/mcp-rss-aggregator (24 stars, Python — OPML import), RSSidian (24 stars — Obsidian bridge, semantic search), rss-news-analyzer-mcp (trend detection, spike analysis), 5+ additional implementations
   - Hacker News (8+ implementations — one of the most MCP-served single platforms): rawveg/hacker-news-mcp (multi-transport STDIO/SSE/REST, natural language, trend analysis), 7+ additional implementations
   - News APIs: @newsmcp/server (free, no API key, events clustered from hundreds of sources, 12 topics, 30+ regions), guangxiangdebizi aggregator (5 APIs with failover), @angheljf/nyt, Dappier (commercial, rights-cleared)
   - Product Hunt: jaipandya/producthunt-mcp-server (trending posts, collections, users)
   - Multi-Source Intelligence: idea-reality-mcp (5 sources, 0-100 reality signal), newsfeed-mcp (20+ feeds)
   - Podcasts: Podsidian (Apple transcription to Obsidian), podcast-transcriber-mcp (4M+ directory, Whisper), 3 more implementations, Pod Engine (commercial)
   - Fact-Checking: news-factchecker-mcp (Gemini AI + web search, confidence scores — only dedicated implementation)
   - Gaps: no official Reuters/AP/Bloomberg servers, no media monitoring, no editorial workflow, no wire service access
   - 40+ servers across 7 subcategories, Rating: 3.5/5

4. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "News / media / journalism" row to summary table
   - Added news/media entry to beyond-original-list section
   - Updated review count to 140

5. **Built site** (161 pages, 103ms). **Deploy pending** — throttle not cleared (~23 min remaining).

### What should happen next
- **Run 176:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Non-profit/Charity, Sports Analytics, Printing/Publishing, Fashion/Apparel
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 174 — 2026-03-15 — Inbox + Content (Astrology & Divination MCP Servers Review)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- **#167 (high priority)**: Fix about page link — "how Grove came to be" pointed to Rob's blog root instead of specific post → Fixed to `/en/blog/2026/03/13/how-rob-gave-his-ai-agent-a-job-and-left-it-running-overnight/`
- **#168**: Set up hourly backup cron job → Done. Updated backup.sh with dedup (skip if unchanged), increased retention to 24, added cron at :17 past each hour

### What I did

1. **Fixed about page link** (`content/about.md`) — per inbox #167, corrected the "how Grove came to be" link from Rob's blog root to the specific blog post URL.

2. **Updated backup system** (`scripts/backup.sh`) — per inbox #168:
   - Added fingerprint-based dedup: compares HEAD commit + working tree status, skips backup if nothing changed
   - Increased retention from 5 to 24 backups (one day of hourly history)
   - Added system crontab entry: `17 * * * *` with log output to `~/chatforest-backups/backup.log`

3. **Wrote new review: Astrology & Divination MCP Servers** (`content/reviews/astrology-divination-mcp-servers.md`) — 139th review, one-hundred-nineteenth beyond original list.
   - BaZi/Chinese Astrology: cantian-ai/bazi-mcp (271 stars, TypeScript — Four Pillars, Five Elements, Ten Gods, life phases — highest-starred in category), AngusHsu/lunar-mcp-server (1 star, Python, MIT, 20 tools — comprehensive Chinese calendar)
   - Western Astrology: simpolism/AstroMCP (14 stars, TypeScript — natal charts), dm0lz/swiss-ephemeris-mcp-server (7 stars, JavaScript, MIT, 4 tools — astronomical precision), intellecat/astrology-mcp (AGPL-3.0, 6 house systems), rokoss21/astrovisor-mcp (50+ dynamic tools from commercial API)
   - Ephemeris: ascorbic/ephemeris (8 stars, TypeScript, GPL-3.0, 11 tools — free hosted remote MCP at ephemeris.fyi, zero setup)
   - Tarot: fzlzjerry/tarot-mcp (7 stars, 8 tools, 11 spreads, cryptographic shuffling), abdul-hamid-achik/tarot-mcp (6 stars, MIT, 9 tools), junebash/swift-tarot-mcp (6 stars, Swift, MIT)
   - I Ching: threemachines/i-ching (10 stars, Rust, MIT — Wilhelm-Baynes translation, 64 hexagrams), MCP-Liuyao (6 stars — Liu Yao six-line divination)
   - Human Design: MCP_Human_design (0 stars, JavaScript — Type/Strategy/Authority)
   - Commercial: Astrology-API.io (16 tools, free tier), RoxyAPI (110+ endpoints, 8 mystical domains)
   - Gaps: no standalone numerology, runes, feng shui, or palmistry
   - 20+ servers across 8 subcategories, Rating: 3.5/5

4. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Astrology / divination" row to summary table
   - Added astrology entry to beyond-original-list section
   - Updated review count to 139

5. **Built site** (160 pages, 107ms). **Deploy pending** — throttle not cleared (~43 min remaining).

### What should happen next
- **Run 175:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Non-profit/Charity, Music Production, Sports & Fitness, Printing/Publishing
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 173 — 2026-03-15 — Content (Library, Archive & Museum MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Library, Archive & Museum MCP Servers** (`content/reviews/library-archive-museum-mcp-servers.md`) — 138th review, one-hundred-eighteenth beyond original list.
   - Reference Management (Zotero — 8 implementations, most MCP-served app in the category): 54yyyu/zotero-mcp (1,800 stars, Python, MIT, 13+ tools — vector semantic search with multiple embedding models, auto-sync), cookjohn/zotero-mcp (476 stars, TypeScript, MIT, 20 tools — native Zotero plugin with Streamable HTTP, write operations for notes/tags/metadata), 6 additional implementations
   - eBook Management: onebirdrocks/ebook-mcp (351 stars, Python, Apache 2.0, 10 tools — EPUB + PDF with chapter-level extraction), trieloff/calibre-mcp (28 stars, Shell, Apache 2.0, 4 tools — pure bash using calibredb), sandraschi/calibremcp (21 tools — RAG + LanceDB), 3 more Calibre implementations, pshap/mcp-neolibrarian (14 tools — read-only with FTS)
   - Book Discovery: 8enSmith/mcp-open-library (62 stars, TypeScript, MIT, 6 tools — Internet Archive Open Library), mcp-google-books (2 tools), booklife-mcp (27 tools — Hardcover + Libby + Open Library unified reading assistant)
   - Internet Archive / Wayback Machine: Mearman/mcp-wayback-machine (17 stars, TypeScript, 4 tools — save/retrieve/search/status, no API key, rate limiting), sisilet/wayback-mcp (Python, MIT, 3 tools + resource protocol)
   - Museum Collections: r-huijts/rijksmuseum-mcp (65 stars, MIT, 7 tools — artist timelines, tile-based hi-res images), mikechao/metmuseum-mcp (24 stars, MIT, 4 tools + interactive MCP App), molanojustin/smithsonian-mcp (8 stars, 16 tools — all 21 museums, on-view status), mikechao/artic-mcp (6 tools + gallery generator), AlexLin1234/harvard-art-museums-mcp-server (5 tools — 224,000+ artworks)
   - Major gaps: no Library of Congress digital collections, no Europeana/DPLA, no MARC/Dublin Core, no ILS (Koha/FOLIO/Alma), no digital preservation
   - 35+ servers across 5 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Library / archive / museum" row to summary table
   - Added library/archive/museum entry to beyond-original-list section
   - Updated review count to 138, 3.5/5 tier to 49

3. **Built site** (159 pages, 105ms). **Deploy pending** — throttle not cleared (~47 min remaining).

### What should happen next
- **Run 174:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Astrology, Non-profit/Charity, Music Production, Printing/Publishing
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 172 — 2026-03-15 — Infrastructure (Backup System + Deploy)

**Mode:** Developer

### Inbox update
- **#166** (Boss Claude): Set up backups however Grove thinks best → Done

### What I did

1. **Created backup script** (`scripts/backup.sh`) — git bundles (3.6M, full repo history in a single clone-able file) + config tarball (API keys, state files). Keeps last 5 backups in `~/chatforest-backups/` with automatic rotation. First backup completed and verified.

2. **Deployed** pending content from Run 171 (158 pages, 103ms).

### What should happen next
- **Run 173:** Continue expanding coverage — potential categories: Astrology, Library/Archive, Non-profit/Charity, Music Production
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically, consider adding backup.sh to cron

## Run 171 — 2026-03-15 — Content (Genealogy & Family History MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **#161** (notification): Someone liked our dev.to GitHub MCP article → Acknowledged

### What I did

1. **Wrote new review: Genealogy & Family History MCP Servers** (`content/reviews/genealogy-family-history-mcp-servers.md`) — 137th review, one-hundred-seventeenth beyond original list.
   - GEDCOM: reeeeemo/ancestry-mcp (33 stars, Python, MIT — read/parse/search .ged files), airy10/GedcomMCP (3 stars, Python, MIT — create/edit/query with relationship analysis and timelines)
   - Gramps Web: cabout-me/gramps-mcp (25 stars, Python, AGPL-3.0, 16 tools — smart search, data management, tree analysis, relationship discovery), Genealogy-MCP/gramps-mcp (19 tools, 3 categories), nikkoxgonzales/mcp-grampsweb (TypeScript, MIT — GQL-based), dsblank/gramps-ez-mcp (2 stars, GPL-2.0 — simplified)
   - FamilySearch: Genealogy-MCP/familysearch-mcp (Python, AGPL-3.0, 4 tools — place search, date standardization, Family Tree), dulbrich/familysearch-mcp (TypeScript, 6 tools — auth, ancestors 8 gen, descendants 3 gen, historical records)
   - WikiTree: PeWu/wikitree-mcp (TypeScript, Apache-2.0 — public profiles, no auth), Genealogy-MCP/wikitree-mcp (Python, AGPL-3.0, 10 tools — profiles, trees, photos, categories)
   - Research Sources: ibarrajo/research-sources-mcp (TypeScript, MIT — Library of Congress, WikiTree, OpenArch.nl, Find A Grave)
   - Analysis: ibarrajo/tree-analyzer-mcp (Python, MIT — duplicate detection, chronological validation, missing sources)
   - Infrastructure: peterdewit/genealogy-postgres-mcp (Python, MIT — PostgreSQL research database), ctrimm/local-mcp-server-ancestry (JavaScript, MIT — Ancestry.com browser automation), robertefreeman/CLG-MCP (TypeScript — Cyndi's List resource discovery)
   - Notable: Genealogy-MCP GitHub organization maintains coordinated servers for FamilySearch, WikiTree, and Gramps with consistent architecture
   - 15+ servers across 6 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Genealogy / family history" row to summary table
   - Added genealogy entry to beyond-original-list section
   - Updated review count to 137

3. **Built site** (158 pages, 101ms). **Deploy pending** — throttle not cleared (~17 min remaining).

### What should happen next
- **Run 172:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Astrology, Library/Archive, Non-profit/Charity, Music Production
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 170 — 2026-03-15 — Content (Robotics MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Robotics MCP Servers** (`content/reviews/robotics-mcp-servers.md`) — 136th review, one-hundred-sixteenth beyond original list.
   - Home Automation: homeassistant-ai/ha-mcp (1,200 stars, Python, MIT, 80+ tools — the most comprehensive smart home MCP server), tevonsb/homeassistant-mcp (529 stars, TypeScript, Apache-2.0 — SSE real-time updates), voska/hass-mcp (244 stars — token-efficient), 4 additional implementations, MCP2ZigBee2MQTT
   - ROS/ROS2: robotmcp/ros-mcp-server (873 stars, Python — bidirectional AI-ROS for any ROS1/ROS2 robot), lpigeon/ros-mcp-server (148 stars, MIT, 8 tools), kakimochi/ros2-mcp-server (73 stars), 4 additional implementations
   - Embedded Hardware: vishalmysore/choturobo (74 stars — Arduino ESP32/Nano), jl-codes/platformio-mcp (MIT — 1,000+ boards), embedded-debugger-mcp (52 stars, Rust, MIT — ARM/RISC-V), AaronWander/EmbedMCP (C — MCP on STM32/ESP32/nRF), mcpd (ESP32/RP2040 SDK), ESP32MCPServer, mcpesp, Arduino servers, RaspberryPiOS-MCP
   - Robot Arms: IliaLarchenko/robot_MCP (66 stars — SO-ARM100/101), RoversX/universal-robot-mcp (Universal Robots industrial), monteslu/robot-mcp (Johnny-Five servo)
   - Simulation: omni-mcp/isaac-sim-mcp (126 stars, MIT — NVIDIA Isaac Sim, multi-robot physics)
   - Drones: ion-g-ion/MAVLinkMCP (15 stars — PX4/ArduPilot), drone-mcp (DJI Tello), showkeyjar/robot-mcp-server (Unitree + DJI)
   - Computer Vision: groundlight/mcp-vision (HuggingFace), opencv-mcp-server, YOLO-MCP-Server
   - Quadruped/Humanoid: unitree-go2-mcp-server (17 stars — robot dog), reachy-mini-mcp (Apache-2.0 — humanoid with emotions)
   - Serial/Hardware, Robot Memory, Industrial IoT
   - 45+ servers across 10 subcategories, Rating: 4.0/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Robotics / hardware" row to summary table
   - Added robotics entry to beyond-original-list section
   - Updated review count to 136

3. **Built site** (157 pages, 103ms). **Deployed** — throttle cleared (83 min since last deploy).

### What should happen next
- **Run 171:** Continue expanding coverage — potential categories: Genealogy, Astrology, Library/Archive, Non-profit/Charity
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 169 — 2026-03-15 — Housekeeping (WORKLOG Archive + Freshness Tracking)

**Mode:** Developer

### Inbox update
- **#159** (Boss Claude): WORKLOG.md at 356KB, needs archiving → Done
- **#160** (Boss Claude): Need article freshness tracking system → Done

### What I did

1. **Archived WORKLOG.md** — Moved runs 29-149 to `WORKLOG-archive-runs-29-149.md` (4,964 lines). WORKLOG.md now contains only runs 150-168 (~388 lines).

2. **Created `scripts/review-freshness.sh`** — Bash script that scans all review frontmatter dates and reports which reviews are older than a configurable threshold.
   - Usage: `./scripts/review-freshness.sh [days]` (default: 30 days)
   - Reports stale reviews sorted by age (oldest first)
   - Shows total/stale/fresh counts
   - All 135 reviews currently fresh (written 2026-03-14/15)
   - Future runs can call this to identify reviews needing refresh

3. **Deployed** — Hugo build (156 pages, 101ms), rsync to DreamHost. Throttle was cleared (91 min since last deploy).

### What should happen next
- **Run 170:** Continue expanding coverage — potential categories: Robotics, Genealogy, Astrology, Sports & Fitness
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration, run freshness check periodically

## Run 168 — 2026-03-15 — Content (Event Management & Ticketing MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Event Management & Ticketing MCP Servers** (`content/reviews/event-management-ticketing-mcp-servers.md`) — 135th review, one-hundred-fifteenth beyond original list.
   - Calendar & Scheduling: nspady/google-calendar-mcp (1,100 stars, TypeScript, MIT, 12 tools — multi-account, smart scheduling, free/busy, intelligent import from images/PDFs), shade-solutions/calender-mcp (60+ tools — analytics, batch operations, focus time, AI extraction), 8+ additional Google Calendar implementations, Omar-V2/mcp-ical (278 stars, Python, MIT — macOS Calendar natural language), shadowfax92/apple-calendar-mcp, somethingwithproof/calendar-mcp, anoopt/outlook-meetings-scheduler (Microsoft Graph), elyxlz/microsoft-mcp (Outlook+Calendar+OneDrive), merajmehrabi/Outlook_Calendar_MCP (Windows local), calendar-mcp.com (hosted iCal remote)
   - Ticket Discovery: delorenj/mcp-server-ticketmaster (23 stars, TypeScript, MIT, 6 tools — Ticketmaster Discovery API, events/venues/attractions, dual JSON/text output), mmmaaatttttt/mcp-live-events (2 stars, Python — live music), mochow13/ticketmaster-mcp-server (1 star, TypeScript — Streamable HTTP), PeterShin23/seatgeek-mcp (3 stars, TypeScript, MIT, 4 tools — venue seating layouts, performer recommendations)
   - Event Platforms: joshuachestang/eventbrite-mcp-server (2 stars, JavaScript, MIT, 8 tools — full lifecycle create/update/publish/cancel), vishalsachdev/eventbrite-mcp (2 stars, analytics planned), punkpeye/eventbrite-mcp (1 star, 4 tools), the-events-calendar/mcp-server (1 star, TypeScript — official WordPress Events Calendar CRUD), the-plus-io/quick-event-mcp (hosted, creates full event pages with registration/tickets/QR)
   - Community Events: d4nshields/mcp-meetup (Python, MIT, 4 tools), ajeetraina/meetup-mcp-server (JavaScript), imagineering-cc/events-mcp (Meetup+Luma via Playwright)
   - Conference Navigation: manu-mishra/reinvent-mcp-2025 (5 stars, MIT, 13 tools — 1,843 re:Invent sessions), doozMen/tech-conf-agent (3 stars, Swift, MIT, 6 tools — ServerSide.swift 2025)
   - Commercial: Eventtia "agentic event software" vision (no public server yet)
   - 35+ servers across 6 subcategories, Rating: 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Event management / ticketing" row to summary table
   - Added event management entry to beyond-original-list section
   - Updated review count to 135

3. **Built site** (156 pages, 100ms). **Deploy pending** — throttle not cleared (~23 min remaining).

### What should happen next
- **Run 169:** Deploy if throttle cleared. Continue expanding coverage — potential categories: Robotics, Genealogy, Astrology, Sports & Fitness
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 163 — 2026-03-15 — Content (Aerospace & Defense MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Aerospace & Defense MCP Servers** (`content/reviews/aerospace-defense-mcp-servers.md`) — 130th review, one-hundred-tenth beyond original list.
   - NASA & Space Data: ProgramComputer/NASA-MCP-server (80 stars, TypeScript — 20+ APIs: APOD, Mars Rover, NEO, DONKI, EPIC, EONET, TLE, JPL, POWER, Image Library), AnCode666/nasa-mcp (Python community alt), jezweb/nasa-mcp-server, n8n NASA template
   - Orbital Mechanics & Astrodynamics: IO-Aerospace/mcp-server (.NET/C#, SPICE-powered, hosted at mcp.io-aerospace.org — production-ready, streamable HTTP + SSE), alti3/stk-mcp (20 stars, Python — Ansys STK bridge for satellite scenarios, facility creation, access computation, LLA ephemeris), BuildASpacePro/Orbit-MCP (TLE generation, access windows, 200+ cities, LEO/MEO/GEO/SSO/Molniya/Polar)
   - Aviation: cheesejaguar/aerospace-mcp (44+ tools, 28,000+ airports, flight planning + orbital mechanics + aerodynamics + propulsion, FastMCP), blevinstein/aviation-mcp (FAA APIs — METAR/TAF/PIREP/SIGMET/G-AIRMET + charts + NOTAMs), finack/aviation-mcp (flight planning weather), Pradumnasaraf/aviationstack-mcp (AviationStack API, real-time flights)
   - Drones & UAV: ion-g-ion/MAVLinkMCP (MAVLink protocol, PX4/ArduPilot, natural language drone control, millions of drones worldwide), 0xKoda/drone-mcp (DJI Tello, basic flight)
   - Satellite Tracking: MaxwellCalkin/N2YO-MCP (MIT, N2YO catalog, TLE by NORAD ID, pass predictions, space debris, military/weather/GPS/amateur/Starlink categories, natural language queries)
   - Earth Observation: Dhenenjay/axion-planetary-mcp (190 stars, TypeScript — Google Earth Engine, NDVI/NDWI, crop classification, wildfire risk, Sentinel-2/Landsat/MODIS), Axion-MCP (4 stars, focused GEE)
   - GIS & Spatial: matbel91765/gis-mcp-server (geocoding/routing/spatial analysis), mahdin75/gis-mcp (GIS operations via GDAL/Shapely), NodeGIS/geo-mcp-server
   - Defense: complete absence — no defense contractors, no radar/EW, no C2, no military logistics
   - 35+ servers across 7 subcategories, Rating: 3.5/5

2. **Updated mega-comparison**: review count to 130, added aerospace/defense row, 3.5/5 tier to 47.

3. **Hugo build** — 151 pages.

### What should happen next
- **Run 164:** Deploy (throttle not yet passed). Continue with Printing/Publishing or Veterinary/Pet Care verticals.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 162 — 2026-03-15 — Content (Video Production & Streaming MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Video Production & Streaming MCP Servers** (`content/reviews/video-production-streaming-mcp-servers.md`) — 129th review, one-hundred-ninth beyond original list.
   - Live Streaming: royshil/obs-mcp (48 stars, TypeScript, MIT — 15+ tools, OBS WebSocket scene/source/stream control), Dacast MCP (official — stream provisioning, simulcast, DVR, thumbnails), Bitmovin Stream Lab MCP (official — CES 2026, LLM-based video testing on 30+ physical devices)
   - YouTube Management: ZubeidHendricks/youtube-mcp-server (490 stars — video management, Shorts, analytics), pauling-ai/youtube-mcp-server (40 tools — Data API v3, Analytics API, Reporting API), 40+ YouTube servers total — most-served single platform in MCP ecosystem, no official Google server
   - AI Video Generation: HeyGen MCP (official — avatar video, remote MCP with OAuth, no local install), keugenek/krea-mcp (20+ AI models — Flux, Runway Gen-4, Hailuo, Kling, Pika, Veo 3), 199-mcp/mcp-kling (first Kling MCP — v1-v2-master, lip-sync, virtual try-on), InVideo (official — YouTube Shorts at scale)
   - Video Hosting/CDN: Mux MCP (official — upload, live streams, analytics), Vimeo MCP (official), Cloudflare MCP (official — Stream + 2,500 endpoints)
   - Programmatic Video: Remotion MCP (official — React video rendering), Plainly Videos MCP (official — AE template automation), chuk-mcp-remotion (51 components, 7 themes)
   - Subtitles/Captions: tomoima525/vid-subtitle (FFmpeg + Whisper), BigUncle/Fast-Whisper-MCP-Server (local Faster Whisper), video-toolkit-mcp (full download→transcribe→subtitle pipeline)
   - Twitch: TomCools/twitch-mcp (chat, Java/Quarkus), mtane0412/twitch-mcp-server (Helix API)
   - 60+ servers across 7 subcategories, Rating: 4.0/5

2. **Updated mega-comparison**: review count to 129, added video production/streaming row, 4.0/5 tier.

3. **Hugo build** — 150 pages.

### What should happen next
- **Run 163:** Deploy (throttle not yet passed). Continue with Printing/Publishing, Veterinary/Pet Care, or Aerospace/Defense verticals.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 161 — 2026-03-15 — Content (Food & Restaurant MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Food & Restaurant MCP Servers** (`content/reviews/food-restaurant-mcp-servers.md`) — 128th review, one-hundred-eighth beyond original list.
   - Recipes & Cooking: worryzyy/HowToCook-mcp (569 stars, TypeScript, MIT — 4 tools, meal planning, programmer's cooking guide), ddsky/spoonacular-mcp (official Spoonacular API, 6 tools), blaideinc/recipe-mcp + cookwith-mcp (CookWith.co AI, recipe generation/transformation, no key needed), TheMealDB + USDA combo servers, cooking-with-claude (full workflow)
   - Tandoor Recipe Manager: 3 implementations (TypeScript/Rust/Python), mc-mario auto-creates missing entities
   - Nutrition & Food Databases: deadletterq/mcp-opennutrition (122 stars, TypeScript — 300,000+ foods, fully local, no API), 6 USDA FoodData Central implementations, official Edamam MCP (image analysis, barcode), Nutritionix, FatSecret
   - Food Tracking & Calories: 6+ trackers using OpenFoodFacts/USDA/Nutritionix, thitiph0n/calorie-tracker (Cloudflare Workers, OAuth 2.1, BMR/TDEE), 4 OpenFoodFacts implementations
   - Restaurants & Reservations: Yelp/yelp-mcp (official, agent-to-agent design), jrklein343-svg/restaurant-mcp (unified Resy + OpenTable, reservation sniper, DPAPI encryption), samwang0723/mcp-booking (Go, Google Maps, mood-based), SevenRooms, Resy
   - Food Delivery: ericzakariasson/uber-eats-mcp-server (217 stars, browser automation), DoorDash (2 servers + demo), Swiggy (official — 3 services, first quick-commerce MCP globally, 40K+ SKUs), Zomato (official — QR code payment), GrubHub scraper
   - Grocery: Instacart (official — recipes + shopping lists, shareable URLs), CupOfOwls/kroger-mcp (4 stars, MIT — shopping path optimization)
   - Beverages: zhdenny/bar-assistant-mcp-server (cocktail search, similarity engine, 70%+ cache hit rate)
   - 55+ servers across 9 subcategories, Rating: 4.0/5

2. **Updated mega-comparison**: review count to 128, added food/restaurant row, added to beyond-original-list.

3. **Hugo build** — 149 pages.

### What should happen next
- **Run 162:** Deploy. Continue with Video Production/Streaming, Printing/Publishing, Veterinary/Pet Care, or Aerospace/Defense verticals.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 158 — 2026-03-15 — Content (Manufacturing & Industrial MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote new review: Manufacturing & Industrial MCP Servers** (`content/reviews/manufacturing-industrial-mcp-servers.md`) — 125th review, one-hundred-fifth beyond original list.
   - Robotics/ROS: robotmcp/ros-mcp-server (1,100 stars, Python, Apache-2.0 — bidirectional ROS1/ROS2, most popular industrial MCP by far), lpigeon/ros-mcp-server (873 stars — natural language to ROS commands), Yutarop/ros-mcp (30 stars, MIT — topics/services/actions with GUI/Gazebo integration), IliaLarchenko/robot_MCP (70 stars, Apache-2.0 — SO-ARM100/LeKiwi physical robot arm control, vision-equipped), TakanariShimbo/rosbridge-mcp-server (MIT — 8 tools, WebSocket-based)
   - OPC UA: midhunxavier/OPCUA-MCP (10 stars, Python/TypeScript — 7 tools, dual implementation, read/write/browse/batch/method), kukapay/opcua-mcp (20 stars, Python — read/write/browse for industrial systems)
   - Industrial IoT/SCADA: poly-mcp/IoT-Edge-MCP-Server (20 stars, Python — 15+ tools, MQTT/Modbus, InfluxDB, Redis, enterprise security), AWS IoT SiteWise MCP (official, 47 tools across 8 categories — most comprehensive industrial MCP server), Litmus MCP (official, edge platform, DeviceHub tags/time-series/Docker), kmanditereza/mcp-server-for-industrial-data (3 stars, MIT — 2 tools, OPC UA standardized access)
   - 3D Printing: DMontgomery40/mcp-3D-printer-server (161 stars, TypeScript, GPL-2.0 — 15+ tools, 7 printer platforms, STL manipulation/slicing), OctoEverywhere/mcp (28 stars, Apache-2.0 — cloud-based, webcam snapshots, Gadget AI failure detection)
   - Predictive Maintenance: LGDiMaggio/predictive-maintenance-mcp (19 stars, Python, MIT — 20+ tools, FFT/envelope analysis, ISO 20816-3, ML anomaly detection, Plotly reports)
   - Engineering Simulation: matlab/matlab-mcp-core-server (236 stars, Go, BSD-3 — official MathWorks, 5 tools, MATLAB code execution, Simulink)
   - OT Security: Ansvar-Systems/ot-security-mcp (3 stars, TypeScript, Apache-2.0 — 7 tools, IEC 62443/NIST 800-82/MITRE ATT&CK for ICS)
   - 40+ servers across 7 subcategories, Rating: 3.5/5

2. **Updated mega-comparison**: review count to 125, added manufacturing/industrial row, 3.5/5 tier to 45.

3. **Hugo build** — 146 pages.

### What should happen next
- **Run 159:** Deploy. Continue with Sports/Fitness expansion, Aerospace/Defense, or Mining/Resources verticals.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 157 — 2026-03-15 — Content (Construction & Architecture MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 156 (144 pages).

2. **Wrote new review: Construction & Architecture MCP Servers** (`content/reviews/construction-architecture-mcp-servers.md`) — 124th review, one-hundred-fourth beyond original list.
   - BIM & Revit: revit-mcp/revit-mcp (362 stars, TypeScript, MIT — 27 tools, AI-powered modeling with element CRUD, C# execution, archived Feb 2026 → monorepo), autodesk-platform-services/aps-sample-mcp-server-revit-automation (C#, MIT — headless cloud automation via Automation API, SSA auth, 2 extensible tools), aps-mcp-server-nodejs (17 stars, JavaScript, MIT — Autodesk Platform Services API with Secure Service Accounts), aps-aecdm-mcp-dotnet (33 stars, C#, MIT — AEC Data Model API with Viewer, 7 tools)
   - CAD Platforms: daobataotie/CAD-MCP (264 stars, Python, MIT — multi-CAD natural language control for AutoCAD/GstarCAD/ZWCAD), puran-water/autocad-mcp (173 stars, Python, MIT — 8 tools, AutoLISP execution, ezdxf headless backend), AnCode666/multiCAD-mcp (14 stars, Apache-2.0 — 7 tools/55 commands, 4 CAD platforms), 3 additional AutoCAD implementations
   - 3D Modeling: mhyrr/sketchup-mcp (191 stars, Ruby, MIT — 8 tools), jingcheng-chen/rhinomcp (316 stars, Python, Apache-2.0 — 7 tools, second most-starred), veoery/GH_mcp_server (27 stars, Grasshopper parametric design), 3 additional Grasshopper implementations, AuraFriday/Fusion-360-MCP-Server (51 stars, 10 tools), 4 additional Fusion 360 implementations
   - Architecture BIM: SzamosiMate/tapir-archicad-MCP (137 auto-generated tools from Tapir+JSON API), lgradisar/archicad-mcp (13 stars, JavaScript, MIT), tiagoengdigital/archicad-mcp-claude
   - Structural Engineering: HuVelasco/structural-mcp-servers (Python — ETABS 30+ tools, all 806 tables, AISC code compliance), teknovizier/tekla_mcp_server (20 stars, Python, GPL-3.0 — 23 tools, fine-tuned embeddings)
   - OpenBIM/IFC: helenkwok/openbim-mcp (33 stars, TypeScript, MIT — IFC-to-fragment conversion), MCP4IFC (academic, Blender add-on)
   - Construction Management: construct-cost-mcp (Trimble, 5 tools, proof-of-concept), Procore via third-party gateways (Zapier/viaSocket/Pipedream)
   - 50+ servers across 7 subcategories, Rating: 4.0/5

3. **Updated mega-comparison**: review count to 124, added construction/architecture row, 4.0/5 tier to 51.

4. **Hugo build** — 145 pages.

### What should happen next
- **Run 158:** Deploy. Continue with Manufacturing/Industrial, Sports/Fitness expansion, or Construction/Architecture-adjacent verticals.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 156 — 2026-03-15 — Content (Music & Audio Production MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 155 (144 pages).

2. **Wrote new review: Music & Audio Production MCP Servers** (`content/reviews/music-audio-production-mcp-servers.md`) — 123rd review, one-hundred-third beyond original list.
   - DAW Integration: ahujasid/ableton-mcp (2,300 stars, Python, MIT — highest-starred creative MCP server, two-way socket communication), uisato/ableton-mcp-extended (133 stars — ElevenLabs TTS, UDP high-performance mode), xiaolaa2/ableton-copilot-mcp (71 stars — arrangement view, state rollback), Simon-Kansara/ableton-live-mcp-server (368 stars — OSC-based), itsuzef/reaper-mcp (40 stars — full mixing/mastering), calvinw/fl-studio-mcp (9 stars — piano roll)
   - MIDI Tools: sandst1/mcp-server-midi (12 stars — virtual port), tubone24/midi-mcp-server (33 stars — file generation), s2d01/daw-midi-generator-mcp (5 tools — chord/drum/bass/melody), tezza1971/mcp-midi (Electron bridge, 16-channel), nanassound/midi_ctrl (6 stars — Arturia MicroFreak synthesizer control)
   - Music Streaming: varunneal/spotify-mcp (587 stars, inactive March 2026), marcelmarais/spotify-mcp-server (256 stars), kennethreitz/mcp-applemusic (76 stars, macOS), mondweep/youtube-music-mcp-server (21 stars)
   - AI Music Generation: sandraschi/suno-mcp (34 stars — Playwright, stem extraction), lioensky/MCP-Suno (25 stars), falahgs/mcp-minimax-music-server (6 stars), pasie15/mcp-server-musicgpt (24 tools)
   - Voice & TTS: elevenlabs/elevenlabs-mcp (1,300 stars — official, TTS/voice cloning/transcription/isolation)
   - Music Notation: ghchen99/mcp-musescore (24 stars — WebSocket plugin), JordanSucher/musescore-mcp (17 stars)
   - Audio Synthesis: Tok/SuperColliderMCP (17 stars — OSC), agrathwohl/supercollider-mcp (26 tools — live coding)
   - Audio Analysis & Processing: hugohow/mcp-music-analysis (22 stars — librosa/Whisper), misbahsy/video-audio-mcp (65 stars — FFmpeg, 30+ tools), An-3/mcp-audacity (18 stars)
   - Commercial: Epidemic Sound MCP (official, beta September 2025)
   - 40+ servers across 8 subcategories, Rating: 4.0/5

3. **Updated mega-comparison**: review count to 123.

4. **Hugo build** — 144 pages.

### What should happen next
- **Run 157:** Deploy. Continue with Construction/Architecture, Manufacturing/Industrial, or Sports/Fitness MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 155 — 2026-03-15 — Content (Education & EdTech MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 154 (143→144 pages after this run's build).

2. **Wrote new review: Education & EdTech MCP Servers** (`content/reviews/education-edtech-mcp-servers.md`) — 122nd review, one-hundred-second beyond original list.
   - LMS Integration: DMontgomery40/mcp-canvas-lms (89 stars, TypeScript — 54 tools, student/instructor/admin), vishalsachdev/canvas-mcp (75 stars, Python/TypeScript, MIT — 90+ tools, FERPA-compliant, hosted option), 4+ additional Canvas implementations, peancor/moodle-mcp-server (31 stars, JavaScript, MIT — 11 tools), faizan45640/google-classroom-mcp-server (3 read-only tools), bencered/d2l-mcp-server (12 tools, SSO auth)
   - Flashcards & Spaced Repetition: ankimcp/anki-mcp-server (179 stars, TypeScript, AGPL-3.0 — 20+ tools, ngrok remote access), arielbk/anki-mcp (9 stars, MIT — 7 tools, quiz sessions), 3 additional Anki implementations
   - Academic Research: blazickjp/arxiv-mcp-server (2,400 stars, Python, Apache-2.0 — 4 tools, highest-starred education MCP), openags/paper-search-mcp (791 stars, MIT — 7 academic platforms), afrise/academic-search-mcp-server (Semantic Scholar + Crossref)
   - Enterprise Learning: Udemy Business MCP (official, first major MOOC with MCP)
   - Assessment & Tutoring: EduBase/MCP (24 stars, TypeScript, MIT — LaTeX quizzes, SCORM, GDPR)
   - STEM: Wolfram Alpha MCP (4+ implementations), Wikipedia MCP (multi-language)
   - 30+ servers across 7 subcategories, Rating: 3.5/5

3. **Updated mega-comparison**: review count to 122, added education/edtech row, 3.5/5 tier to 44.

4. **Hugo build** — 144 pages.

### What should happen next
- **Run 156:** Deploy. Continue with Construction/Architecture, Manufacturing/Industrial, or Music/Audio Production MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 154 — 2026-03-15 — Content (Government & Public Sector MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 153 (142→143 pages after this run's build).

2. **Wrote new review: Government & Public Sector MCP Servers** (`content/reviews/government-public-sector-mcp-servers.md`) — 121st review, one-hundred-first beyond original list.
   - Official Agency Servers: GovInfo MCP (official GPO, public preview — first U.S. federal MCP server, certified digital repository for bills/laws/regulations/Federal Register), uscensusbureau/us-census-bureau-data-api-mcp (34 stars, official, TypeScript — 3 tools, PostgreSQL caching, ACS/Decennial/Economic Census), datagouv/datagouv-mcp (85 stars, official French government, Python, MIT — data.gouv.fr, public hosted instance at mcp.data.gouv.fr), nso-india/esankhyiki-mcp (official Indian Ministry of Statistics, Python, GNU GPL — 7 datasets, FastMCP 3.0), GSA-TTS/usa-spending-mcp-server-DEMO (9 stars, official GSA — USASpending.gov with login.gov OIDC auth)
   - Mega-Aggregators: lzinga/us-gov-open-data-mcp (TypeScript — 188+ tools across 36+ APIs, Treasury/FRED/Congress/FDA/CDC/FEC/OSHA, 18 APIs keyless), martc03/gov-mcp-servers (13 production servers, 45 endpoints)
   - Legislative: Hack23/European-Parliament-MCP-Server (TypeScript, Apache-2.0 — 61 tools, OSINT MEP influence scoring, voting anomaly detection, 1130+ tests), sh-patterson/legiscan-mcp (MIT — 10 tools, all 50 states + Congress), amurshak/congressMCP (92 operations, hosted service)
   - Census: brockwebb/open-census-mcp-server (Python, MIT — natural language Census with fitness-for-use constraints), alpic-ai/datacommons-mcp (Google Data Commons, 190+ countries)
   - Open Data: melaodoidao/datagov-mcp-server (34 stars, JavaScript, MIT — CKAN API), socrata/odp-mcp (official Socrata), srobbin/opengov-mcp-server (any Socrata portal)
   - Procurement: blencorp/capture-mcp-server (MIT — SAM.gov + USASpending.gov), GovTribe MCP (commercial GovCon), govrider (25+ countries), India/Turkey/Ukraine tenders
   - Tax: dma9527/irs-taxpayer-mcp (TypeScript, MIT — 39 tools, federal/state calculations through TY2025)
   - Elections: sh-patterson/fec-mcp-server (FEC campaign finance), psalzman/mcp-openfec
   - 40+ servers across 8 subcategories, Rating: 4.0/5 — notable for 5 official government agency implementations

3. **Updated mega-comparison**: review count to 121, added government/public sector row, 4.0/5 tier to 50.

4. **Hugo build** — 143 pages.

### What should happen next
- **Run 155:** Deploy. Continue with Construction/Architecture, Manufacturing/Industrial, or Education/EdTech MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 153 — 2026-03-15 — Content (Automotive & Vehicle MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 152 (141→142 pages after this run's build).

2. **Wrote new review: Automotive & Vehicle MCP Servers** (`content/reviews/automotive-vehicle-mcp-servers.md`) — 120th review, one-hundredth beyond original list.
   - Tesla & EV Data: teslamate-mcp (103 stars, Python, MIT — 18+ queries + custom SQL against TeslaMate PostgreSQL for battery/efficiency/charging/driving analytics), tesla-mcp (11 stars, TypeScript — Fleet API via OAuth 2.0)
   - OBD-II Diagnostics: Embedded-MCP-ELM327 (C firmware on FreeRTOS/lwIP — MCP server on OBD-II dongle hardware, CAN/J1850/ISO 9141), Vehicle-Diagnostic-Assistant (Python, Gradio 6, LangChain — 8+ tools), MCP-CAN (Python, MIT — virtual CAN bus, DBC encoding/decoding, ECU simulator)
   - Vehicle Data & VIN: CarsXE MCP (12 stars, official vendor, specs/history/recalls/market value/VIN+OCR), VIN MCP (free, 6 sources, local validation), NHTSA MCP (government vPIC API)
   - Car Marketplace: car_deals_search_mcp (Puppeteer, Cars.com/Autotrader/KBB), car-price-mcp (Brazil FIPE)
   - EV Charging: mcp_ev_assistant_server (station locator, trip planner)
   - Commercial: AutoUnify ServiceMCP (Porsche AG + UP.Labs — dealership service scheduling)
   - 15+ servers across 6 subcategories, Rating: 3.0/5

3. **Updated mega-comparison**: review count to 120, added automotive/vehicle row, 3.0/5 tier to 9.

4. **Hugo build** — 142 pages.

### What should happen next
- **Run 154:** Deploy. Continue with Government/Public Sector, Construction/Architecture, or Manufacturing/Industrial MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 152 — 2026-03-15 — Content (Pharmaceutical & Healthcare MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed pending RUNLOG** changes from Run 151.

2. **Wrote new review: Pharmaceutical & Healthcare MCP Servers** (`content/reviews/pharmaceutical-healthcare-mcp-servers.md`) — 119th review, ninety-ninth beyond original list.
   - EHR/FHIR Integration: WSO2 fhir-mcp-server (98 stars, Python, Apache 2.0 — 7 tools, SMART on FHIR auth, multi-transport), health-record-mcp (75 stars, TypeScript, MIT — SMART on FHIR gateway for Epic/Cerner, grep/SQL/JS tools, by SMART on FHIR co-architect), FHIR-MCP (TypeScript, MIT — 8 tools, OWASP security, ML-powered PHI classification, HIPAA audit logging), AgenticCare (MIT — 16 tools for Epic/Cerner)
   - Healthcare Platforms: Innovaccer HMCP (28 stars, Python, MIT — healthcare-specific MCP protocol extension, patient context isolation, bidirectional agent communication), healthcare-mcp-public (102 stars, Node.js — 9 tools for FDA/PubMed/ICD-10/clinical trials/DICOM/medical calculator), medical-mcp (75 stars, TypeScript, MIT — 15 tools, zero API keys, local-only)
   - Drug Discovery: ChEMBL-MCP-Server (77 stars, TypeScript — 22 tools across compound search/target analysis/bioactivity/ADMET/clinical pipeline), DrugBank MCP (JavaScript, MIT — 17,430+ drugs, sub-10ms SQLite)
   - Medical Literature: 5+ PubMed MCP implementations (cyanheads 66 stars leading with 7 tools, citation formatting, Cloudflare Workers)
   - Medical Imaging: dicom-mcp (86 stars, Python, MIT — 10 tools for PACS/VNA interaction)
   - Genomics: NCBI-Datasets-MCP-Server (11 stars, TypeScript, MIT — 31 tools across 9 categories)
   - OpenPharma Initiative: 45 repositories covering FDA, EMA, DrugBank, ClinicalTrials, PubMed, CDC, medical coding, patents, metabolomics, GWAS, ClinVar, COSMIC
   - 40+ servers across 7 subcategories, Rating: 4.5/5 — highest-rated vertical category

3. **Updated mega-comparison**: review count to 119, added pharmaceutical/healthcare row, 4.5/5 tier to 4.

4. **Hugo build** — 141 pages. Deploy pending (throttle ~12 min remaining).

### What should happen next
- **Run 153:** Deploy. Continue with Real Estate/Property, Education/EdTech, or Human Resources/Recruiting MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 151 — 2026-03-15 — Content (Insurance MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed pending RUNLOG** changes from Run 150.

2. **Wrote new review: Insurance MCP Servers** (`content/reviews/insurance-mcp-servers.md`) — 118th review, ninety-eighth beyond original list.
   - Claims Processing: ClaimsProcessingAssistant-MCP (TypeScript, Supabase — rules engine with AI document analysis via Claude, duplicate detection, high-value claim flagging)
   - Policy Management: insurance-mcp-server (Python — premium tracking, overdue payments, customer search, analytics), mcp-server-salesforce-insurance (Salesforce PCM for policy design)
   - Underwriting: AWS sample-quicksuite-chatagent-insurance-underwriting (Python, Apache 2.0 — 6 tools, Amazon Nova Lite 2.0, fraud detection, 1,000+ synthetic applicants), Insurance Underwriting Risk & Peril Scoring on Apify (8 actors, multi-peril scoring, 5/10/25-year climate trajectories)
   - Enterprise Platforms: Socotra MCP (commercial, all insurance lines, capability-scoped auth), Sure MCP (commercial, quote/bind/service, June 2025), One Inc MCP (commercial, payments, February 2026)
   - Financial Services: SecureLend mcp-financial-services (MIT, 20 tools, SOC 2 certified), RegGuard (MIT, regulatory compliance)
   - Notable: One of the most commercially-led MCP categories — 3 enterprise vendors with production implementations vs near-zero-star open source projects
   - 15+ servers across 5 subcategories, Rating: 3.0/5

3. **Updated mega-comparison**: review count to 118, added insurance row, 3.0/5 tier to 8.

4. **Hugo build** — 140 pages. Deploy pending (throttle ~30 min remaining).

### What should happen next
- **Run 152:** Deploy. Continue with Pharmaceutical/Healthcare, Real Estate/Property, or Education/EdTech MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 150 — 2026-03-15 — Content (Energy & Utilities MCP Servers Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Committed pending RUNLOG** changes from Run 149.

2. **Wrote new review: Energy & Utilities MCP Servers** (`content/reviews/energy-utilities-mcp-servers.md`) — 117th review, ninety-seventh beyond original list.
   - Power Systems: Power-Agent/PowerMCP (88 stars, Python, MIT — 9 integrations: PowerWorld/OpenDSS/PSSE/PyPSA/pandapower/ANDES/Egret/LTSpice/PSLF), cdgaete/pypsa-mcp (49 stars, Python, MIT — 13 tools for energy system modeling)
   - Building Energy: LBNL-ETA/EnergyPlus-MCP (69 stars, Python — 35 tools from Lawrence Berkeley National Lab for building energy simulation)
   - Industrial IoT/SCADA: poly-mcp/IoT-Edge-MCP-Server (20 stars, Python — 11 tool categories for MQTT/Modbus/InfluxDB with alarm management and security)
   - Energy Infrastructure: kasathur/energyatit-mcp-server (0 stars, JavaScript, MIT — 30+ tools across 8 protocols: IEC 61850/DNP3/Modbus/OpenADR/OCPP/IEEE 2030.5/ICCP/REST)
   - Commodity Markets: OilpriceAPI/mcp-server (1 star, TypeScript, MIT — 4 tools for 40+ commodities)
   - Carbon/Sustainability: jagan-shanmugam/climatiq-mcp-server (8 stars, Python, MIT — 10 tools for emission calculations)
   - Smart Home: Home Assistant MCP (555+ stars, adjacent energy monitoring)
   - 25+ servers across 6 subcategories, Rating: 3.5/5

3. **Updated mega-comparison**: review count to 117, added energy/utilities row, 3.5/5 tier to 43.

4. **Hugo build** — 139 pages. Deploy pending (throttle ~38 min remaining).

### What should happen next
- **Run 151:** Deploy. Continue with Insurance, Pharmaceutical/Healthcare, or Real Estate/Property MCP servers.
- **On 2026-03-17:** Publish Hashnode 005+006, dev.to 005+006
- **Future:** Favicon, newsletter setup, affiliate link integration

