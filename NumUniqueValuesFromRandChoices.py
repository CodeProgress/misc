import random
import pylab


def num_unique(numRandPicks, limit):
    return len(set(random.randint(1, limit) for _ in xrange(numRandPicks)))


def plot_num_unique_to_limit(numPicksLimit, valueLimit):
    """Plots the quantity of unique values from n random selections
    example: numPicksLimit = 1000, valueLimit = 100
             x axis will be 1 - 1000  the number of random picks
             y axis will be 1 - 100   how man unique numbers were selected after n random picks
             sample result:
                100 random picks between 1 and 100 (inclusive) will give roughly only 64 unique numbers
    expected result: numPicksLimit needs to be roughly 10x valueLimit to guarantee all numbers are picked
    """
    xValues = range(1, numPicksLimit + 1)
    yValues = [num_unique(i, valueLimit) for i in range(1, numPicksLimit + 1)]
    pylab.plot(xValues, yValues)

    pylab.xlabel('Number of Random Picks Between 1 and {}'.format(numPicksLimit))
    pylab.ylabel('Number of Unique Values Selected Between 1 and {}'.format(valueLimit))
    pylab.title('Quantity of Unique Values from N Random Selections')
    pylab.show()

plot_num_unique_to_limit(1000, 100)