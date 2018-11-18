#This script can download file from a specified directory in an FTP server.
#Note that the filepaths are written in Windows format. Can be changed to Linux format.
#import os and ftplib from FTP library. ftplib has the necessary objects to download stuff.

import os
from ftplib import FTP

#define ftp object by specifying the main FTP site address. Do not provide full link here.
ftp=FTP("ftp.ncbi.nih.gov")
#Login - if you need username and password, you can pass them as arguments in ftp.login()
ftp.login()
#Go to your directory of interest.
ftp.cwd("/pub/yutinn/Loki_Castle_NCLDV_2018/23_bins_nt")
#Obtain the filenames as a list
filenames_list=ftp.nlst()
print filenames_list

#Now, the power of for loop. We will simply go through this list one by one and write the content of that file into local directory -recursively for each of the files.

for n in filenames_list:
	#specify what the filepath on local machine. 'n' is the recursive variable pointing to the filename in the filename_list.
	local_filename=os.path.join("C:\Users\Monir\Documents\Aureo_new_ideas\Codon analysis other giants\Loki_MG", n)
	#open this newly specified file for binary writing -'wb'
	file=open(local_filename, 'wb')
	#ftp.retrbinary method with the 'command' (RETR) will retrieve the file. And then the "callback" function file.write will write the retrived data to the file.
	#need to learn more about this command from Frank.
	#more info on this command here: https://docs.python.org/2/library/ftplib.html
	#turns out since RETR is a command, we need to make sure that the ftp.retrbinary understands the final version of the command that we create here.
	#So we need to provide a space between RETR and the file name. Then it will be "RETR x.fna" etc. Otherwise the merge and doesn't make sense.
	ftp.retrbinary('RETR '+ n, file.write)
	#close the file. Keep the loop going.
	file.close()
ftp.quit()
