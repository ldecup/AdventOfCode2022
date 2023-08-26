inFile = open('Day5/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

posArray = [['H','C','R'],
            ['B','J','H','L','S','F'],
            ['R','M','D','H','J','T','Q'],
            ['S','G','R','H','Z','B','J'],
            ['R','P','F','Z','T','D','C','B'],
            ['T','H','C','G'],
            ['S','N','V','Z','B','P','W','L'],
            ['R','J','Q','G','C'],
            ['L','D','T','R','H','P','F','S']]
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
    for i in range(int(move['qty'])):
        posArray[int(move['to'])].append(posArray[int(move['from'])].pop())
    print(posArray)

message = ''
for stack in posArray:
    message = message + stack.pop()
print(message)