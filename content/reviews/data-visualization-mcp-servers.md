---
title: "Data Visualization MCP Servers — AntV, ECharts, Vega-Lite, Plotly, Matplotlib, D3, and More"
date: 2026-03-15T08:00:00+09:00
description: "Data visualization MCP servers let AI agents generate charts, dashboards, and interactive graphics from natural language."
og_description: "Data visualization MCP servers: AntV mcp-server-chart (4,069 stars, 27 tools, 26+ chart types), Grafana mcp-grafana (3,012 stars, official, v0.14.0), hustcc/mcp-echarts (229 stars, dormant Jan 2026), Tableau tableau-mcp (270 stars, official, v2.2.4), QuickChart MCP (160 stars, URL-based Chart.js, archived), Vega-Lite MCP (96 stars, abandoned May 2025), Apache ECharts MCP (69 stars, official, cloud-hosted image URLs), Vizro MCP (3,690 stars parent repo, McKinsey, vizro-mcp stale Feb 2026), Metabase MCP (imlewc leads at 145 stars), xoniks DuckDB+Plotly (19 stars, natural language to interactive charts). 20+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Data visualization MCP servers across charting libraries, grammar-of-graphics tools, code-based renderers, BI platforms, and data-aware visualizers. AntV's mcp-server-chart leads pure charting at 4,069 stars and 27 tools. Grafana's official mcp-grafana (3,012 stars) is now one of the highest-starred MCP servers in the ecosystem, covering dashboards, alerting, and observability visualization. Tableau's official MCP server (270 stars, v2.2.4) fills the enterprise BI gap. The category is broad but several community servers have gone dormant — Vega-Lite abandoned, hustcc/mcp-echarts quiet since January 2026."
last_refreshed: 2026-05-18
---

Data visualization is a natural fit for MCP — AI agents that can turn a dataset into a chart from a natural language prompt eliminate one of the most common friction points in data work. The category spans five areas: **charting libraries** ([AntV](https://antv.antgroup.com/), [ECharts](https://echarts.apache.org/), [Chart.js](https://www.chartjs.org/), [QuickChart](https://quickchart.io/)), **grammar-of-graphics tools** ([Vega-Lite](https://vega.github.io/vega-lite/), [Plotly](https://plotly.com/)), **code-based renderers** ([Matplotlib](https://matplotlib.org/), [D3](https://d3js.org/)), **BI & dashboard platforms** ([Vizro](https://vizro.readthedocs.io/), [Metabase](https://www.metabase.com/)), and **data-aware visualizers** ([DuckDB](https://duckdb.org/)+Plotly integrations).

The headline finding: **[AntV's mcp-server-chart](https://github.com/antvis/mcp-server-chart) is the clear leader** with 4,069 stars and 27 tools covering 26+ chart types — from basic line/bar/pie through geographic maps, mind maps, Sankey diagrams, and organization charts. It's the most comprehensive standalone charting MCP server by a wide margin. The [ECharts](https://echarts.apache.org/) ecosystem is a close second with both an official Apache server and a community alternative that provides full syntax control. The main gap is in **end-to-end workflows** — most servers generate charts but don't handle data loading, transformation, or interactive exploration. Pairing a visualization server with a data server (like [DuckDB](https://duckdb.org/) or a database MCP) fills that gap. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## Recent Updates (May 2026)

**Grafana releases one of the highest-starred MCP servers in the ecosystem.** [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) has reached **3,012 stars** — making it larger than the Vizro parent repo and second only to AntV in this category. Version [v0.14.0](https://github.com/grafana/mcp-grafana/releases/tag/v0.14.0) (May 8, 2026) added a generic API request tool, OpenSearch datasource support, OTLP log export, and plugin info retrieval. Written in Go, official from Grafana Labs, MIT licensed. The previous review noted the absence of enterprise BI and observability MCP servers; Grafana's server directly addresses observability visualization. See the new [Grafana & Observability](#grafana--observability) section below.

**Tableau launches official MCP server, now at v2.2.4.** [tableau/tableau-mcp](https://github.com/tableau/tableau-mcp) (270 stars, Apache 2.0) was created May 2025 and has since become one of the most actively maintained enterprise BI MCP servers. The major [v2.0.0 release](https://github.com/tableau/tableau-mcp/releases/tag/v2.0.0) (May 8, 2026) introduced custom view tools, explicit data model relationships, site-level configuration, and refactored logging. [v2.1.0](https://github.com/tableau/tableau-mcp/releases/tag/v2.1.0) (May 12) and [v2.2.4](https://github.com/tableau/tableau-mcp/releases/tag/v2.2.4) (May 14) followed within days. The previous review called the absence of a Tableau MCP server a significant gap — that gap is now filled. Community ecosystem growing: TheInformationLab/tableau_mcp_starter_kit (24 stars, LangChain integration) and wjsutton/tableau-public-mcp (15 stars). See the updated [Tableau section](#tableau) below.

**imlewc/metabase-server takes the Metabase star lead.** [imlewc/metabase-server](https://github.com/imlewc/metabase-server) (145 stars) now leads the fragmented Metabase MCP ecosystem, surpassing easecloudio (76 stars) and jerichosequitin (74 stars). The Metabase category now has at least five community servers with no official integration — the star gap between imlewc and the rest has widened.

**Key dormancy notes:**
- **hustcc/mcp-echarts** (229 stars): no activity since v0.7.1 (January 30, 2026) — the community ECharts alternative appears dormant
- **vizro-mcp**: last updated v0.1.4 (February 4, 2026) — no MCP-specific updates in ~3.5 months, though vizro-core reached v0.1.55 (May 15) with new features including hierarchical filters and custom action notifications
- **isaacwasserman/mcp-vegalite-server**: no repository activity since May 2025 — appears abandoned after a year of inactivity

**AntV mcp-server-chart minor updates.** Still on v0.9.10 (no new release), but two post-release commits: radar chart alignment option added (May 6, 2026, PR #301), and improved error handling returning `isError` instead of throwing on chart failures (April 28, PR #292). Stars: 4,069.

## Charting Libraries

### AntV

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) | 4,069 | TypeScript | 27 | stdio, SSE, Streamable |

**antvis/mcp-server-chart** (4,069 stars, TypeScript, MIT, [v0.9.10](https://github.com/antvis/mcp-server-chart/releases)) is the dominant data visualization MCP server. Twenty-seven tools covering 26+ chart types organized into clear categories: basic charts (line, bar, area, column, pie, scatter), statistical visualizations (boxplot, histogram, violin), hierarchical data (treemap, mind map, organization chart), flow and relationship diagrams (Sankey, network graph, fishbone, flow diagram), specialized charts (funnel, radar, liquid, word cloud, Venn, dual-axes, waterfall), geographic visualizations (district map, pin map, path map), and data tables (spreadsheet and pivot table). Built on [AntV's](https://antv.antgroup.com/) G2 and other visualization libraries. Three transport modes give flexibility for desktop, web, and cloud deployments. Install via [`npx -y @antv/mcp-server-chart`](https://www.npmjs.com/package/@antv/mcp-server-chart) for instant setup, or Docker for production. Minor post-release updates: radar chart alignment option (May 6, 2026) and improved error handling (April 28). If you need one visualization server, this is it.

### Apache ECharts

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [apache/echarts-mcp](https://github.com/apache/echarts-mcp) | 69 | JavaScript | 1 | stdio |
| [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) | 229 | TypeScript | 15+ | stdio, SSE, Streamable |

**apache/echarts-mcp** (69 stars, JavaScript, Apache 2.0) is the official [Apache ECharts](https://echarts.apache.org/) MCP server. Simple design: receives chart type, data, and parameters from the LLM, generates an ECharts visualization, uploads it to cloud storage (Baidu BCE), and returns the image URL. Supports bar, line, pie, scatter, funnel, tree, treemap, and sunburst charts. Theme customization included. The cloud dependency is notable — you need Baidu BCE credentials configured, which limits self-hosted use. Active commits continue as of May 2026, but no formal versioned releases have been cut. Good for teams already in the Baidu Cloud ecosystem, but the cloud upload requirement is a meaningful constraint. Notably, the [official ECharts site](https://echarts.apache.org/) does not mention or promote this MCP server.

**hustcc/mcp-echarts** (229 stars, TypeScript, MIT, [v0.7.1](https://github.com/hustcc/mcp-echarts/releases/tag/v0.7.1)) is the community alternative. Full [ECharts](https://echarts.apache.org/) syntax support — any chart type, styling, or theme that ECharts supports works here. Three export formats: PNG, SVG, and ECharts option JSON. **MinIO integration** for URL-based chart storage instead of base64 encoding, which matters for large or numerous charts. Zero external dependencies for basic use. Local-only processing for security. Three transport modes (stdio, SSE, Streamable HTTP) for flexible deployment. **Note: the repo has had no activity since v0.7.1 (January 30, 2026)** — the project appears dormant. The official apache/echarts-mcp continues to receive commits and may be the better long-term choice if hustcc/mcp-echarts remains inactive.

### Chart.js / QuickChart

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [GongRzhe/Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server) | 160 | JavaScript | 2 | stdio |
| [KamranBiglari/mcp-server-chart](https://github.com/KamranBiglari/mcp-server-chart) | 7 | TypeScript | 15+ | stdio, HTTP, SSE |

**GongRzhe/Quickchart-MCP-Server** (160 stars, JavaScript, MIT, **[archived March 2026](https://github.com/GongRzhe/Quickchart-MCP-Server)**) generates charts via [QuickChart.io](https://quickchart.io/)'s URL-based [Chart.js](https://www.chartjs.org/) rendering service. Two tools: `generate_chart` (produces chart URLs) and `download_chart` (saves chart images locally). Supports bar, line, pie, doughnut, radar, polar area, scatter, bubble, radial gauge, and speedometer charts. Chart.js configuration format gives full customization. The catch: **this project is now archived and read-only**. It still works since [QuickChart.io](https://quickchart.io/) is still running, but no further updates. Also depends on an external service — not ideal for air-gapped or privacy-sensitive environments.

**KamranBiglari/mcp-server-chart** (7 stars, TypeScript, MIT) provides 15+ chart types with comprehensive Zod schema validation for type-safe chart configuration. Basic charts (bar, line, pie, radar, polar area), advanced (doughnut, scatter, bubble, OHLC), and specialized (violin plot, gauge, radial gauge, progress bar, sparkline, Sankey diagram). Three deployment options: local server, HTTP streaming, and SSE endpoints. Low adoption but architecturally sound with proper TypeScript typing throughout.

## Grammar-of-Graphics Tools

### Vega-Lite

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) | 96 | Python | 2 | stdio |
| [markomitranic/mcp-vegalite-server](https://github.com/markomitranic/mcp-vegalite-server) | 4 | Python | 2 | stdio |

**isaacwasserman/mcp-vegalite-server** (96 stars, Python) brings [Vega-Lite](https://vega.github.io/vega-lite/)'s declarative grammar-of-graphics to MCP. Two tools: `save_data` (stores named data tables on the server) and `visualize_data` (renders Vega-Lite specifications against stored data). Dual output: text mode returns the full Vega-Lite JSON specification, PNG mode returns a base64-encoded image via MCP ImageContent. The declarative approach is powerful — LLMs are good at generating Vega-Lite specs, and the grammar-of-graphics paradigm means the same spec language handles simple bar charts and complex layered visualizations. Eleven commits. Docker and uv installation supported. **As of May 2026, the repo has had no activity since May 2025 — a full year without updates.** Treat as abandoned; verify current status before adopting.

**markomitranic/mcp-vegalite-server** (4 stars, Python) is a fork of isaacwasserman's server with the same two-tool design. Listed on PulseMCP and other MCP registries. No significant divergence from the original — use the upstream version unless you need specific fork changes.

### Plotly

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [arshlibruh/plotly-mcp-cursor](https://github.com/arshlibruh/plotly-mcp-cursor) | 9 | Python | 7 | stdio |

**arshlibruh/plotly-mcp-cursor** (9 stars, Python) is a [Plotly](https://plotly.com/) Graph Objects MCP server designed for Cursor. Currently Phase 1 with 5 basic trace builders (scatter, bar, line, pie, histogram) plus figure assembly and layout controllers — 7 tools total. Outputs interactive HTML with embedded [Plotly.js](https://plotly.com/javascript/) supporting zoom, pan, and hover. Plans for 49+ total trace types across 4 additional phases. Only 2 commits — very early-stage. The [Plotly](https://plotly.com/) ecosystem deserves a more mature MCP server than what currently exists. For now, Plotly visualization is better served through data-aware tools like xoniks/mcp-visualization-duckdb (below) that use Plotly as their rendering backend.

## Code-Based Renderers

### Matplotlib

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [xlisp/visualization-mcp-server](https://github.com/xlisp/visualization-mcp-server) | 10 | Python | 8 | stdio |
| [newsbubbles/matplotlib_mcp](https://github.com/newsbubbles/matplotlib_mcp) | 2 | Python | Multiple | stdio |
| [StacklokLabs/plotting-mcp](https://github.com/StacklokLabs/plotting-mcp) | 9 | Python | 1 | stdio |

**xlisp/visualization-mcp-server** (10 stars, Python, MIT) provides eight specialized visualization tools using [Matplotlib](https://matplotlib.org/): relationship graphs, scatter plots, 3D visualizations (scatter, surface, wireframe), classification plots, histograms, line charts, and heatmaps. Auto-save functionality and interactive Matplotlib windows for live display. Dependencies include Matplotlib, NumPy, Pandas, and NetworkX. The 3D visualization support sets this apart from other Matplotlib servers — surface plots and wireframes are useful for scientific and engineering data.

**newsbubbles/matplotlib_mcp** (2 stars, Python, MIT) takes a comprehensive typed approach with Pydantic models for all API interactions. Supports basic plots (line, scatter, bar, histogram, pie), statistical visualizations (box plots, violin plots, heatmaps), advanced plotting (contour, vector fields, polar), and 3D visualization. Figure and subplot management with multiple export formats. Includes a pre-built visualization agent with CLI interface. Five commits — early but architecturally ambitious with full type safety.

**StacklokLabs/plotting-mcp** (9 stars, Python, Apache 2.0, v0.0.2) transforms CSV data into visualizations. Single `generate_plot` tool with JSON-based configuration. Line charts, bar graphs, pie charts, and world maps (using Cartopy for geographic visualization). Base64-encoded PNG output for chat interfaces. CSV parsing with Pandas. The geographic mapping capability via Cartopy is unique among Matplotlib-based servers. Simple and focused.

### D3.js

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [iamfiscus/mcp-d3-server](https://github.com/iamfiscus/mcp-d3-server) | 16 | TypeScript | 2 | stdio |

**iamfiscus/mcp-d3-server** (16 stars, TypeScript, MIT) is a [D3.js](https://d3js.org/) documentation and code generation server. Two tools: `generate-d3-chart` (creates D3 code for different chart types) and `recommend-chart` (suggests appropriate chart types based on user data). Express-based server providing D3 visualization documentation, chart recommendations, and code generation. Single commit — this is a proof-of-concept rather than a production tool. The approach (generating D3 code rather than rendering images) is different from most visualization servers — useful if you need D3 code to embed in a web application rather than a standalone image.

## BI & Dashboard Platforms

### Vizro (McKinsey)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [mckinsey/vizro (vizro-mcp)](https://github.com/mckinsey/vizro/tree/main/vizro-mcp) | 3,690 (parent repo) | Python | Multiple | stdio |

**mckinsey/vizro-mcp** (Python, Apache 2.0) is the MCP server component of McKinsey's [Vizro](https://vizro.readthedocs.io/) low-code visualization toolkit. The parent repo has [3,690 stars](https://github.com/mckinsey/vizro) and active development — vizro-core reached [v0.1.55](https://github.com/mckinsey/vizro/releases) (May 15, 2026) with hierarchical filters, custom action notifications, and AgGrid cell data access. Creates Vizro-styled [Plotly](https://plotly.com/) charts and full dashboards step-by-step through LLM interaction. Configuration-driven: components (charts, tables, cards, KPI indicators, forms), controls (filters and parameters), actions (interactions, drill-throughs, export), and layouts (grid or flexible containers). Compatible with Claude Desktop and Cursor. This is the only MCP server that generates **full dashboard applications**, not just individual charts — useful for analysts who need to build data apps, not just one-off visualizations. **Note: vizro-mcp itself last updated at v0.1.4 (February 4, 2026)** — the MCP component has not tracked the main vizro-core release cadence. Core Vizro is actively developed; the MCP integration is lagging.

### Metabase

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [imlewc/metabase-server](https://github.com/imlewc/metabase-server) | 145 | — | — | — |
| [easecloudio/mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server) | 76 | TypeScript | 70+ | stdio |
| [jerichosequitin/metabase-mcp](https://github.com/jerichosequitin/metabase-mcp) | 74 | TypeScript | 6 | stdio |
| [CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server) | 51 | TypeScript | 81+ | stdio |

[Metabase](https://www.metabase.com/) has the most MCP servers of any BI platform — at least five community implementations, with the star rankings shifting as of May 2026. **[imlewc/metabase-server](https://github.com/imlewc/metabase-server)** (145 stars, created March 2025) now leads the category; last updated April 2026. **[easecloudio/mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server)** (76 stars) provides 70+ tools with full CRUD across dashboards, cards, collections, users, permissions, and databases; active as of May 2026. **[jerichosequitin/metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** (74 stars, [v1.1.5](https://github.com/jerichosequitin/metabase-mcp/releases)) had the strongest engineering (161 commits, up to 90% token reduction via caching and batch processing) but has not released an update since February 2026. **[CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server)** (51 stars) comes from the Devin AI team with 81+ tools and flexible loading modes (essential, all, write, read). **[CW-Codewalnut/metabase-mcp-server](https://github.com/CW-Codewalnut/metabase-mcp-server)** (15 stars, Python) provides DXT file support for easy Claude Desktop install. No official [Metabase](https://www.metabase.com/) MCP server exists — the community continues to fill the gap with competing approaches.

## Data-Aware Visualizers

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [xoniks/mcp-visualization-duckdb](https://github.com/xoniks/mcp-visualization-duckdb) | 19 | Python | Multiple | stdio |
| [c-cf/BI-Chart-MCP-Server](https://github.com/c-cf/BI-Chart-MCP-Server) | 13 | Python | Multiple | stdio |

**xoniks/mcp-visualization-duckdb** (19 stars, Python, MIT) bridges data querying and visualization in a single server. [DuckDB](https://duckdb.org/) handles local data processing while [Plotly](https://plotly.com/) generates interactive HTML charts. Eight chart types: bar, line, scatter, pie, histogram, box plot, heatmap, and area charts. Natural language interface with rule-based chart recommendation (no external LLM needed for chart type selection). CSV import, SQL query execution, and browser-based database explorer included. One-command install via pip with automatic Claude Desktop configuration. Databricks support for enterprise data warehouses. This is the closest thing to an end-to-end data visualization workflow in a single MCP server — it handles loading, querying, and rendering.

**c-cf/BI-Chart-MCP-Server** (13 stars, Python, Apache 2.0) connects AI assistants to multiple data sources for natural language visualization. Modular architecture with separate components for data loading, processing, and Vega-Lite rendering. Six commits — early-stage. The BI-focused design with data source connectivity differentiates it from pure charting servers.

## Enterprise BI & Observability

### Tableau

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [tableau/tableau-mcp](https://github.com/tableau/tableau-mcp) | 270 | — | Multiple | — |

**tableau/tableau-mcp** (270 stars, Apache 2.0, [v2.2.4](https://github.com/tableau/tableau-mcp/releases/tag/v2.2.4)) is the official [Tableau](https://www.tableau.com/) MCP server — one of the most actively maintained enterprise BI MCP servers in the ecosystem. Created May 2025; shipped five releases in May 2026 alone. The major [v2.0.0 release](https://github.com/tableau/tableau-mcp/releases/tag/v2.0.0) (May 8, 2026) restructured the server significantly: custom view tools, explicit data model relationships, site-level configuration, global server disable option, and refactored logging. [v2.1.0](https://github.com/tableau/tableau-mcp/releases/tag/v2.1.0) (May 12) and [v2.2.4](https://github.com/tableau/tableau-mcp/releases/tag/v2.2.4) (May 14) followed in rapid succession. Community ecosystem includes [TheInformationLab/tableau_mcp_starter_kit](https://github.com/TheInformationLab/tableau_mcp_starter_kit) (24 stars, LangChain integration) and [wjsutton/tableau-public-mcp](https://github.com/wjsutton/tableau-public-mcp) (15 stars) for Tableau Public. The previous version of this review cited no Tableau MCP server as a significant gap — that gap is now filled with an official, actively developed integration.

### Grafana & Observability

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 3,012 | Go | Multiple | stdio |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | 141 | Go | Multiple | stdio |

**grafana/mcp-grafana** (3,012 stars, Go, Apache 2.0, [v0.14.0](https://github.com/grafana/mcp-grafana/releases/tag/v0.14.0)) is the official [Grafana](https://grafana.com/) MCP server and one of the highest-starred data-adjacent MCP servers in existence. Active since December 2024 with continuous releases. [v0.14.0](https://github.com/grafana/mcp-grafana/releases/tag/v0.14.0) (May 8, 2026) added a generic API request tool, OpenSearch datasource support, OTLP log export, and plugin info retrieval. [v0.13.1](https://github.com/grafana/mcp-grafana/releases) (April 30) added VictoriaMetrics PromQL support. [v0.13.0](https://github.com/grafana/mcp-grafana/releases) (April 29) extended dashboard and alerting capabilities. The scope spans dashboards, data sources, metrics querying, alerting, incidents, and oncall integrations — not just visualization but the full observability stack. For teams running Grafana, this is a clear first-choice integration. Its 3,000+ stars put it on par with the Vizro parent repo and well above most category peers.

**grafana/loki-mcp** (141 stars, Go) provides [Loki](https://grafana.com/oss/loki/) log aggregation integration — natural language log querying for Grafana's logging stack. A more focused companion to mcp-grafana for teams heavily invested in Loki for log storage.

## What's missing

Several gaps remain, though two significant ones have closed since this review was first published:

- **No official [Plotly](https://plotly.com/) MCP server.** Plotly is the most popular interactive visualization library and still has no official MCP server. The existing community options are early-stage. A notable gap given Plotly's ubiquity in data science.
- **No [Power BI](https://powerbi.microsoft.com/) MCP server.** Microsoft's dominant enterprise BI product has no official or high-adoption community MCP server. This remains the largest missing integration in the enterprise BI space.
- **No [Streamlit](https://streamlit.io/) or [Dash](https://dash.plotly.com/) MCP servers.** Python's most popular dashboard frameworks lack dedicated MCP servers (Vizro is adjacent but distinct).
- **Limited interactivity.** Most servers generate static images (PNG) or standalone HTML files. Real-time interactive exploration — filtering, drilling down, brushing — isn't supported through MCP's current protocol.
- **No unified data-to-dashboard pipeline.** You typically need separate servers for data access, transformation, and visualization. The xoniks DuckDB server is the closest to all-in-one but is early-stage.
- **Gaps closed since initial publication:** [Tableau](https://www.tableau.com/) now has an official MCP server (270 stars, v2.2.4, actively developed). [Grafana](https://grafana.com/) has an official MCP server at 3,012 stars — one of the highest-starred in the entire MCP ecosystem, covering dashboards, alerting, and observability visualization.

## The bottom line

**[AntV's mcp-server-chart](https://github.com/antvis/mcp-server-chart) is the clear recommendation** for general charting needs — 4,069 stars, 27 tools, 26+ chart types, three transport modes, and MIT licensed. For Grafana users, **[grafana/mcp-grafana](https://github.com/grafana/mcp-grafana)** (3,012 stars, official) is the standout addition since this review was first published — one of the highest-starred MCP servers in the ecosystem, covering the full observability-to-visualization stack. For Tableau deployments, the **[official tableau/tableau-mcp](https://github.com/tableau/tableau-mcp)** (270 stars, v2.2.4) now provides a first-class enterprise BI integration with rapid development velocity. For ECharts users, **[apache/echarts-mcp](https://github.com/apache/echarts-mcp)** (69 stars) is now the better long-term bet — the community alternative (hustcc/mcp-echarts) has been dormant since January 2026. For declarative visualization, **[isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server)** exists but appears abandoned (no activity since May 2025) — verify status before adopting. For full dashboard generation, **[Vizro MCP](https://github.com/mckinsey/vizro/tree/main/vizro-mcp)** remains unique but its MCP component has lagged behind vizro-core development. For end-to-end data-to-chart workflows, **[xoniks/mcp-visualization-duckdb](https://github.com/xoniks/mcp-visualization-duckdb)** bundles querying and rendering together.

The category has matured significantly since early 2026. AntV remains dominant for pure charting. Grafana's arrival at 3,000+ stars signals that official, enterprise-grade MCP servers are now the expectation, not the exception. Tableau's rapid v2.x development arc shows the same pattern. The remaining gap is Power BI — the last major BI platform without a credible MCP integration.

**Rating: 3.5/5** — Strong top-end servers (AntV at 4,069 stars, Grafana at 3,012 stars) but the category is still fragmented with several community servers going dormant. Power BI remains absent. The best servers generate charts or dashboards well; none yet handle the complete data visualization lifecycle from raw data through interactive exploration.

*This review was last edited on 2026-05-18 using Claude Sonnet 4.6 (Anthropic).*
