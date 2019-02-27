import os, sys, re
from Bio import SeqIO

summary=open(sys.argv[1], "r")
target_folder=sys.argv[2]

replicon_list=[]
for i in summary.readlines():
	line = i.rstrip()
	tabs=line.split("\t")
	replicon=tabs[1]
	replicon_list.append(replicon)

for i in os.listdir(target_folder):
	if i.endswith(".fna"):
		contig_list=[]
		path=os.path.join(target_folder, i)
		for j in SeqIO.parse(path, "fasta"):
			if j.id in replicon_list:
				contig_list.append(j)
		newname=re.sub(".fna",".viral.fna",i)
		handle=open(newname, "w")
		SeqIO.write(contig_list, handle, "fasta")		






