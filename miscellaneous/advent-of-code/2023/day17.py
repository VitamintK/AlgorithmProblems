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

"""Wow, sad one today because I finished this pretty quickly but then spent minutes and minutes debugging
and stupidly didn't think to just read the problem statement a bit more carefully, where I would have realized
that you're not supposed to count (0,0) :(

First day using my new AOC CLI tool though, which was fun!
"""

PART = 1
# PART = 2
if PART == 1:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    
    def dfs(r, c, dr, dc, i):
        pass
    pq = [(0, 0, 0, 0, 0, 0, None)]
    been = dict()
    while len(pq) > 0:
        ex = heappop(pq)
        x, r, c, dr, dc, i, prev = ex
        # print(ex)
        y = (r, c, dr, dc, i)
        if y in been:
            continue
        been[y] = prev
        if r ==len(inps)-1 and c == len(inps[0])-1:
            ans = x
            break
        for ddr, ddc in dirs:
            nr, nc = r+ddr, c+ddc
            if not is_grid_valid(len(inps), len(inps[0]), nr, nc):
                continue
            if ddr == -dr and ddc == -dc:
                continue
            if (ddr != dr or ddc != dc) and i < 4 and not (dr==0 and dc==0):
                continue
            ii = i+1 if ddr == dr and ddc == dc else 1
            if ii > 10:
                continue
            heappush(pq, (x + int(inps[nr][nc]), nr, nc, ddr, ddc, ii, y))
    
    while True:
        y = been[y]
        r, c, dr, dc, i = y
        print(r,c)
        if r == 0 and c == 0:
            break

    

    print(ans)
else:
    pass