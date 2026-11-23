#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = (
    "I bought noise-cancelling headphones so I could hear myself think, "
    "and it turns out I had nothing to say."
)


def main() -> None:
    # The gate allows 1-200 characters; refuse to write anything longer
    # so a bad edit can never silently produce an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
