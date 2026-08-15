"""
Rosalind — Calculating Expected Offspring (IEV)

A population has six possible parent-couple genotype pairings for a
single gene with dominant/recessive alleles. Given the number of
couples of each pairing, and assuming each couple has exactly two
offspring, calculate the expected number of offspring displaying the
dominant phenotype.

Pairing order (as given by Rosalind) and probability that a given
offspring shows the dominant phenotype:
    AA-AA : 1.0    (all offspring dominant)
    AA-Aa : 1.0
    AA-aa : 1.0
    Aa-Aa : 0.75   (3/4 dominant, from a standard Punnett square)
    Aa-aa : 0.5
    aa-aa : 0.0    (all offspring recessive)

Expected value is linear, so the total expected dominant-phenotype
offspring is simply: sum(couples[i] * prob[i] * 2) across all six
pairings (the *2 accounts for two offspring per couple).

Usage:
    python solution.py n1 n2 n3 n4 n5 n6
    e.g. python solution.py 1 0 0 1 0 1
"""

import sys

# Probability a single offspring shows the dominant phenotype, per pairing.
DOMINANT_PROBABILITIES = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

OFFSPRING_PER_COUPLE = 2


def expected_dominant_offspring(couples: list[int]) -> float:
    """Return the expected number of dominant-phenotype offspring.

    `couples` must have exactly 6 values, in the fixed Rosalind order:
    AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa.
    """
    if len(couples) != 6:
        raise ValueError("Expected exactly 6 couple counts")

    return sum(
        count * prob * OFFSPRING_PER_COUPLE
        for count, prob in zip(couples, DOMINANT_PROBABILITIES)
    )


def main(couples: list[int]) -> None:
    result = expected_dominant_offspring(couples)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python solution.py n1 n2 n3 n4 n5 n6")
        sys.exit(1)
    main([int(x) for x in sys.argv[1:7]])
