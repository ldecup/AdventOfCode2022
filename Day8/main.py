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
    print(charLine)
    charLine = ''

#Output
nbVisibleTrees = len(sortedTrees) + 2*len(data) + 2*len(data[0]) - 4
print('Number of visible trees: ' + str(nbVisibleTrees))