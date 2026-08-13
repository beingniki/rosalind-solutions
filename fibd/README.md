# FIBD — Mortal Fibonacci Rabbits

Rosalind problem: rabbit pairs reproduce every month starting one month
after birth, but each pair dies after living exactly `m` months. Given
`n` months and lifespan `m`, find the total pairs alive after `n` months.

## Files
- `solution.py` — age-tracking simulation + CLI
- `test_solution.py` — unit tests (run with `python test_solution.py` or `pytest`)

## Run
```bash
python solution.py 6 3
# 4
```

## Approach
Track the population as counts by age (1 to m), rather than trying to
derive a single closed-form recurrence with an off-by-one-prone subtraction
term. Each month:
1. All pairs except last month's newborns are old enough to reproduce -> new "age 1" group.
2. Every other age group shifts up by one.
3. The oldest group (age m) is dropped, since those pairs die this month.

This mirrors the real biological process directly, which makes it easier
to reason about and test than a single algebraic formula.

Link: https://rosalind.info/problems/fibd/
