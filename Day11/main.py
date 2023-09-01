import math
import os

inFile = open('Day11/input.txt', 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n').lstrip(' ').split(':'))
data.append([''])

class monkey:
    def __init__(self, id, items, operation, testDivisibleBy, thowToWhenTrue, thowToWhenFalse, inspectedItems):
        self.id = id
        self.items = items
        self.operation = operation
        self.testDivisibleBy = testDivisibleBy
        self.thowToWhenTrue = thowToWhenTrue
        self.thowToWhenFalse = thowToWhenFalse
        self.inspectedItems = inspectedItems

monkeyList = []
globalTest = 1
currentMonkey = monkey(None,None,None,None,None,None,None)
for line in data:
    if line[0].split(' ')[0] == 'Monkey':
        currentMonkey.id = line[0].split(' ')[1]
    elif line[0] == 'Starting items':
        currentMonkey.items = line[1].lstrip(' ').split(', ')
    elif line[0] == 'Operation':
        currentMonkey.operation = line[1].lstrip(' ').split(' ')[-2:]
    elif line[0] == 'Test':
        currentMonkey.testDivisibleBy = int(line[1].lstrip(' ').split(' ')[2])
        globalTest *= currentMonkey.testDivisibleBy
    elif line[0] == 'If true':
        currentMonkey.thowToWhenTrue = int(line[1].lstrip(' ').split(' ')[3])
    elif line[0] == 'If false':
        currentMonkey.thowToWhenFalse = int(line[1].lstrip(' ').split(' ')[3])
    elif line[0] == '':
        currentMonkey.inspectedItems = 0
        itemList = []
        for item in currentMonkey.items:
            itemList.append(int(item))
        currentMonkey.items = itemList
        monkeyList.append(currentMonkey)
        currentMonkey = monkey(None,None,None,None,None,None,None)







for i in range(10000):
    os.system('cls')
    print("Round: " + str(i))
    for monkey in monkeyList:
        for item in monkey.items:
            monkey.inspectedItems += 1
            #Compute worry level
            if monkey.operation[0] == '*':
                if monkey.operation[1] == 'old':
                    worryLevel = item * item
                else:
                    worryLevel = item * int(monkey.operation[1])
            elif monkey.operation[0] == '+':
                if monkey.operation[1] == 'old':
                    worryLevel = item + item
                else:
                    worryLevel = item + int(monkey.operation[1])
            #worryLevel = math.floor(worryLevel/3)

            #Perform monkey action
            if worryLevel % monkey.testDivisibleBy == 0:
                monkeyList[monkey.thowToWhenTrue].items.append(worryLevel % globalTest)
                #print("Monkey " + str(monkey.id) + " threw " + str(worryLevel) + " to monkey " + str(monkey.thowToWhenTrue))
            else:
                monkeyList[monkey.thowToWhenFalse].items.append(worryLevel % globalTest)
                #print("Monkey " + str(monkey.id) + " threw " + str(worryLevel) + " to monkey " + str(monkey.thowToWhenFalse))
        monkey.items = []

print("Monkey inventories:")
monkeyActivityList = []
for monkey in monkeyList:
    monkeyActivityList.append(monkey.inspectedItems)
    print(monkey.items)
monkeyActivityList = sorted(monkeyActivityList)

monkeyBusiness = monkeyActivityList[-1] * monkeyActivityList[-2]
print("Monkey business: " + str(monkeyBusiness))