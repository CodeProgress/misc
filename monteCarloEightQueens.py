import itertools
import random

# quick first draft

perms = itertools.permutations(range(4))

def is_conflict(sq1, sq2):
    if sq1[0] == sq2[0]:
        return True
    if sq1[1] == sq2[1]:
        return True
    if abs(sq1[0]-sq2[0]) == abs(sq1[1] - sq2[1]):
        return True
    return False


board = []
rows = range(8)
cols = range(8)
counter = 0
max_num_queens = 0

while len(board) < 8:
    counter += 1
    conflict = False
    rand_row = random.choice(rows)
    rand_col = random.choice(cols)
    pos_q = (rand_row, rand_col)
    for q in board:
        if is_conflict(q, pos_q):
            conflict = True
            break
    if not conflict:
        rows.remove(rand_row)
        cols.remove(rand_col)
        board.append(pos_q)
    else:
        rows = range(8)
        cols = range(8)
        board = []
    if len(board)> max_num_queens:
        board_size = len(board)
    if counter > 10000:
        break
        
print board