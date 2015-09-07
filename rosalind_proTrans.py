#!/usr/bin/python
# File created on 07 Sep 2015

# Definately overkill, just wanting to get in the
# habit of using a consistent format

__author__ = "Nate Olson"
__credits__ = ["Nate Olson"]
__version__ = "0.0.1-dev"
__maintainer__ = "Nate Olson"
__email__ = "nathandavidolson@gmail.com"

import sys
from collections import defaultdict
from rosalind_revComp import rev_comp
from rosalind_utils import parse_fasta


# codon table code from https://www.biostars.org/p/2903/
codon_table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
               "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
               "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
               "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
               "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
               "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
               "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
               "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
               "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
               "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
               "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
               "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
               "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
               "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
               "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
               "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}


def get_reading_frames(seq):
    """ Get all six reading frames for a RNA sequence

    Given a RNA sequence as input returns a list of all six
    RNA reading frames.

    Args:
        seq: nucleotide sequence as a text string

    Returns:
        dict with a list of reading frames

    Example:
        Input: "ACGTGCTAGTACAGT"
        Returns:
        {F0: ["ACG", "UGC", "UAG", "UAC", "AGU"],
         F1: ["CGU", "GCU", "AGU", "ACA"],
         F2: ["GUG", "CUA", "GUA","CAG"],
         R0: ["ACU", "GUA", "CUA", "GCA", "CGU"],
         R1: ["CGU", "GCU", "AGU", "ACA"],
         R2: ["GUG", "CTA", "GTA", "CAG"] }

    """
    f_seq = ["F", seq]
    rc_seq = ["R", rev_comp(seq, return_rna=True)]

    reading_frames = defaultdict(list)
    for direction, rna_seq in [rc_seq, f_seq]:
        for i in [0, 1, 2]:
            codons = [rna_seq[j:j + 3] for j in range(i, len(rna_seq) - 2, 3)]
            reading_frames[direction + str(i)] = codons
    return reading_frames


def rna_to_prot(seq):
    """ Translate RNA sequence to AA

    Given a RNA sequence as input return the AA sequence for all
    open reading frames.

    Args:
        seq: nucleotide sequence as a text string

    Returns:
        list of strings

    """

    reading_frames = get_reading_frames(seq)

    # translating reading frames
    aa_seqs = defaultdict(list)
    for frame, codons in reading_frames.iteritems():
        for codon in codons:
            aa_seqs[frame] += codon_table[codon]

    orfs = defaultdict(list)
    for frame, aa_list in aa_seqs.iteritems():
        for i in xrange(len(aa_list)):
            orf = ""
            if aa_list[i] == "M":
                orf += aa_list[i]
                for j in aa_list[i + 1:]:
                    if j == "*":
                        orfs[frame].append(orf)
                        break
                    else:
                        orf += j
    return orfs


def dna_to_prot(seq):
    """ Translate DNA sequence to AA

    Given a DNA sequence as input returns all AA sequence open
    reading frames.

    Args:
        seq: nucleotide sequence as a text string

    Returns:
        list of strings

    """

    # convert DNA seq to RNA
    rna_seq = seq.replace("T", "U")
    return rna_to_prot(rna_seq)


def print_rosalind_orfs(orf_dict):
    orfs = []
    for aa_list in orf_dict.values():
        orfs += aa_list

    print "\n".join(set(orfs))


def main(filename):
    dat = parse_fasta(filename)
    for name, seq in dat.iteritems():
        orf_dict = dna_to_prot(seq)
        print_rosalind_orfs(orf_dict)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
