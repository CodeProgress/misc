
class TicTacToe(object):
    def __init__(self, edgeLength):
        self.edgeLength = edgeLength
        self.board      = self.make_board()

    def make_board(self):
        return [[' ' for row in range(self.edgeLength)] for col in range(self.edgeLength)]

    def get_rows(self):
        return [self.board[x] for x in range(self.edgeLength)]
    
    def get_cols(self):
        rows = self.get_rows()
        return map(list, zip(*rows))
    
    def move(self, piece, row, col):
        self.board[row][col] = piece

    def __str__(self):
        output = '\n'
        for row in self.board:
            for col in row:
                output += col + '|'
            output += '\n'
        return output


board = TicTacToe(3)

#example game
board.move('x', 0, 0)
board.move('o', 1, 1)
board.move('x', 2, 2)
board.move('o', 0, 2)
board.move('x', 2, 0)
board.move('o', 1, 0)
board.move('x', 2, 1)

print board