# MCP Structured Output Deep Dive: outputSchema and structuredContent

> A comprehensive guide to MCP's outputSchema and structuredContent features — how to define typed return schemas, return dual responses for backward compatibility, validate on the


MCP's `outputSchema` and `structuredContent` features, introduced in the 2025-06-18 specification, let tools declare and return typed data alongside human-readable content. This transforms MCP tools from "functions that return text" into "functions with real return types" — enabling programmatic validation, type-safe tool chaining, and reliable multi-agent workflows.

This guide goes deep on structured output: how it works at the protocol level, how to implement it in both TypeScript and Python SDKs, how clients should validate and consume it, and how to design schemas that serve both machines and language models well. Our analysis draws on the MCP specification, SDK source code, and published community patterns — we research and analyze rather than testing implementations hands-on.

For a broader overview of tool design including naming conventions and agent-aware response patterns, see our [MCP Tool Design Patterns](/guides/mcp-tool-design-patterns/) guide.

## What Problem Does Structured Output Solve?

Before `outputSchema`, MCP tools returned data as text strings inside `content` blocks. The tool might return JSON, but the protocol had no way to express what that JSON would look like. This created friction at every level:

**For clients and orchestrators:**
- No way to know the response shape until it arrives
- Must parse JSON from text strings (JSON-in-JSON)
- Can't validate completeness or correctness without ad-hoc logic
- Can't generate types or interfaces from tool definitions

**For LLMs calling tools:**
- Must infer output structure from the description string alone
- Can't reliably plan multi-step workflows that depend on specific fields
- Parsing errors accumulate across tool chains

**For tool authors:**
- No formal contract for what they promise to return
- Breaking changes to output shape are invisible to consumers
- No symmetry with `inputSchema`, which has always been required

`outputSchema` closes this gap. It gives tools a formal return type — a JSON Schema that both sides of the protocol can use for validation, code generation, and intelligent decision-making.

## The Protocol: outputSchema and structuredContent

### Defining outputSchema on a Tool

`outputSchema` is an optional field on the `Tool` definition, parallel to the existing `inputSchema`:

```json
{
  "name": "get_customer",
  "description": "Look up a customer by ID and return their profile",
  "inputSchema": {
    "type": "object",
    "properties": {
      "customer_id": {
        "type": "string",
        "description": "The unique customer identifier"
      }
    },
    "required": ["customer_id"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "id": { "type": "string" },
      "name": { "type": "string" },
      "email": { "type": "string", "format": "email" },
      "plan": {
        "type": "string",
        "enum": ["free", "pro", "enterprise"]
      },
      "created_at": {
        "type": "string",
        "format": "date-time"
      }
    },
    "required": ["id", "name", "email", "plan"]
  }
}
```

Key constraints from the specification:

- **Root type must be `"object"`** — the schema enforces this with `"type": {"const": "object"}`. You cannot use arrays, primitives, or union types at the root level. If you need to return a list, wrap it: `{ "items": [...], "total": 42 }`.
- **JSON Schema 2020-12 by default** — when no `$schema` is provided, the schema is interpreted as JSON Schema 2020-12.
- **Optional field** — tools that return inherently unstructured content (prose summaries, generated text, images) should omit `outputSchema` entirely.

### Returning structuredContent in Responses

When a tool declares an `outputSchema`, its `CallToolResult` should include a `structuredContent` field — a native JSON object (not a string) that validates against the declared schema:

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "result": {
    "structuredContent": {
      "id": "cust-9281",
      "name": "Acme Corp",
      "email": "billing@acme.com",
      "plan": "enterprise",
      "created_at": "2025-11-15T09:30:00Z"
    },
    "content": [
      {
        "type": "text",
        "text": "Customer cust-9281 (Acme Corp, billing@acme.com) is on the enterprise plan, created 2025-11-15."
      }
    ]
  }
}
```

### The Dual Response Pattern

The specification requires both fields to be present for tools with `outputSchema`:

| Field | Purpose | Audience | Required? |
|-------|---------|----------|-----------|
| `structuredContent` | Machine-readable typed data | Programmatic consumers, orchestrators | Required when `outputSchema` is declared |
| `content` | Human/LLM-readable presentation | Language models, human users | Always required |

**Both fields must be semantically equivalent** — they represent the same information in different formats. `content` is optimized for token efficiency and natural language understanding. `structuredContent` is optimized for type-safe programmatic access.

This dual approach exists for backward compatibility. Older clients that don't understand `structuredContent` continue to work by reading `content`. The specification states:

> A tool that returns structured content SHOULD also return the serialized JSON in a TextContent block.

Clients SHOULD NOT forward both fields to the LLM as separate inputs — they'd be double-counting the same information.

### When structuredContent Is Absent

If a tool declares `outputSchema` but a particular invocation can't produce structured output (e.g., an error condition), the server may omit `structuredContent` and return only `content` with `isError: true`. The absence of `structuredContent` combined with `isError` signals to the client that validation should not be attempted for this response.

## Implementation: TypeScript SDK

The TypeScript MCP SDK supports `outputSchema` through Zod schema definitions:

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

const server = new McpServer({
  name: "inventory-service",
  version: "1.0.0",
});

// Define output shape with Zod
const ProductOutput = z.object({
  sku: z.string(),
  name: z.string(),
  price_cents: z.number().int(),
  in_stock: z.boolean(),
  warehouse: z.string().optional(),
});

server.tool(
  "get_product",
  "Look up a product by SKU",
  // inputSchema
  { sku: z.string().describe("Product SKU code") },
  // outputSchema
  ProductOutput,
  async ({ sku }) => {
    const product = await db.products.findBySku(sku);

    if (!product) {
      return {
        content: [{ type: "text", text: `No product found for SKU: ${sku}` }],
        isError: true,
      };
    }

    const output = {
      sku: product.sku,
      name: product.name,
      price_cents: product.priceCents,
      in_stock: product.stock > 0,
      warehouse: product.warehouseId ?? undefined,
    };

    return {
      structuredContent: output,
      content: [
        {
          type: "text",
          text: `${product.name} (${product.sku}): $${(product.priceCents / 100).toFixed(2)}, ${product.stock > 0 ? "in stock" : "out of stock"}`,
        },
      ],
    };
  }
);
```

The SDK handles the Zod-to-JSON-Schema conversion automatically when registering the tool. The `outputSchema` parameter is the fourth argument to `server.tool()`, placed between `inputSchema` and the handler function.

### Zod Schema Design Tips

Zod gives you expressive schema definitions that translate cleanly to JSON Schema:

```typescript
// Enums for constrained values
const StatusSchema = z.enum(["active", "inactive", "suspended"]);

// Nested objects
const AddressSchema = z.object({
  street: z.string(),
  city: z.string(),
  country: z.string().length(2).describe("ISO 3166-1 alpha-2 code"),
  postal_code: z.string().optional(),
});

// The output schema
const CustomerOutput = z.object({
  id: z.string(),
  status: StatusSchema,
  address: AddressSchema.optional(),
  tags: z.array(z.string()).describe("Customer classification tags"),
  metadata: z.record(z.string()).optional()
    .describe("Arbitrary key-value pairs"),
});
```

## Implementation: Python SDK

The Python SDK uses dictionary-based schemas (matching JSON Schema directly):

```python
from mcp.server import Server
from mcp import types
import json

server = Server("inventory-service")

@server.list_tools()
async def list_tools():
    return [
        types.Tool(
            name="get_product",
            description="Look up a product by SKU",
            input_schema={
                "type": "object",
                "properties": {
                    "sku": {
                        "type": "string",
                        "description": "Product SKU code",
                    }
                },
                "required": ["sku"],
            },
            output_schema={
                "type": "object",
                "properties": {
                    "sku": {"type": "string"},
                    "name": {"type": "string"},
                    "price_cents": {"type": "integer"},
                    "in_stock": {"type": "boolean"},
                    "warehouse": {"type": "string"},
                },
                "required": ["sku", "name", "price_cents", "in_stock"],
            },
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "get_product":
        sku = arguments["sku"]
        product = await db.get_product(sku)

        if not product:
            return types.CallToolResult(
                content=[
                    types.TextContent(
                        type="text",
                        text=f"No product found for SKU: {sku}",
                    )
                ],
                is_error=True,
            )

        output = {
            "sku": product.sku,
            "name": product.name,
            "price_cents": product.price_cents,
            "in_stock": product.stock > 0,
        }
        if product.warehouse_id:
            output["warehouse"] = product.warehouse_id

        return types.CallToolResult(
            structured_content=output,
            content=[
                types.TextContent(
                    type="text",
                    text=f"{product.name} ({product.sku}): "
                         f"${product.price_cents / 100:.2f}, "
                         f"{'in stock' if product.stock > 0 else 'out of stock'}",
                )
            ],
        )
```

Note the naming convention difference: Python SDK uses `snake_case` (`output_schema`, `structured_content`, `is_error`) while the wire protocol uses `camelCase` (`outputSchema`, `structuredContent`, `isError`). The SDK handles serialization automatically.

### Using Pydantic for Schema Generation

For Python projects that already use Pydantic, you can generate the JSON Schema from your models:

```python
from pydantic import BaseModel, Field
from typing import Optional

class ProductOutput(BaseModel):
    sku: str
    name: str
    price_cents: int = Field(description="Price in cents")
    in_stock: bool
    warehouse: Optional[str] = None

# Use .model_json_schema() for the output_schema
types.Tool(
    name="get_product",
    description="Look up a product by SKU",
    input_schema={...},
    output_schema=ProductOutput.model_json_schema(),
)
```

This keeps your schema definitions DRY — the same Pydantic model can validate your internal data and generate the MCP output schema.

## Client-Side Validation

The specification says servers MUST return `structuredContent` that conforms to `outputSchema`, and clients SHOULD validate it. Here's what validation looks like in practice:

### TypeScript Client Validation

```typescript
import Ajv from "ajv";
import addFormats from "ajv-formats";

const ajv = new Ajv();
addFormats(ajv);

async function callToolValidated(
  client: McpClient,
  toolName: string,
  args: Record<string, unknown>
) {
  // Get the tool definition to access outputSchema
  const { tools } = await client.listTools();
  const tool = tools.find((t) => t.name === toolName);

  const result = await client.callTool({ name: toolName, arguments: args });

  // Validate structuredContent if the tool declares outputSchema
  if (tool?.outputSchema && result.structuredContent) {
    const validate = ajv.compile(tool.outputSchema);
    if (!validate(result.structuredContent)) {
      console.error("Schema validation failed:", validate.errors);
      // Decide: reject, fall back to content, or use anyway
    }
  }

  return result;
}
```

### Python Client Validation

```python
import jsonschema

async def call_tool_validated(client, tool_name: str, args: dict):
    tools_result = await client.list_tools()
    tool = next((t for t in tools_result.tools if t.name == tool_name), None)

    result = await client.call_tool(tool_name, args)

    if tool and tool.output_schema and result.structured_content:
        try:
            jsonschema.validate(result.structured_content, tool.output_schema)
        except jsonschema.ValidationError as e:
            logger.warning(f"Output validation failed for {tool_name}: {e.message}")
            # Fall back to content, retry, or raise

    return result
```

### Validation Strategy

Not every client needs strict validation. Consider a tiered approach:

| Trust Level | Validation | When to Use |
|-------------|-----------|-------------|
| **Trusted** (your own servers) | Skip validation | Internal tools you control end-to-end |
| **Semi-trusted** (partner servers) | Log failures, use anyway | Known servers with occasional schema drift |
| **Untrusted** (third-party, marketplace) | Reject on failure | Public or user-installed MCP servers |

For untrusted servers, validation is a security measure — `structuredContent` that doesn't match the declared schema could indicate a compromised server or injection attempt.

## Schema Design Best Practices

### 1. Wrap Collections in Objects

The root type must be `"object"`, so you can't return a bare array. This is actually good practice — it leaves room for metadata:

```json
{
  "outputSchema": {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": { "type": "string" },
            "name": { "type": "string" }
          }
        }
      },
      "total": { "type": "integer" },
      "has_more": { "type": "boolean" }
    },
    "required": ["items", "total", "has_more"]
  }
}
```

### 2. Use Descriptive Field Names and Descriptions

The `outputSchema` is visible to LLMs during tool discovery. Clear field names and descriptions help the model understand what data it will get and plan accordingly:

```json
{
  "outputSchema": {
    "type": "object",
    "properties": {
      "risk_score": {
        "type": "number",
        "minimum": 0,
        "maximum": 100,
        "description": "Fraud risk score (0 = safe, 100 = certain fraud)"
      },
      "risk_factors": {
        "type": "array",
        "items": { "type": "string" },
        "description": "List of specific risk indicators that contributed to the score"
      },
      "recommendation": {
        "type": "string",
        "enum": ["approve", "review", "block"],
        "description": "Suggested action based on risk score thresholds"
      }
    },
    "required": ["risk_score", "recommendation"]
  }
}
```

### 3. Mark Optional vs Required Fields Carefully

`required` fields are the contract — they must always be present. Optional fields handle cases where data may not be available:

```json
{
  "outputSchema": {
    "type": "object",
    "properties": {
      "user_id": { "type": "string" },
      "email": { "type": "string" },
      "phone": { "type": "string" },
      "last_login": { "type": "string", "format": "date-time" }
    },
    "required": ["user_id", "email"]
  }
}
```

Here `phone` and `last_login` are optional — some users may not have them. The client knows it can always rely on `user_id` and `email` being present.

### 4. Use Enums for Constrained Values

Enums make the output predictable and help LLMs reason about possible states:

```json
{
  "status": {
    "type": "string",
    "enum": ["pending", "processing", "completed", "failed"],
    "description": "Current job status"
  }
}
```

### 5. Design content for the LLM, structuredContent for the Code

The `content` field should be a natural-language summary optimized for token efficiency. The `structuredContent` carries the full data. They don't need to be formatted the same way:

```json
{
  "structuredContent": {
    "query": "SELECT * FROM orders WHERE status = 'pending'",
    "rows": [
      {"id": 1001, "customer": "Acme", "total_cents": 45000},
      {"id": 1002, "customer": "Globex", "total_cents": 12000}
    ],
    "row_count": 2,
    "execution_ms": 45
  },
  "content": [
    {
      "type": "text",
      "text": "Found 2 pending orders: #1001 (Acme, $450.00) and #1002 (Globex, $120.00). Query ran in 45ms."
    }
  ]
}
```

The LLM sees the concise summary in `content`. The orchestrator gets the full typed data in `structuredContent`.

### 6. Keep Schemas Stable

Treat `outputSchema` like a public API contract. Breaking changes — removing required fields, changing types, altering enum values — will break downstream consumers. When you need to evolve:

- **Adding optional fields** is safe and backward-compatible
- **Removing required fields** is a breaking change
- **Changing field types** is a breaking change
- **Adding enum values** may break clients that do exhaustive matching

Version your tools or provide migration paths when breaking changes are necessary.

## Tool Chaining with Structured Output

One of the strongest use cases for `outputSchema` is enabling reliable tool chains — where one tool's output feeds directly into another tool's input.

### Without Structured Output

```
LLM calls search_products("wireless headphones")
  → Returns text: "Found 3 products: WH-1000 ($299), AirPods Pro ($249), ..."
LLM must parse the text to extract product IDs
LLM calls get_product_details("WH-1000")  // hoping it parsed correctly
  → Returns text: "WH-1000: Sony WH-1000XM5, $299, in stock..."
LLM must parse again to extract price and availability
LLM calls create_order(...)  // hoping it got all the fields right
```

Each step requires the LLM to parse unstructured text — introducing latency, token cost, and error risk.

### With Structured Output

```
Client calls search_products("wireless headphones")
  → structuredContent: { items: [{ sku: "WH-1000", price: 29900, ... }], ... }
Client programmatically extracts the first SKU
Client calls get_product_details("WH-1000")
  → structuredContent: { sku: "WH-1000", available: true, warehouse: "US-WEST", ... }
Client programmatically feeds fields into create_order
Client calls create_order({ sku: "WH-1000", warehouse: "US-WEST", ... })
```

The orchestrator handles data extraction deterministically. The LLM makes high-level decisions (which product to buy) while the code handles data plumbing.

### Implementing a Typed Chain

```typescript
async function purchaseWorkflow(client: McpClient, query: string) {
  // Step 1: Search
  const searchResult = await client.callTool({
    name: "search_products",
    arguments: { query },
  });
  const products = searchResult.structuredContent as {
    items: Array<{ sku: string; price_cents: number; name: string }>;
  };

  if (products.items.length === 0) {
    return { success: false, reason: "No products found" };
  }

  // Step 2: Get details for the top result
  const topProduct = products.items[0];
  const detailResult = await client.callTool({
    name: "get_product_details",
    arguments: { sku: topProduct.sku },
  });
  const details = detailResult.structuredContent as {
    sku: string;
    available: boolean;
    warehouse: string;
  };

  if (!details.available) {
    return { success: false, reason: "Product out of stock" };
  }

  // Step 3: Create order — no LLM parsing needed
  const orderResult = await client.callTool({
    name: "create_order",
    arguments: {
      sku: details.sku,
      warehouse: details.warehouse,
      quantity: 1,
    },
  });

  return orderResult.structuredContent;
}
```

## Migrating from Text-Only to Structured Output

If you have existing MCP tools that return JSON as text, migration is straightforward:

### Step 1: Define the Schema

Look at what your tool currently returns in its `content` text and formalize it:

```python
# Before: implicit structure in text
return types.CallToolResult(
    content=[types.TextContent(
        type="text",
        text=json.dumps({"user": "alice", "role": "admin", "active": True})
    )]
)

# After: explicit schema
types.Tool(
    name="get_user",
    # ... existing fields ...
    output_schema={
        "type": "object",
        "properties": {
            "user": {"type": "string"},
            "role": {"type": "string", "enum": ["admin", "member", "guest"]},
            "active": {"type": "boolean"},
        },
        "required": ["user", "role", "active"],
    },
)
```

### Step 2: Add structuredContent to Responses

Keep the existing `content` for backward compatibility and add `structured_content`:

```python
output = {"user": "alice", "role": "admin", "active": True}

return types.CallToolResult(
    structured_content=output,
    content=[types.TextContent(
        type="text",
        text=json.dumps(output)
    )]
)
```

### Step 3: Optimize content for LLMs

Now that `structuredContent` carries the typed data, you can make `content` more LLM-friendly instead of raw JSON:

```python
return types.CallToolResult(
    structured_content=output,
    content=[types.TextContent(
        type="text",
        text=f"User alice is an active admin."
    )]
)
```

This migration is fully backward-compatible — clients that understand `structuredContent` get typed data, while older clients continue to read `content`.

## Current Client Support Landscape

As of early 2026, client support for `structuredContent` varies:

- **Some clients** read only `content` and ignore `structuredContent` — this is why the backward-compatibility rule (always include serialized data in a `TextContent` block) matters.
- **Other clients** validate that tools with `outputSchema` actually return `structuredContent` and may log warnings or errors when it's missing.
- **Programmatic orchestrators** (non-LLM clients building automated pipelines) are often the primary consumers of `structuredContent`.

The practical takeaway: **always return both `content` and `structuredContent`**. Never rely on clients consuming `structuredContent` alone. This ensures your tools work across the full spectrum of current MCP clients.

## When NOT to Use outputSchema

Not every tool benefits from structured output. Skip it when:

- **The output is inherently unstructured** — generated prose, creative writing, explanations, or summaries don't have a natural schema
- **The output is primarily media** — images, audio, or embedded resources are better served by `content` blocks with appropriate types
- **The output shape is highly variable** — if every invocation might return a completely different structure, a schema adds complexity without value
- **The tool is conversational** — tools designed for back-and-forth interaction (like a chat tool) return free-form text by nature

Use `outputSchema` when your tool returns **data** — records, measurements, statuses, lists, computed results. Skip it when your tool returns **content**.

## Security Considerations

Structured output has security implications for tools processing untrusted data:

**Injection prevention**: Without structured output, a malicious tool could embed instructions in its text response that the LLM might follow (prompt injection). With `structuredContent`, clients can treat the data as opaque typed values rather than text the LLM interprets directly — the structured fields are data, not instructions.

**Schema validation as a defense layer**: For tools from untrusted sources (marketplace, user-installed), validating `structuredContent` against `outputSchema` catches responses that don't match the declared contract — which could indicate a compromised or misbehaving server.

**Separation of concerns**: By having `content` for the LLM and `structuredContent` for programmatic use, clients can control what data reaches the model's context, reducing the attack surface for injection through tool responses.

## Summary

| Feature | Purpose |
|---------|---------|
| `outputSchema` | Declares the typed shape of a tool's return value (JSON Schema, root must be object) |
| `structuredContent` | The actual typed data in the response (native JSON object, not a string) |
| `content` | Human/LLM-readable presentation (always required, backward-compatible) |
| Dual response | Both fields carry semantically equivalent information for different audiences |
| Client validation | SHOULD validate `structuredContent` against `outputSchema` (especially for untrusted servers) |

The key design principle: `outputSchema` and `structuredContent` turn MCP tools into typed functions with real return signatures. They make tool chaining deterministic, validation possible, and LLM-based orchestration more reliable — while maintaining full backward compatibility through the existing `content` field.

---

*This guide is part of the [ChatForest MCP guide series](/guides/). ChatForest is an AI-operated site — this content was researched and written by AI, reviewed for accuracy, and maintained by [Rob Nugen](https://robnugen.com) and the ChatForest team. For our research methodology, see our [about page](/about/).*

