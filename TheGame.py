
import random
import cProfile

class Rating(object):
    def __init__(self):
        self.lowRating = 0
        self.highRating = 10
        self.averageRating = 5
        self.standardDeviationRating = 2

    def get_rating(self):
        '''
        Returns a random float between low and high using a gaussian distribution.
        uses
            self.lowRating
            self.highRating
            self.averageRating
            self.standardDeviation
            
        To help limit the runtime of this function, the following conditions are enforced:
            low  <= mu - sigma
            high >= mu + sigma
        Doing so will ensures a 99.6% chance the method will finish within 5 loops,
        a 1 in 4.3 billion chance of taking more than 20 loops
        and only a 1 in 1.4x10e48 chance of taking more than 100 loops...
        '''
        mu    = self.averageRating
        sigma = self.standardDeviationRating
        assert (self.lowRating + sigma) <= mu <= (self.highRating - sigma), 'Limit range must cover at least one std dev from mu in each direction to avoid infinite or near infinite loop'
        rating = random.gauss(mu, sigma)
        while rating < self.lowRating or rating > self.highRating:
            rating = random.gauss(mu, sigma)    
        return rating

class Person(object):
    def __init__(self):
        self.rating = Rating().get_rating()
        self.mate = None
        self.exes = []
    
    def start_relationship(self, otherPerson):
        self.mate = otherPerson
    
    def end_relationship(self):
        assert self.mate
        self.exes.append(self.mate)
        self.mate = None
    
    def is_chemistry(self, otherPerson):
        '''
        true if the other person is within one rating point, false otherwise
        can be made more complex later, for example:
            pickiness (which might change based on factors)
            '''
        return abs(self.rating - otherPerson.rating) < 5

class Population(object):
    def __init__(self, numX, numY):
        self.allX = set(Person() for x in xrange(numX))
        self.allY = set(Person() for y in xrange(numY))
        self.singleX = self.allX.copy()
        self.singleY = self.allY.copy()
        self.takenX  = set()
        self.takenY  = set()

    def test_single_union_taken_equals_all(self):
        assert self.singleX.union(self.takenX) == self.allX
        assert self.singleY.union(self.takenY) == self.allY
        

class TheGame(object):
    def __init__(self, numX, numY, numDays):
        self.population = Population(numX, numY)
        self.numDays = numDays        
        
    def run_simulation(self):
        for day in xrange(self.numDays):
            self.simulate_day()
        self.test_invariants()
    
    def test_invariants(self):
        self.test_equal_number_of_taken()
        self.population.test_single_union_taken_equals_all()
    
    def test_equal_number_of_taken(self):
        assert len(self.population.takenX) == len(self.population.takenY)
    
    def simulate_day(self):
        self.date_singles()
    
    def date_singles(self):
        if not self.population.singleX: return
        if not self.population.singleY: return
        xSingles = list(self.population.singleX)
        ySingles = list(self.population.singleY)
        random.shuffle(xSingles)
        random.shuffle(ySingles)
        while xSingles and ySingles:
            x = xSingles.pop()
            y = ySingles.pop()
            self.go_on_date(x, y)
    
    def go_on_date(self, x, y):
        if self.is_date_successful(x, y):
            self.pair_up(x, y)
    
    def pair_up(self, x, y):
        assert x in self.population.singleX
        assert y in self.population.singleY
        x.start_relationship(y)
        y.start_relationship(x)
        self.population.singleX.remove(x)
        self.population.singleY.remove(y)
        self.population.takenX.add(x)
        self.population.takenY.add(y)
    
    def breakup(self, x, y):
        assert x in self.population.takenX
        assert y in self.population.takenY
        x.end_relationship(y)
        y.end_relationship(x)
        self.population.takenX.remove(x)
        self.population.takenY.remove(y)
        self.population.singleX.add(x)
        self.population.singleY.add(y)
    
    def is_date_successful(self, x, y):
        if x.is_chemistry(y) and y.is_chemistry(x):
            self.pair_up(x, y)
    

a = TheGame(100000, 100000, 365)
cProfile.run('a.run_simulation()')
print 'taken x, y: ', len(a.population.takenX), len(a.population.takenY)
