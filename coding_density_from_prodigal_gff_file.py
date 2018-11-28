## This will do several things on the "prodigal" gff output of gene prediction on contigs. Within the first loop, it will look for lines that starts with a certain string and do operation only on those lines. For example, lines that start with "# Sequence" contain the length of the whole contig, so it will go thorugh that line to pull out the contig name and the length and store them in a dictionary. Within the same loop in the second step it will calculate the differences between the start and end of each gene predicted, and will store all these differences (coding region length) in a default dictionary for each of the contig name as the key. In the second loop, these values will be summed up and will be devided by the length of each contig to get coding density. This will be done iteratively going through each key in the dictionary.

import os, sys, re
from collections import defaultdict

fh=open("C_eustigma.out", "r")

contig_length={}
cds_length_for_each_contig=defaultdict(list)
for i in fh.readlines():
	if i.startswith("# Sequence"):
		metadata=i.rstrip()
		meta_tabs=metadata.split(": ")
		meta_tabs_v2=meta_tabs[1].split(";")
		seqlength=meta_tabs_v2[1].split("=")
		final_seqlength=seqlength[1]
		final_seqlength=float(final_seqlength)
		seqname_v1=meta_tabs_v2[2].split("=\"")
		seqname_v2=seqname_v1[1].split(" ")
		final_seqname=seqname_v2[0]
		#print seqlength_final
		#print final_seqname
		#do something
		contig_length[final_seqname]=final_seqlength
		#print contig_length
	elif i.startswith("#"):
		pass
	#elif i.startswith("# Model"):
	#	pass
	else:
		line = i.rstrip()
		tabs =line.split("\t")
		contig_name=tabs[0]
		CDS_end=tabs[4]
		CDS_start=tabs[3]
		CDS_length=float(tabs[4])- float(tabs[3])
		cds_length_for_each_contig[contig_name].append(CDS_length)

coding_density_file=open("coding_density", "w")
	
for k in cds_length_for_each_contig:
	value_list=cds_length_for_each_contig[k]
	coding_density_total=sum(value_list)
	length=contig_length[k]
	final_ratio=(coding_density_total/length)*100
	final_result = k + "\t" + str(coding_density_total) + "\t" + str(length) + "\t" + str(final_ratio) +"\n"
#	print k, coding_density_total, final_ratio
	coding_density_file.write(final_result)

coding_density_file.close()
