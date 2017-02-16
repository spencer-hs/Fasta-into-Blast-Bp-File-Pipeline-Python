import sys
import os.path
import subprocess

if len(sys.argv)<4:
    print "USAGE: python %s requires assembly/name/fasta" % (sys.argv[0])
    sys.exit()
assemfasta= sys.argv[1]
projname=sys.argv[2]
genefasta= sys.argv[3]
outputfile= assemfasta+"_"+ projname +"_extracted.fa"
OFH=open(outputfile,"w")

cmd = ['formatdb','-i',assemfasta,'-p','F']
subprocess.call(cmd)
output= assemfasta + "_out.blast"

cmd =['blastall','-d',assemfasta,'-i', genefasta,'-o',output,'-p','blastn','-e'\
, '1e-15']
subprocess.call(cmd)
blastoutput= assemfasta + "_out.bp"
cmd= ['perl','/home/nsheth/Util/use/useParse.pl',output]
subprocess.call(cmd)
output= assemfasta + "_out.bp"
#print output           
BOFH= open(output)

for line in BOFH:
    if line.startswith(">"):
        list=line.split("|")
        seqid= list[0]
        #print seqid                                                            
    if line.startswith("SUB"):
        list2= line.split()
        seqnum= list2[0]
        #print seqnum 
        number = seqnum.split(":")
        num= number[1]
        #print num                                                              
    elif line.startswith("qb"):
        list3= line.split()
        #print list3                                                            
        startpos = list3[2]
        startpos2= startpos.split(":")
        startnum= startpos2[1]
        endpos=list3[3]
        endpos2= endpos.split(":")
        endnum= endpos2[1]
        length= list3[8]
        #print startnum                    
        #print endnum                                                           
AFH= open(assemfasta)
for line in AFH:
    line= line.strip()
    if num in line :
       sequence = next(AFH)
       print >> OFH, "%s | %s | %s | %s | %s\n%s" % (assemfasta, seqid ,length, startnum , endnum ,sequence)
