#!/usr/bin/python
# File created on 04 Sep 2015

# Definately overkill, just wanting to get in the
# habit of using a consistent format

__author__ = "Nate Olson"
__credits__ = ["Nate Olson"]
__version__ = "0.0.1-dev"
__maintainer__ = "Nate Olson"
__email__ = "nathandavidolson@gmail.com"

import sys
from collections import Counter
from rosalind_utils import readdat


def count_nuc(seq):
    """ Counting nucleotides in a seqeunce

    Given a DNA sequence as input count the number of
    nucleotides (A's, G's, C's, and T's) in the sequence.

    Args:
        seq: nucleotide sequence as a text string

    Returns:
        Dictionary with counts nucleotide counts.
        For example:
            {'A': 10, 'G': 10, 'C': 10, 'T': 10}

    """
    # TODO add ability to count RNA and AA
    # TODO add checks for characters not in alphabet

    # convert to upper case for consistency
    seq = seq.upper()
    nuc_count = Counter(seq)

    return nuc_count


def rosalind_format_output(nuc_count):
    print "%d %d %d %d" % (nuc_count['A'], nuc_count['C'],
                           nuc_count['G'], nuc_count['T'])


def main(filename):
    dat = readdat(filename)
    counts = count_nuc(dat[0])
    rosalind_format_output(counts)

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
