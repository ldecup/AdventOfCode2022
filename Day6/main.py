inFile = open('Day6/input.txt', 'r')
dataStream = inFile.readlines()[0]
inFile.close()

datagramList = []
for i in range(4,len(dataStream)):
    datagram = dataStream[i-4:i]
    for char in datagram:
        if char in datagram:
            break
        else:
            datagramList.append([i,datagram])
        

print(datagramList)