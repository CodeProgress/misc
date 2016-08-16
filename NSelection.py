import random
import math
import pylab


class NSelection:
    def __init__(self, num_players):
        self.num_players = num_players
        self.layout = self.create_layout()

    def create_layout(self):
        return [random.randint(0, self.num_players-1) for _ in range(self.num_players)]

    def play_round_pick_one(self, verbose=False):
        if verbose:
            print self.layout
        for index in range(len(self.layout)):
            if self.layout[index] == -1:
                continue
            guess_at_index = self.layout[index]
            guess_at_guess_index = self.layout[guess_at_index]
            if index == guess_at_guess_index and guess_at_index != index:
                self.layout[index] = -1
                self.layout[guess_at_index] = -1
        if verbose:
            print self.layout, '\n'
        self.num_players = len([z for z in self.layout if z != -1])
        self.layout = self.create_layout()


class NMultiSelection:
    def __init__(self, num_players):
        self.num_players = num_players
        self.num_selections = self.get_num_selections()
        self.layout = self.create_layout()

    def get_num_selections(self):
        return int(math.log(self.num_players, 2))
        # return 2

    def create_layout(self):
        return [set(random.sample(xrange(self.num_players), self.num_selections)) - {guess}
                for guess in range(self.num_players)]

    def play_round_pick_log2_num_players(self, verbose=False):
        indices_to_remove = set()
        if verbose:
            print self.layout
        for j in range(len(self.layout)):
            if self.layout[j] == -1:
                continue
            guesses_at_index = self.layout[j]
            for guess in guesses_at_index:
                guesses_at_guess_index = self.layout[guess]
                if j in guesses_at_guess_index and guess != j:
                    indices_to_remove.add(j)
                    indices_to_remove.add(guess)

        for j in indices_to_remove:
            self.layout[j] = -1
        if verbose:
            print self.layout, '\n'
        self.num_players = len([q for q in self.layout if q != -1])
        if self.num_players <= 1:
            self.layout = [q for q in self.layout if q != -1]
        else:
            self.num_selections = self.get_num_selections()
            self.layout = self.create_layout()

counts = []
for i in [2**x for x in range(1, 11)]:
    g = NMultiSelection(i)

    counter = 0
    while len(g.layout) > 2:
        g.play_round_pick_log2_num_players()
        counter += 1

    counts.append(counter)

pylab.plot(counts)
pylab.show()
