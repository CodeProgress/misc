import random
import pylab

def num_successful_matches(numElements, numTrials = 100000):
    # start with a shuffled list
    aList = random.sample(range(numElements), numElements)
    
    # define the goal ordering
    goalList = range(numElements)
    
    numSuccessfulMatches = 0
    
    for trial in range(numTrials):
        # mutate the list
        for index, value in enumerate(aList):
            if index != value:
                randIndex = random.choice(aList)
                aList[index], aList[randIndex] = aList[randIndex], aList[index]
        if aList == goalList:
            numSuccessfulMatches += 1
            #reset the list
            aList = random.sample(range(numElements), numElements)
    
    return numSuccessfulMatches


numElements = 10
outcomes = []
for i in range(1, numElements+1):
    outcomes.append(num_successful_matches(i))

pylab.plot(range(1, numElements+1), outcomes)
pylab.xlabel("Number of Elements in List")
pylab.ylabel("Number of Recurrences")
pylab.show()


# maybe track how many digits are out of place during each loop and watch it
# fluctuate on its way to the match