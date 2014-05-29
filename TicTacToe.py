
class TicTacToe(object):
    def __init__(self, edgeLength = 3, winLength = 3):
        assert winLength <= edgeLength
        self.edgeLength = edgeLength
        self.board      = self.make_board()
        self.winLength  = winLength

    def make_board(self):
        return [[' ' for row in range(self.edgeLength)] for col in range(self.edgeLength)]

    def get_rows(self):
        return [self.board[x] for x in range(self.edgeLength)]
    
    def get_cols(self):
        rows = self.get_rows()
        return map(list, zip(*rows))
    
    def get_diags(self):
        #diags = []
        #for i in range(self.winLength-1, self.edgeLength):
        #    colNum = 0
        #    while colNum < i:
        pass
    def move(self, piece, row, col):
        self.board[row][col] = piece
    
    def is_winning_state(self):
        pass

    def __str__(self):
        output = '\n'
        for row in self.board:
            for col in row:
                output += col + '|'
            output += '\n'
        return output


board = TicTacToe()

#example game
board.move('x', 0, 0)
board.move('o', 1, 1)
board.move('x', 2, 2)
board.move('o', 0, 2)
board.move('x', 2, 0)
board.move('o', 1, 0)
board.move('x', 2, 1)

print board