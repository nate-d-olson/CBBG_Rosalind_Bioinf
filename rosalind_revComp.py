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


def rev_comp(seq):
    """ Sequence reverse complement seqeunce

    Given a DNA sequence as input return the reverse complement
    of the sequence.
    Example:
        Input  TTTGCGACCC
        Result CCCTCGCAAA
    Args:
        seq: nucleotide sequence as a text string

    Returns:
        string

    """
    # TODO add checks for characters not in alphabet
    # TODO work with RNA and ambiguous bases

    # convert to upper case for consistency
    seq = seq.upper()

    comp_lookup = {"A": "T", "T": "A",
                   "G": "C", "C": "G"}
    rev_comp = "".join([comp_lookup[x] for x in seq[::-1]])

    return(rev_comp)


def readdat(filename):
    """ Reading input file

    Reads lines in file and returns a list

    Args:
        filename: name of file with input data

    Returns:
        List of lines in the input file as strings

    Raises:
        IOError: An error occurred accessing the file.
    """

    try:
        open(filename, 'r')
    except:
        # TODO add error message
        raise

    with open(filename, 'r') as f:
        dat = map(str.strip, f.readlines())
    return dat


def main(filename):
    dat = readdat(filename)
    print rev_comp(dat[0])

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
