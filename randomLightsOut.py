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

    def are_all_lights_out(self):
        for row in self.board:
            for squ in row:
                if squ.is_on():
                    return False
        return True


class Square:
    LIGHT_ON = 'o'
    LIGHT_OUT = 'x'

    def __init__(self, row, col):
        self.value = self.LIGHT_ON
        self.row = row
        self.col = col

    def flip(self):
        if self.value == self.LIGHT_OUT:
            self.value = self.LIGHT_ON
        else:
            self.value = self.LIGHT_OUT

    def is_out(self):
        return self.value == self.LIGHT_OUT

    def is_on(self):
        return self.value == self.LIGHT_ON

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
            if self.value == self.LIGHT_OUT:
                self.value = self.LIGHT_ON
            else:
                self.value = self.LIGHT_OUT

boardSize = 6
# game = LightsOut(boardSize, Square)
game = LightsOut(boardSize, RandomSquare)

# print "Start standard game:"
# game.print_series_of_moves([(1, 1), (0, 0)])
#
# print "Start random game:"
# randGame.print_series_of_moves([(1, 1), (0, 0)])

counter = 0
while not game.are_all_lights_out():
    randRow = random.randint(0, boardSize-1)
    randCol = random.randint(0, boardSize-1)
    sq = game.get_square_from_coordinates((randRow, randCol))
    if sq.is_out():
        continue
    game.flip_square_and_neighbors(sq)
    counter += 1
    if counter % 100000 == 0:
        print counter
        print game
print game
print counter
