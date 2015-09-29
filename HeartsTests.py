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
    
    def test_valid_outcomes(self):
        self.reset_all()
        outcomes = self.hearts.simulate_games()
        for outcome in outcomes:
            assert max(outcome) >= 100
            assert min(outcome) >= 0
            
    def set_players_scores(self, aListOfFourScores):
        assert len(aListOfFourScores) == 4
        for i, score in enumerate(aListOfFourScores):
            self.hearts.players[i].score = score
            
    def test_game_over_conditions(self):
        self.reset_all()
        
        # Game that are NOT over
        self.set_players_scores([0,0,0,0])
        self.assertFalse(self.hearts.is_game_over())

        self.set_players_scores([10,30,40,30])
        self.assertFalse(self.hearts.is_game_over())

        self.set_players_scores([99,99,99,99])
        self.assertFalse(self.hearts.is_game_over())

        # Games that are over
        self.set_players_scores([0,0,0,100])
        self.assertTrue(self.hearts.is_game_over())

        self.set_players_scores([100,100,100,100])
        self.assertTrue(self.hearts.is_game_over())

        self.set_players_scores([10,0,23,120])
        self.assertTrue(self.hearts.is_game_over())
        
    def test_first_hand(self, numTests = 1000):
        for t in xrange(numTests):
            self.reset_all()
            self.hearts.reset_for_next_round()
            self.hearts.play_first_hand()
            
            winner = self.hearts.playerWhoStartsHand
            winnersWonCards = self.hearts.players[winner].pileOfCardsWon
            assert winnersWonCards.is_card_in_hand(self.hearts.twoOfClubs)
            self.assertEqual(0, self.scoring.score_hand(winnersWonCards))
            
            for p in self.hearts.players:
                assert p.hand.num_cards_in_hand() == 12
                assert not p.hand.is_card_in_hand(self.hearts.twoOfClubs)
    
    @staticmethod
    def check_if_players_cards_contains_pass_pile(passPile, player):
        return all(player.hand.is_card_in_hand(x) for x in passPile)
    
    def test_passing_cards(self):
        directions = ['left', 'right', 'across', 'noPass']
        
        self.reset_all()
        self.hearts.reset_game()

        for direction in directions:
            self.hearts.reset_for_next_round()
    
            self.hearts.Passing.players = self.hearts.players
            if self.hearts.Passing.is_passing_round():
                self.hearts.Passing.all_players_select_three_cards() 
                assert all((len(player.passPile) == 3) for player in self.hearts.players)
    
            playerOne, playerTwo, playerThree, playerFour = self.hearts.players
            pileOne, pileTwo, pileThree, pileFour = [player.passPile for player in self.hearts.players]
            
            self.hearts.Passing.pass_cards()
            
            if direction == 'left':
                assert self.check_if_players_cards_contains_pass_pile(pileOne, playerTwo)
                assert self.check_if_players_cards_contains_pass_pile(pileTwo, playerThree)
                assert self.check_if_players_cards_contains_pass_pile(pileThree, playerFour)
                assert self.check_if_players_cards_contains_pass_pile(pileFour, playerOne)    
            elif direction == 'right':
                assert self.check_if_players_cards_contains_pass_pile(pileOne, playerFour)
                assert self.check_if_players_cards_contains_pass_pile(pileTwo, playerOne)
                assert self.check_if_players_cards_contains_pass_pile(pileThree, playerTwo)
                assert self.check_if_players_cards_contains_pass_pile(pileFour, playerThree)
            elif direction == 'across':
                assert self.check_if_players_cards_contains_pass_pile(pileOne, playerThree)
                assert self.check_if_players_cards_contains_pass_pile(pileTwo, playerFour)
                assert self.check_if_players_cards_contains_pass_pile(pileThree, playerOne)
                assert self.check_if_players_cards_contains_pass_pile(pileFour, playerTwo) 
            elif direction == 'noPass':
                self.assertEquals(len(pileOne), 0)
                self.assertEquals(len(pileTwo), 0)
                self.assertEquals(len(pileThree), 0)
                self.assertEquals(len(pileFour), 0)
                self.assertEquals(playerOne.hand.num_cards_in_hand(), 13)
                self.assertEquals(playerTwo.hand.num_cards_in_hand(), 13)
                self.assertEquals(playerThree.hand.num_cards_in_hand(), 13)
                self.assertEquals(playerFour.hand.num_cards_in_hand(), 13)

            self.hearts.Passing.change_pass_direction()
        

unittest.main()