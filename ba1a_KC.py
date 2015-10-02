#!/usr/bin/python
# File created on 11 Sep 2015

__author__ = "Kenneth Cheng"
__credits__ = ["Kenneth Cheng"]
__version__ = "0.0.1-dev"
__maintainer__ = "Kenneth Cheng"
__email__ = ""

"""
Problem Description: 
    Compute the Number of Times a Pattern Appears in a Text
    Given two strings: text and pattern.
    Return an integer: number of times pattern appears in text.
"""

import sys
import time
from rosalind_utils import readdat

def pattern_freq(text, pattern):

    txt_l = len(text)
    pat_l = len(pattern)
    freq = 0
    
    for i in xrange(txt_l - pat_l + 1):
        if text[i:i + pat_l] == pattern:
            freq += 1
            
    return freq

# Another approach with the str.find method    
def pattern_freq_v2(text, pattern):

    freq = 0
    startpoint = 0
    while True:
        startpoint = text.find(pattern, startpoint) + 1
        if startpoint > 0:
            freq += 1
        else:
            return freq

def main(filename):
    dat = readdat(filename)
    print pattern_freq(*dat)
    
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)