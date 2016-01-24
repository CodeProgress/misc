#Solitaire 

import random

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.isRed = suit in 'hd'
        self.isBlack = suit in 'sc'
        assert self.isRed != self.isBlack # assures suit in 'shdc'
    
    def __str__(self):
        return self.rank+self.suit
    
class Deck(object):
    def __init__(self):
        self.ranks = set('23456789TJQKA')
        self.suits = set('shdc')
        self.deck = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def isLegalCard(self, card):
        return card.rank in self.ranks and card.suit in self.suits

class Pile(object):
    def __init__(self, name, iterable):
        self.pile = (name, iterable)

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
    
class AccumPile(Pile):
    def __init__(self, name, iterable, visibilityIndex):
        self.pile = (name, iterable)
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
        allGoalPiles.append(Pile('s', []))
        allGoalPiles.append(Pile('h', []))
        allGoalPiles.append(Pile('d', []))
        allGoalPiles.append(Pile('c', []))
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
            
            cardToMove = raw_input("Enter card to move (ex: 3h or flip) ")
            if cardToMove == 'exit': 
                break
            elif cardToMove == 'flip':
                self.flipToNextDrawCard()
                continue
            if not self.isLegalCard(cardToMove): 
                print "Invalid Move"
                continue
            
            destinationPile = raw_input("Enter which pile to move card onto (ex: '1') ")
            if destinationPile == 'exit': 
                break
            if not self.isLegalDestinationPileName(destinationPile): 
                print "Invalid Pile"
                continue    
            if not self.isLegalMove(cardToMove, destinationPile):
                print "Invalid Move"
                continue
        
            self.playMove(cardToMove, destinationPile)

        self.printGameOutcome()
    
    def flipToNextDrawCard(self):
        assert not self.drawPile.isEmpty()   
        self.discardPile.addToTopOfPile(self.drawPile.popFromTopOfPile())
        if self.drawPile.size() == 0:
            for i in range(self.discardPile.size()):
                self.drawPile.addToTopOfPile(self.discardPile.popFromTopOfPile())
            assert self.discardPile.size() == 0
            assert self.drawPile.size() > 0
            self.drawPile.shufflePile()
        print self.drawPile.size()
        print self.discardPile.size()

    def isLegalCard(self, cardToMove):
        if len(cardToMove) != 2: return False
        possibleCard = Card(cardToMove[0], cardToMove[1])
        return self.originalDeck.isLegalCard(possibleCard)
    
    def isLegalDestinationPileName(self, destinationPile):
        if any(x.getName() == destinationPile for x in self.accumPiles):
            return True
        if any(y.getName() == destinationPile for y in self.goalPiles):
            return True
        return False
    
    def isLegalMove(self, cardToMove, destinationPile):
        # determine where card to move is coming from
        
        return False
    
    def isGameOver(self):
        return sum(gp.size() for gp in self.goalPiles) == 52

    def printGameOutcome(self):
        if self.isWinner: print "Victory!"
        else: print "Better luck next time!"

    def playMove(self, move, destinationPile):
        
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

        