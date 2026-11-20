"""news-image-20261120 entry: one image that sums up 20 November 2026.

The image is entry.png beside this file: a newspaper front page, "The World
in a Day", composed in HTML (src/frontpage.html) and rendered to a
1024x1024 PNG (build/render.sh). This program verifies the image is a whole
PNG or JPEG within the gate's caps and copies it, byte for byte, to
/output/entry.png, so two runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
MAX_BYTES = 1_048_576  # the gate's 1 MiB cap


def main() -> None:
    data = (HERE / "entry.png").read_bytes()
    is_png = data[:8] == b"\x89PNG\r\n\x1a\n"
    is_jpeg = data[:3] == b"\xff\xd8\xff"
    if not (is_png or is_jpeg):
        raise ValueError("entry.png is not a PNG or JPEG image")
    if len(data) > MAX_BYTES:
        raise ValueError(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.png").write_bytes(data)


if __name__ == "__main__":
    sys.exit(main())
