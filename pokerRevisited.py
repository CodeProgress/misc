
import itertools
import random

def draw_hand(numCards = 5):
    """returns a random hand of numCards cards as a list of tuples (rank, suit)
    example: [('5', 's'), ('t', 'c'), ('7', 'd'), ('3', 'd'), ('3', 'c')]
    200,000 per second
    """
    return random.sample(deck, numCards)

def is_flush(hand):
    """returns True if all 5 cards in hand are of the same suit, False otherwise
    3,000,000 per second
    """
    return hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]


ranks = "23456789tjqka"
suits = 'cdhs'

deck  = list(itertools.product(ranks, suits))

#possibleHands = itertools.combinations(deck, 5)     # 2,598,960 possible hands

suitIndependentHandsIter = itertools.combinations_with_replacement(ranks, 5)

suitDependentHands   = []
suitIndependentHands = []

for i in suitIndependentHandsIter:
    if len(set(i)) == 5:
        suitDependentHands.append(i)
        suitIndependentHands.append(i)
    elif len(set(i)) != 1:
        suitIndependentHands.append(i)

# 7462 unique hands: len(suitedHands) + len(suitNeutralHands)




#
#straight_flush*
#four_of_kind
#full_house
#flush*
#straight*
#three_of_kind
#two_pair
#pair
#high_card*

# *affected by suit

