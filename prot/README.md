# PROT — Translating RNA into Protein

Rosalind problem: translate an RNA string into its protein string using
the standard genetic code — every 3 bases (a codon) map to one amino
acid, until a STOP codon is reached (not included in the output).

## Files
- `solution.py` — codon table + translation logic, with CLI
- `test_solution.py` — unit tests (run with `python test_solution.py` or `pytest`)
- `sample_input.txt` — Rosalind's sample dataset

## Run
```bash
python solution.py sample_input.txt
# MAMAPRTEINSTRING
```

## Approach
A lookup table (dict) maps all 64 possible RNA codons to their amino acid
(or "Stop"). Walk the RNA string 3 characters at a time, translate each
codon, and stop as soon as a Stop codon is hit — this mirrors how
ribosomes actually terminate translation in a cell.

Link: https://rosalind.info/problems/prot/
