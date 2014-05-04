#Code relates to a challenge that is currently in progress... To avoid spoilers,
#problem description will be uploaded after submission deadline

import random

def are_all_gone(shots, numShots):
    if shots[-1] == 0: 
        return False                #Last can't be slowest
    if sum(shots) < numShots/2: 
        return False                #Need at least half ones for all to cancel
        
    stack = [0]
    index = 0
    while index < len(shots):
        if shots[index] == 0: stack.append(0)
        else:
            if len(stack) == 0: stack.append(0)
            else: stack.pop()
        index += 1
    return len(stack) == 0

def sim_shots(numShots):
    shots = [int(round(random.random())) for x in range(numShots-1)]
    return are_all_gone(shots, numShots)

def sim_trials(numTrials, numShots):
    count = 0.
    for i in xrange(numTrials):
        if sim_shots(numShots):
            count += 1.
    return count/numTrials

#Monte Carlo simulations
print sim_trials(100000, 2)      # Expected = 0.5
print sim_trials(100000, 4)      # Expected = 0.375
print sim_trials(100000, 6)      # Expected = 0.3125


"""
Simulation results for 100,000,000 trials

sim_trials(100000000, 2)
NumShots   = 2
NumTrials  = 100,000,000
Expected   = 0.5
Simulation = 0.50000767
Dif        = 7.670e-06


sim_trials(100000000, 4)
NumShots   = 4
NumTrials  = 100,000,000
Expected   = 0.375
Simulation = 0.37496729
Dif        = 3.271e-05


sim_trials(100000000, 6) 
NumShots   = 6
NumTrials  = 100,000,000
Expected   = 0.3125
Simulation = 0.31250537
Dif        = 5.370e-06

"""
