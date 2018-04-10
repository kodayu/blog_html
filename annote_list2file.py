#!python
file1 = 'tf.txt'
file2 = 'NNT_STAD.rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data.data.txt'

tf = []
with open(file1) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		if data[1] not in tf:
			tf.append(data[1])

out = open('result.txt',"w")
with open(file2) as f:
	for line in f:
		line = line.strip('\n')
		data = line.split('\t')
		if data[0] in tf:
			line = line+'\t'+'TF'
		else:
			line = line+'\t'+''
		out.write(line+'\n')

out.close()