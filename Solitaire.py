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
    
    def isEmpty(self):
        return self.size() == 0
    
    def __str__(self):
        return str(self.pile)
    
class Solitaire(object):
    def __init__(self):
        self.originalDeck = Deck()
        self.drawPile = self.createDrawPile()
        self.discardPile = self.createDiscardPile()
        self.goalPiles = self.createGoalPiles()
        self.accumPiles = self.createAccumPiles()
        self.allPiles = {}     #dictionary: key=name, value=Pile object
        self.addPilesToAllPiles()
        self.isWinner = False
    
    def createDrawPile(self):
        drawPile = Pile('draw', self.originalDeck.deck[::])
        drawPile.shufflePile()
        return drawPile
    
    def createDiscardPile(self):
        return Pile('discard', [])
        
    def createGoalPiles(self):
        allGoalPiles = []
        allGoalPiles.append(Pile('s_goal', []))
        allGoalPiles.append(Pile('h_goal', []))
        allGoalPiles.append(Pile('d_goal', []))
        allGoalPiles.append(Pile('c_goal', []))
        return allGoalPiles
    
    def createAccumPiles(self):
        assert self.drawPile.size() == len(self.originalDeck.deck)
        allAccumPiles = []
        for i in range(7):
            allAccumPiles.append(Pile(str(i), [self.drawPile.popFromTopOfPile() for _ in range(i + 1)]))
        
        assert sum(x.size() for x in allAccumPiles) == 28, 'accum piles have incorrect number of cards'
        return allAccumPiles
        
    def addPilesToAllPiles(self):
        self.addPileToAllPiles(self.drawPile)
        for goalPile in self.goalPiles:
            self.addPileToAllPiles(goalPile)
        for accumPile in self.accumPiles:
            self.addPileToAllPiles(accumPile)
    
    def addPileToAllPiles(self, pile):
        self.allPiles[pile.getName()] = pile        
    
    def playGame(self):
        while not self.isGameOver():
            cardToMove = raw_input("Enter card to move (ex: 3h) ")
            if cardToMove == 'exit': break
            if not self.isLegalCard(cardToMove): 
                print "Invalid Move"
                continue
            
            destinationPile = raw_input("Enter which pile to move card onto (ex: '1') ")
            if destinationPile == 'exit': break
            if not self.isLegalMove(cardToMove, destinationPile): 
                print "Invalid Move"
                continue    
        
            self.playMove(cardToMove, destinationPile)

            self.printGameState()

        self.printGameOutcome()
    
    def isLegalCard(self, cardToMove):
        if len(cardToMove) != 2: return False
        possibleCard = Card(cardToMove[0], cardToMove[1])
        return self.originalDeck.isLegalCard(possibleCard)
    
    def isLegalMove(self, cardToMove, destinationPile):
        # to be completed
        return False 
    
    def isGameOver(self):
        return self.drawPile.isEmpty()

    def printGameOutcome(self):
        if self.isWinner: print "Victory!"
        else: print "Better luck next time!"

    def playMove(self, move):
        
        # drawPile
        
        # goalPiles
        
        # accumPiles
        
        pass
    
    def printGameState(self):
        print self.drawPile.valueOfTopCard()
        print [gp.valueOfTopCard() for gp in self.goalPiles]
        # to be completed
        # print only the VISIBLE accumPile cards


game = Solitaire()
game.playGame()

        