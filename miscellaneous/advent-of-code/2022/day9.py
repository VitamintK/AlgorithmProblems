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

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    visited = set()
    visited.add((0,0))
    knots = [[0,0] for i in range(10)]
    for inp in inps:
        d, x = inp.split()
        dr, dc = dirs[directions.index(d)]
        x = int(x)
        for i in range(x):
            knots[0][0] += dr
            knots[0][1] += dc
            for j in range(1,10):
                hr = knots[j-1][0]
                hc = knots[j-1][1]
                tr = knots[j][0]
                tc = knots[j][1]
                if hr != tr and hc != tc and abs(hr-tr)+abs(hc-tc)>2:
                    offr = (hr-tr)/abs(hr-tr)
                    offc = (hc-tc)/abs(hc-tc)
                    tr += offr
                    tc += offc
                elif hr==tr and abs(hc-tc)>1:
                    offc = (hc-tc)/abs(hc-tc)
                    tc += offc
                elif hc==tc and abs(hr-tr)>1:
                    offr = (hr-tr)/abs(hr-tr)
                    tr += offr
                knots[j][0] = tr
                knots[j][1] = tc
            visited.add((tr,tc))
    print(visited)
    

    print(len(visited))
else:
    pass