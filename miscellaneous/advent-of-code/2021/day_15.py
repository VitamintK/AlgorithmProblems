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

if True:
    ans = 0
    inpss = []
    while True:
        try:
            inpss.append(input())
        except EOFError:
            break
    inps = []
    for row in inpss:
        r = [int(x) for x in row]
        rs = r[:]
        for i in range(1,5):
            for j in r:
                rs.append((j + i)%9 if (j+i)%9!=0 else 9)
        inps.append(rs)
    inpss = []
    for i in range(5):
        for r in inps:
            inpss.append([(x+i)%9 if (x+i)%9!=0 else 9 for x in r])
    inps = inpss
    for r in inps:
        print(r)
    n = len(inps)
    m = len(inps[0])
    print(n,m)
    pq = [(0, 0,0)]
    visited = set()
    while len(pq) > 0:
        cost, r, c = heappop(pq)
        # print(cost, r, c)
        if (r,c) == (n-1,m-1):
            print(cost)
            break
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if not is_grid_valid(n,m,nr,nc):
                continue
            if (nr,nc) in visited:
                continue
            visited.add((nr, nc))
            heappush(pq, (cost+int(inps[nr][nc]), nr, nc))

    print(ans)
else:
    pass