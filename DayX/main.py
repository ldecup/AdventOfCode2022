inFile = open('DayX/testinput.txt', 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n'))