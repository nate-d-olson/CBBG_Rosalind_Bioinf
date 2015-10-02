#!/usr/bin/python
# File created on Oct 1, 2015

__author__ = "Kenneth Cheng"
__credits__ = ["Kenneth Cheng"]
__version__ = "0.0.1-dev"
__maintainer__ = "Kenneth Cheng"
__email__ = ""

"""
Definition:
    We say that a k-mer Pattern appears as a substring of Text with at most d mismatches 
    if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern,
    i.e., HammingDistance(Pattern, Pattern') <= d. 

Problem Description: 
    Approximate Pattern Matching Problem
    Given: Strings Pattern and Text along with an integer d.
    Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
"""

import sys
from rosalind_utils import readdat
from ba1g_KC import hamming_dist

# Approach 1:
  
def approx_pat_posi(pattern, text, d):

    posilist = []
    lenp = len(pattern)
    lent = len(text)
    d = int(d)
    
    for i in xrange(lent - lenp + 1):
        if hamming_dist(text[i:i + lenp], pattern) <= d:
            posilist.append(str(i))
            
    return ' '.join(posilist)
    

def main(filename):
    dat = readdat(filename)
    with open('ba1h_out.txt', 'w') as fout:
        fout.write(approx_pat_posi(*dat))
    
    
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)