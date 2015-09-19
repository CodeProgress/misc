# Hearts
import itertools
import random
import cProfile


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def is_heart(self):
        return self.suit == 'h'
    
    def is_queen_of_spades(self):
        return self.suit == 's' and self.rank == 'Q'
    
    def __str__(self):
        return self.rank + self.suit


class Deck(object):
    def __init__(self):
        self.orderedDeck = self.build_ordered_deck()
        self.cardRankings = {}
        self.create_card_rankings()
        self.deck = self.orderedDeck
        self.shuffle_deck()
    
    def deal_one_card(self):
        assert self.deck
        return self.deck.pop()

    @staticmethod
    def build_ordered_deck():
        ranks = list('23456789TJQKA')
        suits = list('hscd')
        return [Card(suit, rank) for suit, rank in itertools.product(ranks, suits)]
    
    def reset_deck(self):
        self.deck = self.orderedDeck[::]
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def create_card_rankings(self):
        value = 52
        for card in self.orderedDeck:
            self.cardRankings[card] = value
            value -= 1
        # {card(2, 'h'): 52, card(3, 'h'):51, ...}

    def get_ranking_of_card(self, declaredSuit, card):
        if card.suit != declaredSuit:
            return 0
        return self.cardRankings[card]    

    def get_num_cards_in_deck(self):
        return len(self.deck)


class Hand(object):
    def __init__(self):
        self.hand = {'h': {}, 's': {}, 'c': {}, 'd': {}}
    
    def is_suit_in_hand(self, suit):
        return len(self.hand[suit]) > 0
      
    def is_card_in_hand(self, card):
        if not self.is_suit_in_hand(card.suit): 
            return False
        if card.rank not in self.hand[card.suit]: 
            return False
        return True
    
    def get_token_card_for_testing(self, isFirstHand=False):
        for suit in self.hand.keys():
            for card in self.hand[suit]:
                possibleCard = self.hand[suit][card]
                if isFirstHand and (possibleCard.is_heart() or possibleCard.is_queen_of_spades()):
                    continue
                else:
                    return self.hand[suit].pop(card)
        raise(KeyError, 'There are no cards in the hand') 
            
    def get_token_suit_card_for_testing(self, suit):
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

    def count_hearts(self):
        return len(self.hand['h'])
    
    def reset(self):
        self.hand = {'h': {}, 's': {}, 'c': {}, 'd': {}}
            
    def num_cards_in_hand(self):
        return sum(len(self.hand[suit]) for suit in self.hand)

class Scoring(object):
    def __init__(self):
        self.HEART_POINT_VALUE = 1
        self.QUEEN_OF_SPADES_POINT_VALUE = 13
        self.VALUE_OF_ALL_POINTS = (self.HEART_POINT_VALUE * 13) + self.QUEEN_OF_SPADES_POINT_VALUE
        self.QUEEN_OF_SPADES = Card('Q', 's')
    
    def score_hearts(self, hand):
        return hand.count_hearts() * self.HEART_POINT_VALUE
    
    def score_queen_of_spaces(self, hand):
        if hand.is_card_in_hand(self.QUEEN_OF_SPADES):
            return self.QUEEN_OF_SPADES_POINT_VALUE
        else:
            return 0
    
    def contains_queen_of_spades(self, hand):
        return hand.is_card_in_hand(self.QUEEN_OF_SPADES)
    
    def is_moon_shot(self, scores):
        return max(scores) == self.VALUE_OF_ALL_POINTS

    def convertedMoonShotScores(self, preMoonShotScores):
        scores = preMoonShotScores
        if self.is_moon_shot(preMoonShotScores):
            scores = map(lambda x: 0 if x == 26 else 26, scores)

        return scores

    def score_hand(self, hand):
        score = 0
        score += self.score_hearts(hand)
        score += self.score_queen_of_spaces(hand)

        return score

    def score_round(self, players):
        preMoonShotScores = []
        for player in players:
            scoreThisRound = self.score_hand(player.pileOfCardsWon)
            preMoonShotScores.append(scoreThisRound)

        scores = self.convertedMoonShotScores(preMoonShotScores)

        scoreIndex = 0
        for p in players:
            p.score += scores[scoreIndex]
            scoreIndex += 1

        totalPointsInRound = sum(scores)
        assert totalPointsInRound == 26 or totalPointsInRound == 26*3


class Player(object):
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.score = 0
        self.hand = Hand()
        self.pileOfCardsWon = Hand()
        self.passPile = []

    def add_card_to_hand(self, card):
        self.hand.add_card(card)

    def add_cards_to_hand(self, cards):
        self.hand.add_cards(cards)

    def add_cards_to_won_pile(self, cards):
        self.pileOfCardsWon.add_cards(cards)
        
    def add_cards_to_pass_pile(self, cards):
        assert self.passPile == []
        for card in cards:
            self.passPile.append(card)
        
    def get_cards_from_pass_pile(self):
        tempCards = self.passPile
        self.passPile = []
        return tempCards

    @staticmethod
    def get_suit_of_hand_current_turn(cardsAlreadyPlayed):
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
        suit = self.get_suit_of_hand_current_turn(cardsAlreadyPlayed)
        selectedCardToPlay = self.get_card_for_testing(suit)  # change this for different strategies
        
        self.check_if_legal_selection(suit, selectedCardToPlay)
        
        return selectedCardToPlay
        
    def play_a_specific_card(self, aCard):
        assert self.hand.is_card_in_hand(aCard)
        return self.hand.get_card(aCard)
        
    def get_card_for_testing(self, suit, isFirstHand=False):
        if suit and self.hand.is_suit_in_hand(suit):
            return self.hand.get_token_suit_card_for_testing(suit)
        if isFirstHand:
            return self.hand.get_token_card_for_testing(True)
        return self.hand.get_token_card_for_testing()
    
    def reset_for_next_round(self):
        self.hand.reset()
        self.pileOfCardsWon.reset()
        self.passPile = []


class PassingCards(object):
    def __init__(self):
        self.passingVariants = [
            self.get_left_pass_pairings(),
            self.get_right_pass_pairings(),
            self.get_across_pass_pairings(),
            []]
        self.currentPassingDirection = 0
        self.noPassingRoundNum = 3
        self.players = []
        
    def change_pass_direction(self):
        self.currentPassingDirection += 1
        self.currentPassingDirection %= len(self.passingVariants)
    
    def is_passing_round(self):
        return self.currentPassingDirection != self.noPassingRoundNum
    
    def all_players_select_three_cards(self):
        assert self.players
        for player in self.players:
            self.add_three_cards_to_passing_pile(player)

    @staticmethod
    def add_three_cards_to_passing_pile(player):
        # User interaction
        cards = []
        for _ in range(3):
            cards.append(player.hand.get_token_card_for_testing())
        player.add_cards_to_pass_pile(cards)

    @staticmethod
    def pass_cards_from_to(fromPlayer, toPlayer):
        cardsToPass = fromPlayer.get_cards_from_pass_pile()
        toPlayer.add_cards_to_hand(cardsToPass)
    
    def map_pass_pairings(self, passPairings):
        for pairing in passPairings:
            fromPlayer = self.players[pairing[0]]
            toPlayer = self.players[pairing[1]]
            self.pass_cards_from_to(fromPlayer, toPlayer)

    @staticmethod
    def get_left_pass_pairings():
        return [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0)]

    @staticmethod
    def get_right_pass_pairings():
        return [
            (0, 3),
            (3, 2),
            (2, 1),
            (1, 0)]

    @staticmethod
    def get_across_pass_pairings():
        return [
            (0, 2),
            (2, 0),
            (1, 3),
            (3, 1)]

    def pass_cards(self):
        passPairings = self.passingVariants[self.currentPassingDirection]
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
        self.startingNumberOfCards = 13
        
        # class variables
        self.players = [Player(playerNumber) for playerNumber in xrange(self.NUM_PLAYERS)]
        self.playerWhoStartsHand = 0
        self.turnPile = []
        self.turnOrderings = self.create_turn_orderings()
        self.currentHandNumber = 1
        
        # singleton classes:
        self.Deck = Deck()
        self.Scoring = Scoring()
        self.Passing = PassingCards()

    def reset_game(self):
        self.players = [Player(playerNumber) for playerNumber in xrange(self.NUM_PLAYERS)]
        self.playerWhoStartsHand = 0
        self.currentHandNumber = 1

    def reset_for_next_round(self):
        for player in self.players:
            player.reset_for_next_round()
        self.Deck.reset_deck()
        self.deal_cards_to_players()
        self.turnPile = []
        self.currentHandNumber = 1

    def deal_cards_to_players(self):
        for _ in xrange(self.startingNumberOfCards):
            for player in self.players:
                player.add_card_to_hand(self.Deck.deal_one_card())
        assert len(self.Deck.deck) == 0

    def is_game_over(self):
        return max([player.score for player in self.players]) >= self.endingConditionNumberOfPoints
            
    def play_game(self, verbose=False):
        while not self.is_game_over():
            self.play_round()
            if verbose:
                for player in sorted(self.players, key=lambda p: p.score):
                    print 'Player {} score: {}'.format(player.playerNumber, player.score)

        if verbose:
            print ['Player {} score: {}'.format(player.playerNumber, player.score)
                   for player in sorted(self.players, key=lambda p: p.score)]

        return [player.score for player in sorted(self.players, key=lambda p: p.score)]

    def play_round(self):
        self.reset_for_next_round()
        self.play_all_hands_of_round()
        self.Scoring.score_round(self.players)
        
    def get_winning_card(self):
        assert self.turnPile
        firstCardPlayed = self.turnPile[0]
        declaredSuit = firstCardPlayed.suit
        return sorted(self.turnPile, key=lambda card: self.Deck.get_ranking_of_card(declaredSuit, card))[-1]
    
    def get_position_of_winning_card(self):
        winningCard = self.get_winning_card()
        return self.turnPile.index(winningCard)
    
    def get_position_of_winning_player(self, winningCardPosition):
        orderOfPlayersForThisHand = self.turnOrderings[self.playerWhoStartsHand]        
        return orderOfPlayersForThisHand[winningCardPosition]    
        
    def get_winning_player_of_hand(self):
        winningCardPosition = self.get_position_of_winning_card()
        winningPlayerPosition = self.get_position_of_winning_player(winningCardPosition)
        winningPlayer = self.players[winningPlayerPosition]
        assert winningPlayer.playerNumber == winningPlayerPosition
        return winningPlayer
    
    def play_all_four_cards_of_hand(self):
        for i, positionOfCurrentPlayerToMove in enumerate(self.turnOrderings[self.playerWhoStartsHand]):
            currentPlayerToMove = self.players[positionOfCurrentPlayerToMove]
            if self.currentHandNumber == 1 and i == 0:
                selectedCard = currentPlayerToMove.play_a_specific_card(self.twoOfClubs)
            elif self.currentHandNumber == 1:
                selectedCard = currentPlayerToMove.get_card_for_testing('c', True)
            else:
                selectedCard = currentPlayerToMove.play_card(self.turnPile)
            self.turnPile.append(selectedCard)
            
    def play_hand(self):
        self.play_all_four_cards_of_hand()
        winningPlayer = self.get_winning_player_of_hand()
        winningPlayer.add_cards_to_won_pile(self.turnPile)
        self.turnPile = []
        self.playerWhoStartsHand = winningPlayer.playerNumber
        # Test that the total number of cards won + total cards left to be played = 52
        assert sum(p.pileOfCardsWon.num_cards_in_hand() for p in self.players) \
            + sum(player.hand.num_cards_in_hand() for player in self.players) == 52
        self.currentHandNumber += 1
        
    def play_first_hand(self):
        self.Passing.execute_passing_phase(self.players)
        self.playerWhoStartsHand = self.get_position_of_player_with_two_of_clubs()
        self.play_hand()

    def play_remaining_hands(self):
        while self.currentHandNumber <= 13:
            self.play_hand()
    
    def play_all_hands_of_round(self):
        self.play_first_hand()
        self.play_remaining_hands()

    def get_position_of_player_with_two_of_clubs(self):
        for playerNumber in range(self.NUM_PLAYERS):
            if self.players[playerNumber].hand.is_card_in_hand(self.twoOfClubs):
                return playerNumber
        raise(ValueError, "Two of clubs not in deck")    

    @staticmethod
    def create_turn_orderings():
        return {
            0: [0, 1, 2, 3],
            1: [1, 2, 3, 0],
            2: [2, 3, 0, 1],
            3: [3, 0, 1, 2]}

    def simulate_games(self, numGames=100):
        outcomes = []
        for _ in xrange(numGames):
            outcomes.append(self.play_game())
            self.reset_game()
        return outcomes

Hearts().simulate_games()


