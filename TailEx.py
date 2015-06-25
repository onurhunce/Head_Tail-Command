import sys
from sys import argv

#reading with default value
def readFile(file):
	with open(file) as f:
		#f.seek(-37,2)
		temp = f.read().splitlines()
		start_point = len(temp) - 10
		for lines in range(start_point,len(temp)):
			print temp[lines]

#reading depending on the user' input	
def readFileArgv(file,line):
	with open(file) as f:
		temp = f.read().splitlines()
		start_point = len(temp) - line
		for lines in range(start_point,len(temp)):
			print temp[lines]		

try:
	script,filename,n,lines=argv
	linenumber=int(sys.argv[3])
except:
	n="none"
	filename=sys.argv[1]
if n=="-n":
	readFileArgv(filename,linenumber)

else:	
	readFile(filename)