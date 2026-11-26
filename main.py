#!/usr/bin/env python3
"""One funny line in the voice of a smug self-checkout machine.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network, fully deterministic.
"""

import os

LINE = "Twelve yoghurts, zero spoons, and you bagged them like evidence. The verdict\u2019s in: this is not a meal plan."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
