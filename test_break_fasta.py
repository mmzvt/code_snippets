#This script can be used to fragment the fasta records based on a specified size (window_size) and write them into a new file. Can be used to calculate different stats on fragments of the sequences. For example, can be used to eventually calculate the tetranucleotide frequence of fasta through specified sliding window. The script first breaks down the fasta based on the window size and then for ecah of these fragments, gives a record id that is original record id + fragment number (1,2,3 etc). The whole process is done iteratively for each record (rec).
import sys, os
from Bio import SeqIO
#from collections import defaultdict
raw_file=open(sys.argv[1], "r")
window_size=sys.argv[2]
output=open(sys.argv[3], "w")

pieces=[]
for rec in SeqIO.parse(raw_file, "fasta"):
	total_size=len(rec.seq)
	window=int(window_size)
	n = 0
	for pos in range(0, total_size, window):
		n +=1
		fasta_frag=str(rec.seq[pos:pos+window])
		newname=rec.id + "_"+ str(n)	 
		#prints directly to shell. Can be '>'ed to a file instead.
		print ">" + newname + "\n" + fasta_frag + "\n"


