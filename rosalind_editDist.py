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

"""
Rosalind Edit Distance Problem Description
Problem:
    Given two strings s and t (of possibly different lengths), the edit
    distance dE(s,t) is the minimum number of edit operations needed to
    transform s into t, where an edit operation is defined as the
    substitution, insertion, or deletion of a single symbol. The latter
    two operations incorporate the case in which a contiguous interval
    is inserted into or deleted from a string; such an interval is called
    a gap. For the purposes of this problem, the insertion or deletion of
    a gap of length k still counts as k distinct edit operations.

Given: Two protein strings s and t in FASTA format (most 1000 aa in length).
Return: The edit distance dE(s,t).
"""


def calc_edit_distance(seq1, seq2):
    """ Calculate the edit distance between two strings

    Given two strings calculate the edit distance,
    or minimum number of operations needed to transform seq1 into
    seq2.  Edit operation is defined as a substitution, insertion,
    or deletion. Gaps that are the result of insertion and deletion
    edits are scored based on the lenght of the gap, one edit per
    gap length.

    Args:
        seq1: sequence as a text string
        seq2: sequence as a text string

    Returns:
        int: edit distance

    """
    n_seq1 = len(seq1)
    n_seq2 = len(seq2)

    # initiating matrix for dynamic programming
    edit_dist = np.zeros((n_seq1 + 1, n_seq2 + 1))
    for i in xrange(n_seq1 + 1):
        edit_dist[i, 0] = i * 1
        for j in xrange(n_seq2 + 1):
            edit_dist[0, j] = j * 1

    # finding edit dist using dynamic programming
    for i in xrange(1, n_seq1 + 1):
        for j in xrange(1, n_seq2 + 1):
            edit_dist[i, j] = min(
                edit_dist[i - 1, j - 1] + (seq1[i - 1] != seq2[j - 1]),
                edit_dist[i - 1, j] + 1,
                edit_dist[i, j - 1] + 1)

    return edit_dist[n_seq1, n_seq2]


def main(filename):
    dat = parse_fasta(filename)
    if len(dat.values()) > 2:
        print "More than two sequences in input file, " \
              "only calculting edit distance between" \
              " two sequences"
        # need to clarify message as parse_fasta retuns a dict,
        # not just first two seqs
    print calc_edit_distance(dat.values()[0], dat.values()[1])


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
