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
directions = 'RDLU'
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)
def sign_of(x):
    if x==0:
        return 0
    return x/abs(x)

if False:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    grid = set()
    for inp in inps:
        xs = get_ints(inp)
        grid.add(tuple(xs))
    for x,y,z in grid:
        for index in [0,1,2]:
            for d in [-1,1]:
                    new_coords = [x,y,z]
                    new_coords[index] += d
                    if tuple(new_coords) not in grid:
                        ans += 1
    

    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    grid = set()
    for inp in inps:
        xs = get_ints(inp)
        grid.add(tuple(xs))
    outside = [0,0,0]
    n,m,o = 22,22,22
    seen = set()
    def dfs(coord):
        global ans
        for index in [0,1,2]:
            for d in [-1,1]:
                new_coords = list(coord)
                new_coords[index] += d
                new_coords = tuple(new_coords)
                x,y,z = new_coords
                if -1<=x<n and -1<=y<m and -1<=z<o:
                    if (x,y,z) in grid:
                        ans += 1
                    elif new_coords not in seen:
                        seen.add(new_coords)
                        dfs(new_coords)
    dfs(outside)

    print(ans)