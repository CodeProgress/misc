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
        self.deck = self.build_new_shuffled_deck()
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_one_card(self):
        assert self.deck
        return self.deck.pop()
    
    def build_new_shuffled_deck(self):
        RANKS = list('23456789TJQKA')
        SUITS = list('hscd')
        deck = [Card(suit, rank) for suit, rank in itertools.product(RANKS, SUITS)]
        random.shuffle(deck)
        return deck
    
class Hand(object):
    def __init__(self):
        self.hand = {'h':set(), 's':set(), 'c':set(), 'd':set()}
   
    def is_suit_in_hand(self, suit):
        return suit in self.hand 
      
    def is_card_in_hand(self, card):
        if not self.is_suit_in_hand(card.suit): 
            return False
        if card.rank not in self.hand[card.suit]: 
            return False
        return True
    
    def remove_token_card_for_testing(self):
        for suit in self.hand.keys():
            try:
                return Card(self.hand[suit].pop(), suit)
            except KeyError:
                continue
        raise(KeyError, 'There are no cards in the hand')
    
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
        self.HEART_POINT_VALUE = 1
        self.QUEEN_OF_SPADES_POINT_VALUE = 13
        self.VALUE_OF_ALL_POINTS = (self.HEART_POINT_VALUE * 13) + self.QUEEN_OF_SPADES_POINT_VALUE
        self.SHOOT_THE_MOON_SCORE = -26
    
    def score_hearts(self, Hand):
        return len(Hand['h']) * self.HEART_POINT_VALUE
    
    def score_queen_of_spaces(self, Hand):
        if self.contains_queen_of_spades(Hand):
            return self.QUEEN_OF_SPADES_POINT_VALUE
        else:
            return 0
    
    def contains_queen_of_spades(Hand):
        return 'Q' in Hand['s']
    
    def is_moon_shot(self, score):
        return score == self.VALUE_OF_ALL_POINTS
    
    def score_hand(self, Hand):
        score = 0
        score += self.score_hearts(Hand)
        score += self.score_queen_of_spaces(Hand)
        
        if self.is_moon_shot(score): 
            return self.SHOOT_THE_MOON_SCORE
            
        return score
    
class Player(object):
    def __init__(self):
        self.score = 0
        self.hand = Hand()
        self.discardPile = Hand()


class PassingCards(object):
    def __init__(self):
        self.passingVariants = [
            self.pass_cards_left,
            self.pass_cards_right,
            self.pass_cards_across,
            lambda :None]
        self.currentPassingDirection = 0
        self.Players = []
        
    def change_pass_direction(self):
        self.currentPassingDirection += 1
        self.currentPassingDirection %= len(self.passingDirections)
    
    def is_passing_round(self):
        return self.currentPassingDirection != 3
    
    def all_players_select_three_cards(self):
        for player in self.Players:
            self.select_three_cards(player)
    
    def select_three_cards(self, Player):
        # User interaction
        cards = []
        for _ in range(3):
            cards.append(Player.remove_token_card_for_testing())
    
    def pass_cards_left(self):
        pass
    
    def pass_cards_right(self):
        pass
    
    def pass_cards_across(self):
        pass
    
    def pass_cards(self, direction):
        pass            
    
    def facilitate_passing_cards(self, Players):
        if self.is_passing_round():
            self.Players = Players
            # select three cards
            self.passingVariants[self.passingDirection]()
            pass
        self.Players = []
        
    
class Hearts(object):
    def __init__(self):
        NUM_PLAYERS = 4
        self.players = [Player() for player in xrange(NUM_PLAYERS)]
        self.handsPlayed = []
        # singleton classes:
        self.Scoring = Scoring()
        self.Passing = PassingCards(self.players)
    
    def play_game(self):
        pass
        
    def play_round(self):
        pass
    
    def play_hand(self):
        pass
    
    
    '''
    Concept inventory:
        Select three cards
        Direction to pass cards
            left, right, across, keep
        
        
        
    '''
    
    
         
# invariants to test for when testing mode is on
'''
at the end of every round, 
    discard pile goes up by 4
    each player's hand goes down by 1
'''
