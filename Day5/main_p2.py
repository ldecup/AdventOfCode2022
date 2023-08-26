inFile = open('Day5/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

posArray = [['R','S','L','F','Q'],
            ['N','Z','Q','G','P','T'],
            ['S','M','Q','B'],
            ['T','G','Z','J','H','C','B','Q'],
            ['P','H','M','B','N','F','S'],
            ['P','C','Q','N','S','L','V','G'],
            ['W','C','F'],
            ['Q','H','G','Z','W','V','P','M'],
            ['G','Z','D','L','C','N','R']]
#posArray = [['Z','N'],['M','C','D'],['P']]

moveData = []
for line in inData:
    line = line.rstrip('\n').split(',')
    moveData.append({
        'qty': line[0],
        'from': int(line[1])-1,
        'to': int(line[2])-1
    })

print(posArray)
for move in moveData:
    print(move)
    movedCrates = posArray[int(move['from'])][-int(move['qty']):]
    for i in range(int(move['qty'])):
        posArray[int(move['from'])].pop()
        posArray[int(move['to'])].append(movedCrates.pop(0))
    print(posArray)

message = ''
for stack in posArray:
    message = message + stack.pop()
print(message)