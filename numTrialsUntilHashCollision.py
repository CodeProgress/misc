# probability of drawing ths same number twice
# i.e. hash collision

import random
import pylab

def num_trials_until_collision(limit):
    count = 1
    aSet = set()
    while True:
        x = random.randint(1, limit)
        if x in aSet: return count
        aSet.add(x)
        count += 1


def calc_stats_num_trials(limit, numTests, verbose = True):
    outcomes = []
    for i in range(numTests):
        outcomes.append(num_trials_until_collision(limit))
    if verbose: 
        #print outcomes
        print "avg: " + str(sum(outcomes)/float(numTests))
        print "max: " + str(max(outcomes))
        print "min: " + str(min(outcomes))
    #return

def plot_num_trials(maxLimit, incr):
    # add in numTests at some point
    outcomes = []
    for i in range(1, maxLimit, incr):
        outcomes.append(num_trials_until_collision(i))
    pylab.plot(outcomes)
    pylab.show()
    
plot_num_trials(10000, 1)


