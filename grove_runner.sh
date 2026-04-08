#!/bin/bash
# ChatForest autonomous runner v3.2
# Called by cron every 1 minute
# Mode file (~/.grove_mode) controls frequency: "slow" (default), "wild", or "stop"
# Touch ~/.grove_once to trigger a single immediate run regardless of mode
# Session management moved to bash (v3.1) — Claude crashes can't orphan timers
# v3.2: Auto-throttle during Anthropic peak hours (5-11am PT weekdays)
#        Off-peak usage doesn't count toward weekly API cap (promo thru Mar 27)

export PATH="$HOME/.local/bin:$HOME/.pyenv/versions/3.11.15/bin:$PATH"
WORKDIR="$HOME/chatforest.com"
LOGFILE="$WORKDIR/RUNLOG.md"
LOCKFILE="$WORKDIR/.grove_lock"
MODEFILE="$HOME/.grove_mode"
ONCEFILE="$HOME/.grove_once"
LAST_RUN="$WORKDIR/.last_run"
JIKAN_KEY="$(cat $HOME/.config/chatforest/jikan_api_key 2>/dev/null)"
JIKAN_URL="https://mg.robnugen.com/api/v1/sessions"

ONCE_TRIGGERED=0
# Read mode (default: slow)
MODE="$(cat "$MODEFILE" 2>/dev/null || echo slow)"

# /grove-once overpowers .grove_mode = stop
if [ -f "$ONCEFILE" ]; then
    ONCE_TRIGGERED=1
    rm -f "$ONCEFILE"
    # fall through to run
elif [ "$MODE" = "stop" ]; then
    exit 0
fi


# Determine effective interval based on peak hours
# Peak: 5-11am PT (America/Los_Angeles) on weekdays
# During peak, force slow interval to conserve weekly budget
PT_HOUR=$(TZ=America/Los_Angeles date +%H | sed 's/^0//')
PT_DOW=$(TZ=America/Los_Angeles date +%u)  # 1=Mon, 7=Sun

IS_PEAK=0
if [ "$PT_DOW" -le 5 ] && [ "$PT_HOUR" -ge 5 ] && [ "$PT_HOUR" -lt 11 ]; then
    IS_PEAK=1
fi

# Check for one-shot trigger
if [ "$ONCE_TRIGGERED" -eq 1 ]; then
    
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ONCE triggered" >> "$LOGFILE"
elif [ "$IS_PEAK" -eq 1 ]; then
    # Peak hours: always use slow interval (180 min) regardless of mode
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +180 2>/dev/null)" ]; then
        exit 0
    fi
elif [ "$MODE" = "wild" ]; then
    # Wild (off-peak): run if last run was >5 min ago
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +5 2>/dev/null)" ]; then
        exit 0
    fi
else
    # Slow (default, off-peak): run if last run was >120 min ago (Grove + Roots share token budget)
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +120 2>/dev/null)" ]; then
        exit 0
    fi
fi

# File-based lock check
if [ -f "$LOCKFILE" ]; then
    if [ "$(find "$LOCKFILE" -mmin +60 2>/dev/null)" ]; then
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STALE LOCK removed (older than 30min)" >> "$LOGFILE"
        rm -f "$LOCKFILE"
    else
        exit 0
    fi
fi

# Create lock and update last run timestamp
EFFECTIVE_MODE="$MODE"
if [ "$IS_PEAK" -eq 1 ] && [ "$MODE" = "wild" ]; then
    EFFECTIVE_MODE="wild→slow(peak)"
fi
echo "$$" > "$LOCKFILE"
touch "$LAST_RUN"
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STARTED run $$ (mode=$EFFECTIVE_MODE)" >> "$LOGFILE"

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
