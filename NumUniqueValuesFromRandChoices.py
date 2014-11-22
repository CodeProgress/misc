import random
import pylab

def numUnique(numRandPicks, limit):
    nums = set()
    for i in xrange(1, numRandPicks):
        nums.add(random.randint(1, limit))
    return len(nums)

numTrials = 1000
pylab.plot(range(numTrials), [numUnique(i, 100) for i in range(numTrials)])
pylab.xlabel('Number of Random Selection Between 1 and 100')
pylab.ylabel('Number of Unique Values Selected Between 1 and 100')
pylab.title('Quantity of Unique Values from N Random Selections')
pylab.show()

