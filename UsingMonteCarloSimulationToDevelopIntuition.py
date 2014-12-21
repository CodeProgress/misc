#Using Monte Carlo simulation to develop intuition

import random

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

"""
FAIR_DIE = [1,2,3,4,5,6]

def roll_die():
    return random.choice(FAIR_DIE)

def roll_two_dice():
    return (roll_die(), roll_die())
    
def prob_framework(condition1, condition2, numTrials = 1000000):
    totalNumOutcomes = 0.0
    observedNumOutcomes = 0.0
    for i in xrange(numTrials):
        roll = roll_two_dice()
        if condition1(roll):
            totalNumOutcomes += 1
            if condition2(roll):
                observedNumOutcomes += 1
    return observedNumOutcomes/totalNumOutcomes

def prob_of_both_even_if_one_even():
    condition1 = lambda roll: roll[0] % 2 == 0 or roll[1] % 2 == 0
    condition2 = lambda roll: sum(roll) % 2 == 0 # now test if the sum is even, if it's not then the other one is odd
    return prob_framework(condition1, condition2)
    
def prob_sum_odd_if_one_even():
    condition1 = lambda roll: roll[0] % 2 == 0 or roll[1] % 2 == 0
    condition2 = lambda roll: sum(roll) % 2 != 0
    return prob_framework(condition1, condition2)
 
def prob_of_both_3_if_one_3():
    condition1 = lambda roll: roll[0] == 3 or roll[1] == 3
    condition2 = lambda roll: sum(roll) == 6
    return prob_framework(condition1, condition2)      
   
def prob_one_even_if_one_3():
    condition1 = lambda roll: roll[0] == 3 or roll[1] == 3
    condition2 = lambda roll: sum(roll) % 2 != 0
    return prob_framework(condition1, condition2)

                  
print prob_of_both_even_if_one_even()
# a) Actual: 1/3   Experimental: 0.333863120164   Deviation: 0.0005297868306666786

print prob_sum_odd_if_one_even()
# b) Actual: 2/3   Experimental: 0.665579967746   Deviation: 0.0010866989206665956

print prob_of_both_3_if_one_3()
# c) Actual: 1/11  Experimental: 0.0902056193665  Deviation: 0.0007034715425909138

print prob_one_even_if_one_3()
# d) Actual: 6/11  Experimental: 0.544705655178   Deviation: 0.0007488902765454553
