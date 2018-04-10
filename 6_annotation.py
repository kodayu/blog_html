#!python
import sys
from itertools import islice
filein = sys.argv[1]
fileout = open(sys.argv[2],"w")
if filein == '':
	print('laji, inputfile is needed\n')
	sys.exit()

cir, ace, ubi, pho, met, m6a, kin, onco = {}, {}, {}, {}, {}, {}, {}, {}
def file_deal(filename):
	cor = {}
	with open(filename) as f:
		for line in f:
			data = line.split('\t')
			cor[data[0]] = data[1]
	return cor

cir = file_deal("./several_gene_list_summary/circledian.list")
ace = file_deal("./several_gene_list_summary/acetylation.list")
ubi = file_deal("./several_gene_list_summary/ubiquitin.list")
pho = file_deal("./several_gene_list_summary/phosphotase.list")
met = file_deal("./several_gene_list_summary/methylation.list")
m6a = file_deal("./several_gene_list_summary/m6A_related.list")
kin = file_deal("./several_gene_list_summary/kinase.list")
onco = file_deal("./several_gene_list_summary/onco.list")
meta = file_deal("./several_gene_list_summary/metastasize_related.list")
n = 0
with open(filein) as f:
	for line in f:
		line = line.strip('\n')
		fileout.write(line+'	Circadian	Acetylation	Ubiquitin	Phosphotase	Methylation	m6A_related	Kinase	oncogene	metastasize_related\n')
		n = 2
		if n > 0:
			break

with open (filein) as f:
	for line in islice(f,1,None):
		line = line.strip('\n')
		data = line.split('\t')
		anno = []
		if data[0] in cir:
			anno.append(cir[data[0]])
		else:
			anno.append('---')
		if data[0] in ace:
			anno.append(ace[data[0]])
		else:
			anno.append('---')
		if data[0] in ubi:
			anno.append(ubi[data[0]])
		else:
			anno.append('---')
		if data[0] in pho:
			anno.append(pho[data[0]])
		else:
			anno.append('---')
		if data[0] in met:
			anno.append(met[data[0]])
		else:
			anno.append('---')
		if data[0] in m6a:
			anno.append(m6a[data[0]])
		else:
			anno.append('---')
		if data[0] in kin:
			anno.append(kin[data[0]])
		else:
			anno.append('---')
		if data[0] in onco:
			anno.append(onco[data[0]])
		else:
			anno.append('---')
		if data[0] in meta:
			anno.append(meta[data[0]])
		else:
			anno.append('---')
		result = '\t'.join(anno)
		fileout.write(line+'\t'+result+'\n')
fileout.close()