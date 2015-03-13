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
        self.deck = self.build_new_deck()
        self.cardRankings = self.create_card_rankings(self.deck)
        self.shuffle_deck()
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_one_card(self):
        assert self.deck
        return self.deck.pop()
    
    def create_card_rankings(self, deck):
        return dict(enumerate(deck))
    
    def build_new_deck(self):
        RANKS = list('23456789TJQKA')
        SUITS = list('hscd')
        return [Card(suit, rank) for suit, rank in itertools.product(RANKS, SUITS)]
    
class Hand(object):
    def __init__(self):
        self.hand = {'h':{}, 's':{}, 'c':{}, 'd':{}} 
    
    def is_suit_in_hand(self, suit):
        return suit in self.hand 
      
    def is_card_in_hand(self, card):
        if not self.is_suit_in_hand(card.suit): 
            return False
        if card.rank not in self.hand[card.suit]: 
            return False
        return True
    
    def get_token_card_for_testing(self):
        for suit in self.hand.keys():
            if len(self.hand[suit]) > 0:
                return self.hand[suit].popitem()[-1]
        raise(KeyError, 'There are no cards in the hand')
    
    def get_token_suit_card_for_tesing(self, suit):
        return self.hand[suit].popitem()[-1]
    
    def get_card(self, card):
        assert self.is_card_in_hand(card)
        return self.hand[card.suit].pop(card.rank) 
    
    def remove_card(self, card):
        assert self.is_card_in_hand(card)
        self.hand[card.suit].pop(card.rank)
    
    def remove_cards(self, cards):
        for card in cards:
            self.remove_card(card)
    
    def add_card(self, card):
        assert not self.is_card_in_hand(card)
        self.hand[card.suit][card.rank] = card
    
    def add_cards(self, cards):
        for card in cards:
            self.add_card(card)
            
    
class Scoring(object):
    def __ini__(self):
        self.HEART_POINT_VALUE = 1
        self.QUEEN_OF_SPADES_POINT_VALUE = 13
        self.VALUE_OF_ALL_POINTS = (self.HEART_POINT_VALUE * 13) + self.QUEEN_OF_SPADES_POINT_VALUE
        self.SHOOT_THE_MOON_SCORE = -26
        self.QUEEN_OF_SPADES = Card('Q', 's')
    
    def score_hearts(self, Hand):
        return len(Hand['h']) * self.HEART_POINT_VALUE
    
    def score_queen_of_spaces(self, Hand):
        if self.contains_queen_of_spades(Hand):
            return self.QUEEN_OF_SPADES_POINT_VALUE
        else:
            return 0
    
    def contains_queen_of_spades(self, Hand):
        return Hand.is_card_in_hand(self.QUEEN_OF_SPADES)
    
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
        self.pileOfCardsWon = Hand()
        self.passPile = []
        
    def add_cards_to_pass_pile(self, cards):
        assert self.passPile == []
        self.passPile.append(cards)
        
    def get_cards_from_pass_pile(self):
        tempCards = self.passPile
        self.passPile = []
        return tempCards
        
    def play_card(self, suit):
        # User interaction
        self.play_card_for_testing(suit)
        
    def play_card_for_testing(self, suit):
        if len(self.hand[suit]) > 0:
            return self.hand.get_token_suit_card_for_tesing()
        return self.hand.get_token_card_for_testing()

class PassingCards(object):
    def __init__(self):
        self.passingVariants = [
            self.left_pass_pairings,
            self.right_pass_pairings,
            self.across_pass_pairings,
            []]
        self.currentPassingDirection = 0
        self.noPassingRoundNum = 3
        self.players = []
        
    def change_pass_direction(self):
        self.currentPassingDirection += 1
        self.currentPassingDirection %= len(self.passingDirections)
    
    def is_passing_round(self):
        return self.currentPassingDirection != self.noPassingRoundNum
    
    def all_players_select_three_cards(self):
        assert self.players
        for player in self.players:
            self.add_three_cards_to_passing_pile(player)
    
    def add_three_cards_to_passing_pile(self, Player):
        # User interaction
        cards = []
        for _ in range(3):
            cards.append(Player.get_token_card_for_testing())
        Player.add_cards_to_pass_pile(cards)
    
    def pass_cards_from_to(self, fromPlayer, toPlayer):
        toPlayer.hand.add_cards(fromPlayer.get_cards_from_pass_pile)
    
    def map_pass_pairings(self, passPairings):
        for pairing in passPairings:
            fromPlayer = self.players[pairing[0]]
            toPlayer = self.players[pairing[1]]
            self.pass_cards_from_to(fromPlayer, toPlayer)
    
    def left_pass_pairings(self):
        return [
            (0,1),
            (1,2),
            (2,3),
            (3,0)]
    
    def right_pass_pairings(self):
        return [
            (0,3),
            (3,2),
            (2,1),
            (1,0)]
    
    def across_pass_pairings(self):
        return [
            (0,2),
            (2,0),
            (1,3),
            (3,1)]
    
    def pass_cards(self):
        passPairings = self.passingVariants[self.passingDirection]
        self.map_pass_pairings(passPairings)
        pass            
    
    def execute_passing_phase(self, players):
        if self.is_passing_round():
            self.players = players
            self.all_players_select_three_cards()
            self.pass_cards()
        self.change_pass_direction()
        self.players = []


class Mechanics(object):
    def __init__(self):
        pass


class Hearts(object):
    def __init__(self):
        # constants
        self.NUM_PLAYERS = 4
        self.twoOfClubs = Card('2', 'c')
        
        # class variables
        self.players = [Player() for player in xrange(self.NUM_PLAYERS)]
        self.playerToMove = 0
        self.turnPile = []
        self.turnOrderings = self.create_turn_orderings()
        
        # singleton classes:
        self.Scoring = Scoring()
        self.Passing = PassingCards()
    
    def play_game(self):
        pass
        
    def play_round(self):
        self.Passing.execute_passing_phase(self.players)
        self.play_first_hand()
        pass
    
    def get_position_of_winning_card(self):
        position = 0
        highestCardSoFar = self.turnPile[0]
        turnSuit = self.turnPile[0].suit
        
    
    def play_hand(self):
        for playerNumber in self.turnOrderings[self.playerToMove]:
            self.players[playerNumber].play_card()
                  
        pass
        
    def play_first_hand(self):
        self.playerToMove = self.get_position_of_player_with_two_of_clubs()
        self.play_hand()
        pass

    def get_position_of_player_with_two_of_clubs(self):
        for playerNumber in range(self.NUM_PLAYERS):
            if self.players[playerNumber].hand.is_card_in_hand(self.twoOfClubs):
                return playerNumber
        raise(ValueError, "Two of clubs not in deck")    
            
    def create_turn_orderings(self):
        return {
            0: [0,1,2,3],
            1: [1,2,3,0],
            2: [2,3,0,1],
            3: [3,0,1,2]}
            
    
class Tests(object):
    def __init__(self):
        self.queenOfSpades = Card('Q', 's')
        self.deck          = Deck()
        self.hand          = Hand()
        self.scoring       = Scoring()
        self.player        = Player()
        self.passingCards  = PassingCards()
        self.hearts        = Hearts()
    
        
test = Tests()
        
# invariants to test for when testing mode is on
'''
at the end of every round, 
    discard pile goes up by 4
    each player's hand goes down by 1
    game pile for turn never has more than 4 cards
'''


'''
    Concept inventory:
        Select three cards
        Direction to pass cards
            left, right, across, keep
        
'''
