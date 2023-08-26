inFile = open('Day2/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

moveDict = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'loss',
    'Y': 'tie',
    'Z': 'win'
}
victoriesDict = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}
lossDict = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
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

moveList = []

for strat in strategyData:
    if strat[1] == 'win':
        moveList.append([
            strat[0],
            victoriesDict[strat[0]]
        ])
    elif strat[1] == 'tie':
        moveList.append([
            strat[0],
            strat[0]
        ])
    elif strat[1] == 'loss':
        moveList.append([
            strat[0],
            lossDict[strat[0]]
        ])       

totalScore = 0

for move in moveList:
    if move[0] == move[1]:
        moveScore = 3 + scoreDict[move[1]]
    elif move[1] == victoriesDict[move[0]]:
        moveScore = 6 + scoreDict[move[1]]
    else:
        moveScore = 0 + scoreDict[move[1]]
    totalScore = totalScore + moveScore

print("total score: " + str(totalScore))