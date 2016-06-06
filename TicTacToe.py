import random
import cProfile

class TTTGame(object):
    """
    |0|1|2|
    |3|4|5|
    |6|7|8|
    """
    movesDict = {0: '0,0', 1: '0,1', 2: '0,2',
                 3: '1,0', 4: '1,1', 5: '1,2',
                 6: '2,0', 7: '2,1', 8: '2,2'}

    def __init__(self, board):
        self.board = board
        self.numMoves = 0
        self.pieceToMoveFlag = 0
        self.xPiece = 'x'
        self.oPiece = 'o'
        self.winner = self.board.emptyCellValue

    def unpackMoves(self, moves):
        return [self.movesDict[move] for move in moves]

    def playGame(self):
        while not self.isGameOver():
            move = self.getNextMove()
            if not self.isValidMove(move):
                print "Invalid Move"
                continue
            self.playMove(move)
            print self.board

        print "Game Over! The winner is {}".format(self.winner)

    def simulateGame(self, moves):
        """assumes all moves are valid"""
        for move in moves:
            self.playMove(move)
            if self.isGameOver():
                break

    def getNextMove(self):
        move = raw_input("enter row,col (ex: 1,2): ")
        return move

    def getRowAndColFromValidatedMove(self, move):
        indexOfComma = move.index(',')
        row = int(move[:indexOfComma])
        col = int(move[indexOfComma + 1:])
        return (row, col)

    def playMove(self, move):
        row, col = self.getRowAndColFromValidatedMove(move)
        self.board.setGridValue(row, col, self.getNextPieceToMove())
        self.numMoves += 1

    def getNextPieceToMove(self):
        self.pieceToMoveFlag ^= 1  # flips flag between 0 and 1
        if self.pieceToMoveFlag == 1:
            return self.xPiece
        return self.oPiece

    def isValidMove(self, move):
        if len(move) > 5:
            return False  # suitable for grids up to 99x99 or 9x999
        if move.count(',') != 1:
            return False
        indexOfComma = move.index(',')
        try:
            possibleRowNum = int(move[:indexOfComma])
            possibleColNum = int(move[indexOfComma+1:])
        except ValueError:
            return False

        # make sure square is in grid range
        if not (0 <= possibleRowNum <= self.board.numRows-1):
            return False
        if not (0 <= possibleColNum <= self.board.numCols-1):
            return False

        # make sure square is empty
        if self.board.getGridValue(possibleRowNum, possibleColNum) != ' ':
            return False

        return True

    def isGameOver(self):
        """change this, winner should not be determined as a side effect inside the isGameOver() method"""
        if self.numMoves <= 4:
            return False
        return self.checkRowsForWin() or self.checkColsForWin() or self.checkDiagonalsForWin() or self.numMoves >= 9

    def checkRowsForWin(self):
        for row in range(self.board.numRows):
            vals = set()
            for col in range(self.board.numCols):
                vals.add(self.board.getGridValue(row, col))
            if len(vals) == 1 and ' ' not in vals:
                self.winner = vals.pop()
                return True
        return False

    def checkColsForWin(self):
        for col in range(self.board.numCols):
            vals = set()
            for row in range(self.board.numRows):
                vals.add(self.board.getGridValue(row, col))
            if len(vals) == 1 and ' ' not in vals:
                self.winner = vals.pop()
                return True
        return False

    def checkDiagonalsForWin(self):
        numRows = self.board.numRows
        numCols = self.board.numCols
        if numRows != numCols:
            return False
        diagOneVals = set()
        diagTwoVals = set()
        for i in range(numRows):
            diagOneVals.add(self.board.getGridValue(i, i))
            diagTwoVals.add(self.board.getGridValue(i, numRows - 1 - i))
        if len(diagOneVals) == 1 and ' ' not in diagOneVals:
            self.winner = diagOneVals.pop()
            return True
        if len(diagTwoVals) == 1 and ' ' not in diagTwoVals:
            self.winner = diagTwoVals.pop()
            return True
        return False

class TTTBoard(object):
    def __init__(self, numRows=3, numCols=3):
        assert numRows >= 1 and numCols >= 1
        self.numRows = numRows
        self.numCols = numCols
        self.emptyCellValue = ' '
        self.grid = self.createGrid()
        self.emptyCells = set((row,col) for row in range(self.numRows) for col in range(self.numCols))

    def createGrid(self):
        grid = []
        for row in range(self.numRows):
            grid.append([self.emptyCellValue for _ in range(self.numCols)])
        return grid

    def getGridValue(self, row, col):
        return self.grid[row][col]

    def setGridValue(self, row, col, value):
        self.grid[row][col] = value
        cell = (row, col)
        if cell in self.emptyCells:
            self.emptyCells.remove(cell)

    def getEmptyCells(self):
        """returns a set of tuples of (row, col) corresponding to the empty cells"""
        return self.emptyCells

    def __str__(self):
        output = ""
        for row in range(self.numRows):
            rowAsString = "|" + '|'.join(self.grid[row]) + "|"
            if row != self.numRows - 1:
                rowAsString += '\n'
            output += rowAsString
        return output

def simulateTrials(numTrials):
    outcomes = {'x': 0, 'o': 0, ' ': 0}
    moves = range(9)

    for trial in range(numTrials):
        board = TTTBoard()
        game = TTTGame(board)
        random.shuffle(moves)
        game.simulateGame(game.unpackMoves(moves))
        outcomes[game.winner] += 1

    print outcomes
    return outcomes

if __name__ == '__main__':
    cProfile.run("simulateTrials(10000)")

