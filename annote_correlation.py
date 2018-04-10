#!python
file1 = 'tf.txt'
file2 = 'NNT_STAD.rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data.data.txt'

cor = {}
with open(file2) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		cor[data[0]] = data[1]+'\t'+data[2]

out = open('result.txt',"w")
with open(file1) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		if data[1] in cor:
			line = line+'\t'+cor[data[1]]
		else:
			line = line+'\t'+''+'\t'+''
		out.write(line+'\n')

out.close()