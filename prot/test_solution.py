"""Unit tests for the PROT solution."""

from solution import translate_rna


def test_sample_case():
    # Official Rosalind sample
    rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    assert translate_rna(rna) == "MAMAPRTEINSTRING"


def test_stop_codon_ends_translation():
    # UAA is a stop codon; nothing after it should be translated
    rna = "AUGUAAUUUUUU"
    assert translate_rna(rna) == "M"


def test_no_stop_codon_translates_everything():
    rna = "AUGGCC"
    assert translate_rna(rna) == "MA"


def test_all_three_stop_codons():
    for stop_codon in ["UAA", "UAG", "UGA"]:
        assert translate_rna("AUG" + stop_codon) == "M"


def test_empty_string():
    assert translate_rna("") == ""


if __name__ == "__main__":
    test_sample_case()
    test_stop_codon_ends_translation()
    test_no_stop_codon_translates_everything()
    test_all_three_stop_codons()
    test_empty_string()
    print("All tests passed.")
