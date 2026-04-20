# DNS & Domain Management MCP Servers — Registrars, DNS Providers, WHOIS, and Lookup Tools

> DNS and domain management MCP servers let AI agents manage DNS records, check domain availability, perform WHOIS lookups, and interact with registrars.


DNS and domain management is one of those tasks that sounds simple — point a name at an IP address — until you're juggling DNS records across three registrars, debugging propagation delays, and trying to remember which provider holds which domain. DNS and domain management MCP servers let AI agents manage DNS records, register domains, perform WHOIS lookups, check availability, and run diagnostics across providers.

The headline finding: **this is the most fragmented MCP category we've reviewed**. There's no single dominant server. Instead, you get 30+ servers scattered across registrars, cloud providers, and utility tools — most with single-digit GitHub stars. The standouts are Spaceship MCP (47 tools, 13 record types), joachimBrindeau's Dynadot MCP (106 API actions with claimed 100% test coverage), and the multi-registrar domain-suite-mcp that unifies four providers in one server. For DNS diagnostics, cenemil/dns-mcp-server and jsdelivr's Globalping MCP offer complementary local and global perspectives. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## The Landscape

### DNS Lookup & Diagnostics

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [cenemil/dns-mcp-server](https://github.com/cenemil/dns-mcp-server) | — | TypeScript | 3+ | stdio |
| [glucn/mcp-dns](https://github.com/glucn/mcp-dns) | ~16 | TypeScript | 1 | stdio |
| [patrickdappollonio/mcp-domaintools](https://github.com/patrickdappollonio/mcp-domaintools) | ~10 | Go | 6 | stdio |
| [jsdelivr/globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server) | — | TypeScript | 5 | stdio |
| [kumarprobeops/probeops-mcp-server](https://github.com/kumarprobeops/probeops-mcp-server) | — | — | 11-21 | stdio |

**cenemil/dns-mcp-server** is the most DNS-focused lookup tool. Three core tools — `dns_lookup`, `reverse_dns_lookup`, and `batch_dns_lookup` — plus DNS trace capability that follows resolution from root servers. Supports all major record types (A, AAAA, CNAME, MX, TXT, NS, SOA, PTR, SRV, CAA) with configurable DNS servers (Google, Cloudflare, custom). Simple and focused.

**glucn/mcp-dns** (16 stars, MIT) is even simpler — a single DNS query tool using Node.js's native DNS module. Supports A, AAAA, MX, TXT, CNAME, NS records. Good for agents that just need basic DNS lookups without extra complexity.

**patrickdappollonio/mcp-domaintools** (~10 stars, MIT, Go) broadens the scope beyond DNS to include WHOIS queries, TLS certificate analysis, HTTP endpoint monitoring, and connectivity testing. May have been renamed to `mcp-netutils`. More of a network Swiss army knife than a pure DNS tool.

**jsdelivr/globalping-mcp-server** is the standout for distributed DNS testing. Built on jsdelivr's Globalping network of thousands of probes worldwide, it can run DNS resolution, ping, traceroute, MTR, and HTTP measurements from multiple geographic locations simultaneously. When you need to debug DNS propagation or verify records from different regions, this is the tool. Requires a Globalping account for higher rate limits.

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
| [miraclebakelaser/porkbun-mcp-server](https://github.com/miraclebakelaser/porkbun-mcp-server) | — | — | — | stdio |

**major/porkbun-mcp** (MIT) stands out for its **safety-first design** — write operations are disabled by default, requiring explicit opt-in. Covers DNS records, domains, DNSSEC, and SSL certificates via Porkbun's API. This is the right approach for a registrar MCP server where accidental changes can take down production websites.

#### Namecheap

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [cordlesssteve/namecheap-mcp-server](https://github.com/cordlesssteve/namecheap-mcp-server) | — | TypeScript | 5+ | stdio |
| [johnsorrentino/mcp-namecheap](https://github.com/johnsorrentino/mcp-namecheap) | — | — | 3 | stdio |
| [cfdude/mcp-namecheap](https://github.com/cfdude/mcp-namecheap) | — | — | — | stdio |

Three competing Namecheap servers, none with significant adoption. **cordlesssteve/namecheap-mcp-server** (TypeScript, Node.js 18+) is the most complete — domain availability checking, domain list management, DNS host record CRUD (A, AAAA, CNAME, MX, TXT, etc.), nameserver configuration, and premium domain detection. **johnsorrentino/mcp-namecheap** is more limited (3 tools: domain list, availability check, custom DNS). No official Namecheap server exists.

#### GoDaddy

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Harshalkatakiya/godaddy-mcp](https://github.com/Harshalkatakiya/godaddy-mcp) | ~0 | TypeScript | 2 | stdio |
| [alpnix/GoDaddy-MCP](https://github.com/alpnix/GoDaddy-MCP) | — | — | — | stdio |

GoDaddy's MCP presence is minimal. **godaddy-mcp** (MIT) offers only domain availability checking (FAST and FULL modes) — no DNS management, no domain registration. GoDaddy does have an official MCP endpoint via their developer portal, but the community implementations are bare-bones. Given GoDaddy's market share, this is a notable gap.

#### Dynadot

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [joachimBrindeau/domain-mcp](https://github.com/joachimBrindeau/domain-mcp) | — | TypeScript | 10 | stdio |

**joachimBrindeau/domain-mcp** (MIT) is the most comprehensive single-registrar MCP server we found. 10 composite tools that cover **106 Dynadot API actions**: DNS management, domain transfers, WHOIS contacts, folder organization, aftermarket operations (auctions, backorders, expired domains), and account management. Claims 100% test coverage. If you use Dynadot, this is unusually thorough.

#### Spaceship

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [BartWaardenburg/spaceship-mcp](https://github.com/BartWaardenburg/spaceship-mcp) | — | TypeScript | 47 | stdio |

**spaceship-mcp** (MIT) has the highest tool count of any registrar MCP server: **47 tools across 8 categories**. Supports 13 DNS record types (A, AAAA, ALIAS, CAA, CNAME, HTTPS, MX, NS, PTR, SRV, SVCB, TLSA, TXT). Full domain lifecycle — registration, renewal, transfer, restoration — plus SellerHub, WHOIS privacy, and contact management. Unofficial/community project. The record type coverage is the most complete we've seen in any DNS MCP server.

#### Hostinger

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [hostinger/api-mcp-server](https://github.com/hostinger/api-mcp-server) | — | TypeScript | 100+ | stdio |

**Hostinger's official MCP server** includes DNS hosting configuration, DNS snapshot create/check/restore, domain registration, VPS management, billing, and WordPress deployment. DNS is one part of a broader hosting management platform. Node.js 20+ required. Notable for DNS snapshot functionality — backup and restore DNS configurations — which no other registrar server offers.

### Cloud Provider DNS

These are typically DNS management features within broader cloud platform MCP servers rather than standalone DNS tools.

| Provider | Server | DNS Tools | Notes |
|----------|--------|-----------|-------|
| Cloudflare | [cloudflare/mcp](https://github.com/cloudflare/mcp) | Full CRUD | 2,500+ API endpoints including DNS; Code Mode |
| Cloudflare | [ry-ops/cloudflare-mcp-server](https://github.com/ry-ops/cloudflare-mcp-server) | 4 (list, create, update, delete) | Python, DNS-focused subset |
| Cloudflare | [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | DNS Analytics (4 tools) | Zone listing, DNS reports, settings |
| AWS | [awslabs/mcp](https://github.com/awslabs/mcp) | Route53 via `configure_domain` | Part of AWS Serverless MCP |
| Google Cloud | [googleapis/gcloud-mcp](https://github.com/googleapis/gcloud-mcp) | Cloud DNS zone/record CRUD | Part of broader Google Cloud MCP |

**Cloudflare** has the strongest DNS MCP story. The official `cloudflare/mcp` server's Code Mode covers the entire Cloudflare API — including DNS record management — in just 2 tools (~1,000 tokens). For DNS-specific work, **ry-ops/cloudflare-mcp-server** (Python, 13 tools) provides dedicated `list_dns_records`, `create_dns_record`, `update_dns_record`, and `delete_dns_record` tools. See our [Cloudflare MCP review](/reviews/cloudflare-mcp-server/) (4.5/5) for the full analysis.

**AWS Route53** has no dedicated MCP server. Route53 DNS configuration is available through the broader `awslabs/mcp` AWS Serverless MCP Server via the `configure_domain` tool, alongside ACM certificates and CloudFront custom domain mappings. For dedicated Route53 management, you'd need the general AWS MCP servers — see our [AWS MCP review](/reviews/aws-mcp-servers/) (4/5).

**Google Cloud DNS** is accessible via `googleapis/gcloud-mcp` with zone and record CRUD operations supporting all major record types (A, AAAA, CNAME, MX, NS, SOA, PTR, SRV, TXT, CAA), DNSSEC status, and public/private zones. Requires Google Cloud service account authentication.

**Notable absence:** Azure DNS has no standalone MCP server — it's accessible only through the broader Microsoft Azure MCP server.

### WHOIS & Domain Availability

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [bharathvaj-ganesan/whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp) | ~47 | TypeScript | 4 | stdio |
| [rinadelph/domain-mcp](https://github.com/rinadelph/domain-mcp) | ~46 | Python | 5 | stdio |
| [bingal/FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server) | ~30 | Go | 1 | stdio |
| [imprvhub/mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability) | — | Python | 3 | stdio |
| [BurtTheCoder/mcp-dnstwist](https://github.com/BurtTheCoder/mcp-dnstwist) | ~20 | TypeScript | 2 | stdio |

**bharathvaj-ganesan/whois-mcp** (~47 stars, MIT) is the most popular WHOIS server — 4 tools including `whois_domain` for ownership information, registration dates, and availability checking.

**rinadelph/domain-mcp** (~46 stars, Python) is notable for requiring **zero API keys** — domain availability, WHOIS, DNS records, SSL certificates, and expired domain search all without configuration. Good for research and exploration.

**bingal/FastDomainCheck-MCP-Server** (~30 stars, MIT, Go) focuses on bulk domain registration checking — up to 50 domains simultaneously using WHOIS + DNS dual verification. Written in Go for performance.

**mcp-domain-availability** (Python, Mozilla Public License 2.0) supports 50+ TLDs with DNS/WHOIS/socket triple verification, parallel processing, and zero-clone install via `uvx`. Includes a smart suggestions tool.

**mcp-dnstwist** (~20 stars, MIT) is security-focused — DNS fuzzing to detect typosquatting, phishing, and brand impersonation by generating domain permutations and checking registration status. Requires `dnstwist` installed separately. Not for DNS management, but valuable for brand protection.

### Hosting Platform DNS

Several hosting platform MCP servers include DNS management as a secondary feature:

- **[DigitalOcean MCP](https://github.com/digitalocean/digitalocean-mcp)** — Official server includes domain and DNS record management alongside droplet and App Platform management
- **[Vercel MCP Servers](https://github.com/Quegenx/vercel-mcp-server)** — Domain management (add, remove, get, list) alongside deployment tools; also [wong2/vercel-domains-mcp](https://github.com/wong2/vercel-domains-mcp) focused specifically on Vercel domains

## What's Missing

- **No unified DNS management standard.** Each registrar server has its own tool names, parameter formats, and record type handling. Switching registrars means relearning the MCP interface.
- **No Route53-only server.** AWS's most popular DNS service has no dedicated MCP server — it's buried in the broad AWS Serverless MCP Server.
- **No Azure DNS standalone.** Same gap as Route53.
- **Minimal safety controls.** Apart from major/porkbun-mcp's read-only default, most registrar servers let agents create, modify, and delete DNS records without confirmation. For a service where a wrong record can take down production, this is concerning.
- **Low adoption across the board.** Most servers have single-digit or zero GitHub stars. Community validation is minimal.
- **No DNS propagation monitoring.** No server specifically tracks whether DNS changes have propagated globally — you'd need to combine a management server with Globalping to verify changes took effect.

## Our Take

**Rating: 3.5/5** — Extensive coverage across registrars and providers, but fragmented, low-adoption, and missing safety controls that DNS management demands.

**For DNS lookups and diagnostics:** Use **cenemil/dns-mcp-server** for local resolution and **jsdelivr/globalping-mcp-server** for distributed testing. Together they cover both "what does DNS resolve to?" and "has my change propagated globally?"

**For domain management across multiple registrars:** Start with **oso95/domain-suite-mcp** — it's the only server that unifies Porkbun, Namecheap, GoDaddy, and Cloudflare in one interface.

**For Cloudflare DNS:** Use the official **cloudflare/mcp** server (Code Mode) or **ry-ops/cloudflare-mcp-server** for DNS-focused operations. See our [Cloudflare MCP review](/reviews/cloudflare-mcp-server/) (4.5/5).

**For single-registrar management:** The best options are **spaceship-mcp** (47 tools, most record types), **joachimBrindeau/domain-mcp** for Dynadot (106 API actions), and **major/porkbun-mcp** for Porkbun (safety-first with read-only defaults).

**For WHOIS and availability checking:** **rinadelph/domain-mcp** requires zero API keys and covers availability, WHOIS, DNS records, and SSL in one package.

**The safety gap is real.** DNS changes can break production immediately. Only one server (porkbun-mcp) defaults to read-only mode. Before connecting any registrar MCP server, verify it doesn't allow destructive operations without explicit confirmation — or configure your MCP client to require approval for write tools.

**Bottom line:** You can manage DNS via MCP today, but you'll be stitching together low-adoption community servers with limited safety guarantees. The category needs an official server from a major registrar or a well-maintained multi-provider tool with proper safety controls to reach its potential. For now, use these servers for research and non-critical domains, and think carefully before letting an agent manage production DNS.

*Reviewed March 2026 by ChatForest. We research these servers by analyzing documentation, source code, GitHub issues, and community discussions. We do not claim to have hands-on tested every server listed — our assessments are based on thorough research of publicly available information.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

