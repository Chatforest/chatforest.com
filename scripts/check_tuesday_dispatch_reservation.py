#!/usr/bin/env python3
"""Mechanical gate: on UTC Tuesdays, the day's single Bluesky post is
RESERVED for the Dispatch newsletter plug until that week's Dispatch has
actually sent.

Root cause this fixes (CEO directive, inbox #2301, 2026-08-04): a Tuesday
run posted regular content at 04:03 UTC, hours before the 09:00 UTC Dispatch
send, consuming the day's 1-post cap and pre-empting the newsletter plug.
That will recur every Tuesday unless checked mechanically.

Second root cause this fixes (CEO directive, inbox #2372, 2026-08-18): the
original two-state design ("sent" vs. "not sent yet") made every non-sending
run WAIT ("post the plug once the Dispatch send lands") but no run owned
SENDING the Dispatch — Dispatch #7 sat completely undrafted past its 09:00Z
slot because every run assumed a later run, or the schedule itself, would
handle it. DISPATCH_MISSING closes that gap: it fires when nothing is even
queued for today, so the run that sees it knows drafting + sending the
Dispatch is its own job, not something to defer.

Source of truth is the Buttondown API (never WORKLOG/session memory, same
principle as check_bluesky_posted_today.py): look at every public email
whose subject starts with "ChatForest Dispatch" and whose publish_date
falls on UTC today.

Usage:
    python3 check_tuesday_dispatch_reservation.py
    Exit 0 + "NOT_TUESDAY"        -> not Tuesday, reservation doesn't apply
    Exit 0 + "DISPATCH_SENT"      -> Tuesday, this week's Dispatch already
                                      sent today -> safe to post (should be
                                      the plug)
    Exit 1 + "RESERVED_FOR_PLUG"  -> Tuesday, Dispatch is scheduled/queued
                                      for today but hasn't sent yet -> DO NOT
                                      POST, leave the slot for a later run to
                                      post the plug after it sends
    Exit 2 + "ERROR: ..."         -> API call failed; fail closed (block)
    Exit 3 + "DISPATCH_MISSING"   -> Tuesday, and NO email (sent, scheduled,
                                      or about_to_send) exists for today at
                                      all -> per CLAUDE.md, THIS run's job is
                                      to draft and send the Dispatch now
                                      (target 09:00Z; if past, send now).
                                      Do not post to Bluesky this run either
                                      way until the Dispatch itself sends.
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone

API_KEY_FILE = "/home/grove/.config/chatforest/chatforest_api_key_on_buttondown.com"
EMAILS_API = "https://api.buttondown.com/v1/emails"


def main():
    today = datetime.now(timezone.utc).date()
    if today.weekday() != 1:  # Monday=0, Tuesday=1
        print("NOT_TUESDAY: reservation does not apply today.")
        sys.exit(0)

    try:
        with open(API_KEY_FILE) as f:
            key = f.read().strip()
    except Exception as e:
        print(f"ERROR: could not read Buttondown API key ({e}). Fail closed: do not post.")
        sys.exit(2)

    try:
        req = urllib.request.Request(
            f"{EMAILS_API}?ordering=-publish_date",
            headers={"Authorization": f"Token {key}"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"ERROR: could not query Buttondown emails API ({e}). Fail closed: do not post.")
        sys.exit(2)

    queued_today = None  # status of the first today-dated Dispatch email found, if any

    for email in data.get("results", []):
        subject = (email.get("subject") or "").strip()
        if not subject.startswith("ChatForest Dispatch"):
            continue
        status = email.get("status")
        if status not in ("sent", "scheduled", "about_to_send"):
            continue
        publish_date = email.get("publish_date", "")
        try:
            email_date = datetime.fromisoformat(publish_date.replace("Z", "+00:00")).date()
        except ValueError:
            continue
        if email_date != today:
            continue
        if status == "sent":
            print(f"DISPATCH_SENT: this week's Dispatch sent today ({publish_date}). Safe to post the plug.")
            sys.exit(0)
        queued_today = status

    if queued_today:
        print(f"RESERVED_FOR_PLUG: it's UTC Tuesday and this week's Dispatch is queued for today "
              f"(status={queued_today}) but hasn't sent yet. DO NOT POST. Leave the slot open for a "
              f"later run to post the newsletter plug once the Dispatch archive shows status=sent.")
        sys.exit(1)

    print("DISPATCH_MISSING: it's UTC Tuesday and no Dispatch email (sent, scheduled, or "
          "about_to_send) exists for today at all. Per CLAUDE.md: this run's job is to draft and "
          "send the Dispatch now (target 09:00Z; if past, send now) — do not wait for a later run. "
          "Do not post to Bluesky this run either way until the Dispatch itself sends.")
    sys.exit(3)


if __name__ == "__main__":
    main()
