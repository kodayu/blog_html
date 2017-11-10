#!python
# this code is used for find one gene's expression in tumor, and the gsea of this gene
#"USAGE: python *.py genename(eg:'A2LD1|87769') cancer_file(tcga_gene_nomarlized_file)"

import sys
import re
from numpy import median
gene = sys.argv[1]
filein = "./genes_normalized/"+sys.argv[2]        #change
out1 = open(gene+'_'+sys.argv[2]+'.gct',"w")
out2 = open(gene+'_'+sys.argv[2]+'.cls',"w")
cor = {}
genes = 0
with open(filein) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		if re.search('Hybridization',line):
			del data[0]
			data_copy = data
			continue
		if re.search('\?',line):
			continue
		genes += 1
		if data[0] == gene:
			del data[0]
			for i in range(len(data)):
				tumor_type = data_copy[i].split('-')
				num = tumor_type[3][0]+tumor_type[3][1]
				if int(num) < 10:
					cor[data_copy[i]] = float(data[i])		
med = median(list(cor.values()))
label = []
for i in cor.keys():
	if cor[i] >= med:
		label.append('High')
	else:
		label.append('Low')
out2.write(str(len(label))+' 2 1\n# High Low\n'+'\t'.join(label)+'\n')
out2.close()
position = []
out1.write('#1.2\n'+str(genes)+'\t'+str(len(label))+"\n")
m = 0
with open(filein) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		if re.search('\?',line):
			continue		
		if re.search('Hybridization',line):
			out1.write('NAME	DESCRIPTION	'+'\t'.join(cor.keys())+'\n')
			for i in cor.keys():
				for j in range(len(data)):
					if data[j] == i:
						position.append(j)
			continue
		m += 1
		genename = data[0].split('|')
		result = genename[0] + '\t' + 'A' + str(m)
		for i in position:
			result = result + '\t' + data[i]
		out1.write(result+'\n')
out1.close()