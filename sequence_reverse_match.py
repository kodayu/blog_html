#!python
#USAGE: python *.py fasta_file output_file
#only support one fasta sequence
import sys
import re
cor = {}
cor['a'] = 't'
cor['c'] = 'g'
cor['t'] = 'a'
cor['g'] = 'c'
cor['A'] = 'T'
cor['C'] = 'G'
cor['T'] = 'A'
cor['G'] = 'C'
filein = sys.argv[1]
fileout = open(sys.argv[2],"w")
sequence = []
with open(filein) as f:
	for line in f:
		line = line.strip('\n')
		if re.search('>',line):
			fileout.write(line+'\n')
			continue
		sequence.append(line)

fasta = ''.join(sequence)
rever = fasta[::-1]
data = []
for i in rever:
	data.append(cor[i])
fileout.write(''.join(data))
fileout.close()
	