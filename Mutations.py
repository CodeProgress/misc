'''
generational differences
terminology:  
    Genomes are made of strands.
    Offspring are created by mutating each strand independently.
    mutation occur at a fixed probability.
    strands can take two states: zero or one.
'''


import random
import collections
import pylab
import cProfile
import numpy

GENOME_SIZE = 100
NUM_TRIALS = 1000
PROBABILITY_OF_STRAND_MUTATION = .2

def generate_random_genome(size = GENOME_SIZE):
    return [random.randint(0,1) for strand in xrange(size)]

def generate_random_genome_w_numpy(size = GENOME_SIZE):
    return numpy.random.choice([0,1], size)

def mutated_strand_value(strandValue):
    return strandValue^1

def updated_strand(strandValue, probabilityOfStrandMutation = PROBABILITY_OF_STRAND_MUTATION):
    if random.random() <= probabilityOfStrandMutation:
        return mutated_strand_value(strandValue)
    return strandValue
        
def create_offspring(genome):
    offspring = []
    for strand in genome:
        offspring.append(updated_strand(strand))
    return offspring

def create_offspring_w_numpy(genome, probabilityOfStrandMutation = PROBABILITY_OF_STRAND_MUTATION):
    copyGenome = genome.copy()
    copyGenome[numpy.random.rand(*genome.shape) <= probabilityOfStrandMutation] ^= 1
    return copyGenome
    
def count_num_mutations(parent, child):
    assert len(parent) == len(child)
    numStrands = len(parent)
    numMutations = 0
    for strand in range(numStrands):
        if parent[strand] != child[strand]:
            numMutations += 1
    return numMutations
    
def count_num_mutations_w_numpy(parent, child):
    return numpy.sum(parent != child)
    
def create_num_mutations_counter(numTrials = NUM_TRIALS):
    numMutationsCounter = collections.Counter()
    
    for trial in xrange(numTrials):
        genZero = generate_random_genome()
        genOne = create_offspring(genZero)
        numMutationsCounter[count_num_mutations(genZero, genOne)] += 1

    return numMutationsCounter

def create_num_mutations_counter_w_numpy(numTrials = NUM_TRIALS):
    numMutationsCounter = collections.Counter()
    
    for trial in xrange(numTrials):
        genZero = generate_random_genome_w_numpy()
        genOne = create_offspring_w_numpy(genZero)
        numMutationsCounter[count_num_mutations_w_numpy(genZero, genOne)] += 1

    return numMutationsCounter


def plot_num_mutations_counter(numMutationsCounter):
    # purely for visualization, add in values so keys with zero occurances show on graph
    numMutationsCounter.update(range(GENOME_SIZE+1))
    
    numMutations, numMutationsCount = zip(*numMutationsCounter.iteritems())
    
    pylab.scatter(numMutations, numMutationsCount)
    pylab.show()

plot_num_mutations_counter(create_num_mutations_counter_w_numpy())




#cProfile.run('create_num_mutations_counter()', sort='tottime')
#cProfile.run('create_num_mutations_counter_w_numpy()', sort='tottime')

# first run, no optimzations (size = 1000, numTrials=1000):  
#   (GENOME_SIZE = 1000, NUM_TRIALS = 1000):
#   6106884 function calls in 2.593 seconds
#   (GENOME_SIZE = 1000, NUM_TRIALS = 10000):
#   61070795 function calls in 25.650 seconds
#   (GENOME_SIZE = 10000, NUM_TRIALS = 100)
#   6101161 function calls in 2.558 seconds
#   (GENOME_SIZE = 10000, NUM_TRIALS = 1000)
#   61005747 function calls in 25.531 seconds
#   (GENOME_SIZE = 100000, NUM_TRIALS = 1000)
#   610008018 function calls in 264.955 seconds


# after numpy optimizations
#   (GENOME_SIZE = 1000, NUM_TRIALS = 1000):
#   13062 function calls in 0.076 seconds
#   (GENOME_SIZE = 1000, NUM_TRIALS = 10000):
#   130071 function calls in 0.750 seconds
#   (GENOME_SIZE = 10000, NUM_TRIALS = 100)
#   1371 function calls in 0.036 seconds
#   (GENOME_SIZE = 10000, NUM_TRIALS = 1000)
#   13150 function calls in 0.354 seconds
#   (GENOME_SIZE = 100000, NUM_TRIALS = 1000)
#   13359 function calls in 3.421 seconds


