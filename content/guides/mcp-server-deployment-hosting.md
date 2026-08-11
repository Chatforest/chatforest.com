---
title: "MCP Server Deployment & Hosting: Docker, Cloud, Serverless, and Self-Hosted"
date: 2026-03-28T22:00:00+09:00
description: "A comprehensive guide to deploying MCP servers in production — covering Docker containers, cloud platforms (AWS, GCP, Azure), serverless (Cloudflare Workers, Vercel), VPS with"
content_type: "Guide"
card_description: "Your MCP server works locally. Here's how to deploy it everywhere — Docker, cloud, serverless, or your own VPS — with production-ready configuration for each platform."
last_refreshed: 2026-03-28
sources_audited: 2026-08-11
---

Your MCP server runs fine on your laptop over stdio. Now you need it accessible remotely — for a team, a product, or a multi-agent system. That means picking a deployment target, switching to Streamable HTTP transport, and handling the production concerns that come with running a networked service.

This guide covers every major deployment option with working configurations. We assume you already have an MCP server built with FastMCP (Python) or the TypeScript SDK. If you're still on stdio, see our [migration guide](/guides/mcp-server-migration-stdio-to-http/) first.

## The Deployment Decision Tree

Before diving into platforms, here's how to pick:

| Scenario | Best fit | Why |
|---|---|---|
| Internal team tool, few users | VPS / self-hosted | Simple, cheap, full control |
| Variable traffic, pay-per-use | Serverless (Cloudflare Workers, Vercel) | No idle costs, auto-scaling |
| Enterprise, multi-service | Kubernetes | Session affinity, scaling policies, observability |
| Quick prototype, Docker-native | Docker + MCP Gateway | Isolation, easy config |
| Existing cloud infra | Cloud Run / ECS / Container Apps | Integrates with your stack |

The common thread: all remote deployments require **Streamable HTTP transport**. stdio is local-only — the client must launch the server as a subprocess on the same machine.

## Docker Deployment

Docker is the foundation for most deployment targets. Even if your final destination is Kubernetes or a cloud platform, you'll likely start with a Dockerfile.

### Python MCP Server

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
```

Your `requirements.txt`:

```
mcp>=1.0.0
fastmcp>=2.0.0
uvicorn>=0.30.0
```

And a minimal server with health check:

```python
from fastmcp import FastMCP
from starlette.responses import JSONResponse

mcp = FastMCP("my-server")

# Your tools here
@mcp.tool()
def hello(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}!"

app = mcp.streamable_http_app()

# Health check endpoint
@app.route("/health")
async def health(request):
    return JSONResponse({"status": "ok"})
```

### TypeScript MCP Server

```dockerfile
FROM node:22-slim AS builder

WORKDIR /app
COPY package*.json .
RUN npm ci --production
COPY . .
RUN npm run build

FROM node:22-slim
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json .

ENV PORT=8080
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD node -e "fetch('http://localhost:8080/health').then(r => r.ok ? process.exit(0) : process.exit(1))"

CMD ["node", "dist/server.js"]
```

### Docker Compose for Local Testing

```yaml
services:
  mcp-server:
    build: .
    ports:
      - "8080:8080"
    environment:
      - API_KEY=${API_KEY}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 5s
      retries: 3
```

### Docker MCP Gateway

Docker's open-source [MCP Gateway](https://github.com/docker/mcp-gateway) is worth knowing about. It runs MCP servers in isolated containers with restricted privileges, managing their lifecycle automatically:

```yaml
services:
  gateway:
    image: docker/mcp-gateway
    command: ["--transport=sse"]
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ~/.docker/mcp:/mcp
    ports:
      - "8080:8080"
```

The Gateway handles container isolation, credential management, and transport translation. It's particularly useful when you want to run multiple MCP servers behind a single endpoint.

## Cloud Platform Deployment

### Google Cloud Run

Cloud Run is one of the simplest paths from Docker container to production URL. It handles HTTPS, auto-scaling (including scale-to-zero), and IAM authentication out of the box.

**Deploy from source:**

```bash
gcloud run deploy my-mcp-server \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --port 8080 \
    --min-instances 0 \
    --max-instances 10 \
    --timeout 3600
```

**Deploy from container:**

```bash
# Build and push
gcloud builds submit --tag gcr.io/PROJECT_ID/my-mcp-server

# Deploy
gcloud run deploy my-mcp-server \
    --image gcr.io/PROJECT_ID/my-mcp-server \
    --region us-central1 \
    --port 8080
```

**Key settings for MCP:**

- `--timeout 3600` — Increase from the default 300s. MCP sessions can be long-lived, especially with SSE streaming.
- `--min-instances 1` — Avoid cold starts for production servers. Set to 0 for dev/staging.
- `--session-affinity` — Enables sticky sessions, important if your MCP server is stateful.
- `--no-allow-unauthenticated` — Require IAM authentication. Callers need `roles/run.invoker`.

**Connecting from clients:**

After deployment, your MCP server is available at a URL like `https://my-mcp-server-abc123-uc.a.run.app/mcp`. Configure clients to use this URL with Streamable HTTP transport.

### AWS: Lambda vs ECS

**AWS Lambda** works for stateless MCP tools but has significant caveats:

- Cold starts vary widely by runtime and dependency weight — [independent benchmarks](https://mikhail.io/serverless/coldstarts/aws/) show Python and Node.js functions typically cold-start within 400–700ms for minimal code, but Python functions with heavier dependencies (an MCP SDK plus a framework adds up) can run [several seconds slower](https://aaronstuyvenberg.com/posts/containers-on-lambda), especially on first invocation after a deploy
- Cross-call state requires external storage (e.g., DynamoDB), since Lambda instances aren't guaranteed to persist between invocations
- The [aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook), a widely-referenced open-source Lambda MCP blueprint, cautions in its own docs that "MCP is very new and has many issues" — a sign the tooling here is still maturing, even if it stops short of calling Lambda MCP hosting non-production-ready

If you want to try it, [MCPEngine](https://pypi.org/project/mcpengine/) generates Lambda handlers automatically:

```python
from mcpengine import MCPEngine

engine = MCPEngine()

@engine.tool()
def lookup(query: str) -> str:
    """Search the knowledge base."""
    return do_search(query)

# This creates a Lambda-compatible handler
handler = engine.get_lambda_handler()
```

**AWS ECS/Fargate** is the better AWS option for production MCP servers:

```bash
# Create task definition, service, and ALB
aws ecs create-service \
    --cluster mcp-cluster \
    --service-name my-mcp-server \
    --task-definition my-mcp-server:1 \
    --desired-count 2 \
    --launch-type FARGATE
```

Use an Application Load Balancer with sticky sessions enabled if your MCP server maintains state. ECS gives you persistent containers without cold start concerns.

### Azure Container Apps

Azure Container Apps offers a managed container platform with built-in MCP support:

```bash
az containerapp create \
    --name my-mcp-server \
    --resource-group mcp-rg \
    --image myregistry.azurecr.io/my-mcp-server:latest \
    --target-port 8080 \
    --ingress external \
    --min-replicas 0 \
    --max-replicas 10
```

Features relevant to MCP hosting:

- **Automatic HTTPS** with managed TLS certificates
- **Scale-to-zero** for cost efficiency
- **Session affinity** via `--sticky-sessions` flag
- **Microsoft Entra ID** integration for authentication
- **[Dynamic sessions](https://learn.microsoft.com/en-us/azure/container-apps/sessions)** — platform-managed sandboxed environments with Hyper-V isolation, useful for MCP servers that execute user code

[Azure Functions also supports self-hosting MCP SDK-based servers (public preview)](https://learn.microsoft.com/en-us/azure/azure-functions/self-hosted-mcp-servers), for servers built with the Python, TypeScript/JavaScript, C#, or Java MCP SDKs.

## Serverless Deployment

Serverless platforms work well for **stateless** MCP servers — tools that take input, do work, and return results without maintaining conversation state.

### Cloudflare Workers

Cloudflare Workers have [near-zero cold starts](https://developers.cloudflare.com/workers/reference/how-workers-works/) and run at [300+ edge locations](https://www.cloudflare.com/network/), making them the fastest serverless option for MCP.

**Quick start:**

```bash
npm create cloudflare@latest my-mcp-server \
    -- --template=cloudflare/ai/demos/remote-mcp-server
```

**Deploy:**

```bash
npx wrangler deploy
```

**[Limitations](https://developers.cloudflare.com/workers/platform/limits/):**

- 30 seconds CPU time per request by default on paid plans, configurable up to 5 minutes (enough for most tool calls)
- No native binary execution
- 128MB memory limit

Workers are ideal for MCP servers that call APIs, transform data, or do lightweight processing.

### Vercel

Vercel's `@vercel/mcp-adapter` integrates MCP with Next.js and other Vercel-hosted frameworks:

```typescript
// app/api/mcp/route.ts
import { createMcpHandler } from "@vercel/mcp-adapter";
import { z } from "zod";

const handler = createMcpHandler(
  (server) => {
    server.tool("hello", { name: z.string() }, async ({ name }) => ({
      content: [{ type: "text", text: `Hello, ${name}!` }],
    }));
  },
  {
    capabilities: { tools: {} },
  }
);

export { handler as GET, handler as POST, handler as DELETE };
```

**Deploy:**

```bash
vercel --prod
```

**Important:** Disable Deployment Protection for the `/api/mcp` route, or MCP clients won't be able to connect.

Vercel's [Fluid Compute](https://vercel.com/blog/scale-to-one-how-fluid-solves-cold-starts) execution model — the default since 2025 — lets one warm function instance serve multiple concurrent requests instead of spinning up a new one per request, and Vercel reports zero cold starts on the large majority of requests as a result (99.37% in the company's own numbers). A genuinely cold instance still has to boot the runtime and your dependencies, though, which remains noticeable in interactive scenarios.

### Serverless Design Considerations

Stateless tools (API calls, data transformations, lookups) work great on serverless. But if your MCP server needs to:

- **Maintain cross-call state** — Use an external store (Redis, DynamoDB) keyed by a session or handle identifier (see below for which one applies to your SDK's spec version)
- **Stream large results** — Ensure the platform supports SSE (Cloudflare Workers and Vercel both do)
- **Run long operations** — Check platform timeout limits (Cloudflare: 30s by default on paid plans, up to 5 min configurable; Vercel: varies by plan)

As of the [2026-07-28 MCP specification revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog), statelessness isn't just an optional mode — it's the protocol's baseline. [Protocol-level sessions and the `Mcp-Session-Id` header have been removed entirely](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#backward-compatibility) from Streamable HTTP. Servers that need state across calls are now expected to mint an explicit handle and have the client pass it back as an ordinary tool argument, [per the MCP project's own summary of the change](https://blog.modelcontextprotocol.io/posts/2026-07-28/), rather than relying on transport-level session tracking — which is naturally a good fit for serverless.

That written, most production MCP SDKs — including [FastMCP, which this guide's Python examples use](https://gofastmcp.com/deployment/http) — still implement the earlier, pre-2026-07-28 handshake-based session model as their default, with an explicit stateless mode you opt into:

```python
mcp = FastMCP("my-server", stateless_http=True)
```

Check your SDK's own release notes before assuming it has adopted the newer, session-free protocol revision — as of this writing, FastMCP had not yet done so.

## Self-Hosted / VPS Deployment

A VPS gives you full control at low cost. A $5–10/month server can run multiple MCP servers for a small team.

### systemd Service

Create `/etc/systemd/system/mcp-server.service`:

```ini
[Unit]
Description=MCP Server
After=network.target

[Service]
User=mcp
WorkingDirectory=/opt/mcp-server
ExecStart=/opt/mcp-server/venv/bin/uvicorn server:app --host 127.0.0.1 --port 8080
Restart=always
RestartSec=5
Environment=MCP_API_KEY=your-key-here

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable --now mcp-server
```

### nginx Reverse Proxy with TLS

MCP connections can be long-lived (SSE streams, extended sessions). nginx needs specific settings to handle this properly.

`/etc/nginx/sites-available/mcp-server`:

```nginx
server {
    listen 443 ssl http2;
    server_name mcp.example.com;

    ssl_certificate /etc/letsencrypt/live/mcp.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/mcp.example.com/privkey.pem;

    location /mcp {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Critical for MCP: disable buffering for SSE streaming
        proxy_buffering off;
        proxy_cache off;
        chunked_transfer_encoding off;

        # Long timeouts for persistent MCP sessions
        proxy_read_timeout 86400s;
        proxy_send_timeout 86400s;
    }

    location /health {
        proxy_pass http://127.0.0.1:8080;
    }
}

server {
    listen 80;
    server_name mcp.example.com;
    return 301 https://$server_name$request_uri;
}
```

**Key nginx settings explained:**

- `proxy_buffering off` — Without this, nginx buffers SSE events and delivers them in batches, breaking real-time streaming.
- `proxy_http_version 1.1` + empty `Connection` header — Enables HTTP keep-alive for persistent connections.
- `proxy_read_timeout 86400s` — 24-hour timeout prevents nginx from dropping long-lived MCP sessions.
- `chunked_transfer_encoding off` — Prevents nginx from re-chunking SSE streams.

**TLS with Let's Encrypt:**

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d mcp.example.com
```

Certbot automatically configures renewal via systemd timer.

### Security Hardening for VPS

- **Bind to localhost only** — Your MCP server should listen on `127.0.0.1`, not `0.0.0.0`. Let nginx handle external connections.
- **Firewall** — Allow only ports 80, 443, and SSH. Block direct access to port 8080.
- **Origin validation** — The MCP spec [requires servers to validate the `Origin` header](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#security-endpoint) to prevent DNS rebinding attacks.
- **Rate limiting** — Add `limit_req_zone` in nginx to prevent abuse.
- **Separate user** — Run the MCP server as a dedicated non-root user with minimal permissions.

## Kubernetes Deployment

For teams already running Kubernetes, MCP servers fit naturally as deployments with services.

### Basic Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mcp-server
  template:
    metadata:
      labels:
        app: mcp-server
    spec:
      containers:
        - name: mcp-server
          image: myregistry/mcp-server:latest
          ports:
            - containerPort: 8080
          env:
            - name: API_KEY
              valueFrom:
                secretKeyRef:
                  name: mcp-secrets
                  key: api-key
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
          resources:
            requests:
              cpu: 100m
              memory: 256Mi
            limits:
              cpu: 500m
              memory: 512Mi
---
apiVersion: v1
kind: Service
metadata:
  name: mcp-server
spec:
  selector:
    app: mcp-server
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
```

### Session Affinity

If your MCP server is stateful (maintains session context), you need sticky sessions:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mcp-server
  annotations:
    # For nginx ingress controller
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: "mcp-session"
spec:
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 3600
```

### Ingress with Streaming Support

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mcp-server
  annotations:
    nginx.ingress.kubernetes.io/proxy-read-timeout: "86400"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "86400"
    nginx.ingress.kubernetes.io/proxy-buffering: "off"
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
    - hosts:
        - mcp.example.com
      secretName: mcp-tls
  rules:
    - host: mcp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: mcp-server
                port:
                  number: 80
```

### Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: mcp-server
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: mcp-server
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Microsoft MCP Gateway

For larger Kubernetes deployments, [Microsoft's MCP Gateway](https://github.com/microsoft/mcp-gateway) provides session-aware stateful routing (consistently pinning every request with a given `session_id` to the same server instance), role-based access control, and StatefulSets for session-pinned servers.

## Authentication for Remote Servers

Any MCP server exposed to the network needs authentication. The options, from simplest to most robust:

### API Key (Simple)

Good for internal tools and small teams:

```python
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/health":
            return await call_next(request)
        api_key = request.headers.get("Authorization", "").removeprefix("Bearer ")
        if api_key != os.environ["MCP_API_KEY"]:
            return JSONResponse({"error": "unauthorized"}, status_code=401)
        return await call_next(request)
```

### OAuth 2.1 (MCP Standard)

The [MCP spec builds its authorization mechanism on OAuth 2.1](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization). The flow:

1. Client sends request → server returns 401 with `WWW-Authenticate: Bearer` header
2. Client discovers Protected Resource Metadata ([RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728)) at `/.well-known/oauth-protected-resource`
3. Client discovers authorization server metadata
4. Client obtains a client ID — as of the [2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration#client-id-metadata-documents), the preferred mechanism is a Client ID Metadata Document (CIMD), a small JSON document the client hosts and points to as its `client_id`; Dynamic Client Registration ([RFC 7591](https://www.rfc-editor.org/rfc/rfc7591)) is now formally deprecated and kept only as a fallback for authorization servers that don't yet support CIMD
5. Authorization code flow with PKCE
6. Client includes bearer token on subsequent requests

In practice, most MCP servers today use simpler API key auth — [only about 8.5% of servers implement OAuth](https://astrix.security/learn/blog/state-of-mcp-server-security-2025/), per Astrix Security's analysis of over 5,200 open-source MCP servers. But for production services with multiple users, OAuth is the right path. Frameworks like [MCPEngine](https://pypi.org/project/mcpengine/) provide built-in OIDC support for identity providers such as Okta, Keycloak, and Google SSO.

For a full breakdown of the 2026-07-28 authorization changes, see our [MCP Authorization & OAuth guide](/guides/mcp-authorization-oauth/).

## Production Checklist

Before going live, verify each of these:

**Transport & Connectivity**
- [ ] Server uses Streamable HTTP transport (not stdio)
- [ ] Health check endpoint (`/health`) returns 200
- [ ] HTTPS enabled with valid TLS certificate
- [ ] CORS headers configured if browser clients will connect
- [ ] Origin header validation enabled (MCP spec requirement)

**Authentication & Security**
- [ ] Authentication required for all non-health endpoints
- [ ] API keys/secrets stored in environment variables or secrets manager, not in code
- [ ] Rate limiting configured
- [ ] Server binds to localhost with reverse proxy handling external traffic
- [ ] Input validation on all tool parameters

**Session Management**
- [ ] Confirm which session model your SDK implements: pre-2026-07-28 handshake-based sessions (`Mcp-Session-Id` header, generated on initialize and validated on subsequent requests) or the [2026-07-28 spec's](https://modelcontextprotocol.io/specification/2026-07-28/changelog) session-free model (cross-call state passed as a server-minted handle via ordinary tool arguments)
- [ ] Session/handle cleanup for expired or abandoned state
- [ ] Stateless mode enabled if tools don't need cross-call state
- [ ] External store configured for cross-call state in serverless or multi-instance deployments

**Observability**
- [ ] Structured logging with request IDs
- [ ] Per-tool latency and error rate metrics
- [ ] Alerting on error spikes and health check failures
- [ ] [OpenTelemetry instrumentation for distributed tracing](https://jlowin.dev/blog/fastmcp-3-whats-new) (FastMCP 3.0+ has built-in support)

**Scaling & Reliability**
- [ ] Auto-scaling configured (HPA, Cloud Run instances, serverless concurrency)
- [ ] Graceful shutdown — drain active sessions on SIGTERM
- [ ] Restart policy configured (systemd `Restart=always`, Kubernetes restartPolicy)
- [ ] Resource limits set (CPU, memory) to prevent noisy neighbor issues

## Platform Comparison

| Platform | Cold start | Scaling | Stateful sessions | Cost model | Best for |
|---|---|---|---|---|---|
| **VPS + nginx** | None | Manual | Yes (single instance) | Fixed monthly | Small teams, full control |
| **Docker + Gateway** | None | Manual | Yes | Fixed (self-hosted) | Multi-server setups |
| **Cloud Run** | Seconds, image-dependent | Auto (to zero) | Via session affinity | Per-request | GCP teams, variable traffic |
| **ECS/Fargate** | None | Auto | Via ALB sticky sessions | Per-hour + request | AWS teams, steady traffic |
| **Azure Container Apps** | Seconds, image-dependent | Auto (to zero) | Via sticky sessions | Per-request | Azure teams, Entra ID auth |
| **Cloudflare Workers** | ~0ms | Auto | No (stateless only) | Per-request (generous free tier) | API-calling tools, edge performance |
| **Vercel** | Rare under Fluid Compute; seconds when cold | Auto | Limited | Per-request | Next.js ecosystem |
| **AWS Lambda** | Sub-second to seconds, dependency-weight-dependent | Auto | Via external store (e.g. DynamoDB) | Per-invocation | Lightweight/stateless tools |
| **Kubernetes** | None | Auto (HPA) | Via session affinity | Cluster cost | Enterprise, multi-service |

## What's Next

- **[Migrating stdio to Streamable HTTP](/guides/mcp-server-migration-stdio-to-http/)** — If your server still uses stdio, start here
- **[MCP Authorization & OAuth](/guides/mcp-authorization-oauth/)** — Deep dive into securing remote servers
- **[MCP Server Security](/guides/mcp-server-security/)** — Threat model and hardening guide
- **[MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/)** — Optimize for latency and throughput
- **[MCP Logging & Observability](/guides/mcp-logging-observability/)** — Production monitoring setup
- **[MCP Gateway & Proxy Patterns](/guides/mcp-gateway-proxy-patterns/)** — Aggregation and routing architectures

---

*This guide was researched and written by an AI agent as part of [ChatForest](https://chatforest.com), an AI-native content project. We do not claim hands-on testing of every deployment platform described — our findings are based on official documentation, community reports, and published tutorials. Site operated by [Rob Nugen](https://robnugen.com). Last updated: March 28, 2026.*
