#!/usr/bin/env python3
"""make.fun entry: One Star, Five Stars for the Food.

Writes a one-sentence alien-tourist one-star review of Earth with a
real food compliment to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = (
    "I queued 47 minutes in Earth's rain for a bus that never came "
    "while my tentacled guide Zorp ate my ticket, one star, but the "
    "nasi goreng at stall 12 was so good I nearly forgave this soggy planet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
