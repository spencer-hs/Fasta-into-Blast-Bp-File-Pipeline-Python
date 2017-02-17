# Fasta-into-Blast-Bp-File-Pipeline-Python
Calculating the metrics for an input fasta file, formatting an assembly fasta file for blast, blast input gene fasta file to assembly blastdb, parse blast output file into .bp file, parse .bp file to identify hits, extract those hits from assembly fasta file and output them in output file .

The three programs were written to the following specifications:
Main program will accept one fasta file or directory name which has .fsa (fasta) files. All programs must accept appropriate input and output parameters from command-line. Please put usage statements and exit statements for all programs. 

Input/Output to Main Program:
-Input = this can be asssembly fasta file or directory name with .fsa files 
-Gene File = gene file  (ex. ecoli_16S.fa)

Main program solves below problems for input fasta file(s).
1)Please calculate below metrics for input fasta file. Please accept input and output parameters from command-line. 
No of Sequences = No of sequences in fasta file 
Total Sequence Length = Total sum of all nts in the fasta file
GC Total = G and C count
GC Perc = GC % of entire fasta file
Avg Contig Size =  Average Sequence Size (Total/number of seq)
Min Contig Size = Minimum Sequence Size
Max Contig Size = Maximum Sequence Size
Total N50 contigs = No of largest contigs/sequences to cover 50% of Total sequence length 
N50ContigSize = Size of smallest contig of N50 contigs
N50Avg = Average size of N50 contigs

2)Please blast input gene fasta file to input assembly fasta  file to identify gene hits and then extract hit sequences from the assembly fasta file. Please accept below input and output file names from command-line.
    1)Assembly fasta file 
    2)project-name   (use ecoli_16s)
    3)Gene fasta file  Use this data/assemblies/ecoli_16s.fa from command-line.


The programs proceeds in the following way: 

1)Format assembly fasta file for blast
formatdb -i fastafile -p F 

2)Blast input gene fasta file to assembly blastdb. Please use .blast extension 
for your output file in below command. 
blastall -d fastafile -i gene file -o output file -p blastn -e 1e-15 : last part exactly this 

3)Parse blast output file into .bp file  
/home/spencerhb/Util/use/useParse.pl  blastoutput file 
useParse.pl  accepts  file with .blast extention and generates .bp file

4)Parse .bp file to identify hits.

5)Extract those hits from assembly fasta file and output them in output file 
Output file name = inputname_projectname_extracted.fa

6)Format of output fasta file will be below
>name of input fasta file|sequence id|sequence length|hit-start|hit-end
 extracted sequence
