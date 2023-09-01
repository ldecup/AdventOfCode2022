inFile = open('Day10/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n').split(' '))

registerX = [1]

for instruction in data:
    if instruction[0] == 'noop':
        registerX.append(registerX[-1])
    elif instruction[0] == 'addx':
        registerX.append(registerX[-1])
        registerX.append(registerX[-1] + int(instruction[1]))

#Part 1
totalStrength = 20*registerX[19]
for i in range(60,len(registerX),40):
    totalStrength += i*registerX[i-1]
print('Total strength: ' + str(totalStrength))

#Part 2
screenArray = []
for y in range(6):
    screenArray.append([])
    for x in range(40):
        screenArray[y].append('.')

for y in range(6):
    for x in range(40):
        currentCycle = y*40+x #Cycles go from 0 to 239, not 1 to 240
        sprite = [registerX[currentCycle]-1,registerX[currentCycle],registerX[currentCycle]+1]
        if x in sprite:
            screenArray[y][x] = '#'

for lines in screenArray:
    line = ''
    for char in lines:
        line += char + ' ' #Extra space to make the output human readable
    print(line)