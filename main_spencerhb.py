import os
import os.path
import sys
import subprocess

if len(sys.argv)<2:
    print "Usage %s requires input/genefile" % (sys.argv[0])
    sys.exit()

path = sys.argv[1]
genefile = sys.argv[2]                                                         
outfile= path + "_.txt"

if os.path.isfile(path) and path.endswith(".fsa"):
    cmd = ['python', 'program_one_project_spencerhb.py', path, outfile]
    #print "X=" , cmd
    subprocess.call(cmd)
    cmd = ['python', 'program_two_project_spencerhb.py',path, 'ecoli_16s', genefile]
    subprocess.call(cmd)

if os.path.isdir(path):
    files= os.listdir(path)
    #print files
    for f in files:
        fullpath = os.path.join(path,f)
        if os.path.isfile(fullpath) and fullpath.endswith(".fsa"):
            cmd = ['python', 'program_one_project_spencerhb.py', path, outfile]
            subprocess.call(cmd)
            cmd = ['python', 'program_two_project_spencerhb.py',path, 'ecoli_16s', genefile]
            subprocess.call(cmd)
    
