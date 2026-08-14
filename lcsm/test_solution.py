"""Unit tests for the LCSM solution."""

from solution import longest_common_substring, parse_fasta


def test_parse_fasta():
    seqs = parse_fasta("sample_input.fasta")
    assert seqs == ["GATTACA", "TAGACCA", "ATACA"]


def test_sample_case_length_and_validity():
    seqs = ["GATTACA", "TAGACCA", "ATACA"]
    result = longest_common_substring(seqs)
    # Rosalind accepts any correct longest common substring; length 2 is optimal
    # for this sample (e.g. "AC" or "CA" both work).
    assert len(result) == 2
    assert all(result in s for s in seqs)


def test_identical_sequences():
    seqs = ["ACGTACGT", "ACGTACGT"]
    assert longest_common_substring(seqs) == "ACGTACGT"


def test_no_common_substring():
    seqs = ["AAAA", "TTTT"]
    assert longest_common_substring(seqs) == ""


def test_single_sequence():
    seqs = ["ACGT"]
    assert longest_common_substring(seqs) == "ACGT"


def test_common_substring_not_at_start():
    seqs = ["XXXABCXXX", "YYABCYY", "ABC"]
    result = longest_common_substring(seqs)
    assert result == "ABC"


if __name__ == "__main__":
    test_parse_fasta()
    test_sample_case_length_and_validity()
    test_identical_sequences()
    test_no_common_substring()
    test_single_sequence()
    test_common_substring_not_at_start()
    print("All tests passed.")
