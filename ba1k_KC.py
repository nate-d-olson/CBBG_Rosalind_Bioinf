#!/usr/bin/python
# File created on Oct 3, 2015

__author__ = "Kenneth Cheng"
__credits__ = ["Kenneth Cheng"]
__version__ = "0.0.1-dev"
__maintainer__ = "Kenneth Cheng"
__email__ = ""

"""
Definition:
    Given an integer k, we define the frequency array of a string Text as an array of length 4**k,
    where the i-th element of the array holds the number of times that the i-th k-mer
    (in the lexicographic order) appears in Text

Problem Description:
    Computing a Frequency Array
    Given: A DNA string Text and an integer k.
    Return: The frequency array of k-mers in Text.
"""

import sys
from rosalind_utils import readdat
from ba1a_KC import pattern_freq_v2

# Approach 1:


# generate all k-mers possible in lexicographic order:
def permutdna(n):
    if n == 1:
        return (base for base in 'ACGT')
    return (dna + base for dna in permutdna(n - 1) for base in 'ACGT')


# calculate frequency array:
def freq_array(dna, k):
    k = int(k)
    return (pattern_freq_v2(dna, pattern) for pattern in permutdna(k))


# Approach 2 (directly copied from sb. else's code):
def patternToNumber(pattern):
    letter_value = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    total = 0
    for i in range(len(pattern)):
        # grab the letters from the rear ([-(i+1)]) for increasing i's
        # and multiply it's value by the position it's in
        total += letter_value[pattern[-(i + 1)]] * len(letter_value)**(i)
    return total


def computingFrequencies(text, k):
    array = [0] * ((4**k))
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        j = patternToNumber(kmer)
        array[j] += 1
    return ' '.join(str(x) for x in array)


def main(filename):
    dat = readdat(filename)
    with open('ba1k_out.txt', 'w') as fout:
        for item in freq_array(*dat):
            fout.write(str(item) + ' ')


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
