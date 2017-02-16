import sys
import re
import math

if len(sys.argv) <3:
    print "Usage: python %srequires input seq_id output" % sys.argv[0]
    sys.exit()

infile=sys.argv[1]
outfile= sys.argv[2]
outfile= infile + "_.txt"

INFH= open(infile)
OFH= open(outfile, 'w')

seq_count=0
total_length=0
gc_count=0
N50_counter=0
n50=0
list=[]
list2=[]
list3=[]
for line in INFH:
    line= line.strip()
    if line.startswith(">"):
        seq_count +=1
#        print "Seq count= %d" % (seq_count)                                    
    else:
        sequence=line
        length=len(sequence)
        if length >0:
            total_length+= length
            average_length= float(total_length)/seq_count
            list.append(length)
            minimum= min(list)
            maximum= max(list)
        for letter in sequence:
            if letter == 'G' or letter == 'C':
                gc_count+=1
                if gc_count >0:
                    gc_percent= (float(gc_count)/total_length)* 100
n_2= float(total_length)/2

for num in sorted(list, reverse=True):
    n50=n50+num                                                              

    list2.append(num)
    #print list2                                                                
    if n50>= n_2:
         small= str(num)
         N50_counter+=1
         list3.append(n50)
         length3=len(list3)
         #print list3                                                              
average= float(n50/N50_counter)   

#print n_2                    
print >> OFH,  "Number of Sequences= %d" % (seq_count)
#print "Length= %d" % (length)                                               
print >> OFH, "Total Length of Sequences in Fasta File= %d" % (total_length)
print >> OFH, "GC Count of all Sequences= %d" % (gc_count)
print >> OFH, "GC Content Percent = %f %%" % (gc_percent)
print >> OFH,"Average Contig Size = %.3f" % (average_length)
print >> OFH, "Minimum Contig Size= %d" % (minimum)
print >> OFH, "Maximum Contiq Size= %d" % (maximum)
print >> OFH, "Number of N50=", N50_counter
print >> OFH, "N50 Contig Size=", small
print >> OFH, "N50 Contig Average Length= ", float(average)
