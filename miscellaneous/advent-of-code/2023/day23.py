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

INTERVAL_TYPE_INCLUSIVE = 0
INTERVAL_TYPE_EXCLUSIVE = 1
# def make_interval_class(start_type=INTERVAL_TYPE_INCLUSIVE, end_type=INTERVAL_TYPE_EXCLUSIVE):
#     class Interval:
#         start_type = start_type
#         end_type = end_type
#         def __init__(self, start, end):
#             self.start = start
#             self.end = end
# def merge(interval_a, interval_b):
#     interval = (min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1]))
#     if interval[0] > interval[1]:
#         return None
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
    for c in range(len(inps[0])):
        if inps[0][c] == '.':
            sc = c
            break
    for c in range(len(inps[0])):
        if inps[-1][c] == '.':
            ec = c
            break
    R, C = len(inps), len(inps[0])
    def dfs(r, c, been):
        if r == R-1:
            return 0
        best = None
        for dr, dc in dirs:
            if inps[r][c] == '<' and dc != -1:
                continue
            if inps[r][c] == '>' and dc != 1:
                continue
            if inps[r][c] == '^' and dr != -1:
                continue
            if inps[r][c] == 'v' and dr != 1:
                continue
            nr, nc = r+dr, c+dc
            if is_grid_valid(R, C, nr, nc) and inps[nr][nc] in '.<>v^' and (nr, nc) not in been:
                been.add((nr, nc))
                if inps[nr][nc] != '.':
                    been = been.copy()
                res = dfs(nr, nc, been)
                if res is not None:
                    if best is None:
                        best = res + 1
                    else:
                        best = max(best, res + 1)
        return best
            
    
    ans = dfs(0, sc, {(0, sc)})
    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for c in range(len(inps[0])):
        if inps[0][c] == '.':
            sc = c
            break
    for c in range(len(inps[0])):
        if inps[-1][c] == '.':
            ec = c
            break
    R, C = len(inps), len(inps[0])
    junctions = [(0, sc), (R-1, ec)]
    for r in range(R):
        for c in range(C):
            neighbor_slides = 0
            if inps[r][c] != '.':
                continue
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if is_grid_valid(R, C, nr, nc) and inps[nr][nc] in '<>v^':
                    neighbor_slides += 1
            if neighbor_slides >= 3:
                junctions.append((r,c,))
    def dfs(j, been, start):
        r,c = j
        if (r,c) in junctions and (r,c) != start:
            return [((r,c), 0)]
        neighbor_distances = []
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if is_grid_valid(R, C, nr, nc) and inps[nr][nc] in '.<>v^' and (nr, nc) not in been:
                been2 = been.copy()
                been2.add((nr, nc))
                # if inps[nr][nc] != '.':
                #     been = been.copy()
                neighbor_distances.extend(dfs((nr, nc), been2, start))
                
        return [(j, d+1) for (j,d) in neighbor_distances]
    
    neighbor_distancess = dict()
    for junction in junctions:
        neighbor_distances = dfs(junction, {(junction)}, junction)
        neighbor_distancess[junction] = neighbor_distances
    def dfs2(junction, been):
        if junction == (R-1, ec):
            return 0
        best = None
        for (j, d) in neighbor_distancess[junction]:
            been2 = been.copy()
            if j not in been2:
                been2.add(j)
                res = dfs2(j, been2)
                if res is not None:
                    if best is None:
                        best = res + d
                    else:
                        best = max(best, res + d)
        return best
    print('starting dfs2')
    ans = dfs2((0, sc), {(0, sc)})
    print(ans)