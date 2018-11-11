
#This script can be used to change the IDs in a multi-fasta file and the records with modified IDs can be written in a new fasta file.
# The original identifiers of my fasta was in the following format:
#lcl|XXXXXXXXXXXXX [locus_tag=AaXXXX] [protein=XXXXXXXXXXXX] [protein_id=XXXXXXXXX] [location=XXXX..XXXX] [gbkey=CDS]
#I wanted the locus_tag as the new identifier in place of the "lcl|XXXX..." id. Basically split the fasta record 'description' by tabs and take the tab that contains the locus tag. 
# Note that this is not an elegant script. Smart methods might exist which could directly take the value of the locus_tag and put it as fasta identifier. But I am new at Python.
#Hope this helps!

import os, sys
from Bio import SeqIO

#Open the file handle of fasta file.

AaV_fasta=open("AaV_CDS.fasta", "r")

#Initiate a list to put the fasta records with modified IDs.
AaV_records = []

#Recursive modification begins...

for i in SeqIO.parse(AaV_fasta, "fasta"):

#take the description of each fasta record iterator
	
  desc=i.description
  
  #Keep splitting it until you get the desired string
  
	desc_tabs=desc.split(" ")
	
  #print desc_tabs[1]
	
  desc_tabs_v2=desc_tabs[1].split("=")
	desc_tabs_v3=desc_tabs_v2[1].split("]")
  
  #replace the orignial ID with the new ID
	
  i.id=desc_tabs_v3[0]
	print i.id
  
  #Append all the records with modified ID in the list
	
  AaV_records.append(i)
  
#Write fasta file
SeqIO.write(AaV_records, "AaV_CDS_mod_names.fasta", "fasta")
