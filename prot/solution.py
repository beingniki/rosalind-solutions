"""
Rosalind — Translating RNA into Protein (PROT)

Given an RNA string, translate it into its corresponding protein string
using the standard genetic code: each group of 3 RNA bases (a codon)
maps to one amino acid, until a STOP codon is reached (which is not
included in the output).

Usage:
    python solution.py input.txt
    (input.txt contains a single line: the RNA string)
"""

import sys

# Standard RNA codon table. "Stop" marks translation termination codons.
CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


def translate_rna(rna: str) -> str:
    """Translate an RNA string into a protein string, stopping at the
    first STOP codon (which is not included in the result).
    """
    protein_chars = []
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i + 3]
        amino_acid = CODON_TABLE[codon]
        if amino_acid == "Stop":
            break
        protein_chars.append(amino_acid)
    return "".join(protein_chars)


def main(path: str) -> None:
    with open(path) as f:
        rna = f.read().strip()
    print(translate_rna(rna))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py input.txt")
        sys.exit(1)
    main(sys.argv[1])
