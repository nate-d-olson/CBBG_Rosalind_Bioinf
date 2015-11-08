#!/usr/bin/python
# File created on 7 Nov 2015


__author__ = "Nate Olson"
__credits__ = ["Nate Olson"]
__version__ = "0.0.1-dev"
__maintainer__ = "Nate Olson"
__email__ = "nathandavidolson@gmail.com"

import sys
from rosalind_utils import parse_fasta
import numpy as np


def dna_profile(motifs):
    """ DNA Motif Profile

    Given a set of DNA motifs as input return the motif profile.
    Example:
        Input  TTTGCGACCC
        Result CCCTCGCAAA
    Args:
        motifs: a list of dna motifs of length L
    Returns:
        a 4 X L matrix with counts for each DNA base at each
        position in the motif

    """

    # create matrix for profile
    l = len(motifs[0])

    profile = np.zeros((4, l), dtype=np.int)

    # base row assignments
    # 0 - A, 1 - C, 2 - G, 3 - T
    for i in motifs:
        for j in xrange(0, l):
            if i[j] == "A":
                profile[0, j] += 1
            elif i[j] == "C":
                profile[1, j] += 1
            elif i[j] == "G":
                profile[2, j] += 1
            elif i[j] == "T":
                profile[3, j] += 1

    return profile


def print_profile(profile):
    """
    Prints profile accoring to Rosalind required format

    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    """

    bases = ["A", "C", "G", "T"]

    for i in xrange(0, 4):
        base_counts_str = map(str, profile[i])
        print "%s: %s" % (bases[i], " ".join(base_counts_str))
    return


def profile_consensus(profile):
    """ DNA Consensus sequence from profile

    Calculate consensus sequence from motif profile.
    Example:
        Input
        Result
    Args:
        profile: a 4 X L profile matrix
    Returns:
        consensus sequence from a profile
    """

    bases = ["A", "C", "G", "T"]
    consen_seq = ""
    for i in xrange(0, len(profile[0])):
        base_counts = list(profile[:, i])
        base_index = base_counts.index(max(base_counts))
        consen_seq += bases[base_index]

    return consen_seq


def main(filename):
    dat = parse_fasta(filename)
    profile = dna_profile(dat.values())
    print profile_consensus(profile)
    print_profile(profile)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
