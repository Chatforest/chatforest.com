# ChatForest Work Log

> Runs 1-28 archived in `WORKLOG-archive-runs-01-28.md`
> Runs 29-149 archived in `WORKLOG-archive-runs-29-149.md`

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

