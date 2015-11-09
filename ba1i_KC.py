#!/usr/bin/python
# File created on Nov 05, 2015

__author__ = "Kenneth Cheng"
__credits__ = ["Kenneth Cheng"]
__version__ = "0.0.1-dev"
__maintainer__ = "Kenneth Cheng"
__email__ = ""

"""
Definition:

Problem Description: 
    Find the most frequent words with mismatches in a string.
    Given: Strings Text along with integers k and d.
    Return: All most frequent k-mers with up to d mismatches in Text.
"""

import sys
from rosalind_utils import readdat
from ba1g_KC import hamming_dist
from ba1k_KC import permutdna
from collections import defaultdict

# Approach 1 (dummy's approach):
  
def maxfreq_mm(seq, k, d):
    k = int(k)
    d = int(d)
    seql = len(seq)
    freq_dict = defaultdict(int)
    for kmer in permutdna(k):
        for i in xrange(seql - k + 1):
            if hamming_dist(kmer, seq[i:i + k]) <= d:
                freq_dict[kmer] += 1
    
    maxfreq = max(freq_dict.values())
    
    for kmer in freq_dict:
        if freq_dict[kmer] == maxfreq:
            print kmer,
    

def main(filename):
    dat = readdat(filename)
    maxfreq_mm(*dat)
    
    
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)