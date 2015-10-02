#!/usr/bin/python
# File created on Oct 1, 2015

__author__ = "Kenneth Cheng"
__credits__ = ["Kenneth Cheng"]
__version__ = "0.0.1-dev"
__maintainer__ = "Kenneth Cheng"
__email__ = ""

"""
Definition:
    For kmer1 and kmer2, we say position i is a mismatch if kmer1[i] != kmer2[i].
    Define the number of mismatches between two strings as the Hamming distance between them. 

Problem Description: 
    Hamming Distance Problem
    Given: Two DNA strings.
    Return: An integer value of Hamming distance between the two dna strings.
"""

import sys
from rosalind_utils import readdat

# Approach 1:
  
def hamming_dist(p, q):
    hammdist = 0
    lenp = len(p)
    lenq = len(q)
    if lenp != lenq:
        print "length of p and q not equal."
        raise
    for i in xrange(lenp):
        hammdist += (p[i] != q[i])
    return hammdist
    

def main(filename):
    dat = readdat(filename)
    print hamming_dist(*dat)
    
    
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)