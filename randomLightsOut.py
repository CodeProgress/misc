import random


class LightsOut:
    def __init__(self, side_length, square_type):
        self.side_length = side_length
        self.board = [[square_type(row, col) for row in range(self.side_length)] for col in range(self.side_length)]

    def __str__(self):
        output = ''
        final_row_index = len(self.board) - 1
        for i, row in enumerate(self.board):
            row_str = [str(x) for x in row]
            output += ' '.join(row_str)
            if i != final_row_index:
                output += '\n'
        return output

    def flip_square_and_neighbors(self, square):
        square.flip()
        for sq_coordinates in square.get_neighbor_squares_coordinates_to_flip():
            if self.is_coordinate_on_board(sq_coordinates):
                self.get_square_from_coordinates(sq_coordinates).flip()

    def get_square_from_coordinates(self, coordinates):
        row, col = coordinates
        return self.board[row][col]

    def is_coordinate_on_board(self, coordinates):
        row, col = coordinates
        return (0 <= row < self.side_length) and (0 <= col < self.side_length)

    def print_series_of_moves(self, moves):
        print self, '\n'
        for move in moves:
            self.flip_square_and_neighbors(self.get_square_from_coordinates(move))
            print self, '\n'


class Square:
    def __init__(self, row, col):
        self.value = 'x'
        self.row = row
        self.col = col

    def flip(self):
        if self.value == 'x':
            self.value = 'o'
        else:
            self.value = 'x'

    def get_neighbor_squares_coordinates_to_flip(self):
        north = (self.row + 1, self.col)
        south = (self.row - 1, self.col)
        east = (self.row, self.col - 1)
        west = (self.row, self.col + 1)
        return [north, south, east, west]

    def __str__(self):
        return self.value


class RandomSquare(Square):
    def __init__(self, row, col):
        Square.__init__(self, row, col)
        self.probability_of_flip = .5

    def flip(self):
        if random.random() < self.probability_of_flip:
            if self.value == 'x':
                self.value = 'o'
            else:
                self.value = 'x'


game = LightsOut(4, Square)
randGame = LightsOut(4, RandomSquare)

print "Start standard game:"
game.print_series_of_moves([(1, 1), (0, 0)])

print "Start random game:"
randGame.print_series_of_moves([(1, 1), (0, 0)])
