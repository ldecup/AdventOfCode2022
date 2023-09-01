import os
import copy

#Works with test input, underestimates with real input

inFile = open('Day9/testinput.txt', 'r')
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
        pos[1] -= 1
    elif dir == 'D':
        pos[1] += 1
    return pos

headPos = [0,0]
tailPos = [0,0]
listHeadPos = [headPos.copy()]
listTailPos = [tailPos.copy()]
biggestX = 0
biggestY = 0
for instructions in data:
    for i in range(int(instructions[1])):
        headPos = move(headPos,instructions[0])
        tailPos = updateTail(headPos, tailPos, listHeadPos[-1])
        listHeadPos.append(headPos.copy())#why the hidden pointers Python, whyyyy :(
        if tailPos not in listTailPos:
            listTailPos.append(tailPos.copy())
        if abs(headPos[0]) > biggestX:
            biggestX = abs(headPos[0])
        if abs(headPos[1]) > biggestY:
            biggestY = abs(headPos[1])

initPosArray = []
for y in range(2*biggestY+1):
    initPosArray.append([])
    for x in range(2*biggestX+1):
        initPosArray[y].append('.')

""" for i in range(len(listHeadPos)):
    os.system('cls')
    posArray = copy.deepcopy(initPosArray)
    posArray[listTailPos[i][1]+biggestY][listTailPos[i][0]+biggestX] = 'T'
    posArray[listHeadPos[i][1]+biggestY][listHeadPos[i][0]+biggestX] = 'H'
    for lines in posArray:
        line = ''
        for char in lines:
            line += char
        print(line)
    input('Continue...') """

#Output
print('Number of unique positions visited: ' + str(len(listTailPos)))