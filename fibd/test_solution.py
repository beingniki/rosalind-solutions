"""Unit tests for the FIBD solution."""

from solution import mortal_rabbit_pairs


def test_sample_case():
    # Official Rosalind sample: n=6, m=3 -> 4
    assert mortal_rabbit_pairs(6, 3) == 4


def test_month_one():
    assert mortal_rabbit_pairs(1, 3) == 1


def test_month_zero():
    assert mortal_rabbit_pairs(0, 3) == 0


def test_immortal_case_matches_classic_fibonacci():
    # With a very long lifespan (never die within n months),
    # this should match the classic Fibonacci sequence of pairs.
    n, m = 8, 100
    assert mortal_rabbit_pairs(n, m) == 21  # F(8) in the rabbit-pair convention


def test_lifespan_one_pair_always_dies_next_month():
    # m=1: every pair dies the month after it's born, before it can reproduce
    assert mortal_rabbit_pairs(1, 1) == 1
    assert mortal_rabbit_pairs(2, 1) == 0
    assert mortal_rabbit_pairs(3, 1) == 0


if __name__ == "__main__":
    test_sample_case()
    test_month_one()
    test_month_zero()
    test_immortal_case_matches_classic_fibonacci()
    test_lifespan_one_pair_always_dies_next_month()
    print("All tests passed.")
