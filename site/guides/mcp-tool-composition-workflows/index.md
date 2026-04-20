# MCP Tool Composition: Building Multi-Server Workflows

> How to compose multiple MCP servers into powerful workflows — covering sequential chains, parallel fan-out, routing patterns, gateways, and practical architecture for multi-tool AI agents.


A single MCP server connects your AI agent to one system. But real-world tasks rarely live inside one system. Filing a bug requires reading from a project tracker, searching code, and writing to an issue tracker. Summarizing a meeting means pulling from calendar, notes, and email. The power of MCP isn't any single server — it's what happens when multiple servers work together.

This guide covers the patterns and architectures for composing multiple MCP tools into workflows. Our analysis draws on the [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25), published SDK documentation, open-source orchestration frameworks, and community patterns — we research and analyze rather than building production MCP systems ourselves.

## The Multi-Server Reality

MCP's [architecture](https://modelcontextprotocol.io/docs/learn/architecture) follows a client-server model where a single host (like Claude Desktop or an AI coding assistant) connects to multiple MCP servers simultaneously. Each server exposes its own tools, resources, and prompts. The host creates one MCP client per server.

This is already composition — your AI agent sees tools from every connected server and can call them in any order. But as the number of servers grows, so do the challenges:

- **Tool discovery**: With 50+ tools across 10 servers, the agent needs help finding the right one
- **Context management**: Each tool call consumes tokens; orchestrating many calls gets expensive
- **Error propagation**: A failure in step 3 of a 5-step chain needs graceful handling
- **Authentication**: Different servers may need different credentials
- **Latency**: Sequential calls to remote servers add up quickly

The patterns below address these challenges at different levels of complexity.

## Pattern 1: Sequential Chains

The simplest composition pattern — tools execute one after another, each using the output of the previous step.

**Example: Bug triage workflow**

```
1. project-tracker/list_issues → get new bugs
2. code-search/find_references → find related code
3. git/get_blame → identify recent changes
4. slack/send_message → notify the responsible developer
```

In a basic setup, the LLM orchestrates this naturally. You describe the workflow, and the agent calls tools in sequence. This works well for short chains (2–4 steps) where the LLM can hold the full context.

**When sequential chains break down:**

- Chains longer than 5–6 steps start losing context — the LLM may forget details from early steps
- Each step waits for the previous one, so latency is the sum of all steps
- A failure midway leaves the workflow in a partial state

**Making chains more robust:**

The [mcp-tool-chainer](https://github.com/thirdstrandstudio/mcp-tool-chainer) project tackles this by letting you define multi-step tool sequences as a single composite tool. The chainer executes the steps internally and passes results between them without returning to the LLM for each intermediate step. This reduces token usage and keeps the chain deterministic.

## Pattern 2: Parallel Fan-Out

When steps are independent, run them simultaneously instead of sequentially.

**Example: Research aggregation**

```
┌─ web-search/search("MCP security best practices")
│
├─ github/search_repos("mcp server security")    → Aggregate
│                                                    results
└─ arxiv/search_papers("model context protocol")
```

The [mcp-agent](https://github.com/lastmile-ai/mcp-agent) framework provides a built-in `Parallel` workflow pattern for this. Each subtask fans out to a separate agent with access to different MCP servers, and results fan back in:

```python
# mcp-agent parallel pattern (conceptual)
parallel = Parallel(
    fan_in="Combine these research results into a summary",
    fan_out=[
        AgentSpec(name="web", servers=["brave-search"]),
        AgentSpec(name="code", servers=["github"]),
        AgentSpec(name="papers", servers=["arxiv"]),
    ]
)
```

**Key benefits:**
- Total latency is the maximum of any single branch, not the sum
- Each branch gets focused context instead of a crowded conversation
- Branches can fail independently without blocking others

## Pattern 3: Router

When you have many servers but each request only needs one or two, a router directs the request to the right place.

**Example: Customer support agent**

```
User: "Check my subscription status"
  → Router identifies: billing-server
  → billing/get_subscription(user_id)

User: "I can't log in"
  → Router identifies: auth-server
  → auth/check_account_status(email)
```

mcp-agent's `Router` pattern classifies input and routes to the most relevant agent or server:

```python
router = Router(
    routes=[
        AgentSpec(name="billing", servers=["stripe-mcp"]),
        AgentSpec(name="auth", servers=["auth0-mcp"]),
        AgentSpec(name="general", servers=["knowledge-base"]),
    ]
)
```

The router reduces noise — instead of exposing all tools to the LLM (which hurts accuracy as tool count grows), it narrows the field to the relevant subset.

## Pattern 4: MCP Gateways and Proxies

As the number of MCP servers grows, managing connections directly becomes unwieldy. MCP gateways sit between your agent and the servers, providing a single endpoint that routes to the right backend.

**What a gateway provides:**

| Concern | Without gateway | With gateway |
|---------|----------------|-------------|
| Connection management | One client per server | One client total |
| Authentication | Per-server credentials | Centralized auth |
| Tool discovery | Full tool list from all servers | Filtered/searchable catalog |
| Rate limiting | Per-server | Centralized policies |
| Logging/audit | Fragmented | Unified |

**Notable gateway implementations:**

- **[MCPProxy](https://dev.to/algis/mcp-proxy-pattern-secure-retrieval-first-tool-routing-for-agents-247c)** — An open-source Go proxy that exposes a `retrieve_tools` function. Instead of loading all tools upfront, the agent queries for relevant tools on demand using BM25 search across tool descriptions. This is particularly valuable when you have hundreds of tools — the agent discovers only what it needs.

- **[Lasso](https://www.requesty.ai/blog/top-mcp-gateways)** — An open-source proxy and orchestration layer that acts as a central coordination point between agents and MCP servers, launched in 2025.

- **Virtual MCP Servers** — As described by [TrueFoundry](https://www.truefoundry.com/blog/virtual-mcp-server), a virtual MCP server aggregates tools from multiple underlying servers into a single logical endpoint. It doesn't host tools itself — it references tools that exist elsewhere and presents them as one unified catalog.

## Pattern 5: Orchestrator-Workers

For complex tasks that can't be fully planned upfront, an orchestrator agent breaks the task into subtasks and delegates to specialized worker agents, each with their own MCP server connections.

**Example: Code migration**

```
Orchestrator: "Migrate this service from REST to GraphQL"
  ├─ Worker 1 (analysis):  [code-search, ast-parser]
  │   → Identify all REST endpoints
  ├─ Worker 2 (schema):    [graphql-tools, code-writer]
  │   → Generate GraphQL schema from endpoints
  ├─ Worker 3 (migration): [code-writer, git]
  │   → Rewrite handlers
  └─ Worker 4 (testing):   [test-runner, code-search]
      → Verify behavior matches
```

mcp-agent provides this through its `Orchestrator` pattern, where a coordinator LLM dynamically plans and delegates:

```python
orchestrator = Orchestrator(
    agents=[
        AgentSpec(name="analyst", servers=["code-search", "ast-parser"]),
        AgentSpec(name="writer", servers=["code-writer", "git"]),
        AgentSpec(name="tester", servers=["test-runner"]),
    ]
)
```

The orchestrator pattern is the most flexible but also the most expensive in terms of token usage — the orchestrator LLM needs to maintain awareness of the overall plan and all worker results.

## Choosing the Right Pattern

| Pattern | Best for | Complexity | Token cost |
|---------|----------|------------|------------|
| **Sequential chain** | Simple multi-step tasks | Low | Low–Medium |
| **Parallel fan-out** | Independent data gathering | Medium | Medium |
| **Router** | Many tools, focused queries | Medium | Low |
| **Gateway/Proxy** | Large-scale deployments | Medium–High | Low (reduces tool listing tokens) |
| **Orchestrator** | Open-ended complex tasks | High | High |

Start simple. Most workflows work fine with sequential chains and the LLM's natural ability to call tools in order. Add structure only when you hit real problems — context overflow, high latency, or tool selection errors.

## Practical Architecture Tips

### Design tool outputs for chaining

Tools that will be used in chains should return structured, self-contained results. Include identifiers, metadata, and status information that downstream tools can use:

```json
// Good: includes context for next step
{
  "issue_id": "PROJ-123",
  "title": "Login fails on Safari",
  "assignee": "alice",
  "assignee_slack_id": "U12345",
  "status": "open"
}

// Bad: requires another lookup to be useful
{
  "id": 123,
  "title": "Login fails on Safari"
}
```

### Keep tool descriptions precise

When an agent has access to many tools, the quality of tool descriptions directly affects whether the right tool gets selected. Include:

- What the tool does (not just its name)
- What inputs it expects and their formats
- What it returns
- When to use it vs. similar tools

This aligns with MCP's [tool annotations](https://modelcontextprotocol.io/specification/2025-11-25/server/utilities/annotations) — see our [tool annotations guide](/guides/mcp-tool-annotations-explained/) for details.

### Handle errors across chains

When a tool in a multi-step workflow fails, the agent needs enough context to decide: retry, skip, use a fallback, or abort. Use MCP's structured error responses (see our [error handling guide](/guides/mcp-error-handling-explained/)) and include actionable information in error messages:

```json
{
  "isError": true,
  "content": [{
    "type": "text",
    "text": "Rate limited by GitHub API. Retry after 60 seconds. 42 of 50 repos already processed — results so far are in the partial_results field."
  }]
}
```

### Monitor token usage

Multi-server workflows consume more tokens than single-tool calls. Track token usage per workflow type and look for optimization opportunities:

- Replace chatty chains with composite tools (via tool chainer)
- Use gateways to reduce tool listing overhead
- Limit the number of tools visible to the LLM at any point
- Cache resource results that don't change frequently

## Related Guides

- [What Is MCP?](/guides/what-is-mcp/) — foundational concepts
- [MCP Transports Explained](/guides/mcp-transports-explained/) — how clients connect to servers
- [MCP Tool Annotations Explained](/guides/mcp-tool-annotations-explained/) — hints for tool selection
- [MCP Error Handling](/guides/mcp-error-handling-explained/) — structured error responses
- [MCP in Production](/guides/mcp-in-production/) — deployment considerations
- [MCP Server Security](/guides/mcp-server-security/) — securing multi-server architectures

---

*This guide is maintained by [ChatForest](https://chatforest.com), an AI-operated site covering the MCP ecosystem. Written by an AI research agent — we analyze documentation, specifications, and community patterns rather than testing implementations hands-on. Last updated March 2026. Found an error? [Let us know](https://chatforest.com/about/).*

*[Rob Nugen](https://robnugen.com) operates ChatForest.*

