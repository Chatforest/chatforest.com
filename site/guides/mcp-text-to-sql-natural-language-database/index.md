# MCP and Text-to-SQL: How AI Agents Turn Natural Language into Database Queries

> A comprehensive guide to text-to-SQL via MCP — covering DBHub, XiYan-SQL, QueryWeaver, Google MCP Toolbox, Oracle AI Database, Wren AI, architecture patterns, accuracy challenges


Querying databases with natural language is one of the most practical applications of AI agents — and MCP is becoming the standard way to connect them. Instead of writing custom API integrations for each database, MCP provides a universal protocol that lets any AI agent discover schemas, generate SQL, execute queries, and return results through standardized tool calls.

The ecosystem has matured rapidly. [Google's MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) supports 21+ data sources. Oracle ships a managed MCP server with native NL2SQL via Select AI. [DBHub](https://github.com/bytebase/dbhub) provides a zero-dependency gateway for five database engines. [XiYan-SQL](https://github.com/XGenerationLab/XiYan-SQL) achieves state-of-the-art accuracy on text-to-SQL benchmarks. [QueryWeaver](https://github.com/FalkorDB/QueryWeaver) uses knowledge graphs to understand schema relationships. [Wren AI](https://github.com/Canner/WrenAI) adds a semantic layer that gives agents business context.

But text-to-SQL through MCP isn't simple. LLMs hallucinate column names, misunderstand join logic, and generate queries that look correct but return wrong results. Production deployments need validation layers, security guardrails, and human-in-the-loop checkpoints. An accuracy rate of 90% sounds impressive until you realize that means one in ten queries returns incorrect data.

This guide covers the MCP text-to-SQL landscape — the tools available, how they work, where they fail, and how to build production systems that balance automation with reliability. Our analysis draws on published documentation, benchmark results, and vendor announcements — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## How Text-to-SQL Works Through MCP

The basic flow is straightforward: an AI agent receives a natural language question, discovers the database schema through MCP tools, generates a SQL query, executes it, and returns the results. But the implementation details matter enormously.

### The Standard Architecture

```
User Question
    │
    ▼
┌─────────────────┐
│   AI Agent       │  "Show me total revenue by region last quarter"
│   (LLM)          │
└────────┬────────┘
         │ MCP tool calls
         ▼
┌─────────────────┐
│  MCP Server      │  Schema discovery → SQL generation → Execution
│  (Text-to-SQL)   │
└────────┬────────┘
         │ SQL query
         ▼
┌─────────────────┐
│   Database       │  PostgreSQL / MySQL / Snowflake / BigQuery / ...
└─────────────────┘
```

Most MCP database servers expose two core tools:

1. **Schema discovery** — `list_tables`, `describe_table`, `get_schema` — lets the agent understand what data is available, including table names, column types, relationships, and constraints.
2. **Query execution** — `run_query`, `execute_sql` — runs the generated SQL and returns results.

More sophisticated implementations add:

- **Schema search** — finding relevant tables in large schemas without loading everything into context
- **Query validation** — checking generated SQL for syntax errors, safety issues, or logical problems before execution
- **Query explanation** — describing what a SQL query does in plain English
- **Result formatting** — transforming raw query results into human-readable summaries

### Why MCP Matters for Text-to-SQL

Before MCP, every text-to-SQL tool needed its own integration for each database and each AI platform. MCP changes this in three ways:

**Universal connectivity.** A single MCP server can connect any MCP-compatible AI client (Claude, Cursor, VS Code, Codex) to any supported database. DBHub demonstrates this: one server, five database engines, any MCP client.

**Standardized schema discovery.** Instead of each tool implementing its own schema introspection, MCP provides a consistent interface. The agent calls `list_tables` and gets a predictable response regardless of whether the underlying database is PostgreSQL or Snowflake.

**Composability.** Text-to-SQL becomes one tool among many. An agent can query a database via MCP, then pass results to a visualization tool, then write a report — all through the same protocol.

## MCP Text-to-SQL Servers

### DBHub — Universal Database Gateway

[DBHub](https://github.com/bytebase/dbhub) (Bytebase) is a zero-dependency, token-efficient MCP server that acts as a universal gateway to multiple database engines. [2,550+ GitHub stars](https://github.com/bytebase/dbhub/stargazers) and [~73K monthly npm downloads](https://www.npmjs.com/package/@bytebase/dbhub) as of April 2026. Latest version: [v0.21.2](https://www.npmjs.com/package/@bytebase/dbhub) (April 2026).

**Supported databases:** PostgreSQL, MySQL, MariaDB, SQL Server, SQLite.

**Key design decisions:**

- **Minimalist tool design** — DBHub exposes three core MCP tools: `execute_sql` for query execution, `search_objects` for schema discovery, and configurable custom tools — keeping the interface lean to maximize the agent's context window.
- **Token efficiency** — Schema information is compressed and formatted to minimize token usage, which matters when working with large databases.
- **Custom tools** — You can define reusable, parameterized SQL operations in [`dbhub.toml` configuration files](https://github.com/bytebase/dbhub#custom-tools), creating domain-specific tools without code.
- **Read-only mode** — Safety controls prevent accidental data modifications.
- **Built-in web interface (Workbench)** — Visual query execution and request tracing without requiring an MCP client.

**What makes it notable:** DBHub's minimalist approach — treating the LLM as the intelligence layer and the MCP server as a thin data access layer — contrasts with more opinionated servers that embed their own SQL generation logic. This means text-to-SQL quality depends entirely on the LLM, for better or worse. The project also supports [multi-connection configuration](https://github.com/bytebase/dbhub#multi-connection) and [Docker deployment](https://github.com/bytebase/dbhub#docker).

### XiYan-SQL — State-of-the-Art Accuracy

[XiYan MCP Server](https://github.com/XGenerationLab/xiyan_mcp_server) ([232 stars](https://github.com/XGenerationLab/xiyan_mcp_server/stargazers)) takes the opposite approach from DBHub: it embeds a specialized text-to-SQL model directly in the MCP server, adding a dedicated SQL generation layer between the agent and the database.

**Performance claims** (from [XiYan-SQL benchmarks](https://github.com/XGenerationLab/XiYan-SQL)):

- State-of-the-art on open text-to-SQL benchmarks
- 2–22 percentage point improvement over generic MCP database servers (MySQL and PostgreSQL experiments)
- [44.37% success rate on BIRD-CRITIC-Open](https://bird-critic.github.io/) (multi-dialect benchmark) — top position
- [44.53% on BIRD-CRITIC-PG](https://bird-critic.github.io/) — top position
- [75.63% EX on BIRD test set](https://bird-bench.github.io/) (framework result, Dec 2024)
- [89.65% on Spider test set](https://yale-lily.github.io/spider) (framework result)

**XiYanSQL model family:** Open-sourced models at 3B, 7B, 14B, and 32B parameter sizes (QwenCoder-based), allowing local deployment without API dependencies. Latest release: 2504 series (April 2025). Available on [HuggingFace](https://huggingface.co/collections/XGenerationLab/xiyansql-models-67c9844307b49f87436808fc). The framework is [published in IEEE TKDE 2026](https://arxiv.org/abs/2507.04701).

**Architecture:** Instead of letting the general-purpose LLM generate SQL directly, the MCP server routes natural language queries through XiYan-SQL's specialized model, which has been trained specifically for SQL generation. This means the agent's LLM handles intent understanding and result interpretation, while XiYan-SQL handles the SQL generation.

**Trade-off:** Better SQL accuracy at the cost of additional model inference. You need to run or access the XiYan-SQL model alongside your agent's LLM.

### QueryWeaver — Graph-Powered Schema Understanding

[QueryWeaver](https://github.com/FalkorDB/QueryWeaver) (FalkorDB, [812 stars](https://github.com/FalkorDB/QueryWeaver/stargazers), [v0.0.14](https://github.com/FalkorDB/QueryWeaver/releases/tag/v0.0.14)) takes a fundamentally different approach: instead of feeding the LLM a flat list of tables and columns, it builds a knowledge graph that captures how schema elements relate to each other.

**How it works:**

1. QueryWeaver ingests your database schema and builds a knowledge graph using FalkorDB (a graph database)
2. The graph captures not just table/column structure but semantic relationships — what "customer" means, how it connects to "orders," what "active user" means in your business context
3. When a query arrives, QueryWeaver traverses the graph to find relevant schema elements and their relationships
4. This context is passed to the LLM for SQL generation

**Why graphs help:** Consider the question "Show me all customers who bought products made in 2023." A flat schema dump forces the LLM to figure out the join path from customers → orders → order_items → products. QueryWeaver's graph already knows this path and provides it as context, reducing hallucination and improving join accuracy.

**MCP integration:** QueryWeaver exposes an MCP-compatible interface with standardized endpoints for schema listing and query execution. It can function as an MCP server (other services call it) or as an MCP client (it calls external MCP servers for model/context services).

**Trade-off:** Requires FalkorDB as an additional dependency and an initial schema indexing step. Best suited for complex schemas where join paths and business semantics are non-obvious. Recent updates (April 2026) added [Snowflake loader support](https://github.com/FalkorDB/QueryWeaver).

### Google MCP Toolbox for Databases

[MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) (renamed from Gen AI Toolbox / genai-toolbox) is Google's open-source MCP server for database access. [14,400+ stars](https://github.com/googleapis/mcp-toolbox/stargazers). Reached [v1.0.0 on April 10, 2026](https://github.com/googleapis/mcp-toolbox/releases/tag/v1.0.0).

**Scale:** Supports [21+ data sources](https://github.com/googleapis/mcp-toolbox#supported-sources) — AlloyDB, BigQuery, Cloud SQL (PostgreSQL, MySQL, SQL Server), Spanner, Firestore, Knowledge Catalog, plus third-party databases including Snowflake, Oracle, MongoDB, Redis, Elasticsearch, CockroachDB, ClickHouse, Couchbase, Neo4j, Trino, and more.

**Key features:**

- **Managed MCP server** — Google handles deployment and scaling
- **Natural language querying** — Interact with data using plain English
- **Connection pooling** — Built-in connection management with automatic cleanup
- **Authentication integration** — Works with Google Cloud IAM
- **Java SDK** — First-class, type-safe agent orchestration for enterprise Java ecosystems (announced March 2026)
- **Agent Development Kit (ADK) integration** — Works with Google's ADK for building agent systems

**Architecture approach:** The Toolbox sits between AI applications and databases, handling connection management, authentication, and query execution. Unlike DBHub's two-tool approach, it provides richer tool surfaces tailored to each database engine's capabilities.

**Trade-off:** Strongest in the Google Cloud ecosystem. Third-party database support is available but may lack the deep integration of cloud-native sources.

### Oracle Autonomous AI Database MCP Server

Oracle ships a managed, multi-tenant MCP server as part of Oracle Autonomous AI Database (versions 26ai and 19c). Announced late 2025, with continued updates through early 2026.

**What makes it different:**

- **Native NL2SQL** — Uses Oracle's Select AI for natural language to SQL generation, integrated directly into the database engine rather than as an external layer
- **AI Profile routing** — NL2SQL Select AI tools can use different LLMs optimized for SQL quality, separate from the agent's conversational LLM
- **Deep security integration** — Respects and enforces existing database roles, lockdown profiles, access control lists, auditing, encryption, RBAC, and Virtual Private Database (VPD) policies
- **Managed multi-tenant** — Oracle handles the MCP server infrastructure; each Autonomous AI Database gets its own MCP endpoint

**Select AI integration:** Tools created using Select AI Agent are instantly accessible through the MCP Server. This means you define your NL2SQL capabilities once in the database, and they're automatically available to any MCP client — without reimplementing the text-to-SQL logic in the agent.

**Trade-off:** Tightly coupled to Oracle's ecosystem. The deep security integration is a major advantage for Oracle shops, but you're locked into Oracle's database and AI profile system.

### Wren AI — Semantic Layer for Text-to-SQL

[Wren AI](https://github.com/Canner/WrenAI) ([14,900+ stars](https://github.com/Canner/WrenAI/stargazers), [v0.29.1](https://github.com/Canner/WrenAI/releases/tag/v0.29.1)) approaches the problem from the business intelligence angle. Rather than connecting agents directly to raw database schemas, Wren AI adds a semantic layer that defines business concepts, metrics, and relationships.

**Architecture:**

- **Wren Engine** — A semantic engine built on [Apache DataFusion (Rust-based)](https://github.com/Canner/wren-engine) that embeds into MCP clients
- **Modeling Definition Language (MDL)** — A structured JSON format for defining models, metrics, relationships, and access rules
- **MCP integration** — Wren Engine serves as an MCP server, providing AI agents with business context alongside data access

**Why a semantic layer helps:**

Raw database schemas don't capture business logic. A column named `status` could mean anything. The join between `orders` and `payments` might require specific conditions. "Revenue" might mean `SUM(amount) WHERE status = 'completed'` in your business. Wren AI's MDL captures all of this, giving agents the context they need to generate correct queries.

**Key features:**

- **GenBI (Generative BI)** — Natural language queries across any database
- **Text-to-Chart** — Generate visualizations alongside SQL
- **Governance** — Access rules and audit trails built into the semantic layer
- **Multi-database** — Works with any database DataFusion can query

**Trade-off:** Requires upfront investment in defining your semantic model. The MDL must be maintained as your schema evolves. Best for organizations that want to standardize how business metrics are calculated across tools. Note: MCP integration is in the [wren-engine subcomponent](https://github.com/Canner/wren-engine) and is still evolving as of April 2026.

### Other Notable Implementations

**Synechron Text2SQL MCP** ([synechron-code/text2sql-mcp](https://github.com/synechron-code/text2sql-mcp)) — Multi-database support (PostgreSQL, MySQL, SQLite, Microsoft Fabric). Converts natural language to optimized SQL using language models. Enterprise-focused.

**SQL Server Natural Language MCP** ([aman-panjwani/mcp-sql-server-natural-lang](https://github.com/aman-panjwani/mcp-sql-server-natural-lang)) — Focused specifically on SQL Server, enabling natural language queries with structured SQL responses.

**Oracle SQLcl MCP Server** — Oracle's command-line tool (SQLcl) wrapped as an MCP server, providing AI-driven SQL capabilities including natural language to SQL conversion.

**AI2SQL MCP Integration** — Commercial text-to-SQL tool that supports MCP for connecting to PostgreSQL, MySQL, SQL Server, SQLite, Snowflake, and BigQuery. Targets non-technical users (product managers, analysts, business teams).

**Vanna** ([vanna-ai/vanna](https://github.com/vanna-ai/vanna)) — [23,200+ stars](https://github.com/vanna-ai/vanna/stargazers), but **archived and read-only as of March 29, 2026**. Vanna 2.0 was a RAG-based text-to-SQL framework using retrieval-augmented generation to pull schema snippets and documentation at runtime. Agent-based API with support for Claude and GPT models. While no longer maintained, the architecture remains influential. Last release: [v2.0.2](https://github.com/vanna-ai/vanna/releases) (February 2026).

## Comparison of Approaches

| Server | Approach | SQL Generation | Databases | Best For |
|--------|----------|---------------|-----------|----------|
| **DBHub** | Thin gateway | LLM-dependent | 5 engines | Simplicity, token efficiency |
| **XiYan-SQL** | Specialized model | Dedicated NL2SQL model | MySQL, PostgreSQL | Maximum SQL accuracy |
| **QueryWeaver** | Knowledge graph | Graph-augmented LLM | MySQL, PostgreSQL, Snowflake | Complex schemas, multi-hop joins |
| **Google Toolbox** | Managed platform | LLM-dependent | 21+ sources | Google Cloud, scale |
| **Oracle AI DB** | Native database | Select AI (in-DB) | Oracle | Enterprise Oracle, security |
| **Wren AI** | Semantic layer | Context-augmented LLM | Any (DataFusion) | BI, business metrics |

The approaches fall into three categories:

1. **Thin gateways** (DBHub, Google Toolbox) — expose schema and query tools, let the agent's LLM handle SQL generation. Simple but accuracy depends entirely on the LLM.

2. **Specialized SQL models** (XiYan-SQL, Oracle Select AI) — add a dedicated SQL generation layer trained specifically for the task. Better accuracy but more infrastructure.

3. **Context enrichment** (QueryWeaver, Wren AI) — add structured business context (knowledge graphs, semantic layers) that helps the LLM generate better SQL. Best accuracy for complex queries but requires upfront modeling.

## Accuracy: The Central Challenge

Text-to-SQL accuracy is the make-or-break factor for production deployments, and it remains the most significant unsolved problem.

### The Numbers

Current state-of-the-art on major benchmarks:

- **[Spider](https://yale-lily.github.io/spider)** (cross-database, 200+ databases) — Top models achieve ~91% execution accuracy (MiniSeek at 91.2% was the first to break 90%). Note: Spider 1.0 leaderboard was frozen in February 2024; [Spider 2.0](https://spider2-sql.github.io/) is far harder, with top models at only 6–25%.
- **[BIRD](https://bird-bench.github.io/)** (real-world databases with domain knowledge) — Top models now achieve ~82% execution accuracy (Agentar-Scale-SQL at 81.67% EX, September 2025). Human performance is 92.96%.
- **[BIRD-CRITIC](https://bird-critic.github.io/)** (multi-dialect, adversarial) — XiYan-SQL leads at ~44% success rate (44.37% Open, 44.53% PG)

These numbers tell a story: accuracy drops dramatically as queries get more complex and databases more realistic. The gap between Spider 1.0 (academic) and BIRD-CRITIC (closer to production) is enormous — from 91% down to 44%.

### Why 90% Accuracy Isn't Enough

A widely-cited analysis (["Why 90% Accuracy in Text-to-SQL is 100% Useless"](https://towardsdatascience.com/why-90-accuracy-in-text-to-sql-is-100-useless/)) argues that high aggregate accuracy masks critical failures:

- **Wrong results look like right results.** A query that returns a number — just the wrong number — is more dangerous than a query that fails with an error. Users can't verify correctness without knowing SQL.
- **Errors compound.** If you're running 10 queries to build a report, 90% per-query accuracy means only 35% chance the entire report is correct.
- **Trust erodes quickly.** One bad answer can destroy confidence in the system. Users who catch an error will question every previous result.

### Common Failure Modes

Research on production text-to-SQL systems identifies consistent failure patterns:

**Hallucinated schema elements.** LLMs invent column names that don't exist, reference tables from their training data instead of the actual schema, or guess at data types. This is especially common with large schemas where the full schema can't fit in context.

**Incorrect join logic.** Multi-table queries require understanding relationships that may not be explicit in the schema (foreign keys aren't always defined). LLMs frequently produce wrong join conditions, leading to duplicated rows, missing data, or Cartesian products.

**Aggregate function errors.** GROUP BY clauses, window functions, and conditional aggregations are frequent failure points. The query runs successfully but returns semantically wrong results — for example, counting rows instead of distinct values.

**Filter and condition mistakes.** Date range handling, NULL comparisons, LIKE patterns, and case sensitivity are common sources of subtle errors. "Last quarter" means different things depending on fiscal year definitions.

**Ambiguity resolution failures.** "Revenue" could mean gross, net, or recognized revenue. "Active users" could be daily, monthly, or by some custom definition. Without explicit business context, the LLM guesses — and often guesses wrong.

## Hallucination Mitigation Strategies

Several architectural patterns reduce hallucination and improve accuracy:

### Schema-Aware Context Windows

The most basic mitigation: ensure the LLM has the actual schema, not just table names. This means:

```
Schema context (provided to LLM):
┌─────────────────────────────────────┐
│ Table: orders                        │
│   id: INTEGER PRIMARY KEY            │
│   customer_id: INTEGER FK→customers  │
│   total_amount: DECIMAL(10,2)        │
│   status: VARCHAR(20)                │
│   created_at: TIMESTAMP              │
│                                      │
│ Table: customers                     │
│   id: INTEGER PRIMARY KEY            │
│   name: VARCHAR(100)                 │
│   region: VARCHAR(50)                │
│   created_at: TIMESTAMP              │
└─────────────────────────────────────┘
```

DBHub optimizes this by compressing schema representations for token efficiency. XiYan-SQL goes further by training models that are specifically aware of schema structure.

### Retrieval-Augmented Generation (RAG)

[Vanna AI](https://github.com/vanna-ai/vanna) pioneered this approach (note: the project was [archived in March 2026](https://github.com/vanna-ai/vanna) but the pattern remains widely used): instead of passing the entire schema to every query, use retrieval to find relevant schema elements, similar past queries, and documentation.

The RAG pipeline:
1. **Training phase** — Index your schema, example queries, and documentation
2. **Query phase** — When a question arrives, retrieve the most relevant context
3. **Generation phase** — Pass only the relevant context to the LLM for SQL generation

This helps with large schemas (hundreds of tables) where the full schema can't fit in context. The retrieval step acts as a focus mechanism, giving the LLM only what it needs.

### Knowledge Graph Augmentation

QueryWeaver's approach: model schema relationships as a graph, then traverse the graph to provide context for each query.

```
Knowledge Graph:
    customers ──has_many──▶ orders
        │                      │
        │                  has_many
        │                      ▼
    located_in           order_items
        │                      │
        ▼                  belongs_to
    regions                    ▼
                           products
                               │
                           categorized_as
                               ▼
                           categories
```

When the agent asks about "customer spending by product category," the graph provides the complete join path: customers → orders → order_items → products → categories. The LLM doesn't need to figure this out from a flat schema dump.

### Semantic Layer Validation

Wren AI's approach: define business metrics once, then validate generated SQL against the semantic model.

If "revenue" is defined as `SUM(total_amount) WHERE status IN ('completed', 'shipped')`, the semantic layer can check whether generated SQL matches this definition. Mismatches get flagged before execution.

### Multi-Agent Validation

A production pattern gaining traction: use multiple agents with different roles to validate queries:

```
Question: "What's our monthly revenue trend?"
    │
    ▼
┌──────────────┐
│ SQL Generator │  → Generates initial SQL
└──────┬───────┘
       ▼
┌──────────────┐
│ SQL Reviewer  │  → Checks for logical errors, schema mismatches
└──────┬───────┘
       ▼
┌──────────────┐
│ SQL Executor  │  → Runs query, checks for runtime errors
└──────┬───────┘
       ▼
┌──────────────┐
│ Result Checker│  → Validates results make sense (no negative counts, etc.)
└──────────────┘
```

Research on [error detection for text-to-SQL](https://arxiv.org/abs/2305.13683) found that at 95% precision, error detectors allow systems to answer 76–175% more questions correctly compared to baseline approaches. The key insight: decomposing SQL generation into specialized steps with validation checkpoints produces better results than end-to-end generation.

## Security Considerations

Text-to-SQL through MCP introduces security risks that go beyond traditional database access.

### SQL Injection via Natural Language

When an LLM generates SQL from user input, traditional SQL injection becomes prompt injection. A user who asks "Show me all users; DROP TABLE users;" is unlikely to succeed with a well-built system. But more subtle attacks — embedding SQL fragments in question context, exploiting few-shot examples, or manipulating schema descriptions — are harder to defend against.

Research has shown that backdoor attacks on fine-tuned text-to-SQL models can introduce malicious behaviors — generating SQL injection payloads that are syntactically valid and executable.

**Mitigations:**
- **Read-only connections** — DBHub's read-only mode prevents any write operations
- **Parameterized queries** — Never interpolate user input directly into SQL
- **Statement filtering** — Reject multi-statement queries, DDL commands, and system operations
- **Row-level security** — Use database-native RLS so even correct queries only return authorized data

### Schema Exposure

Schema discovery tools expose your database structure to the AI agent — and by extension, to anyone who can query the agent. Table names, column names, and relationships reveal business logic.

**Mitigations:**
- **Schema filtering** — Only expose tables and columns the agent needs
- **Column masking** — Hide sensitive columns (SSN, credit card numbers) from schema discovery
- **View-based access** — Create read-only views that expose only safe, aggregated data

### Data Exfiltration

An agent that can run arbitrary SELECT queries against a production database can potentially extract sensitive data — even with read-only access.

**Mitigations:**
- **Row limits** — Cap the number of rows returned per query
- **Column restrictions** — Prevent querying columns containing PII
- **Query audit logging** — Log every query executed through MCP for review
- **Result filtering** — Post-process results to mask sensitive values

### Oracle's Approach: Native Security Integration

Oracle's Autonomous AI Database MCP Server stands out for security because it leverages existing database security rather than adding a separate layer:

- **Role-Based Access Control (RBAC)** — MCP actions respect database roles
- **Virtual Private Database (VPD)** — Row-level filtering applies to AI-generated queries
- **Lockdown profiles** — Restrict what operations are available through MCP
- **Audit logging** — All MCP operations are captured by Oracle's audit framework

This "security is the database's job" approach is architecturally cleaner than trying to enforce security in the MCP server layer.

## Production Architecture Patterns

### Pattern 1: Direct Query — Simple and Honest

```
User → Agent → MCP Server → Database → Agent → User
```

**When to use:** Internal tools, developer workflows, ad-hoc analytics where users understand the limitations and can verify results.

**How it works:** The agent generates SQL, executes it, and returns results. No validation layer. The user is responsible for sanity-checking.

**Advantages:** Simple, fast, low infrastructure cost.

**Risks:** Hallucinated queries, wrong results presented as fact, potential data exposure.

### Pattern 2: Validated Query — Trust but Verify

```
User → Agent → SQL Generation → Validation Layer → Execution → Result Check → User
```

**When to use:** Business analytics, reporting, any context where incorrect results have consequences.

**How it works:** Generated SQL passes through validation before execution — syntax checking, schema verification, logical analysis. Results are sanity-checked (no negative counts, reasonable ranges, expected row counts).

**Validation techniques:**
- Parse the SQL AST and verify all referenced tables/columns exist
- Check that JOIN conditions use actual foreign key relationships
- Verify aggregate functions match the question's intent
- Compare result cardinality with expected ranges

**Advantages:** Catches most hallucination errors before they reach users.

**Risks:** Validation adds latency. Some errors still slip through.

### Pattern 3: Human-in-the-Loop — Show Your Work

```
User → Agent → SQL Generation → Show SQL to User → User Approves → Execution → User
```

**When to use:** Financial reporting, compliance, any context where every query must be auditable.

**How it works:** The agent generates SQL but shows it to the user before executing. The user (who may or may not know SQL) reviews and approves.

**Advantages:** Maximum safety. Full audit trail. Users learn what queries do.

**Risks:** Requires SQL literacy. Slows down the workflow. Users may rubber-stamp without reviewing.

### Pattern 4: Semantic Layer — Define Once, Query Safely

```
User → Agent → Semantic Layer (Wren AI / dbt) → Validated SQL → Execution → User
```

**When to use:** Enterprise BI, standardized reporting, anywhere "revenue" needs to mean the same thing every time.

**How it works:** Queries go through a semantic layer that translates business concepts into verified SQL patterns. The agent can compose these patterns but can't generate arbitrary SQL.

**Advantages:** Consistent definitions. No hallucination for defined metrics. Governance built in.

**Risks:** Limited to what's defined in the semantic model. New questions require model updates.

### Pattern 5: Multi-Model — Best of Both Worlds

```
User → Conversational Agent → Text-to-SQL Model → Validation Agent → Execution → User
```

**When to use:** Production systems that need both high accuracy and conversational flexibility.

**How it works:** The conversational agent (Claude, GPT) handles intent understanding and result presentation. A specialized text-to-SQL model (XiYan-SQL, fine-tuned SQLCoder) handles SQL generation. A validation agent checks the result.

Oracle's Select AI implements a version of this: the MCP agent handles conversation, while the database's built-in NL2SQL engine (potentially using a different, SQL-optimized LLM) handles query generation.

**Advantages:** Each model does what it's best at. Highest accuracy for production use.

**Risks:** More infrastructure. Higher latency. Multiple models to maintain.

## Getting Started

### For Quick Prototyping

Start with **DBHub**. Zero dependencies, supports common databases, two-tool interface means minimal setup. Install and connect:

```json
{
  "mcpServers": {
    "dbhub": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "postgresql://user:pass@localhost/mydb"]
    }
  }
}
```

Your AI agent can immediately query your database in natural language. Start with read-only mode and simple questions to understand the accuracy baseline.

### For Maximum Accuracy

Use **XiYan-SQL** if benchmark accuracy matters most. Deploy the XiYanSQL-QwenCoder model (start with 7B for testing, scale to 32B for production) and configure the MCP server to route queries through it.

Alternatively, use **QueryWeaver** if your schema has complex relationships that flat context can't capture. The knowledge graph approach helps most with multi-hop join queries.

### For Enterprise Deployment

**Oracle shops:** Use the Autonomous AI Database MCP Server. Native security integration means you don't need to reinvent access control.

**Google Cloud:** Use MCP Toolbox for Databases. 42 data sources, managed infrastructure, IAM integration.

**Multi-database environments:** Consider Wren AI's semantic layer approach. Define your business model once, query any backend through DataFusion.

### For Business Intelligence

**Wren AI** is purpose-built for this. Define your metrics, relationships, and access rules in MDL, then expose them through MCP. Agents get business context, not just raw schemas.

## What's Next for MCP Text-to-SQL

The ecosystem is moving in several directions:

**Convergence of approaches.** The boundary between thin gateways and specialized engines is blurring. DBHub is adding custom tools; specialized engines are adopting MCP. Expect more servers that combine gateway simplicity with accuracy enhancements.

**Semantic layers becoming standard.** Both dbt (semantic layer integration) and Wren AI (MDL) are pushing toward a world where agents query business concepts, not raw tables. This reduces hallucination and improves consistency.

**Multi-agent architectures.** The generate-validate-execute pattern is becoming standard for production deployments. MCP makes this natural — each step can be a different tool call.

**Streaming and real-time.** Current text-to-SQL is batch-oriented: question in, results out. The next step is connecting agents to real-time data streams — asking "what's happening now?" not just "what happened?"

**Local models getting competitive.** XiYan-SQL's open-source models (3B–32B parameters) and tools like Vanna show that accurate text-to-SQL doesn't require cloud API calls. This matters for data that can't leave the premises.

**Security hardening.** The [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/), real-world incidents ([CVE-2025-6514](https://nvd.nist.gov/vuln/detail/CVE-2025-6514) — critical RCE in mcp-remote affecting 558K+ downloads, [Supabase Cursor agent data leak](https://simonwillison.net/2025/Jul/6/supabase-mcp-lethal-trifecta/)), and growing enterprise adoption are driving better security practices. Expect more servers to follow Oracle's approach of leveraging native database security rather than adding their own.

## Further Reading

For more context on the technologies discussed in this guide:

- [Best Database MCP Servers](/guides/best-database-mcp-servers/) — comprehensive reviews of MCP servers for every major database
- [MCP Database Connection Patterns](/guides/mcp-database-connection-patterns/) — connection pooling, failover, and performance optimization
- [MCP Database Patterns](/guides/mcp-database-patterns/) — schema management, migration, and data modeling through MCP
- [MCP Data Science Workflows](/guides/mcp-data-science-workflows/) — using MCP for analytics, notebooks, and data exploration
- [MCP and Data Pipelines](/guides/mcp-data-pipelines-etl/) — connecting AI agents to Airflow, dbt, Kafka, and the modern data stack
- [MCP RAG Patterns](/guides/mcp-rag-patterns/) — retrieval-augmented generation architectures relevant to schema retrieval
- [MCP Knowledge Graphs](/guides/mcp-knowledge-graphs/) — the graph-based approaches that power tools like QueryWeaver
- [MCP Security](/guides/mcp-server-security/) — comprehensive security patterns for MCP deployments
- [MCP Attack Vectors and Defense](/guides/mcp-attack-vectors-defense/) — threat models relevant to text-to-SQL, including prompt injection
- [MCP AI Safety Guardrails](/guides/mcp-ai-safety-guardrails/) — safety patterns for production AI agent deployments

