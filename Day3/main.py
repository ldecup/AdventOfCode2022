inFile = open('Day3/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

priorities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

sackData = []

for line in inData:
    sack = line.rstrip('\n')
    sackData.append([
        sack[:int(len(sack)/2)],
        sack[-int(len(sack)/2):],
    ])

totalPriority = 0

for sacks in sackData:
    for items in sacks[0]:
        if items in sacks[1]:
            totalPriority = totalPriority + priorities.index(items) + 1
            break

print(totalPriority)