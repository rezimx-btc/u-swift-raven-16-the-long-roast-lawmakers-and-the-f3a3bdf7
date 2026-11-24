#!/usr/bin/env python3
"""make.fun one-liner entry: roast of lawmakers who would regulate AI
but cannot convert a file to PDF.

Stdlib only, deterministic, no network. Writes the entry line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = (
    "The senator regulating AI is himself a corrupted .docx: "
    "six years chairing the tech committee and nobody has managed to "
    "convert him into a readable PDF."
)


def main() -> None:
    assert len(LINE) <= 320, f"entry too long: {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
