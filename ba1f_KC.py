#!/usr/bin/python
# File created on Oct 1, 2015

__author__ = "Kenneth Cheng"
__credits__ = ["Kenneth Cheng"]
__version__ = "0.0.1-dev"
__maintainer__ = "Kenneth Cheng"
__email__ = ""

"""
Definition:
    Define the skew of a DNA string as the (number of 'G's) - (number of 'C's) in it.
    Define the prefix_i of a DNA string is the initial substring of DNA of length i. 

Problem Description: 
    Minimum Skew Problem
    Given: A DNA string genome.
    Return: All integer(s) of i, minimizing skew(prefix_i(genome)), i = 0 to len(genome).
"""

import sys
from rosalind_utils import readdat

# Approach 1:
  
def min_skew_prefix_len(dna):
    dna = dna.upper()
    skewlist = [0]
    curr_skew = 0
    skewdict = {'A':0, 'T':0, 'G':1, 'C':-1}
    for nt in dna:
        curr_skew += skewdict[nt]
        skewlist.append(curr_skew)
    minskew = min(skewlist)
    return [i for i, val in enumerate(skewlist) if val == minskew]
    

def main(filename):
    dat = readdat(filename)
    print min_skew_prefix_len(*dat)
    
    
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)