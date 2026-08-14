# LCSM — Finding a Shared Motif

Rosalind problem: given several DNA strings (FASTA), find the longest
substring common to all of them. If multiple substrings of the same
maximal length qualify, any one is a valid answer.

## Files
- `solution.py` — binary-search-on-length approach + CLI
- `test_solution.py` — unit tests (run with `python test_solution.py` or `pytest`)
- `sample_input.fasta` — Rosalind's sample dataset

## Run
```bash
python solution.py sample_input.fasta
```

## Approach
A shared motif can't be longer than the shortest input sequence, so:
1. Take the shortest sequence as the source of candidate substrings.
2. Binary search on candidate *length* rather than checking every possible
   substring pair directly — for a given length, test whether any substring
   of that length from the shortest sequence appears in every other sequence.
3. Narrow the search: if a common substring of a given length exists, try
   longer; if not, try shorter.

This is a step up from earlier problems (SUBS, GRPH) because a brute-force
comparison of every substring against every other string scales badly —
binary search on length cuts the work down substantially while still
being straightforward to reason about and test.

Link: https://rosalind.info/problems/lcsm/
