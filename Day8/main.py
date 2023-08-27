inFile = open('Day8/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n'))

#Find visible trees
visibleTrees = []
for y in range(1, len(data) - 1):
    for x in range(1, len(data[0]) - 1):
        #Check the trees on the left
        isTreeVisible = True
        for trees in data[y][:x]:
            if trees >= data[y][x]:
                isTreeVisible = False
        if isTreeVisible:
            visibleTrees.append([x,y])
        #Check the trees on the right
        isTreeVisible = True
        for trees in data[y][x+1:]:
            if trees >= data[y][x]:
                isTreeVisible = False
        if isTreeVisible:
            visibleTrees.append([x,y])
        #Check the trees above
        isTreeVisible = True
        for treesLines in data[:y]:
            if treesLines[x] >= data[y][x]:
                isTreeVisible = False
        if isTreeVisible:
            visibleTrees.append([x,y])
        #Check the trees below
        isTreeVisible = True
        for treesLines in data[y+1:]:
            if treesLines[x] >= data[y][x]:
                isTreeVisible = False
        if isTreeVisible:
            visibleTrees.append([x,y])

#Compute scenic scores
bestTree = {
    'score': 0,
    'x': 0,
    'y': 0
}
for y in range(1, len(data) - 1):
    for x in range(1, len(data[0]) - 1):
        treeScores = {
            'left': 0,
            'right': 0,
            'up': 0,
            'down': 0
        }
        #Look left
        for trees in list(reversed(data[y][:x])):
            if trees >= data[y][x]:
                treeScores['left'] = treeScores['left'] + 1
                break
            else:
                treeScores['left'] = treeScores['left'] + 1
        #Look right
        for trees in data[y][x+1:]:
            if trees >= data[y][x]:
                treeScores['right'] = treeScores['right'] + 1
                break
            else:
                treeScores['right'] = treeScores['right'] + 1
        #Look up
        for treeLines in list(reversed(data[:y])):
            if treeLines[x] >= data[y][x]:
                treeScores['up'] = treeScores['up'] + 1
                break
            else:
                treeScores['up'] = treeScores['up'] + 1
        #Look down
        for treeLines in data[y+1:]:
            if treeLines[x] >= data[y][x]:
                treeScores['down'] = treeScores['down'] + 1
                break
            else:
                treeScores['down'] = treeScores['down'] + 1
        #Compute tree score, store it if it's best
        treeScore = treeScores['left']*treeScores['right']*treeScores['up']*treeScores['down']
        if treeScore > bestTree['score']:
            bestTree = {
                'score': treeScore,
                'x': x,
                'y': y
            }

#Remove duplicates
sortedTrees = []
for trees in visibleTrees:
    if trees not in sortedTrees:
        sortedTrees.append(trees)

#Print a visual map
charLine = ''
for y in range(len(data)):
    for x in range(len(data[0])):
        if [x,y] in sortedTrees:
            charLine = charLine + 'X'
        else:
            charLine = charLine + '.'
    #print(charLine)
    charLine = ''

#Output
nbVisibleTrees = len(sortedTrees) + 2*len(data) + 2*len(data[0]) - 4
print('Number of visible trees: ' + str(nbVisibleTrees))
print('Best tree: ' + str(bestTree))