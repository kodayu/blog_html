#!python
# USAGE 'Please input gmt file and merged file, and pathway type, followed by output file')
import sys
from itertools import islice
#depend on exactly the situation to descion whether use these		
'''
gseafile = 'gsealist.txt'
gsea = []
with open(gseafile) as f:
	for line in f:
		line = line.strip('\n')
		gsea.append(line)
'''
#read gmt file and transfer it to gene>pathway form.
cor = {}
with open(sys.argv[1]) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		for i in range(2,len(data)):
			if data[0] in gsea:
				if data[i] in cor:
					cor[data[i]] = cor[data[i]] + ";" + data[0]
				else:
					cor[data[i]] = data[0]

#deal with the annotation file
#read title
out = open(sys.argv[4],"w")
with open(sys.argv[2]) as f:
	for line in f:
		line = line.strip('\n')
		out.write(line+"\t"+sys.argv[3]+'\n')
		break
#add annotation
with open(sys.argv[2]) as f:
	for line in islice(f,1,None):
		line = line.strip('\n')
		data = line.split('\t')
		if data[1] in cor:                             #annotation file gene symbol position
			out.write(line + "\t" + cor[data[1]] + "\n")
		else:
			out.write(line + "\t" + "\n")
out.close()