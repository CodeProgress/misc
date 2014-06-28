#Monte Carlo Pi Approximation

import random
from math import pi     #only used to calc difference btw pi and approximation

def throw_dart():
    """
    Return random x, y coordinates within a square of side length 2
    corners (1,1), (1,-1), (-1,1), (-1,-1)
    -1 <= x <= 1
    -1 <= y <= 1
    """
    return random.random()*2 - 1, random.random()*2 - 1
    
def is_inside_circle(x, y):
    """return True if x,y fall within a circle of radius 1, centered at 0,0"""
    return (x**2 + y**2)**.5 < 1

def calc_pi_from_areas(numInside, total):
    areaOfSquare            = 4
    circleAsPercentOfSquare = numInside/float(total)
    return areaOfSquare * circleAsPercentOfSquare

def approx_pi(numTrials):
    insideCircle = 0
    for i in xrange(numTrials):
        x, y = throw_dart()
        if is_inside_circle(x,y):
            insideCircle += 1
    
    return calc_pi_from_areas(insideCircle, numTrials)

tabSize = 16

print '\n' + 'Num Trials \t Pi Approx \t Difference'.expandtabs(tabSize)
print '-'*tabSize*3 
for numTrials in [2**x for x in range(20)]:
    approx     = approx_pi(numTrials)
    difference = abs(approx - pi)
    print '{} \t {} \t {}'.format(numTrials, approx, difference).expandtabs(tabSize)
