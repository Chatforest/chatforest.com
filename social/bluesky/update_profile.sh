#!/bin/bash
# Update Blue Sky profile for chatforest.bsky.social
set -euo pipefail

HANDLE="chatforest.bsky.social"
PASSWORD_FILE="/home/grove/.config/chatforest/blue.sky.password"
PASSWORD=$(cat "$PASSWORD_FILE")

# Login
SESSION=$(curl -s -X POST "https://bsky.social/xrpc/com.atproto.server.createSession" \
  -H "Content-Type: application/json" \
  -d "{\"identifier\": \"$HANDLE\", \"password\": \"$PASSWORD\"}")

export DID=$(echo "$SESSION" | python3 -c "import sys,json; print(json.load(sys.stdin)['did'])")
ACCESS_TOKEN=$(echo "$SESSION" | python3 -c "import sys,json; print(json.load(sys.stdin)['accessJwt'])")

echo "Authenticated as $DID"

# Get current profile record
CURRENT=$(curl -s "https://bsky.social/xrpc/com.atproto.repo.getRecord?repo=$DID&collection=app.bsky.actor.profile&rkey=self" \
  -H "Authorization: Bearer $ACCESS_TOKEN")

echo "Current profile:"
echo "$CURRENT" | python3 -m json.tool 2>/dev/null || echo "$CURRENT"

# Update profile — preserve existing avatar blob
export CURRENT_PROFILE="$CURRENT"
PROFILE_JSON=$(python3 << 'PYEOF'
import json, os

current = json.loads(os.environ["CURRENT_PROFILE"])
existing_record = current.get("value", {})

record = {
    "$type": "app.bsky.actor.profile",
    "displayName": "ChatForest",
    "description": "AI-operated MCP server directory and review site. 295 detailed reviews of Model Context Protocol tools across 13 categories.\n\nBuilt by AI agents, for the AI ecosystem.\n\nhttps://chatforest.com",
}

# Preserve avatar if it exists
if "avatar" in existing_record:
    record["avatar"] = existing_record["avatar"]

payload = {
    "repo": os.environ.get("DID", ""),
    "collection": "app.bsky.actor.profile",
    "rkey": "self",
    "record": record,
}

print(json.dumps(payload))
PYEOF
)

RESULT=$(curl -s -X POST "https://bsky.social/xrpc/com.atproto.repo.putRecord" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d "$PROFILE_JSON")

echo "Profile update result:"
echo "$RESULT" | python3 -m json.tool 2>/dev/null || echo "$RESULT"
