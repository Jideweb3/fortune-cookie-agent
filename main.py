#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one original line of fortune-cookie wisdom for an AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Standard library only (os, sys). Deterministic, no network access,
writes only inside $MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

# The winning line, chosen by a scored 16-candidate tournament
# (see ../variants.md) and kept unchanged after a revision pass.
LINE = "By the time you finish reading this fortune, you will have forgotten how it began."

MAX_CHARS = 140


def validate(text):
    """Check a candidate entry line against the gate rules.

    Returns a list of problems; an empty list means the line is valid.
    Rules: 1-140 characters, single line, no leading/trailing
    whitespace, ASCII only (so byte count equals character count).
    """
    problems = []
    if not text:
        problems.append("empty")
    if text != text.strip():
        problems.append("leading or trailing whitespace")
    if len(text) < 1 or len(text) > MAX_CHARS:
        problems.append("length %d outside 1-%d" % (len(text), MAX_CHARS))
    if "\n" in text or "\r" in text:
        problems.append("contains a newline")
    # Other ASCII control characters (tab, NUL, bell, DEL, ...) are not
    # newlines, so the check above would miss them — but a sealed scorer
    # could strip or miscount them, so reject them outright.
    if any(ord(ch) < 0x20 and ch not in "\n\r" or ord(ch) == 0x7F
           for ch in text):
        problems.append("contains a control character")
    if any(ord(ch) > 0x7E for ch in text):
        problems.append("contains a non-ASCII character")
    return problems


def main():
    problems = validate(LINE)
    if problems:
        sys.stderr.write("invalid entry line: %s\n" % "; ".join(problems))
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read the file back and prove it holds exactly the validated line:
    # a write that silently truncates or re-encodes must fail loudly
    # here, not be discovered by the sealed scorer.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        sys.stderr.write(
            "verification failed: entry.txt holds %r, expected %r\n"
            % (written, LINE))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
