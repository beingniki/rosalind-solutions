"""Unit tests for the SUBS solution."""

from solution import find_motif_positions


def test_sample_case():
    # Standard Rosalind sample: s = GATATATGCATATACTT, t = ATAT
    s = "GATATATGCATATACTT"
    t = "ATAT"
    assert find_motif_positions(s, t) == [2, 4, 10]


def test_overlapping_matches():
    assert find_motif_positions("AAAA", "AA") == [1, 2, 3]


def test_no_match():
    assert find_motif_positions("GGGG", "AT") == []


def test_motif_longer_than_string():
    assert find_motif_positions("AT", "ATAT") == []


def test_motif_equals_string():
    assert find_motif_positions("ATAT", "ATAT") == [1]


if __name__ == "__main__":
    test_sample_case()
    test_overlapping_matches()
    test_no_match()
    test_motif_longer_than_string()
    test_motif_equals_string()
    print("All tests passed.")
