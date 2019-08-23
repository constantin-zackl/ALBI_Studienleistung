import sys, re, math

#variables
plusname = "plus.prob"
minusname = "minus.prob"

plus = {}
minus = {}
alphabet = ["A", "C", "G", "T"]
windows = [51, 201, 501]
sequenceName = sys.argv[1]
sequence = ""
logratio = [[],[],[]]

# import markov model file
try:
    plusfile = open(plusname, "r")
    minusfile = open(minusname, "r")
except:
    print("Error, cannot open markov model file")

# check the sequence data
if (not(re.search(".fasta", sequenceName))):
    print("Error, sequence must be .fasta file")
    sys.exit()

sequencedata = open(sequenceName, "r")

# import sequence data
line = sequencedata.readline().rstrip("\n")
while line!= "":
    try:
        if not(">" in line):
            sequence += line
    except:
        break;
    line = sequencedata.readline().rstrip("\n")

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

# calc the log likelihood score
value = 0
# for w in windows:
for w in range(len(windows)):
    print(windows[w])
    for i in range(0, len(sequence) - windows[w]):
        for k in range(i, i+windows[w]):
            value += math.log10((plus[sequence[i-1]][sequence [i]])/(minus[sequence[i-1]][sequence[i]]))
            logratio[w].append(value)
        value = 0

# open files and write
for i in range (len(windows)):
    resultfile = open ("result" + str(windows[i]) + ".txt", "w")

    for r in range(len(logratio)):
        for x in range(len(logratio[r])):
            resultfile.write(str(logratio[r][x]) + "\n")
