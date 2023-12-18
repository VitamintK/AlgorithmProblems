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
import numpy as np

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
directions = 'RDLU'
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)
def sign_of(x):
    if x==0:
        return 0
    return x/abs(x)
####################################

PART = 1
PART = 2
if PART == 1:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    r, c = 0,0
    grid = set()
    for inp in inps:
        d, x, _ = inp.split()
        x = int(x)
        dr, dc = dirs[directions.index(d)]
        for _ in range(x):
            r += dr
            c += dc
            grid.add((r,c))
    def dfs(r,c):
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if (nr,nc) not in grid:
                grid.add((nr, nc))
                dfs(nr, nc)
    dfs(1,1)

    print(len(grid))
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    r, c = 0,0
    grid = set()
    prev_d = None
    for i in range(len(inps)):
        inp = inps[i]
        def get_d_x(inp):
            _,_,y = inp.split()
            y = y[1:-1]
            x = y[1:-1]
            d = int(y[-1])
            # print(x)
            x = int(x, 16)
            return d, x
        # def get_d_x(inp):
        #     d, x, _ = inp.split()
        #     x = int(x)
        #     return directions.index(d), x
        
        d, x = get_d_x(inp)
        nd, nx = get_d_x(inps[(i+1)%len(inps)])
        pd, px = get_d_x(inps[(i-1)%len(inps)])
        dr, dc = dirs[d]

        if (d+1)%4 == nd:
            x += 1
        if (d-1)%4 != pd:
            x -= 1

        nr, nc = r+dr*x, c+dc*x
        ans += (nr + r) * (nc - c)
        r, c = nr, nc
    print(abs(ans // 2))