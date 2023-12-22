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
            inps.append([x for x in input()])
        except EOFError:
            break
    R, C = len(inps), len(inps[0])
    for r in range(R):
        for c in range(C):
            if inps[r][c] == 'S':
                sr, sc = r, c
                inps[r][c] = '.'
                break
    been = set()
    def dfs(r,c, i):
        global ans
        if i == 64:
            ans += 1
            return
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if is_grid_valid(R,C, nr,nc) and inps[nr][nc] == '.':
                if (nr, nc, i+1) in been:
                    continue
                been.add((nr, nc, i+1))
                dfs(nr, nc, i+1)
    dfs(sr, sc, 0)
    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append([x for x in input()])
        except EOFError:
            break
    R, C = len(inps), len(inps[0])
    for r in range(R):
        for c in range(C):
            if inps[r][c] == 'S':
                sr, sc = r, c
                inps[r][c] = '.'
                break
    def get_for_x(sr, sc, x):
        been = set()
        n = [0]
        def dfs(r,c, i):
            if i == x:
                n[0] += 1
                return
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if is_grid_valid(R,C, nr,nc) and inps[nr][nc] == '.':
                    if (nr, nc, i+1) in been:
                        continue
                    been.add((nr, nc, i+1))
                    dfs(nr, nc, i+1)
        # def dfs(r,c, i):
        #     if i == x:
        #         n[0] += 1
        #         return
        #     for dr, dc in dirs:
        #         nr, nc = r+dr, c+dc
        #         if is_grid_valid(R,C, nr,nc) and inps[nr][nc] == '.':
        #             if (nr, nc, i+1) in been:
        #                 continue
        #             been.add((nr, nc, i+1))
        #             dfs(nr, nc, i+1)
        dfs(sr, sc, 0)
        return n[0]
    def get_shortest(sr, sc):
        q = deque([(sr, sc, 0)])
        shortest = dict()
        while q:
            r, c, i = q.popleft()
            if (r,c) in shortest:
                continue
            shortest[(r,c)] = i
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if is_grid_valid(R,C, nr,nc) and inps[nr][nc] == '.':
                    q.append((nr, nc, i+1))
        return shortest
    shortest = get_shortest(sr, sc)
    N = 26501365
    N = 50
    full = get_for_x(sr, sc, 200 + N%2)
    corners = [(0,0), (0,C-1), (R-1,0), (R-1,C-1)]
    corner_invs = [(R-1,C-1), (R-1,0), (0,C-1), (0,0)]
    lengths = (N-R) // R
    print(lengths)
    for (dest_r, dest_c), (from_r, from_c) in zip(corners, corner_invs):
        l = shortest[(dest_r, dest_c)]
        # full, inside
        ans += (lengths * (lengths-1)) // 2 * full
        # partial, outside
        ans += lengths * get_for_x(from_r, from_c, (N - l - 2 - (lengths-1)*R))
        # partial, outside 2
        xxx = (N - l - 2 - (lengths) * R)
        if xxx >= 0:
            ans += (lengths + 1) * get_for_x(from_r, from_c, xxx)
        # axes
        ans += ((N-R) // R) * full
    ans += full

    print(ans)