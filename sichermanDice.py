# create sicherman dice

import itertools
import collections
import cProfile

NORMAL_DIE = [1,2,3,4,5,6]

def enumerate_dice(*args):
    return collections.Counter(sum(roll) for roll in itertools.product(*args))

GOAL_DISTRIBUTION = enumerate_dice(NORMAL_DIE, NORMAL_DIE)

def is_any_sum_overrepresented(die1, die2):
    enumeration = enumerate_dice(die1, die2)
    for diceSum in enumeration:
        if diceSum not in GOAL_DISTRIBUTION: 
            return True
        if enumeration[diceSum] > GOAL_DISTRIBUTION[diceSum]:
            return True
    return False

def is_valid_distribution_both(die1, die2):
    if die1[-1] +  die2[-1] != 12: return False
    if die1[-1] == die2[-1]: return False
    if die1[0] +   die2[0] != 2:  return False
    return True

def is_valid_distribution_single(die):
    if die[-1] == die[-2]: return False
    if die[0] ==  die[1]: return False    
    return True

def is_distribution_equal(die1, die2):
    return enumerate_dice(die1, die2) == GOAL_DISTRIBUTION and sorted(die1) != NORMAL_DIE
    
def find_sicherman_dice_brute_force():
    sichermanDice = []
    for die1 in itertools.combinations_with_replacement(range(0, 6), 6):
        if not is_valid_distribution_single(die1): continue
        for die2 in itertools.combinations_with_replacement(range(0, 11), 6):
            if not is_valid_distribution_single(die2): continue
            if not is_valid_distribution_both(die1, die2): continue
            if is_distribution_equal(die1, die2):
                sichermanDice.append((die1, die2))
    return sichermanDice

cProfile.run('find_sicherman_dice_brute_force()')

sichermanDiceConfigurations = find_sicherman_dice_brute_force()
for sichermanDice in sichermanDiceConfigurations:
    print sichermanDice


