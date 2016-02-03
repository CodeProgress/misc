# Solitaire

import random
from datetime import timedelta
from time import clock


class Card(object):
    def __init__(self, rank, suit):
        assert rank in 'A23456789TJQK'
        assert suit in 'shdc'
        self.rank = rank
        self.suit = suit
        self.isRed = suit in 'hd'
        self.isBlack = suit in 'sc'
        assert self.isRed != self.isBlack

    def __str__(self):
        return self.rank + self.suit

    def areCardsEqual(self, cardToCompare):
        if type(cardToCompare) != Card: return False
        return self.rank == cardToCompare.rank and self.suit == cardToCompare.suit


class Deck(object):
    def __init__(self):
        self.ranks = 'A23456789TJQK'
        self.suits = 'shdc'
        self.deck = [Card(rank, suit) for rank in self.ranks for suit in self.suits]


class Pile(object):
    def __init__(self, name, iterable):
        self.pile = (name, iterable)
        self.indexes = {rank: index for index, rank in enumerate('A23456789TJQK')}

    def getName(self):
        return self.pile[0]

    def getIterable(self):
        return self.pile[1]

    def add(self, cardToMove):
        self.addToTopOfPile(cardToMove)

    def remove(self, cardToRemove):
        assert cardToRemove.areCardsEqual(self.valueOfTopCard())
        return self.popFromTopOfPile()

    def addToTopOfPile(self, obj):
        self.getIterable().append(obj)

    def popFromTopOfPile(self):
        assert self.getIterable(), 'Attempting to pop from an empty Pile!'
        return self.getIterable().pop()

    def valueOfTopCard(self):
        if self.isEmpty():
            return None
        return self.getIterable()[-1]

    def shufflePile(self):
        random.shuffle(self.getIterable())

    def size(self):
        return len(self.getIterable())

    def getIndexOfCard(self, card):
        for index, possibleCard in enumerate(self.getIterable()):
            if card.areCardsEqual(possibleCard):
                return index
        raise ValueError("Card is not in the pile!")

    def isEmpty(self):
        return self.size() == 0

    def __str__(self):
        return str(self.getName()) + ' ' + str(self.valueOfTopCard())


class DrawPile(Pile):
    def __init__(self, name, iterable):
        super(DrawPile, self).__init__(name, iterable)
        self.discardPile = self.createDiscardPile()

    def remove(self, cardToRemove):
        assert cardToRemove.areCardsEqual(self.valueOfTopCard())
        drawCardToRemove = self.popFromTopOfPile()
        if self.isEmpty():
            self.resetDrawPile()
        return drawCardToRemove

    def createDiscardPile(self):
        return Pile('discard', [])

    def resetDrawPile(self):
        discardPileSize = self.discardPile.size()
        for i in range(discardPileSize):
            self.addToTopOfPile(self.discardPile.popFromTopOfPile())
        assert self.discardPile.size() == 0
        self.shufflePile()

    def flipToNextCard(self):
        if self.isEmpty() and self.discardPile.isEmpty():
            return
        if not self.isEmpty():
            self.discardPile.addToTopOfPile(self.popFromTopOfPile())
        if self.isEmpty():
            self.resetDrawPile()

    def __str__(self):
        return str(self.getName()) + ' ' + str(self.valueOfTopCard())


class GoalPile(Pile):
    def __init__(self, name, iterable):
        super(GoalPile, self).__init__(name, iterable)

    def canAdd(self, possibleCard):
        assert possibleCard.rank in self.indexes
        if possibleCard.suit != self.getName():
            return False
        if self.isEmpty():
            return self.indexes[possibleCard.rank] == 0
        return self.indexes[possibleCard.rank] - self.indexes[self.valueOfTopCard().rank] == 1


class AccumPile(Pile):
    def __init__(self, name, iterable, visibilityIndex):
        super(AccumPile, self).__init__(name, iterable)
        self.visibilityIndex = visibilityIndex

    def add(self, cardToMove):
        '''cardToMove could be a single card, or list representing a diff accumPile splice'''
        if type(cardToMove) != list:
            self.addToTopOfPile(cardToMove)
        else:
            for card in cardToMove:
                self.addToTopOfPile(card)

    def remove(self, cardToRemove):
        cardsToRemove = []
        cardIndex = self.getIndexOfCard(cardToRemove)
        assert cardIndex >= self.visibilityIndex
        spliceToMove = self.getIterable()[cardIndex:]
        for i in range(len(spliceToMove)):
            cardsToRemove.append(self.popFromTopOfPile())
        if len(cardsToRemove) == 1:
            return cardsToRemove[0]
        return cardsToRemove[::-1]  # reverse to preserve original ordre

    def popFromTopOfPile(self):
        assert self.getIterable(), 'Attempting to pop from an empty Pile!'
        cardToPop = self.getIterable().pop()
        if len(self.getVisibleCards()) == 0:
            self.visibilityIndex -= 1
            if self.visibilityIndex < 0:
                self.visibilityIndex = 0
        return cardToPop

    def spliceToDifferentAccumPile(self, card, differentPile):
        # Note: This does not check for legality
        origLenBothPiles = self.size() + differentPile.size()
        cardIndex = self.getIndexOfCard(card)
        assert cardIndex >= self.visibilityIndex
        spliceToMove = self.getIterable()[cardIndex:]
        for i in range(len(spliceToMove)):
            differentPile.addToTopOfPile(spliceToMove[i])
            self.popFromTopOfPile()
        assert origLenBothPiles == self.size() + differentPile.size()

    def getVisibleCards(self):
        return self.getIterable()[self.visibilityIndex:][::]

    def canNestUnder(self, possibleCard):
        assert possibleCard.rank in self.indexes
        if self.isEmpty():
            return True
        return (self.indexes[self.valueOfTopCard().rank] - self.indexes[possibleCard.rank] == 1) \
               and possibleCard.isRed != self.valueOfTopCard().isRed

    def __str__(self):
        return str(self.getName()) + ' x{} '.format(max(self.visibilityIndex, 0)) + str(
            [str(card) for card in self.getIterable()[self.visibilityIndex:]])


class Statistics(object):
    def __init__(self):
        self.startTime = clock()
        self.actionCounter = 0

    def incrementActionCounter(self):
        self.actionCounter += 1

    def __str__(self):
        elapsedTime = clock() - self.startTime
        elapsedTime = str(timedelta(seconds=int(elapsedTime)))  # format
        return "Elapsed time: {}, Total actions: {}".format(elapsedTime, self.actionCounter)


class Solitaire(object):
    def __init__(self):
        self.originalDeck = Deck()
        self.drawPile = self.createDrawPile()
        self.goalPiles = self.createGoalPiles()
        self.accumPiles = self.createAccumPiles()
        self.isWinner = False
        self.stats = Statistics()

    def createDrawPile(self):
        drawPile = DrawPile('draw', self.originalDeck.deck[::])
        drawPile.shufflePile()
        return drawPile

    def createGoalPiles(self):
        allGoalPiles = []
        allGoalPiles.append(GoalPile('s', []))
        allGoalPiles.append(GoalPile('h', []))
        allGoalPiles.append(GoalPile('d', []))
        allGoalPiles.append(GoalPile('c', []))
        return allGoalPiles

    def createAccumPiles(self):
        assert self.drawPile.size() == len(self.originalDeck.deck)
        allAccumPiles = []
        for i in range(7):
            visibilityIndex = i
            allAccumPiles.append(
                AccumPile(str(i), [self.drawPile.popFromTopOfPile() for _ in range(i + 1)], visibilityIndex))

        assert sum(x.size() for x in allAccumPiles) == 28, 'accum piles have incorrect number of cards'
        return allAccumPiles

    def playGame(self):
        while not self.isGameOver():
            self.printGameState()
            self.checkPileTotals(True)
            self.stats.incrementActionCounter()

            cardToMoveText = raw_input("Enter card to move (ex: 3h or f) ")
            if cardToMoveText == 'exit':
                break
            elif cardToMoveText == 'f':
                self.drawPile.flipToNextCard()
                continue

            cardToMove = self.createCardToMove(cardToMoveText)

            if not cardToMove:
                print "Invalid Move"
                continue

            sourcePile = self.getSourcePileOfCardToMove(cardToMove)
            if not sourcePile:
                print "Invalid Move"
                continue

            destinationPileText = raw_input("Enter which pile to move card onto (ex: '1') ")
            if destinationPileText == 'exit':
                break

            destinationPile = self.getDestinationPileName(cardToMove, sourcePile, destinationPileText)
            if not destinationPile:
                print "Invalid Pile"
                continue

            self.playMove(cardToMove, sourcePile, destinationPile)

            print "Successfully played move!"

        self.printGameOutcome()

    def createCardToMove(self, cardToMoveText):
        if len(cardToMoveText) != 2:
            return None
        try:
            possibleCard = Card(cardToMoveText[0], cardToMoveText[1])
        except AssertionError:
            return None
        return possibleCard

    def getSourcePileOfCardToMove(self, cardToMove):
        '''returns the name of the pile the card belongs to, unless illegal card, returns None'''
        if cardToMove.areCardsEqual(self.drawPile.valueOfTopCard()):
            return self.drawPile
        for accumPile in self.accumPiles:
            for aCard in accumPile.getVisibleCards():
                if cardToMove.areCardsEqual(aCard):
                    return accumPile
        for goalPile in self.goalPiles:
            if cardToMove.areCardsEqual(goalPile.valueOfTopCard()):
                return goalPile
        return None

    def getDestinationPileName(self, cardToMove, sourcePile, destinationPile):
        # if destintion is valid Accum Pile
        for accumPile in self.accumPiles:
            if destinationPile == accumPile.getName():
                if accumPile.canNestUnder(cardToMove):
                    return accumPile

        # if destination is valid Goal Pile
        for goalPile in self.goalPiles:
            if not cardToMove.areCardsEqual(sourcePile.valueOfTopCard()):
                return False  # goal pile can only handle one card at a time
            if destinationPile == goalPile.getName():
                if goalPile.canAdd(cardToMove):
                    return goalPile

        return None

    def isGameOver(self):
        if sum(gp.size() for gp in self.goalPiles) == 52:
            self.isWinner = True
            return True
        return False

    def printGameOutcome(self):
        self.printGameState()
        if self.isWinner:
            print "Victory!!"
        else:
            print "Better luck next time!"
        print self.stats

    def playMove(self, cardToMove, sourcePile, destinationPile):
        destinationPile.add(sourcePile.remove(cardToMove))

    def printGameState(self):
        print self.drawPile
        for gp in self.goalPiles: print str(gp)
        for ap in self.accumPiles: print str(ap)

    def checkPileTotals(self, verbose=False):
        drawPileSize = self.drawPile.size()
        discardPileSize = self.drawPile.discardPile.size()
        accumPilesSize = sum(x.size() for x in self.accumPiles)
        goalPilesSize = sum(y.size() for y in self.goalPiles)
        totalSize = sum([drawPileSize, discardPileSize, accumPilesSize, goalPilesSize])
        assert totalSize == 52
        if verbose: print drawPileSize, discardPileSize, accumPilesSize, goalPilesSize, totalSize


game = Solitaire()
game.playGame()
