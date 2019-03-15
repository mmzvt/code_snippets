import os, sys, re
from collections import defaultdict

input_file=open(sys.argv[1], "r")
output_file=open(sys.argv[2], "w")
output_file.write(str("Contig_name"+"\t"+"Num_viral_hits"+"\t"+"Num_prok_hits"+"\t"+"Num_euk_hits"+"\t"+"Percent_viral_hits"+"\t"+"Percent_prok_hits"+"\t"+"Percent_euk_hits"+"\n"))

test_dict=defaultdict(list)

for i in input_file.readlines():
	line = i.rstrip()
	tabs= line.split("\t")
	what_i_want=tabs[4]
	dict_key=tabs[0].split("_")
	test_dict[dict_key[0]].append(what_i_want)

for key in test_dict:
	count_virus=0
	count_prok =0
	count_euk =0
	length=len(test_dict[key])
	for v in test_dict[key]:
		if v == "Viruses":
			count_virus +=1
		elif v=="Eukaryota":
			count_euk +=1
		elif v== "Bacteria" or v == "Archaea":
			count_prok +=1
	proportion_virus = (round(float(count_virus),2)/round(float(length),2))*100
	proportion_virus= round(float(proportion_virus),2)

	proportion_prok = (round(float(count_prok),2)/round(float(length),2))*100
	proportion_prok=round(float(proportion_prok),2)

	proportion_euk = (round(float(count_euk),2)/round(float(length),2))*100
	proportion_euk=round(float(proportion_euk),2)

	output= str(key)+"\t"+str(count_virus)+"\t"+str(count_prok)+"\t"+str(count_euk)+"\t"+str(length)+"\t"+str(proportion_virus)+"\t"+str(proportion_prok)+"\t"+str(proportion_euk)+"\n"
	
	output_file.write(output)

#header= "Contig_name", "\t", "Num_viral_hits", "\t", "Num_prok_hits", "\t", "Num_euk_hits", "\t", "Percent_viral_hits", "\t", "Percent_prok_hits", "\t", "Percent_euk_hits"
	
