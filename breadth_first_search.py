import Queue


def bfs(start, goal, successor_function):
    visited = set()
    q = Queue.Queue()
    q.put([start])
    while not q.empty():
        cur_path = q.get()
        val = cur_path[-1]
        if val == goal:
            return cur_path
        for next_val in successor_function(val):
            if next_val not in visited:
                q.put(cur_path + [next_val])
                visited.add(next_val)

def nearest_ints(int_val):
    return int_val + 1, int_val -1


print bfs(0, 10, nearest_ints)
