from scipy.stats import ttest_rel
from itertools import islice
import sys
import re
import math

if sys.argv[1] == '':
	print ("USAGE: data_matrix output_file")
	sys.exit()
def correct_pvalues_for_multiple_testing(pvalues, correction_type = "Benjamini-Hochberg"):
	from numpy import array, empty
	pvalues = array(pvalues)
	n = float(pvalues.shape[0])
	new_pvalues = empty(int(n))
	if correction_type == "Bonferroni":
		new_pvalues = n * pvalues
	elif correction_type == "Bonferroni-Holm":
		values = [ (pvalue, i) for i, pvalue in enumerate(pvalues) ]
		values.sort()
		for rank, vals in enumerate(values):
			pvalue, i = vals
			new_pvalues[i] = (n-rank) * pvalue
	elif correction_type == "Benjamini-Hochberg":
		values = [ (pvalue, i) for i, pvalue in enumerate(pvalues) ]
		values.sort()
		values.reverse()
		new_values = []
		for i, vals in enumerate(values):
		    rank = n - i
		    pvalue, index = vals
		    new_values.append((n/rank) * pvalue)
		for i in range(0, int(n)-1):
		    if new_values[i] < new_values[i+1]:
		        new_values[i+1] = new_values[i]
		for i, vals in enumerate(values):
		    pvalue, index = vals
		    new_pvalues[index] = new_values[i]
	return new_pvalues

merge = sys.argv[1]             #input filename
out = open(sys.argv[2],"w")     #output filename
with open(merge) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		out.write(line + '	logFC	tvalue	pvalue	p.adj	label'+'\n')
		break

pvalue, tvalue, fc, text = [], [], [], []
control_position = [6,7,8]                       #control data position
test_position = [9,10,11]                        #test data position
with open (merge) as f:
	for line in islice(f,1,None):
		line = line.strip('\n')
		data = line.split('\t')
		m, n, te, nc = 0, 0, 0, 0
		tes, nco = [], []
		for i in control_position:                   #control
			if (data[i] != ''):
				data[i] = float(data[i])
				#data[i] = math.log10(data[i])
				m += 1
				nc += math.log2(data[i]+1)
				nco.append(math.log10(data[i]+1))
		for i in test_position:                              #test
			if (data[i] != ''):
				data[i] = float(data[i])
				#data[i] = math.log10(data[i])
				n += 1
				te += math.log2(data[i]+1)
				tes.append(math.log10(data[i]+1))
		if ((m >= 2)and(m == n)):
			foldchange = te - nc                         #log2 test/control
			t, p = ttest_rel(tes, nco)			
		else:
			continue
		pvalue.append(p)
		tvalue.append(t)
		fc.append(foldchange)
		text.append(line)

padj = correct_pvalues_for_multiple_testing(pvalue)
for i in range(len(pvalue)):
	if padj[i] < 0.05:
		if 2**fc[i] < 0.5:
			label = 'Down'
			out.write(text[i] + '\t' + str(fc[i]) + '\t' + str(tvalue[i]) + '\t' + str(pvalue[i]) + "\t" + str(padj[i]) + "\t" + label + '\n')
		elif 2**fc[i] > 2:
			label = 'Up'
			out.write(text[i] + '\t' + str(fc[i]) + '\t' + str(tvalue[i]) + '\t' + str(pvalue[i]) + "\t" + str(padj[i]) + "\t" + label + '\n')
		else:
			label = 'Not'
			out.write(text[i] + '\t' + str(fc[i]) + '\t' + str(tvalue[i]) + '\t' + str(pvalue[i]) + "\t" + str(padj[i]) + "\t" + label + '\n')
	else:
		label = 'Not'
		out.write(text[i] + '\t' + str(fc[i]) + '\t' + str(tvalue[i]) + '\t' + str(pvalue[i]) + "\t" + str(padj[i]) + "\t" + label + '\n')

out.close()