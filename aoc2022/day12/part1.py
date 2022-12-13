import enum
from collections import defaultdict, deque
#grid = [list(x) for x in open(0).read().strip().splitlines()]
grid = [x for x in open("input_t.txt").read().strip().splitlines()]

adj_build = defaultdict()
adj_list = defaultdict()
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

if __name__ == '__main__':
    for i in grid:
        print(i)

    for i, j in enumerate(grid):
        for k, l in enumerate(j):
            adj_build[(i, k)] = l
    
    for k in adj_build:
        for i in DIRS:
            adj_list[(k)] += [DIRS[0][1] +
            print(k)






    


