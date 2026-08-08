"""
Rosalind — Finding a Motif in DNA (SUBS)

Given a DNA string s and a shorter motif string t, find every
position in s where t occurs as a substring, including overlapping
occurrences. Positions are reported 1-indexed (Rosalind convention).

Usage:
    python solution.py input.txt
    (input.txt: line 1 = s, line 2 = t)
"""

import sys


def find_motif_positions(s: str, t: str) -> list[int]:
    """Return all 1-indexed starting positions where t occurs in s.

    Overlapping matches are included, e.g. find_motif_positions("AAAA", "AA")
    returns [1, 2, 3].
    """
    if not t or len(t) > len(s):
        return []

    positions = []
    start = 0
    while True:
        idx = s.find(t, start)
        if idx == -1:
            break
        positions.append(idx + 1)  # convert to 1-indexed
        start = idx + 1  # move forward by 1 to allow overlaps
    return positions


def main(path: str) -> None:
    with open(path) as f:
        lines = [line.strip() for line in f if line.strip()]
    s, t = lines[0], lines[1]

    positions = find_motif_positions(s, t)
    print(" ".join(str(p) for p in positions))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py input.txt")
        sys.exit(1)
    main(sys.argv[1])
