import random
import math
import sys

class Tree(object):
    def __init__(self):
        self.tree = [0]
        self.currentEntry = 1

    def insert_random_into_tree(self, index=1):
        self.resize_tree(index)
        if self.tree[index] == 0:
            self.insert(index)
        else:
            self.insert_random(index)
     
    def insert_random(self, index):
        if random.random() < .5:
            self.insert_left(index)
        else:
            self.insert_right(index)
    
    def resize_tree(self, index):
        if index >= len(self.tree):
            self.tree+=[0]*len(self.tree)   
              
    def insert(self, index):
        self.tree[index] = self.currentEntry
        self.currentEntry += 1
    
    def insert_left(self, index):
        index *= 2
        self.insert_random_into_tree(index)
    
    def insert_right(self, index):
        index *= 2
        index += 1
        self.insert_random_into_tree(index)
    
    def calc_tree_height(self):
        return int(math.log(len(self.tree), 2))

    def insert_n_numbers(self, num=1000):
        self.currentEntry = 1
        for i in xrange(num):
            self.insert_random_into_tree()

    def print_stats(self):
        print 'length of tree = {}'.format(len(self.tree))
        print 'tree height = \t {}'.format(self.calc_tree_height())
        print 'memory usage = \t {}'.format(sys.getsizeof(self.tree))
    
class TreeAsDict(Tree):
    def __init__(self):
        self.tree = {}
        self.currentEntry = 1
        self.maxIndex = 1

    def insert_random_into_tree(self, index=1):
        if not self.tree.has_key(index):
            self.insert(index)
            if index > self.maxIndex: self.maxIndex = index
        else:
            self.insert_random(index)   

    def calc_tree_height(self):
        return int(math.log(self.maxIndex, 2)) + 1


t = Tree()     
t.insert_n_numbers()
t.print_stats()

tDict = TreeAsDict()     
tDict.insert_n_numbers()
tDict.print_stats()


