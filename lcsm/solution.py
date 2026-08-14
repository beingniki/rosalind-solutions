"""
Rosalind — Finding a Shared Motif (LCSM)

Given several DNA strings (FASTA), find the longest substring that is
common to every one of them. If there are multiple longest common
substrings of the same length, any one of them is a valid answer.

This is the classic "longest common substring across many strings"
problem — more involved than earlier problems because a shared motif
could start at any position in any sequence, so a naive check is
expensive if not written carefully.

Usage:
    python solution.py input.fasta
"""

import sys


def parse_fasta(path: str) -> list[str]:
    """Read a FASTA file and return a list of sequences, order preserved."""
    sequences = []
    current = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current:
                    sequences.append("".join(current))
                    current = []
            else:
                current.append(line)
    if current:
        sequences.append("".join(current))
    return sequences


def longest_common_substring(sequences: list[str]) -> str:
    """Return the longest substring shared by every sequence in the list.

    Strategy: take the shortest sequence as the source of candidate
    substrings (a shared motif can't be longer than the shortest
    sequence anyway), then binary-search on candidate length -- for
    each length, check all substrings of that length from the shortest
    sequence against every other sequence. This avoids generating and
    comparing every possible substring pair directly, which would be
    far too slow for longer sequences.
    """
    if not sequences:
        return ""

    shortest = min(sequences, key=len)
    other_seqs = [s for s in sequences if s is not shortest]

    def has_common_substring_of_length(length: int) -> str | None:
        if length == 0:
            return ""
        seen_candidates = set()
        for start in range(len(shortest) - length + 1):
            candidate = shortest[start:start + length]
            if candidate in seen_candidates:
                continue
            seen_candidates.add(candidate)
            if all(candidate in s for s in other_seqs):
                return candidate
        return None

    low, high = 0, len(shortest)
    best = ""
    # Binary search for the longest length that still has a common substring.
    while low <= high:
        mid = (low + high) // 2
        found = has_common_substring_of_length(mid)
        if found is not None:
            best = found
            low = mid + 1
        else:
            high = mid - 1

    return best


def main(path: str) -> None:
    sequences = parse_fasta(path)
    print(longest_common_substring(sequences))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py input.fasta")
        sys.exit(1)
    main(sys.argv[1])
