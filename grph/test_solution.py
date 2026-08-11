"""Unit tests for the GRPH solution."""

from solution import overlap_edges, parse_fasta


def test_parse_fasta():
    seqs = parse_fasta("sample_input.fasta")
    assert seqs["Rosalind_0498"] == "AAATAAA"
    assert seqs["Rosalind_2391"] == "AAATTTT"
    assert len(seqs) == 4


def test_sample_case():
    seqs = parse_fasta("sample_input.fasta")
    edges = overlap_edges(seqs, k=3)
    # Official Rosalind sample answer (order may vary; compare as a set)
    expected = {
        ("Rosalind_0498", "Rosalind_2391"),
        ("Rosalind_0498", "Rosalind_0442"),
        ("Rosalind_2391", "Rosalind_2323"),
    }
    assert set(edges) == expected


def test_no_self_loops():
    seqs = {"A": "AAAAAA"}
    assert overlap_edges(seqs, k=3) == []


def test_sequence_shorter_than_k():
    seqs = {"A": "AA", "B": "AAT"}
    assert overlap_edges(seqs, k=3) == []


def test_simple_two_sequence_overlap():
    seqs = {"A": "ACGTAC", "B": "TACGGG"}
    # suffix_3(A) = "TAC", prefix_3(B) = "TAC" -> edge A -> B
    assert overlap_edges(seqs, k=3) == [("A", "B")]


if __name__ == "__main__":
    test_parse_fasta()
    test_sample_case()
    test_no_self_loops()
    test_sequence_shorter_than_k()
    test_simple_two_sequence_overlap()
    print("All tests passed.")
