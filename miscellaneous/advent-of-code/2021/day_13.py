from collections import defaultdict, deque, Counter
# d = deque()
# d.append(5)
# x = d.popleft()
import re
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist") 
# # or re.search
# >>> m.group(0)       # The entire match
# 'Isaac Newton'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'Isaac'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'Newton'
# >>> m.group(1, 2)    # Multiple arguments give us a tuple.
# ('Isaac', 'Newton')
from heapq import heappush, heappop
# >>> heap = []
# >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# >>> for item in data:
# ...     heappush(heap, item)
# heap[0] is the smallest item
import string
# string.ascii_lowercase == 'abcde...'
# string.ascii_uppercase == 'ABCDE...'
from functools import lru_cache
# @lru_cache(maxsize=None)

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

if True:
    ans = 0
    points = []
    X, Y = 0,0
    while True:
        try:
            inp = input()
            if inp.strip() == '':
                break
            x,y = get_ints(inp)
            points.append((x,y))
            X = max(X, x)
            Y = max(Y, y)
        except Exception as e:
            break
    while True:
        try:
            inp = input()
            # print(inp)
            coord = inp.split()[-1][0]
            num = get_ints(inp)[0]
            np = []
            print(coord)
            if coord == 'x':
                for x,y in points:
                    if x < num:
                        np.append((x,y))
                    else:
                        np.append((2*num-x, y))
            else:
                print(num)
                for x,y in points:
                    if y < num:
                        np.append((x,y))
                    else:
                        np.append((x, 2*num-y))
            points = np
        except Exception as e:
            print(e)
            break
    print(len(set(points)))
    print(set(points))
    grid = [[' ' for j in range(100)] for i in range(100)]
    for x,y in points:
        grid[y][x] = '8'
    for line in grid:
        print(''.join(line))
else:
    pass