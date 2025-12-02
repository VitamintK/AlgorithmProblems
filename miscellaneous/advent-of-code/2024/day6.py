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
    for r, row in enumerate(inps):
        if '^' in row:
            start = (r, row.index('^'))
    
    dr, dc = -1, 0
    
    r, c = start
    pos = set()
    pos.add((r, c))
    while True:
        nr, nc = r+dr, c+dc
        if not is_grid_valid(len(inps), len(inps[0]), nr, nc):
            break
        if inps[nr][nc] == '#':
            dr, dc = dirs[(dirs.index((dr,dc))+1) % 4]
        else:
            r, c = nr, nc
        pos.add((r, c))

    print(len(pos))
else:
    ans = 0
    inpss = []
    while True:
        try:
            inpss.append(input())
        except EOFError:
            break
    for r, row in enumerate(inpss):
        if '^' in row:
            start = (r, row.index('^'))
    
    for R in range(len(inpss)):
        for C in range(len(inpss[0])):
            inps = [[x for x in r] for r in inpss]
            inps[R][C] = '#'

            dr, dc = -1, 0
            
            r, c = start
            pos = set()
            pos.add((r, c))
            seen = set()
            seen.add((r, c, (dr, dc)))
            while True:
                nr, nc = r+dr, c+dc
                if not is_grid_valid(len(inps), len(inps[0]), nr, nc):
                    break
                if inps[nr][nc] == '#':
                    dr, dc = dirs[(dirs.index((dr,dc))+1) % 4]
                else:
                    r, c = nr, nc
                pos.add((r, c))
                if (r, c, (dr, dc)) in seen:
                    ans += 1
                    break
                seen.add((r, c, (dr, dc)))

    print(ans)