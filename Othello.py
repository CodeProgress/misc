# Enforce the rules of othello

"""
 1 2 3 4 5 6 7 8
1
2
3
4      w b
5      b w
6
7
8

black moves first
rows numbered along left
cols numbered along top
"""

class Othello:
    def __init__(self):
        self.board = Board()
    
    def check_for_pieces_flip(self, row, col, color):
        # left, right, up, down, diagonals
        pass
    
    def is_legal_move(self, row, col, color):
        pass
    
    def is_game_over(self):
        pass

class Board:
    def __init__(self):
        self.board = [[' ' for  row in xrange(8)] for col in xrange(8)]
        self.rowDict = dict(zip('12345678', range(8)))
        self.colDict = dict(zip('12345678', range(8)))
        self.validRows = set(range(8))
        self.validCols = set(range(8))
        self.create_starting_position()
    
    def create_starting_position(self):
        self.place_white_piece('4', '4')
        self.place_black_piece('4', '5')
        self.place_black_piece('5', '4')
        self.place_white_piece('5', '5')
    
    def get_row_from_str(self, row_number_string):
        assert row_number_string in self.rowDict
        return self.rowDict[row_number_string]
        
    def get_col_from_str(self, col_number_string):
        assert col_number_string in self.colDict
        return self.colDict[col_number_string]
    
    def convert_user_input_to_row_col(self, user_input):
        assert len(user_input) == 2
        row_str = user_input[0]
        col_str = user_input[1]
        return self.get_row_from_str(row_str), self.get_col_from_str(col_str)

    def place_white_piece(self, row, col):
        self.update_board(row, col, 'w')
    
    def place_black_piece(self, row, col):
        self.update_board(row, col, 'b')
        
    def update_board(self, row_str, col_str, color):
        assert color in 'wb'
        row = self.get_row_from_str(row_str)
        col = self.get_col_from_str(col_str)
        self.board[row][col] = color

    def is_row_col_on_board(self, row, col):
        return self.is_row_on_board(row) and self.is_col_on_board(col)

    def is_row_on_board(self, row):
        return row in self.validRows
        
    def is_col_on_board(self, col):
        return col in self.validCols

    def __str__(self):
        boardStr = ''
        boardStr += ' ' + '- '*8 + '\n'
        
        for row in self.board:
            boardStr += '|' + ' '.join(row) + '|' + '\n'
        
        boardStr += ' ' + '- '*8
        return boardStr

game = Othello()

print game.board
