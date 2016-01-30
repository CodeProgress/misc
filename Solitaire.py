#Solitaire 

import random

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
        return self.rank+self.suit
    
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
        return self.getIterable().index(card)
    
    def isEmpty(self):
        return self.size() == 0
    
    def __str__(self):
        return str(self.getName()) + ' ' + str(self.valueOfTopCard())
    
class DrawPile(Pile):
    def __str__(self):
        return str(self.getName()) + ' ' + str(self.valueOfTopCard())

class GoalPile(Pile):
    def __init__(self, name, iterable):
        super(GoalPile, self).__init__(name, iterable)

    def canAdd(self, possibleCard):
        assert possibleCard.rank in self.indexes
        if self.isEmpty():
            return self.indexes[possibleCard.rank] == 0 and possibleCard.suit == self.getName()
        return self.indexes[possibleCard.rank] - self.indexes[self.valueOfTopCard()] == 1
    
class AccumPile(Pile):
    def __init__(self, name, iterable, visibilityIndex):
        super(AccumPile, self).__init__(name, iterable)
        self.visibilityIndex = visibilityIndex
    
    def popFromTopOfPile(self):
        assert self.getIterable(), 'Attempting to pop from an empty Pile!'
        cardToPop = self.getIterable().pop()
        if self.visibilityIndex > self.size():
            self.visibilityIndex -= 1
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
        return (self.indexes[self.valueOfTopCard().getRank()] - self.indexes[possibleCard.rank] == 1) \
                    and possibleCard.isRed() != self.valueOfTopCard().isRed()
    
    def __str__(self):
        return str(self.getName()) + ' x{} '.format(max(self.visibilityIndex, 0)) + str([str(card) for card in self.getIterable()[self.visibilityIndex:]])
    
class Solitaire(object):
    def __init__(self):
        self.originalDeck = Deck()
        self.drawPile = self.createDrawPile()
        self.discardPile = self.createDiscardPile()
        self.goalPiles = self.createGoalPiles()
        self.accumPiles = self.createAccumPiles()
        self.isWinner = False
    
    def createDrawPile(self):
        drawPile = DrawPile('draw', self.originalDeck.deck[::])
        drawPile.shufflePile()
        return drawPile
    
    def createDiscardPile(self):
        return Pile('discard', [])
        
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
            allAccumPiles.append(AccumPile(str(i), [self.drawPile.popFromTopOfPile() for _ in range(i + 1)], visibilityIndex))
        
        assert sum(x.size() for x in allAccumPiles) == 28, 'accum piles have incorrect number of cards'
        return allAccumPiles 
    
    def playGame(self):
        while not self.isGameOver():
            self.printGameState()
            
            cardToMoveText = raw_input("Enter card to move (ex: 3h or flip) ")
            if cardToMoveText == 'exit': 
                break
            elif cardToMoveText == 'flip':
                self.flipToNextDrawCard()
                continue
            
            cardToMove = self.createCardToMove(cardToMoveText)
            
            if not cardToMove:
                print "Invalid Move"
                continue
            
            sourcePile = self.getSourcePileOfCardToMove(cardToMove)
            if not sourcePile: 
                print "Invalid Move"
                continue
            
            destinationPile = raw_input("Enter which pile to move card onto (ex: '1') ")
            if destinationPile == 'exit': 
                break
            if not self.isLegalDestinationPileName(cardToMove, sourcePile, destinationPile): 
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
    
    def flipToNextDrawCard(self):
        assert not self.drawPile.isEmpty()   
        self.discardPile.addToTopOfPile(self.drawPile.popFromTopOfPile())
        if self.drawPile.size() == 0:
            for i in range(self.discardPile.size()):
                self.drawPile.addToTopOfPile(self.discardPile.popFromTopOfPile())
            assert self.discardPile.size() == 0
            assert self.drawPile.size() > 0
            self.drawPile.shufflePile()

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
    
    def isLegalDestinationPileName(self, cardToMove, sourcePile, destinationPile):
        # if destintion is valid Accum Pile
        for accumPile in self.accumPiles:
            if destinationPile == accumPile.getName():
                return accumPile.canNestUnder(cardToMove)
                
        # if destination is valid Goal Pile
        for goalPile in self.goalPiles:
            if destinationPile == goalPile.getName():
                return goalPile.canAdd(cardToMove)

        return False
    
    def isGameOver(self):
        return sum(gp.size() for gp in self.goalPiles) == 52

    def printGameOutcome(self):
        if self.isWinner: print "Victory!"
        else: print "Better luck next time!"

    def playMove(self, cardToMove, sourcePile, destinationPile):
        
        # drawPile
            # cardName, goalPile: move card to destintion pile
            # cardName, accumPile: move card to destintion pile
            # cleanup - after a drawPile move, if draw pile is empty, move discard onto draw
        
        # goalPiles
            # cardName, accumPile: move card to destintion pile
        
        # accumPiles
            # cardName, goalPile: move card to goal pile
            # cardName, accumPile: move splice to accum pile
        
        pass
    
    def printGameState(self):
        print self.drawPile
        for gp in self.goalPiles: print str(gp)
        for ap in self.accumPiles: print str(ap)

game = Solitaire()
game.playGame()

        