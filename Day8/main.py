inFile = open('Day8/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n'))

for line in data:
    visibleTrees = []
    highestTree = int(line[0])
    visibleTrees.append([0,line[0]])
    for tree in line:
        if int(tree) > highestTree:
            visibleTrees.append([line.index(tree),int(tree)])
        else:
            break
    print(visibleTrees)

print("done")