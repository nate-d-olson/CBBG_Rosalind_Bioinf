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
from rosalind_utils import readdat


def rev_comp(seq, return_rna=False, reverse=True):
    """ Sequence reverse complement seqeunce

    Given a DNA sequence as input return the reverse complement
    of the sequence.
    Example:
        Input  TTTGCGACCC
        Result CCCTCGCAAA
    Args:
        seq: nucleotide sequence as a text string
        return_rna: boolean returns U in place of T if true, default false
        return_comp: boolean if true does not reverse seq, default true
    Returns:
        string

    """
    # TODO add checks for characters not in alphabet
    # TODO work with RNA and ambiguous bases

    # convert to upper case for consistency
    seq = seq.upper()

    comp_lookup = {"A": "T", "T": "A",
                   "G": "C", "C": "G"}

    if return_rna:
        comp_lookup = {"A": "U", "T": "A", "U": "A",
                       "G": "C", "C": "G"}
    if reverse:
        rev_comp = "".join([comp_lookup[x] for x in seq[::-1]])
    else:

        rev_comp = "".join([comp_lookup[x] for x in seq])

    return(rev_comp)


def main(filename):
    dat = readdat(filename)
    print rev_comp(dat[0])


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
