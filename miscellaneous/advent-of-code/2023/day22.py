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
    i = 0
    while True:
        try:
            a,b = input().split('~')
            a = get_ints(a)
            b = get_ints(b)
            inps.append((a, b, i))
            i += 1
        except EOFError:
            break
    # R, C = len(inps), len(inps[0])
    inps.sort(key=lambda x: x[0][2])
    inps2 = []
    children = defaultdict(list)
    parents = defaultdict(list)
    for low, high, i1 in inps:
        z = 1
        for l2, h2, i2 in sorted(inps2, key=lambda x: x[1][2], reverse=True):
            if not (min(h2[0], high[0]) < max(low[0], l2[0])) and not (min(h2[1], high[1]) < max(low[1], l2[1])):
                if h2[2] + 1 < z:
                    break
                z = h2[2] + 1
                children[i1].append(i2)
                parents[i2].append(i1)
        lo = (low[0], low[1], z)
        hi = (high[0], high[1], z + high[2] - low[2])
        inps2.append((lo, hi, i1))
        
    for i in range(len(inps)):
        if i not in parents:
            ans += 1
        else:
            for p in parents[i]:
                if len(children[p]) == 1:
                    break
            else:
                ans += 1

    print(ans)
else:
    ans = 0
    inps = []
    i = 0
    while True:
        try:
            a,b = input().split('~')
            a = get_ints(a)
            b = get_ints(b)
            inps.append((a, b, i))
            i += 1
        except EOFError:
            break
    # R, C = len(inps), len(inps[0])
    inps.sort(key=lambda x: x[0][2])
    def go(inps):
        X = 0
        inps2 = []
        children = defaultdict(list)
        parents = defaultdict(list)
        for low, high, i1 in inps:
            z = 1
            for l2, h2, i2 in sorted(inps2, key=lambda x: x[1][2], reverse=True):
                if not (min(h2[0], high[0]) < max(low[0], l2[0])) and not (min(h2[1], high[1]) < max(low[1], l2[1])):
                    if h2[2] + 1 < z:
                        break
                    z = h2[2] + 1
                    children[i1].append(i2)
                    parents[i2].append(i1)
            if z < low[2]:
                X += 1
            lo = (low[0], low[1], z)
            hi = (high[0], high[1], z + high[2] - low[2])
            inps2.append((lo, hi, i1))
        return X, inps2, children, parents
    def go2(inps, children, parents, i):
        parents = parents.copy()
        children = children.copy()
        changed = set()
        def dfs(x):
            ...
            # ok I started to code the solution for Part 2 but then I checked and the brute-force that I coded up originally
            # and started to run actually finished, even with python. So I just submitted that and won't finish the proper solution.
            # the brute-force solution is the `go` approach you can see below. I was going to do a smarter `go2` solution
            # using the dependency DAG.
            if x not in parents:
                return 0
            for p in parents[x]:
                dfs(p)
        return dfs(i)
    _, inps, children, parents = go(inps)
    for i in range(len(inps)):
        inps2 = inps[:]
        inps2.pop(i)
        X, _ = go(inps2)
        ans += X

    print(ans)