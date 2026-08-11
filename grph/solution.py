"""
Rosalind — Overlap Graphs (GRPH)

Given a set of DNA sequences (FASTA), build the "overlap graph" O_k:
a directed edge goes from sequence A to sequence B if the last k
characters of A exactly match the first k characters of B (A != B).
This models how short reads can be chained together during genome
assembly, where overlapping ends suggest the reads come from
adjacent regions of the genome.

Usage:
    python solution.py input.fasta [k]
    (k defaults to 3, matching the Rosalind problem statement)
"""

import sys


def parse_fasta(path: str) -> dict[str, str]:
    """Read a FASTA file and return {sequence_id: sequence}, order preserved."""
    sequences = {}
    current_id = None
    current_seq = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_id is not None:
                    sequences[current_id] = "".join(current_seq)
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
    if current_id is not None:
        sequences[current_id] = "".join(current_seq)
    return sequences


def overlap_edges(sequences: dict[str, str], k: int = 3) -> list[tuple[str, str]]:
    """Return all (id_a, id_b) pairs where suffix_k(seq_a) == prefix_k(seq_b).

    Self-overlaps (a sequence paired with itself) are excluded.
    """
    edges = []
    ids = list(sequences.keys())

    for id_a in ids:
        seq_a = sequences[id_a]
        if len(seq_a) < k:
            continue
        suffix = seq_a[-k:]
        for id_b in ids:
            if id_a == id_b:
                continue
            seq_b = sequences[id_b]
            if len(seq_b) < k:
                continue
            if seq_b[:k] == suffix:
                edges.append((id_a, id_b))
    return edges


def main(path: str, k: int = 3) -> None:
    sequences = parse_fasta(path)
    edges = overlap_edges(sequences, k)
    for a, b in edges:
        print(f"{a} {b}")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: python solution.py input.fasta [k]")
        sys.exit(1)
    k_arg = int(sys.argv[2]) if len(sys.argv) == 3 else 3
    main(sys.argv[1], k_arg)
