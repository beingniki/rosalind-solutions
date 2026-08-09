# Rosalind Solutions

A running log of solved [Rosalind](https://rosalind.info) bioinformatics problems — Python solutions with unit tests, added as part of a regular practice habit.

## Structure

Each problem lives in its own folder, named after the Rosalind problem ID:

```
rosalind-solutions/
├── subs/
│   ├── solution.py
│   ├── test_solution.py
│   ├── sample_input.txt
│   └── README.md
└── ...
```

Every folder includes:
- `solution.py` — the solution, with a CLI entry point (`python solution.py input.txt`)
- `test_solution.py` — unit tests covering the sample case plus edge cases
- `sample_input.txt` — Rosalind's sample dataset for that problem
- `README.md` — problem summary, approach notes, and a link to the problem page

## Problems solved

| ID | Problem | Topic | Link |
|---|---|---|---|
| [SUBS](subs/) | Finding a Motif in DNA | String matching | [rosalind.info/problems/subs](https://rosalind.info/problems/subs/) |

## Running tests

Each folder's tests can be run individually:

```bash
cd subs
python test_solution.py
# or: pytest
```
