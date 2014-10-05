import time
import random

x = set([random.randint(1, 100000) for num in xrange(1000000)])
y = set([random.randint(1, 100000) for num in xrange(1000000)])

start = time.clock()
print len(x.intersection(y))
print time.clock() - start

start = time.clock()
print len(x-y)
print time.clock() - start

start = time.clock()
print len(y-x)
print time.clock() - start

