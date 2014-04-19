import random
import pylab
import collections

# 1D 2048 board simulation
# initial exploration:

def sim_game(numSlots):
    board = [0]*numSlots
    
    while True:
        add_digit(board)
        consolidate(board)
        if board[-1] != 0:
            break
    return board
    
def add_digit(board):
    nextPiece = random.choice([2,4])
    board[board.index(0)] = nextPiece
        
def consolidate(board):
    """returns none, modifies board in place"""
    lenBoard = len(board)
    index = lenBoard - 1
    while index > 0:
        if board[index] != 0:
            if board[index] == board[index -1]:
                board[index -1] *= 2
                board[index] = 0
                #shift everything down
                if index < len(board) - 1:
                    board[index] = board[index + 1]
                    board[index + 1] = 0
                    #recheck that index
                    index += 1
        index -= 1

def sim_games(numSlots, numGames = 100, verbose = False):
    games = []
    posGames = collections.Counter()
    for i in xrange(numGames):
        outcome = sim_game(numSlots)
        games.append(outcome)
        posGames[tuple(outcome)] += 1
    if verbose: print posGames
    return sum(max(x) for x in games)/float(len(games))

#pylab.plot([sim_games(5, 2**x) for x in range(2, 17)])
#pylab.show()

print sim_games(2, 100000, True)




#Possible outcomes for N=5
posOutcomes =  {
  (2, 4, 2, 4, 2),
  (2, 4, 2, 8, 2),
  (2, 4, 2, 8, 4),
  (2, 8, 2, 4, 2),
  (2, 8, 2, 8, 2),
  (2, 8, 2, 8, 4),
  (2, 8, 4, 2, 4),
  (2, 16, 2, 4, 2),
  (2, 16, 2, 8, 2),
  (2, 16, 2, 8, 4),
  (2, 16, 4, 2, 4),
  (2, 16, 8, 2, 4),
  (2, 16, 8, 4, 2),
  (2, 32, 2, 4, 2),
  (2, 32, 2, 8, 2),
  (2, 32, 2, 8, 4),
  (2, 32, 4, 2, 4),
  (2, 32, 8, 2, 4),
  (2, 32, 8, 4, 2),
  (2, 32, 16, 2, 4),
  (2, 32, 16, 4, 2),
  (2, 32, 16, 8, 2),
  (2, 32, 16, 8, 4),
  (4, 2, 4, 2, 4),
  (4, 2, 8, 2, 4),
  (4, 2, 8, 4, 2),
  (4, 2, 16, 2, 4),
  (4, 2, 16, 4, 2),
  (4, 2, 16, 8, 2),
  (4, 2, 16, 8, 4),
  (8, 2, 4, 2, 4),
  (8, 2, 8, 2, 4),
  (8, 2, 8, 4, 2),
  (8, 2, 16, 2, 4),
  (8, 2, 16, 4, 2),
  (8, 2, 16, 8, 2),
  (8, 2, 16, 8, 4),
  (8, 4, 2, 4, 2),
  (8, 4, 2, 8, 2),
  (8, 4, 2, 8, 4),
  (16, 2, 4, 2, 4),
  (16, 2, 8, 2, 4),
  (16, 2, 8, 4, 2),
  (16, 2, 16, 2, 4),
  (16, 2, 16, 4, 2),
  (16, 2, 16, 8, 2),
  (16, 2, 16, 8, 4),
  (16, 4, 2, 4, 2),
  (16, 4, 2, 8, 2),
  (16, 4, 2, 8, 4),
  (16, 8, 2, 4, 2),
  (16, 8, 2, 8, 2),
  (16, 8, 2, 8, 4),
  (16, 8, 4, 2, 4),
  (32, 2, 4, 2, 4),
  (32, 2, 8, 2, 4),
  (32, 2, 8, 4, 2),
  (32, 2, 16, 2, 4),
  (32, 2, 16, 4, 2),
  (32, 2, 16, 8, 2),
  (32, 2, 16, 8, 4),
  (32, 4, 2, 4, 2),
  (32, 4, 2, 8, 2),
  (32, 4, 2, 8, 4),
  (32, 8, 2, 4, 2),
  (32, 8, 2, 8, 2),
  (32, 8, 2, 8, 4),
  (32, 8, 4, 2, 4),
  (32, 16, 2, 4, 2),
  (32, 16, 2, 8, 2),
  (32, 16, 2, 8, 4),
  (32, 16, 4, 2, 4),
  (32, 16, 8, 2, 4),
  (32, 16, 8, 4, 2),
  (64, 2, 4, 2, 4),
  (64, 2, 8, 2, 4),
  (64, 2, 8, 4, 2),
  (64, 2, 16, 2, 4),
  (64, 2, 16, 4, 2),
  (64, 2, 16, 8, 2),
  (64, 2, 16, 8, 4),
  (64, 4, 2, 4, 2),
  (64, 4, 2, 8, 2),
  (64, 4, 2, 8, 4),
  (64, 8, 2, 4, 2),
  (64, 8, 2, 8, 2),
  (64, 8, 2, 8, 4),
  (64, 8, 4, 2, 4),
  (64, 16, 2, 4, 2),
  (64, 16, 2, 8, 2),
  (64, 16, 2, 8, 4),
  (64, 16, 4, 2, 4),
  (64, 16, 8, 2, 4),
  (64, 16, 8, 4, 2),
  (64, 32, 2, 4, 2),
  (64, 32, 2, 8, 2),
  (64, 32, 2, 8, 4),
  (64, 32, 4, 2, 4),
  (64, 32, 8, 2, 4),
  (64, 32, 8, 4, 2),
  (64, 32, 16, 2, 4),
  (64, 32, 16, 4, 2),
  (64, 32, 16, 8, 2),
  (64, 32, 16, 8, 4)}


