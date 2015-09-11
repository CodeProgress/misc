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

outcomes = []
for i in range(11):
    outcomes.append(num_successful_matches(i))

pylab.plot(outcomes)

pylab.show()
