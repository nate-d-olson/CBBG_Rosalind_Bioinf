# Reverse Complement Problem
# Find the reverse complement of a DNA string

def rvcp(dna):
    
	# build a dict for the complementary replacement:
	cmpl = {'A':'T', 'T':'A', 'C':'G', 'G':'C'} # so dna string should be in uppercase
	
	# read dna bp by bp from the end, use cmpl for complement, and append to dna_rvcp:
	dna_rvcp = ''
	i = len(dna) - 1
	while i >= 0:
	    dna_rvcp = dna_rvcp + cmpl[dna[i]]
	    i=i-1
	
	return dna_rvcp

fin = open('ba1c_in.txt')
dna = fin.readline().strip()
print rvcp(dna)
