import pylab
import random

def add_random():
    return (random.random()*2 - 1)

def random_walk_gen(func):
    pos = 0
    while True:
        yield pos
        pos += func()

randomWalk = random_walk_gen(add_random)
pylab.plot([randomWalk.next() for x in xrange(1000000)])
pylab.show()

