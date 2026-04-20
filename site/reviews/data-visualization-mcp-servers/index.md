# Data Visualization MCP Servers — AntV, ECharts, Vega-Lite, Plotly, Matplotlib, D3, and More

> Data visualization MCP servers let AI agents generate charts, dashboards, and interactive graphics from natural language.


Data visualization is a natural fit for MCP — AI agents that can turn a dataset into a chart from a natural language prompt eliminate one of the most common friction points in data work. The category spans five areas: **charting libraries** ([AntV](https://antv.antgroup.com/), [ECharts](https://echarts.apache.org/), [Chart.js](https://www.chartjs.org/), [QuickChart](https://quickchart.io/)), **grammar-of-graphics tools** ([Vega-Lite](https://vega.github.io/vega-lite/), [Plotly](https://plotly.com/)), **code-based renderers** ([Matplotlib](https://matplotlib.org/), [D3](https://d3js.org/)), **BI & dashboard platforms** ([Vizro](https://vizro.readthedocs.io/), [Metabase](https://www.metabase.com/)), and **data-aware visualizers** ([DuckDB](https://duckdb.org/)+Plotly integrations).

The headline finding: **[AntV's mcp-server-chart](https://github.com/antvis/mcp-server-chart) is the clear leader** with 4,000+ stars and 27 tools covering 26+ chart types — from basic line/bar/pie through geographic maps, mind maps, Sankey diagrams, and organization charts. It's the most comprehensive standalone charting MCP server by a wide margin. The [ECharts](https://echarts.apache.org/) ecosystem is a close second with both an official Apache server and a community alternative that provides full syntax control. The main gap is in **end-to-end workflows** — most servers generate charts but don't handle data loading, transformation, or interactive exploration. Pairing a visualization server with a data server (like [DuckDB](https://duckdb.org/) or a database MCP) fills that gap. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## Charting Libraries

### AntV

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) | 4,000+ | TypeScript | 27 | stdio, SSE, Streamable |

**antvis/mcp-server-chart** (4,000+ stars, TypeScript, MIT, [v0.9.10](https://github.com/antvis/mcp-server-chart/releases)) is the dominant data visualization MCP server. Twenty-seven tools covering 26+ chart types organized into clear categories: basic charts (line, bar, area, column, pie, scatter), statistical visualizations (boxplot, histogram, violin), hierarchical data (treemap, mind map, organization chart), flow and relationship diagrams (Sankey, network graph, fishbone, flow diagram), specialized charts (funnel, radar, liquid, word cloud, Venn, dual-axes, waterfall), geographic visualizations (district map, pin map, path map), and data tables (spreadsheet and pivot table). Built on [AntV's](https://antv.antgroup.com/) G2 and other visualization libraries. Three transport modes give flexibility for desktop, web, and cloud deployments. Install via [`npx -y @antv/mcp-server-chart`](https://www.npmjs.com/package/@antv/mcp-server-chart) for instant setup, or Docker for production. The star count (4,000+) makes it one of the most popular MCP servers in any category. If you need one visualization server, this is it.

### Apache ECharts

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [apache/echarts-mcp](https://github.com/apache/echarts-mcp) | 69 | JavaScript | 1 | stdio |
| [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) | 223 | TypeScript | 15+ | stdio, SSE, Streamable |

**apache/echarts-mcp** (69 stars, JavaScript, Apache 2.0) is the official [Apache ECharts](https://echarts.apache.org/) MCP server. Simple design: receives chart type, data, and parameters from the LLM, generates an ECharts visualization, uploads it to cloud storage (Baidu BCE), and returns the image URL. Supports bar, line, pie, scatter, funnel, tree, treemap, and sunburst charts. Theme customization included. The cloud dependency is notable — you need Baidu BCE credentials configured, which limits self-hosted use. Fifty-three commits. Good for teams already in the Baidu Cloud ecosystem, but the cloud upload requirement is a meaningful constraint. Notably, the [official ECharts site](https://echarts.apache.org/) does not mention or promote this MCP server.

**hustcc/mcp-echarts** (223 stars, TypeScript, MIT, [v0.7.1](https://github.com/hustcc/mcp-echarts/releases/tag/v0.7.1)) is the community alternative and the better choice for most teams. Full [ECharts](https://echarts.apache.org/) syntax support — any chart type, styling, or theme that ECharts supports works here. Three export formats: PNG, SVG, and ECharts option JSON. **MinIO integration** for URL-based chart storage instead of base64 encoding, which matters for large or numerous charts. Zero external dependencies for basic use. Local-only processing for security. Three transport modes (stdio, SSE, Streamable HTTP) for flexible deployment. Validation mechanisms improve AI model output accuracy. If you want ECharts in your MCP stack, this is the one — it's more flexible than the official server and doesn't require cloud storage credentials.

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

**isaacwasserman/mcp-vegalite-server** (96 stars, Python) brings [Vega-Lite](https://vega.github.io/vega-lite/)'s declarative grammar-of-graphics to MCP. Two tools: `save_data` (stores named data tables on the server) and `visualize_data` (renders Vega-Lite specifications against stored data). Dual output: text mode returns the full Vega-Lite JSON specification, PNG mode returns a base64-encoded image via MCP ImageContent. The declarative approach is powerful — LLMs are good at generating Vega-Lite specs, and the grammar-of-graphics paradigm means the same spec language handles simple bar charts and complex layered visualizations. Eleven commits. Docker and uv installation supported.

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
| [mckinsey/vizro (vizro-mcp)](https://github.com/mckinsey/vizro/tree/main/vizro-mcp) | 3,700 (parent repo) | Python | Multiple | stdio |

**mckinsey/vizro-mcp** (Python, Apache 2.0) is the MCP server component of McKinsey's [Vizro](https://vizro.readthedocs.io/) low-code visualization toolkit. The parent repo has [3,700 stars](https://github.com/mckinsey/vizro) and active development ([v0.1.54](https://github.com/mckinsey/vizro/releases) as of April 2026). Creates Vizro-styled [Plotly](https://plotly.com/) charts and full dashboards step-by-step through LLM interaction. Configuration-driven: components (charts, tables, cards, KPI indicators, forms), controls (filters and parameters), actions (interactions, drill-throughs, export), and layouts (grid or flexible containers). Compatible with Claude Desktop and Cursor. This is the only MCP server that generates **full dashboard applications**, not just individual charts — useful for analysts who need to build data apps, not just one-off visualizations.

### Metabase

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [easecloudio/mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server) | 64 | TypeScript | 70+ | stdio |
| [CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server) | 51 | TypeScript | 81+ | stdio |
| [jerichosequitin/metabase-mcp](https://github.com/jerichosequitin/metabase-mcp) | 67 | TypeScript | 6 | stdio |

[Metabase](https://www.metabase.com/) has the most MCP servers of any BI platform — at least five community implementations. **[easecloudio/mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server)** (64 stars) provides 70+ tools with full CRUD across dashboards, cards, collections, users, permissions, and databases. **[CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server)** (51 stars) comes from the Devin AI team with 81+ tools and flexible loading modes (essential, all, write, read). **[jerichosequitin/metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** (67 stars, [v1.1.5](https://github.com/jerichosequitin/metabase-mcp/releases)) is the most actively maintained (161 commits) with up to 90% token reduction via response optimization, multi-layer caching, and batch processing. **[CW-Codewalnut/metabase-mcp-server](https://github.com/CW-Codewalnut/metabase-mcp-server)** (15 stars, Python) provides DXT file support for easy Claude Desktop install. **[hyeongjun-dev/metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** (35 stars) adds another option. No official [Metabase](https://www.metabase.com/) MCP server exists — the community has filled the gap with multiple approaches. If you're on Metabase, you have options; evaluating which fits your specific Metabase version and deployment is worthwhile.

## Data-Aware Visualizers

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [xoniks/mcp-visualization-duckdb](https://github.com/xoniks/mcp-visualization-duckdb) | 19 | Python | Multiple | stdio |
| [c-cf/BI-Chart-MCP-Server](https://github.com/c-cf/BI-Chart-MCP-Server) | 13 | Python | Multiple | stdio |

**xoniks/mcp-visualization-duckdb** (19 stars, Python, MIT) bridges data querying and visualization in a single server. [DuckDB](https://duckdb.org/) handles local data processing while [Plotly](https://plotly.com/) generates interactive HTML charts. Eight chart types: bar, line, scatter, pie, histogram, box plot, heatmap, and area charts. Natural language interface with rule-based chart recommendation (no external LLM needed for chart type selection). CSV import, SQL query execution, and browser-based database explorer included. One-command install via pip with automatic Claude Desktop configuration. Databricks support for enterprise data warehouses. This is the closest thing to an end-to-end data visualization workflow in a single MCP server — it handles loading, querying, and rendering.

**c-cf/BI-Chart-MCP-Server** (13 stars, Python, Apache 2.0) connects AI assistants to multiple data sources for natural language visualization. Modular architecture with separate components for data loading, processing, and Vega-Lite rendering. Six commits — early-stage. The BI-focused design with data source connectivity differentiates it from pure charting servers.

## What's missing

Several gaps stand out:

- **No official [Plotly](https://plotly.com/) MCP server.** Plotly is the most popular interactive visualization library and has no official or mature community MCP server. The existing ones are early-stage.
- **No [Tableau](https://www.tableau.com/) or [Power BI](https://powerbi.microsoft.com/) MCP servers.** The enterprise BI tools with the largest market share have no MCP integration.
- **No [Streamlit](https://streamlit.io/) or [Dash](https://dash.plotly.com/) MCP servers.** Python's most popular dashboard frameworks lack dedicated MCP servers (Vizro is adjacent but distinct).
- **Limited interactivity.** Most servers generate static images (PNG) or standalone HTML files. Real-time interactive exploration — filtering, drilling down, brushing — isn't supported through MCP's current protocol.
- **No unified data-to-dashboard pipeline.** You typically need separate servers for data access, transformation, and visualization. The xoniks DuckDB server is the closest to all-in-one but is early-stage.

## The bottom line

**[AntV's mcp-server-chart](https://github.com/antvis/mcp-server-chart) is the clear recommendation** for general charting needs — 4,000+ stars, 27 tools, 26+ chart types, three transport modes, and MIT licensed. For ECharts users, **[hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts)** (223 stars) provides full syntax control with local rendering and multiple export formats. For declarative visualization, **[isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server)** (96 stars) brings grammar-of-graphics to MCP. For full dashboard generation, **[Vizro MCP](https://github.com/mckinsey/vizro/tree/main/vizro-mcp)** from McKinsey is unique in the category. For end-to-end data-to-chart workflows, **[xoniks/mcp-visualization-duckdb](https://github.com/xoniks/mcp-visualization-duckdb)** bundles querying and rendering together.

The category is broad and active but fragmented. The charting library servers (AntV, ECharts) are mature and production-ready. The grammar-of-graphics tools (Vega-Lite) are solid for their focused use case. Everything else — Plotly, Matplotlib, D3, BI platforms — ranges from early-stage to community experiments. The visualization space needs what dbt did for data transformation: a comprehensive, official-backed server that handles the full workflow.

**Rating: 3.5/5** — Strong top-end servers ([AntV at 4,000+ stars](https://github.com/antvis/mcp-server-chart) is exceptional) but the category is fragmented with no unified solution. Significant gaps in enterprise BI tools and interactive exploration. The best servers generate charts well; none yet handle the complete data visualization lifecycle.

*This review was last edited on 2026-04-15 using Claude Opus 4.6 (Anthropic).*

