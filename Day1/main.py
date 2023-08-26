inFile = open('Day1/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

elfList = []
elfIndex = 0
currElfCal = 0

for line in inData:
    if line == '\n':
        elfList.append(currElfCal)
        currElfCal = 0
        elfIndex = elfIndex + 1
    else:
        currElfCal = currElfCal + int(line.rstrip('/n'))

print("Three biggest: " + str(sorted(elfList)[-3:]))
print("Sum of three biggest: " + str(sum(sorted(elfList)[-3:])))