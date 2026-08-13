"""
Rosalind — Mortal Fibonacci Rabbits (FIBD)

A pair of rabbits reproduces every month starting one month after birth,
but each pair dies after living exactly m months. Given n months and
lifespan m, find the total number of rabbit pairs alive after n months.

This is a variant of the classic Fibonacci recurrence, but pairs must
also be removed once they reach the end of their lifespan.

Usage:
    python solution.py n m
    e.g. python solution.py 6 3
"""

import sys


def mortal_rabbit_pairs(n: int, m: int) -> int:
    """Return the total rabbit pairs alive after n months, lifespan m months.

    Tracks the population as a list of counts by age (1..m), shifting
    ages forward each month and dropping the oldest group (they die),
    while adding a new "age 1" group equal to all pairs old enough to
    reproduce (every age except the newborns from last month).
    """
    if n == 0:
        return 0

    # ages[0] = pairs of age 1 (just born), ages[m-1] = pairs of age m (about to die)
    ages = [1] + [0] * (m - 1)

    for _ in range(2, n + 1):
        newborns = sum(ages[1:])       # every pair except last month's newborns can reproduce
        ages = [newborns] + ages[:-1]  # shift ages up by one; oldest group (age m) dies off

    return sum(ages)


def main(n: int, m: int) -> None:
    print(mortal_rabbit_pairs(n, m))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python solution.py n m")
        sys.exit(1)
    main(int(sys.argv[1]), int(sys.argv[2]))
