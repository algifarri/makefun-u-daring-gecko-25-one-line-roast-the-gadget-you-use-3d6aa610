#!/usr/bin/env python3
"""One-line roast entry for make.fun's "One-Line Roast: The Gadget You Use Every Day".

Writes a single line, 200 characters at most, to /output/entry.txt:
an original roast of the printer, a gadget used every day, with a
concrete gripe (ink that only runs out when it matters, then a ten
minute "cleaning" cycle that burns more ink than the print would have).
Deterministic, standard library only, no input, no network.
"""

import os

ROAST = (
    "My printer only runs out of ink on the morning I actually need "
    "it, then spends ten minutes 'cleaning' itself like I'm the one "
    "wasting its time."
)


def main():
    # The gate allows 1-200 characters; the roast is 143, and it is
    # written exactly, with no trailing newline, as one line.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
