#!python
# this code is used for find one gene's expression in tumor, and the gsea of this gene
#"USAGE: python *.py genename(eg:'A2LD1|87769') cancer_file(tcga_gene_nomarlized_file)"

import sys
import re
gene = sys.argv[1]
filein = "./genes_normalized/"+sys.argv[2]        #change
out1 = open(gene.split('|')[0]+'_'+sys.argv[2].split('.')[0]+'.gct',"w")
out2 = open(gene.split('|')[0]+'_'+sys.argv[2].split('.')[0]+'.cls',"w")
genes = 0
tumor, gene2value = [], []
with open(filein) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		if re.search('Hybridization',line):
			data_copy = data
			for i in range(1,len(data)):
				tumor_type = data_copy[i].split('-')
				num = tumor_type[3][0]+tumor_type[3][1]
				if int(num) < 10:
					tumor.append(i)
			continue
		if re.search('\?',line):
			continue
		genes += 1
		if data[0] == gene:
			for i in tumor:
				gene2value.append(float(data[i]))
up = int(len(gene2value)/3)
down = int((len(gene2value)/3)*2)
value = sorted(gene2value)
label, cancer = [], []
m, n = 0, 0
for i in range(len(gene2value)):
	if gene2value[i] >= value[down]:
		m += 1
		if m > up:
			continue
		label.append('High')
		cancer.append(tumor[i])		
	elif gene2value[i] <= value[up]:
		n += 1
		if n > up:
			continue
		label.append('Low')
		cancer.append(tumor[i])
	else:
		continue
if label[0] == 'High':
	out2.write(str(len(label))+' 2 1\n# High Low\n'+'\t'.join(label)+'\n')
else:
	out2.write(str(len(label))+' 2 1\n# Low High\n'+'\t'.join(label)+'\n')
out2.close()
out1.write('#1.2\n'+str(genes)+'\t'+str(len(label))+"\n")
m = 0
with open(filein) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		tmp = []
		if re.search('\?',line):
			continue		
		if re.search('Hybridization',line):
			j = 0
			for i in cancer:
				tmp.append(data[i]+str(j))
				j += 1
			out1.write('NAME	DESCRIPTION	'+'\t'.join(tmp)+'\n')
			continue
		m += 1
		genename = data[0].split('|')
		result = genename[0] + '\t' + 'A' + str(m)
		for i in cancer:
			result = result + '\t' + data[i]
		out1.write(result+'\n')
out1.close()