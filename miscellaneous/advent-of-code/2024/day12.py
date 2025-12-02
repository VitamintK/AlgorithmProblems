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
    def dfs(x,r,c):
        a, b = 0, 1
        inps[r][c] = x + '0'
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if not is_grid_valid(R, C, nr, nc) or inps[nr][nc][0] != x:
                a += 1
            elif inps[nr][nc] == x:
                aa, bb = dfs(x, nr, nc)
                a += aa
                b += bb
        return a, b

    for r in range(R):
        for c in range(C):
            if len(inps[r][c]) ==1:
                p, a = dfs(inps[r][c], r,c)
                print(inps[r][c], p, a)
                ans += p * a

    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append([[x, 0,0, 0, 0,0] for x in input()])
        except EOFError:
            break
    R, C = len(inps), len(inps[0])
    def dfs(x,r,c):
        a, b = 0, 1
        inps[r][c][1] = 1
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if not is_grid_valid(R, C, nr, nc) or inps[nr][nc][0] != x:
                didx = dirs.index((dr, dc))
                a += 1 - inps[r][c][didx+2]
                for ddr, ddc in (dirs[(didx+1)%4], dirs[(didx-1)%4]):
                    nrr, ncc = r+ddr, c+ddc
                    if is_grid_valid(R, C, nrr, ncc) and inps[nrr][ncc][0] == x and ((not is_grid_valid(R, C, nrr+dr, ncc+dc)) or inps[nrr+dr][ncc+dc][0] != x):
                        inps[nrr][ncc][didx+2] += 1
                    # and (len(inps[nrr][ncc])==1 or inps[nrr][ncc][didx] == 0):
                        # a -= 1
                inps[r][c][didx+2] = 1
            elif inps[nr][nc][0] == x and inps[nr][nc][1] == 0:
                aa, bb = dfs(x, nr, nc)
                a += aa
                b += bb
        return a, b

    for r in range(R):
        for c in range(C):
            if inps[r][c][1]==0:
                p, a = dfs(inps[r][c][0], r,c)
                # print(inps[r][c][0], p, a)
                ans += p * a

    print(ans)