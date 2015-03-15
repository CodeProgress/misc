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
        self.orderedDeck  = self.build_ordered_deck()
        self.cardRankings = self.create_card_rankings(self.orderedDeck)
        self.deck = self.orderedDeck
        self.shuffle_deck()
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_one_card(self):
        assert self.deck
        return self.deck.pop()
    
    def create_card_rankings(self, deck):
        return dict(zip(deck, range(1, 53, -1)))   # {card(2, 'h'): 52, card(3, 'h'):51, ...}
    
    def build_ordered_deck(self):
        RANKS = list('23456789TJQKA')
        SUITS = list('hscd')
        return [Card(suit, rank) for suit, rank in itertools.product(RANKS, SUITS)]
    
    def reset_deck(self):
        self.deck = self.orderedDeck
        self.shuffle_deck()
    
    def get_ranking_of_card(self, declaredSuit, card):
        if card.suit != declaredSuit:
            return 0
        return self.cardRankings[card]    
    
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
    
    def reset(self):
        self.hand = {'h':{}, 's':{}, 'c':{}, 'd':{}}
            
    
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
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.score = 0
        self.hand = Hand()
        self.pileOfCardsWon = Hand()
        self.passPile = []
    
    def add_cards_to_won_pile(self, cards):
        self.pileOfCardsWon.add_cards(cards)
        
    def add_cards_to_pass_pile(self, cards):
        assert self.passPile == []
        self.passPile.append(cards)
        
    def get_cards_from_pass_pile(self):
        tempCards = self.passPile
        self.passPile = []
        return tempCards
        
    def get_suit_of_hand_current_turn(self, cardsAlreadyPlayed):
        isSuitDetermined = len(cardsAlreadyPlayed) > 0 
        if isSuitDetermined:
            suit = cardsAlreadyPlayed[0].suit
        else:
            suit = None
        return suit
        
    def check_if_legal_selection(self, suit, selectedCardToPlay):
         if suit and selectedCardToPlay.suit != suit:
            if self.hand.is_suit_in_hand(suit):
                raise(ValueError, 'You must select a {} if you have a {}'.format(suit, suit))
    
    def play_card(self, cardsAlreadyPlayed):
        # User interaction
        suit               = self.get_suit_of_hand_current_turn(cardsAlreadyPlayed)               
        selectedCardToPlay = self.get_card_for_testing(suit)  # change this for different strategies or player interaction
        
        self.check_if_legal_selection(suit, selectedCardToPlay)
        
        return selectedCardToPlay
        
    def get_card_for_testing(self, suit):
        if suit and self.hand.is_suit_in_hand(suit):
            return self.hand.get_token_suit_card_for_tesing()
        return self.hand.get_token_card_for_testing()
    
    def reset_for_next_round(self):
        self.hand.reset()
        self.pileOfCardsWon.reset()
        self.passPile = []

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
        self.endingConditionNumberOfPoints = 100
        
        # class variables
        self.players = [Player(playerNumber) for playerNumber in xrange(self.NUM_PLAYERS)]
        self.playerWhoStartsHand = 0
        self.turnPile = []
        self.turnOrderings = self.create_turn_orderings()
        self.currentHandNumber = 1
        
        # singleton classes:
        self.Deck    = Deck()
        self.Scoring = Scoring()
        self.Passing = PassingCards()
    
    def reset_for_next_round(self):
        self.Deck.reset_deck()
        for player in self.players:
            player.reset_for_next_round()
        self.turnPile = []
        self.currentHandNumber = 1
    
    def is_game_over(self):
        return max([player.score for player in self.players]) < self.endingConditionNumberOfPoints
            
    def play_game(self):
        while not self.is_game_over():
            self.play_round()
            for player in sorted(self.players, key = lambda : self.players.score):
                print 'Player {} score: {}'.formate(player.playerNumber, player.score)
        
    def play_round(self):
        self.reset_for_next_round()
        self.play_all_hands_of_round()
        pass
        
    def get_winning_card(self):
        assert self.turnPile
        firstCardPlayed = self.turnPile[0]
        declaredSuit = firstCardPlayed.suit
        return sorted(self.turnPile, key = lambda card: self.Deck.get_ranking_of_card(declaredSuit, card))[-1]
    
    def get_position_of_winning_card(self):
        winningCard = self.get_winning_card()
        return self.turnPile.index(winningCard)
    
    def get_winning_player_number(self, winningCardPosition):
        orderOfPlayersForThisHand = self.turnOrderings[self.playerWhoStartsHand]        
        return orderOfPlayersForThisHand[winningCardPosition]    
        
    def get_winning_player_of_hand(self):
        winningCardPosition = self.get_position_of_winning_card()
        winningPlayerPosition = self.get_position_of_winning_player(winningCardPosition)
        winningPlayer = self.players[winningPlayerPosition]
        assert winningPlayer.playerPosition == winningPlayerPosition
        return winningPlayer
    
    def play_all_four_cards_of_hand(self):
        for positionOfCurrentPlayerToMove in self.turnOrderings[self.playerWhoStartsHand]:
            currentPlayerToMove = self.players[positionOfCurrentPlayerToMove]
            selectedCard = currentPlayerToMove.play_card(self.turnPile)
            self.turnPile.append(selectedCard)
            
    def play_hand(self):
        self.currentHandNumber += 1
        self.play_all_four_cards_of_hand()
        winningPlayer = self.get_winning_player_of_hand()
        winningPlayer.add_cards_to_won_pile(self.turnPile)
        self.playerWhoStartsHand = winningPlayer.playerNumber
        
    def play_first_hand(self):
        self.Passing.execute_passing_phase(self.players)
        self.playerWhoStartsHand = self.get_position_of_player_with_two_of_clubs()
        self.play_hand()

    def play_remaining_hands(self):
        while self.currentRoundNumber <= 13:
            self.play_hand()
    
    def play_all_hands_of_round(self):
        self.play_first_hand()
        self.play_remaining_hands()

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
        self.player        = Player(0)
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

'''
    To do:
        Clean up terminology: Hand vs Round     
        
'''

