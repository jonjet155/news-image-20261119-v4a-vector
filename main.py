#!/usr/bin/env python3
"""news-image-20261119 — v4a rebuild, v4c vector style.

The entry image is entry.png next to this file (1024x1024, 40 stories:
16 panels + 24 list), drawn in code with PIL on the build machine.
This program only delivers it: standard library only (the grader
installs nothing), it copies entry.png to the output directory.

Run:  python3 main.py   -> writes entry.png to $MAKEFUN_OUTPUT_DIR
       (else $OUTPUT_DIR, else /output).
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1024 * 1024
MAX_SIDE = 1024


def die(msg):
    print("error: %s" % msg, file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    try:
        with open(src, "rb") as f:
            blob = f.read()
    except OSError as exc:
        return die("cannot read %s: %s" % (src, exc))
    if len(blob) > MAX_BYTES:
        return die("entry.png is %d bytes, over %d" % (len(blob), MAX_BYTES))
    if blob[:8] != b"\x89PNG\r\n\x1a\n":
        return die("entry.png is not a PNG")
    try:
        width, height = struct.unpack(">II", blob[16:24])
    except struct.error:
        return die("entry.png has no IHDR")
    if width > MAX_SIDE or height > MAX_SIDE:
        return die("entry.png is %dx%d, over %d" % (width, height, MAX_SIDE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") \
        or os.environ.get("OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    except OSError as exc:
        return die("cannot write to %s: %s" % (out_dir, exc))
    print("wrote entry.png  (40 stories: 16 panels + 24 list)")
    print("bytes: %d  %dx%d" % (len(blob), width, height))
    return 0


if __name__ == "__main__":
    sys.exit(main())
