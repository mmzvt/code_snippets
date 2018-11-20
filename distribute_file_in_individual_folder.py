import os, sys,re
import subprocess, shlex

input_folder="test_1"

for i in os.listdir(input_folder):
	prefix=re.sub(".faa", "", i)
	new_folder=os.path.join(input_folder, prefix)
	try:
		os.mkdir(new_folder)
	except:
		pass
	cmd = "cp " + os.path.join(input_folder, i) + " -t "+new_folder
	print cmd
	cmd2 = shlex.split(cmd)
	print cmd2
	subprocess.call(cmd2)

