"""Seared Ribeye -- The Perfect First Bite.

Writes one food photograph to /output/entry.png.

The picture is a single thick-cut seared ribeye steak, medium-rare,
one slice cut and leaning against it, juice and a little steam,
on a warm cream plate. It is stored next to this file as steak.jpg
(1024x1024 JPEG, quality 85) and copied byte-for-byte to the output,
so the program is deterministic, uses only the standard library,
and needs no network.
"""

# The copy is byte-for-byte on purpose: the steak picture itself is
# the entry, and this program only delivers it unchanged.
import os
import shutil

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "steak.jpg")
OUTPUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(ASSET, "rb") as source:
        with open(OUTPUT, "wb") as target:
            shutil.copyfileobj(source, target)
    # The entry gate is 1,048,576 bytes; fail loudly instead of
    # silently submitting an oversized file.
    size = os.path.getsize(OUTPUT)
    if size > 1048576:
        raise SystemExit("entry.png is %d bytes, over the 1 MiB limit" % size)


if __name__ == "__main__":
    main()
