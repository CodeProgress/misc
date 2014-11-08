# Goal:  use the monte carlo method to determine optimal strategy in blackjack
# Stretch Goal: graph it to make basic strategy card, real time updating
# populate table entries as they occur randomly, most common will be most accurate
#   but also make it so you can test specific cases

import random

class Deck(object):
    def __init__(self):
        self.originalDeck = [x+y for x in 'AKQJT98765432' for y in 'shdc']
        self.deck         = [] 
        self.build_deck()
    
    def build_deck(self):
        self.deck = self.originalDeck 
        self.shuffle() 
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal_card(self):
        assert self.deck
        return self.deck.pop()
    
    def __str__(self):
        return str(self.deck)

class Player(object):
    def __init__(self):
        self.reset_hand()
        
    def reset_hand(self):
        self.hand = {}
        
    def add_to_hand(self, card):
        if self.hand[card]: self.hand[card] += 1
        else: self.hand[card] = 1
        
class Dealer(Player):
    pass

class BlackJack(object):
    def __init__(self, Deck):
        self.deck = Deck()
        
        # point values
        lowCardValues     = {str(lowCard):lowCard for lowCard in range(2, 10)}
        highCardValues    = {highCard: 10 for highCard in 'KQJT'}
        aceValues         = {'A': [1, 11]}
        self.cardPointValues = {}
        self.cardPointValues.update(lowCardValues)
        self.cardPointValues.update(highCardValues)
        self.cardPointValues.update(aceValues)

    def score_hand(self, hand):
        score = 0
        for card in hand:
            score += self.cardPointValues[card]
        return score    
    
    def optimal_move(self, hand, dealerUpCard):
        """returns what to do with the given hand
        hand: list
        returns: "hit", "stand", "double", "split"
        """
        pass

aDeck = Deck()