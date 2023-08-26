inFile = open('Day2/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

moveDict = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}
victoriesDict = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}
scoreDict = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

strategyData = []

for line in inData:
    strategyData.append([
        moveDict[line.rstrip('/n')[0]],
        moveDict[line.rstrip('/n')[2]]
    ])

totalScore = 0
moveScore = 0

for move in strategyData:
    moveScore = 0
    if move[0] == move[1]:
        moveScore = 3 + scoreDict[move[1]]
    elif move[1] == victoriesDict[move[0]]:
        moveScore = 6 + scoreDict[move[1]]
    else:
        moveScore = 0 + scoreDict[move[1]]
    totalScore = totalScore + moveScore

print("total score: " + str(totalScore))