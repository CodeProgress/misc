import random
import pprint


class MagicSquare(object):
    def __init__(self, north, east, south, west):
        self.North = north
        self.East = east
        self.South = south
        self.West = west


class MagicGrid(object):
    def __init__(self, sideLength):
        # preconditions
        assert sideLength >= 1

        # variables
        self.sideLength = sideLength
        self.square = [[None] * sideLength for _ in range(sideLength)]
        self.directions = ['North', 'East', 'South', 'West']
        self.start = (0,0)
        self.end = (self.sideLength-1 , self.sideLength-1)
        self.allDestinationSquares = set()# note: this is different than 'possible' destination squares

        # methods
        self.create_magic_squares()

        # postconditions
        assert self.sideLength >= 1
        assert self.end > self.start


    def create_magic_squares(self):
        for row in range(self.sideLength):
            for col in range(self.sideLength):
                self.square[row][col] = self.create_magic_square()

    def create_random_directions(self):
        randomDirections = []
        for _ in self.directions:
            row = random.randint(0, self.sideLength-1)
            col = random.randint(0, self.sideLength-1)
            coord = (row, col)
            randomDirections.append(coord)
            self.allDestinationSquares.add(coord)
        return randomDirections

    def create_magic_square(self):
        return MagicSquare(*self.create_random_directions())

    def is_ending_square_in_destination_squares(self):
        # 100,000 trials percent chance of True:
        #     size 8: 98.331, 7: 98.209, 6: 98.214, 5: 98.377 %, 4: 98.454 %, 3: 98.481 %, 2: 98.982
        return ms.end in ms.allDestinationSquares

    def __repr__(self):
        # refactor...
        allBoxes = []
        for row in range(self.sideLength):
            boxesInRow = []
            for col in range(self.sideLength):
                linesInRow = []
                sq = self.square[row][col]
                linesInRow.append('|------------------|')
                linesInRow.append('|      {}      |'.format(sq.North))
                linesInRow.append('|{}      {}|'.format(sq.West, sq.East))
                linesInRow.append('|      {}      |'.format(sq.South))
                linesInRow.append('|------------------|')
                boxesInRow.append(linesInRow)
            allBoxes.append(boxesInRow)
        reorderedAllBoxes = []
        for row in range(self.sideLength):
            reorderedAllBoxes.append(zip(*[allBoxes[row][x] for x in range(self.sideLength)]))
        
        finalString = ''
        for i in reorderedAllBoxes:
            for j in i:
                finalString += ''.join(j) + '\n'
        return finalString

# counter = 0
# for i in range(1000):
#     ms = MagicGrid(4)
#     if ms.is_ending_square_in_destination_squares():
#         counter += 1
# print counter

ms = MagicGrid(4)
print ms

