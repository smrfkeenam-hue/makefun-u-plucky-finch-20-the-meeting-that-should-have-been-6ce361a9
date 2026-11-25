import os

# One line, 136 characters: a meeting about an email that spawns
# another meeting, and the minutes go back by email to the people
# who were already in the room. The loop is the joke.
ENTRY = "I attended a meeting about an email, where we agreed the email needed a meeting, and the minutes were emailed to everyone who was there."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = os.path.join(out_dir, "entry.txt")
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
