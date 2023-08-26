inFile = open('Day3/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

priorities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

sackData = []

for line in inData:
    sackData.append(line.rstrip('\n'))

sackGroups = []

for i in range(0, len(sackData), 3):
    sackGroups.append([
        sackData[i],
        sackData[i+1],
        sackData[i+2],
    ])

totalPriority = 0

for groups in sackGroups:
    for items in groups[0]:
        if items in groups[1]:
            if items in groups[2]:
                totalPriority = totalPriority + priorities.index(items) + 1
                break

print(totalPriority)