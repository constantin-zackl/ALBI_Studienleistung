import sys, re

# variables
seqname = sys.argv[1]
resname = sys.argv[2]
countAll = {"A":0, "C":0, "G":0, "T":0}
countDiN = {"AA":0, "AC":0, "AG":0, "AT":0, "CA":0, "CC":0, "CG":0, "CT":0, "GA":0, "GC":0, "GG":0, "GT":0, "TA":0, "TC":0, "TG":0, "TT":0}
transition = {"AA":0, "AC":0, "AG":0, "AT":0, "CA":0, "CC":0, "CG":0, "CT":0, "GA":0, "GC":0, "GG":0, "GT":0, "TA":0, "TC":0, "TG":0, "TT":0}
# fuer die Übergangswahrrscheinlichkeiten werden alle ax, x aus {A, C, G, T} gezählt
# es langt jedoch alle vorkommen an a, c, g  und t zu zählen wobei
# die letzte stelle ausgelassen werden muss da auf sie keine
# Base mehr folgt.
sequence = ""

# methods
def print_usage():
    print("Usage: <sequencedata.fasta> <resultname> ")

# pre check the variables
if (not(re.search(".fasta", seqname))):
    print("Error, please enter a correct sequence file name")
    print_usage()
    sys.exit()

seqdata = open(seqname, "r")

if (not(re.search(".", resname))):
    print ("Error, no file endings for the result file")
    sys.exit()

# read the file and remove \n
line = seqdata.readline().rstrip("\n")
while line!= "":
    try:
        if not(">" in line):
            sequence += line
    except:
        print (1)
        break;
    line = seqdata.readline().rstrip("\n")

# Base Count and dinucleotide count
for i in range (0, len(sequence)-1):
    countAll[sequence[i]] += 1
    countDiN["" + sequence[i] + sequence[i+1]] += 1

# calculate the transition probabilities
for t in transition:
    transition[t] = countDiN[t] / countAll [t[0]]

# write to textfile
file = open(resname + ".prob", "w")
space = "     "
file.write("  ")
for b in countAll:
    file.write(b + space*5)
file.write("N") # in case N is used for any Base in the sequence files
file.write("\n")

ntransition = 0
for b in countAll:
    file.write(b + " ")
    for c in countAll:
        ntransition += transition[""+b+c]
        file.write(str(transition[""+b+c]) + space)
    file.write(str(ntransition)+"\n")
    ntransition = 0

file.write("N ")
file.write(str(transition["AA"] + transition["CA"] + transition["GA"] + transition["TA"]) + space)
file.write(str(transition["AC"] + transition["CC"] + transition["GC"] + transition["TC"]) + space)
file.write(str(transition["AG"] + transition["CG"] + transition["GG"] + transition["TG"]) + space)
file.write(str(transition["AT"] + transition["CT"] + transition["GT"] + transition["TT"]) + space)
file.write("1") # the probability of any base to another is 1

print ("Succesfully generated Markov probabilities from file " + seqname)

# close the file
seqdata.close()
