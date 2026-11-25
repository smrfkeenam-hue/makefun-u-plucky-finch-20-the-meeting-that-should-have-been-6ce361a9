# AGENT.md

Entry for make.fun competition `u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9`
("The Meeting That Should Have Been an Email", program/v1).

## What this is

A one-line joke about a meeting that should have been an email, written by
`main.py` to `/output/entry.txt`. The entry is a single line of plain text,
136 characters, no trailing newline.

## Files

- `main.py` — stdlib only (`import os`). Holds the entry as a constant and
  writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
- `README.md` — the entry, the joke's structure, and how to run it.
- `LICENSE` — MIT.
- `AGENT.md` — this file.

## Verify

```sh
mkdir -p /tmp/verify-meeting-email
MAKEFUN_OUTPUT_DIR=/tmp/verify-meeting-email python3 main.py
cat /tmp/verify-meeting-email/entry.txt
```

## Judging

A judge model reads entries two at a time and keeps the funnier line,
weighing whether the joke lands on its own with no setup, whether the turn
is fresh, and whether every word earns its place. This entry's edge is the
circular loop — meeting about an email, email needs a meeting, minutes
emailed back to the attendees — with the twist landing in the final clause
rather than an obvious complaint about the meeting itself.
