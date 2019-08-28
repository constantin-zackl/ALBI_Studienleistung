import sys, re
import matplotlib.pyplot as plt

# variables
dataName = sys.argv[1]
data = []

# precheck variables
if (not(re.search(".txt", dataName))):
    print ("Error, please enter a correct CpG Scan Result as a .txt file")
    sys.exit()

# import the data
file = open(dataName, "r")
line = file.readline().rstrip("\n")
while line != "":
    try:
        data.append(float(line))
    except:
        break
    line = file.readline().rstrip("\n")

# plot and display
plt.plot(data)
plt.show()
