# IEV — Calculating Expected Offspring

Rosalind problem: given the number of couples for each of six possible
parent genotype pairings (for one gene, dominant/recessive), and assuming
each couple has exactly two offspring, find the expected number of
offspring showing the dominant phenotype.

## Files
- `solution.py` — expected-value calculation + CLI
- `test_solution.py` — unit tests (run with `python test_solution.py` or `pytest`)

## Run
```bash
python solution.py 1 0 0 1 0 1
# 3.5
```

## Approach
Each pairing has a fixed probability that any one offspring shows the
dominant phenotype (from a standard Punnett square):

| Pairing | P(dominant offspring) |
|---|---|
| AA-AA | 1.0 |
| AA-Aa | 1.0 |
| AA-aa | 1.0 |
| Aa-Aa | 0.75 |
| Aa-aa | 0.5 |
| aa-aa | 0.0 |

Expected value is linear (`E[X+Y] = E[X] + E[Y]`), so the total expected
dominant offspring is just a weighted sum across all six pairings:
`couples[i] * probability[i] * 2` (two offspring per couple), summed.
No simulation needed — this is a direct calculation.

Link: https://rosalind.info/problems/iev/
