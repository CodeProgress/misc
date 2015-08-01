import random
import collections

numTrials = 2
numValues = 10
aList = range(numValues)

counter = collections.Counter()

for trial in xrange(numTrials):
    for i in aList:
        aList[i] = random.randint(0, numValues-1)

    counter.update(aList)

print counter


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

