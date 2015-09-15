#!/usr/bin/python
# File created on 14 Sep 2015

__author__ = "Nate Olson"
__credits__ = ["Nate Olson"]
__version__ = "0.0.1-dev"
__maintainer__ = "Nate Olson"
__email__ = "nathandavidolson@gmail.com"

import sys
from rosalind_utils import parse_fasta
import numpy as np
from Bio.SubsMat.MatrixInfo import blosum62 as bl62


# bl62 triangular matrix - code to prevent errors when getting score
def get_score(x, y, mat):
    return mat[(x, y)] if (x, y) in mat else mat[(y, x)]

# both of these now work
assert get_score('A', 'B', bl62) == get_score('B', 'A', bl62)

"""
Rosalind Generalizing the Alignment Score
Problem:
    To penalize symbol substitutions differently depending
    on which two symbols are involved in the substitution,
    we obtain a scoring matrix S in which Si,j represents
    the (negative) score assigned to a substitution of the
    ith symbol of our alphabet A with the jth symbol of A.
    A gap penalty is the component deducted from alignment
    score due to the presence of a gap. A gap penalty may be
    a function of the length of the gap; for example, a linear
    gap penalty is a constant g such that each inserted or
    deleted symbol is charged g; as a result, the cost of
    a gap of length L is equal to gL.

Given: Two protein strings s and t in FASTA format
       (each of length at most 1000 aa).

Return: The maximum alignment score between s and t. Use:

The BLOSUM62 scoring matrix.
Linear gap penalty equal to 5 (i.e.,
a cost of -5 is assessed for each gap symbol).
"""


def calc_align_score(seq1, seq2, gap_penalty=-5, mat=bl62):
    """ Calculate the global alignment score for two sequences

    Given two strings calculate global alignment score a
    a scoring metric (default BLOSSUM62) is used to score matches
    and substitutions, gaps are scored linearly based on the length
    of the gap.

    Args:
        seq1: sequence as a text string
        seq2: sequence as a text string
        gap_penalty: cost of a single insertion or deletion, default -5
        mat: scoring matrix, default = BLOSSUM62

    Returns:
        int: global alignment score
    """

    n_seq1 = len(seq1)
    n_seq2 = len(seq2)

    # initiating matrix for dynamic programming
    align_score = np.zeros((n_seq1 + 1, n_seq2 + 1))
    for i in xrange(n_seq1 + 1):
        align_score[i, 0] = i * gap_penalty
        for j in xrange(n_seq2 + 1):
            align_score[0, j] = j * gap_penalty

    # finding edit dist using dynamic programming
    for i in xrange(1, n_seq1 + 1):
        for j in xrange(1, n_seq2 + 1):
            s = get_score(seq1[i - 1], seq2[j - 1], mat)
            align_score[i, j] = max(
                align_score[i - 1, j - 1] + s,
                align_score[i - 1, j] + gap_penalty,
                align_score[i, j - 1] + gap_penalty)

    return align_score[n_seq1, n_seq2]


def main(filename):
    dat = parse_fasta(filename)
    if len(dat.values()) > 2:
        print "More than two sequences in input file, " \
              "only calculting edit distance between" \
              " two sequences"
        # need to clarify message as parse_fasta retuns a dict,
        # not just first two seqs
    print calc_align_score(dat.values()[0], dat.values()[1])


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
