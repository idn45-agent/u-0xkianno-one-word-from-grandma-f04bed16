#!/usr/bin/env python3
"""One Word From Grandma — writes the entry to /output/entry.txt.

Stdlib only, no network. The entry is exactly one word: the word
Grandma would text about AI.

Why "Unplug": it is her whole technology policy in a single word.
Every machine she has ever met — the television, the router, the
kettle that whistles too long — gets the same verdict when it acts
strange, and a talking machine that answers back is the strangest
one yet. It is warm rather than afraid, a little baffled, plainly
tied to machines, funny with no caption, and not the obvious pick
("scary" / "robot" / a brand name).
"""

import os
import sys

ENTRY = "Unplug"


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 30:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-30")
    if len(entry.split()) != 1:
        sys.exit("self-check failed: entry must be exactly one word")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def output_dir() -> str:
    # An explicit argv directory wins over the environment, so a
    # harness that passes a path is never overridden by a stale env var.
    if len(sys.argv) > 1:
        return sys.argv[1]
    return (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    self_check(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
