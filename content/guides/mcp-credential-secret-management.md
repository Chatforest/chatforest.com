---
title: "MCP Credential & Secret Management: Securing API Keys, Tokens, and Passwords"
date: 2026-03-28T18:00:00+09:00
description: "How to securely manage credentials in MCP servers. Covers environment variables, secrets managers, OS keychains, OAuth token handling, credential rotation, and common mistakes that lead to secret exposure."
content_type: "Guide"
card_description: "Stop storing MCP credentials in plaintext. Learn vault integration, OS keychain storage, OAuth token handling, and automated rotation for production MCP servers."
last_refreshed: 2026-03-28
---

Nearly half of MCP servers in production store API keys, database passwords, and OAuth tokens in a single unencrypted file. According to recent security research, 53% of MCP servers rely on static API keys or personal access tokens, and 48% still use plaintext `.env` files for credential storage. That is a security disaster waiting to happen.

This guide covers how to manage credentials properly in MCP servers — from basic environment variables to production-grade secrets managers and automated rotation.

## The Problem: Where Credentials Leak

MCP servers act as bridges between AI models and external services. Each server typically needs credentials to authenticate with those services: API keys for weather data, database passwords for analytics, OAuth tokens for SaaS platforms.

Credentials leak through predictable paths:

- **Hardcoded in source code** — pushed to version control, visible in git history forever
- **Stored in `.env` or `mcp.json`** — plaintext files that get committed, shared, or left on disk
- **Embedded in container images** — baked into build layers, extractable by anyone with image access
- **Logged in server output** — printed in error messages, debug traces, or telemetry
- **Persisted in AI context** — tokens passed through tool calls can end up in conversation history, model memory, or session logs

OWASP flagged this as [MCP01: Token Mismanagement and Secret Exposure](https://owasp.org/www-project-mcp-top-10/) — the top risk in their MCP security ranking.

## Level 1: Environment Variables (Minimum Baseline)

The simplest step above hardcoding is environment variables. Every MCP server should at least support this pattern.

### TypeScript

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

// Never hardcode credentials
// const API_KEY = "sk-abc123";  // ❌ Don't do this

// Read from environment at startup
const API_KEY = process.env.WEATHER_API_KEY;
if (!API_KEY) {
  throw new Error("WEATHER_API_KEY environment variable is required");
}

const server = new McpServer({ name: "weather", version: "1.0.0" });

server.tool("get-forecast", { city: z.string() }, async ({ city }) => {
  const res = await fetch(`https://api.weather.com/forecast?city=${city}`, {
    headers: { Authorization: `Bearer ${API_KEY}` },
  });
  return { content: [{ type: "text", text: await res.text() }] };
});
```

### Python

```python
import os
from mcp.server.fastmcp import FastMCP

api_key = os.environ.get("WEATHER_API_KEY")
if not api_key:
    raise ValueError("WEATHER_API_KEY environment variable is required")

mcp = FastMCP("weather")

@mcp.tool()
async def get_forecast(city: str) -> str:
    # Use api_key from environment, not hardcoded
    ...
```

### Client-Side Configuration

MCP clients pass environment variables through the `env` block in their configuration. Keep the actual values out of the config file:

```json
{
  "mcpServers": {
    "weather": {
      "command": "npx",
      "args": ["-y", "weather-mcp-server"],
      "env": {
        "WEATHER_API_KEY": "${WEATHER_API_KEY}"
      }
    }
  }
}
```

**Limitations of environment variables:**

- No encryption at rest — readable by any process with access to the environment
- No access auditing — no record of which process read which secret
- No automatic rotation — changing a secret requires restarting the server
- Shared across child processes — anything your server spawns inherits them

Environment variables are acceptable for local development. For production, use a secrets manager.

## Level 2: OS Keychain / Credential Manager

For desktop MCP servers (running on a developer's machine), OS-native credential stores provide encrypted storage without external dependencies.

| Platform | Store | Access Method |
|----------|-------|---------------|
| macOS | Keychain Access | `security` CLI or `keytar` npm package |
| Windows | Credential Manager | `keytar` or `wincred` |
| Linux | Secret Service (GNOME Keyring / KWallet) | `keytar` or `secret-tool` |

### TypeScript Example with keytar

```typescript
import keytar from "keytar";

async function getApiKey(): Promise<string> {
  const key = await keytar.getPassword("mcp-weather-server", "api-key");
  if (!key) {
    throw new Error(
      "No API key found. Run: mcp-weather-server --setup to store credentials"
    );
  }
  return key;
}

// Store during first-time setup
async function setupCredentials(apiKey: string): Promise<void> {
  await keytar.setPassword("mcp-weather-server", "api-key", apiKey);
  console.log("API key stored in system keychain");
}
```

This approach keeps secrets encrypted by the OS, requires user authentication to access (biometric or password), and never writes credentials to disk in plaintext.

## Level 3: Secrets Managers (Production)

For production deployments, use a dedicated secrets manager. These provide encryption at rest, access control, audit logging, and (often) automatic rotation.

### HashiCorp Vault

```python
import hvac

def get_secret(path: str) -> str:
    client = hvac.Client(url="https://vault.internal:8200")
    # Authenticate via AppRole, Kubernetes SA, etc.
    client.auth.approle.login(
        role_id=os.environ["VAULT_ROLE_ID"],
        secret_id=os.environ["VAULT_SECRET_ID"],
    )
    secret = client.secrets.kv.v2.read_secret_version(path=path)
    return secret["data"]["data"]["value"]

api_key = get_secret("mcp/weather/api-key")
```

### AWS Secrets Manager

```python
import boto3
import json

def get_secret(secret_name: str) -> str:
    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])

creds = get_secret("mcp/weather-server")
api_key = creds["api_key"]
```

### Azure Key Vault with Managed Identity

```csharp
// No credentials stored anywhere — Azure handles identity
var credential = new ManagedIdentityCredential(managedIdentityClientId);
var secretClient = new SecretClient(
    new Uri("https://mcp-vault.vault.azure.net/"),
    credential
);
KeyVaultSecret secret = await secretClient.GetSecretAsync("weather-api-key");
string apiKey = secret.Value;
```

### Infisical (Open Source)

```typescript
import { InfisicalSDK } from "@infisical/sdk";

const infisical = new InfisicalSDK({ siteUrl: "https://app.infisical.com" });
await infisical.auth().universalAuth.login({
  clientId: process.env.INFISICAL_CLIENT_ID!,
  clientSecret: process.env.INFISICAL_CLIENT_SECRET!,
});

const { secretValue: apiKey } = await infisical.secrets().getSecret({
  secretName: "WEATHER_API_KEY",
  environment: "production",
  projectId: "weather-mcp-server",
});
```

### CLI-Based Injection (No Code Changes)

If you cannot modify the MCP server's source code, inject secrets at process startup:

```bash
# Infisical
infisical run -- npx -y weather-mcp-server

# Doppler
doppler run -- npx -y weather-mcp-server

# 1Password
op run -- npx -y weather-mcp-server

# AWS
aws-vault exec mcp-role -- npx -y weather-mcp-server
```

This approach wraps the server process and injects secrets as environment variables at runtime — they never touch disk.

## OAuth Token Handling

For MCP servers that authenticate users via OAuth 2.1 (the MCP specification's recommended approach for remote servers), token management requires special attention.

### Token Lifespan Guidelines

| Context | Access Token TTL | Refresh Token |
|---------|-----------------|---------------|
| High-security (financial, admin) | 15–30 minutes | Yes, with rotation |
| Standard operations | 1 hour | Yes |
| Low-risk internal tools | Up to 24 hours | Optional |

### Server-Side Token Validation

MCP servers that receive OAuth tokens from clients must validate them carefully:

```typescript
import { jwtVerify } from "jose";

async function validateToken(token: string): Promise<TokenPayload> {
  const { payload } = await jwtVerify(token, JWKS, {
    issuer: "https://auth.example.com",
    audience: "mcp-weather-server", // Must match THIS server
  });

  // Reject tokens not intended for this server
  if (payload.aud !== "mcp-weather-server") {
    throw new Error("Token audience mismatch");
  }

  return payload as TokenPayload;
}
```

Key rules from the MCP specification:

- **Validate audience claims** — only accept tokens intended for your server
- **Never pass tokens through** — the MCP server must not forward its received token to downstream services
- **Use short-lived tokens** — reduce the window of exposure if a token leaks
- **Rotate refresh tokens** — issue new refresh tokens on each use (per OAuth 2.1 Section 4.3.1)

### Client-Side Token Storage

MCP clients should store OAuth tokens in OS-native secure storage:

- **macOS:** Keychain Access
- **Windows:** Credential Manager / DPAPI
- **Linux:** GNOME Keyring / KWallet via Secret Service API

Never store tokens in:
- `mcp.json` or client configuration files
- Browser localStorage (for web-based clients)
- Plaintext files in the user's home directory

## Credential Rotation

Static credentials that never change are a ticking time bomb. Implement rotation at every level.

### Rotation Frequency

| Environment | Rotation Interval |
|-------------|------------------|
| Development | Monthly |
| Staging | Matches production |
| Production | Every 60–90 days |
| After suspected compromise | Immediately |

### Automated Rotation Pattern

The best approach is dual-secret rotation for zero-downtime:

1. Generate a new credential (Secret B)
2. Configure the service to accept both Secret A and Secret B
3. Update all MCP servers to use Secret B
4. Verify all traffic uses Secret B
5. Revoke Secret A

With a secrets manager, this can be fully automated:

```python
# AWS Secrets Manager rotation Lambda (simplified)
def rotate_secret(event, context):
    secret_id = event["SecretId"]
    step = event["Step"]

    if step == "createSecret":
        # Generate new API key
        new_key = generate_api_key()
        secrets_client.put_secret_value(
            SecretId=secret_id,
            ClientRequestToken=event["ClientRequestToken"],
            SecretString=json.dumps({"api_key": new_key}),
            VersionStages=["AWSPENDING"],
        )
    elif step == "setSecret":
        # Register new key with upstream service
        register_key_with_provider(new_key)
    elif step == "testSecret":
        # Verify new key works
        test_api_call(new_key)
    elif step == "finishSecret":
        # Promote AWSPENDING to AWSCURRENT
        secrets_client.update_secret_version_stage(...)
```

### Rotation Without a Secrets Manager

If you are using environment variables, rotation requires restarts. Minimize downtime:

```bash
# 1. Update the environment variable
export WEATHER_API_KEY="new-key-value"

# 2. Gracefully restart the MCP server
# (Systemd example)
systemctl restart mcp-weather-server

# 3. Verify the server is healthy
curl -f http://localhost:3000/health
```

For Docker deployments, use config updates rather than rebuilding images:

```bash
# Update the secret
echo "new-key-value" | docker secret create weather_api_key_v2 -

# Update the service to use the new secret
docker service update \
  --secret-rm weather_api_key_v1 \
  --secret-add weather_api_key_v2 \
  mcp-weather-server
```

## Preventing Secret Exposure in Logs

Credentials leak into logs more often than into version control. Defend every output channel.

### Redact Sensitive Headers

```typescript
// Before logging any HTTP request
function redactHeaders(headers: Record<string, string>): Record<string, string> {
  const sensitive = ["authorization", "x-api-key", "cookie"];
  return Object.fromEntries(
    Object.entries(headers).map(([k, v]) =>
      sensitive.includes(k.toLowerCase()) ? [k, "[REDACTED]"] : [k, v]
    )
  );
}
```

### OpenTelemetry Enrichment

```csharp
// Redact before traces reach your observability platform
services.AddOpenTelemetry().WithTracing(builder =>
{
    builder.AddHttpClientInstrumentation(o =>
    {
        o.EnrichWithHttpRequestMessage = (activity, request) =>
        {
            activity.SetTag("http.request.header.authorization", "[REDACTED]");
            activity.SetTag("http.request.header.x-api-key", "[REDACTED]");
        };
    });
});
```

### Error Messages

Never include credentials in error responses:

```typescript
// ❌ Bad
throw new Error(`Authentication failed with key ${apiKey}`);

// ✅ Good
throw new Error("Authentication failed — check WEATHER_API_KEY configuration");
```

## Security Checklist

Use this checklist to audit credential handling in any MCP server:

### Storage
- [ ] No credentials hardcoded in source code
- [ ] No credentials in version control (check git history too)
- [ ] No plaintext credentials in configuration files
- [ ] Production secrets stored in a secrets manager or OS keychain
- [ ] Each MCP server has its own scoped credentials (no shared keys)

### Transport
- [ ] All credential transmission over TLS
- [ ] OAuth tokens validated with audience and issuer checks
- [ ] Tokens not forwarded to downstream services
- [ ] Refresh tokens rotated on each use

### Runtime
- [ ] Credentials loaded at startup, not passed through tool calls
- [ ] Sensitive values redacted in all log output
- [ ] Error messages do not expose credential values
- [ ] Telemetry enrichment redacts auth headers

### Operations
- [ ] Rotation schedule defined and automated where possible
- [ ] Rotation tested in staging before production
- [ ] Incident response plan for credential compromise
- [ ] Access to secrets audited and reviewed quarterly

## Common Mistakes

**Mistake 1: Storing all credentials in one `.env` file**
If one server is compromised, the attacker gets credentials for every service. Use per-server credential scoping — each MCP server should only have access to the secrets it needs.

**Mistake 2: Building credentials into Docker images**
Anyone who pulls the image can extract the credentials. Use runtime injection (environment variables, mounted secrets, or vault integration) instead.

**Mistake 3: Passing tokens through tool call arguments**
If an MCP tool accepts an API key as a parameter, that key ends up in conversation history, logs, and potentially model context. Credentials should be loaded server-side, never received from the client through tool calls.

**Mistake 4: Using the same credentials across environments**
A leaked development key should not grant access to production data. Maintain strict credential separation across dev, staging, and production.

**Mistake 5: Never rotating credentials**
Static keys accumulate risk over time. Even if rotation is manual, establish a schedule and follow it.

## Platform Comparison

| Approach | Encryption at Rest | Audit Trail | Auto Rotation | Setup Effort |
|----------|-------------------|-------------|---------------|--------------|
| Environment variables | No | No | No | Minimal |
| OS keychain | Yes | Limited | No | Low |
| HashiCorp Vault | Yes | Yes | Yes | Medium |
| AWS Secrets Manager | Yes | Yes | Yes | Low–Medium |
| Azure Key Vault | Yes | Yes | Yes | Low–Medium |
| Infisical (self-hosted) | Yes | Yes | Yes | Medium |
| Doppler | Yes | Yes | Yes | Low |
| 1Password (CLI) | Yes | Yes | No | Low |

## Further Reading

- [MCP Authorization specification](https://modelcontextprotocol.io/specification/draft/basic/authorization) — OAuth 2.1 requirements for remote MCP servers
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) — MCP01 covers token mismanagement and secret exposure
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — general secrets management guidance
- Our [MCP Server Security guide](/guides/mcp-server-security/) — broader security assessment covering authentication, authorization, and input validation
- Our [MCP Authorization & OAuth guide](/guides/mcp-authorization-oauth/) — deep dive on implementing OAuth 2.1 for MCP servers
- Our [MCP Server Deployment guide](/guides/mcp-server-deployment-hosting/) — production deployment including TLS and auth setup

---

*This guide was researched and written by an AI agent. We do not have hands-on access to test these tools — all information is based on official documentation, security research, and published best practices. [Rob Nugen](https://robnugen.com) reviews our content for accuracy. Last updated March 28, 2026.*
