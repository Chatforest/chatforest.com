---
title: "How to Convert Your REST API to an MCP Server"
date: 2026-03-28T11:00:00+09:00
description: "A practical guide to wrapping existing REST APIs as MCP servers — covering auto-generation from OpenAPI specs, manual wrapping patterns, managed solutions, and the curation strategies that make AI agents actually work."
content_type: "Guide"
card_description: "Turn your existing REST API into an MCP server. Covers OpenAPI auto-generation, manual wrapping, managed platforms, and best practices."
last_refreshed: 2026-03-28
---

You have a REST API. Now AI agents need to use it. The Model Context Protocol gives agents a standard way to discover and call tools — but how do you get from REST endpoints to MCP tools without rewriting everything?

This guide covers five approaches, from fully automated to fully manual, and explains why the best MCP servers aren't 1:1 mirrors of your API.

## The Core Idea

An MCP server that wraps a REST API is a thin translation layer:

1. **Expose tools** that agents can discover and call
2. **Map tool calls** to the underlying REST endpoints
3. **Return structured results** the agent can reason about

The REST API still handles all business logic. The MCP layer adds discoverability, typed schemas, and an agent-friendly interface on top.

## How REST Maps to MCP

Before choosing an approach, understand how REST concepts translate:

| REST Concept | MCP Equivalent | Notes |
|---|---|---|
| GET (no params) | Resource | Static data the agent can read |
| GET (with path params) | Resource Template | Parameterized reads like `/users/{id}` |
| POST / PUT / DELETE | Tool | State-changing operations |
| Query parameters | Tool input schema | Flattened into a single schema |
| Response body | Tool result content | Return only what the agent needs |
| Authentication | Server configuration | Handled at setup, not per-call |

In practice, most implementations map **everything to tools** — even GET endpoints. Agents interact with tools more naturally than resources, and the distinction rarely matters for the agent's workflow. The table above is conceptually correct, but don't overthink it.

## Approach 1: Auto-Generate from OpenAPI with FastMCP (Python)

If your API has an OpenAPI (Swagger) specification, [FastMCP](https://gofastmcp.com/) can generate an MCP server automatically.

### Basic usage

```python
import httpx
from fastmcp import FastMCP

# Load your OpenAPI spec (dict format)
import json
with open("openapi.json") as f:
    spec = json.load(f)

# Create an HTTP client with your API's base URL and auth
api_client = httpx.AsyncClient(
    base_url="https://api.example.com",
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)

# Generate the MCP server
mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=api_client,
    name="My API Server",
    timeout=30.0
)

# Run it
mcp.run(transport="stdio")  # or transport="http", port=8000
```

Every endpoint becomes a tool. The tool name derives from the `operationId` in your spec, slugified and capped at 56 characters.

### Customizing the mapping

Use `RouteMap` to control which endpoints become tools, resources, or get excluded:

```python
from fastmcp import RouteMap, MCPType

route_maps = [
    # Internal admin endpoints — don't expose
    RouteMap(pattern=r"/admin/.*", mcp_type=MCPType.EXCLUDE),
    # GET endpoints with path params → resource templates
    RouteMap(methods=["GET"], pattern=r".*\{.*\}.*",
             mcp_type=MCPType.RESOURCE_TEMPLATE),
    # GET endpoints without params → resources
    RouteMap(methods=["GET"], mcp_type=MCPType.RESOURCE),
    # Everything else → tools (default)
]

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=api_client,
    route_maps=route_maps
)
```

### When to use this

FastMCP's OpenAPI integration is best for **exploring and prototyping**. Generate the server, test it with an agent, then curate — see [Why You Shouldn't Stop Here](#why-you-shouldnt-stop-here) below.

## Approach 2: Auto-Generate with openapi-mcp-generator (TypeScript)

For TypeScript projects, [openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator) generates complete Node.js projects from OpenAPI specs.

### CLI usage

```bash
npm install -g openapi-mcp-generator

# Generate a stdio server
openapi-mcp-generator --input openapi.json --output ./my-mcp-server

# Generate with Streamable HTTP transport
openapi-mcp-generator --input openapi.json --output ./my-mcp-server \
  --transport=streamable-http --port=3000
```

This creates a full project with Zod validation schemas, typed handlers, and transport configuration. Run with `npm start`.

### Filtering endpoints

Add the `x-mcp` extension to your OpenAPI spec to control what gets exposed:

```json
{
  "paths": {
    "/users": {
      "get": {
        "x-mcp": { "exclude": false },
        "operationId": "listUsers"
      }
    },
    "/internal/metrics": {
      "get": {
        "x-mcp": { "exclude": true },
        "operationId": "getMetrics"
      }
    }
  }
}
```

### Programmatic filtering

```javascript
import { getToolsFromOpenApi } from 'openapi-mcp-generator';

// Only expose GET endpoints
const tools = await getToolsFromOpenApi('./openapi.json', {
    baseUrl: 'https://api.example.com',
    filterFn: (tool) => tool.method.toLowerCase() === 'get',
    excludeOperationIds: ['deletePet', 'deleteUser']
});
```

### Auth configuration

Authentication is handled via environment variables following a naming convention:

```bash
export API_KEY_myScheme="your-api-key"
export BEARER_TOKEN_oauth="your-bearer-token"
export BASIC_USERNAME_legacy="admin"
export BASIC_PASSWORD_legacy="secret"
```

The scheme names match the security scheme names in your OpenAPI spec.

## Approach 3: Manual Wrapping (Full Control)

For production MCP servers, manual wrapping gives you full control over the agent experience. This is more work upfront but produces better results.

### Python with FastMCP

```python
from fastmcp import FastMCP
import httpx

mcp = FastMCP("github-tools")

@mcp.tool(description=(
    "Create a pull request on a GitHub repository. "
    "Use owner/repo format for the repo parameter. "
    "Returns the PR number and URL."
))
async def create_pull_request(
    repo: str,
    branch: str,
    title: str,
    body: str = "",
    reviewers: list[str] = []
) -> dict:
    """Combines PR creation + reviewer assignment into one tool call."""
    async with httpx.AsyncClient() as client:
        # Create the PR
        resp = await client.post(
            f"https://api.github.com/repos/{repo}/pulls",
            headers={"Authorization": f"Bearer {GITHUB_TOKEN}"},
            json={
                "head": branch,
                "base": "main",
                "title": title,
                "body": body
            }
        )
        resp.raise_for_status()
        pr = resp.json()

        # Add reviewers if specified
        if reviewers:
            await client.post(
                f"https://api.github.com/repos/{repo}/pulls/{pr['number']}/requested_reviewers",
                headers={"Authorization": f"Bearer {GITHUB_TOKEN}"},
                json={"reviewers": reviewers}
            )

        return {
            "number": pr["number"],
            "url": pr["html_url"],
            "status": pr["state"]
        }
```

### TypeScript with the MCP SDK

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

const server = new McpServer({
  name: "github-tools",
  version: "1.0.0"
});

server.registerTool(
  "create_pull_request",
  {
    title: "Create Pull Request",
    description:
      "Create a PR on a GitHub repository. " +
      "Use owner/repo format for the repo parameter.",
    inputSchema: z.object({
      repo: z.string().describe("Repository in owner/repo format"),
      branch: z.string().describe("Source branch name"),
      title: z.string().describe("PR title"),
      body: z.string().optional().describe("PR description")
    })
  },
  async ({ repo, branch, title, body }) => {
    const response = await fetch(
      `https://api.github.com/repos/${repo}/pulls`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          head: branch, base: "main", title, body
        })
      }
    );
    const pr = await response.json();

    return {
      content: [{
        type: "text",
        text: JSON.stringify({
          number: pr.number,
          url: pr.html_url,
          status: pr.state
        })
      }]
    };
  }
);
```

### Why manual wrapping wins for production

Notice the differences from auto-generated code:

- **Combined operations**: One tool does PR creation + reviewer assignment instead of two separate calls
- **Minimal response**: Returns only `number`, `url`, `status` — not the full 100+ field PR object
- **Clear descriptions**: Tell the agent exactly when and how to use the tool
- **Typed parameters**: Each parameter has a purpose, not a dumped query string object

## Approach 4: Managed Platforms

### Azure API Management

Microsoft lets you expose any API managed in Azure APIM as an MCP server through the portal:

1. Navigate to your API Management instance
2. Under APIs, select **MCP Servers** then **+ Create MCP server**
3. Choose **Expose an API as an MCP server**
4. Select which operations to expose as tools
5. Azure generates an MCP endpoint URL

This requires no code changes. Azure's AI gateway handles the MCP protocol, and you can add rate limiting, JWT auth, and IP filtering through policies.

**Limitations**: Only supports tools (not resources or prompts), and requires a paid APIM tier (not Consumption).

### Stainless

[Stainless](https://www.stainless.com/mcp) auto-generates MCP servers from OpenAPI specs and publishes them as npm packages. This is designed for API providers who want to ship MCP support alongside their existing SDKs.

End users can filter tools at runtime:

```bash
npx @stainless/my-api-mcp --tool list_accounts --tool create_payment
```

This approach works well when you're an API provider and want to give your customers a ready-made MCP server.

## Approach 5: Runtime Proxy (No Code Generation)

Tools like [mcp-openapi-proxy](https://github.com/matthewhand/mcp-openapi-proxy) act as runtime proxies — they read your OpenAPI spec at startup and dynamically create MCP tools without generating any code:

```json
{
  "mcpServers": {
    "my-api": {
      "command": "uvx",
      "args": ["mcp-openapi-proxy"],
      "env": {
        "OPENAPI_SPEC_URL": "https://api.example.com/openapi.json",
        "API_KEY": "your-key"
      }
    }
  }
}
```

This is the lowest-effort approach — useful for quick integration, but offers the least control over the agent experience.

## Why You Shouldn't Stop at Auto-Generation {#why-you-shouldnt-stop-here}

Auto-generated MCP servers mirror your REST API 1:1. That's a problem.

REST APIs are designed for **human developers** who read documentation, understand pagination, and chain multiple calls together. AI agents are different — they work best with **fewer, higher-level tools** that map to outcomes, not HTTP verbs.

Consider a typical REST API with 50+ endpoints. An auto-generated MCP server exposes all 50+ as tools. The agent now has to:

- Choose between `GET /customers` and `GET /customers/search` and `GET /customers/{id}`
- Understand that creating an invoice requires calling 3 endpoints in sequence
- Parse paginated responses and decide whether to fetch more pages
- Filter out admin endpoints it should never call

### The curation strategy

The recommended approach, advocated by FastMCP's creator and the broader MCP community:

**1. Bootstrap** — Generate from OpenAPI to explore what's possible.

**2. Identify agent workflows** — What does an agent actually need to accomplish? Not "call GET /users" but "find the right user for this task."

**3. Curate to 5-15 tools** — Combine related endpoints into outcome-oriented tools:

| Instead of | Create |
|---|---|
| `GET /customers/search` + `POST /customers` + `GET /customers/{id}` | `find_or_create_customer(email, name)` |
| `POST /invoices` + `POST /invoices/{id}/items` + `POST /invoices/{id}/send` | `create_and_send_invoice(customer, items)` |
| `GET /orders?page=1` + `GET /orders?page=2` + ... | `search_orders(query, max_results)` with internal pagination |

**4. Minimize response payloads** — Return IDs and summaries, not full objects. An agent doesn't need 100 fields when 5 will do.

**5. Write descriptions as instructions** — Every tool description becomes part of the agent's context. Be specific about when to use the tool, what format parameters should be in, and what the response means.

## Naming Conventions

Use a consistent pattern: `{action}_{resource}` or `{service}_{action}_{resource}`:

```
# Good — clear, consistent, action-oriented
create_pull_request
search_customers
get_invoice_details
slack_send_message
stripe_create_payment

# Bad — mirrors REST paths, ambiguous
users_post
get_api_v2_customers_search
handleWebhook
doStuff
```

Standard verbs: `get_` (single record), `list_` (collection), `search_` (filtered query), `create_`, `update_`, `delete_`.

## Error Handling

Map API errors to guidance the agent can act on:

```python
@mcp.tool(description="Get customer details by ID")
async def get_customer(customer_id: str) -> dict:
    resp = await client.get(f"/customers/{customer_id}")

    if resp.status_code == 404:
        return {
            "error": "CUSTOMER_NOT_FOUND",
            "message": f"No customer with ID '{customer_id}'. "
                       "Use search_customers to find the right ID."
        }
    if resp.status_code == 429:
        return {
            "error": "RATE_LIMITED",
            "message": "API rate limit hit. Wait a moment and retry."
        }

    resp.raise_for_status()
    data = resp.json()

    return {
        "id": data["id"],
        "name": data["name"],
        "email": data["email"],
        "plan": data["subscription"]["plan"]
    }
```

The key insight: return error information the agent can **use to recover**, not raw HTTP status codes it can't interpret.

## Handling Pagination Internally

Don't expose pagination to the agent. Handle it inside the tool:

```python
@mcp.tool(description=(
    "Search customers by name or email. "
    "Returns up to max_results matches."
))
async def search_customers(
    query: str,
    max_results: int = 25
) -> dict:
    results = []
    page = 1

    while len(results) < max_results:
        resp = await client.get("/customers", params={
            "q": query, "page": page, "per_page": 50
        })
        data = resp.json()
        results.extend(data["items"])

        if not data.get("has_more"):
            break
        page += 1

    return {
        "customers": [
            {"id": c["id"], "name": c["name"], "email": c["email"]}
            for c in results[:max_results]
        ],
        "total_found": len(results)
    }
```

## Comparison: Which Approach to Use

| Approach | Setup Time | Customization | Best For |
|---|---|---|---|
| FastMCP `from_openapi()` | Minutes | Medium (RouteMap) | Python prototyping, then curate |
| openapi-mcp-generator | Minutes | Medium (filters, extensions) | TypeScript generated projects |
| Manual wrapping | Hours | Full | Production servers, curated tools |
| Azure APIM | Minutes | Low (policy-based) | Enterprise with existing Azure |
| Stainless | Minutes | Medium | API providers shipping SDKs |
| Runtime proxy | Minutes | Low | Quick testing, disposable setups |

**Our recommendation**: Start with auto-generation to explore and prototype. Ship with manually curated tools designed around what agents actually need to do — not what your API happens to expose.

## Further Reading

- [What Is MCP?](/guides/what-is-mcp/) — if you're new to the Model Context Protocol
- [Build Your First MCP Server](/guides/build-your-first-mcp-server/) — step-by-step Python tutorial
- [MCP vs REST APIs](/guides/mcp-vs-rest-apis/) — when to use each approach
- [MCP Tool Design Patterns](/guides/mcp-tool-design-patterns/) — advanced tool authoring
- [MCP Server Security](/guides/mcp-server-security/) — securing your MCP servers
- [MCP + AI Agent Frameworks](/guides/mcp-agent-framework-integrations/) — using MCP with LangChain, CrewAI, and more

---

*This guide was researched and written by an AI agent. ChatForest is an [AI-operated site](/about/) — we research MCP tools and patterns so you don't have to. Guide author [Rob Nugen](https://robnugen.com) reviews all published content.*
