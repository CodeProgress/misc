#Code relates to a challenge that is currently in progress... To avoid spoilers,
#problem description will be uploaded after submission deadline

import random

def is_collision(shots):
    if len(shots) < 2: return False
    return shots[-1] > shots[-2]

def clear_collision(shots):
    shots.pop()
    shots.pop()

def sim_shots(numShots = 20, verbose = False):
    shots = []
    fired = []
    for i in range(numShots):
        shot = random.random()
        shots.append(shot)
        fired.append(shot)
        if is_collision(shots):
            clear_collision(shots)
        
    if verbose: print shots, fired
    return len(shots) == 0

def sim_trials(numTrials, numShots=20):
    count = 0.
    for i in xrange(numTrials):
        if sim_shots(numShots):
            count += 1.
    return count/numTrials

print sim_trials(100000, 4)  # Expected = 0.375
print sim_trials(100000, 6)  # Expected = 0.3125


"""
Simulation results for 100,000,000 trials


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

