import sys
from sys import argv

#read file and print in default ten lines
def readFile(file):
	with open(file) as f:
		temp = f.read().splitlines()		
		for i in range (0, 10):
			print temp[i]

#read file and print depend on the input
def readFileArgv(file,line):
	with open(file) as f:
		temp = f.read().splitlines()		
		for i in range(0, line):
			print temp[i]

try:
	script, filename, n, lines = argv
	linenumber = int(sys.argv[3])
except:
	n = None
	filename = sys.argv[1]
if n == "-n":
	readFileArgv(filename,linenumber)

else:	
	readFile(filename)