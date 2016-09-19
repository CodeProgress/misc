import random
import pylab

numTrials = 10000

listOfNumPeopleUntilDuplicate = []

for _ in xrange(numTrials):
    seen = set()
    limit = 365
    
    while True:
        birthday = random.randint(0, limit)
        if birthday in seen:
            break
        else:
            seen.add(birthday)
        # number of loops will never be more than limit due to pigeonhole principle

    listOfNumPeopleUntilDuplicate.append(len(seen))

maxVal = max(listOfNumPeopleUntilDuplicate)
histOfVals = [0 for _ in xrange(maxVal + 1)]

for i in listOfNumPeopleUntilDuplicate:
    histOfVals[i] += 1

pylab.plot(histOfVals)
pylab.xlabel("Number of People Until Duplicate")
pylab.show()
    