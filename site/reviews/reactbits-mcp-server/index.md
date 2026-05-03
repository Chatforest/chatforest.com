# The ReactBits MCP Server — 135+ Animated React Components for AI Coding Agents

> ReactBits MCP server gives AI coding assistants access to 135+ animated React components from ReactBits.dev — searchable, with CSS and Tailwind variants, demo code, and dependency info.


**At a glance:** Community-built MCP server for ReactBits.dev, 42 GitHub stars, 5 tools, 110+ animated components, CSS and Tailwind variants, TypeScript, MIT license

> **May 2026 Update:** Stars grew modestly from 38 to 42 (+10.5%), but the server remains frozen since July 2025 — now 9+ months without a commit. The underlying ReactBits library has exploded from 24k to **38.8k stars**, but that growth hasn't reached this MCP server. Most significantly: ReactBits creator **David Haz explicitly stated his own MCP server "is not available"** and directed users to use [shadcn's MCP](https://ui.shadcn.com/docs/mcp) instead, effectively withdrawing any creator endorsement from the MCP ecosystem. React Bits Pro (paid tier, 50+ premium components) launched in early 2026 — none of those components are accessible via MCP. **Rating downgraded 3.5 → 3.0/5.**

ReactBits is one of the most popular animated React component libraries on GitHub, with over 38,000 stars and 110+ components spanning text animations, backgrounds, buttons, cards, and navigation elements. The [ReactBits MCP server](https://github.com/ceorkm/reactbits-mcp-server) by ceorkm bridges that library to AI coding agents — letting them search, browse, and pull component source code directly into your project without you copy-pasting from a browser. Note: this is an unofficial community server. ReactBits creator David Haz has stated his own MCP "is not available" and recommends shadcn's MCP instead.

The idea is straightforward: instead of describing what you want and hoping the LLM hallucinates something close, the agent can look up battle-tested, community-vetted components from ReactBits.dev and give you the actual code. Each component comes in four variants (JS-CSS, JS-Tailwind, TS-CSS, TS-Tailwind), and the MCP server surfaces all of them.

**Category:** [Developer Tools](/categories/developer-tools/)

## What It Does

The server exposes five tools:

- **list_components** — browse all available components, optionally filtered by category (Animations, Backgrounds, Buttons, Cards, Text Animations, Components, Navigation) and style variant (CSS or Tailwind).

- **get_component** — retrieve the full source code for a specific component in your chosen style variant. This is the core tool — it fetches the actual implementation from ReactBits.dev's GitHub repository.

- **search_components** — find components by name or description. Useful when you know what effect you want ("aurora background", "typewriter text") but not the exact component name.

- **get_component_demo** — get usage examples and demo code showing how to integrate a component into a React project. Includes prop documentation and typical usage patterns.

- **list_categories** — enumerate all component categories. Helpful for discovery when you're browsing rather than searching.

The server fetches component data from the ReactBits GitHub repository, caches it locally for performance, and serves it through the standard MCP protocol. It's read-only — no write operations, no side effects.

## Setup

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "reactbits": {
      "command": "npx",
      "args": ["-y", "reactbits-dev-mcp-server"]
    }
  }
}
```

### Cursor

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "reactbits": {
      "command": "npx",
      "args": ["-y", "reactbits-dev-mcp-server"]
    }
  }
}
```

### VS Code (Continue)

Add to your Continue configuration:

```json
{
  "mcpServers": [
    {
      "name": "reactbits",
      "command": "npx",
      "args": ["-y", "reactbits-dev-mcp-server"]
    }
  ]
}
```

### Global Installation

```bash
npm install -g reactbits-dev-mcp-server
```

### Requirements

- Node.js (for npx or global install)
- No API keys required
- No authentication needed

## Component Quality

The server includes a built-in health scoring system that rates component completeness on a 0–10 scale:

- **Excellent (9.0+/10):** Backgrounds, cursor animations, text effects — these are ReactBits' strongest categories with polished, production-ready implementations
- **Good (8.0+/10):** General components and navigation elements
- **Incomplete (2.0/10):** Buttons, forms, and loaders — these return placeholder code rather than working implementations

This transparency is valuable. The server warns you when a component is incomplete rather than silently serving broken code. But it also means roughly a third of the component categories aren't practically useful yet — a limitation inherited from the ReactBits library itself, not the MCP server.

## Dependencies to Know

Components from ReactBits use various animation libraries depending on the effect:

- **framer-motion** — most text animations
- **gsap** — cursor animations and complex transitions
- **three.js / @react-three/fiber** — 3D backgrounds and effects
- **ogl** — WebGL rendering

The MCP server surfaces dependency information for each component, so your AI agent can include the right `npm install` commands when integrating a component. This is a smart design choice — it prevents the common failure mode where generated code references libraries that aren't in your project.

## Who This Is For

**React developers using AI coding agents** who want quick access to polished animation components. Instead of describing an animation effect in prose and hoping the LLM generates something decent, you can pull in a tested, community-maintained implementation.

**Developers building visually rich UIs** who want to move fast. ReactBits components are copy-paste ready — the MCP server just makes the copy-paste happen through your AI agent instead of through a browser tab.

**Prototypers and demo builders** who need impressive visual effects without spending time implementing them from scratch. Text animations, background effects, and cursor interactions are exactly the kind of polish that makes prototypes look production-ready.

## What's Good

**Solves a real workflow problem.** Animated components are notoriously hard for LLMs to generate from scratch — they require precise CSS animations, timing functions, and often WebGL or canvas work. Pulling from a curated library is dramatically more reliable than generation.

**No authentication required.** Install and use. No API keys, no accounts, no rate limits. The server fetches from public GitHub repositories and caches results locally.

**Four style variants per component.** JS-CSS, JS-Tailwind, TS-CSS, TS-Tailwind. Whatever your project's tech stack, there's a matching variant. The agent can ask for the right one based on your project configuration.

**Built-in quality transparency.** The health scoring system means the agent knows when a component is incomplete and can warn you or suggest alternatives. This prevents the frustrating experience of integrating a component only to discover it's a placeholder.

**Dependency awareness.** Each component comes with its dependency list. The agent can install prerequisites before dropping in the component code — avoiding build errors on the first try.

**Backed by a massively popular library.** ReactBits itself has grown to 38,800+ GitHub stars (up from 24k). These aren't obscure components — they're widely used and community-vetted.

## What's Not

**42 stars — low adoption for the MCP server itself.** The underlying library is popular (38k+ stars), but this specific MCP server is a community project with minimal traction. The star gap between library and server has widened significantly.

**Incomplete component categories.** Buttons, forms, and loaders score 2.0/10 — they return placeholder code. If you need animated buttons or form components, this server won't help yet. That's a ReactBits limitation, but it affects the MCP server's utility.

**Frozen since July 2025 — now 9+ months stale.** All four npm versions (1.0.0 through 1.1.2) shipped on a single day in July 2025. The ReactBits library has continued evolving, meaning newer components won't be accessible via this server. The library now claims 110+ components where the server still advertises "135+" — the count is out of sync.

**Creator explicitly pointed away from MCP.** ReactBits creator David Haz stated in a GitHub issue that his own MCP server "is not available" and directed users to use [shadcn's MCP](https://ui.shadcn.com/docs/mcp) instead. This effectively signals no official MCP investment from the ReactBits team.

**React Bits Pro is inaccessible.** The premium paid tier (50+ advanced components, 70+ animated UI blocks) launched in early 2026 — none of these will ever appear in the community MCP server, which only accesses the free open-source library.

**Community-built, not official.** Multiple competing community implementations exist ([hasan-tec](https://github.com/hasan-tec/reactbits-mcp), [JohnCarter09](https://github.com/JohnCarter09/ReactBits_MCP), [duolabstech](https://github.com/duolabstech/react-bits-mcp-server)), all with zero meaningful adoption and all effectively abandoned.

**Read-only access to a read-only resource.** You're essentially getting a search interface over a component library that's already freely browsable at reactbits.dev. The value-add is convenience within the AI agent workflow, not access to anything new.

**No remote server option.** stdio only — no HTTP transport, no hosted server. Fine for local development, but limits integration options.

## The Bottom Line

The ReactBits MCP server is a useful convenience layer for React developers who want their AI coding agents to pull from a curated component library instead of generating animations from scratch. For the categories where ReactBits components are fully implemented — backgrounds, text animations, cursor effects — the results are significantly better than what most LLMs can generate independently.

The value proposition is narrow but real: animated components are one of the few areas where **retrieval genuinely beats generation** for AI coding agents. An LLM trying to write a WebGL aurora background from scratch will usually produce something mediocre. Pulling a tested implementation from a 24k-star library produces something that actually works.

The limitations have grown since this review was first published. The library itself has nearly doubled in popularity (24k → 38.8k stars), but the MCP server that bridges it to AI agents is now 9+ months frozen. The creator's own words — that the official MCP "is not available" and users should go elsewhere — signal that MCP is not on ReactBits' roadmap. React Bits Pro adds premium components that MCP will never expose. And the four npm versions that all shipped on the same day in July 2025 reveal this as a one-shot project, not an actively maintained integration.

The core value proposition (retrieval beats generation for animated components) still holds. But the practical risk has increased: the server may fall out of sync with the library, and users relying on it have no guarantee of updates, bug fixes, or support.

**Rating: 3.0 / 5** — The underlying ReactBits library is thriving, but this MCP server is effectively abandoned. The component categories where it works (backgrounds, text animations, cursor effects) still deliver real value over LLM generation. But with 9+ months of zero commits, creator-directed abandonment of the MCP ecosystem, and React Bits Pro components permanently out of reach, the trajectory is clearly declining. Use it for its strengths, but don't build a workflow that depends on it long-term.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*

