inFile = open('Day7/input.txt', 'r')
inData = inFile.readlines()
inFile.close()
del inFile

dataRaw = []
for line in inData:
    dataRaw.append(line.rstrip('\n').split(' '))
del inData

data = []
for i in range(len(dataRaw)):
    if i < len(dataRaw)-1:
        line = dataRaw[i]
        if line[0] == '$':
            if line[1] == 'ls':
                currLine = line
                nextLine = dataRaw[i+1]
                while nextLine[0] != '$':
                    currLine = currLine + [dataRaw.pop(i+1)]
                    if i < len(dataRaw)-1:
                        nextLine = dataRaw[i+1]
                    else:
                        break
                data.append(currLine)
            else:
                data.append(line)
    else:
        break

class fsObject:
    def __init__(self, name, type, size, children, parent):
        self.name = name
        self.type = type
        self.size = size
        self.children = children
        self.parent = parent

fileSystem = [fsObject('/', 'folder', 0,[], None)]

currentFSO = fileSystem[0]
arborescence = ['/']
for instruction in data:
    if instruction[1] == 'ls':
        for i in range(2,len(instruction)):
            if instruction[i][0] == 'dir':
                currentFSO.children.append(fsObject(instruction[i][1],'folder',0,[],currentFSO))
            else:
                currentFSO.children.append(fsObject(instruction[i][1],'file',int(instruction[i][0]),None,currentFSO))
                tempFSO = currentFSO
                while tempFSO != None:
                    tempFSO.size = tempFSO.size + int(instruction[i][0])
                    tempFSO = tempFSO.parent
    elif instruction[1] == 'cd':
        if instruction[2] == '..':
            currentFSO = currentFSO.parent
            arborescence.pop()
        else:
            for child in currentFSO.children:
                if child.name == instruction[2]:
                    currentFSO = child
                    arborescence.append(currentFSO.name)
                    break

def findBigFSO(currentFSO):
    global smallFolderList
    if currentFSO.size <= 100000 and currentFSO.type == 'folder':
        smallFolderList.append([currentFSO.name, int(currentFSO.size)])
    if currentFSO.children != None:
        for child in currentFSO.children:
            findBigFSO(child)

currentFSO = fileSystem[0]
smallFolderList = []
findBigFSO(fileSystem[0])

totalSizeSmallFolders = 0
for folder in smallFolderList:
    totalSizeSmallFolders = totalSizeSmallFolders + folder[1]

totalFSSize = 70000000
neededSpace = 30000000
availSpace = totalFSSize-fileSystem[0].size
spaceToClean = neededSpace - availSpace

def listFolderSizes(currentFSO):
    global folderSizeList
    if currentFSO.type == 'folder':
        folderSizeList.append([currentFSO.name, currentFSO.size])
        if currentFSO.children != None:
            for child in currentFSO.children:
                listFolderSizes(child)

folderSizeList = []
listFolderSizes(fileSystem[0])

smallestFolder = folderSizeList[0]
for folder in folderSizeList:
    if folder[1] >= spaceToClean and folder[1] < smallestFolder[1]:
        smallestFolder = folder

#print("Small folder list: " + str(smallFolderList))
print("Total size of small folders: "+ str(totalSizeSmallFolders))
print("Available space before deletion: " + str(availSpace))
print("Space to free up: " + str(spaceToClean))
#print("List of all folder sizes: " + str(folderSizeList))
print("Folder to delete: " + str(smallestFolder))