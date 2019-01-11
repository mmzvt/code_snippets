#This will get the best hit from a blast outfmt 6 or other tabular result formats. Basically it just adds the first value of a line as a key to the defaultdict and then add the whole line(s) as values in list. After that, the first value of each key is accessed and printed out in a new file. THe blast out file has to be already be sorted according to 'best' hits, which blast does by default.
import sys, os, re
from Bio import SeqIO
from collections import defaultdict

blast_result=open(sys.argv[1], "r")
ref_names = open(sys.argv[2], "r")
best_hit=open(sys.argv[3], "w")

#ref_ids=[]
#for ref in ref_names.readlines():
#	ref_ids.append(ref)

# d=defaultdict(list)
# for line in blast_result.readlines():
# 	line=line.rstrip()
# 	tabs=line.split("\t")
# 	d[tabs[0]].append(line)

d=defaultdict(list)
for line in blast_result.readlines():
	line=line.rstrip()
	tabs=line.split("\t")
	d[tabs[0]].append(line)


# for k in d.keys():
# 	print d[k][0]

# print(d.keys())
for obj in d:
	best_hit.write(d[obj][0]+"\n")

	#print(d[obj][0])
blast_result.close()
ref_names.close()
best_hit.close()
