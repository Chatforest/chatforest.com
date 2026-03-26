---
title: "Real Estate & Property MCP Servers — Zillow, Airbnb, MLS, Mortgage Analysis, and More"
description: "Real estate MCP servers: Airbnb MCP (394 stars, 2 tools), Zillow MCP (31 stars, 7 tools), BatchData (27 stars, 8 tools), 30+ tools for CRM, MLS access, mortgage parsing, investment calculators, and regional markets. Rating: 3.5/5."
slug: real-estate-property-mcp-servers
tags: mcp, ai, realestate, fintech
canonical_url: https://chatforest.com/reviews/real-estate-property-mcp-servers/
---

Real estate MCP servers are connecting AI assistants to property data, market analytics, and transaction workflows. Instead of manually searching Zillow, pulling MLS comps, or running mortgage calculators, these servers let AI agents search listings, retrieve valuations, parse mortgage documents, and analyze investment opportunities.

The landscape spans six areas: **property search & listings** (Airbnb, Zillow, MLS access), **property data & valuation** (BatchData, appraisal tools), **real estate CRM & management** (agent tools, deal pipelines), **MLS & industry standards** (RESO-based servers), **mortgage & investment analysis** (document parsing, financial calculators), and **regional market servers** (country-specific property data).

**Category:** [Finance & Fintech](https://chatforest.com/categories/finance-fintech/)

## Key Findings

- **Airbnb dominates by star count** — openbnb-org/mcp-server-airbnb (394 stars) is the most popular real estate MCP server, though it only covers vacation rentals
- **No major platform has an official MCP server** — Zillow, Realtor.com, Redfin, and Trulia are all absent
- **The MLS industry is paying attention** — GumpperGroup's UNLOCK MLS RESO Reference server uses Bridge Interactive's RESO Web API, signaling industry buy-in
- **Mortgage document parsing exists** — confersolutions/mcp-mortgage-server converts Loan Estimates and Closing Disclosures into MISMO-compliant JSON
- **Regional diversity is remarkable** — servers span Korean, Australian, Swedish, French, Spanish, Philippine, and Russian markets

## Top Servers

### Property Search
| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) | 394 | 2 | Airbnb search + listing details, DXT packaged |
| [sap156/zillow-mcp-server](https://github.com/sap156/zillow-mcp-server) | 31 | 7 | Zillow Bridge API — search, Zestimates, market trends, mortgage calc |
| [Repliers-io/mcp-server](https://github.com/Repliers-io/mcp-server) | 14 | 8 | MLS listings, similar listings, address history |

### Property Data & Valuation
| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [zellerhaus/batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate) | 27 | 8 | Address verification, geocoding, property lookup via BatchData.io |

### CRM & Management
| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [agentic-ops/real-estate-mcp](https://github.com/agentic-ops/real-estate-mcp) | 26 | 30+ | Most comprehensive — property, agent, market, client, area intelligence |
| [ashev87/propstack-mcp](https://github.com/ashev87/propstack-mcp) | 1 | 50 | Propstack CRM — contacts, deals, viewings, buyer matching |

### Mortgage & Investment
| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [confersolutions/mcp-mortgage-server](https://github.com/confersolutions/mcp-mortgage-server) | 2 | 4 | MISMO-compliant LE/CD PDF parsing, TRID compliance |
| [sigaihealth/realvestmcp](https://github.com/sigaihealth/realvestmcp) | — | 31 | BRRRR analysis, house hacking, syndication, portfolio modeling |

## What's Missing

- **No official platform servers** — Zillow, Realtor.com, Redfin have no official MCP servers
- **No commercial real estate** — CoStar, LoopNet, CREXi completely absent
- **Limited CRM integration** — Follow Up Boss, kvCORE, Sierra Interactive absent
- **No title & escrow** — no title search, lien check, or closing automation
- **No rental management** — Zillow Rental Manager, Apartments.com absent

## The Bottom Line

**Rating: 3.5 / 5** — Impressive breadth across property search, valuation, mortgage analysis, and international markets. The absence of official platform servers and fragmentation across many low-star repositories limits production readiness. The most promising signal is MLS/RESO industry engagement — positioning MCP as "IDX feeds for AI."

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*
