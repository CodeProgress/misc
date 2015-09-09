import random
import collections
import pylab as pl

def increment_outcome_array(array, x_index, y_value):
    array[x_index][y_value] += 1

numTrials = 1000
numValues = 20
counter = collections.Counter()
outcomeArray = pl.array([[0]*numValues for i in range(numValues)])

aList = range(numValues)

for trial in xrange(numTrials):
    for i in aList:
        aList[i] = random.randint(0, numValues-1)

    for finalIndex, val in enumerate(aList):
        increment_outcome_array(outcomeArray, finalIndex, val)
    
    counter.update(aList)

print counter
pl.pcolor(outcomeArray)
pl.colorbar()
pl.show()


'''
Results for:
    numTrials = 10000000
    numValues = 10
    
0: 10263836, 
1: 10227903, 
2: 10181384, 
3: 10125428, 
4: 10064540, 
5: 9992793, 
6: 9924944, 
7: 9845493, 
8: 9737539, 
9: 9636140

Question:  Why this and not a uniform distribution?
'''

