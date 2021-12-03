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

if False:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    N = len(inps)
    n = len(inps[0])
    bits = ''
    bits2 = ''
    for i in range(n):
        zs = 0
        for j in range(N):
            if inps[j][i] == '0':
                zs += 1
            else:
                zs -=1
        if zs > 0:
            bits += '0'
            bits2 += '1'
        else:
            bits += '1'
            bits2 += '0'
    
    gamma = int(bits, 2)
    eps = int(bits2, 2)
    print(gamma * eps)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    N = len(inps)
    n = len(inps[0])
    indices = list(range(N))
    cur = 0
    while len(indices) > 1:
        zcount = 0
        zs = []
        os = []
        for j in indices:
            if inps[j][cur] == '0':
                zcount += 1
                zs.append(j)
            else:
                zcount -=1
                os.append(j)
        if zcount > 0:
            indices = zs
        elif zcount < 0:
            indices = os
        else:
            indices = os
        cur += 1
    assert len(indices) == 1
    oxy = int(inps[indices[0]], 2)

    indices = list(range(N))
    cur = 0
    while len(indices) > 1:
        zcount = 0
        zs = []
        os = []
        for j in indices:
            if inps[j][cur] == '0':
                zcount += 1
                zs.append(j)
            else:
                zcount -=1
                os.append(j)
        if zcount < 0:
            indices = zs
        elif zcount > 0:
            indices = os
        else:
            indices = zs
        cur += 1
    assert len(indices) == 1
    co2 = int(inps[indices[0]], 2)
    print(oxy * co2)