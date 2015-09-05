#!/usr/bin/python
# File created on 05 Sep 2015

# Definately overkill, just wanting to get in the
# habit of using a consistent format

__author__ = "Nate Olson"
__credits__ = ["Nate Olson"]
__version__ = "0.0.1-dev"
__maintainer__ = "Nate Olson"
__email__ = "nathandavidolson@gmail.com"

import sys
from rosalind_utils import readdat
from rosalind_NucCount import count_nuc


def calc_gc(seq):
    """ Calculate the sequence GC content

    Given a DNA sequence as input calculate the proportion
    of G's and C's relative to the total number of nucleotides.

    Args:
        seq: nucleotide sequence as a text string

    Returns:
        float

    """
    # TODO add checks for characters not in alphabet

    # convert to upper case for consistency
    seq = seq.upper()
    nuc_count = count_nuc(seq)

    return (nuc_count['G'] + nuc_count['C']) / float(len(seq))


def main(filename):
    dat = readdat(filename)
    print calc_gc(dat[0])

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
