# How to Build Your First MCP Server

> A step-by-step tutorial for building an MCP server in Python. From zero to a working server with tools, resources, and Claude Desktop integration.


You've read about [what MCP is](/guides/what-is-mcp/). Now let's build something. By the end of this guide, you'll have a working MCP server that exposes custom tools to Claude Desktop, VS Code, Cursor, or Claude Code. We'll use Python because the SDK is clean and the code is readable — but the concepts apply to TypeScript too.

## What You'll Build

A weather lookup server. It won't call a real weather API (that would require API keys and distract from the MCP concepts), but it will demonstrate everything you need:

- **Tools** — functions Claude can call
- **Tool annotations** — metadata hints that help clients handle your tools intelligently
- **Input validation** — typed parameters with descriptions
- **Error handling** — what happens when things go wrong
- **Client integration** — connecting your server to Claude Desktop, VS Code, Cursor, or Claude Code

The server is intentionally simple. The point isn't the weather data — it's understanding the pattern so you can wrap *your* API, database, or service.

## Prerequisites

- Python 3.10 or newer
- `uv` (recommended) or `pip` for package management
- A client to test with — Claude Desktop, VS Code (Copilot), Cursor, or Claude Code

## Step 1: Set Up the Project

Create a new directory and install the MCP Python SDK with CLI tools:

```bash
mkdir weather-mcp && cd weather-mcp
uv init
uv add "mcp[cli]"
```

If you're using pip instead of uv:

```bash
mkdir weather-mcp && cd weather-mcp
python -m venv .venv
source .venv/bin/activate
pip install "mcp[cli]"
```

The `[cli]` extra gives you the `mcp` command-line tool — you'll use it to test, inspect, and install your server.

## Step 2: Write the Server

Create `server.py`:

```python
from mcp.server.fastmcp import FastMCP

# Create the server
mcp = FastMCP("weather")

# Sample weather data (in a real server, this would call an API)
WEATHER_DATA = {
    "london": {"temp_c": 12, "condition": "Cloudy", "humidity": 78},
    "tokyo": {"temp_c": 22, "condition": "Clear", "humidity": 45},
    "new york": {"temp_c": 18, "condition": "Partly cloudy", "humidity": 62},
    "sydney": {"temp_c": 26, "condition": "Sunny", "humidity": 55},
    "paris": {"temp_c": 14, "condition": "Rainy", "humidity": 85},
}


@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: The city name (e.g., "London", "Tokyo")
    """
    city_lower = city.lower().strip()
    data = WEATHER_DATA.get(city_lower)

    if not data:
        available = ", ".join(WEATHER_DATA.keys())
        return f"No weather data for '{city}'. Available cities: {available}"

    return (
        f"Weather in {city.title()}:\n"
        f"  Temperature: {data['temp_c']}°C\n"
        f"  Condition: {data['condition']}\n"
        f"  Humidity: {data['humidity']}%"
    )


@mcp.tool()
def list_cities() -> str:
    """List all cities with available weather data."""
    return "Available cities: " + ", ".join(
        name.title() for name in WEATHER_DATA
    )


if __name__ == "__main__":
    mcp.run()
```

That's the whole server. Let's break down what's happening:

- `FastMCP("weather")` creates a server named "weather." The name shows up in client UIs.
- `@mcp.tool()` registers a function as an MCP tool. The SDK reads the function signature and docstring to generate the tool's schema automatically.
- The type hints (`city: str`) become the tool's input schema. The docstring becomes the tool's description — this is what the AI model reads to decide when and how to use the tool.
- `mcp.run()` starts the server and handles the JSON-RPC protocol over stdio.

## Step 3: Test It Locally

The `mcp` CLI (included when you installed `mcp[cli]`) makes testing easy. Run your server in dev mode:

```bash
mcp dev server.py
```

This launches the MCP Inspector — a browser-based UI at `localhost:6274` where you can see your tools, call them with test inputs, and inspect the JSON-RPC messages. It's invaluable during development. The dev server watches for file changes and reloads automatically.

You can also verify the server runs standalone:

```bash
# With uv:
uv run python server.py

# With pip/venv:
python server.py
```

The server will start and wait for JSON-RPC messages on stdin. It won't print anything visible — that's normal. Press `Ctrl+C` to stop it.

**Alternative:** If you prefer the Inspector directly (or are building a TypeScript server), you can still use:

```bash
npx @modelcontextprotocol/inspector uv run python server.py
```

## Step 4: Connect to a Client

You've built and tested your server. Now connect it to a real AI client. Pick whichever you use.

### Option A: Claude Desktop (quickest)

The `mcp` CLI can register your server automatically:

```bash
mcp install server.py --name "weather"
```

This writes the config entry for you. Restart Claude Desktop — you should see the hammer icon in the chat input. Click it to verify your `get_weather` and `list_cities` tools appear.

**Manual setup:** If you prefer to edit the config file yourself, open:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Add your server. If using uv:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": ["run", "--directory", "/full/path/to/weather-mcp", "python", "server.py"]
    }
  }
}
```

If using a venv with pip:

```json
{
  "mcpServers": {
    "weather": {
      "command": "/full/path/to/weather-mcp/.venv/bin/python",
      "args": ["/full/path/to/weather-mcp/server.py"]
    }
  }
}
```

Restart Claude Desktop and look for the hammer icon.

### Option B: VS Code (Copilot)

VS Code has built-in MCP support since version 1.116. Create `.vscode/mcp.json` in your project:

```json
{
  "servers": {
    "weather": {
      "command": "uv",
      "args": ["run", "--directory", "/full/path/to/weather-mcp", "python", "server.py"]
    }
  }
}
```

**Important:** VS Code uses `"servers"` as the top-level key, not `"mcpServers"` — this is the most common copy-paste mistake.

### Option C: Cursor

Cursor uses the same format as Claude Desktop. Add to your Cursor MCP config:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": ["run", "--directory", "/full/path/to/weather-mcp", "python", "server.py"]
    }
  }
}
```

### Option D: Claude Code

In your terminal:

```bash
claude mcp add weather -- uv run --directory /full/path/to/weather-mcp python server.py
```

Use `--scope project` to share the config with your team (writes to `.mcp.json`), or `--scope user` for all your projects.

### Try it

Whichever client you chose, try asking: "What's the weather like in Tokyo?" The AI will call your tool and incorporate the result.

## Step 5: Add a Resource

Tools are functions the model *calls*. Resources are data the model can *read*. Let's add a resource that exposes a weather summary:

```python
@mcp.resource("weather://summary")
def weather_summary() -> str:
    """A summary of weather across all available cities."""
    lines = []
    for city, data in WEATHER_DATA.items():
        lines.append(f"{city.title()}: {data['temp_c']}°C, {data['condition']}")
    return "\n".join(lines)
```

Add this to your `server.py` before the `if __name__` block. Resources are identified by URIs (here, `weather://summary`). Clients can read them without the model needing to make a tool call — useful for context that should be available upfront.

## Step 6: Add Tool Annotations

Tool annotations are metadata hints that tell clients how your tools behave. They help clients make UX decisions — like auto-approving read-only tools or requiring confirmation for destructive ones.

```python
@mcp.tool(
    annotations={
        "title": "Get Weather",
        "readOnlyHint": True,
        "openWorldHint": False,
    }
)
def get_weather(city: str) -> str:
    ...
```

The available annotations:

| Annotation | Default | Meaning |
|---|---|---|
| `title` | — | Human-readable display name |
| `readOnlyHint` | `False` | Tool doesn't modify anything |
| `destructiveHint` | `True` | Tool may perform destructive updates |
| `idempotentHint` | `False` | Repeated calls with same args have no additional effect |
| `openWorldHint` | `True` | Tool interacts with external entities |

Our weather tools are read-only and don't touch external systems, so `readOnlyHint=True` and `openWorldHint=False` are appropriate. A tool that deletes records would leave `destructiveHint=True` (the default).

Annotations are hints, not security guarantees — clients decide how to use them.

## Step 7: Handle Errors Gracefully

When wrapping real APIs, things fail. Here's the pattern:

```python
@mcp.tool(
    annotations={
        "title": "Get Forecast",
        "readOnlyHint": True,
        "openWorldHint": False,
    }
)
def get_forecast(city: str, days: int = 3) -> str:
    """Get a weather forecast for a city.

    Args:
        city: The city name
        days: Number of days to forecast (1-7, default 3)
    """
    if days < 1 or days > 7:
        return "Error: days must be between 1 and 7"

    city_lower = city.lower().strip()
    if city_lower not in WEATHER_DATA:
        available = ", ".join(WEATHER_DATA.keys())
        return f"No data for '{city}'. Available: {available}"

    # In a real server, you'd call a forecast API here
    data = WEATHER_DATA[city_lower]
    return f"{days}-day forecast for {city.title()}: {data['condition']}, ~{data['temp_c']}°C"
```

Key principle: **return error messages as strings, don't raise exceptions.** The model can read and react to a string error. An unhandled exception crashes the tool call and gives the model nothing useful to work with.

## The Complete Server

Here's the full `server.py` with everything we've built:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

WEATHER_DATA = {
    "london": {"temp_c": 12, "condition": "Cloudy", "humidity": 78},
    "tokyo": {"temp_c": 22, "condition": "Clear", "humidity": 45},
    "new york": {"temp_c": 18, "condition": "Partly cloudy", "humidity": 62},
    "sydney": {"temp_c": 26, "condition": "Sunny", "humidity": 55},
    "paris": {"temp_c": 14, "condition": "Rainy", "humidity": 85},
}


@mcp.tool(
    annotations={
        "title": "Get Weather",
        "readOnlyHint": True,
        "openWorldHint": False,
    }
)
def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: The city name (e.g., "London", "Tokyo")
    """
    city_lower = city.lower().strip()
    data = WEATHER_DATA.get(city_lower)

    if not data:
        available = ", ".join(WEATHER_DATA.keys())
        return f"No weather data for '{city}'. Available cities: {available}"

    return (
        f"Weather in {city.title()}:\n"
        f"  Temperature: {data['temp_c']}°C\n"
        f"  Condition: {data['condition']}\n"
        f"  Humidity: {data['humidity']}%"
    )


@mcp.tool(
    annotations={
        "title": "List Cities",
        "readOnlyHint": True,
        "openWorldHint": False,
    }
)
def list_cities() -> str:
    """List all cities with available weather data."""
    return "Available cities: " + ", ".join(
        name.title() for name in WEATHER_DATA
    )


@mcp.tool(
    annotations={
        "title": "Get Forecast",
        "readOnlyHint": True,
        "openWorldHint": False,
    }
)
def get_forecast(city: str, days: int = 3) -> str:
    """Get a weather forecast for a city.

    Args:
        city: The city name
        days: Number of days to forecast (1-7, default 3)
    """
    if days < 1 or days > 7:
        return "Error: days must be between 1 and 7"

    city_lower = city.lower().strip()
    if city_lower not in WEATHER_DATA:
        available = ", ".join(WEATHER_DATA.keys())
        return f"No data for '{city}'. Available: {available}"

    data = WEATHER_DATA[city_lower]
    return f"{days}-day forecast for {city.title()}: {data['condition']}, ~{data['temp_c']}°C"


@mcp.resource("weather://summary")
def weather_summary() -> str:
    """A summary of weather across all available cities."""
    lines = []
    for city, data in WEATHER_DATA.items():
        lines.append(f"{city.title()}: {data['temp_c']}°C, {data['condition']}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
```

## Where to Go from Here

You now know the pattern. Every MCP server follows the same shape:

1. Create a `FastMCP` instance
2. Decorate functions with `@mcp.tool()` or `@mcp.resource()`
3. Call `mcp.run()`

What changes is what's inside the functions. Some ideas for your next server:

- **Database query server** — expose read-only SQL queries as tools
- **Internal API wrapper** — let AI agents interact with your company's services
- **File processor** — parse CSVs, transform data, generate reports
- **Notification server** — send Slack messages, create Jira tickets, trigger webhooks

### Features We Didn't Cover

The MCP Python SDK (v1.27.0 as of April 2026, pin to `mcp>=1.25,<2` — V2 is coming) has more capabilities for when you're ready:

- **Prompts** (`@mcp.prompt()`) — reusable prompt templates that clients can discover and use
- **Context object** — accept a `Context` parameter in your tools for logging (`ctx.info()`, `ctx.debug()`), progress reporting (`ctx.report_progress()`), and requesting user input via elicitation (`ctx.elicit()`)
- **Structured output** — return Pydantic models, TypedDicts, or dataclasses from tools and the SDK auto-generates an output schema. Clients get validated JSON instead of free-form text
- **Streamable HTTP transport** — call `mcp.run(transport="streamable-http")` to serve your MCP server over HTTP instead of stdio. This is the standard for remote/production deployments (SSE transport is deprecated — don't use it for new projects)
- **Elicitation** — your tools can request information from the user through the client, in two modes: structured forms (for non-sensitive data) and URL redirects (for auth flows and payments)
- **Sampling** — your server can ask the client's LLM to generate text, enabling agentic loops within a single tool call
- **Tasks** — for long-running operations, return a task handle immediately and let the client poll for results

The [official MCP docs](https://modelcontextprotocol.io) are the best reference once you've got the basics down.

Build something, publish it to GitHub, and let us know — we might [review it](/reviews/).

**Already built a server?** Read our [MCP Server Setup Guide](/guides/mcp-server-setup-guide/) for detailed configuration across Claude Desktop, VS Code, Cursor, Claude Code, Windsurf, ChatGPT, and JetBrains IDEs.

## What Changed (April 2026)

| Change | Details |
|---|---|
| `mcp dev` replaces manual Inspector | Python SDK now includes `mcp dev server.py` for one-command testing with browser UI |
| `mcp install` for Claude Desktop | Auto-registers your server — no manual JSON editing needed |
| 7 clients covered | Added VS Code (Copilot), Cursor, and Claude Code setup instructions |
| Tool annotations | New section — `readOnlyHint`, `destructiveHint`, etc. help clients handle tools intelligently |
| Install command updated | Now `mcp[cli]` to include CLI tools (`mcp dev`, `mcp install`, `mcp run`) |
| "Where to Go" expanded | Added Context object, structured output, Streamable HTTP, elicitation, sampling, tasks |
| SSE deprecated | Streamable HTTP is now the standard for remote servers; SSE should not be used for new projects |
| Version pinning advice | Pin to `mcp>=1.25,<2` — V2 is in development with breaking API changes |

