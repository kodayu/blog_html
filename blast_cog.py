import sys
import re

if sys.argv[1] == '':
	print ("Please input blast.out fun.txt whog annotationfile")
	sys.exit()
	
blast = sys.argv[1]
fun = sys.argv[2]
whog = sys.argv[3]
out = open(sys.argv[4],"w")
out.write('query acc.ver	subject acc.ver	% identity	alignment length	mismatches	gap opens	q. start	q. end,	s. start	s. end	evalue	bit score	classification	description\n')
cog_class = {}
with open(whog) as f:
	for line in f:
		line = line.strip('\n')
		if re.search(r'^\[',line):
			la = re.match(r'\[(\w+)\]',line)
			label = la.group(1)
		elif re.search(r':',line):
			ha = re.split(r'\s\s',line)
			cogname = ha[2]
			cog = cogname.split(' ')
			for i in cog:
				cog_class[i] = label
		else:
			continue

class_des = {}
with open(fun) as f:
	for line in f:
		line = line.strip('\n')
		if re.search(r'\[',line):
			data = re.split(r'(\s\[)|(\]\s)',line)
			class_des[data[3]] = data[6]
		else:
			continue
					
pro = []
with open(blast) as f:
	for line in f:
		line = line.strip('\n')
		if re.search(r'^#',line):
			continue
		data = line.split('\t')
		if data[0] not in pro:
			des = ''
			pro.append(data[0])
			for i in cog_class[data[1]]:
				des += class_des[i] + ";"
			out.write(line + "\t" + cog_class[data[1]] + "\t" + des + "\n")     #add a class and a description
		else:
			continue
out.close()
