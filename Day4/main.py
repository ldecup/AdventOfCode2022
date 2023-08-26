inFile = open('Day4/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

globalData = []
for line in inData:
    line = line.rstrip('\n').split(',')
    globalData.append([
        [line[0].split('-')[0],line[0].split('-')[1]],
        [line[1].split('-')[0],line[1].split('-')[1]]
    ])

overlapCount = 0
for pairs in globalData:
    if int(pairs[1][0]) >= int(pairs[0][0]):
        if int(pairs[1][1]) <= int(pairs[0][1]):
            print(str(pairs[1]) + ' is included in ' + str(pairs[0]))
            overlapCount = overlapCount + 1
            continue
    if int(pairs[0][0]) >= int(pairs[1][0]):
        if int(pairs[0][1]) <= int(pairs[1][1]):
            print(str(pairs[0]) + ' is included in ' + str(pairs[1]))
            overlapCount = overlapCount + 1
            continue

print(overlapCount)
