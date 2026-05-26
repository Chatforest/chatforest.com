# Salesforce's Data 360 MCP Server Solves the Tool Overload Problem

> Salesforce's Data 360 MCP Server doesn't register 190 REST operations as 190 tools. It registers three. A search tool, a payload examples tool, and an execute tool — three handles that give an LLM access to an entire enterprise API surface. That design choice is worth understanding.


In May 2026, Salesforce published the [Data 360 MCP Server](https://developer.salesforce.com/blogs/2026/05/introducing-the-data-360-mcp-server-developer-preview) as an open-source developer preview. The server connects Salesforce's Data 360 APIs — identity resolution, segmentation, ingestion, semantic models, and more — to any MCP-compatible client.

The technical implementation is worth examining. It solves a problem that anyone who has tried to expose a large enterprise API surface through MCP has encountered: too many tools breaks the context window.

## The Tool Overload Problem

MCP gives LLMs access to external capabilities through tools. Each tool has a name, a description, and a parameter schema. The LLM reads this information to understand what it can do and how to do it.

When a REST API has 190 distinct operations, the naive MCP implementation registers 190 tools. The problem: the full tool list goes into the LLM's context window on each request. At 190 tools, each with a description and parameter schema, you have consumed a significant portion of a context window before the LLM has done any work. The model may also struggle to select accurately from such a large flat list of options.

Cloudflare's engineering team wrote about this problem when building their own MCP server. The Salesforce Data 360 team referenced that research explicitly when designing their solution.

## Three Tools Instead of 190

The Data 360 MCP Server consolidates 190 REST operations behind three facade tools:

**search** — The LLM uses this to discover capabilities by intent, keyword, or family. Instead of scanning a list of 190 tool names, the model describes what it wants to do and the search tool returns the relevant operations. This makes the discovery pattern conversational rather than exhaustive.

**payload_examples** — Before executing an operation, the LLM fetches a working JSON payload example for that specific operation. This solves a real problem with complex enterprise APIs: the parameter schemas are often intricate and context-specific. Rather than asking the model to synthesize correct parameters from scratch, the tool provides a concrete working example to adapt.

**execute** — The LLM calls this with a specific operation name and the appropriate parameters. Execution is the final step after the model has already discovered the right operation and understood the payload structure.

The workflow is always: search → payload_examples → execute. Three steps, three tools, regardless of which of the 190 underlying operations is involved.

## What the 190 Operations Cover

Under the hood, the three facade tools map to 187 Data 360 operations organized into 21 tool families. The coverage spans the core Data 360 API surface:

- **Ingestion** — pushing data into Data 360 from external sources
- **Identity resolution** — merging records across sources into unified customer profiles
- **Transforms and mappings** — shaping and joining data within the platform
- **Segmentation** — building and managing audience segments
- **Retrievers** — querying the unified data model
- **Semantic models** — describing what your data means in terms the platform understands

This is the data infrastructure layer of Salesforce's AI platform. The MCP server makes that infrastructure reachable from any MCP-compatible client — Claude Code, Cursor, Codex, or any other tool that speaks MCP via stdio transport.

## Current State: Developer Preview

The server is in developer preview. There are a few limitations worth knowing:

It runs locally via stdio transport, not as a remotely hosted service. Each running instance connects a single user to a single Salesforce org. The multi-tenant version — where the server handles multiple users — is not yet available. The [GitHub repository](https://github.com/forcedotcom/d360-mcp-server) includes an installer script that configures common MCP clients.

Requirements are Java 17 or later and Maven 3.9 or later, plus a Salesforce org with Data 360 enabled.

When the server reaches general availability, Salesforce plans to offer it as a Salesforce Hosted MCP Server — the same distribution channel as their other product integration MCP servers, which became generally available in April 2026.

## The Pattern Is Worth Generalizing

The three-tool facade pattern is not Salesforce-specific. It describes a general architectural approach for any MCP server that wraps a large, structured API:

- **One tool for discovery** — lets the model navigate to the right capability
- **One tool for context** — gives the model the information it needs to call correctly
- **One tool for execution** — does the actual work

This is distinct from the common approach of one tool per endpoint, and also distinct from attempting to cram everything into a single monolithic tool. The three-tool structure preserves explicitness (the model knows exactly what it is doing) while keeping the context footprint manageable (only three tool definitions, not 190).

The MCP ecosystem is young enough that conventions for server design at scale are still forming. The facade pattern is one of the more interesting structural proposals to appear so far, and a major enterprise software vendor adopting it explicitly is a signal that this approach has traction.

---

*Salesforce Data 360 MCP Server was announced as a developer preview in May 2026. Source: [Salesforce Developers Blog](https://developer.salesforce.com/blogs/2026/05/introducing-the-data-360-mcp-server-developer-preview) and [github.com/forcedotcom/d360-mcp-server](https://github.com/forcedotcom/d360-mcp-server).*

