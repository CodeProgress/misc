import random

listLength = 4

startList = random.sample(xrange(listLength), listLength)
goalList = random.sample(xrange(listLength), listLength)

count = 0
while startList != goalList:
    randIndex = random.randint(0, listLength-1)
    otherIndex = startList[randIndex]
    if startList[randIndex] != goalList[randIndex] and startList[otherIndex] != goalList[otherIndex]:
        startList[randIndex], goalList[otherIndex] = goalList[otherIndex], startList[randIndex]
    count += 1
    if count > 1000000:
        break

print startList
print goalList

#problem: explain what's going on here

