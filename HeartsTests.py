import unittest
import Hearts

class Tests(unittest.TestCase):
    def reset_all(self):
        self.queenOfSpades = Hearts.Card('Q', 's')
        self.deck = Hearts.Deck()
        self.hand = Hearts.Hand()
        self.scoring = Hearts.Scoring()
        self.player = Hearts.Player(0)
        self.passingCards = Hearts.PassingCards()
        self.hearts = Hearts.Hearts()

    def test_deck_length(self):
        self.reset_all()
        assert self.deck.get_num_cards_in_deck() == 52

    def test_high_and_low_scores(self, numGames=100, verbose=False):
        self.reset_all()
        newGame = self.hearts
        highestScore = 0
        lowestScore = 124
        for i in xrange(numGames):
            finalScores = newGame.play_game()
            if finalScores[0] < lowestScore:
                lowestScore = finalScores[0]
                if verbose:
                    print [player.score for player in sorted(newGame.players, key=lambda p: p.score)]
            if finalScores[3] > highestScore:
                highestScore = finalScores[3]
                if verbose:
                    print [player.score for player in sorted(newGame.players, key=lambda p: p.score)]
            assert lowestScore >= 0
            assert highestScore <= 125
            newGame.reset_game()

        assert lowestScore < highestScore
        return [lowestScore, highestScore]

    def test_scoring_moon_shot(self):
        self.reset_all()
        assert self.scoring.is_moon_shot([26, 0, 0, 0])
        assert self.scoring.is_moon_shot([0, 26, 0, 0])
        assert self.scoring.is_moon_shot([0, 0, 26, 0])
        assert self.scoring.is_moon_shot([0, 0, 0, 26])
        assert self.scoring.convertedMoonShotScores([26, 0, 0, 0]) == [0, 26, 26, 26]
        assert self.scoring.convertedMoonShotScores([0, 26, 0, 0]) == [26, 0, 26, 26]
        assert self.scoring.convertedMoonShotScores([0, 0, 26, 0]) == [26, 26, 0, 26]
        assert self.scoring.convertedMoonShotScores([0, 0, 0, 26]) == [26, 26, 26, 0]

        assert not self.scoring.is_moon_shot([13, 13, 0, 0])
        assert not self.scoring.is_moon_shot([13, 11, 1, 1])
        assert not self.scoring.is_moon_shot([13, 3, 0, 0])
    
    def get_player_score(self, position):
        return self.hearts.players[position].score
    
    def add_cards_to_players_won_cards(self, listOfCardsWonPerPlayer):
        assert len(listOfCardsWonPerPlayer) == len(self.hearts.players) == 4
        index = 0
        for player in self.hearts.players:
            player.add_cards_to_won_pile(listOfCardsWonPerPlayer[index])
            index += 1

    def test_scoring_round(self):
        self.reset_all()
        self.add_cards_to_players_won_cards([self.deck.deck[::], self.deck.deck[::], self.deck.deck[::], self.deck.deck[::]])
        with self.assertRaises(AssertionError):
            self.scoring.score_round(self.hearts.players)
    
    def test_each_all_player_scores_eqauls_twentysix(self):
        self.reset_all()
        self.add_cards_to_players_won_cards([self.deck.deck[:13], self.deck.deck[13:26], self.deck.deck[26:39], self.deck.deck[39:]])
        self.scoring.score_round(self.hearts.players)
        self.assertEquals(26, self.get_player_score(0) + self.get_player_score(1) + self.get_player_score(2) + self.get_player_score(3))

    def test_starting_conditions(self):
        self.reset_all()
        self.assertEquals(4, self.hearts.NUM_PLAYERS)
        self.assertEquals('c', self.hearts.twoOfClubs.suit)
        self.assertEquals('2', self.hearts.twoOfClubs.rank)
        self.assertEquals(100, self.hearts.endingConditionNumberOfPoints)
        self.assertEquals(13, self.hearts.startingNumberOfCards)
        
        # class variables
        self.assertEquals(4, len(self.hearts.players))
        self.assertEquals(0, self.hearts.playerWhoStartsHand)
        self.assertEquals([], self.hearts.turnPile)
        self.assertEquals(1, self.hearts.currentHandNumber)
        
        

unittest.main()