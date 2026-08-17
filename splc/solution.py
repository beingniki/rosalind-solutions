"""
Rosalind — RNA Splicing (SPLC)

Given a DNA string and a collection of its introns (substrings to
remove), splice out the introns, transcribe the remaining exons into
RNA, and translate that RNA into a protein string.

This combines three earlier ideas: FASTA parsing (like CONS/GRPH),
DNA -> RNA transcription, and codon translation (like PROT).

Usage:
    python solution.py input.fasta
    (input.fasta: first record = DNA string, remaining records = introns)
"""

import sys

# Reuse the same codon table approach as PROT.
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


def parse_fasta(path: str) -> list[str]:
    """Read a FASTA file and return a list of sequences, order preserved."""
    sequences = []
    current = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current:
                    sequences.append("".join(current))
                    current = []
            else:
                current.append(line)
    if current:
        sequences.append("".join(current))
    return sequences


def splice_introns(dna: str, introns: list[str]) -> str:
    """Remove every occurrence of each intron substring from the DNA string."""
    exon_dna = dna
    for intron in introns:
        exon_dna = exon_dna.replace(intron, "")
    return exon_dna


def dna_to_rna(dna: str) -> str:
    """Transcribe DNA to RNA (T -> U)."""
    return dna.replace("T", "U")


def translate_rna(rna: str) -> str:
    """Translate an RNA string into a protein string, stopping at Stop."""
    protein_chars = []
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i + 3]
        amino_acid = CODON_TABLE[codon]
        if amino_acid == "Stop":
            break
        protein_chars.append(amino_acid)
    return "".join(protein_chars)


def splice_and_translate(dna: str, introns: list[str]) -> str:
    exon_dna = splice_introns(dna, introns)
    rna = dna_to_rna(exon_dna)
    return translate_rna(rna)


def main(path: str) -> None:
    sequences = parse_fasta(path)
    dna, introns = sequences[0], sequences[1:]
    print(splice_and_translate(dna, introns))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py input.fasta")
        sys.exit(1)
    main(sys.argv[1])
