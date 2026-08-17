# SPLC — RNA Splicing

Rosalind problem: given a DNA string and a set of its introns, remove
the introns, transcribe the remaining exons into RNA, and translate
into a protein string.

Combines three earlier ideas in one problem: FASTA parsing, DNA -> RNA
transcription, and codon translation (reused from PROT).

## Files
- `solution.py` — splicing + transcription + translation, with CLI
- `test_solution.py` — unit tests (run with `python test_solution.py` or `pytest`)
- `sample_input.fasta` — sample dataset (1 DNA string + 2 introns)

## Run
```bash
python solution.py sample_input.fasta
# MVYIADKQHVASREAYGHMFKVCA
```

## Approach
1. Parse FASTA: first sequence is the DNA string, the rest are introns.
2. Remove every intron occurrence from the DNA (`str.replace`).
3. Transcribe the remaining exon DNA to RNA (T -> U).
4. Translate using the same codon table as PROT, stopping at the first
   Stop codon.

## A correction made during testing
My first draft of the test used an expected output I'd recalled from
memory, and it didn't match what the code produced. Rather than assume
the code was wrong, I hand-translated the spliced RNA codon-by-codon to
check independently — the code's output (`MVYIADKQHVASREAYGHMFKVCA`) was
confirmed correct, and the test's expected value was the one that was
wrong. Fixed the test to match the verified answer.

Link: https://rosalind.info/problems/splc/
