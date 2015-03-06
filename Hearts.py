# Hearts
import itertools
import random

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

class Deck(object):
    def __init__(self):
        RANKS = list('23456789TJQKA')
        SUITS = list('hscd')
        self.deck = [Card(suit, rank) for suit, rank in itertools.product(RANKS, SUITS)]
        self.shuffle_deck()
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_one_card(self):
        assert self.deck
        return self.deck.pop()
    
    
class Hand(object):
    def __init__(self):
        self.hand = {'h':set(), 's':set(), 'c':set(), 'd':set()}
   
    def is_suit_in_hand(self, suit):
        return card.suit in self.hand 
      
    def is_card_in_hand(self, card):
        if not self.is_suit_in_hand(card.suit): 
            return False
        if card.rank not in self.hand[card.suit]: 
            return False
        return True
    
    def remove_card(self, card):
        assert self.is_card_in_hand(card)
        self.hand[card.suit].remove(card.rank)
    
    def remove_cards(self, cards):
        for card in cards:
            self.remove_card(card)
    
    def add_card(self, card):
        assert not self.is_card_in_hand(card)
        self.hand[card.suit].add(card.rank)
    
    def add_cards(self, cards):
        for card in cards:
            self.add_card(card)
            
    
class Scoring(object):
    def __ini__(self):
        pass

    
class Player(object):
    def __init__(self):
        self.score = 0
        self.hand = Hand()
    

class Hearts(object):
   def __init__(self):
       NUM_PLAYERS = 4
       self.players = [Player() for player in range(NUM_PLAYERS)]
      
       
         
# invariants to test for when testing mode is on
'''
at the end of every round, 
    discard pile goes up by 4
    each player's hand goes down by 1
'''
