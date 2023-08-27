import os

inFile = open('Day9/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n').replace(' ',''))

def updateTail(headPos, tailPos, prevHeadPos):
    if abs(headPos[0]-tailPos[0]) > 1 or abs(headPos[1]-tailPos[1]) > 1:
        newTailPos = prevHeadPos
    else:
        newTailPos = tailPos
    return newTailPos

def move(pos, dir):
    if dir == 'R':
        pos[0] += 1
    elif dir == 'L':
        pos[0] -= 1
    elif dir == 'U':
        pos[1] += 1
    elif dir == 'D':
        pos[1] -= 1
    return pos

headPos = [0,0]
tailPos = [0,0]
listHeadPos = [[headPos[0],headPos[1]]]
listTailPos = [[tailPos[0],tailPos[1]]]
biggestX = 0
biggestY = 0
for instructions in data:
    for i in range(int(instructions[1])):
        headPos = move(headPos,instructions[0])
        tailPos = updateTail(headPos, tailPos, listHeadPos[-1])
        listHeadPos.append(headPos.copy())#why the hidden pointers Python, whyyyy :(
        listTailPos.append(tailPos.copy())
        if headPos[0] > biggestX:
            biggestX = headPos[0]
        if headPos[1] > biggestY:
            biggestY = headPos[1]

#Remove duplicates
sortedList = []
for positions in listTailPos:
    if positions not in sortedList:
        sortedList.append(positions)

initPosArray = []
for y in range(biggestY):
    initPosArray.append([])
    for x in range(biggestX):
        initPosArray[y].append('.')

for i in range(len(listHeadPos)):
    os.system('cls')
    posArray = initPosArray.copy()
    posArray[listTailPos[i][1]][listTailPos[i][0]] = 'T'
    posArray[listHeadPos[i][1]][listHeadPos[i][0]] = 'H'
    for lines in posArray:
        line = ''
        for char in lines:
            line += char
        print(line)
    input('Continue...')

#Output
print('Number of unique positions visited: ' + str(len(sortedList)))