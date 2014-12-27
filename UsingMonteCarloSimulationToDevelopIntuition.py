#Using Monte Carlo simulation to develop intuition

import random
import itertools

"""
Problem Statements:
    
A friend rolls two fair dice:

    One die is even...
        a) What is the probability that the other die is even?
        b) What is the probability that the sum is odd?

(Repeat):
    
    One die is a 3...
        c) What is the probability that the other die is a 3?
        d) What is the probability that the other die is even?

A friend rolls three dice:
    One die is a 1, another die is a 2...
        e) Probability the final die is a 3?
    Two dice are the same...
        f) Probability the other die is the same?

"""
FAIR_DIE = [1,2,3,4,5,6]

def roll_die(numSides = 6):
    return random.randint(1, numSides)

def roll_n_dice(numDice = 1):
    return [roll_die() for _ in xrange(numDice)]
    
def prob_framework(condition1, condition2, numDice = 2, numTrials = 1000000):
    totalNumOutcomes = 0.0
    observedNumOutcomes = 0.0
    for i in xrange(numTrials):
        roll = roll_n_dice(numDice)
        if condition1(roll):
            totalNumOutcomes += 1
            if condition2(roll):
                observedNumOutcomes += 1
    return observedNumOutcomes/totalNumOutcomes

def enumation_framework(condition1, condition2, numDice = 2):
    allDice = [FAIR_DIE for _ in xrange(numDice)]
    possibleOutcomes = itertools.product(*allDice)
    numOutcomesSatisfyingCondition1 = 0
    numOutcomesSatisfyingCondition2 = 0
    for outcome in possibleOutcomes:
        if condition1(outcome):
            numOutcomesSatisfyingCondition1 += 1
            if condition2(outcome):
                numOutcomesSatisfyingCondition2 += 1
    return (numOutcomesSatisfyingCondition2, numOutcomesSatisfyingCondition1)
     

# a)
def prob_of_both_even_if_one_even():
    condition1 = lambda roll: roll[0] % 2 == 0 or roll[1] % 2 == 0
    condition2 = lambda roll: sum(roll) % 2 == 0 # now test if the sum is even, if it's not then the other one is odd
    return prob_framework(condition1, condition2)

# b)     
def prob_sum_odd_if_one_even():
    condition1 = lambda roll: roll[0] % 2 == 0 or roll[1] % 2 == 0
    condition2 = lambda roll: sum(roll) % 2 != 0
    return prob_framework(condition1, condition2)

# c)
def prob_of_both_3_if_one_3():
    condition1 = lambda roll: roll[0] == 3 or roll[1] == 3
    condition2 = lambda roll: sum(roll) == 6
    return prob_framework(condition1, condition2)      

# d) 
def prob_one_even_if_one_3():
    condition1 = lambda roll: roll[0] == 3 or roll[1] == 3
    condition2 = lambda roll: sum(roll) % 2 != 0
    return prob_framework(condition1, condition2)

# e)
def prob_one_3_if_one_1_and_one_2():
    condition1 = lambda roll: 1 in roll and 2 in roll
    condition2 = lambda roll: sum(roll) == 6
    return prob_framework(condition1, condition2, 3)

# f)
def prob_all_same_if_two_same():
    condition1 = lambda roll: len(set(roll)) <= 2
    condition2 = lambda roll: len(set(roll)) == 1
    print enumation_framework(condition1, condition2, 3)
    return prob_framework(condition1, condition2, 3)
                  
#print prob_of_both_even_if_one_even()
# a) Actual: 1/3   Experimental: 0.333863120164   Deviation: 0.0005297868306666786

#print prob_sum_odd_if_one_even()
# b) Actual: 2/3   Experimental: 0.665579967746   Deviation: 0.0010866989206665956

#print prob_of_both_3_if_one_3()
# c) Actual: 1/11  Experimental: 0.0902056193665  Deviation: 0.0007034715425909138

#print prob_one_even_if_one_3()
# d) Actual: 6/11  Experimental: 0.544705655178   Deviation: 0.0007488902765454553




