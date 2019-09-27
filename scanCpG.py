import sys, re, math

#variables
plusname = "plus.prob"
minusname = "minus.prob"

plus = {}
minus = {}
alphabet = ["A", "C", "G", "T", "N"]
windows = [51, 201, 401]
sequenceName = sys.argv[1].strip(".").strip("\\") # remove .\\
sequence = ""
logratio = [[],[],[]]

# print Usage
def print_usage():
    print ("Usage: <sequenceName.fasta>")

# import markov model file
try:
    plusfile = open(plusname, "r")
    minusfile = open(minusname, "r")
except:
    print("Error, cannot open markov model file")

# check the sequence data
if (not(re.search(".fasta", sequenceName))):
    print("Error, sequence must be .fasta file")
    print_usage()
    sys.exit()

sequencedata = open(sequenceName, "r")

# import sequence data
line = sequencedata.readline().rstrip("\n")
while True:
    try:
        if line[0] != ">":
            sequence += line
    except:
        break
    line = sequencedata.readline().rstrip("\n")
print("Imported the sequence")

# import the plus model
line = plusfile.readline()
for zeile in alphabet:
    plus[zeile] = {}
    line = plusfile.readline().split()
    for spalte in range(1, len(line)):
        plus[zeile][alphabet[spalte -1]] = float(line[spalte])

# import the minus model
minusfile.readline()
for zeile in alphabet:
    minus[zeile] = {}
    line = minusfile.readline().split()
    for spalte in range(1, len(line)):
        minus[zeile][alphabet[spalte -1]] = float(line[spalte])

print("Imported the Markov Models")

# calc the log likelihood score and save the values to textfiles
value = 0

for w in range(len(windows)): # all window sizes
    print("Running scan with window size " + str(windows[w]))
    resultfile = open ("result_" + str(sequenceName).strip(".fasta") + "_" + str(windows[w]) + ".txt", "w")
    for i in range(0, len(sequence) - windows[w]):
        for k in range(i, i+windows[w]-1):
            value += math.log10((plus[sequence[k-1]][sequence [k]])/(minus[sequence[k-1]][sequence[k]]))
        logratio[w].append(value)
        resultfile.write(str(value)+"\n")
        value = 0

print ("Scan finished succesfully")
