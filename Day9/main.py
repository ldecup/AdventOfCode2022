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
listTailPos = [[0,0]]
for instructions in data:
    for i in range(int(instructions[1])):
        prevHeadPos = headPos
        headPos = move(headPos,instructions[0]) #this updates prevHeadPos for some reason ?
        print('head moved to: ' + str(headPos))
        tailPos = updateTail(headPos, tailPos, prevHeadPos)
        print('tail moved to: ' + str(tailPos))
        listTailPos.append(tailPos)
        

#Remove duplicates
sortedList = []
for positions in listTailPos:
    if positions not in sortedList:
        sortedList.append(positions)

#Output
print('Number of unique positions visited: ' + str(len(sortedList)))