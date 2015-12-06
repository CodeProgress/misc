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
        assert sideLength >= 1
        self.sideLength = sideLength
        self.square = [[None] * sideLength for _ in range(sideLength)]
        self.directions = ['North', 'East', 'South', 'West']
        self.create_magic_squares()
        self.start = (0,0)
        self.end = (self.sideLength, self.sideLength)

    def create_magic_squares(self):
        for row in range(self.sideLength):
            for col in range(self.sideLength):
                self.square[row][col] = self.create_magic_square()

    def create_random_directions(self):
        return [(random.randint(0, self.sideLength-1), random.randint(0, self.sideLength-1)) for _ in self.directions]

    def create_magic_square(self):
        return MagicSquare(*self.create_random_directions())

    def __repr__(self):
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

        pprint.pprint(reorderedAllBoxes)
        return 'To be completed...'

ms = MagicGrid(3)

print ms
