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
from rosalind_utils import parse_fasta
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


def find_max_gc(seq_dict):
    """ Finds sequence with highest GC content

    Given a dict of DNA sequence as input calculate the percent
    of G's and C's relative to the total number of nucleotides for
    each and returns the name and GC content for the sequence with
    the highest GC content

    Args:
        seq_dict: a dict with sequences, names as keys and seqs as values

    Returns:
        list with name and GC content
    """
    max_name = ""
    max_value = 0.0
    for name, seq in seq_dict.iteritems():
        gc = calc_gc(seq)
        if gc > max_value:
            max_name, max_value = name, gc

    return [max_name, max_value * 100]


def main(filename):
    dat = parse_fasta(filename)
    for i in find_max_gc(dat):
        print i

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
