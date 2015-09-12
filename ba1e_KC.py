#!/usr/bin/python
# File created on 11 Sep 2015

__author__ = "Kenneth Cheng"
__credits__ = ["Kenneth Cheng"]
__version__ = "0.0.1-dev"
__maintainer__ = "Kenneth Cheng"
__email__ = ""

"""
Definition:
    Given integers L and t, a string pattern forms an (L, t)-clump inside a (larger) string genome
    if there is an interval of genome of length L in which pattern appears at least t times.

Problem Description: 
    Clump Finding Problem
    Given: A string genome, and integers k, L, and t.
    Return: A non-repetive list of all k-mers forming (L, t)-clumps in genome.
"""

import sys
import time
from collections import defaultdict
from rosalind_utils import readdat

def ltclumps(genome, k, l, t):

    # create a defaultdict to store all positions each k-mer appears,
    # kmer_pos's keys are the distinct k-mers in genome,
    # kmer_pos's values are lists of where the corresponding k-mer appears;
    # and create a list to keep all distinct k-mers that are (L,t)-clumps in genome:
    kmer_pos = defaultdict(list)
    hits = []
    for i in range(len(genome) - k + 1):
        kmer_pos[genome[i:i+k]].append(i)
    
    # loop through all the distinct k-mers in genome:
    for kmer in kmer_pos:
        
        # kmer_pos[kmer] is the list recording all the positions that k-mer appears in genome,
        # the positions are represented by indexes genome in ascending order.
        # len(kmer_pos[kmer]) is the number of times that k-mer appears in genome.
        
        # if k-mer appears in genome less than t times, then it can't be a hit; go to next k-mer:
        if len(kmer_pos[kmer]) < t:
            continue
        
        # else, k-mer could be a hit, scan through k-mer's position list, i.e. kmer_pos[kmer].
        # calculate the bp distances between all pairs of every (k - 1)th occurrence of k-mers,
        # which is kmer_pos[kmer][i + t -1] - kmer_pos[kmer][i] + k.
        # as long as we find one of the distances <= l, then the k-mer is a hit,
        # we append it to the list of hits, and break the loop
        for i in range(len(kmer_pos[kmer]) - t + 1):
            if kmer_pos[kmer][i + t -1] - kmer_pos[kmer][i] + k <= l:
                hits.append(kmer)
                break
    
    return hits

# A second but similar approach:
def ltclumps2(genome, k, l, t):

    """
    this approach follows the same idea as the previous method, but the same time as it builds up 
    the kmer_pos default dictionary, it begins to check whether the k-mer being added to kmer_pos 
    could be a hit (at the current time point).
    once a k-mer is identified as a hit, we don't record its positions of further occurrences.
    """
    
    kmer_pos = defaultdict(list)
    hits = []
    
    for i in range(len(genome) - k + 1):
    
        kmer = genome[i:i+k]
        
        if kmer in hits:
            continue
            
        cur_pos_list = kmer_pos[kmer]
        cur_pos_list.append(i)
        len_cpl = len(cur_pos_list)
        
        if len_cpl > t and cur_pos_list[len_cpl - 1] - cur_pos_list[len_cpl - t] + k <= l:
            hits.append(kmer)
            
    return hits

def main(filename):
    dat = readdat(filename)
    genome = dat[0]
    k = int(dat[1])
    l = int(dat[2])
    t = int(dat[3])
    print 'Approach 1:'
    startt = time.clock()
    print ltclumps(genome, k, l, t)
    endt = time.clock()
    print 'Wall time /sec:', endt - startt
    # this don't work: timeit.repeat('ltclumps(genome, k, l, t)', setup='from __main__ import ltclumps', repeat=3, number=100)
    print 'Approach 2:'
    startt = time.clock()
    print ltclumps2(genome, k, l, t)
    endt = time.clock()
    print 'Wall time /sec:', endt - startt
    # this don't work: timeit.repeat('ltclumps2(genome, k, l, t)', setup='from __main__ import ltclumps2', repeat=3, number=100)
    
    
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)