#Suppose, you are making a tree with a fasta file. The sequence names should have some information regarding the species/genus of the sequence.
#Most of the time,the sequence names are just GI/accession numbers - so after the tree is made, it is hard to tell which sequence belongs to which organism/virus etc. For this reason, we attempt to modify the fasta headers of the reference sequences to be used for tree building. We create a dictionary from two lists - one list contain the original fasta reference names. another list has the abbreviated species/virus name corresponding to this header. After that, we attach the 'value' of each of the keys in the dictionary to the corresponding fasta header in the reference fasta file. This code will take care of such scenario.


import sys, os, re
from Bio import SeqIO

guide=open("VLTF3_ref_abbr_names", "r")
fasta_file=open("VLTF3_ref_candidate_combined.faa", "r")


abbr=[]
seqname=[]

for i in guide.readlines():
	line=i.rstrip()
	tabs=line.split("\t")
	#print tabs
	abbr.append(tabs[0])
	seqname.append(tabs[1])
#print abbr
#print seqname

abbriviations_dict=dict(zip(seqname,abbr))
#print abbriviations_dict

seqList=[]
for ff in SeqIO.parse(fasta_file, "fasta"):
	if ff.id in abbriviations_dict:
		x=ff.id+"_"+abbriviations_dict[ff.id]
		ff.id=x
		seqList.append(ff)
	#print seqList
SeqIO.write(seqList, "test_seqs.faa", "fasta")
