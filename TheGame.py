
import random

class Person(object):
    def __init__(self):
        self.rating = self.gauss_with_limits()
        self.status = None
        
    def gauss_with_limits(self, mu = 5, sigma = 2, low = 0, high = 10):
        '''
        Returns a random float between low and high using a gaussian distribution.
        
        To help limit the runtime of this function, the following conditions are enforced:
            low  <= mu - sigma
            high >= mu + sigma
        Doing so will ensures a 99.6% chance the method will finish within 5 loops,
        a 1 in 4.3 billion chance of taking more than 20 loops
        and only a 1 in 1.4x10e48 chance of taking more than 100 loops...
        '''
        assert (low + sigma) <= mu <= (high - sigma), 'Limit range must cover at least one std dev from mu in each direction to avoid infinite or near infinite loop'
        
        gauss = random.gauss(mu, sigma)
        while gauss < low or gauss > high:
            gauss = random.gauss(mu, sigma)    
        return gauss
    
class TheGame(object):
    def __init__(self, numX, numY, numDays):
        pass
    
    def run_simulation(self):
        for day in xrange(self.numDays):
            pass
    
    
    
    
