# Frequent Words Problem
# Find the most frequent k-mers in a string

def mfkmer(dna, k):

    # create a dict containing all k-mers in dna and their respective frequencies:
    kmerfreq = dict()
    for i in range(len(dna) - k + 1):
        kmerfreq[dna[i:i+k]] = kmerfreq.get(dna[i:i+k], 0) + 1

    # get the values of kmerfreq and find the maximum, i.e. frequency of the mf k-mer:
    maxfreq = max(kmerfreq.values())	
	
    # reverse lookup into kmerfreq for keys corresponding to the value maxfreq:
    for kmer in kmerfreq:
        if kmerfreq[kmer] == maxfreq:
            print kmer,
    print '\n'
	
	
fin = open('ba1b_in.txt')
dna = fin.readline().strip()
k = int(fin.readline().strip())
mfkmer(dna, k)