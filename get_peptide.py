import os
import itertools
import re
##a function to substr peptides
def peptide(a,b,c,d): ##a-position;b-range;c-full_length;d-protein_sequence
	pep = ""   ##define the null first
	for i in range((a-b-1),(a+b),1):
		if (i<0 or i>c-1):
			pep += "-"              #'-' instead of null data
		else:
			pep += d[i]
	return pep
#get_peptides
peptidefile = open ('gsh_peptide.txt',"w")         #define the output file
with open('gsh.fastaR') as f:                      #read the fastaR file
	for line1,line2 in itertools.izip_longest(*[f]*2):
		line2 =line2.strip('\n')
		pos_all = re.search('\t[\d,]+\n',line1)
		pos_a = re.sub('[\t\n]','',pos_all.group())
		pos_a = str(pos_a)
		pos = pos_a.split(',')
		line2_l = len(line2)
		for num in pos:
			num = int(num)
			result = peptide(num,15,line2_l,line2)
			peptidefile.write(result + "\t" + "1" + "\n")
		for i in range(1,line2_l+1):
			if line2[i-1] in ['C']:                          #it depends on what you want to research
				if (str(i) not in pos):
					result1 = peptide(i,15,line2_l,line2)
					peptidefile.write(result1 + "\t" + "0" + "\n")
peptidefile.close()
