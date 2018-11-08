##This small code takes a file with cells separated by tabs. The value of a particular cell can be modified and printed out.
import os, sys, re

original_file=open("all_hmm_out.speci.txt", "r")

output_file=open("all_hmm_out_modified_names.txt", "w")

modified_rows=[]

for i in original_file:
		original_line=i.rstrip()
		tab_sep_lines=original_line.split("\t")
		uscore_sep_sampleID=tab_sep_lines[1].split("_")
		modified_id=uscore_sep_sampleID[0]+"_"+tab_sep_lines[0]
		modified_entire_line=modified_id+"\t"+tab_sep_lines[2]+"\t"+tab_sep_lines[3]+"\t"+tab_sep_lines[4]+"\t"+tab_sep_lines[5]
		
		print (modified_entire_line)
