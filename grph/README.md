# GRPH - Overlap Graphs

Rosalind problem: given DNA sequences in FASTA format, build the overlap
graph O_k — a directed edge from sequence A to B exists if the last k
characters of A match the first k characters of B (A != B, k = 3 by default).

This is a simplified model of genome assembly: overlapping read ends
suggest two reads come from adjacent regions of the genome.

## Files
- `solution.py` : FASTA parser + overlap-edge finder, with CLI
- `test_solution.py` : unit tests (run with `python test_solution.py` or `pytest`)
- `sample_input.fasta` : Rosalind's sample dataset

## Run
```bash
python solution.py sample_input.fasta
# or with a custom k:
python solution.py sample_input.fasta 4
```

## Approach
For every pair of distinct sequences (A, B), compare the last `k` characters
of A against the first `k` characters of B. Sequences shorter than `k` are
skipped since they can't form a valid overlap. This is an O(n^2) comparison
over all sequence pairs, which is fine at the scale Rosalind tests.

Link: https://rosalind.info/problems/grph/
