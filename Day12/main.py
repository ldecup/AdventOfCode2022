#Both Dijkstra and A* find a path, but apparently not the shortest one
#Cost is constant, so Dijkstra has no use over A* but still returns a shorter path ??
#Todo: try with BFS

inFile = open('Day12/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n'))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class node:
    def __init__(self, coords, height, gCost, hCost, fCost, parentNode):
        self.coords = coords
        self.height = height
        self.gCost = gCost #Distance to start
        self.hCost = hCost #Distance to target
        self.fCost = fCost #gCost + hCost
        self.parentNode = parentNode

def AreNeighbours(node1, node2):
    if (abs(node1.coords[0] - node2.coords[0]) <= 1 and node1.coords[1] == node2.coords[1]) or (abs(node1.coords[1] - node2.coords[1]) <= 1 and node1.coords[0] == node2.coords[0]):
        return True
    else:
        return False

def GetDistance(node1, node2):
    return abs(node1.coords[0] - node2.coords[0]) + abs(node1.coords[1] - node2.coords[1])

def ChooseAlgo(value):
    algo = 'A*' #Dijkstra or A*
    if algo == 'Dijkstra':
        return 0
    else:
        return value

nodeList = []
for idLine, line in enumerate(data):
    for idChar, char in enumerate(line):
        if char == 'S':
            startNode = node([idLine,idChar],1,0,None,None,None)
            nodeList.append(startNode)
        elif char == 'E':
            endNode = node([idLine,idChar],26,None,0,None,None)
            nodeList.append(endNode)
        else:
            nodeList.append(node([idLine,idChar],letters.index(char)+1,None,None,None,None))

startNode.hCost = ChooseAlgo(GetDistance(startNode, endNode))
startNode.fCost = startNode.hCost
endNode.gCost = GetDistance(startNode, endNode)
endNode.fCost = endNode.gCost

#A* pathfinding implementation
openNodes = [startNode]
closedNodes = []
while len(openNodes) > 0:
    #Find the lowest fCost node and set it as the current node
    currentNode = openNodes[0]
    for nodes in openNodes:
        if nodes.fCost < currentNode.fCost or (nodes.fCost == currentNode.fCost and nodes.hCost < currentNode.hCost):
            currentNode = nodes
    openNodes.remove(currentNode)
    closedNodes.append(currentNode)

    #Check if that node is the target
    if currentNode is endNode:
        break

    #Find eligible neighbours
    eligibleNeighbours = []
    for nodes in nodeList:
        if AreNeighbours(nodes, currentNode):
            if nodes not in closedNodes:
                if nodes.height - currentNode.height <= 1 or nodes.height <= currentNode.height:
                    eligibleNeighbours.append(nodes)
                    nodes.gCost = GetDistance(nodes, startNode)
                    nodes.hCost = ChooseAlgo(GetDistance(nodes, endNode))
                    nodes.fCost = nodes.gCost + nodes.hCost

    #Find best neighbour to select as parent
    for nodes in eligibleNeighbours:
        if (currentNode.gCost + 1 < nodes.gCost) or nodes not in openNodes:
            nodes.gCost = currentNode.gCost + 1
            nodes.hCost = ChooseAlgo(GetDistance(nodes, endNode))
            nodes.fCost = nodes.gCost + nodes.hCost
            nodes.parentNode = currentNode
            if nodes not in openNodes:
                openNodes.append(nodes)

#Backtrack path
if endNode.parentNode is None:
    print('No path found')
else:
    currentNode = endNode
    path = []
    while currentNode is not None:
        currentNode = currentNode.parentNode
        path.append(currentNode)
    print(len(path)-1)

    #Draw path in file
    fileArray = []
    outFile = open('Day12/output.txt', 'w')
    for i in range(len(data)):
        line = []
        for j in range(len(data[0])):
            line.append(data[i][j])
        fileArray.append(line)
    for nodes in closedNodes:
        if nodes in path:
            fileArray[nodes.coords[0]][nodes.coords[1]] = 'P'
    for lines in fileArray:
        line = ''
        for char in lines:
            line += char
        outFile.writelines(line)
        outFile.writelines('\n')
    outFile.close()