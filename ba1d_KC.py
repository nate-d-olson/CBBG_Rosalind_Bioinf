# Find all occurrences of a pattern in a string

def loc(pattern, string):
    
	# from the beginning to the end, find substring with length len(pattern) in string. If substring eq pattern then print the index:
	patlen = len(pattern)
	for i in range(len(string) - patlen + 1):
	    if pattern == string[i:i + patlen]:
		    print i,
	print '\n'

fin = open('ba1d_in.txt')
pattern = fin.readline().strip()
string = fin.readline().strip()
loc(pattern, string)
