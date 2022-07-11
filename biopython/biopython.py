from Bio import SeqIO
from Bio.Emboss.Applications import NeedleCommandline


#for seq_record in SeqIO.parse("db.fa", "fasta"):
	#print(seq_record.id)
	#print(repr(seq_record.seq))
	#print(len(seq_record))
	#print(seq_record.seq)
	

needle_cline = NeedleCommandline(asequence="asequence.fa", bsequence="bsequence.fa", gapopen=10, gapextend=0.5, outfile="alineacion.txt")
print(needle_cline)

needle_cline()
with open('alineacion.txt') as f:
	output = f.readlines()
for line in output:
	if 'Score:' in line:
		 print(int(float(line[:-1].split(':')[-1].strip())))
		 
		 
Ana Velez Rueda7:42 PM
https://biopython-cn.readthedocs.io/zh_CN/latest/en/chr06.html
Ana Velez Rueda7:44 PM
https://biopython-cn.readthedocs.io/zh_CN/latest/en/chr06.html#getting-information-on-the-alignment
		 
		 
		 ftp://207.154.17.70/pub/EMBOSS/