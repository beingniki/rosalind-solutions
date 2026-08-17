"""Unit tests for the SPLC solution."""

from solution import (
    dna_to_rna,
    parse_fasta,
    splice_and_translate,
    splice_introns,
    translate_rna,
)


def test_sample_case():
    # Verified by manual codon-by-codon translation (see README for the trace)
    dna = "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"
    introns = ["ATCGGTCGAA", "ATCGGTCGAGCGTGT"]
    assert splice_and_translate(dna, introns) == "MVYIADKQHVASREAYGHMFKVCA"


def test_parse_fasta():
    seqs = parse_fasta("sample_input.fasta")
    assert len(seqs) == 3
    assert seqs[0].startswith("ATGGTCTACATAGCT")


def test_splice_introns_removes_all_occurrences():
    dna = "AAABBBAAABBBAAA"
    assert splice_introns(dna, ["BBB"]) == "AAAAAAAAA"


def test_splice_introns_no_match_leaves_unchanged():
    dna = "AAAAAA"
    assert splice_introns(dna, ["GGG"]) == "AAAAAA"


def test_dna_to_rna():
    assert dna_to_rna("GATTACA") == "GAUUACA"


def test_translate_rna_reused_correctly():
    assert translate_rna("AUGUAA") == "M"


if __name__ == "__main__":
    test_sample_case()
    test_parse_fasta()
    test_splice_introns_removes_all_occurrences()
    test_splice_introns_no_match_leaves_unchanged()
    test_dna_to_rna()
    test_translate_rna_reused_correctly()
    print("All tests passed.")
