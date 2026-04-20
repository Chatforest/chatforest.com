# Best Design MCP Servers in 2026

> Figma, Penpot, Adobe Creative Suite, Lucid diagramming, UI component libraries, and more — we've reviewed 30+ design MCP servers across 8 categories. Here's what works, what's emerging, and where the gaps are.


Design MCP servers let AI agents interact with design tools — reading Figma layouts, generating UI components, controlling Adobe Creative Suite, manipulating Penpot files, and accessing component libraries. Instead of switching between your IDE and your design tool, you describe what you want and the agent builds it using data from the source.

We've researched 30+ design MCP servers across the full landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in March 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Figma (design-to-code) | [Framelink MCP](https://github.com/GLips/Figma-Context-MCP) | 13,800+ | [Figma Dev Mode](https://mcp.figma.com/mcp) (official, 13 tools, OAuth) |
| Figma (manipulation) | [TalkToFigma](https://github.com/grab/cursor-talk-to-figma-mcp) | 6,300+ | [Figma Dev Mode](https://mcp.figma.com/mcp) (code-to-canvas) |
| Penpot (open-source) | [penpot/penpot-mcp](https://github.com/penpot/penpot-mcp) | 220 | [montevive/penpot-mcp](https://github.com/montevive/penpot-mcp) (community) |
| Adobe Creative Suite | [VoidChecksum/adobe-mcp](https://github.com/VoidChecksum/adobe-mcp) | — | [alisaitteke/photoshop-mcp](https://github.com/alisaitteke/photoshop-mcp) (50+ Photoshop tools) |
| UI component generation | [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) | 5,700+ | [magicuidesign/mcp](https://github.com/magicuidesign/mcp) (Magic UI library) |
| Design systems | [shadcn/ui MCP](https://shadcnstudio.com/mcp) | — | [Flowbite MCP](https://flowbite.com/) (Tailwind components) |
| Diagramming | [Lucid Software MCP](https://lucid.co/) | — | — (first mover) |
| CAD / 3D modeling | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | 17,800+ | [jingcheng-chen/rhinomcp](https://github.com/jingcheng-chen/rhinomcp) (274 stars) |

## Why design MCP servers matter

Design-to-code translation is one of the highest-friction steps in software development. Designers create in Figma, developers rebuild in React. Design MCP servers eliminate that gap by giving AI agents direct access to design data.

The value comes in three forms:

1. **Design-to-code translation.** Paste a Figma URL, and your AI agent generates code that matches the design — using your project's components, framework, and conventions. No more manually inspecting frames for padding values and hex colors.
2. **Design manipulation.** Instead of learning Figma's interface or Adobe's toolbars, tell your agent: "Create a card component with a 16px border radius and our brand blue." The agent creates the design element directly.
3. **Component libraries on tap.** Servers like 21st.dev Magic and Magic UI give agents access to production-ready component catalogs. Ask for "a marquee of logos" and get back a polished, responsive React component — no manual browsing of component docs.

The landscape splits into eight categories: **Figma design-to-code** (reading designs for code generation), **Figma manipulation** (creating and modifying designs), **Penpot** (open-source alternative), **Adobe Creative Suite** (Photoshop, Illustrator, Premiere, After Effects), **UI component generation** (AI-generated UI from prompts), **design systems** (shadcn, Tailwind, component libraries), **diagramming & process design** (Lucid Software), and **CAD/3D modeling** (Blender, Rhino, AutoCAD).

---

## Figma design-to-code servers

This is the most mature and most competitive design MCP category. Two servers dominate: Framelink (community, descriptive output) and Figma Dev Mode (official, prescriptive output with exclusive write operations).

### The winner: Framelink MCP (GLips/Figma-Context-MCP)

**Stars:** 13,800+ | **Forks:** 1,093 | **Language:** TypeScript | **License:** MIT | **Tools:** 2

[Framelink](https://github.com/GLips/Figma-Context-MCP) is the most adopted design-to-code MCP server by a wide margin. Two tools (`get_figma_data` and `download_figma_images`) that output descriptive JSON instead of prescriptive React code. [Full review →](/reviews/framelink-figma-mcp-server/)

**Why it wins:** Descriptive output beats prescriptive output. When Figma's official server sends `<div className="flex gap-4 p-6 bg-white rounded-xl">`, your AI copies that structure — even if your project uses Vue, Svelte, or a different CSS approach. When Framelink sends `{layout: "horizontal", gap: 16, padding: 24, background: "#fff", borderRadius: 12}`, your AI generates code matching your project's conventions.

**Key features:**
- **Descriptive JSON output** — framework-agnostic design data
- **Preserved component nesting** — official server flattens it
- **~25% smaller payloads** — less token usage
- **Works with any Figma account** — no Dev seat required, no 6-calls/month cap
- **53K+ weekly npm downloads**, 17 releases, v0.7.1 (March 2026)
- Compatible with Cursor, Claude Code, Windsurf, Cline, VS Code, Zed, Amp, and more

**The catch:** Read-only — cannot create or modify designs. Two tools means no Code Connect, no design tokens, no FigJam support. No OAuth (uses personal access token).

**Best for:** Any developer converting Figma designs to code, regardless of framework.

### Runner-up: Figma Dev Mode MCP (Official)

**Stars:** 443 (guide repo) | **Language:** — | **License:** Proprietary | **Tools:** 13

[Figma Dev Mode MCP](https://mcp.figma.com/mcp) is Figma's official hosted server. Zero-install remote architecture with OAuth authentication. [Full review →](/reviews/figma-dev-mode-mcp-server/)

**Why it's notable:** In March 2026, [Figma opened the canvas to AI agents](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/) with expanded write capabilities. The `use_figma` tool lets agents create and modify real Figma objects — components, variables, frames, auto layout — using your existing design system. `generate_figma_design` captures live web pages and converts them to editable Figma frames. Code Connect mappings improve code generation accuracy over time. FigJam diagram generation from Mermaid syntax.

**The big March 2026 update — Skills:** [Figma Skills](https://help.figma.com/hc/en-us/articles/39166810751895-Figma-skills-for-MCP) are markdown files that teach agents how to complete multi-step design workflows. No plugin development, no code — just a markdown file with `## When to use` and `## Instructions` sections. Figma ships 9 example skills covering component library creation, design generation, accessibility specs, and code-to-design-token coordination. Anyone can [author custom skills](https://developers.figma.com/docs/figma-mcp-server/create-skills/) with optional `references/` folders for naming guides, variable taxonomies, or component rules. Skills make agent behavior predictable by encoding your conventions as executable instructions.

**Key features:**
- **`use_figma` tool** — execute Plugin API code to create/modify real Figma primitives (components, variables, frames, auto layout)
- **Skills system** — reusable markdown workflows that guide agent behavior on the canvas
- **Remote hosted** at `mcp.figma.com/mcp` — zero install
- **OAuth authentication** — no API key management
- **Code Connect** — map Figma components to code components
- **Design system rules** — framework-specific translation context
- **Broad client support** — Claude Code, Codex, Copilot (VS Code + CLI), Cursor, Augment, Factory, Firebender, Warp

**The catch:** Free during beta, but [will become a paid API](https://help.figma.com/hc/en-us/articles/39252411778583-Figma-MCP-server-FAQs). Prescriptive output (React + Tailwind by default) can conflict with your codebase conventions. Nested components get flattened. PulseMCP ranking (#136 globally) trails Framelink (#27) significantly.

**Best for:** Teams who want agents to both read and write Figma designs using their existing design system.

**Recommendation:** Start with Framelink for pure design-to-code reading. Add the official server if you need write operations — especially with the new Skills system, which makes agent-driven design creation far more reliable than raw tool calls.

**Full reviews:** [Framelink MCP](/reviews/framelink-figma-mcp-server/) · [Figma Dev Mode MCP](/reviews/figma-dev-mode-mcp-server/)

---

## Figma manipulation servers

These servers go beyond reading designs — they create and modify Figma elements directly. This is the "design from your IDE" category.

### The winner: TalkToFigma (grab/cursor-talk-to-figma-mcp)

**Stars:** 6,300+ | **Language:** TypeScript | **License:** — | **Tools:** 20+

[TalkToFigma](https://github.com/grab/cursor-talk-to-figma-mcp) started as a side project by a [Grab](https://www.grab.com/) engineer, built for his team. It went viral, earned 5,000+ stars, and Grab adopted it as an official open-source project.

**Why it wins:** Full bidirectional Figma control. Read designs, create shapes, modify text, adjust colors, manage components — all through natural language. Uses a WebSocket bridge between the MCP server and a Figma plugin, so it operates within Figma's plugin sandbox with proper permissions.

**Key features:**
- **20+ Figma operations** — shape creation, text modification, color adjustments, component management
- **WebSocket architecture** — Figma plugin ↔ WebSocket server ↔ MCP server
- **Works with Cursor, Claude Code** — any MCP-compatible IDE
- **Programmatic design manipulation** — create wireframes, prototypes, and full layouts from natural language

**The catch:** Requires running a WebSocket server locally plus installing the Figma plugin. More moving parts than Framelink. Not a read-optimized server — for pure design-to-code, Framelink produces better output.

**Best for:** Designers and developers who want to create or modify Figma designs from their IDE, not just read them.

### Also notable: Figma Dev Mode (write operations)

Since March 2026, Figma's official server is a serious alternative for design manipulation. The `use_figma` tool executes Plugin API code directly — creating components, variables, frames, and auto layout with full design-system awareness. Combined with Skills (markdown workflow definitions), agents can now follow multi-step design conventions reliably. TalkToFigma still wins for interactive, back-and-forth design sessions through its WebSocket bridge, but for automated, convention-driven design generation, the official server's Skills system is increasingly compelling. See the design-to-code section above for details.

---

## Penpot servers (open-source design)

[Penpot](https://penpot.app/) is the leading open-source design tool. Its "design expressed as code" philosophy makes it uniquely suited for MCP integration — designs are programmatically accessible at a granular level.

### The winner: penpot/penpot-mcp (Official)

**Stars:** 220 | **Forks:** 33 | **Language:** TypeScript | **Status:** Integrated into main repo (archived standalone Feb 2026)

[penpot/penpot-mcp](https://github.com/penpot/penpot-mcp) is Penpot's official MCP server, now integrated directly into the main Penpot repository. It communicates via a dedicated Penpot MCP Plugin through WebSocket, enabling AI agents to work within the context of a design file.

**Why it wins:** Official support from the Penpot team. Design-to-code, code-to-design, design-to-documentation, and documentation-to-design-system workflows — all bidirectional. Type-safe TypeScript implementation using the Penpot Plugin API. Free and open-source, unlike Figma's paid tiers.

**Key features:**
- **Bidirectional design workflows** — read and modify Penpot designs
- **Plugin API integration** — operates through Penpot's plugin system
- **WebSocket communication** — real-time connection between MCP server and Penpot
- **Design system generation** — create design system elements from documentation
- **Zero cost** — fully open-source, self-hostable

**The catch:** Smaller ecosystem than Figma. Penpot itself has fewer users, so less community tooling and fewer templates. The standalone repo was archived in February 2026 — you now need to use the version integrated into the main Penpot repo.

**Best for:** Teams committed to open-source design tools, or organizations that need self-hosted design infrastructure.

### Also notable: Community implementations

- **[montevive/penpot-mcp](https://github.com/montevive/penpot-mcp)** — community implementation with alternative approach
- **[zcube/penpot-mcp-server](https://github.com/zcube/penpot-mcp-server)** — connects AI assistants to Penpot via MCP
- **[Acorn-Technology-Solutions-inc/penpot-mcp](https://github.com/Acorn-Technology-Solutions-inc/penpot-mcp)** — connects AI agents to designs

The Penpot MCP ecosystem is small but growing, reflecting Penpot's own growth trajectory. As Figma alternatives gain traction, expect more MCP implementations.

---

## Adobe Creative Suite servers

Adobe dominates professional creative work — Photoshop, Illustrator, Premiere Pro, After Effects, InDesign. MCP servers for Adobe are community-driven (Adobe hasn't shipped an official MCP server) and generally work by executing scripts via Adobe's scripting engines.

### The winner: VoidChecksum/adobe-mcp

**Language:** — | **License:** — | **Tools:** Multi-app

[VoidChecksum/adobe-mcp](https://github.com/VoidChecksum/adobe-mcp) provides full Creative Cloud automation from Claude. Controls Photoshop, Illustrator, Premiere Pro, After Effects, InDesign, and Animate through a single unified MCP server.

**Why it wins:** Broadest Adobe coverage in a single server. Instead of installing separate MCP servers for each Adobe app, one server handles the entire Creative Cloud suite. Direct scripting engine integration for each application.

**Key features:**
- **Multi-app support** — Photoshop, Illustrator, Premiere Pro, After Effects, InDesign, Animate
- **Single unified interface** — one MCP server for the entire Creative Cloud
- **Script execution** — runs native scripts in each application's scripting environment

**The catch:** Community-maintained, not Adobe-supported. Relies on Adobe's scripting APIs, which vary in capability and reliability across applications. Requires the Adobe apps to be running locally.

### Also notable

**Photoshop-specific:**
- **[alisaitteke/photoshop-mcp](https://github.com/alisaitteke/photoshop-mcp)** — 50+ tools for Photoshop automation: layers, filters, selections, brushes, text, shapes, and workflow management
- **[mikechambers/adb-mcp](https://github.com/mikechambers/adb-mcp)** — Adobe Creative Suite MCP by a former Adobe developer

**Illustrator-specific:**
- **[spencerhhubert/illustrator-mcp-server](https://github.com/spencerhhubert/illustrator-mcp-server)** — runs scripts on Adobe Illustrator (macOS only, AppleScript)
- **[krVatsal/illustrator-mcp](https://github.com/krVatsal/illustrator-mcp)** — create vector graphics in Illustrator via natural language (Windows, TypeScript scripting engine)
- **[inaniwaudon/illustrator-mcp](https://github.com/inaniwaudon/illustrator-mcp)** — MCP server for Adobe Illustrator

**Multi-app:**
- **[matrayu/adobe-mcp](https://github.com/matrayu/adobe-mcp)** — unified server for Photoshop, Premiere Pro, Illustrator, and InDesign

**The gap:** Adobe has not released an official MCP server for any Creative Cloud application. All implementations are community-driven. There's no MCP server for Adobe XD (Adobe's own design tool, now largely supplanted by Figma), Adobe Firefly (AI image generation), or Adobe Express.

---

## UI component generation servers

These servers generate production-ready UI components from natural language descriptions. Think "v0 in your IDE" — describe a component, get back polished code.

### The winner: 21st-dev/magic-mcp

**Stars:** 5,700+ | **Language:** TypeScript | **Status:** Beta (free during beta)

[21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) is like [v0](https://v0.dev/) but inside your IDE. Type `/ui` followed by a description, and the server generates and writes UI component files directly into your project.

**Why it wins:** Production-quality output that follows your project's code style. Components are generated with clean TypeScript, proper props, responsive design, and proper integration with your existing codebase. Supports Cursor, Windsurf, VS Code/Cline, and Claude.

**Key features:**
- **Natural language → components** — describe what you want, get production-ready code
- **Project-aware** — follows your code style and file structure
- **Multiple variations** — generates options so you can pick your favorite
- **Handles complexity** — from simple buttons to complex interactive forms
- **Free during beta** — all features available at no cost

**The catch:** Beta status means potential instability. Depends on 21st.dev's API — if the service goes down, so does component generation. Works best with React + Tailwind projects. Not open about the generation model.

**Best for:** Frontend developers who want to ship polished UI components quickly without manually browsing component libraries.

### Runner-up: Magic UI MCP (magicuidesign/mcp)

[magicuidesign/mcp](https://github.com/magicuidesign/mcp) is the official MCP server for the Magic UI component library — React + Tailwind components specifically designed for marketing pages and landing sections.

**Why it's useful:** Instead of AI hallucinating component APIs, it pulls from Magic UI's actual registry. List components with filters, search by keyword, get full install instructions and source code. Production-ready components with the right JSX and Tailwind classes.

**Key features:**
- **Registry access** — browse Magic UI's component catalog from your IDE
- **Install instructions** — get exact setup steps for each component
- **Source code** — full component source, not just usage examples
- **Related items** — discover similar components

**Best for:** Teams already using or considering Magic UI for their frontend.

---

## Design system servers

These servers expose component libraries and design systems to AI agents, so they can generate code using your actual components rather than guessing.

### shadcn/ui MCP

[Shadcn Studio MCP](https://shadcnstudio.com/mcp) integrates shadcn/ui's component library directly into your IDE. The server supports multiple registries, including private ones — meaning your custom design system can be exposed to AI agents the same way the public shadcn/ui components are.

**Key features:**
- **Component browsing** — search and list shadcn/ui components
- **Multi-registry** — supports public and private component registries
- **AI theme generation** — generate themes for your design system
- **Figma-to-code** — integration with Shadcn Studio's Figma design system

### Flowbite MCP

Flowbite ships an official MCP server so AI assistants can access Flowbite's Tailwind CSS component library. Components, docs, and patterns are available directly in your IDE.

### shadcn-vue-mcp

[HelloGGX/shadcn-vue-mcp](https://github.com/HelloGGX/shadcn-vue-mcp) brings shadcn-vue and Tailwind CSS to Vue developers via MCP. If you're building with Vue and want AI-assisted component development, this is currently the only option.

### The trend

Design system MCP servers are early but growing fast. The pattern is clear: expose your component library via MCP so AI agents generate code using your actual components instead of hallucinating custom implementations. Expect every major component library to ship an MCP server by the end of 2026.

---

## Diagramming & process design servers

A newer category: MCP servers for creating flowcharts, sequence diagrams, process maps, and architecture diagrams through natural language. This bridges the gap between design tools and technical documentation.

### Lucid Software MCP Server

**Status:** GA (launched November 2025, updated March 2026) | **License:** Proprietary | **Tools:** Multiple

[Lucid Software](https://lucid.co/) — makers of Lucidchart and Lucidspark — ships an MCP server that lets AI agents search existing diagrams, create new ones from natural language descriptions, and (as of April 2026) edit documents via a new Edit Document API.

**Why it's notable:** Lucid is the first major diagramming platform to ship MCP support. The March 2026 update added a Process Agent that goes beyond simple generation — it asks clarifying questions about scope, risk, and compliance before creating diagrams. Support for swimlanes, color-coded workflows, nested containers, and sequence diagrams (complex login flows, API interactions) is built in.

**Key features:**
- **Search and fetch** — find and summarize existing diagrams across your Lucid workspace
- **Diagram creation** — describe workflows in natural language, get fully editable diagrams
- **Edit Document API** — request changes through natural language, Lucid AI executes modifications (launching April 2026)
- **Process Agent** — initiates discovery conversations with clarifying questions, analyzes scope and risk before building
- **Broad client support** — ChatGPT, Claude, Microsoft Copilot, GitHub Copilot, Cursor
- **ChatGPT Apps SDK** — upcoming direct integration for generating Lucid diagrams from ChatGPT

**The catch:** Proprietary and requires a Lucid subscription. The MCP server works within the Lucid ecosystem — you can't use it to generate standalone SVGs or Mermaid files. The Process Agent and Edit Document API are still rolling out (April 2026).

**Best for:** Teams already using Lucidchart for process documentation, architecture diagrams, or workflow visualization. The MCP server turns "draw me a diagram of this flow" into an actual editable Lucid document, not a text description.

---

## CAD / 3D modeling servers

For comprehensive coverage of CAD and 3D modeling MCP servers — Blender, AutoCAD, FreeCAD, SketchUp, Rhino/Grasshopper, Revit, Fusion 360, and OpenSCAD — see our dedicated reviews:

- [Interior Design & Architecture MCP Servers](/reviews/interior-design-architecture-mcp-servers/) — 30+ servers across 7 subcategories
- [CAD & 3D Modeling MCP Servers](/reviews/cad-3d-modeling-mcp-servers/) — dedicated CAD review

**The headlines:** [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) dominates with 17,800+ stars — one of the most popular MCP servers in any category. Every major CAD platform now has at least one MCP server. [rhinomcp](https://github.com/jingcheng-chen/rhinomcp) leads Rhino/Grasshopper with 274 stars. [FreeCAD-MCP](https://github.com/proximile/FreeCAD-MCP) offers 57 tools with Docker headless execution.

---

## Which design MCP server should you use?

**"I need to convert Figma designs to code"** → Start with **Framelink MCP**. Descriptive JSON output, framework-agnostic, works with any Figma account.

**"I need to create or modify Figma designs from my IDE"** → Use **TalkToFigma** for general manipulation, or **Figma Dev Mode** specifically for code-to-canvas capture.

**"I want an open-source alternative to Figma"** → Use **Penpot** with its official MCP server. Free, self-hostable, bidirectional design workflows.

**"I need to automate Adobe Creative Suite"** → Use **VoidChecksum/adobe-mcp** for multi-app control, or specialized servers for individual apps (Photoshop, Illustrator).

**"I want AI to generate UI components in my IDE"** → Use **21st-dev/magic-mcp** for general component generation, or **Magic UI MCP** if you're using that specific library.

**"I need my AI to know my design system"** → Look at **shadcn/ui MCP** or **Flowbite MCP** if you use those libraries. The broader pattern of exposing design systems via MCP is still early.

**"I need to create flowcharts or process diagrams"** → Use **Lucid Software MCP** if you're a Lucid customer. No open-source MCP diagramming alternative exists yet.

**"I need 3D modeling / CAD control"** → Start with **Blender MCP** (17,800+ stars). See our [interior design & architecture review](/reviews/interior-design-architecture-mcp-servers/) for the full landscape.

---

## Three trends to watch

### 1. Official servers are catching up — but community servers still lead

Figma shipped an official MCP server, but Framelink has 34x more stars. Penpot integrated MCP into their main repository. Adobe hasn't shipped anything yet. The pattern: community servers establish the market, then platforms ship official alternatives with exclusive capabilities (like Figma's code-to-canvas). Both coexist because they serve different needs.

### 2. Component libraries are becoming MCP-native

shadcn/ui, Magic UI, Flowbite — component libraries are shipping MCP servers so AI agents can generate code using actual components instead of guessing. This is the most impactful trend for everyday frontend development. By end of 2026, not having an MCP server will be a competitive disadvantage for component libraries.

### 3. Design manipulation is the next frontier

Reading designs for code generation is solved. The frontier is creating and modifying designs from code — TalkToFigma, Figma's code-to-canvas, Penpot's bidirectional workflows. The end state is a design-code loop where changes flow freely in both directions, with AI mediating the translation.

---

## What's missing

Despite 30+ servers and growing, significant gaps remain:

- **No Canva MCP for design** — Canva's MCP server is for app development assistance, not for creating or editing designs programmatically
- **No Adobe Firefly MCP** — Adobe's AI image generation has no MCP integration
- **No Adobe XD MCP** — though XD itself is being sunset in favor of Figma
- **No Sketch MCP** — the macOS-native design tool has no MCP server
- **No color palette / typography tools** — no dedicated servers for design token management, color theory, or font selection
- **No design QA servers** — no automated design-to-implementation comparison tools
- **No accessibility checking** — no servers that analyze designs for WCAG compliance
- **No collaborative design** — no MCP servers for real-time multi-agent design collaboration
- **No prototyping** — no servers for creating interactive prototypes or micro-interactions

The design MCP ecosystem is still early compared to developer tool categories (databases, version control, CI/CD). Expect rapid growth as more design platforms recognize MCP as a competitive necessity.

---

*Last updated: April 2026. Star counts and feature details may have changed since publication. See our individual reviews for the most detailed analysis: [Framelink MCP](/reviews/framelink-figma-mcp-server/) · [Figma Dev Mode MCP](/reviews/figma-dev-mode-mcp-server/) · [Interior Design & Architecture MCP](/reviews/interior-design-architecture-mcp-servers/) · [Image Generation MCP](/reviews/image-generation-mcp-servers/)*

