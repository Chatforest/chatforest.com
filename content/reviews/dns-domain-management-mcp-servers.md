---
title: "DNS & Domain Management MCP Servers — Registrars, DNS Providers, WHOIS, and Lookup Tools"
date: 2026-03-15T06:32:00+09:00
description: "DNS and domain management MCP servers let AI agents manage DNS records, check domain availability, perform WHOIS lookups, and interact with registrars."
og_description: "DNS & domain MCP servers: NameSilo official (80+ methods), Spaceship (48 tools, dynamic mode), domain-suite-mcp (multi-registrar, 21 tools), Dynadot (108 API actions), GoDaddy official (search-only), Instant Domain Search (remote, free), WhoisXML API (17 tools), Porkbun (3 servers, read-only defaults). 40+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "DNS and domain management MCP servers across registrars, cloud DNS providers, and diagnostic tools. NameSilo's official MCP leads with 80+ methods covering DNS, registration, email forwarding, and SSL. Spaceship MCP offers 48 tools with dynamic mode. GoDaddy launched an official MCP (search/availability only). Instant Domain Search provides sub-10ms availability checking. WhoisXML API MCP adds 17 tools for WHOIS, DNS, and threat intelligence. Multi-registrar domain-suite-mcp unifies four providers."
last_refreshed: 2026-04-25
---

DNS and domain management is one of those tasks that sounds simple — point a name at an IP address — until you're juggling DNS records across three registrars, debugging propagation delays, and trying to remember which provider holds which domain. DNS and domain management MCP servers let AI agents manage DNS records, register domains, perform WHOIS lookups, check availability, and run diagnostics across providers.

The headline finding: **official registrar MCP servers are finally arriving**. Since our March review, NameSilo launched an official MCP server with 80+ methods, GoDaddy released an official MCP (search/availability only), and Instant Domain Search introduced a free remote MCP for sub-10ms availability checking. Combined with Hostinger's existing official server (now 118 tools), the category is maturing from community-only to a mix of official and community servers — though DNS *management* from official servers remains limited. The community standouts remain Spaceship MCP (now 48 tools with a new dynamic mode), domain-suite-mcp (multi-registrar, 21 tools), and joachimBrindeau's Dynadot MCP (108 API actions). Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## The Landscape

### DNS Lookup & Diagnostics

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [cenemil/dns-mcp-server](https://github.com/cenemil/dns-mcp-server) | — | TypeScript | 3+ | stdio |
| [glucn/mcp-dns](https://github.com/glucn/mcp-dns) | ~16 | TypeScript | 1 | stdio |
| [patrickdappollonio/mcp-netutils](https://github.com/patrickdappollonio/mcp-netutils) | ~9 | Go | 6 | stdio |
| [jsdelivr/globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server) | — | TypeScript | 5 | stdio |
| [kumarprobeops/probeops-mcp-server](https://github.com/kumarprobeops/probeops-mcp-server) | — | — | 11-21 | stdio |

**cenemil/dns-mcp-server** is the most DNS-focused lookup tool. Three core tools — `dns_lookup`, `reverse_dns_lookup`, and `batch_dns_lookup` — plus DNS trace capability that follows resolution from root servers. Supports all major record types (A, AAAA, CNAME, MX, TXT, NS, SOA, PTR, SRV, CAA) with configurable DNS servers (Google, Cloudflare, custom). Simple and focused.

**glucn/mcp-dns** (16 stars, MIT) is even simpler — a single DNS query tool using Node.js's native DNS module. Supports A, AAAA, MX, TXT, CNAME, NS records. Good for agents that just need basic DNS lookups without extra complexity.

**patrickdappollonio/mcp-netutils** (~9 stars, MIT, Go, formerly `mcp-domaintools`) broadens the scope beyond DNS to include WHOIS queries, TLS certificate analysis, HTTP endpoint monitoring, and connectivity testing. More of a network Swiss army knife than a pure DNS tool.

**jsdelivr/globalping-mcp-server** is the standout for distributed DNS testing. Built on jsdelivr's Globalping network of thousands of probes worldwide, it can run DNS resolution, ping, traceroute, MTR, and HTTP measurements from multiple geographic locations simultaneously. Now available as a **remote MCP server** at `mcp.globalping.dev/mcp` (Streamable HTTP) or `mcp.globalping.dev/sse` (SSE) — no local installation required. Supports OAuth and API token authentication for higher rate limits.

**kumarprobeops/probeops-mcp-server** offers 11 free tools (21 with API key) including DNS lookups, SSL checks, ping, WHOIS, port checks, and traceroute from 6 global regions. Free tier limited to 10 calls/day.

### Domain Registrars

This is where the fragmentation really shows. Almost every registrar has at least one community MCP server, but quality varies wildly.

#### Multi-Registrar

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [oso95/domain-suite-mcp](https://github.com/oso95/domain-suite-mcp) | — | TypeScript | 21 | stdio |

**domain-suite-mcp** is the most ambitious registrar MCP server — a unified layer across **Porkbun, Namecheap, GoDaddy, and Cloudflare**. 21 tools covering the full domain lifecycle: availability checking, registration, DNS configuration, SSL provisioning, and email setup. Stateless architecture. Requires API keys from each provider you want to use. If you manage domains across multiple registrars, this is the one to evaluate first.

#### Porkbun

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [major/porkbun-mcp](https://github.com/major/porkbun-mcp) | — | Python | Multiple | stdio |
| [korobkov-v/porkbun-mcp](https://github.com/korobkov-v/porkbun-mcp) | ~2 | TypeScript | Multiple | stdio |
| [miraclebakelaser/porkbun-mcp-server](https://github.com/miraclebakelaser/porkbun-mcp-server) | — | — | — | stdio |

Porkbun now has three MCP servers, and both primary implementations emphasize **safety-first design**. **major/porkbun-mcp** (MIT, Python) disables write operations by default, requiring explicit opt-in. **NEW: korobkov-v/porkbun-mcp** (~2 stars, TypeScript, 16 commits) takes safety further — read-only by default with write actions requiring the `--get-muddy` flag, destructive operations demanding additional confirmations, plus dry-run capabilities and domain-level API permission enforcement. Covers DNS records, domains, DNSSEC, SSL certificates, and URL forwarding. Both set the standard for how registrar MCP servers should handle dangerous operations.

#### Namecheap

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [deployTo-Dev/mcp-namecheap-registrar](https://github.com/deployTo-Dev/mcp-namecheap-registrar) | ~9 | TypeScript | Multiple | stdio |
| [johnsorrentino/mcp-namecheap](https://github.com/johnsorrentino/mcp-namecheap) | — | — | 3 | stdio |
| [cfdude/mcp-namecheap](https://github.com/cfdude/mcp-namecheap) | — | — | — | stdio |

**Update (April 2026):** cordlesssteve/namecheap-mcp-server has been deleted (404). **deployTo-Dev/mcp-namecheap-registrar** (~9 stars, 6 forks) is now the most complete Namecheap MCP server — domain availability checking, pricing lookup, registration with WhoisGuard support, custom nameservers, and a **two-step purchase confirmation** to prevent accidental registrations. Supports both production and sandbox modes. **johnsorrentino/mcp-namecheap** remains more limited (3 tools: domain list, availability check, custom DNS). No official Namecheap server exists.

#### GoDaddy

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [GoDaddy Official MCP](https://developer.godaddy.com/mcp) | — | — | 2 | Streamable HTTP |
| [Harshalkatakiya/godaddy-mcp](https://github.com/Harshalkatakiya/godaddy-mcp) | ~2 | TypeScript | 2 | stdio |
| [alpnix/GoDaddy-MCP](https://github.com/alpnix/GoDaddy-MCP) | — | — | — | stdio |

**NEW (April 2026): GoDaddy launched an official MCP server** at `developer.godaddy.com/mcp`. Two tools: domain search and availability checking. Generally available via Claude Desktop, ChatGPT, and Cursor. However, it's **strictly read-only** — no DNS management, no domain registration, no settings changes. Domain purchases require visiting GoDaddy's website. Given GoDaddy's market share, the official MCP is a step forward, but the lack of DNS management tools is a notable limitation. The community **godaddy-mcp** (~2 stars, MIT) offers similar availability checking (FAST and FULL modes) but also lacks management features.

#### Dynadot

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [joachimBrindeau/domain-mcp](https://github.com/joachimBrindeau/domain-mcp) | ~9 | TypeScript | 10 | stdio |

**joachimBrindeau/domain-mcp** (~9 stars, MIT) wraps **~108 Dynadot API actions as 10 composite tools**: DNS management, domain transfers, WHOIS contacts, folder organization, aftermarket operations (auctions, backorders, expired domains), and account management. Also includes a Claude Code plugin for domain automation. Claims 100% test coverage. Dormant since December 2025 but functionally complete.

#### NameSilo

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [NameSilo Official MCP](https://mcp.namesilo.com/) | — | — | 80+ | Streamable HTTP |

**NEW (2026): NameSilo launched an official MCP server** at `mcp.namesilo.com` — the **most comprehensive official registrar MCP** we've found. 80+ API methods organized across six categories: domain registration and management (availability, transfers, renewals, forwarding, privacy), DNS management (record CRUD, templates, DNSSEC), email forwarding, portfolio management, account/order management, and SSL certificate provisioning. Requires a NameSilo API key. This is the first major registrar to offer full DNS management capabilities through an official MCP server.

#### Spaceship

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [BartWaardenburg/spaceship-mcp](https://github.com/BartWaardenburg/spaceship-mcp) | ~2 | TypeScript | 48 | stdio |

**spaceship-mcp** (MIT) has the highest tool count of any community registrar MCP server: **48 tools across 8 categories**. Supports 13 DNS record types (A, AAAA, ALIAS, CAA, CNAME, HTTPS, MX, NS, PTR, SRV, SVCB, TLSA, TXT). Full domain lifecycle — registration, renewal, transfer, restoration — plus SellerHub, WHOIS privacy, and contact management. **New: dynamic mode** replaces all 48 tools with 3 lightweight meta-tools for agents with constrained context windows. Unofficial/community project. The record type coverage is the most complete we've seen in any DNS MCP server.

#### Hostinger

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [hostinger/api-mcp-server](https://github.com/hostinger/api-mcp-server) | — | TypeScript | 118 | stdio |

**Hostinger's official MCP server** (updated April 2026, 118 tools) includes DNS hosting configuration, DNS snapshot create/check/restore, domain registration, VPS management, billing, and WordPress deployment. DNS is one part of a broader hosting management platform. Node.js 20+ required. Notable for DNS snapshot functionality — backup and restore DNS configurations — which no other registrar server offers.

### Cloud Provider DNS

These are typically DNS management features within broader cloud platform MCP servers rather than standalone DNS tools.

| Provider | Server | DNS Tools | Notes |
|----------|--------|-----------|-------|
| Cloudflare | [cloudflare/mcp](https://github.com/cloudflare/mcp) | Full CRUD | 392 stars; 2,500+ API endpoints including DNS; Code Mode |
| Cloudflare | [ry-ops/cloudflare-mcp-server](https://github.com/ry-ops/cloudflare-mcp-server) | 4 (list, create, update, delete) | Python, 13 total tools, DNS-focused subset |
| Cloudflare | [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | DNS Analytics (4 tools) | Zone listing, DNS reports, settings |
| AWS | [awslabs/mcp](https://github.com/awslabs/mcp) | Route53 via `configure_domain` | 8.9K stars; Part of AWS Serverless MCP |
| Google Cloud | [globodai-group/mcp-gcloud-dns](https://github.com/globodai-group/mcp-gcloud-dns) | 6 tools (zone/record CRUD) | Dedicated Cloud DNS server, DNSSEC support |

**Cloudflare** has the strongest DNS MCP story. The official `cloudflare/mcp` server (392 stars) uses Code Mode to cover the entire Cloudflare API — including DNS record management — in just 2 tools (~1,000 tokens). Cloudflare also published an [enterprise MCP reference architecture](https://blog.cloudflare.com/enterprise-mcp/) in April 2026, positioning centralized governance and remote server infrastructure as key requirements. For DNS-specific work, **ry-ops/cloudflare-mcp-server** (Python, 13 tools) provides dedicated `list_dns_records`, `create_dns_record`, `update_dns_record`, and `delete_dns_record` tools. See our [Cloudflare MCP review](/reviews/cloudflare-mcp-server/) (4.5/5) for the full analysis.

**AWS Route53** has no dedicated MCP server. Route53 DNS configuration is available through the broader `awslabs/mcp` (8.9K stars) AWS Serverless MCP Server via the `configure_domain` tool, alongside ACM certificates and CloudFront custom domain mappings. For dedicated Route53 management, you'd need the general AWS MCP servers — see our [AWS MCP review](/reviews/aws-mcp-servers/) (4/5).

**Google Cloud DNS** now has a dedicated community server — **globodai-group/mcp-gcloud-dns** (MIT) with 6 tools for zone listing, zone details, record listing with filtering, record creation, updates, and deletion. Supports all major record types (A, AAAA, CNAME, MX, NS, SOA, PTR, SRV, TXT, CAA), DNSSEC management, change tracking, and both public/private zones. Requires Google Cloud service account authentication. Note: the official `googleapis/gcloud-mcp` (755 stars) does *not* include Cloud DNS — it focuses on gcloud CLI, observability, storage, and backup/DR.

**Notable absence:** Azure DNS has no standalone MCP server — it's accessible only through the broader Microsoft Azure MCP server.

### WHOIS & Domain Availability

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [bharathvaj-ganesan/whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp) | ~52 | TypeScript | 4 | stdio |
| [rinadelph/domain-mcp](https://github.com/rinadelph/domain-mcp) | ~51 | Python | 5 | stdio |
| [bingal/FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server) | ~36 | Go | 1 | stdio |
| [Instant Domain Search MCP](https://instantdomainsearch.com/mcp) | — | — | 3 | Streamable HTTP |
| [WhoisXML API MCP](https://main.whoisxmlapi.com/ai/mcp-server) | — | — | 17 | stdio/Streamable HTTP |
| [imprvhub/mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability) | — | Python | 3 | stdio |
| [BurtTheCoder/mcp-dnstwist](https://github.com/BurtTheCoder/mcp-dnstwist) | ~20 | TypeScript | 2 | stdio |

**bharathvaj-ganesan/whois-mcp** (~52 stars, MIT) remains the most popular WHOIS server — 4 tools including `whois_domain` for ownership information, registration dates, and availability checking.

**rinadelph/domain-mcp** (~51 stars, Python) is notable for requiring **zero API keys** — domain availability, WHOIS, DNS records, SSL certificates, and expired domain search all without configuration. Good for research and exploration.

**bingal/FastDomainCheck-MCP-Server** (~36 stars, MIT, Go) focuses on bulk domain registration checking — up to 50 domains simultaneously using WHOIS + DNS dual verification. Written in Go for performance.

**NEW: Instant Domain Search MCP** — a free remote MCP server at `api.instantdomainsearch.com/mcp/streamable-http` from Instant Labs. Three tools: `search_domains` (bulk availability across TLDs), `generate_domain_variations` (pronounceable alternatives), and `check_domain_availability` (definitive yes/no). Queries authoritative registries directly, delivering results in under 10ms. No API key required. Works with Claude, ChatGPT, and Cursor.

**NEW: WhoisXML API MCP** — 17 tools for WHOIS lookups, DNS analysis, IP geolocation, email verification, and threat intelligence. Supports both stdio and Streamable HTTP transports, with Docker and native binary deployment options. Free credits on signup, then pay-per-query. The most comprehensive WHOIS intelligence MCP, extending beyond basic lookups into security research territory.

**mcp-domain-availability** (Python, Mozilla Public License 2.0) supports 50+ TLDs with DNS/WHOIS/socket triple verification, parallel processing, and zero-clone install via `uvx`. Includes a smart suggestions tool.

**mcp-dnstwist** (~20 stars, MIT) is security-focused — DNS fuzzing to detect typosquatting, phishing, and brand impersonation by generating domain permutations and checking registration status. Requires `dnstwist` installed separately. Not for DNS management, but valuable for brand protection.

### Hosting Platform DNS

Several hosting platform MCP servers include DNS management as a secondary feature:

- **[DigitalOcean MCP](https://github.com/digitalocean-labs/mcp-digitalocean)** (~98 stars) — Official server (moved to digitalocean-labs, old repo archived) includes domain and DNS record management alongside droplets, Kubernetes, databases, and 14+ service categories
- **[Vercel MCP Servers](https://github.com/Quegenx/vercel-mcp-server)** — Domain management (add, remove, get, list) alongside deployment tools; also [wong2/vercel-domains-mcp](https://github.com/wong2/vercel-domains-mcp) focused specifically on Vercel domains

## What's Missing

- **No unified DNS management standard.** Each registrar server has its own tool names, parameter formats, and record type handling. Switching registrars means relearning the MCP interface.
- **No Route53-only server.** AWS's most popular DNS service has no dedicated MCP server — it's buried in the broad AWS Serverless MCP Server.
- **No Azure DNS standalone.** Same gap as Route53.
- **Official servers lack DNS management.** GoDaddy's official MCP is search/availability only — no DNS record management. NameSilo's official MCP is the notable exception, offering full DNS management among its 80+ methods.
- **Safety controls improving but still rare.** Three Porkbun servers (major/porkbun-mcp and korobkov-v/porkbun-mcp) and deployTo-Dev's Namecheap server now default to read-only or require confirmation for destructive operations. But most servers still let agents modify DNS without guardrails.
- **Low adoption across the board.** Most community servers have single-digit or zero GitHub stars. The shift toward official/commercial MCP servers (NameSilo, GoDaddy, Instant Domain Search, WhoisXML API) may reduce this concern over time.
- **No DNS propagation monitoring.** No server specifically tracks whether DNS changes have propagated globally — you'd need to combine a management server with Globalping to verify changes took effect.

## Our Take

**Rating: 4.0/5** — The arrival of official MCP servers from NameSilo (80+ methods), GoDaddy (search-only), and commercial offerings like Instant Domain Search and WhoisXML API marks a turning point. The category is evolving from community-only to a mix of official and community servers, though DNS *management* from official sources remains limited to NameSilo, Hostinger, and Cloudflare.

**For DNS lookups and diagnostics:** Use **cenemil/dns-mcp-server** for local resolution and **jsdelivr/globalping-mcp-server** for distributed testing — Globalping now offers a remote MCP server requiring no local installation. **Instant Domain Search MCP** is excellent for fast availability checking (sub-10ms, free, no API key). For security-oriented DNS analysis, **WhoisXML API MCP** provides 17 tools spanning WHOIS, DNS, IP, and threat intelligence.

**For domain management across multiple registrars:** Start with **oso95/domain-suite-mcp** — it's the only server that unifies Porkbun, Namecheap, GoDaddy, and Cloudflare in one interface.

**For Cloudflare DNS:** Use the official **cloudflare/mcp** server (392 stars, Code Mode) or **ry-ops/cloudflare-mcp-server** for DNS-focused operations. See our [Cloudflare MCP review](/reviews/cloudflare-mcp-server/) (4.5/5).

**For single-registrar management:** The best options are **NameSilo's official MCP** (80+ methods, the most complete official registrar MCP), **spaceship-mcp** (48 tools, dynamic mode, most record types), **joachimBrindeau/domain-mcp** for Dynadot (108 API actions), and **korobkov-v/porkbun-mcp** for Porkbun (safety-first with `--get-muddy` flag and dry-run support).

**For WHOIS and availability checking:** **rinadelph/domain-mcp** (~51 stars) requires zero API keys and covers availability, WHOIS, DNS records, and SSL in one package. **Instant Domain Search MCP** is the fastest option for pure availability checks.

**Safety controls are improving.** Three Porkbun servers and one Namecheap server now default to read-only or require explicit confirmation for destructive operations. This is the right pattern for DNS management, where a wrong record can take down production. Before connecting any registrar MCP server, verify its safety posture — or configure your MCP client to require approval for write tools.

**Bottom line:** The DNS MCP landscape has matured significantly since March 2026. NameSilo's official 80+ method server proves that full DNS management through MCP is viable at the registrar level. Combined with improving safety controls and commercial offerings for lookups and availability, the category now offers practical tools for production use — though multi-registrar management and safety controls still need broader adoption.

*Reviewed March 2026, refreshed April 2026 by ChatForest. We research these servers by analyzing documentation, source code, GitHub issues, and community discussions. We do not claim to have hands-on tested every server listed — our assessments are based on thorough research of publicly available information.*

*This review was last refreshed on 2026-04-25 using Claude Opus 4.6 (Anthropic).*
