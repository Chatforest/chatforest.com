#\!/bin/bash
# ChatForest autonomous runner v3.1
# Called by cron every 1 minute
# Mode file (~/.grove_mode) controls frequency: "slow" (default), "wild", or "stop"
# Touch ~/.grove_once to trigger a single immediate run regardless of mode
# Session management moved to bash (v3.1) — Claude crashes can't orphan timers

export PATH="$HOME/.local/bin:$HOME/.pyenv/versions/3.11.15/bin:$PATH"
WORKDIR="$HOME/chatforest.com"
LOGFILE="$WORKDIR/RUNLOG.md"
LOCKFILE="$WORKDIR/.grove_lock"
MODEFILE="$HOME/.grove_mode"
ONCEFILE="$HOME/.grove_once"
LAST_RUN="$WORKDIR/.last_run"
JIKAN_KEY="$(cat $HOME/.config/chatforest/jikan_api_key 2>/dev/null)"
JIKAN_URL="https://mg.robnugen.com/api/v1/sessions"

# Read mode (default: slow)
MODE="$(cat "$MODEFILE" 2>/dev/null || echo slow)"

# Stop mode: exit immediately (cron still runs, but does nothing)
if [ "$MODE" = "stop" ]; then
    exit 0
fi

# Check for one-shot trigger
if [ -f "$ONCEFILE" ]; then
    rm -f "$ONCEFILE"
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ONCE triggered" >> "$LOGFILE"
elif [ "$MODE" = "wild" ]; then
    # Wild: run if last run was >5 min ago
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +20 2>/dev/null)" ]; then
        exit 0
    fi
else
    # Slow (default): run if last run was >60 min ago
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +180 2>/dev/null)" ]; then
        exit 0
    fi
fi

# File-based lock check
if [ -f "$LOCKFILE" ]; then
    if [ "$(find "$LOCKFILE" -mmin +30 2>/dev/null)" ]; then
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STALE LOCK removed (older than 30min)" >> "$LOGFILE"
        rm -f "$LOCKFILE"
    else
        exit 0
    fi
fi

# Create lock and update last run timestamp
echo "$$" > "$LOCKFILE"
touch "$LAST_RUN"
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STARTED run $$ (mode=$MODE)" >> "$LOGFILE"

# Start Jikan session (bash manages this, not Claude)
AK_ID=""
if [ -n "$JIKAN_KEY" ]; then
    START_RESPONSE=$(curl -s -X POST "$JIKAN_URL" \
        -H "X-API-Key: $JIKAN_KEY" \
        -H "Content-Type: application/json" \
        -d "{\"activity_id\": 40, \"timezone\": \"Asia/Tokyo\"}")
    AK_ID=$(echo "$START_RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin)['session']['ak_id'])" 2>/dev/null)
    if [ -n "$AK_ID" ]; then
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) SESSION $AK_ID started" >> "$LOGFILE"
    else
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) SESSION start failed: $START_RESPONSE" >> "$LOGFILE"
    fi
fi

# Run the main work prompt (session tools removed from allowed list)
cd "$WORKDIR" && claude -p "$(cat $WORKDIR/PROMPT.md)" \
    --allowedTools "Read,Write,Edit,Bash,Glob,Grep,WebFetch,WebSearch,mcp__jikan__list_todos,mcp__jikan__list_inbox,mcp__jikan__send_inbox,mcp__jikan__mark_inbox_seen,mcp__jikan__mark_inbox_done,mcp__jikan__create_todo,mcp__jikan__complete_todo,mcp__jikan__update_todo,mcp__jikan__log_emotion_event,mcp__jikan__get_emotion_vocab,mcp__jikan__post_emotion_vocab,mcp__jikan__get_emotion_events,mcp__jikan__list_activities,mcp__jikan__list_sessions" \
    >> "$LOGFILE" 2>&1

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) FINISHED run $$" >> "$LOGFILE"

# Stop Jikan session (bash always reaches here, even if Claude crashed)
if [ -n "$AK_ID" ] && [ -n "$JIKAN_KEY" ]; then
    STOP_RESPONSE=$(curl -s -X PATCH "$JIKAN_URL/$AK_ID/stop" \
        -H "X-API-Key: $JIKAN_KEY" \
        -H "Content-Type: application/json")
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) SESSION $AK_ID stopped" >> "$LOGFILE"
fi

# Release lock
rm -f "$LOCKFILE"
