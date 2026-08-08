# SUBS — Finding a Motif in DNA

Rosalind problem: given a DNA string `s` and a shorter motif `t`, find every
1-indexed position in `s` where `t` occurs, including overlapping matches.

## Files
- `solution.py` — solution + CLI entry point
- `test_solution.py` — unit tests (run with `python test_solution.py` or `pytest`)
- `sample_input.txt` — Rosalind's sample dataset

## Run
```bash
python solution.py sample_input.txt
# 2 4 10
```

## Approach
Repeated `str.find()` from the position just after each match, so
overlapping occurrences (e.g. `AA` inside `AAAA`) aren't missed — the naive
"split and count" approach would miss these.

Link: https://rosalind.info/problems/subs/
