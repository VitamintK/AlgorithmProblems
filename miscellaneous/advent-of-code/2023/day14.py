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

if False:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for c in range(len(inps[0])):
        cnt = 0
        for r in range(len(inps)):
            if inps[r][c] == 'O':
                ans += len(inps) - cnt
                cnt += 1
            if inps[r][c] == '#':
                cnt = r + 1
    print(ans)
else:
    def dbg(inps):
        for r in inps:
            print(''.join(r))
        print()
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    def hsh(ls):
        # print(ls)
        return hash(tuple(tuple(l) for l in ls))
    inps = np.array([list(i) for i in inps])
    seen = dict()
    vals = []
    for i in range(1000000000):
        if hsh(inps) in seen:
            break
        seen[hsh(inps)] = i
        for x in range(4):
            ans = 0
            inps = np.rot90(inps, x%4, axes=(1, 0))
            copy = np.copy(inps)
            Os = []
            for c in range(len(inps[0])):
                cnt = 0
                for r in range(len(inps)):
                    if inps[r][c] == 'O':
                        ans += len(inps) - cnt
                        Os.append((cnt,c))
                        copy[r][c] = '.'
                        cnt += 1
                    if inps[r][c] == '#':
                        cnt = r + 1
            for o in Os:
                copy[o[0]][o[1]] = 'O'
            copy = np.rot90(copy, x%4, axes=(0, 1))
            inps = copy
            # dbg(inps)
        ans = 0
        for r in range(len(inps)):
            for c in range(len(inps[0])):
                if inps[r][c] == 'O':
                    ans += len(inps) - r
        vals.append(ans)
    cycle_len = seen[hsh(inps)] - i
    N = 1000000000 - 1
    print(vals[(N - seen[hsh(inps)])%cycle_len])
    print(vals)
        

    # print(ans)