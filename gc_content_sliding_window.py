import sys, os
from Bio import SeqIO
from Bio.SeqUtils import GC

raw_file=open(sys.argv[1], "r")
window_GC = open(sys.argv[2], "w")
window_size=sys.argv[3]

pieces=[]
#window_GC=[]
for rec in SeqIO.parse(raw_file, "fasta"):
	total_size=len(rec.seq)
	window_size=int(window_size)
	chunksize=total_size//window_size
	for pos in range(0, total_size, window_size):
		pieces.append(str(rec.seq[pos:pos+window_size]))
#print pieces
	for small_chunk in pieces:
		gc_content=GC(small_chunk)
		window_GC.write(str(gc_content)+"\n")
#print chunksize
#print total_size//2000
window_GC.close()
#print window_GC
