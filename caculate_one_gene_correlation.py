#!python
#USAGE:python *.py gene_name cancer_file
import re
import sys
from scipy import stats
input_gene = sys.argv[1]
filein = sys.argv[2]
out = open(input_gene+'_'+filein,"w")

pos = []
cor = {}
with open(filein) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		if re.search('Hybridization',line):
			for i in range(1,len(data)):
				tumor = data[i].split('-')
				num = int(tumor[3][0]+tumor[3][1])
				if num < 10:
					pos.append(i)
			continue
		

with open(filein) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		if re.search('Hybridization',line):
			continue
		elif re.search('^\?',line):
			continue
		else:
			gene = data[0].split('|')
			cor[gene[0]] = []
			for i in pos:
				cor[gene[0]].append(float(data[i]))

out.write('gene_name\tpearson\tpvalue\n')
for i in cor:
	r, p = stats.pearsonr(cor[i], cor[input_gene])
	out.write(i+'\t'+str(r)+'\t'+str(p)+'\n')


out.close()
					