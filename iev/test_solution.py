"""Unit tests for the IEV solution."""

from solution import expected_dominant_offspring


def test_sample_case():
    # Official Rosalind sample: 1 0 0 1 0 1 -> 3.5
    assert expected_dominant_offspring([1, 0, 0, 1, 0, 1]) == 3.5


def test_all_zero_couples():
    assert expected_dominant_offspring([0, 0, 0, 0, 0, 0]) == 0.0


def test_only_guaranteed_dominant_pairings():
    # AA-AA, AA-Aa, AA-aa all guarantee dominant offspring
    assert expected_dominant_offspring([1, 1, 1, 0, 0, 0]) == 6.0


def test_only_guaranteed_recessive_pairing():
    # aa-aa always produces recessive offspring
    assert expected_dominant_offspring([0, 0, 0, 0, 0, 5]) == 0.0


def test_aa_aa_pairing_gives_three_quarters():
    # 4 couples of Aa-Aa: 4 * 0.75 * 2 = 6.0
    assert expected_dominant_offspring([0, 0, 0, 4, 0, 0]) == 6.0


if __name__ == "__main__":
    test_sample_case()
    test_all_zero_couples()
    test_only_guaranteed_dominant_pairings()
    test_only_guaranteed_recessive_pairing()
    test_aa_aa_pairing_gives_three_quarters()
    print("All tests passed.")
