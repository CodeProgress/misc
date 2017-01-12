import itertools
import random


def is_conflict(sq1, sq2):
    if sq1[0] == sq2[0]:
        return True
    if sq1[1] == sq2[1]:
        return True
    if abs(sq1[0]-sq2[0]) == abs(sq1[1] - sq2[1]):
        return True
    return False

def any_conflicts(board):
    if len(board) <= 1:
        return False
    queen = board[0]
    for q in board[1:]:
        if is_conflict(queen, q):
            return True
    return any_conflicts(board[1:])


def get_all_solutions(size=8):
    all_solutions = []
    perms = itertools.permutations(range(size))
    for board in perms:
        sq_board = [(x, board[x]) for x in range(len(board))]
        if not any_conflicts(sq_board):
            all_solutions.append(board)
    return all_solutions

def solution_in_rand_permutations(size=8):
    start = range(size)
    num_trials = 0
    while True:
        num_trials += 1
        board = random.sample(start, size)
        sq_board = [(x, board[x]) for x in range(size)]
        if not any_conflicts(sq_board):
            print "Number of trials needed: {}".format(num_trials)
            return board
    

print len(get_all_solutions())
print solution_in_rand_permutations(8)
