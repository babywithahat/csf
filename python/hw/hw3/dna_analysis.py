# Name: Alejandro 
# Evergreen Login: chaveza
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

seq = ""
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    if linenum % 4 == 2:
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

total_count = 0
gc_count = 0
at_count = 0
g_count = 0
c_count = 0
a_count = 0
t_count = 0

for bp in seq:
    total_count = total_count + 1

    if bp == 'C' or bp == 'G':
        gc_count = gc_count + 1
    if bp == 'A' or bp == 'T':
        at_count = at_count + 1
    if bp == 'G':
        g_count = g_count + 1
    if bp == 'C':
        c_count = c_count + 1
    if bp == 'A':
        a_count = a_count + 1
    if bp == 'T':
        t_count = t_count + 1

#Calculation
gc_content  = float(gc_count) / total_count
at_content  = float(at_count) / total_count
sum_count   = g_count + c_count + a_count + t_count
seq_length  = len(seq)
atgc_ratio = float(at_count) / gc_count
if (gc_content > 0.6):
  gc_class = 'High'
elif(gc_content < 0.4):
  gc_class = 'Low'
else:
   gc_class = 'Moderate'
# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G count:', g_count
print 'C count:', c_count
print 'A count:', a_count
print 'T count:', t_count
print 'Sum count:', sum_count
print 'Total count:', total_count
print 'seq length:', seq_length
print 'AT/GC ratio:', atgc_ratio
print 'GC Classification:', gc_class 
