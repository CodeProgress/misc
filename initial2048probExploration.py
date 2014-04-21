import random
import pylab
import collections
import fractions

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

def consol(board, memo = {}):
    """returns none, modifies board in place"""
    if board in memo:
        return memo[board]
    b = list(board)
    index = len(b) - 1
    while index > 0:
        if b[index] == b[index - 1]:
            b[index - 1] *= 2
            b.pop(index)
        index -= 1
    memo[board] = tuple(b)
    return memo[board]

def dfs2048(numSlots):
    """DFS implementation that is not memoized, returns exact solution
    once numSlots gets above 4, exponential runtime becomes unreasonable
    run cProfile on this to appreciate the power of the memo in exact2048rec
    """
    outcomes = {}
    q        = [[(2,), 1],[(4,), 1]] #[[board], depth]
    while q:
        pos = q.pop()
        board = pos[0]
        depth = pos[1]
        if len(board) >= numSlots:
            score = max(board)
            probability = fractions.Fraction(1, 2**depth)
            if score in outcomes: outcomes[score] += probability
            else: outcomes[score] = probability
        else:
            for nextPiece in [2,4]:
                nextBoard = board + (nextPiece, )
                nextBoard = consol(nextBoard)
                nextPos = [nextBoard, depth + 1]
                q.append(nextPos)
    
    return sum(x * outcomes[x] for x in outcomes)


def exact2048rec(board = tuple(), depth = 0, numSlots = 5, memo = {}):
    """returns the exact solution as a fraction in lowest terms
    recursive function with memoization to handle overlapping subproblems
    """
    if board in memo: 
        return memo[board] * 2

    if len(board) >= numSlots:
        score = max(board)
        probability = fractions.Fraction(1, 2**depth)
        return probability * score
        #print board, depth
        
    left = consol(board + (2,))
    right = consol(board + (4,))
    
    memo[left] = exact2048rec(left, depth+1, numSlots)
    memo[right] = exact2048rec(right, depth+1, numSlots)
    
    return  memo[left] + memo[right]


#pylab.plot([sim_games(5, 2**x) for x in range(2, 17)])
#pylab.show()

numSlots  = 5
numTrials = 100000

print sim_games(numSlots, numTrials)
print exact2048rec(numSlots = numSlots)




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


